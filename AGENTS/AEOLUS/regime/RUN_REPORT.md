run_date: 2026-09-28 (pulls 20:00:00–20:00:29 EDT; report written 20:03 EDT)
worker: AEOLUS regime/ (ENSO) domain worker · window covered: AEOLUS dark 2026-09-18 → 2026-09-28

observations_added: 14 rows to `workbook/SERIES.tsv` (8 new weekly cells: Niño-3.4/3/1+2/4 for weeks centred 16SEP and 23SEP 2026; 6 revision rows). 7 rows to `workbook/LOG.tsv`. `DOSSIER.md`: two-clock header (Last real data refresh 2026-09-23 = newest observation week), new pass block, §1 weekly / Niño-1+2 / Niño-4 rows.

---

## FOUR-BASELINE TABLE (as of 2026-09-28; none interchangeable)

| Baseline | Value | Period | Source | New since 9/18? |
|---|---|---|---|---|
| **ONI** | +1.80 | JJA 2026 | `CPC-oni.ascii` (ERSSTv6) | **No.** JAS not posted (expected with the 8 Oct discussion) |
| **RONI** | +1.36 | JJA 2026 | `CPC-RONI.ascii` (ERSSTv6) | **No.** HTTP 200, 920 lines. No 404 |
| **OISST monthly** Niño-3.4 | +2.52 | Aug 2026 | `CPC-sstoi.indices` col 4 | **No.** September not posted |
| **Weekly** Niño-3.4 | **+3.1** (SST 29.7) | week centred 23SEP 2026 | `CPC-wksst9120.for` col 3 | **Yes.** 2 new weeks |

ONI−RONI recomputed (JJA): 1.80 − 1.36 = +0.44. Same as 9/18, so no new derived row.

---

threshold_state:
- ONI vs "strong" ≥1.5: JJA 2026 +1.80 → **+0.30 above**. ONI vs "very strong" ≥2.0: **0.20 below**. AEO-02 is specified on the NDJ season, which has not arrived. Not graded.
- Very-strong probability (CPC-ensodisc, 10 Sep 2026 issue, still current): verbatim *"greater than 90% chance of a very strong event during the Northern Hemisphere fall and winter 2026-27."* Unchanged.
- Historic-event probability (same issue): verbatim *"During the October-December 2026 season, there is a 75% chance of a historic event that would exceed the strength of previous El Niño events dating back to 1950 (+2.5°C or more for a 3-month RONI value)."* **Confirms the 75% on file** (raised from 69% in the 13 Aug issue). Next discussion **8 October 2026**.
- RONI vs historic bar +2.5 (OND): latest RONI JJA +1.36 → **1.14 below**. NOT-FIRED. The bar is an OND forecast target, not a present-state test.
- Weekly trend (wksst9120.for, Niño-3.4): 19AUG 2.6 → 26AUG 2.6 → 02SEP 2.8 (rev.) → 09SEP 2.9 → 16SEP 3.0 → **23SEP 3.1**. **Still rising**: four straight weekly gains of +0.1 to +0.2.

changes:
- **WALTER's "23SEP 29.7 °C, +3.1" is VERIFIED at the primary** (`wksst9120.for`, row `23SEP2026 … 29.7 3.1`).
- Weekly by region, 09SEP → 16SEP → 23SEP (wksst, 1991-2020): Niño-1+2 4.5 → 4.6 → **4.7** · Niño-3 3.7 → 3.8 → **3.9** · Niño-3.4 2.9 → 3.0 → **3.1** · Niño-4 0.9 → 1.0 → **1.1**. All four regions rose in both weeks.
- **Weekly record context. I computed this from the file myself (2,352 weeks, 02SEP1981–23SEP2026) and did not take it from any chart:**
  - Niño-3.4 23SEP2026 +3.1 is **rank 1**. The prior max was **18NOV2015 +3.0**, and 16SEP2026 tied it. Only 3 weeks in the file are ≥3.0.
  - Same calendar week in earlier big events: 23SEP2015 +2.0 · 24SEP1997 +1.8 · 22SEP1982 +1.7 · 20SEP2023 +1.7. That puts 2026 **1.1 above 2015** at this point in the season, and 2015 peaked 8 weeks later.
  - Raw SST 29.7 °C ranks **2nd** (18NOV2015 was 29.8).
  - Niño-3 +3.9 is also a file record (the highest before 2026 was 3.3, Nov 1997). So is Niño-1+2 +4.7 (the highest before 2026 was 4.5, 29JUN1983).
  - ⚠️ **Basis caveat:** this is an **absolute** anomaly on a fixed 1991-2020 baseline, so it does not net out tropical-mean warming. On this same file 1997-98 peaks at only +2.3 (17DEC1997). So "record" is **true on this instrument and not established on RONI**: RONI JJA +1.36 is still below the 2023-24 RONI peak of +1.40.
- **Have observations run ahead of CPC's historic-event threshold? Not demonstrably. Reported, not graded.**
  - The threshold is **+2.5 on a 3-month RONI** (ERSSTv6, relative index). On that instrument the latest reading is JJA +1.36, which is 1.14 below.
  - The weekly absolute Niño-3.4 has been numerically above 2.5 every week since 12AUG (2.6) and is +3.1 now. That is a **different instrument**, and a numeric exceedance there is **not** an exceedance of the RONI bar. No conversion was applied, because the offset is not constant.
  - The nearest like-for-like test is CPC's September RONI outlook for ASO: median 2.07 (25th percentile 1.96, 75th 2.18). It becomes testable when RONI JAS/ASO print (JAS expected about 8 Oct).
