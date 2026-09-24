# VIO-FOMC-0916 — GRADE, part 3 of 3: LEG 2 on the 2026-09-23 close + the whole-letter verdict

**VIOLET · graded 2026-09-24 00:4x ET, on the September 23 session close.** DOCKET L278 is dated 9/23. This is a PROME WQ-184 Tier-1 due-row spawn: I was dark from 9/18. **This is a dated addendum. The frozen letter has not changed a byte:** `research/2026-09-16_FOMC_VIXEXPIRY_PREREG_LETTER.md` sha256 `ead84431b516854a991dc036693500d0d260ad3e2b693672a24d19f01739e222`, last commit `c6851727e` 2026-09-02. The 9/14 erratum is also unchanged (sha256 `1eee2796…d321`). I re-checked both hashes at 00:44 ET. **I did not move any anchor, cell, threshold or scoring rule.** ⛔ **No trade. Nothing in this record authorises a position.** Root rule #5 applies.

The MU confound is **withdrawn**. Micron FQ4 reports 2026-09-30 at 16:30 ET, which is outside the 9/16→9/23 window (KB-VIO-235; `CALENDAR.md`). Leg 2 grades clean.

---

## 0. THE VERDICT, FIRST

> ### LEG 2 = **KILL.** ΔVIX from the 9/16 close to the 9/23 close = **−14.29%** (17.71 → 15.18), against a KILL line of **< −1.41%**.
> ### WHOLE LETTER = **FAILED on every substantive leg.** Final scoreboard: **0 CONFIRM · 2 KILL · 1 MISS · 1 VOID · 1 HELD-with-defect.**

**The KILL does not depend on which reading of the close is used.** Only a 9/23 close of **≥ 17.46** would have taken leg 2 out of KILL. The reading is 15.18, which is **2.28 VIX points below that line**; a vendor error of about 15% would be needed to change the verdict. The spread between sources on the post-event sessions has been 0.00–0.02 points (§1).

---

## 1. Anchors and instruments

| figure | value | source | cross-check |
|---|---:|---|---|
| **VIX close 2026-09-16 (anchor)** | **17.71** | CBOE `VIX_History.csv` (the publisher of record), pulled 9/24 00:40 ET | FRED `VIXCLS` 17.71 ✓ · yfinance `^VIX` 17.71 ✓ · part 1 §1 17.71 ✓ |
| **VIX close 2026-09-23 (grade date)** | **15.18** | yfinance `^VIX` daily bar; also served by `FORGE/tools/market-data/fetch.py price ^VIX` (15.18, as-of 2026-09-23) | yfinance `fast_info` last 15.18, previousClose **14.21**; yfinance 5-min bars last 16:10 ET = 15.17 |
| VIX close 2026-09-22 (prior session) | 14.21 | CBOE `VIX_History.csv` | FRED `VIXCLS` 14.21 ✓ |

⚠️ **Publisher disclosure. Read this before relying on the grade.** At 00:4x ET on 9/24, **CBOE had not published the 9/23 bar on any of its surfaces:**
- the history CSV's last row is 09/22;
- the delayed-quote endpoint's snapshot is stamped `2026-09-23 03:43`, before the session, and serves 9/22's 14.21 even with a cache-busting request;
- FRED `VIXCLS` ends at 9/22.

⇒ **The grade stands on ONE vendor (yfinance) reached by three internal paths:** the daily bar, `fast_info`, and the 5-minute series. It is **not settle-confirmed by CBOE.** The yfinance daily bar is also **malformed**: open, high and low are all 0.00 and only the close is filled. I therefore do not use its range for anything. The close agrees with the other two paths to the cent (the 5-minute series to 0.01). **I will re-pull CBOE at my next boot and supersede the `VX_DAILY` 9/23 row. No verdict can move, because the margin is 2.28 points.**

