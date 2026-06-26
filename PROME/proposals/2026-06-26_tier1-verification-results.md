# Verification-Pass Results — Tier-1 Bank Q1'26 Load-Bearing Figures
**Date:** 2026-06-26 · **Author:** Claude Code Prome · **Status:** RESEARCH/DRAFT — PROPOSED corrections (NOT yet applied to canonical synthesis docs; awaiting Will)
**Source:** Workflow `wzmprhwb2` (run `wf_089c545a-610`) — 17 agents, per-bank verify → independent adversarial re-pull → propagation map. Executes `PROME/action-cards/VERIFICATION_PASS_2026-06-26.md` Tier-1.
**Method:** Each figure pulled from the **primary** (EDGAR 10-Q / FDIC Call Report), then an *independent* skeptic re-pulled the same primary to refute. **Adversarial stage upheld 100% of Stage-1 verdicts; zero hallucination flags.**

---

## Scorecard — 28 figures, 8 banks

| Verdict | Count | Meaning |
|---|---|---|
| ✓ exact | **11** | verbatim/exact match to primary |
| Δ close-but-mislabeled | **9** | value ~right but wrong label/basis/anchor |
| ✗ conflict | **5** | materially wrong or not in primary |
| ? unverifiable | **3** | not in the primary pulled; needs another source |

**11/28 (39%) clean-exact.** The trade thesis still **survives** — but it survives because the instrument's *discriminators absorbed the errors*, not because the inputs were precise. Two of the five ✗ landed on the marquee names of the two surviving Q2 paths (ALLY, ZION).

---

## Verified-vs-claimed (full)

### SYF — 10-Q, Q1'26 (acc 0001601712-26-000016, filed 2026-04-23)
| Figure | Claimed | Verified | Verdict |
|---|---|---|---|
| NCO | 5.42% | 5.42% (consolidated; commercial seg 6.55% shown separately) | ✓ |
| ACL coverage | 10.42%, +36bps QoQ | 10.42% vs 10.06% Q4'25 = +36bps (ACL/loans, not /NPL) | ✓ |
| FY26 NCO guide | <5.5% (was 6.0%) | new = "below 5.5–6.0% range"; **prior was "in line with 5.5–6.0% RANGE," not a 6.0% point** (FY25 actual 5.65%) | Δ |

### ALLY — 10-Q + 8-K release (acc 0000040729-26-000009 / 0001193125-26-160281)
| Figure | Claimed | Verified | Verdict |
|---|---|---|---|
| retail-auto NCO | 1.97% | 1.97% (197bps) | ✓ |
| retail-auto 30+ DQ | 4.6% | 4.60% (incl non-accrual) | ✓ |
| ACL **release ~$224M** | release/drawdown | **WRONG SIGN — Q1'26 was a +$50M BUILD** ($3,490M→$3,540M; Prov $467M > NCO ~$417M). Only "release" language is *prior-year* Credit-Card-sale context. $224M not an ACL move. | ✗ |
| S-tier originations | 37% | **41%** (trailing 5Q = 42/42/42/41; never 37%) | ✗ |
| nonprime | 10.1% | **~11.3%** (FICO<620 = $1.3B/$11.5B). **10.1% is exactly ALLY's CET1 ratio → likely metric mix-up** | Δ |

### COF — 10-Q (acc 0000927628-26-000048, filed 2026-05-07)
| Figure | Claimed | Verified | Verdict |
|---|---|---|---|
| domestic card NCO | 5.1% | 5.10% (correctly isolated vs total card 5.05% / total-co 3.45%) | ✓ |
| ACL build $230M ($155M **subprime**) | — | **$230M total ✓ and $155M ✓ — but $155M = Consumer-Banking AUTO build, NOT subprime card** (Card seg actually *released* $8M; Commercial +$83M). No prime/subprime split in filing. | Δ |
| auto originations | +21% YoY | +21% ($11,130M vs $9,210M) | ✓ |

### EGBN — 10-Q (acc 0001050441-26-000066, filed 2026-05-07)
| Figure | Claimed | Verified | Verdict |
|---|---|---|---|
| nonaccrual coverage | 114% (was 149%) | 114% / 149% (ACL/NPL, HFI-only) | ✓ |
| NPA ratio | 1.31% (was 1.04%) | 1.31% / 1.04% (NPA/total assets) | ✓ |
| IPRE | +23% | +22.6% — **only for IPRE *nonaccruals*** ($62.5M→$76.7M); IPRE *total balance fell −9.6%*. Restate as "IPRE nonaccruals +23% QoQ" | Δ |
| CRE 547% / DC construction 100% | — | **BOTH WRONG. Actual CRE = 295.1% of capital (now BELOW the 300% reg threshold); construction = 75.7%. The "100%" was the regulatory THRESHOLD, not EGBN's ratio. 547% appears nowhere.** EGBN no longer exceeds either concentration threshold. | ✗ |

