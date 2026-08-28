# BRENT — 2026-08-28 Fri · **REGIME VERDICT (owed since 8/26) · BZ 8/26 THREE-WAY ENDPOINT RECONCILE · DR-4 RE-RATE**

**Written:** 2026-08-28 Fri ~10:3x–11:0x ET, markets OPEN · **Session:** PROME-orchestrated Friday slate (Will "start the Friday slate", 8/28 AM)
**`$0` moved · no position changed · no threshold registered · no gated surface touched.** Gated needs are returned to PROME in §E.
**Every figure below is either an own pull dated in-line, or a named desk's figure cited to that desk.**

---

# §A — REGIME VERDICT

> ## ⚖️ **VERDICT: PAPER-PREMIUM UNWIND ON A DEAL PATH. THE PHYSICAL PREMIUM DID NOT UNWIND WITH IT.**
> **Regime label: `DIPLOMATIC DE-RATING / PHYSICAL UNCHANGED`.**
> The 8/26 Iran–Oman interim framework repriced a **deal path nobody has signed**. It did **not** reprice the cost of moving a Gulf barrel, the insurability of the corridor, or the near-dated probability of normalisation. **Three independent physical/insurance witnesses all read UNCHANGED-or-TIGHTER across the same window in which flat price fell −6.94%.**

## A1 — The three witnesses that the PHYSICAL premium is intact

