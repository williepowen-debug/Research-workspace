---
name: finding_dormant_instrument_is_a_query_plus_unexercised_reading_rules
description: "A dormant instrument is not one artifact — it is a QUERY plus the READING RULES beside it (lag figures, threshold bases, denominators, settle windows), and they rot at DIFFERENT rates. The query is exercised on every run and self-tests; a figure written next to it is never exercised and inherits the query's credibility untested. Auditing dormant instruments by 'does it still run?' certifies exactly HALF of them — and the un-exercised half fails toward a FAKE finding in the quiet direction. STUE ES-02 2026-09-05."
metadata: 
  node_type: memory
  symptoms: "the query still runs so the instrument is fine · does it still run · revived a dormant instrument · re-pulled after weeks dark · the lag rule was wrong · manufactured an 85% collapse that doesn't exist · reading rule rotted while the query didn't · settle-window / publication-lag / denominator drifted"
  type: feedback
  originSessionId: 0240dacf-4098-4179-8f47-b9fbb15e30bf
  modified: 2026-09-05T14:48:44.172Z
---

**A registered instrument you haven't run in weeks is TWO things, not one: the QUERY (the API call / fetch / grep) and the READING RULES around it (the publication-lag figure, the threshold basis, the denominator, the settle-window rule). They rot at different rates.** The query is exercised on every single run, so it self-tests — it either returns valid data or it visibly breaks (404, auth, drift). A figure written *beside* the query is never exercised: it just sits there, and **it inherits the query's credibility by proximity without ever being tested.**

**Concrete (STUE ES-02, 2026-09-05, first cold re-run after 23 days dark):** the CFPB query woke perfectly — valid JSON first try, no auth, no drift, historical months reproducible. But the reading rule beside it — a documented *"~5–6 day publication lag"* — had rotted: the real settled boundary is a CLIFF ~14 days back, not a taper. **A reader applying the documented rule would have read an 85% "collapse" that does not exist.** The query passing certified nothing about the rule.

**Why this is the dangerous shape:** the un-exercised half fails toward a **fake finding in the QUIET direction** — a manufactured collapse/all-clear, which is exactly the direction that gets banked without challenge (`[[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]]`). And it defeats the obvious audit: **"does the instrument still run?" certifies exactly half of a dormant instrument.** The lag figure is a `[[finding_dated_carry_item_has_no_expiry_check]]` — a string that reading does not evaluate; running the query IS using it, so it stays honest, while the figure beside it was never used.

**How to apply:**
- When reviving or auditing ANY dormant instrument, test the QUERY and the READING RULES as **separate artifacts**. "It runs" is not "it reads right."
- For settle/publication windows specifically: **never subtract a fixed N days — print the dailies, find the step-change (the cliff), discard everything after it.** A fixed lag manufactures a false collapse the moment the real boundary moves.
- Fleet audit implication: a dormant-instrument sweep keyed on runnability alone (`does it 404?`) passes the exact half that fails silently. The reading-rules need their own exercise. `[[finding_adoption_is_not_validation]]` — consumed + confident + never-exercised = nobody tested it.
