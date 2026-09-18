#!/usr/bin/env python3
"""PreToolUse(Bash) hook — the BLOCKING wrapper over `scripts/pipeline_rc_guard.py`'s recogniser.

`scripts/pipeline_rc_guard.py` is DAEDALUS's file (delivered 2026-09-12 UNWIRED BY DESIGN: "PROME or Will wires
it"). It exits 0 always (warn-only). WQ-244 (Will 2026-09-17 22:33:18Z Decision Deck APPROVE) rules that it BLOCKS
on a clean detection and fails OPEN on its own error. This wrapper imports `diagnose()` from the DAEDALUS file
(byte-unchanged), exits 2 + the guard's own fix text on a CONFIRMED hit, and exits 0 with a visible advisory on any
error of its own — a missing or broken recogniser included.

v3 (2026-09-18, after the SECOND independent cold read `wq244cold2`, 4 ❌ on this wrapper — each a drill below):
 ❌7 recogniser 1 (gate | pager … $?) has NO command-word test, so five ORDINARY commands blocked — `grep -rn
    "read_cap_check" … | head; echo $?`, `ls scripts/*_check.py | wc -l; echo $?`, … — the gate NAME was an argument.
    Now: a recogniser-1 hit is CONFIRMED only if the gate token sits in COMMAND position of its pipeline segment
    (the command word, or an interpreter's first non-flag argument; a flag-shaped gate such as `--selftest` needs an
    interpreter or a script as the command word). Recogniser 2 (`||` / `if !` / `[ $? -ne 0 ]`) already has that test
    in DAEDALUS's file and is consulted as-is.
 ❌8 v2's blanking ate a real pipe inside `bash -c "…"`. Now: `-c` and `eval` bodies are LIFTED before blanking.
 ❌9 an apostrophe in a word (`don't`) paired with a later quote and swallowed a real pipe. Now: a quote opens only
    at a word boundary.
 ❌10 `PIPESTATUS`/`pipefail` mentioned ANYWHERE (a comment, an unrelated string) disables both recognisers via the
    recogniser's own `ALREADY_SAFE` allowlist — DAEDALUS's file, declared here as the recogniser's perimeter and
    packeted to DAEDALUS, not re-implemented by this wrapper.
v2 (after `wq244cold`): pipes inside quoted strings are text — their `|` characters are blanked before a hit is
confirmed; a `$?` read inside the same quoted string still counts.

ACCEPTANCE CONDITIONS (WQ-229): B1 a command the recogniser flags, whose gate sits in command position, exits 2
with the fix text · B2 a command it does not flag exits 0 silently · B3 malformed hook input exits 0 with an
advisory · B4 the recogniser failing to import exits 0 with an advisory · B5 the DAEDALUS file is byte-unchanged ·
B6 a fully-quoted mention of the anti-pattern exits 0 · B7 a gate NAME in argument position (grep/ls/find/sed/git-log
of it) exits 0 · B8 a real defect inside a lifted `-c`/`eval` body, or beside a word-internal apostrophe, exits 2.
Modes: hook JSON on stdin · `--selftest` · `--explain "<cmd>"` (says when a raw hit was SUPPRESSED and why).
"""
import importlib.util
import json
import os
import re
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
_GUARD = os.path.join(_ROOT, "scripts", "pipeline_rc_guard.py")
_BLOCK_LINE = "   ⛔ BLOCKED by PROME/tools/hooks/pipeline_rc_block.py (WQ-244, Will 2026-09-17): fix the rc read and re-run.\n"
_LIFT = (re.compile(r"\b(?:bash|sh|zsh|dash)\s+(?:-[a-zA-Z]*c[a-zA-Z]*\s+)(['\"])(.*?)\1", re.S),
         re.compile(r"\beval\s+(['\"])(.*?)\1", re.S))
