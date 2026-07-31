# BRENT SCRATCH — Thu Jul 30, 2026 ~7:25 PM ET · **CLOSEOUT** (long session: THESIS v5.2 molecule split · DEPLOY GATE v2 ratified · off-ramp harvest+tenor ratified · lesson-conflict check BUILT · predictions swept · 7 late packets consumed)

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

---

## ⏳ FIRST THING NEXT SESSION

**0. 🔴 FRIDAY 7/31 IS A THREE-EVENT DAY. Run closeout step 7a; grade off raw `f_disagg.txt`, not Socrata alone.**
   - **CFTC COT as-of 7/28** — THE print that finally sees BOTH the $100.69 high and the −18.1% crash. Ladder from **123,490**. ⚠️ **Do NOT let it stack with 8/7.**
   - **Baker Hughes** — does the −2 extend or reverse off **450**? (BRT-26, frozen line 457.)
   - **Russia diesel decree expiry.** ✅ **GRADER SPLIT CONFIRMED with TERRY: I grade the MECHANISM leg (LOADINGS — base 234 kb/d Jul 1-10 vs 400 June vs ~817 2025-avg) · TERRY grades the CARD CONSEQUENCE · NEITHER of us grades the decree.**
   - ⚠️⚠️ **TERRY CORRECTED MY OWN FRAMING — ADOPTED: 7/31 IS NOT A RESOLVER, IT IS THE START OF THE OBSERVATION WINDOW.** If only loadings grade the leg and loadings take 2-3 weeks, the tradeable information lands **mid-to-late August**. My packet said "grade on loadings" and then described a one-day wait; **both could not be true and I did not notice.** Do not expect resolution tomorrow.

**1. ⏳ THE CONVEX ARM IS ON A CLOCK IT NEVER HAD — check leg (a) EVERY session.** DEPLOY GATE v2 (Will, Option A): **OVX ≤ −15% off the post-arm running peak.** Peak **68.97** ⇒ fires at **OVX ≤ 58.62**; last read 63.46 = **−8.0%, NOT MET.** **10 of 20 trading days used — ARM EXPIRES ~2026-08-13** un-deployed, then needs a FRESH Tier-1/Tier-2 event. ⚠️ **The peak RE-RATCHETS — re-derive it from the arming date each session; never carry 58.62 as a constant.** *(PROME holds an independent backstop row at 8/13.)*

**2. 🔴 Sun 8/2 — OPEC+**: +188 kb/d Sept expected; watch for the reported **Oct-Dec pause**. LESSONS #10: paper ≠ physical.

---

## ★ THE SESSION IN TWO LINES

**Market:** the war's shape is a **MOLECULE SPLIT** — product and gas take confirmed damage across three theaters while crude keeps escaping it. **Process:** four spec defects and five prediction defects shared one root — **specs written without ever asking whether they could fire** — and that root now has a mechanical check.

## CHANGES SINCE LAST SESSION

- **🔴 War resumed hard, oil gates untouched.** CENTCOM "heavy wave" 7/29; Iran launching **daily**; **Kuwait hit 7/30, one worker killed = the exchange's FIRST FATALITY.** Target set military/maritime ⇒ **FAL-01 + GATE 2 unfired.**
- **🆕 FIRST MEDITERRANEAN STRIKE** — drone on the **US-owned LNG FSRU *Energos Winter*, Damietta**, spread to *GasLog Salem*; UNCLAIMED. Logged **RF-043**. ⚠️ **IMPORT/regas infrastructure — NOT an Egyptian LNG export event; do not let it be written up as one.**
- **📈 Tape:** Brent settled **$90.74 (+7.91%) 7/29**, ~**$89.2-89.8 intraday 7/30**, still **−11.4%** below the $100.69 peak. Wires ranged **$87.30-$92.65** today — never cite a single 7/30 print.
- **⛽ Diesel is the violent leg at the pump too:** retail **$5.339/gal, +42.8% YoY** vs gasoline $4.098 **+30.5%** [AAA 7/30].

## WHAT I DID

**★ THESIS → v5.2 — THE DISCRIMINATOR IS MOLECULE-SCOPED.** *"Premium, zero barrels offline"* was only ever true of **CRUDE**. CRUDE = premium (Petroline operational, Aramco confirms no loading impact) · **LNG = supply-loss since 3/24** · **REFINED PRODUCT = supply-loss since 7/27, now in THREE theaters** (Jazan 400 kb/d shut · Perm + Ryazan · Damietta FSRU). Scoping from FALCON, phrasing HAWK's — **the second/third theaters and the mechanism are mine.** Mechanism: a refinery hit **frees feedstock for export** ⇒ crude-bearish / product-bullish.

