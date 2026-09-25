"""prome_gate gate-citability leg (DOCKET L417, WQ-250 ③) — throwaway-directory fixture, never the live tree.

Acceptance conditions -> PROME/tools/tests/ACCEPTANCE_prome_gate_citability_L417.md
Run: python3 -W error::ResourceWarning -m unittest PROME/tools/tests/test_prome_gate_citability_L417.py
"""
import pathlib, sys, tempfile, unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import prome_gate as G   # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[3]


def row(gate, state, cond="crude MM shorts > x", surf="AGENTS/X/KB.md"):
    r = [""] * 12
    r[0], r[3], r[5], r[10] = gate, cond, state, surf
    return r


class Citability(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.root = pathlib.Path(self.tmp.name)
        (self.root / "AGENTS/X").mkdir(parents=True)
        (self.root / "AGENTS/X/CLEAN.md").write_text("letter: crude MM gross shorts > 35B; attested.\n")
        (self.root / "AGENTS/X/UNVER.md").write_text("letter … production UNVERIFIED — query: SOFR99-IORB run.\n")
        (self.root / "PROME").mkdir()
        (self.root / "PROME/GATES_README.md").write_text("rule prose: production UNVERIFIED and realisation UNKNOWN register but never fire.\n")

    def tearDown(self):
        self.tmp.cleanup()

    def scan(self, rows):
        return G.scan_gate_citability(rows, self.root)

    def test_pass_with_hit_when_lead_is_not_armed(self):                         # condition 1
        o = self.scan([row("G-A", "LIVE / NOT ARMED — attestation pending: SOFR99", surf="AGENTS/X/UNVER.md")])
        self.assertEqual(o["violations"], []); self.assertEqual(o["hits"], [("AGENTS/X/UNVER.md", 1, ["G-A"])])
        self.assertIn("1 hits over 1 files · AGENTS/X/UNVER.md (1) → G-A", G.citability_detail(o))

    def test_fail_on_live_lead(self):                                              # condition 2
        o = self.scan([row("G-B", "LIVE — armed", surf="AGENTS/X/UNVER.md")])
        self.assertEqual(o["violations"], ["G-B → AGENTS/X/UNVER.md (production UNVERIFIED)"])
        self.assertIn("VIOLATIONS: G-B", G.citability_detail(o))

    def test_condition_cell_hit_two_homes(self):                                   # condition 3
        o = self.scan([row("G-C", "LIVE — x", cond="≥30bp ×2d — realisation UNKNOWN", surf="AGENTS/X/CLEAN.md")])
        self.assertEqual(o["condition_hits"], ["G-C"]); self.assertEqual(o["violations"], ["G-C → condition cell (realisation UNKNOWN)"])

    def test_non_live_ignored_on_both_surfaces(self):                              # condition 3
        o = self.scan([row("G-D", "RESOLVED(2026-09-01)", cond="realisation UNKNOWN", surf="AGENTS/X/UNVER.md")])
        self.assertEqual(sum(len(v) for k, v in o.items() if isinstance(v, list)), 0); self.assertEqual(o["files"], 0)

    def test_readme_cited_but_never_scanned(self):                                 # condition 4
        o = self.scan([row("G-E", "LIVE — x", surf="PROME/GATES_README.md + AGENTS/X/CLEAN.md")])
        self.assertEqual(o["violations"], []); self.assertEqual(o["files"], 1); self.assertEqual(o["unreachable"], [])

    def test_guard_falsified_readme_prose_would_fire(self):                        # the guard itself
        saved = G.CITABILITY_NEVER_SCAN
        G.CITABILITY_NEVER_SCAN = ()
        try:
            o = self.scan([row("G-E", "LIVE — x", surf="PROME/GATES_README.md")])
            self.assertEqual(len(o["violations"]), 1)                              # the defect, induced
        finally:
            G.CITABILITY_NEVER_SCAN = saved
        # and the live README really does carry both tokens — the exclusion is load-bearing, not decorative
        txt = (ROOT / "PROME/GATES_README.md").read_text(encoding="utf-8")
        self.assertTrue(G.CITABILITY_TOKENS.search(txt))

    def test_unreachable_path_is_error_never_skip(self):                           # condition 5
        o = self.scan([row("G-F", "LIVE — x", surf="AGENTS/X/MISSING.md")])
        self.assertEqual(o["unreachable"], [("G-F", "AGENTS/X/MISSING.md")]); self.assertEqual(o["files"], 0)
        G.results.clear(); G.record_gate_citability([row("G-F", "LIVE — x", surf="AGENTS/X/MISSING.md")], self.root)
        sev = [r[0] for r in G.results]; G.results.clear()
        self.assertIn(G.ERROR, sev)
        self.assertEqual(G.aggregate_rc([(G.ERROR, "n", False, "d", "o")], []), 2)

    def test_none_prose_cell_is_not_error(self):                                   # condition 5
        o = self.scan([row("G-G", "LIVE — x", surf="NONE | consumer is a thesis leg (M-09 successor)")])
        self.assertEqual(o["unreachable"], []); self.assertEqual(o["files"], 0); self.assertEqual(o["violations"], [])

    def test_clean_output_shape(self):                                             # condition 7
        o = self.scan([row("G-H", "LIVE — x", surf="AGENTS/X/CLEAN.md")])
        self.assertEqual(G.citability_detail(o), "0 hits over 1 files · condition cells: 0 · 1 of 1 LIVE rows' letters read")

    # ── reader round 1 (2026-09-25): CE1 directory-style pointer · CE7 ./README · CE4 short row · CE2 duplicate gate_id · header drift
    def test_reader_ce1_directory_style_pointer_is_unread_and_says_so(self):
        (self.root / "AGENTS/X/KB.tsv").write_text("KB-X-1\tletter … production UNVERIFIED — q\n")
        o = self.scan([row("G-X1", "LIVE — ARMED 1-of-2", surf="AGENTS/X (KB-X-1)")])
        self.assertEqual(o["files"], 0); self.assertEqual(o["read"], 0); self.assertEqual(o["unread"], ["G-X1"])
        self.assertTrue(o["unreachable"] and "directory-style" in o["unreachable"][0][1], o)
        self.assertIn("0 of 1 LIVE rows' letters read · UNREAD: G-X1", G.citability_detail(o))
        G.results.clear(); G.record_gate_citability([row("G-X1", "LIVE — ARMED", surf="AGENTS/X (KB-X-1)")], self.root)
        self.assertIn(G.ERROR, [r[0] for r in G.results]); G.results.clear()

    def test_reader_ce7_dot_slash_readme_is_still_excluded(self):
        o = self.scan([row("G-R", "LIVE — x", surf="./PROME/GATES_README.md")])
        self.assertEqual(o["violations"], []); self.assertEqual(o["files"], 0)

    def test_reader_ce4_short_row_is_error_not_silent(self):
        short = ["G-S", "", "", "realisation UNKNOWN", "", "LIVE — x"]           # 6 cells, condition cell carries a token
        o = self.scan([short])
        self.assertEqual(o["short"], ["G-S"]); self.assertEqual(o["unread"], ["G-S"]); self.assertEqual(o["live"], 1)
        G.results.clear(); G.record_gate_citability([short], self.root)
        self.assertIn(G.ERROR, [r[0] for r in G.results]); G.results.clear()

    def test_reader_ce2_duplicate_gate_id_second_row_is_checked(self):
        o = self.scan([row("G-D", "LIVE / NOT ARMED — pending", surf="AGENTS/X/UNVER.md"),
                       row("G-D", "LIVE — armed", surf="AGENTS/X/UNVER.md")])
        self.assertEqual(o["violations"], ["G-D → AGENTS/X/UNVER.md (production UNVERIFIED)"])

    def test_header_drift_is_loud(self):
        import csv, io
        bad = "gate_id\tregistered\towner\tcondition\tconsequence_on_fire\tSTATE_X\n"
        hdr = next(csv.reader(io.StringIO(bad), delimiter="\t"))
        with self.assertRaises(RuntimeError):
            for k, i in G.GATES_COLS.items():
                if len(hdr) <= i or hdr[i] != k:
                    raise RuntimeError("drift")

    def test_leg_records_blocking_on_violation(self):                              # condition 2, at the record layer
        G.results.clear(); G.record_gate_citability([row("G-B", "LIVE — armed", surf="AGENTS/X/UNVER.md")], self.root)
        rows = list(G.results); G.results.clear()
        self.assertEqual([(r[0], r[2]) for r in rows], [(G.BLOCK, False)])
        self.assertEqual(G.aggregate_rc(rows, []), 1)


if __name__ == "__main__":
    unittest.main()
