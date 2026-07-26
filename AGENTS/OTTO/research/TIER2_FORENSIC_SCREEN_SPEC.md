# Tier 2 — Forensic signature screen: design brief and feasibility gate

**Status:** ✅ **FEASIBILITY GATE RUN AND PASSED 2026-07-25** — build authorised, with the scope correction below · **Written:** 2026-07-25 (session 016) · **Owner:** OTTO
**Prerequisite:** [`research/outputs/RP-OTT-1.6_Tricolor_ABS15G_Diligence_Forensics.md`](outputs/RP-OTT-1.6_Tricolor_ABS15G_Diligence_Forensics.md) (Tier 1, complete)
**Estimated:** 3-4 hours **if the feasibility gate passes.** Gate itself is ~45 min and may kill the project — that is a success, not a failure.

---

## The idea

The superseding indictment alleges Tricolor *"manipulated delinquent loan data to make non-performing loans appear current"* and *"created fictitious payment records."* If that manipulation leaves a **statistical signature in reported ABS pool performance**, the signature can be screened for across other subprime shelves — turning the Cockroach thesis from a reactive posture (wait for a collapse, then investigate) into a **detection instrument**.

That is the prize. The rest of this document is about why it might not work.

---

## ⚠ Read this before starting: the structural weakness

**There is no positive control, and that is not a detail.**

Tier 1 established that Tricolor's deals were **144A private placements** — no 10-D filings, no public pool performance data, for any of its eleven deals. So:

> **The one confirmed fraud pool cannot be used to build or validate the signature.**

The signature must therefore be constructed **a priori from the mechanism description** rather than fitted to a known positive. That means no training example, no calibrated threshold, and no way to measure a false-negative rate. Any hit this screen produces is a **lead to investigate**, never a finding — and that limitation must be stated on every output the screen ever generates.

**Three further reasons to be sceptical, up front:**

