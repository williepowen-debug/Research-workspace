#!/usr/bin/env python3
"""
test_boot.py — drills for AGENTS/ISHM/boot.py (CHECK_STANDARD §3: watch the alert line on a
capable case AND the clean line on a clean case; watch every failure path return rc 2).

Each leg is driven in-process against a throwaway COPY of the desk: the module's path globals are
re-pointed at the copy, the date is pinned, and FRED is read from fixture CSVs. No network, no
real-file writes; the class teardown asserts every real desk file is md5-unchanged. One subprocess
drill runs main() through the ISHM_HOME / ISHM_FRED_DIR hooks to check the combined verdict.

Run from anywhere:
  python3 "$(git rev-parse --show-toplevel)/AGENTS/ISHM/scripts/test_boot.py"
  python3 -m unittest discover -s AGENTS/ISHM/scripts -p 'test_*.py'   (from the repo root)

Built by DAEDALUS 2026-10-23 (ISHM build).
"""

import hashlib
import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

DESK = Path(__file__).resolve().parents[1]
TODAY = date(2026, 10, 23)


def _md5s():
    return {p: hashlib.md5(p.read_bytes()).hexdigest()
            for p in sorted(DESK.rglob("*")) if p.is_file() and "__pycache__" not in p.parts}


def _load_boot():
    spec = importlib.util.spec_from_file_location("ishm_boot", DESK / "boot.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


CAT_HDR = "date\tevent\twhat_to_check\tthreshold_signal\tpriority\twho_cares\tnotes\tdate_class\n"
PRINT_HDR = ("Series\tRef_Period\tRelease_Date\tVintage\tValue\tUnit\tSA\tPrior\tConsensus\tBasis\tSource\t"
             "Successor_Date\tRead_By\tNotes\n")


def _print_row(series="ISM-MFG", ref="2026-09", rel="2026-10-01", vint="FINAL", basis="PRIMARY-VERIFIED",
               succ="", sa="SA"):
    return "\t".join([series, ref, rel, vint, "50.0", "index", sa, "49.0", "", basis, "ismworld.org",
                      succ, "ISHM", ""]) + "\n"


def _fred_csv(fid, last="2026-09-01", n=36, html=False):
    if html:
        return "<html><body>not here</body></html>\n"
    y, m = map(int, last[:7].split("-"))
    rows = []
    for _ in range(n):
        rows.append(f"{y:04d}-{m:02d}-01,100.0")
        m -= 1
        if m == 0:
            y, m = y - 1, 12
    return f"observation_date,{fid}\n" + "\n".join(reversed(rows)) + "\n"


class BootDrills(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.before = _md5s()
        cls.tmp = Path(tempfile.mkdtemp(prefix="ishm_boot_drill_"))

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)
        assert _md5s() == cls.before, "a drill wrote to a REAL desk file"

    def setUp(self):
        self.home = self.tmp / f"desk_{self._testMethodName}"
        shutil.copytree(DESK, self.home, ignore=shutil.ignore_patterns("__pycache__"))
        self.fred = self.home / "_fred"
        self.fred.mkdir()
        self.b = _load_boot()
        b = self.b
        b.HERE = self.home
        b.PREDICTIONS = self.home / "workbook" / "PREDICTIONS.tsv"
        b.CATALYSTS = self.home / "docket" / "CATALYSTS.tsv"
        b.PRINTS = self.home / "workbook" / "PRINTS.tsv"
        b.PERIMETER = self.home / "PERIMETER.tsv"
        b.VX = self.home / "workbook" / "VX.tsv"
        b.FLOW = self.home / "workbook" / "FLOW.tsv"
        b.TODAY = TODAY
        b.OFFLINE = False
        os.environ["ISHM_FRED_DIR"] = str(self.fred)
        self.write_fred()

    def tearDown(self):
        os.environ.pop("ISHM_FRED_DIR", None)

    # helpers -----------------------------------------------------------------------------
    def write(self, rel, text):
        (self.home / rel).write_text(text, encoding="utf-8")

    def append(self, rel, text):
        with (self.home / rel).open("a", encoding="utf-8") as f:
            f.write(text)

    def write_fred(self, **kw):
        for fid in self.b.FRED_SERIES.values():
            (self.fred / f"{fid}.csv").write_text(_fred_csv(fid, **kw), encoding="utf-8")

    def cats(self, *rows):
        self.write("docket/CATALYSTS.tsv", CAT_HDR + "".join("\t".join(r) + "\n" for r in rows))

    def run_leg(self, name):
        rc, lines = getattr(self.b, name)()
        return rc, "\n".join(lines)

    # 2. predictions -----------------------------------------------------------------------
    def test_predictions_clean_empty(self):
        rc, out = self.run_leg("predictions_due")
        self.assertEqual(rc, 0, out)
        self.assertIn("✓ none due", out)

    def test_predictions_due(self):
        self.append("workbook/PREDICTIONS.tsv",
                    "ISH-01\t2026-10-01\tISM below 50\t60%\t1m\t2026-10-20\tOPEN\t\t\tstance\t\n")
        rc, out = self.run_leg("predictions_due")
        self.assertEqual(rc, 1, out)
        self.assertIn("DUE: ISH-01", out)

    def test_predictions_unparsable(self):
        self.append("workbook/PREDICTIONS.tsv",
                    "ISH-01\t2026-10-01\tx\t60%\t1m\tnext ISM\tOPEN\t\t\tstance\t\n")
        rc, out = self.run_leg("predictions_due")
        self.assertEqual(rc, 1, out)
        self.assertIn("unparsable Resolve_By", out)

    # 3. catalysts -------------------------------------------------------------------------
    def test_catalysts_missing(self):
        (self.home / "docket" / "CATALYSTS.tsv").unlink(missing_ok=True)
        rc, out = self.run_leg("catalysts_due")
        self.assertEqual(rc, 2, out)

    def test_catalysts_bad_header(self):
        self.write("docket/CATALYSTS.tsv", "# comment first\n" + CAT_HDR)
        rc, out = self.run_leg("catalysts_due")
        self.assertEqual(rc, 2, out)
        self.assertIn("line 1 is not", out)

    def test_catalysts_empty_forward(self):
        self.cats(["2026-10-01", "[ISM-MFG] ISM Sep", "", "", "P2", "ISHM", "", "FIRM"])
        rc, out = self.run_leg("catalysts_due")
        self.assertEqual(rc, 1, out)
        self.assertIn("EMPTY-FORWARD", out)

    def test_catalysts_thin_forward(self):
        self.cats(["2026-11-10", "[IP] G.17", "", "", "P2", "ISHM", "", "FIRM"])
        rc, out = self.run_leg("catalysts_due")
        self.assertEqual(rc, 1, out)
        self.assertIn("THIN-FORWARD", out)

    def test_catalysts_today(self):
        self.cats(["2026-10-23", "[SPG-PMI-MFG] flash", "", "", "P1", "ISHM", "", "FIRM"],
                  ["2026-12-15", "[IP] G.17", "", "", "P2", "ISHM", "", "FIRM"])
        rc, out = self.run_leg("catalysts_due")
        self.assertEqual(rc, 1, out)
        self.assertIn("TODAY", out)

    def test_catalysts_clean(self):
        self.cats(["2026-11-02", "[ISM-MFG] ISM Oct", "", "", "P1", "ISHM", "", "FIRM"],
                  ["2026-12-15", "[IP] G.17", "", "", "P2", "ISHM", "", "FIRM"])
        rc, out = self.run_leg("catalysts_due")
        self.assertEqual(rc, 0, out)
        self.assertIn("✓ none due", out)

    # 4. missed prints ---------------------------------------------------------------------
    def test_missed_print_flagged(self):
        self.cats(["2026-10-01", "[ISM-MFG] ISM Sep", "", "", "P1", "ISHM", "", "FIRM"])
        rc, out = self.run_leg("missed_prints")
        self.assertEqual(rc, 1, out)
        self.assertIn("MISSED PRINT: [ISM-MFG]", out)

    def test_missed_print_clean_when_read(self):
        self.cats(["2026-10-01", "[ISM-MFG] ISM Sep", "", "", "P1", "ISHM", "", "FIRM"])
        self.append("workbook/PRINTS.tsv", _print_row())
        rc, out = self.run_leg("missed_prints")
        self.assertEqual(rc, 0, out)
        self.assertIn("✓ every past keyed catalyst has its print on file", out)

    def test_missed_print_older_print_still_flags(self):
        self.cats(["2026-10-01", "[ISM-MFG] ISM Sep", "", "", "P1", "ISHM", "", "FIRM"])
        self.append("workbook/PRINTS.tsv", _print_row(ref="2026-08", rel="2026-09-01"))
        rc, out = self.run_leg("missed_prints")
        self.assertEqual(rc, 1, out)
        self.assertIn("newest on file 2026-09-01", out)

    def test_missed_print_unknown_key(self):
        self.cats(["2026-10-01", "[NOPE] x", "", "", "P1", "ISHM", "", "FIRM"])
        rc, out = self.run_leg("missed_prints")
        self.assertEqual(rc, 1, out)
        self.assertIn("not a declared SERIES-KEY", out)

    def test_missed_print_unkeyed_is_reported_not_flagged(self):
        self.cats(["2026-10-01", "Boundary review with WATT", "", "", "P3", "ISHM", "", "FIRM"])
        rc, out = self.run_leg("missed_prints")
        self.assertEqual(rc, 0, out)
        self.assertIn("carry no [SERIES-KEY]", out)

    # 5. print ledger ----------------------------------------------------------------------
    def test_print_ledger_empty(self):
        rc, out = self.run_leg("print_ledger")
        self.assertEqual(rc, 1, out)
        self.assertIn("0 print rows", out)

    def test_print_ledger_clean(self):
        self.append("workbook/PRINTS.tsv", _print_row())
        rc, out = self.run_leg("print_ledger")
        self.assertEqual(rc, 0, out)
        self.assertIn("✓ enums valid", out)

    def test_print_ledger_bad_basis(self):
        self.append("workbook/PRINTS.tsv", _print_row(basis="TRUST-ME"))
        rc, out = self.run_leg("print_ledger")
        self.assertEqual(rc, 1, out)
        self.assertIn("not a Class 12 token", out)

    def test_print_ledger_flash_successor_due(self):
        self.append("workbook/PRINTS.tsv", _print_row(series="SPG-PMI-MFG", vint="FLASH", succ="2026-10-01"))
        rc, out = self.run_leg("print_ledger")
        self.assertEqual(rc, 1, out)
        self.assertIn("SUCCESSOR DUE", out)

    def test_print_ledger_flash_superseded_clean(self):
        self.append("workbook/PRINTS.tsv", _print_row(series="SPG-PMI-MFG", vint="FLASH", succ="2026-10-01")
                    + _print_row(series="SPG-PMI-MFG", vint="FINAL", rel="2026-10-01"))
        rc, out = self.run_leg("print_ledger")
        self.assertEqual(rc, 0, out)

    def test_print_ledger_flash_without_successor_date(self):
        self.append("workbook/PRINTS.tsv", _print_row(series="SPG-PMI-MFG", vint="FLASH"))
        rc, out = self.run_leg("print_ledger")
        self.assertEqual(rc, 1, out)
        self.assertIn("no Successor_Date", out)

    # 6. perimeter -------------------------------------------------------------------------
    def test_perimeter_clean_as_built(self):
        rc, out = self.run_leg("perimeter")
        self.assertEqual(rc, 0, out)
        self.assertIn("exactly the 8 ruled tickers", out)

    def test_perimeter_ninth_name(self):
        self.append("PERIMETER.tsv", "ETN\tEaton\tx\tx\t2026-10-23\t\n")
        rc, out = self.run_leg("perimeter")
        self.assertEqual(rc, 1, out)
        self.assertIn("NOT IN THE RULED EIGHT: ETN", out)

    def test_perimeter_banner_lost(self):
        text = (self.home / "PERIMETER.tsv").read_text(encoding="utf-8").split("\n", 1)[1]
        self.write("PERIMETER.tsv", text)
        rc, out = self.run_leg("perimeter")
        self.assertEqual(rc, 1, out)
        self.assertIn("lost its FROZEN banner", out)

    def test_perimeter_name_missing(self):
        lines = (self.home / "PERIMETER.tsv").read_text(encoding="utf-8").splitlines(keepends=True)
        self.write("PERIMETER.tsv", "".join(l for l in lines if not l.startswith("UNP\t")))
        rc, out = self.run_leg("perimeter")
        self.assertEqual(rc, 1, out)
        self.assertIn("RULED NAME MISSING: UNP", out)

    # 7. matrix + map ----------------------------------------------------------------------
    def test_matrix_unscored_as_built(self):
        rc, out = self.run_leg("matrix_and_flow")
        self.assertEqual(rc, 1, out)
        self.assertIn("UNSCORED: 8 of 8", out)

    def _score_all(self, score="2"):
        p = self.home / "workbook" / "VX.tsv"
        p.write_text(p.read_text(encoding="utf-8").replace("\tUNKNOWN\tUNSCORED\t", f"\t{score}\tSCORED\t"),
                     encoding="utf-8")

    def test_matrix_scored_clean_composite_excludes_thermometer(self):
        self._score_all("2")
        rc, out = self.run_leg("matrix_and_flow")
        self.assertEqual(rc, 0, out)
        self.assertIn("Total 14/35", out)       # 7 MECHANISM rows x 2; the THERMOMETER is not added

    def test_matrix_orphan_flow(self):
        self._score_all("2")
        self.append("workbook/FLOW.tsv", "FL-ISH-99\tx\tVX-ISH-99\tUNTESTED\tx\tx\t2026-10-23\t\n")
        rc, out = self.run_leg("matrix_and_flow")
        self.assertEqual(rc, 1, out)
        self.assertIn("orphan mechanism", out)

    def test_matrix_bad_score(self):
        self._score_all("7")
        rc, out = self.run_leg("matrix_and_flow")
        self.assertEqual(rc, 1, out)
        self.assertIn("is not 1-5 or UNKNOWN", out)

    # 8. FRED ------------------------------------------------------------------------------
    def _ledger_current(self):
        rows = "".join(_print_row(series=k, ref="2026-09", rel="2026-10-17") for k in self.b.FRED_SERIES)
        self.append("workbook/PRINTS.tsv", rows)

    def test_fred_clean_when_ledger_current(self):
        self._ledger_current()
        rc, out = self.run_leg("fred_hard_data")
        self.assertEqual(rc, 0, out)
        self.assertIn("✓ ledger current with FRED", out)

    def test_fred_new_print_flagged(self):
        rc, out = self.run_leg("fred_hard_data")
        self.assertEqual(rc, 1, out)
        self.assertIn("NEW PRINT ON FRED: [IP] INDPRO 2026-09", out)
        self.assertIn("no ledger row yet", out)

    def test_fred_html_is_failure(self):
        self._ledger_current()
        (self.fred / "INDPRO.csv").write_text(_fred_csv("INDPRO", html=True), encoding="utf-8")
        rc, out = self.run_leg("fred_hard_data")
        self.assertEqual(rc, 2, out)
        self.assertIn("not a FRED CSV", out)

    def test_fred_small_population_is_failure(self):
        self._ledger_current()
        (self.fred / "TCU.csv").write_text(_fred_csv("TCU", n=3), encoding="utf-8")
        rc, out = self.run_leg("fred_hard_data")
        self.assertEqual(rc, 2, out)
        self.assertIn("positive-control population", out)

    def test_fred_stale_series_is_failure(self):
        self._ledger_current()
        (self.fred / "AMTMNO.csv").write_text(_fred_csv("AMTMNO", last="2026-01-01"), encoding="utf-8")
        rc, out = self.run_leg("fred_hard_data")
        self.assertEqual(rc, 2, out)
        self.assertIn("series or route broken", out)

    def test_fred_missing_fixture_is_failure(self):
        self._ledger_current()
        (self.fred / "NEWORDER.csv").unlink()
        rc, out = self.run_leg("fred_hard_data")
        self.assertEqual(rc, 2, out)
        self.assertIn("FRED NEWORDER: fetch/parse FAILED", out)

    def test_fred_offline_is_not_a_pass(self):
        self.b.OFFLINE = True
        rc, out = self.run_leg("fred_hard_data")
        self.assertEqual(rc, 1, out)
        self.assertIn("NOT RUN (--offline)", out)

    # main() through the drill hooks ------------------------------------------------------
    def test_main_combined_verdict_and_drill_banners(self):
        env = dict(os.environ, ISHM_HOME=str(self.home), ISHM_FRED_DIR=str(self.fred),
                   ISHM_BOOT_TODAY=TODAY.isoformat())
        p = subprocess.run([sys.executable, str(DESK / "boot.py")], env=env, capture_output=True, text=True)
        self.assertEqual(p.returncode, 1, p.stdout + p.stderr)
        self.assertIn("DRILL CLOCK", p.stdout)
        self.assertIn("DRILL: ISHM_HOME", p.stdout)
        self.assertIn("NOT RUN (drill home)", p.stdout)
        self.assertIn("ISHM boot: REVIEW", p.stdout)

    def test_main_failure_dominates(self):
        (self.home / "docket" / "CATALYSTS.tsv").unlink(missing_ok=True)
        env = dict(os.environ, ISHM_HOME=str(self.home), ISHM_FRED_DIR=str(self.fred),
                   ISHM_BOOT_TODAY=TODAY.isoformat())
        p = subprocess.run([sys.executable, str(DESK / "boot.py")], env=env, capture_output=True, text=True)
        self.assertEqual(p.returncode, 2, p.stdout + p.stderr)
        self.assertIn("a leg FAILED", p.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
