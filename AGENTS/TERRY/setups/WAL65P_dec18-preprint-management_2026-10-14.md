# MANAGEMENT CARD — WAL Dec-18-2026 $65P ×4 (Fidelity) — into the Q3 print

**Id:** `MGMT-WAL65P-DEC18`

> **RULED 2026-10-14 21:32 ET — WQ-429 choice A, SELL ×4 before the Mon 10/19 print** (Will verbatim *"Approve 428, 429 and 430"*, recorded by PROME as the recommended A and stated back for correction; record `PROME/proposals/2026-10-14_wq428-430-RULED.md`). **2026-10-15 10:10 ET capture: no WAL order in Pending, ×4 still held** (FORGE D-82) — order state UNKNOWN; fill to be booked from Will's capture. RED's flip (FT-02 ×3 AND LIQ-07 S1): FT-02 **1 of 3** at HY 325 [FRED 10/14]; cannot complete before ~Mon 10/19 publication. Screening 10:38 ET: WAL $73.57, 65P 1.45/2.05 (vendor, not a bid).

**Terry verdict:** CONDITIONAL — lean SELL ×4 before the Mon 10/19 print (§ 8 A). HOLD ×4 through the print is a legitimate alternative and is priced here (§ 8 B). No roll now. The order is Will's (root rule #5).
**Date:** 2026-10-14 Wed, written 21:04 ET (`date`). Screening pulls 20:54–20:55 ET, after the close. Session: PROME spawn (prome-8e, WQ-425), Claude Opus 5.5 (`claude-opus-5-5`), Claude Code.
**Authority:** WQ-425 — Will 2026-10-14 20:49 ET, verbatim *"Approve 425, spawn TERRY for the OZK and WAL cards"* (record `PROME/proposals/2026-10-14_wq425-RULED.md`). C5 held-option card, pulled forward from Wed 12/16. Preparation only: **$0 moved · no order · no new position · no threshold, gate or score moved.**
**Thesis owners:** the WAL desk (thesis v2.4) and REGINALD (regional banks, funding). The line itself is Will's own (bought 10/7, Will-direct); its entry rationale is **UNRECOVERABLE** and is not reconstructed (construction rule #20).
**Supersedes, as this line's management surface:** the 10/7 position note `NOTE-WAL65P-DEC18` (`setups/WAL65P-OZK40P_new-fidelity-lines_note_2026-10-07.md`), which stays as history.
**Data freshness:** WAL **$72.22** (−2.05%), 10/14 close (`fetch.py price WAL`, 20:54 ET). Option quotes: vendor chain (`chain_fetch.py --no-cache`, 20:54–20:55 ET), **SCREENING ONLY**; Fidelity's bid is the price (durable finding 5b). Position: FORGE 10/14 broker receipt, capture time **UNKNOWN**; its $1.75 mark is a mark, not a quote. **Computations** (base rates, event-implied move, post-print model values, roll arithmetic): `research/2026-10-14_WQ425-preprint-cards/` (`OUTPUT.txt` + the four scripts).

## 0. Inputs and hard caveats
- [x] Live price: WAL $72.22 close 10/14.
- [x] Option chain: vendor screening, after hours. Named-leg gate `--legs 65` rc 0. **Thin:** OI 37, 4 traded on 10/14, quote 28% wide.
- [~] Position truth: ×4, basis $682.65 (FORGE 10/14 receipt; the WAL desk image-verified the Fidelity line on 10/14). **Working orders UNKNOWN** ⇒ `[POSITION_STATE_INCOMPLETE]` on orders only.
- [x] Catalyst dates: WAL Q3 release **Mon 10/19 after the close**, call **Tue 10/20 12:00 ET** (issuer IR, verified by the WAL desk 10/9, KB-217). Q3 10-Q: EDGAR from about 10/26, statutory deadline Mon 11/9. Next dividend ($0.42) inferred mid-November from the cadence, not announced.
- [x] Thesis owners current: `AGENTS/WAL/STATUS.md` (10/14 closeout); REGINALD `reports/2026-10-13_WAL_rate-funding-reconciliation.md` and `reports/2026-10-14_WAL_December_outcome_probabilities.md`.
- [x] Challenge consumed: RED CHG-RED-052 (RED re-issued it as **CHG-RED-054** on 10/14 — 052 was already a 9/10 id; every 052 on this card means 054), grade **MODERATE** on this line.