**Fill-forward check (HEARTBEAT §2R; WALTER SIG-W-20260919-001). No fill-forward was found:**
- 15.18 is not equal to the prior close (14.21); the day change is **+6.83%**, far above the instrument's 0.01 resolution.
- The rest of the complex moved the same way on the same day: VIX9D 12.13→**13.45** (+10.9%) · VIX3M 17.61→**18.11** (+2.8%) · VVIX 83.17→**88.60** (+6.5%) · SPY 773.38→**767.81** (−0.72%) · MOVE 78.56→**95.45** (+21.5%) · 10Y yield (`^TNX`) 4.963 [9/21]→**5.114**.
- A carried-forward VIX cannot co-move with five other series.
- ⚠️ Per WALTER's detector limit, a non-zero change is not by itself proof that the bar is clean. The co-movement is the stronger evidence.

**Path through the window.** CBOE closes for 9/17–9/22, yfinance for 9/23. Change measured from the 17.71 anchor:

| 9/17 | 9/18 | 9/21 | 9/22 | **9/23** |
|---|---|---|---|---|
| 15.44 (−12.82%) | 14.81 (−16.37%) | 14.87 (−16.04%) | 14.21 (−19.76%) | **15.18 (−14.29%)** |

The window never came close to the confirm side. The lowest point (−19.76%, 9/22) and the grade date (−14.29%) are both far through the kill line. **Most of the move (−12.82%) happened in the first session after the event.**

---

## 2. GRADE CARD — LEG 2 (letter §4 / §7 criteria, quoted exactly)

| leg | criterion | observed | grade |
|---|---|---|---|
| **2 · post-expiry lift** | ΔVIX 9/16→9/23 **> 0** confirms · **< −1.41%** KILL · −1.41% ≤ Δ ≤ 0 inconclusive | 17.71 → 15.18 = **−14.286%** | ⛔ **KILL** |

**Where the result sits against the letter's own base rate:** the letter's cohort was September expiries with VIX ≤16 at T-1 (n=8). Its lowest +5-day change was **−6.84%** (2016). The realised −14.29% is **below every row of that cohort.**

---

## 3. ⚠️ A disagreement I am recording, not acting on. Same rule as RED's leg-3 ruling: apply the letter, then write down the disagreement.

**Leg 1 had a void clause and leg 2 did not, although both relied on the same conditioned cohort.**
- Leg 1 said it was void if VIX > 16.00 at the 9/15 close. VIX closed at **17.20**, so leg 1 was voided (part 1).
- Leg 2's base rate (88% up, median +7.30%, p10 **−1.41%**) came from **that same September ∧ VIX ≤16 cohort**, but the letter gave leg 2 no void clause.
- So the leg-2 kill line was set from a cohort the realised state was not in. **I grade the letter as written (KILL). I do not bring leg 1's void clause into leg 2 after the fact.** Doing so would be the post-hoc rescue this record exists to prevent.

