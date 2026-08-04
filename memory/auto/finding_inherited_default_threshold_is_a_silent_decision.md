---
name: finding_inherited_default_threshold_is_a_silent_decision
description: "A correctly-built, correctly-running freshness check reported 'quiet' for 13 days over a ledger contradicting STATUS on two channel scores — because it inherited a shared script's 30-day default, tuned for a slower ledger than the one it was pointed at"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 1e5860de-fa41-4c29-8324-e3e12ede250f
  modified: 2026-08-04T17:46:31.992Z
---

**WATT's `boot.py` printed `✓ quiet` on its ledger-staleness leg at every boot while `VX.tsv` sat 13 days and three half-sessions behind `STATUS.md`** — carrying **P1=3** against STATUS's **P1=2**, **P3=3** against **P3=4**, and a *"leg-5 DM2 DARK — no `PJM_API_KEY`"* source note the key's restoration had already falsified. Found 2026-08-04 only because Will asked whether the prior session had closed out properly.

**Nothing was broken.** The shared `scripts/ledger_staleness.py` defaults to `--days 30`, and its own docstring says that is deliberate — *"30 = rot, not mild drift."* Correct for a slow reference ledger. **13 < 30.** The check ran, passed, and was right about the question it was actually asking.

**The defect was that nobody ever chose the threshold.** It arrived as a default, and a default you did not examine is a decision you made silently. The ledger in question exists *to change every session*; the threshold was tuned for one that changes quarterly.

**Why this class is expensive:** it fails **silent and green**. A noisy check gets fixed on its first false alarm. This one actively certified a contradiction as healthy, at every boot, for three sessions — and the artifact it was guarding was a *state* file, so nothing downstream looked wrong either. The visible closeout (STATUS, SCRATCH, LESSONS, brief folded last, KB, memo, pushed and verified on origin) was complete and correct the whole time.

**How to apply:**
- **Set a freshness/staleness threshold from the CADENCE OF THE THING MEASURED, not from a fleet default.** Ask "how often is this file *supposed* to change?" before accepting any `--days`.
- **Prefer a threshold measured RELATIVE to a companion artifact** (here: age *behind `STATUS.md`*, not absolute age). That is what makes a tight bound safe — a long gap between sessions ages both files, so only genuine write-back drift trips it. WATT moved to `--days 7` on exactly this reasoning.
- **A shared script's default is scoped to the median caller, never to you.** When you point a shared checker at your own surfaces, override the threshold locally rather than editing the shared script (`scripts/` is not yours to change — flag the default to PROME as fleet-shaped instead).
- **Tightening a stale threshold is a discovery action, not just a fix.** WATT's `--days 30 → 7` immediately surfaced a *second* hidden defect the old bound had been hiding: `TRADE.md`, 23 days behind, still reading *"No trigger crossed"* after two of its triggers had fired. Re-run the tightened check and read what falls out before assuming you knew the scope.

Related: [[finding_test_the_guard_not_just_the_guarded]] (that one is a guard *broken at build* — this one is a guard *built and running correctly* with a mis-scoped bound, so code review cannot catch it), [[finding_banner_is_a_warning_not_a_fix]], [[finding_derived_surface_band_rot]], [[finding_verification_zero_is_ambiguous]], [[finding_mtime_is_corrupted_by_git_sync]].
