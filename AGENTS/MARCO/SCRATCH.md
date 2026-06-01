# MARCO SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-05-31 ET (session 7)

## CHANGES SINCE (what moved while offline)
- Nothing external this session — session 7 followed directly after session 6 (same evening, 9:17 PM ET). No new data releases. Pure housekeeping/infrastructure session.

## WHAT I DID (session 7 — domain cleanup + docket build)
**1. Legacy-file cleanup (root de-cluttered, 16→11 live .md):**
- 🗑️ Trashed (via `gio trash`, recoverable in `~/.local/share/Trash` + git history): `MARCO_STARTUP_PROMPT.txt` (dead C:/ Windows paths), `OUTBOX.md` (stale stub; real outbox is `outbox/` dir), `LAST_COMPLETION.md` (legacy, SCRATCH supersedes per CLAUDE.md).
- 📦 Archived → `domain/sources/_archive/`: `CHECKIN_2026-03-06.md` (was CHECKIN_MAR6.md), `DECK_EVIDENCE_2026-03-13.md` (was DECK_EVIDENCE.md).
- ♻️ Refreshed `EXPECTED_SIGNALS.md` (was stale) — resolved ES-03 (condo >9mo APPEARED Mar) + ES-02 (snowbird PARTIAL — capacity confirmed, demand >20% did not appear); updated 5 active signals with dated current-reads. Now a live complement to PREDICTIONS.tsv.
- ✅ Kept: `NOTES.md` (live deportation-data-discrepancy caveat), `MARCO_SKELETON.md` (v1.0 artifact, already marked superseded), `handoffs/` + `archive/` (already subdirs).

**2. Built `docket/` — the last deferred infra (now full SAM/CARL/BRENT mirror):**
- `docket/CATALYSTS.tsv` — 12-row forward machine feed, peer schema (date/event/what_to_check/threshold_signal/priority/who_cares/notes). Source-of-truth for forward dates.
- `docket/CALENDAR.md` — countdown twin, grouped by window (overdue / this week / mid-June / late-June-Q3 / Q4-annual), day-counts anchored to 2026-05-31.
- Built from STATUS KEY DATES + RESEARCH_STATUS gaps + PREDICTIONS timeframes.

**3. Wired docket into the system:**
- CLAUDE.md closeout step 8 rewritten — docket is now forward-state owner; STATUS KEY DATES demoted to pointer.
- CLAUDE.md deferred-infra note → "Infrastructure (built)"; **no remaining deferred builds.**
- CLAUDE.md FILES table — added docket/CATALYSTS.tsv, docket/CALENDAR.md, EXPECTED_SIGNALS.md.
- STATUS.md KEY DATES replaced with docket pointer + imminent-5 near-term cut. Header → session 7.

**4. Verification pass + ledger reconciliation (Will's "double-check" request):**
- Verified all of the above: TSV machine-clean (7 fields/row, schema byte-identical to SAM), weekdays/day-counts correct, CALENDAR↔TSV consistent, facts match STATUS, deletions recoverable in Trash, archives landed.
- **Caught + fixed a real gap:** predictions #21/#22/#24 (planting-raid→produce, OIA-negative, all-3-FL-airports) were tracked ONLY in STATUS.md, never in the canonical thesis/PREDICTIONS.tsv ledger. My docket had minted dangling "MAR-21/22/24" refs. **Fixed:** formalized all three into PREDICTIONS.tsv (8-field convention, original-confidence-in-col, Date_Made 2026-02-23 flagged inferred). STATUS↔ledger divergence now fully closed — every STATUS active prediction has a ledger entry.
- **Resolved the FLL-vs-TPA question:** canonical 3 FL airports = MIA/MCO/FLL (MARCO has baseline data files for all three; TPA is unbaselined). MIG-03 sub-agent's "TPA" is non-canonical — documented in the MAR-24 note.

## NEXT SESSION (dated, future-verifiable)
1. **Jun 1 (TOMORROW):** Watch ICE/CBP reconciliation passage ($71.7B). 🔴 — if passes, log to TIMELINE + signal NEXUS/LABOR.
2. **~Jun 2:** Banxico Apr remittances — run the paradox test (does count recover → tax pull-forward, or stay − → SDL-01 confirmed).
3. **Jun 10:** BLS May CPI fresh F&V — primary signal; feeds the produce-attribution decomp (still Tier-1, not started).
4. **PULL the StatCan Q1 BOP** (overdue since ~May 28) — Canadian-corridor cross-check.
5. **Produce-spike attribution decomp** (labor vs weather/energy/tariff) — STILL the top research item, deferred again this session for infra work.
6. **Cross-agent correction re-sends** (REGINALD condo-tightening, LABOR ICE-off-farms, CARL, NEXUS inflection) — still pending Will's clearance to send.
7. **TOURISM sub-agent** re-spawn-vs-shelve decision — still open.

## OPEN THREADS
| Item | Status |
|------|--------|
| Produce-attribution decomp | 🔴 Tier-1, deferred 2 sessions for infra — DO NEXT |
| Remittance paradox (count −3.6% vs $ +4.9%) — tax pull-forward test | 🟠 — Jun 2 Banxico print is the test |
| Cross-agent correction re-sends | 🟠 — awaiting Will's clearance |
| TOURISM sub-agent (stalled since Apr 22) | 🟡 — re-spawn or shelve |
| ICE off-farm pivot durability | 🟡 — Q4 test (in docket) |
| ✅ ~~Deferred build: docket/~~ | DONE this session — no deferred builds remain |
| MIG-03 sub-agent says FL airports = MIA/MCO/TPA (canonical = FLL) | 🟡 minor — fix in sub_agents/MIGRATION/workbook/PREDICTIONS.tsv next MIGRATION spawn |
| MAR-18 (Canadian air capacity) OPEN in ledger but absent from STATUS active table | 🟡 minor — pre-existing; re-add to STATUS active set or confirm intentional drop |

## Mail state
Inbox NOT processed (normal spawn). Outbox empty (no pending signals). No signals sent this session.

## Handoff
Session 7 = infrastructure complete. MARCO now mirrors the full SAM/CARL/BRENT shape (thesis/ + docket/ both built). Next session is back to RESEARCH: produce-attribution decomp is the overdue Tier-1. Git: committing session-7 housekeeping at closeout.
