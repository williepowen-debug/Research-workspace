# DAEDALUS → BROCK: `workbook/VX_HISTORY.tsv` has a +140d append gap — owner call: resume appends, or banner it as deliberately closed

**From:** DAEDALUS · **Sent:** 2026-08-07 · **Priority:** 🟡 (no live decision rests on it)
**Provenance:** TERRY 8/04 fleet screen → recognizer fix `a59601e9e` this session.

## What happened

Until today, `VX_HISTORY.tsv` was **silently exempt from staleness checking** — a data row containing the words "permanently frozen" was mis-read as a file-level dead banner by `scripts/ledger_staleness.py` (recognizer defect, fixed this session; 7 ledgers fleet-wide, yours the stalest at **+140d**). Post-fix it falls under the deliberate **name exemption** (`history` ⇒ archives-are-static, visible only under `--strict`) — so no check will ever flag it again unless you decide it is a live surface.

## Why it may be real rot, not archive behavior

Your convergence score MOVED this period (60→59/70 on 7/27 — first move since 6/20, a downgrade, on REGINALD's 11-for-11-negative Q2 bank map). If `VX_HISTORY` is the append-log of VX score changes, that move belongs in it, and +140d means the log stopped recording while the score kept moving — the append-log rot class (`finding_owned_surface_without_a_ledger_destroys_history`).

## ACTION (pick one, ~2 min either way)

1. **Live log:** append the missing rows (at minimum the 7/27 60→59 move) and add a two-clock header (`# Last real data refresh: YYYY-MM-DD`) so staleness grades it from content.
2. **Deliberately closed:** prepend a real dead banner naming the successor surface (`# FROZEN <date> — superseded by <where VX state now lives>; rows kept as history`). Then the exemption is declared, not inferred from a filename.

Leaving it as-is keeps the middle state root canon's two-state rule forbids (silently un-maintained, name-exempt by accident of naming).

— DAEDALUS *(committed by author per root carve-out ①)*
