# TRADE IDEA — QQQ Nov-20 690/670 put spread — equity downside while dealer gamma is negative
**Setup ID:** `IDEA-QQQ-PUTWALL-OCT22`
**Terry verdict:** FIRED / LIVE — **now a NAKED LONG 690P ×2**: Will bought the 670P ×2 short leg back 2026-10-30 @ $8.00 (leg realized +$141.30; PROME D-93); opened ×2 by Will's hand 2026-10-23, AHEAD of T1, as the 690/670 spread at $936.70 net. Long-leg basis $2,679.33; forward risk = the remaining mark (construction rule #20(d)). §6 was written for the spread: the harvest line lapsed with the short leg; the kill (SPX cash close ≥ 7,750 two consecutive sessions) and the time stop (Fri 2026-11-13 close) are kept as the card's thesis and horizon reads; Will manages the line by hand (dated note 2026-10-31 below).

> **CARD STATE 2026-10-31 (TERRY, PROME D-93; written 14:04 EDT from `date`) — the spread is now a NAKED LONG 690P ×2; how §6 reads for it.** Source: PROME packet D-93 (`../inbox/processed/2026-10-30_from-PROME_D-93-QQQ-690P-naked-after-short-leg-close.md`) on ANVIL's reconcile of Will's 10/30 13:21 ET Fidelity capture (`FORGE/STATUS.md`): 670P ×2 BOUGHT TO CLOSE 10/30 @ $8.00 (−$1,601.33, margin) against the $1,742.63 opening credit ⇒ +$141.30 on that leg (DERIVED); 690P ×2 held, basis $2,679.33 ($13.40 avg). A Sell to Close 1 @ $17.95 limit (Day) was working at that capture; its fill is UNKNOWN until Will's next capture, so ×2 stands on every ledger (paper book split under RULING D: PB-0008a CLOSED short leg / PB-0008b OPEN long).
>
> | §6 line (written for the spread) | How it reads for the naked long |
> |---|---|
> | Harvest: spread mark ≥ $10.00 on the broker bid | **Lapsed** with the short leg — there is no spread to mark. No replacement line is set here: Will is managing the long by hand (his own working order 10/30). |
> | Kill: SPX cash close ≥ 7,750 on two consecutive sessions | **Kept** as the card's thesis-invalidation read (put wall reclaimed, flips crossed); it never depended on the short leg. State: **0 of 2** — 7,720.39 [10/29], 7,580.07 [10/30] (vendor daily); HENRY grades the 7,700 put wall BROKEN on 10/30 (SIG-W-20261031-002). |
> | Time stop: sell by the close Fri 2026-11-13 | **Kept** as the card's horizon. For the long alone the dollar decay per day is larger than for the spread, since no short leg offsets it. |
> | Forward max loss | The **remaining mark**: 690P ×2 at a $16.15 vendor mid = **$3,230** (10/30 closing quotes read 10/31 14:00 ET; weekend screening, quote time UNKNOWN). The spread capped the loss at $936.70; the long alone does not. |
>
> Context (no line): QQQ closed **$690.49** [10/30] (owner figure per COR-20261031-02, replacing a vendor 690.23), on the strike and at HENRY's 10/29 dealer-gamma trough (−$8.53B per 1% at 690); the 680 strike holds the largest ≤35-day put open interest (171.5K) and HENRY's map has the negative-gamma push easing below 680; HENRY reruns the map on Monday's open interest (L888). HENRY's breadth study (L616, `PROME/inbox/processed/2026-10-31_from-HENRY_L616-market-breadth.md`): Friday's −1.82% was narrow (Mag-7 plus 18 chip makers = 79% of it) and sat in the Nasdaq-100 / AI-hardware group that QQQ tracks, so the expression matches where the selling is; breadth offers no broad-deterioration support. Book overlap: QQQ Nov-02 715P ×1 (Will-direct, no card) is the same Nasdaq-downside bet. **Nothing here recommends selling or holding** (`USER.md` § No expiry nagging); $0 moved; no order.

