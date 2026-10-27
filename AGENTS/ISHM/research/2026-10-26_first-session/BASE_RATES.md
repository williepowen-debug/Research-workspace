# ISHM — descriptive base rates, October 26, 2026

Reproduce with `.venv/bin/python3 AGENTS/ISHM/research/2026-10-26_first-session/reproduce_base_rates.py` from the repository root. Inputs are frozen CSV/XLSX snapshots in sources/. Outputs: BASE_RATES.json and J2_monthly_sample.csv. This is a dated analysis, not an installed collector or capital gate.

## Freight down without high-yield spread widening

Instrument: Cass shipments, NSA index, y/y change; ICE BofA US HY option-adjusted spread via the FRED BAMLH0A0HYM2 mirror, percent converted to basis points. Monthly OAS is the mean of available daily observations. Economic scale: comparable percentage volume changes and spread changes in bp, not Cass expenditure dollars. Missing observations are dropped, never scored as calm.

The Cass publisher workbook and FRED mirror agree exactly for **129 monthly levels, January 2016–September 2026**. ICE CSV returned **October 27, 2023–October 23, 2026**, even when a 1996 start was requested. Use only complete months, **November 2023–September 2026 (35 months)**. Start is imposed by the available joint history, not selected for a convenient result. October 2026 is incomplete and excluded. Cass y/y is negative in 33 of those months, predominantly one continuing freight downturn. A three-negative-month rule produces the same eligible observations here.

| Reference for HY widening | No widening / narrowing, ≤0bp | No material widening, ≤25bp | Alternative, ≤50bp |
|---|---:|---:|---:|
| Trailing 3-month monthly-mean change, freight y/y <0 | 18/30 (60.0%) | 26/30 (86.67%) | 28/30 (93.33%) |
| Forward 3-month monthly-mean change, freight y/y <0 | 19/32 (59.38%) | 28/32 (87.5%) | 30/32 (93.75%) |

Trailing eligibility begins February 2024 to avoid the partial October 2023 anchor. Forward endpoints mature only through June 2026, so July–September are excluded from that denominator. These are separate windows, not conflicting counts. The ≤25bp label does not mean literally no widening: the strict ≤0bp alternative is shown beside it. Current-vintage data, not real-time backtest; freight publication lags are not simulated. No assertion that freight caused either spread outcome. Broader episodes, GFC and COVID are absent from the joint sample. Do not publish confidence intervals as if the overlapping months were independent trials.

**Use:** qualify freight-based warnings and route physical evidence to LIQUID/RED. **Do not use:** register a credit threshold, alter RED's recession probability, or infer a trading edge from this small sample. Existing owner records: RED's published P(NBER recession beginning in calendar 2026) is a dated 4–12% range; LIQUID's market-price persistence is not itself financing restriction. Those remain their owners' judgments.

## Historical distributions for proposed physical-data bands

| Series and sample | n | p10 | p25 | Median | p75 | Latest | Negative months | Below −5% |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Core nondefense ex-aircraft orders, SA nominal y/y, February 1993–August 2026 | 403 | −7.284% | −2.030% | 4.036% | 9.085% | 14.106% | 132/403 | 57/403 |
| Cass shipments, NSA y/y, January 2017–September 2026 | 117 | −8.001% | −5.832% | −2.087% | 3.857% | 1.919% | 70/117 | 36/117 |
| FRED rail carloads RAILFRTCARLOADSD11, monthly SA y/y, January 2001–July 2026 | 307 | −8.439% | −3.111% | −0.148% | 2.174% | 0.594% | 158/307 | 62/307 |

Sample starts use the earliest returned level plus 12 months for a y/y change; the rail series is a monthly SA mirror, **not** the weekly NSA AAR four-week trend. Do not transfer its percentile directly to a weekly rule. Core orders are nominal: inflation, mix and revisions matter. These are unconditional monthly frequencies, not persistence-rule event frequencies. Proposed two-month rules need their own event counts before registration. Different sample eras and secular truck-to-rail mix limit commensurability. COVID observations remain in the full samples; recent-window/ex-COVID sensitivity is owed before any rule becomes a capital gate.
