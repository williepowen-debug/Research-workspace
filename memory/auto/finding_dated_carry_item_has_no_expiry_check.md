---
name: finding_dated_carry_item_has_no_expiry_check
description: "A carried item with a DATE in it never self-reports as wrong: a crossed threshold produces an event, but a date that simply passes produces nothing and keeps sitting on the list looking pending. State items get re-checked at boot; dated items do not."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 0fed4cdb-2b75-4107-8c19-03bcb6b7439f
  modified: 2026-08-07T22:23:26.245Z
---

**A threshold that gets crossed produces an EVENT. A date that simply PASSES produces nothing** — no alert, no contradiction, no failed check. It just keeps sitting on the carry-forward list looking pending, and every boot re-reads it as live.

**WALTER, 2026-08-07.** Four dispatched signals said *"MU 8/4 is the resolver."* Micron's fiscal Q4 ends ~09/03 and prints late September; it was never going to report on 8/4. VULCAN sent the correction on **8/3**. It sat unread in the inbox while "MU Tuesday 8/4" stayed in the STATUS near-trigger block **and** in the `LAST_COMPLETION` FOLLOW-UP list — the file whose entire purpose is to survive handoff — **through 8/4, 8/5, 8/6 and into 8/7.** The date came and went and **nothing in the system noticed**, because nothing was watching for a date to become the past.

**Why the asymmetry is structural, not carelessness:**
- Every *state* item on a carry list gets re-derived at boot — live levels are re-pulled, thresholds re-evaluated, registries re-read, staleness computed. **They are checked because checking them is the same act as using them.**
- A *dated* item is a string. Reading it does not evaluate it. **"MU 8/4" reads identically on 8/1 and on 8/7**, and only a human comparing it to today's date can tell the difference — which is exactly the comparison nobody makes while scanning a list they wrote themselves.
- The failure is silent in the **worst direction**: the item stays on the list, so it reads as *tracked*. An item that vanished would at least be noticed.

**How to apply:**
- **When a dated item goes onto a carry list, write what happens when the date passes** — not just the date. "MU 8/4 → if 8/4 closes with no print, the date is wrong, re-derive it" is self-checking; "MU 8/4" is not.
- **At boot, diff every dated carry item against today** before working the list. It is one pass and it is the only thing that catches this class.
- **A date sourced from an agent's prose (yours or another's) is UNVERIFIED until checked against the issuer's own calendar.** This one originated in VULCAN's 7/12 STATUS and was restated four times without re-derivation, then propagated to WALTER, then into four dispatched signals. **Nobody re-derived it because everybody had seen it before.**
- **Prefer verification by ABSENCE where it is available** — it is the strongest form and usually the cheapest. EDGAR showed MU's most recent 8-K of *any* kind was 6/24, so no 8/4 earnings report exists. That is dispositive in a way "the fiscal calendar suggests late September" is not.

**Related:** [[finding_weekday_assumed_never_evaluated]] and [[finding_date_gate_beats_weekday_name]] cover dates that are wrong *when written*; this one covers dates that were merely **unexamined** and then **expired**. [[finding_canonical_surfaces_stale_inbox_carries_live_state]] is the delivery half — the correction existed and was sitting unprocessed. [[finding_expected_window_rederived_from_now_drifts]] is the mirror image: there the anchor moves when it should be pinned; here it is pinned and nobody checks whether the pin is still in the future.
