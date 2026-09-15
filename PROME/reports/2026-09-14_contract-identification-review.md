# L394 — independent review of contract-identification repairs

**Disposition: NOT ACCEPTED.** Four reproducible findings remain. Review performed by Codex/PROME on September 14, 2026, independently of the original implementation and its author acceptance fixtures. This is a bounded review, not a certification of every historical repair.

## Reviewed artifact and evidence

- **VERIFIED:** workspace HEAD at review start: `bd46a3b82c9d55c542f069dffd50085c7c92d759`.
- **VERIFIED:** last change to `FORGE/tools/market-data/fetch.py`: `e2de0bd1b68dcb3e87a57fd7246f44ef1886ecbc`. The reviewed file is identical at both commits; SHA-256 `ac47f686f82aebd61ba7a468e0e680ce3cfd7dbfbd2c503eb1e389a00ccd0914`.
- **VERIFIED:** existing author suite passes **6/6**. Its fixed contract symbols depend on the execution month; this run was September 14, 2026.
- **VERIFIED:** the separate [counterexample runner](2026-09-14_contract-review-counterexamples.py) reports `Ran 10 tests`, `FAILED (failures=7)`, exit 1. Four methods pass; six fail, with the nonfinite-price method producing two failing subtests. No harness errors remain. An initial harness-only error referenced a nonexistent TTL constant; it was corrected before these results.
- **UNKNOWN:** whether the malformed vendor responses used below occur live. These are synthetic, offline counterexamples, not observed market incidents. The cache defect uses the real cache functions with an isolated filesystem and simulated time.

## Findings / assertion ledger

### R1 — P1: partial-cache retries extend the lifetime of quotes they never refresh

**Claim (VERIFIED):** a persistent failure in a basket can keep successful prices cached beyond their original TTL, repeatedly.

**Exact artifact:** `fetch.py:715` computes missing keys; `:730` copies cached successes; `:881` writes the whole result again; `_cache_set` at `:283` assigns the current time to the basket.

**Verification:** run the counterexample command below, test `test_partial_cache_retries_do_not_renew_old_successful_quote`.

**Observed:** at simulated t=10,000 the basket fetches BZ=100 and BAD=error. The vendor fixture then changes BZ to 110. Calls at t=10,119 and t=10,238 only retry BAD. BZ still returns 100 after its original 120-second TTL. Ticker calls are `['BZ=F', 'BAD', 'BAD', 'BAD']`. The error remains visible, but every retry renews the old successful row's cache timestamp. **INFERRED:** continuing this pattern prevents expiry indefinitely.

**Proposed change / acceptance:** preserve each quote's acquisition/expiry time when merging partial results, or refetch the basket when renewing its TTL. A retry must not extend a quote's lifetime unless that quote is fetched again. Keep failures visible and retryable. This is an overlap defect in the coverage repair, separate from the 900-second probe calibration.

### R2 — P1: absent timestamps bypass matched-leg freshness verification

**Claim (VERIFIED):** removing either the continuous timestamp or the matched candidate timestamp still permits `IDENTIFIED`.

**Exact artifact:** `fetch.py:1073` records an unknown age; `:1105` excludes missing timestamps from the stale list; `:1125` refuses only membership in that list.

**Verification:** tests `test_missing_matched_timestamp_cannot_establish_compatible_times` and `test_missing_continuous_timestamp_cannot_establish_compatible_times`.

**Observed:** two distinct prices, one match, timestamp missing on one side → `IDENTIFIED`, `tracking=BZU26.NYM`, `control=passed-distinct-prices`, matched age `None`. The temporal compatibility required by the final stale-match repair has not been established.

**Proposed change / acceptance:** require valid timestamps on both matched legs before identifying; missing or invalid timing evidence gets an explicit refusal/unknown result. Preserve the settled distinction that a stale nonmatched leg is advisory. Changing `STALE_S` cannot repair this missing-data path.

### R3 — P1: the probe ignores vendor symbol mismatches

**Claim (VERIFIED):** the separate probe does not carry the symbol guard already present in `price_fetch`.

**Exact artifact:** `fetch.py:1033` and `:1049` read metadata, but record only its price/time under the requested symbol. Contrast `price_fetch` at `:831`, which checks `metadata['symbol']`.

**Verification:** tests `test_wrong_matched_symbol_cannot_identify_requested_contract` and `test_wrong_continuous_symbol_cannot_identify_requested_root`.

