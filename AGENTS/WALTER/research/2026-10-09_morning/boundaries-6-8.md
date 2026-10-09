# Boundaries #6 / #8 — matched-month computation, 10/9 ~09:57 ET (WALTER boot-gap close)

Basis: Yahoo/yfinance `fast_info` last trade at ~13:57Z 10/9 (NOT settlements), named contracts. Brent contract identity
for BZZ26/BZF27 is UNRESOLVED by the metadata probe (truncated name); the symbol was requested by name. `previous_close`
is a vendor field: CLX26 prev 90.43 vs the 10/8 settle of $91.49 (Newsquawk), so it is not the settle and is shown only as
a vendor figure. Month basis is UNRULED (Will's decision pending, outbox/2026-09-14_boundary-6-8-month-basis-RECOMMENDATION-to-Will.md). No grade.

| Month | #6 RB×42 − WTI (last) | #8 (2·RB+HO)×42/3 − Brent (last) | vendor prev-close #6 / #8 |
|---|---|---|---|
| Nov-26 (X) | 46.15 | n/a (Brent Nov expired 10/1) | 47.57 / n/a |
| Dec-26 (Z) | 41.11 | **48.43** (3.1% under $50) | 41.95 / 49.92 |
| Jan-27 (F) | 38.17 | 47.82 | 38.44 / 48.62 |

#6 letter: re-cross from <$30 back ≥$30 OR single-day spike ≥$50 → neither condition on any month.
#8 letter: >$50 sustained 2–3 sessions → not met on the live last trade; Dec within ~3%; BRENT is fire-primary (STATUS fresh 10/8).
Inputs: RBX26 3.2747 HOX26 4.7701 CLX26 91.39 | RBZ26 3.1311 HOZ26 4.6153 CLZ26 90.40 BZZ26 103.86 | RBF27 3.0357 HOF27 4.5169 CLF27 89.33 BZF27 100.42
