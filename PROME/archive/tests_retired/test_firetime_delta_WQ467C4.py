#!/usr/bin/env python3
"""Tests for PROME/tools/firetime_delta.py and its gate summary (WQ-467 C4). Acceptance:
PROME/tools/tests/ACCEPTANCE_firetime_delta_WQ467C4_2026-10-21.md (FD1-FD6). Temp files only;
the live baseline is never read or written."""
import pathlib
import sys
import tempfile
import unittest

HERE = pathlib.Path(__file__).resolve()
sys.path.insert(0, str(HERE.parents[1]))
import firetime_delta as fd  # noqa: E402
import prome_gate as g  # noqa: E402

LOG = """⚠️  AGENTS/WAL/STATUS.md
    ⚠️  DATE DRIFT: artifact says 2027-01-05 ('1/5') — matches no docket row but is near: Colorado (2026-12-31). VERIFY + full logic re-read.
⚠️  AGENTS/OZK/thread.md
    ⚠️  DATE DRIFT: artifact says 2026-12-25 ('Dec-25') — near: OZK SUB-NOTES (2026-12-24)
    ⚠️  DEAD POINTER: `reports/x.md` does not exist
✅ PROME/BOOT.md
    ·  predates cited `PROME/HANDOFF.md` by 1d — re-read if load-bearing
⚠️  778ef6a38:PROME/inbox/a.md
    ⚠️  UNREADABLE: [Errno 2] No such file or directory: 'x'

→ 4 flag(s). Rule: a DATE flag means FULL LOGIC RE-READ
"""


class Delta(unittest.TestCase):
    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        self.addCleanup(self.td.cleanup)
        self.base = pathlib.Path(self.td.name) / "b.tsv"

    def test_FD6_parse_counts_every_flag(self):
        flags, raw = fd.parse(LOG)
        self.assertEqual((len(flags), raw), (4, 4))
        self.assertIn(("AGENTS/OZK/thread.md", "DEAD POINTER", "`reports/x.md`"), flags)

    def test_FD3_no_baseline_means_all_new(self):
        flags, _ = fd.parse(LOG)
        new, old = fd.split(flags, fd.load_baseline(self.base))
        self.assertEqual((len(new), len(old)), (4, 0))

    def test_FD1_near_text_change_is_not_new(self):
        flags, _ = fd.parse(LOG)
        fd.accept(flags, None, "rec.md", self.base, today="2026-10-21")
        later = LOG.replace("near: Colorado (2026-12-31)", "near: SOMETHING ELSE (2027-01-02)")
        new, old = fd.split(fd.parse(later)[0], fd.load_baseline(self.base))
        self.assertEqual((len(new), len(old)), (0, 4))

    def test_FD1_new_flag_is_new(self):
        flags, _ = fd.parse(LOG)
        fd.accept(flags, None, "rec.md", self.base, today="2026-10-21")
        more = LOG.replace("⚠️  AGENTS/OZK/thread.md\n", "⚠️  AGENTS/OZK/thread.md\n    ⚠️  DATE DRIFT: artifact says 2026-11-30 ('11/30') — near: X\n")
        new, old = fd.split(fd.parse(more)[0], fd.load_baseline(self.base))
        self.assertEqual([n[2] for n in new], ["artifact says 2026-11-30 ('11/30')"])
        self.assertEqual(len(old), 4)

    def test_FD5_accept_keeps_first_date_and_drops_absent(self):
        flags, _ = fd.parse(LOG)
        fd.accept(flags, None, "first.md", self.base, today="2026-10-21")
        fewer = [f for f in flags if f[1] != "UNREADABLE"]
        extra = ("AGENTS/X.md", "DATE DRIFT", "artifact says 2026-11-01 ('11/1')")
        fd.accept(fewer + [extra], fd.load_baseline(self.base), "second.md", self.base, today="2026-10-22")
        b = fd.load_baseline(self.base)
        self.assertEqual(len(b), 4)
        self.assertEqual(b[flags[0]], ("2026-10-21", "first.md"))
        self.assertEqual(b[extra], ("2026-10-22", "second.md"))
        self.assertFalse(any(k[1] == "UNREADABLE" for k in b))

    def test_FD4_accept_requires_pointer(self):
        log = pathlib.Path(self.td.name) / "l.txt"
        log.write_text(LOG)
        rc = fd.main(["--log", str(log), "--baseline", str(self.base), "--accept"])
        self.assertEqual(rc, 2)
        self.assertFalse(self.base.exists())

    def test_FD6_orphan_flag_is_a_parse_miss(self):
        log = pathlib.Path(self.td.name) / "l.txt"
        log.write_text("    ⚠️  DATE DRIFT: artifact says 2027-01-01 ('1/1')\n" + LOG)
        self.assertEqual(fd.main(["--log", str(log), "--baseline", str(self.base)]), 2)

    def test_FD2_gate_summary_ok_only_when_nothing_new(self):
        flags, _ = fd.parse(LOG)
        real = g.ROOT
        try:
            g.ROOT = pathlib.Path(self.td.name)
            (g.ROOT / "PROME/state").mkdir(parents=True)
            ok, summ = g._firetime_delta_summary(LOG, 1)
            self.assertFalse(ok)
            self.assertIn("4 NEW", summ)
            self.assertIn("NO readable baseline", summ)
            fd.accept(flags, None, "rec.md", g.ROOT / "PROME/state/firetime_dispositioned.tsv")
            ok, summ = g._firetime_delta_summary(LOG, 1)
            self.assertTrue(ok)
            self.assertIn("0 NEW · 4 persisting (dispositioned at rec.md)", summ)
            with self.assertRaises(ValueError):
                g._firetime_delta_summary(LOG, 2)
        finally:
            g.ROOT = real


