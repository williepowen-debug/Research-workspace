---
name: verify-recommended-fix-not-just-finding
description: "a verified audit/review finding often ships with an UNVERIFIED fix — the fix can contradict authoritative rules; verify the recommended fix against ground truth before applying, not just the finding."
metadata:
  node_type: memory
  type: finding
---
A finding can be correct while its recommended FIX is wrong. An audit/reviewer verifies the *problem* against ground truth but rarely re-verifies that its *suggested remedy* is consistent with the authoritative rules.

**2026-07-01, CLOSEOUT audit W7:** the reviewer correctly found a real self-contradiction (`HEARTBEAT.md` was treated as a PROME auto-update in one table but Will-gated in another) — the finding was CONFIRMED. But its recommended fix was "make HEARTBEAT a PROME auto-commit," which **contradicts root `CLAUDE.md`** (HEARTBEAT commits are explicitly Will-gated as a shared doc). Applying that suggested fix would have silently expanded PROME's autonomy against governance. I resolved it the opposite (conservative) way — keep Will-gated, fix the *other* table instead — and flagged the deviation to Will.

**Why:** trusting a verified finding's fix by association is a real failure mode — the credibility of the diagnosis launders the remedy. Fixes that *expand* permissions/autonomy or relax a gate are the highest-risk to rubber-stamp.

**How to apply:** for each accepted finding, verify the RECOMMENDED FIX separately against the authoritative source (governance doc, spec, root rules) before implementing — especially any fix that grants new autonomy, widens scope, or relaxes a gate. Prefer the resolution that aligns to the stricter existing rule; a fix that would expand autonomy needs explicit Will approval, not an audit's say-so. Sibling of [[finding_verify_runtime_context_before_tool_broken]] (verify the *claim*) — this is verify the *remedy*.
