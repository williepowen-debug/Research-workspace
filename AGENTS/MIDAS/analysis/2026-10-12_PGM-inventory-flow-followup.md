# MIDAS — bounded PGM inventory/flow follow-up — 2026-10-12

**Disposition: UNRESOLVED for the recent price weakness.** Latest NYMEX warehouse evidence is now reachable and shows measured zero movement for October 9. Issuer current NAV/assets are reachable, but a matched September 30→October 9 fund share-count/physical-holdings series was not retrieved. These observations do not establish an inventory or redemption explanation for the decline. No new forecast, band, score, monitor or capital action.

## Assignment and reconciliation

Authority: `0cb6d515f:AGENTS/MIDAS/inbox/2026-10-12_from-PROME_laptop-orchestration.md` and `PROME/reports/2026-10-12_laptop-orchestration.md`. Will directed PROME to coordinate the existing owner windows. PROME records the completed broad metals review `cad8c1c12` and delivery `60815a590` as consumed. This pass covers only the existing PGM inventory/flow gaps; it does not repeat the broad review or perform lifecycle closeout. MIDAS thread: **01a131e1-82c3-7702-beae-4992d53e8fd5**, Codex/OpenAI; exact model remains UNKNOWN. Public-source retrieval approximately 21:28–21:33 UTC October 12; access timestamps saved with responses.

The comparison needing an explanation remains **September 30→October 9**: January-2027 platinum PLF27 **−1.4893%**; December-2026 palladium PAZ26 **−5.1138%**, from the already-committed same-contract vendor bars. The new inventory report covers only the **October 9 activity interval**, and the issuer snapshot is dated **October 9**. They are not a new weekly flow series.

## NYMEX inventories — the latest-point access gap is closed

