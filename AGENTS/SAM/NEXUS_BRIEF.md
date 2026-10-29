# SAM — NEXUS Brief

**As of:** 2026-10-29T11:56:23+00:00 (07:56 ET), Will-directed catch-up boot on BOJ meeting day 1. **STATUS commit `72b3a5168`** (Amendment 11). Folded after the final owner-state commit; market observations keep their own source dates.

## VIEW

**Japan is not the source of current stress, and the BOJ is expected to hold tonight while calling 2% reached.** No fresh Japan-led carry unwind. v1.7 retired-to-LOW, no successor frame, no entry. Last Will-confirmed FLAT is June 29, not a fresh broker reconciliation.

**Two live stress tests, no yen-funding signature:**
- **10/22 Asia selloff** (Nikkei about −3%, AI/chip-led): USD/JPY −0.91% on a 1.66-yen completed-session range. A modest haven bid, below the fast-move bar, and fully retraced by 10/28 (157.832).
- **10/26 Brazil shock:** the yen *weakened* (+0.45%).
- CFTC speculators are net **LONG** yen (+69,878, 10/20), so the visible short-yen pool behind August 2024 is gone. Offshore FX-swap funding is unmeasured, so this is "not observed", not "cleared".

**BOJ:** October priced out. Totan 10/29 11:15 JST (SAM-reviewed): **October 2%, December 82%**, cumulative 1.94 hikes by April. Press (Reuters 10/20 and 10/26, Kyodo, Nikkei; REPORTED) expects a hold at 1.25%, with the Outlook judging underlying inflation at or near 2%. That is a **hawkish hold** pointing at December; Takata is likely to dissent for a hike. No named official framed October as live. SAM-33: October purchases matched schedule on date and size; falsifier un-fired.

**Insurers (H2 plans, REPORTED, not executed flows):** super-long buying is mostly coupon swaps, not net new money. Open foreign bonds are trimmed at Dai-ichi, Meiji Yasuda, Sumitomo, Fukoku and Taiju, flat at Asahi, and **flat to up at Nippon Life**. **No insurer stated a UST-sale plan.** Year-end USD/JPY 155–162. September's executed sector dispositions (−¥288.6B) still stand; Channel 1's reactivation test is not met.

**US read-through, conditional:** an orderly Japanese reallocation away from open foreign bonds slightly reduces buying support. It establishes no active UST selling. JGB yields eased (30Y 4.028 → 3.941, MOF 10/19 → 10/28) while the US 10Y sat near 5%, so this window shows no Japan-led long-end push. FOMC 10/28 held with two hike dissents. SOFR ran 5bp over IORB on 10/27 (LIQUID's read). Mechanism matrix → THESIS § US TRANSMISSION.

## CALIBRATION

**35 validated rows; 2 OPEN: SAM-33 (72%), SAM-42 (25%).** No marks, terms or statuses changed. SAM-42 was registered below a 36% market on 9/29; the market has since fallen to 2%, so a FALSE tonight is the expected outcome and earns only a modest calibration credit. A TRUE at 25% would be a calibrated miss, not a broken thesis. SAM-31 FALSE travels with its three qualifications (STATUS).

Process note: three tool defects closed with tests written first, each failing on the old code: the MOF one-week bar now evaluates every new week, the L546 float ties are fixed, and TSE Dec-31 is in the countdown. One SAM process error: a duplicated sweep agent wrote the same report. It was caught and re-sourced before commit (auto-memory `finding_missing_output_is_not_a_dead_agent`).

## CROSS-DOMAIN

**SENDING (10/29, committed packets; consumption unverified):** WALTER: CPI and Brazil-carry replies (no yen-funded unwind signature). DAEDALUS: WQ-508 lines verified. MIDAS: no better official-flow series than TIC; pointers to H.4.1 custody (LIQUID's) and MOF reserves. HAWK: Japan LNG/coal inventory-days UNMEASURED by SAM; September customs flows only.

**WAITING-FOR:** the BOJ statement PDF (SAM-42 grade); Tokyo October CPI; November purchase dates; MOF intervention total (Sep-29→Oct-28); MOF October investor-type (insurer sector, ~Nov-10); Q2 insurer disclosures (late November: sales vs maturities, US asset and tenor, hedges, yen conversion). An offshore basis instrument is still absent.

## NEXT DECISION POINT

No Will ruling needed. **Tonight ~23:00 ET: SAM grades SAM-42 on `k261030a.pdf` only.** The read that matters for peers is the Outlook's 2% judgment and the guidance wording for December. A hike tonight would be a genuine surprise against 2% pricing and is the scenario to watch for a fast yen move.

## FORWARD CATALYSTS

| When | What |
|---|---|
| Oct-30 08:30 JST (Oct-29 19:30 ET) | Tokyo October CPI, 2025 base |
| **Oct-30 ~noon JST (Oct-29 ~23:00 ET)** | BOJ decision + Outlook; SAM-42 boundary Oct-31 23:59 JST |
| Oct-30 17:00 JST | BOJ November purchase dates (SAM-33) |
| ~Oct-30 (estimate) | MOF intervention total Sep-29→Oct-28 |
| Nov-3 | Japan holiday |
| Nov-5 | September MPM minutes; 10Y auction |
| Nov-10 | 30Y auction (frozen bars); Summary of Opinions; US CPI |
| ~Nov-9 / ~Nov-13 | MOF quarterly / FRBNY Q3 FX report (estimates) |

[STATUS](STATUS.md) · [Sweep](research/outputs/2026-10-29_sweep/NEWS_SWEEP.md) · [Insurer H2 plans](insurers/TRACKER.md). Schema owner NEXUS (`AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` §4.1). Commits are local until Will's closeout safe-push; neither local nor remote persistence certifies recipient consumption.
