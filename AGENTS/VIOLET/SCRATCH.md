# VIOLET SCRATCH — September 4, 2026 (Fri pre-open ~08:3x–09:0x ET — **Will-spawned catch-up after 2 sessions dark. The tail reloaded to its first ≥150, the rates run rolled over, NFP came in 3× consensus — and I had to correct my own headline finding from 9/2 against myself.**)

> **Scope as given (Will):** *"boot up… we may have been dark for a couple days so first task is to simply catch up on recent info/data."* Straight catch-up. No thresholds moved, no proposals, no edits outside `AGENTS/VIOLET/`.
> **🔑 The session's shape: I booted expecting to reconcile two days of tape and instead found that (a) the finding I led with on 9/2 does not reproduce, (b) my grading series crossed RED's line for the first time this leg, and (c) the single largest input to my pre-registered FOMC letter printed 25 minutes before boot. The first of those is the one that changes how I work.**

---

## CHANGES SINCE (9/2 ~21:5x → 9/4 ~09:0x — 2 sessions dark)

- **`^SKEW` 144.12 [9/2] → 150.63 [9/3], +4.52% — the FIRST ≥150 OF THIS LEG.** CBOE has now published it (own pull 9/4 08:4x, HTTP 200, 202,850 B), confirming the mirror to the hundredth. ⇒ **RED-FT-10 = 1 OF 4, ARMED, NOT FIRED.**
- **20d `^SKEW` avg kept climbing:** 141.13 [9/1] → 141.67 [9/2] → **142.47 [9/3]**. Regime un-terminated **and rising**.
- **THE FRONT END WENT THE OTHER WAY:** VIX 15.20 → **14.32** (−5.8%), VVIX 86.25 → **83.80**, and M1:M2 contango **steepened to +12.16% = `COMPLACENCY_TOP_30PCT`**, the richest of the leg.
- **MOVE ROLLED OVER:** 77.88 [9/1] → **79.71 [9/2] peak** → **74.68 [9/3] = −5.03**, the largest one-day drop in the series. Back **below** confirm-3 (75.50); above F1 (72.41). ⇒ **crack-vs-fade tree back to 0 of 6.**
- **AUGUST NFP +162,000 vs +53,000 consensus** (08:30 ET today, own BLS fetch), unemployment 4.1%, AHE +0.3% vs +0.2% exp. **Under the inverted reaction function this is the HAWKISH print**, 8 days before FOMC.
- **OVX canary WATCH → FIRE** [9/3] — but **on the denominator** (OVX fell 47.77→46.41; VIX fell faster).
- **JPY waking:** USDJPY 160.2 → **156.58** (−2.3% in 2 sessions), RV10 p23.8 → **p62.2**. Band still CALM.
- **Credit unchanged in direction:** CCC 10.49 → 10.53, CCC-BB 8.97 → **9.00**, still widening.

---

## WHAT I DID

1. **Booted clean.** Origin 0 behind (no pull needed — and BOND/SAM had uncommitted work in the tree, so a pull would have been protocol-blocked anyway). Staleness rc=0, corrections rc=0, workbook validates 225 rows / 0 errors.
2. **Closed the WALTER lane 2/2** — `SIG-W-20260903-001` (acted) and `-011` (noted); board_log rows written, files `git mv`'d to `processed/`.
3. **Answered the ACTION in `-001` the same session it was owed:** pulled CBOE, found 9/3 **published** at 150.63, and derived the sustain arithmetic — **earliest possible fire is the 9/9 close**, because **Labor Day 9/7** breaks the chain (9/3 · 9/4 · 9/8 · 9/9).
4. **RESOLVED THE RED/WALTER DISPUTE AGAINST MYSELF.** Re-pulled yfinance across six windows; the 8/28 bar is present at 149.77 in all of them **including `period='20d'`, the exact call my 9/2 pull used**. Not a window artifact, not a method difference. **KB-VIO-215 → CORRECTED; KB-VIO-221 filed.**
5. **Fetched the NFP print at BLS primary** rather than taking the search-index summary (which still claimed the release was "tomorrow").
6. **Fixed a CALENDAR/CATALYSTS divergence I did not create but did own:** CALENDAR still carried MU at **Sep 29** two sessions after CATALYSTS was reconciled to **~9/22**. Also stripped a 2-week-stale hard OI figure out of CALENDAR's 9/16 row.
7. **Added Labor Day 9/7 to both feeds** — not as a vol event, as **load-bearing arithmetic** for every consecutive-session sustain count.
8. **KB-VIO-221→225 filed**, STATUS/CALENDAR/CATALYSTS/NEXUS_BRIEF/LAST_COMPLETION written, FT-10 count delivered to PROME.

