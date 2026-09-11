# VIOLET → PROME · 2026-09-11 01:0x ET · **VECTOR 2 — cheap vol into FOMC 9/16. VERDICT: NOT CHEAP. STRUCTURE: NONE.** (DOCKET L326)

## COMPLETION — VIOLET — 2026-09-11
STATUS: ✅ DONE
CHANGED: PROME/inbox/2026-09-11_from-VIOLET_VECTOR-2-cheap-vol-into-FOMC-read.md, AGENTS/VIOLET/STATUS.md, AGENTS/VIOLET/SCRATCH.md, AGENTS/VIOLET/NEXUS_BRIEF.md, AGENTS/VIOLET/workbook/KB.tsv, AGENTS/VIOLET/workbook/VX_DAILY.tsv, AGENTS/VIOLET/board_log.tsv, inbox→processed (13 files)
RESULT: Index vol is NOT cheap — the window closed between 9/8 and 9/10. VVIX 84.42→102.66 (+21.6%) and VIX9D 11.97→17.70 (+47.9%) in four sessions on CBOE settles; cheap-tail window CLOSED (L1 and L2 both fail); VIX 17.84 vs SPX RV10 9.84% = VRP +8.00 vol pts (1.81×). STRUCTURE = **declared NONE** on four independent legs of the design's own letter. New: OVX/VIX 3.41 (p96.6) 🔴 FIRE with the NUMERATOR leading this time (OVX +35.1% vs VIX +22.8%) — oil→equity-vol transmission is live, which makes any long-vol add CORRELATED with the $6,007 energy sleeve, not a diversifier. Found `vx_daily_gapcheck.py` structurally blind to leading-edge gaps (rc=0 "no gaps" with 3 sessions missing) — 3 rows restored, 2,514 CBOE cells agreed, 0 corrected.
GAPS: SPX/VIX option CHAINS not priced — bid/ask/IV/OI is TERRY's data and domain (design §5); the debit-to-width test is stated in measurable form, not computed. COT 9/8 report not out (releases Fri 9/11 15:30 ET).
WILL_NEEDS: None. No card, no order, nothing to approve — the read is STAND DOWN.
FOLLOW-UP: Grade the pre-registered falsifier at the 9/16 close (below). VIO-FOMC-0916 (L276–L278) FROZEN and untouched — unchanged by this.

---

# 1. VERDICT FIRST

> ## ⛔ **INDEX VOL IS NOT CHEAP AGAINST THIS STACK. IT WAS CHEAP ON 9/4 AND THE WINDOW CLOSED BETWEEN 9/8 AND 9/10.** The single most important number is not VIX — it is **VVIX 102.66 [9/10 CBOE SETTLE, VERIFIED]**, up **+21.6%** from 84.42 [9/4]. **VVIX is the price of the exact thing the rising-vol design would buy**, and it repriced harder than the thing it is written on. **I propose nothing. STAND DOWN.**

**The four-session repricing, all CBOE `*_History.csv`, own pull 2026-09-11 ~00:5x ET (HTTP 200; VIX 472,513 B · VVIX 108,562 B · SKEW 202,938 B). All VERIFIED.**

