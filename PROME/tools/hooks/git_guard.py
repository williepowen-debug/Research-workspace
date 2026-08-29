#!/usr/bin/env python3
"""PreToolUse(Bash) hook — refuses the root-canon forbidden git commands BEFORE they run.
Will-approved 2026-08-29 ("approved go ahead"); PROME-scoped first, fleet-wide after a week.

Canon (root CLAUDE.md § Git Protocol, prose until now): never add-all / add-dot, never
reset HEAD, never commit --amend, never force-push; plus commit -a (sweeps the whole
index — Gate C custody rule). `git stash drop` is left to judgment (canon permits it when
own files are committed).

⚠️ WHAT THIS IS: a BEST-EFFORT LINT LAYER, not a security boundary. The 8/29 commissioning
commit (e67992c34) said "prohibitions become impossibilities" — that claim is RETRACTED
(RAV review 8/29 PM, verified: five bypasses passed the 14/14 self-test). The guard matches
a regex over the literal command text after stripping prose; anything that builds the
command at runtime is invisible to it by construction:
  - a git call inside a script invoked by path (`bash do_it.sh`, `python3 x.py` → subprocess)
  - commands assembled from variables or eval (`CMD="add ."; git $CMD`)
  - a git alias, a wrapper binary, or a different working tree via `--git-dir`/`--work-tree`
    (the -C form IS covered since 8/29 PM)
The root CLAUDE.md prohibition is the rule; this hook catches the direct forms of breaking it.

Protocol: stdin = JSON {tool_name, tool_input:{command}}; exit 2 + stderr = BLOCK (the
message reaches the model); exit 0 = allow. A parse failure ⇒ ALLOW, but VISIBLY: it prints
an advisory to stderr so a silently fail-open guard cannot be mistaken for coverage
(a guard that fails closed on its own bug would halt every shell command).

Text vs command (8/29 PM re-cut after the RAV bypass set): heredoc bodies are dropped.
A quoted string is PROSE only if it contains whitespace ("...", a commit message);
a quoted token with no whitespace (`"."`, `"--amend"`) is an ARGUMENT and is unquoted.
The body after `bash -c` / `sh -c` / `zsh -c` is a COMMAND and is unquoted and scanned.
"""
import json
import re
import sys

# `git` followed by any of its global options (-C <dir>, -c k=v, --git-dir=…, --work-tree=…,
# --no-pager …) before the subcommand — `git -C /tmp add .` is still add-dot.
GIT = r"\bgit(?:\s+(?:-C\s+\S+|-c\s+\S+|--git-dir=\S+|--work-tree=\S+|--no-pager|-p|-P|--no-optional-locks))*\s+"

RULES = [
    (GIT + r"add\s+(?:.*\s)?(?:-A\b|--all\b)",
     "add-all sweeps every agent's work — pathspec adds only"),
    (GIT + r"add\s+(?:.*\s)?\.(?:/)?(?:\s|$|;|&|\|)",
     "add-dot sweeps the shared index — pathspec adds only"),
    (GIT + r"reset\s+HEAD\b",
     "reset HEAD is a global unstage on the shared index"),
    (GIT + r"reset\s+(?:--hard|--mixed|--soft)?\s*$",
     "bare reset unstages everyone's work"),
    (GIT + r"commit\b[^\n|;&]*\s--amend\b",
     "commit --amend rewrites whoever holds HEAD — note the fix in the next commit instead (root rule 4b)"),
    (GIT + r"push\b[^\n|;&]*\s(?:-f\b|--force\b|--force-with-lease\b)",
     "force push is never permitted — scripts/safe-push.sh only"),
    (GIT + r"commit\s+(?:.*\s)?-a(?:m)?\b",
     "commit -a commits the whole tree — pathspec commits only"),
]

_SHELL_C = re.compile(r"\b(?:bash|sh|zsh|dash)\s+(?:-[a-zA-Z]*c[a-zA-Z]*\s+)(['\"])(.*?)\1", re.S)
_QUOTED = re.compile(r"'([^']*)'|\"([^\"]*)\"")


def _drop_heredocs(cmd: str) -> str:
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
    return "\n".join(out)


def _unquote_or_drop(m: re.Match) -> str:
    body = m.group(1) if m.group(1) is not None else m.group(2)
    return body if not re.search(r"\s", body) else " "


def strip_text(cmd: str) -> str:
    """Prose out, arguments in: heredocs dropped; `-c "…"` bodies scanned as commands;
    whitespace-bearing quoted strings dropped; whitespace-free quoted tokens unquoted."""
    s = _drop_heredocs(cmd)
    # the body of `bash -c "…"` is a command: lift it out of its quotes so the rules see it
    s = _SHELL_C.sub(lambda m: " " + m.group(2) + " ", s)
    s = _QUOTED.sub(_unquote_or_drop, s)
    return s


def main():
    try:
        data = json.load(sys.stdin)
    except Exception as e:
        sys.stderr.write(f"⚠️ git_guard: could not parse hook input ({type(e).__name__}) — "
                         "ALLOWING without a check. This is fail-open, not coverage.\n")
        return 0
    if data.get("tool_name") != "Bash":
        return 0
    cmd = (data.get("tool_input") or {}).get("command", "") or ""
    try:
        scan = strip_text(cmd)
    except Exception as e:
        sys.stderr.write(f"⚠️ git_guard: text-stripper failed ({type(e).__name__}) — "
                         "ALLOWING without a check. This is fail-open, not coverage.\n")
        return 0
    for rx, why in RULES:
        if re.search(rx, scan):
            sys.stderr.write(
                f"⛔ git_guard BLOCKED: {why}\n   command: {cmd[:200]}\n"
                "   (root CLAUDE.md § Git Protocol — this hook lints the direct forms of the prohibition)\n")
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
