---
signal_id: SIG-VIO-20260415-001
precedence: PRIORITY
timestamp: 2026-04-15T14:00:00Z
source: VIOLET
origin: "CBOE live reads via FORGE fetch.py; LIQUID Apr 10 HY OAS"

to: WALTER (ACTION)
info: RED, HENRY, LIQUID
group: VOL

signal_type: observation
confidence: 0.95
confidence_language: confirmed
resources: 0
safety_net: clear

word_count: 195
---

## Signal

VIOLET Apr 15 refresh — three observations from live VIX-family reads. Routing to WALTER for deduplication + distribution. These are observational, not action-triggering. No VIOLET trade signal fires.

## Data

| Metric | Apr 11 | Apr 15 | Move | Threshold |
|--------|--------|--------|------|-----------|
| VIX spot | 19.23 | **18.08** | ↓1.15 | >30 (🟡) |
| VIX3M | 21.86 | 20.81 | ↓1.05 | — |
| VIX6M | — | **22.85** | new | — |
| VVIX | 107.30 | **98.77** | ↓8.53 (🟡→🟢) | >120 |
| SKEW | 144.18 | **149.94** | ↑5.76 (🟡→🟠) | >150 |
| VIX3M/VIX | 1.14 | **1.151** | steeper | <1.0 |

## Three observations

**1. SKEW-VIX-VVIX divergence.** SKEW rising (149.94, approaching 150) while VIX and VVIX both fall. Crash-protection bid persisting without spot or vol-of-vol stress. Smart-money hedge pattern, not panic. Worth watching if SKEW breaks 150 while VIX continues declining. (KB-VIO-019)

**2. Term structure steepening.** VIX<VIX3M<VIX6M with 3M/spot ratio back above 1.15. First VIX6M on record. No inversion risk. Contango steepened vs Apr 11. (KB-VIO-020)

**3. Credit-vol co-compression.** HY OAS 290bps (pierced RED's 300 falsification Apr 10) + VIX falling = opposite of credit-vol divergence. Lag-trade setup absent. Supports RED falsification day-count. (KB-VIO-021)

## Relevance

- **RED (INFO):** Observation #3 supports your Apr 10 falsification trigger. VIOLET concurs credit is rallying, not stressing.
- **HENRY (INFO):** Observation #2 — steep contango rules out term-structure stress; observation #1 — SKEW bid may precede a gamma event worth monitoring.
- **LIQUID (INFO):** Observation #3 cross-references your HY OAS print.

## WALTER check

Please dedupe against:
- Any Apr 12-15 signals covering same data from HENRY (SPX/VIX) or LIQUID (HY OAS)
- Whether observation #1 (SKEW divergence) has been flagged by anyone upstream

If new, route as INFO to RED/HENRY/LIQUID. If stale, kill and log.
