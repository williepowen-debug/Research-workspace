# HOMER STATUS — HOT SURFACE

**Promoted from CARL sub-agent 2026-07-12** (Will-directed; DAEDALUS review `AGENTS/DAEDALUS/builds/homer_promotion/PROMOTION_REVIEW.md`).

> ⚠️⚠️ **HOT/COLD SPLIT 2026-09-02.** The pre-split `STATUS.md` was **148,572 B = 274% of the 54,250 B read cap**, so **every boot was reading a fragment** — and `READ_CAP.md` rule 12 says the fragment lost is whatever convention puts LAST, **which on a STATUS file is the Will-facing `## BOTTOM LINE`.**
> ✅ **The whole pre-split file is preserved BYTE-FOR-BYTE at `STATUS_COLD.md`** (148,572 B, crc32 `3627953216`, verified by RECOMPUTE not by banner — `READ_CAP.md` rule 11). **Nothing deleted.** This file carries **values + obligations**; the cold register carries **evidence, correction narrative and session history**. ⛔ **The cold register is FROZEN at the split and NOT maintained — this file is canonical; where they disagree, this file wins.** Full rationale: `docket/CATALYSTS.tsv` row 22.
> 🔁 **DATED RE-TRIGGER, and it is deliberately NOT a leanness claim** (`READ_CAP.md` rule 7 — *"the header did not become false by being wrong; it became false by being left"*): **re-measure every closeout via `python3 scripts/read_cap_check.py --agent HOMER`, and unconditionally by 2026-12-02.**
> ⚠️⚠️ **STATE THE NUMBER, NOT THE VERDICT: this file is **31–32 KB against a 32,550 B budget — ~98%, well under 1 KB of headroom** — and ~58% of the 54,250 B cap. UNDER the binding budget, and the checker prints it 🟡 rotate-tier, not ✅.** ★ **It went 28.6 → 31.8 KB within this same session when the August Trepp print and CORAL's FMHPI ruling landed — I rotated the split explainer to pay for them, which is the mechanism working, and it is also the proof that a live dashboard regrows on ARRIVING DATA, not just on narrative.** ⇒ ⛔ **NEXT SESSION MUST ROTATE BEFORE IT ADDS — there is no room left to defer it. Named first candidates: the superseded builder prints (KB Home FQ2, Lennar FQ2 — both in `workbook/BUILDER.tsv`) and the Q2 realization marks.**
> ⚠️ **The other regrowth mode: narrative. It goes to `memory/` and `reports/`. This file takes VALUES and OBLIGATIONS.**

**Last Updated:** **2026-09-02 (Wed — PROME-orchestrated full owner session: MF maturity-wall kill EXECUTED + published; read-cap remediation EXECUTED; inbox drained)** | **Status:** 🔴 CRITICAL

## ⚠️ DATA VINTAGE — READ BEFORE QUOTING ANY ROW

**Current at this session:** FMHPI **July** (PRIMARY, master file) · Census New Home Sales **July** (SECONDARY, via WALTER SIG-028-029) · MBA CREF loan-maturity survey **2026-02-09** (NEW today, publisher text via newslink mirror).
**Everything else is as at 2026-08-23.** The desk was dark 8/24–8/30 and 8/31 was a single-purpose scoped touch.

⚠️⚠️ **UNRESOLVED GAP — a week of prints may have landed while the desk was dark and NONE has been checked.** Status **UNKNOWN**, not absent:
| Release | Due | Status |
|---|---|---|
| **Fannie + Freddie JULY MF monthlies** | ~8/25-28 | ⚠️ **UNKNOWN — highest-value recurring pull the desk owns** (2nd datapoint on the registered mod-suppression test). Path convention: Fannie `/media/document/pdf/MMDDYY.pdf`-style, Freddie `MMYYmvs.pdf`, both with `curl -L` + UA |
| **ICE First Look — JULY** | ~8/24-26 | ⚠️ **UNKNOWN.** Second read on the two-instrument composition tell (90+ falling while FC inventory rises) and on FHA new-defaults −15% YoY, the live counter-signal to HOM-02 |
| **Case-Shiller — JUNE** | 8/25 | ⚠️ **UNKNOWN.** 13th consecutive negative REAL month? |
| **BEA Q2 GDP second estimate** | 8/27 | ⚠️ **UNKNOWN** (residential fixed investment) |
| **MBA weekly apps · PMMS** | weekly since 8/20 | ⚠️ **UNKNOWN** — up to 2 PMMS prints unread |
⛔ **Path-test before concluding absence** (June/prior controls return 200 at the same convention) — absence and a broken path look identical, and this desk has been wrong in both directions.

---

