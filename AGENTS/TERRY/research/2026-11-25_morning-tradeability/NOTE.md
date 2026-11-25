# TERRY — morning tradeability, WQ-745 re-read, VIX leg, inbox drain (2026-11-25)

**Session:** TERRY, Claude Code, Claude Opus 5.5, laptop; PROME prome-77 morning wake, preflight 09:43 ET. Started 09:43 EST (from `date`). **NO ORDER. $0. No new card. No card term changed.**
**Data:** vendor intraday (`fetch.py`, `chain_fetch.py --no-cache`), 09:47–09:51 EST unless stated. Option marks are SCREENING marks (durable finding 5b); a fill is priced on the broker chain. Today is a **red day** (S&P 6,992.27 −2.90%, SPY $697.72 −2.93% at 09:47).

## Tape at the read (09:47 EST, vendor, intraday, not closes)

| Object | Read |
|---|---|
| CRWV | **$37.75 −11.40%** (11/24 close $42.60; 10/6 $91.72 ⇒ −58.8%) |
| NVDA / ARM | $142.44 −8.33% / $145.66 −9.84% |
| S&P / SPY / QQQ | 6,992.27 −2.90% (under HENRY's 7,037.04 close line, intraday) / $697.72 −2.93% / $610.72 −4.29% |
| RSP / KRE / HYG | $210.97 −1.40% / $68.99 −1.11% / $76.19 −0.31% |
| VIX / VIX3M | 32.71 +24.1% / 28.76 (ratio 0.879, inverted) |
| HY OAS (FRED BAMLH0A0HYM2) | **363 [11/23]**; the **11/24 cell NOT posted** at 09:48 and 09:50 EST pulls (CCC 1,387, BB 219 [11/23]) |

## 1. WQ-745 re-read — `IDEA-CRWV-AIFIN-NOV24` (CRWV Feb-19-2027 40/30P ×1 ≤ $3.25)

**Verdict: every term stands as written. No level, operator, instrument or consequence changed. No correction to the WILL_QUEUE row's text is needed; three facts in it have aged and are given here as dated updates, not corrections.**

| Term / caveat on the card | Today | Still right? |
|---|---|---|
| T1 (a): green CRWV close ≥ $48.00 | $37.75 at 09:47; needs **+27.2%** and a green close | Right as written. Further away than at writing (+12.7% from $42.60) |
| T1 (b): LIQUID CoreWeave 5Y CDS ≥ 1,200 bp, ≤ 2 sessions old | 1,314 bp [11/24] is LIQUID's read; WALTER SIG-W-20261125-013 relays the same 1,314 as a record, 68% implied 5-year default probability (secondary, undated "overnight") | Met today on the 11/24 read; that read goes stale for an entry after 11/26 by the card's own 2-session rule, so a later entry needs a fresh LIQUID read |
| Cap ≤ $3.25 net debit | Screen 40P 9.35/9.40, 30P 4.50/4.70 ⇒ **mid $4.78, outer $4.90** (11/24: $4.03 / $4.15). IV 111.7% / 123.1% (11/24: 109/119%). Black-Scholes at today's IVs reproduces the mid ($4.75 at $37.75) | Right. The cap and the trigger agree: the model puts the spread at $3.25 near CRWV **$46** (80 DTE) and at **$2.91–3.13** at $48 (70–86 DTE). The cap is the real entry gate; lowering the $48 trigger would not let it fill |
| Breakeven $36.75 at the limit | Spot $37.75 is now 2.6% above it | Right; the "−13.7% from today's $42.60" line on the card is dated 11/24 and correct for that date |
| Do-not-trade: CoreWeave's ~$4B IG loan launches and prices | Not found today (VULCAN, WALTER -013: no pulled or repriced AI-infrastructure deal found) | Stands |
| CoreWeave earnings date NOT VERIFIED | Still not verifiable: the Q4 FY2026 date is not announced. Precedent: Q4 FY2025 reported **2026-02-26**, date announced **2026-02-05** (CoreWeave IR release, BusinessWire 2026-02-05; search 09:5x EST). If the pattern holds, the print falls after the 2/19 expiry and the 2/05 time stop | Caveat stands, now with a precedent. Still read from IR before any entry |
| Nvidia 10-Q about 12/04 (12/09 with a 12b-25) | Still unfiled at EDGAR 09:33 ET (VULCAN); VULCAN's unscored P(NT 10-Q) about 0.30 | Stands |
| Book overlap with HYG ×5 = $632.80 | Unchanged; HYG fill UNKNOWN | Stands |
| Thanksgiving: 11/26 closed, 11/27 short; no entry on 11/27 | Calendar checked (11/26/2026 is the fourth Thursday) | Stands |

**Aged facts in the WQ-745 row (updates, not errors):** (i) "Tonight it cannot be entered: the spread screens at about $4.03": today it screens at **$4.78 mid / $4.90 outer** with CRWV $37.75. (ii) "CoreWeave is already down 54% since 10/6": **−58.8%** at 09:47. (iii) TERRY's trigger odds "40%": my current, **unscored** view is **about 20%** (below). The registered CAL-0010 stays at 0.40 as registered and is graded as registered; I do not re-register.

**Why ~20% now:** reaching a $48 close from $37.75 in about 11 sessions has a touch probability of about 0.30 at the 112% implied vol and 0.47–0.55 at the 160–190% realised (reflection approximation, continuous; discrete closes lower it). Leg (b) must hold on the same day: a 27% relief rally would very likely tighten the CDS from its 1,314 record, and it also needs a fresh LIQUID read. Joint ≈ 0.35 × 0.55 ≈ 0.20.

**Still worth Will's decision?** Yes, and the lean is unchanged: **A, low conviction; B equally sound.** The decision is cheap (a standing NOT-FIRED idea, $326.30 max, no chase) and today's tape does not falsify the premise. But today adds **no financing-specific evidence**: VULCAN reads the fall as an AI valuation de-rating across suppliers (credit barely moved; HYG −0.3%), and adds counterevidence on the financing leg (SpaceX GPU lease notes about $32.1B priced and upsized at 8.259%, Apollo via WALTER correction 11/23; Fermi's customer prepayment funded, 8-K 11/23). The CDS record (1,314) is the one piece that points at CoreWeave's financing itself, and it is secondary. If Will approves, the most likely outcome is that the card lapses unfired at the 12/11 close (about 80%).

**Do not:** buy the spread today. It is a red-day put at $4.78 mid, 47% over the cap, after a −11% session: the chase the card was built to refuse.

## 2. VIX leg (VIOLET's trigger: HY cell ≥ 370)

**The 11/24 HY cell was NOT posted** at the 09:48 and 09:50 EST FRED pulls (last 363 [11/23]); a final pull at closeout is recorded in §5. **NOT-FIRED; nothing built.**

What I would need to build it live, and what today's screen says:
1. **The 11/24 cell ≥ 370** (first-published, FRED BAMLH0A0HYM2). Without it there is no trigger.
2. **VIOLET's current direction** (11/23 lean: fade, 60–65%). VIOLET is live in-process under PROME today.
3. **A broker chain** for the fill (5b).
4. **The day-colour test, measured, not assumed.** My 11/24 note wrote "builds it live on a red day (root rule #6: calls on red days)". For a VIX call that literal reading inverts the proxy: on an equity red day VIX calls are where convexity is dearest. Measured today: VIX Dec-16 30/40C screens 30C 2.63/2.70, 40C 1.30/1.36 ⇒ **mid $1.34, outer $1.40**, against **$0.77 / $0.89** after hours 11/24, **+57% at the outer**. That is paying up for convexity by direct measurement, so the root-rule-#6 test (`RISK_RULES.md` § Breaking root rule #6) argues **against** a same-day build even if the cell prints ≥ 370. Size at the outer: ×5 = $706.50 (1.4× the $500 default); ×3 = $423.90 inside it; breakeven about 31.40 on the 12/16 settlement (the December VIX future was not readable on the vendor: `VXZ26.CBF` errors).
5. **Book overlap:** it pays on the same second-leg branch as HYG ×5 and shares the AI antecedent with the CRWV idea: one view, not three.

If the cell prints ≥ 370 later today: I would bring it to PROME as a NOT-FIRED, re-priced idea with the measured day-colour cost on the card and a lean to **wait for a VIX-down session**, not as a same-day build. Projection (unscored): the 11/24 cell ≥ 370 about 30% (it needs +7 bp on 363; HYG closed $76.43 on 11/24 and was unchanged pre-open 11/25 per WALTER -005 and HENRY, and the 11/24 tape was equal-weight up, RSP +0.54%).

## 3. Inbox — eleven packets (the ten named in the wake plus VIOLET's, arrived 09:52 ET), each answered

| # | Sender, subject | TERRY answer | Reason | Changes on |
|---|---|---|---|---|
| 1 | BRENT 11/24, Red Sea bypass tail (Yanbu ~2.5–3.1 mb/d; halt 5% / 72h, 8–10% / 2 wk) | **NO CARD** | Energy arm RETIRED by Will 8/7, WQ-192 stand-down, BG-02 NOT MET: a crude tail call is a new direction, not mine to open. BRENT's odds are low and unpriced-ness is not a trigger. Mirror (11/18, not truth) shows 30 USO shares: existing upside exposure | A Houthi launch at Yanbu or Jeddah or a stated loadings cut (FALCON's up-tells) **and** Will reopening the energy arm |
| 2 | FALCON, Red Sea port threat (FAL-13 25% damage by 12/09; halt ~8%) | **NO CARD** (joint with 1) | Threat triggered, not carried out; FALCON says any card's trigger is BRENT's barrel read, not its ladder | Same as 1 |
| 3 | NEXUS, AI-infrastructure credit edge (65% stays concentrated / 35% broadens to 12/09) | **NO NEW CARD** | The two branches already have expressions: concentrated ⇒ WQ-745 CRWV (NOT-FIRED, §1); broadening ⇒ HYG ×5 (approved, fill UNKNOWN). Today fits "concentrated": RSP −1.40% vs SPY −2.93%, HYG −0.31% while AI CDS print records. No reply to NEXUS needed: nothing here changes what NEXUS watches | Broadening tells (HENRY's: HY > 376 on an RSP-down day, KRE < $65, HYG < ~$75.50) |
| 4 | RED, TRY-FIRE-006 grade (RED leg MIXED) + RED-FT-11 FUNDAMENTAL | **RECORDED; NO CARD** | Item 1 recorded in `POSTMORTEMS.md` owner-grades table (8 of 12 desks now; still owed WAL, BOND, LIQUID, DEWEY, PROME). Item 2: RED says no investment implication; agreed | — |
| 5 | HENRY, PCE + red line (S&P close < 7,037.04 by 12/4 ~70%) | **NO CARD** | Buying index puts today is a red-day put at VIX 32.7 (+24%): paying up, no refuting measurement. The vol row's condition met **intraday only** again: SPY Dec-4 698 straddle mid $28.04 ≈ 30% implied vs 35.8% 10-day realised incl. today's bar (35.1% ex today); "at a close" unread; $2,815 at ask = 5.6× default. HYG ×5 is the broadening expression | A close with implied ≤ realised and S&P < ~7,400 (`TRY-NOTRADE-SPXGAMMA-NOV21`), at Will's per-card choice of size |
| 6 | CARL, CRL-32 not fired (saving 4.1%), V5 gas 4→3 | **NO CARD** | CARL reads no investment implication: a cautious, not collapsing, household; nothing listed is keyed to it | November saving rate ≤ 3.8% ex-rebate or real spending falling (12/23 print) |
| 7 | REGINALD, FDIC Q3 QBP | **NO CARD** (concur with REGINALD) | Large-bank CRE improved on every basis; the two "worse" lines are mostly one private bank. OZK foreclosed CRE +$128.0M is one quarter, no owner direction | A second named bank with a nine-figure multifamily nonaccrual jump (12/31 Call Report); KRE < $60 (REG-T-01) |
| 8 | SAM, SoftBank LTV at its 25% line (24.7–25.3% on Arm $146.41) | **NO CARD** | 25% is policy, not covenant; SAM: no default risk, 65% the 12/31 ratio prints under 25%. Any Arm/SoftBank put today is a red-day put after −9.8% (Arm), on the same AI antecedent as WQ-745 (N_eff). Margin-call levels undisclosed: the forced-sale tail cannot be sized | SoftBank announcing an Arm block sale or a margin-loan draw; a disclosed call level; Arm holding under ~$130 (SAM's invalidation) |
| 9 | VULCAN, AI selloff / Entity List / Section 301 / Nvidia 10-Q | **NO NEW CARD; consumed into §1** | Valuation de-rating, not a financing refusal; financing counterevidence (SpaceX notes upsized). Section 301 excludes servers and chips in the notices read. An NT 10-Q would be a dated event; `TRY-NOTRADE-NVDASEC-NOV21` already changes on it | An NT 10-Q or Item 4.02 at Nvidia (12/04–12/09); a pulled AI-infrastructure deal |
| 11 | VIOLET, arrived 09:52 ET mid-session: VIX over 30, a 7th straight inverted close likely; 13 past seven-close streaks | **NO CARD either side** | **Long vol:** not cheap by measurement: Dec-16 30/40C outer $1.40 vs $0.89 on 11/24 (+57%). **Short vol (the fade VIOLET's history favours 9 of 13):** the Dec future already prices it (VIOLET: Z6 27.60 at 09:48 vs spot ~32; put-call parity at the 25 strike gives ~27.2). A defined-risk fade, Dec-16 25/20P, screens 25P 2.06/2.12, 20P 0.31/0.34 ⇒ outer $1.81, breakeven 23.19 on the 12/16 settlement, about 36% of width: it needs the settlement ~15% under a future that already discounts the fade, and it offsets the approved HYG ×5 hedge's branch. VIOLET's "dip under 25 somewhere, ~60%" is not a settlement-date call | VIOLET registering a settlement-keyed call (Z6 12/16 settlement ≤ ~23) with odds well above ~36%; or its lasting tells (close ≥ 31 with HY ≥ 370, VIX6M > 30) for the long side on a VIX-down day |
| 10 | HOMER, DR-4956-FL CONFIRMED (7 counties) | **NO CARD** | Replaces the 11/24 REPORTED label; no listed exposure named; `TRY-NOTRADE-DRAIN-NOV24` conditions unchanged | A named lender or REIT flood provision, a deferral programme, or an SE-coast urban flood with an exposure screen |

## 4. WALTER lane (BOARD, §3.5-exempt pull)

| Signal | Disposition | Use |
|---|---|---|
| SIG-W-20261125-005 FLASH VIX > 30 and +5 premarket | acted | §2: VIX leg NOT-FIRED (HY 11/24 unposted); vol screen +57% since 11/24 |
| SIG-W-20261125-013 AI credit swaps at records (CoreWeave 1,314) | acted | §1: leg (b) source corroborated (secondary); no deal pulled today |

BOARD scan run, 2 new since SIG-W-20261124-001, 2 logged.

## 5. Forward view (unscored unless named)

- **Expected:** the AI selloff stays concentrated through 12/09 (NEXUS 65%); CRWV does not close back at $48 by 12/11 (about 80%), so WQ-745 most likely lapses unfired. HY 11/24 cell under 370 (about 70%).
- **Meaningful alternative:** credit broadens (HY > 376 on an RSP-down day, KRE < $65): then the approved HYG ×5 is the book's expression, and a VIX build becomes a question for a VIX-down session, not today.
- **What would change my mind:** a pulled or flexed AI-infrastructure financing (the financing-specific evidence that today lacks); a CoreWeave $4B loan pricing (kills WQ-745); an NT 10-Q at Nvidia.
- **HY 11/24 cell, final pull at closeout (09:55 EST, FRED):** still NOT posted; last cell 363 [11/23]. The VIX leg stays NOT-FIRED for this session; the next TERRY session reads the cell first.

Small items logged (WQ-622, `SIGNALS.tsv`): `COMBO-CREDIT-FOLLOWING` (AI single-name CDS records vs HYG −0.3%), `COMBO-REBOUND-BREADTH` (RSP −1.40% vs SPY −2.93%), `COMBO-BEAR-PREMISE-EROSION` (QBP large-bank CRE better; OZK foreclosed CRE +$128.0M as counterevidence).
