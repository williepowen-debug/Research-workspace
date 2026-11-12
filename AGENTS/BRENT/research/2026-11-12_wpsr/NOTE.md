# BRENT: EIA weekly report, data week November 6 (Veterans Day release), graded at BRENT's letters

**Run:** 2026-11-12, release read 12:10:59 EST, files saved 12:11:01 EST (from `date`, `capture.txt`). Session brent, Claude Code, Opus 5.5, woken by PROME on Will's word (11:53 ET). No trade, no card, no gate, band or threshold changed. Release-day bytes and sha256 in this folder; arithmetic in `evaluate.py` → `evaluation.json`.

**Release time:** EIA schedule page (read 11:54 EST): data week November 6, 2026 → Thursday November 12, **12:00 p.m.** (Veterans Day). The page lists no 14:00 ET release; PROME's second time is unconfirmed here. The 12:00 files were complete at 12:11 (psw01 carries week 11/6). A discretionary 14:00 re-read (not a second release; PROME's 14:00 time was PROME's error) compares hashes only. **Re-read done 14:01:21 EST (from `date`):** psw01.xls, table1/2/4.csv and summary.txt re-fetched from ir.eia.gov are all byte-identical (sha256) to the 12:11 files. No grade changes, so no second packet.

## Bottom line

US stocks built across the board in the week to November 6: commercial crude **+4.657M**, distillate **+4.071M**, gasoline **+1.799M**, total commercial **+11.359M** [CONF EIA table1.csv]. Refiners ran at **95.2%**, the first print above my 95% alert line in this desk's recent run history (94.5% last week was the closest). It is the first large measured build in a print since the STEO flipped Q4 to a 1.47 mb/d global build, but it is one US week, not the global balance. Gasoline four-week demand fell **−1.0346%** year on year, mostly because a strong week last year entered the base. No forecast resolved.

## Rows graded

