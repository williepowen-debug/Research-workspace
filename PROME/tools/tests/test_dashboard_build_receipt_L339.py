#!/usr/bin/env python3
"""Falsification set for the L339 repair — a FAILED dashboard build must not leave a PASSING gate.

Defect: fleet_dashboard.py writes dashboard_state.json ONLY on a clean build, so a failing build left the
previous snapshot in place, returned rc=1 with nothing on stdout or stderr, and prome_gate's dashboard checks
then certified that stale snapshot and passed.

Test list = the acceptance conditions written BEFORE the edit
(PROME/proposals/2026-09-11_L339-dashboard-build-gate-PROPOSAL.md §1), not the bug report.

Frozen fixtures in a tempdir — never the live tree (a test pinned to a live surface rots on its next edit).
Run: python3 -W error::ResourceWarning -m unittest PROME/tools/tests/test_dashboard_build_receipt_L339.py
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import prome_gate  # noqa: E402
import fleet_dashboard  # noqa: E402

STAMP_OK = "2026-09-11 22:56"
STAMP_NEW = "2026-09-11 23:30"


def snapshot(built):
    """A snapshot that passes every PRE-EXISTING dashboard check, so the only
    thing a failure can come from is the L339 receipt check itself."""
    return {"v": 1, "built": built,
            "one": "A reported strike on the Petroline put Brent at $107.63 and the marks did not move.",
            "split": "20/47/33", "channels": {"Energy": "crit"},
            "levels": {f"t{i}": str(i) for i in range(8)},
            "gates": {}, "docket": [], "fleet": {}, "pending": []}


class GateFixture:
    """Throwaway ROOT + helpers. Fixture only — no tests, so inheriting it does
    not silently re-run another class's suite (which would inflate a count the
    tests README says must be measured, never remembered)."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        (self.root / "PROME/tools").mkdir(parents=True)
        (self.root / "HEARTBEAT.md").write_text("# HEARTBEAT\n", encoding="utf-8")
        self._saved_root = prome_gate.ROOT
        prome_gate.ROOT = self.root
        prome_gate.results.clear()
        self.addCleanup(self._restore)

    def _restore(self):
        prome_gate.ROOT = self._saved_root
        prome_gate.results.clear()
        self._tmp.cleanup()

    def write_state(self, built):
        (self.root / "PROME/tools/dashboard_state.json").write_text(
            json.dumps(snapshot(built)), encoding="utf-8")

    def write_receipt(self, attempted, ok, errors=()):
        (self.root / "PROME/tools/dashboard_build.json").write_text(
            json.dumps({"v": 1, "attempted": attempted, "ok": ok, "errors": list(errors)}),
            encoding="utf-8")

    def run_gate(self):
        prome_gate.results.clear()
        prome_gate.check_dashboard_state()
        return list(prome_gate.results)

    def blocking_failures(self, res):
        return [r for r in res if r[0] == prome_gate.BLOCK and not r[2]]

    def named(self, res, fragment):
        return [r for r in res if fragment in r[1]]


