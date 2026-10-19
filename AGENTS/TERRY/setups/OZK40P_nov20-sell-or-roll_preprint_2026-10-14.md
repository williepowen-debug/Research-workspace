# SELL-OR-ROLL CARD — OZK Nov-20-2026 $40P ×4 (Fidelity) — pulled forward to before the Q3 print

> **CURRENT FOLLOW-THROUGH — 2026-10-19T17:32:27-04:00**
> **October19 follow-through:** captured ×4, exact basis $322.65, displayed value $100. No closing fill supplied; full working orders UNKNOWN. WQ-428 SELL×4 retains the existing October20 15:30 ET backstop before the after-close print; no new approval or extension inferred. Will verifies held quantity, any working order and live Fidelity bid before acting. October19 17:29 screening OZK45.19,40P0.25/0.35,OI2457,width33.33%,DIRINC advisory; not executable. Do not reuse October14 limits or promise a fill. LIQUID's final LIQ-07=S2 (October16 L721 report), so RED's FT-02 AND S1 flip is NOT MET. No roll or replacement capital proposed. Book only an actual filled ticket.

**Id:** `MGMT-OZK40P-NOV20`

> **RULED 2026-10-14 21:32 ET — WQ-428 SELL ×4 before the Tue 10/20 print** (Will verbatim *"Approve 428, 429 and 430"*; record `PROME/proposals/2026-10-14_wq428-430-RULED.md`). **2026-10-15 10:10 ET capture: no OZK order in Pending, ×4 still held** (FORGE D-82) — order state UNKNOWN; fill to be booked from Will's capture. **F1 status 10/15:** RED-FT-02 at **1 of 3** (HY OAS 325 bp [FRED 10/14], SIG-W-20261015-001); third cell earliest = the 10/16 observation, published ~Mon 10/19; LIQ-07 read Fri 10/16. A sale before then forecloses the F1 branch — the ruled default stands. Screening 10:38 ET: OZK $45.91, 40P 0.30/0.60 (vendor, not a bid).

**Terry verdict:** CONDITIONAL — SELL ×4 to close before the Tue 10/20 print (window § 6); no roll. The order is Will's (root rule #5).
**Date:** 2026-10-14 Wed, written 21:04 ET (`date`). Screening pulls 20:54–20:55 ET, after the close. Session: PROME spawn (prome-8e, WQ-425), Claude Opus 5.5 (`claude-opus-5-5`), Claude Code.
**Authority:** WQ-425 — Will 2026-10-14 20:49 ET, verbatim *"Approve 425, spawn TERRY for the OZK and WAL cards"* (record `PROME/proposals/2026-10-14_wq425-RULED.md`). C5 held-option card, pulled forward from Wed 11/18. Preparation only: **$0 moved · no order · no new position · no threshold, gate or score moved.**
**Thesis owner:** the OZK desk (evidence). The line itself is Will's own (bought 10/7, Will-direct); its entry rationale is **UNRECOVERABLE** and is not reconstructed (construction rule #20).
**Supersedes, as this line's management surface:** the 10/7 position note `NOTE-OZK40P-NOV20` (`setups/WAL65P-OZK40P_new-fidelity-lines_note_2026-10-07.md`), which stays as history.
**Data freshness:** OZK **$44.93** (−0.33%), 10/14 close (`fetch.py price OZK`, 20:54 ET). Option quotes: vendor chain (`chain_fetch.py --no-cache`, 20:54 ET), **SCREENING ONLY** — bid/ask age unknowable from the feed, market closed; Fidelity's bid is the price (durable finding 5b). Position: FORGE 10/14 broker receipt, capture time **UNKNOWN**; its $0.30 mark is a mark, not a quote. **Computations** (base rates, event-implied move, post-print model values, roll arithmetic): `research/2026-10-14_WQ425-preprint-cards/` (`OUTPUT.txt` + the four scripts).

