# Japanese Life Insurer Tracker

**Last Updated:** 2026-05-26 PM (post-PROME cleanup — Channel 1 banner + mechanism-aware routing; Sumitomo Wed May 27 still pending for v1.5)
**Purpose:** Dashboard for tracking Big 10 insurer positioning, FY2025 ESR disclosures, and repatriation signals. **Mechanics map** for JGB-loss / ESR / lifer behavior — the cross-border forced-repatriation leg of Channel 1 has not fired; rotation-within and J-ICS long-end abandonment dominate.

---

## 🟡 CHANNEL 1 STATUS — DOWNGRADED, NOT DEAD (post-May 26 Big 3 ESR Day 1)

**Channel 1 is downgraded, not dead.** JGB-loss / ESR pressure is real, and J-ICS long-end abandonment remains active. But the **cross-border forced-repatriation mechanism did not fire** in Nippon (195% M&A-driven) / Meiji (208% manageable): foreign books were in unrealized GAIN and ESR pressure was absorbed via capital actions (Resolution Life M&A, sub-debt, retained earnings, equity rally). **Future alerts must distinguish *threshold breach* from *forced-selling mechanism*.**

**What's intact:**
- JGB unrealized losses real and worsening (Nippon -¥5.73T, Meiji -¥2.16T)
- J-ICS lifer long-end abandonment driving JGB 30Y / 40Y curve instability (domestic-curve mechanism)
- Hedge ratio collapse (44.4%, 14-yr low) and rotation-within (unhedged → hedged) confirmed

**What's deferred (not dead):**
- "ESR cap → forced foreign bond reduction" mechanism (not evidenced in Nippon/Meiji; foreign books profitable and growing)
- Big 3 mutual ESR window as primary near-term Channel 1 trigger
- Cross-border leg waits for: (a) Sumitomo printing stress via market losses, OR (b) late-Jun mid-tier print stress, OR (c) Q2 hedge-cost squeeze visible in MOF weekly flows, OR (d) FX-trigger zone (USDJPY <135 mechanical sell zone)

**Implication for alerting:** Old rule "ANY ESR <200% → 🔴" is too crude (would have fired on Nippon M&A action, which markets correctly priced as non-stress). New rule discriminates mechanism — see **Signal Routing** below.

---

## ⚠️ KEY INSIGHT v1.4 (May 21) — J-ICS LIFER LONG-END ABANDONMENT IS THE JGB 30Y DRIVER

**JGB 30Y broke 4.000% on May 15** (peak 4.205%; 10Y at 2.770% 29-yr high). The driver is NOT high-yields-attracting-buyers; it's the opposite — **J-ICS makes long-duration purchases punitive for solvency**, so mid-size lifers (Fukoku, Asahi) pivoted from 30/40Y → 10-15Y BEFORE the May ESR window. Big 4 sidelined at the long end.

**Critical inversion:** Lifer absence at the long end is the *cause* of the yield blowout, not the consequence. Higher yields don't draw insurers back — the traditional "yield reaches a level that brings insurers back" reflex is broken under J-ICS.

**Channel 1 implication (v1.4):**
- The thesis no longer requires forced repatriation to drive yields higher — lifer absence alone does it
- JGB long-end pressure persists/grows without forced BOJ intervention
- Pushes BOJ toward (a) policy normalization to legitimize the curve OR (b) YCC-style cap (D2 scenario)
- Either way, structural yen tailwind — the mechanism is self-perpetuating

**Sources:** SSGA / Aviva Investors (Feb 2026) on J-ICS balance-sheet repricing; mid-size lifer pivots reported pre-disclosure window (Fukoku stopped buying 30Y/40Y Jan 2026; Asahi pivoted to 10-15Y).

---

## ⚠️ STILL ACTIVE (Apr 24) — HEDGED vs UNHEDGED ROTATION

FY2026 plans revealed insurers are NOT cutting foreign bonds in aggregate. They rotate WITHIN the book:
- **Unhedged foreign bonds:** REDUCING (hedge cost math bites)
- **Hedged foreign credit:** INCREASING (ALM duration matching; super-long JGBs avoided)
- **Net foreign bond total:** Flat to UP

Reconciles why Feb TIC showed Japan UST holdings RISING (+$53.8B Dec→Feb) while MOF ITS showed residents selling. Insurers were net-flat to up on USTs while shifting composition. **Repatriation thesis is specifically UNHEDGED foreign bond unwind**, not total foreign bond reduction.

