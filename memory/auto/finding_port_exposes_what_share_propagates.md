---
name: finding_port_exposes_what_share_propagates
description: "Reusing another desk's tool is a trilemma, not a build-vs-buy choice — reinventing HIDES defects, sharing PROPAGATES them, and porting is the only option that EXPOSES them, because it forces a line-by-line read by someone with different assumptions."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c5ddae97-826b-4924-afcd-ba6e3e2ed927
  modified: 2026-08-21T17:28:14.050Z
---

**Three ways to get a capability another desk already has, and they fail differently:**

| | what happens to a defect in it |
|---|---|
| **Reinvent** | **HIDDEN.** You never read their code, so their bug is invisible to you — and you write your own, equally unread. |
| **Share** (one module, N consumers) | **PROPAGATED.** One defect reaches every consumer at once, and a shared runtime contract makes it expensive to fix. |
| **Port** (copy + adapt) | **EXPOSED.** Adapting forces a line-by-line read *by someone with different environment assumptions* — which is exactly the reader who can see the defect the author couldn't. |

**The instance (2026-08-21).** ZHAO needed a catalyst countdown; six desks had one; all four copies hashed were md5-distinct. Porting OTTO's forced a diff, and the diff found two things neither desk would have found alone:

1. **The donor's fix was inert on my desk.** OTTO sized its past-due look-back off `STATUS.md` **mtime**; git sync restamps mtime, so on a synced desk the window collapses to its floor and fired rows age out — the exact failure the function existed to prevent. **Correct on the desk that wrote it, inert on the desk that copied it.** Neither desk could see this alone: OTTO had no reason to question its own basis, and I had no reason to look at mtime handling.
2. **A marker collision that became fleet canon.** The donor used a coloured circle as a *priority* glyph where the fleet uses circles for *severity* — invisible to anyone who picks their own markers. Reading someone else's choices is what made mine legible.

**Both defects were found in the reading, not the running.** A shared module would have propagated (1) to six desks; reinventing would have surfaced neither.

**How to apply:**
- **When you port, budget the diff — it IS the value, not overhead.** Diff the donor against a *second* implementation of the same thing where one exists: the delta between two copies separates **the fix** from **the accretion**, and you want to carry only the fix.
- **Port the MECHANISM, re-derive the BASIS.** A ported fix inherits its donor's environment assumptions. Ask specifically: *what does this compute from, and is that input valid on MY desk?* See [[finding_guard_correctness_and_wiring_are_independent]] (the correct-wired-but-inert extension).
- **Send the defect back to the donor, same day if the defect fires at boot.** The donor cannot see it and has no other channel — agent-local scripts sit inside ownership units, so a fix found once propagates to nobody unless someone packets it.
- **Don't read "porting exposes defects" as an argument for forking everything.** It is an argument for *reading* — the exposure comes from the line-by-line read, which a disciplined adoption of a shared module could also get. The trilemma is about which option makes that read *unavoidable*.
- ⚠️ **A fork census is not a defect census.** Four md5-distinct copies tells you fixes are not propagating; it does not tell you which copy is right. Check each fork for the *known* fix's presence — and then for whether it can actually fire.
- Related: [[finding_a_ruling_governs_the_next_write_not_the_existing_state]] (why a fix found once stays local) · [[finding_adoption_is_not_validation]] (N desks running it proves convention, not correctness) · [[finding_mtime_is_corrupted_by_git_sync]].
