# TRADE IDEA — USO Jan-15-2027 170/185 call spread — own the post-election strike window the held calls do not reach
**Setup ID:** `IDEA-USO-POSTELECTION-OCT22`
**Terry verdict:** NO TRADE — WQ-491 resolved, not taken (Will in the TERRY window 2026-10-29 11:42 ET, verbatim "I think we already bought more USO since then"); his own 10/29 capture shows USO Nov-20 170C ×1 and Oct-30 163C ×1, not this spread. Closed; no further grading.

**Prior verdict (superseded 2026-10-29):** CONDITIONAL — **NOT-FIRED**; unapproved proposal. Nothing is approved in advance.
**Prepared:** 2026-10-22 13:29 ET (clock read from `date`), TERRY (Claude Opus 5.5, Claude Code), PROME spawn on WQ-487 A. Commission basis: Will 2026-10-20 11:50 ET, verbatim *"we can loosen rules for trade ideas"*.
**Thesis owners (evidence, not a TERRY thesis):** BRENT (oil thesis); FALCON (US–Iran direct-kinetic row 5; SIG-W-20261022-003, -007). FALCON's packet `2026-10-22_from-FALCON_oil-leg-catalyst-window-NOT-FIRED.md` (~13:4x ET) landed after the first draft and is folded into § 2; FALCON's figures govern the trigger-state cell.
**Data freshness:** USO spot $162.30–162.43 and BZZ26 $112.48 (+3.36%; vendor contract label truncated, identity rests on the requested symbol, not a settle) at 13:26–13:29 ET; chain 13:29 ET `--no-cache`. Vendor option quotes are **SCREENING marks**; the order is priced on the broker chain (durable finding 5b).

> **CLOSE READ 2026-10-22 (TERRY, PROME spawn prome-e7; 19:3x ET from `date`): no cell on this card keys on the 10/22 close.** USO completed close **$162.51** (+1.70% vs $159.80 on 10/21, GREEN). The entry window opens Fri 10/23 on a RED USO session; $162.51 is $5.49 under the $168.00 no-chase line (an order-time test) and $12.51 above the $150.00 kill (binds only if held; nothing is held). Trigger (FALCON row 5, US strike on Iran) not re-graded here: FALCON owns it. No Will ruling on WQ-491 as of 19:3x ET. State unchanged: NOT-FIRED.

## 1. One-line setup
The reporting puts any renewed US strike on Iran **after the 11/3 election**, while every USO call line the book holds expires **10/23–10/30**. This card buys the same view with tenor that reaches the window, as a capped call spread entered on a red day.

## 2. Trigger state, in figures (NOT-FIRED)

| Item | State | Source |
|---|---|---|
| **Trigger: US strike on Iranian territory (FALCON row 5)** | **NOT FIRED** — none found since 9/8 | FALCON via SIG-W-20261022-003 |
| Posture | 10/21: one anonymous US official (secondhand, Drop Site via HormuzLetter): CENTCOM "putting all the pieces into place to renew major combat operations", awaiting Trump. **Posture, not a strike or a decision** | SIG-003 |
| Timing evidence | NYT 10/21: US–Israel planning for strikes **after** the election; Trump 10/8: no attack before the 11/3 midterms; TASS: operations called off seven times at the last minute | SIG-003 |
| Theater claims | IRGC claims 4 STS tankers + 3 mine hits in the northern Gulf: **CLAIM ONLY**, no UKMTO confirmation | SIG-W-20261022-007 |
| Crude | BZZ26 $112.48 (+3.36%), CLZ26 $99.41 (+2.33%) at 13:26 ET; CoinDesk: Brent highest since May | `fetch.py`; SIG-002 |
| **FALCON grade (10/22 ~13:4x ET)** | FAL-07 US strike **NOT FIRED**, 45 days without a US strike on Iran since 9/8. FALCON's estimate: **65%** for a renewed strike 10/22–12/31, but only **~10% [EST] before 11/3** (Trump's no-strike-before-11/3 pledge stands; NYT: planning for after the election). Production rung D 85→92 ARMED, NOT FIRED. IRGC tanker/mine claims **0 of 7 confirmed**; GATE-FALCON-001 leg 2 NOT MET | FALCON packet 10/22 (KB-FALCON-315/316) |
| What today's +3% rests on | the CLAIM-ONLY IRGC tanker hits; FALCON: debunking puts the move at risk of reversal, confirmation by UKMTO or an operator supports it | FALCON packet |

The card is a **pre-position before the trigger** (the loosened-ideas lane). If the trigger fires first, crude gaps and this structure is re-priced from scratch, not chased.

## 3. Root rule #6 (day colour)
Calls belong on red days. **Today USO is GREEN** (+1.56%). No refuting measurement is offered (Jan-15 170C at 49.25% IV; no red-day comparison in hand), so **no fill today**. Entry only on a **RED USO session** (USO below its prior close at order time).

