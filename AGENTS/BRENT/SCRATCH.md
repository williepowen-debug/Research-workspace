# BRENT SCRATCH — Fri Jul 31, 2026 ~4:00 PM ET · **FULL CLOSEOUT** (diesel decree graded · Stage-A v3→v5 across three rulings · two boot/closeout audits · COT + Baker Hughes graded · 5 ruled implementations shipped)

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

---

## ⏳ FIRST THING NEXT SESSION

**0. ✅ BOTH FRIDAY PRINTS ARE GRADED AND CLOSED — NOTHING OWED, NOTHING STACKING.**
   - **COT as-of 7/28 = FUEL SPENT.** Shorts 129,072 (7/7) → 101,016, cumulative **−28,056** (SPENT band ≤−25,000); **WoW −22,474**, the cycle's largest single-week cover. Net 63,979 → 92,943, driver **short-covering**. Raw `f_disagg.txt`; ICE sibling corroborates (−5,015). ⚠️ **78.3% of gross shorts still stand** — "SPENT" = the accelerant fired, not the short is gone. **⇒ off-ramp sizing modifier: fuller-size branch LIVE (size-if-fired ONLY).**
   - **Baker Hughes 451 (+1), NOT a breach, 6 to 457.** BRT-26 **OPEN**, window end-Q3. Confidence held **~58%**, not re-marked off one print.
   - 🔴 **NEXT COT = as-of 8/4, released Fri 8/7. DO NOT let it stack — 7/28 is closed.**

**1. ⏳ ARM CLOCK: 11 of 20 td used at 7/31. LAST DEPLOYABLE SESSION = THU 2026-08-13** (9 sessions left after today: 8/3,4,5,6,7,10,11,12,13). **Leg (a) NOT MET** — peak **68.97 (7/23) close basis, Will-ruled**; needs **OVX ≤58.62**; last 65.60 = **−4.89%**, and moving AWAY from met (OVX rose +3.4% while Brent rose +2.3%). ⚠️ **RE-DERIVE THE PEAK EVERY SESSION — never carry 58.62 as a constant.**

**2. 🔴 Sun 8/2 — OPEC+**: +188 kb/d Sept expected; watch the reported **Oct-Dec pause**. LESSONS #10: paper ≠ physical.

**3. 🟠 Wed 8/5 — EIA wk-7/31**, first volume print overlapping the gasoline-crack move. **Pre-register BEFORE the print, with the premise's SOURCE-GRADE stated inside it.** No BRT-29 grade (LESSONS #9).

## ★ THE SESSION IN TWO LINES

**Market:** the Russian diesel ban **did not lapse — it was extended and permanently split by channel**, which is the opposite of the bearish impulse I pre-registered. **Process:** I got the decree call wrong by grading a policy outcome off a minister's forward guidance, and then found that **two of my own 7/30 artifacts don't survive re-derivation.**

## CHANGES SINCE LAST SESSION

- **⛔ DIESEL DECREE — MY REGISTERED LAPSE BASE CASE FAILED.** Signed decree (announced Thu 7/30): ban runs **Aug 1 2026 → Jan 31 2027**; **diesel/marine/gasoil restricted through Aug 31**; from **Sept 1 the lift applies ONLY to PRODUCERS exporting directly** (*"refineries, rather than retailers"*) — **non-producer/trader diesel stays banned to Jan 31 2027**; **gasoline all-participants to Jan 31 2027** (supersedes the "Dec 31 2026" Novak figure I carried). 4 named outlets, 2 fetched in full. ⚠️ **Russian primary NOT reached — decree number + signature date UNVERIFIED.**
- **📈 Tape:** Brent **$90.11 (+2.34%)** back above $90, still −10.5% below the peak; WTI $85.18; USO $129.81; OVX **65.60 (+3.39%)**; VIX 18.01. ⚠️ All **session-in-progress at 10:18 AM**, not closes.
- **🌊 Rhine barge freight at an ALL-TIME HIGH** ~€160/t, +~400% in two months, **in July with low-water season still ahead** [WALTER SIG-011]. Consumed **NOTED**: a delivered-cost/logistics leg on European diesel, **NOT a supply leg** — do not fuse it into the crack thesis.

## WHAT I DID

**⛔ GRADED THE DECREE AGAINST THE FROZEN PRE-REG AND RECORDED THE MISS.** Root cause: **I graded a POLICY OUTCOME off a MINISTER'S FORWARD GUIDANCE (Novak 7/25-27) instead of the INSTRUMENT.** An on-record intention is not the legal act. *The unattributed CGTN counter I declined to carry was directionally right — declining it was still correct on one body-less claimant; the fix is to register such calls as **PENDING THE INSTRUMENT**, not resolved by the guidance.*
> **★ My pre-registered second-order read is UNTOUCHED and now untestable for a month** — *"the ban exists BECAUSE refining is down; the binding constraint is CAPACITY, not policy."* Earliest test = **producer-direct loadings from Sept 1**. Catalyst rows registered for **9/1** and **2027-01-31**.

