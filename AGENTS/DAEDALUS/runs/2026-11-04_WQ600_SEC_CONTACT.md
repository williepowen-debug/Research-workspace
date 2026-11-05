# WQ-600 SEC contact moved to a local setting — 2026-11-04

**Result:** COMPLETE on this box, updated 2026-11-05: DEWEY (26596405a) and PROME (8a6e327e2) applied their 9 files. Corrections below supersede the first version of this record. Desktop setting unverified. Authority: WQ-600 A, Will 2026-11-04 20:59 ET, verbatim "approved with your recs", record `PROME/proposals/2026-11-04_wq591-601-RULED.md`; PROME ACTION 2 in `inbox/processed/2026-11-04_from-PROME_WQ600-601-RULED.md`. Going forward only; history not rewritten. The address appears in no file this work created.

## Design

`scripts/sec_contact.py` reads `SEC_CONTACT` from the environment, else from `FORGE/tools/market-data/.env`, the fleet's existing gitignored home for local settings. Tools call `sec_ua("<their existing format with {}>")`.

**Failure timing:** `grade_auction`, `edgar_watch` and `market_tracker` are imported by tests and base-rate scripts, and three desks read this at boot, so an import-time raise would break unrelated offline work. `sec_ua` never raises. When absent it prints the fix to stderr and returns a header value holding the fix and an interior newline; urllib, http.client and requests refuse that header. WAL's handler reports only the exception type, which is why the stderr line exists. The one curl-based script uses `sec_contact()`, which raises.

## Files

| Group | Files | Handling |
|---|---:|---|
| Live tools on idle desks: BOND 2, CYPHER, ISHM, LABOR 2, REGINALD 2, SAM, VULCAN 2, WAL 2 | 13 | Changed |
| Dated one-off scripts: SHADE 2, VULCAN 3, REGINALD 1 | 6 | Changed, parse-checked only; not run |
| SAM `before/` snapshots | 2 | Address replaced by a placeholder; never run, no hash reference found |
| DEWEY (live, working this in its own window) | 8 | Packet |
| `FORGE/tools/filing-watch/poll_edgar.py` (PROME commits FORGE) | 1 | Packet |

## Verification

| Check | Result |
|---|---|
| `scripts/test_sec_contact.py` | 12 pass; a live listener sees no connection when absent, and receives the request when present |
| Controls | Newline removed: 2 fail. Stderr line removed: 1 fail. A first control run errored on module load and proved nothing; repeated properly |
| Absent, real tools | 13 of 13 import and carry the refusal |
| Present, real tools | 13 of 13 byte-equal to the old format with a fixture contact |
| End to end | WAL's real `http()` refused with ValueError naming the fix, before the setting existed |
| Real SEC request | HTTP 200, WESTERN ALLIANCE BANCORPORATION, data.sec.gov, after the setting was added |
| Desk suites | docket_check 17 assertions, grade_auction rc 0, insider 11/11, 8k_monitor 16/16, BOND test_monitor_repairs OK, VULCAN 28 passed, WAL test_boot OK |

## Corrections, 2026-11-05

DEWEY's report exposed two defects in the first version, and a live check exposed a third.

| Defect | Evidence | Fix |
|---|---|---|
| The newline was trailing. Regex `$` matches before a final newline, so `requests` 2.31 (system Python) accepted the header. "Refused before connecting" was true only under `.venv`, requests 2.34 | `check_header_validity`, both versions; `scripts/test_sec_contact.py` errored under `/usr/bin/python3` | Interior newline. 13 tests pass on both Pythons; trailing-newline control fails under system Python |
| 5 tools contact only non-SEC hosts: BOND `docket_check`, `grade_auction` (TreasuryDirect), ISHM boot (FRED), LABOR `job_postings_tracker` (GitHub raw), SAM `bis_gli` (BIS). They sent the address needlessly and would have stopped without the setting | Host and use-site audit of all 13 live tools | No address, no setting. Follows DEWEY's `trace_bond` and `pdf2text`. Narrows PROME's "all 30" |
| FRED stalls custom User-Agents. `ISHM-Research` would have silently broken ISHM's feed | Three shuffled rounds, 12 s timeout: bare, `/1.0` and parenthetical forms 0 of 3; `Python-urllib` and dotted forms 3 of 3 at 0.1 s; `finding_negative_reachability_is_a_claim_about_your_request` Instance 4 | `Python-urllib`. Real `_fred` pulled INDPRO, TCU, DGORDER |

**Final checks (2026-11-05 08:30–08:45 ET):** absent: 8 of 8 SEC tools refuse, 5 of 5 non-SEC tools carry no address and need no setting. Live: TreasuryDirect, BIS and GitHub 200 twice, SEC 200, FRED through `_fred`. Suites: docket_check 17, grade_auction rc 0, BOND repairs OK, VULCAN 28 passed, WAL test_boot OK.

## Limits

- This box only: the setting is in the laptop's `.env`. The desktop has no setting until someone adds it; until then the SEC tools refuse on that box. PROME's MACHINE_LOCAL row is in place.
- 1 real-tool absent run end to end (WAL); the other 7 SEC tools verified by import and header value. CYPHER, LABOR and SAM have no suite run here. The non-SEC UA strings were tested live; the tools' own full runs were not, except ISHM `_fred`.
- A curl-based tool would need `sec_contact()`; only the one such script was found.
- Stderr prints on import of an affected tool when absent, including sessions that make no SEC call.
- No `.py` file holds the address. It remains in history and in the 25 non-code tracked files ruled out of scope (including `SIGNALS/feeds.yml`).
