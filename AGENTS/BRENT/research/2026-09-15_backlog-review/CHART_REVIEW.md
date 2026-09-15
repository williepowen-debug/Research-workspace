# Shanghai/Brent chart — September 15 review

**Disposition: verification task completed, chart UNVERIFIED.** Will does not have the original link or series details (direct reply this session). Do not carry this as a pending request back to Will. Reopen only if source metadata arrives.

Viewed the exact image from WALTER's processed WILL inbox; preserved here as `shanghai-original.jfif`. Its SHA-256 agrees with WALTER's earlier manifest. It labels both prices “Active Contract”, with September 15 on the Brent and spread legends. It does not identify actual contract months, quote times, FX inputs or a publisher.

| Calculation from displayed numbers | Result |
|---|---:|
| 124.59492 − 106.36 | 18.23492 |
| Displayed spread | 18.25626 |
| Discrepancy | 0.02134 |
| Brent implied by Shanghai minus displayed spread | 106.33866 |

Under ordinary nearest rounding, the combined rounding allowance from the two prices and spread is at most 0.005010. The discrepancy exceeds it. This establishes inconsistent displayed inputs, not which series is wrong. Asynchrony, different formula inputs or a stale legend remain hypotheses.

The [INE 2024 educational handbook](https://www.ine.cn/upload/20240605/1717571185052.pdf), question 61 (printed page 78), confirms RMB denomination, net-of-tax pricing and bonded delivery. The current contract-page requests returned a human-verification page despite HTTP 200; they do not verify a current contract specification or price. Do not arbitrarily deduct VAT from this chart.

Reproduction requires a named SC contract price in CNY/barrel, a named Brent contract in USD/barrel, synchronized timestamps/price types and FX quoted in CNY per USD. Then `SC / FX − Brent` gives an unadjusted price difference. Matching delivery periods, grade, freight, financing and delivery-location costs are additionally needed for an arbitrage interpretation. None is supplied by this image. No measured shortage, current spread or trigger follows.

Exact decimal arithmetic and image identity: `chart-arithmetic.json`. SIG-007 outcome is recorded in BRENT's board log and NEXUS; no outbound message sent.