## SIGNAL DASHBOARD — LIVE VALUES ONLY
*Values + band state only. Evidence, corrections, provenance and every superseded figure → `STATUS_COLD.md`. Band definitions → `CLAUDE.md`. Series history → `workbook/`.*

> ⚠️⚠️ **BAND-REPORTING RULE, BINDING EVERYWHERE (rung census 8/23): report the highest UNCROSSED rung and the distance to it, never the highest crossed one.** *"Fannie MF is YELLOW"* is a label; *"0.60% — 5bps below Orange, Red untested"* is a signal. **4 rungs confidently pinned, 5 sample-limited and unclaimable.** ⛔ **Instruments that grade NOTHING are listed at OPEN OBLIGATIONS §C — check there before reading any silence as calm.**

### Foreclosure Pipeline
| Metric | Value (as of) | Band |
|---|---|---|
| Foreclosures H1-2026 (ATTOM) | **227,548 filings (+21% YoY)**; starts 164,566 (+18%); **REO 27,983 (+33%)**; **timeline 563 days, lowest since 2013** *(H1)* | 🔴 (national band DISARMED) |
| **★ ICE active FC inventory** | **292K / 0.53% of active loans — highest in six years** (+84K YoY, +39.3% YoY); **FC starts at a six-year high** *(June, PRIMARY)* | 🔴🔴 |
| **★★ FHA total DQ (SA)** | **11.79% Q2-2026** (−9bps QoQ), **+122bps YoY** | 🔴 **ORANGE (>10%), 21bps below RED (>12%)** |
| **★★ 90+/FC pipeline** | **570K 90+ + 292K FC = 862K** *(June, PRIMARY)* | 🔴🔴 **past ORANGE (>850K), below RED (>1M)** — all three rungs discriminate |
| **★ Non-bank servicer watch** | ⚠️ **🔴 by a one-time SEEDING decision — NO registered trigger has fired. Read the label before citing the colour** | 🔴 **SEEDED** |
| Servicer credit surface | **No rating action, covenant event, facility draw or liquidity event at any of the six watched servicers since 7/24** — a verified negative | 🟠 credit / 🔴 equity |
| Servicer weakest link | **Freedom Mortgage #1** — 15.5% of Ginnie 30-day-DQ pop., leverage 2.2× highest-of-peers, **MSR UNHEDGED** *(DEWEY 7/24)* | 🟠 |

