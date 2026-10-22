# Catching the system up to live data — spawn plan and priorities, Thu 2026-10-22

**Written 2026-10-22 10:57 ET · PROME session a5be8f8c (desktop) · for Will, on his ask *"generate a report on what agents should be spawned and where our priorities should be."*** Evidence: the 10:40 ET gate run (/tmp/prome-boot-a5be8f8c), the one dashboard pull 10:40 ET, a per-desk git census (last commit touching each desk, last STATUS commit, unfiled inbox files), GATES review dates, DOCKET due rows, and HEARTBEAT amendments #1–#2. WALTER is live in Will's own window (walter-f1, started ~10:52 ET) and is NOT in this plan; it routes for whoever we wake.

## 1. Where the system actually is

The fleet is less stale than the git failure made it feel. Of 38 desks with a STATUS file (41 folders, minus the three dormant/retired ATHENA · SENTRY · YEYOU), 34 had a commit touching the desk folder on or after 10/20 and 20 on 10/21 or 10/22 (basis: `git log -1 --format=%ad --date=short -- AGENTS/<NAME>/` at HEAD 342883532, 10:5x ET; ARGUS's re-count at a later HEAD gave 38/36 by folder and 35/29 by STATUS-file commits — the census moves with the morning's commits). The 10/21 evening and late sessions (8 Will-launched war desks + 13 PROME spawns) and this morning's 3 wakes did the catch-up. Three folders are dormant or retired by roster (ATHENA 3/14, SENTRY 9/24 dormant, YEYOU retired 9/5) and must not be woken.

What IS stale, ranked by how much it matters to the book:

