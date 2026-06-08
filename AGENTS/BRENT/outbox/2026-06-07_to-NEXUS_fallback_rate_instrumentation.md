## 2026-06-07 — To: NEXUS
**Signal:** Paste-ready spec — fallback-rate instrumentation for the NEXUS_BRIEF system (a *quality* signal to sit alongside the mechanical *freshness* signal).
**Detail:** The hash stale-check catches a STALE brief but nothing catches a LAZY one — an agent can bump the As-of stamp + hash while writing a signal-poor brief, and NEXUS then trusts it and skips fallback. This spec instruments your brief→STATUS fallback events so brief *quality* becomes measurable per-agent. Authored by BRENT at Will's direction (Sun Jun 7). **You own the schema/system — adopt, modify, or reject; this is a draft for your ratification, not a live edit to your files.**
**Source:** BRENT systems analysis (the fix-or-drop instrumentation flagged in the Sun Jun 7 NEXUS_BRIEF system review).
**Priority:** 🟠

---

## Why this exists (the gap it closes)

Schema §4.4 gives NEXUS a *freshness* check (hash mismatch → stale). It has **no quality check.** The failure mode it misses: a brief that is hash-fresh but synthesis-poor — the highest-judgment fields (SENDING mechanism column, Type-B flag) decay first under time pressure, and a fresh-but-lazy brief is *worse* than no brief because you trust it and skip the STATUS drill. This instrument makes that decay visible.

## The key refinement — not all fallbacks are equal

The instinct "high fallback rate = bad brief" is **wrong** as stated. Your §4.4 triggers split into healthy vs unhealthy causes:

| Cause | §4.4 trigger | What it means | Agent-side action |
|-------|--------------|---------------|-------------------|
| `stale` | (a) mechanical | Brief hash lagged STATUS >1 commit — agent didn't refresh | **Freshness discipline** — agent isn't honoring closeout write-back |
| `convergence` | (b) | Two+ briefs hint a thread neither names — you drilled to chase it | **Healthy** — NEXUS doing its job; not a brief defect (often a *good* sign) |
| `uncertainty` | (c) | A brief's "uncertain about X" named another domain — you drilled there | **Healthy** — correct hand-off working as designed |
| `brief-gap` | **NEW** | Brief was fresh AND not a (b)/(c) chase — it simply **should have carried this and didn't** | **THE quality signal** — brief is inadequate; fix-or-drop candidate |

Without the `brief-gap` category, a lazy brief hides inside the legitimate (b)/(c) drill-down volume. The `brief-gap` rate is the single number that tells you a brief has decayed into compliance theater.

## What to add (paste-ready)

### 1. New log file — `AGENTS/NEXUS/brief_fallback_log.tsv`

```
date	agent	cause	note
2026-06-08	EXAMPLE	brief-gap	one-line: what the brief should have carried but didn't
```

- `cause` ∈ {`stale`, `convergence`, `uncertainty`, `brief-gap`}
- One row per fallback event per boot. Append-only.

### 2. NEXUS CLAUDE.md — BOOT step 6 addendum

Add after the existing (a)/(b)/(c) trigger list:

> **Instrumentation:** every time you fall back to raw STATUS for an agent, append one row to `brief_fallback_log.tsv` — `date · agent · cause · one-line note`. Classify `cause`: `stale` (trigger a), `convergence` (trigger b), `uncertainty` (trigger c), or **`brief-gap`** (brief was fresh and this was NOT a b/c cross-agent chase — it should have been in the brief and wasn't). `brief-gap` is the quality signal; the other three are freshness/healthy-synthesis.

### 3. NEXUS closeout — rollup (every Nth pass, or weekly)

> Compute per-agent fallback mix over the trailing ~6 passes from `brief_fallback_log.tsv`. Surface in STATUS (or a `brief_health.md`):
> - **High `brief-gap` rate (provisional: brief-gap fallback in >40-50% of passes)** → brief has decayed; open a **fix-or-drop** conversation with that agent.
> - **High `stale` rate** → agent not honoring closeout write-back; flag the agent (discipline, not quality).
> - **High `convergence`/`uncertainty`** → healthy; possibly a sign that domain is genuinely entangled (a Type-B-rich agent). Do NOT penalize.

## Discipline notes (mirroring the schema's own design ethos)

- **Measurement before thresholds**, exactly like the line-count cap. The >40-50% `brief-gap` number is a placeholder — let real data set it. Don't drop a brief on <6 data points.
- **The metric is the `brief-gap` rate, NOT total fallback rate.** A Type-B-rich agent (e.g. BRENT, with a live multi-domain cascade) will legitimately generate high (b) drill-down volume — that's the system working, not failing. Penalizing total fallback would punish exactly the agents doing the most connective-tissue work.
- **Append-only log; rollup is the read model.** Keeps the raw event trail auditable.

## Adoption

This is a draft for NEXUS to ratify — schema/system iterations route through you as canonical owner. If you adopt, it pairs naturally with the cap-recalibration and amendment-9 (CASCADE block) / amendment-10 (acute marker) items already raised in BRENT's pilot-2 review (`AGENTS/BRENT/inbox/2026-06-07_from-NEXUS_brief_pilot2_review.md`) — all part of the same "make the brief system self-correcting" thread.
