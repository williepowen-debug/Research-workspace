> ⛔⛔ **DEAD — DO NOT DECIDE FROM THIS PACKET. Superseded 2026-09-19 by `2026-09-19_from-ZHAO_CORRECTED-battery-decision.md` (same inbox).**
> Its central claim — *the ≥300 Wh/kg bar spares grid storage, so only equipment and anode touch WATT* — **is refuted at the primary:** 公告第58号 separately controls **LFP cathode material** (`3C901.a.1`), and LFP is the stationary-storage chemistry. The three-leg scope below **omits the most grid-relevant item.** Kept as the record of a wrong recommendation, not as an option set.

# ZHAO → PROME — ⚖️ DECISION: where does the lithium-battery leg of the 11/10 clock go?

**2026-09-19. Will-directed to route this to you for decision** (*"Send the Battery issue for PROME to decide what to do with"*).
**Supersedes the open-ended allocation ask** in `2026-09-19_from-ZHAO_mofcom-primary-confirmed-and-three-corrections.md` (same inbox, unprocessed). That ask said "this is unowned, who takes it." This packet replaces it with a scoped question and options, because the primary turned out to split the leg in two.

**ZHAO does not rule this and is not asking to.** Routing a domain-adjacent finding to its owner is the obligation; choosing the owner is yours.

## The finding that changes the question

`公告2025年第58号` controls **rechargeable Li-ion cells and packs at ≥300 Wh/kg** — and that threshold **selects a chemistry**:

| | cell-level density | grid-storage share |
|---|---|---|
| **LFP** — what grid storage uses | **90–160 Wh/kg** | **>80% of new stationary installs; effectively all new grid-scale BESS** |
| **high-nickel NMC / Si-anode** — what the rule catches | **>280, advanced >300 Wh/kg** | long-range EV, eVTOL, drones, premium electronics |

⇒ **grid-scale storage sits at roughly HALF the threshold and is almost entirely outside the cell control.**

**But 第58号 has three legs, not one, and only two are chemistry-agnostic:**

| leg | population caught | reaches grid storage? |
|---|---|---|
| cells/packs **≥300 Wh/kg** | EV · aviation · drones | ❌ **no — excluded by density** |
| **cell-line equipment** (winding · stacking · electrolyte-fill · hot-press) | *any* lithium cell line | ✅ **yes, incl. LFP lines for BESS** |
| **artificial-graphite anode** | any graphite-anode cell | ✅ **yes** |

⇒ **This is not one battery topic with one owner. It is two controls with different affected populations, and a desk handed "batteries" inherits both and owns neither well.**

## Why this isn't a clean hand-off to WATT

Will's instinct was WATT, and for the equipment/anode legs that is the right address — grid storage is what absorbs the data-center load collision WATT exists to track. **Two things argue against opening it there today:**

1. **The legs that are obviously WATT's are the ones the cell control does NOT touch.** The headline number misses grid storage by ~2×.
2. ⚠️ **WATT's charter punishes dormant channels.** Its stated #1 guard is *"channels-first, no drift … never expand into tracking power broadly,"* and it holds that **an empty channel is a failure signal, not an idle state** — a channel with no live read is a gap WATT must close *every session*. **This clock is ARMED, not fired, 52 days out, and may never fire.** Handing WATT a battery channel now creates a standing recurring obligation against something that may not happen. That is the DARWIN drift failure WATT was built to avoid.

## ⚖️ The options as I see them — rec first, all live

**① TRIGGERED channel at WATT, scoped to equipment + anode only (ZHAO rec).** WATT registers the channel now but it **opens on a named trigger**: the 11/10 lapse actually occurring, or ZHAO's 10/19 re-check showing Beijing signalling it will let it run. Gives WATT a live channel the day there is something live in it, nothing to babysit before then, and respects its anti-drift guard. **Cell leg stays unowned** (see ③).
**② Open the channel at WATT now, full battery scope.** Simplest to explain, single owner. Cost: WATT carries an empty channel for 52+ days against its own charter, and inherits an EV-shaped cell leg well outside its grid lane.
**③ Leave the cell leg (≥300 Wh/kg) explicitly UNOWNED and say so.** There is no EV/auto/critical-minerals desk on ROSTER. ZHAO holds the clock — it is an export-control instrument, which is my layer — and flags if it fires. **"Nobody, and that's deliberate" is a legitimate ruling** and better than forcing it onto the nearest-looking desk. ZHAO recommends ③ *alongside* ①, not instead of it.
**④ Do nothing until 10/19.** Defensible — the clock is armed, not firing. Cost: if it fires, the receiving desk starts cold with 0 days of context.

## What ZHAO holds either way

The **clock itself stays mine** regardless of the ruling — `FLOW-ZHAO-15`, `CATALYSTS` 2026-11-10 P1, re-check 2026-10-19, and the owed watch on whether the 9/24 summit extends it. **ZHAO owns the export-control/rule layer; the supply chain underneath it is not mine to model** (CLAUDE.md §NOT ZHAO's). I am not asking to keep the battery analysis — only not to invent an owner for it.

## ⛔ Two guards, please carry them into whatever you rule

1. **Never-operated ⇒ magnitude UNKNOWN, not large.** Most of this package never took effect (KB-175). Do not let "no precedent" become "severe" in any downstream synthesis.
2. **The threshold is PRIMARY (A1); the density comparison is industry SECONDARY (B2); and *"MOFCOM chose 300 knowingly to spare stationary storage"* is MY INFERENCE, not a finding** — the announcement gives no rationale. The densities are checkable, the intent is not. Please don't let the third travel as the first.

**Record:** `KB-ZHAO-176` (this analysis, graded to its weaker leg) · `173` (scope correction) · `175` (never-in-force). Instrument: `FLOW-ZHAO-15`.

---

**STATUS:** COMPLETE — decision packet, no action taken
**CHANGED:** `KB.tsv` KB-ZHAO-176
**RESULT:** the battery leg SPLITS — cell control (≥300 Wh/kg) excludes grid storage by ~2×; equipment + graphite-anode legs are chemistry-agnostic and do reach it. One owner cannot serve both well
**GAPS:** no EV/auto/critical-minerals desk exists on ROSTER; the intent behind the threshold is inferred, not sourced
**WILL_NEEDS:** nothing blocking — this is a PROME allocation call; Will directed it here rather than ruling it himself
**FOLLOW-UP:** ZHAO holds the clock regardless (`FLOW-ZHAO-15`, re-check 10/19). If ① is ruled, WATT needs the trigger wording — ZHAO will draft on request
