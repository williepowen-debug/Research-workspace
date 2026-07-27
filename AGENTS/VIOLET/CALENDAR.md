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

**Pattern:** Earnings season = vol supply as single-stock vol gets realized. **Concentration watch:** with record AI/semi concentration (47%) + the leveraged-ETF amplifier complex (US aggregate figure UNVERIFIED — the $464bn number is do-not-propagate per DEWEY 7/20, likely gross-AUM not net rebalance-demand; the demonstrated vehicle-scale case is Korea's ~$9-10bn 2× chip-ETF complex), a single AI-name earnings gap is the most likely Path-B vol trigger this cycle. Semis carry the 2nd-highest constituent-level IV on record into 7/29-8/1 (KB-VIO-126).

---

## ACTIVE FORWARD CATALYSTS

| Date | Event | VIX Implication | VIOLET Checkpoint |
|------|-------|-----------------|-------------------|
| **Jul 29** | **FOMC 2:00 PM ET (no SEP) + Warsh presser 2:30** | Tests 6/17 dot-flip follow-through. **Live hike odds ~34.3% for THIS meeting** (65.7% hold, own pull 7/27, KB-VIO-128) — the board had been pointed at September (82%) instead. Forward guidance **withdrawn** ⇒ wider two-sided distribution with no channel to narrow it. | 🔴 **First gate of the Fed-HIKE regime; 2 td out.** Crack-completing legs on **SETTLE** basis: VIX>20 · inversion VIX3M/VIX <1.0 (KB-VIO-122). Inside buyback blackout. **Final KB-VIO-123 grade due Stale_By 7/30.** |
| **Jul 29** | **SK hynix Q2** | Memory/AI-semi leg of the same stack | 🟠 **Pre-print de-rating already live:** ADRs at a **NEW LOW, below their record $26.5B IPO price** from earlier this month, on a flat-to-up tape (NDX −0.32% vs SPX +0.02%) = **sector-specific de-rate, not beta** [WALTER SIG-027]. VULCAN owns the memory axis; VIOLET consumes for the Path-B vol read. |
| **Jul 29** | **MSFT + META Q2 (AH)** | Same-day as FOMC | 🟠 **VULCAN-09 test.** Reaction function already demonstrated: GOOGL capex raise to $195-205B + TSLA +142%, both negative FCF → Mag-7 −4.8% / ~$787B on 7/23. Semis at 2nd-highest constituent IV on record (KB-VIO-126). |
| **Jul 30** | **AMZN Q2 (AH) + 🆕 AAPL Q3 FY26 (AH, 5:00 PM ET)** | **Apple was missing from the fleet calendar entirely** — flagged by WALTER SIG-013, date verified by own pull 7/27 | 🔴 **Highest-density single night.** AAPL is **Tim Cook's FINAL earnings call as CEO** (→ John Ternus) — a CEO-transition print for the largest index constituent, stacked on AMZN and the BOJ window. Consensus ~$108.9B rev / ~$1.89 EPS. |
| **Jul 30-31** | **BOJ MPM (decision 7/31)** | Carry→vol transmission | 🟠 jpy_vol **IV/RV 3.24×** [7/27] re-loaded against RV10 at **p7.7** — event premium widening on a floor-level realized leg, into carry's strongest year since 2005 (crowded short-FX-vol). **SAM owns the yen call; VIOLET owns the transmission read only.** |
| **Jul 31** | COT release (report-date 7/28) · **KB-VIO-127 Karsan call resolves** | Positioning + scored prediction | 🟡 Did the lev-money unwind continue through FOMC? Karsan HIT = VIX ≥23 touch or >20 settle-and-hold — **base case MISS** (episode high 20.31, rejected). |
| Aug 19 | VIX August expiration | Standard monthly | ⚪ Low. |
| Sep 16 | FOMC + SEP + VIX Sep quarterly expiry | Quarterly dot-plot convergence | 🟠 Next major gate. |

**Resolved (7/2–7/22):** June jobs 7/2 (Gate B NO-FIRE, KB-VIO-111) · post-DISH CCC 7/2 · SK Hynix ADR ~7/10 · June CPI 7/14 · VIX July expiry 7/15 · Japan TIC/MOF/BoK 7/16 · **MOF ITS 7/22 — passed clean (USDJPY 163.82 weakened, no carry unwind; jpy_vol canary CALM).**

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
*Last Updated: 2026-07-27 (post-close settle boot: forward-catalyst set REBUILT — CATALYSTS.tsv carried only 3 forward rows while STATUS treated BOJ + the megacap cluster as live, a twin-divergence the protocol forbids. Added MSFT/META 7/29, **AMZN + AAPL 7/30** (Apple was absent fleet-wide; date verified by own web pull, and it is Cook's final call), BOJ 7/31, COT 7/31, KB-VIO-127 resolution 7/31. FOMC row updated with the live 34.3% July-hike odds per KB-VIO-128. Twin verified via catalyst_countdown.py same session. Prior: 7/23.)*
*Superseded stamp: 2026-07-23 (sit-rep boot: pruned fired July catalysts [7/2–7/16 + MOF 7/22] to Resolved; forward set now FOMC 7/29 (🔴, 4 td) → Aug expiry → Sep FOMC+SEP+quarterly. FOMC row gains the VIOLET crack-leg watch (VIX>20 + inversion <1.0, KB-VIO-122). Twin: CATALYSTS.tsv same-session. Prior: 7/01 five-day-gap boot.)*
