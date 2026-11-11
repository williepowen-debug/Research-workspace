# FERT TRIGGERS.tsv Notes rotation — 2026-11-11 (verbatim)

Rotated under read-cap rotate-tier (TRIGGERS.tsv 28,620 B = 88% of the 32,550 B budget before rotation). Text below is exactly as it stood in the Notes column of `workbook/TRIGGERS.tsv` before the rotation; history only, never current. Each row keeps its newest consumption entry and its standing METHOD / BUILD / DATE / WINDOW entries.

## T1 — Notes entries moved 3 (verbatim, original order)

- CONSUMED 2026-10-28 22:19 ET (Will-directed full session, Opus): no follow-on India tender found ISSUED (WebSearch extended 10/28). AFC w/e 23.10 (pub 10/26): India EXPECTED back with a tender potentially approaching 2 Mt; market expects L1 around $375/mt CFR, implying China netbacks ~$345-350/mt FOB — an expectation, not an offer or award (KB-FERT-098). G2 not gradeable; nitrogen channel DEAD. Next_Check 11/04 = next DTN Wednesday + watch for issuance; on issuance, re-date to the bid-closing date.

- CONSUMED 2026-10-21 08:57 ET (WQ-184 due-row spawn, PROME af287aee, Opus; DOCKET L576 + GATES G5): IPL 1.7 Mt tender OUTCOME reported — India 'secured approximately 410,000 metric tonnes' against 1.7 Mt, Chinese suppliers declining $320-325/mt FOB netbacks [AFC w/e 16.10, pub 10/19, MIRROR, single-sourced]; awarded CFR NOT STATED; INFERRED at/below the L1 counters $352.10 E / $356.25 W /mt CFR (KB-FERT-071) => $244-248 under $600; G2 not gradeable on a stated price; nitrogen channel DEAD (KB-FERT-080). AFC: 'another tender will be required' — Next_Check 10/28 = watch for the follow-on IPL tender and any stated award price (rides T4).

- ROTATED 2026-10-21: 2 older entries moved verbatim to archive/TRIGGERS_notes_rotated_2026-10-21.md (read-cap rotate-tier); ROTATED 2026-10-15: 3 older entries moved verbatim to archive/TRIGGERS_notes_rotated_2026-10-15.md (read-cap rotate-tier); ROTATED 2026-10-07: 2 older entries moved verbatim to archive/TRIGGERS_notes_rotated_2026-10-07.md (read-cap rotate-tier)

## T2 — Notes entries moved 2 (verbatim, original order)

- HISTORICAL CONSUMPTION: CONSUMED 2026-10-26: October edition updated 10/23, PRIMARY. FAH annual-average forecasts 2026 2.3% / 2027 1.0%, down from September 2.4%/1.8%; no fertilizer explanation in summary. Signal NOT FIRING (KB-FERT-083). Release date 10/23 initially asserted from Updated stamp only (verification superseded above), supersedes estimated 10/25. Next_Check 11/25 EST, calendar Error/No results; verify next wake.

- CONSUMED 2026-10-01 (overdue since 9/25): Sep edition 'Updated 9/25/2026' — FAH 2026 +2.4% (1.8-3.0), 2027 +1.8% (-5.0 to 9.2), DOWN from 2.7/2.9 (7/24 edition). Fertilizer / input costs: ZERO mentions (raw-HTML grep). Signal (fertilizer APPEARING) did NOT fire. KB-FERT-049. Next edition ~10/25 [EST].

## T3 — Notes entries moved 1 (verbatim, original order)

- CONSUMED 2026-10-01 (overdue since 9/11): Aug-2026 CUSR0000SAF11 321.3 vs Jul 321.2 = +0.03% m/m SA — G4 line (+0.4%) not approached. KB-FERT-050. ROW NOW ROLLING for the OCTOBER CPI print (T6 holds September, 10/13); Next_Check [EST — verify on the BLS schedule]. ⛔ METHOD: fredgraph.csv failed from this box 10/01 (HTTP/2 INTERNAL_ERROR then hang); use FORGE/tools/market-data/fetch.py fred CUSR0000SAF11 (FRED API) — worked.

## T4 — Notes entries moved 3 (verbatim, original order)

- CONSUMED 2026-10-28 22:17 ET (Will-directed full session, Opus): DTN 10/28 first-party (data wk Oct 19-23) MAP $983 / DAP $939 -> GATE-FERT-G5 NOT FIRED 11 of 11; MAP $17 (+1.73%) under; 12-print pace ~+0.98%/mo MAP, ~1.75 months to the line (KB-FERT-097; GATE_GRADES.md). Slug found on the crops index (fertilizer-prices-continue-climb-6). Next_Check 11/04 = next DTN Wednesday.

- CONSUMED 2026-10-21 08:56 ET (WQ-184 due-row spawn, PROME af287aee): DTN 10/21 first-party (data wk Oct 12-16) MAP $981 / DAP $937 -> GATE-FERT-G5 NOT FIRED 10 of 10; MAP $19 (+1.94%) under; 11-print pace ~+0.99%/mo MAP (KB-FERT-079). Next_Check 10/28 = next DTN Wednesday.