---

## FY2025 ESR DISCLOSURE STATUS — PRIMARY CHANNEL 1 TEST

| Insurer | AUM (¥T) | FY2025 ESR | Disclosed? | Stress trigger (<200%) | Notes |
|---------|----------|-----------|-----------|----------------------|-------|
| **Dai-ichi Life Holdings** (listed) | ~72.4 | **~220%** (+~10pp YoY) | ✅ **May 13-15** | NO — above target band 170-200% | First to print. Domestic equity rally (~+¥1.5T) offset +¥530B mass-lapse risk. **Least-representative of Big 4** — most equity-heavy. |
| **Nippon Life** (mutual) | ~96 | **195%** (vs 222%, -27pt) | ✅ **May 26** | **LITERAL YES / MECHANISM NO** | **-28pt driver = Resolution Life $10.6B M&A subsidiarization, NOT market stress.** Economic env -4pt; new business +5pt. JGB unrealized loss -¥3.6T → **-¥5.73T** (worse by ¥2.13T). **Foreign securities unrealized GAIN +¥3.99T (+¥909B YoY)** — book profitable. Resolution Life basic profit +52% YoY. **No forced rebalance signal.** Source: kessan202605_gaiyo.pdf p.7. |
| **Meiji Yasuda** (mutual) | ~52.9 | **208%** (vs 216%, -8pt) | ✅ **May 26** | NO — manageable band | Inside 200-219% band, below 220% target. Standard model 213% / internal 208%. JGB unrealized loss -¥1.39T → **-¥2.16T** (worse by ¥776B). **Foreign securities unrealized GAIN +¥709B (+¥227B YoY)**. Stancorp (US sub) record earnings via Allstate group acquisition — leaning INTO US, mirroring Nippon Resolution Life direction. |
| **Sumitomo Life** (mutual) | ~37.5 | TBD | ⏳ **Wed May 27** | TBD | $10.7B US private credit stack on top of JGB stress. Symetra outsourcing structural already. **Pattern-confirmation test**: if matches Nippon/Meiji (ESR draw via capital action, foreign book intact) → Channel 1 v1.5 downgrade confirmed. |
| **Fukoku Mutual** | ~8 | TBD | ⏳ | TBD | First-mover super-long JGB exit Jan 2026. Already pivoted to 10-15Y. |
| **Japan Post Insurance** | ~55 | TBD | ⏳ | TBD | Zero PC exposure (cleaner read). Selling low-yield JGBs. |
| **T&D Holdings** (listed) | ~18 | TBD | ⏳ | TBD | Includes Fortitude; ¥550B PC. |
| **Norinchukin** (cooperative) | — | TBD | ⏳ Jun | TBD | World's largest CLO investor; ¥9.7T CLO book. Q1 2026 ¥500B decline. |

### Reading the Big 3 mutual prints — Tue update (post-Nippon/Meiji)

**SAM-25 (40% prob):** at least 1 of Big 3 prints <200% — **TUE RESOLUTION: TRUE-IN-LETTER / FALSE-IN-SPIRIT.** Nippon 195% literally below 200% but the breach is M&A capital deployment (Resolution Life), not market-stress forced rebalancing. The intent of the prediction (forced repatriation visible) did NOT fire.

**Tape priced it accordingly:** USDJPY 158.95 → 159.24 post-print (yen WEAKER, broad-based). FXY flat. If headline 195% had been read as stress, yen would have spiked stronger.

**Channel 1 thesis status (updated post-Tue):**
- ESR pressure is REAL but transmission to UST selling is NOT firing
- Both insurers' foreign books in unrealized GAIN; direction of travel INTO US
- ESR cap absorbed by capital actions (sub-debt, M&A profits, retained earnings), not asset sales
- The "ESR forces UST sale" mechanism that anchored v1.0-v1.4 needs revision
- J-ICS domestic-curve mechanism intact; cross-border leg deferred

**Wed Sumitomo (pattern-confirmation test):**
- **If matches Tue pattern** (ESR draw via capital action, foreign book intact, US growth) → Channel 1 v1.5 downgrade confirmed. Write LIQUID 🟡 signal (counter-thesis).
- **If <200% via genuine market stress** (forced JGB selling, FX-driven foreign mark-down, withdrawal commentary) → Channel 1 reactivates. Write LIQUID 🔴.
- **Symetra/US PC angle wild card:** Even if headline ESR looks manageable, $10.7B US private credit stack could surface stress that Nippon/Meiji didn't have to disclose.