## 1. The line, and what it is not
| Field | Value |
|---|---|
| Instrument | WAL Dec-18-2026 $65 put ×4, Fidelity Traditional IRA |
| Basis | **$682.65** ($1.71 avg), bought 10/7 (Activity) |
| FORGE mark `[10/14 rcv]` | $1.75 ⇒ $700 (+$17.35) |
| Vendor quote, 20:54 ET (screening) | **bid 1.70 / ask 2.25**, mid 1.975; IV 42.5% backed out of the mid (vendor field 43.9%) |
| Distance | strike $7.22 = **10.0% below** spot; breakeven at expiry $63.29 = **12.4% below** |
| Time | 65 calendar days; **46 sessions** from 10/15 through 12/18 (RED counts 45) |
| Forward max loss (rule #20(d)) | the remaining value, **$680 (bid) – $790 (mid) = 1.36–1.58× Will's $500 per-card cap** (6/26 rule) |
| Exercise if held in the money at expiry | sells 400 WAL at $65 = **$26,000 short stock** in an IRA that cannot carry it (handling UNKNOWN, D-60). Sell or roll before 12/18 regardless. |

**Kept separate, not touched:** the **Robinhood WAL Dec-18 $70P ×1** (`TRY-WAL-ROLL70`) and its own guard `GATE-TERRY-ROLL70-EXIT` (WAL official close ≥ $81.90 on three consecutive sessions; **0 of 3** through 10/13 per REGINALD's log, read by the WAL desk 10/14; time stop Fri 12/4). Different account, strike and card; nothing here transfers to it. **L170** (frame before filing for the WAL print) is Will's and the WAL desk's, not this card's.

## 2. The thesis owners, and the disagreement resolved at the artifacts
| Source (read 10/14) | What it says |
|---|---|
| WAL desk `research/2026-10-13_preprint-expectations-gap.md`, line 88 | *"No trade construction referral is justified now."* |
| WAL desk `research/2026-10-14_relative-weakness-interpretation.json`, `recommended_next_steps` item 3 | *"Recommend bringing TERRY's Fidelity65P management review forward before earnings, using current bid/ask, implied volatility, time decay and plausible pre/post-event scenarios."* |
| REGINALD 10/13 reconciliation | *"No TERRY construction recommendation follows."* |

**Found: no contradiction — the two WAL notes answer different questions.** The 10/13 note says the evidence doesn't justify building a new short. The 10/14 note asks for a management review of the put Will already holds, before the volatility drop. This card is that review and proposes no new construction.

**The thesis today:** WAL v2.4 short thesis **ACTIVE**, margin of safety exhausted; resolution = the Q3 print plus the pending $99M appraisal; triage composite 13/25. The WAL desk finds **"NO DEMONSTRATED EXPECTATIONS GAP"** (price ≈ 6.7× FY2027 consensus EPS of ~$11; a credible ~$11 path is the counter-case). REGINALD 10/13: a +100bp gradual rise lifts net interest income +3.2% but broader earnings-at-risk only +0.8%. Securities marks can still cut tangible equity (AFS fair value $667M below cost at 6/30), but rates do not squeeze both earnings and equity. REGINALD 10/14: **25% subjective chance WAL closes below $65 on 12/18** (judgment range 20–35%), and *"no demonstrated put-pricing advantage."*

## 3. The print, measured
**WAL's last 8 prints** (reaction-session close-to-close; `options/partb_realized_moves.py`, re-run 2026-10-14 20:55 ET): **−8.93** · −5.14 · +0.71 · −3.98 · +3.24 · +1.16 · +0.69 · +3.61 (%). Mean |move| 3.43%, root-mean-square **4.30%**, worst −8.93%. Construction rule #18: four regional-bank names, **0 of 32 prints ≥ 10%**. At exactly 10.0% out of the money, **the print alone cannot be this strike's catalyst** (#18(a)). The Dec-18 tenor buys about 8 more weeks of transmission after it.

**What the market prices for the print:** backing a one-day event move out of the at-the-money put IVs (vendor IV fields, 72.5 strike: Nov-20 44.2%, Dec-18 39.9%, Jan-15 37.5%, Mar-19 37.0%) gives **≈ 9–10% one-day standard deviation** across three expiry pairs, **about 2× WAL's realized 4.30%**. The ex-event volatility it implies (≈ 31–34%) is itself ~1.5× WAL's realized 22% (21-day 22.2%, 63-day 22.5%). *(Two-expiry, flat-base-vol estimates on after-hours screening quotes, n = 8 prints. Directional, not a measured constant. The 8-print sample has no crisis print, and March 2023 WAL traded ~−47% intraday.)*

**What the 65P is worth after the print** (Black–Scholes model mid, r 4%, 59 days left at the 10/20 close, post-print IV 36–40% on the 65 strike; screening model, not a bid):

| WAL on 10/20 | −15% | −12% | −8.93% (worst in sample) | −5.14% | −3.98% | 0% | +1.16% | +3.61% | +5% |
|---|---|---|---|---|---|---|---|---|---|
| per contract | $5.45–5.83 | $4.23–4.64 | $3.20–3.61 | $2.19–2.59 | $1.94–2.32 | $1.25–1.58 | $1.09–1.41 | $0.81–1.09 | $0.68–0.94 |
| ×4 | $2,180–2,333 | $1,693–1,856 | $1,278–1,444 | $876–1,034 | $775–929 | $498–632 | $435–562 | $324–436 | $272–375 |

- **Averaged over WAL's own 8 prints:** $618–754 for the four (central, 38% post-print IV: **$685**) against **$790 at the mid / $680 at the bid tonight.** Holding through the print costs about **$105 in expectation** (range $36–172), roughly 13% of the line.
- WAL has to fall **≈ 2–4% on 10/20** for the held put to beat a sale at tonight's mid. 3 of 8 prints did (−8.93, −5.14, −3.98).
- The tail it buys: at the sample's worst print the four are worth about **$1,360 (+$570 vs tonight's mid)**; at −12% about $1,775 (+$985); at −15% about $2,255 (+$1,465).
- A no-move print costs about **$160–290**; a +3.6% print (last July's) about **$350–470**.

## 4. Base rates, like for like
Own reproduction, adjusted daily closes, 46-session windows (WAL/OZK/KRE batch: **2,711 bars each**, 2016-01-04 → 2026-10-14; rule #19 batch control passes):

| Event by 12/18 | History, 5y (ex-2023) | History, 10y | Option-implied (mid IV 42.5% / vendor 43.9%) | REGINALD, subjective |
|---|---|---|---|---|
| Below the **$65 strike** (−10.0%) | 23.5% (21.7%) | 16.8% | 31.0% / 31.7% | **25%** (20–35%) |
| Below **breakeven $63.29** (−12.4%) | 19.0% (17.2%) | 13.7% | 25.9% / 26.8% | not assigned |

Every row puts the market above history and above REGINALD. **No source on file gives this line a pricing edge.** ⚠️ CHG-RED-052's WAL row sets a breakeven base rate (17.9%) beside a strike-level implied figure (30.3%). Like for like, the gap is smaller (see the OZK card § 4), and RED's conclusion stands.

## 5. Day colour (root rule #6)
A put is sold into a **red** session, when it is richest. 10/14 was red for WAL (−2.05%). The rule governs buys, so neither selling nor holding breaks it. But **the proxy and the direct measurement agree tonight**: the convexity in this line is expensive (event ≈ 2× realized; ex-event IV ≈ 1.5× realized). Holding through the print is, in effect, buying that convexity again at that price. If Will sells, the first red WAL/KRE session in the window is the better day. The colour is worth about $0.05–0.15 a contract ($20–60 for four), less than the half-spread.

## 6. Where the line sits in the bank-put book (21 contracts, one bet)
FORGE marks `[10/14 rcv]`, capture time UNKNOWN. These are marks, not bids.

| Line (Fidelity) | Qty | Basis | Value at FORGE mark | Strike vs live spot | Card |
|---|---|---|---|---|---|
| KRE Nov-27 $67P | 4 | $510.65 | $540 | −2.2% (KRE $68.54) | none (FORGE D-77) |
| KRE Dec-18 $60P | 5 (two lots: $513.34 + $878.02) | $1,391.36 | $260 | −12.5% | none |
| KRE Dec-31 $65P | 2 | $337.33 | $308 | −5.2% | `MGMT-KRE65P-DEC31` (stop 12/31 15:00 ET) |
| HBAN Oct-16 $16P | 2 | $191.34 | $170 | expires Fri 10/16 | `MGMT-HBAN16P-OCT16` (WQ-302) |
| OZK Nov-20 $40P | 4 | $322.65 | $120 | −11.0% | `MGMT-OZK40P-NOV20` |
| **WAL Dec-18 $65P** | **4** | **$682.65** | **$700 (33% of the book)** | **−10.0%** | **this card** |
| **Total** | **21** | **$3,435.98** | **$2,098** | | |

Robinhood, outside the 21 (9/29 carry, unverified): WAL Dec-18 $70P ×1 (~$265 derived), KRE Jan-15-2027 $25P ×1 (~$1).

**Independence (RISK_SCORING § 2b):** N_claimed = 6 Fidelity lines (+2 Robinhood). Shared antecedent: regional-bank credit or funding stress does **not** arrive. **N_eff = 1.** The WAL line is the book's **largest single line by mark** and the only one over the $500 per-card cap on its own. Selling it removes WAL's idiosyncratic event exposure. The bet stays on through KRE (RED: the Nov-27 67P is "the best-placed line") and the Robinhood WAL 70P.

## 7. Root rule #7, applied (TERRY is the canonical owner of rules 6–7)
*"Roll duration, don't trim size. Trimming = thesis broken. Rolling = timeline uncertain."* When a live thesis is late, #7 says buy time rather than cut size. **It does not oblige holding a long option through an event priced at about twice its record, in a line over the card cap.** Selling here would not be a response to timing. It would be declining a rich price, with the view still held elsewhere in the book.
⚠️ **The tension, plainly:** the WAL desk holds the thesis ACTIVE, and **this print is its registered resolution event.** Selling gives up exactly the tail the thesis waits for (+$570 at the worst print in the sample). If Will reads #7 as binding here, **B is the rule-consistent choice, at an expected cost of about $105.**

## 8. The three paths
### A — SELL ×4 before the print (TERRY's lean)
**Why:** (1) no pricing edge from any source (§ 4); (2) holding through costs about $105 in expectation on WAL's own record, with the event priced about 2× realized (§ 3); (3) the print alone cannot reach a 10%-out-of-the-money strike (#18(a)); (4) forward risk is 1.36–1.58× the $500 cap (§ 1); (5) the sale is at roughly breakeven; (6) the one bet stays in the book (§ 6). *Good thesis, bad trade is still a bad trade:* this is a reasonable thesis held through its resolution event in an expensive instrument.
- **Window:** Thu 10/15 – **Mon 10/19 15:30 ET** (the release comes after that day's close). Prefer the first red WAL/KRE session.
- **Ticket:** sell to close ×4, Day limit. Start at Fidelity's mid (screening $1.975), step $0.05 toward the bid each session it doesn't fill; floor = Fidelity's live bid. **Never a market order**: 28% wide, OI 37. Check for a working order first.
- **Proceeds** (assumes $0.65/contract commission, before tiny regulatory fees):

  | Fill | Gross | Net | Realized vs $682.65 |
  |---|---|---|---|
  | $1.70 (tonight's screening bid) | $680 | ≈ $677.40 | ≈ −$5.25 |
  | $1.80 | $720 | ≈ $717.40 | ≈ +$34.75 |
  | $1.90 | $760 | ≈ $757.40 | ≈ +$74.75 |
  | $1.975 (screening mid) | $790 | ≈ $787.40 | ≈ +$104.75 |
- **Way back in, named but not proposed:** if the print fires the WAL desk's own **Bear CONFIRM** (WAL-01 office classified > $500M at deck slide 12, or WAL-02 ex-fraud net charge-offs > 40bp), that is a registered trigger. A post-print re-entry at lower volatility would then be a **new deployment on a fresh card** (6/26 rule satisfied by the fired trigger; rule #21's entry economics bind in full). It would cost more than tonight's line after a gap. That is the price of path A.

### B — HOLD ×4 through the print (legitimate alternative)
Choose this if Will is holding the WAL thesis through its resolution. **Expected cost about $105; downside on a no-move or up print about $160–470; upside at the sample's worst print about +$570.**
- **Print-day mechanics:** release Mon 10/19 after the close. Tue 10/20: the volatility drop lands at the open. Don't trade the first 30 minutes (spreads widen); the call is at **12:00 ET**. Read Fidelity's bid after the call.
- **Pre-registered post-print read, by Wed 10/21 15:00 ET** (a re-read whenever the appraisal leg later resolves), keyed to the **WAL desk's own registered carriers and graded by that desk, not by TERRY** (no threshold is set or moved here):
  - **B1 — the thesis's own kill fires:** the WAL desk grades its **bear-medium KILL** as fired: both legs, (a) **0 new office migrations** at deck slide 12 **and** (b) the **$99M appraisal benign** (first of 8-K / Q3 call / 10-Q) ⇒ **SELL ×4** within two sessions of the grade. This is #7's thesis-broken branch. Leg (a) alone, with (b) silent, is **not** a fire (the owner's own no-verdict band) and falls to B3.
  - **B2 — Bear CONFIRM fires** (WAL-01 or WAL-02 as above) ⇒ **HOLD.** P/L harvest suggestion (durable finding 9, not a rule until Will says so): sell ×4 at any Fidelity bid **≥ $3.42** (2× the $1.71 basis). At the sample's worst print the model mid is $3.20–3.61.
  - **B3 — mixed or no verdict** ⇒ HOLD to the C5 sell-or-roll card due **Wed 12/16**. The next carrier is the Q3 10-Q (by 11/9).

### C — ROLL: none now
- A construction rule #21 roll means same WAL, same $65 strike, later expiry. Screening net debits ×4: **Jan-15 65P ≈ $420 natural / $190 mid**; **Mar-19 65P ≈ $920 natural / $710 mid**.
- A net-debit roll is **new capital under Will's 6/26 rule** (fresh capital only on a fired trigger, max $500 per card). **No trigger has fired.** The March roll alone breaks the card cap, and buying any later 65P before the print pays the event premium on the buy leg. Non-Negotiable #6: no roll by hope.
- If Will wants more time on the WAL view, price it **after** the print, when volatility is lower: at the 12/16 C5 card, or on a fired trigger.

## 9. What would change this card
- **Toward HOLD:** RED's flip conditions on the book (FT-02 HY > 320 ×3 **and** LIQ-07 S1 at the 10/16 read). If both land before a sale, the bet's regime case strengthens, and B becomes the stronger choice as a labeled tail bet.
- **Toward SELL sooner:** a WAL pre-announcement, an 8-K on the $99M appraisal, or a red-day bid at or above the screening mid.
- Any change in Fidelity's live quote. Every figure here is screening, and the moment-property numbers (bid, IV, the expected cost) are valid only at their 20:54 ET timestamp (construction rule #14).

## Decision
- [ ] **APPROVE A** — sell WAL Dec-18 $65P ×4 to close before the 10/19 print, per § 8 A
- [ ] **APPROVE B** — hold ×4 through the print, with the § 8 B post-print read by 10/21 15:00 ET
- [ ] **REWORK** with changes: ___

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**
