---
name: finding_test_the_guard_not_just_the_guarded
description: "Three consecutive guard-builds each shipped with a v1 defect only RUNNING them revealed — and the failure DIRECTION decides the cost: a guard that fails NOISY gets fixed on its first false alarm, one that fails SILENT reports healthy forever and is worse than no check"
metadata:
  node_type: memory
  type: finding
  originSessionId: 5f21c120-9c30-4c19-b4e5-6edec656e299
  modified: 2026-07-29T02:13:24.099Z
---

**Three governance/health checks built by WALTER on consecutive days each had a v1 defect that only EXECUTING the check revealed — code review and design intent caught none of them (n=3, 2026-07-27/28, PROME-endorsed promotion):**

1. **Cluster-cadence check v1** inferred a review's subject from whether the cluster NAME appeared in its body — reported four clusters as freshly reviewed because a thorough review *name-checks peers it is not about*. Failure direction: **SILENT** (everything reads FRESH forever; the check goes quiet and looks healthy).
2. **`delivery_claim_vs_git` v1** fired **17 false HIGHs** on its first run (a retired inbox dir + an agent that consumes by DELETING). Failure direction: **NOISY** — annoying, but it got fixed within the hour *because* it fired.
3. **`memory_index_check` v1** flagged `README` as an unindexed memory. Fixed **by construction** (require the canonical slug shape) rather than a denylist that breaks on the next template. Failure direction: noisy, cheap.

4. **A guard that AGED into pointing the wrong way — the silent-failure direction, realised.** *(Added 2026-07-28, BRENT. n=4, and the first instance where the defect was not in v1 but in the WORLD moving under a correct v1.)* BRENT's `thresholds.py` runs on **every boot** and carried `Brent <$75 = "THESIS BREAK, squeeze failed"` and `<$85 = "squeeze weakening, front-running peace"`. Both were **correct when written at thesis v4**. At v5 the thesis **retired sub-$75 as a break** (it is structural decoupling, and *thesis-CONFIRMING*) and graded $85×3 as **fired = sustained premium, i.e. bullish**. The script was never repointed, so the boot instrument would have alerted **in the exact opposite direction of the thesis it exists to serve.** **Not hypothetical: Brent opened at $84.95 — below the $85 line — on the very day the strike pause broke and the premium re-widened.** A morning boot would have printed *"squeeze weakening, front-running peace"* at the moment the opposite was happening. A third row (`Dated Brent <$100 = "physical squeeze resolving"`) was **firing every single boot**, inferring physical tightness from flat price — the precise inversion of that thesis's central finding — and had become pure alert-fatigue noise.

   **Root cause worth more than the instances:** the script's header credited its numbers to a workbook ledger **frozen four weeks earlier**. **A guard that restates a registry inherits that registry's staleness silently, and a FROZEN source cannot signal that it stopped moving.** Fix class: **guards must READ the canonical registry, never RESTATE it** — or, where restating is unavoidable, name the canonical file in the header and re-verify on every version bump of the thing it guards. (Fleet n=2 with REGINALD; entering the blueprint.)

   **The direction lesson, sharpened:** cases 1-3 asked *does the guard fail silent or noisy on day one?* This adds *does it fail silent or noisy on day one hundred?* **A guard whose thresholds encode a superseded worldview fails SILENT in the worst way available — it is loud, confident, and backwards**, and it is trusted precisely because it is automated and has "always been there." **Version-stamp every guard against the doc it serves; when you bump the doc's version, grep the guards.**

**Why:** a guard encodes assumptions about the artifact it watches (naming conventions, consumption patterns, what "about" means), and those assumptions have never been exercised until the guard runs against real data. The guarded system's defects are known; the guard's own defects are brand new.

**How to apply:** before shipping any check/guard/tripwire, (a) run it against a known-GOOD case AND a known-BAD case — synthetic is fine; (b) ask *which direction does this fail when its assumption breaks?* — a silent-failure design (false all-clear) must be rebuilt to fail loud or fail visible, because a wrong guard that reports healthy is strictly worse than no guard: it retires the vigilance that would otherwise exist. (c) Prefer fixes **by construction** (make the document declare its subject; require the slug shape) over enumerated exceptions, which rot. Companion to [[finding_standing_guard_is_a_false_negative_risk]] (a *correct* guard can still wave away the real event) and [[finding_single_witness_guard_deletes_real_data]]; distinct from both — this is about the guard's OWN v1 defects and their failure direction.
