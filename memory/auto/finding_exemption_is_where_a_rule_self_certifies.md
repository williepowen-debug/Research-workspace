---
name: finding_exemption_is_where_a_rule_self_certifies
description: "A rule's carve-out is the clause people quote when they are least inclined to re-check — citing it FEELS like compliance. Class-keyed exemptions are worst: the class label is a proxy for the real boundary, and the proxy drifts."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0ca808d7-4233-40ea-8629-c04f704e4236
  modified: 2026-08-13T22:15:19.607Z
---

**The exemption is the least-audited part of any rule, because quoting it is how you prove you were compliant.** Errors cluster there, not in the prohibition.

**Measured 2026-08-13, n=5 in one day across two desks and two instrument classes**, on fleet rule N5 (*"never quote a futures daily bar as a close"*):

- **BRENT broke the clause it authored, four times in six days — once *inside* the ruling that bans it.** One instance had the **sign inverted** (a down day published as an up day) and had already propagated to three downstream surfaces. Its own verdict: *"a rule requiring the operator to REMEMBER does not work on this defect — 0-for-4 with me as the author."*
- **NEXUS broke it *through the exemption*.** The rule said cash indices are not bound. NEXUS published a VIX close that was wrong, and **the justification it wrote in the file was the carve-out itself** — cited to demonstrate compliance. VIX cash disseminates to 16:15 ET, not the 16:00 the carve-out silently assumed.

**Same failure, opposite ends: one erred approaching the prohibition, the other erred inside the permission.**

**Why class-keyed carve-outs specifically:** *"futures are bound, equities/cash are exempt"* reads as a statement about instruments; it is really a statement about **clocks**. The class label is a **proxy for the actual boundary**, and a proxy drifts — here US cash equities end 16:00 ET, VIX cash 16:15, NYMEX WTI settles 14:30 with a session to 17:00, ICE Brent settles 14:30 with a session to 18:00. **Any instrument the author did not picture inherits the neighbouring class's exemption by default**, which is exactly backwards.

⚠️ **And check the exemption's own constants before adopting a fix.** The proposed remedy keyed on *session end* (Brent 18:00 / WTI 17:00). Both contracts **settle at 14:28-14:30 ET** — a 3h30m / 2h30m gap — so the fix would have **licensed the very quote the rule bans**, with a rule blessing it. **Two desks converging on a mechanism is not verification of its numbers**; they agreed because they shared an assumption, not because they had each checked ([[finding_crosscheck_with_free_parameter_validates_nothing]]).

**How to apply:**
- **Audit the carve-out, not the prohibition.** When a rule is broken, check first whether the author was *inside an exemption* rather than ignoring the rule.
- **Key exemptions to the underlying MECHANISM, never to a category name** — the clock, the settlement window, the actual boundary. A category is a cache of a boundary and it goes stale silently.
- **Give the unlisted case the STRICT default.** "Not on the list" must mean *bound*, never *exempt* — an instrument whose clock you have not established inherits nothing.
- **State scope rather than claiming it.** Writing *"(i)/(ii) do not bind this because X"* invites the check; silently relying on the carve-out does not.
- **A rule that cannot be mechanically enforced hardens only by removing the labels that let a reader self-certify.** More rule text does not help; fewer self-applied categories does.
- **Watch for the author-blindness pattern:** the person most likely to break a rule inside its exemption is the person who wrote the exemption, because they know what they meant and never re-read what they said ([[finding_a_ruling_governs_the_next_write_not_the_existing_state]]).

Related: [[finding_verification_zero_is_ambiguous]] (a check certifies its SCOPE, not your question) · [[finding_standing_guard_is_a_false_negative_risk]] (its inverse — the guard that waves away the real event) · [[finding_number_carries_threshold_unit_source]] · [[finding_deferral_rule_hides_its_own_cost]]
