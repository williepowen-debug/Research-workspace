---
signal_id: SIG-W-20260621-007
dispatched: 2026-06-21T22:48:00Z
origin: Will Telegram intake (3rd 6-image batch, msgs 2554-2559, 2026-06-21 ~22:46 UTC)
source: Data Driven Stocks @stockdatamarket (X) — "How the VIX opens after a long weekend" (CBOE VIX daily open/close via Yahoo Finance, 1990-2026, n=232)
signal_type: seasonal-pattern
domain: VOL
cluster: POSITIONING_VALUATION
signal_role: primary_substance
narrative_channel: n/a
precedence: PRIORITY
to: VIOLET
info: [HENRY, RED]
confidence: 0.75
verify_verdict: SKIP-VERIFY (backtest from CBOE VIX daily data, n=232; methodology stated — the "weekend effect" is a documented IV-decay-on-a-365-day-clock artifact)
verify_method: BOARD-grep novel; named backtest, no verify-spawn (statistical-pattern caveat in body)
---

# VIX gaps UP 87% of the time on the first session back from a long weekend — and Mon 6/22 IS that session (post-Juneteenth)

## Substance (SKIP-VERIFY 0.75)

Data Driven Stocks backtest (1990-2026, n=232): on the **first trading session after a holiday long weekend, the VIX gaps UP ("fear") 87% of the time, vs a 47% baseline** on any ordinary day. The average opening gap is **+5.09% (+0.92 VIX pts) after a long weekend vs +0.41% ordinary.** Mechanism (stated): implied vol is priced on a 365-day clock but decays only on trading days, so IV is marked DOWN over the closed weekend/holiday and **pops back up at the next open** — a long weekend amplifies the effect.

**Why now:** **Monday 6/22 is the first session back from the Juneteenth (Fri 6/19) 3-day weekend** — exactly the setup this stat describes. (Cross-ref: SAM's "Mon CFTC, Juneteenth-delayed" confirms the holiday calendar.)

## Why it matters — a structural up-bias on a Monday that's already loaded

**VIOLET (action) — vol-regime:** this is a **structural ~+5% VIX-open bias for Mon 6/22**, stacking on top of an already-loaded first-session-back: the Mon Brent open is the Iran-decoupling test (SIG-W-20260621-001/-004), the positioning tape is at froth extremes (SIG-W-20260621-002 concentration + -006 levered-ETF $464bn), and quarter-end rebalancing flows hit into June 30 (SIG-W-20260621-008). The VIX-weekend-effect is a **mechanical open-print artifact, not a regime call** — it typically fades intraday (IV re-decays) — so treat it as "expect a higher VIX *open*, don't read it as fresh fear" unless a real catalyst (Brent spike / headline) co-fires. The value is knowing the open gap is mechanical so you don't over-read it (or, conversely, so a *muted* open despite the long weekend is itself informative).

**HENRY (info) — index-mechanics:** the VIX-open bias is the vol-side companion to the Monday tape you'll be reading (Brent + month-end flows + froth positioning). A mechanically higher VIX open ≠ a down-equity signal on its own.

**RED (info):** n=232 backtest, mechanical artifact — steelman the "this is just IV-clock decay, not predictive of direction" read. It biases the *VIX open level*, not equity direction or realized vol; don't let a higher VIX open be miscoded as a confirmed fear signal.

## Source framing

Named backtest with a stated, well-understood mechanism (the VIX weekend effect is real and documented). Route as **"expect a mechanically higher VIX open Mon 6/22; it's an artifact, not a fresh-fear signal."**

## AIGs / cross-refs

- BOARD: SIG-W-20260621-002 (concentration), SIG-W-20260621-006 (levered-ETF froth), SIG-W-20260621-008 (quarter-end rebalancing), SIG-W-20260621-001/-004 (Mon Brent decoupling test) — all converge on Mon 6/22 being a loaded first-session-back
- VIOLET STATUS 6/12 (complacency tape into stacked catalyst window)

## Provenance

- Intake: Telegram 3rd 6-image batch msgs 2554-2559, 2026-06-21 ~22:46 UTC
- Pipeline: BOARD-grep novel + timeliness check (Mon 6/22 = first session back from Juneteenth weekend) → SKIP-VERIFY (named backtest) → dispatch
