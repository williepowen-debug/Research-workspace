# MANAGEMENT NOTES — USO $150C Oct-09-2026 ×2 · KRE $65P Dec-31-2026 ×2 (Fidelity IRA) — Will's 9/30 rolls

**Date:** 2026-10-01 Thu, written 11:11 ET (live reads `date` 11:09:14–11:09:58). **Spawn:** PROME `prome-2a`, Tier 1 (packet `inbox/processed/2026-09-30_from-PROME_sep30-lines-were-ROLLED-not-expired_fills-and-card-asks.md`, ask 3).
**Ids:** `MGMT-USO150C-OCT09` · `MGMT-KRE65P-DEC31` (management notes; no SETUPS rows).
**Terry verdict:** 🟡 **RECORDED — Will's own hand (root rule #5); sell-or-roll rails set, no action owed today.** These notes record the lines and their rails; they do not re-litigate the rolls.
**`$0` MOVED · NO ORDER · NO NEW TRADE PROPOSED · NO GATE OR THRESHOLD MOVED.** Cents from `FORGE/STATUS.md` (ANVIL `33bc8c293`); option quotes are vendor SCREENING marks — the live bid is Fidelity's (`RISK_RULES.md` durable finding 5b).

---

## A. USO $150C Oct-09-2026 ×2 — `MGMT-USO150C-OCT09`

| Item | Value | Source |
|---|---|---|
| Fill | **BOUGHT 9/30 ×2 @ $2.99, basis $599.33** — leg 2 of a net-debit roll out of the USO Sep-30 159C ×2 (sold @ $0.01, net $1.87 ⇒ −$919.46); limit $2.98 | FORGE (transcription rows 5–6) |
| Live 11:09 ET | USO **$148.26 (+1.78%)** ⇒ 150 strike **$1.74 out of the money**; vendor 150C bid/ask **3.55 / 3.65** (last trade 10:48) ⇒ ×2 ≈ $710 ⇒ ≈ **+$111 vs basis** (INFERRED) | `fetch.py`; `chain_fetch.py --no-cache` |
| Thesis / book | Oil — BRENT owns the thesis. New oil-call exposure on the "one oil bet" book; Will **accepted that concentration in writing 9/25** (WQ-297 A, `PROME/proposals/2026-09-25_wq297-298-RULED.md`). Beside the 37 USO shares (WQ-200: no rule, hand-managed) | FORGE; STATUS 9/25 block |

**Rail (sell-or-roll, `USER.md` 9/30 19:03 ET):**
- **Hard stop Fri 10/09 15:00 ET.** Sell at Fidelity's bid, or roll as one net-debit order.
- **Exercise path if held in the money:** a close above $150.00 ⇒ the IRA **buys 200 USO at $150 = $30,000** against ≈ $14,094 settled cash (FORGE header, derived) — it cannot fund it; Fidelity's handling **UNOBSERVED (D-60)**.
- **Roll form (construction rule #21: same strike, later expiry):** indicative today, buy at the ask and sell the Oct-09 at the bid: **Oct-16 150C** 5.00 / 5.15 ⇒ ≈ $1.60/ct (≈ $320 for two) · **Oct-23 150C** 6.35 / 6.60 ⇒ ≈ $3.05/ct (≈ $610). Re-price at the order.
- **Root rule #6:** calls on red days — USO is **green today (+1.78%)**: the wrong colour to BUY a call leg, the right colour to SELL.

**Rules on the line, recorded and not re-litigated:** strike moved 159 → 150, so the 9/30 trade was not a construction rule #21 roll · forward max loss = remaining mark (construction rule #20) ≈ $710 ≈ **1.4× the $500 per-card cap** · ⚠️ **no P/L-keyed harvest (durable finding 9)** — suggested form if Will wants one: sell both at any Fidelity bid ≥ $5.98 (2× the $2.99 fill) · catalyst map: none registered on this line (BRENT owns oil's calendar).

## B. KRE $65P Dec-31-2026 ×2 — `MGMT-KRE65P-DEC31`

| Item | Value | Source |
|---|---|---|
| Fill | **BOUGHT 9/30 ×2 @ $1.68, basis $337.33** — leg 2 of a net-debit roll out of the KRE Sep-30 60P ×2 (sold @ $0.01, net $1.87 ⇒ −$451.48); limit $1.67 filled after $1.63 and $1.55 attempts were Verified Canceled | FORGE (transcription rows 1–4, 7–8) |
| Live 11:09 ET | KRE **$68.36 (−1.55%)** ⇒ 65 strike **$3.36 / 4.9% out of the money**; vendor 65P bid/ask **2.00 / 2.28** (13% wide, OI 83, last trade 9/30 15:13) ⇒ ×2 ≈ $400 at the bid ⇒ ≈ **+$63 vs basis** (INFERRED) | `fetch.py`; `chain_fetch.py --no-cache` |
| Fidelity's 9/30 mark | $0.01 post-close — **not a valuation (FORGE D-67)**; the line is not −99% | FORGE |
| Thesis | Regional banks — REGINALD owns | — |

**Rail (sell-or-roll):** hard stop **Thu 12/31 15:00 ET** (91 days). Exercise path if held in the money: the IRA **sells 200 KRE at $65 = $13,000 short** — Fidelity's handling UNOBSERVED (D-60). Roll form, when the time comes: 65 strike, a later expiry, same two. ⚠️ **Liquidity:** a $0.28-wide market on 83 open interest — crossing it costs ≈ $56 on two; work a limit, never a market order.

**Recorded against this desk's own card, not re-litigated:** the add went on the same day `setups/KRE_add-puts_conditional-card_2026-09-30.md` read **CONDITIONAL — NO FILL** (REG-T-01 un-fired · X1 CLOSED · construction rule #23 driver unnamed). Strike moved 60 → 65: not a construction rule #21 roll. Root rule #6: KRE was red on the day of a put BUY (9/30 −0.56%); it is red again today (−1.55%) — right colour to SELL, wrong to add. Forward max loss ≈ $400 (under the $500 per-card cap). ⚠️ No P/L-keyed harvest (durable finding 9) — suggested form if Will wants one: sell both at any Fidelity bid ≥ $3.36 (2× the $1.68 fill). Construction rule #18: the Q3 regional-bank prints (dates from company IR, REGINALD's clock) move this sector a median 2–3% (0 of 32 ≥ 10%) — a print alone rarely reaches a 4.9%-OTM strike; the 91-day tenor, not a print, is what this line holds.

**APPROVAL REQUIRED — Will must approve/reject before execution** (no action is proposed; any sale or roll is his order).
