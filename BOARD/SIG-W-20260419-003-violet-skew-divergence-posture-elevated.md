---
signal_id: SIG-W-20260419-003
precedence: IMMEDIATE
timestamp: 2026-04-19T15:44:00Z
source: WALTER
origin: "Forwarded from VIOLET inbox signal SIG-VIO-20260415-002 (Apr 15 18:30 UTC), processed by WALTER 2026-04-19. VIOLET data: 19-year backtest (yfinance ^VIX/^VVIX/^SKEW 2007-2026), pattern-matched against current SKEW-VIX-VVIX divergence flagged in companion -001."

to: HENRY (ACTION — MARKET_VOL primary, posture-change)
info: RED, LIQUID, PROME, NEXUS
group: VOL
dispatched: 2026-04-19T15:44:00Z
dispatch_note: "POSTURE CHANGE: VIOLET 🟡 WATCH → 🟠 ELEVATED WATCH. IMMEDIATE precedence per FORMAT_SPEC posture-change rule. NEXUS added to info per convergence-engine relevance. NOT FLASH — does not meet position-specific or auto-upgrade safety-net threshold (VIX still 18, no HY OAS jump on session). VIOLET-002 was 4d-stale in WALTER inbox before processing — original posture call dated Apr 15. Cross-link: SIG-W-20260419-002 (companion VIX-family observations) + SIG-W-20260416-003 (equity internals: NDX RSI 30→70, SPX neg-breadth ATH). Updated VIOLET REGISTRY row to ORANGE."

signal_type: posture-change
confidence: 0.85
confidence_language: assessed
resources: 0
safety_net: clear

word_count: 340

# cluster backfilled 2026-06-10 from INDEX section placement (pre-v0.7 signal; cluster field added to FORMAT_SPEC 2026-05-05)
cluster: POSITIONING_VALUATION
---

## Signal

**VIOLET posture: 🟡 WATCH → 🟠 ELEVATED WATCH.** A 19-year backtest of the SKEW-VIX-VVIX divergence pattern flagged in companion SIG-W-20260419-002 materially shifted VIOLET's read on what the persistent SKEW bid implies forward.

## The data

Magnitude-matched SKEW-VIX-VVIX divergence — 20-day window, SKEW ≥+10, VIX ≤−5, VVIX ≤−15 — is a **1% base rate event**: 17 distinct episodes over 19 years.

Of 16 completed historical episodes:

- **15/16 (94%)** produced VIX rise ≥15% within 60 days
- **13/16 (81%)** produced ≥30% rise
- **9/16 (56%)** produced ≥50% rise
- **Only 1/16 was genuinely peaceful** (2018-04-30)

Current SKEW peak of **156.9** sits in the high-severity cohort (SKEW >150 peaks: 6/7 STRESS +50%).

**Recent analogs:**
- 2024-05 → Aug 2024 yen unwind
- 2024-11 → Q1 2025 vol regime (VIX 52)
- 2025-12 → our own Mar 2026 event

## VIOLET scenario probabilities — revised

| | Prior (30d window) | Revised (60d window) |
|---|---|---|
| Healthy recovery | 55% | **22%** |
| New VIX event within 60d | 30% | **66%** |
| Structural | 15% | 12% |

## Cross-link to existing BOARD signals

- **SIG-W-20260419-002 (this dispatch's companion):** observed SKEW divergence pattern that triggered the backtest.
- **SIG-W-20260416-003 (Apr 16):** NDX RSI 30→70 in 3 weeks + SPX closes record >7000 on negative breadth. Equity-internals deterioration into ATH. *Pairs cleanly with VIOLET vol-side bid for crash protection.* Two independent data layers, same regime read.
- **SIG-W-20260414-006 (Apr 14):** GS Prime — HF short cover fastest since 2020. Positioning capitulation into now-collapsed Islamabad ceasefire.
- **SIG-W-20260414-008 (Apr 14):** DB — financials positioning at multi-year lows vs consensus +20-40% EPS growth.

**Convergence shape:** four independent positioning/vol/internals data points (HF positioning + DB financials gap + equity internals + VIOLET SKEW divergence) all pointing to "wrong-footed into catalyst week." Catalysts: WAL/ZION Apr 21, Iran ceasefire expiry Apr 21, BOJ Apr 28.

## Network implications

- **HENRY (ACTION):** Elevated vol risk through Jun 15 (full 60d window). Review equity hedge exposure. The Apr 21 / Apr 28 catalyst stack now has a vol-side prior attached.
- **RED:** HY OAS falsification day-count proceeds, but the vol side disagrees with credit's "all clear." Credit-vol divergence itself warrants re-weighting your falsification threshold.
- **LIQUID:** Watch for HY OAS widening as confirmation of the 66% scenario.
- **PROME:** Network posture input — VIOLET is the second agent (after RED) to formalize an adversarial-style probability framework. Worth knowing for coordination.
- **NEXUS:** Convergence-engine input. Four-point cluster outlined above is candidate for a new convergence row.

## Checkpoints

- **2026-04-29:** early read (14d after Apr 15 trigger)
- **2026-06-15:** full 60-day window close

## Source

- VIOLET inbox file: `AGENTS/WALTER/inbox/SIG-VIOLET-WALTER-20260415-002-skew-divergence-escalation.md`
- VIOLET research file: `AGENTS/VIOLET/research/2026-04-15_skew_divergence_episodes.md`
- Underlying: yfinance ^VIX / ^VVIX / ^SKEW 2007-2026, 17 historical episodes
