# Path-Conditioned Cut: DIET Episodes With Early ≥+40% Prints

**Date:** 2026-06-10 ~2:15 PM ET (intraday, pre-EOD-adjudication)
**Trigger:** Orch critique #2 of VIOLET's 6/10 conversational base case — unreconciled tension between the L1 canonical table (~60% episode rate for ≥+50% VIX peak, window open to ~Aug) and the tactical distribution (~10-15% "genuine escalation" tail). Asked: of DIET episodes that reached ≥+50%, how many had already printed ≥+40% early, and what did their paths do next?
**Data:** `workbook/DIET_COILED_SPRING.csv` (fire days, KB-VIO-079 lineage) + yfinance ^VIX daily closes 2012-2026. Episode clustering per `scripts/diet_coiled_spring.py` (gap ≤21 td). Peaks measured on **closes** (consistent with canonical table).

---

## METHODOLOGY NOTE — ANCHOR SENSITIVITY (the catch that matters)

Our own records anchor the live episode inconsistently:
- **First-fire anchor (5/20, VIX 17.44):** live episode peak so far = **+23.3%** (6/5 close 21.51). +50% = VIX 26.16. On this basis the episode has NOT printed an early +40%.
- **Last-fire anchor (5/29, VIX 15.32):** how the thesis's "PAID FORWARD → +40% at td-4" line was computed. Live = **+40.4%** at td-5. +50% = **VIX 22.98** — i.e., essentially the fade-invalidation line (23), just above 6/10's overnight peak (22.24).

**Canonical-table construction (Orch refinement 2, VERIFIED 6/10 ~2:45 PM):** the KB-VIO-079 episode-level rates are the **max over per-fire-day forward windows** — verified by reproduction: max-over-fire-days gives exactly 23/25 / 18/25 / 15/25 (DIET) and 15/16 / 13/16 / 9/16 (STRICT); first-fire-day-only does NOT (22/25, 17/25). So the episode counts as a hit whenever *any* fire day's window crosses the threshold, and the most favorable (lowest-base) fire day governs. **For the live episode that is 5/29 @ 15.32 → the table-consistent operative +50% line is VIX ≈ 23.0, not ~26.** (This file's first version attributed first-fire anchoring to the canonical table — wrong, corrected here.)

**Rule going forward:** any % claim about this episode must name its anchor (METRIC SEMANTICS discipline; same class as the final_5d_change mislabel, KB-VIO-059). The cut below was run on BOTH anchors.

## RESULTS

**Conditional fires identically on both anchors:**

| Cut | First-fire anchor | Last-fire anchor |
|---|---|---|
| Unconditional P(peak ≥+50% in fwd-60td), 25 DIET eps | 56% (14/25) | 52% (13/25) |
| Episodes printing ≥+40% by td-12 ("early big print") | 6 | 6 |
| **P(≥+50% \| early ≥+40%)** | **100% (6/6)** | **100% (6/6)** |
| P(≥+50% \| NO early +40%) | 42% (8/19) | ~37% (7/19) |
| Exact-shape subset: early peak in [+40, +50) then pullback — went on to touch ≥+50% later | **3/3** (HH at td16/td26/td46) | **1/1** (2023-09: +43 early → +57 td24) |
| Reached ≥+85% (VIX-30-class from live base) within early40 group | **1/6 (17%)** (only 2024-12 +104; 2014-11 peaked +83, below line) | **2/6 (33%)** (2014-11 +95, 2024-12 +104) |
| STRICT corroboration | 1/1 early40 → hit50 | — |

**Path detail, early40 group (first-fire anchor):** 2014-11 (+44 early → +83 td16, end +11) · 2017-08 (+54 in-spike, faded, end −6) · 2018-03 (+57 in-spike, faded, end −22) · 2023-09 (+48 early → +69 td26, end −4) · 2024-08 (+45 early → +50 td46, end +11) · 2024-12 (+104 in-spike, end +84).

Key decomposition: 3 of 6 hit ≥+50% *during* the early spike itself; the other 3 peaked +44-48 early, pulled back, and **all 3 made a later higher high ≥+50%**. There is **zero precedent in this table for "printed +40% early, then never touched +50%."**

## INTERPRETATION

1. **The check forces the tail UP.** Conditional on our shape (early +40% print, td-5, pullback underway), a later ≥+50% touch is the modal-to-near-universal historical path, not a 10-15% tail. Under table-consistent (max-over-fire-days) methodology the operative ≥+50% line is **VIX ≈ 23.0** — a touch of the invalidation line is the historical NORM for this shape. **This makes the "sustained" qualifier load-bearing, not just correct:** without it, the fade framework's invalidation fires on the *expected* path. (Conservative first-fire reading puts the retest level at ~24.5-26; both anchors stated per the naming rule.)
2. **The VIX-30-class tail (≈+85% from live base) ran 17-33% in the early40 group (1/6 first-anchor / 2/6 last-anchor)** vs the conversational 10-15%. n is tiny and the rate is anchor-dependent — carry the range, not the flattering endpoint — but the direction of the error is clear: the conversational distribution was too light on the right side.
3. **Fade *destination* survives; fade *path* doesn't.** Half the early40 group ended the 60td window at or below base (end −6/−22/−8/−4%) — consistent with "premium deflates eventually." But the path to that destination ran through a ≥+50% touch in 6/6. Sequencing implication for the Event-Premium Fade: if the gate opens post-6/17, sizing/structure must budget for a 23-26 retest inside the window (open to ~Aug 12-25 depending on anchor) — or treat the retest itself as the entry.
4. **Caveats, honestly held:** (a) n=6/3/1 in the conditional cells — these are shape-precedents, not statistics; (b) partial mechanical bake-in (an early +40% print starts only 10 vol-% from the +50% line on the same base); (c) base rates are unconditional on catalyst type — none of the 6 analogs featured a live interstate war with an active diplomatic off-ramp (Qatar channel), and none sat inside the current record-GEX suppression structure; (d) close-basis peaks understate intraday touches.

## DISPOSITION

- **Independently verified by Orch 6/10 ~2:30 PM** (recomputed both anchors from same data): headline 6/6 confirmed, exact-shape membership/outcomes confirmed, anchor arithmetic confirmed. Two refinements folded in above: (1) ≥+85% quoted as 17-33% range with anchors named; (2) canonical-table construction corrected to max-over-fire-days → operative +50% ≈ 23.0 (VIOLET then verified the construction by exact reproduction of the canonical rates). Cut APPROVED as input to tonight's adjudication and the rewritten distribution.
- Feeds tonight's (6/10 EOD) re-adjudication + the written scenario distribution (KB row, KB-VIO-052 precedent), per Orch/Will verdict. Distribution to be written **decomposed**: P(fade | Iran stabilizes) × P(Iran stabilizes) [Iran prior: unowned working assumption unless HAWK has a read], with the right-side buckets re-weighted per this cut.
- Anchor-naming rule → METRIC SEMANTICS (MEMORY.md) at next MEMORY pass.
- KB rows to log at EOD write-back: this cut + the anchor-inconsistency catch + the max-over-fire-days construction note (KB-VIO-079 amendment candidate: the canonical table should state its episode-hit construction inline).
