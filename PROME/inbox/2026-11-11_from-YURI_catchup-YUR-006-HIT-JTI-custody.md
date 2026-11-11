# 2026-11-11 · from YURI → PROME: catch-up done; YUR-006 HIT (Japan Tobacco's Russian business under state custody)

**Session:** PROME prome-2b catch-up wake (Will 09:24 ET). Claude Code subagent, Opus 5.5 (`claude-opus-5-5`), 09:36 ET onward. Desk commit `8389e02f8b`. Record: `AGENTS/YURI/research/2026-11-11_L772_YUR-006_GRADE-and-catchup.md`.

## What changed in YURI's read since 2026-11-02, in plain words

1. **Russia seized control of Japan Tobacco's Russian business.** On 5 and 6 November Putin signed two decrees, Указ №817 and №832. Together they put all seven JTI companies in Russia under state "temporary management" by a firm called АО «Промышленные активы». YURI read both decrees in full at the official legal portal. Neither contains a sale or transfer clause: the owner keeps title on paper and loses control.
2. **That answers DOCKET L772 early: YES, so YUR-006 is a HIT.** The row asked whether a fifth amendment to the seizure list (Decree 302) would appear by 15 November. Two appeared. Brier 0.09 on the 0.70 forecast.
3. **The seizures did not pause for the peace talks.** On 6 November Putin told his Security Council that US–Russia–Ukraine talks would start "next week, Tuesday" in the UAE, and he signed the second JTI decree the same day. The talks opened 10 November in Abu Dhabi; that date comes from press reports, not a primary read.
4. **Japan Tobacco stock has already fallen 28%.** It closed at ¥7,769 on 5 Nov, before the decree, and at ¥5,562 on 11 Nov. It was locked limit-down on 6 and 9 Nov.
5. **No Russian decision on gas.** The US proposal to restart gas transit has no Russian instrument behind it. Peskov said on 2 Nov that a restart is "impossible", but that comes from press reports only. The government did add two export controls: a 3-month ban on aromatics exports (№1443, 31 Oct) and fertilizer export quotas for December to May (№1457, 5 Nov).

## Row-by-row

| Item | State | Evidence / note |
|---|---|---|
| **DOCKET L772 / YUR-006** | **ANSWERED: HIT 2026-11-11** | Two qualifying list amendments. №817 (signed and published 05.11, pravo eo 0001202611050002, 3/3 pp) adds items IV-93..99. №832 (06.11, eo 0001202611060040, 2/2 pp) adds III-57 and IV-100..101. Kremlin acts 81186/81193 corroborate. Disposal or buyer clause: none. Brier 0.09. PROME may close the row. |
| YUR-004 | MISS 11/02 (unchanged) | 60 presidential titles 23.10 → 10.11: no mobilisation title. №800/№803/№830 are MoD regulation titles; bodies not read. |
| YUR-005 | HIT 10/31 (unchanged) | government.ru docs 23.10 → 10.11: no new diesel act after №1436 |
| YUR-F02 (DAEDALUS grades 11/28) | OPEN | Call record **YUR-C01** written 11/11 09:42 ET (record §4). Call: the custody track runs independently of the talks track. Falsifier: any JTI interest removed from the №302 list, or a buyer or disposal named for it, by 11/28. YURI claims no credit; whether the channels fit is DAEDALUS's call. |
| Score (1–5) | 2, unchanged | Custody widening plus talks; no mobilisation declaration |
| Inbox | Drained: 0 top-level + 7 WALTER | Two ACTION cards: -030 (gas proposal ≠ decision, no row) and -060 (8 headlines; none passes the document test). Five INFO cards noted. All logged in `board_log.tsv`, moved with `consume:YURI`. |
| Corrections boot leg | 0 OK | `corrections_boot_check.py YURI` rc 0 |

## Routing PROME should carry (this session's limit was one packet, so YURI sent no others)

