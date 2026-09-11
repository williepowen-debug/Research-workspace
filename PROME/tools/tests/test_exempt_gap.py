#!/usr/bin/env python3
"""Falsification set for exempt_gap.py (built 2026-09-11 with the tool — the guard is tested before it is trusted;
cold read 2026-09-11 added the fail-closed legs: skipped-by-name, empty set, duplicate id, cell-not-mention, info-cc).

Frozen fixture, built in a tempdir (never the live tree — a test pinned to a live surface rots on its next edit).
Run: python3 -m unittest PROME/tools/tests/test_exempt_gap.py  (from repo root)
"""
import datetime as dt
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import exempt_gap  # noqa: E402

TODAY = dt.date(2026, 9, 11)


def sig(root, sid, action, key="action", idkey="signal_id", info="PROME", slug="fixture"):
    d = sid.split("-")[2]
    (root / "BOARD").mkdir(exist_ok=True)
    (root / "BOARD" / f"{sid}-{slug}.md").write_text(
        f"---\n{idkey}: {sid}\ndate: {d[:4]}-{d[4:6]}-{d[6:]}\n{key}: [{action}]\ninfo: [{info}]\n---\n"
        f"# headline for {sid}\n", encoding="utf-8")


def ledger(root, rel, ids, notes=""):
    p = root / "AGENTS" / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("timestamp_read\tsignal_id\tdisposition\tnotes\n"
                 + "".join(f"x\t{i}\tnoted\t{notes}\n" for i in ids), encoding="utf-8")


def doctor(root, names):
    p = root / "AGENTS" / "WALTER" / "tools" / "walter_doctor.py"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("x = 1\nPULL_COMPLETE = {" + ", ".join(f'"{n}"' for n in names) + "}  # c\n", encoding="utf-8")


def run_main(root, *extra):
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        rc = exempt_gap.main(["--root", str(root), "--today", "2026-09-11", *extra])
    return rc, out.getvalue() + err.getvalue()


