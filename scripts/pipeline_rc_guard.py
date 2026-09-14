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
import os
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

# ── SECOND RECOGNISER: A THREE-STATE rc COLLAPSED BY A TWO-VALUED IDIOM ──────────────────────
# ADDED 2026-09-14 (DOCKET L355, the rule the row generalises). SAME FAMILY, SAME REASON THIS FILE
# IS A HOOK: a verdict destroyed at an EPHEMERAL call site that no repo scan can ever see.
#
# THE INSTANCE. DAEDALUS's last command of 2026-09-12 was
#     bash verify_push.sh "$s" >/dev/null 2>&1 || { echo "NOT ON ORIGIN"; }
# It reported 32 of 32 commits NOT ON ORIGIN. All 32 were on origin. `verify_push.sh` had behaved
# CORRECTLY: it returns rc 2 CANNOT-CERTIFY for a subject match older than its 60-minute window —
# a contract written into that file IN CAPITALS BY THE SAME AUTHOR after it false-alarmed on its
# own second use. The `||` collapsed rc 2 into rc 1. Nothing was ever at risk; the alarm was the
# caller's, and a caller who believes it goes looking for a push failure that never happened.
#
# ⛔ THE RULE: a three-state rc contract is defeated by `||`, `&&`, `!`, `if not`, and every other
# two-valued idiom in the language. Writing `rc 0/1/2` in a docstring does not make callers
# three-valued — ONLY A CALL SITE THAT NAMES THE STATES IS. So the author of the contract is not
# protected by having authored it; this instance is the proof.
#
# WHY A HOOK AND NOT A LINT — MEASURED, NOT ASSUMED (census 2026-09-14, this repo, every committed
# .md/.sh/.py/.tsv/.json): 31 tools reserve rc 2, and the census returned 28 raw matches of a
# two-valued idiom near one of their names. ON INSPECTION, **TRUE POSITIVES = 0.** Every hit was
# prose (KB/PATTERNS/DOCKET rows that merely contain `||`), a `(cd "$(git rev-parse --show-toplevel)"
# && python3 …)` CWD-GUARD — where the `&&` precedes the tool and consumes nothing — or a
# CORRECTLY-LABELLED QUOTATION of the defect inside its own diagnosis (the run record and the
# memory file that document the instance above). Committed recipes are clean; the defect is typed
# at the moment of use. Identical shape to the pipeline class this file was built for.
# ⚠️ PAT-083: that census shares a corpus with the 2026-09-12 pipeline census, so the two are NOT
# independent evidence that the repo is clean. It establishes WHERE the class lives, nothing more.
#
# FALSE-POSITIVE DISCIPLINE, the same as the recogniser above: the left side must be a tool KNOWN
# to reserve rc 2, never any command. `cmd || echo failed` is the most ordinary idiom in shell and
# firing on it would kill this guard's credibility inside a day.
# The list is DERIVED, and the derivation is rerunnable rather than remembered:
#   git ls-files '*.py' '*.sh' | xargs grep -lE 'CANNOT[- ]?(EVALUATE|CERTIFY)' \
#     | xargs grep -lE 'sys\.exit\(2\)|return 2\b|exit 2\b'
# Re-run it at each Wiring Sweep; a tool that gains an rc 2 and is missing here is a DORMANT guard
# leg, not a clean one (`finding_guard_correctness_and_wiring_are_independent`).
THREE_STATE_TOKENS = (
    r"verify_push|read_cap_check|validate_all|complete_check|maturity_scan|sweeps_due|"
    r"profile_clock_check|falsification_scan|walter_route_check|regen_patterns_hot|scorecard|"
    r"corrections_boot_check|ledger_staleness|memory_index_check|memory_citation_census|"
    r"orch_log|argus_scope|reads_check|derived_freshness|closeout_guard|run_tests|"
    r"skew_bar_continuity|vx_daily_gapcheck|boot\.py"
)
# ⚠️ `&&` IS DELIBERATELY EXCLUDED from the shell idiom class. The dominant committed use of `&&`
# beside these tools is the cwd guard `(cd "$(git rev-parse --show-toplevel)" && python3 …)`, where
# the `&&` comes BEFORE the tool and consumes nothing — 5 of the census's 28 raw hits, and every
# one a false positive. Requiring the `&&` to FOLLOW the tool would still fire on the ordinary
# `check && echo ok` display idiom. `||` and `!` carry the real signal: both act ON the verdict.
# ⛔ THE TOOL NAME MUST BE IN COMMAND POSITION, NOT ANYWHERE IN THE STRING. The first cut of this
# recogniser was a single regex `(TOKEN)[^\n;|]*\|\|` and it fired on
#     grep -n "verify_push" AGENTS/DAEDALUS/runs/x.md || true
# where the name is a SEARCH ARGUMENT and the `||` belongs to grep. That is the ordinary shape of
# every search this desk runs, so the guard would have been noise from its first hour
# (`finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction` — the fix is to
# make the recogniser PRECISE, never to relax the severity). So it is a function, not a regex: the
# segment that precedes `||` must INVOKE the tool, which means the token is preceded by an
# interpreter or a path separator and is not sitting inside quotes.
# ⛔ THE TOOL MUST BE THE SEGMENT'S **COMMAND WORD**, not merely path-qualified somewhere in it.
# ⚠️ REWRITTEN 2026-09-14 after an INDEPENDENT ADVERSARIAL REVIEW broke the first cut with 14 of 14
# innocent commands. That cut allowed `[./]` as a command-position marker, so ANY path-qualified
# MENTION counted — defeating, in one character class, the rule stated directly above it in
# capitals. Every one of these fired:
#     ls -la scripts/read_cap_check.py || echo missing
#     [ -f scripts/read_cap_check.py ] || exit 1
#     git show HEAD:scripts/read_cap_check.py > /tmp/old.py || echo fail
#     cp scripts/read_cap_check.py /tmp/ || echo copyfail
# Isolated mechanism: `ls read_cap_check.py || x` did NOT fire, `ls scripts/read_cap_check.py || x`
# DID — the only difference a slash. ⛔ And my own "name as an argument" drill passed ONLY because
# it QUOTED the name; drop the quotes, which is the ordinary form, and it fires.
# `[ -f <tool> ] || exit 1` is a preflight any runner contains and `git show HEAD:<tool>` is
# something THIS SESSION typed — a guard that fires on those is noise inside an hour.
# ⚠️ The inherited 0.00% FP figure did NOT transfer: re-measured over 855 committed `||`/`if !`
# lines it showed 8 hits, but that corpus contains almost no `||`-beside-a-tool-PATH lines and is
# blind to this class by construction — PAT-083, the same caveat the pipeline census carries.
# ⇒ PARSE the segment rather than pattern-match it: strip env assignments, take the COMMAND WORD.
_INTERPRETERS = ("python3", "python", "bash", "sh", "zsh", "exec", "command", "time", "source", ".")
_ENV_ASSIGN = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*=")
_TOOL_RE = re.compile(THREE_STATE_TOKENS, re.I)


