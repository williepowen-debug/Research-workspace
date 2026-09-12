#!/usr/bin/env python3
"""pipeline_rc_guard.py — a PreToolUse Bash lint for the `cmd | tail; echo $?` class.

WHAT IT CATCHES, and it is ONE shape: a command that pipes a GATE/CHECK into a pager or filter
(`head`, `tail`, `grep`, `cut`, `sed`, `awk`, `wc`, `sort`, …) and then reads `$?`. In POSIX
shell `$?` after a pipeline is the LAST element's status, so the gate's verdict is DESTROYED and
replaced by `tail`'s (always 0) or `grep`'s (0/1 for MATCH, which reads plausible and is not the
gate's answer at all). `${PIPESTATUS[0]}` or `set -o pipefail` is the fix.

WHY IT IS A HOOK AND NOT A REPO LINT — this is the whole design argument, so it is written here
rather than in a proposal nobody re-reads. The class does NOT live in committed files: a repo-wide
census on 2026-09-12 found **ZERO documented recipes** with this shape across every `.md`/`.sh`/
`.py`/`SKILL.md`/`BOOT.md`/`CLOSEOUT.md` — every hit was a *description* of the defect, in four
separate canon surfaces including `BLUEPRINTS/CHECK_STANDARD.md:37`, which already states the rule
AND the mechanics. The defect lives in EPHEMERAL SHELL INVOCATIONS typed at the moment of use. No
file-scanning instrument can ever see one.

THE EVIDENCE THAT THIS NEEDS A MECHANISM AND NOT A FIFTH DESCRIPTION (PROME, 2026-09-12): PROME
handed DAEDALUS `python3 PROME/tools/boot_session.py ... 2>&1 | tail -80; echo "RC=$?"` as a
REFERENCE CASE for assurance-shaped output that cannot report its own failure — the transcript had
recorded `RC=0` beside a real verdict of `rc=1` — and then did the identical thing **two hours
later in the same session** (`read_cap_check ... | head -20; echo "rc=$?"` printing rc=0 against a
real rc=1). Naming a trap, in writing, to someone else, does not stop the namer from walking into
it within the same session. `finding_a_check_that_only_advises_is_overridden_the_control_is_
downstream` — and its sharper form: a rule written four times and violated twice in one day is not
under-documented, it is unmechanised. `finding_mechanize_the_cap_not_the_ritual`.

⚠️ IT WARNS, IT DOES NOT BLOCK — and that is a deliberate, narrow exception to my own preference
for blocking controls. A pipeline into a pager is the single most common legitimate shell idiom in
this repo; blocking it would produce constant false positives on commands that never read `$?` at
all, and a guard that cries wolf is silent-green inverted (the lesson `verify_push.sh` already
paid for). So the recogniser requires BOTH legs — a known gate on the left AND an `$?` read after
the pipe — and emits a warning naming the exact fix. Exit 0 always: a PreToolUse hook reserves
rc 2 for blocking, and any other non-zero is a hook ERROR that lets the command run unchecked.

⛔ THIS FILE DOES NOT REPEAT git_guard's L294 DEFECT (F-6, found the same day): every dereference
of the parsed JSON happens INSIDE the `try`, so hook input that is valid JSON but not an object
(`[]`, `null`, `"ok"`, `3`) lands in the DECLARED fail-open branch with a printed warning, never
in an undeclared `AttributeError` traceback. Drilled on all four shapes.

UNWIRED AT DELIVERY, BY DESIGN. Wiring a PreToolUse hook edits `.claude/settings.json`, which is
not DAEDALUS's to change. PROME or Will wires it; the precedent and the exact shape to copy is the
existing `git_guard.py` entry. Run `--selftest` before wiring.

FALSE-POSITIVE RATE, MEASURED BEFORE WIRING (2026-09-12): harvested every piped shell command line
from committed `.md`/`.sh`/`.tsv` in the repo — 3,039 of them — and ran this recogniser over all.
**0 hits. FP rate 0.00%.** That matters because the one thing that would kill this guard is firing
on the ordinary `cmd | head` idiom until its reader stops looking.
⚠️ WHAT THAT MEASUREMENT DOES *NOT* ESTABLISH, and the distinction is PAT-083's: it shares a corpus
with the census that found zero documented recipes, so the two are NOT independent confirmations
that the repo is clean. It establishes only that the RECOGNISER does not over-fire on real committed
command lines. The defect this guard exists for never appears in that corpus by construction — it
lives in shell typed at the moment of use, which is why a 0% FP rate here says nothing at all about
the TRUE-positive rate in the place it will actually run.

Exit contract (CHECK_STANDARD §9): 0 always in hook mode (warn-only, fail-open by design).
                                   --selftest: 0 = every drill behaved · 1 = a drill failed.

Usage:
    echo '{"tool_name":"Bash","tool_input":{"command":"..."}}' | python3 scripts/pipeline_rc_guard.py
    python3 scripts/pipeline_rc_guard.py --selftest
    python3 scripts/pipeline_rc_guard.py --explain "<a shell command>"    # ad hoc check
"""
import json
import re
import sys