The official [CME registrar page](https://www.cmegroup.com/clearing/operations-and-deliveries/registrar-reports.html) links **Platinum and Palladium Stocks** to [PA-PL_Stck_Rprt.xls](https://www.cmegroup.com/delivery_reports/PA-PL_Stck_Rprt.xls). The guessed `Platinum_Palladium_Stocks.xls` URL is not the canonical report. Python urllib on the canonical URL returned 403; the browser tool identified the link but could not parse its Excel content. One ordinary browser-like request using the already-installed curl_cffi client returned **200**, `application/vnd.ms-excel`, **24,064 bytes**. Raw workbook is saved, not reconstructed from a secondary report.

**Locator:** workbook sheet `Daily Metal Stocks Report`. Zero-based rows 11–12 and 85–86 carry report/activity dates. Rows 76–78 and 150–152 carry aggregate totals; columns C/H are PREV TOTAL/TOTAL TODAY. Source units are **troy ounces**.

| Metal | Report date | Activity date | Registered | Eligible | Combined | Receipts / withdrawals / adjustments |
|---|---|---|---:|---:|---:|---|
| Platinum | 2026-10-12 | 2026-10-09 | 116,425.323 oz | 194,514.399 oz | 310,939.722 oz | 0 / 0 / 0 — MEASURED_ZERO |
| Palladium | 2026-10-12 | 2026-10-09 | 196,832.119 oz | 53,114.143 oz | 249,946.262 oz | 0 / 0 / 0 — MEASURED_ZERO |

Registered and eligible totals both equal their PREV TOTAL fields; net change is zero. Every depository subtotal reconciles to its aggregate within 0.000001 oz, and registered + eligible = combined. **The workbook does not print a separate date beside PREV TOTAL**; it is the reported prior-total comparison for the October 9 activity interval, not a independently date-attested September 30 anchor.

For the dated comparison actually available, PLF27 rose **3.1242%** and PAZ26 **2.2214%** from October 8 to October 9 while reported warehouse stocks were unchanged. This is descriptive co-movement across different reporting clocks; it does not identify the rebound's cause. It supplies no observed receipt, withdrawal or reclassification channel on that activity date.

**Proxy limits:** registered/eligible are exchange warehouse and warrant categories, not global refined supply, total readily available metal, fund creations/redemptions or end consumption. A category move can occur without metal leaving a warehouse; total stocks can move through venue relocation. Neither a flat daily point nor the large registered count proves abundant global supply. No September 30 stock anchor or full decline-window stock series was retrieved. The registrar page's historical-data route is CME DataMine; no subscription, registration or historical pipeline was attempted.

## Issuer funds — dated current economics recovered, flows remain unmeasured

Direct public downloads succeeded for [Aberdeen PPLT](https://www.aberdeeninvestments.com/en-us/investor/funds/view-all-funds/-us0032601066) and [Aberdeen PALL](https://www.aberdeeninvestments.com/en-us/investor/funds/view-all-funds/-us0032621023). Their raw `__NEXT_DATA__` JSON is saved separately from the HTML. Exact numerical locator: `props/pageProps/page/pageData/fundDetailsData`, its `fundSizeValue/fundSizeValueDate`, and `selectedShareclass.prices` plus `selectedShareclass.investmentTrustPrices`.

| Fund | Issuer observation date | Assets, USD | NAV/share, USD | Market price/share, USD | Market/NAV −1 |
|---|---|---:|---:|---:|---:|
| PPLT | 2026-10-09 | 1,996,379,203.74 | 15.14129 | 15.25 | +0.71797% |
| PALL | 2026-10-09 | 602,284,406.51 | 20.63501 | 20.77 | +0.65418% |

All three embedded date fields agree for each fund. The rendered PPLT browser extraction mixed a **10/8 market-price tile** with **10/9 NAV/assets**, so it was not used for this calculation. The raw embedded market field explicitly reads **10/9 / $15.25**. Exact raw fields, rather than a summarized mixed-vintage webpage, control the table.

These dated marks show modest positive premiums, rather than a discount, on October 9. A shared date is not proof of a shared valuation clock; premiums can reflect the time between metal valuation and exchange close. **They do not reveal net redemptions, metal sales, authorized-participant inventories or investor motive.** Market turnover is not a creation/redemption flow. Asset values combine price valuation and quantity changes; an asset-value decline alone cannot identify outflow.

AUM ÷ NAV conditionally implies approximately **131.85 million PPLT shares / 29.19 million PALL shares**, if the asset value is the same-date net asset value. These are **INFERRED_ONLY**, not retrieved reported share counts; NAV rounding and the asset-field definition limit exact inference. They are not entered as observed share counts or used to calculate flow. No matched September 30 share-count or physical-ounce baseline was retrieved.

The embedded issuer configuration disables the holdings tab and contains no current physical-ounce/share-count history in the retrieved fund payload. Its localization dictionary includes the words “Shares Outstanding”; those labels are not numeric holdings evidence. A March 31 factsheet with share/ounce figures is public, but its vintage precedes the May share splits and is not a September flow anchor. The cited legacy `abrdn.com/usa/etf` link redirects to the new issuer ETF list, while both legacy `/en-us/etf/fund-details/pplt|pall` URLs return 404. This bounds **this retrieval**, not a claim that issuer bar lists or historical holdings do not exist publicly.

Lease rates were not available in the desk's existing accessible sources, and PROME limited that leg to already-accessible evidence. No new lease-rate acquisition project or subscription was started.

## Supported / weakened / unresolved

| State | Finding | What follows |
|---|---|---|
| **SUPPORTED** | Latest primary NYMEX point is retrievable; October 9 registered/eligible/combined stocks and all movement fields reconcile. Issuer October 9 NAV/assets/market data also recovered | Replace the blanket latest-inventory access gap with a dated snapshot plus a historical-comparison gap |
| **WEAKENED** | The desk's prior “all three instruments absent / NYMEX stocks not publicly retrievable” access premise was too broad | Correct current owned surfaces. Do not read the access correction as a price-mechanism verdict |
| **UNRESOLVED** | Inventory/redemption explanation for September 30→October 9 platinum/palladium weakness | Daily zero movement does not cover the decline window. Matched stock history, reported fund share/physical-ounce changes and lease evidence remain missing |

**Next existing date:** **October 19 weekly review**. MIDAS-09/10 still resolve October 30; WQ-368 remains due November 1. I2 stays 2; actual composite stays 8/20, with the approved unscored bands unchanged. No source in this pass establishes a fresh supply shock or an ETF liquidation channel. Macro sensitivity remains a candidate, not a newly identified residual explanation.

Held GLD/TERRY context remains at the consumed broad review and `60815a590` packet. No new GLD estimate, position advice or net-book hedge calculation was made. The broad review's prior observations remain historical; the current evidence-gap classification is updated by this follow-up.

## Durable evidence and verification

`sources/2026-10-12_pgm-followup/` contains raw Excel, issuer HTML/embedded JSON, a cell-level CSV, access attempts and `findings.json` with raw SHA-256 hashes and arithmetic. Calculations were one-off reads using existing installed clients/readers; no persistent tool, pipeline or monitor was added. Warehouse sums, registered/eligible identities, measured-zero fields, issuer dates and decimal premium calculations were checked directly. No behavioral tests are needed for this content-only pass.

Local result/state commit and the dated PROME delivery packet record exact versions. Opening pull/push remain deferred while outside-desk uncommitted work exists. This is a completed bounded research pass, not a lifecycle-closeout ask. PROME acceptance requires reading the committed follow-up artifact.

### Return transport recheck

PROME supplied return address `01a131cf-1c7d-7900-9dcf-d98af587e290` in the current committed orchestration report (version 004656ce2, Return address addendum). Local `codex queue --help` confirms supported `--thread` and `--message` arguments. This replaces the earlier capability gap for this exact coordination pair; it does not establish fleet-wide discovery. Content is committed before the queue notice. An accepted queue receipt establishes notification only; follow-up claim acceptance still requires PROME's artifact read. Actual send result is recorded separately after delivery.
