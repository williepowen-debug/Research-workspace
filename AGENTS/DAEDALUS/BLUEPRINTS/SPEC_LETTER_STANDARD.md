# SPEC LETTER STANDARD — authoring rules for registered spec letters (fleet build standard)

**Owner:** DAEDALUS · **Ruled:** Will 2026-08-30, verbatim *"Approve WQ-136 as revised: close both rows 72 and 73 as T6 items; preserve the three lessons as named, owner-assigned specification rules in the proposed DAEDALUS home and register the implementation work."* · **Record:** `PROME/proposals/2026-08-30_wq136-t6-spec-rules-RULED.md`; grade that produced them `PROME/proposals/2026-08-30_t6-hard-close-GRADED.md` · **Encoded:** 2026-09-01 (DAEDALUS); SL-5 added 2026-09-03 · **DOCKET checkpoint:** 2026-09-08 · **Kin:** `STRICT_TEXT.md` rule 7 (thresholds: LEVEL + INSTRUMENT + WINDOW + REVISION POLICY — this file is the LETTER-level complement); `CHECK_STANDARD.md` governs standing checks, not letters; PAT-115 / PAT-127 (resolver dating, frozen-absolute vs floating-relative drift).

**Scope — STRICT (a wrong reading has a cost):** any FROZEN spec letter registered for grading — forum tests, prediction letters with a trigger, gate definitions, kill memos. **Forward-only:** governs the NEXT write; no retroactive sweep of frozen letters is implied (`finding_a_ruling_governs_the_next_write_not_the_existing_state`); a sweep is a separate Will ruling with its own cost. **T6's frozen text stays unedited** — its grade is recorded by annotation beside it.

## The three rules (each earned by a T6 defect that did not change the verdict and WILL recur)

### SL-1 — A "fresh high" (or "new low") condition names ALL FIVE: series · observation basis · comparison period · strictness · and whether it means a FIXED threshold, a PRIOR MAXIMUM, or BOTH
*Instance:* T6's HOLD/EXTEND leg read *"fresh high >5.28% while odds fall."* Before 2026-08-17 the two readings were coextensive (5.28 sat above the 2026 max 5.27). Then `DGS30` printed 5.31 [8/17] and they split: a 5.29 close is >5.28 but is not a fresh high. **One print created an ambiguity that did not exist that morning.** BOND found it and did not self-rule; BOND+LIQUID settled it CONJUNCTIVE on 8/23.
*The rule:* a fixed level and a prior maximum are the same test only until the series moves. Coextensive-at-registration ≠ equivalent. Write which one, or write BOTH with the conjunction stated.

### SL-2 — An exchange-probability trigger names ALL FIVE: contract · CLOSE-vs-INTRADAY basis · eligible calendar/session set · strictness · missing-observation treatment
*Instance (the load-bearing one):* T6's trigger read *"Sept-hike <25%"* with **no basis at all**. On the close basis the minimum qualifying session close was 0.25 [Fri 8/14] — exactly on a strict `<` line, no fire. On an intraday basis it would have fired (session low 0.23). The close basis was adopted 2026-08-27 (ORACLE KB-ORC-070 + `t6_pin.py`), 13 days after the breach was in the data, as a CHANGE of reference for an unrelated question — and nobody noticed it also decided a two-desk forum test.
*Sub-rules:* **session set** — Kalshi trades weekends; 8/15 (Sat) 0.26 and 8/16 (Sun) 0.25 were `is_session=N`; "touched three straight days" mixed session and calendar closes (PROME and RED, same direction). **Strictness** — `<25%` vs `≤25%` was the entire verdict.

