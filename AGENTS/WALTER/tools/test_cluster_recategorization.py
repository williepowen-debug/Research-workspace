"""CLUSTER_RECATEGORIZATIONS.tsv moves INDEX placement only, and refuses every stale or invalid row."""
import os
import tempfile
import unittest

import gen_board_index as index

TAX = {"CONSUMER_STAGFLATION", "MISC"}
HEADER = "\t".join(index.RECAT_COLS) + "\n"


def sigs():
    return {"SIG-W-20261007-013": dict(id="SIG-W-20261007-013", file="SIG-W-20261007-013-x.md", date="2026-10-07",
                                       domain="LABOR_MARKET", cluster="LABOR_DOWN", precedence="PRIORITY",
                                       action=["LABOR"], info=[], confidence="0.9", title="Workday")}


class RecategorizationTests(unittest.TestCase):
    def run_rows(self, *rows):
        s, errors = sigs(), []
        with tempfile.TemporaryDirectory() as t:
            p = os.path.join(t, "CLUSTER_RECATEGORIZATIONS.tsv")
            open(p, "w", encoding="utf-8").write("# comment\n" + HEADER + "".join(r + "\n" for r in rows))
            index.apply_recategorizations(s, errors, path=p, clusters=TAX)
        return s["SIG-W-20261007-013"], errors

    def test_valid_row_moves_placement_and_marks_row(self):
        s, errors = self.run_rows("SIG-W-20261007-013\tLABOR_DOWN\tCONSUMER_STAGFLATION\t2026-10-23\tWill\tchain name")
        self.assertEqual(errors, [])
        self.assertEqual(s["cluster"], "CONSUMER_STAGFLATION")
        self.assertIn("RE-FILED 2026-10-23", index.render_row(s, {}))
        self.assertIn("`LABOR_DOWN`", index.render_row(s, {}))

    def test_stale_from_cluster_refuses(self):
        s, errors = self.run_rows("SIG-W-20261007-013\tMISC\tCONSUMER_STAGFLATION\t2026-10-23\tWill\tx")
        self.assertEqual(s["cluster"], "LABOR_DOWN")
        self.assertTrue(any("stale or wrong row" in e for e in errors))

    def test_target_outside_taxonomy_refuses(self):
        s, errors = self.run_rows("SIG-W-20261007-013\tLABOR_DOWN\tLABOR_DOWN2\t2026-10-23\tWill\tx")
        self.assertEqual(s["cluster"], "LABOR_DOWN")
        self.assertTrue(any("not a CLUSTER_TAXONOMY cluster" in e for e in errors))

    def test_unknown_signal_duplicate_short_row_and_bad_date_refuse(self):
        _, e1 = self.run_rows("SIG-W-20990101-001\tLABOR_DOWN\tMISC\t2026-10-23\tWill\tx")
        _, e2 = self.run_rows("SIG-W-20261007-013\tLABOR_DOWN\tMISC\t2026-10-23\tWill\tx",
                              "SIG-W-20261007-013\tLABOR_DOWN\tMISC\t2026-10-23\tWill\tx")
        _, e3 = self.run_rows("SIG-W-20261007-013\tLABOR_DOWN\tMISC")
        _, e4 = self.run_rows("SIG-W-20261007-013\tLABOR_DOWN\tMISC\t10/23\tWill\tx")
        self.assertTrue(any("no BOARD file" in e for e in e1))
        self.assertTrue(any("re-filed twice" in e for e in e2))
        self.assertTrue(any("non-empty" in e for e in e3))
        self.assertTrue(any("not YYYY-MM-DD" in e for e in e4))

    def test_unparsed_taxonomy_refuses(self):
        s, errors = sigs(), []
        with tempfile.TemporaryDirectory() as t:
            p = os.path.join(t, "r.tsv")
            open(p, "w").write(HEADER + "SIG-W-20261007-013\tLABOR_DOWN\tMISC\t2026-10-23\tWill\tx\n")
            index.apply_recategorizations(s, errors, path=p, clusters=set())
        self.assertEqual(s["SIG-W-20261007-013"]["cluster"], "LABOR_DOWN")
        self.assertTrue(any("did not parse" in e for e in errors))

    def test_absent_ledger_is_a_no_op(self):
        s, errors = sigs(), []
        index.apply_recategorizations(s, errors, path="/nonexistent/r.tsv", clusters=TAX)
        self.assertEqual((s["SIG-W-20261007-013"]["cluster"], errors), ("LABOR_DOWN", []))

    def test_live_taxonomy_parses_and_contains_target(self):
        self.assertIn("CONSUMER_STAGFLATION", index.taxonomy_clusters())
        self.assertNotIn("LABOR_DOWN", index.taxonomy_clusters())




class ErratumSuppressionTests(unittest.TestCase):
    """INDEX_ERRATUM_SUPPRESSIONS.tsv hides only the INDEX marker, and refuses every stale or invalid row (WQ-503 B)."""

    def run_rows(self, erratum, *rows):
        s = sigs()
        s["SIG-W-20261007-013"].update(erratum=erratum, corrects=[], corrects_direction="", status="", status_date="", status_ref="")
        errors = []
        with tempfile.TemporaryDirectory() as t:
            p = os.path.join(t, "INDEX_ERRATUM_SUPPRESSIONS.tsv")
            open(p, "w", encoding="utf-8").write("# comment\n" + "\t".join(index.ERRATUM_SUPP_COLS) + "\n" + "".join(r + "\n" for r in rows))
            index.apply_erratum_suppressions(s, errors, path=p)
        return s, errors

    def test_matching_row_suppresses_marker(self):
        s, errors = self.run_rows("SELF", "SIG-W-20261007-013\tSELF\t2026-10-28\tWill\tleftover")
        self.assertEqual(errors, [])
        self.assertEqual(index.derive_markers(s).get("SIG-W-20261007-013", []), [])

    def test_unsuppressed_marker_still_renders(self):
        s, errors = self.run_rows("SELF")
        self.assertTrue(any("ADDITIVE ERRATUM" in m for m in index.derive_markers(s)["SIG-W-20261007-013"]))

    def test_changed_header_refuses_and_keeps_marker(self):
        s, errors = self.run_rows("2026-10-29 — new", "SIG-W-20261007-013\tSELF\t2026-10-28\tWill\tx")
        self.assertTrue(any("stale or wrong row" in e for e in errors))
        self.assertTrue(index.derive_markers(s)["SIG-W-20261007-013"])

    def test_missing_signal_and_duplicate_refuse(self):
        _, errors = self.run_rows("SELF", "SIG-W-20990101-001\tSELF\t2026-10-28\tWill\tx",
                                  "SIG-W-20261007-013\tSELF\t2026-10-28\tWill\tx", "SIG-W-20261007-013\tSELF\t2026-10-28\tWill\tx")
        self.assertTrue(any("no BOARD file" in e for e in errors))
        self.assertTrue(any("suppressed twice" in e for e in errors))

if __name__ == "__main__":
    unittest.main()
