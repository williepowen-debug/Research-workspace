# BRENT SCRATCH — October 4, 2026 (CATO BU1–BU7 bounded correction; 22:28–22:48 ET)

## CHANGES SINCE LAST SESSION

- CATO supplied four parser/routine counterexamples and challenged two October 4 research inferences. No new market observation arrived during this correction pass.
- IATA's August passenger report was already available: global RPK −0.8% YoY, ASK +0.3%, load factor 85.1%; the contraction was concentrated, with ex-Middle-East RPK +0.6%.

## WHAT I DID THIS SESSION

- Repaired the EIA local parser to identify consolidated tables from their columns, not date spelling. Missing YoY no longer absorbs WoW or trailing historical percentages; legacy April fields remain supported.
- Extended regression coverage for CATO's September 2, September 30, April 29 and missing-YoY/trailing-percentage cases. Full BRENT suite: 70/70 pass; local September 30 report: complete.
- Withdrew the unsupported Riyadh “1% of Saudi crude runs” and small/not-material outage claim. Current state: 126 kb/d nameplate is ~3.8% of EIA's dated 2023 Saudi domestic capacity; capacity is not throughput or confirmed loss, so damage and materiality remain unknown.
- Preserved the verified OPEC+ November hold but removed “90% paper,” “near-zero physical” and zero-expectations-gap precision. EIA `COPS_OPEC` is September-vintage and OPEC-only; it omits Russia, Kazakhstan and Oman and cannot quantify the seven-country counterfactual.
- Ingested the official August IATA release into the demand composite.
- Corrected all four saved routine prompts: one root Git protocol only; Thursday checks later supporting files after an already-recorded core week. Live cloud objects remain unverified because no routine-control tool is exposed.
- Full disposition record: [CATO correction report](audits/2026-10-04_cato-correction/REPORT.md). No threshold, gate, prediction, thesis version or trade state moved. **$0.**

## NEXT SESSION (dated, future-verifiable)

1. **Will UI action:** at `claude.ai/code/routines`, replace all four live prompts with their corrected saved after-images; on Thursday remove Gmail, Claude_Docs, Google_Drive, Quartr, Claude_Code_Remote and Canva; save, reopen and export/re-fetch for comparison.
2. **Mon 10/5:** Aramco November OSPs; seek an Aramco/Saudi/counting source for the Riyadh facility and actual throughput loss. FIRMS/fire evidence alone does not establish an outage.
3. **Tue 10/6:** October STEO. Update the OPEC-only context, but do not treat it as coverage of Russia/Kazakhstan/Oman.
4. **Wed 10/7:** WPSR. Parser is ready; missing YoY must remain a coverage finding.
5. **Routine acceptance remains separate:** Thu 10/8, Fri 10/9, Wed 10/14 and Thu 10/15 after live configuration reconciliation.

## OPEN THREADS / WATCHES

- **Routine state:** saved prompts repaired; live prompt and connector state unresolved pending Will's UI work. First-run behavior untested.
- **OPEC physical effect:** requires a matched participant-level counterfactual; no precision is defensible from `COPS_OPEC` alone.
- **Riyadh:** facility/damage/throughput/duration/yield unknown; no materiality grade.
- **Existing market obligations unchanged:** Mon OSP/broker confirmation; Tue STEO/SPR bids; Wed WPSR; Fri COT and USO $150C sell-or-roll rail.

## POSITION DECISIONS PENDING

- **USO Oct-09 $150C ×1:** recorded open as of 10/1; Will's hand; sell-or-roll by Fri 10/9 15:00 ET. Broker truth after 10/1 remains unverified.
- **VLO 1 sh:** VLO-HELD-01 unchanged; no Riyadh or OPEC inference moves it.
- **USO 37 sh:** hand-managed. **WQ-192 STAND DOWN** remains binding.

## MAIL STATE

- Inbox unchanged; no new packet processed. Two board-log correction receipts supersede the October 4 Riyadh/OPEC overclaims.

## WORKBOOK HEALTH

- Frozen `workbook/KB.tsv` malformed historical rows remain untouched. `LESSONS_INDEX.tsv` substantive reconciliation remains a separate owed item; this bounded pass did not expand into it.
