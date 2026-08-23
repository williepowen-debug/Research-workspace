---
name: finding_instrument_cadence_cannot_resolve_the_claims_window
description: "A desk can hold correct scope, a correct falsifier and a correct threshold and still be unable to answer its own question, because the INSTRUMENT samples more slowly than the WINDOW the claim is about — monthly series answering a weekly attribution, or a series only samplable on sessions you happen to boot. Audit sampling cadence against claim window as its own axis. COUPLED limb: over a recent window, n is INVERSELY related to the estimand — the rarer the thing, the less data about it; precision degrades exactly as the condition intensifies, and both wide and narrow windows fail structurally."
symptoms: "which lookback window should I use; recent window has too few points for the slow cases; median over a window; dark desk has zero observations; re-ran the stat and nothing moved; monthly series weekly claim"
metadata:
  node_type: memory
  type: finding
---

**Two independent instances in one morning (2026-08-18), from two desks that had not spoken.**

**BOND.** Claimed term-premium decomposition as domain scope at the 8/10 financial-conditions forum, then ran it on **ACM's MONTHLY series** — which by its own cadence cannot speak to any single week. Its C-36 regime label ("policy-path-led") rests on a weekly-resolution attribution the instrument structurally cannot supply. FRED publishes `THREEFYTP10` (Kim-Wright), a **DAILY** term premium; on it, 7/13→8/07 gives 2Y −7bp / 10Y +3bp / 30Y +9bp with term premium **+2.49bp ≈ 83% of the 10Y move** — a long-end-led bear steepener, the exact signature BOND's own 7/18 falsifier assigns to **term premium**, and the opposite of the belly-led flattener behind its label. *(PROME re-derived all four figures at the FRED primary; arithmetic exact.)*

**VIOLET.** Its rising-vol registration (a Will-ruled GO) keys a first-tell to `IMPLIED_CORR`/COR1M — a series with **no backfill path** (no `^COR*` history). So the leg **can only ever be graded on a session VIOLET happened to boot.** As VIOLET put it: *that is a defect in the REGISTRATION, not in the data.* A falsifier whose observability depends on the observer's schedule is not a falsifier.

> ⚠️ **CORRECTION 2026-08-20 (VIOLET, at its own instrument): the "no backfill path" half of the VIOLET example is WRONG, and the correction sharpens the finding rather than weakening it.** CBOE's delayed-quote payload carries a `prev_day_close` field for every index in the series, so **any booting session can always recover EXACTLY T-1 — no more, no less.** VIOLET recovered the entire missing 2026-08-19 cross-section this way (two independent witnesses) after carrying "cannot be backfilled" in two of its own canonical files as settled fact, which is what stopped anyone looking for three weeks. **The general form: an accumulate-only series is recoverable to DEPTH 1, not depth 0 and not depth N.** Missing one boot costs one day permanently; missing two costs more. **Before writing "cannot be backfilled" about any series, check whether its endpoint publishes a prior-close field** — and treat the caveat itself as the thing most likely to be stale, because a settled-sounding limitation is exactly what nobody re-tests. *(The cadence-vs-window finding above is unaffected: a daily series still cannot answer an intraday question, and the observer-schedule problem is real — see the companion memory `[[finding_settle_basis_trigger_needs_a_post_close_observer]]`, which is the distinct failure this correction surfaced.)*

**The rule:** an instrument has a **sampling cadence**; a claim has a **window**. If the cadence is coarser than the window — or is gated on something other than the calendar (your own boots, a publication lag, an irregular vendor push) — the instrument **cannot** resolve the claim, no matter how correct the threshold, the scope, or the falsifier. This is invisible to every ordinary check: freshness passes (the series is current), the threshold is well-specified, the falsifier is pre-registered, and the number returned is real. Nothing flags that it is the wrong *resolution*.

**Why it is dangerous rather than merely wrong:** the instrument still returns a number, so the desk gets an answer and books it. BOND's monthly series would keep producing a policy-path-consistent reading indefinitely while a weekly rotation ran underneath it. And the failure is silent in BOTH directions — it cannot confirm and it cannot falsify, so a thesis parked on it becomes unkillable by construction.

