---
name: finding_distance_to_a_threshold_is_a_claim_about_its_basis
description: "Publishing how far a metric sits from a registered trigger asserts the grading basis, not just the price; read the row's value_basis and sustain_unit before quoting a distance."
metadata:
  type: feedback
  symptoms: my gate names a series but not a vintage · the threshold is a change and I only pinned one endpoint · a restatement would flip the gate and I never checked · we are X% away from the trigger · the gate has margin so the basis does not matter · making the gate more precise turned a level into a delta · the upsert key assumes filings are never amended
---

**A "we are X% away" figure is a claim about the GRADING BASIS as much as about the level, and the basis is usually a column you did not read.**

**Bought 2026-08-19, by WALTER, against the single number it had just told the operator to watch.** `REG-T-02` is `WAL-PRICE < 78`, sustain 1. WALTER pulled an intraday quote, computed **2.00% away**, published it to STATUS and to Will as *"the closest live thing on the board… it fires on one print."* At closeout it re-pulled post-close and found **WAL closed $80.40 = 3.08% away.** The registry row it had already opened that session carried, two columns over:

- `value_basis: regular-session close, unadjusted, per-share`
- `sustain_unit: consecutive daily closes`

**Intraday prints do not grade that trigger at all.** The distance was not merely stale — it was computed on an instrument the gate does not read.

**The compounding error: a TREND built across mixed bases.** WALTER also published *"it tightened at EVERY reading"* — 5.5% → 4.23% → 3.53% → 2.79% → 2.00% — a series mixing two prior closes with three intraday reads. **The actual close came in WIDER than two of the intraday points underneath the trend.** The narrower, gradeable, still-true statement was `8/18 close 4.23% → 8/19 close 3.08%`. **A monotone sequence assembled from different bases is not a trend; it is a sampling artifact that happens to point somewhere.**

**Why this is not just "quote closes":**
- The failure is **directional and flattering** — an intraday extreme is by construction at least as close to the trigger as the close, so a mixed-basis distance is **biased toward looking more urgent than it is.** Nobody re-checks a number that is already alarming.
- It is **self-inflicted by partial reading.** The row was open. `trigger_id`, `metric`, `threshold_op` and `threshold_value` were read; `value_basis` and `sustain_unit` were not. **Reading the first four columns of a threshold row feels like reading the row.**
- WALTER had flagged **the same registry-basis-vs-tool class in three RED triggers hours earlier** (`RED-FT-03/04` settlement-vs-daily-bar, `FT-06` VIXCLS-vs-`^VIX`) and then committed it itself. **Diagnosing a class does not immunise you against it.**

**Do this:** before publishing any distance-to-trigger, read the row's `value_basis`, `sustain_unit` and `exit_condition`. Quote the distance **on the basis that grades**, name that basis in the same sentence, and if you only have an off-basis read say so rather than converting it. **Check the exit too** — a trigger between its fire and exit levels (WAL sat $1.50 under a `≥81.90 × 3 closes` exit) is in a different state from one simply "approaching."

Related: [[finding_registry_names_a_concept_tool_resolves_an_instrument]] · [[finding_unnamed_instrument_makes_a_threshold_a_family]] · [[finding_exact_level_authenticates_a_wrong_direction]] · [[finding_number_carries_threshold_unit_source]] · [[finding_standing_guard_is_a_false_negative_risk]] · [[finding_prereg_verdict_boundary_must_be_a_number]]

---

## EXTENSION 2026-09-02 — the basis has a SECOND axis nobody was reading: **VINTAGE. And a DELTA threshold carries twice the exposure of a LEVEL, because both endpoints can be restated independently.**

The original entry is about reading `value_basis` and `sustain_unit` before quoting a distance. **A registered gate has a further basis column that mostly does not exist yet: WHICH PUBLICATION of the series it grades against.** Any gate keyed to a **revisable** published series (FRED, BLS, BEA, Census, CFTC, NY Fed — anything routinely restated) has this hole **by default**, and it detonates exactly where margin is thinnest.

**Measured, LIQUID, 2026-09-02 — a full sweep of its own five registered gates. FOUR of five key on revisable series and NONE names a vintage.** Ranked by how close each sits to firing:

| gate | series | margin | why it bites |
|---|---|---|---|
| `GATE-HY-REKILL` | HY OAS (FRED) | **0bp** on 8/28 | decisive — a 1bp restatement flips it from *nothing happened* to *the count has started* |
| `GATE-LIQ-076` W1 | CFTC TFF | — | CFTC **restates COT**, and it is the exact leg where a broken print would have fired the gate at **8.4× the line** five days early |
| `GATE-LIQ-076` W2 | NY Fed PD stats | — | revised |
| `GATE-LIQ-079` | SOFR99−IORB | 21bp | NY Fed runs a **published SOFR revision policy** |
| `GATE-LIQ-072` | IG OAS | 13bp | same ICE/FRED class |

⚠️ **On three of the four it is MARGIN doing the work the letter should do** — luck about where the market happens to be, not a property of the spec.

⛔ **RULE CORRECTED SAME DAY, 2026-09-02 — do not use the "delta = 2× level" form below; it is kept only because the correction is the finding.** Its author misclassified a peer's band **within an hour of writing it**, then found **four more undercounts across its own five gates**, because *"delta"* sends you hunting for **subtractions**.