| To | What | Why |
|---|---|---|
| **TERRY** | Tradeability finding below | Will's 11/10 standing word: check every material finding for tradeability |
| WALTER | SIG for №817/№832 (JTI custody) plus №1443 and №1457 | Charter: never route around WALTER. No `SIG-YURI-WALTER-*` file was dropped this session because of the one-packet limit. |
| SAM | Japanese state is JT's largest holder (37.55%, relayed) and Tokyo protested 11/06 | Japan channel; whether SAM covers it is SAM's call |
| HANS / HAWK | Custody track continues during talks: HAWK's reaction leg, including its null | Boundary: HAWK owns the reaction |
| FERT | №1457 fertilizer quotas >18.8 Mt (N >11.3 Mt, AN >2.3 Mt, complex >7.5 Mt), 01.12.2026–31.05.2027 | Routine renewal; not potash |
| BRENT | №1443: benzene, toluene, o-/p-xylene and phenol export ban outside the EAEU, 3 months from 31.10 | Products consequence is BRENT's |

## Finding for TERRY (a finding, not a trade; YURI never proposes trades)

**The finding:** Russia's Decree-302 list now covers 100% of JTI's Russian group, seven companies, under custody with no sale clause. That comes from primary reads of №817 and №832.

**What the tape shows:** Japan Tobacco (TSE 2914; US ADR JAPAY) fell 28.4% from ¥7,769 (5 Nov close) to ¥5,562 (11 Nov close). The yfinance daily bars were pulled 11/11 09:40 ET, after the Tokyo close. The 6 and 9 Nov sessions were locked limit-down. JAPAY shows ⚠stale on `fetch.py`.

⚠️ **Sourcing weakness, which must travel with the finding.** These figures are press relays (Reuters, Nikkei, Japan Times), not read at JT's filings:
- Russia is about 10% of JT revenue and about 25% of adjusted operating profit.
- Japan's Ministry of Finance holds 37.55% of JT.
- JT says Russian operations continue and the impact is under review.

**Inference (YURI's, not verified):** a 28% fall against a 25% profit share looks like the market has priced close to a total write-off of the Russian business.

**Historical pattern (context, not a forecast):** earlier custody cases (Danone, Carlsberg) ended in forced sales at a deep discount, not in returns. YURI's YUR-C01 falsifier would catch a return by 11/28. Whether any of this is mispriced is TERRY's question. NO CARD is a complete answer.

## Could not read
- **JT issuer disclosures** (jt.com, TSE filings): the 10% / 25% / 37.55% figures stay unverified.
- **Abu Dhabi talks outcome** at a primary; the second day, 11/11, was not yet reported.
- **Peskov 02.11** at a primary.
- **Manager identity:** which «Промышленные активы» manages the assets.
- **Part-read bodies:** №827 page 2, №799 pages 2–3, №801 pages 2–7.
- **Not probed:** ЕГРЮЛ for JTI entities, and mil.ru.

## COMPLETION — YURI — 2026-11-11
STATUS: ✅ DONE
CHANGED: AGENTS/YURI/{STATUS.md, NEXUS_BRIEF.md, board_log.tsv, workbook/INTENT_LEDGER.tsv, research/2026-11-11_L772_YUR-006_GRADE-and-catchup.md, sources/2026-11-11/* (30 files), inbox/WALTER/processed/ ×7}; this packet
RESULT: YUR-006 / DOCKET L772 HIT on primaries. Указ №817 (05.11) and №832 (06.11) put seven JTI Russian companies under custody, no sale clause; Brier 0.09. Inbox 7/7 drained; feeds refreshed to 10–11.11; F02 call YUR-C01 written; Score 2 unchanged.
GAPS: JT issuer figures are press relays; Abu Dhabi outcome and Peskov not read at a primary; one-packet limit means no WALTER SIG, HANS, SAM, FERT or BRENT packets were sent (PROME relays); no push (PROME pushes).
WILL_NEEDS: None. A TERRY read on Japan Tobacco is offered as a finding.
FOLLOW-UP: PROME closes DOCKET L772 (HIT), relays the routing table, and sends TERRY the JT finding. DAEDALUS grades YUR-F02 on 11/28, YUR-C01 included.
