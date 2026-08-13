# BRENT SCRATCH — Wed Aug 12, 2026 **~17:2x ET** *(dedicated live session, PROME-directed)* · **THE SESSION WHERE A PREDICTION MARKET FOUND A ZERO-TRANSIT DAY MY OWN INSTRUMENT MISSED BY ONE ROW — AND THE PRICE STRIP HAD BEEN SAYING IT ALL ALONG**

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

> # 🔴 **`$0` MOVED. NO GATE FIRED (there is no live gate). NO THRESHOLD MOVED OR REGISTERED. NO POSITION CHANGED. NO PREDICTION RESOLVED.**
> **THREE RULINGS LANDED: Routing Boundary #3 RESCINDED · crude instrument-basis canon RULED per surface · 35a ENCODED as REVERT. THESIS → v5.5.**
>
> ## ⛔⛔⛔ **READ THIS BEFORE ANYTHING ELSE: I COMMITTED A 4TH INSTRUMENT-CLASS ERROR *INSIDE* THE RULING THAT BANS IT, AND PROME CAUGHT IT IN VERIFICATION.**
> **I published `Brent $88.61 / WTI $82.88 / M1−M3 +$3.93` labeled "8/12 SETTLES." THEY WERE LIVE BARS.** Captured 16:38–16:55 ET; **ICE Brent trades to 18:00 ET.** PROME pulled $88.37→$88.40 ~8s apart; my 17:07 re-pull moved **every** leg (BZV26 −0.23 · BZX26 −0.19 · BZZ26 −0.35 · CL=F −0.26). **ALL 8/12 FUTURES FIGURES WITHDRAWN — last valid crude settles are 8/11.** 8/12 **equity** closes are fine (16:00 ET close, before my read).
> ✅ **NOTHING SUBSTANTIVE MOVED** — every candidate value leaves M1−M3 backwardated (+3.93/+4.05/+4.46) and WTI−Brent ≈−$5.7, so the basis ruling, the Cushing second witness and the zero-transit finding all stand.
> ⛔⛔ **THE STANDING RULE THIS BUYS, AND IT IS MECHANICAL BECAUSE 4-FOR-4 PROVES A REMEMBERED RULE DOES NOT WORK: NEVER read a futures daily bar as a "close" before that contract's own session end — ICE Brent 18:00 ET · NYMEX WTI 17:00 ET. If you read it earlier it is a PROVISIONAL LIVE BAR and must be labeled AT CAPTURE, not at review. Split every tape by SESSION-END, not by date — equities (16:00 ET) and futures are different clocks and that difference is exactly what bit me four times.**

---

## ✅✅ 35b RULED BY WILL — 2026-08-12 evening, relayed by PROME at session close. **RECORDED HERE BECAUSE A FRESH SESSION BOOTS ON THIS FILE, NOT PROME'S.**

**WILL RULED ALL THREE OF MY RECOMMENDATIONS AS PROPOSED:** **(a)** adopt the successor spec (trailing-8wk-median base · 1.0-median-unit bar · ±0.5 deadband · two-leg agreement) · **(b)** **Leg B GATING**, accepting the 33.6% NO-VERDICT rate · **(c)** **effective AFTER the 8/14 grade.** Full spec → [`setups/2026-08-12_35b-COT-successor-band-N1-build.md`](setups/2026-08-12_35b-COT-successor-band-N1-build.md).

