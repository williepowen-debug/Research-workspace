# HANS Revival Plan — 2026-06-22

> **HISTORICAL — a 2026-06-22 planning document, not maintained.** Its levels are June-2026 vintage and must not be read as current (see `CLAUDE.md` §revival warning). Live state → `STATUS.md`.
> *(HISTORICAL banner added 2026-09-18 at closeout. Found via `consumer_check --self`, which flagged statement-time values here as stale: they are correctly-dated HISTORY, and the defect was that nothing on the file SAID so. Data Hygiene requires a surface be FROZEN-with-a-banner or LIVE-with-an-alert, never the silent-rot middle — these were neither.)*

**Owner:** Prome / HANS  
**Purpose:** Bring HANS back to decision-useful state after stale Mar-Apr war-regime assumptions.  
**Operating rule:** break the work into small packets. Each phase must leave HANS more useful even if we stop there.

---

## Diagnosis

HANS has valuable scaffolding — PMI→ISM, ECB/Fed divergence, UST custody flows, European bank exposure, energy/storage, sovereign spreads — but his live state was dangerously stale. `STATUS.md` had been anchored to Apr30 assumptions: protracted kinetic war, Hormuz closed, Qatar LNG permanent loss, Brent ~$111, Scenario D ~85%.

That baseline is now archived at `archive/STATUS_PRE_REVIVAL_2026-06-22.md`. Current live baseline is `STATUS.md`.

---

## Revival Principles

1. **Current facts first.** No March/April assumption survives unless re-verified.
2. **U.S.-market transmission only.** HANS is not a Europe encyclopedia.
3. **One channel per work packet.** PMI, ECB, TIC, energy, banks, sovereign spreads each get their own pass.
4. **Write as you go.** Every phase updates `STATUS.md` or a named research file.
5. **No trade proposals from HANS.** He flags signals; TERRY/Prome translate into trade structure if needed.
6. **Self-contained outbox only when thresholds fire.** No acknowledgment mail.

---

## Phase 0 — Safety Reset ✅ Completed

**Goal:** Prevent stale HANS from contaminating future work.

**Done:**
- Archived Apr30 status to `archive/STATUS_PRE_REVIVAL_2026-06-22.md`.
- Replaced `STATUS.md` with a current revival baseline.
- Patched `CLAUDE.md` with revival warning and corrected scope/thresholds.
- Retired live use of: Hormuz closed/mined, Qatar permanent loss, Brent $111, Scenario D 85%, HY 350+, old gate counts.

**Stop condition:** HANS can cold-boot without starting from false regime assumptions.

---

## Phase 1 — Current Snapshot / Dashboard ✅ Batch A complete 2026-06-22

**Goal:** Establish HANS’s live “what matters now” page.

**Scope:** Pull current levels / latest releases for the six HANS channels:

| Channel | Minimum current facts |
|---|---|
| PMI / industrial lead | Germany/EZ manufacturing, services, composite; latest German IP/orders if easy. |
| ECB / policy divergence | ECB deposit/MRO/MLF, latest projections, market-implied path if available, EUR/USD. |
| UST/custody flows | Apr 2026 TIC country table: UK, Ireland, Lux, Belgium, France, Switzerland, Germany, Euro Area. |
| Energy/storage | TTF, EU storage %, injection pace, winter target gap, LNG flow context. |
| Banks/private credit | ECB/EBA/Reuters/primary notes on concentrated exposures; names and mechanism only. |
| Sovereign/LDI | France-Germany, Italy-Germany spreads, UK 10Y/30Y gilt stress, TPI/LDI watch. |

**Deliverables:**
- `AGENTS/HANS/research/REFRESH_2026-06-22.md`
- `STATUS.md` updated with current snapshot table.

**Batch A result:** completed as a pre-PMI snapshot. Current read: Europe is mixed/stagflationary; manufacturing has not broken enough to confirm U.S. ISM weakness, but services/composite are contracting and ECB tightened into the mix. Jun23 flash PMIs remain pending.

