#!/usr/bin/env python3
"""
test_x_bookmarks_scan.py — acceptance matrix (A-rows) for x_bookmarks_scan.py.
Pure-logic + process-level isolation; live OAuth/API paths (L1-L4) are for the live
first-run. Updated 2026-10-03 after coldread read-1 (exclusion-set model; --mark stage;
all-or-nothing isolation). Run:  python3 this.py  (or -m unittest ...; both must pass).
"""
import importlib
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

# Isolate BOTH module paths before import (A8). The module derives the unset one
# beside the set one, so setting both to one tmp dir is the clean test setup.
_TMP = tempfile.mkdtemp(prefix="xbm_test_")
os.environ["WALTER_X_ENV"] = str(Path(_TMP) / ".env")
os.environ["WALTER_X_SEEN"] = str(Path(_TMP) / "seen.json")
sys.path.insert(0, str(Path(__file__).resolve().parent))
import x_bookmarks_scan as xbm  # noqa

TOOL = str(Path(__file__).resolve().parent / "x_bookmarks_scan.py")
PY = sys.executable


def bm(pid, author="a1", text="hello", created="2026-10-03T00:00:00Z"):
    return xbm.parse_bookmark({"id": pid, "author_id": author, "text": text, "created_at": created},
                              {"a1": "qtr"})


class PureLogic(unittest.TestCase):
    def tmp(self, name):
        return str(Path(tempfile.mkdtemp(prefix="xbm_")) / name)

    # A1 (new model): exclusion-set, API order preserved, NO floor -----------
    def test_select_new_is_set_membership_order_preserved(self):
        items = [bm("1200"), bm("1000"), bm("950")]   # API newest-bookmarked-first order
        out = xbm.select_new(items, seen_ids=["1000"])
        self.assertEqual([b["id"] for b in out], ["1200", "950"])   # 1000 seen; order kept

    def test_old_post_bookmarked_today_is_surfaced(self):
        # X1/CX7 regression: a low (old) post ID not in seen MUST surface
        out = xbm.select_new([bm("1500000000000000000")], seen_ids=["1974000000000000000"])
        self.assertEqual(len(out), 1)

    def test_seen_never_refires(self):
        self.assertEqual(xbm.select_new([bm("5000")], ["5000"]), [])

    def test_idless_item_always_surfaced(self):
        p = xbm.parse_bookmark({"id": None, "text": ""}, {})
        self.assertEqual(len(xbm.select_new([p], seen_ids=["anything"])), 1)

    # A4 / CX4b -------------------------------------------------------------
    def test_malformed_surfaced_with_warnings(self):
        p = xbm.parse_bookmark({"id": None, "text": ""}, {})
        self.assertIsNone(p["id"])
        self.assertTrue(any("MALFORMED" in w for w in p["warn"]))
        self.assertTrue(any("EMPTY TEXT" in w for w in p["warn"]))

    def test_non_string_text_never_raises(self):
        p = xbm.parse_bookmark({"id": "1", "author_id": "a1", "text": 12345}, {"a1": "u"})
        self.assertEqual(p["text"], "12345")    # coerced, not crashed (CX4b)
        for junk in [{}, {"id": 0}, {"text": "x"}, {"id": "9", "author_id": "z"}]:
            xbm.parse_bookmark(junk, {})         # must not raise

    # A5 / CX2 — every corruption shape refuses with the fix instruction ------
    def test_corrupt_seen_shapes_fail_closed(self):
        for content in ["{ not json", "[]", '"x"', '{"consumed": null}',
                        '{"consumed": "1200"}']:
            p = self.tmp("seen.json")
            Path(p).write_text(content, encoding="utf-8")
            with self.assertRaises(SystemExit) as cm:
                xbm.load_seen(p)
            self.assertIn("REFUSING", str(cm.exception.code))

    def test_non_utf8_seen_refuses(self):
        p = self.tmp("seen.json")
        Path(p).write_bytes(b"\xff\xfe\x00garbage")
        with self.assertRaises(SystemExit) as cm:
            xbm.load_seen(p)
        self.assertIn("REFUSING", str(cm.exception.code))

    def test_missing_seen_is_empty_not_error(self):
        d = xbm.load_seen(self.tmp("nope.json"))
        self.assertEqual(d["consumed"], [])

    # A6 / CX3 --------------------------------------------------------------
    def test_rewrite_env_preserves_collapses_crlf(self):
        p = self.tmp(".env")
        Path(p).write_bytes(b"# c\r\nX_CLIENT_ID=abc\r\nDUP=1\r\nDUP=2\r\n")
        xbm.rewrite_env({"X_BOOKMARK_ACCESS_TOKEN": "tok", "DUP": "NEW"}, p)
        raw = Path(p).read_bytes()
        env = xbm.load_env(p)
        self.assertIn(b"\r\n", raw)                     # CRLF preserved (CX3c)
        self.assertIn(b"# c", raw)
        self.assertEqual(env["X_CLIENT_ID"], "abc")
        self.assertEqual(env["X_BOOKMARK_ACCESS_TOKEN"], "tok")
        self.assertEqual(env["DUP"], "NEW")             # duplicate collapsed (CX3b)
        self.assertEqual(raw.decode().count("DUP="), 1)

    def test_load_env_strips_quotes(self):
        p = self.tmp(".env")
        Path(p).write_text('X_CLIENT_ID="abc"\n')
        self.assertEqual(xbm.load_env(p)["X_CLIENT_ID"], "abc")   # CX3d

    # A7 --------------------------------------------------------------------
    def test_save_seen_ids_only_rejects_stray_key(self):
        p = self.tmp("seen.json")
        xbm.save_seen({"consumed": ["111", "222"], "pilot_start_id": "2026-10-03T00:00:00Z"}, p)
        raw = Path(p).read_text()
        self.assertNotIn("hello", raw)
        self.assertIn("111", raw)
        with self.assertRaises(ValueError):             # explicit, survives python -O (not an assert)
            xbm.save_seen({"consumed": [], "pilot_start_id": None, "text": "leak"}, p)

    # A9 --------------------------------------------------------------------
    def test_boot_line_shape(self):
        self.assertEqual(xbm.format_boot_line(3, 2), "3 new bookmarks since last launch, 2 dispatched")
        self.assertEqual(xbm.format_boot_line(1, 0), "1 new bookmark since last launch, 0 dispatched")

    # A10 / CX5b ------------------------------------------------------------
    def test_not_authorized_exits_zero(self):
        Path(os.environ["WALTER_X_ENV"]).write_text("# empty\n", encoding="utf-8")
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = xbm.main([])
        self.assertEqual(rc, 0)
        self.assertIn("Not authorized", buf.getvalue())

    def test_half_authorized_exits_zero(self):
        Path(os.environ["WALTER_X_ENV"]).write_text("X_BOOKMARK_ACCESS_TOKEN=t\n", encoding="utf-8")
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = xbm.main([])
        self.assertEqual(rc, 0)
        self.assertIn("Partially authorized", buf.getvalue())


