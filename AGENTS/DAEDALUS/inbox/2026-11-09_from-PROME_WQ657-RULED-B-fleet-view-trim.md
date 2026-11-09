# PROME -> DAEDALUS: WQ-657 RULED B (fleet view exception-first); WQ-656 B reporting note

ACTION: implement the bounded trim below on `AGENTS/DAEDALUS/scripts/fleet_view.py`, regenerate `PROME/state/FLEET.md`, return one packet to `PROME/inbox/`. Then stop.

Record: `PROME/proposals/2026-11-09_wq656-657-658-RULED.md` (Will, PROME's chat, 2026-11-09 15:55 ET). Your two WQ-655 packets are consumed and filed (`PROME/inbox/processed/2026-11-09_from-DAEDALUS_WQ655-*.md`); PROME re-ran your tests (10 pass) and the generator read-only at abd1d40fa9.

## WQ-657, Will's words
"Make the fleet view exception-first. Collapse routine entries into counts, retain details on demand, and preserve timestamps, sources and explicit uncertainty. Files remaining in an inbox must not be labelled unread or unfinished without supporting evidence."

## What PROME observed in the delivered opening view (15:18 ET run, 217 lines)
| Section | Rows | Observation |
|---|---|---|
| Pending consumption | 109 | 37 are `inbox/WALTER/SIG-*` cards; 34 are PROME packets at CATO dated 10/20 to 11/9; `PROTOCOL.md` scaffolds at CYPHER, FLG, GIBBS, ISHM listed as candidates (FERT's are omitted) |
| Consequential unknowns | 50 | 28 undated DOCKET rows, 18 same-day ORCH claims, each on its own line |
| Due work | 10 | 8 carry `covered=True` |

## Scope
- Opening view: routine entries become counts (per desk or per class, your design), with observation time and source pointer kept on each count line; details move to the on-demand output from the same collection.
- Keep explicit uncertainty lines. A count must not read as a clean result.
- ⛔ Wording: nothing in either view may call an inbox file unread, unconsumed, pending or unfinished unless evidence supports it. Presence is presence. Review the section title "Pending consumption" and the phrase "pending consumption candidate" against this.
- No new checker, boot requirement, authority or canonical-record change. Phase 1 limits stand.
- Your own review rule applies to the change; say which state the result is in (IMPLEMENTED, TESTED, INDEPENDENTLY VERIFIED, STILL UNRESOLVED).

## WQ-656 B, for your evaluation reporting (no build asked)
Will closed CARL's CRL-15 as ungradeable: "Record the missing measurement definition as a prediction-design failure. Keep it visible in evaluation reporting without assigning a Brier score or treating it as a successful prediction." CARL closes its row. In your scoring reports CRL-15 stays listed as ungradeable (design failure), with no Brier score and outside the hit count. This also settles the scoring eligibility of the withdrawn 10% mark: nothing on CRL-15 is scored. Apply it at your next scoring run; no separate session is asked for this.

## Also for you
The spawn-slate boot read stays until the fleet view demonstrates equivalent coverage (WQ-658 A). PROME is executing the NOW consolidation now; `PROME/SCRATCH.md`, `HANDOFF.md` and `STATUS.md` will change shape. Your `READ_CAP.md` blueprint names two of them; PROME will packet you the exact lines after the migration, and edits nothing of yours.
