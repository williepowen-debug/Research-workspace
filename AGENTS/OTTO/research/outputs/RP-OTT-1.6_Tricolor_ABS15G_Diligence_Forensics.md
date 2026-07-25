# RP-OTT-1.6 — Tricolor ABS-15G Diligence Forensics: seven years of clean third-party reports that could not have caught the alleged fraud

**Date:** 2026-07-25 (session 016) · **Analyst:** OTTO · **Series:** 1.x (fraud/structural deep dives)
**Source grade:** `[CONF SEC EDGAR]` — all 11 Form ABS-15G filings + 12 Exhibit 99.x agreed-upon-procedures reports, depositor **Tricolor Auto Receivables 2, LLC (CIK 0001757871)**, filed 2018-11-05 → 2025-06-02. Primary documents only; no secondary sourcing.
**Commissioned as:** "Tier 1" of the 2018-2021 vintage thread (Will, 2026-07-25).

---

## Punchline

**Two findings, and the second is the one that matters.**

1. **The 2018-2021 vintage thread is largely empty — I was wrong to headline it.** Tricolor securitized **only two deals** in that window (2018-2, 2021-1) with a **32-month gap** between them. Nine of eleven deals are 2022-2025. The impaired-collateral concentration is **2022-2025**, not 2018-2021. Retiring this as a lead.
2. **The diligence was structurally incapable of detecting either alleged fraud mechanism** — and it ran clean for seven years across three accounting firms. The agreed-upon procedures verify the securitization data tape against **Tricolor's own servicing and origination systems**, which is precisely what the indictment alleges was falsified. A tape reconciled to a doctored system ties out perfectly.

This is the mechanical answer to *"how did $2B of allegedly fraudulent collateral clear diligence eleven times?"*

---

## 1. Complete deal inventory (recovered — was not previously held)

Tricolor's ABS were **144A private placements**, so there are no public 10-D distribution reports and no per-deal trust filers. Rule 15Ga-2 filings are the one public artifact each deal leaves. **The shelf is "Tricolor Auto Securitization Trust" (TAST)** — not "Tricolor Auto Receivables Trust," which is why vintage probing on the wrong stem returned zero.

| Deal | ABS-15G filed | Diligence provider | Sample | Signed by |
|---|---|---|---|---|
| TAST **2018-2** | 2018-11-05 | Crowe | 150 contract files | Daniel Chu |
| TAST **2021-1** | 2021-07-12 | Crowe | **101, "haphazard"** — size set by **J.P. Morgan Securities LLC** | Daniel Chu |
| TAST 2022-1 | 2022-04-18 | Deloitte & Touche | 150 | Daniel Chu |
| TAST 2022-2 | 2022-10-28 | Deloitte & Touche | 150 | Daniel Chu |
| TAST 2023-1 | 2023-01-31 | Deloitte & Touche | **50** (of 10,077 = **0.5%**) | Daniel Chu |
| TAST 2023-2 | 2023-10-03 | Deloitte & Touche | 150 | Daniel Chu |
| TAST 2024-1 | 2024-01-18 | Deloitte & Touche | 150 (+ prior report re-filed) | Daniel Chu |
| TAST 2024-2 | 2024-05-07 | **Grant Thornton** | 150 | Daniel Chu |
| TAST 2024-3 | 2024-09-30 | Grant Thornton | 150 | Daniel Chu |
| TAST 2025-1 | 2025-02-28 | Grant Thornton | 150 | Daniel Chu |
| TAST 2025-2 | 2025-06-02 | Grant Thornton | 150 | Daniel Chu |

**Observations:**
- **The 2019-2020 hole.** No filings between Nov 2018 and Jul 2021 — a 32-month gap spanning COVID. The "2018-2021 vintage" contains ~2 deals; 2022-2025 contains 9.
- **"2018-**2**"** implies a 2018-1 predating the ABS-15G obligation. Deal count is ≥12.
- **Daniel Chu — the indicted founder — personally signed all eleven** as CEO of the depositor. Every diligence certification carries his signature.
- **Three providers in seven years: Crowe → Deloitte (Apr 2022) → Grant Thornton (May 2024).** Two rotations. GT took over ~15 months before the September 2025 collapse.

---

## 2. Why the diligence could not have caught it

The AUP reports state their comparison sources explicitly. Deloitte (TAST 2023-2, representative):

> *"We compared Characteristic 5. through 7. to the corresponding information set forth on the **Contract**. We compared Characteristics 8. through 12. to the corresponding information set forth on the **Servicing System Screen Shots**. We compared Characteristic 13. to the corresponding information set forth on the **company's origination system**."*

Set that against the superseding indictment's allegations (2026-06-24):

