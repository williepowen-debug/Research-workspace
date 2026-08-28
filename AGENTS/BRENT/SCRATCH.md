# BRENT SCRATCH — Fri Aug 28, 2026 **~11:0x ET** *(PROME-orchestrated Friday slate; markets OPEN; session STILL RESIDENT for the 13:00 rigs print and the 15:30 COT print — this file is written mid-session and gets a second pass at the true close)*

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11). ⛔ **STAMP CORRECTED 2026-08-28 11:0x ET — this file was first written carrying a `~12:1x`/`~12:2x` ET session stamp while the wall clock read `11:0x`. I wrote the timestamp from the SESSION NARRATIVE (how much work had happened) instead of from `date`. `[[finding_write_timestamps_from_the_clock_not_the_narrative]]`, caught by running `date` before the Baker Hughes pre-check rather than by any guard. ⚠️ THE PRICE STAMPS ARE UNAFFECTED AND WERE ALWAYS RIGHT: every `~10:5x ET` tape figure was stamped AT CAPTURE and cross-checks to WALTER's independent `~14:5xZ` pull. Only the SESSION stamps drifted, and they drifted LATE — i.e. they made this work look more recent than it is. Corrected in place, left visible.**

> # ⛔ THE ONE THING TO READ FIRST: `BZ=F` ALONE IS NO LONGER A CITABLE IDENTIFIER ON THIS DESK
>
> **Yahoo's `BZ=F` DAILY and INTRADAY series rolled Oct→Nov on DIFFERENT DATES and disagreed about what "front" meant for three sessions (8/25, 8/26, 8/27).** Daily was `BZV26` through 8/27 and `BZX26` from 8/28. Intraday was `BZX26` from 8/25. **One ticker, two contracts, same moment, depending on which resolution you request.**
>
> **BINDING FROM TODAY: every Brent figure this desk publishes NAMES (a) the CONTRACT and (b) the BASIS — `close` vs `live bar`.**
>
> **Certified endpoint: `BZV26` (Oct26) `$87.84` [8/26 close]. Certified move: `94.39` [8/21 close] → `87.84` = `−6.94%`.** The fleet's `−8.5%` is retired; WALTER concurs and is fixing its own four surfaces.

---

## ✅ WHAT THIS SESSION DID

**① REGIME VERDICT DELIVERED WITH A NAMED CHECKABLE RESOLUTION — the ask owed since 8/26 is now closed properly.** The 8/27 delivery had a verdict and falsifiers but **no dated, gradeable resolution**; that gap is what today filled. **Verdict: `PAPER-PREMIUM UNWIND ON A DEAL PATH; THE PHYSICAL PREMIUM DID NOT UNWIND WITH IT.`** Three independent physical/insurance witnesses (JWC listing = mine · TD3C freight = RED's · event pricing = ORACLE's), plus WALTER's bypass-leg framing as a fourth reason. **Registered `BRT-30`, 80%, resolves 2026-10-26.**

**② BZ 8/26 THREE-WAY ENDPOINT RECONCILE CLOSED — and it retracted one of my own 8/27 claims.** Two defects, neither a desk error: the daily/intraday roll split, and the evening-tick-labelled-as-close. **`−8.5%` decomposes to `−6.94` like-for-like + `−0.95` contract + `−0.61` timing = `−8.51`, reproducing WALTER's figure to the decimal.** **WALTER independently derived the same headline mid-session; I returned one refinement (its live tick was Nov-basis, not only next-session).**

**③ DR-4 RE-RATED — DEWEY's softening REFUTED, and my own `77–80%` superseded as TOO HIGH.** Built a 5-year pace-decay test off 1,913 daily EU AGSI+ observations: the naive-pace method over-projected **5 of 5 years**, median **+14.0pp**. **Seasonally-corrected landing zone `~70–76%`.** The **80% floor needs `0.81×` against a five-year BEST of `0.623×` ⇒ out of reach at 5/5.**

**④ `gie_pull.py` OWNER-WIRE ACCEPTED AND CADENCE INSTALLED** — two `CATALYSTS.tsv` edits, `supersedes: none`, per-boot wire deliberately refused under the retirement ratchet, **limit named rather than papered over.**

**⑤ INBOX DRAINED — 6 items, every sender, board_log rows 258–263.** Includes **ending the DAEDALUS deferral at its 4th re-affirmation** — the content is already verbatim in `board_log` 8/21T12:0x, so archiving lost nothing and un-stuck a rotting inbox slot.

**⑥ FIVE PACKETS OUT** (DEWEY · RED · WALTER · HAWK · PROME), commits `37955e32f` + `fea13a864`. **Doorbelled live: `walter-0828`, `red-96`. DEWEY and HAWK are DARK → flagged to PROME per rule 6b.**

---

## ⏳ NEXT — IN THIS SESSION, NOT NEXT SESSION

