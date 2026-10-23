# MIDAS — STATUS

**COT as-of 10/20 (released 10/23 15:30 ET, consumed):** gold net long 49.68% of OI, −2.77pp, **fifth straight weekly decline**, first below 50% since 7/28 (92nd pct); longs −8,158 contracts while shorts were flat, so this is long liquidation. Silver 17.37% (−3.51pp), Pt 18.67%, Pd −36.66%. The week ends before 10/22. MIDAS-16 was registered before this release.

**News sweep 2026-10-23 (Will-directed):** `shared/research/2026-10-23_gold-silver-news-sweep.md`. New: Russia's central bank selling gold for a 10th straight month (−6.2t Sept, ~−62t since Dec 2025) as a named offset to official buying; Goldman ESTIMATES 79t Aug central-bank buying vs WGC REPORTED 39t; Chinese banks ending retail leveraged metals trading; no October CME margin hike found; India ~6,500t silver import permits (premium $2.50 → $0.45/oz); China a net silver exporter; a 13.75% Shanghai silver 'premium' is mostly VAT. Today (14:57 ET) yields +3.5bp, dollar +0.2%, gold −1.25%: an ordinary rates-and-dollar day, unlike Thursday. WALTER SIG-021 noted (board_log). No score/prediction change.

**Predictions registered 2026-10-23 (Will-directed, rows committed before 15:30 ET):** MIDAS-13 GLD any issuer close ≥ $378.95 by 11/20 (P 0.50) · MIDAS-14 SLV d200 ≤ −20% at 11/2 close (P 0.70) · MIDAS-15 PALL d200 ≤ −25% at 11/2 (P 0.35) · MIDAS-16 gold COT as-of 10/27 < 52.4490% (P 0.70) · MIDAS-17 GLD beats rate-implied path 10/22 → 11/20 (P 0.55). Letters and base rates in `workbook/PREDICTIONS.tsv`; WQ-451 letter tests are DOCKET L819–L822 (PROME-registered).

**Catch-up October 23, 2026 (Will-directed, Fri; started 13:37 ET, first commit 13:49 ET):** `shared/research/2026-10-23_catch-up.md`, captures `shared/sources/2026-10-23_catch-up/`. **October 22 was a liquidation day:** every metal fell with equities (S&P −1.21%, Nasdaq −2.60%) while PRIMARY Treasury 10Y real fell 2.76 → 2.64, 10Y nominal 5.13 → 4.96, 2Y 4.81 → 4.65, DXY flat. Media "rate-hike bets" attribution is contradicted by those moves and not adopted. PRIMARY GLD bullion −11.98t on 10/22 (1,045.64t), ~−10t since 9/30, reversing the 10/20 accumulation read. **M1 flip rule (gold < $4,050 AND DFII10 ≥ 2.40 → M1 2): NOT fired on the 10/22 vendor close $4,060.40 (+0.26%); 10/23 trading ~1% below the line. A secondary source says 10/22 settled $4,042.80 (below; unverifiable) → 10/22 and 10/23 both UNRESOLVED, certified-settle retrieval Mon 10/26; CME blocks this box's IP.** Band counterfactual on post-approval data: SLV d200 first < −20% on 10/14 (now −24.16%) and PALL first < −25% on 10/22 (−26.76%) → would-be M2 4 / I2 4, counterfactual 13/20, one shared root; **actual 8/20 unchanged until the 11/1 21:40 ET floor**. LME copper +47,525t in four sessions to 272,950t (+16.9% vs median, benign), mostly US warehouses on tariff-arb unwind, not China demand. CFTC 10/13 vintages consumed (CFTC reachable again; 403 cleared). Inbox: DAEDALUS WQ-508 packet filed (lines already applied in `f4149bf51`, none contested); **PROME WQ-451 commission (gold haven vs de-dollarisation decomposition letter) received, NOT yet executed — kept in inbox.** Tree had foreign uncommitted WALTER work at boot → no pull.

**Session state 2026-10-23:** older dated blocks (10/12–10/20 closeouts, the 10/12 news update, superseded evidence lines and the old top-3) moved verbatim to `analysis/STATUS_ARCHIVE_2026-10.md` (audit `analysis/2026-10-23_desk-audit.md`). WQ-421 was APPROVED 10/15 and consumed 10/20; it is not open. Five boot legs: metals, ledger age, predictions, gold COT, Ag/Pt/Pd COT.

## Dated evidence

