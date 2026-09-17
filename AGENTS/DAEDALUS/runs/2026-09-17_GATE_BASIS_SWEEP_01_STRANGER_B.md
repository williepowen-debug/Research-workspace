# GATE BASIS SWEEP 01 — STRANGER GRADER, SET B
**Grader:** stranger (no fleet knowledge; read only `READER_BRIEF_COMMON.md` §Hard rules/§Useful commands + `GATE_LETTERS_B.md`)
**Date of grading:** 2026-09-17 (Thu), first fetch 09:34:07 EDT
**Rule of the exercise:** grade from the LETTER ALONE. No GATES.tsv, no owner directory, no STATUS file, no definition_surface was opened. Where a letter points at a "definition_surface" or a register file, that pointer is treated as UNAVAILABLE — which is exactly the test.
**Data used:** FRED/ALFRED API (`FORGE/tools/market-data/.env` key, never printed), `FORGE/tools/market-data/fetch.py`, yfinance via repo `.venv`, SEC EDGAR browse-edgar (declared UA from `.env`), Parcl Labs public research pages, one web search.

---

## SUMMARY TABLE

| Gate | Verdict | One-line reason |
|---|---|---|
| GATE-TERRY-007 | **NOT FIRED** (0-of-5; high confidence) | DGS10 has no print below 4.50 anywhere since registration; latest 5.00 (2026-09-15). Direction is *away* from the gate. |
| GATE-TERRY-ROLL70-EXIT | **NOT FIRED** (0-of-3; high confidence) | WAL max close since 9/1 = $81.00 (2026-09-03); $81.90 never touched on a close. |
| GATE-BRK-R2 | **CANNOT-GRADE (letter does not define the vehicle universe; "PER-VEHICLE … ONE vehicle" has no enumerated population, and the register it points to is unavailable to me)** | I can measure any *named* vehicle from filings; I cannot know which vehicles are in scope, so "no vehicle fired" is unprovable. For the one vehicle the letter names (OCIC) there is no in-window observation. |
| GATE-CORAL-MSI-01 | **CANNOT-GRADE (letter states a level but no breadth count and no sustain duration, and the word "breadth+sustain" makes both load-bearing)** | I fetched real MSI values — 5 of 8 FL metros are >6.0 today — but "breadth" (how many? of what denominator?) and "sustain" (how many days?) are unquantified, so the same numbers support FIRED or NOT FIRED. |

Two of four gates are gradeable today by a stranger. Both gradeable ones are *negatives at a distance* — neither is near its boundary, which is the only reason my unresolved assumptions (below) did not change the verdict.

---

# GATE 1 — GATE-TERRY-007 (registered 2026-08-19; owner TERRY/BOND)

### 1. The condition in my own words
Watch the 10-year Treasury constant-maturity yield as published by FRED under series DGS10. Each publication day is one observation. If **five observations in a row** are each **below 4.50 percent**, the gate fires — and firing means TERRY writes an exit proposal for something called "004" and sends it to Will for [Approve]; it is never self-executed. A **single** observation below 4.50 does *not* fire anything but does **reset a counter belonging to a different gate ("arm-#2")**. If a 9/30 expiry arrives before five-in-a-row is achieved, the gate is MOOT and resolves NO-VERDICT rather than NOT-FIRED. The letter tells me the count stood at 0-of-5 at first grade on 8/20, and that the lowest print in the observed window was 4.63.

### 2. Questions I had to answer by ASSUMPTION

