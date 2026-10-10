# CALENDAR rotation 2026-10-10 (verbatim; each block = ONE table row, contiguous)

Rotated at the 2026-10-10 closeout (read-cap rule 5: CALENDAR 25,290 B ≥ 75% of budget). These are resolved or past rows of §LATER. crc32 is over each row's UTF-8 bytes with no trailing newline; recompute before trusting. Table header for reading: `| Date | Event | What to Check | Threshold / Signal | Who Cares |`.

## BLOCK C1 (506 B, crc32 `0b269ca9`)

=====BEGIN C1=====
| ~~Wed Sep 16, 10:30 ET~~ ✅ **RESOLVED — BENIGN** | **WAL CEO Vecchione, Barclays GFS fireside chat** | Message: profitability + buybacks + credit cleanup; deposit optimisation done for 2026; **adjusted NIM up a few bp from deposit fees, headline NIM ~−1bp from deposit remix**; more guidance on the Q3 call (Investing.com / Seeking Alpha transcript, secondary). No 8-K. WAL closed 77.80 on the day (FOMC day, range 76.59-81.25) — not separable from the Fed. Original row → archive. | REGINALD |
=====END C1=====

## BLOCK C2 (529 B, crc32 `124e9854`)

=====BEGIN C2=====
| ~~Wed Sep 16~~ ✅ **RESOLVED — HIKE AS PRICED** | **FOMC: +25bp to 3.75-4.00%, 12-0** (first hike since 2023) | Dots: 16 of 18 see another hike; year-end 2026 median ~4.1-4.4% (CNBC 9/16, secondary). **Level response (what this row said to check):** 10Y 5.01 [9/16] → 4.94 → 5.01 → 4.96 [9/22] → **5.11 [9/23 ^TNX], highest since 2007**; 30Y 5.35 [9/16] → 5.29 [9/22]. ⇒ the hike itself was absorbed; **the level moved on the 9/23 PMI + Barr day, not on the decision.** | BOND owns the curve; REGINALD rate leg |
=====END C2=====

## BLOCK C3 (557 B, crc32 `ee8298e4`)

=====BEGIN C3=====
| ~~Wed Sep 30~~ ✅ **RESOLVED — SOLD, NOT LAPSED (FORGE 10/7 reconcile)** | **`KRE $60P Sep-30 ×2`** | **Will SOLD both 9/30 @ $0.01 ⇒ −$451.48, as leg 1 of a roll into `KRE $65P Dec-31-2026 ×2` @ $1.68** (his own roll, `MGMT-KRE65P-DEC31`; standing sell-or-roll practice, `USER.md`). My 9/29 "lapse on track / LAPSE ruled" pre-read was overtaken by the roll — written back from the broker reconcile, not the tape, as registered. The ≤$66 tripwire never came near (KRE lowest close 69.44 [9/30]). Full prior row → git history. | | REGINALD |
=====END C3=====

## BLOCK C4 (301 B, crc32 `6a2c00cf`)

=====BEGIN C4=====
| ~~~Wed Sep 9~~ ⏳ **DATE PASSED — marked 2026-09-14; OTTO-owned, context only for me, not checked.** | CRMT Q1-FY27 10-Q — first public data covering the waiver period, two days AFTER the 9/7 decision | Whether a standstill extension / conversion / filing is disclosed. | Context only. | OTTO |
=====END C4=====

## BLOCK C5 (506 B, crc32 `f3dee7be`)

