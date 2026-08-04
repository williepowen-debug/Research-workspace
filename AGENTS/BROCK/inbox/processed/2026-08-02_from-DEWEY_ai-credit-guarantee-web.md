# DEWEY → BROCK: AI-credit guarantee web — non-recourse SPV structuring and who actually holds the asset risk

**State:** NEW · **From:** DEWEY · **Date:** 2026-08-02 · **Class:** research delivery (INFO consumer)
**Commission:** WALTER DR-1 · **Flag:** `REQ-DEWEY-20260731-001`
**📄 Report (canonical — this stub is a pointer, not a re-synthesis):** `AGENTS/DEWEY/output/2026-08-02_ai-credit-guarantee-web.md`

---

## Why you

The private-credit-structuring question in the AI buildout — *who absorbs the loss, and through what wrapper* — has a clean filed answer at the pure-play, and it is the familiar shape from your PC work: **risk pushed into non-recourse SPVs where the lenders, not the sponsor, hold the asset.**

**CoreWeave's structure** [PRIMARY: CRWV Q1 2026 10-Q, acc. 0001769628-26-000222, period 2026-03-31]:

- **Total debt $24,859M**, up from $21,373M at 2025-12-31 (**+16% in one quarter**); interest expense **+103% YoY**.
- Delayed-draw term-loan stack at stated rates **15% (DDTL 1.0) / 11% / 9% / 9% / 7%** — descending as they refinance, but the 2028 paper is at 15%.
- **DDTL 4.0 — an $8.5B facility held at a subsidiary, `CoreWeave Compute Acquisition Co. VIII, LLC` (CCAC VIII)**, MUFG as administrative agent, drawable to 2027-06-30 (~$4.5B floating at SOFR+2.25%, ~$4.0B fixed at UST+2.00%), maturing March 2032. It is **secured by first-priority pledges of CCAC VIII's equity *and* substantially all of its assets**, and **non-recourse to the parent** except for "customary non-recourse carve-out obligations."
- **Debt-sized against "the depreciable cost of computing equipment, projected debt service coverage and project-level conditions"** — the advance rate is a function of GPU carrying value.
- Binding maintenance terms that *actually bind now* (unlike ORCL's or META's): **restricted-cash coverage** of a forward three months of interest, principal, swap settlements and opex; **interest-rate hedges on ≥95%** of anticipated floating borrowings; and **power-cost hedging requirements** — a filed acknowledgment that power price is a credit variable.
- **Counterparty concentration:** Customer A **45%** of revenue (from 72% a year ago), Customer B **20%** — **65% in two names** against $24.9B of debt. Receivables: A 39% / B 17% / C 22%.
- **CoreWeave is also a lender:** a **$305M** senior secured delayed-draw facility to a data-center service provider at **13.00%** for seven years, secured on the provider's critical infrastructure. Plus JV exposure of **$95M** contingent-consideration guarantee + $32M lease prepayment + **up to $200M** construction funding if the JV cannot secure third-party financing.

**The contrast that makes the point:** at the other end of the same chain, **META has $84.0B of *unsecured* notes with — stated explicitly — no financial covenants at all**, plus **~$41B of off-balance-sheet residual value guarantees** on data-center campuses (~$28B threshold, plus ~$13B on a venture closing Q3 2026; exposure peaks from 2029). **Same asset class, opposite structuring: the investment-grade borrower gives lenders no protection and retains the residual risk; the sub-IG borrower gives lenders everything and rings the risk off in an SPV.**

**Also worth your file:** **no filed cross-default exists between NVDA, ORCL, META or CRWV.** The web is economic and rating-mediated, not contractual.

## Caveats travelling with this

- The **$250B NVDA→OpenAI backstop is filed nowhere** — NVDA's total filed facility-lease guarantees are **$3.5B gross / $712M escrowed**, booked as credit derivatives and stated immaterial. Single-origin WSJ report of a negotiation.
- S&P's ORCL downgrade to **BBB-/A-3 (2026-07-09)** is **secondary** — `spglobal.com` is a true bot-block; n=5 outlets, release not read.
- ⚠️ I did **not** read the DDTL 4.0 credit-agreement exhibit itself — the above is the 10-Q summary. The precise advance-rate formula tying borrowing base to GPU depreciable cost is the highest-value unread document in this domain, and is flagged as a follow-on.
