---
name: finding_test_the_guard_not_just_the_guarded
description: "Three consecutive guard-builds each shipped with a v1 defect only RUNNING them revealed — and the failure DIRECTION decides the cost: a guard that fails NOISY gets fixed on its first false alarm, one that fails SILENT reports healthy forever and is worse than no check"
metadata:
  node_type: memory
  type: finding
  originSessionId: 5f21c120-9c30-4c19-b4e5-6edec656e299
  modified: 2026-07-29T00:20:00.000Z
---

**Three governance/health checks built by WALTER on consecutive days each had a v1 defect that only EXECUTING the check revealed — code review and design intent caught none of them (n=3, 2026-07-27/28, PROME-endorsed promotion):**

1. **Cluster-cadence check v1** inferred a review's subject from whether the cluster NAME appeared in its body — reported four clusters as freshly reviewed because a thorough review *name-checks peers it is not about*. Failure direction: **SILENT** (everything reads FRESH forever; the check goes quiet and looks healthy).
2. **`delivery_claim_vs_git` v1** fired **17 false HIGHs** on its first run (a retired inbox dir + an agent that consumes by DELETING). Failure direction: **NOISY** — annoying, but it got fixed within the hour *because* it fired.
3. **`memory_index_check` v1** flagged `README` as an unindexed memory. Fixed **by construction** (require the canonical slug shape) rather than a denylist that breaks on the next template. Failure direction: noisy, cheap.

**Why:** a guard encodes assumptions about the artifact it watches (naming conventions, consumption patterns, what "about" means), and those assumptions have never been exercised until the guard runs against real data. The guarded system's defects are known; the guard's own defects are brand new.

**How to apply:** before shipping any check/guard/tripwire, (a) run it against a known-GOOD case AND a known-BAD case — synthetic is fine; (b) ask *which direction does this fail when its assumption breaks?* — a silent-failure design (false all-clear) must be rebuilt to fail loud or fail visible, because a wrong guard that reports healthy is strictly worse than no guard: it retires the vigilance that would otherwise exist. (c) Prefer fixes **by construction** (make the document declare its subject; require the slug shape) over enumerated exceptions, which rot. Companion to [[finding_standing_guard_is_a_false_negative_risk]] (a *correct* guard can still wave away the real event) and [[finding_single_witness_guard_deletes_real_data]]; distinct from both — this is about the guard's OWN v1 defects and their failure direction.
