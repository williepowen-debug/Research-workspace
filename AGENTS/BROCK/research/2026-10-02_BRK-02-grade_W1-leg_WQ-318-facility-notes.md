# 2026-10-02 — BRK-02 graded · L182 W1 BROCK leg run · WQ-318 facility notes read

**Written:** 2026-10-02 Fri from 09:31 ET by BROCK (PROME follow-up on Will's 09:23 ET "go for all four"). $0. No trade view.

---

## 1. BRK-02 — "Industry non-accruals rise to >2.5%" (75%, made 2026-02-23, resolve 2026-09-30) — ❌ RESOLVED-FALSE

**Resolver of record:** `domain/sources/BRK02_INDUSTRY_INSTRUMENT_BLIND_SPEC_AUG13.md` (Will-ratified 8/13). Required: quantity NON-ACCRUALS · form RATE · basis COST · population INDUSTRY (broad, selection independent of outcome) · standing series · reading published by 9/30. The six-name median is a TELL, never the resolver (ruling ⑤a). Bodies opened only now — after 9/30, as §5 allows.

### 1a. Every candidate found, at the publisher's own page (raw HTML read 2026-10-02 ~09:2x ET, not via summarizers)

| Instrument | Class (spec) | Population | Statistic | Basis | Q2-26 | Prior | Published | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---:|---:|---|---|---|---|---|
| **Octus BDC Nonaccrual Report** | §6(a) SEC-derived aggregate | **over 170 BDCs** (174 in Q1) | **aggregate**, $ in nonaccrual ÷ all BDC debt investments | **cost** | **1.90%** ($9.5B) | **2.02%** Q1 ($10.0B) | **2026-09-18** | ✅ | ✅ broadest | ✅ quarterly | ✅ |
| KBRA BDC quarterly analysis | §6(b) agency review | 35 KBRA-rated BDCs; figure is the **non-perpetual-life** subset | **median** | cost | **2.75%** | 1.81% Q1 | secondary 2026-09-07 (Alternative Credit Investor) | ✅ | 🟡 rated universe + subset | ✅ | ✅ |
| Morningstar DBRS commentary | §6(b) agency review | ~60 BDCs, DBRS coverage | **average** | cost | **3.4%** | 3.1% Q4-25 · 2.9% Q4-19 | **2026-08-25** | ✅ | 🟡 coverage universe | 🟡 INFERRED standing | ✅ |
| Fitch 32-rated-BDC review (the spec's named survivor) | named | 32 rated BDCs | — | unverified | **no figure found** | 1Q26 edition 2026-06-18, "non-accruals increased", no rate in any readable copy | 2Q26 edition SEARCH-NOT-FOUND by 9/30 | ❌ unverified | — | ✅ | ❌ |
| Fitch Private Credit Transparency Monitor 2Q26 | §6(b) | BDC portfolios | none ("broadly stable quarter over quarter") | — | — | — | 2026-09-16 | ❌ no rate | — | — | — |
| PitchBook LCD universe | §6(a) | 213 BDCs, $516B debt | aggregate | cost | not found | 1.9% Q1-26 | Q1 only | ✅ | ✅ | 🟡 | ❌ no Q2 found |

Sources: octus.com/resources/articles/bdc-weekly-review-reported-nonaccruals-decline-sequentially/ (Sep 18, 2026: *"The aggregate debt nonaccruals represented 1.9% of total aggregate BDC reported debt investments (at cost) in the second quarter, down from 2.02% the prior quarter"*) · octus.com/resources/blog/data-drop-bdc-nonaccruals-q126/ (Jun 12, 2026, universe 174) · dbrs.morningstar.com/research/487859 (Aug 25, 2026: *"average non-accruals increased to 3.4% of investment portfolios at cost as of Q2 2026, from 3.1% in Q4 2025"*) · alternativecreditinvestor.com/2026/09/07/… (KBRA: *"median non-accrual investments increased to 2.75 per cent of total investments at cost, up from 1.81 per cent in the first quarter"*, 35 rated BDCs) · theleadpc.com Fitch syndication via WP REST API (Fitch reports dated 18-06-2026 and 16-09-2026).

### 1b. The grade, and why this instrument

**Resolving instrument: Octus, 1.90% at cost for Q2-26 — below 2.5%, and falling (2.02% → 1.90%). ⇒ BRK-02 RESOLVED-FALSE.**

- **Why Octus — from text written blind on 8/13, not chosen today:** spec §1 fixes population = INDUSTRY ("a broad private-credit / BDC population, not a hand-picked set"), and §6 ranks class (a) "SEC-derived aggregations compiled from BDC 10-Q non-accrual disclosures at cost — **best definition-match in principle**". Octus is that class, over essentially the whole registered universe. KBRA and DBRS are class (b) with rated/coverage universes — the same "rated ≠ industry" qualification the spec put on Fitch.
- **The named survivor (Fitch) does not resolve:** no Fitch non-accrual RATE for 2Q26 published by 9/30 that I could read; its 9/16 Transparency Monitor says "broadly stable" — consistent with Octus's direction.
- **The disagreement is real and is recorded, not hidden.** The rated-universe readings fire: KBRA 2.75% (median, non-perpetual-life subset) and DBRS 3.4% (average). The gap is mostly STATISTIC: a dollar-weighted aggregate is dominated by the large perpetual non-traded BDCs (e.g., BCRED 2.2% at cost, Q2), while a median or simple average counts each small listed BDC equally. ⚠️ DBRS was already 3.1% at Q4-25 — above the line before the letter was written — so it cannot show a "rise to" anything.
- **No tie-break was pre-registered** among several qualifying instruments. The spec's C2 text and §6 ranking decide it. If PROME or Will reads the letter as "a typical BDC" rather than "the industry", the grade would flip to TRUE on KBRA — that reading is not the one the spec registered.
- **Conflict and direction:** I am conflicted (the thesis is mine). The grade goes AGAINST my book; the flattering reading (TRUE on KBRA/DBRS) was available and is declined on the spec's own text.
- ⚠️ **Contamination disclosed:** search-engine summaries showed me values from several candidates (KBRA 2.75, PitchBook 1.9 Q1, a "20-largest median 2.8%") before I had qualified any instrument. The selection rests on the 8/13 text, not on those values.
- ⚠️ **Attribution error caught:** a search summary attributed KBRA's 2.75% to **Fitch**; the publisher's text says KBRA. The same summaries attributed a "20 largest BDCs median 2.8%" to Fitch, which I could not find at Fitch. Neither was used. (`[[finding_attribution_authenticates_a_figure_its_named_source_never_produced]]`.)

**Invalidation / Action_If_Falsified check:** the row's invalidation is "non-accruals decline 2 consecutive quarters" → kill leg "trim/close APO Dec $95P overlay". **NOT met:** Octus fell once (Q1 → Q2); it rose Q4-25 → Q1-26 (+40% in dollars). KBRA and DBRS rose. ⇒ **No position consequence**, and any disposition of the put is Will's regardless. **Confidence calibration:** a 75% call missed on its registered instrument.

**No score moves.** The Default-rates vector (🔴4) keys on ">7% at a non-CDLI top-tier name OR CDLI NA >1%" — not this. Recorded as a counter-datum in the REGIME BLOCK.

---

## 2. L182 W1 — BROCK leg: "enumerate PRICE-PRODUCING exits to give the no-print counter a denominator"

**Definitions (FORUM P2 §4a, 8/13):** a NO-PRINT exit = a disclosed transfer of PC exposure out of a vehicle with no arms-length loan-level price, via GP-led secondary, IG wrap, affiliate/related-party transfer, or deferred consideration. Its complement, a PRICE-PRODUCING exit, transfers exposure at an arms-length price. W1 asks whether an existing public surface lets them be enumerated.

**Pre-stated 08:3x ET, before any search:** *"FOUND functionally — BDC 10-Q/10-K schedules + realized-gain notes name exited positions with proceeds vs cost; perimeter-limited (BDCs only)."*

**Run:** Q2-26 10-Qs of five of the six-name set read at EDGAR (ARCC 0001628280-26-050307 · FSK 0001628280-26-053783 · OBDC 0001655888-26-000056 · OCSL 0001414932-26-000017 · MFIC 0001193125-26-335848; OTF not located — CIK lookup failed; not run).

| What the filings carry | Example (Q2-26 unless stated) | Price-producing exits enumerable? |
|---|---|---|
| Exits in AGGREGATE, sales and repayments MERGED | ARCC "Sales, repayments or exits of investments" **$3,026M**; cash-flow "Proceeds from sales and repayments" at all five; OCSL "exited 26 portfolio companies" (9M); MFIC "Number of exited companies (7)" | ❌ no split by route or price |
| Named realized gains/losses for "significant" items only | MFIC "Significant realized gains (losses)" table (Renovo −$9.0M, 6M) — restructurings/write-offs | ❌ not arms-length sales; selective |
| Block sales with a block-level price | OBDC Feb-2026: $357.6M FV sold at **99.8% of par**, 74 companies, "to certain purchasers" (purchaser unnamed ⇒ arm's-length status UNKNOWN) | 🟡 event-level price, not per loan |
| Affiliate transfers (the NO-PRINT side) | ARCC: **$1,087M (Q2) / $2,128M (H1)** of loans sold to IHAM or IHAM vehicles (its own controlled affiliate) | n/a — numerator, not denominator |

**Result: NOT FOUND for enumeration · PARTIAL for bounds.** No public surface enumerates price-producing exits loan by loan. The filings give an UPPER bound (total exits per BDC per quarter, route unsplit) and occasional event-level prices (block sales).

**Graded against the pre-statement — they DIFFER:** I expected 10-Qs to "name exited positions with proceeds vs cost". **They do not**, except for selected "significant" realized items, which are mostly restructurings. The pre-statement over-claimed the surface. The perimeter caveat (BDCs only) was right but moot.

**Self-check:** NOT FOUND supports the bloc's opacity claim, which is partly mine — the flattering direction. It stands on the table above: the absence is of a ROUTE + PRICE split per exit, checked in five filings, not a failed search.

**A finding the leg was not asked for, recorded because it cuts against the counter as built:** ARCC alone moved **$1.09B in Q2-26** to its affiliate IHAM. Under definition (iii) (affiliate/related-party transfer) that is no-print volume, so the counter's "current count: 2" (8/13) is a large undercount if affiliate sales qualify. Whether they do is a definition question for the counter's registration (FORUM ruling 4), not decided here.

**Tally for PROME (W1 withdrawal test, ≥2 of 4 legs finding an existing surface):**
| Leg | Strict reading | Functional reading |
|---|---|---|
| CREED VX-3.01 | FOUND | FOUND |
| SHADE (a) gated US routes | NOT FOUND | FOUND (Athene IR site) |
| SHADE (b) AARe Note-14 | NOT FOUND (as pre-stated) | NOT FOUND |
| **BROCK price-producing exits** | **NOT FOUND** | **NOT FOUND (bounds only)** |
| **Total** | **1 of 4 — not withdrawn** | **2 of 4 — withdrawn** |

⇒ Per DOCKET L182, a BROCK NOT-FOUND sends the strict-vs-functional question to Will (the test was Will-approved 8/13). My leg does not change either reading's count.

---

## 3. WQ-318 — the facility notes (upgrade of my 08:4x "NONE FOUND")

Read the debt notes of ARCC, FSK and OBDC Q2-26 10-Qs (same accessions as §2).

| Lender | Borrower (PC vehicle) | Facility | What changed | Source | Fit |
|---|---|---|---|---|---|
| **JPMorgan Chase Bank, N.A.** (administrative agent), **ING Capital LLC** (collateral agent), lenders party | **FS KKR Capital Corp (FSK)** | Third A&R Senior Secured Revolving Credit Agreement (7/16/2025); **Amendment No. 1, 2026-05-08** | **(b) TIGHTER + covenant amendment:** commitments cut **$4,700.0M → ~$4,051.7M (−13.8%)**; margin **+12.5bp** (term SOFR 1.65% → 1.775% at borrowing base ≥1.60x; 1.775% → 1.90% below); minimum Shareholders' Equity floor reset **~$5,048.6M → $3,750.0M** (loosened to fit a lower NAV); "non-extending lender" language. 6/30: $733M drawn, $3,017M available | FSK 10-Q Q2-26, Note 9 + MD&A table | ✅ **FOUND** |
| Sumitomo Mitsui Banking Corp. (agent) | ARCC (via ACJB) | SMBC Funding Facility | commitment **$1,100M → $1,600M**; accordion $1,300M → $2,500M; drawn $563M → $728M | ARCC 10-Q Q2-26 | opposite sign — lender EXPANDING |
| BNP Paribas (agent & lender) | ARCC (via AFB) | BNP Funding Facility | commitment **$1,265M → $1,465M**; drawn $717M → $674M | same | opposite sign |
| (syndicate) | ARCC | Revolving Credit Facility | commitment $5,493M → $5,481M; drawn **$2,028M → $1,566M** (utilization ~37% → ~29%) | same | utilization FELL |
| Truist Bank (agent) | Blue Owl Capital Corp (OBDC) | Revolving Credit Facility, 3rd amendment **2026-06-25** | maturity extended to 6/25/2031; revolver **$3.95B → $3.93B** (−0.5%) "for certain lenders"; pricing not read | OBDC 10-Q Q2-26 | benign |

**Upgrade: NONE FOUND → FOUND, n=1 named — FSK's JPMorgan-agented revolver: smaller, more expensive, with the equity covenant reset.** Counter-evidence at the same depth: ARCC's bank lenders ENLARGED their lines and ARCC drew less. That is bifurcation — banks tightening on the weakest large BDC (FSK: 7.1% non-accrual at cost Q2, the highest of the six-name set) and expanding to the strongest. **No attributable bank LOSS found.** Not read: OCSL, MFIC, OTF facility notes; BCRED/OCIC/North Haven (not in this pass).

**No threshold fires:** my "BDC revolving facility draws spike → LIQUID 🔴" row is not met (FSK and ARCC draws FELL). Bank warehouse/NDFI vector (🟠3) keys on a reserve BUILD at one of the 11 banks (BRK-31) — this is a lender-side term change, not a reserve build. No rescore.
