# MARCO SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-02 ET (session 11 — workbook bring-current sweep, same-day after session 10)

## CHANGES SINCE (what moved while offline)
- Same-day reboot after session 10 (Jun 1 reconciliation + Apr Banxico). No new market data between sessions except the NTTO release surfaced below.
- **NTTO overseas arrivals Apr 2026: −14.1% YoY** (2.6M); non-US-citizen air −9.8%; YTD overseas −4.3%. New datapoint (release ~May). Deteriorating on YoY — the non-Canada international channel, an independent leg under the structural-tourism read.

## WHAT I DID (session 11 — Will's task: "get MARCO updated to current" = full pass: data + structure + carried debt)
- **FLOW.tsv** — fixed newline-merge bug (FLOW-IMG-01/FLOW-BDR-01 were one line); added the owed **FLOW-PRD-01** (diesel/freight→produce-CPI transient CONFOUNDER, MARCO↔BRENT, carried 3 sessions); now 12 flows, all 12 cols clean.
- **VX.tsv** — fixed newline-merge bug (3.04/ELP-01) + a pre-existing 13-col bug (VX-MARCO-3.03 missing Priority → added HIGH). Synced to current: **2.08** (Apr remittances + normalizing), **2.01** (ICE off-farm pivot + funding contested), **1.01** (session-9 structural 2-yr-stack read), **1.02** (NTTO Apr −14.1%, was frozen at Jan "8% below 2019"). All 57 rows now 14 cols.
- **ML.tsv** — fixed TWO corruptions (line-40 field-join MIG-05/BDR-01; line-50 REM-03 description duplication); parses cleanly (59 rows). Flagged 2 contradicted entries (ML-IVF-02, ML-IVF-05 Canadian magnitudes) with `[DATA STALE]` pointers in Status (KB-safe — Status isn't KB-mapped). Documented in CLAUDE.md FILES table as the **FROZEN founding-research log** (Jan20–Feb4), superseded by KB.tsv.
- **KB.tsv** — appended KB-MARCO-IVF-NTTO-26 (overseas −14.1%); normalized a 7-col row. 63 lines, all 8 cols.
- **Banxico Apr RE-VERIFIED vs primary** — data agent flagged a trade-press "$5.69B/+26% Apr" claim conflicting with our $4.98B/+3.7%. Checked Banxico primary + 6 MX outlets: **our figure is CORRECT; the $5.69B/+26% is garbled** (the "+15%/$21.3B cumulative" claim flatly contradicts the Banxico $19.68B primary — likely a May/Mother's-Day mislabel). Inoculation note added to STATUS remittance row. The fleet figure held; the "fresh" number was the bad one.
- **Structural parity** — verdict: MARCO already at/above fleet (SAM/CARL/BRENT/VIOLET) parity. Has canonical SCRATCH, thesis machinery (THESIS/CHANGELOG/TIMELINE/PREDICTIONS), docket, ROOMS+DEFERRED+COUPLINGS (richer than CARL/SAM), LAST_COMPLETION retired. Gaps (`board/BOARD_LOG.tsv`, `templates/SCRATCH.template.md`) judged cargo-cult for MARCO — no upstream BOARD feed to diff; SCRATCH structure already specified in CLAUDE.md. **No structural builds.**
- **Found**: `ml_to_kb.py` is now LEGACY/destructive — mode 'w' would wipe hand-added KB rows (sessions 8+). Flagged in CLAUDE.md. KB.tsv is now the hand-maintained living workbook.

## NEXT SESSION
1. **Jun 5 BLS May NFP** — FL leisure/hospitality sub-sectors (ES-MARCO-01), not headline. **Jun 10 CPI = ES-MARCO-08** (produce-vs-pump fork, v2.1; FLOW-PRD-01 now formalizes the confounder).
2. **Jun 11 StatCan May** — read the 2-yr STACK (does it worsen past −30%?). **Jun 13 Air Transat** final US flight. **~Jun 17 FL Realtors May** (condo: >9.0 = distress re-engaging, <8.5 = absorption). **~Jun 27 WestJet** winter = TOUR-05 last input.
3. **MCO/FLL April pax** — confirmed NOT a MARCO miss; airports publish 4–6wk lag, April not out yet. Re-pull ~mid/late-Jun (flymco.com/airport-business, broward.org/Airport). MAR-22/MAR-24 stay OPEN until then.
4. **Reconciliation rework watch** — GOP strip Byrd-flagged provisions + retry floor vote (~late Jun, TBD). 🟠 open, not done.
5. **Cross-agent re-sends (still deferred per Will — mail-dedicated spawn):** NEXUS carries 3 corrections (v2.1 produce-thermometer, v2.2 tourism-structural, v2.3 enforcement-lock→contested) + REGINALD (condo tightening) + LABOR (ICE off-farms).

## OPEN THREADS
| Item | Status |
|------|--------|
| ICE/CBP reconciliation rework + floor vote | 🟠 ~late-Jun TBD |
| ES-MARCO-08 produce-vs-pump test | 🔴 Jun 10 CPI |
| WestJet winter 2026-27 schedule | 🟠 ~Jun 27 — TOUR-05 last input |
| MCO/FLL April pax (data not yet published) | 🟡 re-pull ~late-Jun |
| Cross-agent correction re-sends (3 for NEXUS) | 🟡 deferred — mail-dedicated spawn |
| Top-level workbook FLOW.tsv lag | ✅ RESOLVED 6/2 — FLOW-PRD-01 added, file repaired |
| Remittance paradox | ✅ RESOLVED 6/2 (session 10) — normalizing; Apr re-verified session 11 |

## Mail state
Inbox + outbox empty. No outbound written (cross-agent re-sends still deferred per Will).

## ⚠️ PENDING PUSH (session 11)
Session-11 commit is LOCAL only. Origin diverged (remote +1) and RED + LABOR have uncommitted working-tree changes → per git protocol, did NOT pull/rebase (would risk their work). **Push deferred to next session** once the tree is clean outside MARCO. Local commit is safe.

## Handoff
Session 11 was a "bring MARCO current" sweep — no thesis change, all confirmatory. Three workbook TSVs (FLOW, VX, ML) had latent structural corruptions (newline-merges, a duplication, a dropped column) now all repaired and column-validated; VX synced to the v2.3 reads; ML documented as the frozen founding log with KB.tsv as the living file. The one substantive new datapoint (NTTO overseas −14.1% YoY Apr) reinforces structural-tourism on an independent non-Canada leg. The Banxico re-verify is the session's quiet win: a "fresher" trade-press number was wrong and our established figure held — primary > aggregator. Thesis spine (SDL-01, v2.3) untouched. Clean handoff; all MARCO files current and structurally valid.
