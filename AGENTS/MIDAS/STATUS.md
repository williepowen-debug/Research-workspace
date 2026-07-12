# MIDAS — STATUS

**Last Updated:** 2026-07-12 (first real session — `metals_watch.py` built + wired; first live baseline across all 4 channels) · **Status:** 🟡 monitoring (all 4 channels have live reads; nothing elevated; M1's framing corrected — see below)
**Class:** Market-agent (metals as macro tells: monetary + industrial) · **Spawnable by:** PROME or Will · **Maturity:** L2 (instrumented — spot/yield/GSR live via `metals_watch.py`; COT baseline established; LME inventory + PGM-supply confirmation still gaps)

> **All prices Fri 7/10 close (COMEX futures via yfinance) unless noted — metals markets closed weekend of 7/11-7/12, no weekend freshness claimed.** FRED DFII10 is T+1: latest available obs is 2026-07-09.

---

## HEADLINE CORRECTION (read this first)

The 7/11 build session characterized M1 as "gold's continued structural bid *despite* positive real yields" — a debasement premium — **without a live gold-spot pull** (STATUS explicitly flagged this as owed). This session's first live pull **does not support that framing**: over the trailing ~90 days, gold **fell** while real yields **rose** — the classic real-rate-consistent (inverse) relationship, not a divergence. See KB-MIDAS-005 and the M1 row below. This is the single most important finding of the session — M1's local state and score are revised accordingly. The Tier-2 structural debasement thesis (multi-year CB buying / de-dollarization, gold still nominally near all-time highs) is **untested by this pull**, not falsified — this is a Tier-1 (live-signal) read only.

---

## CONVERGENCE MATRIX (universal 5-pt + local state)

| # | Channel | Score (1–5) | Local state | Independence | Key signal [src, date] | Upgrade trigger |
|---|---|:---:|---|---|---|---|
| **M1** | Gold — debasement / real-rates | **2 🟡** | **CONVERGE** — gold -18.6% (90d, $5,052.50→$4,113.70) while DFII10 +36bp (1.95→2.31); real-rate-consistent, debasement premium NOT confirmed this window. Spec positioning still crowded net-long (52.2% of OI, CFTC 7/7) — the long hasn't capitulated | monetary root (shared w/ M2) | gold **$4,113.70** [GC=F, yfinance, 2026-07-10]; DFII10 **2.31** [FRED, 2026-07-09] | gold holds/rises through *further* real-yield increases, sustained 3+ sessions → 3; a NC-long capitulation (COT) alongside a break <$4k → different (liquidity-event) read, cross-flag LIQUID |
| **M2** | Silver + gold/silver ratio | **1 ⚪** | GSR **68.37** [computed, GC=F/SI=F, 2026-07-10] — comfortably below Yellow(85). Silver -18.4% same 90d window (correlated w/ gold, confirms monetary-root co-movement) | monetary root (shared w/ M1) + industrial overlap | GSR 68.37; silver $60.17 [SI=F, 2026-07-10] | GSR >85 sustained 3+ sessions → 2; >95 → 4 |
| **I1** | Copper — Dr. Copper / China | **1 ⚪** | Copper **+10.5% vs 200dma** ($6.28 vs $5.68), **+9.2% QoQ** ($5.75 4/9→$6.28 7/10) — growth-*confirming*, opposite of the roll/collapse threshold. LME inventory leg still a gap (no free API found) | industrial/China root | copper $6.28 [HG=F, 2026-07-10] | copper QoQ <-5% sustained → 2; China GDP miss (7/16) + copper -5%+ in 2 sessions → yellow trigger (MIDAS-04) |
| **I2** | PGMs (platinum/palladium) | **2 🟡** | Platinum $1,629.00 (+0.6%), Palladium $1,276.30 (+2.6%, 90d strength). Structural backdrop (PROVISIONAL, WebSearch — needs primary verify): WPIC ~240koz 2026 Pt deficit; SA power-cost + flooding constraints; US Commerce anti-dumping action on Russian Pd (rate unreconciled: 132.83% vs 828% cited by different sources/stages) | supply root (SA/Russia) | Pt $1,629 / Pd $1,276.30 [PL=F/PA=F, 2026-07-10] | confirmed major SA/Russia outage or finalized sanction determination → 4 |

**Composite: 6/20** *(M1 2 + M2 1 + I1 1 + I2 2). Down from the 7/11 provisional 9/20 — reflects the M1 correction (3→2) and the other three channels resolving to genuinely benign reads (2→1 for M2/I1) rather than "gap" placeholders. All 4 channels now carry a dated live read for the first time.*

**Independence note:** unchanged from 7/11 — a risk-off shock drives M1 (gold up) AND I1 (copper down) via the same macro root; count once. Right now the two channels are **not** co-moving that way: gold is *down* 90d while copper is *up* 90d — a "growth without a monetary flight-to-gold" read, not reflation (both up) or risk-off (gold up/copper down). Neither of THESIS.md's two named coherent-divergence cases quite fits; logged as a third state in KB-MIDAS-009.

---

## LIVE CHANNEL READS (sourced + dated)

- **M1 — Gold — debasement / real-rates**: gold **$4,113.70** [GC=F, yfinance, 2026-07-10 close]; DFII10 **2.31** [FRED, 2026-07-09]. 90d divergence check (monthly-marker verified, not a 2-point artifact): 3/19 gold $4,600.70 @ DFII10 1.88 → 4/15 $4,800.00 @ 1.90 → 5/15 $4,555.80 @ 2.10 → 6/15 $4,328.00 @ 2.15 → 7/9-10 $4,113.70 @ 2.31. Monotonic: yields up, gold down, every marker. **CONVERGE, not DIVERGE.** COT (CFTC Legacy Futures-Only, report date 2026-07-07, released 7/10): gold net noncommercial long **194,246 contracts (52.2% of 371,776 OI)**, +227 WoW — crowded long, not yet unwinding. **Gold-leg ownership CONFIRMED** for LIQUID's EndGame discriminator ("gold can't reclaim $4k"): live read $4,113.70, comfortably above $4k, leg **NOT fired** (consistent with LIQUID's 7/1 "EASED" read). Routes to BOND (real-yield level) + LIQUID (safe-haven / EndGame leg).
- **M2 — Silver + gold/silver ratio**: silver **$60.17** [SI=F, 2026-07-10]; GSR **68.37**, benign. COT: silver net NC long 28,015 ct (26.7% of 104,859 OI), +647 WoW. Routes to LIQUID.
- **I1 — Copper — Dr. Copper / China**: copper **$6.28/lb** [HG=F, 2026-07-10]; +10.5% vs 200dma ($5.682), +9.2% QoQ. COT: copper net NC long 64,272 ct (25.6% of 250,948 OI), -516 WoW (small de-risking, still net long). LME/COMEX inventory: **GAP** — no free public API found (CME `warehouseStockAPI.json` → 403; LME's stock-breakdown report is vendor-gated w/ 2-day lag). Cross-flag ZHAO (China demand) — China Q2 GDP due ~7/16 (NBS calendar), MIDAS-04 registered as the reaction-test resolver.
- **I2 — PGMs**: platinum **$1,629.00** [PL=F, 2026-07-10, +0.6%], palladium **$1,276.30** [PA=F, 2026-07-10, +2.6%]. Structural backdrop PROVISIONAL (KB-MIDAS-008) — needs primary-source verification (Federal Register / Commerce Dept determination, WPIC platinum quarterly) before treating as EMPIRICAL. Cross-flag HAWK (supply geopol).

**Inherited cross-agent context:** BOND owns the real-rate level MIDAS's M1 diverges (or, currently, does NOT diverge) from; ZHAO owns the China demand MIDAS's copper reads; LIQUID owns the EndGame liquidity-event discriminator whose gold leg MIDAS now confirms live.

---

## EXIT / INVALIDATION (standing-rule-vs-state triad)

| Channel | Standing rule | Current state @ level | FIRED? |
|---|---|---|---|
| M1 | gold up while real yields up, extreme + sustained (debasement premium) | gold **down** 18.6% while real yields **up** 36bp (90d) — the OPPOSITE pattern | **NOT-FIRED — trending toward the FALSIFICATION side of the bidirectional flip rule**, not the confirmation side |
| M2 | gold/silver ratio >95 sustained (risk-off) | GSR 68.37, well below Yellow(85) | NOT-FIRED |
| I1 | copper −20% AND LME inventory +100% (demand collapse) | copper **+9.2% QoQ** (opposite direction); LME inventory unmeasured | NOT-FIRED (and directionally opposite) |
| I2 | major SA/Russia PGM supply outage/sanction | structural deficit + sanctions proceeding ongoing, no confirmed acute outage | NOT-FIRED |

**Fired-count: 0 of 4.** **Thesis-kill vs channel-kill:** M1's CONVERGE read this session is **not** a thesis-kill — it's the live-signal (Tier-1) layer testing negative against the Tier-2 structural thesis, one data window. The bidirectional flip rule (below) says a *sustained* convergence would falsify the premium; one 90-day window is evidence, not yet a verdict. Re-test at MIDAS-03 (CPI 7/14 reaction) and again at MIDAS-01's 9/30 resolution.

**Cleanest bidirectional flip (BRENT discipline):** M1 — if gold sells off as real yields rise (converging), the debasement premium is falsified; if gold holds/rises through rising real yields, it's confirmed. **This session's read sits on the falsification side of that line for the trailing 90d** — flagged, not yet declared, pending sustained confirmation (see MIDAS-01/MIDAS-03).

---

## OPEN ON MIDAS (next session)

1. **LME/COMEX inventory (I1)** — no free API found this session (KB-010); try westmetall.com scrape or a signup-gated aggregator next.
2. **I2 primary-source verification** — reconcile the 132.83%/828% Russian-palladium tariff figures (Federal Register / Commerce Dept determination); verify WPIC 240koz platinum-deficit figure against the WPIC quarterly report directly (this session's read is WebSearch-summarized, PROVISIONAL).
3. **MIDAS-03 resolution (CPI 7/14)** — same-day gold-vs-real-yield sign check, resolves by 7/16 (DFII10 T+1 publish).
4. **MIDAS-04 resolution (China Q2 GDP ~7/16)** — verify exact NBS release date/time; copper 2-session reaction test, resolves by 7/20.
5. **CB gold-buying / WGC flow data (Tier-2 M1 structural leg)** — not pulled this session; still an assumption-tier fact in KB-MIDAS structural notes. Candidate for a quarterly-cadence pull, not daily.
6. **COT weekly-cadence wiring** — consider a lightweight weekly leg in `metals_watch.py` (or a separate weekly script) rather than the manual pull done this session.

---

## BOTTOM LINE

**MIDAS's first live baseline (2026-07-12) lands a correction, not a confirmation.** `metals_watch.py` is built and wired into `boot.py` (leg 0) — real yield, 5-metal spot (futures + ETF cross-check), GSR, and an M1 divergence classifier all run automatically now. The headline finding: the 7/11 build session's "gold structurally bid despite rising real yields" framing does **not** hold up against the actual data — over the trailing 90 days, gold is **down 18.6%** while real yields are **up 36bp**, the classic inverse (real-rate-consistent) relationship, verified across 5 monthly markers, not a two-point artifact. M1's score drops from 3 to 2 pending a sustained re-test (MIDAS-03 at the 7/14 CPI print, MIDAS-01 at 9/30). The industrial channel is comfortably benign and, if anything, growth-confirming: copper is +9.2% QoQ, +10.5% vs its 200dma — the opposite of a China-demand-collapse signal. PGMs show early structural-deficit + sanctions context (platinum ~240koz 2026 deficit, Russian palladium anti-dumping action) but that's PROVISIONAL pending primary-source verification. COT baseline established for all three (gold/silver/copper net noncommercial positioning, CFTC 7/7 report) — gold specs are still crowded net-long (52% of OI) despite the price decline, meaning the long hasn't capitulated yet; that's the thing to watch, not a fresh divergence claim. Next: verify I2 sources, close the LME-inventory gap, resolve MIDAS-03/04 against their catalyst dates.
