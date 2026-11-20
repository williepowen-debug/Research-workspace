# BRENT — diesel and refining commission (D:L783), close of the late-November window

**Run:** 2026-11-20, PROME prome-77 due-row wake (letter written 11:59:04 ET; this session booted 11:59 ET from `date`). Bounded. Research only: no trade, threshold, basis, gate letter or holding grade. `$0` moved. First deliverable: [10/21 REPORT](../2026-10-21_diesel-commission/REPORT.md); interim read: [11/06 NOTE](../2026-11-06_diesel/NOTE.md).

## Bottom line

1. **The question the commission asked has been answered by the market, and then overtaken.** The December crack (HOZ26 × 42 − CLZ26) went below the $90.16 SELL line on **11/2 ($89.2472, vendor daily, TERRY's source ②; CME never read)**. TERRY wrote the SELL; Will sold the one original Valero share on 11/5 at $366.665 (GATE-TERRY-VLO-HELD-01 RESOLVED EXECUTED, PROME/GATES.tsv). Leg A of that gate took no new observations after 11/19. The two Valero shares Will added carry no TERRY rule (FORGE D-78), so **no live line on any Valero card reads this crack today.**
2. **"Before expiry" is today.** CLZ26's last trading day is **Friday 11/20** (CME rule: three business days before the 25th of the prior month; 11/25 is a Wednesday). After today's settle there is no December pair to observe; HOZ26 runs to 11/30 against no crude leg.
3. **BRENT's governing December crack estimate: about $82.1/bbl on 11/20** (vendor daily row 82.1042 at the 11:50 ET bar, intraday, thin CL volume 8,717 on the expiry day [EST, not a settlement]); the 14:28–14:30 ET window read is in [§ Window](#window-read-1428-1430-et) once taken. It is **$8.06 under $90.16** and the lowest December reading in three months (high $107.45 on 10/13). Mean daily change over the last 20 sessions −$0.78, s.d. $2.57.
4. **Direction since 10/21: down $13 (−13.6%)**, with the US stock print turning and crude falling. The scarcity premium is still very high by history (my 11/6 note put $90.59 at the 99.9th percentile of 1987–2024 front cracks), so this is an unwind from an extreme, not a return to normal.
5. **FALCON's Kpler relay is NOT verified at a source.** Neither Kpler's site nor the pages a fetch helper read (Gulf News, Kpler blog 11/3, OilPrice 11/20) carry "all-route Middle East shipments about 64% of pre-war, against 97% in October" or "Hormuz crude 8.5 mb/d preliminary through 11/16". **Label stays: relayed (AP via Gulf News live blog per FALCON), preliminary, not read at the source.** It is the one figure this week that could mean fewer barrels; the falling crack says the market is not trading it.

## Window read (14:28–14:30 ET)

*(filled after the window; see `../2026-11-20_brt33/NOTE.md`)*

## 1. December crack path, 10/19 → 11/20 [vendor daily rows, EST, not settlements; `out_crack.txt`]

| Date | Dec crack | Jan crack | Note |
|---|---|---|---|
| 10/13 | 107.45 (3-month high) | 104.19 | |
| 10/21 | 95.09 | 92.82 | Commission start; governing 95.0479 was the window read |
| 10/29 | 90.68 | 88.86 | |
| **11/2** | **89.25** | 87.23 | **First below 90.16 → SELL rec, share sold 11/5** |
| 11/3 | 94.20 | 91.27 | Rebound |
| 11/4 | 88.51 | 85.59 | Crude −8% day |
| 11/13 | 90.30 | 87.69 | Last December row above 90 |
| 11/16 | 85.72 | 83.51 | |
| 11/18 | 83.58 | 81.05 | ⚠️ 11/18 and 11/19 rows carry identical vendor volumes (27,707 / 104,865): the 11/19 row is a vendor artefact class (memory: daily bar read after the evening open); prices differ, treat 11/19 as EST |
| 11/19 | 82.75 | 79.74 | Last authorised leg-A date (no live reader) |
| 11/20 | 82.10 | 79.57 | Intraday 11:50 ET; CLZ26 expiry day |

## 2. Dated catalyst table, brought current (direction is for the distillate crack: ↓ lowers it, ↑ raises it, ± unclear)

**Fired and graded since 10/21**

| Date | Event | What happened | Source tier | Direction |
|---|---|---|---|---|
| 10/28, 11/4 | EIA WPSR | Distillate fell to **99.259M** (week 10/30), lowest since 5/2/2003 | P (EIA) | ↑ then; priced (11/6 note) |
| 11/2 | December crack below 90.16 | $89.2472 vendor daily; SELL written; sold 11/5 | Vendor (TERRY ②) | — |
| 11/4 (awards) | **NEHHOR exchange** | DOE awarded **300,000 bbl** of ultra-low-sulfur distillate from Boston and New Haven storage (energy.gov award notice dated 11/4, read via search, page not opened). Completion date conflicts: **11/6** (DOE bulletin, search summary) vs **11/13** (RFP/press). Deliveries completed: **NOT CONFIRMED** | P (DOE, via search) | ↓ small, regional (300k bbl ≈ 0.3% of US distillate stocks) |
| — | "DOE releasing 50M bbl diesel over four months" (Senate release) | Still found nowhere at DOE. Treat as the G7 100M package restated, not new US barrels | Government relay only | — |
| 11/1 → | Russia: producer exemption from 11/1; producer ban to **1/31/2027** (decree №1436, YURI) | Exports allowed in tranches; refinery damage binds | P via YURI | ↓ small |
| 11/5–11/10 | US-bound Russian diesel cargoes | Two of three diverted (Brazil, Mediterranean), third "for orders"; none confirmed delivered to the US (OSPREY KB-274, AP/AFP) | Secondary | ± (barrels sell elsewhere) |
| 11/12, 11/18 | EIA WPSR | Distillate **103.330M** (+4.071M, week 11/6), **104.901M** (+1.571M, week 11/13); utilization 95.2% → 95.7% | P (EIA) | **↓** stocks rebuilding, refiners running hard |
| 11/13 | IEA OMR | Diesel "overriding concern"; European diesel 77% above pre-war [secondaries]; Q4 surplus is a FORECAST | Secondary ×5 (iea.org 403) | ± |
| 11/18 | Reuters (two industry sources), via Kyiv Independent | **Russian refinery processing ~700k t/d (end-October) → ~400k t/d: −43% on the stated tonnes** (headline says 45%); 15 of 35 major refineries disrupted in 20 days. Runs, not measured damage. COR-20261119-14 applied: the 43% figure is the one used here | Secondary (Reuters not read) | ↑ (world buffer) |
| 11/19 | Shenzhen declaration (kremlin.ru, YURI) | Point 2: "the three states plan to increase production and supply of refined petroleum products". **Not a Russian export decision**; the producer diesel ban to 1/31/2027 stands (YURI). Putin closed the energy and sea truce talks after the bridge strikes | P (kremlin.ru via YURI) | ± (statement of intent only) |
| 11/19 | Crimea fuel purchase limits (Sevastopol: full tank + 20 l); bridge road closed since 11/17, rail reopened | OSPREY, Kyiv Independent | Secondary | ± local, no export effect |
| 11/19 | Kaleykino (Transneft, Tatarstan, Druzhba feeder) tanks hit; General Staff confirms 11/20 | No Druzhba flow effect reported (OSPREY) | Secondary | — (crude, not product) |
| 11/19 | Citgo Lemont: unit shut after flaring (Quantum title) | Unit not named, duration unknown; **title only** | Headline | ↑ tiny, Midwest |
| ~11/20 | **China October product exports** (the modeled GAC row) | Customs total refined products **5.18 Mt, −27.7% m/m from 7.16 Mt** (includes marine fuel, so not comparable with the ~3.7 Mt clean-product approval); no customs diesel split found; one report 313 kb/d October diesel, unsourced | Secondary (Reuters via Baird Maritime, search summary) | ↑ (less Asian diesel), September's 1.85 Mt diesel was a 3-year high |
| 11/20 | Iran "moves to restart oil exports" (OilPrice 11/20, read by a fetch helper) | **Intent, not a measured flow.** One ship-to-ship crude transfer from a sanctioned Suezmax (Bloomberg citing UANI and Kpler); a Reuters/TankerTrackers STS loading paraphrased; Kpler: Iran production 1.8 mb/d, half pre-war. CENTCOM: any vessel receiving Iranian-linked STS cargo becomes a blockade-evasion target (undated in the article; FALCON verified the 11/18 advisory at Reuters' text) | Secondary; no volume | — crude; no product effect |

**Forward (open)**

| Date | Event | Source tier | Direction | What to read |
|---|---|---|---|---|
| **Fri 11/20 14:28–14:30 ET** | Last December-pair observation (CLZ26 expiry) | Vendor proxy | — | § Window |
| Mon 11/23 | EIA retail diesel and GASREGW | P | — | Pump pass-through of the crack fall |
| Wed 11/25 | EIA WPSR week 11/20 (no holiday shift; EIA schedule read 11/19 by the routine) | P | Third build ↓ / draw ↑ | BRT-34 third print; four-week exports |
| 11/26–11/27 | Thanksgiving: driving and flying peak | — | ± | Jet and gasoline, small for diesel |
| Sun 11/29 | OPEC+ January decision | P (statement) | Moves crude, both legs | Crack sign unclear |
| Mon 11/30 | HOZ26 last trade | Exchange | — | No crude partner after today |
| Early December | China November product exports (quota up 25% but shipments lag, Mysteel) | Secondary | ↓ if shipments catch up | |
| Mon 12/21 | **CLF27 last trade** (business day before 12/25 is 12/24; three business days before = 12/21) | Exchange rule | — | End of the January pair |
| ~end-December | Jazan (400 kb/d) expected back (Kpler 10/21) | Secondary | ↓ | Red Sea product exports |
| 1/31/2027 | Russian producer diesel ban expires | P via YURI | ↓ if not extended | |
| 4/7/2027 | OFAC GL 135 (Russian diesel) expires | P | ± | |

## 3. Forward view — PROJECTION (BRENT's judgment, not evidence; unscored, no row registered)

- **What I expect:** the January crack (HOF27 × 42 − CLF27, $79.57 at 11:50 ET) **stays below $90.16 through CLF27's last trade on 12/21.** My estimate: **about 20%** that it settles at or above $90.16 on any session before 12/21; **about 5%** that it reaches $100 (the diesel-buffer combo check).
- **Why:** US distillate has rebuilt 5.6M barrels in two weeks with utilization at 95.7%; crude is in its third weekly fall with the surplus showing at sea; the January crack already sits $2.5 under December, so the curve prices easing.
- **Model reference, not my number:** a driftless walk on the last 20 and 40 sessions' daily s.d. ($2.39, $3.06) over 20 sessions gives 32–44% for $90.16 and 6–14% for $100. I mark below it because the last 20 sessions averaged −$0.80 a day and each support (Russian runs −43%, Gulf product exports, China's October cut) was already known while the crack fell.
- **The meaningful alternative:** the world buffer is thinner than the US print (combo:diesel-buffer): Russian product exports keep falling, the Kpler route figure proves to be lost barrels, or a cold December in the Northeast meets 104.9M of stocks still about 8% below the 5-year. That path re-widens the crack fast; the 10/13 high was $107.
- **What would change my mind:** two consecutive WPSR distillate draws larger than the season norm (~2.3M) with exports back toward 1.7 mb/d; a Kpler or Vortexa primary showing Gulf product exports falling further in November; a Russian halt on producer exports before 1/31.
- **Not registered:** no fixed line reads this crack after today, and no position rule depends on it. Named here as an unscored outlook.

## 4. For TERRY (WQ-696 handoff, sent by packet)

The evidence implies the US distillate scarcity premium is unwinding from an extreme: December crack −$13 since 10/21 to about $82, January about $80, with US stocks rebuilding. Horizon: through the January pair's 12/21 expiry. Invalidated by a renewed run of large distillate draws, a measured fall in Russian or Gulf product exports, or the January crack back above $90. Unknown: the Kpler route figure (unverified), European stocks (unread), and how much of the fall is crude-led versus product-led. It supports no new BRENT-originated idea; whether the two added Valero shares (no TERRY rule, D-78) need a read is TERRY's call.

**Sources:** vendor daily bars (yfinance, `daily-vendor.json`, pulled 2026-11-20 ~12:00 ET); EIA WPSR weeks 10/30, 11/6, 11/13 (BRENT TRACKER, primary); energy.gov NEHHOR award notice (node 4861302, via search) and DOE GovDelivery bulletin (search summary); OilPrice 11/20 (Charles Kennedy, read by fetch helper); Kpler blog 11/3 (read by fetch helper, October basis only); Reuters-via-Baird Maritime China October exports (search summary); Mysteel November plans (title); WALTER cards SIG-W-20261118-014, 20261119-003/-004/-005/-014, 20261120-006; FALCON packet 11/19; OSPREY packet 11/19; YURI via WALTER correction 014; PROME/GATES.tsv rows 18 and 20; FORGE/STATUS.md D-78.
