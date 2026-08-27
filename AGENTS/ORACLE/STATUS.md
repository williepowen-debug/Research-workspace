# ORACLE STATUS

**Live dashboard — prediction-market probabilities, divergences, alerts.**
**Last pull:** 2026-08-27T18:38Z (Polymarket 43 rows + Kalshi 14 rows, both `pull --log`). **Box:** desktop (PROME-confirmed 8/27, hostname DESKTOP-BC6EF81); Kalshi signed lane **LIVE**.
**Session:** 2026-08-27 catch-up boot after **9 dark days (8/19–8/26)**.

> **Prices here are a LOG, not a live quote.** Never cite this file as the current price — re-pull. Every figure carries platform/date/volume; thin (<$5K liq) is flagged ⚠️ and is never marked on one print.

---

## 🔴 Alerts (read first)

**1. T6 pin — COMMITTED, ZERO GAPS, and the graded 8/21 reference is the CLOSE 0.32, not the intraday 0.35.**
Registered test, co-owned LIQUID/BOND, **last gradeable session Fri 2026-08-28** (Will Option C).
- **NOT FIRED on either leg.** Level 32.0% vs `<25%` trigger = **+7.0pp from the line**. 5-session leg 0.32 vs 8/20 close 0.29 = **NOT BELOW**.
- Ledger `workbook/T6_PIN.tsv`, **zero marked gaps** — the 9 dark days were recovered as **real exchange data** (Kalshi daily candlesticks), not marked as gaps.
- ⚠️ **PROME's day-1 provisional $0.35 (8/21 11:14:58 EDT) is the day's INTRADAY HIGH** — 8/21 opened 0.29, peaked 0.35 in the 11:00–12:00 hour, **closed 0.32**. Ruled the daily **close** pin-canonical on N5 clause **(i-b)**. **At an unchanged 0.32 the two candidate references give OPPOSITE leg-2 verdicts on the 8/28 path** — 0.35 fires, 0.32 does not. The ruling makes T6 *harder* to fire; disclosed as running against the more eventful outcome.
- **Fallback if ORACLE is dark 8/28:** `python3 tools/t6_pin.py --write` regenerates the window and re-grades both legs off the Kalshi creds alone, marking its own gaps. Any desk can run it. → BOND, LIQUID, PROME · KB-ORC-070 · VX-ORC-10

**2. 🟠 My own derived-series tool logged a SETTLED leg as live for six sessions — found, fixed, and it was never the arithmetic.**
`tools/disruption_supply_spread.py`'s closure context column read exactly **100.00 on 8/09, 8/11×2, 8/12, 8/18, 8/27**; last honest value **10.50 on 8/02**. Cause: the 0-ships market is a by-**date ladder** and ODDS_LOG stores only its *highest-probability* leg, so a settled July-31 rung pinned at 100% became the permanent "top." **The `RESOLVED_PROB` guard existed and was correct — it had simply never been wired to that column.** Now suppressed-and-marked. Live rungs 8/27: by-Aug-31 **11.1%**, by-Sep-30 **26.0%**. → KB-ORC-071

**3. 🟡 The same top-leg quirk produces a FALSE `⛔RESOLVED` maintenance alarm — do not retire that market.**
The dashboard has flagged 0-ships "RESOLVED — replace now (end 2026-08-01)" every session since early August. **The event is live.** Acting on the warning would have retired a live instrument. Watchlist row annotated DO-NOT-REPLACE; the warning will keep firing.

**4. 🟡 Hormuz: the crowd has written off near-term relief, and ORACLE tracks only the far leg.**
Normalization curve: **by-Sep-15 1.4%** ($828K) · Oct-31 13.5% · Nov-30 22.0% · **Dec-31 32.5%** ($9.8M — the only leg pinned). A rising ladder is arithmetically normal; **the finding is the front level** — 1.4% for the next three weeks, with by-Aug-31 at **0.4% on $16.6M**. Consequence: the spread's disruption leg (1 − P(normal by Dec-31) = 67.5%) **understates near-term severity**, where the same construction reads 98.6%. → HAWK, BRENT, FALCON · KB-ORC-072

