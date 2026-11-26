# LABOR TRADE.md
**Generated:** 2026-06-09 | **Domain:** LABOR (input agent) | **Direct trade:** NONE HELD (KELYA $7.5P expired worthless 2026-08-21)
**Prior version:** `domain/sources/TRADE_archive_20260307.md`

**Purpose.** Two jobs: (1) index which LABOR signals transmit to which other agents, so cross-agent triggers are explicit; (2) keep the closed KELYA record (no position since 2026-08-21; history archived). **Live position state (contracts, cost basis, mark) lives in FORGE — this file does not duplicate it.** Cross-position triggers for KRE/WAL/OZK/HYG/etc. live with the position owner; LABOR sends the signal, FORGE/REGINALD/HENRY/CARL act on it.

**Anchor reads:**
- `STATUS.md` — current dashboard, convergence matrix, predictions, exit rules
- `LESSONS.md` L-01 — company-tier ≠ industry employment
- `docket/CATALYSTS.tsv` — forward catalyst source of truth
- auto-memory `[[feedback_prediction_canonical_measure]]`, `[[feedback_position_cost_basis_not_authoritative]]`

---

## §1 — Transmission Signal Index

LABOR vector → threshold → target agent(s) → priority. This table owns the trigger definitions and their base-rate provenance; live levels and distances live in STATUS § KEY THRESHOLDS, not here. When a threshold fires: route the signal to WALTER per CLAUDE.md Outbox Protocol and self-commit the `AGENTS/SIGNALS.md` row (root carve-out ②).

| # | Vector | Threshold (fires signal) | Target agent(s) | Priority |
|---|---|---|---|---|
| T-01 | Initial claims | >250K sustained (4+ wk MA) | CARL, REGINALD | 🔴 |
| T-02 | Initial claims | >300K single print | REGINALD (all ORANGE banks → RED), HENRY | 🔴 |
| T-03 | **EPOP** *(re-specced 2026-08-07, BD-15)* | **EPOP fell ≥0.3pp over 3 months.** ~~U-3 ≥4.7%~~ — retired: a U-3 LEVEL bar fired in **65.4%** of all months since 1990 and separated recession from non-recession by only **+12.9pp**. The EPOP leg: base **11.7%**, in-recession **64.5%**, out **7.6%** = **+56.9pp**. Population denominator ⇒ immune to the participation artifact | CARL, HENRY | 🟠 |
| T-04 | **EPOP** *(re-specced 2026-08-07, BD-15)* | **EPOP fell ≥0.5pp over 6 months AND ≥0.3pp over 3 months** (conjunction base-rated JOINTLY, not multiplied: base **8.2%**, in-rec **58.1%**, out **4.4%** = **+53.6pp**). ~~U-3 ≥5.0%~~ retired — it fired in **58.1%** of all months since 1990, separation only **+13.8pp**. Compound chosen over the single 6-month leg because a 🔴 that escalates REGINALD to RED needs the lower false-positive rate (4.4% vs 9.1%) | HENRY (structural bid break), REGINALD | 🔴 |
| T-05 | NFP | ≥+200K ×3 consecutive (revised series) | FORGE — **Kill A** trigger for bearish labor theses | 🔴 |
| T-06 | NFP + slack | **NFP <100K AND (U-3 rose ≥0.2pp OR EPOP fell ≥0.3pp over 3 months)** *(re-specced 2026-08-07, BD-15)*. The OR-leg exists because the U-3 leg alone was **blocked two consecutive months** (Jul-2 +57K and Aug-7 −23K, U-3 falling both times on a shrinking labour force). Base **12.1%**, in-rec **71.0%**, out **7.6%** = **+63.3pp** — strictly better than the old spec's 7.8% / 54.8% / 4.2% / +50.7pp on capture **and** separation | CARL, REGINALD, HENRY | 🟠 |
| T-07 | WARN pipeline | **a completed month with >50K employees affected** on LayoffAlert's monthly series (effective-date basis, 46 states, `[2ND]`), graded the following month *(re-specced 2026-10-28, Will — the old 'accel >50K/mo cumulative MoM' wording had no measurable source after 9/29; BD-36)* | CARL (consumer conversion), REGINALD (sector-specific) | 🟠 |
| T-08 | Healthcare NFP | net-negative print (aggregate, not hospital-only) | CARL (consumer discretionary), REGINALD (healthcare REIT exposure) | 🟠 |
| T-09 | AI-displacement (Challenger AI-cited %) | >40% sustained 2+ months | CARL, HENRY (tech employment concentration) | 🟠 |
| T-10 | JOLTS hire rate | sustained collapse <5.0M, 2+ months | CARL (hiring → income → spending), HENRY | 🟠 |
| T-11 | FL state UR | >5.0% or 5th consecutive monthly ↑ | CARL (FL consumer cliff), REGINALD (FL banks) | 🟠 |
| T-12 | Staffing canaries (RHI/KFRC/MAN) | sequential reversal back to YoY decline | PROME (regime shift) | 🟠 |
| T-13 | DOGE/federal NFP | <-25K single print OR cumulative >400K | REGINALD (EGBN DC exposure), CARL | 🟠 |
| T-14 | Hormuz hiring freeze (BRENT cross-check) | direct labor-transmission verified | CARL, HENRY | 🟠 |