# Left-hand side: things whose EXIT CODE is a verdict someone acts on. Deliberately a NAMED LIST
# rather than "any command" — a generic recogniser would fire on every `ls | head` in the repo and
# train its reader to ignore it (PAT-070/the false-alarm trap). Extend it when a new gate ships.
GATE_TOKENS = (
    r"prome_gate|boot_session|validate_all|read_cap_check|claim_check|consumer_check|"
    r"memory_index_check|memory_citation_census|ledger_staleness|corrections_boot_check|"
    r"orch_log|docket_view|asmade_audit|wiring_census|complete_check|maturity_scan|"
    r"sweeps_due|render_directory|regen_patterns_hot|spawn_list|walter_doctor|reads_check|"
    r"safe-push|verify_push|orphan_check|env_doctor|session_banner|profile_clock_check|"
    r"falsification_scan|exempt_gap|reconcile_delivery_log|gen_trigger_scan|gen_board_index|"
    r"--selftest|--check\b|_check\.py|_check\.sh|_audit\.py|_gate\.py|test_[a-z_]*\.py|pytest|unittest"
)
# Right-hand side: filters/pagers that SWALLOW the left side's status.
SWALLOWERS = r"head|tail|grep|egrep|fgrep|cut|sed|awk|wc|sort|uniq|tr|column|less|more|jq|tee|xargs|rg"
# The read of `$?` that makes it a false verdict rather than a harmless display.
RC_READ = r"\$\?|\$\{\?\}"

PIPE_THEN_RC = re.compile(
    rf"(?P<gate>{GATE_TOKENS})"        # a gate on the left
    # ⚠️ `&` MUST BE ALLOWED HERE. v1 used `[^|;&\n]*` and MISSED BOTH of PROME's real
    # instances, because each carried `2>&1` before the pipe and `&` was in the exclusion class.
    # The guard's own v1 failed on the two cases it was written from — caught only because the
    # selftest drives the VERBATIM commands, not paraphrases of them (CHECK_STANDARD §3).
    rf"[^|;\n]*"                       # its args and redirections, up to the pipe
    rf"\|\s*(?:{SWALLOWERS})\b"        # piped into something that swallows the status
    rf"[^\n]*?"                        # rest of the pipeline
    rf"(?:;|&&|\|\||\n)\s*[^\n]*?"     # then a following command
    rf"(?:{RC_READ})",                 # which reads $?
    re.I | re.S,
)
# The two correct forms — if either is present the author already knows.
ALREADY_SAFE = re.compile(r"PIPESTATUS|pipefail", re.I)


def diagnose(cmd):
    """(hit, message). Pure; no I/O. The selftest drives THIS, so the recogniser is tested
    independently of the hook plumbing — `finding_test_the_guard_not_just_the_guarded`."""
    if not cmd or not isinstance(cmd, str):
        return False, ""
    if ALREADY_SAFE.search(cmd):
        return False, ""
    m = PIPE_THEN_RC.search(cmd)
    if not m:
        return False, ""
    gate = m.group("gate")
    return True, (
        f"⚠️  pipeline_rc_guard: `$?` here reports the PAGER, not `{gate}`.\n"
        f"   In a pipeline `$?` is the LAST element's status — `tail`/`head` exit 0 whatever the\n"
        f"   gate did, and `grep` exits 0/1 for MATCH, which reads plausible and is not the gate's\n"
        f"   verdict. A failing gate will be recorded as a pass.\n"
        f"   FIX (either): `cmd | tail -80; echo \"RC=${{PIPESTATUS[0]}}\"`\n"
        f"             or: `set -o pipefail` before the pipeline\n"
        f"       or best: read the rc BARE first, then pipe for display:\n"
        f"                `out=$(cmd 2>&1); rc=$?; printf '%s\\n' \"$out\" | tail -80; echo \"RC=$rc\"`\n"
        f"   (CHECK_STANDARD §14(b). Measured 2026-09-12: this rule is written in four canon\n"
        f"    surfaces and was still walked into twice in one session, hours apart, by its namer.)\n"
        f"   command: {cmd[:180]}\n"
        f"   ⚠️ WARNING ONLY — nothing is blocked; re-run it however you like.\n"
    )


