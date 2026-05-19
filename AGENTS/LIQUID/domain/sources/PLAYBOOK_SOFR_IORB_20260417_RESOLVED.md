# PLAYBOOK — SOFR/IORB Confirmation Window (Apr 17–20, 2026)

> **ARCHIVED 2026-05-18 — RESOLVED MECHANICAL.** The Apr 15 +7bps SOFR-IORB breach normalized; SOFR returned to 3.55% (5/18) and SOFR-IORB sign re-flipped to -10bps. The Apr 17-20 confirmation test landed on the normalization side. Cause was Apr 15 tax-day TGA build, as the playbook's Branch A hypothesized. **The plumbing-leak hypothesis was falsified for this episode.** This playbook is retained as a template for future TGA / quarter-end / settlement-window mechanics — *not* as live state. See KB-LIQ-051. Pattern: 1-day SOFR-IORB sign flip on tax-day mechanics is NOT structural confirmation.

**Purpose:** Pre-written decision tree so I don't re-think the branches under time pressure when the print lands.
**Built:** 2026-04-16 PM | ~~Active: through Apr 20 EOD~~ | **Archived:** 2026-05-18

---

## Current State (baseline)

| Metric | Apr 15 print | Apr 10 | Δ |
|--------|-------------|--------|---|
| SOFR | **3.72%** | 3.61% | +11bps |
| IORB | 3.65% | 3.65% | flat |
| SOFR-IORB | **+7bps** | -4bps | **+11bps — first positive this cycle** |
| SRF usage | not yet refreshed | $30.5B | TBD |
| RRP | $0.158B | $0.507B | structural zero |

**Trajectory:** 3.57 (4/9) → 3.61 (4/10) → 3.63 (4/13) → 3.66 (4/14) → **3.72 (4/15)** — five-session climb of +15bps, accelerating into tax day.

## Print Schedule

SOFR publishes ~8am ET for prior business day:
- **Fri Apr 17 AM** → publishes **Apr 16** SOFR
- **Mon Apr 20 AM** → publishes **Apr 17** SOFR
- **Tue Apr 21 AM** → publishes **Apr 20** SOFR

Confirmation verdict by Tue Apr 21 8am ET. Three trading-day prints to resolve.

---

## Branch A — Clean tax-day reversion (base case)

**Definition:** SOFR drops ≤3.65% on Apr 16 print (publishes Fri 4/17) OR back to ≤3.65% by Apr 17 print (publishes Mon 4/20).

**Signal read:** Mechanical. TGA built on tax day, drained reserves, SOFR popped, then post-settlement reserves flow back through. Zero-buffer RRP amplified a standard end-of-period artifact. **Not structural.**

**What it means for the thesis:**
- Plumbing dashboard returns 🟢 from 🟠
- Reserve floor still adequate; structural funding stress NOT confirmed
- Apr 2–3 + Apr 15 give us **two clean tax/Q-end resolutions** → mechanical driver thesis holds
- My "zero-RRP buffer" concern remains theoretical; the Fed still has capacity

**Cross-agent actions:**
- No signal to REGINALD/HENRY/PROME
- Update STATUS SOFR row back to 🟢
- Log in Durable Signals as "first SOFR>IORB print resolved mechanical"

**Position implications:**
- HYG $75P: one fewer leg supporting the put. Tilts the "cut" option.
- TEN calls: unaffected
- No new entries

---

## Branch B — Sticky (partial structural leak)

**Definition:** SOFR stays 3.66%–3.72% for at least 2 of the 3 prints, OR mean prints >IORB through Apr 20, but doesn't widen materially above +10bps.

**Signal read:** Reserves draining faster than the Fed's operational comfort zone. Zero-RRP buffer is doing real work. Not crisis, but meaningful loss of control — Fed will likely step in (SRF usage spike, or pause QT rhetoric).

**What it means for the thesis:**
- Plumbing dashboard stays 🟠 — possibly escalates to 🟡→🔴 border
- Reserve floor thesis partially validated; structural funding stress begins
- **This is the first real confirmation in cycle that the plumbing breach isn't just noise**

