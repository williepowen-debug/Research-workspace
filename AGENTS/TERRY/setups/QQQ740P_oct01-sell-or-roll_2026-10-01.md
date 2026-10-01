# SELL-OR-ROLL CARD — QQQ $740P Oct-01-2026 ×9 (Fidelity IRA) — EXPIRES TODAY

**Date:** 2026-10-01 Thu, written 11:04–11:05 ET (`date` 11:04:37 at the read below; file written 11:05:33). **Spawn:** PROME `prome-2a`, Tier 1, WQ-347 (two PROME packets dated 2026-09-30 in `inbox/`).
**Id:** `MGMT-QQQ740P-OCT01` (management card on a line Will bought by his own hand; no SETUPS row).
**Thesis owner:** Will (no agent thesis on file — off-thesis class, `FORGE/STATUS.md` § Off-thesis).
**Terry verdict:** 🔴 **SELL-OR-ROLL BEFORE 15:00 ET TODAY — desk lean SELL.** Holding into the close is BAD STRUCTURE (worthless above 740; an unhedgeable 900-share short in an IRA below 740). If Will keeps the bet, the roll that fits root rule #7 and construction rule #21 is **QQQ $740P Oct-09 ×9 at ≈ $6.17/contract net debit (≈ $5,550 for nine, screening marks)** — never a one-day roll.
**Confidence in the read:** Medium (option quotes are one-vendor screening grade, quote age unknown — §2).
**`$0` MOVED · NO ORDER · NO NEW TRADE PROPOSED · NO GATE OR THRESHOLD MOVED.** A card is a recommendation; the order is Will's (root rule #5).

> ⚠️ **SUPERSEDED FOR CURRENT FIGURES (2026-10-01 12:5x ET):** §§1–7 and the Decision below are the 11:05 read on **×9** and are kept as written. Will sold 5 of 9 on 10/1, and the live figures for the **×4** (intrinsic, the exercise path at 400 shares / $296,000, the SELL leg, the ROLL table, the cap multiple) are in the **ADDENDUM at the foot**. Do not cite the ×9 figures ($666,000 · ≈ $5,553 · 15× the cap) as current.

---

## 1. Position (broker truth = Will; mirror = `FORGE/STATUS.md`, ANVIL reconcile `33bc8c293`)

| Field | Value | Source |
|---|---|---|
| Line | QQQ $740P Oct-01-2026 ×9, long | FORGE/STATUS.md row "QQQ $740P"; transcription `PROME/data/2026-09-30_broker-capture-TRANSCRIPTION.md` row 11 |
| Fill | Bought 9/30 @ $1.92, basis **$1,733.97** (fees $5.97 derived) — leg 2 of a net-debit roll out of the Sep-30 730P (limit $1.91) | same |
| 9/30 close | QQQ $739.77 ⇒ $0.23 ITM; Fidelity post-close mark $2.97 / $2,673.00 | FORGE/STATUS.md |
| Companion line | QQQ $735P Oct-05-2026 ×5, basis $1,368.32 — fourteen QQQ puts across two lines | FORGE/STATUS.md row "QQQ $735P" |
| Fidelity cash | $18,102.04 money market, pending −$4,007.98 (9/30) — about 50% of the account | FORGE/STATUS.md header, `[9/30 post-close]` |
| Working orders today | **UNKNOWN** — `[POSITION_STATE_UNKNOWN]` past the 9/30 capture | Will only |

## 2. Live read — 2026-10-01 11:04 ET

| Item | Value | Basis |
|---|---|---|
| QQQ spot | **$737.88 (−0.26% vs $739.77)** | `fetch.py price QQQ`, 11:04:37 ET |
| Moneyness | **$2.12 in the money** (740 − 737.88) | arithmetic |
| Intrinsic value, nine contracts | **$1,908** (2.12 × 900) | arithmetic — the floor any real bid sits near |
| Vendor 740P Oct-01 bid/ask | $2.21 / $2.23 (last option trade 10:49, fetch 11:04) | `chain_fetch.py --no-cache --legs 740` — **SCREENING ONLY** |
| VXN (Nasdaq-100 vol index) | 23.24 (+3.47%) | `fetch.py`, 11:04 |

