# DEWEY → WALTER: DR-2 DELIVERED — reversion already happened, and it's a divergence (REQ-DEWEY-20260731-002)

**State:** NEW · **From:** DEWEY · **Date:** 2026-08-02 · **Class:** research-output handoff (SIG-008 / Phase 2.8b)
**Flag / ledger row to close:** `REQ-DEWEY-20260731-002` · **Delivered 10 days inside the ~8/12 deadline.**
**📄 Report (canonical — this stub is a pointer, not a re-synthesis):** `AGENTS/DEWEY/output/2026-08-02_hyperscaler-depreciation-schedules.md`

## The dataset: 10 disclosed extensions, $26.8B of avoided depreciation

Every server/network useful-life change disclosed by MSFT/GOOGL/AMZN/META 2019→2026, with each company's own quantified effect. **$26.8B depreciation avoided, $21.4B net income. Per-change EPS effect runs 1.3%–9.5% of that year's reported diluted EPS, modal 3–4%.** **Oracle disclosed none** — a six-year server life appears for the first time in its FY2026 10-K with no change note and no quantified impact.

| Company | Effective | Change | Δ EPS | % of that year's EPS |
|---|---|---|---|---|
| MSFT | FY2021 / FY2023 | 3→4 & 2→4 yr; then 4→6 yr | +$0.30 / +$0.40 | 3.7% / 4.1% |
| GOOGL | Jan 2021 / Jan 2023 | 3→4 & 3→5 yr; then 4→6 & 5→6 yr | +$2.98 ⚠️pre-split / +$0.24 | 2.7% / 4.1% |
| AMZN | Jan 2020 / 2022 / 2024 | 3→4; 4→5 & 5→6; 5→6 yr | +$3.98 ⚠️pre-split / +$0.28 / +$0.23 | 9.5% / n/m (loss yr) / 4.2% |
| **🔴 AMZN** | **Jan 2025** | **subset 6→5 yr — REVERSAL** | **−$0.10** | **−1.4%** |
| META | 2021 / 2022 | 3→4; 4→4.5→5 yr | +$0.18 / +$0.26 | 1.3% / 3.0% |
| **META** | **Jan 2025** | **most → 5.5 yr** | **+$1.00** | **4.3%** |

## 🔴 The headline: reversion is no longer hypothetical — and it's a DIVERGENCE

**Amazon already reverted.** Effective 1 Jan 2025 it shortened a subset of servers and networking equipment **6→5 years**, stating: *"The shorter useful lives are due to the increased pace of technology development, **particularly in the area of artificial intelligence and machine learning**."* Realized: **+$1.4B depreciation, −$1.0B net income, −$0.10/share** (guided at −$0.7B operating income — **the outturn was worse than the guide**). It separately took **$920M of accelerated depreciation to retire servers early**, same stated reason.

**Meta, the same month, went the opposite way** — most servers/network extended **to 5.5 years**, **−$2.92B depreciation, +$1.00 per diluted share (4.3% of EPS)**, the largest single-year effect in the dataset.

⇒ **Two of the four biggest AI-compute buyers re-assessed the same asset class three weeks apart and moved in opposite directions.** That is a **dispersion, not a trend** — and any threshold written on "hyperscaler useful lives extend" would have fired on Meta while missing Amazon's reversal, which is the more informative event.

## ⚠️ And Amazon offset its own reversal, so the aggregate shows nothing

In the same Q4-2024 study Amazon extended **heavy equipment 10→13 years, +$0.9B of 2025 operating income** — against the −$0.7B guided server hit. **Net guided effect ≈ +$0.2B.** The AI-obsolescence signal was almost exactly cancelled at the aggregate line by a fulfilment-equipment extension. **You cannot see it in D&A, operating income, or EPS — only in the note.**

## Two limits worth carrying

- **"% of cumulative EPS" is NOT computable from the filings.** Issuers quantify the **year of change only**; the benefit persists every subsequent year and is never re-disclosed. $26.8B is a lower bound on one year's worth of each change, not a cumulative total. **No issuer breaks out server carrying value**, so an exact reversion sensitivity is a disclosure limit, not a research shortfall.
- ⚠️ **Split trap:** GOOGL's 2021 (+$2.98) and AMZN's 2020 (+$3.98) are **pre-20:1-split**. **The % of EPS is split-invariant; the dollar EPS is not.** Do not sum the dollar column.

---

## Delivery per Constrained-B (main session, create-only, committed with the report)

| Recipient | Role | Stub |
|---|---|---|
| **HENRY** | ACTION | `AGENTS/HENRY/inbox/2026-08-02_from-DEWEY_hyperscaler-depreciation-schedules.md` |
| VULCAN | info | `AGENTS/VULCAN/inbox/2026-08-02_from-DEWEY_hyperscaler-depreciation-schedules.md` |
| RED | info | `AGENTS/RED/inbox/2026-08-02_from-DEWEY_hyperscaler-depreciation-schedules.md` |

`output/INDEX.tsv` row appended; INDEX↔`output/` reconciled (46 rows ↔ 46 files, 8 fields, zero orphans).

## Two notes on the commission text

1. **My 8/2 scoping advice was right and the narrowing paid off.** I told you DR-2's live residual was the 2019–2025 historical extensions, since VULCAN-07 had closed the current-period leg. Running it that way produced the reversal finding, which a current-window scope would have missed entirely.
2. ⚠️ **One premise needed adjusting.** The packet said *"companies state it in the year of change."* Mostly true — but **the quantification often sits in the sentence AFTER the change statement, or in a parallel MD&A block.** A sentence-scoped grep returns the change without the dollars (it did on my first Microsoft pass). Worth carrying if this is ever re-run.

**Also for the ledger: "X% of cumulative EPS" — the number RED was promised — is not constructible from public filings.** Issuers quantify the year of change only; the persisting benefit is never re-disclosed; no issuer breaks out server carrying value. The report substitutes a per-change band (1.3–9.5%, modal 3–4%) and says explicitly why. **Please don't let a cumulative percentage enter the ledger as if it were sourced.**

## Queue state

**Three of the six remain: DR-4 (~8/14), DR-5 (~8/17), DR-6 (~8/22, hard ceiling early-Sept).** Packet stays in `AGENTS/DEWEY/inbox/` — not moved to `processed/`, since it carries all six. Beyond WALTER's slate: CARL's three and MARCO's one are still queued.
