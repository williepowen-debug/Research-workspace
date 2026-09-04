---
name: finding_a_ruling_governs_the_next_write_not_the_existing_state
description: "Ruling a convention changes what gets written NEXT and touches nothing already on disk — measured same-day: a fleet-wide ban was true of 64% of its author's own surfaces hours after he wrote it. Pair every new convention with a retroactive sweep, or the stock of violations outlives the rule."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: caf3458a-6c5d-41b6-8f8e-67f8a322e6a1
  modified: 2026-08-27T18:00:00.000Z
symptoms: "ruled but not swept; the rule exists so the area reads handled; doc-only condition executed while the live instance it describes sits in the old state; lapsed-but-unrevoked grant; compliance rate unknown at ruling time"
---

A newly-ruled convention acts on **future writes only**. Nothing in a normal fleet kit scans existing state for violations of a rule at the moment that rule is made. So the **flow** gets cleaner while the **stock** of violations sits untouched — and because the rule now exists, everyone reads the area as handled.

**Measured, 2026-08-12, all in one evening:**
- BRENT ruled the crude instrument-basis canon, wrote it, and packeted seven desks. Its own audit hours later measured **54 of 150 crude figures on its live surfaces still unlabeled — the ban was true of 64% of them, not 100%.**
- Inside the very packet that banned quoting a live bar as a settle, BRENT **committed the 4th instance of that class in six days.** Maximum rule; no prevention.
- PROME corrected a claim in `HEARTBEAT` §3 and left the identical retired claim live in §5 and the thresholds list — the same shape as the audit finding it was relaying at that moment.
- Two ledger columns kept storing `0` for events their unit could not express, months after the scope that admitted those events was written into the header.

**Why the failure is structural, not carelessness** (BRENT's own words, and they generalize): *"A ruling changes what I write next. It does not touch what is already written, and nothing in my kit scans for it."*

**Why:** rules act on **attention**, which is the resource already exhausted at the moment of the error. That makes a written rule the *weakest* prevention available — weaker than making the error impossible to express, weaker than failing loudly at the moment of the act, weaker than automatic detection soon after. Fleets default to writing rules because rules are the cheapest thing to write, not because they work best.

**How to apply:**
1. **Pair every newly-ruled convention with a retroactive sweep of existing state, in the same session.** Ruling without sweeping leaves a violation stock that now looks governed. If the sweep can't run that session, say what the current compliance rate is — "ruled, and currently true of 64%" is honest; "ruled" alone is not.
2. **Prefer structure over rule.** If a value must carry its unit, make the capture function return the unit so a bare value is unwritable. That converts an attention problem into an impossibility.
3. **Find your own violations mechanically, not by re-reading.** Grep the strings you replaced and classify each hit as retirement-context vs live-claim; re-derive numbers from primaries rather than re-reading them. Re-reading does not catch what you just wrote — you skim your own text.
4. **Never rely on the erring party's attention.** Every real catch in the evening above was external. Self-discipline is not a mechanism.

**n+1, 2026-08-27, and the stakes were a live AUTHORITY GRANT, not prose:** the KERNEL C8 review's condition N3 ruled that activation closure is "an act, not a clock-lapse — a lapsed-but-unrevoked activation is a valid live grant sitting unattended." The condition was executed **doc-only** (runbook step 9 re-worded, Will-worded, pushed) while **the one live activation the finding described — `LIVE-2026-0001`, `revoked_at: null` — sat as a valid unattended grant for ~55 minutes**, and was closed 8 minutes before window-end only because the custodian's read-back happened to run inside the window (revocation `e0e7f859b`-adjacent commit, refusal then proven at preflight: `LIVE_WINDOW_REFUSED`). The reviewer wrote the rule about the exact instance and did not sweep the instance; the custodian who owned the instance was dark. Same structure as 8/12, sharper consequence class: for **grants and permissions**, the un-swept stock isn't stale prose — it's standing authority. Sweep order for authority objects: revoke the live instance FIRST, re-word the doc second.

Related: [[finding_banner_is_a_warning_not_a_fix]] (a banner buys time on a *known* stale doc; this is the unknown stock behind a *new* rule) · [[finding_verification_correction_downstream_propagation]] · [[finding_retired_threshold_has_no_publisher]] · [[finding_dated_carry_item_has_no_expiry_check]] · [[finding_anti_ratchet_governs_state_not_prose]].

**n+4 in ONE session (OTTO 2026-08-27)** — and the sharpest instance shows the residue can be an *example* rather than a rule. **(1)** Root carve-out ① (2026-07-23) created an exception to "never commit outside your dir"; OTTO's local `CLAUDE.md` carried a **parenthetical EXAMPLE of the old general rule** written 2026-04-15, which nothing swept. It then read as an independent never-commit policy for three months and **held four signal packets undelivered** before Will had to rule it. **When a rule gains an exception, grep for its worked examples — they outlive it wearing its authority.** **(2)** A block-1 session write-back left three summary surfaces asserting a state that later blocks had cleared. **(3)** A coordinator amended a packet and the recipient's note still asserted the closed gap. **(4)** A reconciled metric definition left the whole ledger history mixed-basis until a backfill re-ran it. **Pair every ruling with a retroactive sweep, and include derived examples in the sweep — not just restatements of the rule.**

**n+1 (DAEDALUS, 2026-09-04 — a closeout step keyed on a file the ruling never asked anyone to create):** root closeout step 1c-bis (`ledger_staleness.py --nudge <NAME>`) reads each desk's `workbook/LEDGER_GLOB`; `ls AGENTS/*/workbook/LEDGER_GLOB` = **7 of 43 desks**. The step shipped as a rule about the NEXT closeout and nudges on nothing for 36 desks — every one of them runs the step, gets a clean line, and is certified. Found on the VIOLET profile refresh (reader C: "no LEDGER_GLOB ⇒ 1c-bis nudges on nothing"). Pair the ruling with the census; proposed as a wiring-sweep #2 leg.
