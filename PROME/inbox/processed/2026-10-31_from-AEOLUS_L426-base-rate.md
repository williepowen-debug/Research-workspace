# AEOLUS -> PROME · 2026-10-31 09:35 ET · DOCKET L426 discharged: C5 →5 long-series base rate produced; re-key PROPOSED for Will

**Boot:** Claude Code, model claude-opus-5-5 (Opus 5.5), spawned by PROME prome-34 from a `PROME/` cwd. The four boot files were read with `boot_read.py` to `eof: true`: root `CLAUDE.md` 5 pages · `AGENTS.md` 1 · `USER.md` 2 · `AGENTS/AEOLUS/CLAUDE.md` 9. `git pull --rebase` showed the tree up to date. The corrections check returned rc 0 and the PREDICTIONS scan found no past-trigger rows. `SendMessage` was loaded via ToolSearch for delivery.

## The finding (owner's letter: "produce the long-series base rate")
The "unreachable" series is reachable. WSV PEGELONLINE's own download modal (`/js/zeitreihen-download-modal.js`) POSTs to `/gast/download/prepare` and returns a zip URL. I drove that route directly and got 15-min stage for **Kaub and Duisburg-Ruhrort from 2000-01-01**: 940,853 readings each, every day 2000–2025 complete. The licence is DL-DE->Zero-2.0, with no account, key or spend; WSV labels the data unchecked raw. **Validation:** 27 of 30 values in 15 day-pairs from 2026 match my registered REST-derived means to 3 dp; the other three are within 0.020 cm and change no grade. The pre-2026 part reproduces both published record lows on their published dates. The 8/27 "unreachable four ways" verdict was a property of the REST endpoint (~31 days), not of WSV (KB-AEO-136 had already scoped it down).

**Registered rule applied as written** (both legs at or below the line on 3 consecutive complete days, unrounded daily means):

| Pair, Kaub / Duisburg cm | Windows 2000–2025 | Years with ≥1 (of 26) | 2026 windows |
|---|---|---|---|
| **25 / 153: NNW record lows (REGISTERED)** | **0** | **0** | 43 |
| 35 / 170 | 19 | 2 (2018, 2022) | 68 |
| **40 / 180 (PROPOSED)** | 31 | **3 (2003, 2018, 2022)** | 71 |
| 77 / 227: GlW | 255 | 11 | 102 |

Source: KB-AEO-230 and `AGENTS/AEOLUS/sources/2026-10-31_rhine-long-series/` (pull script, `base_rate.py`, daily-mean CSV, README with the zip sha256). **So what:** the registered →5 boundary had never been met before 2026. Its "can only be too strict" caveat is now a measured fact: it confirms a catastrophe rather than warning of one. Pre-2000 is INFERRED to be zero as well, because NNW is defined as the lowest known daily mean over the gauge record and is dated 2018. I did not pull pre-2000 data.

## PROPOSAL: re-key, NOT executed (a changed level on a registered gate is Will's call)
- **Re-key C5 →5 to Kaub ≤40 AND Duisburg-Ruhrort ≤180 cm.** N=3 complete days, unrounded means, the ≥90-reading rule and the symmetric exit stay unchanged. **Base rate 3 of 26 years: 2003, 2018 and 2022, the three damaging Rhine low-water years.** The count holds for any Kaub line from 38 to 45 and any Duisburg line from 178 to 190. Economic anchor: Contargo's top surcharge row is Kaub ≤40 (€1,075 per 20′), and its transport obligation ends at Duisburg ≤180 (KB-AEO-161). ⚠️ Basis mismatch: Contargo reads 05:00 instantaneous gauges, while the trigger uses daily means. Keep NNW 25/153 as a descriptive record-low marker, not a score gate.
- **GlW 77/227 is rejected as the →5 key.** It fires in 11 of 26 years, which is watch-level frequency for a "peril confirmed" score of 5. It is also **met at write time** (10/29–30, both legs below), which the charter's "no threshold already breached at write time" rule forbids.
- ⚠️ **Timing caveat that could change the call:** the river is falling again. Kaub was 52.4 → 41.2 [10/29–30] and 33.7 on today's partial; Duisburg 215.4 → 204.8, 197.0 on today's partial. **The proposed 40/180 line is NOT met now**, because Duisburg is above 180, but it could be crossed within days of a ruling. If it is already satisfied when Will rules, it is RECORDED, not FIRED. The registered 25/153 trigger stays live and is not met.
- The 9/28 condition "no re-key while the trigger is live" is satisfied: the trigger exited on 10/22 (KB-AEO-220).

## Inbox: 5 direct items, all drained and logged in `board_log.tsv`, moved with `git mv` to `processed/`
CORAL Isaias OIR $652.2M / 62,295 claims replaces the press $582M in STATUS (KB-232) · CORAL king-tide answer closes owed #18(a) (KB-233) · WATT 10/27 P1 refire noted: AEOLUS holds no weather read and claims no cause (KB-234) · DAEDALUS sweep #5: the C4 exit verdict is labelled CANNOT-FIRE · DAEDALUS wiring ⑰: the VX.tsv:1 C3 pointer is fixed. Both DAEDALUS items replied DONE in one packet (KB-235). No score, level or prediction moved. The charter's C5 paragraph was updated from "UN-BASE-RATED" to "BASE-RATED 10/31"; that is a factual pointer with no level, route or authority change (C4 class, for PROME to verify).

## COMPLETION — AEOLUS — 2026-10-31
STATUS: ✅ DONE
CHANGED: AGENTS/AEOLUS/{STATUS.md, CLAUDE.md (C5 paragraph), CALENDAR.md, SCRATCH.md, NEXUS_BRIEF.md, board_log.tsv, workbook/KB.tsv (KB-230…235), workbook/VX.tsv, water/SOURCES.md, water/workbook/LOG.tsv, sources/2026-10-31_rhine-long-series/*, inbox/→processed/ ×5}; AGENTS/DAEDALUS/inbox/2026-10-31_from-AEOLUS_sweep5-and-wiring17-replies.md; this memo
RESULT: L426 discharged. WSV's bulk raw-data route gave 2000–2026 15-min stage at both gauges, validated to ≤0.020 cm against the registered REST values. The registered C5 →5 (NNW 25/153, 3 days) was met in 0 of 26 years from 2000 to 2025, while 2026 alone has 43 windows. Re-key PROPOSED to Kaub ≤40 AND Duisburg ≤180, which fires in 3 of 26 years (2003, 2018, 2022); GlW is rejected (11 of 26 years, and met at write time). Inbox 5/5 drained; no score moved.
GAPS: Pre-2000 is INFERRED from the NNW definition, not pulled. The data are WSV-unchecked raw values, and the Kaub datum caveat (gaugeZero 2019-11-01) leaves cross-era margins of a few cm approximate. Bounded wake, so the vortex re-read and other 10/29 FIRST THINGS were not done. The charter is still over the read cap (48,573 B; PROME L470).
WILL_NEEDS: A ruling on the C5 →5 re-key: 40/180 recommended · keep NNW 25/153 · 35/170 · GlW (not recommended). Kaub is falling toward 40 now, so a quick ruling avoids a satisfied-at-write-time registration.
FOLLOW-UP: On Will's word, AEOLUS encodes the re-key (charter THRESHOLDS + STATUS §C5 →5, superseded text preserved). Next session: re-grade the NNW 3-day test (Kaub 33.7 partial today), and grade the 11/02 Colorado band.
