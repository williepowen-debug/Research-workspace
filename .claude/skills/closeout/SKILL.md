---
name: closeout
description: PROME session closeout runner — the execution order for `PROME/CLOSEOUT.md` (which stays canonical). Use on "close out", "lets close out", before /clear or a machine switch, or a long pause. Picks the tier (Light / Standard / Heavy / Bounce), runs the mechanical gate, writes the state files in owner order, commits path-scoped, auto-pushes with the receipt.
user-invocable: true
---

# /closeout — PROME closeout (order of operations; rules live in `PROME/CLOSEOUT.md`)

0. **Read `PROME/CLOSEOUT.md` "When to run" + "Skip rules"** and pick the tier. Say the tier to Will in one line. `date` (or the NOW: stamp) before every timestamp you write.
1. **Mechanical gate first:** `python3 PROME/tools/prome_gate.py closeout` — BLOCKING fails are dispositioned before any prose. It runs DOCKET-today, orphan_check, WILL_QUEUE reconcile, byte budgets. Read the advisories.
2. **State files, owner order (Chunk 1):** WILL_QUEUE (rows ruled today → RECENTLY DONE with anchors; new Will items registered; reconcile stamp = ONE stamp) → GATES/DOCKET (rows fired/resolved/re-dated) → SCRATCH full rewrite (★ NEXT SESSION first; errors ledger; cautions; operator card FROM THE MIRROR; calendar = DOCKET view) → STATUS header (one-line headline; spine-audit stamp) → HANDOFF entry (rotate the oldest if >5; crc32 recomputed from the archived bytes) → HEARTBEAT only if a market/system event or Will decision changed it.
3. **Memory (Chunk 2):** `memory/YYYY-MM-DD.md` daily log. Auto-memory only for an unpredictable-trigger lesson; if the MEMORY.md byte check reads ≥75%, demote to cold until <70% (never delete). `python3 scripts/memory_index_check.py --strict --slug <name>` per new slug; `bash scripts/check_memory_length.sh`.
4. **Residuals (Chunk 3, trigger-gated):** consumer_check if a figure was superseded · ledger_staleness nudge if STATUS moved without its ledgers · claim_check weekday on DOCKET/GATES/WILL_QUEUE/SCRATCH/STATUS · research retirement (>60d, unread, unreferenced → archive) · `.claude/agents` + `.claude/skills` root↔PROME parity (gate advisory).
5. **Git (Chunk 4):** every commit through `python3 PROME/tools/commit_check.py commit -F <msgfile> -- <exact paths>` (message via the Write tool, never inline — the git guard reads prose as commands; the same applies to ANY prose that quotes a git command — DOCKET/WILL_QUEUE row text, packet bodies — write it via the Write tool or inside a heredoc, which the guard strips). Root/shared docs only on Will's word, cited verbatim in the message. Then `bash scripts/safe-push.sh` — the receipt is `Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch).`; anything else is not a receipt. Non-ff ⇒ `git pull --rebase --autostash` after checking incoming paths don't overlap dirty paths; never force.
6. **Report to Will:** what landed (hashes), what's owed at next boot, open ⚖️ rows by number, the push receipt line verbatim.
