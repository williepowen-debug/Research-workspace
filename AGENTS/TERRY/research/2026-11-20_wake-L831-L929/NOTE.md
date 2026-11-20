# TERRY — 2026-11-20 wake: D:L831 (Oracle), D:L929 (QQQ 200-day), tape read, Japan Tobacco, inbox drain

**Session:** TERRY, Claude Code, model Claude Opus 5.5 (exposed), laptop. Read the PROME prome-77 task letter at 11:22 ET (`date`, 11:22:11 EST). Root `CLAUDE.md`, `AGENTS.md`, `USER.md`, `PROME/COMPLETION_SPEC.md` and `AGENTS/TERRY/CLAUDE.md` read explicitly; no `AGENTS/TERRY/AGENTS.md` exists. Boot card run 11:22:21.
**Tools used:** Bash, Read/Write/Edit, one read-only Sonnet helper (postmortem list extraction, scratchpad output only), FRED public CSV, `fetch.py`, `chain_fetch.py`, yfinance via `.venv`.
**Missing dependencies (laptop, PROME/MACHINE_LOCAL.md):** Kalshi signed credentials, gh token and CourtListener token are absent; none was needed. DTCC CDS files were not pulled (LIQUID's instrument). Oracle IR pages were not re-tried (403/Cloudflare on 10/25, a blocked site; not evaded). Broker chain: none (vendor screens only, durable finding 5b).
**No order. $0. No trade, spend, paid data or external send.**

## 1. D:L831 — `IDEA-ORCL-PUTSPREAD-OCT23`, entry window ends today

| Question (DOCKET L831) | Answer | Basis |
|---|---|---|
| Condition met? (Oracle-IR-verified fiscal-Q2 date written on the card before any entry) | **NO.** The card never carried a verified date. § 0 still reads "UNVERIFIED — checked 2026-10-25": FAQ index lead December 14, 2026, not verified at a rendered issuer page; Oracle IR returned 403/Cloudflare to automated reads. Not re-checked today: moot, the trigger never fired. | card § 0, § 10; `../2026-10-25_boot/ORACLE_DATE.md` |
| FILLED? | **NO.** No ORCL line in `FORGE/STATUS.md` (11/18 capture, ANVIL 814245c3df); no fill reported. Position state after 11/18 13:21 ET `[POSITION_STATE_UNKNOWN]`. | `FORGE/STATUS.md` grep 11:22 ET |
| State | **NOT FIRED — CLOSED UNFIRED at the window end.** T1 (Oracle 5Y CDS ≥ 350 bp, DTCC disseminated basis) never fired on any read on file: high 342.5 [10/20]; 314 [10/22]; 293 [10/30]; 300 [11/3]; 305 [11/5]; about 318 partial [11/6]; 300–302 [11/10]; about 295 [11/12] (LIQUID DTCC reads; `AGENTS/LIQUID/archive/status_snapshots/STATUS_rotated_2026-11-16.md` l.9). No read after 11/12 is on file in the repo; LIQUID quarantined NT-underlier Oracle spreads (STATUS l.39). Not FIRED-NO-ENTRY: there was no fire to miss. | |
| Equity side | ORCL $104.10 −5.86% (vendor 11:22 ET, intraday); 11/19 close $110.57. The gap the card was built on (credit wide, equity holding ≥ $120) closed from the equity side: ORCL has been under the $120 T2 line since 11/5 and is now under the card's $115 long strike by $10.90. | `fetch.py` 11:22:57 |
| Void lines | CDS ≤ 280: not hit on any read. ORCL ≥ $145 close: not hit. "No green day by 11/20": moot. | |

Write-back: card header state, `SETUPS.tsv`, `setups/INDEX.md`, `TRADE_BOOK.md`, `CARD_LEDGER.tsv`. The 12/4 time stop has nothing to act on.

## 2. D:L929 — `IDEA-QQQ-200D-NOV05`, window ends today (NOT approved, WQ-617 RULED C)

The card's letter (§ 2): **T1 = Cboe VIX3M/VIX ≥ 1.00, live at order time, on a red QQQ session, through Fri 11/20**; credit leg HY OAS first-published ≤ 344 bp at entry; debit ≤ $4.90. **The ratio must be at or above 1.00 (curve back in contango).** PROME's 11:19 pointer (0.92) is consistent.

| Leg | Live at my read | Status |
|---|---|---|
| T1 ratio | VIX3M 28.24 / VIX 30.31 = **0.932** (vendor 1-minute bars stamped 11:08 ET; the bars are about 15 minutes delayed) | **NOT MET** (needs ≥ 1.00) |
| T1 red QQQ | QQQ $627.32 vs the 11/19 close $645.04 (daily bar) = −2.75%, red | met |
| Credit | HY OAS **352 bp [11/19]** (FRED BAMLH0A0HYM2 public CSV, pulled 11:23 ET, first cell for 11/19) vs ≤ 344 | **FAILS**, and stays failed for the rest of the window: the next cell (11/20) publishes Monday |
| Debit | not graded (T1 fails first) | — |

**Verdict: NOT FIRED. CLOSED unfired (DOCKET L929's "otherwise close it").** Nothing comes to Will on this card. Because the credit leg cannot be met before the window ends, the close does not depend on where the ratio goes by 16:00. Card file closed in its header; ledgers updated.

## 3. Tradeability read on today's tape (Will 11/10, 10/20)

**Tape at my read (vendor, intraday, 11:22–11:25 ET unless stated):** S&P 500 7,084.58, 9.39% under its 7,818.93 close of 10/6 (1-year daily bars, 251 bars) · SPY $706.85 −1.26% · QQQ $627.32 −2.75% · RSP $211.52 −0.05% · IWM −0.96% · KRE +0.33% · HYG $76.49 −0.05% · GLD $324.82 −3.09% (gold falling with equities) · ORCL −5.86% · VIX 30.26, VIX3M 28.22 (ratio 0.93, inverted) · HY OAS 352 [11/19, FRED], fifth straight rise from 320 [11/12] · QQQ 200-day 682.01 (200 of 200 bars to 11/19), QQQ 8.0% under it.

**What kind of selloff it is:** cap-weighted and tech-led. QQQ −2.75% while equal-weight RSP is flat and regional banks are up. Credit spreads are widening (HY 352, first print over 350, REG-T-04 at 1 of 3) but the credit ETF is not falling (HYG −0.05%; rates rallying offsets spread). This is the AI-concentration leg selling, not a broad credit event, at today's read.

### 3a. The base-rate check (TERRY's measurement, run today, one specification, not data-mined but chosen today)
First red QQQ close with VIX close > 30 and VIX3M/VIX < 0.95 (episode start = no signal in the prior 20 sessions). yfinance daily bars 2006-07-17 to 2026-11-19, 5,121 bars, adjusted QQQ closes. **17 episodes; today would be the 18th if the 16:00 closes meet it.**

| Horizon | Median QQQ return | Share up | Worst | Best |
|---|---|---|---|---|
| +5 sessions | +2.9% | 76% | −2.8% | +5.9% |
| +10 sessions | +3.6% | 59% | −13.8% | +10.5% |
| +20 sessions | **+6.0%** | **76%** | −16.5% (2008-09) | +18.1% |
| all days, +20 (base) | +2.0% | 67% | | |

Ex-2008/09 (n=15): +20 median +6.1%, 80% up. Episode list: 2007-08, 2007-11, 2008-01, 2008-03, 2008-09, 2009-02, 2009-10, 2010-05, 2011-08, 2015-08, 2018-02, 2018-12, 2020-02, 2020-10, 2024-08, 2025-04, 2026-03. **QQQ +20 sessions ≥ +3.6% in 11 of 17; negative in 4 of 17** (2008-01, 2008-09, 2010-05, 2020-02); 2 near-flat (2009-02 +0.4%, 2011-08 +0.7%).

**Caveats that travel with it:** n=17, overlapping regimes, built today; QQQ data start 2006, so the 2000–2002 tech unwind, the closest analog to an AI-concentration unwind, is not in the sample; the 11/5 study (`../2026-11-05_selloff-read/NOTE.md`) found the opposite at +10 sessions after single days of QQQ ≤ −5% (median −4.2%, 11 episodes), a different condition and horizon; the losers include the credit-led episodes (2008-09, 2020-02). HY OAS history before 2023 is not reachable here (FRED's ICE series is truncated), so I could not condition on credit widening.

### 3b. Answer: one NOT-FIRED idea, and NO CARD on every other angle

**`IDEA-QQQ-CAPIT-NOV20` — QQQ Dec-18 640/650 call spread ×1, NOT-FIRED, NOT approved, Will decides at fire.** Card: `../../setups/QQQ_dec18-640-650C_capitulation-base-rate_2026-11-20.md`. Trigger: today's 16:00 closes meet the measured condition (VIX close > 30 and VIX3M/VIX close < 0.95 on a red QQQ close). **Credit filter (added 11:3x on LIQUID's 11/20 packet):** enter only after REG-T-04 has FAILED on the 11/20 or 11/23 HY cell (a first-published print ≤ 350); LIQUID puts REG-T-04 completing on the 11/23 cell at about 55%, so the filter alone likely blocks entry more often than not. Entry on the first red QQQ session after both, through Wed 11/25, live order-time, broker debit ≤ $4.50, QQQ ≤ $635; void if REG-T-04 fires. Screen at 11:24 ET: 640C $18.31/$18.49 · 650C $14.08/$14.11 ⇒ outer $4.41, mid $4.31 (vendor, screening marks). Max loss $451.30 at the limit (inside $500); max gain $548.70; breakeven $644.50 (+2.7% from $627.32). **X1 CLOSED: any fill goes past X1 by Will's choice.** TERRY verdict CONDITIONAL, confidence Low, edge Small (RISK_SCORING § 2: "watch / tiny only"). **My lean: decline unless Will wants a defined contrarian ticket; ×1 is the most I would take.** Reason for the lean: the sample's losers are the credit-led cases and credit is widening today; no desk holds a bullish view.

**NO CARD (reasons in figures):**
- **More downside (puts) today:** root rule #6 says puts on green days. Today is red with VIX +6.4%; I have no measurement that refutes the proxy (implied vol is higher, not lower: QQQ Dec ATM IV about 36% on the 11:24 screen vs about 28% on 11/5). Not a break; a chase.
- **A credit expression:** the book's credit card already exists: `IDEA-HYG-FOLLOW-NOV05` HYG Jan-15 76/73P ×5, APPROVED FIRED 11/6, fill is Will's hand. Screen 11:25 ET: 76P $0.78/$0.85 · 73P $0.18/$0.31 ⇒ outer $0.67, mid $0.57 vs its ≤ $0.60 broker limit (record only; no prompt, USER.md). A second credit card would share its falsifier (HY path): N_eff 1.
- **VIX/vol long:** VIX 30.26 with the curve inverted is buying vol after the spike: paying up for convexity (the root rule #6 question). VIOLET owns vol. No card.
- **Gold falling with equities (GLD −3.09%):** MIDAS's domain; Will holds GLD by his own hand (`MGMT-GLD-SHARES-OCT24`); a liquidation tape, no owner direction. No card.
- **Oracle −5.86%:** the D:L831 card closed; a new Oracle put now would be chasing a stock 28% under its 10/28 close with Dec puts at high IV. No card.
- **Funding calm:** no card from an absence.

## 4. YURI — Japan Tobacco (TSE 2914), packet 11/19

YURI's evidence (JT filing, issuer-stated): Russia about 25% of adjusted operating profit and about 10% of revenue on the FY2026 revised basis; deconsolidated 06.11; ¥1,377.0bn loss on loss of control; 2026 dividend ¥272 → ¥204.
**Price (vendor):** 2914.T ¥5,857 [11/19 close] → **¥5,265 [11/20, −10.11%]**, volume 26.1M vs about 9–11M on 11/16–11/19. ADR JAPAY $18.55 [11/18] → $15.50 [11/19, −16.4%] → $16.45 intraday 11/20. **YURI's open question "is it already in the price" is answered on the tape: the market took 10–16% off on the first sessions.**
**Read: NO CARD.** JAPAY has no listed options (yfinance `options` empty); a Tokyo-share short is not a vehicle this desk constructs; the remaining catalysts are a Russian decree (No. 302 list removal or a disposal decree) with no date, which is a binary I cannot time; no owner holds a direction on JT's equity. Logged as information. Changes if: a decree on the JTI companies is published, or JT's February FY2026 results guide 2027 off the "above 10% ex-Russia" line.

## 5. Inbox drain (17 packets; census 17 top-level · WALTER/ 0 · WILL/ 0)

| Packet | Disposition |
|---|---|
| PROME 11/16 postmortem thesis grades and close prices | **DONE** (§ 7): list, 12 owner asks, 3 prices found, 6 UNAVAILABLE, template line. Owner answers are recorded when they arrive. |
| PROME 11/17 seven more close-price lines | **DONE** (§ 7, Table 2). |
| YURI JT and bridge | § 4, NO CARD. Bridge/truce: no oil card (products lean is BRENT's; BRENT reads today). |
| REGINALD HY 347, bank side absent | Consumed: bank leg absent through 11/18 (BANK-ABSENT); used in § 3. `TRY-COND-KREADD` stays NOT ARMED. NO CARD. |
| REGINALD REG-36 → REG-37 | Consumed: cite REG-37 (HY > 350 three straight by 12/11, 30%). The new idea's void line names REG-T-04, REGINALD's gate, not the prediction row. |
| HENRY D:L823 KRE/QQQ alarm | Consumed: UNRESOLVED (resolves 2027-01-20 to 02-18); HENRY retired "credit leads equity by 2–3 sessions". NO CARD. |
| HENRY WQ-696 gamma trough | Consumed: vol-timing, no direction; HEN-64 (SPX close < 7,100 on any session 11/19–11/25, 0.40). S&P 7,084.58 intraday today: under 7,100, not a close. Used in § 3 (expiry today removes about 40% of the short gamma). NO CARD. |
| RED S68 | Consumed: FT-06 exit, no implication; CHG-057 MODERATE. NO CARD. |
| VULCAN Anthropic / AMD / Nvidia MoUs | Consumed: no implication on items 1 and 3; AMD Hunterbrook: a disclosure overhang with no dated catalyst (VULCAN-193 P=0.20 by 2/28/2027); a short single-name put after a −9.75% day is a chase on a red day (root rule #6). NO CARD. |
| GIBBS JPM vendor / Fed FSR / ECB-BoE | Consumed: no implication. NO CARD. |
| CYPHER JPM vendor / TruStage / N-able | Consumed: no implication. NO CARD. |
| HANS ECB NBFI probe / TTF | Consumed: HNS-16 (TTF close ≥ EUR 100 by 12/30, 35%) is HANS's projection; no listed liquid TTF vehicle this desk uses; no card asked. NO CARD. |
| OSPREY Russian refining 400 kt/d | Consumed: products over crude; BRENT prices it today. NO CARD. |
| AEOLUS Lake Mead | Consumed: no liquid vehicle; 12/08 MWD vote is the dated water test. NO CARD. |
| CORAL flood of record (Brevard) | Consumed: no implication; SBCF exposure small in Brevard. NO CARD. |
| CORAL South Florida storms | Consumed: no implication. NO CARD. |
| FALCON Riyadh PIF tower | Consumed: no oil asset hit. NO CARD. |
| **LIQUID 11/20 HY 352 broadening (landed 11:2x, read 11:30)** | Consumed: broad price-of-risk repricing (BB +26, BBB +10, IG +8 since 10/28; B 380; CCC 1,361), funding unchanged; LIQUID's projection REG-T-04 completing on the 11/23 cell about 55%. **Changed the new idea: credit filter added (§ 3b).** No funding card (nothing in funding moved). HYG card unchanged. |
| LABOR 11/20 Florida October UR 4.3% | Consumed: no implication; no live Florida-credit card to weaken. NO CARD. |
| **WALTER FLASH SIG-W-20261120-001 (BOARD, TERRY on action; doorbell 11:30 ET)** | Read whole 11:30 ET: VIX at the 30 line, AI/chip selloff (NVDA −6.38%, AMD −10.6%, SMH −7.0%), no single sourced cause, gold −3.8%, REG-T-04 day 1 of 3. This § 3 is the tradeability read. Logged `acted` in `board_log.tsv`. |

All 19 packets (17 from the census plus LIQUID and LABOR of 11/20) are filed to `inbox/processed/`.

## 6. NEXUS_BRIEF wording (WQ-719 A, WQ-721 A)

TERRY has no `NEXUS_BRIEF.md`, and neither `CLAUDE.md` nor `CLOSEOUT.md` says a brief is rewritten every session or "even no-change" (grep 11:26 ET: no match). **No charter line to change; nothing changed.**

## 7. Postmortem list (PROME 11/16 + 11/17 packets, D:L1170 item 1)

All four steps done this session (owner answers pending):
1. **List:** `POSTMORTEM_LIST.md` (this folder): 25 dated postmortem entries. Thesis graded by the owner desk: 2 (FIRE-005, FIRE-007, both SAM). Graded by TERRY only: VIOLET-VIXCS, WILL-QQQ-VFADE. Deliberately not graded, owner named: 9 cards. Owner Will (no desk grade): the QQQ put cluster, VFADE and the October QQQ cohorts. No owner stated: RESHAPE-BC, USORH and the 10/12–10/29 bookkeeping entries (recorded "no thesis owner of record"; nobody asked).
2. **Owner asks sent (12 packets, one per desk):** BRENT (USOARM, XLE65C, REFINER, FIRE-006) · REGINALD (WAL Sep-18 pair, ROLL70, HYG-BDC) · WAL (ROLL70, WAL Sep-18) · BOND and LIQUID (FIRE-004) · HENRY (REFINER, PUTWALL) · VULCAN (PUTWALL) · DEWEY and BROCK (HYG-BDC) · VIOLET (VIXCS) · RED and FALCON (FIRE-006). The ORCL card's thesis (PROME ELLISON) is asked in the PROME packet.
3. **Close prices:** 3 of 9 found as broker rows already in the record (QQQ 719P +$208.99 10/20; QQQ 715P Oct-22 sold $7.31, +$730.32; CRWV 56P +$88.34 10/23), verified by TERRY at the cited lines; 6 UNAVAILABLE with the missing row named (one of them, the second PUTWALL 690P, is the audit's other "missing" line). Written to `POSTMORTEMS.md` (2026-11-20 entry) and the three `setups/INDEX.md` cells. Bonus: the WAL Sep-18 pair has broker EXPIRED rows (9/21 "as of 2026-09-18").
4. **Template line added** to `POSTMORTEMS.md` § Template: "Thesis grade (owner desk)" row.

## 8. Combo reviews due 11/20 (SIGNALS.tsv rows 41–45)

All five kept with a new dated member or a stated reason; next review Fri 12/4. Credit-following: HY 343 → 347 → 352 [11/17–11/19], bank leg absent (REGINALD), HYG flat. Rebound-breadth: QQQ −2.75% vs RSP −0.05% today, the tech-led shape again; the 200-day card closed unfired. Bear-premise-erosion: kept (members 11/16–11/17 are new since the 11/13 review, so the drop condition is not met); REGINALD BANK-ABSENT added. Vendor-vs-broker: no broker same-timestamp quote yet; today's QQQ chain printed DIRINC on 9 rows. Card-vs-hand: HYG fired 11/6, no fill known after 14 days.

## PROJECTION (TERRY's judgment, not evidence; moves no score, gate or trade)

- **What I expect:** a tech-led drawdown whose next 20 sessions are more likely up than down from today's close: QQQ above $627.32 on Fri 12/18, about 60% (subjective; below the 76% sample rate because credit is widening and the AI-unwind regime is missing from the sample).
- **The meaningful alternative:** credit confirms (REG-T-04 fires by 12/11, REGINALD's REG-37 30%) and the drawdown runs in HENRY's follow-through case; then the rebound idea voids before entry or loses.
- **Horizon:** 20 sessions to 12/18; the credit test by the HY prints published 11/23 and 11/24.
- **What would change my mind:** HY first-published over 350 on 11/20 and 11/23 (REG-T-04), or a hyperscaler capex cut or AI-lender pull (VULCAN's tell).
- **Registered:** the trigger forecast for the new idea only (CALIBRATION.tsv, "today's closes meet the condition", p 0.50 subjective). The QQQ-above-$627.32 view is **unscored** (no row).
