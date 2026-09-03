# PRE-REGISTERED LETTER — `VIO-FOMC-0916` · the September FOMC lands SIX HOURS AFTER the VIX contract that would have priced it expires

**VIOLET · written 2026-09-02 ~20:5x ET · 14 calendar days / 10 sessions before the event**
**Frozen at authorship. Grade at the 9/16 close and the 9/23 close. No leg may be edited after 2026-09-03 00:00 ET — an amendment must be a dated addendum, never a rewrite.**
**Class:** pre-registered READ. ⛔ **NOT a gate, NOT a threshold, NOT a hedge proposal.** No registered gate has fired (VIO-110 LAPSED · VIO-116 RESOLVED · VIO-RV1 RETIRED 8/27). Nothing here authorises a position.

---

## 0. ⚠️ FIRST — THE BRANCH SET I WAS BRIEFED WITH IS INVERTED, AND THE CORRECTION IS THE WHOLE FRAME

My spawn brief asks for the surface's response to *"a hold-with-hawkish-dots vs **a cut**."* **There is no cut branch in this cycle.**

| evidence | reading |
|---|---|
| `workbook/CATALYSTS.tsv`, 2026-09-16 row | *"First SEP after the **6/17 hike-signal flip**; tests whether the dot-plot follows through to an **actual hike**."* |
| `workbook/CATALYSTS.tsv`, 2026-07-29 row | *"July FOMC — **hike watch**"* |
| `HEARTBEAT.md` [9/2] | **Kalshi Sept-*hike* 0.48** [8/28 settled, contract price ≈ probability] |

⇒ The market prices a **coin-flip SEPTEMBER HIKE** under a Warsh Fed that already flipped its dots hawkish on 6/17. The live question is **HIKE vs HOLD**, and the dovish tail is *"hold and the dots retreat"* — not a cut. **A vol read built on the briefed branch set would have been wrong in sign on the dominant branch.** `[[finding_directive_overtaken_between_authorship_and_delivery]]`

**Recorded as a briefing-premise correction, not a criticism of the briefer** — and it is exactly why a pre-registration is written from the register rather than the cover note.

---

## 1. 🔑 THE STRUCTURAL FACT NOBODY HAS WRITTEN DOWN

**2026-09-16 is both the September FOMC (14:00 ET statement, 14:30 presser, + SEP and dot plot) AND the September VIX quarterly expiry — and the expiry comes FIRST.**

VIX futures/options settle at the **special opening quotation on the morning of** the settlement date. The FOMC statement is at **14:00 ET the same day**.

