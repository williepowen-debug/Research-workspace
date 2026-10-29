# AEOLUS · SEISMIC — RUN REPORT (most recent run only)

run_date: 2026-10-29T07:44-04:00 (2026-10-29T11:44Z) · run type: GAP SCAN 2026-09-28 → 2026-10-29 + owed #8 proposals (S-5 re-spec, S-2 AND/OR)

```
observations_added:  3 rows to SERIES.tsv, 3 to LOG.tsv, 3 to EVENTS.tsv
threshold_state:
  S-1 volcanic climate | GVP RSS returned HTTP 403 (2 tries); no SO2 read registered | NOT-EVIDENCED (no coverage this run)
  S-2 insured cat      | M7+ in gap = 2: M7.7 Panama 10/09 (Panama City 207 km), M7.0 Nagqu China 10/22 (Nagqu 191 km);
                       | no insured-loss estimate in pulled sources; PAGER total-economic point est USD 369M / 414M
                       | NOT-FIRED on the table (OR) reading and on the prose (AND) reading
  S-3 aviation >48h    | no VAAC command registered; GVP down | NOT-EVIDENCED (instrument gap)
  S-4 energy infra     | no named LNG/refining/nuclear/pipeline asset in pulled USGS content | NOT-EVIDENCED (no instrument)
  S-5 US volcano       | Kilauea ADVISORY/YELLOW @ Very High Threat since 2026-10-17 19:59:31Z; Great Sitkin WATCH/ORANGE @ High
                       | NOT met now. Letter held 2026-09-07 23:00:41Z -> 2026-10-17 19:59:31Z (39.87 d), then exited.
changes:
  - Kilauea WATCH/ORANGE -> ADVISORY/YELLOW on 2026-10-17 19:59:31Z (9/28 read: WATCH/ORANGE). HVO 10/28: "remains paused
    following episode 55 on October 17. The forecast for episode 56 fountaining has been pushed to Nov. 1-7, 2026."
  - usgs_significant_30d 7 -> 18; usgs_max_mag_30d 6.6 -> 7.7; M7+ in window 0 -> 2.
  - usgs_volcano_elevated 4 -> 4 (same four volcanoes; Kilauea down one level, now 1 WATCH + 3 ADVISORY).
  - gvp_weekly_items: no new row (pull failed, see G1).
proposed_findings:  (PROPOSALS only, AEOLUS adjudicates)
  P1. S-5 historical span, for rule-6c recording: both legs met 2026-09-07 23:00:41Z -> 2026-10-17 19:59:31Z (39.87 d).
      Source: USGS volcanoApi/elevated, Kilauea record pulled 2026-10-29 10:03Z: alertLevel=ADVISORY, colorCode=YELLOW,
      alertLevelPrev=WATCH, colorCodePrev=ORANGE, codeChangeDate=2026-10-17 19:59:31, nvewsThreat="Very High Threat".
      Onset date is from the 9/28 pull of the same record.
  P2. Two M7+ in the gap, both below S-2 on both readings (source: USGS event + losspager products):
      - M7.7 us6000u18k, 2026-10-09 17:56Z, 12 km WSW of Pitaloza Arriba, Panama, depth 12.6 km. PAGER economic ORANGE,
        fatality YELLOW. losses.json total economic USD 369,119,185 (Panama 369.1M). alerts.json P(>=USD 1B)=0.345,
        P(>=USD 10B)=0.093. These are TOTAL ECONOMIC, not insured. Panama City 207 km (modelled MMI 4.85), Colon 219 km;
        within 100 km: 23 PAGER cities, 207k people total, largest Aguadulce 51.7k. Aftershocks M6.6/6.1/6.0/5.8, all yellow.
        Context only, not a link: the PAGER cities file models MMI 5.14 at Balboa Heights and 4.71 at Colon (canal ends).
        That is a model output, not an observation. Registered sources carry no canal-operations data, so no disruption is
        claimed. Panama is a C5 geography, so AEOLUS may want to look; the worker does not route.
      - M7.0 us6000u43g, 2026-10-22 14:33Z, 191 km ENE of Nagqu, China, depth 18 km. PAGER economic ORANGE, fatality YELLOW.
        Total economic USD 414,408,661; P(>=USD 1B)=0.362, P(>=USD 10B)=0.101. Nagqu 191 km, Lhasa 392 km. felt=8.
  P3. OWED #8(a) - S-5 RE-SPEC (draft).
      Current wording (README L51, verbatim): "USGS alert to **WARNING/RED**, or **WATCH/ORANGE** at a **Very High Threat**
      volcano". Route: "log + watch".
      What is wrong with it:
       1. The slash fuses two independent scales. SOURCES §2 says "two independent scales - quote both", and the API has
          separate alertLevel and colorCode fields. The letter does not say whether WATCH/RED or WARNING/ORANGE qualify,
          or whether "WARNING/RED" means both or either. Kilauea 9/07 matched both, so the gap has not been tested yet.
       2. It has no consequence leg. README's own discriminator says an event routes here "only with a dated instrument and
          a priced or physical consequence". S-5 tests alert state only. The one fire so far (Kilauea, 39.87 d) was
          summit-confined: HVO 9/28 "no anomalous activity outside of the summit". It had no aviation or port impact
          in the pulled sources.
       3. No exit or re-fire rule. The exit is implicitly the test failing, but nothing says whether a re-raise is a new
          fire. That matters because README promotes the folder to C7 on ">=3 fires in ~6 months". Episode 56 is forecast
          for Nov 1-7.
       4. Base rate unknown, and KB-AEO-160 overstates what is known. KB-160 says Kilauea "toggles ORANGE routinely".
          Evidence from this folder: Kilauea was ADVISORY/YELLOW on 8/13 and 8/27 while the same episodic eruption was
          running, and there has been one WATCH/ORANGE span (9/07-10/17). That is n=1, not "routinely". Whether episodes
          re-raise the alert is a HYPOTHESIS until the HVO notice history is pulled (HANS detail links returned "[]" on
          9/28, see G4).
       5. The name says "escalation" but the letter is a state. A Very High Threat volcano parked at WATCH/ORANGE would
          "fire" continuously. Great Sitkin has been WATCH/ORANGE since 2021-07-23 (at High Threat, so it does not qualify).
      Proposed falsifiable version (all fields from volcanoApi/elevated, read separately, never as a slash pair):
       S-5a STATE (LOG ONLY, never counted as a fire, never toward C7):
            nvewsThreat = "Very High Threat" AND (alertLevel in {WATCH, WARNING} OR colorCode in {ORANGE, RED});
            or colorCode = RED or alertLevel = WARNING at any threat level.
            Onset = codeChangeDate. Exit = the condition is false on the current record.
       S-5b FIRE: S-5a is true AND at least one dated consequence instrument, each with its own registered source:
            (i) a VAAC ash advisory for that volcano, plus an FAA airspace restriction or an airport closure >24 h
                (VAAC/FAA commands need registering first; G2);
            (ii) an issuer (HVO/AVO) notice reporting activity outside the summit crater or a lava flow/ash fall toward
                named infrastructure or population;
            (iii) an evacuation order.
            Exit = S-5a exits, or no consequence instrument is active for 7 days.
       Re-fire: a re-entry within 30 days of an exit is the SAME episode. It counts once toward C7.
       Before adopting: pull the HVO/AVO alert-change history to base-rate S-5a, and pick whether High Threat volcanoes
       join S-5a. Neither is done here.
  P4. OWED #8(b) - S-2 AND/OR discrepancy. Verbatim wordings found:
       - README.md L48 (formal table): "**M7.0+** onshore within ~100 km of a major insured urban zone, **or** any event
         with a credible **>$10B insured** estimate"
       - AGENT.md L66 (table): "M7.0+ within ~100 km of a major insured urban zone, **or** credible >$10B insured"
         (this copy drops "onshore" and "any event", which is drift)
       - AGENT.md L55 and SOURCES.md L30 (prose): "S-2 needs magnitude **AND** proximity to an insured/populated zone
         **AND** a loss estimate."
       - README prose (discriminator, verbatim): "an event routes here **only with a dated instrument and a priced or
         physical consequence.** Magnitude alone is not a signal."
      Correction to the registered framing: the AND3 wording is NOT in README prose. It is in AGENT.md L55 and SOURCES.md
      L30. README is internally consistent with OR.
      Reading consistent with the rest of the charter: OR (the table). Reasons:
       1. The AND3 line contradicts its own example. It says "an M6.5 under a city ... is the routable event". An M6.5
          fails M7.0+, so it can route only through the stand-alone ">$10B insured" leg, which only exists under OR.
       2. Every grading so far used OR: DOSSIER 8/27 (Colombia/Indonesia legs tested separately), RUN_REPORT 9/28
          ("magnitude leg 0.4 short; no insured-loss estimate"), and SAM 8/14 concurrence ("M7.0+ near a major insured
          zone **or** a credible >$10B insured estimate").
       3. A sibling rule treats a single >$10B insured cat as sufficient on its own: wildfire/README L54, C4 upgrade
          "carrier insolvency OR a single >$10B insured cat".
      What the AND line gets right: leg A (M7.0+ within ~100 km) can fire on magnitude plus location alone, which
      README's "magnitude alone is not a signal" rejects. Leg A also leaves "major insured urban zone", "onshore" and
      "credible" undefined.
      Proposed: keep OR. Replace AGENT.md L55 and SOURCES.md L30 with a pointer to the README row. Tighten leg A to
      "M7.0+ AND PAGER economic alert >= ORANGE AND a named metro area (AEOLUS list) within 100 km of the epicentre".
      Define leg B as "low end of a named cat-modeler or reinsurer insured-loss estimate >= USD 10B". Also restore
      "onshore"/"any event" in the AGENT.md table, or drop "onshore" from both. Owner's choice; worker grades nothing.
gaps:
  G1. GVP WeeklyVolcanoRSS (SOURCES §3 verbatim, with user-agent): HTTP 403 at 2026-10-29 10:04Z and again 10:04:25Z.
      Body <title>: "Smithsonian site temporarily unavailable". Headers: server: cloudflare, cf-ray a5215af7bf165d37-MIA.
      Cause NOT determined. The page text claims a site-side outage; a block on this box's IP is an untested alternative.
      No substitute source used. S-1/S-3 global coverage for the gap = none.
  G2. S-3: VAAC still has no registered pull command (named in SOURCES §3 only). Not reconstructed.
  G3. S-4: no registered instrument; graded only as "nothing in the pulled sources".
  G4. S-1 SO2: https://so2.gsfc.nasa.gov/ resolves (HTTP 200) but has no registered pull command; no SO2 read taken.
      HVO alert-change history (needed for the P3 base rate) also has no registered command; not pulled.
```