### Multifamily — GSE + CMBS Books
| Metric | Value (as of) | Band |
|---|---|---|
| **★ Fannie MF serious DQ (monthly)** | **0.60% JUNE** (+2bps MoM) — **the first post-modification month, and it drifted UP** | 🔴 **5bps below Orange (>0.65%); Red (>0.80%) untested** |
| **★ Freddie MF DQ (monthly)** | **0.51% JUNE** (+4bps MoM, issuer verbatim) | 🔴 above Red (>0.50%) |
| Fannie MF serious DQ (qtrly) | **0.60% Q2** from 0.78% Q1 — **issuer-attributed to a portfolio MODIFICATION** | 🟠 headline / 🔴 mechanism |
| **Fannie MF credit provision** | **$259M Q2 vs $174M Q1 (+49% QoQ)** — *"weaker property valuations and slower NOI growth"* | 🔴 **expected loss RISING while measured DQ FALLS — this pairing is the signal, not the DQ level** |
| Freddie MF DQ (qtrly) | **0.51% Q2** — ⚠️ **NOT a new high: Q3-25 also 0.51% (MBA) and Sep-25 also 0.51% (issuer Table 6)** | 🔴 crosses Red |
| **★★ CMBS MF DQ (Trepp) — SIX-MONTH PATH, AUGUST ADDED 9/2** | **Mar 7.15 → Apr 7.71 → May 6.95 → Jun 7.23 → Jul 7.69 → AUG 7.69 (UNCHANGED, 0bp)** — *"Multifamily was unchanged at 7.69%"* (Trepp Aug report, pub 9/1; CREED pull 9/2, **SECONDARY at HOMER**). **The run of increases ENDS here**: MF was the largest mover in July (+46bp) and **the ONLY unchanged type of the five in August** (office +9 to **12.00**, retail +24, lodging +49, industrial +1) | 🔴🔴 ★ **four direction changes then a flat month — this series CURES; it is a level, not a trend.** ⚠️⚠️ **DO NOT RELAY "CMBS delinquency IMPROVED in August": the overall −1bp (7.86→7.85) is a NET of two large gross flows** — Trepp verbatim, *"several large loans became delinquent after failing to pay off at maturity, but their impact was offset by cures, including a large Times Square loan that returned to performing."* **The maturity-default flow did not stop** |
| **★ CMBS MF special servicing** | **8.39% July** (+16bps); Jun 8.23 · May 8.51 — **~70bps ABOVE MF DQ, and it ROSE in a month the overall SS rate FELL 11bps** | 🟠 |
| Trepp **maturity-adjusted** MF | ⛔ **STILL UNGRADED; June 9.53% has no counterpart.** ⚠️⚠️ **BUT THE WORD "UNPUBLISHED" IS WITHDRAWN 9/2 — IT WAS NEVER ESTABLISHED.** CREED (9/2): the maturity-adjusted series **lives in Trepp's full PDF, which is subscriber-gated and unarchived for August**, and it reported a **July headline-wide 9.62%** — so **Trepp IS publishing it; I cannot REACH it.** | ⛔⛔ **THE ~9/4 KILL MUST NOT FIRE ON "ABSENT" — THAT PREMISE IS FALSE.** An **ACCESS** failure and a **PUBLICATION** failure take opposite remedies: re-speccing the leg off a series the publisher still prints would retire a working instrument because MY pipe is broken (`finding_claim_outlives_its_discredited_instrument`). ⇒ **Re-frame the kill before executing it: the question is whether I can ever reach the series, not whether it exists.** Successor if the answer is no: **MF special servicing** (Aug SS report due ~9/8-10, not yet out) |
| ⛔ **2026 MF maturity wall** | ⛔⛔ **RETIRED 2026-09-02. `$160B+ 2026 (+50% YoY)` and `$270B+ 2026-27` ARE BOTH DEAD.** ⚠️ **Kill-on-sight: *"the $160B MF wall is Trepp's."*** ✅ **Replacement is PRIMARY and is a SHARE, NOT A DOLLAR: 13% of MF-backed balances mature in 2026** [MBA CREF, rel 2026-02-09]. Only MF-labelled dollar MBA prints: **$39B (4%), GSE/FHA/Ginnie, BLENDED with healthcare** | ⛔ **RETIRED, published** → `reports/2026-09-02_MF-maturity-wall-RETIREMENT-published.md` |
| **Realization marks (Q2, one-off — ledger: `workbook/MULTIFAMILY.tsv`)** | **Banc of California $827.0M to held-for-sale, 95.8% multifamily** · **Arbor Realty ~$1.07B NPAs with REO (~$545M) now EXCEEDING delinquencies (~$525M)** · **S2 Capital (DFW) $400M fund $0-to-LPs**; ~1/3 of ~$900M TX CRE flagged July auctions | 🔴🔴 **the GSE/CMBS books are ratios; these are realized marks** |
| Rent + concessions | **$1,962 asking (+2.3% YoY)**; SF $2,314 (+3.0%) vs **MF $1,786 (+1.7%)**; **concessions 39.8%** vs 35.9% a year ago *(July, Zillow)* | 🟠 |

### Mortgage Rates / Demand *(HOMER-owned surface, ★ ruling)*
| Metric | Value (as of) | Band |
|---|---|---|
| **★ 30-Yr PMMS** | **6.65% Aug 20** (−2bps WoW, 2nd consecutive decline); run 6.43 (Jul 2 low) → 6.69 (Aug 6 peak) → **6.65** | 🟠 Orange (>6.5%) crossed; **Red (>7.0%) untested**; Yellow PINNED |
| **★ 10Y-FRM spread** | **~196bps** (6.65 − 4.69, both 8/20) vs ~150bps norm ⇒ **~46bps structurally wide** | 🔴 ★ **the whole two-week PMMS decline is SPREAD, not rate — DGS10 flat at 4.69 on 8/6 and 8/20** |
| ⚠️ **BASIS TRAP — three live "30-Yr rate" instruments** | **PMMS contract 6.65% [8/20] · MBA contract conforming 6.77% [8/14] · MBA EFFECTIVE incl. points 6.96% [8/7]** — 12bps+ apart, **all correct** | ⚪ **name the instrument or the number is meaningless** |
| MBA weekly apps | **Composite −0.4% SA, but PURCHASE −2% while REFI +2%** on a 2bp move; refi share **41.9%** *(wk 8/14)* | 🟠 ⚠️ **the two YoY legs now move in OPPOSITE directions — restate "no refi escape" as a PURCHASE claim if it continues** |
| **★★ NAR pending home sales** | **71.2 (−2.3% MoM, −2.2% YoY); ALL FOUR REGIONS FELL, 2nd month** (West 52.7, −7.1% YoY) *(July, PRIMARY)* | 🔴 ⚠️ **the "at the COVID trough" claim is REFUTED — the trough is 69.0** |
| Existing home sales (SAAR) | **4.06M July** (−1.7% MoM, +0.7% YoY, decelerating from +2.8%) | 🟠 **closest approach of the cycle to <4.0M RED, clears by 60K**; Yellow+Orange PINNED |
| **★★ Starts / permits** | **STARTS 1,239K SAAR, −12.4% MoM, −13.5% YoY — but PERMITS ROSE 1,443K, +5.0% MoM** *(July CB26-127)* | 🔴 |
| New-home sales + overhang | **June 628K SAAR; months-supply 9.3.** July 607K (SECONDARY, WALTER) | 🟠 |

