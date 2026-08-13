---
name: finding-skill-regated-not-removed
description: "A harness skill absent from the model-visible list may be REGATED to user-invocation, not removed — /deep-research v2.1.219. Check the platform changelog before declaring a capability gone or amending specs around its absence; the fix can be one line: the USER types the slash command."
metadata: 
  node_type: memory
  type: finding
  originSessionId: 8d29eb7a-a690-4165-acd1-10f1c645b638
  modified: 2026-08-13T01:26:40.377Z
---

**A capability missing from the model's view is not necessarily missing from the platform.** Claude Code skills exist in (at least) two invocation modes: model-invocable (listed in the session's available-skills, callable via the Skill tool) and user-invocable (typed by the operator as `/<name>`). A harness update can move a skill from one mode to the other, and from inside a session that transition is indistinguishable from removal.

**The instance (2026-07-28):** `/deep-research` — DEWEY's named primary research engine — vanished from every session's skills list on the box. No local definition existed anywhere (repo `.claude/skills`, user skills, plugins, workflows), so it was harness-provided and nothing in git could restore it. DEWEY correctly fell back to hand-orchestrated subagent legs and flagged a spec amendment. The changelog answered it: **v2.1.219 "Changed `/deep-research` to start only when invoked manually; Claude no longer launches it on its own."** Regated, not removed. The whole fix: Will types `/deep-research <prompt>` in the agent's window.

**Why:** agents reason from their available-skills list as if it were the platform's capability inventory. It is only the *model-invocable* slice. Spec amendments, tooling rebuilds, or "the platform lost X" escalations written against that slice can be wrong — and expensive — when the capability is one keystroke away on the user's side.

**How to apply:**
- A previously-working harness capability disappears → **check the platform changelog FIRST** (`raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md`), before amending specs, building replacements, or declaring outage. Distinguish: removed / renamed / regated (model→user invocation) / plan-or-model-gated.
- Before relying on the manual path, **live-test it once** (user types the command with a trivial prompt) — the changelog says what changed, not that your version behaves as described.
- Generalizes: any agent spec that names a harness feature as a dependency should record *which invocation mode* it assumes, because the mode is a platform decision that can change under you.

**RECURRENCE — n=2, same agent, same skill (2026-08-12, DEWEY C3).** DEWEY hit the identical absence at engine-selection and again told Will *"the skill is not installed / my documented fan-out engine is gone,"* then offered Will a set of options framed on that premise. **The memory above already existed, already named this exact skill, and already prescribed the fix.** Will ruled primary-pull-only — a decision that stands on its merits — but it was made against a wrong premise, with the fan-out genuinely one keystroke away. Caught only at closeout, incidentally, while reading a prior handoff in the delivery lane for formatting.

**What the recurrence teaches, beyond the original lesson:** the failure was *not* missing knowledge — it was **not recalling a memory at the moment of use.** The trigger ("a capability I expect is absent from my list") fires at a moment that feels like a *discovery*, and discovery-feeling moments are exactly when a stored correction is least likely to be consulted. So the operational fix is a **hard precondition, not a reminder**: *before telling anyone a capability is gone, or changing a plan because of its absence, grep your own memory and prior deliverables for that capability's name.* One `grep` over `memory/` + your own outbox/handoff archive. The claim "X is gone" is a **state claim about the platform** and inherits [[feedback_verify_state_before_propagating]] — it is not exempt because it is about tooling rather than data.

Related: [[finding_verify_runtime_context_before_tool_broken]] · [[feedback_subagent_web_tools_not_autoloaded]] · [[finding_unversioned_local_secret_fails_silently]] (sibling class: capability failures whose cause is one layer away from where you'd debug) · [[feedback_verify_state_before_propagating]] · [[finding_dated_carry_item_has_no_expiry_check]] (sibling: a stored correction that is never re-evaluated at the moment it applies).
