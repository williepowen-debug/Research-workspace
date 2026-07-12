# HOMER STATUS

**Promoted from CARL sub-agent 2026-07-12** (Will-directed; DAEDALUS review `AGENTS/DAEDALUS/builds/homer_promotion/PROMOTION_REVIEW.md`). Parent-era record (pre-promotion dashboard, Spawn 1-6 history) lives in `archive/` + `state_vectors/` — not restated here.

**Last Updated:** 2026-07-12 (first-boot live-data session, post-promotion-rebuild) | **Status:** 🔴 CRITICAL | **Data vintage:** rebuilt from CARL's current STATUS housing rows at promotion (freshest available source at cutover), THEN refreshed this session with live web pulls (ICE First Look May 2026, Freddie PMMS Jul 9, NAR June EHS, builder-earnings calendar verification). Most core rows are now July-current on the check date; a few (Fannie/Trepp MF, Case-Shiller, Freddie HPI) remain at their natural release-cadence vintage (May/June) — that is normal lag, not staleness, and is flagged per-row.

**Inheritance verification (this session, 2026-07-12):** spot-verified 4 load-bearing inherited figures against primaries — **0 drifts found** in the values themselves (Fannie May 0.58% MF serious DQ confirmed exact via CalculatedRisk/PR Newswire/StockTitan; Trepp June 7.23% MF DQ [+28bps, 48bps below Apr's 7.71% ATH] confirmed exact via Multi-Housing News/Yield PRO/ConnectCRE; ATTOM Q1 82,631 FC starts confirmed internally consistent across HOMER/CARL files — it's the FC-starts figure, not a separate metric). **3 staleness gaps found and fixed** (not copy-drift, but rows that aged out since the 6/26–7/4 cutover pulls): 30Y PMMS was 3 weeks stale (Jun 18 6.47% → now Jul 9 6.49%, w/ Jul 2 6.43% 7-wk-low waypoint); ICE foreclosure-pipeline trio (FC inventory/starts/DQ rate) was April-vintage → refreshed to May (ICE First Look, rel Jun 26); NAR Existing Home Sales June print was mis-scheduled in the inherited docket as a ~7/23 upcoming catalyst — it **already released 7/9** (4.09M SAAR, -2.4% MoM, +2.8% YoY) and is now booked as data, not a forward catalyst (see docket fix below). **MF-books as-of-date check:** Fannie (May, rel Jun 26) and Trepp (June, rel ~Jul 4) are NOT the same calendar month — confirmed intentional, not drift: Trepp's monthly print structurally releases ~3-4 weeks faster than Fannie's, so a 1-month stagger between the two books is the steady-state, not a desync to fix.

---

## MARQUEE OPEN QUESTION — GSE-vs-CMBS Multifamily Divergence

The single best open housing question, now consolidated under one owner (HOMER, ★ ruling `PROMOTION_REVIEW.md`):

| Book | Metric | Trajectory | Read |
|------|--------|-----------|------|
| **GSE (Fannie)** | Serious DQ | Feb 0.74% → Mar 0.78% (2bps from 0.80% GFC peak) → Apr 0.64% → **May 0.58%** (2nd consec <0.65%) | **IMPROVING — CRL-03 invalidated on its own pre-registered trigger** (CARL v2.6.1, 2026-07-02); gap to GFC peak widened to 22bps and moving away |
| **CMBS (Trepp)** | MF DQ | Mar 7.15% → Apr 7.71% (ATH) → May 6.95% (large-loan cure) → **June 7.23%** (+28bps, resumed rising) | **DETERIORATING** — maturity-adjusted (incl. past-maturity loans still paying) = **9.53%, new multi-year high** (CREED 7/4 pull) |

**Divergence WIDENING, not narrowing.** Different books, different mod regimes: GSE extend-and-pretend mechanism cooled the headline; CMBS book has less workout runway and is realizing losses (Sun Belt 2022-vintage cluster: S2 Capital $400M DFW fund $0-to-LPs, ~$900M TX CRE flagged for July auctions, Trepp $2.54B hard CMBS maturities due July at 36% sub-8% debt yield). This is now a **one-owner (HOMER) / two-consumer (CREED, REGINALD) figure** — REGINALD independently sourced the same Trepp print pre-promotion (its own STATUS carries a 7.71%/7.23% row); that 3-way citation habit is what the promotion is meant to collapse to one primary + cited consumers. *Source: Fannie Mae Monthly Summary Table 7 (rel Jun 26 2026); Trepp via CREED 2026-07-04 pull.*

---

## SIGNAL DASHBOARD

### Foreclosure Pipeline
| Metric | Value | As Of | Source | Status |
|--------|-------|-------|--------|--------|
| Foreclosures Q1 2026 (ATTOM) | **118,727 filings** (+6% QoQ, +26% YoY). **Q1 REO 14,020 (+45% YoY) — pipeline CONVERTING, not just accumulating.** | Apr 16, ATTOM | ATTOM | 🔴 |
| ICE Active FC Inventory | **280K (+34% YoY, highest in 6 years);** above Mar-2020 pre-pandemic 271K for 3rd consec month. FC starts 33K May (-9% MoM, +19% YoY); cures -6% MoM, FHA lagging. | May 2026, ICE First Look (rel Jun 26) | ICE | 🔴🔴 |
| MBA Q1 NDS All Loans DQ | **4.44%** (+18bps QoQ, +40bps YoY); FHA FC inventory highest since Q4 2018, VA highest since Q2 2017. NY Fed HHDC echo (7/12): mortgage serious-DQ transition 1.4→1.5%, +59K new-FC notations — consumer-transmission read, stays at CARL. | Q1 2026 (rel May 14) + NY Fed HHDC | MBA | 🔴 |
| FHA DQ / Mortgage DQ inflection | **11.52% (Q4-25) vs Conv 2.89%**; ICE national DQ rate 3.50% May (+15bps MoM — flagged calendar-driven/Sunday month-end, not broad deterioration); FHA non-current >13% (FL/2022+ Sun Belt thin-equity vintage concentrated). | Q4-25 MBA + May-26 ICE | MBA/ICE | 🔴 |
| 90+/FC Pipeline | **577K 90+ DQ (not in FC), 5-mo SA low but +111K YoY (largest annual increase since 2020) + 280K FC inventory ≈ 857K combined** — refreshes the stale MBA 878K Feb cut with ICE's May read (different source/methodology, same concept; composition shifted toward more FC-inventory, fewer new serious-DQ entries). | May 2026, ICE First Look (rel Jun 26) | ICE | 🔴🔴 |
| Nat'l State Leaders Q1 | TX 10,617 FC starts #1; FL 10,099 #2. Top rates: IN 1/739 HU, SC 1/743, FL 1/750. | Q1 2026, ATTOM | ATTOM | 🔴 |
| Non-Bank Servicer Stress | **PennyMac FHA DQ 7.5%** (+160bps QoQ); loanDepot $107.5M loss; Rithm Q1 "DQ will reverse" claim QUIETLY DROPPED → mod-accounting normalization framing. | Apr 28 + Apr 13 | PennyMac/Rithm 10-Q/8-K | 🟠 |

### Multifamily — GSE + CMBS Books
| Metric | Value | As Of | Source | Status |
|--------|-------|-------|--------|--------|
| Fannie MF Serious DQ | **0.58% May** — see Marquee section above | May 2026 (rel Jun 26) | Fannie Mae | 🟠 (was 🔴) |
| CMBS MF DQ (Trepp) | **7.23% June (maturity-adj 9.53%)** — see Marquee section above | June 2026 (CREED 7/4 pull) | Trepp | 🔴🔴 |
| 2026 MF Maturity Wall | **$160B+ due 2026 (+50% YoY)**; broader $270B+ 2026-27 | 2026, Trepp/CRE Daily | Trepp | 🔴🔴 |
| Sun Belt MF Realization | S2 Capital (DFW) $400M fund **$0-to-LPs**; $140M DFW FCs Jun-22; ~1/3 of ~$900M TX CRE flagged July auctions; Trepp $2.54B hard CMBS maturities due July, 36% sub-8% debt yield | Jun-Jul 2026, TheRealDeal/CRE Daily | — | 🔴🔴 |
| Rent Growth Negative | **56% of top 100 cities** — CARL retains consumer-transmission read; HOMER carries as MF-demand context | Jan 2026, Apollo/Slok | Apollo/Slok | 🟠 |

### Mortgage Rates / Demand (HOMER-owned surface, ★ ruling)
| Metric | Value | As Of | Source | Status |
|--------|-------|-------|--------|--------|
| 30-Yr Mortgage (PMMS) | **6.49% Jul 9** (+6bps from 6.43% Jul 2, which was a 7-week low). Post-FOMC dip fully played out by Jul 2, then partially reversed. YoY 6.72% (-23bps). Still no genuine refi relief. **[Refreshed this session — was 3wk-stale at Jun 18 6.47%.]** | Jul 9, Freddie PMMS | Freddie | 🟠 |
| 10Y-FRM Spread | **~195-200bps** (vs ~150bps historical norm) — HOMER-owned mortgage-specific surface; Treasury/Fed direction referenced-only (BROCK/HENRY). Post-FOMC UST 10Y 4.52%/30Y ~4.95% (cracked 5.00% intraday, highest since 2007). [UST leg needs a fresh Jul pull next session — held at Jun 22 vintage.] | Jun 22, Freddie PMMS + UST | Freddie/UST | 🟠 |
| MBA Purchase Apps | **+1.1% WoW** (wk Apr 24) — refi window opened-and-shut, Refi −4.4%. **[STALE — owed a fresh weekly pull, not sourced this session.]** | Apr 24, MBA | MBA | 🟠 |
| Existing Home Sales (SAAR) | **4.09M June** (-2.4% MoM from May, +2.8% YoY), stays clear of <4.0M RED. Median $440,600 (+1.8% YoY, 36th consecutive YoY increase); inventory 4.6mo (1.56M units). **[Refreshed this session — corrects an inherited docket error that flagged this as a ~7/23 upcoming catalyst; it released 7/9. Next EHS release: Aug 10 (July data).]** | Jun 2026 (rel Jul 9), NAR | NAR | 🟠 |
| New-Home Sales + Builder Overhang | **580K SAAR May (−7.3% MoM, not stat-sig)**; **months-supply 10.3, tied 2008-09 bust high** (from 9.3 Apr). Builder supply ~2x existing. ~50% of AZ/FL listings cutting prices. | May 2026 (rel Jun 24), Census | Census | 🔴 |

### Builder Distress
| Metric | Value | As Of | Source | Status |
|--------|-------|-------|--------|--------|
| NAHB HMI June | **35** (−2 from May 37; 14th consec mo <40, 26th consec <50 — streak not seen since 2011-12). Traffic 25 unchanged; price-cutters 35% (up from 32%); incentives 62% (15th mo ≥60%). South 33 / West 27 = FL/Sun Belt epicenters. | Jun 16, NAHB | NAHB | 🔴 |
| Lennar FQ2 2026 | GM **15.6%** (−220bps YoY); EPS $1.24 (−31% YoY); ASP $371K (−5% YoY); orders −4% YoY. **FY26 delivery guide CUT ~85K→82-83K** (rates + geopolitics, not energy). K-shape demand biting now; margin defended via cost deflation at expense of volume. | Q2 FY2026 (rel Jun 11), LEN | LEN | 🔴 |
| DHI Q2 FY2026 | GM **20.1%** (litigation/warranty benefit + cost control, not pricing recovery). ASP −3% YoY; cancellations 16%; FY26 closings trimmed −500. Tariff $10,900/home = FY27 hit (CRL-23). | Apr 21, DHI | DHI | 🔴 |
| PHM Q1 2026 | GM **24.4% MISS** (−310bps YoY); incentives 10.9% (+290bps YoY). Mgmt names "K-shape" explicitly: active adult +14%, first-time flat. | Apr 23, PHM | PHM | 🔴 |
| KB Home FQ2 2026 | **Net income −75% YoY; op margin 8.6%→2.5%; revenue −27%; ASP −5.5%.** Sharpest builder-margin crush of the cycle — direct CRL-23 datapoint. | Q2 FY2026 (rel Jun 26), KBH | KBH | 🔴🔴 |

### Pricing / Inventory
| Metric | Value | As Of | Source | Status |
|--------|-------|-------|--------|--------|
| Case-Shiller National | **+0.8% YoY Apr** (nominal, ticked up from +0.7% Feb). **Real −2.4% YoY, 11th consecutive negative month.** Regional K-shape: Midwest/NE lead (Chicago +6.5%, NY +3.8%) vs Sun Belt/West fall (Seattle −2.3%, Denver/Tampa −1.8%, Phoenix −1.7%). | Apr 2026 (rel Jun 30) | S&P/CS | 🟠 nominal / 🔴 real |
| Freddie HPI YoY | **+1.9% May — ACCELERATING** off the revised Jan +0.9% trough (Apr +1.4% → May +1.9%; the inherited "Mar +0.7% cycle low" was a vintage print, since revised — verified vs CalculatedRisk 6/30). Moving AWAY from the "HPI turns negative 2026" call — nominal reframe to real-erosion. **Now the HOM-01 resolver series** (rollover call, see Predictions). | May 2026 (rel Jun 30) | Freddie | 🟠 (was 🔴) |
| Realtor.com List Price | **−2.4% YoY May, steepest decline since 2017** — leading-edge, ahead of the lagging close-price HPI series (60-90d lag → HPI likely rolls Jul-Aug). | May 2026, Realtor.com | Realtor.com | 🔴 |
| Redfin Sellers/Buyers Gap | **47% more sellers than buyers Apr** — narrowing from 49% end-2025 peak; imbalance present but moderating. | Apr 2026, Redfin | Redfin | 🟠 |
| Housing Starts Apr | SAAR 1.465M (−2.8% MoM); SF starts 0.930M (−9.0% MoM, most in nearly a year); MF +14.3% offsetting. 30Y 6.51% multi-week high transmitting. | Apr 2026, Census CB26-84 | Census | 🔴 |

### State-Level Housing (FL/TX priority)
| State | Metric | Value | As Of | Status |
|-------|--------|-------|-------|--------|
| FL | FC Starts (Monthly) | **3,315 #2 nationally** (behind TX 3,590); worst FC RATE 1 in 2,110 HU | May 2026, ATTOM | 🔴 |
| FL | Condo Inventory | **12.9mo** (vs SFH 5.4mo) — Triple Squeeze active. **[RECONCILE FLAG 7/12: probably Miami-Dade-specific, NOT statewide — CORAL carries statewide 8.9mo (FL Realtors Apr). Do not cite as statewide pending CORAL confirm — `reports/2026-07-12_FL-condo-reconciliation-package.md`]** | May 2026, Steadily/RESF | 🔴🔴 |
| FL | Q1 FC Filings (tri-county) | 3,168 units (1 in 846 HU), +9.4% QoQ, +16.6% YoY. 608-day avg FC timeline — late-24/early-25 pipeline hits market mid-late 2026. | Q1 2026, ATTOM | 🔴 |
| TX | Jul CRE FC Auction Pipeline | ~$900M flagged (~1/3 S2 Capital DFW MF) — see Marquee section | Jul 2026, TheRealDeal | 🔴🔴 |

---

## OPEN ITEMS

1. **First-boot data refresh — DONE this session for the highest-value rows** (ICE pipeline trio, PMMS, June EHS; see Inheritance verification note above). Still owed: MBA weekly purchase-apps refresh, UST 10Y/30Y leg of the 10Y-FRM spread, Freddie HPI/Case-Shiller next-print pulls (next release Jul 28 — see Catalysts). Not a hard blocker, but next session should close these.
2. **FL condo reconciliation — HOMER's side DELIVERED (round 2, this session):** `reports/2026-07-12_FL-condo-reconciliation-package.md`. Key result: the price "divergence" mostly dissolves on scope (−6.1% statewide vs −10% Miami-Dade epicenter median = expected, not contradictory — HOMER already carries the same −6.1% in STATE_HSG.tsv). One REAL conflict found: HOMER's "FL Condo Inventory 12.9mo" is probably Miami-Dade-specific mislabeled as statewide (CORAL: statewide 8.9mo FL Realtors Apr, Miami-Dade 12.9mo By The Sea Realty Apr; HOMER's own KB-HMR-016 corroborates Miami 13.2mo as the Q1 prior) — all 3 HOMER surfaces flagged in place pending CORAL confirm. Package includes proposed figure-ownership split + 5 questions for CORAL; CORAL delivery routed via PROME (route-out).
3. **CRL-06 data package DELIVERED this session** — `AGENTS/HOMER/reports/2026-07-12_CRL-06-data-package.md`. Full starts/filings/REO dataset incl. a genuinely new finding: the metric choice is outcome-determinative — starts (82,631 Q1, 55,718 Apr+May, tracking a 2nd straight >70K quarter) and filings (118,727 Q1) both already clear 70K, but REO (14,020 Q1) does not and is not the same order of magnitude — so "which metric" isn't a rounding question, it flips the resolution. CARL still owns the resolution call.
4. **CREED task packet DELIVERED 7/12, verified still on disk/unconsumed this session** (S5 demotion to HOMER-fed cross-reference + Trepp MF routing — `AGENTS/CREED/inbox/2026-07-12_from-DAEDALUS_homer-promotion-s5-demotion.md`). CREED's own 7/4 STATUS independently carries the same June 7.23%/9.53%-mat-adj Trepp figures HOMER owns — consistent, not contradictory; the packet's job is to formalize CREED as consumer, not to fix a numeric error.
5. **3-way Trepp citation collapse** — REGINALD packet DELIVERED 7/12, verified still on disk/unconsumed this session (`AGENTS/REGINALD/inbox/2026-07-12_from-DAEDALUS_homer-promotion-trepp-mf-owner.md`); HOMER-primary / CREED+REGINALD-consumer formalized in the rulings, but the REGINALD-side re-source lands at REGINALD's next boot — not yet executed in its files.

---

## CATALYSTS (near-term — full calendar in `docket/CATALYSTS.tsv`, corrected this session)

| Date | Event | Watch |
|------|-------|-------|
| **Jul 16, 10:00am ET** | NAHB HMI (July) | Builder sentiment continuation off June's 35 (14th consec <40) |
| **Jul 16** | ATTOM Q2 2026 foreclosures (est., unconfirmed) | CRL-06 metric test; V10 acceleration continuation — starts/filings pace already tracking >70K (see CRL-06 package) |
| **Jul 17** | Census Housing Starts/Permits (June) | SF vs MF starts split; South/West softness continuation |
| **Jul 21, 8:30am ET call** | DHI FQ3 2026 earnings (corrected from prior 7/22 est.) | CRL-23 FY27 tariff language; GM vs. KB Home's 2.5% floor |
| **Jul 22, 8:30am ET call** | PHM Q2 2026 earnings (corrected from prior 7/23 est.) | CRL-23 read-through; K-shape commentary continuation |
| **Jul 28** | S&P Case-Shiller (May data) | Nominal-accel/real-negative divergence continuation; Realtor.com leading-edge rollover test |
| **~Jul 30** | Freddie FMHPI (June data) | **HOM-01 Leg-1 first read** (YoY below May's +1.9% = streak break); early-kill arm 1 of 2 if it accelerates |
| Thu, weekly, 12:00pm ET | Freddie PMMS | Rate trajectory off Jul 9's 6.49% (+6bps off 7-wk low) |
| ~late-Jul | Trepp CMBS (June/July print), Fannie June MF DQ | GSE-vs-CMBS divergence continuation |
| Aug 10 | NAR Existing Home Sales (July data) | **[Corrected this session — June data already released 7/9 (4.09M SAAR); do not treat EHS as a ~7/23 catalyst.]** |
| ~Aug | MBA Q2 NDS | Pipeline confirmation |

---

## PREDICTIONS

**HOM-01 OPEN (registered 2026-07-12, round 2 — first HOMER-native prediction):** Freddie FMHPI national nominal YoY **rolls over** — Leg 1 (direction): Jun- or Jul-data release prints YoY below the prior month, ending the post-trough accel run (Jan +0.9% revised trough → Apr +1.4% → May +1.9%); Leg 2 (level): YoY ≤ +1.0% by the Aug-data release (~Sep 30). BOTH legs = CONFIRMED; 60%, PROVISIONAL tier. Mechanism: Realtor.com list-price lead (−2.4% YoY May, steepest since 2017; 60-90d list-to-close lag). Early-kill: Jun AND Jul data both accelerate >+1.9%. Registration note: the inherited "Mar +0.7% cycle low" was a vintage print — FMHPI revisions moved the trough to Jan +0.9% (verified vs CalculatedRisk 6/30 post); grading uses each release's as-published figures. Full mechanics: `thesis/PREDICTIONS.tsv`.

**CRL-06 (foreclosures >70K/qtr) and CRL-23 (builder FY27 GM compression) remain on CARL's `thesis/PREDICTIONS.tsv`** — parent-retained per DAEDALUS ★ ruling (both are CARL convergence-matrix thesis-scoring instruments); HOMER is the data owner feeding them, not the resolution owner. CRL-06 data package (this session) is the current best evidence pack; CARL owns the resolution call.

---

## BOTTOM LINE

HOMER's first live session closed the promotion-rebuild's honest data-vintage gap on the highest-value rows: inheritance verification found the copied figures themselves clean (0 drifts on Fannie 0.58%, Trepp 7.23%/9.53%, ATTOM 82,631 starts — all confirmed against primaries), but 3 rows had aged out since the 6/26-7/4 cutover pulls and are now refreshed (30Y PMMS 6.49% Jul 9, ICE FC-pipeline trio to May, NAR EHS to the actual June print — which also corrected an inherited docket error that had June's already-released 7/9 report misfiled as a ~7/23 upcoming catalyst). The single most important thing right now is still the GSE-vs-CMBS multifamily divergence (Fannie improving to 0.58% vs. Trepp deteriorating to a maturity-adjusted 9.53% multi-year high, now confirmed on both legs) — HOMER is the one owner, CREED/REGINALD are consumers, and both handoff packets are verified still on disk and unconsumed (expected — lands at their next boots). The CRL-06 data package is delivered (`reports/2026-07-12_CRL-06-data-package.md`) with a genuinely new finding: the starts-vs-filings-vs-REO metric choice is outcome-determinative, not cosmetic — CARL's resolution call actually matters. Next: ATTOM's ~7/16 Q2 release (date still unconfirmed by press release) is the next hard test; NAHB (7/16), Census starts (7/17), and DHI/PHM earnings (7/21, 7/22 — both corrected by a day from the inherited estimate) are the near-term catalyst wall, each now carrying an exact date/time and a mechanical resolver per the sweep's GAPS lens (see `reports/2026-07-12_domain-sweep.md`). Round 2 (same day, PROME-directed) added the first HOMER-native prediction — HOM-01, the FMHPI nominal-rollover call (60% PROVISIONAL, first resolver ~Jul 30) — and delivered HOMER's side of the FL-condo reconciliation with CORAL, which dissolved the headline price "divergence" on scope but surfaced a real label conflict in HOMER's own 12.9mo inventory row (probably Miami-Dade, not statewide — flagged in place pending CORAL confirm).
