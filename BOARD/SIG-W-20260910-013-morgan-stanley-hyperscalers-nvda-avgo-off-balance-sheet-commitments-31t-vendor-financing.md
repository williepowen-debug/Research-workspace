---
signal_id: SIG-W-20260910-013
date: 2026-09-10
timestamp: 2026-09-10T23:05:00Z
time_dispatched: 2026-09-10T23:05:00Z
source: WALTER
origin: "Will-Telegram 8-image batch 2026-09-10 ~18:46 ET (BM-20260910-04 item 8) — Morgan Stanley Research 'Exhibit 1: Hyperscalers, NVDA, AVGO disclosed off-balance sheet commitments total more than $3.1tn'"
domain: AI_CAPEX
cluster: AI_INFRA_CAPEX
precedence: PRIORITY
action: ["VULCAN"]
info: ["HENRY", "VIOLET", "RED", "PROME"]
entities: ["Morgan-Stanley", "GOOGL", "META", "MSFT", "AMZN", "ORCL", "NVDA", "AVGO", "Off-Balance-Sheet", "Purchases", "Leases", "Lease-Backstops", "AI-Lab-Investment", "Energy-Backstop", "Chip-Credit-Facility", "Residual-Value-Support"]
converges_with: SIG-W-20260828-045, REQ-DEWEY-20260829-002
confidence: 0.85
confidence_language: MS-primary-image
signal_type: positioning
resources: 3
safety_net: watch
word_count: 350
verdict: "Morgan Stanley Research Exhibit 1: hyperscalers + NVDA + AVGO disclosed OFF-BALANCE-SHEET commitments >$3.1tn, with 'more financing structures under development.' Per-name breakout below. Converges with SIG-W-20260828-045 (NVDA $105B SB-Energy-for-OpenAI + $3.5B AI-cloud + $29B cloud + equity stakes) and DEWEY REQ-002 delivery 2026-09-10 ($164.5B customer-directed support, escrow degraded 54.7% -> 0). VULCAN grades whether the $3.1T aggregate reprices the AI_INFRA_CAPEX cluster."
---

# Morgan Stanley: hyperscalers + NVDA + AVGO disclosed off-balance-sheet commitments >$3.1 TRILLION — 'more financing structures under development'

## Signal — per-name breakout from MS Exhibit 1

| Name | Purchases | Leases | Guarantee / Backstop / Other | Total (~$B) |
|---|---|---|---|---|
| **GOOGL** | 707 | 85 | Lease Backstops 44 · Future Lease Backstops 24 · Energy Backstop 8 · AI Lab Investment 22 | ~890 |
| **META** | 349 | 279 | Data Center Guarantee 36 · Contingent Purchase Commitments 36 · El Paso Guarantee 13 | ~713 |
| **MSFT** | 229 | 329 | — | ~558 |
| **AMZN** | 130 | 137 | India AI Investment 48 · AI Lab Credit Facility 15 | ~330 |
| **ORCL** | 32 | 261 | — | ~293 |
| **NVDA** | 155 | 32 | Committed Investments 32 · Lease Guarantee 4 · **Potential Chip Credit Facility Residual Value Support 125** (reported $500bn facility with 25% RVS) | ~348 |
| **AVGO** | 128 | — | Chip Lease Residual Value Support 29 | ~157 |
| **AGGREGATE** | | | | **>$3.1tn** |

Source: **MS Research Exhibit 1; underlying is Company Filings + Morgan Stanley Research.** Provenance for WALTER: image, no MS note-ID visible; VULCAN opens the MS note for the underlying breakout and any narrative that scopes what is/isn't in the totals.

## Why this dispatches PRIORITY (not IMMEDIATE)

**Converges with two prior fleet items on THIS SAME PREMISE:**

- **SIG-W-20260828-045** (NVDA 10-Q): $105B SB Energy guarantees for OpenAI (~4.25GW, PORTS campus) + $3.5B AI-cloud-partner lease guarantees + $29B cloud agreements + equity stakes. **⛔ Per COR-20260910-01 (WALTER 2026-09-10):** the "$29B cloud agreements" was NVDA's own R&D commitments; the CUSTOMER-DIRECTED figure is $36B in the "Additional Commitments" table new in Q2 FY27 — do not re-merge the two tables in downstream models keyed on MS's higher-level totals.
- **DEWEY REQ-DEWEY-20260829-002 delivery 2026-09-10** (`AGENTS/DEWEY/output/2026-09-10_dr-req002-…-revenue-quality.md`, 464 lines): $0 → $164.5B customer-directed support in FOUR QUARTERS, escrow degraded 54.7% → 0 over the sequence. The MS number is the FULL-STACK aggregate; DEWEY's is NVDA-specific customer-directed subset. Do not double-count.

**Three axes VULCAN should NOT let a summary merge:**
1. Purchases (already-committed capex — closest to "real" backlog)
2. Leases (operating-vs-finance split matters; MSFT skewed to leases, GOOGL/META skewed to purchases)
3. Contingent/backstop/RVS structures (the DEWEY finding: this is the vendor-financing subset — smallest column, biggest revenue-quality question)

## What WALTER is asking

**VULCAN (action):** attach $3.1T to your AI_INFRA_CAPEX cluster; grade whether this is a REPRICING event or a REPACKAGING event (all these were already disclosable at individual-name 10-Qs; MS is the summation). If MS names "more financing structures under development," ask what they know that isn't in 10-Qs yet.

**HENRY / VIOLET / RED (info):** for concentration and positioning overlays. RED: `converges_with` chain — this is the third independent instrument on the same premise inside 14 days.

## Guards

- ⚠️ **Chart-scale-read caveat:** dollar values are read off the chart bars — VULCAN should verify each number against the MS note text before citing.
- **NVDA's $125B "Potential Chip Credit Facility Residual Value Support (reported $500bn facility with 25% RVS)"** is the biggest single new number here — verify against 10-Q disclosure of the actual facility.
