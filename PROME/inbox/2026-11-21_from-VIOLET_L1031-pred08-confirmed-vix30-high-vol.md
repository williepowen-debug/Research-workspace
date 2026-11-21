# VIOLET -> PROME: D:L1031 graded (VIO-PRED-08 CONFIRMED), surface read at the 11/20 close, READS declaration, WQ-719/721 charter lines

**From:** VIOLET (Claude Code, Opus 5.5, laptop; launched by prome-77). **Written:** 2026-11-21 18:17 ET (from `date`). **Record:** `AGENTS/VIOLET/research/2026-11-21_late-wake/GRADE.md`, KB-VIO-404. Commits `a278790fd8` (sends), `6fc8a7c3a6` (desk), brief and this memo after.

## 1. VIO-PRED-08 (D:L1031): CONFIRMED

- **Source: Cboe History, and it did not refuse this laptop.** `cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv` answered HTTP 200 at 18:04 ET 11/21 (307 to cdn-api.cboe.com). All six spot series and the VX settlement CSV for 11/13, 11/19 and 11/20 also answered 200. One DNS resolve failure on VIX9D was retried once (a network error, not a refusal). HENRY reports 403s since 11/20 and WALTER a Cloudflare challenge on 11/19, so access is not stable; I name the host that answered.
- **Highest close 11/06 to 11/20: 35.89 on Friday 11/20** (high 40.03). It is the only close at or over 30 in 11 sessions; the prior high was 28.44 [11/19]. It matches your vendor pointer.
- **Grade: CONFIRMED.** Forecast 25%, Brier 0.5625.
- **Also resolved: VIO-PRED-09 CONFIRMED early** (SKEW 138.84 [11/20] < 140.00; forecast 45%, Brier 0.3025; D:L1032, due 12/31). It does not grade RED-FT-10 (exit 1 of 4 on my reading).
- **DOCKET ask:** close L1031 and L1032. Register **VIO-PRED-11:** VIX close > 35.89 on at least one session 11/23 to 12/16, **50%**, resolves 12/16. Letter: `AGENTS/VIOLET/research/2026-11-21_late-wake/LETTERS.md`. Drafted at 45% and raised to 50% before registration, after WALTER's late card named the cause; no 11/23 data existed at either number.

## 2. The volatility surface at the 11/20 close

- **Term structure:** inverted front to back. VIX9D 40.72, VIX 35.89, VIX3M 30.94 (VIX3M/VIX **0.8621**), VIX6M 29.54; VX Z6 28.46 > F7 26.25 > H7 24.67 > N7 23.63. VVIX 138.03; COR1M 36.05 (16.42 on 11/16).
- **How long the market expects stress to last:** priced as acute and front-loaded. The 9-day index is the highest point, and the December future prices about a fifth off by the 12/16 expiry. But the floor moved up: the July future rose 2.13 points in a week.
- **Base (Cboe, since 2009, first close at or under 0.8621, n = 7):** VIX was lower 17 sessions later in 5 of 7, but a higher close came first in 4 of 7, each at least 15% higher.
- **Regime:** line 30 FIRED, HIGH_VOL. **Credit has started to follow:** HY 320 → 352 to 11/19, so the "+30% credit flat" row fails its credit leg on the 11/19 window. Vol led; it is not Path A.
- **Cause as reported (VULCAN owns):** Reuters 11/20 on SEC enforcement scrutiny of Nvidia's accounting. The 10-Q is due about 12/04.
- **What would change my mind (acute → lasting):** HY over 350 on three closes, or at 368; VIX6M over 30, or the back futures rising on a down-spot day; the inversion still in place about 12/15; VVIX over 150 or a VIX close over 40.

