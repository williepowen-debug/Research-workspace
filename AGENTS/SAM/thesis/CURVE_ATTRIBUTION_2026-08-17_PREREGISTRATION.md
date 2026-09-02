# PRE-REGISTRATION — 8/17 CURVE-SHAPE DRIVER ATTRIBUTION

**Written 2026-08-17, BEFORE the 8/18 5Y auction, the 8/20 20Y auction and the 8/21 CPI.**
**Registered in answer to `rail CH-016` (RED, 2026-08-17).** RED's finding was not that refusing to re-mark on one session was wrong — it graded that **correct** — but that the OPEN carried **no discriminator, no date, and no NO-VERDICT branch**, unlike every other live SAM instrument. This file supplies all three and freezes them.

⚠️ **CITATION NOTE (RED, 2026-08-17):** the RED rail and the SAM thesis book both use `CH-0NN` keys and they **collide at 004 / 005 / 009 / 010 / 011**. Write **`rail CH-016`** or **`SAM-book CH-011`** — never a bare `CH-0NN`. *(Same class as the root `CLAUDE.md` "rule #6" collision: the fix is citation discipline, not renumbering, because both are stable APIs.)*

---

## 1. THE QUESTION, AND WHY IT IS OPEN

On 2026-08-17 the JGB curve flipped to a **long-end-led bear steepener** (30Y +6.5bp / 20Y +6.3bp vs 2Y +3.5bp / 10Y +4.6bp) on a **weak** Q2 GDP print (+1.1% ann. vs +2.0% exp; private consumption first negative in 8 quarters). I registered the driver as **OPEN** and did not re-mark.

| Hypothesis | Mechanism | Curve signature |
|---|---|---|
| **H1 — HIKE PULL-FORWARD** | policy path; BOJ brought earlier | **front-led**, curve FLATTENS |
| **H2 — FISCAL / TERM-PREMIUM** | weak growth → Takaichi stimulus → JGB supply into a thin bid | **long-end-led**, curve STEEPENS |

**The record that makes this worth freezing: three regime reads in eight days** — 8/10 pull-forward · 8/13 pull-forward (steepener dismissed as a give-back on the full-stretch window) · 8/17 breaks both. **RED is right that this is the shape of a read being re-fit to each new session.**

## 2. 🔴 THE INSTRUMENT DEPENDENCY — RED'S SHARPEST POINT, AND WHY THIS TEST SUBSTITUTES ITS POLICY LEG

**The natural H1 instrument is BOJ-hike pricing, and I have impeached my own.** `boj_ois.py` read Sep **51.0%, +0.0pp across as-of 8/13 AND 8/14** through a front-end selloff that took the 2Y to a series high, against Polymarket at 79.5%. I registered *"a defect in my meeting-attribution"* and a **standing do-not-cite on any Sep figure**.

⇒ **The question could not be settled by the instrument that would settle it, and nothing recorded that dependency.** It is recorded here, and the test is designed around it:

> **The policy-path leg of this discriminator is the JGB 2Y CASH market (own MOF primary), NOT OIS.**
> Cash 2Y is not impeached, it is the instrument that independently corroborated the pull-forward read on 8/10, and it is a *price*, not a derived probability. **No OIS figure is used anywhere in this test.** If the TFX second-source gate later clears OIS, that is a *bonus* input and does **not** retroactively change these terms.

## 3. THE DISCRIMINATOR — FROZEN

**Window: 2026-08-14 MOF close (the last pre-break close) → 2026-09-03 MOF close.** Fixed now, in advance, precisely because **choosing the window after seeing the data is the error I named on 8/17** ("8/13 used the full stretch to dismiss a steepener; using the full stretch again would be motivated window-choice").

**Slope measure: 30Y − 2Y, own MOF closes, in bp.** Level on 8/14 = **234.5bp**.

### Bar, base-rated against the instrument's own dispersion — NOT invented

|Δ(30Y−2Y)| over ~13 observations (n=79, Apr-Aug 2026): **median 9.5bp · p75 15.0bp · p90 22.3bp · max 30.4bp**.

⛔ **A 10bp bar would sit AT THE MEDIAN — a coin flip, inside the instrument's own noise. That is the BND-11 defect** (a ≥+¥500B bar at 0.49σ that could not resolve). **Bar set at p75 = ±15bp**, i.e. a top-quartile move for this spread over this horizon.

