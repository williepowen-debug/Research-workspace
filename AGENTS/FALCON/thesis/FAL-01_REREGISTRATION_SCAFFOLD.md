# FAL-01 → FAL-03 Re-Registration Scaffold

**Written:** 2026-07-27 (session 2, post-crash re-boot) · **Author:** FALCON
**Purpose:** the derivation behind FAL-03. FAL-01 failed on 2026-07-25 (Jazan); this document is the record of *how* its successor's confidence and threshold were re-derived, so the number is auditable rather than asserted.
**Owed since:** 2026-07-27 session 1 (SCRATCH item 5). Three conditions were set for the successor and all three are discharged below.

---

## 0. The three registered conditions on this successor

| # | Condition (set 7/27 s1) | Discharged where |
|---|---|---|
| 1 | **Re-derive the confidence — do NOT inherit the 70%** | §3 — derived at **58%** from a regime-split base rate + a two-leg decomposition |
| 2 | **State the class test as an OPERATIONAL THRESHOLD**, not an exemplar list | §2 — three named routes (FM / stated volume-days / loadings interruption) |
| 3 | **Enumerate which belligerents the confidence is priced off** | §4 — four named axes + a fifth-actor re-registration trigger |

---

## 1. What actually broke FAL-01 — and what did not

FAL-01: *"No Gulf-ally or Iranian oil-PRODUCTION-infrastructure hit (Aramco/ADNOC/Kharg-oil-terminal class) AND no vessel confirmed SUNK by Jul 26"* — 70%, FAILED on the 7/25 Jazan strike.

**What did not break it:** the modelled dyad. US-Iran mutual restraint around the energy complex — the thing the 70% was actually priced off — **held to the end and is still holding.** Thirteen consecutive strike nights, zero production hits, then a full campaign pause on 7/24.

**What broke it:** the **actor axis**. A third belligerent pair (Saudi-Houthi, four-year truce broken) reached the asset class my wording covered but my confidence never modelled. Fourth instance of the wording-wedge family: HAW-10 (locus) → HAW-14 (catalyst) → HAW-15 (mechanism) → **FAL-01 (actor)**.

> **A prediction written over an ASSET CLASS is exposed to every belligerent who can reach that class — not just the two whose behaviour justified the confidence.**

**The second, quieter defect:** FAL-01 fired on **"hit."** "Hit" is a low, binary, widely-reachable bar that says nothing about whether any oil stopped moving. Jazan fired it while producing **zero confirmed barrels offline** — the tape *fell* 9% the same week. A test that fires on an event the market correctly ignores is measuring the wrong thing.

---

## 2. The operational threshold (condition 2)

**⚠️ Hindsight-fitting disclosure, stated up front.** Applied retroactively to FAL-01's window, the threshold below would have resolved FAL-01 **CONFIRMED** — Jazan produced no confirmed loss. I am therefore choosing a bar that would have saved my own failed row, and that deserves scrutiny rather than a footnote.

**The defense, on the record:** the operational-threshold framing was recommended by **HAWK on 2026-07-25** — *two days before* FAL-01 resolved — in `inbox/processed/2026-07-25_from-HAWK_fal01-mangaf-class-test-window-closes-tomorrow.md`, which explicitly scopes it *"Suggestion for FAL-01's successor, not for FAL-01 itself (pre-registration discipline — don't re-spec inside the window)."* The bar was pre-registered before the outcome was known. It is not retro-fitted. It is also not adopted *because* it flatters FAL-01 — it is adopted because "hit" measures reachability and "supply offline" measures consequence, and only the second one transmits to markets.

### FAL-03 FIRES if ANY of the following is confirmed in-window

| Route | Threshold | Why this route exists |
|---|---|---|
| **(a) Force majeure** | Declared by the operator or the state on crude, condensate, refined-product, LPG or LNG deliveries | The cleanest, most unambiguous signal; already has 2 in-war precedents (Bapco, Ras Laffan) so it is a *demonstrated-reachable* bar, not a theoretical one |
| **(b) Stated volume-days** | **≥100,000 bpd** (or gas equivalent) stated offline for **≥7 consecutive days**, attributed on the record by the operator, the state, or a named-source trade primary (Argus/Platts/Reuters citing refinery/terminal officials or shipping agents) | Captures a real outage that the operator soft-pedals; the trade-primary route is the one that actually works against Gulf disclosure practice |
| **(c) Export interruption** | Loadings **suspended ≥72h** at a **named** export terminal, evidenced by **two independent routes** (e.g. Kpler/Vortexa loadings + a shipping-agent or port-authority notice), **AND not attributable solely to war-risk routing avoidance** | The disclosure-independent route. The exclusion clause is load-bearing — see §5 |

