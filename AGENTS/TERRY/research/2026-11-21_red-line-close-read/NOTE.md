# TERRY — tradeability read on the Friday 11/20 close (PROME prome-77 late-wake letter)

**Written:** 2026-11-21, started 18:15 EST (from `date`) · TERRY, Claude Code, Claude Opus 5.5, laptop · **NO ORDER. $0. Nothing here is approved.**
**Basis:** vendor (yfinance) daily bars for Friday 11/20, pulled 18:16–18:19 EST Saturday; markets closed. Every option price below is a **vendor SCREEN read Sat 11/21 18:17–18:19 EST, last trades Fri 11/20 ≤ 16:14 ET** — not a live quote, not a broker quote (durable finding 5b). FRED HY and VIXCLS for 11/20 not posted at 18:19 EST.

## 0. Answer in one screen

| Item | Verdict | Why, in one line |
|---|---|---|
| (1) HENRY: S&P closed under the red line, dealers short gamma ~6,400–7,100 | **NO CARD** | His finding is "big moves both ways". Options already price that: the SPY two-week straddle implies about **35.8%** annualised volatility against **27.0%** realised over the last 10 sessions. A straddle costs **$3,754** per contract, 7.5× the $500 default. No two-sided structure fits $500. |
| (1b) Direction off the same finding | **NO CARD** | A short now is late (−11.62% from the 10/6 peak), Friday was a red day (root rule #6: no puts on red days, no refuting measurement), and it would stack on the falsifier Will already carries (KRE and WAL puts, the approved HYG card). The long side is WQ-724, which stays with Will untouched. |
| (2) VULCAN: Reuters says SEC staff are examining Nvidia's accounting; 10-Q unfiled, due 12/04 | **NO CARD** | No desk owns a direction (VULCAN: "no investment implication from my letters"). NVDA is −44.53% over 30 sessions and −14.01% Friday. Its options imply about 85–88% volatility against 69–73% realised. The dated event (10-Q by 12/04, or a late-filing notice) can push the stock either way. The $500-sized put spread that fits is a bet on the bad branch. |
| VULCAN memory divergence (MU into its ~12/16 print) | **NO CARD this session** | The print date comes from third-party calendars, not Micron's own announcement (option-specific rule: event dates from the issuer only). MU is −13.89% Friday and −39.88% over 30 sessions. A call card would also overlap WQ-724 (same falsifier: AI chips keep falling). |
| HOMER builders and FHA | **NO CARD** | The Toll and Lennar print dates are not announced. HMI 25 has been public since 11/17. Friday was red. |
| BRENT diesel crack | **NO CARD** | BRENT offers no idea. Will's two VLO shares are his own hand (FORGE D-78); held-line card commissions are paused (C5, 10/20). |
| CARL (consumer side of the red line, arrived 18:35) | **NO CARD now** | CARL's own trigger needs two legs: Michigan's December preliminary (12/04) AND AXP's Q4 billed business at about +4% or less (late January). Neither has fired. A premium-versus-trade-down pair does not fit a $500 defined-risk card, and CARL flags it as partly priced (WMT +1.52%, RCL −2.20% on 11/20). Revisit at the 12/04 print. |
| FALCON (Bahrain industrial site hit 11/21, arrived 18:40) | **NO CARD** | No energy asset established, no force majeure, no letter moved. If Bapco confirms a Sitra outage, it is a products and crack story that is crude-bearish at the margin, and BRENT owns that leg. Overlap: Will's USO 30 sh (crude) and VLO 2 sh (crack) would move in opposite directions on it. Nothing to construct before the site is named. |
| CYPHER, HAWK, YURI, NEXUS | Agree: no implication | Each owner says none, and I found no instrument they missed. NEXUS's honest form is credit-tier persistence (PRED-51), which is the approved HYG card's ground. |

## 1. HENRY's red line and negative gamma: measured

**Tape (vendor closes 11/20):** S&P 6,910.39 (−3.70%); SPY $689.81 (−3.64%); QQQ $608.45 (−5.67%); NVDA $125.53 (−14.01%); MU $594.51 (−13.89%); HYG $76.33 (−0.26%); VIX 35.89, VIX3M 30.94 (ratio 0.8621), VIX9D 40.72. HY 352 bp [FRED 11/19]; 11/20 cell posts about Monday.

**Realised volatility.** Close-to-close log returns, annualised ×√252, from one 90-bar vendor pull ending 11/20. Bar counts are stated per construction rule #19.

| | 5 returns | 10 returns | 20 returns |
|---|---:|---:|---:|
| SPY | 20.3% | 27.0% | 26.5% |
| QQQ | 37.5% | 41.2% | 40.5% |
| NVDA | 90.5% | 73.1% | 69.0% |

SPY's last 10 daily moves: +2.34, −0.37, +1.31, −0.35, −0.36, −1.93, −1.02, −0.31, −1.98, −3.71 (%).

**Implied volatility, from prices.** The vendor's weekend IV fields are inconsistent (SPY Dec-4 690 call 38.92% against the 690 put 30.74% at the same strike), so I use prices, not those fields.

| SPY structure (screen, last trades 11/20 ≤ 16:14 ET) | Bid / ask | Cost ×1 at ask | Reads as |
|---|---|---:|---|
| Dec-4 690C + 690P straddle (9 sessions; Thanksgiving 11/26 closed, 11/27 half day) | C 20.70/20.88 · P 16.35/16.66 | **$3,754** | mid 37.30 = 5.41% of spot ⇒ about **35.8%** annualised (straddle ≈ 0.8·σ·√T, T = 13/365); break-evens at expiry about $652.27 / $727.35 |
| Dec-18 690 straddle | C 25.50/25.91 · P 21.42/21.81 | $4,772 | — |
| Dec-4 650P + 730C strangle | P 6.61/6.81 · C 3.32/3.46 | $1,027 | needs about ±7.3% by 12/4 |
| Dec-4 640P + 740C strangle | P 5.31/5.50 · C 1.62/1.74 | $724 | needs about ±8.3% by 12/4 |
| Dec-4 640P alone | 5.31/5.50 | $550 | a direction bet, not a vol bet |

VIX options (Dec-16) and XSP options showed **zero bid and zero ask on every strike** on the weekend vendor feed (`DEAD`). They cannot be screened until Monday. XSP would not help anyway: XSP is SPX ÷ 10 ≈ 691, so its straddle costs about the same as SPY's.

**Read.** HENRY is right that the options book offers no cushion. But "realised volatility stays high" pays only if realised volatility exceeds what is already priced: about **36%** for the next 9 sessions, against **27%** over the last 10. That has happened only in the escalation branch, which VIOLET's surface already prices as acute (Dec VIX future 28.46 against spot 35.89). On the $500 default, the only structures available are out-of-the-money wings ($724–$1,027 for both sides) or a single wing, which is a direction bet. Root rule #6's own question is "am I paying up for convexity?" The direct measurement answers **yes**, by about 9 volatility points. **NO CARD.**

**What would make it a card (NOT-FIRED condition, not a card):** the SPY two-week at-the-money straddle prices implied volatility **at or under 10-day realised**, measured at a close, while the S&P stays under about 7,400 (HENRY's negative-gamma zone). That would mean VIX near 27–28 with daily moves still around 1.7% or more. Even then a SPY straddle is about 7× the $500 default, so it is Will's call per card, never pre-approved. I am not registering a forecast for this condition.

**Direction.** HENRY's tail branch (S&P close under 7,037.04 **and** REG-T-04, meaning HY over 350 on three first-published closes) already has its price leg met. Its credit leg grades on the 11/20 cell (posts about Mon 11/23) and the 11/23 cell (about Tue 11/24). If it fires, the expression that already exists is the **approved HYG card** (`IDEA-HYG-FOLLOW-NOV05`, ×5 Jan-15 76/73P, limit ≤ $0.60, window to 12/4, Will's hand). Screen at 18:19 EST: 76P 0.85/1.10, 73P 0.04/0.68 (`NONMONO`, 73P spread 178% of mark); outer $1.06, mid about $0.62. Recorded only; this is not a prompt. A second credit-tail card would double the cluster that has no cluster cap. HENRY's reflex branch (close back over 7,300 with VIX under 25) would buy calls on a green day after the rally. That is a chase under root rule #6, and it overlaps WQ-724.

## 2. VULCAN: Nvidia, the SEC report and the 10-Q

**Evidence (VULCAN KB-VULCAN-473, KB-456; not re-verified by me):** Reuters 11/20 says SEC enforcement staff are scrutinising potential accounting issues; it is the second origin after the WSJ's 11/17 civil-probe report, and a wider reported scope. No formal order, subpoena or Wells notice appears in any page VULCAN read; the SEC declined comment and Nvidia did not respond. 10-Q not on EDGAR at 17:54:35 ET 11/21. Nvidia's own words: "in the coming weeks". Deadline about **12/04** by VULCAN's arithmetic (period end 10/25 + 40 days); a Form 12b-25 extends it to about **12/09**.

**NVDA Dec-11 screen** (first expiry past both dates; last trades 11/20 ≤ 16:00 ET):

| Structure | Bid / ask | Worst-case debit ×1 |
|---|---|---:|
| 125 straddle | C 10.30/11.35 · P 9.50/10.25 | $2,160 (17.2% of spot) |
| 125/110 put spread | 9.50/10.25 · 4.50/5.00 | $575, over the $500 default |
| 115/105 put spread | 5.85/6.40 · 3.40/4.00 | $300, max value $1,000 |

Vendor IV at the money is 84.7–88.2%. The 120P is crossed (`XSD`) and the 135P and 140P are locked (`LOCK`) on this feed, so the chain is unreliable for any strike there.

**Read.** Four reasons, in the order they bind. (a) **No owner direction.** VULCAN says its letters imply nothing, and the reported probe is unconfirmed by the SEC or by Nvidia. (b) **Late.** NVDA is −44.53% over 30 sessions and −14.01% on the report day; a put now sells into a move that has already happened. (c) **Paying up.** Implied volatility of 85–88% sits above 69–73% realised over 20 and 10 sessions (90.5% over 5), and Friday was a red day; root rule #6 is unrefuted. (d) **The dated event can go either way.** A clean 10-Q by 12/04 is a relief catalyst; a 12b-25 or a restatement is a gap down. A put spread ($300 at 115/105) is a bet on one branch with no owner behind that branch. **NO CARD.**

**What would make it a card:** a confirmed formal step (an SEC statement, a Wells notice, or an Nvidia 8-K or 10-Q disclosing an investigation, a restatement or a material weakness), or a 12b-25 filing, **read by VULCAN** into a direction. Then TERRY builds a defined-risk structure on a day that passes root rule #6, with the strike matched to the measured move (construction rule #18). The reverse branch (a clean 10-Q) would be a call idea on a red day, and it would overlap WQ-724.

## 3. Overlap against existing cards and Will's held positions

Will's holdings are taken from the FORGE 11/18 Fidelity capture (intraday, ANVIL-reconciled) and the Robinhood 11/10 view. ⚠️ Nothing newer is in the record, and I infer no disposition.

| Exposure | Shares a falsifier with |
|---|---|
| KRE puts (Nov-27 70P ×2, 68P ×10, 67P ×4; Dec-18 60P ×5; Dec-31 65P ×2), WAL Dec-18 65P ×4, approved-unfilled HYG card ×5 | any index-short or credit-tail card: the shared falsifier is "credit and banks do not follow the equity break" |
| WQ-724 `IDEA-QQQ-CAPIT-NOV20` (with Will; not re-graded, not re-priced here) | any reflex long, any NVDA or MU call idea: the shared falsifier is "AI chips keep falling" |
| Will's short-dated NVDA Nov-18 155P, QQQ Nov-18 655P and Nov-19 648P (FORGE D-103; expiries before the 11/20 close, disposition unseen) | history only; any NVDA put would repeat the same hand |
| GLD 18 sh, USO 30 sh, VLO 2 sh | none of the ideas above |

Since every read is NO CARD, nothing new is added to either cluster.

## 4. What I want to see Monday before any of this is worth Will's time

1. **The HY print.** FRED's 11/20 cell (about Mon 11/23) and 11/23 cell (about Tue 11/24). If both are over 350, REG-T-04 fires: credit is joining, HENRY's tail branch is live, and VIOLET's "acute, fading" reading starts to fail. At 344 or under, credit is not following and the equity break stays an equity unwind.
2. **The open against 6,910.39 and 7,037.04.** HENRY puts a move over 2% either way at about 1 in 3 (unscored). A gap back over 7,037 makes the red line a one-day break; a gap under 6,885 (Friday's 0DTE low, a Seeking Alpha title) puts the 6,700 test (HEN-65) in play.
3. **VIX and the term structure.** The ratio was 0.862 Friday. The vol idea above only becomes worth Will's time if implied volatility falls toward realised while daily moves stay large.
4. **NVDA.** Any weekend SEC or Nvidia statement, an 8-K, the 10-Q, or a 12b-25 on EDGAR, and the open against $125.53.
5. **Broker screens.** The weekend vendor IV fields are broken, and the VIX and XSP chains show zero bid and zero ask. Any number that matters on Monday comes from the broker at the time it is used.

## 5. Calibration and postmortem duties done this session

- **CAL-0009 graded, outcome 1 (TRUE), Brier 0.25.** The row forecasts the trigger only, not the trade: VIX 35.89 > 30; VIX3M/VIX 30.94/35.89 = 0.8621 < 0.95; QQQ $608.45 < $645.04 (vendor daily bars re-pulled 18:19 EST; VIOLET's Cboe History reads 35.89 too). The FRED VIXCLS cross-check was not posted at 18:19 EST. ⚠️ This records my forecast's outcome, nothing more. `IDEA-QQQ-CAPIT-NOV20` is not re-graded or re-priced, its credit filter (11/20 and 11/23 HY cells) is unread, and no fire decision is made. That stays with Will (WQ-724).
- **Owner thesis grades recorded in `POSTMORTEMS.md`:** BRENT ×4, HENRY ×2, VULCAN ×1, VIOLET ×1, FALCON ×1 (TRY-FIRE-006 RIGHT on the strand, observability caveat). Five of the 12 asked desks have answered; REGINALD, WAL, BOND, LIQUID, DEWEY, BROCK, RED and PROME (ORCL) are still owed.

## PROJECTION (TERRY's judgment, not evidence; moves no score, gate or trade)

- **What I expect:** over the 9 sessions to 12/4, SPY's realised volatility comes in **under** the roughly 36% the Dec-4 straddle prices. About 65%, subjective. Why: implied sits about 9 points over the last 10 sessions' realised; VIOLET's analogs show VIX lower 17 sessions later in 5 of 7; HENRY puts a close back over 7,037 at about 65%.
- **The meaningful alternative:** credit joins (REG-T-04 completes on the 11/20 and 11/23 cells; NEXUS about 55%, unscored), and realised volatility runs above implied in the tail. A second leg in a book with no cushion to about 6,400 is exactly that case.
- **Horizon:** to Fri 12/4. The credit test comes with the prints published about 11/23 and 11/24, and Nvidia's 10-Q deadline (about 12/04) sits at the end of it.
- **What would change my mind:** both HY cells over 350 together with a Monday close more than 2% lower; or an SEC or Nvidia formal step.
- **Unscored.** No CALIBRATION row: it attaches to no card, and I keep it as an outlook.

## 6. Inbox, BOARD and small items

- **Inbox drained: 14 of 14 to `processed/`** (the 12 counted at launch, plus CARL and FALCON, which landed at 18:35 and 18:40). Each one was read in full before filing.
- **BOARD scan run, 13 new since SIG-W-20261120-004, 1 logged.** The new signals are 11/20 -005 to -013 and 11/21 -001 to -004. Only 11/21 -001 (LATE FLASH, VIX +5) names TERRY in its action line; it is logged as acted.
- **Small items (`SIGNALS.tsv`, combo rows):** dated members added to credit-following, rebound-breadth, bear-premise-erosion and vendor-vs-broker. Poland and Kyiv (HAWK, YURI) match no TERRY theme, and the owner desks hold them.
- **NEXUS_BRIEF lines (WQ-719 A, WQ-721 A):** this desk keeps no NEXUS_BRIEF, and neither `CLAUDE.md` nor `CLOSEOUT.md` carries an "every session" or "even no-change" brief line. No charter change made.

## Missing dependencies and limits

Laptop: Kalshi, gh and CourtListener credentials are absent (not needed here). CME is IP-blocked (not needed). The Cboe chain is unavailable to this desk; I used the vendor screens above. The vendor's weekend IV fields are broken, and the VIX and XSP chains are `DEAD`. `RISK_RULES_CONSTRUCTION.md` was not read in full this session because no actionable card was built (BOOT step 7 binds at card build); I applied rules #14, #18 and #19 by their hot-index triggers.
