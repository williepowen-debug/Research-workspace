# STATUS rotation 2026-10-10 (verbatim, contiguous)

Rotated at the 2026-10-10 Sat PM write-back (Will: "make sure we have properly updated our files") to bring `STATUS.md` back under its read budget (rule 5 STOP <70% = 22,785 B; it stood at 25,352 B). History only; **recompute the crc before trusting this banner.**

The block is the contiguous lines 2–28 of `STATUS.md` as they stood at rotation, between the two marker lines below. crc32 is computed over those lines joined by `\n`, UTF-8, no trailing newline.

## BLOCK T20 — 10/10 SAT AM headline + 10/9 FRI PM headline + prior-headline pointer + Last Updated stamp chain (STATUS.md lines 2–28 at rotation, 3168 B, crc32 `084f8b0d`)

=====BEGIN T20=====
**🟢 10/10 SAT (Will-launched): CAUGHT UP ON DATA; three overdue process items DONE; no score, threshold or trade moved.**
- **Settled grades:** 10/9 closes graded (WAL $74.27, exit 0-of-3, row 28; FLG 3rd close below RED).
- **Predictions:** REG-03/06/07 instruments named. ⚠️ REG-07's level reading was true at birth, so it grades on the CHANGE from 0.62%; **Will may VOID it before SSB prints 10/21**.
- **DAEDALUS fixes:** F#4 wording fixes + wiring ⑰ done. The `V1V3-ACCELERATE` token rename is deferred because WALTER reads it.
- **Stale tables:** VX 27 rows STALE · FLOW frozen · two June baselines FROZEN-VINTAGE · KB +3.
- **Large-bank desk:** proposal packeted to DAEDALUS (Will-directed).
- **HBAN puts:** Will's word on WQ-302 committed verbatim in POSITIONS (`cb236344f`).
- **Owed at next boot (Will):** ① the 9/7 DAEDALUS packet decision ② the FHLB Atlanta / SF 10-Qs ③ five July threads.
**🟠 10/9 FRI PM — MONITOR REPAIR + Q3 EARNINGS READ PLAN (Will-directed); STRESS STILL CONCENTRATED ON 6/30 EVIDENCE; NO SCORE, THRESHOLD OR TRADE MOVED.**
- **Repair (`8255c2d13`):**
  - OZK's 8-K and insider checks now use the FDIC (they had queried the SEC, where OZK hasn't filed since 2017).
  - **VLY was keyed to Old Republic's SEC ID (74260 → 714310).**
  - FLG / AMTB / CFG / CUBI added. A failed, unparseable or uncovered bank can no longer print an all-clear.
  - The countdown reads the CALENDAR earnings table; unsettled and NaN daily bars are excluded from settled grades.
- **Plan:** `reports/2026-10-09_Q3_earnings_read_plan.md`.
  - Individual-bank deterioration is not cross-bank spread. Only L180 or the FL-rail aggregate can show spread.
  - L180 is graded on the ORIGINAL total-CRE rate. Multifamily is a separate sub-read.
  - Missing banks → UNKNOWN wherever they could flip a breadth verdict.
  - **11/07 = planned Call Report retrieval, completeness checked then.**
- **Baseline (Call Report):**
  - Total-CRE bad-loan rate 2.46% → **2.23%** [6/30/25 → 6/30/26].
  - Multifamily 3.88% → **3.58%**, but **up from 3.23% last quarter**, all at FLG / EGBN / CFG. That is individual, not spread.
  - L180 dry run Q1 → Q2: *c* = 1 (WAL foreclosed property +2.3%).
- **Tape:** 10/9 vendor quotes (settled bars not posted) WAL 74.27 · KRE 69.01 · FLG 11.32 · OZK 44.41, while SPY rose +0.60%.
- **Claims:** 197K [w/e 10/3]; w/e 9/26 revised to 199K.
*Prior headlines (10/9 AM · 10/7 WED) and the archive-pointer chain for 9/29 → 8/10 → `archive/STATUS_rotation_2026-10-09.md` BLOCK T15, crc32 `4546cd82` (read-cap rotation 10/9 PM; recompute before trusting).*
**Last Updated:** **2026-10-10 Sat ~12:4x ET (Will-launched, continuation; closeout)**: 10/9 settled grade · REG-03/06/07 instruments · F#4 + wiring ⑰ · stale tables · large-bank desk packet · WQ-302 verbatim. Prior: **2026-10-09 Fri ~22:xx ET (Will-launched evening session, Opus 5.5)**: boot · WALTER lane 2 → 0 · bounded monitor repair `8255c2d13` · Q3 read plan + Will's clarifications · FL frame A3 · CALENDAR earnings table · read-cap rotation T14–T19. *Stamp chain (10/9 AM and earlier) → BLOCK T16, crc32 `3ba61974`.*
=====END T20=====

## BLOCK T21 — FLG ladder note in §CONVERGENCE MATRIX (STATUS.md lines 49–49 at rotation, 792 B, crc32 `fc6e141e`)

