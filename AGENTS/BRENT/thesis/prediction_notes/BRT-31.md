# BRT-31 — Path-B successor (gasoline demand, two consecutive weeks ≤ −1.5%)

**Registered 2026-10-01 13:2x ET** by BRENT (spawned by PROME `prome-0c`), on **WQ-346 RULED**: Will's 9/30 19:32 ET blanket word (*"Lets look at the WQ and see if there are other simple or no brainer decisions you can just move forward with and assume I approve?"*), applied by PROME on its own written recommendation; Will can reverse it by naming the row. Packet: `inbox/processed/2026-09-30_from-PROME_WQ-346-RULED_BRT-31-v2-approved-at-40pct.md` (PROME `be8b72644`).

**The letter = v2 AS WRITTEN**, verbatim at [`setups/2026-09-30_BRT-31-path-B-successor-DRAFT-v2.md`](../../setups/2026-09-30_BRT-31-path-B-successor-DRAFT-v2.md) §2 (commit `98d07c696`). The PREDICTIONS.tsv row transcribes §2; **on any disagreement the v2 file §2 governs.** v1 (`167112780`) is the superseded record; CARL's blind read (`13aa2cd46`) forced v2 (❌1 base rate/confidence, ❌2 outcome precedence).

| Field | Registered value |
|---|---|
| Window | Data weeks ending 10/9 → 11/27, fixed at the ruling. **The 10/2 print is NOT graded** (Labor Day one-sided). First release Thu 10/15 12:00 ET |
| Confidence | **40%** = P(MET \| not NOT-FIRED). Base graded by the letter: NOT-FIRED 22%; if fired MET 46 · NOT MET 32 · NV 22; equal-weight MET 43 |
| Precedence | First terminal event in data-week order; a same-week tie → NOT-FIRED |
| Contamination | CLOSED list (federal excise cut; state cuts ≥ 10% of consumption); can only refuse NOT MET |

**Caveats recorded at the ruling (WQ-346 row):** ~6 surviving episodes, ±15 pts · CARL's unconditional 25–30% view is defensible · the 15% ordinary-times noise floor. DOCKET L537 carries the rider.

**Grading log:** window weeks one to four evaluated (October 20, 21, 28 and November 5); overall row remains OPEN, not resolved.

## October20 owner evaluation — data weekOctober9/releaseOctober15

First week NON-QUALIFYING: exact four-week WGFUPUS2 comparison−0.3959714211930791%, qualifying streak0. Price checkOctober12$4.331 versusOctober13,2025$3.061 =+41.4897092453%; below+20%counter0of3. Confidence40%and overall OPEN unchanged; no terminal event. Full source/date/counter/contamination evaluation and matched weekly output correction: [report](../../research/2026-10-20_eia-oct15-evaluation/REPORT.md), [machine receipt](../../research/2026-10-20_eia-oct15-evaluation/evaluation.json). Exact eight inputs match publisher-dated archived weekly rows; no local release-day XLS capture or immutable-archive guarantee claimed. NCin-window suspension3.7523%SEDScoverage alone below10%; other identified cuts predatewindow. Bounded policy review is not a50state absence certificate; finalNOTMETneeds recheck. METstillavailableunderletter. No rounded-summary substitution or new threshold.

## October 21 owner evaluation — data week October 16 / release October 21

Week two is NON-QUALIFYING. The exact four-week `WGFUPUS2` comparison is +1.461596692482385% (8,712.0 vs 8,586.5 kb/d; current 8982, 8408, 8769, 8689; base 8454, 8455, 8919, 8518). Qualifying streak 0. Price check 10/19 $4.284 vs 2025-10-20 $3.019 = +41.90%; below-20% counter 0 of 3. EIA weekly retail was used as the letter's same-survey fallback because FRED was unreachable at boot. This is a release-day capture of first-published values; prior-week inputs show no revisions against the 10/20 capture. Confidence 40% and overall OPEN unchanged; no terminal event. Both window prints so far are above −1.0%. Contamination screening was not re-run, since it can only refuse NOT MET; the 10/20 bounded-review caveat stands. [Report](../../research/2026-10-21_eia-oct21/REPORT.md) §5, [machine receipt](../../research/2026-10-21_eia-oct21/evaluation.json).

## October 28 owner evaluation — data week October 23 / release October 28

