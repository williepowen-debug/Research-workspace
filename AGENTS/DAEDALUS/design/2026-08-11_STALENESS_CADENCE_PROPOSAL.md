# Staleness-cadence proposal — (b) pre-commit nudge + (a) STATUS-writes backstop + (c) absolute-age floor

**Status:** ✅ **APPROVED — Will verbatim "approve the staleness proposal", 2026-08-20 (in DAEDALUS's session, morning). Rollout live: modes built 8/20 (this session); root-canon (b) line drafted → PROME to land with Will's OK on record; (a)+(c) CANDIDATES pass runs at Staleness #4 ~9/1.** *(Prior: DRAFT for Will; greenlit PROME→WATT 2026-08-04, (b)-first ordering endorsed; drafted 2026-08-11)* · **Provenance:** WATT 8/4 §3 (the sprint-blindness finding + its own withdrawn per-day `LEDGER_CADENCE`, correctly withdrawn) · Staleness Sweep #3 (PAT-092 live witness, PAT-095) · **Owner if adopted:** DAEDALUS (`ledger_staleness.py` + `scripts/` grant).

## The problem — three measured blind spots of a day-denominated relative clock

1. **Sprint-shaped work is invisible** (WATT 8/4, Will's own root-cause): an active agent refreshes STATUS repeatedly while a ledger idles — the fleet backlog stands at **~32 ledgers 12+ STATUS-writes behind**, of which a 30-day threshold had flagged exactly 4.
2. **A stalled agent freezes the metric** (PAT-092; MARCO = the live witness 8/11): STATUS stops moving → the relative delta reads **constant (+59d across three reads, 8/4→8/11) while true age grew to 70d**. The instrument understates precisely when things worsen.
3. **Even a firing alarm doesn't convert** (PAT-095): REGINALD's +130d alarm fired through a full recovery session. Detection must land where work is selected — the commit/closeout moment or a named ask — not only at boot.

## Mechanisms, in adoption order

**(b) FIRST — the pre-commit nudge (thresholdless, PROME-endorsed ordering).** At closeout, when the commit set includes `STATUS.md` but none of the agent's `LEDGER_GLOB`-tracked ledgers, print one line: `nudge: STATUS moving without ledgers — X.tsv now N STATUS-writes behind (freeze-or-refresh, or say why not)`. No threshold to tune, fires at the exact moment the gap is being created, lands in the session that can act (the PAT-095 lesson). Implementation: ~20-line `--nudge <AGENT>` mode in `ledger_staleness.py`, invoked as one closeout-protocol line (no git-hook infra needed). **Will-gate: the root-canon closeout line.**

**(a) BACKSTOP — the STATUS-writes unit.** `--writes` mode: staleness measured in **STATUS-commits-since-ledger-commit** (`git log --oneline <since-ledger-commit> -- STATUS.md | wc -l` per ledger), flag at ≥12 (the backlog framing's own bar). Denominates staleness in the agent's OWN activity, so sprints can't hide a gap and idle agents don't false-flag. First pass runs **CANDIDATES-not-defects** (PROME 8/4 item 2, verbatim: owners confirm each ledger's real cadence before anything is called stale) over the 32-ledger backlog at Staleness Sweep #4 (~9/1).

**(c) FLOOR — absolute age.** Flag any non-exempt ledger whose absolute content vintage exceeds 90d **regardless of the relative delta** — the direct PAT-092 counter (a stalled agent's co-drifting surfaces cross the floor even when relative reads 0). Cheap: `file_time()` already computes the absolute vintage.

## What this deliberately does NOT do

No per-day per-ledger cadence registry (WATT's withdrawn form — right to withdraw: it invents N settings nobody will maintain). No boot-time-only alerting expansion (PAT-095 — boot alarms don't convert). No change to the two-state banner rule or existing default mode (PAT-035: all three mechanisms additive, default `--all` byte-identical, each capable-case-watched before shipping per CHECK_STANDARD §3).

## Rollout if approved

1. Ship `--writes` + `--abs-floor` + `--nudge` additively; fleet-diff validation. 2. Root closeout gains the one (b) line (Will's edit to approve). 3. Sweep #4 (~9/1) runs (a)+(c) CANDIDATES pass over the backlog. 4. Retire the interim "trade-pass-certifies-24-not-fleet" caution when the coverage work lands.

— DAEDALUS, 2026-08-11
