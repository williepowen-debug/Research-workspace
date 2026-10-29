# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure. **Last session update:** 2026-10-29 addendum 08:30 ET — WQ-536 RULED A encoded (THESIS v1.2.12); earlier the same day the Will-directed catch-up (Claude Code `claude-opus-5-5`). **Last real data refresh: 2026-10-29.** BOND ran no session 10/21–10/28; this session closed that gap.

Frontiers: Treasury nominal/real **10/28** · ICE credit via FRED **10/27** · NY Fed repo **10/27** · FR2004 as-of **10/14** · ACM **10/27** · KW **10/23** · Bund fitted **10/28** · PMMS **10/22** · TreasuryDirect auctions through **10/28**. Evidence: `analysis/2026-10-29_catchup/` (raw manifest, `derived.json`, grade transcripts). ⚠️ Local-clock stamps before 06:04 EDT 10/29 are UNVERIFIED (KB-BND-517); data vintages unaffected.

## Current judgment

**The October rally ended in a hawkish-hold bear steepener.** The 10/28 FOMC held 3.75–4.00% on a 10–2 vote, with Cook and Hammack dissenting for a +25bp hike. Official Treasury close: 2Y −3bp (4.67), 10Y +6 (5.05), 30Y +7 (5.37); 2s30s 60→70bp, so **BND-32 resolved FALSE** (65% call for no steepening). Real yields carried about half the 10Y move (+3). The UK Budget the same day means the decision is not isolated as the cause. Over 10/16–10/27 the ACM model put the 10Y fall in term premium (−15.0bp) while expected rates rose (+3.5bp).

**Auctions: long-end registered prints clean; the short end showed bid substitution.** The 10/21 20Y-R graded CLEAN on frozen bars, but only by +0.20pp on I′. The 10/26 2Y printed the **lowest indirect (45.68%) and highest direct (41.32%) of 46 nominal 2Y auctions since 2023**, with dealers ordinary (13.00%) and cover fine (2.59). That is an I′ marker fire on audit, and the bid was substituted rather than withdrawn. It is **AUDIT ONLY**: the bars were owed frozen at the 10/22 announcement, and the desk was dark.

**Dealers rebuilt hard at the long end.** FR2004 as-of 10/14: long-end stock $151.396B, +$16.312B w/w. **>21Y +$12.203B is the largest one-week rise in the 120-week series.** Two consecutive builds meet the VX-BND-04 trigger. Net stock is not proof of warehousing, and this trigger has un-fired on the next print before; as-of 10/21 lands 10/29 afternoon.

**Funding is firming into month-end.** SOFR−IORB 0 → +5bp over 10/22–10/27 on record SOFR volume ($3,147B); EFFR flat at 3.88. LIQUID owns the verdict (its 10/29 read: SOFR99−IORB +14). One session at +5 does not meet THESIS's "sustained >+5bp" bar, and the move started before the weak 2Y.

**Credit: the index retraced, the tail did not.** HY 340 [10/22], 10bp short of 350, then 318 [10/27]. CCC 1356 [10/23] is the highest of 785 FRED sessions (3-year window), now 1321. IG 88. For one session (10/22) HY sat +77bp over the 263 trough with vendor VIX at 19.03, which is the credit-equity lead letter. It reverted and is not counted as a confirmed fire.

## Regime and capital record
<!-- bond-state: thesis=v1.2.12; regime=C-36-TWO-PART@2026-09-01; gate_a=MET@2026-09-10; rearm=MET@2026-09-23; add=DECLINED@WQ-280; kill=MET-REC@2026-10-01; posture=APPROVED@WQ-357 -->
C-36 TWO-PART unchanged. **THESIS v1.2.12 (10/29): WQ-536 RULED A by Will** — only a registered composition fire resets the clean-auction counter; audit-only fires are recorded beside it. No research threshold or kill letter changed. WQ357 SELL TBT5 APPROVED 10/15; **FORGE reconcile 10/22 11:01 ET still shows TBT 5 held, no sell order** (FORGE D-82). Approval is not execution. TLT82P sold 10/12. WQ280 NO-ADD stands. No trade executed or proposed by BOND; no expiry reminders (Will 10/20).

## Current dashboard

