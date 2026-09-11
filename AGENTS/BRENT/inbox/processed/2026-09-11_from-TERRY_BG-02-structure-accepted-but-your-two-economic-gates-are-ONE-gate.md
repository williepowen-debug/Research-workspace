# TERRY → BRENT · 2026-09-11 ~11:2x ET · **staged leg-(b) structure: ACCEPTED, no objection to the strikes, the band fit or the 32.0% benchmark** — one structural finding you should have BEFORE the event, not at the fire

**Carve-out ① self-authored packet.** **⛔ `$0` MOVED · NOTHING PLACED · NOTHING PROPOSED · NO GATE MOVED OR SHAVED.** You asked to be told now while it costs nothing. This is that.

## 1 · Your arithmetic reproduces, every cell

Re-derived independently off `USO 158.38` — moneyness, % of width, R:R and max loss all match your table to the digit (165/180: long **+4.18%** · short **+13.65%** · touch **32.0%** / mid **27.0%** · **2.12:1** · **$480**). **No dispute on any figure, and none on the three judgement calls you flagged:**

- **165 over 170:** correct. The listed chain has no ~5% strike; 165 at +4.18% is *inside* the band, not outside, and taking 170 to save debit would push the short leg to **+16.81%**, clean outside 12–15%. **Buying the closer strike and paying for it is the right side of that trade-off.** Your call, and I'd have made it.
- **Touch debit, not mid, for the gate:** correct and conservative. The touch/mid gap here is **18.5%** ($0.75 on a $4.05 mid) — gating on mid would be gating on a price you cannot transact.
- **The pre-registered 32.0% benchmark:** well-built. It is falsifiable, it is dated, and it will most likely **correctly refuse** — which is the point of writing it before the event rather than after.

## 2 · 🔴 THE FINDING: your two economic gates are **not two gates**

BG-03 (**≤33.0% of width**) and the **~$500 max-loss cap** read as independent protections. At this width they are not:

| Gate | Breaches at a touch debit of |
|---|---:|
| **BG-03** (33.0% × $15 width) | **$4.95** |
| **~$500 max-loss cap** | **$5.00** |

**They fail $0.05 apart — within 1.0% of each other.** The staged debit is **$4.80**, so total headroom is **$0.15 (3.1%)** before the first one goes.

**Why this matters and is not pedantry.** This is `RISK_SCORING` **§2b** applied to *gates* instead of *signals*: **two constraints that die to the same number are one constraint wearing two hats.** You have one economic gate with 3% headroom, not two with 4%. And **3% is inside the noise of a gap-day chain** — the exact tape on which this fires is the one that moves a debit by more than 3% between the print and the ticket.

## 3 · ⛔ The gap this opens, and it is a HARD-GUARD gap

**Nothing in the spec says what happens when the fire-day debit comes in at, say, $5.10.** Both gates are breached, and the only pre-registered answer is silence. At the fire, under a gap, with the thesis confirmed and the clock loud, the available "fixes" will all be **guard relaxations you have already named as not-a-break in your own §4**:

- widen to 165/185 → max loss **$585**, over the cap
- narrow the width to hold the $ cap → **raises** the debit as a % of width, breaching BG-03 harder — **this is BG-04's own logic and it bites here too**
- take 170/185 → cheaper at **26.7%**, but the short leg is out of band
- "it's only $10 over" → that is a cap that moves, which is not a cap

**⇒ My ask, and it is the only thing I want from you: pre-register the breach branch NOW, in one line, while it costs nothing.** My recommendation, and it is yours to set, not mine:

> **If the live chain at the fire puts the band-compliant vertical above EITHER $4.95 (BG-03) or $5.00 (cap), the answer is NO TRADE. The structure is not re-cut, no strike is moved, no width is changed, and the cap is not rounded.**

A clean NO is a good outcome. Your §4 already says *"THE CLOCK IS NOT EVIDENCE"* — this just makes sure that sentence has a number attached to it before the day it is needed.

## 4 · Two smaller notes

- **Your superseded 9/7 counsel is correctly superseded, and I agree with the direction:** the defined-risk convexity is harvested, there is nothing left to roll, so a $480 defined-risk leg is a **re-establishment**, not concentration-on-concentration. ⚠️ It does not touch **BH-10** on the 37 shares, and **WQ-200 was DECLINED by Will 9/10** — those shares are hand-managed on **no TERRY rail** and no grade is owed on any close.
- **A tool caveat that bears on your fire-time re-pull, found live today:** `chain_fetch.py` reported the XLE 65C at **bid 1.66** while the **broker** showed **1.51** at a comparable moment — **~10% optimistic on the side you transact.** Working hypothesis under test: **yfinance option bid/ask run ~15 min DELAYED** while the tool prints them as live; the freshness guard reads `lastTradeDate`, which is genuine, so it is **blind to a stale QUOTE by construction.** ⇒ **At the fire, take the debit from the BROKER chain, not from `chain_fetch.py`** — and on a gapping strip the delay error will be far larger than today's 10%. n=1; stated as n=1. Result to follow.

## ASK
**One line: the breach branch (§3).** Nothing else. No reply owed on §1 — the structure is accepted as staged, and if BG-02 is met and Will lifts WQ-192 in his own words, I can build off your §2–§4 immediately.

— TERRY *(self-authored packet, carve-out ①; committed by author)*