> ⛔ **DO NOT SCHEDULE A TIMED GRADE ON A BACKGROUND BASH WAITER IN THIS ENVIRONMENT — MEASURED n=2 TODAY.** Two `until [ $(date +%H%M) -ge … ]; do sleep; done` background waiters armed for the 13:00 rig print were **KILLED, not fired** (11:05→11:27 and 11:27→11:35 — **different durations, so it is not a timeout**; each died around a session turn boundary). Their output files contain only `[killed]`; **there is no error and no signal until the task notification arrives.** ⚠️ **A reaped waiter is worse than no waiter, because you stop watching for the thing yourself.** ✅ **What replaced it:** a **persistent Monitor** polling the BH primary every 4 min and emitting on a **HASH CHANGE** — i.e. on the report actually posting, not on a clock — plus fetch-failure lines and a periodic still-unchanged heartbeat, **so silence is never ambiguous.** ✅ **And the real backstop needs nothing running: the `2026-08-28` Baker Hughes row in `docket/CATALYSTS.tsv` is self-contained** (URL, the `urllib`-not-`curl` warning, a runnable one-liner executed in its published form, ladder, direction, hash guard) **and Catalyst Countdown prints it at every boot.**


| when | what | state |
|---|---|---|
| **~13:00 ET today** | **`BRT-26` Baker Hughes.** Direction verified: `above 457`, **fails on a RISE.** Ladder …455 (8/14) → **452 (8/21)**, distance **5**. Locator: probe URL as `.xlsx` → `NAM Summary` → `U.S. Breakout Information` → `Oil` → `This Week`. **Browser UA** (the host tarpits a self-identifying one). **Never** a digit-regex on the BH HTML. **Two independent pulls.** | **PENDING — NOT PRE-GRADED** |
| **~15:30 ET today** | **COT vintage #3, as-of Tue 8/25.** `COT-FUEL-35B`: Leg A ≤113,745 / deadband 109,165–118,325 · Leg B ≤4.909% GATING · both must agree. Ladder **108,059 / 5.7206%**. RAW `f_disagg.txt`, never Socrata; query by market NAME; verify `report_date` IN-ROW; `cot_grade.py --expect 2026-08-25`, **exit 3 = WAIT**. | **PENDING — NOT PRE-GRADED** |
| **at the true close** | **Second pass on this file + `NEXUS_BRIEF.md` + `STATUS.md` grade rows + `CATALYSTS.tsv` 8/28 rows updated from ⏳ to ✅ + prune the 8/17 and 8/21 fired rows past 1-week retention.** | owed |

### 🔧 GRADE PATH — SETTLED, AND IT IS THE PART A COLD SESSION NEEDS

**Run the URL PICKER FIRST at every rig grade, not only if a monitor is silent.** Full runnable recipe (HEAD-only, 11 requests) lives in the `2026-08-28` Baker Hughes row of `docket/CATALYSTS.tsv`, **verified in its published form**. ⛔ **PICK BY THE DATE IN `content-disposition`, NEVER BY LINK TEXT — `na-rig-count` lists 10 uuids including `e98bcf83`, the YEAR-STALE archive that cost this desk a month on 8/14, and BOTH link texts say "New Report."** The picker also **self-validates the registry probe** every run.

**Trigger stack for today's 13:00 print (5 nets, 3 of them uuid-independent):** PROME 13:02 clock wake *(the guarantee — now carries the picker rule)* · PROME hash monitor · BRENT hash Monitor · the in-page **US total `588`** on `rig-count-overview` *(⛔ TRIGGER ONLY, never a grade source — total ≠ oil leg; 8/14 was total +5 / oil +1)* · the self-contained catalyst row. ⚠️ **Both hash monitors share ONE untested assumption — that `6f748ddc` updates in place; n=0 observed transitions. The picker and the `588` signal are the nets that survive a uuid rotation.**

### ⚑ ADOPTED THIS SESSION — HENRY'S ROUTING OBLIGATION (supersedes my "no fix exists")

**When my own instrument disagrees with a publisher of record: the cell carries BOTH figures with BOTH bases named, AND the disagreement is routed back to that publisher the same session.** Deferring silently is what turns a caught error into a propagated one. ★ **I had concluded "no note fixes this" and stopped — a correct negative read as "nothing fixes this." The remedy was a ROUTING obligation, not a note.**

### ⚠️ `STATUS.md` IS 229% OVER THE ~54,250 B READ CAP — AND EVERY LINE CHECK PASSES

124,233 B / 158 lines = **786 B/line**; **64% of the 250-line cap.** My 8/28 narrative was rotated verbatim (`workbook/STATUS_archive_20260828_session_rows.md`, `crc32 f8cc283a`, −23,312 B) but **the file was already 208% over before this session** — the rest is the **Will-gated** second half of DAEDALUS's two-commit plan (byte-tier from measured density, then boot-wired). **Returned to PROME; do not cut further without the ruling.** ⛔ **A `cat` of this file truncates — read it in slices.**

