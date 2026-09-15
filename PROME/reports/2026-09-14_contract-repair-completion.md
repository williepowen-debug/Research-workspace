# L394 repair completion — September 14, 2026

**Implemented, tested, and independently accepted for R1–R4.** Will authorized the repairs after the [independent defect review](2026-09-14_contract-identification-review.md). L394 is resolved for this bounded repair scope; L392 calibration remains open.

## Changes

- **R1 — cache expiry:** a partial basket refresh fetches every member before renewing the basket timestamp. Complete cache hits still avoid vendor requests. Legacy cached errors trigger retry, and persistent failures retain explicit error rows and CLI exit 3. **Tradeoff:** a failing basket now costs more vendor requests while failures persist.
- **R2 — timing evidence:** continuous and matched quotes need positive integral epoch-second timestamps. Missing/invalid continuous timing refuses; missing/invalid matched timing refuses. Unknown nonmatched timing is explicitly advisory. The 900-second matched-leg cutoff is unchanged.
- **R3 — instrument identity:** probe responses must name the requested symbol. Only letter case and surrounding whitespace are normalized. Invalid continuous symbols refuse; invalid candidates are dropped with a reason before counting the usable control set.
- **R4 — usable prices:** nonfinite, nonnumeric, Boolean and unsupported price values cannot enter the probe's control. Invalid continuous prices refuse; invalid candidate prices are dropped. Finite zero and negative prices remain valid.

The original six-case acceptance suite now freezes its September 2026 fixture date. The original review reproductions remain intact; the expanded regression suite promotes their cases into maintained tests.

## Verification receipt

**VERIFIED:** final production file `FORGE/tools/market-data/fetch.py`, based on repository revision `3f4f44aa9`, SHA-256:

`c1c60d748cd6ce973b9affa6f53cf2c6271b258e65437e50a36a88271b16c2bd`

| Check | Result |
|---|---|
| Original independent counterexamples on first repaired candidate | 10/10 passed; all cases also included in the final regression suite |
| Expanded regression suite on final source | 22/22 passed |
| Original acceptance suite on final source | 6/6 passed |
| Independent reader's new cases on final source | 7/7 passed |
| Independent exact-timestamp checks | 8 integral representations accepted; 11 invalid inputs rejected |
| Same expanded suite on the pre-repair exported source | Exit 1: defects detected, including assertion failures and invalid-input exceptions |

The counts overlap; they are not a total of unique scenarios. Tests use isolated module/cache copies and fake vendor data. No live market-data claim follows from these results.

### Independent review and correction

The independent reader (`docket_result_read`, separate from the repair author) first reviewed candidate hash `d1082a7ed2db25a2500d901e2cf67f76e9476ae5ebf9315c8ff5218b8cd60af3`. Its own new counterexample supplied timestamp text `1000000.00000000001`: float conversion erased the fractional part and incorrectly permitted identification. **That candidate was not accepted.**

The correction validates the original numeric representation with `Decimal` before accepting integrality. The independent reader inspected and retested the final hash above, confirmed refusal on both affected legs, and delivered: **“ACCEPTED for the bounded R1–R4 repair scope. No blocking findings remain.”** This is review of the final correction, not author confirmation substituted for independent verification. The reader confirmed read-only closeout with no repository changes.

The [independent cases](2026-09-14_contract-repair-independent.py) are retained alongside this receipt; only their harness path was made relative when copied from the reviewer's temporary file. The discovered fractional-input case is also in the maintained regression suite.

## Reproduce

```bash
.venv/bin/python3 -W error::ResourceWarning PROME/tools/tests/test_fetch_contract_repairs.py
.venv/bin/python3 -W error::ResourceWarning PROME/tools/tests/test_contract_probe_acceptance.py
mkdir -p /tmp/prome-contract-repair-check/FORGE/tools/market-data
cp FORGE/tools/market-data/fetch.py /tmp/prome-contract-repair-check/FORGE/tools/market-data/fetch.py
.venv/bin/python3 -W error::ResourceWarning PROME/reports/2026-09-14_contract-repair-independent.py /tmp/prome-contract-repair-check/FORGE/tools/market-data/fetch.py
```

For a historical comparison, export `3f4f44aa9:FORGE/tools/market-data/fetch.py` and set `FETCH_REVIEW_SOURCE` to that exported path when running the expanded suite. Expected result: failure. The old review report remains the historical receipt for that version.

## Completion states and remaining limits

- **IMPLEMENTED — VERIFIED:** R1–R4 and the independent timestamp correction are in the named final source.
- **TESTED — VERIFIED:** executable regression and acceptance checks pass as recorded above.
- **INDEPENDENTLY VERIFIED — VERIFIED, bounded:** final source accepted by the independent reader after its own counterexample and follow-up test.
- **STILL UNRESOLVED:** L392's close/overnight calibration of 900 seconds; consumer spread guards; previously declared unknown-symbol renderability and live negative-control demonstration. Absolute freshness against the wall clock and concurrent filesystem writers are not certified here. This acceptance does not certify every historical repair or authorize a capital/threshold change.
