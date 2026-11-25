# BRENT — EIA week 11/20, the Gulf and Red Sea overnight, live prices (2026-11-25)

Session brent-desk-agent-2026-11-25, woken by PROME prome-77 for DOCKET L1224 (boot 10:23 EST, times from `date`). Delivery packet: `PROME/inbox/2026-11-25_from-BRENT_l1224-eia-and-gulf-read.md`. Scripts here: `pull.py` (vendor one-minute and daily bars, captures c1 10:24:56, c2 10:31:14 and c7 10:42:26 kept in `raw/`; c3–c6 were lagged repeats and were trashed), `wpsr/fetch.sh` and `wpsr/evaluate.py` (EIA release-day files and the BRT-31/BRT-34 arithmetic; `wpsr/evaluation.json` holds the receipt with sha256 of every file).

## 1. Live prices, reconciled to one figure per contract (vendor one-minute bars, about 10 minutes behind; not settles)

cmegroup.com refuses this machine (IP block since 10/28; no evasion); no ICE page read. Prior settles are the vendor's daily bars for 11/24 (secondhand; Jan 91.40 matches The Nation's 11/24 settle via WALTER card 006).

| Contract | 11/24 settle (vendor daily) | 11/25, last bar before release (ET) | Change |
|---|---|---|---|
| **Brent January BZF27 (M1; last trade 11/30)** | 91.40 | **93.46 at 10:12** (93.12 at 10:23) | **+2.3%** |
| Brent February BZG27 (M2) = vendor `BZ=F` since the 11/18 roll | 88.78 | 90.06 at 10:14 (89.60 at 10:24) | +1.4% |
| Brent March BZH27 (M3) | 86.59 | 87.39 at 10:13 | +0.9% |
| WTI January CLF27 = vendor `CL=F` | 82.05 | 83.51 at 10:14 (83.11 at 10:24) | +1.8% |
| Heating oil January HOF27 | 3.6588 | 3.685 at 10:14 | +0.7% |
| RBOB January RBF27 | 2.4406 | 2.429 at 10:24 | −0.5% |

**The two figures PROME saw are one market on two contracts.** "Brent Jan $92.88" is BZF27; "BZ=F 89.52" is February, because the vendor's continuous ticker rolled to February on 11/18. In the same minutes (08:46 ET: Jan 92.88, Feb 89.48; 09:17 ET: Jan 92.89, Feb 89.55) the two figures sit about $3.40 apart, which is the January−February spread. **One figure: Brent January (BZF27) about $93.1 to $93.5 this morning, up about 2% on the 11/24 settle.** WALTER card 008's "Brent 89.21, −2.4% against 91.40" divides the February quote by the January settle: a mixed-contract artefact. February was up, not down. `thresholds.py` at boot read the same February ticker (89.97, +1.34%).

**Path overnight (BZF27, first bar each hour):** 90.15 at 00:12, 89.78 at 02:00, low 89.52 about 03:00, then a steady climb from 03:40 ET (European morning) to 93.5 by 10:00. The Ras Tanura claim reached the wire at 07:01Z (02:01 ET, Newsquawk via WALTER card 008); price fell for the next hour. **No single news minute carries the rise; its cause is not established.**

**Curve (same capture, about 10:13 ET):** M1−M2 +3.40 against +2.63 at the 11/24 window; M1−M3 about +6.07 against +4.81; M2−M3 +2.67 against +2.18. The front steepened while flat price rose. ⚠️ January expires 11/30 on thin volume (vendor daily January 8,151 lots against February 17,755), so part of M1's lead is expiry-week mechanics; February−March also widened by about $0.49, so not all of it. My unregistered description from 11/17 ("M1−M3 above about +6.3 while flat price rises") is close (+6.07) but not met.

**EIA reaction (capture c7, 10:42 EST; the vendor runs about 11 minutes behind, so only the first two minutes after 10:30 are visible):** muted. WTI January 83.20 at 10:29 → 83.16 at 10:30 → 83.09 at 10:31 (718 lots); Brent February 89.76 → 89.66; heating oil 3.677 → 3.671; RBOB 2.436 → 2.434. No January Brent bar printed 10:26–10:31 (thin expiring contract). A crude build at 97.5% runs and flat gasoline demand gave the tape nothing new.

## 2. EIA Weekly Petroleum Status Report, week ending 11/20 (released Wed 11/25 10:30 ET, holiday week)

