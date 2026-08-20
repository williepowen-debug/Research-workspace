# CREED REIT Equity Tape Module — 2026-06-21

**Purpose:** absorb the useful live-monitoring surface from dormant `AGENTS/REITS/` into CREED without treating old REITS workbook values as current.

**Source archive:** `AGENTS/REITS/`  
**Current owner:** CREED  
**Status:** module / tracker design (durable methodology below — trigger designs, tracker panels, guardrails).

> **Latest tape snapshot: 2026-08-20 (live pull).** **VNQ vs SPY 3mo = −0.34pp total-return / −0.98pp price-only** (window 5/19→8/20, 63 sessions, direct yfinance). **Negative on BOTH bases, so the sign is robust to basis choice.** `CREED-T-08a` (< −10pp): **~9.0–9.7pp away, NOT FIRED.**
>
> 🔴 **SUPERSEDED — read this before citing anything below.** This header previously read *"2026-07-27 INTRADAY … VNQ vs SPY **+2.04pp/3mo** — the relative has **FLIPPED POSITIVE**"*. **That reading is refuted in DIRECTION as well as level:** the counter-signal has moved **~2.4–3.0pp TOWARD** the trigger and is now **DECAYING, not strengthening**. The 7/27 figure states **no basis**, so the delta is directionally solid but **not verified like-for-like**. ⚠️ **`CLAUDE.md`'s pointer to this file said "latest tape snapshot 7/2" while this header said 7/27 — it had lagged by three weeks before today. Both corrected 2026-08-20.** ⚠️ **Instrument note: `FORGE/tools/market-data/fetch.py` has `price`/`fred` only — no history — so this figure CANNOT be produced by the standard tool; it needs a direct yfinance history call.** *(Prior snapshot for the trail: 7/27 intraday +2.04pp/3mo, +2.86pp/1mo.)*
>
> ⚠️ **THIS MODULE COVERS ONLY THE EQUITY LEG — and that was a blind spot until 2026-07-27.** THESIS Signal 8 has been **split into 8a (CRE equity) and 8b (CRE credit / commercial mortgage REITs)** because the two legs diverged hard: over the same 3mo window **7 of 11 CRE mortgage REITs were NEGATIVE** (median ≈ −9%) while equity REITs rallied, with **ARI winding down** (~$9B book sold to Athene at 99.7%) and **KREF cutting its dividend 60%** on risk-rated-5 office/multifamily/life-science reserves. **The mREIT row in the trigger table below ("route to LIQUID first; CREED only as adjacent tape") UNDERSTATED this leg — 8b is now a scored CREED vector set (`VX-CREED-10.01`–`10.05`), not adjacent tape.** Standing discipline: **never cite a CRE mREIT price move without checking corporate actions** (ARI's −37%/1mo was a $3.75 return-of-capital going ex).
>
> *Prior snapshots for the trail: 7/20 (VNQ −1.6pp/3mo; data-center DLR −13.4%/3mo, since unwound to −3.0%) · 7/2 (VNQ −2.9pp/3mo; office REITs +5–15% off the 6/18 baseline; OZK −5.7% lone dissent) — both in their dated packs.* The methodology and trigger designs below are unchanged except as noted above.

---

## Bottom Line

REIT public-equity tape is now a **CREED input**, not a standalone live agent.

Use REITs as a market-price / valuation / dividend signal for CRE recognition, not as independent thesis ownership. CREED owns the property-market interpretation; REGINALD owns bank implications; LIQUID owns rates/funding; CARL owns consumer spillovers.

---

## Scope CREED Now Owns

Public REIT / real-estate equity tape:

- broad REIT ETF stress: VNQ / sector REIT ETFs
- office REITs: SLG, BXP, VNO and peers
- retail REITs: SPG, KIM and peers
- residential / multifamily REITs where relevant to CREED/CARL
- industrial / data-center REITs as counter-signal or bifurcation evidence
- mortgage REITs only when book-value/dividend/MBS-spread stress matters to LIQUID
- NAV discount / cap-rate / public-private value gap signals
- dividend coverage, dividend cuts, and refinancing stress

---

## Durable Signals Pulled Forward From REITS

Treat these as trigger designs, not current values:

| Signal | Trigger design | CREED interpretation | Route |
|---|---|---|---|
| Office REIT capitulation | major office REIT NAV discount >50%, or office REIT basket breaks materially with confirming leasing/vacancy/default evidence | public market is pricing permanent office impairment | REGINALD if bank-exposed collateral/metros overlap; LIQUID if refi/funding driven |
| REIT sector stress | VNQ underperforms SPY by >10% over 3 months, or broad REIT ETF breaks while rates/funding tighten | CRE valuation stress is becoming public-market visible | LIQUID / HENRY; REGINALD only if bank transmission evidence appears |
| mREIT dividend/book-value shock | NLY/AGNC/STWD or peers cut dividends or show acute book-value erosion | mortgage spread / funding stress, not necessarily property CRE stress | LIQUID first; CREED only as adjacent tape |
| Retail REIT stress | major retail REIT reports >10% same-store NOI decline, occupancy deterioration, or financing stress | consumer spending / retail-property stress | CARL; REGINALD if collateral/bank exposure matters |
| REIT refinancing failure | major REIT cannot refinance at reasonable terms, tenders distressed debt, or signals asset sales forced by maturities | maturity wall becomes public issuer stress | LIQUID + REGINALD |
| Cap-rate expansion | transaction cap rates rise >100bp in a sector with observable price discovery | private marks should reprice; collateral value risk rises | REGINALD / CREED tracker |
| Dividend cut as recognition | office/retail/residential REIT dividend cut tied to NOI/refi stress | cash-flow impairment visible in public equity | CREED update; route by property type |

---

## Current Tracker Design

If CREED builds the monthly tracker, include a REIT tape panel:

| Panel | Metric | Frequency | Source examples | Notes |
|---|---|---|---|---|
| Broad REIT tape | VNQ absolute / relative to SPY | weekly/monthly | market data | confirmation/counter-signal, not thesis alone |
| Office REIT basket | SLG/BXP/VNO price, NAV discount, dividend coverage | monthly/earnings | filings, Green Street/broker notes where available | tie to office vacancy/leasing/default evidence |
| Retail REIT basket | SPG/KIM same-store NOI, occupancy, guidance | earnings | filings | route to CARL when consumer stress drives it |
| mREIT stress | NLY/AGNC book value, dividend, agency MBS spread stress | earnings/monthly | filings, market data | route mostly to LIQUID |
| Public-private gap | NAV discounts, cap-rate comps, forced-sale marks | monthly/event | Green Street, MSCI/RCA, broker/source notes | use to challenge stale private marks |
| Refinancing stress | maturity disclosures, tender/exchange/distressed asset-sale language | earnings/event | filings | route to LIQUID/REGINALD |

---

## Guardrails

- Do not import old `AGENTS/REITS/workbook/VX.tsv` values as current. They are Jan 2026 stale.
- Do not treat REIT price weakness alone as broad CRE→bank confirmation.
- Require mechanism confirmation: vacancy/leasing/default/refi/NOI/dividend/transaction evidence.
- CREED does not make trade recommendations from REIT tape. TERRY/Will own trade construction and approval.
- `AGENTS/REITS/` remains source archive only unless Will explicitly revives it.
