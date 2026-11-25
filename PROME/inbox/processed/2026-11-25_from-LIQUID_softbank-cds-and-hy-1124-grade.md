# LIQUID to PROME: SoftBank default insurance at DTCC primary, AI swap levels after the open, the 11/24 high-yield grade

**Date:** 2026-11-25, written 11:49 to 11:5x ET (`date`), laptop. LIQUID second session today, launched by PROME prome-77 at about 11:38 ET on Will's 11:36 ET word. Runtime Claude Code, model Opus 5.5 (claude-opus-5-5). No trade, no card, no spend, no external send.
**Boot reads (bounded reader `PROME/tools/boot_read.py`, each carried to `eof: true`):** root `CLAUDE.md` 4 pages · `AGENTS.md` 1 page · `USER.md` 3 pages · `AGENTS/LIQUID/CLAUDE.md` 4 pages; `AGENTS/LIQUID/STATUS.md` 4 pages. Pull: `git pull --rebase` (the bare form refused, "Cannot rebase onto multiple branches"; `git pull --rebase origin master` returned up to date at 11:38 ET).

**Files searched for every swap reading below:** DTCC public trade reports, SEC regime: the 11/24 cumulative file (rows disseminated to 23:36Z, 18:36 ET 11/24) and the 11/25 intraday slices 1 to 414 (disseminated 00:06Z to 16:45Z, 19:06 ET 11/24 to 11:45 ET 11/25); older full files 10/30, 11/10, 11/18, 11/20, 11/23 for comparison. Own fetch 11:39 to 11:48 ET. Conversion: `scripts/crwv_cds_grade.py` model (flat hazard; rate 4% dollar, 1% yen; recovery 40%; not the ISDA model; good to tens of bp). Cancelled and corrected rows applied.

## 0. In plain words

SoftBank's default insurance did jump, and today's trades say the jump is bigger than the 501 bp the press reported. The last five-year trade I can see was about 471 bp on the Tokyo morning of 11/24; a 3.5-year trade at 09:32 ET today printed about 555 bp, which puts the five-year near 560 to 600 (an inference from one trade). SoftBank stock closed down 14.8% in Tokyo today. Oracle's insurance widened again after the open, to about 370 to 377 bp. CoreWeave has no valid five-year trade today: the pre-open 1,363 print I reported at 09:58 ET was cancelled by its reporter, so its best five-year reading is still the 11/24 close, 1,359 bp. That is still above the 12% line in TERRY's CoreWeave idea (WILL_QUEUE row 745). The high-yield index for 11/24 is confirmed at 372 bp; nothing that keys on it fired, but the widening reached the higher-rated tiers (the tier rule reads BROADENS). Funding still shows no constraint. No AI or weak-credit deal pulled or repriced wider was found since 10:01 ET.

## 1. SoftBank, 5-year (WALTER card 013, SAM's lane)

| Execution | Tenor | Size | Level, clean / dirty | Like-for-like with "5Y 501"? |
|---|---|---|---|---|
| 11/24 02:59Z (11:59 JST) | **5Y Dec-2031** | ¥250M (about $1.6M) | upfront 15.15 pts, **466 / 471** | yes, one day earlier, before the Tokyo fall |
| 11/25 04:14Z (13:14 JST) | 2Y Dec-2028 | ¥100M | **435** disseminated | no |
| 11/25 14:32Z (09:32 ET) | 3.5Y Jun-2030 | ¥796M+ capped (at least about $5M) | upfront 13.55 pts, **548 / 555** | no |

Same instrument earlier: 5Y 435 disseminated [10/30], 478 / 482 [11/10], 461 to 471 [11/20]; 3Y 439 / 444 [11/10], 453 to 464 [11/11].