- ROTATED 2026-10-21: 2 older entries moved verbatim to archive/TRIGGERS_notes_rotated_2026-10-21.md (read-cap rotate-tier); ROTATED 2026-10-15: 1 older entry moved verbatim to archive/TRIGGERS_notes_rotated_2026-10-15.md (read-cap rotate-tier); ROTATED 2026-10-07: 4 older entries moved verbatim to archive/TRIGGERS_notes_rotated_2026-10-07.md (read-cap rotate-tier)

## T5 — Notes entries moved 1 (verbatim, original order)

- ROTATED 2026-10-21: 1 older entry moved verbatim to archive/TRIGGERS_notes_rotated_2026-10-21.md (read-cap rotate-tier); ROTATED 2026-10-15: 2 older entries moved verbatim to archive/TRIGGERS_notes_rotated_2026-10-15.md (read-cap rotate-tier)

## T8 — Notes entries moved 3 (verbatim, original order)

- CONSUMED 2026-10-14 23:57 ET (WQ-184 due-row spawn, PROME prome-8e, Opus; GATES G3/G5 + DOCKET L576/L577): NASS Crop Production 10/09 — corn 16.0 billion bu, yield 181.2 bu/acre (+2.7 vs Sep, -5.3 vs 2025); Crop Progress 10/13 — corn 33% harvested vs 39% avg, 56% G/E. FL-FERT-05 stays REFUTED; y/y yield gap UNATTRIBUTED. KB-FERT-074. Next = November Crop Production 2026-11-10 (ESMIS schedule).

- CONSUMED 2026-10-01 (overdue since 9/15): NASS 9/28 release (wk ending 9/27) — corn harvested 18% = 5-yr avg 18%; condition 57% G/E / 17% P/VP vs 66% / 10% a year ago; poor cluster CO/KS/TX/SD (dryness pattern, not linked to fertilizer by any source). FL-FERT-05 stays REFUTED; condition gap logged UNATTRIBUTED. KB-FERT-051. ⛔ A search summary reported 66% G/E — that is last year's column; read the NASS .txt (esmis release-files/<id>/progWWYY.txt; list at esmis.nal.usda.gov/publication/crop-progress). NEXT = USDA October Crop Production / WASDE yield [EST 10/09 — verify].

- ROTATED 2026-10-15: 2 older entries moved verbatim to archive/TRIGGERS_notes_rotated_2026-10-15.md (read-cap rotate-tier)

## T10 — Notes entries moved 3 (verbatim, original order)

- WAKE RE-READ 2026-10-26: Argus-authored IFDC 10/21 (cutoff 10/13) corroborates added rounds, estimates unconfirmed by authorities; not evidence covering post-10/13. No formal gate regrade; 3.3 Mt primary-basis check still owed 11/05. KB-FERT-086.

- RE-READ 2026-10-14 23:57 ET (WQ-184 due-row spawn, PROME prome-8e, Opus; GATES G3/G5 + DOCKET L576/L577; GATES review_by 10/15): GATE-FERT-G3 NOT FIRED both legs, 6th consecutive. Leg 1: no downward revision; export rounds ADDED (4th round >1.5 Mt [Profercy 10/02], no shipment expiry, 3rd-tranche volume still available [AFC 10/12]); MOFCOM price site (reached): regime = quota system + dynamic adjustment, first self-discipline round ~2.0 Mt Jun-Aug. ⚠️ '3.3 Mt' is a MOFCOM-documented IMPORT tariff-rate quota per Fertiaxis 9/24 (MOFCOM doc unreachable) — basis flag on the GATES registration cell, no grade moves. Leg 2: no floor reimposition found; India offers $352-356/mt CFR -> China netback ~$320/mt FOB [AFC], below the standing $430-500 floors = not binding. Dateline trap caught: a 2025-10-21 'China halts exports from Oct 15' item (KB-FERT-077). KB-FERT-072. Next_Check 2026-11-05 = CF Q3 call (CF commentary is a named G3 instrument; rides DOCKET L578).

- ROTATED 2026-10-21: 1 older entry moved verbatim to archive/TRIGGERS_notes_rotated_2026-10-21.md (read-cap rotate-tier)

## T11 — Notes entries moved 3 (verbatim, original order)

- CONSUMED 2026-10-07 21:43 ET (WQ-184 due-row spawn, DOCKET L288): OCTOBER-2026 edition VERIFIED PUBLISHED — CMO page (cache-busted, HTTP 200, 55,918 B) Pink Sheet card reads 'published (10/02/2026) … Next update: November 3, 2026'; hash path unchanged 74e8be41ceb20fa0da750cda2f6b9e4e-0050012026; CMO-Pink-Sheet-October-2026.pdf HTTP 200 (267,820 B application/pdf, in-doc date October 2, 2026); xlsx 'Updated on October 02, 2026', last row 2026M09. Rock Sep $170.0/mt = Aug = Jul ⇒ FERT-11 HIT (KB-FERT-059). Two-source cross-check + zero-free-parameter Q3 validation PASSED; no restatement. The 'third consecutive rise' watch is now a THREE-MONTH RE-PLATEAU at $170.0. Benchmark-label corrections at the primary's own definitions: urea = prill spot FOB MIDDLE EAST since Mar-2022 ('E. Europe' is the series name); KCl = granular spot CFR BRAZIL since Jan-2020 (KB-FERT-060/061). Next_Check 2026-11-03 = the WB's own stated next update, read 10/07. VERIFY-THEN-GRADE protocol unchanged; the 10/02 checks found it absent at 08:31 and 11:13 ET, so it posted later on its stated day.

