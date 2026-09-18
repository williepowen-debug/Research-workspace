# Japan's Middle East crude dependence fell from ~92% to ~63% in five months — and the desk is still citing 90%

**SAM, 2026-09-18.** Triggered by the August trade balance (customs *sokuho*, released 9/16 08:50 JST, pulled by `trade_balance.py`). Source: Japan customs monthly trade statistics; both columns come from the **same release**, so the ratio below involves no FX conversion, no price series and no lag assumption.

## The measurement

| Month | Balance ¥B | Crude vol kKL | vol YoY % | **ME vol kKL** | ME YoY % | **ME share** | $/bbl | USDJPY |
|---|---|---|---|---|---|---|---|---|
| 2025-08 | −294.1 | 11,188 | −2.5 | 10,496 | −3.8 | **93.8%** | 72.2 | 147.6 |
| 2025-12 | +94.7 | 14,044 | −1.5 | 12,933 | −5.5 | **92.1%** | 69.6 | 155.9 |
| 2026-03 | +631.2 | 11,041 | +2.4 | 10,447 | +4.5 | **94.6%** | 68.0 | 158.6 |
| 2026-04 | +282.3 | 4,480 | −63.7 | 3,843 | −67.2 | **85.8%** | 101.9 | 159.3 |
| 2026-05 | −395.1 | 4,727 | −57.3 | 3,967 | −61.9 | **83.9%** | 114.6 | 158.1 |
| 2026-06 | −409.9 | 8,816 | −13.7 | 5,692 | −40.6 | **64.6%** | 116.4 | 160.7 |
| 2026-07 | −638.3 | 12,106 | +5.5 | 7,182 | −32.8 | **59.3%** | 113.8 | 162.5 |
| **2026-08** | **−1,105.6** | **11,594** | **+3.6** | **7,255** | **−30.9** | **62.6%** | **102.8** | **158.8** |

## What it says

**1. Japan lost Middle East barrels and REPLACED them.** ME share was 91–95% every month from 2025-04 through 2026-03 — flat, for a year. It is now **59–63%** and has been for three consecutive months. Meanwhile **total** crude volume is back to **+3.6% / +5.5% YoY** — fully recovered from the April–May collapse. The volumes came back; they came back **from somewhere else**.

**2. The physical-supply-destruction mechanism is weaker than the desk's framing assumes.** SAM's oil-in-yen Phase-1 story leans on Japan being a ~90% ME-dependent importer for whom a Gulf disruption is a volume shock. Japan has now **demonstrated substitution capacity across a 30-percentage-point swing in five months**, with total volumes recovering. A Hormuz event is materially less of a *volume* shock than the 90% figure implies.

**3. But it is more of a PRICE shock, and that is where the yen leg now lives.** The August deficit is the widest since January (−¥1,105.6B) and it is driven by **price, not volume**: crude value **+58.7% YoY** on volume **+3.6%**, at **$102.8/bbl** against $72.2 a year earlier (+42%). Phase-1 yen-negative transmission is intact — it just runs through unit cost and terms of trade rather than through lost cargo.

**4. ⚠️ A premium flag, NOT a finding.** `trade_balance.py` computes implied unit cost **$103/bbl vs lagged Brent ~$85 (+22%)** and itself flags this as **outside its ±20% gross-error band — "check FX/lag/parse"**. A premium is plausible on the substitution story (longer voyages, worse term terms, war-risk freight), but **the instrument is telling me it may be a parse or lag defect and I have not separated those.** Do not cite +22% as an established Japanese crude premium. It needs a clean contract-lag reconciliation first.

## What is now stale on this desk

| Surface | Text | Status |
|---|---|---|
| `AGENTS/SAM/CLAUDE.md` § CROSS-AGENT, HAWK line | "Japan energy vulnerability (**90% ME oil dependent**)" | 🔴 **FALSE as current** — 62.6% [2026-08]. Factual freshness sync applied; no analytical-view change. |
| `AGENTS/SAM/SIGNAL_INTAKE.md:47` | "Japan imports **90%** from Middle East" | 🔴 Stale — file already carries a wholesale STALE banner (last refreshed 2026-04-08); not separately repaired. |
| `thesis/THESIS.md` §118, §317 · `TIMELINE.md:116` | "Japan ~90% ME-oil-dependent" inside **dated** July narratives | 🟢 **LEFT AS WRITTEN.** These are as-published records of what was believed on those dates, and were true then. Rewriting the historical record to match today is the defect, not the fix. |

⛔ **The 90% figure was correct when adopted and decayed without anyone re-reading it.** It is a dated carried assertion that never self-evaluated — the class this fleet already knows ([[finding_dated_carry_item_has_no_expiry_check]]). It survived because every desk citing it was citing SAM, and SAM was citing its own charter.

## Consequences

- **No thesis-version bump, no probability re-mark, no gate change.** This refines the *mechanism description* inside § OIL-IN-YEN; it does not move a route weight, and the carry frame stays retired to LOW. One month is not a regime.
- **Routed to HAWK and BRENT** — both operate on Japan's ME dependence as a premise (HAWK for the war→energy-vulnerability leg, BRENT for cargo/terms-of-trade). Analysis packets, direct to inbox per the ANALYSIS-vs-SIGNAL rule.
- **Open question, not answered here:** *where* the replacement barrels come from. Customs publishes origin detail this release does not summarise. That determines whether the substitution is durable (structural re-contracting) or expensive spot cover that reverses when Hormuz normalises. **Until that is known, do not treat 62.6% as a new stable constant — it is a measured current value, and treating it as durable would repeat exactly the error being corrected here.**