## 4. Structure, size and risk (default size shown as the default)

| Item | Figure (13:29 ET vendor screen) |
|---|---|
| Instrument | USO **Jan-15-2027 170C long / 185C short**, ×1, one complex order |
| Legs | 170C bid 12.00 / ask 12.30 (OI 2,726) · 185C bid 7.70 / ask 8.15 (OI 924) |
| Debit | worst case (ask − bid) **$4.60**; mid $4.22 |
| **Max loss** | **$461.30** = $460.00 + $1.30 assumed fees. Inside the **$500/card default**; a larger size is Will's per-card choice, not proposed |
| Max gain | $1,500 width − $461.30 = **$1,038.70** at USO ≥ $185 on expiry (+13.9% from $162.40) |
| Breakeven at expiry | USO **$174.60** (+7.5%) |
| DTE | 85 calendar days — inside the desk's 60–90 DTE new-deployment band (construction rule #21). Dec-18 (57 DTE) fails that band, so it was rejected |
| **Entry window** | first RED USO session from Fri 10/23 through Mon 11/2 (before the election) |
| **Do not chase** | net debit **> $5.00** on the broker chain, or USO **> $168.00** at the order → no order |
| X1 | **X1 sizing gate CLOSED (DON'T-SIZE).** A fill against it is Will's explicit per-card choice |

**Why this expression:** USO implied vol is ~49–50% across the Jan strip; the vertical sells the 185 wing (50.35%) so the call skew pays part of the cost, and max loss is fixed. **This is a NEW DEPLOYMENT, not a roll** (different strike and expiry; construction rule #21): the band binds and it is met. It is not a recommendation to sell or roll any held line, and it says nothing about those lines.

## 5. Effective-N and book concentration (RISK_SCORING §2b)

| Field | Entry |
|---|---|
| N_claimed | 3: CENTCOM posture · post-election timing reports · Gulf shipping claims |
| Shared antecedent | one decision, a US strike on Iran; all three die together on a deal, a ceasefire or a seventh call-off |
| **N_eff** | **1** |
| Book overlap | **Same falsifier as the whole oil sleeve:** USO 35 shares (mirror mark $160.87 at 11:01 ET), USO call lines Oct-23 163C ×1, Oct-28 165C ×1, Oct-30 165C ×2, Oct-30 163C ×1, and partly VLO 3 shares. This card adds ≤ $461.30 to that one bet. Its only new property is **tenor past 11/3**; it adds no independent edge |
| BRENT sizing modifier | COT short-crowding test (`COT-FUEL-35B-V2`) last read at this desk: vintage #9 [as-of 10/6] JOINT NOT-SPENT; later vintages not read here. A sizing modifier, never a trigger |

## 6. Management (written before any fill)
- **Harvest (durable finding 9):** sell the spread when it marks **≥ $9.20** on the broker bid (2× the worst-case debit).
- **Kill:** a US–Iran deal or ceasefire announcement confirmed by FALCON, **or** USO close **< $150.00** (−7.6% from $162.40) → sell at the spread bid.
- **Time stop:** sell by the close **Thu 2026-12-31** if neither harvest nor kill has fired (the post-election window will have resolved one way or the other).
- If the trigger FIRES while the spread is held: hold to harvest; no add without a named driver in figures (construction rule #23).

## 7. Why not / counter-case
- The oil sleeve is already one of the book's largest exposures (USO 35 shares alone $5,630.45 at the 11:01 ET mirror mark); this is the same bet again.
- One anonymous official, secondhand; Trump has called these operations off repeatedly; the White House timing statements point to **no** strike before 11/3, so a fill before then pays theta for a reported, not decided, event.
- FALCON puts the strike odds before 11/3 at ~10% [EST]: most of the 65% sits after the election, so an entry before 11/3 pays time value for a window that has not opened. That is the reason for a January tenor, and also the cost.
- FALCON suggested carrying the exposure into the window as a roll (root rule #7). Under construction rule #21 a change of strike or expiry is a NEW DEPLOYMENT, not a roll, so this card is gated as one; it does not touch or replace the held lines.
- Brent at its highest since May on a CLAIM-ONLY tanker headline (0 of 7 confirmed): buying calls into that strength is the chase root rule #6 exists to prevent, hence the red-day entry and the $168 no-chase line.
- USO tracks crude front-month futures with roll costs; a strike that spikes Brent briefly may not hold to a level USO needs (+7.5% to breakeven).
- Positive expectancy is **not** demonstrated.

## 8. Calibration
No probability is stated; no Brier row.

## 9. Decision
- [ ] APPROVE (as written, ×1, max loss $461.30)
- [ ] REJECT
- [ ] REWORK with changes: ____

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.** All lines above are PROPOSED CARD CONDITIONS, not registered fleet gates. The choice routes via PROME for registration before any Will-facing ask.
