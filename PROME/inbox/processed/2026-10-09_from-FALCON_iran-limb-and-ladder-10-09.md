# FALCON → PROME — Iran limb 10/09 graded against the ladder: nothing fires; Iraq correction applied; inbox drained

**From:** FALCON (spawned by prome-75, Tier 1, on Will's word at 10:24 ET) · **Written:** 2026-10-09 ~10:4x ET (from `date`) · **Runtime:** Claude Code · **Model:** Opus (`claude-opus-5-5`), desktop
**Full report:** `AGENTS/FALCON/reports/2026-10-09_iran-limb-and-ladder.md` · **Commits:** `4d06ed3a0` (work) · `c43bcd519` (NEXUS brief) · this memo

## Verdict

Nothing fires. **B 1 / C 14 / D 85 HELD.** No consequent is met, so I routed nothing.

## Production rung D 85→92: ARMED, NOT FIRED

**Registered consequent, verbatim (EXIT §2a):** "Moves | **D 85 → 92; C 14 → 7; B stays 1** (floor, disclosed). One move; cannot fire again"

| Item | Grade |
|---|---|
| KKIA, 10/08 (GACA-confirmed: 3 Saudi citizens killed incl. a Saudia pilot; airport facilities and a parked Saudia jet hit) | **KKIA is an airport, not a crude production facility. OUT.** |
| Houthi order to staff at ALL Saudi oil facilities (-020) | **A threat. No facility named, no hit.** No oil-site strike found for 10/08–10/09 |
| UKMTO 160-26 (10/09 10:00Z, ~13 nm W of Al Jazirah Al Hamra in Ras Al Khaimah; position INFERRED, inside the Gulf) | **Hull: OUT** |
| IRGC "NV Sunshine" claim | **CLAIM-ONLY.** No registry match. Not merged with 160-26 (position and identity don't match; a link is possible). **Hull: OUT** |
| Fujairah tanker fire | **Cause not established, no UKMTO number. Hull: OUT** |

## GATE-FALCON-001 event override: NOT TRIGGERED

**Override, verbatim:** "review IMMEDIATELY on any Bab-theater ENFORCEMENT event — an interdiction, a toll actually levied, a transit restriction executed, or a hull attacked in the zone"

- **None of the five items is a Bab-theater enforcement event.** All are in the Gulf, Hormuz, the Gulf of Oman or on Saudi land.
- No Red Sea or Bab incident was found for 10/08–10/09.
- Leg 2 was not re-graded. The gate review is due 10/14.

## 7-day review

No event override applies to it, so I did not grade it early. Formal review is due **10/14**. The downgrade triggers stay unmet: hulls were struck 10/06–10/09, and there is no dated framework.

## Other results

- **Casualty ratchet:** I added the KKIA deaths as CAS-024. The RATE-STEP reads 7 killed vs 12 in the prior window, **so it is NOT LIT**. The ratchet stays YELLOW.
- **Losses** stay at 3.

## L619 (CATO WP22): Iraq correction applied

- My reading of Iraq's VLCC as a "bypass" is **withdrawn**: the ship sails THROUGH Hormuz.
- I added a dated correction line to `reports/2026-10-07_gate001-review-and-inbox-drain.md` (on the row and in a closing note), plus a correction row in `board_log` (KB-263).
- Receipt COR-20261008-18 is APPLIED.
- No grade was affected. Leg 2 is not re-graded before 10/14.

## Drain

- **Consumed 13/13:** 10 from WALTER, 3 from DAEDALUS. All logged in `board_log` and moved to `processed/` with `consume:FALCON`. Census now 0 · 0 · 0.
- **Correction receipts:** four written in the WQ-399 form. The corrections check PASSes.
- **DAEDALUS asks:**
  - Charter step 9 is FIXED (C4).
  - These are DEFERRED to 10/14 as proposals through PROME: the leg-2 vintage rule, the gate-letter clarifications, the FAL-06 search floor and ceiling, and the VX IRAN-02 band instrument. Each is a change to a letter or a band column, and today's task forbade threshold moves.

## Skipped (with reasons)

- **WARRISK re-pull:** all rows are stale. It was outside this task's scope and is carried to the next session.
- **Khurais FIRMS re-pull:** outside scope. The standing watch is carried.
- **baghdad / kharg scripts:** demoted / impeached.
- **STRIKES sweep:** no facility-class candidate.

## For PROME

- No GATES flip is needed; the gate stays LIVE with review_by 10/14.
- There is no WILL_QUEUE item.
- `orphan_check` lists `PROME/state/ORCH_LOG.tsv` as [not yours]. It is PROME's; I did not touch it.

## COMPLETION — FALCON — 2026-10-09
STATUS: ✅ DONE
CHANGED: AGENTS/FALCON/{STATUS,SCRATCH,NEXUS_BRIEF,CLAUDE}.md, board_log.tsv, workbook/KB.tsv (KB-258..265), domain/vessel-incidents/VESSELS.tsv (VI-0056..0059), domain/casualties/CASUALTIES.tsv (CAS-024), registry/corrections_receipts.tsv, reports/2026-10-07_gate001-review-and-inbox-drain.md (correction note), reports/2026-10-09_iran-limb-and-ladder.md (new), scripts/*_state.json, 13 inbox items → processed/
RESULT: Nothing fires; B1/C14/D85 HELD. The D 85→92 production rung is NOT FIRED: KKIA (10/08, 3 killed, GACA) is an airport, OUT; the Houthi all-oil-facilities order is a threat with no hit; 160-26, NV Sunshine (claim-only, not merged) and the Fujairah fire are hulls, OUT. The GATE-FALCON-001 event override is NOT TRIGGERED (none is Bab). The 7-day review is not graded early; due 10/14. The Iraq "bypass" reading is withdrawn (it sails THROUGH Hormuz; COR-20261008-18 APPLIED). 13/13 inbox items consumed; 4 receipts; corrections check PASS.
GAPS: The UKMTO PDFs return 403, so 160-26's position is INFERRED from a place name and its hull is unnamed. NV Sunshine has no registry match. WARRISK and Khurais FIRMS were not re-pulled (outside this task's scope; carried). DAEDALUS's letter and band asks are deferred to 10/14 because today's task forbade threshold moves.
WILL_NEEDS: None.
FOLLOW-UP: 10/14 FALCON wake for the GATE-FALCON-001 review, the 7-day scenario review and the DAEDALUS deferral proposals. Standing watch: a counting source confirming a strike on a Saudi PRODUCTION-class site ⇒ D 85→92 the same hour.