class ReadOneFixes(unittest.TestCase):
    """Independent read 1 (2026-10-21): ❌1 crash fails open, ❌2 stale rows, ⚠️4 accept guards."""

    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        self.addCleanup(self.td.cleanup)
        self.real = g.ROOT
        g.ROOT = pathlib.Path(self.td.name)
        (g.ROOT / "PROME/state").mkdir(parents=True)
        self.addCleanup(lambda: setattr(g, "ROOT", self.real))

    def test_X1_traceback_at_rc1_is_unknown_not_clean(self):
        tb = "Traceback (most recent call last):\n  File x\nKeyError: 'date'\n"
        with self.assertRaises(ValueError):
            g._firetime_delta_summary(tb, 1)

    def test_X1_partial_output_then_traceback_is_unknown(self):
        with self.assertRaises(ValueError):
            g._firetime_delta_summary(LOG.split("⚠️  AGENTS/OZK")[0] + "Traceback (most recent call last):\nValueError\n", 1)

    def test_X1_rc1_without_footer_is_unknown(self):
        with self.assertRaises(ValueError):
            g._firetime_delta_summary(LOG.split("\n→")[0], 1)

    def test_X1_footer_count_mismatch_is_unknown(self):
        with self.assertRaises(ValueError):
            g._firetime_delta_summary(LOG.replace("→ 4 flag(s)", "→ 9 flag(s)"), 1)

    def test_X1_rc0_with_flags_is_unknown(self):
        with self.assertRaises(ValueError):
            g._firetime_delta_summary(LOG, 0)

    def test_X1_clean_rc0_run_passes(self):
        fd.accept([], None, "rec.md", g.ROOT / "PROME/state/firetime_dispositioned.tsv")
        ok, summ = g._firetime_delta_summary("✅ PROME/BOOT.md\n", 0)
        self.assertTrue(ok)

    def test_X2_fixed_flag_still_in_baseline_is_owed(self):
        flags, _ = fd.parse(LOG)
        fd.accept(flags, None, "rec.md", g.ROOT / "PROME/state/firetime_dispositioned.tsv")
        fewer = LOG.replace("    ⚠️  DEAD POINTER: `reports/x.md` does not exist\n", "").replace("→ 4 flag(s)", "→ 3 flag(s)")
        ok, summ = g._firetime_delta_summary(fewer, 1)
        self.assertFalse(ok)
        self.assertIn("1 dispositioned flag(s) no longer reported", summ)

    def test_X4_accept_refuses_missing_pointer_file_and_incomplete_log(self):
        base = pathlib.Path(self.td.name) / "b.tsv"
        log = pathlib.Path(self.td.name) / "l.txt"
        log.write_text(LOG)
        self.assertEqual(fd.main(["--log", str(log), "--baseline", str(base), "--accept",
                                  "--pointer", "no/such/record.md"]), 2)
        log.write_text(LOG.split("\n→")[0])
        (fd.ROOT / "PROME/reports").exists()
        self.assertEqual(fd.main(["--log", str(log), "--baseline", str(base), "--accept",
                                  "--pointer", "PROME/BOOT.md"]), 2)
        self.assertFalse(base.exists())


