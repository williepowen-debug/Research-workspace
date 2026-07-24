# Funding-seizure gate CALIBRATION — episode generalization + false-positive rate
**Date:** 2026-07-16 | **Mode:** Thesis | **Confidence:** High (both episodes + FP rate, DEWEY-pulled primaries) / Medium (the archetype taxonomy itself)

**Flag:** PROME prompt **07b** (Will-approved 7/9) · **Parent:** `output/2026-07-09_funding-seizure-x1-gate.md` — closes its two declared gaps; does **not** re-litigate its verdict.
**Deliver-by:** ~7/16 ✅ **on time**
**Engines:** DEWEY primary pull (FRED series construction + FP census) + 2 targeted episode agents (adversarially tasked to *refute*) + 3 salvaged sub-agents. **No `/deep-research` fan-out — sized down per *Engine sizing*** (2 interpretive legs, not a breadth problem).

---

## Key Finding

**The gate does NOT generalize. It is SCOPED to funding-origin (dealer-collateral/repo) seizures — and both tested episodes failed it, in opposite directions.**

The parent report derived the gate from two **funding-origin** episodes (Sep-2019 repo, Oct-2022 LDI), where plumbing broke first and credit lagged. Neither Mar-2020 nor Mar-2023 is that archetype, and **in both, the gate's conjunction never satisfies**:

- **Mar-2020 (exogenous-shock-origin):** **credit LED funding by ~17 business days.** The hypothesis that they broke *simultaneously* is **refuted — in the direction worse for the gate.**
- **Mar-2023 (deposit-run-origin):** the acute leg peaked at **+7bps** (vs +690 in Sep-2019) and **never reached +20**; the slow leg never moved. Meanwhile **HY OAS widened +125bps.** The gate is not merely blind here — **it is anti-correlated**: the policy response *injects* reserves, so the harder authorities fight a deposit run, the calmer the gate reads.

**The FP calibration is usable, and the apparent FP/FN trade-off DISSOLVES once the gate is scoped** (§3). **Recommendation: keep the gate, scope it explicitly to funding-origin, and put an archetype discriminator upstream of it** (§4).

---

## 1. The episode matrix (the deliverable)

| Episode | Archetype | Acute leg peak (SOFR99−IORB) | Slow leg (EFFR−IORB) | Credit | **Gate verdict** |
|---|---|---|---|---|---|
| **Sep-2019** repo | **funding-origin** | **+690bps** | fired (reserve scarcity, 15-18mo lead) | never repriced | ✅ **WORKS** *(derivation case)* |
| **Oct-2022** UK LDI | **collateral-origin** | n/a (UK) | n/a | gilt +140bps/3d, ~half reversed | ✅ **WORKS** *(analog)* |
| **Mar-2020** COVID | **exogenous-shock-origin** | +190bps (**Mar 16**) | ❌ **never fired** — reserves AMPLE and **RISING** | **LED, from Feb 21** | ❌ **conjunction NEVER fires**; acute-alone fires **late** |
| **Mar-2023** SVB | **deposit-run-origin** | **+7bps** (never hit +20) | ❌ **never fired** (pinned −7/−8) | **HY +125bps from Mar 9** | ❌ **never fires; anti-correlated** |

### 1a. Mar-2020 — credit led funding by ~17 business days *(hypothesis REFUTED, worse than proposed)*

**The sequence** [PRIMARY: FRED SOFR/SOFR99/EFFR/IOER/DBAA/DAAA/DGS10/TEDRATE/WRESBAL, DEWEY-pulled 7/16]:

| Date | Credit (Baa−10Y) | Funding | Note |
|---|---|---|---|
| **Feb 21** | **205→209bps — repricing STARTS** | **FLAT** (SOFR−IOER −2bps, EFFR−IOER −2bps, TED 15bps) | FSB dates "flight to safety" from here |
| Feb 24-28 | 213→**238bps** (+33 vs Feb 20) | **still flat** | credit moving alone |
| **Mar 3** | — | **first tremor** (TED 15→38bps) | **credit led by ~7 business days** |
| Mar 13 | **330bps** (+125 vs Feb 20) | SOFR99−IOER +32bps | |
| **Mar 16** | — | **ACUTE LEG FIRES: +190bps** | **credit led by ~17 business days (24 calendar)** |
| Mar 20-23 | **peak 423→431bps** | — | |