### Builder Distress
| Metric | Value (as of) | Band |
|---|---|---|
| **★ NAHB HMI** | **35 (+1)**; sales 39 (+2), expectations 43 (flat), **traffic 23 (flat)** — the +1 was ENTIRELY present conditions *(Aug, PRIMARY)* | 🔴 ⚠️ **my price-cutter "streak" BROKE here** |
| DHI FQ3-2026 | GM **20.7%** (−110bps YoY); **7,600 completed unsold homes, 600 aged >6mo**; avg rate buydown **1.6 ppts** (from 1.7) | 🟠 **moves AWAY from CRL-23's ≤17.5%** |
| PHM Q2-2026 | GM **25.0%** (vs 27.0% YoY) bought with **ASP −3%**; orders +6%, closings −8% | 🟠 **moves AWAY from CRL-23's ≤22.0%** |
| LGI Q2-2026 | HB GM **19.8% (−306bps YoY)**; ★ **like-for-like ASP −1.2% under a +0.5% HEADLINE** | 🟠 |
| Older builder prints *(FQ2, ledger: `workbook/BUILDER.tsv`)* | **KB Home: net income −75% YoY, op margin 8.6%→2.5%, revenue −27%** — sharpest margin crush of the cycle · **Lennar GM 15.6% (−220bps YoY), FY26 deliveries CUT ~85K→82-83K** | 🔴🔴 / 🔴 |
| **★★ Residential construction employment** | **+2,100 — first monthly increase in four months**; total 3.3M; **trailing 12-mo −44,200 = 17th consecutive month of annual decline** *(July, BLS)* | 🔴 |
| Q2 GDP residential fixed investment | **+1.5% SAAR, first positive in FIVE quarters**; housing share of GDP **15.8%, lowest since 2019** | 🟡 |

### Pricing / Inventory
| Metric | Value (as of) | Band |
|---|---|---|
| **★ Freddie FMHPI national** | **+2.31% YoY SA July** (+2.24% NSA), MoM SA +0.40% — **the FASTEST print of the post-trough run**; June revised in-vintage to **+1.81% SA** *(PRIMARY)* | 🟠 nominal / 🔴 real |
| Case-Shiller national | **+1.1% YoY May** (accelerating); 10-City +2.4%, 20-City +1.6%; **MoM SA −0.05%** | 🟠 nominal / 🔴 **12th consecutive negative REAL month** |
| **★★ Realtor.com list price** | May −2.4% → Jun −2.5% → **Jul −2.4%** (9th negative); ★ **mix-controlled $/sqft improved monotonically −2.5 → −2.1 → −2.0 — the mix FLIPPED SIGN** | ⛔ **STRIPPED OF STANDING as a 60-90d HPI lead (HOM-01 IF-MISSED, executed). CONTEXT ONLY** |
| ⚠️ **Redfin sellers/buyers gap** | **51.3% more sellers than buyers in July** (from 47.9%) — just shy of December's record 51.8%; **buyers 966,752, a RECORD LOW** | 🔴 |
| ⚠️ Parcl Labs *(cross-check, NOT canonical)* | **US home prices −1.7% YoY — disagrees in SIGN with Case-Shiller's +1.1%** *(7/31)* | ⚪ flag |

### State-Level Housing (FL/TX priority)
> ★★ **HOMER PUBLISHES NO STATEWIDE FLORIDA FIGURE. CORAL RULES.** HOMER-owned inside FL: **metro-level FC rates + the Miami-Dade condo cut** — sub-statewide only.