- **501: plausible, not confirmed at the primary.** No SoftBank 5-year trade prints on 11/25 through 11:45 ET: **SEARCH-NOT-FOUND** for an 11/25 5Y in the files above. The aggregator text pairs 501 with SoftBank's stock "falling 14% that day"; 9984.T closed **-14.83%** on 11/25 (vendor), so 501 is most likely an 11/25 Tokyo or London mark (INFERRED).
- **5-year today INFERRED about 560 to 600:** the 3.5-year sat about 25 to 35 bp under the 5-year on the 11/10 curve. One capped trade, n=1. ⚠️ Most SoftBank swap trading is between non-US dealers and is not in this report: a sample, not the market.
- Packet to SAM: `AGENTS/SAM/inbox/2026-11-25_from-LIQUID_softbank-cds-dtcc-read.md` (SAM's next wake 11/30). Arm $148.23 at 11:47 ET (vendor) against SAM's 25% central line at $150.1 (SAM's arithmetic); the line is SAM's to grade.

## 2. The other names on card 013, and CoreWeave and Oracle after the open

| Name, 5Y | Latest valid reading | Prior | Note |
|---|---|---|---|
| **CoreWeave** (500 coupon) | **1,314 clean / 1,359 dirty [11/24 close]**; three trades $2M to $3M (15:23Z, 20:12Z, 21:01Z) | 1,092 [11/23] | the 11/25 07:56 ET 5Y odd lot ($95,000, 1,363) is **CANCELLED** (EROR row, slice 306). No other 5Y trade on 11/25 through 11:45 ET. 4Y Dec-2030 1,379 / 1,429 [11/25 08:20 ET, $2M] stands (1,239 / 1,284 [11/24]) |
| **Oracle** (100 coupon) | **370 to 377 [11/25 10:07 to 10:10 ET]**, three trades ($2M, $3M, $5M+) | 362 / 367 [11/25 09:47 ET]; disseminated 365 to 370 [11/24] | wider after the open; new high against 342.5 [10/20] (KB-LIQ-158) |
| **Alphabet** | **96 to 97 disseminated [11/24]** | 95 [11/20] | no 11/25 trade. Converted prints (106 to 110) are near the coupon and sign-ambiguous (KB-LIQ-150): the disseminated figure governs. "Widest on record" is not testable from my files |
| **SpaceX** | **286 to 295 dirty (281 to 290 clean) [11/24]** | 261 to 265 [11/18]; 290 disseminated [10/30] | no 11/25 5Y trade (one 1-year only). About level with 10/30, so "record" is marginal at best |

**For WQ-745 (TERRY's CoreWeave idea): the best like-for-like 5-year figure dated 11/25 is the 11/24 close, 1,359 bp dirty (13.6% a year; 1,314 = 13.1% on the clean basis).** It is above the 12% line and the 10% kill. Today's 5-year is INFERRED higher (4-year +140 bp overnight; about 1,450 to 1,500 if the 5-year moved the same), which is not a reading. Any entry after 11/26 needs the 11/25 full file (posts about 20:15 ET 11/25) or a later one. Packet to TERRY: `AGENTS/TERRY/inbox/2026-11-25_from-LIQUID_crwv-cds-1125-correction-for-wq745.md`.

**Basis change, my own (no gate letter moves):** I headline the dirty column from today. Same-minute check, Oracle 11/24: disseminated quotes 365 to 370 sit 3 to 8 bp above the dirty conversion and 8 to 13 bp above clean, as the script's own 9/28 measured note says. My earlier headlines (1,314; Oracle 356 and 362) were the clean column. Recorded as KB-LIQ-163. The change raises CoreWeave by about 45 bp and Oracle by about 5 bp; it changes no gate grade (GATE-LIQ-069 leg L2 has stood fired since 9/26).

## 3. High yield for 11/24: confirmed and graded (WALTER card 018)

FRED first-published, my pull 11:45 ET (latest-revised the same): **HY 372** (+9; 363 [11/23]), **BB 225** (+6), **B 405** (+12), **CCC 1,405** (+18), **IG 98** (+1), **BBB 122** (+2). PROME's 372 is confirmed.

| Rule | Grade on the 11/24 cell |
|---|---|
| GATE-LIQ-069 L1 (BB >220 while CCC flat, ≤15 bp over 5 sessions) | **NOT FIRED**: BB 225 is above 220, but CCC +76 over 5 sessions (vs 11/17) is not flat (`gate069_legs.py` 11:4x ET) |
| GATE-LIQ-069 L4 (any cohort name -15% on the session with HY +5 bp or more) | **NOT FIRED**: credit half met (+9), equity half fails (worst CRWV -11.85%, raw close 11/24) |
| GATE-LIQ-069 legs fired | still **3** (L2, L5, L4); no new consequence |
| Tier rule (9/25 §1c) | **BROADENS**: B and CCC wider, and BBB +2 meets its daily p95 (+2); also BB's 15-session change +19 meets its p90 (+19) |
| One-session +25 bp safety net | **not met** (+9) |
| GATE-HY-REKILL (<260 strictly, ×2) | **NOT FIRED, 0 of 2** (372 is 112 above 260) |
| >320 sustained (WQ-444) | extends, 8 observations (323 [11/13] to 372 [11/24]) |

GATES review_by for 069 stays **11/27** (the 11/25 cell; 11/26 holiday). My rule does not move it. Nothing to route as a new fire.

## 4. Deals and loan marks since 10:01 ET

- **No AI-infrastructure or weak-credit deal pulled, postponed or repriced wider found** (web search 11:47 to 11:50 ET, aggregator results only; absence from search, not proof). CoreWeave's planned at-least-$4B investment-grade loan: no launch or pull reported.
- **Handed to BROCK** (`AGENTS/BROCK/inbox/2026-11-25_from-LIQUID_loan-etf-marks-1125.md`): the loan ETF is lagging bonds, BKLN -0.39% against HYG -0.12% and JNK -0.20% (vendor 11:47 ET); managers -2.5% to -3.8%, BIZD -0.25%. No CLO mark found. The only named loan mark is the one already logged (Project Jupiter piece about 85, 11/24).
- Funding unchanged from the morning: SOFR-IORB +4, SOFR99-IORB +12 [11/24]; constraint NOT SHOWN.

## 5. Forward view, re-marked (unscored; my judgment, not registered)

| Event, horizon | Odds now (09:58 ET) | Why; what changes my mind |
|---|---|---|
| HY 11/25 cell at least +10 bp over 372 | **40%** (55%) | HYG recovered to -0.12% by 11:47 ET; loans weaker (BKLN -0.39%) keeps it live |
| HY 11/25 cell +25 bp or more | **8%** (15%) | far from the ETF move a +25 day shows |
| GATE-LIQ-069 L4 fires on the 11/25 session | **15%** | needs one cohort name to close -15% or worse (CRWV -10.55% at 11:47 ET) and HY +5 |
| SoftBank 5Y next DTCC print at or above 550 bp (by 12/4) | **65%** | the 3.5-year is already at 555; a sharp SoftBank or Arm rebound lowers it |
| CoreWeave 5Y stays above 1,200 bp (dirty) through 12/11 | **70%** (65%) | today's 4-year +140; falls if the $4B loan prices near 7 to 7.5% or the stock rebounds as on 11/23 |
| One more named AI-infrastructure or weak-credit deal pulled by 12/11 | 70% (unchanged) | |
| Broad HY freeze (several mainstream deals pulled) by 12/4 | 20% (unchanged) | index credit still lags the single-name moves |

## 6. Cards since 10:01 ET

| Card | Lane | Disposition |
|---|---|---|
| SIG-W-20261125-018 | LIQUID | **acted**: §3 grade; corrects its CoreWeave 5Y line (cancelled print). Logged in `board_log.tsv`, filed to `processed/` |
| SIG-W-20261125-016 | LIQUID | **info-only**: Brent sign correction, BRENT's; no LIQUID record carried the figure. Logged, filed |
| SIG-W-20261125-013 | SAM (not in LIQUID's lane) | read only, answered in §1 and §2, no log row of mine |
| SIG-W-20261125-015 | not in LIQUID's lane | read only: China Section 301 notice charges servers and chips up to 10%, a proposal, not a tariff; no LIQUID gate or record touched |
| SIG-W-20261125-020 | not in LIQUID's lane | read only: owner outcomes and prints; nothing keys on LIQUID |

Correction packet to WALTER for card 018 and the card-013 levels: `AGENTS/WALTER/inbox/2026-11-25_from-LIQUID_correction-card-018-crwv-and-ai-cds-levels.md`.

## COMPLETION — LIQUID — 2026-11-25
STATUS: ✅ DONE
CHANGED: PROME/inbox/2026-11-25_from-LIQUID_softbank-cds-and-hy-1124-grade.md, AGENTS/LIQUID/STATUS.md, AGENTS/LIQUID/workbook/KB.tsv (KB-LIQ-163), AGENTS/LIQUID/board_log.tsv, AGENTS/LIQUID/inbox/WALTER/processed/ (016, 018), packets to SAM, TERRY, BROCK, WALTER, VULCAN inboxes (VULCAN and BROCK KBs cite the cancelled 1,363)
RESULT: SoftBank 5Y at DTCC 466/471 [11/24 Tokyo], no 11/25 5Y trade (SEARCH-NOT-FOUND), 3.5Y 548/555 [11/25 09:32 ET] so 5Y INFERRED 560 to 600; 9984.T -14.83%. CoreWeave's pre-open 5Y 1,363 was CANCELLED; best 5Y for WQ-745 is 1,359 dirty / 1,314 clean [11/24 close], above 12%; Oracle 370 to 377 after the open; Alphabet 96 to 97, SpaceX 286 to 295 [11/24]. HY 372 [11/24] confirmed with ladder; 069 L1 and L4 NOT FIRED, tier rule BROADENS, +25 net not met, re-kill 0 of 2; no deal pulled found since 10:01 ET.
GAPS: 11/25 full DTCC file (about 20:15 ET) and the 11/25 ICE cell not read; Alphabet/SpaceX "record" untestable from my history; SoftBank reading is a US-nexus sample; no CLO marks reachable.
WILL_NEEDS: None.
FOLLOW-UP: 069 review 11/27 (11/25 cell; GATES already 11/27); CoreWeave 5Y on the 11/25 full file before any WQ-745 entry after 11/26 (PROME re-spawn); pushes are PROME's.