---

## Signal Dashboard — 2026-08-27T18:38Z

### Tier 1 — direct thesis relevance
| Market | Plat | Now | Δ1d | Δ7d | Vol | Note |
|---|---|---|---|---|---|---|
| Fed: HIKE at Sept mtg (specific) | PM | **30.5%** | −4.0 | +3.0 | $10.7M | T6's fallback platform |
| Fed hike at Sept mtg (>3.75%) | Kalshi | **32.0%** | −1.0 | — | 391.0K ct | **T6 canonical** |
| Fed: HIKE in 2026 (aggregate) | PM | 57.5% | — | **+8.0** | $8.0M | off the 54.5% 8/12 trough |
| Fed: HIKE by Oct (cumulative) | PM | 44.5% | — | +4.0 | $504.6K | |
| Fed: NO cuts 2026 | PM | 87.9% | +0.6 | +1.5 | $7.6M | |
| US recession 2026 | PM | 8.5% | — | +1.0 | $1.7M | crowd calm |
| Recession 2026 (NBER) | Kalshi | 7.0% | — | — | 3.4M ct | 1.5pp from PM |
| August CPI print (modal) | PM | 48.0% | +0.5 | **+7.0** | $13.4K | ★ rolled today; prints ~9/11 |
| US inflation >5% 2026 | PM | 8.0% | +1.5 | — | $313.6K | |
| US credit rating downgrade 2026 | Kalshi | 12.0% | — | — | 74.7K ct | was 14.0% 8/12 |
| Major bank bailout before 2027 | PM | 8.0% | +1.5 | −0.5 | $4.1K ⚠️ | |
| US bank failure by Dec 31 | PM | 55.5% | −3.0 | — | $1.3K ⚠️ | ★ re-pinned (relisted slug) |
| Which banks fail by EOY (top) | PM | 3.9% | +0.7 | −0.1 | $8.3K ⚠️ | |

### Tier 2 — catalyst / theater
| Market | Plat | Now | Δ1d | Δ7d | Vol | Note |
|---|---|---|---|---|---|---|
| Hormuz normal by Dec 31 | PM | 32.5% | −3.0 | +1.0 | $9.8M | see Alert 4 |
| WTI $100 (Sep) — war premium | PM | 22.5% | +1.0 | — | $1.2K ⚠️ | ★ month-roll; **thin at inception** |
| US invade Iran before 2027 | PM | 12.5% | −3.0 | −5.0 | $62.3M | |
| Iranian regime fall before 2027 | PM | 6.5% | — | — | $25.3M | |
| Iran targets shipping (today) | PM | 51.0% | +6.5 | +31.0 | $1.4K ⚠️⏳0d | thin + 0d — **not markable** |
| Hormuz ships-transit wk of 8/24 | PM | 77.0% | −2.0 | — | $2.4K ⚠️ | ★ re-pinned; placeholder-grade |
| Hormuz avg daily transits end-Aug | PM | 98.3% | +0.4 | +2.3 | $51.7K | |
| Clarity Act signed 2026 | PM | 14.5% | — | **−11.0** | $11.2M | **only deep live >10pp mover** → BROCK |
| Russia-Ukraine ceasefire by Dec 31 | PM | 20.5% | −3.0 | −2.5 | $2.2M | |
| BOJ September decision (top) | PM | 87.5% | +1.5 | +3.0 | $122.1K | |
| BOJ September decision | Kalshi | 85.0% | −1.0 | — | 42.0K ct | 2.5pp from PM |
| AI bubble burst 2026 | PM | 11.5% | −1.5 | −1.9 | $2.3M | fading → BROCK |
| China invade Taiwan before 2027 | PM | 4.0% | −0.4 | +0.1 | $40.4M | |
| Corporate bankruptcies 2026 >750 | Kalshi | 83.0% | — | — | 6.2K ct | |