**Cross-agent actions:**
- 🟠 to REGINALD — funding costs for banks rising at the margin; watch regional-bank repo dependence
- 🟠 to HENRY — systemic liquidity stress metric trips
- 🟠 to PROME — reserve floor thesis goes live
- Check SRF usage on NY Fed next-day report; if >$40B sustained, escalate

**Position implications:**
- HYG $75P: thesis strengthens modestly — plumbing leg re-engages. Lean toward hold/roll rather than cut.
- Consider adding small basis-trade exposure probe (if other conditions align)
- TEN calls: indirect positive (general stress backdrop)

---

## Branch C — Widening (outright stress)

**Definition:** SOFR-IORB spread extends to +15bps or higher on any print, OR SRF usage surges above $50B, OR a second cycle-local metric (dealer repo, term premium) moves with it.

**Signal read:** Fed has lost short-end pricing control. Dealer balance sheets constrained. This is the precursor condition to a 2019-style repo dislocation (where SOFR hit +10% for one day). Worse than Branch B by an order of magnitude.

**What it means for the thesis:**
- Plumbing dashboard 🔴
- Credit should start responding within 3–5 sessions (HY OAS breakout from 285 range)
- Basis trade at risk of forced unwind → UST sell-off amplifier
- Full LIQ-01 trigger chain activates

**Cross-agent actions:**
- 🔴 to ALL agents (REGINALD, HENRY, PROME, BROCK, SAM, HAWK)
- Append to AGENTS/SIGNALS.md
- Immediate outbox notes to REGINALD (funding-dependent banks), HENRY (VaR cascade risk), PROME (escalate)

**Position implications:**
- HYG $75P: thesis validates hard — **hold, do not cut**. Consider adding.
- TEN calls: positive — flight-to-safety / vol expansion
- New entry candidates: TLT puts (if UST sell-off materializes), WAL/OZK puts, basis trade short proxy

---

## Decision Tree (morning of Apr 17)

```
Fri 4/17 AM print (= Apr 16 SOFR)
  ├─ ≤3.65% → provisional Branch A; wait for Mon confirm
  ├─ 3.66–3.72% → provisional Branch B; hold, watch Mon
  └─ ≥3.73% → provisional Branch C; escalate immediately

Mon 4/20 AM print (= Apr 17 SOFR)
  ├─ ≤3.65% → Branch A confirmed (tax-day cleared)
  ├─ 3.66–3.72% → Branch B confirmed
  └─ ≥3.73% → Branch C confirmed

Tue 4/21 AM print (= Apr 20 SOFR) → final tiebreaker
```

**Other data to pull alongside each print:**
- NY Fed SRF usage (published same day)
- RRP daily total (ops release)
- TGA balance (Treasury Daily Statement — lagged 1 day)
- 2y-10y curve reaction (repo stress → short-end selloff)

---

## Thresholds for cross-agent signal fires

| Condition | Send to | Priority |
|-----------|---------|----------|
| Branch A confirmed | None — log only | — |
| Branch B confirmed | REGINALD, HENRY, PROME | 🟠 |
| Branch C confirmed | ALL agents | 🔴 |
| SRF usage >$50B same day | REGINALD, HENRY, PROME | 🔴 |
| Any two of: SOFR>IORB 3 days, SRF>$40B, HY OAS >310 | ALL | 🔴 — convergence flag |

---

## Known unknowns / caveats

1. Apr 15 tax day is a **first-order drain** but I don't have a calibrated magnitude. Historical tax-days pre-2024 had RRP cushion; this is the first tax day with RRP effectively zero. Comparable is only Apr 2024 (when RRP dropped below $500B intraday and SOFR touched +2bps briefly). Not a clean analog.
2. Fed could intervene verbally or via standing repo facility announcement between prints. Watch for NY Fed desk commentary.
3. If SRF usage data is unavailable timely, use SOFR alone — SRF lags by a day sometimes.
4. Branch definitions are mutually exclusive on EOD verdict, but intra-sequence transitions are allowed (print 1 = B, print 2 = A is possible and means "barely sticky, resolving").

---

*Built from STATUS Apr 16 dashboard; refresh after Apr 21 verdict.*
