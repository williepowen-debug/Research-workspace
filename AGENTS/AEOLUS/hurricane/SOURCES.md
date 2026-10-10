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
🔴 **CORRECTED 2026-09-28 — SUM `bal01`–`bal49` ONLY; EXCLUDE INVEST decks (`bal90`–`bal99`).** This line used to read *"b-decks include INVEST (AL9x) entries that contribute 0 — keep them in the loop, they are not errors."* **False on 9/28:** `bal90` and `bal91` each repeated a **40-kt row at the naming hour** (the invest's last fix duplicates the named storm's first), so summing every deck gave **9.9000 vs the correct 9.5800 — +0.32 double-count**. An invest that never becomes a named storm contributes 0 anyway (it rarely reaches 35 kt as an invest); one that does is already counted in its AL01–49 deck. **Excluding invests is correct in both cases.** *(KB-AEO-153.)*

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

> 🔴 **RE-CUT 2026-09-18 after the hurricane worker's gap #4: this section listed four PUBLISHER NAMES and no COMMANDS, while the peril leg above carries copy-paste commands throughout.** A worker cannot execute a publisher name, so **every loss figure was being reached by ad-hoc search rather than by a verified instrument — and that asymmetry is the structural reason the loss leg keeps going stale between vintages.** One command below is now verified; the rest are honestly marked as unresolved rather than left as names implying a route exists.

### ✅ VERIFIED — cat-bond insurance risk spread (the MID-CYCLE surface) · added 2026-09-18
**This is AEO-03's SEARCH instrument (KB-AEO-121). It is NOT the resolving instrument — that stays the Jan-1-2027 renewal ROL print.**
```bash
curl -s -A "Mozilla/5.0" -L "https://www.artemis.bm/catastrophe-bond-market-yield/"
# Full Highcharts series is INLINE in the page HTML — no JS execution needed.
# Regex the  categories:[...]  array, then each   name:'X' ... data:[...]   block.
# 827 weekly points, 2010-10-08 → present. Collated by Plenum Investments AG.
# Series: Insurance Risk Spread · Collateral Yield (3m T-Bills) · Expected Loss.
```
**Read 2026-09-18 (latest point 2026-08-28): spread 5.05% · EL 2.50% · multiple 2.02x · collateral yield 3.81%.**
> ⚠️ **TWO CAVEATS THAT TRAVEL WITH EVERY CITATION.** **① It is NOT rate-on-line** — a cat-bond spread and a reinsurance ROL are different instruments on different perimeters, correlated but not interchangeable. **NEVER enter it against the ROL threshold row.** **② It refreshes MONTHLY**, so the newest point runs ~3 weeks behind and **a landfall would not show for up to a month.** It is a between-renewals price surface, **not an event detector**.
> 🔴 **UN-BASE-RATED — and unlike the C5 Rhine trigger, this one CAN be base-rated before it is keyed (827 points exist). Build the base rate FIRST; do not register a band off the current level.**

> **Re-pull 2026-10-08:** 831 points, latest **2026-09-25** (4 new WEEKLY points since 8/28: 4.91 / 4.79 / 4.66 / **4.57**). The series is weekly; the PAGE refreshes in batches (~monthly) — so the lag is "up to ~4 weeks", not a monthly series. Year-ago 2025-09-26 = 5.48 → −16.6% YoY; 4.57 is the lowest point since 2020.