| Metal | Named contract | Oct 22 vendor Close | Oct 19 → Oct 22 | Oct 22 ETF Close |
|---|---|---:|---:|---:|
| Gold | GCZ26.CMX, Dec 2026 | $4,060.40 | −2.40% | GLD $369.00 |
| Silver | SIZ26.CMX, Dec 2026 | $55.007 | −3.96% | SLV $49.34 |
| Platinum | PLF27.NYM, Jan 2027 | $1,576.90 | −4.33% | PPLT $14.20 |
| Palladium | PAZ26.NYM, Dec 2026 | $1,056.60 | −5.89% | PALL $19.12 |
| Copper | HGZ26.CMX, Dec 2026 | $6.398/lb | −2.71% | CPER $38.47 |

*October 23 refresh; the October 9 table it replaces is in git history and the 10/12 news-sweep bundle.* GSR 73.82 (10/22, same-date same-month). DFII10 2.64% 10/22 PRIMARY Treasury (FRED 10/21 2.76). LME 272,950t 10/22 MIRROR. COT 10/13 consumed: gold 52.4490% (p95.97, fourth decline), silver 20.8710%, Pt 19.1156%, Pd −34.8595%. Older paragraph below retains its October 9–12 dates.

Yahoo MIRROR daily bars are **uncertified exchange settlements**; the newest futures row is excluded and native price precision retained. **Real yield:** PRIMARY Treasury real par curve 10Y **2.64% on 10/22** (FRED DFII10 2.76 on 10/21; BOND owns the level). **LME copper 272,950t on 10/22** (Westmetall MIRROR), +16.9% vs the 233,500t 2-year median, benign; the build is mostly US warehouses (MEDIA Reuters). Contract map reviewed 10/23 on 10/22 volumes, next review 10/30.

## Domain and scoring state

| # | Channel | Score (1–5) | Local state | Independence | Key signal [source/date] | Upgrade trigger |
|---|---|:---:|---|---|---|---|
| M1 | Gold / real rates | **4** | Rate-driven slide plus a 10/22 liquidation day (WQ-451 instrument); not a stress hedge in 2026 | Monetary root shared with M2 | PRIMARY 10Y real 2.64% (10/22); GLD trust 1,045.64t (10/22); COT 49.68% (10/20) | Flip to 2: certified settle < $4,050 with DFII10 ≥ 2.40 — **UNRESOLVED 10/22–10/23** |
| M2 | Silver / GSR | **1** (would-be 4) | SLV trend red since 10/14 (post-approval); no physical squeeze evidence | Monetary and industrial roots | GSR 73.82; SLV d200 −24.16%; COT 17.37% (10/20) | Scores after the 11/1 21:40 ET floor at its then-current level (MIDAS-14) |
| I1 | Copper / China | **1** | LME build is a US tariff-arbitrage unwind, not China demand | China/industrial root | LME 272,950t; HGZ26 $6.398 (10/22); Teck strike possible 10/24 | Copper −20% AND LME +100% |
| I2 | Platinum / palladium | **2** (would-be 4) | PALL red 10/22, PPLT orange; one root with silver | Industrial plus precious/supply roots | PALL d200 −26.76%, PPLT −18.27% (10/22); Nornickel 9M 10/26 | Scores after the floor (MIDAS-15); confirmed SA/Russia disruption rule |

**Composite: actual 8/20; counterfactual 13/20** with the shared-root flag (silver 10/14 and palladium 10/22 within 15 sessions).

**CROSSING recommendation approved October12** in response to the sit-rep; approval evidence `analysis/2026-10-12_WQ-368-CROSSING-APPROVAL.md`. PROME completed shared WQ-368 writeback; no further approval owed. The floor remains **November1 21:40ET**, all numerical bands unchanged. Reviewed counterfactual11/20 is diagnostic. PPLT−15% crossedOctober7 after approval and recovered; PALL−20% crossedOctober1 before21:40 approval, no qualifying recross throughOctober9. Trend state does not latch an old cross. October12 SLV/PPLT/PALL d200=−17.30/−13.22/−22.37%; crash legs decayed1 and upside legs1. No new T/C/S crossing onOctober12. Earlier crossing history throughOctober9 remains unchanged.


| ETF (Oct 22 close) | d200 / T level | C dd252 / decayed level | S upside / level | Would-be max |
|---|---|---|---|---:|
| SLV | −24.16% / **4** (first < −20% 10/14, re-cross 10/22) | −53.28% / 1 | 1 | **4** |
| PPLT | −18.27% / 3 (re-cross −15% 10/14) | −43.71% / 1 | 1 | 3 |
| PALL | −26.76% / **4** (first < −25% 10/22) | −48.58% / 1 | 1 | **4** |

