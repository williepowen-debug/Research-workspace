# AI_INFRA_CAPEX — COHERENCE REVIEW, 2026-08-31

reviews_cluster: AI_INFRA_CAPEX

**Date:** 2026-08-31 · **Run by:** WALTER · **Trigger:** `walter_doctor cluster_review_overdue` — 70 signals, last review **35d** ago, past the 30d window. Will-ruled priority #1 this session.
**Authority:** `CLUSTER_TAXONOMY` v0.7 — cadence trigger; the **v0.6 bidirectional test is unchanged and remains the instrument**. Evaluation is WALTER-owned, no Will gate; **changing structure is Will's** (RULE 8).
**Precedent:** [`AI_CAPEX_AXIS_CHECK_2026-07-27.md`](AI_CAPEX_AXIS_CHECK_2026-07-27.md) · [`AI_CAPEX_AXIS_CHECK_2026-07-16.md`](AI_CAPEX_AXIS_CHECK_2026-07-16.md)

---

## 1. VERDICT

> **KEEP the cluster. Limb (a) does NOT fire — but it has moved to the boundary (5 populated angles, was 4). Limb (b) still fires, on ONE original angle instead of two.**
>
> 🔑 **THE HEADLINE IS NOT THE VERDICT — IT IS THAT THE JULY DIAGNOSIS WAS RIGHT, THE PRESCRIBED FIX SHIPPED, AND THE ANGLE CAME BACK.** `memory / input-cost` went **0–1 → 13 signals**, from dead angle to the cluster's **second-largest**, and the recovery is traceable to the exact keyword rules that were added. **This is a closed loop: diagnosis → fix → measured recovery.** It is the first time this cluster's review has been able to say that.

## 2. SCOPE + METHOD (stated, because limb (b) is not mechanizable)

**70 signals total** (reconciles with `/BOARD/INDEX.md` ToC and `board_reconcile`). **52 in the trailing 60d window (2026-07-02 → 2026-08-31).**

⚠️ **There is still no `axis:` field on signals**, so angle assignment is a **judgment read of all 52**, not a count. Method: **primary angle per signal**, assigned on the signal's *subject*, not on term presence. **A MENTION IS NOT A DECLARATION** — the 7/27 lesson that created the `reviews_cluster:` requirement applies to me here too: a keyword scan for `depreciat|obsolescen` returned **8 hits**, and on inspection **7 were passing mentions inside signals about credit, power or market structure.** Counting those would have manufactured an obsolescence angle that does not exist.

## 3. THE BIDIRECTIONAL TEST

### Limb (a) — DISPERSION: angle count > 5?

| Angle | 60d signals | Populated? | vs 7/27 |
|---|---:|---|---|
| **financing** | ~15 | ✅ dominant | ~10 — still the plurality, but no longer a majority |
| **memory / input-cost** | **~13** | ✅ | **0–1 → 13. THE CHANGE.** |
| **ROI / capex-guidance / FCF** | ~11 | ✅ | 2–3 → 11 |
| **power** | ~8 | ✅ | 3 → 8 |
| **supply-chain / geopol-semis** | ~4 | ✅ | 2–4, stable |
| **obsolescence** | **1** | ❌ | 0 → 1 |

**Genuinely populated: 5. Not >5. ⇒ LIMB (a) DOES NOT FIRE.**

⚠️ **But record the movement rather than just the verdict: this was 4-populated-with-a-5th-marginal on 7/27 and is now a clean 5.** The test asks >5, so **one more genuinely populated angle fires it.** The cluster has **broadened**, which is the opposite of the 7/16 and 7/27 finding that it was *concentrating*. **Financing fell from ~57% of the cluster to ~29%** — not because financing slowed (10 → 15) but because everything else grew faster.

### Limb (b) — CONCENTRATION: any ORIGINAL angle < 2 in 60d?

Original four: **financing · ROI · obsolescence · input-cost.**

| Original angle | 60d | Fires? |
|---|---:|---|
| financing | ~15 | ✅ no |
| ROI | ~11 | ✅ no |
| **input-cost / memory** | **~13** | ✅ **no — RECOVERED, was firing** |
| **obsolescence** | **1** | ❌ **FIRES** |

