# CORAL — Florida Real Estate Stress Monitor
## Comprehensive Florida Agent | 10 pillars (real estate · insurance · banks · migration · tourism · fiscal · labor · climate)

**Last Updated:** 2026-09-13 ~12:1x ET (Sun) — PROME L0 owner spawn (DOCKET L332 / WQ-184). Headlines: **(1) 🟠 GATE-CORAL-MSI-01 STANDS DOWN.** Reading #6 = **4-of-5 >6.0** — the SECOND consecutive sub-threshold reading, 11 days after the first, so the Will-ratified 8/23 condition is **MET** and the supply-side price-discovery leg goes **🔴→🟠**. ⛔ **THE LEG ONLY** — CORAL overall stays 🟠 and the **BANK-TRANSMISSION RAIL is untouched in BOTH directions.** **(2) ⚠️ IT FIRED ON DATA THAT MOVED THE OTHER WAY** — 3 of 5 metros ROSE, Lakeland re-crossed **above** 6.0, Tampa a **series high 7.15**; breadth fails on **Cape Coral alone (5.91)**. Graded **as written, not re-fitted**; the rule defect goes to Will as a **PROSPECTIVE** question (OQ S). **(3) Parcl listings now render a literal `0` placeholder** — never carry "0 listings." **(4) FL enrollment: the routed −7,600 does NOT reconcile at primary** (§ FL ENROLLMENT). **(5) Mail drained 5-of-5.**

**File map (read-cap split 2026-09-02):** **`STATUS.md`** = state, colours, live levels, every owed action (boot-read whole) · **`STATUS_DETAIL.md`** = the full evidence rows behind each dashboard line — sources, vintages, basis caveats (on-demand, sectional) · **`archive/STATUS_SESSIONS_20260721-20260823.md`** = dated session narrative 7/17→8/23, verbatim (never boot-read). **State disagreement ⇒ this file wins; provenance disagreement ⇒ `STATUS_DETAIL.md` wins; either disagreement is a defect to fix.**

---

## 9/13 (Sun) — 🟠 MSI LEG STANDS DOWN ON A RULE THAT FIRED AGAINST THE DATA'S DIRECTION — READ FIRST

⭐ **Full evidence — per-metro series, verbatim stamps, the triple-verification legs, the listings-placeholder finding → `STATUS_DETAIL.md` § "2026-09-13 session evidence".** *(The 9/2 session block that stood here is preserved VERBATIM at `STATUS_DETAIL.md` § "2026-09-02 session evidence".)*

**1. 🟠 GATE-CORAL-MSI-01 — reading #6. The stand-down condition is MET.** Parcl metro pages pulled direct 2026-09-13 ~12:0x ET, HTTP 200 on all five; **all five self-stamp `Updated: 9/13/2026`** (verbatim) — a **NEW** vintage vs the 9/3 pages of reading #5, so this is a new observation, not a re-read.

| Metro | MSI 9/2 | **MSI 9/13** | Δ | >6.0? |
|---|---:|---:|---:|:--:|
| Tampa | 7.01 | **7.15** | **+0.14** | ✅ |
| Punta Gorda | 6.52 | **6.59** | +0.07 | ✅ |
| North Port | 6.29 | **6.27** | −0.02 | ✅ |
| **Cape Coral** | 5.95 | **5.91** | −0.04 | ❌ |
| **Lakeland** | 5.97 | **6.01** | **+0.04** | ✅ |

**⇒ 4-of-5 >6.0. <5-of-5 ⇒ SUB-THRESHOLD READING 2 OF 2.**

⛔ **GRADED ON THE FROZEN 8/23 LETTER, NOT RE-FITTED.** All three legs check out independently: reading 1 (9/2) 3-of-5 **<5-of-5** ✅ · reading 2 (9/13) 4-of-5 **<5-of-5** ✅ · spacing **11 days** by observation and **10 days** by page vintage, both **≥10** ✅ · **CONSECUTIVE** — no MSI reading was taken or logged between 9/2 and 9/13 (KB ends at ML-CORAL-074; no CORAL commit between) ✅. **⇒ 🔴→🟠 ON THE SUPPLY-SIDE PRICE-DISCOVERY LEG ONLY.**

⛔⛔ **SCOPE, RESTATED BECAUSE THIS IS THE CELL SOMEONE ACTS ON: CORAL's OVERALL STATE STAYS 🟠 AND THE BANK-TRANSMISSION RAIL IS UNTOUCHED — NOT MET, NOT ARMED, in BOTH directions.** A supply-side leg standing down is **not** a Florida all-clear and is **not** evidence about bank transmission. Next bank re-test is still **Q3, ~late Oct**.

