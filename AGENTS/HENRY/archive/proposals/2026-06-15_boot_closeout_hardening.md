# PROPOSAL — HENRY Boot + Closeout Hardening

**Status:** DRAFT — NOT APPLIED. Designed 2026-06-15 (Will chose "draft-only"). Application is **eval-gated**: every change below edits HENRY's CLAUDE.md SPAWN PROTOCOL, which is an eval re-baseline trigger. Do NOT apply until the `evals/` baseline has been run against current HENRY. PROME owns fleet-wide protocol; HENRY owns its own CLAUDE.md but flags boot/closeout step changes to Will/PROME.

**Why:** the 6/15 boot-audit + closeout-audit found HENRY's boot/closeout is the leanest in the macro cluster — missing the symmetric read↔write framing, predictions-resolution, promotion-removal, NEXUS_BRIEF/MAINTENANCE maintenance steps, and the discipline overlay that VIOLET/SAM/BRENT carry. Both this session's failures (5-session staleness; VIOLET "stale 6/1" carry-forward) trace to these gaps. The artifacts (boot.py, NEXUS_BRIEF, MAINTENANCE, evals) are now built; this proposal WIRES them into the protocol.

**Design principle (from BRENT):** boot and closeout are ONE symmetric sequence — what you READ at boot you WRITE BACK at closeout. Each new step is paired.

---

## APPLICATION SEQUENCE (the gate)

- **Phase 1 — BASELINE (Will, ~20–40 min):** run `evals/` vs current HENRY → reference. *(Prerequisite for everything below.)*
- **Phase 2 — APPLY TIER-1 (additive):** the steps that add hygiene actions without changing how HENRY *reasons*. Apply → re-run evals → confirm guardrails hold → promote.
- **Phase 3 — APPLY TIER-2 (behavior-changing):** the steps that change boot/closeout behavior. Apply → re-run evals + **boot smoke-test** → promote.
- Re-baseline trigger fires on each phase; never silent-ship.

---

## PROPOSED SPAWN PROTOCOL (full replacement for CLAUDE.md §SPAWN PROTOCOL)

*Annotated with [T1]/[T2] tier + [NEW]/[KEEP]. Read-step N pairs with write-step N′.*

### BOOT (read phase — order matters)
1. [KEEP] Read `STATUS.md`
2. [KEEP] Read `LESSONS.md`
3. [KEEP] Read `MEMORY.md` (ends on handoff: CHANGES SINCE / NEXT SESSION)
4. [T1][NEW] **Run `scripts/boot.py`** — live tape + FRED credit + predictions-due scan (~15s, display-only; does NOT write STATUS). *(pairs → write 8, 7)*
5. [T2][NEW] **Read peer `NEXUS_BRIEF.md`** for HENRY's edges (BRENT energy→CPI, VIOLET vol, SAM carry, LABOR employment, LIQUID/REGINALD/BROCK credit) — or NEXUS synthesis. **This is the VIOLET-stale fix:** peer state in front of you at boot, not carried-forward from your own file. *(pairs → write 11)*

### EXECUTE
6. [KEEP] Execute the task.
   - [T2][NEW] **Live-event override:** if boot reveals a live regime-moving print or active catalyst window (CPI/FOMC day, VIX +30% intraday, credit gap), EXECUTE stays open — snapshot STATUS as a working dashboard, stay engaged; do NOT trigger full write-back until the event stabilizes / task completes / Will signals stop. The session is not over because boot is over.