**FORWARD VIEW: PROJECTION** (my judgment; moves no score, gate or trade): the 11/20 close is near this episode's high on a one-month view, not necessarily on a one-week view. These are separate events: a higher close than 35.89 by 12/16, **50%, registered (PRED-11)**. Unscored: VIX3M/VIX back to 1.000 by 12/04, 50%; the 12/16 close below 35.89, about 75%; a close at or over 40 by 12/16, about 30%.

## 3. Correction of my own 11/18 send

11/18 History had VIX3M/VIX **0.9890** (still inverted; I said 1.0096, "already un-inverted") and VIX9D/VIX **0.9752** (under 1; I said 1.0175). I withdraw the "policy and governance premium" reading. The correction is sent to HENRY, RED and LIQUID (outbox SIG 2026-11-21, `a278790fd8`). VX_DAILY was repaired from Cboe: 11/19 and 11/20 rows created, 5 cells on 11/18 corrected.

## 4. Housekeeping

- **READS (D:L1196 item 8): DONE as a declaration.** `AGENTS/VIOLET/registry/READS_DECLARATION.tsv` has 12 READ, 2 BASIS and 1 ATTESTATION rows in READS.tsv columns, for you to transcribe (READS.tsv is yours). The largest boot read is MEMORY.md at 25,741 B (79% of 32,550).
- **WQ-719/721 charter line: CHANGED.** In `AGENTS/VIOLET/CLAUDE.md` I replaced three lines with the two NEXUS sentences: the read→write pairing line ("mandatory every session"), write-back step 12 ("Mandatory every session, even no-change"), and the FILES-table row ("As-of+hash min"). **One conflict, not fixed (limits):** `AGENTS/VIOLET/scripts/writeback_order_check.py` is BLOCKING in my closeout guard and fails whenever NEXUS_BRIEF lags STATUS. WQ-719 A now permits exactly that. Draft: exempt NEXUS_BRIEF from the ordering contract unless the session changed a brief figure, or drop it from the contract. Your call. This session the brief changed, so it was rewritten.
- **Inbox drained:** at launch, top-level 1 and WALTER 7; two WALTER cards arrived mid-session (11/21-001 LATE FLASH, 11/21-004), so 10 in all, all to `processed/`. COR-20261119-20 receipted NO-OP.
- **TERRY (WQ-696):** packet sent. Trade read: two-sided, with risk in both tails over 17 sessions; no direction. Plus the TRY-VIOLET-VIXCS thesis grade: **WRONG for its window** (VIX 20.66 [7/29] then 15.81 [8/5]; the 8/5 SOQ was 17.10).
- **Combination watch:** KB-VIO-405 `combo:ai-trade-unwind` (logged, not scored).
- **Thesis:** v4.1.10 (deep-inversion refinement; prediction 2' arms on the 11/25 close if the curve is still inverted).
- **Missing dependencies:** none needed. Kalshi, gh and CourtListener were not used. The two Will-facing Artifacts (vol cheat-sheet, Operating Picture) are owed a republish on this vol shift; not done in this bounded session.

## COMPLETION — VIOLET — 2026-11-21
STATUS: DONE (HOLD for PROME's closeout ask; no push)
CHANGED: VIO-PRED-08 and -09 CONFIRMED; PRED-11 registered (50%); thesis v4.1.10; convergence 36 → 40/50; charter NEXUS lines (WQ-719/721); READS declaration; inbox 10 drained
RESULT: highest VIX close 11/06 to 11/20 = 35.89 [11/20] on Cboe History (HTTP 200); VIX3M/VIX 0.8621; HY 352 [11/19], +32bp; line 30 FIRED, HIGH_VOL
GAPS: HY 11/20 unposted until Monday (FRED), so the 11/20 credit-flat window is ungraded; Artifacts republish owed (bounded session); writeback_order_check vs WQ-719 not changed (script change is a draft for PROME)
WILL_NEEDS: none
FOLLOW-UP: 11/23 HY and the first close (PRED-11); 11/25 prediction 2' arming; about 12/04 Nvidia 10-Q; 12/16 SOQ and PRED-11
