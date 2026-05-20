# LIQUID STATUS
**Last Updated:** 2026-05-20 (post-20Y auction) | **Agent:** LIQUID | **Status:** 🟠 **CREDIT THESIS REASSESSMENT TRIGGER FIRED (APO >$130 ×9 sessions, 5/8→5/20)**; HY OAS 286bps (+6 daily, 26bps above 260 kill — cushion widening); 5/20 20Y auction printed soft-but-functional, NO foreign-demand-crisis (indirect 67.7%, tail 0bp); ACTIVE CHANNEL refined: term-premium digestion, not broken auction mechanism (KB-LIQ-057)

---

## Thesis-Kill Proximity (5/20)

**HY OAS 286bps. Kill 260 (HEARTBEAT line 80). Cushion: 26bps** (widening; closest-of-cycle was 276 on 5/17 = 16bps).

**APO co-trigger live since 5/12** (~Day 9 today, 5/8 → 5/20 inclusive). HEARTBEAT line 80 reassessment trigger fired but HY OAS-260 kill not breached. Per `workbook/KILL_MEMO_HY_OAS_260.md`: APO co-trigger alongside HY OAS compression = treat as Trigger C even if HY OAS doesn't hit 260. **Open framing question:** "thesis grinding but intact via duration channel" vs "thesis on life support, kill-memo-Trigger-C de-facto already." POSITIONS read is the gate.

POV-arc for how we got here: see `thesis/CHANGELOG.md` § POV Pivots (5/20, 5/19, 5/18).

---

## May 20 — 20Y Auction Result + Live Tape (BOND-sourced; HERMES sweep pending)

**5/20 20Y NEW issue ($16B, coupon 5.000%, CUSIP 912810UV8, 1pm ET takedown) — printed soft-but-functional, NO orange trigger fired.**

| Metric | Print | LIQUID threshold (CALENDAR) | BOND grading | Reading |
|---|---:|---|---|---|
| BTC | 2.55 | n/a | soft band (clean ≥2.60) | Just below clean |
| **Indirect** | **67.7%** | <55% = 🟠-to-ALL | clean (≥58%) | **STRONG** — foreign demand showed up at price |
| Dealer | 9.4% | n/a | clean (≤10%) | Near 4/22 baseline 8.6% |
| **Tail** | **0bp** (stopped on screws) | >+2bps = 🟠-to-ALL | clean | Confirmed via ZH ~3:25pm ET (single-source) |

**Implication for v2 Leg B (FOI demand hole):** The foreign-demand-canary reading of the 5/13-5/19 long-end break is **disproved by this print**. Foreign demand showed up at price. This sharpens the read: **term-premium digestion** (expensive), not **broken auction mechanism** (failed). HY OAS drifted +3bp to 286; not transmission-grade. Credit cascade thesis still inactive.

**Tape relief consistent with non-orange print:** TLT $83.01 → $83.89 (+$0.88), VIX 17.99 → 17.47, KRE 🟡→🟢.

**5/21 10Y reopening (Leg 2) tomorrow.** BOND posterior on bad print fell ~35-40% → ~20-25%. Aggressive-add gate (two tails in 24h) now closed since Leg 1 didn't tail.

**SOFR-IORB at -12bps (BOND 5/19 fresh, vs my STATUS -10bps).** My read: consistent with ample-reserves-absorbing-supply, not stress-not-yet-funded. Rationale: (a) SRF flat, (b) RRP structurally zero so no buffer to drain, (c) plumbing channel resolved per KB-LIQ-051, (d) today's strong indirect confirms demand exists at price — pre-auction plumbing stress would show as SOFR jump on settlement-week funding, not SOFR-IORB drift more negative. Replying to BOND via outbox.

---

## May 19 Live Re-Verification

> *Dashboard run 2026-05-19 12:24 UTC (08:24 ET) via `FORGE/tools/market-data/dashboard.py`. Pass-through 5/18 numbers from Prome confirmed accurate; deltas below are 5/18→5/19 unless noted.*

