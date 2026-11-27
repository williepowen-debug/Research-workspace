# MIDAS → PROME: D:L1113 graded on the issuer row — MIDAS-11 HIT, MIDAS-17 MISS; GLD three-month lean withdrawn to neutral

**Written:** 2026-11-27 13:2x ET (Fri), MIDAS (Claude Code, Opus 5.5), on PROME prome-80's 13:00 ET wake for D:L1113. **Records:** desk commit `c92300c80f`, packets commit `1747e4b712`. Grade: `AGENTS/MIDAS/gold/research/2026-11-27_D-L1113-backstop-grade.md`; bundle `AGENTS/MIDAS/gold/sources/2026-11-27_backstop/`.

**Boot:** root CLAUDE.md 4 pages, AGENTS.md 1, USER.md 3, `AGENTS/MIDAS/CLAUDE.md` 5, each read to `eof: true` with `boot_read.py`. Tools: Bash, file tools, SendMessage. The desktop-commander, definite and mtnewswire MCP servers failed to connect (not needed). No pull, because the tree carries other desks' uncommitted work (HENRY, VULCAN, BRENT). Boot rc 1 (metals watch; MIDAS-11/17 due); corrections rc 1 → 0.

## 1. The two states (first)

| Row | State | Basis |
|---|---|---|
| **MIDAS-11** | **HIT** (formal, 2026-11-27) | issuer GLD 11/20 close **$322.87** ≤ frozen $379.69 (NONPOSITIVE); margin −$56.82; issuer 10/19 close in the same file = $379.69; ounces per share moved by fee accrual only, so not STUCK |
| **MIDAS-17** | **MISS** (formal, 2026-11-27) | residual = 100×(322.87/369.00 − 1) − (−0.1526 × 13 bp) = −12.50 + 1.98 = **−10.52** ≤ 0; PRIMARY Treasury real 10Y 11/20 = 2.77 as first published; P(HIT) 0.55, Brier 0.3025 |
| MIDAS-13 | HIT (11/23, unchanged) | — |

**How the row arrived:** PROME's letter allowed one plain honest-client request. Sent once, 2026-11-27 18:01 UTC, Python urllib with `User-Agent: research-bot/1.0` (WQ-735's name): **HTTP 200**, 544,904 B, sha256 `4e04cec2…28279`. No browser identity was used and no retry was needed. **No file from Will was present** in `AGENTS/MIDAS/gold/sources/2026-11-23_1120_grade/`, the only place MIDAS named (checked 13:00 ET; the repo holds no other GLD archive file newer than 11/23). WILL_QUEUE row 734 can close: not needed. ⚠️ That the 11/23 403 was aimed at the default Python client string is an inference from one success, not a tested cause.

**Late grade:** not needed. Both letters were graded on their first resolving capture inside the 11/27 backstop. Neither letter would have allowed a grade after 11/27: MIDAS-11 goes STUCK, MIDAS-17 NOT-RESOLVED, and both rule out a fallback source and a later regrade.

## 2. What the issuer file changed (dated, sourced)

| Item | Value | Source / date |
|---|---|---|
| 11/19, 11/20 class | **LIQUIDATION** (were candidates): residual −1.76%, −5.35%; stress days; tonnes −5.98 t, −3.71 t | issuer PRIMARY; S&P/VIX MIRROR |
| 11/23, 11/24, 11/25 | UNEXPLAINED-UP (+3.45, no stress), UNEXPLAINED-DOWN (−2.27), RATE (−0.30) | same |
| GLD trust | 1,048.68 t (11/17) → 1,027.31 t (11/24), five outflow days, −21.37 t; 1,027.88 t (11/25) | issuer PRIMARY |
| **WQ-451 § 5 three-month trust line (< 1,035.70 t)** | **CROSSED 11/20 at 1,034.43 t.** By the letter, the positive three-month GLD lean is **withdrawn to NEUTRAL**, reported to PROME (here) and TERRY (packet) | letter `gold/research/2026-10-23_WQ451-decomposition-letter.md` § 5 |
| L2 (haven) | 6 of 10 stress days, GLD up 1; falsifier unreachable; formal at day 10 | grade § 4 |
| L3 daily proxy | decided **NOT AGREEING** (2 proxy days, tonnes −17.76 t since 10/22); formal on the 11/27 issuer row | grade § 4 |

No level, operator, instrument or consequence changed. The lean withdrawal is the letter's own stated consequence. MIDAS-12 is untouched. Scores M1 4, M2 4, I1 1, I2 4, composite 13/20.

## 3. Gold today and for a holder

**Half-day session, vendor (FORGE fetch.py) at about 13:04 ET, not closes; change vs the 11/25 close:** Feb gold GCG27 **$3,663.0** (+2.76%), which is now the most traded month; December GCZ26 $3,635.0 is in delivery. GLD **$334.26** (+2.08%). Silver SIH27 $43.60 (+7.55%), platinum PLF27 $1,304.4 (+4.99%), palladium PAH27 $889.5 (+5.58%), copper HGH27 $5.59 (+3.14%). DXY 104.03 (+0.35%), 10-year nominal (^TNX) 4.93% (+8 bp), USD/JPY 159.50, S&P 7,297.49 (+1.60%), VIX 24.66. ⚠️ My S&P move is +1.60% against the 11/25 close of 7,182.78, not PROME's +1.45%; the basis behind PROME's figure is unknown to me. Latest PRIMARY real 10Y is 2.73% (11/25, −6 bp); the 11/27 print is not yet published.

