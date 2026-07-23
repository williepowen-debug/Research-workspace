# LABOR TRADE.md
**Generated:** 2026-06-09 | **Domain:** LABOR (input agent) | **Direct trade:** KELYA only
**Prior version:** `domain/sources/TRADE_archive_20260307.md`

**Purpose.** Two jobs: (1) index which LABOR signals transmit to which other agents, so cross-agent triggers are explicit; (2) own the KELYA position decision logic. **Live position state (contracts, cost basis, mark) lives in FORGE — this file does not duplicate it.** Cross-position triggers for KRE/WAL/OZK/HYG/etc. live with the position owner; LABOR sends the signal, FORGE/REGINALD/HENRY/CARL act on it.

**Anchor reads:**
- `STATUS.md` — current dashboard, convergence matrix, predictions, exit rules
- `LESSONS.md` L-01 — company-tier ≠ industry employment
- `docket/CATALYSTS.tsv` — forward catalyst source of truth
- auto-memory `[[feedback_prediction_canonical_measure]]`, `[[feedback_position_cost_basis_not_authoritative]]`

---

## §1 — Transmission Signal Index

LABOR vector → threshold → target agent(s) → priority. Thresholds reference STATUS § KEY THRESHOLDS; do not duplicate values here. When threshold fires: write `outbox/` signal per CLAUDE.md Outbox Protocol; append to `AGENTS/SIGNALS.md` if cross-agent.

| # | Vector | Threshold (fires signal) | Target agent(s) | Priority |
|---|---|---|---|---|
| T-01 | Initial claims | >250K sustained (4+ wk MA) | CARL, REGINALD | 🔴 |
| T-02 | Initial claims | >300K single print | REGINALD (all ORANGE banks → RED), HENRY | 🔴 |
| T-03 | U-3 | ≥4.7% Q2 | CARL, HENRY | 🟠 |
| T-04 | U-3 | ≥5.0% | HENRY (structural bid break), REGINALD | 🔴 |
| T-05 | NFP | ≥+200K ×3 consecutive (revised series) | FORGE — **Kill A** trigger for bearish labor theses | 🔴 |
| T-06 | NFP | <100K single print + ≥0.2pp U-3 jump | CARL, REGINALD, HENRY | 🟠 |
| T-07 | WARN pipeline | accel >50K/mo cumulative MoM | CARL (consumer conversion), REGINALD (sector-specific) | 🟠 |
| T-08 | Healthcare NFP | net-negative print (aggregate, not hospital-only) | CARL (consumer discretionary), REGINALD (healthcare REIT exposure) | 🟠 |
| T-09 | AI-displacement (Challenger AI-cited %) | >40% sustained 2+ months | CARL, HENRY (tech employment concentration) | 🟠 |
| T-10 | JOLTS hire rate | sustained collapse <5.0M, 2+ months | CARL (hiring → income → spending), HENRY | 🟠 |
| T-11 | FL state UR | >5.0% or 5th consecutive monthly ↑ | CARL (FL consumer cliff), REGINALD (FL banks) | 🟠 |
| T-12 | Staffing canaries (RHI/KFRC/MAN) | sequential reversal back to YoY decline | PROME (regime shift) | 🟠 |
| T-13 | DOGE/federal NFP | <-25K single print OR cumulative >400K | REGINALD (EGBN DC exposure), CARL | 🟠 |
| T-14 | Hormuz hiring freeze (BRENT cross-check) | direct labor-transmission verified | CARL, HENRY | 🟠 |

*(No standing broadcast queue — the Transmission Index above fires fresh outbox signals on trigger, e.g. Jun 18 >250K → T-01; Jul 2 NFP → T-05/T-06.)*

---

## §2 — KELYA Position

