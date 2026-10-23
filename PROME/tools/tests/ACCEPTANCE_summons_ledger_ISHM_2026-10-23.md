# ACCEPTANCE — register ISHM's catalyst ledger in `prome_gate.SUMMONS_LEDGERS` (2026-10-23 09:52 ET, prome-03, desktop)

**Defect in its own terms (DAEDALUS changelist `PROME/inbox/processed/2026-10-23_from-DAEDALUS_ISHM-built-registration-changelist.md`, action 2; scaffold 080fbc7d6):** ISHM is a Tier-2 print-driven desk built this morning under WQ-506 (Will 09:35 ET). Its dated rows will live only in `AGENTS/ISHM/docket/CATALYSTS.tsv` (rows land in DAEDALUS's follow-up commit after the issuer release-calendar verification). A desk that never boots cannot summon itself; the boot gate's BD-02 check is the only wake carrier, and it reads only ledgers named in `SUMMONS_LEDGERS`.

**Acceptance conditions, written before the edit:**
1. On today's date the advisory names ISHM as `EMPTY-FORWARD (no row within 14d)` — the ledger has its header only, so the correct state is "registered, empty", never silence (the 2026-10-10 VIOLET shape).
2. The existing registered desks (LABOR · VULCAN · VIOLET · CYPHER · GIBBS) still appear unchanged on today's date (no displacement): VULCAN's three TODAY rows still print.
3. Gate rc unchanged — the check stays ADVISORY.
4. A missing ledger path reads `MISSING`, never a crash (unchanged branch, exercised with a bogus path).
5. Schema: ISHM's header equals LABOR's byte for byte (`date|event|what_to_check|threshold_signal|priority|who_cares|notes|date_class`).

**Neighbours (WQ-229 five, considered):** ordinary = AC1 · overlap = an ISHM print date that is ALSO a DOCKET row naming ISHM yields two nods for one date; `ListAgents` precedes every spawn, so never two spawns — same as CYPHER · wrong owner = an ISHM row naming CARL (the consumer read of the same print) summons ISHM to read, never CARL — the ledger's owner column is ISHM's, N/A for this instrument · missing information = the empty ledger IS the case, AC1 · concurrent activity = DAEDALUS's follow-up commit adds rows while this registration stands; the check reads the live file at every boot, so the rows appear at the next boot with no further registration — N/A.

**Test (harness, 2026-10-23 09:52 ET; `pg.results` read after each call, bogus path appended last):** AC1 ✅ (`ISHM ledger EMPTY-FORWARD (no row within 14d)` at 10/23; also at 11/22, beside LABOR · VIOLET · CYPHER · GIBBS which are empty that far out) · AC2 ✅ (VULCAN's three 10/23 TODAY rows unchanged) · AC3 ✅ (record severity ADVISE, unchanged) · AC4 ✅ (`BOGUS ledger MISSING (AGENTS/NOPE/x.tsv)`) · AC5 ✅ (headers byte-equal, 8 columns).

**State:** IMPLEMENTED · TESTED (author) · NOT independently verified (a one-line registry addition; small self-contained fix per WQ-229 — no reader owed). The boot gate that ran this session (08:30 ET) predates the edit; the next boot's advisory carries ISHM. Disclosed in the session report as process change 2 of 5 (purpose class DOMAIN: a desk wake, the GIBBS and CYPHER precedent).