def _quoted(seg, pos):
    """True if `pos` falls inside a quoted run in `seg` — a name inside quotes is an ARGUMENT."""
    return seg.count('"', 0, pos) % 2 == 1 or seg.count("'", 0, pos) % 2 == 1


def _command_word_tool(seg):
    """The three-state tool this SEGMENT INVOKES, or None.

    INVOKED means: the tool is the segment's command word (`./verify_push.sh`, `verify_push.sh`),
    or the first non-flag argument of an interpreter (`bash verify_push.sh`, `python3 x/tool.py`).
    A tool appearing anywhere else is an ARGUMENT — `ls`, `cat`, `git show`, `cp`, `[ -f … ]` —
    and is NOT an invocation."""
    raw = seg.strip()
    toks = [t for t in raw.split() if t]
    while toks and _ENV_ASSIGN.match(toks[0]):
        toks.pop(0)
    if not toks:
        return None
    head = toks[0].lstrip("(")
    cands = [head]
    if head in _INTERPRETERS or os.path.basename(head) in _INTERPRETERS:
        for t in toks[1:]:
            if not t.startswith("-"):
                cands.append(t)
                break
    for c in cands:
        if c.startswith(("'", '"')):
            continue                       # a quoted command word is a literal, not an invocation
        pos = raw.find(c)
        if pos >= 0 and _quoted(raw, pos):
            continue
        m = _TOOL_RE.search(c)
        if m:
            return m.group(0)
    return None