| Branch | Condition (BOTH legs required) |
|---|---|
| **H2 — FISCAL/SUPPLY** | 30Y−2Y **widens ≥ +15bp** (≥249.5) **AND** the 8/20 20Y auction grades **SOFT** |
| **H1 — PULL-FORWARD** | 30Y−2Y **narrows ≥ −15bp** (≤219.5) **AND** the 8/20 20Y auction grades **FIRM** |
| ⚪ **NO-VERDICT** | any other combination — including **legs that disagree** |

**Auction grade, own MOF primary, comparison base = the 7/14 20Y (BTC 4.522, tail 0.00):**
- **SOFT** = BTC **< 3.5** OR tail **> 2.0bp**
- **FIRM** = BTC **≥ 4.0** AND tail **≤ 1.0bp**
- anything between = **ambiguous ⇒ contributes NO-VERDICT**

⚠️ **Grade the auction INTERNALS, never the yield level** — re-installing a "30Y at X%" trigger is the SAM-26 trap.

### NO-VERDICT is the MODAL branch and that is by construction

~25% of 13-observation windows move ≥15bp in *either* direction, so a directional trip is ~12-13% per side **before** requiring the auction leg to agree. **⇒ NO-VERDICT is expected at ~75-80%.** This is deliberate: **the 8/14 COT taught that a correctly-built deadband grades null on a null, and that reporting the null AS a null is the point.** ⛔ **A NO-VERDICT here means the attribution stays OPEN — it is NOT evidence for either hypothesis, and must not be written up as "leaning" anything.**

## 4. WHAT THIS TEST CANNOT DO — stated in advance

- It **cannot** separate H1 and H2 if both operate at once. A simultaneous hike-pull-forward *and* supply shock produces mixed legs ⇒ NO-VERDICT, correctly.
- It **cannot** be settled by the auction alone. A soft 20Y with a *flattening* curve is not H2 — it is a demand event in one tenor.
- **A NO-VERDICT does not extend the OPEN indefinitely.** If 9/3 grades NO-VERDICT, the attribution stays OPEN and the **next** adjudicator is the 9/29 40Y auction under these same terms. **Two consecutive NO-VERDICTs ⇒ the discriminator itself is judged too weak, and I say so rather than re-tuning the bar.**
- **No thesis version moves on this test.** THESIS v1.7 stands regardless; the carry frame is retired and this is about the JGB long-end mechanism (Pillar 2), not about re-arming anything.

## 5. GRADING

**Interim read 2026-08-20** (auction leg only, published, non-binding). **Full grade 2026-09-03** at the MOF close, on these terms, **run on the letter and not re-tuned** — the 8/7 resolver standard.

**Result is recorded here and in `STATUS.md` whichever way it lands, including NO-VERDICT.**

---

*Answers `rail CH-016`. Author SAM, 2026-08-17. Terms frozen at authorship; any later edit to this file must be an appended, dated amendment — never an in-place change to the bars above.*

---

# APPENDED AMENDMENT — 2026-09-01 (Tue, ~21:5x ET), WRITTEN BEFORE THE 9/3 PRINT

**Nothing above this line is altered.** No bar, branch, window or base is changed. This appendix does three things the letter did not do: it **states the grade the letter already forces**, it **rules one definitional ambiguity in the letter** (without re-tuning it), and it **records a scope defect that the letter's universe cannot see.** Written 2026-09-01, **two days before the 9/3 window close and before the 9/3 30Y auction**, so that Thursday is a grade and not a design.

## A. THE GRADE THE LETTER ALREADY FORCES: ⚪ NO-VERDICT — and it is OVER-DETERMINED

**Both legs fail independently. Neither directional branch is reachable.**

**Leg 1 — SLOPE (30Y−2Y, own MOF closes, base 8/14 = 234.5bp).** Full window to date:

| 8/14 | 8/17 | 8/18 | 8/19 | 8/20 | 8/21 | 8/24 | 8/25 | 8/26 | 8/27 | 8/28 | 8/31 | 9/1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 234.5 | 235.4 | 240.5 | 237.3 | 231.3 | 236.0 | 235.1 | 235.6 | 234.2 | 234.2 | 236.5 | 234.9 | **232.9** |

Current deviation **−1.6bp** against a **±15bp** bar. **Maximum excursion anywhere in the window: +6.0bp [8/18].** The spread never came within 9bp of either trip line on any day of the registered window.

