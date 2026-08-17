# WATT — SCRATCH (next-session pickup)

**2026-08-17 — SIXTH SESSION (Will-directed Monday boot; PROME doorbelled two perishables mid-boot). Two things fired and NEITHER was the summer heat this seat was built to catch.**

**Composite 13/20, unchanged for a FOURTH session — and this time the COMPOSITION didn't move either (2/5/4/2). That is the honest result, not a shortfall:** both firings were **new information inside existing channels**, not escalations of them. Forcing a score move to signal "something happened" is the drift the #1 guard exists to stop.

---

## 🔑 HEADLINE — PJM HAS FILED DOOR B (~2026-08-13)

PJM's **Interim Resource Adequacy Service (IRAS)** petition asks FERC to accept, **within 60 days (⇒ ~2026-10-12)**, a framework in which new Large Loads *"build, bring, or buy the new generation resources… **paying the full cost of those resources.**"* Components: Reliability Backstop Procurement (from **June 2027**) · a **Large Load Registry** · **emergency load reduction prioritizing large loads over residential** · from the **2029/30** BRA, new large loads without their own supply **excluded** from capacity procurement.

- **This is WATT-08's question answered by the PROPOSING party ~10 months early.** Confidence **~65% → ~70% Door B, DATE UNCHANGED, NOT BANKED** (L-32). FERC's order registered as **WATT-10** (~10/12, outer bound 10/31).
- **🔑 The under-noticed limb is (c)** — it writes **curtailment priority into TARIFF**, converting the DOE §202(c)/Manual 13 precedent from an *emergency action* into a **standing commercial term of service**.
- ⚠️ **DOCKET NUMBER NOT VERIFIED.** FR combined-notice cycle runs **~4 days behind** (as of 8/17 it had published only filings received through 8/12); FR term-search for "Interim Resource Adequacy" returns **0**. Sourced to **PJM Inside Lines 8/13**, not eLibrary. **Cite no docket.** Relationship to **EL26-67 NOT established**.
- **Routed to VULCAN, HENRY, CARL + PROME today.**

**Abeyance still UNRULED, and there are now THREE motions** — **Silver Run Electric filed 8/3** for the same 90 days, and **FERC declined a shortened answer period for the SECOND time** (answers 5pm ET 8/7 both times) = weak evidence against a grant [FR 91 FR 51171-72, FR Doc 2026-16175, full text pulled]. ⚠️ A search summary ran the heading **"Abeyance Granted"** over text reciting only the MOTIONS — **fused claim, refuted by the primary.** And **every ISO/RTO** asked for the same 90 days (RTO Insider 8/4; EL26-67/68/70/71/72) — evidence about how hard large-load rules are to write.

## 🔑 SECOND FIRING — MY OWN P1 RED BAND, ON A TECHNICALITY I SHOULD HAVE CLOSED WHEN I WROTE IT

**Sunday 8/16: DM2 5-min max $1,217.52 @16:35 EPT — the season's first RED-band print.** 5 intervals ≥$1,000 in **two** episodes (16:20/16:35, then 19:40/19:50/19:55), 10 ≥$500, both retracing to $40–77 within 5–10 min, **day mean $78.41**.

**Why it is a transient, and the evidence is clean:**
- **Base rate (4,149 August 5-min intervals): 8/16 is the ONLY day with ANY print ≥$500.** Every other day's max = $73.16–$422.35. ≥$500 = 0.24%, ≥$1,000 = 0.12%, all one day.
- **ANTI-correlated with demand** — 8/16 was the month's **LOWEST** peak (122,075 MW); the **highest** (145,375 MW, 8/6) maxed at **$422.35**.
- **Zero PJM postings of any class** accompanied it.

**⚠️ BUT: the old rule ("RT LMP >$1,000 sustained 2+ intervals" — no interval length, no scarcity qualifier) FIRED ON ITS LETTER** (19:50 + 19:55 consecutive ≥$1,000). Recorded as **FIRED-ON-LETTER / MECHANISM-REFUTED**; the old firing **stays in the record**; re-specified prospectively as a **conjunction**:
> **LMP ≥$1,000 sustained 2+ CONSECUTIVE 5-min intervals AND (emergency posting live OR demand ≥97% of trailing 24h peak).**

**⚠️ AND THE INVERSE GUARD — do not let next session dispose of this:** PJM **priced like scarcity at ~67% of installed capacity with no posting.** Logged as a live hypothesis, **FL-WATT-10 minimum-commitment fragility** (thin unit commitment in valley hours + a contingency or the sunset ramp), **with a test**. If real it moves P1 risk **from peak to valley** and couples to P3 (always-on load raises the valley floor).

**P1 HELD at 2** — "cold channel with one unexplained transient" is a 2. **Registered upgrade trigger: a SECOND demand-decoupled RED print, or the 8/16 verified hourly confirming ≥$1,000 → 2→3.**

## ✅ WATT-06 RESOLVED **MISS**

Zero PJM-RTO emergency-class postings 7/17–8/15; the July episodes were **heat-clustered, not a cadence**. **Three independent legs** (the board is a rolling window and cannot certify a 30-day question): **(1) message-ID continuity** — 8/4 boot logged #105429 (8/3) latest; today #105434 (8/6) is **both the only posting and the latest ID** ⇒ nothing of any class issued 8/6→8/17, residue confined to IDs **105430–105433**; **(2) physical** — August's highest day 145,375 MW sat ~14 GW under the 159,046 MW at which the July EEA-1 fired; **(3) publisher** — PJM's **Hot Weather Alert 8/9-11** is *explicitly* "routine" and non-action-requiring, and no Max Gen/Load Management/EEA post all month. ⚠️ **The 8/16 spike does NOT count** — outside the window AND a price event where the bar is a **posting**.

---

## ▶ PICK UP HERE (priority order)

1. **🟡 RE-PULL THE 8/16 VERIFIED HOURLY ON OR AFTER ~2026-08-20 — NOT BEFORE.** ⚠️ **I re-pulled at Will's request at 09:16 EPT 8/17 and it corrected my own clock (L-33): the verified-hourly feed lags ~4 DAYS, not one business day.** Frontier = **2026-08-13**; 8/14 + 8/15 + 8/16 all return 0 rows, while a **control pull of 7/23–8/2 returns its full 264 rows** ⇒ query sound, feed just hasn't reached mid-August. My "Sunday → next business day" was the right conclusion from the wrong reason, and it was published in KB-WATT-079 — **the very row whose purpose was establishing my instrument clocks to discharge N5.** `rt_hrl_lmps`, `pnode_id=1`, `8/16/2026 00:00to8/16/2026 23:59`. **Any hour ≥$1,000 → P1 2→3.**
   **▶ PRE-REGISTERED so the re-pull GRADES rather than confirms: predicted max hourly $502.28 @ 19:00 EPT (upper bound ~$525), ZERO hours ≥$1,000, day mean $78.41.** Estimator = mean of the 12 five-min prints per hour, **validated over 261 overlapping hours (8/3–8/13): mean error −$0.13/MWh, median +$0.01, max |err| $22.25.** ⚠️ **$502.28 sits in my ORANGE band (≥$500)** — expect **Orange, not Red**, missing the RED bar by ~2×. **If the print falls outside ±$22.25 of $502.28, the ESTIMATOR failed and must be re-validated before reuse.**
