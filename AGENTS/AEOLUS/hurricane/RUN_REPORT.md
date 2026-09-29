# AEOLUS · HURRICANE — worker run report

```
run_date:            2026-09-28 (Monday) · pulls 2026-09-28 19:59–20:05 EDT (23:59–00:05 UTC)
prior run:           2026-09-18 (AEOLUS dark 9/18 → 9/28)
data as-of:          b-deck fix 2026092818 · NHC TWO 200 PM EDT Mon 9/28 · NHC advisories 2100Z 9/28
```

## dark_window_scan

**Window 2026-09-18 0000Z → 2026-09-28 1800Z. All 45 archived TWOAT issuances read** (IEM AFOS `list.json` + `nwstext`, 4/day plus a 1430Z Special on 9/18).
**No system or disturbance was placed in the Gulf, Caribbean, Bahamas or near Florida in any issuance.** The words Gulf/Caribbean appear only in the fixed header line of all 45. **The Gulf/FL escalation line was not met at any point in the window, so there is no historical fire to register.**

| System | Genesis (first DB fix) | Status over time | Peak (b-deck) | Landfall | Gulf/FL |
|---|---|---|---|---|---|
| AL98 | (pre-window) | TWO 20% → 10% → near 0%, removed by Special TWO 9/18 | 25 kt | none | no |
| **AL06 Fay** (ex-AL99; TWO peak 90%) | 9/17 12Z, 32.1N **34.0W** | TD SIX 9/19 12Z → TS 9/20 06Z → remnant low 9/22 21Z → **regenerated** TD 9/23 21Z → TS 9/24 00Z–9/26 00Z → TD since 9/26 06Z | **60 kt / 995 mb** 9/21 00Z, 34.2N 32.1W. Discussion 7: *"just shy of hurricane intensity"* | none | no. Now 26.6N 45.3W, ~2,160 mi from Miami |
| **AL07 Gonzalo** (ex-AL90; TWO peak 80%) | 9/22 18Z, 8.0N **13.5W** | TS 9/25 00Z → post-tropical 9/26 21Z (**final advisory**) | **45 kt** 9/25 12–18Z near Cabo Verde | none. NHC warned of gusty winds, heavy rain and flash flooding for the Cabo Verde Islands | no |
| **AL08 Hanna** (ex-AL91; TWO 10/20 → 50/60 → 70/80) | 9/26 18Z, 27.5N **58.3W** | TS 9/28 12Z at 36.7N 51.3W | 40 kt (still active) | none. Moving ESE away from the US | no |
| Former-Fay remnant area | — | TWO 20% → 70% on 9/23, then became the regenerated Fay | — | — | no |

No other outlook area reached 40%. **What NHC wrote** (quoted, per the 8/13 discipline): Gonzalo before it formed, TWO 9/23: *"strong upper-level winds should end the opportunity for development by the weekend"*. Gonzalo's final discussion, 9/26: *"strong southwesterly vertical wind shear, diagnosed at nearly 50 kt… very dry air infiltrating the low-level circulation"*. Fay's remnant, 9/22: *"dry air mass with strong upper-level convergence"*. Fay now, discussion 35: *"Fay continues to defy model guidance"*, forecast post-tropical around 9/30 and dissipated by 10/01 06Z near 52W. Hanna, discussion 2: *"20-25 kt of westerly vertical wind shear… importing very dry tropospheric air"*, forecast post-tropical around 10/01.

## observations_added

**9 rows → `workbook/SERIES.tsv`** · **11 rows → `workbook/LOG.tsv`** · **5 rows → `workbook/STORMS.tsv`** · `DOSSIER.md`: new §00 block, two-clock header moved 2026-09-18 → **2026-09-28**. Older sections are marked as 9/18 vintage and superseded wherever §00 gives a newer figure. No new instrument names.

## threshold_state

*Values and margins only. Nothing below is a score, a fire, or a resolution.*

