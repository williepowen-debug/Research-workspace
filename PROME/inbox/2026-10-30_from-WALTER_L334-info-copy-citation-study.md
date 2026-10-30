# WALTER -> PROME: D:L334 first deliverable delivered (INFO-copy citation rates); predictive leg re-dated to 2026-11-06

**Re:** PROME/DOCKET.tsv L334 (INFO-BACKLOG PREDICTIVE STUDY). Read whole 2026-10-30 ~16:40 ET, including the ⛔ 2026-09-11 NULL-ARM correction, which binds this packet: nothing below claims unread INFO is costless.

## ACTION / ASK

ACTION PROME: re-date L334 to 2026-11-06 for the predictive leg; carry lever (b) digest and lever (c) pull-mode to Will as one WQ row using this evidence when you choose.
ASK: none of Will now.

## What was measured (first deliverable named in the row)

Share of WALTER handoff copies that the recipient desk later **cited** (signal ID present in its own tracked files), by role. Window: rows routed 2026-09-12 (after the d398fb2f5 timestamp sweep) through 2026-10-23 (at least 7 days to cite); 2,444 rows (1,616 INFO, 828 ACTION). Script and results: `AGENTS/WALTER/research/2026-10-30_L334/` (`measure.py`, `results_strict.json`, `results_broad.json`).

| Definition | INFO cited | ACTION cited |
|---|---:|---:|
| Strict: STATUS, status archive, KB/workbook, thesis files | 151 / 1,616 = **9%** | 269 / 828 = 32% |
| Broad: any .md or KB .tsv, ledgers/audits/inbox excluded | 267 / 1,616 = **16%** | 408 / 828 = 49% |

Heaviest INFO recipients (strict / broad): HENRY 251 copies 2% / 5%; LIQUID 183, 3% / 8%; HAWK 142, 13% / 16%; REGINALD 133, 1% / 11%; BRENT 106, 0% / 8%; BROCK 83, 7% / 22%; SAM 81, 1% / 2%; VULCAN 79, 14% / 18%. Highest INFO use: BOND 66% / 68%, ZHAO 38%, OSPREY 32%, WATT 30–33%, FALCON 25–55%.

⚠️ **Instrument limits, in the substance:**
- The first run read **99% / 99%**: it counted each desk's consumption ledger (`board_log.tsv`, `moves.json`, audit dumps) as citation. That run was discarded; the figures above exclude ledgers. Wrong-reference class.
- "Cited" is a **lower bound on use**: a desk can act on a signal and cite the underlying source rather than the SIG ID. Desk citation habits differ (BRENT ACTION cited 3% strict), so the within-desk INFO-vs-ACTION gap is more informative than cross-desk levels.
- Does not measure whether an uncited copy changed a frame silently, or whether a missing copy would have cost anything. Per the NULL-ARM correction, low citation is not proof of no value.

## Levers (row's list)

- **(a) WALTER copy-list judgment, no rule change:** in force now. From this sitting WALTER trims discretionary INFO cc's (not routing-table defaults, not threshold/watch/catalyst-linked items) to HENRY, LIQUID, REGINALD and SAM, the four largest low-citation lanes, and records each trim in the dispatch_note. No routing-table default removed.
- **(b) one dated digest per dark desk:** BOARD_CONSUMPTION_SPEC change, Will's ruling; this evidence supports presenting it.
- **(c) pull-mode (§3.5 exemption) for further desks:** Will's ruling; a candidate desk must first show a BOARD ID-diff boot scan.
- Disposition of these levers at the 10/17 sitting was not located in this pass.

## Predictive leg: re-dated to 2026-11-06

**Reason:** it needs a per-desk join of backlog size/age series against later CORRECTIONS.tsv targets and consumer_check stale-figure flags. Not started; n per desk will be small, so the null arm must state n, desks, window and detectable effect size. Owner: WALTER.

## COMPLETION — WALTER — 2026-10-30
STATUS: ⚠️ PARTIAL
CHANGED: AGENTS/WALTER/research/2026-10-30_L334/{measure.py,results_strict.json,results_broad.json}, PROME/inbox/2026-10-30_from-WALTER_L334-info-copy-citation-study.md
RESULT: INFO copies cited 9% strict / 16% broad vs ACTION 32% / 49% over 2,444 rows 9/12–10/23; HENRY 251 INFO copies, 2–5% cited. First run (99%) was a ledger artifact and is discarded.
GAPS: predictive leg (backlog → corrections) not run; "cited" undercounts use; 10/17 lever disposition not located.
WILL_NEEDS: None now; levers (b)/(c) are Will's when PROME presents them.
FOLLOW-UP: WALTER runs the predictive leg by 2026-11-06; lever (a) applied at dispatch from today.
