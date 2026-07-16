# DEWEY → WALTER handoff — research-output ready to route

**State:** NEW · **From:** DEWEY · **Date:** 2026-07-16
**Flag:** PROME prompt **07b** (Will-approved 7/9) · parent flag **REQ-DEWEY-20260702-003**
**Report:** `AGENTS/DEWEY/output/2026-07-16_funding-gate-calibration.md`
**Mode:** Thesis · **Confidence:** High (both episodes + FP census — DEWEY-pulled primaries) · Medium (the archetype taxonomy, n=4)
**Parent:** `output/2026-07-09_funding-seizure-x1-gate.md` — this closes its two declared gaps and does **not** re-litigate its verdict.

---

## One-line verdict

**The gate does NOT generalize — it is SCOPED to funding-origin (dealer-collateral/repo) seizures.** Both tested episodes fail it, in **opposite directions**: Mar-2020 (exogenous-shock) saw **credit LEAD funding by ~17 business days**; Mar-2023 (deposit-run) saw the acute leg peak at **+7bps** while **HY OAS widened +125bps**. The parent's verdict stands *for repo/collateral seizures* and is now bounded: **the gate's silence is not evidence of calm.**

## Routing (DEWEY suggests; WALTER decides)

| Recipient | Why | Disposition |
|---|---|---|
| **LIQUID** | Gate co-owner (KILL_MEMO / X1 machinery). Gets the scoped spec + the archetype discriminator + the FP calibration. **The X1 re-scope this was commissioned for.** | **ACTION** |
| **HENRY** | Funding-plumbing mandate; the 2-year-Treasury discriminator is a HENRY-usable daily/free observable | **ACTION** |
| **PROME** | `GATES.tsv` implication (§(d) below) + a BACKLOG build-pass ask + a parent-report correction | **ACTION** |
| **NEXUS** | Bears on the fast/slow-layer split — Mar-2023 is a worked example of "credit repriced, funding never did" | info |
| **BROCK** | The Mar-2023 HY +125bps episode is a base-rate datum for forced-sale/recognition work | info |

## The two gaps, answered

**Gap (1) — does it generalize?** **No — and more strongly than the prompt's framing anticipated.** The prompt offered "or do deposit-run episodes fire the credit leg FIRST (= a scoped, not general, pre-emption)?" **That, but worse:** in Mar-2023 funding **never followed at all**, and in Mar-2020 the **conjunction never satisfied** (reserves were ample and *rising*: $1.626T → $1.896T; EFFR−IOER flat −2bps through February).

**Gap (2) — the false-positive rate.** **Answered and usable.** Apr-2018→Jul-2026: +10bps → 94% FP *(threshold structurally unusable — a 214-day "single event" swallows Sep-2019)*; +20bps → 83%; **+30bps → 69% — but 16 of 18 FPs are calendar artifacts, so +30 AND non-calendar collapses FP to ~20%.** **Mechanical firing is defensible at that spec — but only with the archetype discriminator upstream.**

## ⚠️ Corrections that must propagate

1. **To the parent report (07):** its "7/9 pull" **mixed two vintages** — the −7bps/+2bps readings are the **7/08** row; RRP $5.77B is the **7/09** row (where the spread was −12/0). Carried corrected here.
2. **The "SOFR ticked yellow 7/16" report CANNOT be confirmed** — **no 7/16 SOFR print exists yet** (NY Fed publishes ~08:00 ET next business day; IORB is the only 7/16 value on the tape). The *direction* is real (7/09→7/15: spread 0→+8bps; RRP $5.77B→**$0.151B**, −97%), but **the acute leg has NOT fired.** PROME's queue rationale cited that tick.
3. **An IG proxy nearly produced a wrong verdict.** Baa−Aaa (+8bps) suggested "credit didn't reprice" in Mar-2023. **Wrong series.** Actual **HY OAS: 397 (Mar-6) → 522 (Mar-24) = +125bps**, moving **Mar-9, concurrent with the run**. IG OAS peaked only 164. Both true — the error was calling "credit" what was only IG, **and X1's trigger is HY.**

## The recommendation (for LIQUID)

**Keep the gate. Scope it. Put an archetype discriminator upstream.**

| Archetype | Gate applies? | The right leading observable |
|---|---|---|
| **Funding-origin** (Sep-2019, LDI) | ✅ **its scope** | SOFR99−IORB **≥+30 AND non-calendar** + slow leads + dispersion |
| **Deposit-run** (Mar-2023) | ❌ **anti-correlated** | **DGS2 3-day move** (−102bps at Mar-13 = largest since Oct-1987; daily, free; fired while repo sat −10bps); H.4.1 primary credit (confirmatory, weekly) |
| **Exogenous-shock** (Mar-2020) | ❌ credit leads ~17 business days | **credit itself** — no funding pre-emption exists *(the honest answer)* |

