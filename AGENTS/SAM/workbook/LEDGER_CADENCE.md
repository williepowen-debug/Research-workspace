# SAM ledger cadence declaration

**Source audit: September 14 ET / September 15 JST, 2026. Owner: SAM.** All 19 root workbook TSVs inspected for schema and source cadence. [Machine-readable inventory](../research/outputs/2026-09-14_stale-sweep/ledger-inventory.tsv) contains row counts, vintage and next check for every ledger. Frozen/archive rows are deliberately historical.

| Ledger | Class | Latest observation | Next check |
|---|---|---|---|
| `BIS_GLI.tsv` | LIVE quarterly | 2026-Q1 | Next BIS GLI quarter; check publication, not STATUS-write count |
| `BOJ_MEETING_OIS.tsv` | LIVE reviewed image | 2026-09-15 11:15 JST assumed | New image or Sep-18 00:00 JST expiry |
| `BOJ_OIS.tsv` | FROZEN 2026-09-08 | 2026-09-03 historical | None |
| `CFTC_JPY.tsv` | LIVE weekly | 2026-09-08 | 2026-09-18 release, September 15 positions |
| `CPI.tsv` | LIVE monthly | National Jul / Tokyo Aug 2026, 2025 base | National Aug Sep-18; Tokyo Sep Oct-02 |
| `FLOW.tsv` | FROZEN 2026-08-17 | Historical | None |
| `FLOW_ARCHIVE.tsv` | ARCHIVE | Historical | None |
| `FXY_OPTIONS.tsv` | LIVE snapshot | 2026-09-14 | Next snapshot |
| `GPIF_FLOWS.tsv` | LIVE quarterly | FY2026 Q1, 2026-06-30; released Aug-07 | FY2026 Q2, approximately November |
| `JGB_AUCTIONS.tsv` | LIVE per auction | 2026-09-08 5Y | 2026-09-15 20Y result |
| `JGB_YIELDS.tsv` | LIVE daily | 2026-09-14 | Next MOF business-day release |
| `KB.tsv` | LIVE event knowledge | Latest entry 2026-09-11 | Material evidence or correction |
| `KB_ARCHIVE.tsv` | ARCHIVE | Historical | None |
| `MOF_FLOWS.tsv` | LIVE weekly | 2026-08-30 through 2026-09-05 | 2026-09-17 usual Thursday cadence |
| `RATE_DIFFERENTIAL.tsv` | LIVE daily | 2026-09-14 | Next common US/JP source date |
| `TRADE_BALANCE.tsv` | LIVE monthly | 2026-07 kakusoku | 2026-09-16 August provisional |
| `USDJPY.tsv` | LIVE daily | 2026-09-14 completed session | Next completed London-labelled session |
| `VX.tsv` | FROZEN 2026-08-17 | Historical | None |
| `XCCY_BASIS.tsv` | FROZEN expired 2026-09-14 | 2026-09-10 | None; replacement feed not activated |

## GPIF accounting scope — necessary when using the existing schema

`asset_size_jpy_bn` is the GPIF headline total. The four allocation balances and percentages in the Q1 report include GPIF **and the Pension Special Account**. At June 30, headline ¥317,759.6B differs from the composition total ¥320,373.2B; approximately ¥2.6T of special-account assets explains the difference. Displayed components sum to ¥320,373.1B because of rounding. Do not “repair” either total to force equality. Hedged foreign bonds can be classified as domestic bonds; this table cannot identify UST holdings or transactions. See the [sweep assessment](../reports/2026-09-14_stale-sweep.md).

## Historical declaration

The September 1 disposition table, including then-open defects and obsolete next-release dates, is preserved in [the before-image](../research/outputs/2026-09-14_stale-sweep/before/workbook/LEDGER_CADENCE.md). A STATUS-write count is not a quarterly freshness clock. Missing an actual scheduled release still requires investigation.

**BIS revision control, September 14 sweep:** Q1 total ¥65.91T / loans ¥42.01T / debt securities ¥23.90T. The loader now upserts same-quarter revisions; USD values explicitly state the conversion convention. A matching quarter label alone does not establish freshness.