def selftest():
    """CHECK_STANDARD §3: each leg watched on a CAPABLE case AND a CLEAN case."""
    cases = [
        # (command, expect_hit, label)
        ('python3 PROME/tools/boot_session.py --replay 2>&1 | tail -80; echo "RC=$?"', True,
         "CAPABLE — PROME's own instance #1, verbatim shape"),
        ('python3 scripts/read_cap_check.py --agent BROCK | head -20; echo "rc=$?"', True,
         "CAPABLE — PROME's instance #2, two hours later"),
        ('python3 scripts/validate_all.py 2>&1 | grep FINDINGS; echo $?', True,
         "CAPABLE — grep swallows it and returns a PLAUSIBLE 0/1"),
        ('bash scripts/safe-push.sh | tail -4 && echo "rc=$?"', True,
         "CAPABLE — && instead of ;"),
        ('python3 scripts/claim_check.py --selftest | tail -1; echo "RC=${?}"', True,
         "CAPABLE — ${?} spelling"),
        # CLEAN cases — each must NOT fire, and each is a real idiom from this repo
        ('python3 scripts/read_cap_check.py --agent PROME | tail -2', False,
         "CLEAN — piped for DISPLAY, $? never read"),
        ('python3 scripts/validate_all.py; echo "RC=$?"', False,
         "CLEAN — no pipe at all, the correct form"),
        ('python3 scripts/read_cap_check.py --fleet | tail -3; echo "RC=${PIPESTATUS[0]}"', False,
         "CLEAN — PIPESTATUS: the author already knows"),
        ('set -o pipefail; python3 scripts/validate_all.py | tail -5; echo "RC=$?"', False,
         "CLEAN — pipefail set"),
        ('ls -la AGENTS/ | head -20; echo "rc=$?"', False,
         "CLEAN — not a gate; a generic recogniser would false-positive here"),
        ('git status --porcelain | wc -l; echo $?', False,
         "CLEAN — git is not in the gate list; git_guard owns that lane"),
        ('cat notes.md | grep TODO; echo $?', False,
         "CLEAN — no gate on the left"),
        ('out=$(python3 scripts/validate_all.py 2>&1); rc=$?; printf "%s" "$out" | tail -5; echo "RC=$rc"',
         False, "CLEAN — the recommended form: rc read BARE before the pipe"),
    ]
    fails = []
    for cmd, want, label in cases:
        got, _ = diagnose(cmd)
        mark = "✓" if got == want else "✗"
        if got != want:
            fails.append(f"{label}: expected hit={want}, got {got} — {cmd[:70]}")
        print(f"  {mark} hit={str(got):5} want={str(want):5}  {label}")
    # malformed-input legs — the L294 F-6 defect, tested rather than assumed
    for bad in ([], None, "ok", 3, {"tool_name": "Bash"}, {"tool_name": "Bash", "tool_input": None}):
        try:
            rc = _handle(bad)
            ok = rc == 0
        except Exception as e:
            ok = False
            fails.append(f"malformed input {bad!r} raised {type(e).__name__} — the F-6 defect")
        print(f"  {'✓' if ok else '✗'} malformed hook input {str(bad)[:24]:26} -> rc 0, no exception")
    for f in fails:
        print(f"  ❌ {f}")
    total = len(cases) + 6
    print(f"{'✅' if not fails else '❌'} PIPELINE-RC-GUARD SELFTEST {total - len(fails)}/{total} drill(s) behaved")
    return 0 if not fails else 1


def _handle(data):
    """Everything that touches `data` lives here, and every dereference is guarded. Returns an
    exit code. ⛔ Never raises for a non-object input — that is L294 F-6, and this file is the
    same shape as the file that has it."""
    try:
        if not isinstance(data, dict):
            raise TypeError(f"hook input is {type(data).__name__}, expected an object")
        if data.get("tool_name") != "Bash":
            return 0
        ti = data.get("tool_input")
        cmd = (ti or {}).get("command", "") if isinstance(ti, dict) else ""
    except Exception as e:
        sys.stderr.write(f"⚠️ pipeline_rc_guard: unusable hook input ({type(e).__name__}: {e}) — "
                         "ALLOWING without a check. This is fail-open, and it is DECLARED.\n")
        return 0
    hit, msg = diagnose(cmd)
    if hit:
        sys.stderr.write(msg)
    return 0


def main(argv):
    args = argv[1:]
    if "--selftest" in args:
        return selftest()
    if "--explain" in args:
        i = args.index("--explain")
        cmd = args[i + 1] if i + 1 < len(args) else ""
        hit, msg = diagnose(cmd)
        print(msg if hit else "✅ no pipeline-$? defect recognised in that command.")
        return 0
    if args:
        print(f"pipeline_rc_guard: unknown argument(s) {' '.join(args)} — modes are "
              f"`--selftest`, `--explain <cmd>`, or hook JSON on stdin.", file=sys.stderr)
        return 0
    try:
        data = json.load(sys.stdin)
    except Exception as e:
        sys.stderr.write(f"⚠️ pipeline_rc_guard: could not parse hook input ({type(e).__name__}) — "
                         "ALLOWING without a check. This is fail-open, not coverage.\n")
        return 0
    return _handle(data)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
