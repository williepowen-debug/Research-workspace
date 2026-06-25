# HEARTBEAT.md
**Updated:** 2026-06-25 ~12:40 ET (Claude Code Prome — Desktop CC origin; live-data refresh + do-now-batch synthesis)

## Regime

**Energy tail deflated; credit-bear PAUSED above the kill-line; the live transmission surface is bank-vs-private-credit — but MACRO, not yet credit-substance.** Resolved since the 6/21 read:

1. **Energy de-rated.** The Jun-20 Hormuz re-closure declaration resolved **non-kinetic** — Brent FELL ~8% to ~$74 (not the threatened spike); HAW-11 kinetic leg expired unfired 6/22. Cushing breached 20M (EIA 6/24) → **BRENT Boundary #3 fired** (WTI delivery/calendar dislocation). Energy is deflated on the tape but coiled (physically tight + near-record spec short); snap-back tail only if Brent sustains <$60 or the MOU collapses.
2. **Credit-bear PAUSED — not killed, not confirmed.** HY OAS **271 [6/23]** widened back ABOVE the <260 soft-kill (cushion doubled 5→11bp); LIQUID's two-closes-<265 Trigger A reset/broken. The "<260 kills the credit axis" scare is off — but 263→271 is risk-off *beta*, not credit-substance recognition; only faint quality dispersion (CCC ~2× HY) hints at the tail leading. **6/24 HY print due ~today** = held-or-reverted confirm.
3. **Bank-vs-PC divergence is MACRO multiple-compression, not credit recognition (yet).** Alt-managers (APO −11% cumulative, ARES) de-rated on higher-for-longer while wrappers (ARCC/FSK/OBDC/BIZD) held ~flat and banks (KRE/OZK/WAL) rallied. Today = pause, not acceleration.

**★ Convergence discipline (X1 — ratified by SAM + BROCK + LIQUID independently):** carry-unwind risk and PC-manager compression are **~1 root on macro/risk-off days — do NOT double-count** them as two bear confirmations. PC becomes a genuine independent bear root ONLY when the decoupling trigger fires: **wrapper basket LEADS managers down (BROCK's half) + HY OAS >280 sustained (LIQUID's half).** Both UNFIRED today (wrappers flat; HY 9bp short of 280) → root stays single/macro.

**May PCE (6/25):** firm (core 3.4% YoY) but as-priced — duration caught a bid, vol calm. Backward-looking; can't show the June energy washout yet. Real disinflation test = **June CPI (Jul 14)**. One-legged stagflation: rates/hawkish leg live, energy leg inverted.

**Carry:** USD/JPY 161.66 / FXY red — fuel loaded, no funding crunch. MOF silent 9+ days at 161+; intervention zone ~162–163 (SAM S1) — and intervention would PAY a long-FXY position (the convexity tail).

## Stress dashboard

**Live as of 2026-06-25 ~11:09 ET (markets open); [brackets] = FRED as-of. Refresh dashboard/FRED before re-citing as current.**

HY OAS **271🟢 [6/23]** *(+8 off 263; 11bp above <260 kill; 9bp below >280 trigger; 6/24 due)* · CCC **956🟡 [6/23]** *(CCC-BB tail-gap ~795)* · BB 161 · IG 74 · 10Y **~4.39🔴** *(bid; vs 4.50 [6/23])* · TLT **$87.50🟡** · VIX **18.43🟢** · Brent **$74.24🟢** *(−8% post-declaration)* · Cushing **<20M🔴** *(EIA 6/24 — Boundary #3)* · USD/JPY **161.66🔴** · FXY **$56.76🔴** · APO **$121.64🟡** *(from $137.50)* · ARES **$112.54🟡** · BIZD **$12.19🔴** · KRE **$74.57🟢** · OZK **$51.89🟢** · WAL **$81.35🟢** · Init claims **215k🟢 [6/20]** *(shadow-adj 270k)* · Cont claims **1.821M🟢 [6/13]** · SOFR-IORB **−0.03🟢 [6/24]** · CP-TBill **0.12🟢 [6/23]**

## Thresholds

Full definitions in `FORGE/tools/market-data/config.py`. The live trigger-lines right now:
- **HY OAS >280 sustained** — LIQUID's half of the X1/credit-recognition trigger (9bp away).
- **Wrapper basket (ARCC/FSK/OBDC/BIZD) leads managers down** — BROCK's half. **Both** must fire for PC to count as an independent bear root.
- **HY <260, two consecutive closes** — would re-kill the credit-bear axis; currently 11bp away, reset.

## HEARTBEAT Cadence / Ownership

**Approved Jun 4:** Prome owns `HEARTBEAT.md`. Update after Prome boot-surface refreshes, regime-level changes, or major decision-rail changes — not daily for hygiene.

## Near Gates — Jun 25 → Jul

| Date / Window | Gate | Owner(s) | Read |
|---|---|---|---|
| **~Today 6/25 EOD** | 6/24 HY OAS print | LIQUID/Prome | Does 271 hold or revert? Confirms the kill-line reset. |
| **Fri 6/26** | CFTC COT (Jun-16 data) | SAM/LIQUID | First post-MOU positioning; spec-yen-short extreme = unwind-vulnerability. |
| **Late Jun–early Jul** | MOF intervention watch (USD/JPY 162–163) | SAM | Rate-checks = pre-strike tell; intervention PAYS long-FXY. Speed not level. |
| **Thu 7/3** | June NFP (pulled forward) | LABOR/HENRY | Soft print accelerates growth-leg + inverse-feedback. |
| **Mon 7/14** | June CPI | HENRY/CARL/LIQUID | The real energy-washout / disinflation test (May PCE couldn't show it). |
| **~7/25+** | Q2 BDC / 10-Q marks | BROCK/CARL | Wrapper credit-substance recognition; the catalyst for the >280 + wrapper-leading trigger. |

## Blocking / Pending

| Pri | Decision / Work | Reference |
|---|---|---|
| 🔴 | **FXY position broker truth (Will).** Trim 13→6 fill unconfirmed; USD/JPY ~0.85 from the 162.5 stop. Hold-if-filled / trim-if-not; near-zone hard stop is a whipsaw trap. | `AGENTS/SAM/MOF_INTERVENTION_PLAYBOOK.md`, SAM STATUS |
| 🟠 | **HY>280 / wrapper-leading decoupling trigger.** The live bear-root watch; both halves unfired. | `AGENTS/BROCK/domain/sources/MACRO_VS_CREDIT_DISCRIMINATOR_JUN25.md`, LIQUID |
| 🟡 | **LIQUID energy-sector OAS** structurally unavailable from free FRED (paid sub-index); reasoned in-line-to-tighter unless Brent <$60. | LIQUID 6/25 |
| 🔵 | **NEXUS 9d-stale** — needs the X1 don't-double-count rule + regime delta; refresh deferred (Will hold). | `AGENTS/NEXUS/STATUS.md` |

## Pointers
- Operator card → `PROME/TODAY.md` · Working state → `PROME/SCRATCH.md` · Session synthesis → `PROME/synthesis/2026-06-25_donow_reconciliation.md`
- Agent state → `AGENTS/<NAME>/STATUS.md`

## Skip
Late night (11pm–8am ET): urgent only. Weekend: light monitoring.
