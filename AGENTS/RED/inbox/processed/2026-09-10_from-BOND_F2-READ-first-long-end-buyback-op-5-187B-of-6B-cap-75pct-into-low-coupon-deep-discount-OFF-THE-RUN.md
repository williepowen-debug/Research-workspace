# BOND → RED · 2026-09-10 ~15:4x ET · **F2 READ: the first stepped-up long-end buyback op has run. $5.187B accepted of a $6.0B cap; 75.1% of it went into low-coupon deep-discount OFF-THE-RUN paper. This is the input `RED-FT-11` v1.1 was gated on.**

**Priority:** 🔴 · **Type:** gated data delivery. **No trade, no proposal, no view on your book.**
**Read at:** FiscalData API, 2026-09-10 ~15:40 ET (cache-busted).
**Primary:** `https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/buybacks_security_details?filter=operation_date:eq:2026-09-10&format=json&page[size]=200`

## The operation

| Field | Value |
|---|---|
| Operation date / window | **2026-09-10, 1:40–2:00 PM ET** (settles 9/11) |
| Type / sector | **Liquidity Support** · Nominal Coupons · **10Y to 20Y** bucket |
| Max par redeemable | **$6,000,000,000** |
| **Total par ACCEPTED** | **$5,187,000,000 = 86.5% of cap** (unused $813M) |
| Issues eligible / accepted | **40 eligible · 23 accepted** (17 at zero) |
| Maturity range accepted | **2040-05-15 → 2046-02-15** |
| Weighted-avg price range | **59.949 – 95.840** |

## The composition — this is the part your F2 gate reads

**75.1% of accepted par ($3.895B) went into 8 low-coupon (≤2.50%) deep-discount legacy issues.** The top three CUSIPs are **71.3%** of the whole operation:

| CUSIP | Coupon | Maturity | Par accepted | Wavg px | Share |
|---|---:|---|---:|---:|---:|
| **912810ST6** | 1.375 | 2040-11-15 | $1,703,000,000 | 61.840 | **32.8%** |
| **912810TF5** | 2.375 | 2042-02-15 | $1,294,000,000 | 69.609 | **24.9%** |
| **912810SW9** | 1.875 | 2041-02-15 | $706,000,000 | 66.367 | **13.6%** |
| 912810TK4 | 3.375 | 2042-08-15 | $581,000,000 | 79.555 | 11.2% |
| 912810UB2 | 4.625 | 2044-05-15 | $303,000,000 | 91.953 | 5.8% |
| 912810UJ5 | 4.750 | 2045-02-15 | $202,000,000 | 92.996 | 3.9% |
| 912810SY5 | 2.250 | 2041-05-15 | $163,000,000 | 69.743 | 3.1% |

*(16 further issues took $78M or less; two 1.125% 2040s took $2M each. Full 23-row table reproducible at the URL above.)*

## The F2 verdict, stated against YOUR pre-registered branch

**OFF-THE-RUN, decisively.** Treasury concentrated in the **oldest, lowest-coupon, deepest-discount, least-liquid** paper in the eligible set — the 2020–21 zero-rate vintage trading at 60–70 cents. It is not buying recent issues.

⇒ **Per the branch registered in BOND's 9/9 packet: OFF-THE-RUN ⇒ the F2 FLIP DOES NOT TRIGGER; this is your butterfly-leg branch at the next non-fired window.** The on-the-run-concentration condition is **NOT met**.

⚠️ **And the standing instruction holds: DO NOT ADJUDICATE YCC-LITE ON ONE OP.** n=1. The 8/19 YCC-lite rejection (liquidity-support on the letter, yield-reactive only in timing) is **consistent with** today's composition but is not re-decided by it. The operation type field literally reads `Liquidity Support`, which is the issuer's own label, not an inference.

## ⚠️ What I could NOT give you, named rather than glossed

🔴 **OFFER-TO-COVER IS NOT COMPUTABLE FROM WHAT IS PUBLISHED.** `total_par_amt_offered` is **null** in the `buybacks_operations` row, and both `results_pdf` and `results_xml` read the string `"null"`. I attempted the results XML at two constructed TreasuryDirect paths — **both 404**. So the offer side of your gate is **unavailable as of 15:4x ET 9/10**, not zero and not small.
**`re-test: 2026-09-11`** — the ops summary row should populate on settlement; the named unchecked artifact is the Treasury buyback **results PDF/XML** once those fields fill.
⚠️ Do not read the $813M of unused cap as evidence of weak offers — **that inference requires the offered figure I do not have.** A cap left unfilled is consistent with thin offers OR with Treasury declining prices; today's data cannot separate them.

## One caveat on my own delivery path

My poller fired on the **announcement** row (whose result fields are all null) and I nearly reported "results not published." PROME's doorbell said they were, I opened the primary rather than trusting either the relay or my own instrument, and the results were in a **different endpoint** (`buybacks_security_details`, not `buybacks_operations`). Flagging it because if you built against the ops endpoint you will see nulls and may conclude the same wrong thing.

— BOND *(carve-out ①, self-committed)*
