---
name: finding-subagent-prefire-date-verification
description: "For sub-agents maintaining date-keeping sets (catalysts, calendars, predictions), add a STANDING MONITOR that re-fetches source-of-truth for cadence-derived rows within N days of fire date; revise if shifted. Two consecutive BRENT/FASTOW runs caught 2-day errors using this pattern."
metadata: 
  node_type: memory
  type: finding
  originSessionId: dc022fd9-625c-4d0e-9520-19ecc1acdec2
---

For sub-agents maintaining date-keeping sets (catalyst dockets, calendars, prediction timeframes), add a recurring **pre-fire date verification** monitor: every run, scan the set for rows whose dates were *cadence-derived* (estimated from a release-class cadence rule rather than locked to a published source-of-truth URL) AND whose projected fire date is within the next ~7 calendar days. Re-fetch the source-of-truth page. Revise the date if shifted.

**Why:** cadence-derived dates silently drift. Release schedules slip 1-3 days routinely (OPEC MOMR varies 11th-13th; EIA STEO varies Tue-Wed; CFTC COT shifts on holiday weeks). At write-time the cadence estimate is reasonable; by fire-time the official schedule has often resolved to a specific date that differs by 1-3 days. Without the pre-fire check, the sub-agent ships stale dates and the parent agent acts on them.

**Validated:** BRENT/FASTOW caught 2-day errors on two consecutive runs (Run 1 STEO Jun 11 → Jun 9; Run 2 OPEC MOMR Jun 13 → Jun 11) — same error magnitude both times. Both would have caused real downstream confusion at the parent agent's next session boot if not caught pre-fire.

**Why a STANDING MONITOR (recurring watch), not a one-shot:** the set grows over time; new cadence-derived rows enter every audit cycle; rows that were >7d out at write-time roll into the 7d window every week. A one-shot fixes today's rows; the monitor handles the flow.

**Halt-vs-continue rule (load-bearing):** if the source-fetch returns ambiguous data (conflicting calendars) or fails (404/timeout), the sub-agent must **leave the original date in place** AND log to ESCALATIONS — do NOT silent-revise on partial information. Three-source rule: two independent sources agreeing → accept; otherwise → escalate. Without this rule, the monitor itself becomes a silent data-corruption vector.

**Cost:** ~1 minute per row in the 7d window (single source fetch). For BRENT/FASTOW, typically 0-2 rows per run.

**Detection mechanism:** two options:
1. **Notes-language heuristic** (BRENT's current approach): scan row's `notes` column for "best-estimate," "verify against," "cadence-derived," "typical," "customary" strings. Fragile to phrasing drift but zero-schema-change to implement.
2. **Typed field** (cleaner long-term): add a `date_class` value beyond confirmed/modeled — e.g., `cadence-derived` — and key the monitor off it. Robust but requires schema migration. Defer until heuristic misses.

**Transferable scope:** any sub-agent maintaining a discrete-event SET with mixed source-locked + cadence-derived dates: SAM/KOYOMI (calendar steward), prediction-book stewards (PREDICTIONS.tsv timeframes), future agent sub-stewards. The pattern does NOT apply to fully-source-locked sets (e.g., a position-expiry-only ledger).

Related: `[[finding_subagent_baseline_audit]]` (sub-agents that maintain a SET need explicit baseline-scope audit); `[[finding_threshold_vs_mechanism]]` (separate the cadence-estimate uncertainty from the underlying release-class certainty).

**Coordinator-side corollary (2026-07-17):** the same discipline applies to the COORDINATOR's own wall-clock narration — PROME wrote "~12:00 PM ET" into a spawn packet and several user-facing timing claims when it was actually ~10:00 (estimates drift fast in long multi-delivery sessions; a teammate's UTC-stamped idle notification exposed the ~2h error). Run `date` BEFORE writing any specific clock time into a spawn prompt, watcher window, or timing claim — the "verify against `date`" line given to sub-agents is not a substitute for the coordinator doing it. Contained damage that time only because every packet carried its own verify-date instruction and the sequencing (grade-after-release, verify report-date) was event-anchored rather than clock-anchored — event-anchor over clock-anchor is the robust default.
