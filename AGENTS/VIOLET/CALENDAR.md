# VIOLET CALENDAR

VIX-specific catalysts and monitoring schedule. **Source of truth for dated catalysts: `workbook/CATALYSTS.tsv`** (machine feed for `scripts/catalyst_countdown.py`). This file is the human twin and must not diverge.

---

## VIX EXPIRATION DATES (Monthly)

VIX futures and options expire on the **Wednesday 30 days prior to the third Friday of the following month**.

| Month | Expiration Date | Notes |
|-------|-----------------|-------|
| ~~Apr 2026~~ | Apr 15 | EXPIRED |
| ~~May 2026~~ | May 20 | EXPIRED. Episode-17 VIX 25C expired worthless 5/19. |
| ~~Jun 2026~~ | Jun 17 | EXPIRED — quarterly. Resolved clean alongside FOMC (no pin stress; VIX +12% on the hawkish dot, then faded). M1 (war-premium carrier) expired with it. |
| **Jul 2026** | **Jul 15** | Standard monthly. FOMC Jul 29 same month. |
| Aug 2026 | Aug 19 | — |
| Sep 2026 | Sep 16 | Quarterly (same day as FOMC + SEP). |

**Pin risk:** VIX tends to drift toward strikes with high open interest near expiration.

---

## FOMC MEETINGS (Vol Events)