| Instrument | 9/4 SETTLE | **9/10 SETTLE** | Δ | Read |
|---|---:|---:|---:|---|
| **VVIX** | 84.42 | 🔴 **102.66** | **+21.6%** | 1y pct **69.8**. The convexity itself got expensive |
| **VIX9D** | 11.97 | 🔴 **17.70** | **+47.9%** | The front end that was "cheapest of the leg" is gone |
| VIX | 14.53 | **17.84** | +22.8% | 1y pct 59.1 (1y range 13.47–31.05) |
| VIX3M | 17.61 | 19.73 | +12.0% | |
| VIX6M | 19.89 | 21.17 | +6.4% | Long end moved least — this is an EVENT bid, not a regime re-rate |
| **VIX9D / VIX** | 0.8238 | **0.9922** | **+0.168** | Front end has fully caught the belly |
| **VIX3M / VIX** | 1.2120 | **1.1059** | **−0.106** | Cash curve FLATTENED — was steepening on 9/4 |
| **M1:M2 contango (adj)** | +11.51% | **+5.53%** | **−5.98 pp** | VX/U6 18.1289 : VX/V6 19.1305 [9/10 CBOE settlement CSV, 1,731 B] |
| `^SKEW` daily | 151.58 | **147.02** | −3.0% | 1y pct 69.4. **The tail did NOT lead this — it gave back** |
| `^SKEW` 20d avg | 143.42 | **145.21** | +1.79 | Elevated-SKEW regime **UN-TERMINATED**, still climbing |
| **MOVE (rates vol)** | 73.10 | 🔴 **82.09** | **+12.3%** | **+9.68 over F1 (72.41) · +6.59 over confirm-3 (75.50)** [investing.com PRIMARY, move.py] |
| **OVX (oil vol)** | 44.96 | 🔴 **60.76** | **+35.1%** | p92.9. **See §4 — this is the new thing** |
| COR1M (implied corr) | 8.60 [9/6] | **14.38** [9/11 TICK] | +67% | ⚠️ tick, not a settle |
| CCC OAS · CCC−BB | 10.51 · 8.99 [9/3] | 10.64 · **9.06** [9/9 FRED] | +0.13 · +0.07 | Dispersion still through 8.00, widening slowly |

🔑 **THE SHAPE OF THE MOVE IS THE ARGUMENT.** VIX9D rose **+47.9%**, VIX **+22.8%**, VIX6M **+6.4%** — a clean monotone decay with tenor. That is the signature of a **dated event being priced**, not of a regime re-rating. And `^SKEW` — the leg that was at a new leg high on 9/4 — **fell 3.0%** while everything else rose. **The bid moved from the far tail to the front end. You do not buy the front end after it has repriced +48%; that is the definition of paying up.**

---

# 2. IMPLIED vs REALIZED — the measurement that settles "cheap"

**SPX realized, own calc off yfinance `^GSPC` closes through 9/10 (log returns, ann ×√252). VERIFIED.**

| | Value | vs implied |
|---|---:|---|
| RV5d | **11.17%** | VIX9D 17.70 ⇒ **+6.53 vol pts** |
| RV10d | **9.84%** | VIX 17.84 ⇒ **+8.00 vol pts · 1.81×** |
| RV20d | **8.73%** | |
| Parkinson 10d (hi/lo) | 6.26% | intraday ranges even quieter than closes |

**Last five SPX sessions: 7,747.71 → 7,718.60 → 7,673.52 → 7,636.36 → 7,591.70. Three straight down days of −0.59% / −0.49% / −0.59%.** SPX is **−2.01%** since 9/3 and VIX is **+24.6%** over the same span. **A 2% drift has not produced 2% daily moves; it has produced a 24% vol bid.** That gap IS the event premium, and it is now paid.

### 2b. What the front end actually prices per event day

Strip the quiet days out of VIX9D and see what is left for the events. **Assumptions declared: 6 trading sessions in the 9-calendar-day window (9/11 CPI · 9/14 · 9/15 · 9/16 FOMC · 9/17 · 9/18 OPEX); the three non-event days run at trailing RV10 9.84%; trading-day (252) variance accounting.**

> Total front-end variance 7.459e-4 − 3 quiet days 1.153e-4 = 6.307e-4 over 3 event days ⇒ **σ ≈ 1.45% per event day (≈23.0% annualized).**

**⇒ The market is paying for a ~1.45% SPX move on each of CPI, FOMC and triple-witching day, against a 10-day realized daily move of 0.62%.** That is a **2.3× uplift on event days**, fully priced, four sessions ahead. **It is not obviously wrong — and it is not cheap.** Token: **INFERRED** (the decomposition is an estimate with stated assumptions; the inputs are VERIFIED).

---

# 3. THE EVENT STACK IT IS PRICING

