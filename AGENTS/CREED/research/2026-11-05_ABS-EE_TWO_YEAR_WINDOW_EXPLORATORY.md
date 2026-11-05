# ABS-EE two-year window — exploratory result, kept apart from the approved screen

**Written:** 2026-11-05 (Thu), on Will's direction, 13:08 ET: *"Keep this as a descriptive lease-rollover screen, with no new recurring cadence or predictive study. Preserve the exploratory two-year result separately."*
**Status:** one observation, October 2026 cycle. Exploratory. Not in the approved scope, not a tested threshold, not a band, not a signal. No re-run is scheduled. `KB-CREED-105`.
**Approved screen, for contrast:** `research/2026-11-05_ABS-EE_OFFICE_LEASE_SCREEN_RUN1.md` and `KB-CREED-102`. Figures below must not be quoted as that screen's result.

**Perimeter:** registered CMBS trusts that file Form ABS-EE, roughly 2017+ vintages, single-property office loans, performing, fresh tenant data. It does not see 144A SASB, CRE CLOs, pre-2017 conduits or bank balance sheets. It is not "the office market" and must not be summed with Trepp's all-CMBS figures.

---

## The question

The approved test asks whether the largest lease ends before the loan matures. A lease ending six months after a 2027 maturity passes that test, yet a refinancing lender would still see almost no lease term. The window counts loans whose largest lease ends on or after maturity and less than 730 days later. Two years is CREED's judgement.

## Result

Cells are loans / balance. Observation: October 2026 cycle.

| Maturity year | Ends under 2y after maturity | Of which tenant >30% | Of which >30% and thin |
|---|---|---|---|
| 2026 | 4 / $0.18B | 2 / $0.08B | 0 / $0.00B |
| 2027 | 36 / $1.33B | 19 / $0.93B | 4 / $0.08B |
| 2028 | 72 / $2.65B | 32 / $1.30B | 3 / $0.10B |
| 2029 | 72 / $3.54B | 29 / $1.47B | 6 / $0.32B |
| **2026–29** | **184 / $7.70B** | **82 / $3.79B** | **13 / $0.50B** |
| 2030+ | 78 / $3.17B | 50 / $2.30B | 3 / $0.06B |
| All | 262 / $10.87B | 132 / $6.09B | 16 / $0.56B |

"Thin" means DSCR under 1.25x or occupancy under 80%.

## Added to the approved figures (CREED's combination, 2026–29, of the $31.87B fresh book)

| Cut | Approved test | Two-year window | Combined | Combined share |
|---|---|---|---|---|
| Any tenant share | 222 / $5.80B | 184 / $7.70B | 406 / $13.50B | 42.4% |
| Tenant >30% and thin | 19 / $0.47B | 13 / $0.50B | 32 / $0.98B | 3.1% |

The two rows are disjoint by construction: a lease cannot both end before maturity and on or after it.

## Largest window names (2026–29, tenant >30% and thin)

Candidates to read, not findings of distress. All three are performing. "Thin" mixes two tests, so read the cell. None matched a row in `cases/`; the name match is loose, so that is not proof of absence.

| Balance | Loan | Maturity | Largest tenant (share) | Lease end | DSCR | Occupancy |
|---|---|---|---|---|---|---|
| $261.6M | Parklawn Building, Rockville MD | 2029-11-01 | United States of America (72.9%) | 2030-07-31 | 2.81x | 73% (thin on occupancy only) |
| $71.3M | Zenith Ridge, Canonsburg PA | 2028-08-06 | Ansys (38.3%) | 2029-12-31 | 1.11x | 79% |
| $42.0M | 379 West Broadway, New York | 2027-11-06 | WW379 Broadway (87.6%) | 2029-04-30 | 1.20x | 100% |

## Limits

- **Untested against distress.** The cross-section in `KB-CREED-104` (34.4% against 32.0%) covers the lease-first flag only. No such comparison was run for the window, so nothing here shows it separates anything.
- **The cutoff is unvalidated.** No alternative window was run, so how much these dollars depend on 730 days is unknown.
- **No predictive study follows.** Will's direction of 11/05 closes that path; this page stays a record.

## Where the data lives

- Loans: `research/data/2026-10_absee_office_lease_loans.tsv`, rows with `cut` = `ENDS_UNDER_2Y_AFTER` (262). Rows with `LEASE_BEFORE_MATURITY` (562) are the approved test.
- Totals: `research/data/2026-10_absee_office_lease_summary.json`, under `screen`, keys beginning `window`.
