# AEOLUS · REGIME DOSSIER ARCHIVE — 10/09 pass, Sept RONI table, §6 9/17 detail, closed/stale open questions

**Rotated 2026-10-29 from `AGENTS/AEOLUS/regime/DOSSIER.md` (31,018 → 22,772 B; READ_CAP rule 5, rotate tier 95% → <70%), VERBATIM, in 12 pieces.** Each piece carries one AEOLUS-added `### Piece N` header line naming its source lines (line numbers are those at the moment of cut, pieces 1–6 against the 31,018 B file). Superseded, not deleted.
**Obligation census:** nothing open is lost — 10/09 facts = KB-AEO-181 · Sept RONI curve superseded by the October table (§1b) · 9/17 DJF detail superseded by the §6 15 Oct diff · Q1 closed · Q5 adopted as KB-181 · Q2/Q3/Q6/Q7 remain as pointer lines in the dossier.
**Receipt — body only, excluding this 6-line banner: 10623 B · crc32 3572056773.**
**Reproduce:** `tail -n +7 archive/REGIME_DOSSIER_ARCHIVE_2026-10-29_10-09-pass-sep-table-sec6-closedQs.md | python3 ../../PROME/tools/measure.py /dev/stdin` (from `AGENTS/AEOLUS/`).
### Piece 1 — regime/DOSSIER.md lines 15–21 as of 2026-10-29 (verbatim)
> **2026-10-09 — worker pass (the 8 Oct Discussion, unread by AEOLUS until now). All four registered instruments plus the Discussion re-printed.**
> 1. 🔴 **The Discussion's "+2.1 °C Niño-3.4" is a RELATIVE MONTHLY index, not a weekly reading, and there was no drop.** Text: *"Most Niño indices increased in the past month, reaching +2.1°C in Niño-3.4, +3.0°C in Niño-3, and +3.9°C in Niño-1+2 [Fig. 2]."* Fig. 2's caption, verbatim: *"relative sea surface temperature (SST) anomalies … minus tropical mean (20°N-20°S). The relative indices are re-scaled to match the variance of traditional indices. Anomalies are departures from the 1991-2020 base period monthly means. Data: OISSTv2.1."* The same month on the TRADITIONAL monthly (`sstoi`) is **+2.84**. The TRADITIONAL weekly (`wksst`) **rose** from +3.1 (23SEP) to **+3.2 (30SEP)**. **WALTER's "weekly +2.1" mislabels the instrument.**
> 2. 🔴 **It is a FIFTH and SIXTH index family, and it resolves open question 5.** The deck's bullet slide (5 Oct) sits under a chart titled **"Relative SST Anomalies"**, so its "latest weekly SST departures" (0.1/2.3/3.3/4.5) are **relative weekly** OISSTv2.1. `wksst` is **traditional** weekly OISSTv2.1. Both use OISSTv2.1, so CPC's footnote is **true** and there is **no self-contradiction**. A gap that is nearly the same across regions is what removing one tropical-mean value produces. ⚠️ The earlier "ERSST" labels on the Discussion's quads (9/10: 0.1/1.8/2.5/3.4; July: 1.4/1.7/2.9) **match today's relative Fig. 2 at Aug and Jul**, read off the chart ±0.1. Those labels were most likely wrong. That inference rests on the values: the old captions can't be re-read.
> 3. **ONI JAS +2.16 / RONI JAS +1.69** (first JAS print, 3 Oct). ONI has crossed the 2.0 very-strong line (+0.16 above it). RONI is **0.81 below** +2.5. **The same season ranks differently on the two instruments:** ONI JAS is the highest JAS on record (1997 +1.79), but **RONI JAS is 2nd, BEHIND 1997 (+1.84).** ONI−RONI = **+0.47**, so the within-event narrowing has **reversed** (JJA +0.44).
> 4. **Historic-event odds: OND 75 → 83%**, plus newly stated **SON 54% · NDJ 70%**. 🔴 **The headline changed KIND:** 9/10 said *">90% very strong"* (≥2.0, fall/winter). 10/8 says *">83% strong-to-very strong through JFM 2027"* (≥1.5, a longer window). **That is not a downgrade.** Very-strong odds rose at every season in the Strength table (OND 98→100, DJF 75→81, JFM 39→46).
> 5. **Derived, HYPOTHESIS:** CPC's historic odds reproduce from its own RONI percentile table within 1 pt **if the cut-off is ≥2.45** (a RONI that rounds to +2.5), and miss by 4–10 pts at ≥2.50. That held in 4 of 4 seasons. LOG `historic_odds_imply_2.45_cutoff_HYPOTHESIS`.
> 6. **The RONI record holder is 1982-83 (+2.40, DJF 1983), not 1997 or 2015.** §2's peak table omitted it.
### Piece 2 — regime/DOSSIER.md lines 71–86 as of 2026-10-29 (verbatim)
**September issue (kept for comparison):**

