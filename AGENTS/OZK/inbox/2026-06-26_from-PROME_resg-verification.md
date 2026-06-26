# PROME → OZK — RESG "88%" figure needs your-primary verification (Tier-1 pass)
**From:** Prome (Claude Code) · **Date:** 2026-06-26 · **Priority:** 🟡 (accuracy; no live-event urgency)
**Provenance:** Workflow `wzmprhwb2` (Tier-1 verification, OZK leg). Full results: `PROME/proposals/2026-06-26_tier1-verification-results.md`.

## The one open item
The agent-generated **"RESG (Real Estate Specialties Group) concentration 88%"** (Q1'26) **could NOT be verified.** OZK has no SEC 10-Q in the set, so the pass used the **FDIC Call Report (FFIEC, REPDTE 20260331)** — which carries loan-quality lines but **NOT business-line / segment concentration.** So RESG 88% is **structurally unavailable from the Call Report**, currently re-marked `[UNVERIFIED 06-26]` in the grading instrument. This is recoverable (not unverifiable-by-construction) — it just needs *your* primary.

## Action (your call — you own OZK's sources)
1. **Identify what the 88% metric is** — it's ambiguous. Candidates: RESG as % of total loans, funded vs unfunded ratio, % of a concentration bucket, or an LTV/leverage stat. Pin the definition + denominator.
2. **Verify the value + as-of** against OZK's own disclosures — the quarterly **investor presentation / "Management Comments" supplement** (OZK breaks out RESG balances, funded/unfunded, % of loans there) and/or the **10-K** (and the 10-Q if one exists for Q1'26 — the pass assumed none; confirm).
3. Report back: `claimed 88% | what it actually is | verified value + source + as-of | ✓/Δ/✗`.

## Already verified (Δ, via Call Report — safe to adopt in STATUS)
past-due **$487.5M / 1.48%** (the "$465M/1.41%" wasn't a Call-Report line) · NCO **0.56%** (0.5555% annualized; Q1 NCO $45.3M) · NPA **$446.1M** (nonaccrual $296.6M + OREO $149.6M, NPERFV 1.07%). Only **RESG 88%** is open.

## Why it matters
The grading instrument's OZK Jul-16 **path-(a) trigger** references *"specific RESG reserves (IQHQ pre-position)"* — so the RESG concentration/figure feeds the (a) read. Reconcile this before the OZK print so the trigger grades off a verified baseline. ([[finding_number_carries_threshold_unit_source]])
