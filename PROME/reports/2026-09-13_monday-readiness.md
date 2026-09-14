# Monday readiness — the slate is over the cap, and the Friday close moved three things

**Written:** 2026-09-13 20:2x ET (Sun, markets closed since the Fri 9/11 close) · **Author:** PROME, session `prome-27`
**Scope:** what Monday 2026-09-14 owes, who owns it, and what the Friday close changed. **$0 moved. No gate graded. No trade proposed. STAND DOWN (WQ-192) holds.**
**Canon:** `PROME/DOCKET.tsv` owns the dates · `PROME/GATES.tsv` owns gate state · `PROME/WILL_QUEUE.md` owns Will's list. This report points; it does not become a second copy of any of them.

---

## 1. The headline: Monday is over the spawn cap

**Six desks own dated 2026-09-14 work. The WQ-184 L0 cap is four spawns per boot.** Anything past four is a slate for Will's word — which is what this section is.

Darkness below is the desk's own last self-commit, read from git subjects, as of Sun 20:2x. Inbox counts are `PROME/tools/inbox_census.py`, files only, lanes separate — never `ls | wc`.

| Rank | Desk | Dated Monday work | Dark | Inbox | Why this rank |
|---|---|---|---|---|---|
| **1** | **TERRY** | **L356** — grade the 004 add line on the card's own letter | 2d (9/11 15:12) | 6 · WALTER/1 · WILL/2 | 🔴 The only capital-adjacent row. `DFII10` **2.55 [9/10 official]** is **THROUGH** the 2.50 add line for the first time in the position's life. Two further TERRY items land the same day: TERRY-007's 9/10 cell is gradeable now (DGS10 **4.95**, still 45bp from the 4.50 exit) and **L254's WAL <$71 re-open window opens Monday** — TERRY pre-registered it, and it is the only pre-registered condition in the book whose window opens this week. |
| **2** | **BOND** | **L357** — grade `BND-22` | **3d (9/10 18:12) — the darkest dated owner** | 3 · WALTER/6 | 🔴 A registered 55% prediction that **resolved FALSE on the 9/10 close and still reads `Status = OPEN`**. An ungraded resolved prediction is a calibration loss that cannot be recovered later. ★ **Pair it with TERRY, same day, deliberately:** TERRY's card says a 2.50 **add LINE** (a level) and BOND's thesis says **≥2.50 SUSTAINED**. That disagreement is outcome-determining and PROME did not pick. It resolves cheapest with both reads present. |
| **3** | **DAEDALUS** | **L285 · L348 · L349 · L354 · L355** — five rows | 1d (9/12 18:21) | **18** | Two are 🔴 instrument-integrity defects the whole fleet's checks run on: **L355** — `validate_all` D1 handles rc 2 but **rc 1 still becomes PASS** (a false green, carried 9/12 with written conditions); **L354** — a false **RED**, the `.py`/`.sh` advisory now drives fleet rc 1. **L285** is the ladder-integrity sitting; PROME consumes it and **WQ-181 ② goes to you out of it**. |
| **4** | **RED** (+ WALTER doorbell) | **L341** VX.tsv re-review · **L344** `state`/`state_detail` schema split | 1d (9/12 16:22) | 11 · WALTER/1 | **L344 cannot ship without WALTER's co-signature** — `state` is a column WALTER's scan executes on. RED pushed L341 from 9/12 **with a written reason rather than silently**, which is the behaviour we want and the reason it is ranked rather than chased. WALTER is 1d dark; a doorbell, not a fifth spawn. |
| — | **HOMER** | **L331** full session — every print since 8/23 **unchecked** | 2d (9/11 11:33) | 1 | **SLATED, past the cap.** Real backlog (GSE Jul+Aug MF monthlies, Trepp Aug), but no dated market consequence lands Monday. Also carries two firetime flags of its own: a dead `thesis/THESIS.md` pointer and a 2026-12-02 date matching no docket row. |
| — | **FALCON** | `GATE-FALCON-001` **`review_by` 9/14** | 2d (9/11 19:49) | 2 · data/1 | **SLATED, past the cap.** The 9/14 date was owner-set because the **Yanbu weekly loadings print lands there**. Legs 1+3 FIRED-and-holding; leg 2 is open and **ungraded on basis** (no TankerMap like-for-like read). ⚠️ Its FIRMS instrument is dead on this box — see §4. |

**PROME's recommendation: 1–4 as ranked, HOMER and FALCON to your word.** The case for swapping FALCON in ahead of RED is the Yanbu print; the case against is that leg 2 has been ungradeable on basis for a week and a print does not fix a missing like-for-like read.

---