> ### ⛔⛔ **THE 8/14 ORDER OF OPERATIONS IS LOAD-BEARING AND MUST NOT COLLAPSE. DO THESE IN ORDER:**
> **1️⃣ GRADE THE INCUMBENT BAND ONE FINAL TIME** on the Aug-11 vintage under **35a REVERT semantics**, ladder from **102,560**, raw `f_disagg.txt`, code `067651`, `report_date` verified in-row.
> **2️⃣ WRITE THE RE-GRADE DOWN. IT MUST BE WRITTEN, NOT ASSUMED.** ⚠️ **A WoW re-gross of just +1,513 UN-FIRES the fuller-size modifier — P = 47.4% all-history (n=234) / 50.0% last 52wk. Under REVERT it switches off SILENTLY. If nobody writes the grade, the branch's state is simply unknown and TERRY may size off a stale LIVE.**
> **3️⃣ ONLY THEN register the successor.** ⛔ **NEVER run incumbent and successor on the same vintage.**
> *(Order is also on the DOCKET 8/14 row so a fresh session cannot collapse it. If this file and the docket disagree, re-derive from the build file — do not guess.)*

## 📋 TWO SELF-AUDITS RAN 8/12 EVENING — 16 findings total. **DO NOT RE-LITIGATE; DO NOT PRE-EMPT WILL.**

- **Canonical surfaces → [`AUDIT_2026-08-12_self-audit-canonical-surfaces.md`](AUDIT_2026-08-12_self-audit-canonical-surfaces.md)** — 7 findings. **F-1 (fixed):** the 8/7 retraction never reached the derived Brent→USO arithmetic; break-even was understated **$1.67** on a LIVE position. **F-5 (fixed):** 11 dead outbox pointers.
- **INCIDENTS ledger → [`AUDIT_2026-08-12b_INCIDENTS-ledger-sweep.md`](AUDIT_2026-08-12b_INCIDENTS-ledger-sweep.md)** — 9 findings, **ZERO edits by design.** ⛔ **VERDICT TO HONOUR: the ledger is a good EVENT RECORD and is NOT a CAPACITY MEASURE. No aggregate over it is quotable until the schema carries units.**
- ⛔ **WITH WILL, DO NOT PRE-EMPT: F-2 · F-3 · F-4 · F-7 · I-1 · I-2 · I-3 · I-6 · I-7.** PROME is presenting six of them as **ONE convention** (a value whose basis or unit moved while its label stayed still), not nine spec calls. **My "EXTEND `instrument_check.py`, don't build a tenth script" recommendation carried.**
- 🟡 **STILL OPEN, no rush (PROME offered it back):** RF-033's fourth-zero question is **resolved** (documented anti-double-count) — what remains is **I-9**, the `capacity_bpd` column: 7 zeros conflating *wrong-unit* (6) with *unknown* (1, RF-037 KOC), plus 7 blanks.

## ⏳ FIRST THING NEXT SESSION

