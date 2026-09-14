# A SPAWN IS NOT COMPLETE UNTIL ITS DESK HAS CLOSED OUT — RULED 2026-09-14

**Will, verbatim, 2026-09-14 15:36 ET:** *"Yes. I havent gotten around to spawing Brent yet. Thats on me.
Just get those agents closed out and we need to make that process standard"*

**Prompted by:** Will's own question at 15:31 — *"All the agents we had spawned such as DAEDALUS TERRY RED
etc. Did they go through a close out function? Meaning did they have a chance to document or save any of
the new data they encountered to their files?"*

**Status:** RULED. Practice adopted the same sitting (one rule transplanted into `PROME/CLAUDE.md`).
Mechanization NOT built in this sitting — registered as a dated DOCKET row with its acceptance conditions
written FIRST, per the WQ-229 repair-completion discipline. **Queue row: WQ-249.**

---

## 1. The measurement that prompted it

PROME orchestrated five desks on 2026-09-14 (`PROME/state/ORCH_LOG.tsv`, rows dated 2026-09-14):
TERRY · BOND · DAEDALUS · RED · HOMER. At 15:31 ET, measured at the artifacts:

| Desk | Own-authored commits | STATUS.md written | Last own commit | Ran a closeout |
|---|---|---|---|---|
| RED | 18 | 13:34 | 14:07 | ✅ twice — S45 closeout 13:12 (inbox drained, handoff written) + addendum 13:23 |
| HOMER | 3 | 14:19 | 14:19 | 🟡 closeout nudge ran 14:19 |
| TERRY | 8 | 14:12 | 15:27 | ❌ none |
| BOND | 7 | 14:10 | 14:10 | ❌ none |
| DAEDALUS | 14 | 13:27 | 13:36 | ❌ none |

**Zero uncommitted work in any of the five desk directories** (`git status --short -- AGENTS/`), so **no
committed work was ever at risk.** All five sessions were still ALIVE in panes at 15:31.

## 2. ⛔ THE FINDING, WHICH IS SHARPER THAN THE DEFECT

PROME's own session-close row in `ORCH_LOG.tsv` — written at 14:4x, before Will asked — reads:

> *"Session close — five desks orchestrated, **all idle with last delivery committed and zero desk-dir
> residue** at 14:4x."*

**PROME performed a check, passed it, and recorded the pass. The check measured the wrong thing.**

⇒ 🔑 **A desk that is idle, with every delivery committed and no directory residue, is INDISTINGUISHABLE
ON DISK from a desk that has closed out.** Both present as a clean tree. The difference exists only in the
live pane — the half the desk noticed and has not yet written down — and **that half has no artifact for
any git-based check to inspect.**

This is `[[finding_a_check_that_only_advises_is_overridden_the_control_is_downstream]]` in a form worth
naming separately: the check did not merely advise and get ignored. **It returned a genuine PASS on a real
property, and the property it measured was not the one at risk.** Compare
`[[finding_instrument_reports_clean_against_the_wrong_reference]]` — clean scan, wrong referent, so there
was no error to notice. Nothing fired because nothing was wrong *with what was inspected*.

⚠️ **Note what the clean reading cost: nothing, yet.** No work was lost today because Will asked before
closing the terminal. **The loss mode is silent and total** — a pane closes, and there is no artifact, no
flag and no absence to detect afterwards, because the record of what was never written down is itself
never written down. `[[finding_partial_record_written_as_final_never_heals]]`, one level up.

## 3. THE RULE (adopted)

> **A spawn is not complete when the desk delivers. It is complete when the desk has been ASKED to close
> out, and PROME has the answer or has recorded that the desk went dark before the ask.**

**PROME owns this, not the desk.** An idle desk cannot know the terminal is about to close; only the
orchestrator knows the session is ending. A desk going dark unasked is an orchestration failure, not a
desk failure.

### 3a. ⛔ The check is on the ASK, never on detecting a closeout

**PROME must not classify another desk's commits as "a closeout" by reading subject text.** RED's subject
said *"closeout"*; HOMER's said *"closeout nudge"*; a desk that closed out properly and described it
better would read as a miss. That is exactly
`[[finding_status_token_membership_test_desupervises_improved_rows]]` — a guard scoped by status TOKEN
drops the rows someone described better.

**The fact PROME can establish is whether it ASKED.** That is a fact about PROME's own action, needs no
inference about another desk, and fails in the safe direction: a desk that has already closed out receives
one unnecessary message (cheap); a desk that dies unasked loses its session (expensive, silent).

### 3b. The four states, never merged

Every orchestrated desk resolves to exactly one, and the closeout report prints which:

