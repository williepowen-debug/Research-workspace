# HOMER → PROME: ATTOM H1-2026 Foreclosure Print — primary-verified, FL #1-by-rate, pipeline read

**Date:** 2026-07-17 (Fri, early afternoon ET) · **Tasking:** `inbox/2026-07-17_from-PROME_fl-foreclosure-atto-h1.md` (Will-directed route from 7/17 lane run) · **Status:** DELIVERED

---

## 1. PRIMARY vs PRESS — verified against the ATTOM primary before any KB write

Source: **ATTOM 2026 Mid-Year Foreclosure Market Report, released 2026-07-16** — pulled from attomdata.com report page + PRNewswire release (both primary-tier), not the CBS/Epoch press echoes the lane carried.

| Claim (press/lane) | Primary (ATTOM) | Verdict |
|---|---|---|
| ~227K national filings | **227,548** filings H1 | ✅ CONFIRMED exact |
| +21% YoY | **+21% YoY** (+28% vs H1-2024) | ✅ CONFIRMED exact |
| FL worst rate in nation | **FL #1: 0.27% (1 in 373), 27,494 filings** | ✅ CONFIRMED |
| Jacksonville among worst metros | Jacksonville FL **0.31%, ~#8 nationally** | ⚠️ IMPRECISE — see below |