def _segments_before(cmd, sep_re):
    """Each segment IMMEDIATELY preceding an occurrence of `sep_re`.

    ⛔ Split on `;`, `&&` and a single `|` — NEVER on a bare `&`: `2>&1` would cut the segment down
    to the string `1`. This file's other recogniser carries that warning from its own v1; I read it
    and wrote the bug anyway, and only a drill on the VERBATIM instance caught it."""
    return [re.split(r";|&&|(?<!\|)\|(?!\|)", part)[-1] for part in re.split(sep_re, cmd)[:-1]]


# The author already knows if they NAME THE STATES or capture the code for later comparison.
# ⛔ `CANNOT` WAS REMOVED FROM THIS ALLOWLIST 2026-09-14 (adversarial review F3, mechanism 2). The
# bare word exempted any caller who MENTIONED "CANNOT-CERTIFY" in an error string while still
# collapsing both states — `tool || echo "CANNOT-CERTIFY: it failed"` went clean. **Naming a state
# in a message is not branching on it**, which is this guard's entire thesis, inverted by its own
# allowlist. Only a construct that TESTS a state earns the exemption.
THREE_STATE_SAFE = re.compile(
    r"-eq\s*2|==\s*2|!=\s*2|returncode\s*==|\brc\s*=\s*\$\?|case\s+\$\?|"
    r"PIPESTATUS|pipefail", re.I)
# A two-valued COMPARISON on `$?` — merges rc 1 and rc 2 into one branch exactly as `||` does.
_TWO_VALUED_RC_TEST = re.compile(
    r"\[\[?\s*\$\?\s*(?:-ne|-gt|!=|>)\s*0|\(\(\s*\$\?\s*\)\)|"
    r"test\s+\$\?\s*(?:-ne|-gt)\s*0")


def diagnose(cmd):
    """(hit, message). Pure; no I/O. The selftest drives THIS, so the recogniser is tested
    independently of the hook plumbing — `finding_test_the_guard_not_just_the_guarded`."""
    if not cmd or not isinstance(cmd, str):
        return False, ""
    if ALREADY_SAFE.search(cmd):
        return False, ""
    m = PIPE_THEN_RC.search(cmd)
    if not m:
        return _diagnose_three_state(cmd)
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