| Metric | 5/19 Live | 5/18 (Prome) | Daily Δ | Reading |
|---|---|---|---|---|
| HY OAS | 280bps | 280 | +4 | 🟢 — but compression run + APO co-trigger flips read |
| CCC OAS | 935 | 935 | +13 | 🟡 — quality bifurcation widening |
| SOFR | 3.55% | 3.55 | -0.01 | 🟢 normalized |
| SOFR-IORB | -10bps | -10 | -1 | 🟢 plumbing channel resolved |
| 10Y | 4.59% | 4.59 | **+12bps daily** | 🔴 **acute duration move** |
| TLT | $83.56 | $83.56 | flat | 🔴 confirms |
| Brent | **$110.59** | $109.30 | +$1.29 | 🔴 reflation continuing — April CPI loop hot |
| USD/JPY | **159.10** | 158.83 | +0.27 | 🔴 now 0.90 from 160 trigger |
| VIX | 18.03 | 17.82 | +0.21 | 🟡 gamma-suppression hypothesis still live |
| KRE | $67.92 | 67.92 | flat | 🟡 REGINALD-domain |
| BIZD | $12.52 | 12.52 | flat | 🔴 mark stress confirmed via FSK NAV -9.9% |
| **APO** | **$134.07** | — | — | **🚨 Day 7 of >$130** (5/8: $133.20, 5/15: $135.52 peak) |
| ARES | $123.70 | — | — | 🟡 BROCK-domain |
| FXY | $57.80 | — | — | 🟡 SAM-domain |
| Initial Claims | 211k (266k shadow) | — | — | 🟢 not labor-break |
| Cont Claims | 1.782M | — | — | +24k weekly |
| Gas (wkly) | $4.50 | — | — | 🔴 +$0.05 |
| CP-TBill | 0.12 | 0.12 | flat | 🟢 plumbing clean |

**Dashboard summary:** 🔴 CRITICAL (score 10) — 6🔴 / 7🟡 / 7🟢.

