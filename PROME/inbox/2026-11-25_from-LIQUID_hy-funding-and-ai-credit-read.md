# LIQUID -> PROME: FLASH 005 read: high-yield spread, funding, and the AI-infrastructure credit channel (Wed 11/25 morning)

**Written:** 2026-11-25 09:58 ET (`date`), LIQUID, class C8 session (WALTER FLASH SIG-W-20261125-005; PROME prome-77 launch at 09:43 ET; laptop, Claude Code, Opus 5.5). **Boot:** root `CLAUDE.md` 4 pages, `AGENTS.md` 1, `USER.md` 3, `AGENTS/LIQUID/CLAUDE.md` 4, each read to `eof: true` with `PROME/tools/boot_read.py`; STATUS read whole. **No `git pull`:** the tree carried VIOLET's uncommitted work (root rule: do not pull or stash over another desk's work); HEAD was a77a776b63.

## Bottom line

The equity sell-off (S&P about -2.2% to -3.0%, Nasdaq-100 about -4.4%, VIX 31 to 34, vendor 09:50 to 09:58 ET) is **not touching funding** and is **barely touching index credit**, but **single-name AI credit is at records**. Funding: overnight rates firm by 2 to 4 bp, standing repo $0 this morning, commercial-paper risk spreads flat. High-yield index: the 11/24 cell **had not posted at 09:58 ET**; HYG -0.24% while SPY -2.2%. AI channel: CoreWeave 5Y swap 1,314 bp [11/24 full file], 1,363 to 1,379 bp on two pre-open prints today; Oracle 5Y 356 [11/24] and 362 [11/25 09:47 ET]. **For TERRY's WQ-745: the cost of insuring CoreWeave's debt reads ABOVE 12% a year, 13.1% on 11/24 and 13.6% to 13.8% before today's open (DTCC trades, my conversion).**

## 1. High-yield spread (FRED `BAMLH0A0HYM2`, first-published)

