# Dealer-Positioning Nexus Watch — registered 2026-07-11 (Sat ~18:00 ET)
**Owner:** LIQUID (credit-plumbing side; HENRY covers rates→equity — reconcile on contact, one figure per shared metric) · **Status:** ARMED-WATCH · **LAST REVIEW 2026-08-28 (the registry `review_by` date) — CONJUNCTION NOT MET, 0-of-3, no leg within a week of firing; W1 graded PRE-PRINT vs as-of 8/18. Next `review_by` proposed 2026-09-30 (PROME encodes). ⚠️ The 8/23 suggested W1 cumulative amendment is WITHDRAWN — base-rated dead-loud at 52.0% of rolling 8-week windows (n=237, 2022-02-08→2026-08-18) AND silent on its own motivating episode. See §GATE-LIQ-076 REVIEW below.** (a monitoring conjunction, **NOT a prediction of the CPI print** — the print branch lives in `CPI_20260714_CREDIT_PREREG.md`) · **Born from:** threads-sweep TOP-1 (7/11), Will-approved.

## The mechanism (why these three belong in one file)

A hot CPI 7/14 landing on a completed arm-#2 (10Y 5-of-5 ≥4.50 if Mon holds) hits three pre-loaded surfaces at once: front-end repricing forces P&L on the record leveraged SOFR short → cover flow amplifies rates vol (the MOVE leg) → duration-sensitive credit paper reprices into a dealer book that is **structurally short exactly the long-end IG bucket** → gap-pricing, not orderly repricing. My HY>280 X1 line could then be *reached by amplification rather than credit substance* — KB-LIQ-062's beta-vs-substance discriminator and KB-LIQ-074's acute funding rows are the check when this fires. This is the load-bearing scenario the mandate-extension SIG named: the HY>280 trigger assumes dealers can reprice; this watch monitors whether they can.

## The three legs (all fresh-pulled Sat 7/11 from free primaries — vintages stamped)

| Leg | Latest | Trend / context | Source |
|-----|--------|-----------------|--------|
| **1. Positioning** — SOFR-3M futures, leveraged-fund net | **−2,872,406 contracts [as-of Tue 7/7, released Fri 7/10]** ≈ **−$700B notional-equiv** (convention band $690-720B: $2,500 × IMM price ≈ $241K/contract → $692B; the cruder $250K shorthand → $718B — *corrected 7/11 PM from the single-convention round-4 figure*) | Record zone INTACT and RECENT: build −306K [12/23/25] → ~−0.9M Jan-Apr plateau → May-Jun acceleration → **−2,943,898 [6/30] = the record ≈ −$710B** → −2,872,406 [7/7] (+71,492 w/w = FIRST meaningful cover since mid-June, marginal). **Structure (7/11 deep-dive):** asset managers net-short the SAME side (−501,067 [7/7], persistently since 5/5) and **dealers are the mirror long +3,317,752** — a lev+AM −3.37M short warehoused ~1:1 by dealer books; 185 distinct lev short traders (window high = broad), top-4 net short 12.1% of OI. Companions same-direction: SOFR-1M −283,695; 10Y ERIS SOFR swap −135,113 ≈ −$13.5B [all 7/7] | CFTC TFF via publicreporting.cftc.gov API (futures-only, `gpe5-46if`); full decomposition → `research/2026-07-11_sofr-deep-dive.md` |
| **2. Dealer warehouse** — corp-bond net positions | IG >10y (G10): **−$9,402mm [as-of Wed 7/1]**. IG 5-10y (G5L10): **−$213mm [7/1]** | ⚠️ **CORRECTION to my 6/17-based framing:** the G5L10 −$825mm [6/17] flip did NOT persist — +$365mm [6/24], −$213mm [7/1] = **oscillation around zero**, not a sustained no-bid flip. The real structural datum is the LONG end: G10 2026 mean **−$10.0B** vs 2025 mean −$3.96B, 2024 −$0.59B, 2023 −$0.15B — a multi-year ~6x deepening; 2026 range −$6.7B to −$11.7B. HY buckets small/mixed: BELG5L10 −$1,734mm [7/1, widest of the 8-wk window], BELG10 +$366mm | NY Fed PD stats API (`markets.newyorkfed.org/api/pd/`), weekly, ~8d lag; next as-of-7/8 release ~Thu 7/16 |
| **3. Rates-vol** — MOVE vs VIX | MOVE **72.41 [7/9]**, 3 sessions up unreversed; VIX 15.51 [7/9] calm | Rates-led vol signature (VIOLET find, PROME canon 7/9; ^MOVE now in FORGE SERIES per 7/11 commit `34999644` — pull live from Mon) | VIOLET-owned read; FORGE fetch.py ^MOVE |

