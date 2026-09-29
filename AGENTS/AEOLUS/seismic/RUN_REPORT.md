# AEOLUS · SEISMIC — RUN REPORT (most recent run only)

run_date: 2026-09-28T20:02-04:00 (2026-09-29T00:02Z) · run type: DARK-WINDOW EVENT SCAN (boot rule 6c), gap 2026-08-27 → 2026-09-28

```
observations_added:  4 rows to SERIES.tsv, 1 to LOG.tsv (file created, header + 1 row), 2 to EVENTS.tsv
threshold_state:
  S-1 volcanic climate   | GVP week 9/10-9/16: max plume 2.5 km above crater (Aira); no VEI 5+ and no stratospheric SO2 reported | NOT-FIRED (coverage covers 1 week of the 4.5-week gap)
  S-2 insured cat        | FDSN 8/27-9/28: M7.0+ = 0; largest M6.6 New Caledonia 9/25 (PAGER green) | NOT-FIRED (magnitude leg 0.4 short; no insured-loss estimate)
  S-3 aviation >48h      | no airspace/port closure in the GVP edition; VAAC has no registered command | NOT-EVIDENCED (instrument gap)
  S-4 energy infra       | no named LNG/refining/nuclear/pipeline damage in the pulled sources | NOT-EVIDENCED (no registered instrument)
  S-5 US volcano         | Kilauea WATCH/ORANGE + nvewsThreat "Very High Threat", since 2026-09-07 23:00:41Z, still current 9/28 18:21Z | LETTER MET ON BOTH LEGS. Worker does not fire; AEOLUS grades.
changes:
  - Kilauea ADVISORY/YELLOW -> WATCH/ORANGE on 9/07 (8/13 + 8/27 read: ADVISORY/YELLOW). Began inside the dark window; ungraded for about 21 days.
  - usgs_volcano_elevated 5 -> 4 (Kupreanof no longer listed; Kilauea moved up a level).
  - usgs_significant_30d 12 (8/13) / 13 (8/27 audit) -> 7; usgs_max_mag_30d 7.4 -> 6.6.
  - gvp_weekly_items 23 -> 20 (edition week 9/10-9/16).
proposed_findings:  (PROPOSALS only, AEOLUS adjudicates)
  P1. S-5 two-leg letter satisfied by Kilauea from 2026-09-07 23:00:41Z to at least 2026-09-28 18:21Z.
      Source: USGS volcanoApi/elevated record (alertLevel=WATCH, colorCode=ORANGE, nvewsThreat="Very High Threat",
      alertLevelPrev=ADVISORY, codeChangeDate=2026-09-07 23:00:41). Supporting: GVP weekly 9/10-9/16 "Volcano Alert Level
      remained at Watch ... Aviation Color Code at Orange". GVP cites HVO, so it is the same issuer, not independent.
      Context for grading (fact, not a grade): the HVO 9/28 synopsis reads "Small overflows from the north vent continue
      within Halema'uma'u crater ... no anomalous activity outside of the summit."
  P2. M5.5 Jiangyou, Sichuan, China, 2026-09-03 (us7000tdw6): PAGER ORANGE on the ECONOMIC alert, fatality alert GREEN.
      losses.json point estimate USD 392.7M total economic (not insured); alerts.json bins P(>=$1B)=0.35, P(>=$10B)=0.10.
      Below the S-2 M7.0 leg. Total economic is not insured loss, so the >$10B insured leg is not evidenced.
      Source: USGS losspager product for us7000tdw6 (review-status: automatic).
gaps:
  G1. GVP RSS holds ONE edition (pubDate "Thu, 17 Sep 2026", week 10-16 Sep). Weeks ~8/20-9/9 and 9/17-9/28 cannot be seen
      through the registered command. The 9/24 edition was expected by the feed's own "updated by 2300 UTC every Thursday"
      but was not in the feed at pull. S-1/S-3 coverage of the gap is therefore partial.
  G2. S-3: SOURCES.md names VAAC (Washington VAAC via NOAA/NESDIS) but registers no pull command. Not reconstructed.
  G3. S-4: no registered instrument. Graded only as "nothing in the pulled sources".
  G4. S-1 SO2: https://so2.gsfc.nasa.gov/ resolves (HTTP 200) but has no registered pull command. No SO2 mass read taken.
  G5. USGS significant_month rolls ~30 days (earliest ~8/29), so 8/27-8/28 is not in it. Covered with the FDSN API that
      SOURCES.md §1 lists (query?format=geojson&starttime=2026-08-27&endtime=2026-09-29&minmagnitude=7.0 -> count 0;
      minsig=600 for 8/27-8/30 -> count 0).
  G6. Kilauea HANS detail links in the elevated record (hansApi/notice/DOI-USGS-HVO-2026-09-28T16:49:27+00:00 and
      noticeSection/...16:49:28+00:00) return HTTP 200 with an empty body "[]". The 9/07 change notice text was not
      retrieved. The elevated record's codeChangeDate is the only date source.
  G7. Local tooling, not a source defect: re-parsing the saved GVP file with the shell's grep returned nothing. Evidenced
      cause: in this shell `grep` is a wrapper that runs ugrep with -I, which skips a file argument it reads as binary
      (the feed is ISO-8859). The verbatim SOURCES.md pipe (stdin) works and returned 20 items.
```

