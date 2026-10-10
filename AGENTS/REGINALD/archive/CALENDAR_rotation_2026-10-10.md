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