| State | Metric | Value | Band |
|---|---|---|---|
| FL | H1 FC rate *(CORAL-canonical, HOMER cites)* | **#1 NATIONALLY: 0.27% (1-in-373), 27,494 filings, +32.7% YoY** | 🔴 speed / 🟠 level |
| FL | **Metro FC rates (HOMER-owned)** | **Punta Gorda 0.50% (#1 US metro), Lakeland 0.48% (#2 US)** | 🔴 |
| FL | Monthly FC rate | **1 in 2,106 HU, #1 nationally, flat MoM** *(June)* | ⛔ **a monthly ratio is an OBSERVATION, NEVER a band reading** |
| FL | **Miami-Dade condo (HOMER-owned)** | **12.0 months supply, 86 median DOM, declining median price** *(July)* | 🔴🔴 |
| FL | Statewide condo | ⚠️ **CORAL-owned open tension** — FL Realtors June cuts AGAINST the collapse frame | ⚠️ packet sent |
| FL | FMHPI statewide | **+1.68% SA YoY July** — **routed to CORAL, NOT published as mine.** ✅ **CORAL RULED IT 9/2 AND THE "THREE-WAY DISAGREEMENT" DISSOLVES** | ⛔⛔ **THE TENSION WAS NEVER REAL, AND THE REASON BINDS ON MY OWN INSTRUMENT: FMHPI EXCLUDES CONDOMINIUMS, CO-OPS AND PUDs BY CONSTRUCTION** (Freddie verbatim; SF-detached + townhome, conforming conventional first-lien only). **It cannot bear on ANY condo question, in either direction.** ⚠️ **VINTAGE CORRECTED: my "CORAL median +4.9%" was CORAL's JUNE figure; their JULY SF median is +3.7%** — like-for-like the gap is **2.0pp, not 3.2pp**, and **both statewide SF instruments AGREE IN SIGN** (the gap is the mix premium — my own composition lesson pointing at consistency). **ZHVI was a COUNTY SUBSET on a different month and was never a statewide sign** |
| **TX** | August CRE FC auction pipeline | **>$1.15B across 47 loans**; Tarrant County 11 = modal | 🔴🔴 |
| FL | Band state | **ANNUAL Yellow >0.72% / Orange >1.50% / Red >3.00%; ratio >2.0/2.5/2.9×** | ✅ calibrated — ⚠️ **evaluable ONCE A YEAR at the ATTOM year-end; "no band reading" is NORMAL** |

### ⚠️ STANDING CAVEATS THAT QUALIFY THE ROWS ABOVE — obligations, not commentary
1. **FHA PROCESS BREAK — the one NOT carried on an always-loaded surface, so it is stated in full here.** Any FHA DQ **YoY** spanning **Oct-2025** is **~79% slower-cure-drain, not credit** (WALTER SIG-028-009 / DEWEY DR-1; `workbook/PIPELINE.tsv`). It qualifies HOM-02's "+122bps YoY" and is **opposite-signed** to the HUD ML 2026-08 FC-migration mechanic. **Say which one you mean.**
2. **GSE MF band defect** (open — A1) · 3. **Builder price ≠ what the buyer pays** (the buydown/concession-cap exclusion; NAHB's cut figure is a LOWER BOUND; DHI's cost disclosure is DEGRADING) · 4. **FL rank ≠ FL level** (FL is #1 because everyone else fell further; level normalizing up, SPEED is the story). ⇒ **All three are stated IN FULL on `CLAUDE.md`, which is always loaded — not restated here.** *(Deliberate: a caveat duplicated on two surfaces drifts on one of them.)*

## OPEN OBLIGATIONS
*Every row is something this desk still owes or must not forget. Closed items live in `STATUS_COLD.md` and `archive/`.*

### A. Owed work — mine to do
| # | Item | State |
|---|---|---|
| **A1** | ⛔ **GSE MF band re-spec — STILL OWED.** Bands key on a headline one modification moved 18bps. `CLAUDE.md` currently *warns* (pair with provision direction) rather than re-bands | **OPEN.** REGINALD holds the rider; the "wait until after 8/31" it recommended **has now expired** |
| **A2** | **Non-funding-leverage RIDER** — ratify the NO-VERDICT PRECURSOR (Will-approved 8/23, read as option A) | ⚠️ **STATUS ROW CORRECTED 2026-09-02: the pre-split file said "NOT DRAFTED." That is FALSE and had been since 8/23** — the draft is `reports/2026-08-23_non-funding-leverage-RIDER-DRAFT-for-ratification.md` (9,618 B). **What is owed is RATIFICATION, not drafting.** ★★ **And `docket/CATALYSTS.tsv` said so correctly the whole time — its row reads *"RIDER DRAFTED, AWAITING RATIFICATION"*. ⇒ **Two of my own surfaces disagreed for ten days and the BOOT-READ one carried the false state**, which is the worst possible allocation (`finding_ask_which_surface_the_reader_travels_not_where_the_fact_belongs`) |
| **A3** | **Rent Growth (% cities negative) RETUNE** — ⛔ **WORK AUTHORIZED, LEVELS WILL-GATED.** Successor: % of Zillow metros negative YoY. **20/40/55 CANNOT carry over** — different denominator, different distribution | **OPEN.** Row grades nothing until ruled |
| **A4** | **National Foreclosures (Qtr) RETUNE** — ⛔ **WORK AUTHORIZED, LEVELS WILL-GATED.** Basis **ruled = STARTS** (my choice, informed by CARL's CRL-06 ruling, **not inherited from it**). Needs a sourced ATTOM quarterly-starts distribution spanning crisis→workout→normal | **OPEN.** Row grades nothing |
| **A5** | **L3 BUILDS 3b + 3c** — `thesis/THESIS.md` + a thesis-level KILL RAIL, and the convergence handle. ★ **Do NOT build 3b by generalizing HOM-01/HOM-02** — per-prediction machinery is not a thesis-level rail | **OPEN, unambiguously authorized to BUILD (Will 8/23).** With HOM-01 closed, the resolver-first deferral argument has partly expired: only HOM-02 remains open |
| **A6** | **Cure Rates band has NO CURRENT FEED** — needs ICE *Mortgage Monitor*, not *First Look* | **OPEN**, dated re-spec condition set |
| **A7** | **5 sample-limited threshold rungs** unresolved (Fannie MF Yellow · Freddie MF Yellow+Orange · Builder Price Cuts Yellow · FHA DQ Orange) | **Research task, not a ruling.** Needs a longer series |
| **A8** | **FL Orange >1.50% is the ONE bracketed level** — 2014-2016 FL annual rates are unmapped | **Re-anchor if a 2014-2016 FL annual rate surfaces** |
| **A9** | **ZHVI leg UNCONFIRMED AT PRIMARY** (six FL top-50 counties negative, screenshot-sourced via WALTER). Smoothing/revision, contract-vs-close timing and coverage not excluded | **Corroborated, not closed** |
| **A10** | **Freddie MF quarterly Q1-2026 value not held** — MBA is a different compiler than the 10-Q, so the Q3-25 tie is corroboration, not identity | Minor residual |
| **A11** | **SIG-043 residue: MBA NDS primary still 403-gated.** Carrier B-vs-C FHA SDQ untangle owed **if anyone contests**; my 11.79% stands (HousingWire direct-fetch-verified 8/13) | ⚠️ **Re-confirmed 9/2 — `mba.org` 403s this box on the CREF release too, on a browser UA. It is a site-wide gate, not a per-page one** |

### B. Owed by others / flagged, not mine to edit
| # | Item |
|---|---|
| **B1** | **CREED courier re-spec proposed 8/22** — courier the ROW not the print (MF DQ + MoM as a one-line paste, back-filled if missed), plus mat-adj MF and MF special servicing. ⛔ **A dated NO is more useful than a standing yes that doesn't fire** — awaiting either |
| **B2** | **CARL owes freeze/refresh/retire on "help with mortgage"** (charter-named HOMER source, CARL-owned interpretation, NO pull owner). Chase at CARL's next boot |
| **B3** | **REGINALD `NEXUS_BRIEF:23`** carried three superseded HOMER figures at last check — their file, their edit; packet sent 8/23 |
| **B4** | **`## VIEW` in `NEXUS_BRIEF.md` ~57 items, no cap** — schema-owned, flagged to NEXUS and Will. ⚠️ **The §4.5 line-ceiling is on the wrong axis and can NO LONGER be repaired by amendment** (schema capped at 12; a 13th needs a re-spec sitting). **The ceiling is UNENFORCED — do not cut brief content against it** |
| **B5** | **PROME `HEARTBEAT_COLD.md:77`** still reads *"$160B+ MF maturity wall RETIRES 9/4"* — **it retired 9/2 and is published.** PROME-owned; flagged, never edited by me |
| **B6** | **`PROME/DOCKET.tsv` L224's carrier list is WRONG** — it names CORAL, LIQUID and DAEDALUS; **none of them carries this figure** (CORAL's $160B is a rate-cap expiration volume; LIQUID's is ORCL debt; DAEDALUS merely cites the docket row). Correction packeted to PROME + CREED 9/2 |

### C. Instruments that GRADE NOTHING — do not read their silence as calm
- ⛔ **National Foreclosures (Qtr)** — DISARMED 8/22. Filings pinned ~1.65× above Red; starts also pinned; REO can never reach Yellow. **Do not read its silence as "the pipeline is contained."**
- ⛔ **FL Foreclosures YoY** — RETIRED 7/31. **Do not read its silence as "FL is fine."**
- ⛔ **Rent growth (% cities negative)** — no feed, last reading above Red. **Neither Red nor fine.**
- ⛔ **Cure rates** — no feed.
- ⛔ **Trepp maturity-adjusted MF** — unpublished three months.
- ⚠️ **FL ANNUAL + FL RATIO bands** — evaluable **once a year** at the ATTOM year-end. Silence is normal.
- ⚠️ **Ginnie Mae APM 26-06** and **NY Fed HHDC VantageScore 4.0** — **MEASUREMENT BREAKS, not catalysts.** Any DQ-ratio or score-based series spanning them is not like-for-like.

---

## CATALYSTS — FORWARD ONLY
*Graded/passed rows → `STATUS_COLD.md`. Full calendar → `docket/CATALYSTS.tsv`.*

| Date | Event | Watch |
|---|---|---|
| **🔴 ~9/4** | **Trepp August print** | ⛔ **DATED KILL FIRES: maturity-adjusted MF rate — RE-SPEC THE LEG OFF IT if absent a THIRD consecutive month.** Successor already named: **MF special servicing.** ✅ *(The second ~9/4 kill — the $160B wall — was EXECUTED EARLY on 9/2 and is closed.)* |
| **9/17** | Census New Residential Construction (August) | Starts/permits divergence: July was starts −12.4% with permits **+5.0%** |
| **🔴 9/21** | **HUD Mortgagee Letter 2026-08 MANDATORY COMPLIANCE** | **The clearest dated FHA foreclosure-pipeline ACCELERANT held.** ⚠️ Opposite-signed to the Oct-2025 process break — say which mechanic you mean |
| **~9/25** | Census New Home Sales (August) | ★ **median vs AVERAGE price gap = the mix tell** (June: avg −9.5% MoM vs median −3.3%) |
| **~9/29** | Case-Shiller (July data) | Nominal accel vs the MoM SA leading edge; consecutive negative REAL months |
| **~9/30** | **FMHPI August data** | **Routine PRICING pull — NO LONGER A RESOLVER** (HOM-01 closed). Nominal accel vs CPI is the live wealth-effect question (→ HENRY) |
| **~last week of Sept** | **Fannie + Freddie AUGUST MF monthlies** | ⚠️ **Cadence is the LAST WEEK OF THE FOLLOWING MONTH** — the old "~mid-month" key was wrong by ~2 weeks and cost a refresh. **First check whether JULY posted** (see vintage gap above) |
| **~mid-Oct** | **ATTOM Q3-2026 report** | ⚠️ **The monthly press release is NOT a reliable instrument** (skipped in 3 of the last 6 months) — quarterly/mid-year/year-end are what I docket. **Year-end is the ONLY resolver for the FL annual bands** |
| **~10/15** | **GSE condo: limited/streamlined project reviews ELIMINATED** | **WAITING-ON-INSTRUMENT.** ⚠️ **NOT before Oct-Nov** — August-application loans must close first. National pre-mandate all-cash baseline banked at **26% (NAR July)** |
| **~Oct / ~Nov** | **PHM Q3 / DHI FQ4** | **CRL-23 trajectory checkpoints** (formal resolvers are Q1-FY27, Jan/Apr 2027). DHI aged-spec tail (600 >6mo): does volume discipline hold? |
| **🔴 ~mid-Nov** | **MBA Q3-2026 NDS** | ⛔ **HOM-02's MODAL DECIDER.** Early-kill arm 1 of 2 already fired (Q2 declined QoQ) — **a second QoQ decline closes HOM-02 MISSED EARLY** |
| **~January** | **ATTOM year-end** | **The ONLY resolver for the FL ANNUAL and FL/national RATIO bands** |
| Weekly | **PMMS (Thu 12:00 ET)** · **MBA apps (Wed)** | PMMS: third consecutive decline or a base? **Watch whether the 10Y stays pinned** — if it does, the move is still all spread |
| Monthly | ICE First Look (~24th-26th) · Realtor.com (~1st-3rd) · Census NHS (~25th) · Redfin (~2nd Tue-Wed) · Case-Shiller (last Tue) | The six recurring rows added 8/23 after four series aged at once |
| Standing | **Nonbank Ginnie servicer credit watch** (DEWEY 7/24 waterfall follow-on) | Quarterly + event-driven |

---

## PREDICTIONS
*Ledger of record: `thesis/PREDICTIONS.tsv`. Full grading narrative → `STATUS_COLD.md`.*

| ID | Call | State |
|---|---|---|
| **HOM-01** | FMHPI national nominal YoY **rolls over** (60%, PROVISIONAL) | ⛔ **CLOSED — MISSED (EARLY-KILL), graded 2026-08-31, the day the print posted.** July **+2.31% SA** > frozen +1.9% ⇒ arm 2 fired; Leg-1 also failed independently ⇒ **0-for-2. The desk's first closed prediction.** ⛔ **DO NOT RE-OPEN.** IF-MISSED clause executed: **the Realtor.com headline list-price series LOSES STANDING as a 60-90d HPI lead.** ⛔ No confidence re-rate — **Will-gated**; 60% PROVISIONAL stands as the calibration record |
| **HOM-02** | MBA NDS **FHA SA total DQ ≥12.00%** in the Q2/Q3/Q4-2026 release (65%, PROVISIONAL) | 🔴 **OPEN. Early-kill arm 1 of 2 FIRED** (Q2 declined QoQ). Q2 confirm leg **NOT met — 11.79%, 21bps short.** **Q3 (~mid-Nov) is the modal decider; a second QoQ decline closes it MISSED EARLY.** ⚠️ Behind on the front end (ICE June FHA new defaults −15% YoY), and the front-end read is **further qualified by the Oct-2025 process break** |
| **CRL-06** | Foreclosures >70K/qtr | ✅ **RESOLVED CONFIRMED at CARL 2026-07-16** on HOMER's data package; metric **ruled = STARTS** (Q1 82,631). HOMER remains data owner |
| **CRL-23** | FY27 builder GM compression (DHI ≤17.5% OR PHM ≤22.0% AND tariff ≥10% sustained) | 🟡 **OPEN at CARL** (parent-retained); **HOMER is data owner.** Data-owner read: **the DHI FQ3 + PHM Q2 pair moves AWAY from both triggers** (20.7% and 25.0%, both margin-up sequentially). Resolvers Jan/Apr 2027 |

⚠️ **`Date_Resolved` and `Outcome` stay EMPTY for any prediction whose arms have fired but which is not resolved — one arm of a two-arm kill is not a resolution.** Graded state lives in `Status`, which is what a due-scan reads.

⚠️⚠️ **CalculatedRisk may be GONE** — its front page's newest posts are **January 2026**. **UNKNOWN, not chased.** ⛔ **It is the named mirror in HOM-01's spec class: any future prediction citing CR needs a NEW named mirror, verified before registration.**

---

## BOTTOM LINE

**2026-09-02 (Wed) — a full owner session with two structural jobs and no new data: a figure died, and the desk's own boot reads came back under the cap.**

**① THE $160B+ MF MATURITY WALL IS RETIRED AND PUBLISHED, two days ahead of its own kill date.** CREED's 8/28 verdict (NOT ATTACHABLE — a **CF Capital sponsor quote** that acquired a Trepp label by **co-location**) held when I ran the owner-declared path myself: **MBA's CREF loan-maturity survey publishes property type as a PERCENT and lender type in DOLLARS, and there is no multifamily property-type dollar anywhere.** ★★ **The part that is not housekeeping: the dead sentence also carried a DIRECTION — "+50% YoY" — and MBA's own 2026 total is $875B, DOWN 9% from $957B in 2025. On MBA's schedule multifamily is the LEAST maturity-pressured major property type (13% vs office 17%, hotel 30%) and the aggregate wall is SHRINKING.** ⇒ **For four months this desk carried a multifamily-maturity story that pointed the wrong way, and my surface is the one REGINALD and CREED nest CRE totals against. This is a retraction of pressure, not a cleanup.** ⛔ **And the docketed dispatch list was wrong: CORAL, LIQUID and DAEDALUS do not carry the figure at all** (a rate-cap volume, ORCL debt, and a citation of the docket row) — **three desks would have received a correct-looking correction about a number they do not hold.** A string match is not a carry.

**② READ-CAP REMEDIATION EXECUTED — both boot reads were over the physical cap and every boot had been reading a fragment.** `STATUS.md` **148,572 B → ~31.8 KB (−79%)** and `LESSONS.md` **97,396 B → 21,676 B (−78%)**, by hot/cold split with the full pre-split text preserved **byte-for-byte** and **crc-verified by recompute** at `STATUS_COLD.md` / `LESSONS_COLD.md`. ★ **The audit that mattered was by OBLIGATION, not by bytes** — and it found one: the pre-split OPEN ITEM 18 read **"NOT DRAFTED"** for the non-funding-leverage rider **ten days after the draft existed and Will had approved it.** A byte-clean split would have carried that falsehood forward intact. **Both files carry a DATED re-trigger rather than a leanness claim, because the failure mode of a size fix is that it runs once and disarms the next check.** ⚠️ **Reported precisely rather than as a win: STATUS lands at ~98% of budget with well under 1 KB of headroom and the checker prints it 🟡 rotate-tier, not ✅ — the next append rotates before it adds.**

**③ WHAT DID NOT CHANGE, and it is most of the desk.** No band moved, no level moved, no prediction moved, no capital path touched. **HOM-02 remains the only open HOMER-native prediction** and is behind on its front end. **The marquee question stands unchanged: recognition regimes differ — the CMBS MF leg oscillates and CURES (four direction changes in four months), the GSE books do not.** The domain's cleanest sentence is still **"inflow cooling, conversion accelerating"** — three instruments — and it cuts **against** HOM-02. Say both.

⚠️ **THE HONEST GAP: a week of prints landed while the desk was dark and NOT ONE has been checked** — both GSE July MF monthlies (the highest-value recurring pull this desk owns), ICE July First Look, Case-Shiller June, BEA's second estimate, two PMMS prints. **The vintage table above says UNKNOWN, not absent.** That is the first work of the next session, ahead of any of the four approved queue items.