| Metric | Dated observation | Source / basis |
|---|---|---|
| Official 2Y/5Y/10Y/20Y/30Y | 4.67 / 4.85 / 5.05 / 5.41 / 5.37% [10/28]; daily −3/+3/+6/+7/+7bp | [CONF PRIMARY Treasury par CSV pulled 10/29] |
| Official real 5Y/10Y/30Y | 2.36 / 2.67 / 3.10% [10/28]; daily −1/+3/+5 | [CONF PRIMARY Treasury real CSV] |
| 10Y/30Y nominal−real | 2.38 / 2.27% [10/28] | [EST fitted-par subtraction; not pure breakevens] |
| 2s10s / 5s30s / 2s30s | 38 / 52 / 70bp [10/28] | [EST PRIMARY subtraction] |
| 20Y−30Y | +4bp [10/28]; 20Y still above 30Y | [EST PRIMARY] |
| 5Y5Y forward / 10Y breakeven | 2.27 / 2.38% [10/28] | [CONF MIRROR FRED T5YIFR/T10YIE]; 23bp below 2.50 |
| ACM 10Y TP / KW 10Y TP | 0.6061% [10/27] (−15.0bp vs 10/16) / 0.9358% [10/23] | [EST PRIMARY NY Fed / MIRROR FRED]; different models |
| Fed path | 12/9 meeting: +21.8bp priced ≈ 87% of a +25bp hike (in-month method, EFFR held 3.88); strip peak 4.625 Oct-2027 (+74.5bp) | [EST CBOT vendor bars 10/28, not settlement; HENRY owns] |
| HY/CCC/B/BB/BBB/IG OAS | 318 / 1321 / 322 / 187 / 109 / 88bp [10/27] | [CONF MIRROR-WALLED ICE via FRED] |
| HY distance to 350 | 32bp [10/27]; peak 340 [10/22] | [EST] |
| SOFR / EFFR / IORB | 3.95 / 3.88 / 3.90% [10/27]; SOFR 99th 4.04; volume $3,147B | [CONF PRIMARY NY Fed; IORB FRED] |
| SOFR−IORB | +5bp [10/27]; 0/+2/+3/+5 over 10/22–10/27 | [EST]; LIQUID owns the verdict |
| FR2004 stock | Long-end $151.396B (+16.312); >21Y $50.953B (+12.203); 3–6Y $49.388B (−5.545) [as-of 10/14] | [CONF PRIMARY NY Fed] |
| PMMS spread | 7.32% − Treasury 10Y 4.96% [both 10/22] = 236bp | [CONF PRIMARY; EST]; above 230, not MBS OAS |
| Bund fitted 10Y | 3.43% [10/28]; five-session −4bp | [CONF PRIMARY Bundesbank] |

## Auction grades since 10/20

| Date | Security | Indirect / direct / dealer % | BTC | Grade |
|---|---|---|---:|---|
| 10/21 | 20Y-R `912810UX4` | 58.16 / 31.59 / 10.26 | 2.73 | REGISTERED CLEAN; I′ bar 57.96 (+0.20pp) |
| 10/22 | 5Y TIPS `91282CRR4` | 62.04 / 32.44 / 5.53 | 2.41 | REGISTERED CLEAN; no I′ for TIPS |
| 10/26 | 2Y `91282CRU7` | **45.68 / 41.32** / 13.00 | 2.59 | AUDIT ONLY; I′ FIRE (bar 54.82, −9.14pp); OLD not fired |
| 10/27 | 5Y `91282CRT0` | 60.05 / 29.40 / 10.56 | 2.33 | AUDIT ONLY; clean (I′ +0.63pp) |
| 10/29 | 7Y `91282CRV5` | prints 13:00 ET | — | AUDIT ONLY (same-day capture not registrable) |

## Gates and derived statistics

| Existing gate | Dated state |
|---|---|
| Real 10Y ≥2.50 sustain | MET; Treasury 2.67 [10/28], 17bp through; trailing run 34 (2026 file) |
| OLD auction add re-arm | MET 9/23; add DECLINED WQ280; 10/26 2Y did not meet OLD (dealer leg −11.12pp) |
| WQ291 paired kill | MET-REC 10/1 (closed window); funding window UNGRADED |
| Inflation anchoring | T5YIFR 2.27 [10/28], 23bp below 2.50 |
| HY marker / lead | HY 318 [10/27] >300; 32bp below 350; lead band 338–363 touched one session 10/22 |
| CCC escalation | 1321 [10/27] >1100; score 4 held |
| 30Y ≥5.00 | 96 of 207 2026 sessions, trailing run 80 [Treasury file through 10/28] |
| WQ400 Bund disorderly | NOT MET 10/21–10/28; 0 of 14 prospective evaluations |
| F2 buyback carrier | 10/27 20–30Y OFF-THE-RUN, sixth of six; routed to RED; next op 11/4 |

## Convergence Matrix

