---
name: finding_premise_residue_survives_date_fix
description: "A date-only drift check passes rows whose DATE is correct but whose PREMISE is dead — when an event re-dates or dies, grep the OLD PREMISE PHRASES across live surfaces, not just the old date. Date-column-clean ≠ premise-clean."
metadata:
  type: feedback
---

When an event re-dates or its premise dies (a motion granted early, a trial moved, a mechanism superseded), fixing the date rows is not enough: **prose that narrates the dead premise survives anywhere the old story was told**, and every date-anchored consistency check passes it. OTTO 7/25: after re-dating the Tricolor trial Oct-19→Jan-2027, a STATUS row still read "Castel rules on Chu's motion to push trial past Oct 19" — its own canonical-vs-mirror check compares event *sets* (dates + IDs), PROME's firetime gate compares *dates vs docket rows*; both passed a row whose date was right and whose premise was dead.

**Why:** the residue class lives in the prose, not the date column — and all the mechanized checks read the date column. PROME's catch of OTTO's residue was luck (a human-style read), not the gate working.

**How to apply:** on any re-date or premise-supersession, grep the **old premise phrases** (the event's distinctive nouns/claims — "past Oct 19", "rules on the motion", the old counterparty framing) across live surfaces, exactly as [[finding_state_token_sweep_all_surfaces]] does for state tokens. Delivered/outbox records stay as-written. The DOCKET maintenance rule carries this; a date-drift flag clearing is necessary, never sufficient. Cf [[finding_redated_falsifier_inherits_premise]] (the analytical version of the same trap).
