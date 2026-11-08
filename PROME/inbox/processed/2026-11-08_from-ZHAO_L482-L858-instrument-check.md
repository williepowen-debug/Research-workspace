# ZHAO -> PROME: L482 and L858 instrument check, done 11/08 (a day early)

**From:** ZHAO, Claude Code subagent (model Opus 5.5, claude-opus-5-5), spawned by PROME prome-bf on Will's word 11:59 ET. Repo `/home/willi/Research-workspace`, branch master. Written 2026-11-08 12:09 ET (by `date`). Record: `AGENTS/ZHAO/workbook/KB.tsv` KB-ZHAO-242 to 245.
**Boot reads (bounded reader, each to `eof: true`):** root `CLAUDE.md` 5 pages · `AGENTS.md` 1 page · `USER.md` 2 pages · `AGENTS/ZHAO/CLAUDE.md` 6 pages. Plus STATUS, the 11/06 run book, the corrections check (rc 0). `boot.py` not run (no market data needed for this task).

## One line per row (all reads 2026-11-08 12:01 to 12:07 ET, at the primary)

| Row | Result | Primary checked |
|---|---|---|
| **L482** extension paper | **NOT FOUND**: no new official document matching the 2027-01-10 extension beyond BIS FR 2026-22793 (already logged 11/05) | FR API public inspection (current list 103 docs; available_on 11/07, 11/08, 11/09 = 0) and documents; govinfo FR-2026-11-09 issue (complete, 98 docs); whitehouse.gov actions (newest 11/05), fact sheets (newest 11/05), briefings (newest 11/07); MOFCOM live list via unit API (stamp 18:01 Beijing 11/08); Customs Tariff Commission (newest 2026-04-28) |
| **L435** BIS Affiliates Rule stay | **FOUND, PUBLISHED**: 91 FR 70789-70790 in the 11/9 issue, text unchanged ("further stayed until January 10, 2027"). Run-book branch C did not occur | govinfo `FR-2026-11-09/html/2026-22793.htm` |
| **L437** MOFCOM/GAC 公告70 | **NOT FOUND**: no re-suspension; newest 公告 still 第56, 57号 (11/06). Clock stays ARMED, reads to 11/10 | mofcom.gov.cn unit API with parseType=bulidstatic; home page |
| **L858** USTR ship-fee final | **NOT FOUND**, published or on public inspection. The 11/9 issue is complete without it, so FR publication before 11/9 23:59 ET can no longer happen; a Monday public-inspection filing for the 11/10 issue still can | FR API (USTR documents newest 11/02; public inspection); govinfo 11/9 issue; ustr.gov press releases (newest the 11/06 Greer-He readout) |
| **L858** China MoT mirror | **NOT FOUND** (no re-suspension) on the MoT home page; the notices list needs JavaScript, so SEARCH-NOT-FOUND, not VERIFIED. Primary of the clock itself READ: MoT 公告2025年第60号 suspends the US-ship port fees 1 year from 2025-11-10 13:01 Beijing, "in sync with" the US suspension | xxgk.mot.gov.cn t20251104_4179268; mot.gov.cn home |

## The three 11/10 clocks, kept separate

1. **L435 BIS Affiliates Rule stay: 🟢 resolved on paper.** Published. The US perimeter does not widen on 11/10; the next cliff is 1/10 to 1/11. ZHA-19 still grades on the 11/10 record per its letter; not graded early, not re-marked.
2. **L437 MOFCOM/GAC 公告70: 🔴 still armed.** No Chinese paper. ZHA-20 stays 85%. A second adverse input arrived after the mark: MOFCOM's 11/07 spokesperson answer says the US is "departing from the important consensus reached by the two heads of state" (KB-244). Logged, not scored. Read at the Beijing 11/10 close (11/11).
3. **L858 USTR ship fees: 🟠 open.** ⚠️ **The row's consequence clause is wrong on its own evidence.** It reads "no final notice in the FR before 11/9 23:59 ET means fees resume 11/10". But FR 2026-21755 itself records that last year's suspension ran from 12:01 a.m. 11/10/2025 under a notice published 11/13/2025, three days late, and MOFCOM 令2025年第7号 shows the US announced on 11/9 ET. The operative fact is a USTR determination, which may appear by press release or public inspection before FR publication. On the row's letter the FR-publication leg is settled NO, but the fee outcome is UNKNOWN until USTR acts.

## New, flagged and not registered

- **A fourth ships-linked Chinese clock:** MOFCOM 令2025年第7号 suspends the countermeasures on Hanwha Ocean's five US subsidiaries for 1 year from Beijing 2025-11-10, keyed on the US s.301 suspension. No DOCKET row names it. It belongs beside L858. Registering it is PROME's decision.

## Inbox

Whole inbox drained: 1 file (top level), 0 in the WALTER lane. The NEXUS B24 brief-pin packet was filed to `processed/` (KB-245, board_log). Action 1 (the NONE token) is in. Action 2 (`CLAUDE.md:37`) is a charter edit that waits for Will's word, held in STATUS NEXT ACTIONS 9 with the WQ-622 line (290 B of cap room). Charter not edited.

## Packets (FYI, no ask, so no rule-6 doorbell owed)

`AGENTS/{BRENT,WATT,VULCAN,HAWK,HENRY}/inbox/2026-11-08_from-ZHAO_11-10-clocks-instrument-check.md`. ⚠️ ZHAO's charter MAIL rule says outbox plus a route for PROME. I used direct inbox delivery under carve-out ① because the spawn brief said to.

## Unreachable

GAC (customs.gov.cn HTTP 412) · the MoT notices list (JavaScript only) · 公告2025年第72号 primary · 公告 39/43/45/47 and 54/55/58 still unlocated. China's own readout of the 11/06 call has not been found.

```
STATUS: ✅ DONE
CHANGED: AGENTS/ZHAO/{STATUS.md, NEXUS_BRIEF.md, workbook/KB.tsv, board_log.tsv, inbox/processed/2026-11-06_from-NEXUS_brief-pin-B24-decision.md}, 5 FYI packets (BRENT, WATT, VULCAN, HAWK, HENRY), this memo
RESULT: L482 NOT FOUND (no new extension paper). L435 BIS stay PUBLISHED 11/9 at 91 FR 70789, unchanged. L437 MOFCOM 公告70: no re-suspension, still armed, ZHA-20 85% held with a 2nd adverse input (KB-244). L858: no USTR final; FR publication before 11/9 23:59 ET now impossible, but 2025's final came 3 days late, so fee resumption is UNKNOWN, not implied. MoT mirror 公告60 primary read; no re-suspension seen.
GAPS: GAC 412; MoT notices list needs JavaScript (home page only); China's readout of the 11/06 call not found.
WILL_NEEDS: The two ZHAO charter lines (WQ-622 line; NEXUS B24 at CLAUDE.md:37), unchanged from 11/06.
FOLLOW-UP: 11/10: ZHA-19 grade + USTR determination + China mirrors (MoT 公告60, MOFCOM 令7); 11/11: ZHA-20 at the Beijing close. PROME: fix L858's consequence clause; decide on a row for MOFCOM 令2025年第7号.
```
