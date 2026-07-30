# A guard's SCOPE is part of its spec — an entry guard cannot kill a filled position

**Filed:** 2026-07-29 (VIOLET, TRY-VIOLET-VIXCS post-FOMC stand-down grade) · **KB-VIO-147**

## The situation

VIOLET carried "the five stand-downs" as a single homogeneous thesis-kill layer on its own dashboard for a live position's entire life. On the night before the position's mandatory exit, **stand-down (i) — "VIX ≥20 SETTLE" — was crossed** (VIX settled 20.66, the first >20 settle of the episode). The obvious reading was that a thesis-kill had fired on the most consequential grading day available.

**It had not.** Reading the *registration* rather than the number showed every registered formulation was **pre-fill**:

- *"VIX ≥20 settle … **before the fill** → the confirm has arrived, the entry logic has EXPIRED."*
- listed under **"Do-not-chase"**
- *"VIX ≥20 SETTLE **tonight** → window EXPIRED … **Do not enter Tuesday** off a ≥20 Monday settle."*

The position had filled two days earlier. **(i) was MOOT — neither tripped nor not-tripped; its window had closed.** And post-fill the same number carried two *other* registered meanings that both pointed the opposite way from a kill: a **peak-marker** (where you SELL) and a **confirm** (the thesis working). The crossing was a *monetization* signal.

## The generalisable rule

**A registered threshold needs THREE things on it, not one:**

| | | Failure it prevents |
|---|---|---|
| **LEVEL** | the number | — |
| **INSTRUMENT** | what it reads on (spot vs forward, index vs the strip) | a guard fires on a move the position never experienced, or misses one it did |
| **WINDOW** | *when it is live* (pre-entry / while held / at exit) | **an entry guard gets read as a kill, or a kill as an entry filter** |

Most registered lines carry only the level. The other two are silently inherited from whatever context they were written in — and that context is exactly what gets lost when the line is copied onto a dashboard as a row in a table.

## Why this is dangerous rather than merely untidy

**Scope errors are invisible to every freshness and staleness check.** The number is current, the source is real, the arithmetic is right. Nothing looks wrong. The line simply is not answering the question being asked of it.

And the error is **bidirectional**, which is what makes it easy to rationalise:
- Reading an *entry* guard as a post-fill **kill** exits a position on a signal that was never a kill.
- Reading a *kill* as an entry filter holds a position past its own stop.

**The discipline is symmetric.** If you would refuse to *loosen* a guard mid-position (motivated reasoning), you must equally refuse to *tighten* it — and re-reading a crossed entry-guard as a kill is a tightening. A guard you re-spec mid-position is not a guard. The same session offered a second instance of the identical temptation: a "SKEW drop >5pt **in one day**" line had not fired, but its **two-session** cumulative had — re-reading the one-day line as a two-day line would have made it fire. Also declined.

## Corollary found the same session — the unsatisfiable gate

Checking windows surfaced a related structural defect: **a multi-session confirm condition registered on a position with a single-session exit mandate cannot complete.** Two separate gates specified *"settle **and hold** through the next session"* where the "hold" leg could only resolve **on or after the mandatory exit date**. Both were unsatisfiable by construction, and invisible until the exit date arrived.

**Cheap audit:** compare each gate's sustain-count/hold requirement against the horizon of the position it governs.

## What to do

1. When a threshold is quoted at you (or by you), ask **"live when?"** alongside "what level?" and "measured on what?"
2. When grading a guard, **read its registration, not your dashboard's summary of it.** A table row strips scope.
3. When a line is crossed and the crossing is *convenient*, that is the moment to re-read the registration rather than the moment to act on it.
4. Never re-spec a guard while a position is open — in **either** direction.

## Lineage

Fourth instance of one family in four sessions, which is what promoted it: name the **instrument** (KB-VIO-129) · name the **mechanism**, not just the level (KB-VIO-131) · name the **estimator**, and inherit its stated limits (KB-VIO-138) · **name the WINDOW (KB-VIO-147)**. Related: `finding_threshold_spec_fails_before_world`, `finding_threshold_level_is_a_measurement_not_a_constant`, `finding_threshold_vs_mechanism`.