Week three is NON-QUALIFYING. The exact four-week `WGFUPUS2` comparison is −0.6762200736648250% (8,629.25 vs 8,688.0 kb/d; current 8358, 8982, 8408, 8769; base 2025-10-24 8924, 10-17 8454, 10-10 8455, 10-03 8919). Qualifying streak 0. Price check 10/26 $4.269 vs 2025-10-27 $3.035 = +40.66%; below-20% counter 0 of 3 (EIA weekly retail, the letter's same-survey fallback). Release-day capture of first-published values; no revisions against the 10/21 capture. The Wednesday routine's "−0.679%" divided EIA's rounded 4-week averages (8,629/8,688); the letter's unrounded basis is −0.6762%. All three window prints so far are above −1.0%. Confidence 40% and overall OPEN unchanged; no terminal event. Contamination screening not re-run (it can only refuse NOT MET); the 10/20 bounded-review caveat stands. [Report](../../research/2026-10-28_eia-oct28/REPORT.md), [machine receipt](../../research/2026-10-28_eia-oct28/evaluation.json).

## November 5 owner evaluation — data week October 30 / release November 4

Week four is NON-QUALIFYING. The exact four-week `WGFUPUS2` comparison is −0.4350707350102234% (8,639.0 vs 8,676.75 kb/d; current 8808, 8358, 8982, 8408; base 8874, 8924, 8454, 8455). Qualifying streak 0. Price check 11/2 $4.153 vs 2025-11-03 $3.019 = +37.56%; below-20% counter 0 of 3 (EIA weekly retail, the letter's same-survey fallback). Read from the EIA API on November 5, not a release-day workbook; the three prior-week inputs match the October 28 capture. The Thursday fallback's −0.4380% used EIA's rounded pair, not the letter's arithmetic. Row OPEN at 40%, no terminal event. [Evidence](../../research/2026-11-05_evening-rows/NOTE.md).

## November 12 owner evaluation — data week November 6 / release November 12 (Veterans Day)

Week five is NON-QUALIFYING. The exact four-week `WGFUPUS2` comparison is −1.034580498866213% (8,728.75 vs 8,820.0 kb/d; current 8767, 8808, 8358, 8982; base 2025-11-07 9028, 10-31 8874, 10-24 8924, 10-17 8454), release-day psw01 capture 12:11 EST, no revisions to prior inputs against the 10/28 capture. Qualifying streak 0. Price check 11/9 $3.995 vs 2025-11-10 $3.056 = +30.73%; below-20% counter 0 of 3 (EIA weekly retail, the letter's fallback). **This is the first window print at or below −1.0%, so the NOT MET end state ("every print > −1.0%") is no longer reachable.** Remaining end states: MET, NO-VERDICT, NOT-FIRED-PRECONDITION (needs all three remaining price weeks under +20%), NO-VERDICT-CONTAMINATED. Mechanism: base effect; current four-week demand rose 89.75 kb/d while the base rose 143.25 as last year's 9,028 entered. Arithmetic only: w/e 11/13 qualifies if it prints ≤ 8,890 kb/d; w/e 11/20 then needs the two prints to sum ≤ 17,054. OPEN at 40%, no terminal event. Note: `../../research/2026-11-12_wpsr/NOTE.md`.

## November 18 owner evaluation — data week November 13 / release November 18 (section added 2026-11-25; the grade itself was written 11/18 in the PREDICTIONS row and its note)

Week six QUALIFYING: −1.784805113989929% (8,680.75 vs 8,838.5 kb/d), streak 1; price +24.27%, counter 0 of 3. This section was missing from this note until 2026-11-25; the 11/18 grade stands as written in `thesis/PREDICTIONS.tsv` and `../../research/2026-11-18_gulf-eia/NOTE.md`.

## November 25 owner evaluation — data week November 20 / release November 25 (holiday week, 10:30 ET)

Week seven is NON-QUALIFYING. The exact four-week `WGFUPUS2` comparison is −0.2190237797246558% (8,769.75 vs 8,789.0 kb/d; current 2026-11-20 8714, 11-13 8790, 11-06 8767, 10-30 8808; base 2025-11-21 8726, 11-14 8528, 11-07 9028, 10-31 8874), from my release-day psw01 capture (files saved 10:30:58 EST; no revisions to prior inputs). The week needed 8,263.66 kb/d or less to qualify and printed 8,714, flat on last year's 8,726. Streak 0. Price check 11/23 $3.642 vs 2025-11-24 $3.061 = +18.98%, the first window week under +20% (counter 1 of 3; one window week left, so the precondition cannot fire).

**What is decided:** MET is unreachable (week 11/27 cannot pair with a qualifying 11/20) and NOT MET was ruled out on 11/12. The window-end label is **NO-VERDICT**, or **NO-VERDICT-CONTAMINATED** only if a listed federal or large-state gasoline-tax cut takes effect by 11/27; both are excluded from calibration. The row stays OPEN until the window-end print (data week 11/27, release about 12/02), where the grade is written. **What the window showed:** one qualifying week (11/13) came from last year's high base (9,028 entering), not from a fall in current volume; current weekly volume ran 8,7xx–8,8xx kb/d through November while retail fell from $4.15 to $3.64. Label discipline: this is not "volume resilient" (that is the NOT MET label, unavailable) and not "weakening measured". Note: `../../research/2026-11-25_eia-gulf/NOTE.md`.
