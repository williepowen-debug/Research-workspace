# Peer read — VIOLET · LIQUID · BOND (Will-directed, 2026-09-24 ~22:5x ET)

*Read-only pass over each desk's STATUS (+ NEXUS_BRIEF/SCRATCH where needed) at their latest 9/24 commits: VIOLET `34a0c593a` 22:47 · LIQUID `33c7cf99e` 22:13 · BOND `fded178ee` 21:42. Nothing edited in any peer file. $0, no threshold moved.*

## Per desk

| Desk | Headline (their file, 9/24) | Key figures [src] | Next test |
|---|---|---|---|
| **VIOLET** | Rates vol has repriced further than equity vol on the same catalyst — a SPREAD, not a lead-lag (walked back 22:47) | MOVE 104.58 [9/24, p98.3 of a 58-row ledger since 7/6] · VVIX 90.57 (first close >90 post-FOMC) · VIX3M/VIX 1.1761 (compressing 2 sessions, still contango) · OVX ratio 3.47 FIRE · convergence 28/50 | CBOE history has not published 9/23–9/24; re-pull. Cheap-tail alert 4/4 on the 9/22 basis — on 9/24 readings VVIX 90.57 exceeds its L1 ≤90 leg |
| **LIQUID** | 9/23 rate shock was the first in this window to reach credit — one day, lower tiers only | Ladder 9/22→9/23: IG 0 · BBB 0 · BB +3 · **B +7** · CCC +18 · HY +5→273 [FRED]. Of 21 days since 2023-09 with 10Y ≥+12bp, HY widened ≥5bp only twice (2025-04-07, 9/23). Reserves $2,930.2B [WRESBAL wk to 9/23], −$83.6B, TGA +$100.1B explains it; repo did not reprice. GATE-HY-REKILL 0-of-2; HY 7bp under the 280 X1 half | **9/30 quarter-end: ~$183B 2Y/5Y/7Y settle with $130B reserve cushion to <$2.8T; SOFR publishes 10/1.** A Q-end spike alone is the null |
| **BOND** | Second straight fresh long-end high; real-led | Treasury par 9/24: 30Y 5.47 (since 2004-06) · 10Y 5.18 · 5Y 5.03 · 2Y 4.87 · 10Y real 2.85 (since 2008-11-24; 22 prior sessions ever ≥) · 1y1y 5.23 · T5YIFR 2.33. 9/23 5Y = old-conjunctive composition failure (indirect 54.31%, dealer 15.77%, BTC 2.21); **thesis kill NOT fired** (funding −3bp). Composite 14/35 (▲2) | 9/30 quarter-end + PCE + BND-27 (CCC <1100, 7bp away) + TLT 77P expiry |

## Where they bear on HENRY

1. **Term premium — BOND measured what I had not (`KB-BND-325`).** Under NY Fed **ACM**, 10Y TP fell 6.4bp 9/15→9/23 while the 10Y rose 11bp ⇒ the post-FOMC rise is expected POLICY PATH. Under **Kim-Wright** (`THREEFYTP10`), TP hit 0.9719 [9/16], highest since 2011, but its frontier is 9/18. **The two models disagree; name the model in any TP claim.** My candidate real-yield letter listed THREEFYTP10 only as the TP instrument — it needs both, with the disagreement enumerated as an outcome region.
2. **Credit-primary rule (H4):** LIQUID's 9/23 ladder is the first sign of rates reaching credit above CCC (B +7). n=1 day — a tell, not a trend. HY 273 is 7bp under LIQUID's 280 X1 half (conjunctive; wrapper not armed ⇒ X1 cannot fire on HY alone).
3. **Agreement on the core read:** all three desks + HENRY have the rise real-yield-led (DFII10 2.63→2.85, breakevens flat/down), funding calm, the CCC tail at 2026 highs (1,093; CCC−BB 934) with the blended index inert.

## Defects noticed in peer surfaces (not edited — owners' files)

| Desk | Location | Defect |
|---|---|---|
| VIOLET | `STATUS.md:87` (§ REGIME STATUS) | Still reads *"9/23–9/24 confirm rates vol is LEADING, not one-day"* — the exact claim walked back at 22:47 in her BOTTOM LINE, SCRATCH and NEXUS_BRIEF. Supersession did not travel to this bullet |
| VIOLET | `STATUS.md:9` | 10Y 4.963→5.114→5.162 is the `^TNX` vendor basis, unlabelled; Treasury par is 4.96→5.11→5.18 (+22bp, not +20) |
| LIQUID | `STATUS.md:4-21` | BOTTOM LINE is stamped 9/17 and carries 9/16 levels (HY 270, CCC−BB 921, reserves $3,013.8B) above a 9/24 LIVE STATE that supersedes them "for the items named here only" — a top-of-file reader gets week-old levels |
| LIQUID | `LAST_COMPLETION.md` | 2026-08-28 content, no FROZEN banner (VIOLET and BOND both bannered theirs) — current-and-wrong by name |
