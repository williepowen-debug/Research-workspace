# Domain-state report — CATO review, September 25, 2026

## Disposition and scope

Will asked for thoughts on PROME's domain-state report and pasted its spoken summary. Reviewed `PROME/reports/2026-09-25_domain-state-report.md` at `ebe0c906a47b0152f057f6ac78309f82d8178f33`, against selected owner records. Starting tree and index clean. This is a bounded evidence/inference and decision-summary review, not an independent market-data refresh, broker reconciliation, validation of every domain, or full FORUM-7 audit. Figures below describe dated repository claims, not current prices.

**Verdict:** useful domain map, but the opening and portfolio conclusions overstate what the supporting records establish. Recommend a bounded correction using existing owner work, then the already-scheduled grades. No new research, launch, capital ruling or publication follows from this review. No owner edits or messages sent. All findings below remain recommendations, not implemented repairs.

## What holds up

- HENRY's matched-date table supports the report's arithmetic: September 22–24 nominal 10Y +22bp, real +22, breakeven unchanged; distant SOFR contracts moved much more than the immediate meeting. Its interpretation section explicitly says distant futures carry risk premium and the two-day burst is not established as pure path. Source: `AGENTS/HENRY/research/2026-09-25_rates-move-and-hike-alignment.md`, table and “Preferred interpretation.”
- Credit level versus pace is usefully separated. LIQUID's current grade is continued bottom-rung widening at an ordinary pace, without established broadening; the short historical percentile window is disclosed. Funding conclusions name material unobserved channels.
- RQ8's withdrawn forward-volatility claim stays withdrawn. The corrected ten-event sample does not establish a forward VIX signal either way. Its failure supplies no affirmative assurance about future equity volatility.
- FORUM-7 freezes an interpretation rule for data not yet published. Its model-conditional classification and historical model frequencies should not be promoted to causal proof or probabilities of this episode. The inspected letter has intermediate and missing-data branches omitted from the brief; this review does not validate its design.

## Findings

### DS1 — MEDIUM: headline turns unestablished mechanisms into absence

Report line 6 says everything downstream is “a same-day co-move, not a transmission,” and the yen moved “with no intervention.” Its own credit heading says transmission unproven; Japan's detailed paragraph says no intervention **confirmed**. The mortgage paragraph also attributes its rise to Treasury yields, which makes the blanket dismissal of all downstream transmission particularly unhelpful. A contemporaneous observation alone does not adjudicate causality in either direction.

**Consequence:** the opening can reassure more strongly than the evidence or domain paragraphs permit. **Correction/closure:** in the report opening and spoken summary, say broader cross-market stress transmission has not been established; distinguish that from observed borrowing-cost repricing. Preserve “no intervention confirmed”; remove “unopposed” unless supported. Maintain the distinction between real/breakeven decomposition and path/premium inference. Do not reopen earlier accepted review rounds automatically; this finding concerns this new report.

### DS2 — HIGH: current whole-book claims exceed the position and risk evidence

Report lines 6, 53 and 59 call the book unchanged/defined-risk, its only live line VLO, net long duration through GLD, and one Mideast bet with a single falsifier. The report does disclose WQ-274, but that caveat does not establish those affirmative claims.

- Its own list has six Fidelity option lines, two Robinhood option lines and six stock lines: **14 held lines**, plus two staged VLO shares. The spoken “thirteen” disagrees. This is an internal count, not certification of current holdings.
- TERRY's September 24 STATUS retains TLT harvest/expiry and WAL management, alongside VLO. “Only live line” needs narrowing to the particular pending staging action. The held VLO share has no exit rule in `FORGE/STATUS.md:99`; the staged-share stand-down is not an exit instruction for it.
- The original cited concentration assessment is `AGENTS/TERRY/outbox/delivered/2026-07-16_to-PROME_try-fire-004-arm-packet.md` §9: a July rates-short/energy thesis and July holdings. TERRY's `setups/FLOW-TRIGGER_duration-TLT-put.md:298` later qualifies its concentration implication after a rates-mechanism relabel. Neither supplies an updated common falsifier for every line in the September list.
- “Net long duration through GLD” traces to that TLT card's **September 11** delta/beta comparison (line 279), not a refreshed whole-book risk calculation. The report itself says MIDAS last read September 11.