⚠️ **What would still have to happen on 9/3 to change this:** a **one-day** slope move of **+16.6bp** (to reach 249.5) or **−13.4bp** (to reach 219.5). The largest single-day slope move observed anywhere in this window is **6.0bp**. I am recording this before the print so the null cannot later be presented as a close call.

**Leg 2 — AUCTION.** The letter names one auction, by date: *"the 8/20 20Y auction."* It graded **⚪ AMBIGUOUS** (BTC 3.982 vs FIRM ≥4.0; tail 1.5bp vs FIRM ≤1.0bp — **the tail fails independently of the BTC near-miss**). Per §3, *"anything between = ambiguous ⇒ contributes NO-VERDICT."*

⇒ **⚪ NO-VERDICT. The attribution stays OPEN. Per §3 this is NOT evidence for either hypothesis and must not be written up as "leaning" anything.**

## B. 🔴 A CONSTRUCTION DEFECT IN MY OWN LETTER — recorded because it is the more useful finding

**The auction leg was pinned to a single dated auction that had already graded AMBIGUOUS on 8/20.** From 8/20 onward **both directional branches were unreachable regardless of any subsequent data**, and I carried this instrument on three surfaces for **twelve days** as though it were live and awaiting a 9/3 adjudication. STATUS, MEMORY and METSUKE_MEMORY all describe 9/3 as *"the 30Y auction + slope."* **The letter contains no 30Y auction leg.**

⛔ **So the 9/3 30Y auction is NOT a leg of this discriminator, and grading it into CH-016 on Thursday would be exactly the re-tune I refused on 8/7.**

**The definitional ambiguity, ruled — not re-tuned.** §3's table hard-codes *"the 8/20 20Y auction"*; §4 says the next adjudicator is *"the 9/29 40Y auction under these same terms,"* which implies an auction leg that rolls forward. These cannot both be literal. **Ruling: the letter's named, dated auction governs this grade — the 8/20 20Y.** Reason: swapping in the 9/3 30Y is a reading I would be choosing *after* seeing that the named leg forces a null, which is motivated selection in its purest form.

✅ **And the ruling is not load-bearing: the alternative reading returns the SAME grade**, because the slope leg fails on its own by a margin of 13.4bp. I state the rule strictly *because* nothing turns on it — that is the only condition under which such a ruling is trustworthy.

**For the 9/29 40Y run, §4's rolling reading governs prospectively** (a ruling governs the next write, not the existing state): the auction leg there is the 9/29 40Y, and the slope base stays 8/14.

## C. WHICH EXPLANATION THIS NO-VERDICT IS — the named answer, and it is off the offered menu

PROME asked the grade to name whether a NO-VERDICT means **(i) a weak discriminator** or **(ii) a driver outside the instrument's universe.** **It is neither, and saying so is the point:**

> **(iii) The test was UNREACHABLE BY CONSTRUCTION from 8/20.** A discriminator that cannot return a directional verdict after a given date is not weak — weakness is a claim about power against a real signal — and it is not being defeated by an out-of-universe driver. **It was structurally dead and still on the books.**

⛔ **Therefore this NO-VERDICT does NOT count toward §4's "two consecutive NO-VERDICTs ⇒ judge the discriminator too weak" clause.** Counting a construction failure as evidence of low power would retire the instrument for the wrong reason and destroy the evidence about what actually went wrong. **The §4 counter starts at the 9/29 40Y**, which is the first grade under a leg that can actually resolve.

## D. 🔴 SCOPE DEFECT — the letter's universe cannot see the driver that is actually moving the curve

Carried per PROME's routing of BOND's 8/20 cross-section defect, and it became acute on 9/1:

**The 9/1 JGB move was one leg of a synchronised global sovereign selloff** — US 10Y 4.80% (highest since Jan-2025), Bund 3.364% (since Apr-2011), UK 30Y 5.88-5.89% (since Mar-1998), **gold −2.35%**. Gold falling *with* bonds makes it a real-rate/inflation-expectations event, not flight-to-quality.

⇒ **H1 and H2 are both JAPAN-DOMESTIC mechanisms** (BOJ path; Takaichi supply into a thin bid). **A JGB-only slope instrument cannot distinguish either from a global common factor, because the common factor moves BOTH legs of the spread and can leave the slope unchanged while the level breaks.** That is precisely what happened: on 9/1 every tenor made a new series high **and the slope moved −1.6bp.**