### Tier 3 — sentiment
| Market | Plat | Now | Δ1d | Δ7d | Note |
|---|---|---|---|---|---|
| Nothing Ever Happens 2026 | PM | **85.0%** | +3.0 | +3.5 | new series high — complacency extended |
| Best asset 2026 (S&P top) | PM | 53.5% | — | −8.5 | risk-on leadership eroding |
| FL Cat-4 hurricane by 2027 | PM | 17.0% | +1.0 | +1.5 | ⚠️thin → CORAL/AEOLUS |
| FL Cat-5 hurricane by 2027 | PM | 14.5% | +3.0 | +3.0 | ⚠️thin |

**Derived series:** disruption−supply spread **+45.0pp** `[v4-sep-wti-supply-leg]` — ⚠️ **regime bumped today**; the drop from +66.7 is the **August→September WTI leg swap** (0.8% with 5 days left → 22.5% with a full month), **not** supply fear catching up. **Never chart v4 against v3.**

---

## Convergence Matrix

| Axis | Crowd says | Our thesis | Gap | State |
|---|---|---|---|---|
| Fed path (Sept hike) | 30.5% PM / 32.0% Kalshi | T6 tests `<25%` | +7.0pp above trigger | 🟢 not fired |
| Recession 2026 | 8.5% PM / 7.0% Kalshi | RED still owed a current number | unmeasured since 6/13 | ⚪ stale ask |
| Bank failure / bailout | bailout 8.0%, named-EOY 3.9% | REGINALD regional stress | crowd calm, books thin | 🟢 |
| Hormuz / oil supply | 67.5% disruption, 22.5% WTI-$100 | premium ≠ shortage | spread wide (+45.0) | 🟡 premium regime intact |
| Tail complacency | NEH 85.0% (series high) | — | crowd repricing *and* pricing "nothing happens" | 🟠 standing divergence |
| Credit credibility | downgrade 12.0% | BOND owns the label | policy axis ≠ credibility axis | 🟡 |

---

## Maintenance flags

- ★ **Four rolls executed today:** July→**August CPI** (headline annual — **not** the Core ladder, which exists separately; swapping would be a silent basis change) · Aug→**Sept WTI-$100** (+ REGIME bump) · Hormuz weekly →wk-of-8/24 · bank-failure binary → relisted slug.
- ⚠️ **New supply leg is THIN at inception** ($1.2K vol vs the August leg's $706.5K). The spread's supply leg is now single-print-unreliable — flagged, not silently carried.
- ⚠️ **Do NOT replace the 0-ships market** on its false `⛔RESOLVED` (Alert 3).
- **Coverage sweep RUN today** (was 20d overdue) — 9 hits, **no new macro themes to nominate**; clock reset, next due ~2026-09-03. Minor: sports slugs (`lal-bar-bil-*`) leaked past the ex-sports filter.
- **Kalshi watchlist carries 9 `[finalized]` dead rows** (July CPI ×3, July U3 ×2, Fed-July ×2, Brent-Jul, Iran-crude) pulling as dead weight every session — **roll or freeze next session.**
- Several **past-dated Iran-shipping legs sit unresolved** (8/17 52.4%, 8/24 37.5%, 8/25 32.0%) — awaiting resolution, **not live probabilities**; do not read as signal.

---

## BOTTOM LINE

**The crowd de-risked the Fed and re-risked nothing else.** Sept-hike odds bottomed at 0.25 on 8/14–8/16 — touching but never crossing T6's line — and have ground back **+7pp** to 32.0%/30.5%, with the two platforms 1.5pp apart for the third consecutive pin. **T6 is not fired and is not close on the level leg.** The tape is much quieter than the 8/09 six-breach sweep: exactly one deep live >10pp mover (Clarity Act −11.0), with every other big Δ7d either mechanical resolution or a thin ⏳0d book.

**The two findings worth a peer's attention are both about instruments, not prices:** a graded reference value that changes T6's verdict depending on whether you read a close or an intraday capture, and a guard that was correct for six sessions while never being wired to the column it was supposed to protect.

**Standing divergence, unchanged:** *Nothing Ever Happens* at a new high (85.0%) while the same board reprices the Fed by 7pp in a week. The crowd is simultaneously repricing hard and pricing that nothing happens. → RED, VIOLET