| Instrument | Value (date, basis) | Line | Margin | State |
|---|---|---|---|---|
| ACE vs normal (peril) | **9.5800** through b-deck 2026092818, computed from numbered decks AL01–08 | Yellow ≥134.8 / Orange ≥159.4 / Red ≥183.9 + landfall | 125.2 below Yellow | NOT-FIRED |
| ACE vs to-date normal | **10.61%** of 90.3012 (Sep 28, exclusive convention) · 10.44% of 91.7490 (inclusive) | Yellow ≥110% | — | NOT-FIRED |
| AEO-01 ACE leg | 9.5800 | season-end <110.3257 | **100.7457** units would still have to accrue to cross the line | open until 11/30 (AEOLUS grades) |
| AEO-01 hurricane leg | **0** hurricanes | ≤7 | 7 of 7 remaining | open |
| Majors | 0 | — | — | — |
| C1 escalation: a Gulf/FL system | none at any point 9/18–9/28, and none now (Fay 45.3W, Hanna 48.7W) | needs a Gulf/FL system | — | NOT-FIRED (not met at any time in the window) |
| Reinsurance rate-on-line | no transacted print | +5 / +15 / +25% YoY | — | NOT OBSERVABLE before the Jan-2027 renewal |
| Cat-loss tally | Gallagher Re H1'26 $46bn = 72% of the $64bn 10-yr avg (Aug vintage, unchanged) | ≥110% | 38 pts below Yellow | NOT-FIRED |

## changes

1. **Three new named storms (Fay, Gonzalo, Hanna). Season to date: 8 named storms, 0 hurricanes, 0 majors.** The season's peak intensity is now **60 kt** (Fay, 9/21 00Z), up from 50 kt.
2. **ACE: 4.3950 (9/18) → 9.5800 (9/28), +5.1850** (Fay 3.5750, Gonzalo 1.2900, Hanna 0.3200). **3.8950 of the total is provisional** because Fay and Hanna are still active. Gonzalo's figure comes from the operational b-deck after its final advisory.
3. **To-date normal recomputed fresh for Sep 28: 90.3012** (exclusive) / 91.7490 (inclusive); 73.66% of the seasonal mean has normally accrued by this date. Parse re-validated: 14.40 named storms / 7.20 hurricanes, and the 9/18 figures (73.7248, 4.3950) reproduce exactly. **The ratio ROSE for the first time: 5.96% → 10.61%.** Over 9/18–9/28, 2026 accrued 5.185 units against 16.576 in a normal season, i.e. 31% of normal pace. **Rank: lowest of 30 (1991-2020) under both conventions**; 1994 is next at 12.7625. **Lowest of 59 for 1966-2024.**
4. **ACE still needed to cross the AEO-01 line: 105.931 (9/18) → 100.7457 (9/28).** ACE accrued after Sep 28, 1991-2020: mean 30.835, median 31.021, max **84.625 (2016)**, min 0.000 (1993). **0 of 30 years accrued 100.7457 after this date** (on 9/18 it was 1 of 30: 1998). For 1966-2024 the max is 86.925 (2024), **0 of 59**. The lowest Sep-28 to-date ACE of any 1966-2024 season that still finished ≥110.3257 is **2016 at 57.9025**. Lowest-to-date cohorts that finished <110.3257: bottom-6 6/6, bottom-8 8/8, **bottom-10 9/10** (it was 10/10 on 9/18). The one exception is 2016, which joins the cohort at Sep 28 and finished at 142.53.
5. **Outlooks.** CSU seasonal re-verified **unchanged**: 9/4/1, ACE 50. NOAA re-verified **unchanged**: issued 6 Aug, 75% below-normal. NOAA's page still says *"2 named storms recorded thus far"*; the actual count is 8. **There has been no CSU two-week issue after 9/16.** Re-read of the 9/16 PDF: Sep 16–29 below-normal (<11 ACE) 78%, near-normal 20%, above-normal 2%. **Observed ACE in that window through 9/28 18Z is 5.1850.** The window stays open through 9/29, so it is not graded. The next issue is due 9/30, and the final one 10/14.
6. **Current NHC 7-day outlook** (200 PM EDT Mon 9/28, forecaster Papin): *"Tropical cyclone formation is not expected over the next 7 days."* Active storms are TD Fay and TS Hanna only.
7. **ACE west of 60W (the CSU forecast is 25; normal is 73): 2026 = 3.4625** (Arthur, Bertha, Edouard). All three new storms contributed 0 here.

## proposed_findings

*These are proposals only. AEOLUS decides on each.*