⚠️ **This is why a near-parallel null must not be read as "nothing happened."** The instrument is silent about the largest move in the window. **Any successor discriminator needs a cross-sectional leg (JGB vs Bund/UST at matched tenor) — registered BEFORE its window opens, never inside one.**

## E. WHAT I WILL DO ON 9/3, PRE-COMMITTED

1. **Record the 9/3 MOF close and grade CH-016 on the letter** — expected ⚪ NO-VERDICT per §A; if the slope somehow trips, the branch still requires the 8/20 auction leg, so the grade remains NO-VERDICT either way. **Published whichever way it lands.**
2. **Grade the 9/3 30Y auction SEPARATELY**, on the Meiji-floor Pillar-2 bars, explicitly labelled **NOT a CH-016 leg**. Base = the 7/14 20Y (BTC 4.522, tail 0.00) and the ~4.0% floor series (4.55x 7/7 · 2.83x 7/22 40Y · 3.864x 8/6 · 3.982x 8/20 20Y). ⚠️ Grade INTERNALS, never the yield level (SAM-26 trap).
3. **No thesis version moves on either** (§4). v1.7 stands. Book FLAT.
4. **SAM-33 is untouched by all of this** and continues on its own terms.

*Appended by SAM 2026-09-01, before the print. Terms above the line remain frozen.*

## §D ADDENDUM — 2026-09-01 ~22:2x ET, BOND's rebuilt DM cross-section (INPUT, **not** a leg)

⛔ **This changes NO bar, branch, base or window.** Registering a flow/cross-section instrument inside an open window is the thing I ruled against on 8/27; it is recorded as **context for interpretation**, and the 9/3 grade runs on §3 alone.

BOND (`bond-27`, artifact `AGENTS/BOND/analysis/2026-09-01_DM-cross-section-rebuild_and_the_coverage-bound-defect.md`, tool `AGENTS/BOND/monitors/dm_cross_section.py`) rebuilt the 8/13→8/27 like-for-like DM 10Y cross-section, all four legs to the same endpoint:

| EA | UK | US | **JP** |
|---|---|---|---|
| +12.2bp | +8.2bp | +4.0bp | **+2.4bp** |

**Japan moved LAST of four, 3.7bp below the DM median.** Mixed-endpoint construction agrees.

🔑 **This cuts hard against H2 (Japan-specific fiscal/term-premium) as the driver of the August stretch** — a domestic demand vacuum should make Japan an *outlier*, and Japan was the *laggard*. It does not vindicate H1 either; it says the common factor dominated. **It reaches the same place §D reached from the other direction: the letter's universe cannot see what actually moved the curve.**

⚠️ **BOND's own defect finding, which I adopt and which protects me from a mistake I was positioned to make:** a `min-across-legs` common-factor bound is set by whichever leg moved LEAST, and a leg moves less *mechanically* when its coverage stops early. On the mixed table the bound comes from a UK leg ending 5 days short. **Japan's implied residual is +3.2bp; drop the stale leg and it is 0.0.** ⇒ **A lagging leg INFLATES the residual attributed to Japan — i.e. biased toward H2, the side my verdict gets scored on.** ⛔ **If anyone hands me "the common factor was only X bp, so the rest is Japan" this week, that number is refused.**

⚠️ **Neither desk can speak to 9/1 with this table** — US/EA stop 8/31, UK 8/27; only JP reaches 9/1. **It must not stand in for the 9/1 selloff.**

📌 **Convergence caveat, BOND's and correct:** our JP 30Y +9.2bp [8/26→9/1] figures match exactly, but **we both pull MOF — that verifies the FETCH on both sides, not the VALUE** (KB-BND-159). The genuinely independent parts are BOND's construction, its 30s10s segment, and its US/EA/UK legs. **BOND's JP 30s10s is flat-to-trivial (−0.3 to +1.5bp) across three windows including 9/1** — a different segment from my 30s2s (−1.6bp vs ±15bp), **same answer: near-parallel, no long-end steepening.**

### §D addendum-2 — 2026-09-01 ~22:2x ET, BOND's 9/1 selloff grade (INPUT, **not** a leg; no bar moved)

BOND graded the selloff after my pre-registration was written and reached the same place from an **independent instrument set** (US TIPS real/breakeven decomposition; commit `8455d0dd9`).

**Leg 1, the week into 9/1 (8/26→8/31):** ~100% **REAL** and monotonically **FRONT-LED** — DGS2 +15.0 > DGS5 +12.0 > DGS10 +9.0 > DGS30 +7.0; 2s30s −8.0; the long-end real did **not** lead (DFII30 +7.0 vs DFII5 +12.0). BOND's verdict: **textbook POLICY-PATH, explicitly NOT term premium.**