**★ UPGRADED TO THE ACTUAL X1 TRIGGER SERIES (post-drafting).** The above ran on a **Baa−10Y proxy** because HY OAS was unreachable (FRED's ICE truncation). The `fred_pull.py --splice` helper **built later the same session** (Will-greenlit build-pass) closed that gap. Actual **ICE BofA HY OAS** [PRIMARY: Ice Data Indices via archived FRED, DEWEY-pulled]:

| Date | HY OAS | vs Feb-20 | Note |
|---|---|---|---|
| **2020-02-20** | **362bps** | — | base |
| **2020-02-21** | **366** | +4 | **credit starts moving — matches FSB's Feb-21 "flight to safety" date exactly** |
| 2020-02-28 | 504 | +142 | funding still flat |
| **2020-03-09** | **668** | **+306** | **credit already +306bps — acute leg has NOT fired** |
| **2020-03-16** | **838** | **+476** | **← the acute leg fires HERE (+190bps SOFR99−IOER)** |
| **2020-03-23** | **1087** | **+725** | peak |

**→ By the time the acute leg printed, HY OAS had already completed 66% of its eventual +725bps move** — *worse* than the proxy's 59%, and this is **the series X1 actually triggers on.** The gate is a lagging indicator in this archetype, and the upgrade **strengthens the finding** rather than softening it. *(Baa−10Y retained above as independent corroboration — two different credit measures, same verdict.)*

**The refutation attempt failed — and its failure strengthens the finding.** The obvious objection: late-Feb Baa−10Y widening is a *Treasury-rally* artifact, not credit deterioration. Decomposition kills it: DGS10 fell **−46bps** while DBAA fell only **−12bps** → **corporates underperformed the safe asset by 34bps.** Genuine credit underperformance. *(The same caveat runs the other way on TED — partly bill-richening — which makes funding look* less *stressed early, widening the credit lead.)*

**Leg (b) is fatal.** Reserves were **ample and RISING** throughout [PRIMARY: FRED WRESBAL]: $1.626T (Feb 26) → $1.699T (Mar 4) → $1.745T (Mar 11) → $1.896T (Mar 18) — post-Sep-2019 bill purchases had rebuilt them off the $1.394T trough. EFFR−IOER sat at **−2bps flat through February** and only went +15bps **Mar 16-18** — *coincident*, not leading, and **confounded** by the Mar 15 emergency cut (EFFR pinned at the top of the new 0-0.25% range is partly transition mechanics, not scarcity).

**→ The conjunction never satisfies in Mar-2020.** Even relaxed to the acute leg alone, it fires **Mar 16-17** — *after* the Mar 15 cut, *one day before* CPFF/MMLF, ~5 business days before the Mar 23 bottom.

**Mechanism:** Vissing-Jorgensen [ACADEMIC: BIS WP966] establishes the Mar 9-18 Treasury spike was **not** a Treasury-fundamentals or illiquidity event but a **negative demand shock from forced sellers** (foreigners $287B, mutual funds $266B, households/HFs $196B, 2020Q1). **Funding was the consequence; credit was the cause.** The gate has the causal arrow backwards here.

### 1b. Mar-2023 — the gate is ANTI-CORRELATED with deposit runs

**Funding: genuinely calm** [PRIMARY: FRED, DEWEY-pulled]:

| Date | SOFR99−IORB | Event |
|---|---|---|
| Mar 8 | **−3bps** | AFS sale announced |
| Mar 9 | **−3bps** | the $42B run day |
| Mar 10 | **−4bps** | SVB fails |
| Mar 15 | **+7bps** | crisis-week peak |
| Mar 31 | +10bps | **quarter-end artifact, not the crisis** |

**EFFR−IORB pinned at −7/−8bps for the entire month** — the slow leg never moved. **Mar-2023 does not rank in the top 12 firings since 2018.** Ranked: Sep-2019 **+690** · Mar-2020 **+190** · **Mar-2023 +7**. The gate is calibrated to a phenomenon ~**70-100× larger** than anything SVB produced.

**⚠️ Credit DID reprice — correcting an intermediate finding.** An IG-based proxy (Baa−Aaa, +8bps) initially suggested "nothing repriced." **That proxy is wrong for this question.** The actual ICE BofA **HY OAS** [PRIMARY: Ice Data Indices via archived FRED, **DEWEY-verified independently**]:

| Date | HY OAS | Δ | Anchor |
|---|---|---|---|
| **Mar 6** | **397bps** | — | **trough — tightening INTO the crisis week** |
| Mar 8 | 409 | +11 | AFS sale |
| **Mar 9** | **427** | **+18** | **the run — credit moving WITH it, not after** |
| Mar 10 | 461 | +34 | failure |
| **Mar 13** | **503** | **+42** | largest single day (first session post-failure) |
| **Mar 24** | **522** | — | **peak = +125bps off the Mar 6 trough** |

IG OAS peaked **164bps (Mar 15)** — modest. **Both are true: IG barely moved; HY moved +125bps.** The error was calling "credit" what was only IG. **`[[finding_composition_mask_unmask_discriminator]]` — an IG proxy masks an HY move, and X1's trigger is HY.**

**→ In Mar-2023 credit repriced +125bps while funding never moved.** The exact REVERSE of Sep-2019.

**The mechanism is the durable finding.** The gate presumes *stress ⇒ reserve scarcity ⇒ repo bid above IORB*. In Mar-2023 causality ran **backwards**: the stress was bank solvency/deposit flight, and the response **injected** reserves — Fed assets **+$297B in one week** ($8,342B→$8,639B), reserves **+$252B** ($2,999.7B→$3,251.5B), primary credit **$4,581M→$152,853M (33×**, exceeding the Oct-2008 record of $110,737M**)**, BTFP $0→$11.9B→$53.7B, FDIC bridge lending $142.8B. **Repo was calm *because* the response flooded the very channel the gate monitors. The harder authorities fight a deposit run, the calmer the gate reads.**

---

## 2. Answering the prompt's gap (1) precisely

> *"…did funding microstructure lead credit in those episodes too? Or do deposit-run episodes fire the credit leg FIRST (which would mean the gate protects only the repo channel — a scoped, not general, pre-emption)?"*

**Answer: the second — and more strongly than the prompt's framing anticipated.**

- **Mar-2023 (deposit-run):** credit fired **and funding never did at all.** Not "credit first, funding later" — **funding never followed.**
- **Mar-2020 (shock):** credit led by 17 business days, and the conjunction **never satisfied** because reserves were ample and rising.

**→ The gate protects ONLY the repo/dealer-collateral channel. It is a scoped pre-emption, not a general one.** Both non-repo archetypes defeat it, by different routes.

---

## 3. Gap (2) — the false-positive rate, and why the SVB "miss" is not a miss

> ⚠️ **CORRECTED 2026-07-24 — the fire-COUNT column below and the "~20% FP" are WRONG; see the [Correction addendum](#correction-addendum-2026-07-24--fp-census-fire-counts) at the end. The mechanism verdict (funding-scoped gate; Mar-2020/Mar-2023 fail the conjunction) is UNAFFECTED — only this FP census is.** Short version: the raw fire-DAY counts are **532 / 133 / 48** (+10/+20/+30), not 83/52/26 (DEWEY re-pulled 7/24; matches LIQUID's `fp_backtest_079.py` exactly); and the "~20% FP" was **day-weighted** — the honest episode-level FP is **~62%** (calendar filter alone) → **~25%** only with LIQUID's persistence leg (KB-LIQ-087).

**Census, 2018-04-03 → 2026-07-15** (SOFR's true start; DEWEY-constructed from FRED, IORB spliced to IOER at the **2021-07-28/29 seam**, level continuous at 0.15%):

| Threshold | Fires | TP | FP | **FP rate** | FP calendar-flagged | FP non-calendar |
|---|---|---|---|---|---|---|
| +10 bps | 83 | 5 | 78 | **94%** | 46 | 32 |
| +20 bps | 52 | 9 | 43 | **83%** | 26 | 17 |
| **+30 bps** | **26** | **8** | **18** | **69%** | **16** | **2** |

**★ The usable spec: at +30bps, 16 of 18 false positives are calendar artifacts.** A quarter/month-end filter (±2 business days of quarter-end, month-end, Apr-15) leaves **2 non-calendar FPs against 8 TPs → FP rate collapses ~69% → ~20%.**

**★ The FP/FN trade-off DISSOLVES under scoping — this is the key synthesis.** A naive read says "+20/+30 misses SVB entirely (peak 10bps, 1 day) — a false-negative cost." **That is wrong.** SVB was **never a funding seizure**: repo was calm, and the gate is scoped to funding-origin. **Not firing on SVB is CORRECT behavior, not a miss.** Mar-2023 should be **struck from the TP list** for this gate. *(Arithmetically consistent: SVB never reached +20, so the 8 TPs at +30 are Sep-2019/Mar-2020 events only.)*

**→ Answer to "mechanical or human-confirm?": MECHANICAL is defensible at +30bps AND non-calendar** — *provided* the archetype discriminator (§4) sits upstream. Without it, mechanical firing is unsafe: the gate would sit silent through a Mar-2020 or Mar-2023 while the actual repricing happened elsewhere, and silence would read as "no stress."

⚠️ **Caveats that bound the census:**
1. **The +10bps threshold is structurally unusable** — contiguous-run counting yields a **214-day "single event"** (2019-02-07→2019-12-16) that swallows Sep-2019 whole. The 94% FP rate is, if anything, *understated*.
2. **TP attribution is window-based** (Sep 1-Oct 31 2019; Mar 1-Apr 15 2020; Mar 8-Apr 15 2023) → TP counts are **event** counts, not crisis counts (3 crises).
3. **2020-08 → 2023-03 is a total dead zone** (zero fires at any threshold — ZIRP + $2T RRP buffer). **FP rates are regime-dependent and do not transfer across regimes.**
4. **Pre-2018 is NOT constructible** — SOFR/SOFR99 begin 2018-04-03; `RRPONTSYAWARD` is an administered award rate, not a market GC distribution, and cannot substitute. **The prompt's "since 2015" is unanswerable; scoped to Apr-2018+ and stated, not fudged.**
5. Calendar flags do **not** include FOMC dates, Treasury settlement, or GSE paydowns.

---

## 4. Recommendation → LIQUID / HENRY / PROME

**Keep the gate. Scope it. Put a discriminator upstream.**

**(a) ARCHETYPE DISCRIMINATOR (new — the load-bearing addition).** Before asking "did the gate fire?", ask **what kind of stress is this?**

| Archetype | Origin | Does the gate apply? | The right leading observable |
|---|---|---|---|
| **Funding-origin** (Sep-2019, LDI) | plumbing/collateral | ✅ **YES — this is its scope** | SOFR99−IORB +30 non-calendar + slow leads + dispersion |
| **Deposit-run** (Mar-2023) | bank solvency / deposit flight | ❌ **NO — anti-correlated** | **DGS2 3-day move** (−102bps at Mar 13 = largest since Oct-1987, daily+free, fired while repo sat −10bps); **H.4.1 primary credit** (33× spike, weekly/confirmatory); H.8 small-vs-large deposit split (−$149.3B / +$53.5B, ~9d lag, diagnostic) |
| **Exogenous-shock** (Mar-2020) | outside → risk assets → forced deleveraging | ❌ **NO — credit leads by ~17 business days** | **credit itself is the leading indicator**; no funding pre-emption is available *(the honest answer)* |

**(b) SCOPED GATE SPEC (funding-origin only):** acute **SOFR99−IORB ≥ +30bps AND non-calendar** *(FP ~20%)* **AND** slow reserve-scarcity leads (EFFR−IORB, above-IORB borrowing, reserve-demand slope) **AND** the single-name/dispersion leg. **Mechanical firing is defensible at this spec** — with the discriminator upstream.

**(c) What this does NOT buy — state plainly.** The gate gives **no pre-emption in 2 of the 4 archetypes.** For shock-origin, credit *is* the early signal — X1 works fine there and needs no gate. For deposit-runs, watch the **2-year**, not repo. **The parent's verdict stands for repo/collateral seizures and is now bounded: X1 needs the gate, but the gate is not a general-purpose stress alarm, and its silence is not evidence of calm.**

**(d) `GATES.tsv`?** The scoped spec is calibrated (FP ~20%) and defensible as a **registered action-gate row** *only with the archetype discriminator attached*. Registering the bare conjunction would encode a false generality.

**Current readings [PRIMARY: FRED, 7/15-16]: no seizure — but the buffer is gone.** SOFR99−IORB **+8.0bps** (below every threshold); SOFR−IORB −1bp; EFFR−IORB −2bps; SOFR vol $3,104B; **RRP $0.151B** — drained from $5.77B on 7/09 (**−97%**). Over 7/09→7/15 the spread moved **0 → +8bps** — *tightening, acute leg NOT fired*. **The "SOFR ticked yellow 7/16" report CANNOT be confirmed: no 7/16 SOFR print exists yet** (NY Fed publishes ~08:00 ET next business day; IORB is the only 7/16 value on the tape). ⚠️ **Correction to the parent report:** its "7/9 pull" mixed vintages — **−7bps/+2bps is the 7/08 row**; **RRP $5.77B is 7/09**, where the spread was −12/0.

---

## Counter-Evidence

1. **The gate's core verdict survives** — for funding-origin seizures, Sep-2019 (+690bps, HY *never* repriced) and UK-LDI remain unrefuted. **This report narrows the gate's scope; it does not overturn the parent.**
2. **Mar-2020's acute leg DID fire (+190bps ≥ +30)** — so on the *acute leg alone* Mar-2020 is a true positive. The failure is the **conjunction** (slow leg never fired) and the **timing** (**66% of the HY move already done** — 59% on the Baa proxy). An acute-only gate would fire — late and uselessly.
3. **The archetype taxonomy is DEWEY's construct, not a sourced framework.** Four episodes, three archetypes — thin. A future episode may not fit. *(Confidence: Medium on the taxonomy; High on the underlying per-episode data.)*
4. **RRP-drained regime is unprecedented in the sample.** The $0.151B buffer means the next funding event may look nothing like the 2018-19 reserve-scarcity regime the FP census is built on. **Caveat 3 (regime-dependence) cuts directly against the calibration's forward validity** — the honest weak point of this report.
5. **The 2-year Treasury recommendation is single-episode.** −102bps/3d at Mar-2023 is compelling but n=1 for this purpose; it is *not* calibrated for false positives (a large 2Y move has many benign causes — CPI, FOMC).

**What would disprove this:** a deposit-run or shock episode where SOFR99−IORB *does* blow out ≥+30 ahead of credit; or a funding-origin seizure where the +30/non-calendar spec fires on noise.

---

## Source Quality Assessment

**High.** Everything load-bearing is DEWEY-pulled FRED primary or Ice Data Indices via archived FRED; episode narratives anchor to FSB/BIS/Fed/[ACADEMIC] post-mortems. **Both episode agents were tasked to REFUTE the hypothesis; both tried and reported honestly** — Mar-2020 refuted it in the direction *worse* for the gate.

**Gaps:**
1. **Pre-2018 unconstructible** (§3 caveat 4) — the prompt's "since 2015" is scoped, not answered.
2. **Barr Review figures were NOT verified by the parent agent** — the salvaged sub-agent corrects them: **"over $40 billion"** (not "$42 billion"); **"roughly 85 percent"** of the deposit base (not "~80%"); the ~$100B is an **expectation communicated to supervisors**, not queued order flow; 94% uninsured verified. *Cited here at the corrected values.*
3. **FHLB Q1-2023 advances / ~$304B issuance: not verified.**
4. ~~**Dealer-side repo leg unmeasured**~~ → **✅ CLOSED same session by the `ofr_stfm.py` build** (Will-greenlit build-pass, triggered by *this* gap). **The dealer-side segment was calm too — the verdict no longer rests on the SOFR distribution alone** [PRIMARY: OFR U.S. Repo Markets, DEWEY-pulled 7/16]:

| SVB week | GCF (interdealer) | DVP | Tri-party |
|---|---|---|---|
| 2023-03-08 | 4.57% | 4.48% | 4.55% |
| 2023-03-10 *(failure)* | 4.58% | 4.50% | 4.55% |
| **2023-03-15 (peak)** | **4.65%** | 4.55% | 4.56% |
| 2023-03-16 | 4.66% | 4.55% | 4.55% |

**GCF over the entire SVB week: 4.57% → 4.66% = +9bps, and it sat AT IORB (4.65%) — +0bps — on Mar-15.** GCF is the *interdealer* segment where a collateral squeeze shows up **first**; it did not move. **This independently corroborates repo-calm from the exact blind spot the verdict was flagged on.** *(Still open: SRF take-up. Fails are now pullable but are weekly/lagging — diagnostic, not pre-emptive.)*
5. Bank CDS / KRE magnitudes not verified. No Fed/BIS *statement* that repo stayed orderly retrieved — the verdict rests on rate data (stronger than a quote, but the citation gap is real).
6. **No BIS Quarterly Review April 2020 exists** (BIS publishes Mar/Jun/Sep/Dec; the Mar-2020 edition *predates* the turmoil). Substituted the FSB Holistic Review — more granular on dating anyway. *Prompt premise corrected.*

---

## References
- **FSB, *Holistic Review of the March Market Turmoil*, 17 Nov 2020** — [fsb.org/uploads/P171120-2.pdf](https://www.fsb.org/uploads/P171120-2.pdf) [PRIMARY] *(the two-phase dating: "flight to safety" ~Feb 21-Mar 11; "dash for cash" ~Mar 11-23)*
- Vissing-Jorgensen, *The Treasury Market in Spring 2020*, BIS WP966 / NBER w29128 [ACADEMIC]
- Fed FEDS Note, *The Corporate Bond Market Crises and the Government Response*, 7 Oct 2020 [PRIMARY]
- Fed FSR May-2020 · May-2023 [PRIMARY]
- **Barr Review** (Fed, *Review of the Federal Reserve's Supervision and Regulation of SVB*), 28 Apr 2023 [PRIMARY]
- **ICE BofA HY OAS `BAMLH0A0HYM2` / IG `BAMLC0A0CM`** — full history via archived FRED raw endpoint, `Source: Ice Data Indices, LLC`, range 1996-12-31→2023-12-11 [PRIMARY] *(DEWEY-verified 7/16; see BACKLOG — FRED's live API is truncated to a rolling ~3yr window)*
- FRED (DEWEY-pulled 7/16): SOFR, SOFR1/25/75/**99**, SOFRVOL, **IORB**/IOER, EFFR, RRPONTSYD, WRESBAL, TEDRATE, DBAA, DAAA, DGS2, DGS10, WLCFOCEL, BORROW, H.8 deposits
- Supporting artifacts (this run): `output/2026-07-16_repo-market-svb-window-mar2023.md` · `output/2026-07-16_credit-spreads-march-2023-oas.md` · `output/2026-07-16_svb-march-2023-sequence-verification.md`
- **Reproduction recipe** (the FP census is derived data — regenerate it, do not chase a path). The working series was 2,066 daily rows `date, sofr, sofr99, policy, policy_src, spread99_bps, sofr_bps, effr_bps, rrp_bn, sofrvol_bn`, built as:
  1. `scripts/fred_pull.py {SOFR,SOFR99,EFFR,RRPONTSYD,SOFRVOL} --start 2018-04-03 --csv` *(the `--start` bug is fixed as of `fef252d9`; pre-fix pulls silently returned the ten OLDEST rows)*
  2. Policy rate = **IORB spliced to IOER at the 2021-07-28/29 seam** (level-continuous at 0.15%); tag each row with which one applies.
  3. `spread99_bps = (SOFR99 − policy) × 100`; fire = spread ≥ threshold; flag ±2 business days of quarter-end / month-end / Apr-15.
  *(The original working files lived under a session-scoped `/tmp` scratchpad and are gone by design — session-UUID'd paths do not survive the session, so they are deliberately not cited as artifacts. Closeout step 8d.)*

---

## Process Report

**Searches run:** **No `/deep-research` fan-out — deliberately sized down** per *Engine sizing* (2 interpretive legs ≠ a breadth problem). Instead: 1 DEWEY primary pull (series construction + FP census) + 2 targeted episode agents (adversarially tasked) + 3 salvaged sub-agents. **~310K subagent tokens vs the ~4.5M a harness run costs — ~14× cheaper for a better-evidenced answer.** This is the *Engine sizing* rule paying off; the fan-out would have added nothing (the load-bearing data is all FRED series construction, which it structurally cannot do).

**What worked:**
- **Adversarial tasking of the episode agents.** Both were told to *refute*. Mar-2020 came back **refuting my hypothesis in the opposite direction** (credit led by 17 days, not simultaneous) — a result I'd have missed had I asked for confirmation. `[[finding_adversarial_verify_own_convergence]]`.
- **The decomposition discipline caught two artifacts** that would each have flipped a verdict: Mar-2020's Baa−10Y widening survives the Treasury-rally objection (corporates underperformed by 34bps); Mar-2023's apparent +43bps Baa−10Y widening **does not** (Aaa−10Y was +35 of it — a benchmark effect).
- **Salvaging the "stalled" sub-agents.** The parent declared 3 sub-agents non-reporting and delivered with gaps; they had in fact completed. **One of them overturned the parent's own "credit didn't reprice" conclusion** by recovering the actual HY OAS series. `[[finding_workflow_scratch_crash_recovery]]` — always check for late returns before accepting a declared gap.

**Source frustrations:**
- **⚠️ FRED ICE BofA truncation → SOLVED same-day, and my own ruling was WRONG.** I logged "DOCUMENT, not BUILD — no free source exists" after verifying the wall (all `BAML*` = exactly 795 obs from exactly 2023-07-17; controls unaffected). **~1hr later a sub-agent found full 1996-2023 history via Wayback snapshots of FRED's raw `/data/<ID>.txt` endpoint** (`Source: Ice Data Indices, LLC` — DEWEY-verified independently). **I closed a wall as unsolvable without an archive-endpoint check — exactly what `[[finding_declared_data_wall_needs_fleet_memory_check]]` warns against.** BACKLOG corrected. Dead paths (do not retry): `fredgraph.csv?cosd=`, ALFRED `vintage_date`, live `/data/*.txt`.
- **`fred_pull.py` silent-truncation bug — found + FIXED + committed earlier this session** (`fef252d9`). `--start` returned the ten OLDEST rows, silently. **Fleet-wide exposure.**
- **A near-miss worth recording:** I first "verified" the fix against `BAMLH0A0HYM2` — a series that *cannot* demonstrate it (licensing-truncated). Had I not controlled against `UNRATE`/`DGS10`, I'd have reported a phantom fix-failure. **Verify a fix against a series that can actually show the fix.**
- `archive.org/wayback/available` returns **false negatives** (0 snapshots for a URL with 5) — use the **CDX index API**. `--compressed` is mandatory or gzip reads as an empty page.

**Confidence:** **High** on both episode verdicts + the FP census (all DEWEY-pulled primaries; the two independent legs — repo-calm and HY-repricing — corroborate rather than merely coexist). **Medium** on the archetype taxonomy (DEWEY's construct, n=4). **The RRP-drained regime is the honest weak point**: the FP calibration is built on a regime that no longer exists.

**If I had more time/tools:** the dealer-side repo leg (GCF/DVP fails/SRF) via `ofr_stfm.py` — the one unclosed leg under the repo-calm verdict; FP-calibrate the DGS2 discriminator (currently n=1); Barr Review CDS/FHLB legs.

**Suggestions:**
1. ✅ **`ofr_stfm.py` — BUILT + shipped this session** (Will-greenlit build-pass). **It immediately closed this report's own load-bearing gap:** GCF interdealer +9bps across the SVB week, sitting *at* IORB — repo-calm corroborated from the dealer-side segment the verdict was flagged on. Public/no-key: OFR `series/dataset?dataset=repo` (164 series) + NY Fed `pd/get/<KEYID>.json`. **Traps encoded:** `-F` (Final) lags **~3.5 months** behind `-P` (Preliminary) → the module **splices Final history + Preliminary tail and labels the boundary**, because preferring Final alone silently serves 3-month-old data as "latest"; NY Fed's `/get/all/timeseries/` returns **200-with-empty**; OFR `/v1/metadata/` needs auth while `/v1/series/dataset` does not. *(Still open: SRF take-up; MMF composition.)*
2. ✅ **`fred_pull.py --archive/--splice` — BUILT + shipped this session.** Full 1996→today for licence-truncated ICE BofA series (7,722 spliced obs; **107-obs overlap between archive and live matched EXACTLY**, which validates the archive source). **It also immediately upgraded this report's Mar-2020 leg from a Baa proxy to the actual HY OAS series — strengthening the finding 59% → 66%.** The truncation now **warns loudly on stderr** instead of failing silently.
3. **Auto-memory candidates (promotion scan):** (a) *an IG proxy masks an HY move* — the Baa−Aaa/HY divergence nearly produced a wrong verdict; (b) *don't close a data wall without an archive-endpoint check* — strengthen the existing `[[finding_declared_data_wall_needs_fleet_memory_check]]` with the Wayback recipe; (c) *verify a fix against a series that can demonstrate it*.
4. **BACKLOG build-pass:** ≥3 candidates now sit past the gate (`ofr_stfm.py` **2nd-hit**, `fred_pull.py` Wayback fallback **solution-in-hand**, `ffiec_callreport.py`/`disaster_shocks.py` high-recurrence). **Surfacing a build-pass suggestion to Will per closeout step 11.**
</content>

---

## Correction addendum (2026-07-24) — FP-census fire-counts

**Trigger:** LIQUID's independent FP backtest (`AGENTS/LIQUID/scripts/fp_backtest_079.py`, KB-LIQ-087) did not reconcile to this report — LIQUID counted **48** raw +30bp fire-days vs this report's **26**, and an episode-level FP of **62%** vs the propagated "~20%." PROME routed the reconcile (`inbox/2026-07-24_from-PROME_gate079-fp-backtest-reconcile-request.md`). **DEWEY re-derived independently from raw FRED (own code path, not LIQUID's) and CONFIRMS LIQUID. This report's §3 census was wrong.**

### What was wrong
1. **The entire "Fires" column is a bad tally.** DEWEY's independent re-pull (SOFR99 − spliced IORB/IOER ceiling, ×100, rounded 1dp, same 2018-04-03→2026-07-15 window) gives raw fire-**DAYS**:

   | Threshold | This report said | **Correct (fire-days)** | non-cal days | cal-artifact days | raw episodes | non-cal episodes |
   |---|---|---|---|---|---|---|
   | +10 bps | 83 | **532** | 362 | 170 | 52 | 56 |
   | +20 bps | 52 | **133** | 69 | 64 | 38 | 23 |
   | **+30 bps** | **26** | **48** | **21** | **27** | **22** | **8** |

   The re-pull matched LIQUID's script to the day. The original 83/52/26 is **not reproducible** by any construction tried (strict `>30` = 42; median-SOFR−ceiling = 10; unrounded = 45) — it was an un-reproducible census error, likely a sub-agent intermediate mis-transcribed into the table (the "8 TP / 2 non-cal" cells appear to have mislabeled what are actually the **8 non-calendar episodes**, of which 2 are TP).

2. **The "~20% FP" was DAY-WEIGHTED and too optimistic.** At +30bp there are **8 non-calendar episodes**: 2 true positives (Sep-2019 repo, peak 690bp; Mar-2020, peak 190bp) and ~5–6 false positives (isolated quarter-turn/1-day spikes: 2018-12-06, 2019-01-03, 2019-07-03→05, 2019-10-15→17, 2024-09-19, 2024-12-26). **Episode-level FP ≈ 62–75%** (LIQUID: 5 of 8 = 62%), not ~20%. The "~20%" was flattered because Sep-2019 — a *single* true event — supplies ~8–9 of the 21 non-calendar fire-DAYS, so day-weighting drowns the isolated FP spikes.

3. **The fix is the persistence leg, and this reconciliation VALIDATES it as necessary (not optional).** LIQUID's ≥2-consecutive-non-calendar-day requirement (added to GATES.tsv 2026-07-23, KB-LIQ-087) removes the four 1-day FP spikes (2018-12-06, 2019-01-03, 2024-09-19, 2024-12-26), cutting episode-FP to **~25%** while leaving both TPs (Sep-2019, Mar-2020 are multi-day) fully intact. **The usable mechanical spec is +30bp AND non-calendar AND ≥2 consecutive days** — the persistence leg is load-bearing, which this report's day-weighted "~20%" had obscured.

### What still stands (unaffected by the count error)
- **The mechanism verdict is intact:** the gate is SCOPED to funding-origin seizures; Mar-2020 and Mar-2023 both fail the conjunction (Mar-2020: slow leg never fired + 66% of the HY move already done; Mar-2023: repo calm, causal arrow backwards). None of that depends on the fire-day tally.
- **SVB is still correctly a non-fire** (peak ~10bp, never reached +20). Striking it from the TP list stands.
- **The archetype discriminator (§4) and the dealer-side corroboration (GCF +9bp) stand.**

### Discipline note
This is a DEWEY census error that propagated a too-favorable FP number into a live gate calibration — caught only because LIQUID independently rebuilt it. The number was **not reproducible**, which is the tell: a load-bearing count that can't be regenerated from a stated recipe should never have shipped without a re-run. `[[finding_verification_correction_downstream_propagation]]`, `[[finding_asymmetric_rigor_counterparty_claims]]` (LIQUID was right; deference-plus-verification both applied — I re-derived rather than just accepting, and the re-derivation confirmed them). Reconciliation delivered to LIQUID; GATES.tsv already carries the corrected 62%/25% (LIQUID, 7/23) — no GATES edit owed from DEWEY.
