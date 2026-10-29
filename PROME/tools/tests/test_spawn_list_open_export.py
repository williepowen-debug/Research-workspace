#!/usr/bin/env python3
"""spawn_list.py --open export contract v1 — tests derived from
ACCEPTANCE_spawn_list_open_export_2026-10-29.md (conditions 1–8, five neighbour categories).
Fixtures are verbatim DOCKET shapes where the shape matters; the live docket is used for the
partition and projection checks so the contract is tested against what the launcher will read."""
import datetime as dt, io, json, pathlib, subprocess, sys, unittest
from contextlib import redirect_stdout, redirect_stderr

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "PROME/tools")); sys.path.insert(0, str(ROOT / "scripts"))
import spawn_list  # noqa: E402

T = dt.date(2026, 10, 29)
H = "date\tcatalyst\towners\tstate\tartifacts_citing\tnotes\n"
def row(*c): return "\t".join(c) + "\n"


class Ordinary(unittest.TestCase):
    def test_plain_dated_row_exports_every_field_untruncated(self):
        long = "x" * 400
        text = H + row("2026-10-30", long, "LABOR/PROME", "PENDING — registered 10/22", "a", "n" * 300)
        r = spawn_list.open_records(text, T)
        self.assertEqual(len(r), 1); r = r[0]
        self.assertEqual(set(r), set(spawn_list.OPEN_FIELDS))
        self.assertEqual((r["key"], r["line"], r["due"], r["status"]), ("D:L2", 2, "2026-10-30", "future"))
        self.assertEqual((r["catalyst"], r["notes"], r["owner_cell"]), (long, "n" * 300, "LABOR/PROME"))
        self.assertEqual(r["owner_token"], "LABOR"); self.assertFalse(r["covered"]); self.assertFalse(r["approx"])

    def test_json_envelope_and_tsv_header(self):
        for fmt in ("json", "tsv"):
            buf = io.StringIO()
            with redirect_stdout(buf):
                rc = spawn_list.export_open("PROME/DOCKET.tsv", T, fmt)
            self.assertEqual(rc, 0)
            out = buf.getvalue()
            if fmt == "json":
                d = json.loads(out)
                self.assertEqual((d["schema"], d["version"], d["as_of"]), ("spawn_list.open", 1, "2026-10-29"))
                self.assertEqual(len(d["source_sha256"]), 64); self.assertIn("GATES", d["scope"])
                self.assertEqual(d["count"], len(d["rows"])); self.assertGreater(d["count"], 0)
            else:
                lines = out.rstrip("\n").split("\n")
                self.assertEqual(lines[0].split("\t"), list(spawn_list.OPEN_FIELDS))
                self.assertTrue(all(len(l.split("\t")) == len(spawn_list.OPEN_FIELDS) for l in lines[1:]))
                self.assertIn(lines[1].split("\t")[4], ("true", "false"))

    def test_cli_json_matches_library_and_tsv_flag_is_honoured(self):
        p = subprocess.run([sys.executable, "PROME/tools/spawn_list.py", "--open", "--json", "--as-of", "2026-10-29"],
                           cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        d = json.loads(p.stdout)
        self.assertEqual(d["count"], len(spawn_list.open_records((ROOT / "PROME/DOCKET.tsv").read_text(encoding="utf-8"), T)))
        p2 = subprocess.run([sys.executable, "PROME/tools/spawn_list.py", "--open", "--tsv", "--as-of", "2026-10-29"],
                            cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(p2.returncode, 0); self.assertTrue(p2.stdout.startswith("key\tline\t"))
        self.assertNotIn("DOCKET open rows", p2.stdout, "--open --tsv must not print the human table")


class OneInterpretation(unittest.TestCase):
    def test_list_open_is_a_projection_of_open_records_on_the_live_docket(self):
        text = (ROOT / "PROME/DOCKET.tsv").read_text(encoding="utf-8")
        a = spawn_list.list_open(text, T); b = spawn_list.open_records(text, T)
        self.assertEqual(len(a), len(b))
        for t, r in zip(a, b):
            self.assertEqual(t, (r["line"], r["date_cell"], r["owner_cell"], r["status"] in ("overdue", "today"), r["catalyst"]))

    def test_status_partitions_the_live_docket(self):
        rows = spawn_list.open_records((ROOT / "PROME/DOCKET.tsv").read_text(encoding="utf-8"), T)
        self.assertEqual(sum(1 for r in rows if r["status"] in ("overdue", "today", "future", "undated")), len(rows))
        for r in rows:
            if r["status"] == "undated": self.assertEqual(r["due"], "")
            if r["status"] == "overdue": self.assertLess(r["due"], "2026-10-29")
            if r["status"] == "today": self.assertEqual(r["due"], "2026-10-29")
            if r["status"] == "future": self.assertGreater(r["due"], "2026-10-29")


class Overlap(unittest.TestCase):
    def test_pending_row_with_a_covered_promise_is_listed_with_coverage_visible(self):
        st = "PENDING — COVERED:FLG spawn required in the ~11/14 window; NO gate registered at birth"
        r = spawn_list.open_records(H + row("2026-11-14", "FLG T-01", "FLG (grade) / PROME (spawn)", st, "", ""), T)
        self.assertEqual(len(r), 1); self.assertTrue(r[0]["covered"])
        self.assertTrue(r[0]["coverage"].startswith("FLG spawn required"))
        self.assertTrue(r[0]["spawn_suppressed"])

    def test_prome_slated_coverage_is_covered_but_not_spawn_suppressed(self):
        st = "PENDING — COVERED: PROME 9/11 boot slate — WATT L0 spawn (SLATED 9/11)"
        r = spawn_list.open_records(H + row("2026-09-11", "x", "WATT", st, "", ""), T)[0]
        self.assertTrue(r["covered"]); self.assertFalse(r["spawn_suppressed"])

    def test_range_is_due_on_its_end_and_approx_is_flagged(self):
        text = H + row("2026-08-14..2026-11-30", "ranged", "OWNER", "PENDING", "", "") + row("~2026-11-15", "approx", "SHADE", "PENDING", "", "")
        a, b = spawn_list.open_records(text, T)
        self.assertEqual((a["due"], a["status"], a["approx"]), ("2026-11-30", "future", False))
        self.assertEqual((b["due"], b["status"], b["approx"]), ("2026-11-15", "future", True))
        self.assertEqual(spawn_list.open_records(text, dt.date(2026, 11, 30))[0]["status"], "today")

    def test_terminal_row_carrying_PENDING_in_history_is_excluded(self):
        trap = "RESOLVED · PENDING — COVERED:HOMER (RAN 8/22 after 8d dark)"
        self.assertEqual(spawn_list.open_records(H + row("2026-08-17", "x", "HOMER", trap, "", ""), T), [])


class WrongOwner(unittest.TestCase):
    def test_will_and_prome_rows_are_present_and_flagged(self):
        text = H + row("2026-10-28", "a", "Will", "PENDING", "", "") + row("2026-10-29", "b", "PROME/DAEDALUS", "PENDING", "", "") + row("2026-10-30", "c", "HAWK (RU<->NATO/EU posture)/BRENT", "PENDING", "", "")
        w, p, h = spawn_list.open_records(text, T)
        self.assertTrue(w["will_owned"]); self.assertEqual(w["status"], "overdue")
        self.assertTrue(p["prome_owned"]); self.assertEqual(p["status"], "today")
        self.assertEqual(h["owner_names"], "HAWK/BRENT", "a slash inside a parenthetical is not an owner split")
        self.assertEqual(h["owner_token"], "HAWK")


class MissingInformation(unittest.TestCase):
    def test_undated_row_is_listed_as_undated_never_dropped(self):
        r = spawn_list.open_records(H + row("next-PROME-session", "x", "PROME", "PENDING", "", ""), T)
        self.assertEqual((len(r), r[0]["due"], r[0]["status"]), (1, "", "undated"))

    def test_short_row_pads_notes_instead_of_crashing(self):
        r = spawn_list.open_records("2026-10-30\tx\tOWNER\tPENDING\n", T)
        self.assertEqual((r[0]["notes"], r[0]["covered"]), ("", False))

    def test_unreadable_docket_is_rc2_with_an_error_object_never_an_empty_success(self):
        for fmt in ("json", "tsv", "human"):
            out, err = io.StringIO(), io.StringIO()
            with redirect_stdout(out), redirect_stderr(err):
                rc = spawn_list.export_open("PROME/DOES_NOT_EXIST.tsv", T, fmt)
            self.assertEqual(rc, 2)
            if fmt == "json":
                d = json.loads(out.getvalue()); self.assertIn("error", d); self.assertNotIn("rows", d)
            else:
                self.assertIn("UNKNOWN", err.getvalue()); self.assertEqual(out.getvalue(), "")

    def test_empty_docket_is_rc0_with_zero_rows(self):
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".tsv", delete=False, encoding="utf-8") as f:
            f.write(H); path = f.name
        out = io.StringIO()
        with redirect_stdout(out):
            rc = spawn_list.export_open(path, T, "json")
        d = json.loads(out.getvalue()); self.assertEqual((rc, d["count"], d["rows"]), (0, 0, []))


if __name__ == "__main__":
    unittest.main(verbosity=2)
