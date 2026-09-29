# WQ-317 cross-market attribution — SAME-DAY PARTIAL (9/29) + the book's lines + nearest BOND lines

**BOND · 2026-09-29 12:5x ET · PROME doorbell (prome-e6, 12:5x ET; Will: "I'd like us to take a look at BOND. Yield rates are continuing to rise.")** · Letter: `inbox/processed/2026-09-28_from-PROME_WQ-317-cross-market-attribution-read.md` (DOCKET L532, full page due Fri 10/02). **This is a PARTIAL: HANS's EU/UK rows are NOT received (HANS's own last STATUS cells: Bund 3.57 [9/24], gilts [9/18] — stale, not used); EU/UK legs below are TradingEconomics SECONDARY snapshots and London-close ETF proxies, labelled. Nothing is filled by inference.** KB: `KB-BND-362` (attribution) · `KB-BND-363` (book). Intraday marks are vendor and NOT official; the 9/29 Treasury cells (~16:15 ET) are the grade; **no matrix move on an intraday mark.**

## 1 · Today's leg (9/29), what moved where

| Market | Level | Day change | Basis / time | Source |
|---|---:|---:|---|---|
| US 10Y | 5.285% | **+4.1bp** | TE table ~12:55 ET; ^TNX 5.272 at 11:40 (high 5.289 10:25) | TE (secondary) · yfinance |
| US 30Y | 5.61% | **+5–6bp** | TE page +0.06; ^TYX 5.602 at 11:40 (high 5.614 10:25) vs official 5.56 [9/28] | TE · yfinance |
| US front end | flat | ~0 | SHY +0.01% 12:3x ET; FF strip Oct–Jan −0.2..−0.5bp (rates_context 12:35) | yfinance · CBOT ZQ vendor |
| UK 10Y gilt | 5.41% | **+1bp** | TE page 12:5x (TE table +0.9); IGLT.L 0.00% at 16:00 BST | TE · LSE ETF proxy |
| UK 30Y gilt | 5.86–5.92% | **−3 to +2bp** | two TE snapshots disagree by 6bp; GLTL.L (15+ gilts) −0.26% at London close ≈ +1–2bp at D≈17 [EST] | TE · LSE ETF proxy — **HANS leg owed** |
| DE 10Y Bund | 3.616% | **−3bp** (TE page) / +2.8 (TE table) | conflicting TE snapshots; DBXG.DE (EZ govt 25+) **+0.17%** at Frankfurt close ⇒ long Bunds bid | TE · Xetra ETF proxy — **HANS leg owed** |
| DE 30Y Bund | 3.95% | −1bp | TE page | TE |
| JP 10Y / 30Y | 3.09 / 4.18% | −1bp / flat | TE OTC quotes; **MOF `jgbcme.csv` last row = 9/28 (3.082 / 4.122) — 9/29 not posted at 12:52 ET** | TE · MOF (primary, lagging) |
| AU 10Y · CA 10Y | 5.368 · 3.991% | **+4.5 · +2.4bp** | TE table | TE |
| Brent | ~$103.9 | **−1.3%** (12:1x ET, PROME/BRENT) | my `BZ=F` daily bar prints 96.91 −7.95% = a **roll artifact, unusable** | PROME relay of BRENT; BRENT owns |
| SOFR − IORB | **0bp** | — | SOFR 3.90 [9/28] = IORB 3.90; EFFR 3.88 [9/28]; RRP $0.63B [9/24] | FRED direct 12:5x ET; LIQUID owns |
| MOVE | 106.8 | +4.9% | vendor ^MOVE 12:3x ET; VIOLET owns (two sources disagreed 9/24–25) | yfinance |

**Intraday sequencing (vendor 5-min bars, `^TYX`):** 5.541 at 07:20 → 5.565 at 08:00 → 5.576 at 09:30 → 5.592 at **10:00** → **high 5.614 at 10:25** → 5.61 at 11:00 → 5.60 at 11:30 (index bars end 11:40). TLT continued lower to **77.93 at 12:55** (78.85 at 08:00; −0.84% on the day at 12:5x). ⇒ ~2.5bp of the 30Y move came during European hours, ~2.5bp between the US open and 10:25, and TLT kept selling into midday after Europe closed. **During the London/US overlap (08:00–11:30 ET) the UST long end rose while Bunds rallied and gilts sat still.**