=====T21 BEGIN=====
> 🔴 **FLG price ladder `VX-REG-6.03` RED since 10/7** (band 3 $11.39 broken at **$11.30 [10/7 close]**, −20.6% vs FROZEN $14.24; band 1 $12.82 broke 9/16, band 2 $12.10 broke 9/28). **Packets PROME + FLG sent 10/7 (`018af9846`)** per the 9/24 registration; the ladder is exhausted (no band beyond RED). Detector: `scripts/vx_ladder_check.py` (exit-code defect FIXED `b6544d45d` 9/24 — DAEDALUS Prose-Remedy #1, verified 10/9). ✅ **Intraday-bar defect FIXED 10/9 (`8255c2d13`):** today's (ET) bar and any NaN bar are now always excluded via `scripts/settled_bars.py`. A clock filter alone would have failed, because the 10/9 bar still read NaN at 20:3x ET. Settled count = 2 closes below RED through 10/8; 10/9 NOT GRADED until settled. Matrix score unchanged (price is not an input).
=====T21 END=====

## BLOCK T22 — THRESHOLD STATUS heading (10/9 PM refresh note) (STATUS.md lines 106–106 at rotation, 371 B, crc32 `7314d335`)

=====T22 BEGIN=====
## ⚠️ THRESHOLD STATUS (**10/9 PM refresh: claims w/e 10/3 and DGS10/DGS30 10/8 (FRED API); VIX/^TNX/Brent 10/9 vendor reads; WAL/KRE 10/9 = vendor quotes, NOT settled. The 10/9 AM refresh note (settled 10/8 closes; FRED 10/8 via ALFRED; SOFR/discount window via WALTER) and older vintages → BLOCK T19, crc32 `cebafa60`.** Rows not named keep their stated vintage.)
=====T22 END=====

## BLOCK T23 — THRESHOLD STATUS WAL + KRE rows (10/8-led) (STATUS.md lines 113–114 at rotation, 1145 B, crc32 `77401802`)

=====T23 BEGIN=====
| **WAL** | **<$78** | **$75.50** [**Thu 10/8 CLOSE**, +1.55%; two routes]; **10/9 $74.27 CLOSE, settled, two routes agree (graded 10/10: row 28, 0-of-3, 9.32% short)** | 🔴 **`REG-T-02` = `FIRED` (cycle 2, since 9/1). Exit run `0-of-3` — COUNT FROM `registry/REG_T02_EXIT_LOG.tsv` (27 rows through 10/8), never from here.** Exit = `WAL ≥ 81.90 ×3 CONSECUTIVE closes`; 10/8 is $6.40 / 7.81% short. Closes 9/30–10/6: 75.10 · 75.70 · 76.38 · 76.02 · 76.09 — all SUPPRESSED RE-ENTRIES. **Q3 print LOCKED Mon 10/19 AMC** (call Tue 10/20 12:00 ET). Guards the RH `Dec-18 $70P` (ROLL70) only — not the NEW Fidelity `Dec-18 $65P ×4`. |
| KRE | <$60 | **$69.59** [**Thu 10/8 CLOSE**]; **10/9 $69.01 CLOSE** (settled, two routes agree, 10/10); 10/7 $68.89 (closing low of the selloff) | 🟡 **`REG-T-01` = `UN-FIRED`**, $8.89 / 12.9% above the line. Path 69.83 [9/29] · 69.44 · 69.95 · 70.78 · 70.39 · 70.07 · **68.89** = new closing low of this selloff in my 9/14→10/7 series (−7.0% from 74.11 [9/14]). The Sep-30 $60P ×2 was SOLD 9/30 and rolled to Dec-31 $65P ×2 (Will). `TRY-COND-KREADD` (TERRY) NOT armed on my legs. |
=====T23 END=====

## BLOCK T24 — THRESHOLD STATUS CCC/HY row (with the 10/6 prior read) (STATUS.md lines 116–116 at rotation, 964 B, crc32 `ec961eab`)

=====T24 BEGIN=====
| **CCC/HY ratio** | >3.6× (3 consec) | **3.975×** [CCC **1,252** / HY 315, **10/8**]; 3.977× [1,229/309, 10/7] | 🔴 **HARD-FIRE CONTINUES. 10/7–10/8: CCC +38bp to 1,252 = NEW FRED-window high, HY +12, ratio flat-to-down — both legs widening, no re-cross ⇒ no escalation by the vector's rule (LIQUID/RED own the tail read). B 308 [10/7] · 315 [10/8]; BB 189 · 194.** Prior 10/6 read: ratio 4.007× — and the ratio's 10/2→10/6 RISE is HY-TIGHTENING-LED (HY 324 → 303 while CCC held 1,202–1,215) = the denominator form, so NO escalation by the vector's own rule.** CCC **1,215 [10/1] = FRED-window high**. B 302 [10/6] (316 · 316 · **329 [10/1]** · 312 · 314 · 302): held >300 seven prints, never reached ORANGE 330. BB 185 (peak 204 [10/1]). Re-arm ESC escalated 9/26; not repeated (Will 9/26: re-entry is LIQUID's). BROCK 10/2: CCC/BB compressed 6.780 → 6.077, tail not leading. Full rows → `workbook/VX.tsv` `VX-REG-18.04`/`18.05`. |
=====T24 END=====

## BLOCK T25 — §KEY CATALYSTS date mirror (STATUS.md line 59 at rotation, 659 B, crc32 `2288fccd`)

=====T25 BEGIN=====
*Dates are OWNED by `CALENDAR.md` — **earnings dates in its Q3-2026 BANK EARNINGS DATES table** (CUBI + FLG NOT ANNOUNCED at 10/9 21:2x ET). Read plan → `reports/2026-10-09_Q3_earnings_read_plan.md`. The four-row mirror that sat here (capital-rules final rule TBD · IQHQ Aug · OZK sub-notes Oct 1 · Affinius Oct) → BLOCK T8, crc32 `6e2cf1ef`. Next (10/7, issuer-announced): CFG Fri 10/16 · WAL Mon 10/19 AMC · OZK Tue 10/20 AMC · EGBN/SSB Wed 10/21 AMC, BKU 10/21 BMO · VLY 10/22 BMO, AMTB 10/22 AMC · SBCF 10/27 AMC · FLG/CUBI TBA · Nano P&A NOT posted 10/9 (bid summary posted 10/8) → re-check **Tue 10/13** · JWT 11/05 · MI3 run 11/07.*
=====T25 END=====
