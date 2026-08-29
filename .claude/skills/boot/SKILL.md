---
name: boot
description: PROME session boot runner — the execution order for `PROME/BOOT.md` (which stays canonical). Use on "please boot up", "boot", session start. Reads the chain in owner order, runs the one-shot gate, and FORCES the owed-items question to Will before any directed work starts.
user-invocable: true
---

# /boot — PROME boot (order of operations; rules live in `PROME/BOOT.md`)

**This is a RUNNER over `PROME/BOOT.md`, not a replacement for it.** Every step below maps to a BOOT.md step and carries no rule of its own. If a step here is unclear, or the session is protocol/structure-shaped, open BOOT.md — the reasons are only there.

0. **Banner check (BOOT step 0):** the SessionStart banner should already be in context (`[boot-banner] repo a/b vs origin/master …`). **The banner already ran `git fetch`** and flags `[FETCH FAILED — do not trust 0/0]` on failure — a clean banner is a fetched 0/0, not a stale one. No banner ⇒ flag to Will and run `git status --short && git fetch origin && git rev-list --left-right --count HEAD...origin/master` by hand. `date`/the NOW: stamp before any timestamp you write.
1. **Read in owner order (BOOT steps 1–5):** `USER.md` → `PROME/HANDOFF.md` (top entry) → `PROME/SCRATCH.md` (whole — ★ NEXT SESSION is the spine) → `PROME/ACTIVE_DECISIONS.md` **(header + the Live Decision Index ROWS — the section headings are not the index)** → **`PROME/GATES.tsv`** (fire-ledger; BOOT step 3 pairs it with ACTIVE_DECISIONS — the gate checks it mechanically, you still read it) → `PROME/STATUS.md` (header + spine-audit stamp) → `HEARTBEAT.md` (orientation only on weekends/holidays; observation dates preserved) → **`PROME/BOOT.md` § Boot-class fleet memories** (~4.7 KB, 15 one-liners — the boot-class lessons have no other carrier; skipping them is how a solved failure comes back).
2. **One-shot gate:** `python3 PROME/tools/prome_gate.py boot` — ONCE (it advances the board cursor). BLOCKING fails ⇒ disposition before anything else. Read every advisory line; the WQ cap and firetime flags are usually carried — say so rather than re-discover them. **To re-check ONE advisory later in the session, run that check standalone** (`board_scan.py` with no `--advance`, `firetime_check.py`, the parity/byte checks) — never re-run the gate for it.
3. **Owed-items question (rule = `PROME/BOOT.md` step 8):** if SCRATCH item 0 / HANDOFF "not run" lists prior-session work, ask Will in ONE line — *"owed from <date>: A · B · C — first, or after <directed lane>?"* — with a rec, before any directed work. Third boot unrun ⇒ DOCKET `COVERED:` or WQ row, per the rule.
4. **Declare boot state (BOOT step 7)** (one short block): synced/dirty · regime source + freshness posture · top lane · blockers · catalysts inside 24h · spine-audit stamp age (>7d **or missing** ⇒ `/spineaudit` this session or say why not).
5. **Conditional reads (BOOT step 6)** only as their triggers fire: ROSTER/FLEET_MAP for fleet work · **`AGENTS/*/outbox/*to-PROME*` for routing/signal work** (`[[feedback_scan_agent_outboxes_at_boot]]` — the inbox is not the only place PROME-targeted signal lands) · `PROME/inbox/` is the sole delivery surface — anything under `AGENTS/PROME/` is a sender regression: read, migrate, flag.
6. **Present top proposals (BOOT step 9)** only when useful; max 5, ranked by urgency/position relevance.
7. **Then** the session's work. Structure/hygiene asks are Will's to direct; the owed items are yours to have ASKED about.
