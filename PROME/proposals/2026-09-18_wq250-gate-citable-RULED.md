# WQ-250 — RULED 2026-09-17 (Will, Decision Deck tap, APPROVE, no note; consumed by `prome-89` 18:37 ET) — a spec letter carrying `production UNVERIFIED` or `realisation UNKNOWN` is REGISTRABLE BUT NOT GATE-CITABLE until the attestation lands

**Will's word:** APPROVE on PROME's rec = DAEDALUS's rec (L348 ruling record `AGENTS/DAEDALUS/runs/2026-09-14_L348_SL4_SL5e_RULE_CONFLICT_RULED.md` §4: *"YES, and applied to BOTH clauses symmetrically, as a separate amendment … it should probably live wherever gate eligibility is owned rather than here"*). Tap capture verbatim = `PROME/WILL_QUEUE.md` WQ-250 Notes (RECENTLY DONE at the next reconcile).
**Drafted 2026-09-18 10:5x ET by `prome-0e`** under `PROME/CLAUDE.md` § Session Process Controls *"Canon drafts live in the ruling record, transplanted once"*: this record carries the exact clauses; ONE blind PLAN read here; then each canon file takes ONE insertion edit; the RESULT read may force at most one further edit; residue is declared here.
**Three insertion points, three owners:** ① + ② `AGENTS/DAEDALUS/BLUEPRINTS/SPEC_LETTER_STANDARD.md` — **DAEDALUS encodes** (its file; the tap says *"before DAEDALUS encodes"*; PROME packets this record). ③ `PROME/GATES_README.md` — **PROME encodes** (gate eligibility is PROME's surface, which is where DAEDALUS said the rule should live). **$0 at stake:** DAEDALUS verified 2026-09-14 that zero letters on `PROME/GATES.tsv` carry either token; ③ names the query and it is re-run at encode with the count cited.

## The rule, in one sentence
A spec letter whose SL-4(b) production attestation reads `production UNVERIFIED — <query>`, or whose SL-5(e) realisation reads `realisation UNKNOWN`, may be REGISTERED, reviewed and graded for the record, but no `PROME/GATES.tsv` row may FIRE, ARM or carry a capital consequence on its basis until the named attestation has landed at the letter.

## ① SPEC_LETTER_STANDARD.md — SL-4: REPLACE the paragraph beginning `⚠️ **OPEN, NOT RULED HERE —` (line 31 at crc32 3037955298) with
> ⛔ **GATE-CITABILITY — RULED (WQ-250, Will 2026-09-17; record `PROME/proposals/2026-09-18_wq250-gate-citable-RULED.md`): a letter carrying `production UNVERIFIED — <query>` is REGISTRABLE BUT NOT GATE-CITABLE.** It may be registered, reviewed and graded for the record; a `PROME/GATES.tsv` row may not fire, arm or carry a capital consequence on its basis until the named query has been run and the print recorded in this letter. The same rule binds SL-5(e)'s `realisation UNKNOWN` — symmetric by construction, neither clause is the softer one. Gate-side enforcement = `PROME/GATES_README.md` GATE-CITABILITY RULE; this standard governs authoring and asks only that the letter carry the unmade query verbatim, so the attestation that lifts the bar is unambiguous. Verified 2026-09-14: zero such letters sat on `PROME/GATES.tsv`.

## ② SPEC_LETTER_STANDARD.md — SL-5(e): APPEND one sentence directly after `⛔ **\`0 of N\` IS A COMPLETE DECLARATION** …`
> ⛔ **`realisation UNKNOWN` is REGISTRABLE BUT NOT GATE-CITABLE (WQ-250 — the same rule as SL-4(b), record `PROME/proposals/2026-09-18_wq250-gate-citable-RULED.md`): a gate row resting on it may not fire, arm or carry a capital consequence until the realisation count is pulled and written here.**

## ③ PROME/GATES_README.md — NEW `#` rule line directly after the ENVELOPE COLUMNS line (line 30 at crc32 2730882643)
> # GATE-CITABILITY RULE (WQ-250, Will 2026-09-17 Decision Deck APPROVE; record PROME/proposals/2026-09-18_wq250-gate-citable-RULED.md): a row whose condition, consumed_by or definition_surface rests on a spec letter carrying `production UNVERIFIED — <query>` (SPEC_LETTER_STANDARD SL-4(b)) or `realisation UNKNOWN` (SL-5(e)) REGISTERS with the lead token `LIVE / NOT ARMED — attestation pending: <the letter's query verbatim>` and may not FIRE, ARM or carry a capital consequence until the owner records the attestation at the letter and PROME re-cuts the state cell. Registration is encouraged — the row is how a pending attestation gets a review_by; firing on it is forbidden. Both tokens on one letter ⇒ both attestations lift it. Check at every touch: `grep -nE 'production UNVERIFIED|realisation UNKNOWN' PROME/GATES.tsv` — cite the count (0 at the 2026-09-14 verification; re-run at encode).

## Acceptance conditions (WQ-229) — what the PLAN read checks the clauses against
- **C1 Symmetric:** both tokens carry the identical consequence; neither clause reads as the softer one.
- **C2 Authoring untouched:** nothing above changes what a desk must WRITE to register (SL-4(b)'s and SL-5(e)'s declaration duties stand); only what a GATES row may DO on that basis changes.
- **C3 The lift is mechanical:** the attestation that lifts the bar is the letter's own named query, run and recorded — no judgement call, no new token.
- **C4 Zero live rows move:** ③'s grep returns 0 on `PROME/GATES.tsv` at encode, stated with the count.
- **C5 Three insertion points, no fourth restatement:** root `CLAUDE.md`, `STATE_VOCABULARY.md` and `FORGE/PREDICTION_DISCIPLINE.md` untouched — `LIVE / NOT ARMED —` is an existing lead-token form (`GATE-LIQ-079`).
- **C6 Paths:** every path in the clauses is repo-root-relative (SPEC_LETTER_STANDARD's own convention).

## Neighbours considered (five categories)
**ordinary** — a reachable feed: nothing changes, the letter attests and the row fires as before. **overlap** — a letter carrying BOTH tokens: one bar, lifted only when both attestations land (③ says so). **wrong owner** — PROME never edits SPEC_LETTER_STANDARD (DAEDALUS encodes ① ② from this record by packet); DAEDALUS never edits GATES_README (③ is PROME's). **missing information** — a letter that names no query cannot be lifted: SL-4(b) already forbids *"leaving the question unasked"*; this record adds no rule there. **concurrent activity** — N/A: three files, three single-writer owners, sequenced by packet.

## PLAN read (blind, Opus coldreader — filled at delivery)
_pending_

## Encode receipts (filled at encode)
① ② DAEDALUS — _pending: packet to `AGENTS/DAEDALUS/inbox/` after the PLAN read_ · ③ PROME — _pending_

## Declared residue
_none yet_