- **Revisions on today's vintage** (OISSTv2.1 near-real-time; not errors): 12AUG Niño-1+2 4.0→4.1 · 19AUG Niño-3 3.3→3.2 · 26AUG Niño-3 3.4→3.3 · 26AUG Niño-4 1.0→0.9 · 02SEP Niño-1+2 4.6→4.4 · **02SEP Niño-3.4 2.7→2.8**.
- **Weekly deck (SOURCES ⑥), now "prepared 28 September 2026":**
  - Bullet slide reads Niño-4 0.1 / Niño-3.4 2.2 / Niño-3 3.1 / Niño-1+2 3.9. Against wksst 23SEP (1.1 / 3.1 / 3.9 / 4.7) the deltas are **−1.0 / −0.9 / −0.8 / −0.8**. This is the third consecutive deck with the same near-uniform gap. The basis is still unresolved and the KB-088 ruling stands.
  - The deck restates RONI JJA as "1.4ºC", which is consistent with the file's +1.36.
- **MJO / WWB (deck, qualitative only; no index value; MJO has no registered command):**
  - *"Low-level (850-hPa) westerly wind anomalies were evident from the western to the east-central equatorial Pacific Ocean. Wind anomalies were easterly over the eastern Pacific Ocean."*
  - *"Over the far eastern Pacific Ocean, easterly wind anomalies have periodically emerged."*
  - *"Since late May 2026, anomalous convergence has mostly persisted over the Indian Ocean and Indonesia."*
  - CPC adds: *"Eastward propagation is not necessarily indicative of the Madden-Julian Oscillation (MJO)."* **No discrete westerly wind burst is named.**
- **Subsurface (deck):** 0-300 m heat content *"Positive anomalies increased from late May 2026 to late July 2026. Since then the positive anomalies have remained steady."* Also: *"negative anomalies have strengthened west of the Date Line."* The last downwelling Kelvin wave was initiated in June 2026. This is reported as CPC text. The worker makes no peak call.
- **Newly captured** (CPC probabilistic outlook, dated 10 Sep, carried in the deck): *"El Niño is expected to persist through March-May 2027, with a possible chance (55%) of ENSO-neutral in April-June 2027."*
- **New on 28 Sep** (single-model statement, logged not adopted): *"CFS.v2 ensemble mean … favors El Niño to continue through Northern Hemisphere winter 2026-27."*

proposed_findings (PROPOSALS only; AEOLUS adjudicates):
1. **Weekly Niño-3.4 series record.** `wksst9120.for` week centred 23SEP2026 = +3.1 (OISSTv2.1, 1991-2020). This is the highest of 2,352 weeks since 1981; the prior max was 18NOV2015 +3.0. The value is 1.1 above 2015's same-calendar-week value (+2.0). Qualifier: an absolute baseline, so this is **not** a RONI record (RONI JJA +1.36 < 2023-24 peak +1.40). Source: CPC-wksst9120.for, pulled 2026-09-28.
2. **Observations vs the historic bar are not yet comparable.** The historic bar is +2.5 RONI (OND); the latest RONI is JJA +1.36 (1.14 below). Weekly absolute readings above 2.5 since 12AUG do not test it. First test: RONI JAS about 8 Oct 2026, against CPC's ASO median 2.07. Sources: CPC-RONI.ascii, CPC-roni-outlook (Sept 2026), CPC-wksst9120.for.
3. **Surface/subsurface divergence (CPC text, 28 Sep deck).** Surface Niño-3.4 weekly rose 2.6 → 3.1 from 26AUG to 23SEP. Over the same period 0-300 m heat content has been *"steady"* since late July, and negative subsurface anomalies *"have strengthened west of the Date Line."* Candidate EXPECTED_SIGNAL for peak timing. The mechanism is a hypothesis; only the CPC wording is evidenced. Source: CPC-enso-evolution-pdf 28Sep2026.
4. **55% ENSO-neutral by AMJ 2027** (CPC probabilistic outlook, 10 Sep 2026). This is relevant to any C2/C6 read that extends into spring 2027. Source: CPC-enso-evolution-pdf 28Sep2026 (outlook slide "Updated: 10 September 2026").

gaps:
- **ONI JAS 2026**: not yet posted. `oni.ascii.txt` HTTP 200, last row `JJA 2026 29.09 1.80`. Not an error; expected with or near the 8 Oct discussion.
- **RONI JAS 2026**: not yet posted. `RONI.ascii.txt` **HTTP 200 (size 14,720 B, 920 lines)**, last row `JJA 2026 1.36`. **The 9/11 404 did not recur**, so no re-location was needed and no source was substituted.
- **OISST monthly Sept 2026**: not yet posted. `sstoi.indices` HTTP 200, last row `2026 8`.
- **CPC ENSO Diagnostic Discussion**: HTTP 200, still the **10 September 2026** issue; next is 8 October 2026. No new odds exist to report.
- **MJO index / WWB quantification**: no registered SOURCES.md command. The deck carries qualitative text only (quoted above). Nothing was substituted.
- **IOD / PDO / numeric SOI**: still unregistered (SOURCES.md § UNREGISTERED). Nothing was pulled and nothing was substituted.
- **Vocabulary (housekeeping):** `nino3_weekly` / `nino12_weekly` / `nino4_weekly` are pre-existing SERIES names that are not in AGENT.md's controlled-vocabulary table. They are used here for continuity; none were invented. AEOLUS may want to add them to the table.
- `regime/AGENT.md` appears modified in `git status` (the 9/28 "WHAT TO REPORT" re-cut). **That edit is not this worker's**: I read the file and did not write it. This report follows the re-cut's question list.
- No `pulled_at` stamp is later than the wall clock. The rows are stamped 20:00 ET (SERIES) and 20:02 ET (LOG); `date` read 20:01:26 and 20:02:32 at those writes.