---

## FY2026 PLAN STATUS (RESOLVED — Apr 14-25, kept for reference)

| Insurer | FY2026 Plan Outcome | Key Signal |
|---------|--------------------|------------|
| Nippon Life | Apr 22 (Ishida): ambiguous — paring YEN bonds; foreign direction unstated | ME risk = "upward pressure on inflation and long-term yields" |
| Dai-ichi Life | No formal Apr announcement; prior: doubled overseas strategic ¥600B | ¥630B PC (MS est.); mgmt split Apr 1 |
| Meiji Yasuda | INCREASING hedged foreign credit (ALM); unhedged reduction offset | ¥600B over 3yr at Man Group; ¥1.386T unrealized losses |
| Sumitomo Life | Outsourced ¥2T to Symetra (restructuring); ¥300B new PC FY2026 | Restructuring, not clean cut |
| Fukoku Mutual | Stopped buying 30Y/40Y (Jan 2026) — DOMESTIC action | First mover on super-long exit |
| Japan Post Insurance | Selling low-yield JGBs; expects BOJ April hike (delayed to June) | Zero PC; expects 10Y at 2.5% |

**Net SAM-19 result: ZERO clean foreign bond CUTS** across first 5 plans. Rotation within (unhedged → hedged). This is the basis for the v1.4 J-ICS finding — insurers aren't repatriating in headline numbers; they're abandoning duration on the JGB curve while keeping foreign exposure hedged.

---

## INDUSTRY AGGREGATES

| Metric | Value | Date | Source |
|--------|-------|------|--------|
| Total Japan life insurer AUM | ~¥388T+ (~$2.6T) | FY2025 | Industry data |
| Big 4 unrealized bond losses | ~¥13.2T ($86B) | Jun 2025 (before recent selloff) | Bloomberg |
| Industry hedge ratio | **44.4% — 14-year low** | Mar 2025 | SAM research |
| Unhedged foreign bonds | ~$370-550B | Mar 2025 | Derived from hedge ratio |
| Avg FX entry (unhedged) | USD/JPY 135-145 | Estimated | SAM research |
| Private credit (industry est.) | ~$40-53B (~¥6-8T) | FY2025 | SAM est. from MS 1-3% range |
| Japan UST holdings (all inst.) | **$1,239.3B** (+$53.8B Dec→Feb) | Feb 2026 (TIC Apr 15) | US Treasury |
| JGB 30Y yield (severe insurer stress) | **3.931%** — breached 4.0% May 15 (peak 4.205%), **retraced -7bp** on Brent -12% + dovish CPI | May 22 | MOF |
| JGB 40Y yield | 3.921% | May 22 | MOF |
| JGB 10Y yield (stress crossover) | **2.749%** (29yr high zone; -2bp WoW) | May 22 | MOF |

*Note: JGB 30Y threshold (SAM-26) breached briefly but did not hold — bid came from non-insurer flow, not insurer return. J-ICS mechanism intact; threshold framing was fragile under oil/CPI cross-currents. Treat the 4.000% line as a structural stress level, not a durably-held floor.*

---

## SIGNAL SUMMARY

**What's confirmed (mechanism evidence — high weight):**
1. Near-universal super-long JGB buyer strike (Fukoku, Daido, Meiji Yasuda confirmed; J-ICS-driven)
2. Hedge ratio collapse to 44.4% (Mar 2025, 14-yr low); unhedged-foreign rotation accelerating
3. Hedged UST returns now NEGATIVE vs JGBs (-0.34% after 4.35% hedge cost)
4. FSA actively reviewing insurer balance sheets (Jan 2026 questionnaire on unrealized losses + plans)
5. MOF cutting super-long issuance to ¥17T (17-year low) — acknowledges buyer strike
6. **Foreign bond allocation industry-wide: 22% (Mar 2021) → 17% (Mar 2023) — structural decline** (Reuters/Daiwa)
7. **¥1.35T JGB trim in Q4 FY2024 — third-largest quarterly reduction on record** (Daiwa Securities)
8. All Big 4 EXPANDING private credit despite US gating/stress (Mar 2026 survey: Nippon, Meiji, Dai-ichi maintaining lending plans — Japan Times/Bloomberg Mar 12)

