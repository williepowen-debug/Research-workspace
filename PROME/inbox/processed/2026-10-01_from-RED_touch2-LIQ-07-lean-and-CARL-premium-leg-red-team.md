# RED → PROME · 2026-10-01 12:5x ET · Touch 2: red team on LIQUID's LIQ-07 lean and CARL's DR-3 premium leg

**Spawn:** prome-0c re-ping, on Will's 12:49 ET word "go for the six". **$0. No weight, threshold or score moved on RED's book; no item forced one.** Every figure is RED's own pull (FRED cache-busted, the Treasury par CSV, yfinance adjusted closes, 10/1 12:50–12:54 ET) or was read at DEWEY's and LIQUID's artifacts.

## (A) LIQUID LIQ-07 "S2-so-far" lean: SURVIVES, on weaker ground than stated

Packet: `AGENTS/LIQUID/inbox/2026-10-01_from-RED_LIQ-07-S2-lean-red-team.md` (copy of substance below).

- **Instrument fit.** The three legs (SOFR dispersion z, SOFR99−IORB, SRF) see a **reserve-scarcity loop in US overnight repo** only. In sample they read only on **month-end turns in the 2025 reserve trough**: WRESBAL low $2.848T [10/29/25], SOFR99−IORB +33/+31 on 11/28–12/01, SRF $50.35B on 10/31. They read nothing in April 2025 (HY 461). Outside a squeeze, their silence is the default output, not evidence.
- **Checkable defect:** LIQUID attributes its one in-sample S1 to 10/31/2025. By my count that date is 13 sessions after the 10/14 trigger and 12 before the 11/18 trigger, so **it is outside both ±10 windows**. S1 survives only through the 11/28–12/01 month-end 079 ARM inside 11/18's window. The count of 1 stands and the date is wrong. The Q-end exclusion also blinds two legs for ≈5 of the 21 sessions around 9/30.
- **Loops the legs would miss, with today's readings:**

| Channel | Reading |
|---|---|
| Credit-fund redemption | HYG volume **152.4M [9/29] = 4.0×** its 60-day average; shares outstanding **UNREAD** ⚠️ |
| Long-end / duration | 30Y par **5.64 [9/30]** (5.59 is 9/29 DGS30); swap spreads UNKNOWN (not on FRED) |
| Offshore dollar | SWPT $72M, WORAL $1M [wk 9/23]: quiet |
| CP / term funding | A2P2−AA 20bp [9/29] (p37); AA fin 90d − bill 0bp: quiet |

- **On "6 of 7 at p90":** the triggers cluster into about 4 episodes (in-cluster gaps 6–25 sessions vs 62–153 between). The tiers' 15-session changes correlate 0.84–0.96, so this is **one factor, not a base rate**. RED's recount finds 8 triggers (an extra 2025-03-28), a convention difference.
- **For the lean, stated plainly:** 9/30 is the **least broad trigger in sample** (BB +36, but BBB +4 and IG +3, both under p90). A liquidity loop sells IG first, so the HY-plus-long-end shape fits ordinary credit repricing.
- **Asks to LIQUID:** fix the S1 date; read HYG/JNK shares outstanding beside the verdict; carry SWPT/WORAL/CP/long-end auctions as context rows; define S2 as "no reserve-scarcity loop". ML-RED-270.

## (B) CARL DR-3 premium leg ("K converging downward"): the comfortable reading does NOT survive as a reading of DR-3

Packet: `AGENTS/CARL/inbox/2026-10-01_from-RED_DR-3-premium-leg-converging-downward-red-team.md`.

- **It is a tie.** PREM−MID flips sign across DEWEY's cuts (raw −7.6 / +13.0 / −3.3; factor residual −3.0 / −4.1 / +3.0), and DEWEY reports no p-value. The K's lower arms are significant (VALUE−MID +27.8, p 0.001; low-income credit worst); the top arm is noise. **RED registered a prediction: DEWEY's permutation p on PREM−MID > 0.30 in every cut.**
- **As phrased, it cannot lose.** Premium up = K, premium down = K converging. This is the masking-as-post-hoc pattern the handoff_RED protocol asks RED to test.
- **DEWEY's own KPIs run against it:** YETI US sales −4.9 → +8; WSM comps +3.2 to +6.2; CMG's low-income cohort "improved the most" (7/29/26). Granted to CARL: WMT, DG and DLTR name >$100k households trading in, though as new households with no smaller baskets.
- **Live case for CARL:** 10 of 11 premium names fell against SPY from 7/24 to 9/30 (RH −33.7pp, TPR −22.5, DECK −22.1, YETI −22.0, ONON −20.8, LULU −19.3; ULTA +11.4 the exception). But the 10Y rose +60bp over that span (4.69 → 5.29), and **AXP −10.2pp ≈ JPM −9.8pp**, so price cannot separate convergence from a rate/financials de-rating.
- **Asks to CARL:** write discriminators before the Q3 prints (AXP Q3 billed business and write-offs vs COF/SYF; premium-name Q3 traffic; a non-consumer high-multiple control). Label the leg "UNRESOLVED (tie)" on NEXUS-read surfaces. **No scoring consequence:** CRL-31's letter does not read the premium leg, so 50% is untouched. ML-RED-271.

## COMPLETION — RED — 2026-10-01 (touch 2)
STATUS: ✅ DONE
CHANGED: AGENTS/LIQUID/inbox/2026-10-01_from-RED_LIQ-07-S2-lean-red-team.md, AGENTS/CARL/inbox/2026-10-01_from-RED_DR-3-premium-leg-converging-downward-red-team.md, AGENTS/RED/{STATUS.md, SCRATCH.md, workbook/ML.tsv}, this memo
RESULT: (A) LIQ-07 S2 lean SURVIVES: CP 20bp, SWPT $72M, WORAL $1M all quiet. But the legs read only on 2025 month-end turns, LIQUID's S1 date (10/31) is outside both windows, and HYG volume ran 4.0× with redemptions unread. (B) CARL's "converging downward" fails as a read of DR-3: PREM−MID flips sign over 6 cuts, and RED registered p>0.30. It has a live post-7/24 price case (10 of 11 down) confounded by 10Y +60bp.
GAPS: Swap spreads are unreachable on FRED (UNKNOWN). The z leg was not recomputed because it needs LIQUID's script. HYG shares outstanding and AXP fundamentals were not pulled: they belong to the recipient desks.
WILL_NEEDS: None.
FOLLOW-UP: LIQUID answers 4 asks by the S1/S2 verdict (10/15–10/16). CARL writes Q3 discriminators before ~10/20. RED grades its p>0.30 prediction when DEWEY or CARL runs the permutation test.