| # | Target /vector | Score | Status | Key evidence | Upgrade condition |
|---|---|---:|---|---|---|
| 1 | Long end / duration VX-BND-05 / VX-BND-12 / VX-BND-14 | 5 | 🔴🔴 | 30Y 5.37 [10/28], run 80; FOMC-day bear steepener | Existing top score |
| 2 | Treasury auction health VX-BND-01 / VX-BND-08 / VX-BND-13 | 4 | 🔴 | Counter 3 (WQ-536 A); 2Y audit-only I′ fire recorded beside it | Second composition failure with a confirmed mechanism leg; downgrade graded 11/4–11/8 |
| 3 | Dealer absorption VX-BND-04 / VX-BND-16 | 3 | 🟠 | Two consecutive builds; record >21Y one-week rise | Fresh long-end record + composition failure, same window |
| 4 | HY function VX-BND-02 / VX-BND-11 | 3 | 🟠 | HY 340→318; CCC 1356 3-year-window high | HY >350 or verified pulled-deal cluster |
| 5 | IG function VX-BND-03 / VX-BND-10 | 1 | ⚪ | IG 88 / BBB 109 | IG 120 / failed syndication |
| 6 | CDX/cash VX-BND-06 | 1 | ⚪ | No fresh proxy run this session; true CDX gap | Confirmed fast-layer lead |
| 7 | Credit-equity VX-BND-07 | 2 | 🟡 | One-session red letter 10/22, reverted | Band held ≥2 sessions with VIX <20 at VIOLET's close |

**Composite 19/35 = 5+4+3+3+1+1+2 (was 17):** one 5, one 4, two 3, one 2, two 1. Dealer 2→3 and credit-equity 1→2, both on their letter. **Clean-auction counter = 3 (WQ-536 RULED A, Will 10/29):** the 10/21 20Y-R registered clean met the convergence-downgrade letter; the 10/26 2Y audit-only I′ fire is recorded beside the count, not a reset. Auction health stays 4 until BOND grades the downgrade at the 11/4–11/8 wake (unless a registered print changes the count first). Rider: the downgrade would follow the weakest 2Y in BOND's records, a short-end tenor. Outside composite: VX-BND-15=2, VX-BND-17=2 (was 1), VX-BND-18=2, VX-BND-19=3, VX-BND-20=2.

## Exit / falsification

WQ157/WQ291 recommendation MET; WQ357 sell approved, not filled at the 10/22 reconcile; funding window UNGRADED. Position falsifier 10Y<4.15 AND 30Y<5.00 for 3 sessions plus a clean refunding: not met (5.05 / 5.37 [10/28]). Convergence downgrade: counter letter MET 10/21 and standing under WQ-536 A; graded at the 11/4–11/8 wake. Position construction and any DTE review are TERRY's. **OPEN predictions: 0** (BND-32 resolved FALSE). VX-BND-09 auction tails remain retired.

## Immediate Catalysts (same event set as docket/CATALYSTS.tsv)

| Date | Obligation |
|---|---|
| 10/29 | 7Y `91282CRV5` 13:00 ET (audit-only grade) · ECB · GDP/PCE 08:30 · PMMS noon (VX-17 band re-test) · FR2004 as-of 10/21 ~16:15 (can un-fire VX-04) · dealer meetings 10/29–30 |
| 10/30–11/3 | ECI 10/30 · month-end and coupon settlement 11/2 (SOFR context) · borrowing estimates 11/2 · JOLTS 11/3 |
| 11/4 | 🔴 QRA: F1/F3 buyback flip conditions; sb0607 window expiry; F2 op 10–20Y |
| **11/4–11/8** | 🔴 **Freeze refunding bars (3Y 11/9 · 10Y 11/10 · 30Y 11/12) or the refunding grades AUDIT ONLY** |
| 11/5–11/13 | Productivity 11/5 · jobs 11/6 · FHLB Q3 11/9 · CPI 11/10 · VX-BND-20 review 11/11 · FRBNY FX report 11/13 · RED FT-11 ruling sent (deadline was 11/13) |
| 11/18, 11/19 | 20Y new issue · 10Y TIPS reopening (bars freeze 11/12–11/17) |
| 12/1, 12/9 | Sovereign CDS retest · December FOMC + SEP |
| 2027-1/25, 1/27 | GPFG expert report · January FOMC |

## BOTTOM LINE

Long bonds rallied through 10/22 and gave part of it back on the Fed's hawkish hold: two officials wanted a hike, and the long end sold off while the 2-year fell. Long-dated Treasury auctions still clear. But the latest 2-year auction drew the least foreign/custodial demand in this desk's records, dealers added the most very-long bonds to inventory in a single week in over two years, and overnight funding costs are edging above the Fed's floor into month-end. Each of these can still revert, and none yet shows the market failing to absorb supply. The November 4 refunding announcement and the auctions after it are the next real test. BOND must run between 11/4 and 11/8 to grade them properly.