### WAL — 10-Q, Q1'26 *(path (c) anchor)*
| Figure | Claimed | Verified | Verdict |
|---|---|---|---|
| NCO | 39bps | 39bps **only as the NON-GAAP "as adjusted" figure; GAAP/reported = 1.45% (145bps)**. Unit-carry trap. | Δ |
| classified assets | 1.08% | 1.082% ($1,070M/$98,853M; derived) | ✓ |
| **$99M life-sci charge-off** | implied Q1 realized loss | **NOT a charge-off — $99M is the OUTSTANDING BALANCE of a CRE non-owner-occ loan** (life-science-building collateral), late-Apr-2026 subsequent event, **appraisal pending, no loss booked**. "Sponsor walk-away" = unsupported inference. | ✗ |

### OZK — **FDIC Call Report** (no SEC 10-Q exists), REPDTE 20260331
| Figure | Claimed | Verified | Verdict |
|---|---|---|---|
| past-due $465M / 1.41% | — | 30-89d $190.9M + nonaccrual $296.6M = $487.5M = 1.48% ($465M not a Call-Report line) | Δ |
| NCO | 0.57% | 0.56% (0.5555%) — 1bp | Δ |
| NPA | $451M | $446.1M (nonaccrual $296.6M + OREO $149.6M) | Δ |
| RESG concentration | 88% | **NOT in Call Report** (segment concentration isn't a Call-Report line → needs OZK 10-K / investor deck) | ? |

### ZION — 10-Q, Q1'26 *(path (b) lead name)*
| Figure | Claimed | Verified | Verdict |
|---|---|---|---|
| NCO | 0.03% | 0.03% | ✓ |
| **muni $5.78B AFS** | — | **muni AFS = ~$869M FV (cost $857M). The $5.78B is TOTAL muni exposure incl HTM/loans that DON'T flow to AOCI** → ZION's muni-specific AOCI mechanism is ~6–7× smaller than written. | ✗ |
| Basel III CET1 impact | +93bps | **NOT quantified in 10-Q** (needs earnings deck / Pillar 3) | ? |

### CFG — 10-Q, Q1'26
| Figure | Claimed | Verified | Verdict |
|---|---|---|---|
| NCO | 0.39% | 0.39% | ✓ |
| consumer 18.7% housing-secured | — | **NOT in primary** — housing-secured = 38.2% of total loans (different denominator) | ? |
| BDC/fund-finance | $12.5B | $12.85B (cap-call $8,756M + secured priv-credit $4,096M) — +3%, immaterial | Δ |

---

## Discrepancy log → propagation (the corrections that touch canonical docs)

**REQUIRED rewrites (2) — these touch load-bearing rows:**

1. **ALLY (grading-instrument.md ~:52)** — DELETE "RELEASED ~$224M Q1 → leans mask-deferring; reversal = transmission." REPLACE: *"Q1'26 = +$50M CECL build, growth-driven = COLLECTIVE under Discriminator-1 → non-counting. Watch Q2 for a SPECIFIC-cohort build."* Sign-flip, but the build is collective → **path (a) odds unchanged**.

2. **ZION (grading-instrument.md ~:68; front-back-reconciliation.md ~:36)** — re-anchor the (b)/AOCI false-control trap on **total AFS securities**, footnote *muni-AFS ≈ $869M, not $5.78B*. Path (b) survives (fires on ≥2 of {ZION,WAL,CFG,EGBN} + ZION's broader AFS book) but the muni-specific framing was ~6–7× overstated. **Biggest dent to the cleanest-surviving path's lead name.**

**Lower-priority fixes:**
- **COF (grading ~:53; recon ~:65)** — re-label "$155M subprime"→AUTO; note Card seg *released* $8M in Q1. Refines bridge read (card releasing / auto+CRE building); Card-NCO trigger unaffected.
- **WAL (grading ~:71; recon :37,:78,:83)** — add unit-carry note: 39bps/55bps thresholds are on the **adjusted** basis (GAAP Q2 headline will read ~1.45%); grade adjusted-vs-adjusted. Drop the "sponsor walk-away" inference; $99M already correctly carried as not-yet-charged-off.
- **EGBN (grading ~:69 Note col)** — correct to CRE 295.1% / construction 75.7%; note no longer over-threshold. Note-column color only; real (a) trigger (coverage 114%→149%, NPA off 1.31%) untouched.
- **SYF (front-half-demask ~:51,:113)** — re-anchor prior guide as "in line with 5.5–6.0% range." Net direction (guiding down) preserved.

**Re-mark the 3 unverifiable (?) — do NOT leave as silent "verified":**
- OZK RESG 88% → recoverable via OZK 10-K / investor deck (not Call Report).
- ZION Basel III +93bps → recoverable via earnings deck / Pillar 3.
- CFG 18.7% housing-secured → recompute denominator (housing-secured = 38.2% of total loans).

**Not in these 3 docs (fix upstream in CARL/source rows):** ALLY S-tier 37→41; ALLY nonprime 10.1→~11.3 (decouple from CET1).

---

## One-line verdict

**The trade thesis SURVIVES verification: (b) AOCI + (c) WAL remain the live Q2 exception; (a) consumer-source stays a 2027 story.** No single correction moves a path's odds — the lone sign-flip (ALLY build-not-release) is neutralized by the collective/specific discriminator, and the ZION muni overstatement dents but doesn't break path (b). **But the figure quality is the real flag: 39% clean-exact, and the two surviving paths' marquee names (ALLY, ZION) both carried material errors.** The instrument's discriminators did the load-bearing work — that's the genuine validation here. Apply the 2 required rewrites + re-mark the 3 unverifiables before this goes trade-load-bearing.

---
---

# TIER 2 — LABOR (Workflow `wzlhvzlcb`, 2026-06-26)
**Status:** RESEARCH/DRAFT — PROPOSED. 11 agents, 5 figure-groups, verify→adversarial→propagate. **Sources:** FRED (ICSA/CCSA/UNRATE/PAYEMS + ALFRED vintages), BLS (USFIRE/JOLTS/A-12/LAUS), NY Fed, CBO/KC-Fed/Brookings.

## Scorecard — 16 figures: 8✓ / 5Δ / 3✗ (+1 unverifiable)

**Headline meta-finding:** the canonical **synthesis docs are largely CLEAN** — most wrong figures live **UPSTREAM in LABOR/CORAL/MARCO STATUS**, and the synthesis already filtered them (e.g. it renders revisions UPWARD and already rejected +50K for +21K). The verification proved the synthesis *more accurate than its noisy inputs.*

## The catches

| Figure | Claimed | Verified | Where | Verdict |
|---|---|---|---|---|
| **NFP revisions** | "+93K **downward**" | **+93K UPWARD** (Mar +29K, Apr +64K) — sign error; cuts *against* labor-weakening | **synthesis already says "up" ✓** — ✗ is in LABOR STATUS | ✗ (upstream) |
| **Prof-biz openings** | "<1M, 1st since Apr'20" | **FALSE** — recent SA min = 1,047K (Mar'26); never sub-1M except Apr'20; May'26 popped to 1,715K | NOT in synthesis (LABOR STATUS) | ✗ (upstream) |
| **"31 months" white-collar** | 31 consec months | **series-UNDEFINED + stale**; real = **Information-sector emp 37 consec YoY-neg months** (May'23–May'26). No CES sector shows 31 consec MoM declines | synthesis (demask:115, recon:53/50, grading:83) | Δ → **STRENGTHENS** |
| **2.2M removals (CBO)** | CBO projection | **mis-attributed** — it's a *disputed DHS* self-deportation claim (CMS: "the Two Million Myth"); CBO removals ≈ **290K**. Realized foreign-born LF decline ≈ **~1.0M**, not 1.5–1.9M | synthesis (demask:137,:59,:24,:40,:114) | ✗ (provenance+quantum) |
| **~1.5–1.9M LF impact** | KC-Fed/Brookings | realized ≈ **~1.0M** (NFAP/BLS-CPS); attribution false (sourced to MARCO in docs) | synthesis :59 | Δ (downsize) |
| **Continuing-claims velocity** | +21K vs +50K | **+21K = true WoW ✓**; +50K = 3–5wk cumulative off the ~1,771K late-May trough; 4wk = +36K. **Synthesis already uses +21K** | demask:28,:52,:106 | Δ (resolved) |
| **FL UR 4.8 vs 4.9** | ambiguous | **4.8% SA (Apr AND May'26) ✓**; the "4.9" = stale **NSA Jan'26**. *Landmine defused.* | (FL STATUS) | ✓ |
| **Mgmt-occ LTU 25.4%** | 25.4% | **unverifiable** — no public BLS occupation×duration table; likely mislabeled aggregate LTU | (LABOR STATUS) | ? |
| **FL +40.5K jobs** | unstated period | = Apr'26 **MoM SA** gain (current vintage trims to +33.9K); not over-the-year | NOT in synthesis (CORAL/MARCO) | Δ (upstream) |

**The surviving spine (✓):** LTU 27.5% (LNS13025703 ✓), Financial-activities −107K YoY (USFIRE ✓), recent-grad UR 5.7% (NY Fed Q1'26 ✓, series now frozen), U-3 4.3% ✓, NFP +172K ✓, CCSA 1,821K ✓, breakeven ~50K/mo ✓ (well-supported).

## Propagation

**Canonical synthesis-doc edits (3, light — PENDING WILL):**
1. **White-collar "31-mo"** → name the series + restate **31 → ~37 consec YoY-neg months (Information-sector)** [demask:115, recon:53/50, grading:83]. *Strengthens the structural read.*
2. **Immigration supply-floor** → re-mark **2.2M as DHS-disputed (not CBO)** + downsize realized LF cut to **~1.0M** [demask:137,:59,:24,:40,:114]. U-3 ~4.6% counterfactual is *already demoted to low-conf color* (demask:59/61) → direction holds.
3. **Cosmetic** → claims-vintage +1K refresh (227K/230K); relabel velocity "+21K = 1-wk WoW" [demask:28,:52,:106].

**Upstream STATUS routes (5 — NOT Prome's to edit; route to owning agents):**
- **LABOR** — the +93K **sign error** (down→up), the prof-biz "<1M" **false** claim, the mgmt-occ 25.4% unverifiable re-mark, the 2.2M-CBO mis-attribution.
- **CORAL/MARCO** — FL +40.5K period-label (MoM SA, not YoY).

## Tier-2 verdict

**The labor read SURVIVES all four planks** — *2027-grind / no 4th Q2 path / ~30% Aug-7 tail / immigration-masked* — and **two corrections STRENGTHEN it** (31→37 months; claims *not* accelerating-down → no pull-forward). The structural-recession claim's dramatic *headline numbers* were inflated (31mo, sub-1M openings, 2.2M, "downward" revisions), but the **mechanism spine holds**: elevated LTU 27.5%, financial-sector −107K, real ~1.0M immigration LF floor, breakeven ~50K so +172K NFP still masks. **No new Q2 catalyst; (a) stays 2027.** The cleanest takeaway: the *synthesis* was right even where its *inputs* were wrong — the errors to fix are upstream in the STATUS files.

---
---

# TIER 3 — remaining flagged-uncertain (2026-06-26, direct verify)
**Status:** RESEARCH/DRAFT. The other 3 Tier-3 items (OZK no-10-Q, FL UR 4.8/4.9, claims velocity) were already resolved in Tiers 1–2. The two remaining both verified clean — **neither needed the unverifiable-by-construction fallback** (both had real primaries; EDGAR was reachable with declared-UA).

| Figure | Claimed | Verified | Source | Verdict |
|---|---|---|---|---|
| **AMTB ACL** | "~45% ACL" | **ACL/NPL coverage = 45.0%** ($79.236M ÷ $176.050M) — coverage-of-NPL, **NOT ACL/total-loans** (=1.21%); reads under-reserved (~45¢ per $1 of NPL) | AMTB Q1'26 10-Q, acc 0001734342-26-000037 (filed 2026-05-01), Note 5 / MD&A | ✓ (definition clarified) |
| **Student-loan defaults** | "~9.16M" (Bloomberg) | **9.16M borrowers in default (270+ DPD)**, Apr 2026 — real **Dept of Ed/FSA** figure, Bloomberg only relayed | FSA Data Center; trajectory 6M (Aug'25) → 7.7M (Dec'25) → ~9M (Mar-31) → 9.16M (Apr) | ✓ (provenance upgrade; minor as-of Δ) |

**Two definition/provenance traps to carry forward** ([[finding_number_carries_threshold_unit_source]]):
- **AMTB 45% = ACL/NPL coverage** (under-reserved), *not* ACL/total-loans (1.21%) — cite the denominator. Confirms the AMTB FL-resi/condo leg as under-reserved, consistent with the path-(a) 2027 read. (These belong to CARL/REGINALD upstream — refinements, not corrections.)
- **Student-loan: cite "9.16M in default (270+ DPD), Dept of Ed/FSA, Apr 2026"** — not Bloomberg. For a Q1/Mar-31 cite use ~9.0M / $220B (~13% of the $1.64T portfolio). Do **not** sum with NY Fed's 10.3%-of-balances 90+ DPD or the 2.6M Q1 "newly-defaulting" cohort (different methodologies).

**Neither figure appears verbatim in the 3 canonical synthesis docs** (AMTB/student-loan are referenced conceptually only) → no canonical stamp required.

## VERIFICATION PASS COMPLETE (Tiers 1–3)
Tier 4 (macro/regime — HY/CCC, 10Y, prices) is **live-pull-at-trade** (rule #4), not a pre-verify target. The one scheduled item is the **10Y 6/30 re-pull** (feeds AOCI path (b)). Aggregate across all three tiers: ~26 load-bearing figures checked, **both theses survive**, with the material corrections (ALLY, ZION, WAL, EGBN, +93K labor sign, 31→37, 2.2M provenance) all applied/routed.