def _diagnose_three_state(cmd):
    """(hit, message) for the rc-2-collapsed-by-a-two-valued-idiom class. Pure; no I/O.

    PERIMETER, STATED SO A CLEAN RUN CANNOT BE OVER-READ: this is a PreToolUse **Bash** hook, so
    it sees shell commands and nothing else. The same collapse written in PYTHON source
    (`if subprocess.run(...).returncode:` merges rc 1 and rc 2 into one branch) is REAL and is NOT
    covered here — it lives in committed files, where a repo lint can reach it, and claiming it
    here would be a guard whose clean line means less than a reader thinks (PAT-074).
    """
    if THREE_STATE_SAFE.search(cmd):
        return False, ""
    tool = None
    # (1) `||` — the verdict-consuming idiom. Only the segment IMMEDIATELY left of it counts.
    for seg in _segments_before(cmd, r"\|\|"):
        tool = _command_word_tool(seg)
        if tool:
            break
    # (2) `if ! <tool>` — negation is two-valued in exactly the same way.
    if not tool:
        m = re.search(r"if\s*!\s*([^\n;]*)", cmd)
        if m:
            tool = _command_word_tool(re.split(r";|&&", m.group(1))[0])
    # (3) `<tool>; [ $? -ne 0 ]` / `(( $? ))` / `test $? -gt 0` — ADDED 2026-09-14 off the same
    # adversarial review (F3). This is the MOST IDIOMATIC way the collapse is written and NEITHER
    # recogniser could see it: recogniser 1 needs a pipe-into-a-pager, recogniser 2 needed `||`.
    # A two-valued COMPARISON on `$?` merges rc 1 and rc 2 exactly as `||` does.
    if not tool and _TWO_VALUED_RC_TEST.search(cmd):
        for seg in re.split(r";|&&|\n", cmd):
            t = _command_word_tool(seg)
            if t:
                tool = t
                break
    if not tool:
        return False, ""
    return True, (
        f"⚠️  pipeline_rc_guard: `{tool}` has a THREE-STATE rc contract (0 clean · 1 FINDINGS ·\n"
        f"   2 CANNOT-CERTIFY) and this call site is TWO-VALUED, so rc 2 will be read as rc 1.\n"
        f"   rc 2 means the check COULD NOT EVALUATE — it is NOT evidence of failure. Treating it\n"
        f"   as failure manufactures an alarm; treating it as success certifies an unchecked run.\n"
        f"   MEASURED INSTANCE (2026-09-12): `bash verify_push.sh \"$s\" >/dev/null 2>&1 || echo NOT\n"
        f"   ON ORIGIN` reported 32 of 32 commits NOT ON ORIGIN. All 32 were on origin — every one\n"
        f"   was an rc 2 from the tool's own documented 60-minute window.\n"
        f"   FIX — name the states instead of testing truthiness:\n"
        f"       {tool} ...; rc=$?\n"
        f"       case $rc in 0) ok ;; 1) echo REAL FINDING ;; 2) echo CANNOT-CERTIFY ;; esac\n"
        f"   (Writing `rc 0/1/2` in a docstring does not make a caller three-valued. Only a call\n"
        f"    site that names the states is — the 2026-09-12 instance was typed by the author of\n"
        f"    the very contract it collapsed.)\n"
        f"   command: {cmd[:180]}\n"
        f"   ⚠️ WARNING ONLY — nothing is blocked; re-run it however you like.\n"
    )


