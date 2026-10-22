# TRADE IDEA — QQQ Nov-20 690/670 put spread — equity downside while dealer gamma is negative
**Setup ID:** `IDEA-QQQ-PUTWALL-OCT22`
**Terry verdict:** CONDITIONAL — **NOT-FIRED**; unapproved proposal. Nothing is approved in advance.
**Prepared:** 2026-10-22 13:29 ET (clock read from `date`), TERRY (Claude Opus 5.5, Claude Code), PROME spawn on WQ-487 A. Commission basis: Will 2026-10-20 11:50 ET, verbatim *"we can loosen rules for trade ideas"* (`USER.md` § Trade ideas loosened).
**Thesis owners (evidence, not a TERRY thesis):** HENRY (dealer gamma, put wall: SIG-W-20261022-004); VULCAN / LIQUID (AI tape and IG-tech credit: SIG-W-20261022-006); LIQUID (HY >320 rung MET 3/3, X1 CLOSED: SIG-W-20261019-003); WALTER follow-ups (FINRA margin debt $1,480,054M Sep-26, CCC effective yield 18.01% [10/20]: SIG-W-20261022-016); HENRY (Asia: CSI 300 20% below its June peak: SIG-W-20261022-002).
**Data freshness:** spot and chain pulled 13:26–13:28 ET 10/22 (`fetch.py price`, `chain_fetch.py --no-cache`). Vendor option quotes are **SCREENING marks, not fill prices** (durable finding 5b): the order is priced on the broker chain. Position truth: `FORGE/STATUS.md` mirror of Will's 11:01 ET capture (ANVIL `ec5a7058b`), a mirror, not the broker.

> **CLOSE GRADE 2026-10-22 (TERRY, PROME spawn prome-e7, DOCKET L803 ①; written 19:3x ET from `date`): T1 NOT FIRED.** SPX **cash close 10/22 = 7,663.43** (vendor daily bar; 390 one-minute bars 09:30–15:59, last bar 7,663.45; prior close 10/21 7,757.17 ⇒ −1.21%). 7,663.43 ≥ 7,650.00 by **13.43 points (+0.18%)**. The session low **7,637.36** traded under the line intraday; an intraday print is not a close. The void line (SPX close ≥ 7,750 before an order) is not met either. **State: NOT-FIRED, still armed** — T1 grades again at each cash close; the entry window (first green QQQ session after T1) runs to Fri 10/30. HENRY reads the same close for L787 (one figure, two consumers); if HENRY's graded close differs, HENRY's packet governs the correction. QQQ closed $704.47 (−2.86%, red), so the put-entry colour would have been wrong today anyway. No Will ruling on WQ-490 as of 19:3x ET (`PROME/WILL_QUEUE.md`). Evidence: `../research/2026-10-22_L803-close-grade/CLOSES.json`.

## 1. One-line setup
Buy a defined-risk Nov-20 QQQ put spread if the S&P 500 closes below HENRY's put-wall break line, entered on a green day, to own a falling-market leg for the FOMC (10/28) and election (11/3) window while dealers are positioned to amplify moves.

## 2. Trigger state, in figures (NOT-FIRED)

| Leg | Line | State at 13:26 ET 10/22 | Status |
|---|---|---|---|
| **T1 — put wall broken (the trigger)** | SPX **cash close < 7,650.00** (HENRY: "a cash close under ~7,650 would be the clean break at both horizons") | SPX **7,649.77** intraday (−1.38%), 0.23 pts under the line — **not a close** | **NOT FIRED** (grades at the 16:00 ET cash close) |
| T2 — gamma still negative | HENRY's latest read NEGATIVE; SPX below the ~7,745 (14d) flip | 09:53 ET: NEGATIVE both horizons (14d −$29.0B per 1%, 35d −$39.3B; flips ~7,745 / ~7,750). Free-tier proxy; sign and flip are the robust reads | MET at HENRY's 09:53 read; moment property, re-read at entry |
| Credit context (not a gate here) | LIQUID >320 rung | HY OAS 333 [10/20], 327 [10/21] (FRED first-published, via SIG-012); REG-T-04 (>350 ×3) not fired | Context only; LIQUID's X1 stays CLOSED |

