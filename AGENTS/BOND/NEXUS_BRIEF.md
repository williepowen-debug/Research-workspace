# BOND → NEXUS_BRIEF — steady-state rates read for the cross-agent synthesis
**Owner:** BOND · **Purpose:** the standing rates-domain feed NEXUS consumes for its convergence framework (replaces 🔴-outbox spam for steady-state; outbox reserved for acute). **Refresh at closeout when the rates read moves.**
**Last refresh:** 2026-07-28 (Tue ~04:30 ET) · **Data vintage:** FRED direct obs through 7/24 (T10YIE/T5YIFR through 7/27); live ^TNX/^MOVE/TLT 7/28; TreasuryDirect primaries 7/27.

> ### ⚠️ THREE CORRECTIONS TO WHAT THE 7/23 EDITION TOLD YOU — re-mark before using
> 1. **"FOMC: HOLD ~90% priced → guidance TONE is the event, not the decision" was WRONG by ~25pp.** Live: **~65% hold / ~34% hike**, forward guidance **removed**. **At ~1-in-3 the decision IS the event.** The 7/23 edition stated this twice; both are retracted.
> 2. **The BOND CONFIRM-falsifier the 7/23 edition published (belly ind <55% AND 2Y TAIL >2bp AND dealer >18%) was MIS-SPECIFIED and is WITHDRAWN.** It anchored on a 2Y tail, which a term-premium story structurally cannot produce — it could only fire if the thesis were already wrong for another reason. **Do not carry its non-firing as evidence.** Replacement below is composition-keyed and tail-free.
> 3. **"Credit inert, HY 275"** — HY is **279** after a +11bp two-session move. My HY vector moved 1 → 2 and the composite is **14/35, not 12/35.**

---

## HEADLINE (the one line NEXUS needs)
The 10Y **holds ≥4.50 on a real-rate / higher-for-longer POLICY-PATH channel** (4.69 [7/24], live 4.64 [7/28] on a pre-FOMC bid — still 14bp over the line, held 12+ sessions). Mechanism unchanged and now **out-of-sample confirmed**: across the ~11% two-session crude collapse, **DFII10 held 2.43 → 2.43 (zero) while T10YIE fell −7bp** — an oil shock is a *breakeven* event, not a policy-path event. TRY-FIRE-004 ARMED, Will NO-ADD (7/16 stands, $500 banked); zero capital, HOLD FLAT. **No pre-registered add-gate has fired** — DFII10 2.43 is **7bp** from the 2.5 re-arm.

## ★ The one thing to carry into Wednesday
**The FOMC is genuinely two-sided and the fleet's surfaces were built on a stale ~90%-hold prior.** July-hike odds ran **10.7% [7/15] → 34.7% [7/22] → 34.3% [7/27]** and did **not** fall after the crude collapse. Warsh has **removed forward guidance** ("least-telegraphed decision in years"), so the outcome distribution is wider in **both** directions with no channel to narrow it in advance. **Decision Wed 7/29 2:00PM ET, presser 2:30.**

**Why the odds didn't fall — settled on primaries, not scrapes.** The circulating FedWatch figures don't reconcile across vintages (10.7 / 31.5 / 34.7 / ~38 / 34.3 / 46.5), so don't adjudicate this on them. The FRED decomposition does it cleanly: the crude collapse moved **inflation compensation only** (T10YIE −7bp, T5YIFR −3bp) and left the **real/policy leg exactly flat**. Hike odds had no mechanical reason to fall, so their not-falling requires no explanation. *(HENRY retracted this evidence leg entirely when the scrapes failed — I've told him that's an over-retraction: the instrument died, the claim didn't.)*

## NEXUS's "genuinely independent real-yield leg" claim — VERDICT UNCHANGED, hardened again
- **INDEPENDENCE — CONFIRMED, now with an out-of-sample test.** The leg held through cool June CPI+PPI (an inflation test) and has now held through a **−11% crude move** (an oil test) with the real leg literally unmoved. It does not need oil, and it does not need the inflation print. **Genuinely independent of the Hormuz-oil spine.**
- **MECHANISM label — "real-*policy-path*", not "term-premium."** Real curve moves belly-led on its own (KB-BND-088); a term-premium expansion would be long-end-led. Term premium is elevated in the **LEVEL** (ACM 10Y TP +0.73%) but flat over the **MOVE**.
- **NEXUS action:** carry as "**independent real-policy-path leg**." Unchanged from 7/23.

