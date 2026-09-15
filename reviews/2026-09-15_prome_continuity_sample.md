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

| PROME action | Canonical record | State / next action |
|---|---|---|
| WQ-213 follow-up | `PROME/WILL_QUEUE.md` WQ-213 · `PROME/DOCKET.tsv` L389 | Read Will's reassessment appointment before the separate needed-by deadline; take both from WQ-213. |
| Recurring roll-hazard method | `PROME/DOCKET.tsv` L386; instances L384/L385 | **Keep L386 undated.** The method must cover both disagreement between legs and a matched pair changing relative to its own history. Read L386 for the owed work. |

The scheduling row follows the existing reassessment-first instruction in SCRATCH and the September 14 Codex closeout. It does not set or change an appointment. The roll row preserves the specific method distinction; a bare “see docket” would lose that guard on the startup path.

## 2. HANDOFF — the machine-change paragraph only

### Before (verbatim at source revision 3c6f9759d)

> ⛔ **THE MACHINE CHANGED AND PROME'S OWN BOOT REPORT GOT IT WRONG — it wrote *LAPTOP*, inherited from the entries below rather than checked at `hostname`.** The capability columns DIFFER: this box HAS FFIEC creds, Kalshi keys, the FIRMS `MAP_KEY` and the `liquid-hy-watch` timer, all of which `MACHINE_LOCAL.md` records as MISSING on the laptop — **a launch brief written off the inherited label would have stood down work that runs fine here.** Caught by an external reviewer, not by PROME.

### Proposed replacement

> **Verify the current host and capabilities before preparing a launch brief:** run `hostname` and the capability check in `PROME/BOOT.md` step 5. Do not infer the machine or available credentials from earlier handoff entries. `PROME/MACHINE_LOCAL.md` is the inventory; capability presence does not establish authentication.

This replaces only the quoted paragraph, not the surrounding handoff entry or its live blockers. It avoids carrying a dated claim about which machine has which credentials as if it described the current session.

## What stays, and where history would go

| Material | Treatment if this sample is approved |
|---|---|
| WQ-213 appointment, deadline and decision authority | Stay at WILL_QUEUE; STATUS points there. No trade or ruling changes. |
| L386 undated guard and the two comparison types | Stay explicit in STATUS; detailed work stays at DOCKET L386. |
| Other roll restrictions and market caveats | Unchanged elsewhere in STATUS/HANDOFF; this sample does not remove them. |
| Original STATUS incident narrative | Preserve verbatim in existing `PROME/archive/STATUS_HISTORY.md` with source revision and section label. |
| Original HANDOFF machine incident | Preserve verbatim in the existing HANDOFF archive structure with a pointer from the rewritten entry. |
| Source history now | Already recoverable with `git show 3c6f9759d:PROME/STATUS.md` and `git show 3c6f9759d:PROME/HANDOFF.md`; exact excerpts are also above. No archive move has happened. |

## Fresh-session walkthrough

- **Where is the appointment?** WQ-213, reached directly from the queue row; it precedes the separate deadline.
- **Can the recurring roll work be given a date?** No; that prohibition remains visible.
- **Is comparing the two current legs enough?** No; comparison with the pair's own history remains explicit.
- **Which machine/capabilities are available now?** Measure them through the existing boot checks; the old desktop narrative does not answer this.
- **Did any research grade, authority or completed task change?** No. This is proposed organization of existing instructions.

This walkthrough is an author check, not an independent cold-read result. Before implementation, the existing plan/result review requirements for archival moves still apply. The broader STATUS/HANDOFF rewrite remains outside this sample. The immediate decision is whether this amount of startup detail is useful to Will.
