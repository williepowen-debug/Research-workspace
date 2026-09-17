# GATE BASIS SWEEP 01 — STRANGER GRADER A
**Date:** 2026-09-17 (Thu) · **Grader:** stranger (no fleet context; graded from the letter alone)
**Inputs read:** `scratchpad/READER_BRIEF_COMMON.md` (Hard rules + Useful commands) · `scratchpad/GATE_LETTERS_A.md`
**Not read (by instruction):** `PROME/GATES.tsv`, any `AGENTS/<owner>/`, any STATUS file, any `definition_surface`.
**Data pulled:** FRED/ALFRED (SOFR99, IORB, EFFR, SOFR, SOFR1/25/75) · CFTC Public Reporting Socrata (`72hh-3qpy` disaggregated futures-only, `kh3c-gbw2` disagg. futures+options, `gpe5-46if` TFF futures-only, `yw9f-hn96` TFF futures+options) · NY Fed Markets API (`markets.newyorkfed.org/api/pd/get/<key>.json`, series break SBN2024) · yfinance `^MOVE` / `^VIX` · DTN Progressive Farmer public article.

## SUMMARY TABLE

| Gate | Verdict | Margin to fire | Letter self-sufficient? |
|---|---|---|---|
| GATE-LIQ-076 | **NOT FIRED** (0-of-3) | (a) 7.7% below record, no >300K cover · (b) all constructions +$60B..+$145B vs −$12B · (c) MOVE 83.90 peak vs >85 | **NO** — leg (b) names buckets the publisher does not publish |
| GATE-LIQ-079 | **NOT FIRED** (never ARMED; FIRE ungradeable by the letter's own terms) | max spread +12.0bp (2026-08-31) vs ≥+30bp | PARTIAL — ARM is gradeable; FIRE self-declares UNGRADEABLE |
| GATE-BRENT-COT-35B | **CANNOT-GRADE (leg B basis undefined)** — Leg A = SPENT; Leg B flips on denominator choice → NO-VERDICT or SPENT | Leg A 107,229 vs ≤109,164 (inside by 1,935) | **Leg A YES** (base reproduces exactly) · **Leg B NO** |
| GATE-FERT-G5 | **NOT FIRED** | MAP $962 (needs +3.95%) · DAP $923 (needs +8.34%) | MOSTLY — instrument named precisely; geography/series-granularity unstated |

---

# GATE-LIQ-076 (owner LIQUID, registered 2026-07-11)

## 1. Condition in my own words
A deliverable-only ("WRITE-UP", explicitly NOT a position trigger) gate that fires when **at least two of three dealer-positioning legs are true inside a two-week window**:
- **(a)** CME 3-month SOFR futures **leveraged-fund gross short** is at or past its record, **OR** a single week's short reduction ("cover") exceeds 300,000 contracts.
- **(b)** Primary-dealer net position in Treasury coupons **>10y is below −$12B**, **OR** the **5–10y** bucket is below −$800mm, **and that condition holds two consecutive weekly prints**.
- **(c)** MOVE **>85** on a session where VIX is **<20**.
"One observation" differs per leg: (a) one weekly CFTC TFF print; (b) a *pair* of consecutive weekly NY Fed PD prints; (c) one daily close pair.

## 2. Questions I had to answer BY ASSUMPTION

| # | Question the letter leaves open | Assumption I made |
|---|---|---|
| A1 | Which CFTC contract is "SOFR-3M"? No market code given. | `134741` "SOFR-3M - CHICAGO MERCANTILE EXCHANGE". (Trap: `134742` is **SOFR-1M**, adjacent code, same exchange.) |
| A2 | TFF **futures-only** or **futures+options**? | Graded futures-only (`gpe5-46if`); cross-checked combined (`yw9f-hn96`). Both agree here. |
| A3 | "lev short" = gross short or net? | `lev_money_positions_short` (gross short, spreads excluded). |
| A4 | "record" over what history? | All-history of the TFF series as published on the Socrata endpoint (first obs 2018-07-24, n=424). |
| A5 | "at/past record" — is the current print compared to the *running* record excluding itself, or the all-time max including itself? | Excluding itself (otherwise every print trivially "at record" when it is the max). |
| A6 | "300K" unit — contracts, or $ notional? | Contracts. |
| A7 | "single-week cover" — week-over-week decline in gross short, or a decline in net? | Δ gross short, consecutive report dates. |
| A8 | "G10>10y" — which NY Fed series? | **No such published bucket exists.** I graded all three plausible constructions (see below). |
| A9 | "G5L10" — which bucket? | Same problem. Constructions below. |
| A10 | Units of (b): "$12B" and "$800mm" — NY Fed publishes $ millions. | −12,000 mm and −800 mm respectively. |
| A11 | (b) net outright position, or long-leg only? | Net outright (`PDPOSGSC-*` is net outright). |
| A12 | (b) "×2 consecutive wks" — does it attach to BOTH sub-legs or only the second? | Assumed both. |
| A13 | (c) MOVE vendor? | yfinance `^MOVE` (ICE BofA MOVE). Letter says "vendor named at grade" — I name yfinance. |
| A14 | (c) "while" — must MOVE>85 and VIX<20 be the **same session**? | Yes (the vintage note says "the same session"). |
| A15 | (c) `>85` / `<20` strict; tie at exactly 85.00 / 20.00? | Strict, so a tie does not fire. |
| A16 | "within 2wk" — 14 calendar days or 10 business days? Measured from the **observation date** or the **publication date**? | 14 calendar days, by observation/reference date: window 2026-09-03 → 2026-09-17. |
| A17 | What resets the 2-of-3 count? | Assumed a rolling window (a leg drops out when its observation ages past 14d). No reset rule is stated. |
| A18 | Does the gate latch once fired? | Assumed no latch (not stated). |

## 3. Observations needed — was the letter precise enough to fetch?

| Element | Series / where | Named precisely? |
|---|---|---|
| (a) series id | CFTC TFF, contract code 134741 | **NO** — name only, no code, no dataset, no futures-only/combined |
| (a) unit | contracts | **NO** (inferred) |
| (a) vintage | "the CFTC TFF weekly print … as first published" | **YES** |
| (a) operator + boundary | "at/past record" (≥) · ">300K" (strict) | **PARTIAL** — "record" referent undefined (history start, self-inclusion) |
| (a) precision / tie | integer contracts; tie at exactly record → fires ("at") | YES |
| (a) consecutiveness | single week | YES |
| (a) reset | — | **NO** |
| (b) series id | NY Fed PD `PDPOSGSC-*` | **NO — the named buckets do not exist** |
| (b) unit | $ millions → $B conversion | **NO** (inferred) |
| (b) vintage | "the two consecutive NY Fed PD weekly prints" | **YES** |
| (b) operator + boundary | "<−$12B", "<−$800mm" — strict less-than | YES |
| (b) precision / tie | $1mm granularity | YES |
| (b) consecutiveness | "×2 consecutive wks" | **PARTIAL** (scope over sub-legs unclear, A12) |
| (b) reset | — | **NO** |
| (c) series id | MOVE index, VIX index | **PARTIAL** — index named, vendor deferred to grade time |
| (c) unit | index points | YES |
| (c) vintage | "closes on the same session" | **YES** |
| (c) operator + boundary | >85, <20 strict | YES |
| (c) precision / tie | 2dp vendor | **PARTIAL** (tie convention unstated) |
| (c) consecutiveness | single session | YES |
| (c) reset | — | **NO** |
| gate-level window | "within 2wk" | **NO** — calendar vs business, observation vs publication date |

## 4. Grade attempt — actual numbers

### Leg (a) — NOT MET
CFTC TFF futures-only, code 134741, `lev_money_positions_short` (source: publicreporting.cftc.gov `gpe5-46if`, pulled 2026-09-17; latest report date 2026-09-08):

| Report date | Lev-money short | Δ wk |
|---|---|---|
| 2026-06-30 | **4,006,610** ← all-time max (n=424, 2018-07-24→2026-09-08) | +174,619 |
| 2026-07-28 | 3,593,844 | −261,446 (largest cover in the series' recent range — still <300K) |
| 2026-09-01 | 3,556,980 | −6,229 |
| 2026-09-08 | **3,698,383** | **+141,403** (an increase, not a cover) |

Latest print is **7.69% below** the record. No week in the 2wk window shows any cover, let alone >300K.
Cross-check, TFF futures+options (`yw9f-hn96`): record 3,819,899 (2026-06-30); latest 3,506,857 (2026-09-08). Same verdict → **A2 is non-decisive today.**

### Leg (b) — NOT MET (robust across all constructions)
The letter's buckets do not exist. NY Fed SBN2024 publishes: `L2`, `G2L3`, `G3L6`, `G6L7`, `G7L11`, `G11L21`, `G21`. Latest print **2026-09-02** (all values $ millions, net outright, positive = net long):

| Series | 2026-08-26 | 2026-09-02 |
|---|---|---|
| G7L11 | 35,028 | 30,910 |
| G11L21 | 64,997 | 66,836 |
| G21 | 51,751 | 46,970 |
| G3L6 | 64,118 | 47,743 |
| G6L7 | 34,958 | 33,399 |

| Construction of ">10y" | 2026-09-02 | vs −$12,000mm |
|---|---|---|
| G11L21 + G21 (">11y") | **+113,806** | +$125.8B above |
| G7L11 + G11L21 + G21 (">7y") | **+144,716** | +$156.7B above |
| G21 alone | **+46,970** | +$59.0B above |

| Construction of "G5L10" | 2026-09-02 | vs −$800mm |
|---|---|---|
| G3L6 + G6L7 | +81,142 | far above |
| G6L7 + G7L11 | +64,309 | far above |
| G7L11 alone | +30,910 | far above |

Dealers are **net long by tens of billions** in every construction. Two-consecutive-week test cannot be met. A8/A9 are **non-decisive today** — but they would be decisive in a stressed tape, which is exactly when this gate matters.

### Leg (c) — NOT MET
yfinance closes, pulled 2026-09-17:

| Date | MOVE | VIX | >85 & <20? |
|---|---|---|---|
| 2026-09-10 | 82.09 | 17.84 | no |
| 2026-09-11 | 82.21 | 15.84 | no |
| 2026-09-14 | **83.90** (window max) | 17.10 | no |
| 2026-09-15 | 83.71 | 17.20 | no |
| 2026-09-16 | 80.73 | 17.71 | no |
| 2026-09-17 | *no MOVE print yet* | 15.42 | — |

Peak MOVE 83.90 — **1.10 points short**. VIX<20 on every session, so the binding leg is MOVE alone.
⚠️ Vendor calendar mismatch observed: `^VIX` returns a 2026-09-07 close (15.30); `^MOVE` has no 2026-09-07 row. "Same session" is unenforceable on a day only one vendor prints.

### VERDICT: **NOT FIRED** — 0-of-3 in the 2026-09-03 → 2026-09-17 window. (Letter records "Graded 0-of-3 7/18"; still 0-of-3.)

## 5. MISREADS (where two reasonable graders diverge)

| # | Ambiguity | Grader 1 | Grader 2 | Decisive today? |
|---|---|---|---|---|
| M1 | **"G10>10y" / "G5L10" name no published NY Fed bucket.** | Sums G11L21+G21 as ">10y" | Sums G7L11+G11L21+G21, or pro-rates G7L11 | No (all far from threshold) — **but decisive in any stress episode**, spread here is $31B between constructions |
| M2 | "record" for leg (a): all-history vs post-COVID vs since-registration | All-history max 4,006,610 → NOT MET | "Record since registration (7/11/2026)" → max would be 3,698,383 = today's print = **at record → MET** | **YES — this single reading flips leg (a) from false to true** |
| M3 | "300K single-week cover" — gross short Δ vs net Δ | Gross Δ: no cover | Net Δ (long−short) could move differently | Not today |
| M4 | SOFR-3M contract code | 134741 (3M) | 134742 (SOFR-1M, adjacent code, 470,684 short — "at record?" is a different question entirely) | Not today (both below record), but levels differ 8× |
| M5 | 2wk window measured by observation date vs publication date | PD data 2026-09-02 is inside by publication (released ~9/10–9/17) | By reference date, 9/02 is 15 days old = **outside** a strict 14-day window | Not today (leg false either way); decisive when the PD leg is the marginal one — PD data carries a ~1–2wk publication lag that the window rule never mentions |
| M6 | "2-of-3" — must the two legs be simultaneous, or merely both inside the window? | Both inside window | Both true on the same date | Not today |
| M7 | MOVE vendor (letter defers to "vendor named at grade") | yfinance ^MOVE 83.90 | A different MOVE feed/settlement could print ≥85 | **Near-decisive** — 1.1 points is inside plausible vendor dispersion |

## 6. Smallest edit removing the largest ambiguity
Replace `PD G10>10y` and `G5L10` with the exact NY Fed keyids and units — e.g. `PDPOSGSC-G11L21 + PDPOSGSC-G21 < −12,000 ($mm, net outright, SBN2024)` — and pin leg (a)'s record as `all-history max of CFTC TFF futures-only code 134741, excluding the print being graded`.

---

# GATE-LIQ-079 (owner LIQUID, registered 2026-07-17)

## 1. Condition in my own words
Two stages.
- **ARM**: the SOFR 99th-percentile rate minus IORB is **≥ +30bp**, on a day that is **not a calendar-pressure day** (month-end / quarter-end / settlement bulge), and this holds on **≥2 consecutive days**. One observation = one business day's (SOFR99, IORB) pair; arming needs ≥4 observations (2 series × 2 days).
- **FIRE**: armed **plus** a "slow-lead backing" leg (EFFR−IORB, above-IORB borrowing volume, or reserve-demand slope) **plus** a dispersion leg.
The letter itself declares FIRE **UNGRADEABLE until those series and thresholds are named on the definition surface** — so a stranger cannot reach FIRE by construction. Extra non-grading constraints ride along (never log as "X1 MET"; does not open the X1 sizing gate; a live fire suspends the wrapper-leads read; RRP is the wrong regime variable).

## 2. Questions I had to answer BY ASSUMPTION

| # | Question | Assumption |
|---|---|---|
| B1 | "SOFR99" — which series? | FRED `SOFR99` (SOFR 99th percentile, NY Fed source). |
| B2 | "IORB" | FRED `IORB`. |
| B3 | Unit of the spread | Percentage points ×100 = bp. |
| B4 | Same-day pairing? IORB prints 7 days/wk, SOFR99 only business days; IORB moved 3.65→**3.90** on 2026-09-17 while SOFR99 for 9/17 is not yet published. | Same-day pairing only; a day with no SOFR99 print is not an observation. (Pairing SOFR99 9/16 with IORB 9/17 would give **−20bp** — a 25bp artifact created purely by calendar mismatch.) |
| B5 | "≥+30bp" — inclusive | Yes, ≥. |
| B6 | **"non-calendar" — what is the list?** | No definition given. I applied: month-end, quarter-end, year-end, mid-month settlement (15th), and major-issuance settlement days. **This is a free parameter.** |
| B7 | "≥2 consecutive days" — consecutive *business* days, or calendar? | Business days (the series' own calendar). |
| B8 | If a calendar day sits between two qualifying days, does it break the run or is it skipped? | **Unstated.** I assumed it breaks the run (conservative). |
| B9 | What resets an armed state? | **Unstated** — no disarm rule, no expiry. I treated ARM as evaluated fresh each day. |
| B10 | "as first published" | Verified via ALFRED. |

## 3. Observations needed

| Element | Series / where | Named precisely? |
|---|---|---|
| Series id (ARM) | FRED `SOFR99`, `IORB` | **YES** (unambiguous short names) |
| Unit / conversion | pp → bp | **PARTIAL** ("+30bp" implies bp; series are in pp) |
| Vintage | "AS FIRST PUBLISHED", ≥4 observations | **YES** — best-specified vintage clause in the set |
| Operator + boundary | ≥ +30bp | **YES** |
| Precision / tie | FRED publishes 2dp (1bp granularity); exactly 30bp fires | **YES** (≥ resolves the tie) |
| Consecutiveness | "≥2 consecutive days" | **PARTIAL** (business vs calendar; gap handling) |
| Reset / disarm | — | **NO** |
| "non-calendar" filter | — | **NO — undefined, and it is a gate leg** |
| FIRE legs | EFFR−IORB / above-IORB borrowing / reserve-demand slope / dispersion | **NO** — letter says so itself |

## 4. Grade attempt — actual numbers
FRED, pulled 2026-09-17. Window 2026-07-17 (registration) → 2026-09-16 (latest SOFR99 print): **43 paired business days.**

| Rank | Date | SOFR99 | IORB | Spread |
|---|---|---|---|---|
| 1 | **2026-08-31** | 3.77 | 3.65 | **+12.0bp** ← series max (and a **month-end**, i.e. the one the non-calendar filter would strike) |
| 2 | 2026-07-31 | 3.75 | 3.65 | +10.0bp (month-end) |
| 3= | 2026-07-28 / 07-29 / 08-04 / 08-17 / 08-25 / 09-01 | 3.74 | 3.65 | +9.0bp |
| — | 2026-09-16 (latest) | 3.70 | 3.65 | **+5.0bp** |

**Days at ≥+30bp: 0 of 43.** Peak is **18bp short** of the arming threshold, and the peak is itself a calendar day.

ALFRED vintage check (`realtime_start=2026-09-11..2026-09-17`): SOFR99 for 09-10/11/14/15/16 each carries a single vintage, `realtime_start` = first business day after the reference date, values 3.70/3.69/3.70/3.72/3.70 — **identical to the current print**. The "as first published" convention is satisfiable and immaterial at this distance from the threshold.

Context (not gate legs, fetched to sanity-check the regime): EFFR−IORB = 3.63−3.65 = **−2bp** flat all window; SOFR−IORB = −3bp on 2026-09-16; SOFR75−IORB = +2bp. No funding tightness anywhere in the distribution.

### VERDICT: **NOT FIRED.** ARM never satisfied (0/43 days ≥30bp; max +12.0bp on 2026-08-31). FIRE is moot, and would be **UNGRADEABLE** by the letter's own terms regardless.

## 5. MISREADS

| # | Ambiguity | Grader 1 | Grader 2 | Decisive today? |
|---|---|---|---|---|
| N1 | **"non-calendar" is undefined.** | Strikes month-end/quarter-end only | Strikes month-end + mid-month settle + issuance settles + FOMC-adjacent days | No (threshold never reached), but it directly controls the gate's *only* filter — and the observed maximum lands on exactly the class it is supposed to strike |
| N2 | IORB same-day pairing on 2026-09-17 (IORB 3.90 posted, SOFR99 not yet) | Skips 9/17 as "no observation" | Uses latest-available IORB against latest-available SOFR99 → −20bp, a pure calendar artifact | Not today, but this is a **live sign-flip mechanism on every IORB step date** |
| N3 | A calendar day interrupting a 2-day run | Breaks the run | Skipped, run continues across it | No |
| N4 | No disarm/expiry rule | ARM re-evaluated fresh daily | Once armed, stays armed until a stated reset (there is none) → **permanent arm** | No today; catastrophic on first arm |
| N5 | FIRE being "UNGRADEABLE, not false" | Reports CANNOT-GRADE for FIRE | Reports NOT FIRED for FIRE | Cosmetic today (ARM fails first) — but the two are **not the same verdict** and the letter is right to say so |

## 6. Smallest edit removing the largest ambiguity
Write the **non-calendar** exclusion as an explicit enumerated day list (e.g. "exclude the last two business days of any month, the first business day of any month, and 15th-of-month settlement dates") — it is the only undefined leg standing between this letter and a fully mechanical ARM grade.

---

# GATE-BRENT-COT-35B (owner BRENT, registered 2026-08-14)

## 1. Condition in my own words
A three-state classifier, not a fire/no-fire gate, run on every weekly COT print (explicitly **"never a latch"** — re-read each print from scratch):
- **Leg A** on crude managed-money **gross shorts** vs a FROZEN base of **122,904.5**: `≤109,164` = **SPENT** · `109,165–118,325` = **NO-VERDICT** (the deadband is decisive, not a coin-flip) · `≥118,326` = **NOT-SPENT**.
- **Leg B**, a gating overlay on managed-money share of open interest: `≤4.909%` = GATING.
- **Both legs must agree**, else NO-VERDICT.
One observation = one weekly CFTC COT print.

## 2. Questions I had to answer BY ASSUMPTION

| # | Question | Assumption / resolution |
|---|---|---|
| C1 | **Which "crude"?** No contract, no exchange, no market code. Owner is named "BRENT". | **RESOLVED BY REPRODUCTION, not by the letter** — see §4. Only CFTC code **067651 "WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE", disaggregated FUTURES-ONLY** reproduces 122,904.5. Tested and rejected: 067411 (ICE WTI), 067651 futures+options, 06765T (NYMEX Brent Last Day), and three ICE Brent-differential contracts. |
| C2 | "MM gross shorts" field | `m_money_positions_short_all` (gross short, spreads excluded). |
| C3 | Base window "6/16-8/4" = which dates? | COT **report dates** 2026-06-16 … 2026-08-04 inclusive = exactly 8 prints. ✔ matches "an 8-obs median". |
| C4 | Median of an even sample | Arithmetic mean of the two centre values → the `.5` the letter insists on. ✔ reproduces. |
| C5 | **Leg B: "OI-share" of WHAT over WHAT?** | **UNRESOLVED.** Assumed `m_money_positions_short_all ÷ open_interest_all` — but on which dataset? |
| C6 | Leg B dataset: futures-only (matching Leg A) or futures+options? | Graded both. **They disagree.** |
| C7 | Leg B direction: does `≤4.909%` mean SPENT, or is it a permission flag independent of spent/not-spent? | Assumed ≤4.909% ⇒ SPENT-direction (that is what "agree" requires to be meaningful). |
| C8 | What does Leg B say when share is **above** 4.909%? NOT-SPENT, or simply "not gating" (= no opinion)? | **Materially unstated.** If "no opinion", then "both agree" is vacuous and the verdict is Leg A alone = SPENT. |
| C9 | Does Leg B have a deadband? | None stated — a single hard boundary against Leg A's explicit deadband. Asymmetric by design or by omission? |
| C10 | Vintage: CFTC revises COT | No vintage clause at all in this letter (unlike 076/079). Assumed current print as of 2026-09-17. |
| C11 | `median_unit 9,160`, `bar -1.0`, `deadband +/-0.5` | Verified: 122,904.5 − 1.0×9,160 = **113,744.5** ≈ the stated centre 113,745 ✔; ±0.5×9,160 = ±4,580 → 109,164.5 and 118,324.5 ✔ match the stated 109,164 / 118,326 rails. **The arithmetic reproduces exactly.** |

## 3. Observations needed

| Element | Series / where | Named precisely? |
|---|---|---|
| Leg A series id | CFTC disagg. futures-only 067651, `m_money_positions_short_all` | **NO in the letter — YES by reproduction** (base is a unique fingerprint) |
| Leg A unit | contracts | YES (implied by level) |
| Leg A vintage | — | **NO** (no vintage clause at all) |
| Leg A operator + boundary | ≤109,164 / ≥118,326, integer rails | **YES** — best-specified boundary set in the whole batch |
| Leg A precision / tie | integers; deadband explicitly "decisive"; centre explicitly NOT a boundary | **YES** — exemplary |
| Leg A consecutiveness | none ("re-read every print, never a latch") | **YES** |
| Leg A reset | explicit REVERT / no latch | **YES** |
| **Leg B series id** | ? | **NO — dataset and denominator both unstated** |
| Leg B unit | percent to 3dp | PARTIAL |
| Leg B operator + boundary | ≤4.909% | YES (operator), **NO** (basis) |
| Leg B above-threshold semantics | ? | **NO** (C8) |

## 4. Grade attempt — actual numbers

**Base reproduction (this is the letter's strongest feature).** CFTC 067651, disaggregated futures-only, `m_money_positions_short_all`, report dates 2026-06-16 → 2026-08-04:

| Date | MM gross short |
|---|---|
| 2026-06-16 | 123,945 |
| 2026-06-23 | 126,811 |
| 2026-06-30 | 122,319 |
| 2026-07-07 | 129,072 |
| 2026-07-14 | 119,187 |
| 2026-07-21 | 123,490 |
| 2026-07-28 | 101,016 |
| 2026-08-04 | 102,560 |

Sorted, centre pair = 122,319 and 123,490 → median = **122,904.5**. **Exact match to the letter.** Rejected candidates: futures+options 067651 median 102,737.5; ICE WTI 067411 median ≈23,738; NYMEX Brent 06765T median 1,538.

**Latest print: 2026-09-08** (COT for Tue 2026-09-15 releases Fri 2026-09-18 — not yet available on 2026-09-17).

| Leg | Basis | Value | Rail | Reading |
|---|---|---|---|---|
| **A** | 067651 futures-only MM short | **107,229** | ≤109,164 | **SPENT** (inside the rail by 1,935 contracts) |
| **B** | 067651 **futures-only** share = 107,229 / 1,939,911 | **5.528%** | ≤4.909% | **NOT gating** |
| **B′** | 067651 **futures+options** share = 87,414 / 2,605,602 | **3.355%** | ≤4.909% | **GATING** |

- Under **B** (futures-only, consistent with Leg A's dataset): A=SPENT, B=not-gating → **legs disagree → NO-VERDICT.**
- Under **B′** (futures+options): A=SPENT, B=gating → **both agree → SPENT.**

I could not reproduce **4.909%** from any construction I tried, which is what leaves C5/C6 open:
- futures-only share, base-window median = **6.372%** (4.909 is 1.463pp below it — no stated unit produces 1.463)
- futures+options share, base-window median = **4.003%** (4.909 is *above* it — wrong side for a "spent" rail)
- 109,164.5 ÷ 0.04909 = implied OI of **2,223,976** — matches neither the futures-only (1.94M) nor combined (2.61M) OI.

Base-rate sanity (last 200 weekly prints, 2022-11-15 → 2026-09-08, futures-only): share ranges 1.298%–8.836%; **119/200 (60%)** are ≤4.909%. So the futures-only reading is a live, non-degenerate rail historically — it is only the 2026 regime (5.4–6.8%) that sits above it. On futures+options, every one of the last 16 prints is ≤4.4%, i.e. the rail would be **always-on**. Neither fact settles which the author meant.

### VERDICT: **CANNOT-GRADE (Leg B basis undefined).**
Leg A is cleanly gradeable and reads **SPENT** at 107,229. The gate-level verdict is **NO-VERDICT** or **SPENT** depending entirely on a single unstated choice of dataset for Leg B. Two competent graders, both obeying the letter, **publish different verdicts today.**

## 5. MISREADS

| # | Ambiguity | Grader 1 | Grader 2 | Decisive today? |
|---|---|---|---|---|
| **P1** | **Leg B dataset: futures-only vs futures+options** | 5.528% → not gating → **NO-VERDICT** | 3.355% → gating → **SPENT** | **YES — this is the decisive misread of the batch** |
| P2 | Leg B numerator: MM short ÷ total OI, vs MM short ÷ MM total (long+short+spread) | 5.528% | A different denominator entirely | **YES** |
| P3 | C8 — what Leg B says above 4.909% | "NOT-SPENT" → disagreement → NO-VERDICT | "no opinion" → Leg A stands alone → **SPENT** | **YES** — a third path to the same fork |
| P4 | "crude" with no contract named | Reproduces the base, lands on 067651 futures-only | Takes the owner name literally and grades **Brent** (06765T: 1,791 shorts — a nonsense comparison to a 122,904.5 base, but a grader who does not think to reproduce the base will not notice the scale mismatch is a *tell*) | Not today for a careful grader; **yes** for a fast one |
| P5 | No vintage clause (unlike sibling gates 076/079, which both carry an explicit WQ-162 convention) | Grades current print | Grades first print | Not today; the omission is the point |
| P6 | Boundary 118,325 vs 118,326 — the letter states both the band top (118,325) and the rail (≥118,326), which are consistent, but the derived value is 118,324.5 | Uses stated integers | Uses derived 118,324.5 and rounds down → 118,324 | No (we are at the other end) |

## 6. Smallest edit removing the largest ambiguity
State Leg B as a full expression with its dataset — e.g. `Leg B = m_money_positions_short_all ÷ open_interest_all on CFTC 067651 DISAGGREGATED FUTURES-ONLY; ≤4.909% = SPENT, >4.909% = NOT-SPENT` — which fixes P1, P2 and P3 in one line and makes the whole gate mechanical.

---

# GATE-FERT-G5 (owner FERT, registered 2026-08-17)

## 1. Condition in my own words
Fires when the **DTN Progressive Farmer weekly retail average price** of **either DAP or MAP** exceeds **$1,000 per (short) ton**. One observation = one weekly DTN retail print for one of the two nutrients; either one clearing the line is sufficient. The letter's whole emphasis is instrument hygiene: this is the **retail $/ton** series, explicitly **not** Pink Sheet $/metric-tonne and **not** NOLA $/short-ton — three series that quote the same commodity at very different levels.

## 2. Questions I had to answer BY ASSUMPTION

| # | Question | Assumption |
|---|---|---|
| D1 | Which DTN geography — national average, or a state/regional average? | **National average** (the figure DTN's public weekly article reports). DTN also publishes **state averages** to MyDTN subscribers; the letter does not say which. |
| D2 | "ton" — short ton, metric tonne? | Short ton (DTN's unit). The letter's own warning against "$/mt" implies it. |
| D3 | `> $1,000` strict; what if a print is exactly $1,000? | Strict `>`, so exactly 1,000 does **not** fire. DTN publishes whole dollars, so an exact tie is realistically reachable. |
| D4 | Which weekly print is "the" observation — the article's stated current week, or the latest row of the trend table? | The article's current-week figure (the trend table is published at ~monthly spacing). |
| D5 | Does the gate latch once a print clears $1,000? Any reset? | **Unstated.** Assumed no latch, graded on the latest print. |
| D6 | Consecutiveness — does one print suffice? | Yes, one print (no "×N weeks" language). |
| D7 | Vintage — DTN restates? | **No vintage clause in this letter at all.** Assumed as-published. |
| D8 | "DAP OR MAP" — inclusive or? | Inclusive; either one firing is enough. |

## 3. Observations needed

| Element | Series / where | Named precisely? |
|---|---|---|
| Series id | "DTN Progressive Farmer weekly retail $/ton", DAP and MAP | **YES** — the most precisely named instrument in the batch, including two explicit *anti*-instruments |
| Unit / conversion | $/short ton (vs $/mt and $/st alternatives called out) | **YES** |
| Vintage | — | **NO** (no clause) |
| Operator + boundary | `> $1,000` | **YES** |
| Precision / tie | whole dollars; tie at 1,000 resolved by strict `>` | **PARTIAL** (tie convention not spelled out, but `>` settles it) |
| Consecutiveness | one print | **YES** (by absence of any N-week language) |
| Reset | — | **NO** |
| **Geography** | national vs state | **NO** |
| Reachability | DTN's weekly series is subscriber-gated; the free article gives the current week + a ~monthly-spaced trend table | **PARTIAL** — a stranger can grade the *current* week but cannot reconstruct the full weekly history |

## 4. Grade attempt — actual numbers
Source: DTN Progressive Farmer, "Fertilizer Prices Continue Lower for 6 of 8 Major Nutrients" (DTN Retail Fertilizer Trends), by Russ Quinn, published **2026-09-16 03:53 CDT**, covering the week **Sep 7-11 2026**. URL: `dtnpf.com/agriculture/web/ag/crops/article/2026/09/16/fertilizer-prices-continue-lower-6-8`. Fetched 2026-09-17.

| Nutrient | Week Sep 7-11 2026 | Threshold | Gap to fire |
|---|---|---|---|
| **MAP** | **$962/ton** | >$1,000 | **+3.95%** needed |
| **DAP** | **$923/ton** | >$1,000 | **+8.34%** needed |

DTN trend table, DRY (national avg $/ton), from the same article:

| Week | DAP | MAP |
|---|---|---|
| Sep 8-12 2025 | 862 | 917 |
| Mar 23-27 2026 | 857 | 906 |
| **May 18-22 2026** | 912 | **953** |
| Jun 15-19 2026 | 910 | 955 |
| Jul 13-17 2026 | 911 | 958 |
| Aug 10-14 2026 | 917 | 960 |
| **Sep 7-11 2026** | **923** | **962** |

MAP has risen 9 consecutive observations but the series **high in the public table is $962** — no print has come near $1,000. DTN's own YoY line: "MAP is 5% higher, DAP is 7% more expensive" vs a year ago; MoM both "slightly more expensive", DTN classing nothing this week as a significant (≥5%) move.

**Letter cross-check:** the letter's registration-date base rate ("MAP +4.3% / DAP +9.1% to the line") back-solves to MAP ≈ $959 and DAP ≈ $917 — which brackets the **Aug 10-14 2026** print (MAP 960, DAP 917) sitting closest to the 2026-08-17 registration date. **The base rate is consistent with the named instrument** (MAP off by ~$1, likely a rounding or a 958/959/960 week choice). The stated "~+0.5% MoM cost-push" also holds: MAP has run +$2 to +$3/month (≈+0.25%/mo) since June, i.e. the observed drift is if anything *slower* than the letter's figure.

### VERDICT: **NOT FIRED.** Neither DAP ($923) nor MAP ($962) exceeds $1,000/ton on the latest DTN weekly print (week of Sep 7-11 2026, published 2026-09-16). At the observed ~+0.25%/mo drift, MAP needs roughly 15 months to reach the line; at the letter's stated +0.5%/mo, roughly 8.

## 5. MISREADS

| # | Ambiguity | Grader 1 | Grader 2 | Decisive today? |
|---|---|---|---|---|
| Q1 | **National vs state average.** DTN publishes state averages behind MyDTN. | National: MAP $962 → NOT FIRED | "DTN retail" with no geography ⇒ any state average >$1,000 fires | **Potentially YES and unverifiable from public data** — with a national mean of $962 and MAP dispersion across states routinely wide, an individual state at >$1,000 is plausible. A stranger cannot check it. |
| Q2 | Which weekly print counts when the article's current week and the trend table's last row disagree | Uses article body (Sep 7-11) | Uses trend table last row (same here) | No |
| Q3 | Latch / reset after a fire | One print fires, done | Requires the print to persist | No today |
| Q4 | Vintage — DTN occasionally restates a week | Grades as-published | Grades revised | No (both ~$40–80 from the line) |
| Q5 | "$1,000/ton" — the letter's anti-instrument warning implies short ton, but never says "short ton" | $/short ton: MAP $962 | If a grader reached for $/metric tonne, $962/st ≈ $1,060/mt → **FIRES** | **YES in principle** — the letter anticipates exactly this and blocks it with the "NEVER conflate" clause, which is why this gate is the best-defended of the four on instrument identity |

## 6. Smallest edit removing the largest ambiguity
Add the geography and the exact figure grabbed: `DTN national average retail price, as stated in the weekly DTN Retail Fertilizer Trends article body (not a state average)`.

---

# CROSS-GATE OBSERVATIONS

| Property | 076 | 079 | 35B | G5 |
|---|---|---|---|---|
| Series id fetchable without guessing | ✗ (a) ✗✗ (b) ~ (c) | ✓ | ✗ (recoverable by base reproduction) / ✗✗ (leg B) | ✓ |
| Unit stated | ✗ | ~ | ~ | ✓ |
| Vintage convention | ✓ (WQ-162) | ✓ (WQ-162, best in batch) | **✗ absent** | **✗ absent** |
| Operator + boundary | ~ | ✓ | ✓ (leg A, exemplary) | ✓ |
| Precision / tie convention | ~ | ✓ | ✓ (leg A — deadband + explicit "centre is not a boundary") | ~ |
| Consecutiveness | ~ | ~ | ✓ | ✓ |
| **Reset / latch rule** | **✗** | **✗** | ✓ ("never a latch") | **✗** |

Three systematic gaps, each visible from the letter alone:

1. **Reset is the most-omitted element in the batch — 3 of 4 letters have no reset or latch rule.** 35B is the only one that states it, and states it well ("REVERT: re-read every print, never a latch"). A gate with a fire condition and no reset condition is only half a specification: it is gradeable once and then undefined forever.
2. **The two letters carrying an explicit vintage convention (076, 079) are the two whose thresholds are nowhere near being touched; the two without one (35B, G5) are the two that are live.** 35B in particular sits 1,935 contracts inside its Leg A rail with no first-print-vs-revised rule, on a series (CFTC COT) that does revise.
3. **Naming an instrument by its common name rather than its publisher key is the single largest source of cross-grader divergence.** 079 names `SOFR99`/`IORB` — unambiguous FRED ids — and is the only letter I could fetch with zero guessing. 076 leg (b) names buckets (`G10>10y`, `G5L10`) that its publisher **does not publish**, which no amount of care resolves: every grader must invent a construction, and the constructions differ by $31B.

## ONE-LINE EDIT PER GATE (largest ambiguity removed, smallest edit)

| Gate | Smallest edit |
|---|---|
| **GATE-LIQ-076** | Replace `PD G10>10y` / `G5L10` with the actual NY Fed keyids and units: `PDPOSGSC-G11L21 + PDPOSGSC-G21 < −12,000 ($mm, net outright, SBN2024)`. |
| **GATE-LIQ-079** | Enumerate the `non-calendar` exclusion as an explicit day list — it is the only undefined ARM leg. |
| **GATE-BRENT-COT-35B** | Write Leg B with its dataset and both directions: `MM short ÷ open interest on CFTC 067651 DISAGGREGATED FUTURES-ONLY; ≤4.909% SPENT, >4.909% NOT-SPENT`. |
| **GATE-FERT-G5** | Add `national average` to the instrument line. |

**If only one edit across the whole batch:** fix **GATE-BRENT-COT-35B Leg B's denominator** — it is the only ambiguity in the set that changes a *published verdict today* (NO-VERDICT vs SPENT), on the only gate of the four that is anywhere near its line.

---
*Report written 2026-09-17 by a stranger grader with no access to GATES.tsv, owner directories, STATUS files or definition surfaces. Every number above carries its source and fetch date. No repository file other than this one was created or modified; no git command was run.*