**⚠️⚠️ THE FINDING THAT MATTERS MORE THAN THE GRADE: the rule stood the leg down while its own underlying series moved the OTHER way.** Between the two readings **three of five metros ROSE**, **Lakeland re-crossed ABOVE the threshold** (5.97 → 6.01), and **Tampa printed the highest MSI in the whole series** (6.9 → 6.96 → 6.99 → 7.05 → 7.01 → **7.15**). Breadth fails on **Cape Coral alone, 0.09 under the line.** ⭐ **The 8/23 anti-noise leg guarded the TIME dimension and left the LEVEL dimension unguarded** — it was written to refuse a rounding-error de-fire and it has now produced one by a different route: a single metro a rounding-distance below 6.0 can hold the stand-down open indefinitely while the other four strengthen. **That is a rule defect, and it is Will's to rule on PROSPECTIVELY — CORAL proposes and does not self-apply, exactly as on 8/23 when the fire had no falsifier.** ⛔ **The defect does NOT change today's grade.** Re-fitting a rule at the grading table because the result is inconvenient is the precise failure the pre-registration exists to prevent, and the rule was written on 8/23 **before** the data turned.

**⛔ WHAT I AM NOT CLAIMING — inference audit (step 13a).** A rising MSI is **not** published here as "seller stress is intensifying." **RIVAL MECHANISM, same direction:** MSI can rise because the *remaining listing pool* is more distressed (composition) rather than because *more sellers* are motivated (breadth) — both push the index up, so **the index level cannot separate them.** ⭐ **The discriminator is UNIT VOLUME — active listing counts — and that is exactly what is no longer retrievable (OQ L).** So the MSI moves are published as **measured values only**, with the causal upgrade **explicitly declined**. This makes OQ L matter *more*, not less.

**2. ⚠️ INSTRUMENT INTEGRITY — the Parcl listings field got WORSE, not better, and in the way that evades review.** On 9/2 the per-metro active-listing count was **absent** from the server HTML (SEARCH-NOT-FOUND). On 9/13 it is **present and renders as a literal `0`** (`Total Active Listings · 0`) on **all five** metros — with **no backing numeric field anywhere in the payload** (verified: zero matches for any `*listing*` numeric key). **Tampa carried 26,801 active listings on 8/23; a true 0 is impossible.** ⇒ **It is a hydration placeholder, not a measurement.** ⛔ **DO NOT carry "0 listings" and do not let it satisfy a presence check** — a required field satisfied by a placeholder passes every presence audit while being pure fabrication downstream. **OQ L remains UNRESOLVED and is now higher-priority**, because it is also the discriminator the inference audit above just named. Price-cut share likewise absent (prose only, no number).

**3. Verification legs (detail → `STATUS_DETAIL.md`):** every MSI value read **three independent ways** — `<title>`, `og:description`, embedded JSON `"value"` — **all agree to the hundredth on all five metros.** Stamps read verbatim across an intervening HTML comment node (the naive grep returns an empty stamp — a silent false negative).

**4. STILL LIVE FROM 9/2, unchanged and not re-derived** *(full text → `STATUS_DETAIL.md`)*: **FMHPI excludes condominiums by construction**, so the "three statewide signs" conflict dissolved — it was a perimeter question. ⭐ **THE ONE FIGURE THE DESK PUBLISHES** *(binds per METRIC — FL house prices and FL condo prices are two metrics)*:
> **FL statewide single-family, constant-quality: `+1.68% YoY SA, July 2026` (FMHPI FL, Freddie issuer master file)** — **excludes condo/co-op/PUD; conforming conventional only.**
> **FL statewide condo/townhouse: `$295,000 median, 0.0% YoY, July 2026` (FL Realtors, PRIMARY), EXPLICITLY a mix statistic** — no constant-quality statewide FL condo index is in hand (OQ K).
> ⚠️ **The caveat that cuts at my own mechanism: FMHPI sees only conforming conventional financed sales while FL cash share was 51.0% in July** — structurally blind to the cash capitulation-clearing channel this desk says is doing the price discovery. **A rising FMHPI is not evidence against that read.**

## THESIS RAILS — "The Coral Bleaching"