1. **🔴 THE 8/11 EIA STEO WRITE-BACK — item ①, THE ONE PINNED ITEM I DID NOT DO.** Not blocked; **de-prioritised** against PROME's own ⑥/Cushing/⑦ ordering and I ran out of session. **READ THE 2027 RECOVERY COLUMNS, NOT THE 0.0 TROUGH.** A trough non-move is *"confirmed,"* never *"vindicated."* **~99.6% of the 2027 supply increment is MIDDLE EAST ⇒ EIA's window-closing forecast embeds an un-audited assumption that FALCON's theater de-impairs. If the 2027 path slips, my tenor tolerance rises.** Write back to STATUS/CATALYSTS/TRACKER (my P2 §F carried-work declaration).
2. **🔴 Fri 8/14 — COT as-of 8/11. THE MOST IMPORTANT PRINT OF THE CYCLE, and now for FOUR reasons:** first post-**8/6**-escalation read · first post-**8/8-ADNOC** read · the print that settles the band coin-flip · **and the LAST print the incumbent band ever grades.** **Ladder from 102,560. Raw `f_disagg.txt`, code `067651`, `report_date` verified IN-ROW. ⛔ MUST NOT STACK.** ⚠️ **NEW AND OPERATIVE: under the 35a REVERT encode, a WoW re-gross of just +1,513 UN-FIRES the fuller-size branch — P = 47.4% all-history (n=234) / 50.0% last 52wk. It will switch off SILENTLY unless someone re-grades it. RE-GRADE IT.**
3. **🟠 Fri 8/14 — Baker Hughes.** 451 (7/31), 6 to the frozen 457. ⚠️ **Primary 403-blocked several weeks — if BRT-26 breaches on secondaries alone, SAY SO ON THE GRADE.** *(Instrument-check flags `BRT-26-RIGS` STALE, newest datapoint 7/31 = 12d vs a 10d budget.)*
4. **🟠 ~8/17 — CPC / non-Russian-tanker falsifier.** ⚑ **Live input from WALTER `SIG-W-20260812-001`: Novorossiysk was struck overnight 8/11-12 (Palianytsia jet drones + Neptune + naval drones, Zelenskyy on record); SHESKHARIS RE-STRUCK (~600-700 kb/d, already down to one berth) — but CPC is NOT reported hit. That distinction is the whole ballgame: the falsifier SURVIVES this event rather than being resolved by it.**
5. **🟡 OWED FROM THIS SESSION'S MAIL — two items I NOTED rather than ACTED, deliberately, and must not lose:**
   - **INCIDENTS.tsv row for the 8/11-12 Novorossiysk / Sheskharis strike.** Not written this session. **Check HAWK's cross-theater `STRIKES.tsv` first — it is the unified ledger; do not fork a parallel record.**
   - **Pull the Shell Q2 deck PRIMARY** before `SIG-W-20260812-016` touches any gate wording. Shell's own slide puts **damage, barrels and the words "force majeure"** on the Qatar disruption (Pearl GTL Train 2 damaged to Q1-2027) — **which is a counter-example to my GATE-1/FAL-01 evidence bar** ("no damage assessment, no bpd offline, no force majeure"). ⛔ **WALTER states plainly it never reached the deck — every figure is read off a screenshot. A named-operator force-majeure disclosure is exactly the class I must not bank off an unverified image.**
