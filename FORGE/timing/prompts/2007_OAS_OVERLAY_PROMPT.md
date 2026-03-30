# Research Prompt: 2007 vs 2026 HY OAS Overlay

## Objective

Build a precise daily comparison of high-yield credit spread behavior in 2007 vs 2026 to determine: **where are we in the credit cycle relative to the 2007-2008 analog, and are we tracking faster, slower, or differently?**

## What I Need

### 1. Daily HY OAS Data — 2007 Full Year

Pull the **ICE BofA US High Yield Option-Adjusted Spread** (FRED series: BAMLH0A0HYM2) for every trading day in 2007. I need:

- Date
- OAS level (bps)
- Daily change
- Cumulative change from Jan 1 2007

Key dates to flag explicitly:
- When did OAS first cross 300? 320? 350? 400? 500?
- What was OAS on the day of each major event (Bear Stearns hedge funds Jun 7, BNP Paribas Aug 9, Northern Rock Sep 14, Citi writedown Oct/Nov)?

### 2. Daily CCC OAS Data — 2007 Full Year

Same series but for CCC-rated: **ICE BofA CCC & Lower US High Yield OAS** (FRED series: BAMLH0A0HYM2EY — or the CCC-specific series if available).

Key question: **Did CCC lead HY in 2007?** By how many days/weeks did CCC cross its thresholds before HY followed?

### 3. 2026 Comparison Points

For context, here's where we are now (as of March 30, 2026):
- HY OAS: ~342 bps
- CCC OAS: ~1,013 bps
- HY OAS crossed 300: approximately early March 2026
- HY OAS crossed 320: approximately March 17, 2026

### 4. S&P 500 Overlay — 2007

For each date in the 2007 OAS series, also pull the S&P 500 close. I want to see:
- When OAS crossed each threshold (300, 350, 400, 500), where was SPX relative to its eventual peak (Oct 9, 2007 at 1,565)?
- How many trading days elapsed between OAS crossing 300 and SPX peaking?
- How many trading days between SPX peak and SPX -10%, -20%?

### 5. Spread Velocity Analysis

Calculate the **rate of OAS widening** in 2007:
- Average daily change in each month (Jan-Dec 2007)
- Maximum 5-day, 10-day, and 20-day widening moves
- Were there periods of compression (tightening) within the overall widening trend? How long did they last? How much did OAS tighten before resuming the widening?

This is critical — I need to understand the **relief rally pattern within credit spreads**, not just equities. If OAS went 300→350→320→400, I need those dates precisely.

### 6. Issuance Freeze Data

At what OAS level did HY bond issuance effectively freeze in 2007?
- Monthly HY issuance volumes for 2007 (SIFMA or Dealogic data)
- Was there a specific OAS threshold where issuance dropped >50%? >80%?
- How many days between issuance freeze and the first major credit event?

## Output Format

**Table 1: 2007 OAS Milestone Timeline**

| Date | HY OAS | CCC OAS | SPX | Event | Days from OAS 300 |
|------|--------|---------|-----|-------|-------------------|

**Table 2: Threshold Crossing Dates**

| Threshold | 2007 Date | Days from 300 | 2026 Date | 2026 Days from 300 | Faster/Slower |
|-----------|-----------|---------------|-----------|--------------------|----|

**Table 3: Relief Rallies Within the Widening (2007)**

| Start Date | OAS at Start | Trough Date | OAS at Trough | Compression (bps) | Duration (days) | Then What? |
|------------|-------------|-------------|---------------|-------------------|-----------------|------------|

**Table 4: Monthly Spread Velocity (2007)**

| Month | Avg Daily Δ (bps) | Max 5d Move | Max 10d Move | HY Issuance ($B) |
|-------|-------------------|-------------|-------------|-------------------|

**Table 5: Credit → Equity Lag (2007)**

| Credit Event | OAS Level | Date | SPX on Date | SPX Peak Date | Lag (days) | SPX Drawdown at Credit Event |
|-------------|-----------|------|-------------|---------------|-----------|---------------------------|

## Key Questions to Answer

1. **Speed:** Is 2026 tracking faster or slower than 2007? We crossed 300 in early March and hit 342 by March 30 (~3-4 weeks). How does that velocity compare?

2. **CCC as leading indicator:** In 2007, did CCC spreads blow out before HY? Our CCC is already at 1013 while HY is only 342 — that gap feels abnormally wide. Was the CCC/HY ratio this extreme in 2007?

3. **Relief rallies in credit:** How many tightening episodes occurred between OAS 300 and OAS 500 in 2007? How deep and how long? This directly informs whether the current bounce is a 2-day or 2-week phenomenon.

4. **Issuance freeze threshold:** If issuance froze at OAS 400 in 2007, and we're at 342 now, how many weeks until we hit that wall? Once issuance freezes, how quickly does the cycle accelerate?

5. **Credit → equity timing:** Precisely how many trading days did credit spreads lead equities in 2007? The common claim is "~3 months." Is that accurate? Was it 60 days? 90? 120?

6. **The CCC divergence:** CCC at 1013 while HY at 342 means the quality spectrum is already bifurcated. Did this happen in 2007? If CCC blew out first and HY followed with a lag, that lag tells us something about how much time we have before HY accelerates toward 500+.

## What NOT to Do

- Don't give me monthly averages when I need daily data for threshold crossings
- Don't summarize — give me the actual dates and numbers
- Don't hedge with "it's different this time" caveats — I know it's different, I want the raw analog data so I can make my own adjustments
- Don't mix up HY OAS with HY total return or HY yield — I specifically need the option-adjusted spread

## Sources

- FRED (Federal Reserve Economic Data) for OAS series
- SIFMA for issuance data
- Bloomberg terminal data if available
- Academic papers on 2007-2008 credit cycle chronology (Gorton 2008, Brunnermeier 2009 are good references)
