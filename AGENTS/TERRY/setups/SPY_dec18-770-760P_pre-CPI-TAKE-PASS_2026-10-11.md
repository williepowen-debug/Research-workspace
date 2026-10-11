# TRADE CARD — SPY — pre-CPI downside protection
**Date:** 2026-10-11 13:45:44 EDT
**Setup ID:** TRY-NOTRADE-WQ409-SPY
**Thesis owner:** VIOLET (alert), PROME/Will (commission); TERRY owns construction only.
**Thesis reference:** PROME/inbox/processed/2026-10-10_from-VIOLET_skew-ft10-count-and-fragility-cluster.md §2.
**Terry verdict:** NO TRADE
**TAKE/PASS recommendation:** **PASS.** This is TERRY's recommendation, not Will's decision or VIOLET's PASSED receipt.
**Confidence in trade structure:** Medium on bounded spread mechanics; low on pricing edge.
**Execution status:** BLOCKED. $0 deployed, no order or fill, no paper would-fire.
**Data freshness:** Sunday retrieval of closed-market vendor screening data; option bid/ask observation timestamps UNKNOWN. Last option trades are Friday 10/09. Broker position truth last captured 10/08 intraday, time UNKNOWN.

## 0. Decision and hard caveats

One concrete candidate: **buy 1 SPY Dec-18-2026 $770 put and sell 1 SPY Dec-18-2026 $760 put as one debit spread**. Screening entry cost $262 before commissions, entry loss $263.30 with the explicit $1.30 opening-fee assumption. This caps downside payment at a $10 spread width; it is **bounded downside protection, not uncapped crash convexity**.

PASS because cheap headline volatility does not establish mispricing of these contracts; the alert is OPEN, not a verified capital-deployment trigger; current QQQ disposition and combined risk are unknown. A low absolute premium is not a measured edge. The December spread pays for time past the one CPI event and its tail payout is capped. No calibrated CPI return distribution or forward/option comparison establishes a favorable expected payoff here. No probability, Kelly fraction or EV is invented.

The commission in PROME/proposals/2026-10-11_wq414-409-RULED.md authorizes analysis only. It does not approve this spread, authorize a capital-gate override, or establish a QQQ sale. Sunday is not an entry window.

## 1. Alert and catalyst verification

| Object | Latest source observation | Existing alert letter | Result |
|---|---:|---|---|
| Cboe VIX daily CLOSE | 14.84, 2026-10-09 | ≤16 | met |
| Cboe VVIX daily value | 84.88, 2026-10-09 | ≤90 | met |
| Cboe SKEW daily value | 154.34, 2026-10-09 | ≥140 | met |
| September CPI release | Wednesday 2026-10-14, 08:30 Eastern | near dated catalyst | verified at BLS |

Own primary CSV pulls on 10/11 reproduce VIOLET's 10/09 4/4 OPEN observation. Latest row in all three files is 10/09; there is no Sunday live re-grade. This reproduces the existing alert, not a new threshold or a trade trigger. Source URLs and saved evidence are in research/2026-10-11_WQ409-source-and-intake-receipt.md.

BLS calendar: https://www.bls.gov/schedule/2026/10_sched.htm (October 14 CPI row; calendar says all times Eastern). Recheck the release date before any entry. The pre-CPI entry window ends before 10/14 08:30; do not turn a missed pre-event entry into a post-event chase.

## 2. Exact candidate and quote vintage

**Instrument/expiry:** SPY ETF puts, Dec-18-2026, 100-share multiplier, long 770P / short 760P, one spread. 68 calendar days from 10/11; 67 from Monday 10/12 or 66 from Tuesday 10/13. Construction rule #21's 60–90-day new-deployment band is respected. This is a new deployment, not a roll.

**Vendor pull:** chain_fetch.py --no-cache --json --legs 770,760 at **2026-10-11 13:39:37 ET**. Named legs exist; legs_missing and legs_defective both empty. Yahoo/yfinance is a **MIRROR / SCREENING** source, never the broker execution price (RISK_RULES.md finding 5b). The tool's spot_asof is retrieval time, not evidence of a Sunday trade. Delta/theta unavailable from this feed.

