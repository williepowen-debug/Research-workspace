# Regional Bank SEC Filing Availability Triage — May 9

Source: `python3 FORGE/tools/filing-watch/poll_edgar.py --dry-run --lookback-days 10 --material-only` run after watchlist expansion on 2026-05-09 12:26 ET.

This is an availability note, not a full Call Report extraction. The SEC submissions API worked; direct filing-document fetches from this host may hit SEC automated-tool 403, so deeper extraction may need browser/manual access, adjusted SEC access, or an alternate source path.

---

## Watchlist Fix Completed

Expanded `FORGE/tools/filing-watch/watchlist.yml` to include missing REGINALD / portfolio names:

- SSB — SouthState Bank Corporation, CIK `0000764038`
- EGBN — Eagle Bancorp, Inc., CIK `0001050441`
- HBAN — Huntington Bancshares Incorporated, CIK `0000049196`
- CFG — Citizens Financial Group, Inc., CIK `0000759944`
- VLY — Valley National Bancorp, CIK `0000714310`

Result: filing radar now catches **VLY 10-Q, EGBN 10-Q, and CFG 10-Q** in the May 1-10 window.

---

## REGINALD Filings Detected

| Ticker | Form | Filed | URL | Monday use |
|---|---|---:|---|---|
| FITB | 8-K | 2026-05-08 | https://www.sec.gov/Archives/edgar/data/35527/000003552726000185/fitb-20260508.htm | Check if new event/financial supplement changes FITB residual put read. |
| ZION | 10-Q | 2026-05-07 | https://www.sec.gov/Archives/edgar/data/109380/000010938026000083/zions-20260331.htm | Highest priority for ZION kill/retain review. |
| VLY | 10-Q | 2026-05-07 | https://www.sec.gov/Archives/edgar/data/714310/000071431026000027/vly-20260331.htm | Validate provisions-mask-deterioration concern / FL-NY CRE stress. |
| VLY | 8-K | 2026-05-07 | https://www.sec.gov/Archives/edgar/data/714310/000119312526210654/d145489d8k.htm | Supplemental VLY context. |
| RF | 10-Q | 2026-05-07 | https://www.sec.gov/Archives/edgar/data/1281761/000128176126000037/rf-20260331.htm | Peer/regional read; no current RF position. |
| EGBN | 10-Q | 2026-05-07 | https://www.sec.gov/Archives/edgar/data/1050441/000105044126000066/egbn-20260331.htm | EGBN Jun $25P / DC CRE canary; high priority if time. |
| FITB | 10-Q | 2026-05-05 | https://www.sec.gov/Archives/edgar/data/35527/000003552726000182/fitb-20260331.htm | FITB Jun $45P residual; check provision/CRE/NDFI quality. |
| ZION | 8-K | 2026-05-04 | https://www.sec.gov/Archives/edgar/data/109380/000010938026000078/zion-20260504.htm | Supplement to ZION review. |
| ZION | 8-K | 2026-05-04 | https://www.sec.gov/Archives/edgar/data/109380/000010938026000077/zions-20260501.htm | Supplement to ZION review. |
| CFG | 10-Q | 2026-05-04 | https://www.sec.gov/Archives/edgar/data/759944/000075994426000101/cfg-20260331.htm | NDFI / fund-finance bridge check; no direct position but high thesis relevance. |
| WAL | 8-K | 2026-04-30 | https://www.sec.gov/Archives/edgar/data/1212545/000162828026028778/wal-20260430.htm | WAL Investor Day / Q1 supplement context. |

---

## Still Missing From EDGAR Window

No matching May 1-10 material filings appeared in the expanded radar run for:

- **OZK** — core portfolio exposure; check separately / may not have filed in window.
- **SSB** — May contract; check separately / may not have filed in window.
- **HBAN** — profitable Oct put; not urgent unless new filing appears.

---

## Monday Extraction Priority

1. **ZION 10-Q** — kill/retain Jul $57.5P; look for CRE, criticized/classified, deposits, provision quality.
2. **CFG 10-Q** — NDFI/fund finance bridge; thesis relevance to bank/private-credit transmission.
3. **VLY 10-Q** — test REGINALD provisions-mask-deterioration concern.
4. **EGBN 10-Q** — DC CRE / DOGE / office canary; position exists but small.
5. **FITB 10-Q + 8-K** — residual position; provision/CRE/NDFI quality.
6. **WAL 8-K / existing Q1 files** — support WAL June hold/roll decision.
7. **OZK / SSB separate check** — if no filing, use existing earnings materials and Monday tape.

---

## Extraction Targets

For each available 10-Q / Call Report, extract only decision metrics:

1. **MI3 / modified / restructured loans** — especially WAL, OZK, EGBN, ZION.
2. **CRE concentration and migration** — office, multifamily, construction, hotel if available.
3. **NDFI / mortgage warehouse / lender finance / fund finance** — WAL and CFG first.
4. **ACL / provision / charge-off / past-due migration** — look for release-into-deterioration.
5. **FHLB / brokered deposit / liquidity shifts** — funding-stress tell.

---

## Immediate Build Implication

The filing radar is now more complete for the current bank book. The next real work is extraction/classification, not more watchlist hygiene.
