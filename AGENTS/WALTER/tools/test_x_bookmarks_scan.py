#!/usr/bin/env python3
"""
test_x_bookmarks_scan.py — acceptance matrix (A-rows) for x_bookmarks_scan.py.
Pure-logic only; the live OAuth/API paths (L1–L4) are exercised by the first
live run on Will's token, not here. Run:  python3 -m pytest -q  OR  python3 this.py
"""
import importlib
import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

# Isolate module-level paths BEFORE import (A8: seen-file AND env both isolated).
_TMP = tempfile.mkdtemp(prefix="xbm_test_")
os.environ["WALTER_X_ENV"] = str(Path(_TMP) / ".env")
os.environ["WALTER_X_SEEN"] = str(Path(_TMP) / "seen.json")
xbm = importlib.import_module("x_bookmarks_scan") if "x_bookmarks_scan" in sys.modules else None
if xbm is None:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import x_bookmarks_scan as xbm  # noqa


def bm(pid, author="a1", text="hello", created="2026-10-03T00:00:00Z"):
    return {"id": pid, "author_id": author, "text": text, "created_at": created}


class PureLogic(unittest.TestCase):
    def tmp(self, name):
        return str(Path(tempfile.mkdtemp(prefix="xbm_")) / name)

    # A1 / A2 / A3 -----------------------------------------------------------
    def test_select_new_floor_and_integer_compare(self):
        users = {"a1": "qtr"}
        items = [xbm.parse_bookmark(bm("1000"), users),   # newer than floor 900
                 xbm.parse_bookmark(bm("900"), users),    # == floor → excluded
                 xbm.parse_bookmark(bm("950"), users),    # newer
                 xbm.parse_bookmark(bm("1200"), users)]   # newest, but already seen
        out = xbm.select_new(items, seen_ids=["1200"], pilot_start_id="900")
        ids = [b["id"] for b in out]
        self.assertEqual(ids, ["1000", "950"])            # 900 excluded, 1200 seen, newest-first

    def test_integer_not_string_compare(self):
        # as strings "1000" < "900"; integer compare must put 1000 above the 900 floor
        users = {"a1": "x"}
        items = [xbm.parse_bookmark(bm("1000"), users)]
        self.assertEqual([b["id"] for b in xbm.select_new(items, [], "900")], ["1000"])

    def test_seen_never_refires_even_if_newest(self):
        users = {"a1": "x"}
        items = [xbm.parse_bookmark(bm("5000"), users)]
        self.assertEqual(xbm.select_new(items, ["5000"], "100"), [])

    # A4 --------------------------------------------------------------------
    def test_malformed_surfaced_not_dropped(self):
        p = xbm.parse_bookmark({"id": None, "text": ""}, {})
        self.assertIsNone(p["id"])
        self.assertTrue(any("MALFORMED" in w for w in p["warn"]))
        self.assertTrue(any("EMPTY TEXT" in w for w in p["warn"]))
        # a malformed (idless) item is still handed over by select_new
        out = xbm.select_new([p], seen_ids=[], pilot_start_id="1")
        self.assertEqual(len(out), 1)

    def test_parse_never_raises(self):
        for junk in [{}, {"id": 123}, {"text": "x"}, {"id": "9", "author_id": "z"}]:
            xbm.parse_bookmark(junk, {})  # must not raise

    # A5 --------------------------------------------------------------------
    def test_corrupt_seen_fails_closed(self):
        p = self.tmp("seen.json")
        Path(p).write_text("{ not json", encoding="utf-8")
        with self.assertRaises(SystemExit):
            xbm.load_seen(p)

    def test_missing_seen_is_empty_not_error(self):
        d = xbm.load_seen(self.tmp("nope.json"))
        self.assertEqual(d["consumed"], [])
        self.assertIsNone(d["pilot_start_id"])

    # A6 --------------------------------------------------------------------
    def test_rewrite_env_preserves_others(self):
        p = self.tmp(".env")
        Path(p).write_text("# comment\nX_CLIENT_ID=abc\nOTHER=keepme\n", encoding="utf-8")
        xbm.rewrite_env({"X_BOOKMARK_ACCESS_TOKEN": "tok1", "X_CLIENT_ID": "abc"}, p)
        env = xbm.load_env(p)
        self.assertEqual(env["OTHER"], "keepme")
        self.assertEqual(env["X_CLIENT_ID"], "abc")
        self.assertEqual(env["X_BOOKMARK_ACCESS_TOKEN"], "tok1")
        self.assertIn("# comment", Path(p).read_text())

    # A7 --------------------------------------------------------------------
    def test_seen_stores_ids_only_no_body(self):
        p = self.tmp("seen.json")
        xbm.save_seen({"consumed": ["111", "222"], "pilot_start_id": "100"}, p)
        raw = Path(p).read_text()
        self.assertNotIn("hello", raw)           # no post text
        self.assertIn("111", raw)
        with self.assertRaises(AssertionError):  # a stray text key is refused
            xbm.save_seen({"consumed": [], "pilot_start_id": None, "text": "leak"}, p)

    # A9 --------------------------------------------------------------------
    def test_boot_line_shape(self):
        self.assertEqual(xbm.format_boot_line(3, 2), "3 new bookmarks since last launch, 2 dispatched")
        self.assertEqual(xbm.format_boot_line(1, 0), "1 new bookmark since last launch, 0 dispatched")

    # A10 -------------------------------------------------------------------
    def test_not_authorized_exits_zero(self):
        # empty .env (the isolated WALTER_X_ENV from module import) → clean status, rc 0
        Path(os.environ["WALTER_X_ENV"]).write_text("# empty\n", encoding="utf-8")
        buf = io.StringIO()
        # Pass argv explicitly so the test runner's own flags (python -m unittest
        # <path>, pytest -v) never leak into the tool's parser. main() now takes
        # argv=None (PROME-found 2026-10-03; A10 must hold regardless of launcher).
        with redirect_stdout(buf):
            rc = xbm.main([])
        self.assertEqual(rc, 0)
        self.assertIn("Not authorized", buf.getvalue())


if __name__ == "__main__":
    unittest.main(verbosity=2)
