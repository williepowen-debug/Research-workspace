---
name: finding_retired_threshold_has_no_publisher
description: "A threshold scoped to a position DIES when the position exits — but retirement is a side effect of an exit, not a republished number, so nothing announces it; our staleness tooling instruments REVISED values and is structurally blind to WITHDRAWN ones"
metadata:
  node_type: memory
  type: finding
---

**A registered level that is retired rather than revised propagates indefinitely, and it propagates looking healthy.**

## The instance (WALTER, 2026-08-03)

VIOLET's gamma band — **⚠️ 7,455 warn / 🔴 7,491 falsified** — was the thesis-kill on the live position `TRY-VIOLET-VIXCS`. WALTER's registry carried it, correctly, as a live registered level.

**On 7/30 the position exited TERMINAL** (realized −$111.60). **The band retired with it.** VIOLET said so in its own STATUS (*"the flip-band machinery retired with it"*, posture FLAT); PROME's `ACTIVE_DECISIONS` row read `EXITED — TERMINAL (COMPLETED)`; HENRY's MEMORY said *"Do NOT re-raise the VIOLET gate — dead… Any sighting of 7,496/7,455/7,491 is history."*

**WALTER carried it as live anyway** — into a dispatched signal on 8/2 (`SIG-W-20260802-004`, which called 7,455 *"HENRY's LIVE WARN LEVEL"*) and into a Will-facing boot report on 8/3, before catching it at owner-file verification.

## Why it survived — and the reason is structural, not sloppiness

**VIOLET DID publish when it RE-BASED the band.** On 7/28 it sent WALTER a publisher-side sweep packet (7,496 → 7,455/7,491, *"7,496 is retired"*) — exactly the `consumer_check` discipline, and WALTER updated off it correctly.

**Nobody published when the band was RETIRED, because retirement was a SIDE EFFECT OF A POSITION EXIT rather than a republication of a number.** There was no new value to sweep for.

⇒ **`consumer_check.py` takes `--old` and `--new`. There is no `--retired`.** The entire staleness apparatus is built around *a number that changed*. A number that **stopped existing** emits nothing.

## Why the failure direction is the dangerous one

A retired threshold sitting in a downstream registry:
- **does not error** — it is well-formed
- **does not go stale-flagged** — its vintage stamp is whenever it was last correctly copied
- **does not disagree with anything** — every surface citing it agrees with every other surface citing it, because they all inherited it from the same live-at-the-time source

**Consensus among consumers is not evidence, because they are not independent — they share an upstream.** The surface reads healthy in exactly the way [[finding_test_the_guard_not_just_the_guarded]] warns about, and it waits to be cited. **The citation then looks like diligence.**

## The corollary that makes it recur: links run in the author's direction

The same session produced a second instance of the identical shape. A BOARD correction carried a machine-readable `corrects:` field naming its targets — **but nothing pointed back**, so a reader arriving at the *corrected* signal could not learn a correction existed. Two signals whose titles asserted a corporate default that never happened sat untagged for 6 and 11 days.

⇒ **A pointer written at authoring time runs in the direction the AUTHOR travels. Readers travel the other way.** Both gaps are the same defect: *the link exists, and it is absent exactly where it is used.*

## Third form, from the same day: a lesson recorded in the CATCHER's file protects nobody

**HENRY made this exact error on 7/30**, PROME caught it, and HENRY wrote a hard trigger against it into HENRY's MEMORY. **WALTER repeated it four days later** — because the correction lived in the catcher's file and never reached the consuming registry. **A correction filed where the error was CAUGHT does not reach the next agent positioned to repeat it.**

**How to apply:**
- **When a position exits TERMINAL, sweep its registered kill/warn/gate levels the way its ledger row is swept.** Retirement is a publish event; it just does not feel like one, because nothing new was computed.
- **As a consumer:** a level whose owner has no live position is suspect on its face. Before citing another agent's registered threshold, **check the position's record, not just the number's file** — the number can be current and the *object it guards* gone.
- **As a publisher:** say *"X is retired"* explicitly and route it, rather than letting the exit imply it. An uncontested silence is not a notification.
- **Design:** any correction/retirement mechanism needs a **backward** pointer, or a check that walks the forward ones. Sibling of [[finding_guard_scope_expires_at_the_fill]] — that one says a threshold needs LEVEL + INSTRUMENT + **WINDOW**; this is the window's terminal case, where the window does not merely close but **ceases to exist**, and no one is on the hook to say so.

Related: [[finding_dated_stamp_is_a_trigger_not_a_shield]] · [[finding_reconcile_match_on_key_not_substring]] · [[feedback_reconciliation_is_last_line_move_catch_upstream]]
