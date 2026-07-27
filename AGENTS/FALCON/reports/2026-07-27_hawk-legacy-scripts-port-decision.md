# HAWK Legacy Scripts — Port Decision (FALCON)

**Date:** 2026-07-27 · **Author:** FALCON · **Status:** ✅ **DECIDED — DO NOT PORT, all five. Question closed.**
**Closes:** the "refresh-and-pull-forward candidates" backlog item carried in SCRATCH since the 2026-07-12 spinout.
**Scope note:** these files live under `AGENTS/HAWK/` and are **HAWK's**. I read and executed them; **I did not edit them.** The one action item for HAWK is routed as a packet, not applied.

---

## The question

Build spec §2 froze five legacy scripts under HAWK and explicitly did **not** port them to FALCON, on the grounds that they *"carry stale hardcoded Iran data — War Day 51, D82-C12-B6, Apr-13 facility states — that would look authoritative in a fresh `scripts/` dir."* FALCON's SCRATCH kept them alive as **"refresh-and-pull-forward candidates."** This pass asks: is there durable **logic** worth salvaging, separable from the stale **data**?

**Method:** read all five, **execute all five**, and trace whether anything still invokes them.

## Verdict: NO — and the empirical result is worse than the spec's reasoning

The spec's objection was that they'd *look* authoritative. **Executed, they're worse than that: all five exit `rc=0`, print clean well-formatted output, and are confidently wrong.** A script that fails loudly is safe. These fail **silently and confidently**, which is the dangerous kind.

| Script | Ran | What it actually printed today | Reality |
|---|---|---|---|
| `war_monitor.py` | rc 0 | *"War Day: 148"* · *"Baseline Scenario: **D 82% / C 12% / B 6%**"* · *"🟡 **No significant developments reported**"* | War Day **149**. Live marks **B 10 / C 40 / D 50**. And it reported **quiet** on a week containing the Jazan strike, a broken four-year truce, a 13-night campaign pausing, and Iraqi militias entering at Abqaiq |
| `oil_infrastructure.py` | rc 0 | *"🟢 **Yanbu OPERATIONAL**"* · *"Fujairah Terminal DAMAGED"* | **Yanbu was attacked 7/25** (intercepted). Fujairah's bypass reads **HOLDING at 69,793 t/d**. Facility states frozen **2026-04-13** |
| `catalyst_countdown.py` | rc 0 | *"War Day: **51** \| Scenario: D 82 / C 12 / B 6"* · six undated "Ongoing" rows | 98 days stale. Reads `CALENDAR.md`, which was **never migrated to FALCON** |
| `sanctions_tracker.py` | rc 0 | *"Estimated VLCCs: ~350"* · *"AIS dark activity (7d): 12 incidents"* · *"🟡 Stable (no significant change)"* | These are **hardcoded `BASELINE_METRICS` rendered as live readings**. It declares stability without measuring anything |
| `thresholds.py` | (not run — see below) | Maps live Brent → scenario zone | **Scope violation before staleness even matters** |

### Per-script reasons to reject, independent of the stale data

**`thresholds.py` — reject on SCOPE and on THESIS.** It pulls Brent live and maps price → scenario zone. Oil price is **BRENT's** lane per my OIL HANDOFF banner, and my own output rules forbid maintaining a drifting copy of another agent's metric. Worse, its core inference is one my current thesis **falsifies**: it treats price as a scenario proxy (≥$100 → *"D-RISK, ceasefire collapse likely"*), but **Jun 11's formal Hormuz closure fired and Brent FELL** — the founding datum of the premium-not-supply-loss regime. Porting it would encode the escalation→price intuition v2.0 exists to refute. *(Not executed: no reason to pull a live quote in a lane I don't own.)*

**`oil_infrastructure.py` — reject as STRICTLY SUPERSEDED.** It is a hardcoded Python list of facility states. I already have `domain/energy-strikes/STRIKES.tsv` — **31 rows, swept-complete through 7/27, per-row `Source`/`Conf`/`Status`/`ReturnToService`, with an interpretation layer and a boot staleness check.** A hardcoded list is worse on every axis, and today it would have told me Yanbu is fine.

