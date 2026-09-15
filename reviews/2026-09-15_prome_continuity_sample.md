# Continuity cleanup sample — proposed, not applied

This is a small before/after sample for Will's review. It applies the document roles already stated in `PROME/CLOSEOUT.md`: STATUS carries current operational state, HANDOFF carries concise navigation, and historical accounts have an on-demand home. It proposes no new rule, tool or recurring review.

## 1. STATUS — two adjacent queue rows

These rows currently mix an account of a repaired scheduling omission with a live instruction about recurring contract-roll hazards.

### Before (verbatim at source revision 3c6f9759d)

```markdown
| ✅ **An INSTRUMENT caught something, for the first time all day** | `PROME/DOCKET.tsv` **L389** | `docket_view.py --check` flagged a **2026-09-18** prose date in SCRATCH that **no DOCKET row covered**. It was right: **`WQ-213`'s `needed_by` is a dated obligation with a capital consequence and had NO row** — WILL_QUEUE held the decision, DOCKET held nothing. Other WQ items with dated consequences already carry rows (L254/WQ-168, L263/WQ-171), so this was a **gap in the pattern, not a deliberate exclusion**. ★ Worth its own line because **every other catch today came from one desk reading another's work.** |
| 🔴 **The roll hazard is a CLASS and PROME registered it as a chain of dated rows** | **L386** (class, undated) · L384/L385 (instances) | ⛔ **A dated instance goes QUIET EXACTLY BEFORE THE NEXT OCCURRENCE** — the failure the hazard itself describes. **Four forms surfaced, each invisible to the guard built for the one before it**, and TERRY's sentence is the one to keep: ***our guards have been one form behind all day.*** The axis changed — ①②③ were legs disagreeing with **each other**; ④ is a matched pair disagreeing with **its own past**, which a same-moment guard structurally cannot see. ⛔ **L386 must never be given a date.** |
```

### Proposed replacement

Remove the completed scheduling-incident row from STATUS, preserving its account in history. Add no replacement WQ-213 reminder: `PROME/SCRATCH.md` § NEXT SESSION already directs the boot to Will's reassessment appointment, and `PROME/WILL_QUEUE.md` owns the appointment and deadline. Confirm that route still exists when applying this sample.

Replace only the recurring roll-hazard row with:

| PROME action | Canonical record | State / next action |
|---|---|---|
| Recurring roll-hazard method | `PROME/DOCKET.tsv` L386; instances L384/L385 | **Before using a continuous energy spread, read and apply L386's contract-identity and threshold-basis checks. Keep L386 undated: the hazard recurs across rolls.** |

The roll row supplies the trigger and next action. L386 owns the detailed method: identify the contracts with its required control and check whether the observed level uses the same contract basis as the threshold. Matching the two current legs alone is insufficient. That procedure remains at its source rather than being reproduced in STATUS.

## 2. HANDOFF — the machine-change paragraph only

### Before (verbatim at source revision 3c6f9759d)

> ⛔ **THE MACHINE CHANGED AND PROME'S OWN BOOT REPORT GOT IT WRONG — it wrote *LAPTOP*, inherited from the entries below rather than checked at `hostname`.** The capability columns DIFFER: this box HAS FFIEC creds, Kalshi keys, the FIRMS `MAP_KEY` and the `liquid-hy-watch` timer, all of which `MACHINE_LOCAL.md` records as MISSING on the laptop — **a launch brief written off the inherited label would have stood down work that runs fine here.** Caught by an external reviewer, not by PROME.

### Proposed replacement

> Verify the current host and use `PROME/BOOT.md` step 5's capability checks; do not inherit machine assumptions from earlier handoffs.

This replaces only the quoted paragraph. BOOT retains the commands, capability states, inventory pointer and distinction between credential presence and authentication. The surrounding handoff entry and its live blockers remain outside this sample.

## What stays, and where history would go

| Material | Treatment if this sample is approved |
|---|---|
| WQ-213 appointment, deadline and decision authority | Stay at WILL_QUEUE, reached through the existing SCRATCH resume instruction. No additional STATUS reminder. |
| L386 undated guard and use-time instruction | Stay explicit in STATUS; contract-identity and threshold-basis procedures remain at DOCKET L386. |
| Other roll restrictions and market caveats | Unchanged elsewhere in STATUS/HANDOFF; this sample does not remove them. |
| Original STATUS incident narrative | Preserve verbatim in existing `PROME/archive/STATUS_HISTORY.md` with source revision and section label. |
| Original HANDOFF machine incident | Preserve verbatim in the existing HANDOFF archive structure with a pointer from the rewritten entry. |
| Source history now | Already recoverable with `git show 3c6f9759d:PROME/STATUS.md` and `git show 3c6f9759d:PROME/HANDOFF.md`; exact excerpts are also above. No archive move has happened. |

## Fresh-session walkthrough

- **Where is the appointment after removing the STATUS row?** The existing SCRATCH resume instruction directs the session to WQ-213 before the implementation queue. WILL_QUEUE owns the appointment and separate deadline.
- **Can the recurring roll work be given a date?** No; that prohibition remains visible.
- **When must the session read the roll method?** Before using a continuous energy spread, as the replacement row explicitly states.
- **Is comparing the two current legs enough?** No; the row also names threshold-basis checks and requires reading and applying L386, where the full method remains.
- **Which machine/capabilities are available now?** Measure them through the existing boot checks; the old desktop narrative does not answer this.
- **Did any research grade, authority or completed task change?** No. This is proposed organization of existing instructions.

This walkthrough is an author check, not an independent cold-read result. Before implementation, the existing plan/result review requirements for archival moves still apply. The broader STATUS/HANDOFF rewrite remains outside this sample.
