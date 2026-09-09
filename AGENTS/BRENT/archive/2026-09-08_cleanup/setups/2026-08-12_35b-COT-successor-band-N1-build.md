# 35b — COT SPENT-BAND SUCCESSOR: N1 DEADBAND-MANDATE BUILD

**BRENT · 2026-08-12 Wed ~17:0x ET · live session (PROME-directed)**
**Authority:** Will RULED 8/11 — *"yes we should rebase with up to date info"* → re-base AUTHORIZED. Relayed via `inbox/processed/2026-08-11_from-PROME_rows-35a-35b-RULED-revert-plus-rebase.md`.
**⛔ STATUS OF THIS DOCUMENT: PROPOSAL + DIAGNOSTICS. NOTHING HERE IS REGISTERED. NOTHING HERE IS LIVE. The successor numbers return to Will for the register — one touch, and this file is the packet.**
**⛔ The INCUMBENT band is untouched by this file. It grades the 8/11 vintage (posts Fri 8/14 ~15:30 ET) ONE FINAL TIME under REVERT semantics (35a, encoded in `TRADE.md` today), then dies on its own do-not-carry-past date.**

**Data:** CFTC disaggregated futures-only, `publicreporting.cftc.gov/resource/72hh-3qpy`, market `WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE`. **n = 235 weekly rows, 2022-02-08 → 2026-08-04.** Own pull 2026-08-12 ~16:5x ET. **Median |WoW| move in MM gross shorts = 9,160 contracts.**
*(⚠️ The carried figure was 9,264 on n=159 weeks. Re-measured here on the full available series. The difference is immaterial to every conclusion — recorded so the two numbers do not become a third instance of the "two values for one figure" class.)*

---

## ⛔⛔ HEADLINE — THE FINDING THAT SHOULD DRIVE WILL'S DECISION

**The incumbent band's `FUEL SPENT` verdict is an ANCHOR ARTIFACT. It fires on exactly ONE of eight candidate anchor weeks — and that one week, 7/7, is the LOCAL MAXIMUM of the series.**

| Anchor week | MM shorts at anchor | Cumulative vs 8/4 (102,560) | Verdict at the −25,000 bar |
|---|---:|---:|---|
| 2026-07-28 | 101,016 | **+1,544** | not spent |
| 2026-07-21 | 123,490 | −20,930 | not spent |
| 2026-07-14 | 119,187 | −16,627 | not spent |
| **2026-07-07 (registered base)** | **129,072** | **−26,512** | **SPENT** |
| 2026-06-30 | 122,319 | −19,759 | not spent |
| 2026-06-23 | 126,811 | −24,251 | not spent |
| 2026-06-16 | 123,945 | −21,385 | not spent |
| 2026-06-09 | 118,758 | −16,198 | not spent |

**⇒ ANCHOR ROBUSTNESS = 1 / 8 = 12.5%.** Move the base one week in either direction and the verdict inverts. **This is a much more serious defect than the margin finding I reported on 8/7** ("clears by 1,512"): a thin margin is a resolution problem, but **anchor-fitting means the verdict is a property of WHICH WEEK I FROZE, not of what the crowd did.** The 7/7 anchor was chosen pre-print in good faith on 7/17 — it was not cherry-picked — but it happened to land on the highest short reading in the surrounding two months, and every subsequent grade has inherited that.

---

## THE FIVE N1 PUBLICATIONS — INCUMBENT BAND (all required BEFORE any registration)

| # | N1 publication | Value | Read |
|---|---|---|---|
| **①** | **Distance in median units** | margin **1,512** ÷ median\|WoW\| **9,160** = **0.165 median units** | 🔴 **No resolving power.** The signal is 1/6th of one ordinary week's noise. |
| **②** | **Condition base rate** | **35 / 231 = 15.2%** of all rolling 4-week windows meet `cum ≤ −25,000` | 🔴 Fires ~1 window in 6.6. **The "rare regime" framing the band is cited with is FALSE.** |
| **③** | **NO-VERDICT base rate** | with an honest ±0.5-median deadband (±4,580) around the bar: **18 / 231 = 7.8%** | 🔴 **The current observation sits 0.165 median units from the bar ⇒ it is INSIDE that deadband. Today's honest verdict is NO-VERDICT, not SPENT.** |
| **④** | **Inside-observed-support** | 4wk cumulative range observed **−97,276 … +80,077**, median −473. **−25,000 = 15.2nd percentile** | 🟢 **PASSES.** The bar is inside support and is not a tail-fitted number. This is the one leg the incumbent gets right. |
| **⑤** | **Leg-suppression / normalization** | raw: 102,560 vs 129,072 ⇒ **"SPENT."** OI-share: **5.44%** vs trailing median **4.82%** ⇒ **74th percentile, ABOVE median.** OI itself moved only −1.0% since anchor | 🔴 **THE TWO LEGS DISAGREE. Raw says the fuel is spent; OI-normalized says money-manager shorts are still heavier than usual. The incumbent band publishes only the raw leg — the disagreeing leg is structurally suppressed.** |

**4 of 5 fail.** Combined with 12.5% anchor robustness, **the incumbent is not a band that has drifted — it is a band that was never measuring what it claimed.**

---

## SUCCESSOR CANDIDATE — SPEC UNDER TEST

