---
name: boot
description: PROME session boot runner — the execution order for `PROME/BOOT.md` (which stays canonical). Use on "please boot up", "boot", session start. Reads the chain in owner order, runs the one-shot gate, and FORCES the owed-items question to Will before any directed work starts.
user-invocable: true
---

# /boot — PROME boot (order of operations; rules live in `PROME/BOOT.md`)

0. **Banner check:** the SessionStart banner should already be in context (`[boot-banner] repo a/b vs origin/master …`). No banner ⇒ flag to Will and run `git status --short && git fetch origin && git rev-list --left-right --count HEAD...origin/master` by hand. `date`/the NOW: stamp before any timestamp you write.
1. **Read in owner order:** `USER.md` → `PROME/HANDOFF.md` (top entry) → `PROME/SCRATCH.md` (whole — ★ NEXT SESSION is the spine) → `PROME/ACTIVE_DECISIONS.md` (head + live index) → `PROME/STATUS.md` (header + spine-audit stamp) → `HEARTBEAT.md` (orientation only on weekends/holidays; observation dates preserved).
2. **One-shot gate:** `python3 PROME/tools/prome_gate.py boot` — ONCE (it advances the board cursor). BLOCKING fails ⇒ disposition before anything else. Read every advisory line; the WQ cap and firetime flags are usually carried — say so rather than re-discover them.
3. **⚠️ OWED-ITEMS QUESTION — mandatory, before directed work.** If SCRATCH item 0 (or the HANDOFF "not run" line) lists work owed from a prior session, put it to Will as ONE line with a recommendation: *"Owed from <date>: A · B · C. Run them first (~N min) or after the <directed lane>?"* — never just mention them. Three sessions in a row (8/28–8/29) mentioned T6/HEN-42/NEXUS at boot and let the directed lane absorb the session; the closeout gate caught it each time at the END. A dated owed item that reaches its third boot unrun gets a DOCKET `COVERED:` annotation or a WQ row — it stops being a SCRATCH bullet.
4. **Declare boot state** (one short block): synced/dirty · regime source + freshness posture · top lane · blockers · catalysts inside 24h · spine-audit stamp age (>7d ⇒ `/spineaudit` this session or say why not).
5. **Conditional reads** only as BOOT.md §6 triggers them (ROSTER/FLEET_MAP for fleet work; `PROME/inbox/` is the sole delivery surface — anything under `AGENTS/PROME/` is a sender regression: read, migrate, flag).
6. **Then** the session's work. Structure/hygiene asks are Will's to direct; the owed items are yours to have ASKED about.