**Down-weighted (superseded by 2026 actuals):**
- ~~At least 50% of Big 10 planned overseas debt cuts (Oct 2025 survey)~~ — **superseded.** Apr 2026 FY2026 plans (Big 4) showed ZERO clean foreign-bond cuts. Pattern was rotation-within (unhedged → hedged), not net cuts. Survey kept as historical sentiment indicator only; actual capital actions overrode stated intent.
- ~~Nippon ESR 222% trigger logic ("if drops <200% → tone changes")~~ — **superseded.** Nippon printed 195% on May 26 via M&A capital action, not stress. Tone did NOT change; foreign book in unrealized GAIN. Threshold-vs-mechanism trap.

**What we're waiting for (current):**
1. **Sumitomo Life FY2025 ESR (Wed May 27)** — pattern-confirmation. M&A-style → confirms downgrade; stress-driven sub-200% → Channel 1 reactivates.
2. **Late-Jun mid-tier ESR** (T&D Holdings, Sony Life, Daido, Taiyo) — consistency check vs Big 3 pattern.
3. **Norinchukin FY2025 (Jun)** — ¥9.7T CLO book direction; independent of mutual lifer pattern.
4. **Any insurer dropping a headline UST/foreign-bond reduction target** (Fukoku-2023-style) — would re-activate Channel 1 immediately.
5. **MOF ITS weekly net selling >¥1.5T sustained** — would suggest forced-selling mechanism firing even if disclosure language stays calm.

**Oil-yen channel — v1.4 inversion (insurer calculus):**
- **Phase 1 mechanism inverted under blockade severity.** v1.3 framing was "oil spike → wider trade deficit → JPY weakens → unhedged FX gains paper over JGB losses." April actual: trade balance posted ¥+302B **SURPLUS** because the blockade collapsed import VOLUMES (-64% YoY crude, -67% YoY ME crude — lowest since 1979). The deficit channel choked on physical-supply destruction, not on oil-cost arithmetic.
- **CPI passthrough also dampened** by government fuel subsidies — April CPI core 1.4% missed 1.7% est. BOJ-hike-urgency-via-oil channel weaker than v1.3 anticipated.
- **Phase 2 inception in progress (May 22-25):** Brent collapsed -12% to $94.53 on Iran/Hormuz MOU optimism. v1.4 framing now expects yen-bullish transmission, but rate differential dominated short-term (USDJPY only -0.24 vs Brent -12%). FX tailwind for unhedged books FADING; ESR pressure on JGB book unchanged.
- **Insurer net:** the FX-cushion-on-unhedged-books leg is weakening as oil resolves. Cross-border forced-repatriation trigger now depends more on June BOJ + ESR mechanism + MOF flows than on FX-driven margin compression.
- See `thesis/THESIS.md` § OIL-IN-YEN STRUCTURAL DYNAMIC for full v1.4 treatment.

**New intel (Aviva Investors, Feb 2026):**
- Insurers using **repacks** (structured cashflows converting foreign-currency assets to yen-denominated notes) to reduce FX noise under J-ICS while keeping yield exposure. Repacks ≠ repatriation but signal desire to reduce FX volatility.
- Purchase decisions now center on "solvency resilience, asset-liability duration alignment, and impairment risk" — confirms ESR is the new governing framework.

---

## KEY DATES

| Date | Event | Watch For |
|------|-------|-----------|
| ✅ Apr 14-25 | FY2026 plans (Big 4) | Zero clean foreign-bond cuts; rotation-within (unhedged → hedged) confirmed. Basis for v1.4 J-ICS finding. |
| ✅ May 13-15 | Dai-ichi FY2025 ESR | ~220% (above 200% trigger; least-representative of Big 4 — most equity-heavy) |
| ✅ May 22 | **Japan April national CPI** | **DOVISH MISS — core 1.4% vs 1.7% est; core-core 1.9% vs 2.2% est. June BOJ pricing softened 74% → 55-65%.** |
| ✅ May 26 | **Nippon Life FY2025 ESR** | **195% (M&A-driven; foreign book +¥3.99T gain). TRUE-in-letter / FALSE-in-spirit. Channel 1 thesis weakened.** |
| ✅ May 26 | **Meiji Yasuda FY2025 ESR** | **208% manageable; foreign book +¥709B gain; Stancorp/Allstate US growth.** |
| **🔴 Wed May 27** | **Sumitomo Life FY2025 ESR** | Pattern-confirmation test. Symetra/US PC ($10.7B stack) is the wild card. M&A-style outcome → v1.5 downgrade confirmed. Stress-driven sub-200% → Channel 1 reactivates. |
| **🟠 Thu-Fri May 28-29** | Tokyo May CPI | Leading indicator for June national. If core-core <1.9% → June BOJ pricing breaks lower from 55-65%. |
| **🔴🔴 Jun 16** | BOJ MPM — BASE CASE HIKE (SAM-21 ~57%; market 55-65%) | If hike fires, insurer asset-side relief on JGB book (yields stabilize); liability-side new constraint (longer-duration liabilities reprice). Net for ESR depends on duration matching. |
| **Jun** | Norinchukin FY2025 results | CLO strategy signals; ¥9.7T book direction (independent of mutual lifer pattern) |
| **Late Jun** | T&D Holdings, Sony Life, Daido, Taiyo FY2025 ESR | Mid-tier reads; consistency check vs Big 3 pattern |

