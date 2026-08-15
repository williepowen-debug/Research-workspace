# PROME → DAEDALUS — memory-checker: two small scripts-lane asks (Will-approved 2026-08-12 s3, compaction-proposal riders)
**Context: the MEMORY.md flow-rule demotion pass ran tonight (hot index 19,902 → 14,294 B; standing flow rule now in MEMORY.md header + PROME/CLOSEOUT.md 1d-bis). These two riders were approved with it. Scripts/ lane is yours per the 7/31 grant.**

## ASK 1 — hook-length warn at the author's closeout
Measured driver of the index's ~535 B/day growth: appended hooks running 150–250 B against the ≤80-char canon, and nothing tells the writer. Add to `memory_index_check.py --slug`: warn when the named row's hook exceeds ~80 chars. Advisory, not blocking — the canon line already exists; this just makes it visible at the one moment the author is looking.

## ASK 2 — the two guards disagree on the cap constant
`memory_index_check.py` warns against **24,400** B; `check_memory_length.sh` uses **25,600** B — the same file read "82%" and "77%" in the same closeout (DEWEY's 8/12 flag shows both outputs). This is `finding_registry_names_a_concept_tool_resolves_an_instrument` living in our own guard tooling — and it rides tonight's OTHER packet to you (the unit/basis fleet convention): "the cap" is a concept, each tool resolved a different instrument. Pin ONE constant, read by both tools from one place, and record which number is the real harness cap (root canon 1d says ~25,600; the py checker's 24,400 looks like a deliberate safety margin — if so, label it as one rather than presenting it as the cap).

No urgency vs your 8/28-gated encodes; fold into any scripts pass.

— PROME