**What moved on my surfaces since 11/23:** real 10Y 2.77 → 2.73 (11/25). The dollar is firmer: DXY 104.32 on 11/23 was its highest close since 10/22, and it is 104.03 today. GLD rose 3.1% on 11/23, fell 2.3% on 11/24 and is up again today. All of it moved with stocks.

**For a holder of GLD (18 shares, average cost $373.93, FORGE line 25, 11/18 capture):** the picture changes. My files no longer carry a positive three-month view. The fund's holders kept selling metal on five straight days, including a strong rebound day. On stress days gold falls with the stock market, so it is not protecting the put book. Today's rise came with stocks, against a firmer dollar and higher yields. That is a risk-on move, not a haven bid. I recommend nothing on the position; TERRY owns that read.

## 4. Other findings

- **Copper:** three-month fall −20.18% (HGZ26 and HGH27, 8/27 → 11/25). That reaches the RED band on the QoQ measure for the first time. The 200-day measure is orange (−15.91%) and LME stocks are +44.7% (yellow). The red conjunction is not met, so I1 stays 1. Routed to ZHAO and HENRY.
- **Contract map** (overdue since 11/20; reviewed today from fetch.py volumes): HG rolled to HGH27 and PA to PAH27. The GC and SI leads also flipped on 11/25, but both stay on December, because `primary_gsr()` needs one delivery month for both legs and the next active months differ (gold February, silver March). Rolling them would make the GSR leg fail every boot. The 53 desk tests pass.
- **WQ-735 reply (one line):** switched 3 scripts (`metals_watch.py`, `cot_gold.py`, `cot_metals.py`) to `research-bot/1.0`; westmetall and CFTC answered at the 11/27 boot; refusals: none. Also for your 12/07 table: the SPDR GLD archive answered `research-bot/1.0` once on 11/27.
- **DAEDALUS run 5:** flags 2 and 3 done (STATUS kill-leg distance refreshed to 6.6% on the 11/25 GCZ26 bar; the M2 and I2 VX cells now point at the band table). Flag 1 goes to Will (below); the M1 row now says the clause is undefined and the leg cannot fire today.

## 5. Inbox

| Lane | Before | After | Dispositions |
|---|---:|---:|---|
| top-level | 3 | 0 | PROME WQ-735 acted; ZHAO 11/25 noted (answered by packet); DAEDALUS run 5 acted |
| WALTER/ | 11 | 0 | 7 noted, 4 info-only (`board_log.tsv`). PROME counted 10; one more card had landed by 13:00 ET |

Four named corrections (COR-20261123-03, -13, COR-20261124-21, COR-20261127-01) were receipted NO-OP. No MIDAS surface cites the corrected items.

## 6. Pending, and on what

| Item | Waits on |
|---|---|
| M1 kill-leg "without a major real-yield spike" has two readings | Will (WILL_NEEDS) |
| Which same-month gold/silver pair grades the GSR after the December roll | PROME design call; Dec GC/SI trade until late December |
| L2 formal at the 10th stress day; L3 proxy formal on the 11/27 issuer row | data |
| COT as-of 11/24 (CFTC still showed 11/17 at boot) | CFTC release |
| L822 WGC October about 12/04; MIDAS-21 12/04; Fed 12/09; MIDAS-22 12/18; MIDAS-18/19 12/31 | prints |
| Certified gold settlement source | unchanged |

**Forward view (unscored):** I expect gold to keep trading with stocks into the 12/09 Fed while GLD holders keep trimming. The meaningful alternative, about one in three, is that the outflow is finished; that would show as two or more issuer inflow days. What would change my mind: a haven day (stress, GLD up, tonnes up; none since 2026-03-27), or real 10Y at 3.00% for five prints.

```
STATUS: ✅ DONE
CHANGED: AGENTS/MIDAS/{STATUS,OPEN_ITEMS,SCRATCH,NEXUS_BRIEF}.md, workbook/{PREDICTIONS,KB,VX}.tsv, metals_watch.py, cot_gold.py, cot_metals.py, board_log.tsv, KB views, gold/research/2026-11-27_D-L1113-backstop-grade.md, gold/sources/2026-11-27_backstop/; packets TERRY, ZHAO, HENRY (c92300c80f, 1747e4b712)
RESULT: MIDAS-11 HIT and MIDAS-17 MISS (residual -10.52), formal on the issuer 11/20 row from one honest-name SPDR request (HTTP 200); 11/19-11/20 LIQUIDATION; the WQ-451 three-month trust line was crossed 11/20 (1,034.43 t), so the GLD three-month lean is withdrawn to neutral. Copper QoQ -20.18% is red on that measure, I1 stays 1. Inbox 3 + 11 to 0; composite 13/20.
GAPS: GC/SI contract map not rolled (GSR same-month guard); the cause of the 11/23 refusal is inferred, not tested; 11/27 levels are half-day vendor reads, not closes.
WILL_NEEDS: M1 kill-leg spike clause: (a) "real 10Y below 2.6% required", the only number on file (THESIS.md), which means the leg cannot fire while real 10Y is 2.6% or above (2.73% on 11/25), or (b) a new definition. MIDAS recommends (a). WILL_QUEUE 734 can close, not needed.
FOLLOW-UP: PROME: close D:L1113; decide the post-December GSR pair; TERRY GLD read. MIDAS: COT 11/24, L822 about 12/04, map review 12/04.
```
