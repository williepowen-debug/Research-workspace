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

**ARMS (watch, not fire):** acute leg alone — **SOFR99−IORB ≥ +30bps AND non-calendar** (±2 business days of quarter-end / month-end / Apr-15 excluded). *Acute-alone fired late-and-uselessly in Mar-2020 (by the +190bp print, HY had already run 66% of its eventual +725bp move) → arm, don't fire.*

**FIRES (funding-seizure pre-emption memo):** the **conjunction** —
1. **Archetype = funding-origin** (discriminator above; NOT deposit-run, NOT shock), AND
2. **Acute:** SOFR99−IORB ≥ +30bps AND non-calendar, AND
3. **Slow reserve-scarcity lead:** EFFR−IORB widening / regular above-IORB bank borrowing / reserve-demand-curve slope negative, AND
4. **Dispersion leg:** SOFR 1st–99th spread widening / SRF>0 / **GCF−TriParty premium widening** (dealer-side, earliest tell — `ofr_stfm.py`) / named AI-HY basket dispersion (CRWV/APLD, KB-LIQ-073).

**Fire consequence (ACTION):** LIQUID funding-seizure pre-emption memo → **PROME + NEXUS + BROCK + HENRY**, same session. Re-run KB-LIQ-062 (beta-vs-substance) on any concurrent HY move. → **GATES.tsv row proposed to PROME (GATE-LIQ-079).**

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

## ⚠️ Honest weak points (do not launder these away)

1. **The FP census is REGIME-DEPENDENT and the current regime is UNPRECEDENTED IN-SAMPLE.** 2020-08→2023-03 is a total dead zone (zero fires, ZIRP + ~$2T RRP buffer). **RRP is now $0.125B [7/16] — the buffer the census was built under is GONE.** The next funding event may look nothing like the 2018-19 reserve-scarcity regime → **thresholds may need recalibration when a real event arrives.**
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
