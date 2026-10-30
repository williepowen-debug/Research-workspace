# MIDAS → PROME: GLD's July-low close break, tested for forced selling (WQ-554 hypothesis; C9 commission)

**Date:** 2026-10-30, written 16:54 EDT · **Commission:** PROME prome-c5, C9 class (PROME/CLAUDE.md § Done without asking): $0, one bounded session, inside MIDAS's charter, from the finding on the record (GLD's first close below the 7/16 low). **Hypothesis tested:** Will's, at WILL_QUEUE row 554 (RECENTLY DONE): forced selling, meaning winners liquidated to meet losses elsewhere. **Not re-presented, not recommended:** his "wait for a green day" word. No card (TERRY constructs; Will decides).

**Boot:** Claude Code, Opus 5.5. Bounded reads to `eof: true`: root `CLAUDE.md` 5 pages · `AGENTS.md` 1 · `USER.md` 2 · `AGENTS/MIDAS/CLAUDE.md` 5. `boot.py` rc 1 (metals; MIDAS-09/10/16 due; gold and Ag/Pt/Pd COT 10/27 unconsumed); after the session, COT legs are clear. Corrections rc 0. No pull: the tree carries DAEDALUS's dirty `GATE_LOG.tsv`; fetch showed origin == local.

## Result

**Study:** `AGENTS/MIDAS/gold/research/2026-10-30_july-low-break-liquidation-test.md`. Raw captures, hashes and scripts are in `AGENTS/MIDAS/gold/sources/2026-10-30_july-low-break/`.

| Question | Answer (source basis) |
|---|---|
| The break | GLD **$355.78, −3.47%** (MIRROR close; issuer row not yet printed). July 16 low was $364.96. Lowest close since 2025-10-02; −28.26% from the 1/29 peak. Volume about 4–7× the prior four days. |
| With or against macro drivers? | **Against.** PRIMARY Treasury real 10Y 2.63 → **2.60**, 2Y −5 bp, DXY −0.15%. The frozen WQ-451 beta implied GLD **+0.46%**, so the residual is **−3.93% (2.80 sd)**. The media story of "Fed hike bets" is contradicted by the 2Y falling on both 10/29 and 10/30. |
| Liquidation tape? | **Yes.** S&P −1.82%, QQQ −3.47%, IWM −1.65%, bitcoin −1.14%, copper −1.8%, VIX +2.22 to 19.42; only TLT/IEF were up. GDX and SLV fell 5–6%, but **in line with their normal betas**, so they add no extra stress signal. GLD fell 1.50 pp more than its equity beta predicts. |
| Frozen WQ-451 class, 10/30 | **LIQUIDATION-candidate.** The residual and equity-stress legs pass. The tonnes leg is **pending** until the issuer prints 10/30. 10/29 was UNEXPLAINED-DOWN on a calm day. |
| Flows (all predate today) | PRIMARY GLD trust **1,041.08 t (10/29)**, −16.54 t since 10/21, still +39.20 t vs 7/16. WGC week to 10/23: outflows **concentrated in North America, Europe adding** (PRIMARY text; the −$1.21 bn net is MEDIA). |
| COT as-of 10/27 (released today) | Legacy net/OI **46.9875%** (−2.70 pp), sixth straight decline. **Disaggregated: Other Reportables cut 14,956 longs; managed money ADDED 1,538.** Managed-money net (WGC futures+options tonnes) fell eight straight weeks through 10/20, 470.7 → 338.1 t, in an orderly way. |
| Correlation | 20-session GLD/SPY +0.72 (120-session +0.56). The 5-minute intraday correlation today, 0.53, is ordinary. Gold began falling overnight, before the US open. It made its low after stocks did and recovered less into the close. |

**Verdict, with confidence in plain words:**
- **Liquidation (selling gold for cash alongside everything else) was the proximate driver of today's break: moderate confidence.**
- **"Forced" (margin calls) is unproven.** We found no margin data and no October CME margin change. The COT and WGC flow data predate today. Public data cannot separate forced from voluntary de-risking.
- **"Winners" fits only partly.** Gold is −28% for 2026 buyers, though far up for 2022–25 holders.
- **The broader October decline is mixed.** The slide on calm 10/29 and three weeks of falls against easing rates (real −31 bp, GLD −7.49% since 10/9) point to a slower investor retreat, with high real yields as the backdrop. Liquidation sits on top of it, not instead of it.
- **What would distinguish the two (study §5):** under liquidation, gold rebounds when equity stress clears, outflows stop, Asian physical premiums firm, and managed money builds no shorts. Under a demand repricing, gold keeps falling on calm green-equity days, outflows spread across regions, managed money goes short, and central-bank Q3 buying comes in under 100 t.
- **Not yet testable:** China/India premiums are unheld, and WGC Q3 Gold Demand Trends was not found published.

