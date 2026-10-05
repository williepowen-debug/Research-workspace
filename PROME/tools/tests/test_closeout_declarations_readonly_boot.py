#!/usr/bin/env python3
"""2026-10-05 reviewer bundle: (a) `prome_gate.py boot` is NON-ADVANCING unless --advance-board;
boot_session.run_once is the only caller that passes it. (b) closeout root steps 1c/1d are
declaration-gated BLOCKING rows; 1e runs mechanically. Pure tests: every subprocess is
patched; nothing here touches BOARD state, memory/auto/ or any live surface."""
import contextlib
import io
import pathlib
import subprocess
import sys
import unittest
from unittest.mock import patch

HERE = pathlib.Path(__file__).resolve()
TOOLS = HERE.parents[1]
sys.path.insert(0, str(TOOLS))
import prome_gate as gate      # noqa: E402
import boot_session as session  # noqa: E402


def quiet(fn, *a, **k):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            rc = fn(*a, **k)
        except SystemExit as e:
            rc = e.code
    return rc, buf.getvalue()


class ReadOnlyBoot(unittest.TestCase):
    def test_bare_boot_never_advances(self):
        with patch.object(sys, "argv", ["prome_gate.py", "boot"]), \
             patch.object(gate, "mode_boot") as boot, patch.object(gate, "mode_closeout") as close:
            self.assertEqual(quiet(gate.main)[0], 0)
            boot.assert_called_once_with(advance_board=False)
            close.assert_not_called()

    def test_flag_advances(self):
        with patch.object(sys, "argv", ["prome_gate.py", "boot", "--advance-board"]), \
             patch.object(gate, "mode_boot") as boot:
            self.assertEqual(quiet(gate.main)[0], 0)
            boot.assert_called_once_with(advance_board=True)

    def test_refresh_and_closeout_reject_the_flag(self):
        for argv in (["prome_gate.py", "refresh", "--advance-board"],
                     ["prome_gate.py", "closeout", "--advance-board", "--no-memory", "--no-superseded"]):
            with patch.object(sys, "argv", argv), patch.object(gate, "mode_boot"), \
                 patch.object(gate, "mode_closeout"), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(quiet(gate.main)[0], 2)

    def test_board_scan_gets_advance_only_with_flag(self):
        def capture(flag):
            calls = []
            with patch.object(gate, "run_script", side_effect=lambda *a, **k: calls.append(a)), \
                 patch.object(gate, "run_capability"), patch.object(gate, "guard"), \
                 patch.object(gate, "SESSION_JSON", None):
                gate.mode_boot(advance_board=flag)
            return [a[2] for a in calls if a[1] == "board_scan"][0]
        self.assertNotIn("--advance", capture(False))
        self.assertIn("--advance", capture(True))

    def test_boot_session_one_shot_is_the_advancing_caller(self):
        seen = {}
        def child(cmd, **kw):
            seen["cmd"] = cmd
            kw["stdout"].write("x\n")
            return subprocess.CompletedProcess(cmd, 0)
        import tempfile
        with tempfile.TemporaryDirectory() as d, patch.object(session.subprocess, "run", side_effect=child):
            quiet(session.run_once, pathlib.Path(d) / "boot")
        self.assertEqual(seen["cmd"][2], "boot")
        self.assertIn("--advance-board", seen["cmd"])