**Stop condition:** Will/Prome can read one page and know whether Europe confirms, contradicts, or complicates the U.S. thesis.

---

## Phase 2 — PMI → ISM Lead Module ✅ Scaffold complete / Jun23 update pending

**Goal:** Restore HANS’s highest-value signal.

**Questions:**
1. Did Jun Germany/EZ flash PMIs confirm recovery or re-arm weakness?
2. Is German manufacturing still leading U.S. ISM by ~2 months in current data?
3. What July/Aug U.S. ISM read does Europe imply?
4. Is services masking manufacturing weakness or vice versa?

**Deliverables:**
- `AGENTS/HANS/research/PMI_ISM_LEAD_2026-06.md`
- `STATUS.md` PMI section updated.
- Outbox to HENRY/NEXUS only if threshold fires:
  - German mfg PMI <48 or rapid 2-month decline = 🟠 weakness lead.
  - German mfg PMI >50.5 with broad strength = 🟡 contradiction to U.S. slowdown thesis.

**Stop condition:** HANS can answer: “What does Europe imply for U.S. ISM timing?”

**Next mini-task before/alongside Batch B:** after Tue 2026-06-23 flash PMIs print, update the Jun row in `PMI_ISM_LEAD_2026-06.md`, classify the signal, update `STATUS.md`, and send outbox only if the <48 weakness or >50.5 broad-strength contradiction threshold fires.

---

## Phase 3 — ECB / Fed Divergence + Funding ✅ Batch B1 complete 2026-06-22

**Goal:** Determine whether Europe is tightening into weakness and what that does to dollar funding / UST demand.

**Questions:**
1. Was the Jun11 ECB hike a one-off inflation defense or start of a renewed hiking path?
2. How does ECB/Fed divergence affect EUR/USD, DXY, and European demand for dollar assets?
3. Is dollar funding stress showing up in EUR/USD basis, swap lines, or bank funding data?
4. Does TPI matter yet?

**Deliverables:**
- `AGENTS/HANS/research/ECB_FED_DIVERGENCE_2026-06.md`
- Updated thresholds in `STATUS.md`.
- Optional outbox to LIQUID/BOND if funding/spread thresholds fire.

**Batch B1 result:** completed Jun22. ECB Jun11 hike classified as **conditional renewed tightening risk**; Fed still has the higher policy anchor at Fed midpoint **3.625%** vs ECB deposit **2.25%** (+137.5bp USD-over-EUR). Funding stress is monitor-only: no verified threshold fired; EUR/USD basis remains a data gap; Fed SWPT was operational-size, not crisis use.

**Stop condition:** HANS can say whether Europe is easing pressure on U.S. rates or adding term-premium/funding risk.

---

## Phase 4 — UST Custody / TIC Flow Refresh ✅ Batch B2 complete 2026-06-22

**Goal:** Rebuild Europe’s role in the UST demand map.

**Questions:**
1. Are UK/Ireland/Lux/Belgium still absorbing USTs?
2. Is Belgium/Euroclear behaving like a China/official proxy or just custody noise?
3. Is Europe offsetting Japan/China selling or joining the demand hole?
4. Are bill vs coupon flows diverging?

**Deliverables:**
- `AGENTS/HANS/research/EUROPE_UST_HOLDINGS_2026-04_TIC.md` ✅ Created.
- `workbook/VX.tsv` update deferred per Batch B2 scope; exact recommended workbook updates listed in the research doc for Phase 8.
- Optional outbox to LIQUID/ZHAO/SAM if Europe custody selling appears material. Not written; no verified threshold fired.

