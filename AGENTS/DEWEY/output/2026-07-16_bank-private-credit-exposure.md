# Bank exposure to private-credit vehicles — fund-finance, XPV syndicate, Atlas SP, and the CCLFX channel
**Date:** 2026-07-16 | **Mode:** Thesis | **Confidence:** High (XPV roster, CCLFX channel, sizing) / Medium (transmission markers) / **Low-and-flagged (hold-vs-distribute, base rate — both unresolved)**

**Flag:** REQ-DEWEY-20260702-010 (Batch-2 #14) · **Deliver-by:** 2026-07-14 (run 7/16, +2d — see *Freshness re-anchor*)
**Engines:** `/deep-research` fan-out (102 agents, 4.49M tokens, 20 sources → 68 claims → 25 verified → 18 confirmed / **7 killed**) + 3 DEWEY primary pulls (EDGAR N-CSR/10-Q, Fed FSR PDF, FRED H.8) + 1 targeted Atlas leg.

---

## Key Finding

**The bank leg is real, growing fast, and — on the Fed's own stress arithmetic — quantitatively small through the direct credit channel.** A full drawdown of *all* undrawn commitments (+44pp utilization, $36B) would cut aggregate GSIB CET1 by **~2 basis points** and LCR by ~1pp; the Fed concludes "financial stability concerns from the direct credit channel seem limited" [PRIMARY: FEDS Notes, May 23 2025]. **This is direct, quantified counter-evidence to PRED-24's Stage-3 "bank↔shadow-bank contagion" premise as a *direct-lending* story.** If Stage-3 fires, the mechanism is almost certainly *indirect* (correlated drawdowns, fire-sale marks) — which the Fed itself concedes "could exceed historical experience."

**Two premises in the prompt did not survive contact with the primaries:**
1. **Cliffwater has no NAV facility or subscription line.** The channel REGINALD was pointed at does not exist at these funds. CCLFX/CELFX run a **single senior secured credit facility, administrative-agented by PNC**, plus $6.51B of senior notes.
2. **"Propose named-bank thresholds" is not constructible from Fed data** — the Fed league table ranks **lead-arranger role, not held exposure** (*arranger ≠ holder*). It **is** constructible at exactly two names — **CFG and WAL** — whose 10-Qs disclose *held* balances.

**The single best observable marker found is not in any regulator publication:** CCLFX's revolver stood at **$1.25B drawn at FY-end but peaked at $3.15B intra-year** (2.5×). Year-end balance-sheet snapshots systematically understate the line-draw channel.

---

## 1. The named banks (the deliverable)

### 1a. CCLFX / CELFX — the live gating name · **DEWEY primary pull; the fan-out could not reach this**
> The fan-out's verdict was *"No source names the revolver's lender banks."* The N-CSR does. This is the primary-pull-carries-the-verdict pattern.

**PNC Bank, N.A. is administrative agent + joint lead arranger on BOTH Cliffwater funds.** The other joint lead arrangers are **not banks**: MassMutual (CCLFX), Barings Finance LLC (CELFX, a MassMutual subsidiary).

**CCLFX facility** [PRIMARY: N-CSR filed 2026-06-08, FY-end 2026-03-31, [sec.gov](https://www.sec.gov/Archives/edgar/data/1735964/000121390026066324/ea0291746-01_ncsr.htm)] — entered 2022-03-29, **amended effective 2026-03-26**:

| Tranche | Committed | Outstanding 3/31/26 | Rate | Maturity |
|---|---|---|---|---|
| Term Loan | $1,426.5M | $1,426.5M (fully drawn) | 5.58% | 2032-04-23 |
| **Revolver** | **$4,842.5M** | **$1,250.0M** | 5.57% | 2031-03-26 |
| DDTL | $1,421.0M | $609.0M | 5.56% | 2032-04-23 |
| **Total** | **$7,690.0M** | **$3,285.5M** | — | — |

- **Accordion to $10.0B** (lender discretion). **Syndicate lenders NOT disclosed** — "certain lenders from time to time as parties thereto." The lender list lives in the credit-agreement exhibit, not filed with the N-CSR. *This is a disclosure-perimeter limit, not a search failure.*
- **Senior Notes $6,509.6M** (net), purchasers **not disclosed** (private placement); $39.96B securities pledged.
- Covenants: "customary"; **no financial-ratio covenant disclosed**; events of default include **change of management of the Fund**. 300% asset coverage (1940 Act).
- PNC is also swap counterparty (Daily Simple SOFR +0.905% to +3.214%) — *hedging, not financing; do not double-count as exposure.*

**CELFX facility** [PRIMARY: N-CSR 2026-06-08]: PNC admin agent + Barings JLA. Term $300M (fully drawn) + revolver $1,275M ($400M drawn) = **$1,575M committed / $700M outstanding**; accordion to $3.0B.

**Vintage reconciliation (fan-out vs primary):** the fan-out found a 2021-vintage SPV lender = MassMutual, admin agent Cortland; and a "$1.370B notes / revolver reportedly upsized to ~$4.23B Oct-2025" [INSTITUTIONAL/NEWS]. The FY26 N-CSR supersedes both: notes are now **$6.51B**, revolver committed **$4.84B**, admin agent **PNC**. MassMutual persists as JLA. **Coherent evolution — cite the N-CSR figures, not the relayed ones.**

### 1b. Held exposure at named banks — the ONLY thresholdable data · DEWEY primary pull
All as-of **2026-03-31** [PRIMARY: Q1-2026 10-Qs].

| Bank | Disclosure | Amount | % of loans | Trend |
|---|---|---|---|---|
| **WAL** | **Total loans to NDFIs** | **$14,928M** | **25.2% of HFI** | prior-period table not captured |
| — *of which* mortgage credit intermediaries | | $10,253M | 17.3% | (warehouse-type, **not** private credit) |
| — *of which* business credit intermediaries | | $3,415M | 5.8% | |
| — *of which* **PE funds** | | **$1,260M** | **2.1%** | |
| **CFG** | **Capital call facilities** | **$8,756M** | 6% | +2.1% QoQ |
| **CFG** | **Secured private credit finance** | **$4,096M** | 3% | +3.4% QoQ |
| **CFG** | Other finance & insurance | $5,268M | 4% | +13.7% QoQ |
| **JPM** | "Asset Managers" *(proxy — see caveat)* | $168,851M | 3rd-largest industry | **+10.5% QoQ** |

- **WAL's 25.2% is the striking number — and it must be read with its composition.** ~69% is mortgage-warehouse-type lending, **not** PE/private-credit. PE funds are just 2.1% of loans. *The headline concentration is real; the private-credit read of it is not.* (`[[finding_composition_mask_unmask_discriminator]]`)
- **CFG names capital-call facilities outright** — the cleanest subscription-line disclosure of the three. All finance lines outgrow the +1% total book.
- **JPM caveat: "Asset Managers" ≠ NDFI.** JPM-defined bucket, excludes "Banks & Finance Companies" ($79,113M, separate), not reconcilable to the Fed definition. Criticized $367M (0.2%), **zero nonperforming migration** — the growth is IG and clean.
- **Blind spot:** neither WAL nor CFG splits committed vs drawn. Given the FSR shows *utilized outpacing committed*, this is material at the single-name level.

### 1c. Servicer warehouse / MSR lines — new named exposures [PRIMARY: FY2025 10-Ks]

| Servicer | Lender | Facility | Size | Outstanding |
|---|---|---|---|---|
| **UWM** | **Citibank, N.A.** | Conventional MSR + warehouse | **$2.0B — UNCOMMITTED** | **$900.0M** @ 12/31/25 |
| **UWM** | **Goldman Sachs Bank USA** | Ginnie Mae MSR | **$500.0M — UNCOMMITTED** | n/d |
| **UWM** | UBS AG · JPMorgan · Jefferies · BofA | Master Repurchase Agmts | n/d | n/d |
| **Rocket** | **Citibank** (MSR) · **JPMorgan** (revolver admin agent) | | n/d | n/d |
| **Onity/PHH** | **NONE NAMED** | Warehouse | $1,224.6M (+17% YoY) | — |
| **Freedom** (private) | **NONE NAMED** ("broad group") | Warehouse + MSR | ~$5.5B MSR-secured | — |

**Both UWM facilities are UNCOMMITTED** — the lender may decline to fund. That is the *opposite* of the CCLFX committed-revolver risk profile and cuts against a simple "banks are on the hook" read.

---

## 2. The XPV syndicate — CONFIRMED verbatim, but the decision question is UNRESOLVED

**CONFIRMED (3-0, ×3 independent verifications), from the issuer's own release** [PRIMARY: Apollo press release, Jun 9 2026, [apollo.com](https://www.apollo.com/insights-news/pressreleases/2026/06/apollo-leads-35-billion-capital-solution-for-broadcom-ai-xpv-platform-in-partnership-with-blackstone-and-leading-global-banks-3308896)]:

> *"Wells Fargo is serving as Global Coordinator, Joint Bookrunner and Joint Lead Arranger and BNP Paribas, Citi and UBS are serving as Joint Bookrunners and Joint Lead Arrangers. Goldman Sachs, Bank of America and Morgan Stanley are serving as Joint Placement Agents on the A2 tranche."*

The ORC-relayed structure (BROCK NEXUS_BRIEF, *"[UNVERIFIED — ORC-relayed 6/15, pull primary]"*) is **confirmed exactly. That UNVERIFIED tag can be cleared.**

**Two precision corrections:**
1. **"Initial $35 billion capital solution"** — cite as *initial*, not total.
2. **Goldman/WFC/Citi also appear as ADVISORS to Apollo** — a separate role. **Do not conflate advisor with syndicate member.**

**❌ NEGATIVE FINDING — the question the bank leg turns on is not answerable from primary sources.** The release discloses **no tranche sizes** and **no hold-vs-distribute treatment for A1**. Placement-agent titles on A2 imply agency *by market convention only*; bookrunner/JLA titles on A1 imply but do not establish underwriting commitment. A press release is not a disclosure vehicle for retained exposure. **Resolvable only from Q2/Q3-2026 bank 10-Q NDFI/leveraged-lending disclosure — which does not exist yet.** Corollary: a placement-agent title does not preclude those banks taking principal exposure elsewhere in the structure.

*Trade-press coverage (INN, Globe and Mail, pulse2) is verbatim republication of the release and adds nothing — a republisher chain, not corroboration.*

---

## 3. Sizing — six numbers, six different universes. **Never stack or substitute them.**

| Figure | Scope | As-of | Source |
|---|---|---|---|
| **$95B committed / $56B drawn** | Largest US banks → PD funds + BDCs (**scope-limited FLOOR**) | 2024-Q4 | FEDS Notes 2025-05-23 [PRIMARY] |
| **~$600B (~25% of $2.6T)** | PE + BDCs + private credit, **commitments**, FR Y-14Q banks | 2025-Q4 | **May-2026 FSR** [PRIMARY] |
| **$2.6T** | **All** NBFI commitments, FR Y-14Q | 2025-Q4 | May-2026 FSR [PRIMARY] |
| **~$1,994B** | H.8 NDFI loans **outstanding**, all commercial banks | 2026-06 | FRED `LNFACBM027SBOG` [PRIMARY] |
| ~$300B / $455B / $220B | Boston Fed / OFR-JPM-Moody's / FSB member data | 2024-25 | [PRIMARY/INSTITUTIONAL] |
| ~$1.4T | Private credit market size (10% of US nonfin corp debt) | 2025-H2 | May-2026 FSR Box 4.1 |

**Growth — and why every growth number is contaminated:**
- FSR: PE/BDC/private-credit commitments **+17% YoY** vs **+14%** all-NBFI. **Utilized (~20%) > committed (~16%)** on the PE/BDC leg — *draw running ahead of commitment*, the aggregate echo of the CCLFX revolver finding.
- H.8 NDFI: **+24.6% YoY** headline — **contaminated**. A **+$210B (+17.5%) single-month step Dec-2024→Jan-2025** is a benchmark/reclassification artifact, not lending. Post-break: **+6.1% over 5 months (~15% annualized)**. *No Fed technical note located documenting the revision — the break is identified from the data itself.*
- FSR's own Box 3.1: the NBFI classification was **re-cut again**, reclassifying funds *into* the PE/BDC bucket — a **+$261B revision**. **The 17% and 25% are NOT like-for-like vs prior vintages.**

> **The true like-for-like growth rate of bank private-credit exposure is NOT KNOWABLE from public data.** Measured exposure is partly a *measurement* story. Do not cite 17% or 24.6% as clean. This is the honest answer to the prompt's "growth rates" ask.

**Concentration:** ~60% of the $95B at five US GSIBs; **JPM largest US lead arranger**, then Citi/WFC/BAC; BNP/SMBC/Barclays ~30% of BDC lead-arranging [PRIMARY: FEDS Notes].

> ⚠️ **ARRANGER ≠ HOLDER — the caveat that reshapes the deliverable.** The league table ranks **lead-arranger role, not held exposure** — precisely the distinction the decision turns on. **No Fed source discloses per-bank dollar exposure** (FR Y-14Q microdata is confidential). **Named-bank dollar thresholds cannot be built from Fed primaries.** The 60%/five-GSIB and ~30%/foreign-BDC-arranger stats are also *different populations* — don't cross-multiply.

**❌ SNC is a dead end for this question.** Keyword census across the 2025 report + attachment: **zero** hits for `nondepository`, `NDFI`, `nonbank`, `private credit`, `fund finance`, `subscription`, `NAV`. SNC segments by **lender** type, not borrower-as-NDFI. [PRIMARY: SNC 2025, released 2026-01-12]. *Headlines for context: $6.9T commitments (+6%), non-pass 8.6% (from 9.1%), US banks 45% of commitments / 22% of non-pass — and the Fed says the non-pass decline is "primarily due to growth in new commitments rather than an underlying improvement in credit quality."* **Retire SNC from this question's source list.**

---

## 4. Atlas SP — a well-sourced NEGATIVE, plus a premise correction

**Atlas SP's funding stack beyond BNP is genuinely NON-PUBLIC — structural, not a search failure.** Atlas SP Partners **is not an SEC financial registrant**. It files ABS-15G as a securitization sponsor (e.g. Atlas SP Commercial Mortgage, L.P., CIK 0002095291) but **no 10-K/10-Q of its own** — there is no "Notes Payable / Warehouse Facilities" note to read. Apollo's filings treat Atlas only as an **AUM/origination platform**, never as a borrower.

**The evidence for the non-disclosure is the asymmetry itself:** EDGAR full-text shows **"Atlas SP" 756× as lender/underwriter/sponsor, essentially never as borrower** (searches: "Atlas SP" 756, "Atlas Securitized Products" 429, "Atlas SP Partners" 48; Apollo CIK-scoped 17 hits, all AUM/earnings context).

| Provider | Type | Size | Date | Tag |
|---|---|---|---|---|
| **BNP Paribas** | Strategic financing + capital-markets collaboration; day-1 commitment, "expected to increase" | **$5.0B day-1** | 2024-09-20 | [PRIMARY: BNP/Apollo release] |
| **HSBC** | Back-leverage secured on Atlas's senior lending to Market Financial Solutions | **not disclosed** | 2026-04-30 | [NEWS: 9fin — **headline-only, body paywalled; UNVERIFIED as to size/terms**] |
| ADIA | **Cornerstone equity/capital** — *not a funding line* | n/d | 2023-06-07 | [PRIMARY: Apollo release] |
| MassMutual | Minority **equity** owner — *not a funding line* | n/d | ~2023-24 | [UNVERIFIED] |

**Do not let the equity/financing distinction collapse:** only BNP and HSBC are *financing* providers; only BNP is sized. **No repo counterparty list, no committed-vs-outstanding, no maturity ladder exists publicly.**

> **⚠️ PREMISE CORRECTION (in-repo "settled" fact).** The prompt marks *"Atlas SP dominant"* as out-of-bounds/answered (Apr-14). But **Atlas SP appears ZERO times in UWM, Rocket, FOA, and Onity 10-Ks.** Its servicer-warehouse footprint is concentrated in the already-mapped **PFSI/PMT and loanDepot** (Atlas omnibus/repo agreements on EDGAR from 2023-03) and does **not** extend to the largest originators. **Dominant in a segment, not across the sector.** Premise-qualifying, not premise-confirming — route to REGINALD/HOMER.

**Second-order finding: "public company ⇒ lenders disclosed" is FALSE.** Onity names **zero** bank counterparties across an 800,991-char 10-K (comprehensive word-boundary grep, not sampling — `[[finding_comprehensive_grep_over_sampling]]`). Onity, FOA and Freedom all disclose facility *types* and *sizes* but not *who*. **Counterparty-name disclosure is issuer-discretionary.** This bounds every future counterparty-mapping request.

*Apollo context datum [PRIMARY: 8-K 2026-04-01]: Q1-2026 alt income "reflects a lower contribution from origination platforms, including ATLAS SP Partners" — the only recent Atlas-specific performance tell in the filings.*

---

## 5. Transmission markers → PRED-24 Stage-3 (the honest answer)

### 5a. What the data supports
| Marker | Evidence | Usable? |
|---|---|---|
| **Intra-year PEAK revolver draw vs year-end** | **CCLFX: $3.15B peak vs $1.25B at FY-end (2.5×)** [PRIMARY: N-CSR] | ✅ **Best marker found.** Year-end snapshots systematically understate the channel. |
| **Utilized growth > committed growth** | FSR fig 3.16: PE/BDC utilized ~20% vs committed ~16% | ✅ Aggregate confirmation of the same mechanism |
| **Held balances at disclosing names** | **CFG capital-call $8,756M; WAL NDFI $14,928M** | ✅ **The only thresholdable named-bank data** |
| Subscription-line mechanics | ~200bps over benchmark; covenants MAY include min capital-coverage ratio; NAV financing 200-400bps | ⚠️ Medium conf (2-1); mechanism only |
| Escalating repurchase ratio | CCLFX Class I: 3.42% → 2.90% → 5.32% → **7.00%** | ✅ Primary-confirmed escalation |

### 5b. What does NOT support a threshold — state plainly
- **❌ No base rate survives, in either direction.** The one benign base-rate claim ("subscription facilities: minimal defaults over 30 years") was **REFUTED 0-3**. **No verifiable historical precedent for a fund liquidity event converting into bank balance-sheet LOSS (as opposed to a line draw) survived verification.** Any trigger rests on **mechanism alone, with zero calibration.** The Fed's own indirect-channel caveat — correlated NBFI drawdowns "could exceed historical experience" — means history may not calibrate it anyway.
- **❌ Named-bank dollar thresholds are not constructible from Fed data** (arranger ≠ holder, §3).
- **⚠️ Several attractive "markers" are DEWEY inferences, NOT sourced claims.** Tag them as analysis if used: *"undrawn capacity = the line-draw channel"*; *"capital-coverage-ratio breaches and subscription-line spreads = trigger markers"*; *"gating beyond ~3 quarters exhausts the cushion."*

### 5c. Proposed gate — mechanism-based, explicitly uncalibrated
**Conjunction (all three), at the only two thresholdable names:**
1. **CFG** capital-call facilities + secured private credit finance (currently $12,852M combined) rising **>10% QoQ** (vs +2.1%/+3.4% now) — *a draw surge, not commitment growth*; **and**
2. **WAL** NDFI **business-credit-intermediary** line (currently $3,415M, 5.8%) rising while total HFI is flat — *isolates private-credit from the mortgage-warehouse mass*; **and**
3. A **fund-side draw tell**: next CCLFX N-CSR/N-CSRS showing peak revolver draw >$4.0B (vs $3.15B FY26) **or** the accordion exercised toward $10B.

**Confidence: LOW-MEDIUM, and it is a *watch*, not a trip.** It is mechanism-derived with **no base rate**, and the Fed's 2bp-CET1 arithmetic says even a *full* drawdown is not a solvency event. **Recommend REGINALD treat this as a monitoring spec, not a pre-registered action gate.** Registering it in `GATES.tsv` would overstate its calibration.

---

## Counter-Evidence (mandatory — and here it is decisive)

1. **★ The Fed's stress arithmetic kills the direct-channel thesis.** Full drawdown of ALL undrawn commitments (+44pp utilization, $36B ≈ 2% of Y-14 CET1) → **~2bp CET1, ~1pp LCR**. "Financial stability concerns from the direct credit channel seem limited." [PRIMARY: FEDS Notes 2025-05-23]. **This is the strongest evidence in the report and it argues AGAINST the thesis the prompt was built to arm.**
2. **The Fed reads bank behavior as benign** — banks were **still increasing** commitments through Q4-2025; adjustments "consistent with historical patterns… normal risk-management practices" [May-2026 FSR].
3. **JPM's exposure is clean** — Asset Managers criticized $367M (0.2%), **zero** nonperforming, growth overwhelmingly IG.
4. **Redemptions "remain manageable"** per the Fed; Q1-2026 outflows only *moderately* exceeded inflows [May-2026 FSR].
5. **Bank credit + cash covers ≥3 quarters** of net redemptions at the 5% cap for the 10 largest perpetual BDCs (80% of sector) — **but see the vehicle-class trap below.**
6. **UWM's MSR facilities are UNCOMMITTED** — banks can decline to fund; not balance-sheet-locked.
7. **Cliffwater's revolver has no disclosed financial-ratio covenant** — reduces mechanical covenant-breach transmission.
8. **7 of 25 verified claims were KILLED**, including the tidiest mechanism story: *"interval funds are legally REQUIRED to accept ≥5% of redemptions, forcing CCLFX to fire-sell while BDCs can gate"* — **REFUTED 0-3**. Also killed: KBRA's $850B subscription-market sizing (1-2), the FSB <0.5%-of-bank-assets bound (1-2), and "up to 90% of bank lending to BDCs is credit lines" (0-3).

**What would disprove the benign read:** A1 XPV exposure confirmed as **held** rather than distributed (Q2/Q3 10-Qs); CFG/WAL draw surges per §5c; an *arms-length* CCLFX secondary print materially below carry (NEXUS's PRED-45 watch); or evidence of *correlated* drawdowns — the indirect channel the Fed's 2bp figure explicitly does **not** cover.

---

## Source Quality Assessment

**Strong.** The spine is primary: Apollo's own release (XPV roster), CCLFX/CELFX N-CSRs (facility + PNC), Q1-2026 10-Qs (WAL/CFG/JPM held balances), May-2026 FSR + FEDS Notes (sizing, stress arithmetic), FRED H.8, FY2025 servicer 10-Ks. The fan-out's value was **source discovery + adversarial verify** (it killed 7 of 25 claims, including a plausible mechanism story); the **load-bearing verdict came from the primary pull** — the fan-out could not name Cliffwater's banks; the N-CSR did.

**Gaps that bound the answer:**
1. **Hold-vs-distribute on XPV A1 — unresolved.** Not in any primary source; needs Q2/Q3-2026 10-Qs.
2. **No historical base rate survives** for fund-liquidity-event → bank-LOSS conversion.
3. **The Fed does not publicly size NAV loans or subscription lines separately** — zero hits for `subscription`/`NAV loan`/`fund finance` in the entire May-2026 FSR. That granularity exists only in confidential FR Y-14Q microdata. **Combined with Cliffwater not using such facilities at all, the prompt's framing of the channel is itself the finding.**
4. **Cliffwater syndicate lenders undisclosed** beyond PNC (credit-agreement exhibit not filed).
5. **CCLFX data is 3.5 months stale** (as-of 3/31/26). The 5/29/26 offer has closed; results file ~Dec-2026. **The primary record cannot reach Q2's 17% or the $1B secondary.**
6. **No committed-vs-drawn split** at WAL/CFG.
7. Atlas SP repo stack non-public (§4). 9fin HSBC article paywalled — highest-value single unlock.

**⚠️ Vintage/staleness — structural:** the FSR is **Q4-2025/Q1-2026 data**, the FEDS Notes are **2024 data**. **Every "banks are still lending / risks are manageable" finding is structurally incapable of speaking to Q2/Q3-2026 transmission.** The reassurance is real *and* it is looking backwards at a period that pre-dates the gating wave. Both halves of that sentence matter.

**⚠️ VEHICLE-CLASS TRAP:** **CCLFX is an INTERVAL fund; the FSR's redemption and ≥3-quarter-buffer statistics are PERPETUAL-BDC statistics.** Apollo Debt Solutions is *inside* that stat; **CCLFX is not.** Interval funds carry **higher leverage** per the Fed. Applying the comfort figure to Cliffwater is a category error.

**⚠️ Premise errors corrected:** (a) **there is no April-2026 FSR** — the 2026 vintage is **May 8, 2026** (cadence shifted from the 2024/25 April pattern); citing "FSR Apr-2026" would look like a phantom source. (b) The FSR body says **$2.6T**; the fig-3.15 accessibility table says "about 2700 billion" — body text taken as authoritative, discrepancy flagged, not silently reconciled.

**Confidence:** **High** — XPV roster (3-0 ×3, issuer primary); CCLFX facility/PNC (N-CSR); held balances (10-Qs); the 2bp stress figure. **Medium** — transmission mechanism; sizing comparability. **Low, flagged** — hold-vs-distribute; any threshold calibration.

---

## Freshness re-anchor (deliver-by 7/14 passed; run 7/16)

Per the manifest's freshness rule. **The decision moved and it moved TOWARD this prompt:** PROME's 7/16 audit re-rated 14 "the hottest" because CCLFX's gating + forced $1B sale made the scenario live rather than hypothetical. **Live context woven in.** Q2 bank prints land **today (7/16)**; WAL/OZK/ALLY **7/21**. **The 10-Q figures here are Q1 (3/31/26) — Q2 10-Qs will supersede §1b within ~3 weeks and are the natural re-test.** Nothing in the re-anchor changes the verdict; it raises the value of the CFG/WAL watch.

---

## References
1. Apollo, "Apollo Leads $35 Billion Capital Solution for Broadcom AI XPV Platform…", Jun 9 2026 — [apollo.com](https://www.apollo.com/insights-news/pressreleases/2026/06/apollo-leads-35-billion-capital-solution-for-broadcom-ai-xpv-platform-in-partnership-with-blackstone-and-leading-global-banks-3308896) · [ir.apollo.com](https://ir.apollo.com/news-events/press-releases/detail/629/) [PRIMARY]
2. Federal Reserve, **Financial Stability Report, May 8 2026** — [PDF](https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf) [PRIMARY]
3. FEDS Notes, "Bank Lending to Private Credit: Size, Characteristics, and Financial Stability Implications", May 23 2025 — [federalreserve.gov](https://www.federalreserve.gov/econres/notes/feds-notes/bank-lending-to-private-credit-size-characteristics-and-financial-stability-implications-20250523.html) [PRIMARY] ← *the 2bp stress figure*
4. FEDS Notes, "Shifting Dynamics in Bank Funding of NBFIs: The Rise of Credit Lines", Jul 14 2025 [PRIMARY]
5. CCLFX **N-CSR**, filed Jun 8 2026, FY-end Mar 31 2026, CIK 0001735964 — [sec.gov](https://www.sec.gov/Archives/edgar/data/1735964/000121390026066324/ea0291746-01_ncsr.htm) [PRIMARY]
6. CELFX **N-CSR**, filed Jun 8 2026, CIK 0001842754 — [sec.gov](https://www.sec.gov/Archives/edgar/data/1842754/000121390026066323/ea0290403-01_ncsr.htm) [PRIMARY]
7. CCLFX **N-23C3A**, filed May 8 2026 (5% offer, window 5/8–5/29/26, NAV $10.39) — [sec.gov](https://www.sec.gov/Archives/edgar/data/1735964/000121390026053701/ea0289460-01_n23c3a.htm) [PRIMARY]
8. Apollo Debt Solutions BDC **10-Q**, filed May 11 2026, CIK **0001837532** — [sec.gov](https://www.sec.gov/Archives/edgar/data/1837532/000119312526215667/ck0001837532-20260331.htm) [PRIMARY]
9. WAL **10-Q**, filed May 11 2026 — [sec.gov](https://www.sec.gov/Archives/edgar/data/1212545/000162828026033054/wal-20260331.htm) [PRIMARY]
10. CFG **10-Q**, filed May 4 2026 — [sec.gov](https://www.sec.gov/Archives/edgar/data/759944/000075994426000101/cfg-20260331.htm) [PRIMARY]
11. JPM **10-Q**, filed May 1 2026 — [sec.gov](https://www.sec.gov/Archives/edgar/data/19617/000162828026029344/jpm-20260331.htm) [PRIMARY]
12. **SNC Program Report 2025**, released Jan 12 2026 — [federalreserve.gov](https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260112a.htm) · [OCC](https://www.occ.gov/publications-and-resources/publications/shared-national-credit-report/files/shared-national-credit-report-2025.html) [PRIMARY] — *negative finding*
13. FSB, private-credit report, Jun 5 2026 — [fsb.org](https://www.fsb.org/uploads/P060526.pdf) [PRIMARY]
14. FRED `LNFACBM027SBOG` — Loans to Nondepository Financial Institutions, All Commercial Banks (monthly, SA); weekly `LNFACBW027SBOG` [PRIMARY]
15. BNP Paribas / Apollo, ATLAS SP $5B financing collaboration, Sep 20 2024 [PRIMARY]
16. Apollo **8-K**, Apr 1 2026 (Q1 alt income, ATLAS SP contribution) [PRIMARY]
17. UWM **10-K** (Feb 25 2026, CIK 1783398); Rocket **10-K** (Mar 2 2026, CIK 1805284); Onity **10-K** (Feb 17 2026, CIK 873860) [PRIMARY]
18. 9fin, "HSBC provides back-leverage to Atlas SP…", Apr 30 2026 [NEWS — **paywalled, headline-only**]

---

## Process Report

**Searches run:** 1 `/deep-research` workflow (**102 agents, 4.49M subagent tokens, ~9min**, 5 angles → 20 sources → 68 claims → 25 verified → **18 confirmed / 7 killed**, 0 errors) + **4 DEWEY primary pulls** (CCLFX/CELFX/ADS EDGAR; FSR+H.8+SNC+3 bank 10-Qs; Atlas SP targeted leg; [07b FRED leg run concurrently, separate report]).

**What worked:**
- **The carve-out earned its keep, decisively.** The fan-out explicitly concluded *"No source names the revolver's lender banks"* — the N-CSR primary pull named **PNC**. Same pattern as prompts 08/13. `[[finding_deep_research_primary_pull_owns_three_data_classes]]` holds: class (c) issuer-filing detail is unreachable by fan-out and is where the verdict lived.
- **The fan-out's real value was adversarial verify + coverage self-flagging** — it killed 7 claims (incl. the seductive "interval funds must accept 5%" mechanism) and **self-reported Atlas SP as returning zero verified claims** in `openQuestions`. That is adversarial *coverage*, which the harness historically lacks; noting it as an improvement.
- **EDGAR full-text inversion** on the Atlas leg: instead of "who funds Atlas?" (unanswerable), ask "who *discloses* Atlas?" — 756 lender hits vs ~0 borrower hits *is* the proof of non-disclosure.
- **Guardrailed sub-agents all returned complete.** Zero mid-run deaths (cf. the 7/10 un-guarded 5-bank pull that died). The return-partial-with-gaps instruction is now load-bearing standard.

**Data gaps:** hold-vs-distribute on XPV A1 (needs Q2/Q3 10-Qs); no surviving base rate for fund-event→bank-loss; Fed doesn't size NAV/subscription lines separately (confidential FR Y-14Q); Cliffwater syndicate beyond PNC (exhibit not filed); committed-vs-drawn at WAL/CFG; Atlas repo stack (non-public by structure); CCLFX 3.5mo stale — cannot reach Q2's 17%/$1B.

**Source frustrations:**
- **`fred_pull.py` silent-truncation BUG — found and FIXED this session.** `fetch()` applied `limit=10` even with `start=`; since `start` also flips sort to ascending, `--start 2015-01-01` returned **the ten OLDEST rows and nothing since** — silently, no error, plausible dates. **Fleet-wide exposure** (any agent's date-ranged FRED pull). Fixed + live-verified (401 rows vs 10); committed `fef252d9`. **Fabrication-adjacent — exactly the failure class the citation discipline exists to prevent.** ⚠️ *Any prior date-ranged FRED citation by any agent is suspect — flagged to PROME as a possible sweep.*
- **9fin paywall** — HSBC/Atlas back-leverage headline-only. Highest-value single unlock for the Atlas leg.
- **Bloomberg/Axios/PitchBook** rated "unreliable" by the harness (paywall → 0 claims). **The CCLFX 17%/$1B never reached a primary** — Bloomberg's Jun 2 2026 piece is behind the wall.
- **SNC exhibit PDFs are chart images** — pdfminer got titles/axes, not data points. Would need OCR.
- **Grep traps (both cost a retry):** `UBS` matches `subservicing` → word-boundary anchoring (`\bUBS AG\b`) mandatory; XBRL header blocks swamp output → filter `grep -viE "xbrl|fasb|http"`.
- **H.8 structural break undocumented** — identified from the data; no Fed technical note located.

**Confidence in findings:** **High** on the XPV roster (issuer primary, 3-0 ×3), the CCLFX facility/PNC (N-CSR), held balances (10-Qs), and the 2bp stress figure. **Medium** on transmission mechanism. **Low, explicitly** on hold-vs-distribute and any calibration. **The report's central verdict rests on the Fed's own arithmetic arguing against the prompt's thesis** — the most robust position available.

**If I had more time/tools:** fetch the CCLFX credit-agreement exhibit via the N-2/486 exhibit index (would name the syndicate — the single biggest remaining unlock); 9fin access; Q2-2026 10-Qs (supersede §1b + resolve XPV hold-vs-distribute) — **the natural re-run is ~3 weeks out**; OCR for SNC exhibits.

**Suggestions:**
1. **⚠️ Fleet-wide: prior date-ranged FRED pulls are suspect** pending the `fred_pull.py` fix (now committed). PROME's call whether a sweep is warranted.
2. **Retire SNC** from NDFI/fund-finance source lists — negative finding is definitive (§3).
3. **"Public company ⇒ lenders disclosed" is FALSE** (Onity/FOA/Freedom). Bounds every future counterparty-mapping request — worth fleet memory.
4. **BACKLOG build-pass candidate** — 3+ candidates now sit past the build gate (`ffiec_callreport.py`, `disaster_shocks.py`, `ofr_stfm.py`, all high-recurrence). Surfacing per CLAUDE.md closeout step 11; **builds stay Will-greenlit**.
5. **REGINALD's NEXUS-spec ask needs rewording** — it points at "NAV facilities / subscription lines," which **Cliffwater does not have**. The real channel is a **PNC-agented senior secured revolver + undisclosed-purchaser senior notes**, and the marker is **peak intra-year draw, not year-end balance**.
</content>