*(No standing broadcast queue — each firing is routed fresh to WALTER. As of 2026-11-26 T-01, T-02, T-05 and T-06 have never fired; v2 freeze-thaw, which is not a T-number, fired 2026-11-06.)*

> **State notes (re-stamped 2026-11-26 on the 11/6 vintage):** T-05 Kill-A is **DORMANT** — 0 of 3 (Aug rev +186K, Sep rev +60K, Oct +165K; STATUS § EXIT RULES). *(7/24 note: RESET 7/2, revised run 214/148/129/57.)* T-12 mechanistic trigger lives in STATUS Vector 14 If-Falsified column, not §KEY THRESHOLDS. T-14 re-arms only on BRENT demand-destruction Path B per Vector 15 (price re-arm alone ≠ labor transmission).

---

## §2 — KELYA Position

**Position:** 🔒 **NONE — the KELYA $7.5P Aug 21 EXPIRED WORTHLESS on 2026-08-21.** KELYA closed **$17.09** that day (low $16.60; Yahoo daily bars, pulled 2026-09-29) ⇒ `17.09 − 7.50 = $9.59` out of the money. **No KELYA line in `FORGE/STATUS.md`** (broker-view reconcile 2026-09-27, to the Fri 9/25 close; `grep -i kely` = 0 rows). Premium lost / cost basis → FORGE, never restated here. *(Re-stated 2026-09-29 on DAEDALUS Staleness Sweep #5: this line named the expired contract as the live position for 39 days. The pre-expiry live-state text is preserved in git — `git log -p -- AGENTS/LABOR/TRADE.md`.)*

**Post-mortem ANSWERED 2026-11-26** (Will's word 15:40 ET): `domain/sources/2026-11-26_KELYA_POSTMORTEM.md` — the conflation was inferable at entry: the canonical BLS temp-help series was `−2.33%` YoY on the day LAB-01 was registered against a `<−6%` line, and `−3.38%` on the 3/6 data, not the `−12%` the dashboard carried. *Was:* the post-mortem question (*was the entry sound on the Mar-7 data, or was the company-vs-industry conflation already inferable?*) — unanswered since 8/21. Carried in STATUS PICKUP; no new position is implied by answering it.

**Archived 2026-11-26:** the thesis state, verdict, re-arm conditions, decision triggers, lessons and the whole §3 Jun–Aug catalyst playbook moved verbatim to `domain/sources/TRADE_archive_20261126.md`. **BD-14** (§3 grids unenumerated) is discharged by the removal.


---

## §4 — What this file does NOT cover

Per `[[finding_outside_this_rail_disclosure]]`:

- **Other-agents' positions** (KRE/WAL/OZK/HYG/IWM/AAL/etc.) — position-level entry/exit triggers live with the position owner. LABOR sends the signal via §1; the owner decides.
- **Live KELYA contracts/cost basis/mark** — owned by FORGE per `[[feedback_position_cost_basis_not_authoritative]]`.
- **Cross-agent signal *delivery*** — signals route through WALTER (root `CLAUDE.md`; Direct Messaging v1 canon at `MESSAGING/`); no standing queue.
- **New position ideas** — none proposed in this rebuild. LABOR-direct trade scope ends at KELYA absent new structural break.
- **Hedging/repair structures on KELYA** — none; the position expired 2026-08-21.