**✅ EIA PRIMARY RE-CONFIRMED — two relayed figures WRONG.** Raw `urllib`, independent of both my script and PROME's. **Cushing 18.60M (−771K)**, not 19.10M. **Gasoline demand −0.25% YoY, not +0.7% — SIGN BACKWARDS.** **Utilisation 97.2% = a real PRINT**, not my `~96% [EST]`. Relay was **exact** on crude and SPR — *a source right on the front page buys credibility it spends in the back.*
> **🔻 And the retraction was the wrong half:** I had killed my own gasoline-crack demand tell on that bad figure. **Re-graded: unconfirmed but NO LONGER CONTRADICTED.** *A self-correction is an assertion too — verify the number that makes you RETRACT.*

**★ THE BARREL IS SPLITTING, volume-confirmed both halves:** distillate demand **+4.74% YoY** vs gasoline **−0.25%**; diesel crack **$99.08 (7/29) = fresh 6-mo high, 99.2nd %ile**; **US distillate stocks BUILT +1.06M at 97.2% runs** ⇒ **the marginal barrel clears OFFSHORE.** Supply leg found: **Russia's outright diesel export ban cut loadings to 234 kb/d vs ~817 2025-avg.**

**⚑ TWO WILL RULINGS IMPLEMENTED:**
- **DEPLOY GATE v2 (Option A)** — sequenced, not simultaneous. Old `{2.89 / 44.2}` **retired in full and swept from every live surface.** ⛔ **My escalation was FALSE**: the gate fired **50.4%** of the prior year. Real defect: it and the arm trigger were **mutually exclusive by construction — open on 0 of 38 escalation days.**
- **OFF-RAMP HARVEST + TENOR (Option B)** — tenor **60-90 → 21-35 DTE**; **H1** hard stop 8 sessions after entry · **H2** ≥half at −7% · **H3** exit on any close above entry. *The one historical case was **won by day 9 and lost by being held**.* **Entry defects left KNOWINGLY OPEN by the ruling and labelled as such.**

**⚖️ STRUCTURAL FIX BUILT — `scripts/lessons_check.py` + `workbook/LESSONS_INDEX.tsv`.** Lessons now carry machine-comparable `asserts`; a contradiction = same key, different value. **Wired INTO `boot.py`** (0.0s), not just documented. **Found an L16↔L18 conflict my manual audit missed** ⇒ L18 is **outvoted 2-to-1** on entry timing.

**🔎 PREDICTIONS SWEEP — of 7 OPEN, only 2 clean.** **BRT-17 + BRT-21 → STUCK** (excluded from any tally) · **BRT-16** ambiguous premise · **BRT-07** threshold below my own thesis floor · **BRT-12** no "neither" branch. **Claims and confidences UNCHANGED — retro-editing either is a calibration sin.**

**📬 7 LATE PACKETS CONSUMED AT CLOSEOUT** — caught only because my first inbox check was a **false clean** (ran `ls inbox/` from repo root; the path silently resolved to nothing).

## 🔴 CORRECTIONS I MADE TO MYSELF TODAY (5)

1. **Routing regression, mine:** I delivered **both** PROME packets to **`AGENTS/PROME/inbox/` — a DEAD path** (PROME is top-level: **`PROME/inbox/`**). They sat ~3h unseen. **Nothing errors — the write succeeds and the packet is never read.** Durable fix written into my CLAUDE.md: a delivery-path table + *"the recipient's inbox must ALREADY EXIST."*
2. **Over-retracted** the gasoline-crack tell on a bad relay figure (above).
3. **"Gasoline crack −$10.89 in ONE session"** was an intraday read that did not hold — the 7/29 close was **$58.25**.
4. **"Unfireable gate"** escalation to Will — **false**, retracted on the record.
5. **The 7/31 one-day-wait framing** — incoherent with my own loadings standard; TERRY caught it.

## NEXT SESSION (dated, future-verifiable)

1. 🔴 **Fri 7/31** — COT + Baker Hughes + **start** the loadings window (not a resolver).
2. 🔴 **Sun 8/2** — OPEC+.
3. 🟠 **Wed 8/5** — EIA wk-7/31, first volume print overlapping the gasoline-crack move. **Pre-register BEFORE the print, and state the premise's SOURCE-GRADE inside it this time.** Still no BRT-29 grade (LESSONS #9).
4. 🟠 **~8/12 FALCON co-belligerency falsifier + July CPI · ~8/13 arm expiry · ~8/15 Jazan restart.**
5. 🟠 **TTF — a first number arrived and it CUTS AGAINST ME.** **€59.25/MWh, −2.17% on the day**: above HANS's >€50 line but **no upward repricing on three degraded channels.** ⇒ **materially softens the LNG-as-the-war's-real-supply-loss line I carry to SAM and HAWK — carry the softening to them.** ⚠️ One secondary number; **my primary pull (TTF front-month + EU storage) supersedes it.** Question stays OPEN with a number attached.
6. 🟠 **Register BRT-16 / BRT-21 successors FORWARD** (disambiguated premise; P(trigger) stated separately from P(consequence|trigger)). **Do this unrushed — the originals got written in a hurry and that is why they are defective.**
7. 🟡 **Branch-2 partial-execution rung** — 4th session owed. FALCON verified −23%/−32%, which sits exactly between my rungs.

