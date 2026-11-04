# WQ-31 desktop FFIEC access — blocked

Observed November 4, 2026, 22:08 UTC on hostname DESKTOP-BC6EF81. User authorized credential reconciliation, two access controls, and conditional complete Q3 WAL retrieval/handoff. Existing canonical credential home is gitignored `FORGE/tools/market-data/.env`; request authentication was supplied to curl over stdin, never arguments or persistent request files.

The desktop canonical token's decoded expiry is 2026-11-05 19:02:19 UTC. This is metadata, not proof of validity. The renewed laptop credential recorded in WQ-31 expires 2027-01-31 02:28 UTC and is absent from the approved desktop locations checked: canonical .env, repository-root secondary .env, process environment. No credential changed; no transcript/history credential recovery attempted.

Both `RetrieveReportingPeriods` and the known-period `RetrieveFacsimile` control (WAL RSSD 3138146, 20260630, SDF) returned HTTP 500 with application code 5002. Curl completed normally (rc 0). Sanitized endpoint/time/parameter/status/length/hash receipts are in `controls.json`; response bodies, authentication headers and credential values were not retained. The application code is reported without assigning an unverified meaning.

**Specific blocker:** the renewed credential has not been securely installed on this desktop, and both authenticated controls fail with the currently configured credential. This does not prove non-filing or absence of Q3 data, nor establish that credential replacement alone will fix service access.

**Next action:** through the established local credential method, put the renewed FFIEC PWS token for the recorded `williepow` account in this desktop's gitignored `FORGE/tools/market-data/.env` (`FFIEC_CDR_TOKEN`, with matching `FFIEC_CDR_USERNAME`). Do not put the token in chat, packets, tracked files or shell arguments. Then repeat both controls. On success retrieve the full 20260930 SDF for RSSD 3138146, verify bank/date and payload structure, preserve original response/decoded filing with hashes and provenance, and send WAL the durable source for independent extraction.

WQ-31 / WQ-495.CDR remain open; no new decision or duplicate task created. No Q3 filing retrieved and no extraction handoff claimed. WALTER's recovery search and WAL's completed grading were not repeated. This is a bounded access attempt, not a new monitor or tooling installation.
