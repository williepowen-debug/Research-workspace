---
name: mechanize-the-cap-not-the-ritual
description: "Any closeout-deferrable limit (doc-length cap, state-file freshness, registry lag, spec-version pointer) wants an automated check that self-alarms at BOOT — not a remembered ritual. A run of light closeouts skips exactly the ritual, so the debt accumulates silently and only the DATA layer, which was mechanized, stays healthy."
metadata: 
  node_type: memory
  type: finding
  originSessionId: d9120b76-6f02-48ad-a7c4-5a82302951e8
  modified: 2026-08-10T22:15:33.891Z
---

Two instances, same shape, one agent.

**(a) Summary-doc caps rotted invisibly.** Two weeks of Tier-1 (light) closeouts left WALTER's `STATUS.md` at **12 stacked leads / 100KB** against its own 5-lead cap, NETWORK AWARENESS **5 days stale**, and **16 registry-lag rows**. None of it self-alarmed — because only the **DATA** layer was mechanized (BOARD reconcile, version drift, log reconcile), not the **SUMMARY-doc** layer. The fix that actually held was not "remember to do Tier-2": it was adding a `status_spine_overflow` check to the boot doctor so the cap alarms itself (LOW at 6-8 leads, MED at 9+).

**(b) The cobbler's-children gap.** A 6-agent self-audit found `CLAUDE.md` four spec-versions stale (BOARD_CONSUMPTION v0.2 in the doc vs v0.6 on disk), a 530KB unreadable BOARD INDEX, and push-state wrong in three documents — **none watched by the doctor**, whose checks covered the data layer but not the agent's own instruction/summary docs. Same-session fix: **+4 doctor checks** (`claude_md_version_drift`, `log_reconcile`, `cushing_capability`, `staleness_sweep_overdue`), so the drift now self-alarms at boot.

**Why:** a deferrable maintenance step is, by construction, the thing a busy session defers. The discipline that says "run the full closeout every 3rd light one" is enforced by the same attention that is already saturated — so it fails precisely when load is high, which is when the state matters most. **Self-correcting beats periodically-audited.** A periodic audit also has a hidden cost: it finds the problem *once*, then the same class re-accumulates (registry_lag was fully cleared and back to 11 MEDs in **5 days**, because active agents commit daily).

**(c) The strongest version: WRITING THE LESSON IS ITSELF A RITUAL, AND IT FAILS THE SAME WAY.** *(BRENT, 2026-08-10, n=3 on one defect.)* After Will retired a gated position arm on 8/7, BRENT ran a verification grep, reported clean, and PROME found three surfaces still carrying the arm as pending. BRENT then wrote the corrective lesson explicitly — *"when a spec's STATUS changes, grep the PENDING/FORWARD vocabulary (`due`, `by <date>`, `runs to`, `awaiting`), not just the LIVE vocabulary."* **Three days later a fourth residue surfaced: the arm's own `Status:` field still read `ARMED … expires 8/13`** — i.e. LIVE vocabulary, on the canonical trade surface, in the single most load-bearing place for it to be wrong. **The lesson had been written, re-read at boot, and reproduced anyway.**

**And a mechanized guard DID exist and passed clean three times** — a boot step requiring every `PENDING`/`⏳` row to be resolved-or-reaffirmed. **It reads EXECUTION LOG rows only**, so it never looked at section status fields. ⇒ **a guard's SCOPE is the thing to audit, not its output; a clean pass certifies where it looked, not that you are safe** ([[finding_verification_zero_is_ambiguous]]).

**⇒ THE RULE THIS ADDS: count your own repeats. If you have written the same corrective lesson N times and reproduced the defect N times, stop rewriting it — the lesson is not the fix.** Writing a lesson is enforced by exactly the attention that was already saturated when the defect happened, so **prose scales worse than a check**. Convert it into (i) a new guard, or (ii) a **scope extension of the guard that already passed clean over the wrong thing** — the second is usually cheaper and is the one people miss, because a passing check does not look like a gap.

**How to apply:** when you catch a stale doc, a breached cap, or a drifted pointer, **do not just fix it** — ask whether a check could have caught it, and add the check in the same session. Extending the doctor is the durable fix; re-auditing is not. **If a check already runs and did not catch it, the answer is almost always to widen its SCOPE, not to add a second check** (retirement-ratchet friendly: extending supersedes nothing and costs no new attention). Corollary for anything version-pointed: bump the spec → sweep the pointer doc **in the same commit** → let the guard confirm.

Related: [[finding_doc_mirror_consistency_check]] · [[finding_status_spine_staleness_under_appended_top]] · [[finding_passive_surface_rot_push_not_dashboard]] · [[finding_governance_doc_stale_default_drift]] · [[finding_verify_roster_by_commit_activity]] · [[finding_seeded_selfsweep_secondary_surface_rot]]