| When | Event | State | Token |
|---|---|---|---|
| **Fri 9/11 08:30** | **August CPI** | Nearest HIGH/MED catalyst, **0d** (`cheap_tail.py` calendar-day basis) | VERIFIED |
| **Wed 9/16 14:00** | **FOMC + SEP + dot plot** | **Hike odds have MOVED off the coin flip.** CME FedWatch **~59–60%** for +25bp · Kalshi **57%** · Polymarket **49%** (web, 9/10–9/11). Packet's PM 50.5 / Kalshi 50.0 are **[9/7] and 4 days stale.** Drivers cited: strong August payrolls, hot PPI, Warsh hawkish, energy costs | **INFERRED** (search extract of secondary coverage; not fetched at CME primary) |
| **Wed 9/16 (AM)** | **VIX September quarterly settlement** — VX/U6 final settlement date **2026-09-16** per the CBOE settlement CSV | 🔑 **SEE §5 — it settles BEFORE the 2pm statement** | VERIFIED |
| **Fri 9/18** | **SPX quarterly OPEX / triple witching** | **$9.6T of US options exposure expires between now and 9/18 (~35% of total US options exposure); $6.2T on 9/18 itself (~23%)** — tracking to beat June's $7.7T record. **Traces to a Citadel Securities publication ("September Setup: The Asymmetry Has Changed"), NOT merely the X post WALTER relayed** | **VERIFIED that the source is Citadel primary; INFERRED on the exact split** (direct fetch of the Citadel page returned **HTTP 403**; figures are from the search extract of that page) |
| **9/10 (done)** | **Brent +7.15% to $108.45**; East–West pipeline reportedly struck 17:56Z 9/10 | **FALCON tell #2 NOT FIRED / pending confirmation · BRENT BG-02 NOT MET** — PROME-verified, not re-graded here. Brent **$107.89 (+0.24%) 2026-09-11** [fetch.py BZ=F, yfinance basis] | per PROME packet |

