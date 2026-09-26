# WQ-299 — PROME SELF-CORRECTION REFORM: a process ceiling · a repair-episode read cap · a rule freeze with named consolidations · over-cap means triage owed — RULED 2026-09-26 13:07 ET (§ RULING below; encoded `ac8158d84`) — was PROPOSAL, REVISION 1 (2026-09-25 21:04 ET, `prome-1d`)

**Provenance.** Drafted 2026-09-25 20:32 ET on Will's word *"Okay how would we begin to address some of these?"* (20:28), after a self-analysis session he opened at 18:23. **Revision 1 at 2026-09-25 21:04 ET on CATO's review `AGENTS/CATO/runs/2026-09-25_2050_wq299-session-direction.md` (WR1–WR6), taken as the plan read under the WQ-178 read budget** — every WR is a meaning-changing flag and each is fixed below; the un-fixed remainder is in § Declared residue. Draft 0 is `git show 121805063:` this path. **No second revision** (read budget; the two-correction stop binds this file).

**Why one record.** The 9/11–9/25 record shows one shape. PROME produced 1,004 commits on its own paths (711 fleet-prefixed vs WALTER's 201), 212 with a fix/reader/residue subject (21%); orchestration touches ran 48 and 45 on 9/24–9/25 against a normal 10–15, ~127 of the fortnight's rows were readers or ARGUS; DOCKET grew 335→500 lines with 28 OVERDUE (20 PROME-owned, seven annotated *"not started — every PROME build slot since 9/19 went to repairs"*); WILL_QUEUE stood at 21 OPEN over the 20 cap with 7 rows aged past 9/19. **The slips that REACHED WILL this week were all in the Will-facing compression step** (F1's direction inverted · "$1.8B" shipped as ".8B" · APO "no ruling" against an 8/13 HOLD · a tenfold misquote of WALTER's figure); the fortnight's other slips were mechanical and caught before commit. That is a claim about the slips that reached the operator, not an exhaustive failure taxonomy (CATO WR1). The numbers are PROME's own `git log` / `awk` / ORCH_LOG measurements, unreplicated; the commands are in `memory/2026-09-25.md`.

**Every ruling is forward-only. Decline any one and the others stand. Nothing here authorizes a build; T1 and T2 are HELD.**

## R1 — A CEILING of one process change per session; due domain and position obligations first
**Rule letter:** *Process instrumentation — a tool, gate, check, hook, registry, acceptance file or charter text whose PURPOSE is PROME's own process, whichever docket row names it — is a CEILING of ONE change per session, never a quota: zero is the default whenever a DUE domain or position obligation exists (a DOCKET row at or past its date, a GATES row at its review_by, an item on Will's list, the book), and those are worked first. Reader rounds on the process change count inside it. The closeout report names the change and its purpose class (PROCESS / DOMAIN). An overrun is disclosed as a skipped control; disclosure is not authorization.* Unit = the session; the DAY unit is the 30-day-review candidate if session resets prove to restore the allowance (WR2).
**Encode:** one bullet in `PROME/CLAUDE.md` § Session Process Controls, paired in the same edit with consolidation **C1** below so the section's bullet count does not rise (R3) · `PROME/CLOSEOUT.md` report line.
**Acceptance tests:** (1) ordinary — one process change + two domain rows reads clean; (2) overlap — a desk's fetcher PROME repairs for a due DESK row is DOMAIN by purpose; a `prome_gate` leg is PROCESS whoever asked; (3) wrong owner — N/A, the perimeter rule already excludes other desks' tools; (4) missing — a session with no closeout report (crash) reads UNKNOWN, never PASS; (5) concurrent — the unit is the session, declared; the record shows 2–5 PROME legs a day, which is why the day unit is the review candidate.

