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
2. **Mechanical gate** → CLOSEOUT.md "⚡ Mechanical tail in one shot":
   `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/prome_gate.py closeout`
3. **State files** → CLOSEOUT.md Chunk 1 (which now lists the two ledgers), plus the "Boot↔Closeout symmetry" table's Chunk-1 rows (`GATES.tsv`, `DOCKET.tsv`) and Standard+ rows (**the two Will-facing pages regenerate LAST**). Before the ledgers: name every gate and catalyst this session touched; each gets a row edit or a stated no-op — "nothing moved" from memory is how a landed verdict fails to flip its row.
4. **Memory** → CLOSEOUT.md Chunk 2.
5. **Residuals** → CLOSEOUT.md Chunk 3 — trigger-gated at ANY tier; walk its list, don't recall it.
6. **Git + push** → CLOSEOUT.md Chunk 4 in full — root steps 1b–1e, "PROME commit form" (the wrapper + the message-file rule), the command block including its pre-commit and post-push `git status` checks and the `memory/` commits, "Auto-push" for the receipt:
   `cd "$(git rev-parse --show-toplevel)" && python3 PROME/tools/commit_check.py commit -F <msgfile> -- <exact paths>`
   `cd "$(git rev-parse --show-toplevel)" && bash scripts/safe-push.sh`
7. **Report to Will** → CLOSEOUT.md Chunk 4 "Session summary to Will".
