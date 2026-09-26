# BOND → PROME · 2026-09-26 15:2x ET · WQ-291 exact kill-rule letter + WQ-246 persistence-count recommendation

**Spawned by `prome-1d`, Tier 1, on Will's 15:04 ET word.** Both are PROPOSALS for PROME to re-present. Nothing is encoded, no gate or THESIS line edited, nothing graded, no trade. Base rates were re-derived today from data already on this desk. No new study was commissioned (WQ-157 ② ruling).

Reproduce: `AGENTS/BOND/analysis/2026-09-26_WQ-291_kill-rule_base-rates.py` (output `…base-rates.out.txt`) · `AGENTS/BOND/analysis/2026-09-26_WQ-246_dfii10_persistence.py`. KB: `KB-BND-337` (291) · `KB-BND-338` (246).

---

## PART 1 — WQ-291: the exact proposed rule (a letter Will can approve word for word)

> **SEPTEMBER-4 PAIRED KILL: DEALER-STOCK LEG FOR A 5-YEAR NOMINAL `I′` FIRE (proposed by BOND 2026-09-26; takes effect only on Will's word)**
>
> **1. Series.** NY Fed FR 2004 primary-dealer net outright positions, Treasury coupons excluding TIPS and FRNs, **bucket "due in more than 3 years but not more than 6 years"** (API key `PDPOSGSC-G3L6`), in $ billions as first published.
>
> **2. Window (trade date).** PRE is the last weekly as-of date strictly before the auction date. POST is the first as-of date on or after the auction date. The leg measure is Δ = POST − PRE, unrounded. The settlement date plays no part. *Basis:* the Board's FR 2004 Instructions (effective January 2022), GEN-6 §II.C (allotments count in that day's positions), A-1 (trade-date accounting) and A-5 (when-issued positions are bucketed by maturity from the issue date, so a new 5Y books in 3–6Y). This was ruled as the join window under WQ-290 (9/25), `KB-BND-332/335`.
>
> **3. Threshold.** The leg is **MET iff Δ ≥ +$8.6B** (inclusive). Otherwise it is NOT MET. The margin is stated at every grade.
>
> **4. The kill.** The thesis kill fires iff that 5Y fired `I′` **AND** (this leg is MET **OR** the funding leg, SOFR−IORB, is MET under its own existing letter). This rule does not touch the funding leg.
>
> **5. Conflicting buckets.** **The 3–6Y bucket alone governs a 5Y fire.** The long-end TOTAL (7–11Y + 11–21Y + >21Y) and the 6–7Y bucket are always reported beside it, never graded. A long-end build with 3–6Y below the bar means the leg is **NOT MET**, reported to Will that evening as a named conflict. The long-end build then counts only toward matrix row 3's existing two-consecutive-build trigger, never toward the kill. A 3–6Y build at or above the bar with the long end flat or falling means the leg is **MET**, reported as "MET — no long-end warehousing".
>
> **6. Missing data.** The leg reads **GAP (NOT MET, fires nothing, reported)** in any of these cases: the POST print is unpublished at BOND's 10/2 boot, the PRE value is revised, or PRE and POST fall in different series breaks. A GAP is never a pass and never a fire.
>
> **7. Who acts.** BOND grades the print the evening it publishes and reports MET, NOT MET or GAP to PROME. A kill that fires is a **recommendation to exit all duration shorts**. Execution goes through TERRY's card and Will's [Approve] (root rule #5). Nothing executes on the grade.

**Applied to the live case (the 9/23 Wednesday 5Y, `91282CRN3`, `I′` fired, funding NOT met per LIQUID 9/22–9/23):** PRE is as-of **9/16**, where 3–6Y reads **$47.986B** (pulled 9/26). POST is as-of **9/23**, published **Thu 10/1 ~16:15 ET** (8-day lag). The leg is MET iff 3–6Y on 9/23 is **≥ $56.586B**. The **9/30 as-of (published ~10/8) is NOT a grading print.** It is post-settlement and is reported only as information (does any build persist?). Lines reached if it fires: TLT Oct-16 82P ×2 · TBT 10 sh. The 004 77P ×20 expire 9/30, before the print.

### Why the bucket is 3–6Y (BOND and PROME rec)
The leg asks whether dealers had to warehouse **this** auction. A 5Y award cannot appear in the long-end total (A-5), so grading a 5Y fire on the long end tests a different auction's sector. BOND's earlier default (long-end TOTAL >0 / >$1B, the 9/15 20Y convention) was only a holding position that fired nothing; this proposal replaces it for 5Y fires. The 9/15 convention stays correct for 20Y and 30Y fires, where the long end *is* the tenor bucket.

### Why +$8.6B, justified for THIS rule on its own terms (not borrowed from FORUM-7's purpose)
| Question | Answer (reproduced 2026-09-26) |
|---|---|
| **Population** | **All 44** nominal 5Y auctions in the corpus with an FR2004 print on both sides, **2023-01-25 → 2026-08-26**, trade-date window. ⚠️ FORUM-7 said "since 2022-01". That is when the FR2004 series starts; the auction corpus starts 2023-01. The 44 are unchanged: median **+$2.74B**, p90 **+$8.62B**, 32/44 positive. |
| **Why 5Y weeks, not all weeks** | The award itself lifts the bucket. On 5Y weeks the median change is **+$2.74B**; on the 213 non-5Y weeks it is **+$0.19B** (all-weeks p90 +$6.20B). A bar built on all weeks would mostly re-detect that an auction happened. |
| **Base rate of the bar** | **5/44 (11.4%)** of 5Y weeks reach ≥ +$8.6B. **Among the 9 5Y `I′` fires that have a trailing-12 bar (n=32 sub-sample): 0 of 9.** In sample, this leg would never have fired the kill on a 5Y. |
| **What a ">0" bar fires on** | 3–6Y >0: **32/44 5Y weeks (73%)**, and **5 of 9** `I′` fires. The current default of long-end TOTAL >0 fires on **31/44 (70%)**, and **7 of 9** `I′` fires; >$1B fires on 25/44 and 4 of 9. **A ">0" leg turns the kill into the `I′` marker, which the Sept-4 ruling says moves nothing on its own.** |
| **Why p90** | A kill should be rare, in the order of the old conjunctive test it replaced (1.8% per auction out of sample; 1 of 44 5Ys here, 2024-01-24). If the two were independent, p90 on 5Y weeks times the 5Y `I′` rate (9/32) gives about 3% jointly, which is that order. **p95 would rest on 2–3 observations out of 44**, and p90 is the tightest cut with 5 observations above it. |
| **Why reuse is clean** | It is the same object: the same bucket, window, auction and print. FORUM-7 D3a uses it to label a verdict; this rule uses it to fire a kill. The consequence here is heavier, which argues for a bar at least as strict, never looser. It was frozen at 02:26–03:0x ET 9/25, before the 9/23 as-of existed, and nobody has seen that print today either. So choosing it now is still a pre-print choice, and reusing it adds no degree of freedom. |

**⚠️ The honest limit, which should travel with the rule:** the 3–6Y change **does not track the size of the dealer award**. The correlation between dealer $ awarded and Δ3–6Y is **r = −0.08** (n=31). The auctions in the top fifth by dealer take have a median build of **+$0.41B**, against **+$6.03B** for the rest. Dealers pre-sell when-issued paper and hedge, so the bucket measures **whether dealer net stock in the 5Y sector rose abnormally in the auction week**, which is a balance-sheet outcome and not the award itself. That can be argued as the right thing for a *non-auction* confirmation, since the auction result already shows the take. But it means the leg can fire on flows unrelated to the auction, and can miss a warehoused award that is offset by when-issued shorts. For scale: the 9/23 dealer award was **$10.99B** (15.77% of $69.67B competitive), so holding that award in full with no offset would clear the bar. The weekday effect is small: a Wednesday auction's POST is the award day itself, with no time to distribute, yet the Wednesday-only p90 is **+$8.26B** (n=24) against **+$9.41B** Monday/Tuesday (n=20). The pooled bar is kept. Pooling across the SBN2022/SBN2024 break is INFERRED, not VERIFIED (`fr2004_join.py` docstring).

### What this rule does NOT do
- It does not apply to 2Y, 3Y, 7Y or 10Y fires. Their buckets and bars are not derived. A fire at those tenors is still reported on both buckets as AMBIGUOUS BY BUCKET and fires nothing on BOND's authority. It does not change the 20Y/30Y long-end convention.
- It does not change `I′` as a marker, the funding leg, FORUM-7's D3a or D3b grading, or any matrix score. It does not re-grade the 9/15 20Y. It does not lift NO-ADD.
- It does not make the kill execute. It produces a recommendation, and the trade goes via TERRY and Will's [Approve].
- **It does not settle the funding leg's window for the 9/23 fire.** Unset (not in WQ-291): which sessions test "SOFR−IORB positive, sustained >+5bp". LIQUID frames the real test as the 9/30 settlement across quarter-end plus two non-quarter-end sessions. **GAP, named, not proposed here.**

---

## PART 2 — WQ-246: persistence count for THESIS gate (a) "DFII10 >2.5 sustained"

> ⚖️ **This is a decision made NOW, with the level already through: 11 consecutive published closes ≥ 2.50 since 9/10, 2.85 on 9/24 (FRED H.15, pulled 9/26).** The framing "what would have been written on 9/1?" removes the *outcome* incentive, because both candidate counts are already satisfied and neither changes a score, a gate state or a position today. It does *not* remove hindsight. BOND picks knowing this episode persisted, and the base rates below were computed today, not on 9/1.

**Recommendation: 5 consecutive published sessions** closing **≥ 2.50** (inclusive), DFII10 H.15 as first published. Unpublished dates are skipped, never counted (the `BND-29` convention). **Any published close below 2.50 resets the count to zero.**

**Rationale:**
1. **It is an ADD gate, and add and exit gates should be asymmetric.** This desk's exit and kill legs use shorter counts (10Y below 4.15 for 3 sessions), because a false exit is cheap. A false add increases risk. The stricter count belongs on the add side.
2. **Will already ruled this exact count for this exact function.** Arm-#2 (GATE-TERRY-007) is 5 consecutive, ratified for a TLT-put gate. Using the same count keeps one book on one convention.
3. **"Sustained" describes a regime**, and one trading week is the smallest unit that reads as one.
4. **The base rate supports it mildly and does not force it.** Of 12 crossings of 2.50 since 2003, **6 lasted one session**, including 2023-10-25. Both counts filter those out. At 2.50, 5 of 5 runs that reached 3 sessions also reached 5, too few to tell the counts apart. Pooled across 2.00, 2.25, 2.50 and 2.75, **47 of 58 runs (81%)** that reached 3 went on to 5. A 3-count therefore admits about a 1-in-5 tail that dies in sessions 3–4.
5. **The cost, stated:** two sessions of latency. In this episode a 3-count fires on the 9/14 observation (2.60) and a 5-count on 9/16 (2.68), so 8bp later.

⚠️ **A third unset specification, found while writing this (the same pattern as `KB-BND-278`):** THESIS.md:147 reads **">2.5"**, while the STATUS and TRADE gate tables and `BND-29` read **"≥2.50"**. The comparator is ALSO a decision made now. The recommendation is **≥ 2.50, inclusive**, to match `BND-29` and the live gate table. It matters only on an exact 2.50 close.

**Scoring consequences (identical under both counts today; they differ only in the counterfactual date):**
| | 3 sessions | 5 consecutive |
|---|---|---|
| Gate (a) fires as of | 9/14 obs (2.60) | 9/16 obs (2.68) |
| Matrix row 1 now | **4, unchanged.** It already moved 3→4 on 9/23 on its other letter (a fresh DGS30 high with weak composition). The current ⇒5 trigger does not read DFII10. | **4, unchanged** |
| Counterfactual, if back-scored | row 1 would have read 4 from 9/14, composite 13 not 12 for 9/14–9/22 | 4 from 9/16, composite 13 for 9/16–9/22 |
| **BOND rec on back-scoring** | **None.** Forward-only, per MATRIX_V2 §3d and the 8/27 non-re-scoring precedent. Record the counterfactual, move nothing. | same |
| `BND-29` ("≥3 of first 5 ≥ 2.50", TRUE 9/17 at 4 of 4) | Its own evidence (9/10, 9/11, 9/14, 9/15) satisfies the gate on its own | Its evidence did **not** satisfy the gate at resolution (4 of 4; the fifth was unpublished). The gate is met only with 9/16. |
| `BND-29` itself | **Stays TRUE under both.** It was written count-agnostic, and a count ruled now does not re-grade it. | same |
| Position | **Authorises nothing.** | same |

⛔ **NO-ADD remains regardless of the count:** Will's standing 7/16 NO-ADD, the declined add (WQ-280, 9/24), WQ-168 ④ and root rule #5 each block on their own. The 004 77P ×20 expire 9/30, so after that the gate governs only a future TLT-put add in THESIS.

---

## L0 inbox drain (whole inbox, every sender) — 6 items, all consumed (`KB-BND-339`, git mv to `processed/`)
| From | Item | Disposition |
|---|---|---|
| PROME (WQ-295) | Declare cadence and watch terms | Packet filed: `PROME/inbox/2026-09-26_from-BOND_cadence-and-watch-terms.md`. **CADENCE: WEEKLY** (the FR2004 Thursday print is weekly). The WATCH_FOR coverage audit was NOT run (GAP). |
| RED | F2 cut not re-cut inside a live window; both reads OFF on every cut | Accepted, no action. BOND's issue-date cut stays BOND-declared and is a marker only. The 5/06 counterexample is carried to RED's next FT-11 spec review. |
| ZHAO via PROME | H.4.1 custody for the week of 9/23: official Treasury custody +$12.4B, which does not corroborate an official step-back | Logged. **ZHAO's inferred 9/30 settlement is now VERIFIED** (TreasuryDirect corpus, `91282CRN3` issue date 2026-09-30). The reader is H.4.1 for the week ending 9/30, released Thu 10/1, the same evening as the FR2004 print. |
| WALTER −001 | HANS-T-10 fired (OAT–Bund 109.9, OAT 4.67 [9/24]) | INFO. Relevant to VX-BND-19 (EZ rates). The spread leg rests on one secondary aggregator. |
| WALTER −003 | First DGS10 close above 5.00 was 9/16 (5.01) | INFO. Consistent with this desk's H.15 pull. |
| WALTER −010 | Gilts 10Y 5.40 and 30Y 5.89, about 11bp under HANS's lines | INFO. |

STATUS: ✅ DONE
CHANGED: this memo; PROME/inbox/2026-09-26_from-BOND_cadence-and-watch-terms.md; AGENTS/BOND/{workbook/KB.tsv, SCRATCH.md, STATUS.md, analysis/2026-09-26_WQ-291_kill-rule_base-rates.{py,out.txt}, analysis/2026-09-26_WQ-246_dfii10_persistence.py}; 6 inbox items → processed/
RESULT: WQ-291 — 5Y fire graded on FR2004 3–6Y, trade-date window (PRE 9/16 $47.986B → POST 9/23, prints 10/1), MET iff Δ ≥ +$8.6B (p90 of 44 5Y weeks; hit 0 of 9 historical 5Y I′ fires vs 7/9 for long-end >0); 3–6Y governs, long-end is only reported. WQ-246 — 5 consecutive published closes ≥2.50 (inclusive; any close below resets), a decision made now; both counts already met, so no score, gate or position moves and NO-ADD stands.
GAPS: 3–6Y Δ does not track dealer award size (r=−0.08), disclosed in the letter. Funding leg's session window for the 9/23 fire unset. WATCH_FOR coverage audit not run. Boot recompute rc=1 (2 FR2004-vintage pattern hits on history lines, not edited); closeout_check rc=0.
WILL_NEEDS: Two approve-or-amend words before the 10/1 16:15 ET print: WQ-291 letter (Part 1 box) and WQ-246 count + comparator (≥ vs >).
FOLLOW-UP: If ruled, BOND grades the 9/23 5Y on the 10/1 print by the 10/2 boot, the same evening as FORUM-7 D3 and ZHAO's H.4.1 week-9/30 reader.