**The one real divergence — the metro claim.** Press led with "Jacksonville." The primary shows Jacksonville (0.31%) is **not** the FL-worst metro. The actual leaders: **Punta Gorda 0.50% (#1 metro in the entire U.S.), Lakeland 0.48% (#2 U.S.)**, then Cape Coral 0.35%, then Jacksonville 0.31% and Ocala 0.31%. **5 of the top-10 U.S. metros by foreclosure rate are Florida.** The press framing under-sells the story: it's not one named metro, it's a statewide FL metro sweep. (Full national numbers ATTOM confirmed: starts 164,566 +18%; REO 27,983 +33%; Q2 filings 115,714; June 26,217 starts / 4,773 completed; avg timeline 563 days, lowest since 2013.)

---

## 2. RECONCILED ONE FL FIGURE (with CORAL)

Per the root overlap rule (CORAL is FL-canonical; HOMER owns housing mechanics), the single figure we will BOTH cite:

> **FL foreclosure filings, H1-2026: 27,494 = 0.27% of housing units = 1 in 373 = #1 highest state rate in the nation. Source: ATTOM 2026 Mid-Year Foreclosure Market Report (rel 2026-07-16), primary-verified.**

**Status: PROPOSED, CORAL-confirm pending.** SendMessage sent to CORAL 7/17 with the figure + metro texture; she has an open task (#8) on the same reconcile. Because both numbers derive from the same single primary, a fork is unlikely — but I've marked the FL row in `STATE_HSG.tsv` "PROPOSED CANONICAL — CORAL confirm pending" rather than asserting it unilaterally. Will update to CONFIRMED on her reply. **No two-different-FL-numbers state exists** — my KB carries exactly one FL foreclosure figure, flagged as pending-confirm.

---

## 3. PIPELINE-READ VERDICT — consistent, sharpened, NOT a fresh flow-acceleration

Grading the print against my existing rows produced a three-part answer, and the nuance is the finding:

- **On LEVEL — slight escalation.** FL moved from #3-by-rate (April) to **#1 state by rate** on the H1 cumulative. Moves the FL row up; consistent with my standing 🔴 read.
- **On FLOW RATE-OF-CHANGE — DECELERATING, not accelerating.** National YoY growth cooled Q1 +26% → H1 +21%; **Q2 filings (115,714) came in slightly BELOW Q1 (118,727)** — the quarterly level is flattening off the Q1 high. ATTOM's own framing ("gradually returning to more typical patterns") is real on the growth rate. This is a high-plateau, not a new spike. *(Reconciliation check: Q1 118,727 + Q2 115,714 = 234,441 gross vs 227,548 H1-unique = 6,893 dual-quarter overlap — standard ATTOM per-period dedup, no contradiction with my Q1 figure.)*
- **On CONVERSION SPEED — this is the genuine acceleration.** Avg foreclosure timeline fell to **563 days, the lowest since 2013 (−13% YoY)**, while REO completions ran **+33% YoY** for the half and June REO reaccelerated (+23% YoY, 4,773) after May's −20% MoM dip. So the accumulated inventory is converting to bank-owned and reaching the market **faster** even as the inflow rate cools. That's bearish for the Sun Belt price cohorts (more REO supply, sooner) and it **resolves my open "watch-June-REO" thread — conversion trend intact.**

**Net verdict:** The print CONFIRMS and SHARPENS my thesis (pipeline converting, FL Sun Belt epicenter) rather than overturning it or forcing a regime change. It does NOT read as a fresh distress acceleration — the flow rate is cooling; the acceleration is in throughput/conversion. Overall domain status stays **🔴**.

**FHA/VA thin-equity corroboration (asked):** MEDIUM-HIGH, but INDIRECT. ATTOM is filings-based with no loan-type split, so it can't directly test the DEWEY 6/27 prior (FHA non-current >13%, ~3× market, EPDs highest since 2009, FL/2022-vintage). But the **geography is the FHA/thin-equity map**: the leading states (FL, SC, IN, DE, IL) and metros (Punta Gorda, Lakeland, Cape Coral, Jacksonville, Ocala; Columbia SC, Macon GA, Fayetteville NC) are precisely the affordable Sun Belt markets with heavy FHA/first-time-buyer penetration and 2021-22 peak-price purchases now near/underwater. The foreclosure surge is concentrated where the thin-equity cohorts bought. Consistent with the mechanism at the state/metro level; not a clean loan-type confirmation.

---

## 4. MORTGAGE-RATE SURFACE (HOMER-owned) — rate-high × foreclosure-surge

30Y PMMS printed **6.55% [7/16]** (+6bps WoW, second straight weekly rise off the Jul-2 seven-week low of 6.43 → 6.49 → 6.55; WSJ daily 6.62 [7/17] runs above the survey), back at/near 2026 highs. The rate-high resuming *into* the foreclosure surge is self-reinforcing: **stressed FHA/thin-equity Sun Belt borrowers have no refi escape valve** (can't refinance out of distress at 6.55%), so cures stay suppressed and the 563-day-and-shortening pipeline drains straight to REO. On the demand side, the same rate wall is landing hard — **NAR Pending Home Sales June −5.4% MoM (a 4.9pp miss vs −0.5% expected, all four regions down), with NAR explicitly blaming "the highest mortgage rates in nearly a year and the record-high national median home price"** — and today's Census June starts "beat" (+19% MoM) is a composition mask: **SF starts were flat (−0.2%) and SF permits fell −2.4%** — the whole jump was multifamily, building supply into an already-distressed MF book. Rate-high freezes purchase demand at the top of the funnel while foreclosures convert to supply at the bottom — pressure from both ends onto the same Sun Belt price cohorts.

---

## 5. REGINALD Path-C flag — WRITTEN

Note delivered to `AGENTS/REGINALD/inbox/2026-07-17_from-HOMER_fl-foreclosure-collateral-context.md`. FL is worst-in-nation on residential foreclosures with metro concentration in exactly the Sun Belt names that matter for FL-bank collateral; flagged as collateral context for REGINALD's Monday 7/21 triple-print prep. Residential-first (housing pipeline), so I've framed it as context, not a bank-exposure call (that read stays REGINALD's).

---

## 6. Byproduct for CARL (CRL-06, CARL-owned) — Q2 actuals now in

My 7/12 CRL-06 package was Q1 + a run-rate estimate. H1 gives **Q2 actuals**, and the metric-choice-is-outcome-determinative finding holds with real data: **Q2 clears 70K on FILINGS (115,714 ✓) and on STARTS (~82-88K ✓) but NOT on REO (~13,963 ✗).** CARL owns the resolution call; flagging that the Q2 data is now available to close it (route via NEXUS_BRIEF / your call on whether to ping CARL).

---

**Files touched (all `AGENTS/HOMER/`):** `workbook/PIPELINE.tsv` (+7 national H1 rows), `workbook/STATE_HSG.tsv` (+FL H1 state + FL metro rows), `workbook/BUILDER.tsv` (+PMMS 7/16, Pending Home Sales June, Census June starts), `STATUS.md`, `SCRATCH.md`, `NEXUS_BRIEF.md`. Plus `AGENTS/REGINALD/inbox/` note.
