# VIOLET: Nvidia Q3 FY27 close read, credit-vol WATCH endpoint, 11/18 SOQ plan

**Written:** 2026-11-17, 16:5x ET (from `date`). Task: PROME prome-19 wake on the two CATALYSTS rows dated 11/17 (DOCKET D:L926). Claude Code, Opus 5.5.
**Basis:** every 11/17 VIX-complex value is the **Cboe delayed-quote close print (16:14:31 ET last trade), basis TICK until Cboe History posts** (not posted at 16:47 ET; History's last row was 11/16). VX settles are CFE 11/17 settlements. Post-release figures are delayed quotes, not closes. Snapshots: `snaps/` (raw JSON per pull); capture script `snap.sh`.

## 1. The surface into the release (11/17 close print vs 11/16 History)

| Measure | 11/16 History (SETTLE) | 11/17 close print (TICK) | Change |
|---|---:|---:|---:|
| VIX | 22.91 | **25.46** (row; snapshot 25.45), high 27.73, low 22.39 | +11.1% |
| VIX9D / VIX9D:VIX | 23.15 / 1.0105 | 26.70 / **1.0487** | front week dearer |
| VIX3M / VIX3M:VIX | 23.02 / 1.0048 | 24.98 / **0.9811** | **inverted** |
| VIX6M | 23.79 | 25.37 | under spot |
| VVIX | 114.23 | **121.28** (row; snapshot 121.16), high 127.85 | **over 120** |
| COR1M | 16.42 | 20.18 | +22.9% |
| VX/X6 settle (expires 11/18 AM SOQ) | 22.5309 | **24.7417** | +9.8% |
| VX/Z6 / F7 / G7 settle | 21.1059 / 21.2827 / 21.3889 | 22.6881 / 22.6527 / 22.8088 | +7.5% / +6.4% / +6.6% |
| X6 over Z6 | +6.8% | **+9.05%** (strict M1:M2 −8.30%) | premium grew |
| SKEW | 146.33 | no 11/17 bar (quote stamp 11/16 17:00) | not read |

## 2. Through the release (results about 16:20 ET; VULCAN owns what it states)

| Instrument | Before | After | Source and basis |
|---|---:|---:|---|
| VX/X6 last | 24.73 (16:00 pull) | 24.10 (16:30 pull), **24.00 (16:46 pull)** | Cboe futures quote API, delayed; source gives no trade time |
| VX/Z6 last | 22.60 | 22.20 | same |
| VX/F7 / G7 last | 22.58 / 22.73 | 22.33 / 22.49 | same |
| NVDA | 155.46 (15:59 bar) | 161.20 (16:30), 158.95 (16:46) | yfinance 1-min, after-hours quotes, **not closes** |
| ES front future | 7,356.50 (16:15) | 7,387.50 (16:30), 7,380.75 (16:36) | yfinance 1-min |

**Read (inference, one evening, delayed quotes):** the release took some premium out but did not drain it. X6 fell 0.74 (−3.0%) from its 24.7417 settle; the back months fell 1.4% to 2.2%. X6 still sits **+8.1% over Z6** (24.00 / 22.20). The market still expects tomorrow's SOQ well above December. NVDA was up 2% to 4% after hours and ES up about 0.3%: a relief tape, not a shock.

The release, per WALTER card SIG-W-20261117-019 (read at the Nvidia primary; VULCAN owns its meaning) reported:
- a beat: revenue $115.8B, Data Center $107.6B;
- a Q4 guide of $130.0B ± 3%, including an extra week, with no China data-center compute assumed;
- a gross-margin guide of 71.0 to 72.0%, against 74.8% GAAP in Q3;
- Kress as interim CEO, with a CEO search and an independent board committee investigation referenced.

The governance thread is still open in the release itself, which keeps a non-earnings carrier alive past the SOQ.

## 3. Against what I wrote before it (11/16 record, KB-VIO-399)

| 11/16 statement | Outcome tonight |
|---|---|
| The premium sits in the window the Nvidia reaction sets (X6 settles 11/18) | **Held, and it grew before the print:** X6 over Z6 went from 6.8% to 9.05% on the settle, and VIX9D/VIX from 1.0105 to 1.0487. Part of it came off after the release (X6 −3.0%). |
| Invalidators of the "event-specific and short" read sent to TERRY: (a) HY +15bp in a session | **NOT MET:** 323 [11/13] → 334bp [11/16], +11 over one session. 11/17 unpublished. |
| (b) VVIX over 120 | **MET on the print:** 121.28. |
| (c) VIX3M/VIX under 1.000 | **MET on the print:** 0.9811. |
| (d) A VIX close over 25 that holds past 11/18 | **First half met:** 25.46. The hold is pending. |
| (e) VIX9D/VIX above 1 after 11/18 | **Pending** until after the SOQ. |
| Earnings vs governance premium (open hypothesis) | **Not testable tonight.** The test is VIX9D/VIX after the SOQ. The new BIS chip-licence rule and China's vow of countermeasures (WALTER SIG-W-20261117-007), plus Huang offering to return (SIG-W-20261117-013, titles only), are non-earnings carriers that outlast the SOQ. |

**Net:** two of my five invalidators of "event-only, short" hit **before** the release. On the print, the premium was not only Nvidia's earnings. The after-release tape gave back about 3% of X6 and 2% of Z6, not the whole premium.

## 4. VIOLET-owned outbound rows graded on the print (TICK until History)

| Row (CLAUDE.md trigger table) | Letter | Grade |
|---|---|---|
| Regime shift LOW_VOL → RISING_VOL | 11/16 History 22.91 ≥ 20.00 | **FIRED on History (SETTLE, 0 corrected).** All desks via NEXUS_BRIEF |
| Term structure inverts, VIX > VIX3M | 25.46 > 24.98 | **MET on the print.** 🔴 LIQUID, HENRY; a peak-marker, not an onset (KB-VIO-034). First since 11/06 (0.9594) |
| VVIX > 120 | 121.28 | **MET on the print.** 🟠 RED, HENRY. First since 11/06 (121.94) |
| VIX +30% in 5 days, credit flat (HY 5-session change ≤ +25bp, first-published FRED, same sessions) | 11/10 19.46 → 11/17 25.46 = **+30.83%**; HY 330 [11/10] → 11/17 **unpublished** (needs ≤ 355bp) | **VIX leg MET; credit leg PENDING** the FRED 11/17 cell (11/16 334 = +4). 🔴 HENRY, RED, sent as conditional |
| VIO-PRED-08 (VIX close ≥ 30.00 by 11/20) | window high 25.64 [11/06]; 25.46 tonight | **OPEN:** 4.54 short, 3 sessions left. No early grade |

None of these changes a level, operator or consequence. They are existing rows applied.

## 5. What did not move

- **Credit:** HY OAS 334bp [11/16], CCC 13.10% [11/16], FRED first-published; the 11/17 cell is not out. LIQUID owns the series.
- **Back of the curve:** VIX6M 25.37, and Z6/F7/G7 settles flat at 22.65 to 22.81 (adjusted Z6→F7 −0.16%).
- **Oil vol:** OVX/VIX 1.94, CALM [11/17].
- **Carry:** JPY RV10 6.14%, p26.0, CALM [11/17].
- **Rates vol:** MOVE 101.28 [11/16]; 11/17 not read.
- **Positioning:** CFTC report 11/10, leveraged money net −34,762, p36.5, NORMAL.

## 6. Credit-vol WATCH endpoint (KB-VIO-328), window 10/13 to 11/17

- **Size condition:** +100bp from 268bp [9/22], so **368bp**.
- **HY path (FRED BAMLH0A0HYM2, own cache pulled 11/17 15:58 ET):** 316 [10/13] → peak **348 [11/05]** (+80) → 320 [11/12] → 334 [11/16].
- **Grade: CLOSED, size condition NOT MET** on every cell through 11/16. The 11/17 cell (posts 11/18) changes this only at ≥ 368, which needs +34bp in one session.
- **Lag:** not measurable. No Path A credit event occurred, so there was nothing to time vol against.
- **Over the same window VIX went 15.27 [10/13] → 25.46 (TICK) [11/17]** without credit meeting its size condition. That is the Path B shape (concentration, governance, policy), not a credit lead. It is a watch, not a letter (WQ-611 A).

## 7. 11/18 row (VIX November AM SOQ)

It cannot be graded tonight. What it needs:
- the SOQ (VRO) and X6 final settlement, published Wednesday morning;
- VIX9D/VIX after the SOQ (the earnings-vs-governance test);
- the FRED 11/17 HY cell (it closes both the WATCH endpoint and the credit leg of the +30% row);
- History for 11/17, to confirm tonight's TICK fires.

**Wake asked: Wednesday 11/18, 11:00 ET**, after the SOQ prints and after LIQUID's third cell (about 10:50 ET per PROME). The reason is the 🔴 +30% row's credit leg, which is time-sensitive to HENRY and RED. If no wake is given, everything grades at the next ordinary session. Only timeliness is lost.
