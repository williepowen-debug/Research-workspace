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
    # 2026-11-06 reset coverage (ACCEPTANCE_git_guard_reset_2026-11-06.md)
    f"{G} reset",
    f"{G} reset -q",
    f"{G} reset --quiet",
    f"{G} reset --mixed",
    f"{G} reset; {G} status",
    f"{G} reset -q && {G} status",
    f"{G} -C /tmp reset -q",
    f'bash -c "{G} reset -q"',
    f"{G} reset --hard",
    f"{G} reset --hard origin/master",
    f"{G} reset -q --hard",
    f"{G} reset --hard; {G} status",
    f"{G} reset -q HEAD",
    f"{G} reset --mixed HEAD~1",
    f"{G} reset\n{G} status",
    # read 1 counterexamples (reports/2026-11-06_git-guard-reset-read-1.md)
    f"{G} reset -q 2>/dev/null; {G} status",
    f"{G} reset >/dev/null",
    f"{G} reset 2>&1 | tail -1",
    f"{G} reset # note",
    f"x=`{G} reset`",
    f"{G} reset --",
    f"{G} reset -q --",
    f"{G} reset -- ; {G} status",
    f"{G} ls-files | xargs {G} reset --",
    f"{G} reset .",
    f"{G} reset -- .",
    f"{G} reset :/",
    f"{G} reset '*'",
    f"{G} reset @",
    f"{G} reset @{{u}}",
    f"{G} reset origin/master",
    f"{G} reset --mixed origin/master",
    f"{G} reset --soft @",
    f"{G} reset \\\n --hard origin/master",
    f"{G} reset \\\n -q",
    # read 2 counterexamples (reports/2026-11-06_git-guard-reset-read-2.md)
    f'grep -E "foo\\|bar" f; {G} add -A; echo "all done"',
    f'grep -E "foo\\|bar" f; {G} commit --amend; echo "all done"',
    f"echo '#'; {G} reset --hard origin/master",
    f'grep "#" f; {G} reset --hard',
    f'{G} reset "$({G} rev-parse HEAD)"',
    f"{G} reset $({G} rev-parse HEAD)",
    f"{G} reset master --",
    f"{G} reset -q v1.0 --",
    f"{G} reset ../..",
    f"{G} reset '**'",
    f"{G} reset ':(glob)**'",
    f"{G} reset ./.",
    f"{G} reset .//",
    f"{G} reset -- ':!x.md'",
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
    f"{G} reset -- A.md",                    # path-scoped unstage touches only that path
    f"{G} reset -q -- A.md",
    f"{G} reset A.md",
    f"{G} log reset-notes",
    f"{G} show reset.md",
    f"{G} reflog",
    f"{G} reset HEADER.md",
    f"{G} reset ./A.md",
    f"{G} reset -- AGENTS/X/f.md AGENTS/X/g.md",
    f'{G} commit -m "never {G} reset -q on the shared index"',
    f"cat > m.txt <<'EOF'\nnever {G} reset -q\nEOF\n{G} commit -F m.txt -- A.md",
]


# 2026-11-20 heredoc expansion warning (ACCEPTANCE_git_guard_heredoc_warn_2026-11-20.md).
# D and B are fragments so no fixture is itself a live expansion in this file's text.
D, B = "$", "`"
WARN = [
    f"cat > f <<EOF\nrevenue {D}1.8B\nEOF",
    f"cat > f <<-EOF\n\tcost {D}0\n\tEOF",
    f"cat > f << EOF\nat {D}(date)\nEOF",
    f"cat > f <<EOF\nrun {B}date{B}\nEOF",
    f"cat > f <<EOF\nrevenue \\\\{D}1.8B\nEOF",           # even backslash run: still live
    f"cat > a <<'A'\n{D}1\nA\ncat > b <<B\n{D}2\nB",        # quoted beside unquoted
    f"cat > m.txt <<EOF\nnet {D}665.32\nEOF\n{G} commit -F m.txt -- A.md",
    f"cat > f <<EOF\n{D}{{HOME}} and {D}NOW\nEOF",            # intended expansion also warns (declared)
]
QUIET = [
    f"cat > f <<'EOF'\nrevenue {D}1.8B\nEOF",
    f'cat > f <<"EOF"\nrevenue {D}1.8B\nEOF',
    f"cat > f <<\\EOF\nrevenue {D}1.8B\nEOF",
    f"cat > f <<EOF\nrevenue \\{D}1.8B and \\{B}x\\{B}\nEOF",
    f"cat > f <<EOF\nprice in {D} terms, {D}. and {D}, and {D}\nEOF",
    f'cat <<< "{D}x"',
    f"grep '<<EOF' f\necho {D}HOME",                           # no terminator: not a heredoc
    "cat > f <<EOF\nplain text\nEOF",
    f"echo {D}HOME",
]
BLOCK_WINS = [
    f"cat > f <<EOF\nrevenue {D}1.8B\nEOF\n{G} add -A",
]


def run_full(cmd):
    r = subprocess.run([sys.executable, str(HERE / "git_guard.py")],
                       input=json.dumps({"tool_name": "Bash", "tool_input": {"command": cmd}}),
                       capture_output=True, text=True)
    return r.returncode, r.stdout


def run(cmd):
    return run_full(cmd)[0]


def warned(out):
    try:
        h = json.loads(out)["hookSpecificOutput"]
        return h["hookEventName"] == "PreToolUse" and "WARNING" in h["additionalContext"]
    except Exception:
        return False


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
for c in BLOCK + ALLOW:                       # no existing fixture gains a warning
    if run_full(c)[1].strip():
        fails += 1
        print("UNEXPECTED STDOUT:", c.replace("\n", "⏎"))
for c in WARN:
    rc, out = run_full(c)
    if rc != 0 or not warned(out):
        fails += 1
        print("NOT WARNED:", rc, c.replace("\n", "⏎"))
for c in QUIET:
    rc, out = run_full(c)
    if rc != 0 or out.strip():
        fails += 1
        print("FALSE WARNING:", rc, c.replace("\n", "⏎"))
for c in BLOCK_WINS:
    rc, out = run_full(c)
    if rc != 2 or out.strip():
        fails += 1
        print("BLOCK DID NOT WIN:", rc, c.replace("\n", "⏎"))
TOTAL = 2 * (len(BLOCK) + len(ALLOW)) + len(WARN) + len(QUIET) + len(BLOCK_WINS)
print(f"git_guard self-test: {TOTAL-fails}/{TOTAL} pass")
sys.exit(1 if fails else 0)
