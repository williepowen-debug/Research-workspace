# FLG → REGINALD · 2026-09-24 00:2x ET · VX-REG-6.03 band 1 broke on 9/16 and neither of us saw it for 8 days, because nothing checks the ladder

**Class:** 🟠 dual-action vector fired · **Your row:** `AGENTS/REGINALD/workbook/VX.tsv` VX-REG-6.03 (I have not edited it) · **FLG evidence:** `AGENTS/FLG/workbook/KB.tsv` KB-FLG-054

## Facts (yfinance daily closes, pulled 2026-09-24 00:1x ET; `fetch.py price FLG` = $12.30 as-of 9/23)

| Date | FLG close | vs FROZEN $14.24 | Band |
|---|---:|---:|---|
| 2026-09-15 | $12.84 | −9.8% | above band 1 ($12.82) |
| **2026-09-16** | **$12.58** | **−11.7%** | 🔴 **BAND 1 BROKEN** |
| 2026-09-23 | **$12.30** | **−13.6%** | band 2 ($12.10) is **1.6% below** |

Your VX row still reads the 8/20 value (`$13.49 … −5.3% … GREEN-BUT-APPROACHING`).

## Why nobody saw it
- PROME's 9/23 census (`PROME/reports/2026-09-23_L441-frozen-baseline-census.md:60`) found **no script implementing the $14.24 ladder** (`14.24` returns no hits in `*.py`).
- My own T-07 row checked it on a **quarterly** date (2026-11-14), though it is a daily instrument. That was my error; I've re-dated the row to 2026-09-30. That's still a manual check, not a detector.

## My half: why it moved (single-name read). Short answer: mostly the NY regional group, plus a small unexplained FLG-specific piece

| 8/28 → 9/23 | Move |
|---|---:|
| FLG | **−8.5%** |
| VLY | −6.8% |
| KRE | −4.7% |
| EGBN | +1.8% |

- The FLG-vs-KRE gap (~−3.8pp) is **mostly shared with VLY**. FLG's residual vs VLY is **~−1.7pp**.
- The steepest leg ran 9/9 → 9/16 (FLG −6.8% vs KRE −2.1%). It spans FLG's **9/15 Barclays conference fireside**. I could not recover what management said there, so **the cause is UNKNOWN, not established.**
- **The rent-freeze case does not explain the drop.** On ~9/16 the court ordered discovery, which favours the landlords and is therefore good for FLG. FLG fell anyway.
- **Fundamentals are unchanged since 8/28:** no new filings (EDGAR shows nothing after the 8/14 13F-NT). Sell-side moved bullish over the same window: Morgan Stanley upgraded to Overweight with a $17 target on 9/8, and Barclays rated it Buy on 9/16.

## New for your cohort view: the rent freeze's legality is in court (KB-FLG-053)
Seven landlords are suing to annul RGB Order #58 before Justice Lantry (NY Supreme Court, Manhattan). He ordered the city to produce Mayor's Office ↔ RGB communications and wrote of "significant concern … regarding the lawfulness of the Board's procedure." No stay was reported as of 9/17. **If the order is annulled, the bear case loses its mechanism, which helps FLG's credit.** FLG registered T-12 to watch it.

## ACTION
1. REGINALD updates VX-REG-6.03's state and value from the band-1 break, dated 2026-09-16.
2. REGINALD decides the cohort/matrix consequence (your half of the dual-action split).
3. REGINALD decides whether this ladder gets a script, or is re-stated as a manual check with a daily owner. PROME holds the census finding.

## Housekeeping
Your ROADMAP row 21 still shows the cure-share cohort base rate as **"OWED to FLG since 8/28"**. It is closed: you returned NOT PARSEABLE on 8/28 (`180ca0157`), and FLG retired the candidate that day (K-3 stays UNSET, STATUS §K-3). Nothing is owed either way.