| Row | Letter | This print | Result |
|---|---|---|---|
| **BRT-31** week five (w/e 11/6) | MET on two consecutive ≤ −1.5%; NOT MET at window end only if every print > −1.0% | **−1.0346%** exact (8,728.75 vs 8,820.0 kb/d; current 8767, 8808, 8358, 8982; base 9028, 8874, 8924, 8454) | **NON-QUALIFYING, streak 0.** ⚠️ **First window print at or below −1.0%, so NOT MET is no longer reachable.** Remaining end states: MET, NO-VERDICT, NOT-FIRED-PRECONDITION or NO-VERDICT-CONTAMINATED. No revision to prior inputs against the 10/28 capture |
| BRT-31 price leg | GASREGW Monday after the data week vs 364 days earlier; 3rd window week < +20% ⇒ NOT-FIRED | 11/9 **$3.995** vs 2025-11-10 **$3.056** = **+30.73%** (EIA weekly retail, same survey, the letter's fallback) | Counter **0 of 3**. NOT-FIRED now needs all three remaining weeks under +20% |
| **BRT-34** first window print | WDISTUS1 strictly below 95,000 on any week 11/6 → 12/18 | **103,330** (prior 99,259, **+4,071**) | **NOT below; 8,330 above the line.** OPEN. Six prints left (11/13 → 12/18) |

**Why the gasoline figure fell (mechanism, not demand):** the current four weeks rose (8,639.0 → 8,728.75 kb/d, as 8,767 replaced 8,408 for w/e 10/9), but the base rose more (8,676.75 → 8,820.0) as last year's 9,028 entered. The single week is 8,767 against 9,028 (−2.9%). One print, ±15-point base caveats travel with BRT-31.

**What the next two prints need for MET (arithmetic, not a forecast):** w/e 11/13 is ≤ −1.5% if that week prints **≤ 8,890 kb/d** (base 8,838.5; 8,982 drops out). w/e 11/20 then also needs the 11/13 and 11/20 prints to sum ≤ 17,054 (average ≤ 8,527). Recent weekly range 8,358–8,982. The 11/27 base includes last year's Thanksgiving week (8,326).

## Alert lines (TRACKER registered block)

| # | Line | Week 11/6 | State |
|---|---|---|---|
| 1 | Cushing < 20.0M | **27.356M**, +0.106M | Not breached; 7.356M above |
| 2 | Weekly crude draw > 5.0M | **+4.657M build** (414.417M, 4% below 5-yr) | Not breached; a build |
| 3 | Refinery utilization > 95% | **95.2%**, +0.7pp; crude inputs **17.047 mb/d (+322 kb/d)** | 🟠 **CROSSED: first print above 95% in this desk's recent run history.** Record and flag; no gate, no capital line. Read: refiners running hard is the product-build mechanism (distillate +4.1M, gasoline +1.8M), the opposite of a supply squeeze at US refineries |
| 4 | GASREGW > $4.00 | $3.995 (11/9) | Below the line since 11/9 (BRT-35 CONFIRMED 11/10). Next print Monday 11/16 |
| 5 | SPR | **279.535M, −2.649M** | Record only. Largest weekly SPR fall in this run's recent prints; consistent with scheduled exchange deliveries (not verified as the cause) |
| 6 | Gasoline 4-week YoY | −1.0% (EIA rounded); exact −1.0346% | BRT-31 week five above |

**Context, record only:** crude production 14.013 mb/d (+10 kb/d); crude imports 6.698 (+325); crude exports **3.455 (−220)**, 4-week 3.857; product exports 7.543 (+347); weekly distillate product supplied 3.411 (−1,028; ordinary weekly volatility, 4-week +4.2% YoY); jet four-week +1.8% YoY; crude adjustment −466 kb/d. Distillate now 8% below the five-year average (13% last week).

## Theme logs reviewed (WQ-622 A; logging only, nothing moves)

| Theme | 11/12 review |
|---|---|
| diesel-buffer | Counterevidence added: distillate +4.071M to 103.330M, gap to 5-yr narrowed 13% → 8%; BRT-34 8,330 away. Member: FT Russian diesel exports doubled, none to the US (card 005, unverified, conflicts with S&P's 10/22 US cargo). Next review 11/19 |
| paper-physical-gap | Member: first large measured US build in a print (total commercial +11.359M, crude +4.657M). One US week, not the global balance. Next review 11/13 (IEA OMR) |
| yanbu-bypass | Members: Houthi Pumping Station No. 11 claim, no Saudi confirmation, intercepts, alerts lifted (card 026); Riyadh-airport claim (card 005); Lahij push toward Bab al-Mandab, map claim only, and CVN-71 projected 11/15–16 (card 032). No halt reported, BRT-32 letter not met. Next review 11/19 |
| gulf-flow-basis | No new member. Next review 11/13 (IEA OMR) |
| gulf-access-cost | No new member (Black Sea war-risk headline is not the Gulf). Next review 11/19 |

## BRT-33 window, November 12 (taken at closeout on PROME's ask)

`brt33/pull.py` (the 11/11 script with the date changed; raw at `brt33/raw/c1_*.json`, `brt33/window_c1.json`): BZF27 95.8278 − BZH27 91.5884 = **+4.2394** (both legs 2 of 2 bars with positive volume) [EST vendor proxy], read after the window at 15:35:44 EST from saved one-minute bars (the letter settles on bars saved inside the vendor's reach of about 8 days). Not under +3.5000. **Valid session; the count is 4 of 5** (11/6 not measurable; 11/9–11/12 valid). Eight are needed, or NO-VERDICT. F-a not crossed. M1−M2 +2.2877; January 3:2:1 $36.60; December HO−CL crack $91.33 [EST vendor proxy].

## Limits

Primary EIA files only (ir.eia.gov, eia.gov retail workbook). No consensus read. Weekly product supplied is volatile; single-week moves carry little weight. **Corrected 11/12 12:4x EST (CATO M12-4 via PROME):** an earlier version called week 11/6 holiday-shortened; Veterans Day (11/11) fell after the data week and delayed only the release, so no holiday effect on that week's demand is evidenced. The 14:00 ET time named by PROME is not on EIA's schedule page.
