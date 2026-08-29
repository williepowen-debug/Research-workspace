#!/usr/bin/env python3
"""Self-test for git_guard.py — run: python3 PROME/tools/hooks/test_git_guard.py
Cases are built from fragments so this file's own text never trips the live hook."""
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).parent
G = "git"
BLOCK = [
    f"{G} add -A",
    f"{G} add . && {G} commit -m x",
    f"{G} reset HEAD",
    f"{G} commit --amend -m x",
    f"{G} push --force origin master",
    f'{G} commit -am "x"',
    f"cd x && {G} add --all",
    # RAV bypass set (8/29 PM) — each passed the original 14/14 self-test; now fixtures
    f'{G} add "."',
    f"{G} -C /tmp add .",
    f'bash -c "{G} add ."',
    f'{G} commit "--amend" -m x',
    f"{G} add ./",
    f"{G} -c core.editor=true commit --amend",
]
ALLOW = [
    f"{G} add A.md B.md",
    f"{G} commit A.md -m x",
    f"{G} push origin master",
    f"{G} status --short",
    f'{G} commit -m "never {G} add -A or {G} reset HEAD"',
    f"cat > m.txt <<'EOF'\nnever {G} add -A/. · commit --amend\nEOF\n{G} commit -F m.txt -- A.md",
    f"python3 - <<'PY'\nold = '{G} add -A'\nPY",
    f'echo "{G} add . is forbidden here"',   # prose with whitespace stays prose
    f"{G} add ./A.md ./B.md",                # dot-prefixed PATHS are not add-dot
]


def run(cmd):
    r = subprocess.run([sys.executable, str(HERE / "git_guard.py")],
                       input=json.dumps({"tool_name": "Bash", "tool_input": {"command": cmd}}),
                       capture_output=True, text=True)
    return r.returncode


fails = 0
for c in BLOCK:
    rc = run(c)
    if rc != 2:
        fails += 1
        print("NOT BLOCKED:", c.replace("\n", "⏎"))
for c in ALLOW:
    rc = run(c)
    if rc != 0:
        fails += 1
        print("FALSE POSITIVE:", c.replace("\n", "⏎"))
print(f"git_guard self-test: {len(BLOCK)+len(ALLOW)-fails}/{len(BLOCK)+len(ALLOW)} pass")
sys.exit(1 if fails else 0)
