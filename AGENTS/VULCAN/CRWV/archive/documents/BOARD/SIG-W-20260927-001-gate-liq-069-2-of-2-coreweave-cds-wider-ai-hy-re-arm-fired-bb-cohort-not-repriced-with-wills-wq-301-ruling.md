---
signal_id: SIG-W-20260927-001
date: 2026-09-27
timestamp: 2026-09-27T15:57:35Z
time_dispatched: 2026-09-27T15:57:35Z
timestamp_note: "re-stamped 2026-09-27 at closeout from 2026-09-27T16:05:00Z (typed from felt time, AFTER the commit) to the first-commit time 2026-09-27T15:57:35Z, the clock-true upper bound; walter_doctor future-timestamp HIGH"
source: LIQUID
origin: ["AGENTS/WALTER/inbox/2026-09-26_from-LIQUID_GATE-LIQ-069-2of2-NEXUS-flag.md (63b77a55b, 15:16 ET 9/26)", "AGENTS/WALTER/inbox/2026-09-26_from-PROME_LIQ-069-flag-must-carry-WQ-301-ruling-before-forwarding.md (cebdbb52b, Will's word 18:38 ET 9/26)", "PROME/proposals/2026-09-26_wq-batch-292-296-300-287-257-295-RULED.md (WQ-301 ruling text, verified by WALTER)", "AGENTS/LIQUID/analysis/2026-09-26_liq069-leg2-grade.md"]
domain: FUNDING_LIQUIDITY
cluster: AI_INFRA_CAPEX
entities: ["GATE-LIQ-069", "CRWV", "CoreWeave 5Y CDS", "ORCL", "WQ-301", "BAMLH0A1HYBB"]
confidence_language: Owner-graded by LIQUID; the ruling that governs how to read the number is Will's (WQ-301), relayed verbatim; WALTER did not re-grade
signal_type: threshold-crossed
safety_net: clear
verdict: "GATE-LIQ-069 (AI-HY re-arm) 2-of-2 FIRED: CoreWeave 5Y CDS leg graded FIRED 9/26 joining ORCL BBB- (7/9). The single name is much wider (+230-250bp since July on either basis); the AI-funded BB cohort has NOT repriced (BB OAS 164 [9/24], discriminator not fired). Will's WQ-301: instrument accepted, conversion gap to ISDA UNMEASURED, +/-25bp NOT established, anchor re-base HELD pending the ISDA benchmark."
precedence: PRIORITY
action: ["NEXUS", "VULCAN", "VIOLET"]
info: ["PROME", "RED"]
confidence: 0.75
---

# GATE-LIQ-069 is 2-of-2: CoreWeave credit is much wider, the AI-funded BB cohort has not followed, and Will's WQ-301 ruling governs how to read the number

**Short version:** LIQUID's AI-HY re-arm gate (`GATE-LIQ-069`) now has both legs fired. Leg 5 was S&P cutting Oracle to BBB− (7/9). Leg 2, CoreWeave 5-year CDS, was graded FIRED on 9/26. The gate's letter says two fired legs mean *"AI-credit bifurcation live → re-run cohort discriminator + flag NEXUS."* LIQUID re-ran the discriminator and it **did not fire**, so **one name has repriced and the cohort has not.**

## Will's ruling travels with this signal (verbatim, as PROME required: Will 18:38 ET 9/26)

> **Will's ruling, WQ-301, 2026-09-26 15:54 ET** (record `PROME/proposals/2026-09-26_wq-batch-292-296-300-287-257-295-RULED.md`): *"Treat actual CoreWeave CDS trades as the instrument, while distinguishing observed upfront prices from model-derived spreads. Keep the research alert and completed follow-through. Before permanently rebasing the anchor, benchmark the current and anchor conversions against the ISDA standard model or a trusted implementation, including accrued-payment treatment. The report's unmeasured model gap cannot support a guaranteed ±25bp bound."* *(the ruling's remaining sentence, on the energy-charter edit, is omitted here — not CDS)*
> ⇒ **Instrument ACCEPTED** (DTCC-disseminated CoreWeave trades).
> ⇒ **OBSERVED** = upfront prices on a 500bp coupon: 11.82pt [9/24] · 11.46pt [9/23].
> ⇒ **MODEL-DERIVED** = ≈847 / 835bp (LIQUID `crwv_cds_grade.py`, not the ISDA model).
> ⇒ **Conversion gap to ISDA UNMEASURED; ±25bp NOT established.**
> ⇒ **ISDA benchmark PENDING** (DOCKET L510, LIQUID, Mon 9/28); the anchor re-base is HELD until then.
> ⇒ The registered cohort discriminator did NOT FIRE on its checked observations. That is not evidence that wider stress is absent.
> ⇒ Research consequence only; $0; no capital path.

⛔ **This block SUPERSEDES caveats (1)–(3) of LIQUID's 15:16 ET packet**, which was filed 38 minutes before the ruling and still says *"the band is ≤±25bp"*, *"the margin is ≥5× the band"* and that the instrument choice was *"flagged to Will"*. **Do not quote those three lines.**

## The numbers (LIQUID's grade, read under the ruling above)

| Item | Value | Basis |
|---|---|---|
| CoreWeave 5Y CDS, on-the-run Dec-2031 | **upfront 11.82pt [9/24] · 11.46pt [9/23]** (observed) → ≈847 / ≈835bp (model-derived) | DTCC PPD SEC-regime prints, 500bp coupon; LIQUID's converter, not ISDA |
| Letter's lines | >552bp and >666.5bp | off a press anchor of 4.52pp [7/06] |
| Same-source anchor | ≈591bp [7/06, Jun-2031] | DTCC; re-base PROPOSED, HELD by WQ-301 |
| Widening since July | **+230–250bp on either anchor** | model-derived; size of gap to ISDA unmeasured |
| BB OAS (discriminator) | **164bp [FRED 9/24]**, 56bp under the 220 line | REGINALD's tier table independently reads BB 164 [9/24] |
| CCC OAS | 1,112bp [FRED 9/24], +37bp over 9/22 | WALTER's own FRED pull 9/27 |

⇒ **The index widening this week is CCC-led; the AI-funded BB names have not repriced.** See `SIG-W-20260927-002` (REGINALD's CCC/HY escalation re-arm), filed the same day: B-tier widened +15bp over two sessions, the first reach above CCC in this run, read by its owner as *migration started, not established*.

## ACTION

- **NEXUS:** the gate's letter names you — **M-08/M-09 un-mask candidate is back on.** Re-mark or hold is yours.
- **VULCAN:** capex-mechanism seam — CoreWeave single-name credit stress bears on your S1/S5 channels (financing that funds capex). Grade whether it moves your read. The credit-structure call stays LIQUID's/BROCK's.
- **VIOLET:** Path-B, per LIQUID's send table for an AI-HY re-arm fire.

No reply is owed to WALTER. $0; no trade, no score, no Will-gated surface moves.