## Fire conditions (watch → write-up, NOT a position trigger)

| ID | Condition | Meaning |
|----|-----------|---------|
| W1 *(re-worded 7/11 PM)* | SOFR-3M lev net beyond **−2,950,000** contracts (new record past the **−2,943,898 [6/30]** peak) **OR** a one-week **cover >300,000** contracts (~4x the largest cover in the 30-wk history; largest weekly build was −379K [6/2]) | Pin deepening / unwind starting (either direction is information) — **but read any cover through the basis-vs-directional discriminator below before calling it systemic** |
| W2 | G10 net-short **< −$12.0B** (beyond the 2026 extreme −$11.66B) **OR** G5L10 **< −$800mm two consecutive weeks** (the persistence the 6/17 print lacked) | Warehouse bid withdrawing at the duration end / mid-curve flip turning real |
| W3 | **MOVE >85 while VIX <20** | Rates-led vol regime confirmed (VIOLET's figure governs) |
| **CONJUNCTION** | **Any 2 of W1/W2/W3 inside a rolling 2-week window** | Same-session write-up → PROME + NEXUS (+HENRY seam); re-run KB-LIQ-074 acute rows (SOFR 99pct tail, SRF) and read any concurrent HY move through KB-LIQ-062 (amplification ≠ substance) |

## Basis-vs-directional caveat (added 7/11 PM deep-dive — load-bearing for interpretation)

The directional/RV split of the short is **not knowable from free data** (CFTC doesn't tag strategy; per-expiry positioning unpublished — front-vs-deferred strip placement is a labeled unknowable). Observable structure leans **substantially directional** (build tracks the hike-repricing exactly; asset managers same-side short since 5/5; 185 traders = broad; press/analyst framing = higher-for-longer), with a **real but unsizable RV component** (dealer mirror-long = warehoused hedging flow; record SOFR-FF spread volumes). Consequences: (a) the squeeze mechanic runs on the *directional share only* — a soft CPI puts the short offside and the cover bid lands in the FRONT-END/STIR complex; transmission to the 10Y is indirect (steepener impulse), so "forced cover caps the 10Y" over-claims; (b) **at any W1 cover, check swap spreads / SOFR-FF spread concurrently: spreads stable while shorts cover = directional squeeze confirmed; spreads moving with the cover = RV unwind, less systemic.** Full evidence table → `research/2026-07-11_sofr-deep-dive.md` §3.

## ★★ GATE-LIQ-076 REVIEW — Fri 2026-08-28 (the `review_by` DATE itself; owner pass, W1 PRE-PRINT)

**Why this section exists:** `GATE-LIQ-076.review_by = 2026-08-28`, owner-set 8/20 in the Will-ruled envelope pass, migrated to the real `review_by` column by PROME 8/22. **This is that review.** ⛔ **I do not edit `PROME/GATES.tsv`** — every registry consequence below is **RETURNED to PROME**, never applied here.

**VERDICT: CONJUNCTION NOT MET — 0-of-3 at the latest data on every leg. No joint PROME/NEXUS amplification write-up owed. The gate is NOT ARMED and no leg is within a week of firing.**

⏳ **W1 is PRE-PRINT.** The CFTC TFF file carrying **as-of Tue 8/25** publishes **today ~15:30 ET**; everything below reads **as-of 8/18** and gets re-graded after the print. Per KB-LIQ-096 an as-of date is never labelled with its release date.

### 1. The three legs at latest data

| Leg | Grade | Latest data [as-of] | vs the registered terms | Direction |
|-----|-------|--------------------|------------------------|-----------|
| **W1 — SOFR-3M leveraged-fund net** | **NOT FIRED** · ⏳ **PRE-PRINT** | **−2,530,893 [as-of Tue 2026-08-18]** (LF long 1,052,967 − short 3,583,860); w/w **+28,923**. At the spec's own $240–250K/contract band ≈ **−$607B to −$633B** notional-equiv, vs the **−$707–736B** peak | (a) at/past the **−2,950,000** record? **NO — 419,107 contracts AWAY** and on the wrong side; the −2,943,898 [6/30] peak is 7 weeks old. (b) one-week cover **>300,000**? **NO — +28,923**, 9.6% of the line | **AWAY.** LF *spreading* 2,962,207 and OI 13,431,079 [8/18] both stable, so this is a net-risk change, not a book-size change |
| **W2 — dealer warehouse (NY Fed PD)** | **NOT FIRED — and moving decisively AWAY** | **G10 IG >10y −$7,869mm [as-of Wed 2026-08-19]** (−9,157 [8/05] · −6,929 [8/12] · **−7,869 [8/19]**). **G5L10 +$2,302mm [8/19]** — the **4th consecutive positive print and the largest of the series window** (+793 · +508 · +1,921 · **+2,302**) | G10 **< −$12.0B**? **NO** — $4.1B of room, and the 2026 extreme −$11,663 [6/10] keeps receding. G5L10 **< −$800mm ×2 consecutive**? **NO — it has not printed below −$800mm once since 6/17, and the last four prints are net LONG** | **AWAY. Dealers are ADDING inventory, not shedding it.** The one thing a funding-seizure read needs — a withdrawing warehouse bid — is absent in the series built to measure it |
| **W3 — rates-vol (MOVE vs VIX)** | **NOT FIRED — and the closest approach has receded** | **MOVE 69.86 [2026-08-27 close, yfinance `^MOVE`]** · **VIX 14.36 [2026-08-28 ~11:0x ET intraday]** | MOVE **>85 while VIX <20**? **NO — MOVE is 15.1 points under the line.** The VIX condition is satisfied and always has been; MOVE is the whole binding leg | **AWAY.** 83.02 [7/31] was the window max and nearest-ever approach; 73.40 [8/21] → **69.86 [8/27]**, now **13.2 points below** that high |

**Cross-read (unchanged from 8/23 and now on one more PD print):** W2's direction independently corroborates BOND's benign dealer read. A genuine funding-stress unwind pushes dealer warehouse short *wider*; G10 has gone −$9.6B → −$7.9B while the 5–10y bucket went **net long +$2.3B**. Two instruments sharing no input, same answer.

### 2. ★★ THE REVIEW'S FINDING — **the fix I proposed on 8/23 is a DEAD BAND, and it fails in BOTH directions at once**

On 8/23 I routed a suggested amendment to W1: *"OR cumulative net change ≥300,000 over any rolling 8-week window,"* and asserted *"on the current tape that leg would have fired ~8/04 and would be firing now."* **PROME's objection was that an 8-week window fitted to one 7-week observation has zero out-of-sample. I base-rated it before answering. PROME is right, and the measurement is worse than the objection.**

**Basis:** CFTC TFF futures-only, **raw history archives** `fut_fin_txt_YYYY.zip` 2022–2026 merged with the current `FinFutWk.txt` (never Socrata). Net = LF long − LF short, spreading excluded by construction. **n = 237 weekly as-of dates, 2022-02-08 → 2026-08-18** — the full life of the SOFR-3M TFF series; 2018–2021 return zero rows, so this is the entire population, not a sample.

#### (a) It is dead-LOUD on history — the MEDIAN 8-week window clears it

| Rolling window | windows | `|Δ| ≥ 300,000` | **base rate** |
|---|---:|---:|---:|
| 4 weeks | 233 | 107 | **45.9%** |
| 6 weeks | 231 | 121 | **52.4%** |
| **8 weeks** *(my proposal)* | **229** | **119** | **🔴 52.0%** |
| 10 weeks | 227 | 126 | **55.5%** |
| 12 weeks | 225 | 137 | **60.9%** |

**The median 8-week absolute change is 311,665 contracts — above the line I proposed.** One-sided (cover-only, the direction I actually cared about) it is **50/229 = 21.8% of all windows, 13 distinct episodes in 4.6 years ≈ 2.8/year.** For a gate whose deliverable is a joint PROME/NEXUS write-up, 2.8 write-ups a year on a leg that is supposed to mark a record position leaving is not a trigger; it is a subscription.

**Contrast — the leg AS WRITTEN is a real tail:** single-week `|Δ| ≥ 300,000` fires **13/236 = 5.51%** (p95 = 312,882). **The existing W1 weekly leg is correctly calibrated. The cumulative leg I proposed to sit beside it is not.**

#### (b) It is ALSO silent on the exact episode it was designed to catch

| as-of | LF net | w/w | **rolling 8-wk cum** | fires ≥300K? |
|---|---:|---:|---:|---|
| 2026-07-28 | −2,445,938 | +248,236 | −342,549 | no |
| **2026-08-04** | −2,532,086 | −86,148 | **−82,222** | **NO** *(a net BUILD)* |
| 2026-08-11 | −2,559,816 | −27,730 | −159,916 | no |
| **2026-08-18** | −2,530,893 | +28,923 | **+255,355** | **NO — 44,645 short of the line** |

**My 8/23 claim that "that leg would have fired ~8/04 and would be firing now" is FALSE on both halves.** The last 8-week cumulative ≥300,000 was **2026-04-28 (+305,968)**, four months ago.

#### (c) Both failures have ONE root cause, and it is a class I was caught on five days ago

The **+413,005** is measured **6/30 → 8/18 — peak-to-latest, 7 weeks, anchored on the series' record extreme.** A *rolling* 8-week window does not compute that; on 8/18 it computes **+255,355**. **A peak-anchored magnitude cannot be converted into a fixed-window threshold, and I converted one.**

> ⚠️ **`[[finding_window_start_at_an_extremum_inverts_the_move]]` — n=2 for this desk in five days.** BOND caught the first on 2026-08-27: WRESBAL *"−$207B in five weeks"* measured from the 7/15 **series maximum**. I wrote the second on **8/23**, four days *before* being caught on the first, and it survived my own 8/27 correction pass because I fixed the instance and never swept for siblings. **`[[finding_a_correction_pass_is_unreviewed_work]]` cuts the other way too: the surfaces a correction did NOT touch are where the same defect is still sitting.**

> 🔴 **And this is the 4th DEAD-BAND instance in six days (KB-LIQ-104 ES-LIQ-04 · the TIC_FRAMEWORK kill · KB-LIQ-106 SOFR75−IORB · this), the 3rd in the DANGEROUS manufactures-a-signal direction — and the FIRST one I authored myself, in a packet whose whole subject was another instrument's calibration failure.** A desk that has killed three dead bands in a week proposed a fourth in the middle of doing it. **The competence is in the detector, not in the author.**

#### (d) If a cumulative leg is still wanted, here is what it costs

To match the weekly leg's own 5.5% tail rate, the 8-week **cover-only** threshold must be **≥600,000** (13/229 = **5.7%**); ≥700,000 gives 3.1%, ≥800,000 gives 2.2%.

⛔ **The scale-invariant %-of-position form is WORSE and I am naming it as rejected now so it cannot arrive later from whoever it favours.** The net position swings *through zero* on this series (+1,188,431 [2023-12-26] to −2,943,898 [2026-06-30]), so a ratio to the prior level has a near-zero denominator: median |Δ8w| = **56.2% of the prior position**, p95 = **385.6%**. It is uninterpretable, not conservative.

⚠️ **Honest limit on my own replacement number:** ≥600,000 is a **percentile of a 4.6-year sample containing no funding seizure** — the identical defect I flagged on KB-LIQ-106's proposed bands and on GATE-079's R4. It is a *better-calibrated* band, not a validated one. **Stated rather than buried.**

### 3. ⇒ RETURNED TO PROME (registry consequences — PROME's to apply on Will's word, not mine)

1. **WITHDRAW the 8/23 suggested W1 amendment.** *"OR cumulative net change ≥300,000 over any rolling 8-week window"* is **base-rated at 52.0% of windows and does not fire on its own motivating episode.** Do not encode it. **PROME's objection is upheld and should be recorded as upheld** — the base rate it asked for is what killed the proposal.
2. **The 8/23 FINDING survives the death of its fix.** W1 keys on a weekly delta; a record position can leave on a multi-week drift; a weekly-delta trigger is structurally blind to that. **That is still true** (the pin is −14.0% off its peak and no weekly print ever tripped 300K). **What is now also true is that no calibrated 8-week leg would have caught this particular exit either** — +255,355 at its widest rolling reading. **Either the blindness is accepted as the price of a rare trigger, or the successor is a differently-shaped instrument, not a longer window.** My recommendation, offered as a recommendation: **accept it, document the blind spot on the row, and change nothing** — PROME's option (a). That is a reversal of my 8/23 preference and it is caused by the number PROME asked for.
3. **`review_by` re-date:** GATE-LIQ-076 discharges today. **Proposed next `review_by` = 2026-09-30**, aligned to the quarter-end funding turn already on my catalyst docket (the Q3 turn is the next event that could plausibly move any of the three legs) — owner-set, PROME to encode.
4. **GATE-HY-REKILL `review_by` — PROME's 8/22 ASK, answered: CONFIRM 2026-09-30.** The provisional PROME-set date is right and for the right reason: the level is intake-lane auto-watched, so the clock reviews the **letter**, not the print. Matches my own 072 quarter-cadence rationale. **No re-date requested.**

### 3-ter. ✅ W1 GRADED on the as-of Tue 2026-08-25 print — **NOT FIRED (branch (c))**. And the print arrived with an INSTRUMENT FAULT that would have produced a FALSE FIRE.

**Graded 2026-08-28 ~15:4x ET against the branches pre-registered at 11:4x (commit `22d01ad17`), unchanged.**

| leg | condition | as-of **Tue 2026-08-25** | grade |
|---|---|---|---|
| **(a)** record | net ≤ **−2,950,000** | **−2,596,865** | **NOT FIRED** — 353,135 away |
| **(b)** cover | one-week cover > **+300,000** | **−65,972 — a BUILD, wrong direction entirely** | **NOT FIRED** |
| **(c)** | neither | ✅ | **NOT FIRED — the base case** |

**Full row [as-of Tue 8/25, CME]:** LF long **966,344** · LF short **3,563,209** · **net −2,596,865** · w/w **−65,972** · **spreading 2,894,444** (−67,763) · **OI 13,036,905** (−394,174). **Spreading and OI both fell modestly alongside net — a small, orderly re-build, no book-size event.** **Discriminator not applied: it is only owed on a (b) fire, and (b) did not fire — the week was a build, not a cover.**

**GATE-LIQ-076 CONJUNCTION: 0-of-3, exactly as pre-registered.** W2 and W3 could not change before this print and did not. **No joint PROME/NEXUS write-up owed.** ★ **The 11:4x pre-registration called this correctly and in advance: "NO OUTCOME OF THIS PRINT CAN FIRE THE GATE."**

**Read against the 7-week bleed: the pin has stopped leaving.** Peak −2,943,898 [6/30] → −2,530,893 [8/18] was +413,005 covered; **8/25 gives back −65,972 of it.** Net from peak now **+347,033 (−11.8%)**, and the last two prints are **+28,923 then −65,972** — the drift has flattened and turned. ⚠️ **Two prints is not a trend and I am not calling one.**

### 🔴 THE PRINT ARRIVED BROKEN, AND MY PRE-REGISTRATION WOULD NOT HAVE SAVED ME → **KB-LIQ-116**

**First read of the new file returned: net −7,967, w/w +2,522,926.** Under the pre-registered branch **(b)**, that is a **cover of 8.4× the 300,000 line — a FIRE**, on a gate whose fire routes a joint write-up to PROME and NEXUS.

**Cause: `SOFR-3M - FMX FUTURES EXCHANGE` is NEW in the as-of 8/25 file.** `cftc_tff_rates.py` keyed rows on the market name **with the exchange stripped**, so both venues collapsed to `("SOFR-3M", date)` and **the 167,749-OI FMX row silently overwrote CME's 13,036,905-OI row. Last row wins.**

> ⚠️ **THE PRE-REGISTRATION DID NOT PROTECT ME HERE, AND I WANT THAT ON THE RECORD.** The branches were correct, filed four hours early, and would have emitted a false fire on the first bad input. **Pre-registration defends against POST-HOC RATIONALISATION; it does nothing against a CORRUPTED INPUT.** What actually stopped it was refusing to grade an implausible magnitude — **a discretionary act, which is exactly what pre-registration is designed to remove.** ⇒ **A pre-registered rule needs a pre-registered INPUT CHECK or it is a loaded weapon pointed at whatever the fetcher hands it.**

**This is `INSTRUMENT-FAULT` / detector `F1` (series-identity), designed with HENRY this afternoon and arriving live within the hour.** Same family as **KB-LIQ-113** (wrong basis, right on the median day) and **KB-LIQ-109** (dead-quiet band): **an instrument that looks right and is answering about something else.**

**FIXED IN THE TOOL, not just noted:** the loader now indexes the **full market name**, prints a **loud `INSTRUMENT-FAULT` block** naming every colliding venue with its OI, refuses to let the number pass unremarked, and **the remedy it prints is executable** (`--contracts "SOFR-3M - CHICAGO MERCANTILE EXCHANGE"` now resolves — it did not on the first cut, which would have made the guard its own dead band). **Verified: the guard fires on today's file, and the CME-only series is continuous and clean back to 7/07.**

### 3-bis. ⏳ PRE-REGISTERED W1 GRADE for the as-of Tue 2026-08-25 print (filed 11:4x ET, ~4h BEFORE the ~15:30 publication)

**Filed before the number is known, so the 15:33 grade is mechanical and cannot be shaped by what prints** — the KILL_MEMO principle applied to my own gate. **Last known: net −2,530,893 [as-of 8/18], w/w +28,923, LF spreading 2,962,207, OI 13,431,079.**

| Branch | Condition on the as-of 8/25 print | Grade |
|---|---|---|
| **(a) record leg** | LF net **≤ −2,950,000** | **FIRED.** Requires a one-week BUILD ≥ **419,107** — larger than any weekly build in the series (max **−619,056**, so reachable but ~p99) |
| **(b) cover leg** | one-week **cover > +300,000** | **FIRED.** Largest cover in the series is **+248,236 [7/28]**, 83% of the line — never yet reached |
| **(c) neither** | −2,950,000 < net, and w/w cover ≤ +300,000 | **NOT FIRED** — the base case |

🔴 **PRE-REGISTERED AND DECISIVE: NO OUTCOME OF THIS PRINT CAN FIRE THE GATE.** GATE-LIQ-076 requires **2-of-3 inside a rolling 2-week window.** **W2 is NOT FIRED and moving away** (G10 −$7,869mm, G5L10 **+$2,302mm** [as-of 8/19], 4th consecutive net-LONG) and **W3 is NOT FIRED and receding** (MOVE 69.86 [8/27], 15.1 under the >85 line). **Both are weekly/daily instruments that cannot change before this print lands.** ⇒ **Even a W1 fire leaves the conjunction at 1-of-3, and NO joint PROME/NEXUS write-up is owed today.** *(Stated now so a dramatic W1 number cannot be read at 15:33 as more than it is.)*

**Riders, all pre-committed:**
1. **Read LF SPREADING and OI alongside net.** Spreading is excluded from net by construction, so a spread-heavy book can move net without changing gross risk.
2. **If (b) fires, apply the §Basis-vs-directional discriminator BEFORE calling anything systemic:** swap spreads / SOFR-FF stable while shorts cover ⇒ **directional squeeze**; spreads moving with the cover ⇒ **RV unwind, less systemic.**
3. **KB-LIQ-096 basis:** the as-of date is **Tuesday 8/25**; the file publishes Friday. **Never label the number with the Friday.**
4. ⛔ **The withdrawn cumulative leg (KB-LIQ-107) is NOT part of this grade** and must not be reintroduced at the print — it is base-rated dead at 52.0% of rolling 8-week windows. **Named here so it cannot arrive at 15:33 as a fresh idea.**

### 4. Cadence + next prints

- **CFTC TFF:** today **Fri 8/28 ~15:30 ET**, carrying **as-of Tue 8/25** — the W1 re-grade. This is also the 8/26 5Y auction's positioning read publishing **two days after** the auction (KB-LIQ-096); `KB-BND-092` already closed on the BTC 2.37 print, so nothing is pending on it.
- **NY Fed PD:** weekly Thu; next ~**9/3** (as-of Wed 8/26).
- **MOVE / VIX:** daily via FORGE (`^MOVE` is T+1 on this feed — declare the basis).
- **Reusable fetchers:** `scripts/cftc_tff_rates.py` (weekly + YTD merge); the multi-year base-rate pull used for §2 runs off the same raw archives and reproduces the table in one pass.

---

## ★ GRADED — Sun 2026-08-23 (the overdue leg-(a) pass; covers 7/21 → 8/18 CFTC, → 8/12 NY Fed PD, → 8/21 MOVE)

**Overdue since 7/25** — carried on the owed list through five closeouts. Graded tonight off a purpose-built reusable fetcher, `scripts/cftc_tff_rates.py` (CFTC TFF **raw files**, not Socrata; as-of dates are TUESDAYS, files publish Fri ~15:30 ET).

**Verdict: CONJUNCTION NOT MET — 0-of-3.** No joint PROME/NEXUS write-up owed. **But the shape is the finding: two legs printed their CLOSEST-EVER approach in this window while the third moved decisively the other way.**

| Leg | Grade | Data [as-of] | vs terms |
|-----|-------|--------------|----------|
| **W1 — SOFR-3M lev net** | **NOT FIRED** — *closest approach on record* | net **−2,530,893 [8/18]** (L 1,052,967 − S 3,583,860). Weekly ΔNET across the window: +92,780 [7/21] · **+248,236 [7/28]** · −86,148 [8/04] · −27,730 [8/11] · +28,923 [8/18] | (a) new record past −2,950,000? **NO** — moving *away*, 413K less short than the −2,943,898 [6/30] peak. (b) one-week cover >300,000? **NO** — but **248,236 [7/28] is the LARGEST single-week cover in the series, 83% of the line**, 51,764 short of firing. It landed in **FOMC week** (7/28-29) and reads directional/policy-path, not RV — the expected signature per the §Basis-vs-directional discriminator |
| **W2 — dealer warehouse** | **NOT FIRED** — *and moving decisively AWAY from the line, in the direction that matters* | **G10 −$6,929mm [8/12]**, the least-short print of the window (7/15 −9,319 · 7/22 −9,735 · 7/29 −8,855 · 8/05 −9,157 · **8/12 −6,929**). **G5L10 +$1,921mm [8/12]** — 7/29 +793 · 8/05 +508 · **8/12 +1,921** | G10 < −$12.0B? **NO** (−$6.9B; ~$5.1B of room, and the 2026 extreme −$11,663 [6/10] is receding). G5L10 < −$800mm ×2 consecutive? **NO** — it never reached −800 once, and the last **three** prints are strongly **positive**. Source: NY Fed PD API `PDPOSCSBND-G10`/`-G5L10`, series break **resolved at runtime** (`SBN2024`) — ⚠️ a stale break returns a valid 200 whose data stops in mid-2024, and a mis-cased code returns an EMPTY 200; both traps hit me tonight before the fix (BOND's `fr2004_fetch.py` documents them) |
| **W3 — rates-vol** | **NOT FIRED** — *closest approach* | **MOVE 73.40 [8/21]**, window max **83.02 [7/31]** (also 80.48 [8/03], 80.08 [7/23]); **VIX 15.13 [8/21]** | MOVE >85 while VIX <20? **NO** — but 83.02 is **1.98 points** under the line **with the VIX condition satisfied**, the nearest W3 has come. VIOLET-owned figure |

### ★ THE FINDING — W1 IS BLIND TO THE BEHAVIOUR IT WAS BUILT TO WATCH (→ KB-LIQ-097)

**The pin has materially unwound and W1 could never have said so.**

| SOFR-3M lev net | as-of | contracts |
|---|---|---:|
| peak | 6/30 | **−2,943,898** |
| now | 8/18 | **−2,530,893** |
| **cumulative** | 7 weeks | **+413,005 covered (−14.0%)** |

At the spec's own $240–250K/contract band that is **≈ −$100B of notional pin removed** (≈$707–736B → ≈$607–633B). **413,005 exceeds W1's own 300,000 trigger by 38% — and no weekly print came close**, because it arrived as a **seven-week bleed averaging ~59K/week.**

> **W1 keys on a WEEKLY delta. The position is exiting on a MULTI-WEEK drift. A weekly-delta trigger cannot see a cumulative one — it is shaped to catch a squeeze and is blind to an orderly exit, which is the more likely way a record position actually leaves.**

This is the time-dimension twin of KB-LIQ-095/084/080: an instrument that cannot see the thing it was built for because of how it aggregates. **⚠️ Route-out owed to PROME — GATE-LIQ-076's W1 wording needs a cumulative leg. I do not edit GATES.tsv.** Suggested, not adopted: *"OR cumulative net change ≥300,000 over any rolling 8-week window."* On the current tape that leg would have fired ~8/04 and would be firing now.

**Directional-vs-RV read on the 248,236 cover [7/28] (discriminator applied):** it is 8.4% of the position and landed in **FOMC week**. Same class as the 7/14 cool-CPI cover, one size up: a **directional/policy-path** trim, not an RV unwind and not a squeeze. Consistent with W2 moving the *opposite* way — a genuine funding-stress unwind would push dealer warehouse short *wider*, and it went from −$9.6B to −$6.9B while the 5–10y bucket flipped **net long**.

**Cross-read that matters more than the grade:** W2's direction independently corroborates BOND's benign dealer read *and* my 8/23 KB-BND-092 refutation. **Dealers are ADDING inventory, not shedding it** — a withdrawing warehouse bid is the one thing all three theses would have needed, and it is absent in the series built to measure it.

**Next graded read:** CFTC TFF Fri **8/28** (as-of Tue **8/25**) — ⚠️ **this is also the 8/26 5Y auction's positioning read, and it publishes two days AFTER the auction (KB-LIQ-096). Do not grade the 8/26 auction's basis leg on 8/26.** NY Fed PD ~Thu **8/27** (as-of 8/19).

---

## GRADED — Sat 2026-07-18 (post-CPI COT [as-of 7/14] + PD [as-of 7/8], primary files)

**Verdict: CONJUNCTION NOT MET — 0-of-3 legs fired.** No joint PROME/NEXUS amplification write-up owed. The hot-print-into-loaded-book scenario did not materialize: CPI 7/14 printed COOL, so the loaded short was not squeezed and dealer capacity was never tested.

| Leg | Grade | Data [as-of] | vs terms |
|-----|-------|--------------|----------|
| **W1 — SOFR-3M lev net** | **NOT FIRED** | **−2,786,954 ct [7/14]** (L 1,108,561 − S 3,895,515), an **85,452-ct COVER** off −2,872,406 [7/7]; ≈ **−$680B** (band $669B @$240K/ct → $697B @$250K) — still record-zone | (a) new record past −2,950,000? **NO** (less short than the −2,943,898 [6/30] peak). (b) cover >300,000? **NO** (85,452). Source: raw CFTC TFF `FinFutWk.txt` futures-only, released Fri 7/17 3:30 ET — **graded off the raw file, NOT Socrata** (which lags releases). Reconciled to prior via change columns (ΔLong +61,925 / ΔShort −23,527 = +85,452 net cover ✓) |
| **W2 — dealer warehouse** | **NOT FIRED** | **G10 IG >10y −$9,589mm [7/8]** (vs −$9,402mm [7/1]; w/w −$187mm more short), ~$2.4B from the line. **G5L10 +$168mm [7/8]** (vs −$213mm [7/1], back positive) | G10 < −$12.0B? **NO** (−$9.6B; 2026 extreme was −$11,663 [6/10]). G5L10 < −$800mm ×2 consecutive weeks? **NO** — still oscillating (−825[6/17]→+365[6/24]→−213[7/1]→+168[7/8]). Source: NY Fed PD API `PDPOSCSBND-G10`/`-G5L10` |
| **W3 — rates-vol** | **NOT FIRED** | **MOVE 68 / VIX 18.71 [7/17 close]** | MOVE >85 while VIX <20? **NO** (MOVE 17bp under the line). VIOLET-owned figure |

**Directional-vs-RV read on the W1 cover (discriminator applied):** the 85,452-ct cover (3% of the position) landed into a COOL CPI 7/14 — a cool print puts the substantially-directional short modestly offside → a small front-end/STIR cover bid. This is the *expected directional signature* (cover tracks the disinflation surprise), **not** an RV unwind and not a systemic squeeze. The short remains **near-record** (−2.79M ≈ −$680B, ~5% off the −$736B/−2.94M [6/30] peak) — the pin is intact, marginally trimmed. No swap-spread cross-check needed for grading since W1 did not fire; had it fired on the cover, the check would be: swap spreads stable = directional squeeze, moving = RV unwind (§ Basis-vs-directional caveat).

**WALTER structural-why caveat carried (alongside, not instead of, the mechanical verdict):** the leveraged short is a 28-yr record (first since 1998) warehoused ~1:1 by a dealer mirror-long — the sourced 'why' leans **structural** (hedging/warehouse flow + higher-for-longer repricing), NOT directional bear conviction. A near-record short that is structural is not itself a fresh bear signal; the conjunction gate is the discipline that keeps positioning magnitude from being over-read as transmission.

**Next graded read:** CFTC TFF Fri 7/24 (as-of Tue 7/21); NY Fed PD ~Thu 7/23 (as-of 7/15). Rolling 2-week conjunction window resets — the 7/11-registration window closes with 0-of-3.

## Cadence + next prints

- **CFTC TFF:** Fridays ~3:30 ET; next = 7/17 carrying **as-of Tue 7/14 = the post-CPI positioning read** (does the short cover into a hot print?).
- **NY Fed PD:** weekly Thu; next release ~7/16 (as-of Wed 7/8).
- **MOVE:** daily via FORGE from Mon 7/13.
- Feeds: KB-LIQ-074 (slow-lead leg), ES-LIQ-02/04 (tracker cross-refs), NEXUS CPI-week read. Registered in KB as **KB-LIQ-076**.