_QUOTED = re.compile(r"(?<![\w])\"(?:[^\"\\]|\\.)*\"|(?<![\w])'[^']*'", re.S)
_INTERP = ("python3", "python", "bash", "sh", "zsh", "exec", "command", "time", "source", ".")
_ENV_ASSIGN = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")


def _lift(cmd):
    for rx in _LIFT:
        cmd = rx.sub(lambda m: " " + m.group(2) + " ", cmd)
    return cmd


def _blank_quoted_pipes(cmd):
    """Replace every PIPE CHARACTER inside a (word-boundary-opened) quoted string with a space. A `$?` read inside
    the same string survives, so blanking can never manufacture a false negative on a real defect."""
    return _QUOTED.sub(lambda m: m.group(0).replace("|", " "), cmd)


def _gate_in_command_position(text, m):
    """m = the recogniser's PIPE_THEN_RC match. True when the gate token is the command word of its own segment
    (the text from the previous ; & | ( or newline up to the gate), or the first non-flag argument of an interpreter."""
    start = m.start("gate")
    seg_start = max([text.rfind(ch, 0, start) for ch in (";", "\n", "(", "|", "&")] + [-1]) + 1
    toks = text[seg_start:m.end("gate")].split()
    while toks and _ENV_ASSIGN.match(toks[0]):
        toks.pop(0)
    if not toks:
        return False
    head = toks[0].lstrip("(")
    gate = m.group("gate")
    cands = [head]
    if head in _INTERP or os.path.basename(head) in _INTERP:
        for t in toks[1:]:
            if not t.startswith("-"):
                cands.append(t)
                break
    if gate.startswith("-"):      # --selftest / --check: a flag — the command must be an interpreter or a script
        return os.path.basename(head) in _INTERP or head.endswith((".py", ".sh")) or any(c.endswith((".py", ".sh")) for c in cands[1:])
    return any(gate.lower() in os.path.basename(c).lower() for c in cands)


def verdict(cmd, guard_path=_GUARD):
    """(hit, message, suppressed_reason)."""
    mod = _load(guard_path)
    text = _blank_quoted_pipes(_lift(cmd))
    hit, msg = mod.diagnose(text)
    if not hit:
        raw_hit, _ = mod.diagnose(cmd)
        return False, "", ("raw hit suppressed: the pipe was inside a quoted string" if raw_hit else "")
    m = mod.PIPE_THEN_RC.search(text)
    if m and not _gate_in_command_position(text, m):
        hit2, msg2 = mod._diagnose_three_state(text)
        if hit2:
            return True, msg2, ""
        return False, "", f"raw hit suppressed: `{m.group('gate')}` is an ARGUMENT of `{text[max(text.rfind(c,0,m.start('gate')) for c in (';','\n','(','|','&'))+1:m.start('gate')].split()[0] if text[max(text.rfind(c,0,m.start('gate')) for c in (';','\n','(','|','&'))+1:m.start('gate')].split() else '?'}`, not the command run"
    return True, msg, ""


