---
name: finding_ranked_head_sample_is_not_the_population
description: Sampling the top of a list ranked on a variable correlated with the outcome gives a rate that cannot be extrapolated — it is a claim about the head, not the population.
metadata:
  type: feedback
---

An audit spot-checked the **5 oldest** retirement candidates and reported *"5 of 5 UNREFERENCED."* Accurate about those five. A full check of all **33** found **19 REFERENCED (58%)** — the opposite conclusion. Acting on the extrapolation would have retired 19 files that live surfaces cite.

**Why it fails structurally:** the candidates were ranked by **age**, and age **correlates with the outcome** — old files are old precisely because nothing kept pointing at them. So sampling the head systematically over-estimates the unreferenced share. The sample wasn't wrong; the *frame* was.

Same family as computing a base rate on whatever window a default fetch returns: **a rate off a ranked head is a claim about the head; a rate off a window is a claim about the window.** Both are sampling frames masquerading as populations.

**A sibling frame, same family:** a cohort assembled for **question A** is a biased sample for **question B** — a coefficient can clear significance at n=14 and vanish at n=26. Full case and the fix (extend the sample once) → [[finding_extend_the_sample_before_publishing_a_coefficient]].

**How to apply:**
- When a sample is drawn by **ranking on a variable plausibly correlated with the outcome**, the sample rate is not the population rate. **Either check all of it, or state the frame in the sentence** ("of the 5 oldest…", "over 2025-02→2026-08…").
- Cheapest fix is usually to just check all of it — 33 files took one scripted pass.
- Watch for this in audit findings that *extrapolate from a spot-check*: the spot-check can be correct and the generalization still wrong.
- Related: [[finding_comprehensive_grep_over_sampling]] · [[finding_magnitude_ranked_discovery_blind_to_deep_slow]] · [[finding_base_rate_the_instrument_before_its_event_table]] · [[finding_verification_zero_is_ambiguous]].