Own capture from `ir.eia.gov/wpsr/` with the honest client name `research-bot/1.0` (WQ-735): release seen 10:30:11 EST, files saved 10:30:58 EST. Before 10:30 the server answered 403 with its "outside of a release window" page, which is an embargo, not a client refusal; `wpsr.csv` still answered that page after release (not published this week, not a block). `table1.csv`, `table2.csv`, `table4.csv`, `table9.csv`, `psw01.xls`, `psw09.xls` and the retail workbook all 200.

| Series | Week 11/20 | Week 11/13 | Change |
|---|---|---|---|
| Commercial crude (WCESTUS1) | 418,906 kb | 417,797 | +1,109 (build; 3% below 5-yr) |
| Cushing | 25.613 M | 26.147 M | −0.534 M (5.6 M above the 20 M floor) |
| SPR | 273,465 kb | 276,361 | −2,896 |
| Refinery utilization | **97.5%** | 95.7% | +1.8 points (TRACKER line 3 stays crossed, highest this window) |
| Crude runs | 17,346 kb/d | 16,918 | +428 |
| Crude exports | 3,269 kb/d | 4,488 | −1,219 |
| Crude imports | 6,250 kb/d | 5,576 | +673 |
| Gasoline stocks | 217,682 kb | 215,949 | +1,733 |
| **Distillate stocks (WDISTUS1)** | **105,616 kb** | 104,901 | +715 (6% below 5-yr) |
| Jet stocks | 43,204 kb | 44,143 | −939 |
| Gasoline supplied, weekly (WGFUPUS2) | 8,714 kb/d | 8,790 | −76 (8,726 a year ago) |
| Distillate supplied | 3,917 kb/d | 3,785 | +132 (4-wk +3.9% YoY) |
| Total commercial stocks | 1,222.567 M | 1,224.938 M | −2.370 M |

### BRT-31 week seven (owner grade by the letter)

- **NON-QUALIFYING: −0.2190237797%** (4-wk 8,769.75 against 8,789.0 kb/d; current 8714, 8790, 8767, 8808; base 2025-11-21 8726, 11-14 8528, 11-07 9028, 10-31 8874). No revisions to prior inputs. EIA's own summary line reads −0.2% on rounded averages.
- **Price leg:** GASREGW 11/23 $3.642 against 2025-11-24 $3.061 = +18.98%, the first window week under +20%: counter 1 of 3, one week left, so the precondition cannot fire.
- **Decided:** MET unreachable; NOT MET ruled out 11/12. **Window-end label NO-VERDICT** (or NO-VERDICT-CONTAMINATED only if a listed tax cut takes effect by 11/27), written at the week-11/27 print, about 12/02. Both labels are excluded from calibration. Row OPEN at 40% until then.
- **What it means:** the single qualifying week (11/13) was a base effect, not a volume fall. US gasoline volume held flat on last year while retail fell from $4.15 (11/2) to $3.64 (11/23). Not "volume resilient" (that label belongs to NOT MET, which is out of reach).

### BRT-34 third window print

- **105,616, not below 95,000; 10,616 above the line.** Four prints left (11/27, 12/4, 12/11, 12/18). YES needs draws averaging about 2,654 kb a week, at 97.5% utilization. OPEN at 45% as registered; my unregistered view is about 5%.

## 3. The Gulf and Red Sea overnight: what is established and what is not