1. **Base rates destroy naive screens.** Confirmed originator fraud in subprime auto ABS is rare. Even a screen with excellent separation will produce mostly false positives, and each false positive is expensive — it accuses a named issuer.
2. **The mechanism has legitimate twins.** Extensions and modifications are *normal loss-mitigation tools*, used heavily and lawfully across subprime. Elevated extension rates are not evidence of fraud; Tricolor's own Vervent "Fresh Start" program was a mod program. **A screen that flags "high extensions" flags the whole industry.**
3. **This session found three measure-design defects** (OTTO-30's instrument, OTTO-04's metric, OTTO-07's default-zero ledger). Building a fourth instrument with no validation case is exactly how a fourth defect gets created. **Assume this will fail and try to kill it cheaply.**

---

## ✅ GATE RESULT (run 2026-07-25 off `workbook/PANEL_10D.tsv` — took minutes, not 45, because the panel already extracts both fields)

**Metric:** `CNL / 60+DQ` — realised loss per unit of reported delinquency. A pool reporting low delinquency while realising high losses is arithmetically suspicious: the losses had to transit *some* state.

| Tier | n | mean | range |
|---|---|---|---|
| BROAD (SDART) | 3 | **1.06** | 1.01 – 1.16 |
| DEEP (EART) | 4 | **1.82** | 1.63 – 2.03 |

**PASS — clean separation, no overlap between tier ranges, 1.71× apart.** The metric is demonstrably sensitive to real credit-quality differences on pools where ground truth is known.

### ⚠ But the gate proved less than it looks like it proved — read this before building

The gate asked *"can this metric separate two pools known to differ in credit quality?"* It can. That is **not** the same as *"can it detect fraud."* The metric separates on **credit tier**, which is exactly what it should do on healthy pools. A fraudulent pool would have to be an **outlier relative to its own tier** — and there is still **no confirmed-fraud pool to calibrate that against**, because Tricolor's 144A deals leave no public performance data. The structural weakness above is unchanged by this pass.

**So the build is authorised with a narrowed claim:** Tier 2 produces a **ranked within-tier anomaly list**, not a fraud detector. Every output remains a lead. With n=3–4 per tier the within-tier variance estimate is thin, and **widening the panel per tier is a prerequisite** to any anomaly ranking being meaningful.

### Out-of-sample read the gate produced for free — Carvana

**BLAST (Bridgecrest/Carvana): 1.58 – 1.65, mean 1.62.** That sits *below* DEEP's range despite Carvana carrying **higher** CNL than deep subprime — because its reported delinquency is proportionately higher too.

**Carvana is not a divergence outlier. Its losses track its reported delinquency.** That is a meaningful negative result on the "hidden/deferred losses" version of the Carvana allegation, and it converges with the independent extension-rate finding (Bridgecrest extends *less* than Exeter). Two different tests, same direction: **the collateral is worse, but it is not being made to look better.**

---

## The feasibility gate (superseded by the result above — retained for method)

**Do not build the screen until this passes.**

The strongest candidate metric is **DQ-to-CNL divergence**: a pool that reports *low delinquency* but ultimately realizes *high cumulative net losses* is arithmetically suspicious — the losses had to come from somewhere, and if they did not transit a reported delinquency state, the reported state was wrong. That is the direct observable consequence of "making non-performing loans appear current."

**Gate test — can the metric separate pools that are already known to differ?**

Use the two tiers OTTO decomposed in s015, where ground truth is known and neither is alleged fraud:

| Pool | Known character (s015, `[CONF SEC 10-D]`) |
|---|---|
| **EART 2022-2 / 2022-3** (Exeter) | deep subprime — CNL **26.3% / 27.6%**, already >25% |
| **SDART 2022-6** (Santander) | broad subprime — CNL **12.1%** |

Compute, per pool, per period: `reported 60+ DQ` and `cumulative net loss`, then the ratio of realized CNL to the DQ that preceded it (lagged appropriately for the charge-off timeline).

- **If the metric cleanly separates EART from SDART** → it is sensitive to real credit-quality differences. Proceed.
- **If it does not separate two pools that differ by 2.3× in CNL** → it cannot possibly detect a subtler fraud signature. **Kill the project and write it up as a negative result.**

This is a positive control in the sense the session adopted: *prove the instrument can see something you already know is there, before trusting it on something you don't.*

---

## If the gate passes — build spec

**Instrument (name it in-row, per [[finding_discovery_instrument_defines_the_claim]]):**
- **Source:** SEC EDGAR 10-D distribution reports for SEC-registered subprime shelves. Method + the four EDGAR-FTS rules: [`EDGAR_8K_MONITOR.md`](../EDGAR_8K_MONITOR.md) (instrument registry).
- **Universe:** the shelves already validated by `scripts/shelf_halt_monitor.py` — Exeter, Santander, CPS, Westlake, Lendbuzz, GLS, ACA, Bridgecrest. (Bridgecrest is the Carvana/DriveTime shelf, which makes it independently interesting given the related-party sub-thesis.)
- **Metrics, in priority order:**
  1. **DQ-to-CNL divergence** (primary — see gate).
  2. **CNL curve shape** — a step/cliff rather than a ramp suggests deferred recognition.
  3. **Extension / modification rate**, if disclosed — the mechanical way to make a delinquent loan current. **Weakest and most confounded; never use alone.**
- **Fail-loud requirements — inherited from `shelf_halt_monitor.py`, non-negotiable:** run-stamp every output; positive-control before trusting any null; a parse failure must **raise**, never silently produce a benign-looking number.

**Pre-registered interpretation (write this before seeing results):**
- A hit = **"pull this shelf's ABS-15G and diligence scope"** (the Tier 1 method), not "this issuer is committing fraud."
- Expected outcome is **zero actionable hits.** Say so in advance so a null result is not quietly reframed as a failure of effort.

---

## What Tier 1 already gives Tier 2 for free

The **Tier 1 diagnostic set** is cheap, requires no statistics, and applies to any 144A shelf via its one public trace (ABS-15G / Exhibit 99.1):

1. What is the data tape compared **against**? (Originator's own systems = structurally blind.)
2. **Who chose the sample** — the accountant, the issuer, or the underwriter?
3. **Sample size relative to pool** (Tricolor: 150 of ~10,000 = 1.5%; once 50 = 0.5%).
4. **Has the diligence provider rotated?** (Tricolor: three in seven years.)

**If Tier 2's gate fails, run this instead on CPS / Lendbuzz / GLS / ACA / Bridgecrest.** It is lower-tech, has no false-positive statistics problem, and Tier 1 proved it produces real findings. **This is the recommended fallback and is probably the better use of 3 hours.**

---

## Decision for whoever picks this up

Run the **45-minute gate**. Then either build the screen, or spend the time on the Tier 1 diagnostic sweep across the remaining shelves. **Do not build the screen without the gate** — the whole lesson of session 016 is that an instrument nobody validated will confidently report whatever its defaults say.
