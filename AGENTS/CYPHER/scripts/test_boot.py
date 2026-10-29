#!/usr/bin/env python3
"""
test_boot.py — drills for AGENTS/CYPHER/boot.py (CHECK_STANDARD §3: watch the alert line on a
capable case AND the clean line on a clean case; watch every failure path return rc 2).

Each test copies the desk into a throwaway directory (with the repo's scripts/ linked in, so
leg 1's shared staleness tool still runs), edits the COPY, and runs boot.py there against
fixture files — no network, no real-file writes. The class teardown asserts every real desk
file is md5-unchanged.

Run from anywhere:
  python3 "$(git rev-parse --show-toplevel)/AGENTS/CYPHER/scripts/test_boot.py"
  python3 -m unittest discover -s AGENTS/CYPHER/scripts -p 'test_*.py'   (from the repo root)

Built by DAEDALUS 2026-10-22 (moved from the build session's scratchpad drill suite, 22 drills,
plus the matrix/map leg added the same evening).
"""

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

DESK = Path(__file__).resolve().parents[1]
ROOT = DESK.parents[1]

KEV_OK = {"catalogVersion": "2026.10.21", "dateReleased": "2026-10-21T14:04:39Z", "count": 1,
          "vulnerabilities": [{"cveID": "CVE-2020-0001", "dateAdded": "2020-01-01"}]}
KEV_LISTED = dict(KEV_OK, vulnerabilities=[{"cveID": "CVE-2026-109618", "dateAdded": "2026-10-24"}])
KEV_EMPTY = dict(KEV_OK, vulnerabilities=[])
KEV_STALE = dict(KEV_OK, dateReleased="2026-09-01T00:00:00Z")
_OLD = {"_source": {"file_date": "2026-09-23", "display_names": ["Astrana Health"]}}
_NEW = {"_source": {"file_date": "2026-10-21", "display_names": ["Example Bancorp (EXB)"]}}
ED_OK = {"hits": {"total": {"value": 1}, "hits": [_OLD]}}
ED_ZERO = {"hits": {"total": {"value": 0}, "hits": []}}
ED_RECENT = {"hits": {"total": {"value": 3}, "hits": [_NEW, _NEW, _OLD]}}
ED_TRUNC = {"hits": {"total": {"value": 150}, "hits": [_OLD]}}
_801_NEW = {"_source": {"file_date": "2026-10-22", "items": ["8.01"], "display_names": ["Quest Diagnostics (DGX)"]}}
_801_EARN = {"_source": {"file_date": "2026-10-22", "items": ["2.02", "9.01"], "display_names": ["Earnings Corp (ERN)"]}}
_801_ABS = {"_source": {"file_date": "2026-10-21", "items": ["1.01", "8.01", "9.01"], "display_names": ["Auto Lease Trust"]}}
_801_OLD = {"_source": {"file_date": "2026-09-10", "items": ["8.01"], "display_names": ["Old Co"]}}
E801_OK = {"hits": {"total": {"value": 2}, "hits": [_801_EARN, _801_OLD]}}
E801_HIT = {"hits": {"total": {"value": 4}, "hits": [_801_NEW, _801_NEW, _801_EARN, _801_ABS]}}
E801_ZERO = {"hits": {"total": {"value": 0}, "hits": []}}
# Leg 9 document drills (CYPHER_EDGAR801_DOCDIR): the matched document is read for incident wording.
_801_DOC = lambda fname, name: {"_id": f"0000000000-26-000001:{fname}", "_source": {
    "file_date": "2026-10-22", "items": ["8.01", "9.01"], "ciks": ["0000000001"], "display_names": [name]}}
E801_DOCS = {"hits": {"total": {"value": 3}, "hits": [_801_DOC("boiler.htm", "Boiler Bancorp"),
                                                      _801_DOC("fls_only.htm", "Vendor Hit Bancorp"),
                                                      _801_DOC("missing.htm", "Unread Corp")]}}
DOC_BOILER = ("<p>Item 8.01 Other Events. The Board declared a dividend of $0.28.</p><p>Forward-Looking Statements. "
              "Risks include legal proceedings; risks associated with cybersecurity threats, data breaches, ransomware "
              "attacks, or other failures in our systems.</p>")
