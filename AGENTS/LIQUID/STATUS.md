# LIQUID STATUS
**Last Updated:** 2026-06-26 | **Agent:** LIQUID | **Status:** 🟠 **Credit-bear ARMED — pre-trigger, entry-gated, NOT shelved.** The kill is dead, the bear is not.

> **No live levels in this file.** Run `scripts/boot.py` (3-dashboard live sweep — Credit / Domestic / Foreign) for every current price/spread/yield; it classifies against the same thresholds referenced here. State files carry *posture and pointers*, not quotes (they rot). HY OAS is auto-watched between sessions by `scripts/hy_oas_watch.py` (systemd timer; alerts → `alerts/HY_OAS_ALERTS.log`).

*Domain: financial plumbing — repo/funding rates, credit spreads, public-BDC mark catch-down, foreign Treasury demand, dealer capacity, basis trade. Watches transmission in from BOND (curve), SAM (Japan repat), HAWK/BRENT (oil-CPI loop).*

---

## Current State (posture, not levels)

- **Credit-bear timing = ARMED** — pre-trigger, entry-gated on the X1 conjunction (HY OAS >280 sustained **AND** wrapper-basket-leads-managers-down). Thesis LIVE and substance firming; never frame as "paused" (KB-LIQ-063).
- **Soft-kill receded** — HY OAS backed up off the June one-print low; the <260 ×2-closes kill (Trigger A) is broken/reset, off the near-term table. Re-arms only on two fresh sub-265 closes. The shared 🔴-ALL kill (LIQUID/BROCK/REGINALD/NEXUS) is OFF the table.
- **The widening is risk-off BETA, not yet credit-substance recognition** — discriminator is CCC leading + the public wrapper basket breaking its floor *with* the index (KB-LIQ-062). Until both X1 halves fire, the bear root stays SINGLE (macro/carry-unwind), not bifurcated into an independent PC-credit root.
- **Surviving load-bearing root = the CCC-BB tail-gap pin** (KB-LIQ-058; NEXUS R3 falsifier = gap <~400, nowhere near). Calm-senior / wide-tail signature visible across HY index + European CLO 2.0 (first rated-tranche default) + govvie term premium.
- **Substance firming beneath a calm headline** (BROCK): record-match broad-index default rate, BDC Q1 non-accruals up, div cuts, wrapper-equity recognition leaking. Candidate PC→public transmission (alts/PC equity crack) is DEEPENING.
- **Funding plumbing CLEAN** — SOFR-IORB negative, SRF unused, reserves above floor, RRP at structural-zero (quarter-end choppiness ≠ re-activation). No funding stress.
- **Positions: FLAT of LIQUID single-names.** HYG put expired worthless 6/19 as planned (do NOT re-surface); TEN closed (winner); APO Dec $95P is BROCK-owned. No LIQUID position action is gated on the kill — it is a *thesis* event, not a position event.

> **X1 / kill — canonical definitions live in `workbook/KILL_MEMO_HY_OAS_260.md`** (two-sided trigger ladder + the X1 conjunction + APO co-trigger) and **KB-LIQ-062** (the beta-vs-substance principle). Do not restate the ladder here — reference those.

---

## Triggers & Thresholds (durable reference — live levels → `scripts/boot.py`)

| Metric | Threshold / line | Owner |
|--------|------------------|-------|
| **HY OAS** | <260 kill (×2 closes) · 265–280 approach · **>280 X1-decoupling (LIQUID half)** · >320 confirm · 350 freeze | LIQUID — ladder in KILL_MEMO |
| **CCC-BB tail-gap** | NEXUS R3 falsifier <~400 (pin = wide) | LIQUID / NEXUS |
| HY Energy OAS | >300 energy-credit trip — **structurally unavailable on free FRED** (paid ICE sub-index); reason, don't fabricate | LIQUID |
| APO co-trigger | broke <$130 = alts-crack deepening (the old >$130-recovery framing is moot; KILL_MEMO) | BROCK |
| BIZD | $12.50 mark-stress line | LIQUID / BROCK |
| VIX | >25 (>23 = HENRY cascade) | HENRY |
| SOFR / SOFR-IORB | SOFR >3.70 · IORB spread sustained >0 = funding stress | LIQUID |
| 10Y / 30Y / 2Y | 10Y >4.50 sustained · 30Y >5.00 re-establish / <4.90 unwind · 2Y front-end tell | LIQUID / BOND |
| RRP / SRF / Reserves | RRP sustained >$10B into July · SRF >$50B · reserves <$2.8T (canonical WRESBAL, **not** FFIEC) | LIQUID |
| USD/JPY | >160 (triggered on level; repat pushed to Sep tail) | SAM |
| Auction indirect | <55% sustained = demand break | LIQUID / BOND |

