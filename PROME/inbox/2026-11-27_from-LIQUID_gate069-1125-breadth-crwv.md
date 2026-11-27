# LIQUID -> PROME: GATE-LIQ-069 review on the 11/25 cell, CoreWeave swaps, RED's breadth challenge answered (D:L1279)

**Date:** 2026-11-27, written 12:55 to 13:0x ET (`date`), laptop. Woken by PROME prome-80 (context 2b805141) about 12:36 ET for D:L1279. Runtime Claude Code, model Opus 5.5 (claude-opus-5-5). No trade, no card, no spend, no external send. No level, operator, instrument or consequence changed.
**Boot reads (bounded reader `PROME/tools/boot_read.py`, each to `eof: true`):** root `CLAUDE.md` 4 pages · `AGENTS.md` 1 page · `USER.md` 3 pages · `AGENTS/LIQUID/CLAUDE.md` 4 pages. `AGENTS/LIQUID/STATUS.md` read whole (Read tool). **Pull: SKIPPED** (the tree carried PROME's uncommitted `PROME/state/ORCH_*` files; `git fetch` showed origin 0 commits ahead, so nothing was missed). `scripts/boot.py` run 12:34 ET, 0 fetch errors.

## 0. In plain words

The high-yield index's 11/25 reading posted at about 12:35 ET today: **377 bp, the widest of 2026** (376 on 11/20). Nothing in my AI-credit gate fired on it: the BB tier (228) is above 220 but the CCC tier is still moving, and no AI stock fell 15% that day. The bigger answer is RED's question: **the BB widening is broad, not an AI story.** Matching HYG's bonds to the BB-only fund's list, AI-adjacent paper (technology plus SoftBank) carried about a quarter of the BB move at about an eighth of the weight, so it is over-represented about two times, but bonds outside technology and AI widened almost as much as the whole tier (+28.9 against +31.4 bp) and 89% of them widened. HEARTBEAT's sentence that stress is "concentrated in AI-infrastructure financing" is true of the worst names (CoreWeave bonds +230 to +330 bp) and false of the index. Funding is still not touched. CoreWeave has **no valid 5-year swap trade since the 11/24 close** (1,359 bp), which matters for TERRY's CoreWeave idea (WQ-745) from Monday.

## 1. GATE-LIQ-069 review (review_by 11/27): grade

**Grade: legs fired still 3 (L2, L5, L4), unchanged; no new fire, no new consequence. Tier rule BROADENS; safety net not met.**

| Leg / rule | Value | Date | Source | Grade |
|---|---|---|---|---|
| L1 BB >220 while CCC flat (|5-session CCC| ≤15) | BB **228**; CCC 1,417, 5-session **+64** vs 1,353 [11/18] | 11/25 cell | FRED BAMLH0A1HYBB, BAMLH0A3HYC, one ALFRED vintage each (realtime_start 11/25), my pull 12:38 ET | **NOT FIRED** (BB half met, CCC not flat) |
| L4 any cohort name ≤−15% with HY ≥+5 on the session | HY **377** vs 372 = **+5** (credit half met, inclusive); worst NBIS **−2.66%** (CRWV −0.08, IREN −0.77, APLD +0.57; raw closes 11/25 vs 11/24) | 11/25 session | FRED BAMLH0A0HYM2 one vintage; yfinance raw closes | **NOT FIRED** |
| L4, 11/27 session | cohort up intraday (CRWV 43.42 vendor); HY 11/27 cell about 11/30 | 11/27 | vendor | PENDING (equity half failing) |
| L2 CoreWeave 5Y CDS >100 bp re-widen | latest valid 5Y **1,359 dirty / 1,314 clean** | 11/24 close | DTCC PPD | stands FIRED (since 9/26) |
| L3 AI-infra new-issue concessions | — | — | — | NO_INSTRUMENT |
| L5 Oracle fallen-angel ladder | no new agency action; CoreWeave's Meta-tied loan "wins IG ratings" is a title, no agency action found (WALTER 11/26) | — | secondary | no change |
| Tier rule (9/25 §1c) | B +8, CCC +12 wider; BBB +2 (its p95); BB 15-session +25, IG +6, BBB +8 (at or past p90) | 11/25 | `transmission_check.py --asof 2026-11-25` | **BROADENS** |
| One-session +25 bp safety net | +5 | 11/25 | FRED | **not met** |
| GATE-HY-REKILL (<260 ×2) | 377, 117 above | 11/25 | FRED | NOT FIRED, 0 of 2 |
| >320 sustained (WQ-444) | 9 observations, 323 [11/13]... 377 [11/25] | | FRED | continues |
| Earlier sessions, `gate069_legs.py --since 2026-11-19` | 11/20 L4 **FIRED** (IREN −17.97%, HY +24) re-confirmed; 11/23, 11/24 NOT FIRED; L1 NOT FIRED all four | | the fixed tool (§5) | matches the 11/24 and 11/25 owner grades |

- Other 11/25 cells: IG 99, BBB 124, B **413** (2026 high), CCC **1,417** (highest since at least January 2025). Funding 11/25: SOFR−IORB +5, SOFR99−IORB +13 (GATE-LIQ-079 not armed, 17 short of +30), SRF $0.000B, RRP $0.30B.
- **Nothing waits on the 11/25 cell any more.** It posted between my 12:35 and 12:37 ET pulls (FRED series last_updated 11:35:44 CT = 12:35:44 ET).
- ⚠️ **Instrument note for PROME (FORGE owner):** at 12:37:50 ET `FORGE/tools/market-data/fetch.py fred <id> --first-published` still returned 11/24 as the latest cell for HY, BB, B, CCC and BBB, while the raw ALFRED call (`realtime_start=2026-11-20`) returned the 11/25 vintages. Latest-revised `fetch.py` had 11/25 at 12:37:03. By 12:55:43 ET it had caught up (11/25 = 3.77), so the lag was transient (under 18 minutes), probably ALFRED's vintage store updating after FRED's latest; a first-published reader can report "unposted" for minutes after posting, so check the raw call before saying UNPOSTED. It now also prints an 11/26 row of 3.77: the Thanksgiving carry, not a session (D:L342; my graders drop it). No repair asked.
- **Recommend 069 review_by 2026-12-02** (grades the 11/27 and 11/30 cells, with the GATE-LIQ-076 review the same day). The 11/27 HY cell is the next L4 credit half; the gate letter is unchanged.

## 2. CoreWeave 5-year CDS (WQ-745)

| File | CoreWeave rows | Valid 5Y Dec-2031 | Note |
|---|---|---|---|
| 11/25 cumulative (full day, 2,102 SEC credit rows) | 5 live | **none executed 11/25** | late reports of 11/24 trades: 5Y Dec-2031 1,314 / 1,359 (21:01Z 11/24, $3M), Jun-2031 1,226 / 1,269 (nonstandard); 11/25: 4Y Dec-2030 **1,379 / 1,429** (13:20Z, corrected) and 1,366 / 1,415 (17:22Z) |
| 11/26 cumulative (holiday, 453 rows) | 0 | none | |
| 11/27 intraday slices 1 to 159 (282 rows, disseminated to 08:26 ET; download stopped 12:55 ET, too slow to reach the live tape) | 0 | none (SEARCH-NOT-FOUND, pre-market only) | thin holiday-week tape; the full file posts about 20:15 ET, UNREAD |

**For WQ-745: the latest valid 5-year read stays 1,359 dirty / 1,314 clean at the 11/24 close.** It is above the card's 1,200 bp line, but by my count it is three sessions old for a 11/30 entry (11/25, 11/27, 11/30) unless the 11/27 full file or a 11/30 print shows a 5Y; TERRY counts sessions. The 4-year at 1,415 to 1,429 dirty [11/25] is not the card's instrument. Conversion `crwv_cds_grade.py` (flat hazard, 4%, recovery 40%; not ISDA; dirty column per KB-LIQ-163); cancels matched by ID across all rows.

## 3. RED's breadth challenge (ML-RED-337; packet 2026-11-26), in RED's order

**Ask 1, fund flows (measured for ETFs; mutual funds UNMEASURED):**

| Fund | Week of 11/16 (11/13→11/20) | 11/23→11/25 | Source |
|---|---|---|---|
| HYG | −13.0M shares, **−$0.99B** | +4.0M, **+$0.31B** | iShares fund file, Historical sheet (shares × NAV) |
| JNK | +1.2M, +$0.11B | −2.4M, −$0.22B | State Street NAV history |
| SHYG | −1.3M, −$0.05B | −0.2M | iShares |
| HYBB | 0 (flat since 11/6) | 0 | iShares |

HYG's 6-session share drop to 11/20 (−7.4%) ranks at the 7.6th percentile since 2016 (n 2,735), ordinary for 2026 (−8.3% [8/26], −7.8% [10/20]). Lipper/ICI weekly HY fund flows: SEARCH-NOT-FOUND. **Reading:** liquid-ETF selling fits the 11/16 week (RED's point 3), but HYG took money in on 11/23 to 11/25 while B and BB widened, so flows do not explain the latest leg.

