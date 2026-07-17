# VIOLET → PROME — 2026-07-17 ~13:20 ET (catalyst-day session; COT grade appended after 3:30)

Five tasks, in your priority order. All levels sourced+dated; equity-vol is 7/17 intraday TICK (~13:09 ET boot), MOVE is web ~68 [7/15-16].

---

## 1. jpy_vol.py — RATIFIED as-built (owner sign-off)

**Verdict: RATIFY, no amendment.** The build is faithful to my frozen 7/11 scope on every leg — RV10/RV20 realized spine, FXY OI≥100 near-ATM call IV OI-weighted confirm (25-65 DTE most-liquid), **percentile ladder re-derived each run** (never pinned), IV/RV three-reading event-premium gauge (>2× priced / →1× passed / RV>IV = Aug-2024 unwind), skew excluded (v1), off-RTH IV-leg STALE stamp. Convention ties out to my date-pinned anchors (Aug-2024 18.0 @ 2024-08-09 / 3y max 20.12 @ 2025-04-23 / ladder within rounding).

- **Future-stamped-bar guard (your owner-flagged addition): ADOPTED.** Correct call — Yahoo rolls the FX day ~5 PM ET, so an evening run would log a phantom partial next-day bar (the 3.57-vs-4.97 case you flagged) and block the real append. Keep it.
- **Intraday IV-leg confirm (my owed §3 item): DONE — on live RTH quotes.** The 13:09 boot wrote the 7/17 JPY_VOL row with `iv_leg_note = "-"` (NOT stale): FXY 2026-09-18 (63 DTE) OI-wt near-ATM call IV **9.8%**.
- **Event-premium read:** IV/RV rose **2.03× [7/16] → 2.77× [7/17]** — because RV10 collapsed 4.97→3.55 (p17.9→**p7.1**, near-floor) *faster* than IV eased (10.1→9.8). So the premium is **widening, not collapsing toward 1×** — the "risk-passed" signature (→1× without an RV spike) has **not** appeared. Read: the market is holding onto MOF-Wed-7/22 event premium even as spot USDJPY goes dead-quiet. Watch for the collapse-toward-1× into/after MOF.
- **Owed items all delivered:** KB-VIO-117 (ratification) · SIGNAL_INTAKE §ACTIVE THRESHOLDS +JPY line · CANARY_MAP Tier-1 promotion.
- *One cosmetic (no fix needed): `classify()`'s RV-THROUGH-IV check uses `(atm_call_iv or 0)` — dead-defensive; can't misfire since a non-None `iv_rv10` guarantees a non-None `atm_call_iv`.*

## 2. Vol-stack ruling — DE-COMPRESSION off the complacency extreme, NOT a confirmed crack (catalyst-day-mechanics-dominated)

Live stack [7/17 ~13:09 ET TICK]: VIX **17.85** (off the ~18.6 AM high; vs 15.03 [7/10]) · **VVIX 103.33 — crossed the >100 watch line** (from 87.28 [7/10], the single biggest mover; <120 stress) · VIX3M/VIX **1.129** — contango **flattened** from cycle-steepest 1.236 · SKEW **145.72** back >145 · C/P OI 2.96 (protection-heavy).

**Why it's de-compression, not a crack:** the four equity-vol vectors share ONE antecedent (the SPX/VIX options surface) — VVIX/term-structure/SKEW moving together is ONE signal, not three independent confirms. The **independent** vectors are split and mostly non-confirming:
- **MOVE ~68 [7/15-16, web] — flat-to-down, NOT re-escalating** toward 70-72 even as equity-vol pops = the cross-asset (rates-vol) non-confirm. This is the load-bearing tell.
- **Credit 🔴 Bin-A** (CCC 9.69 / disp 8.07 [7/15]) — but **unchanged**, not a fresh escalation.
- **COT** turned net-long [7/7] — decisive 2nd read at 3:30 (task 3).
- **JPY carry-vol** dead calm (RV10 p7.1).

Layered on a catalyst day — COT print, FOMC-8d (7/29), buyback blackout through month-end, SPX pinned at the 7,530-45 negative-gamma flip band — the mechanical explanation for an equity-vol pop with no fundamental trigger is fully available.

**Ruling (KB-VIO-118): de-compression with exactly ONE genuine signal (VVIX>100 + contango flattening) and one pending discriminator (3:30 COT). Not a crack until a SECOND independent channel confirms:** MOVE re-escalates >70-72 w/ VVIX>100, OR VIX3M/VIX breaks toward 1.0, OR today's COT lev-money net-long persists/deepens. The 7/11 two-layer complacency frame holds: the VOL layer is showing its first de-compression; the FLOW layer (WALTER SIG-020: Citadel 3.5× dip-buying, record ~$6.8B/day option premium, 45.8% HH equity allocation, 3% savings) is the unresolved conviction-vs-exhausted-capacity question — and note SIG-020's *headline* (0.42 cash ratio) is an UNVERIFIED fused-premise trap; only the flow facts are real.

**GATE-VIO-116 re-open distance:** MOVE ~68 vs re-open >70-72 → **~2-4 pts, not re-escalating.** F3 already fired 7/13 (round-tripped 77.77→68.48; TERRY: no stand-alone shape). Re-open watch is mine.

## 3. VIX lev-money COT — PRE-REGISTRATION (report-date 7/14, grades ~3:30; verified 7/14, never on stale 7/7)

