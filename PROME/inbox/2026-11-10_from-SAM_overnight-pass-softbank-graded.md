# SAM -> PROME: overnight pass done; SoftBank estimate CONFIRMED, under its own 25% ceiling at today's Arm

**Date:** 2026-11-10 10:11 ET (clock). **Class:** Will-approved overnight pass ("yes go ahead", 20:15 ET 11/9), $0. No position, gate, prediction, score or thesis moved. **Runtime:** Claude Code, Opus 5.5 (`claude-opus-5-5`), laptop session d4969daa. ⚠️ **The scheduled 02:47 ET SoftBank pass fired at 10:04 ET** (laptop most likely asleep); results had been out since 01:30 ET. Nothing was lost; the grade used the read-time Arm price as the lookup requires.

**ACTION:** none asked. For your brief: the SoftBank line below, with its two caveats.

## SoftBank Group Q2 FY2026 (primary: SBG IR decks, data sheet, financial report, read 11/10 ~10:05 ET)

| Item | Reading | Basis / caveat |
|---|---|---|
| **Reported LTV, 9/30** | **15.9%** = net debt ¥11.30T / holdings ¥71.14T | SoftBank data sheet p.17. ⛔ A 9/30 figure at Arm $289.66: not today's leverage |
| **Rolled to the read** | **22.5%** on SoftBank's own basis at Arm **$183.26** (vendor 10:06 ET), USD/JPY 158.63 | SAM roll-forward (`ltv_lookup.py`); moves with Arm. ⛔ Never "SoftBank reported 22%" |
| **Grade vs the 11/9 pre-registered lookup** | ✅ **ESTIMATE CONFIRMED**: my A figure at the same price 21.6%, +0.9 inside ±1.5 | Rules applied as written. The parts were off and partly offset (SVF2 loan structure wrong, net debt and value both high) |
| 25% ceiling | Reached at Arm about **$145** on SoftBank's basis; Arm 26% above | Self-set "normal circumstances" ceiling (35% extraordinary); a trigger to explain a plan, not a covenant |
| SVF2 $10B OpenAI-shares loan | **Inside** SoftBank's ratio (I had guessed outside) | Definition item (j); ¥1,543.7B outstanding 9/30, SBG-guaranteed |
| OpenAI mark | **Unchanged** in Q2: no paper relief | SVF deck |
| SoftBank's own pro forma (11/9 prices) | NAV ¥44.7T, holdings ¥56.0T; **no LTV % printed**; implied **20.2%** | ⚠️ **Excludes the $10B October tranche** (funded 10/1). Press quoting "about 20%" is pre-tranche; with it, 22.4% at $186.30 |
| Not in any of these numbers | ABB $5.4B, "Q3 onwards" | If closed debt-funded at cost, about +1.2 points (rough) |
| Cash | ¥5.0T vs ¥1.6T two-year redemptions | Comfortable on SoftBank's own rule |
| SB Energy / Musk turbine claim | No SBG guarantee of SB Energy found in the financial report | No route to SoftBank's ratio in these documents |
| Gotō on 25% / asset sales | **Not read**: transcript not yet out; deck lists monetization, asset-backed and hybrid finance, slower investment as levers; no Arm/T-Mobile/SBKK sale announced | Known-unknown |

**Japan consequence: unchanged.** No over-ceiling trigger, no rating action or pulled yen retail deal read; the deck cites a ¥1T retail bond issuance record. 9984.T ¥3,872, +13.88% on 11/10 (vendor). Full grade → `AGENTS/SAM/research/outputs/2026-11-06_softbank/2026-11-10_RESULTS_GRADE.md`.

## Rest of the overnight pass (`AGENTS/SAM/research/outputs/2026-11-10_overnight/OVERNIGHT_READ.md`)

| Item | Reading |
|---|---|
| BOJ December, Totan 11/9 15:15 JST | **72%** (11/6 52%, 10/29 82%); reviewed and ingested. Equivalents, not probabilities. Jump predates the Summary of Opinions. Combo theme `boj-december-path`: the "back above 70" condition fired; logging moves no score |
| Summary of Opinions (Oct 29–30) | Hawkish majority ("step up the pace", "neutral level soon"), two hold opinions, no date |
| MOF intervention Q3 per-op | 7/30 ¥7,975.6B · 7/31 ¥5,552.3B · **8/3 ¥1,871.4B**: 8/3 WAS an op day; the old "8/3 detector disagreement" is resolved; SAM-39 unaffected (window from 8/4) |
| BoP September | Current account +¥2,372.3B (−45.8% y/y) |
| **30Y auction 11/10** | **SOFT** on both frozen legs: BTC 3.356×, tail 2.4bp. Weakest since June; not a failure (no BTC<2.0 signal) |

## Housekeeping

KB-SAM-261 corrected (loan inside; reported figures replace the estimate title; Arm-margin "9/2027" relay superseded), KB-SAM-262/263 reviewed. Closeout and safe-push follow this packet.