| Item | Established at a primary or named source | Not established |
|---|---|---|
| Ras Tanura (Gulf side; refinery 550 kb/d, terminal about 6.5 mb/d loading capacity, The National) | Coalition spokesman Turki al-Maliki: four drones intercepted and destroyed over Ras Tanura, fragments fell, no injuries in a first assessment (The National, updated 12:59 local 11/25; WALTER card 008). Defence Ministry separately: two drones, then one more, in the Eastern Province | Any hit on the refinery or terminal; any fire at the plant (Saree's claim only); any Aramco statement; any loading change. The "600 sq km of smoke" (Reuters on NASA imagery, relayed by one outlet) establishes smoke, not its source. The phrase "temporarily disrupted some of Aramco's operations" refers to PREVIOUS attacks in The National's text, not to 11/25 |
| Hodeidah | Coalition struck Houthi "operational capabilities" at Hodeidah port early 11/25 after warning civilians to leave (The National; Reuters 03:26Z via WALTER 006); severity "not immediately clear" | A second strike at 12:48Z (Al Mayadeen via Newsquawk, CLAIM ONLY); whether Saree's 11:52Z conditional warning is new or a late relay (WALTER 008/010 open) |
| Houthi threat to Saudi ports | Retaliation against Yemeni ports will be met with attacks on Saudi ports (The National); 11/20–23 emails named Jeddah (WALTER 025) | Any attack on a Saudi Red Sea port, tanker or loading berth: none found (WALTER 008, 010; The National 11/25). No carrier, port, insurer or loading notice found |
| Hormuz 11/24 | UKMTO: three vessels struck by unknown projectiles 22 Nov (same event as card 017, counted once) | IRGC mine and container-ship claims (CLAIM ONLY, no hull named). Transit counts are three instruments, never blended: MarineTraffic 125 vessels 11/17–23 (226 on 11/1–7); JMIC 114 assisted passages 19–21 Nov; one AIS platform 28 ships, 4.18 M barrels in 24 hours |
| Kazakhstan | — | 1.74 mb/d on 11/24, about 0.36 mb/d under its November average, on unstable CPC loadings (unnamed sources via Newsquawk, WALTER 010; CPC and ministry not read) |
| Tanker cyber | — | "As many as 50" tankers targeted (WSJ via Maritime Executive, WALTER 003); an administration official says no evidence of Iran and "a minor nuisance". No ship disabled, no insurer action |
| Bahrain Sitra (FALCON 11/21 ask) | Bapco CEO 11/18: Sitra weeks from full capacity, hit six times this war (The National 11/18) | Any Bapco or BNA statement after the 11/21 attack: none found 11/25. No product read owed |

**Barrel read.** Nothing read today removes a barrel. Ras Tanura matters for two different things: the refinery (550 kb/d; a hit is a product event, crude-bearish at the margin, cracks up) and the terminal (its exports must still pass Hormuz; Kpler had Ras Tanura at 2.95 mb/d for 10/1–25 against 4.16 in September, Gulf News 10/31). The Red Sea side carries the larger loss if hit: Yanbu about 2.5 to 3.1 mb/d of crude plus up to about 1 mb/d of west-coast products (11/24 note), with OPEC surplus capacity about 0.01 mb/d (EIA STEO 11/10). The Houthi condition for striking Saudi Red Sea ports has now been met on 11/20 and 11/25 with no port hit found after either. The Kazakhstan item, if real, is about 0.36 mb/d for one day, unconfirmed. **The tape:** Brent January +2.3% and a steeper front with no confirmed loss is a risk premium being re-bid, larger than last night's shrug, partly expiry-week mechanics.

## 4. Registered rows touched (no level, operator, instrument or consequence moved)

| Row | Read today | State |
|---|---|---|
| BRT-31 | week 7 −0.2190%, non-qualifying | OPEN; window-end label NO-VERDICT (or -CONTAMINATED) at the 12/02 print |
| BRT-34 | 105,616 | OPEN, 10,616 above the line |
| BRT-33 | intraday M1−M3 about +6.07 (not a window read) | OPEN; windows 11/25 and 11/27 read from one capture at the next wake (see packet) |
| BRT-32 (Yanbu halt) | no stated halt | OPEN, 20% as registered |
| BG-02 R1 | no hull sunk, no cargo loss, no loading halt | NOT MET |
| COT-FUEL-35B | #16 releases 11/30 | unchanged |
| BRT-23, BRT-28 | regraded to the letter under C10 | `../../thesis/prediction_notes/2026-11-25_regrade-BRT-23-BRT-28.md` |

## 5. Forward view (my projections; not registered)

| Call | Horizon | Odds | Why | What would change it |
|---|---|---|---|---|
| BRT-33 resolves NO at the first read after 11/27 | 11/30 read | about 98% NO | M1−M3 about +6 this morning; the line is +3.50; 11/27 is a holiday-shortened session that may print no window bar at all | a front collapse of about $2.5 in two sessions (a ceasefire with flows) |
| A Saudi Red Sea loading halt stated by Aramco, the ministry, SPA, Reuters or Bloomberg (BRT-32 letter) | to 12/31 | about 20% (registered 20%) | threat condition met twice, nothing carried out; Houthi fire went to Ras Tanura on the Gulf side instead | any hit on Yanbu, Jeddah or a loading berth |
| Brent January expires 11/30 above $90 | 11/30 | about 70% | 93 now, risk premium re-bid, steep front | a Hormuz or Qatar-channel deal headline; OPEC+ 11/29 surprise |
| US distillate under 95,000 by 12/18 (BRT-34) | 12/23 release | about 5% | runs at 97.5% and builds three weeks running | an export surge or a big refinery outage |

**Meaningful alternative:** the risk premium re-bid fades as on 11/16–11/18 (front fell 3.5% within two days of the tanker hits) if no strike follows the Ras Tanura attempt by the weekend. **Investment implication:** none from me; TERRY packeted for a tradeability read, no card asked.
