#!/usr/bin/env python3
"""PreToolUse(Bash) hook — refuses the root-canon forbidden git commands BEFORE they run.
Will-approved 2026-08-29 ("approved go ahead"); PROME-scoped first, fleet-wide after a week.

Canon (root CLAUDE.md § Git Protocol, prose until now): never add-all / add-dot, never
reset HEAD, never commit --amend, never force-push; plus commit -a (sweeps the whole
index — Gate C custody rule). `git stash drop` is left to judgment (canon permits it when
own files are committed).

Protocol: stdin = JSON {tool_name, tool_input:{command}}; exit 2 + stderr = BLOCK (the
message reaches the model); exit 0 = allow. Any parse failure ⇒ allow (a guard that fails
closed on its own bug would halt every shell command).

Text is not a command: heredoc bodies and quoted strings are stripped before matching.
The guard's own commissioning commit (8/29) was its first false positive — the commit
message quoted the prohibition. A dangerous flag never sits inside quotes in a real command.
"""
import json
import re
import sys

RULES = [
    (r"\bgit\s+add\s+(?:.*\s)?(?:-A\b|--all\b)",
     "add-all sweeps every agent's work — pathspec adds only"),
    (r"\bgit\s+add\s+(?:.*\s)?\.(?:\s|$|;|&|\|)",
     "add-dot sweeps the shared index — pathspec adds only"),
    (r"\bgit\s+reset\s+HEAD\b",
     "reset HEAD is a global unstage on the shared index"),
    (r"\bgit\s+reset\s+(?:--hard|--mixed|--soft)?\s*$",
     "bare reset unstages everyone's work"),
    (r"\bgit\s+commit\b[^\n|;&]*\s--amend\b",
     "commit --amend rewrites whoever holds HEAD — note the fix in the next commit instead (root rule 4b)"),
    (r"\bgit\s+push\b[^\n|;&]*\s(?:-f\b|--force\b|--force-with-lease\b)",
     "force push is never permitted — scripts/safe-push.sh only"),
    (r"\bgit\s+commit\s+(?:.*\s)?-a(?:m)?\b",
     "commit -a commits the whole tree — pathspec commits only"),
]


def strip_text(cmd: str) -> str:
    """Drop heredoc bodies and quoted strings so prose cannot trip a command rule."""
    out, i, lines = [], 0, cmd.split("\n")
    while i < len(lines):
        ln = lines[i]
        m = re.search(r"<<-?\s*['\"]?(\w+)['\"]?", ln)
        out.append(ln)
        if m:
            term = m.group(1)
            i += 1
            while i < len(lines) and lines[i].strip() != term:
                i += 1
        i += 1
    s = "\n".join(out)
    s = re.sub(r"'[^']*'", "''", s)
    s = re.sub(r'"[^"]*"', '""', s)
    return s


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0
    if data.get("tool_name") != "Bash":
        return 0
    cmd = (data.get("tool_input") or {}).get("command", "") or ""
    scan = strip_text(cmd)
    for rx, why in RULES:
        if re.search(rx, scan):
            sys.stderr.write(
                f"⛔ git_guard BLOCKED: {why}\n   command: {cmd[:200]}\n"
                "   (root CLAUDE.md § Git Protocol — this hook mechanizes the prohibition)\n")
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
