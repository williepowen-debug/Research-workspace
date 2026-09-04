# Funding-Seizure X1 Pre-emption Gate — SCOPED + CALIBRATED
**Registered:** 2026-07-17 (LIQUID) · **KB:** KB-LIQ-079 (supersedes KB-LIQ-074 CANDIDATE) · **Status:** ✅ **SIGNED OFF WITH RIDERS — BROCK 2026-07-20** (`inbox/processed/2026-07-20_from-BROCK_gate-liq-079-x1-signoff.md`). X1-semantics interface CLOSED; riders R1–R4 folded into §Interface below and binding on this spec. Also retires the KB-LIQ-074 sign-off chase. **Not armed** at sign-off (SOFR99−IORB +5bp [7/16], 25bp under the +30 line) — definitional, not live.
**Input:** DEWEY 07b calibration `AGENTS/DEWEY/output/2026-07-16_funding-gate-calibration.md` (closes the 7/09 parent's two declared gaps: episode generalization + false-positive rate) + parent `2026-07-09_funding-seizure-x1-gate.md`.

---

## Why this gate exists (the load-bearing question)

The HY>280 X1 credit-recognition trigger **assumes dealers can reprice**. In a funding-origin seizure, plumbing breaks first and the corporate-credit index **lags or never prints** (Sep-2019 produced *zero* HY reprice). An index-level trigger is then a *lagging confirmation* of a funding seizure. This gate lets the bear fire on a funding/dispersion conjunction **even if HY OAS never prints 280** — but only inside a scope where that logic holds.

## ★ The discriminator is ATTACHED — a bare conjunction is false generality

DEWEY 07b's finding: **the gate does NOT generalize.** It is scoped to **funding-origin** (dealer-collateral/repo) seizures. Both non-funding archetypes DEFEAT it, in *opposite* directions. **Before asking "did the gate fire?", classify the stress:**

| Archetype | Origin | Gate applies? | Right leading observable |
|---|---|---|---|
| **Funding-origin** (Sep-2019 repo, Oct-2022 UK-LDI) | plumbing / collateral | ✅ **YES — its scope** | SOFR99−IORB +30 non-calendar + slow reserve-scarcity leads + dispersion |
| **Deposit-run** (Mar-2023 SVB) | bank solvency / deposit flight | ❌ **NO — ANTI-CORRELATED** | **DGS2 3-day move** (−102bp at Mar-2023 = largest since Oct-1987) + H.4.1 primary credit (33× spike) + H.8 small-vs-large deposit split |
| **Exogenous-shock** (Mar-2020 COVID) | outside → risk assets → forced deleveraging | ❌ **NO — credit LEADS by ~17 business days** | **credit itself is the early signal**; no funding pre-emption is available (the honest answer) |

**The mechanism to internalize (the durable finding):** the gate presumes *stress ⇒ reserve scarcity ⇒ repo bid above IORB*. In a deposit run causality runs **backwards** — the policy response **injects** reserves (Mar-2023: Fed assets +$297B/wk, reserves +$252B, primary credit $4.6B→$152.9B = 33×, beating the Oct-2008 record). **Repo was calm *because* the response flooded the very channel the gate monitors. The harder authorities fight a deposit run, the quieter this gate reads. Its silence is NOT evidence of calm.**

## The scoped fire spec (funding-origin ONLY)

**ARMS (watch, not fire):** acute leg alone — **SOFR99−IORB ≥ +30bps AND non-calendar (±2 business days of quarter-end / month-end / Apr-15 excluded) AND ≥2 CONSECUTIVE such days.** *Acute-alone fired late-and-uselessly in Mar-2020 (by the +190bp print, HY had already run 66% of its eventual +725bp move) → arm, don't fire.*

> **⚠️ The persistence leg (≥2 consecutive days) was ADDED 2026-07-23** by my own FP backtest (§LIQUID INDEPENDENT FP BACKTEST below, KB-LIQ-087). It cuts episode-level FP from **5 of 8 → 2 of 8 non-calendar episodes (n=1 true positive)** while leaving the Sep-2019 true positive **completely intact**. ⚠️ **Denominator form is mandatory (adopted 2026-07-30, BROCK's n=1 flag; PROME fixed `PROME/GATES.tsv` to match): never write a bare "62%" or "25%" — a rate cannot be estimated from one true positive, and the percentage sheds its denominator the instant it is lifted into another surface.** **Do NOT instead widen the calendar filter** — tested and rejected: adding tax dates erases the 690bp Sep-2019 peak, because that seizure was *caused* by a corporate-tax-date reserve drain. **Calendar width is capped at the registered ±2bd; persistence is the correct discriminator.** This is a LIQUID-domain change to the funding mechanics — BROCK's 7/20 sign-off explicitly did not cover the FP census, so it needs no re-sign-off, but BROCK is notified because it changes *when* the gate they signed off on arms.

**FIRES (funding-seizure pre-emption memo):** the **conjunction** —
1. **Archetype = funding-origin** (discriminator above; NOT deposit-run, NOT shock), AND
2. **Acute:** SOFR99−IORB ≥ +30bps AND non-calendar, AND
3. **Slow reserve-scarcity lead:** EFFR−IORB widening / regular above-IORB bank borrowing / reserve-demand-curve slope negative, AND
4. **Dispersion leg:** SOFR 1st–99th spread widening / SRF>0 / **GCF−TriParty premium widening** (dealer-side, earliest tell — `ofr_stfm.py`) / named AI-HY basket dispersion (CRWV/APLD, KB-LIQ-073).

**Fire consequence (ACTION):** LIQUID funding-seizure pre-emption memo → **PROME + NEXUS + BROCK + HENRY**, same session. Re-run KB-LIQ-062 (beta-vs-substance) on any concurrent HY move. → **GATES.tsv row proposed to PROME (GATE-LIQ-079).**

> ✅ **VINTAGE CONVENTION (WQ-162, Will 2026-09-02 21:29 ET *"Approve WQ-162 with your recs"*; mirrored here 2026-09-03 as a CONVENTION line, never a revision claim).** **ARM:** SOFR99 (NY Fed SOFR 99th percentile) and IORB on EACH of the ≥2 consecutive non-calendar days — ≥4 observations — taken **AS FIRST PUBLISHED**; if a later print differs it is noted, never re-grading an armed or un-armed day. **FIRE legs 3–4 above name SERIES but NO THRESHOLDS** (*"widening"*, *"slope negative"*, *"SRF>0"*): ⚠️ **until each is banded and base-rated on this surface, FIRE is `UNGRADEABLE`, not false** — ARM stays fully gradeable and is the leg `boot.py` watches daily (+8bp [latest, 9/3 boot], 22bp under +30). ⛔ **No thresholds are set here 2026-09-03:** a band written without a base rate is the dead-band class (KB-LIQ-104/106/107/109), and the FP census behind ARM (n=1 true positive) measured none of these legs. Owner commitment: band + base-rate the FIRE legs (EFFR−IORB · above-IORB borrowing · reserve-demand slope · SOFR 1st–99th / SRF / GCF−TriParty) at or before the 2026-10-31 `review_by` and return the bands to PROME as a PROPOSAL. A rule on what the grader DOES; adopted under SEARCH-NOT-FOUND on publisher revision behaviour (`KILL_MEMO_HY_OAS_260.md` §canonical letter item 6).

## ★ Interface with X1 — BROCK riders R1–R4 (BINDING, signed off 2026-07-20)

BROCK owns the wrapper-leads half of X1, so the X1-semantics interface is theirs to adjudicate. Verdict: **sign off with riders.** All four are interface-scoped and bind this spec. BROCK explicitly did **not** re-derive the funding mechanics or the FP census — those stay LIQUID/DEWEY's, and the sign-off confers no validation of them.

| # | Rider | What it forbids / requires |
|---|---|---|
| **R1** | **Separate root, NOT an X1 satisfaction** | A funding-origin seizure is a *plumbing* event, not credit-recognition. **X1 semantics are UNCHANGED: X1 still requires BOTH the wrapper-leads half AND HY OAS >280 sustained.** Any 079 fire is memo'd as a **funding-seizure pre-emption** — never as "X1 MET" or "wrapper-leads fired." Two triggers, two names. |
| **R2** | **Does NOT auto-open the X1 sizing gate** | X1's sizing gate governs *private-credit-as-an-independent-bear-root*. A funding seizure hits everything and validates nothing about PC specifically. 079 may arm a **funding/liquidity** posture; **PC sizing stays gated on X1** (or on marks-window substance). Different bear, different sizing rail. |
| **R3** | **A 079 fire SUSPENDS the wrapper-leads read** | During a live funding-origin seizure BROCK's observable is **contaminated, not readable** — wrappers and managers both gap on forced deleveraging (Mar-2020 fire-sale pattern), which is not credit recognition. BROCK re-adjudicates on a **clean leg after the plumbing event clears.** Corollary to the shock-archetype row above ("credit LEADS ~17bd"), wrapper-specific. |
| **R4** | **Regime caveat carried, non-blocking** | My own declared weak point #1 (FP census is regime-dependent; **RRP is now ~$0.9B — the buffer the census was built under is GONE**) means a real fire may need recalibration. That is a **LIQUID call at fire-time**; logged here so the interface record carries it. |

**Consequence requested (PROME registers, not BROCK):** GATES.tsv `GATE-LIQ-079` = **ARMED-scoped**, with **R1/R2 baked into the row semantics** (separate root; does not open the X1 sizing gate); fire-consequence memo → PROME + NEXUS + BROCK + HENRY.

⚠️ **Open, and now the binding constraint on this gate:** the **false-positive backtest** (Rank-3, deferred 7/18) was supposed to run *before* the sign-off ask went out — the sign-off arrived first. R4 is therefore live: the "+30bp non-calendar" arm line still rests on a census built in an RRP-buffered regime that no longer exists. **Do not treat sign-off as calibration.** The FP rate is the next owed piece of work on this file.

## False-positive calibration (the second gap DEWEY closed)

Census 2018-04-03 → 2026-07-15 (SOFR's true start; IORB spliced to IOER at the 2021-07-28/29 seam):

| Threshold | Fires | FP rate | With calendar filter |
|---|---|---|---|
| +10bps | 83 | **94%** (structurally unusable — a 214-day "single event" swallows Sep-2019 whole) | — |
| +20bps | 52 | 83% | — |
| **+30bps** | **26** | **69%** | **±2bd calendar filter → 16 of 18 FPs are calendar artifacts → FP ~20%** |

**Mechanical firing is defensible at +30bps AND non-calendar — *with the discriminator upstream.*** Without it, the gate sits silent through a Mar-2020 or Mar-2023 while the repricing happens elsewhere.

---

## ★★ LIQUID INDEPENDENT FP BACKTEST — 2026-07-23 (KB-LIQ-087, closes the R4 / Rank-3 owed item)

**Script:** `scripts/fp_backtest_079.py` (reproducible, FRED primary: SOFR99, IORB spliced to IOER at the 2021-07-28/29 seam, RRPONTSYD; 2,071 obs 2018-04-03 → 2026-07-22). Run independently — **not** inherited from DEWEY.

### ⚠️ Finding 1 — DEWEY's ~20% FP does NOT reproduce. The honest number is worse.

| | DEWEY 07b | **LIQUID backtest** |
|---|---|---|
| +30bps raw fire-**days** | 26 | **48** |
| non-calendar fire-days | — | **21** |
| non-calendar **episodes** | — | **8** |
| **FP, episode-level** *(a count, NOT a rate — n=1 TP)* | ~20% *(refuted)* | **5 of 8** |

I cannot reconcile 26 vs 48 without DEWEY's working. **Do not cite the ~20% figure.** Two things drive the gap: (a) an unreconciled census difference, and (b) **day-weighting flatters the gate** — Sep-2019 alone contributes 8 of the 21 non-calendar fire-days, so a per-day FP rate buries the fact that there is only **one** true event. *Episode-level is the decision-relevant unit: you decide once per episode, not once per day.* Same bias DEWEY correctly flagged at +10bps ("a 214-day single event swallows Sep-2019 whole") — it is still present at +30, just smaller.

### The 8 non-calendar episodes, classified

| Episode | Days | Peak | Classification |
|---|---|---|---|
| 2018-12-06 | 1 | 50bp | FP — Dec-18 reserve-scarcity prelude |
| 2019-01-03 | 1 | 49bp | FP — year-end turn leaking past ±2bd |
| 2019-07-03→05 | 2 | 41bp | FP — Q-end + Jul-4 holiday leakage |
| **2019-09-13→25** | **8** | **690bp** | ★ **TRUE POSITIVE — the Sep-2019 repo seizure** |
| 2019-10-15→17 | 3 | 60bp | TP-continuation (post-Sep-19 + Oct-15 tax date) |
| 2020-03-12→18 | 4 | 190bp | **SCOPE-EXCLUDED** — COVID = shock archetype, discriminator vetoes |
| 2024-09-19 | 1 | 44bp | FP — mid-Sep corporate tax date |
| 2024-12-26 | 1 | 40bp | FP — year-end turn leakage |

### ★ Finding 2 — DO NOT widen the calendar filter. It would ERASE the true positive.

The obvious "fix" for those FPs is a wider filter (tax dates, wider year-end). **I tested it and it is actively dangerous.** Adding quarterly corporate tax dates cuts Sep-2019 from **8 days / 690bp peak → 3 days / 70bp peak**, because **Sep-15 IS a corporate tax date and the Sep-2019 seizure was *caused* by exactly that** — corporate tax payments plus a large UST settlement draining reserves on 9/16. Daily prints: 9/16 **+250bp**, 9/17 **+690bp**, 9/18 **+290bp** — all three removed by a tax-date filter.

> **The durable lesson: funding seizures happen ON calendar dates, because calendar dates are precisely when reserve scarcity bites.** "Calendar artifact" reasoning, pushed one step too far, filters away the event class the gate exists to detect. The registered ±2bd month/quarter-end + Apr-15 filter is at about the maximum defensible width.

### ✅ Finding 3 — ADD A PERSISTENCE LEG instead (adopted; see revised ARMS spec above)

**Require ≥2 consecutive non-calendar days at ≥+30bps.** Tested:

- Removes **4 of 5 FPs** (all four are 1-day turn-noise prints: 2018-12-06, 2019-01-03, 2024-09-19, 2024-12-26)
- **Retains the true positive completely intact** — 8 days, 690bp peak, untouched
- Episode-level FP **5 of 8 → 2 of 8 non-calendar episodes (n=1 true positive)** — a count, not a rate; never restate as a bare percentage

This is preferable to a wider filter because it is **mechanistically motivated, not merely curve-fitted**: turn/tax noise is a *one-day settlement artifact* that reverses next session, whereas a genuine seizure is a *persistent* collateral-financing failure. That distinction is the reason to trust it at n=1 (below).

### Finding 4 — the +30 line is regime-appropriate, and today is quiet *by drained-regime standards*

| Regime (RRP<$50B = drained) | n | mean | p50 | p90 | p95 | days ≥+30 | +30 sits at |
|---|---|---|---|---|---|---|---|
| **DRAINED** | 970 | +13.7bp | +9 | +21 | +25 | 37 | **96.2nd pctile** |
| BUFFERED | 1,099 | +2.7bp | +2 | +7 | +9 | 10 | 99.1st pctile |

In today's drained regime **+30 ≈ p96** → expect ~4% of days to tag spuriously; that is a real calibration statement replacing "illustrative." **Today's +5bp [7/22] sits at the 7th percentile of the drained distribution** (drained mean +13.7, median +9) — so the correct reading is not merely "25bp below the line" but **"running below its own regime baseline."**

### ★ Finding 5 — R4 ANSWERED: my weak point #1 was OVERSTATED. Restating it.

**The RRP-drained regime is NOT unprecedented in-sample — it is the majority of the *informative* sample.** Contiguous drained spans: **2018-01-11→2020-03-24 (542 obs)**, 2020-04-09→2021-04-16 (252), **2025-08-14→2026-07-23 (230, current)**. And **19 of the 21 non-calendar fire-days sit in the DRAINED regime** — the census's entire information content comes from a regime structurally comparable to today's. The 2020-08→2023-03 dead zone is the *unrepresentative* part, not today.

**But the weak point survives in a sharper and more useful form:** *RRP level is the wrong regime variable.* 2018-20 drained meant **reserve scarcity**; today drained means **RRP≈0 with reserves ~$3.06T (still ample)**. Those are different states that the RRP<$50B cut conflates. → **Monitor the reserve-demand-curve slope / reserves-to-GDP, not the RRP level**, when judging whether this calibration still applies. That is now the live regime question, replacing "the buffer is gone."

## ⚠️ Honest weak points (do not launder these away)

1. ~~**The FP census is REGIME-DEPENDENT and the current regime is UNPRECEDENTED IN-SAMPLE.**~~ **REVISED 2026-07-23 by my own backtest (KB-LIQ-087) — the original claim was OVERSTATED.** The drained regime is *the majority of the informative sample* (2018-01→2020-03 = 542 obs drained; 19 of 21 non-calendar fire-days sit there), so the census is built on a regime structurally comparable to today's, not an alien one. **Sharper surviving form: RRP level is the WRONG REGIME VARIABLE.** 2018-20 "drained" meant *reserve scarcity*; today "drained" means *RRP≈0 with reserves ~$3.06T, still ample* — the RRP<$50B cut conflates two different states. → **judge continued applicability off the reserve-demand-curve slope / reserves-to-GDP, not the RRP level.**

1b. **★ NEW, and now the binding statistical weakness: n=1.** There is exactly **ONE** true positive in the entire constructible sample (Sep-2019). Every FP rate quoted anywhere in this file — DEWEY's or mine — is computed against a single positive event, so none of them is a *statistical* estimate; they are descriptions of one episode's neighbourhood. **The persistence leg is defensible at n=1 only because it is mechanistically motivated** (turn/tax noise is a one-day settlement artifact that reverses; a seizure is a persistent collateral-financing failure) **rather than fitted to the data.** Treat any tuning that *lacks* such a mechanism as overfitting. This supersedes the old weak point #1 as the honest headline limitation.
2. **The archetype taxonomy is DEWEY's construct** (n=4, 3 archetypes) — thin; a future episode may not fit.
3. **DGS2 (the deposit-run discriminator) is n=1 and NOT FP-calibrated** — a large 2Y move has many benign causes (CPI, FOMC).
4. **Pre-2018 is unconstructible** (SOFR starts 2018-04-03) — "since 2015" is scoped, not answered.
5. **Row-definition mismatch (from KB-LIQ-074) RESOLVED:** acute leg = **SOFR99−IORB** (99th-pctile repo vs the policy ceiling), not 99pct−SOFR. This spec adopts SOFR99−IORB throughout.

## Current reading [LIQUID-pulled 2026-07-16/17, FRED + OFR + NY Fed]

**No seizure. Acute leg not even armed — but the buffer is gone.**
- SOFR99−IORB **+5bp [7/16]** (peaked +8 [7/15]) — **25bp below the +30 arm line.**
- SOFR−IORB −3bp [7/16]; EFFR−IORB −2bp [7/16] (slow leg quiet).
- **GCF−TriParty +2bp** [7/15, `ofr_stfm.py`] — dealer-side calm (GCF 3.70 / DVP 3.66 / Tri 3.68).
- RRP **$0.125B [7/16]** — drained (−97% from $5.77B 7/09); buffer exhausted, mechanic intact (KB-LIQ-067/070).
- WRESBAL **$3,142.7B [as-of Wed 7/15]**, rebounded above $3T (cushion to $2.8T ~$343B).
- ⚠️ **Watch (diagnostic, weekly/lagging):** UST dealer financing **fails-to-receive $120.9B [7/8] +13% w/w**, fails-to-deliver $101.1B +5% w/w (`ofr_stfm.py`). Elevated but NOT the acute leg — fails lag; pair with the SOFR99 tail.

**Archetype today:** none active. If one arms, classify FIRST (funding-origin vs deposit-run vs shock) before reading the gate.