### ✅ VERIFIED 2026-10-08 — offshore SHUT-IN releases (energy theater; BRENT prices them)
```bash
curl -s -A "Mozilla/5.0" -L "https://www.bsee.gov/newsroom/latest-news/statements-and-releases/press-releases/mma-monitors-gulf-response-isaias"
# strip tags; the table sits after "Total Percentage of GOA": platforms evacuated, rigs, Oil BOPD shut-in + %, Gas MMCFD + %
```
**🔑 FIND THE LATEST RELEASE VIA THE ISSUER'S RSS — verified 2026-10-08 (aeolus-1008b) and 2026-10-09 (this read).** The index page is "Access denied", and update slugs are not guessable (10/7 = `…isaias`, 10/8 = `…isaias2`, **10/9 = `…isaias3`**):
```bash
curl -s -A "Mozilla/5.0" -L "https://www.bsee.gov/rss.xml" | python3 -c "
import sys,re
for it in re.findall(r'<item>(.*?)</item>',sys.stdin.read(),re.S):
    t=re.search(r'<title>(.*?)</title>',it).group(1)
    if 'MMA Monitors' in t: print(re.search(r'<pubDate>(.*?)</pubDate>',it).group(1),'|',t,'|',re.search(r'<link>(.*?)</link>',it).group(1))"
```
**Read 2026-10-09 (`…isaias3`, pubDate 14:11Z, operator reports as of 11:00 CDT 10/9):** oil **1,458,814 BOPD = 71.51%** · gas **1,259.2 MMCFD = 58.84%** · platforms **129 of 371 = 34.77%** · rigs 8 = 72.73% · DP rigs moved 2 = 11.76%. ⚠️ An absent item in the RSS means only that the feed does not list it. It does not prove that no release was issued.
**Issuer since 2026-07-10 = Marine Minerals Administration (BOEM + BSEE reunified), still on bsee.gov.** Read 10/8 (release dated 10/7, data as of 11:00 a.m. CDT): oil 511,619 BOPD = 25.08% · gas 350.25 MMCFD = 16.37% · 8 of 371 platforms.
⚠️ **The press-release INDEX returns "Access denied" (HTTP 200 shell)** — a missing later release is SEARCH-NOT-FOUND, never a verified absence. Update releases have taken new slugs in past seasons (`bsee-monitors-gulf-of-america-oil-and-48`, `…-53`); guessed Isaias update slugs 404'd 10/8. ⚠️ The issuer's rig table carried two slips on 10/7 (2/11 printed 18.8%; a 17-rig DP denominator labelled "non-dynamically positioned") — record as printed, flag, never "correct" silently.

### ✅ VERIFIED 2026-10-08 — Florida emergency orders (geography of a Florida event)
`https://www.flgov.com/eog/news/executive-orders` lists EOs with PDF links (`/eog/sites/default/files/executive-orders/2026/EO%2026-NNN.pdf`); extract the county list from Section 1 with pdfminer. EO 26-202 (10/6/2026, "Tropical Depression Nine") = 25 north-Florida counties. FDEM `floridadisaster.org` carries the storm update page.

### ⚠️ UNRESOLVED — no verified primary command exists for these
| Source | Gives | State 2026-09-18 |
|---|---|---|
| **Swiss Re Institute** sigma / H1 nat-cat | insured nat-cat vs long-term trend | 🔴 **HTTP 403 on two independent attempts** (WebFetch + `curl -A "Mozilla/5.0..."`). **Figures are SECONDARY-SOURCED ONLY — label them so; never silently upgrade to primary.** |
| **Gallagher Re** cat reports | H1 & full-year insured nat-cat vs 10-yr avg | 🔴 `ajg.com/gallagherre/news-and-insights/` returns **HTTP 200 with a 212-byte JS shell — no content.** Figures reached via Artemis / Reinsurance News reporting, **not the issuer.** |
| **Munich Re / Aon** cat reports | same | not attempted this run |
| **Guy Carpenter** ROL index | the renewal-pricing series | the canonical ROL series; **visible only at Jan/Jun renewals** |

⚠️ **Commercial publishers on their own schedule** — H1 lands ~Jul-Aug, full-year ~Jan. **Between publications the loss leg is genuinely stale; label it rather than substituting a peril figure.**
⚠️ **NOAA NCEI's billion-dollar disaster DB was DISCONTINUED (Jul 2025)** — do not cite it (L-05).
⚠️ **A MODELLED SCENARIO IS NOT A TALLY.** Swiss Re's 2026-09-16 Florida figures ($300bn+ Cat-5 Miami/Tampa, $200bn+ 1926 repeat, ~$100bn Andrew repeat) are scenarios and **must never enter the cat-loss band**. Same for any survey of *expectations* (Moody's 9/16 Jan-2027 −7.5% to −15%) — an expectation is not a transacted print.

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
