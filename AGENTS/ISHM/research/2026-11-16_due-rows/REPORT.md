# ISHM due-row session — 2026-11-16

**Assignment:** PROME prome-6f desk-catalyst summons (WQ-184 class); PROME's words, not Will's. Runtime: Claude Code, Opus 5.5 (claude-opus-5-5). Started 10:18 ET Monday 2026-11-16 by the system clock.
**Boot:** `boot.py` rc 1 (three rows due today, IP tomorrow; known carries: PRINTS row 47 AAR-BREADTH date, VX-ISH-08 unscored); corrections check rc 0; FRED current on all 7 series. Checkout equal to origin/master after fetch; no pull needed (other desks' dirty files present, untouched).
**Rules applied:** graded only by the desk's own written rules; no level, band, threshold, score or trade changed.

## Row results

| Row key (docket/CATALYSTS.tsv) | Result | Basis |
|---|---|---|
| `2026-11-16 [CASS-SHIP] Cass Freight Index, Oct 2026` | **PUBLISHED, GRADED. Row retired** (successor row 2026-12-14 already registered; its note now carries the issuer's own rule) | Report page HTTP 200 at 10:19 ET (`sources/cass_october-2026_report_read1019ET.html`); historical XLSX (`sources/cass_historical_1116.xlsx`). Shipments 1.056 NSA, **+5.9% y/y** (1.056 vs 0.997 = +5.918%), two-year stack −2.3%, NSA m/m −0.6%, **SA m/m +1.7%** (1.04022), third straight SA gain. Expenditures 4.01, +26.5% y/y (price/volume/fuel, not volume). Prior months unrevised: 35 sample y/y values match the new XLSX, max difference 0. **Release day:** page body undated; HTTP `Last-Modified: Fri, 13 Nov 2026 22:40:34 GMT` (17:40 ET) for the page, 22:20 GMT for the XLSX, so it posted after our 10:19 ET 404 that morning. Issuer rule as printed on the page: "We strive to release our indexes on the 13th of each month. When this falls on a Friday or weekend, our goal is to publish on the next business day." |
| `2026-11-16 [EMPIRE] NY Fed Empire State Manufacturing Survey, Nov 2026` | **PUBLISHED, GRADED. Row retired** (successor row 2026-12-15 registered) | Issuer PDF `2026_11_empire-state-manufacturing-survey.pdf` and SA diffusion CSV agree (`sources/`); responses collected November 2–9; read 10:19 ET (08:30 ET is the issuer schedule, not observed). See § Empire |
| `2026-11-16 J2 base-rate sample: add matured months only` | **October month added; no forward window matured; counts unchanged.** Re-dated to 2026-12-14 (November Cass month plus the August forward window, which matures when November completes) | See § J2 |

## Cass — J2 freight leg

| Item | Value | Basis |
|---|---|---|
| Shipments y/y, October | +5.9% (September +1.9%, August +2.1%) | PRIMARY-VERIFIED, NSA |
| Shipments SA m/m | +1.7%, third straight gain | PRIMARY-VERIFIED, issuer SA |
| Issuer's reasons | easy comparison to late-2025 trade-war effects; holiday restocking; "to some extent" the IEEPA tariff refunds; slow retail and industrial growth | issuer judgment |
| Issuer's November expectation | about +3% y/y on normal seasonality | issuer judgment, not a forecast of ours |

**Proposed J2 deterioration test** (unregistered; `workbook/EXIT_PROTOCOL.md`): negative Cass y/y on two consecutive releases plus a negative four-week AAR comparison. October +5.9% → **NOT-MET.** AAR was not re-read: with Cass positive the test cannot fire whatever rail shows. ⚠️ Part of the October gain is a base effect and one-time refunds by the issuer's own account; the two-year stack is still −2.3%, so volumes are recovering toward, not above, 2024 levels.

## Empire — November

| Index (SA diffusion points) | November | October |
|---|---|---|
| General business conditions | **7.8** | 25.5 |
| New orders | **3.0** | 23.2 |
| Shipments | 8.8 | 13.1 |
| Unfilled orders | 10.3 | 14.0 |
| Delivery times | 13.8 | 19.8 |
| Inventories | 9.2 | 11.6 |
| Employees | **18.1** (highest since June 2022) | 10.3 |
| Prices paid / received | 45.9 / 27.2 | 59.5 / 30.6 |
| Supply availability | −9.2 | −15.1 |
| Future general / future capex | 28.9 / **23.0** (capex highest since December 2022) | 21.0 / 14.0 |

**Grade by the written rule** ("Regional composite sign", band OWED): sign **positive**; no regional band is registered, so nothing fires. November breadth so far: 1 of 5 districts reported, 0 negative (Philadelphia and Kansas City November 19, Richmond November 24, Dallas November 30). The unregistered "≤1 of 5 negative" description cannot be read until all five are in. October values unrevised.

**Composition (read against the question, not a verdict):** orders cooled hard (23.2 → 3.0) while hiring jumped and capex plans rose. That is one district, one month; it fits "strong but slowing" and does not separate real demand from borrowed. Prices paid → CARL's figure; employment → LABOR's.

## J2 — matured months only

Script `j2_october_add.py` reads the 2026-11-13 sample unchanged and appends one row; outputs `J2_monthly_sample_2026-11-16.csv`, `J2_BASE_RATES_2026-11-16.json`. HY input is the 2026-11-13 FRED pull (October complete in it); no fresh pull was needed because no new window matured.

| Item | Value |
|---|---|
| October 2026 Cass y/y | +5.92% → freight-up, enters no freight-down denominator |
| October trailing three-month HY change | +47.9 bp (July 2.743% → October 3.222%) |
| Forward windows matured today | none (August's target month, November, is incomplete) |
| Freight-down counts | forward 28/33 at ≤25 bp, 19/33 at ≤0, 31/33 at ≤50; trailing 26/30, 18/30, 28/30 — **all unchanged** |

The widening of August–October ran while freight was rising, so it is not freight-led. Descriptive only; LIQUID owns the spread read, RED the probability read.

## Inbox — every lane

| Lane | Contents | Disposition |
|---|---|---|
| `inbox/` top level | `PROTOCOL.md` only (standing protocol file, not a packet) | Nothing to process. PROME's census count of 1 matches this file |
| `inbox/WALTER/` | empty (only `processed/`) | Nothing to process |

## Tomorrow — G.17 industrial production, October (P1, 2026-11-17 09:15 ET)

Not pre-graded. The desk wants to be tapped for it: it is the first measured October output figure against October's survey strength (VX-ISH-02), and the annual revision follows on November 24.

## Routing

- LIQUID, RED: J2 result at the Cass print (routing table, P2) — Cass +5.9%, test NOT-MET, counts unchanged.
- TERRY: **no packet.** No material finding: Cass confirms the freight recovery already on record, Empire is one district inside an unregistered band, and the J2 counts did not move.
- PROME: delivery packet `PROME/inbox/2026-11-16_from-ISHM_due-rows.md`.
