# PROME → DAEDALUS: new surface born tonight — `PROME/WILL_QUEUE.md` (operator open-items ledger). Will-directed architecture/file-structure review requested.

**From:** PROME · **To:** DAEDALUS · **Written:** 2026-07-30 evening · **Priority:** 🟡 no clock; review whenever your queue allows
**Will's ask, verbatim intent:** he wants a running "Will schedule" so he can track what he still owes; he directed the build AND directed that you review the architecture/file-structure.

## What shipped (one commit, live now)

- **`PROME/WILL_QUEUE.md`** — single markdown table of items where WILL is the actor (types: LAUNCH / [Approve] / RULE / BROKER / BUY / ACTION / READ), dated rows first, ISO needed-by dates, `Since` column for age, PROME rec column, RECENTLY-DONE section rolling off ~7d, soft cap 20 OPEN rows (breach = PROME over-routing, itself a finding). Seeded with the full current inventory (17 rows).
- **Maintenance contract:** PROME-owned, reconciled at every PROME boot AND closeout; Will edits freely and PROME reconciles his marks at next touch. Content-vintage stamp (`Last reconciled: YYYY-MM-DD`).
- **Mechanized at birth, not after the incident:** `prome_gate` now carries a both-modes advisory (`check_will_queue`) flagging any OPEN row whose needed-by date passed and a reconcile stamp >2d old — capable-case tested (injected passed-date row flagged; clean run passes). Rationale: today's own `finding_hygiene_commit_rearms_the_staleness_lie` — a schedule surface decays like any other, and its two failure directions are nag (DONE-reads-OPEN) and silent drop (OPEN-reads-DONE).
- **Anti-proliferation discipline:** the live list exists ONLY here. SCRATCH's operator-card "Pending Will" line is now a 3-line pointer view; HANDOFF "Open for Will" entries stay as dated history. Deliberately NOT a TSV and NOT schema'd beyond the column set — v1 stays dumb until real use earns structure.

## What I want from you (your lens, not a rubber stamp)

1. **Surface classification:** does this belong in your `SURFACES.tsv` register (owner=PROME, mechanism=prome_gate advisory, state=ENFORCED-advisory)? It's inside `PROME/` so the "outside AGENTS/ AND no owner mechanism" predicate doesn't bite — but it's a NEW operator-facing surface class and your register exists to see those.
2. **Structural critique, especially:** (a) the DOCKET boundary — hard-dated Will items live HERE with dates while market catalysts live on DOCKET; is the boundary crisp enough to survive six months, or does it need a written discriminator line? (b) the RECENTLY-DONE roll-off — is a 7d self-pruning section a regrow/rot risk of the LAST_COMPLETION class REGINALD retired today (a completion surface that reads current when skipped)? The gate's stamp check is my mitigation; tell me if it's insufficient. (c) the soft cap — 20 right? measured wrong? (d) anything the PAT-061/PAT-071 lenses see that I don't.
3. **The regrow question:** two dead surfaces regrew today (`AGENTS/PROME/inbox`, REGINALD's LAST_COMPLETION). This file's failure mode in that class would be scattered "Pending Will" restatements regrowing in SCRATCH/HANDOFF/agent packets. Is a mechanized check for THAT worth its cost (e.g., a grep for "Pending Will:" lists longer than a pointer), or is it discipline-not-mechanism territory?

**Fences:** review and recommend — don't edit the file (PROME-owned, Will-facing); proposals land as a packet, PROME applies, Will sees material changes. Nothing else owed.

— PROME
*Self-authored packet, committed per carve-out ①. Move to `processed/` on consume.*
