# HENRY -> PROME: D:L823 UNRESOLVED at +20 sessions (resolves 2027-01-20 to 2027-02-18); first map on the 11/19 chain published; WQ-719 A charter edit made

**prome-36 task letter (10:02:36 ET), read from 10:02 ET; work 10:02–10:2x ET. Claude Code, Opus 5.5 (`claude-opus-5-5`), laptop. Commits: `956d624675` (desk; STATUS HEAD), `fb90af8386` (TERRY packet). Record `AGENTS/HENRY/research/2026-11-19_d823/GRADE.md`.**

## 1. D:L823: UNRESOLVED, not a hit and not yet a sixteenth false positive

- **The study's letter, read in its code** (`PROME/reports/2026-10-23_kre-qqq-transition-signature/build.py` lines 15, 26, 28, 234–235): a hit is a qualifying day in [alarm day, +20 sessions], where qualifying = KRE and QQQ return from that day to **60 sessions later** both ≤ −10%; an alarm is resolvable only with 80 forward sessions.
- So today (11/19, session 20) closes the **start window**; it does not resolve the alarm. **First candidate resolves 2027-01-20, last 2027-02-18** (NYSE holidays entered by hand; an unscheduled closure would push both).
- **Closes used:** yfinance adjusted closes (the study's vendor), pulled 10:04 ET; full 21-row table in GRADE.md § 1. Deepest joint decline from a window day so far: **KRE −4.9%, QQQ −4.7% (11/4 → 11/18)**. A hit now needs KRE at or under $63.34–$66.72 and QQQ at or under $582–$653 on the matching day.
- ⚠️ **The DOCKET row's paraphrase reads as decidable today; the study's letter is not.** The row was dated at the end of the start window. **Recommend: re-date D:L823 to 2027-02-18** (note 2027-01-20 as the first possible resolution). Your row; I changed nothing.
- **State since the alarm:** the see-saw ended. 20-session correlation +0.31 on 11/18 (−0.24 at the alarm), opposite-sign days 40% (80%), KRE 4.3% under its relative high, both legs about −4.8% over 10 sessions. The study's own plain-language watch sentence ("HY OAS keeps rising from 3.40% and KRE closes below its 20-session relative high by 4% or more, while QQQ is still falling") is **met on two legs on the 11/18 close and on HY's last print (343 [FRED 11/17])**; HY 11/18 was not posted at 10:05 ET. That sentence was never registered and has no measured precision (one analog, July 2024, which fell sharply for a week and recovered within weeks).

## 2. H4 against the study's 2-of-9 result, and the KB row

- **"Credit leads equity by 2–3 sessions": contradicted for onsets.** HY widened before the equity break in 2 of 9 (anchor B; 1 of 9 on anchor A), median 6.5 sessions after. I stop citing that clause now.
- **"Equity cannot bottom until HY OAS peaks": untested** (the study measures starts, not bottoms). I used it on 11/18 (MAP § 7); that use rests on its own record.
- **Charter text NOT edited** (the letter's limits send charter changes back as a draft). **Draft for your decision**, replacing the H4 paragraph in `AGENTS/HENRY/CLAUDE.md` § CORE METHODOLOGY (and the settled LESSONS heading "[Analysis] — Credit Leads Equities, Not Vice Versa", same content):
  > **Credit-Primary Rule (H4):** Equity cannot bottom until HY OAS peaks (untested as of 2026-11-19). ~~Credit leads equity by 2–3 sessions.~~ In the nine KRE/QQQ joint declines 2007–2024, HY OAS widened after the equity break (onset before the break in 2 of 9, median 6.5 sessions after; `PROME/reports/2026-10-23_kre-qqq-transition-signature/REPORT.md` Tables B3 and N), so a quiet credit tape is no all-clear for an equity break. Rate of change matters more than absolute level.
- Offered, not run: a pre-declared test of the bottom clause on `build.py`'s data (basket trough vs HY peak in a window fixed before looking).
- **KB:** ML-HEN-233 (study + this grade), ML-HEN-234 (FOMC minutes), ML-HEN-235 (Philadelphia Fed). **The 10/23 desk write-back the row said was owed is now done:** STATUS (§ VIEW 11/19), KB, and MEMORY and NEXUS_BRIEF at closeout.

## 3. First dealer map on the 11/19 chain (open interest through 11/18, first with Nvidia results-day trades): PUBLISHED by my rules

| Chain | Spot (vendor live) | Flip 14d / 35d | Net gamma ($B per 1%) | Walls |
|---|---|---|---|---|
| SPX, 10:04 ET | 7,390.00 | **7,545 / 7,556** | **NEGATIVE −43.9 / −62.2** | both WITHHELD (put = call at 7,400 / 7,000; call 14d 7,400 near-tie vs 35d 7,000) |
| QQQ, 10:05 ET | 673.05 | 673 / 673 | 0.0 / 0.0, on the flip: no regime | call **680 PUBLISHED** (clean both); put WITHHELD |

Read after the 09:47 ET IV-zero window. The flip moved down about 7 points from the 11/18 close read (7,552 / 7,561 on 11/17 open interest): the results-day trading did not change the regime. A close over about 7,550 turns it. `PUBLISHED.tsv` rows written, walls by hand. ⚠️ Free-tier proxy: sign and flip robust, $B assumption-dependent.

## 4. WQ-719 A charter edit: made

Will's words as carried in the letter ("719 A, 720 A approved", 12:10 ET 11/18; "721 yes right? No brainer?", 15:44 ET). Applied my 11/18 packet § 5 text, plus one sentence for WQ-721 A:
- **`AGENTS/HENRY/CLAUDE.md` line 54 (step 10)**, now: "NEXUS_BRIEF: rewrite and commit it at closeout only when a figure, threshold, or cross-desk send or wait in it changed (schema §4.1, WQ-719 A); otherwise leave it untouched, with no As-of or pin refresh. When it is rewritten, it is the session's last write-back, and its As-of line carries `STATUS commit: <hash>` equal to STATUS HEAD at that commit (amendment 11). A lagging pin after a no-change session is a warning, not a failure (`scripts/brief_pin_check.py`). If that check reports the pin as PIN-UNRESOLVED, correct the pin to STATUS HEAD at that closeout and commit the brief with no other change and no new As-of (schema §4.1, WQ-721 A)." The old timestamp-check sentence is struck.
- **Line 251 (FILES row)**, now: "Rewritten at closeout only when its content changes (step 10)."
- **Brief header:** `brief_pin_check.py HENRY` at 10:0x ET reads **OK-PINNED (`da9bfcc47b` = STATUS HEAD at that time)**: the UNPINNED state in the letter was cleared at my 11/18 closeout (`b2eb480e4f`). Today's commit moved STATUS HEAD to `956d624675`; the brief's figures changed (map, FRED, D:L823), so it is rewritten with a new pin as the last write at closeout.

## 5. Inbox drain (whole inbox)

General `inbox/` top level: 0. **WALTER lane: 8 of 8 drained** (board_log rows, `git mv` to processed): 20261118-010 acted (HY input to §§ 1–2); -013 FOMC minutes noted (KB ML-HEN-234; HEN-63 0.70 not re-marked: moving a registered probability toward the market after the fact is not evidence); 20261119-002 Philadelphia Fed noted (KB ML-HEN-235); 20261118-014, -015, 20261119-001, -005, -007 info-only. FRED SP500 11/18 7,323.63 and VIXCLS 11/18 24.56 confirm my 11/18 closes.

## 6. Trade assessment, limits, dependencies

- **TERRY** (`AGENTS/TERRY/inbox/2026-11-19_from-HENRY_d823-kre-qqq-alarm-unresolved.md`, `fb90af8386`), WQ-696 form: a state description with no new investment implication; horizon, invalidation and unknowns stated; no card asked.
- Zero dollars. No threshold, level, gate or charter authority changed; the H4 text and the DOCKET re-date come to you as drafts. Not pushed. STATUS rotated 30,339 B → 22,167 B (68% of its read cap); LESSONS.md is at 76% (rotate-tier), left for an ordinary wake.
- **Missing on this box:** Kalshi credentials, gh token, CourtListener token (none needed). Definite and MT Newswire connectors failed to connect; desktop-commander skipped. Not needed.
- **Holding** for your closeout ask (MEMORY, LAST_COMPLETION, NEXUS_BRIEF last, root 1b/1e).

## COMPLETION — HENRY — 2026-11-19
STATUS: ✅ DONE (closeout held for PROME's ask)
CHANGED: AGENTS/HENRY/{CLAUDE.md, STATUS.md, STATUS_COLD.md, board_log.tsv, workbook/KB.tsv, workbook/PUBLISHED.tsv, research/2026-11-19_d823/GRADE.md, inbox/WALTER/processed/ (8)}, AGENTS/TERRY/inbox/2026-11-19_from-HENRY_d823-kre-qqq-alarm-unresolved.md, this packet
RESULT: D:L823 UNRESOLVED by the study's own code (80 forward sessions: 2027-01-20 to 2027-02-18); joint decline so far KRE −4.9% / QQQ −4.7%. H4's lead clause contradicted (HY led in 2 of 9); bottom clause untested. Map published: SPX flip 7,545 / 7,556, NEGATIVE −43.9 / −62.2 $B per 1%, walls withheld; QQQ on its flip, call wall 680. WQ-719 A edit made at CLAUDE.md lines 54 and 251; 8 of 8 WALTER signals drained.
GAPS: HY 11/18 not posted at 10:05 ET (third leg of the study's watch sentence). H4 charter text and LESSONS heading not edited (draft above, limits).
WILL_NEEDS: None.
FOLLOW-UP: PROME: re-date D:L823 to 2027-02-18 (first resolution 2027-01-20); decide the H4 draft. HENRY: closeout on your ask.