> **Intra-day update (2026-05-19 13:23 UTC / 09:23 ET):** Yields extending higher across the curve. **30Y 5.168% — FRESH LIFE-OF-CYCLE HIGH** (vs 5.046 May 5 print, first since 2007; today's print is +12bps above that and still climbing). 10Y 4.647 (+24bps day, +40bps month). 5Y 4.301 (+21bps day). Whole curve at 1mo highs; roughly parallel bear move. Confirms "more days like 5/18 +12bps possible" risk flagged in morning re-verify. **Duration channel intensifying intra-session.** Updated in THESIS v2.0 §3 Leg B and §4 transmission map.

**Two reads that changed since revival pass-through:**
1. **APO trigger was already fired (Day 7), not pending.** This is the key finding from live re-verification. The reassessment HEARTBEAT-grade trigger has been live for ~6 sessions without LIQUID acknowledging it. POSITIONS read is gating action.
2. **10Y +12bps in a single session (5/18)** = acute, not chronic. Duration channel is repricing in real time, not just grinding wider.

---

## May 18 Revival Read (32-day gap)

**Active transmission channel migrated PLUMBING → DURATION over the gap.** Apr 16 LIQUID watched SOFR-IORB for the next leg. The next leg fired through 10Y / TLT / Brent-reflation instead:

- 10Y: 4.29 → 4.59 (+30bps over 32d, with +12bps acute on 5/18) — duration regime broke wide
- TLT: $86.28 → $83.56 (-$2.72) — confirms
- Brent: $98.20 → $110.59 (+$12) — reignites April-CPI loop, keeps 30Y >5% / 10Y >4.5% narrative durable
- HY OAS: 285 → 280 (-5bps; grinding tighter then reversed Monday) — but APO bull divergence loud
- CCC OAS: 924 → 935 (+11bps) — quality bifurcation re-igniting (still 65bps from 1000 trigger)
- SOFR-IORB: +7 → -10 (April +7bps breach **resolved mechanical** — tax-day TGA build, not structural leak)
- BIZD: $12.96 → $12.52 — mark stress confirmed via FSK Q1 NAV -9.9%
- USD/JPY: 159.18 → 159.10 (trigger 160 still 0.90 away; SAM-domain)
- KRE: $68.78 → $67.92 (REGINALD-domain, weaker bank tape)
- VIX: 17.90 → 18.03 (gamma/momentum suppression hypothesis live — per 5/14 signal)
- **APO: $120.81 → $134.07 (+11% over gap)** — public-equity PC sentiment fully recovered; co-trigger fires.

**Diagnostic:** The plumbing-leak hypothesis is falsified for the April episode. The bear thesis is *partially* transmitting through duration. The credit-spread component is under pressure from BOTH directions: HY OAS grinding near cycle tights AND APO co-trigger fired. Duration channel alive but credit-thesis reassessment is overdue.

---

*Apr 16 Refresh + Apr 16 Plumbing Dashboard pruned 5/20 (lived ~35 days). POV-arc preserved in `thesis/CHANGELOG.md` § POV Pivots 2026-04-10 + 2026-04-16. Findings preserved in KB-LIQ-051 (SOFR resolved mechanical) and KB-LIQ-052 (channel migration). Apr 14 external signals (IMF GFSR / TCW Red Lobster / GS HF whipsaw / SEC PDT) live in Durable Signals → KB.tsv lineage.*

---

## Thresholds (5/20 LIVE)

| Threshold | Level | Current | Status |
|-----------|-------|---------|--------|
| **HY OAS confirmation** | >320bps (LIQ-01) | 286 (5/20) | 🟢 34bps below |
| **HY OAS thesis-kill** | <260 sustained (HEARTBEAT) | 286 (5/20, +6 daily) | 🟢 26bps cushion (widening); closest 276 on 5/17 |
| **HY OAS freeze** | >350bps | 286 (5/20) | 🟢 64bps away |
| **APO co-trigger** | >$130 for 3 sessions (HEARTBEAT line 80) | $134 — Day 9 (5/8–5/20) | 🟠 **FIRED 5/12; reassessment overdue** |
| CCC OAS | >1000bps | 935 (5/19) | 🟢 65bps away — bifurcation widening but not at trigger |
| VIX | >25 | 17.47 (5/20 post-auction) | 🟢 Well below; gamma-suppression hypothesis live |
| **10Y duration regime** | >4.50% sustained | 4.59% (5/19; 4.647 intra-day) | 🔴 Broke wide; +12bps acute on 5/18; 30Y 5.168 fresh life-high 5/19 |
| **20Y Auction Indirect** | <55% sustained | 67.7% (5/20 NEW issue) | 🟢 Foreign demand STRONG — sharpens demand-hole read to "compresses price, doesn't break mechanism" (KB-LIQ-057) |
| USD/JPY | 160 | 159.10 (5/19) | 🟠 0.90 from trigger; SAM-domain co-watch |
| **SOFR** | >3.70 | 3.55% (5/18) | 🟢 Normalized |
| **SOFR-IORB** | sustained > 0 | -12bps (5/19 BOND) | 🟢 Resolved — April +7bps was tax-day mechanical (KB-LIQ-051); current drift = ample reserves absorbing supply |
| RRP buffer | >$5B | $0.158B (Apr 16) | 🔴 Structural zero |
| SRF usage | >$50B | TBD (need NY Fed) | — Check next refresh |
| Foreign CB UST | stable | $2.7T (lowest since 2012) | 🔴 Structural outflow |
| Reserve floor | >$2.8T | ~$3.0T | 🟡 Cushion intact but draining |

---

## Cross-Domain Signals (5/20)

- **APO Day 9 >$130 → BROCK, PROME (pending outbox):** HEARTBEAT-grade reassessment trigger live since 5/12. Public-equity PC sentiment fully re-absorbed Stage 3 narrative ($120 → $134 over 32d). Diverges with FSK NAV -9.9% and 2nd US bank failure 5/16. If BROCK still models Stage 4 transition 4-6 weeks, this argues *later, not earlier* timing.
- **10Y +12bps single-session (5/18) + 30Y 5.168 fresh life-high (5/19) → HENRY, REGINALD:** Acute duration move, not just gap-chronic. Brent reflation + CCC bifurcation widening = active leg of bear thesis.
- **USD/JPY 159.10 → SAM:** 0.90 from 160 trigger. Persistent creep; BOJ verbal-intervention risk rising. Watch April trade balance follow-through.
- **Brent $110.59 → HAWK, BRENT:** Continuing reflation, feeds April-CPI loop. Above $100 war-premium re-ignition watch.
- ✅ **SOFR-IORB read sent to BOND (5/20)** — `outbox/2026-05-20_to-BOND_sofr-iorb-ample-reserves-read.md`. 4-point cross-check favors ample-reserves-absorbing-supply over stress-not-yet-funded.
- ~~SOFR>IORB → RESOLVED MECHANICAL.~~ See KB-LIQ-051.

*Pending escalation outboxes to consider: BROCK on APO Day 9, HENRY on duration acute. Held until next session per Will direction.*

---

## Active Proposals (5/20)

**PROPOSAL 3 — CRUDE SHORT ON HOLD.** Hormuz/Dimona still active; Brent $110.59 (reflating).
**PROPOSAL 4 — HYG PUT REVIEW.** HYG $75P Jun x10 deep OTM. HY OAS 286 (vs 320 trigger; 26bps cushion above 260 kill, widening). Subject to KILL_MEMO trigger ladder; APO co-trigger fired Day 9. **Pending POSITIONS read + Will decision** — review for cut.
**PROPOSAL 5 — BCRED Q2 HARD GATE.** APO bull-recovery ($134 Day 9 of >$130) + FSK NAV -9.9% mark stress = mixed Stage 3/4 signal. Revisit on BCRED Q2 release window.

## Active Positions

| Position | Expiry | Thesis | Status (5/20) |
|----------|--------|--------|--------|
| TEN calls (Jun $30) | Jun 2026 | Triple premium | Dimona extends — hold |
| HYG $75P Jun x10 | Jun 2026 | LIQ-01 retest to 350 | **Thesis weakened.** APO co-trigger Day 9; HY OAS 26bps from 260 kill (cushion widening, not narrowing). Subject to kill-memo review. |

---

## Danger Windows + Watch (5/20)

| Window / Frequency | Risk |
|---|---|
| **Daily** | HY OAS 260 kill proximity (currently 26bps cushion, widening); APO co-trigger sustain (Day 9); 10Y/30Y duration regime extension; SOFR/SOFR-IORB stability |
| **This Week (May 20-23)** | ✅ 20Y auction (5/20, soft-but-functional, no orange); **5/21 10Y reopening (Leg 2, BOND-led — corroboration test for KB-LIQ-057)**; initial claims Thu 5/21; BDC Q1 continuation (OBDC/ARCC/BXSL/MAIN) |
| **Next Week (May 26-30)** | Memorial Day Mon 5/25; 2Y/5Y/7Y auctions Tue-Thu; April PCE Thu 5/28; FOMC May minutes (VERIFY) |
| **June** | NFP Fri 6/5; May CPI Wed 6/10; June FOMC Wed 6/17 (decision) — Warsh succession color, liquidity-facility language; May TIC (April flows) Thu 6/18; BCRED Q2 redemption window |
| **Powell → Warsh transition** | Policy continuity vs hawkish shift; intervention willingness collapse risk |

## Active Playbooks / Monitors

| File | Purpose | Active window |
|------|---------|---------------|
| `workbook/KILL_MEMO_HY_OAS_260.md` | Pre-written 1-pager: actions that fire when HY OAS <265 for 2 sessions OR <260 intraday | live until thesis reframed |
| `workbook/BDC_MARK_CONVERGENCE_MONITOR.md` | Public-BDC mark watch; TCW Red Lobster follow-through — checks my own "PC decelerating" narrative | rolling, Q1 BDC earnings active (FSK May NAV -9.9% in; OBDC etc. pending) |

---

## Durable Signals Log

All durable findings live in `workbook/KB.tsv` (57 entries, KB-LIQ-001 through KB-LIQ-057). Query that file for signal lineage. Notable recent anchors:
- **KB-LIQ-057** (5/20) — Foreign demand showed at price; term-premium digestion ≠ broken auction
- **KB-LIQ-052** (5/18) — Duration regime break May 2026; channel migrated PLUMBING → DURATION
- **KB-LIQ-051** (5/18) — April SOFR-IORB breach resolved mechanical (tax-day TGA)
- **KB-LIQ-053/054** (3/10, 3/11) — Stagflation trap structural / Financial hub transmission (4-path)
- **KB-LIQ-055/056** (2/11) — Foreign custodial flow disaggregation / Collateral velocity (Belgium/SIFMA)

For pre-KB historical entries (PC Stage 3 cadence: Barings/Blue Owl/FT-Stanger gates, MS $85B BD→bank, WFC $200B SPOF, Janus, Foreign CB UST trough, Goldman TRS pause) see git history of this file pre-5/20 OR earlier STATUS snapshots in `archive/status_snapshots/`.

---

*Domain: Financial plumbing — repo markets, funding rates, credit spreads, foreign Treasury demand, dealer capacity.*