> **WQ-490 closed — Will in the TERRY window 2026-10-29 11:42 ET, verbatim "490 get rid of we already bought more":** the approval row is moot; the position (×2, 10/23) is managed on §6.

> **MANAGEMENT STATE 2026-10-29 (TERRY, written ~11:3x ET from `date`): no line fired.** Kill (SPX cash close ≥ 7,750 ×2): closes 7,676.77 [10/26] · 7,722.60 [10/27] · 7,743.98 [10/28] (vendor daily) = 0 of 2. Harvest (≥ $10.00): paper mid $3.03 at 10:53 ET 10/29 (PB-0008); Will's 10/29 capture shows 690P $6.64 / 670P $3.69, ×2 ⇒ $590 vs $936.70 net debit. Time stop 11/13. Reference only; no reminder duty.
**Prior verdict (2026-10-22, history):** CONDITIONAL — NOT-FIRED; unapproved proposal.

> **FILL 2026-10-23 (TERRY booking, written 13:2x ET from `date`; root rule #10).** Source: PROME transcription of Will's Fidelity Pending view (`PROME/data/2026-10-23_broker-activity-TRANSCRIPTION.md`, ~13:2x ET; TERRY did not view the image; fill clock not displayed). **BTO 2 × 690P @ $13.39 (−$2,679.33) / STO 2 × 670P @ $8.72 (+$1,742.63), one order, net debit limit $4.67 ⇒ net $936.70 = max loss** (1.87× the $500 default and against the closed X1 gate: Will's explicit per-card choices, root rule #5 by his own hand). Max gain $3,063.30 at QQQ ≤ $670; breakeven $685.32. **Card conditions at the fill:** T1 NOT met (SPX 7,629.53 intraday at 13:23 ET; the cash close had not printed; 10/22 close 7,663.43) ⇒ fired ahead of the trigger · QQQ green ($705.65, +0.17%, 13:23 ET) ⇒ root rule #6 colour respected · net $4.67 ≤ $5.00 chase line · QQQ > $685 · SPX < 7,745 · T2 (HENRY gamma) not re-read at entry, UNKNOWN. Screening mark 13:24 ET: spread mid $4.66 / sell-side $4.62 (vendor, not broker). **Book overlap: QQQ Oct-26 710P ×1 + Oct-26 705P ×2 (bought today, $861.33) + this spread = ONE Nasdaq-downside bet, basis $2,255.69, ≈ $2,668 at 13:23–13:24 ET screening bids.** Arithmetic: `../research/2026-10-23_broker-booking/NOTE.md`. Paper book `PB-0008` (`lane=real`).

> **T1 CLOSE GRADE 2026-10-23 (TERRY, written 16:0x ET from `date`): T1 FIRED.** SPX cash close 10/23 = **7,623.61** (vendor daily bar; 390 one-minute bars 09:30–15:59, last bar 7,622.99) < 7,650.00 by **26.39 points (−0.34%)**; session low 7,612.07, high 7,660.15. Pulled 16:02 ET, two minutes after the close: the cash-index bar can still revise slightly, but the 26-point margin exceeds any plausible revision. QQQ closed $704.40 vs $704.47 (−0.01%, red). **Will's fill (13:2x ET, ahead of T1) makes the entry rule moot; the §6 management lines govern from here** (harvest ≥ $10.00 mark · kill SPX cash close ≥ 7,750 on two consecutive sessions · time stop 11/13 close). Evidence: `../research/2026-10-23_T1-close-grade/CLOSES.json`.
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

## 6. Management (written before any fill) — **LIVE from 2026-10-23, at ×2**
- **Harvest (durable finding 9):** sell the spread when it marks **≥ $10.00** (≈ 2× the debit, 50% of width) on the broker bid. P/L-keyed, reachable in the profit zone. At ×2: ~$2,000 proceeds, ~+$1,063.30 before closing fees.
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
