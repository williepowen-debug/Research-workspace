---
signal_id: SIG-W-20260626-021
dispatched: 2026-06-26T23:39:00Z
origin: Will-Telegram image batch 2026-06-26 (re-send, 6/24-dated) — Daily Chartbook (GS CTA estimates)
source: Goldman Sachs CTA flow estimates in S&P 500 (via @dailychartbook)
signal_type: data-release
domain: MARKET_VOL
cluster: POSITIONING_VALUATION
cluster_secondary: n/a
signal_role: primary_substance
narrative_channel: n/a
precedence: PRIORITY
to: HENRY
info: [TERRY, RED]
confidence: 0.70
verify_verdict: SKIP-VERIFY 0.70 — GS CTA model estimates (objective desk output); ~2d stale, so the WEEK/MONTH flow magnitudes are decayed (CTA estimates re-run daily). The asymmetry STRUCTURE + the SPX pivot levels are the durable read.
verify_method: none (GS model estimates; HENRY/TERRY weight).
routing_note: CTA positioning/flow + SPX pivot levels → HENRY action (index-flow mechanics). TERRY info (positioning/timing — pivots + flow-asymmetry inform entry/expiry/sizing per ROUTING_TABLE v0.13). RED info (cluster). cluster POSITIONING_VALUATION. Flow #s decayed; pivots durable.
---

# GS CTA estimates — flat/up modestly bid, but a down-tape unloads ~$40bn over 1mo; SPX pivots 7352/7063/6642 (HENRY)

**One line:** Goldman's CTA flow model (as of 6/24): **over the next month — flat tape +$2.69bn, up tape +$6.68bn, but DOWN tape −$40.45bn** (the classic asymmetric trigger structure — CTAs are long and would have to dump on a break). Key SPX pivot levels: **short-term 7,352 / mid-term 7,063 / long-term 6,642.**

> **GRADE: SKIP-VERIFY 0.70, primary_substance.** GS desk model; ~2d stale so the precise week/month $ are decayed (re-run daily) — but the **down-tape asymmetry** (−$40bn on a break vs +$6.7bn on a melt-up) and the **pivot levels** are the durable, actionable read.

## Per-recipient genuine delta

### → HENRY (ACTION) — the CTA asymmetry + pivot map
The structure: CTAs are positioned long enough that a flat/up tape adds little (+$2.7-6.7bn) but a **down tape forces ~$40bn of selling over a month** = the mechanical accelerant under a break. Pairs your dealer-gamma/0DTE mechanics — the pivots (7,352 short / 7,063 mid / 6,642 long) are the levels where the CTA flip compounds a selloff. Note staleness: re-pull the current GS CTA estimate before acting on the exact $ (the pivots move slower).

### → TERRY (INFO)
Directly your lane: the SPX pivot ladder (7,352 / 7,063 / 6,642) + the down-tape CTA asymmetry inform entry/expiry/sizing on any index or semi short — a break below the short-term pivot opens the mechanical-selling window; sizing should account for the squeeze risk on an up-tape (CTAs add little, so less fuel for a squeeze from them). Flow #s ~2d decayed; the structure holds.

### → RED (INFO)
Cluster/counter: CTA positioning is a mechanical-flow read, not a fundamental one — the −$40bn down-tape is conditional on a break that hasn't happened (index near highs, VIX 18). The asymmetry is a known late-cycle feature; weigh as accelerant-if-triggered, not a standalone bear signal.

## Sources
- Daily Chartbook (@dailychartbook, X) ~6/24/26 — "GS CTA Estimates in S&P 500." US estimates — over next 1 week: flat −$201mm / up −$840mm / down −$1.16bn; over next 1 month: flat +$2.69bn / up +$6.68bn / down −$40.45bn. Key SPX pivot levels: short-term 7,352 / mid-term 7,063 / long-term 6,642. (Chart window 22Dec2025–22Jul2026; GS model, illustrative.)
