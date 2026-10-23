# Fire-time flags at the 2026-10-23 19:4x ET boot (prome-06, laptop) — dispositions

Run: `prome_gate.py boot` inside `boot_session.py --run-dir /tmp/prome-boot-6e4cd04f` (gate 19:44 ET); log `checks/04-firetime-owner-routed-flags-persist-.txt`. Delta against `PROME/state/firetime_dispositioned.tsv` = 44 flags: 3 NEW · 41 persisting (dispositioned at the 10/21 and 10/22 records) · 1 baseline row no longer reported.

| Flag | Disposition |
|---|---|
| NEW DEAD POINTER `PROME/WILL_QUEUE.md` — `scripts/routine-requirements.txt` | DONE: PROME's own row 510 (WQ-510, BRENT's routine-preamble install) named a file BRENT's draft would CREATE on install; the path was prospective, never on disk. Reworded to "a new routine-requirements text file under scripts/ (created on install; not on disk yet)" so no path token is parsed. Decision text, options and rec unchanged. |
| NEW DATE DRIFT `AGENTS/REGINALD/STATUS.md` — "12/30" (2026-12-30) | DONE (verified at the artifact, full logic re-read of the line): "Eagle Q4 wall ~$525M (10/27–12/30)" is the END of EGBN's Q4 maturity-wall window from REGINALD's `reports/2026-10-22_EGBN_Q4_maturity_wall.md` — an evidence range, not a scheduled obligation; nothing is owed on 12/30 and no docket row is implied (the Q4-wall grade lives at the Q4 print, ~late Jan 2027, per REGINALD's 10/22 read already in DOCKET L521's context). REGINALD's file, REGINALD's wording; no change asked. |
| NEW DATE DRIFT `AGENTS/LIQUID/STATUS.md` — "1/4" (2027-01-04) | ROUTED to LIQUID (owner) by packet `AGENTS/LIQUID/inbox/2026-10-23_from-PROME_status-fraction-reads-as-a-date.md` (carve-out ①): the text is "Event legs 1/4" in the GATE-LIQ-072 row — one of four legs, the DEWEY table-fraction class of 10/23; no date exists. LIQUID is dark (ListAgents 19:4x ET: no other session); fix at its next touch. |
| 1 baseline row no longer reported | DONE: pruned with `firetime_delta.py --prune` (its disposition is "done: pruned"). |

Accepted into the baseline with `firetime_delta.py --accept --pointer` this record; `PROME/state/firetime_dispositioned.tsv` committed in the same closeout-of-boot commit.