**Batch B2 result:** completed Jun22. Correct Apr2026 TIC Table 5/Table 3 data retrieved. Europe is **neutral/noisy, not a confirmed UST demand-hole contributor**: seven-country watchlist holdings **$2.963T**, Apr net sales **~-$0.7B**, coupon/LT **+$17.4B**, bills/ST **-$17.0B**. UK bought; Belgium/Ireland/Germany sold; custody attribution caveats are central for Ireland/Lux/Belgium/Euroclear.

**Stop condition:** Europe’s UST-demand role is current enough for LIQUID/NEXUS synthesis.

---

## Phase 5 — Energy / Storage / Industrial Competitiveness ✅ Batch C1 complete 2026-06-22

**Goal:** Separate true EU energy stress from stale war-panic assumptions.

**Questions:**
1. Is EU storage path adequate for winter 2026-27?
2. Is TTF in manageable seasonal relief or still structurally punitive?
3. Does the EU-China energy-cost wedge still support deindustrialization/capacity migration?
4. Does renewed Hormuz risk re-arm the March energy-stagflation channel?

**Deliverables:**
- `AGENTS/HANS/research/EU_ENERGY_STORAGE_2026-06.md` ✅ Created.
- `STATUS.md` energy section updated. ✅
- `FLOW-HANS-8` status recommendation: **CONDITIONAL**. ✅
- Optional outbox to BRENT/HENRY/LIQUID if storage/TTF threshold fires. Not written; no verified threshold fired.

**Batch C1 result:** completed Jun22. EU energy is **CONDITIONAL, not ACTIVE**: TTF/EU gas about **€42.49/MWh** is below the **>€50/MWh** alert line, but storage **45.56%** vs **54.38%** year ago and a ~**+0.21pp/day** recent injection pace leave the 80% Nov1 path dependent. The EU-U.S./China industrial energy-cost wedge remains structurally punitive. Hormuz risk is monitored as declaratory/contested tail risk unless physical disruption is verified.

**Stop condition:** HANS can say whether energy is currently a live stress channel or a conditional tail.

---

## Phase 6 — European Banks / Private Credit / CRE Bridge ✅ Batch C2 complete 2026-06-22

**Goal:** Connect Europe to BROCK/REGINALD/LIQUID without exaggerating systemic risk.

**Questions:**
1. What are the actual private-credit exposures at Deutsche, Barclays, BNP, HSBC, UBS?
2. Are exposures concentrated but manageable, or a dollar-funding/transmission bridge?
3. Are European CRE gates still relevant after March signals?
4. What would confirm contagion: CDS, funding, provisions, gating, regulatory action?

**Deliverables:**
- `AGENTS/HANS/research/EU_BANK_PRIVATE_CREDIT_2026-06.md` ✅ Created.
- Handoff thresholds for BROCK/REGINALD/LIQUID/NEXUS. ✅ Added in research doc and STATUS.
- Optional outbox only if a named threshold fires. Not written; no verified current threshold fired.

**Batch C2 result:** European bank/private-credit risk is **MONITOR, not ACTIVE bridge**. DB/Barclays/BNP/HSBC concentrate nearly two-thirds of BI/The Banker’s **€137B** UK/Europe bank exposure estimate, but disclosed exposures are mostly **~2–3% of loan books**; ECB supervisory data put euro-area bank worldwide PC exposure at **€62.5B** (**0.2% assets / 2.5% equity**) and modeled direct bank losses **≤1.3% equity**. UBS Euroinvest CRE gate remains sourceable/current but small. Upgrade only on bank CDS/funding/provisions/regulatory action, multiple large gates, or forced selling.

**Stop condition:** Europe’s PC/bank link is demoted to monitor with explicit upgrade thresholds.

---

## Phase 7 — Sovereign Spread / UK LDI Monitor ✅ Batch C3 complete 2026-06-22

**Goal:** Restore the Europe rates-stress early warning system.

**Questions:**
1. Are French/OAT spreads still core-safe, or drifting into periphery behavior?
2. Is Italy near TPI-sensitive levels?
3. Is UK gilt/LDI stress dormant or re-emerging under higher global duration vol?
4. Does European sovereign stress help USTs via flight-to-quality or hurt via global duration repricing?

