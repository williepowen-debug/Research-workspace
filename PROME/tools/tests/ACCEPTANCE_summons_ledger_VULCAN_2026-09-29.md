# ACCEPTANCE — register VULCAN's catalyst ledger in `prome_gate.SUMMONS_LEDGERS` (2026-09-29, prome-82)

**Defect in its own terms (VULCAN 41b210490, relayed by Will 09:57 ET):** VULCAN has missed every pre-committed Friday post-close instrument slot since 8/28 (5 of 5) and all three GPU readings; its dated rows live only in `AGENTS/VULCAN/docket/CATALYSTS.tsv`, which no PROME boot instrument reads, so nothing summons a spawn. LABOR's ledger is the only registered summons ledger (BD-02, 8/20). Fix = PROMOTE the existing control (WQ-229: prefer promoting an existing control to adding a new one): one registry line.

**Acceptance conditions, written before the edit:**
1. A VULCAN row dated within `SUMMONS_WINDOW_DAYS` (2) of today appears in the desk-catalyst-summons advisory with desk name, date, priority and event — today: the 2026-09-30 rows (MU FQ4 · EXIT_PROTOCOL rewrite · S2 re-arm grade · ORCL guarantee).
2. LABOR's rows still appear unchanged (no displacement).
3. VULCAN's PAST-DUE rows still present (8/28 · 9/04 · 9/11 · 9/18 · 9/25 …) flag as past-due — by design ("owners prune fired rows, so past-due-still-present reads as ungraded — the exact BD-02 miss shape"); the check stays ADVISORY; gate rc unchanged.
4. A missing ledger path reads `MISSING`, never a crash (unchanged branch, exercised by pointing at a bogus path in the harness).
5. Schema: VULCAN's header equals LABOR's (`date|event|what_to_check|threshold_signal|priority|who_cares|notes|date_class`) — verified 09:5x ET before the edit.

**Neighbours (WQ-229 five, considered):** ordinary = AC1 · overlap = a VULCAN row that is ALSO a PROME DOCKET row (L114 MU 9/30) flags in both places — acceptable, two nods for one date never spawn twice because `ListAgents` precedes every spawn · wrong owner = a row in VULCAN's ledger naming another desk still summons VULCAN (the ledger is VULCAN's; N/A by construction) · missing information = a row with no parseable date is skipped (existing branch) · concurrent = a live VULCAN session at boot ⇒ doorbell, not spawn (standing preflight).

**Test:** harness below imports `prome_gate`, runs `check_desk_catalyst_summons()` with the real registry and with a bogus path, prints the recorded results.

**State:** IMPLEMENTED · TESTED (author) · NOT independently verified (a one-line registry addition; small self-contained fix per WQ-229 — no reader owed) · the past-due noise is VULCAN's to prune.

**Test result (harness, 10:0x ET):** AC3 ✅ (25 VULCAN past-due rows flag) · AC4 ✅ (`BOGUS ledger MISSING`, no crash) · AC5 ✅ · AC2/AC1 ⚠️ TRUE IN THE FLAG LIST, INVISIBLE IN THE DETAIL: `check_desk_catalyst_summons` sorts flags by date ASCENDING and prints only `detail_bits[:4]` with no full-output log, so with 25 past-due VULCAN rows the four visible bits are all 2026-08-26…08-28 and the in-window rows (VULCAN 9/30 ×4 · LABOR 10/01) sit inside "(+21 more)". The promotion is correct and INEFFECTIVE until either VULCAN prunes its past-due rows (the design's assumption — asked of VULCAN 10:0x, it is live) or the check lists forward-window rows first and summarizes past-due as a count — the latter is a second code change in the same instrument and is NOT made this session (R1 one-change ceiling; DOCKET row registered for DAEDALUS/PROME). Same shape as `finding_display_filter_gating_safety_net`, inverted: the past-due tail gates the forward window.

**State:** IMPLEMENTED · TESTED (author) · NOT independently verified · EFFECTIVE only after VULCAN's prune (owner action) — disclosed in the closeout report as the session's ONE process change (PROCESS class).

**Owner action landed 10:0x ET (VULCAN 45f3fa7f2, on origin):** 18 strictly past-due rows swept verbatim to `AGENTS/VULCAN/archive/CATALYSTS_FIRED_2026-09.tsv` (crc 0xed0ccdc9); VULCAN reports the check now shows only today's and forward rows. Correction to the count above: 25 was the FULL flag count including the 9/29–10/01 in-window rows; 18 were past-due. AC1/AC2 now hold in the visible detail as well; L548's ordering defect stands for the general case.
