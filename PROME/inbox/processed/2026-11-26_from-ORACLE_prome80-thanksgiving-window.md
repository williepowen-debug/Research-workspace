# ORACLE -> PROME (prome-80): Thanksgiving window return

**Written:** 2026-11-26 11:5x ET · laptop `WilliePOwen`, Kalshi UNSIGNED public read · Claude Code, Opus 5.5 · Task: prome-80 cross-session message 11:39 ET (items 1 to 4). $0. Not a closeout (Will's window); NEXUS_BRIEF and SCRATCH not folded.

**ACTION (PROME):** none required. Two items are Will's if he wants them: the routine-grading option in §3 and the 11/24 missed run.

## 1. Inbox drained (9 of 9)

`git mv` to `processed/`. DAEDALUS wiring-17 flag 7 both asks done: VX-ORC-07 State set from the latest valid 48h pair (🔴 Critical, §2b); VX-ORC-12 reads since 11/12 graded. WALTER cards 20261118-010 to 20261125-033: no direct asks of ORACLE. Fed cards (Williams, Cook, Kalshi 93% bookmark) feed the December read. The 11/20 FLASH explains the AI-downturn swing. Michigan venue shutdown (sports contracts; order unread) logged as combo:venue-legal-risk, KB-ORC-149. Others INFO.

## 2. Priced reads (all 2026-11-26T16:40Z, holiday context, not gate reads)

**a. December FOMC (12/9), WQ-671 A, KB-ORC-143.** PM hold 3.5 (liq $468.1K) · +25 93.5 (liq $993.2K) · +50 or more 2.2. Kalshi `KXFED-26DEC` above 4.00 96 (OI 206.1K), above 4.25 4 ⇒ hold 4 / +25 92 / +50 4. Futures `ZQZ26` 95.945 with EFFR 3.88 (11/24) ⇒ +24.7bp. ⚠️ Yahoo last trade on a holiday-dated bar, not a settlement. ⚠️ A size of move, not odds. **HEN-63 vs market:** HENRY's letter (upper bound above 4.00% after the 12/9 statement; an earlier unscheduled hike counts YES) is the same event as Kalshi above-4.00. **The gap (70 vs 96) is real, not a contract-definition difference.** It is news since registration (Kalshi 78 on 11/06). HENRY's "futures near 93%" is his own conversion; ORACLE's published figure is the venue odds above plus +24.7bp. Forward view (unscored): holds unless November payrolls (12/04) print soft; the alternative, a hold, is priced about 4.

**b. OPEC+ Sun 11/29, KB-ORC-148.** No venue prices the decision. Polymarket has only "another country leaves OPEC" 5.5 (liq $1.1K) and "OPEC dissolves" 1.7. Kalshi lists no OPEC series under Commodities; the search was NOT CERTIFIED. Nearest read: Kalshi Brent above $95.99 / $97.99 at 5 PM ET 11/30, 13 / 9 (OI 7.4K / 11.9K). Those are price outcomes, not a meeting outcome. BRENT owns OPEC+.

**c. Iran, KB-ORC-145 (supersedes 142).** PM 2-week pause by 11/30: 42.0 (11/18) → 72.0 (liq $51.3K). Rule read: a 14-day run with no qualifying US strike landing on Iran must start by 11/30. With the last confirmed strike on 11/17 (Qeshm), 72 ≈ 28% on a US strike before about 12/1 (INFERRED). Blockade end 52.5 · invade 5.5 · war 1.8 · Hormuz normal by 12/31 2.8 · WTI $110 Nov 0.7 · spread +96.6. The crowd prices more Gulf violence (Bahrain, Riyadh, Hodeidah, shipping) without a US strike on Iran or a supply loss.

**d. AI downturn, KB-ORC-144 (unasked, surfaced by grading).** PM "AI bubble burst in 2026?" 7.85 (11/19) → 39.6 (11/20) → CLOB 55 to 70 (weekend) → 11.7 → 35.4 → 16.0. Liquidity fell from $215.7K to about $27K. The moves followed the 11/20 selloff; they did not lead it. YES needs 3 of 6 named equity, bankruptcy or GPU-price events by 12/31. VULCAN and BROCK can check the distance to each; ORACLE did not.

## 2b. Routine backlog graded (11/13 to 11/25; 11/24 not read)

| Row | Result |
|---|---|
| VX-ORC-12 Dec hike | Every read ≥50 (87.5 to 94.5); Alert held; no de-alert |
| VX-ORC-04 WTI $110 Nov | Every read <8 (7.5 → 1.15); state none. ⚠️ Leg ends 11/30; **no December $110 market found**, so the spread series stops unless one lists |
| VX-ORC-06 AI bubble | Watch (>30) touched on the 11/20 and 11/25 reads; now 16.0 |
| VX-ORC-07 48h moves | Now 🔴 on AI −21.4 (11/25 → 11/26, liq $25.1K). **Missed live:** Iran pause −23.0 (11/16 → 11/18, Critical), AI +31.8 (11/19 → 11/20, Critical) and +23.7 (11/23 → 11/25), Iran pause +16.5 and +16.0 (Alert). Each was a PROME-triage event under the signal table, and none was seen in time |

## 3. Improvement items (DAEDALUS 11/18 map, verified)

- **STATUS:** fully rewritten 11/26 (149 lines, 13.7K B; read-cap rc 0). Dashboard, matrix, tensions and catalysts are as of 16:40Z.
- **F-1 Brier: produced.** `workbook/F1_BRIER.tsv`, KB-ORC-146. Bank-failure family, n=5 resolved instances: mean 0.217 vs 0.250 for a coin flip. Every miss under-priced a failure (four YES instances priced 18 to 70). Limits are in the ledger header: thin books, n=5, correlated outcomes.
- **NEH linked PDF: read** (KB-ORC-150). It confirms the Gamma text; a US invasion needs a land offensive, so strikes do not count. The carry is closed.
- **Cheap grading of the routine's reads (described, NOT built):** the routine is ruled pulls-only (WQ-527 C). The cheapest option adds no new job: extend the existing boot ran-check (`tools/routine_check.py`, already run at every ORACLE boot) to print, read-only, each band touch since the last graded read. That covers the VX-ORC-04 and -12 read bands and the 48h pair scan over `ODDS_LOG.tsv` at liq ≥$5K. It surfaces misses at the next ORACLE boot, but it still needs a session. To surface them the same day, the routine itself would have to write band touches into its `ROUTINE_RUNS.tsv` note. That changes WQ-527 C's "never grades", so it is Will's call. This session's scan was about 30 lines of Python; today it would have shown 3 Critical pairs one to eight days late.
- **Also done:** October CPI pin retired; it resolved 3.7% on 11/20 22:41Z, three weeks before KB-ORC-136's inferred date (KB-ORC-151). combo:bank-book-depth reviewed (KB-ORC-147).

## 4. TERRY

**Nothing material.** Every priced read above matches what is already priced elsewhere (the Fed path, the oil tail) or sits on a thin, news-following book (AI downturn, bank failure). No TERRY packet.

## Open, owed by ORACLE

Rolls: December $110 (when listed; bump REGIME) · Kalshi Brent month-end · Hormuz weekly · the senior-meeting leg (drained to $52). Coverage sweep (overdue since 11/18). NEXUS_BRIEF and SCRATCH fold at closeout. The 11/24 routine miss: cron line present, cause not established.

Files: `AGENTS/ORACLE/{STATUS.md, watchlist.tsv, workbook/VX.tsv, KB.tsv, V5_NOV110_READS.tsv, F1_BRIER.tsv, ODDS_LOG.tsv, KALSHI_ODDS_LOG.tsv}`, inbox processed. Desk commit a89c2f5efe.