**Consequence:** the operator could mistake an unreconciled position mirror and old thesis grouping for current aggregate exposure and complete management coverage. **Correction/closure:** retain WQ-274 prominently; correct the count; name existing live management rules; scope or date the concentration and duration claims. Do not use “defined-risk” as a blanket assurance without specifying what risk is bounded. Resolve current-book truth in the existing reconciliation workstream, not by assuming this review certifies it.

### DS3 — MEDIUM: completed gamma measurement is presented as still owed

Report line 29 says the last published board was September 21 intraday. `AGENTS/HENRY/STATUS.md` §GEX records a **September 24 close remeasurement**: spot inside the 7,702–7,707 flip band, opposite signs across horizons, near-zero estimated net gamma, walls not publishable; next refresh September 25 close. The model assumptions and unmeasured September 21–23 intervening path remain disclosed.

**Consequence:** “not measured” replaces an existing, informative but indeterminate measurement. **Correction/closure:** carry the September 24 finding and its limits in the report/summary; retain today's refresh. Do not assert a positive or negative sign or certify HENRY's model from this read.

### DS4 — MEDIUM: distance to HY threshold omits the action conditions

Report line 18 and spoken summary say HY re-arm is seven basis points away. `PROME/ACTIVE_DECISIONS.md`'s credit-watch row requires sustained readings (three closes); LIQUID's STATUS and `workbook/KILL_MEMO_HY_OAS_260.md` distinguish the index half from the conjunctive wrapper condition. The wrapper half remains NOT ARMED; X1 and sizing remain CLOSED. A single level cross does not authorize deployment.

**Correction/closure:** label seven basis points as distance to the index threshold, carry the sustain condition, and state that the separate wrapper condition still blocks sizing. This does not change any gate.

### DS5 — MEDIUM: checkpoint and terminal expiry are conflated

Report line 56 makes September 28 the v5 death date; spoken summary calls the re-pin deadline Sunday. **September 28 is Monday.** `PROME/DOCKET.tsv:299` and ORACLE STATUS distinguish that roll/checkpoint from death if no successor exists by the September market's October 1 close. Exact venue closing timestamp/timezone was not independently reconciled here.

**Correction/closure:** distinguish the September 28 task from the terminal market close; carry the owner's precise timestamp before using it operationally. No substitute strike without Will's decision.

### DS6 — LOW: spoken chronology and estimate qualification

Spoken summary and report opening date the $0.36 VLO buffer to Wednesday; HENRY's basis report and TERRY STATUS date it **Thursday September 24**, tier-3 settlement-window **estimate**, provisional pending the finalized dated row. The full energy paragraph correctly labels the estimate and UNKNOWN band; the opening should preserve that qualification. Spoken CRMT summary says Wednesday; the full report correctly dates the third bridge endpoint September 24 and calls the filing unread.

**Correction/closure:** use calendar dates and label the VLO estimate in the opening; retain CRMT's unread status without asserting termination or renewal. No new data pull needed to fix these discrepancies.

## Recommended operator response and limits

Retain the domain report after a bounded summary correction. Prioritize the live portfolio-management and scheduled observation work already assigned; don't use this report to add another forum. The important synthesis is a sharp rates repricing, continued lower-quality credit weakness, and no established broad stress transmission in the measured channels. The important operational gap is a current, reconciled book with clearly scoped management conditions.

Checks: read full report; compared selected HENRY, LIQUID, TERRY, ORACLE, FORGE and PROME source records; checked count and calendar arithmetic. Orphan advisory and diff whitespace check clean. Weekday advisory flagged the quoted erroneous Sunday next to its explicit Monday correction (DS5); inspected, not an actual date assertion to change. No code changed, tests needed or run, external facts certified, live trades inspected, owners contacted, or hosted output checked. No financial action proposed. Resume: orient and await Will; findings do not authorize a correction campaign.