**Data and speakers today:** Conference Board consumer confidence **81.9 (Aug 88.6; expectations 63.6, −5.9) — weakest since April 2014** (Conference Board, released 10:00 ET 9/29; consensus ~89 per Investing.com). JOLTS Aug job openings **7.1M** (Jul revised 7.3M), quits 3.1M, layoffs 1.6M (BLS 10:00 ET). **The 30Y rose ~2bp in the 25 minutes after a growth-negative surprise** — yields rising through bad growth data is the opposite of the hike/growth channel. Fed speakers: "a busy schedule" (Investing.com) — **names and content NOT captured = GAP** (WALTER dark). Wire drivers named for the episode (Bloomberg 9/29 headline, paywalled; Babypips 9/28): fiscal/debt ($40T), "hefty corporate-debt supply" (unquantified), energy — **energy is DOWN today, so not today's channel.**

## 2 · Verdict — PARTIAL

**Today's leg (9/29): US-ORIGINATED.** Not IMPORTING (Europe and Japan were flat-to-lower in yield through the overlap; oil down); not SHARED (no common driver visible — the only global-tape item, Australia +4.5bp, is the Anglo-sphere pattern of 9/28 again, secondary). **EXPORTING is UNTESTED until the Tokyo 9/30 session (JGB cash/MOF CSV) and the European 9/30 open**; the US moved alone on the day.

**Episode (9/22→9/29): UNDETERMINED, and the letter says that is acceptable.** Legs: 9/22–9/23 — no JGB cash session existed (Silver Week, `KB-BND-360`, SAM) ⇒ JGB cash cannot be the source of the first leg; 9/24–9/25 — real-led, 20 of 21bp real (`KB-BND-343`); 9/28 — global US+EU sell-off, wire-attributed oil/Iran + hike odds (`KB-BND-357`, WALTER -021) ⇒ SHARED-branch evidence for that day; 9/29 — US alone. **Evidence that would distinguish the branches and what BOND holds:** intraday sequencing (held for 9/29 only, vendor bars — a 5-min tick series is not a settle) · futures-vs-cash timing (NOT held) · flow data (TIC lags weeks; FR2004 as-of 9/23 prints Thu 10/1) · **the Tokyo 9/30 reaction (the next test, tonight)** · HANS's intraday EU/UK reads (owed). **Daily closes alone cannot establish causation — this page does not try.**

## 3 · The book — what tomorrow's close needs (figures, dates, basis)

| Item | Figure | Basis |
|---|---:|---|
| TLT Sep-30 77P ×15 fees-in breakeven | **$76.89** | TERRY card `AGENTS/TERRY/setups/FLOW-TRIGGER_duration-TLT-put.md` (~76.885 incl. fees) — verified at the artifact |
| TLT mark | **$77.96** [12:49 ET, PROME] · 77.93 [12:55, yfinance] | vendor, MOMENT property — re-pull live |
| Price move to breakeven | **−1.37%** (77.96 → 76.89) | arithmetic |
| TLT duration | **14.78 yrs** [iShares, 9/28] · **14.7–14.8** empirical (TLT %Δ per 1bp DGS30, last 20/40/60 sessions to 9/25; 15.4 over 120) | iShares primary · BOND regression, FRED DGS30 + yfinance closes |
| **20+Y yield move needed by Wed close** | **≈ +9bp** (9.3 at D 14.78) ⇒ 30Y from ~5.61 intraday to **~5.70** | linear, no convexity, DGS30 as the proxy for the 20+Y basket |
| Strike 77.00 touch | ≈ +8bp | same |
| Base rate, 2-session DGS30 ≥ +9bp | **5.2%** (last 1y, n=248) · **8.4%** (last 3y, n=748) · **4.3%** conditional on 4 straight up closes (n=94, ~12y; median next-2 = 0bp) | BOND computation, FRED DGS30 full series |
| **The grind pays zero** | strike 1.2% below spot with 1.5 sessions left; TERRY's own card says the same | TERRY card §Stress |
| TLT Oct-16 82P ×1 | ITM: 82 − 77.96 = **$4.04 intrinsic** at the 12:49 mark; last sale 1 @ $3.60 [9/28] | FORGE `STATUS.md` row 56; card `MGMT-TLT82P-OCT16` (TERRY); Will's A/B/C choice by **Wed 10/14 close** |
| TBT 10 sh | **$42.31 +1.87%** [12:5x ET] | FORGE row 32 (basis $34.65); no management rule |