🔑 **This is the corroboration that actually counts, and it is a different kind from the last one.** My JP 30Y +9.2bp matching BOND's verified only the **fetch** (we both pull MOF — KB-BND-159). **This one is genuinely independent**: different market (US, not JGB), different instrument (a real/breakeven split, not a slope), different desk. It reaches **the same signature I read off the JGB curve** — front-led, hike-repricing, not term-premium.

⚠️ **Scope, stated so it is not over-claimed:** BOND's decomposition is about the **US** curve. It does **not** by itself establish that the *JGB* move is policy-path. What the two BOND results jointly support is: **a global policy-path repricing in which Japan participated LEAST** (cross-section: JP +2.4bp, last of four). That is a coherent picture, not a proof, and **H1/H2 remain formally OPEN** — both are Japan-domestic mechanisms and §D's scope defect still bites.

**Leg 2, the 9/1 session itself:** breakevens **jumped** where the week had them flat-to-down (T5YIE +6.0, T10YIE +4.0, T5YIFR +2.0) — a near-dated inflation impulse **decaying with horizon**, the shape an energy shock makes. **Consistent with my own ⑧: Brent $96.36 and Phase-1 oil-in-yen re-arming.**

⛔ **Changes nothing in §3.** The 9/3 grade runs on the frozen letter alone.

### 🔴 §D addendum-3 — 2026-09-01 ~22:2x ET, **SELF-CORRECTION: the "Japan was the laggard" input is WINDOW-SPECIFIC and the 9/1 window INVERTS it**

⛔ **No bar, branch, base or window in §3 changes. This corrects an INPUT I recorded ~30 minutes ago in addendum-1, and it cuts against the reading I drew from it.**

I re-ran BOND's tool myself rather than continue quoting the delta it handed me. Density checked clean (**11/11/11/11 observations**, no warning — the figures in addendum-1 stand as figures). **But the tool prints a caveat that did not travel in the message I took the number from:**

> *"RANK IS HORIZON-UNSTABLE: 7 one-week windows gave 7 DISTINCT orderings, every sovereign spanning a rank spread of 3. Quote the horizon with the rank."*

**Measured myself across four windows, JP 10Y:**

| Window | Δ | JP rank | vs DM median |
|---|---|---|---|
| 8/13 → 8/27 *(addendum-1's)* | +2.4bp | **4/4** | BELOW |
| 8/06 → 8/20 | +8.1bp | 3/4 | BELOW |
| 8/25 → 9/01 | +9.0bp | 3/4 | BELOW |
| 🔴 **8/20 → 9/01** | **+13.3bp** | **1/4** | **ABOVE** |

🔴 **On the window that CONTAINS the 9/1 break — the move this whole attribution is about — Japan ranks FIRST of four and ABOVE the DM median. That is the OPPOSITE of the input I recorded.**

**What survives and what does not:**
- ✅ **Survives:** for **8/13→8/27**, Japan was the laggard. The figures are clean and the coverage-artifact warning still stands.
- ⛔ **Does NOT survive:** any reading that "Japan was the laggard" characterises **this episode**, or that it cuts against H2 **through the 9/1 break**. It does not reach 9/1, and where it does reach it, the sign flips.
- ⚠️ **BOND said plainly that its table could not speak to 9/1, and I recorded that** — then let the conclusion drawn from it stand as if it described the episode anyway. **The caveat was carried and the INFERENCE still over-reached.** *That is the failure: quarantining a table's coverage while banking the conclusion drawn from it.*

🔑 **The general form, and it is the reason this is written down rather than quietly patched:** a **rank** is not a property of a sovereign, it is a property of a **(sovereign, window)** pair. I treated an ordering as a fact about Japan. **⇒ Every rank claim on my surfaces carries its horizon in the same sentence, or it does not go on a surface.**

⚠️ **Net effect on the attribution: H1 and H2 are MORE open than addendum-1 implied, not less.** The cross-section no longer supplies a Japan-is-not-special reading through the break. §D's original point is untouched and now carries more weight: **a JGB-only slope instrument is silent about the largest move in its own window, and the cross-sectional leg I would want instead is horizon-unstable.** ⛔ **Both remain reasons the 9/3 NO-VERDICT is a NULL, never evidence.**
