# EVENT_WINDOW_STATE — Current declared state

**Current state:** `CLOSED`
**Last transition:** —
**Last transition by:** —
**Verification gate status:** Phase 2 watch active — **1 of 3 Path B triggers fired (Trigger #3, 2026-05-15)**; needs ≥2/3 Path B OR Path A 4/4 for OPEN declaration per JOINT_PROPOSAL §2d
**Expected close trigger:** n/a (no OPEN window declared)

---

*BURST_WINDOW state machine per JOINT_PROPOSAL_2026-05-05_walter_carl_brent §2d (3-way cosigned BRENT+CARL+WALTER 2026-05-05/06; Will sign-off 2026-05-08). This file is the canonical current state — read at WALTER boot (spawn-protocol step 7b) and BRENT boot (BRENT CLAUDE.md spawn-protocol delta, BRENT self-task next session). When state = OPEN, all Phase-2-cluster signals dispatch FLASH; cross-cluster signals stay normal precedence.*

---

## State machine

```
States:
  CLOSED (default)         — normal dispatch cadence; FLASH per-signal as usual; this file shows CLOSED
  OPEN (declared)          — all Phase-2-cluster signals dispatch FLASH; threaded Telegram master-message;
                             daily 00:00 UTC roll-up by WALTER; close-of-window summary at transition
  PENDING_VERIFICATION     — declared OPEN but verification gate has not yet fired (≤48h)

Transitions:
  CLOSED → OPEN              ← BRENT declares on Path A 4/4 met OR Path B EIA triggers fire
                              (BRENT-led declaration; alternatively WALTER declares if BRENT stale
                              + first-mover Phase-2-announcement detected)
  OPEN → CLOSED              ← either side declares close after ≥48h stable post-event
                              (default: WALTER-led; either side may fire earlier on disambiguation)
  OPEN → CLOSED (early)      ← LESSONS #18 disambiguation — verification gate fails 48h post-declare;
                              window signals tagged "false-positive window-context"

Verification gates (BRENT canonical):
  (a) Platts Dated Brent convergence to baseline
  (b) Lloyd's transit returns to 60-135/day baseline
  (c) P&I insurer resumption notice
  (d) Sovereign action on blockade (Iran formal climbdown, US Project Freedom stand-down)
```

## During OPEN window — operational rules

- All Phase-2-cluster signals dispatch FLASH (overrides per-signal precedence)
- Telegram pings get threaded under a single rolling **"BURST WINDOW OPEN — Phase 2 trigger"** master message; one new message per dispatched signal under that thread
- Daily 00:00 UTC roll-up posted by WALTER (signal count, key dispatches, verification-gate progress)
- Close-of-window summary at transition to CLOSED (window duration, dispatches fired, gate-confirmation status, retroactive false-positive-tagging if early-close)
- Other-cluster signals stay normal precedence (don't bleed Phase-2 burst into unrelated domains)
- All dispatched signals carry `event_window: open` per FORMAT_SPEC v0.8

## Update protocol (state transition)

WALTER and BRENT both have write access to this file. To declare a state change:

1. **Replace the lead block** (Current state / Last transition / Last transition by / Verification gate status / Expected close trigger lines)
2. **Append a new entry** to the State Transition Log section below — one row per transition, immutable history
3. **Commit immediately** — state is operational, can't sit unstaged. WALTER stages this file alongside other WALTER scope per CLAUDE.md spawn-protocol step 16b (file lives under AGENTS/WALTER/, no exception needed)
4. **Telegram-ping Will** on every transition — one line, format: `BURST_WINDOW: <prior> → <new>; declared by <agent>; trigger <reason>; expected close <trigger>`

Either agent may declare CLOSED → OPEN; default declaration is BRENT (domain primary). Either agent may declare OPEN → CLOSED; default is WALTER (post-48h-stable check). LESSONS #18 disambiguation early-close can fire from either side.

## State Transition Log (append-only)

*Records actual state transitions only (CLOSED ↔ OPEN ↔ PENDING_VERIFICATION). Trigger fires that do not cross the OPEN threshold are recorded in the "Pre-OPEN trigger fire log" section below.*

| Date | From | To | Declared by | Trigger | Expected close | Outcome |
|------|------|-----|-------------|---------|----------------|---------|
| 2026-05-08 | — | CLOSED (initial) | WALTER | Scaffold create per JOINT_PROPOSAL §2d Will sign-off | n/a | n/a — initial state |

## Pre-OPEN trigger fire log (Path B / Path A observability)

*Records individual Path B (3-trigger) or Path A (4-criteria) fires that have not yet crossed the OPEN-declaration threshold (≥2/3 Path B OR 4/4 Path A). Recorded for observability + cumulative count tracking; do NOT cause state transitions on their own.*

| Date | Trigger | Detail | Path B count after | Recorded by |
|------|---------|--------|--------------------|-------------|
| 2026-05-15 | Path B Trigger #3 (CFTC MM positioning) | Brent CFTC Managed Money net longs 70,791 (week of May 5) — down 29K from 99,887 peak over 2 weeks at Brent $106-111 distribution; large-spec distribution underway per BRENT thesis v2.0 + commits `ad9d29fb` (Friday data refresh) + `3ef8d916` (SIGNALS.md cross-agent alert) | 1/3 | BRENT (entered into log by WALTER 5/21 closeout) |

---

## Cross-references

- Spec source: `JOINT_PROPOSAL_2026-05-05_walter_carl_brent.md` §2d (full text, state machine + cost-asymmetry justification + verification gates)
- WALTER spawn-protocol read: step 7b (after BOARD INDEX scan, before registry refresh)
- BRENT spawn-protocol delta: BRENT CLAUDE.md (BRENT self-task) — when state = OPEN, expect FLASH burst, boot fast / integrate fast / re-position fast
- Header field: `event_window: open|closed` per FORMAT_SPEC v0.8 (default closed)
- CHECKLIST tagging: Phase 2.5 event-window state check (per CHECKLIST v0.11+)
- FILTER_SPEC: OPEN-window dispatch posture sub-section under Tuning Rules

---

*Owned: WALTER (write access); BRENT (write access for declarations). Read: all agents at boot. Source-of-truth for current state — when in doubt, read this file before believing memory.*