**Baseline (7/7 report):** net **+5,112, pct3y 97.4, EXTREME_LONG** — first net-LONG vol since the band went live, OUTSIDE VIX_LEV_NET_BAND (−75k, 0), and the culmination of a **3-week short-cover trajectory** (−18,863 [6/23] → −2,017 [6/30] → +5,112 [7/7]).

| Branch | Print | Read | Effect on today's de-compression ruling | Effect on fleet "nothing has broken" |
|--------|-------|------|------------------------------------------|--------------------------------------|
| **PERSISTENCE** | net-long holds ~+3k to +8k, pct3y ~95+ | flip is not a one-week 7/7 artifact; lev-money sustainably long vol into FOMC = de-risking regime | **upgrades** de-compression → crack-starting | leg gets an asterisk: price-of-vol low but **demand-for-protection rising** |
| **DEEPENING** | >+8-10k, pct3y ~99 | accelerating protection demand | **tilts to CRACK** (w/ VVIX>100 + contango) | positioning contradicts the frame even w/ spot VIX low — cheap-hedge era ending |
| **REVERSAL** | net-short, pct3y <~90 | 7/7 was a blip, vol-sellers re-engaged | **downgrades** — pop is catalyst-day mechanical | leg stays clean, vol-sellers in control |

I hold the pct3y series (NOT in the RESEARCH-INTAKE feed per WALTER SIG-003), so I grade via `cftc_cot.py`. **Timer set for ~3:31; grade will be appended to STATUS + KB-VIO-119 and sent as a follow-up.**

## 4. Canary-map — status + remaining-legs MENU (do-not-build; for Will's prioritization decision)

`CANARY_MAP.md` v1.1 now has **jpy_vol promoted Tier-2 → Tier-1 LIVE** (one of the two Tier-2 build holes closed). The concrete menu of what the remaining legs would be, ranked by build-cost / leverage:

| Leg | Tier | State | What building it takes | Notes |
|-----|------|-------|------------------------|-------|
| **OVX / OVX−VIX gap** | 2 | instrumented (yfinance ^OVX) but **UNCALIBRATED** + currently DARK (stale since 7/1) | **cheapest, highest-leverage:** resume the boot pull + run ONE analog scan (Abqaiq 2019 / Ukraine 2022 / Israel-Iran 2024) to set the numeric line | this is the "dark canary through a war week" the whole map exists to prevent |
| **Single-stock vs index skew split** | 2 | **no pullable source** (arrives via WALTER only) | establish a pullable source (WALTER/YCharts) + one percentile pass vs the 10-yr series (0.71 [7/10] is a record low but has no calibrated line) | fed the 7/11 NO-FIRE; the FLOW-side canary for SIG-020's conviction question |
| **NDX−SPX 3m ATM IV dispersion** | 2 | **no free pull found** (WALTER intake only) | dependency-gated on the VULCAN seam reconciliation, then a route-out for the series | anchors exist (ATH 10.80 [6/23], mean ~5.1) but the line waits on VULCAN |
| **Net GEX / flip band** | 3 | HENRY-owned; F2 dependency | not a VIOLET build — coordinate a repull *cadence* with HENRY (its staleness is my problem too) | free-tracker ±err is the accepted source (your 7/16 routing) |
| **KOSPI 8,200 / 2×-ETF amplifier** | 3 | **NO OWNING AGENT** — known fleet coverage gap | governance, not a VIOLET build: PROME/DAEDALUS assigns an owner, else it's a watch line with no watcher | the map's biggest named hole; worked 6/23-7/2 (Korea realized the unwind offshore first) |

**Recommendation for the menu:** if Will greenlights any, **OVX first** (instrument already exists, just needs the boot pull resumed + one calibration scan) — highest value per unit build. The KOSPI hole is the most important *systemically* but is an owner-assignment decision, not a VIOLET build.

## 5. Lane ratification (vol-regime RESEARCH-INTAKE query) — KEEP, but AMEND (rebut the CUT)

**The CUT rationale ("cftc_cot structured feed covers your domain") is a category error.** cftc_cot covers weekly **positioning**; this lane's job — per my SIGNAL_INTAKE — is the **structural / narrative vol events boot can't compute** (ETP stress, vol-control/CTA de-risking, microstructure/methodology changes, vol-spike narratives). No overlap. So: **keep it, but re-point** from level-reporting terms I already self-pull (VIX spike/collapse) toward the structural class.

- **Current:** `"VIX spike" OR "VIX collapse" OR "volatility regime" OR "vol compression" OR "VVIX" OR "SKEW index"`
- **Proposed amend:** `"vol ETP" OR "short-vol unwind" OR "volatility control" OR "vol-targeting" OR "dispersion trade" OR "0DTE" OR "VIX methodology" OR "variance swap" OR "volatility regime" OR "vol compression"`
- **Rationale:** drops the two terms that just re-report levels I pull live (VIX spike/collapse, VVIX/SKEW are on my boot); keeps the direction-neutral regime terms (RED-FT-06 low-vol trigger is live); adds the structural/microstructure class that is genuinely "notice while nobody's looking." That's how it earns its keep at the 7/30 review. REGISTRY Domain row looks current enough — no flag.

---

*Files touched this session: STATUS (full 7/17 refresh), KB-VIO-117/118/119, SIGNAL_INTAKE (+JPY threshold line), CANARY_MAP v1.1, SCRATCH, NEXUS_BRIEF, JPY_VOL/VX_DAILY/VIX_OPTIONS/COT_VIX auto-appended by boot. COT grade + follow-up message after 3:30.*
