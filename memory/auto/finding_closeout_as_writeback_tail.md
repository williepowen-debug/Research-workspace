---
name: finding_closeout_as_writeback_tail
description: "Codify session closeout as the write-back tail of the auto-loaded CLAUDE.md SPAWN PROTOCOL, not a standalone doc; auto-load is the decisive factor"
metadata: 
  node_type: memory
  type: finding
  originSessionId: ce1da1cb-3936-497e-9926-8c9fd798acbc
---

When codifying an agent's session-end closeout, make it the **write-back tail of the SPAWN PROTOCOL inside CLAUDE.md** (the always-auto-loaded instructions), mirroring the boot read-phase — NOT a standalone `CLOSEOUT.md`.

**Why:** CLAUDE.md is pulled into context every session automatically; a standalone doc requires *remembering to open it* at exactly the moment you're least likely to — session end, full context, "just commit and go." Closeout is the most skip-prone step, so the checklist must be where you'll see it without an act of remembering. Secondary reasons: boot/closeout adjacency makes read→write pairings legible (read STATUS at boot N → write STATUS at closeout M), so omitted write-backs are visible; and one sequence can't desync the way two files can. Bulk detail (templates, rewrite rules) → referenced files loaded on demand, so CLAUDE.md doesn't bloat (it pays a context tax every boot). This is the hybrid SAM and CARL both converged on.

**How to apply:** For any agent lacking a codified closeout (REGINALD/BROCK/HENRY candidates), add BOOT / EXECUTE / CLOSEOUT phase headers to its CLAUDE.md SPAWN PROTOCOL. Closeout skeleton (~7 steps): STATUS write-back → workbook/ledgers + resolve due predictions → thesis+CHANGELOG (version bump) → forward-state (catalysts TSV authoritative, incidents, tracker) → rewrite ephemeral handoff via a template → promotion scan → git. Push the handoff template to a referenced `templates/` file.

**Corollary (validated 5/31 on BRENT):** run the closeout immediately after writing it — the first dogfood run surfaced a stale `CATALYSTS.tsv` (frozen 6 weeks, fired rows never pruned, missing all near-term catalysts) that was making `boot.py`'s countdown silently under-report upcoming events. Forward-state maintenance (the closeout step that prunes/syncs the catalyst feed) is exactly what catches that drift; a "TSV authoritative" claim is only real once something runs it. Also watch for protocol steps that name ledger files the agent has quietly stopped maintaining (BRENT's KB/VX/FLOW dormant 6+ wks) — decide revive-vs-demote rather than letting the protocol claim upkeep that isn't happening.

Related: [[feedback_intra_day_closeout_discipline]] (run closeout at every session end, not just end-of-day), [[finding_followup_audit_pass]] (end-to-end re-read surfaces adjacent drift), [[feedback_check_existing_design_docs]] (search before authoring new spec).
