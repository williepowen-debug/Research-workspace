#!/usr/bin/env python3
"""PreToolUse(Bash) hook — the BLOCKING wrapper over `scripts/pipeline_rc_guard.py`'s recogniser.

`scripts/pipeline_rc_guard.py` is DAEDALUS's file (delivered 2026-09-12 UNWIRED BY DESIGN: "PROME or Will
wires it"). It exits 0 always (warn-only). WQ-244 (Will 2026-09-17 22:33:18Z Decision Deck APPROVE) rules
that it BLOCKS on a clean detection and fails OPEN on its own error. This wrapper does exactly that WITHOUT
editing the recogniser: it imports `diagnose()` from the DAEDALUS file, exits 2 + the guard's own fix text
on a hit, and exits 0 with a visible advisory on any error — a missing or broken recogniser included.
Both recognisers (pipe-into-a-pager then `$?`; three-state rc collapsed by `||`/`if !`/`[ $? -ne 0 ]`)
block.

v2 (2026-09-18, after the independent cold read `wq244cold` ❌3): the recogniser's 0.00% false-positive
figure was measured over COMMITTED lines, not TYPED commands, and a wrapper that blocks makes a false
positive fatal. Its counterexample — `echo "do not write: python3 scripts/read_cap_check.py … | tail -1;
echo $?"` — is one quoted `echo` argument, not a pipeline, and was BLOCKED. Now: a hit is confirmed only
if it SURVIVES blanking every quoted string that contains a `|` (a pipe inside quotes is text, never a
pipeline); the real defect's pipe is always unquoted, and its `echo "RC=$?"` carries no pipe, so the
true positives are untouched (drilled below). ⚠️ Two neighbours the recogniser does not see stay unseen —
`if <gate> | tail -1; then …` and `<gate> && echo ok || echo FAILED` (reader ⚠️9) — that is DAEDALUS's
file's perimeter, declared here, not widened by this wrapper.

ACCEPTANCE CONDITIONS (WQ-229): B1 a command `diagnose()` flags AND that still flags with quoted pipes
blanked exits 2 with the fix text · B2 a command it does not flag exits 0 silently · B3 malformed hook
input (non-JSON, non-object, non-object tool_input) exits 0 with an advisory · B4 the recogniser failing
to import exits 0 with an advisory (fail-open on the wrapper's own error) · B5 the DAEDALUS file is
byte-unchanged by this wiring (`git status` shows no diff) · B6 a fully-quoted mention of the anti-pattern
(echo/printf/grep argument) exits 0.
Modes: hook JSON on stdin · `--selftest` · `--explain "<cmd>"`.
"""
import importlib.util
import json
import os
import re
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
_GUARD = os.path.join(_ROOT, "scripts", "pipeline_rc_guard.py")
_BLOCK_LINE = "   ⛔ BLOCKED by PROME/tools/hooks/pipeline_rc_block.py (WQ-244, Will 2026-09-17): fix the rc read and re-run.\n"
_QUOTED = re.compile(r"\"(?:[^\"\\]|\\.)*\"|'[^']*'", re.S)


def _blank_quoted_pipes(cmd):
    """Replace every PIPE CHARACTER inside a quoted string with a space — a quoted pipe is text, never a
    pipeline. Only the `|` goes: a `$?` read inside the same quoted string (`echo "RC=$? | done"`) must
    survive, or the blanking would manufacture a false NEGATIVE on a real defect (drilled below)."""
    return _QUOTED.sub(lambda m: m.group(0).replace("|", " "), cmd)