DOC_FLS_ONLY = ("<p>Item 8.01 Other Events. Our audit provider has discovered a data security incident in which an "
                "unauthorized actor accessed and acquired certain files, including Bank customer data.</p>"
                + "<p>" + "The Bank's own systems and operations were not involved. " * 12 + "</p>"   # >300 chars, as in the real filing
                "<p>Forward-Looking Statements. Factors include the potential misuse of affected data by the threat "
                "actor or other parties and additional cybersecurity incidents.</p>")   # SR Bancorp 2026-07-10 shape
ED_ITEMS = {"hits": {"total": {"value": 2}, "hits": [
    {"_source": {"file_date": "2026-10-21", "items": ["5.02", "8.01", "9.01"], "display_names": ["Charter Text Corp"]}},
    {"_source": {"file_date": "2026-10-21", "items": ["1.05", "9.01"], "display_names": ["Real Incident Bank"]}}]}}
TODAY = "2026-10-22"   # the build date: seeded State_As_Of / Last_Checked cells are fresh on it


def _md5s():
    return {p: hashlib.md5(p.read_bytes()).hexdigest()
            for p in sorted(DESK.rglob("*")) if p.is_file() and "__pycache__" not in p.parts}


class BootDrills(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.before = _md5s()
        cls.tmp = Path(tempfile.mkdtemp(prefix="cypher_boot_drill_"))
        cls.fx = cls.tmp / "fixtures"
        cls.fx.mkdir()
        for name, obj in (("kev_ok", KEV_OK), ("kev_listed", KEV_LISTED), ("kev_empty", KEV_EMPTY),
                          ("kev_stale", KEV_STALE), ("ed_ok", ED_OK), ("ed_zero", ED_ZERO),
                          ("ed_recent", ED_RECENT), ("ed_trunc", ED_TRUNC), ("e801_ok", E801_OK),
                          ("e801_hit", E801_HIT), ("e801_zero", E801_ZERO), ("e801_docs", E801_DOCS),
                          ("ed_items", ED_ITEMS),
                          ("kev_seen", dict(KEV_OK, vulnerabilities=[{"cveID": "CVE-2026-114625", "dateAdded": "2026-10-23"}]))):
            (cls.fx / f"{name}.json").write_text(json.dumps(obj), encoding="utf-8")
        cls.docs = cls.tmp / "docs"
        cls.docs.mkdir()
        (cls.docs / "boiler.htm").write_text(DOC_BOILER, encoding="utf-8")
        (cls.docs / "fls_only.htm").write_text(DOC_FLS_ONLY, encoding="utf-8")

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)
        assert _md5s() == cls.before, "REAL CYPHER FILES CHANGED DURING DRILLS"

    # ---- helpers -------------------------------------------------------------------------
    def fresh(self):
        root = self.tmp / f"root_{self._testMethodName}"
        if root.exists():
            shutil.rmtree(root)
        (root / "AGENTS").mkdir(parents=True)
        shutil.copytree(DESK, root / "AGENTS" / "CYPHER", ignore=shutil.ignore_patterns("__pycache__"))
        (root / "scripts").symlink_to(ROOT / "scripts")
        return root / "AGENTS" / "CYPHER"

    def edit(self, d, rel, old, new, count=1):
        p = d / rel
        t = p.read_text(encoding="utf-8")
        self.assertIn(old, t, f"fixture edit anchor missing in {rel}")
        p.write_text(t.replace(old, new, count), encoding="utf-8")

    def score_all(self, d, score="2"):
        p = d / "workbook" / "VX.tsv"
        p.write_text(p.read_text(encoding="utf-8").replace("\tUNKNOWN\tUNKNOWN — not scored at build\t",
                                                           f"\t{score}\tdrill\t"), encoding="utf-8")

    def run_boot(self, d, env=None, args=(), today=TODAY):
        e = {k: v for k, v in os.environ.items()
             if k not in ("CYPHER_BOOT_TODAY", "CYPHER_KEV_FILE", "CYPHER_EDGAR_FILE", "CYPHER_EDGAR801_FILE",
                          "CYPHER_EDGAR801_DOCDIR")}
        e.update({"CYPHER_KEV_FILE": str(self.fx / "kev_ok.json"),
                  "CYPHER_EDGAR_FILE": str(self.fx / "ed_ok.json"),
                  "CYPHER_EDGAR801_FILE": str(self.fx / "e801_ok.json")})
        if today:
            e["CYPHER_BOOT_TODAY"] = today
        e.update(env or {})
        p = subprocess.run([sys.executable, str(d / "boot.py"), *args], capture_output=True,
                           text=True, env=e, cwd="/")
        return p.returncode, p.stdout + p.stderr

    def assertBoot(self, d, rc, *needles, env=None, args=(), today=TODAY):
        got, out = self.run_boot(d, env=env, args=args, today=today)
        if rc is not None:
            self.assertEqual(got, rc, out)
        for n in needles:
            self.assertIn(n, out, out)
        return out

    def stamp(self, d, rel, col, value=TODAY):
        """Set every data row's <col> to <value> in the COPY (the clean fixture must not depend on
        which live cells happen to be fresh — a single-row anchor broke all drills on 2026-10-23)."""
        p = d / rel
        lines = p.read_text(encoding="utf-8").split("\n")
        hi = next(i for i, l in enumerate(lines) if l.split("\t")[0] in ("ID", "Wave_ID", "Row"))
        hdr = lines[hi].split("\t")
        c = hdr.index(col)
        for i in range(hi + 1, len(lines)):
            r = lines[i].split("\t")
            if len(r) == len(hdr):
                r[c] = value
                lines[i] = "\t".join(r)
        p.write_text("\n".join(lines), encoding="utf-8")

    def set_cell(self, d, rel, key, col, value):
        """Set one cell by row key (first column, or Wave_ID+Row for the watch) in the COPY — never
        anchor a drill on a live cell's current text (three drills rotted that way by 2026-10-29)."""
        p = d / rel
        lines = p.read_text(encoding="utf-8").split("\n")
        hi = next(i for i, l in enumerate(lines) if l.split("\t")[0] in ("ID", "Wave_ID", "Row"))
        hdr = lines[hi].split("\t")
        for i in range(hi + 1, len(lines)):
            r = lines[i].split("\t")
            k = f"{r[0]} {r[1]}" if hdr[0] == "Wave_ID" and len(r) > 1 else r[0]
            if len(r) == len(hdr) and k == key:
                r[hdr.index(col)] = value
                lines[i] = "\t".join(r)
                p.write_text("\n".join(lines), encoding="utf-8")
                return
        self.fail(f"row {key} not found in {rel}")

    def first_row(self, d, rel, col, value):
        rows = [l.split("\t") for l in (d / rel).read_text(encoding="utf-8").split("\n") if not l.startswith("#")]
        hdr = rows[0]
        return next(r[0] for r in rows[1:] if len(r) == len(hdr) and r[hdr.index(col)] == value)

    def clean_copy(self):
        d = self.fresh()
        self.stamp(d, "workbook/INCIDENTS.tsv", "Last_Checked")
        self.stamp(d, "workbook/ESCALATION_WATCH.tsv", "State_As_Of")
        self.score_all(d)
        return d

    # ---- clean path ----------------------------------------------------------------------
    def test_clean_all_quiet(self):
        self.assertBoot(self.clean_copy(), 0, "CYPHER boot: all quiet", "✓ enums valid",
                        "✓ every vector scored", "/40 (raw", "watched CVE(s) absent",
                        "✓ no Item 1.05", "✓ every open row checked")

    # ---- incidents -----------------------------------------------------------------------
    def test_incident_recheck_alert_on_seed(self):
        d = self.clean_copy()   # every row stamped TODAY; 15 days later the REPORTED rows are due
        rid = self.first_row(d, "workbook/INCIDENTS.tsv", "Event_State", "REPORTED")
        self.assertBoot(d, 1, "REPORTED/ATTEMPTS-ONLY row(s) last checked >14d ago", rid, today="2026-11-06")

    def test_incident_blank_date_on_confirmed_row(self):
        d = self.clean_copy()   # 2026-10-29 fix: a CONFIRMED row with no Last_Checked used to pass silently
        rid = self.first_row(d, "workbook/INCIDENTS.tsv", "Event_State", "CONFIRMED")
        self.set_cell(d, "workbook/INCIDENTS.tsv", rid, "Last_Checked", "")
        self.assertBoot(d, 1, f"{rid}: blank or unparsable Last_Checked on a CONFIRMED row")
        self.set_cell(d, "workbook/INCIDENTS.tsv", rid, "Event_State", "SUPERSEDED")   # dead rows carry no clock
        self.assertBoot(d, 0, "every live row dated")

    def test_incident_bad_enum(self):
        d = self.clean_copy(); self.edit(d, "workbook/INCIDENTS.tsv", "\tOT-PHYSICAL\t", "\tOT\t")
        self.assertBoot(d, 1, "Class 'OT' is not in the declared enum")

    # ---- matrix + map --------------------------------------------------------------------
    def test_unscored_matrix_is_review(self):
        d = self.clean_copy(); self.stamp(d, "workbook/VX.tsv", "Score", "UNKNOWN")
        self.assertBoot(d, 1, "UNSCORED: 9 of 9 vector(s)", "composite UNKNOWN")

    def test_thermometer_excluded_from_composite(self):
        d = self.clean_copy()
        self.stamp(d, "workbook/VX.tsv", "Score", "2")            # 8 MECHANISM x 2 = 16; the thermometer must not add
        self.assertBoot(d, 0, "Total 16/40")
        self.edit(d, "workbook/VX.tsv", "\tTHERMOMETER\t2\t", "\tTHERMOMETER\t5\t")
        self.assertBoot(d, 0, "Total 16/40")

    def test_bad_score_and_kind(self):
        d = self.clean_copy()
        self.edit(d, "workbook/VX.tsv", "VX-CYP-01\tBank / core-vendor compromise\tMECHANISM\t2\t",
                  "VX-CYP-01\tBank / core-vendor compromise\tMECHANSIM\t7\t")
        self.assertBoot(d, 1, "VX-CYP-01: Kind 'MECHANSIM'", "VX-CYP-01: Score '7'")

    def test_flow_bad_state_and_orphan(self):
        d = self.clean_copy()
        self.edit(d, "workbook/FLOW.tsv", "FL-CYP-02\tVX-CYP-01\t", "FL-CYP-02\tVX-CYP-99\t")
        self.edit(d, "workbook/FLOW.tsv", "\tNOT-OBSERVED\t", "\tREFUTED\t")
        self.assertBoot(d, 1, "FL-CYP-02: Vector 'VX-CYP-99' has no VX row", "is not in the declared FLOW enum")

    def test_matrix_missing_is_fail(self):
        d = self.clean_copy(); (d / "workbook" / "VX.tsv").unlink()
        self.assertBoot(d, 2, "matrix: workbook/VX.tsv MISSING")

    # ---- KEV -----------------------------------------------------------------------------
    def test_kev_listed(self):
        self.assertBoot(self.clean_copy(), 1, "KEV LISTED: CVE-2026-109618", "FIRED CANDIDATE",
                        env={"CYPHER_KEV_FILE": str(self.fx / "kev_listed.json")})

    def test_kev_seen_quiets_matching_listing_only(self):
        d = self.clean_copy()   # live 014 carries KEV-SEEN:CVE-2026-114625@2026-10-23
        env = {"CYPHER_KEV_FILE": str(self.fx / "kev_seen.json")}
        self.assertBoot(d, 0, "already adjudicated", "CVE-2026-114625@2026-10-23", env=env)
        self.set_cell(d, "workbook/INCIDENTS.tsv", "CYB-INC-014", "Watch_Keys", "KEV:CVE-2026-114625;KEV-SEEN:CVE-2026-114625@2026-10-20")
        self.assertBoot(d, 1, "KEV LISTED: CVE-2026-114625", "KEV-SEEN:CVE-2026-114625@2026-10-23", env=env)   # date changed
        self.set_cell(d, "workbook/INCIDENTS.tsv", "CYB-INC-014", "Watch_Keys", "KEV:CVE-2026-114625")
        self.assertBoot(d, 1, "KEV LISTED: CVE-2026-114625", env=env)                                          # no token
        self.set_cell(d, "workbook/INCIDENTS.tsv", "CYB-INC-014", "Watch_Keys", "KEV:CVE-2026-114625;KEV-SEEN:CVE-2026-114625")
        self.assertBoot(d, 1, "malformed KEV-SEEN token", env=env)

    def test_kev_fetch_fail(self):
        self.assertBoot(self.clean_copy(), 2, "KEV: fetch/parse FAILED", "do NOT read as 'not listed'",
                        env={"CYPHER_KEV_FILE": "/nonexistent.json"})

    def test_kev_empty_catalog(self):
        self.assertBoot(self.clean_copy(), 2, "0 vulnerabilities", env={"CYPHER_KEV_FILE": str(self.fx / "kev_empty.json")})

    def test_kev_stale_catalog(self):
        self.assertBoot(self.clean_copy(), 1, "the feed itself may be stale", env={"CYPHER_KEV_FILE": str(self.fx / "kev_stale.json")})

    def test_kev_malformed_key(self):
        d = self.clean_copy(); self.edit(d, "workbook/INCIDENTS.tsv", "KEV:CVE-2026-114625", "KEV:CVE-26-1")
        self.assertBoot(d, 1, "malformed KEV key 'CVE-26-1'")

    def test_terminal_rows_drop_kev_keys(self):
        d = self.clean_copy()
        self.set_cell(d, "workbook/ESCALATION_WATCH.tsv", "WAVE-2026-10 2", "State", "FIRED")
        out = self.assertBoot(d, 0, "FIRED 1", "1 FIRED row(s)", "watched CVE(s) absent from KEV")
        self.assertIn("CVE-2026-109618", out)                    # incident 007 still carries the wave CVEs
        self.set_cell(d, "workbook/INCIDENTS.tsv", "CYB-INC-007", "Event_State", "FALSE")
        out = self.assertBoot(d, 0, "watched CVE(s) absent from KEV", "CVE-2026-114625")
        kev_line = next(l for l in out.splitlines() if "absent from KEV" in l)
        self.assertNotIn("CVE-2026-109618", kev_line)            # dropped with the FALSE row and the FIRED watch row

    # ---- EDGAR ---------------------------------------------------------------------------
    def test_edgar_zero_control_is_fail(self):
        self.assertBoot(self.clean_copy(), 2, "positive-control population is empty",
                        env={"CYPHER_EDGAR_FILE": str(self.fx / "ed_zero.json")})

    def test_edgar_recent_hit_deduplicated(self):
        out = self.assertBoot(self.clean_copy(), 1, "8-K Item 1.05 2026-10-21: Example Bancorp",
                              env={"CYPHER_EDGAR_FILE": str(self.fx / "ed_recent.json")})
        self.assertEqual(out.count("Example Bancorp"), 1, out)

    def test_edgar_items_without_105_not_review(self):
        out = self.assertBoot(self.clean_copy(), 1, "Charter Text Corp — items 5.02, 8.01, 9.01, NOT filed under Item 1.05",
                              "8-K Item 1.05 2026-10-21: Real Incident Bank", env={"CYPHER_EDGAR_FILE": str(self.fx / "ed_items.json")})
        self.assertNotIn("⚠️ 8-K Item 1.05 2026-10-21: Charter Text Corp", out)

    def test_edgar_truncated(self):
        self.assertBoot(self.clean_copy(), 1, "150 filings but only 1 returned",
                        env={"CYPHER_EDGAR_FILE": str(self.fx / "ed_trunc.json")})

    def test_edgar_fetch_fail(self):
        self.assertBoot(self.clean_copy(), 2, "8-K Item 1.05: fetch/parse FAILED", env={"CYPHER_EDGAR_FILE": "/nonexistent.json"})

    def test_offline_reports_skipped_legs(self):
        self.assertBoot(self.clean_copy(), 1, "KEV key(s)", "NOT RUN (--offline): 8-K Item 1.05",
                        "NOT RUN (--offline): 8-K Item 8.01", args=("--offline",))

    # ---- EDGAR 8.01 cyber (leg 9) ---------------------------------------------------------
    def test_801_clean(self):
        self.assertBoot(self.clean_copy(), 0, "✓ no 8.01 cyber-term 8-K since", "control population 2")

    def test_801_hit_filtered_and_deduplicated(self):
        out = self.assertBoot(self.clean_copy(), 1, "8-K 8.01 cyber-term 2026-10-22: Quest Diagnostics",
                              env={"CYPHER_EDGAR801_FILE": str(self.fx / "e801_hit.json")})
        self.assertEqual(out.count("Quest Diagnostics"), 1, out)
        self.assertNotIn("Earnings Corp", out, out)
        self.assertNotIn("Auto Lease Trust", out, out)

    def test_801_boilerplate_vs_incident_vs_unread(self):
        out = self.assertBoot(self.clean_copy(), 1,
                              "ℹ️ 8-K 8.01 cyber-term 2026-10-22: Boiler Bancorp — boilerplate only",
                              "⚠️ 8-K 8.01 cyber-term 2026-10-22: Vendor Hit Bancorp — incident narrative in the document",
                              "⚠️ 8-K 8.01 cyber-term 2026-10-22: Unread Corp — document unread",
                              env={"CYPHER_EDGAR801_FILE": str(self.fx / "e801_docs.json"),
                                   "CYPHER_EDGAR801_DOCDIR": str(self.docs)})
        self.assertNotIn("⚠️ 8-K 8.01 cyber-term 2026-10-22: Boiler Bancorp", out)

    def test_801_zero_control_is_fail(self):
        self.assertBoot(self.clean_copy(), 2, "8-K 8.01 cyber: 0 term hits",
                        env={"CYPHER_EDGAR801_FILE": str(self.fx / "e801_zero.json")})

    def test_801_fetch_fail(self):
        self.assertBoot(self.clean_copy(), 2, "8-K 8.01 cyber: fetch/parse FAILED",
                        env={"CYPHER_EDGAR801_FILE": "/nonexistent.json"})

    # ---- escalation watch ----------------------------------------------------------------
    def test_watch_stale(self):
        self.assertBoot(self.clean_copy(), 1, "RE-CHECK DUE: WAVE-2026-10 row 1", "RE-CHECK DUE: WAVE-2026-10 row 9",
                        "RE-CHECK DUE: WAVE-2026-10 row 5", today="2026-11-01")

    def test_watch_bad_token(self):
        d = self.clean_copy(); self.edit(d, "workbook/ESCALATION_WATCH.tsv", "\tNOT-FIRED\t", "\tTRIGGERED\t")
        self.assertBoot(d, 1, "State 'TRIGGERED' is not a Class 2 token")

    def test_watch_empty_and_missing(self):
        d = self.clean_copy()
        p = d / "workbook" / "ESCALATION_WATCH.tsv"
        p.write_text("\n".join(l for l in p.read_text(encoding="utf-8").splitlines()
                               if l.startswith("#") or l.startswith("Wave_ID")) + "\n", encoding="utf-8")
        self.assertBoot(d, 1, "0 watch rows")
        p.unlink()
        self.assertBoot(d, 2, "escalation watch: workbook/ESCALATION_WATCH.tsv MISSING")

    # ---- catalysts + predictions ---------------------------------------------------------
    def test_catalyst_window(self):
        d = self.clean_copy()
        first = min(l.split("\t")[0] for l in (d / "docket" / "CATALYSTS.tsv").read_text(encoding="utf-8").splitlines()[1:] if l)
        day_before = (__import__("datetime").date.fromisoformat(first) - __import__("datetime").timedelta(days=1)).isoformat()
        self.assertBoot(d, 1, f"in 1d: {first}", today=day_before)

    def test_catalyst_empty_forward(self):
        self.assertBoot(self.clean_copy(), 1, "EMPTY-FORWARD", "past-dated row(s)", today="2028-01-01")

    def test_prediction_due(self):
        d = self.clean_copy()
        p = d / "workbook" / "PREDICTIONS.tsv"
        p.write_text(p.read_text(encoding="utf-8") + "CYP-01\t2026-10-23\tTest row\t50%\t1w\t2026-10-30\tOPEN\t\t\t\t\n", encoding="utf-8")
        self.assertBoot(d, 1, "DUE: CYP-01", today="2026-10-31")


if __name__ == "__main__":
    unittest.main(verbosity=2)