| Season | P(RONI ≥ 2.0) "very strong" | RONI 25th | **RONI median** | RONI 75th |
|---|---|---|---|---|
| ASO 2026 | 77% | 1.96 | 2.07 | 2.18 |
| SON 2026 | 97% | 2.26 | 2.43 | 2.60 |
| **OND 2026** | **98%** | **2.44** | **2.67** | **2.90** |
| NDJ 2026-27 | 93% | 2.28 | 2.57 | 2.85 |
| DJF 2026-27 | 75% | 1.94 | 2.27 | 2.59 |
| JFM 2027 | 39% | 1.50 | 1.82 | 2.14 |
| FMA 2027 | 5% | 0.97 | 1.26 | 1.54 |
| MAM 2027 | 0% | 0.54 | 0.79 | 1.05 |
| AMJ 2027 | 0% | 0.12 | 0.38 | 0.65 |

⇒ **Forecast peak timing = OND 2026** (median 2.67, the series maximum; 98% ≥ 2.0). CPC prose: *"El Niño will continue to strengthen through the end of the year."*
⇒ **The OND 25th percentile (2.44) sits just below the +2.5 historic bar** — arithmetically consistent with the 75% headline. ⚠️ *(2026-10-09 worker flag, not an overwrite: on a strict ≥2.50 cut-off this table implies ~69% for OND, not 75%. 75% comes out only at ≥2.45. See §1 item 5 and LOG `historic_odds_imply_2.45_cutoff_HYPOTHESIS`.)* **Decay is forecast to be fast:** ≥2.0 odds fall 93% → 75% → 39% → 5% across NDJ→FMA.
### Piece 3 — regime/DOSSIER.md lines 152–170 as of 2026-10-29 (verbatim)
**Product:** CPC seasonal outlook, retrieved at the primary as **GIS shapefiles** (`seastemp_202609.zip` / `seasprcp_202609.zip`, layers `lead3_DJF_temp` / `lead3_DJF_prcp`) — **not** an image and **not** a search summary.
**`Fcst_Date` = 20260917 · `Valid_Seas` = "DJF 2026-2027"** — the issuance of Thursday 17 Sep 2026.

### TEMPERATURE — the PJM footprint

| Location | DJF above-normal probability |
|---|---|
| **Cleveland OH** | **50%** |
| Washington DC · Baltimore · Philadelphia · Newark NJ · Pittsburgh · Columbus OH · Dayton OH · Indianapolis · Chicago (ComEd) · Charleston WV · Louisville | **40%** |
| Richmond VA · Roanoke VA (southern edge) | 33% |

**Florida:** *near-normal* remains the **favored** temperature category (33%) at Miami / Orlando / Tampa.
**Northern tier:** Seattle, Boise, Missoula, Great Falls all **40% above-normal** — consistent with guard ② (the North goes **milder**, not colder).
**Southwest:** Los Angeles, San Diego, Phoenix, Tucson, Denver all **Equal Chances** on temperature.

### ⚠️ THE MOST IMPORTANT THING ABOUT THIS OUTLOOK IS THAT IT DID NOT MOVE

Polygon-to-polygon against the 8/20 issuance (`lead4_DJF` in `seastemp_202608`): **identical at all 8 PJM points tested**, and identical at 9 of 10 precipitation points. **CPC raised historic-event odds 69% → 75% over the same month and did not strengthen the DJF CONUS signal at all.**
⇒ **A rising ENSO amplitude is not translating into a stronger forecast CONUS anomaly.** That is itself the reliability problem of §5 showing up in CPC's own product, and it is the single most decision-relevant thing in this pass for anyone keying a winter view to "historic El Niño."
### Piece 4 — regime/DOSSIER.md lines 237–237 as of 2026-10-29 (verbatim)
1. ✅ **CLOSED — CPC DJF 2026-27 outlook.** Fetched 2026-09-18 (§6). **Still owed to WATT and MARCO**, whose 8/12 packets were built on composites this product supersedes — **and the headline for them is that the outlook did NOT strengthen** while the event did.
### Piece 5 — regime/DOSSIER.md lines 239–242 as of 2026-10-29 (verbatim)
   - **ONI-based read (JJA 2026): +1.80** — the ≥1.5 "strong" line is **crossed**, margin +0.30. On this basis the event reads *strong, and approaching historic.*
   - **RONI-based read (JJA 2026): +1.36** — **has not yet reached the level 2023-24 peaked at (+1.40)**, and sits **1.14 below** the +2.5 OND bar CPC quotes odds against. Trajectory FMA −0.44 → MAM −0.04 → AMJ +0.49 → MJJ +0.97 → **JJA +1.36**.
   - ⚠️ **The two instruments have never disagreed more about what kind of event this is.** **Would likely *soften* several composite-derived reads if RONI became the keying instrument.** Worth doing **before winter**, and worth telling WATT/MARCO if it changes anything.
   - **CPC's own forecast bridges the gap:** its RONI outlook takes +1.36 (JJA) → **2.07 (ASO) → 2.43 (SON) → 2.67 (OND)**. The +2.5 bar is reached **only at OND, and only at roughly the 30th percentile upward** (§1b).