| # | Question the letter left open | My assumption | Could flip a grade? |
|---|---|---|---|
| A1 | "official FRED DGS10 closes" — is DGS10 a *close*? | DGS10 is not a close at all; it is the Treasury/H.15 **3:30pm ET constant-maturity quote**, unit = Percent. I treat "official close" as "the DGS10 daily value." | No here (gap is 50bp), yes at a boundary |
| A2 | `<4.50%` — strict or inclusive? | Strict `<`. An exact 4.50 print does NOT count and does NOT reset. | Yes at the boundary |
| A3 | Published precision — DGS10 prints 2 decimals (4.63, 5.00). A "4.50" print is therefore possible and is a tie. | Tie → not below → does not advance the count; I also assume it does not *reset*, because the reset rule is written as "<4.50", the same operator. A different grader could read a 4.50 as breaking consecutiveness. | Yes |
| A4 | What breaks "CONSECUTIVE"? Holidays and missing prints. **DGS10 has a literal gap: 2026-09-07 = "."** (Labor Day). | Non-publication days are skipped, not treated as breaks — "consecutive" = consecutive *observations*, not consecutive calendar days. | Yes |
| A5 | Vintage — first print vs revised. DGS10 is revisable in principle. | Grade on the current FRED vintage. (I did not need ALFRED because no value is near 4.50.) | Rarely |
| A6 | What resets the 5-count (as opposed to arm-#2's counter)? The letter tells me what resets *arm-#2* and is silent on what resets **this** gate's count. | I assume any observation ≥4.50 resets this gate's count to 0. This is an inference from the word CONSECUTIVE, not from the letter. | Yes |
| A7 | Ruling B says "a SINGLE close <4.50 = arm-#2 counter RESET only." Does the 1st of a 5-run *also* reset arm-#2? | Yes — every sub-4.50 print resets arm-#2, including ones that go on to become part of a 5-run. | N/A to this gate |
| A8 | "MOOT ⇒ NO-VERDICT if the 9/30 expiry beats it" — 9/30 of which year, and beats *what* (the 5th print, or the proposal, or Will's approval)? | 2026-09-30; "beats it" = the 5th qualifying print has not occurred on or before 2026-09-30. | Yes — a 5-run completing 9/29 with a proposal written 10/1 is FIRED under my reading, MOOT under another |
| A9 | Is the *grade* the fire, or is the fire the proposal? | The measurement condition is the fire; the proposal is the consequence. | No |

### 3. Observations needed — did the letter name them precisely enough to fetch without guessing?

| Element | Letter's text | Precise enough? |
|---|---|---|
| Series id | "FRED DGS10", plus an explicit DO-NOT list ("never ^TNX/^TYX") | **YES** — best-specified element in the whole set B |
| Unit / conversion | "<4.50%" vs DGS10's native Percent unit | **YES** (both percent; no bp/decimal conversion trap) |
| Vintage | not stated | **NO** — first-print vs revised unstated; also the *publication lag* is unstated (see below) |
| Operator + boundary | "<4.50%" | **YES** on operator, **NO** on tie handling |
| Precision / tie | not stated | **NO** — 4.50 is a reachable 2dp print and is unadjudicated |
| Consecutiveness | "FIVE CONSECUTIVE" | **PARTIAL** — count unit is clear; whether a non-publication day breaks the run is not, and the series contains a real gap (9/07) |
| Reset | stated for arm-#2, **not** for this gate's own 5-count | **NO** |

### 4. Grade attempt — actual numbers

`FORGE/tools/market-data/fetch.py fred DGS10` and FRED API `series_id=DGS10&observation_start=2026-08-01`, both fetched 2026-09-17 09:34 EDT:

| Date | DGS10 (%) | <4.50? |
|---|---|---|
| 2026-08-19 (registration day) | 4.65 | no |
| 2026-08-20 | 4.69 | no |
| 2026-08-21 | 4.74 | no |
| 2026-08-24 | 4.70 | no |
| 2026-08-25 | 4.64 | no |
| 2026-08-26 | 4.66 | no |
| 2026-08-27 | 4.67 | no |
| 2026-08-28 | 4.73 | no |
| 2026-08-31 | 4.75 | no |
| 2026-09-01 | 4.79 | no |
| 2026-09-02 | 4.79 | no |
| 2026-09-03 | 4.77 | no |
| 2026-09-04 | 4.78 | no |
| 2026-09-07 | **.** (no print — Labor Day) | n/a |
| 2026-09-08 | 4.80 | no |
| 2026-09-09 | 4.83 | no |
| 2026-09-10 | 4.95 | no |
| 2026-09-11 | 4.96 | no |
| 2026-09-14 | 4.97 | no |
| 2026-09-15 | **5.00** | no |

Minimum over the whole 2026-08-03 → 2026-09-15 pull (n=32 obs): **4.63** (2026-08-04, 08-05, 08-13), consistent with the letter's stated "window low 4.63".
Longest run of sub-4.50 prints since registration: **0**.
Distance to the boundary today: **+50 bp** (5.00 vs 4.50), and widening — the series rose ~35bp in the 9 sessions to 9/15.

**VERDICT: NOT FIRED. Counter 0-of-5.** (Not MOOT — 2026-09-30 has not arrived.)

**Vintage note a grader must carry:** FRED `last_updated = 2026-09-16 15:16:34-05`, `observation_end = 2026-09-15`. At 09:35 EDT on 9/17 the **2026-09-16 value is not yet on FRED**. A gate phrased on "official FRED closes" is therefore always graded on **T-2** in a morning session, not T-1. The letter does not say this and a grader who assumes "yesterday's close is available" will silently grade a stale window — harmless at 50bp, decisive inside 5bp.

### 5. MISREADS (two reasonable graders diverge)
| Misread | Grader X | Grader Y |
|---|---|---|
| The gap at 2026-09-07 | skips it; a 5-run may straddle Labor Day | treats the missing print as breaking CONSECUTIVE; resets to 0 |
| A print of exactly 4.50 | not <4.50 → no advance, no reset, run survives | not <4.50 → run **broken**, reset to 0 |
| "official closes … never ^TNX" | reads this as "use DGS10, full stop" | reads "close" literally and reaches for a 4:00pm ET official close, which **DGS10 is not** (it is a 3:30pm quote) — and may substitute a Treasury par-yield or a futures settle |
| MOOT boundary | run completing on 9/30 = FIRED | any resolution reached after 9/30 = NO-VERDICT |
| What resets this gate's counter | ≥4.50 resets (inferred) | letter only specifies an arm-#2 reset ⇒ this gate's count is **cumulative**, not consecutive-run — a genuinely different instrument |

### 6. Smallest edit that removes the largest ambiguity
> Replace "FIVE CONSECUTIVE official FRED DGS10 closes <4.50%" with "**five consecutive published DGS10 observations (current FRED vintage; non-publication days skipped, they do not break the run) each strictly < 4.50; any observation ≥ 4.50, including exactly 4.50, resets this count to 0.**"

---

# GATE 2 — GATE-TERRY-ROLL70-EXIT (registered 2026-09-03; owner REGINALD grades / TERRY proposes / Will executes)

### 1. The condition in my own words
Watch the official closing price of WAL. If the close is **at or above $81.90 on three consecutive trading sessions**, the exit condition is met (REGINALD grades it, TERRY writes the proposal, Will executes). Any close **below** $81.90 resets the count to zero. The letter states the count stood at 0-of-3 as of the 2026-09-02 close of $79.12.

### 2. Questions I had to answer by ASSUMPTION

| # | Question | My assumption | Could flip a grade? |
|---|---|---|---|
| B1 | **Which WAL?** The letter gives a bare ticker and no issuer name, no exchange, no CUSIP. "WAL" is also a ticker elsewhere. | WAL = Western Alliance Bancorporation (NYSE). Confirmed only because the repo's own fetch tool resolves WAL → "Western Alliance" — i.e. I resolved it from a tool, **not from the letter**. | Yes — a wrong issuer is a silently wrong grade |
| B2 | "OFFICIAL CLOSE" — consolidated tape official closing price, last trade, or adjusted close? | Consolidated official close, **unadjusted**. | Yes if a dividend/split falls in a candidate run |
| B3 | Split/dividend adjustment. WAL pays a quarterly dividend. A price *threshold* on an *adjusted* series drifts. | Unadjusted (`auto_adjust=False`). The letter is silent; this is my choice. | Yes |
| B4 | `≥ $81.90` — inclusive. Letter says "≥", so a close of exactly 81.90 counts. Good. But what resets? Letter says "a close <81.90 resets". | 81.90 exactly = counts, no reset. Operator pair is **complete and consistent** here — the best-specified boundary in set B. | No |
| B5 | Precision — WAL trades to $0.01, so 81.90 is exactly reachable; no rounding question. | 2dp, exact. | No |
| B6 | "THREE CONSECUTIVE SESSIONS" — sessions of which calendar? Half-days? | NYSE trading sessions; half-days count. | Rarely |
| B7 | Does today (an **open** session) count? At 09:34 EDT WAL last-traded $79.58 on 20,342 shares — an opening print, not a close. | Today is not gradeable until the close. I grade through 2026-09-16. | Yes — a grader quoting an intraday tick as a "close" can manufacture a leg |
| B8 | Is $81.90 static or does it move with anything (a strike, a cost basis, a roll)? | Static as written. The name "ROLL70" hints the level may derive from something, but the letter does not say so. | Yes if it is actually derived |
| B9 | Does the count survive a gap (holiday, halt)? | Consecutive *sessions*, gaps skipped. | Yes |

### 3. Observations needed — precise enough?

| Element | Precise enough? |
|---|---|
| Series id | **NO** — bare ticker, no issuer/exchange/venue named. Resolvable, but by assumption |
| Unit / conversion | **YES** — USD per share, no conversion |
| Vintage | **NO** — official-close vs last-trade vs adjusted-close unstated; adjustment policy unstated |
| Operator + boundary | **YES** — "≥ $81.90" plus an explicit reset "<81.90"; both directions written |
| Precision / tie | **YES by construction** — tick size 0.01 makes 81.90 exact and "≥" resolves the tie |
| Consecutiveness | **PARTIAL** — "THREE CONSECUTIVE sessions" is clear; holiday/half-day handling unstated |
| Reset | **YES** — explicitly written. The only gate in set B with an explicit reset rule |

### 3b. Structural note on this letter
The letter is self-described as "summary + pointer only" with the real definition at a ROLL70 card. Read strictly, **that makes the cell ungradeable by design** — yet it also carries a complete-looking operator, level, count and reset, so it reads as sufficient. I graded it as if sufficient. A grader who honored the pointer would return CANNOT-GRADE without the card. Both are defensible readings of the same cell; that is itself the defect.

### 4. Grade attempt — actual numbers
yfinance daily OHLC, `auto_adjust=False`, fetched 2026-09-17 ~09:36 EDT:

| Session | Close | High | ≥81.90? |
|---|---|---|---|
| 2026-09-02 | 79.12 | 80.55 | no (matches the letter's stated 0-of-3 anchor exactly ✓) |
| 2026-09-03 | **81.00** | 81.02 | no |
| 2026-09-04 | 80.95 | 81.39 | no |
| 2026-09-08 | 79.94 | 81.03 | no |
| 2026-09-09 | 79.66 | 79.86 | no |
| 2026-09-10 | 79.28 | 79.82 | no |
| 2026-09-11 | 79.29 | 80.64 | no |
| 2026-09-14 | 79.18 | 80.74 | no |
| 2026-09-15 | 79.03 | 80.49 | no |
| 2026-09-16 | 77.80 | **81.25** | no |
| 2026-09-17 (OPEN, not a close) | 79.58 @09:34 | 80.71 so far | n/a |

Max **close** since 2026-08-25: **$81.00** (2026-09-03) — 90c short. Max **intraday high**: $81.39 (9/04). Longest run of qualifying closes: **0**.
The letter's own anchor reproduces exactly ($79.12 on 9/02), which independently validates that I resolved the right instrument.

**VERDICT: NOT FIRED. Count 0-of-3.**

### 5. MISREADS
| Misread | Grader X | Grader Y |
|---|---|---|
| Intraday vs close | grades closes only → 0-of-3 | sees 81.25 (9/16 high) and 81.39 (9/04 high) and counts "touched 81.90"-style legs on highs → would have counted legs had the high reached 81.90; on a $0.50-higher tape the two graders **diverge outright** |
| Adjusted vs unadjusted | unadjusted → thresholds stay meaningful | `auto_adjust=True` → every pre-dividend close is shaded **down**, making the gate strictly harder over time, invisibly |
| Today's session | excludes an open session | quotes the 09:34 print of $79.58 as "today's close" and logs an observation that does not exist |
| The pointer clause | grades from the summary | refuses to grade without the ROLL70 card |
| Which WAL | Western Alliance (NYSE) | any other listing carrying that symbol |

### 6. Smallest edit that removes the largest ambiguity
> Replace "WAL OFFICIAL CLOSE" with "**Western Alliance Bancorporation (NYSE: WAL) consolidated official closing price, UNADJUSTED for dividends/splits; an open session is not an observation.**"

---

# GATE 3 — GATE-BRK-R2 (registered 2026-09-03; owner BROCK)

### 1. The condition in my own words
For each vehicle (some population of funds that repurchase their own shares from holders), compute per period a **satisfaction ratio = Σ accepted ÷ Σ submitted**. The gate fires if **any single vehicle** hits either: **(a)** three consecutive quarters with a ratio below 100%, or **(b)** any single quarter with a ratio below 25%. Monthly figures are never graded — quarters only. Leg (b) is prospective only: the quarter's **repurchase pricing date** must be on or after 2026-09-03; the letter explicitly excludes OCIC's 22.82% as out-of-window. The measurement must come from SEC filings ("filing-primary"). CCLFX is declared not measurable. The letter also warns that a non-fire is not evidence of health.

### 2. Questions I had to answer by ASSUMPTION

| # | Question | My assumption | Could flip a grade? |
|---|---|---|---|
| C1 | **WHICH VEHICLES?** "PER-VEHICLE … ONE vehicle shows …" — the letter names a population but never enumerates it. Two are named only as exclusions (OCIC out-of-window, CCLFX not measurable). | I cannot assume this. This is the blocking gap. A *negative* verdict requires the denominator — you cannot say "no vehicle fired" over an unnamed set. See §4. | **Decisive** |
| C2 | What is a "vehicle"? Non-traded BDC? Perpetual-life NAV REIT? Interval fund? All of the above? | From OCIC (non-traded BDC) + CCLFX (interval fund), I inferred "non-traded/perpetual vehicles with share-repurchase or tender programs." Inferred from two exclusion examples — weak. | Yes |
| C3 | "satisfaction" — of shares, or of dollars? | Shares. Not stated. A $-weighted ratio differs whenever price varies within the offer. | Yes |
| C4 | Does a vehicle that repurchases **100% of a capped offer** but prorates count as sub-100%? This is the crux: most programs cap at 5% of NAV/quarter, so "Σaccepted ÷ Σsubmitted" <100% is the **designed, normal** outcome of any oversubscribed quarter — not stress. | I assume the ratio is taken as written, cap or no cap. Under that reading leg (a) fires on three ordinary oversubscribed quarters. | **Yes — this is the biggest substantive risk in the letter** |
| C5 | `<100%` and `<25%` — strict. 100.00% exactly = not sub-100. | Strict `<` both legs. | Yes |
| C6 | Precision — filings report e.g. "22.82%" (4sf) or raw share counts. Is 99.97% "sub-100%" or rounding? | Compute from raw share counts; do not round. | Yes |
| C7 | What resets leg (a)'s 3-quarter run? | A quarter at ≥100% resets. Not stated. | Yes |
| C8 | Do the 3 quarters have to be the **same vehicle**? | Yes ("ONE vehicle shows"). This one *is* clear. | No |
| C9 | "repurchase pricing date" — the offer's expiration, the NAV valuation date, the payment date, or the filing date? These can be 3–6 weeks apart. | I assume the NAV/valuation date the repurchase price is struck at. Four candidate dates exist for every offer. | **Yes — it is the sole in/out-of-window test** |
| C10 | Leg (a) — is it also prospective, or does history count? The ⚠️ scopes prospectivity to "(b)" only. | Leg (a) may use history (so a fire could already be latent in pre-9/03 quarters). | **Yes** |
| C11 | Skipped quarters — a vehicle that runs no offer in a quarter. Break or skip for leg (a)? | Unstated. I would skip, but this is a guess. | Yes |
| C12 | What is "one observation"? One vehicle-quarter, presumably, but for leg (a) the observation is a 3-quarter window. | vehicle-quarter. | No |

### 3. Observations needed — precise enough?

| Element | Precise enough? |
|---|---|
| Series id | **NO** — no vehicle list, no CIKs, no form types. "Filing-primary" names a *source class*, not a series |
| Unit / conversion | **PARTIAL** — formula Σaccepted÷Σsubmitted is given (good), but shares-vs-dollars is not, and the cap/proration question is unaddressed |
| Vintage | **NO** — SC TO-I/A final results vs 10-Q disclosure vs 8-K give the same quarter at different dates and occasionally different numbers |
| Operator + boundary | **YES** — "<100%", "<25%" are unambiguous operators |
| Precision / tie | **NO** — a 99.9% print's treatment is unstated |
| Consecutiveness | **PARTIAL** — "≥3 CONSECUTIVE … quarters" is clear in words; skipped-quarter handling and reset are not |
| Reset | **NO** |

### 4. Grade attempt — what stopped me
I could execute the *measurement* but not the *population*.

What I did fetch (SEC EDGAR, `browse-edgar` for CIK 0001812554, Blue Owl Credit Income Corp. = OCIC, fetched 2026-09-17):

| Filing | Date | Meaning |
|---|---|---|
| SC TO-I | 2026-08-26 | Q3-2026 issuer tender offer commenced |
| SC TO-I/A | 2026-07-24 | final amendment (results) for the Q2 offer commenced 2026-05-26 |
| SC TO-I | 2026-05-26 | Q2-2026 offer |
| SC TO-I/A | 2026-04-27 | results for the Q1 offer commenced 2026-02-27 |
| SC TO-I | 2026-02-27 | Q1-2026 offer |

The pattern is stable across 2024–2026: offer commences ~Feb/May/Aug/Nov 26th, **results amendment lands ~2 months later** (Jan 27 / Apr 27 / Jul 24 / Oct 24). So for the one vehicle the letter names, the offer that is live right now (filed 8/26) will not publish a satisfaction ratio until **~2026-10-24**, and its pricing date is almost certainly 2026-09-30. **Between 2026-09-03 and 2026-09-17 there is no OCIC observation at all** — not a non-fire, an *absence*.

Why that is not a verdict: the letter's fire condition is "**ONE vehicle** shows…", quantified over a set it never names. To return NOT FIRED I would have to enumerate every vehicle in scope and check each. I can name plausible candidates from domain knowledge, but a stranger picking the universe *is* the hallucination the letter is supposed to prevent. The pointer that would resolve it (`PC_REDEMPTION_REGISTER.tsv`) is out of bounds for this exercise — and note that under the brief's own hard rule 3, a register is an artifact the letter delegates to, which means **the letter is not the instrument; the register is.**

**VERDICT: CANNOT-GRADE — the letter does not define the population the existential quantifier ranges over. Sub-result: for OCIC (the only vehicle named), NOT-SEEN in window; next observable ~2026-10-24.**

### 5. MISREADS
| Misread | Grader X | Grader Y |
|---|---|---|
| The universe | refuses to grade without the register (my reading) | picks a plausible 6–10 vehicle list from memory and returns a confident NOT FIRED over a set nobody ratified |
| Proration / caps | ratio as written → an oversubscribed-but-fully-funded 5% cap counts as sub-100% → leg (a) fires on three **normal** quarters | reads "satisfaction" as "was the program honored as designed" → a capped-and-prorated quarter is 100% satisfied → leg (a) almost never fires. **These two graders produce opposite verdicts on identical filings** |
| Leg (a)'s window | historical quarters count → a fire may already be latent pre-9/03 | applies the 9/03 prospectivity to both legs → clock starts fresh, earliest possible leg-(a) fire ≈ Q3-2027 |
| "repurchase pricing date" | NAV valuation date (≈9/30 for a Q3 offer) | filing date of the results amendment (≈10/24) — a **seven-week** difference on the only in/out test the gate has |
| OCIC 22.82% | out-of-window, discard entirely | "22.82% < 25%, and the same program is still running" → treats the next quarter as leg-(a) quarter 2 |

### 6. Smallest edit that removes the largest ambiguity
> Add: "**Universe = the N vehicles listed in PC_REDEMPTION_REGISTER.tsv as of <date> (CIKs: …); the ratio is SHARES accepted ÷ SHARES submitted taken as filed, and a quarter capped-and-prorated below 100% DOES count as sub-100%.**" (Population first — without it the gate has no denominator; the cap clause second, because it is the one that silently inverts leg (a).)

---

# GATE 4 — GATE-CORAL-MSI-01 (registered 2026-08-23, leg fired 2026-07-23; owner CORAL/Will)

### 1. The condition in my own words
Track the **Motivated Seller Index (MSI)** published by Parcl for Florida metro markets. MSI is a 0–10 composite of seller urgency — explicitly **not** months-of-supply, which is a different live metric on the same dashboard (statewide condo 7.8, SF 4.5) and would produce a false "already breached" read. The threshold is **MSI > 6.0**, and the gate wants **"breadth + sustain"** — i.e. it is not enough for one metro to poke above 6.0 for one day. The cell is summary+pointer; the canonical letter is elsewhere; the cell also declares that PROME set no number and is transcribing Will's 2026-07-23 ratification.

### 2. Questions I had to answer by ASSUMPTION

| # | Question | My assumption | Could flip a grade? |
|---|---|---|---|
| D1 | **BREADTH = how many metros?** The word carries a quantity that is not written. 1? 3? a majority? | I cannot assume. Blocking. | **Decisive** |
| D2 | **Breadth of WHAT denominator?** Which FL metros are in scope? Parcl publishes many (Miami, Tampa, Orlando, Jacksonville, Cape Coral, North Port, Lakeland, Palm Bay, Deltona, Port St. Lucie, Naples, Ocala, Pensacola, Tallahassee, Gainesville…). Top-4? All? A CORAL-chosen set? | I sampled 8 and report them all rather than pick. | **Decisive** |
| D3 | **SUSTAIN = how long?** 3 days? 2 weeks? A month? Consecutive? | I cannot assume. Blocking — and unmeasurable anyway (see D5). | **Decisive** |
| D4 | Metro vs ZIP vs state granularity — Parcl publishes all three and the letter says "FL metro". | Metro pages. This one the letter **does** specify. | No |
| D5 | **Vintage / history.** Parcl metro pages show only the current value ("Updated: 9/17/2026", "updated daily"). The history needed for "sustain" is behind the Parcl Labs API, which returned **HTTP 403 `{"detail":"Not authenticated"}`** — there is no PARCL key in `FORGE/tools/market-data/.env` (keys present: EIA, FRED, PJM, FFIEC, ESTAT, SEC_USER_AGENT, AGSI, FIRMS). | Today's snapshot only. **Sustain is not measurable by me at all.** | **Decisive** |
| D6 | `>6.0` strict, and at what precision? Parcl prints 2dp. Lakeland today is **6.03** — inside the third significant figure of the stated threshold. Is "6.0" a 2sf threshold (so 6.03 rounds to 6.0 = not above) or an exact 6.00? | Exact 6.00, strict `>`, so 6.03 counts. A grader reading "6.0" as 2sf would exclude it. | **Yes — it is live today** |
| D7 | Does a metro dropping below 6.0 reset the sustain clock, or is it cumulative days? | Unstated. | Yes |
| D8 | Does MSI get revised? Daily-updating composites usually do. | Unknown; no ALFRED-style vintage service exists. | Yes |
| D9 | Is the leg already FIRED? The header says the leg "FIRED 2026-07-23 Will-ratified" and went 31 days unregistered. So is this gate's job to re-grade, or to record an already-fired leg? | I graded it as a live condition. If it is a record of a past fire, "grading it today" is a category error. | **Yes — changes what the exercise even is** |

### 3. Observations needed — precise enough?

| Element | Precise enough? |
|---|---|
| Series id | **PARTIAL** — "Parcl FL metro MSI" names source + geography-class + metric, and the ⛔⛔ block does outstanding work ruling out the confusable metric. But no metro list and no API endpoint |
| Unit / conversion | **YES** — "0-10 composite scale" is stated outright. The single best-specified unit in set B |
| Vintage | **NO** — no as-of convention, no revision policy, no statement that only today's value is publicly retrievable |
| Operator + boundary | **YES** on operator (">6.0") |
| Precision / tie | **NO** — "6.0" vs "6.00" is live at 6.03 today |
| Consecutiveness | **NO** — "sustain" is named but never quantified |
| Reset | **NO** |
| Breadth | **NO** — named but never quantified, and its denominator is never listed |

### 4. Grade attempt — actual numbers
Parcl Labs public metro research pages, all showing "Updated: 9/17/2026", fetched 2026-09-17:

| FL metro | MSI (9/17/2026) | Parcl label | >6.0? |
|---|---|---|---|
| Tampa | **7.14** | Motivated | YES |
| Jacksonville | **6.32** | Motivated | YES |
| North Port | **6.27** | Motivated | YES |
| Orlando | **6.19** | Motivated | YES |
| Lakeland | **6.03** | Motivated | YES (but see D6) |
| Palm Bay | 5.87 | Motivated | no |
| Cape Coral | 5.85 | Motivated | no |
| Miami | 4.75 | **Stubborn** | no |

**5 of 8 sampled FL metros are above 6.0 today; the spread across the state is 4.75 → 7.14 (2.39 points), so a same-day statewide read is genuinely dispersed, not uniform.** Reference: Parcl's own scale calls 5–7.5 "motivated" and >7.5 "fire sale"; the national MSI has been quoted around 5.44–5.60 in Parcl's public research. So >6.0 is above the national level but comfortably inside Parcl's own "normal motivated" band — a threshold set one notch above average, not at a distress boundary.

Why this is not a verdict: with breadth unquantified, **5-of-8** supports FIRED under "3 or more metros" and NOT FIRED under "a majority of all FL metros" or "the four largest metros" (Miami at 4.75 fails that one). With sustain unquantified *and* unfetchable (Parcl API 403, no key), no reading of "sustain" can be evaluated at all — not even generously.

**VERDICT: CANNOT-GRADE — "breadth+sustain" is the operative condition and neither term carries a number; sustain is additionally unmeasurable without a Parcl Labs API key.**

I want to be explicit about what this gate does *right*, because it is unusual: the ⛔⛔ mislabel block is the single most valuable paragraph in set B. Without it I would have graded months-of-supply, found statewide condo 7.8 > 6.0, and returned a confident **FIRED** on the wrong instrument — a verdict that passes every magnitude sanity check. The letter anticipated my exact failure and prevented it. It then failed to give me a number for the two words the condition actually turns on.

### 5. MISREADS
| Misread | Grader X | Grader Y |
|---|---|---|
| Breadth | "several metros" ⇒ 5-of-8 is breadth ⇒ leans FIRED | "the FL metros" ⇒ needs most/all ⇒ Miami 4.75 and Cape Coral 5.85 fail ⇒ leans NOT FIRED |
| Denominator | the big-4 (Miami/Tampa/Orlando/Jax) ⇒ 3-of-4 | every Parcl FL metro (15+) ⇒ a sample of 8 cannot even be a denominator |
| Sustain | treats "sustain" as satisfied by Parcl's own smoothing (MSI is already a trailing composite) ⇒ ignores it | requires N consecutive days of history ⇒ CANNOT-GRADE (my reading) |
| `>6.0` at Lakeland 6.03 | exact 6.00 ⇒ counts ⇒ 5 metros | 2sf "6.0" ⇒ 6.03 is not distinguishable ⇒ 4 metros. **One metro of breadth swings on typography alone** |
| Already-fired status | re-grades today as a live condition | reads the 7/23 fire as settled and returns "already FIRED, registered late" |
| The metric (absent the ⛔⛔ block) | MSI 0–10 seller-urgency index | months-of-supply → statewide condo 7.8 → **false FIRED**, magnitude-plausible |

### 6. Smallest edit that removes the largest ambiguity
> Replace "breadth+sustain on Parcl FL metro MSI >6.0" with "**≥N of the following M named FL metros (list them) each post MSI > 6.00 on the same day, on D consecutive daily Parcl updates; any day that drops below resets D.**" — i.e. put the three missing integers (N, M, D) in the letter.

---

# CROSS-GATE FINDINGS

### Where the four letters actually stand, element by element
YES = a stranger can fetch it without guessing. NO = required an assumption.

| Element | TERRY-007 | ROLL70-EXIT | BRK-R2 | CORAL-MSI-01 |
|---|---|---|---|---|
| Series id | **YES** (+DO-NOT list) | NO (bare ticker) | NO (no universe) | PARTIAL (+DO-NOT block) |
| Unit / conversion | YES | YES | PARTIAL | **YES** (scale stated) |
| Vintage | NO | NO | NO | NO |
| Operator + boundary | YES | **YES** (both directions) | YES | YES |
| Precision / tie | NO | YES (by tick size) | NO | NO (live today at 6.03) |
| Consecutiveness | PARTIAL | PARTIAL | PARTIAL | **NO** (unquantified) |
| Reset | NO | **YES** (explicit) | NO | NO |
| Gradeable today? | yes | yes | **no** | **no** |

1. **Vintage is 0-for-4.** Not one letter says which vintage to grade on, and the vintage problem is real in three of them: FRED DGS10's 9/16 value did not exist at 09:35 on 9/17 (so morning grading is T-2); WAL adjusted-vs-unadjusted silently walks a fixed dollar threshold; tender results appear in 2–3 different filings at different dates. **Vintage is the element every author assumed away and no author wrote down.**

2. **Reset is 1-for-4, and ROLL70-EXIT is the model.** "a close <81.90 resets the count" is eleven words and it eliminates an entire misread class. TERRY-007 is the instructive failure: it specifies a reset **for a different gate's counter** (arm-#2) and none for its own, which actively invites the reading that its own count is cumulative rather than consecutive.

3. **The two ungradeable gates both fail on an unquantified quantifier, not on data access.** BRK-R2's "ONE vehicle" has no population; CORAL-MSI-01's "breadth+sustain" has no integers. In both cases I reached real primary data (EDGAR filings; live Parcl metro values) and still could not produce a verdict. **Data availability was never the binding constraint — the missing word was.** Conversely the two gates that *are* gradeable were gradeable not because their letters were complete but because both are 50bp/90c away from their boundary; every unresolved assumption I listed was rendered harmless by distance. Neither letter would survive its own boundary.

4. **"SUMMARY + POINTER ONLY" is a self-nullifying cell, and it appears twice** (ROLL70-EXIT, CORAL-MSI-01). Both cells then carry enough apparent detail to grade from. A cell that says "don't grade me" while looking gradeable will be graded, and the grader will not know which of the two he did.

5. **The DO-NOT clause is the highest-yield sentence type in set B, on evidence.** TERRY-007's "never ^TNX/^TYX" and CORAL-MSI-01's ⛔⛔ months-of-supply block each pre-empted a specific wrong instrument. The CORAL one demonstrably saved me from a false FIRED. Neither gate with a DO-NOT clause has a series-identity misread in its table above; both gates without one do. **Naming the wrong instrument is worth more per byte than describing the right one** — and note that CORAL-MSI-01 spends far more of its letter on the DO-NOT than on the condition, and is still the less gradeable of the two.

6. **Every fire condition in set B is a run-length, and no letter defines what breaks a run.** 5-consecutive, 3-consecutive, 3-consecutive-quarters, "sustain". DGS10 contains an actual gap (2026-09-07 = "."), quarterly programs can skip a quarter, and Parcl days are calendar-daily. Four gates, four run-length conditions, zero gap policies.

### Fleet-level smallest edit
> **Add a fixed 7-field basis line to every gate letter** — `series · unit · vintage · operator+boundary · precision/tie · run-unit + what-breaks-a-run · reset` — and require every quantifier word ("breadth", "sustain", "one vehicle") to carry an integer at the point of use. On today's evidence that turns 2 gradeable gates into 4, and it is strictly cheaper than the narrative these letters already carry: **BRK-R2 and CORAL-MSI-01 are the two LONGEST letters in the set and the two that cannot be graded.** Length is not specification.

---

## PROVENANCE
| Claim | Source | Fetched |
|---|---|---|
| DGS10 2026-08-03→09-15, n=32, min 4.63, last 5.00 | FRED API `series_id=DGS10` (key from `FORGE/tools/market-data/.env`, not printed) | 2026-09-17 09:34 EDT |
| DGS10 `last_updated 2026-09-16 15:16:34-05`, `observation_end 2026-09-15`, units=Percent | FRED API `/fred/series?series_id=DGS10` | 2026-09-17 09:35 EDT |
| WAL daily OHLC 2026-08-25→09-17 | yfinance via repo `.venv`, `auto_adjust=False` | 2026-09-17 ~09:36 EDT |
| WAL $79.58 +2.29% intraday | `python3 FORGE/tools/market-data/fetch.py price WAL` | 2026-09-17 09:35 EDT |
| OCIC = Blue Owl Credit Income Corp., CIK 0001812554; SC TO-I 2026-08-26; SC TO-I/A 2026-07-24, 2026-04-27; 2024–2026 quarterly cadence | SEC EDGAR `browse-edgar` atom, declared UA from `.env` | 2026-09-17 |
| Parcl MSI: Tampa 7.14 · Jacksonville 6.32 · North Port 6.27 · Orlando 6.19 · Lakeland 6.03 · Palm Bay 5.87 · Cape Coral 5.85 · Miami 4.75, all "Updated: 9/17/2026" | parcllabs.com/research/markets/fl/<metro>/metro | 2026-09-17 |
| MSI methodology (0–10; DOM + price-cut frequency/speed/size; 5–7.5 "motivated", >7.5 "fire sale"); national ~5.44–5.60 | Parcl Labs research pages via web search | 2026-09-17 |
| Parcl Labs API returns 403 `{"detail":"Not authenticated"}`; no PARCL key in `.env` | `curl api.parcllabs.com/v1/search/markets`; `cut -d= -f1 FORGE/tools/market-data/.env` | 2026-09-17 |

**Compliance:** read-only throughout. This file is the only file created. No git mutation. No GATES.tsv, no `AGENTS/<owner>/` directory, no STATUS file was opened. No key printed.
