# HOMER architecture: DAEDALUS read of the outside review (2026-11-25)

**Written:** 2026-11-25 15:17 ET · Will 15:14 ET: read, analyze, give thoughts. Read-only on HOMER (live, homer-2f); nothing sent, no HOMER file edited. Subject: outside review pinned at 55de4ed42e, supplied by Will (Downloads, not committed).

## Verdict

The review's facts about size and placement reproduce. Its main conclusion (weight, not design) is half right: it shows cost, and cites no error caused by weight. The three errors corrected on 11/25 were a partly read report (LESSONS §56), two unsized one-loan highs (THESIS D18) and a live print written into a frozen grade (LESSONS §57). Two were raised from outside HOMER (CATO and WALTER; PROME relaying an outside review).

## Reviewer claims checked

| Claim | Result |
|---|---|
| Charter 42,713 B; BOOT at line 192 of 281; lines 107–151 = 9,482 B | REPRODUCED |
| CATALYSTS 141,316 B, 74 rows, 15 RESOLVED (24,605 B with newlines), servicer row 40,158 B, boot print 16,368 B | REPRODUCED |
| PREDICTIONS sizes; no new forecast 7/24 to 11/05; Brier 0.358 over 4 | REPRODUCED |
| Registry levels match the charter | REPRODUCED by eye, 12 of 12 rows |
| Lines 107–151 are "band derivation history, not levels" | WRONG in part: 5,029 B are live rules (reporting rule, rent-breadth rules, cure comparator, severity-ladder limit, retired-band prohibition, annual-only ratio, basis discipline, GSE pairing). About 4,453 B are derivation. Moving the block as proposed removes binding rules from the boot read |
| FHA 11.74% and PMMS 7.21% each in 7 files | OVERSTATED: the MULTIFAMILY hits are coincidental strings (overall CMBS special servicing 11.74%, row 110; Arbor portfolio yield 7.21%, rows 114 and 117). FHA 6 (one a resolved forecast record), PMMS 6. Existing sales 3.75M is undercounted: THRESHOLDS also carries it |
| 31 HOMER commits on 11/25 | Path-scoped count; 19 are HOMER's, 12 other desks' deliveries into its folder |
| HB-10 2026-11-30 "can never look stale"; set to release date | WRONG: it goes stale 2027-01-15 instead of 2027-01-02, and the file's own rule is data period end, as on its other monthly rows |
| Move 15 RESOLVED rows to archive | UNSAFE as written: rows 28 (PHM), 31 (MTH), 32 (NVR) hold "next print ~late Jan 2027" inside a RESOLVED key, with no successor row in CATALYSTS and none in PROME DOCKET. Boot skips RESOLVED rows, so the dates are invisible today (HOMER's own LESSONS §50). Row 4 (CRL-23) partly covers PHM |
| THESIS should not carry current values | CONFLICTS with frozen §4: §9 must update fired counts at each print |
| Calendar print under 5 KB | NOT REACHABLE as stated: column 2 alone is 4,269 B. Column 1 cut to 80 characters and column 2 to 100 gives about 8.7 KB |
| Closeout steps moved to the top | Does not fix recall; moves them further from use |
| Upkeep share | Own caveat accepted; not re-measured. "No scoreable calls" omits the frozen kill rail, the PMMS and Trepp pre-registrations (9/29, October) |

## Not in the review

1. 40 of 57 LESSONS rows are cut mid-rule ("…"), and the index says to open the cold file before acting on one.
2. The live servicer trigger (classes A to G) sits in a 12.5 KB calendar cell that opens with superseded text, in a 40 KB row over the 32,550 B read budget. Class A fired 8/07 and was found 9/29; it fired 11/16 and REGINALD was told 11/24 (row's own words). Cause not established.
3. STATUS emphasis is saturated: 43 red marks, 49 stars, 213 bold spans; 23 of 72 table lines carry red.
4. Top-end saturation: 4 of 12 bands and 2 of 5 legs at maximum, A2 capped with no upgrade rung. The forecasts are the only instrument that can still register worsening. No change proposed (Will 11/24).
5. Frozen and live text share THESIS; that is what §57 hit.
6. A charter reorder is boot-defining: READS re-attestation is owed and step numbers must not change.

## Recommended order (HOMER's files; nothing done)

1. Roll the three builder rows to their January keys. 2. Give the servicer trigger one clean home (verbatim, no class changed). 3. CLOSEOUT to its own file read at closeout (5,328 B), BOOT up top, step numbers unchanged. 4. Column 1 = next date plus anchor type, history to notes (about 7.7 KB). 5. Finish or shorten the 40 cut lessons. 6. Derivation only (about 4.5 KB) to a reference file, rules stay; Will's word first. 7. Separate frozen grades from live counts in THESIS at the next natural edit. Steps 3, 4 and 6 save about 17.5 KB of about 155 KB (11%). Keep the charter as the home of band levels: the registry is edited every print, so a Will-gated level should not live only there. Skip HB-10; STATUS_COLD, LAST_COMPLETION and the PREDICTIONS essays are tidy-up with no boot saving.

## Limits

One reader; workbook bodies and cold registers not read; housing analysis not judged. FLEET_MAP HOMER row and the profile (trigger 11/20 fired) are stale, owed at PR #11.