class Isolation(unittest.TestCase):
    # A8 — setting only ONE test var must STILL isolate the other (never live) ----
    def test_partial_env_still_isolates_seen(self):
        tmp = tempfile.mkdtemp(prefix="xbm_iso_")
        env = {k: v for k, v in os.environ.items() if k not in ("WALTER_X_ENV", "WALTER_X_SEEN")}
        env["WALTER_X_ENV"] = str(Path(tmp) / ".env")
        code = (f"import importlib.util as u;s=u.spec_from_file_location('m',{TOOL!r});"
                "m=u.module_from_spec(s);s.loader.exec_module(m);print(m.SEEN)")
        out = subprocess.run([PY, "-c", code], env=env, capture_output=True, text=True).stdout.strip()
        self.assertNotIn("registry/x_bookmarks_seen.json", out)   # live file NOT in use
        self.assertTrue(out.startswith(tmp))                      # isolated beside the set var

    def test_partial_seen_still_isolates_env(self):
        tmp = tempfile.mkdtemp(prefix="xbm_iso_")
        env = {k: v for k, v in os.environ.items() if k not in ("WALTER_X_ENV", "WALTER_X_SEEN")}
        env["WALTER_X_SEEN"] = str(Path(tmp) / "seen.json")
        code = (f"import importlib.util as u;s=u.spec_from_file_location('m',{TOOL!r});"
                "m=u.module_from_spec(s);s.loader.exec_module(m);print(m.ENV_PATH)")
        out = subprocess.run([PY, "-c", code], env=env, capture_output=True, text=True).stdout.strip()
        self.assertNotIn("AGENTS/WALTER/.env", out)
        self.assertTrue(out.startswith(tmp))


class MarkFlow(unittest.TestCase):
    # X2/CX8 — stage on report, consume exactly the stage on --mark, IDs only -----
    def test_mark_consumes_only_staged_ids_no_body(self):
        d = Path(tempfile.mkdtemp(prefix="xbm_mark_"))
        orig_env, orig_seen = xbm.ENV_PATH, xbm.SEEN   # restore after, or later tests read this .env
        xbm.ENV_PATH = d / ".env"
        xbm.SEEN = d / "seen.json"
        (d / ".env").write_text("X_BOOKMARK_ACCESS_TOKEN=t\nX_USER_ID=1\n")
        xbm.save_seen({"consumed": [], "pilot_start_id": None}, d / "seen.json")
        orig_fetch = xbm.fetch_new_bookmarks
        # report run sees one item; a second bookmark appears only if a re-fetch happens
        state = {"n": 0}

        def fake_fetch(env, seen):
            state["n"] += 1
            items = [bm("500", text="SECRET ALPHA")]
            if state["n"] > 1:
                items.append(bm("600", text="SECRET BRAVO"))
            return xbm.select_new(items, seen["consumed"])
        xbm.fetch_new_bookmarks = fake_fetch
        try:
            with redirect_stdout(io.StringIO()):
                xbm.main([])            # stages ["500"]
                xbm.main(["--mark"])    # consumes the stage; MUST NOT re-fetch
        finally:
            xbm.fetch_new_bookmarks = orig_fetch
            xbm.ENV_PATH, xbm.SEEN = orig_env, orig_seen
        raw = (d / "seen.json").read_text()
        consumed = json.loads(raw)["consumed"]
        self.assertEqual(consumed, ["500"])          # only staged, 600 never consumed (CX8b)
        self.assertNotIn("SECRET", raw)              # IDs only, no body (CX8a)


if __name__ == "__main__":
    unittest.main(verbosity=2)