**FROZEN vs TRACKED:** the **100,000 bpd** bar is **FROZEN** — an absolute volume, not indexed to any moving quantity, and it does not decay into a stale reference. The ≥7-day and ≥72h durations are likewise frozen.

**Scope:** Gulf-ally **or** Iranian oil/gas production, refining, or export assets. Direction is deliberately unrestricted — FAL-01 never had a direction gap and the successor does not introduce one.

---

## 3. The confidence derivation (condition 1) — 58%, NOT 70%

### 3a. The base rate, regenerable from my own ledger

Derived from `domain/energy-strikes/STRIKES.tsv` by classifying the `Status` column as operational (`halted` / `offline` / `reduced` / `FM-declared` / `suspended`) vs non-operational (`hit` / `fire` / `no-damage` / `ATTEMPTED`). **Reproducible** — re-run the classification over the TSV and the counts regenerate.

| Regime | Window | Days | Operational-class events | Rate |
|---|---|---:|---:|---|
| **Acute / damage regime** | Feb 28 – Apr 9 2026 | ~41 | **10** | ~5.1 per 3wk |
| **Premium regime** | Apr 10 – Jul 27 2026 | **109** | **0** | **0 per 3wk** |

**The theater is bimodal, and the split is sharp.** In the premium regime there were still five logged strikes — VTTI Fujairah (5/4), KOC platform (7/12), Mangaf (7/18), **Jazan (7/25)**, Abqaiq (7/27) — and **not one** produced a confirmed loss. The war has been reaching the asset class routinely for 15 weeks without taking barrels off the market.

**⚠️ Intake caveat, stated honestly** (`[[finding_count_measures_intake_not_domain]]`): this zero is a count of *my ledger*, not of the world, and the ledger's own scope label says *"absence of a row != absence of a strike."* The Apr–Jun stretch was also a genuine ceasefire/lull, so the zero is probably real — but it is intake-limited and should not be treated as an exhaustive negative.

**A naive base-rate read would price FAL-03 at ~85-90%.** I am not marking it there.

### 3b. Why the discount to 58% — two-leg decomposition

The premium regime's clean record is *not* transferable to this window, because this window does not start from a quiet board.

**Leg A — Jazan converts retroactively (25%).** A 400 kbpd Aramco refinery is *currently burning* with a damage assessment pending and 3 days of silence. This is a live, already-in-flight trigger that no prior window began with. Pushing the probability **down**: Aramco's disclosure practice is genuinely opaque (Ras Tanura, 550 kbpd, closed out as "very minor"); and Jazan is a **refinery**, so an outage would show in refinery *runs*, not in the OPEC MOMR / IEA OMR crude-production series that land mid-window — those monthlies are a strong route for a *crude* loss and a **weak** one for this specific asset. The most probable firing route here is a named-source trade primary (Argus/Platts), not an official statement. → **25%**.

**Leg B — a new qualifying event in-window (22%).** P(a new attack on the class in 21 days) is high — roughly weekly attempts through July (7/12, 7/18, 7/25, 7/27) across three live axes — call it ~80%. But P(confirmed loss | attack) in the current regime is ~0/5 observed; allowing for regime drift and zero spare capacity, ~28%. → 0.80 × 0.28 ≈ **22%**.

**Combination:** P(fire) = 1 − (1−0.25)(1−0.22) = 1 − 0.585 = **41.5%** → **P(no fire) ≈ 58%.**

### 3c. Why 58 and not the naive 85-90

The discount off the base rate is large and deliberate. Four reasons, in order of weight:
1. **A live in-flight trigger** (Jazan, burning, assessment pending) — no prior premium-regime window opened this way.
2. **Three active belligerent axes, not one** — the premium-regime zero was accumulated under a single restrained dyad. That structural condition no longer holds (§4).
3. **The four-year Saudi-Houthi truce is broken** — the constraint that kept the Red Sea assets out of the class is gone.
4. **OPEC spare capacity is 0.02 mb/d (ME 0.00)** — with no buffer, any real outage becomes *measurable and newsworthy* faster, which raises the probability that a loss is **confirmed** rather than absorbed quietly.

**And the direction of the adjustment is the lesson:** FAL-01 failed by trusting a regime that a new actor broke. When the demonstrated failure mode is over-trusting a quiet base rate, erring toward the discount is the correct direction. **58% is derived, not anchored — the 70% was not consulted.**

---

## 4. Belligerent enumeration (condition 3) — the actor axis

**This confidence is priced off FOUR belligerent axes, not two.** This section is the direct fix for what killed FAL-01.