**⇒ LIMB (b) FIRES on obsolescence alone — down from two angles on 7/27.**

## 4. 🔑 THE MEMORY RECOVERY — verified at the artifact, not assumed from timing

The 7/16 and 7/27 reviews both concluded the memory angle was empty **in WALTER's INTAKE, not in the domain** (TrendForce **0 hits in 764 archive rows**; Micron's FQ3 beat *"never entered WALTER — not killed, never seen"*). The 7/27 review recommended adding memory-pricing and megacap capex-guidance lines to the RESEARCH-INTAKE lane.

**That fix shipped.** `newsweep_config.py` now carries:
- **line ~119–129, added 2026-07-16:** `"TrendForce" OR "DRAM contract price" OR "NAND pricing" OR "memory shortage" OR "HBM"` (label `memory-cycle`) **and** `"hyperscaler capex" OR "AI capex" OR "data center capex" OR "capex guidance"`.
- **line ~229–240, ruled 2026-07-28, shipped 2026-07-30** (option-3 keyword lane, after the DRAMeXchange endpoint time-box failed): label `memory-pricing`.

**The memory surge begins 2026-07-31 — the day after the lane shipped.** ⚠️ **Temporal correlation is not attribution, so I traced origins.** Seven memory signals sampled; **six name the lane explicitly and by rule:**

| Signal | Origin |
|---|---|
| `-20260731-002` | RESEARCH-INTAKE `newssweep` 7/31 — 8 NEW_WATCH on the **`memory pricing` / `TrendForce`** rules |
| `-20260807-003` | RESEARCH-INTAKE NEW_WATCH (**TrendForce** 8/06) |
| `-20260812-008` | RESEARCH-INTAKE sweep 8/12 — NEW_WATCH ×2 (**TrendForce**) |
| `-20260817-002` | RESEARCH-INTAKE `news.json` 8/17 NEW_WATCH cluster (VULCAN-tagged) |
| `-20260826-003` | RESEARCH-INTAKE newssweep — **7 NEW_WATCH on kw `TrendForce` in one day** |
| `-20260828-034` | **Will-Telegram** — the one exception (Bernstein double-ordering survey) |

⇒ **The recovery is caused by the shipped fix, on the exact rules the diagnosis prescribed.** **A second cause also resolved:** the 7/16 check found WALTER's own *clustering* was filing memory signals under `ASIA_CHINA`; all 13 now sit in `AI_INFRA_CAPEX`.

📌 **Why this is worth stating at length rather than as a tick:** the July reviews made a **falsifiable causal claim** — *"this angle is empty because we don't collect it, not because the domain went quiet"* — and staked a specific remedy on it. **The remedy shipped and the angle recovered 13×.** `[[finding_count_measures_intake_not_domain]]` is now **confirmed by intervention**, not just by argument.

## 5. 🔴 OBSOLESCENCE — the diagnosis has CHANGED, and the remedy is the one that just worked

7/27 said: *"nobody in the fleet owns hyperscaler depreciation schedules."* **That is no longer the whole story.** Running the doctor's own mandated discriminator — *is the angle empty in the DOMAIN or empty in INTAKE?*:

| Check | Result |
|---|---|
| **INTAKE** — depreciation/useful-life/obsolescence queries in `newsweep_config.py` | **ZERO.** No collection exists for this angle at all. |
| **DOMAIN** — does VULCAN engage with it? | **Yes** — it appears in VULCAN's `THESIS.md`, `LESSONS.md`, `STATUS.md`, `SCRATCH.md`, and VULCAN has received two WALTER pointers (7/24 NOTE *"depreciation-pointer-hits-your-named-obsolescence-gap"*, and `SIG-W-20260828-050`). |
| **INSTRUMENT** — any registered VULCAN threshold on depreciation/useful life? | **NONE.** grep of VULCAN's `registry/*.tsv` + thesis returns nothing. |
| **WORLD** | **Not empty.** Depreciation schedules and useful-life assumptions are disclosed quarterly by every hyperscaler. |

