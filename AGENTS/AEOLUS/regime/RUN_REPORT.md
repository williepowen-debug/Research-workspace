run_date: 2026-10-09 (pulls 20:32:57–20:35 EDT; report written 20:40 EDT)
worker: AEOLUS regime/ (ENSO) domain worker · trigger: CPC 8 Oct 2026 Diagnostic Discussion, not yet read by AEOLUS (WALTER SIG-W-20261008-027)

observations_added: 13 rows to `workbook/SERIES.tsv`: ONI JAS, RONI JAS, Sep monthly Niño-3.4 and Niño-1+2, the four weekly regions for week centred 30SEP, 3 revision rows for 09SEP, historic_prob_ond and oni_minus_roni. 7 rows to `workbook/LOG.tsv`. `DOSSIER.md`: two-clock header (Last real data refresh 2026-09-30), new pass block, §1 state and odds, §1b October tables, §2 notes, OQ 2/3/5/6.

---

## EVERY FIGURE — instrument, basis, source, as-of (none interchangeable)

| Figure | Instrument / basis | Source | As-of |
|---|---|---|---|
| **ONI +2.16** (SST 29.12) | ONI, ERSSTv6, 30-yr centred | `oni.ascii.txt` (Last-Mod 03 Oct) | JAS 2026 |
| **RONI +1.69** | RONI, ERSSTv6, 1991-2020 | `RONI.ascii.txt` (Last-Mod 03 Oct) | JAS 2026 |
| ONI−RONI **+0.47** | derived, recomputed | both files above | JAS 2026 |
| **Niño-3.4 +2.84** (SST 29.60) · 1+2 +4.69 · 3 +3.64 · 4 +0.95 | OISST monthly, **traditional**, 1991-2020 | `sstoi.indices` (Last-Mod 05 Oct) | Sep 2026 |
| **Niño-3.4 +3.2** (29.9) · 3 +4.0 · 1+2 +5.3 · 4 +1.2 | OISSTv2.1 weekly, **traditional**, 1991-2020 | `wksst9120.for` (Last-Mod 09 Oct) | week ctr 30SEP |
| Niño-3.4 weekly 23SEP **+3.1** (unrevised) · 16SEP 3.0 · 09SEP **2.8 (rev. from 2.9)** · 02SEP 2.8 | same | same | — |
| **Niño-3.4 +2.1 · Niño-3 +3.0 · Niño-1+2 +3.9** | **RELATIVE MONTHLY** OISSTv2.1, minus tropical mean 20°N–20°S, re-scaled, 1991-2020 | ensodisc text + Fig. 2 caption | Sep 2026 |
| Deck bullets 0.1 / 2.3 / 3.3 / 4.5 (Niño-4 / 3.4 / 3 / 1+2) | **RELATIVE weekly** OISSTv2.1 (chart titled "Relative SST Anomalies") | deck, prepared 5 Oct | ~30SEP |
| Historic event (RONI ≥ +2.5): **SON 54 · OND 83 · NDJ 70** | CPC forecast, RONI | ensodisc prose | issued 8 Oct |
| P(RONI ≥ 2.0): SON 100 · OND 100 · NDJ 96 · DJF 81 · JFM 46 · FMA 6 | CPC Strength table | roni/strengths ("Issued October 2026") | issued 8 Oct |
| RONI medians: SON 2.47 · **OND 2.74 (peak)** · NDJ 2.65 · DJF 2.36 · JFM 1.90 | CPC outlook percentiles | roni/outlook ("Issued October 2026") | issued 8 Oct |

Discussion status: **El Niño Advisory.** Synopsis, verbatim: *"El Niño continues to strengthen, with a strong-to-very strong El Niño likely through January-March 2027 (remaining greater than an 83% chance)."* Next discussion: **12 November 2026.**

## THE +3.1 vs +2.1 QUESTION — a different instrument, not a drop

- The Discussion's own text: *"Most Niño indices increased **in the past month**, reaching +2.1°C in Niño-3.4 … [Fig. 2]"*. That is a monthly figure, not a weekly one.
- Fig. 2's caption, verbatim: *"relative sea surface temperature (SST) anomalies … minus tropical mean (20°N-20°S). The relative indices are re-scaled to match the variance of traditional indices. Anomalies are departures from the 1991-2020 base period monthly means. Data: OISSTv2.1."*
- On the traditional instruments over the same period: monthly Sep **+2.84**; weekly 23SEP **+3.1** (unrevised), then 30SEP **+3.2**. **The traditional weekly rose.** WALTER's "weekly +2.1" mislabels the instrument.
- **Side effect: this resolves DOSSIER open question 5.** The deck's bullet numbers are relative weekly. `wksst` is traditional. Both are OISSTv2.1, so CPC's footnote is true and there is no self-contradiction. The earlier "ERSST" labels on the Discussion's quads (9/10: 0.1/1.8/2.5/3.4; July: 1.4/1.7/2.9) match today's relative Fig. 2 at Aug and Jul when read off the chart. ⚠️ That match is inferred from values; the old captions can't be re-read.

