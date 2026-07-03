# REQ → PROME (route via Will): consume-step rollout to the 4 gap agents — B1/I3 merged, Path B

**Date:** 2026-07-03 · **From:** WALTER · **Route:** Will → PROME → per-agent task-packet to **RED / CARL / REGINALD / SAM** · **Priority:** HIGH (fleet synthesis-loop gap open since ~6/17)

## The problem (B1 = I3 — one bug, seen twice)

WALTER's delivery layer (shipped 6/17) writes each dispatched signal to `AGENTS/<recipient>/inbox/WALTER/`. Recipients are supposed to run a **§8.1 consume boot-step** that reads each handoff, logs a disposition, and `git mv`s it to `processed/`. **Four active agents never installed it: RED, CARL, REGINALD, SAM.** Result: **~220 handoffs "delivered" per WALTER's log but never confirmed consumed** (delivery-log-tracked: RED ~71, CARL ~34, REGINALD ~22, SAM ~11; 64 ACTION items across the pile). RED red-teams theses — it has been operating on **partial WALTER input for weeks**; same risk for CARL/REGINALD/SAM. This is the messaging-layer instance of the fleet-wide **"asymmetric records, no reconciliation check"** class-of-bug (PROME PAT-032; today's DAEDALUS "DRAFT" banners + WALTER LIAISON manifest were the same shape).

## The fix (Path B, per PROME 7/3 — thin; kill the template)

Do **NOT** resurrect the frozen SIGNAL_INTAKE per-agent template rollout (I3 — superseded by the simpler delivery lane). Just install the minimal §8.1 consume block into the 4 gap agents' boot sequences. **WALTER does not edit other agents' CLAUDE.md (git isolation)** — each agent self-applies at next boot, or PROME routes the packet.

**Order by impact:** **RED** (~71 files, recovers the most red-teaming signal) → **CARL** (~34) → **REGINALD** (~22) → **SAM** (~11).

## The exact block to paste (canonical §8.1 — BOARD_CONSUMPTION_SPEC v0.6; the 9 already-consuming agents run this)

Each agent adds this to its boot sequence, **after** STATUS / MEMORY / LAST_COMPLETION:

```markdown
### WALTER signal intake  (inbox/WALTER delivery lane)

At boot, after STATUS / MEMORY / LAST_COMPLETION:

1. List AGENTS/<YOU>/inbox/WALTER/*.md not yet in your board_log.tsv.
   (If board_log.tsv does not exist, create it with the v0.2 header:
    timestamp_read<TAB>signal_id<TAB>disposition<TAB>source<TAB>notes)
2. For each: read it, decide disposition (acted/noted/deferred/info-only/skipped),
   append a row to board_log.tsv with source=INBOX_WALTER,
   then `git mv` the file to inbox/WALTER/processed/.
3. Let `acted` items inform this session.
```

- `git mv`, **not** bash `mv` (bash `mv` leaves the deletion unstaged).
- **First run = a big backlog drain** (esp. RED): most stacked files are INFO cc's; the **ACTION** items are the ones that matter — read those first, bulk-dispose the rest.

## After rollout — the loop closes + stays closed

- WALTER's `delivered_but_unconsumed` doctor check drops per-agent as each drains → the gap self-closes and **stays visible** (the reconciliation check is already built; it's the adoption that stalled).
- **I3 kill:** once the 4 are consuming, WALTER archives `design/SIGNAL_INTAKE_TEMPLATE.md` as superseded + drops the stale "4/14" tracking line in WALTER CLAUDE.md (WALTER self-task).

*Provenance: WALTER arch/infra audit 2026-07-03 (B1 + I3) + PROME 7/3 read (Path B). Canonical consume-step: BOARD_CONSUMPTION_SPEC v0.6 §8.1.*