**Deliverables:**
- `AGENTS/HANS/research/SOVEREIGN_LDI_MONITOR_2026-06.md` ✅ Created.
- Updated `STATUS.md` rates/spreads table. ✅
- Updated `workbook/VX.tsv` sovereign/LDI rows. Deferred to Batch D by C3 scope; exact row recommendations listed in research doc.

**Batch C3 result:** European sovereign/LDI stress is **ABSENT/MONITOR**. France is **yellow political-risk premium** rather than old-core clean or new-periphery: Jun22 same-source TE yields imply OAT/Bund **~65bp**, below **80bp** orange / **100bp** red. Italy is **green** at BTP/Bund **~71bp**, far from **150–200bp** stress or **>200bp** TPI-sensitive levels. UK gilt/LDI risk is elevated but contained: UK 10Y **4.80%**, 30Y **5.50%**, both easing over the month; March LDI cash calls were limited/normal-market per Reuters. UST impact is mildly helpful/neutral now; harmful term-premium risk only if UK long-end volatility re-accelerates or France/Italy spreads widen together.

**Stop condition:** HANS can explain whether Europe rates stress is absent, helpful to USTs, or term-premium negative.

---

## Phase 8 — Workbook Hygiene / Cold-Boot Hardening ✅ Batch D complete 2026-06-22

**Goal:** Make HANS durable again.

**Tasks:**
- ✅ Update `workbook/VX.tsv` current values or mark rows STALE.
- ✅ Add Jun 2026 findings to `workbook/ML.tsv`.
- ✅ Reclassify stale flow rows in `workbook/FLOW.tsv`.
- Not needed: compact boot order / README; `CLAUDE.md` + `STATUS.md` now provide the cold-boot guardrail.
- Not in Batch D scope: old inbox processing; no current verified threshold required outbox.

**Deliverables:**
- `workbook/VX.tsv` refreshed for Apr TIC, ECB/Fed, energy/storage, PMI pending rail, sovereign/LDI, and stale war rows.
- `workbook/FLOW.tsv` demoted stale war/diesel active rows to monitoring.
- `workbook/ML.tsv` appended with durable Jun22 revival lessons (`ML-HANS-386`–`ML-HANS-392`).

**Batch D result:** complete. HANS no longer cold-boots from the stale Feb/March war regime; Jun23 PMIs remain the next pending live rail.

**Stop condition:** A fresh HANS spawn can update one channel without rereading months of stale files.

---

## Suggested Execution Order

**Batch A — Make him useful this week:** Phases 1–2.  
**Batch B — Rates/funding relevance:** Phases 3–4.  
**Batch C — Stress bridges:** Phases 5–7.  
**Batch D — Durability:** Phase 8.

Recommended next action after Batch A: do the **Jun23 PMI mini-update** when actuals print, then run **Batch B** as two separate packets if needed:
1. ECB/Fed divergence + funding basis. ✅ Complete Jun22.
2. TIC/custody country table refresh. ✅ Complete Jun22.

Do not let Batch B drift into sovereign spreads, bank/private-credit, or energy; those belong to Batch C. Batch C1 energy/storage, Batch C2 bank/private-credit/CRE, C3 sovereign/LDI, and Batch D workbook/cold-boot hygiene are now complete. Next live packet is the Jun23 PMI mini-update when actuals print.

---

## Open Decision for Will

Do we want HANS revived as:

1. **Fast tactical monitor** — Phase 1 + Phase 2 only this week; rest later.
2. **Full domain refresh** — all phases over several packets.
3. **Minimal safety reset** — stop after Phase 0 unless Europe starts firing thresholds.

Prome recommendation: **Option 1 now**, then Phase 3/4 if PMI or ECB/Fed divergence becomes market-relevant.
