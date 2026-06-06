---
name: doc-mirror-consistency-check
description: Doc-ownership tables should encode canonical→mirror DIRECTIONS, not just "what each doc owns"; a closeout/boot check then verifies each pair agrees (canonical wins on mismatch). Catches silent state-file drift.
metadata:
  type: finding
---

A doc-ownership table that only lists "what each doc owns" doesn't prevent the most common state-file rot: a **mirror** drifting from its **canonical** source. The fix is to encode the *direction* (X is canonical, Y mirrors X) in the table, then add a consistency-check step that verifies each pair agrees — **canonical wins on mismatch**.

**Why:** Agents keep snapshot copies — STATUS mirrors the thesis matrix, the predictions ledger, the catalyst feed. Those silently diverge across sessions (and across machines). SAM's "what lives where" doc-ownership table and BRENT's "one source of truth per metric" discipline overlay both help, but **neither makes a *check* possible** — a check needs a defined canonical→mirror direction to verify against. Encoding the direction is the connective tissue that turns "ownership" into something mechanically verifiable.

**How to apply:**
- In the doc-ownership table, add a **"mirror pairs (canonical → mirror)"** list. CARL's three: `thesis/THESIS.md` matrix/score → STATUS matrix section · `thesis/PREDICTIONS.tsv` OPEN IDs → STATUS predictions table · `docket/CATALYSTS.tsv` → `docket/CALENDAR.md` event set. Adapt to each agent's own docs (REGINALD: thesis/positions → STATUS; HENRY: vol/Greeks → STATUS; etc.).
- Add a **closeout step** (conditional — only if you mutated a mirrored doc this session): verify the pairs agree before commit; on mismatch, fix the *mirror* (canonical wins), never the canonical.
- Best: **script it** (`scripts/consistency_check.py`, sibling of the catalyst countdown) and run it as a **boot scan** too — a manual eyeball check every boot gets skipped, and drift accumulates *between* sessions, so boot-side detection is the higher-value half.

Validated CARL Jun 6 2026: the check caught a real STATUS↔PREDICTIONS drift (3 OPEN predictions absent from the STATUS mirror) on its **first dogfood run** — the same failure class the audit had flagged hours earlier. Transferable to BRENT/SAM/REGINALD/HENRY — they have the ownership / one-source pieces but not the mirror-direction encoding. See [[finding_boot_closeout_hardening_recipe]], [[feedback_intra_day_closeout_discipline]].