=====BEGIN C5=====
| ~~Fri Sep 18~~ ✅ **EXPIRED — pair finished OTM** | **WAL Sep-18 $67.5P ×1 + $70P ×1** (WAL-desk book) | WAL closed **$78.54 [9/18]** → $70P −10.9% / $67.5P −14.1% OTM ⇒ **lapsed worthless, as held to expiry under `WQ-143` (B)**, decision-free. The Dec-18 $70P roll (filled 9/2) is live and guarded by `REG-T-02`. ⚠️ **Graded off the tape; `../WAL/` owns the record and a broker-export confirm is owed there (root rule #4).** Original row → archive. | WAL desk / TERRY; REGINALD info |
=====END C5=====

## BLOCK C6 (651 B, crc32 `57f797b9`)

=====BEGIN C6=====
| ~~🔴 ~Oct 1-6~~ ✅ **RESOLVED 10/6 — ANNOUNCED** | **WAL Q3-2026 EARNINGS-DATE ANNOUNCEMENT — MY DATED OBLIGATION (TRY-FIRE-002)** | **Release Mon 10/19/2026 after the close; call Tue 10/20 12:00 ET** (Business Wire, PHOENIX 10/06 09:00 — issuer text read in full via syndication 10/7; weekdays `date -d`). Announced 13 days ahead (pattern was 15–19). ⚠️ **My pattern estimate (Tue 10/20 AMC) was one day off** — the registration was right to lock on the release, not the pattern. | **DONE: TERRY packeted the LOCKED dates 10/7 (`fe37dd785`).** The WAL desk's frame-before-filing (L170) is WAL's. | REGINALD (done); TERRY consumes |
=====END C6=====


### Rotation 2026-10-10 Sat ~15:3x ET — core-file sweep (Will: "Do a sweep of our core REGINALD files")

Read-cap rule 5: `CALENDAR.md` stood at 24484 B (≥75% of budget); rotate until <70% (22785 B). Verbatim, contiguous; crc32 over each block's lines joined by `\n`, UTF-8, no trailing newline. **Recompute before trusting.**

## BLOCK C7 — Last Updated stamp chain, 10/10 ~15:3x back to 9/24 (CALENDAR.md lines 3–3 at rotation, 2835 B, crc32 `aa6aa94c`; lines joined by \n)

=====BEGIN C7=====
**Last Updated:** **2026-10-10 (Sat ~15:3x ET, core-file sweep):** `REG-T-06` row + Q3 nowcast ≈ $770B · 11/05 JWT row: token is on BOTH machines (laptop verified 10/10). No date moved, no threshold changed. **Prior 2026-10-10 (Sat ~13:5x ET):** + WEEKLY FUNDING READ row (two 9/29 bars crossed) + `REG-T-06` leg-3 row (~10/29 ESTIMATE; Will's re-letter word owed before it). No threshold changed. **Prior 2026-10-10 (Sat ~12:4x ET):** + PREDICTION INSTRUMENT DATES table (REG-07 10/21 · REG-06 scans 10/31, 11/30, 2027-01-05 · REG-03 Q3/Q4 QBP). No threshold changed. **Prior 2026-10-09 (Fri ~22:xx ET, Will-directed evening session):** + canonical **Q3-2026 BANK EARNINGS DATES** table (read by `scripts/earnings_countdown.py`; CUBI + FLG still NOT ANNOUNCED, searched 21:2x ET) · WQ-313 row: L180 graded on the ORIGINAL total-CRE basis, multifamily a separate sub-read, missing banks → UNKNOWN when they could flip the verdict, **11/07 = planned retrieval, completeness checked then** (Will 21:33 ET; plan `reports/2026-10-09_Q3_earnings_read_plan.md` §2.0) · claims → 197K [w/e 10/3]. No threshold changed. **Prior 2026-10-09 (Fri ~10:4x ET, L516 wake):** Nano row re-dated — P&A NOT posted, bid summary read, next check Tue 10/13. **Prior 2026-10-07 (Wed ~22:3x ET, L527 session):** WAL Q3 date announcement row RESOLVED ✅ (Mon 10/19 AMC; TERRY packeted) · `KRE $60P Sep-30` row RESOLVED ✅ (SOLD 9/30, rolled to Dec-31 $65P — not a lapse) · OZK sub-notes row → ≈+$12.3M (OZK correction) · WAL+EGBN pattern row REPLACED by the WQ-318 six-bank print row (CFG 10/16 · WAL 10/19 · OZK 10/20 · EGBN 10/21; FLG/CUBI not announced) · claims → 197K [w/e 9/26] · FL rail Q3 dates VERIFIED (BKU/SSB 10/21 · AMTB 10/22 · SBCF 10/27) · VLY Thu 10/22 BMO · Nano P&A NOT posted (10/7). No threshold changed. Prior stamp: **2026-09-29 (Tue ~17:5x ET):** `KRE $60P Sep-30` row re-marked off the 9/29 close (−14.1% OTM, one session left; lapse on track). No date moved, no threshold changed. Prior stamp: **2026-09-27 (Sun ~21:1x ET):** + WQ-313 Q3-checks row (DOCKET L35/L180/L521/L514). No date moved, no threshold changed. Prior stamp: **2026-09-27 (Sun ~12:5x ET):** + Nano Banc forward-reads row (P&A check-by 10/9 · bar date est. · MLR ~3/25/27). No date moved, no threshold changed. Prior stamp: **2026-09-26 (Sat ~18:3x ET — catch-up through the 9/25 close):** `KRE $60P Sep-30` row re-marked (KRE $71.55 [9/25], −16.1% OTM, 3 sessions; lapse on track); claims row → 197K [w/e 9/19]. No date moved, no threshold changed. Prior stamp: **2026-09-24 (Thu 00:xx ET — catch-up):** FOMC + WAL chat + WAL Sep-18 expiry rows RESOLVED ✅; `KRE $60P Sep-30 ×2` PRE-REGISTERED (lapse expected, tripwire KRE ≤$66). No threshold changed. Prior stamps → `archive/CALENDAR_rotation_2026-09-24b.md`.
=====END C7=====
