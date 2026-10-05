#!/usr/bin/env python3
"""PreToolUse(Bash) hook — ⚠️ ADVISORY since WQ-263 (Will 2026-09-22: a confirmed hit WARNS, exit 0, never 2; the history below records the BLOCKING era) — the wrapper over `scripts/pipeline_rc_guard.py`'s recogniser.

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
v6 (2026-09-18, after the FIFTH independent cold read `wq244cold5`, 5 ❌ on this wrapper — the LAST pass today; the
   convergence question is WQ-263, Will's):
 ❌4 `cat > note.md <<'EOF' … <the anti-pattern> … EOF` BLOCKED — the wrapper had no heredoc handling (FALSE POSITIVE,
    the third spelling of "writing the warning is blocked"). Now: heredoc bodies (terminator must exist) are dropped
    before scanning.
 ❌5 `ls scripts/{read_cap_check,validate_all}.py | wc -l; echo $?` BLOCKED — brace EXPANSION read as a brace GROUP by
    the v5 boundary (FALSE POSITIVE, created by the v5 fix). Now: `{` bounds a segment only when followed by
    whitespace, and only a bare `{` token is stripped from a head.
 ❌9 `command python3 <gate> | tail; echo $?` slipped through — v5 stopped walking `command` to kill r4 ❌6 (silent
    bypass). Now: `command` is walked past unless its next token is a lookup flag (`-v`/`-V`/`-p`).
 ❌10 `gate |& tail -1; echo $?` — `|&` (bash's `2>&1 |`) is unseen by DAEDALUS's recogniser: its perimeter, declared,
    packeted.
 ❌13 a stale comment still listed `command` among walked prefixes — corrected.
v5 (2026-09-18, after the FOURTH independent cold read `wq244cold4`, 4 ❌ on this wrapper — each a drill below):
 ❌3 `… | tail -3 || echo $?`: the immediate-segment test found the last `|` inside `||` and counted zero separators
    (silent bypass). Now: the pipeline's last SINGLE pipe is located and the separator set is counted properly.
 ❌4 a `;` inside a quoted string (`echo "a;b rc=$?"`) was counted as a command boundary (silent bypass). Now: `;`,
    `&` and newlines inside quoted runs are blanked before counting, like the pipe characters.
 ❌5 `time { gate | tail; }; echo $?` — `{` was not a segment boundary, so the gate read as `time`'s argument (silent
    bypass). Now: `{` bounds a segment and is stripped from a head token.
 ❌6 `command -v pytest | head -1; echo $?` BLOCKED — the v4 prefix walk promoted `command`'s lookup argument to the
    command word (FALSE POSITIVE). Now: `command` is not walked past.
 ⚠️ the PAT-172 size assertion compared a literal to itself; the drill count is now derived from the drills run.
v4 (2026-09-18, after the THIRD independent cold read `wq244cold3`, 4 ❌ on this wrapper — each a drill below):
 ❌5 the command-position test walked ONE interpreter level, so `time` / `env VAR=1` / `nice -n 5` before `python3 <gate>`
    suppressed a real defect. Now: prefix commands (time env nice sudo timeout nohup stdbuf command exec) and their
    arguments are walked past before the command word is judged.
 ❌6 only the FIRST recogniser-1 match was tested, so a legitimate argument-position mention earlier in the line
    consumed the rest. Now: EVERY match is tested; any one in command position confirms the hit.
 ❌7 a `$?` belonging to an unrelated LATER command (`… | tail -3; git status --short; echo $?`) blocked a gate piped for
    display — the recogniser's regex lets any number of commands sit between the pipeline and the read. Now: the
    read must sit in the segment IMMEDIATELY after the pipeline (exactly one command boundary between them).
 ❌8 (wiring) `python3 "$(git rev-parse --show-toplevel)/…"` exits 2 — the BLOCK code — if the root fails to
    resolve. Now: the wiring tests the script path first and fails OPEN with an advisory when it is missing.
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
_ADVISE_LINE = "   ⚠️ ADVISORY (pipeline_rc_block.py, WQ-263 2026-09-22): NOT blocked — fix the rc read if the diagnosis is right.\n"
_LIFT = (re.compile(r"\b(?:bash|sh|zsh|dash)\s+(?:-[a-zA-Z]*c[a-zA-Z]*\s+)(['\"])(.*?)\1", re.S),
         re.compile(r"\beval\s+(['\"])(.*?)\1", re.S))
_QUOTED = re.compile(r"(?<![\w])\"(?:[^\"\\]|\\.)*\"|(?<![\w])'[^']*'", re.S)
_INTERP = ("python3", "python", "bash", "sh", "zsh", "source", ".")
_PREFIX = ("time", "env", "nice", "sudo", "timeout", "nohup", "stdbuf", "exec")
_ENV_ASSIGN = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")


def _lift(cmd):
    for rx in _LIFT:
        cmd = rx.sub(lambda m: " " + m.group(2) + " ", cmd)
    return cmd


def _blank_quoted_pipes(cmd):
    """Replace every PIPE, `;`, `&` and NEWLINE inside a (word-boundary-opened) quoted string with a space — quoted
    text is never a pipeline or a command boundary. A `$?` read inside the same string survives, so blanking can
    never manufacture a false negative on a real defect (r4 ❌4 added the separators)."""
    return _QUOTED.sub(lambda m: re.sub(r"[|;&\n]", " ", m.group(0)), cmd)


_BRACE_GROUP = re.compile(r"\{(?=\s)")      # a brace GROUP opens `{ `; a brace EXPANSION `{a,b}` does not (r5 ❌5)
_HEREDOC = re.compile(r"<<-?\s*(['\"]?)(\w+)\1")


def _last_brace_group(text, before):
    pos = -1
    for mm in _BRACE_GROUP.finditer(text, 0, before):
        pos = mm.start()
    return pos


def _drop_heredocs(cmd):
    """Drop heredoc BODIES (terminator must exist, bash-exact) so prose is never scanned as a pipeline (r5 ❌4)."""
    out, lines, i = [], cmd.split("\n"), 0
    while i < len(lines):
        ln = lines[i]; out.append(ln)
        m = _HEREDOC.search(ln)
        if m:
            dash, term = ln[m.start():m.start() + 3] == "<<-", m.group(2)
            end = next((j for j in range(i + 1, len(lines)) if (lines[j].lstrip("\t") if dash else lines[j]) == term), None)
            if end is not None:
                i = end
        i += 1
    return "\n".join(out)


def _gate_in_command_position(text, m):
    """m = the recogniser's PIPE_THEN_RC match. True when the gate token is the command word of its own segment
    (the text from the previous ; & | ( or newline up to the gate), or the first non-flag argument of an interpreter."""
    start = m.start("gate")
    seg_start = max([text.rfind(ch, 0, start) for ch in (";", "\n", "(", "|", "&")] + [_last_brace_group(text, start)] + [-1]) + 1
    toks = text[seg_start:m.end("gate")].split()
    # walk past env assignments and PREFIX commands with their arguments (r3 ❌5): `time`, `env VAR=1`, `nice -n 5`,
    # `sudo -u x`, `timeout 30`, `nohup`, `stdbuf -oL`, `exec`, and `command X` (but never `command -v X`, a lookup —
    # r4 ❌6 / r5 ❌9) — then judge the command word.
    while toks:
        t = toks[0][1:] if toks[0].startswith("(") else toks[0]
        if t == "{":
            toks.pop(0); continue
        if _ENV_ASSIGN.match(t):
            toks.pop(0); continue
        if os.path.basename(t) == "command":
            if len(toks) > 1 and toks[1].startswith(("-v", "-V", "-p")):
                break                                 # a lookup, not a run (r4 ❌6)
            toks.pop(0); continue                     # `command X` runs X (r5 ❌9)
        if os.path.basename(t) in _PREFIX:
            toks.pop(0)
            while toks and (toks[0].startswith("-") or _ENV_ASSIGN.match(toks[0]) or toks[0].isdigit()):
                toks.pop(0)
            continue
        break
    if not toks:
        return False
    head = toks[0][1:] if toks[0].startswith("(") else toks[0]
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


_SEP = re.compile(r";|&&|\|\||\n")


_SINGLE_PIPE = re.compile(r"(?<!\|)\|(?!\|)")


def _read_is_immediate(m):
    """r3 ❌7: the `$?` read must sit in the segment IMMEDIATELY after the pipeline — exactly one command boundary
    between the pipeline's last SINGLE pipe and the read. Two or more means the `$?` belongs to a later command.
    r4 ❌3: `||` is a boundary, never a pipe, so the last single pipe is located with a look-around."""
    whole = m.group(0)
    pipes = list(_SINGLE_PIPE.finditer(whole))
    tail = whole[pipes[-1].end():] if pipes else whole
    tail = re.sub(r";\s*}", "", tail)          # a brace group's closing `; }` is not a command boundary (r4 ❌5)
    return len(_SEP.findall(tail)) == 1


def verdict(cmd, guard_path=_GUARD):
    """(hit, message, suppressed_reason)."""
    mod = _load(guard_path)
    text = _blank_quoted_pipes(_lift(_drop_heredocs(cmd)))
    hit, msg = mod.diagnose(text)
    if not hit:
        raw_hit, _ = mod.diagnose(cmd)
        return False, "", ("raw hit suppressed: the pipe was inside a quoted string" if raw_hit else "")
    if mod.ALREADY_SAFE.search(text):
        return True, msg, ""
    matches = list(mod.PIPE_THEN_RC.finditer(text))
    if not matches:
        return True, msg, ""                      # recogniser 2 (three-state) — DAEDALUS's own command-word test
    reasons = []
    for m in matches:                              # r3 ❌6: every match, not the first
        if not _gate_in_command_position(text, m):
            seg = text[max([text.rfind(c, 0, m.start("gate")) for c in (";", "\n", "(", "|", "&")] + [_last_brace_group(text, m.start("gate"))]) + 1:m.start("gate")].split()
            reasons.append(f"`{m.group('gate')}` is an ARGUMENT of `{seg[0] if seg else '?'}`, not the command run")
            continue
        if not _read_is_immediate(m):
            reasons.append(f"the `$?` after `{m.group('gate')}`'s pipeline belongs to a LATER command, not the pipeline")
            continue
        return True, msg, ""
    hit2, msg2 = mod._diagnose_three_state(text)
    if hit2:
        return True, msg2, ""
    return False, "", "raw hit suppressed: " + "; ".join(reasons)


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
        _advise(f"⚠️ pipeline_rc_block: {type(e).__name__}: {e} — ALLOWING without a check. "
                "Fail-open, DECLARED (WQ-244).\n")
        return 0
    if hit:
        # WQ-263 (Will 2026-09-22 19:37 / 19:51 ET, "approved" + "with CATO fix"): this wrapper is ADVISORY. Five
        # independent reads found a false positive in every round, the last ones in the wrapper's OWN compensation
        # layer, so a confirmed hit now WARNS and exits 0. The diagnosis text is unchanged; only the verdict moved.
        _advise(msg.replace("   ⚠️ WARNING ONLY — nothing is blocked; re-run it however you like.\n", "") + _ADVISE_LINE)
        return 0
    return 0


def _advise(text):
    # Exit-0 stderr is debug-only in Claude; context must travel on stdout.
    # No permissionDecision: an advisory must preserve the normal permission flow.
    sys.stderr.write(text)
    sys.stdout.write(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "additionalContext": text}}) + "\n")


EXPECTED_DRILLS = 36


def selftest():
    fails = []; ran = [0]
    def drill(label, want, data, path=_GUARD):
        ran[0] += 1
        # WQ-263: the wrapper never blocks. `want` keeps its historical meaning — 2 = the recogniser must CONFIRM a
        # hit, 0 = it must not — and a confirmed hit must now surface as an ADVISORY on stderr with rc 0.
        import io, contextlib
        err = io.StringIO()
        out = io.StringIO()
        try:
            with contextlib.redirect_stderr(err), contextlib.redirect_stdout(out):
                rc = _handle(data, path)
        except Exception as e:
            rc = f"raised {type(e).__name__}"
        advised = _ADVISE_LINE in err.getvalue()
        ok = (rc == 0 and advised) if want == 2 else (rc == 0 and not advised)
        if err.getvalue():
            try:
                payload = json.loads(out.getvalue())["hookSpecificOutput"]
                ok = ok and payload == {"hookEventName": "PreToolUse", "additionalContext": err.getvalue()}
            except (ValueError, KeyError):
                ok = False
        else:
            ok = ok and not out.getvalue()
        print(f"  {'✓' if ok else '✗'} rc={rc!s:4} advised={advised!s:5} want={'hit→advisory' if want == 2 else 'no-hit'}  {label}")
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
    # r3 ❌5 / ❌6 / ❌7 VERBATIM
    drill("r3 ❌5: time python3 <gate> | tail; echo $? -> 2", 2, bash('time python3 scripts/validate_all.py 2>&1 | tail -1; echo $?'))
    drill("r3 ❌5: env VAR=1 python3 <gate> | tail; echo $? -> 2", 2, bash('env VAR=1 python3 scripts/validate_all.py 2>&1 | tail -1; echo $?'))
    drill("r3 ❌5: nice -n 5 python3 <gate> | tail; echo $? -> 2", 2, bash('nice -n 5 python3 scripts/validate_all.py 2>&1 | tail -1; echo $?'))
    drill("r3 ❌6: an argument-position mention BEFORE a real defect on the same line -> 2", 2, bash('grep -rn "read_cap_check" AGENTS/ | head -20; echo $?; python3 scripts/validate_all.py 2>&1 | tail -1; echo $?'))
    drill("r3 ❌7: gate piped for display, then an unrelated command, then echo $? -> 0", 0, bash('python3 scripts/read_cap_check.py --agent PROME | tail -3; git status --short; echo $?'))
    # r4 ❌3 / ❌4 / ❌5 / ❌6 VERBATIM
    drill("r4 ❌3: gate | tail -3 || echo $? -> 2", 2, bash('python3 scripts/validate_all.py 2>&1 | tail -3 || echo $?'))
    drill("r4 ❌4: a ; inside the quoted read string -> 2", 2, bash('python3 scripts/validate_all.py 2>&1 | tail -1; echo "a;b rc=$?"'))
    drill("r4 ❌5: time { gate | tail -1; }; echo $? -> 2", 2, bash('time { python3 scripts/validate_all.py 2>&1 | tail -1; }; echo $?'))
    drill("r4 ❌5: bare { gate | tail -1; }; echo $? -> 2", 2, bash('{ python3 scripts/validate_all.py 2>&1 | tail -1; }; echo $?'))
    drill("r4 ❌6: command -v pytest | head -1; echo $? -> 0 (a lookup, not a run)", 0, bash('command -v pytest | head -1; echo $?'))
    # r5 ❌4 / ❌5 / ❌9 / ❌10 VERBATIM
    drill("r5 ❌4: the anti-pattern inside a heredoc BODY (writing a note) -> 0", 0, bash("cat > note.md <<'EOF'\npython3 scripts/validate_all.py 2>&1 | tail -1; echo $?\nEOF"))
    drill("r5 ❌5: ls scripts/{read_cap_check,validate_all}.py | wc -l; echo $? — brace EXPANSION -> 0", 0, bash('ls scripts/{read_cap_check,validate_all}.py | wc -l; echo $?'))
    drill("r5 ❌9: command python3 <gate> | tail; echo $? — `command X` runs X -> 2", 2, bash('command python3 scripts/validate_all.py 2>&1 | tail -1; echo $?'))
    # The shared recognizer now understands |&; keep the real hit covered.
    drill("gate |& tail; echo $? -> advisory", 2, bash('python3 scripts/validate_all.py |& tail -1; echo $?'))
    # --explain honesty (⚠️17): a suppressed raw hit is REPORTED
    _, _, why = verdict('python3 scripts/validate_all.py | tail -1; git status; echo $?')
    ok = why.startswith("raw hit suppressed"); print(f"  {'✓' if ok else '✗'} verdict() names a suppressed raw hit ({why[:60]!r})")
    if not ok: fails.append("suppression not reported")
    _, _, why = verdict('ls -la | head -3; echo $?')
    ok = why == ""; print(f"  {'✓' if ok else '✗'} verdict() reports nothing when there was no raw hit")
    if not ok: fails.append("phantom suppression reported")
    total = ran[0] + 2                      # drills run + the two verdict() checks below
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
        _advise(f"⚠️ pipeline_rc_block: could not parse hook input ({type(e).__name__}) — ALLOWING. Fail-open, declared.\n")
        return 0
    return _handle(data)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