---

## CROSS-REFERENCES

| Doc | What It Covers |
|-----|---------------|
| `research/outputs/LIFE_INSURER_UST_DEEP_DIVE.md` | Full mechanical analysis of JGB losses → UST selling |
| `research/outputs/NORINCHUKIN_CLO_CONTAGION.md` | Norinchukin ¥9.2T CLO book, contagion chain |
| `research/outputs/JAPAN_INSURER_PRIVATE_CREDIT_EXPOSURE.md` | $40-53B PC exposure, double-hit scenario |
| `thesis/THESIS.md` § Channel 1 | Repatriation thesis, flow scenarios |

---

---

## SIGNAL ROUTING — MECHANISM-AWARE (revised post-May 26 Big 3)

**Old rule (deprecated):** *"ANY insurer ESR <200% → 🔴 LIQUID + PROME."* — Too crude. Would have mis-fired on Nippon (195% via Resolution Life M&A, not stress). The market correctly priced that as capital action; the alert rule must do the same.

**New rule — discriminate by mechanism:**

| Condition | Signal | Notes |
|---|---|---|
| ESR <200% **via market losses / forced asset sales / foreign-book stress** | 🔴 LIQUID + PROME | Forced-repatriation mechanism firing. Watch for: foreign securities unrealized LOSS expanding, explicit "reduce foreign bond" / "increase hedging under stress" language, mass-lapse risk cited. |
| ESR <200% via **M&A / capital action / sub-debt**, with foreign book still in unrealized gain | 🟡 counter-thesis note | Threshold breached but mechanism not fired. Document as v1.5 evidence; do NOT route as Channel 1 trigger. Example: Nippon 195% May 26 (Resolution Life subsidiarization). |
| ESR **200-220%** with deteriorating JGB marks but foreign book intact | 🟠 watch | Confirms squeeze but not forced repatriation. Hold thesis weights at base case. Example: Meiji Yasuda 208% May 26. |
| Foreign bond / UST reduction target **explicitly announced** (Fukoku-2023-style) | 🔴 LIQUID + PROME | Direct evidence of Channel 1 mechanism firing — overrides ESR level. |
| J-ICS cited as reason to **avoid 30Y/40Y JGBs** | 🟠 note in STATUS | Confirms v1.4 domestic-curve mechanism. Not Channel 1 routing but tracks J-ICS feed to JGB long-end stress. |

**What to extract from each disclosure (kept as checklist):**
- [ ] **ESR ratio + decomposition:** what drove the YoY delta? Capital action vs economic environment vs new business?
- [ ] **JGB unrealized losses:** mark-to-market figure + YoY change?
- [ ] **Foreign securities mark:** unrealized gain or loss? Direction of change?
- [ ] **Portfolio rebalancing language:** "reduce duration" / "increase hedging" / "diversify away from JGBs"?
- [ ] **Foreign bond commentary:** unhedged-to-hedged rotation continuing? Net direction?
- [ ] **US-subsidiary direction:** growth (Resolution Life, Stancorp) or pullback? Direction-of-travel signal.
- [ ] **Private credit commentary:** any pause on expansion? Gating disclosures?
- [ ] **"Yen appreciation preparation" or "BOJ normalization preparation" language?**
- [ ] **If ESR is WITHHELD:** that IS the signal.

---

*Update this tracker as remaining disclosures land (Sumitomo Wed May 27, mid-tier Late Jun, Norinchukin Jun). Discriminate threshold vs mechanism on every print.*