# ── THE SUITE ASSERTS ITS OWN SIZE (2026-09-14) ───────────────────────────────────────────────
# WHY: a pass line that prints `n_ok / <count of what ran>` is SELF-REPORTING, not asserting.
# Delete a check and the suite prints a smaller number and still exits 0 — an unreachable or
# deleted test is indistinguishable from a passing one in the only output anyone reads (PAT-172).
# MEASURED on this file before the fix: deleting one check took it from 71/71 to 70/70, rc 0.
# ⚠️ I MINTED PAT-172 AND HANDED THIS REMEDY TO RED WHILE ALL THREE OF MY OWN SUITES HAD THE GAP.
# ⛔ AND RED'S ADOPTION OF IT REPRODUCED THE CLASS: it incremented an expected-count in a second
# place, which drifted from the verdict, and the suite printed a FAIL line and ALL PASS together.
# So: EXPECTED is a CONSTANT compared against the count derived from the SAME if/else that sets
# the verdict, and the mismatch is appended to the SAME failure list that drives rc. One number,
# one verdict, no second accumulator to drift. Falsify it by deleting a check, never by trusting it.
EXPECTED_DRILLS = 53


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

        # ── THREE-STATE COLLAPSE (2026-09-14, DOCKET L355) ───────────────────────────────────
        # CAPABLE cases. The first is the REAL INSTANCE VERBATIM, not a paraphrase of it — the
        # same discipline that caught this file's own v1 failing on the two cases it was written
        # from. A recogniser tested against a tidied-up version of the bug is untested.
        ('bash verify_push.sh "$s" >/dev/null 2>&1 || { f=$((f+1)); echo "  NOT ON ORIGIN: $s"; }',
         True, "CAPABLE — the 2026-09-12 instance VERBATIM: 32/32 false alarms from rc 2"),
        ('python3 scripts/read_cap_check.py --agent BROCK || echo "read cap FAILED"', True,
         "CAPABLE — || on a tool whose rc 2 means CANNOT-EVALUATE, not failure"),
        ('if ! python3 scripts/validate_all.py; then echo "suite failed"; fi', True,
         "CAPABLE — `if !` is two-valued; rc 2 is reported as a suite failure"),
        ('python3 scripts/ledger_staleness.py DAEDALUS || exit 1', True,
         "CAPABLE — the most dangerous form: rc 2 aborts a closeout as though work had failed"),
        # ⛔ OUT OF PERIMETER, PINNED AS SUCH. The identical collapse in PYTHON source is real,
        # but this is a PreToolUse **Bash** hook and never sees Python source. My first draft
        # asserted want=True here and the drill caught it — a guard that claims a lane it cannot
        # see is `finding_guard_correctness_and_wiring_are_independent` in its dormant form.
        ('if subprocess.run([sys.executable, "scripts/complete_check.py"]).returncode:', False,
         "OUT OF PERIMETER — a Bash hook cannot see Python source; a repo lint owns that lane"),

        # CLEAN cases. Each is a real idiom from THIS repo, and the first three are the exact
        # shapes the 2026-09-14 census turned up and I classified as false positives — pinned
        # here so that classification is a test, not an assertion in a run record.
        ('(cd "$(git rev-parse --show-toplevel)" && .venv/bin/python3 AGENTS/CARL/scripts/boot.py)',
         False, "CLEAN — the CWD GUARD: `&&` PRECEDES the tool and consumes no verdict (CARL:7.0)"),
        ('(cd "$(git rev-parse --show-toplevel)" && .venv/bin/python3 AGENTS/LIQUID/scripts/boot.py)',
         False, "CLEAN — same cwd-guard shape at a second desk (LIQUID:1b)"),
        ('grep -n "verify_push" AGENTS/DAEDALUS/runs/x.md || true', False,
         "CLEAN — `||` on GREP, not on the three-state tool; the name only appears as an argument"),
        ('bash AGENTS/DAEDALUS/scripts/verify_push.sh "$s"; rc=$?; case $rc in 0) ;; 1) echo NO ;; 2) echo CANNOT ;; esac',
         False, "CLEAN — the FIX: the call site names all three states"),
        ('python3 scripts/read_cap_check.py --agent PROME; if [ $? -eq 2 ]; then echo CANNOT; fi',
         False, "CLEAN — `-eq 2` tested explicitly, so the author is three-valued"),
        # ⚠️ I originally wrote this leg as want=False with a note saying it must fire — a leg
        # that contradicted itself. The drill failed and that is how I found it. want=True.
        ('python3 scripts/validate_all.py || echo done', True,
         "CAPABLE — validate_all is three-state; a bare `||` reads its rc 2 as a finding"),
        ('make build || echo "build failed"', False,
         "CLEAN — an ordinary two-valued command; firing here would kill the guard's credibility"),
        ('rm -f /tmp/x || true', False, "CLEAN — the commonest shell idiom there is"),

        # ── F2 REGRESSION SET — the 14 innocent commands an INDEPENDENT ADVERSARIAL REVIEWER used
        # to break recogniser 2's first cut (2026-09-14). Every one fired then; every one must be
        # silent now. They are kept VERBATIM as the reviewer wrote them: a counterexample rewritten
        # in the author's own idiom stops being the reviewer's test.
        # ⛔ The mechanism was `[./]` in the command-position regex — ANY path-qualified mention
        # counted. My own "name as an argument" drill above passed ONLY because it quoted.
        ('ls -la scripts/read_cap_check.py || echo missing', False, "F2 — `ls` is the command word"),
        ('cat scripts/validate_all.py || echo nope', False, "F2 — `cat`"),
        ('wc -l scripts/read_cap_check.py || true', False, "F2 — `wc`"),
        ('test -f scripts/validate_all.py || echo absent', False, "F2 — `test -f`"),
        ('[ -f scripts/read_cap_check.py ] || exit 1', False, "F2 — a preflight any runner contains"),
        ('git show HEAD:scripts/read_cap_check.py > /tmp/old.py || echo fail', False,
         "F2 — and THIS SESSION typed exactly this to fetch the pre-fix code"),
        ('git log --oneline -- scripts/validate_all.py || true', False, "F2 — `git log`"),
        ('cp scripts/read_cap_check.py /tmp/ || echo copyfail', False, "F2 — `cp`"),
        ('rm -f /tmp/read_cap_check.py || true', False, "F2 — `rm`"),
        ('diff scripts/validate_all.py /tmp/validate_all.py || echo differs', False, "F2 — `diff`"),
        ('head -20 scripts/ledger_staleness.py || true', False, "F2 — `head`"),
        ('if ! [ -f scripts/read_cap_check.py ]; then echo missing; fi', False, "F2 — `if ! [ -f`"),
        ('if ! grep -q foo scripts/validate_all.py; then echo no; fi', False, "F2 — `if ! grep`"),
        ('mkdir -p out && cp scripts/orch_log.py out/ || echo nope', False, "F2 — `cp` after `&&`"),
        # …and the UNQUOTED form of my own argument drill, which is the ordinary way it is typed.
        ('grep -n verify_push AGENTS/DAEDALUS/runs/x.md || true', False,
         "F2 — the drill above passed only because it QUOTED; unquoted must stay silent too"),

        # ── F3 COVERAGE SET — genuine collapses recogniser 2's first cut MISSED. The `$?`
        # two-valued COMPARISON is the most idiomatic form of this defect in the language and
        # neither recogniser could see it.
        ('python3 scripts/read_cap_check.py --fleet; if [ $? -ne 0 ]; then echo BAD; fi', True,
         "F3 — `[ $? -ne 0 ]` merges rc 1 and rc 2"),
        ('python3 scripts/validate_all.py; if (( $? )); then echo bad; fi', True,
         "F3 — arithmetic truthiness on $?"),
        ('python3 scripts/read_cap_check.py --fleet > /dev/null; test $? -gt 0 && echo bad', True,
         "F3 — `test $? -gt 0`"),
        ('python3 scripts/validate_all.py || echo "CANNOT-CERTIFY: it failed"', True,
         "F3 — MENTIONING a state is not BRANCHING on it; the bare-CANNOT allowlist exempted this"),
        # …and the correct forms must still be exempt.
        ('python3 scripts/read_cap_check.py --fleet; if [ $? -eq 2 ]; then echo CANNOT; fi', False,
         "CLEAN — `-eq 2` names the state; that is the whole fix"),
        ('python3 scripts/validate_all.py; rc=$?; case $rc in 0|1|2) ;; esac', False,
         "CLEAN — captured and cased"),
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
    if total != EXPECTED_DRILLS:
        fails.append(f"SUITE SIZE CHANGED: {total} drill(s) ran, EXPECTED_DRILLS says "
                     f"{EXPECTED_DRILLS}. A deleted drill is invisible in a self-reported count "
                     f"(PAT-172) — update EXPECTED_DRILLS in the same edit if deliberate.")
        print(f"  ❌ {fails[-1]}")
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
