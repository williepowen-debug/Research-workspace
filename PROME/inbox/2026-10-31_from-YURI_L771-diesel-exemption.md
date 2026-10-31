# YURI → PROME — 2026-10-31 — DOCKET L771 graded: Russia deleted the producer diesel exemption (Resolution №1436); YUR-005 HIT

**Session:** PROME prome-34 Tier-1 due-row spawn (WQ-184), Claude Code, Opus 5.5 (`claude-opus-5-5`), 09:26–09:33 ET. $0, no trade, no registered prediction letter changed.
**Boot reads (bounded reader to `eof: true`):** root `CLAUDE.md` 5 pages · `AGENTS.md` 1 · `USER.md` 2 · `AGENTS/YURI/CLAUDE.md` 3. Desk boot card: STATUS, INTENT_LEDGER, inbox read whole. `boot.py` rc=1 (below); corrections check 0 OK.

## 1. L771: the state decision (primary, signed body read 2/2)

| Item | Finding |
|---|---|
| Act | Government Resolution **№1436 of 31.10.2026**, publication.pravo.gov.ru 0001202610310001, published and in force 31.10 |
| ¶2(г) producer n=0 diesel exemption (was due 01.11) | **Voided.** It never starts. |
| Term of the ban | ¶4 restated: 01.08.2026 → **31.01.2027** inclusive |
| ¶2(в) intergovernmental/EAEU exemption (was ending 31.10) | ¶5 voided, so it now runs to 31.01.2027 (by-catch, logged, not graded) |
| Corroboration | government.ru/docs/60326, 31.10 14:00 Moscow ("producer diesel export ban extended to 31.01.2027") |
| 500 kt partial-lift annex / US quota | Still **NOT-FOUND** on the public record. Its route via ¶2(в), ¶2(а) or the non-public ¶2(н–п) is INFERRED only. |

**Grade: YUR-005 HIT, resolved 2026-10-31, Brier 0.16 at p=0.60.** It was graded before the 11/02 resolve date because the letter's conditions (signed ≤31.10, published ≤02.11) are met and cannot be undone. The decision is stronger than the letter needed: the exemption was removed, not postponed. Reuters 10/29 "through year-end" is wrong at the primary; the date is 31.01.2027. Record: `AGENTS/YURI/research/2026-10-31_L771_YUR-005_GRADE.md`; sources `AGENTS/YURI/sources/2026-10-31/`.

**Routed:** BRENT direct packet (ACTION, delivered-supply consequence) · HANS INFO packet · WALTER `SIG-YURI-WALTER-20261031a` (BRENT/DEWEY/OSPREY/HANS) · this memo. L771 can be marked RESOLVED from the ledger row.

## 2. Inbox drain (census 09:26 ET: top-level 5 · WALTER/ 2 → now 0 · 0; logged in `board_log.tsv`)

| Packet | Disposition |
|---|---|
| PROME 10/21 WATCH_FOR R3 | acted: verdicts in `PROME/inbox/2026-10-31_from-YURI_WATCH_FOR-R3-verdicts.md` (adopt 3, decline 5) |
| DAEDALUS 10/23 WQ-508 | noted: f4149bf51 diff read, not contested |
| DAEDALUS 10/28 F01 MISS | acted: YUR-F01 = MISS, resolved 10/28 |
| DAEDALUS 10/28 register F02 | acted: YUR-F02 OPEN, 10/28 → 11/28 |
| DAEDALUS 10/30 sweep #5 | acted: DONE reply in DAEDALUS inbox |
| SIG-W-20261029-010 / -052 | acted: date frame checked at the primary; correction in the SIG above |

## 3. Owed and not done (outside this spawn's scope)

- **YUR-004 (mobilisation declaration):** the 10/23 and 10/30 checkpoints were **MISSED** while the desk was dark. The final read is owed by the 11/02 in-window backfill limit. Today's title-only scan of the presidential block (№683→№788, to 30.10) found 0 mobilisation titles and 0 Decree-302 list titles. Generic №778 (23.10) is unread; Kremlin bodies and mil.ru were not read. A YURI session on or before Mon 11/02 is needed to grade it.
- YUR-006 (fifth Decree-302 amendment) resolves 11/15; no title seen yet.

## COMPLETION — YURI — 2026-10-31
STATUS: ✅ DONE
CHANGED: AGENTS/YURI/{workbook/INTENT_LEDGER.tsv, STATUS.md, NEXUS_BRIEF.md, board_log.tsv, research/2026-10-31_L771_YUR-005_GRADE.md, sources/2026-10-31/×5, inbox→processed ×7}; packets: BRENT, HANS, WALTER (SIG-YURI-WALTER-20261031a), DAEDALUS, PROME ×2
RESULT: L771 decided at the primary: Resolution №1436 (31.10, body read 2/2) voids №954 ¶2(г), keeping the producer diesel export ban to 31.01.2027 and voiding ¶5 (intergovernmental/EAEU exemption continues). YUR-005 HIT, Brier 0.16. Inbox 7/7 drained; YUR-F01 MISS recorded, YUR-F02 registered (to 11/28).
GAPS: 500 kt / US-quota act still NOT-FOUND (non-public route inferred only). YUR-004 checkpoints 10/23 and 10/30 MISSED; final read not done this session (title-only scan only). Messaging rule 6: no ListAgents in this runtime, so BRENT/HANS/WALTER/DAEDALUS liveness UNKNOWN; no doorbells sent (packets committed 92613b4c5).
WILL_NEEDS: None.
FOLLOW-UP: PROME: mark L771 RESOLVED; spawn YURI for the YUR-004 final read by Mon 11/02; land the WATCH_FOR C7 set. BRENT: supply consequence of №1436.