**Position:** KELYA $7.5P Aug 21
**Live state (refreshed 7/23):** spot **$15.23** (−1.10%) [CONF fetch.py 7/23]; strike $7.5 = **$7.73 OTM**; **29 DTE**. **✅ DTE ≤30 MECHANICAL CHECKPOINT FIRED 7/23** (due 7/22, graded first session after): spot $15.23 ≫ $10 → **write-off confirmed per the pre-registered trigger — stop spending attention.** No action proposed to Will (tax-loss close only if mark >$0.05, implausible at $7.73 OTM / 29 DTE; would need a live chain quote to verify). Next mechanical touch: Aug 21 expiry + post-mortem (§2 "what this taught us" open question). Contracts / cost basis / mark → FORGE. *(Prior marks: $13.44 Jul 9 / $13.00 Jul 2 / $11.65 Jun 9.)*

### Thesis state

**What we got right.** KELYA Q1 (May 7) confirmed company-tier weakness: revenue $1.041B (-10.7% YoY, MISS), Non-GAAP EPS $0.03 (MISS vs $0.0755), basic LOSS $0.17, adj SG&A -10.3% (3rd straight ~10%+ quarter), no forward guidance. The "small/mid staffing cracking" read was correct at the company level.

**What we got wrong.** The market refused to price it bearishly. Tape framing: "smaller Q1 loss challenges bullish margin expansion narrative." Stock did not crater on the miss — it rallied to $11.65 (vs $9.50 stop, vs $7.5P strike).

**Why the trade decayed:**
1. **LAB-01 ❌ FALSIFIED Jun 2** — industry-tier temp-help is *expanding* (BLS CES TEMPHELPS +7.9K Apr; ASA index +4.9% YoY Apr). Company weakness (KELYA, RHI) ≠ industry employment direction. The bearish staffing-canary thesis the position rode is broken at the sector level. *(See LESSONS L-01 + auto-memory `[[feedback_prediction_canonical_measure]]`.)*
2. **Staffing canary reversal confirmed** — KFRC raised Q2 guidance, RHI 2nd consecutive sequential growth quarter (May 4 STATUS). Sector is bottoming, not accelerating lower.
3. **Hard data revising UP** — NFP May +172K beat with **net +93K upward revisions** (Apr 115K→179K, Mar→214K). Realization-weakness leg on the back foot; Kill A (NFP ≥200K ×3) now has Mar across the line.
4. **Time decay** — 73 DTE on a $4.15 OTM put requires >35% drawdown in <2.5 months. Implied required move not supported by current vol or thesis state.

### Verdict: **Functionally dead. Manage to expiry.**

> **Jul-2 print resolution (added 2026-07-02):** The §2 re-arm letter *technically fired* — NFP June +57K (<100K ✓) AND revisions stopped trending up (reversed to net −74K ✓). But the third leg the grid assumed never came: **U-3 FELL to 4.2%** (labor force −720K = supply-shrink artifact, not strength), and the market shrugged (KELYA $13.00, −0.84%; spot moved *away* from the strike vs the "$9-10 on print" re-arm scenario). Mechanism read: freeze-deepening, not demand-break — no claims confirmation (215K). **Verdict unchanged: write-off; no action proposed to Will.** The playbook's Jul-2 grid lacked a "NFP <100K + U-3 ↓ (participation-driven)" branch — gap documented in LESSONS L-06; future grids carry a denominator-artifact branch.