**⇒ Obsolescence is empty in INTAKE (zero queries) and UNINSTRUMENTED in the domain (zero threshold rows) — while being live and published in the world.** That is the `HANS-T-12` shape: **a registered angle with no metric surface cannot fire however far it moves**, and a row-count audit passes clean over it forever. `[[finding_banded_threshold_with_no_metric_surface_is_untrippable]]`

🚩 **And the one signal that would move this angle off <2 is sitting UNCONSUMED right now.** `SIG-W-20260828-050` (BCA: hyperscaler capex >$1T in 2027, **margins forecast to RISE while D&A runs to 36% of EBITDA**) — the cleanest depreciation datum this cluster has had since 5/11 — is in `AGENTS/VULCAN/inbox/WALTER/`, delivered 8/28, **not yet consumed.** VULCAN is one of the desks on the doctor's dark-ACTION list (6 unconsumed, 5 ACTION).

## 6. RECOMMENDATIONS

**Cluster action: NONE.** Keep it whole. Limb (a) has now failed three times across 46 days and 47 further signals. The angles still answer one question — *"does the buildout continue?"*

1. **🔴 ADD AN OBSOLESCENCE / DEPRECIATION COLLECTION RULE TO THE INTAKE LANE — the same remedy that just worked on memory, on the last angle still failing limb (b).** Candidate terms: `"useful life" · "depreciation schedule" · "server refresh cycle" · "GPU depreciation" · "asset impairment"` scoped to hyperscaler/AI-infra names. **The argument is no longer theoretical: the identical intervention on the identical cluster produced a 13× recovery in 32 days, and the origin trace proves the lane did it.** Lane scope is PROME's surface and the ruling is Will's — **proposed, not built.**
2. **🟠 VULCAN owes an instrument decision, not a data point.** Even with collection, obsolescence has **no registered threshold**, so it cannot fire. Ask VULCAN whether depreciation/useful-life gets a `VULCAN-T` row — **or whether it should be formally folded into ROI**, which is exactly VULCAN's own proposed 5-axis re-cut. **Either answer resolves limb (b) honestly; leaving it unowned does not.** ⚠️ Note the incentive trap and state it plainly: **folding obsolescence into ROI would make limb (b) stop firing without anyone learning anything about depreciation.** That is a legitimate taxonomy simplification and an illegitimate way to silence a trigger — it must be decided on the merits, and the merits are VULCAN's and Will's.
3. **🟡 The 5-axis re-cut is now better supported by evidence than it was.** `financing · ROI (incl. obsolescence) · memory/input-cost · power · supply-chain-geopol` — proposed by VULCAN 7/16, **still not adopted**, needs Will + VULCAN. **What this review adds:** four of those five axes are now independently populated at ≥4 signals (financing 15 · memory 13 · ROI 11 · power 8 · supply-chain 4), so the re-cut now *describes the observed cluster* rather than predicting it. **Honouring VULCAN's caveat — *"arrive there by the reasoning, not by deference to my frame."***
4. **📌 Watch limb (a).** At 5 populated angles the cluster is one angle from firing the dispersion limb. **If the obsolescence collection in (1) ships and works as memory did, limb (a) fires next review** — and that would be a *good* problem, caused by fixed collection rather than a fragmenting domain. **Say so at that review, or the next reader will read a successful fix as a split signal.** That misreading is precisely what 7/27 caught and is this cluster's recurring failure mode.

## 7. CAP POLICY — the 7/27 recommendation is DISCHARGED

7/27 recommended retiring per-cluster numeric caps fleet-wide. **`CLUSTER_TAXONOMY` v0.7 did exactly that the same day (Will-approved), replacing the cap with this cadence check.** Nothing further owed. **This review is the first one produced by the replacement mechanism**, and it is worth recording that the mechanism worked as designed: the cadence fired at 35d on a cluster nobody was looking at, and it surfaced a *recovery* rather than a breach — which a row-count cap could never have shown.
