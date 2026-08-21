# BRENT SCRATCH — Fri Aug 21, 2026 **~08:3x ET** *(live session, Will-directed · boot Thu eve → full closeout Fri pre-open · **THE SESSION WHERE THREE "OIL IS ROLLING OVER" STORIES ALL TURNED OUT TO BE MEASUREMENT ERRORS — AND SO DID TWO OF MY OWN CLAIMS***

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

> # 🔴 **THE HEADLINE: NOTHING IN THE OIL TAPE BROKE THIS WEEK. THREE SEPARATE BEARISH READS IN CIRCULATION WERE ARTIFACTS — A CONTRACT ROLL, AN INTRADAY BAR, AND A MISLABELLED INSTRUMENT. CRUDE RAN FIVE STRAIGHT SESSIONS TO ITS HIGHEST CLOSE SINCE 7/24.**
> **⚠️ AND THE SYMMETRY IS THE REAL LESSON: I CAUGHT THREE OF OTHER DESKS' MEASUREMENT ERRORS AND COMMITTED TWO OF MY OWN IN THE SAME SESSION — a live instrument declared dead off ONE WRONG VERB, and duplicate catalyst rows my own boot had already printed to me. BOTH TIMES THE DISCONFIRMING EVIDENCE WAS ALREADY IN MY HAND.**

> # 🔴 **`$0` MOVED. NO POSITION CHANGED. NO GATE FIRED OR UN-FIRED. NO THRESHOLD MOVED. NO PREDICTION RESOLVED.**
> **INBOX 20 → 0 (both lanes) · OUTBOX 0 · board_log 214 → 234 · STATUS 226 → 232 · NEXUS_BRIEF 207 → 103 · CATALYSTS 19 → 12 rows.**

---

## CHANGES SINCE LAST SESSION *(dark 8/17 → 8/20 eve; the 8/19 EIA commit was the autonomous routine, not a session)*