2. **🟠 Verify 212,000 MW at a PJM primary AND establish its POPULATION.** Currently ONE secondary (law-firm digest). Whole active queue vs one cycle's intake vs EIT-eligible subset = **three different populations, only the first is the right denominator** for P3's `queue > 2× peak` rule (212 GW ÷ 160,451 MW = **~1.32×**; needs ~321,000 MW to trip). **Do not publish the ratio cross-agent until pulled.** *(PJM **EIT was ACCEPTED BY FERC 6/9/26** — the "targeted Aug-2026" item is CLOSED, two months early.)*
3. **🟠 Pull the IRAS docket number** (retry FR API in a few days; or PJM eTariff FercDockets) **and establish its relationship to EL26-67.** Then **FERC's abeyance ruling**.
4. **🟡 Test or kill FL-WATT-10.** PJM unit-commitment / reserve data for **8/16 16:20–16:35 and 19:35–20:00 EPT**; re-run demand-vs-price anti-correlation over a longer window than August.
5. **🟡 P4 instrument fix — 13 days owed, and N5 now gives a SECOND independent argument for it.** Boot overstated by **$11.06** (+$59.37 vs same-vintage **+$48.31**). Also **undischarged under N5 (i-b): I have not established the settlement clock of the NG=F gas leg**, so every spark figure I publish is PROVISIONAL by default until I do (KB-WATT-079).
6. **Predictions: 4 OPEN.** WATT-02 (9/7, EEA2+ — trending MISS; **do NOT bank the 8/16 price spike, its bar is a POSTING**) · WATT-08 (2027-06-30, ~70% Door B) · WATT-09 (~11/30, contingent) · **WATT-10 (NEW, 10/31 outer bound)**.
7. **⚠️ Winter P1 registration is GATED and the gate HELD.** AEOLUS: winter **energy/mean DOWN (established)**; winter **PEAK — NO SIGN** (n=2, split). **2023-24 = warmest US winter on record AND PJM still peaked 134,777 MW Jan 17, running Cold Weather Advisory → Alert → Conservative Operations → NERC TLR-1.** ⇒ **never register "no EEA because El Niño."** Peak-based, sign-agnostic, weighted **mid-Jan–Feb**, not December. Vintage discipline: ONI is revised (use today's file); **never mix +2.03 and +1.2 in one sentence** (different baselines).
8. **Lower urgency:** hedged-vs-floating share of neocloud load (owed VULCAN) · Oracle/We Energies $7B LC vs the Wisconsin PSC docket · Hut8 Beacon Point MW · TSMC-AZ timing · WSJ Trump/utilities full text · EIA-923 PJM-fleet heat rate · the "1-year-early" reconcile.

## ✅ AFTERNOON 8/17 (Will: "lets start working through these") — 4 of the 5 open items CLOSED

**① VERIFIED-HOURLY LAG — I was wrong TWICE and the second one is the instructive one (L-34, KB-WATT-083).** Morning: *"posts next business day"* (assumed). Midday: *"lags ~4 days"* (**measured once**). At 09:20 EPT frontier = **8/13**; at ~09:55 EPT the identical query returned **8/15** — PJM published Fri+Sat **while I worked**. ⇒ **BATCH-PUBLISHED, variable ~1–4 day lag.** Standing form: ***measure the frontier at use time.*** **8/16 still unpublished — try ~8/18, not ~8/20.** Pre-registered estimate UNCHANGED ($502.28 @19:00, zero hours ≥$1,000). 🔑 *One probe establishes a POINT, not a RATE — and the correction FELT rigorous, which is what stopped me asking "is this stable?"*

**② QUEUE FIGURE — CLOSED at PJM primaries, and my number was wrong AND the wrong population (KB-WATT-084/085).** PJM's own: **Cycle 1 = 811 projects / 220 GW** [Inside Lines 4/29]; **+30 GW** transition remainder, **~53 GW signed-but-unbuilt**, **25 GW connected since 2020** [PJM fact sheet **upd. 5/21**, PDF extracted]. My "829 / 212,000 MW" was a stale rendering of **Cycle-1 intake**, not the active queue. **Active ≈250 GW ⇒ 1.56×** the 160,451 MW peak (tracker 282.3 GW = 1.76×; Cycle-1-only 1.37×). **Needs 2× ≈321 GW — NOT-FIRED on any basis, but I had published 1.32×.** **P3 rule RE-SPECIFIED to name its population** — same defect class as the RED band.
🔑 **Two unexpected reads:** **gas = 106 GW = 48% of Cycle 1** (marginal unit stays gas ⇒ structurally supports P4 + the 7.0 HR benchmark); **storage = 67 GW = 30% and produces ZERO net energy** ⇒ **220 GW of queue ≠ 220 GW of supply relief.** And **EIT accepts up to 10 projects/yr × 2 yrs** — the fast lane is **quantity-rationed, not just price-rationed**, sharpening FL-WATT-07.

**③ IRAS DOCKET — STILL OPEN.** FR term-search returns 0; the combined-notice cycle had only reached filings received 8/12. **No abeyance ruling either.** Retry the FR API in a few days or PJM's eTariff directory. **Cite no docket.**

**④ FL-WATT-10 — TESTED AND REFUTED ON ITS OWN CRUX (KB-WATT-086, L-36).** Prediction: valley hours carry thin ONLINE reserve. **Measured: SR availability 8/16 = 2,514 MW vs 8/6 (peak day) = 2,571 MW — 2.2% apart. NOT thinner.** Marked **REFUTED**, not re-described — re-framing it to survive would be the retro-reading I refused on the RED band that morning, and worse since I'd be grading my own idea.
**What the test DID establish:** **local congestion RULED OUT** — congestion max **$3.84** all day (mean $0.16) vs a **$1,217.52** total ⇒ spikes are **99.6–99.8% SYSTEM ENERGY**. And a striking signature: **REG cleared $3,568.97 (16:20) / $3,923.16 (16:25) with procured regulation ABOVE requirement (834 vs 750 MW)** — extreme price, **no quantity shortfall** = steep supply curve for a *capability*. → **FL-WATT-13 registered as a CANDIDATE with its own test.** ⚠️ **Contrary evidence in the row:** REG also spiked $1,549.91 / $900.89 / $1,713.31 the same day with **no** energy spike, and the two episodes sit at different times of day — one ramp story does not obviously cover both. **Do not route or price FL-WATT-13 until tested.**

**⑤ P4 INSTRUMENT — FIXED, plus both DAEDALUS SFG actions (L-35).** Same-vintage spark off **DM2 on-peak** is now the **primary** (+$48.12/MWh, n=1,144); the stale ICE-proxy spark is **REFUSED, not caveated**, at >3d gap — printing what it *would* have said (+$59.17, 12-day gap) so the refusal is auditable. *A caveated number gets quoted; the caveat does not travel.* Boot leg was **rc-only** → now `run_rc_and_marker` (rc **OR** marker, additive). EIA **cache source-mode stated as a wall** (real fix is a FORGE edit — **flagged to PROME, not made**).
⚠️ **Running it caught a defect the fix introduced:** the new guard fired REVIEW on by-design notices. Fixed by **vocabulary** — `⚠️` = state-dependent degradation, `NOTE:` = standing wall — not by weakening the guard. **Then tested the guard can still FIRE: 5/5** (stdout marker rc0 · **stderr** marker rc0 · clean NOTE rc0 · rc1 · rc2). **Boot = `all quiet` rc=0.**

**Two-state pilot, PASS 2:** rotated the 8/16 tape detail + the 6 CLOSED open items. **Pair 67,485 → 58,361 vs the 61,440 cap.** ⚠️ **Mid-session the pair hit 64,880 (3,440 OVER) purely from new true content** — the cap is a live constraint for this seat, not slack.

---

## ✅ CLOSED LATE 8/17 (Will: "anything left incomplete or open?") — the deferred-debt sweep

**`THESIS.md` REWRITTEN — all 9 contradictions fixed, the dead flip killed.** It had gone **36 days** unrefreshed (not the 26 measured 8/7). Fixed: P2 clears ×2→**×3** · shortfalls 1→**2** · **the dead flip** (it still named the 28/29 BRA a *"~Dec-2026"* future test — **an auction that resolved 7/14**; a falsification surface pointing at a PAST event reads live and can never fire, which is the worst defect in the file) · P1 "DM2 not wired"→**instrument of record** · P1 episodes 1→**2** · P3 "55GW not capex-funded"→**VULCAN-06** · P3 trigger live→**FIRED-AND-SPENT** · P4 heat-rate uncalibrated/+$49.53→**calibrated/+$48.31** (the number I formally retracted to BRENT was still alive in my own thesis file) · P4 ICE proxy source→**backdrop**.
**🔑 ROOT CAUSE FIXED, not just the 9 symptoms:** the file had **no vintage of its own**, so it sat **outside every staleness check's range** — a checker keyed on STATUS literally cannot see a file that never claims a date. It now carries a **two-clock header + per-channel `[stamp]` lines** + an explicit **precedence rule (STATUS wins; THESIS is the defect)**. Added **P2 stage 5** (two doors → now a filing) and **P3 stage 5** (ride-through compliance cost).

**Three hygiene defects from the same 8/7 profile, all closed:**
- **`CLAUDE.md` said `power_watch.py` is 3 legs in TWO places** (boot step 4 + FILES table) when it has run **5** since 7/16 — PAT-052, **flagged 7/22, open 26 days.** Both fixed, with the measured **DM2 ~4-day verified lag** written in so the next reader inherits it.
- **`FLOW.tsv` had NO vintage field (D10)** — currency readable only by inference. Added `as_of`, backfilled all 12 rows, documented in `SCHEMA.tsv` (which had covered only KB).
- **`KILL_MEMO.md` did not exist** though my own THRESHOLDS section mandates one for every cascade trigger. **Written cold**: C1–C5 conjunctions, a 5-step ladder (verify → classify → route → score → write), standing prohibitions, and a separate *slower* ladder for C5 the thesis-kill. ⚠️ **C3 gained a third limb because of 8/16** — an absolute peak floor, so 97%-of-peak on a quiet Sunday can't pass as a July-grade event. ⚠️ It is **decoupled from STATUS by design — do NOT rewrite it at closeout**, and never during a live event.

**`boot.py` now returns `all quiet` rc=0** (WATT-06 resolved, so the predictions-due scan is clear).

---

## ▶ DUE 2026-08-22 — two-state STATUS pilot report to DAEDALUS

**First rotation DONE: 10,902 B across 6 genuinely superseded blocks → `status_archive/STATUS_ARCHIVE_2026-08.md`. Pair 67,485 → 57,785 B, UNDER the 61,440 cap, nothing manufactured. Falsifier NOT hit.**
**🔑 The finding that cuts against the pilot's premise (L-31):** DAEDALUS predicted I'd have **nothing** to rotate because my mass is *dense* (543 B/line) rather than accreted. **Density and accretion are INDEPENDENT.** I had no dated session *sections* — what its scanner matched on — but I did carry dated session lead **blockquotes** and live reads labelled *"retained for continuity."* **A scan keyed on headings cannot see accretion living inside prose.** Second time in two weeks the same detector class mis-read this agent (cf. the 8/3 falsification-rail mis-read). **Report it as an over-cap-solved-legitimately result, and say the scan was wrong about me in the direction of "clean."**

---

**INBOX: CLEARED** — 10 top-level packets + 7 WALTER signals all consumed and `git mv`'d to `processed/`. ⚠️ Note for next time: I moved all 7 WALTER signals first and only THEN read the 5 I hadn't consumed via VULCAN's relay — caught it, read them, logged KB-WATT-078/079/080. **Filing before reading is how a consumed-looking backlog hides unconsumed work.**

**GIT:** local was **level with origin** at boot (fetched and verified) — no pull needed. SAM/WALTER had uncommitted files in the tree the whole session, so the "Before pulling" stop rule was moot rather than violated.

**⚠️ RATE LIMIT (standing):** PJM non-member = **6 calls/min**; `power_watch.py` spends 1/run. **This session spent 5** (1 boot + 4 deliberate range pulls: 8/16 hourly ×2, 8/16 5-min, Aug 5-min tape, 8/11-16 on-peak). Never loop.

---

**2026-08-04 AM — FIFTH SESSION (Will-directed, 13-day catch-up). Two obligations cleared; the big research leg is gate-open and UNSTARTED.**

Will's direction this session: *"start those obligations first"* — VULCAN and AEOLUS before the PROME P2 leg. Done, both with real primary-sourced answers rather than acknowledgment notes.

**Scores: P1 3→2, P3 3→4. Composite 13/20 — flat for the THIRD session while composition went 4/5/3/2 → 3/5/3/2 → 2/5/4/2.** The flat total is the least informative number on the page (L-14 again).

- **P1 3→2 🟡 COLD.** 19 days, zero emergency-class postings. Demand 101,714 MW = 75.6% of a 134,628 MW 24h peak that is itself ~28 GW under mid-July. **WATT-03 → MISS**, **WATT-04 → HIT** (industrial retail 8.71¢ May vs 8.66¢ Apr; **8.71¢ is now my canonical P2 retail figure**, supersedes 8.66¢ and DEWEY's "~9¢").
- **P3 3→4 🔴.** VULCAN-06 resolved → the WoodMac 55GW high side is capex-funded. Fired my registered trigger, which is now **SPENT — do not re-fire.** ⚠️ Score ≠ triad: P3's standing rule ("queue > 2× peak") is still NOT-FIRED.
- ✅ **`PJM_API_KEY` restored** — leg-5 DM2 live and it earned its keep day one.

**⚠️ TWO INSTRUMENT DEFECTS, ONE ROOT CAUSE (the session's keeper findings — L-16, L-17):** the EIA ICE proxy now lags **~13 days**. (1) It could not resolve its own prediction: on 8/4 the file still ends at deliv **7/22**, so 11 of WATT-03's 26 window days were never published by its 8/2 check date — I resolved across the gap with DM2 verified hourly (264/264 rows, max single hour $397.87) rather than grading MISS on absent data. **DM2 is now the resolution instrument of record for P1 price predictions.** (2) It inflates the P4 spark spread ~47% (+$43.86 reported vs **+$29.84** same-vintage) by pairing a deliv-7/22 power leg with 8/4 gas. **I did NOT score that delta against P4's "compresses 50%" trigger — it's a basis change (ICE peak OTC vs DM2 RT on-peak), not a market move.**

**Obligations cleared (packets written + committed):**
- **→ VULCAN** — VULCAN-06 consumed (P3 3→4); **shared demand figure agreed as a CATEGORY CORRECTION**: `~55 GW aggregate utility-reported large-load forecast / ~32 GW PJM vetted system-COINCIDENT peak growth` — two bases, one number each, never netted or averaged (L-18). *(⚠️ The "nameplate interconnection ceiling" wording I originally sent was imprecise and is corrected in the PM addendum below — 55 GW is a utility FORECAST aggregate, not a queue figure.)* Hedge read on CRWV: no sourced %, but they mandated ≥95% on RATES and **nothing** on power while writing a defined term for "Excess Unhedged Power Costs" + a §5.25 covenant + a trailing-3-month mark ⇒ **unhedged tail is real ⇒ live transmission**. Flagged that the Negative NOI Event bites on a *projection* ~5 months ahead of any operating loss. FERC door: **Door B ~65%**, registered as **WATT-08**.
- **→ AEOLUS** — Colorado River hydro leg **SIZED, and their anchor corrected on both legs** (L-19). Glen Canyon does NOT stop at 3,490 ft (**630 MW remains**); the binding cliff is **Hoover at Mead 1,035 ft** — capacity **1,274 → 382 MW**, Mead at **1,041 ft = ~6 ft margin**, USBR projects 1,037 ft by 12/31 — and 1,035 is an **economic** threshold in USBR's own words. **But the sizing killed the story:** −27.6% of combined generation already gone, Palo Verde still averaging **$24/MWh** ⇒ too small to reprice as energy. Real loss is **capacity/ancillary (~892 MW)** and WECC has no market to price it into. **Verdict: Tier-2 candidate, NOT core-channel promotion.**

**▶ ADDENDUM, 2026-08-04 PM — Will: *"lets start working through these still open tasks."* Items 2 and 3 CLOSED. Item 1 (the PROME P2 leg) is now the only major open thread.**

**WATT-07's abeyance check (was item 2) was the session's biggest find, and it invalidated something I had published hours earlier.**
- **PJM AND the Indicated PJM TOs each moved 7/28 to hold the show cause in abeyance for 90 DAYS** [Federal Register 91 FR 49426, FR Doc 2026-15779 — FERC Secretary notice dated 7/30, published 8/4; full text pulled via the federalregister.gov API]. They asked FERC to shorten the answer period to 5 days (answers by 8/3); **FERC declined** and set answers for **5:00 p.m. ET Fri 8/7**. **FERC has NOT ruled.**
- → **WATT-07 HIT on its abeyance branch** (the registered alternative fired). Substantive question **deferred, not answered** → successor **WATT-09** registered (8/17-if-denied / ~mid-Nov-if-granted, outer bound 11/30).
- → **WATT-08 re-dated 12/31 → 2027-06-30 the same day I registered it.** Once the filing slipped to ~November, a 12/31 verdict on cost assignment was impossible by construction. **Resolvability defect = status/date change, NOT a confidence cut** — confidence stays ~65% Door B.
- ⚠️ **TWO ERRORS OF MINE, corrected in the record and to VULCAN:** (1) the large-load show cause is **EL26-67-000**, not **EL25-49** — EL25-49 is the *earlier co-location* proceeding (Constellation complaint, 12/18/2025 order, separately modified 6/18/2026); (2) the PJM order has a **FOUR**-item directive list and **omits co-location** — FERC limited it to large loads **NOT** co-located with generation. **Consequence: co-located load is not in the docket I had told VULCAN to watch.** (L-20, L-21.)

**The firm-curtailable number (was item 3) resolved to "there is no third number" (L-22).**
- **32 GW already IS the firm figure** — PJM's vetted, system-**coincident** peak growth.
- The ~23 GW gap is **not** a vetting haircut (PJM's 2026 trim cut summer-2028 peak 4.4 GW / 2.6%, of which **large loads only 0.7%**) and **not** queue attrition (the "~20% of submitted capacity reaches an IA" / "38 GW cancelled 2025" stats are **GENERATION**-queue numbers — **wrong population**). Residual = **non-coincidence + utility self-report duplication**.
- ⚠️ Also corrected my own AM wording: **55 GW is an aggregate of utility-REPORTED FORECASTS, not an interconnection-queue nameplate figure** — different failure mode (self-report inflation vs speculative/duplicate requests).
- **NCBL is a RECLASSIFICATION, not a haircut** (≥50 MW, first-to-be-curtailed, avoids capacity charges, still pays transmission — moves load out of the *capacity construct*, leaves physical peak intact). It went **VOLUNTARY** and is **NOT in effect**; the 28/29 BRA already cleared 7/14 at cap **and** 6,831 MW short without it. **⇒ capacity-obligation offset from curtailable load = 0 GW today.**
- **Sent VULCAN a second packet the same day** correcting the 8/17 resolver, the docket/scope, and the nameplate wording, and delivering the firm number. **Nothing further owed to VULCAN.**

**▶ NEXT SESSION — revised priority:**
1. ~~**THE PROME BATCH-3 P2 LEG**~~ — ✅ **DELIVERED later the same session; see ADDENDUM 2 below.** *(This line was written before Will asked me to take the leg on.)*
2. **FERC's ruling on the 90-day abeyance** — answers closed 8/7. This is the single most informative near-term event on the P2/P3 regulatory track and it sets whether WATT-09 resolves 8/17 or ~11/15.
3. **PJM Expedited Interconnection Track** was targeted to be in place by **Aug-2026** — check status (KB-WATT-052 tail).
4. Then: WATT-06 (8/15), the 6 unfolded WALTER signals, and the older breadth items.

**New this half-session:** KB-WATT-049..052 · L-20..L-22 · WATT-09 registered · WATT-07 HIT · WATT-08 re-dated.

---

**▶ ADDENDUM 2, 2026-08-04 PM — Will: *"can we do this remaining open thread?"* THE PROME BATCH-3 P2 LEG IS DELIVERED. All three still-open items are now closed.**

**Memo:** `outbox/2026-08-04_to-PROME_batch3-P2-power-axis-time-to-power-is-the-cost.md`. STATUS written back the same session (PROME explicitly warned that 7/27 ran 3-for-3 on polished memos + stale STATUS).

**THE HEADLINE — time-to-power prices, and it dwarfs the power price.**
- A year of delay on a **1 GW AI data center** costs **$1.50B** (shell+electrical sunk, 10% WACC) to **$9.55B** (full stack + GPU depreciation @25%) = **$201/MWh to $1,283/MWh** at 7.446M MWh/yr (85% LF).
- Against **US industrial retail $87.1/MWh** and **PJM wholesale ~$48/MWh** ⇒ **delay is 2.3×–14.7× the commodity.**
- **Levelized:** PJM's **3.4-year average queue wait** carries the shell at **$5.10B/GW** = **$68/MWh over a 10-yr life = 79% of a second power bill.** *That is the literal answer to PROME's "effective cost-of-compute penalty for queue position."*
- **The gap that IS the finding:** the queue-skip price is **capped at $555/MW-day = $27.2/MWh — 7×–47× BELOW the delay it relieves.** ⇒ backstop structurally oversubscribed; constraint is **administrative rationing, not price**; and **co-location/BTM is the market routing around a price cap**, not a tax dodge.

**Q4 answered LOUDLY — and NOT as PROME expected. The ~10× SURVIVES.**
- Capacity **10.2×** → annualized energy **9.4×** → realized 2025 output **4.1×**.
- **It survives because TWO composition errors cancel:** **28% of the US 53 GW is battery storage producing ZERO net energy**, and **China's CFs are ~half the US's**. ⚠️ **Correcting only one side (the usual sneer at Chinese CFs) yields a WRONG ~5%** — further from truth than the naive 10×. (L-23.)
- DEWEY's **>430 GW wind+solar VERIFIES** (434.4 = 315.07 solar + 119.33 wind, NEA 1/28/26); ~543 GW total verifies (~540 implied from 3,891 GW cumulative @ +16.1%).
- ⚠️ **TERMINOLOGY TRAP:** China's reported **"utilization rate" 94.0%/94.7% is (1 − curtailment), NOT a capacity factor.** Real China solar CF **~15%**. (L-24.)
- ⚠️ **NEAR-MISS I CAUGHT:** the quoted "336 TWh solar, +40%" is the **2025 INCREASE**, not the total (**1,175 TWh**). Reading it as the total implies a ~3.5% CF — the implausibility is what surfaced it. **Compute a ratio whose plausible range you know, and treat an out-of-range answer as a definition problem first.**
- ⚠️ **UNITS ERROR flagged to PROME:** "total 2023 US consumption of 477 GW" — consumption is TWh, not GW; 477 GW is *average power* (4,183 TWh / 8,760 h). And **700 GW does not survive as a net figure** (national aggregate, duplicate-laden). Use PJM 220 GW / ERCOT 198 GW instead.

**Q2 — both readings true, and NOT symmetric (L-25).** China's conversion of capacity→energy is **deteriorating** (curtailment 9.2% solar / 8.5% wind early-26; CEC solar utilization **−12%** vs 2020-23; 47% of capacity delivering ~22% of generation). **But curtailing a MWh costs ~$30–60/MWh and waiting costs $201–1,283/MWh** ⇒ **China did not build a more efficient system; it chose a form of waste ~an order of magnitude cheaper.**

**THESIS REFRAME (KB-WATT-058):** the corrected SDI mechanism on my axis is **cost-per-year-of-delay, not cost-per-kWh**. The US is not overpaying for electricity — it is paying a **large, invisible carrying cost on capital that is built but cannot be energized**, which lands as deferred revenue + idle depreciating assets. **The bust channel is stranded TIME, not expensive power.**

**▶ NEXT SESSION:**
1. **FERC's ruling on the 90-day abeyance** (answers closed 8/7) — sets whether WATT-09 resolves 8/17 or ~11/15. Highest-value near-term item.
2. **Awaiting PROME:** whether the abeyance slip earns a DOCKET row (flagged in the memo as catalyst-worthy).
3. **PJM Expedited Interconnection Track** — targeted to be in place Aug-2026, check status.
4. **WATT-06 (8/15)**, the **6 unfolded WALTER signals**, the **P4 instrument fix**, and the older breadth items.
5. Open invitation to VULCAN still standing: give me your load factor and I'll convert $555/MW-day to $/MWh on my basis.

**New this half-session:** KB-WATT-053..058 · L-23..L-25 · Batch-3 P2 memo delivered.

---

**▶ PICK UP HERE (priority order):**
1. **🔴 THE PROME BATCH-3 P2 LEG — gate-open since this boot, still UNSTARTED.** `inbox/2026-07-27_from-PROME_batch3-dispatch-P2-power.md` (kept in inbox deliberately, with DEWEY's 7/24 stub, as the leg's working material). Deliverable: memo → `outbox/` to PROME + same-session STATUS write-back. **Do not rebuild on the refuted "China's cheaper electricity" premise** — it's wrong on price (US industrial **8.71¢** vs China ~9.7¢/~11.6¢), right on **capacity/speed/queue**. The four questions, and PROME's loud-flag request on whether **543-vs-53 GW survives conversion to actual generation** (capacity ≠ dispatchable; >430 GW of China's add is wind+solar). **Re-verify 543/53 GW and the 700 GW queue at run time.**
2. **WATT-07's 8/3 abeyance sub-deadline passed UNCHECKED** — needs a FERC eLibrary EL25-49 pull to see whether PJM filed a 45-day abeyance request. If it did, the 8/17 resolution slips ~45 days. Cheap, dated, and I told VULCAN I'd check it.
3. **Firm-curtailable-adjusted demand number** — the open half of the VULCAN shared figure. Needs a defensible curtailable share (DOE §202(c) + PJM Manual 13, ≥50 MW on 15-min notice). Told VULCAN not to wait on it.
4. **Instrument fix (P4):** compute spark off DM2 on-peak, or refuse to print when leg vintages differ by more than a few days.
5. **WATT-06 (8/15)** trending hard toward FALSIFIED/heat-clustered — 19 days clear. **WATT-02 (9/7)** same direction. **WATT-08 (12/31)** new.
6. **6 WALTER signals still unfolded** (in `inbox/WALTER/`): Oracle→We Energies **>$7B letter-of-credit** collateral call on the BBB− downgrade breaching an A− tariff threshold (SIG-009 — *a power-CONTRACT mechanism, arguably mine*); NOAA **81% very-strong El Niño Oct-Dec** (SIG-012 — Q4 winter-load input); PNW wildfire ignition-liability + the **PSPS-looks-like-demand-destruction** trap (SIG-011); Nvidia/OpenAI guarantee (SIG-002); SIG-010, SIG-018.
7. Older, still open: Hut8 Beacon Point MW + TSMC-AZ fab timing; full WSJ Trump/utilities residential-bill text; EIA-923 PJM-fleet heat-rate; the "1-year-early" reconcile vs PJM's published 2026 summer peak.

**GIT:** did **NOT** pull this session — SAM and TERRY had uncommitted work in the tree (the "Before pulling" stop rule). **Push went out anyway and succeeded** — `safe-push.sh` was a clean fast-forward sweeping 6 commits (3 mine + PROME/SHADE's); pushing never touches anyone's uncommitted work, only the "pull" half of the protocol was blocked. **Verified on origin by hash AND by path** (both packets + the memory file + PREDICTIONS.tsv statuses), not just off the `Pushed.` line. ⚠️ **Still un-pulled** — next session starts behind origin; pull first.

**⚠️ RATE LIMIT (standing):** PJM non-member = 6 calls/min; `power_watch.py` spends 1/run. **This session spent 3** (1 boot + 2 deliberate range pulls). Never loop.

---

**2026-07-22 EVE — FOURTH SESSION (Will-directed, 6-day catch-up). Thesis RECOMPOSED acute→structural.**

The heat broke and the two channels moved in opposite directions — that's the whole session:
- **P2 4→5 🔴🔴 — the 28/29 BRA cleared** (my own upgrade trigger, ~5mo early). $325/MW-day = at cap (97.5%), **6,831 MW short**, $16.4B, 3rd straight at-cap / 2nd straight RTO-wide shortfall. VERIFIED vs PJM Inside Lines + RTO Insider + Talen PR (WALTER SIG-009). **Resolves WATT-01 HIT.** KB-WATT-032.
- **P1 4→3 🟠 — acute episode over.** 6 days no emergency-class since 7/15-16 EEA-1; demand 116,586 MW = 92.2% of a much lower 126,409 MW peak (−36 GW off mid-July's 159–162 GW); proxy normalized ($72/MWh, no Orange since deliv 7/2). KB-WATT-038.
- **Composite flat 13/20 but recomposed** — weight off thermometer (P1) onto mechanism (P2). Status stays 🟠 (auction print ≠ live acute firing). **No deploy change.**
- **WATT-05 HIT** — PJM filed the FERC 30-day large-load informational report by 7/20. Registered **WATT-07** (substantive reform response, 8/17). KB-WATT-033.
- **7/3 EEA2 gap CLOSED** — PROME's 7/16 memo primary-verified it (DOE 202-26-32/33, Manual 13, params verbatim). The last load-bearing "don't carry a trade" caveat is gone. KB-WATT-034.
- **boot.py FIXED** — routed leg-4 through `.venv`; `python3 boot.py` no longer false-fetch-fails on this box. L-13.
- **Integrated 5 WALTER signals + 4 top-level inbox items; lane query ratified to PROME** (added "reserve margin" + "data center power").

**⚠️ NEW GAP (Will-flagged): `PJM_API_KEY` is NOT on this laptop** (machine switch). Leg-5 official intraday DM2 LMP is DARK. Harmless this calm week; **restore before the next heat episode** (STATUS OPEN #1; apiportal.pjm.com or copy the other box's `.env`).

**⚠️ MID-SESSION 🔴 ADJUDICATED — AEOLUS live-C3 flag NOT corroborated.** A 🔴 AEOLUS note (`inbox/processed/2026-07-22_from-AEOLUS_live-c3-doe-eea-record-peak-thu.md`) landed mid-session alleging a DOE §202(c) order issued 7/22 eve + a 166,304 MW record PJM peak forecast for Thu 7/23. Verified against 4 primaries: **DOE 202(c) index shows NO 7/22 order** (latest PJM = 202-26-35, 7/14); live board quiet; demand 36 GW off peak; PJM primary says record was 7/2-4 only. → resurfacing of earlier-July events, false 7/22 date. P1 NOT inflated (KB-WATT-039, L-15); replied to AEOLUS/inbox refuting. **✅ RESOLVED same session — AEOLUS UNCONDITIONALLY RETRACTED the flag** (confirmed my 4 primaries win, logged their L-11, marked KB-AEO-029 CORRECTED, adopted the P2 signal as KB-AEO-034). The flag is CLOSED, not open.

**▶ PICK UP HERE (next session, priority order):**
1. **Thursday-7/23 realized-peak check (now just CONFIRMATORY — AEOLUS already retracted).** Quick EIA-930 PJM 7/23 daytime peak + board glance. Expected mild (refutation stands). Only if 7/23 somehow printed a record with EEA2+/§202(c) would this reopen — very low odds. Do it, but it's a 30-second confirmation, not the priority it was pre-retraction.
2. **WATT-04 resolves at the 7/23 EIA EPM release** — industrial retail ≥ 8.66¢/kWh? Resolve HIT/MISS.
2. **Restore PJM_API_KEY** if Will has switched back to the desktop or dropped it on the laptop — re-run boot to confirm leg-5 live.
3. **VULCAN-06 (7/22–7/31 megacap cluster)** — the 32-vs-55 GW P3 discriminator. Watch VULCAN's read; reconcile-to-one, price whatever MW lands. Don't front-run.
4. **Two ex-PJM MW verifications** (web, no key): Hut8 Beacon Point campus MW, TSMC-AZ fab-start timing (KB-WATT-035). Low urgency (breadth, not PJM scorers).
5. **Read the full WSJ Trump/utilities residential-bill-cap text** (KB-WATT-037, FL-WATT-05) before pricing the cost-reallocation mechanism.
6. **WATT-06 (8/15) + WATT-03 (8/2) + WATT-02 (9/7)** — all P1, all trending toward no-recurrence as the season cools. Resolve as dates pass; don't leave OPEN-but-stale.
7. **WATT-07 (8/17)** — PJM's substantive FERC reform response. Routes to HENRY/CARL on outcome.
8. **Still open, low urgency:** full EIA-923 PJM-fleet heat-rate derivation; reconcile the "1-year-early" finding vs PJM's published 2026 summer peak (~Jan-2027).

**⚠️ RATE LIMIT (standing, when key present):** PJM non-member = 6 calls/min; `power_watch.py` spends 1/run. Never loop; no ad hoc DM2 pulls.

---

**2026-07-16 — THIRD SESSION (PROME-spawned, Will-directed): EEA-1 ESCALATION ADJUDICATED.**

The thing WATT was built to catch fired, and the answer was **🟠 HOLDS, not 🔴**.

- **PJM-RTO NERC EEA-1 (#105399)** — first WATT-observed emergency-class posting. **Effective 00:01–23:59 on 7/16** (forward-issued for the whole operating day, no end time — *not* a stale 7/15 posting; corrected PROME's framing by pulling the detail page). Plus 5 local load-relief warnings + HLV Warning.
- **Official DM2 LMP leg 5 went live and earned its keep day one:** caught **$410.55 @11:30 EPT** same-day, retraced to **$90.08 @14:55**. The biweekly proxy would have surfaced it ~2wk late — exactly the 7/12-flagged blind spot. **PJM_API_KEY item CLOSED.**
- **Verdict rationale:** EEA-1 is one rung *below* the pre-registered EEA2+ Red bar; $410.55 ≪ $1,000; demand 92.1% < the 97% Orange bar. **Decisive evidence — a 1,500h EIA-930 pull showed this episode is MILDER than 7/1–7/3 on all three axes** (159,046 vs **162,648 MW**; EEA-1 vs **EEA2**; $410 vs **$574**) and is **rolling over** (daily peaks: 126,711 → 141,765 → 151,116 → **159,046 (7/15)** → 154,690 (7/16)). WATT scored that bigger episode 🟠; scoring this one 🔴 = drift.
- **C3 read:** chain **CONFIRMED as mechanism, NOT firing as cost** — a ~4h spike that retraced is a rounding error vs an 8.66¢/kWh industrial bill. P1 spikes aren't the cost channel; **P2 is** (annual cadence). For HENRY: FCF power-cost input **unchanged**; **curtailment risk strengthens** (§202(c) bites at EEA2, and PJM is one rung away twice in 14 days).
- **P1 3→4, composite 12→13/20. Status color 🟠 unchanged. No deploy-posture change.**
- **Routed:** AEOLUS + HENRY direct inbox notes (🟠). VULCAN/CARL/REGINALD/BRENT via NEXUS_BRIEF (curated — outbox stays empty; 🟠 doesn't earn a fleet push). Report: `reports/2026-07-16_eea1-adjudication.md`. KB-WATT-026..031, VX-WATT-P1 rescored, FL-WATT-01 rewritten, L-09..L-12 logged.

**▶ PICK UP HERE (next session, in priority order):**

1. **⚠️ TOP — WILL-FLAGGED, still open: the 7/3 EEA2 is INHERITED and UNVERIFIED** (KB-AEO-018, from HENRY's provisional tenure; KB-WATT-031). It under-props THREE conclusions: WATT-02's n=1 recurrence anchor, the §202(c) curtailment precedent, and the "Episode A was worse" comparison this adjudication rests on. Root rule #3 — **must not carry a trade until verified against a PJM primary.** PJM's board retains only ~15 recent postings → needs an archive-grade pull. Recommended to PROME 7/16; **also asked HENRY** (if he has the 7/3 primary in his archive, it closes cheaply). **Check whether either came back.**
2. **WATT-02 stays OPEN — do NOT bank today's EEA-1 as a hit.** The bar is **EEA2+** (resolve 9/7). Today was a near-miss one rung short. This is the exact "don't bank an unpassed forecast" trap; it will be tempting next boot.
3. **Predictions due:** **WATT-05 (7/20** — FERC informational report on large-load/DC interconnection reform), **WATT-04 (7/23** — EIA Electric Power Monthly, May-26 data, industrial ≥8.66¢), **WATT-03 (8/2** — proxy ≥$500 recurrence), **WATT-06 (8/15 — NEW)**. Resolve as dates pass; none were resolvable 7/16.
4. **~7/21 — the biweekly EIA wholesale file should finally carry 7/13–7/17 delivery prints.** This is the **first real cross-check between leg 4 (daily-wtd proxy) and leg 5 (official 5-min)**: does the $410.55 5-min max show up as an elevated daily-wtd print for deliv 7/15 or 7/16? Two price series that should agree — a coherence test worth doing deliberately.
5. **VULCAN-06 discriminator (7/22–7/31 megacap cluster)** — the 32-vs-55 GW resolution clock for P3. Watch VULCAN's read; **reconcile-to-one, don't duplicate**. WATT prices whatever MW lands.
6. **Reconcile the "1-year-early" finding** (PROVISIONAL, KB-WATT-029): PJM hit 162,648 MW (7/02) vs its own **2027**-forecast peak of 160,451 MW. **Not like-for-like** — EIA-930 hourly-avg vs PJM instantaneous coincident peak; mismatch runs *conservative* so it only strengthens. Confirm vs PJM's published 2026 summer peak (PJM Load Forecast Report, ~Jan-2027). **This is the session's keeper finding — don't let it rot into a naked number.**
7. **Full EIA-923 PJM-fleet heat-rate derivation** — still open, still low urgency (HR 7.0→8.0 swing ≈$3/MWh at $3 gas).

**⚠️ RATE LIMIT (standing):** PJM key is **non-member tier = 6 calls/min**. `power_watch.py` spends **1 call/run**. **Never loop the instrument; no ad hoc DM2 pulls.** This session spent exactly 1.

**Open dependencies (not WATT's to do):** PROME/HENRY → 7/3 EEA2 primary verification (item 1); VULCAN → 7/22–7/31 cluster read (VULCAN-06); Will → nothing pending (PJM_API_KEY closed 7/16).

---

**▶ ADDENDUM 3, 2026-08-04 PM-2 — Will: *"I think our last session may have ended suddenly without a proper close out. Please investigate."* IT HALF DID. Audit done, debt paid, and the detector that hid it is fixed.**

**THE VERDICT: the visible closeout was complete and correct — the invisible half wasn't.**
- ✅ **Complete and verified:** STATUS, SCRATCH, LESSONS, NEXUS_BRIEF, KB.tsv and the PROME memo all committed `09f91c5da` at **11:48**, and **confirmed present on origin by path**, not off a `Pushed.` line. **NEXUS Amendment 10 satisfied** — brief 11:47 > STATUS 11:45, i.e. the brief was genuinely folded LAST. Delivery was **per spec**: the PROME dispatch asked for the memo in `outbox/`, not PROME's inbox (§Deliverable line 54) — so nothing was orphaned.
- ❌ **Missed — closeout step 2's other half:** `VX.tsv` and `FLOW.tsv` untouched since **7/22**, 13 days and **three half-sessions** behind. VX carried **P1=3** vs STATUS **P1=2**, **P3=3** vs **P3=4**, and a *"leg-5 DM2 DARK — no PJM_API_KEY"* source note the restoration had already falsified. **Both now current.**
- ❌ **Missed — boot step 6:** the delivered PROME dispatch + DEWEY stub were still sitting in `inbox/` (they had been kept there deliberately as the leg's working material). Leg is DELIVERED → both `git mv`'d to `inbox/processed/`.

**FLOW gained the four pathways the last two sessions produced and never logged:** **FL-WATT-06** two-doors cost-allocation switch (WATT-08/09) · **FL-WATT-07** queue wait → sunk-shell carrying cost → **stranded time** (the KB-WATT-058 reframe) · **FL-WATT-08** power price → Projected DSCR → neocloud borrowing capacity + mandatory prepayment (CRWV §5.25, the first *filed* mechanism) · **FL-WATT-09** correlated-control (Ashburn: the disturbance came from 3 GW of load **leaving**, not arriving).

**🔧 THE ROOT CAUSE, AND THE FIX (L-26).** `boot.py`'s staleness leg printed **"✓ quiet"** at every one of those boots. Not a bug — the shared `ledger_staleness.py` defaults to **`--days 30`**, correctly tuned for *"rot, not mild drift"*. **13 < 30.** That default is simply wrong for a ledger whose whole job is to change every session. **`boot.py` now passes `--days 7` to both staleness legs.** Safe because the threshold is measured **relative to STATUS.md, not in absolute time** — a long gap between sessions ages STATUS too and does not trip it; only genuine write-back drift does. Validated: `py_compile` + both legs run at the exact new invocation.

**🔧 WHICH IMMEDIATELY CAUGHT A SECOND ONE (L-27).** `TRADE.md`, **23 days** behind, still read ***"No trigger crossed"*** — when **P2's trigger fired 7/14** (28/29 BRA at cap + short) and **P3's resolved 7/31** (VULCAN-06). Its blueprint-§8 banner was **true** ("no open positions") while the table under it was **false**; the banner exempted it from the alert but not from being wrong. Rewritten as a **trigger-state** table with a two-clock `Last real data refresh:` header. **Two triggers FIRED, still NO proposal — deliberately**: both fired on structural, known-in-advance prints (an annual auction, a quarterly cluster), which raises conviction but supplies no entry; a firing gate is not a thesis confirmation (TERRY Non-Negotiable #15), and P1 — the only channel that could supply a live Red band — is cold.

**MARKET READ UNCHANGED.** Boot 17:37Z **rc=0, all quiet**: 0 emergency-class (1 routine DOM warning #105429), demand **112,734 MW @16Z = 83.7%** of the 134,628 MW 24h peak, DM2 **$34.00 @13:30, max $144.88 @12:20**. **Composite holds 13/20 · status holds 🟠 · no deploy-posture change · no prediction resolvable today.**

**⚠️ RATE LIMIT: this session spent exactly 1 PJM call** (the single boot run). No ad hoc DM2 pulls.

**▶ NEXT SESSION (unchanged from Addendum 2, re-ranked):**
1. **FERC's ruling on the 90-day abeyance** — answers closed **8/7** (now 3 days out). Sets whether **WATT-09** resolves 8/17 or ~11/15. Still the highest-value near-term item.
2. **WATT-06 resolves 8/15** — 11 days out, trending FALSIFIED/heat-clustered (0 emergency-class in 19 days). Do not bank it early; the bar is any EEA-1+.
3. **Awaiting PROME:** whether the abeyance slip earns a DOCKET row (flagged in the memo as catalyst-worthy). **Also worth routing:** the `--days 30` default is a *fleet-shaped* finding — every agent with a fast-moving state ledger inherits it silently. Not my file to change (`scripts/` is shared) — flag to PROME.
4. **PJM Expedited Interconnection Track** — targeted in place Aug-2026, check status (KB-WATT-052 tail).
5. **P4 instrument fix** — compute spark off DM2 on-peak, or refuse to print when leg vintages differ by more than a few days (L-17).
6. **6 unfolded WALTER signals** in `inbox/WALTER/` (SIG-009 We Energies >$7B LC collateral call is arguably mine — a power-CONTRACT mechanism; SIG-012 El Niño Q4 winter load; SIG-011 PSPS-looks-like-demand-destruction; SIG-002, -010, -018), then the older breadth items.
7. **Open invitation to VULCAN still standing:** give me your load factor and I convert $555/MW-day to $/MWh on my basis.

**GIT:** pull **not** needed — fetched and verified local is **level with origin** (0 behind; the 1 commit ahead is TERRY's, not mine, and safe-push will sweep it). SAM had uncommitted work in the tree the whole session, so the "Before pulling" stop rule was moot rather than violated. **Nothing of mine was ever orphaned.**

---

**▶ ADDENDUM 4, 2026-08-04 PM-2 — Will: *"anything else left unaddressed or incomplete?"* YES — boot step 6. The 6 WALTER signals are now PROCESSED (they had been carried across 3 sessions).**

**KB-WATT-059..064 logged, all 6 `git mv`'d to `inbox/WALTER/processed/`. `inbox/WALTER/` is now empty of unprocessed signals for the first time since 7/23.**

| Signal | Verdict | Row |
|---|---|---|
| **SIG-009** Oracle >$7B LC ← We Energies | **The seam runs BOTH ways** — CRWV is power PRICE → DSCR → borrowing capacity; this is credit RATING → tariff covenant → collateral call. ⚠️ single-lineage FT, **not verified** | KB-WATT-059 |
| **SIG-010** federal energy grants cancelled by 2024 vote | ⚠️ **WATT was the ACTION recipient — the 3 requested steps are still NOT DONE.** See below | KB-WATT-060 |
| **SIG-011** PNW wildfire | Took only the **PSPS-looks-like-demand-destruction** read-guard; WECC, out of footprint, does not touch P1 | KB-WATT-061 |
| **SIG-012** NOAA 81% very strong El Niño Oct-Dec | **Sign may be INVERTED for my footprint** — routed to AEOLUS | KB-WATT-062 |
| **SIG-018** Oracle/Pentagon "up to $7B" | 10-yr **ceiling**, not revenue. ⚠️ **Must NOT be netted against SIG-009's $7B** — unrelated objects | KB-WATT-063 |
| **SIG-002** FLASH Nvidia $250B guarantee / 10-GW Ohio | **The largest single load yet attached to the Door A/B switch, and it's IN PJM.** A **CREDIT** de-rate, not a demand de-rate | KB-WATT-064 |

**🔑 The one that changes a read: SIG-002.** The 10-GW Ohio campus is in **PJM** (already joined at FL-WATT-09) and is now the largest single load attached to the $555/MW-day switch. If a 10-GW load is financed on a guarantee written *precisely because the offtaker is sub-IG*, then **Door B lands on a counterparty whose credit is the reason the structure exists at all** — that strengthens the Door-B-degrades-AI-capex-ROI leg **without** changing WATT-08's registered ~65%. **P3 stays 4** (its upgrade trigger is spent; next rung needs IPP guidance RAISED, not reaffirmed). ⚠️ The guarantee is an **ongoing negotiation** — no filing, no confirmation, **do not size it.**

**⚠️ SIG-012 — I did NOT carry a direction, deliberately.** The advertisement behind it names "power grids" as a threat, but a strong El Niño conventionally means **MILDER eastern-US winters**, which would **LOWER** PJM winter peak. **The naive read may be sign-inverted.** Packet to AEOLUS: `AEOLUS/inbox/2026-08-04_from-WATT_el-nino-sign-for-PJM-winter-peak-the-naive-read-may-be-inverted.md` — asked for the sign for **PJM winter peak specifically** (+ peak-vs-load-shape, + any hydro/gas leg touching P4). **This gates any Q4 P1 successor prediction:** WATT-06 (8/15) and WATT-02 (9/7) both expire *before* the Oct-Dec window, so a winter re-escalation call registered on an inverted sign would manufacture a MISS I'd have earned by not asking.

**⚠️ STILL OPEN AND OWED BY ME — SIG-010's three steps (WATT is the ACTION recipient).** WALTER read the post and headline card only; programme, dollar total, states, case and *the exact wording of the acknowledgment* are all unverified. Owed: **(1)** retrieve the primary court filing; **(2)** executed or **ENJOINED** — a cancellation under litigation may be reversed, which is a different signal entirely; **(3)** does any of it touch **grid-RELIABILITY / interconnection** funding vs efficiency/consumer/climate programmes — **only the first bears on my thesis and the headline does not distinguish them.** Logged ASSUMPTION, **not priced**, and it has **no established bearing on any channel** until (3) is answered. *This is deferred research, not a done item — do not let the KB row's existence read as closure.*

**Nothing here changed a score.** Composite 13/20, status 🟠, P1 2 / P2 5 / P3 4 / P4 2 — all unchanged.

---

**▶ ADDENDUM 5, 2026-08-04 PM-2 — Will: *"yes go ahead."* SIG-010's THREE STEPS ARE DONE. The last owed item from the audit is closed.**

**`KB-WATT-065/066/067`. Intake row `KB-WATT-060` marked SUPERSEDED (retained as intake record only). Packet closing the action → `WALTER/inbox/2026-08-04_from-WATT_SIG-010-closed-...`.**

1. **THE PRIMARY** — a filed declaration by **Jeffrey Novak, DOE principal deputy general counsel**: *"DOE accepts that the inclusion of grants in the October notice tranche was based solely on the political identity of the grant recipient's state…"*, and not *"based on any programmatic, statutory, cost-reduction, or performance-based factor."* **284** grants met the blue-state test; **~340** proposed-but-spared were all in Trump-2024 / ≥1-Republican-senator states. **An admission by a party against interest inside a proceeding — it holds.**
2. **EXECUTED OR ENJOINED → ~98.5% EXECUTED.** ⚠️ **The circulating "a judge ruled the $7.6B illegal" is a FUSED claim.** Actually vacated: *City of Saint Paul v. Wright* (Mehta, Jan-26) **7 grants / $27.6M**, + *American Institute of Chemical Engineers v. Wright* (stipulated judgment) **11 / $82.1M** = **18 grants, ~$109.7M = ~1.5%** of $7.5B. Plaintiff-specific vacaturs, **not** a global injunction. **Anyone carrying "struck down" is wrong by ~65× on dollars.**
3. **DOES IT REACH GRID/INTERCONNECTION → YES.** **GDO: 25 awards cancelled, incl. $464M GRIP** for the transmission-study process on **5 HV lines across 7 Midwest states**, recipient = **MN Dept of Commerce + Great Plains Institute + MISO + SPP**. Tranche: EERE 200 · FECM 68 · **GDO 25** · MESC 6 · ARPA-E 1.

**🔑 The 'and/or' resolves an apparent contradiction:** affected-state list is all-blue, yet the GRIP lines run through mostly-RED states — because the **RECIPIENT** is Minnesota while the **PLACE OF PERFORMANCE** spans red states. That is exactly the population the concession's *"recipient location and/or at least one place of performance"* defines.

**⚠️ NO CHANNEL SCORE MOVES, and that is the finding, not a shortfall.** It is **MISO/SPP, not PJM** — out of my footprint. And **none of the ~$109.7M vacated is grid/transmission** (restored items are efficiency, critical minerals, solar, hydrogen, EV charging, SolSmart) ⇒ **the $464M transmission money appears to remain cancelled.** The mechanism is real and now primary-sourced — federal cost-share for transmission is a political variable, raising state-level grid-capex variance and pushing deferred cost-share toward **RATE BASE** (→ CARL consumer leg, → HENRY cost input) — but it is **breadth, not a P-channel input.** *Cf. L-19: don't promote a channel because the primary source turned out rich.*

**⚠️ CARRIED, NOT RESOLVED (3 open caveats):**
- **Count discrepancy is a POPULATION difference, not competing estimates** — 321 awards (Latitude 10/2/25) vs 223 projects (DOE release) vs 284 grants (the concession). Only 284 is the politically-defined subset. **Do not pick one.**
- **Cancellation = Oct-2025; admission = Jul-2026** — 9-month lag; cite as separate events.
- **INFERENCE not verified:** that the $464M GRIP sits among the **284** specifically (vs merely within the 321 tranche). Recipient-state logic makes it likely; confirming needs the grant schedule attached to the filing. **Not adjudicated.**
- **Not established:** whether further litigation reaches the remainder, or whether DOE is appealing. **~1.5% is a FLOOR on reversals, not a final figure.**

**▶ NEXT SESSION — unchanged ranking, minus this item:**
1. **FERC abeyance ruling** — answers closed 8/7. Sets WATT-09 at 8/17 vs ~mid-Nov. Highest-value.
2. **WATT-06 resolves 8/15** — trending FALSIFIED/heat-clustered. Don't bank early; bar is any EEA-1+.
3. **Awaiting AEOLUS:** El Niño sign for PJM winter peak (gates any Q4 P1 successor prediction).
4. **Awaiting PROME:** DOCKET row for the abeyance slip; the `--days 30` fleet-shaped staleness proposal; MEMORY.md at 82%.
5. **Oracle/We Energies $7B** — confirm vs the Wisconsin PSC docket (KB-WATT-059 is PROVISIONAL, single-lineage FT).
6. **P4 instrument fix** — spark off DM2 on-peak, or refuse to print on mismatched vintages (L-17).
7. PJM Expedited Interconnection Track (targeted Aug-2026); older breadth items.