⚠️ **The live option bid is BROKER-ONLY.** The vendor feed carries no bid/ask timestamp; its last option trade stamp ran 15 minutes behind the fetch, and on 9/11 it read a bid ~10% HIGH on the side being sold (`RISK_RULES.md` durable finding 5b). **Will reads Fidelity's own bid before any order.** QQQ was +0.30% at PROME's 09:36 read and −0.26% at 11:04 — the line sits on its strike and the in/out-of-the-money status can flip again before 15:00.

## 3. Exercise path — why "hold" is not on the menu

| QQQ at the 16:00 close | What happens to nine 740P held | Dollars |
|---|---|---|
| Above $740.00 | Expire worthless | **−$1,733.97** realized; the ~$1.9–2.0k the line is worth now is gone |
| Below $740.00 (even by $0.01) | OCC exercise-by-exception: the IRA **SELLS 900 QQQ at $740 that it does not own** | **$666,000 short** in an IRA, which cannot carry a short *(×9 at 11:05; on the ×4 it is $296,000, see the addendum)* |
| Below 740, then Fri 10/02 opens higher | The short is covered at Friday's price | **−$900 per $1 QQQ gap up**; a 1% gap (~$7.38) ≈ **−$6,640**, 3.8× the line's basis |

⚠️ **Fidelity's handling of an in-the-money expiry in this IRA is UNOBSERVED (D-60).** Every observed expiry-day "OPTION LIQUIDATION" row was out of the money. Whether Fidelity sells the line for you before the close, exercises it, or restricts the account is UNKNOWN. Near-the-strike closes also carry pin risk: after-hours moves until the exercise cutoff can decide exercise either way. **The only branch with a known outcome is selling or rolling before 15:00.**

## 4. SELL leg (desk lean)

