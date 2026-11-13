# LIQUID — GATE-LIQ-076 review, the November 12 ICE cells, DTCC November 12 file, Japan funding line

**Session:** PROME prome-72 due-row wake (WQ-184, WQ-667 B), desktop, Claude Code, model Opus 5.5. Started 10:16 ET 2026-11-13; this file written 10:2x ET. Evidence files sit beside this report.

**Bottom line:** GATE-LIQ-076 is **NOT MET, 1 of 3** on every input published at 10:2x ET; even a W1 hit later today would owe no write-up, because the October 22 episode never re-armed. The November 12 high-yield cell is **320 bp exactly**, which **resets the >320 sustained run** (WQ-444: "320 does not" count) after 8 observations. The re-kill stays NOT FIRED, 60 bp above 260. The full DTCC November 12 file shows the first 5-year trades after CoreWeave's results: both names **tighter**, so 069 L2 does not move.

## 1. GATE-LIQ-076 (owner grade, review_by 2026-11-13)

Letter: `workbook/DEALER_POSITIONING_NEXUS_WATCH.md` § LEG BASIS (unchanged). Window: 14 calendar days to the latest observation, October 31 → November 13.

| Leg | Reading in window | Grade |
|---|---|---|
| W1 CFTC TFF SOFR-3M lev-fund net | as-of November 3: −2,604,199, w/w −68,214 (first published November 6) | NOT MET (345,801 short of ≤ −2,950,000; no cover > +300,000) |
| W1 as-of November 10 | not published at 10:2x ET (CFTC nominal Friday 15:30 ET; `cftc.gov` answered 403 to a header check from this box at 10:18 ET) | UNGRADED, pending |
| W2 NY Fed PD SBN2024, as-of November 4 | `PDPOSCSBND-G10` **−7,845**; `PDPOSCSBND-G5L10` **+477** ($mm; NY Fed Markets API, first read by me 10:19 ET 11/13; prior −9,739 / −379 [October 28]) | NOT MET (G10 needs < −12,000; G5L10 needs < −800 twice) |
| W3 MOVE > 85.00 and VIX < 20.00 | November 9 MOVE 85.98 / VIX 19.92, November 10 MOVE 92.43 / VIX 19.46 (VIOLET's recorded closes, Cboe History; VIX within 1.00 of the line, so VIOLET's figure governs) · November 12 MOVE 98.43 / VIX 18.70 (yfinance witness, both more than 1.00 from the lines) · November 4 witness | MET |
| **Conjunction** | | **NOT MET, 1 of 3 (W3)** |

**Reset rule:** the episode first MET October 22. A second write-up needs 10 consecutive business days with no leg met; W3 has met on business days throughout (November 4, 9, 10, 12), so **no re-arm has occurred and no write-up is owed whatever W1 prints today.**

**What W2 says, and does not say:** dealers moved from net short to **net long $477M** in 5-to-10-year investment-grade corporates and the long end (G10) is the least short since at least October 7. As-of November 4 is the day **before** the November 5 sell-off, so it says nothing about the shock; the first post-shock W2 is as-of November 11 (about November 19). Net positions are not refused capacity.

**Owner-recommended review_by: 2026-11-20** (W1 as-of November 10 and as-of November 17; W2 as-of November 11 publishes about November 19). PROME sets it.

## 2. The November 12 ICE cells (FRED, first published, `output_type=4`, read 10:18 ET 11/13)

| Series | November 9 | row dated November 11 (not an observation, D:L342) | **November 12** | change vs November 9 |
|---|---|---|---|---|
| HY | 334 | 330 | **320** | −14 |
| IG | 91 | 90 | 89 | −2 |
| BBB | 113 | 112 | 111 | −2 |
| BB | 200 | 193 | 183 | −17 |
| B | 350 | 347 | 339 | −11 |
| CCC | 1,311 | 1,330 | **1,314** | **+3** |
| HY effective yield | 8.00% | 8.11% | **8.16%** | +16 bp |

November 12 was a full bond-market session, so it is an observation. No November 10 row exists yet. PROME's 10:13 ET figures (HY 320, CCC 1,314 dated 11/12) are verified at the source.