**Observed:** changing the matched response's vendor symbol to `CLV26.NYM`, or the continuous response's symbol to `CL=F`, leaves the verdict `IDENTIFIED` for `BZU26.NYM`. The fixture retains Brent's monthless name so the optional name cross-check cannot mask the defect. The probe has explicit evidence that the response names a different instrument and discards it.

**Proposed change / acceptance:** validate the continuous response and every candidate against the requested vendor symbol before using their prices. Refuse an invalid continuous response; exclude invalid candidates with a stated reason, then rerun the minimum-control and match requirements. Missing symbol evidence also needs an explicit disposition. Preserve documented aliases only through an explicit normalization rule.

### R4 — P2: a nonfinite quote counts as a valid negative-control price

**Claim (VERIFIED):** `NaN` and infinity can supply the supposedly distinct second contract required for identification.

**Exact artifact:** `fetch.py:1054` accepts any non-`None` price; `:1080` and `:1082` then count entries and distinct values without requiring finite prices.

**Verification:** `test_nonfinite_quote_is_not_a_second_control_price`, subtests `nan` and `inf`.

**Observed:** continuous=100, matched candidate=100, sole other candidate=NaN (or infinity) → `IDENTIFIED`, `control=passed-distinct-prices`. There is only one usable dated quote, so the negative control has not been performed over two usable prices.

**Proposed change / acceptance:** validate conversion and finiteness before adding a candidate; record invalid quotes as dropped and require at least two valid distinct quotes afterward. Validate the continuous price too. Do not impose positivity: negative futures prices are not this defect.

## What held, and review limits

**VERIFIED in fixtures:** a matched quote 10,000 seconds older is refused; fresh matched/stale nonmatched behavior passes the author suite; vendor-name agreement identifies and disagreement refuses; duplicate prices, no match, and too few candidates take the expected refusal paths in the author suite. Those repairs work on their tested inputs.

**Acceptance mapping:** R2/R3 prevent accepting reliable dated-contract resolution (conditions 3–4 and the final freshness repair); R4 defeats the usable negative control (condition 5); R1 violates ordinary cache expiry in the overlap/coverage repair. Conditions 1–2 and 6–8 received source inspection, not exhaustive fresh end-to-end certification. Prior live observations remain historical evidence; this review does not reproduce or upgrade them.

**Neighbours considered:** ordinary cases tested; overlap tested with partial cache success plus persistent failure; wrong instrument tested through vendor symbols; missing information tested through timestamps and invalid quotes. Concurrent vendor observations are represented by differing timestamps. Concurrent filesystem writers were not exercised; fixtures use isolated caches, and the production file was checked unchanged. Foreign VIOLET work was outside the edit scope.

**Declared residue:** L392 still owns calibration of 900 seconds in the registered close/overnight windows. Unknown-symbol renderability, a live negative-control failure demonstration, and the consumer spread guard remain unresolved as previously recorded. Absolute quote age versus wall clock is not certified by this review's relative timestamp tests. The author suite's calendar dependence should be addressed when extending the regression suite. No threshold, consumer guard, or production-code change was made in this review.

## Reproduce

From the repo root, export the reviewed revision into an isolated temporary tree:

```bash
mkdir -p /tmp/prome-contract-review-20260914/FORGE/tools/market-data
git show e2de0bd1b68dcb3e87a57fd7246f44ef1886ecbc:FORGE/tools/market-data/fetch.py > /tmp/prome-contract-review-20260914/FORGE/tools/market-data/fetch.py
.venv/bin/python3 -W error::ResourceWarning PROME/reports/2026-09-14_contract-review-counterexamples.py /tmp/prome-contract-review-20260914/FORGE/tools/market-data/fetch.py
```

The runner freezes September 2026, loads another isolated copy, replaces yfinance, and suppresses audit writes. No live credentials, cache, or network are required. Its assertions state desired behavior and intentionally fail on the reviewed revision; it is retained beside the report rather than added to automatic test discovery. Run the author check separately with `.venv/bin/python3 PROME/tools/tests/test_contract_probe_acceptance.py`.

## Completion states

- **IMPLEMENTED:** prior repairs present; R1–R4 not repaired by this review.
- **TESTED:** author suite passes; independent counterexamples reproduce R1–R4.
- **INDEPENDENTLY VERIFIED:** review performed against the named revision; **acceptance FAIL**, not a clean verification of the implementation.
- **STILL UNRESOLVED:** L394 remains PENDING for R1–R4 remediation and review of the resulting revision. L392 calibration and the consumer spread guard remain separate.
