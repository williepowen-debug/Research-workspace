---
name: finding_level_without_a_reference_has_two_failure_modes
description: "A level with no reference carries no information — and the failure has two modes. Saying nothing is a gap; attaching an adjective is a wrong finding."
metadata:
  node_type: memory
  type: feedback
---

**A measured level without its reference carries no information at all.** The trap is that it *looks* like information — it is a real number from a real primary, correctly pulled.

**There are two failure modes, and the talkative one is worse.**

AEOLUS pulled first live reads for two rivers on 2026-08-13, neither with a baseline:

- **Danube** — had a level, no reference, **said nothing.** Budapest 24 cm, and no way to tell if that was high or low. *A gap.*
- **Paraná** — had a level, no reference, **said something.** Called Rosario 3.02 m **"mid-range."** *A wrong finding.*

**Both references existed. Both reversed the read.** The Danube authority publishes per-station record lows (`LKV`) *and its own below/above flag* — **13 consecutive stations were below their all-time records.** The Paraná's own 366-day history put 3.02 m at the **99th percentile**, one centimetre off the trailing-year maximum — near the *top* of its range, not the middle.

⚠️ **Why "mid-range" happened, because the mechanism generalises:** the only threshold that source published was a **flood** alert at 5.00 m. 3.02 looked unremarkable beside it. **The one reference in view pointed the opposite direction from the question being asked**, and got used anyway — unconsciously, and it felt like description rather than inference.

**Rules:**
1. **Never attach a magnitude adjective — low, high, normal, mid-range, elevated — to a level until you hold its distribution or its published extreme.** The adjective *is* the claim.
2. **If the only reference in view points the opposite direction from your question, it is not a reference — it is a distractor.**
3. **Prefer deriving the reference from the station's own history over hunting for a published one.** Usually faster, always reproducible, and it yields percentiles a published threshold cannot.
4. **State the base's span.** A trailing-year percentile is a rank *within* that year — the Paraná's benign year hides a 2021 crisis that went far lower.

Related: [[finding_registry_names_a_concept_tool_resolves_an_instrument]] · [[finding_base_rate_the_instrument_before_its_event_table]] · [[finding_number_carries_threshold_unit_source]]
