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


def sig(root, sid, action, date=None, key="action", idkey="signal_id"):
    d = sid.split("-")[2]
    (root / "BOARD").mkdir(exist_ok=True)
    (root / "BOARD" / f"{sid}-fixture.md").write_text(
        f"---\n{idkey}: {sid}\ndate: {d[:4]}-{d[4:6]}-{d[6:]}\n{key}: [{action}]\ninfo: [PROME]\n---\n"
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
        rows, _ = self.run_scan()
        self.assertIn("SIG-W-20260508-004", self.by(rows, "CARL")["aged"])
        self.assertIn("SIG-W-20260509-001", self.by(rows, "RED")["aged"])
        self.assertNotIn("SIG-W-20260509-002", self.by(rows, "TERRY")["unlogged"])
        self.assertEqual(exempt_gap.owners("CARL (ACTION — x, y)"), ["CARL"])
        self.assertEqual(exempt_gap.owners(["carl", "RED"]), ["CARL", "RED"])
        self.assertEqual(exempt_gap.owners("C"), [])                     # a lone letter is never a desk


if __name__ == "__main__":
    unittest.main()
