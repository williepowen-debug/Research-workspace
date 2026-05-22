# NEXUS SIGNALS — Active Cross-Agent Signal Tracker
**Purpose:** Live, unresolved signals flowing between agents. Signals are inputs — once absorbed into a convergence (STATUS.md) or resolved, they move to archive.
**Last Updated:** 2026-04-04 16:30 UTC | **Last Pass:** 12 (Apr 4)

---

## Lifecycle
1. Signal arrives (inbox, agent outbox, PROME route)
2. NEXUS evaluates: new convergence? upgrades existing? contradiction?
3. **If absorbed** → archive to `domain/signals_archive/` with mapping
4. **If resolved** → archive with outcome
5. **If still developing** → stays here

---

## ARCHIVED (detail in `domain/signals_archive/SIGNALS_THROUGH_PASS11.md`)
SIG-001→C-11 | SIG-002→C-11 | SIG-003→C-02/C-16 | SIG-004→resolved | SIG-005→resolved | SIG-006→C-10 | SIG-007→C-10 | SIG-008→resolved | SIG-010→C-02/C-16 | SIG-011→C-32 | SIG-012→C-10 | SIG-013→thresholds | SIG-014→QUEUE | SIG-018→T-15 | SIG-021→C-29 | SIG-030→T-15 | SIG-032→thresholds | SIG-033→C-34 | SIG-034→C-27 | SIG-035→C-02 | SIG-036→C-07/C-34 | SIG-037→thresholds | SIG-038→C-21 | SIG-039→findings | SIG-040→findings | SIG-041→C-07/C-34 | SIG-042→findings | SIG-043→findings | SIG-044→C-17 | SIG-045→T-15

---

## 🟠 ACTIVE

| SIG-ID | Date | From → To | Signal | Status | Priority |
|--------|------|-----------|--------|--------|----------|
| SIG-015 | 2026-03-25 | LABOR → NEXUS | **Meta layoffs executing** — "several hundred" across Reality Labs, Facebook, recruiting. First tranche of ~15K/20% pipeline. Tech layoffs accelerating. | 🟠 Developing — feeds C-02 upstream (employment → credit) | 🟠 |
| SIG-017 | 2026-03-25 | SAM → NEXUS/HENRY | **Ceasefire rally pattern = relief, not reversal** — Tehran denied negotiations throughout. Pattern repeats with each headline. | 🟠 Recurring — T-14 tension | 🟠 |
| SIG-019 | 2026-03-26 | HAWK → HENRY | **Russia suspends ammonium nitrate exports** — Combined with China N-K halt + Gulf urea impairment = THREE major fertilizer sources offline. Urea +40% ($700/mt). Q3-Q4 food CPI lock-in. | ✅ Absorbed → **C-35 NEW** (Fertilizer Supply Collapse) | 🔴🔴 |
| SIG-020 | 2026-03-26 | HAWK → HENRY/NEXUS | **Israel strikes Caspian Sea weapons route** — War theater expanding. Drones, oil, wheat route disrupted. | 🟠 Active — feeds C-10 theater expansion | 🟠 |
| SIG-031 | 2026-03-24 | NEXUS → CARL | **FL UI Wave 2 — Apr 26 peak** — Mechanical. Second WARN cohort exhaustion wave. | 🟡 Scheduled — 22 days out | 🟡 |

---

## Signal Cleanup Protocol
- **Absorbed into convergence** → archive with C-XX mapping
- **Event resolved** → archive with outcome
- **2 passes without change** → archive or flag stale
- 🔴🔴🔴 = immediate / position decision | 🔴🔴 = active catalyst | 🔴 = monitoring | 🟠 = developing | 🟡 = background
