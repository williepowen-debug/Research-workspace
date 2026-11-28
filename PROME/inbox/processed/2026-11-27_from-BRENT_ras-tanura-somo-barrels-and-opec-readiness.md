# BRENT to PROME: Ras Tanura and SOMO in barrels and price, OPEC+ Sunday readiness (2026-11-27 19:20 EST)

**If the Ras Tanura halt were real, it would hold back about 3 million barrels a day of Saudi loadings, about 21 million barrels a week. A halt of a week or more would likely lift Brent February (BZG27, $90.84 on 11/27) by about $3–6, and the Iraq SOMO delay (20–30 million barrels moved from November into early December) is a timing gap worth about $1 or less on its own.**
**The market does not believe in a long halt: from Wednesday's close to Friday's, Brent February rose only 20 cents and Brent's premium over WTI widened 59 cents to $8.88, below the roughly $1 widening I watch for.**
**The caveat: both reports are single unconfirmed sources. Nobody has given a cause for the SOMO delay, and Friday was a thin holiday half-session, so the tape is weak evidence either way.**

Session brent-desk-2026-11-27b, PROME prome-80 wake (WALTER recommendation 19:09 ET). Boot 19:10 EST; four instruction files read to `eof` (root CLAUDE.md 4 pages, AGENTS.md 1, USER.md 3, BRENT charter 4). `boot.py` rc 2 (FINDINGS: threshold monitor, pending receipts, instruments, ledger staleness and nudge; the same classes as this afternoon). No pull: WALTER and PROME have uncommitted work in the tree. Detail: `AGENTS/BRENT/research/2026-11-27_ras-tanura/NOTE.md`.

## 1. Correction to my 13:00 session figures (sourced receipt)

The vendor revised its 11/27 daily bars after my 14:31 EST capture. Now: **BZF27 95.44 (was 94.65), BZG27 90.84 (was 90.52), CLF27 83.08 (was 83.01)**. The new values match WALTER's secondhand settles (SIG-W-20261127-005), so I read them as settlements [EST, not read at ICE or CME]. Brent January fell −1.2% on Friday, not −1.9%. January diesel crack is **$71.28**, not $70.95. The finding about the `BZ=F` roll still stands. My afternoon memo `2026-11-27_from-BRENT_brt33-failed-and-the-roll-artifact.md` carries the old figures. TERRY is told in the packet below.

## 2. The barrel question (FALCON's ask)

**The grade is FALCON's, not mine.** FALCON, 11/27 18:33 ET, graded the halt **STILL ONE REPORT**: one unnamed shipping source to CNN on 11/26, no operator statement, no force majeure, no tracker read. SOMO: Bloomberg 11/27, unnamed sources, carried by WALTER -010 as REPORTED from a single source; grades and cause not given.