class ReceiptGateCase(GateFixture, unittest.TestCase):
    """Drives prome_gate.check_dashboard_state() against a throwaway ROOT."""

    # ---- A4 · ordinary: the success path must still pass -------------------
    def test_A4_successful_build_gate_passes(self):
        self.write_state(STAMP_OK)
        self.write_receipt(STAMP_OK, ok=True)
        res = self.run_gate()
        self.assertEqual(self.blocking_failures(res), [],
                         "a clean build must leave every blocking dashboard check green")

    # ---- A1 · the reported defect: failed build => gate must NOT pass ------
    def test_A1_failed_build_blocks_the_gate(self):
        self.write_state(STAMP_OK)          # stale snapshot from an earlier clean build
        self.write_receipt(STAMP_NEW, ok=False,
                           errors=["each HEARTBEAT amendment needs one reviewed dashboard projection"])
        res = self.run_gate()
        self.assertTrue(self.blocking_failures(res),
                        "a failed build left every blocking check green — this IS the L339 defect")

    # ---- A2 · the error text must reach the operator, not just an rc ------
    def test_A2_build_errors_are_visible_in_the_gate_detail(self):
        self.write_state(STAMP_OK)
        self.write_receipt(STAMP_NEW, ok=False, errors=["unclosed dashboard amendment block"])
        detail = " ".join(r[3] for r in self.run_gate())
        self.assertIn("unclosed dashboard amendment block", detail,
                      "the operator must be able to read WHY the build failed, from the gate alone")

    # ---- A3 · snapshot older than the build that was run ------------------
    def test_A3_snapshot_older_than_last_build_is_refused(self):
        self.write_state(STAMP_OK)
        self.write_receipt(STAMP_NEW, ok=True)   # a later build succeeded but did not produce this file
        res = self.run_gate()
        self.assertTrue(self.blocking_failures(res),
                        "the gate must refuse a snapshot that is not the latest build's output")

    # ---- A6 · missing information is NOT the same as a failed build -------
    def test_A6_missing_receipt_blocks_and_is_distinguishable(self):
        self.write_state(STAMP_OK)               # no receipt written at all
        res = self.run_gate()
        fails = self.blocking_failures(res)
        self.assertTrue(fails, "no receipt must fail closed, never silently pass")
        self.assertIn("NO BUILD RECEIPT", " ".join(r[3] for r in fails))
        self.assertNotIn("LAST BUILD FAILED", " ".join(r[3] for r in fails),
                         "absent evidence must not be reported as a failed build")

    # ---- A5 · content stamps only; mtime must not rescue a stale file -----
    def test_A5_fresh_mtime_does_not_certify_a_stale_snapshot(self):
        self.write_receipt(STAMP_NEW, ok=False, errors=["boom"])
        self.write_state(STAMP_OK)     # written LAST => newest mtime in the fixture
        res = self.run_gate()
        self.assertTrue(self.blocking_failures(res),
                        "a freshly touched file must not read as current — git sync restamps mtime")

    # ---- 2 · OVERLAP: the category whose miss kept the last repair open ---
    def test_overlap_failed_then_successful_build_clears(self):
        """The record must not latch: a failure followed by a clean build passes again."""
        self.write_state(STAMP_OK)
        self.write_receipt(STAMP_NEW, ok=False, errors=["boom"])
        self.assertTrue(self.blocking_failures(self.run_gate()))
        self.write_state(STAMP_NEW)              # the repair build produces its own snapshot
        self.write_receipt(STAMP_NEW, ok=True)
        self.assertEqual(self.blocking_failures(self.run_gate()), [],
                         "a fixed build must clear the block, or the gate is unrecoverable")

    def test_overlap_failed_build_whose_snapshot_is_already_current(self):
        """Same stamp on both, but the build FAILED. `ok` decides, not the stamps."""
        self.write_state(STAMP_NEW)
        self.write_receipt(STAMP_NEW, ok=False, errors=["attention renderer raised"])
        self.assertTrue(self.blocking_failures(self.run_gate()),
                        "matching stamps must not launder a failed build")

    # ---- 4 · missing information, second shape: unreadable record ---------
    def test_corrupt_receipt_fails_closed(self):
        self.write_state(STAMP_OK)
        (self.root / "PROME/tools/dashboard_build.json").write_text("{not json", encoding="utf-8")
        self.assertTrue(self.blocking_failures(self.run_gate()),
                        "an unreadable receipt must fail closed, never be skipped")

    # ---- falsify the guard: it must be able to PASS, not just always fail --
    def test_guard_is_not_always_on(self):
        self.write_state(STAMP_OK)
        self.write_receipt(STAMP_OK, ok=True)
        self.assertTrue(self.named(self.run_gate(), "L339"),
                        "the L339 check must run at all")
        self.assertEqual(self.blocking_failures(self.run_gate()), [],
                         "a guard that cannot pass is decoration")

    # ---- the stale-note must travel onto the checks that read the file ----
    def test_stale_note_marks_the_checks_that_read_the_stale_file(self):
        self.write_state(STAMP_OK)
        self.write_receipt(STAMP_NEW, ok=False, errors=["boom"])
        panels = self.named(self.run_gate(), "panels nonempty")[0]
        self.assertIn("STALE SNAPSHOT", panels[3],
                      "a green line over a stale snapshot is the shape that let the failure ship")


