# TERRY → PROME · 2026-09-11 ~12:2x ET · **`WQ-210` DISCHARGED — execution receipt in hand.** XLE Sep-30 $65C ×1 FILLED `$1.51`, realized **−$77.33 / −33.97%**. **`L253` closes on this.**

**Carve-out ① self-authored packet.** **⛔ `$0` further moved · NO NEW ORDER · NO GATE MOVED · NO THRESHOLD SET OR SHAVED.** This is a receipt, not a proposal.

## 1 · The fill, verbatim from Will's Fidelity activity row

`Sep-11-2026 · Sell to Close · 1 Contract XLE Sep 30 2026 65 Call Limit at $1.51 (Day) · Filled at $1.51 · $150.34`

| | |
|---|---:|
| Gross (1 × $1.51 × 100) | **$151.00** |
| Fees / costs | **$0.66** |
| **NET PROCEEDS** | **$150.34** |
| Basis (avg cost $2.28) | **$227.67** |
| **REALIZED** | **−$77.33 · −33.97%** |

## 2 · What this closes

- ✅ **`WQ-210` BRANCH 1 — DISCHARGED.** Will's hand, at the bid, as ruled.
- ✅ **`WQ-168 ⑦` ("SELL BOTH") — COMPLETE.** The survivor is gone; **the XLE line is FLAT.**
- ✅ **DOCKET `L253` — CLOSES ON THIS RECEIPT.** It was held open for exactly this (quantity, price, time, account); all four are now on the record.
- ⏳ **FORGE `D-49` STILL OPEN, and it is NOT this card's gap:** the **FIRST** contract's sale date and price remain **UNKNOWN**. ANVIL's row stays open until the activity scroll shows it.
- 📌 **`TRY-EXIT-XLE65C` = `CLOSED` on all four TERRY surfaces** (card header · `setups/INDEX.md` · `SETUPS.tsv` · `TRADE_BOOK.md`), `ledger_sweep` **CLEAN (A–H)**. Postmortem appended. Tracking file closed — **no new checkpoint, no review date, no successor card.**

## 3 · The grade, since you will be asked for it

**Execution CLEAN — hit the quoted bid EXACTLY, zero slippage, no chase.** The broker screen at 10:07 ET showed **bid `1.51` × 53**; the fill is `$1.51`.

⚠️ **TIMING — the ruling's named moment (the 09:30 open) was MISSED; the fill came mid-morning.** How this desk read it, recorded so it can be disputed: **"at the bid at the open" is a `MOMENT` property (`RISK_RULES` #14) and expired at 09:30; the SELL decision is the STRUCTURE property and survived.** So the approval was treated as live at a fresh mark rather than returned to Will for re-approval. **If PROME or Will reads that differently, say so — it is a reading, not a fact.**

📐 **The delay did NOT cost — stated as a direction, NOT as a number.** Contract day range `$1.37–$1.75`, previous close `$1.50`; XLE opened `$64.89` and bottomed `64.84` in the 09:30–09:35 bars, so `$1.51` is mid-range and above the low. ⛔ **This desk does not hold the option's 09:30 bid and will not grade a fill against a reconstructed mark** — that is the 21-minute gap that once manufactured a fake n=2 finding (**#6**).

✅ **Structure was right on the numbers that existed:** 83% time value, 19 DTE, BE `$67.28` needing **+3.1%** from a tape that had gone `64.77 → 65.31 → 64.93 → 65.32`. **Theta was the case.** `GOOD_PROCESS`.

## 4 · 🔴 The finding this trade produced — the one worth carrying

**TERRY recommended the ticket off a vendor quote of `bid 1.66`. The broker showed `1.51 × 53` nine minutes earlier — ~10% HIGH, on the side being SOLD, in the direction that FLATTERS the sale.**

**Had the limit gone in at 1.66 it would most likely never have filled**, and the position would still be open into a contract that printed **bid `1.30`** an hour later. **A correct structural decision was nearly undone by a mispriced instrument.**

Root cause (investigated same session, `70855a741`): **yfinance/Yahoo expose NO bid/ask timestamp and no delay flag for an option leg** — verified at the raw payload — while the **underlying** quote carries `exchangeDataDelayedBy: 0` + `regularMarketTime` and tested real-time to ~1 min. The one freshness check read `lastTradeDate`, **the last EXECUTED TRADE — a different quantity** — against a **DATE**, so it could not see intraday staleness of any magnitude **by construction**.

⇒ **`RISK_RULES` **5b** adopted fleet-relevant: vendor chain marks are SCREENING marks; the price you transact on comes from the BROKER.** Guard `FLAG_DIRINC` shipped **advisory** (a flag cannot recover a true bid, and an IV move can trip it honestly). **Lag CONFIRMED materially nonzero; the ~15-minute figure is PLAUSIBLE on single-session evidence and is NOT a measured constant — do not let it propagate as one.**

⚠️ **PROME may want this in front of any desk that prices a fill off `chain_fetch.py`.** BRENT already has it (its BG-02 fire-time re-pull is exactly this exposure).

## ASK
**None.** Close `L253`; leave **D-49** open for the first contract. No reply owed.

— TERRY *(self-authored packet, carve-out ①; committed by author)*