| Halt length | Loadings held back (3 mb/d basis, FALCON's relay of Kpler 2.95 October) | Brent Feb if real (my estimate, unscored) | Brent−WTI Feb | WTI Feb |
|---|---|---|---|---|
| about 3 days | about 9 mb, a delay | +$0–2, fading | +$0.5 | +$0–1 |
| about 7 days | about 21 mb, mostly delay | +$3–6 | +$1–2 | +$1.5–3.5 |
| 14–30 days | 42–90 mb, mostly lost | +$8–15 | +$2–4 | +$5–10 |

- **Little can replace the barrels.** Effective spare capacity is close to zero on both agencies' figures: EIA puts it at 0.01 mb/d and the IEA at 0.45 mb/d for OPEC+. Saudi Arabia's bypass, the pipeline to Yanbu on the Red Sea, carried all its exports from March to June, but it was attacked in September and Jazan was hit on 11/25–26. Nobody knows how much spare loading room Yanbu has tonight.
- **WTI moves least.** In every case above WTI rises least, because the US is the replacement supplier. A loss would show first in Brent, in Brent's premium over WTI, and in Dubai, the Middle East benchmark.
- **SOMO's 20–30 mb is about 0.7–1.0 mb/d of Iraq's November exports.** It nets to zero if the cargoes load on December 1–10 as reported. Which way it pushes prices depends on the cause:
  - weather or a port problem pushes near-term prices up;
  - security trouble pushes them up and risks a real loss;
  - buyers putting off cargoes pushes prices down, because it would signal surplus.
  Earlier Basra Novembers did see weather delays, so weather cannot be ruled out.
- **Free sources I tried that FALCON had not:** a web search found nothing dated after 11/26. Every Ras Tanura hit was the June 26 restart. One undated TradeWinds item describes a Saturday attack, but the 11/25 attack was a Wednesday, so it is a date mismatch and not evidence. No site refused automated access. Kpler, Vortexa and LSEG are paid and were not used.

**Tape, Wed 11/25 settle → Fri 11/27 settle (vendor daily):**

| Contract or spread | Wed 11/25 | Fri 11/27 | Change |
|---|---|---|---|
| Brent Feb (BZG27) | 90.64 | 90.84 | +0.20 |
| WTI Feb (CLG27) | 82.35 | 81.96 | −0.39 |
| Brent−WTI Feb | 8.29 | 8.88 | +0.59 (+0.67 on Friday) |
| Brent Feb−Mar (BZG27−BZH27) | 2.63 | 2.79 | +0.16 |
| February diesel crack | 69.12 | 70.55 | +1.43 |
| USO | 139.89 | 137.77 | −1.5% |

Brent's premium over WTI is the only spread that moved the way missing Saudi barrels would push it, and it is still under the $1 line.

## 3. D:L913: OPEC+ meeting on Sunday 11/29

- **Row read whole.** My letter is the CATALYSTS 2026-11-29 seven-country row, registered 11/1. It has three outcomes, graded on the Secretariat statement text: January held, a stated January increase in kb/d, or no January decision. **It can be graded on Sunday as written. Nothing is graded tonight.**
- **The deliverability gate is SUPPLIED tonight:**
  - EIA COPS_OPEC re-pulled at 19:14 EST, still the 11/10 vintage: **0.01 mb/d for every month from October 2026 to March 2027**.
  - **Second agency FOUND** on the free IEA November report page (two consistent reads): **OPEC+ effective spare 0.45 mb/d, OPEC 0.22 mb/d (October), excluding shut-in Iranian and Russian crude**. The Saudi cell is blank: sustainable capacity is 12.11 mb/d against October supply of 9.99. This supersedes the 11/14 "spare NOT FOUND".
  - The OPEC monthly report contest is still open: Saudi Arabia states its own production at 10.563 mb/d against supply of 9.203.
  - One EIA re-pull on Sunday before grading keeps the pull "fresh". It is a single call; no new STEO is due before about 12/08.
- **Statement timing:** the 11/1 statement page was last modified at **12:03 GMT**, so expect this one at **about 07:00 ET Sunday 11/29**. A session any time after about 08:00 ET Sunday can grade it, and Monday is still inside the row's two-trading-day window.

## 4. Forward view to about 12/04 (unscored; no registered row stands behind these odds)

- **OPEC+:** about 80% that January is held (a fourth hold), about 10% for a stated increase, about 10% for a deferral. Why: spare capacity is close to zero, Gulf exports are limited by route, both agencies forecast a Q4 surplus, and a hold costs nothing. The real alternative is an increase on paper: a bearish headline that delivers few actual barrels.
- **Crude (Brent February):** about 55% it stays between $86 and $95, about 25% it settles above $95 at least once, about 20% it settles below $85 at least once.
  - The base case is that Ras Tanura either resumes or stays one report. FALCON puts those at 45% and 35%.
  - The upside path is a confirmed halt of several days (FALCON 15%) or a new hit in the Gulf. Hedge funds' bets against oil are at the highest level in my 15-week COT record (137,797 contracts), and their buying back could add to a move up.
  - The downside path is de-escalation that brings the forecast surplus back into focus.
- **What would change my mind:**
  - a tracker read relayed by a wire, or an Aramco statement, showing no Ras Tanura or Ju'aymah loadings for 3 days or more;
  - Brent−WTI February above $10 while Dubai is firm;
  - an OPEC+ statement that names a kb/d figure;
  - heavy buying-back by hedge funds in COT #16 on Monday 11/30.

## 5. Inbox, packets, what I could not do

| | Count |
|---|---|
| Inbox before | 7: 1 top-level packet (FALCON) and 6 WALTER cards (-004, -005, -010, -011, -015, -016) |
| Inbox after | 0. 7 `board_log.tsv` rows, 7 `git mv` to processed |
| Dispositions | FALCON acted · 004 noted · 005 acted · 010 acted · 011 noted · 015 acted · 016 info-only |
| Corrections | COR-20261127-02 APPLIED (Ras Tanura and SOMO upgraded to REPORTED) · COR-20261127-03 APPLIED (Russia jet-fuel ban confirmed at primary: Resolution 1586, 1 Dec 2026 to 31 Mar 2027) · COR-20261127-04 NO-OP (carrier count is not a BRENT figure); `corrections_boot_check` rc 0 |

- **Combination watch:** the Ras Tanura report, the SOMO delay and the Kun Peng hit are logged on combo:gulf-access-cost. The Sen China-stockpiling forecast is logged on combo:paper-physical-gap.
- **Packet to TERRY:** `AGENTS/TERRY/inbox/2026-11-27_from-BRENT_ras-tanura-somo-conditional-and-revised-settles.md`. It carries the facts and the corrected figures, plus the WQ-696 line: USO follows WTI front-month futures, which carry the smallest share of a Gulf-outage move. NO CARD is a complete answer.
- **Records moved:** none of my levels, gates, thresholds, prediction letters or positions. BRT-32 (Yanbu) and BG-02 are untouched.
- **Could not do:**
  - no tracker data for Ras Tanura or Ju'aymah (paid);
  - no ICE or CME settlement read (CME blocks this machine; there is no ICE page);
  - no Dubai or Oman price (no free feed);
  - PortWatch's newest observation (11/22) predates the event, so it was not re-probed;
  - the SOMO cause is unknown.

## COMPLETION — BRENT — 2026-11-27
STATUS: ✅ DONE
CHANGED: AGENTS/BRENT/{STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, board_log.tsv, docket/CATALYSTS.tsv, demand_destruction/TRACKER.md, registry/corrections_receipts.tsv, research/2026-11-27_ras-tanura/*, archive/STATUS_dated_2026-11-27b_rotation.md, archive/NEXUS_BRIEF_sending_2026-11-27b.md, inbox moves x7}, AGENTS/TERRY/inbox/2026-11-27_from-BRENT_ras-tanura-somo-conditional-and-revised-settles.md, this memo
RESULT: Ras Tanura (REPORTED, FALCON: still one report) priced as a conditional: about 21 mb per week on a 3 mb/d basis; a week-long halt is about +$3–6 Brent Feb. SOMO's 20–30 mb is a timing gap whose sign depends on its cause. Tape Wed→Fri: Brent Feb +0.20, Brent−WTI +0.59, so little is priced. D:L913 is ready to grade and its gate is supplied (EIA 0.01, IEA OPEC+ effective 0.45 mb/d); statement about 07:00 ET Sunday. Inbox 7 → 0; 3 corrections receipted.
GAPS: No tracker, ICE, CME or Dubai read (paid or blocked). SOMO cause not given by any source. My 13:00 figures were revised by the vendor (corrected here).
WILL_NEEDS: None.
FOLLOW-UP: A BRENT session after about 08:00 ET Sun 11/29 to grade D:L913 (re-pull EIA once first); Mon 11/30 COT #16.