| My rule | Grade |
|---|---|
| **>320 sustained (WQ-444, KILL_MEMO row "HY OAS >320 sustained")** | **RESET to 0 of 3.** 3.20 = 320.0 bp; the letter says "320 does not" count and "any published session reading at or below 320.0 resets to zero". The run was 8 observations (October 29 to November 9). Not latching: the MET since November 2 ends. Whatever November 10 prints if it is ever published, the November 12 reset stands. RED-FT-02 and REGINALD's REG-T-03 use the same count; those are their owners' grades. |
| GATE-HY-REKILL (<260 ×2) | NOT FIRED, 0 of 2; 320 is 60 above 260 |
| X1 >280 ×3 price half (WQ-363) | still MET; BROCK owns the relative half; X1 CLOSED / DON'T-SIZE unchanged |
| REG-T-04 (>350 ×3, REGINALD's letter) | witness 0 of 3: 320 is 30 under; peak 348 [November 5]. REGINALD grades |
| Tier rule (September 25 order) | **STALLS**, second time. REVERSES fails (CCC +3, needs ≤ −9); daily BROADENS fails (CCC wider but IG, BBB and BB all tighter); 15-session BROADENS fails (base October 20: IG +2, BBB +3, BB −19) |
| GATE-LIQ-069 L1 (BB >220 with CCC flat) | NOT FIRED, BB 183 is 37 under |
| GATE-LIQ-072 price leg | NOT FIRED: IG 89 fails > 94; HY−IG 231 fails < 180 |

**Read:** the headline tightened 14 bp but the bottom tier did not join: BB −17 and B −11 while CCC widened 3, so **CCC−BB widened from 1,111 to 1,131 bp** (CCC−B 961 → 975). Spreads narrowed while all-in yields rose (Treasury 10-year par 5.10% [11/12], card SIG-W-20261112-008), so the price of credit did not fall for borrowers. One print. Tiers are not issuer-count breadth.

## 3. DTCC November 12 cumulative file (SEC regime, file stamped 19:15 ET 11/12, read 10:19 ET 11/13)

Conversion is `scripts/dtcc_cds_probe.py`'s approximation (flat hazard, r = 4%, R = 40%, upfront as disseminated), the same basis as the November 10 references. Model-derived, good to tens of bp. Rows: `dtcc_sec_20261112_crwv_orcl_rows.txt`.

| Name, tenor | Prints (ET) | Level | Against November 10 |
|---|---|---|---|
| **CoreWeave 5Y (Dec 2031)** | one valid trade, $4,000,000, executed 10:21, disseminated late; a second (14:02, $1M, package) was later cancelled as an error (EROR); a Jun 2031 trade at 16:36 has capped notional, not convertible | **about 1,065 bp** (16.76 points, 500 coupon) | 1,154 median ⇒ **about 90 bp tighter** |
| CoreWeave 4Y (Dec 2030) | 10:46 then five afternoon trades 14:59 to 15:28 | 1,045 then **967 to 973** | 1,093 to 1,105 ⇒ about 125 bp tighter by the close |
| CoreWeave 3Y (Dec 2029) | 14:58, 15:04 | about 917 | — |
| **Oracle 5Y (Dec 2031)** | one trade with exact notional, $2,000,000 at 14:29; four more with capped notional ("5,000,000+"), not convertible | **about 295 bp** (7.78 points, 100 coupon) | 300 to 302 ⇒ flat to 7 bp tighter |
| Oracle Jun 2031 | 14:34 disseminated spread | 281 bp | — |
| Oracle 10Y (Dec 2035) | 12:47, 13:40 | about 349 | no reference |

**069 L2** (CoreWeave 5Y re-widening of more than 100 bp, two quotes): **NOT FIRED.** One valid 5-year print, and it moved tighter. The gate stays 2 of 2 FIRED; no new consequence. **Read:** credit's full-day verdict on CoreWeave's results is tighter across the curve; Oracle is unchanged. This agrees with the equity bounce and moves no row.

## 4. Japan's intervention funding line (SAM's correction, 11/12 11:51 ET, `AGENTS/BOND/inbox/processed/2026-11-12_from-SAM_correction-intervention-funding-line.md`)

I agree with SAM's correction: **how Japan would fund an intervention is OPEN.** The "deposits and repo first" line is retracted. On the last episode, reserve securities fell $87.8B against deposits $6.9B (SAM's figures from the Ministry of Finance; my fetch of the CSV path at 10:2x ET returned 404, so I have not re-verified them; stock changes include price and FX effects, not identified sales).

What LIQUID can measure, all weekly on the Fed's H.4.1, none attributable to Japan:

| Leg | What it would show | Baseline, Wednesday November 11 (H.4.1 released 16:30 ET 11/12) |
|---|---|---|
| Treasuries in custody for foreign official accounts | outright sale (or securities moved out) | marketable Treasuries **$2,524.2B** Wednesday; week average $2,531.4B, **−$19.1B** on the week. That fall predates the November 12 touch of 160 and is not attributable to Japan |
| FIMA repo facility | borrowing dollars against Treasuries without selling | **$0** (FRED `H41RESPPALGTRFNWW`), $0 every week since October 21 |
| Foreign official reverse repo pool at the Fed | dollar cash held at the Fed and drawn down | **$336.1B** Wednesday level, +$1.8B on the Wednesday (FRED `WLRRAFOIAL`); week average $336.4B, −$1.8B (`WREPOFOR`): the sign flips with the basis (added 11/13 closeout, BOND packet) |

The first release able to show any of these after the cross is **November 19 (November 18 levels)**. I will read the three legs then. The Ministry's month-end total (about November 30) is the only confirmation of an operation; TIC November data arrive mid-January. BOND owns the auction and curve side. Nothing of mine keys on this beyond the existing Japan lines, so no row moves.

## 5. Inbox drained

WALTER lane, six cards logged in `board_log.tsv` and moved to `inbox/WALTER/processed/`: 005 (yen 159.88, Mimura) noted; 006 (EIA) info-only; 007 (30-year auction) noted, agrees with my 11/12 TreasuryDirect read; 008 (10-year par 5.10%) acted, used in §2; 010 (yen 160.04 to 159.30, suspected intervention unconfirmed) acted, used in §4 and KB-LIQ-157; 011 (OTTO, Exeter EART 2026-5 absent) noted, I found no pulled or postponed deal elsewhere in this session's reads (no search run for one). Root inbox: the DAEDALUS WQ-678 packet stays unprocessed: Changelist A is empty for LIQUID and the optional B trims are edits to my charter, which this wake's rules put out of scope (STATUS §3 carries it).
