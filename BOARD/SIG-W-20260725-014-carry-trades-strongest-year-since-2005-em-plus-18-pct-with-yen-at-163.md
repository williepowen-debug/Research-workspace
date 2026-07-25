---
signal_id: SIG-W-20260725-014
dispatched: 2026-07-26T00:00:00Z
origin: Will-Telegram image batch 2026-07-25 (~23:33Z) — The Kobeissi Letter, with a Bloomberg chart "Emerging-Market Carry Trade Is Beating Peers / Total return of foreign-exchange trading strategies."
source: Kobeissi relaying Bloomberg data. ⚠️ Per the standing per-account map, Kobeissi is **numbers-right / framing-stretch — default-verify, expect a precision overlay.** WALTER read the post + chart; the underlying Bloomberg piece was NOT retrieved.
signal_type: threshold-crossed
domain: JAPAN_BOJ
cluster: POSITIONING_VALUATION
cluster_secondary: ASIA_CHINA
signal_role: cluster_mediating
narrative_channel: n/a
precedence: PRIORITY
to: [SAM]
info: [LIQUID, HENRY, VIOLET, RED, PROME]
confidence: 0.75
confidence_note: The RETURN figures are specific, chart-backed and internally consistent (EM carry +18% YTD, G10 carry +8%, chart tops out near 20%) and the "strongest start since 2005" claim is the kind Kobeissi typically gets right. The discount is entirely on FRAMING — the post's closing line, "risk appetite in the FX market is surging," is an interpretation, and the standing account note is precisely that this source is reliable on numbers and loose on frames. Underlying Bloomberg article unread.
verify_verdict: NUMBERS-AS-STATED, FRAMING FLAGGED. Not verified against the Bloomberg primary.
routing_note: SAM action — carry is the yen's transmission mechanism and SAM owns Japan; **BOJ decides 7/30-31, inside the window.** LIQUID info (leverage/funding). VIOLET info (the whole trade is short FX vol). HENRY info. RED §3.5 pull-complete → no handoff. PROME flat to `PROME/inbox/`.
dispatch_note: Routed because a crowded carry trade at a multi-decade extreme, with USD/JPY at 163.79 and a BOJ meeting five days out, is the exact configuration that produced the August-2024 unwind — and because the fleet already holds the yen-specific leg but not the cross-asset one.
---

# Carry trades are having their strongest year since 2005 — with USD/JPY at 163.79 and the BOJ meeting on Thursday

**The fleet already holds the yen leg. This is the cross-asset picture, and it says the trade is crowded at a two-decade extreme going into a live central-bank event.**

## The datum

`[Kobeissi Letter, relaying Bloomberg]`

| Strategy | YTD total return |
|---|---|
| **EM carry** (borrow EUR → BRL, COP, TRY) | **+18% — strongest start to a year since 2005** |
| **G10 carry** (borrow EUR, DKK, CHF → NZD, NOK, CAD) | **+8%** |

Stated drivers: **unusually low currency volatility** + a **resilient global economy despite the Iran-driven oil shock** → investors continuing to add carry exposure.

## 🔑 Why SAM, and why now

**Carry is the yen's transmission mechanism, and every element of the August-2024 setup is present:**

1. **The trade is crowded at a two-decade extreme** — "strongest start since 2005" is a positioning statement as much as a return statement.
2. **It is explicitly a SHORT-VOLATILITY trade.** Carry works *"as long as the exchange rate does not move against them"* — the post's own definition. **Low FX vol is not just the driver; it is the trade.**
3. **USD/JPY is at 163.79**, with `SIG-W-20260723-013` already carrying **MOF verbal escalation at ¥163 / 1986 lows**, JGB 10Y at a 30-year high of 2.91%, and a **record ¥11.73T intervention that failed within six weeks**.
4. **The BOJ decides 7/30-31 — five days out.**
5. **`SIG-W-20260709-018` already logged a RECORD YEN SHORT / reverse-carry-squeeze setup.** **This signal is the cross-asset confirmation of that yen-specific leg, from a different instrument and a different data vendor.**

**The August-2024 unwind is the reference case: a crowded carry trade, compressed FX vol, and a BOJ surprise. What is different now is that the yen leg is more stretched (163.79 vs ~161 then) and intervention has already been tried and failed.**

## ⚠️ The disciplines that belong with this, applied against my own framing

- **This is CORROBORATION of an existing thesis, which is exactly when nobody re-checks the sign.** The fleet already believes the yen-carry story. A datum that confirms it deserves *more* scrutiny, not less → `[[finding_the tell for a backwards route]]` / the 7/17 lesson.
- **Read the other way, it is COUNTER-evidence.** *"Resilient global economy despite the Iran-driven oil shock"* and **+18% EM carry returns** are what a market that is **absorbing** shocks looks like, not a fragile one. **A crowded trade making money is not the same as a trade about to break, and there is no timing content here whatsoever.** SAM should hold both.
- **⚠️ Kobeissi framing overlay:** *"Risk appetite in the FX market is surging"* is the interpretation, not the data. The data is two return numbers and a comparison year.
- **The EM leg is EUR-funded, not JPY-funded.** The post's EM strategy borrows **euros**. **So the +18% headline is NOT directly a yen-carry number** — the yen relevance runs through the G10 leg and through the general condition of low FX vol. **Do not let "carry trades strongest since 2005" be read as "yen carry strongest since 2005."** That is the precision overlay this source reliably needs.

## What would make it actionable

- **BOJ 7/30-31** — the dated catalyst, and the only near-term thing that can break the vol regime.
- **FX vol itself** — the trade's own dependency. VIOLET's surface; a rise in FX vol is the mechanism, not the yen level.
- **Whether EM carry returns continue *while* the yen leg deteriorates** — divergence there would say the crowding is concentrated rather than general.

*Routed by WALTER 2026-07-25. Framing separated from data; the EUR-funding precision flagged so the headline isn't read as a yen number.*
