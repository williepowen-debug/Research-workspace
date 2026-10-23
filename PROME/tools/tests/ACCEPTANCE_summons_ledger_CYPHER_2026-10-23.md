# ACCEPTANCE — register CYPHER's catalyst ledger in `prome_gate.SUMMONS_LEDGERS` (2026-10-23 00:3x ET, prome-e7)

**Defect in its own terms (CYPHER first-session COMPLETION packet, `PROME/inbox/processed/2026-10-22_from-CYPHER_first-session-COMPLETION.md`, 2ce5419e0, ask 1):** CYPHER is a Tier-2 on-demand desk; its dated rows live only in `AGENTS/CYPHER/docket/CATALYSTS.tsv` (10/27 · 10/29 · 11/04 · 11/15 · 11/18 · 11/20 R1 flip · 12/17 · 2027-01-08 · 2027-01-31). A desk that never boots cannot summon itself, and no PROME boot instrument read that ledger. Same shape as GIBBS 10/21 and VULCAN 9/29.

**Acceptance conditions, written before the edit:**
1. A CYPHER row dated within `SUMMONS_WINDOW_DAYS` (2) of a test date appears in the desk-catalyst-summons advisory with desk name, date, priority and event (test date 2026-10-26 ⇒ the 10/27 eMudhra row).
2. The existing registered desks (LABOR · VULCAN · VIOLET · GIBBS) still appear unchanged on today's date (no displacement).
3. Gate rc unchanged — the check stays ADVISORY.
4. A missing ledger path reads `MISSING`, never a crash (unchanged branch, exercised with a bogus path).
5. Schema: CYPHER's header equals LABOR's (`date|event|what_to_check|threshold_signal|priority|who_cares|notes|date_class`).

**Neighbours (WQ-229 five, considered):** ordinary = AC1 · overlap = CYPHER's 10/29 R1 re-check is ALSO DOCKET L812 — two nods for one date never spawn twice because `ListAgents` precedes every spawn · wrong owner = a CYPHER row naming DEWEY (10/29 008R rerun) summons CYPHER to READ the rerun, never DEWEY — the owner column of the ledger is CYPHER's, N/A for this instrument · missing information = an undated row is counted in `undated` and skipped (unchanged branch) · concurrent activity = CYPHER live in Will's window (`cypher-be`) at registration time; a summons flag with a live owner is a doorbell, not a spawn — the rule text already says ListAgents first.

**Test (harness, 00:3x ET; `pg.results` read after each call, bogus path appended last):** AC1 ✅ (`CYPHER 2026-10-27 [P2] Chrome Root Store v43 removes emSign ECC Root (in 1d)` at test date 10/26) · AC2 ✅ (GIBBS and VULCAN TODAY rows unchanged on 10/23) · AC3 ✅ (record severity ADVISE, unchanged) · AC4 ✅ (`BOGUS ledger MISSING`) · AC5 ✅ (headers byte-equal).

**State:** IMPLEMENTED · TESTED (author) · NOT independently verified (a one-line registry addition; small self-contained fix per WQ-229 — no reader owed). The boot gate that ran this session (00:30 ET) predates the edit; the next boot's advisory carries CYPHER. Disclosed in the boot report as this session's ONE process change (purpose class DOMAIN: a desk wake, GIBBS precedent "SUMMONS_LEDGERS registration = PROME process slot").
