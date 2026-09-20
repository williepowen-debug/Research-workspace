# PROPOSAL — extend the closeout consumer-check to retired-prose claims, completed checkboxes, and falsified standing negations

**Status:** PROPOSED (drafted in the record per canon-draft discipline; NOT enacted — needs a cold read, then Will's ruling before any edit to root `CLAUDE.md` closeout or `PROME/CLOSEOUT.md`).
**Author:** PROME · **Date:** 2026-09-20 · **Origin:** n=4 in ~24h (CRUISE + SAM); CRUISE wrote it into its closeout receipt as owed and handed the "closeout step?" call to PROME/Will. CATO review `AGENTS/CATO/runs/2026-09-20_1010_prome-punchlist-assessment.md` (059dbad8e) reframed it as an EXTENSION, not a new mechanism.

---

## The defect class (evidence)

Four times in ~24h a correction or a new registration reached the **deep** artifact and left a **summary/consulted** surface stating the old thing as live:

1. **CRUISE funding-gap retirement** — the model was retired in KB-CRU-075/076 and the source doc, but the STATUS VX-CRU-05 vector row, KB-CRU-075 Notes, and three WATCHLIST spots still read *"unverified ~$1.3B gap / or an equity raise"* / *"highest-value UNREAD document"*. PROME's sweep found 4; CRUISE found a 5th (a completed checkbox still unticked).
2. **CRUISE registering CRU-09** immediately **falsified two standing *"no prediction registered"* lines** on its own STATUS — caught by trimming, not by any check.
3. **SAM** — the brief still said *"TWO REMAIN UNADJUDICATED"* (a superseded live instruction) and MEMORY led with the withdrawn *"+2% blended"* rationale.
4. Same class, same day, both desks.

Common shape: **a ruling governs the next write, not the existing state** (`finding_a_ruling_governs_the_next_write_not_the_existing_state`), and **hand-fixing the named rows is not fixing the class** (`finding_hand_fixing_named_rows_is_not_fixing_the_class`). Vigilance did not fix it four times running.

## What is ALREADY covered (so we extend, not duplicate — CATO point 3)

Root `CLAUDE.md` closeout **1c** + `scripts/consumer_check.py` already require a consumer sweep when a session supersedes a **figure** (threshold, flip level, split, band), including a `--self` scan of the author's own dir. That control is tuned for **numeric** values and cross-agent routing. It does **not** catch: retired **prose** claims, completed **checkboxes/tasks**, or standing **negations** a new registration falsifies — and it says nothing about verifying the replacement's **meaning**.

## The proposed extension (narrow)

At closeout, when a session **retires/supersedes a claim**, **completes a task or checkbox**, or **registers a new prediction/commitment** (three triggers — the task-completion one is explicit, CATO: an ordinary completion leaves an "UNREAD"/open checkbox stale without retiring any claim), it sweeps **ALL its named consulted surfaces — including files it did NOT touch this session** (STATUS, TRADE, KB/FLOW/VX summary rows, WATCHLIST, the operator brief, MEMORY) for, and resolves:
- (a) the retired claim still stated as **current** (not merely mentioned — a labelled retraction is fine);
- (b) **completed** tasks/checkboxes still shown open;
- (c) standing **negations** now false (*"no prediction registered"*, *"N remain unadjudicated"*).
- (d) **and confirms the replacement reads correctly in meaning** — not just that the old string is gone.

⚠️ **Scope is the NAMED-SURFACE LIST, never this session's commit set (CATO).** The stale WATCHLIST spots were in a file CRUISE did not touch when it retired the gap in KB — a commit-set scope would exclude precisely the summaries this targets.

Mechanism: **extend the existing consumer-check step / `consumer_check.py`**, NOT a new standalone gate. ⚑ **Capability audit FIRST (CATO):** `consumer_check.py` already supports literal-text matching in one mode — establish exactly what it cannot yet do (own-surface prose scan · checkbox state · standing-negation detection) BEFORE requiring any new code (WQ-229: promote/repair the existing control before adding one). ⚠️ **Grep is discovery, not proof (CATO):** a hit may be a correct retraction; an absence does not prove the surviving prose is right. The instrument surfaces candidates; the session verifies meaning.

## Acceptance conditions (written first, in the defect's own terms — WQ-229)

1. After a retirement, **no own summary surface a reader travels still asserts the retired claim as current** (a labelled retraction or a correctly-superseded row passes; a bare live-shaped restatement fails).
2. After a registration, **no standing negation on an own surface contradicts the new state.**
3. **Completed tasks/checkboxes reflect completion.**
4. The check **flags the meaning question** (replacement verified), and does **not** treat a zero-grep as proof of correctness.
5. It is an **extension of the existing consumer-check** (capability audit first), adds no parallel gate, and covers **all named surfaces including UNTOUCHED files** — the sweep is NOT scoped to this session's commit set (CATO).
6. **False-positive tolerance:** a correctly-labelled retraction/retirement must NOT be flagged as live (else the check becomes noise and gets overridden — `finding_a_check_that_only_advises_is_overridden_the_control_is_downstream`).
7. **Task-completion is a trigger in its own right:** completing a task must fire the sweep even when no claim was retired, or a stale checkbox survives (the CCL-Q3-date and NCLH-10-Q misses).

## Five neighbours (WQ-229 — considered, N/A justified)

- **Ordinary:** a plain retirement (CRUISE gap). Covered — the core case.
- **Overlap:** a token that is retired in one sense but live in another (retired *"$1.3B gap"* vs live *"$1.3B revolver capacity"*). **This is why grep≠proof** — a blind grep-and-delete would nuke the live one; the meaning-check (d) is the guard. Load-bearing, not N/A.
- **Wrong owner:** the stale surface is **another agent's** file (PROME could only packet CRUISE, not edit). Scope of THIS control = the authoring session's **own** surfaces; cross-agent stale stays with the existing `consumer_check` → packet flow. Justified boundary.
- **Missing information:** a session may not know all its own summary surfaces → the extension must carry (or point at) a **per-desk enumerated surface list**, or it silently under-scans.
- **Concurrent activity:** another session edits the surface mid-sweep → handled by the existing shared-tree commit discipline. ⚠️ The sweep binds the authoring session's **named-surface list**, NOT its commit set — a stale summary usually sits in a file the session did not touch (CATO); scoping to the commit set is the specific hole this proposal must not reproduce.

## Completion state (WQ-229 — not to be merged)

This proposal is **drafted only** — not IMPLEMENTED, not TESTED, not VERIFIED. Next steps, in order: (1) cold read of this record; (2) Will's ruling on whether it extends closeout canon; (3) if ruled, extend `consumer_check.py` + the closeout step with a test that fails against pre-fix behaviour on the four evidence cases above; (4) independent reader devises its own counterexample before it is called fixed (CONSEQUENTIAL — it touches a shared closeout control). Prefer promoting/repairing the existing control over any new one.

## Addendum 2026-09-20 PM (TERRY doorbell, verified in the tool source) — the self-mode safety risk + its safeguard

⛔ **The load-bearing risk for a SELF-sweep, verified at `scripts/consumer_check.py` L697-708 (the LINE-CLASS DEMOTION block), not asserted:** a 🔴 cannot tell a stale COPY from a FROZEN THRESHOLD from a DATED HISTORY ROW. On BROCK's first `--from-ledger` run via PROME, **123 candidates and BOTH certified 🔴 were NOT stale** — (a) `DOCKET.tsv:183` a deliberately FROZEN kill line (packeting/re-basing it to the current value is the ratchet that DESTROYS a falsifier); (b) a `MARKET_DATA` row DATED 2026-07-27 carrying the then-current value (a refresh CORRUPTS the series). **0-for-2 on the highest-confidence tier, and in BOTH cases ACTING ON THE FLAG causes the damage.**

🔑 **Why cross-agent mode is safe and self-mode is not:** cross-agent, the remedy is a packet to the owner and the owner pushes back. **In self-sweep mode the flagged party, the dispositioning party, and the party with the cheapest wrong remedy are ALL the same session, at closeout, under time pressure** — and the cheapest way to clear a 🔴 on your own frozen threshold is to edit the threshold, i.e. the exact defect. `[[finding_a_flag_resolved_in_the_wrong_direction_launders_the_defect]]`; TERRY's own `ledger_sweep` CHECK-I rationale in reverse (a guard whose cheapest remedy is a bad action buys nothing).

✅ **Scope correction (TERRY, `[[finding_impeachment_must_be_scoped_to_the_claim_not_the_source]]`):** the self-audit 0-record/4-instrument scoreboard impeaches JUDGEMENT-dependent self-audit, NOT a literal-string match — a superseded-string probe needs no judgement and does not depend on the author knowing what they meant, so the author-blindness mechanism does not reach it. The scoreboard BOUNDS this proposal's scope (literal-string subclass; misses paraphrases/titles); it is NOT an objection to it.

**Safeguard — ACCEPTANCE CONDITIONS 8-10 (uses the tool's OWN distinctions; the ask is only that self-mode not bypass them):**
8. Self-mode KEEPS every demotion class (DEMOTE-NEVER-SUPPRESS; the frozen-threshold and dated-capture line-classes stay demoted to 🟠 with their reason printed).
9. Self-mode NEVER auto-acts on a 🔴 — no silent clear, no auto-edit.
10. The frozen-threshold and dated-capture classes must be dispositioned **in writing with the reason**, never silently cleared. A `git mv`/edit that clears a 🔴 on the author's own frozen threshold is the failure this exists to prevent.

## Open, not part of this proposal
CATO flags the CRUISE funding model's **cash-flow timing AND minimum-reserve** limitations as still unresolved (the deposits-ahead-of-sailing / trailing-OCF-understates-stress point, documented in KB-CRU-076 but not modelled, and the minimum operating-cash reserve the breakeven ignores). CRUISE domain items, carried — noted here only so they are not lost.

## Cold-read result (2026-09-20 ~11:00 ET) — declared residue per WQ-178

Bounded blind cold read (coldreader, Opus): **11/17 claims ✅ · 6 ⚠️ · 0 ❌.** Verdict: **ready for the operator's ruling** — mechanism sound, honestly scoped; "grep is discovery, not proof" is correctly locked into condition 4 + item (d) + the overlap-neighbour (no condition treats a zero-grep as proof); all 5 pointers resolve; both `consumer_check.py` capability claims verify. Ledger: `scratchpad/coldread_retired-claim-sweep.md`.

No ❌ ⇒ no result-edit beyond this declaration + one one-word slug fix (WQ-178: fix ❌ only, declare ⚠️, no cascade). The 6 ⚠️ are declared, NOT fixed; the two near-blocking ones resolve at **implementation** (if adopted), not before the ruling — Will rules on the mechanism, not the build:

1. **(near-blocking) "The four evidence cases" is not cleanly enumerable.** The evidence section says *n=4 / four times* but enumerates **three distinct cases** — (i) CRUISE funding-gap retirement + stale checkbox, (ii) CRU-09 registration falsifying two standing negations, (iii) SAM supersede + negation — plus CRUISE's self-found 5th checkbox. The implementer test-target in "Completion state" step 3 must be re-stated as these enumerated cases on adoption.
2. **(near-blocking) The per-desk enumerated surface list the scope rule rides on does not yet exist / is unlocated** (Missing-information neighbour, L50). Building or locating it is implementation step 1.
3. Condition 7's referents (CCL-Q3-date, NCLH-10-Q checkboxes) live in the CRUISE evidence upstream, not restated in the evidence section here.
4. "Capability audit first" names WHAT to probe (own-surface prose scan · checkbox state · standing-negation detection), not HOW.
5. Condition 2 phrases negation-checking against "registration," but SAM's negation was falsified by adjudication/task-completion — covered mechanically by the all-triggers sweep, phrased narrowly.
6. Truncated finding-slug — fixed inline (condition 6).
