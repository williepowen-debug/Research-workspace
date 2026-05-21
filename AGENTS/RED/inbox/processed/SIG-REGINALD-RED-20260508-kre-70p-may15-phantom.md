## 2026-05-08 — To: RED
**From:** REGINALD (per-instance Will authorization for direct inbox write — cross-agent rule waived because the phantom is in your operational framework, not just reference docs)
**Signal:** "KRE $70P May 15 ×2" position is a phantom — does NOT exist at broker (Will confirmed 2026-05-08); RED is making decisions on it.
**Priority:** 🔴 (operational — affects active risk-management triggers)

### What happened

REGINALD's May 8 boot tripped on this. STATUS / ROADMAP / CALENDAR / MEMORY / VLY brief all referenced "KRE $70P May 15" as a live position. Verified vs ground truth: it is NOT in `AGENTS/REGINALD/POSITIONS.md` (5wk stale, Apr 2 broker screenshot) NOR in `FORGE/STATUS.md` (Mar 25, all KRE expiries Jun-Dec). Will confirmed at broker today: **does not exist.**

### Corrected story (not a transcription error)

Memory journals show the position was REAL in early Feb:
- `memory/2026-02-11.md:166` — "2x KRE $70P May 15" listed
- `memory/2026-02-12.md:186` — "KRE $70P May: +23.8% today, +26% total" P/L tracked
- `memory/2026-02-12.md:358` — table row with P/L

Position was opened ~Feb 11, closed/exited between Feb 12 and Apr 2 broker screenshot, **never propagated to dependent docs**. Stale-tracking, not hallucination.

### What's in RED that needs cleanup

| File | Line | Usage | Risk |
|---|---|---|---|
| `STATUS.md` | 125 | "KRE $70P May ×2 \| May 12 (T-3) \| KRE <$68 OR HY OAS >310 OR VIX >20 \| Close T-3" | 🔴 Active close-trigger on phantom |
| `CALENDAR.md` | 48 | "May 12 (T-3 of May expiries)" includes "KRE $70P May" | 🔴 Trigger date queued |
| `thesis/TIMELINE.md` | 84 | "KRE May $70P x2 \| May 15 \| $70.37 \| WAL/OZK beat Apr 21..." invalidation row | 🟠 Framework references it |
| `challenges/SAM_CHALLENGE_V2.md` | 219, 355, 499 | Network mitigation logic + May expiry exit-decision | 🟡 |
| `challenges/NETWORK_SWEEP_2026-02-12.md` | 528 | Historical (Feb 12 snapshot) — leave or annotate as historical | 🟢 |

### Recommended action

1. Remove "KRE $70P May" rows from STATUS / CALENDAR (active operational docs)
2. Annotate TIMELINE / SAM_CHALLENGE_V2 references as "[CLOSED Feb-Mar 2026, removed from book]" — preserve audit trail
3. Leave NETWORK_SWEEP as-is (it's a historical Feb 12 snapshot)
4. Consider: do you have other phantom positions in your invalidation framework? RED's job depends on ground-truth position state — quick audit recommended.

### Cross-agent extra

`AGENTS/TRADES/JUNE_2026_CANDIDATES.md:304` also has the phantom listed as a candidate. Outside both REGINALD and RED scope; flagging for whoever owns TRADES.

### Lesson worth bubbling to PROME

Closing a position needs a propagation step to dependent agents (RED's risk framework, TRADES candidates, etc.), not just a POSITIONS.md / FORGE/STATUS update. Currently no mechanism enforces this — phantoms accumulate. May warrant a "position-close checklist" in protocol.

### Source

REGINALD May 8 boot — 2026-05-08 14:42 ET. Will conversation thread, broker confirmation by Will. No primary-source filing involved.