class ExemptGap(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        doctor(self.root, ["CARL", "RED", "PROME", "TERRY"])
        self.fixtures = {  # sid → action owner; counts below DERIVE from this table (never hardcoded beside it)
            "SIG-W-20260901-015": "CARL",      # 10d old
            "SIG-W-20260910-005": "CARL",      # 1d old
            "SIG-W-20260908-010": "RED",       # 3d old
            "SIG-W-20260908-011": "TERRY",     # TERRY has no ledger in setUp
            "SIG-W-20260908-012": "HENRY",     # nobody exempt
        }
        for sid, owner in self.fixtures.items():
            sig(self.root, sid, owner)

    def tearDown(self):
        self.tmp.cleanup()

    def run_scan(self, **kw):
        return exempt_gap.scan(self.root, TODAY, kw.pop("min_age_days", 2), **kw)

    def by(self, rows, desk):
        return next(r for r in rows if r["desk"] == desk)

    def n_addressed(self, desk):
        return sum(1 for o in self.fixtures.values() if o == desk)

    # ---- routing + ledger semantics
    def test_exempt_set_is_read_from_the_doctor_minus_prome(self):
        rows, note, inst = self.run_scan()
        self.assertEqual([r["desk"] for r in rows], ["CARL", "RED", "TERRY"])
        self.assertIn("read from", note)
        self.assertTrue(inst["exempt_ok"])

    def test_aged_unlogged_action_flags_and_fresh_one_does_not(self):
        ledger(self.root, "CARL/board/BOARD_LOG.tsv", [])
        c = self.by(self.run_scan()[0], "CARL")
        self.assertEqual(c["unlogged"], ["SIG-W-20260901-015", "SIG-W-20260910-005"])
        self.assertEqual(c["aged"], ["SIG-W-20260901-015"])   # the 1-day-old one is under the 2d floor
        self.assertEqual(c["fresh"], 1)

    def test_logged_in_any_ledger_including_archive_clears(self):
        ledger(self.root, "CARL/board/BOARD_LOG.tsv", ["SIG-W-20260901-015"])
        ledger(self.root, "RED/board_log.tsv", [])
        ledger(self.root, "RED/archive/board_log_pre-2026-09-06.tsv", ["SIG-W-20260908-010"])
        rows, _, _ = self.run_scan()
        self.assertEqual(self.by(rows, "CARL")["aged"], [])
        self.assertEqual(self.by(rows, "RED")["unlogged"], [])   # archived ledger counts

    def test_an_id_at_the_start_of_a_notes_cell_is_still_a_mention(self):
        # result cold read ❌1: the notes cell BEGINS with the id — cell-exact matching must not count it
        ledger(self.root, "CARL/board/BOARD_LOG.tsv", ["SIG-W-20260101-001"], notes="SIG-W-20260901-015 superseded, ignoring")
        c = self.by(self.run_scan()[0], "CARL")
        self.assertIn("SIG-W-20260901-015", c["aged"])

    def test_post_v012_file_with_no_routing_key_is_skipped_and_legacy_one_is_counted(self):
        # result cold read ❌2: `routing: [CARL]` on a 9/1 file is one key away from addressing nobody silently
        (self.root / "BOARD" / "SIG-W-20260901-016-newkey.md").write_text(
            "---\nsignal_id: SIG-W-20260901-016\nrouting: [CARL]\n---\n# IMMEDIATE\n")
        (self.root / "BOARD" / "SIG-W-20260401-002-earlyapril.md").write_text(
            "---\nsignal_id: SIG-W-20260401-002\nprecedence: ROUTINE\n---\n# old\n")
        (self.root / "BOARD" / "SIG-W-20260910-008-erratum.md").write_text(       # empty action = routed to nobody, fine
            "---\nsignal_id: SIG-W-20260910-008\naction: []\ninfo: [RED]\n---\n# erratum\n")
        _, _, inst = self.run_scan()
        self.assertEqual([n for n, _ in inst["skipped"]], ["SIG-W-20260901-016-newkey.md"])
        self.assertEqual(inst["unrouted_legacy"], 1)

    def test_lowercase_or_stray_name_under_board_is_skipped_by_name_index_is_not(self):
        # result cold read ❌3: the glob must enumerate every .md under BOARD/ except INDEX.md
        (self.root / "BOARD" / "sig-w-20260901-017-lower.md").write_text("---\naction: [CARL]\n---\n# h\n")
        (self.root / "BOARD" / "INDEX.md").write_text("# index\n")
        _, _, inst = self.run_scan()
        self.assertEqual([n for n, _ in inst["skipped"]], ["sig-w-20260901-017-lower.md"])

    def test_a_mention_in_a_notes_cell_is_not_a_logged_row(self):
        # the id appears only inside another row's notes cell — that is a mention, not a disposition
        ledger(self.root, "RED/board_log.tsv", ["SIG-W-20260101-001"], notes="see SIG-W-20260908-010 later")
        r = self.by(self.run_scan()[0], "RED")
        self.assertEqual(r["unlogged"], ["SIG-W-20260908-010"])

    def test_desk_with_no_ledger_is_untestable_not_pass(self):
        rows, _, _ = self.run_scan()
        t = self.by(rows, "TERRY")
        self.assertTrue(t["untestable"])
        self.assertEqual(t["addressed"], self.n_addressed("TERRY"))

    def test_info_cc_is_not_the_exemptions_risk(self):
        # CARL on the INFO line only: never addressed. A code path reading info: as action would fail this.
        sig(self.root, "SIG-W-20260801-001", "HENRY", info="CARL")
        ledger(self.root, "CARL/board/BOARD_LOG.tsv", [])
        c = self.by(self.run_scan()[0], "CARL")
        self.assertEqual(c["addressed"], self.n_addressed("CARL"))
        self.assertNotIn("SIG-W-20260801-001", c["unlogged"])

    def test_legacy_to_key_and_bare_id_key_are_read(self):
        # 585 April–July BOARD files use `to:` for the action line; 104 use bare `id:` (TERRY 9/11).
        sig(self.root, "SIG-W-20260720-001", "CARL", key="to")
        sig(self.root, "SIG-W-20260820-003", "CARL", idkey="id")
        ledger(self.root, "CARL/board/BOARD_LOG.tsv", [])
        c = self.by(self.run_scan()[0], "CARL")
        self.assertIn("SIG-W-20260720-001", c["aged"])
        self.assertIn("SIG-W-20260820-003", c["aged"])

    def test_legacy_to_value_forms_bare_and_annotated_and_near_miss(self):
        # live forms measured 9/11: bracket 158 · bare 194 · "NAME (annotation, with, commas)" 220
        sig(self.root, "SIG-W-20260508-004", "CARL (ACTION — load-bearing, commas, inside; more)", key="to")
        sig(self.root, "SIG-W-20260509-001", "RED", key="to")
        sig(self.root, "SIG-W-20260509-002", "TERRYX", key="to")        # near-miss: must NOT address TERRY
        ledger(self.root, "CARL/board/BOARD_LOG.tsv", [])
        ledger(self.root, "RED/board_log.tsv", [])
        ledger(self.root, "TERRY/board_log.tsv", [])
        rows, _, _ = self.run_scan()
        self.assertIn("SIG-W-20260508-004", self.by(rows, "CARL")["aged"])
        self.assertIn("SIG-W-20260509-001", self.by(rows, "RED")["aged"])
        self.assertNotIn("SIG-W-20260509-002", self.by(rows, "TERRY")["unlogged"])
        self.assertEqual(exempt_gap.owners("CARL (ACTION — x, y)"), ["CARL"])
        self.assertEqual(exempt_gap.owners(["carl", "RED"]), ["CARL", "RED"])
        self.assertEqual(exempt_gap.owners("C"), [])                     # a lone letter is never a desk

    # ---- fail-closed instrument legs (cold read 9/11)
    def test_bad_filename_date_is_skipped_counted_named_and_fails_closed(self):
        ledger(self.root, "CARL/board/BOARD_LOG.tsv", [])
        ledger(self.root, "RED/board_log.tsv", ["SIG-W-20260908-010"])
        ledger(self.root, "TERRY/board_log.tsv", ["SIG-W-20260908-011"])
        bad = self.root / "BOARD" / "SIG-W-20260500-001-bad.md"
        bad.write_text("---\nsignal_id: SIG-W-20260500-001\naction: [CARL]\n---\n# h\n")
        rows, _, inst = self.run_scan()
        self.assertEqual(self.by(rows, "CARL")["aged"], ["SIG-W-20260901-015"])   # (a) the scan survived
        self.assertEqual([n for n, _ in inst["skipped"]], ["SIG-W-20260500-001-bad.md"])  # (b) named, not swallowed
        rc, out = run_main(self.root)
        self.assertEqual(rc, 2, out)                                              # (c) fail closed, by name
        self.assertIn("SIG-W-20260500-001-bad.md", out)

    def test_non_matching_name_and_no_frontmatter_are_skipped_by_name(self):
        (self.root / "BOARD" / "SIG-W-2026091-3-short.md").write_text("---\naction: [CARL]\n---\n# h\n")
        (self.root / "BOARD" / "SIG-W-20260903-009-nofront.md").write_text("# no frontmatter at all\n")
        _, _, inst = self.run_scan()
        self.assertEqual(sorted(n for n, _ in inst["skipped"]),
                         sorted(["SIG-W-2026091-3-short.md", "SIG-W-20260903-009-nofront.md"]))

    def test_duplicate_signal_id_merges_owners_and_is_named(self):
        sig(self.root, "SIG-W-20260901-015", "HENRY", slug="second-file-same-id")
        ledger(self.root, "CARL/board/BOARD_LOG.tsv", [])
        rows, _, inst = self.run_scan()
        self.assertIn("SIG-W-20260901-015", self.by(rows, "CARL")["aged"])     # CARL's obligation survives
        self.assertEqual(inst["dupes"], ["SIG-W-20260901-015"])

    def test_empty_exempt_set_is_an_instrument_failure_not_a_pass(self):
        doctor(self.root, ["PROME"])                     # only PROME ⇒ nothing to scan after the discard
        _, note, inst = self.run_scan()
        self.assertFalse(inst["exempt_ok"])
        self.assertIn("FALLBACK", note)
        rc, out = run_main(self.root)
        self.assertEqual(rc, 2, out)

    def test_unreadable_ledger_is_named_not_zero(self):
        (self.root / "AGENTS" / "RED" / "board_log.tsv").mkdir(parents=True)   # a directory where a file should be
        rows, _, inst = self.run_scan()
        self.assertEqual(len(inst["ledger_errors"]), 1)
        self.assertFalse(self.by(rows, "RED")["untestable"])
        rc, out = run_main(self.root)
        self.assertEqual(rc, 2, out)
        self.assertIn("LEDGER UNREADABLE", out)

    def test_exit_codes_1_then_0(self):
        ledger(self.root, "CARL/board/BOARD_LOG.tsv", ["SIG-W-20260901-015"])
        ledger(self.root, "RED/board_log.tsv", [])
        ledger(self.root, "TERRY/board_log.tsv", ["SIG-W-20260908-011"])
        rc, out = run_main(self.root)
        self.assertEqual(rc, 1, out)            # RED's 3d-old action signal is unlogged
        self.assertIn("⚠️  RED", out)
        ledger(self.root, "RED/board_log.tsv", ["SIG-W-20260908-010"])
        rc, out = run_main(self.root)
        self.assertEqual(rc, 0, out)

    def test_desks_override_prints_full_list_and_honest_note(self):
        ledger(self.root, "CARL/board/BOARD_LOG.tsv", [])
        rc, out = run_main(self.root, "--desks", "CARL")
        self.assertIn("OVERRIDDEN by --desks", out)
        self.assertNotIn("read from", out)


if __name__ == "__main__":
    unittest.main()
