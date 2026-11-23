# Acceptance: closeout receipts reconciled in ORCH_LOG; calendar size target raised (WQ-729, WQ-733)

**Authority:** Will 2026-11-23 12:17 ET: "Receipts: reconcile the 22 closeout rows since 11/18 and the 94 'still working' launch rows where a real receipt exists. Leave the 1,559 prose rows and the missing-evidence rows as they are, with their limits stated." and "WQ-729 items 1, 2 and 3 approved as restated." Record `PROME/proposals/2026-11-23_wq733-RULED.md`.

## Receipts
**Method:** `PROME/tools/tests/recon_receipts_2026-11-23.py` (kept as the record of what ran). For each PROME-owned session whose rows carry the structured block, if one of its rows has a delivered cell beginning "CLOSED OUT" (the receipt as recorded at the time), ONE new row (touch `9-RECEIPT-RECONCILE`, dated 2026-11-23) quotes that receipt and names every unresolved row of the session under `resolves`. No new ask, no new evidence, nothing inferred. Tested on a scratch copy first; two sessions the checker rejected there (BRENT brent-bd, VULCAN vulcan-46: "original timestamp/date mismatch", their launch rows' stamps and dates disagree) were excluded.

| Checker count (`python3 PROME/tools/orch_closeout.py --json`) | Before | After |
|---|---|---|
| UNKNOWN | 1,640 | 1,618 |
| ASKED, still working | 96 | 71 |
| Resolution issues | 5 | 5 (the same five, all older) |
| Rows appended | | 28 (47 rows resolved: 25 launch rows, 22 closeout rows) |

**Left as they are, limits stated:** the rows written as prose before the format existed (the bulk of the 1,618); rows whose evidence is missing or malformed (timestamp absent, disposition UNKNOWN, ANVIL 9/30 and TERRY 10/01 asked with no receipt); 71 launch rows still reading "still working": 46 from September and October and about 24 from 11/19 to 11/20 whose receipt, if one exists, is recorded on a row with no matching session identity (a hand mapping, not done), plus BRENT brent-bd and VULCAN vulcan-46 above and one session in flight (HANS, 11/23). A count that reads "still working" for those is a record gap, not a statement that the desk is running.

⚠️ During the scratch test the generated view `PROME/state/ORCH_INFLIGHT.md` was overwritten from the scratch copy (the append helper writes the default view path even with `--ledger`); it was restored from git before the real run, and `orch_log.py check` passes. Scratch tests of this helper need `--view-path`.

**State:** IMPLEMENTED · TESTED (author; the checker's own counts are the test) · not independently verified. reads: 0.

## Calendar size target
`scripts/docket_view.py --budget` default 6,000 to 16,000 (two lines). Tested: no warning at today's 9,987 B block; the warning still fires with `--budget 5000`. **State:** IMPLEMENTED · TESTED (author).

## Still owed under WQ-729 and WQ-733 (DOCKET row dated 2026-11-24)
The boot runner edit (a procedure file: plan read and result read), the wording for `receipt` and `resolves` in the closeout procedure, and the independent read on cc98a77b3c.
