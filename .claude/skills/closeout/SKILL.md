---
name: closeout
description: PROME session closeout runner — the execution order for `PROME/CLOSEOUT.md` (which stays canonical). Use on "close out", "lets close out", before /clear or a machine switch, or a long pause. Picks the tier (Light / Standard / Heavy / Bounce), runs the mechanical gate, writes the state files in owner order, commits path-scoped, auto-pushes with the receipt.
user-invocable: true
---

# /closeout — ordered index over `PROME/CLOSEOUT.md`

This file is an **index in execution order**, nothing more. Every rule, tier definition, threshold, rotation recipe and reason lives in `PROME/CLOSEOUT.md`; each line below names the section that owns it. On any conflict CLOSEOUT.md wins — fix this index rather than working around the conflict. Which steps a tier runs is the tier table's business (Pre-closeout item 4), not this file's.

Commands are quoted here only where they are stable interfaces, copied verbatim with the repo-root `cd` — CLOSEOUT.md Chunk 4's STEP 0.

0. **Pre-closeout + tier** → CLOSEOUT.md "Pre-closeout", items 1–4 (item 3 applies at ANY tier; item 4 holds the tier table and the Standard+ MANDATORY surfaces). Take the clock per BOOT.md step 0 before writing any timestamp.
1. **Read CLOSEOUT.md § Closeout-class fleet memories** (the last section of the file) — before the writes, so they can shape them.
2. **Preflight gate (optional)** → the same command as step 7; useful to surface BLOCKING items before you start writing, never a substitute for step 7.
3. **State files** → CLOSEOUT.md Chunk 1 (GATES/DOCKET bullet FIRST — it carries the enumerate-or-stated-no-op rule), plus the "Boot↔Closeout symmetry" table's Chunk-1 rows (`GATES.tsv`, `DOCKET.tsv`, **WQ LEDGER** — `python3 PROME/tools/wq_ledger.py sync` then `check`, after the WILL_QUEUE paired write, before the deck regen), its **`HEARTBEAT.md` row** (Write-Back Contract: regime-level change or >48h stale in a market week — ask at every tier, answer no-op explicitly). ⛔ **The Will-facing pages do NOT regenerate here** — Fleet-Ops at step 6, Helm + Deck at step 8 (WQ-231). After any DOCKET touch, regenerate the view:
   `cd "$(git rev-parse --show-toplevel)" && python3 scripts/docket_view.py --write PROME/SCRATCH.md`
   After the WILL_QUEUE paired write, regenerate the Pending-Will block — mandated by CLOSEOUT.md's symmetry-table WILL_QUEUE row, which also owns why a skip ships under a green gate. (Commanded here from 2026-09-12, spine audit #13; step 7 had asserted it was "generated back at step 3" while no step commanded it.):
   `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/willq_view.py --write PROME/SCRATCH.md`
3b. **Blind-reader verification (trigger-gated)** → CLOSEOUT.md Chunk 1, which owns the triggers and the WQ-165 stop rule. Runner: `/coldread` step 4. (Added 2026-09-12, spine audit #13 — step 3's selective enumeration had made its absence read as completeness.)
4. **Memory** → CLOSEOUT.md Chunk 2.
5. **Residuals** → CLOSEOUT.md Chunk 3 — trigger-gated at ANY tier; walk its list, don't recall it.
5b. **ARGUS audit (Standard/Heavy)** → CLOSEOUT.md Chunk 4 item 1f — scope, spawn (or the rc-3 skip), apply ❌ only, ⚠️ to residue, RUN-LOG row. **BEFORE the gate** (WQ-231: its ❌ fixes are writes to gate-checked sources, and no such write may fall after the run that certifies — the scoped form; the manual's ⚡ bullet owns it):
   `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/argus_scope.py`
5c. **Root session-end steps 1b–1e** → CLOSEOUT.md Chunk 4 "Root session-end steps 1b-1e" — 1b orphan · 1c consumer · 1d memory-index · 1d-bis hot-index flow (PROME-only) · 1e claim. ⛔ There is no "ledger" member: root's ledger nudge is 1c-bis and the manual declares it N/A for PROME (no `PROME/workbook/LEDGER_GLOB`). **Their WRITES land here, before the gate** (WQ-231; a 1c packet or a 1d-bis demotion is a write like any other). The commit itself stays at step 9.
5d. **Helm SOURCE writes (Standard+)** → CLOSEOUT.md THE HELM row items ① and ② — if the picture changed, rewrite the BRIEF narrative and refresh `HANDBOOK.md` §Top priorities. These are hand edits to sources, so they run BEFORE the gate; only the render (③) follows it at step 8.
6. **Fleet-Ops dashboard (Standard+)** → CLOSEOUT.md symmetry row. Run it **before** the gate: it writes `PROME/tools/dashboard_state.json`, which IS the gate's input.
7. **FINAL gate** → CLOSEOUT.md "⚡ Mechanical tail in one shot" — after every write in 3–6, immediately before the render:
   `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/prome_gate.py closeout`
   **rc=1 ⇒ fix, then REGENERATE every derived artifact whose sources the fix touched, THEN re-run the full gate** (WQ-231). The gate reads the generated FILE, not the sources. The four: `dashboard_state.json` (step 6) · SCRATCH's DOCKET-VIEW (`docket_view.py --write`) · SCRATCH's Pending-Will block (`willq_view.py --write`) · `WQ_LEDGER.tsv`+`.crc` (`wq_ledger.py sync` then `check`) — the last three are generated back at step 3. ⛔ **No wq_ledger check exists in the gate**, so that one is never caught. Loop to rc=0; the gate that counts is the LAST one over the CURRENT derived state. ⛔ It does **not** certify "the shipped state": it establishes selected source records + `dashboard_state.json`, never the Helm, the Deck, publication, or the eventual (possibly rebased) commit.
8. **THE HELM + DECISION DECK render, then publish (Standard+)** → CLOSEOUT.md symmetry rows. Last, because they carry the change-feed and have no gate dependency — so no gate failure at step 7 can oblige a second real render. Report which state was reached: source VALIDATED → output GENERATED → page PUBLISHED. A publication failure does not invalidate the gate and is never reported as a shipped closeout.
9. **Git + push** → CLOSEOUT.md Chunk 4 in full — "PROME commit form" (the wrapper + the message-file rule), the command block including its pre-commit and post-push `git status` checks and the `memory/` commits, "Auto-push" for the receipt:
   `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/commit_check.py commit --stage --push -F <msgfile> -- <exact paths>`
9b. **ARGUS baseline (Standard/Heavy, AFTER the commit)** → CLOSEOUT.md Chunk 4 item 1f: `python3 PROME/tools/argus_scope.py --record-baseline HEAD`; commit the baseline file with the NEXT commit. ⛔ Skipping it leaves the baseline on the prior session, so tomorrow's ARGUS re-audits tonight's committed work and the trial metric is corrupted.
10. **Report to Will** → CLOSEOUT.md Chunk 4 "Session summary to Will".
