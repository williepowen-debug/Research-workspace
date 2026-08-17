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
