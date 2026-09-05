---
name: feedback-single-month-subcomponent-skepticism
description: "Single-month sub-component metric moves (ISM internals, CMBS by-property-type, single-trust ABS, single-print sentiment, etc) must be flagged \"needs 2nd-print confirmation\" before treating as load-bearing thesis evidence; rule applies regardless of magnitude"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 97a0fc9c-bf53-4fae-8e5d-2da56800198c
---

When integrating a print where a SUB-COMPONENT metric (ISM internals like New Orders / Prices Paid / Employment; CMBS DQ by-property-type; single ABS trust loss; single-month sentiment cohort; single Atlanta-Fed-Wage-Tracker cut; single-trust prepay/CNL; single-month bankruptcy filings YoY%, etc) moves sharply, flag it `[FLAG: single-month, needs 2nd-print confirmation]` in STATUS/KB before treating as load-bearing for a vector score, prediction confidence change, or thesis call. Magnitude alone does not earn load-bearing status; sustained 2-month direction does.

**Why:** Validated CARL Jun 5 2026. ISM Svc Apr 2026 New Orders -7.1pp single-month decel was treated as load-bearing stagflation sub-component anchor in late-May STATUS / KB-CARL-279 — FULLY REVERSED +3.8pp to 57.3 in May print one month later. Single-month sub-component move turned out to be noise, not signal. Pattern is generic: any sub-component of a composite index, sliced metric, or single-trust/single-cohort cut is noisier than the headline; cross-agent risk includes CFTC positioning (single-week noise vs trend), VIX Z-scores (single-day spike), wage tracker tier cuts (single-month tier shift), CMBS by-property (single-month +137bps without follow-on).

**How to apply:**
- Before any STATUS row update / VX status color change / KB row creation that treats a sub-component move as evidence, ask: "is this single-print or sustained?"
- If single-print: include explicit `[FLAG: single-month, needs 2nd-print]` text in Notes and DO NOT let it move a vector score or prediction confidence on its own
- Wait for 2nd print in same direction (any magnitude) OR a 3rd-source corroborating signal before promoting to load-bearing
- Composite headline moves (ISM headline, NFP headline, CPI headline) are NOT sub-components — this rule is for the slices and internals
- Sustained 2-month direction beats sharp 1-month magnitude. Direction at 2 months > magnitude at 1 month.

**3rd validation + write-time corollary (CARL Jun 11 2026):** May CPI hospital services +0.7% MoM sign-flipped back UP from Apr -0.3% — the Apr negative that DOC had staged as a care-avoidance pricing signal was single-month noise; the held-for-2nd-print discipline prevented a false confirm. Corollary: the rule applies at PREDICTION-WRITE time too, in both directions — CARL's Jun-9 pre-registered CPI sheet extrapolated Apr's hot Food-at-Home +0.7% and core +0.4% into "2nd consec" expectations and missed both (May FaH +0.1%, core +0.2%). Over-weighting one hot month when writing a forward line is the same failure as over-weighting one cold month when resolving — inverse of the CRL-01/CRL-19 magnitude-light family.

Related: [[finding_threshold_vs_mechanism]] separates mechanism intact from threshold breached; this rule prevents single-month thresholds from triggering false mechanism conclusions. Compounds with [[feedback_yoy_baseeffect_use_multiyear_stack]] (also a print-isolation discipline).

---

## Extension 2026-09-05 (CARL) — the REVISION axis, which this rule's own remedy does NOT cover

The rule above treats sub-components as **noisy**, and prescribes waiting for a 2nd print. **There is a second failure mode on the same objects that waiting does not fix: the sub-component's published HISTORY gets rewritten, harder than the headline's.** A claim can be 2nd-print-confirmed and still be deleted retroactively.

**Worked case (CARL 2026-09-04/05, BLS Employment Situation).** V16 Employment was moved 3→4 (Will-approved 8/10) on a July NFP first print of **−23K**, *"the first negative print of the cycle."* The cell's K-shape leg — the part that was CARL's own rather than LABOR's — named **retail trade −19K** and **club stores/supercenters −21K**, *"breaking BLS's own flat 12-month pattern… the trade-down destination is shedding staff."*

On the 9/4 vintage (CARL's own arithmetic off FRED levels, not a relayed headline):

| cited at grade time | current vintage | |
|---|---|---|
| headline July **−23K** | **+21K** | 44K swing on a **159,075K** base = **0.028%** |
| retail trade **−19K** (`USTRADE`) | **+13.2K** | 32.2K swing on a **15,488K** base = **0.208%** |
| club stores **−21K** (`CES4245100001`) | **+9.6K** | both now positive in **5-6 of 6** months |
| L&H 2nd straight shed (`USLAH`) | **+62.0K** August | reversed |

**≈7× the relative revision on the sector line vs the headline** *(n=1 instance — a measurement, not a law; worth testing against a longer CES revision history).* The sector legs did not soften. **They sign-flipped**, and with them the only instrument the desk had for its own K-shape claim.

**Why this is the dangerous axis and not just a bigger version of the noise one:**
- **The 2nd-print remedy does not reach it.** Waiting produces a second print of a series whose *first* print is still being rewritten underneath you. Both prints can move.
- **Vintage discipline is aimed at headlines.** Fleet rules ([[finding_derived_metric_across_vintages_biases_toward_stale_leg]], and CARL/PROME's own WQ-175 FROZEN-ON-REVISABLE, ruled 2026-09-04) get applied to the topline figure. **Nobody stamps a vintage on a sector line** — and the sector line is exactly where a thesis claim lives, *because it is the only cut that speaks to the thesis.* The discipline and the exposure are in different places.
- **One sample in four views is not four witnesses — and the views are not equally reliable.** LABOR's INDEPENDENCE_MAP §2 correctly says payrolls/private/revisions/sector lines are one CES witness. The unstated half: **order the views by revision variance**, and the one you want to cite is the worst.

**A forward-only vintage rule protects the VERDICT and leaves the EVIDENCE SENTENCE standing.** WQ-175 correctly held V16's grade intact (a later vintage crossing the bar ⇒ dated annotation, never a re-grade; a letter naming no vintage grades as first published). But **seven CARL surfaces still asserted "July NFP −23K = the first negative print" in the present tense with no vintage tag** — so the protection was invisible and the falsehood was visible. The grade was safe; the presentation was not.

**How to apply (adds to the list above, does not replace it):**
1. When a sub-component/sector line is about to become **load-bearing for a score, a vector move or a Will-facing claim**, write it with its **vintage stamp on the surface**, not only in the changelog: `retail trade −19K [2026-08-07 first print — RECOMPUTE before re-citing]`.
2. **Prefer the level series over the reported delta.** Re-derive the MoM yourself from the published level (`USTRADE`, `PAYEMS`) — that is what makes a revision visible at all; a stored delta silently keeps its old vintage forever.
3. **A grade that RESTED on a revisable sub-component owes a re-check at the next release**, not at the next window. Register it as a revision watch on the row itself.
4. When the revision lands: **annotate, do not re-grade** — and then say plainly, in the same breath, whether the **conviction** survived even though the **score** did. Those are two answers and only one of them is governed by the letter. Related: [[finding_threshold_vs_mechanism]], [[finding_claim_outlives_its_discredited_instrument]], [[finding_impeachment_must_be_scoped_to_the_claim_not_the_source]].
