# EUR→USD funding backstop gate: the one letter

⛔ **PROPOSED, NOT REGISTERED. Setting a threshold is Will's word. The instrument (`scripts/usd_swapline.py`) is WITHHELD: not for operational use and not to be cited as a reading until PROME's read 3, the last of this episode's budget, says otherwise.** No route is live under this letter.

**LIQUID · consolidated 2026-10-08 (DOCKET L568, read 2 ❌ X5).** Code basis: `9004d5450`. Every figure below reprints from `python3 AGENTS/LIQUID/scripts/usd_swapline.py --baserate` at that commit unless it is tagged otherwise.

**This letter replaces three texts in full; none of them is live:**
1. §1 of `PROME/inbox/processed/2026-10-01_from-LIQUID_reconciled-swapline-letter-and-closeout.md`, which contradicts the code in places: it says SWPT older than 13 days is "flagged STALE", credits all 15 WATCH ops to the Aug–Dec 2016 squeeze, gives an unadjusted $10B SWPT line, and says turn ops are "excluded".
2. The letter points of `PROME/inbox/processed/2026-10-01_from-LIQUID_reconciled-letter-HANS-AGREE-amendment-c.md`.
3. The "letter's turn clause, re-settled" in `PROME/inbox/processed/2026-10-01_from-LIQUID_usd-swapline-fix-pass.md`, and the same clause at `analysis/2026-10-01_eurusd-basis-instrument.md` §7a.

## 1. What it measures

Banks draw on the Fed's central-bank swap lines only when market dollars, including the FX-swap basis, cost more than the line. The line costs OIS + 25bp (the 9/23 operation priced at 4.15%). Usage is therefore a **ceiling-binding** signal: a material draw says the basis has reached the backstop for some borrower. It is **not a basis level** (that stays unmeasured; HANS-T-12), it is **silent below the ceiling**, and it carries stigma. **"Below backstop lines" means the backstop is not binding. It never means "no dollar strain".**

## 2. Sources, timing, scope

| Leg | Source | Timing | Owner |
|---|---|---|---|
| OPS | NY Fed Markets API, per operation, by counterparty | dated by trade date; posted at settlement (~T+1, ~16:00 ET) | LIQUID (script) |
| SWPT | FRED `SWPT` (H.4.1 central-bank liquidity swaps, $M, Wednesday level). **Global, all counterparties, not European.** | published Thursday ~16:30 ET | LIQUID (script) |
| Tender | ECB USD tender pages: bidder count, cadence and tenor announcements | per tender | **[HANS]**, not computed by the script |

- **European set:** ECB, SNB, BoE. Danmarks Nationalbank and Norges Bank are not in it.
- **Ties are inclusive (≥).**
- **The headline covers European operations TRADED in the last 14 days.** An operation that is still outstanding but was traded more than 14 days ago drops out of the headline.

## 3. Lines (PROPOSED)

A **turn op** is an operation with a term of 21 days or less whose funds are out over a quarter-end: settle ≤ QE < maturity, keyed on **settlement**. A trade of 9/30 that settles 10/1 is not a turn op. A long operation over a quarter-end (e.g. 84 days) is not one either. **[The turn bound is LIQUID's post-read change. HANS SAW it 10/9 and AGREES the 21-day bound for the tenor-onset exclusion (HANS's leg). The TURN lines and the SWPT window sit on LIQUID's amount legs, which HANS says are not HANS's to agree or decline (HANS packet `AGENTS/LIQUID/inbox/2026-10-09_from-HANS_liquid-floor-and-turn-bound-answer.md`, 10:05 ET).]**

| Grade | Condition | Who computes it |
|---|---|---|
| **WATCH** (a look, no route) | one non-turn European op ≥ **$1.0B** · OR one turn op ≥ **$5.0B** | script |
| | OR one ECB USD tender with ≥ **8 bidders** | **[HANS]** |
| **ORANGE** | a European central bank moves to **daily** USD operations: HANS is primary, on the ECB announcement or tender page; the script's cross-check is one counterparty trading on ≥ 3 distinct dates inside 7 days | **[HANS]** + script cross-check |
| | OR a **tenor onset**. This is HANS's amendment (c) plus LIQUID's replay qualifiers: the ONSET (no such op by that counterparty in the prior 90 days) of a USD operation ≥ 28 days, or of a non-weekly tenor (outside 5–8 days) that does not span a quarter-end. Excluded: NY Fed small-value test operations (`isSmallValue = Y`) and ≤ 21-day operations spanning a quarter-end. **≥ $0.1B floor: LIQUID-proposed, AGREED by HANS 10/9, ties inclusive** (HANS packet `AGENTS/LIQUID/inbox/2026-10-09_from-HANS_liquid-floor-and-turn-bound-answer.md`, 10:05 ET). It is in-sample: it was fitted after the hit, on one positive episode. The qualifiers were added in LIQUID's re-replay. | **NOT computed by any script** |
| **ALERT** (route via WALTER) | one non-turn European op ≥ **$5.0B** · OR one turn op ≥ **$15.0B** · OR `SWPT` ≥ **$10,000M** with the as-of outside a turn window, ≥ **$15,000M** inside one (as-of within QE −7 … +14 days) | script |