| # | Axis | Status at registration | Demonstrated reach to the class |
|---|---|---|---|
| **(a)** | US / Israel → Iran | **PAUSED** since 7/24 (13 nights, then stopped) — munitions-constrained, not intent | Yes — South Pars, Isfahan (Mar) |
| **(b)** | Iran → Gulf allies | Retaliation halted 7/24, explicitly conditional ("attack for attack") | Yes — Ras Tanura, Bapco, Kuwait refineries, Ras Laffan (Mar) |
| **(c)** | **Houthi / Ansar Allah → Saudi** (Red Sea: Jazan, Yanbu) | 🔴 **ACTIVE** — four-year truce broken 7/25 | **Yes — this is the axis that broke FAL-01** |
| **(d)** | **Iran-aligned Iraqi militias → Saudi / Gulf** | 🔴 **NEWLY ACTIVE** — Abqaiq attempt 7/27, launched from Iraqi territory | Attempted, not yet achieved (intercepted) |

**Registered rule:** a qualifying event by **ANY of the four** fires FAL-03. No axis is exempt, and the confidence is priced with all four live.

**Fifth-actor clause:** if a **fifth** belligerent axis appears (a new state or non-state actor reaching this asset class), that is a **re-registration trigger — not an exculpation.** I do not get to say "I didn't model them" twice. Log it, re-derive, and if the window is still open the row resolves on its registered terms regardless.

---

## 5. Resolvability guard — silence must NOT auto-confirm

**The spec's biggest weakness, addressed head-on.** FAL-03 is written as a negative ("no confirmed loss"). Gulf operators systematically under-disclose. So the default failure mode is: **nothing gets confirmed → the row CONFIRMS → I collect a win for an outcome I never actually observed.** That is the measurement instrument defining the claim (`[[finding_discovery_instrument_defines_the_claim]]`), and it would make the row worthless.

**Pre-registered guard — the Jazan leg must be AFFIRMATIVELY closed.** At window close I must be able to point to one of:
- **(i)** a positive qualifying disclosure or measurement → **FAILED**; or
- **(ii)** an affirmative all-clear — an operator/state "no material impact" or "back at full rates" statement, or independent evidence of normal runs/loadings → contributes to **CONFIRMED**.

If **neither** exists — Jazan's status still genuinely unknown and no independent route resolved it — that leg resolves **UNRESOLVED**, and the row closes **PARTIALLY at best, never CONFIRMED.**

Per `[[finding_resolvability_defect_is_status_not_confidence]]`: if the deciding evidence is unavailable at close, that is a **Status** change (PARTIALLY / STUCK / extend), **never** a confidence cut and **never** a default-CONFIRMED.

**The (c)-route exclusion clause is part of the same guard, in the opposite direction.** Bab al-Mandab traffic is already −56% for **war-risk routing** reasons. A Red Sea loadings drop is therefore **confounded** between "hulls won't sail" and "the refinery is down." Without the exclusion clause, route (c) would fire on the premium regime itself — precisely the thing FAL-03 exists to distinguish from a supply loss.

---

## 6. Kill-switch framing (HAW-11 discipline)

FAL-03 is registered as **the explicit falsification test for FALCON's currently load-bearing thesis** — the one carried into BRENT / HENRY / SAM / CARL read-throughs:

> **"This is a risk-PREMIUM regime, not a supply-LOSS regime. Willingness to move a hull is priced; lost barrels are not."**

- **If FAL-03 FIRES** → the premium thesis is dead, the **P→R conversion has happened**, and every cross-agent read-through built on "zero barrels offline" needs immediate revision.
- **If FAL-03 EXPIRES CONFIRMED** → the premium read is reinforced *through* a broken truce, a burning Aramco refinery and a third belligerent axis — which would make it considerably more robust than it is today.

**Wording-identity (HAW-10):** FAL-03's registered text in `PREDICTIONS.tsv` is **canonical**. STATUS's D-tell #1 and the Gulf-production/bypass-infra vector threshold must **reference** it, not restate it. Both were reconciled to point at FAL-03 in the same session this row was registered — a loose restatement in either place recreates the exact HAW-10 wedge.

**Unconditional — no void path.** FAL-03 states no premise, so per the ledger's HAW-07 discipline it has **no VOID route**. A ceasefire, a Hormuz reopening or a blockade lift does **not** void it; those would simply make CONFIRMED more likely on the merits.

---

## 7. What would make me re-register early

- A **fifth belligerent axis** reaching the class (§4).
- The **100k bpd / 7-day** bar proving unmeasurable in practice for a real event — i.e. the threshold failing on its **spec** rather than on the world (`[[finding_threshold_spec_fails_before_world]]`).
- Route (c)'s war-risk confound proving impossible to exclude cleanly on a live case.
