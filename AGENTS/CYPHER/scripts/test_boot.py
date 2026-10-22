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
                          ("ed_recent", ED_RECENT), ("ed_trunc", ED_TRUNC)):
            (cls.fx / f"{name}.json").write_text(json.dumps(obj), encoding="utf-8")

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
             if k not in ("CYPHER_BOOT_TODAY", "CYPHER_KEV_FILE", "CYPHER_EDGAR_FILE")}
        e.update({"CYPHER_KEV_FILE": str(self.fx / "kev_ok.json"),
                  "CYPHER_EDGAR_FILE": str(self.fx / "ed_ok.json")})
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

    def clean_copy(self):
        d = self.fresh()
        self.edit(d, "workbook/INCIDENTS.tsv", "\t2026-10-02\tNo attribution.", "\t2026-10-22\tNo attribution.")
        self.score_all(d)
        return d

    # ---- clean path ----------------------------------------------------------------------
    def test_clean_all_quiet(self):
        self.assertBoot(self.clean_copy(), 0, "CYPHER boot: all quiet", "✓ enums valid",
                        "✓ every vector scored", "Total 16/40", "✓ 3 watched CVE(s) absent",
                        "✓ no Item 1.05", "✓ every open row checked")

    # ---- incidents -----------------------------------------------------------------------
    def test_incident_recheck_alert_on_seed(self):
        d = self.fresh(); self.score_all(d)
        self.assertBoot(d, 1, "RE-CHECK DUE: 1 REPORTED/ATTEMPTS-ONLY", "CYB-INC-001")

    def test_incident_bad_enum(self):
        d = self.clean_copy(); self.edit(d, "workbook/INCIDENTS.tsv", "\tOT-PHYSICAL\t", "\tOT\t")
        self.assertBoot(d, 1, "Class 'OT' is not in the declared enum")

    # ---- matrix + map --------------------------------------------------------------------
    def test_unscored_matrix_is_review(self):
        d = self.fresh()
        self.edit(d, "workbook/INCIDENTS.tsv", "\t2026-10-02\tNo attribution.", "\t2026-10-22\tNo attribution.")
        self.assertBoot(d, 1, "UNSCORED: 9 of 9 vector(s)", "composite UNKNOWN")

    def test_thermometer_excluded_from_composite(self):
        d = self.clean_copy()
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
        self.edit(d, "workbook/ESCALATION_WATCH.tsv",
                  "\tNOT-FIRED\t2026-10-22\tSCHEDULED\tMACHINE\tWALTER (routing); REGINALD, SHADE, VULCAN",
                  "\tFIRED 2026-10-22\t2026-10-22\tSCHEDULED\tMACHINE\tWALTER (routing); REGINALD, SHADE, VULCAN")
        self.assertBoot(d, 0, "FIRED 1", "1 FIRED row(s)", "✓ 3 watched CVE(s)")   # incident 007 still carries them
        self.edit(d, "workbook/INCIDENTS.tsv", "\tATTEMPTS-ONLY\tPRIMARY-VERIFIED", "\tFALSE\tPRIMARY-VERIFIED")
        self.assertBoot(d, 0, "✓ 1 watched CVE(s) absent from KEV: CVE-2026-114625")

    # ---- EDGAR ---------------------------------------------------------------------------
    def test_edgar_zero_control_is_fail(self):
        self.assertBoot(self.clean_copy(), 2, "positive-control population is empty",
                        env={"CYPHER_EDGAR_FILE": str(self.fx / "ed_zero.json")})

    def test_edgar_recent_hit_deduplicated(self):
        out = self.assertBoot(self.clean_copy(), 1, "8-K Item 1.05 2026-10-21: Example Bancorp",
                              env={"CYPHER_EDGAR_FILE": str(self.fx / "ed_recent.json")})
        self.assertEqual(out.count("Example Bancorp"), 1, out)

    def test_edgar_truncated(self):
        self.assertBoot(self.clean_copy(), 1, "150 filings but only 1 returned",
                        env={"CYPHER_EDGAR_FILE": str(self.fx / "ed_trunc.json")})

    def test_edgar_fetch_fail(self):
        self.assertBoot(self.clean_copy(), 2, "8-K Item 1.05: fetch/parse FAILED", env={"CYPHER_EDGAR_FILE": "/nonexistent.json"})

    def test_offline_reports_skipped_legs(self):
        self.assertBoot(self.clean_copy(), 1, "NOT RUN (--offline): 3 KEV key(s)", "NOT RUN (--offline): 8-K", args=("--offline",))

    # ---- escalation watch ----------------------------------------------------------------
    def test_watch_stale(self):
        self.assertBoot(self.clean_copy(), 1, "RE-CHECK DUE: WAVE-2026-10 row 1", "RE-CHECK DUE: WAVE-2026-10 row 9",
                        "row 5 (ARMED", today="2026-11-01")

    def test_watch_bad_token(self):
        d = self.clean_copy(); self.edit(d, "workbook/ESCALATION_WATCH.tsv", "\tARMED\t", "\tTRIGGERED\t")
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
        self.assertBoot(self.clean_copy(), 1, "in 1d: 2026-10-27", today="2026-10-26")

    def test_catalyst_empty_forward(self):
        self.assertBoot(self.clean_copy(), 1, "EMPTY-FORWARD", "5 past-dated row(s)", today="2027-01-01")

    def test_prediction_due(self):
        d = self.clean_copy()
        p = d / "workbook" / "PREDICTIONS.tsv"
        p.write_text(p.read_text(encoding="utf-8") + "CYP-01\t2026-10-23\tTest row\t50%\t1w\t2026-10-30\tOPEN\t\t\t\t\n", encoding="utf-8")
        self.assertBoot(d, 1, "DUE: CYP-01", today="2026-10-31")


if __name__ == "__main__":
    unittest.main(verbosity=2)