### Piece 6 — regime/DOSSIER.md lines 246–246 as of 2026-10-29 (verbatim)
5. ✅ **PROPOSED RESOLUTION (2026-10-09), for AEOLUS to adjudicate: the gap is RELATIVE vs TRADITIONAL, not ERSST vs OISST and not a CPC self-contradiction.** On the 5 Oct deck, the chart beside the bullet numbers is titled **"Relative SST Anomalies"**. The Discussion's Fig. 2 is captioned *"relative … minus tropical mean (20°N-20°S) … re-scaled … Data: OISSTv2.1"*. `wksst`/`sstoi` are traditional. All of them are OISSTv2.1, so the footnote was true all along. Removing one tropical-mean value from every region produces exactly a gap that is nearly the same across regions. **Evidenced for the 5 Oct deck and the 8 Oct Discussion. For earlier vintages it is INFERRED** from matching values; the old captions can't be re-read. *(Superseded framing kept so the change is visible: "the ~−0.8/−0.9 uniform gap tracks ERSST-vs-OISST, yet CPC's footnote says the weekly slides use OISSTv2.1 … a documented CPC self-contradiction.")* **Ruling stands: `wksst9120.for` is the sole scored weekly figure.** The relative indices are a separate family, and **no registered command pulls them as numbers.**
### Piece 7 — regime/DOSSIER.md line 201 as of 2026-10-29 (verbatim)
   - **2026-10-09 update:** **ONI JAS +2.16 against RONI JAS +1.69.** ONI has crossed the 2.0 very-strong line. RONI is 0.31 short of 2.0 and has not crossed it. **On RONI the event is behind 1997's same-season pace (1.84). On ONI it leads (1.79).** The October outlook needs RONI SON 2.47, OND 2.74.
### Piece 8 — regime/DOSSIER.md line 202 as of 2026-10-29 (verbatim)
3. **Track the ONI−RONI offset as OND approaches.** Current **+0.47** (JAS; JJA was +0.44). At that value +2.5 RONI would imply ~+2.97 ONI, **for illustration only. It is not a conversion.** ⚠️ **The "narrowing within this event" noted 9/18 has REVERSED** (FMA +0.55 → MJJ +0.42 → JJA +0.44 → JAS +0.47). **Re-compute every pass, never carry the conversion forward.** *(10/29: recomputed, still +0.47. No new season has printed, so there is no new point. The ASO print is the next one.)*
### Piece 9 — regime/DOSSIER.md line 206 as of 2026-10-29 (verbatim)
7. **AEO-07 / AEO-08 (PJM DJF).** Measurement supplied, not graded: **PJM is 40% above-normal** across the footprint (50% at Cleveland, 33% on the southern VA edge) — **unchanged from the 8/20 read.**
### Piece 10 — regime/DOSSIER.md line 205 as of 2026-10-29 (verbatim)
6. **AEO-02** (ONI ≥1.5 in an **NDJ** season) resolves on **ONI**, now **+2.16 at JAS** (JJA +1.80). ⚠️ **The threshold is met at the current season but AEO-02 is specified on NDJ — the season has not arrived. Worker does not resolve predictions; the measurement and the margin (+0.66) are above.**
### Piece 11 — regime/DOSSIER.md line 47 as of 2026-10-29 (verbatim)
- *Prior (10 Sep): ">90% very strong", historic OND 75%.*
### Piece 12 — regime/DOSSIER.md line 17 as of 2026-10-29 (verbatim)
> **Prior passes 9/28 · 9/18 · 8/21 · 8/27 → rotated verbatim 2026-10-21 to `archive/REGIME_DOSSIER_ARCHIVE_2026-10-21_prior-passes-and-sec2.md`** (grep it, never boot-read). Standing ruling from them: `wksst9120.for` is the sole authoritative weekly figure (KB-088); never cite deck bullet numbers for anything scored.