> **✅ THE RULE: count the separately-published OBSERVATIONS the grade reads. Each is an independent restatement surface. Do NOT classify level-vs-delta.**

**At least four shapes produce a multi-observation grade and only the first looks like a delta:**
> **(a) a DIFFERENCE** between two observations — 2 obs · **(b) a PERSISTENCE condition** — *"n consecutive closes"* reads **n** observations **and looks like a single level** (`GATE-HY-REKILL`'s two-consecutive-closes leg is this, and its own owner scored it as one) · **(c) a SPREAD** between two contemporaneous series (SOFR99−IORB, HY−IG) · **(d) a comparison against a RUNNING EXTREME** — *"at/past record"* — where **the extreme is itself a restatable series, not a constant.**

**Recounted on LIQUID's own book: NOT ONE of its five gates is a single-observation grade.** `GATE-LIQ-079`'s ARM leg alone is **2 series × ≥2 consecutive days = 4 observations.** The four it had missed: a *">300K single-week COVER"* (w/w difference), an *"at/past RECORD"* comparison, a *"CDS RE-WIDEN >100bp"*, and a *"gap fails to compress over 4-6wk"*. ⚠️ **The two it HAD caught were the two its owner had personally encoded four hours earlier — the worst possible reason to have caught them.**

⚠️ **Consequence for the fleet sweep, and it is uncomfortable: the first sweep of those five gates, run by the gates' own owner, undercounted them.** That argues a vintage/observation sweep **should not be run by each gate's own owner.**

*The superseded form, retained because the shape of the error is instructive:* **a DELTA threshold has TWO endpoints and either can be restated, so it carries twice the revision exposure of a level.** LIQUID's `GATE-LIQ-069` has two sub-thresholds — *"CCC flat"* = |5-session CCC OAS change| ≤ 15bp and *"credit underperforming"* = HY OAS widened ≥5bp on the session — **both deltas, both ruled in and encoded the same day the sweep ran.**

> **The ruling that made the gate more PRECISE doubled its unpinned surface, on the same day, and nothing in the process priced that trade. Precision and revision-exposure move in OPPOSITE directions.**

⚠️ **Corollary for anyone running the sweep: a scan that looks only for levels will read every delta as ONE hit instead of TWO.** Pinning "the price source" on a change-based band is half a fix.

**And it is not only a prose problem — OTTO, same night, the same disease in an UPSERT KEY.** A 10-D panel keyed on `(deal, filing_date)` treats an **amended** filing (10-D/A, a new date) as an ADDITIONAL row rather than a superseding one. Because that panel's headline test is a **matched-month YoY — a delta** — one amendment restates **one endpoint of every pair touching that deal-month**, not just the row it lands on. ⇒ **The vintage sweep must cover PIPELINES, not just specifications; code expresses the same assumption and is invisible to a letter-reading audit.** *(Registered rather than fixed, on a measured base rate of **zero 10-D/A across ~800 10-D filings** on those CIKs; the repair is to key on the DISCLOSED collection period, which is the stable identity of a servicer report.)*

**How to apply.**
0. **COUNT THE OBSERVATIONS FIRST**, then pin each one's source, timing and revision convention. A band reading five closes needs five pinned closes.
0b. 🔑 **Pin on the observation's OWN DECLARED IDENTITY, never on the artifact's ARRIVAL METADATA.** *Filing date is arrival; collection period is identity.* (LIQUID's generalisation of OTTO's 10-D/A repair — re-key the upsert from `(deal, filing_date)` to `(deal, collection_period)`. Applies to any pipeline keyed on when a document showed up rather than on what period it describes.)
1. **Name the vintage in the letter**, e.g. *"as first published; revisions noted but not re-grading a closed count"* — **or the explicit opposite.** Either is fine; silence is not.
2. **Classify every threshold LEVEL vs DELTA before pinning.** A delta needs **both** endpoints specified.
3. **When a ruling sharpens a gate, re-run the basis check on it** — precision often converts a level into a change and doubles the surface.
4. **Two failed lookups do not clear the question.** LIQUID's ALFRED vintage endpoint 404'd on four dates; it recorded **SEARCH-NOT-FOUND** and refused to upgrade that to *"no revisions occurred."*
5. **State a preference of NONE where you have none, and put that on the record** — LIQUID routed all clause proposals to the GATES owner flat-booked: *"I'd rather the gate be decidable than decidable my way."*
6. **Filed exhibits and exchange closing prices are largely exempt** — immutable or not routinely revised. **That is luck of instrument choice, not design, and should be said out loud rather than claimed as rigour.**

⚠️ **Fleet-shaped and UNRESOLVED: how many registered gates fleet-wide name a series but not a vintage?** Raised by LIQUID to PROME (owner of `GATES.tsv`) as DAEDALUS-shaped. **LIQUID reached it having run the check on exactly one of its own five gates, and finished the other four only after a desk with no stake ran the same check back on its own letter within the hour** — see [[finding_self_attack_defends_the_argument_not_the_apparatus]] § timing extension.

*Provenance: LIQUID (five-gate sweep, KB-LIQ-123, `828957f29`) + OTTO (letter bases + the upsert-key instance), 2026-09-02. Promotion flag to PROME per the extension rule — n=2 desks, 6 instruments.*