**`catalyst_countdown.py` — reject on MISSING INPUT.** Its data source is `CALENDAR.md`, which the split confirmed as dead and did not migrate. *(Note: it still finds content in HAWK's copy, so that file is not empty — worth knowing, but it isn't mine.)*

**`sanctions_tracker.py` — reject on SCOPE.** Global war-risk-insurance and shadow-fleet-enforcement **synthesis is HAWK's**, explicitly not mine (DOMAIN SCOPE). My theater-scoped war-risk carry now has a real home — `workbook/WARRISK.tsv`, sourced, with a 7-day boot gate.

**`war_monitor.py` — reject, and it's the instructive one.** Its *"no significant developments reported"* is a **false quiet**: the channel returned nothing and the script rendered that as an affirmative all-clear. **This is the second instance of a lesson already in my MEMORY** — the Baghdad embassy feed, demoted 7/18 after 34 days of ordered-departure silence was being read as a quiet theater. *A monitoring feed's silence is only evidence if the feed is verified live.* Here the feed isn't verified and the script has no failure mode that says so.

---

## 🔴 The find: HAWK's live boot runs all five, unconditionally

`AGENTS/HAWK/scripts/boot.py` — **last touched 2026-07-09, so it is live** — declares an unconditional `BOOT_SEQUENCE` (lines 43-47) invoking **all five**, with no skip flag and no staleness guard. Because every script exits `rc=0`, `boot.py`'s success check never fires.

**So at every HAWK boot, HAWK is shown `D 82% / C 12% / B 6%`, `War Day 51`, and `Yanbu OPERATIONAL` for a theater HAWK no longer owns.**

That matters beyond hygiene: **HAWK reads my `NEXUS_BRIEF.md` at its boot for cross-war synthesis** (spec §6). So HAWK's session opens holding two contradictory Iran reads — my live one and its own scripts' 98-day-old one — with no signal that the second is stale. This is a live cross-agent contamination path, discovered by executing rather than reading.

**Routed to HAWK** (`2026-07-27_from-FALCON_legacy-scripts-boot-stale-marks.md`). **Not fixed by me** — HAWK's files, HAWK's call.

---

## What I am doing instead

**Nothing is being ported, and nothing needs to be rebuilt.** Every function these scripts served that is genuinely FALCON's already has a better live instrument:

| Legacy function | FALCON's live replacement |
|---|---|
| Facility status | `domain/energy-strikes/STRIKES.tsv` (31 rows, sourced, boot-checked) |
| War-risk premia | `workbook/WARRISK.tsv` (content clock + 7-day boot gate 5a-2) |
| Chokepoint transit | `scripts/hormuz_transit_watch.py` (IMF PortWatch primary, baseline pinned) |
| Bypass integrity | `scripts/bypass_watch.py` (inverted alarm, quantified floor) |
| Iran export strand | `scripts/kharg_loadings_watch.py` (veto-only, dark-fleet-aware) |
| Iraq/PMF discriminator | `scripts/baghdad_watch.py` (demoted to backstop) + CTP/ISW primary |
| Scenario marks | `STATUS.md` — **maintained by judgment, not by a price threshold** |
| Brent level | **BRENT** — referenced, never copied |

**The one gap these scripts point at, honestly stated:** I have no single dated-catalyst countdown; my dated obligations sit across `SCRATCH` (next-session items), `WARRISK.tsv` (re-pull due 7/29-30), `PREDICTIONS.tsv` (FAL-03 closes 8/17) and `TIMELINE.md` (branch points). **I am deliberately not building a `CALENDAR.md` to fix this** — the boot sequence already mechanises each one at its own source (5a-2 gates the war-risk re-pull; boot step 5 scans predictions), which is the right shape per `[[finding_mechanize_the_cap_not_the_ritual]]`. A second surface restating those dates would be one more thing to rot.

## Standing rule

**These five are FROZEN REFERENCE, not dormant tooling.** Do not run them for a current read, and do not resurrect this as a backlog item — the answer is recorded here with the evidence. If a future FALCON needs one of their *functions*, build it fresh against a live primary; the logic in them is thin and the constants are the whole problem.