Durable mechanism, confirm/falsify rails, timing gates, and ownership rules live in `thesis/THESIS.md` (v1.0). ⭐ **Refreshed 2026-08-23 (Will-approved) after 31 days stale: (a) the 🔴 MSI leg's Will-ruled STAND-DOWN rail is installed — it previously had a trigger and no falsifier; (b) the six falsify criteria were GRADED FOR THE FIRST TIME EVER — score 1.5 of 6 ⇒ HOLD 🟠, with a PRE-REGISTERED decision rule and a dated cadence (next grade 2026-11-15) so the score cannot be reverse-engineered from a print.** ⭐ The substantive read: the thesis split is not weakening, it is **SHARPENING** — the bank half keeps curing (criteria 1-2 moving toward falsification) while the household/collateral half does not (criteria 3-4 firmly against). ⚠️ **Criterion 5 (bankruptcy per-capita) graded UNGRADED — untracked since June; the instrument is OWED before 11/15 (OQ I).** STATUS carries current levels only: **household/condo stress confirmed; bank-loss transmission not confirmed until FL bank credit data prove the bridge.**

---

## SIGNAL DASHBOARD — HOT (state + level + vintage). ⭐ **Full evidence rows, sources, basis caveats → `STATUS_DETAIL.md`**

| Channel | Level (dated) | Status |
|---|---|---|
| **🟠 MSI supply-side leg** | **4-of-5 >6.0 (9/13)** — 2nd sub-threshold reading ⇒ **STOOD DOWN 🔴→🟠 on 9/13**, leg only. Cape Coral 5.91 alone under; Tampa **7.15** series high | 🟠 |
| FL foreclosure — H1 cumulative | #1 of 50, **0.27%** (ATTOM, 7/17). ⚠️ RANK ≠ level; 4 non-convertible bases | 🔴 |
| FL REO completions | FL Q1 **1,014, +108% YoY**; nat'l H1 +33% | 🟠 |
| Condo/TH median (**mix statistic**) | **$295K, 0.0% YoY (Jul)** — the flip did not hold | 🟠 |
| **FL statewide SF, constant-quality** | **+1.68% YoY SA (Jul, FMHPI FL)** — ⚠️ excludes condo/co-op/PUD, conforming only | 🟡 |
| SF median (**mix statistic**) | **$425K, +3.7% YoY (Jul)** — decelerating from +4.9% Jun | 🟡 |
| Condo inventory (statewide) | **7.8 mo (Jul)** — 4th straight tightening; CORAL-canonical | 🟡 |
| Condo inventory (metro) | Miami-Dade **12.0mo / 86 DOM (Jul)**; Broward 10.1 (Jun); ⚠️ **PB 8.2 still APR — STALE** | 🟠 |
| SE-FL vintage (30+yr) pending $/sf | **$313, −9%** — ⚠️ no fresher SE-FL-wide read since 7/13 | 🟠 |
| Special assessments | **$25K–$100K/unit typical, to $400K**; SIRS tail ≤12/31/26, funding-pause ≤12/31/28 | 🔴 |
| GSE warrantability channel | **PRIMARY-TIER.** Full Review live 8/3/26; binding FL constraint = **pass/fail inspection bullet** (no $ amount) + **>$50K/unit master deductible** | 🟠 |
| Termination / receivership | *Biscayne 21* 100%-consent STANDS; Two Roads "economic waste" suit **unresolved** | 🟡 |
| FL property-cat reinsurance | 6/1 **−15/−20% risk-adjusted**; Citizens net ROL **8.46% vs 11.95%** | 🟢 easing |
| Citizens policies in force | **278,196 (7/31 month-end)** — ⚠️ **six weeks flat, and the SIGN SPLIT is the finding: personal +138 (GREW), commercial −188 (−4.1%). Depopulation has STOPPED.** 8/31 month-end **owed, ~now** | 🟠 |
| Citizens commercial / condo-assoc | Commercial **+10.4% capped** eff 7/1/26 (⚠️ +18.8% uncapped un-re-confirmed — lean on capped) | 🟠 amplifier |
| Recent-vintage neg. equity | Cape Coral **11.1%** #1 US; Lakeland 10.8%; 2024 vintage **35.4%** underwater | 🟠 |
| Bankruptcy filings | FL ~**190/100k** vs nat'l ~168-173, **+22.2% YoY** — ⚠️ tripwire **instrument not built** (OQ I) | 🟠 canary |
| **Hurricane season 2026** | **5 named / ZERO hurricanes; NO FL landfall.** NHC 9/2 8PM: **no formation expected 7 days.** CSU remainder-of-season FL-Peninsula major landfall **7% (climo 21%)** | 🟡 |
| Sargassum (SE FL) | ~**38M MT** Jul outlook, record tier — ⚠️ NOAA SIR SE-FL band **still not retrievable** since 7/21 | 🟠 |

## WHOLE-FLORIDA PILLARS — detail → `COVERAGE.md`; evidence → `STATUS_DETAIL.md`