**Entry window:** the **first GREEN QQQ session** (QQQ above its prior close at order time) **after T1 fires**, through Fri 2026-10-30. Before the order, T2 must still read NEGATIVE (HENRY's latest) and SPX must be below 7,745.
**Void before entry:** SPX cash close ≥ 7,750 (wall reclaimed) before the order, or no green session by 10/30.

## 3. Root rule #6 (day colour)
Puts belong on green days. **Today is RED:** QQQ $705.92 (−2.66%), SPX −1.38%, VIX $19.24 (+15.35%) at 13:26 ET. I have **no measurement refuting the proxy** (the 690P marks 25.86% IV today and I hold no same-strike green-day comparison), so a fill today would be paying up for convexity. **No break is claimed; the card waits for a green session.** Entry on a green day also lowers the debit mechanically.

## 4. Structure, size and risk (default size shown as the default)

| Item | Figure (13:28 ET vendor screen) |
|---|---|
| Instrument | QQQ **Nov-20-2026 690P long / 670P short**, ×1, one complex order, never legged |
| Legs | 690P bid 13.59 / ask 13.65 (OI 61,216) · 670P bid 8.74 / ask 8.80 (OI 38,291); `--legs 690,670` gate: both usable, no LOCK/XSD/DEAD/NOBID |
| Debit | worst case (ask − bid) **$4.91**; mid $4.85 |
| **Max loss** | **$492.30** = $491.00 debit + $1.30 assumed fees (0.65/contract/side, budget arithmetic, not an account certification). Inside the **$500/card default**; a larger size is Will's per-card choice, not proposed |
| Max gain | $2,000 width − $492.30 = **$1,507.70** at QQQ ≤ 670 on expiry (−5.08% from $705.90) |
| Breakeven at expiry | QQQ **$685.09** (−2.95%) |
| Payoff ratio | 3.06 : 1 |
| DTE | 29 calendar days; spans FOMC 10/28 and the 11/3 election |
| **Do not chase** | net debit **> $5.00** (25% of width) on the broker chain → no order; QQQ already **< $685** at entry → no order (breakeven gone, payoff ratio collapses) |
| X1 | **X1 sizing gate CLOSED (DON'T-SIZE).** A fill against it is Will's explicit per-card choice; this card does not waive it |

**Why this expression:** a vertical sells the 670 wing (28.36% IV) against the 690 (25.86%), so the put skew pays part of the cost; outright 690P would risk ~$1,365 for the same view. Tenor matches the view's horizon (construction rule #16): the stress case runs over weeks (FOMC, election, AI-capex financing), not a session, so 0–5 DTE is the wrong instrument even if the view is right (the $4,341 lesson in construction rule #16). Not a print card (construction rule #18 does not bind).

## 5. Effective-N (RISK_SCORING §2b)

| Field | Entry |
|---|---|
| N_claimed | 5: negative gamma · put wall tested · AI-tape repricing (Meta 5y CDS record 114.5–119.3bp, two vendors; SOXX −6.31% today) · margin debt record + CCC yield 18% · Asia (CSI 300 bear market) |
| Shared antecedent | the AI-capex / growth repricing. Gamma and margin debt are **amplifiers** of a move, not independent causes; Asia's selloff is the same AI-spending doubt (chips led) |
| **N_eff** | **≈ 1.5 → sized as ONE view** |
| Book overlap | Same falsifier as the held **QQQ Oct-26 710P ×1** (the book's only remaining index hedge) and, partly, the bank put lines (risk-off). The combined equity-downside forward risk is this card's $492.30 plus the 710P's remaining broker mark; it is one bet, not two |

## 6. Management (written before any fill)
- **Harvest (durable finding 9):** sell the spread when it marks **≥ $10.00** (≈ 2× the debit, 50% of width) on the broker bid. P/L-keyed, reachable in the profit zone.
- **Kill:** SPX cash close **≥ 7,750 on two consecutive sessions** (wall reclaimed, flips crossed) → sell at the spread bid.
- **Time stop:** sell by the close **Fri 2026-11-13** if neither harvest nor kill has fired. No roll pre-registered; any roll is a new Will-gated proposal (Non-Negotiable #6).
- Forward max loss after a fill is the remaining mark (construction rule #20 (d)).

## 7. Why not / counter-case
- **Will declined a QQQ dated-downside put spread on 10/15** (WQ-365 DECLINE, `TRY-COND-QQQ-DATED-DOWNSIDE`). What changed since: dealer gamma flipped NEGATIVE (10/22 09:53), the put wall was tested, Meta credit at a record, SOXX −6.31%, HY 327–333 vs 266 [9/21]. Whether that is enough is his call.
- Breadth does not confirm a systemic move: **KRE +2.51%** against the tape; REGINALD grades HY transmission into bank instruments **BANK-ABSENT** (~0.6, SIG-012); VIX 19.24 is far from a panic level (safety net is >30).
- The gamma read is a free-tier proxy with assumption-dependent dollar figures; dealers' positioning can flip back on one rally.
- Will already trades short-dated QQQ puts by hand; this card adds a slower, defined-risk version of the same view rather than a new independent edge.
- Positive expectancy is **not** demonstrated; edge is qualitative (convexity bought on a negative-gamma regime with a named break line).

## 8. Calibration
No probability is stated; no Brier row.

## 9. Decision
- [ ] APPROVE (as written, ×1, max loss $492.30)
- [ ] REJECT
- [ ] REWORK with changes: ____

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.** All lines above are PROPOSED CARD CONDITIONS, not registered fleet gates. The choice routes via PROME for registration before any Will-facing ask.
