# VIOLET → PROME: L278 leg 2 = KILL, VIO-FOMC-0916 closed (letter FAILED) · L441 DECLARED with spec · inbox drained · WQ-259 prep

**From:** VIOLET (spawned by prome-4d, WQ-184 Tier-1 due-row, DOCKET L278) · **Written:** 2026-09-24 00:5x ET · **Record:** `AGENTS/VIOLET/research/2026-09-24_VIO-FOMC-0916_GRADE_part3.md`

## 1. L278: LEG 2 GRADED on the 9/23 close = ⛔ KILL

| figure | value | basis |
|---|---:|---|
| Anchor: VIX close 9/16 | **17.71** | CBOE `VIX_History.csv`; FRED VIXCLS and yfinance agree |
| VIX close 9/23 | **15.18** | yfinance: daily bar, `fast_info` and the 5-min series agree. ⚠️ **Not CBOE-confirmed**: the history CSV, the delayed-quote endpoint and FRED had not posted by 00:4x ET |
| ΔVIX 9/16→9/23 | **−14.29%** | KILL line < −1.41% ⇒ **KILL** |
| Close needed to change the verdict | ≥ 17.46 | **2.28 points** above the reading |
| Fill-forward check | none found | +6.83% vs 14.21 [9/22 CBOE], co-moving with VIX9D, VIX3M, VVIX, SPY and MOVE |

- **PROME's consumer read (15.18, −14.3%, KILL) matches my grade.** I graded it myself on my own pulls.
- **The whole letter FAILED: 0 CONFIRM · 2 KILL · 1 MISS · 1 VOID · 1 HELD-with-defect.**
- **L125 can point at the part-3 record.** Legs 2, 3 and 4 are one error on n=1 event (a stress event was modelled; a resolution event was traded).

⚠️ **A disagreement I recorded but did not apply:**
- Leg 2 borrowed the leg-1 cohort (VIX ≤16 at T-1, 88% up) but, unlike leg 1, had no void clause.
- On the level cohort that actually applied (n=34) the prior was **53%**.
- I graded the leg as written. This becomes acceptance condition ⑤ for the next letter.

⛔ **A correction to part 2 (KB-VIO-309):**
- The 9/18 MOVE bar printed **80.64**. WALTER SIG-W-20260919-001 had it, and it sat unconsumed in my inbox for 5 days.
- The leg-3 verdict (CONFIRM B / MAP MISS) is **unchanged**, and B is now 3/3 on direct evidence.
- Part 2's claim that *"A-cells moved monotonically opposite"* is withdrawn. Part 2's body is left as written; part 3 §4 supersedes it.

**No item forced a trade, a threshold move or a score change.** Convergence is still 27/50.

> **ATTENTION** 🟠 — **MOVE spiked to 95.45 on 9/23**, up 21.5% in one day and the highest value in VIOLET's 57-row ledger [investing.com PRIMARY, yfinance agrees].
> - The 10Y yield (`^TNX`) went 4.963 [9/21] → 5.114, and TLT fell 1.6%.
> - VIX rose only 6.83% and the curve stayed in contango (VIX3M/VIX 1.193).
> - The cause is not attributed; the rates substance belongs to HENRY/BOND. It is carried in the NEXUS CROSS-DOMAIN brief. One day of data is not a regime broadcast.

## 2. L441: the M1:M2 "historical average" 5.6. Disposition: **DECLARED** (KB-VIO-310)

**What I measured.** I recomputed the average on my own CBOE settle ledger `workbook/VX_TERM_HISTORY.tsv`:
- method: standard monthly contracts, roll-adjusted (the front contract is skipped when it has ≤5 days to expiry);
- sample: 3,324 sessions, 2013-05-20 → 2026-08-03;
- result: **mean 5.41% · median 5.84% · p70 8.22% · p90 12.0%**. The last 252 sessions: mean 5.86, median 5.52.

⇒ **5.6 sits between the full-history mean and median. It has not decayed toward all-clear.** I have given it a vintage; I have not replaced it.

**Spec for the FORGE side** (`vix_futures.py` `AVG_STEEPNESS`; PROME implements):
1. Keep **5.6**. Add a comment giving the basis, vintage and re-check date: `re-measured 2026-09-24 on VIOLET VX_TERM_HISTORY.tsv, n=3,324, 2013-05-20→2026-08-03, mean 5.41 / median 5.84; re-check 2026-12-16 (KB-VIO-310)`.
2. Print the vintage beside the value: `Historical avg: 5.6% (vintage 2026-09-24, re-check 2026-12-16)`.
3. **Fail visibly after the re-check date.** If today is past the re-check date and the vintage has not been re-stamped, print `UNVERIFIED` next to the `BELOW_AVG`/`ABOVE` classification instead of a bare label. This is fail-closed for the class L441 names.
4. **Recompute rule (VIOLET owns it):** at each quarterly VIX expiry (next is 2026-12-16), re-measure by the method above. If the full-history median differs from the constant by **more than 0.5pp**, replace the constant with that median rounded to 0.1. Either way, re-stamp the vintage and tell PROME. The date is registered in VIOLET `CATALYSTS.tsv`.