## 2. What the Friday 9/11 close changed — three things, with their numbers

The 9/11 panel existed on **no PROME surface** until tonight. It is now on `HEARTBEAT.md` §Stress dashboard.

**① The vol event-bid decayed exactly as VIOLET said it would.** VIX9D **17.70 → 14.47 (−18.2%)** · VVIX **102.66 → 91.28 (−11.1%)** · VIX **17.84 → 15.84** · VIX6M **21.17 → 20.39**. The front decayed hardest and the tenor structure is back in contango. VIOLET called the 9/10 spike an **EVENT bid, not a regime re-rate** (VECTOR-2, delivered 9/11, verdict *vol NOT cheap*, structure DECLARED NONE) — Friday is the confirmation. ⛔ **This does not re-open VECTOR-2.** It is an input to VIOLET's own F-B grade at the 9/16 close. FT-10 (`^SKEW` ≥150) is **1-of-4** on a run that opened 9/11 at 154.49; sustain 4 ⇒ **earliest fire Wed 9/16**, which is FOMC day and the VIX SOQ.

**② Brent settled DOWN 2.81% on the day the Saudi state said the Petroline is shut.** BZX26 **$107.63 → $104.61** · BZF27 **$98.36 → $95.69** · **M1−M3 +$9.27 → +$8.92**. Flat price and the curve moved the same way; that is not a destroyed-capacity repricing. ⛔ **It does not grade BG-02** — that letter reads throughput, not price, and the verdict is BRENT's. Its value is that it is **independent of the AIS resolver BRENT itself reported as defective** (WQ-234: an 0.8 mb/d vendor spread on a 0.7 mb/d floor, biased toward firing). Packeted to BRENT with one ask and no proposed instrument. ⚠️ The Sunday $107.33 print is an electronic session, **not** a settle.