class ReadTwoFixes(unittest.TestCase):
    """Independent read 2 (2026-10-21): ❌A prune while a NEW flag is deferred; ⚠️B accept input."""

    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        self.addCleanup(self.td.cleanup)
        self.d = pathlib.Path(self.td.name)
        self.base = self.d / "b.tsv"
        self.log = self.d / "l.txt"

    def _run(self, text, *extra):
        self.log.write_text(text)
        return fd.main(["--log", str(self.log), "--baseline", str(self.base), *extra])

    def test_XA_three_boot_sequence_with_prune(self):
        flags, _ = fd.parse(LOG)
        fd.accept(flags, None, "rec.md", self.base, today="2026-10-21")
        # boot 1: DEAD POINTER fixed, a NEW flag deferred — accept is NOT allowed, prune is
        boot1 = (LOG.replace("    ⚠️  DEAD POINTER: `reports/x.md` does not exist\n",
                             "    ⚠️  DATE DRIFT: artifact says 2026-11-30 ('11/30') — near: X\n"))
        self.assertEqual(self._run(boot1, "--prune"), 0)
        b = fd.load_baseline(self.base)
        self.assertNotIn(("AGENTS/OZK/thread.md", "DEAD POINTER", "`reports/x.md`"), b)
        self.assertNotIn(("AGENTS/OZK/thread.md", "DATE DRIFT", "artifact says 2026-11-30 ('11/30')"), b)  # prune adds nothing
        # boot 2: the fixed DEAD POINTER recurs — it must read NEW, not persisting
        new, old = fd.split(fd.parse(LOG)[0], fd.load_baseline(self.base))
        self.assertIn(("AGENTS/OZK/thread.md", "DEAD POINTER", "`reports/x.md`"), new)

    def test_XB_accept_refuses_empty_or_unrelated_log(self):
        flags, _ = fd.parse(LOG)
        fd.accept(flags, None, "rec.md", self.base, today="2026-10-21")
        before = self.base.read_text()
        self.assertEqual(self._run("", "--accept", "--pointer", "PROME/BOOT.md"), 2)
        self.assertEqual(self._run("hello world\n", "--accept", "--pointer", "PROME/BOOT.md"), 2)
        self.assertEqual(self._run("hello\n", "--prune"), 2)
        self.assertEqual(self.base.read_text(), before)

    def test_XB_accept_refuses_directory_pointer(self):
        self.assertEqual(self._run(LOG, "--accept", "--pointer", "."), 2)
        self.assertFalse(self.base.exists())

    def test_XB_zero_flag_complete_run_is_valid(self):
        self.assertIsNone(fd.validate("✅ PROME/BOOT.md\n", 0, None))


if __name__ == "__main__":
    unittest.main()