## Source resolution (audit: do the sources still resolve?)

| Source | Command | HTTP | Result |
|---|---|---|---|
| USGS significant_month.geojson | SOURCES §1 verbatim | 200 | 18 events, generated 2026-10-29 04:27:41Z |
| USGS FDSN event API | SOURCES §1 "Full API" | 200 | gap queries below + eventid lookups |
| USGS losspager products | linked from the FDSN event record | 200 | alerts/losses/cities/comments for both M7+ |
| USGS volcanoApi/elevated | SOURCES §2 verbatim (`vName`) | 200 | 4 elevated |
| GVP WeeklyVolcanoRSS | SOURCES §3 verbatim, user-agent | **403** | "Smithsonian site temporarily unavailable" (G1) |
| NASA SO2 portal | root URL only | 200 | resolves; no registered pull |
| VAAC | none registered | — | not tested |

## Gap queries (FDSN `starttime=2026-09-28&endtime=2026-10-30`)

| Query | Count | Events |
|---|---|---|
| minmagnitude=7.0 | **2** | M7.7 Panama 10/09 (orange) · M7.0 Nagqu China 10/22 (orange) |
| minmagnitude=6.5 | 8 | + M6.6 Panama 10/09 (yellow, tsunami=1) · M6.7 / M6.8 Mid-Atlantic Ridge 10/13 · M6.9 Ozernovskiy Russia 10/16 · M6.9 Vanuatu 10/24 (tsunami=1) · M6.5 Bonin Is. 10/25 (tsunami=1). All except the M7s are green or yellow. tsunami=1 means a warning was evaluated, not that a wave occurred. |
| alertlevel=yellow | 5 | Panama aftershocks ×4 · M5.7 Khuzdar Pakistan 10/17 |
| alertlevel=orange | 2 | the two M7s |
| alertlevel=red | 0 | — |
