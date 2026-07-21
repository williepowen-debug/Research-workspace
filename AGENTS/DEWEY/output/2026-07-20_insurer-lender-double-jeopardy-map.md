# Insurer-lender double-jeopardy map of the 5 gated funds — BRK / Athene-vector adjudication
**Date:** 2026-07-20 | **Mode:** Thesis (M-08 insurer nexus / gate cascade; consumers SHADE action · BROCK co-owner · REGINALD/NEXUS info · TERRY downstream) | **Confidence:** **High** (lender-side, EDGAR-verified; the "not publicly confirmable" holder verdict) / **Medium** (holder-side completeness for Brighthouse/Corebridge) | **Flag:** REQ-DEWEY-20260702-013 (Batch-2 #17)

## Key Finding
**The insurer-lender double-jeopardy map for the 5 gated funds CANNOT be populated at the named-entity level from public data — and both legs come back empty of named insurers.** The **LENDER leg is bank-led** (EDGAR-verified across all 5 funds: no life insurer is a named lender on any filed credit facility). The **HOLDER leg is behind the NAIC Schedule BA wall** (per-insurer fund-level holdings are not publicly obtainable; every public "shadow" — insurer 10-Ks, earnings releases, NAIC special reports — discloses at asset-CLASS level only). The pathway is **mechanically real** (Fed FEDS Note; Clearwater estimates 10-20% of insurer LP-equity holders also hold the same fund's debt) but **no named public instance exists** of any insurer being both holder AND lender to any one of these five funds. This **validates and sharpens SHADE's 6/26 map**: every "Unknown/NOT CONFIRMED" cell resolves to either **bank-led/refuted** (lender) or **not publicly confirmable** (holder) — *not* to a confirmed exposure. Trade-relevance stays **mechanism-watch, not named-entity exposure.**

> ⚠️ **Epistemic guardrail (load-bearing):** "not publicly confirmable" is a limit of PUBLIC data — it is **NOT** a finding that these insurers hold none of the five. Per-insurer Schedule BA (the definitive source) is behind DOI/InsData access and was not obtained. Absence in a 10-K is *expected* even where a real Schedule-BA position exists. Do not read this report as an all-clear on the vector.

---

## The map — SHADE's "Unknown" cells, resolved

| Fund | Insurer as LENDER (EDGAR credit agreements — DEWEY-verified) | Insurer as HOLDER (Schedule-BA shadow — fan-out) | Double-jeopardy pair? |
|---|---|---|---|
| **ADS** (Apollo) | **NONE** — Bald Eagle Funding SPV Credit Agreement 3/9/26 fully read (606K chars): **BofA (admin agent), Citibank (collateral)**; zero insurer names | **Athene NOT confirmable** — Athene FY2025 10-K: 0 hits for ADS; ADS 10-K frames Athene as parallel *co-investor* only, not a holder; sole affiliate purchase = trivial $50K/2,000-share 2021 seed | **NO named pair** |
| **BCRED** (Blackstone) | **NONE** — facility EX-10.1 6/30/25, bank-led SPV; full insurer roster absent | Corebridge "Blackstone Private Credit" hits = **2021-22 IPO-registration** mentions of the Blackstone asset-mgmt *partnership*, not a disclosed BCRED general-account holding (pre-window) | **NO named pair** |
| **Monroe** (Monroe Capital) | **None named** — 2nd Amend. Loan/Security/Servicing Agmt; ⚠️ but the Eligible-Lender **definition generically permits** "any commercial bank, investment bank or **insurance company**…" — a structural door, no insurer named | Not publicly confirmable | **NO named pair** |
| **CCLFX** (Cliffwater) | **None named** — interval fund, no EX-10 credit-agreement exhibit; **BofA (80 hits)/Wells (20)** dominate → bank-led revolver | "Global Atlantic" 16 hits = **CCLFX's OWN NPORT-P portfolio holdings** → CCLFX is a *creditor to* GA-linked issuers (**REVERSE direction**), not GA holding CCLFX | **NO named pair** |
| **North Haven PIF** (Morgan Stanley) | **NONE** — facility EX-10.1 9/15/25, securitization-subsidiary structure; full roster absent | Not publicly confirmable | **NO named pair** |

**F&G** (prompt's most RBC-fragile, ~430% RBC 12/31/25) — FY2025 10-K names **none** of the five; only >10%-equity concentrations are two **Blackstone-managed SPVs** (Wave $655M; Cooper $472M was 2024). **Brighthouse** — "Apollo Debt Solutions" appears only in its **merger proxy / variable-product** context, not a general-account holdings schedule.

---

## Leg 1 — LENDER side (DEWEY EDGAR carve-out; the fan-out structurally can't reach this)
**Result: no life insurer is a named lender on any of the five funds' filed credit facilities. The facilities are bank-led SPV / securitization / revolving structures.**
- **ADS** [PRIMARY: EX-10.1, acc 0001193125-26-102160, 3/9/26, read in full]: *"CREDIT AGREEMENT among BALD EAGLE FUNDING LLC, as Borrower, THE LENDERS PARTY HERETO, BANK OF AMERICA, N.A., as Administrative Agent, CITIBANK, N.A., as Collateral Agent."* Grep of the entire 606,942-char agreement for Athene / Global Atlantic / Corebridge / MassMutual / TIAA / Brighthouse / Nationwide / "Insurance Company" → **zero hits.**
- **BCRED** [PRIMARY: EX-10.1 6/30/25]: full insurer roster **absent.**
- **Monroe** [PRIMARY: EX-10.1 3/19/26, Second Amendment to Loan, Security and Servicing Agreement]: no insurer named; the only "insurance company" hit is the **generic Eligible-Lender/Assignee definition** — the facility *permits* insurers as lenders but names none. A structural door, not a confirmed lender.
- **North Haven** [PRIMARY: EX-10.1 9/15/25]: full roster **absent.**
- **CCLFX** [interval fund]: no EX-10 credit-agreement exhibit; **BofA (80) / Wells Fargo (20)** dominate its filings vs **zero** insurer-lender names → bank-led revolver (exact lead not pinned in the truncated N-2 window — soft on the name, firm on "no insurer").

> **Keyword-hit decomposition (why raw EFTS counts mislead — context read on each):** ADS-"Athene" 44 hits = shared Apollo/Athene **Code of Business Conduct & Ethics** (EX-99.(R)(2)); BCRED-"Corebridge" 22 = 424B3/N-14/ARS prospectus family; CCLFX-"Global Atlantic" 16 = CCLFX's **own portfolio holdings** (reverse direction). None is a lender relationship. `[[finding_verify_reader_before_source]]`

## Leg 2 — HOLDER side (fan-out: 104 agents, 4.6M tokens, 24/25 claims confirmed)
**Result: no US life insurer's equity/Schedule-BA holding in any of the five is publicly confirmable — the public shadows disclose at asset-class level only.**
- **NAIC Capital Markets Bureau Schedule BA special reports are aggregate-only** [PRIMARY: content.naic.org YE2025 + YE2023]: buckets by asset type (PE/HF/RE ~70-73%) and insurer type, naming **no individual fund or insurer.** Context: YE2025 total Schedule BA **$637.9B BACV; life insurers 65% ($414.3B, +10.6% YoY); affiliated $296.8B (45%, down from 48%) vs unaffiliated $341.1B (55%)** — 2nd consecutive year unaffiliated > affiliated.
- **FSB (June 2026)** gives only aggregate proxy (~10% of life-insurer portfolios may be private credit) and states insurer PC exposure is *hard to estimate* because it hides in corporate / non-mortgage structured-finance categories.
- **Prospective (forward flag for SHADE):** **beginning with FY2026 statutory reporting, insurers must give more granular private-placement disclosures** (private-investment classification, fair value, Level 2/3, PIK, private letter ratings) — so fund-level statutory-shadow granularity **may improve from FY2026 filings onward** (the monitoring path opens up, but may still target attributes not fund names).

## Leg 3 — Athene ↔ ADS pair (SHADE's "most actionable candidate")
- **LENDER leg: REFUTED** — Athene absent from the entire ADS credit agreement; agents are BofA/Citi.
- **HOLDER leg: NOT publicly confirmable** — Athene FY2025 10-K [PRIMARY: ahl-20251231] returns **0 hits** for "Apollo Debt Solutions"/"ADS"/"non-traded BDC"/"business development company." ADS's only Athene reference is co-investment-alignment framing (*"through Athene, Apollo is often among the largest investors in its own funds… which co-invest alongside the Company"*) — parallel co-investment, **not** a disclosed ADS equity stake. Athene's Apollo-affiliated exposure is disclosed only at aggregate related-party level ($35.4B, 9.2% at 12/31/25). ADS Items 12/13 are incorporated by reference to a **not-yet-filed proxy** → per-holder detail unavailable.
- **Net:** the textbook double-jeopardy candidate resolves to **one leg refuted, one leg unconfirmable** — probable exposure (Apollo family) but no public confirmation, and specifically NOT a lender.

## Leg 4 — priority by RBC fragility (F&G > Brighthouse > Corebridge > GA > Athene)
- **F&G** (most fragile, ~430% RBC 12/31/25, above 400% target) [PRIMARY: FY2025 10-K, annual report, Q3 supplement, earnings release]: names **none** of the five; only >10%-equity concentrations are **Blackstone-managed SPVs** (Wave $655M). F&G's portfolio is Blackstone-managed (IMA w/ Blackstone ISG-I) — the **F&G↔Blackstone affiliation is the structural analog to Athene↔Apollo**, so any F&G PC exposure flows through a Blackstone mandate, but BCRED-the-fund is not named.
- **Brighthouse / Corebridge** [DEWEY EDGAR check, closing the fan-out's flagged gap]: fund-name hits exist but decompose to **non-holding context** — Corebridge's 96 "Blackstone Private Credit" hits are **2021-22 IPO S-1 registration** (the Blackstone asset-mgmt partnership); Brighthouse's "Apollo Debt Solutions" hits are **merger-proxy / variable-product** context. Neither is a confirmed general-account fund holding.

---

## Counter-Evidence (carry it)
1. **The overlap is real in aggregate — this is not an all-clear.** Clearwater estimates **10-20% of insurers with LP equity in private-credit funds are ALSO exposed to the same fund's debt** [SECONDARY: PitchBook/Yahoo mirror of a Clearwater 6/24/26 report — an aggregate estimate, distinct from the out-of-bounds ~25% stat]. The Fed FEDS Note (3/2025) describes the mechanism generically (an affiliated life insurer holding both a vehicle's equity and debt). **The pattern exists; only the named mapping for these 5 funds is absent.**
2. **Absence of a named holding ≠ absence of the holding.** Insurer 10-Ks are *expected* to disclose PC at asset-class level even where a real Schedule-BA fund position exists. A negative here is uninformative about the underlying Schedule BA.
3. **The affiliations that would create double-jeopardy DO exist** — F&G↔Blackstone, Athene↔Apollo, Global Atlantic↔KKR, MassMutual↔Barings — they just don't surface at fund-name level in public filings.
4. **Refuted in verify (0-3):** the claim that ADS's ~10,497 Class-S holders-of-record imply dispersed retail *rather than* a concentrated affiliated block — the two are not mutually exclusive; holder counts don't bear on whether an insurer holds a block.

## Source Quality Assessment
- **Strongest:** the LENDER-side verdict (5 funds, primary EDGAR credit-agreement exhibits, ADS read in full — a clean, checkable negative) and the Schedule-BA-aggregate-only structural finding (primary NAIC PDFs, 3-0).
- **A "not confirmable" verdict is epistemically robust** here — it rests on the *structure* of public disclosure (asset-class not fund-name), an invariant, corroborated by FSB + NAIC + multiple insurer 10-Ks all returning zero fund-name hits.
- **Gaps (honest):** (1) **per-insurer NAIC Schedule BA** — the definitive source — NOT obtained (DOI/InsData wall); this is *the* structural limit. (2) **Brighthouse/Corebridge** holder legs addressed by EDGAR grep + form-type reasoning, not a full statutory read. (3) ADS **DEF 14A** (with Item 12 beneficial owners) not yet filed. (4) CCLFX facility lead bank not pinned to a name. (5) SEC.gov 403'd several WebFetch reads (fan-out re-pulled via curl+UA — per `[[finding_edgar_403_user_agent_header]]`).

## References
**Primary — SEC (EDGAR), DEWEY-pulled:** ADS credit agreement EX-10.1 acc 0001193125-26-102160 (CIK 1837532); BCRED EX-10.1 acc 0001803498-25-000062 (CIK 1803498); Monroe EX-10.1 acc 0001104659-26-032174 (CIK 1742313); North Haven EX-10.1 acc 0001193125-25-202527 (CIK 1851322); CCLFX N-2 acc 0001213900-26-018433 (CIK 1735964); Athene FY2025 10-K (CIK 1527469, ahl-20251231); ADS FY2024 10-K (CIK 1837532); F&G FY2025 10-K (CIK 1934850, fg-20251231); Corebridge S-1/A 2022 (CIK 1889539); Brighthouse DEFM14A 2026 (CIK 1685040). *(Reproduction: `edgar_doc.py search/doc --cik <CIK>` + `edgar_fetch.py <CIK>`.)*
**Primary — regulatory:** NAIC Capital Markets Schedule BA special reports YE2025 + YE2023 (content.naic.org); FSB private-credit vulnerabilities report, June 2026 (fsb.org/uploads/P060526.pdf); NAIC government-affairs private-credit issue brief, April 2026; Fed FEDS Note, "Life Insurers' Role in the Intermediation Chain," 2025-03-21.
**Secondary:** PitchBook/Clearwater, "Life insurers lend to private credit funds they back" (Clearwater 6/24/26 report, 10-20% estimate); Moody's (insurancebusinessmag) on insurer PC liquidity/concentration risk.

## Process Report
**Engines:** DEWEY EDGAR lender-side carve-out (legs 1+3, ~20 targeted `edgar_doc`/`edgar_fetch` calls — the load-bearing leg) run **concurrently** with a `/deep-research` fan-out (104 agents, 4.62M tokens, ~11 min, 0 errors, 24/25 claims confirmed) for the holder-side Schedule-BA shadows (leg 2) + institutional framing. **Engine sizing was right:** the lender side is pure single-name filing-mining the fan-out can't reach; the holder side is broad/scattered-source discovery the fan-out is built for — and both converged on the same "no named entity" answer from opposite directions, which is the strongest form of this verdict.
**What worked:** EDGAR full-text + credit-agreement exhibit reads gave a clean, checkable lender-side negative (ADS read in full); the fan-out independently confirmed the holder-side wall from primary insurer 10-Ks + NAIC PDFs.
**What didn't / traps avoided:** raw EFTS keyword counts were misleading on every fund (Code-of-Ethics, prospectus, reverse-direction NPORT holdings) — **context-read each, never counted**; two Monroe/North Haven facility reads first errored on wrong doc paths (manufactured false "none") and were re-read cleanly (`[[finding_verify_reader_before_source]]`).
**Data gaps:** per-insurer Schedule BA (DOI/InsData wall — the structural limit); Brighthouse/Corebridge full statutory reads; ADS DEF 14A pending; CCLFX facility lead-bank name.
**Confidence:** High (lender-side; the "not confirmable" holder verdict). Medium (Brighthouse/Corebridge holder completeness).
**If I had more time/tools:** NAIC InsData / a state-DOI statutory pull would convert "not publicly confirmable" into an actual Schedule-BA fund-level map — the single highest-value unlock. FY2026 statutory filings (enhanced private-placement disclosure) are the standing forward path.
**Suggestions:** SHADE's map cells can now be marked **RESOLVED-as-not-publicly-confirmable** (lender leg = bank-led/refuted; holder leg = Schedule-BA-walled) rather than "Unknown" — the vector stays mechanism-watch, and the concrete monitoring unlock is **FY2026 statutory disclosures + NAIC InsData**, not more public-filing mining.