## 0. Inputs and hard caveats
- [x] Live price: OZK $44.93 close 10/14.
- [x] Option chain: vendor screening, after hours. Named-leg gate `--legs 40` rc 0 (two-sided, no LOCK/XSD/DEAD/NOBID).
- [~] Position truth: ×4, basis $322.65 (FORGE 10/14; the 10/7 view showed $322.66, D-75). **Working orders UNKNOWN** ⇒ `[POSITION_STATE_INCOMPLETE]` on orders only.
- [x] Catalyst dates: OZK Q3 release **Tue 10/20 after the close**, call **Wed 10/21 08:30 ET** (OZK desk, from OZK's 9/30 release). Dividend $0.49 went ex on 10/13 — already in the price.
- [x] Thesis owner current: `AGENTS/OZK/STATUS.md` (updated 10/12) and `AGENTS/OZK/research/threads/2026-10-12_POST_EXTENSION_REVIEW.md`.
- [x] Challenge consumed: RED CHG-RED-052 (RED re-issued it as **CHG-RED-054** on 10/14 — 052 was already a 9/10 id; every 052 on this card means 054) (`AGENTS/RED/challenges/2026-10-14_BANK_PUT_BOOK_CHALLENGE.md`), grade **STRONG** on this line.

## 1. The line
| Field | Value |
|---|---|
| Instrument | OZK Nov-20-2026 $40 put ×4, Fidelity Traditional IRA |
| Basis | **$322.65** ($0.81 avg), bought 10/7 (Activity) |
| FORGE mark `[10/14 rcv]` | $0.30 ⇒ $120 (−$202.65 / −62.81%) |
| Vendor quote, 20:54 ET (screening) | **bid 0.30 / ask 0.50**, mid 0.40, 50% wide; OI 2,462; 1 traded 10/14; last trade 10/12 15:22; IV 37.0% backed out of the mid (vendor field 39.2%) |
| Distance | strike $4.93 = **11.0% below** spot; breakeven at expiry $39.19 = **12.8% below** |
| Time | 37 calendar days; **27 sessions** from 10/15 through 11/20 (RED counts 26) |
| Forward max loss (rule #20(d)) | the remaining value, $120 (bid) – $160 (mid); inside the $500 per-card cap |
| Exercise if held in the money at expiry | sells 400 OZK at $40 = **$16,000 short stock** in an IRA that cannot carry it (broker handling UNKNOWN, D-60). Moot if sold. |

## 2. What changed since the line was bought
- **10/7, the day it was bought:** OZK's $915M RaDD bridge loan was due Fri 10/9 after a short "Fifth Modification" (Citi called it *"a brief forbearance period"*; WALTER `SIG-W-20261008-017`). That maturity was the one dated, OZK-specific event inside this contract's life besides the Q3 print.
- **10/12, OZK 8-K Item 7.01:** the loan was extended to **December 2029 with $100M of fresh capital** (executed 10/9). The OZK desk: *"RaDD maturity-failure catalyst materially disconfirmed"* (`AGENTS/OZK/STATUS.md` line 5).
- **10/12, the OZK desk's post-extension review**, checked at the artifact (lines 5 and 51): *"This review establishes no compelling, specific near-term downside opportunity."* · *"There is no date-certain RaDD default catalyst left in the November-put horizon."*
- **What survives:** other-credit recognition risk — the $169.3M Boston 10 Prospect nonaccrual, foreclosed property (OREO) sales, special-mention migration, and whether the $121.3M RaDD paydown is re-drawn. The owner calls the Q3 print and the early-November 10-Q *"scheduled potential information catalysts, not confirmed forthcoming loss events."* That is a multi-quarter story.

## 3. The print, measured
**OZK's last 8 prints** (reaction-session close-to-close; `options/partb_realized_moves.py`, re-run 2026-10-14 20:55 ET, unchanged from the 8/13 table): −4.47 · **+9.70** · +0.25 · +0.10 · **−6.89** · +0.06 · −2.06 · −1.26 (%). Median |move| 1.66%, worst down −6.89%, root-mean-square 4.58%. Construction rule #18: the four-name regional-bank envelope is a median 2–3% with **0 of 32 prints ≥ 10%**. The strike needs −11.0% and breakeven −12.8%; no OZK print in the sample reached either.

**What the market prices for the print:** backing a one-day event move out of the Nov-20 and Jan-15 at-the-money put IVs (vendor IV fields, 45 strike: 32.7% and 31.1%) gives **≈ 4.1% one-day standard deviation**, against a realized 4.58%. **OZK's print is not overpriced at the money.** The 40P's extra cost is the deep-wing skew: Nov-20 40P 39.2% vs 45P 32.7% (both vendor fields). *(Two-expiry, flat-base-vol estimate on after-hours screening quotes; directional, not a measured constant.)*

**What the 40P is worth after the print** (Black–Scholes model mid, r 4%, 30 days left at the 10/21 close, post-print IV 32–36% on the 40 strike; screening model, not a bid):

| OZK on 10/21 | −15% | −10% | −6.89% (worst in sample) | −4.47% | −2.06% | 0% | +3% | +9.70% |
|---|---|---|---|---|---|---|---|---|
| per contract | $2.42–2.58 | $1.20–1.38 | $0.71–0.88 | $0.45–0.59 | $0.28–0.39 | $0.18–0.27 | $0.09–0.15 | $0.01–0.03 |
| ×4 | $968–1,033 | $481–554 | $285–351 | $181–238 | $110–156 | $70–107 | $34–59 | $6–13 |

- **Averaged over OZK's own 8 prints:** $110–151 for the four (central, 34% post-print IV: **$130**) against **$160 at the mid / $120 at the bid tonight**. Holding through the print is close to a fair coin on OZK's record: an expected cost of roughly **$10–50**.
- OZK has to fall **≈ 2–4% on 10/21** for the held put to beat a sale at tonight's mid (3 of 8 prints did).
- So the case for selling is **not** mainly the price of the print. It is § 2 (the catalyst is gone) and § 5 (a 37-day put cannot carry what survives).

## 4. Base rates, like for like — and a basis note on CHG-RED-052
Own reproduction, adjusted daily closes, 27-session windows (all three tickers in the batch returned **2,711 bars**, 2016-01-04 → 2026-10-14 — rule #19's batch control passes):

| Event by 11/20 | History, 5y (ex-2023) | History, 10y | Option-implied (mid IV 37.0% / vendor 39.2%) |
|---|---|---|---|
| Below the **$40 strike** (−11.0%) | 13.8% (13.0%) | 13.9% | 17.7% / 19.2% |
| Below **breakeven $39.19** (−12.8%) | 9.2% (8.0%) | 9.2% | 13.6% / 15.1% |

⚠️ **CHG-RED-052's table sets a breakeven base rate (7.9%) beside a strike-level implied probability (18.4%).** Those are different events. Like for like, history is about **0.6–0.75× what the option implies**, not "less than half". RED's conclusion — the line is priced above its own history — survives; the size of the gap is smaller. (Implied figures are risk-neutral and carry a risk premium, so some gap is normal.) Routed to RED by packet.

## 5. Recommendation — SELL ×4 before the print
1. **Root rule #7 — this is the thesis-broken branch, so the exit is a sale, not a trim.** The one dated OZK-specific catalyst that could pay a November put was removed by the issuer, and the owning desk finds no specific near-term downside. Selling all four is consistent with *"Trimming = thesis broken."*
2. **The surviving thesis does not fit the instrument** (construction rules #16 and #18(a)). Recognition risk plays out over quarters. A 37-day put 11% out of the money can only be paid by a print-day gap the sample has never shown.
3. **The book keeps the view.** All 21 bank-put contracts are one bet (§ 9). If Will's view is "regional banks crack," the KRE lines carry it without OZK's single-name squeeze risk: short interest **~16.3% of float** (9/15 FINRA, OZK desk), which is fuel on a clean print.
4. **The stake is small:** $120–160 for all four. This card's job is to stop a dead catalyst from riding into the volatility drop and then to expiry.

**Strongest case for holding, stated fairly:** it is a cheap tail. If Q3 books a large Boston or RaDD loss, a −10% to −15% day turns $120–160 into roughly $480–1,030. On OZK's record that tail is rare (worst print −6.89%), and the owner has priced no such loss.

## 6. Order mechanics (Will's hand; nothing here is an order)
- **Window:** Thu 10/15 – Mon 10/19, by 15:30 ET. **Backstop: Tue 10/20 15:30 ET** — the release comes after that day's close. ⚠️ Tue 10/20 also trades WAL's Monday-evening print, and OZK may move in sympathy, either way.
- **Ticket:** sell to close ×4, Day limit. Start at Fidelity's mid (screening $0.40), step down $0.05 each session it doesn't fill; floor = Fidelity's live bid. **Never a market order** on a quote 50% wide. Check for a working order first.
- **Proceeds** (assumes $0.65/contract commission, before tiny regulatory fees):

  | Fill | Gross | Net | Realized vs $322.65 |
  |---|---|---|---|
  | $0.30 (tonight's screening bid) | $120 | ≈ $117.40 | ≈ −$205.25 |
  | $0.35 | $140 | ≈ $137.40 | ≈ −$185.25 |
  | $0.40 (screening mid) | $160 | ≈ $157.40 | ≈ −$165.25 |
- **Day colour (root rule #6):** sell on a red day for regional banks (OZK/KRE down), when puts are richest. The rule governs buys; a sale on a green day is a lower price, not a break. Here the colour is worth about $0.05–0.10 a contract, **$20–40 for the four**, less than the half-spread.

## 7. Roll — NONE
- A construction rule #21 roll means same OZK, same $40 strike, later expiry. **OZK lists no December expiry**; the next is Jan-15-2027.
- Nov-20 40P → Jan-15 40P ×4 costs a **net debit of ≈ $240 at the natural price / ≈ $170 mid-to-mid** (screening: Jan-15 40P 0.75/0.90). A net-debit roll is **new capital under Will's 6/26 rule** (fresh capital only on a fired trigger, max $500 per card). **No trigger has fired**; the line's dated catalyst was disconfirmed. Buying January before the print also pays the event premium on the buy leg. Non-Negotiable #6: no roll by hope.
- If Will wants OZK exposure for the recognition story, that is a new card after the print, at post-print volatility, on a named trigger. Not proposed.

## 8. Flip conditions — RED's, written on the card before any fill
- **F1 — macro credit joins funding before the sale fills.** RED-FT-02 fires (HY OAS **> 320 on three consecutive sessions**; **0 of 3** at 316 on 10/13, per RED's STATUS) **and** LIQ-07 resolves **S1** at LIQUID's Fri 10/16 funding read. The earliest the third FT-02 cell can exist is the 10/16 observation, published about Mon 10/19. **If both land before Will has sold:** RED's grade falls to MODERATE and the card goes back to Will with a second branch: **HOLD through the print as a labeled, deliberate tail bet** (rule #18: *"a bet that the regime break lands on the scheduled date"*), $120–160 at stake. The default stays SELL unless Will chooses the tail.
- **F2 — the print books a large Boston or RaDD loss.** This can only be known after the print, so it is moot if the line is sold first. If any contracts are still held on 10/21, re-mark at Fidelity's bid and sell into the gap that morning. Don't wait.
- Neither condition moves a threshold. FT-02 and LIQ-07 are RED's and LIQUID's registered lines, read as written.

## 9. Independence (RISK_SCORING § 2b)
| Field | Entry |
|---|---|
| N_claimed | 6 Fidelity bank-put lines, 21 contracts (KRE ×3 lines, HBAN, OZK, WAL), plus Robinhood WAL 70P ×1 and KRE 25P ×1 |
| Shared antecedent | regional-bank credit or funding stress does **not** arrive (REGINALD 10/12 basket study: *"credit cause unproved"*; LIQUID funding check 0 of 3 through 10/13) |
| N_eff | **1.** One view in several hats; OZK adds single-name squeeze risk, not a second view |

This card proposes **no size**: an exit lowers exposure. Book table on the WAL card (`MGMT-WAL65P-DEC18`, § 6).

## Decision
- [ ] **APPROVE** — sell OZK Nov-20 $40P ×4 to close before the 10/20 print, per § 6
- [ ] **REJECT** — hold through the print as a deliberate tail bet ($120–160 at stake; § 8 F1 is the condition under which that becomes the stronger case)
- [ ] **REWORK** with changes: ___

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**