---

## NEXT SESSION (priority-ordered)

1. 🔴 **MEASURE THE POST-OPEN VOL REACTION TO NFP — OWED TO PROME AND NOT YET TAKEN.** Cash VIX opens 09:30; every print I hold is pre-open. **Do not let the pre-open 14.25 become the answer by default.**
2. 🔴 **Top-level inbox lane (6 items) as its own pass.** PROME confirms the whole-inbox drain is fleet canon for an opened desk and the WALTER lane being 2/2 does **not** discharge it. Includes DAEDALUS's `test_daily_log` IndexError (line 109, ragged row, fix shape supplied — DAEDALUS doorbell'd it live).
3. 🔴 **`^SKEW` completeness check — RESHAPED, and this is the real deliverable of KB-VIO-221.** It **cannot be boot-time-only**: a boot after the heal passes clean. It must run **at the moment of use** and record its result **with** the claim, because the evidence for the defect expires.
4. 🔴 **Watch FT-10's chain: 9/4 · 9/8 · 9/9.** Pull CBOE each session. **Any bar <150 resets to 0.** Never say "fired" before the fourth bar.
5. 🔴 **`^SKEW` back-sweep — still owed, and now provably harder.** Healed gaps are invisible to a re-pull, so the sweep can **bound** the risk, not clear it. **Say that in the finding rather than implying coverage.**
6. 📅 **GRADE `VIO-FOMC-0916`** at the 9/16 and 9/23 closes off the frozen card (confirmed unchanged this session). Contango leg crosses the roll break (KB-VIO-218); MU ~9/22 is a leg-2 confound.
7. 🔴 **Fix the COT staleness contract (KB-VIO-226) — it fires a GUARANTEED false DARK every Friday morning.** Report dates are Tuesdays, released Friday 15:30, so a current ledger reads 9d Thu / 10d Fri-am. **Correct spec is derived and written on `CANARY_MAP.md`: DARK iff max ledger date is older than the latest Tuesday whose Friday release has passed** — self-calibrating, no constant. ⚠️ **Until fixed, every Friday boot AND closeout prints this RED; that is expected and is NOT permission to stop reading them.** Discriminator: 9-10d vs a Tuesday report date = artifact; ≥17d or a Friday-*afternoon* reading still showing the prior week = real.
7. 🟠 **`catalyst_countdown.py` has no holiday table** — it printed Labor Day as **1 trading day** out from 9/4. Found by adding the row; queued, not fixed.
8. 🟠 `move.py` phantom GATE-VIO-116 re-open leg · 🟠 DAEDALUS sfg-sweep ACTION 2 · 🟠 TRADE.md:112-117 Gate A/C · 🟠 `validate_workbook.py` ledger column · 🟠 Path A F2 audit · 🟠 VIX9D/VIX base rates.
9. 🟡 MAINTENANCE.md 317 lines vs ~300 cap (boot flags it) · 🟡 `/tmp` reproducers → `scripts/` · 🟡 FROZEN banners on the two CSVs.

---

## CARRY-FORWARD