**③ WQ-213 still cannot fill, and Friday was the exact inverse of its condition.** ⚠️ The gate is **RELATIVE, not absolute** — your own words are *"a day the refiners are RED AGAINST OIL"*, and a day-colour read is a MOMENT property that expires with its session (TERRY, `RISK_RULES` #14). At the 9/11 close **VLO +1.29% while USO −2.20%** — refiners green, oil red, the inverse of the condition, the same direction TERRY measured intraday on 9/11 (VLO +2.68% / MPC +3.49% vs USO −3.08% at 10:11). Your 9/10 approval stands, the fresh re-arm is **$1,187.31**, and the hands are owed but **not blocked** — **the gate is the day's colour against oil, not your decision.**

**④ Two claims died after this report's first draft, both surfaced by HENRY at a PROME L0 spawn the same evening.**
- 🔴 **The ULSD crack NEVER took out its 2022 peak.** HENRY corrected its own live headline: **$110.87 was an OVERNIGHT bar read against a 2022 CLOSE.** Close-to-close the 2026 peak is **$109.93 [9/10]**, short by **$0.40** of $110.33 [2022-04-28]; last close **$108.24 [9/11]**. ⚠️ *(An intraday-to-intraday comparison was dropped from this brief: 2022's figure is built as HO's high × 42 minus CL's low, which never traded as a simultaneous print, so it is not an observed crack peak and quoting it re-mints a basis mismatch inside the sentence fixing one.)* and *"+23.0% since 7/23"* was mixed too — **+21.9%** close-to-close. PROME recomputed `HO=F×42 − CL=F` independently and reproduced 109.93 / 108.24 / 90.16 exactly before encoding. ⛔ **The MECHANISM survives and HEN-46 is unaffected** — it rests on the level, never on a record. The superlative is dead and is on the kill-on-sight list.
- 🟠 **SPX gamma has flipped NEGATIVE into FOMC and quarterly opex.** Flip band **~7,671 (14d) / ~7,673 (35d)** — two horizons agreeing to 2pts — against spot **7,656.98 [Fri 9/11 CLOSE]**: **14.0pts / 0.183% below the 14d flip, 16.0pts / 0.209% below the 35d.** Sign was POSITIVE on 9/4. ⚠️ *(The $B net-GEX magnitudes are omitted here deliberately — HENRY's report calls them assumption-dependent and not SpotGamma-grade, and they are the least robust figure in the read. The sign and the flip band are the robust ones.)* ⚠️ **HENRY's own frame, and it is the right one: read it as ON THE FLIP, not as a regime** — SPX moved +0.86% on Friday alone and there have been **three sign flips in eleven sessions**. ⛔ **Both walls WITHHELD** — 7,700 appears as BOTH the put and the call wall at both horizons, and that tie is exactly why neither is publishable. **Do not publish a wall level this week.** ⛔ **SHELF LIFE IS ONE SESSION (HENRY's own measure): do NOT carry this board past Monday's close without re-running it, least of all through 9/16 or 9/18.** VIOLET is unblocked **on the sign only**; the OI term breakdown its hypothesis needs is not producible on the free tier.

**And the thing that did NOT change, which is load-bearing:** **the FRED 9/11 officials have still not published.** Verified at the primary tonight — frontier is **2026-09-10** on DFII10, DGS10, DGS30, DGS2, BAMLH0A0HYM2, BAMLH0A3HYC, three days after the print date. **Every gate reading an official close is frozen at the 9/10 cell**: TERRY-007 (0-of-5), the 004 add line, BND-22. No gate advanced Monday-ward and none could.

---

## 3. The week, in the order it lands

- **Mon 9/14** — the six rows in §1 · `GATE-FALCON-001` review.
- **Tue 9/15** — FOMC begins · `GATE-OSPREY-001` and `GATE-FERT-G3` reviews · L303 PREDICTION_DISCIPLINE canon encode (**PROME writes**) · L316 BOND 20Y-R dual print · L308 OSPREY objection window closes · L335 external-audit F2/F3/F4 (**PROME**) · **WQ-229 and WQ-230 needed-by**.
- **Wed 9/16** — 🔴 **FOMC decision 2:00 PM ET, carrying the SEP and the dot plot** (L125) · VIO-FOMC-0916 legs 1/4/5 grade on the close (L276) · **FT-10 earliest fire** · WPSR = the SPR two-print test's second print (L318) · FERT-G5 (L310) · TERRY-007 weekly review · L350 five desks over read budget.
- **Thu 9/17** — BOJ MPM opens (L34; **Sep hike 98% priced**, so the only surprise left is a HOLD, which is yen-negative) · P4 sitting (L282) · **BG-02 earliest gradeable**.
- **Fri 9/18** — **~$6.2T of US options expire** ⚠️ *(INFERRED from a search extract, not an OCC/CBOE aggregate — the direct path 403s; HENRY 9/13)* · **CRMT scheduled termination date** (L343, the second short bridge) · COT-35B vintage #6 · Sep-18 expiry cluster (L254: WAL 67.5P + 70P LAPSE) · BOND FR2004 join unblocks **WQ-157 leg ②** (L271) · **WQ-234, WQ-225 and WQ-213 needed-by**.

---

## 4. Two things that need your hands, not a ruling

- **Three API keys are missing on this laptop and have been since 8/7** (`FFIEC_CDR_TOKEN`, `FFIEC_CDR_USERNAME`, `FIRMS_MAP_KEY`) — **WQ-238**, needed-by 9/19. This is not abstract: **FIRMS is the hotspot instrument FALCON and OSPREY grade strike claims with**, and FALCON's gate reviews Monday. `env_doctor` reports UNAVAILABLE at every laptop boot and it withholds the dependent claims rather than guessing.
- **WQ-187 is past its needed-by** (9/12; you approved it 9/10 11:18). The row closes when the first digest posts and the hands owed are a PAT and a bot token.

---

## 5. Found while building this, not by any instrument

- **DOCKET L129 was a live 9/18 expiry catalyst for a position that no longer exists.** You closed the RH USO 150/165 Sep-18 call spread by hand on 9/10 for **+$330 (+110%)**; L129 still read `PENDING`. Verified at `FORGE/STATUS.md`'s Robinhood table before resolving — the struck row, the proceeds cell and the 16:10 capture basis all agree, as do ACTIVE_DECISIONS and HEARTBEAT §Book. **Resolved.** It would have fired Friday against nothing.
- **L254's live half was about to go unread.** The USO leg inside it is spent with the spread, but **WAL $70P's re-open condition — "WAL closes <$71 any day in the week of 9/14" — has its window open Monday.** WAL closed **$79.29 [9/11]**, so it is **$8.29 above the $71 line = 11.7% of the line** (10.5% on the close basis; the two differ, so the basis is named): a distance, not a forecast, and TERRY owns the read. The row is re-read and both facts are on it.
- **MARCO's half of the FL joint touch never ran** → **WQ-243**. CORAL delivered 9/13 and packeted MARCO; L332's deliverable is **one reconciled Florida figure**, so a delivered half leaves the row PENDING. MARCO is **10 days dark** with 4 inbox items. PROME is fenced from spawning it by your own 9/11 word recorded on the row.
- **VULCAN's L330 had ridden two boots invisibly.** The 9/12 sweep took its row set from the DARK-owner print and VULCAN was not dark. Spawned tonight under WQ-184 after a same-minute `ListAgents` preflight and a consumer read of VULCAN's own STATUS.
