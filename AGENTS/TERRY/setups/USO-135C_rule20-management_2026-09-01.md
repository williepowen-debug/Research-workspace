# MANAGEMENT WRITE-UP (RISK_RULES #20) — `USO Oct-16-2026 $135C` — ~~×2, HELD~~ → **×1 REMAINS (leg A EXECUTED 9/2: one sold, price OWED)** — named exit / target / time stop. NO NEW RAIL.
**Date:** 2026-09-01 Tue, built ~17:4x–18:1x ET (`date` wall clock, copied not inferred; markets shut — the 9/1 close is the last tape) · **Updated 2026-09-02 Wed ~19:3x ET — terms ADOPTED (WQ-145, 9/1 18:13 ET); leg A EXECUTED by Will 9/2 (ONE 135C sold, fill price NOT YET STATED); ×1 remains under B + C**
**Setup ID:** `TRY-MGMT-USO135C`
**Class:** **MANAGEMENT-ONLY, RETROACTIVE** — RISK_RULES #20 says so on its face: the entry half of this position is **UNRECOVERABLE** and is NOT reconstructed here; only the forward half (risk · target · time stop · roll rule) is written, and all of it is forward-looking.
**Thesis owner:** **BRENT** (oil / Hormuz-supply; catalyst clock is his) · position owner **Will** (Fidelity IRA) · management construction **TERRY**
**Ruling chain:** Will 8/18 HOLD (shares only) → Will 8/21 SELL-ONE (harvest) + HOLD-DON'T-ROLL the second → **Will 8/27 HOLD ×2** (*"I never did sell one — I want to wait. I do think this ride isn't over yet."*) → **WQ-94 RULED 9/1** (*"approve all of those with your recs"*, 17:22 ET): write the rule-#20 management-only terms, return for [Approve]. **The 8/27 HOLD stands until Will approves these terms.**
**Terry verdict:** 🟢 **FIRED / LIVE — terms A + B($135) + C ADOPTED by Will (WQ-145, 2026-09-01 18:13 ET, verbatim *"Approve 144 and 145 with your recs"*); leg A EXECUTED 2026-09-02 (Will verbatim 14:21 ET *"I did sell one of the USO calls"* — ONE Oct-16 $135C sold, PRICE OWED by Will, not inferred); ONE $135C remains, governed by B (USO official close < $135 ⇒ sell the remaining one next open — 9/2 close $141.15, NOT fired) and C (Fri 10/09, unconditional).** `GATE-TERRY-USO135C` (PROME) tracks B/C. *(Verdict at write, 9/1: CONDITIONAL — terms proposed, nothing bound until [Approve]. History.)*
**Data freshness:** USO close **$141.00** [9/1, +5.46%, `snapshot.py` 17:28 ET; 30d range 114.88–141.00 — today IS the high] · chain `chain_fetch.py USO 2026-10-16 --type call --legs 135 --no-cache` **17:28 ET 9/1** (post-close; 135C last print 15:57) · position `FORGE/STATUS.md` 8/29 reconcile: **×2, bought opening 8/03 for $1,421.33 ($7.11/contract) [Fidelity activity view]** — basis is a state-file figure, confirm at any fill (RISK_RULES #4)

> ✅ **TERMS LIVE SINCE 9/1 18:13 ET. Leg A executed by Will's hand 9/2. Every remaining act (B's next-open sell, C's 10/09 sell) is Will's, at his broker (Fidelity IRA).** The #20(a) violation this memo was written to end — a decaying option on no rail — **ended at the adoption**; it is recorded here because this block said for six days that it would keep saying so. *(9/1 text, history: nothing here executes; until approved the leg is HELD on the 8/27 ruling with no exit rule, ×2.)*

---

## 0. Position truth — what is known, what is not (#20(c): UNRECOVERABLE ≠ blank)
| Field | Value | Source / status |
|---|---|---|
| Contracts | ~~**2**~~ → **1 (as of 9/2)** | **ONE SOLD 9/2 by Will (leg A) — Will verbatim 14:21 ET; fill price NOT YET STATED (PROME has asked). Recorded as PRICE-OWED, not inferred from the chain.** *(9/1: 2 per FORGE 8/29, Will-confirmed ×2 on 8/27 — the "×1" this desk asserted 8/27 was its own defect, corrected same session; today's ×1 is a DIFFERENT fact, on Will's word, one day later.)* |
| Entry date / price | **8/03/2026, $7.11/contract, $1,421.33 total** | FORGE 8/29 activity view — **date now KNOWN** (was D-19 UNRECOVERABLE at the 8/18 write of #20). Rationale/trigger/preconditions at entry: **UNRECOVERABLE — not reconstructed** |
| 9/1 mark | **bid $12.10 / ask $12.50 / mark $12.30**, IV 47.1%, OI 2,146, vol 530, spread 3.25% — no quote flag | chain_fetch 17:28 ET |
| **9/2 mark (remaining ×1)** | **bid $11.80 / ask $12.20 / mark $12.00**, IV 45.5%, OI 2,078, vol 517, spread 3.33% — no flag. USO **$141.15 +0.11%** (O 139.42 / H **142.16** / L 138.44 / C 141.15, yfinance). **⚠️ Leg A's fill price is NOT read off this chain — the sale's price is Will's to state; the $14.25 grade (Rule A) waits for it.** | `chain_fetch --legs 135 --no-cache` 19:28 ET 9/2 · `fetch.py` |
| Position value | *(9/1, ×2)* **$2,460 at mark / $2,420 at bid** = +$1,038.67 / +73.1% on the $1,421.33 basis (MOMENT property, #14) · **(9/2, remaining ×1) $1,200 at mark / $1,180 at bid** | **Realized on leg A: UNKNOWN until the price lands.** Basis recovery (the $1,425 line) cannot be graded yet |
| Moneyness | USO $141.00 vs $135 strike = **$6.00 ITM (+4.4%)**; intrinsic $6.00, extrinsic **$6.30** | BS check at 47% IV / 45 DTE: delta **≈0.65**, theta **≈ −$10.5/day/contract** (−$21/day on the pair, accelerating), vega ≈ $18/pt |
| DTE | **45 calendar / ~32 trading** to Fri 10/16 | |
| Sleeve context | 4 USO-linked lines (37 sh · 135C ×2 · RH 150/165 Sep-18 · XLE 65C ×2) — FORGE 8/29: ≈16.7% of the IRA at 8/28 marks; **today's +5.5% grew every line.** BRENT's 8/21 note stands: the convex leg dilutes the linear share on the way UP and re-concentrates it on the way DOWN | `AGENTS/BRENT/TRADE.md` § Concentration; FORGE D-35/D-19 |

## 1. Forward risk — the only number that matters for management (#20(b)/(d))
**Max loss from here (9/2, ×1 remaining) = the remaining mark: $1,200 (mid) / $1,180 (bid).** *(9/1, ×2: $2,460 / $2,420.)* Not the basis. The remaining contract can give back **its whole mark** if USO is ≤ $135 on 10/16; whether the PAIR is now net-positive vs its $1,421.33 basis depends on leg A's proceeds — **owed, not estimated.** The sunk basis is irrelevant to every rule below.

Decay is the second risk and it is not linear: ~$21/day on the pair at 9/1 (**≈ $10–11/day on the remaining ×1 at 9/2**), rising toward ~$20/day per contract in the final two weeks if USO sits near the strike. **Sitting still has a price tag now; it did not on 8/03.**

## 2. ⚠️ RISK_RULES #23 — name the driver before anyone adds. (No add is proposed; the rule is stated so nobody proposes one on today's tape.)
USO +5.46% on 9/1 (WTI $90.67 +5.7% per REGINALD's 9/1 macro line; VIX +13%, 10Y 4.80, gold −2.35%). **Whether today's move was the underwritten Hormuz/supply mechanism or a risk-off/inflation bid is BRENT's to name in figures — not TERRY's.** Until it is named, **#23 forbids an add** and this write-up proposes none. The management terms below are driver-agnostic by design (P/L-keyed and level-keyed), which is why they can be written tonight without the attribution.

## 3. THE TERMS PROPOSED (three rules, OR-joined; each self-executing where possible — RISK_RULES #16 corollary: a control that exists only as a manual act at zero executions is not a control)

### Rule A — PROFIT-KEYED HARVEST (RISK_RULES #9 — the rule this leg has lacked since 8/03) — ✅ **EXECUTED 9/2 (Will: ONE sold). FILL PRICE OWED.**
**Sell ONE contract on a resting GTC limit at ≥ $14.25.** *(ADOPTED 9/1.)* **9/2: ONE 135C SOLD by Will's hand — whether it was this GTC filling at ≥ $14.25 or a discretionary harvest at another price is exactly what the owed price will say; TERRY does not infer it from the chain (the 135C's post-close mark was $12.00 and USO's 9/2 high was $142.16 — stated as the day's tape, NOT as a bound on Will's fill). Grade against the $14.25 line when the price lands; if below it, the harvest is still the RIGHT SIDE of #9 (a profit-zone sell) executed at the operator's discretion, and is recorded as such — not as a rule miss.**
- **Why $14.25:** one contract at $14.25 = **$1,425 ≥ the pair's entire basis ($1,421.33)** ⇒ the remaining contract rides on house money with its own max loss = its mark. Not a round number, not a chart level — **the level at which the position pays for itself**, which is the one harvest that is unarguable on any thesis. 2.0× basis per contract.
- **Distance:** $14.25 − $12.30 mark = **+$1.95 ≈ USO +$3.0 (delta 0.65) ≈ $144** — inside one 5-session σ (USO 5-session σ **6.9%**, p75 ≈ +3.5%; n=250). Reachable; not a gift.
- **Colour:** selling a call into strength = the correct side of root rule #6 (calls on red days is the BUY side; the harvest sells green).
- ⛔ **Not a target for the second contract.** The second contract has no upside cap under these terms — that is Will's *"ride isn't over"* preserved, with a floor under it (Rule B).

### Rule B — GIVE-BACK BACKSTOP (level-keyed, on the UNDERLYING, close-graded) — 🟢 **LIVE, ×1. 9/2 close $141.15 ⇒ NOT FIRED.**
**USO regular-session CLOSE < $135.00 ⇒ sell ~~BOTH remaining contracts~~ → the REMAINING ONE at the next open** (market-on-open or a limit at the bid — do not work it). *(ADOPTED 9/1 at $135 — Will took TERRY's rec, not the $130 alt.)* TERRY/PROME grade the official close daily; a fire ⇒ packet PROME same session, Will executes (`GATE-TERRY-USO135C`).
- **Why the strike:** below $135 the calls are 100% extrinsic again — a decaying asset with 30-odd days left, i.e. the exact shape BRENT's 8/21 card called *"a genuine reason not to sit still — but it argues for CLOSING, not rolling."* At $135 the pair marks ≈ $7–8/contract (≈ $1,400–1,600, ~basis) so the rule protects the *basis*, not the peak.
- **What it costs in noise (measured, RISK_RULES #19 — bar counts stated):** −4.3% from $141. USO 5-session return **p25 = −3.0%, p10 = −6.5%** (n=250); since 2026-03-01 the running-peak give-back exceeded 4% **seven times in 128 bars** (max −32.5%, 5/19→7/1; median drawdown-from-peak observation −13%, n=113). ⇒ **on this instrument's own tape, a −4.3% give-back inside a month is more likely than not.** Rule B WILL probably fire if the ride stalls; that is the design — it converts "ride" into "ride while ITM."
- **Alternative width for Will to pick instead (same shape, wider):** close < **$130** (−7.8%; pair ≈ $4–5/contract ≈ $900, i.e. gives back ~$500 of basis). Hit-rate: 20-session p10 ≈ −8.6% ⇒ roughly a 1-in-8 month. **TERRY recommends $135** — the strike is the one level with a *structural* meaning (intrinsic → 0), everything else is a chart choice.
- **Self-executing form:** Fidelity conditional order (trigger: USO last ≤ $135.00 ⇒ sell 2 × 135C, limit at bid−0.10). ⚠️ Intraday trigger ≠ close — Will's choice: the conditional order (fires on a wick, never misses) or the close-graded version (TERRY/PROME grade the official close; misses an intraday flush that recovers). **Recommend the close-graded version + a next-open sell**, because the leg is liquid enough (OI 2,146, 3% wide) that a one-session lag costs ~$21 of theta, not a gap.

### Rule C — TIME STOP (mandatory, unconditional) — 🟢 **LIVE. Fri 10/09.**
**Fri 2026-10-09, before the close: sell whatever remains (now ×1), at any P/L.** Five sessions before expiry. *(ADOPTED 9/1.)*
- An ITM long call in the IRA that is held through 10/16 **auto-exercises into 200 USO shares at $135 = $27,000 of stock** — not a position this book wants or can carry; Fidelity may force-close it on its own terms if it is not sold. Do not let the broker choose the price.
- Between 10/9 and 10/16 gamma/theta are at their worst; there is nothing to gain from the last week that Rule A has not already captured.
- ⛔ **No roll is pre-registered.** Will ruled HOLD-DON'T-ROLL on 8/21 (BRENT's card: every live catalyst fires before 10/16; Oct→Dec would buy 63 days containing zero registered rows). A roll proposal would be a NEW card on BRENT's catalyst docket, admissible only via Will [Approve] (Non-Negotiable #6).

### What the three rules do together (worked, at 9/1 marks)
| Path | What fires | Outcome on the pair |
|---|---|---|
| USO → $144+ inside a few weeks | **A** sells 1 @ $14.25 = $1,425 (basis recovered); contract 2 rides with **B** and **C** under it | worst case after A = +$1,425 + (contract 2 at ≥ ~$7 if B fires) ≈ **+$700 to +$1,100 realized vs basis** |
| USO stalls 135–141, then closes < $135 | **B** sells 2 @ ~$7–8 ≈ $1,400–1,600 | ≈ **flat to +$180 vs basis** — the ride gave back its gain but not the stake |
| USO stays > $135 into October, never reaches $144 | **C** sells 2 on 10/9 at intrinsic + residual extrinsic | ≈ **+$0 to +$1,000** depending on where USO sits; time value has drained by then |
| USO gaps below $135 overnight (event) | **B** sells at the next open, below the line | **the one path that can lose more than basis** — bounded by the pair's mark, ~$2,460 today; this is the risk Will is holding by choosing HOLD ×2 over SELL-ONE on 8/27 |

## 4. What this write-up deliberately does NOT do
- Does not reconstruct why the leg was bought (#20 — UNRECOVERABLE; the entry date/price are now known, the decision record is not).
- Does not propose an add, a roll, a spread-over, or any new capital (**WQ-94: management-only, no new rail**).
- Does not name today's driver (#23 — BRENT's), and does not read +73% as thesis confirmation (RISK_RULES #23: profit from a mechanism you did not underwrite is evidence against the card; here there is no card).
- Does not couple to `TRY-EXIT-USO35` (shares) — that card's scope fence (commission requirement #3) holds both ways. ⚠️ Note for that card: FORGE 8/29 shows **37 shares** (2 bought 8/26), not 35 — its title is stale; flagged, not fixed here.

## 5. Catalyst map inside the window (BRENT's board, cited not re-derived — `AGENTS/BRENT/docket/CATALYSTS.tsv` is canonical)
Already passed: Bessent 8/24 · Jazan 8/30 · Russia diesel-ban date 9/1. Ahead inside 10/16 (per BRENT's 8/21 list): **OPEC+ 9/6 · SPR test 9/9** · 9/11 CPI · 9/15–16 FOMC · 10/9 time stop · 10/16 expiry. ⚠️ BRENT re-verifies dates; TERRY does not source them.

## 6. Decision
- [x] **APPROVED A + B($135) + C** as written (TERRY rec) — **Will, WQ-145, 2026-09-01 18:13 ET** (*"Approve 144 and 145 with your recs"*; `PROME/proposals/2026-09-01_wq-batch-RULED.md`). The 8/27 HOLD is superseded by these terms.
- [ ] ~~APPROVE with B at $130~~ · ~~A + C only~~ · ~~REJECT~~ — not taken.
- [x] **Leg A EXECUTED 2026-09-02** (Will; ONE sold; **price owed**). ×1 remains under B + C.

**Terms adopted and partly executed by Will. Terry never executes; B and C fires route to Will via PROME the same session.**

---
## 7. Dated log
- **2026-09-01 ~17:4x–18:1x ET — WRITTEN** on WQ-94's ruling. USO $141.00 (+5.46%), 135C 12.10/12.50, pair +$1,038.67 / +73.1% at mark. `$0` moved, no order. Returns to Will via PROME.
- **2026-09-01 18:13 ET — ADOPTED (WQ-145):** A + B($135) + C, Will verbatim *"Approve 144 and 145 with your recs"* (PROME packet `2026-09-01c`). `GATE-TERRY-USO135C` registered by PROME (fires = B or C; A = Will's resting order). The #20(a) violation ends here.
- **2026-09-02 14:21 ET — LEG A EXECUTED by Will:** *"I did sell one of the USO calls."* ONE Oct-16 $135C sold; **fill price not stated (PROME asked; OWED).** ONE remains. USO settled **$141.15 +0.11%** (H 142.16) ⇒ **B NOT FIRED** (close ≥ $135). 135C post-close 11.80/12.20.
- **2026-09-02 ~19:3x ET — RECORDED (this desk, PROME-spawned).** Verdict → FIRED / LIVE; contract count ×2 → ×1 on Will's word; forward max loss re-based to the remaining mark ($1,200 mid); B re-worded to "the remaining one"; A marked EXECUTED / PRICE-OWED — **not graded against $14.25 until the price lands.** No threshold moved, no add, no roll. **Open on Will: the leg-A fill price** (one number; it decides the basis-recovery line and the A-grade).