---

## Catalyst Calendar (dates → `workbook/CATALYSTS.tsv`; live countdown in boot.py)

| Window | Event |
|--------|-------|
| **~Jun 30** | LIQ-03 resolves (CLO AAA vs SOFR+160); BCRED Q2 redemption window; Cliffwater CDLI Q1 NAV; quarter-end (RRP revert + JPM rebalance) |
| **~Jul 3** | 2nd PE-wrapper gate watch (clean close de-escalates) |
| **~Jul 14** | June CPI — HENRY inverse-feedback re-fire test |
| **~Jul 25** | Q2 BDC marks — NEXUS R3 credit-bifurcation transmission test |
| **~Jul 29** | July FOMC — hike watch (modal hike ~Q4) |
| **YE2026** | Warsh balance-sheet review outcome (QT pace / SRF / RRP / SOMA — Leg A buffers) |

---

## Active Playbooks / Monitors

| File | Purpose |
|------|---------|
| `workbook/KILL_MEMO_HY_OAS_260.md` | Canonical two-sided HY OAS trigger ladder + X1 conjunction — live until thesis reframed |
| `workbook/BDC_MARK_CONVERGENCE_MONITOR.md` | Public-BDC mark watch; ~7/25 Q2 marks = NEXUS transmission test |
| `workbook/AUCTION_FRAMEWORK.md` · `workbook/TIC_FRAMEWORK.md` | Foreign-demand / auction-bid reference |
| `scripts/hy_oas_watch.py` | Unattended HY OAS X1/kill watcher (systemd timer; alerts/ surface) |

---

## Open Monitors (qualitative — detail in MEMORY session notes + owners)

- **Athene FABN funding canary** (SHADE owns mechanism; LIQUID owns broad funding/spread confirm) — issuance-freeze + widening penalty + forced encumbered substitution = margin compression on the PC funding engine. Disorderly-failure tail YELLOW; "refinanceable ≠ healthy."
- **USD/JPY repat** (SAM) — triggered on level, carry window locked to a Sep tail; near-term leg downgraded.
- **Warsh balance-sheet review** — QT/SRF/RRP/SOMA "back in play" → thinner future buffers (Leg A); multi-quarter watch.
- **Excess-liquidity "negative first since 2021"** — VALIDATED as NOT a live bear re-arm; only residue = RRP-buffer exhaustion → QT drains reserves directly (slow Leg-A mechanic).

---

## Durable Signals Log → `workbook/KB.tsv` (KB-LIQ-001..064)

Recent (full text in KB.tsv):
- **064** — accumulating bear legs don't earn a conviction tick when the same window brings offsetting bear-negative macro AND the headline move is beta-not-substance.
- **063** — never frame the credit-bear / LIQUID as "paused"; correct frame = ARMED (entry-gated, actively accumulating data).
- **062** — a spread widening *away* from a kill is not a bear-confirm; separate risk-off beta from credit-substance recognition. X1 = wrapper-leads (BROCK) **AND** HY>280 (LIQUID) conjunction.
- **061** — a spread approaching a kill that bounces is not a kill; read the tail, not the headline.
- **060** — a credible-hawkish Fed can RALLY the long end (hawkish dots hit the front end, not the term premium).
- **058** — aggregate HY masks sector/quality bifurcation (the CCC-BB tail).

For pre-KB history see git + `archive/status_snapshots/`. POV-arc → `thesis/CHANGELOG.md` § POV Pivots.
