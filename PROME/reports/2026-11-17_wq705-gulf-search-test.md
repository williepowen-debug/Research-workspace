# WQ-705 A: the Gulf news search, tested once (2026-11-17)

**By:** PROME prome-19 · **Authority:** Will 2026-11-17 09:30 ET, verbatim "703 yes, 705 yes" (WILL_QUEUE row 705, RULED A) · **Run:** 09:33 to 09:35 ET, read-only, Google News RSS with the plain client string `research-intake-comparison-test`; nothing in `/home/willi/Research-Intake` was pulled, checked out or written. Raw responses: the session scratchpad only (not durable).

## Result under the ruling

The changed form the ruling named (last 24 hours, Bahrain added) did NOT return current Gulf headlines. **Under A, nothing changes in the collector, and nothing was changed.**

## What each form returned (first 15 items are what the collector keeps)

| Form | Retrieved | First 15 under 24 hours | First 15 over 72 hours | Bahrain in any title |
|---|---:|---:|---:|---:|
| The collector's search as it is (18 terms joined by OR) | 32 | 0 | 15 (14 over 30 days) | 0 |
| The same with `OR Bahrain when:1d` (the approved changed form) | 32 | 0 | 15 | 0 |
| The same with `when:1d` only | 32 | 0 | 15 | 0 |
| The same in brackets, `(...) when:1d` | 32 | 0 | 15 | 0 |
| The same in brackets with Bahrain, `(... OR Bahrain) when:1d` | 32 | 0 | 15 | 0 |
| A short search, `(Hormuz OR Houthi OR IRGC OR Bahrain OR "Bab el-Mandeb" OR Kharg OR Fujairah) when:1d` | 100 | 15 | 0 | 48 |
| The short search with no recency limit | 100 | 13 | 1 | 47 |

## Reading

- **Observed:** the 18-term search returns 32 items, none newer than about four days and most months old, with or without a recency limit. A seven-term search returns 100 items, nearly all from the last day. The recency limit is not what separates them; the length of the search is.
- **Inferred, not established:** Google's search degrades on the long OR chain. The threshold (how many terms is too many) was not measured.
- **Not established:** that this is what happened on 11/13. The 11/13 response was not stored. WALTER's packet suspected the 15-item cut and the missing recency limit; today's test points at the search's length instead.
- **Not tested:** every other search in `scripts/newsweep_config.py`. Several are as long as this one (the China search has 18 terms).
- The last four forms go one step past the two the ruling named: read-only probes to find why the approved form failed (class C11). No collector change follows from them without Will's word.

## Found in passing, UNVERIFIED

The short search's first items at 09:35 ET were titles about a new Iranian strike on US targets in Bahrain and a tanker struck in Hormuz (CNBC, Reuters, AP, Al-Monitor, Al Jazeera; 1 to 10 hours old). Titles only; PROME read no article. FALCON was woken to establish them (ORCH_LOG, 11/17, class C8).