def _load(path=_GUARD):
    spec = importlib.util.spec_from_file_location("pipeline_rc_guard", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


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
        hit, msg, _ = verdict(cmd, guard_path)
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


EXPECTED_DRILLS = 22


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
    drill("B1 hit: flag-shaped gate (--selftest) on a script -> 2", 2, bash('python3 PROME/tools/measure.py --selftest 2>&1 | tail -1; echo "RC=$?"'))
    drill("B1 hit survives blanking: the $? read sits in a quoted string that ALSO holds a pipe -> 2", 2, bash('python3 scripts/validate_all.py 2>&1 | tail -5; echo "RC=$? | done"'))
    drill("B2 clean: piped for display, $? never read -> 0", 0, bash('python3 scripts/read_cap_check.py --agent PROME | tail -2'))
    drill("B2 clean: PIPESTATUS -> 0", 0, bash('python3 scripts/read_cap_check.py --fleet | tail -3; echo "RC=${PIPESTATUS[0]}"'))
    drill("B2 clean: ordinary ls | head; echo $? -> 0", 0, bash('ls -la AGENTS/ | head -20; echo "rc=$?"'))
    drill("B6 r1 ❌3 VERBATIM: a fully-quoted echo of the anti-pattern -> 0", 0, bash('echo "do not write: python3 scripts/read_cap_check.py --agent PROME | tail -1; echo $?"'))
    drill("B6: the same text as a single-quoted printf argument -> 0", 0, bash("printf '%s\\n' 'never: python3 scripts/validate_all.py | tail -1; echo $?' >> notes.md"))
    # r2 ❌7 VERBATIM — gate NAMES in argument position
    drill("B7 r2 ❌7: grep -rn \"read_cap_check\" AGENTS/ | head -20; echo $? -> 0", 0, bash('grep -rn "read_cap_check" AGENTS/ | head -20; echo $?'))
    drill("B7 r2 ❌7: ls scripts/*_check.py | wc -l; echo \"rc=$?\" -> 0", 0, bash('ls scripts/*_check.py | wc -l; echo "rc=$?"'))
    drill("B7 r2 ❌7: git log --oneline -50 | grep validate_all | head -3; echo $? -> 0", 0, bash('git log --oneline -50 | grep validate_all | head -3; echo $?'))
    drill("B7 r2 ❌7: sed -n \"1,40p\" scripts/read_cap_check.py | head -20; echo $? -> 0", 0, bash('sed -n "1,40p" scripts/read_cap_check.py | head -20; echo $?'))
    drill("B7 r2 ❌7: find . -name \"*_gate.py\" | wc -l; echo $? -> 0", 0, bash('find . -name "*_gate.py" | wc -l; echo $?'))
    # r2 ❌8 / ❌9 — real defects that v2 suppressed
    drill("B8 r2 ❌8: real defect inside bash -c \"…\" -> 2", 2, bash('bash -c "python3 scripts/validate_all.py 2>&1 | tail -1; echo $?"'))
    drill("B8 r2 ❌9: word-internal apostrophe before a real defect -> 2", 2, bash("echo don't worry; python3 scripts/validate_all.py 2>&1 | tail -1; echo 'RC='$?"))
    drill("B3 malformed: list -> 0", 0, [])
    drill("B3 malformed: tool_input is a string -> 0", 0, {"tool_name": "Bash", "tool_input": "x"})
    drill("non-Bash tool -> 0", 0, {"tool_name": "Edit", "tool_input": {"file_path": "x"}})
    drill("B4 recogniser missing -> 0 (fail-open on the wrapper's own error)", 0, bash('python3 scripts/validate_all.py | tail -1; echo $?'), path="/nonexistent/pipeline_rc_guard.py")
    # --explain honesty (⚠️17): a suppressed raw hit is REPORTED
    _, _, why = verdict('grep -rn "read_cap_check" AGENTS/ | head -20; echo $?')
    ok = why.startswith("raw hit suppressed"); print(f"  {'✓' if ok else '✗'} verdict() names a suppressed raw hit ({why[:60]!r})")
    if not ok: fails.append("suppression not reported")
    _, _, why = verdict('ls -la | head -3; echo $?')
    ok = why == ""; print(f"  {'✓' if ok else '✗'} verdict() reports nothing when there was no raw hit")
    if not ok: fails.append("phantom suppression reported")
    total = 22
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
        hit, msg, why = verdict(args[i + 1] if i + 1 < len(args) else "")
        print(msg if hit else ("✅ no pipeline-$? defect confirmed in that command." + (f"\n   ({why})" if why else "")))
        return 0
    try:
        data = json.load(sys.stdin)
    except Exception as e:
        sys.stderr.write(f"⚠️ pipeline_rc_block: could not parse hook input ({type(e).__name__}) — ALLOWING. Fail-open, declared.\n")
        return 0
    return _handle(data)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