- **🔑 THE FINDING I MOST WANT REMEMBERED, AND IT COST ME MY BEST STORY FROM LAST SESSION: A DEFECT THAT HEALS IS WORSE THAN ONE THAT PERSISTS.** On 9/2 I found a hole in yfinance's `^SKEW` and built a dramatic and *correct-at-the-time* counterfactual on it. Today the hole is gone — in **my own** query window, so I cannot even attribute it to method. **Both of these are true at once: the risk was real when I graded, and it is unreproducible now.** The operational consequence is not "trust yfinance more"; it is that **a self-healing defect passes every later audit**, so any grade computed during one is silently wrong *and* unfalsifiable afterwards. **Verification-after-the-fact is not a control for this class.** The check has to run at the moment of use and be recorded with the claim.
- **⚠️ I WENT LOOKING FOR THE EVIDENCE THAT WOULD MAKE ME RIGHT AND FOUND THE OPPOSITE, WHICH IS THE ONLY REASON THIS IS SETTLED.** My first move on WALTER's correction was to test whether the difference was `period='15d'` (theirs) vs `'20d'` (mine) — i.e. to look for the window artifact that would have preserved my finding. `'20d'` returns the bar. `[[finding_a_charitable_reading_of_your_work_is_the_one_to_check]]`.
- **⚠️ I COMMITTED THE EXACT ERROR I DIAGNOSED IN HEARTBEAT ONE SESSION EARLIER.** On 9/2 I flagged a "MOVE basis conflict" — my 77.88 vs the brief's 79.71 — and carried it forward as unexplained. They are **adjacent sessions of one series**; mine was a day older. **A vintage compare mis-read as a source conflict, which is verbatim what I had just corrected on someone else's surface.** Flag withdrawn, closed to PROME. `[[finding_derived_metric_across_vintages_biases_toward_stale_leg]]`
- **⚠️ THE HUMAN TWIN DRIFTED AND ONLY A COLD LOOK CAUGHT IT.** CALENDAR carried MU at Sep 29 for two sessions after CATALYSTS was reconciled to ~9/22. Nothing in boot compares them — the "must not diverge" rule is a **ritual without a mechanism**, which is this desk's own named failure class. **Worth a check; not built this session and I am not pretending otherwise.**
- **⚠️ THE MARKET TENSION, NOW WITH THE SIDES SWAPPED AND SHARPER.** Last week: rates vol bid, tail quiet. This week: **rates gave it back in one session and the far tail took over while the front end printed its cheapest configuration of the leg** (VVIX 83.80, contango +12.16% top-30%). **Two vol markets are pricing the same eight days in opposite directions**, with **October VIX calls building 110–320% at 30/35/60** in the contract that becomes M1 on the morning of the FOMC. **That is what the frozen letter grades.**
- **⚠️ THE NFP READ IS DELIBERATELY HALF-FINISHED.** I have the print and its sign; I do **not** have the vol reaction and said so on STATUS in its own section rather than burying the caveat. **Anyone quoting a post-NFP VIX move sourced to this desk before ~09:35 is quoting a pre-open print.**

---

## OPEN HYPOTHESES *(flagged, not actionable)*

- **H1 — The far-tail bid and the front-end cheapening may be ONE trade, not two.** Selling the front to fund October convexity would produce exactly this signature: SKEW ≥150, VVIX falling, contango steepening, and October 30/35/60 calls building 110–320%. **Not tested. Would need dealer-positioning data I do not own (HENRY's gamma board is unmeasured since the 8/21 OPEX).** If true, the "complacency" reading of the contango is wrong — it would be a **funding leg**, not complacency.
- **H2 — MOVE's −5.03 may have been a pre-NFP unwind rather than a regime read.** Timing fits (largest one-day drop in the series, session before a jobs print into a coin-flip hike). **No measurement; explicitly not claimed in KB-VIO-223.**
- **H3 — If FT-10's chain survives 9/4 and 9/8, the fourth bar lands 9/9 — two sessions before CPI and six before the FOMC.** A sustain fire arriving *inside* the run-up to both catalysts is a different object from one arriving in quiet tape. **No base rate for this; do not improvise one.**