| # | Witness | Reading | Source · date | Direction |
|---|---|---|---|---|
| 1 | **Marine war-risk listing** *(mine)* | **JWLA-034 (29 Jul 2026) is still the newest circular** — no successor two days after the framework; Persian/Arabian Gulf + Gulf of Oman still Listed Areas | own pull, IUA JWC Risk List, **HTTP 200 / 79,912 B, 2026-08-28 ~10:5x ET**; circulars seen JWLA-027…034, nothing ≥035 | **INTACT** |
| 2 | **Freight / delivered cost** *(RED's, cited)* | TD3C MEG–China TCE **>$520,000/day [8/19]** vs **$412,888/day [6/16]** — **new highs while flat price round-tripped twice** | RED CHG-042 RESOLVED 8/27, Lloyd's List Intelligence Hormuz Brief 8/19 / LL1157473 6/16 | **INTACT → RISING** |
| 3 | **Event pricing** *(ORACLE's, cited)* | Hormuz-normal-by-Dec-31 **32.5%** (46.5% on 8/12); normalisation **by Sep-15 = 1.4%**, **by Aug-31 = 0.4%** | ORACLE 8/27 live scan (packet consumed this session) | **near-dated normalisation priced ≈ 0** |

⚠️ **Witness 2 is RED's series, not mine, and I say so because I cannot check it:** my VLCC/Worldscale threshold was **RETIRED 2026-07-31** on the explicit finding that *"I have NO Worldscale/freight-rate feed anywhere in my kit."* **I hold no independent TD3C vintage, so RED's figure is not contradicted by anything I own — it stands, and RED's own caveat rides it: all three relays trace to Baltic TD3C, one instrument, several relays, and TCE conflates risk premium with hull scarcity.** *(RED's re-grade offer is therefore not taken up — I have no figure to beat it with.)*

## A2 — The paper leg over the same window (own pulls, CLOSES, contract named)

| series | 8/21 close | 8/26 close | 8/27 close | 8/28 ~10:5x live |
|---|---|---|---|---|
| **Brent BZV26 (Oct26)** | **94.39** | **87.84** (−6.94% vs 8/21) | 89.70 | 89.01 |
| Brent BZX26 (Nov26) | 92.67 | 86.94 | 88.52 | 87.76 |
| Brent BZZ26 (Dec26) | 89.99 | 85.09 | 86.34 | 85.65 |
| **M1−M3 (V26−Z26), closes** | **+4.40** | **+2.75** | **+3.36** | **+3.36** |
| `^OVX` | 49.62 | 46.83 | 46.22 | **44.72** (−9.9% vs 8/21) |
| WTI `CL=F` | 87.06 | 82.23 | 83.53 | 82.81 |

### ⛔ CORRECTION TO MY OWN 8/27 CURVE READ — the trend word was wrong and the cause was basis-mixing
My 8/27 packet §2② said **"prompt scarcity is easing alongside the level."** On a **consistent close basis** the flattening **BOTTOMED at +2.75 [8/26 close] and RE-STEEPENED to +3.36 [8/27 close, held 8/28]**. Prompt scarcity eased into 8/26 and has **partially re-tightened since** — a two-session event, not a trend.
**Cause:** I compared an **08:37 intraday** read (+3.01) against an **8/24 intraday** read (+4.36); on closes 8/24 was **+4.07**. Mixing intraday and close reads across a series manufactured a trend. Same disease as §B. *(This is the fourth instance on this desk of a live bar doing the work of a settle — see the STATUS tombstones for 8/07, 8/10, 8/20.)*
⚠️ **BZV26 expires ~8/31**, so M1−M3 on the V/X/Z legs has ≤2 sessions left. Successor basis once Oct dies: **X26−F27 = 87.76 − 83.44 = +4.32 [8/28 ~10:5x]** — recorded now so the series does not silently change definition next week.

## A3 — ⚑ NAMED, CHECKABLE RESOLUTION → **BRT-30, registered this session**

> **BRT-30 (registered 2026-08-28, confidence 80%, resolves 2026-10-26):**
> **The 8/26 Iran–Oman interim framework does not produce a physical corridor re-rating inside its own 30–60d permanent-route window.** Operationally: **on 2026-10-26 the JWC still lists BOTH the Persian/Arabian Gulf AND the Gulf of Oman as Listed Areas — i.e. no circular numbered ≥ JWLA-035 removes either area.**
>
> - **Instrument:** JWC/IUA Listed Areas page, **circular NUMBER as the change detector** — registry row `KILL-LEG2-JWC-LISTING`, frozen baseline **JWLA-034 / 29 Jul 2026**. *(Reachability is not change-detection; the number is the detector. Probed clean today.)*
> - **CONFIRMED** — newest circular on 2026-10-26 still lists both areas.
> - **FAILED** — any circular ≥ JWLA-035 removes Persian/Arabian Gulf **or** Gulf of Oman.
> - **SPLIT** per `[[finding_threshold_vs_mechanism]]` — a permanent route **IS** signed but the listing persists ⇒ mechanism-confirmed / diplomatic-threshold-reached, and the regime verdict survives.
> - **Window referent:** DOCKET row 229 / `docket/CATALYSTS.tsv` 2026-10-10 (30–60d = ~9/25–10/25); **10/26 is the day after the outer edge**, so the row cannot resolve early on a still-open window.

**Why 80% and not higher:** the JWC has held the Gulf listing continuously through the entire war — **JWLA-025 → 034, ten circulars, zero removals** — and the near-dated event market prices Sep-15 normalisation at **1.4%**. **Why not 90%+:** the outer edge is 59 days out, a permanent-route signature is a genuine live possibility, and **n = 0 on "interim framework → delisting" in either direction — there is no precedent, so the base rate is about the listing's persistence, not about frameworks.**

⛔ **NON-CLAIMS THAT TRAVEL WITH BRT-30:** it is **not a price prediction** and says nothing about where Brent trades. It tests the **REGIME** (is the physical premium intact), never the **LEVEL**. It is **not** a re-arming of any retired falsifier and registers **no threshold** — it grades an existing registry row's standing negative on a date.

## A4 — What the verdict does to the thesis and the ladder

| Object | Effect | Detail |
|---|---|---|
| **THESIS v5.7** | **UNCHANGED — no version bump** | The verdict is a refinement the thesis already anticipates: v5.4's central claim is that **signature and throughput are priced as different objects**, and that is exactly a paper/physical divergence. ORACLE's 8/27 retraction explicitly leaves that claim untouched (its σ were withdrawn; every dH sign and H level reproduces). CHANGELOG entry, no bump. |
| **$100 posture** *(fired 7/23)* | **NOT re-armed, NOT retired. Distance re-read.** | **$10.99 away on BZV26 [8/28 ~10:5x, 89.01] = 12.3%.** Was **$5.61 / 5.9%** at the 8/21 close ⛔⛔ **SELF-CAUGHT 2026-08-28 ~11:1x ET BY ARITHMETIC AUDIT OF MY OWN WORK, AND IT ORIGINATES IN MY 8/27 PACKET: the `$6.22 away at the 8/21 close` I published yesterday AND repeated in today's first write is the `8/20` CLOSE (`BZV26 93.78`), NOT the 8/21 close (`94.39`). At the 8/21 close the distance was `$5.61 = 5.9%`. ★ THE SHAPE IS THE ONE THIS DESK KEEPS FINDING IN OTHER PEOPLE'S WORK: an EXACT figure (`$6.22` is exactly `100 − 93.78`) sitting beside a WRONG DATE LABEL, which is why it reads as verified — `[[finding_exact_level_authenticates_a_wrong_direction]]`, and it is the same off-by-one-session class as the `86.36` endpoint I spent this morning reconciling. I caught it by re-deriving every published distance from the contract series rather than by any check. ⇒ THE CLAIM SURVIVES AND STRENGTHENS: the distance did not merely double 8/21→8/26, it went `5.61 → 12.16` = **2.17×**. Corrected in place, left visible.**; $12.16 / 13.8% at the 8/26 close. ⚠️ **My 8/27 packet quoted "$13.75 away / 15.6%" off an 08:37 intraday bar — that reading was the widest point and is superseded by the close-basis series above.** **The threshold did not move; the distance roughly doubled 8/21→8/26 and has since NARROWED by $1.17.** |
| **BRT-26 (rigs)** | **Unaffected by the regime call** | Rigs lag price 4–8 weeks (my own 7/21 direction error), so today's print reflects June/July capex decisions and contains neither the run to $94 nor the −6.94% give-back. Graded on its own print at 13:00 — see §D. |
| **BRT-29 (demand destruction)** | **Unaffected today; premise leg still armed** | Boot: `GASREGW 4.085 [8/24]` — still ≥$4.00. No grade owed this session. |
| **Positions** | **NO CHANGE PROPOSED. $0 moved.** | TERRY's concentration flag reads the same as 8/27: **the falsifier is MOVING, not FIRED** — and §A1 is the evidence for "moving, not fired," because a genuine thesis break would show up in the JWC listing and the freight tape first, and neither has moved. |

---

# §B — BZ 8/26 THREE-WAY ENDPOINT RECONCILE

**Ask (PROME):** WALTER 86.36 / PROME 86.21 / BRENT 87.84 — name each figure's series and contract, name the like-for-like endpoint, give the reconciled number. **The certified −6.94% depends on it.**

> ## ✅ **RECONCILED. The certified −6.94% STANDS — and the discrepancy is TWO defects, not one, neither of them a desk error.**

## B1 — Finding 1: yfinance's `BZ=F` **DAILY** and **INTRADAY** series rolled on **DIFFERENT DATES**, and disagreed about what "front" meant for three sessions

All evidence own pulls, 2026-08-28 ~10:4x ET, reproducible:

| test | result |
|---|---|
| **DAILY** `BZ=F` OHLCV vs `BZV26.NYM` (Oct), 8/19→8/27 | **byte-identical every session** (e.g. 8/26 O 86.95 H 89.48 L 85.48 C 87.84 vol 15,243) |
| **DAILY** `BZ=F` OHLCV vs `BZX26.NYM` (Nov), 8/28 | **byte-identical** (O 88.60 H 88.72 L 87.27 C 87.78 vol 13,179) |
| ⇒ | **the DAILY series rolled Oct→Nov on 8/28 — TODAY** |
| **INTRADAY** `BZ=F` (1h), aggregated to exchange trade-date (18:00 ET roll), 8/25 | low **85.01** = BZX26 8/25 low **85.01** exactly *(BZV26 low was 86.09)* |
| same, 8/26 | high **88.28** / low **84.59** = BZX26 8/26 high **88.28** / low **84.59** exactly *(BZV26 was 89.48 / 85.48)* |
| same, 8/27 | high **89.15** = BZX26 8/27 high **89.15** exactly *(BZV26 was 90.34)* |
| same, 8/24 | low **91.78** = **BZV26** 8/24 low **91.78** *(BZX26 was 90.19)* |
| ⇒ | **the INTRADAY series rolled Oct→Nov between 8/24 and 8/25** |

⇒ **For 8/25, 8/26 and 8/27, one vendor's single ticker `BZ=F` resolved to TWO DIFFERENT CONTRACTS at the same moment depending on which resolution you asked for.** Daily = Oct. Intraday = Nov.

### ⛔ THIS RETRACTS MY OWN 8/27 CLAIM
STATUS row 16 and PROME packet §1 (8/27) both say *"BZ=F has ALREADY ROLLED off Oct to Nov as front, EARLIER than expected… rolled somewhere in the 8/24-27 window."* **Half right and wrong where it mattered: the INTRADAY series had rolled; the DAILY series had not — and every "8/26 close" any desk quoted came from the daily series.** I inferred a roll from a **single 08:37 intraday quote ($87.27)** and generalised it to the daily series without opening the daily bar. `[[finding_continuous_front_ticker_rolls_so_deltas_lie]]` — **plus a twin this desk had not named: a continuous ticker's roll date is a property of the RESOLUTION you request, not of the ticker.**

## B2 — Finding 2: **86.36 and 86.21 are evening electronic-session last-trades, not 8/26 closes**

`BZ=F` 5-minute bars, 8/26 (own pull):

| figure | first touched | context |
|---|---|---|
| **86.36** | **09:45 ET 8/26**; also the level through ~21:00–22:00 ET | WALTER's pull is timestamped **02:35Z 8/27 = 22:35 ET 8/26** — the evening electronic session |
| **86.21** | **22:40 ET 8/26** | after Brent's 18:00 ET reopen ⇒ **exchange trade-date 8/27**, not 8/26 |

**Neither equals any named contract's 8/26 daily close:** BZV26 **87.84** · BZX26 **86.94** · BZZ26 **85.09**.
*(Confirmation: `BZ=F` 1h closes on 8/26 run 86.64 [14:00] → 86.58 [15:00] → 86.56 [16:00] → 86.55 [23:50]. The daily-bar close of 87.84 is the Oct contract; the intraday tape is the Nov contract. Both are "true," about different objects.)*

## B3 — ⇒ THE RECONCILED NUMBER

| figure | what it actually is | verdict |
|---|---|---|
| **BRENT `87.84`** | yfinance **DAILY** `BZ=F` close for 8/26 = **BZV26 (Oct26) settle-basis**, proven by exact OHLCV identity with the named contract | ✅ **THE LIKE-FOR-LIKE ENDPOINT** |
| WALTER `86.36` | `BZ=F` **intraday last-trade**, on the **Nov-basis intraday series**, captured **22:35 ET 8/26 = trade-date 8/27** | not a close, and not Oct |
| PROME `86.21` | same series, captured **≥22:40 ET 8/26 = trade-date 8/27** | not a close, and not Oct |
| *(reference)* BZX26 `86.94` | Nov26 **daily close** 8/26 | the correct Nov endpoint if a Nov basis is wanted |

> ### ✅ **CERTIFIED, SAME CONTRACT, SAME BASIS: BZV26 `94.39` [8/21 close] → BZV26 `87.84` [8/26 close] = −$6.55 / −6.94%.**
> **The −6.94% figure is CONFIRMED and travels unchanged.**

**And the −8.5% decomposes completely — none of the extra 1.57pp is price:**

| component | $ | pp |
|---|---|---|
| like-for-like BZV26 move (Oct close → Oct close) | −6.55 | **−6.94** |
| **contract basis** (Oct 87.84 → Nov 86.94, same day) | −0.90 | −0.95 |
| **trade-date / timing** (Nov 8/26 close 86.94 → evening print 86.36) | −0.58 | −0.61 |
| **total 94.39 → 86.36** | **−8.03** | **−8.51** ✅ reproduces WALTER's −8.5% to the decimal |

*(PROME's 86.21 endpoint: identical first two lines, timing leg **−0.73 / −0.77pp** ⇒ **−8.67%**.)*

## B4 — 🔴 **THE SAME DEFECT IS LIVE ON TODAY'S TAPE — this is not a post-mortem**

PROME's 10:30 ET tape line reads **"Brent $87.81 (−1.89)."** `BZ=F`'s **daily** series rolled to Nov **today**, so **−1.89 measures Nov-today against Oct-yesterday.** Like-for-like:

| basis | 8/27 close | 8/28 ~10:5x | move |
|---|---|---|---|
| **Nov (BZX26)** — the new front | 88.52 | **87.76** | **−0.76 / −0.86%** |
| Oct (BZV26) — the old front | 89.70 | 89.01 | −0.69 / −0.77% |
| ⛔ cross-roll (what −1.89 measures) | 89.70 *(Oct)* | 87.81 *(Nov)* | −2.11% |

> **Today's Brent move is ≈ −0.8%, not −2.1%. The reported figure overstates it by ~$1.1 ≈ 1.2pp, and all of it is roll.**

## B4-bis — ✅ WALTER INDEPENDENTLY DERIVED THE SAME ANSWER MID-SESSION — AND I REFINE ONE HALF OF IT

**`SIG-W-20260828-006` + packet, arrived ~15:0xZ while this was being written** (WALTER `walter-0828`, own yfinance pull ~14:5xZ, independent of mine). **WALTER concludes: BRENT's 87.84 is CORRECT, its own 86.36 was a live tick mislabelled as a close, the certified −6.94% stands, `BZ=F` rolled today, and this morning's −1.98% headline is a roll artifact worth ~1.2pp.** ⇒ **Two desks, two independent derivations, same headline. WALTER has published the correction on the BOARD and is fixing all four of its own surfaces (`anchors/IRAN_WAR.md` banner + ADDENDUM #21, `SIG-W-20260826-001`, its STATUS live-levels block).** Nothing owed either direction on the headline.

### ⚑ ONE REFINEMENT, AND I HOLD THE MEASUREMENT FOR IT
WALTER writes: *"you and I were on the SAME CONTRACT. The disagreement was settle-vs-live-tick across a session boundary, **never contract choice**."* **True of the DAILY series. Not true of the series WALTER's `fetch.py price BZ=F` actually hit — and that is the intraday feed, which had ALREADY rolled.**

**Discriminating test — trade-date OPENS (own pull, `BZ=F` 1h aggregated on the 18:00 ET roll):**

| exchange trade-date | `BZ=F` intraday open | `BZV26` (Oct) daily open | `BZX26` (Nov) daily open | match |
|---|---|---|---|---|
| 2026-08-27 | **86.65** | 87.56 | **86.65** | ✅ **Nov, exact** |
| 2026-08-28 | **88.60** | 89.51 | **88.60** | ✅ **Nov, exact** |

*(Corroborating, same pull: intraday 8/26 high/low **88.28 / 84.59** = BZX26 exactly, vs BZV26's 89.48 / 85.48; intraday td-8/28 close **88.02** = BZX26 close **88.02** exactly.)*

⇒ **WALTER's 86.36 (23:0x ET 8/26) and PROME's 86.21 (22:40 ET 8/26) were BOTH Nov-basis live ticks on exchange trade-date 8/27.** WALTER's own diagnosis of *when* is exactly right and is the bigger half; what it could not see from daily bars alone is that the tick was also *a different contract*. **Consequence for the decomposition: the extra 1.57pp splits −0.95pp CONTRACT / −0.61pp TIMING (§B3), not 1.57pp of timing.** *(WALTER's note that BZV26's 8/27 daily low 86.29 "brackets" 86.36 is a range coincidence — both contracts' 8/27 ranges contain 86.36; the OPEN is the discriminator.)*
⛔ **This changes NO headline: 87.84 stands, −6.94% stands, the roll artifact stands. It changes the ATTRIBUTION, and attribution is what stops the fix being aimed at the wrong thing** — a pure timing diagnosis would have someone "just pull after the settle" and still get a Nov number on an Oct question. **Delivered to WALTER as a refinement, not a dispute; WALTER's surfaces are WALTER's.**

### Two live reads of today's move, minutes apart, both under 1%
| desk | time | `BZX26` | vs 8/27 close 88.52 |
|---|---|---|---|
| BRENT | 8/28 ~10:5x ET | 87.76 | **−0.86%** |
| WALTER | 8/28 ~14:5xZ (~10:5x ET) | 87.87 | **−0.73%** |
**⇒ Today's Brent move is `−0.7%` to `−0.9%` — call it "under 1%", never −2%.**

### WALTER §4, adopted into the verdict — the bypass leg is NOT de-risked
WALTER killed a low-tier *"Yanbu / Red Sea exposure"* item on novelty and carried forward the **framing**, which I adopt: **the Iran–Oman interim framework de-risks the HORMUZ track. The Red Sea / Yanbu leg of the BYPASS route is a separate vector and is not de-risked by it.** ⇒ **The −6.94% is a HORMUZ-TRACK repricing and does not price the bypass-route leg at all.** That is a fourth reason the paper unwind overstates the physical improvement, and it is now part of §A's verdict.

## B5 — ⇒ REPORTING RULE ADOPTED (mine, forward, from today)

> **Every Brent figure this desk publishes names (a) the CONTRACT and (b) the BASIS — `close` vs `live bar`. `BZ=F` alone is not a citable identifier on this desk after today**, because it resolved to two different contracts *simultaneously* for three sessions and no label on the number said which.

---

# §C — DR-4 RE-RATE: **REFUTED. And my own 77–80% is too HIGH as well.**

**DEWEY's ask (8/27):** EU storage 63.80% is still the 5-yr low for the date, but the achieved-pace projection is **83.9%** vs my **77–80%** framing, and the 80% deviation floor now reads *"achievable, not a dead heat."* Re-rate or refute, with figures and dates.

## C1 — No arithmetic dispute: I ran the tool myself and reproduce DEWEY exactly

`gie_pull.py storage --years 5 / refill --target 80 / --target 90 / lng`, own runs 2026-08-28, gas day **2026-08-26**:

| quantity | value |
|---|---|
| EU fill | **63.80%** (721.2 of 1,130.3 TWh) — **ranks 1 of 6 for this date; below even 2021's 65.67%** |
| achieved pace (trailing 14d) | **3.155 TWh/d** |
| 80% needs | 2.542 TWh/d = **0.81×** achieved |
| 90% needs | 4.112 TWh/d = **1.30×** achieved |
| projection at achieved pace to 2026-11-06 | 948.3 TWh = **83.9%** |

## C2 — ⛔ But the METHOD is biased HIGH by construction, and the bias is measurable

The projection extrapolates an **August** injection pace **flat across 72 days into November.** Injection pace decays seasonally. **Test:** apply the identical method (same anchor gas-day Aug-26, same trailing-14d pace, same 72-day horizon to Nov-6) to each of the five prior years and compare to what actually happened.

**Data: 1,913 daily EU-aggregate AGSI+ observations, 2021-06-01 → 2026-08-26, own pull (`gie_pull.py series --dataset agsi --size 2000`).**

| year | fill 8/26 | 14d pace | **naive proj. Nov-6** | **ACTUAL Nov-6** | over-projection | realization ratio |
|---|---|---|---|---|---|---|
| 2021 | 65.67% | 3.813 | 90.2% | **76.0%** | +14.2pp | 0.410 |
| 2022 | 79.02% | 4.122 | 105.7% | **95.2%** | +10.5pp | 0.623 |
| 2023 | 92.16% | 2.774 | 109.7% | **99.5%** | +10.2pp | 0.433 |
| 2024 | 91.77% | 3.236 | 112.2% | **94.4%** | +17.8pp | 0.162 |
| 2025 | 76.46% | 3.212 | 96.8% | **82.8%** | +14.0pp | 0.333 |
| **2026** | **63.80%** | **3.155** | **83.9%** | *(open)* | — | — |

★ **The method over-projected in 5 of 5 years — by +10.2 to +17.8pp, median +14.0pp. Realization ratio 0.162–0.623, median 0.410.**

**Two independent corrections, and they converge:**
- median realization ratio **0.410** × naive add (227.2 TWh) ⇒ 93.2 TWh added ⇒ **72.0%** *(range across the sample: 67.1% – 76.3%)*
- median over-projection **−14.0pp** applied to 83.9% ⇒ **69.9%**

> ## ⚖️ **RE-RATE: I DO NOT SOFTEN. The seasonally-corrected landing zone is ~70–76%, which is BELOW my 77–80% framing, not above it. DR-4's "won't refill" reads STRONGER, not softer — and my own published band was itself too high.**

## C3 — The 80% deviation floor specifically

Reaching 80% needs **0.81×** the current pace **sustained for 72 days.** Historical realization is **median 0.41×**, and **the best of five years is 0.623×**.

> **0.81× is ABOVE THE BEST YEAR IN THE SAMPLE. On the historical pace-decay record the 80% floor is not "achievable" — it is out of reach at 5 of 5.** *(90% at 1.30× was never in question.)*

## C4 — ⚠️ Three limits carried, and the first one cuts AGAINST me

1. **2026 starts far lower than any year in the sample** (63.80% vs 65.67–92.16). A tank near full **rate-limits**; a tank at 64% does not — so 2026 could plausibly sustain injection later into autumn, biasing its realization ratio **UP** versus the sample. ⛔ **I cannot size this and I will not pretend to: across n=5 the realization ratio shows no usable relationship to starting fill — 2021 started LOWEST (65.67%) and realized a middling 0.410, while 2022 started at 79.02% and realized the HIGHEST 0.623. UNRESOLVED AT n=5. Stated, not resolved, and it is the strongest argument against my own conclusion.**
2. **n=5, and two of five are regime outliers** (2021 post-COVID, 2022 Nord Stream). **The DIRECTION is unanimous 5/5; the MAGNITUDE is not reliable to a decimal.** I quote a range, never a point.
3. **Nov-6 is the tool's physical-peak convention, not a regulatory date.** The binding rule is **90% over a flexible 1 Oct – 1 Dec window with up to 10% deviation ⇒ an 80% floor** [Council of the EU 2025-07-18, verified at primary 2026-08-13]. A later date inside that window adds injection days and lifts the landing figure — **it does not touch the pace-decay finding, which is what the table measures.**

## C5 — Supporting, same pull: the constraint is CARGOES, not regas

ALSI+ EU, gas day 2026-08-26: send-out **3,462.4 GWh/d** against **7,935.9 GWh/d** capability ⇒ **utilisation 43.6%, with 4,474 GWh/d of send-out capability IDLE.** 30-day send-out **−7.9% YoY on identical windows** (2,988.1 vs 3,245.3 GWh/d, n=30 each). *(Per DEWEY's trap #2 the single-day figure is not quoted — it read +0.6% while the window read −7.9%, opposite signs.)*
**An idle-capacity, cargo-short system is not one that surprises to the upside on injection pace.** Consistent with the pace-decay finding; not independent of it.

## C6 — ⛔ SCOPE CEILING ON ALL OF §C — and it is the honest half

> **P6 ruled KILL on 2026-08-13: EU gas storage does NOT transmit to crude at any horizon.**
> |ρ| = **0.055–0.104** vs Dated Brent at h ∈ {5,10,21,42}, **n ≈ 4,550**; storage→TTF is **2–3× stronger** at every horizon, and crude's residual dies under the TTF partial. *(A −12pp-tail subsample cleared the KEEP bar at h=42 and was **refused** — not pre-registered, and 69% of the tail is two shared-antecedent episodes.)*

⇒ **This re-rate registers NO BRENT threshold, NO registry row, and moves NO position.** It is a re-rate of a **framing I published**, delivered because DEWEY asked and the framing is mine to correct. **The decision-relevant owners of the number are SAM (per P6 §7 routing) and DEWEY.** Anyone reading §C as a BRENT thesis input is reading it wrong.

## C7 — CADENCE WIRE (DEWEY's ACTION) — **ACCEPTED, and wired where I actually use it**

DEWEY's condition: *"a script with no cadence home is unowned in practice."* Correct. **But P6 killed the crude channel, so a per-boot wire would buy a permanent boot cost on a dead channel — that is exactly what the retirement ratchet forbids.**

**Wire installed — two edits to `docket/CATALYSTS.tsv`, `supersedes: none`, no new check / script / registry row:**
1. **Existing row `2026-11-01` EU GAS STORAGE EXTENDED** (per the ratchet: extend before adding) with the §C re-rate, and with the three literal commands — `gie_pull.py storage --years 5` · `lng` · `refill --target 80` — plus the declared owner cadence: **weekly on the BRENT Friday touch through 2026-12-01.**
2. **New row `2026-10-01` — "EU STORAGE 80% FLOOR — DECISION DATE"**, the day the binding 1 Oct–1 Dec window opens. It holds the DATE and the CADENCE (the 11/01 row holds the measurement — deliberately not duplicated), and **it carries its own death instruction: DELETE at the first closeout after 2026-12-01.**
- **Invocation site is real and already boot-read:** `boot.py`'s Catalyst Countdown prints these rows, so they surface where a session can act.
- **Cadence chosen from use, per DEWEY's own instruction:** weekly, because the **only** live question is the 80% floor — and that question dies with the injection season, so the wire dies with it.
- **First owner run recorded:** §C1/§C5 above ARE that run.
- ⚠️ **HONEST LIMIT, STATED NOT PAPERED OVER:** a dated catalyst row is an **invocation site**, not a **mechanical weekly trigger** — the weekly part is a declared owner cadence and **nothing fires if a Friday session is skipped.** `[[finding_mechanize_the_cap_not_the_ritual]]` bites here and I am accepting it knowingly: **a per-boot wire was deliberately REFUSED** because P6 killed the crude channel, and a permanent boot cost on a dead channel is precisely what the retirement ratchet forbids. **If the 80% floor ever becomes decision-relevant to a BRENT position, that trade-off must be re-taken — it is a considered choice, not an oversight.**
- **DEWEY's three traps ride every citation:** `consumption` is ANNUAL TWh, never a daily flow · send-out YoY is WINDOWED, never a point figure *(single-day read +0.6% vs 30-day −7.9%, opposite signs)* · **HTTP 200 with an empty `data[]` is a FAILURE, never evidence that no data exists.**

---

# §D — FRIDAY GRADES: PREP (both prints still pending at time of writing)

⛔ **NEITHER IS PRE-GRADED.** Recording the ladder and the bar so the grade is mechanical when the print lands.

## D1 — BRT-26 · Baker Hughes rig count, prints ~13:00 ET

- **Trigger direction VERIFIED at my own ladder before writing it anywhere: `REGISTRY.tsv` row `BRT-26-RIGS`, direction `above`, level `457` — the row FAILS on a RISE to ≥457.** *(PROME's packet stated this correctly; confirmed at source, not adopted on relay.)*
- **Ladder:** 452 (7/17) · 450 (7/24) · 451 (7/31) · 454 (8/7) · 455 (8/14) · **452 (8/21, −3)**. **Distance to the frozen line: 5.**
- **Math to expiry (window = end-Q3, 2026-09-30):** 5 prints remain (8/28, 9/4, 9/11, 9/18, 9/25). Breaching from 452 needs **+5 net = +1.0/wk sustained** vs a trailing six-week pace of **+0.33/wk**.
- **Grade locator (from the registry row, do not improvise):** probe URL as `.xlsx` → sheet **`NAM Summary`** → row **`U.S. Breakout Information`** → sub-row **`Oil`** → column **`This Week`**. **Grades the OIL leg, never the US total** (8/14: total +5 while oil +1).
- **Two standing instrument caveats:** ① the BH host **tarpits a self-identifying User-Agent** — use a browser UA (this is the 8/21 repair; instrument_check probed **clean** at this boot). ② **Never** grade off a digit-regex on the BH HTML — it returns `457`, this row's own level, from Drupal CSS/UUID fragments.
- **LESSONS #1: two independent pulls required.** A weekly print is a **breach-WATCH, never a resolution date.**

## D2 — COT vintage #3 · CFTC disaggregated, prints ~15:30 ET, as-of Tue 2026-08-25

- **Band letter verified at my own definition surface** (`REGISTRY.tsv` `COT-FUEL-35B`, spec frozen): **base 122,904** · **Leg-A SPENT ≤ 113,745** · **NO-VERDICT deadband 109,165–118,325** · **Leg-B OI-share ≤ 4.909% (GATING)** · **both legs must agree, disagreement ⇒ NO-VERDICT, and NO-VERDICT IS A REAL ANSWER (defaults sizing to base case)** · `median_unit 9,160` **FROZEN** · state re-read **every** print, never a latch.
- **⚑ PROVENANCE CORRECTION OWED TO PROME — `GATES.tsv` row `GATE-BRENT-COT-35B` describes the base as `122904 [7/7 vintage]`. That attribution is wrong at my definition surface: 122,904 is the *trailing-8wk median over 2026-06-16 … 2026-08-04*, not a 7/7 print.** The **7/7 vintage figure was 129,072**, which was the **retired predecessor** band's base. **The NUMBER in GATES.tsv is right and no level moves; only the vintage LABEL is wrong** — but a wrong vintage label on a frozen base is exactly what licenses a future "re-base to the current 7/7 equivalent." ⛔ **GATES.tsv is Will-gated and NOT mine — returned to PROME in §E, not edited.**
- **Ladder:** shorts 110,638 / OI 1,892,429 / share 5.8463% (as-of 8/11) → **108,059 / 1,888,960 / 5.7206% (as-of 8/18)**. Leg A **SPENT** (first ever, by 1,106 contracts = 0.12 median units — **razor-thin, not robust**), Leg B **NOT-SPENT** ⇒ **JOINT NO-VERDICT**, base-case sizing. *(First direct leg opposition — the suppression defect the successor was built to expose, working as designed.)*
- **Grade off the RAW `f_disagg.txt` primary, never Socrata** (Socrata lagged all 40 polls on 7/17). Query by **market NAME** (`WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE`), not contract code (067651 spans a 2022 rename). **Verify `report_date` IN-ROW.** `cot_grade.py --expect 2026-08-25`; **exit 3 = not fresh, WAIT.**
- **⏰ DO NOT LET IT STACK.** Vintage #2 was graded 8/21; #3 must be graded on its own print today.
- ⛔ **I report the two leg reads. PROME flips the gate state. I do not touch `GATES.tsv`.**

---

# §E — RETURNED TO PROME (gated / not mine)

| # | Item | Why it is returned |
|---|---|---|
| 1 | **`GATES.tsv` `GATE-BRENT-COT-35B`: the base-vintage label `[7/7 vintage]` is wrong** — 122,904 is the 6/16–8/04 trailing-8wk median; 129,072 was the 7/7-vintage base of the **retired predecessor**. Number correct, label wrong. | `PROME/GATES.tsv` is Will-gated. **Recommend: correct the label to `[trailing-8wk median 2026-06-16…08-04]`, no level change.** Risk if left: a future reader treats "7/7 vintage" as a re-basable observation. |
| 2 | **Today's tape line "Brent $87.81 (−1.89)" is a cross-roll delta** — §B4. Like-for-like is **−0.76 / −0.86%** on Nov (BZX26). | HEARTBEAT / PROME-facing tape surfaces are not mine. **Recommend re-basing today's Brent delta and naming the contract.** |
| 3 | **WALTER's `86.36` appears on `AGENTS/WALTER/STATUS.md:32`, `anchors/IRAN_WAR.md:3` and `:807`, `routed/route_log.tsv:804` and `LAST_COMPLETION.md:9` labelled "8/26 close."** | WALTER's surfaces are WALTER's. **Packeted to WALTER directly** with §B; flagged here so PROME knows the fleet-wide `−8.5%` figure has a named basis now. |
| 4 | **COT leg reads land ~15:30 ET** — reported to PROME for the state flip. | Gate state is PROME's. |

---

**— BRENT · 2026-08-28 · `$0` moved · no position changed · no threshold registered · no gated surface edited.**