**⏳ ARM CLOCK RE-COUNTED FROM `~8/13` TO AN EXACT 8/13**, with the trading-day list written out so it is auditable, and **leg (a) graded on BOTH readings of an ambiguity I found in the spec** (close vs intraday-high peak basis — unstated). **Both unmet, so nothing turned on it — but it must be ruled before it can bind.**

**⚑ STAGE-A SELF-AUDIT — TWO DEFECTS IN MY OWN 7/30 WORK, FOUND BY RE-DERIVING INSTEAD OF INHERITING:**
1. **The analogue table's TANKER figures DO NOT REPRODUCE** (dividend adjustment ruled out — `auto_adjust` True/False identical). **The CRUDE figures from the same audit reproduce EXACTLY** (+8.96%/−2.07%), so the defect is confined to the half I built the conclusion on. **⇒ "blocked 2 of 2" RETIRED AS UNVERIFIED** (re-derived day 0 = 1-of-2). **The replacement case is unaffected** — it rests on structural defects. Corrected in TRADE.md **and** LESSONS_INDEX.tsv.
2. **My own proposed dispersion fix had a DEAD BAND** — `1%<|move|<3%` unspecified in both directions, which is **the most likely outcome (44.9% unconditional, 34.6% given Brent ≤−3%)**. The **BRT-12 "no NEITHER branch" defect, reproduced inside the fix for a defect of the same family.**
3. **🔑 New fact:** on **Jun-17 — the one analogue where a crude short made money — single-name STNG (−0.61%) BLOCKS inside the ±1% band while the 3-name composite (1.63%) PASSES.** The composite is load-bearing.
> **Frozen replacement proposed:** **Leg T** binary liveness veto (BLOCK iff `max(|STNG|,|FRO|,|DHT|) ≤1.0%`; blocks 5.8% of Brent≤−3% days, n=749/3y) **PAIRED NON-NEGOTIABLY** with **Leg C** crude 2-day follow-through (BLOCK if cum Brent ≥0%; **2-for-2**, robust −2% to +8%). ⛔ **Approving the tanker half alone is a NET LOOSENING** — Leg T passes both analogues, so it removes the only thing that blocked Apr-17 (+19.7%, would have destroyed a short).

**⛔ REFUSED A MIS-SPECIFIED TASK RATHER THAN COMPLY:** PROME's packet said BRT-26 was "due today." **It is not** — registered window is **end-Q3 2026**; boot's predictions-due scan ran clean; and Baker Hughes doesn't post until 1 PM anyway. **A grade forced to a wrong date corrupts the calibration record.** Flagged back.

**📬 NEXUS ping — NOT owed.** The correction packet was **already delivered 7/28** and sits **unprocessed** in `AGENTS/NEXUS/inbox/`. NEXUS_BRIEF is currently accurate. **Did not send a duplicate** — the open loop is on NEXUS's side.

## NEXT SESSION (dated, future-verifiable)

1. ✅ **DONE — both 7/31 prints graded and closed** (COT = FUEL SPENT · rigs 451, no breach). **Next COT as-of 8/4, released 8/7 — do not stack.**
2. 🔴 **Sun 8/2 — OPEC+.**
3. 🟠 **Wed 8/5 — EIA wk-7/31**, first volume print overlapping the gasoline-crack move. **Pre-register BEFORE the print, and state the premise's SOURCE-GRADE inside it.** No BRT-29 grade (LESSONS #9).
4. 🟠 **~8/12 FALCON co-belligerency falsifier + July CPI · 8/13 ARM EXPIRY (hard) · ~8/15 Jazan restart.**
5. 🟠 **Carry the TTF softening to SAM + HAWK** — still owed, 5th session. **And now pair it with the Rhine freight datum** (both European gas/diesel channel-cost, both cutting against the simple "LNG is the war's real supply loss" line).
6. 🟠 **Register BRT-16 / BRT-21 successors FORWARD** (disambiguated premise; P(trigger) separate from P(consequence|trigger)). **Unrushed.**
7. 🟡 **Branch-2 partial-execution rung** — 5th session owed. FALCON verified −23%/−32%, sitting exactly between my rungs.
8. 🟡 **Resolve HOW the 7/30 tanker figures were produced** — I can show they don't reproduce, not yet why.

## OPEN THREADS / WATCHES

