# CREED — National CRE / CMBS Coverage Map

**The map of the territory CREED owns, lane by lane: what it covers, where the number comes from, how fresh the *data* is, and how well-built the lane actually is.** `STATUS.md` is the live dashboard; **this is the map.** Adopted 2026-07-27 from `CORAL/COVERAGE.md` (the 10-pillar Florida map).

*Last refreshed: 2026-07-27 (created; lanes seeded from the 7/27 pack + the then-31-vector workbook — now 32).*

> 🔴 **THE LANE TABLE BELOW IS PRE-FIRE AND KNOWN-STALE (flagged 2026-08-20, rebuild pending).** It predates the 8/13 and 8/20 sessions: lanes 1–3 carry **June** prints as live reads (July: office DQ **11.91%**, office SS **16.58%**, maturity-adj **9.62%**), **lane 3 owns `CREED-T-02` which FIRED 2026-08-20**, lane 6 describes a courier arrangement **killed 8/13**, and lane 1 repeats the **refuted** "Trepp PDF paywalled" claim. **Cite `STATUS.md` and `thesis/THESIS.md`, not this table, until the rebuild lands.** Counts in this header were corrected 8/20; **the lanes were not.**

**Maturity legend:** 🟢 well-covered (fresh data + workbook vectors + a trigger) · 🟡 partial (data exists, gaps or one-source) · 🔴 thin/stub (needs build-out) · ⏳ in flight

> ### ⚠️ Why this file exists, and what it does that `VX.tsv` cannot
> **`VX.tsv`'s `Last_Updated` is a TOUCH date, not a DATA VINTAGE.** At creation all 31 vectors read `2026-07-27` because that is when the workbook was built — while the underlying prints ranged from **FDIC Q1** to **intraday 7/27 tape**. *(Now 32 vectors, and a handful carry `2026-08-20` after the Trepp primary-read pass — **which does not weaken the point, it sharpens it: the file now mixes touch dates across three sessions, so scanning `Last_Updated` is even less informative than when this warning was written.**)* A reader scanning `Last_Updated` would conclude the whole surface is same-day fresh. **It is not, and the difference is exactly where CREED gets hurt.** This map is keyed to **data vintage**, which is the thing that decides whether a number is citable.
>
> **The second reason is worse:** CREED's life-science coverage gap — on the exact asset class inside OZK's Seattle credit *and* KREF's risk-5 reserves — **was found by WALTER, not by CREED.** CREED had no map of its own territory, so it could not see a hole in it. `finding_count_measures_intake_not_domain`: *you can audit what you killed, never what you never saw.* **§Blind spots below records who found each gap, because a gap someone else finds is evidence of a systematic blind spot, not a one-off.**

---

## The lanes