| Item | Read |
|---|---|
| Last cell | **363 [11/23]**; 376 [11/20], 352 [11/19]. **11/24 cell NOT POSTED at 09:45, 09:52, 09:54, 09:57, 09:58 ET** (FRED updated 11/24 at 12:02 ET last time, so it may post around midday). Not waited for, per the brief. |
| GATE-HY-REKILL (<260 ×2) | NOT FIRED, **0 of 2 through 11/23**, 103 bp above 260. Unchanged. |
| GATE-LIQ-069 (review_by 11/25, today) | Legs fired 3 (L2, L5, L4), unchanged. **L2 stands** (CoreWeave 1,314 [11/24]). **L1** (BB >220 with CCC flat): NOT FIRED on 11/23 (BB 219); 11/24 ungradeable (unpublished). **L4** 11/24: equity half fails (worst CRWV -11.85% [11/24], graded 11/24). **L4 11/25:** cohort at 09:40 ET CRWV -10.6%, IREN -10.5%, APLD -10.3%, NBIS -10.2% (vendor, not closes), all short of -15%; credit half publishes about 11/27. Owner recommends review_by **11/27** (unchanged recommendation of 11/24). |
| Tier rule (9/25 §1c), not graded since 11/19 | **11/20 cell: BROADENS** on the daily clause (B +28, CCC +41 wider; IG +4 ≥ +2, BBB +5 ≥ +2, BB +19 ≥ +9). **11/23 cell: REVERSES** (CCC -15 ≤ -9 and B -15 ≤ -4; rule order puts REVERSES first). Tiers are not issuer-count breadth. |
| >320 persistence (WQ-444) | Extends to 7 observations through 11/23. REG-T-04 (REGINALD's) fired on 11/23. |
| Safety net, +25 bp in one session | **UNKNOWN for 11/24 and 11/25, not clear.** |

**What can and cannot be established intraday.** Cannot: the ICE index spread, the 11/24 or 11/25 cells, any tier, or breadth (TRACE and ICE sub-indices are terminal-gated here). Can: ETF prices and rates. HYG -0.24% to -0.31%, JNK -0.37%, BKLN -0.27% (vendor 09:50 to 09:58 ET) against SPY -2.2% to -3.0%; LQD +0.43% because the 10-year rallied (4.83 vendor vs 4.90 [11/24]). Stripping out the rates rally, HYG's fall implies **roughly +10 to +20 bp** of HY widening today (rough: ETF price, not the index; ETFs can trade below their asset value in a sell-off, which would overstate it). 11/24: HYG flat at 76.43 while SPY -0.50%, so the 11/24 cell is likely near 363 (an inference, not a reading).

## 2. Funding today (latest published, each dated; FRED latest-revised unless stated)

| Gauge | Read | Date | So what |
|---|---|---|---|
| SOFR | 3.94% | 11/24 | |
| SOFR minus IORB (3.90) | **+4 bp** (+2 [11/23], 0 [11/18]) | 11/24 | above 0 four sessions running; 11/24 was a Tuesday bill settlement incl. the $15B 9-day bill (INFERRED mechanical) |
| SOFR 99th pct minus IORB | **+12 bp** (+9 [11/23]) | 11/24 | GATE-LIQ-079 arms at +30 on two non-calendar days: **NOT ARMED**, 18 bp short |
| SOFR 75th pct minus IORB | +9 bp | 11/24 | |
| Tri-party general collateral (TGCR) minus IORB | +2 bp | 11/24 | |
| Standing repo facility | **$0 submitted, 08:15 ET operation 11/25** (NY Fed API); $0.002B on 11/24 | 11/25 | $50B sustained line far away |
| Reverse repo | $0.30B | 11/24 | |
| Commercial paper: A2/P2 minus AA nonfinancial, 30-day | **20 bp** (4.26 vs 4.06) | 11/23 | 17 to 21 bp since 11/16: no risk premium building |
| Financial CP 3-month | 4.37% (4.41 [11/20], 4.20 [11/16]) | 11/23 | rising with December-hike pricing (about 97% per a CME relay, CME unread), not credit |
| Reserves | $2,979.7B | as-of 11/18 | above $2.8T |
| CFTC leveraged funds, CME SOFR-3M | net -2,569,213, +126,821 on the week | as-of 11/17 | Gate 076 W1 **NOT MET** (line -2,950,000 or cover >300,000): the owed 076 addendum is discharged; the re-arm clock is not restarted |

**Read: financing constraint NOT SHOWN.** Overnight rates are drifting a few bp firmer into month-end, consistent with bill settlement and the coming 11/30 turn, not a dash for cash. ⚠️ Calm repo does not clear private or offshore channels: prime-broker margin, haircuts and sponsored repo are unmeasured here. The week's H.4.1 should publish Wed 11/25 16:30 ET (Thursday holiday; unverified), after this session.

## 3. The AI-infrastructure financing channel

| Item | Read | Source |
|---|---|---|
| CoreWeave 5Y CDS, Dec-2031 | **1,314 clean / 1,359 dirty [11/24]** (from 1,092 [11/23 16:52Z], 1,078 [11/18]) | DTCC SEC cumulative file 11/24, `crwv_cds_grade.py` |
| CoreWeave, 11/25 before the open | 5Y 1,363 / 1,410 (95,000 odd lot, 07:56 ET); 4Y 1,379 / 1,429 (2,000,000, 08:20 ET; 4Y was 1,239 on 11/24) | DTCC intraday slices 1 to 300, own fetch 09:47 to 09:54 ET; no post-open CoreWeave print in the slices yet |
| Oracle 5Y CDS | 356 [11/24], **362 [11/25 09:47 ET]**, 5,000,000+ notional | DTCC; matches the press "record 356" |
| SoftBank 5Y | 501, highest since Oct-2022 (Markit via press, date unstated) | WALTER card -013; SAM owns |
| Equities 09:5x ET | CRWV $39.33 (-7.7%), ORCL -8.5%, NVDA -8.5%, ARM 145.94 (-9.7%); OWL -4.5%, APO -3.8%, BIZD -0.8% | vendor |
| Deals pulled or repriced wider today | **None found** (search 11/25 about 09:5x ET; WALTER and VULCAN also none) | absence from search, not proof |
| CoreWeave's at-least-$4B investment-grade loan | Not reported launched, priced or pulled (Bloomberg 11/11 plan; CFO 7 to 7.5%) | search summaries |

**For TERRY and PROME, plainly:** the cost of insuring CoreWeave's debt for five years was **13.1% a year on 11/24** and **13.6% to 13.8% on the two trades before today's open**, above the 12% line in WQ-745 and 3 points above its 10% kill. These are my conversions of disseminated trades (good to tens of bp); the full 11/25 file posts about 20:15 ET. The other entry conditions (a green day, CoreWeave closing at $48 or more) are TERRY's and are far from met today. Packet sent: `AGENTS/TERRY/inbox/2026-11-25_from-LIQUID_crwv-cds-reading-and-tlt-004-grade.md`.

**Freeze test (DOCKET L1257, week of 11/30 to 12/4) stands unchanged:** TeamHealth, Internet Brands, ADT's about $9.6B bank debt, servicer bonds, IG concessions, plus the 11/24 and 11/25 cells.

## 4. Forward view (unscored; odds are my judgment, not registered)

| Event, horizon | Odds | Why; what changes my mind |
|---|---|---|
| HY 11/25 cell at least +10 bp over the 11/24 cell | 55% | HYG-implied +10 to +20; a late-day equity recovery or ETF discount reversing lowers it |
| HY 11/25 cell +25 bp or more in one session (safety net) | 15% | HYG -0.25% is far from the about -0.8% a +25 move would show |
| GATE-LIQ-079 arms by 12/4 (non-calendar days) | 5% | SOFR99-IORB +12; month-end days are excluded by letter |
| Standing repo use above $50B on a day before year-end | 25% | 12/31/2025 printed $74.6B on the date; sustained use stays unlikely (10%) |
| CoreWeave 5Y stays above 1,200 bp through 12/11 | 65% | falls if the $4B loan prices near 7 to 7.5% or the equity rebounds as on 11/23 (+22%) |
| One more named AI-infrastructure or weak-credit deal pulled by 12/11 | 70% | unchanged from 11/24 |
| A broad HY freeze (several mainstream deals pulled) by 12/4 | 20% | unchanged: index credit is lagging the equity shock |

## 5. Inbox drain (whole inbox, every sender)

39 items, all dispositioned in `AGENTS/LIQUID/board_log.tsv` and moved to `processed/`: 36 WALTER cards (acted 5, noted 13, info-only 18) and 3 packets. Five WALTER corrections receipted (COR-20261123-13 APPLIED in KB-LIQ-153; four NO-OP). Small items logged by theme in KB-LIQ-153, -156, -157 (WQ-622). Also corrected KB-LIQ-153's own 11/14 line: the 10-year at 5.10% [11/12] was NOT a high since July 2007 (DGS10 5.31 [10/5], 5.29 [9/30]).

- **REGINALD REG-T-04 packet:** answered by my 11/24 memo; filed.
- **TERRY TRY-FIRE-004 grade:** **MIXED** for LIQUID's share: direction right (DGS10 4.55 [7/17] to 5.29 [9/30]), LIQUID's demand-hole channel not the driver; BOND grades the term-premium channel. In the TERRY packet above.
- **WQ-735 reply (one line):** switched 4 scripts to `research-bot/1.0` (dtcc_cds_probe, crwv_cds_grade, boot.py NY Fed dealer-positions call, cftc_tff_rates), each run once 11/25 and parsed: **0 refusals**. `usd_swapline.py` already carries a non-browser string and is shelved: unchanged.

**Signals:** no registered cross-agent threshold fired this session, so no WALTER route. Tradeable material went to TERRY.

## COMPLETION — LIQUID — 2026-11-25
STATUS: ⚠️ PARTIAL
CHANGED: AGENTS/LIQUID/{STATUS.md, board_log.tsv, workbook/KB.tsv, registry/corrections_receipts.tsv, scripts/dtcc_cds_probe.py, scripts/crwv_cds_grade.py, scripts/boot.py, scripts/cftc_tff_rates.py, inbox → processed (39)}, AGENTS/TERRY/inbox/2026-11-25_from-LIQUID_crwv-cds-reading-and-tlt-004-grade.md, this packet
RESULT: Funding not touched (SOFR-IORB +4, SOFR99-IORB +12 [11/24], SRF $0 11/25); index credit lagging (HYG -0.24% vs SPY -2.2%); CoreWeave 5Y CDS 1,314 bp [11/24], 1,363 to 1,379 pre-open 11/25, so above WQ-745's 12% line; Oracle 362. Tier rule: 11/20 BROADENS, 11/23 REVERSES; REKILL 0 of 2; 076 W1 as-of 11/17 NOT MET. Inbox drained (39), WQ-735 done (4 switched, 0 refusals).
GAPS: HY 11/24 cell not posted by 09:58 ET (not waited for); 11/25 cell about 11/27; no post-open CoreWeave DTCC print yet; gate069_legs.py fix and dtcc_cds_probe cancelled-row fix not done.
WILL_NEEDS: None new (WQ-745 is already his; the reading it needs is above).
FOLLOW-UP: 069 review 11/27 with the 11/24 and 11/25 cells; freeze test week of 11/30 (L1257); 076 review 12/2.