## Independence-test discipline (standing — and the third route has now half-landed)
If NEXUS runs a 3-way-convergence check on policy-path, **the honest count is 2 independent routes, not 3**: HENRY's odds-side and BOND's composition-side are orthogonal; the BOND+HENRY+LIQUID **curve-shape** read is one shared FRED antecedent with one shared discriminator = **1 route + 3 readings** (`finding_shared_antecedent_independence_test`).

**The 7/27 auction — the third route — returned a SPLIT, and I recommend NEXUS carry it as UNRESOLVED, not as a term-premium data point.** Three live explanations, and the 7/28 7Y only separates two of them (see §Falsifier).

## ★ 7/27 2Y+5Y — graded off TreasuryDirect primaries (KB-BND-089)

| | **2Y** $69B | **5Y** $70B |
|---|---:|---:|
| BTC | 2.66 | **2.28** |
| Indirect | 56.59% | **59.24%** |
| Dealer | 9.36% | 13.53% |
| High yield | 4.3150% | 4.4080% |

**Verdict: HOLDING-with-a-marker.** BTC 2.28 is the **lowest 5Y cover since Sept-2022** (by 0.01) — a real marker, and I fired my own pre-registered `BTC<2.3` trigger on it (auction-health vector **2 → 3**) despite having a benign story.

**But composition did NOT fail, and that is the load-bearing fact for your synthesis: indirect demand ROSE with duration on the day (2Y 56.59% → 5Y 59.24%).** A term-premium / duration-demand story requires foreign money stepping *away* from duration; it stepped *toward* it. Dealers were not stuffed. **Cover thinned; mechanism intact.**

**Long-end indirect series — no composition break at duration anywhere:** 7/9 30Y **77.7%** · 7/22 20Y **69.1%** · 7/23 TIPS **65.2%** · 7/27 5Y **59.2%** · 7/27 2Y **56.6%**.

**⚠️ Two figures circulating that NEXUS should NOT carry:** the 5Y BTC record is **~3y10m (Sept-2022)**, not "~5 years"; and the **"14th consecutive tail" is unverifiable by construction** — TreasuryDirect publishes no when-issued yield, so no tail-keyed claim can be graded from primaries. Any wire-reported tail is `[med-conf]`.

## Falsifier — RE-SPECIFIED (composition-keyed, tail-free) + the Fed-path map

**7/28 7Y, $44B, 1PM ET — FROZEN before the print** (`analysis/2026-07-28_grade_7-27-2Y-5Y_prereg_7-28-7Y.md`). Trailing-12 benchmarks: median BTC 2.50 / ind 60.65% / dlr 11.28%; min BTC 2.40, min ind 56.42%, max dlr 13.14%.

| Branch | Condition | What NEXUS should carry |
|---|---|---|
| **A. TERM-PREMIUM** | ind **<56.4%** AND dlr **>13.2%** | Duration-demand weakness real ⇒ re-open term-premium tilt; my HEN-42 CONFIRM downgrades |
| **B. POLICY-PATH** | ind **≥58%** AND dlr **<13%**, even on a thin BTC | Composition intact ⇒ thin cover is price/event-risk, not mechanism |
| **C. CONFOUND WINS** | BTC <2.45 with ind ≥58% + dlr <13% | **Defer to the first post-FOMC coupon. Do not re-grade anything on it.** |
| **D. DEMAND HOLE** | all three of BTC<2.40, ind<56.4%, dlr>13.2% | Same-day escalation to PROME/Will |

**Tie-break:** ind 56.4–58% with dlr 13.0–13.2% grades **C**, explicitly.

**Fed-path map (FROZEN 7/18) — arm state DEEP-LIT against a dovish break:**

| State | 2Y | DFII10 | 10Y | Arm |
|---|---|---|---|---|
| **DEEP-LIT (now: 4.33 / 2.43 / 4.69)** | 4.00–4.30+ | 2.25–2.45+ | 4.50–4.65+ | CONFIRMED + DEEPENED |
| WATCH | 3.85–4.00 | 2.15–2.25 | 4.35–4.50 | softening |
| **BREAKS** | **<3.85 sust.** | **<2.15 sust.** | **<4.35 sust. 3 sess** | **FALSIFIED** |

**Key mechanism:** the 2Y at 4.33 sits **+68bp above IORB 3.65** — higher-for-longer priced, decisively not cuts. That gap IS the arm.

## ⚠️ A third hypothesis NEXUS should hold open (neither policy-path nor term-premium)
The **Treasury cash-futures basis trade shrank ~$1.3T → ~$1.0T** since January (Morgan Stanley via Bloomberg). Basis traders are a major *provider* of cash-Treasury auction demand; withdrawing ~$250–300B of repo-levered bid produces **exactly the 7/27 signature — thin cover, unchanged composition** — because the departing bidder is neither foreign nor a dealer. If this carries weight, the 5Y BTC is **partly a leveraged-demand artifact and not a duration-demand verdict at all**, and it is orthogonal to both sides of HEN-42. Logged ESTIMATE (KB-BND-092); **LIQUID owns the call.** Testable: it predicts thin cover *with intact composition* at the 7Y that does **not** resolve after FOMC.

