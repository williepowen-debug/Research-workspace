#!/usr/bin/env python3
"""Run: python3 PROME/tools/tests/test_staged_stamp_check.py  (temp files only; reads no index)."""
import pathlib
import subprocess
import sys
import tempfile

TOOL = pathlib.Path(__file__).resolve().parents[1] / "staged_stamp_check.py"
NOW = "2026-11-20T18:20:00Z"          # 13:20 EST


def run(body_lines, now=NOW, raw=None):
    diff = raw if raw is not None else (
        "diff --git a/PROME/X.md b/PROME/X.md\n--- a/PROME/X.md\n+++ b/PROME/X.md\n@@ -1,0 +2 @@\n"
        + "\n".join(body_lines) + "\n").encode()
    with tempfile.NamedTemporaryFile(delete=False) as fh:
        fh.write(diff)
    r = subprocess.run([sys.executable, "-I", str(TOOL), "--now", now, "--diff-file", fh.name],
                       capture_output=True, text=True)
    return r.returncode, r.stdout


CASES = [
    ("ET stamp 25 min ahead: flagged", ["+done 2026-11-20 13:45 ET"], True),
    ("EST stamp 25 min ahead: flagged", ["+done 2026-11-20 13:45 EST"], True),
    ("Z stamp 25 min ahead: flagged", ["+at 2026-11-20T18:45Z"], True),
    ("Z stamp with seconds ahead: flagged", ["+ts 2026-11-20T18:45:10Z"], True),
    ("3 min ahead: flagged", ["+done 2026-11-20 13:23 ET"], True),
    ("23 h ahead: flagged (declared: a same-day plan too)", ["+launch 2026-11-21 12:20 ET"], True),
    ("stamp now: quiet", ["+done 2026-11-20 13:20 ET"], False),
    ("2 min ahead: quiet", ["+done 2026-11-20 13:22 ET"], False),
    ("past stamp: quiet", ["+done 2026-11-20 11:16 ET"], False),
    ("25 h ahead: quiet", ["+wake 2026-11-21 14:30 ET"], False),
    ("time with no ISO date: quiet", ["+BRENT 14:28 to 14:30 ET", "+Fri 11/20 16:05 ET", "+13:1x ET"], False),
    ("no zone: quiet", ["+done 2026-11-20 13:45"], False),
    ("removed line: quiet", ["-done 2026-11-20 13:45 ET"], False),
    ("context line: quiet", [" done 2026-11-20 13:45 ET"], False),
    ("impossible date: quiet", ["+done 2026-13-45 13:45 ET", "+x 2026-11-20 25:99 ET"], False),
    ("EDT taken at its word (13:45 EDT is 17:45Z, past): quiet", ["+done 2026-11-20 13:45 EDT"], False),
    ("digit run before the date: quiet", ["+id 12026-11-20 13:45 ET"], False),
]
fails = 0
for name, lines, want in CASES:
    rc, out = run(lines)
    got = "AHEAD" in out
    if rc != 0 or got != want:
        fails += 1
        print("FAIL:", name, "| rc", rc, "|", out.strip()[:120])
rc, out = run([], raw=b"\xff\xfe\x00 binary \x80\n+\xff 2026-11-20 13:45 ET\n")
if rc != 0:
    fails += 1; print("FAIL: undecodable bytes changed the exit code")
rc, out = run([], raw=b"")
if rc != 0 or out.strip():
    fails += 1; print("FAIL: empty diff")
rc, out = run(["+x"], now="garbage")
if rc != 0:
    fails += 1; print("FAIL: a helper failure changed the exit code")
rc, out = run(["+a 2026-11-20 13:45 ET"] * 14)
if rc != 0 or "and 4 more" not in out:
    fails += 1; print("FAIL: print cap")
rc, out = run(["+done 2026-11-20 13:45 ET"])
if "PROME/X.md" not in out or "25 min" not in out:
    fails += 1; print("FAIL: file and minutes not named:", out)
# reader's failure 2026-11-20: an added line whose own text starts with `++` shows as `+++ ...` inside a hunk
rc, out = run(["+++ 2026-11-20 13:55 ET"])
if rc != 0 or "AHEAD" not in out or "PROME/X.md" not in out:
    fails += 1; print("FAIL: content line starting with ++ was read as a header:", out)
rc, out = run(["+++ foo", "+later 2026-11-20 13:45 ET"])
if rc != 0 or "PROME/X.md: 2026-11-20 13:45 ET" not in out:
    fails += 1; print("FAIL: a ++ content line renamed the file:", out)
two = (b"diff --git a/A.md b/A.md\n--- a/A.md\n+++ b/A.md\n@@ -1,0 +2 @@\n+ok 2026-11-20 11:00 ET\n"
       b"diff --git a/B.md b/B.md\n--- a/B.md\n+++ b/B.md\n@@ -1,0 +2 @@\n+done 2026-11-20 13:45 ET\n")
rc, out = run([], raw=two)
if rc != 0 or "B.md: 2026-11-20 13:45 ET" not in out or "A.md" in out:
    fails += 1; print("FAIL: second file's header not read:", out)
total = len(CASES) + 8
print(f"staged_stamp_check: {total - fails}/{total} pass")
sys.exit(1 if fails else 0)