| # | Lane | Scope | Vectors / owner docs | Data vintage + live read | Maturity |
|---|---|---|---|---|---|
| 1 | **CMBS delinquency by property type** | office/overall/retail/lodging/industrial DQ; the S1 gauge | `VX-1.01/1.02/1.04/1.05/1.06`; `CREED-T-01a` | **June 2026 Trepp** — office **11.57%** (+4bps), overall 7.35%, retail 6.91%, lodging 5.22%, industrial 1.20%. Trigger >12% hold-2: **no fire.** ⚠️ **Trepp PDF paywalled = primary-CITED, not primary-READ**; co-circulating "retail 12.95%" **UNVERIFIED, do not cite** | 🟢 |
| 2 | **Special servicing** | office/overall SS + the SS−DQ spread (the extend-and-pretend signature) | `VX-2.01/2.02/2.03`; `CREED-T-01b` | **June 2026** — office SS **17.11%** (+36bps), overall 11.2% (+34bps). 89bps under the 18% trigger: **no fire.** The 7/20 vintage-conflation flag was a **false alarm**, retracted 7/27 (WALTER refuted its own hypothesis) | 🟢 |
| 3 | **Maturity wall** | CMBS 2026 maturities, hard vs total, Q4 concentration, maturity-adjusted DQ | `VX-3.01/3.02/3.03`; `CREED-T-02` | **>$100B** CMBS total (>50% not expected to repay, Morningstar DBRS); **$76.6B hard**, 39% in Q4, 36% at DY≤8% (Trepp); maturity-adj DQ **9.53% = multi-year high**. ⚠️ **$875B is REGINALD's** all-lender figure, **not CREED's** — they nest, don't compete | 🟢 |
| 4 | **Bank transmission** | FDIC non-owner CRE PDNA, reserve coverage, named-bank provisioning | `VX-4.01/4.02/4.03/4.04`; `CREED-T-03`; → REGINALD | **FDIC Q1 2026** — large-bank non-owner CRE PDNA **3.40%, still IMPROVING (6th straight quarter)**; overall PDNA 1.53%. **S3 held at 2.** ⚠️ **Q2 QBP (~late Aug) is where the trigger actually lives** — this lane is a quarter stale *by construction*, not by neglect. Live watch-add: OZK Special Mention **+$219M** fresh/unattributed while ACL **released** $10.7M | 🟡 |
| 5 | **Modifications / re-default** | mod volume, 2nd-mod rates, re-default, extension refusals | `VX-8.01` **(1 vector — the thinnest lane)**; `CREED-T-04` | Asset-level only: **Sangertown = a 3rd extension REFUSED on a DSCR hurdle** after rolling twice — the cleanest specimen of extend-and-pretend ending on schedule. **No aggregate series.** ⚠️ **`CREED-T-04` has NO numeric band — it is the only trigger in the registry that is purely qualitative** | 🔴 |
| 6 | **Multifamily** | Trepp CMBS-MF DQ, GSE-vs-CMBS divergence, Sun-Belt realization | `VX-1.03/6.01` — **HOMER-owned for SCORING** | **June 7.23%** (+28bps), maturity-adj 9.53%. ⚠️⚠️ **CITATION LOOP: HOMER's figure is attributed "(CREED 7/4 pull)."** CREED cites HOMER, HOMER cites CREED. **Scoring is HOMER's; the DATA PULL is unassigned.** Routed 7/27, awaiting HOMER's (a)/(b) call. **Keep reading the MF row inside the whole-Trepp pull meanwhile** | 🟡 |
| 7 | **Forced sale / NAV recognition** | realized comps >30% below basis, fund gates, large-book clearing prices | `VX-5.01/5.02`; `CREED-T-06/-06b` | **Cluster, not a single instance:** 205 W Randolph −72% realized, Aon Center −58% appraisal, Galveston $8.79/sf, OZK Seattle deed-in-lieu. **Counter-datum: ARI's ~$9B cleared at 99.7%** — the largest clean mark-validation in the rails, and **the reason S6 was HELD at 3, not raised** | 🟢 |
| 8 | **Office demand (structural)** | tenant demand, AI/return-to-office, conversion exits, life science | `VX-7.02/7.03`; `CREED-T-07` | Life science **CLOSED 7/27: BIFURCATED, not collapsing** [Savills Q2-26] — distressed markets *absorbing* (Chicago 37.6% from 39.2%), Boston/SF worsening on **new supply, not tenant loss**. Conversion exit attacked (Seattle) — **mechanism noted, number NOT adopted** | 🟡 |
| 9 | **CRE equity tape (S8a)** | VNQ-vs-SPY relative, office REITs, malls, brokers, data centre | `VX-7.01`; `CREED-T-08a`; `research/REIT_EQUITY_TAPE_MODULE` | **Intraday 7/27** — VNQ vs SPY **+2.04pp/3mo, FLIPPED POSITIVE**; trigger **12pp away and receding**. Office REITs +14% to +77%/3mo. **COUNTER-SIGNAL, strengthened. Honor it.** *(Not closes — do not re-cite as closes)* | 🟢 |
| 10 | **CRE credit / lender tape (S8b)** | CRE mREIT cohort: dividends, book erosion, provisioning, capital withdrawal, migration to insurers | `VX-10.01`–`10.05`; `CREED-T-08b`; → LIQUID, SHADE | **NEW 7/27** — 7 of 11 mREITs negative/3mo (median ≈ −9%); ARI wind-down (~$9B → Athene at 99.7%), KREF dividend −60%. **8 of 11 held dividends — selective, not a cascade.** ⚠️ **Never cite a CRE mREIT price move without checking corporate actions** | 🟢 |
| 11 | **CRE financing flow (MBA)** | who is adding/shedding CRE debt by holder channel | `VX-9.01`; `KB-CREED-017`; → SHADE | **Q1 2026** (rel 6/18): banks +$17.5B · agency +$12.8B · **life +$3.3B → $775B** · **CMBS/CDO/ABS −$9.6B**. ⚠️ **$775B is WHOLE-LOANS-ONLY** (MBA attributes to the note-holder) — a **floor** on insurer CRE exposure, not a measure of it. ⚠️⚠️ **And the buckets are "note held by an insurer" vs "note held by a TRUST" — an insurer buying a CMBS bond prints in the CMBS bucket.** So −$9.6B is **not** cleanly "the securitized channel shedding." **`FLOW-CREED-08` demoted to real-but-UNESTABLISHED**; `VX-9.01` confidence 82%→60%. Next print ~mid-Sept | 🟡 **(was 🟢 at creation — the level is primary-verified and unchanged; what fell is the INTERPRETATION it supports)** |
| 12 | **Office pricing & vacancy** | price indices, national vacancy — the valuation layer under everything else | `VX-9.02` **(GAP)**, `VX-9.03` | 🔴 **`VX-9.02` Green St CPPI = GAP, no access.** 🔴 **`VX-9.03` national office vacancy is seeded at Q1 vintage** — a clean Moody's Q2 print was **not locatable** on 7/27. **This is CREED's worst-covered lane and it sits underneath the whole thesis** | 🔴 |