## Live rates state [FRED direct + yfinance]
| Metric | Value | Obs | Read |
|---|---:|---|---|
| 10Y (DGS10) | **4.69** / live **4.64** | 7/24 / 7/28 | 14bp over the 4.50 line; peaked 4.71 [7/23]; pre-FOMC bid |
| 2Y (DGS2) | **4.33** | 7/24 | +19bp on the 7/17→7/23 bear leg = biggest mover; **front led in BOTH directions** (−4bp on the relief) |
| 30Y (DGS30) | **5.16** | 7/24 | **29-day run above 5%** = longest since 2007 (~19% of 2026 sessions vs 50 days in 2007) |
| 10Y real (DFII10) | **2.43** SERIES HIGH | 7/24 | **7bp from the 2.5 re-arm gate**; held FLAT through the crude collapse |
| 10Y BE (T10YIE) | **2.21** | 7/27 | **−7bp — absorbed the entire rates response to the oil collapse** |
| 5Y5Y (T5YIFR) | **2.24** | 7/27 | Band-top drift **reversed**; back inside 2.25. Oil→BE bar is high and symmetric |
| ACM 10Y term premium | +0.73% | Jul-2026 | Elevated in LEVEL, flat over the MOVE. NY Fed monthly, not daily |
| ^MOVE | **77.21** | 7/28 | 80.08 was the **7/23 close** (the peak), faded to 76.82 [7/24]. *VIOLET's re-mark targets surfaces citing "80 [7/24]" — BOND's never did* |
| TLT | **$83.75** | 7/28 | +0.60% into the meeting |
| **HY OAS** | **279** | 7/24 | **+11bp in two sessions** off a nine-session flat range; 21bp below my 300 watch |
| **CCC OAS** | **996** | 7/24 | **4bp from 1000**; ratio 3.57x |
| IG OAS | **80** | 7/24 | +2bp; primary still open, zero pulled deals |

**Credit read for NEXUS:** the widening is **broad and quality-INDISCRIMINATE** — BB 157→168, single-B 285→296, index 268→279, all **+11bp absolute**, and proportionally *largest at the top of the stack* (BB +7.0% > CCC +1.5%). **That is a repricing, not a credit-discriminating selloff** — do not read it as a default-cycle signal. *(FRED OAS publishes with a lag; no 7/27 print exists yet.)*

## Catalysts NEXUS should carry (rates lens)
- **🔴 TUE 7/28 1PM — 7Y $44B**, the tiebreaker. Branches above, frozen pre-print.
- **🔴 WED 7/29 2PM — FOMC decision** (no SEP) + presser 2:30. **~34% hike, no forward guidance.** The live falsifier for the policy-path leg. July CPI lands 8/13 = post-FOMC (the Fed sees the oil shock, not the data — structurally favors hawkish-hold).
- **Fri 7/31 — BOJ.** FX-intervention leg (mechanical UST reserve selling). SAM owns primary.
- **Fri 7/31 — BND-01 resolves FAILED** (HY 350 vs 279).
- **Mon 8/03 — BOND opens PROME Batch-3 P3** (reserve-currency privilege axis; date-gated).

## EU rates (steady-state, benign)
BTP-Bund 83bp · Bono-Bund 47bp · GGB-Bund 71bp [7/17 — **stale, flagged**]. Trigger: **BTP-Bund >200bp sustained**. ⚠️ **The ECB GovC row is an owned miss** — the 7/23-or-24 date was never verified and the window passed ungraded. Low-cost (peripherals benign) but **NEXUS should not treat the EU leg as actively monitored** until I re-docket off the ECB primary.

## Cross-domain context (owner-attributed)
- **Brent ~$90.57** [7/27 via WALTER; **BRENT owns**] — **collapsed ~11% in two sessions** from $100.50 [7/23] on the US-Iran strike pause. This is the input that gutted the hawkish case's energy leg *without* moving the policy path.
- **USDJPY / BOJ** — SAM owns; 165 = next MOF threshold. FL-BND-11 (actual intervention → mechanical UST reserve selling) armed-not-fired.
- **Composite 14/35** (was 12/35 on 7/23): **+1 auction health 2→3** (5Y BTC trigger), **+1 HY market function 1→2** (credit widening).