---

threshold_state:
- ONI vs strong ≥1.5: JAS +2.16 → **+0.66 above**. ONI vs very strong ≥2.0: **+0.16 above**. AEO-02 is specified on NDJ, which has not arrived. Not graded.
- RONI vs historic bar +2.5: JAS +1.69 → **0.81 below** (0.76 below a 2.45 cut-off; see the hypothesis below). NOT-FIRED. The bar is an OND forecast target, not a present-state test.
- Historic-event odds OND: **83%** (8 Oct), against 75% on 9/10.
- Very-strong odds: **no longer in the prose.** The Strength table gives OND 100 (Sep table: 98). No SERIES row was written for it (see gaps).
- Weekly Niño-3.4 trend: 02SEP 2.8 → 09SEP 2.8 → 16SEP 3.0 → 23SEP 3.1 → **30SEP 3.2. File record, rank 1 of 2,353 weeks.** Same week in 1997 and 2015: +2.0.

changes:
- ONI JJA +1.80 → **JAS +2.16**. RONI JJA +1.36 → **JAS +1.69**. Monthly Aug +2.52 → **Sep +2.84**. Weekly 23SEP +3.1 → **30SEP +3.2**.
- Historic OND **75 → 83**. Very strong (table): DJF 75→81, JFM 39→46. Every RONI median moved up 0.02–0.09.
- 🔴 **The headline changed kind. Do not read it as >90 → >83.** 9/10 was ">90% very strong" (≥2.0). 10/8 is ">83% strong-to-very strong through JFM" (≥1.5, a longer window). The 83 equals JFM P(≥1.5) = 37+46.
- ONI−RONI offset +0.44 → **+0.47**: the within-event narrowing has reversed.
- Revisions on 09SEP: Niño-3.4 2.9→2.8, Niño-1+2 4.5→4.6, Niño-4 0.9→0.8. The run of consecutive weekly gains to 23SEP is now 3, not 4.

proposed_findings (PROPOSAL-ONLY — AEOLUS adjudicates):
1. **CPC's prose ENSO figures are RELATIVE indices.** Two families (traditional and relative) × two cadences (weekly and monthly) on OISSTv2.1, plus ONI and RONI on ERSSTv6. A relayed "Niño-3.4 = X" must name its family. Sources: ensodisc 8 Oct Fig. 2 caption; deck 5 Oct p5 chart title.
2. **SOURCES ⑤ and ⑥ text needs correcting.** ⑤'s "ERSSTv5 triple" and ⑥'s "basis UNRESOLVED / self-contradiction" are superseded by finding 1. I did not edit SOURCES.md; it is outside this run's write list.
3. **On RONI, 2026 is behind 1997's same-season pace (JAS 1.69 vs 1.84); on ONI it leads (2.16 vs 1.79).** "Record" is true on the absolute instruments and false on RONI at JAS. Source: oni/RONI ascii, 3 Oct vintage.
4. **The RONI record holder is 1982-83 (+2.40, DJF 1983), not 1997 or 2015.** +2.5 beats it by ~0.10, not ~0.25. DOSSIER §2's 2023-24 "peak" of 1.40 is the NDJ value; RONI's own peak was 1.42 (OND). Source: RONI.ascii.
5. **HYPOTHESIS:** CPC's historic odds reproduce from its RONI percentiles at a **≥2.45** cut-off, within 1 pt in 4 of 4 seasons. At ≥2.50 they miss by 4–10 pts. Not stated by CPC; the odds may instead come from the full ensemble distribution.
6. **The headline basis switched** from very strong (≥2.0) to strong-or-stronger (≥1.5) through JFM. Anyone relaying ">83%" as a fall from ">90%" inverts the direction.

gaps:
- **Relative-index values are chart-only.** No registered command pulls the relative monthly or weekly indices as numbers. The Niño-4 relative monthly (~0.0) is read off the chart. Fig. 2 names `…/enso_update/rel_nino_month-hr.png`; I did not search for a data file.
- **No approved instrument names** for: SON/NDJ historic odds, per-season very-strong odds, relative indices, Niño-3/4 monthly. These were recorded in LOG only. **verystrong_prob_ond has no 10/8 row**, because the instrument is defined as "from the prose" and the prose no longer states it. The Strength-table OND value (100) is in LOG and DOSSIER. AEOLUS should rule on redefining it.
- The strengths and outlook pages are not registered SOURCES commands. I reached them via the Discussion's own links, as on 9/18.
- The week centred 07OCT is not yet in `wksst9120.for`. All registered commands returned HTTP 200 with no errors.
- Pre-existing blank lines at SERIES.tsv:23 and LOG.tsv:4 were left untouched (append-only).
