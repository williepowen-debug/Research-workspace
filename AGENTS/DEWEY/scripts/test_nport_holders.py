"""The ONE offline selftest for nport_holders.py (WQ-495.NPORT, Will 2026-10-30 "495 - yes approved").

Run: python3 AGENTS/DEWEY/scripts/test_nport_holders.py
No network. Feeds a SYNTHETIC N-PORT primary_doc.xml (fixtures/nport_synthetic_primary_doc.xml,
invented values in the real namespace and element names) through the scanner's own parse()
and klass(), and checks: only rows matching --match are kept, every output column lands in
its named place, and the class letter is read from the title.
What it does NOT test: EFTS search, the network fetch and its primary_doc.xml fallback, the
latest-position dedupe and the CUSIP class inference (those live inside main()). See README.
"""

import importlib.util
import re
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("nport_holders", HERE / "nport_holders.py")
nh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(nh)

FIXTURE = HERE / "fixtures" / "nport_synthetic_primary_doc.xml"


class NportSelftest(unittest.TestCase):
    def test_parse_filters_maps_columns_and_tags_class(self):
        rows = nh.parse(FIXTURE.read_bytes(), re.compile("VANTAGE DATA|SWCH", re.I),
                        "0000000000-26-000001", "2026-09-30", "https://example.invalid/primary_doc.xml")
        # the unrelated holding is dropped; the two named deals are kept in document order
        self.assertEqual(len(rows), 2)
        got = [dict(zip(nh.COLS, r)) for r in rows]
        v, s = got
        self.assertEqual(v["registrant"], "Synthetic Income Trust")
        self.assertEqual(v["series"], "Synthetic Short Duration Fund")
        self.assertEqual(v["rep_date"], "2026-08-31")
        self.assertEqual(v["file_date"], "2026-09-30")
        self.assertEqual(v["net_assets"], "1000000000.00")
        self.assertEqual(v["cusip"], "92212KAA1")
        self.assertEqual(v["valUSD"], "4900000.00")
        self.assertEqual(v["restricted"], "Y")
        self.assertEqual(s["assetCat"], "ABS-CBDO")
        # class letter from the title: "CLASS A2" form and the bare trailing-letter CMBS form
        self.assertEqual(nh.klass(v["title"]), "A2")
        self.assertEqual(nh.klass(s["title"]), "E")
        # a title with no class token returns empty (the scanner then tries CUSIP inference)
        self.assertEqual(nh.klass("UNRELATED CORP 5.0% 2030"), "")


if __name__ == "__main__":
    unittest.main(verbosity=2)