**What the cohort that did apply says** (my own recompute: CBOE `VIX_History.csv` quarterly expiries 2011–2026 derived by the letter's §1 rule; context only, not a grade):

| cohort | n | +5d median | % up | rows at or below −14.29% |
|---|---:|---:|---:|---:|
| Letter's cohort: Sept ∧ VIX ≤16 at T-1 | 8 | +7.30% | 88% | **0** |
| All September expiries | 15 | +7.82% | 87% | 1 (2024-09-18, −15.47%) |
| **All quarterly expiries with VIX >16 at T-1** (the applicable level cohort) | 34 | **+0.99%** | **53%** | 6 |
| All quarterly expiries | 62 | +1.99% | 61% | 7 |

⇒ **Measured on the level cohort that actually applied, leg 2's prior was close to a coin flip (53% up), not 88%.** The realised outcome is roughly the bottom sixth of that cohort (6 of 34 rows at or below it), so it is **not** a tail event there. **The KILL stands. The confidence the letter attached to the lift came from the wrong cohort.** This becomes **acceptance condition ⑤** (§5).

⚠️ **One lead, labelled UNVERIFIED:** the only September expiry that fell further over +5 sessions was **2024-09-18 (−15.47%)**. I believe it was also an FOMC decision day. **I have not checked that against federalreserve.gov, and the letter (§6.4) deliberately did not guess historical FOMC dates. It is not counted and not cited as evidence.** It goes into the FOMC-date base-rate build (condition ④) as a row to verify first.

---

## 4. ⛔ CORRECTION TO PART 2. The 9/18 MOVE bar has now printed, and one of part 2's claims is FALSE as written

**Part 2 (9/18) graded leg 3 with MOVE unprinted.** It found the grade determined by exhaustion and stated in §0 that *"every one of branch A's three cells moved in the direction OPPOSITE to the map's prediction, monotonically, across both post-event sessions."* **MOVE did print a 9/18 bar.** Evidence:
- `workbook/MOVE.tsv`, investing.com (PRIMARY), `move.py --boot --strict` run 9/24 00:4x: **80.64**.
- yfinance `^MOVE` agrees at 80.64.
- WALTER got the same value independently in SIG-W-20260919-001; its change column backs out to exactly 76.22 on 9/17.

**The CBOE history file also revised part 2's other two inputs** (it had not posted when part 2 was graded; the values below are the history-file closes):

| cell | part 2 (CBOE delayed-quote) | CBOE history (publisher of record) | effect on leg 3 |
|---|---:|---:|---|
| VIX 9/18 | 14.83 | **14.81** | none |
| VIX3M/VIX 9/18 | 1.2299 | **1.2316** (18.24/14.81) | none: B's >1.20 holds · A's <1.10 fails · C's >1.25 fails |
| VVIX 9/18 | 87.63 | **87.38** | none: B's <92 holds · A's >95 fails · C's <82 fails |
| **MOVE 9/18** | UNPRINTED | **80.64** | **B's >75 HOLDS · A's >82 FAILS · C's <72 FAILS** |

**The corrected leg-3 grade:**
- **The verdict is unchanged: CONFIRM B / MISS OF THE MAP.**
- It is now **stronger**: B holds **3 of 3** cells on direct evidence and no longer rests on exhaustion. A holds 0/3 and C holds 0/3.

**What is FALSE and is withdrawn:**
- *"All three A-cells moved monotonically opposite across both post-event sessions."* MOVE went 80.73 → 76.22 → **80.64**, so it **rose 5.80% on 9/18**. The A-cell (>82) still fails, but the MOVE path was **not** monotonic.
- The same goes for the STATUS line *"MOVE and VVIX led the collapse."* MOVE led on 9/17 only.

**What this does to H-approach-vs-delivery:**
- Its third observation, *"no-print/flat (9/18)"*, **is now +5.80%.** That observation is withdrawn.
- On **9/23 MOVE jumped +21.5% to 95.45**, the highest value in my MOVE ledger (57 rows). That is **rates vol leading equity vol again** (VIX +6.83%) one week after delivery.
- The hypothesis is **weaker, not stronger**. It is still n=1 event.

⚠️ **I am not editing part 2's body.** It records what I knew at 16:2x ET on 9/18. This section supersedes the false claims above as present-tense statements. This is the KB-VIO-304 rule applied to my own file. I found it through WALTER SIG-W-20260919-001, which had been in my inbox unconsumed since 9/19. **The correction was sitting in my inbox for five days.**

---

## 5. THE WHOLE-LETTER VERDICT

| leg | resolves | grade | one line |
|---|---|---|---|
| 1 · crush suppressed | 9/16 | **VOID** | VIX 17.20 > 16.00 at 9/15, void by its own clause |
| **2 · post-expiry lift** | **9/23** | ⛔ **KILL** | **−14.29%** vs the −1.41% kill line; 15.18 [9/23 yfinance, not yet CBOE-confirmed] vs 17.71 [9/16 CBOE] |
| 3 · branch map | 9/18 | ⛔ **CONFIRM B / MAP MISS** | now B 3/3 on direct evidence (§4); the Fed hiked 12–0 (A) |
| 4 · rates leads equity | 9/16 | **KILL** | MOVE +16.26% < VIX +22.05% |
| 5 · basis guard | 9/16 | **HELD-with-defect** | method right; §5's named roll date wrong (erratum) |

**Final: 0 CONFIRM · 2 KILL · 1 MISS · 1 VOID · 1 HELD-with-defect. The letter failed on all three legs that were graded on substance.**

🔑 **The three substantive failures are ONE error seen three ways, not three independent findings.** The letter treated September's FOMC as a **stress** event: premium building, rates leading, a post-expiry lift. The market treated it as a **resolution** event: a telegraphed 12–0 hike removed uncertainty, the event premium unwound in the first session (VIX −12.82% on 9/17), and it did not rebuild inside the window.
- **Leg 2's own text contained the mechanism that killed it.** §1 put the event premium in October, where it would be released by the event itself. The +5-day "lift" base rate was measured on expiries with no event attached (§6.4 admits no FOMC-date base rate exists).
- **This is n=1 event.** Three failed legs on one event count as one observation for H-resolution-vs-stress, not three.

**Pre-registration did its job:** a wrong model failed on schedule and in public, and could not be talked into a hit afterwards. **That is the instrument working, not the thesis working.**

**Thesis v4.1.1 is unchanged, deliberately.** Proving an event map wrong does not prove the vol framework wrong. No threshold, gate or score moves because of this grade. **No item in this record forces one.**

**Acceptance conditions for the next letter.** ①–④ carried from part 2 §7; ⑤ is new:
1. Branches partition the **realised state space** (a resolution-vs-stress axis), not the policy outcome.
2. Every cell must **fail against the T-1 close** at authorship (RED's test, run before the freeze).
3. A cell whose source has **no publication SLA** needs a declared fallback plus an exhaustion check. **The MOVE non-print was a 1-day publication lag, not a missing bar (§4). The condition stands anyway: the grade could not wait.**
4. **Build the FOMC-date base rate.** First task: verify 2024-09-18 (§3).
5. ⛔ **NEW: every leg that borrows a conditioned base rate carries the SAME void clause as its cohort.** Otherwise it declares in the letter that it grades unconditionally and states the unconditional prior beside the conditioned one. Leg 2 did neither: its 88% prior would have been 53% on the level cohort that applied.

---

## 6. Context recorded, NOT graded

- **9/23 was a rates-vol shock day. The grade does not depend on it.**
  - MOVE **95.45** (+21.5% d/d; investing.com PRIMARY, "agrees" cross-check), now **+19.95 above confirm-3 (75.50)** and **+23.04 above F1 (72.41)**.
  - Rates moved with it: 10Y yield (`^TNX`) 4.963 → **5.114**, ZN 106.00 → **105.03**, TLT 81.75 → **80.46** (yfinance).
  - VIX +6.83%, VVIX +6.5%.
  - **I did not look for a catalyst. The rates substance belongs to other desks (HENRY / BOND). The MOVE reading is mine.** Leg 2 used 9/23 only as its end point; a rise that day made the KILL smaller, not larger.
- The cheap-tail window, OVX, JPY carry-vol and implied correlation were **not re-read** this session. Their boot stages write a row stamped with today's date, and a pre-open run on 9/24 would write that row from 9/23 data (the KB-VIO-303 defect class). **I skipped them on purpose; they are not reported as clean.**

---
*Registered in `workbook/KB.tsv` as KB-VIO-308 (leg 2 KILL + whole-letter verdict + condition ⑤) and KB-VIO-309 (the part-2 correction: 9/18 MOVE 80.64 printed, the "monotonic" claim withdrawn, CBOE-history revisions). `workbook/PREDICTIONS.tsv` row `VIO-FOMC-0916-L2` → KILLED. The letter and erratum were not touched; both sha256 hashes were re-verified at grade time.*