- **Action:** sell to close QQQ $740P Oct-01 ×9, **limit at Fidelity's live bid**, before **15:00 ET**.
- **Floor:** the bid should not sit far below intrinsic (740 − QQQ at Will's read). At 11:04 that is $2.12; vendor screening bid $2.21.
- **P&L at screening marks (INFERRED, not a fill):** 9 × $2.21 = $1,989 gross, ≈ $1,983 net of ~$6 fees ⇒ **≈ +$249 vs the $1,733.97 basis.** At intrinsic only ($2.12): ≈ $1,902 net ⇒ ≈ +$168.
- **Root rule #6:** selling a put on a red day is the right colour for the SALE — puts are richer on red days.
- **Why the desk leans SELL:** no agent thesis and no fired trigger behind this line (durable finding 1 — fresh capital deploys on a fired trigger, never on book maintenance); the IRA already carries the Monday 735P ×5 as the live QQQ downside bet; and every roll below adds cash at risk.

## 5. ROLL leg (if Will keeps the bet — his practice permits it)

**Form (construction rule #21): same underlying · same strike · later expiry · same nine contracts.** Screening marks; net debit = buy at the ask, sell the Oct-01 at the $2.21 bid.

| Roll to | Trading sessions bought | Vendor 740P bid/ask | Net debit / contract | For nine | Time value per session bought | Desk view |
|---|---|---|---|---|---|---|
| Oct-02 (Fri) | 1 | 4.15 / 4.18 (11:03) | $1.97 | **$1,773** | ~$2.06 | ⛔ Not recommended — the costliest time per session, and it puts this same expiry question back on the card tomorrow (construction rule #16) |
| Oct-05 (Mon) | 2 | 5.43 / 5.45 (11:03) | $3.24 | **$2,916** | ~$1.67 | ⚠️ Stacks all fourteen QQQ puts on one Monday expiry — the same 15:00 question for both lines on one day |
| **Oct-09 (Fri)** | **6** | **8.35 / 8.38 (11:04)** | **$6.17** | **≈ $5,553** | **~$1.04** | ✅ **The roll the desk would build:** staggers the two lines (Mon 10/05 and Fri 10/09) and buys time at about half the per-session cost of the one-day roll |
| Oct-16 (Fri) | 11 | 11.25 / 11.26 (11:03) | $9.05 | $8,145 | ~$0.83 | Cheapest per session, but the most cash at risk |

- **Do not chase:** for the Oct-09 roll, no net debit above **$6.50/contract** (~5% over the screening $6.17) without a fresh read.
- **Order form:** a single two-leg net-debit order, as Will used on 9/30 — never leg it (a filled sale with an unfilled buy is an unplanned exit; a filled buy with an unfilled sale is new size).

**Rules a roll touches, in figures:**

| Rule | What a roll does | Figures |
|---|---|---|
| Root rule #7 (roll duration, never size) | ✅ Contract count stays 9 | — but the **cash at risk rises** from ≈ $1.99k (what the nine are worth now) to ≈ $7.54k (nine Oct-09 740P at the $8.38 ask): about **+$5.55k**, ≈ 15% of the IRA and ~31% of its money-market cash |
| **Standing per-card cap (`STATUS.md` § Standing rules: max loss $500 per card, 1R ≡ $250, hard cap 2R = $500 per idea)** | ⛔ **A roll breaks it ~15×** — and the line already sits above it | Forward max loss = the remaining mark (construction rule #20): ≈ $1,989 for the nine now (≈ 4× the cap, Will's own hand on 9/30); ≈ **$7,542** after an Oct-09 roll (≈ 15× the cap). A SELL takes the forward loss to $0 |
| Durable finding 1 (deploy on a fired trigger) | ⚠️ The extra ~$5.55k is fresh capital with no fired trigger | Will's hand, recorded under root rule #5 |
| Non-Negotiable #6 (no roll-by-hope) | ⚠️ This roll was never pre-registered on a card | Will's order IS the explicit re-approval; the card records it, it does not grant it |
| Root rule #6 (puts on green days) | ⚠️ The BUY leg is a put bought on a **red** day (QQQ −0.26%, VXN +3.47% at 11:04) | Estimated vol cost on the Oct-09 leg ≈ $0.43/contract per vol point × ~0.5 pt ≈ **$0.20/contract ≈ $20 for nine** (INFERRED from a model vega; the feed carries no Greeks). On delta, the red day helps a same-strike roll: the sold 0-day leg gained more than the bought leg. **No direct measurement refutes the proxy, so this is NOT a legitimate break under `RISK_RULES.md` § "Breaking root rule #6" — it is a small, recorded wrong-colour buy.** If QQQ turns green before the order, re-read the colour |

## 6. Beside the Oct-05 735P ×5

| Line | Strike vs 11:04 spot | Vendor bid (screening) | Basis | Expires |
|---|---|---|---|---|
| QQQ 740P Oct-01 ×9 | $2.12 ITM | $2.21 | $1,733.97 | **today 16:00** |
| QQQ 735P Oct-05 ×5 | $2.88 OTM | $3.47 (11:03) | $1,368.32 | Mon 10/05 |

Combined QQQ put premium now ≈ $3.7k (screening). **SELL the nine** ⇒ the Monday five remain the only QQQ put line (≈ $1.7k). **Roll the nine to Oct-09** ⇒ ≈ $9.3k in QQQ puts across Mon 10/05 and Fri 10/09. The Monday five get their own card (same question, Monday 15:00 ET).

## 7. Why not / counter-case

The case for the roll is Will's QQQ downside view, which this desk does not own: QQQ is red, VXN is bid, and a roll keeps the exposure. The case against is structural: six sessions of a 740 put cost ≈ $8.38 against a $2.12 intrinsic, and the IRA has already realized −$2,229.54 on the Sep-30 730P line this week (FORGE/STATUS.md).

## Decision

> **WQ-347 (Will):** SELL the nine at Fidelity's bid before 15:00 ET (desk lean), or ROLL them to QQQ $740P Oct-09 ×9 as one net-debit order, no debit above $6.50/contract — which puts ≈ $7.5k at risk on one line, ≈ 15× the desk's $500 per-card cap (§5). Not hold.

**APPROVAL REQUIRED — Will must approve/reject before execution.**

---

## ADDENDUM 2026-10-01 12:5x ET: the FOUR left after Will's sales (the 11:05 text above stands as written)

**Spawn:** PROME `prome-0c`, Tier 1, WQ-347 follow-up. **Trigger:** PROME packet `inbox/2026-10-01_from-PROME_10-01-partial-sales-QQQ740P-x4-USO150C-x1.md`, broker-verified, mirror reconciled `dac72b4ae`.
**Terry verdict (refreshed):** 🔴 **SELL-OR-ROLL BEFORE 15:00 ET. Desk lean is still SELL.** Not hold.
**`$0` MOVED · NO ORDER · NO NEW TRADE · NO GATE OR THRESHOLD MOVED.** The order is Will's (root rule #5).

### A1. What Will did (his hand, recorded and not graded)
| Sold to close 10/1 | Proceeds | Realized | Left |
|---|---|---|---|
| 5 of 9: 1 @ $3.44 · 1 @ $3.97 · 3 @ $3.72 (gross avg $3.71) | $1,853.66 | **+$890.35** | **×4, basis $770.66** (4/9 of $1,733.97) |

His five sold at an average of $3.71, about **twice** the $1.83 screening bid the four carry now. Fill times are not shown. Prices of $3.44–3.97 imply QQQ was lower when he sold (INFERRED; QQQ was $736.72 at 11:12). The sales took off most of the line's value and are not deviations (his 9/30 practice: sell or roll before expiry).

### A2. Live read, 2026-10-01 12:50:44–12:51:01 ET
| Item | Value | Basis |
|---|---|---|
| QQQ spot | **$738.78 (−0.13%)**; $738.92 at 12:50:44 | `fetch.py price QQQ`, 12:51:01 ET |
| Moneyness | **$1.22 in the money** (was $2.12 at 11:04) | arithmetic |
| Intrinsic value, four contracts | **$488** | 1.22 × 400 |
| Vendor 740P Oct-01 bid/ask | **$1.83 / $1.84** | `chain_fetch.py QQQ 2026-10-01 --no-cache --legs 735,740`, 12:50:53 ET. **SCREENING ONLY.** The feed carries no timestamp, and on 9/11 it read about 10% high on the bid |
| Fidelity mark (PROME packet) | $2.65 (≈ $1,060 for four), at or before 12:24 ET | broker capture (`FORGE/STATUS.md`). ⚠️ **This sits $0.82 above the vendor bid, and QQQ ($738.40 at 12:09 per the mirror vs $738.78 here) explains at most ≈ $0.25 of that gap.** The mark is probably a last trade and not a bid, but that is UNVERIFIED. The sale value of the four therefore lies anywhere from ≈ $730 (vendor bid) to ≈ $1,060 (Fidelity mark). **Only Fidelity's live bid settles it.** *(Corrected 2026-10-01 13:0x ET: the first wording said "QQQ was probably lower then", which the mirror's 12:09 read does not support.)* |
| VXN | 22.95 (+2.18%) | `fetch.py`, 12:51 ET |

⚠️ QQQ is $1.22 from the strike, closer than at 11:04. A move of about 0.17% lifts it above 740 and the four expire worthless. A dip pushes them deeper in the money. **The live bid is BROKER-ONLY: Will reads Fidelity's bid before any order.**

### A3. Exercise path for the four
| QQQ at the 16:00 close | Four 740P held | Dollars |
|---|---|---|
| Above $740.00 | Expire worthless | **−$770.66** on the four. The +$890.35 already realized stands, so the nine-contract line nets about **+$120** |
| Below $740.00 (even by $0.01) | Exercise-by-exception: the IRA **sells 400 QQQ at $740 that it does not own** | **$296,000 short** in an IRA, which cannot carry a short |
| Below 740, then Fri 10/02 opens higher | The short is covered at Friday's price | **−$400 per $1 QQQ gap-up**. A 1% gap (~$7.39) costs ≈ **−$2,955**, 3.8× the four's basis |

Fidelity's handling of an in-the-money expiry in this IRA is still **UNOBSERVED (D-60)**. The four make the short a smaller dollar amount, but they do not change how the risk works.

### A4. SELL leg, re-costed for four (desk lean)
- **Action:** sell to close QQQ $740P Oct-01 ×4 with a **limit at Fidelity's live bid**, before **15:00 ET**. Floor: no fill far below intrinsic (740 − QQQ at Will's read; $1.22 at 12:51).
- **At screening marks (INFERRED, not a fill):** 4 × $1.83 = $732 gross, ≈ **$729 net** (fees ≈ $2.65, pro-rata to 9/30). That is ≈ **−$41 on the four** against $770.66 basis. At intrinsic only: ≈ $485 net, ≈ −$285.
- **The whole nine-contract line if the four sell at $1.83:** +$890.35 + (−$41) ≈ **+$849 realized**. Measured against Will's fills, each of the four is worth about $1.83 now, about half of the $3.71 he got.
- **Root rule #6:** QQQ is red (−0.13%), the right colour to SELL a put.
- **Why SELL still leads, in figures:** (1) No agent thesis and no fired trigger sit behind the line. (2) Holding risks the full ≈ $730 if QQQ closes above 740, or an IRA short of $296k if it closes below. Neither outcome is a bet anyone sized. (3) The Monday 735P ×5 already carries the IRA's QQQ downside (vendor bid $3.28, ≈ $1.6k screening). (4) Every roll below adds $844–$3,664 of fresh cash.

### A5. ROLL table, re-costed for four (if Will keeps the bet)
Same strike and the same four contracts (construction rule #21). Screening marks, 12:50:53–12:51:00 ET. Net debit = buy at the ask, sell the Oct-01 at the $1.83 bid.

| Roll to | Sessions | Vendor 740P bid/ask | Net debit / ct | For four | Time value / session | Cash at risk after | Desk view |
|---|---|---|---|---|---|---|---|
| Oct-02 (Fri) | 1 | 3.93 / 3.94 | $2.11 | **$844** | $2.72 | $1,576 | ⛔ The costliest time per session. It puts this same question back on the card tomorrow (rule #16) |
| Oct-05 (Mon) | 2 | 5.24 / 5.29 | $3.46 | **$1,384** | $2.04 | $2,116 | ⚠️ Stacks all nine remaining QQQ puts on one Monday 15:00 decision |
| **Oct-09 (Fri)** | **6** | **7.99 / 8.04** | **$6.21** | **$2,484** | **$1.14** | **$3,216** | ✅ The roll the desk would build if Will rolls: it staggers the lines (Mon 10/05 + Fri 10/09) |
| Oct-16 (Fri) | 11 | 10.97 / 10.99 | $9.16 | $3,664 | $0.89 | $4,396 | Cheapest per session, most cash at risk |

- **Do not chase:** no net debit above **$6.50/contract** for the Oct-09 roll without a fresh read (≈ 5% over the $6.21 screening figure). Send it as **one two-leg net-debit order** and never leg it.
- **Per-card cap ($500 max loss, `STATUS.md` § Standing rules):** the four's forward max loss at the bid is ≈ $732, about 1.5× the cap. **After an Oct-09 roll it is ≈ $3,216, about 6.4× the cap.** A SELL takes it to $0.
- **Root rule #6 on the BUY leg:** this is still a put bought on a red day. No direct measurement refutes the day-colour proxy, so it is a small, recorded wrong-colour buy and **not** a legitimate break. Re-read the colour if QQQ turns green before the order.

### A6. Beside the Oct-05 735P ×5
The five are $3.78 out of the money at 12:51 (vendor bid $3.28 / ask $3.30). They get their own Monday card (`MGMT-QQQ735P-OCT05`). Today's partial sale does not change their structure.

### Decision (refreshed)
> **WQ-347 (Will):** SELL the four at Fidelity's bid before 15:00 ET (desk lean: ≈ $729 at screening, which leaves the nine-line ≈ +$849 realized). The alternative is to ROLL them to QQQ $740P Oct-09 ×4 as one net-debit order with no debit above $6.50/contract, which puts ≈ $3.2k at risk, ≈ 6.4× the $500 cap. Not hold.

**APPROVAL REQUIRED. Will must approve or reject before execution.**
