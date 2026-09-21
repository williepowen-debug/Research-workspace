"""Boot coverage acceptance: all mutable inputs are owned temporary fixtures."""
import contextlib
import datetime as dt
import importlib.util
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO = Path(__file__).resolve().parents[3]


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, REPO / path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


docket = module("coverage_docket", "scripts/docket_view.py")
gate = module("coverage_gate", "PROME/tools/prome_gate.py")
readcap = module("coverage_readcap", "scripts/read_cap_check.py")
DAY = dt.date(2026, 9, 21)


class Fixtures(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="boot-coverage-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for obj, value in ((docket, str(self.root)), (gate, self.root), (readcap, str(self.root))):
            self.enterContext(patch.object(obj, "ROOT", value))
        self.enterContext(patch.object(gate, "LOG_DIR", self.root))
        self.enterContext(patch.object(gate, "results", []))
        self.enterContext(patch.object(readcap, "READS_TSV", str(self.root / "reads.tsv")))
        self.dk, self.view = self.root / "docket.tsv", self.root / "view.md"
        self.dk.write_text("date\tcatalyst\towners\tstate\tartifacts\tnotes\n"
                           "2026-09-22\tAlpha earnings\tALPHA\tPENDING\t-\t-\n")
        self.view.write_text(docket.BEGIN + "\n" + docket.END + "\n")
        self.capture(docket.write_view, str(self.view), str(self.dk), DAY, brief_chars=45)

    def capture(self, fn, *args, **kwargs):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            rc = fn(*args, **kwargs)
        return rc, output.getvalue()

    def generated(self, day=DAY, **kwargs):
        return self.capture(docket.check_generated, str(self.view), str(self.dk), day,
                            brief_chars=45, **kwargs)

    def prose(self):
        return self.capture(docket.check_view, str(self.view), str(self.dk), DAY)

    def run_cli(self, *args):
        return subprocess.run([sys.executable, "-B", str(REPO / "scripts/docket_view.py"),
                               "--docket", str(self.dk), *args], cwd=self.root,
                              capture_output=True, text=True)

    def manifest(self, reads):
        rows = ["ATTESTATION\tPROME\t.\tmanifest-complete\ts\tPROME\t2026-09-21\tok"]
        rows += [f"READ\tPROME\t{p}\twhole\ts\tPROME\t2026-09-21\tfixture" for p in reads]
        (self.root / "reads.tsv").write_text(readcap.HDR + "\n" + "\n".join(rows) + "\n")

    def test_fresh_and_handwritten_changes_do_not_stale_generated(self):
        before = self.view.read_bytes()
        rc, out = self.generated()
        self.assertEqual(rc, 0)
        self.assertTrue(gate.summarize_generated(out, rc)[0])
        self.assertEqual(self.view.read_bytes(), before)
        self.view.write_text(self.view.read_text() + "\n9/23 Alpha earnings (L2)\n")
        self.assertEqual(self.generated()[0], 0)
        self.assertEqual(self.prose()[0], 1)

    def test_deadline_changed_without_render_is_stale_even_when_prose_passes(self):
        self.dk.write_text(self.dk.read_text().replace("2026-09-22", "2026-09-23"))
        self.assertEqual(self.generated()[0], 1)
        rc, out = self.prose()
        self.assertEqual(rc, 0)
        self.assertIn("EMPTY", gate.summarize_prose(out, rc)[1])

    def test_clock_advance_with_identical_files_is_stale(self):
        before = (self.dk.read_bytes(), self.view.read_bytes())
        self.assertEqual(self.generated(DAY + dt.timedelta(days=1))[0], 1)
        self.assertEqual(before, (self.dk.read_bytes(), self.view.read_bytes()))

    def test_options_are_caller_owned(self):
        self.assertEqual(self.generated(window=22)[0], 1)

    def test_default_clock_uses_et(self):
        instant = dt.datetime(2026, 9, 21, 23, 59)
        with patch.object(docket.dt, "datetime") as clock:
            clock.now.return_value = instant
            self.assertEqual(docket.et_today(), DAY)
            self.assertEqual(str(clock.now.call_args.args[0]), "America/New_York")

    def test_marker_failures(self):
        fresh = self.view.read_text()
        cases = ["", fresh.replace(docket.BEGIN, ""), fresh + docket.END,
                 docket.END + "\n" + docket.BEGIN, fresh.replace(docket.BEGIN, "x" + docket.BEGIN),
                 fresh.replace(docket.END, "<!-- DOCKET-VIEW END --> broken"),
                 fresh + "\n<!-- DOCKET-VIEW BROKEN -->"]
        for text in cases:
            with self.subTest(text=text[:50]):
                self.view.write_text(text)
                with self.assertRaises(docket.DocketError):
                    self.generated()
                self.assertEqual(self.view.read_text(), text)

    def test_bad_sources_cli_cannot_certify(self):
        good = self.dk.read_text()
        for source in [b"", b"ragged\trow\n", b"\xff",
                       good.replace("2026-09-22", "2026-02-30").encode(),
                       good.replace("2026-09-22", "2026-09-23..2026-09-22").encode(),
                       *(good.replace("2026-09-22", span).encode() for span in
                         ("2026-9-22", "2026.09.22", "2026–09–22", "20260922", "9/22/2026"))]:
            with self.subTest(source=source):
                self.dk.write_bytes(source)
                p = self.run_cli("--check-generated", str(self.view), "--as-of", str(DAY))
                self.assertEqual(p.returncode, 2, p.stdout + p.stderr)
                self.assertFalse(gate.summarize_generated(p.stdout, p.returncode)[0])
        self.dk.unlink()
        self.assertEqual(self.run_cli("--check-generated", str(self.view)).returncode, 2)
        self.dk.mkdir()  # Unreadable as a file even when the test process runs as root.
        self.assertEqual(self.run_cli("--check-generated", str(self.view)).returncode, 2)

    def test_symbolic_session_key_remains_renderable(self):
        self.dk.write_text(self.dk.read_text().replace("2026-09-22", "next-PROME-session"))
        self.assertEqual(self.run_cli("--write", str(self.view), "--as-of", str(DAY)).returncode, 0)
        p = self.run_cli("--check-generated", str(self.view), "--as-of", str(DAY))
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)

    def test_identical_content_atomic_replacement_is_detected(self):
        render = docket.render
        def replace(*args, **kw):
            result = render(*args, **kw)
            other = self.root / "replacement.tsv"
            other.write_bytes(self.dk.read_bytes())
            other.replace(self.dk)
            return result
        with patch.object(docket, "render", side_effect=replace):
            with self.assertRaisesRegex(docket.DocketError, "changed before verdict"):
                self.generated()

    def test_cli_write_check_parity(self):
        self.assertEqual(self.run_cli("--write", str(self.view), "--as-of", str(DAY)).returncode, 0)
        self.assertEqual(self.run_cli("--check-generated", str(self.view), "--as-of", str(DAY)).returncode, 0)
        self.assertEqual(self.run_cli("--check-generated", str(self.view), "--skip-ragged").returncode, 2)
        self.assertEqual(self.run_cli("--check-generated", str(self.view), "--as-of", "bad").returncode, 2)

    def test_concurrent_source_or_destination_change_cannot_certify(self):
        render = docket.render
        for path in (self.dk, self.view):
            with self.subTest(path=path.name):
                def mutate(*args, **kw):
                    result = render(*args, **kw)
                    path.write_text(path.read_text() + "\n")
                    return result
                with patch.object(docket, "render", side_effect=mutate):
                    with self.assertRaisesRegex(docket.DocketError, "changed before verdict"):
                        self.generated()

    def test_prose_unmatched_and_undated_citation_are_unassessed(self):
        for text in ("9/22 Unrelated ceremony", "9/22 Alpha earnings (L2)"):
            with self.subTest(text=text):
                self.dk.write_text(self.dk.read_text().replace("2026-09-22", "SESSION"))
                self.view.write_text(text)
                rc, out = self.prose()
                self.assertEqual(rc, 0)  # Existing prose exit contract preserved.
                ok, summary = gate.summarize_prose(out, rc)
                self.assertFalse(ok)
                self.assertIn("unassessed=1", summary)

    def test_readcap_producer_size_manifest_and_rotation(self):
        p = self.root / "PROME/ACTIVE_DECISIONS.md"
        p.parent.mkdir()
        for size, expected_rc in ((100, 0), (25000, 0), (40000, 1), (60000, 1)):
            with self.subTest(size=size):
                p.write_text("x" * size)
                self.manifest(["PROME/ACTIVE_DECISIONS.md"])
                rc, out = self.capture(readcap.main, ["read_cap_check.py", "--agent", "PROME", "--require-manifest"])
                self.assertEqual(rc, expected_rc)
                ok, summary = gate.summarize_read_cap(out, rc)
                self.assertEqual(ok, size == 100)
                self.assertIn("assessed=1", summary)
                self.assertIn(f"active_decisions_over_budget={int(size >= readcap.BUDGET_BYTES)}", summary)
        self.manifest(["PROME/ACTIVE_DECISIONS.md", "absent.md"])
        rc, out = self.capture(readcap.main, ["read_cap_check.py", "--agent", "PROME", "--require-manifest"])
        self.assertIn("manifest_defects=1", gate.summarize_read_cap(out, rc)[1])

    def test_manifest_missing_malformed_or_desk_absent_no_fallback(self):
        for text in (None, "bad header\n", readcap.HDR + "\n"):
            with self.subTest(text=text):
                if text is not None:
                    (self.root / "reads.tsv").write_text(text)
                rc, out = self.capture(readcap.main, ["read_cap_check.py", "--agent", "PROME", "--require-manifest"])
                self.assertEqual(rc, 2)
                ok, summary = gate.summarize_read_cap(out, rc)
                self.assertFalse(ok)
                self.assertIn("counts are unearned", summary)

    def test_structured_readcap_invalid_output(self):
        valid = ("READ-CAP-RESULT v1 mode=agent rc=0 assessed=1 desk=PROME reads=1 over_budget=0 "
                 "over_cap=0 manifest_defects=0 advisories=0 generated_flagged=0 rotation_due=0 "
                 "active_decisions_over_budget=0")
        for text, rc in [("", 0), (valid + "\n" + valid, 0), (valid + " reads=1", 0),
                         (valid.replace("PROME", "CATO"), 0), (valid, 1),
                         (valid.replace("assessed=1", "assessed=0"), 0),
                         (valid.replace("reads=1", "reads=-1"), 0),
                         (valid.replace("over_budget=0", "over_budget=1"), 0),
                         (valid.replace("rotation_due=0", "rotation_due=2"), 0)]:
            with self.subTest(text=text, rc=rc), self.assertRaises(ValueError):
                gate.summarize_read_cap(text, rc)
        ok, summary = gate.summarize_read_cap(valid.replace("rc=0", "rc=2"), 2)
        self.assertFalse(ok)
        self.assertIn("CANNOT-CERTIFY", summary)
        self.assertIn("assessed=1", summary)

    def test_wrapper_retains_success_coverage_and_unknown(self):
        line = "DOCKET-PROSE-RESULT v1 rc=0 matched=0 dated=0 assessed=0 unassessed=0 ignored=0 generated=excluded"
        for body in (line, "broken result"):
            ok = gate.run_script(gate.ADVISE, "fixture", [sys.executable, "-c", f"print({body!r})"],
                                 "fixture", summarize=gate.summarize_prose)
            self.assertEqual(ok, body == line)
            self.assertIn("EMPTY" if ok else "UNKNOWN", gate.results[-1][3])
            self.assertIn("full output:", gate.results[-1][3])
        self.assertEqual(gate.aggregate_rc(gate.results, []), 0)  # Advisory findings remain advisory.

    def test_budget_failure_does_not_suppress_memory(self):
        (self.root / "scripts").mkdir()
        (self.root / "memory/auto").mkdir(parents=True)
        (self.root / "scripts/harness_caps.env").write_text("MEMORY_HARNESS_CAP_BYTES=100\n")
        (self.root / "memory/auto/MEMORY.md").write_text("x" * 80)
        with patch.object(gate, "run_script", return_value=False) as run:
            gate.check_byte_budgets()
            self.assertIn("--require-manifest", run.call_args.args[2])
        self.assertEqual(gate.results[-1][1], "auto-memory byte budget")
        self.assertFalse(gate.results[-1][2])
        (self.root / "scripts/harness_caps.env").write_text("MEMORY_HARNESS_CAP_BYTES=0\n")
        gate.check_memory_budget()
        self.assertIn("UNKNOWN", gate.results[-1][3])

    def test_both_modes_wire_independent_calendar_and_budget_checks(self):
        for mode in (gate.mode_boot, gate.mode_closeout):
            with self.subTest(mode=mode.__name__):
                def guard(fn, *args, **kw):
                    if fn in (gate.check_calendar_views, gate.check_byte_budgets):
                        fn(*args, **kw)
                with patch.object(gate, "guard", side_effect=guard), \
                     patch.object(gate, "run_capability"), patch.object(gate, "run_script") as run:
                    mode()
                calls = run.call_args_list
                for flag in ("--check-generated", "--require-manifest"):
                    self.assertEqual(sum(flag in c.args[2] for c in calls), 1)
                calendar = [c for c in calls if "scripts/docket_view.py" in c.args[2]]
                self.assertEqual(len(calendar), 2)
                self.assertEqual(calendar[0].args[2][3], calendar[1].args[2][3])
                self.assertTrue(all(c.args[0] == gate.ADVISE and "summarize" in c.kwargs for c in calendar))


if __name__ == "__main__":
    unittest.main()
