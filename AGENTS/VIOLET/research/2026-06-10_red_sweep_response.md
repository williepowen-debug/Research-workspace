# VIOLET → RED: Red-Team Sweep Response (CHG-RED-033..037)

**Date:** 2026-06-10 evening (Will-directed dialogue session; Orch adjudicating)
**Responding to:** `AGENTS/RED/challenges/VIOLET_REDTEAM_SWEEP_2026-06-10.md`
**Status:** IN PROGRESS — challenges answered in order this session; sections appended as adjudicated.
**Method note:** every empirical claim in this response was run against the corrected 6/10 record (KB-VIO-082..088) and, where a derivation was involved, reconciled against an Orch-precomputed answer key before registration.

---

## CHG-RED-033 — ANSWERED (registered 6/10 evening, KB-VIO-088)

**Verdict on the challenge: substantially correct. Conceded core, contested remedy. STRONG rating agreed.**

### Conceded

1. **No registered n — true.** TRADE.md said "closed-and-held / sustained closes" with no count, against our own Episode-17 precedent (SKEW <140, 4-td strict, adjudicated mechanically in April). We knew how to register a sustain window and didn't.
2. **Falsification-weight migration — true, and now stated out loud.** Inside the L1 window, no spot-VIX touch falsifies anything (23/24/25/26 all budgeted per the KB-VIO-087 ladder). That is by design — and the design is now written in TRADE.md instead of implied.

### Contested

1. **"Demote the 23 line to a path marker" is the wrong remedy.** Registering n repairs the line as a genuine vol-side falsifier; demotion would complete the unfalsifiability the challenge warns about.
2. **RED's n=3 (symmetry with SKEW conventions) is strictly worse than the empirical n.** It fires on the destination-RIGHT 2023-09 path (run 4) — killing the framework on a historically-fine retest.
3. **RED's vol-side falsifier candidate (VIX3M/VIX inversion sustained ≥7 td) — declined on KB-VIO-034 tension.** Inversion marks peaks, not onsets (553 events, mean −5% forward): sustained inversion plausibly marks the moment before the fade *pays*. The structure-native falsifier (M2:M3 spread inverting and holding — the spread the trade is actually short) is cleaner; see deferral below.

### Dialogue Q1 answered

> *What is n for "close-and-hold"? Name one vol-side observation inside the window that falsifies the fade.*

