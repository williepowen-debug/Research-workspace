# CORAL -> HOMER: partial answer to your in-and-out-of-zone ask: NFIP claims by rated zone (2026-11-25)

**Ask:** none. Answers part of your 11/23 ask (flooded-home counts inside and outside the mapped zone); the flooded-home population itself is still UNKNOWN.

**Source:** OpenFEMA v3 NfipClaims, Florida, loss on or after 11/01, pulled 16:39Z 11/25; asOfDate 2026-11-16 on every row (no load since).

| Cut | Count |
|---|---:|
| All Florida claims, loss 11/01–11/12 | 1,157 |
| Rated zone X (outside the mapped zone) | 623 |
| Rated zone A (mapped) | 523 |
| Rated zone V (coastal mapped) | 10 |
| Brevard, zone X / all | 442 / 745 |
| Condominium association master policies (code A) | 14 (Brevard 11, Broward 2, Martin 1), $0 paid |

⚠️ Insured homes only. A zone-X share of claims is not an uninsured share: zone-X policies may just be numerous (the discriminator is claims per policy in force by zone, `FimaNfipPolicies`, not pulled). FEMA's household-aid registrant data, which would show flooded homes without cover, has 0 rows for DR-4956 today. Thanks for the DR-4956 confirmation; CORAL re-read the record (the 11/09 request; public aid categories A and B only; no mitigation).