- CONSUMED 2026-09-05 — September-2026 edition VERIFIED PUBLISHED (in-document date 2026-09-02, data through AUGUST 2026); T11 graded, see KB-FERT-027/028/029. ⚠️ PROTOCOL RE-KEYED 2026-09-05 to VERIFY-THEN-GRADE: step 1 = confirm the edition EXISTS at the CMO page; step 2 = only then grade. A due date does NOT establish that an edition was published — if absent, report SEARCH-NOT-FOUND with the exact URL tried and re-date, never 'unpublished' by inference. ⛔ URL TRAP FOUND 2026-09-05: the thedocs.worldbank.org document-hash rotates (the 2021-era 5d903e848db1d1b83e0ec8f744e55570-0350012021 path now 404s for EVERY month, silently returning a 100,826-byte error page that `file` still calls a PDF). ALWAYS resolve the current hash from https://www.worldbank.org/en/research/commodity-markets first; as of 2026-09-05 it is 74e8be41ceb20fa0da750cda2f6b9e4e-0050012026. That page also states the NEXT UPDATE date — this row's Next_Check now comes from it, not from a calendar guess. Next_Check 2026-10-02 = the WB's own stated next update, read 2026-09-05. CLOCK + VINTAGE TRAP (unchanged, re-confirmed a third time): the file named for month M carries data through M-1. Two-source cross-check PASSED again (PDF August column == xlsx row 2026M08, cell for cell) and the zero-free-parameter Q2 validation PASSED again (PDF 2026 Apr-Jun rock column 154.0 == (152.5+152.5+156.9)/3). ⇢ GRADES prediction FERT-11 (registered 2026-09-05, Resolve_By 2026-10-09) and feeds the EXIT_PROTOCOL phosphate kill leg (rock at or below the PRE-BREAK PLATEAU LEVEL = $152.5/mt × 2 consecutive editions — ⛔ NOT $157; that paraphrase was $4.40 loose and was corrected out of STATUS 2026-09-05).

- ROTATED 2026-10-07: 3 older entries moved verbatim to archive/TRIGGERS_notes_rotated_2026-10-07.md (read-cap rotate-tier)

## T12 — Notes entries moved 5 (verbatim, original order)

- DEEPER PASS 2026-10-28 22:48 ET (Will-directed): Green Markets sulfur posts re-read — still only the 10/23 teaser. Curtailment leg RE-READ (no longer July-vintage): Mosaic WARN filed 10/05 idles South Fort Meade >6 months, 199 separations 12/08 [MIRROR x2; state WARN list 403 to this client] (KB-FERT-108). Gulf October sulfur contracts cut $45-70/t (KB-FERT-109). DISCARD: Argus 'Tampa molten sulphur price rises for 4Q' = 2024-10-02 article (Q4 2024 $116/lt). At 11/04 call: Q4 sulfur cost, South Fort Meade asset type (mine vs chemical plant) and tonnage, any further idles. Next_Check unchanged 11/04

- PARTLY CONSUMED 2026-10-28 22:19 ET (Will-directed full session, Opus): Green Markets sulfur post 10/23 teaser — most Tampa participants reported SETTLING Q4; level and direction behind the wall, UNREAD (KB-FERT-101). ICIS 10/02 expected Q4 below Q3 $705/lt (expectation only). AFC w/e 23.10: some phosphate producers cutting output rather than accept lower prices (KB-FERT-100). Curtailment not re-read at a primary. Next_Check 11/04 = Mosaic Q3 call 11:00 ET (results 11/03 after close, MIRROR-dated, KB-FERT-103) — the first primary likely to state Q4 sulfur cost and plant status.

- CORROBORATION 2026-10-26: Mosaic Q2 10-Q PRIMARY MD&A pp.30-31 supports prior curtailments and Q3 actions; no October plant-state or Q4 settlement confirmation (KB-FERT-084). Next_Check unchanged.

- PARTLY CONSUMED 2026-10-21 08:57 ET (WQ-184 due-row spawn, PROME af287aee): Q4 Tampa molten sulfur still UNSETTLED per the Green Markets 10/16 post (teaser; body walled); AFC w/e 16.10 Brazil MAP $830-850/mt CFR and India DAP $890-905/mt CFR flat two months (KB-FERT-081). Curtailment (Mosaic South Fort Meade) not re-read. Next_Check 10/28.

- ROTATED 2026-10-21: 2 older entries moved verbatim to archive/TRIGGERS_notes_rotated_2026-10-21.md (read-cap rotate-tier); ROTATED 2026-10-15: 2 older entries moved verbatim to archive/TRIGGERS_notes_rotated_2026-10-15.md (read-cap rotate-tier)
