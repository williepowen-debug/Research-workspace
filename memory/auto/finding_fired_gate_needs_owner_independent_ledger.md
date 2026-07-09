---
name: fired-gate-needs-owner-independent-ledger
description: "A pre-registered gate whose fire-consequence lives only in the owning agent's files gets orphaned when that agent freezes — register action-gates in the PROME-boot-scanned fire-ledger (PROME/GATES.tsv) the session they're approved."
metadata: 
  node_type: memory
  type: project
  originSessionId: 5ecb4c73-dd97-46e9-a08c-5477d4215fde
---

**Incident (2026-07-09 discovery, 2026-07-02 failure):** VIOLET's KB-VIO-110 registered "any ONE gate fires the same-session tail-hedge packet-build." Both gates (CCC persistence + LIQUID breadth confirm) resolved FIRED the morning of 7/2 — the same morning VIOLET's session froze. The consequence (build VIX-call packet → Will [Approve]) lived only in VIOLET's own KB, so no other agent's boot could see the fired gate. It sat orphaned 7 days until the 7/9 backfill spawn audited the window. Will never saw the proposal he was owed (failure was upstream of his decision; the missed hedge happened to be flat-to-down — cheap lesson).

**Why:** file-based coordination means an agent's own KB is invisible to the rest of the fleet between its sessions. A gate registration is a *promise of future action*; promises stored only with the promisor die with the promisor's session.

**How to apply:** every gate whose FIRE requires an action (packet-build / arm / proposal / route) gets a row in `PROME/GATES.tsv` (the fire-ledger) **the same session it's approved** — PROME boot (BOOT.md step 3) scans it: `FIRED-UNEXECUTED` = blocking; `last_checked` >5d on a LIVE row = refresh/flag. Graded-later predictions stay in agent PREDICTIONS ledgers (don't duplicate). Owners' KBs stay canonical for full gate logic. Related: [[finding_asymmetric_records_need_reconciliation]] (sibling class — diverging records; this one is *invisible* records), [[feedback_deploy_on_trigger_not_calendar]].