- **Crude re-rated hard and I was not watching:** Brent **8/13 $87.07 → 8/20 $93.28, five straight up sessions, +7.1%** — the **highest close since 7/24** and the first sustained re-approach to the $100 line since the 7/23 fire. USO **$134.54**.
- **The curve did NOT tighten with it.** M1−M3 **+4.46 (8/11) → +4.52 (8/20)** while spot rose **+$4.37** ⇒ **a PARALLEL upward shift. This leg is a LEVEL re-rating, not a prompt-scarcity squeeze** — and that is the discriminator I own.
- **EIA wk-8/14 (pulled 8/19 by the routine):** SPR **293.426M** (−5.27M, 4th straight draw, 43-yr low) · Cushing **21.252M** (−1.31M, **reversed 33% of the rebuild I rescinded Boundary #3 on**) · util **97.2%** (3rd deepening print) · commercial **428.8M** (+4.41M).
- **Rigs moved twice while I was dark and I missed both:** wk-8/7 **454**, wk-8/14 **455**.
- **20 packets arrived** (14 WALTER lane + 6 top-level), including the **SPR-exchange mechanism** finding and **four TERRY packets closing every open position question.**

## WHAT I DID THIS SESSION

### ① THE THREE CORRECTIONS OUTWARD
- **🔴 THE CRACK "COLLAPSE" IS A CONTRACT-ROLL ARTIFACT — packets to WALTER + TERRY.** `CL`, `HO` and `RB` **ALL rolled Sep→Oct on 8/20**. Rolling-front printed **gasoline −$10.71 / diesel −$3.97**; same-contract truth is **Sep −$1.74 / −$0.98, Oct −$0.49 / +$0.03** — and **BOTH September contracts closed UP.** The −$10.71 is **100% the summer→winter RVP grade spread** (Sep−Oct RBOB $10.79/bbl). **Second defect in the same thread: the "record" was 8/18 $101.96, not Monday, so the give-back is −$1.77 and DECELERATING, not −$5.08 accelerating** — the $96.90 was a pre-open bar that did not hold. ✅ **THESIS v5.6 distillate leg INTACT; it would have been written down on an artifact had I not re-derived it.**
- **🔴 THE DATED-BRENT MISLABEL — packet to PROME, blocking HEARTBEAT §1.** **No 8/19 or 8/20 Dated Brent observation exists**; the series lags ~2 sessions, latest **$95.29 [8/18]**. The circulating **"$93.29 dated Brent 8/20" is the FUTURES number mislabelled** — now fleet-wide kill-on-sight. ★ **The tell: $0.01 from the futures close, against a real prompt premium of +$4.27 / +$4.35 / +$11.06.**
- **⚠️ THE SETTLE, WITH ITS LIMIT STATED:** `BZV26` **$93.28** — **single-source, and it REVISED under observation** (93.32 at 19:37 → 93.28 at 19:42, then stable across 3 pulls/20s). **A settled bar cannot move ⇒ daily-bar CLOSE, not a certified settlement. Last unrevised settle: 8/19 $91.62.**

### ② TWO ERRORS OF MY OWN, BOTH CAUGHT BY OTHERS, BOTH ANNOTATED NOT DELETED
- **⛔⛔ I DECLARED A LIVE INSTRUMENT DEAD OFF ONE WRONG VERB.** I ran `fetch.py price DCOILBRENTEU`, got a 404, and published *"the fleet dashboard has NO working Dated-Brent instrument."* **`fetch.py fred DCOILBRENTEU` worked the whole time** — and returns the series **identical to EIA `RBRTE` to the cent across five dates** (they are two mirrors of one series). **PROME refuted it; I verified before accepting; retracted same session.** ★ **I had pulled the identical series from EIA MINUTES EARLIER — two instruments agreeing should have made me suspect my INVOCATION, not the tool. Shipped inside a packet whose entire subject was instrument discipline.** `[[finding_rejecting_an_instrument_is_an_audit_of_it]]`
- **⛔ I NEARLY SHIPPED DUPLICATE CATALYST ROWS** into the forward-state file whose only job is to be the single source of truth — **while my own boot had already printed both existing rows to me in the catalyst countdown.** Caught in the reconcile; duplicates removed, originals **enriched** instead.

### ③ GRADES AND STALE-SURFACE REPAIR — four stale cells in one pass
- **🔴 `BRT-26` GRADED ON TWO STACKED PRINTS** (wk-8/7 **454**, wk-8/14 **455**). **Now 2 from the frozen 457, not 6.** My TRACKER cell carried `451 / 6 away` through two published prints **and I quoted that stale distance to Will at boot.** Graded before the 8/21 print could stack a third. ⚠️ **BH primary timed out AGAIN (http=000) — all aggregators, two per print.**
- **⛔ TRACKER run-time block: FOUR stale cells found in one unconditional pass** — GASREGW (18 days), **COT (TWO vintages: the 8/14 grade never reached the block three cloud routines read)**, rigs (2 prints), and the 9/10/11 crude-basis set. **Three had fresher values already sitting on my own surfaces.** ★ **This is the unconditional-refresh rule I adopted 8/17 doing exactly what it was adopted for — first closeout it was ever exercised.**
- **STATUS price dashboard REBUILT** — it read *"Thu Jul 30"* in live formatting for **21 days**, carrying **OVX wrong by 28%** and a **retired deploy gate as live** → archived with provenance.
- **THESIS: two file defects fixed** — the `**Version:**` field read **5.5** while the title read **v5.6** (8-day two-clock drift on the thesis's own version field), and *"winds down ~Jul 3"* on the SPR line had been wrong for ~7 weeks.

### ④ THE SPR FINDING — thesis-CONFIRMING, and it arrived as someone correcting their own alarm
**~172M bbl DISCRETIONARY EXCHANGE, not a sale. Barrels repaid IN KIND at 1.18–1.24×, 2026-29. Window "primarily April–August 2026" — ENDS THIS MONTH.** ⇒ twelve straight draws are **what a contracted delivery schedule looks like.** ✅✅ **My THESIS has said since v5.0 that the SPR is "a bridge loan over the Hormuz outage, not evidence of scarcity" — written as an inference, before anyone had the contract. That was the literally correct word.** ⚠️ **0.70, specialist-secondary; the DOE primary carries NO 2026 entry at all.** **Falsifier registered, resolves ~9/9.**

### ⑤ MAIL + HYGIENE
**20 packets consumed, BOTH LANES TO ZERO, 20 moves == 20 ledger rows** (board_log 214→234, 5 fields, trailing newline verified — the 8/17 partial-row class avoided). **NEXUS_BRIEF 207 → 103 lines** (~117 lines of dated correction banners archived; FORWARD CATALYSTS pruned of **six fired rows** it had re-accumulated in 11 days after being rebuilt on 8/10 for that exact drift). **CATALYSTS pruned 7 fired rows, +1 new.**

---

## NEXT SESSION (dated, future-verifiable)

1. **🔴 TODAY Fri 8/21 ~15:30 ET — COT VINTAGE #2 (as-of Tue 8/18). FIRST GRADE OF THE SUCCESSOR ON A CLEAN VINTAGE.** Leg A vs deadband **109,165–118,325**; Leg B OI-share ≤ **4.909%** (**GATING**). Ladder from **110,638 / OI 1,892,429 / share 5.8463%**. `cot_grade.py --expect 2026-08-18`; **exit 3 = WAIT, never grade last week's row.** Raw `f_disagg.txt` code **067651**, NOT Socrata; verify `report_date` IN-ROW. ⛔ **`median_unit 9,160` FROZEN.** ⛔ **Incumbent RETIRED — do not re-grade it.**
2. **🟠 TODAY Fri 8/21 ~13:00 ET — BAKER HUGHES. `BRT-26` IS 2 RIGS FROM FAILING.** ⛔ **Grade the OIL count, not the total.** ⛔ **Never a bare digit-regex on BH HTML.** ⚠️ **Primary has failed on every attempt — if it breaches on secondaries alone, SAY SO ON THE GRADE.**
3. **⛔ RE-SPEC FORWARD CHECK ② BEFORE ~8/24 — DO NOT RUN IT AS WRITTEN.** FALCON (`KB-FALCON-102`): the **670 kbpd** figure is **Asia-only + month-scoped**; **2.17 mb/d** is **total weekly liftings.** **As written the Sidi Kerir lag test manufactures a ~70% PHANTOM COLLAPSE.** Re-scope to like-for-like perimeter first.
4. **🔴 `KILL-LEG2-TRANSIT` — RESOLVE OR RE-INSTRUMENT. MINE AS OWNER (PROME item 3, accepted).** The known-positive control I designed **FAILED**: FALCON's Kharg veto printed **0 t / 0 calls for 8/12** on a day a VLCC demonstrably loaded ~2M bbl. **Now three independent legs of impeachment** (my internal 0.0%-vs-16.8% contradiction · a vendor putting ~58% of transits dark · a failed positive control at a second port and second series). **Six instruments give 0/3/5/6/12/zero for the same days.** ⛔ **Re-scoping a falsifier is a WILL GATE — bring a spec, not a fait accompli.**
5. **🟠 JAZAN STRIKE #4 — DEFERRED WITH A REASON, NOW OWED.** WALTER `-006`: a 4th Jazan-class strike claimed 8/18 across three outlets, **every one calling it the THIRD** — somebody is miscounting and fleet tempo framing depends on which. ⛔ **Check HAWK's cross-theater `STRIKES.tsv` FIRST** (`[[project_energy_strike_ledger]]`) — do not fork a parallel per-theater record. **Also: INCIDENTS still 2 events behind on Novorossiysk/Sheskharis and 17 ACTIVE rows past the 60d budget (worst RF-004 at 154d).**
6. **🔴 ~Wed 9/9 — THE SPR EXCHANGE-WINDOW FALSIFIER.** First September-covering EIA prints. **Draw stops/decelerates ⇒ contracted schedule; continues ~5-6M/wk ⇒ emergency-consumption reading partially recovers.** Base **293.426M**. **OPEN ASK: locate the RFP docket / Federal Register notice / DOE release to confirm 172M, the authorization date and the 18–24% premium AT SOURCE.**
7. **🟡 FORWARD CHECK ① — THE YANBU PRINT HAS NO DUE DATE AND MY CLASSIFICATION WAS WRONG.** I logged it PUBLIC-AND-UNPUBLISHED, *"expected ~8/19."* **FALCON `KB-101`: it is a PRESS RELAY, NOT a scheduled release** ⇒ **nothing to be "overdue" against, and absence is evidence about NEWSWORTHINESS, not barrels.** Still unpublished. **Leg-3's grading cadence needs re-specification.**

## OPEN THREADS / WATCHES

- **🔴 THE SESSION'S TRANSFERABLE FINDING: `=F` TICKERS ROLL — fine for a LEVEL, unsafe for a DELTA across a roll window.** Name the contract or state the basis and check the roll. **Danger dates: late Aug (RB Sep→Oct), late Nov, every expiry.** One roll produced a −$10.71 phantom collapse that two desks propagated.
- **⛔ THE SECOND TRANSFERABLE FINDING, AND IT IS ABOUT ME: I was corrected twice in one session, both times by evidence I already held.** The EIA pull that refuted my dead-instrument claim was minutes old; the boot output that showed the existing catalyst rows was on my own screen. **`finding_a_charitable_reading_of_your_work_is_the_one_to_check`.**
- **⚠️ TWICE IN FOUR DAYS AN OUTSIDE DESK CAUGHT A DEFECT IN AN INSTRUMENT I OWN, WHILE MY OWN CHECKS PASSED CLEAN** (FALCON's perimeter save; PROME's rig-staleness catch). **That is a pattern about my check COVERAGE, not about luck.**
- **⛔ FOUR war-risk-relevant events I can name and cannot measure. NO instrument for: freight/war-risk (Worldscale/Baltic — gap now declared FIVE times) · Yanbu tankage · Petroline throughput · SAUDI AGGREGATE EXPORTS (what `R3` actually needs).**
- **⛔ The Yanbu↔Sidi Kerir DOUBLE-COUNT SEAM is still open** — a cargo loading at Yanbu, part-discharging at Ain Sokhna and reloading at Sidi Kerir can appear in BOTH series. **I do not net the two, and neither should anyone citing them.**
- **⛔ Still unresolved:** Petroline **5 vs 7 mb/d** · SPR floor **252.4M vs 400.0** · P5 row-27 width-bias re-spec (must land BEFORE any re-arm) · Shell Q2 deck primary · EIA imports-by-country · global visible-stocks counter.
- **⛔ EXPORT-SIGN WARNING live · RUNS-DECLINE IS NOT CAPACITY-OFFLINE · "UNCHANGED IS NOT REVERSED" (20 nights, no CENTCOM-CONFIRMED strike — NOT a de-escalation call, and the qualifier is load-bearing).**

## POSITION DECISIONS PENDING

- **NONE PENDING ON THE SHARES — WILL RULED HOLD 8/18** ("we will hold USO"): no trim, no hedge, no size reduction, **no exit rule.** ⛔ **A CHOSEN outcome, not a defaulted one — if it gives back, that must NOT be postmortemed as a management failure.** TERRY stops raising it.
- **🟠 THE ONE GENUINELY OPEN LEG: `USO Oct-16 $135C ×2` HAS NO MANAGEMENT RULE, 56 DTE.** **Will's HOLD covered the SHARES ONLY** — TERRY says so explicitly; *"hold" is not a coherent instruction for a dated option.* **`RISK_RULES` #9 violated on that leg; stub OPEN and Will-gated.** Flagged to PROME (adjacent to Will's row 58).
- **★ THE BOOK IS WORKING: 35 USO shares +$443.10 / +10.39%** (basis $121.88, USO $134.54). **5 live oil expressions.** ⛔ **STNG is a TRACKED TICKER, not a holding.**
- **⛔ NO LIVE DEPLOY GATE EXISTS** — v2 retired 7/30, **v3 retired by Will 8/07**. **`TRY-FIRE-006` RETIRED 8/18** on lifecycle/instrument grounds — ⛔ **NOT evidence against the Kharg-strand premise, which is NOT GRADED.**

## MAIL STATE

- **✅ INBOX 0 · WALTER LANE 0 · OUTBOX 0 — all three empty. board_log 234 rows, 5 fields, zero ragged, trailing newline verified.**
- **SENT (3):** → **PROME** (settle of record + the dated-Brent mislabel; **consumed same session, and it refuted my §3 — retraction annotated in place**) · → **WALTER** and → **TERRY** (the contract-roll crack correction).
- **Owed TO me:** **Will** — the war-risk-halves ruling · the WP3 call · the `USO Oct-16 135C` management stub. **DEWEY** — `gie_pull.py`.