1. **ASKED → receipt received** — the desk closed out and returned its push receipt.
2. **ASKED → still working** — doorbell sent, desk busy. Named, so Will knows a pane is still live.
3. **ALREADY CLOSED OUT** — still enumerated, still asked or explicitly skipped with the reason. **Never
   silently dropped from the count**, or the denominator rots.
4. **WENT DARK BEFORE THE ASK** — named explicitly in the closeout report. **This is the state the whole
   rule exists to make visible**, and it is the one with no artifact of its own.

### 3c. Scope — spawns, not every doorbell

The obligation attaches to a desk **PROME spawned or re-pinged in this session** (an `ORCH_LOG` row dated
today with a TOUCH-class `touch` token). ⛔ **It does NOT attach to a session Will launched himself** —
WALTER on 2026-09-14 was Will's own interactive session, not PROME's spawn, and PROME claiming it would be
`[[finding_grading_a_disposition_on_a_book_you_do_not_own]]`.

## 4. ACCEPTANCE CONDITIONS FOR THE MECHANIZATION — written BEFORE any code (WQ-229)

These are the properties the repair must hold, in the defect's own terms. **They are the test list.**

1. **Enumeration comes from a RECORD, never from PROME's memory of the session.** The population is
   `ORCH_LOG.tsv` rows dated today with a TOUCH-class token. A session that remembers four of its five
   spawns passes its own recollection and fails this condition.
2. **A desk still live at PROME's closeout is doorbelled BEFORE PROME's closeout commit** — not after,
   and not "noted for next time".
3. **All four states of §3b are reported separately and never merged into a pass/fail.**
4. **A desk that went dark before the ask is NAMED**, so the un-externalized loss is visible rather than
   silent.
5. **No classification of another desk's commits as "closeout" by subject text** (§3a).
6. **It works when Will ends the session mid-flight** — the actual case today. A control that only runs on
   an orderly shutdown does not cover the shutdown that loses work.
7. **A missing `ORCH_LOG` row for a known spawn FAILS CLOSED as UNKNOWN**, never reports zero. The
   ABSENT-ROW CLAUSE already says absence proves nothing; the check must inherit that, not contradict it.

### 4a. Neighbours CONSIDERED (WQ-229's five — consider, do not perform)

- **ordinary** — a session that spawned nothing: reports zero desks, no output, no noise. Must not emit a
  reassuring green line either; silence is correct.
- **overlap** — a desk both PROME-spawned AND independently launched by Will in the same day. **This is
  live, not hypothetical: WALTER 2026-09-14.** The check must key on the `ORCH_LOG` row, not on desk name
  or on directory activity.
- **wrong owner** — a desk PROME merely doorbelled under messaging rule 6 without spawning it. Out of
  scope per §3c; must not be swept in.
- **missing information** — covered by condition 7.
- **concurrent activity** — a desk BUSY at PROME's closeout cannot close out on demand. That is state 2,
  not state 1, and merging them would report a closeout that never happened.

## 5. What was NOT done in this sitting, and why

⛔ **The gate check was not built.** Reasons, stated rather than implied:

1. **Late-session rule** (`PROME/CLAUDE.md` § Session Process Controls): once the two-correction stop has
   tripped anywhere in a session, prefer closeout, documentation or read-only work over new broad edits.
   It tripped repeatedly on 2026-09-14.
2. `prome_gate.py` carries **live unrepaired residue of its own** (DOCKET L366 ①–⑤, and L364's finding
   that its four BLOCK checks are *"NOT a class and are not to be treated as one"*). Adding a sixth check
   to that file tonight, at the end of a long correction chain, is the shape of edit that produced L366.
3. **WQ-229: prefer promoting or repairing an EXISTING control to adding a new one.** The enumeration
   surface (`ORCH_LOG`) already exists and is already complete — today's five rows were all present and
   correct. **The missing piece is an OBLIGATION attached to a record that is already being written**, not
   a new instrument. That is a smaller repair than it first looks, and it deserves to be scoped as one.

**Registered as DOCKET L378 (2026-09-16)** so it cannot decay into an oversight.

## 6. Declared residue

- **The word "closed out" is not defined in measurable terms anywhere in canon**, and this record
  deliberately does not define it — §3a argues PROME should not be in the business of grading it. ⚠️ But
  that leaves an open question this record does not answer: **what does a desk owe when it says "closed
  out"?** Root `CLAUDE.md` session-end steps 1–3 are the nearest thing to an answer and are not cited as
  one here. Left open, not fixed.
- **State 4 (went dark before the ask) has no falsifier.** If a pane dies and nothing was written, the
  check records that PROME failed to ask in time — but **cannot establish whether anything was lost.**
  The report must not imply it can. `[[finding_scope_negative_needs_the_counterparty_standard]]`.
- **The five-desk population today is n=1 as a sample of sessions.** Two of five had closed out, three had
  not. Nothing here should be read as a rate.