### SL-3 — A graded window distinguishes `eligibility_window` · `lookback_window` · `grading_window`
- `eligibility_window` — every observation capable of FIRING the trigger.
- `lookback_window` — observations needed for POST-trigger comparison.
- `grading_window` — observations the hard close reads.
*Instance (PROME's own):* `t6_pin.py` was built around 8/21–8/28 (sized for a 5-session lookback on an 8/28 fire); the trigger was eligible from 8/10. The minimum over the tool's window (0.31, "+6.0pp above the line") shipped as the grade — clean against the wrong reference; the true minimum was 0.25, zero margin. Caught by a consumer scan, not the grading run. RED's "+6.0pp" was a DIFFERENT referent (current distance), correctly labelled — same number, different referent, looked corroborated.
*Tool twin:* any successor to `t6_pin.py` grades the FULL eligibility window and prints a verdict even when run after the window closes (ORACLE holds the packet; the vocabulary is registered here so the tool and the letter cannot fork).

### SL-4 — The grading source must be able to PRODUCE the registered level (added 2026-09-01, BOND via PROME + WAL's §0 spec-executability rail, its 4th instance at PR#5)
*Instance:* T6's 5.28% was a `^TYX` intraday figure dated to a Sunday; `DGS30` — the named grading series — never printed 5.28. That cost BOND four registrations. WAL's §0 check asks the same question before grading: *can the named instrument physically carry this datum?*
*The rule:* at registration, show that the named series, at the named basis and session set, HAS printed at the registered granularity (or state that it cannot and pick a level it can). A level lifted from a different instrument, a different basis (intraday vs close), or a non-session date is UNPRODUCIBLE and fails registration — it is not a threshold, it is a wish with a number on it. Kin: STRICT_TEXT rule 7 (INSTRUMENT names the ticker that grades it), `finding_registry_names_a_concept_tool_resolves_an_instrument`.

### SL-5 — An inequality against a series published at FIXED PRECISION declares its TIE SET: operator strictness · the series' published precision · the as-published tie convention · a base rate computed on the SAME operator the letter carries · and EXIT legs audited for ties, not only fire legs (added 2026-09-03; CREED + RED, two desks in four hours, PROME-routed)
*Instances:* **CREED-T-01a** `> 12` — August office CMBS DQ printed exactly `12.00` on a series Trepp publishes to 2dp; the unrounded value is 11.995–12.004 and the sign of `value − 12` is unknowable. NOT FIRED held only because a pre-registration frozen a week earlier fixed the as-published convention — without it the tie would have been adjudicated after seeing the number. **RED FT-11** — the registered `≤ −4bp` base rate (5.0% / 3.8%, LR≈34) was computed on the STRICT cut while the letter BOND adopted is NON-STRICT, on which the leg fires 8.5% / 6.2%, LR≈21 — 1.7× more often; **the tie atom at exactly −4bp is 23 of 661 windows = 41% of the fires.** Corrected pre-go-live. RED's other realised tie set sat on FT-10's EXIT leg — a desk auditing only its fire operator logs the row clean.
*The rule:* every `>`/`<`/`≥`/`≤` over a series published at fixed precision has a NON-EMPTY tie set, and it is silent until the day it lands. At registration: (a) name the operator's strictness AND the published precision; (b) declare the tie convention — default: **the as-published value is the grading value; a print exactly on the line satisfies `≤`/`≥` and does NOT satisfy `<`/`>`; no re-derivation of the unrounded value**; (c) compute any base rate on the operator the letter carries — a base rate on the other operator is a different letter's base rate; (d) audit EXIT/retirement legs for ties the same way. Kin: SL-2's strictness sub-rule (this generalises it from exchange probabilities to every fixed-precision series) · `finding_relative_threshold_cannot_be_graded_by_a_one_sided_instrument`. **One-time sweep of already-registered base rates for operator mismatch = a DATED row, never a retroactive re-grade** — carried as a leg of DAEDALUS wiring sweep #2 (~9/14); PROME asked to register the DOCKET row.

## Registration form (what a conforming letter carries, one line each)
| Element | Example |
|---|---|
| Series + basis | `DGS30, daily close, FRED as-published` |
| Comparison period + strictness + fixed/prior-max | `> 5.28 (FIXED) AND > max(2026 YTD closes) (PRIOR-MAX) — BOTH` |
| Exchange trigger (if any) | `Kalshi FED-SEP-HIKE, session CLOSE, is_session=Y only, strict <0.25, missing session = no observation (not 0)` |
| Windows | `eligibility 2026-08-10→08-28 · lookback 5 sessions post-fire · grading = eligibility ∪ lookback` |
| Producibility (SL-4) | `DGS30 daily close has printed to 0.01 since 1977; 5.28 producible` |
| Tie set (SL-5) | `published to 2dp; strict >12.00; a 12.00 print does NOT fire; base rate computed on strict >; exit leg ≥ audited` |
| Revision policy | per `STRICT_TEXT.md` rule 7 |

## Enforcement
- `builds/REGISTRATION_CHECKLIST.md` row 15 (STRICT text at build) gains this file as a cited standard for any spec letter — DAEDALUS checks at registration, the way rule 7 is checked now.
- **Prior-art line (CHECK_STANDARD §13):** searched `PATTERNS_HOT.md` + memory indexes — PAT-115 (resolver dating), PAT-127 (frozen-absolute vs floating comparator), `finding_instrument_reports_clean_against_the_wrong_reference` (SL-3's mechanism), `finding_unqualified_identifier_is_a_defect_waiting_for_a_reader` (SL-2's) — this file is their LETTER-side registration form, not a new pattern.
- First live use = the next spec letter any desk registers; PROVISIONAL until then per the CHECK_STANDARD §8 flow.