Precedence: ALERT > ORANGE > WATCH > below backstop lines.

## 4. Failing closed, leg by leg (as the code runs it)

| State | Meaning |
|---|---|
| OPS **DOWN** | fetch error, an empty response, or no European operation in 60 days |
| OPS **STALE** | newest European operation older than **22 days** (the longest normal ECB gap is a 3-week year-end op) |
| SWPT **DOWN** | fetch error or no usable rows |
| SWPT **STALE** | as-of older than **10 days**. It is not graded as current. The 10/1 text's "13 days, flagged STALE" is withdrawn |

| Situation | Verdict | Exit |
|---|---|---|
| both legs healthy | the highest grade | 0 |
| a leg down or stale, and a leg with data reads WATCH, ORANGE or ALERT | that grade + `PARTIAL: <leg> <state> (<reason>)`. A stale SWPT ALERT prints as ALERT, labelled STALE with its as-of | 3 |
| a leg down or stale, and nothing reads WATCH or above | `UNGRADEABLE`, each leg's state listed. **Never "below backstop lines" off a partial** | 2 |
| while WITHHELD, a default run | the refusal only, before any network call; no grade printed | 4 |

## 5. Base rates and controls (`--baserate` at `9004d5450`, run 2026-10-08)

| Leg | History | Result |
|---|---|---|
| Amounts, non-turn | 2021H2 → now, 328 European non-turn ops | WATCH 1 (SNB $3.10B [2022-10-05]) · ALERT 2 (SNB $6.27B [10/12], $11.09B [10/19]). **One episode** |
| | 2014–19, 236 European non-turn ops | WATCH 15: **8 in Aug–Dec 2016 and 7 outside it** (2016-04-27, 05-11, 05-18, 07-06; 2017-01-04, 03-15, 03-22; the 7 dates are from read 2's recompute, VERIFIED there) · ALERT 0 |
| Turn ops | 2010 → now, 92 turn ops | TURN-ALERT 2: ECB $33.0B [2011-12-21] · ECB $17.27B [2020-03-25]. TURN-WATCH 6: 3 calm (ECB $6.35B [2016-09-28] · $11.91B [2017-12-20] · $5.01B [2018-03-28]) + 3 March-2020 (BoE $7.71B · BoE $5.00B · ECB $6.65B) |
| SWPT, turn-adjusted | 2007 → now, 1,031 weeks | 186 ALERT weeks. Episode starts 2008-01-02 · 2008-04-02 · 2011-12-14 · 2020-03-25 · 2020-12-16 ($10.0B, the tail of the 2020 regime) · 2022-10-26. The "2012-10-17" start the tool also prints is **an artifact of the window, not a new episode** |
| SWPT window cost | same | **248 of 1,031 weeks (24.1%) sit inside the turn window.** It suppresses 10 weeks ≥ $10B, incl. **2007-12-26 $14,000M** (the first GFC draw week, so the onset reads one week late) and **2012-09-26 … 10-10 ($12.5–14.7B)**, which split 2011–12. It also suppresses the calm 2017–18 year-end ($12.0B), which is why it exists |
| Cadence cross-check | 2014–2026 | 13 weeks, **2 episodes (2020-03-23, 2023-03-20)**, 0 calm |
| Bidders ≥ 8 **[HANS]** | 220 ECB tenders since 2022-11 | 0. Unvalidated against a squeeze |
| Tenor onset **[UNREVIEWED]** | LIQUID's ad hoc replay, 10/1, in no script | 2020-03-18 only with the $0.1B floor (plus a 2014 series-start artifact); without the floor, plus two tiny calm onsets |

**Controls.**
- **2020-03:** ALERT (ECB $75.82B, 84 days, [2020-03-18]) plus ORANGE. The first possible ALERT was **3/19**, because of the posting lag (read 2's day-by-day replay).
- **2022-10:** ALERT on the SNB ($11.09B [2022-10-19]). Read 2's replay gives WATCH from 10/6 and ALERT 10/13–11/2.
- **2023-03:** **MISSED on amounts** (max $0.48B ECB [2023-04-05]). Only the cadence leg caught it, on 2023-03-20. That leg tracks a policy response, so it lags the stress.
- **UK LDI, 2022-09:** **MISSED** (the BoE drew $0.005B).

## 6. What Will must hear, in plain words (read 2's residual risks, kept in substance)

1. **A quarter-end is a blind-ish spot by design.** Any draw up to $15B that lands in a quarter-end week reads WATCH, and WATCH is not routed. Five real March-2020 stress operations of $2–4B read "turn op, below turn lines". A burst the size of the October-2022 SNB draws, placed at a quarter-end, reads WATCH. On SWPT the $15B line applies in about 1 week in 4, and it delayed the 2007 GFC onset by one week.
2. **When banks stop bidding at the weekly tender — the calmest state — the tool goes UNGRADEABLE.** It cannot tell that from a broken feed (568 such days in 2010–15). HANS's tender-page read would separate them.
3. **An unknown counterparty is not printed**, and the run can exit 0 past it.
4. **The track record is thin and fitted in-sample.** Usage fired in 4 episodes (2007–08 on SWPT only, 2011–12, 2020-03, 2022-10) and missed 2 (2023-03, UK LDI). The window since 2021H2 holds ONE positive episode. The lines were set after seeing the hits, and there is no out-of-sample test.
5. **Usage is a late, ceiling-priced signal.** The first possible ALERT in 2020 was 3/19, after the coordinated Fed action of 3/15; that date is from memory and was not checked. The swap-line price changed over the base-rate window (OIS+100 → +50 → +25, also not checked here), so hit counts across eras are not like-for-like.
6. **SWPT is global.** A SWPT ALERT can be Japanese; the BoJ was the largest drawer in 2020.
7. **Same-day operations are not summed per counterparty.** ECB 2020-04-15 summed to $7.07B, which crosses ALERT; neither operation alone does.
8. **The tenor-onset leg is in no script**, and its base rate comes from an ad hoc replay nobody has reviewed. **HANS agreed the $0.1B floor and the 21-day bound on 10/9.** HANS also named one fact: the UK gilt-LDI crisis of 23–28 Sep 2022 falls inside the quarter-end window (QE −7…−2). A draw in that week would have graded on the $15B turn lines and missed. The bidders ≥ 8, daily-ops and tender-page legs are HANS's, read by hand each HANS session, with no script.
9. **The X1 repair is author-tested only.** That repair keeps a working leg's ALERT when the other source fails. It stays unverified until read 3.

*Receipt 2026-10-09 (LIQUID; source: PROME read-3 packet `inbox/2026-10-08_from-PROME_usd-swapline-read-3-STILL-UNRESOLVED-budget-spent.md`, 10/8 15:16 ET). Read 3 found two more risks, added here as written in its ledger. Both are labelled **UNREVIEWED-FIX-PENDING**: LIQUID fixed them on 10/9 under WQ-398 (a) (conditions `4bbbb0563`, code `23977aec5`, record `analysis/2026-10-09_usd-swapline-WQ398-fix.md`), and nobody has read that fix. It stays unverified until the one further read Will names.*

10. **X2-residual: the base-rate replay could count on partial history and still report success.** At `9004d5450` the `--baserate` floors were a sum (≥ 1,000 NY Fed ops) and a count (≥ 900 SWPT rows). One empty NY Fed year, or a SWPT history starting 2008-10, still printed counts with exit 0. If 2016 had come back empty, "2014–19 WATCH 15" would have printed **3**. *The 10/9 fix fails closed on any empty complete year, on any European-op gap > 22 days since 2015-06-10, and on a SWPT history that starts after 2007-01-10, misses a week or is more than 10 days stale. **The floor it cannot see:** a 2010–2015 year cut part-way that still holds one European op passes.*
11. **CE1e/CE1f: one bad field on one leg hid the OTHER leg's ALERT.** At `9004d5450` a single European op with an empty maturity date crashed the run after both fetches. The run printed no SWPT line and no verdict, with exit 1, even with a fresh $50,000M SWPT reading. A malformed SWPT date crashed the run the same way. *Under the 10/9 fix, the malformed leg is marked DOWN and the other leg still prints and grades. One malformed op takes the WHOLE ops leg down, because it could be the ALERT op.*

## 7. Clause → code (X5 check)

| Clause | Where it is computed |
|---|---|
| amount WATCH / ALERT, turn lines, turn test on settlement | `grade()` · `is_turn()` · `spans_qe()` |
| SWPT line, turn-adjusted, window QE −7 … +14 | `swpt_grade()` · `swpt_in_turn_window()` |
| cadence cross-check (≥ 3 dates in 7 days) | `cadence_switch()` |
| 14-day headline, leg states, PARTIAL / UNGRADEABLE / exit codes | `ops_leg()` · `swpt_leg()` · `assess()` · `run_live()` |
| WITHHELD refusal, exit 4 | `WITHHELD` constant · `main()` |
| window cost, suppressed weeks, base rates | `baserate()` |
| bidders ≥ 8 · the daily-ops announcement · the tenor onset | **not computed by any script** ([HANS] / UNREVIEWED) |

## 8. Path to a ruling

1. PROME runs read 3, the last read.
2. If the read clears the instrument, LIQUID sets `WITHHELD = False` as the release step. Any other change after read 3 is unreviewed and is labelled so.
3. PROME registers ONE WQ row carrying §6.
4. Will rules on the lines.

Nothing is registered and nothing routes before step 4. HANS answered on the floor and the turn bound on 10/9 (folded into §3 and §6 item 8).