**Why anti-correlated (the durable finding):** the gate presumes *stress ⇒ reserve scarcity ⇒ repo bid above IORB*. In Mar-2023 causality ran **backwards** — the response **injected** reserves (+$252B; primary credit $4.6B→**$152.9B**, 33×, beating the Oct-2008 record). **Repo was calm *because* the response flooded the channel the gate monitors. The harder authorities fight a deposit run, the calmer the gate reads.**

**(d) `GATES.tsv` → PROME:** the scoped spec is calibrated (FP ~20%) and defensible as a registered action-gate row **only with the discriminator attached**. **Registering the bare conjunction would encode a false generality.**

## What this does NOT support

- **The archetype taxonomy is DEWEY's construct, not a sourced framework** — 4 episodes, 3 archetypes. Thin. Medium confidence.
- **★ The honest weak point: the FP calibration is REGIME-DEPENDENT and the current regime is unprecedented in-sample.** 2020-08→2023-03 is a total dead zone (zero fires at any threshold under ZIRP + $2T RRP). **RRP is now $0.151B — the buffer is gone.** The next funding event may look nothing like the 2018-19 reserve-scarcity regime the census is built on.
- **The DGS2 discriminator is n=1** and is NOT FP-calibrated (a big 2Y move has many benign causes — CPI, FOMC).
- **Pre-2018 is NOT constructible** (SOFR starts 2018-04-03; `RRPONTSYAWARD` is an administered rate, not a market GC distribution). The prompt's "since 2015" is **scoped, not answered.**
- **Dealer-side repo leg unmeasured** (GCF/tri-party, DVP fails, SRF) — the repo-calm verdict rests on the SOFR distribution + ON RRP; **the segment where a dealer squeeze shows FIRST is unclosed.** → the `ofr_stfm.py` build.

## → PROME: BACKLOG build-pass ask (closeout step 11)

**≥3 candidates now sit past the build gate — surfacing per protocol; builds stay Will-greenlit:**
1. **`ofr_stfm.py` — 2nd hit CONFIRMED, gate tripped.** The 7/09 row *predicted 07b as the trigger* and it landed exactly; it is now the load-bearing gap under a delivered verdict. Prioritize GCF/DVP repo + fails.
2. **`fred_pull.py` Wayback fallback — solution in hand.** ⚠️ **I logged "no free source exists" for FRED's ICE-BofA rolling-3yr truncation, then a sub-agent recovered FULL 1996-2023 history via Wayback snapshots of FRED's raw `/data/<ID>.txt` endpoint** (`Source: Ice Data Indices, LLC`; DEWEY-verified independently). **My ruling was wrong within the hour** — exactly what `[[finding_declared_data_wall_needs_fleet_memory_check]]` warns against. BACKLOG corrected. **This unlocks all historical credit-spread work (base rates, episode studies) for the fleet.**
3. `ffiec_callreport.py` / `disaster_shocks.py` — high-recurrence, still 1st-surface.

*(Separately, already fixed + committed `fef252d9`: `fred_pull.py` silently returned the ten OLDEST rows on any `--start` pull. **Fleet-wide exposure** — PROME's call whether prior date-ranged FRED citations warrant a sweep.)*

## Supporting artifacts (this run)
`output/2026-07-16_repo-market-svb-window-mar2023.md` *(has its own NEW handoff in this lane)* · `output/2026-07-16_credit-spreads-march-2023-oas.md` *(data hunt, no handoff — the OAS recovery)* · `output/2026-07-16_svb-march-2023-sequence-verification.md` *(Barr Review verification: **"over $40 billion"** not "$42B"; **"roughly 85 percent"** not "~80%"; the ~$100B is an **expectation communicated to supervisors**, not queued flow; 94% uninsured verified)*

---
*Engines: **no `/deep-research` fan-out** — sized down per *Engine sizing* (2 interpretive legs, not a breadth problem): ~310K subagent tokens vs ~4.5M for a harness run, ~14× cheaper for a better-evidenced answer. 1 DEWEY primary pull (series construction + FP census) + 2 episode agents **adversarially tasked to REFUTE** (Mar-2020 came back refuting DEWEY's own hypothesis) + 3 salvaged sub-agents — one of which **overturned its own parent's conclusion**. Per `README.md`: DEWEY only CREATES here; WALTER owns the `git mv` to `processed/`.*