class Declarations(unittest.TestCase):
    def setUp(self):
        gate.results.clear()

    def rows(self, name):
        return [r for r in gate.results if r[1].startswith(name)]

    def test_undeclared_is_blocking(self):
        gate.check_memory_declared(None)
        gate.check_consumer_declared(None)
        for name in ("memory_index_check", "consumer_check"):
            (sev, _, ok, detail, _), = self.rows(name)
            self.assertEqual((sev, ok), (gate.BLOCK, False))
            self.assertIn("UNDECLARED", detail)
        self.assertEqual(gate.aggregate_rc(gate.results, []), 1)

    def test_declared_none_passes_and_hints_dirty_memory(self):
        with patch.object(gate, "_dirty_memory_paths", return_value=["memory/auto/x.md"]):
            gate.check_memory_declared([])
        gate.check_consumer_declared([])
        (sev, _, ok, detail, _), = self.rows("memory_index_check")
        self.assertEqual((sev, ok), (gate.BLOCK, True))
        self.assertIn("1 uncommitted path", detail)
        self.assertTrue(self.rows("consumer_check")[0][2])
        self.assertEqual(gate.aggregate_rc(gate.results, []), 0)

    def test_slugs_run_strict_per_slug_and_rc1_blocks(self):
        calls = []
        def fake(sev, name, cmd, owner, ok_rc=(0,), summarize=None):
            calls.append((sev, cmd))
            gate.record(sev, name, cmd[-1] != "bad", "rc", owner)
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            (pathlib.Path(d) / "memory/auto").mkdir(parents=True)
            for s in ("good", "bad"):
                (pathlib.Path(d) / "memory/auto" / f"{s}.md").write_text("x\n")
            with patch.object(gate, "run_script", side_effect=fake), patch.object(gate, "ROOT", pathlib.Path(d)):
                gate.check_memory_declared(["good", "bad"])
        strict = [c for s, c in calls if "memory_index_check.py" in " ".join(c)]
        self.assertEqual(len(strict), 2)
        for c in strict:
            self.assertIn("--strict", c)
            self.assertIn("--slug", c)
        self.assertEqual([s for s, c in calls if "memory_index_check.py" in " ".join(c)], [gate.BLOCK] * 2)
        self.assertEqual(gate.aggregate_rc(gate.results, []), 1)

    def test_slug_without_file_blocks_before_running_the_tool(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d, patch.object(gate, "run_script") as rs, \
             patch.object(gate, "ROOT", pathlib.Path(d)):
            gate.check_memory_declared(["typo"])
        strict = [c for c in rs.call_args_list if "memory_index_check.py" in " ".join(c.args[2])]
        self.assertEqual(strict, [])
        (sev, _, ok, detail, _), = self.rows("memory_index_check --strict --slug typo")
        self.assertEqual((sev, ok), (gate.BLOCK, False))
        self.assertIn("no memory/auto/typo.md", detail)

    def test_superseded_pairs_fleet_advisory_own_dir_blocking(self):
        calls = []
        with patch.object(gate, "run_script", side_effect=lambda *a, **k: calls.append((a[0], a[2]))):
            gate.check_consumer_declared([("7496", "7491")])
        self.assertEqual(len(calls), 2)
        self.assertTrue(all("--strict" in c and "--agent" in c and "PROME" in c for _, c in calls))
        fleet = [s for s, c in calls if "--self" not in c]
        own = [s for s, c in calls if "--self" in c]
        # Gap 1: another desk's 🔴 is discharged by a packet, so it must not block PROME's closeout.
        self.assertEqual((fleet, own), ([gate.ADVISE], [gate.BLOCK]))

    def test_consumer_summary_reads_the_footer_not_the_body(self):
        s = gate.summarize_consumer
        # Gap 2: 🟠 CANDIDATE is "needs verification", never clean — even with rc 0.
        ok, detail = s("  hits…\n  🟠 5 CANDIDATE(s), zero certified-stale. A 🟠 is a prompt to LOOK\n", 0)
        self.assertFalse(ok)
        self.assertIn("needs verification", detail)
        # 🔴 inside a quoted hit line is content, not a verdict; the footer is.
        ok, detail = s("  Brent **$88.66 🔴 [7/27 live]** quoted\n  ✓ clean — every consumer is current\n", 0)
        self.assertTrue(ok)
        ok, detail = s("  🔴 2 stale consumer reference(s). Send each owner a packet\n", 1)
        self.assertFalse(ok)
        self.assertIn("🔴 2 STALE", detail)
        with self.assertRaises(ValueError):          # no footer = no verdict (run_script records UNKNOWN)
            s("traceback…\n", 0)
        # PROME v3 fault injection: a 🟠 footer beside rc 1 or 2 is not a verdict — UNKNOWN, blocks.
        for rc in (1, 2):
            with self.assertRaises(ValueError):
                gate.parse_consumer("  🟠 2 CANDIDATE(s), zero certified-stale.\n", rc)
        self.assertEqual(gate.parse_consumer("  🔴 1 stale consumer reference(s).\n", 1), (1, 0, False))

    def test_own_dir_candidate_with_nonzero_rc_blocks_as_unknown(self):
        def fake(sev, name, cmd, owner, ok_rc=(0,), summarize=None):
            try:
                ok, detail = summarize("  🟠 2 CANDIDATE(s), zero certified-stale.\n", 2)
            except ValueError as exc:      # run_script's real handling of a summarizer ValueError
                ok, detail = False, f"UNKNOWN: {exc}"
            gate.record(sev, name, ok, detail, owner)
        with patch.object(gate, "run_script", side_effect=fake):
            gate.check_consumer_declared([("1", "2")])
        own = [r for r in gate.results if r[0] == gate.BLOCK and "own dir" in r[1]]
        self.assertEqual(len(own), 1)
        self.assertFalse(own[0][2])
        self.assertIn("UNKNOWN", own[0][3])
        self.assertEqual(gate.aggregate_rc(gate.results, []), 1)

    def test_own_dir_stale_blocks_but_candidate_is_advisory(self):
        """PROME v2 assessment: an unrelated '320 crates' must not block a 320→321 metric update."""
        def fake(sev, name, cmd, owner, ok_rc=(0,), summarize=None):
            body = ("  🟠 3 CANDIDATE(s), zero certified-stale.\n" if "--self" in cmd
                    else "  ✓ clean — every consumer is current.\n")
            ok, detail = summarize(body, 0)
            gate.record(sev, name, ok, detail, owner)
        with patch.object(gate, "run_script", side_effect=fake):
            gate.check_consumer_declared([("320", "321")])
        own_block = [r for r in gate.results if r[0] == gate.BLOCK and "own dir" in r[1]]
        own_adv = [r for r in gate.results if r[0] == gate.ADVISE and "own dir" in r[1]]
        self.assertEqual(len(own_block), 1)
        self.assertTrue(own_block[0][2], own_block[0][3])          # 🟠 alone does not block
        self.assertEqual(len(own_adv), 1)
        self.assertFalse(own_adv[0][2])
        self.assertIn("🟠 3 CANDIDATE", own_adv[0][3])
        self.assertEqual(gate.aggregate_rc(gate.results, []), 0)
        gate.results.clear()
        def stale(sev, name, cmd, owner, ok_rc=(0,), summarize=None):
            ok, detail = summarize("  🔴 1 stale reference(s) on YOUR OWN surfaces.\n", 1)
            gate.record(sev, name, ok, detail, owner)
        with patch.object(gate, "run_script", side_effect=stale):
            gate.check_consumer_declared([("1", "2")])
        self.assertEqual(gate.aggregate_rc(gate.results, []), 1)   # 🔴 on own surfaces still blocks

    def test_claims_run_mechanically_advisory(self):
        with patch.object(gate, "run_script") as rs:
            gate.check_claims()
        sev, name, cmd, owner = rs.call_args.args[:4]
        self.assertEqual(sev, gate.ADVISE)
        self.assertIn("claim_check.py", " ".join(cmd))
        self.assertIn("PROME/DOCKET.tsv", cmd)

    def test_cli_wires_declarations_into_closeout(self):
        with patch.object(sys, "argv", ["prome_gate.py", "closeout", "--tier", "light", "--slug", "a",
                                        "--superseded", "1", "2", "--superseded", "3", "4"]), \
             patch.object(gate, "mode_closeout") as close:
            self.assertEqual(quiet(gate.main)[0], 0)
            close.assert_called_once_with("light", memory=["a"], superseded=[("1", "2"), ("3", "4")])
        with patch.object(sys, "argv", ["prome_gate.py", "closeout", "--tier", "light"]), \
             patch.object(gate, "mode_closeout") as close:
            quiet(gate.main)
            close.assert_called_once_with("light", memory=None, superseded=None)

    def test_contradictory_declarations_are_usage_errors(self):
        for argv in (["closeout", "--no-memory", "--slug", "x", "--no-superseded"],
                     ["closeout", "--no-memory", "--no-superseded", "--superseded", "1", "2"],
                     ["boot", "--no-memory"]):
            with patch.object(sys, "argv", ["prome_gate.py", *argv]), patch.object(gate, "mode_boot"), \
                 patch.object(gate, "mode_closeout"), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(quiet(gate.main)[0], 2, argv)


if __name__ == "__main__":
    unittest.main()
