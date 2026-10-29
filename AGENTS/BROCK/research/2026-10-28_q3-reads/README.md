# 2026-10-28 Q3 reads — ARCC (WQ-511 first read), OCIC Q3 final, ARCC–MFIC merger, CRMT backstop #5

Read by BROCK (Claude Code, Opus 5.5) 2026-10-28 ~23:38–23:47 ET from EDGAR primary.

## Sources (EDGAR, fetched 2026-10-28 ~23:41 ET)
| Doc | Accession | Accepted (submissions JSON, ET-ambiguous) |
|---|---|---|
| ARCC Q3 10-Q (SOI + XBRL) | 0001628280-26-067383 | 2026-10-27T10:20 |
| ARCC 8-K 2.02/8.01 (Q3 release, Ex 99.1; Q4 div $0.48) | 0001628280-26-067382 | 2026-10-27T10:14 |
| ARCC 8-K 1.01/7.01 (MFIC merger agreement dated 10/26) | 0001104659-26-118958 | 2026-10-27T10:12 |
| OCIC SC TO-I/A (FINAL amendment, Q3 tender) | 0001628280-26-067327 | 2026-10-26T21:23 |
| OCIC 8-K 3.02/8.01 | 0001812554-26-000057 | 2026-10-23T20:04 |
| CRMT (CIK 799850): no filing after 0001171843-26-006742 (10/21) | — | feed read 2026-10-28 ~23:40 ET |

sha256 ARCC 10-Q html c61498077cb0bfa1c4fd9559509a1f0a7f00fbf7a80ca5c6dd9ff16a21a3b055 · XBRL instance a79405ddd37740cab50e3902422cc32a35073306d3ddf4e7cdd985baf388d432

## Method (ARCC software)
Unchanged WQ-511 pipeline: `research/2026-10-23_bdc-software-exposure/scripts/soi.py ARCC <html> <xml> 2026-09-30 <out>`, then `metrics.py` logic with only SP and CUT changed (CUT ARCC = 1913, the row of the first SOI "Total Investments" at 9/30; 6/30 used 1930). SOI FV 29,212M ties to balance-sheet total investments at FV $29,213M. Label = ARCC's own "Software and Services" (broader than "Software").

## ARCC software, original convention (Experiment A cells in catchups/2026-10-28.md)
| Metric | 6/30/26 | 9/30/26 |
|---|---|---|
| Software FV / cost | 6,451.2 / 6,793.0 = 0.950 | 6,303.8 / 6,662 = 0.946 |
| Software debt FV/par | 0.958 | 0.954 |
| Share of software debt PAR marked <80 | 4.2% | 7.4% |
| Share of software debt PAR marked <90 | 11.6% | 11.7% |
| Issuers <80 / <90 (of n) | 3 / 10 (114) | 3 / 10 (112) |
| Worst: Pluralsight FV/par | 0.479 | 0.392 |
| Software FV % of NAV | 46.4 | 45.2 (6,303.8 / 13,946 total stockholders' equity) |
Reading guide (WQ-511 REPORT §2): FV/cost down ≥2 pts OR <80 share ≥8% = first confirmation. **Neither met.**

`ARCC_metrics_2026-09-30.json` = full output (soft + rest + worst names).
