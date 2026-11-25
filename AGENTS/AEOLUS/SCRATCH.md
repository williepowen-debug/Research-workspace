# AEOLUS — SCRATCH (next-session continuity)

**Purpose:** the single "pick up here" file. Read at boot (step 2), append a dated note at closeout (step 4). Keep the latest 3–5 entries; older detail belongs in STATUS history or `memory/YYYY-MM-DD.md`.

---

## ★ STANDING WILL DIRECTIVE (2026-08-03)
**Maintain first-class tracking on MAJOR RIVER water shortages — especially where they affect SHIPPING / TRADE.** Will confirmed C6 water stays inside AEOLUS (no standalone agent for now) AND named the river→navigation→freight nexus as a priority. Coverage split: **C5 = river NAVIGATION→freight** (Rhine, Mississippi/Ohio; the "affects shipping/trade" leg; current score in STATUS); **C6 = water ALLOCATION** (Colorado reservoirs/shortage-tiers/hydropower). Keep a standing scan on the major navigable trade rivers: **Rhine, Mississippi/Ohio, Yangtze, Danube, Paraná** + Panama chokepoint. An empty river read is a gap to close (the #1 guard applies to this watch).
*(August trade lines resolved 8/12 → `archive/SCRATCH_ARCHIVE_2026-11-23_august-trade-lines.md`. No live trade instruction stands here; TRADE.md row 1 = not armed.)*

## 🔴 NEXT SESSION — START HERE (2026-11-25 12:02 ET close, PROME wake on Will's word: card SIG-W-20261125-009 + D:L1256, Claude Code Opus 5.5)

1. **Owed #23: NorCal observed highs 11/25** (predicted peaks ET: Arena Cove 13:12, SF 13:48, Crescent City 13:54, North Spit 14:06). At 08:48 PST the naive projections (predicted high + current residual) were SF ~7.95 vs 8.663, North Spit ~9.86 vs 10.359, Arena Cove ~8.77 vs 8.862, Crescent City ~9.47 vs 10.663 (KB-333). CO-OPS answered normally from 11:47 ET 11/25 (pace 2 s, same `application=research` query, default curl client). Also Wed impact LSRs (KMTR/KEKA) and SoCal Thu morning (SD predicted 7.303 at 09:19 PST).
2. **Florida:** rain ends early Thu; DeLand 6.3 Sat 11/28 vs 6.33 record (unscored ~40%); Sanford 8.5 vs 8.96. CORAL has the hazard read (ef14875b4e). The SE FL watch outcome (to 01:00 ET 11/26) is still mine to read: station totals for the full day.
3. Then the 11/24 block below: 11/27 European low water grade; 11/26 Memphis/CEC/barge.

## (prior) NEXT SESSION — START HERE (2026-11-24 23:39 ET close, session aeolus-desk-agent-2026-11-24, Claude Code Opus 5.5, PROME wake on Will's word)

1. **Wed 11/25 ~14:30 ET: second California tide read** (owed; PROME to register). SF forecast 8.5 ft MLLW at 13:49 ET vs record 8.66 (1983); North Spit 10.0–10.4 vs 10.36 (Jan 2026); Arena Cove vs its new 8.862. ⛔ **CO-OPS datagetter refused this box (HTTP 403) from 23:27 ET 11/24 after my own ~300-request scan.** Test with ONE request; if still 403, use NWPS `api.water.noaa.gov/nwps/v1/gauges/{FTPC1,HBYC1,ANVC1,CECC1}/stageflow` (MLLW, matches CO-OPS to 0.01). Never change the client string. Pace requests (KB-326…329).
2. **11/27:** grade "European low water ended" (7 of 10 at 11/24).
3. Item 0 of the 11/23 block below (alert-vs-measurement pass on the other channels) is still open, and so is the rest of that block, except AEO-17 and the forecasts, which were done 11/24.

### (prior block, 11/23)
#### 🔴 NEXT SESSION — START HERE (2026-11-23 16:59 ET close, session 5869e07f, Claude Code Opus 5.5)

### THE ONE THING
**Colorado is the live channel (Orange 12/02 if unsigned, MWD vote 12/08); Florida and California floods are live now and my California coverage is a gap.**

### FIRST THINGS NEXT SESSION
0. **One pass, channel by channel (promised to Will 11/23): does any other channel read measurements and skip the official warning beside them?** C2 crop-agency and FEWS alerts, C3 NWS cold and PJM alerts, C5 WSV and NWS river notices, C6 Reclamation notices. One check, no new rule.
1. **Mail:** list `inbox/` AND `inbox/WALTER/`; corrections check; receipts.
2. **Floods:** alerts command (`water/SOURCES.md` last section) + gauges; how the 11/24–25 FL watch and 11/24–27 CA tides turned out (KB-318/321); CORAL re-reads 11/24.
2b. **CORAL has the first insured flood figure** (NFIP 1,157 FL claims, $4.84M building paid, data 11/16): STATUS C4 cell "no insured figure" is out of date; fix with the 11/27 B work.
3. **11/26 reads:** Memphis vs −5.1 (full run −6.9 12/10, −7.8 12/21; `/stageflow/forecast`; LEVELS, NO GRADE), SA CEC final, barge print (holiday). Then C5 3 or 2.
4. **12/02:** C6 Orange if unsigned; AEO-01 grade; 12/03 CAP; 12/08 MWD. Run `scripts/c3_winter_grade.py` any session.

### OFFERED TO WILL, NOT ANSWERED OR NOT APPROVED (except the first)
- **DONE 11/23:** WALTER flood-alert check live (its step 7j, f801437643; review 12/02; WALTER sees nothing between sessions). Record-crossing hole FIXED 88ef896074 (word match only: a record stated without the word is missed). Routing now v0.53 (edits 1–4 and part of 5).
- Edit 4 (El Nino/season owner = AEOLUS): Will's word in AEOLUS chat (KB-322); WALTER routing v0.53 live (2714158a44): AEOLUS gets ENSO and season-outlook cards as ACTION. CORAL told. Packet CORAL when an El Nino or season change matters for Florida. `_NETWORK.md` (CARL, TERRY, VULCAN) with PROME.
- Register two winter-rain forecasts (FL DJF wettest third ~80%, CA South Coast ~65%; NCEI climdiv) and one on the Lower Basin signing (no open row covers it).
- Close the California gap (rain, rivers, burn scars, losses). Second reader on Panama (KB-312, AEO-12 55%): give the sources folder, not the conclusion. Short Lake Mead update before 12/08.

### WITH OTHERS
*(Push hold ended: Will "ok go" in AEOLUS chat 18:56 ET 11/23; the report it concerned was already on origin.)*
PROME: one recommendation (SUPERSEDES packet 11/23, KB-325): river-only exit offered, property replacement withdrawn, forecasts MWD 50% and FL rain 75% OFFERED NOT REGISTERED (Will 18:28 ET), WQ-738 count (KB-316: full C2→4 step 1–2 of 36 seasons), diff reads, recipe test row 11/27, artemis.bm on the 12/07 list, `_NETWORK.md` note · AEO-17 re-date (DOCKET 11/24). TERRY: Panama, Memphis, FL/CA floods. CARL: Panama, Memphis. CORAL: rain 17.59 in, tornado, flood watches.

### RULES TO REMEMBER
⛔ **WQ-735: no "Mozilla" request;** default client name, stop on a refusal; do not switch the 10 `SOURCES.md` lines until PROME's packet. Blocked 11/23: FICH (Paraná), CJH (Yangtze timeout), artemis.bm, pslc.org, 8newsnow. WQ-736/737/738 encoded (KB-311/316); neither 4 step has a come-down rule. Owed register: STATUS.

### ⬇️ ROTATED — history lives in `archive/`
- `archive/SCRATCH_ARCHIVE_2026-11-23_11-22-block.md` — the 11/22 pickup block, verbatim.
- `archive/SCRATCH_ARCHIVE_2026-11-22_11-19-block.md` — the 11/19 pickup block, verbatim.
- `archive/SCRATCH_ARCHIVE_2026-11-19_11-11-block.md` — the 11/11 pickup block, verbatim.
- `archive/SCRATCH_ARCHIVE_2026-11-11_11-06-block.md` — the 11/06 pickup block, verbatim.
- `archive/SCRATCH_ARCHIVE_2026-11-06_11-05-closeout-block.md` — the 11/05 closeout pickup block, verbatim.
- `archive/SCRATCH_ARCHIVE_2026-11-05_10-37-block.md` — the 11/05 morning pickup block, verbatim.
- `archive/SCRATCH_ARCHIVE_2026-11-05_10-29-and-10-31-blocks.md` — the 10/31 and 10/29 pickup blocks, verbatim.
- `archive/SCRATCH_ARCHIVE_2026-10-29_10-21-block.md` — the 10/21 PROME catch-up pickup block, verbatim.
- `archive/SCRATCH_ARCHIVE_2026-10-21_10-10-block.md` — the 10/10 El Niño re-point pickup block, verbatim.
- `archive/SCRATCH_ARCHIVE_2026-10-10_10-9-block.md` — the 10/9 landfall-session block, verbatim (two lines in it are superseded — see its banner).
- `archive/SCRATCH_ARCHIVE_2026-10-10_pickup-blocks.md` — the 10/8 (×2) and 9/28 blocks, verbatim.
- `archive/SCRATCH_ARCHIVE_2026-09-28_pickup-blocks.md` — the 9/18 crash-recovery block + the 9/11 drain block, verbatim.
- `archive/SCRATCH_ARCHIVE_2026-08-27_pickup-block.md` · `archive/SCRATCH_ARCHIVE_2026-08-27_superseded-blocks.md` — earlier blocks.
- Recompute any receipt with `tail -n +7 <file> | python3 ../../PROME/tools/measure.py /dev/stdin` (the 8/27 archives use `tail -n +6`); never trust the banner.