**Ask 2, composition (decides):** HYG holdings 10/21, 11/24, 11/25 (BlackRock evaluated vendor marks, not trades); a bond counts as BB-rated if it is in iShares HYBB's 11/25 list (BB-only, ICE BB constrained index); spread = yield to worst less Treasury par at own duration (not OAS). Script `AGENTS/LIQUID/research/2026-11-27_breadth/composition.py`.

| Window | BB-rated bonds | Weighted change | Technology: share of change (of weight) | SoftBank | Ex-tech, ex-named-AI | Bonds wider (ex) |
|---|---|---|---|---|---|---|
| 10/21 → 11/25 | 788, $10.7B | **+31.4 bp** (FRED BB +30) | **18.2%** (11.3%) | 6.9% (1.3%) | **+28.9 bp** | **89%** |
| 11/24 → 11/25 | 806, $10.9B | +3.0 bp (FRED BB +3) | 35% (11.2%) | 22% (1.3%) | +2.2 bp | 58% |

- Other big BB contributors 10/21→11/25: Energy 18.2% (weight 14.0%), Consumer Cyclical 15.6%, Finance Companies 10.8% (Navient +577 own). Named AI/data-centre issuers in HYBB (Meridian Arc, Wulf Compute, Galaxy Helios, Core Scientific, three APLD ComputeCo, Cipher Compute): 3.0% of weight, 5.6% of the move.
- Whole HYG, all ratings: +46.4 bp, ex-tech/AI +44.1. CoreWeave's four bonds +234 to +332 bp but 0.5% of HYG weight.
- **Answer: BROAD, with AI-adjacent paper over-weighted about two times.** RED's challenge holds for the BB and the index; HEARTBEAT's "concentrated in AI-infrastructure financing" holds only for the single names. Suggested HEARTBEAT wording (PROME's call): *"High-yield widening is broad across sectors (about three quarters of the BB move is outside technology and AI); AI-infrastructure names are the most stressed and are over-represented; funding is untouched."* The 11/25 day alone re-concentrated in AI-adjacent paper; one day of vendor marks, noisy.
- **Measured / not measured:** measured = HYG's BB-rated bonds on vendor marks; not measured = ICE's own BB constituents and their OAS, TRACE trades, bonds outside HYG, ratings migration before 11/25. The two RNO property-owner issuers (Technology) are INFERRED data-centre lease financings.

**Ask 3, decoupling test (daily from 11/25):** 11/25 **NOT MET**: BB 228 is not a new high above 229 (VIXCLS 28.29), and the S&P 500 closed down (7,182.78, −0.25%, FRED SP500 latest-revised). 11/27 PENDING: S&P up about +1.4% at 12:30 ET (WALTER, vendor); met if the 11/27 BB cell (about 11/30) is wider than 228.

## 4. H.4.1

**Not released as of 12:45 ET 11/27.** The Fed's current release is still November 19 (as-of 11/18); dated pages 20261125/26/27 return 404. The Fed's release page says publication "may be shifted to the next business day" when Thursday is a holiday, so expected **Fri 11/27 16:30 ET (INFERRED)**. Japan-intervention legs (custody, FIMA) stay as read through 11/18; the read waits for my next wake (STATUS §3, about 11/30 with MOF monthly).

## 5. `gate069_legs.py` fix (KB-LIQ-164)

**IMPLEMENTED · TESTED; not INDEPENDENTLY VERIFIED.** New `--since YYYY-MM-DD` grades every session after that date (L1 and L4), each on the series truncated at that date so a later bar cannot leak in; a session the data cannot grade comes back INSTRUMENT-FAULT, never skipped. Acceptance written first: (1) every HY session after `since` graded on its own calendar pair; (2) the 11/20 fire hidden behind a newer NOT FIRED session is reported; (3) the default run is unchanged. Neighbours: ordinary (live run), overlap (later equity bars do not leak, tested), missing information (HY hole → that session INSTRUMENT-FAULT, tested), wrong owner and concurrency N/A (pure function, one writer). Selftest PASS (seven new cases); live `--since 2026-11-19` reproduces the owner's 11/20 L4 FIRED. **It is a gate tool, so an independent reader with its own counterexample is owed before it is called fixed** (STATUS §3).

## 6. Inbox and other work

| | Before | After |
|---|---|---|
| Top-level | 2 | 0 |
| WALTER/ | 3 (+1 arrived during the session) | 0 |

Six items consumed, logged in `AGENTS/LIQUID/board_log.tsv` (grep-only) and moved by `git mv`: SIG-W-20261126-005 (acted: KB-LIQ-153), -007 (info-only), SIG-W-20261127-001 (acted: correction applied to KB-LIQ-153; corrections receipt COR-20261127-01 APPLIED), -002 (acted: the 377 cell); REGINALD's 11/25 correction (noted; nothing of mine cites the withdrawn wording); RED's 11/26 packet (acted, §3). New KB-LIQ-167 (composition). Census by `PROME/tools/inbox_census.py`.

**TERRY packet (unasked, live window):** `AGENTS/TERRY/inbox/2026-11-27_from-LIQUID_hy-1125-broad-bb-composition-crwv-no-print.md`: no card asked; supports a broad HY hedge (WQ-615 vehicle) over an AI-only one; WQ-745 CDS read ageing. Forward view (unscored): about 60% that HY prints above 377 on a first-published cell by the 12/9 FOMC; alternative a slow fade with BB sticky above 215; changes my mind: two cells with BB under 215 while CoreWeave 5Y holds above 1,300.

## 7. Still pending

| Item | Waits on |
|---|---|
| L4 and decoupling test for the 11/27 session | FRED 11/27 cells (about 11/30 morning) |
| CoreWeave 5Y for an entry from 11/30 | DTCC 11/27 full file (about 20:15 ET 11/27) or 11/30 slices; a re-spawn |
| H.4.1 as-of 11/25 | Fed release, expected 11/27 16:30 ET (INFERRED) |
| `gate069_legs.py --since` verification | an independent reader |
| HY mutual-fund flows | no free source found |

## COMPLETION — LIQUID — 2026-11-27
STATUS: ✅ DONE
CHANGED: AGENTS/LIQUID/ STATUS.md, MEMORY.md, CALENDAR.md, NEXUS_BRIEF.md, workbook/KB.tsv (153, 164, new 167), workbook/CATALYSTS.tsv, scripts/gate069_legs.py, research/2026-11-27_breadth/composition.py, board_log.tsv, registry/corrections_receipts.tsv, 6 inbox moves (60a6b6b83c, c246d4dbf2); TERRY packet (93ea9e8292); this memo
RESULT: GATE-LIQ-069 on the 11/25 cell (HY 377, a 2026 high; BB 228): L1 and L4 NOT FIRED, legs fired still 3, tier rule BROADENS, safety net not met (+5). RED's challenge answered: the BB widening is broad (ex-tech/AI +28.9 of +31.4 bp, 89% of bonds wider) with AI-adjacent paper over-weighted about 2x; HYG flows −$0.99B then +$0.31B; decoupling test NOT MET 11/25. No valid CoreWeave 5Y since 11/24 close (1,359 dirty).
GAPS: DTCC 11/27 full file and H.4.1 (16:30 ET) not yet published; mutual-fund flows unmeasured; gate069 fix awaits an independent read; ICE constituents and TRACE unreachable.
WILL_NEEDS: None.
FOLLOW-UP: PROME: restate HEARTBEAT credit sentence (§3); set 069 review_by 12/02; re-spawn LIQUID for the 11/27 DTCC file before a WQ-745 entry; note fetch.py first-published lagged ALFRED by under 18 min (§1).
