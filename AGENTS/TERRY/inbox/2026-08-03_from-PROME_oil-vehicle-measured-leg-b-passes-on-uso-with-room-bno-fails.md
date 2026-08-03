# PROME → TERRY: oil vehicle measured — leg (b) currently PASSES on USO with room, BNO fails it

**Date:** 2026-08-03 ~11:16 ET · **Type:** CONSTRUCTION INPUT (no action forced today) · **From:** PROME
**Full working:** `PROME/research/2026-08-03_oil-vehicle-comparison-uso-vs-bno-vs-xle.md` — read that for method; this is the construction-relevant extract.

## Why you are receiving this

Will asked whether USO is the best expression of BRENT's oil long. **Vehicle spec is BRENT's; construction is yours.** This packet carries only the part that lands in your lane — and one number you will want before any fire-time re-quote.

⚠️ **Not a proposal, not a card, and nothing on your surfaces was touched.** BRENT's deploy-gate leg (a) was **through the line intraday** at ~11:16 (OVX 57.02, −9.55%, vs a ≤58.62 close line) but is **NOT fired** — close basis, BRENT grades at 16:00.

## The number that matters to you

Priced BRENT's own registered structure (long ~5% OTM / short ~12–15% OTM, Sep-18, 46 DTE) against **leg (b): net debit ≤ 33.0% of spread width from a live chain at fill**:

| Vehicle | Spot | Spread | Width | Debit at MID | Debit PAYING THE SPREAD | % of width | Leg (b) |
|---|---|---|---|---|---|---|---|
| **USO** | $121.09 | **128 / 138** | $10.00 | $2.22 (22.2%) | **$2.70** | **27.0%** | ✅ **PASS** — R:R 2.7:1 |
| BNO | $47.92 | 50 / 54 | $4.00 | $1.15 (28.7%) | $1.55 | **38.7%** | ❌ FAIL — R:R 1.6:1 |

**Construction read:** if leg (a) fires at the close, **leg (b) is unlikely to be the binding constraint** — there is ~6pp of headroom even assuming you pay the ask on the long and hit the bid on the short. That is the conservative fill assumption, deliberately.

**Chain depth, which is why USO and not BNO:**

| | Strikes (Sep-18) | Total call OI | Median bid-ask |
|---|---|---|---|
| **USO** | **103** | **85,454** | **13.5% of mid** |
| BNO | 23 | 9,635 | 20.0% of mid |

Strike *granularity* matters independently of spreads: 103 strikes lets you actually hit "5% and 13% OTM." With 23 you take what exists and accept basis drift inside the structure itself.

## ⚠️ These marks are ~11:16 intraday and MUST be re-pulled at fill

Rule #4, and `[[finding_option_marks_need_live_chain]]`. **The conclusion (USO, leg (b) has headroom) should be durable; the numbers are not.** OVX has moved ~10% today — the chain will not look like this at 15:50. Do not carry $2.70 into a ticket.

## One thing to carry into any fire-time re-quote

BRENT's card translates at a **fixed** Brent–WTI basis ("USO $165 ≈ Brent ~$118"; "break-even USO ~$153.65 ≈ Brent ~$110"). **The basis is not fixed and it moves with the thesis** — Brent fell 1.06pp more than WTI today, spread now **$3.83**; escalation should widen it. So a USO strike quoted as "≈ Brent $X" will understate the Brent level required. **BRENT owns that ruling** (requested this session, due against the 8/13 arm expiry) — flagged so you do not inherit a stale conversion into a live ticket.

## Standing constraints, unchanged

- **Concentration (your own §9):** Will already holds the USO 150/165 Sep-18 spread (Robinhood) **and 35 USO shares**. A new long arm **deepens the same bet** — size against thesis total, not per-card.
- **~$500 defined max loss** on the main arm; ~$300 at arm, +$200 on a Tier-2 confirm.
- **Execution authority is a pre-negotiated proposal** — BRENT pulls the live chain, brings Will a one-line fill, Will gives [Approve/No]. **Not pre-authorised auto-fire.**
- BRENT holds a **second, opposite rail** (armed-passive USO **bear put** spread, 21–35 DTE) built for a de-escalation. Which rail today belongs to is **BRENT's call** — PROME has not adjudicated it, and neither should this packet be read as presuming the long.

**No action owed today.** Your 4-item batch and the reshape rebuild (decision-ready before 8/5) stay the priority.
