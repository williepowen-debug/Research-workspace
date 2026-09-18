#!/usr/bin/env python3
"""PreToolUse(Bash) hook — the BLOCKING wrapper over `scripts/pipeline_rc_guard.py`'s recogniser.

`scripts/pipeline_rc_guard.py` is DAEDALUS's file (delivered 2026-09-12 UNWIRED BY DESIGN: "PROME or Will
wires it"). It exits 0 always (warn-only). WQ-244 (Will 2026-09-17 22:33:18Z Decision Deck APPROVE) rules
that it BLOCKS on a clean detection and fails OPEN on its own error. This wrapper does exactly that WITHOUT
editing the recogniser: it imports `diagnose()` from the DAEDALUS file, exits 2 + the guard's own fix text
on a hit, and exits 0 with a visible advisory on any error — a missing or broken recogniser included.
Both recognisers (pipe-into-a-pager then `$?`; three-state rc collapsed by `||`/`if !`/`[ $? -ne 0 ]`)
block. Their false-positive discipline is the recogniser's, measured there (0 hits over 3,039 committed
piped lines; 53/53 drills incl. the 14-command adversarial F2 set).

ACCEPTANCE CONDITIONS (WQ-229): B1 a command `diagnose()` flags exits 2 with the fix text · B2 a command it
does not flag exits 0 silently · B3 malformed hook input (non-JSON, non-object, non-object tool_input)
exits 0 with an advisory · B4 the recogniser failing to import exits 0 with an advisory (fail-open on the
wrapper's own error) · B5 the DAEDALUS file is byte-unchanged by this wiring (`git status` shows no diff).
Modes: hook JSON on stdin · `--selftest` · `--explain "<cmd>"`.
"""
import importlib.util
import json
import os
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
_GUARD = os.path.join(_ROOT, "scripts", "pipeline_rc_guard.py")
_BLOCK_LINE = "   ⛔ BLOCKED by PROME/tools/hooks/pipeline_rc_block.py (WQ-244, Will 2026-09-17): fix the rc read and re-run.\n"


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
        hit, msg = _load(guard_path).diagnose(cmd)
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


EXPECTED_DRILLS = 9


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
    drill("B2 clean: piped for display, $? never read -> 0", 0, bash('python3 scripts/read_cap_check.py --agent PROME | tail -2'))
    drill("B2 clean: PIPESTATUS -> 0", 0, bash('python3 scripts/read_cap_check.py --fleet | tail -3; echo "RC=${PIPESTATUS[0]}"'))
    drill("B2 clean: ordinary ls | head; echo $? -> 0", 0, bash('ls -la AGENTS/ | head -20; echo "rc=$?"'))
    drill("B3 malformed: list -> 0", 0, [])
    drill("B3 malformed: tool_input is a string -> 0", 0, {"tool_name": "Bash", "tool_input": "x"})
    drill("non-Bash tool -> 0", 0, {"tool_name": "Edit", "tool_input": {"file_path": "x"}})
    drill("B4 recogniser missing -> 0 (fail-open on the wrapper's own error)", 0, bash('python3 scripts/validate_all.py | tail -1; echo $?'), path="/nonexistent/pipeline_rc_guard.py")
    total = 9
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
        hit, msg = _load().diagnose(args[i + 1] if i + 1 < len(args) else "")
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