## OPEN THREADS / WATCHES

- 🔴 **Off-ramp ENTRY defects remain open BY WILL'S RULING** (Option B was harvest+tenor only). **⚠️ And FALCON's answer materially IMPROVED the A/C design AFTER the ruling** — recorded as an addendum to the Stage-A-v3 proposal: the anchor is **NOT** transit-only but a **JWC/Lloyd's revision or P&I re-entry** (dated, published, institutional, **non-sovereign**), because **war-risk premium LEADS and transit count LAGS.** **If A/C is ever revisited, revisit THAT version.**
- 🔴 **The closure is OVER-DETERMINED — 4 layers, the 7/29 wave hit only ONE.** Mines (③) and the **US blockade** (④) survive; **SIG-005 (NCC GHAZAL turned back) is fresh evidence ④ is still actively enforced.** P(transit recovery >50%, 10+d, no signature, 30d) ≈ **15-20%** [FALCON judgment, labelled].
- 🔴 **NEGATIVE CONTROL registered:** transit recovery **with war-risk still 7.5-10%** is **NOT** normalisation — escorted convoys / risk-tolerant operators. **Must not fire Stage A-bis.**
- ⚠️ **THIRD institutional-grade DATELINE false-fire in three days** — Apr-2026 Petroline · Sept-2019 Abqaiq · **Jun-2026 UKMTO "strait now open"** (ranks high in July search; blockade resumed 14 July). **The failure mode is not source grade, it is DATELINE.**
- 🟠 **"War-risk halves" still names NO anchor** — threshold-strength, deliberately unruled.
- 🟡 **Flows-vs-inventories shut-in gap** · **MRPL re-contracting falsifier** (no 2nd Indian adopter in 3-4wks ⇒ one cautious buyer).

## POSITION DECISIONS PENDING

- **USO Sep-18 150/165 spread — HOLD, no action.** Needs **+17.3%** to the $150 strike (was +24.5% on 7/28), **+19.6%** to BE ~$153, **50 DTE**, USO ~$127.9. **No spread mark taken, deliberately** — the 165C leg is thin and a screen mid would be fiction (rule #4). ⚠️ **FORGE reconcile on the fill price STILL OWED from Will.**
- **Convex MAIN arm — ARMED, no capital, ON THE 8/13 CLOCK** (leg (a) needs OVX ≤58.62; not met).
- **Off-ramp — ARMED-PASSIVE.** Harvest+tenor ratified; **entry knowingly defective. NOT functional end-to-end.**
- **TERRY diesel card — `NO AT THIS PRICE`** (reached on live marks before my packet). Thesis stronger, **entry worse**: 99.2nd %ile, crowding unrepaired, and the real wait is **~3 weeks**.
- **XLE $65C Sep-30 = LAPSE.**

## MAIL STATE

- **Inbox ZERO both lanes · Outbox ZERO.** 7 consumed → 7 `board_log` rows → 7 `git mv`'d (**reconciled 7:7**); 1 outbox packet swept to `delivered/` (loop closed — Will ruled Option A).
- **Sent today (7):** PROME ×2 *(to the dead path — migrated by PROME)* · FALCON · HAWK · OSPREY · TERRY ×2.
- **Owed BY me:** carry the **TTF softening** to SAM + HAWK · a **one-line loop-closure to FALCON** on the GATE-2 answer (they said none owed, but the item-3 ask was mine).

## WORKBOOK HEALTH

- **LIVE:** STATUS (**240 lines**, under cap) · TRADE · THESIS **v5.2** + CHANGELOG · NEXUS_BRIEF · CATALYSTS (14 rows) · INCIDENTS (**RF-043**) · PREDICTIONS (**swept**) · **LESSONS_INDEX.tsv (21/21)** · board_log (**106 rows**) · SCRATCH.
- **FROZEN (correct):** KB · VX · FLOW · GROUP_MAP · TIMELINE.
- **Boot kit: 5 scripts, all green** — thresholds · EIA · catalysts · predictions-due · **lesson-conflict (new)**.
- ⚠️ **Known soft spot:** `LESSONS_INDEX.tsv` asserts were encoded by me in one pass. **A mis-encoded lesson is as invisible to the check as an unindexed one.** Worth a DAEDALUS/YEYOU audit.
- **GIT:** own-dir pathspec commits + packets under carve-out ① + memory under ③ + safe-push. ⚠️ **Other agents committed concurrently all session** (VIOLET, DAEDALUS, TERRY, WALTER, FALCON, PROME) — path-scoped commits held, nothing foreign swept.