class ReceiptWriterCase(unittest.TestCase):
    """Drives fleet_dashboard.write_build_receipt against a throwaway path."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self._saved = fleet_dashboard.BUILD_PATH
        fleet_dashboard.BUILD_PATH = str(self.root / "dashboard_build.json")
        self.addCleanup(self._restore)

    def _restore(self):
        fleet_dashboard.BUILD_PATH = self._saved
        self._tmp.cleanup()

    def read(self):
        return json.loads(Path(fleet_dashboard.BUILD_PATH).read_text())

    def test_failure_records_ok_false_with_errors(self):
        fleet_dashboard.write_build_receipt(STAMP_NEW, ["projection missing"])
        r = self.read()
        self.assertFalse(r["ok"])
        self.assertEqual(r["attempted"], STAMP_NEW)
        self.assertEqual(r["errors"], ["projection missing"])

    def test_success_records_ok_true(self):
        fleet_dashboard.write_build_receipt(STAMP_OK, [])
        self.assertTrue(self.read()["ok"])

    def test_no_tmp_file_is_left_behind(self):
        """Atomic rename — category 5's mitigation; a torn read must be impossible."""
        fleet_dashboard.write_build_receipt(STAMP_OK, [])
        self.assertEqual(list(self.root.glob("*.tmp")), [])


