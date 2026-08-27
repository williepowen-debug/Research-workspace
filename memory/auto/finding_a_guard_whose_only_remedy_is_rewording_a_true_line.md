---
name: finding_a_guard_whose_only_remedy_is_rewording_a_true_line
description: "A guard that false-positives on an HONEST disclosure has only one remedy available to its operator — reword a true line — so it converts directly into pressure to make the record less candid; when a check fires, ask what the cheapest way to silence it is before fixing anything"
metadata: 
  node_type: memory
  symptoms: "checker flags my own honest caveat; rc=1 on a line I know is true; the check agrees with my number but still reports CLAIM FALSE; tempted to reword a disclosure to get a clean pass; negation-blind regex; 'NOT drained' matches 'drained'; guard punishes candour; I stopped writing the caveat because the linter complains"
  type: feedback
  originSessionId: 16ea61fe-426e-4d42-81fe-68ebe7403cd2
  modified: 2026-08-27T14:03:10.948Z
---

A guard fires. The finding is a false positive. **Before fixing anything, ask what the CHEAPEST way to make it stop is** — because that is what the operator will actually do, under time pressure, every time.

When the false positive lands on a **stale or wrong** line, the cheapest remedy is to fix the line, and the guard has done its job even when it misfires. **When it lands on a TRUE line — especially a deliberately candid one — the cheapest remedy is to REWORD the true line.** The guard then converts, silently and permanently, into pressure to make the record less honest. Nobody decides to do this; it is just the path of least resistance at closeout, and it leaves no trace, because the reworded line still reads fine.

**Measured instance (BOND, 2026-08-27).** A stale-assertion checker's FILE-STATE rule matched the claim `inbox … drained` with a negation-blind regex. The session had deliberately NOT drained a 7-item inbox and had written so explicitly: *"the general inbox/ was NOT drained — 7 items, deliberately."* The checker reported **CLAIM FALSE** — while its own diagnostic printed *"inbox/ has 7 top-level file(s) unprocessed."* **7 == 7. The tool and the claim agreed exactly, and it still fired.**

The available remedies were: (a) drain the inbox — not possible, it was a separate task with a hard clock elsewhere; (b) **delete or soften the honest sentence** — one edit, instant clean pass, and the resulting file would have implied a clean inbox; (c) fix the checker. **Only (b) is cheap.** A tool built to catch a desk asserting a false file-state was, on this line, rewarding a desk for asserting one.

**Two consequences, and the second is the worse one.**
1. The specific line is at risk of being laundered.
2. **A checker that penalises candour teaches its operator to discount `rc=1` in general.** Every subsequent real finding from that tool arrives already devalued. A false positive on an honest line does not cost one defect — it costs the tool's standing.

**What to do**
- **When a guard fires on something you know is true, do not reword first.** Confirm the guard is wrong (here: compare the claim against the tool's own printed measurement), then fix the guard.
- **Fix it narrowly and prefer a MISS to a false positive** in this specific class. A missed false claim is one defect; a false positive on a candid line corrupts trust in every other finding.
- **Fixture BOTH directions.** The negation guard added here shipped with four fixtures: two that must NOT fire (`"was NOT drained"`, `"was never drained"`) and **two that must STILL fire** (`"inbox drained"`, `"inbox: 0"`) — because the obvious way to kill a false positive is to blind the rule to the defect it exists to catch. See [[finding_test_the_guard_not_just_the_guarded]].
- **Design check, applicable before a guard ships:** ask whether any TRUE sentence could match the pattern. Claim-matching patterns are usually written against the affirmative form and inherit blindness to `not / never / no longer / isn't` for free.

**Generalises past regexes.** Any acceptance rule — a lint, a CI gate, a review checklist, a required field, a status token — where the least-effort path to a green result is *"state something less true"* rather than *"make something more true"* has this shape. Related but distinct: [[finding_noise_filter_erases_signal_class]] is about widening a filter deleting the signal class; this is about the DIRECTION in which a false positive's remedy pushes the record. Also [[finding_guard_correctness_and_wiring_are_independent]] and [[finding_a_correction_pass_is_unreviewed_work]].