- ✅ **OFF-RAMP ENTRY IS NOW FUNCTIONAL END-TO-END — three Will rulings today closed all three entry defects.** **Stage-A v5 = {(i) signature AND (T) tanker liveness AND (C) crude 2-day follow-through}**; the transit test moved to the **kill test as leg 2** (physical), beside the institutional leg — **either failing cuts.** **Sizing half/half; H1 announcement-anchored, both tranches out by day+9.** **Jun-17 now FIRES (+10.37%); Apr-17 still BLOCKS twice over.**
  - ⚠️ **STILL OPEN by prior ruling:** the un-anchored *"war-risk halves"* threshold (candidate replacement: an absolute *"below 2.5% of hull"*, frozen, no percentile).
  - 🔴 **AND THE LIMIT THAT MUST TRAVEL WITH THE SPEC:** this regime has produced **ZERO genuine physical reopenings**, so real-vs-fake is **UNCALIBRATED** — **v5 is optimised against a PROFITABLE TRADE, not a VERIFIED REOPENING (n=2).** Do not delete that sentence from `TRADE.md`.
- 🔴 **The closure is OVER-DETERMINED — 4 layers.** Mines (③) and the US blockade (④) survive; SIG-005 (NCC GHAZAL turned back) is fresh evidence ④ is actively enforced. P(transit recovery >50%, 10+d, no signature, 30d) ≈ **15-20%** [FALCON judgment, labelled].
- 🔴 **NEGATIVE CONTROL registered:** transit recovery **with war-risk still 7.5-10%** is NOT normalisation. Must not fire Stage A-bis.
- 🟠 **Diesel crack: thesis stronger, entry worse.** 99.2nd %ile, desks publicly long, TERRY's crowding objection **UNREPAIRED**, card = **`NO AT THIS PRICE`**. The decree strengthens the supply leg; it does not fix the entry.
- ⚠️ **DATELINE remains the failure mode**, not source grade — three institutional-grade false-fires in three days (Apr-2026 Petroline · Sept-2019 Abqaiq · Jun-2026 UKMTO "strait now open").
- 🟡 Flows-vs-inventories shut-in gap · MRPL re-contracting falsifier.

## POSITION DECISIONS PENDING

- **USO Sep-18 150/165 spread — HOLD, no action.** USO $129.81; **no spread mark taken, deliberately** — the 165C leg is thin and a screen mid would be fiction (root rule #4). ⚠️ **FORGE reconcile on the fill price STILL OWED from Will** (since 7/24).
- **Convex MAIN arm — ARMED, no capital, 9 sessions left on the 8/13 clock.** Leg (a) unmet both bases.
- **Off-ramp — ARMED-PASSIVE, entry knowingly defective.**
- **TERRY diesel card — `NO AT THIS PRICE`.**
- **XLE $65C Sep-30 = LAPSE.**

## MAIL STATE

- **Inbox ZERO both lanes** (1 WALTER signal consumed → 1 `board_log` row → 1 `git mv`, **reconciled 1:1**). **Outbox: 2 written today**, both to PROME (Stage-A proposal · Friday-stack delivery).
- **Owed BY me:** TTF softening + Rhine datum → **SAM, HAWK** · one-line loop-closure to **FALCON** on the GATE-2 answer.
- **Owed TO me:** NEXUS to drain its inbox (my 7/28 correction packet still unprocessed) · Will's FORGE fill-price reconcile · Will's Stage-A ruling.

## WORKBOOK HEALTH

- **LIVE:** STATUS (**242 lines**, under cap) · TRADE · THESIS v5.2 + CHANGELOG · NEXUS_BRIEF · CATALYSTS (**16 rows**, diesel row RESOLVED + 9/1 and 2027-01-31 added) · INCIDENTS · PREDICTIONS (**no resolutions; 7/31 header note added**) · LESSONS_INDEX (**L19 evidence note corrected**) · board_log (**108 rows**) · SCRATCH.
- **FROZEN (correct, all banner-verified 7/31):** `workbook/`KB · VX · FLOW · GROUP_MAP — **4 files, not 5.** ⛔ **`workbook/TIMELINE.tsv` DOES NOT EXIST and never did** *(audit flag F8, fixed 7/31 — this line had listed a phantom file as "correctly frozen," i.e. a health report asserting the state of something it never checked)*. The real artifact is **`thesis/TIMELINE.md`**, which is separately and correctly **FROZEN 2026-07-01 (superseded, last maintained Apr-16)**.
- **Boot kit: 5 scripts, all green.** Lesson-conflict check reports **2 UNRESOLVED `entry_timing` contradictions (L11↔L18, L16↔L18) — KNOWN and deliberately open** pending a Stage-A entry ruling.
- **GIT:** own-dir pathspec commits + safe-push. ⚠️ **VIOLET has uncommitted `fred_cache` CSVs in the tree — NOT mine, not swept.** Origin was at parity at boot (0/0), so no pull was needed or attempted.
