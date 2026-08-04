---
name: finding_automation_reads_its_own_error_back_as_canon
description: "A scheduled run that writes to a ledger the run later READS creates a closed loop — its own error returns as canon; check git author, not file contents"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4a287862-c97e-4aa6-b905-47756ec4dd2a
  modified: 2026-08-04T17:24:20.879Z
---

**A scheduled/automated run that WRITES to a surface it later READS is a closed contamination loop.** Its own error comes back as canon, confirmed by nothing but itself.

**Worked case (BRENT, 2026-08-04).** The Wed 7/29 EIA cloud routine pulled Cushing from an *aggregator*, got `19.10M / −273K`, tagged it **`[CONF]`**, and **committed itself**. It propagated into `TRACKER.md` (two places). The figure was retracted 8/3 — but only in one file. Meanwhile a fleet redesign had just made *"read TRACKER's top block at run time"* the routines' source of truth. **The next run would have read its own retracted figure back as current.**

**Three lessons stacked in one incident:**
1. **A redesign that moves thresholds out of a rotting prompt into a rotting FILE relocates the rot, it does not remove it.** Closing an invisibility problem can create a *freshness dependency with no owner and no alarm*.
2. **The wrong delta INVERTED the read.** True −771K vs the written −273K meant the draw was *accelerating*, not "decelerating" as the file said. **A wrong number is recoverable; a number that reverses the direction of travel is a false all-clear.**
3. **An aggregator was tagged `[CONF]` while a live API key for the primary sat in the kit.** Automation has no reviewer, so a source-tier violation ships silently.

**How to detect it — the discriminator is in git, not in the file.** Routine-written content is *indistinguishable from your own inside the file*; only the commit author separates them (`git log --format='%an' -- <path>`; routines commit as a generic agent identity, live sessions as the operator). A BRENT audit found **46 routine-authored commits, none ever reviewed** — and a prior root-cause diagnosis had wrongly blamed "another session on the other machine."

**How to apply:**
- **If any automation writes into your directory:** audit its past commits by author at least once; you have probably never read them.
- **Never let a run's output surface double as its input surface** without a staleness self-check *inside* the surface — e.g. *"if this stamp is >3 days before the run date, say so in the output and treat every level as UNVERIFIED."* Make the surface **announce its own rot** rather than serve it silently.
- **Fence what a run may not do, in the surface itself:** mark gates and prediction rows **RECORD-ONLY, NEVER GRADE.** Calibration damage is not repairable after the fact.
- **Pin source tier in the prompt:** primary API only; an aggregator may never carry a `[CONF]` tag.
- **A retraction is a PUBLICATION event** — sweep the retracted VALUE across every surface, not just the one you were looking at. Related: [[finding_plausible_stale_value_evades_review]], [[finding_dated_stamp_is_a_trigger_not_a_shield]], [[finding_record_of_an_action_is_not_the_action]], [[finding_offrepo_routine_prompt_rot]].
