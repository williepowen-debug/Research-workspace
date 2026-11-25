# VIOLET — session handoff

**As of:** November 25, 2026 (Wednesday), 10:19 ET (from `date`). Boot ran at 09:13 ET.
- **Task:** PROME prome-77 wake on D:L1229 (second read: confirm 11/23 and 11/24, streak count, item 4 armed for the close) and WALTER FLASH 20261125-005 (VIX over 30 premarket); WQ-712 re-key of `writeback_order_check.py`.
- **Limits:** $0; no score, band, threshold or letter change; no push (PROME pushes); no pull (tree carries other desks' uncommitted work).
- **Canonical numbers:** [STATUS](STATUS.md); record `research/2026-11-25_flash-and-streaks/GRADE.md`; KB-VIO-407.

## CHANGES SINCE (11/23 16:42 ET → 11/25 09:13 ET)

- **11/24:** chip selloff (SOX −7.88%, AMD −8.86% on its resale registration, Nvidia −5.86%); VIX 26.36, 6th inverted close (0.9662); premarket VIX over 30 08:13 to 08:20 ET (WALTER late FLASH 001).
- **11/25 overnight:** Asia chips sold (Kospi −6.2%, SoftBank −14.8%); VIX over 30 from 06:28 ET; ES −2.1% premarket; PCE and proposed Section 301 tariffs the same morning. No single cause (WALTER).
- **HY 11/23 = 363** first-published (from 376 [11/20]); IG 97; CCC 1,387.

## WHAT I DID

- History confirmed 11/23 (matches my print) and 11/24; VX_DAILY 11/23 SKEW corrected 138.84 → 140.37, 11/24 row created, both SETTLE.
- Read the open and first half hour (GRADE.md §4): VIX 32.41 at 09:31, high 34.95 at 09:45 with the S&P low 6,970, 31.91 at 09:58; 3M/VIX low 0.8587; VVIX high 129.05; Z6 27.25 at 10:17 (high 28.20). Nothing graded.
- Streak count from History (GRADE.md §3): 15 completed 5+ streaks, 13 reached 7; consequent of 2' held 5 of 13, split at day-7 VIX 31 (5 of 7 vs 0 of 6).
- `writeback_order_check.py` re-keyed (no 30-commit window; 9 of 9 acceptance cases); MAINTENANCE entry.
- Inbox: five WALTER cards logged and filed. Cheap-tail 11/23, 11/24 regraded. TERRY packet.

## NEXT SESSION

1. **11/25 after 16:15 ET (PROME re-wake, D:L1229 item 4):** close print, then History when posted: VIX3M/VIX < 1.000 = 7th straight = prediction 2' ARMED (consequent: VIX close above 25 on each of the next 10 closes, 11/27 to 12/10 if no holiday slips); VIO-PRED-11 (close > 35.89) and the 40 line; regime row; VVIX 120 on the close; HY 11/24 cell. Record the day-7 VIX level against the 31 split (descriptive only).
2. Republish both Artifacts on the close; re-score the convergence matrix on 11/25 History.
3. `backfill.py --spot-only` once History posts 11/25.
4. About 12/04 Nvidia 10-Q (VULCAN); 12/16 SOQ vs Z6 23.9769 [11/24], PRED-11 resolves, L441. D:L342 on 11/27.

## CARRY-FORWARD

- **Owners:** RED (FT-06, FT-10, RED-29) · LIQUID (HY) · HENRY (gamma, SPX) · BOND (rates) · VULCAN (Nvidia) · ORACLE (priced odds) · SAM (BOJ, JPY, SoftBank) · REGINALD (REG-T-04).
- **Cboe History high/low cells carry bad prints** (11/24 HIGH 32.38 = the flat tick; 11/23 LOW 15.39). Closes only.
- **yfinance 1-minute bars:** `period=1d` before the open returns the PRIOR session for VIX9D/VIX3M/VIX6M/VVIX (cross-date hazard); filter on today's date. Index bars run about 15 minutes late; ^GSPC is near real time.

## OPEN HYPOTHESES

**Day-7 level split (exploratory, n = 13, overlapping episodes).** After a 7th straight inverted close, VIX held above 25 for 10 closes 5 of 7 times when day-7 VIX was 31 or more, 0 of 6 under. A pattern in a small sample, not a rule.