## 📌 NEXT SESSION (dated, future-verifiable)

1. **Sun 8/30 — Jazan refinery restart** (400 kb/d, shut 7/27, date revised 8/15 → 8/30). Verify at a primary; log to `INCIDENTS.tsv` only on facility evidence.
2. **Tue 9/1 — Russia diesel ban, producer-direct carve-out takes effect.** Grade against the INSTRUMENT (the decree), never a minister's forward guidance — that error is on my record from 7/31.
3. **Sun 9/6 — OPEC+ Q4 decision.** Grade against the STATEMENT, not delegate sourcing (the 8/2 error). Per LESSONS #10, grade any adopted number against DELIVERABILITY: effective spare ~0.02 mb/d makes a quota change close to a paper event either way.
4. **Wed 9/9 — SPR exchange window test**, first EIA prints covering September.
5. **~8/31 — `BZV26` EXPIRES.** M1−M3 on the V/X/Z legs dies with it. **Successor basis already recorded so the series does not silently change definition: `X26−F27 = +$4.32` [8/28 ~10:5x].** Do this BEFORE the next curve write, not after.
6. **`INCIDENTS.tsv` re-verify queue: 12 ACTIVE rows past the 60d budget** (oldest RF-004 at 162d) **+ 6 present-tense rows the budget does not cover.** Flags only — downgrading on a timer would fabricate a restart nobody observed.
7. **`CUSHING-20M` instrument STALE** — newest datapoint 8/13 is 15d old against a 10d budget. *(The EIA weekly monitor separately reads 22.43M for wk-8/21, so the SERIES is fine; it is the registry row's freshness path that is stale. Diagnose the path, do not re-level the row.)*

## 🔓 OPEN THREADS

- **⚠️ WILL-GATED, UNCHANGED, NOW FOUR SESSIONS OLD: the `TRADE.md` half of the boot-load cut (five sections left) + the byte-tier declaration and boot wiring.** DAEDALUS's addition #3 says archive and guard are TWO commits; **only the archive half landed (8/27).** **`STATUS.md` is now 128,824 B / 159 lines — comfortably under the LINE cap and that is exactly the disease DAEDALUS measured: archiving by line count does not reduce bytes when retained lines are heavy.** The packet is now in `processed/`; **its load-bearing breakage mapping is verbatim in `board_log` 8/21T12:0x** — read it there, not from the archived file.
- **TERRY: the decoupling-vs-XLE falsifier slot is NAMED BUT EMPTY on a FILLED position** (3× VLO, Will-approved ~12:1x on 8/27). TERRY ruled the urgency INVERTED — an empty falsifier on a filled position outranks one on a conditional position. **Still the top open item between us.** No threshold nominated to Will; `+8.55` sits mid-distribution (p25 3.07 ≤ 8.55 ≤ p75 9.78) on the ruled calendar-30d basis.
- **Row 58 / USO shares leg:** LEG A (profit-keyed) with a ratchet remains better calibrated than any thesis-break instrument I can name at a defensible base rate. Unchanged today.
- **S338 Canadian energy-lines status = UNKNOWN-AT-PRIMARY** (PROME ruling). Carry the framing; assert neither inclusion nor exclusion. Counter-tariff date **Tue 9/8**.
- **Energy HY OAS: PERMANENTLY UNMEASURED** on this desk (`HY-ENERGY-OAS` retired 8/07, no free feed, substitution refused). LIQUID's 6/30 183bp is the fleet's freshest. Systemic-credit leg formally deferred to LIQUID.

## 💼 PENDING POSITION DECISIONS

**NONE PROPOSED TODAY. `$0` moved.** Book unchanged: **USO 35 shares · USO Oct-16 135C ×2 · USO Sep-18 150/165 spread · XLE Sep-30 65C ×2** *(`TRADE.md` is canonical; marks were NOT refreshed this session — a live-chain pull at every decision point is RISK_RULES #5 and no decision point arose)*. **TERRY's concentration flag reads the same as 8/27: the falsifier is MOVING, not FIRED — and §A's three physical witnesses are the evidence for that distinction, because a genuine break would show in the JWC listing and the freight tape first, and neither has moved.**

## 📬 MAIL STATE

**Inbox EMPTY of actionable items except two WALTER artifacts left in place deliberately** — both untracked in git at ~11:0x, therefore WALTER's to commit under carve-out ①; consumed and logged (board_log 2026-08-28T11:4x ×2), **archive to `processed/` once they are tracked.** Four items `git mv`'d to `processed/` this session. **Outbox: nothing pending.** Five packets delivered today (DEWEY · RED · WALTER · HAWK · PROME).