**Gamma (HENRY's, cited not re-derived):** HENRY's board is **EXPIRED, not current** — last measured 9/4 on the 9/3 close: flip band **7,691–7,695**, Net GEX **≈ +$38B/1%**, dealers DAMPEN. HENRY's own finding is that **the sign has a one-session shelf life** (flipped twice in seven days: +$20.4B [8/28] → −$16.7B [9/2] → +$36.8B [9/3]). Spot 7,591.70 is **~100 points below that stale band**, which HENRY labels *"plausibly negative gamma, UNVERIFIED — arithmetic on a stale flip level, not a measurement."* **I carry HENRY's token as written and add nothing.** HENRY says re-run `gamma_flip.py --days 35` before 9/16 and 9/18.

**FT-10 (RED's, cited not re-graded):** RED graded the run **BROKEN, 0-of-4** on 2026-09-09 — 9/8's 148.86 killed the 150.63 [9/3] · 151.58 [9/4] pair on its value, Labor Day bridged as a non-session by RED's own 9/6 ruling. **I add only the dated bars since:** `^SKEW` **149.25 [9/9] · 147.02 [9/10]**, both <150, both CBOE-VERIFIED at my own pull. **The count stays 0; earliest possible fire is unchanged in RED's hands.** RED's fence holds and I repeat it: *the run broke ≠ the tail bid is gone* — the 20d average is **145.21** and rising.

---

# 4. 🔴 THE NEW THING, AND IT IS NOT AN ARGUMENT FOR BUYING VOL — IT IS AN ARGUMENT ABOUT CORRELATION

**`ovx.py` [2026-09-10]: OVX 60.76 (p92.9) · gap 42.92 (p96.2) · OVX/VIX 3.41 (p96.6) ⇒ 🔴 FIRE.** Ladder re-derived n=4,865 from 2007-05-10: p95 FIRE line = 3.21.

⚠️ **THIS FIRE IS NOT THE 9/3 FIRE, AND THE DIFFERENCE IS THE WHOLE POINT.** On 9/3 I refused to upgrade OVX in the convergence matrix because the ratio was elevated on the **DENOMINATOR** — OVX fell, VIX fell faster (`[[finding_spread_metric_blind_to_common_mode]]`). **This time the numerator leads: OVX +35.1% [44.96→60.76] against VIX +22.8% [14.53→17.84].** Both rose; oil vol rose half again as fast. Analog anchors the ladder carries: Abqaiq 2019-09 ratio 3.31 (fired, correctly) · Israel-Iran 2025-06 ratio 3.31 (fired) · Ukraine 2022-03 ratio 2.16 (**refused** — broad co-move, oil not leading). **At 3.41 this sits above both fired analogs.** Context canary, **not an action gate** — routes to BRENT/HAWK reference.

🔑 **THE SIZING CONSEQUENCE, WHICH IS THE ONE THING ONLY THIS DESK CAN SAY:** the energy sleeve is already **~$6,007 on "Mideast stays hot"** (9/10 close). With OVX/VIX at p96.6 and oil vol leading, **a long index-vol structure bought today is substantially the SAME BET, expressed twice.** It would not diversify the sleeve; it would lever it. **Size any adjacent idea against the sleeve, never per-card** — and on this measurement the honest answer is that there is no adjacent idea worth the correlation.

---

# 5. THE STRUCTURE THE RISING-VOL DESIGN NAMES: ⛔ **DECLARED NONE**

**Source of record: `AGENTS/VIOLET/outbox/2026-08-20_to-PROME_rising-vol-registration-DESIGN-v1-trigger-gated.md` (DOCKET L163, commission closed).** The design DOES name a shape — §5: *defined-risk OTM **VIX call spread** (debit) · **30–60 DTE at entry** · lower strike **above** spot · 100% loss is the base case · mandatory harvest at **2× debit** · strikes and exact expiry are **TERRY's at fire-time**.* **But it does not name one for TODAY, and four independent legs of its own letter say so:**

| # | Leg | State on 9/10 | Verdict |
|---|---|---|---|
| **1** | **Entry gate A1–A4 does not arm.** A1 VVIX ≤90 · A2 VIX ≤16 · A3 SKEW ≥140 · A4 catalyst ≤21d, all four on **2 consecutive settles** (A5) | `cheap_tail.py [2026-09-10]`: ⚪ **DORMANT 2/4** — A1 **102.66 > 90 ✗** · A2 **17.84 > 16 ✗** · A3 147.02 ✅ · A4 0d ✅ | **NO FIRE** |
| **2** | **The gate is RETIRED anyway.** GATE-VIO-RV1 **F2-KILLED 2026-08-27** on its own pre-registered falsifier: post-2018 n=22, 60td/≥+50% lift **1.36×, p=0.134** vs the p<0.05 bar it was certified on (pre-2018 n=12 was 1.92×, p=0.024 — the edge lived in a dead regime) | KB-VIO-211 | **A killed gate has no fire condition to meet** |
| **3** | **S1 stand-down is 2.34 points away.** §4: *"S1 VVIX ≥ 105 — the convexity got expensive, the reason to own it is gone"* | VVIX **102.66** | **Buying into a near-triggered stand-down** |
| **4** | **F3 falsifier is the live one.** §6: *"If at fire-time VIX call skew is rich enough that the OTM spread costs more than ~⅓ of its max width, the dislocation is priced and there is nothing to buy. **A cheap-tail window with expensive tails is a contradiction and the correct action is to stand down, not to pay up.**"* | VVIX at 1y p69.8 after +21.6% in four sessions | **Expect F3 to bind. Token: INFERRED — the chain is TERRY's to pull, not mine to guess** |

### 5b. 🔑 AN INSTRUMENT FACT THAT BINDS EVEN IF EVERY LEG ABOVE FLIPPED

*(Provenance: the settlement-timing point is NOT new tonight — my own `NEXUS_BRIEF` carried it on 9/6. What is new is that it is now **verified at the CBOE settlement file** rather than asserted, and that the weekly rows turn out to be a flat-repeat artifact.)*

**There is no September VIX contract that spans the FOMC decision.** `VX/U6` carries final settlement date **2026-09-16** in the CBOE settlement CSV — VIX September futures and options settle at the **SOQ on the morning of 9/16**, hours **before** the 14:00 ET statement. **A "VIX structure with an expiry across 9/16" is necessarily an OCTOBER structure**: `VX/V6`, expiry **2026-10-21**, forward **19.1305 [9/10 settle]**, **40 DTE from today — inside the design's 30–60 DTE band**, and the contract that becomes M1 on the morning of the meeting (KB-VIO-218). ⚠️ **The M1:M2 pair therefore breaks basis on 9/16** (VX/U6:VX/V6 → VX/V6:VX/X6); do not read the contango series across that date.

⚠️ **And the CBOE settlement file's weekly rows are a flat-repeat artifact, not a curve:** VX38/U6 (9/23), VX39/U6 (9/30), VX40/V6 (10/7), VX41/V6 (10/14) all print **18.1289**, identical to VX/U6. **I am not building a weekly term structure out of five copies of one number.** Real monthly curve 9/10: **18.1289 (9/16) → 19.1305 (10/21) → 19.5535 (11/18) → 19.6430 (12/16).**

**⇒ RECOMMENDATION: NONE. No card, no structure, no order.** If Will wants the question re-opened, the re-open condition is mechanical and stated in §7.

---

# 6. THE ENTRY GATE, WRITTEN AS ROOT RULE #6

**Root rule #6 = "puts on green days, calls on red days."** A long-vol structure is the **convexity-buying** side, so it takes the **PUT** treatment: **buy it on a GREEN day.**

- **9/10 was a RED day:** SPX **−0.58%** (7,636.36 → 7,591.70), VIX **+8.38%**. **Buying long vol into that tape is the textbook proxy violation** — you are paying the day's fear premium.
- **The gate, if this ever became a card:** *no long-vol debit is entered on a day SPX closes lower. The first qualifying session is a GREEN SPX close with the structure's debit measured on that day's chain.*

**The direct measurement that would justify a break** (TERRY's ratified test, `AGENTS/TERRY/RISK_RULES.md` § "Breaking root rule #6" — the proxy answers *"am I paying up for convexity?"*, and only a number that refutes it is a break):

> **The October VIX call spread marks at a DEBIT ≤ ⅓ of its max width on the live chain, and that debit is LOWER than the same structure's debit on the most recent GREEN session — both figures written on the card, in the chain's own numbers, BEFORE the fill.**

That is the design's own F3 threshold used as the break test, so the break cannot be argued into existence — it either prices under ⅓ width or it does not. ⛔ **"The window is closing before FOMC" is a CHASE, not a break** (RISK_RULES, verbatim). ⛔ **No hard guard may be relaxed to make it fit** — S1 (VVIX ≥105) and the A1–A4 letter bind as written, and I am not reinterpreting a threshold I wrote on a night I would find it convenient to. **At VVIX 102.66 my expectation is that this test FAILS; I am not computing it, because bid/ask/IV/OI is TERRY's data and TERRY's domain (design §5).**

---

# 7. FALSIFIER — what would make THIS read wrong, pre-registered before the events

**F-A (the configuration test) — the cheap-tail re-open rule, stated mechanically as PROME asked:** the window re-opens **only when all four legs print on ONE dated CBOE close** — VVIX ≤90 **AND** VIX ≤16 **AND** `^SKEW` ≥140 **AND** nearest HIGH/MED catalyst ≤21 calendar days — and the design's A5 needs that on **two consecutive settles**. **From 102.66, VVIX must fall 12.4% and VIX 10.3% for that; it is not a near miss.** If it happens before 9/16, this read is wrong and I say so.

**F-B (the quantitative test, gradeable at the 9/16 close) — the one that can actually kill me:** **if SPX realized volatility over 9/11–9/16 comes in ABOVE 17.84% annualized** (i.e. daily closes averaging **>1.12%** absolute over those 4 sessions), then the front end was not rich — it was right or cheap — and the VRP argument in §2 is refuted on its own instrument. **Registered now, with no position riding on it, before CPI prints.**

**F-C (scope):** F-B grades the LEVEL call. It does **not** grade the structure call — §5 legs 2 and 5b (a killed gate; no September VIX expiry spans the decision) hold **whatever realized vol does.**

---

# 8. HONEST LIMITS — the against-case, stated rather than disclosed away

1. ⚠️ **I AM COMPARING A FORWARD-LOOKING PRICE TO A BACKWARD-LOOKING MEASUREMENT, AND THAT IS THE WEAKEST JOINT IN §2.** RV10 of 9.84% was realized over a tape that had **not yet met CPI or a live hike**. The correct comparator for VIX 17.84 is *forward* realized, which does not exist yet. **STATED, NOT RESOLVED.** F-B exists precisely to settle it against the world instead of against my preference.
2. **Realized is RISING, not flat: RV20 8.73% → RV10 9.84% → RV5 11.17%.** The trend runs *toward* the implied, not away from it. A +8.00 VRP measured against a decelerating realized would be a strong rich signal; against an accelerating one it is weaker.
3. **§2b's per-event-day number depends on its own assumption.** If the three quiet days run hotter than 9.84%, the residual event premium is smaller and vol is less rich than I have called it.
4. **Three channels turned on at once and that is what a regime change looks like.** MOVE re-armed **+9.68 over F1** (from "all but dead" at 73.10 on 9/4), OVX fired on the numerator, COR1M nearly doubled. **In a regime that is actually turning, "expensive versus trailing realized" is exactly what you pay, every time.** My own thesis carries a **68% fade base rate** against that — but **that base rate was built on episodes without a live hike and without a supply shock**, so I am not hiding behind it.
5. **The crack-vs-fade tree (KB-VIO-123) moved 0-of-6 → 1-of-6:** ③ MOVE 82.09 ≥ 75.50 ✅ **FIRED** · ④ VVIX 120 ✗ (102.66, closing) · ⑤ inversion ✗ (1.1059, but moving *toward* from 1.2120) · ⑥ VIX>20 ✗ (17.84) · ② COT p51.9 ✗ (9/1 report; 9/8 releases Fri 15:30) · ① credit LIQUID's. **Three of six are moving the right way for the bears. One fired leg is not a tree.**
6. **`^SKEW` is the leg that argues *against* my own bearish-vol read and I am not burying it:** the daily gave back to 147.02 while everything else bid. The tail did **not** lead this move. The 20d average (145.21, rising) says the regime is intact; the daily says the marginal buyer this week wanted the front end.

---

# 9. WHAT I DID TO MY OWN INSTRUMENTS (reported, not asked about)

🔑 **`vx_daily_gapcheck.py` — built 2026-09-06 to catch exactly this — is STRUCTURALLY BLIND to a gap at the leading edge, and it certified the ledger green while three sessions were missing.** At `AGENTS/VIOLET/scripts/vx_daily_gapcheck.py:121-122` the audited span is `lo = args.since or min(have)` / **`hi = max(have)`**, where `have` is **the ledger's own dates**. **The upper bound of the audit is the last row of the thing being audited, so a missing session after it cannot exist by construction.** Measured: with 9/8, 9/9 and 9/10 absent it printed `✅ rc=0 — 416 session(s) … no gaps`; with all three restored it prints `✅ rc=0 — 419 session(s) … no gaps`. **Identical verdict in both states.** Its own docstring says it exists because *"today is fresh no matter how many holes sit behind it"* — **it closed the holes BEHIND and left the hole AHEAD open.** `[[finding_instrument_reports_clean_against_the_wrong_reference]]`, 9th form: the reference is *derived from* the audited artifact. ⛔ **NOT FIXED TONIGHT** — changing a closeout-BLOCKING guard's span at 01:0x on one session's diagnosis is the ship-then-audit pattern GATE-VIO-RV1 was killed for. Diagnosis written where the next reader meets it; code change is the top instrument item for my next session. → **KB-VIO-273**

- **3 rows restored** (2026-09-08/09/10) from CBOE, all six spot columns confirmed, `basis=SETTLE`; `m1m2` left **blank** (the T-1 vs same-day convention hazard is unresolved and a blank is the absence of a claim, not a guess). **Verified by re-running `backfill.py --spot-only`: 2,514 cells agreed, 0 corrected, 0 filled.**
- **`backfill.py` UPDATES rows, it does not CREATE them** — so the ledger cannot self-heal a trailing-edge gap even when CBOE has the data. Named, not fixed.
- **Publisher quirk, recorded:** CBOE `VIX_History.csv` carries a **09/07/2026 (Labor Day) bar at 15.30** while VIX9D, VIX3M, VVIX and SKEW **all omit it**. The gapcheck's orphan-VIX discriminator handles it correctly (13→14 phantoms excluded). **It also corroborates RED's non-session ruling at the publisher of record: `SKEW_History.csv` has no 9/7 bar.** Anything reading `^VIX` alone across that date will mis-align against the other five.
- **RED's 9/9 packet named three of my surfaces carrying the stale count. Two do** (STATUS chain, the "two consecutive ≥150" line) — **both corrected.** The third, **`scripts/skew_integrity.py`, does NOT** — I checked the owner-declared path and grepped the file; no count, no threshold, no run-state. **Absence VERIFIED at the named artifact, not inferred from a broad grep.**

---

# 10. INBOX DRAINED — 13 of 13, every sender (WQ-206 outcome ①)

| Item | Disposition |
|---|---|
| 9/06 PROME — Codex backfill 2nd pass | **acted** (shipped 9/6; receipt `research/2026-09-06_wq188_2nd_pass_receipt.md`) |
| 9/09 RED — FT-10 run broken, 0-of-4 | **acted** — surfaces corrected; 3rd named surface verified clean |
| 9/10 DEWEY — REQ-002, no near-dated cliff | **info-only** — no vol content; T1/T4/T5 are DEWEY's dated items, not mine |
| 9/10 PROME — cheap-tail CLOSED | **acted** — re-graded **2/4 DORMANT** on the 9/10 bars; **re-open rule written** (§7 F-A) |
| 9/11 PROME — VECTOR 2 | **acted** — this memo |
| SIG-W-20260908-001/002/003/017 | **noted** — NVDA/HBM/DRAM/ASML; no vol content, no surface of mine carries them |
| SIG-W-20260908-010 | **noted** — the withdrawn 0.79%/session figure was never on a VIOLET surface; my ledger has been CBOE-sourced since 9/6 |
| SIG-W-20260908-019 | **acted** — 9/8 SKEW 148.86 confirmed at my own pull; matches RED |
| **SIG-W-20260910-010** ($9.6T) | **acted — VERIFICATION RETURNED.** Traces to a **Citadel Securities** publication, not merely the X post. **And the relayed shape needs correcting: $9.6T expires BETWEEN NOW AND 9/18 (~35% of total US options exposure); $6.2T on 9/18 ITSELF (~23%).** WALTER's kernel reads as if all $9.6T lands on 9/18. Direct fetch of the Citadel page returned **HTTP 403**, so the split is **INFERRED** from the search extract. **The shape survives either way: biggest quarterly OpEx of the year.** |
| SIG-W-20260910-013 (MS $3.1tn) | **noted** — backdrop; no vol instrument |

*Every file `git mv`'d to `processed/`; WALTER lane rows appended to `board_log.tsv` with `source=INBOX_WALTER` per `BOARD_CONSUMPTION_SPEC.md` v0.2.*

---

**⛔ NOTHING FIRED. I PROPOSE NOTHING. FLAT.** No card, no order, no structure — **TERRY constructs nothing from this page because the page names nothing to construct.** `VIO-FOMC-0916` (DOCKET L276–L278) is **FROZEN and untouched by this work**; it grades at the 9/16 · 9/18 · 9/23 closes on its own letter.

**— VIOLET**, 2026-09-11 01:0x ET. *(Self-authored packet, carve-out ①; committed by author. Reproduce §1 and §2 from CBOE `*_History.csv` + `^GSPC` closes; method stated inline.)*

---

# ADDENDUM — 2026-09-11 01:2x ET · three things that landed AFTER the block above was written

**Appended rather than rewritten, and the memo above is unedited** — a delivered record is not re-derived. **None of it changes the verdict.**

**① 🔴 A SECOND GUARD OF MINE HAS A WRONG REFERENCE, AND THIS ONE IS THE MORE DANGEROUS.** `closeout_guard.py`'s cross-surface leg (`surface_agreement.py`) **blocks my closeout on two figures and both disagreements are CORRECT AND INTENDED.** `resolve()` (`:64-81`) globs `PROME/inbox/` **and** `processed/` and reads **every** `*_from-VIOLET_*` match together — a documented choice, so an addendum contradicting its own memo cannot hide — **but it is never bounded to one session.** The five matches are all **2026-09-06** deliveries whose figures (28/50, "2 of 4") were **true at their vintage**. ⇒ **any figure that legitimately changes between deliveries makes this leg red forever, and the red grows by one surface per memo sent.** 🔑 **And its printed remedy — *"fix the non-canonical surfaces by RE-DERIVING"* — is impossible to follow honestly: re-deriving a delivered memo means EDITING HISTORY.** **KB-VIO-273 fails SILENT; this one fails LOUD AND UNFIXABLE, which is the kind that trains a reader to wave reds through — the n=4 `CANARY_MAP` behaviour this guard exists to end.** ⛔ **Neither re-specified tonight.** Correct spec, zero free parameters: **bound the glob to the current session's date prefix.** Disposition written on STATUS ⑦. → **KB-VIO-276**

**② 🟠 JPY CARRY-VOL REFRESHED AND IT IS 0.08 FROM ITS WATCH LINE — SAM, THIS IS YOURS TO OWN.** `jpy_vol.py [2026-09-11]`: **RV10 13.89% (p89.7)**, USDJPY **154.21**, state CALM — from **10.18% / p69.6** on 9/4. **WATCH is 13.97%.** Closest since 7/31. ⛔ **The RV-through-IV leg stays UNUSABLE** (thin-strike guard held: no near-ATM FXY call with OI ≥100 in 25–65 DTE). **Convergence vector 2 → 3 on proximity and rate of change, not on a breach; convergence total 32 → 33/50** (`convergence_score.py` rc=0, declared == computed). **I own only the carry→vol transmission read; SAM owns the substance.**

**③ ✅ `workbook/CATALYSTS.tsv` WAS MISSING THE 9/18 TRIPLE WITCHING ENTIRELY** while HENRY carried it and WALTER routed a signal on it — **a dated event with a named magnitude and no row in either twin.** Added to `CATALYSTS.tsv` and `CALENDAR.md` with the Citadel provenance and the 403 caveat on the row; **9/7 Labor Day graded into CALENDAR's RESOLVED section and pruned from the feed.** `twin_check` **5/5 clean, 1:1, no past rows under the forward heading.**

**Receipts for the whole session:** `convergence_score` rc=0 · `canary_staleness` no stale CURRENT cells, all ledger-backed canaries in contract · `twin_check` 5/5 · `validate_workbook` **276 rows, 0 errors** · `read_cap_check` rc=0 (STATUS **47% of cap**) · `vx_daily_gapcheck` **419 sessions, no gaps** · `backfill.py --spot-only` control **2,514 agreed / 0 corrected**. ⛔ **`closeout_guard` remains RED on the one leg documented in ① — declared, not waved through.**

**— VIOLET**, 2026-09-11 01:2x ET.
