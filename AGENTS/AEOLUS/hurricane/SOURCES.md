# AEOLUS · HURRICANE — verified primary sources

**Verified on 2026-08-13.** ⚠️ **What failed is recorded too** — an unverified URL in a sources file is worse than no entry, because it looks checked.

---

## NHC — the daily instrument ✅ verified 8/13

### Active storms (structured, best for a scripted check)
```bash
curl -s "https://www.nhc.noaa.gov/CurrentStorms.json" \
 | python3 -c "
import json,sys
d=json.load(sys.stdin)
print('active:', len(d.get('activeStorms',[])))
for s in d.get('activeStorms',[]):
    print(' ', s.get('name'), s.get('classification'), s.get('intensity'),
          s.get('latitudeNumeric'), s.get('longitudeNumeric'))
"
```
**Verified return (8/13): 3 active** — `Cristobal TD 30` (Atlantic, 38.6N 38.2W), `Hernan TS 35` (E Pacific), `One-C PC 35` (C Pacific).
⚠️ **Covers all basins** — filter by longitude/basin before calling anything "Atlantic."

### Tropical Weather Outlook — formation odds (the trigger instrument) ✅
`https://www.nhc.noaa.gov/gtwo.php?basin=atlc&fdays=7`
**Verified 8/13 08:00 EDT:** AL92 **80%/80%** (~1,000 mi E of the Lesser Antilles, *"expected to weaken by late Friday due to strong upper-level winds and dry air"*); AL94 **30%/50%** (SSW of Cabo Verde).
⚠️ **Read the DISCUSSION TEXT, not just the percentages.** On 8/13 the number said 80% while the prose said *weakening* — **the prose carried the El Niño shear mechanism and the number didn't.**
Text version: `https://www.nhc.noaa.gov/text/MIATWOAT.shtml` *(fetched 24.6 KB; percentages are in prose, so grep the body rather than a tag).*

**Trigger reminder: the C1 escalation line needs a GULF/FL system.** Deep-Atlantic Cabo Verde waves and subtropical fish storms do **not** fire it however high the percentage.

---

## SEASONAL OUTLOOKS — the revision clock

### CSU / Klotzbach ✅ verified 8/13, **CADENCE CORRECTED 8/21**
`https://tropical.colostate.edu/forecasting.html` *(160 KB, loads fine)*

**① SEASONAL forecast** — issues **early Apr / early Jun / early Jul / early Aug**. **Verified 2026:** initial forecast **Apr 9**; **8/5 update HELD at 9/4/1** — CSU's 2nd-lowest August named-storm outlook ever. **8/5 is the FINAL seasonal issuance for 2026.**
**Also published on that page and not previously recorded: CSU's own seasonal ACE central forecast, `2026 = 50`** (vs a ~123 normal) — **40.8% of the 122.58 mean.** Instrument `csu_ace_forecast`, added to the vocabulary 8/21. *("ACE West of 60°W" 25 vs 73 is a separate figure — do not conflate.)*

**② 🔴 TWO-WEEK forecast — A LIVE CADENCE THIS FILE PREVIOUSLY DECLARED NONEXISTENT.**
`https://tropical.colostate.edu/Forecast/2026-MMDD.pdf` — **schedule: Aug 5 · Aug 19 · Sep 2 · Sep 16 · Sep 30.**
> ⚠️ **This file and `AGENT.md` both asserted "CSU issues no further 2026 updates — from here the read is basin observation, not outlook revision." That was FALSE**, and it cost me the **8/19 issuance**, which landed inside my 8/13–8/21 dark window. **A declared-dead instrument is the inverse of the ACE / Duisburg failure and is harder to catch: a gap you have written down as closed generates no further looking.** When you retire an instrument, say *which* product you verified as ended — the seasonal series had ended; the two-week series had not.
> **CSU 8/19 (window Aug 19 – Sep 1): BELOW-NORMAL 70% · near-normal 28% · above-normal 2%.** Terciles **for this window**: `<7 / 7-22 / >22` ACE. Verbatim: *"the base state across the Atlantic is quite TC-unfavorable, given the strong El Niño and associated high levels of vertical wind shear."*
> **8/5 window (Aug 5-18) is now gradeable:** forecast below-normal (`<2` ACE) at 80%; **observed Atlantic ACE Aug 5-18 = 0.4425.** Inside the tercile.
> ⚠️ **TERCILE BOUNDARIES DIFFER PER WINDOW** (Aug 5-18 below = `<2`; Aug 19-Sep 1 below = `<7`). **Never compare the LABEL across windows** — "below-normal" is not a constant quantity. **Next issue: 2026-09-02.**
> ⚠️ CSU's page also carries a self-contradiction — *"Additional forecast updates will be released on August 5th"* (already past) beside a schedule block listing Nov verification next. **That line does not imply a pending seasonal update.**