Oct 22 crossings are post-approval data; method reproduces the 10/12 values exactly. Would-be M2 4, I2 4 → counterfactual 13/20 with shared-root flag (Ag 10/14 and Pd 10/22 within 15 sessions). Actual stays 8/20 before the 11/1 floor; state legs score at their level after the floor, no latch. The October 12 note below is history.

## Held GLD and standing rails

**Position update 10/23:** **GLD 25 sh** per FORGE `ec5a7058b` (Will's 10/22 11:01 ET capture: BOUGHT 1 on 10/22 @ $371.41; basis $9,390.78; $9,302.00 at that capture's mark) — the book's largest line; PROME 10/23 confirms 10/23 activity touched no GLD. Corrects the "24 sh" (10/20 vintage) cited in PROME's 10/21 packet. Broker/Will truth controls. Beta arithmetic from the October 11 vintage (17 shares) is archived.

Gold's structural diversification relevance does not establish positive real-rate hedging. September PRIMARY WGC global ETFs+67t/+US$10bn, holdings4256t; not GLD-specific flow. Rechecked Q2 CB demand288.9t above100t floor; old Q1~244t revised57t. Monthly August reported39t is a different incomplete object. Historical VECTOR3 two-win falsifier stands.

Standing weekly rail (boot, Friday-as-of): 9/25 → 10/16 DFII10 −9bp, GLD −2.90%, three joint-up signs False/False/False → **no kill-condition-#3 fire**; historical 7/17 → 8/7 fire stays 1/4. Legacy $3,317 shelf not near. The $4,050 flip rule is in the scoring table above.

## Open on MIDAS — top 3

1. **Certified gold settle (Mon 10/26):** grade the M1 flip rule for 10/22 and 10/23. A standing certified-settlement source is missing (CME blocks this box's IP) — **Will's decision** (broker statement vs approved data access).
2. **Calendar:** Nornickel 9M grade 10/26 (pre-registered, `palladium/research/2026-10-23_nornickel-9M-read-setup.md`) · MIDAS-09/10 and MIDAS-16 on 10/30 · floor 11/1 21:40 ET → MIDAS-14/15 on the 11/2 close · DOCKET L819 11/06, L820 11/07, L821 11/18 · MIDAS-11/13/17 11/20 · L822 ~12/04.
3. **M1 successor DRAFT** (`analysis/2026-10-12_M1-successor-DRAFT.md`): review due 10/19 is overdue and the draft is unregistered — retire-or-register decision (the WQ-451 instrument may supersede it). Evidence gaps are listed in `OPEN_ITEMS.md`.

Full obligations `OPEN_ITEMS.md`; mechanisms `THESIS.md`; today's audit `analysis/2026-10-23_desk-audit.md`.

## Bottom line

As of October 22–23, 2026, all metals are in a broad de-risking selloff that is not explained by rates: gold, silver and the platinum-group metals fell with stocks while Treasury real yields dropped 12bp and the dollar held flat, and GLD shed 12 tonnes of bullion in one day. The single most important reading is gold against the $4,050 flip line — it closed 0.26% above on 10/22 and trades ~1% below today; a settle below it drops M1 from 4 to 2. Silver and palladium have both crossed their red trend lines on post-approval data, which would lift the composite from 8 to 13 once the November 1 floor passes if they stay there. Copper's LME stock jump is a US tariff-arbitrage unwind, not a China demand signal; next catalysts are the Teck strike (10/24), Nornickel (10/26) and the FOMC (10/27–28).

Gold: GCZ26 Dec 2026 **$4,060.40/oz [Oct 22 MIRROR vendor Close]**, −2.40% vs Oct 19; ~$4,008 intraday Oct 23; liquidation and GLD outflow (−11.98t) against falling real yields.
Silver: SIZ26 Dec 2026 **$55.007/oz [Oct 22]**, −3.96% vs Oct 19; ~$54 intraday; fell ~2.2× gold on 10/22; SLV trend leg red (−24.16%).
Platinum: PLF27 Jan 2027 **$1,576.90/oz [Oct 22]**, −4.33% vs Oct 19; ~$1,560 intraday; PPLT trend −18.27% (orange); BMI forecast cut on weak car sales (MEDIA).
Palladium: PAZ26 Dec 2026 **$1,056.60/oz [Oct 22]**, −5.89% vs Oct 19; ~$1,047 intraday; PALL first below −25% red line 10/22; Nornickel 9M due 10/26.

All futures prices are uncertified vendor closes; October 23 values are intraday. News mechanisms are hypotheses, not attributions.
