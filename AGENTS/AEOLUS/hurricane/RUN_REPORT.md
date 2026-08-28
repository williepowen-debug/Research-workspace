# AEOLUS · HURRICANE — RUN REPORT

**run_date: 2026-08-27** *(data date 2026-08-27; NHC TWO 800 PM EDT Thu Aug 27 2026; ACE numerator includes bal04 through 2026-08-28 00Z)*
**Refresh pass — AEOLUS dark 6 days (8/21 → 8/27). The Atlantic's 14-day silence ended today: TS Dolly (AL04) formed. Two open jobs from the prior run's ledger both closed.**

---

## observations_added

**11 rows → `workbook/SERIES.tsv`** · **7 rows → `workbook/LOG.tsv`** · **2 rows → `workbook/STORMS.tsv`**

SERIES (new `(date, instrument)` pairs only; no overwrites): `nhc_atlantic_active=1` (Dolly) · `ace=3.4575` · `ace_todate_normal_exclusive=26.72` (new derived row, not in the controlled vocabulary — flagged for AEOLUS) · `ace_todate_normal_inclusive=28.41` (same flag) · `noaa_below_normal_prob=75` / `csu_named_storms=9` / `csu_hurricanes=4` / `csu_major_hurricanes=1` / `csu_ace_forecast=50` — all five **re-verified unchanged**, labelled as such in notes.

STORMS: Dolly (AL04, 8/27, TS 35 kt) · AL92's Caribbean remnant (8/15, recovered from the archive close, dissipated within 6h).

---

## threshold_state
*(value + margin only — a worker does not grade)*

| Instrument | Value 8/27 | Margin | State |
|---|---|---|---|
| **🔴 C1 escalation line — "NHC lights a GULF/FL system"** | **NO Gulf/FL system.** Only active system is TS Dolly, central tropical Atlantic, forecast **dissipated by 72h (~8/30) before reaching the Leewards.** Today's TWO: *"Tropical cyclone formation is not expected during the next 7 days"* (no other invests anywhere) | Not Gulf, Caribbean, FL, or western basin | **NOT FIRED** |
| **ACE vs normal — Yellow ≥134.8** | **3.4575** | **131.3 below Yellow** | **NOT FIRED** |
| ACE — Orange ≥159.4 / Red ≥183.9 + landfall | 3.4575 | 156.0 / 180.4 below | **NOT FIRED** |
| **AEO-01 criterion — season-end ACE <110.3** | 3.4575 season-to-date | **106.8 units of headroom** | *open, resolves 11/30 — AEOLUS grades* |
| AEO-01 second leg — ≤7 hurricanes | **0 Atlantic hurricanes** | 7 of 7 remaining | *open* |
| Reinsurance ROL / cat-loss tally | **NOT RE-PULLED** — carries 8/13 vintage (now 14 days old) | — | **stale, labelled** |

---

## changes  *(since the 8/21 read, with numbers)*

**1. 🔴 The 14-day Atlantic silence ended: TS Dolly (AL04) formed 8/27 1100 AM AST**, central tropical Atlantic (13.6N 38.7W), from Invest AL96. NHC forecasts it to hit increasing SW shear + dry air Friday, degenerate into a tropical wave by Fri/Sat, and be **DISSIPATED by 72h (~8/30 1800Z) — before reaching the Leeward Islands.** Not a Gulf/FL track on the current forecast.

**2. ACE moved for the first time in 14 days: 3.09 → 3.4575 (+0.3675), all from Dolly** (3 synoptic times ≥34 kt so far, all 35 kt TS, still accruing since Dolly remains active).

**3. The ACE-vs-normal RATIO FELL DESPITE the new storm: 16.3% → 12.94% (exclusive convention).** Freshly recomputed to-date normal for Aug 27 = **26.72** (never reused the Aug-21 figure of 18.98). A normal season's to-date-normal climbs **~7.7 ACE units** between Aug 21 and Aug 27 while 2026 added only 0.37 — the seasonal ramp is outrunning the observed activity even with a storm active. Seasonal accrual by Aug 27 = **21.8%** of a normal season (vs 15.48% by Aug 21).