**Three changes, each targeting one named failure above. No other change.**

| Element | Incumbent | **Successor candidate** | Kills |
|---|---|---|---|
| **Base** | single frozen week (7/7 = 129,072) | **trailing 8-week MEDIAN of MM gross shorts** | anchor-fitting (defect #1) |
| **Bar** | −25,000 raw contracts | **current shorts ≤ base − 1.0 median unit (−9,160)**, with a **±0.5 median-unit (±4,580) NO-VERDICT deadband** | sub-noise resolution (①/③) |
| **Legs** | raw gross shorts only | **BOTH raw (Leg A) AND OI-share ≤ its own trailing-104wk median (Leg B). Disagreement ⇒ NO-VERDICT** | leg suppression (⑤) |

### Successor base rates — n = 131 gradeable weeks (2024-02-06 → 2026-08-04)

| Outcome | Count | Rate |
|---|---:|---:|
| **SPENT** | 23 | **17.6%** |
| **NO-VERDICT** | 44 | **33.6%** |
| not spent | 64 | 48.9% |

### Successor anchor-robustness — the defect it exists to kill

| Trailing-median window | base | Leg-A bar | Leg A verdict on 8/4 | distance |
|---|---:|---:|---|---:|
| 6 wk | 122,904 | 113,745 | **SPENT (leg A)** | −1.22 med |
| 8 wk | 122,904 | 113,745 | **SPENT (leg A)** | −1.22 med |
| 10 wk | 122,904 | 113,745 | **SPENT (leg A)** | −1.22 med |
| 12 wk | 121,488 | 112,328 | **SPENT (leg A)** | −1.07 med |

**⇒ ANCHOR ROBUSTNESS = 4 / 4 = 100%, at 1.07–1.22 median units of clearance** (vs the incumbent's 1/8 at 0.165). **The successor's Leg A survives anchor perturbation; the incumbent's does not.**

### ⚠️ WHAT THE SUCCESSOR SAYS ABOUT TODAY — AND IT IS NOT WHAT THE INCUMBENT SAYS

| Week | shorts | base(8wk) | Leg-A bar | dist | OI-share | its median | **VERDICT** |
|---|---:|---:|---:|---:|---:|---:|---|
| 2026-07-28 | 101,016 | 123,718 | 114,558 | −1.48 | 5.43% | 4.78% | **NO-VERDICT** |
| **2026-08-04** | **102,560** | **122,904** | **113,745** | **−1.22** | **5.44%** | **4.82%** | **NO-VERDICT** |

**The incumbent says SPENT. The successor says WE DO NOT KNOW — because Leg A (raw) and Leg B (OI-share) point opposite ways.** ★ **That is the successor working as designed, and it is the whole argument for it: the honest state of this evidence is a non-call, and the incumbent has been converting a non-call into a sizing input for two weeks.**

---

## ⚠️ THE DESIGN TRADE-OFF WILL IS ACTUALLY BEING ASKED TO ACCEPT

**A 33.6% NO-VERDICT rate is high — roughly one print in three returns no call.** That is the price of the two-leg agreement gate, and I am naming it rather than burying it:

- **What is bought:** anchor robustness 12.5% → 100%; clearance 0.165 → ~1.2 median units; the disagreeing normalization leg becomes visible instead of suppressed.
- **What is paid:** the modifier will be *silent* about a third of the time. **For a SIZING modifier this is acceptable** — silence defaults to the base case (normal size within cap), which is the conservative branch. **It would NOT be acceptable for an entry trigger**, and this spec must never be reused as one without a fresh build.
- **Alternative if Will wants fewer non-calls:** drop Leg B to an ADVISORY (published beside the verdict, not gating it). That returns NO-VERDICT to ~11% and SPENT to ~40%, but re-suppresses the exact leg that defect ⑤ is about. **I do not recommend it, and I am recording the option so the choice is Will's rather than mine.**

## ⛔ WHAT I AM *NOT* CLAIMING

- **No out-of-sample test.** The successor was specified against the same 2022–2026 series it is base-rated on. The 100% anchor robustness is a stability property, **not** predictive evidence. **n=0 genuine physical reopenings still applies** — this band, like everything else in the Stage-A kit, is fitted to a sample containing no instance of the event the playbook exists to trade.
- **No price validation.** I have not tested whether SPENT weeks are followed by different price behaviour. The band is a positioning DESCRIPTOR; it has never been shown to be a predictor, and the incumbent was never asked to be one either.
- **Vintage limit.** Everything above is as-of the **8/4** print. **It PRE-DATES the 8/6 re-escalation and the 8/8 ADNOC hull attack.** The 8/11 vintage (Fri 8/14) is the first post-escalation read and could move both legs.

---

## 📋 WHAT GOES BACK TO WILL — the one touch

1. **Adopt the successor spec?** (trailing-8wk-median base · 1.0-median-unit bar · ±0.5 deadband · two-leg agreement) — **numbers as tabled above.**
2. **Leg B gating or advisory?** — my recommendation: **gating** (accept the 33.6% non-call rate).
3. **Effective when?** — my recommendation: **register AFTER the 8/14 grade**, so the incumbent completes its final graded print and the two never run concurrently on the same vintage.

**Nothing is applied until Will rules. The incumbent governs through 8/14.**