| Gap | Vintage | Why it matters | Who closes it |
|---|---|---|---|
| **Broker book** | 10/20 10:43 ET intraday capture; marks 2d old; QQQ Oct-22 715P ×1 is in the book | Every card, every "exposure" line reads from this | **Will's capture** (his hands) → ANVIL reconcile |
| **Regime memo (HEARTBEAT)** | base 10/19 + am.#1 10/21 12:01 + am.#2 10/21 21:0x; no 10/22 cell yet | HY 327 [10/21] after 333 [10/20] = whether the >320 run is 5 of 5 or reset; gamma flipped NEGATIVE 09:53 ET; Brent Dec $111.37 [10/22 10:40 ET vendor]; VIX 18.62 | **PROME am.#3 tonight after the cash close** (no spawn) |
| **Today's deciding prints, ungraded** | EGBN Q3 (printed 10/21 after close, call 10:00 ET today) · CRMT 8-K of 10/21 (bridge extended to 11/01) · HBAN Q3 today · SPX close vs ~7,650 at 16:00 | EGBN decides RED's CHG-027; CRMT decides BROCK L652/L740 (private credit; APO Dec-18 95P in book); SPX close decides the put-wall break (QQQ exposure) | RED · BROCK · GIBBS · HENRY |
| **Will's own question, unanswered** | WALTER dispatch 005 at 10:06 ET today: the HY-to-CRE / regional-bank question → REGINALD, CREED +4 | The book holds OZK 40P ×4, WAL 65P ×4 + 70P ×2, KRE 67P/60P/65P ×11, ZION 62.5P ×2 — the regional-bank put stack is the largest options exposure; REGINALD's SSB Q3 grade (GATE-REG-27) is also due 10/23 | **REGINALD** (CREED only on Will's explicit word, WQ-478) |
| **Credit desk on the 10/22 cells** | LIQUID last grade 10/21 b20fb4fa9; WALTER 004 (gamma negative × HY 333) is an ACTION line in LIQUID's inbox since 09:53 ET | HY run count, LIQ-069/076/079 reviews 10/30; the credit-to-equity read is the one owner read that joins today's two moves | LIQUID |
| **Trade construction backlog** | TERRY last self-commit 10/20; 8 unfiled packets (oldest 10/20): BRENT December-leg observations + diesel crack-path card input, VULCAN CRWV card delta, HENRY HEN-46, PROME OZK Stage-1 grade, two BOARD-gap packets | You asked (10/20) for help on NEW positions; TERRY is the only desk that turns the above into NOT-FIRED cards | TERRY, after the desks above return |
| **Tomorrow's dated set** | FLG Q3 print (FLG is REGINALD's 🔴 6, the top of its bank list) · AXP Q3 07:00 (GIBBS L779) · VULCAN two P1 readings (GPU-rental panel #7; mag7 post-close) · WATT L789 PJM touch (71.5 GW outages) · NEXUS WQ459-HY review + L751 · BRENT COT-35B review · OSPREY L718 (expected NOT MET) · YURI 10/23 read · BROCK L743 CABO | all due Fri 10/23 by DOCKET or GATES date | FLG · GIBBS · VULCAN · WATT · NEXUS · BRENT · OSPREY · YURI · BROCK |

Fresh enough to leave alone (committed 10/21–10/22, nothing due before 10/26): LABOR (today), WATT (today, touch tomorrow), AEOLUS (today), HANS, FALCON (review 10/28), HAWK, OSPREY (10/23 is a grade PROME can read), YURI, VIOLET, VULCAN (until tomorrow), WAL, CARL (10/26), CORAL (10/26–29), MARCO (10/28), FERT (10/26), MIDAS (10/26), SAM, ZHAO (10/27), SHADE (10/28), CRUISE (10/27), CREED (waits WQ-478), BOND, HOMER, OTTO, DEWEY. DAEDALUS has 10 unfiled packets but every one is process work; the process ceiling says domain first, so it waits.

## 2. The spawn plan

**Rules applied:** WQ-184 (a registered due row naming a dark owner is the nod; cap 4 per boot, 8 under C6 when every wake is on a due catalyst/review row) · desk spawns on Opus (Will 9/17) · each spawn drains the desk's whole inbox · ListAgents same-minute before each launch (walter-f1 is the only live peer now) · Claude usage for today is UNKNOWN → one ask (WQ-481).

### Today, in order — 4 sessions (inside the WQ-184 cap)

| # | Desk | Row / basis | What it returns | When |
|---|---|---|---|---|
| 1 | **RED** | D:L35 (DARK, due today) | EGBN Q3 bank-tree grade on CHG-027's pre-registered branches; FT-10 SKEW read; inbox 1 (CARL CRL-29) | now |
| 2 | **BROCK** | D:L740 + D:L652 (due 10/22 and 10/21) | CRMT seventh-bridge grade AT the 10/21 8-K (extension to 11/01, ABS 2024-2 redeemed); backstop #4 final; inbox 3 (GIBBS NDFI figures, VULCAN L782 weak links, PROME 8-K packet) | now |
| 3 | **REGINALD** | WALTER 005 = your question (your word in chat is the nod); GATE-REG-27 SSB grade due 10/23 | the HY-to-CRE / regional-bank answer in REGINALD's letter; SSB Q3 grade; HBAN Q3 comp read (GIBBS summons names REGINALD); inbox 3 | now, on your word |
| 4 | **HENRY** | D:L787 (due today, after the close) | did SPX close under ~7,650 (break) or hold; gamma board refreshed from the close; inbox 1 | after 16:00 ET |

### Tomorrow morning — the Friday set (up to 8 under C6; all on dated rows)

In order: **FLG** L522 after 06:00 (its Q3 frame is written; grade against it) · **GIBBS** L779 AXP 07:00 + HBAN carry · **VULCAN** two P1 readings + CRWV card input · **WATT** L789 · **LIQUID** (HY run count on the 10/22 cell, WALTER 004 ACTION, three gate reviews 10/30) · **NEXUS** L751 + WQ459-HY review · **TERRY** last, consuming all of the above into cards (NOT-FIRED allowed, your rule of 10/20) · **BRENT** COT-35B review 10/23 if the COT publishes. OSPREY L718 and YURI's 10/23 read PROME reads at the artifact (both owners graded 10/21; their rows say what the result will be).

### Not spawned, and why

OZK (L520 ACTIVE: Stage-1 graded 10/21, call read owed by 10/31) · CREED (your explicit permission only, WQ-478 open) · DAEDALUS (process, 10 packets, behind domain work) · the war desks FALCON/HAWK/OSPREY/YURI (graded 10/21, next reviews 10/23–10/28, PROME reads) · dormant/retired ATHENA/SENTRY/YEYOU.

## 3. PROME's own catch-up (no spawn, no usage)

1. HEARTBEAT amendment #3 after the 16:00 close: HY run status, gamma flip, Brent Dec $111.37 [10/22 10:40 ET vendor], VIX/MOVE, today's owner grades as they land.
2. Spine audit #17 becomes due tomorrow (stamp 10/15).
3. Reconcile FORGE on your next capture (ANVIL), which also closes the QQQ Oct-22 715P and the OZK/WAL approved-sale rows one way or the other — from the capture, never inferred.
4. The L600 ranked process table before Sun 10/25.

## 4. What needs your word

- **WQ-481** — the day's Claude usage for the four sessions above (RED · BROCK · REGINALD · HENRY-after-close), then the Friday set tomorrow. If you open any of them in your own window, say so and I direct it there instead of spawning.
- A fresh broker capture when convenient (hands, not a decision).
- WQ-478 if you want CREED on the 10/28 auction or the Trepp October print.

---
*Corrected 2026-10-22 12:17 ET (PROME, on ARGUS ❌): Brent Dec was printed "11.37" twice — an unquoted heredoc dropped the `$1` — the pull was $111.37 at 10:40 ET; three expiry clauses were struck (USER.md § No expiry nagging). The commit history holds the first text.*