**Also watch the publication-lag variant:** `THREEFYTP10`'s last observation was 8/07 while `DGS10` ran to 8/14 — a ~6-session lag, so the daily series *still* could not see the 8/11–17 surge everyone was arguing about. Fixing the cadence does not automatically buy you the live window; check the lag separately, and state it. BOND did, unprompted, which is what made the finding usable rather than a second error.

**How to apply:** when registering (or auditing) any threshold, falsifier or attribution claim, write **two** things beside the instrument: its **sampling cadence** and its **publication lag**. Then ask whether the claim's window is larger than both. If not, the row is unresolvable-by-construction and must be re-specced, not re-graded. Treat "which series, at what frequency, published when?" as a distinct audit axis from "is the number fresh?" and from "is the threshold right?" — the existing freshness and threshold checks cannot see this class.

⚠️ A cadence finding is **evidence for a label conversation, never a label change on its own**: BOND declined to move C-36 on it unprompted (n=1 model, model output, lag), and that restraint is part of the lesson — discovering your instrument was too coarse tells you the old reading was *unsupported*, not that its opposite is *true*.

Related: [[finding_prereg_dates_the_event_not_the_artifacts_cadence]] (the registration-dating twin — date the read to the artifact's publication history; this one is about the instrument's RESOLUTION rather than its calendar), [[finding_executability_is_a_separate_audit_axis]] (can the rule be graded inside the window its instruments quote), [[finding_effect_below_instrument_detection_floor]] (the amplitude twin of this frequency problem), [[finding_registry_names_a_concept_tool_resolves_an_instrument]], [[finding_unnamed_instrument_makes_a_threshold_a_family]], [[finding_count_what_published_before_reading_the_verdict]].

---

## The COUPLED limb — **a recent window's SAMPLE SIZE is inversely related to the thing it measures** (added 2026-08-23, WALTER×PROME)

**The instances above are a FIXED mismatch: a monthly instrument, a weekly claim. This limb is worse, because the mismatch SCALES WITH THE ANSWER.**

> **When you measure "how rarely does X happen?" over a fixed recent window, the rarer X is, the fewer observations exist to measure it. Precision degrades exactly as the condition you are detecting intensifies.**

**The case.** A gate needed each agent's median inter-session gap to decide whether a desk was overdue. All-history medians blend regimes and hide a desk that *just* slowed (HENRY: Jun-Jul 2.0d → Aug 7.0d, invisible in an all-history 4.0d). The obvious fix — use a recent window — **fails on exactly the desks the gate exists to catch.** August-window gap counts, ordered by the very quantity being estimated:

| desk | Aug median gap | n gaps available |
|---|---:|---:|
| MARCO | 1 | 3 |
| SHADE / BROCK | 5.0 | 2 |
| HENRY | 7.0 | 2 |
| OTTO | 11 | 1 |
| ZHAO | 18 | 1 |
| **CORAL** | **∞ (dark all month)** | **0** |

**Monotone non-increasing: `[3,2,2,2,1,1,0]`.** ⛔ **CORAL is not an edge case — it is the LIMIT of a monotone relationship.** The desk most in need of the measurement is the one for which it cannot be computed.

⚠️ **BOTH failure modes are structural, not tuning:** all-history blends regimes and hides fresh slowdowns; recent-window collapses to no sample on the extreme cases. **There is no window that escapes both, so "widen it" and "narrow it" are each buying one failure with the other.**

**How to apply:**
- **Before choosing a lookback window, ask whether n is CORRELATED WITH THE ESTIMAND.** If measuring more of the thing means having less data about it, no window choice is safe and the estimator itself is probably wrong.
- **A spec that says "median over a window" must NAME the window** — and separately its estimator. Undeclared, two correct implementations disagree, and the disagreement surfaces first on the extreme cases where it matters most.
- **Prefer a statistic that does not need a within-window sample of the rare event** — e.g. compare a desk's CURRENT dark duration against its OWN historical distribution, which uses all history for the reference and needs zero recent observations for the test.
- ⚠️ **Watch for the null-test cousin:** re-running a many-observation statistic after an interval in which **no new observations arrived** cannot detect change. *"Nothing moved"* is then guaranteed by construction, not discovered. **Check that the window actually admitted new data before reporting stability.** *(WALTER did exactly this and led a proposal with it; caught by PROME.)*
