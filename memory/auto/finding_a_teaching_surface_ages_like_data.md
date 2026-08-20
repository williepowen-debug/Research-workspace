---
name: finding_a_teaching_surface_ages_like_data
description: A lesson, runbook or charter that embeds figures rots invisibly — its authority as canon is exactly what stops anyone auditing it for freshness, and the stale numbers inherit the rule's credibility.
metadata:
  type: feedback
---

`LESSONS.md` taught, as the corrective reality behind a hard-won rule: *"WAL's NDFI is $6.5B — 68% mortgage warehouse, ex-mortgage only $4.3B."* Measured at the FFIEC primary two quarters later: **$15.81B**, ex-mortgage **$4.92B**, plus **$122.5M of NDFI nonaccrual** that did not exist as a concept when the lesson was written.

**The rule was vindicated** — the mortgage-warehouse share came back **68.9%**, almost exactly. **The scale had quadrupled unflagged**, inside the document whose whole job is to be trusted.

**Why this rots where a dashboard does not, and it is an inversion:** a dashboard is *expected* to be current, so people check it — staleness there is a visible defect. A lesson, charter, runbook or CLAUDE.md is *expected to be timeless*, so nobody audits it — and the figures embedded in it **inherit the rule's authority**. The more durable the surrounding wisdom, the more credible the stale number sitting inside it. Freshness tooling doesn't help: staleness checks point at ledgers and dashboards, never at canon.

I found this staleness myself, packeted the live figures to the owning desk within the hour, and **still nearly left my own teaching surface carrying the old ones** — the same-dir blind spot (`consumer_check --self`), which is where most of this class lives.

**How to apply:**
- **Split every canon document into a RULE half and a FIGURE half.** The rule is permanent. **The figure half is a dated snapshot and must be labelled as one** — or stripped to the mechanism, which is usually better.
- **A figure with no date inside a lesson is the defect**, independent of whether it is currently right.
- **When you correct a number for someone else, immediately grep your own canon for it.** Publishing a correction outward and leaving it stale inward is the modal version of this.
- **Sweep by surface TYPE, not by staleness signal** — LESSONS, CLAUDE.md/charters, script-header runbooks, registry NOTES. None of them trip a ledger check. *(Concrete open instance: a screen runbook I own embeds "item-9 share runs 5.5%→65.8%" and "step detector fires 17/154 = 11.0%" — both will age exactly this way.)*
- **Don't delete the mistake half.** The error that earned the lesson is history and should stand; only the *reality* half is a snapshot.
- Related: [[finding_dated_carry_item_has_no_expiry_check]] (assertions don't self-evaluate) · [[finding_plausible_stale_value_evades_review]] (the plausibility version; this is the *authority* version) · [[finding_header_edit_is_the_edit_most_mistaken_for_maintenance]] · [[finding_claim_outlives_its_discredited_instrument]].
