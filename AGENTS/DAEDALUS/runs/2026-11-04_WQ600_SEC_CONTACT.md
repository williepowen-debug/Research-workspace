# WQ-600 SEC contact moved to a local setting — 2026-11-04

**Result:** PARTIAL. 21 of 30 code files changed; 9 handed to their owners. Authority: WQ-600 A, Will 2026-11-04 20:59 ET, verbatim "approved with your recs", record `PROME/proposals/2026-11-04_wq591-601-RULED.md`; PROME ACTION 2 in `inbox/processed/2026-11-04_from-PROME_WQ600-601-RULED.md`. Going forward only; history not rewritten. The address appears in no file this work created.

## Design

`scripts/sec_contact.py` reads `SEC_CONTACT` from the environment, else from `FORGE/tools/market-data/.env`, the fleet's existing gitignored home for local settings. Tools call `sec_ua("<their existing format with {}>")`.

**Failure timing:** `grade_auction`, `edgar_watch` and `market_tracker` are imported by tests and base-rate scripts, and three desks read this at boot, so an import-time raise would break unrelated offline work. `sec_ua` never raises. When absent it prints the fix to stderr and returns a header value holding the fix and a newline; urllib and requests refuse that header before connecting. WAL's handler reports only the exception type, which is why the stderr line exists. The one curl-based script uses `sec_contact()`, which raises.

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

## Limits

- This box only: the setting is in the laptop's `.env`. The desktop has no setting until someone adds it; until then these tools refuse on that box.
- 1 live real-tool absent run end to end (WAL); the other 12 verified by import and header value. CYPHER, ISHM, LABOR, SAM have no suite run here.
- A curl-based tool would need `sec_contact()`; only the one such script was found.
- Stderr prints on import of an affected tool when absent, including sessions that make no SEC call.
- The address remains in history, in the 25 non-code tracked files ruled out of scope (including `SIGNALS/feeds.yml`), and in the 9 handed-off files until applied.