| Leg | Bid | Ask | IV | Volume | OI | Last executed trade, ET |
|---|---:|---:|---:|---:|---:|---|
| Buy Dec-18 770P | $13.26 | $13.30 | 12.85% | 291 | 14,702 | 10/09 16:02 |
| Sell Dec-18 760P | $10.68 | $10.71 | 13.90% | 774 | 20,143 | 10/09 16:08 |

Units: option prices per share; IV annualized; volume/OI contracts. Bid/ask quote timestamps and delay flags are unavailable, so lastTradeDate does not certify quote freshness. **No executable Sunday quote exists.**

Screening buy-at-ask/sell-at-bid debit = 13.30 − 10.68 = **$2.62/share ×100 = $262**. Screening liquidation side = 13.26 − 10.71 = **$2.55/share ×100 = $255**. Round-trip crossing costs $7 before commissions on these snapshots; this is not a fill estimate at Monday's open.

Latest returned SPY price $778.57 (Sunday snapshot 13:40 ET; closed-market screening reference, underlying quote observation timestamp not established here). Long/short strikes are about 1.10%/2.39% below that reference. Snapshot coverage: SPY 60 bars and QQQ 60 bars; exact bar dates are not recorded by the printed snapshot, so no precise event-envelope or percentile claim is made. Trend context: near top of returned SPY range $727.65–779.09; these are vendor reference observations, not registered support/invalidation lines.

The same Oct-16 770/760 spread screened at $0.95 = $95 at the 13:34:53 Sunday pull (770P 1.41/1.43; 760P 0.48/0.49). **Rejected:** only 5 DTE from Sunday, outside the standing new-deployment band. WQ-409 grants no tenor exception. The October price is an alternative check, not a second proposed card.

## 3. Entry and required live refresh

**No entry authorized.** If Will asks to reconsider TAKE inside this same commission, TERRY refreshes the card before any ticket returns to him:

1. TERRY reconciles broker/Will holdings, QQQ sales/exercise outcomes, working orders and available buying power.
2. TERRY obtains VIOLET's latest source alert reading; closed-market 10/09 OPEN cannot be carried as a Monday/Tuesday current reading.
3. PROME/Will establishes the applicable fired capital trigger or explicit hedge approval under the existing gates. OPEN alone is insufficient.
4. TERRY checks live broker SPY and both legs, timestamps, bid/ask size, IV/skew, delta, theta, volume/OI, commissions, spread permission and event expected move.
5. TERRY evaluates executable pricing and the combined book risk. A price below this cap alone does not resolve the missing edge.
6. Will explicitly approves the final two-leg ticket. Analysis approval is not fill approval.

Candidate entry window: regular market Monday 10/12 or Tuesday 10/13, only after the above checks. Prefer **SPY green versus its prior regular-session close** under root rule #6. Friday's color expires with Friday. A red-day purchase needs the pre-fill figures that refute the day-color proxy under RISK_RULES.md §Breaking root rule #6; none is supplied as a standing pass.

**Proposed no-chase limit:** net debit ≤$2.62/share; total opening debit plus actual opening fees ≤$275 for **one** spread. This is a candidate construction limit, not a registered or approved gate. Do not increase it, deepen the strikes, shorten expiry, add contracts, or enter after CPI to rescue a missed quote. No resting order is implied.

## 4. Risk and capital reconciliation

| Field | Candidate economics / condition |
|---|---|
| Defined spread loss | paid debit ×100 + actual opening fees; $263.30 at $2.62 and assumed $0.65 per leg |
| Proposed maximum | $275 including opening fees; below standing $500/card cap in STATUS.md |
| Size | **0 now**; at most 1 spread if separately approved and all blocks clear |
| Risk unit | at screening cost, $263.30 / canonical $250 = 1.0532R; canonical unit remains STATUS.md |
| Expiry arithmetic, not a forecast | break-even 770 − 2.62 = $767.38 before fees; maximum expiry profit $1,000 − $262 = $738 before fees |
| Exit cost | actual closing commissions/slippage separately reduce proceeds; not silently counted as opening premium loss |
| Actual capital moved | $0 |
| Probability/edge/Kelly | unmeasured; no Kelly sizing |

Nominal maximum spread loss assumes the two legs remain intact. SPY is physically settled with early-assignment/exercise risk; short 760P assignment could require buying 100 SPY for **$76,000**, which is not authorized or shown fundable. A debit spread is not permission to carry an assignment. Broker spread eligibility and handling are UNKNOWN. Close both legs together before expiry; never leave an orphan short option. This operational risk is an additional reason to PASS absent broker truth.