## R2 — THREE independent reads per REPAIR EPISODE, ending in an explicit disposition
**Rule letter:** *A REPAIR EPISODE — the fix to one named defect in one artifact, from its first edit to its disposition — gets at most THREE independent reads in total; parallel readers each count, and the WQ-178 plan/result discipline is unchanged inside it. The third read ENDS the episode with an explicit disposition in the four WQ-229 states — IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED · STILL UNRESOLVED — and STILL UNRESOLVED stays that: the last unreviewed fix is never promoted. Where the unresolved defect is load-bearing, the change is withdrawn or disabled rather than shipped. Will may authorize a specific further read by name. Missing read history is UNKNOWN: a baseline read of the acceptance file precedes any further round; a count is never invented. A later, materially different defect in the same artifact is a new episode.* (Replaces draft 0's lifetime-per-artifact cap and its "absent counter reads as three" — WR3.)
**Encode:** one sentence appended to the existing WQ-178 bullet (no new bullet) · `PROME/tools/tests/README.md` acceptance-file template gains a `reads:` line.
**Acceptance tests:** (1) ordinary — the third read ends the episode with a disposition; (2) overlap — one read spanning two artifacts counts one read in each episode; (3) wrong owner — a read Will commissions counts toward the episode; his override is by name, never implied; (4) missing — no `reads:` line ⇒ UNKNOWN ⇒ baseline first; (5) concurrent — two parallel readers are two reads.

## R3 — Freeze to 2026-10-25 + a NAMED consolidation proposal; nothing retired for being un-automatable
**Rule letter:** *No new bullet enters `PROME/CLAUDE.md` § Session Process Controls before 2026-10-25 except paired with a named consolidation in the same edit. Spine audit #15 carries a CONSOLIDATION PROPOSAL, not an edit: each candidate names what merges into what, what history moves to which pointer, and shows the duty, authority and discoverable pointer that survive; Will approves candidates by name. Automability is never a criterion — a judgment-dependent duty (ownership, uncertainty, independent review) stays. The charter target under 20,000 B (`measure.py`; 24,081 B today) measures the pass; it licenses nothing.* (Replaces draft 0's "a rule that cannot be mechanized leaves the charter" — WR4.)
**Candidates, named now, for the audit's proposal:** **C1** Measurement + No-live-measurements-in-prose → one bullet (both are `measure.py` rules) · **C2** the header's Updated/Prior stamp chain (≈4 KB of history) → the `git log -p` pointer BOOT.md and STATUS.md already use · **C3** the Spawn-default block's 8/22 narrative and quoted rulings → the `PROME/AUTONOMY.md` change-log pointer, with the tier table and the four triage rules retained verbatim · **C4** Two-correction stop + Read budget + Late-session rule → one "correction budget" bullet, every clause retained (they already cite each other). Each keeps every duty; each is approved or declined by name.
**Acceptance tests:** (1) ordinary — an edit adding a bullet with no named consolidation is refused by the result reader; (2) overlap — an amendment to an existing bullet is not a new bullet, and growth inside a bullet is measured by `measure.py` at the audit (WR4's concealment point); (3) wrong owner — root `CLAUDE.md` is Will-gated and outside this freeze; (4) missing — no `measure.py` receipt at the audit means the pass did not run; (5) concurrent — N/A, one charter, one writer.

## R4 — Over-cap or aged rows mean a triage table is OWED, before any registration
**Rule letter:** *When the boot gate reads the WILL_QUEUE actionable count over 20, or any row 7 days past its needed-by, the boot report carries a triage table BEFORE any new row is registered that session: each aged row — or, with no aged rows, the oldest actionable rows down to the cap — marked ALREADY RULED · OWNER WORK FIRST (→ `⛔ waits: <owner>` + a DOCKET row) · EXPLICIT WILL DECISION, each with its completion condition and receipt; queue counts shown after ACTUAL dispositions, never conditionally. A new registration in that session names the triage in its Notes — that is the bounded route for an urgent new decision. The closeout report shows the triage discharged or SKIPPED.* (WR5's tail: over-cap with no aged rows, and the urgent-decision route, both covered.)
**Encode:** `PROME/WILL_QUEUE.md`'s own rules block (the W2 soft-cap rule gains it) — NOT a charter bullet · the `prome_gate` boot advisory text names the obligation (no code change for v1).
**Acceptance tests:** (1) ordinary — 21 rows ⇒ a triage table in the boot report; (2) overlap — a row both aged and `⛔ waits` is already outside the cap and is listed with its blocker, not re-decided; (3) wrong owner — a row whose actor is a desk is triaged OUT to DOCKET, not decided; (4) missing — an undated row uses the existing 21-day tripwire; (5) concurrent — two PROME legs in one day triage once; the second reads the first's table.

## Tools — HELD (WR1); neither is authorized by a ruling on R1–R4
- **T1 `brief_check.py` — HELD, rescoped.** If later commissioned: an ADVISORY LINT of named mechanical errors only — shell-expanded figures (".8B", "/bin/bash"), figures with no source anchor, a gate sentence lacking its GATES row's consequent token — that discloses what it cannot establish (entity, date, basis, negation, antecedent; CATO's counterexample: a source line "Desk A: 5%; Desk B: 2%" anchors the false "Desk B: 5%") and whose acceptance includes valid derived values and false claims with matching numbers or tokens. Never called verification; never blocking. It earns its slot after R1's first review, not tonight. Meanwhile the outgoing brief is checked by hand against owner sources — done for this session's own briefs (§ Corrections).
- **T2 stamp helper + heredoc guard — HELD.** An "only sanctioned source" clause and a new guard change conduct and enforcement; they need their own ask when commissioned.

## Triage of the seven aged rows — REVISED after verification at the owner artifacts (R4 applied first)
| WQ | Category | Disposition tonight | Completion / receipt |
|---|---|---|---|
| 187 | ALREADY RULED (approved 9/10 by Deck tap); Will's hands owed (read-only PAT + Telegram bot token) | UNCHANGED — its own row, its own token, its own completion | closes when the first digest posts |
| 204 | EXPLICIT WILL DECISION — a second, write-scoped token + an iOS Shortcut; a different capability from 187 | UNCHANGED — may share 187's sitting; never merged (WR5) | yes ⇒ closes on the first phone signal; decline ⇒ WALTER retires the sweep + boot step in one commit; 187's approval untouched either way |
| 255 | EXPLICIT WILL DECISION | one word: SPECIAL as written (WR6: decidable apart from WQ-299) | DAEDALUS FLEET_MAP/directory/checklist · PROME ROSTER move |
| 251 | EXPLICIT WILL DECISION — and its BASIS IS OVERTAKEN: the 8/26→9/11 tiers (BB 150 · B 273 · CCC 1,076) are superseded by 9/24 (BB 164 · B 286 · CCC 1,112 [FRED]) and LIQUID read the 9/24 move as broad, rates-led, beta-leaning, PROVISIONAL until a retrace | UNCHANGED tonight; rec WITHDRAW as overtaken — the stand-down (WQ-192) and the X1 DON'T-SIZE gate hold independently, nothing is adopted; re-registers on LIQUID's Mon 9/28 grade if a re-basing question survives it | Will: withdraw / keep |
| 246 | EXPLICIT WILL DECISION (the count) — NOT moot at the 004 expiry: `AGENTS/BOND/thesis/THESIS.md:147` still reads *"sustained"* with no session count, and it blocks the matrix vector-1 upgrade as well as the add-gate (WR5) | RE-DATED 2026-10-01 to BOND's quarterly-refresh sitting (DOCKET L410 carries two more BOND decisions that day) | Will picks 3 sessions / 5 consecutive, framed "what would have been written on 9/1"; ruling authorizes no add (7/16 NO-ADD, WQ-280) |
| 242 | OWNER WORK FIRST — VX-CRU-06 (WQ-222) is the OBSERVATIONAL vector and is encoded on total return (STATUS:78, VX.tsv:7); the remaining deliverable is a FRESH ratio-form PREDICTION succeeding CRU-05 (FAILED 9/13; the id CRU-06 belongs to a CONFIRMED NCLH row) — WR5 | `⛔ waits: CRUISE` · DOCKET L502 (2026-10-02): CRUISE drafts the letter to the WQ-162 six elements | returns as one approve when the letter exists |
| 241 | OWNER WORK FIRST — CORAL proposes the re-fire condition and a LEVEL guard beside the spacing one, prospective; drafting is not adoption; the live 🟠 grade unchanged | `⛔ waits: CORAL` · DOCKET L501 (2026-10-02) | returns as one approve when the letter exists |

**Actual queue arithmetic (this file, after tonight's registrar acts):** OPEN rows 22 with WQ-299 · actionable 20 (241 and 242 blocked) · 19 on WQ-255's word · 18 if 251 is withdrawn · 187 / 204 / 246 stay dated. Draft 0's "21 → 17" was conditional and is retracted.

## Sequence — how we begin
1. **This sitting (done at revision): ** the triage's registrar acts (241, 242 → waits; 246 re-dated; two DOCKET rows) · this record · the 299 row. **No build; no charter edit before the word.** Then domain work.
2. **Monday 9/28, domain first:** OTTO L469 and LIQUID L492 wakes · the paid-data list with prices (L498, by 10/02) · WQ-274's five gaps wait on broker views only Will can open (surfaced, not asked).
3. **On the word:** R1 + C1 in one charter edit (plan read = this record; one result read) · R2's sentence · R4 into the queue's rules block · the R3 freeze line.
4. **Spine audit #15 (due ~9/27):** the consolidation PROPOSAL (C1–C4, by name); the queue's "Last reconciled" line (≈7 KB of history in one header line; the file is 150,327 B) is a C2-class candidate for the same pass.
5. **30-day review (2026-10-25):** re-measure the same ten numbers; R1's unit decided on the measurement.

## Corrections PROME owes from this session's own briefs (checked by hand against owner sources, WR1)
- The 18:5x ATTENTION line said the book was un-reconciled since the 9/16 capture. The mirror carries the 9/16 standing quantities (WQ-272, 9/21); the open gap is WQ-274's transaction reconcile + current-book check, which needs Will's broker views. DOCKET L448 ("still untranscribed", OVERDUE 9/22) is overtaken by that work — itself an instance of pattern 1.
- The 18:5x brief said "every consequential slip landed in the compression step"; narrowed above to the slips that reached Will.
- Draft 0's triage claimed authority F2 does not grant (251), mislabelled an encode (242), and declared a scoring dependency moot (246); all corrected at the artifacts above.

## Declared residue (after CATO's read; un-fixed on purpose, each named)
- WR2 daily-cap candidate — deferred to the 30-day review with the measurement, not adopted blind.
- WR1 "check the actual outgoing brief" — done by hand for this session (§ Corrections); no tool exists and none is built.
- The fortnight statistics are unreplicated PROME measurements; commands recorded for re-run.
- WR4 "R1/R4 add bullets while the freeze demands replacement" — resolved by construction (R1 pairs with C1; R4 leaves the charter), not by a further rule.

## What PROME did without a ruling and what waits
*(Superseded by § RULING, 2026-09-26 13:07 ET — kept as the revision's own closing line.)* DONE at revision: this record · WQ-299 row revised · WQ-241 → `⛔ waits: CORAL` + DOCKET L501 · WQ-242 → `⛔ waits: CRUISE` + DOCKET L502 · WQ-246 re-dated 2026-10-01 · SCRATCH pending-Will view regenerated. **Nothing built, no charter edited, no packet sent.** WAITS ON WILL, each its own word: R1–R4 as revised (*"approve 299"* covers the four) · WQ-255 · WQ-251 withdraw/keep · 187 and 204 (a day for the tokens; 204 may be declined) · WQ-246 at 10/01.

---

## RULING — Will, 2026-09-26 13:07 ET, delivered as pasted text in the `prome-1d` session (verbatim; the record renamed PROPOSAL → RULED at 13:12 ET)
> Approve WQ-299 R1–R4 with the clarifications below. Implement the approved package as one bounded change, complete the existing required review, and close it out. No further proposal rewrite.
>
> Due domain and position obligations that you can advance take priority. Record externally blocked work clearly; it should neither disappear nor create a permanent prohibition on necessary maintenance.
>
> Approve C1, preserving both measurement duties and their pointers. C2–C4 remain proposals for the scheduled audit. Keep the brief checker and stamp/heredoc tools held.
>
> Approve WQ-255: SPECIAL, with CATO remaining my manual adviser and independent reviewer, without automatic launch or signal-routing eligibility.
>
> Withdraw WQ-251 as overtaken, preserving the historical finding and existing restrictions. This adopts no replacement market interpretation. Return with a fresh question only if LIQUID's scheduled work establishes a decision I actually need to make.
>
> Keep WQ-187's existing approval and WQ-204's separate disposition intact; I'll address the hands-on setup separately.
>
> The objective is to improve useful research delivery and reduce the supervision the system requires from me. Once this implementation is complete, return to the existing domain priorities. Recommend the most valuable next action, explain what it will resolve, and identify anything we should defer or stop to make room.
>
> Your closeout should briefly state what was implemented, what remains materially unresolved, and what useful work comes next. Correct the queue-count label at its next update; it does not need another review round.

## Implementation receipt (one bounded change, 2026-09-26 13:12 ET)
- `PROME/CLAUDE.md` — ONE edit: header stamp · § Session Process Controls header gains the R3 freeze sentence · C1: the Measurement and No-live-measurements bullets merged into one (both duties, both pointers, the error numbers and the root-rule-#4 lesson all kept) · the R2 repair-episode sentence appended to the Read-budget (WQ-178) bullet, with the externally-blocked clause · the R1 process-ceiling bullet added at the section's end, paired with C1 (bullet count 12 before, 12 after). Size per `measure.py` at write: see the commit body, never this line.
- `PROME/WILL_QUEUE.md` — rule W2 (soft cap) gains R4; rows 299 · 255 · 251 OPEN → RECENTLY DONE with Will's words verbatim; 187/204 untouched. Counts in the gate's labels: open 19 · blocked 2 (241 CORAL, 242 CRUISE) · actionable 17.
- `PROME/tools/tests/README.md` — the `reads:` line contract (R2's carrier).
- `PROME/ROSTER.md` — CATO moved CLASSIFICATION PENDING → SPECIAL with Will's ruling verbatim (WQ-255); DAEDALUS packet for FLEET_MAP / directory / checklist.
- Tools T1 and T2: HELD, per the ruling. Nothing built.
- Result read: coldreader (opus) on `PROME/CLAUDE.md`, ledger `scratchpad/wq299result.md`, ORCH_LOG row at spawn — this is read 2 of this episode (read 1 = CATO's plan read); the episode's `reads:` count is carried here, not in an acceptance file, because the change is canon text, not a tool.

## Result read and declared residue (read 2 of the episode; coldreader, opus; ledger `scratchpad/wq299result.md`, 30 claims: 20 ✅ · 10 ⚠️ · 0 ❌; verdict *"yes, a cold reader would act correctly"*)
No ❌ ⇒ no further edit of `PROME/CLAUDE.md` this session (canon-drafts rule; read budget: ❌ only). Every ⚠️, un-fixed on purpose, each named:
1. **Line-2 stamp written to the minute (13:12 ET)** — against the merged bullet's own letter (a to-the-minute stamp of itself); the file's convention is the x-masked minute. Fix at the spine-audit #15 C2 pass, which rewrites the header stamp chain anyway.
2. The stamp omits that R4 was encoded in `PROME/WILL_QUEUE.md`, not this file — the record and the WQ row say so; the header does not.
3. The stamp omits the second appended sentence (externally blocked repairs).
4. **A clause is printed twice in the merged Measurement bullet** — the connector phrase repeats the first words of the merged duty ("a document never carries a figure a reader can recompute from an instrument"). A concatenation blemish, no meaning change; fix with C1's wording at the C2 pass.
5. A repair outside the Pre-edit-cold-read class gets its third read without the "only when a ❌ fix changed a rule's meaning" condition — the cap conditions the old third-read rule rather than contradicting it (reader's own reading); left as written, R2 is the ceiling.
6. Whether a NEW repair episode reopens a file "closed for the session" — unstated; intent: a new episode is a new session's work, never the same sitting's.
7. Where a canon-text edit carries its `reads:` count (no acceptance file exists) — this record carries it (read 1 = CATO's plan read, read 2 = this result read).
8. "One change" in the process ceiling has no unit — intent: one process instrument or one canon amendment, whichever docket row names it; the 10/25 review is where a unit is measured, not asserted.
9. "The 2026-10-25 review" is defined only here (§ Sequence step 5): re-measure the ten basis numbers; decide R1's unit.
10. "Charter" = `PROME/CLAUDE.md`; spine audit #15 has no fixed date — STATUS's *Last spine audit* 9/20 + 7d ⇒ due from 9/27.

Episode disposition (R2, WQ-229 states): **IMPLEMENTED · TESTED (checks: willq_view/docket_view/claim_check/read_cap all rc 0) · INDEPENDENTLY VERIFIED-WITH-RESIDUE (one blind result read, 0 ❌) · STILL UNRESOLVED: items 1 and 4 above (wording; next touch).**

**Count correction (13:28 ET 9/26, byte-flow reader 2):** the basis line's *"28 OVERDUE (20 PROME-owned)"* is 21 PROME-owned by a row-by-row count of the 9/25 view; PROME's tally miscounted by one. The fortnight statistics remain PROME's own unreplicated measurements, as declared.


**Ledger-path check (13:38 ET 9/26, ARGUS ❌7):** ARGUS reported `scratchpad/wq299result.md` absent; PROME checked the path at closeout — the file exists in the session scratchpad (`wc -c` receipt in the closeout commit body). The scratchpad is session-local and not in the repo, so the durable evidence is the short-form report quoted in § Result read above and the ORCH_LOG row; the path is a pointer for this session only.