| Alleged conduct | Would the AUP detect it? |
|---|---|
| *"Manipulated delinquent loan data to make non-performing loans appear current"* | **No.** Payment/status characteristics are compared **to the servicing system** — the system alleged to be falsified. A doctored source and a tape derived from it **agree by construction**. |
| *"Created fictitious payment records"* | **No.** Same mechanism — the fiction lives in the source of truth the procedure trusts. |
| *"Pledged the same collateral to multiple lenders simultaneously"* | **Almost certainly not.** Lien/title documents *are* checked (Characteristic 1 → Title Certificate, Title Application, Lien Entry Form), which is a genuine external check — but on **150 of ~10,000 loans (1.5%)**, and confirming *a* lien in Tricolor's favour is not a search for *competing* pledges of the same collateral. |
| ~30,000 vehicles missing | **No.** No procedure inspects a vehicle. |

**This is the structural point: an agreed-upon-procedures engagement is a reconciliation, not an audit.** It tests whether the data tape faithfully reproduces the originator's records. It is not designed to test whether those records are true — and the accountants say so, disclaiming any audit or opinion. **Every one of these reports can be simultaneously accurate and useless against this fraud.**

Reported exceptions across all eleven deals were trivial: *"Two differences in FICO score"* (2024-1), rounding differences under $1, date differences deemed in agreement within 30 days. **No material exception was ever reported.**

---

## 3. Secondary flags (weaker — recorded, not asserted)

- **Sample-size anomaly.** TAST 2023-1 used **50** receivables from a 10,077-loan pool (**0.5%**) — a 3× reduction from the standing 150, then back to 150 for every subsequent deal. Deloitte states the selection was made **"at the Company's instruction."**
- **The issuer and its underwriter set the diligence scope.** Deloitte samples "at the Company's instruction"; for TAST 2021-1, **"The sample size was determined by J.P. Morgan Securities LLC."** JPM is already a known Tricolor-exposed bank ($170M charge-off), so this is not a new name for OTTO-33 — but it documents the underwriter's role in scoping the review that missed the fraud.
- **"Haphazard sample of 101"** (Crowe, TAST 2021-1) — "haphazard" is a distinct and weaker sampling concept than the "random" basis used in every other year.
- **Provider rotation.** Two changes in ~26 months. Diligence-provider churn ahead of a collapse is a conventional yellow flag; on its own it is not evidence of anything, and both successor firms are major.
- **Grant Thornton cross-link `[note, do not overweight]`.** GT performed Tricolor's final four diligence engagements (May 2024 → Jun 2025, i.e. up to ~3 months before collapse) and is **also Carvana's auditor**, ratified by shareholders 2026-05-05 — a fact OTTO tracks under the Carvana sub-thesis. This is a **factual link between OTTO's two largest names, not an allegation**; GT's Tricolor role was a limited AUP engagement, not an audit, and nothing here implies a GT failure. Recorded because OTTO's Carvana red-line trigger is "GT resigns."

---

## 4. What this changes

**Retires a lead.** The 2018-2021 vintage thread is closed as a *securitization* question — the deals aren't there. The "since at least 2018" enterprise allegation still means the **originations** were tainted from 2018, but the securitized exposure concentrates in 2022-2025, which OTTO already tracks. **STATUS/CHANGELOG wording corrected accordingly.**

**Strengthens the Invisible Exit mechanism — materially.** OTTO's Secondary thesis says fraud-lender books look clean until collapse because skip-defaults bypass the reported DQ chain. This gives that a documented transmission path: **the reported data was reconciled, repeatedly, by three major accounting firms, to a system the government alleges was falsified.** "The books looked clean" is no longer an inference — it is eleven filed reports saying so, and a structural explanation for why they said so.

**Adds a reusable screen.** Any 144A subprime shelf leaves ABS-15G/Exhibit 99.1 as its one public trace. The diagnostic questions are cheap and repeatable: *what is the tape compared against; who chose the sample; how large is it relative to the pool; has the provider rotated.* Applicable to CPS, Flagship, Lendbuzz, SAFCO, GCAR and any future cockroach candidate.

**Does not, by itself, implicate anyone.** Nothing here shows an accounting firm did its job improperly. The finding is about **what the procedure is designed to do** — and it is not designed to catch a falsified source system.

---

## 5. Method note

- Deal inventory recovered via `data.sec.gov/submissions/CIK0001757871.json`, then per-accession `index.json` for Exhibit 99.x. Compliant User-Agent required (`[[finding_edgar_403_user_agent_header]]`).
- **Correcting a false zero from earlier the same session:** an initial probe for `"Tricolor Auto Receivables Trust <year>-<n>"` returned zero across 2018-2022 and briefly read as "no Tricolor ABS on EDGAR." The stem was wrong — the shelf is **Securitization**, not **Receivables**. The positive control (Exeter 2021-1 = 2,187 hits; SDART 2019-1 = 1,080) proved the query path, which is what forced the name check rather than accepting the zero (`[[finding_discovery_tool_wrong_slice_false_zero]]`).
- **The 144A finding was the decisive scoping step** and came from the filing-type histogram: 11 filings, all ABS-15G, no 10-D. That single check converted an open-ended thread into a bounded task.