**N_claimed=4 alert checks; N_eff=1 view (judgment, not a fitted correlation estimate).** VIX and VVIX are related volatility surfaces; SKEW is a tail-pricing surface; CPI is a calendar fact, not independent evidence of direction. Shared falsifier: CPI passes without a broad downside/volatility repricing. That can also hurt held QQQ and regional-bank puts; this is no demonstrated independent source of book protection.

Last broker snapshot (10/08 intraday, FORGE/STATUS.md and PROME/data/2026-10-08_broker-capture-TRANSCRIPTION.md): QQQ Oct-15 745P ×1 valued $573 and 740P ×4 valued $1,620, **combined $2,193 snapshot mark**. If still held, the candidate adds $263.30 paid risk to that related snapshot exposure: **$2,456.30 mixed-vintage illustration only**, not live forward risk or independent views. At current decision time the combined figure is **UNKNOWN**. Do not use old marks or original basis to size it. The last capture also holds USO/VLO shares and bank/duration puts; current net beta and loss budget are unmeasured. Will's remark that QQQ may have sold establishes no closure, quantity or proceeds. QQQ Oct-09 755P exercise/sale outcome remains UNKNOWN. The 750C sale already booked is distinct.

Capital finding #2's small pre-approved hedge distinction does not help: this hedge has **not** been pre-approved and no underlying portfolio risk amount has been established. No cooldown, capital, X1, size or trigger override is claimed. Existing owner gates retain their meanings.

## 5. Invalidation, harvest and time stop — candidate only

If a later TAKE is approved, these are proposed management terms, subject to final broker pricing:

- **Before entry:** PASS on failed alert, missing trigger/hedge approval, unresolved position truth, quote defects, unconfirmed calendar or fee-inclusive loss >$275.
- **After entry:** the dated view fails when CPI is absorbed without the intended downside/volatility repricing. Exit the event box; do not relabel it a multi-quarter credit trade.
- **Profit harvest:** sell the **whole spread** when broker executable net credit reaches twice the actual entry debit plus total round-trip fees divided by 100. At $2.62 entry and assumed $2.60 round-trip fees, this means credit ≥$5.266 (round the order to a valid broker increment). One spread means no fractional partial harvest. This reaches the profitable zone without waiting for a further price trigger.
- **Loss review:** at executable spread credit ≤half entry debit, close unless the final card explicitly reapproves a hold. Stops may gap; premium remains the loss budget. No automated stop/order is asserted.
- **Hard event time stop:** sell both legs as one spread by **Wednesday 10/14 15:00 ET**, after the 08:30 CPI. If no orderly quote exists, Will contacts the broker; do not infer a fill. The December expiry preserves tenor but creates no license to extend the event view.
- **Roll:** NONE pre-approved. A later same-strike extension requires a fresh Will approval; changing strikes/structure is a new deployment under construction rule #21. USER.md's sell-or-roll practice governs; no hold-to-expiry/lapse rail is offered.
- **Review cadence:** one live refresh before any reconsideration by Tuesday 10/13, then the CPI-day management window only if approved. No new standing monitoring program commissioned.

## 6. Why not / what would change the answer

A green-day, two-sided chain and a small loss budget make a trade executable; they do not create an edge. Selling the deeper wing reduces the skew bill and caps the crash payout. The near expiry better matches CPI but fails the tenor rail; December clears the rail but purchases unused horizon and has muted immediate sensitivity. A low VVIX value does not price a December SPY spread. Four related alert checks do not measure CPI direction or hedge need.

Reconsider only with current broker/position truth, an applicable approved capital path and a direct pricing comparison that supports this structure. A fresh quote is necessary and insufficient. If the evidence remains inadequate by 10/13, keep the PASS recommendation. The eventual Will TAKE/PASS disposition returns through PROME to VIOLET under L413(a); commissioning and this recommendation are not TAKEN/PASSED in VIOLET's ledger.

## 7. Decision

**Recommendation: PASS.** Will's eventual decision is PENDING. PROME registers any eventual capital decision before presenting it. Nothing in this card authorizes an order.

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**
