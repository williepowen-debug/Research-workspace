---
request_id: REQ-DEWEY-20260702-008
from: PROME (Will-directed batch 2026-07-02 — fleet-mined slate; WALTER logs + routes, see AGENTS/WALTER/inbox/2026-07-02_from-PROME_dewey-batch2-13-prompts.md)
to: DEWEY
created: 2026-07-02T04:00:00Z
revised: 2026-07-16 (v2 — PROME re-anchor per DEWEY's PARK note `AGENTS/DEWEY/outbox/2026-07-16_to-PROME_prompt-12-stale-anchored.md`, Will-approved same day. v1's consumers died: HEN-35 GRADED MISS 7/16, KB-VIO-110 SUPERSEDED 7/9, gamma-flip level Will-ruled 7/16 [accept free-tracker + error bar]. The underlying question survives; its consumers changed.)
state: NEW
flag_trigger: T3 (load-bearing-but-thin)
anchors_feed: HEN-36 (FCF gate, resolves 7/29-31) · VIOLET F2 (explicitly GAP-flagged pending this) · KOSPI 8,200 re-contagion weight (UNVERIFIED as anchor — re-check at intake per queue-freshness rule)
originating_evidence: "HENRY/workbook/FLOW.tsv CTA levels (6,707/6,494/6,902/6,800) ~800pts stale, self-flagged 'do NOT cite as current'"; SPX 7,544 straddling the migrated flip ~7,530-7,545 in NEGATIVE gamma (HENRY 7/16), put wall 7,500 / call wall 7,600, buyback blackout dark 7/14-7/31; $464bn levered-ETF figure UNVERIFIED; 0DTE share unsourced
clusters: AI/factor positioning unwind (M-09) / HEN-36 FCF gate / Path-B coiled spring
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv (same row as v1 — re-anchored, not a new request)
run_order: after 15/17 unless VIOLET F2 forces earlier (PROME call 7/16)
deliver_by: 2026-07-21 (GOOGL 7/22 opens the earnings cluster; FOMC 7/28-29; mega-tech 7/29-31)
---

# DEEP-RESEARCH PROMPT 12 v2 — Mechanical cushion into the 7/22–7/31 earnings cluster: CTA levels, vol-control keying, levered-ETF quantum, 0DTE share

**Decision question:** How thin is the mechanical cushion under SPX into the 7/22–7/31 earnings cluster, given SPX (~7,544) straddles the migrated gamma flip (~7,530–7,545) in a **negative-gamma regime** (dealers amplify) with the buyback bid dark 7/14–7/31? Feeds **HEN-36** (FCF gate 7/29-31) and **VIOLET F2** (GAP-flagged pending exactly this) — **not** HEN-35 (graded MISS) and **not** KB-VIO-110 (superseded; a future hedge would be rates-vol-shaped via TERRY, not VIX calls).

**Materiality gate:**
- **(a) What a cheap verify can't answer:** the load-bearing quanta live in different source families (desk estimates in press, CBOE primaries, FSS/KRX releases, academic/BIS work); none is a single series.
- **(b) Consequence:** replaces stale/unsourced rows (FLOW.tsv CTA levels self-flagged do-not-cite; FLOW-HEN-006 $200-400B/VIX-23 keying; $464bn levered-ETF; unsourced 0DTE share) with sourced values; sizes the mechanical-amplification term in HEN-36 and closes VIOLET F2's gap.

## Leg disposition (v1 → v2, per DEWEY's park note)

| Leg | v2 status | Why |
|---|---|---|
| 1 — CTA trigger levels | **KEEP — high value** | Where mechanical selling begins **below 7,544** is the live question; FLOW.tsv levels ~800pts stale |
| 2 — gamma flip level | **DROPPED** | Will ruled 7/16: accept the free-tracker estimate + error bar; refine from broker SPX-OI screenshots on decision days — do not re-derive |
| 3 — vol-control keying | **KEEP — scoped down** | Threshold moot at VIX ~16; *which variable it keys off* (VIX level vs 1m/3m realized) is durable for any future cascade |
| 4 — levered-ETF quantum | **KEEP — high value** | Durable factual dispute ($464bn vs GS ~$84bn), unaffected by HEN-35's grading; genuinely fan-out-shaped |
| 5 — 0DTE share | **KEEP — cheap** | CBOE primary = DEWEY direct pull, not the fan-out |

## `/deep-research` prompt (paste-and-go)

> Calibrate the SPX mechanical-selling cushion into the 2026-07-22 → 2026-07-31 earnings cluster (GOOGL 7/22, FOMC 7/28-29, mega-tech 7/29-31), with SPX ~7,544 straddling the dealer gamma flip (~7,530–7,545, free-tracker estimate — take as given, do NOT re-derive) in a negative-gamma regime and the buyback bid in blackout 7/14–7/31. Layer by layer, with sourced current values: (1) CTA sell-trigger levels and estimated unwind sizes for SPX (short/medium/long-term triggers) from Goldman Sachs, Nomura (McElligott), UBS, BofA, and Deutsche Bank (Thatte) flow-desk estimates as reported in press since 2026-06-01 — specifically, where below 7,544 does the first trigger sit and what sells there; (2) vol-control and risk-parity AUM currently allocated to US equities and WHICH variable de-leveraging keys off — a VIX level vs trailing realized vol (1m/3m) — with estimated $-selling per vol-point (the keying variable matters more than any threshold at current VIX ~16); (3) verified leveraged/inverse-ETF exposure to AI/semis in the US, Korea, and Taiwan — adjudicate the disputed ~$464bn US net-exposure figure vs Goldman's citable ~$84bn, size the Korean 2x KOSPI/semi complex (~$9B claim), and report the current status of any Korea FSS ruling/restriction on leveraged ETFs (re-verify the KOSPI 8,200 re-contagion anchor at intake before spending on this leg's Korea half); (4) the current 0DTE share of SPX options volume from CBOE primary data and any desk analysis of 0DTE's dampening vs amplifying role at the flip in negative gamma. IN-BOUNDS: desk research quoted in press, CBOE/exchange primaries, FSS/KRX releases, SpotGamma/Menthor-Q/UnusualWhales public shadows, academic/BIS work on vol-control flows. OUT-OF-BOUNDS: re-deriving the gamma-flip level (Will-ruled: free-tracker + error bar stands); re-deriving the AI-capex fundamental thesis (HEN-36 owns it); credit-market triggers (VIOLET tree owns); single-stock analysis; anything already in the 6/27 AI-circular-financing report. TIMEFRAME: values current as of July 2026; flag any figure older than 2026-06-01 as stale. DELIVERABLE FEEDS: HEN-36 mechanical-amplification term (resolves 7/29-31), VIOLET F2 gap closure, KOSPI 8,200 re-contagion weight (if the anchor still stands at intake).

**On return:** hand back to WALTER via `AGENTS/WALTER/inbox/DEWEY/` naming flag REQ-DEWEY-20260702-008 (v2); WALTER routes as a `research-output` signal (→ HENRY action / VIOLET co-action / PROME, TERRY, WALTER info) and closes the ledger row.