6. **🟡 Archive the RED packet** `2026-08-12_from-RED_evidence-for-your-basis-ruling-...` once RED's own commit lands (see MAIL STATE — deliberate 13-rows/12-moves exception).
7. **🟡 Still open from 8/10, unchanged:** EIA imports-by-country primary (Saudi→US ~600 kb/d Apr → ~0 late-Jul; I have the EIA v2 API wired — pull it, don't propagate a Bloomberg chart rendering) · ORACLE's forward cumulative-transit ladder in-or-out of my instrument set · NEXUS_BRIEF still over its 100-line cap · 5 structurally unresolvable predictions (BRT-07/12/16/17/21) · the SPR "floor" ambiguity **252.4M vs 400.0** (147.6M under one word — read the rationale, do not find-and-replace).

## ★ THE SESSION IN FIVE LINES

**A prediction market found the cycle's only ZERO-TRANSIT day through Hormuz — 2026-07-23, `n_total = 0` — and my own graded window opened 7/24.** I can prove the off-by-one: today's pull reproduces my recorded ten-print sequence exactly.
**Ruling the crude instrument basis was supposed to be a labeling chore. Nothing was an artifact — all four 7/23 figures are real, on four instruments, ~$11 apart — and the reconcile produced a NEW INSTRUMENT.**
**The prompt premium (Dated Brent − front settle) broke regime on 7/21 and PEAKED AT THE PRICE LOW on 8/5: the Bessent deal-talk selloff repriced paper and did not reprice a single barrel.** THESIS → **v5.5**.
**Routing Boundary #3 RESCINDED after ~7 weeks — on TWO independent instruments, not one line cleared by a whisker.**
**And I found my own 8/10 "close" wrong for the THIRD time in six days — the press relay PROME tagged "two-witness owed" was right and I was wrong.**

## CHANGES SINCE LAST SESSION

- **⛔⛔ MY 8/10 BRENT "CLOSE" WAS AN INTRADAY PRINT. Published `$87.85`; the settle is `$87.72`** (`BZ=F` and `BZV26.NYM` agree to the cent; it is what HEARTBEAT and the press relay already carried). 87.85 sits inside the 8/10 range. **THIRD instance of this class in six days.** ⇒ **the M1−M3 ladder error is DOWNSTREAM of it, not separate.**
- **✅ ROUTING BOUNDARY #3 RESCINDED.** Cushing 2-of-2: wk-7/31 **20.955M** + wk-8/7 **22.566M** (+3.97M in two weeks, 2.57M above the floor). Second witness: **WTI−Brent −$5.73**, negative every session since 7/28, **$10.7 from the dislocation trigger.** **Re-activation automatic on any single print <20.0M.** LIQUID/HENRY/RED all packeted.
- **🔴 SPR 298.694M (−6.115M) — first cross of the named <300M watch.** 43-yr lows, **draw ACCELERATING** (−2.84 → −3.7 → −5.1 → −6.115). Recorded, not a trigger.
- **⛔ ZERO-TRANSIT DAY 2026-07-23 CONFIRMED** (`n_total`=0, 0 tanker/0 container/0 cargo). **Plus SEVEN zero-TANKER days: 7/24 · 7/25 · 7/27 · 8/2 · 8/5 · 8/6 · 8/9** — for an oil thesis the more relevant object. Recorded, **not** promoted (needs a base rate); routed to FALCON, whose bands key on `n_total`.
- **⚖️ BASIS CANON RULED.** 7/23: **Dated Brent $105.32** (= EIA's "~$105", confirmed) · **front settle $100.69** (= MARCO's bar, real) · Oct-26 $94.26 · Dec-26 $86.97. Bare "Brent $X" banned. ⚠️ **`BZ=F` is CONTINUOUS and rolled Sep-26→Oct-26 on ~8/3.**
- **🆕 PROMPT PREMIUM adopted as a TRACKED SERIES** (n=50 base-rated: mean +1.20, median +1.26, sd 3.10, range −3.27…+7.20). **NEGATIVE 21-of-21 (6/18→7/20) → POSITIVE 16-of-16 since 7/21.** **Max +$7.20 on 8/5 — at the price LOW.**
- **✅ 35a ENCODED REVERT** (TRADE.md, zero thresholds moved). **35b successor BUILT** → `setups/2026-08-12_35b-COT-successor-band-N1-build.md`. **Incumbent is ANCHOR-FITTED: SPENT fires on 1 of 8 anchors, and that one (7/7) is the series' local MAXIMUM.**
- **✅ BLOCKERS 2 → 1.** PortWatch healed (publishes through 8/9, 3d vs a 7d budget) ⇒ `KILL-LEG2-TRANSIT` no longer stale; re-graded on the corrected record, **min 0 / max 6 = 17.1% of the >35 bar, NOT FALSIFIED.** Only `EU-STORAGE` remains (Will's GIE/AGSI+ key).
- **📬 THIRTEEN packets processed** (8 WALTER + 5 general) — inbox was **not** empty at boot despite STATUS claiming so; 8 WALTER signals had accumulated unseen.

## WHAT I DID

**① CLOSED PROME'S ITEMS ⑥ AND ⑦ — the two that gated HEARTBEAT.** Ruled the basis per surface; confirmed the zero-transit day at the primary.
**② RESCINDED BOUNDARY #3 on two independent instruments and ran the adverse reading out loud** (import-driven build) **rather than leaving it implied** — then rejected it with a stated reason: the boundary flags an operational minimum, absent at 22.566M regardless of what filled the tanks.
**③ FOUND THE NEW INSTRUMENT WHILE DOING A LABELING CHORE.** The prompt premium answers the circularity that forced me to downgrade ORACLE on 8/10 — it is priced by cargo buyers and is **not** made of PortWatch.
**④ KILLED "first-ever $100 Brent" ON THE FULL SERIES** (9,953 obs; 1,159 days ≥$100 since 2008-02-29; six episodes over 18 years) — and RED had **independently** reached the same conclusion and sent evidence **before** my ruling. ★ **That sequencing is what prevented a laundering: RED's `$100.19` reproduces from NO instrument I hold on either date, so it is a number with no source — and a basis ruling would have relabeled it into looking sourced.**
**⑤ RETRACTED MY OWN STEEPENING CLAIM** (item ④). With M2/M4 marks finally held: 8/7→8/10 M1−M3 is **+$0.08**, not ~$0.5–0.7, **and the PROMPT leg M1−M2 actually FLATTENED.** Direction survives; magnitude retracted.
**⑥ REFUSED TO CLEAR `BZZ26` ON A CLEAN RESULT** (item ⑤). 12/12 = 100% — **and I called it what it is: 12 pulls in an 18-second window measures one moment, and the 8/11 failure was itself a same-session cluster.** NOT installed.

## NEXT SESSION (dated, future-verifiable)

1. 🔴 **STEO 2027 columns write-back** · 🔴 **8/14 COT (re-grade the REVERT branch, ladder from 102,560, no stacking)** · 🟠 **8/14 Baker Hughes** · 🟠 **~8/17 CPC falsifier (CPC not hit 8/12 — falsifier survives)**.
2. 🟡 **INCIDENTS row for Novorossiysk/Sheskharis 8/11-12** — check HAWK's cross-theater `STRIKES.tsv` first.
3. 🟡 **Shell Q2 deck primary** before the Pearl-GTL force-majeure datum touches GATE-1/FAL-01 wording.
4. 🟠 **Re-confirm the 8/7 crude closes** — FRED now publishes through **8/11**, so `DCOILBRENTEU` CAN witness 8/7 now. **The 8/10 correction is currently one-witness on the settle leg; do not let it harden un-witnessed** — that is the same class as the error it fixes.
5. 🟠 **The `probe_arcgis` fix from 8/7 has STILL never been falsified against a genuinely stale partition** — `[[finding_test_the_guard_not_just_the_guarded]]`. Its clean output is not yet evidence.
6. 🟡 **WP3 residual** (Will's call): make `eia_weekly.py` a registry consumer, or narrow the registry header's "EVERY registered test" claim.

## OPEN THREADS / WATCHES

- **⛔⛔ THE SESSION'S REAL FINDING, AND IT IS ABOUT SCOPE, NOT ARITHMETIC: my throughput record's most extreme observation sat ONE ROW above the top of the window I graded, and a prediction market found it first.** `[[finding_verification_zero_is_ambiguous]]` — **"no zero-transit day" was never a finding, it was the edge of my scope.** ★ **The generalisable version: I have base-rated my thresholds, my instruments and my anchors this cycle. I had never base-rated my WINDOWS.** The rule I am keeping: **a resolved market is a POINTER TO A PULL, never a substitute for one** — but the reason to keep it just changed from "markets can be wrong" to "markets can be right about my blind spot."
- **⛔⛔ THE INSTRUMENT-CLASS ERROR IS NOW n=4 IN SIX DAYS (8/7 ×2 legs · 8/10 · 8/12), ALL THE SAME SHAPE: a still-forming bar quoted as a close.** ★★ **The escalation is the finding: on 8/7 I made it inside the banner correcting two other agents for it; on 8/10 the autonomous routine was right and I would have "corrected" it; on 8/12 the press relay flagged "two-witness owed" was right and I was wrong; and then I made it AGAIN, IN THE RULING THAT BANS IT, in the same document where I wrote "a daily BAR is not a settle" — and propagated it into five packets.** **FOUR TIMES THE EXTERNAL SOURCE WAS RIGHT AND MY CANONICAL SURFACE WAS WRONG.** ⇒ ⛔ **N5 clause (i) is ATTRIBUTED TO ME and I have now violated it four times in the week I authored it. THE LESSON IS DEFINITIVELY NOT THE FIX — 4-for-4 is proof that a rule requiring me to remember does not work on this defect.** **THE MECHANICAL REPLACEMENT (the actual root cause, which is a CLOCK not an attention failure): every one of the four came from reading a daily bar while that contract's own session was still OPEN. ⇒ NEVER read a futures daily bar as a "close" before session end — ICE Brent 18:00 ET · NYMEX WTI 17:00 ET — and if you read it earlier, label it PROVISIONAL LIVE BAR AT CAPTURE, not at review. Split every tape by SESSION-END, not by date: equities close 16:00 ET and futures do not, and that gap is the whole defect.** *(Retirement ratchet: this EXTENDS N5 clause (i) with the capture-time test it was missing; supersedes nothing. **Proposed to PROME/WALTER as an N5 addendum, NOT applied fleet-wide unasked** — N5 is WALTER's to own and circulate.)*
- **★★ THE STRONGEST FREE EVIDENCE I NOW HAVE, AND IT COSTS NOTHING TO KEEP WATCHING: the prompt premium peaked at the price low.** 8/5 front futures $79.45 (bottom of the ~15% deal-talk selloff) with the premium at its cycle max +$7.20. **Watch whether the premium stays positive through any further deal headlines — a paper selloff that physical refuses to follow is v5.4/v5.5 confirming, and it is independent of everything else I own.**
- **⚠️ TWO REGIMES IN n=50 ⇒ the unconditional mean (+1.20) is NOT a usable central tendency. Quote the regime, never the mean.** Also: the series has **never observed a genuine reopening** either — it does **not** close the n=0 calibration gap.
- **⛔ 35b: the incumbent band is ANCHOR-FITTED (1-of-8), which is worse than the margin finding I reported 8/7.** The successor is 4/4 robust and grades today as **NO-VERDICT, not SPENT** — i.e. **the incumbent has been converting a non-call into a sizing input for two weeks.** ⚠️ **Successor's own cost, named not buried: a 33.6% NO-VERDICT rate.** Acceptable for a SIZING modifier (silence defaults to the conservative branch); **would NOT be acceptable for an entry trigger — never reuse this spec as one.**
- **⚠️ R1 (OVX close >68.97) — OVX 56.06 [8/10]. STILL a NAMED CANDIDATE, NOT a registered tripwire. Recorded, never graded.** Re-arming requires a FRESH Will ruling.
- **⛔ EXPORT-SIGN WARNING still live:** an August "global crude exports rising" print is **over-determined and NOT a supply signal.** Burn a refinery → free the crude. Two theaters, two signs, one mechanism.
- **⚠️ RUNS-DECLINE IS NOT CAPACITY-OFFLINE.** ~47% of damaged Russian capacity already restored [Reuters via ua.news, **7/21 vintage**, three limits all pushing the same way]. **Band stays 25-35%; the ~33% re-centre is a candidate with Will, NOT applied.**
- **🕐 TENOR:** EIA's own STEO closes the no-absorber window in **early 2027**. **Positions outliving Q4-2026 bet the Gulf impairment outlasts EIA's recovery path.**
- **🚢 Still no freight/Worldscale feed anywhere in the kit** — the gap that retired `VLCC >WS200` (7/31) and that blocks the Suezmax pool-tightness falsifier. **Building either means acquiring a feed first: a NEW REGISTRATION, not an analysis.**
- **⚠️ Black Sea war risk UNPRINTED for 20+ days (last 7/21). Report it to nobody as flat.**
- 🟠 **46 routine-authored commits still unaudited** · diesel crack card `NO AT THIS PRICE` · **two diesel margin figures unreconciled** (~$70/bbl IEA-basis vs my carried $82.53 [8/4 intraday] — different instruments, no blending until the definitions reconcile).

## POSITION DECISIONS PENDING

- **NONE. `$0` at risk from any gate — there is no live gate.** Convex arm **RETIRED 8/7 by Will, UN-DEPLOYED, `$0` ever at risk.** ⛔ **Will's 8/4 fill decline is STANDING and untouched — two separate decisions.**
- **★ THE REAL RISK IS UNCHANGED AND UNDEFENDED: USO 35 shares ≈ $4,456 at $127.30 = the book's large linear oil leg, no defined risk.** Not a trim recommendation (root rule #7 — thesis intact, and v5.5 strengthened it) and equally not an add.
- **5 live oil expressions.** USO 35sh · **USO Oct-16 135C ×2** · USO Sep-18 150/165 · **XLE Sep-30 65C ×2 (DEMOTED as a vehicle class 8/7 — the demotion rested on capture in both directions plus a six-week realized integral, NOT on distance to strike).** ⚠️ **Option MARKS are `[STALE 8/4 broker export]` — I re-pulled UNDERLYINGS today, not the chains.** ⛔ **STNG is a TRACKED TICKER, not a holding.**

## MAIL STATE

- **✅ INBOX: 13 processed** (8 WALTER + 5 general) — **2 acted / 3 noted / 4 info-only** on the WALTER lane; **5 acted** on the general lane. ⚠️ **The inbox was NOT empty at boot** despite STATUS's 8/10 claim: **8 WALTER signals had accumulated unseen since 8/11.**
- ⛔ **RECONCILE IS 13 ROWS / 12 MOVES — BY DESIGN, DOCUMENTED, NOT AN OMISSION.** RED's packet arrived at **16:48 mid-session** and is **UNTRACKED** (RED states it is committing it itself). `git mv` refuses; bash `mv` would race RED's uncommitted work, which the root protocol forbids. **Left in place at `inbox/` top level, fully processed and ruled. Archive next session once RED's commit lands.**
- **SENT (6):** → **RED ×2** (the $100 correction + the RULING answering its direct ask) · → **LIQUID**, **HENRY** (Boundary #3 rescinded) · → **MARCO** (its bars vindicated + the settle series it asked for) · → **FALCON** (zero-transit day + the seven zero-tanker days) · → **PROME** (the full ruling report that unblocks HEARTBEAT's `[PENDING BRENT basis ruling]` hold).
- **Outbox: 6** — unchanged; loops not demonstrably closed, correctly left top-level.
- **Owed TO me:** **Will — the 35b successor decision (one touch) · the GIE/AGSI+ key (`EU-STORAGE`, pending since 8/2) · the war-risk-halves ruling · the WP3 call · the FORGE fill-price reconcile on the Sep-18 150/165 (open since 7/24, now 19 days).**

## WORKBOOK HEALTH

- **LIVE:** `TRADE.md` · `STATUS.md` (**~240 ln, inside the 250 cap — watch it**) · `RULINGS.md` · `workbook/REGISTRY.tsv` · **THESIS v5.5** · `docket/CATALYSTS.tsv` · `refinery_damage/INCIDENTS.tsv` (53 rows — **+1 owed for Novorossiysk**) · TRACKER · board_log (**181 rows, +13**) · SCRATCH.
- **Boot 19.7s, 6 checks.** Lesson-conflict **0** · prose/index drift **0** · predictions-due clean · **Instrument Check FINDINGS, 1 blocking** (`EU-STORAGE` NO_INSTRUMENT — Will's key) **+ 2 warnings** (`BRT-26-RIGS` and `COT-FUEL` both stale, newest datapoint 7/31 = 12d vs a 10d budget — **both clear on Friday's prints**).
- **Data pulled this session, all own primaries:** CFTC `72hh-3qpy` (235 wks) · FRED `DCOILBRENTEU` (9,953 obs full history) + `DCOILWTICO` · yahoo `BZ=F`/`CL=F`/`BZV26`/`BZX26`/`BZZ26`/`BZF27` daily OHLC · IMF PortWatch `chokepoint6` FeatureServer (7/08→8/12) · EIA wk-8/7 via the 11:4x routine.