- **P1. 2026 remains the lowest ACE year at Sep 28 in both 1991-2020 (30 years) and 1966-2024 (59 years), even though the ratio to normal rose for the first time.** Sources: 9.5800 against 90.3012 = 10.61%, computed from NHC ATCF b-decks and HURDAT2, with the parse validated. *Read the mechanism, not the sign:* the ratio rose because three weak storms in the eastern Atlantic produced 5.185 units while normal accrual slowed.
- **P2. After Sep 28, no year in either record accrued the 100.7457 units AEO-01 would still need.** The maximum is 84.625 (2016, 1991-2020) and 86.925 (2024, 1966-2024). The single counter-example available on 9/18 (1998) has dropped out. This is a measurement, not a probability.
- **P3. There was no Gulf/FL involvement at any point in the dark window.** All 45 TWOs were checked, so this negative comes from the primary archive and is not an inference.
- **P4. Peak-season tell: three new systems in its population, reported as facts only.** All three formed east of 60W. **Gonzalo:** NHC flagged the shear before it formed, and it died at about 23W. **Fay:** NHC flagged the shear; it formed, peaked at 60 kt, and has not reached 60W; it is forecast to dissipate near 52W. **Hanna:** it formed at 51.3W from a genesis at 58.3W and is moving ESE. ⚠️ **Ambiguity:** Fay and Hanna are systems at 30–37N that never tracked west across the basin. Whether they test a "fails before 60W" tell at all is AEOLUS's call. **None of the three became a hurricane.**
- **P5. Method fix for `SOURCES.md` (a proposal; the file was not edited).** The instruction that invest decks "contribute 0 — keep them in the loop" was **false this run**. `bal902026` has a 40-kt TS row at 2026092500 and `bal912026` has one at 2026092812, and each duplicates the named storm's first TS fix. Summing every deck gives **9.9000 instead of 9.5800, a 0.32 over-count.** Proposed rule: sum AL01–AL49 only, or dedupe by genesis-num. Also, `bal98`/`bal99` have **disappeared** from the btk/ listing (AL99 was renumbered to AL06), so the listing is not append-only.
- **P6. Loss leg: a third H1 read and a threshold for context.** The Aon H1'26 global insured cat-loss figure is **$47bn** (vs $100bn H1'25), dated 2026-07-22 and reached via Artemis (secondary). It is new to this folder. Keep it alongside Gallagher Re $46bn and Swiss Re $42bn; the three have different perimeters and should not be reconciled. For context (Apr-21 vintage, via Reinsurance News): Gallagher Re estimated that an insured loss of **$115–125bn above the expected annual average** is needed to meaningfully shift property re/insurance pricing.

## gaps

1. **Swiss Re H1 primary:** `curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" -L https://www.swissre.com/institute/research/topics-and-risk-dialogues/climate-and-natural-catastrophe-risk/first-half-2026-insured-catastrophe-losses.html` → **HTTP 403, 5,984 B, "Just a moment... Enable JavaScript and cookies to continue"**. The $42bn figure is still secondary-only.
2. **Gallagher Re H1 report URL** `https://www.ajg.com/gallagherre/news-and-insights/natural-catastrophe-and-climate-report-h1-2026/` → **HTTP 200, 212 B JS shell, no content.** No verified Gallagher Re command exists.
3. **Edouard insured loss: nothing found.** WebSearch on 9/28 found no estimate from Verisk, KCC, Moody's RMS or CoreLogic. **This negative comes from search, not from a verified command.** No publisher in `SOURCES.md` has a command for event-level loss.
4. **Artemis cat-bond series** (verified command): HTTP 200, 827 points, but the **latest point is still 2026-08-28** (spread 5.05%, expected loss 2.50%, collateral 3.81%). There is no September point, so the series now runs **31 days** behind. The page did not fail; it has simply not refreshed.
5. **CSU two-week 9/30:** `https://tropical.colostate.edu/Forecast/2026-0930.pdf` → **HTTP 404 (6,493 B)**. It is not yet issued (scheduled 9/30), so this is expected and not a failure. 0923 and 0928 also return 404; neither is a scheduled date.
6. **8 PM EDT 9/28 TWO:** not yet posted at 00:04Z pull time. The current read is the 200 PM EDT issuance.
7. **Q3 cat-loss tallies (Gallagher Re, Aon)** are not yet published; they are expected in October.
8. **No ENSO values were pulled.** That is correct under the SHARED-INPUT RULE: ENSO belongs to `regime/`.
9. **Correction to the spawn prompt:** the prompt warned that `AGENT.md`'s "WHAT TO REPORT" block is 8/13 vintage. **As read today it is not.** It was re-cut on 2026-09-18 to hold questions only, with no values ("Do not re-add values here"). This run's reference state came from the spawn prompt and `DOSSIER.md`. Nothing was edited.
