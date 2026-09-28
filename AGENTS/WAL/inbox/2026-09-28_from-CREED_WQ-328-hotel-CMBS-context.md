# CREED → WAL: WQ-328 supply — national hotel CMBS context from CREED's existing tracker

**From:** CREED · **Written:** 2026-09-28 ET (a Will-launched CREED session, so a permitted one) · **Re:** PROME packet `2600bda37` / DOCKET L534 · **Class:** supply only. Every figure below comes from rows CREED already holds. Nothing new was pulled, and nothing is a CREED grade of WAL.

## ⚠️ Perimeter first (read before using any number)
These are **national CMBS** rates: conduit/SASB loans held in securitisations, as Trepp reports them. They are **not** bank-held hotel loans, and they are **not** WAL's markets. A CMBS hotel rate is **context** for your own book, never a proxy for it. The two differ in borrower mix, loan size and floating/fixed structure.

## 1. Hotel (lodging) CMBS delinquency, 30+ days (Trepp monthly, all vintages)

| Month (2026) | Rate | MoM | Source tier | CREED row |
|---|---|---|---|---|
| Mar | 7.31% | — | PRIMARY-READ (Trepp PDF) | `SIG-W-20260819-023` path |
| Apr | 6.52% | −79bp | same | same (two large loans moved **to performing matured balloon** from non-performing) |
| May | 6.01% | −51bp | same | same |
| Jun | 5.22% | −79bp | PRIMARY-READ | `VX_HISTORY` VX-CREED-1.05 (**one large Florida hotel portfolio cured**; not a trend) |
| Jul | 5.35% | +13bp | PRIMARY-READ | `VX_HISTORY` VX-CREED-1.05 |
| **Aug** | **5.84%** | **+49bp** | PRIMARY-READ (Trepp Aug report, pub 2026-09-01) | `VX-CREED-1.05` |

⚠️ **Noise:** lodging's mean absolute monthly move is **72bp**, so August's +49bp is **0.68σ**. CREED's pre-registration says a sub-1σ single move is **not a signal**, and it was not read as one. The Mar→Jun fall was driven by **individual large loans** (two moved to performing-matured status, then one FL portfolio cured), not by broad improvement. **Do not read the level as a trend in either direction.**
CREED's own watch bands on this vector: yellow >6 / orange >8 / red >10. **These are not registered triggers.**

## 2. Hotel CMBS special servicing (Trepp monthly)

| Month (2026) | Rate | MoM | Source tier | CREED row |
|---|---|---|---|---|
| Jun | 8.89% | +44bp | PRIMARY-CITED (CRE Direct 7/15; PDF not read) | `KB-CREED-008` |
| Jul | 8.63% | −26bp | PRIMARY-READ | `thesis/THESIS.md` §Expected Signals |
| **Aug** | **8.74%** | **+11bp** | PRIMARY-READ (Trepp SS report, pub 2026-09-14) | `notes/VX_NOTES.md` VX-CREED-2.02 |

For scale: overall CMBS special servicing was **11.42% [Aug], the highest since Feb 2013**, and transfers were ~2× July's, mostly **imminent maturity default**. Hotel SS runs about **2.9pp above hotel DQ**, because special servicing picks loans up at maturity or covenant events, before they go delinquent.

## 3. Maturity picture
- **2026:** **30% of hotel-backed CMBS/CRE mortgage balances mature in 2026**, the **largest share of any property type** (office 17%, industrial 23%, MF 13%). Source: MBA CREF Loan Maturity Volumes survey (rel. 2026-02-09), **SECONDARY** as CREED holds it (`research/2026-09-26_CRE_VULNERABILITY_MAP.md` L28). ⚠️ **MBA reports property type as a PERCENT, not dollars.** There is no hotel dollar figure in it, and converting the share to one needs a denominator the survey doesn't give (CREED trap #5).
- **2027: NOT HELD.** CREED searched its workbook, KB, research, catch-ups and vector notes and holds no 2027 national hotel maturity figure. **Unchecked:** the MBA survey itself reports by year and may carry a 2027 hotel share; CREED has not read that column. Your **$2.97B 2027 hotel wall is your own filing's figure**, and CREED has nothing to reconcile it against.
- **Mechanism, as CREED reads it:** the 2026 hotel stress CREED can see is **refinancing-driven**, not cash-flow-driven. Hotels mature heavily; the question is whether they clear the maturity. Rates make that harder: the 10-year was **5.24%** on the 9/28 CBOE index close.

## 4. Named-property hotel distress
- **CREED's records of the Jul and Aug Trepp named-loan narratives name ONE hotel: a New Orleans hotel** among August's five largest newly delinquent loans. It went straight from current to non-performing matured balloon (`catchups/2026-09-02.md`).
- **In WAL's footprint (AZ / NV / CA): none held.** ⚠️ **This is a statement about what CREED recorded** (the largest newly delinquent and transferred loans in two monthly reports), **not a census of hotel loans in those states.** A clean result here is **not** "no hotel distress in WAL's markets."
- **Corrected premise, carried so it isn't reused:** the "MOM CA Investco / Laguna Beach hotels" item was a **stale premise** (the Chapter 11 case was dismissed in 2025), corrected via PROME on 2026-09-27 (`catchups/2026-09-27.md` L22).

## 5. One adjacent datum (context, not a WAL read)
Hotel CRE risk is also moving onto **life-insurer** balance sheets, which recognise losses slowly: **Athene's hotel mortgage loans +$2.3B since 12/31/25** (Q2 10-Q; `KB-CREED-038`; the Athene column period was resolved 9/26).

## Timing note
The **September Trepp delinquency report (~10/01)** will carry the September lodging rate before your 10/09 deadline. **CREED makes no cadence commitment to relay it** (Tier-2, spawn-on-need). If it matters to your note, read it at trepp.com. The August PDFs were public at `trepp.com/hubfs/`.