| Pillar | Read | Signal |
|---|---|---|
| **Migration (7)** | Net domestic **+22,517 (−93% from peak, #8)**; intl −57% YoY; natural change negative. *Demand engine failing.* (2025 Census annual, STALE-marked) | 🔴 |
| **Tourism/snowbird (8)** | Bifurcated: Orlando TDT record-June +10% YoY vs **Canadian −12.1%** + SW-FL capacity cuts | 🟠 |
| **Single-family (2)** | **$425K, +3.7% (Jul)**, 4.5mo supply — decelerating | 🟡 |
| **CRE (4)** | ⭐ **Cycle 2 landed 9/2 — the ZEROS, as asked: no FL asset named anywhere in the August Trepp print** (the one hotel named is New Orleans). National lodging DQ **5.35% → 5.84% (+49bp)** — ⛔ **CREED owns this figure and explicitly calls it NOT a signal (0.68σ against a 72bp mean |MoM|, noise floor pre-registered before the print); CORAL carries no second copy.** ⚠️ **🟡 — REASON REWRITTEN 9/2 (CREED cycle-1 evidence): the feed is LIVE but STRUCTURALLY THIN** — Trepp's monthly PDF class has **no geographic table at all**; FL content is **named-loan prose only, ~1 event per 2 months**. ⛔ **Do NOT revert to 🟢 on "the feed landed"** — the lane will not improve by waiting | 🟡 |
| **FL banks (6)** | Rail **NOT met, NOT armed**; Q2 closed **7-of-7 benign**, sync 0-of-≥2 | 🟡 |
| **State fiscal (9)** | **Amendment 3 / Nov 3** — biggest two-sided forward variable; ruling still unlocated (OQ E) | 🟠 |

## FL BANK EXPOSURE — full per-bank grid → `STATUS_DETAIL.md`; watchlist → `FL_BANK_WATCHLIST.md`

**UNCHANGED. Q2 window CLOSED 7-of-7 BENIGN, final sync 0-of-≥2 — empirically closed, not merely mathematically.** The sharpest pre-registered tell (SBCF nonaccrual 3rd rise >$95M) is **FALSIFIED** — nonaccrual reversed to $86.5M with the whole aging ladder falling together. Leading-bucket 10-Q detail **closed by REGINALD 8/10, 4-of-4 REVERT** (BKU Q1 CRE 30-89 $23.4M → $0) ⇒ **lumpiness confirmed; the creep does not broaden.** Across SSB/SBCF/VLY the same pattern: CRE criticized/classified rose on 2024-era rate-shock underwriting, but **LTVs and payment performance are intact → reclassification, not realized loss.** That is the crux of why the bank leg has not transmitted. **Zero HOA/condo/association/SIRS disclosure in any of the 7 releases = the wire is structurally unobservable.** ⚠️ Prices in the detail grid are **7/23–8/3 and MUST be re-pulled live before any citation** (root rule: never cite prices from STATUS). **Next re-test Q3 ~late Oct**; VLY CRE/RBC 329% is a Q1 figure, 10-Q pending.

---

## OPEN QUESTIONS / OWED ITEMS

**A. 🟠 [RULED 2026-08-23 — WILL, IN-SESSION, VERBATIM "accept" — CANONICAL LETTER LIVES HERE] · ✅ CONDITION MET 2026-09-13, LEG STOOD DOWN 🔴→🟠.** The supply-side price-discovery leg fired 7/23 on a Will-ratified breadth+sustain condition with **no falsifier ever registered**. That gap was closed on 8/23 — **and the falsifier it installed has now RESOLVED, in the direction of standing the leg down.** ⭐ **The letter below is kept VERBATIM as the grading surface it was; it is NOT reworded now that it has fired.** **This is the canonical text; `PROME/GATES.tsv` `GATE-CORAL-MSI-01` is a POINTER — on any disagreement, this surface wins and the GATES row is the copy to fix (PAT-006).**

> ### 🔴 MSI SUPPLY-SIDE LEG — REGISTERED STAND-DOWN CONDITION (Will-ruled 2026-08-23, adopted unamended)
> **Breadth <5-of-5 FL metros with Parcl MSI >6.0, on TWO CONSECUTIVE readings ≥10 DAYS APART ⇒ 🔴→🟠.**
>
> ⛔ **BOTH LEGS BIND — neither is decorative:**
> 1. **A single sub-threshold reading does NOT stand the leg down.** One reading below 5-of-5 changes nothing; it starts a clock, it does not ring a bell.
> 2. **Two readings closer than 10 days do NOT count as two.** The second reading must be **≥10 days after** the first sub-threshold reading. A pair taken 3 days apart is ONE observation for this purpose, however many times the pages are pulled.
>
> ⭐ **The spacing is the ANTI-NOISE leg and it is the load-bearing one.**
> **Scope, unchanged in both directions: the SUPPLY-SIDE PRICE-DISCOVERY LEG ONLY.** The bank-transmission rail and CORAL's overall 🟠 state are untouched whether this fires or stands down.
> **Symmetry note (why this form):** the leg FIRED on persistence (breadth sustained ~15d), so it stands down on persistence too. Any future amendment should move the spacing **toward more**, never less.

**✅ RESOLVED STATE — THE CLOCK RAN AND THE CONDITION WAS MET (2026-09-02 → 2026-09-13).**
- **Sub-threshold reading 1 of 2: 2026-09-02** (page vintage `Updated: 9/3/2026`) — **3-of-5 >6.0**; Cape Coral 5.95, Lakeland 5.97.
- **Sub-threshold reading 2 of 2: 2026-09-13** (page vintage `Updated: 9/13/2026`) — **4-of-5 >6.0**; **Cape Coral 5.91 the only metro under.** Spacing **11 days** observed / **10 days** by page vintage — **≥10 on both clocks.** No reading taken in between ⇒ **CONSECUTIVE.**
- **⇒ CONDITION MET. LEG STATE: 🟠 (stood down 2026-09-13 from 🔴).** ⛔ **Supply-side price-discovery leg ONLY** — CORAL overall **🟠 unchanged**, bank-transmission rail **NOT met, NOT armed, unchanged in both directions.**
- **The leg did NOT stand down because Florida improved.** It stood down because breadth is a **count**, and one metro (Cape Coral) sits **0.09** below 6.0 while the other four are above and three of five ROSE. ⭐ **Registered as a rule defect for Will to rule on PROSPECTIVELY** — the 8/23 letter guards SPACING but not LEVEL, so a single laggard can hold a stand-down open while the signal strengthens. ⛔ **CORAL proposes; CORAL does not self-apply, and did not re-fit the rule at the grading table.** → escalated to PROME 9/13 (OQ S).
- **Re-fire:** the 8/23 letter registers a stand-down and **no re-fire condition**. ⚠️ **That is the mirror of the gap closed on 8/23 and it is now the live one** — if breadth returns to 5-of-5 there is no registered rule to take the leg back to 🔴. **Named, not self-answered** (OQ S).

### OWED TABLE — every live obligation this desk carries (⭐ full reasoning, resolution paths and prior failed routes → `STATUS_DETAIL.md` § "OPEN QUESTIONS — full text")

| # | Owed item | Due / next observable | State |
|---|---|---|---|
| A | ✅ **MSI reading 2 of 2 — GRADED 9/13 on the frozen letter: 4-of-5 ⇒ leg STOOD DOWN 🔴→🟠** (leg only) | **DONE 2026-09-13** | ✅ closed |
| B | Miami discriminator — needs a **submarket-level concession cut**; coordinate HOMER | open | QUESTION, not a finding |
| C | FL hotel portfolio identity — **only path = CMBS deal-level remittance**; Trepp monthly ruled out structurally. ⚠️ **[TIGHTENED 9/2, CREED cycle 2] The July/August silence is NOT evidence the portfolio cured** — the narrative lists only the five largest **NEWLY** delinquent loans, so an asset that *stays* delinquent simply stops being mentioned. **August: zero Florida named anywhere** (the one hotel named is New Orleans) | open | search CLOSED, question open, **fate UNKNOWN** |
| D | Warrantability spread — earliest honest read; **+ count FL associations with >$50K/unit master deductible** | **~Oct–Nov** | not yet measurable |
| D2 | **SEL-2026-05 loosening — effective dates UNKNOWN** | open | flagged OPEN, not adopted |
| D3 | GSE gate 2: reserve funding **10% → 15%** | **2027-01-04** | dated |
| E | **Amendment 3 ruling — unlocated on 3 attempts.** ⛔ ML-CORAL-042 stays UNRESOLVED, score no branch. **Switch to COURT DOCKETS, not outlets** | ruling any time; **Nov 3** vote | 🔴 oldest un-worked |
| F | Ocala June-2026 metro UR — **next route FloridaCommerce LMS**; ⭐ normal June shape +0.6pp, so +0.5-0.6pp is NOT signal | owed | 3 routes dead |
| G | **Citizens 8/31 month-end** — base 278,196; ⭐ **watch the personal/commercial SPLIT, not the total** | **owed now** | 🟠 |
| H | **BUILD the bankruptcy instrument** — Ch.7 per capita M.D.+S.D. Fla, tripwire **>~230/100k**. ⛔ criterion 5 scores 0 again if unbuilt | **before 2026-11-15** | not built |
| I | Receivership/termination count — Two Roads "economic waste" suit | unresolved | 🟡 |
| J | **Condo price-band test — UNITS, never SHARE** (a share test confirms the thesis whether or not it is true) | separate report | not run |
| K | ⭐ **[NEW 9/2] No constant-quality statewide FL CONDO index exists at this desk** — every condo composition argument rests on a mix statistic. Paths: FHFA expanded-data HPI · Case-Shiller Miami condo · FL Realtors band cut | open | **new named gap** |
| L | ⭐ **Parcl sub-metrics — WORSE on 9/13: listings now render a literal `0` placeholder with no backing field.** ⛔ Never carry "0 listings." **Escalated: unit volume is the discriminator the MSI inference audit needs**, so this blocks any causal read of MSI. Routes: Parcl API · Realtor.com/Redfin metro inventory | **rolling, now higher-priority** | SEARCH-NOT-FOUND (never zero) |
| M | Falsify grade — ⛔ do not re-derive the rule, do not reword a criterion | **2026-11-15** | baseline 1.5 of 6 |
| N | Bank rail re-test | **Q3, ~late Oct** | NOT met, NOT armed |
| O | Stale rows owed refresh: **PB condo inventory (Apr)** · **SE-FL vintage $/sf (7/13)** · **blacklist count (Apr-2025)** · **NOAA SIR SE-FL sargassum band (since 7/21)** · **VLY CRE/RBC 329% is Q1, 10-Q pending** | rolling | STALE-marked in place |
| P | **NFIP authorization expires** | **2026-09-30** | dated cliff |
| Q | FL Realtors August — read **price and volume as separate legs** | **~2026-09-17** | dated |
| R | **Canadian counter-tariffs — CA$27.6B (CAD), THREE tiers 15/25/50%, NOT one blended rate**; FL lines = appliances, furniture, apparel retail, pulp & paper. ⛔ **Nothing fires for CORAL** — no CORAL letter names a tariff line. MARCO owns the tourism fold, HAWK the trade read | **2026-09-08** | cell corrected at primary 9/2 |
| S | ⭐ **[NEW 9/13] MSI rule defect + missing re-fire condition** — the 8/23 letter guards SPACING but not LEVEL (a single 0.09-under metro stood the leg down while 3 of 5 rose), and it registers **no re-fire condition** if breadth returns to 5-of-5. ⛔ **Will to rule PROSPECTIVELY; CORAL does not self-apply** | escalated to PROME 9/13 | 🔴 open governance gap |
| T | ⭐ **[NEW 9/13] Orange County / FL enrollment — no comparable-basis YoY exists.** Need the 2026-27 OCPS headcount file **or FLDOE Survey 2 (Oct membership)**. ⚠️ FLDOE + BoardDocs 403 on 9/13 = **SEARCH-BLOCKED, never absent.** ⛔ Enrollment cannot separate migration from voucher substitution — do not upgrade pillar 7 on it | **~Oct (FLDOE Survey 2)** | 🟠 press-tier only |


## FL ENROLLMENT — the one figure, for MARCO to reconcile against (SIG-W-20260911-002)

⛔ **THE ROUTED HEADLINE DOES NOT RECONCILE AT PRIMARY. CORAL DOES NOT PUBLISH IT AS A FACT.** WALTER routed *"Orange County FL schools −7,600 students YoY on ~191,000, district names housing affordability + immigration law."* **Primary verification run 9/13 at OCPS direct** (full table, URLs and clean negatives → `STATUS_DETAIL.md` § "2026-09-13 FL enrollment verification").

⭐ **THE ONE FIGURE CORAL PUBLISHES:** **OCPS district total enrollment `201,652` — headcount, vintage `2025-09-15`, source: OCPS "Enrollment Summary by School/Grade" PDF (PRIMARY).** Same series **`199,368` at 2026-05-15.** ⛔ **No 2026-27 file exists yet** (every 2026-27 filename probed returns 403 = absent), **so no comparable-basis YoY is available at all.**

⛔ **THREE INSTRUMENTS, NO SHARED BASIS — do not difference them.** (a) the **headcount** series above · (b) **FY27 Adopted Budget K-12 FTE `228,198, +0.82%`** (PRIMARY, adopted **2026-09-08**) · (c) the **−7,672** claim, off the district's **10-DAY COUNT** (~late Aug 2026), **press-tier, primary unpublished.** `201,652 − 7,672 = 193,980`, **not ~191,000**; 191,000 **exceeds** the traditional-only 180,282; **FTE ≠ headcount.**
⭐ **The sharper fiscal tell than the enrollment number: the FY27 budget was ADOPTED 2026-09-08 — AFTER the late-Aug 10-day count — and still carries a +0.82% INCREASE.** A budget projecting growth against an actual count below it is exactly what *"lost more than projected ⇒ $8.5M extra cuts"* looks like. **The narrative is coherent; the numbers are not comparable.**

⛔ **INFERENCE AUDIT — THIS DOES NOT MOVE PILLAR 7 (MIGRATION), AND THE REASON IS NOT THE SOURCING.** **Rival mechanism moving the statistic the SAME direction, named by the district itself: "expansion of taxpayer-funded vouchers."** A voucher-driven shift from public to private schooling produces a **public-school enrollment decline with ZERO net out-migration**; declining birth rates do the same. ⇒ **Public-school enrollment cannot separate migration from substitution.** Causes are published **unweighted**, and the causal quote is **in no district-published document reached — press-only.** **Pillar 7 UNCHANGED; no colour moves.**
⚠️ **Correction to WALTER:** the signal's limit says *"single local-TV outlet"* — **it is multi-outlet** (WKMG · Spectrum 13 · CF Public Media · FOX 35), all sourcing 7,672 to Supt. Vazquez's 10-day report. Still press, not primary.
**Resolution path → OQ T:** the 2026-27 OCPS headcount file (re-check after mid-Sep), or **FLDOE PK-12 Survey 2 (October membership)**, the canonical FL count. ⚠️ **FLDOE, EDStats and OCPS BoardDocs were ALL 403/unreachable 9/13 — SEARCH-BLOCKED, never absent.**

## FEEDS TO

- **PROME** — 🟠 **MSI reading #6 GRADED: 4-of-5 >6.0 ⇒ second consecutive sub-threshold reading ≥10d apart ⇒ GATE-CORAL-MSI-01 STANDS DOWN 🔴→🟠, supply-side price-discovery leg ONLY.** Stamps `Updated: 9/13/2026` verbatim ×5, HTTP 200 ×5, MSI triple-verified. ⛔ **CORAL overall 🟠 and the bank rail are UNTOUCHED in both directions.** 🔴 **Two governance items for Will (OQ S): (a) the rule stood the leg down while 3 of 5 metros ROSE and Tampa hit a series high — it guards spacing, not level; (b) there is NO registered RE-FIRE condition.** Both **prospective** — today was graded as written. **PROME owns GATES.tsv; CORAL edited no PROME file.**
- **HOMER** *(via PROME — HOMER dark)* — **FMHPI cannot bear on the FL condo question: the Freddie methodology excludes condominiums verbatim.** ⛔ **Vintage correction: the FMHPI-vs-median comparison used CORAL's JUNE median (+4.9%); the July figure is +3.7%** — like-for-like the gap is 2.0pp, not 3.2pp. On single-family the two statewide instruments **agree in sign**; there was never a three-way conflict.
- **REGINALD** — bank rail **UNCHANGED: NOT met, NOT armed.** Q2 closed 7-of-7 benign; your 8/10 leading-bucket close consumed as owner-read, not re-derived. ⚠️ **Upstream-of-the-bridge correction to my 9/2 send: the MSI stand-down CLOCK has now RESOLVED — the leg is 🟠, not 🔴.** ⛔ **Do not read that as FL supply stress easing** — breadth failed on one metro 0.09 under while Tampa printed a series high 7.15. **Nothing about bank transmission changed.** Next re-test Q3 ~late Oct.
- **CREED** — ✅ **§5 ask GRANTED: pillar 4 STAYS 🟡, reason rewritten to yours** — "feed live but structurally thin; no FL geographic layer; named-loan prose only, ~1 event per 2 months." **A 🟢 would have re-created the defect the flag was raised for.** Your −79bp noise caveat **adopted into OQ C**; it materially weakens what CORAL was carrying. **Send the empty months — the zeros are the cadence.**
- **RED** — ✅ **BOTH ROWS CONFIRMED, not superseded** (KB-RED-046 · KB-RED-052): the **~70/30** split and its **~winter** anchoring **STAND on summer data**, and the summer evidence pushed **toward the 70% leg**: Q2 closed 7-of-7 benign with the sharpest pre-registered tell falsified. **Re-date Stale_By to 2026-11-15** (CORAL's pre-registered falsify grade). cc DEWEY, same answer.
- **MARCO** — ✅ your 9/2 adoption of all four FL figures received, zero divergence. ⚠️ **UPDATE THE MSI CELL: you carry it as "reading 1 of a required 2, clock running, leg holds 🔴." Reading 2 landed 9/13 at 4-of-5 ⇒ the leg is now 🟠 (leg only).** ⭐ **FL enrollment (SIG-W-20260911-002) — my figure and its limits are in §"FL ENROLLMENT" below; reconcile to ONE number, and I do not assert your half.** ⛔ **Your VX-FL-02 single-family months-of-supply hole: I hold FL Realtors statewide SF 4.5 months (July 2026) — take it if the perimeter fits, it is a SUPPLY figure, not FMHPI.** Tourism/Canada fold stays yours.
- **CARL** — cost stack unchanged; **Citizens personal-lines depopulation has STOPPED** (+138 July) — the household relief that was easing has flattened. Hurricane tail still low.
- **AEOLUS** — **season 5 named / ZERO hurricanes, no FL landfall; NHC 9/2 8PM: no formation expected 7 days, at the ~9/10 peak.** Your soft-market asymmetry **hardens** — the CSU 7%/9% remainder-of-season tail is being run down by the calendar onto a −15/−30%-priced market. ENSO figure remains yours.
- **DAEDALUS** — ✅ **F-2 fix APPLIED 9/13: intl migration now stamped `+178,674 (2025 annual Census, components of change)`** with your arithmetic shown (−56.5% vs stated −57%) — **the two desks corroborate; never a conflict.** ⏳ **L4 declared-flat `TRADE.md` DEFERRED, not refused** — accepted that it is not Will-blocked.

## BOTTOM LINE

**The 🔴 supply-side price-discovery leg stood down to 🟠 today on its own pre-registered rule — and the reason it stood down is not the reason anyone would assume.** Breadth came in at **4-of-5 >6.0**, a second sub-threshold reading 11 days after the first, so the 8/23 Will-ratified condition was met and the leg went 🔴→🟠. ⛔ **The leg ONLY. CORAL stays 🟠 overall and the bank-transmission rail is untouched in both directions — NOT met, NOT armed.**

⭐ **But between the two readings the series moved the OTHER way.** Three of five metros ROSE, **Lakeland re-crossed back above 6.0**, and **Tampa printed the highest MSI in the entire series (7.15)**. Breadth failed on **Cape Coral alone, 0.09 under the line.** **A leg stood down on a strengthening signal because the rule counts metros and does not look at levels.** That is a real defect in a rule I wrote and Will ratified, and **it is registered for Will to rule on PROSPECTIVELY (OQ S) — not fixed at the grading table today.** Pre-registration is worth nothing if it is renegotiated the moment it returns an awkward answer, so today was graded exactly as written. The companion gap is sharper: **the letter registers a stand-down and NO re-fire condition** — the mirror of the exact hole closed on 8/23.

⚠️ **What I explicitly did NOT conclude.** A rising MSI is published as a **measured value, not as "seller stress is intensifying."** Composition (a more-distressed remaining listing pool) and breadth (more motivated sellers) push the index the same way, so **the index cannot separate them — the discriminator is unit volume.** And **unit volume is precisely what Parcl stopped serving**: the active-listing count now renders as a literal **`0`** with no backing field, which is a placeholder that **passes a presence audit while being fabrication downstream**. ⛔ **Never carry "0 listings."** That instrument gap (OQ L) is now load-bearing, because it blocks the causal read the grade invites.

**What did not move is still the thing that matters. Bank-loss transmission remains unconfirmed** — Q2 closed 7-of-7 benign, the sharpest pre-registered tell falsified, REGINALD's leading-bucket close 4-of-4 REVERT. **Household and collateral stress must still not be read as banks breaking**, and a supply-side leg standing down is **not** a Florida all-clear. Next bank re-test **Q3, ~late Oct**.

**Next:** **Citizens 8/31 month-end, owed NOW — watch the personal/commercial split** · **~9/17 FL Realtors August** (price and volume as separate legs) · **9/30 NFIP expiry + FIGA assessment ends + FL min wage $14→$15** · **~Oct–Nov warrantability friction** · **late Oct Q3 bank prints** · **Nov 3 Amendment 3**, still the biggest two-sided forward variable and the **oldest un-worked item** (E, unlocated on 3 attempts — switch to court dockets) · **Nov 15 pre-registered falsify grade**, with the **bankruptcy instrument (H) still unbuilt** and criterion 5 scoring 0 again if it stays that way.

*CORAL: tracking the bleaching of Florida's condo market. Evidence → `STATUS_DETAIL.md` · session history → `archive/STATUS_SESSIONS_20260721-20260823.md` · prior dashboard → `workbook/STATUS_archive_20260325.md`.*
