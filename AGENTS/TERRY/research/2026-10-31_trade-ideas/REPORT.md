# TERRY — trade ideas from the week of 10/26–10/30 (WQ-569) — evidence report

**Written:** 2026-10-31 14:10 EDT (from `date`). **Authority:** Will's "yes go" on WQ-569 in PROME's chat, 13:42 ET (one bounded Opus trade-ideas session, PROME prome-34). **Runtime:** Claude Code, Claude Opus 5.5 (`claude-opus-5-5`), PROME-spawned desk session. **$0 moved · no order · no approval, trigger, threshold or score changed.** Markets shut Saturday: every price below is a Friday 10/30 close or older, labelled; option figures are weekend SCREENING marks from chains actually read (durable finding 5b).

## 1. Boot receipt
Bounded reader (`PROME/tools/boot_read.py`) to `eof: true`: root `CLAUDE.md` 5 pages · `AGENTS.md` 1 · `USER.md` 2 · `AGENTS/TERRY/CLAUDE.md` 6. Then STATUS, RISK_RULES (whole), RISK_SCORING, CHART_OPTIONS_WORKFLOW, TRADE_CARD_TEMPLATE (+FIRE), RISK_RULES_CONSTRUCTION rules 14–23 (whole), TRADE_BOOK, SETUPS, IDEA_SHELF. `boot.py` ran (ledger sweep clean; BOARD floor clean). `paper_book_mark.py` ran twice (before and after the PB-0008 split). R1 corrections check rc 1 → 0 after one receipt. No pull: the tree carries other desks' work (WALTER, BOARD, PROME tools); ahead 1 / behind 0 at boot.