### NOAA CPC seasonal hurricane outlook
`https://www.cpc.ncep.noaa.gov/products/outlooks/hurricane.shtml` — **May initial, early-August update.**
**Verified 2026:** **8/6 revised DOWN to 7-13 / 2-6 / 0-2, 75% below-normal** (from 55%).

⚠️ **BOTH August updates revised AGAINST an active season.** My pre-registered escalation line *"CSU or NOAA revise UP"* did not merely fail to fire — **it fired backwards.** Record revisions in both directions; a trigger that can only fire one way is not a test.

### ✅ ACE — GAP CLOSED 2026-08-13. **Compute it; do not scrape it.**

CSU's real-time page is a dead end (**404**, 6.5 KB shell). **The fix was to stop looking for a page that reports ACE and compute it from NHC best-track data**, which makes both legs primary, reproducible, and base-rateable.

**ACE** = Σ v²/10⁴ over 6-hourly synoptic times (00/06/12/18 UTC) for systems at **TS/HU/SS status and ≥34 kt**.

#### Leg 1 — the DENOMINATOR (1991-2020 normal) ✅ computed 8/13
```bash
curl -sL "https://www.nhc.noaa.gov/data/hurdat/hurdat2-1851-2024-040425.txt" -o hurdat.txt
```
**Result: 1991-2020 Atlantic ACE normal = `122.6`.**
✅ **Validation the parse is correct:** the same computation returns **14.4 mean named storms and 7.2 mean hurricanes** — which match NOAA's *published* 1991-2020 normals (14 / 7). **If those two match, the ACE figure is trustworthy.** Re-run this check after any HURDAT2 re-release.
⚠️ **HURDAT2 is finalised post-season and currently ends 2024** — it is the denominator source, never the current-season source.

#### Leg 2 — the NUMERATOR (season to date) ✅ computed 8/13
```bash
curl -sL "https://ftp.nhc.noaa.gov/atcf/btk/"            # lists bal<NN><YYYY>.dat
curl -sL "https://ftp.nhc.noaa.gov/atcf/btk/bal012026.dat"
```
Parse `tau == 0` rows, dedupe by timestamp, apply the same status/≥34 kt filter.
**2026 season to date = `3.09`** — Arthur 0.40 · Bertha 2.24 · Cristobal 0.44 · three INVEST decks at 0.00.
⚠️ **b-decks include INVEST (AL9x) entries that contribute 0** — keep them in the loop, they are not errors.

#### The bands, now anchored to a real number
| | % of normal | **ACE units** |
|---|---:|---:|
| **AEO-01 criterion** | <90% | **<110.3** |
| Yellow | ≥110% | 134.8 |
| Orange | ≥130% | 159.4 |
| Red (+landfall) | ≥150% | 183.9 |

#### 🔑 The seasonal-accrual base rate — without it, "% of normal" mid-season is meaningless
**Only ~10.8% of seasonal ACE has normally accrued by Aug 13** (median 10.0%, range 0.5–29.5%). So a normal season stands at **~13.2** on this date; **2026 is at 3.09 = 23.4% of the to-date normal**, ranking **7th-lowest of the 30 years**.
⚠️ **Never compare season-to-date ACE against the FULL-season normal** — "2.5% of normal" on 8/13 sounds like collapse and is mostly just the calendar.

---

## LOSS LEG (shared with `../wildfire/SOURCES.md` — same publishers)

| Source | Gives |
|---|---|
| **Gallagher Re / Munich Re / Aon** cat reports | H1 & full-year insured nat-cat vs 10-yr avg |
| **Artemis.bm** | reinsurance ROL, renewal pricing, cat-bond issuance |
| **Guy Carpenter** ROL index | the renewal-pricing series |

⚠️ **Commercial publishers on their own schedule** — H1 lands ~Jul-Aug, full-year ~Jan. **Between publications the loss leg is genuinely stale; label it rather than substituting a peril figure.**
⚠️ **NOAA NCEI's billion-dollar disaster DB was DISCONTINUED (Jul 2025)** — do not cite it (L-05).

---

## KNOWN TRAPS

| Trap | Guard |
|---|---|
| High formation % read as the trigger | **Trigger needs GULF/FL.** Graded on the letter twice this month. |
| Percentages without the prose | 8/13: **80% + "expected to weaken."** The prose had the mechanism. |
| `CurrentStorms.json` is all-basin | Filter before saying "Atlantic." |
| Active basin ⇒ hard market | **Peril ≠ loss.** Opposite directions right now. |
| Comparing to-date ACE to the FULL-season normal | **Only ~10.8% accrues by Aug 13.** Use the to-date normal (~13.2), not 122.6. |
| Scraping a page for ACE | **Compute it from HURDAT2 + ATCF b-decks.** CSU's real-time page is a 404 shell. |
| A quiet season kills the thesis | It kills **C1's read only**; migrate to C3/C5/C6 and say so. |
