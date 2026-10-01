# SELL-OR-ROLL CARD — QQQ $740P Oct-01-2026 ×9 (Fidelity IRA) — EXPIRES TODAY

**Date:** 2026-10-01 Thu, written 11:04–11:05 ET (`date` 11:04:37 at the read below; file written 11:05:33). **Spawn:** PROME `prome-2a`, Tier 1, WQ-347 (two PROME packets dated 2026-09-30 in `inbox/`).
**Id:** `MGMT-QQQ740P-OCT01` (management card on a line Will bought by his own hand; no SETUPS row).
**Thesis owner:** Will (no agent thesis on file — off-thesis class, `FORGE/STATUS.md` § Off-thesis).
**Terry verdict:** 🔴 **SELL-OR-ROLL BEFORE 15:00 ET TODAY — desk lean SELL.** Holding into the close is BAD STRUCTURE (worthless above 740; an unhedgeable 900-share short in an IRA below 740). If Will keeps the bet, the roll that fits root rule #7 and construction rule #21 is **QQQ $740P Oct-09 ×9 at ≈ $6.17/contract net debit (≈ $5,550 for nine, screening marks)** — never a one-day roll.
**Confidence in the read:** Medium (option quotes are one-vendor screening grade, quote age unknown — §2).
**`$0` MOVED · NO ORDER · NO NEW TRADE PROPOSED · NO GATE OR THRESHOLD MOVED.** A card is a recommendation; the order is Will's (root rule #5).

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
| Below $740.00 (even by $0.01) | OCC exercise-by-exception: the IRA **SELLS 900 QQQ at $740 that it does not own** | **$666,000 short** in an IRA, which cannot carry a short |
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

> **WQ-347 (Will):** SELL the nine at Fidelity's bid before 15:00 ET (desk lean), or ROLL them to QQQ $740P Oct-09 ×9 as one net-debit order, no debit above $6.50/contract. Not hold.

**APPROVAL REQUIRED — Will must approve/reject before execution.**
