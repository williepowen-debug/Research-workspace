# 2026 bank failures: the six, at the FDIC primary

**REGINALD · 2026-10-10 Sat ~15:1x ET (Will asked: "We have had 6 bank failures this year. REGINALD has that data, right?").**
**As of:** FDIC Failed Bank List, page "Last Updated: September 25, 2026" (CSV `https://www.fdic.gov/bank-failures/download-data.csv`, pulled 10/10). **This is a dated snapshot. A 7th failure makes it stale; re-pull the CSV, never count from this file.**

## Answer

**Six, confirmed.** Before today the desk did NOT hold them as one list: five were named in a CREED packet (8/28), Nano Banc had a full forensic report (9/27), and Metropolitan was the original hidden-CRE example. This file is the first place all six sit together.

| # | Closed | Bank | Where | FDIC cert | Total assets | Est. cost to the FDIC fund | Acquirer |
|---|---|---|---|---|---:|---:|---|
| 1 | Fri 1/30 | Metropolitan Capital Bank & Trust | Chicago, IL | 57488 | $261.2M | $19.6M | First Independence Bank |
| 2 | Fri 5/1 | Community Bank and Trust – West Georgia | LaGrange, GA | 25796 | $305.7M | $97.3M | Anchor Bank |
| 3 | Fri 7/10 | Kentland Federal S&LA | Kentland, IN | 28722 | $3.8M | $1.2M | Kentland Bank |
| 4 | Fri 7/17 | Small Business Bank | Lenexa, KS | 25744 | $72.9M | $5.7M | Farmers State Bank of Oakley, KS |
| 5 | Fri 8/21 | Tioga-Franklin Savings Bank | Philadelphia, PA | 33802 | $68M | $5.5M | Second Federal S&LA of Philadelphia |
| 6 | Fri 9/25 | **Nano Banc** | Irvine, CA | 58590 | $736M | $114M | Sunwest Bank |
| | | **Total** | | | **≈ $1.45B** | **≈ $243M** | |

**Sources and basis:**
- Names, dates, certs, acquirers: the FDIC Failed Bank List CSV.
- Rows 1–4, assets and cost: FDIC BankFind failures API (`api.fdic.gov/banks/failures`, `QBFASSET` = assets at the last quarterly report before failure; `COST` = the FDIC's current estimated loss). ⚠️ **That API's index was built 2026-08-25 and returns only these four**, so it misses rows 5–6.
- Rows 5–6, assets and cost: the FDIC closing press releases. Assets are as of 6/30/26; the cost is the FDIC's preliminary estimate at closing.
- The two cost bases differ (current estimate vs estimate at closing).

## How unusual is six?

FDIC failures per year (same CSV):

| 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | **2026 YTD** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 5 | 8 | 0 | 4 | 4 | 0 | 0 | 5 | 2 | 2 | **6** |

- **By count: the most since 2017.**
- **By size: small.** About $1.45B of assets in total. Five of the six are under $310M; the 2023 failures included SVB (~$209B at failure).
- **None is in my 14-bank cohort or on Will's book.**

## What each one means for this desk

| Bank | Link to the desk | Where it is worked |
|---|---|---|
| Metropolitan Capital | The original hidden-CRE example: real estate loans reported as C&I. ⚠️ The 10.7% vs 61% figures are from a secondary source (`sources/Wright_Metropolitan_Capital_Bank_Failure_2026-02-01.md`) and **were never re-checked at the FFIEC primary**; `DECK_EVIDENCE.md` also carried the wrong cert (57120 = Uniti Bank) until today. | `DECK_EVIDENCE.md` |
| Community Bank and Trust – West Georgia | Not worked by this desk. Its estimated cost (32% of assets) is the highest ratio of the six. | — |
| Kentland · Small Business Bank · Tioga-Franklin | Sub-$100M; CREED (8/28): a different cohort from the $10–250B regionals my Q2 recognition reads are about. | CREED packet 8/28 (`inbox/processed/2026-08-28_from-CREED_…`) |
| **Nano Banc** | **The one with a mechanism I have worked:** loss on asset marks ≈ $120M ≈ 17% (desk scenario); 79% of C&I in Memo-3; litigation. Markers are n=1, not adopted. | `reports/2026-09-27_nano-banc-failure-forensics.md`; P&A re-check Tue 10/13 |

⚠️ **Caveat on the count as a signal:** these are small banks failing one at a time on bank-specific causes (Nano: litigation and asset marks). Six is a count, not a channel. A failure among the 14 cohort names, or a pattern in cause across them, would be the signal; neither is present.

## Method

`curl` the CSV and the FDIC press-release / failed-bank pages (User-Agent set); `api.fdic.gov/banks/failures?filters=FAILYR:2026` (the old `banks.data.fdic.gov` host now 301-redirects there). Per-year counts: closing-date column of the CSV.
