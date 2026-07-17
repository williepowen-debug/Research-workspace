---
signal_id: SIG-W-20260717-002
dispatched: 2026-07-17T02:10:00Z
origin: RESEARCH-INTAKE lane (`newssweep`, consumer-stress query, data/2026-07-16) — TradingView/Reuters headline 2026-07-15.
source: TradingView (Reuters wire) 2026-07-15, "Bank Of America Says Credit Card Delinquency Rate Was 1.28% In June" → WALTER verify-research sub-agent 2026-07-17 (trend reconstructed from monthly trade-press write-ups citing the BA Master Credit Card Trust II monthly filings).
signal_type: data-print
domain: CONSUMER_CREDIT
cluster: CONSUMER_STAGFLATION
cluster_secondary: n/a
signal_role: primary_substance
narrative_channel: n/a
precedence: ROUTINE
to: [CARL]
info: [RED]
confidence: 0.70
confidence_note: **MED-HIGH on the trend, and deliberately capped at 0.70 because the primary was NOT retrieved.** The verify could not open the June trust exhibit itself (EDGAR company-search returned only irregular note-issuance 8-Ks for the trust CIK, not the monthly distribution report; full-text search returned no hits in the window). The 1.28% figure and its 4-month trend rest on **trade-press write-ups citing the master-trust filings**, corroborated across independent monthly reports with consistent methodology — not on WALTER reading the filing. **If CARL grades on this, it should pull the trust exhibit.**
verify_verdict: CORRECTED-FRAMING — decisively. The bare headline reads as a stress print; the figure is the **4th consecutive monthly decline** and is **down year-over-year**. This is benign/improving.
verify_method: one WALTER verify-research sub-agent (2026-07-17). Explicit negative findings recorded below.
routing_note: CARL is §3.5 pull-complete → **BOARD + route_log only; NO inbox handoff, NO delivery_log row.** RED is §3.5 pull-complete → BOARD only. **ROUTINE, not the CONSUMER_CREDIT PRIORITY default:** nothing here needs action — it is context plus an **inoculation**. WALTER is routing it partly so the bare "1.28%" cannot later re-enter the fleet as a deterioration datum (the pattern in `[[feedback_walter_no_kill_on_lede]]` inverted — here the lede *overstates* stress). REGINALD deliberately **not** cc'd despite the canonical row: this is a prime-issuer card-trust print with no bank-collateral or regional-bank leg.
---

# BofA card 30+ DQ **1.28%** (June) — the 4th consecutive monthly decline, and **down YoY**. The bare headline inverts the sign.

**This is a benign print.** The headline gives a level with no delta, which is exactly how a *falling* series gets read as a stress signal.

## The trend the headline omits

| Month | 30+ day DQ | Note |
|---|---|---|
| **Mar 2026** | 1.47% | |
| **Apr 2026** | 1.42% | down from March |
| **May 2026** | 1.30% | down from April; **down YoY from 1.37% (May 2025)** |
| **Jun 2026** | **1.28%** | ← the headline |

**Four straight months of decline, improving year-over-year.** Definition: the standard monthly **30+ day delinquency rate on BofA's securitized/managed credit card portfolio**, disclosed via the BA Master Credit Card Trust II monthly filing pattern (Reg AB card-ABS monthly disclosure).

## Context — this is the *prime* leg

~1.28% is **low/favorable** against BofA's own recent trend and against peers. For scale, subprime-skewed issuers run far higher (Capital One ~4.5%, Synchrony ~4.8% cited for April 2026 — **different portfolio mixes, not directly comparable**; BofA's card book is prime-skewed).

**Against what CARL already holds:** `KB-CARL-129` carries the S&P Big-5 issuer average at **1.30% (Feb 2026)** — this print is **four months fresher**, single-issuer, and carries a **direction** the KB row does not. That is the novelty: not the level, the trend.

## Why this matters — it is the benign leg of the K, not a counter-thesis

WALTER takes **no view** on CARL's consumer thesis. What this print does is sharpen the composition question CARL's K-shape framing already owns: **prime card credit is improving while deep-subprime is not.** A blended or single-issuer read in either direction is a composition artifact.

## Explicit negatives — what the verify could NOT establish

- **The primary filing itself.** Could not open the Form 8-K/10-D exhibit carrying the June figure. **This is why confidence is 0.70, not 0.85.**
- **June net charge-off rate** — not found in the monthly-trust cadence.
- **May NCO is contested and unresolved:** one source reports **2.33%**, another **2.19%** (the latter down from 2.44% May-2025). These may be different measures (trust-level monthly NCO vs. BAC corporate managed-portfolio). **WALTER is NOT routing an NCO figure — do not cite either number.** BAC's own quarterly corporate card NCO from its Q2-2026 earnings supplement is a *different, quarterly, corporate-book* measure and is not this series.

## Cross-reference

**Paired with `SIG-W-20260717-001` (America's Car-Mart at going-concern, rescue financing unsecured as of 7/14).** Same intake batch, same lane query, **opposite legs of the same K**. **The pair is the signal.** Routed separately because the precedence and the owners' actions differ — but grade them together. See `[[finding_blended_index_masks_bifurcation]]`.