**Re-arm conditions** (would restore the put's edge — none currently active):
- Initial claims breach **>250K sustained 4+ weeks** + U-3 jump ≥0.2pp single print → would force fundamental re-rating
- NFP June **<100K** AND headline revisions stop trending up → revives realization-weakness leg
- Sector-wide staffing reversal (RHI/KFRC guide-DOWN Q2 update) → kills the canary-bottomed narrative

### Decision triggers to Aug 21

| Trigger | Action |
|---|---|
| **Claims w/e Jun 6 (Jun 11) >250K** | First re-arm signal. Re-evaluate position vs current mark; if mark <$0.05 likely too late to act. |
| **Claims w/e Jun 13/20 also >250K** | Sustained-breach threshold. If KELYA <$10 on the print, may have brief window — coordinate w/ Will, decision binary (close or hold). |
| **JOLTS May (Jun 30)** | If hires sub-5.0M confirms, supports LAB-16 but doesn't move KELYA alone — needs claims breach companion. |
| **NFP June (Jul 2) <100K + U-3 ≥4.5%** | Full re-arm. KELYA likely $9-10 range on print. Decision binary: hold to Aug or close green. |
| **NFP June (Jul 2) ≥200K** | Kill A trigger #2 (Mar #1). Position confirmed dead. Mechanical: hold to expiry (premium fully gone) or close for tax-loss harvest if mark > $0.05. |
| **DTE ≤30 (Jul 22) + spot >$10** | Mechanical write-off. Stop spending attention on the position. |
| **Aug 21 expiry** | Position expires worthless absent a >35% KELYA drawdown in the interim. |

### What this position taught us
- Captured in `LESSONS.md` L-01: company-tier reads ≠ industry employment series; always pull canonical industry series for prediction calibration.
- Captured in auto-memory `[[feedback_prediction_canonical_measure]]` (transferable across agents).
- Open question for post-mortem at expiry: was the original entry sound at the time given Mar 7 data state, or was the company/industry conflation already inferable then? *(Not for this rebuild — flag for post-expiry review.)*

---

## §3 — Forward Catalyst Playbook

For each forward catalyst, the LABOR thesis implication + KELYA position implication + which cross-agent signals fire. Source of truth: `docket/CATALYSTS.tsv` — keep this section synced with the docket at every catalyst closeout.

### Jun 11 (Thu) — Initial Claims w/e Jun 6

| Print | LABOR thesis read | KELYA implication | Cross-agent signal |
|---|---|---|---|
| <215K | Drift stalled; realization-weak leg further weakens | Position confirmed dead — manage to expiry | None |
| 215-230K | Drift continuing per recent pattern; no new info | No change | None |
| 230-250K | Drift accelerating; upgrade Claims/shadow vector | Marginal — needs companion U-3 catalyst | Watch list to CARL/REGINALD |
| **>250K** | **T-01 fires.** Sustained-breach watch begins. | First KELYA re-arm signal | 🔴 CARL, REGINALD |

### Jun 23 (Tue) — BLS State Employment May (FL focus)

| Print | LABOR thesis read | KELYA implication | Cross-agent signal |
|---|---|---|---|
| FL <4.8% | State divergence stalls; bear leg weakens | No change | None |
| FL 4.8-5.0% | 5th consecutive ↑ if 4.9%; trajectory intact | No direct (FL exposure mid for KELYA) | Watch CARL |
| **FL ≥5.0%** | **T-11 fires.** FL UI cliff thesis activates | Indirect — small/mid staffing FL exposure | 🟠 CARL, REGINALD |

### Jun 30 (Tue) — JOLTS May

| Print | LABOR thesis read | KELYA implication | Cross-agent signal |
|---|---|---|---|
| Openings revise Apr down + May <7.0M | Apr 7.6M was noise; post-don't-hire wobbles | Mildly bullish position (hiring weakens) but small | Watch CARL |
| Openings 7.0-7.5M + hires <5.0M | LAB-16 ✅ confirmed: post-don't-hire persists | Supports KELYA thesis but doesn't move alone | T-10 watch |
| Openings >7.5M + hires <5.0M | Post-don't-hire intensifies | Marginal KELYA support | 🟠 CARL, HENRY |
| Hires recover >5.5M | Post-don't-hire wobble; canary-bottomed thesis confirmed | Position confirmed dead | None |

> **✅ RESOLVED Jun 30 (graded Jul 2):** printed **between the grid's rows** — openings 7.594M (>7.5M) but hires 5.170M (5.0-5.5M band, not <5.0M). Read: post-don't-hire GAP widened (LAB-16 ✅ with stabilization nuance; Apr hires revised UP +99K to 5.215M). No cross-agent fire (T-10 needs <5.0M ×2). KELYA: no move.

### Jul 2 (Thu) — NFP June + U-3 + Claims w/e Jun 27 ⚠️ **LINCHPIN**

LAB-02 effective resolution. Kill A check #2 (Mar revised 214K = #1).

| Print | LABOR thesis read | KELYA implication | Cross-agent signal |
|---|---|---|---|
| **NFP <100K + U-3 ≥4.5%** | Realization-weak leg revives; T-06 fires | **Full KELYA re-arm.** Spot likely $9-10. Binary: hold to Aug or close green. | 🟠 CARL, REGINALD, HENRY |
| NFP 100-150K + U-3 flat | Soft but not breaking; status quo | No change | None |
| NFP 150-200K + U-3 flat | Hard-data strength continues | Position confirmed dead | None |
| **NFP ≥200K** | **Kill A trigger #2** (Mar = #1). Bearish realization-weak thesis on the rocks. | Position confirmed dead. | 🔴 PROME, FORGE — Kill A countdown |
| U-3 ≥4.7% regardless of NFP | LAB-02 ✅ confirmed | Supports KELYA but NFP dominates tape reaction | Watch HENRY |

> **✅ RESOLVED Jul 2:** printed **off-grid** — NFP **+57K** (<100K) but **U-3 4.2% DOWN** (participation −0.3pp = supply artifact; the grid's <100K row assumed U-3 ≥4.5%). T-06 did NOT fire (needs a U-3 *jump*). Revisions net **−74K** → **Kill A RESET** (revised run 148/129/57 — zero of three; the Mar-214K "count #1" no longer heads a live streak). LAB-02 ❌ formally. Claims same-morning 215K = no realization confirmation. KELYA $13.00 shrug → §2 verdict stands. Missing-branch gap → L-06.

### Jul 6 (Mon, modeled) — ISM Services PMI June

| Print | LABOR thesis read | KELYA implication |
|---|---|---|
| Svs employment <47 (4th mo) | Realization catching up to announcements | Modest KELYA re-arm if accompanied by claims drift |
| Svs employment ≥48 | Contraction stalling | No change |

### Aug 7 (Fri, modeled) — NFP July

**Kill A check #1 of a FRESH streak** *(renumbered Jul 2 — the Mar-214K-led streak died with the June report's −74K revisions; revised run 148/129/57 = zero banked; see §3 Jul-2 resolution)*. A ≥200K July print = first count only; trigger still needs 3 consecutive. KELYA already at ~14 DTE; mechanical write-off zone unless re-armed earlier.

### Aug 21 (Thu) — KELYA Expiry

Mechanical close-out. Decision tree:
- Spot >$8.50: expires worthless, position closed.
- Spot $7.50-8.50: marginal ITM/ATM, evaluate close-vs-let-expire for capital efficiency.
- Spot <$7.50: ITM, exercise/close per FORGE rules.

---

## §4 — What this file does NOT cover

Per `[[finding_outside_this_rail_disclosure]]`:

- **Other-agents' positions** (KRE/WAL/OZK/HYG/IWM/AAL/etc.) — position-level entry/exit triggers live with the position owner. LABOR sends the signal via §1; the owner decides.
- **Live KELYA contracts/cost basis/mark** — owned by FORGE per `[[feedback_position_cost_basis_not_authoritative]]`.
- **Cross-agent signal *delivery*** — messaging system in flight per `[[project_messaging_overhaul]]`; §1 Transmission Index fires fresh outbox signals on trigger (no standing queue).
- **New position ideas** — none proposed in this rebuild. LABOR-direct trade scope ends at KELYA absent new structural break.
- **Hedging/repair structures on KELYA** — out of scope; position is functionally dead, not a candidate for roll/cover.
