#!/usr/bin/env python3
"""WQ-417 P3 coverage test: SHARED paths PROME demonstrably authored are flagged PROME-EVIDENCED, every path stays
listed, and the historical hidden-packet case (888924d2e, AGENTS/FALCON/inbox/data) is covered. The UNEVIDENCED
sub-lane is a reading hint, never a drop (A4)."""
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "PROME/tools"))
import argus_scope as sc  # noqa: E402

SUBJ = {"888924d2e": "PROME -> FALCON, DAEDALUS: FIRMS key live — first VIIRS corridor pull with coordinates",
        "aa74e2511": "PROME -> TERRY: WQ-302 Will's word - HBAN sell-or-roll by Wed",
        "40b424536": "WALTER: SIG-W-20261010-007 small-bank borrowings + FHLB gap + HY issuance -> LIQUID"}


class TestEvidence(unittest.TestCase):
    def test_falcon_hidden_packet_case_is_evidenced(self):
        e = {"path": "AGENTS/FALCON/inbox/data/2026-09-11_FIRMS_VIIRS_corridor.csv", "committed": ["888924d2e"], "pending": []}
        ev = sc.authorship_evidence(e, SUBJ)
        self.assertTrue(ev and any("888924d2e" in x for x in ev), ev)

    def test_from_prome_filename_pending_only(self):
        e = {"path": "AGENTS/TERRY/inbox/2026-10-10_from-PROME_WQ-302-will-word.md", "committed": [], "pending": ["??"]}
        self.assertTrue(any("from-PROME" in x for x in sc.authorship_evidence(e, SUBJ)))

    def test_other_desk_signal_is_unevidenced(self):
        e = {"path": "AGENTS/LIQUID/inbox/WALTER/SIG-W-20261010-007.md", "committed": ["40b424536"], "pending": []}
        self.assertEqual(sc.authorship_evidence(e, SUBJ), [])

    def test_via_prome_relay_and_msg_route_and_case(self):
        e = {"path": "AGENTS/MARCO/inbox/2026-10-09_from-ZHAO-via-PROME_relay.md", "committed": [], "pending": ["??"]}
        self.assertTrue(any("via-PROME" in x for x in sc.authorship_evidence(e, SUBJ)))
        e = {"path": "AGENTS/BRENT/inbox/MSG-PROME-20261010-001__ACTION__x.md", "committed": [], "pending": ["??"]}
        self.assertTrue(any("MSG-PROME" in x for x in sc.authorship_evidence(e, SUBJ)))
        e = {"path": "AGENTS/BRENT/inbox/MSG-WALTER-20261010-001__ACTION__x.md", "committed": [], "pending": ["??"]}
        self.assertEqual(sc.authorship_evidence(e, SUBJ), [])                                   # the filename names another sender
        e = {"path": "AGENTS/BRENT/inbox/WALTER/MSG-not-top-level.md", "committed": [], "pending": ["??"]}
        self.assertEqual(sc.authorship_evidence(e, SUBJ), [])
        e = {"path": "AGENTS/X/inbox/a.md", "committed": ["c0ffee123"], "pending": []}
        self.assertTrue(sc.authorship_evidence(e, {"c0ffee123": "Prome: lower-case subject"}))

    def test_prometheus_is_not_prome(self):
        e = {"path": "AGENTS/X/inbox/2026-10-10_from-PROMETHEUS_note.md", "committed": ["abc123def"], "pending": []}
        self.assertEqual(sc.authorship_evidence(e, {"abc123def": "PROMETHEUS: a desk that is not PROME"}), [])

    def test_sublane_labels(self):
        self.assertEqual(sc.sublane({"path": "AGENTS/X/inbox/a.md", "committed": ["aa74e2511"], "pending": []}, SUBJ), "SHARED/PROME-EVIDENCED")
        self.assertEqual(sc.sublane({"path": "AGENTS/X/inbox/a.md", "committed": ["40b424536"], "pending": []}, SUBJ), "SHARED/UNEVIDENCED")


if __name__ == "__main__":
    unittest.main()
