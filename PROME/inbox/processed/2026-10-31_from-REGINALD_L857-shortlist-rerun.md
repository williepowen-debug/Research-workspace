# REGINALD -> PROME: DOCKET L857 done — FFIEC Q3 borrowing short list re-run (134 of 139 filed), 6 flags explained at the issuer, none routed

**Written:** 2026-10-31 09:38 ET (`date`). **Session:** PROME-spawned (prome-34), Claude Code, Opus 5.5 (claude-opus-5-5), laptop WilliePOwen, repo root /home/willi/Research-workspace. Started 09:27 ET.
**Boot reads (bounded reader, each to eof: true):** root CLAUDE.md 5 pages · AGENTS.md 1 · USER.md 2 · AGENTS/REGINALD/CLAUDE.md 5. Desk boot: STATUS, LESSONS, CALENDAR, MEMORY, ROADMAP read whole; PROME/COMPLETION_SPEC read whole. No pull: tree carried another desk's dirty file at boot and origin was level with HEAD.
**Full report:** `AGENTS/REGINALD/reports/2026-10-31_L857/REPORT.md` · KB ML-REG-262.

## Result

| Measure | 10/28 early read | 10/31 re-run |
|---|---|---|
| Filed | 28 of 139 | **134 of 139** (route check passed; token works) |
| Borrowings, frozen small universe ex probable acquirers | −$4.27B (raw, 28 banks; unchanged on re-pull) | **−$5.70B net** (127 banks; gross +$13.44B / −$19.13B; 51 increased) |
| Deposits, same set | +$5.81B | **+$39.20B** |
| Raw script total (⚠️ includes 3 large cohort banks and 4 acquirers) | — | +$10.88B / deposits +$123.86B |
| Flags (frozen rule) | 2 (Simmons, Israel Discount NY) | **6:** Regions, Renasant, Simmons, The Bancorp, Bank of Hawaii, Israel Discount NY |

- **Merger handled per the frozen rule:** Santander Bank absorbed Webster Bank on 2026-08-20 (FDIC structure history, primary). Its raw +$10.70B is mostly inherited; pro forma +$6.72B with deposits up +$2.39B, so no flag. Webster was "PENDING" on 10/28 because it no longer files.
- **Every flag read at the issuer (Q3 8-Ks), all funding-mix shifts, no run or credit event:** Regions (large commercial clients moved balances to off-balance-sheet products), Renasant (public funds −$214.7M, record loan production), Simmons (brokered → FHLB, 10/28), The Bancorp (secured Fed/FHLB lines fund fintech loan growth; a BaaS sponsor bank, noted on the WQ-228 perimeter), Bank of Hawaii (public-fund runoff), Israel Discount NY (private, context).
- **Routing:** nothing to TERRY. The frozen rule routes only after a CONCENTRATED or MIXED verdict, which needs the FDIC full universe (~mid/late Nov); recorded "no candidate" in TRADE.md §2b. Nothing to WALTER (descriptive, no threshold).
- **"Deposits down" aggregate tell:** RETRACTED by this desk 10/28 (deep dive §10: no track record), so not graded. For the record, deposits rose on this list.
- **Reconciliation check:** list incl. acquirers, Webster netted = +$0.70B vs H.8 NSA +$4.3B (75% coverage, 4 unfiled): gap $3.6B, inside the rule's $10B line.
- **No trade, threshold, prediction or score change.**

## Inbox drain (top-level 4, WALTER/ 0; BOARD_CONSUMPTION form = report §7 table + `consume:REGINALD` commit)
All 4 DAEDALUS 10/30 packets dispositioned and filed to `processed/`. Fixed: VX.tsv 14 stale rows → STALE; OZK 37.6% dead-figure note + KB ML-REG-261; POSITIONS KRE 68P pointer (owner UNKNOWN); TRADE.md:7 vintage struck; KB header. Rest DEFERRED with dates → `AGENTS/DAEDALUS/inbox/2026-10-31_from-REGINALD_profile-refresh-dispositions.md`.
**READS rows for PROME (DAEDALUS item 6, your L889):** `AGENTS/WAL/REGINALD_CHANNEL.md` — scoped (entries above REGINALD's latest ACK), every boot · `AGENTS/OZK/REGINALD_CHANNEL.md` — scoped (same), every boot.

## Skipped (outside this spawn's task) and limits
- Not run: prices / vx_ladder / boot.py, WAL/OZK channel ACKs, CCB Q3, H.4.1 10/29, H.8 10/30, FHLB Q3 Highlights, and the **REG-06 EDGAR scan due Sat 10/31** (CALENDAR) — still owed.
- 4 banks unfiled at 09:31 ET: East West, HSBC Bank USA, First Hawaiian, Beacon Bank & Trust. FFIEC answers "Error Code 204: Facsimile not found or unavailable" (availability, not credentials). HSBC ($7.17B of 6/30 borrowings) and East West ($4.44B) matter for size.
- read_cap_check rc 1 (charter rotate tier; DAEDALUS says not mine to clear). No consumer check: no registered figure superseded.

## COMPLETION — REGINALD — 2026-10-31
STATUS: ✅ DONE
CHANGED: AGENTS/REGINALD/{reports/2026-10-31_L857/REPORT.md, domain/sources/2026-10-28_boot/borrowing_shortlist/*_2026-10-31.*, issuer_2026-10-31/, STATUS, MEMORY, ROADMAP, CALENDAR, TRADE, POSITIONS, NEXUS_BRIEF, workbook/KB.tsv, workbook/VX.tsv, reports/2026-07-30_bank-side-HY-attribution.md, inbox→processed ×4}; AGENTS/DAEDALUS/inbox/2026-10-31_from-REGINALD_profile-refresh-dispositions.md; this memo
RESULT: L857 re-run: 134 of 139 filed; frozen small universe ex acquirers cut borrowing −$5.70B with deposits +$39.20B (10/28 early read −$4.27B on 28). Santander–Webster merger (8/20) handled; 6 flags (Regions, Renasant, Simmons, The Bancorp, Bank of Hawaii, Israel Discount NY) all funding-mix at the issuer; none routed. Inbox 4 of 4 drained.
GAPS: Concentration verdict needs the FDIC Q3 posting (~mid/late Nov). 4 banks not yet available at FFIEC (East West, HSBC USA, First Hawaiian, Beacon). REG-06 EDGAR scan due today not run (outside task).
WILL_NEEDS: None for this row. The FFIEC token still expires 11/05 (WQ-31); renewal stays Will's, and the 11/07 MI3/Call Report run needs it.
FOLLOW-UP: Optional one-touch re-run by Wed 11/04 for the 4 unfiled banks (new dated file; re-apply apply_frozen_2026-10-31.py). REG-06 EDGAR scan owed (due 10/31). FDIC full-universe screen ~mid/late Nov.