def _load(path=_GUARD):
    spec = importlib.util.spec_from_file_location("pipeline_rc_guard", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def verdict(cmd, guard_path=_GUARD):
    """(hit, message) — a hit must survive the quoted-pipe blanking."""
    mod = _load(guard_path)
    hit, msg = mod.diagnose(cmd)
    if hit and not mod.diagnose(_blank_quoted_pipes(cmd))[0]:
        return False, ""
    return hit, msg


def _handle(data, guard_path=_GUARD):
    try:
        if not isinstance(data, dict):
            raise TypeError(f"hook input is {type(data).__name__}, expected an object")
        if data.get("tool_name") != "Bash":
            return 0
        ti = data.get("tool_input")
        if ti is not None and not isinstance(ti, dict):
            raise TypeError(f"tool_input is {type(ti).__name__}, expected an object")
        cmd = (ti or {}).get("command", "") or ""
        hit, msg = verdict(cmd, guard_path)
    except Exception as e:
        sys.stderr.write(f"⚠️ pipeline_rc_block: {type(e).__name__}: {e} — ALLOWING without a check. "
                         "Fail-open, DECLARED (WQ-244).\n")
        return 0
    if hit:
        msg = msg.replace("   ⚠️ WARNING ONLY — nothing is blocked; re-run it however you like.\n", _BLOCK_LINE)
        if _BLOCK_LINE not in msg:
            msg += _BLOCK_LINE
        sys.stderr.write(msg)
        return 2
    return 0


EXPECTED_DRILLS = 12


def selftest():
    fails = []
    def drill(label, want, data, path=_GUARD):
        try:
            rc = _handle(data, path)
        except Exception as e:
            rc = f"raised {type(e).__name__}"
        ok = rc == want
        print(f"  {'✓' if ok else '✗'} rc={rc!s:4} want={want}  {label}")
        if not ok: fails.append(label)
    bash = lambda c: {"tool_name": "Bash", "tool_input": {"command": c}}
    drill("B1 hit: gate | tail; echo $?  -> 2", 2, bash('python3 PROME/tools/boot_session.py --replay 2>&1 | tail -80; echo "RC=$?"'))
    drill("B1 hit: three-state || collapse -> 2", 2, bash('python3 scripts/read_cap_check.py --agent BROCK || echo "read cap FAILED"'))
    drill("B1 hit survives blanking: the $? read sits in a quoted string that ALSO holds a pipe -> 2", 2, bash('python3 scripts/validate_all.py 2>&1 | tail -5; echo "RC=$? | done"'))
    drill("B2 clean: piped for display, $? never read -> 0", 0, bash('python3 scripts/read_cap_check.py --agent PROME | tail -2'))
    drill("B2 clean: PIPESTATUS -> 0", 0, bash('python3 scripts/read_cap_check.py --fleet | tail -3; echo "RC=${PIPESTATUS[0]}"'))
    drill("B2 clean: ordinary ls | head; echo $? -> 0", 0, bash('ls -la AGENTS/ | head -20; echo "rc=$?"'))
    drill("B6 ❌3 VERBATIM: a fully-quoted echo of the anti-pattern -> 0", 0, bash('echo "do not write: python3 scripts/read_cap_check.py --agent PROME | tail -1; echo $?"'))
    drill("B6: the same text as a printf argument in single quotes -> 0", 0, bash("printf '%s\\n' 'never: python3 scripts/validate_all.py | tail -1; echo $?' >> notes.md"))
    drill("B3 malformed: list -> 0", 0, [])
    drill("B3 malformed: tool_input is a string -> 0", 0, {"tool_name": "Bash", "tool_input": "x"})
    drill("non-Bash tool -> 0", 0, {"tool_name": "Edit", "tool_input": {"file_path": "x"}})
    drill("B4 recogniser missing -> 0 (fail-open on the wrapper's own error)", 0, bash('python3 scripts/validate_all.py | tail -1; echo $?'), path="/nonexistent/pipeline_rc_guard.py")
    total = 12
    if total != EXPECTED_DRILLS:
        fails.append("SUITE SIZE CHANGED (PAT-172)")
    for f in fails: print(f"  ❌ {f}")
    print(f"{'✅' if not fails else '❌'} PIPELINE-RC-BLOCK SELFTEST {total - len(fails)}/{total} drill(s) behaved")
    return 0 if not fails else 1


def main(argv):
    args = argv[1:]
    if "--selftest" in args:
        return selftest()
    if "--explain" in args:
        i = args.index("--explain")
        hit, msg = verdict(args[i + 1] if i + 1 < len(args) else "")
        print(msg if hit else "✅ no pipeline-$? defect recognised in that command.")
        return 0
    try:
        data = json.load(sys.stdin)
    except Exception as e:
        sys.stderr.write(f"⚠️ pipeline_rc_block: could not parse hook input ({type(e).__name__}) — ALLOWING. Fail-open, declared.\n")
        return 0
    return _handle(data)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
