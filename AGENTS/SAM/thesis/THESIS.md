# SAM THESIS — v1.5

**Version:** 1.5
**Last Updated:** 2026-05-27 (Big 3 ESR window resolved 3-of-3 — Nippon 195% M&A, Meiji 208% manageable, **Sumitomo 197% ↑+19pt with foreign book growing**; Channel 1 demoted to deferred structural backstop) | 2026-05-29 maintenance: live probabilities/levels now reference STATUS (doc-ownership cleanup — no view change; version held at 1.5) | 2026-05-31: SAM-21 June-hike mark ~50% → 70% on market repricing to ~88% (POV pivot, no version bump — see CHANGELOG) | **2026-06-01 surgical sync: Channel 3 reactivated on Iran MOU break (SAM-23 ~55% → ~72%); Fed-cut secondary path softened to multi-month tail (Jun 17 reads dead, >97% no-change priced). Surgical fix — no probability re-rates (15% oil-shock / 25% BOJ-delays held pending escalation trajectory). See CHANGELOG.**
**Status:** 🟠 SINGLE-PATH — Channel 1 deferred (3-of-3 Big 3 confirmed ESR pressure absorbed via M&A + equity rally + hedge-cost relief, NOT foreign bond sales); Channel 2 (June BOJ — market ~88% / SAM 70%, repriced May 31) is dominant remaining near-term trigger, now a market-confirmed base case; **Channel 3 REACTIVATED Jun 1 on Iran/Hormuz MOU break (SAM-23 ~72%; intervention #3 zone live; Bessent-Katayama-Himino cabling hike+intervention combo)**
**Conviction:** HIGH on direction; MEDIUM on near-term timing (single-catalyst structure carries more drawdown risk than multi-channel convergence)
**Current state (daily snapshot):** see `STATUS.md`

---

## CORE THESIS

Japan is approaching a structural inflection. As of v1.5, the path is **single-catalyst**: yen strengthens primarily via the June BOJ hike (Channel 2). The forced-repatriation mechanism (Channel 1) is deferred to multi-year — the Big 3 mutual ESR disclosures resolved without forced foreign selling. The structural direction is intact but the near-term path is narrower.

**One-liner:** v1.5 — Channel 2 (June BOJ June 16 — now a market-confirmed base case, market ~88% / SAM 70%; live marks in STATUS) is now the dominant remaining near-term path. Channel 1 (life insurer ESR pressure → foreign bond sale) deferred after 3-of-3 Big 3 mutual prints (Nippon, Meiji Yasuda, Sumitomo) showed ESR pressure absorbed via M&A capital action + equity rally + hedge-cost relief WITHOUT foreign bond reduction. Foreign books in unrealized GAIN at all three; foreign exposure GROWING (Sumitomo's allocation rose from 33.3% → 35.5%); M&A direction INTO US (Resolution Life, Allstate, Dearborn). J-ICS lifer long-end abandonment (the JGB 30Y mechanism, domestic) remains intact. Channel 3 dormant on Brent -12% collapse (Iran/Hormuz MOU framework hardening). Direction confirmed; the single-path structure makes the position correctly sized at 13 shares + Jun-18 $58C — no Sep OTM addition warranted under v1.5.

---

## CARRY-UNWIND PROBABILITY METHOD

The 7d/30d/60d buckets in `STATUS.md` § CARRY UNWIND PROBABILITY are **decomposed estimates** from ~10 hand-set anchors — value is **auditability** (every move traceable to a named driver), not point-precision. Live anchor states + current bucket values live in STATUS. Method added Jun 3 2026 to close RED CH-004 (prior buckets were judgment-calibrated conviction shipped to LIQUID/HENRY as if probability; methodology correction surfaced a ~33pp catalyst→unwind conflation overstating 30d/60d).

### Formula

```
P(unwind, T) = 1 − ∏ (1 − pᵢ(T))     over 5 trigger channels + residual term
where pᵢ(T) = P(catalyst i fires in T) × P(unwind | catalyst i fires) × CFTC_amplifier
Final = bottom-up union − overlap discount (judgment, joint-escalation tail)
```

### Trigger anchors

| # | Trigger | Mechanism | Catalyst-P source | Baseline unwind\|fires | T-eligibility |
|---|---|---|---|---|---|
| 1 | **BOJ surprise** | hawkish-on-size/path. Hike-as-priced doesn't unwind; only hawkish-tail subset within hike-probability mass triggers. | hike prob × hawkish-tail share | 0.45 | 30d, 60d |
| 2 | **MOF intervention #3** | USDJPY 160+ → USD sale → positioning fold | SAM-23 | **0.20** (per CH-003 — Apr 30 + May 6 both spike-reversed same-day; pure FX intervention can't fix the rate gap) | all |
| 3 | **Risk-off shock** | equity/VIX spike → safe-haven yen bid (Aug-2024 precedent) | base ~10%/30d + tape elevation | 0.50 | all |
| 4 | **Fed-cut surprise** | dovish FOMC/CPI → USD compression | FedWatch + soft-CPI tail | 0.45 | 30d, 60d |
| 5 | **Oil/MOU escalation** | Brent $120+ / Hormuz close → Phase 2 yen bid via recession risk | escalation prob | 0.40 | 30d, 60d |
| R | **Residual** | unattributed positioning-cascade base rate (Aug 2024 was partly this — BOJ trigger lit fuse but violence outsized to catalyst) | **STATE-DEPENDENT** — see CFTC gate below | sized 1.5/5/7.5pp (7d/30d/60d) when ACTIVE | all when active |

### CFTC amplifier + residual gate (explicit)

Positioning is the amplifier on P(unwind \| trigger), not a trigger itself. The residual term is **fuel-load-contingent** — it comes OFF when positioning covers. NOT a permanent floor.

| CFTC state (% of cycle peak, -180K Jul-2024 reference) | Amplifier on baseline unwind\|fires | Residual term |
|---|---|---|
| < 30% of cycle peak | 0 (baseline applies) | **OFF** |
| 30-60% | +2-3pp | **OFF** |
| **> 60% (current: 63.7% / -114K)** | **+5pp** | **ON** |
| > 85% (Aug-2024 levels) | +8-10pp | ON |

Re-evaluated weekly on the Sat CFTC print. If positioning covers below ~-108K (60% line), the +5pp amplifier drops AND residual turns off — a future SAM should NOT treat 5pp as a permanent floor.

### Overlap discount — judgment, NOT derived

Independent-union formula over-counts where triggers correlate. The joint-escalation tail:
- **Oil/MOU shock (#5) often IS the risk-off trigger (#3)** — one Iran shock fires both
- **Oil/MOU pushes USDJPY through 160 → fires intervention (#2)** — chain correlation
- **BOJ hike + intervention combo explicitly cabled** (Reuters Jun 1) — #1 and #2 correlate at the meeting

**Discount:** −1pp (7d) / −5pp (30d) / **−7pp (60d, biggest)** — more time → more chance for chain-firing. Sized by judgment, not derived from a joint-distribution model.

### Update discipline

- **Bucket shifts >5pp must attribute to a named driver** (anchor change, residual ON/OFF, overlap re-judgment) — no silent moves
- **Anchors re-state when catalyst-P or unwind\|fires moves >10pp** → log to CHANGELOG
- **CFTC amplifier + residual ON/OFF re-calibrate weekly** on the Sat CFTC print
- **Method itself reviews on each version bump**

### Calibration anchors

- **Aug 2024 unwind** (n=1): USDJPY -7y in 3 sessions, dual BOJ hawkish + Fed dovish + CFTC -180K positioning peak. Sized unwind\|fires conditionals + residual against this single precedent.
- **Base rate ~5-10%/30d unconditional** (judgment; 2-3 major unwinds in 5y across rolling windows).
- **8 resolved SAM predictions:** failure patterns shade anchors — over-hawkish on Takaichi ceiling 2× (SAM-08, SAM-20) discounts BOJ-surprise hawkish-tail; threshold-vs-mechanism trap 3× (SAM-25, SAM-14, SAM-19) reinforces conservative conditionals; **CH-003** (Apr 30 + May 6 same-day reverses) sets MOF unwind\|fires baseline at 0.20.

### What this method is NOT

- Not a backtest (n=1 modern unwind, insufficient sample for empirical fit)
- Not authoritative probability — auditable model output from named priors
- Cross-agent disclosure to LIQUID/HENRY uses "decomposed estimate (37%)," not "true probability (37%)"

---

## THREE TRANSMISSION CHANNELS

### Channel 1: Life Insurer Repatriation (SAM → LIQUID) — **v1.5 STATUS: DEFERRED STRUCTURAL BACKSTOP**

**v1.5 verdict (May 27):** The Big 3 mutual ESR disclosure window (Nippon, Meiji Yasuda, Sumitomo — all printed May 26) resolved with 3-of-3 evidence AGAINST the v1.0-v1.4 transmission mechanism. ESR pressure exists (Nippon -27pt to 195%, Meiji -8pt to 208%) but was absorbed via capital actions (Resolution Life $10.6B M&A), equity rally, and hedge-cost relief — NOT via foreign bond sales. Sumitomo's ESR ROSE +19pt to 197% with foreign exposure GROWING +¥1.11T (foreign bonds +¥543B, +6.2%). Foreign books in unrealized GAIN at all three. M&A direction is INTO the US (Resolution Life, Allstate, Dearborn Life).

**Channel 1 demoted to deferred structural backstop (multi-year, not 2026).** The mechanism is not falsified at the multi-year/cycle level — the structural setup (hedge ratio collapse, J-ICS visibility, rate-differential pressure) is intact. But the 2026 transmission timing assumption is broken. Next near-term Channel 1 re-test window is the H2 FY2026 plan announcements (Oct-Nov 2026) and the FY2026 ESR disclosures (May 2027). See `thesis/CHANGELOG.md` 2026-05-27 entry for the full v1.4 → v1.5 transition.

**What still works (mechanism level — kept in v1.5):**
- **J-ICS lifer long-end abandonment** as the JGB 30Y/40Y driver (DOMESTIC mechanism, independent of foreign-asset transmission) — see subsection below
- Mid-size lifer pivots (Fukoku, Asahi) from 30/40Y → 10-15Y tenors — confirmed
- Norinchukin CLO ¥9.7T position shrinking — confirmed (¥500B decline Q1 2026)

**What's deferred:**
- "ESR cap → forced UST sale" transmission timing — pushed to multi-year horizon
- Big 3 mutual ESR window as primary near-term catalyst — exhausted

---

#### Deferred mechanism reference (condensed — full depth in `research/outputs/`)

*The multi-year structural setup, retained for re-test windows. Channel 1 is DEFERRED under v1.5 — this is reference, not an active near-term driver.*

- **Scale:** Life insurers hold $450-810B USTs; total Japanese institutional foreign exposure ~$3.0-3.5T. Japan holds $1,239.3B USTs (Feb 2026, world's largest holder). The Apr-2025 ESR regime made unrealized losses regulator-visible — but v1.5 confirms **ESR visibility ≠ forced foreign selling** at the disclosure-window timescale (capital actions + equity rally absorb it). *(GPIF is NOT a forced seller — ±6-7% bands cushion; even USD/JPY 150→130 keeps foreign weight ~21.5-21.8%, within band. Confirmed through FY2029.)*
- **Mechanism (legacy):** JGB yields ↑ → unrealized losses mount → ESR pressure → sell foreign bonds first (2-3× risk weight); hedged UST returns negative vs JGBs; selling outright because hedge costs (~4.35%) exceed UST yield (~4%). → `research/outputs/LIFE_INSURER_UST_DEEP_DIVE.md`
- **Hedge-ratio collapse:** 44.4% (Mar 2025, 14-yr low); ~55% of foreign bonds (~$370-550B) unhedged; vol-wtd entry USD/JPY 135-145. Acceleration point USD/JPY <130-135 = mechanical forced selling. At ~159 FX is not the trigger. → `research/outputs/NORINCHUKIN_CLO_CONTAGION.md`
- **Private-credit amplifier:** ~$45B central est (¥6-8T) US private credit, 80-90% unhedged; double-hit (yen strength wipes spread income WHILE US PC marks down + gates). Illiquid/un-sellable. Key: Sumitomo $10.7B, Nippon $3.25B (TCW), Meiji $4.2B, Dai-ichi $4.2B. → `research/outputs/JAPAN_INSURER_PRIVATE_CREDIT_EXPOSURE.md`
- **Flow pace (latest BASE, Apr-30/May-3 data):** Feb TIC stock +$53.8B (aggregate NOT net selling); 4-wk MOF rolling ~$18B/mo (elevated, below stress); JGB auctions orderly across curve (Apr 14 20Y BTC 4.82x). Selling is real but gradual — visible at weekly MOF level, invisible at TIC aggregate (offset by banks/retail Toshin + price effect).

**Flow scenarios (v1.5 — post Big 3 ESR 3-of-3):** Base $80-120B/12mo ($7-10B/mo) **78%** · Stress $150-250B/6mo ($25-40B/mo) **18%** · Crisis $300-500B/3mo **4%**. *(Base confirmed by 3-of-3 Big 3 — rotation-within, no net cut; stress lowered, would need a new shock.)*

#### Lifer Long-End Abandonment — JGB 30Y/40Y driver (**KEPT LIVE in v1.5; DOMESTIC**, independent of foreign-asset transmission)

- Under J-ICS (live Apr 2025), super-long JGB moves reprice the ENTIRE balance sheet (duration mismatch surfaces immediately). Mid-size lifers (Fukoku, Asahi) pivoted 30/40Y → 10-15Y; Big 4 sidelined at the long end.
- **Critical inversion:** lifer absence at the long end is **the cause of the yield blowout, not the consequence**. Higher yields don't draw insurers back — J-ICS makes long-duration purchases punitive for solvency. The "yield level brings insurers back" reflex is broken.
- **Implication:** JGB long-end pressure persists without forced BOJ intervention → pushes BOJ toward normalization OR a YCC-style cap (D2 scenario). Either way, structural yen tailwind. Source: SSGA/Aviva J-ICS analysis.

### Channel 2: Carry Unwind (SAM → HENRY) — **v1.5 STATUS: DOMINANT REMAINING NEAR-TERM TRIGGER**

**Current probability:** daily-marked in STATUS (CARRY UNWIND PROBABILITY table). Structural shape: 7d low (no near-term binary between now and the June meeting); 30d / 60d anchored on June 16 BOJ as the dominant single-path trigger, trimmed on Channel 1 demotion.

CFTC net short JPY has been rebuilding toward the cycle peak (live net + % of peak in STATUS). Positioning did NOT correct after the Apr 28 hawkish hold → fuel load growing into the June catalyst. Aug 2024 precedent: unwind took hours, not days.

**Post Apr 28 BOJ:** Hold + 3 dissents + GDP cut + inflation upgrade = market repriced June hike to 74% *at the time*. Since softened by the May 22 national + May 28 Tokyo CPI misses (partly offset by the May 29 activity beat) — current SAM/market marks in STATUS. Direction confirmed; timing hinges on the June meeting.

**Triggers (any one sufficient):**
- **BOJ hike June base case** (current SAM mark in STATUS — market repriced to ~88% / SAM 70% on May 31, *through* the May CPI misses); Apr 28 resolved hold + hawkish
- MOF intervention at 160 (USDJPY 157 currently off zone; reactivates if oil escalates again or Tokyo weakness reverses; Katayama "free hand" still on the table)
- Fed forced cuts via private credit cascade (USD/JPY sub-145 without BOJ)
- Risk-off event (geopolitical escalation → safe haven yen bid)
- ESR disclosures (mid-May) trigger stress-case repatriation

**The intervention paradox:** MOF acts → sells USD → accelerates carry unwind. MOF doesn't act → yen weakens on oil → forces more repatriation. Either path leads to unwind.

### Channel 3: BOJ Policy Divergence + US-Japan FX Coordination (v1.4 expansion)

**Current rate:** 0.75% (Dec 2025 hike) — AT Takaichi ceiling. Next hike to 1.00% = political collision.
**Timeline:** April 28 = **HELD with 3 dissents for 1.00%** (resolved). May 1 "secondary MPM" was a calendar artifact — no actual policy event. **June 16 = base case (~70% SAM / ~88% market, repriced May 31).**
**Terminal rate:** 0.75% (political ceiling), NOT market consensus 1.25-1.5%

**US-Japan FX Coordination (NEW v1.4 — promoted from candidate):**
- **Apr 30 MOF intervention #1:** ~¥5.48T ($35B). USDJPY 160.70 → 155.55 intraday. First since Jul 2024.
- **May 6 MOF intervention #2:** ~¥4.3T ($28B). USDJPY 157.89 → 155.05 intraday. Combined ~¥10T ($63.5B) — **largest combined round since 2022**.
- **May 11-12 Bessent-Katayama Tokyo meeting:** "Constant and robust" FX coordination affirmed publicly. First US public affirmation of Japan FX intervention since 2022. Bessent has prior public stance favoring faster BOJ hikes. Subtext: US wants rate differential compressed from both sides (Fed cuts eventually, BOJ hikes now).
- **Channel 3 reaction function upgraded:** Intervention #3 is now a near-term catalyst (USDJPY 159+ trigger zone live; SAM-23 75% prob) with diplomatic friction removed.
- **Caveat:** No SWAP line announced. Effectiveness mixed — each intervention drove ~5y/3y intraday spike that reclaimed same-day. Pure FX intervention cannot fix the ~300bp Fed-BOJ rate gap. Bessent meeting did NOT publicly address rates.

**Apr 13 Ueda speech (v1.3 revision):** Speech delivered by Deputy Himino (Ueda at G7/G20). Explicit ME caution: "developments in the Middle East remain uncertain…will closely monitor their potential impact on economic activity, prices, and financial conditions." Word "rate hike" absent. Market bets collapsed 70% → 3-10%. Polymarket 97% no change. This was the decisive signal that April was off the table and June became base case — *"return to policy normalization as soon as June."*

**Why 0.75% ceiling:**
- 75-80% of Japanese mortgages are FLOATING RATE (vs 90% fixed in US)
- BOJ hike → prime rate rises → household payments spike IMMEDIATELY
- Real wages barely positive (+1.4% Jan); food spending at 44-year high
- Takaichi drew explicit 0.75% line (Aida statement); has 2/3 supermajority
- BOJ board being stacked dovish (Asada joined Mar; Sato joins June, hawk→dove swap)

**The Takaichi-Ueda collision is inevitable:**
- Ueda wants 1.0%+ for inflation credibility
- Takaichi caps at 0.75% for mortgage protection
- No path solves both → collision in April-July window
- D2 scenario (YCC return): 32-40% probability

**BOJ evidence (most hawkish cycle):**
- **Apr 28 MPM: 3 dissents (Takata, Tamura, Nakagawa) for hike to 1.00% — biggest split since 2016, first under Ueda; FY26 GDP cut 1.0%→0.5%; inflation forecasts upgraded; Ueda hawkish presser; swap markets repriced June to 74%**
- Mar 18-19 Summary of Opinions: debate shifted from "when" to "how much"
- Takata DISSENTED for 25bp hike to 1.00% (Mar — escalated to 3-board split Apr 28)
- "Raise without hesitation" + "rapid tightening" language used
- New BOJ CPI gauge (first ever): core +2.2% — deliberately signaling above target
- Output gap positive 15th straight quarter
- Ueda removed growth precondition: temporary downward pressure won't prevent hikes

---

## CATALYST SEQUENCE

*Resolved-event narratives live in [`timeline/TIMELINE.md`](timeline/TIMELINE.md) (active) and [`timeline/ARCHIVE.md`](timeline/ARCHIVE.md) (pre-May 11). This section keeps forward-looking only.*

### Forward

| Date | Catalyst | Expected Impact |
|------|----------|-----------------------|
| **Ongoing** | CFTC JPY weekly (auto-pulled) | Fuel-load gauge; broke -102K cycle peak May 30 (-114,667, 4th build week). Live net in STATUS. |
| **Ongoing** | Iran/Hormuz MOU watch — **effectively broken Jun 1** | Tehran suspended document exchange + Hormuz block threat; Brent +4% Jun 1. Watch for walk-back (Trump-Khamenei reset → resign path) vs further escalation (Brent $100+, Hormuz close attempt). Brent live in STATUS. |
| **Ongoing** | Intervention #3 watch — **zone REACTIVATED Jun 1** | USDJPY 159+ = trigger zone (live level in STATUS). **SAM-23 ~72%** (re-rated up from ~55% on MOU break). Katayama May 29 "decisive action" verbal at 159+; Bessent-Katayama-Himino cabling hike + intervention combo per Reuters Jun 1; pre-meeting blackout ~Jun 13. 160 = hard intervention trigger. |
| **🔴🔴 Tue Jun 16** | **BOJ MPM — DOMINANT REMAINING CATALYST** (SAM-21 70% — live mark in STATUS; market ~88% repriced May 31; SAM-24 25bp @85%) | Hike = FXY +5-8% structural; carry unwind fires. **Single-path under v1.5 — market-confirmed base case.** |
| Jun 16 | Sato joins BOJ board (hawk→dove swap) | Medium-term political risk post-June (beyond 1.00% gets harder) |
| Jun 18-19 | May trade balance — Phase 1 stability lag-test | Volume recovery vs cost-side decomposition (per CALENDAR routing) |

*Operational forward calendar (with current status, daily tracking) lives in `docket/CALENDAR.md`.*

---

## OIL-IN-YEN STRUCTURAL DYNAMIC

Oil shock creates a two-phase JPY dynamic:
- **Phase 1 (weeks 1-2):** Oil spike → trade deficit widens → JPY WEAKENS → carry survives
- **Phase 2 (weeks 2-8):** Recession risk compounds → safe haven yen WINS → carry unwind

**Current state (Jun 1 reframe):** Brent live level in STATUS — collapsed from ~$108 (May 21) to ~$92 (late May) on Iran/Hormuz MOU framework hardening, **then re-accelerated +4% Jun 1 on MOU break** (Tehran suspended document exchange + Hormuz block threat). **Phase 2 inception PAUSED; Phase 1 oil pressure rebuilding** (with v1.4 supply-destruction caveat — blockade severity can choke import volumes and invert the trade-deficit mechanism; May TB Jun 18 is the diagnostic). The MOU binary has resolved to the *collapse* branch (oil snapback + intervention #3 zone reactivated). Forward watch is now walk-back (Trump-Khamenei reset) vs further escalation, not sign-vs-collapse.

**v1.4 revision — Phase 1 mechanism INVERTED by supply-destruction effect:** April trade balance (May 21 print) posted ¥+301.9B **SURPLUS** vs ¥-30-45B deficit consensus. **Crude oil imports -64% YoY** (steepest since 1980); ME crude -67.2% YoY (lowest since 1979); LNG from ME -76.1%. The blockade didn't INCREASE Japan's oil bill — it **collapsed import volumes** (physical supply choke). Japan couldn't buy ME barrels. **The Phase 1 mechanism ("oil → trade deficit widens → JPY weakens") inverts when blockade severity chokes physical flow — supply destruction shows up as smaller deficit, not larger.**

**Critical observation:** Yen STILL weakened (USDJPY 157.61 → 159.19 May 12-21) despite the trade surplus. The driver is **rate differential + fiscal supply (super-long JGB selling) + lifer absence**, NOT trade. Channel attribution corrected.

**v1.4 implication:** Trade-balance is no longer a clean Phase-1 confirmation indicator under blockade conditions. Watch rate-differential proxies (USDJPY vs swap-implied rate path), JGB long-end supply/demand, and CFTC positioning instead.

**Phase 1 stability watch (added 2026-05-26 — PROME forward-question):** The April surplus may have been a one-month volume-collapse spike rather than a structural inversion. Investing.com (5/21) caveat: *"this collapse artificially inflates the trade surplus figures, and petroleum-related input costs are expected to rise in the coming months."* If Iran/Hormuz MOU sticks and ME crude flows normalize — even with Brent staying low — volume recovery alone could swing the trade balance back toward deficit on a 1-3 month lag. **May TB print (~June 18-19) is the diagnostic** — mechanism-aware routing logged in `CALENDAR.md`. Diagnostic outcomes: (a) deficit re-opens with Brent <$100 → Phase 1 mechanism back online (transient inversion, not structural); (b) surplus persists with ME volumes recovering → inversion is structural across the cycle; (c) surplus persists but ME volumes still depressed → inconclusive, defer to June TB print. Threshold-vs-mechanism discipline applies: surplus is a threshold-style read, the volume-vs-cost decomposition is the mechanism.

**Oil-yen paradox (modified):** Yen weakening vs JGB yield surge = rate differential still matters more than flow. Oil adding CPI pressure without trade-deficit pressure = Phase 2 starts earlier (less drawdown delay).

**FXY wins in all 3 oil scenarios (3-6mo horizon):**
- Oil $80: +3-5% (yen strengthens, BOJ delays)
- Oil $99-110: flat then +5-8% (BOJ June trigger)
- Oil $130+: -5-8% then +10%+ (drawdown then recovery)

Oil changes TIMING and DRAWDOWN, not DESTINATION. Only loss scenario: oil spikes AND BOJ blocked AND Fed doesn't cut AND intervention fails simultaneously (<5%).

---

## INDEPENDENT CATALYST: FED CUT PATH (SECONDARY PATH under v1.5 — via HANS/BROCK)

Private credit cascade: $10.1B redemption requests Q1 2026 (BlackRock, Blackstone, Apollo, etc). Only ~70% honored. Median borrower interest coverage 1.6x. Q2 2026 = redemption PEAK (KB-152: Apollo 15% / Ares 14% / BCRED 12% + gating; Blue Owl OCIC/OTIC 28.5%/52.9%).

**Mechanism:** cascade → recession risk → Fed cuts → USD weakens → USD/JPY sub-145 WITHOUT BOJ action. Carry unwind fires on U.S. credit deterioration alone.

**Why this is the SECONDARY PATH now (v1.5, elevated May 27; sharpened May 28; **Jun 1 reframe below**):** With Channel 1 deferred, the position is single-path on the June BOJ hike. The May 31 market repricing brought the June hike back to a market-confirmed base case (~88% market / SAM 70%) — the May 28 Tokyo CPI dovish softening was overridden by the activity beat (May 29 IP/retail) + 3-dissent split, with the market siding with the wage/activity mechanism over the CPI threshold. Channel 3 then **reactivated Jun 1 on Iran MOU break** (intervention #3 zone live; SAM-23 ~72%); structure remains single-path on the BOJ hike for thesis-direction purposes but the BOJ pre-meeting cabling window now carries an intervention-combo tail. This secondary path (Fed-cut) is the backup engine if the BOJ disappoints, and it is **not** owned by SAM: SAM owns the *carry / USD-JPY transmission end*; HANS/BROCK own the *US private-credit end*. SAM monitors the carry-end tripwires below and pulls the credit-end read from BROCK/HANS.

**The timing key (Jun 1 reframe — multi-month tail, not Jun-window):** Earlier v1.5 framing read the Jun 17 FOMC as a "discrete catalyst one day behind the primary," softening the "BOJ delays = pure downside" line in RISK FACTORS. **That framing was a stretch.** Per Jun 1 CME FedWatch, Jun 17 FOMC is priced **>97% no-change** at 3.50-3.75%, with **<10% cut odds anywhere in 2026**. April US CPI 3.8% YoY (ME energy passthrough) + resilient labor (115k NFP, 4.3% U/E) are blocking the cut; Apr 29 FOMC minutes acknowledged credit-conditions stress (leveraged loans, CMBS, small-biz) without forcing a pivot. **The PC-cascade path is retained as a multi-month tail (cascade → recession → cuts later in 2026), not a discrete Jun-window backup.** Practical implication: the Jun-18 $58C is pure BOJ binary with no Fed-side insurance, and the "BOJ delays = pure downside" framing in RISK FACTORS stands — softening the mitigation column to reflect this. SAM-side carry tripwire is now US CPI Jun 10 (could move dots a week ahead if a soft surprise prints) rather than Jun 17 FOMC itself.

**Tripwires (carry-end — SAM watches; current values live in STATUS):**

| Tripwire | "Firing" condition | Significance |
|---|---|---|
| Fed-cut pricing (CME FedWatch / FF futures) | Jun 17 cut odds rising; 2026 cut count expanding | **Jun 1: >97% no-change priced for Jun 17; <10% 2026 cut odds — backup engine off for Jun window. Tripwire is *change from this baseline*, not absolute level.** |
| US CPI (Jun 10) | Soft print (vs Apr 3.8%) | Opens Fed-cut path; feeds Jun 17 dots one week ahead. **This is now the SAM-side carry tripwire on the Fed leg — moves dots before Jun 17 itself can.** |
| FOMC Jun 17 dots | Dovish dots / cut delivered | USD/JPY down independent of BOJ — the other half of the carry trade. **Jun 1 reread: hold-confirming not rescue; deliver-no-Jun-window-carry-catalyst is the base case.** |
| USD/JPY 145 | Breach | Secondary-path target zone; unhedged insurer positions underwater → mechanical selling (links back to Channel 1 threshold) |
| PC-cascade escalation (**BROCK/HANS input**) | Redemption peak → systemic / forced-seller | The credit-end trigger SAM cannot generate — pull from BROCK/HANS |

---

## POSITION VIEW

**Vehicle:** FXY (CurrencyShares Japanese Yen Trust) — long, sized to capture carry unwind. Target $60-62 / USD/JPY 148-152 (6-month). **Stop spec (Will-decided 2026-06-03, event-cap mode):** pre-Jun-16 = no mechanical price stop (position event-capped by sizing); post-Jun-16 = exit if BOTH (BOJ dovish) AND (USDJPY 167+/no MOF). $55.05 is the FXY level correlating with USDJPY ~167, meaningful only post-event. Full spec in `STRATEGY.md`.

*Current size, blended entry, and tranche state live in `STATUS.md` and `TRADE.md`. Decision playbook (when to add/hold/exit, vol-signal interpretation) lives in `STRATEGY.md`.*

---

## KEY THRESHOLDS

Structural levels that gate thesis paths. *Current values + breach status live in `STATUS.md`.*

| Level | Significance |
|-------|-------------|
| USD/JPY 160 | MOF intervention trigger |
| USD/JPY 155 | Phase 2 carry unwind onset |
| USD/JPY 147 | Forced carry unwind |
| USD/JPY 145 | Unhedged positions underwater → mechanical selling |
| USD/JPY 130-135 | Life insurer forced systematic selling (avg entry for unhedged) |
| JGB 10Y 2.40% | Stress crossover |
| JGB 30Y 4.0% | Severe insurer stress / acceleration zone (J-ICS lifer long-end abandonment driver) |
| Brent $120 | Kharg Island scenario (Phase 1 oil shock) |
| BOJ rate 0.75% | Political ceiling (Takaichi mortgage constraint) — next hike breaches |

---

## RISK FACTORS (v1.5)

| Risk | Prob | Impact | Mitigation |
|------|------|--------|-----------|
| BOJ delays past June (oil + political cover extends to Sep+) | **25%** (rationale: complement of SAM-21 70% June hike mark, modulo near-zero skip/cut tail. **Raised to 25% post May 28 Tokyo CPI dovish miss; May 31 market repricing to ~88% undid that input, but the SAM 70% mark keeps the implied complement at ~25%, so number held — re-rate is a separate deliberate decision pending escalation trajectory.**) | FXY -3-5% short term | **Single-path, and Jun 1 reframe: closer to pure downside than v1.5 originally framed.** Fed-cut secondary path is now multi-month tail not Jun-window (>97% no-change priced for Jun 17, <10% 2026 cut odds) — Jun-18 $58C is pure BOJ binary. Channel 1 remains deferred (no parallel there). Time = more CFTC fuel load (already broke -102K cycle peak); unwind more violent when fires. May TB (Jun 18) gates the oil/cover side; US CPI (Jun 10) is the soft-Fed tripwire that could move dots a week ahead. |
| Oil shock dominates (Kharg, Brent $120+) | 15% (**held — Jun 1 MOU break raises directional probability but Brent $120+ + "yen stays weak" compound remains low; re-rate deferred pending escalation trajectory**) | FXY to ~$51-53 short term | **Pre-Jun-16 (Will-decided Jun 3): event-capped, no stop fires; accept full drawdown to ~$51-53.** Position sized small ($798) for this acceptance. Brent re-accelerating post Jun 1 MOU break (live Brent in STATUS) — direction reversed from May 27 framing, but well below Kharg threshold. v1.4 supply-destruction caveat applies (blockade severity can mute the channel via import-volume collapse). |
| Intervention fails (USDJPY breaks 162+ despite #3, Bessent jawboning empty) | 12% (held under Jun 1 MOU break — Bessent-Katayama-Himino cabling alignment per Reuters Jun 1 supports execution, not jawbone-only) | FXY to ~$55-56 before recovery | Hold if fundamentals intact; **pre-Jun-16 event-cap means no stop fires on this scenario alone — post-event AND-trigger applies if BOJ also dovish**. #3 zone REACTIVATED Jun 1 (was framed "defused on Brent collapse" pre-Jun-1); execution probability supported by cabling alignment + precedent (¥10T deployed, same-day reclaim pattern). |
| **Channel 1 reactivates (new shock — e.g. JGB 30Y blows out to 4.5%+, ESR re-tests below 200% via market stress)** | **10%** | Re-add Channel 1 to multi-channel structure; FXY +3-5pp 60d prob upside | Watch JGB long-end, M&A capital action saturation at Big 3 mutuals |
| Takaichi board stacking blocks hikes beyond 1.00% | Medium-term | Limits structural appreciation | June hike math unchanged; risk is 2027+ |

**Thesis break condition (v1.5):** USD/JPY pierces 167 with no MOF response AND BOJ turns dovish at June 16 meeting. Single-path structure makes the AND condition slightly weaker but still required — neither alone is sufficient.

---

## PREDICTIONS

*Canonical source: [`PREDICTIONS.tsv`](PREDICTIONS.tsv). Calibration scoreboard at top of that file lists OPEN positions, RESOLVED-special (SAM-25 threshold-vs-mechanism), 8 FAILED with lessons, 7 CONFIRMED. Failure-pattern synthesis (political ceiling, stock-vs-flow, intervention prob-weighting, threshold-vs-mechanism, premise-dependence/standalone-channel) is the working calibration warning before writing any new prediction. Full post-mortems for closed predictions live in [`PREDICTIONS_ARCHIVE.md`](PREDICTIONS_ARCHIVE.md) (not loaded at boot).*

---

## CROSS-AGENT LINKS

- **→ LIQUID:** Life insurer UST selling (base-case pace $7-10B/mo confirmed by v1.5). Hedge ratio 44.4% (14yr low) = $370-550B unhedged. Norinchukin CLO ¥9.7T shrinking. Japan holds **$1,239.3B USTs (Feb 2026)** — +$53.8B Dec→Feb. **v1.5 update: Big 3 mutual ESR window resolved 3-of-3 benign — Channel 1 forced-repatriation timing pushed to multi-year. No acute UST sell signal from Japan lifer side for 2026.** JGB 30Y mechanism (J-ICS lifer long-end abandonment) remains intact but is DOMESTIC — does not transmit to UST demand on the timescale previously framed.
- **→ HENRY:** Carry unwind probabilities + CFTC net short: daily-marked in STATUS. Single-path to Channel 2 (June BOJ Jun 16). Aug 2024 speed precedent intact. **Position structure narrows: with Channel 1 deferred, June BOJ hike is the dominant remaining near-term path for the carry unwind.**
- **← HAWK:** War → Japan energy vulnerability (90% ME oil dependent). Hormuz blockade collapsed Japan's ME crude imports -67% YoY (lowest since 1979) — supply destruction inverted the Phase 1 trade-deficit mechanism. Brent collapsed to ~$92 (late May) on Iran/Hormuz MOU framework hardening — live level in STATUS.
- **← HANS/BROCK:** Private credit cascade → Fed cuts → USD/JPY sub-145 independent of BOJ. **v1.5 elevates this as the secondary path** — with Channel 1 deferred, the US-credit-side route to carry unwind matters more.

---

*This is a living document. Update when: thesis changes, thresholds breach, predictions resolve, or new transmission channels identified.*
