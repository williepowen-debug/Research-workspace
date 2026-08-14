# Row-45 servicer thresholds — BASE-RATING EVIDENCE (⚠️ **PARTIAL — LDI + Onity only**)

**Status:** ⛔ **PARTIAL. THE SPEC REMAINS PROVISIONAL AND NOTHING HAS BEEN RE-ANCHORED.** This file discharges **part** of the dated obligation recorded on `docket/CATALYSTS.tsv` row 11 and `STATUS.md` OPEN ITEM 11.
**Covered here:** **LDI** (loanDepot) · **Onity Group** (formerly Ocwen Financial).
**NOT covered — the larger half of the panel:** **PFSI · RKT · UWMC.** Commissioned in the same session; **did not return inside the session window.**
**Date:** 2026-08-14 · **Author:** HOMER · ⛔ **Zero thresholds moved. Zero capital. No class was changed on the strength of this file.**

---

## 0. ⚠️ PREMISE CORRECTION I HAD WRONG GOING IN

I briefed the research with *"Ocwen did a 1-for-15 reverse split in Aug 2023 — verify."* **It was AUGUST 2020.** Articles of Amendment filed with Florida SoS **2020-08-04**, effective **2020-08-13**, split-adjusted trading from **2020-08-14**; authorized shares cut 200,000,000 → 13,333,333; **no capital raise attached.** *(8-K filed 2020-08-10, items 3.03/5.03, acc. `0001493152-20-015094` — PRIMARY.)*

⇒ **Every Ocwen/Onity per-share figure in this file is post-split**, and any pre-2020-08-13 per-share figure from another source must be divided by 15 before comparison. **This is the `finding_per_share_figures_break_across_splits` class, and I seeded it with the wrong year — the verify instruction is what caught it, not me.**

---

## 1. Observation windows — the denominator problem, confirmed at primary

| Company | Public window | Company-years |
|---|---|---|
| **LDI** (CIK 1831631) | **2021-02-11 → 2026-08-14** (IPO priced 2/11/21) | **5.5** |
| **ONIT** (CIK 873860, "OCWEN FINANCIAL CORP" on EDGAR through **2024-05-30**, "ONITY GROUP INC." from **2024-06-10**) | **2019-01-01 → 2026-08-14** (full) | **7.6** |

⇒ **13.1 combined company-years**, not the 15.2 a naive 2019–2026 window over two names would imply.

---

## 2. ★★ THE HEADLINE RESULT — and it lands squarely on Class E

**Population: 6 capital actions, 4 dividend events.**

| Screen | LDI | ONIT | **Total** |
|---|---|---|---|
| **(a) Raises ≥10% of market cap** | 1 (ATM **capacity** 22.4%, undrawn at 6/30/26) | 2 (2021 notes+warrants **115%**; 2024 Series B preferred **22.6%**) | **3** |
| **(b) …of those, priced ≥15% below VWAP / prior close** | 0 (ATM is at-market by construction) | 0 | **★ 0** |
| **(c) ≥20% dilution, non-growth use** | 1 (ATM, **conditional on full drawdown**; 0 executed) | 0 | **1 (0 executed)** |
| **(d) Dividend cut ≥50% or suspension** | **1** (2022-05-10, **−100%**) | **0 — no common dividend has ever existed** | **1** |
| **(d-ii) …unscheduled** | 1 | 0 | **1 — 100% of cuts in sample** |

### ⛔ THE FINDING THAT MATTERS MOST: Class E's two gates select DISJOINT events in this sample

**Zero of six capital actions clear BOTH the ≥10%-of-market-cap gate AND the ≥15%-discount gate.**

The near-miss makes the point precisely: **Oaktree's Dec-2020 private placement into Ocwen** was priced **−14.8% vs the 10-day VWAP at closing** (−26.5% vs prior close) — a genuine distress-priced deal — **but it was only 4.3% of market cap, so it never reaches the discount test at all.** Conversely the two deals that *are* ≥10% of market cap were **not** discounted (the 2021 warrant strike was **+3.3% ABOVE** the 10-day VWAP; the 2024 preferred has **no common-referenced price**, so its discount is **N/A, not zero**).

⚠️ **This is the `finding_compound_gate_jointly_unsatisfiable` shape and it must be base-rated JOINTLY and CONDITIONALLY, not leg-by-leg.** On this half of the panel, **Class E's conjunction has never fired in 13.1 company-years.** ⛔ **That is NOT yet a verdict on the spec** — n is small, the larger three names are missing, and UWM 8/6 (the event that motivated the re-spec) clears the size gate ~7×. **But it is exactly the evidence the obligation existed to produce, and it points at the CONJUNCTION, not the levels.**

---

## 3. ★ Class F has a structural blind spot this sample exposes

**Onity raised ZERO registered common equity in 7.6 years** — no 424B of any kind; every issuance was a Section 4(a)(2) private placement; both S-3s are **resale** registrations with no proceeds to the company.

**Yet it diluted twice, both structured off the tape:**
- **2021: warrants on 1,184,768 sh = 12.0% of then-outstanding common** (attached to $285M senior secured notes carrying a **12.3% OID**). Net-settled Feb + Dec 2025 for **462,762 shares = 5.4%**, with Onity **paying $3.5M cash**.
- **2024: Series B Perpetual Preferred, $52.79M liquidation preference = 22.6% of common market cap** — **0% common dilution** (non-convertible), so a common-dilution screen scores it as nothing.

