# BOND — Trade Recommendations

**Last Updated:** 2026-05-19 by BOND (live data pull)
**Regime:** 🟡→🟠 watch — long-end leg active (10Y broke 4.5, 30Y >5 sustained); public credit still calm

---

## Current Bottom Line

BOND still **does not support fresh short-HY premium**. HY OAS 283, IG OAS 75 (tightening), HYG holding $79 — credit cascade has no transmission.

BOND **does support duration shorts (TLT puts) with sharper conviction**: 10Y broke 4.5 on 5/15 (4.59), 30Y at 5.12 sustained above 5 for 4 sessions, TLT new low $83.01. The May 20 20Y auction is the decision point — clean = ride the term-premium move; failed = escalate to red across long-end / dealer absorption / FOI vectors.

---

## Active / Legacy Recommendations

| # | Trade | Current Posture | Conviction | Why | Hold / Add / Kill Rules |
|---|---|---|---:|---|---|
| 1 | HYG $75P Jun | **Do not add / do not roll** | 1/5 | HY OAS 283, IG OAS tightened to 75, HYG $79.36 — no credit transmission despite duration move. | **Kill/let decay:** HY OAS <300 and no CDX/issuance stress. **Reopen:** HY OAS >300 with velocity. **Add/roll only:** HY OAS >350 or credible issuance freeze. |
| 2 | TLT puts | **Hold; two-leg gate 5/20–5/21** (conditional-add on Leg 1 weak; aggressive-add on two tails) | 3/5→4/5 conditional / 5/5 on two-tail | 10Y broke 4.5 (4.59 on 5/15), 30Y 5.12 sustained, TLT new low $83.01. BND-07 Day 2. | **Two-leg framing (see `WATCH_20Y_10Y_MAY20-21.md`): Leg 1 (5/20 20Y reopening)** — clean (BTC ≥2.60 / tail ≤+1bp / indirect ≥58%) = hold; soft / demand-hole / dealer mid-teens = **add-conditional armed**; failed (BTC <2.40 / tail >+3bp / dealer >17%) = **aggressive-add same-day** (pre-approved by Will 5/19, executes without live [Approve]). **Add-conditional layer = TLT $83P Aug 15 × 2 (budget ~$500-600, accept up to ~$1,000 on marks); aggressive-add adds same layer same-day + Will-sized additional layer.** **Leg 2 (5/21 10Y 9Y8M reopening)** — single tail confirms firming, hold; **two tails in 24h across both legs = thesis FIRED, aggressive-add, BOND state 🟠→🔴, long-end vector 4→5**. **Kill:** 10Y back below 4.15 AND clean Leg 1 AND 30Y back below 5 for 3 sessions. |
| 3 | Credit-equity lead | **Inactive watch** | 1/5 | HY cash not widening; VIX below 20. No public-credit lead signal. | **Reactivate:** HY OAS +75-100bps from trough while VIX remains <20; strongest if CDX leads cash. |

---

## Reactivation Matrix

| Signal | BOND Interpretation | Trade Implication |
|---|---|---|
| HY OAS >300 for 3 sessions | Credit stress watch reopens | Price HYG/JNK downside, no blind entry. |
| HY OAS >350 + pulled deals | Issuance freeze / refinancing wall | HYG/JNK downside can be proposed to Will. |
| CDX.HY widens while cash OAS stays tight for 2+ weeks | Synthetic protection demand leading cash | Supports early short-credit re-entry. |
| 10Y >4.5 for 5 sessions | Duration stress confirmation | TLT put bias strengthens. |
| 30Y >5 plus weak 30Y auction | Yellow duration fatigue if tail small; demand hole only if dealer take/funding stress confirms | TLT puts watch/hold valid; aggressive add waits for confirmation. |
| Auction BTC <2.3 or tail >2bps with high dealer take | End-demand weakness | Signal LIQUID/ZHAO; duration/credit watch rises. |
| SOFR-IORB turns positive after weak auction | Auction stress funding through repo | Systemic confirmation; escalate to LIQUID/PROME. |

---

## Cross-Agent Dependencies

| BOND Signal | Confirmed By | Who Needs It |
|---|---|---|
| Weak auctions | ZHAO foreign demand / LIQUID repo pressure | PROME, LIQUID, ZHAO |
| Issuance freeze | REGINALD bank refinancing burden / BROCK private-credit marks | REGINALD, BROCK, HENRY |
| CDX leading cash | HENRY/VIOLET vol lag | HENRY, VIOLET, LIQUID |
| Long-end break | HAWK/BRENT inflation shock + LIQUID funding | PROME, LIQUID, HENRY |

---

## Rejected / Downgraded

| Trade | Prior Posture | New Posture | Reason |
|---|---|---|---|
| HYG $75P Jun | Mar 26 conviction 4/5 | Downgraded to 1/5 | HY OAS fell from 319 to 281; issuance strong; no confirmed freeze. |
| Broad credit-equity short timing | Mar 26 conviction 3/5 | Inactive | Credit has not led lower; public tape remains benign. |

---

## Next Review

**May 20 (tomorrow): 20Y Bond auction** — decisive read on whether long-end break is mechanical (failed demand) or just expensive (term premium repricing). Update TLT conviction immediately post-result. Also watch: 10Y >4.5 streak (Day 1 of 5), SOFR-IORB (-12bps, no funding stress yet), HY OAS for any whiff of >300.