**4. The archive gap (prior run's G1) is CLOSED.** IEM's AFOS text archive (`mesonet.agron.iastate.edu`) verified working, independent of nhc.noaa.gov's own broken JS archive. All 20 TWOAT issuances for 8/14-8/18 retrieved and read (exact commands below). **Confirms: no Gulf/FL system existed at any point in that window.** Also surfaces one system the prior run's ATCF-absence proxy could not see: **AL92's remnant briefly reached the Southeastern Caribbean Sea on 8/15 AM** (near-0% formation odds, explicit shear/dry-air kill text), gone by the next issuance 6 hours later.

**5. Peak-season tell: two more confirming instances recovered (AL94's exact death text, AL92-Caribbean), running tally now FOUR-for-four, plus a live fifth test (Dolly, not yet resolved).**

**6. Both seasonal outlooks + the CSU two-week product RE-VERIFIED UNCHANGED. No CSU two-week issue landed in this 6-day gap** (unlike the 8/13-8/21 gap, which missed one) — schedule confirms next issue is 9/2, six days past this write date.

**7. `csu_ace_forecast` RATIFIED** — name and value (50) both confirmed correctly recorded against CSU's live page.

---

## proposed_findings
*(candidate KB rows — PROPOSALS ONLY, AEOLUS adjudicates)*

**P1 — Dolly is a live, named, currently-active test of the same shear mechanism that killed four prior systems.** NHC Discussion #2 (8/27 500 PM AST) verbatim: *"increasing southwesterly shear due to a central Atlantic upper-level trough, fast forward motion and dry air aloft… Global and regional models all show Dolly degenerating into a strong tropical wave."* Forecast dissipation ~8/30. **Not yet resolved — check at next spawn.**

**P2 — the ACE ratio can fall even with an active storm, and the mechanism is date-relative, not activity-relative.** 3.4575/26.72 = 12.94% is LOWER than 3.09/18.98 = 16.3% six days earlier, because the to-date normal accelerates through peak season faster than a single 35kt TS adds ACE. **This is a genuine, reproducible feature of the accrual curve, not noise** — flagging so it isn't misread as "the season got quieter."

**P3 — the archive gap is closed and the two-archive command works cleanly.** Two-step: `curl "https://mesonet.agron.iastate.edu/api/1/nws/afos/list.json?pil=TWOAT&date=YYYY-MM-DD"` (lists ~4 daily issuances with `product_id`/`text_link`), then `curl "https://mesonet.agron.iastate.edu/api/1/nwstext/<product_id>"` (returns the raw text). Verified against 20/20 issuances 8/14-8/18. **Proposed `SOURCES.md` addition.**

**P4 — the AL92-Caribbean-remnant instance.** 8/15 0800 AM EDT TWO: *"Southeastern Caribbean Sea (AL92): A tropical wave... Development of this system is not expected due to strong upper-level winds and dry air"* — near-0%/near-0%. Dropped from the 200 PM issuance six hours later. **This is a Caribbean presence the 8/21 "eight days of complete silence" framing did not capture** — worth a KB note distinguishing "silence in the Atlantic advisory/best-track record" from "silence in the outlook prose," since they are not the same claim.

**P5 — `csu_ace_forecast` vocabulary entry is ratified correct.** No action needed; CSU's page still reads `50 / Average for 1991-2020: 123`, unchanged since 8/5, matching `SOURCES.md`/`AGENT.md` exactly.

**P6 — both `AGENT.md`'s and `SOURCES.md`'s prior-flagged staleness (ACE prohibition, CSU-cadence-nonexistence claim) are CONFIRMED FIXED** as of this run's read — the 8/21 run's proposed corrections were applied. No further action; noting for the record so this isn't re-flagged.

---

## gaps
*(required output — a reported gap beats a worked-around one)*

**G1 — RESOLVED this run.** See P3 / changes #4.

**G2 — Loss leg not pulled** (Gallagher Re / Munich Re / Aon / Artemis / Guy Carpenter). Now 14 days stale. Commercial publishers on their own schedule; nothing new expected between H1 (~Jul-Aug) and full-year (~Jan). **Deliberately labelled stale rather than backfilled.**

**G3 — the 8/21→8/27 base-rate table (bottom-6/8/10 <90%-of-normal shares) was NOT re-run this session.** DOSSIER §1b carries the 8/21 figures explicitly flagged as that vintage, not recomputed for Aug 27. Out of this run's requested scope; noting so it isn't mistaken for current.

**G4 — 8/20's TWO text was not individually re-fetched.** The IEM archive close covered 8/14-8/18 (the originally flagged gap) plus today's live pull (8/27); 8/19-8/26 were not separately verified via the archive (though ATCF/discussion absence + CSU's 8/19 attestation already cover most of that span per the 8/21 run). Trivial to close with the same command if needed.

**G5 — denominator reconciliation (NOAA median vs AEOLUS mean) still open, not addressed this run.**

---

## sources run this pass

| Command / URL | Result |
|---|---|
| `https://www.nhc.noaa.gov/CurrentStorms.json` | ✅ 4 active (Dolly + 2 E-Pac + 1 C-Pac) → **1 Atlantic** (Dolly) |
| `https://www.nhc.noaa.gov/text/MIATWOAT.shtml` | ✅ TWO 800 PM EDT 8/27 parsed; only Dolly active, formation not expected elsewhere in 7 days |
| `https://ftp.nhc.noaa.gov/atcf/btk/` + `bal01/02/03/042026.dat` | ✅ 4 decks now exist (`bal04` new, modified 2026-08-28 01:04); ACE numerator **3.4575** — Arthur/Bertha/Cristobal legs reproduced exactly, Dolly leg = 0.3675 |
| `https://ftp.nhc.noaa.gov/atcf/dis/al042026.discus.001` + `.002` | ✅ Dolly discussions 1 & 2 read in full — shear/dry-air degeneration forecast, dissipation ~72h |
| `https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2024-040425.txt` | ✅ re-validated: full-season normal 122.58, median 129.25, 14.40/7.20 storms/hurricanes vs NOAA's 14/7. **NEW: to-date normal for Aug 27 computed fresh — 26.72 exclusive / 28.41 inclusive** |
| `https://tropical.colostate.edu/forecasting.html` | ✅ re-verified unchanged: 9/4/1, ACE 50; two-week schedule confirms Aug 19 still latest, next 9/2 |
| `https://www.cpc.ncep.noaa.gov/products/outlooks/hurricane.shtml` | ✅ re-verified unchanged: still 6 Aug 2026 issuance, 75/20/5 |
| `https://mesonet.agron.iastate.edu/api/1/nws/afos/list.json?pil=TWOAT&date=YYYY-MM-DD` (×5, 8/14-8/18) | ✅ **NEW verified archive** — 20/20 issuances listed |
| `https://mesonet.agron.iastate.edu/api/1/nwstext/<product_id>` (×20) | ✅ all 20 fetched and read in full |

*Every URL beyond `SOURCES.md`'s four was either a direct extension of an already-verified command (adding `bal04`, `al042026.discus.*`) or the newly-verified IEM archive (P3). No source was substituted, and nothing was reconstructed from memory.*

---

## ⛔ limits observed

Nothing written outside `AGENTS/AEOLUS/hurricane/`. **No channel scored** (DOSSIER still carries AEOLUS's 8/13 score of 2 🟡, explicitly labelled as AEOLUS's). **No trigger fired** — thresholds reported as value + margin. **No prediction resolved** — AEO-01 reported as headroom. **No packet written, no agent routed to.** **No git commit.** `AGENT.md` and `SOURCES.md` were read and verified but NOT edited by this worker — corrections/additions are proposed in LOG.tsv and DOSSIER.md for AEOLUS to fold in, per the established ownership split. Appends only; `SERIES.tsv` / `STORMS.tsv` / `LOG.tsv` all read before write, no `(date, instrument)` duplicates introduced.