**What today's official closes would set (FRED close basis, BOND computation):** DGS30 ≥5.59 ⇒ highest since **2004-05-14**; ≥5.60–5.61 ⇒ since **2004-05-13**; ≥5.62 ⇒ since **2002-07-29**. DGS10 ≥5.27 ⇒ since **2002-05-17**; ≥5.28 ⇒ since **2002-05-15**. (Wires saying "since 2007" for the 10Y use intraday highs; the CBOE indices can differ from the Treasury cell by 1–2bp.) DGS30 run ≥5.00 would be **60**; consecutive up closes **5** if 9/29 closes above 5.56.

## 4 · Nearest BOND lines after today — and whether anything is a recommendation

| Line | Where it stands | Distance / date | Owner of the call |
|---|---|---|---|
| **Thesis kill, 5Y dealer leg (WQ-291)** | FR2004 3–6Y as-of 9/23 must be ≥ **$56.586B** (PRE $47.986B, i.e. **+$8.6B**) | prints **Thu 10/1 ~16:15**; grader `analysis/2026-10-01_wq291_grade.py` dry-run | a MET = a rec via TERRY's card + Will; riders travel |
| Kill funding leg | SOFR−IORB **0bp** [9/28]; **quarter-end window is EXCLUDED by the letter** — read 10/1 + two non-Q-end sessions | 9/30 SOFR publishes 10/1 AM | LIQUID reads |
| Row 1 ⇒5 (long-end) | needs a **composition failure on a long-end auction** | 10/7 10Y-R · 10/8 30Y-R (bars frozen 10/1) | BOND grades |
| Row 4 ⇒4 (HY function) | HY OAS **302** [9/28] vs **350** issuance-freeze line | **48bp** away; 9/29 cell posts ~9/30 AM; a revision of 9/28 to ≤300 re-grades ⇒3 | BOND marker; capital = BROCK 10/02 → TERRY + Will |
| T5YIFR >2.50 | 2.35 [9/28] | **15bp** | BOND |
| Credit-equity lead | HY +39 from the 263 trough; needs +75–100 with VIX <20 | 36–61bp | BOND → HENRY |
| Convergence-downgrade counter | **0** | next eligible 10/6 3Y | BOND |
| TLT add-gates (a)(b) | both THROUGH (DFII10 2.90 [9/28]; 9/23 re-arm) | **ADD DECLINED — WQ-280 (Will 9/24); 7/16 NO-ADD** | Will only, by reopening WQ-280 |
| TLT 77P expiry | HOLD to expiry (WQ-168 ④ / WQ-217); harvest ≥$0.3469 fees-in NOT reached | **Wed 9/30**; hard stop for hand sales 15:00 ET (FORGE) | TERRY watches, Will executes |

**Recommendation from BOND today: NONE.** Nothing today crosses a BOND line: the position is HOLD-to-expiry under a standing ruling, adds are declined under WQ-280, the kill's dealer leg is not evaluable until Thursday and its funding leg is excluded at quarter-end by its own letter. The one thing that would become a recommendation this week is a **MET** on Thursday's FR2004 print — and that goes through TERRY's card and Will's [Approve], never from this desk.

## 5 · Gaps, stated
HANS EU/UK rows (owed; secondary used, labelled) · Fed speaker names/content 9/29 · corporate supply figure for 9/29 · JGB 9/29 close at the primary (MOF posts next JST morning) · futures-vs-cash timing (not held) · Brent at a usable vendor quote (roll artifact; BRENT owns).
