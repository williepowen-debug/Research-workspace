# CREED News Sweep — RESULTS
**Date:** 2026-08-13 · **Window:** 2026-07-27 → 2026-08-13 · **Plan:** `2026-08-13_NEWS_SWEEP_PLAN.md`

**Summary: 10 threads investigated / 2 MEANINGFUL / 0 routed cross-domain / 2 LEADS.** Nothing threshold/band-touching resolved — see §4.

---

## 1. MEANINGFUL

### 1a. FDIC Q2 2026 QBP — **NOT overdue; STATUS.md's "3 weeks past estimate" line was WRONG, correcting it**

[FDIC.gov `quarterly-banking-profile`, fetched 2026-08-13] **Q2 2026 has not published.** FDIC's own stated cadence: *"published about 55 days after the end of the quarter — around late May, late August, late November, and late February."* Q1 2026 published **5/27/26** (57 days after 3/31). Applying the same lag to 6/30/26 → **expected ~8/24–8/29/26**. That is **11–16 days from today**, not overdue.

⚠️ **Self-correction:** this session's earlier STATUS.md catch-up wrote *"FDIC Q2 QBP... now ~3 weeks past its 7/27 estimate, most overdue item."* That conflated CREED's own 17-day dark stretch with the print's own release cadence — the print was never estimated to land before late August, so nothing about it is actually overdue yet. **Corrected in STATUS.md this session** (see commit).

### 1b. ACRE (Ares Commercial Real Estate) Q2 2026 — dividend HELD, but a coverage shortfall — CREED's own cohort, `VX-CREED-10.01`

[Q2 2026 earnings release + call, 8/4/26 — Motley Fool transcript, StockTitan, GAAP release] GAAP net income **$4.4M ($0.08/sh diluted)**; **Distributable Earnings $6.9M ($0.12/sh)** — **below the $0.15/sh dividend declared for Q2 AND Q3**, a real coverage shortfall, not covered by distributable earnings this quarter. Office exposure fell **39% → <25%** of the loan portfolio YoY — real de-risking. `$106M` available capital, 2.0x net debt/equity.

**Flagged, not resolved:** ACRE is currently carried as one of the **8 of 11 HELD-flat** names in `VX-CREED-10.01` and is the underlying test population for `PRED-CREED-004` (≥1 additional cut beyond ARI/KREF/RC, 60% confidence). **The dividend was NOT cut this quarter** — held at $0.15/sh for both Q2 and Q3 — so this does **not** move `PRED-CREED-004` or the 10.01 cohort count. The distributable-earnings shortfall is a leading indicator worth carrying into next session's workbook refresh, not a fired signal.

## 2. LEADS (single-source or unverified — not carried as findings)

### 2a. ACRES Commercial Realty (ticker **ACR** — distinct from ACRE and from RC/Ready Capital; formerly Exantas Capital) — Q2 2026 GAAP net loss

[PR Newswire / StockTitan, 8-K, dated within window] **GAAP net loss $(12.5)M, $(1.87)/sh diluted**, Q2 2026. **Not currently in CREED's tracked 11-name cohort.** Three visually-similar tickers exist in this space (RC, ACR, ACRE) and this sweep confirms they are three distinct companies — flagging the potential confusion explicitly rather than risk a future session conflating them. **Lead for next session:** decide whether ACR belongs in the cohort watch; not added to `VX-CREED-10.01` this session (no coverage-scope change made mid-sweep).

### 2b. CMBS new-issuance YTD figures — a scope discrepancy in the secondary reporting, not resolved

[Scotsman Guide, headline vs body] Headline: *"CMBS issuance passes $76 billion in the first seven months of 2026."* Body of the same underlying KBRA-sourced coverage: *"private-label CMBS and CRE CLO issuance totaled $103.9 billion, up 21% from $85.7 billion"* for the same period. These may be different scopes (CMBS-only vs. CMBS+CRE-CLO combined) rather than a contradiction, but I have not verified which — **flagging the discrepancy rather than picking a number.** Separately: conduit spreads cited **AAA +70bp / BBB- +415bp**, SASB AAA **+85 to +175bp** [same secondary source, undated primary]. **Coverage-gap note:** CREED's workbook carries no vector for new-issuance volume or spread color at all — worth a §10 (Mechanism) or new-category candidate next session if this becomes thesis-relevant; not added this session.

## 3. Checked, found nothing new / explicitly excluded

- **"$25B CMBS past-maturity" figure** — traced to **The Real Deal, dated 2026-02-17.** This is the anniversary/stale-recirculation trap the plan named explicitly: a February article resurfacing in a general search. **Excluded — do not cite as an August finding.** (It is almost certainly the same January-vintage data underlying CREED's already-held 12.34% January office DQ ATH.)
- **Ready Capital $943M loan sale** — dated **2026-04-01.** Outside window, already old news by 7/27. Excluded.
- **Bank of America Plaza (St. Louis) REO sale** — foreclosed summer 2025, auctioned May 2026, sold **June 2026 for ~$9.5M+.** A real forced-sale comp with a price, but dated outside this window. Noted for context only; not a sweep finding.
- **Bank CRE provisions (Citizens $134M↓ from $140M, Northern Trust negative provision, Customers Bancorp flat $23M, BCB Bancorp)** — checked, mixed/directionally-improving picture consistent with CREED's existing base case, but this is squarely REGINALD's dedicated bank-desk lane, which per this week's cross-agent record already runs a comprehensive 11-name read-through. Not routed — my incidental 4-name sample would be redundant with, and inferior to, REGINALD's own tracking. No packet sent.
- **Servicer/ARA background resources** (`crefc.org` "State of CRE Servicing Midyear 2026," dated 7/8/26; an ARA-trends spotlight dated 5/6/26) — both pre-date the window. Useful background for FORUM 5's W1 leg (maturity-adjusted DQ availability) next session; not sweep findings.
- **GSE/multifamily** — no new items found this sweep; HOMER's lane, already current per this session's earlier packet exchange.
- **BROCK's vehicle-side (BDC/private-credit)** — out of scope for a CRE/CMBS-focused search sweep; nothing surfaced.

## 4. Threshold/registered-item touches — flagged, not resolved

- **`PRED-CREED-004`** (≥1 additional CRE mREIT dividend cut) — ACRE's coverage shortfall (§1b) is adjacent but does **not** fire it; the dividend was held. ACR's net loss (§2a) is a name currently outside the tracked cohort. **No grade change.**
- **No item in this sweep touches `PRED-CREED-001`, `-006`, or `-010`.** August Trepp hasn't printed; nothing here substitutes for it.

---
**Sources:** all inline above, each dated. Trepp figures throughout remain **primary-cited, never primary-read**, per standing caveat. No `PREDICTIONS.tsv`/`VX.tsv` edits made from this sweep — findings are flagged for next session's workbook pass.