**Standing conditions graded on the letter:**
- WQ-451 one-month downside line **$360.71: CROSSED** on a MIRROR close; confirm on the issuer print.
- WQ-451 3-month lines: **none crossed.** The "second liquidation day AND trust ≤ 1,035.70 t" line completes if the 10/30 tonnes fall by 5.38 t or more. If it crosses, the letter withdraws the positive 3-month lean to neutral, with a report to PROME and TERRY.
- **MIDAS-16 HIT** (46.9875 < 52.4490; Brier 0.09).
- MIDAS-09/10 not graded: frozen first retrieval is 11/2.
- **M1 flip ($4,050 / DFII10 ≥ 2.40): UNRESOLVED.** No certified settle is held. 10/29 $4,031.40 (MEDIA cites the CME preliminary bulletin) and the 10/30 quote of about $3,888 both sit below the line, with real yields at 2.63/2.60. **No score change. The certified-settlement source is now the only thing between M1 = 4 and M1 = 2** (composite 8 → 6).
- Kill-condition #3: no fire.
- SLV/PPLT/PALL d200 at −30.56/−24.16/−30.72%, all trend-level 4. Actual **8/20**, counterfactual **13/20**.

**No bounce-edge claim:** after the 11 earlier liquidation days, the 10-session forward residual was positive 64% of the time, the same as on all days. This is an instrument fact, not advice.

## Inbox drain (whole inbox, every sender; census before 5 top-level + 1 WALTER, after 0 + 0)

| Item | Disposition | Action |
|---|---|---|
| PROME 10/29 WQ-522 recorded + archive-rule answer | acted | Charter wording applied verbatim under C4 (`CLAUDE.md` § PREDICTIONS; no authority, route or threshold moved). PROME verifies the diff. |
| SAM 10/29 official-flow series | noted | KB-MIDAS-244: pointers only. If WQ-451 L3 ever adopts the H.4.1 custody line, LIQUID confirms the definition. L3 TIC grade 11/18 unchanged. |
| ZHAO 10/29 (orig. 10/16): −41.3% is June crude | acted | KB-243. OPEN_ITEMS I1 exclusion **CLOSED**: never copper. |
| DAEDALUS falsification-5 | acted, **DONE** | STATUS triad and labelled `Kill rail re-derived: 2026-08-07` line restored. Reply `AGENTS/DAEDALUS/inbox/2026-10-30_from-MIDAS_falsification-5-DONE.md`. |
| DAEDALUS wiring-17 run4 flag 10 | acted, **DONE** | `metals_watch.py` named again in the four VX threshold rows. Reply `…_wiring-17-run4-DONE.md`. |
| WALTER SIG-W-20261030-009 (Oyu Tolgoi / Mysteel) | acted (board_log) | Pause is real at MEDIA level: seismic event 10/29, restart begun 10/30. No Rio Tinto primary statement held. Mysteel claim ungraded; LME +16.6% vs median contradicts LME scarcity. No I1 change. |

Non-WALTER items are logged in KB plus `git mv` to `inbox/processed/`. The desk `board_log.tsv` enum is WALTER-only, so those five are logged here, not there. All six were moved with `git mv`.

## Disclosures

- **SKIPPED: weekly contract-map review due 10/30**, out of C9 scope. It is carried in SCRATCH item 4. 10/29 volumes show the named months dominant.
- **Consumer check skipped:** no threshold, band or published figure was superseded.
- **STATUS.md is 29,109 B (89% of read budget, rotate-tier advisory).** Not rotated: an archival split is out of scope and carries its own review budget.
- The MIDAS commit used `AGENTS/MIDAS/inbox` as a pathspec for my own staged `git mv` renames. Verified: commit contains only `AGENTS/MIDAS/` paths. PROME's own staged renames in the shared index were left untouched.

## COMPLETION — MIDAS — 2026-10-30
STATUS: ✅ DONE
CHANGED: AGENTS/MIDAS/{gold/research/2026-10-30_july-low-break-liquidation-test.md, gold/sources/2026-10-30_july-low-break/ (58 files), STATUS, OPEN_ITEMS, SCRATCH, NEXUS_BRIEF, CLAUDE.md (C4 archive wording), workbook/{KB,VX,PREDICTIONS}.tsv, KB_METALS, METALS_CATALOG, gold/README, 6 metal KB views, cot_*_consumed.tsv, board_log, inbox → processed ×6}; AGENTS/DAEDALUS/inbox/ ×2 replies
RESULT: GLD's 10/30 break ($355.78, −3.47%) came against easing real yields (2.63→2.60) and dollar, on a risk-off day with only Treasuries bid; WQ-451 reads LIQUIDATION-candidate (residual −3.93%, 2.8 sd; tonnes leg pending). Liquidation proximate = moderate confidence; "forced"/margin calls unproven; calm-day 10/29 slide and 3-week rate-insensitive decline mean slower investor retreat is also in play. COT 10/27: cut came from Other Reportables (−14,956 longs), managed money +1,538; MIDAS-16 HIT; WQ-451 one-month line $360.71 crossed, no 3-month line; inbox 6/6 drained.
GAPS: GLD 10/30 tonnes/close unpublished (class + 3-month line pending); China/India premiums and WGC Q3 GDT not held; no certified settle; contract-map review skipped (carried); COT/WGC predate 10/30.
WILL_NEEDS: None new — existing certified-gold-settlement source item is now load-bearing (would move M1 4→2, composite 8→6).
FOLLOW-UP: MIDAS next business day (11/2): grade 10/30 WQ-451 class + 3-month line on issuer tonnes (≤1,035.70 t ⇒ lean to neutral, report PROME+TERRY); MIDAS-09/10 retrieval; WGC weekly.
