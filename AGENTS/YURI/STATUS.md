# YURI STATUS

**Last Updated: 2026-09-26 (Sat, 15:2x ET, from `date`)**: second YURI session (spawned by PROME prome-1d, Tier 1, DOCKET L510, on Will's WQ-293 word of 15:04 ET). *Prior:* 2026-09-25 09:1x ET, the first session. The wiring state of record is `2113b2734`.

**Class:** Market (feeder/intent; never proposes trades) · **Byte budget:** 32,550 B (rotate at ≥75%) · **Convergence handle `Score (1–5)`: 2**, re-scored by YURI this session and unchanged from the placeholder. One custodial seizure instrument is live and extending: Decree-302 list amendments № 661 (17.09) and № 674 (21.09). No mobilisation instrument exists through 25.09. The only new political-calendar instrument is № 680 (new Duma sits 30.09).

## Live intent-reads (`workbook/INTENT_LEDGER.tsv` is canonical; this table mirrors it)

| Row | Claim | Resolve_by | Reading | Status |
|---|---|---|---|---|
| YUR-001 (ex DOCKET L432) | Mobilisation decision after the 9/20 Duma vote | 2026-09-21 | **NOT-DECIDED · PERIMETER PARTIAL (YURI 2026-09-25, window 09-19→09-25)**: 0 mobilisation titles on the pravo presidential block (highest № 680); gaps № 671/673/675/676/677; SecCouncil 24.09 = public security; mil.ru 000 ×4 | OPEN. ⚠️ The perimeter cannot complete as defined, so a re-date/re-scope ruling is owed to PROME. Grade: `research/2026-09-25_L432_YUR-001_GRADE.md` |
| YUR-003 (ex DOCKET L434) | Nestlé/Auchan external management converts to a SALE | 2026-10-02 | Not graded (not due). By-catch 25.09: № 674 (21.09) is a further **custodial** list amendment by title. No disposal act appeared in the presidential block through 25.09. Company names still NOT established (scanned bodies, no OCR). | OPEN |
| YUR-F01 | Desk self-falsifier: ≥3 cross-channel actor calls by 2026-10-24 | 2026-10-24 | **0 of 3.** No call claimed on 2026-09-25: the L432 read is single-channel (mobilisation/political calendar). | OPEN (DAEDALUS grades) |

**L433 (Suwałki-Gap exercise) is NOT this desk's.** It is HAWK's outright: *no Russian instrument located as of 2026-09-19; HAWK's tree grepped.* A re-check re-dates that cell and never re-argues the rule. Not re-checked 2026-09-25.

## Session log
- **2026-09-26 (WQ-293).** Wrote the prospective public-declaration test **YUR-004 as PROPOSED, not registered**, at `research/2026-09-26_WQ-293_YUR-004_declaration-test-PROPOSED.md`. The window runs from № 680 on 26.09 through 10/31. Declaration sources: the pravo presidential block and kremlin.ru. mil.ru is a named unread path on every grade line. An uncovered source resolves STUCK, never MISS. YUR-001's reading is preserved verbatim and was not re-graded. Live probe 19:09–19:14Z: pravo 200 with 0 mobilisation titles (baseline № 680); **kremlin.ru 000 on all six variants** (it was 200 on 9/25), so it is intermittent. Inbox 1/1 drained (PROME WQ-295): cadence declared **WEEKLY**, and 7 WATCH_FOR candidates sent to PROME.
- **2026-09-25 (first session).** L432 graded NOT-DECIDED PARTIAL on the extended window, with primaries fetched 13:08–13:12 UTC. A correction went to HAWK: its 9/21 grade cites "№ 638" for the Military-Industrial Commission amendment, and the primary shows that act is **№ 642**; № 638 is a Hero-of-Labour award. The same wrong number in YURI's own ledger was corrected. Whole inbox drained, 1 of 1 (the DAEDALUS wiring packet), logged to `board_log.tsv` and moved to `inbox/processed/` with a `consume:YURI` commit. First `NEXUS_BRIEF.md` written; NEXUS was packeted to add YURI to `BRIEFS_MAP.md`. Boot reads were declared to PROME through the delivery memo (READS.tsv is PROME's file).

## Registration state
Unchanged from wiring (`AGENTS/DAEDALUS/builds/REGISTRATION_CHECKLIST.md`), plus this session's NEXUS_BRIEF and packets. Still owned elsewhere: WALTER `ROUTING_TABLE` Russia-actor keywords · NEXUS `BRIEFS_MAP.md` row (packeted 9/25) · `PROME/registry/READS.tsv` row (asked 9/25).

## Known limits (declared, not inferred away)
No imagery, SIGINT or paid OSINT. The FIRMS key is UNAVAILABLE (WQ-238). The Russian primaries answer on `http://` only. `mil.ru`, `function.mil.ru` and `structure.mil.ru` return 000 on both schemes (4 variants tried 2026-09-25). `kremlin.ru/acts/news` and `duma.gov.ru/news/` timed out 9/25; the main listings were reachable. Decree bodies are scanned images, so only title-level grep is possible. European single-name equities have NO pricing owner, so YUR-003's route flags PROME.

## BOTTOM LINE
Through 26 September, no Russian-state instrument declares mobilisation at the one declaration source this box reached today: the pravo presidential block, highest № 680, 0 mobilisation titles. kremlin.ru did not answer today. The earlier grade stands exactly as recorded, NOT-DECIDED · PERIMETER PARTIAL (09-19→09-25), and it is not proof that no decision was taken. The most important open item is Will's approval of YUR-004, a forward-only, clearly bounded public-declaration test. Its first checkpoint is the new Duma sitting on 30 September, followed by Friday reads from 10/02 (shared with YUR-003) and a final grade on 10/31.
