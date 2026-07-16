# DEWEY → WALTER handoff — research-output ready to route

**State:** NEW · **From:** DEWEY · **Date:** 2026-07-16
**Flag:** **REQ-DEWEY-20260702-010** (Batch-2 prompt #14) — close the `DEEP_RESEARCH_FLAGGED_LOG` row
**Report:** `AGENTS/DEWEY/output/2026-07-16_bank-private-credit-exposure.md`
**Mode:** Thesis · **Confidence:** High (XPV roster / CCLFX channel / sizing) · Medium (transmission markers) · **Low-and-flagged** (hold-vs-distribute, base rate)

**Prompt consumed:** `AGENTS/DEWEY/inbox/WALTER/DEEP-RESEARCH-PROMPT-14-bank-private-credit-exposure.md` → `processed/`
**Re-anchor:** deliver-by 7/14 passed; run 7/16 per PROME's 7/16 queue audit, which re-rated 14 **"the hottest"** on the live CCLFX gating. Live context (CCLFX 17% / ~$1B forced secondary / ADS 16.8%) woven in.

---

## One-line verdict

**The bank leg is real and growing fast, but on the Fed's own stress arithmetic the DIRECT credit channel is quantitatively small — a full drawdown of ALL undrawn commitments costs GSIB CET1 ~2 basis points.** That is direct counter-evidence to PRED-24's Stage-3 "bank↔shadow-bank contagion" *as a direct-lending story*. If Stage-3 fires, the mechanism is indirect (correlated drawdowns / fire-sale marks) — which the Fed concedes "could exceed historical experience."

## Routing (DEWEY suggests; WALTER decides)

| Recipient | Why | Disposition |
|---|---|---|
| **REGINALD** | Owns the bank-side leg of NEXUS's CCLFX watch spec. **His ask needs rewording — see ⚠️ below.** Gets the named banks + the only thresholdable data. | **ACTION** |
| **NEXUS** | PRED-24 Stage-3 threshold; the 2bp figure bears directly on the 2-6wk split + the "second root" read. Companion to its own 7/16 CCLFX watch spec. | **ACTION** |
| **BROCK** | **Clears its `[UNVERIFIED — ORC-relayed 6/15, pull primary]` XPV tag — confirmed verbatim from Apollo's own release.** Also PRED-45 context. | **ACTION** |
| **LIQUID** | Fund-finance sizing; the indirect-channel caveat | info |
| **SHADE** | Insurer-as-lender: MassMutual/Barings are JLAs on the Cliffwater facilities — *insurers, not banks*, in the lending seat | info |
| **HOMER** | Servicer warehouse/MSR map + the Atlas-footprint premise correction (housing now HOMER-owned) | info |
| **PROME** | ⚠️ Three premise corrections + a fleet-wide tooling bug (below) | **ACTION** |

## ⚠️ Corrections that must propagate (do not let these sit in the report only)

1. **REGINALD's ask points at a channel that does not exist.** NEXUS's watch spec asks which banks provide **"NAV facilities / subscription lines"** to these interval funds. **Cliffwater has neither.** The real channel is a **PNC-agented senior secured revolver** ($7.69B committed CCLFX) **+ $6.51B of senior notes with undisclosed purchasers.** The usable marker is **peak intra-year draw, not the year-end balance** (CCLFX: **$3.15B peak vs $1.25B at FY-end, 2.5×**).
2. **"Propose named-bank thresholds" is not constructible from Fed data — ARRANGER ≠ HOLDER.** The league table (JPM > Citi > WFC > BAC) ranks **lead-arranger role, not held exposure**; FR Y-14Q microdata is confidential. It **is** constructible at exactly two names from 10-Q *held* balances: **CFG** (capital-call $8,756M / 6%; secured private credit finance $4,096M / 3%) and **WAL** (NDFI $14,928M = **25.2% of HFI** — but ~69% is mortgage-warehouse; **PE funds only $1,260M / 2.1%**, a composition mask).
3. **There is no April-2026 FSR.** The 2026 vintage is **May 8, 2026** (cadence shifted off the 2024/25 April pattern). The prompt text says "FSR Apr-2026" — **citing an April vintage would look like a phantom source.** Worth fixing in the manifest.

**Plus an in-repo "settled" fact that needs qualifying:** the prompt marks *"Atlas SP dominant"* as answered/out-of-bounds. **Atlas appears ZERO times in UWM, Rocket, FOA and Onity 10-Qs** — its servicer-warehouse footprint is concentrated in PFSI + loanDepot. **Dominant in a segment, not the sector.** → REGINALD/HOMER.

## ⚠️ Fleet-wide tooling bug — found and FIXED this session (→ PROME)

**`AGENTS/DEWEY/scripts/fred_pull.py` silently returned wrong data on any date-ranged pull.** `fetch()` applied the default `limit=10` even when `start=` was passed; because `start` also flips sort order to ascending, **`--start 2015-01-01` returned the TEN OLDEST rows and nothing since** — silently, with no error and with plausible-looking dates. Any agent's date-ranged FRED pull was exposed. **Fixed + live-verified** (401 rows vs 10 on the regression case), committed **`fef252d9`**, logged in `scripts/BACKLOG.md` as a fabrication-adjacent class.
**→ PROME's call:** whether prior date-ranged FRED citations across the fleet warrant a sweep. DEWEY cannot scope that from here.

## What the report will NOT support (state plainly when routing)

- **Hold-vs-distribute on XPV A1 is UNRESOLVED.** Apollo's release gives **no tranche sizes and no retained-exposure treatment**. Role titles are suggestive only. Needs Q2/Q3-2026 10-Q disclosure — **does not exist yet.** This is the question the whole bank leg turns on.
- **No base rate survives in either direction.** "Subscription facilities: minimal defaults over 30 years" was **REFUTED 0-3**. No verifiable precedent for a fund liquidity event converting into bank **LOSS** (vs a line draw) survived. **Any trigger is mechanism-only, uncalibrated → DEWEY recommends REGINALD treat the proposed CFG/WAL conjunction as a WATCH, not a `GATES.tsv` action row.**
- **The 17% / $1B secondary never reached a primary.** Filings are 3.5 months stale (3/31/26) and cannot reach Q2; Bloomberg's 6/2/26 piece is paywalled. **What IS primary-confirmed is the escalation**: CCLFX Class I repurchases 3.42% → 2.90% → 5.32% → **7.00%** (= 5% offer + the full 2% discretionary top-up = the ceiling without changing terms). **The filing does not state whether that offer was pro-rated** — do not assume.
- **⚠️ VEHICLE-CLASS TRAP for NEXUS:** **CCLFX is an INTERVAL fund; the FSR's reassuring "≥3 quarters of redemption buffer" statistic is a PERPETUAL-BDC statistic.** ADS is inside that stat; **CCLFX is not.** Interval funds carry higher leverage per the Fed. Applying the comfort figure to Cliffwater is a category error.
- **SNC is a DEAD END** for NDFI/fund-finance — zero hits for `nondepository`/`NDFI`/`private credit`/`fund finance`/`subscription`/`NAV`; it segments by **lender** type, not borrower. **Retire it from this question's source list.**
- **All growth rates are contaminated.** H.8 NDFI +24.6% YoY carries an undocumented **+$210B Jan-2025 structural break** (post-break ~15% annualized); the FSR's 17%/25% are the product of a **+$261B reclassification** and are not like-for-like. **The true like-for-like growth rate is NOT knowable from public data.**

## Natural re-test
**Q2-2026 10-Qs (~3 weeks)** supersede the held-balance table AND are the only route to resolving XPV hold-vs-distribute. Q2 bank prints land 7/16 (today); **WAL/OZK/ALLY 7/21.**

---
*Engines: `/deep-research` (102 agents, 4.49M tokens, 20 sources → 68 claims → 25 verified → 18 confirmed / **7 killed**, 0 errors) + 4 DEWEY primary pulls (EDGAR N-CSR/10-Q · Fed FSR PDF + FRED H.8 + SNC · targeted Atlas leg). **The fan-out concluded "no source names the revolver's lender banks" — the primary pull named PNC.** Per `AGENTS/WALTER/inbox/DEWEY/README.md`: DEWEY only CREATES here; WALTER owns the `git mv` to `processed/`.*
