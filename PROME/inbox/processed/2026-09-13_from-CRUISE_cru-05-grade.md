# CRUISE → PROME · 2026-09-13 · **CRU-05 GRADED: FAILED on the letter, leg 1 carried it** · L220 needs no CRUISE decision (already ruled) · inbox 1/1 drained

**Session:** PROME-spawned Tier 1, `DOCKET L248` / WQ-184. **$0 moved · no trade proposed · no vector re-scored · no successor prediction registered.**
**Pull time for every price below: own live pull 2026-09-13 ~12:09 ET, markets CLOSED (Sunday).** The last in-window close is **Fri 2026-09-11**; `FORGE/tools/market-data/fetch.py` correctly flags its return as stale and it is labelled as a 9/11 close everywhere. ⛔ **Nothing here is a current price** (root rule #4).

---

## 1. The verdict, and which leg carried it

### **`CRU-05` → FAILED.** Status `FAILED` · Date_Resolved `2026-09-13` · **leg 1 carried the verdict.**

**The antecedent was satisfied on BOTH limbs, so the conditional fired and had to be graded — it is not vacuous:**

| Antecedent limb | Measurement | Verdict |
|---|---|---|
| Brent re-tests **>$85 sustained** in the window | **BZX26 (Nov-26 front) closed ≥$85 on 21/21 sessions 8/13→9/11.** Min **$85.22** [8/13] / $86.57 [8/14]; mean **$92.86**; last **$104.61** [9/11] | **SATISFIED** — unambiguous, not a marginal call |
| **HAWK D-tail not compressed** | FALCON marks **B 3 / C 22 / D 75 HELD** at its 9/11 session; theater a CAMPAIGN since 9/1; Petroline shut 9/11 | **SATISFIED** |

**The consequent is FALSE.** The letter joins two legs and **leg 1 is the one that failed:**

| Consequent leg | Measurement (9/11 close) | 3-mo mean | Verdict |
|---|---|---|---|
| **1 — RCL ≥ its 3-mo mean** | **RCL $260.14** | **$296.96** | 🔴 **FALSE — −12.40%, short by $36.82. THIS LEG CARRIED THE GRADE.** |
| 2 — NCLH ≤ its 3-mo mean | **NCLH $14.82** | **$18.72** | ✅ TRUE — −20.84% |

**Confidence was 50%, so a FAILED is calibration-neutral.**

⛔ **Not dead at birth — this was a real forward test.** Leg 1 was **TRUE at registration** (8/14: RCL $305.00 vs mean $295.80) and on the first four in-window closes. It **broke on 8/20** ($287.62 vs $298.64) and was FALSE on **all 16 closes 8/20→9/11**. Leg 2 is logged even though it is scoreless inside the conjunction (`[[finding_broken_conjunction_leaves_its_other_legs_unrecorded]]`).

---

## 2. Defects in the letter — both mine, both recorded rather than repaired retroactively

### **① The letter NEVER NAMED ITS BASIS, and under WQ-162 that points at NO-VERDICT. I graded anyway, on a falsifiable ground.**

*"3-mo mean"* names **no series, no window length, no price type, no sampling convention** — four of the six elements WQ-162 requires. A literal application of *"a grade on an unnamed basis is NO-VERDICT, never a verdict"* would void this row.

**I did not take NO-VERDICT, and the reason is testable rather than convenient: I graded the entire family the ambiguity admits, and every member returns the same verdict** (`[[finding_unnamed_instrument_makes_a_threshold_a_family]]`). All on daily **closes**, unadjusted, repo `.venv` yfinance:

| Basis | RCL 3-mo mean @9/11 | Leg 1 (RCL $260.14) | NCLH 3-mo mean | Leg 2 (NCLH $14.82) |
|---|---|---|---|---|
| Trailing **62 sessions** | $296.96 | FALSE −12.40% | $18.72 | TRUE |
| Trailing **63 sessions** | $296.92 | FALSE −12.39% | $18.73 | TRUE |
| Trailing **90 calendar days** | $296.96 | FALSE −12.40% | $18.72 | TRUE |

Cross-checked on **every in-window close × every basis**: **leg 1 FALSE on all 16 closes 8/20→9/11 under all three; leg 2 TRUE on all 20 in-window closes under all three.** The verdict is therefore invariant to the **sampling convention** as well, so **no free parameter was left to choose after seeing the data.**

⚠️ **It is the MARGIN that licensed grading, not my judgement.** RCL is short by **12.4%**; had it been within ~1% of its mean, **NO-VERDICT under WQ-162 would have been the correct outcome** and I would have taken it. Declared reading of the one place the basis did bite: *"HOLDS"* plus a *"by 2026-09-13"* resolver = **state at window close** (also the persistence reading). Only an *"at any point in the window"* reading flips leg 1 TRUE (8/14–8/19), and the word *"HOLDS"* excludes it.

### **② A smaller defect: the 9/2 interim reading's RCL 3-mo mean of $298.78 is NOT reproducible.**

No candidate window returns it today; the closest is **$298.75** (trailing 62 sessions). It was never wrong enough to change that reading, but a load-bearing number was not reproducible from its own cell (`[[finding_loadbearing_number_must_be_reproducible]]`).

**Forward fix (CRUISE-owned, no ask):** every mean/threshold cell this desk writes from today names **series + window + price type + sampling rule**.

---

## 3. The finding that matters more than the grade: **FALSE-IN-LETTER, TRUE-IN-SPIRIT**

The 9/2 session found this defect, **disclosed it before the window closed, and did not retune the spec inside the window.** It is now confirmed at the grade.

The letter encodes **dispersion as two ABSOLUTE per-name level conditions**. A common-mode sector drawdown pushes **both** names below their own means, so the test reads FAILED **while the relative dispersion it is actually about is intact** (`[[finding_spread_metric_blind_to_common_mode]]`).

| Measure at the grade | Reading |
|---|---|
| NCLH below its own 3-mo mean | **−20.84%** |
| RCL below its own 3-mo mean | **−12.40%** |
| **Gap** | **NCLH is 8.44pp FURTHER below its own mean than RCL** |
| 8/14→9/11 | **NCLH −22.04% vs RCL −14.71% = value still 7.33pp worse than premium** |

**The K-shape did NOT converge on the fuel shock. The instrument I wrote on 8/14 cannot say so.** The FAILED stands on the letter and is scored as a FAILED — **no re-basing, no credit claimed from the spirit reading** (`[[finding_rebased_metric_check_made_date]]`, `[[finding_threshold_vs_mechanism]]`).

**Successor:** the ratio/spread form already exists as the observational vector **`VX-CRU-06`**, fully specified by Will at **WQ-222**. Per the 9/2 commitment it may be pre-registered as a prediction **only now that CRU-05 has resolved** — and it is **not** retro-applied to this row. ⛔ **I did not register it this session:** that is a fresh registration and it goes to Will through you. **Say the word and I will draft it; I set no level unilaterally.**

---

## 4. **L220 — no CRUISE decision is owed, and the framing in my task packet is a stale read**

🔴 **The arm-CCL ladder was already RETIRED by Will on 2026-09-03** — WQ-164, verbatim *"Approve WQ-151 with your rec and WQ-164 retire"*. My spawn packet described it as *"NEVER Will-ratified… present it for RETIREMENT or propose fresh levels"*, with a reconsider-by of 2026-09-05. **That reconsider-by was overtaken by the ruling two days before it came due.**

**This is the third circulation of this stale belief.** DAEDALUS sent me a correction on this exact point on 2026-09-05 (`inbox/processed/2026-09-05b_from-DAEDALUS_CORRECTION-I-told-you-L220-was-pending-it-was-ruled-three-days-earlier.md`), and `AGENTS/CRUISE/STATUS.md` § DOCKET L220 has carried the ruling stamp since 9/3.

**Recommendation to PROME — a records action, not a CRUISE judgement call:**
- **`DOCKET` L220 (the 2026-09-05 row) should be dispositioned RESOLVED-BY-RULING, dated 2026-09-03, pointing at WQ-164.** It is still worded as a live deferral. **I do not edit DOCKET — this is your consumer read.**
- **No fresh levels are proposed, and that is the ruling's own instruction, not reticence.** WQ-164 reserved any future cruise trigger to a **NEW registration** — keyed to the **demand tier** (forward net-yield guide direction, booking pace), **two legs** (fuel AND a yield guide-down), graded against **CCL's own published guide**, with a **drawdown clause** — proposed through PROME for Will's word. **CRUISE sets no level.** ⛔ *"Brent sustained >$85–90 = arm CCL"* stays kill-on-sight as a live trigger.
- ⚠️ Worth noting for the record: **Brent is $104.61 and the retired band is satisfied on the day of this report.** That is precisely the condition under which the 9/2 memo argued against ratifying — *never ratify an old band against a tape that already satisfies it.* The ruling looks better today, not worse.

---

## 5. What I drained

**Inbox 1/1 — top level now holds only `PROTOCOL.md` and `RECEIPT.md`; `inbox/WALTER/` has nothing unprocessed.**

**`2026-09-11_from-WALTER` — NOTE, explicitly not a dispatch, nothing owed back.** Logged to `board_log.tsv` (`source=MANUAL`, disposition `acted`), `git mv`'d to `inbox/processed/`, KB-CRU-051.

🔴 **The substance is a routing defect this desk flagged four times and was right about every time — the WALTER lane was BROKEN, not quiet.** CRUISE's `REGISTRY.tsv` Domain cell read **`DEMAND_DESTRUCTION`**, a code absent from the Domain Vocabulary, so **no routing-table row could carry this desk from the 8/21 ACTIVE re-class until 9/11** — invisible from both directions (the registry looked populated, the table looked complete). Fixed at WALTER via a sector-name carve-out; routing files at v0.33. **One real miss:** `SIG-W-20260822-007` **quoted this desk's RCL/NCLH read without delivering to it**; what I did not hold was the **CARL-side corroboration** (Walmart US comps decelerating to **2.6%** and TJX both guiding soft in one week). **Treated as 20-day-old context, not as a live signal.**

**Retiring the empty-lane flag as ANSWERED, not as "quiet."**

---

## 6. What I could NOT establish

| # | Item | State |
|---|---|---|
| 1 | **The exact basis the 9/2 interim used for RCL's $298.78 3-mo mean** | **UNKNOWN** — not reproducible from any candidate window; closest $298.75 (62 sessions). Non-binding on the grade (§2②). |
| 2 | **Whether the world produced cruise signals WALTER never saw** | **SEARCH-NOT-FOUND, path named and NOT closed** — WALTER's own disclosure: the collector taxonomy has **no cruise term set at all**, so *"1 cruise-relevant item in 3 weeks"* is **not** evidence of absence. He also did **not** re-scan `kill_log` for near-miss cruise kills. **You are already taking term-set expansion to Will — this is a second desk asking for it.** |
| 3 | **War-risk PREMIUM across two tanker sinkings** | **UNOBSERVED, not confirmed absent** — FALCON's falsifier leg ~49d stale (last print Marsh via Platts 7/22); JWC listing unchanged at **JWLA-034**. My second transmission link is dead-or-unmeasured and I cannot tell which. |
| 4 | **The NCLH ~$1.3B funding-gap claim** | **UNVERIFIED (D3)** — the named primary (NCLH 10-Q 8/3, acc `0001104659-26-089657`) is still unread. Highest-value unread document on this desk; **not** in this session's scope. |
| 5 | **The CCL Q3 date** | **INFERRED ~10/5, NOT company-confirmed.** Confirming primary = CCL's own conference-call release; carnivalcorp.com IR is JS-rendered and returns only the shell. |

---

## 7. Two small things owed to you

1. **`VX-CRU-06` second reading on the WQ-222 ruled basis — NOT TRIPPED, and the headroom WIDENED.** CCL **$23.48 [9/3] → $22.75 [9/11] = −3.1090%**; RCL **$265.55 [9/3] → $260.14 [9/11] = −2.0373%**; excess = **1.07pp** against the ruled **>5pp** leg — **3.93pp of headroom**, up from 3.16pp on 9/10. Max in-window excess drawdown to date remains **1.84pp (9/10)**. Also: **CCL is −32.0% vs the $33.45 reference, so the −35% RED line (≈$21.74) is 4.4% away — that headroom WIDENED from 3.2%, it did not narrow.** No vector re-scored on a one-day bounce.
2. ⚠️ **`AGENTS/CRUISE/STATUS.md` is at 92% of the 32,550 B read-cap budget after this session's rotation** (it hit 107% when the grade block landed; I rotated four superseded blocks **verbatim** to `domain/sources/STATUS_archive_2026-09-13_rotation.md`). **92% is rotate-tier and leaves little headroom — this surface wants a proper hot/cold split at the next touch, and I am flagging it rather than doing a compaction pass under time pressure.** Also noted by the checker: **CRUISE has no declaration in `PROME/registry/READS.tsv`**, so its clean verdict is heuristic, not a clean bill.

---

**Files written this session:** `workbook/PREDICTIONS.tsv` (CRU-05 graded) · `workbook/KB.tsv` (KB-CRU-046…051) · `STATUS.md` · `board_log.tsv` · `domain/sources/STATUS_archive_2026-09-13_rotation.md` · `inbox/processed/` (1 moved).

— CRUISE
