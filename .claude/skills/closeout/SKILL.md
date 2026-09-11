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
2. **Preflight gate (optional)** → the same command as step 6; useful to surface BLOCKING items before you start writing, never a substitute for step 6.
3. **State files** → CLOSEOUT.md Chunk 1 (GATES/DOCKET bullet FIRST — it carries the enumerate-or-stated-no-op rule), plus the "Boot↔Closeout symmetry" table's Chunk-1 rows (`GATES.tsv`, `DOCKET.tsv`, **WQ LEDGER** — `python3 PROME/tools/wq_ledger.py sync` then `check`, after the WILL_QUEUE paired write, before the deck regen), its **`HEARTBEAT.md` row** (Write-Back Contract: regime-level change or >48h stale in a market week — ask at every tier, answer no-op explicitly), and its Standard+ rows (**the two Will-facing pages regenerate LAST**). After any DOCKET touch, regenerate the view:
   `cd "$(git rev-parse --show-toplevel)" && python3 scripts/docket_view.py --write PROME/SCRATCH.md`
4. **Memory** → CLOSEOUT.md Chunk 2.
5. **Residuals** → CLOSEOUT.md Chunk 3 — trigger-gated at ANY tier; walk its list, don't recall it.
6. **FINAL gate — after every write in 3–5 and after the two pages regenerate, immediately before the commit** → CLOSEOUT.md "⚡ Mechanical tail in one shot" (it certifies the SHIPPED state; BLOCKING fails here are fixed before anything is committed; the parity line covers the skill trees):
   `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/prome_gate.py closeout`
7. **Git + push** → CLOSEOUT.md Chunk 4 in full — root steps 1b–1e, "PROME commit form" (the wrapper + the message-file rule), the command block including its pre-commit and post-push `git status` checks and the `memory/` commits, "Auto-push" for the receipt:
   `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/commit_check.py commit --stage --push -F <msgfile> -- <exact paths>`
8. **Report to Will** → CLOSEOUT.md Chunk 4 "Session summary to Will".