**Other points on L441:**
- My `thresholds.py:58` green edge carries the same vintage comment. **Its value is unchanged**, so this is not a threshold move.
- 8.99 and 12.0 are ratified lines and outside L441's scope; neither was moved. One observation only: KB-VIO-025 labels 8.99 the "top 30th percentile", but it measures about p75 (p70 is 8.22).
- The KB-VIO-032 rolling percentile is confirmed **unbuilt**. It is queued in my research queue #3 and would sit alongside the static band, not replace it.

## 3. L0 drain: whole inbox, 4 items, all logged in `board_log.tsv` and moved with `git mv` to `processed/`

| item | disposition | why |
|---|---|---|
| PROME L441 packet | **acted** | DECLARED, spec above |
| WALTER SIG-W-20260919-001 (off-RTH fill-forward) | **acted** | It corrected part 2. Answer to its question: grade VVIX, VIX3M and VIX6M only on CBOE history (the 16:05 delayed-quote VVIX was 0.25 off). Concur, nothing retracted |
| WALTER SIG-W-20260921-001 (¥158 rate check) | **noted**, NO-OP | INFO; SAM owns the substance; it decays at Tokyo's reopen 9/24. Any cheap-tail re-open is the instrument's own post-close read |
| WALTER SIG-W-20260921-008 (Goepfert breadth) | **noted**, NO-OP | INFO; HENRY and RED own breadth. The vol complex does not confirm (VIX 15.18, contango) |

Both lanes are now empty.

## 4. WQ-259 prep (for Will; nothing was republished)

⚠️ **One premise is wrong.** The published pages were last refreshed on **2026-08-18** (`d1bab0c8b`), not 7/30. Their repo sources were brought up to the 9/14 closes and **never redeployed**. My `CLAUDE.md:194` still says 7/30; that is a CLAUDE.md edit and needs Will's word. A refresh would change three things:
1. **Letter:** from "pre-registered, pending" to **graded 0 CONFIRM · 2 KILL · 1 MISS**.
2. **State:** the regime goes from the elevated-SKEW/8/18 picture to LOW_VOL/contango, and MOVE goes to 95.45 as the one live vector.
3. **Cheap tail and score:** the cheap-tail window goes from OPEN (9/17) to LAPSED under WQ-258 with no fresh read, and the convergence score shows 27/50.

**VIOLET's recommendation: refresh after the next post-close boot,** once 9/23 is confirmed by CBOE and the three DARK canaries are re-read. That is Will's call.

## Skipped controls (reported as skipped)

- **The full `boot.py` was not run.** A pre-open run writes 9/24-dated rows from 9/23 data (the KB-VIO-303 defect). As a result, OVX, JPY, cheap-tail, COR, VIX-options and m1m2 were not re-read.
- **`closeout_guard` shows the CANARY_MAP contract RED** (JPY, OVX and cheap-tail DARK at 6–7 days). This is explained on STATUS and clears at the next post-close boot.
- **The thesis-currency advisory** (over its threshold) was not re-read.

## COMPLETION — VIOLET — 2026-09-24
STATUS: ⚠️ PARTIAL (L278 grade and inbox drain are done; the full boot was skipped on purpose, so 3 canaries are DARK)
CHANGED: VIOLET research/…GRADE_part3.md (new), STATUS, SCRATCH, NEXUS_BRIEF, CALENDAR, board_log, scripts/thresholds.py (comment only), workbook/{KB,PREDICTIONS,CATALYSTS,VX_DAILY,MOVE}.tsv, fred_cache, inbox→processed ×4, this memo
RESULT: Leg 2 = KILL. VIX 17.71 [9/16 CBOE] → 15.18 [9/23 yfinance, not yet CBOE-confirmed] = −14.29% against the −1.41% line; the verdict needs ≥17.46 to change. The letter FAILED (0 CONFIRM · 2 KILL · 1 MISS · 1 VOID · 1 HELD-with-defect). L441 DECLARED: 5.6 against a re-measured mean of 5.41 / median of 5.84 (n=3,324), re-check 2026-12-16. Inbox 4→0. MOVE spiked to 95.45 on 9/23 (+21.5%).
GAPS: CBOE had not posted 9/23, so the grade rests on one vendor (margin 2.28 points). OVX, JPY and cheap-tail were not re-read because a pre-open boot writes misdated rows.
WILL_NEEDS: WQ-259 ruling (refresh or hold). Its premise is wrong: the pages were published 8/18, not 7/30. CLAUDE.md:194 is stale and needs Will's word to correct.
FOLLOW-UP: PROME implements the FORGE AVG_STEEPNESS vintage and UNVERIFIED rule (§2); L278 closes and L125 points at part 3. VIOLET post-close boot supersedes the 9/23 row.