---

## ⚠️ Blind spots — and who found each one

**The discipline: record the FINDER.** A gap CREED finds is a lane to build. **A gap someone else finds is evidence of a systematic blind spot** — and **four of the five** below were found by someone else. *(This line read "three" from creation until the 7/27 closeout audit caught it contradicting its own table — the **second** count-drift CREED introduced today while cataloguing the same class in four other agents. Both were found by auditing, neither by remembering.)*

| Gap | Found by | Status |
|---|---|---|
| **Life science** — zero CREED+REGINALD hits, on the exact asset class in OZK's Seattle credit **and** KREF's risk-5 reserves | ⚠️ **WALTER** | **CLOSED 7/27.** Savills Q2-26; bifurcated, not collapsing |
| **The CRE lender leg (S8b)** — S8 was keyed to VNQ-vs-SPY and office-REIT *equity*, so it was structurally blind to the credit side | **CREED** (7/27) | **CLOSED** — S8 split 8a/8b, 5 new vectors, new independent root |
| **Data-centre CRE demand** — the AI↔CRE crossover | ⚠️ **NEXUS** (M-09 weld) | Monitored, **explicitly NOT an independent vote** (shares the M-09 node) |
| **The ARI→Athene affiliated-transfer leg** — CREED routed the transaction and missed that it was related-party | ⚠️ **SHADE** | **CLOSED 7/27**, absorbed with the anti-fusion discriminator |
| **`PRED-CREED-006`'s baseline was a seasonal trough** | ⚠️ **SHADE** | **CLOSED 7/27** — re-spec'd to ≥+$10B (*not* SHADE's proposed +$20B, which over-corrected) |

**Read across the finder column: 4 of 5 were found by other agents.** That is the argument for this file existing, and for §Build-out below.

**Structurally un-owned, flagged rather than claimed:** the **national insurance-cost → NOI/DSCR amplifier**. CREED touched it 7/22 (AEOLUS CA FAIR Plan cc) and **took no claim** — AEOLUS owns C4, REGINALD owns the muni/bank translation, CORAL owns FL. **Nobody owns the national CRE-operating-cost channel.** Not CREED's to seize unilaterally; worth naming to PROME.

## Boundaries — reconcile to one number, don't fork

| Shared metric | One owner | CREED's role |
|---|---|---|
| Bank non-owner CRE PDNA (`VX-4.01`) | **REGINALD** | reconcile to REGINALD's figure |
| Trepp CMBS-MF DQ (`VX-1.03/6.01`) | **HOMER** (scoring) | cite HOMER; **data pull unassigned — see lane 6** |
| $875B all-lender 2026 maturity wall | **REGINALD** | CREED owns the **CMBS slice** (>$100B / $76.6B hard) |
| Whole-Florida CRE synthesis | **CORAL** | FL-specific only; national context is CREED's |
| Insurer absorption / combined sink | **SHADE** | CREED supplies the **CRE leg** of the flow series |
| Funding / refi capacity / plumbing | **LIQUID** | CREED routes lender-withdrawal + refi pressure |

## Build-out backlog (priority order)

1. 🔴 **Lane 12 — office pricing & vacancy.** Two vectors, one a hard GAP and one Q1-stale, sitting **under the entire valuation argument**. Highest-value build. Needs an accessible price-index substitute for Green St CPPI and a locatable Q2 vacancy print.
2. 🔴 **Lane 5 — modifications.** One vector, no aggregate series, and the **only purely-qualitative trigger in the registry**. `CREED-T-04` is a candidate for a Will-gated numeric band once a series exists.
3. 🟡 **Lane 6 — close the MF citation loop.** Blocked on HOMER's (a)/(b) reply.
4. 🟡 **Lane 4 — FDIC Q2 QBP (~late Aug).** Not a build, a scheduled resolution: `PRED-CREED-003`, the single most decision-relevant open item.
5. **Verify-if-load-bearing** (do not spend unless pivotal): KREF Q2 10-Q primary; Meadows occupancy/DSCR; Seattle 37% vacancy vs CoStar/JLL.
