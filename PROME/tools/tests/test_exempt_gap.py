#!/usr/bin/env python3
"""Falsification set for exempt_gap.py (built 2026-09-11 with the tool — the guard is tested before it is trusted).

Frozen fixture, built in a tempdir (never the live tree — a test pinned to a live surface rots on its next edit).
Run: python3 -m unittest PROME/tools/tests/test_exempt_gap.py  (from repo root)
"""
import datetime as dt
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import exempt_gap  # noqa: E402

TODAY = dt.date(2026, 9, 11)


def sig(root, sid, action, date=None):
    d = sid.split("-")[2]
    (root / "BOARD").mkdir(exist_ok=True)
    (root / "BOARD" / f"{sid}-fixture.md").write_text(
        f"---\nsignal_id: {sid}\ndate: {d[:4]}-{d[4:6]}-{d[6:]}\naction: [{action}]\ninfo: [PROME]\n---\n"
        f"# headline for {sid}\n", encoding="utf-8")


def ledger(root, rel, ids):
    p = root / "AGENTS" / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("timestamp_read\tsignal_id\tdisposition\n" + "".join(f"x\t{i}\tnoted\n" for i in ids),
                 encoding="utf-8")


def doctor(root, names):
    p = root / "AGENTS" / "WALTER" / "tools" / "walter_doctor.py"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("x = 1\nPULL_COMPLETE = {" + ", ".join(f'"{n}"' for n in names) + "}  # c\n", encoding="utf-8")


class ExemptGap(unittest.TestCase):
    def test_legacy_filename_receipt_remains_consumed(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "ledger.tsv"
            p.write_text("timestamp_read\tsignal_id\tdisposition\tnotes\n"
                         "x\tSIG-W-20260903-001-skew-150-first-of-leg\tacted\tDone\n")
            self.assertEqual(exempt_gap.logged_ids([p]), {"SIG-W-20260903-001"})

    def test_malformed_ledger_does_not_certify(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "ledger.tsv"
            p.write_text("notes\nSIG-W-20260901-001\n")
            with self.assertRaises(ValueError):
                exempt_gap.logged_ids([p])

    def test_note_reference_is_not_consumption(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "ledger.tsv"
            p.write_text("timestamp_read\tsignal_id\tdisposition\tnotes\n"
                         "x\tSIG-W-20260901-001\tnoted\tCompare SIG-W-20260901-002\n")
            self.assertEqual(exempt_gap.logged_ids([p]), {"SIG-W-20260901-001"})

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        doctor(self.root, ["CARL", "RED", "PROME", "TERRY"])
        sig(self.root, "SIG-W-20260901-015", "CARL")      # 10d old, CARL action
        sig(self.root, "SIG-W-20260910-005", "CARL")      # 1d old, CARL action
        sig(self.root, "SIG-W-20260908-010", "RED")       # 3d old, RED action
        sig(self.root, "SIG-W-20260908-011", "TERRY")     # TERRY action, TERRY has no ledger
        sig(self.root, "SIG-W-20260908-012", "HENRY")     # nobody exempt

    def tearDown(self):
        self.tmp.cleanup()

    def run_scan(self, **kw):
        return exempt_gap.scan(self.root, TODAY, kw.pop("min_age_days", 2), **kw)

    def by(self, rows, desk):
        return next(r for r in rows if r["desk"] == desk)

    def test_exempt_set_is_read_from_the_doctor_minus_prome(self):
        rows, note = self.run_scan()
        self.assertEqual([r["desk"] for r in rows], ["CARL", "RED", "TERRY"])
        self.assertIn("read from", note)

    def test_aged_unlogged_action_flags_and_fresh_one_does_not(self):
        ledger(self.root, "CARL/board/BOARD_LOG.tsv", [])
        c = self.by(self.run_scan()[0], "CARL")
        self.assertEqual(c["unlogged"], ["SIG-W-20260901-015", "SIG-W-20260910-005"])
        self.assertEqual(c["aged"], ["SIG-W-20260901-015"])   # the 1-day-old one is under the 2d floor

    def test_logged_in_any_ledger_including_archive_clears(self):
        ledger(self.root, "CARL/board/BOARD_LOG.tsv", ["SIG-W-20260901-015"])
        ledger(self.root, "RED/board_log.tsv", [])
        ledger(self.root, "RED/archive/board_log_pre-2026-09-06.tsv", ["SIG-W-20260908-010"])
        rows, _ = self.run_scan()
        self.assertEqual(self.by(rows, "CARL")["aged"], [])
        self.assertEqual(self.by(rows, "RED")["unlogged"], [])   # archived ledger counts

    def test_desk_with_no_ledger_is_untestable_not_pass(self):
        rows, _ = self.run_scan()
        t = self.by(rows, "TERRY")
        self.assertTrue(t["untestable"])
        self.assertEqual(t["addressed"], 1)

    def test_info_cc_is_not_the_exemptions_risk(self):
        # a signal that only info-cc's CARL never counts as addressed
        sig(self.root, "SIG-W-20260801-001", "HENRY")
        ledger(self.root, "CARL/board/BOARD_LOG.tsv", [])
        self.assertEqual(self.by(self.run_scan()[0], "CARL")["addressed"], 2)

    def test_exit_codes(self):
        ledger(self.root, "CARL/board/BOARD_LOG.tsv", ["SIG-W-20260901-015"])
        ledger(self.root, "RED/board_log.tsv", [])
        ledger(self.root, "TERRY/board_log.tsv", ["SIG-W-20260908-011"])
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = exempt_gap.main(["--root", str(self.root), "--today", "2026-09-11"])
        self.assertEqual(rc, 1, buf.getvalue())            # RED's 3d-old action signal is unlogged
        self.assertIn("⚠️  RED", buf.getvalue())
        ledger(self.root, "RED/board_log.tsv", ["SIG-W-20260908-010"])
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = exempt_gap.main(["--root", str(self.root), "--today", "2026-09-11"])
        self.assertEqual(rc, 0, buf.getvalue())

    def test_fallback_set_is_loud_when_doctor_unparseable(self):
        (self.root / "AGENTS" / "WALTER" / "tools" / "walter_doctor.py").write_text("nothing here\n")
        _, note = self.run_scan()
        self.assertIn("fallback", note)


if __name__ == "__main__":
    unittest.main()