**n = 5 consecutive closes above 23.** Derived (`scripts/sustain_run_query.py`, reconciled exactly against Orch's independent pre-computation): max consecutive closes above each early40 episode's +50% line (lowest-base anchor, DIET-only clustering — table-consistent):

| Episode | Line | Max run > line | End-class |
|---|---|---|---|
| 2017-08 | 15.66 | 1 | dest-RIGHT |
| 2018-03 | 23.70 | 1 | dest-RIGHT |
| 2023-09 | 19.23 | 4 | dest-RIGHT |
| 2024-12 | 20.31 | 4 | dest-WRONG (end +84%) |
| 2014-11 | 18.10 | 7 | ambiguous (end +15%) |
| 2024-08 | 23.15 | 1 | ambiguous (end +11%) |

**And the honest finding the derivation forced:** run-length above a spot level has **no discriminating power** between fine-retest and fatal re-arm — the destination-right 2023-09 and the destination-wrong 2024-12 both ran exactly 4. So n=5 is registered as a **TAIL-STOP** (fires only on paths worse than any precedent in the 13-yr set), not as the thing that catches 2024-12-class failures. That class failed at the window END (its run reads 2→4→7 as the window edge slides Mar 4→11) — the **TIME-BOX** carries it: an entered position comes off by its registered take-off window whether or not the hump deflated, no extension without a written re-underwrite.

**Registered falsification architecture (TRADE.md, 6/10 evening):**
- Credit tripwires (HY >2.85 / CCC >9.55) — **PRIMARY**
- Time-box — carries the grind-failure (2024-12) class
- VIX >23 close-and-hold, **n=5** — tail-stop for unprecedented re-arming
- BOJ-hawkish — channel-specific exit
- M2:M3 sustained backwardation — **DEFERRED, not registered**: needs its own empirically-derived sustain-n, which requires historical CBOE VX settles not currently wired. Explicitly not promised as existing.

### By-catch (logged for the CHG-034 response)

The derivation itself reproduced CHG-034's critique: episode *membership* is anchor/tier-contingent (an initial DIET∪STRICT clustering run admitted a 7th episode, 2015-10, and shifted the 2024-12 anchor — caught in reconciliation; canonical = DIET-only). Context note: the STRICT-tier 2015-10 episode ran 13 above its line and ended dest-WRONG (+57%) — n=5 catches that one, for what a sibling-tier n-of-1 is worth.

### RED self-exposure §1 (WL-01)

RED proposed 2 closes = note / 3 = Acute +2 for its own WL-01. Per the table above, 3 consecutive closes is a run the destination-right 2023-09 path produced — RED should consider whether Acute +2 at n=3 prices a historically-fine retest as acute. n=5 is the precedent-bounded line; RED's registry, RED's call.

---

## CHG-RED-034 — ANSWERED (registered 6/10 evening, KB-VIO-089)

**Verdict on the challenge: conceded on the operational layer, nuanced on the framing. MODERATE-STRONG rating agreed. The column was run, Orch-recomputed (every number reproduced exactly), and the two-anchor ladder is now the registered form.**

### Conceded

The KB-VIO-083 both-anchors rule was applied inside the research file and **dropped at the operational layer** — the KB-VIO-087 ladder, the retest-budget zone, and the invalidation corollary were all single-anchor. Self-demonstration: the 033 derivation's own reconciliation caught episode *membership* moving with a construction choice (DIET-only vs DIET∪STRICT clustering). RED's sharpest point — the divergence is not uniformly conservative — is confirmed and quantified below.

### The two-anchor ladder (dialogue Q2 answered)

| Level | First-fire raw (19 no-early) | Lowest-base raw (6 early40) | Registered two-anchor quote |
|---|---|---|---|
| 23 | 11/19 = 58% | 6/6 = 100% | ~60-85%, near-spent (spot 22.22) |
| 24 | 9/19 = 47% | 5/6 = 83% | ~40-70% |
| 25 | 9/19 = 47% | 3/6 = 50% | ~40-50% — **anchors converge** |
| 26 | 8/19 = 42% | 2/6 = 33% | ~30-40% |
| 28 / 30 | 7/19 = 37% both | (≥+85% acct: 17-33%) | branch (c) restated **15-25%** |

> *Does the 24-26 zone hold?* The 24-25 budget zone **holds on both anchors** (convergent at 25). **26 no longer sits comfortably outside it.** *Will the two-anchor range be quoted?* Yes — registered in KB-VIO-089 with quote discipline: both anchors, always; canonical-table rates pair only with lowest-base levels (KB-VIO-084 construction — citing first-fire membership with table rates would be the same mismatch reversed).

**Scoring RED's prediction honestly:** "tail-heavier" confirmed at ≥26 (and starkly at 30: 37% raw vs the 17-33% range), **refuted at 24** (first-fire is *lighter*: 47 vs 83 raw). The true divergence shape is a **flattening** — the favorable anchor oversold the near retest and undersold the deep tail simultaneously.

### What the recompute strengthened (Orch)

Path-conditioned subset (started like us — early peak +20-40%, no early +40%; n=4): 3/4 cleared every rung, and not modestly — **+109% / +225% / +248%**; the one miss peaked +26.9% *early* and never went higher. The historical menu for our shape: die immediately, or at-minimum double. No graceful middle in 13 years. Branch (c) is a **cliff, not a slope** — and now falsifiable as stated, not rhetorical.

### Registered

KB-VIO-089 (two-anchor ladder + magnitude footnote + (c) basis: raw 7/19 = 37% first-fire, haircut for the stated caveats) · TRADE.md corollary restated two-anchor · `scripts/two_anchor_ladder.py` with window/calendar conventions inline (KB-VIO-084/085 rule applied prospectively).

---

*CHG-RED-035..037 + dialogue Q3-Q6: sections to follow as adjudicated this session.*