class MainPathCase(unittest.TestCase):
    """Drives fleet_dashboard.main() end to end.

    Added after the independent read (2026-09-11): every ❌ it found lived in
    main() — the crash path, the preview path, the receipt schema — and the
    original 14 tests drove only the writer and the gate, so 14/14 green and the
    holes coexisted. `finding_adoption_is_not_validation`."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self._saved = (fleet_dashboard.BUILD_PATH, fleet_dashboard.STATE_PATH,
                       fleet_dashboard.build, sys.argv)
        fleet_dashboard.BUILD_PATH = str(self.root / "dashboard_build.json")
        fleet_dashboard.STATE_PATH = str(self.root / "dashboard_state.json")
        self.addCleanup(self._restore)

    def _restore(self):
        (fleet_dashboard.BUILD_PATH, fleet_dashboard.STATE_PATH,
         fleet_dashboard.build, sys.argv) = self._saved
        self._tmp.cleanup()

    def receipt(self):
        return json.loads(Path(fleet_dashboard.BUILD_PATH).read_text())

    def seed_clean_receipt(self):
        """A receipt from a PREVIOUS successful build — the state a crash inherits."""
        Path(fleet_dashboard.BUILD_PATH).write_text(
            json.dumps({"v": 1, "attempted": STAMP_OK, "ok": True, "errors": []}))

    def run_main(self, *extra):
        sys.argv = ["fleet_dashboard.py", "-o", str(self.root / "out.html"), *extra]
        import io
        from contextlib import redirect_stdout, redirect_stderr
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            try:
                rc = fleet_dashboard.main()
            except Exception as e:
                rc = e
        return rc, out.getvalue(), err.getvalue()

    def set_build(self, errors=(), raises=None):
        def fake(today, built, sessions_json=None):
            if raises:
                raise raises
            return "<html></html>", {"v": 1, "built": built, "heartbeat_errors": list(errors),
                                     "attention_errors": [], "one": "x" * 60, "split": "1",
                                     "channels": {}, "gates": {}, "docket": [], "fleet": {},
                                     "pending": [], "levels": {}}
        fleet_dashboard.build = fake

    # ---- ❌1: a build that RAISES must record itself as a failure ----------
    def test_crashed_build_overwrites_a_stale_ok_receipt(self):
        self.seed_clean_receipt()
        self.set_build(raises=ValueError("day is out of range for month"))
        rc, _, err = self.run_main()
        self.assertIsInstance(rc, ValueError, "the crash must still propagate")
        r = self.receipt()
        self.assertFalse(r["ok"], "a crashed build left the previous ok:true receipt — "
                                  "this is L339 reached by a different door")
        self.assertIn("did not complete", " ".join(r["errors"]))
        self.assertIn("BUILD CRASHED", err, "a crash must be visible to the operator")

    def test_crashed_preview_writes_no_receipt(self):
        """A preview asserts nothing about the baseline, even when it crashes (A7)."""
        self.seed_clean_receipt()
        self.set_build(raises=RuntimeError("boom"))
        self.run_main("--no-snapshot")
        self.assertTrue(self.receipt()["ok"], "a preview must not overwrite the baseline record")

    # ---- ❌3: a FAILING preview must still show the operator the errors ----
    def test_failing_preview_prints_errors_to_stderr(self):
        self.set_build(errors=["each HEARTBEAT amendment needs one reviewed dashboard projection"])
        rc, _, err = self.run_main("--no-snapshot")
        self.assertEqual(rc, 1)
        self.assertIn("reviewed dashboard projection", err,
                      "rc=1 with an empty stderr is the original symptom, new string")

    def test_failing_preview_still_writes_no_receipt(self):
        self.set_build(errors=["boom"])
        self.run_main("--no-snapshot")
        self.assertFalse(Path(fleet_dashboard.BUILD_PATH).exists(), "A7: preview records nothing")

    # ---- the hole the FIRST correction missed: failure AFTER build() -------
    def test_output_write_failure_still_records_a_failed_build(self):
        """Reproduced 2026-09-11 against c6889828f: build() returned errors, the
        HTML write then raised (missing -o directory), the except-handler wrapped
        only build() so it never ran, the previous ok:true receipt survived and
        the gate PASSED. An except-handler is scoped to what it wraps."""
        self.seed_clean_receipt()
        self.set_build(errors=["each HEARTBEAT amendment needs one reviewed dashboard projection"])
        sys.argv = ["fleet_dashboard.py", "-o", str(self.root / "no_such_dir" / "out.html")]
        import io
        from contextlib import redirect_stdout, redirect_stderr
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            with self.assertRaises(OSError):
                fleet_dashboard.main()
        self.assertFalse(self.receipt()["ok"],
                         "a run that could not produce its outputs left an ok:true receipt")

    def test_receipt_is_failed_before_any_work_happens(self):
        """Fail-closed by default: the record says not-completed from the first
        moment, so a process KILL — which no except-handler can catch — also
        leaves the gate blocking rather than certifying the old snapshot."""
        self.seed_clean_receipt()
        seen = {}

        def spy(today, built, sessions_json=None):
            seen["receipt_during_build"] = self.receipt()
            raise KeyboardInterrupt("operator killed the run")
        fleet_dashboard.build = spy
        sys.argv = ["fleet_dashboard.py", "-o", str(self.root / "out.html")]
        import io
        from contextlib import redirect_stdout, redirect_stderr
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            with self.assertRaises(KeyboardInterrupt):
                fleet_dashboard.main()
        self.assertFalse(seen["receipt_during_build"]["ok"],
                         "the receipt must already read ok:false while the build is still running")

    def test_preview_writes_no_receipt_even_when_output_write_fails(self):
        """A7 holds on the new pre-write path: a preview still asserts nothing."""
        self.set_build()
        sys.argv = ["fleet_dashboard.py", "--no-snapshot",
                    "-o", str(self.root / "no_such_dir" / "out.html")]
        import io
        from contextlib import redirect_stdout, redirect_stderr
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            with self.assertRaises(OSError):
                fleet_dashboard.main()
        self.assertFalse(Path(fleet_dashboard.BUILD_PATH).exists())

    # ---- ordinary: the success path through main() -------------------------
    def test_clean_build_writes_both_files_with_the_same_stamp(self):
        self.set_build()
        rc, out, err = self.run_main()
        self.assertEqual(rc, 0)
        self.assertEqual(err, "", "a clean build must say nothing on stderr")
        state = json.loads(Path(fleet_dashboard.STATE_PATH).read_text())
        self.assertEqual(state["built"], self.receipt()["attempted"],
                         "the gate compares these two stamps; a clean build must make them agree")


class ReceiptSchemaCase(GateFixture, unittest.TestCase):
    """❌2: a receipt that is valid JSON but not an object must BLOCK, never raise.
    An AttributeError out of this check aborts every LATER gate check silently."""

    def _drive(self, raw):
        self.write_state(STAMP_OK)
        (self.root / "PROME/tools/dashboard_build.json").write_text(raw, encoding="utf-8")
        try:
            res = self.run_gate()
        except Exception as e:
            self.fail(f"gate raised {type(e).__name__} on receipt {raw!r} — "
                      "every check after this one would never run")
        self.assertTrue(self.blocking_failures(res), f"receipt {raw!r} must fail closed")

    def test_list_receipt_blocks(self):
        self._drive("[]")

    def test_null_receipt_blocks(self):
        self._drive("null")

    def test_string_receipt_blocks(self):
        self._drive('"ok"')

    def test_number_receipt_blocks(self):
        self._drive("3")

    def test_mismatch_message_states_the_direction_it_can_prove(self):
        """⚠️5: the message asserted OLDER unconditionally; a NEWER state proved it false."""
        self.write_state(STAMP_NEW)
        self.write_receipt(STAMP_OK, ok=True)
        detail = " ".join(r[3] for r in self.blocking_failures(self.run_gate()))
        self.assertIn("NEWER than", detail)


if __name__ == "__main__":
    unittest.main()
