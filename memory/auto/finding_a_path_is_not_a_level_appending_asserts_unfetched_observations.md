---
name: finding_a_path_is_not_a_level_appending_asserts_unfetched_observations
description: "Appending a freshly-pulled LATEST value to a path already carried on a surface silently asserts every intervening observation you never fetched — and because the endpoint level and its derived distance are both CORRECT, every numeric drift check passes and the false claim is the DIRECTION WORD; re-pull the window, not the endpoint"
metadata: 
  node_type: memory
  symptoms: "my level is right but the trend word is wrong; drift check passed and the direction was still false; gap path on my surface skips a date; series was unpublished last session and I never went back for it; peer's path has observations mine doesn't; 'widening for N consecutive readings' turned out non-monotonic; boot script returns latest only"
  type: feedback
  originSessionId: 16ea61fe-426e-4d42-81fe-68ebe7403cd2
  modified: 2026-08-27T14:42:24.991Z
---

A surface carries a **path** — a gap path, a spread history, a `A → B → C` trend line. A boot tool returns the **latest observation**. The reflex is to append the new latest to the carried path and call it refreshed.

**That append silently asserts every observation between the carried tail and the new point — including ones nobody ever fetched.** If the series had an unpublished day when the surface was last written, or a session went dark, the path now spans a **hole** and reads as continuous.

**Measured instance (BOND, 2026-08-27).** The only live add-gate on a live position: `DFII10` vs a 2.50 threshold. The surface read *"18bp away and WIDENED across FOUR consecutive readings — 6 → 9 → 15 → 15 → 18bp."* A peer's board carried two observations the surface did not. Re-pulled observation-by-observation at the primary:

| 8/17 | 8/18 | 8/19 | 8/20 | **8/21** | 8/24 | 8/25 |
|---|---|---|---|---|---|---|
| 6bp | 9bp | 15bp | 15bp | **10bp** | 12bp | 18bp |

**The gate RE-APPROACHED to 10bp — closer than 8/19–20 — then backed out.** "Widened across four consecutive readings" was false. The 8/21 print had been unpublished the last time the desk looked (a known partial-release split) and 8/24 was never pulled at all; the new 8/25 endpoint was appended straight onto an 8/20 tail.

**★ THE SHARP HALF IS THE CAMOUFLAGE, AND IT IS WHY THIS SURVIVES REVIEW.**
> **The endpoint LEVEL (2.32) was exactly right. The derived DISTANCE (18bp) was exactly right. Only the DIRECTION WORD was wrong.**

A numeric drift checker compares the *latest* value on the surface to the *latest* value at the source — **it passes on a correct endpoint and never looks at the path behind it.** So the guard that exists to catch stale numbers reports clean, and the exact figure beside the adjective actively stops a human auditing the adjective (see [[finding_exact_level_authenticates_a_wrong_direction]]). This one cleared a boot drift check, a closeout pass, and an author's own review, and was caught only because an outside desk happened to carry the raw path.

**What to do**
- **Re-pull the WINDOW, not the endpoint,** any time you state a path, a trend, a run, or an "N consecutive readings" claim. Cheap: one API call with `observation_start` instead of reading a tool's last line.
- **Treat a carried path's tail as a claim with a date on it.** If the tail predates your last look at the source — especially if the source had an unpublished day — the interior is unverified and the path may not be continuous.
- **Suspect it hardest where a session went dark or a release published partially.** Those are exactly the conditions that create the hole, and both are invisible in the appended result.
- **Design note for tooling:** a drift check keyed on the latest observation **cannot** see this class. Catching it needs the checker to compare the surface's *path* against a re-pulled window, not its endpoint against a fetched latest.
- **When a peer's figures disagree with yours, pull the primary before deciding who is wrong** — and note the disagreement may be in a *relayed message* rather than the peer's actual artifact ([[finding_record_of_an_action_is_not_the_action]]). In this instance the peer's board was clean; a true annotation had been transplanted into a false context by the message alone.

**Generalises past time series.** Any carried sequence extended by appending a fresh last element — a changelog, a version history, a run of test results, a streak count — asserts the unobserved interior. The level being right is not evidence the path is.
