# Bank CRE modifications series (FDIC RSNRES + its troubled buckets) — adopted as the `VX-CREED-8.01` aggregate

**Written:** 2026-10-22 (Thu) 17:33 ET · **Authorization:** Will, 2026-10-22 17:30 ET, *"okay go ahead now"*, on CREED's suggestion (17:24): *adopt RSNRES as the modifications measure, tracked as a paired series with its past-due/nonaccrual fields, no threshold band yet.* **No score, band or trigger moved; S4 stays 2; `CREED-T-04` stays qualitative.**
**Data:** `research/data/2026-10-22_fdic_restructured_nfnr_series.tsv` (62 quarters, 2011-Q1 → 2026-Q2; FDIC BankFind API `financials`, aggregated by report date, pulled 10/22). Method positive-controlled: the API's Q2-26 sum ($10,657,179k) equals CREED's institution-by-institution sum exactly.

## 1. What the fields are

| Field | FDIC title | Meaning |
|---|---|---|
| `RSNRES` | "RESTRUCT LN - NONFARM NONRES" | modified nonfarm-nonresidential (office, retail, industrial, hotel; not multifamily, not construction) loans **performing** under modified terms |
| `P3RSNRES` / `P9RSNRES` | "30-89 / 90+ DAY P/D RESTRUCT NFNR LN" | the same modified loans, past due |
| `NARSNRES` | "NONACCR RESTRUCTURED NFNR LN" | the same modified loans, nonaccrual |
| `LNRENRES` | "RE NONFARM NONRESIDENTIAL PROP" | all nonfarm-nonres loans (the denominator) |

Titles PRIMARY-READ from FDIC's API dictionary (`risview_properties.yaml`; its description fields are empty). The longer definition ("in compliance with modified terms") is from FDIC's financial-reports workbook, read by a CREED research agent. The Call Report codes (RC-C Memo 1.e) are an inference, not verified.

## 2. Two artifacts that decide how it may be read

1. **Semiannual reporting — VERIFIED by CREED.** Banks with a non-zero `RSNRES` number 732–799 in June and December but 287–327 in March and September in every quarter checked on the current basis (all of 2025, H1 2026); the pattern holds on the old basis too (Q3-22 430 vs Q4-22 1,154). About 450 smaller banks report the item twice a year and show zero in Q1/Q3. ⇒ **Compare June with June and December with December only.** A Q1 → Q2 rise is mostly those banks returning. *(This corrects `KB-CREED-067`'s "+7.8% QoQ".)*
2. **A definition break at 2023-Q1 — PRIMARY-CITED.** ASU 2022-02 retired troubled-debt restructurings. Since adoption, banks report "loans modified since adoption of the new standard to borrowers experiencing financial difficulty that are performing in accordance with their modified terms" (Call Report instruction text as reproduced in an OMB filing, via search; FFIEC and OMB pages refused automated fetches). The series fell from $4.77B (Dec-22) to $1.77B (Mar-23) and rebuilt. ⇒ **Pre-2023 values are a different object (TDRs): context only, never one series with the post-2023 values.**
   - ⚠️ **UNVERIFIED:** a forum post says modified loans are reported only for 12 months after modification. If true, the series is close to a **trailing-12-month flow** of new modifications; if not, it is a stock that started from zero in 2023. Which one it is changes the reading of the peak (§3).

## 3. The valid series (June/December, post-2023 basis, $B)

| Print | Performing modified | Troubled modified (30+ PD + nonaccrual) | Total modified | Performing as % of all NFNR loans |
|---|---:|---:|---:|---:|
| Jun-23 | 4.36 | 1.81 | 6.16 | 0.241% |
| Dec-23 | 8.37 | 3.68 | 12.05 | 0.459% |
| Jun-24 | 9.74 | 4.49 | 14.23 | 0.529% |
| Dec-24 | 13.14 | 5.90 | 19.04 | 0.711% |
| **Jun-25** | **14.73** | **6.66** | **21.39** | **0.786%** |
| Dec-25 | 11.25 | 5.85 | 17.10 | 0.588% |
| **Jun-26** | **10.66** | **4.13** | **14.79** | **0.546%** |

**Reading, with the denominator named (trap #6):** NFNR loans grew steadily ($1.805T → $1.952T), so the share and the level move together. Every column **peaked at Jun-25 and has fallen for two half-years:** performing −27.7% YoY; troubled −38%; total −31%.

**What the fall can mean (not graded; three explanations, each consistent):**
- (a) banks are **modifying fewer troubled CRE loans** (tighter terms, the Glancy 2026 large-bank finding, `KB-CREED-053`). That is less extend-and-pretend, so problem loans resolve by payoff, sale or default instead.
- (b) modified loans **leaving** the series by payoff, charge-off or foreclosure, or by aging out if the 12-month rule holds.
- (c) **cures**: troubled borrowers recovering.
Explanations (a) and (b-default) point toward recognition; (c) points toward healing. **This series alone cannot tell them apart.** The troubled bucket falling faster than the performing one argues mildly against re-default rising (the vector's ORANGE leg).
**The 2023–24 rise is at least partly definitional** (the stock refilling from zero after adoption), so the Jun-25 "peak" may not be a stress high: do not call it one.

## 4. How it is wired (what changed)

- `VX-CREED-8.01` now carries this paired series as its aggregate (value, source, notes). **Status stays YELLOW.** Its bands were written in words before any series existed ("2nd-mod rise" / "re-default rise" / "mod volume falls"). "Mod volume falls" reads literally on §3, but the fall is not attributable (§3), so a literal re-grade to RED would be a word match, not a reading. **Band calibration to this series is owed to Will**: on the June/December basis, n=12 is reached only at Dec-2028 (n=7 now).
- `VX_HISTORY.tsv`: seven `CANONICAL` rows (2023-Q2 … 2026-Q2, half-yearly), basis named. Pre-2023 values are left in the data file only.
- `CREED-T-04` (CMBS re-default / 2nd-mod rate) is a different perimeter (CMBS, not bank) and is not touched.

## 5. Limits that travel with every citation

Bank-reported only (no CMBS, CLO, debt funds); excludes multifamily and construction; the definition changed in 2023; the 12-month window is unverified; Q1/Q3 prints are incomplete. **Next print: Dec-2026 (published ~late Feb 2027).** The Q3-26 print (~late Nov) covers only the quarterly reporters and must not be compared with Jun-26.