## Source resolution (audit method: triggers and sources still resolve)

| Source | Command | HTTP | Result |
|---|---|---|---|
| USGS significant_month.geojson | SOURCES §1 verbatim | 200 | 7 events, generated 2026-09-29 00:00:13Z |
| USGS FDSN event API | SOURCES §1 "Full API" | 200 | used for the full-gap queries below |
| USGS volcanoApi/elevated | SOURCES §2 verbatim (`vName`) | 200 | 4 elevated |
| GVP WeeklyVolcanoRSS (with user-agent) | SOURCES §3 verbatim | 200 | 20 items, pubDate 9/17 |
| NASA SO2 portal | root URL only | 200 | resolves; no registered pull |
| VAAC | none registered | — | not tested (no command to copy) |

## Per-trigger gap queries

| # | Query run | Count | Qualifying event |
|---|---|---|---|
| S-1 | GVP RSS; keyword scan (stratosph / VEI / km above / aviation / airspace / closed) | 20 items; max plume 2.5 km | none |
| S-2 | FDSN `starttime=2026-08-27&endtime=2026-09-29&minmagnitude=7.0` | **0** | none |
| S-2 | FDSN same window, `minmagnitude=6.0` | 6 | none. M6.6 New Caledonia 9/25 · M6.5 Nikolski AK 9/17 (tsunami=1 means a warning was evaluated, not that a wave occurred) · M6.5 Teluknaga Indonesia 9/11 (372 km deep) · M6.4 Kainantu PNG 9/20 · M6.3 Nikolski AK 9/03 (tsunami=1) · M6.2 S. Sandwich 9/02. All PAGER green. |
| S-2 | FDSN same window, `minmagnitude=4.5&alertlevel=yellow / orange / red` | 0 / **1** / 0 | M5.5 Jiangyou China 9/03, economic ORANGE (below M7; insured leg not met) |
| S-3 | GVP scan for closures; VAAC not registered | 0 | none observed (gap G2) |
| S-4 | pulled USGS + GVP content only | 0 | none observed (gap G3) |
| S-5 | volcanoApi/elevated, plus `codeChangeDate` for the whole-gap history | 1 | **Kilauea WATCH/ORANGE @ Very High Threat, 2026-09-07 23:00:41Z → still current 9/28.** Great Sitkin WATCH/ORANGE @ High (unchanged since 2021-07-23; one leg only). |

**Dark-window note (rule 6c):** the S-5 letter was met starting 9/07 during the dark window and is **still met now**, so this is a current state, not only a historical fire. The worker has not fired it, and nothing was routed.
