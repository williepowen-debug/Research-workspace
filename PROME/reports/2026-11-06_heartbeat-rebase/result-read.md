# RESULT read, HEARTBEAT.md 38th base (cold)
Checks 1,2,3,5,6: PASS. (1) archive == before.md (cmp). (2) HEARTBEAT.md == candidate.md (cmp). (3) HEARTBEAT_COLD.md not in git status (unchanged). (4) 27 backticked repo pointers incl. gate.txt in /tmp all resolve. (5) book line identical to will_brief.py --book-line output. (6) ORCL CDS line (342.5 [10/20], 305 [11/5], 306-314 conv, ~318 disseminated, partial to ~15:50 ET) matches REPORT.md table + receipt rows.
(7) Calendar Nov 9-13 and BOJ 12/18: traced, all hold (see rows below).

Fields: claim | artifact | command | observed | proposed change

## ❌
1. "Dealer gamma -> path | Negative everywhere; walls overhead" (HEARTBEAT L49) | AGENTS/HENRY/STATUS.md L24 | grep QQQ gamma row | HENRY: QQQ spot 662.66, wall "650 at both, clean: the only published wall under spot on any chain". HEARTBEAT's own L16 has QQQ 11/6 close $656.10, wall 650, i.e. under spot. SPX 7,500 is overhead, QQQ 650 is not. | "SPX walls overhead; QQQ 650 wall under spot".

## ⚠️
2. Near-term calendar (L68) omits Mon 11/9 3Y auction and Thu 11/12 30Y auction / BND-33 resolution (BOND frozen bars, DOCKET L924), though Tue 10Y is listed | AGENTS/BOND/STATUS.md L60, DOCKET L924 | grep | BND-33 resolves at the 30Y grade 11/12; absent from calendar and from channel 2 | add or say BOND owns it.
3. Wed 11/11 is Veterans Day; REG-T-04 "3 prints above 350" counts a published HY series. DOCKET L711 says REGINALD must confirm holiday NON-SESSION counting before 11/11. HEARTBEAT L6/L47 gives no hint the print count may skip 11/11 | DOCKET L711 | grep | counterexample: HY prints Mon 11/9, Tue 11/10, then nothing 11/11; "3 above 350" earliest-date is not stated | one clause naming non-session rule.
4. Ch2 "SOFR99-IORB +10 bp" vs central judgment and dashboard "SOFR-IORB +2 bp" (L6, L32) | LIQUID STATUS L22 | grep | both right (SOFR99 vs SOFR) but a stranger sees two figures for "funding"; ARM keys on SOFR99 | label the SOFR (median) one in the central line.
5. L6 "high yield widened ... [11/5], the 2026 high" and "widest since 353 [5/9/2025]" (L12): HENRY says series as served starts 11/7/2023, so "widest since" is bounded by that vintage | HENRY STATUS L15 | grep | basis omitted | add "(series from 11/7/2023)".
6. Ch2 "December hike 76%" and ORACLE 77.5/78 while central judgment says "about 76-78" and SAM says 77-79 | HENRY L13, SAM L5 | grep | consistent within the stated spread, but three desks' figures, all vendor | none needed beyond keep labels.
7. Gate pointer `/tmp/prome-boot-87b629ed/.../gate.txt` (L58) resolves now (5231 B, 16:28) but is volatile storage; a later cold reader on another boot cannot resolve it | ls | exists today | cite durable copy or accept.

## Traces (✅)
Sat 11/7 OP-SCALE-01 (GATES, DOCKET L37) and Call Report run (L180); Mon 11/9 CRMT STD (BROCK, DOCKET L927), FLG 10-Q ~11/9 EST (L522); Tue 11/10 SoftBank 15:30 JST = 01:30 ET (SAM funding stack s6), CPI, 10Y auction (BOND), CoreWeave, NY Fed HHDC 11:00 ET (OTTO), MOFCOM (ZHAO), NEXUS L554, STEO (BRENT); Wed 11/11 FALCON-001 review 11/11 (GATES); Thu 11/12 Nebius/Athene (ellison synthesis), BRT-34, MSI #13 (CORAL); Fri 11/13 PPI (HENRY), CFTC W1 ~11/13, CABO (BROCK), COT #14 (BRENT). BOJ MPM Dec 17-18 (SAM L77) so "12/18 decision" correct. Gate reviews 069/079 11/12, 076 11/13, BRK-R2 11/16 then 12/7, all match GATES.
Counterexample devised: HY print-count across Veterans Day (row 3); QQQ wall vs spot (row 1).

VERDICT: Installed file is byte-faithful and almost wholly correct against desk STATUS; one wrong basis (QQQ wall "overhead") and a few omissions; usable after the one-clause fix.