### WRITE-BACK (closeout — run at EVERY session end, not just end-of-day)
7. [KEEP] Write results back to `STATUS.md` (mirror of read 1). Maintain the state-claim convention (`[src M/D]`, `STATE [as-of @ level]`).
8. [T1][NEW] **Resolve DUE predictions** flagged by boot.py (step 4): resolve / re-arm-with-reason / push-date-with-reason — never leave OPEN-but-stale in `workbook/PREDICTIONS.tsv`. Separate "mechanism intact" from "threshold stuck/breached" (`[[finding_threshold_vs_mechanism]]`). (mirror of read 4)
9. [T1][NEW] **Workbook write-back** — new facts → `workbook/KB.tsv`; changed vectors → `workbook/VX.tsv`; cascade/transmission → `workbook/FLOW.tsv`. Mark superseded rows `[STALE]` with disposition, don't delete.
10. [KEEP] Research detail → `research/` (deep dives, prompts, outputs).
11. [T1][NEW] **`NEXUS_BRIEF.md` write-back** — mandatory every session, even no-change (refresh `As of` + `STATUS commit` hash so staleness self-corrects; material STATUS change → content updates). Steady-state cross-agent surface; reference canonical sources, don't restate. (mirror of read 5)
12. [KEEP] Cross-agent signals → `outbox/` — **🔴 acute / time-sensitive only**; steady-state flows through NEXUS_BRIEF (per outbox-restraint).
13. [KEEP] Update `MEMORY.md` Session Notes (CHANGES SINCE / NEXT SESSION); add Feedback/Findings; prune stale; cap 100 lines.
14. [T1][NEW] **Promotion scan** — thesis-level → STATUS/thesis; **transferable cross-agent lesson → auto-memory** (`~/.claude/projects/.../memory/` + one-line index); HENRY-specific durable → local MEMORY. **Remove from local MEMORY after promoting to auto-memory** (it auto-loads at boot; duplication bloats + drifts).
15. [T1][NEW] **Structural-change log** — if this session changed HENRY's *structure* (doc created/retired/moved, script built/behavior-changed, protocol/CLAUDE.md edit, schema change), add a `MAINTENANCE.md` entry (Trigger / What changed / Files / Boot-impact / Lessons).
16. [KEEP] Overwrite `LAST_COMPLETION.md` (Will-facing closeout).

### DISCIPLINE OVERLAY [T1][NEW] — applies throughout write-back
- **One source of truth per metric** — don't write the same value in two docs; own it in the owner doc, reference elsewhere with `[CONF <agent> M/D]`.
- **Stale-marked > carried-forward-as-current** — if you can't refresh a value, mark it `[STALE]` with the date; never present it as live.
- **Re-verify any "[agent] is stale" claim against that agent's actual file header** before repeating it (the VIOLET 6/12 lesson; `[[feedback_verify_counts_before_propagating]]` consumer-vantage umbrella).
- **Don't let prior-session narrative substitute for fresh measurement** — recompute load-bearing values from the source, don't inherit the surface text.

---

## TIER-2 STANDALONE DECISION — handoff convention

VIOLET/BRENT retired `LAST_COMPLETION.md` → `SCRATCH.md` (canonical handoff) + NEXUS_BRIEF + MEMORY. HENRY uses LAST_COMPLETION + MEMORY-Session-Notes.

**Recommendation: KEEP LAST_COMPLETION, do NOT adopt SCRATCH.** It's a HENRY strength — a more explicit Will-facing template than a raw SCRATCH. Instead, **document the divergence inline** in CLAUDE.md (precedent + reason + path-to-alignment, per `[[finding_documented_divergence_as_discipline]]`): "HENRY's canonical handoff = MEMORY Session Notes (next-instance) + LAST_COMPLETION (Will-facing); SCRATCH intentionally not adopted." Flag to PROME for fleet-consistency awareness. *(Net: a no-op on files, a one-line documented divergence — lowest-risk resolution.)*

---

## ACCEPTANCE / VERIFICATION (after applying)

- **Tier-1, re-run evals:** all 3 cases — guardrails (02, 03) must stay PASS; target (01) should hold/improve. A guardrail regression = the additive step degraded reasoning (unlikely for pure hygiene, but that's why we re-run).
- **Tier-2, boot smoke-test (separate from evals):** boot HENRY for real (not skip-boot) and confirm step 5 delivers a fresh peer fact unprompted — e.g. surfaces "VIOLET current to [date]" from her NEXUS_BRIEF without being told. This validates the boot-read *delivers data*; the eval only guards the *judgment*. (Per evals/README §"READ FIRST".)
- **Live-event override:** verify the EXECUTE language doesn't pull a closeout mid-CPI/FOMC (the bug `[[finding_boot_protocol_live_event_override]]` describes).

## MAPPING — gaps → steps (closeout-audit traceability)

| Closeout-audit gap | Proposed step | Tier |
|---|---|---|
| Resolve-DUE-predictions | 8 | T1 |
| Promotion-scan + remove-from-local | 14 | T1 |
| NEXUS_BRIEF refresh (mandatory) | 11 | T1 |
| MAINTENANCE.md step | 15 | T1 |
| Discipline overlay | overlay block | T1 |
| Workbook write-back codified | 9 | T1 |
| Symmetric read↔write framing | whole structure (paired) | T2 |
| Read peer briefs at boot (VIOLET-stale fix) | 5 | T2 |
| Live-event EXECUTE-override | 6 | T2 |
| Handoff reconcile | standalone decision | T2 |

*All boot.py / NEXUS_BRIEF / MAINTENANCE / evals artifacts referenced above already exist (built 6/15). This proposal only wires them into the protocol.*
