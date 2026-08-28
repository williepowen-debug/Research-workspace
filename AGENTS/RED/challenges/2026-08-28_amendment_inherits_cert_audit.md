# CHG-051 AMENDMENT-INHERITS-CERTIFICATE AUDIT (S38h)

**Date:** 2026-08-28 ~15:3x ET
**Trigger:** ML-RED-203 (NEXUS 2026-08-28 §6.2 self-charge on their own CHG-046 resolution artifact — extended to RED's registry as the sibling class to CHG-051 charge B, EDIT axis rather than TIME axis).
**Owed:** rider to CHG-051 naming both staleness axes + per-row audit of FT-01/FT-06/FT-07 (Will-directed today's focus list). Expanded to FT-08 + FT-11 because they came up under the same class in the audit.
**Verdict:** NO LIVE ML-203 DEFECT on the audit set today; three future-risk / class-neighbor items flagged. NO WEIGHT MOVED.

---

## 1 · THE TWO STALENESS AXES (rider text for CHG-051)

**Charge B is a two-axis defect, not one:**

- **AXIS ① — TIME staleness (CHG-051 charge B, published 2026-08-27):** base rates computed once at registration and never RECOMPUTED. Fix: scheduled recomputation via `base_rate_review.py` (boot 9d). Live examples: FT-01 published 21.8% → 48.3% @120obs regime descriptor; FT-07 32.5% → 84.2%. Cause: passage of time + regime drift.

- **AXIS ② — EDIT staleness (NEXUS ML-203, added 2026-08-28):** base rates NOT REVERIFIED against an AMENDED spec text — amendment inherits the ORIGINAL's construction certificate. Fix: at any spec amendment, re-run the base-rate check against the AMENDED text BEFORE landing. Live example: NEXUS's own T6 successor-falsifier (ADDENDUM 2 stripped B's ratio leg → B's reachability collapsed 85.9% → 0.0% as a side effect; the 8/28 falsifier as it graded could only produce C).

**Both axes belong to the same class (base rates are apparatus data, not one-shot registration data). Both need scheduled checks. Different triggers, different remedies.**

---

## 2 · PER-ROW AUDIT (FT-01, FT-06, FT-07 + FT-08, FT-11)

| Row | Amendments since registration | Base-rate re-verified vs AMENDED text? | Verdict |
|---|---|---|---|
| **FT-01** HY<280 s=3 | S36d label change: `IMMEDIATE-FALSIFY` → `SUSTAINED-CALM-COUNTER-SIGNAL` | **YES — the measurement drove the amendment.** The 48.3%@120obs re-computation IS what forced the label change. Certificate was RE-VERIFIED at the amendment. | ✅ **COMPLIANT** |
| **FT-06** VIX<16 s=5 | Magnitude set post-hoc at fire time (S29 8/12; ML-144 spec defect disclosed on the row) | **YES on ML-203 axis** (base rate 5.8%@120obs, stable ~1.0× vs published 6.9%). Amendment was ACTION-side (magnitude), not CONDITION-side. Base rate is about CONDITION frequency, unchanged. | ✅ **COMPLIANT on ML-203 axis** (pre-existing ML-144 defect separate: magnitude post-hoc; disclosed) |
| **FT-07** CCC>930 s=1 | NONE YET — re-spec pending 9/4-9/11 window | Base rate re-computed at S36d review (84.2%@120obs / 100.0%@60obs vs published 32.5% — regime DESCRIPTOR). No amendment has landed; no ML-203 defect present today. | ⏳ **WATCH** — the 9/4-9/11 re-spec MUST re-base-rate against the AMENDED text BEFORE landing. Standing rule below. |
| **FT-08** Core CPI ≥0.4% MoM w/ 3-mo ann. ≥3.0% | ML-156 fix — SAM found the conjunction AND-leg sat in notes vs. machine columns; leg moved into machine columns | **N/A** — amendment was REPRESENTATIONAL (leg location), not semantic. Base rate is MANUAL (release-derived 3-mo compound, no continuous series by design — review at each CPI print). Nothing to re-compute. | ⚠️ **CLASS-NEIGHBOR** — the row's manual-review methodology has NO computable base rate to update against amendment; ML-183 issue (audit-inherits-granularity), NOT strictly ML-203. Recorded for the class census. |
| **FT-11** UST 30Y buyback attribution classifier | S36c amendment on BOND's review — leg CHOICE stands, rationale repaired struck-in-place, limit (e) added, v1.1 pre-registered as ex-ante F2-gated conditional | **YES on the current legs** (trigger legs unchanged per S36c; base rates 4.2% precondition @120obs / 88.8% classifier prior stand). **⚠️ BUT** — v1.1 conditional (butterfly leg `2*DGS20−DGS10−DGS30` swap under BOND's F2 read) has NO base rate registered. | ⚠️ **FUTURE RISK** — if v1.1 fires (BOND F2 reads off-the-run post-9/9), the butterfly-leg swap MUST be base-rated BEFORE the trigger switches to it, or the row falls into the exact ML-203 defect NEXUS just charged RED with. **Rider owed on FT-11 row.** |

---

## 3 · STANDING RULE ADOPTED (for the 9/4-9/11 re-spec window and beyond)

**⚑ At the 9/4-9/11 re-spec window (FT-04, FT-07, FT-08, VX-004 all queued for re-review), and at any FUTURE amendment to any RED registry row:**

**Any change to a trigger's CONDITION (metric / threshold / sustain / leg structure) MUST re-run `base_rate_review.py` against the AMENDED text BEFORE the amendment lands.** The current `base_rate_review.py` reads the row AS-IS — it does not know whether the row was just amended. Enforcement is BEHAVIORAL, not tool-side, until the tool learns to diff spec-versions.

**Failure mode this catches:** a spec amendment inherits the ORIGINAL's construction certificate (NEXUS's Pass B base-rating adopted 4 sessions before B's ratio leg was stripped; B went from 85.9% reachability → 0.0% as a side effect; nobody re-ran the check because the amendment was locally-defensible on the leg it CHANGED, not the leg it INHERITED).

**Corollary rule (from the FT-11 audit finding):** any conditional spec-swap (`if X then use leg Y`) MUST base-rate leg Y at REGISTRATION of the conditional, not at the moment leg Y activates. FT-11 v1.1 owes this now.

---

## 4 · WHAT THE AUDIT DID NOT FIND

**No LIVE ML-203 defect on any of the five audited rows today.** The class is real; the current registry passes the check by measurement, not by luck. Three future-risk / class-neighbor items flagged (FT-07 at the 9/4-9/11 window, FT-08 as a class-neighbor via ML-183, FT-11 v1.1 as future risk).

⚠️ **HONEST NEGATIVE CAVEAT:** this audit is bounded by the five rows examined. **A full-registry audit (all 12 rows) is owed** — deferred here because Will's ask was FT-01/FT-06/FT-07 specifically; expanding by two rows preserved the spirit; expanding to all 12 would exceed today's scope. **Standing item: run this same audit against the remaining seven rows (FT-02, FT-03, FT-04, FT-05, FT-09, FT-10, FT-12) at the 9/4-9/11 window when three of them will be under active amendment anyway.**

---

## 5 · APPARATUS CHECK ON THE AUDIT ITSELF

The audit's own construction, run against ML-185 (self-attack list defends the argument, blind to the apparatus):

- **Argument axis:** did I attack the finding? The audit tests whether each row's base rate has been re-verified — that's the argument test. ✅
- **Apparatus axis:** is the audit method itself sound? **⚠️ ONE APPARATUS DEFECT: the audit relies on `last_reviewed` cells being ACCURATE.** If a row was AMENDED post-review-date without the review-date being updated, the audit reads it as compliant when it isn't. **This is the FT-06 magnitude-set-post-hoc defect one level up.** Recorded here so the next audit iteration checks the DIFF of the row's history against the review-date cadence, not just the cell.
- **Meta-apparatus:** RED conducted its own apparatus self-audit; the finding is that RED's audit tool has its own dependency on data-cell integrity. **Turtles-all-the-way-down risk is real but bounded** — the fix is either an authored `AMENDMENTS.tsv` per row or a git-log-based amendment detector; deferred as scope creep for today.

---

## 6 · WHAT MOVES

- **CHG-051's Key_Finding text on `workbook/CHALLENGES.tsv` gets the two-axes rider** (both TIME + EDIT staleness named).
- **FT-11's row gets the v1.1-base-rate-obligation note** (butterfly leg must be base-rated at v1.1 registration, not at activation).
- **FT-07's row gets the standing 9/4-9/11 rule made explicit** (re-base-rate against amended text before landing).
- **ML-RED-205 filed** naming this audit as a live application of ML-203, with the standing rule.
- **Full-registry audit is a NEW future-owed item** — added to CHG-051's scope, resolves at 9/4-9/11 window.
- **NO WEIGHT MOVED** (audit finding is about apparatus, not the world).
- **NO trigger states changed** (no fires, no exits).

---

*Audit completed 2026-08-28 ~15:3x ET. Five rows audited (FT-01/FT-06/FT-07/FT-08/FT-11). Zero live ML-203 defects; three future-risk / class-neighbor items flagged. Full-registry audit standing at 9/4-9/11 window.*