⇒ **Class F is keyed to *"≥20% dilution of existing common."* A screen reading only common-share issuance would score Onity as having had NO dilution events in the entire window.** It had two, and the larger one is invisible to the class as written. **This is a scope gap in the spec, not a threshold-level problem — and it is not fixed by moving the 20%.**

## 4. ★ Class G — and the caveat I flagged in advance is confirmed at primary

> ***"We have never declared or paid cash dividends on our common stock."***
> — Onity Group FY2025 10-K, Item 5 (`ocn-20251231.htm`, filed 2026-02-17, **PRIMARY**). Identical language in the FY2023 10-K under the Ocwen name.

**Not "not since 20XX" — never.** ⇒ **Onity contributes 0 to the numerator AND 0 to the denominator of any dividend-cut base rate.** Including it as an at-risk observation would **bias the rate downward**, i.e. **flatter the spec** — the exact direction I flagged as the risk before the data arrived.

⇒ **Only LDI was ever eligible to produce a Class-G event: 5.5 company-years at risk, 1 event.** *(Onity does now pay **preferred** dividends — first Series B payment 12/15/2024, **$1.97/sh, $4.2M in FY2025** — which rank ahead of common and are a structural impediment to any future common dividend. Not a Class-G event; worth carrying.)*

**The one event, for the record:** LDI **2022-05-10**, inside the Q1-2022 earnings release — *"we are suspending our regular quarterly dividend for the foreseeable future"* — **$0.08 → $0.00 (−100%)**, alongside revenue $503.3M vs $1,316.0M year-ago and a $(91.3)M net loss. **Unscheduled**: not pre-announced policy, not tied to a disclosed strategic transaction. **It would fire Class G as written.** *(PRIMARY: EX-99.1 to 8-K acc. `0001831631-22-000130`; corroborated in the FY2022 10-K Item 5.)*

---

## 5. Two more things worth carrying into the spec

- **★ Governance concessions cluster in distress-adjacent deals, and the sharpest is DORMANT UNTIL TRIGGERED.** Onity's Series B converts into **two board seats** if dividends fall **six quarters in arrears** (board *observer* pre-NYSE-listing). **A contingent control transfer sitting on the cap table, invisible to any screen reading voting rights today.** Class E's "governance concessions" marker should be read to include **contingent** rights, or it will miss this shape.
- **★ "Discount to VWAP" needs a MEASUREMENT DATE or it is not a threshold.** Oaktree's $23.15 was **fixed 2020-12-21 and issued 2021-05-03** into a $31.51 tape: **−10.3%** measured at announcement, **−14.8% vs VWAP / −26.5% vs prior close** measured at closing. **Same deal, three answers, straddling the 15% line.** ⛔ **Class E does not currently say which date it measures. That is a spec defect and it is load-bearing — it decides whether this deal fires.**
- **LDI's IPO was itself distress-adjacent** and would not fire anything: cut from 15.0M sh at $19–21 to **3.85M at $14.00** (−30% vs the low end, **−74% on size**), with net primary proceeds routed to **buying out insiders including the CEO**. Recorded because a spec meant to catch "capital raised under duress" scored a zero here.

---

## 6. Provenance

- Filing universe from `data.sec.gov/submissions/CIK{0000873860,0001831631}.json` — all 8-K items 1.01/1.02/2.03/3.02/3.03/5.02/5.03/8.01 plus every S-1/S-3/424/FWP, 2019-01-01 → 2026-08-14; cross-checked via EDGAR full-text search. All pulls used a `User-Agent` header (the known 403 class).
- **All dollar amounts, share counts, cover prices, use-of-proceeds language and governance terms are PRIMARY** (8-K, 10-K, 10-Q, 424B3/B4/B5, S-3).
- **SECONDARY, and only these:** the 10-day VWAPs and historical closes used for market caps (yfinance daily OHLCV, typical-price weighted). ✅ **Positive agreement check:** the one price sourceable at primary — LDI's **$1.32** close on 2026-05-14 — appears on the 424B5 cover and **matches** the price feed.
- **NOT FOUND (not estimated):** LDI ATM shares actually sold — the Q2-2026 10-Q discloses the Sales Agreement but no proceeds; treated as **established-but-undrawn** through 6/30/2026.
- ⚠️ **One unreconciled PRIMARY-vs-PRIMARY conflict, recorded rather than resolved:** the 2024-11-05 8-K puts the Series B rate step-up after **2028-11-01**; the May-2025 S-3 says **2029-11-01**. Use the 8-K (contemporaneous with the Articles of Designation) **and cite the conflict.**

---

## 7. ⛔ What is still owed

1. **PFSI · RKT · UWMC** — the larger half of the panel, and the half containing the motivating event (UWM 8/6). **Commissioned this session; did not return in window.**
2. **Re-anchor, or explicitly re-affirm, the four numbers** once the full panel is in — **and per §2 the first question is the CONJUNCTION in Class E, not the levels.**
3. **Rule on the two spec defects this file surfaced**, both of which are **scope/definition** problems that moving a threshold cannot fix: **Class F's common-only dilution screen** (§3) and **Class E's undated discount measurement** (§5).

⛔ **Until all three are closed, the spec stays PROVISIONAL: no packet, no trade rail.**

— HOMER
