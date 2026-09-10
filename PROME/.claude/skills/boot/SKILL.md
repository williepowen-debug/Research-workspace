---
name: boot
description: PROME session boot runner — the execution order for `PROME/BOOT.md` (which stays canonical). Use on "please boot up", "boot", session start. Reads the chain in owner order, runs the one-shot gate, and FORCES the owed-items question to Will before any directed work starts.
user-invocable: true
---

# /boot — ordered index over `PROME/BOOT.md`

This file is an **index in execution order**, nothing more. Every rule, threshold, path list and reason lives in `PROME/BOOT.md`; each line below names the BOOT.md step that owns it. The order here differs from BOOT.md's numbering on purpose (steps 3–6 below = BOOT.md 7 · 8 · 6 · 9). On any conflict BOOT.md wins — fix this index rather than working around the conflict.

Commands are quoted here only where they are stable interfaces; they are copied from BOOT.md verbatim, including the repo-root `cd` (PROME launches from `PROME/`, where a bare `PROME/tools/…` path does not resolve).

0. **Repo state + the clock** → BOOT.md step 0 (the banner, the no-banner rule, the repo-state checks + pull-if-safe, the `NOW:` stamp).
1. **Reads, in owner order** → BOOT.md context-injection paragraph and “Bounded reads” · `USER.md` at the repo root (per `PROME/CLAUDE.md` Boot step 1) · BOOT.md steps 1–4 (`HANDOFF` → `SCRATCH` → `ACTIVE_DECISIONS` **with `GATES.tsv`** → `STATUS`) · step 4b (§ Boot-class fleet memories) · BOOT.md step 5's non-gate items (the `HEARTBEAT.md` read and weekend rule, dashboard-before-levels).
1b. **Decision Deck pickup** → BOOT.md step 3b (read the deck's `rulings` store; consume taps into `WILL_QUEUE.md`; never share the artifact).
2. **One-shot gate** → BOOT.md step 5 "⚡ ONE-SHOT GATE", run ONCE:
   `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/boot_session.py --run-dir /tmp/prome-boot-<session-id>`
   BOOT.md step 5 owns the gate's meaning; step 6 owns the board-scan re-run rule.
3. **Declare boot state** → BOOT.md step 7.
4. **Flag top issues + the owed-items question to Will** → BOOT.md step 8 (the wording, the "choice not mention" rule, and the third-boot disposition all live there). Ask before any directed work.
5. **Conditional reads** → BOOT.md step 6.
6. **Top proposals** → BOOT.md step 9.
7. **Then the session's work.** Work only the scoped task (`PROME/CLAUDE.md` Boot step 4); the owed items are yours to have ASKED about (BOOT.md step 8).
