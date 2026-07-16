# DEWEY → PROME: Prompt 12 PARKED — decision anchors resolved, needs re-write

**Date:** 2026-07-16 | **From:** DEWEY | **To:** PROME (cc WALTER)
**Re:** `REQ-DEWEY-20260702-008` / `DEEP-RESEARCH-PROMPT-12-mechanical-selling-stack.md`
**Disposition:** **PARKED, not consumed** — left state=NEW in `inbox/WALTER/`, NOT moved to `processed/`.
**Will's call (2026-07-16):** park 12, proceed to prompts 15/16/17.

---

## Why

Prompt 12 was written 2026-07-02 with `deliver_by: 2026-07-10`. Reached at 7/16. Re-verified its
premises against live state at intake (queue-freshness rule) — **two of its three DELIVERABLE FEEDS
resolved before the run started:**

| Prompt premise | Live state (verified 7/16) | Source |
|---|---|---|
| "arming or de-arming **HEN-35**'s 30% cascade path" (decision question) | **HEN-35 GRADED MISS** — VIX never neared 23 (July max 18.91); cascade dead on literal terms; mechanism carried to HEN-36 (FCF gate 7/29-31) | `AGENTS/HENRY/STATUS.md` 7/16 ~09:35 ET; `HENRY/LAST_COMPLETION.md` |
| "**VIOLET** tail-hedge sizing (gate armed, **KB-VIO-110**)" | **KB-VIO-110 SUPERSEDED / LAPSED** (Will's 7/9 disposition, not retro-built). A future hedge would be **rates-vol-shaped (TERRY), not VIX-calls** | `AGENTS/VIOLET/STATUS.md` 7/9 + 7/11 |
| "(2) current SPX dealer gamma-flip level … cross-check HENRY's ~7,448" | **Will DECISION 7/16:** accept the free-tracker estimate + its error bar (no subscription); refine from broker SPX-OI screenshot on decision days. Flip has migrated to **~7,530-7,545** | `AGENTS/HENRY/STATUS.md` 7/16 |

Third feed (KOSPI 8,200 re-contagion weight) not separately verified — parked with the rest.

Running the 5-angle harness (~4M tokens) against a resolved prediction and a lapsed gate would have
been a large spend with no live consumer. Flagging rather than silently re-scoping: **the re-anchor
is PROME's call, not DEWEY's** — I find data, I don't re-decide what the fleet is asking.

## The residual IS live — recommended re-write

The underlying question survives; **its consumer changed.** HENRY 7/16: SPX **7,544 straddling** the
migrated-up flip in a **negative-gamma regime** (dealers amplify), put wall 7,500 / call wall 7,600 →
**"cushion THIN"** into **GOOGL 7/22 · FOMC 7/28-29 · mega-tech 7/29-31**. VIOLET's **F2 gate** is
explicitly **GAP-flagged** pending exactly this. Suggested re-anchor if PROME re-issues:

- **Decision question →** *how thin is the mechanical cushion into the 7/22-7/31 earnings cluster,
  given SPX straddles the flip in negative gamma?* (feeds **HEN-36** + **VIOLET F2**, not HEN-35.)
- **Leg 1 (CTA trigger levels) — KEEP, high value.** `HENRY/workbook/FLOW.tsv` levels
  (6,707/6,494/6,902/6,800) are ~800pts stale and self-flagged *"do NOT cite as current."* Where
  mechanical selling begins **below 7,544** is the live question.
- **Leg 4 (levered-ETF $464bn vs GS ~$84bn + Korea FSS) — KEEP, high value.** A durable factual
  dispute, unaffected by HEN-35's grading. Genuinely fan-out-shaped (source discovery).
- **Leg 5 (0DTE share) — KEEP, cheap.** CBOE primary = DEWEY direct pull, not the fan-out.
- **Leg 3 (vol-control AUM / VIX-23-vs-realized keying) — MEDIUM.** Threshold moot at VIX 16.17, but
  *which variable it keys off* is durable for any future cascade.
- **Leg 2 (gamma flip) — DROP.** Will already ruled the exact level not worth buying; DEWEY would only
  re-derive the free-tracker read he accepted.

## Pattern note (bigger than this prompt)

This is the **second** Batch-2 prompt to need an intake re-anchor (cf. 7/10 prompt 08, and the 7/9
prompt 10 energy-HY reframe). Batch-2 prompts carry **baked-in urgency framing that rots** — the
prompt's own `deliver_by` is the tell. Suggest PROME **re-sort + re-verify anchors** on the remaining
queue (15/16/17) before DEWEY reaches them, or mark prompts with the prediction/gate ID they feed so
a resolved anchor is detectable without a full state read. `[[finding_deep_research_stale_vintage_headline]]`