## 2. Inputs (verified at the artifact)
| Input | Artifact | Used for |
|---|---|---|
| HENRY breadth L616, 10/30 closes | `PROME/inbox/processed/2026-10-31_from-HENRY_L616-market-breadth.md` (HENRY 1704c924b) | bank re-check; QQQ card context; RSP shelf condition |
| ISHM backlog + ISM frame | `PROME/inbox/processed/2026-10-31_from-ISHM_backlog-and-ism-frame.md` | capex pass |
| Russia diesel №1436 | BOARD `SIG-W-20261031-001`; HEARTBEAT energy line; `SIG-W-20261031-004` (Novak plan) | refiner pass |
| MIDAS GLD liquidation test | `PROME/inbox/processed/2026-10-30_from-MIDAS_gld-july-low-close-break-liquidation-test.md`; WQ-554 row | gold pass; GLD card record |
| NEXUS term premium | inbox packet (→ processed) | duration "no card" |
| GIBBS large-bank read | `PROME/inbox/2026-10-31_from-GIBBS_inbox-drain-and-actions.md` (GIBBS 888f60f13), relayed by PROME mid-session | bank re-check |
| REGINALD current judgment | `AGENTS/REGINALD/STATUS.md` (10/30–10/31 blocks) | bank re-check |
| LIQUID DTCC 10/30 | `PROME/inbox/processed/2026-10-30_from-LIQUID_dtcc-1030-orcl-crwv.md` | ORCL card state |
| BOND refunding | `AGENTS/BOND/STATUS.md`; KB-BND-472 (Treasury 8/5 guidance; Citi cut forecast) | duration "no card" |
| AEOLUS vortex | `AGENTS/AEOLUS/workbook/KB.tsv` KB-AEO-225/229 (10/29) | UNG card trigger |
| Positions | `FORGE/STATUS.md` (ANVIL reconcile of Will's 10/30 13:21 ET capture; a mirror, not broker truth) | bank re-check; QQQ card |

Prices: `prices_1030close.txt` (fetch.py, pulled 10/31 13:47 ET, all stale-flagged 10/30 bars). Chains: `chains_screening.txt` (UNG Jan-15/Dec-18 calls, RSP Jan-15 calls). Bank figures: `bank_recheck.py` → `bank_recheck_output.txt`.

## 3. Carded (one)
`IDEA-UNG-SSW-OCT31` — UNG Jan-15-2027 10/12C ×5, limit ≤ $0.50, max loss $256.50, NOT-FIRED on an AEOLUS-logged observed vortex reversal by 11/12 then a red UNG day by 11/20 (`../../setups/UNG_jan15-10-12C_polar-vortex-break_2026-10-31.md`; CAL-0003 p = 0.70 subjective). Supporting figures: UNG $9.08 [10/30] at its 60-bar low; NGZ26 $2.90 / NGF27 $3.37 / NGG27 $3.03 (vendor bars 10/30); EIA storage 3,724 Bcf [10/23] = +1.0% vs 5-yr, −3.8% y/y (report released 10/29, read at ir.eia.gov); Jan-15 10C 0.83/0.88 (OI 31,202, IV 72.6%), 12C 0.45/0.50 (OI 33,917, IV 78.9%).

## 4. Looked at and passed (with the re-look trigger)
| Idea | Owner evidence | Why no card | What would change it |
|---|---|---|---|
| Duration short into the 11/4 refunding (NEXUS ask) | NEXUS: October's 10Y fall was all term premium (ACMTP10 −24.6 bp, 10/8→10/23); BOND KB-BND-472 | Treasury's 8/5 guidance holds coupon sizes "for at least the next several quarters" and the only 11/4 forecast on file (Citi) is a CUT of $3B per 20Y/30Y auction: the supply surprise skews toward LESS long-end supply. Haven bid on equity selloffs (10Y 5.05% official [10/28] → 4.93% vendor [10/30]); BOND's duration-short kill MET (posture since 10/01); Will sold TBT ×10 on 10/30 | A QRA that raises coupon sizes or drops the guidance, or a 10Y/30Y auction that fails on BOND's frozen bars (11/10, 11/12) |
| Refiners on Russia's diesel ban (№1436) | YURI/WALTER 001; WALTER 004; BRENT 10/29 "not suggested: new refiner longs" | The law tightened while the plan loosened: Novak plans 2.15 Mt of November diesel exports vs 510 kt in October (TASS 10/30); the delivered-supply effect is ungraded (BRENT owns it); Dec ULSD crack $93.06 [10/28 ESTIMATE] sits below the held-VLO $95 notice line; any refiner card shares one falsifier with the held VLO shares | BRENT grades №1436 as cutting delivered diesel exports AND the matched December crack settles back above $95 |
| BRENT #1: own the back of the oil curve | BRENT 10/29 (Moderate) | No trigger exists (BRENT: "thesis-level view"); the book already holds the front (USO 30 sh + Nov-20 170C, VLO 3 sh); the useful form of the idea is swapping front for back, which touches lines Will manages by hand (WQ-200) | A BRENT-registered deferred-curve trigger, or Will asking for the swap analysis |
| BRENT #2: tankers into Sinokor 11/1 | BRENT 10/29 (Low–moderate); WALTER 10/30-011 | The event lands Sunday 11/1, before Monday's open; tape already bid 10/29; OVX ~56 makes options dear; BRENT LESSONS #19: tanker equities do not move one way on Hormuz news | Observed enforcement plus a measured freight move, priced fresh |
| Industrial capex (ISHM) | ISHM 10/31: equipment +20.9% SAAR, CAT dealer retail +22% | No edge against consensus (ISHM's ISM ~54 frame is a desk expectation; consensus UNKNOWN); strength narrow (AI hardware, data-center power); CAT fell 3.81% on 10/30 with the AI-hardware selloff | A thesis owner (ISHM/VULCAN) naming a mispriced, dated catalyst |
| Gold | MIDAS 10/30 | MIDAS measured no rebound edge after liquidation days (10-session residual positive 64% of the time = the all-days rate) | MIDAS's 11/2 tonnes grade, or a measured edge |
| More Nasdaq / chip downside | HENRY L616; book | Same falsifier as the held QQQ lines (N_eff ≈ 1); Friday's move already ran (SOXX −8.24%) | — |
| BDC software marks (FSK 11/05) | BROCK 10/29 | BROCK has not proposed; construction rule #18's envelope is unmeasured for BDCs | BROCK's FSK grade 11/05 |
| **Shelf: RSP equal-weight call spread** | HENRY L616: October RSP/SPY +5.91 pp (99.5th percentile since 2003); Friday a pullback (SPY −1.77%, RSP −0.79%) | Meets its shelf row's own second-look condition ("a fresh breadth confirmation after a pullback"); revival is Will's word (`../../setups/IDEA_SHELF.md`). Weekend quotes too wide to price (Jan-15 220C 4.80/6.10, 230C 0.05/2.90) | Will: "revive RSP" → re-priced from scratch at a live chain |
| **Shelf: VST (Vistra) common** | WATT 10/29: PJM evening scarcity hours 19 vs 1 a year earlier; same-load spike rate 4.3% vs 0.7% | Meets its shelf row's second-look condition ("a fresh WATT stress read"); VST $138.37 [10/30] vs the card's $149.70 limit. WATT's own four unknowns travel (priced-in, hedge ratios, size of the money, one baseline year) | Will: "revive VST" → re-priced from scratch |
| Shelf: IEF call spread | BOND 10/15 | Half its condition met (risk-off week, 10-year falling) but IEF already rose to $91.76 [10/30], so the old 90/92 strikes no longer fit the $0.85 cap | Not flagged |

## 5. Bank-put re-check (thesis analysis, not a sell or hold recommendation)
Lines per the FORGE mirror (Will's 10/30 ~13:2x ET capture; marks are intraday lasts, not closes); distances from the 10/30 closes; KRE frequencies = share of overlapping windows since 2006 in which KRE closed at or below the strike after the same number of sessions (an observation, not a probability):

| Line | Close [10/30] | To strike | Sessions | Paid | Value (10/30 midday) | KRE windows at/below strike |
|---|---:|---:|---:|---:|---:|---|
| KRE Nov-20 66P ×3 | 72.01 | −8.3% | 15 | 133.99 | 78.00 | 7.6% |
| KRE Nov-27 70P ×2 | 72.01 | −2.8% | 19 | 281.33 | 204.00 | 29.2% |
| KRE Nov-27 68P ×10 | 72.01 | −5.6% | 19 | 726.63 | 500.00 | 17.1% |
| KRE Nov-27 67P ×4 | 72.01 | −7.0% | 19 | 510.65 | 148.00 | 12.7% |
| KRE Dec-18 60P ×5 | 72.01 | −16.7% | 34 | 1,391.36 | 135.00 | 4.2% |
| KRE Dec-31 65P ×2 | 72.01 | −9.7% | 42 | 337.33 | 150.00 | 11.8% |
| OZK Nov-20 40P ×4 | 50.65 | −21.0% | 15 | 322.65 | 40.00 | — |
| WAL Dec-18 70P ×2 | 76.29 | −8.2% | 34 | 551.33 | 230.00 | — |
| WAL Dec-18 65P ×4 | 76.29 | −14.8% | 34 | 682.65 | 220.00 | — |
| ZION Nov-20 62.5P ×2 | 65.37 | −4.4% | 15 | 435.33 | 80.00 | — |
| VLY Dec-18 12P ×1 | 14.14 | −15.1% | 34 | 15.66 | 5.00 | — |
| FLG Mar-19-2027 10P ×1 | 10.51 | −4.9% | 95 | 70.66 | 55.00 | — |
| **Bank lines (40 contracts)** | | | | **5,459.57** | **1,845.00** | |
| APO Dec-18 95P ×1 (private credit) | 115.84 | −18.0% | 34 | 1,184.67 | 65.00 | — |

**Evidence against the thesis this week:** HENRY — banks joined October's broadening (KRE +3.70% total return in October vs SPY −0.91%; −4.79% over three months) and Friday's −1.82% was narrow (79% from Mag-7 plus 18 chip makers); GIBBS — the 16 large banks add no industry-wide leg (warning pattern at PNC only, on CRE; BAC/BNY/USB preferreds and PNC $1.5B / AXP $3.0B notes placed without difficulty; no cyber 8-K at any of the 16, 10/23–10/31); REGINALD — severity concentrated at FLG/EGBN/AMTB (WAL and OZK mid-pack), the HY widening bank-absent, small-bank Q3 funding no run (borrowings −$5.70B, deposits +$39.20B, frozen screen), "no forward edge for KRE"; rates — REGINALD reads a rising 10-year as what moves regionals, and the 10-year fell (my own 10/24 fit of that link is weak, R² 0.13).
**Evidence for:** HY OAS 314 → 326 bp [10/28→10/29], a session before the equity break (credit-leads rule); Q3 problem loans rose at 7 of 10 of REGINALD's names; BXMT dividend cut and −11.7% book value (CREED, a CRE lender); VNQ/SPY −11.33 pp, rate-led (CREED).
**Decides more than anything this week:** the Q3 10-Qs (~11/10–11/14; VLY modifications, FL frame final), REGINALD's 11/07 Call Report run, FHLB CFR 11/13 (REG-T-06), GIBBS's L780 10-Q pass 11/06.
**Structural note:** the book's two bearish legs are not one bet in this regime. Friday's Nasdaq selloff came with Treasuries bid (10-year down), which REGINALD reads as support for regionals: QQQ −3.47% vs KRE −1.17% on 10/30.
**Caveats that travel:** GIBBS — "none found" is not "none proven" (2023 cyber victims surfaced weeks later); 9 of 16 large-bank 10-Qs unfiled (Goldman's $368M of unexplained loan-impairment charges waits on its 10-Q); the deposit-cost comparison rests on 10 large + 4 regional banks.

## 6. Existing card states written today
- **QQQ (`IDEA-QQQ-PUTWALL-OCT22`), D-93:** now a naked long 690P ×2 (670P ×2 bought back 10/30 @ $8.00, leg +$141.30); spread harvest lapsed; kill (SPX ≥ 7,750 ×2) and time stop (11/13) kept as reads; forward risk = remaining mark ($16.15 mid ×2 = $3,230, screening); kill 0 of 2. Paper book PB-0008 split under RULING D (PB-0008a CLOSED +141.30 / PB-0008b OPEN).
- **HYG (`IDEA-CREDIT-HYG-BDC-OCT23`):** NOT FIRED; void 4 of 5 (330/318/314/326); the 10/30 FRED cell decides Monday; leg (b) HTGC withdrawn on BROCK's Q3 grade.
- **ORCL (`IDEA-ORCL-PUTSPREAD-OCT23`):** NOT FIRED; DTCC 5Y disseminated 293 [10/30] vs 350; ORCL $130.67; void-line basis UNRESOLVED (model-derived 270–276 [10/29] vs ELLISON's unstated basis).
- **GLD (`MGMT-GLD-SHARES-OCT24`):** one-month line crossed at the 10/30 close ($355.78 < $360.71); record only; Will's WQ-554 word recorded on the card.

## 7. Ledger and hygiene
- SETUPS.tsv: 2 SHELVED rows (TRY-EXIT-USO35, TRY-COND-NCLHDEC14P) rotated verbatim → `../../archive/SETUPS_ARCHIVE_2026-10-31.tsv` (crc32 7e56daa3, 5,452 B), because this session's additions would have breached 75% of the read-cap budget (READ_CAP rule 5); 24,285 → 20,755 B before later edits. UNG row added; QQQ/HYG/ORCL/GLD rows updated. INDEX, TRADE_BOOK, CALIBRATION (CAL-0003), PAPER_BOOK updated.
- Ledger sweep A–H CLEAN after one fix (check G caught "Jan-15" vs "Jan-15-2027" on TRADE_BOOK, fixed).
- BOARD scan run: 0 new action-line signals naming TERRY since `SIG-W-20261023-045` (through `SIG-W-20261031-010`); 6 info-line signals read and logged (029-053, 030-002, 030-004 superseded; 030-005, 030-011 noted; 031-002 acted).
- R1: COR-20261031-02 receipted APPLIED (QQQ close 690.49 on the QQQ card; validated against TERRY's own fetch.py pull).
- Inbox: 7 of 7 packets read and consumed (dispositions in the PROME memo); `inbox/WILL/` holds only README/.gitkeep (no new Will drop).
- NEXUS ask (refunding card): **no card, because** the 11/4 supply surprise skews toward a long-bond cut (Treasury guidance + Citi), the haven bid runs against it, and BOND's duration-short kill is met; re-look on a size-raising QRA or a failed 10Y/30Y auction.