| Date | Meeting | VIX Watch |
|------|---------|-----------|
| ~~Apr 28-29, 2026~~ | FOMC | DONE — held 3.50-3.75%, 4 dissents (most since Oct 1992, Powell's last cycle). VIX did NOT spike. |
| ~~Jun 17, 2026~~ | FOMC + SEP | **DONE — Kevin WARSH's first meeting as chair.** Held 3.5-3.75% **12-0**, but dot plot flipped HAWKISH: 2026 median **3.4→3.8%**, **9 of 18 project a hike** (6 project two); Warsh submitted no dot, 130-word statement, dropped forward guidance. VIX **+12% on the day (~18.44)** then faded (6/18 16.40). **Rate-shock leg RE-ARMED → Fed-HIKE regime.** |
| **Jul 28-29, 2026** | **FOMC** | No SEP. Warsh presser only. Decision Wed Jul 29. **First FOMC of the new Fed-HIKE regime — tests 6/17 dot-flip follow-through.** |
| Sep 15-16, 2026 | FOMC + SEP | Quarterly — critical. Decision Wed Sep 16 = same day as VIX Sep quarterly expiry. First SEP after the hike-signal flip. |

**Pattern:** VIX typically rises into FOMC, drops on outcome if no surprise. The GEX-era absorption held through 6/17 even on a hawkish surprise (+12% spike faded in a day, counter 0/5) — refresh hypothesis on each FOMC outcome.

---

## EARNINGS SEASONS (Vol Supply)

| Quarter | Peak Earnings | VIX Impact |
|---------|---------------|------------|
| ~~Q1 2026~~ | Apr 15-May 2 | DONE — vol supply realized, VIX did not spike |
| Q2 2026 | Jul 15-Aug 1 | — (overlaps Jul 15 VIX exp + Jul 29 FOMC) |
| Q3 2026 | Oct 15-Nov 1 | — |
| Q4 2026 | Jan 15-Feb 1 | — |

**Pattern:** Earnings season = vol supply as single-stock vol gets realized. **Concentration watch:** with record AI/semi concentration (47%) + record levered-ETF exposure ($464bn), a single AI-name earnings gap is the most likely Path-B vol trigger this cycle.

---

## ACTIVE FORWARD CATALYSTS

| Date | Event | VIX Implication | VIOLET Checkpoint |
|------|-------|-----------------|-------------------|
| **Jul 2, ~11:30 ET** | **Post-DISH CCC print** (7/1 data, FRED T+1; next print may slip past the 7/3 holiday) | First print with the DISH prepack cleared: persistence = Bin-A upgrade; retrace = composition-artifact | 🔴 **Gate A adjudicates TODAY** (KB-VIO-110); pairs LIQUID breadth (Gate C). |
| ~Jul 10 | SK Hynix ADR Nasdaq listing (single-source — verify) | Semis capital-rotation event (MU + SK Hynix both >$1T) | 🟡 Watch. |
| **Jul 14** | **June CPI** | Energy-collapse pass-through test; **HENRY flip-tripwire catalyst** (thin cushion to the 7,437-7,471 flip) under a hawkish Fed | 🟠 Next macro vol-gate after today. HENRY/CARL own substance. |
| Jul 15 | VIX July expiration | Standard monthly; Q2 earnings season opens same week | ⚪ Low. |
| **Jul 16** | **Japan double-discriminator: May TIC (4PM ET Thu) + MOF ITS wk-7/5-7/11 (~7:50PM ET Wed 7/15) + BoK** | Carry→vol transmission channel (VIOLET-chartered read; SAM owns substance). SAM resolver: ≥+¥500B durable / <¥0 transient-confirmed | 🟠 **Added 7/11 (Will-approved wave).** VIOLET watch: USDJPY 10d RV 5.62% [7/10] vs 3y p50 8.35 (near-floor calm) + FXY ATM IV ~11.4% [7/10] ≈ 2× RV (event premium priced). JPY-vol instrument scoped, not built — `research/2026-07-11_jpy-vol-instrument-scope.md`. |
| Jul 29 | FOMC (no SEP, Warsh) | Tests 6/17 dot-flip follow-through; hike optionality live post-Sintra (~70% Sep odds priced) | 🟠 First gate of the Fed-HIKE regime. |
| Sep 16 | FOMC + SEP + VIX Sep quarterly expiry | Quarterly dot-plot convergence; ~1 hike priced by Sep | 🟠 Next major gate. |

**Note:** the Path-B unwind is **unresolved and broadened** (KB-VIO-106) — bear case now oversupply-2028 + demand-destruction + antitrust, with a standing offshore mechanical amplifier (KOSPI 2x single-stock ETFs, ~$9B, jawboning-only response). Undated watch lines: KOSPI 8,200 (crash close — break re-opens contagion) · Korea FSS leveraged-ETF ruling (vol-suppressing if it lands) · SKEW >150 sustain count (1/4 td toward prediction-#6 re-arm).

**Resolved (7/2):**
- **7/2 June employment (8:30 ET):** +57K big miss / net revisions −74K / U-3 4.2% via participation −0.3pp (supply artifact) / AHE 3.5%↑ = **stagflationary mix**; tape evolved dovish-muted → hawkish-lean (10Y 4.50 +3bp) — absorbed by the freshly-POSITIVE gamma regime (+$35B, HENRY). **Gate B NO-FIRE (KB-VIO-111).** Candidate MOF yen strike on the 8:30 bar (162.5→160.7, UNCONFIRMED — SAM). +57K single-source, re-verify.

**Resolved (6/24-6/30) — the gap window:**
- **6/24 MU Q3 AH:** blowout beat (rev $41.46B vs $35.69B est; HBM booked thru CY2027) → MU +15.7% 6/25 — then the sector relapsed 6/26 (Samsung/SK-Hynix capex-leak oversupply read) and again 7/1 (MU −10.6%, below its 6/23 panic close). The fork "cleared" for one session; unwind unresolved (KB-VIO-106).
- **6/25 May PCE:** headline 4.1% YoY in-line / core 3.4% (+0.1); monthly prints soft → read softer-than-feared; 10Y to 4.36% by 6/29 — then re-hawked 6/30-7/1 (Warsh Sintra, ISM 53.3): 10Y ~4.50, ~70% Sep-hike odds (KB-VIO-109).
- **6/30 Quarter-end rebalance:** front-ran itself into the 6/23-6/26 chop, absorbed via rotation — SPX +1.18%/+0.79% on the peak-flow days; Q2 closed +14.9% (best since 2020), SOX +87.8%. Mechanical-flow excuse for SKEW extension now CLEARED (KB-VIO-108).

**Resolved (6/16-17) — the catalyst window:**
- **6/16 BOJ MPM:** As-priced 1.00% hike (7-1, Asada dovish dissent); yen WEAKENED to ~160.4, NO carry unwind (Aug-2024 analog did not replay). Carry → Sep-18 convexity tail (SAM; 60d unwind 24-28%). Vol-DEFUSED.
- **6/17 FOMC + SEP (Warsh's first) + VIX June quarterly + M1 expiry:** see FOMC table. Hawkish dot-flip, +12% spike faded, counter 0/5, Fed-HIKE regime. Expiries clean.

**Resolved (6/10):**
- **6/10 May CPI:** NON-TAIL — headline in-line, core soft; energy +3.9% m/m = >60% of the increase (oil→Fed channel, KB-VIO-080). Print = vol relief; concurrent Iran escalation kept the front bid (KB-VIO-081).

**Resolved (6/6):**
- **6/05 R12 knife-edge:** RE-ESTABLISHED 6/05 via 20d-avg 140.16, concurrent with VIX +40% NFP-shock (KB-VIO-067/072).
- **6/15 KB-VIO-031 60d-window checkpoint:** RESOLVED HIT via 6/05 VIX +39.7% (Scenario B at td-58).

---

## WEEKLY MONITORING SCHEDULE

| Day | Task |
|-----|------|
| Sunday | Review week ahead, check VIX expiration proximity |
| Monday | Update VIX data, check term structure, FRED credit refresh |
| Tuesday | Monitor VVIX, SKEW, 20d-avg sensitivity |
| Wednesday | VIX expiration day (if applicable) — watch pinning |
| Thursday | Check credit-vol divergence post-VIX expiry |
| Friday | Week-end summary, update regime status, COT release intake (auto via `cftc_cot.py --boot`) |

---

## DATA REFRESH SCHEDULE

| Data Source | Frequency | Tool | Last Updated |
|-------------|-----------|------|--------------|
| VIX/VIX9D/VIX3M/VVIX/SKEW spot | Every boot (auto in boot.py) | `scripts/thresholds.py` / yfinance | 2026-07-01 (post-close boot, SETTLE basis; SKEW 154.82 verified = official CBOE 7/1 close) |
| FRED credit (HY/IG/CCC + ladder BB/B/BBB + global Euro/EM) | **Every boot** (auto in boot.py `--summary`; FRED print lands ~11:30 AM ET T+1) | `scripts/fred_fetch.py --summary` | 2026-07-01, data through 6/30. Gate: **🔴 BIN-A — CCC 9.70, disp 8.06** (KB-VIO-107; DISH decomposition pending). |
| FRED rates (2Y/10Y/TIPS) | Manual session step | `scripts/fred_fetch.py` | 2026-07-01, through 6/30 (10Y owned by HENRY) |
| 20d SKEW avg + 5td_change | Per boot during knife-edge | inline calc | 2026-07-01: **144.08 / margin +4.08 FRESH** (not mechanical) |
| Catalyst countdown | Every boot (auto in boot.py) | `scripts/catalyst_countdown.py` | 2026-07-01 (next: jobs ~7/2, post-DISH prints 7/2-3, VIX exp 7/15) |
| VIX options OI | Every boot (auto in boot.py; **evening runs print OI=0 — artifact**) | `scripts/vix_options.py` | 2026-07-01 boot ran 21:53 ET → artifact rows; **re-run intraday** (last good OI read 6/23) |
| VX_DAILY.tsv time series | Daily (auto-append at boot; EOD `--supersede` after 16:15 ET) | `scripts/thresholds.py` / `scripts/backfill.py` for gaps | 2026-07-01 SETTLE row; 6/22-6/26 backfilled. **6/29-6/30 absent (yf companion ^-indices lag; re-backfill next session).** |
| CFTC COT VIX futures | Weekly Fri 3:30pm ET (auto in boot.py) | `scripts/cftc_cot.py` | 2026-07-01 boot pulled 6/23 positions (Lev Money −18,863 / 70.5 NORMAL; OI −13.5% w/w). Next: 6/30 positions, release **Mon 7/6** (7/3 = observed holiday; PROME docket) |
| NAAIM + ICI equity positioning | Weekly Wed/Thu | `scripts/equity_positioning.py` (**not yet built**) | Not wired |

**Boot sequence:** `python3 scripts/boot.py` runs thresholds + **fred_fetch --summary (credit gate)** + vix_options + cftc_cot + catalyst_countdown.

---

*Created: 2026-04-12*
*Last Updated: 2026-07-01 (boot after 5-market-day gap: MU/PCE/quarter-end moved to Resolved with outcomes; new forward set — June jobs ~7/2 (🔴, verify timing vs 7/3 holiday), post-DISH CCC prints 7/2-3 (🔴), SK Hynix ADR ~7/10, undated watch lines (KOSPI 8,200 / FSS ETF ruling / SKEW sustain 1/4); Data Refresh re-stamped to 7/1 — Bin-A gate state, VX_DAILY 6/29-30 gap, COT holiday-slip note. Twin: CATALYSTS.tsv same-session. Prior: 6/23 nine-day-dark rebuild.)*
