# DEWEY housekeeping completion — November 11, 2026

**Authority:** Will: “okay lets do housekeeping now”; PROME November 10 CourtListener repair request; WQ-645 A ruling dated November 9.

- CourtListener: `scripts/recap_pull.py usage` called the nonexistent `/api/rest/v4/usage/`; corrected to `/api/rest/v4/api-usage/`. [Official Free Law Project documentation](https://wiki.free.law/c/courtlistener/help/api/rest/v4/api-usage), checked November 11. Existing authentication and conservative local pacing preserved. The server's usage accounting is distinct from the helper's local budget.
- Live verification: authenticated command exit 0, expected JSON keys present, 7 usage rows. Evidence saved as `research/2026-11-11_housekeeping/usage-live-check.json`; no token, account identity or raw account history saved. Existing CourtListener suite: 17 checks PASS, `recap-tests.txt`. No new test or collector.
- Authenticated search was already verified during today's L517 pre-read; OTTO's committed receipt is `AGENTS/OTTO/inbox/2026-11-11_from-DEWEY_courtlistener-search-restored.md`. No duplicate search needed.
- N-PORT: `scripts/nport_holders_README.md`, `scripts/test_nport_holders.py` and `scripts/fixtures/nport_synthetic_primary_doc.xml` already satisfy the WQ-645 README/selftest scope (built under WQ-495.NPORT/L880). Single offline selftest PASS, `research/2026-11-11_housekeeping/nport-selftest.txt`. It validates filtering, column mapping and title-based classes, not network retrieval/pagination or completeness of holdings. No new holder research or schedule.
- Both consumed housekeeping packets moved to this desk's `inbox/processed/`; live backlog and continuity updated. Research residuals remain 003R and L517; this maintenance does not resolve either.

## COMPLETION — DEWEY — 2026-11-11
STATUS: ✅ DONE
CHANGED: recap_pull.py, BACKLOG, continuity, test receipts, this record, processed housekeeping requests, PROME receipt
RESULT: Fixed 1 incorrect endpoint; live usage succeeds and 17 existing CourtListener checks pass. N-PORT's 1 existing offline selftest passes; README confirmed.
GAPS: Tests do not establish live N-PORT source coverage. Desktop verified; laptop token not checked. Recipient consumption unverified.
WILL_NEEDS: None.
FOLLOW-UP: PROME records WQ-645 fulfillment and CourtListener repair receipt.
