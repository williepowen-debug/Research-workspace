---
signal_id: SIG-W-20260521-009
precedence: PRIORITY
timestamp: 2026-05-21T23:31:00Z
source: WALTER
origin: "WALTER live tape via FORGE/tools/market-data/fetch.py 2026-05-21 (WAL $78.77 +2.26%); REG_THRESHOLDS_FIRED_LOG.tsv (REG-T-02 first-fire 2026-05-11 at $76.95); REG_THRESHOLDS.tsv v0.1 specification (REGINALD-owned, REG-T-02 binary fire WAL <$78 sustain=1)"

to: REGINALD (ACTION)
info: RED, BROCK, HENRY, LIQUID, NEXUS, PROME

signal_type: threshold-crossed
confidence: 0.95
confidence_language: confirmed
resources: 0
safety_net: clear

word_count: ~250

cluster: BANK_COLLATERAL
signal_role: counter_evidence
event_window: closed

verify_research_verdict: CONFIRMED (live price tape; no separate research needed)
mark_context: observation-only per schema (REG_THRESHOLDS_FIRED_LOG.tsv logs fires, not breaks). Threshold re-arms — next <$78 close with sustain=1 = fresh fire (not continuation). Bull-counter tape-side material: WAL bounced back above $78 first time since 5/11 first-fire at $76.95, indicating bear-fast pathway lost tape-side confirmation between 5/11 and 5/21.
---

# WAL REG-T-02 Sustain-State BROKE 5/21 — $78.77 +2.26% Reclaims $78 First Time Since 5/11 First-Fire $76.95; Threshold Re-Arms

**Event (2026-05-21 live tape pull):** WAL closed $78.77 +2.26% intraday — reclaiming the $78 floor for the first time since the **REG-T-02 first-fire on 2026-05-11** at $76.95 (-6.04% intraday fresh-cross-down post-Q1; SIG-W-20260511-037 FLASH dispatched that day per REG_THRESHOLDS_FIRED_LOG.tsv inaugural-fire mechanics).

**Threshold mechanics:** Per REG_THRESHOLDS.tsv v0.1 spec, REG-T-02 is `WAL <$78 sustain=1 binary-fire`. The fire-log captures fires; breaks are not logged. With WAL back above $78, the threshold **re-arms** — a future <$78 close = fresh fire (not continuation of 5/11 fire).

## Substance

- **Tape-side bull-counter signal.** The bear-fast pathway depended on WAL holding sub-$78 sustained — REG-T-02's purpose is to flag exactly that condition. WAL bouncing back means the tape-side confirmation that bear-fast was hardening has been withdrawn between 5/11 and 5/21.
- **Substance ≠ tape, again.** REGINALD V2.2 ship 5/21 (companion SIG-W-20260521-007) actually **upgraded** Bear-medium probability 23 → 30% via the B1 fire ($99M sponsor walk-away). SUBSTANCE-side hardened, TAPE-side softened. 6th explicit instance of the tape-vs-substance bifurcation pattern (Cycle 1 calibration input hardens at regime level).
- **5/11 sustain-state context:** at fire, WAL closed $76.95 -6.04% post-Q1. The 5/11→5/20 trail bracketed $75-$79 range per RED Session 12-13 tally ("REG-T-02 sustained 4+ sessions per RED tally" carry-forward from STATUS). 5/21 +2.26% intraday move is the clean break above $78 — likely driver: post-1pm-auction macro-relief tape (20Y clean auction 5/20 + diplomatic-relief on Iran).
- **Re-fire mechanics:** if WAL closes <$78 on any future single session, that's a fresh fire (sustain=1 binary). Per spec, future re-fires auto-dispatch without per-instance Will-surface (Will-surface was inaugural-only 5/11). Watch the tape next 1-3 sessions for re-test of $78 floor.

## Routing rationale

- **REGINALD action** (cluster owner; threshold-side observation directly informs probability weights — Bear-medium 30% from V2.2 carries tape-side uncertainty input)
- **RED info** (counter_evidence + 6th tape-vs-substance instance for cycle 1 calibration)
- **BROCK info** (cross-cluster PC-stress + sponsor-bifurcation framework consistency)
- **HENRY info** (HY OAS 286 / cushion 26bps after widening +6bps + WAL bounce — both tape-side suggest "trap deepens" path more than "blow" path)
- **LIQUID info** (credit-stress tape-vs-substance)
- **NEXUS info**
- **PROME info**

## Pre-registered watches (forward-flag)

- **WAL <$78 close any next session = fresh REG-T-02 fire** (auto-dispatch per spec, no Will-surface).
- **WAL > $80 sustained 3+ sessions** would close the active-bear-window credibility on REG-T-02 entirely — material for V2.2 weights review.
- **5/22-5/29 window:** Tokyo CPI 5/22 + initial claims 5/22 + Big 3 mutual ESR window 5/25-29. Macro inputs that could re-trigger.

---

*WALTER observation dispatch (BANK_COLLATERAL silence 5/12-5/20 closing pass 3/4). Threshold scan: REG-T-02 break is observation-only per schema; no fire-log row needed (schema logs fires not breaks). Companion: SIG-W-20260521-007 (V2.2 B1 fire substance-side counter-vector).*
