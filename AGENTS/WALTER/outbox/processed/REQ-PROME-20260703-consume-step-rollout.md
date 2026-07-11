# ✅ CLOSED 2026-07-04 — REQ → PROME: consume-step rollout (B1) DONE both sides; I3-kill RETRACTED

> **✅ CLOSED 2026-07-04.** Consume-step rollout (**B1**) COMPLETE: **RED** installed (DAEDALUS 7/3) · **SAM** canonical-install packet routed (PROME) · **REGINALD** keep-lane drain-step packet routed (PROME; SIG-704-004 OZK flagged read-first) · **CARL** dropped (WALTER §3.5 pull-complete exemption shipped, BOARD_CONSUMPTION_SPEC v0.7 + CHECKLIST v0.24 + doctor `PULL_COMPLETE`; PROME archived its 40 handoffs to `processed/`). PROME synced 0/0 off 4 pushed commits.
>
> **I3 template-kill RETRACTED.** The external-consumer check (run *before* archiving, per `[[finding_external_consumer_check_before_restructure]]`) found `design/SIGNAL_INTAKE_TEMPLATE.md` is **ACTIVE** with **5 live consumers** (SAM/BRENT/VIOLET/CARL/ORACLE each have a `SIGNAL_INTAKE.md`; VIOLET CLAUDE.md + ORACLE SIGNAL_INTAKE.md cite the template PATH; VIOLET rebuilt 6/10, ORACLE 6/18 — both *after* the delivery lane shipped) — **NOT superseded** (the SIGNAL_INTAKE.md spec = *what* WALTER routes; the delivery lane = *how* it's pushed; complementary). Archiving would have broken 5 external path-refs + orphaned 5 live specs. Fixed the stale "4/14 stalled" framing in CLAUDE.md + STATE §1/§8 instead; template STAYS. Same verify-before-propagate / asymmetric-records class the whole packet was an instance of.

---

# REQ → PROME (route via Will): consume-step rollout to the 4 gap agents — B1/I3 merged, Path B [original below, superseded]

**Date:** 2026-07-03 · **From:** WALTER · **Route:** Will → PROME → per-agent task-packet · **Priority:** HIGH (fleet synthesis-loop gap open since ~6/17)

---

## ✅ RECONCILED + REVISED ROUTE — 2026-07-04 (WALTER + PROME, Will-relayed)

**The "4 gap agents / route to 4" framing below is SUPERSEDED.** Live-state reconciliation (WALTER 7/4) corrected it — the packet's counts predated their own resolution (the fleet **asymmetric-records** class again):

- **RED — DONE, no route.** DAEDALUS installed the §8.1 step 7/3 (RED CLAUDE.md step 5.5; write-back `AGENTS/WALTER/inbox/2026-07-03_from-DAEDALUS_RED-consume-step-installed.md`). 98 staged / 0 processed = installed, drains on RED's next boot. Verified.
- **The three remaining are NOT symmetric** — decision keys off whether each has a *complete* `/BOARD/` pull that already catches its ACTION items:
  - **SAM → INSTALL the clean canonical §8.1 block** (no `/BOARD/` scan AND no lane = no structured intake at all; the lane is essential; no existing ledger to conflict). 18 handoffs.
  - **REGINALD → KEEP the lane + INSTALL a drain-step** (adapted for its existing 11-col `board/BOARD_LOG.tsv`). Its `/BOARD/` scan is **tiered/selective (≠ complete)**; reconciliation found **1 un-dispositioned ACTION (SIG-W-20260704-004, the OZK deed-in-lieu)** → per the gate, do NOT silent-archive; the lane's not-missed guarantee has value (and is how OZK reaches it). 26 handoffs — do NOT bulk-archive.
  - **CARL → DROP the lane** (bulk-archive its 40 + WALTER stops delivering). Runs a **complete whole-INDEX BOARD-diff** (dispositions every unrecorded SIG-W); reconciliation confirmed **all 22 ACTION handoffs already dispositioned in its `BOARD_LOG`** (0 misses) → the lane is redundant for CARL. Drop-safe.
- **Mechanics correction:** the doctor's `delivered_but_unconsumed` keys off the **`git mv` to `processed/`**, NOT `board_log.tsv` (WALTER-verified: it globs `inbox/WALTER/*.md` excluding `processed/`). So the git-mv is load-bearing; the log is optional audit → the parallel-log worry is moot.

**Division of labor (git-isolation-clean):**
- **WALTER:** (a) reconciliation-confirm ✅ DONE (CARL clean / REGINALD 1-ACTION-flag) · (b) delivery-side pull-complete skip rule + doctor exemption for **CARL only** (BOARD_CONSUMPTION_SPEC + CHECKLIST) — ships on Will's go for the CARL-drop · (c) this REQ close + the I3 template-kill.
- **PROME:** (1) route **SAM canonical** packet (unambiguous — green-lit) + a **REGINALD drain-step** packet · (2) **CARL-only** bulk-archive + commit (cross-dir write; after WALTER's skip-rule lands, so we don't archive-then-redeliver). Skip anything WALTER flagged (nothing for CARL; hold REGINALD's OZK item — it stays on the lane).

*Below = the original 7/3 packet, retained for provenance; the route is now SAM-install / REGINALD-install / CARL-drop / RED-done.*

---

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