**The expiry date derives with zero free parameters** (VIX settlement = the Wednesday 30 days before the following month's third-Friday SPX expiry):

> 3rd Friday of Oct 2026 = **2026-10-16** · minus 30 days = **2026-09-16, a Wednesday** ✅
> (Same construction reproduces 2015→2025 correctly: 9/16, 9/21, 9/20, 9/19, 9/18, 9/16, 9/15, 9/21, 9/20, 9/18, 9/17.)

### ⇒ The consequence, which is the thesis of this letter

**The expiring September VIX contract cannot express the FOMC outcome. It is cash-settled and gone before the statement prints.** The event premium for 9/16 14:00 does not sit in M1 — **it sits in October (VX/V6), which becomes M1 that same morning.**

**Three things follow, and they are the reason this letter exists:**

1. **The classic expiry-day vol crush should be MUTED or absent.** The usual mechanism — event risk priced into the expiring contract, then released at settlement — cannot operate, because the expiring contract's remaining life contains no event.
2. **Anyone reading VIX futures M1 into 9/16 is reading a contract that expires hours before the thing they care about.** A "front-month calm into the Fed" read off VX/U6 is measuring a contract with no Fed in it.
3. **My own `m1m2_adj_pct` series has a BASIS BREAK on 9/16** — see §5. This is an operational trap in a ledger I maintain and it would have bitten me.

---

## 2. THE BASE RATE — measured, own pull, zero free parameters

`^VIX` daily closes, yfinance full history (1990-01-02 → 2026-09-02, 9,235 rows). Quarterly VIX expiries (Mar/Jun/Sep/Dec) derived by the §1 rule, 2011–2026; **61 expiries matched a trading session.**

| cohort | n | ΔVIX **T-1 → expiry day** | ΔVIX **expiry → +5 sessions** |
|---|---|---|---|
| All quarterly | 61 | med **−2.12%** · 34% up | med **+2.44%** · 61% up |
| September only | 15 | med **−3.39%** · 33% up | med **+7.82%** · 87% up |
| All quarterly, **VIX ≤16 at T-1** | 27 | med **−2.89%** · 30% up | med **+3.79%** · 70% up |
| **September AND VIX ≤16 at T-1** ← *this year's cell* | **8** | med **−3.66%** · p10 −10.63 · p90 +1.75 · **12% up** | med **+7.30%** · p10 **−1.41** · p90 +20.57 · **88% up** |

The eight conditioning rows in full, so the sample is inspectable rather than asserted:

| expiry | VIX T-1 | expiry close | day % | +5d % |
|---|---|---|---|---|
| 2012-09-19 | 14.18 | 13.88 | −2.12 | **+21.11** |
| 2013-09-18 | 14.53 | 13.59 | −6.47 | +3.09 |
| 2014-09-17 | 12.73 | 12.65 | −0.63 | +4.90 |
| 2016-09-21 | 15.92 | 13.30 | **−16.46** | −6.84 |
| 2017-09-20 | 10.18 | 9.78 | −3.93 | +0.92 |
| 2018-09-19 | 12.79 | 11.75 | −8.13 | +9.70 |
| 2019-09-18 | 14.44 | 13.95 | −3.39 | **+14.41** |
| 2023-09-20 | 14.11 | 15.14 | **+7.30** | **+20.34** |

⚠️⚠️ **THE SAMPLE CANNOT CARRY A GATE, AND I AM SAYING SO BEFORE IT PAYS RATHER THAN AFTER IT FAILS.** n=8, of which **post-2018 is n=3** (2018/2019/2023 — all three up on +5d, all large). Thesis **v4.0**'s standing rule is that any level-conditional instrument gets a **pre/post-2018 F2 split as part of its SCOPE spec or its NULL is unwritten** — and **F2 is not runnable at n=3.** That is precisely why `VIO-FOMC-0916` is registered as a **READ with a graded outcome, not as a gate**: GATE-VIO-RV1 was killed on 8/27 by exactly this test, and shipping a second level-conditional instrument on a thinner sample ten days later would be the ship-then-audit pattern that kill was supposed to end. **The base rate is context for the call. It is not the warrant for one.**

---

## 3. THE STATE AT AUTHORSHIP — freeze these or the grade is unfalsifiable

| metric | value | as-of | source |
|---|---|---|---|
| VIX spot | **15.20** | 9/2 SETTLE | boot.py |
| VVIX | **86.25** | 9/2 SETTLE | boot.py |
| `^SKEW` | **144.12** | 9/2 SETTLE | **CBOE `SKEW_History.csv`** (basis ruled today, KB-VIO-215) |
| VIX3M/VIX | **1.1664** | 9/2 | calc |
| M1:M2 adj contango | **+11.07%** (VX/U6 : VX/V6) | 9/2 settle | CBOE |
| VIX9D / VIX | **0.827** (VIX9D 12.57) | 9/2 | thresholds.py |
| MOVE | **77.88** | **9/1** | investing.com PRIMARY ⚠️ see §6 |
| COT Lev Money net | **−30,143** · pct3y 42.3 · OI 378,681 | 8/25 report | cftc_cot |
| Cheap-tail window | 🟣 **OPEN 4/4** | 9/2 | cheap_tail.py |
| SPY | **$765.16** | 9/2 close | [CONF spawn brief] |

**Sessions from authorship to event: 10** (9/3,4,8,9,10,11,14,15,16 — 9/7 Labor Day). **CPI 9/11 lands inside the FOMC blackout** (blackout opens the second Saturday before, 9/5) ⇒ **no Fed speaker can re-anchor the market between the last major print and the decision.** That is a vol-positive structural detail: the market must carry CPI risk for three sessions with the Fed silent.

---

## 4. THE REGISTERED LEGS

### LEG 1 — 🔑 the differentiated call: **the expiry-day crush is SUPPRESSED**

> **CLAIM:** ΔVIX from the **9/15 close** to the **9/16 close** will be **shallower than −3.66%** (the measured September/VIX≤16 median), because the expiring contract carries no event and the event premium sits in October.

- **CONFIRM:** Δ > −3.66%
- **KILL:** Δ ≤ −3.66% — the crush arrives on schedule and the split-timing mechanism is not doing what I claim.
- **NOT-GRADED (declared in advance):** if VIX > 16.00 at the 9/15 close, the conditioning cohort does not apply and this leg is **void, not failed.**
- **Why this is a real test:** 7 of 8 cohort rows fell, median −3.66% ⇒ "shallower than the median" is **≈50/50 by construction.** It is not a gimme and it cannot be satisfied by the modal outcome.
- **Instrument:** `^VIX` daily close, yfinance history, **gap-checked against CBOE** per today's KB-VIO-215 ruling.

### LEG 2 — the post-expiry lift

> **CLAIM:** ΔVIX from the **9/16 close** to the **9/23 close** (+5 sessions) is **positive**.

- Base rate: 88% up (7/8), median **+7.30%**, p10 **−1.41%**.
- **CONFIRM:** Δ > 0 · **KILL:** Δ < **−1.41%** (through the measured p10) · **INCONCLUSIVE:** −1.41% ≤ Δ ≤ 0.
- ⚠️ Registered explicitly as **under-powered** (§2). A hit is weak evidence; a miss through p10 is the informative outcome.

### LEG 3 — the branch map: what the surface should do, by outcome

Graded on the **9/16 close** and the **9/18 close** (T+2, so the presser is digested).

| branch | what it is | VIX3M/VIX | VVIX | MOVE | my prior |
|---|---|---|---|---|---|
| **A · HIKE 25bp** | the dots followed through | **compresses < 1.10** | **> 95** | **> 82** | ~0.45 |
| **B · HOLD, dots keep a 2026 hike** | modal "nothing resolves" | **re-steepens > 1.20 by 9/18** | stays **< 92** | stays **> 75** | ~0.40 |
| **C · HOLD, dots retreat** | dovish surprise | **> 1.25** | **< 82** | **< 72** | ~0.15 |

- 🔑 **The discriminator that matters is NOT the VIX level — it is WHERE the vol shows up.** Branch A is a **rates-led** vol event (MOVE leads, VVIX confirms, equity vol follows late); branch C is an **equity-vol crush** with rates leading the relief. **A read that watches only VIX will grade A and B the same.**
- **CONFIRM a branch** if ≥2 of its 3 cells hold at 9/18. **NULL:** if no branch gets 2-of-3, the map is wrong and I say so — the map is falsifiable as a whole, not just leg-by-leg.
- ⛔ **Priors are stated so I cannot re-weight after the fact. They are not tradeable and no size attaches to them.**

### LEG 4 — the standing divergence this letter is really about

> **CLAIM:** rates vol has been leading equity vol since 8/26 and will still be leading at 9/16.

**MOVE 69.44 [8/26] → 77.88 [9/1] = +12.2%**, through F1 (72.41) and confirm-3 (75.50), while **VIX went 14.70 [8/27] → 15.20 [9/2] = +3.4%.**
- **CONFIRM:** MOVE % change 8/26 → 9/16 exceeds VIX % change 8/27 → 9/16.
- **KILL:** equity vol out-runs rates vol into the event.
- **Why it matters:** if the September risk is a *policy* event, it belongs in rates vol first. **A hike scare that never reaches MOVE is not a hike scare.**

---

## 5. ⚠️ OPERATIONAL TRAP — my own contango series breaks basis on 9/16, and it would have fooled me

`workbook/VX_DAILY.tsv` carries `m1_symbol` / `m2_symbol` / `m1m2_adj_pct`. Today: **VX/U6 : VX/V6**.

**VX/U6 expires 9/16.** From the 9/16 row onward the pair is **VX/V6 : VX/X6**.

> ⛔ **The 9/15 → 9/16 change in `m1m2_adj_pct` measures A CONTRACT ROLL, NOT A MARKET MOVE.** Do not read it as a term-structure change. To measure the real move across the roll, compare **VX/V6 : VX/X6 on 9/16 against VX/V6 : VX/X6 on 9/15** — both pairs are quoted on both days; the ledger simply only stores the front pair.

Pre-registered so that the September contango print is not graded against a September/October pair it is not comparable to. `[[finding_derived_metric_across_vintages_biases_toward_stale_leg]]` · `[[finding_window_start_at_an_extremum_inverts_the_move]]`

---

## 6. DECLARED WEAKNESSES — stated now, so they cannot be discovered later as excuses

1. **n=8 / post-2018 n=3.** F2 unrunnable. §2. **This is the letter's biggest weakness and it is the first thing listed.**
2. **MOVE basis unreconciled.** Mine: **77.88 [9/1]**, investing.com PRIMARY, my `workbook/MOVE.tsv`, flagged stale (9/2 not yet posted at boot). My spawn brief carries **79.71 [9/2]** from another surface. **I have NOT adopted the brief's figure** — MOVE is my metric and one source of truth governs. Both are quoted with their basis; the gap is 1.83 and unexplained. **Grade LEG 3/4's MOVE cells on `workbook/MOVE.tsv`.**
3. **The gamma board is UNMEASURED since the 8/21 OPEX** (HENRY-owned; HENRY spawned in parallel tonight). A 9/16 triple-witching-adjacent expiry with unmeasured dealer gamma is a real blind spot. **I have not re-derived it and I do not own it** — cite HENRY when it lands, or say "unmeasured."
4. **No FOMC-date base rate.** I measured VIX-expiry behaviour, which I could derive exactly, and **deliberately did not measure FOMC-day behaviour, because I would have had to guess historical FOMC dates.** The base rate in §2 is therefore about **expiries**, not about **FOMCs**, and it is silent on how often the two coincide. **Named rather than papered over.** `[[finding_hypothesis_needs_an_instrument_for_its_defining_mechanism]]`
5. **Branch priors are judgment, anchored on one market price** (Kalshi 0.48, 8/28 settled). Not a measured distribution.
6. **The cheap-tail window is OPEN 4/4 into a double catalyst** (CPI 9/11, FOMC 9/16). ⛔ **I make NO proposal.** `cheap_tail.py` is an operator-decision surface whose own route is PROME → TERRY → Will; no gate has fired; **root rule #5 and the spawn constraint both bind.** Recorded as live, not actioned.

---

## 7. GRADE CARD (fill at the 9/16 and 9/23 closes — do not improvise the criteria)

| leg | criterion | grade | note |
|---|---|---|---|
| 1 · crush suppressed | ΔVIX 9/15→9/16 **> −3.66%** (void if VIX>16 on 9/15) | ☐ | |
| 2 · post-expiry lift | ΔVIX 9/16→9/23 **> 0** (KILL < −1.41%) | ☐ | |
| 3 · branch map | ≥2-of-3 cells for exactly one branch at 9/18 | ☐ | branch: ___ |
| 4 · rates leads equity | MOVE %Δ (8/26→9/16) **>** VIX %Δ (8/27→9/16) | ☐ | |
| 5 · basis guard held | contango roll not misread across 9/15→9/16 | ☐ | process leg |

**Resolver anchor type:** LEG 1/2/4 anchor on **scheduled market closes** (dates certain, cannot slip). LEG 3 anchors on the **FOMC statement**, a scheduled-event anchor — if the meeting moves, legs 1/2/4 still grade and **leg 3 voids rather than slipping.** `[[finding_resolver_anchored_to_expected_event_inherits_slip_risk]]`

---

*Frozen 2026-09-02. Author: VIOLET. Registered in `workbook/KB.tsv` as KB-VIO-216 (letter) / KB-VIO-217 (expiry base rate) / KB-VIO-218 (roll basis break). Routed to PROME for the DOCKET/GATES coordination layer — **as a READ, explicitly not as a gate row** — so that a graded outcome cannot fire into a dark coordination layer (KB-VIO-110 class).*
