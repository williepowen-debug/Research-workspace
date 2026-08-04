---
name: finding_live_claim_in_a_closed_container_is_invisible
description: "A forward/unresolved claim parked inside an artifact marked DONE (a confirmed row, a resolved ticket, a closed section) inherits the container's status and stops being read as open — every open-items sweep keys on the container, so the claim can rot for months while sitting in plain sight and passing every audit"
metadata:
  type: finding
---

Sweeps for open work — boot scans, closeout checks, "what do we still owe?" passes — key on the **container's** status, not on each claim inside it. So **a live claim parked in a container marked DONE is invisible by construction.** It is not hidden; it is in plain sight, in a file that is read constantly, and it still gets skipped, because the thing being read is the header.

**NEXUS, 2026-08-03.** `CONFIRMED.md` is a trophy case — every row asserts *this happened*, and rows carry a confidence like 99%. Row **C-05** described three legs, two fired and one **forward**: *"Wave 1 exhaustion fired. Wave 2 peak Apr 26. CA/NY Aug."*

That third leg sat unresolved from **March to August**. It survived:
- every boot's open-items scan (the row's status is *confirmed*),
- two separate audit passes that flagged it in prose and still did not resolve it,
- and its own arrival **in-window**, which changed nothing because nothing was watching.

When it was finally checked, the leg turned out to be **unresolvable from birth** — it named no instrument, no threshold and no magnitude, so **no print could ever have fired it in either direction** (`[[finding_resolvability_defect_is_status_not_confidence]]` — that is a STATUS change to STUCK, not a confidence cut). **Two independent defects, five months, both hidden by the same thing: the row's header said confirmed.**

**The rule.** A container whose status means *finished* must contain only finished things.
- **Fired legs stay; forward legs move out** — to the predictions ledger / open-items tracker — with an instrument, a threshold and a date. The closed row **links** to the open item rather than holding it.
- **When a legacy row already mixes both**, do not rely on prose to flag it. Give the forward leg **its own status cell** (`STUCK`, `RE-SPEC'd`, a resolve date) so that a machine or a skim keys on the leg, not the row, and **state explicitly which legs the headline number applies to.**

**Generalizes past state files.** Same shape wherever status is inherited downward: an open question inside a closed ticket · a TODO inside a merged PR description · an unverified figure inside a "verified" summary · a pending item in a section headed RESOLVED · a caveat inside an artifact stamped APPROVED. In each case the audit reads the container.

**The tell:** you are writing a sentence in the future or conditional tense — *"expected," "should hit," "by August," "if X then"* — into an artifact whose whole purpose is to record the past. If the tense of the claim disagrees with the tense of the container, the claim is in the wrong file.

Related: [[finding_canonical_surfaces_stale_inbox_carries_live_state]] (the live fact riding a surface nobody sweeps) · [[finding_resolvability_defect_is_status_not_confidence]] (what this one turned out to be once read) · [[finding_count_what_published_before_reading_the_verdict]] ("no reading" and "no adverse reading" recording identically — the same invisibility one level out) · [[finding_status_spine_staleness_under_appended_top]] · [[finding_premise_residue_survives_date_fix]].
