---
name: boot
description: PROME session boot runner — the execution order for `PROME/BOOT.md` (which stays canonical). Use on "please boot up", "boot", session start. Reads the chain in owner order, runs the one-shot gate, reports owed work and urgent obligations, then CONTINUES Will's directed task — interrupting only when his answer is necessary for the next action.
user-invocable: true
---

# /boot — ordered index over `PROME/BOOT.md`

This file is an **index in execution order**, nothing more. Every rule, threshold, path list and reason lives in `PROME/BOOT.md`; each line below names the BOOT.md step that owns it. The order here differs from BOOT.md's numbering on purpose (steps 3–6 below = BOOT.md 7 · 8 · 6 · 9). On any conflict BOOT.md wins — fix this index rather than working around the conflict.

Commands are quoted here only where they are stable interfaces; they are copied from BOOT.md verbatim, including the repo-root `cd` (PROME launches from `PROME/`, where a bare `PROME/tools/…` path does not resolve).

0. **Repo state + the clock** → BOOT.md step 0 (early runtime capability disclosure, the banner, the no-banner rule, the repo-state checks + pull-if-safe, the `NOW:` stamp).
1. **Reads, in owner order** → BOOT.md context-injection paragraph and “Bounded reads” · `USER.md` at the repo root (per `PROME/CLAUDE.md` Boot step 1) · BOOT.md steps 1–4 (`HANDOFF` → `SCRATCH` → `ACTIVE_DECISIONS` **with `GATES.tsv`** → `STATUS`) · step 4b (§ Boot-class fleet memories) · BOOT.md step 5's non-gate items (the `HEARTBEAT.md` read and weekend rule, dashboard-before-levels).
1b. **Decision Deck pickup** → BOOT.md step 3b (read the deck's `rulings` store; consume taps into `WILL_QUEUE.md`; never share the artifact; read WALTER `LAST_COMPLETION.md` §WILL_NEEDS as a deck feed — WQ-206).
2. **One-shot gate** → BOOT.md step 5 "⚡ ONE-SHOT GATE", run ONCE:
   `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/boot_session.py --run-dir /tmp/prome-boot-<session-id>`
   BOOT.md step 5 owns the gate's meaning and log-read contract (including the bounded orchestration-log view and full-text fallback); step 6 owns the board-scan re-run rule.
3. **Declare boot state** → BOOT.md step 7.
4. **Report, then continue** → BOOT.md step 8 (the interrupt test, the hands-vs-answer rule, the anti-scoping clause and the third-boot disposition all live there). ⚠️ **BOTH halves of BOOT.md step 8** — the report-and-continue contract AND the `PROME/STATUS.md` `Last spine audit:` stamp check. `prome_gate.py boot` carries no check for that stamp, so this runner is its only carrier. (Named here 2026-09-12, spine audit #13 — the runner had carried one half.) ⛔ **Do not stop for an answer unless BOOT.md step 8's interrupt test returns YES.**
5. **Conditional reads** → BOOT.md step 6.
6. **Top proposals** → BOOT.md step 9.
7. **Then the session's work — start it, do not wait.** Work the scoped task (`PROME/CLAUDE.md` Boot step 4); with no scoped task, the highest-priority authorized work. The owed items are yours to have REPORTED (BOOT.md step 8), not to have asked about.
