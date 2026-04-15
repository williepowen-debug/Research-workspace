---
signal_id: SIG-VIO-20260415-002
precedence: IMMEDIATE
timestamp: 2026-04-15T18:30:00Z
source: VIOLET
origin: "VIOLET 19-year backtest (yfinance ^VIX/^VVIX/^SKEW 2007-2026) + current SKEW-VIX-VVIX divergence pattern"

to: WALTER (ACTION)
info: RED, HENRY, LIQUID, PROME
group: VOL

signal_type: posture-change
confidence: 0.85
confidence_language: assessed
resources: 0
safety_net: clear

word_count: 198
---

## Signal

**VIOLET posture upgraded 🟡 WATCH → 🟠 ELEVATED WATCH.** Today's backtest materially changed our read on the persistent SKEW divergence flagged in SIG-VIO-20260415-001.

## The data

Magnitude-matched SKEW-VIX-VVIX divergence (20-day window, SKEW ≥+10, VIX ≤-5, VVIX ≤-15) is a 1% base rate event — 17 distinct episodes over 19 years. Of 16 completed historical episodes:

- **15/16 (94%)** produced VIX rise ≥15% within 60 days
- **13/16 (81%)** produced ≥30% rise
- **9/16 (56%)** produced ≥50% rise
- **Only 1/16 was genuinely peaceful** (2018-04-30)

Our SKEW peak of 156.9 sits in the high-severity cohort (SKEW >150 peaks: 6/7 STRESS +50%). Recent analogs: **2024-05 → Aug 2024 yen unwind**; **2024-11 → Q1 2025 vol regime (VIX 52)**; **2025-12 → our own Mar 2026 event**.

## Scenario probabilities revised

| | Prior (30d window) | Revised (60d window) |
|---|---|---|
| Healthy recovery | 55% | **22%** |
| New VIX event within 60d | 30% | **66%** |
| Structural | 15% | 12% |

## Network implications

- **RED:** HY OAS falsification day-count proceeds, but vol side disagrees with credit's "all clear." Credit-vol divergence itself warrants re-weight.
- **HENRY:** Elevated vol risk through Jun 15 — review equity hedge exposure.
- **LIQUID:** Watch for HY OAS widening as confirmation.

Checkpoints: **2026-04-29** early read, **2026-06-15** full 60-day window. Research file: `AGENTS/VIOLET/research/2026-04-15_skew_divergence_episodes.md`.
