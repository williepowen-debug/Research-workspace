# Fixed yen futures replacement — September 9 review

**Select 6JZ26.CME → 6JH27.CME as the replacement contract pair. Do not activate the current Yahoo-based feed yet.** Contract identity, expiry spacing and one official settlement anchor pass; precision and same-session quotation controls do not. Existing `workbook/XCCY_BASIS.tsv` and its September 14 expiry guard remain unchanged. No continuous-contract splice or cross-pair daily delta is authorized by this review.

## Exchange evidence

CME September 8 **FINAL bulletin 172**, [Section 33 page 1](https://www.cmegroup.com/daily_bulletin/current/Section33_Japanese_Yen_Call_Options.pdf), explicitly lists the underlying JAPAN YEN FUT expiries: Sep26 September 14, Dec26 December 14, Mar27 March 15. These are futures dates in an options bulletin, not option-expiry dates. The [FX delivery convention](https://www.cmegroup.com/markets/fx/fx-delivery.html) is consistent: third-Wednesday value dates, two business days earlier for last trading. December 14, 2026 → March 15, 2027 is **91 calendar days**.

| September 8 exchange observation | Sep26 | Dec26 | Mar27 |
|---|---:|---:|---:|
| Settlement, USD per JPY | 0.0065110 | 0.0065570 | 0.0066035 |
| Globex volume | 605,633 | 176,493 | 318 |
| Open interest | 233,727 | 263,476 | 788 |

The same values appear in [Section 07 page 1](https://www.cmegroup.com/daily_bulletin/current/Section07_Currency_Futures.pdf). Both were read via the browser; direct download returned HTTP 403. These are transcriptions of exchange tables, not local PDF downloads. `cme-reference.json` records source, page, publication date and values. Thin March activity warrants caution even with an exchange settlement; model-derived settlement is not an executable spread.

## Reconciliation and units

The saved vendor sample contains **56 matched dates**, June 22–September 9. Quote metadata confirms USD-denominated CME futures, not spot or a continuous front. September 8 near prices match the exchange within floating-point noise, but Yahoo gives March **0.0066040**, rounding the official **0.0066035** upward by 0.0000005 USD/JPY. Its zero September 8 volume is incomplete vendor data, not proof of no trading.

Preserve the old instrument's explicitly approximate formula only for comparison:

`implied annual % = (far / near − 1) × 365 / 91 × 100`

`residual bp = [implied annual % − (Treasury 3m bill % − assumed JPY 1.00%)] × 100`

For September 8, Treasury 3m **3.94%**: official Dec–Mar residual **−9.5544bp**; rounded vendor Dec–Mar **−6.4951bp**, a **+3.0593bp** distortion. Vendor Sep–Dec **−10.6257bp** is a different forward interval. The apparent level jump on switching pairs is not a funding-market move.

September 9 vendor Dec–Mar calculates **−23.2652bp**. **Rejected as a reliable current residual**: the two last-trade timestamps differ by **37,786 seconds**, and March shows only 16 trades in the retrieved snapshot. Daily date-label equality does not establish a synchronized settlement. Do not interpret the roughly −16.77bp vendor day change as stress. Saved `candidate-pair-observations.csv` is research-only, including suspect observations; it is not a LIVE ledger.

## Activation requirements and disposition

1. Obtain at least two completed, same-session exchange settlement pairs with full 0.0000005 precision and independent source clocks. The September 8 anchor supplies one. Authenticate the actual downloaded/current bulletin date; a `current` URL is not a dated archive.
2. Use a **separate pair-identified ledger**, retaining contract names, expiries, observation date, source/retrieval clocks, quote precision and assumptions. Never overwrite or append different instruments into the six-column Sep–Dec ledger.
3. Change the reader only after it can reject missing, rounded or unsynchronized legs, and expire at the new near contract's December 14 boundary. Compare changes within each pair; do not join levels or compute a rollover-day change across pairs.
4. Keep this a futures/bill/assumed-policy residual. Dec–Mar forward rates compared with today's three-month bill are not matched-tenor OIS, futures convexity and the JPY policy path remain confounders, and the priced September BOJ move makes the fixed 1.00% assumption particularly limiting. No funding-stress threshold or trade trigger is created.

**Result:** replacement pair validation completed with a feed-quality hold. A reliable automated replacement is outstanding before September 14; if it is not available, the existing monitor should stop as designed. The expiry reminder remains active for this unresolved implementation dependency. Reproduction: `../../.venv/bin/python3 research/outputs/2026-09-09_followthrough/analyze.py` from SAM; no live workbook writes.
