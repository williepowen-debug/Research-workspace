---
signal_id: SIG-W-20260522-002
precedence: PRIORITY
timestamp: 2026-05-22T14:19:16Z
source: WALTER
origin: "DOL ETA weekly Unemployment Insurance Claims release Thu 2026-05-21 8:30 AM ET (week-ending 2026-05-16; DOL primary PDF 403-blocked); aggregator triangulation via TradingEconomics + FXStreet calendar + Seoul Economic Daily wire + AdvisorPerspectives dshort; sub-agent verify 2026-05-22 14:11-14:14 UTC ~$0.05 agent_id ab1620e68df101872; calendar-anchor correction (release was Thu 5/21, not 5/22 — fix in own STATUS docs flagged at closeout)"

to: CARL (ACTION)
info: LABOR, REGINALD, HENRY, RED, NEXUS, PROME

signal_type: data-release
confidence: 0.75
confidence_language: confirmed_aggregator
resources: 0.05
safety_net: clear

word_count: ~260

cluster: CONSUMER_STAGFLATION
cluster_secondary: BANK_COLLATERAL
signal_role: counter_evidence
consumer_transmission: discretionary_demand
consumer_lens: aggregate
event_window: closed

verify_research_verdict: CONFIRMED-AGGREGATOR (DOL primary PDF 403-blocked; three independent aggregators consistent on headline / 4-wk MA / continuing / prior revision; depth gap = state-level table not retrieved)
mark_context: Release was Thursday 5/21, not 5/22 — my STATUS docs had this calendar-anchored wrong. Dispatching one calendar day after release. Pairs as counter_evidence to SIG-W-20260514-001 (which framed labor-transmission as re-arming on 5/14's 211K +6K hot print).
---

# Initial Claims Week-Ending 5/16: 209K Cool Miss vs 210K Cons + Prior 211K Revised Up to 212K + 4-Wk MA 202.5K ↓ -1.5K — 5/14 LABOR Direction-Flip REVERSED, NOT Extended (Counter-Evidence Dispatch to SIG-W-20260514-001)

**Print (DOL ETA Thu 2026-05-21 8:30 AM ET, week-ending 2026-05-16):**

- **Initial claims: 209,000 actual** vs 210,000 consensus = **-1K cool miss**
- **Prior week (5/9) revised UP from 211K → 212K** (+1K hawkish revision)
- Net week-over-week: -3K from revised prior (212K → 209K)
- **4-week moving average: 202,500** — **down 1,500** vs prior week's revised average. Direction: ↓ (cooling)
- **Continuing claims: 1,782K** (week-ending 5/9) — beat 1,790K consensus by 8K; +6K vs prior. Still benign.
- Unadjusted total -5,826 w/w; -15K vs comparable 2025 week (200,637 → 185,625)

## Substance read (counter_evidence to 5/14)

- **5/14 SIG-W-20260514-001 framing REVERSED.** The 211K print +6K hot vs cons / +12K WoW direction-flip framed labor-transmission as "re-arming"; this 5/21 print does the opposite — back below 210K, no follow-through.
- **4-wk MA cooling -1,500** is the higher-signal datapoint. The April 1969-low (189K) → 5/14 break-higher arc has not extended; one-week return-toward-baseline.
- Threshold scan: 41K away from RED-FT-05 (>250K sustain=1) = -16.4% — outside 5% near-miss band. 91K away from REG-T-05 (>300K sustain=1) = -30.3% — far outside band. **Neither fires; neither qualifies for near-trigger watch.**
- **Magnitude is small** — sub-agent recommended SKIP on novelty alone. Dispatch hook is the **directional-reversal-vs-5/14** thread + bull-counter weighting calibration loading (PROME 5/21 ask thread).

## Cluster placement + counter_evidence rationale

- Primary cluster CONSUMER_STAGFLATION (same as 5/14 SIG-W-20260514-001); cluster_secondary BANK_COLLATERAL (labor → C&I / consumer credit transmission unchanged direction).
- **signal_role: counter_evidence** because this print neutralizes the 5/14 direction-flip — labor-transmission re-arming thesis fails to extend at first follow-on data point. Loads cluster_mediating / counter-evidence calibration thread.
- **Bull-counter density extension:** BOARD-side counter_evidence density now 5/66 (~7%) post-PM #2 backfill; this dispatch makes it 6/66 (~9%). PROME 5/21 calibration ask now has structural bull-counter feed.
- **Caveat:** state-level table not retrieved (DOL PDF blocked 403); FL/CA/MI/TX/DOGE-state breakdown unverified — possible state-level surprise hidden in aggregate-cool number.

## Routing rationale

- **CARL ACTION:** primary consumer-thread + labor-transmission analyst. CARL Path C v2.5 active; 53/70 K-shape integration ongoing.
- **LABOR INFO:** primary domain (LABOR is OC-side, STALE 18d per REGISTRY — backup-promotion to CARL acting via routing).
- **HENRY INFO:** equities + vol regime (labor-cooling is bull-tape supportive; R11 vol-spike pathway needs labor-acceleration data, this print withdraws it).
- **REGINALD INFO:** bank-side credit transmission channel.
- **RED INFO:** auto-cc per ROUTING_TABLE v0.7 — counter_evidence signal_role triggers cc-RED rule.
- **NEXUS / PROME standard.**

## Falsification scan (at-dispatch)

- Same live-tape pass as SIG-W-20260522-001 (concurrent dispatch). Live 10:18 AM ET: WAL $78.07 -0.59% / KRE $69.17 -0.07% / HYG $79.89 -0.02% / SPY $745.62 +0.39% (fresh-ATH territory).
- **No new threshold fires.** REG-T-05 / RED-FT-05 (claims thresholds) cool print = no fire; near-miss band not breached.
- WAL REG-T-02 sustain-state intact since 5/21 reclaim ($78.07 holds above $78 by 7 cents — near-trigger watch persists).

## Anticipated downstream consumption

- CARL: Path C v2.5 K-shape integration — labor not yet accelerating per WALTER signal stream.
- RED: bull-counter weighting calibration cycle 1 input (running 5/20-27 window).
- LABOR (if revived): direction-flip-reversed datapoint for the LABOR thesis state machine.
