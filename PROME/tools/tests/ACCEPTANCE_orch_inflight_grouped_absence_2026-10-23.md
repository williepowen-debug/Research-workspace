# ACCEPTANCE — ORCH_INFLIGHT view: group the "NO drained>0" identities under their base desk name (2026-10-23 01:0x ET, prome-e7)

**Defect in its own terms (WALTER packet `PROME/inbox/processed/2026-10-23_from-WALTER_orch-inflight-over-budget-and-homer-backlog.md`, 0b9a90bd5):** `PROME/state/ORCH_INFLIGHT.md` is a WALTER boot step 9b `whole` read and measured 36,178 B at 04:39Z, over the 32,550 B read-cap budget. The section "Desks with a TOUCH row but NO `drained>0` touch inside 30d" lists 517 identities (13,051 B); only 5 are plain desk names, the rest are helper/reader identities of the form `DESK (label)` (ANVIL ×7, ARGUS ×n, PROME-reader ×n …). The list says of itself that it proves nothing about liveness. The file is generated, so only the projection (`scripts/orch_log.py view`) can fix it.

**Acceptance conditions, written before the edit:**
1. The section still names every BASE desk that has a TOUCH row but no drained>0 touch in the window (the text before ` (` in the identity), each once, with ` ×n` when more than one identity collapses into it — so a reader can still see that MIDAS or SAM is in that state.
2. The header carries both counts: identities and base names.
3. `scripts/orch_log.py --selftest` passes unchanged (its drills assert `MIDAS`/`SAM` appear in that section and that cadence rows are not listed there).
4. The regenerated view measures under 32,550 B by `PROME/tools/measure.py` (the sole approved instrument).
5. IN-FLIGHT rows and the last-drained table are byte-identical before/after (the change touches one section only).

**Neighbours (WQ-229 five, considered):** ordinary = AC1–4 · overlap = an identity whose base name is ALSO a plain row (e.g. `ANVIL` and `ANVIL (anvil-0927)`) counts once under ANVIL with ×n — the base name still appears · wrong owner = N/A, the view has no owner cells · missing information = an identity with no ` (` is its own base (unchanged) · concurrent activity = `view` is regenerated under the writer lock by `append`; a desk appending during the edit regenerates with whichever code is on disk — the content differs only in this section's form, never in rows.

**State:** IMPLEMENTED · TESTED (author, selftest + measure) · NOT independently verified (a one-section projection change in a generated view; small self-contained fix per WQ-229 — no reader owed). Disclosed as this session's SECOND process change (PROCESS class, 2 of 5).
