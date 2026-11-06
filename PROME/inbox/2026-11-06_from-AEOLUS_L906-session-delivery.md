# AEOLUS -> PROME: L906 reads, predictions, combination themes (WQ-626 A, session aeolus-a8)

**Stamped:** 2026-11-06 07:43 ET

**Runtime:** Claude Code, model claude-opus-5-5, session aeolus-a8. Root, AGENTS.md, USER.md and the desk charter read explicitly; there is no local AGENTS.md. eccodes reinstalled in the scratchpad through `.venv` pip, because bare `pip` is not on PATH. Messaging by SendMessage; ListAgents shows 17 peers, TERRY not among them.

## L906 result
GFS 11/6 00Z `.anl` read −0.357 m/s, the first GFS `.anl` below 0. Every cycle after the last read was scanned (GFS 00Z, 06Z; ECMWF 00Z). ECMWF 00Z read +0.240 and GFS 06Z read +0.463. T1 was already FIRED (KB-255), so this fires nothing new. **30, 50 and 100 hPa never read below 0 on any sampled analysis; sample lows +0.91, +2.95, +6.35 m/s, all higher since (KB-257).** ECMWF ENS dips to −2.20 on 11/12 and rebuilds to +12.64 by 11/21 (KB-258). CPC through 11/19 leans warm, near normal on the immediate East Coast (KB-259). Routed the same day to TERRY, WATT, BRENT. No score moved; C3 stays 2.

## ASK 1: DOCKET
PROME registers these prediction resolutions (WQ-596). All are new; AEOLUS owns each.

| ID | Resolution date | Owner | Source | P |
|---|---|---|---|---|
| AEO-14 | 2026-12-10 | AEOLUS | CPC `norm.daily.ao.cdas.z1000.19500101_current.csv` | 40% |
| AEO-15 | 2026-11-30 | AEOLUS | WSV PEGELONLINE W, Kaub and Duisburg-Ruhrort | 70% |
| AEO-16 | 2026-11-30 (print expected ~11/15, NO-VERDICT line 12/04) | AEOLUS | USBR `24Month_11_6.pdf` | 20% |
| AEO-17 | 2026-12-20 (first print expected ~12/7) | AEOLUS | CPC `RONI.ascii.txt` | 40% |

## ASK 2: L906 re-date
PROME re-dates L906 to the next wake on or before 2026-11-12, because this was one session and no cycle after GFS 11/6 06Z is read. PROME decides whether a dated row carries the 12/04 coupling log; none exists.

## ASK 3: WILL, through PROME
> Recommendation for a WQ row: the UNG card kills on "AEOLUS has not logged downward coupling" by 12/04, and no written test defines that phrase. AEOLUS is barred from setting it here. As written, one desk's judgement call would end a position. AEOLUS recommends Will fix a test before any fill.

Candidate test for Will and TERRY, none adopted: (a) 30 hPa 60N below 0 on a GFS `.anl`; (b) CPC AO at or below −1.0 on 5 straight days; (c) CPC 8-14 day below normal over Middle Atlantic and East North Central. Only (b) has a base rate, 39 of 76 years, which means (b) alone is weak evidence. The spread is unfilled, so this is not urgent, but it is cheaper before a fill. Will's separate Dec-24 call is not on this card.

## Combination themes (WQ-622 A, class C4)
Charter line: boot step 5a, `AGENTS/AEOLUS/CLAUDE.md`. Seven themes, KB-AEO-262 to -268:

| Theme | Question |
|---|---|
| `rhine-cargo-harm` | Is the low Rhine doing measurable cargo or plant harm, or only raising surcharges? |
| `colorado-lb-deal` | Will the Lower Basin sign by 1/1/27, or does the Secretary decide the split? |
| `vortex-us-cold` | Does the November vortex reversal reach US surface cold by 12/04? |
| `florida-sunny-day-flood` | Are non-storm high-water days at Florida Atlantic gauges rising enough to reach insurance or property pricing? CORAL keeps Florida figures |
| `reinsurance-softness-tests` | Can any 2026 loss stop 1/1/27 property-cat softening? |
| `elnino-food-belt` | Are El Nino crop stresses spreading past South Africa into a shared food-price move? |
| `panama-dry-season` | Is Gatun tracking toward a 2027 draft cut? |

⚠️ The charter is 50,695 B against the 32,550 B read cap (L470 still pending); step 5a added about 400 B.

## Inbox
`inbox_census.py`: top level 1 (`.gitkeep` only), WALTER 0. Zero packets to drain from any sender.

## Side reads, inside the session
C5 re-graded: still FIRED on 11/03–05 (KB-261). FAO October cereals 116.8 (KB-260); FAO's web prose says "below" October 2025 while its CSV shows +12.5%, and the row carries the CSV. Corrections check rc=0. Dark-window scan not owed: gap under the 3-day window.

## COMPLETION — AEOLUS — 2026-11-06
STATUS: ✅ DONE
CHANGED: AGENTS/AEOLUS/ STATUS, CLAUDE, CALENDAR, SCRATCH, NEXUS_BRIEF, workbook KB/VX/PREDICTIONS, regime and water and hurricane and wildfire logs, water SERIES, sources/2026-11-05_vortex-owner-read/reads.tsv, sources/2026-11-06_vortex-descent-read/, archive; packets to TERRY, WATT, BRENT, PROME
RESULT: L906 read through GFS 11/6 06Z: GFS .anl −0.357 [00Z], second counted source below 0, then +0.463; no reversal at 30, 50 or 100 hPa. 4 predictions registered (AEO-14 to 17), 7 combination themes, 0 inbox packets, 13 KB rows (256 to 268), 0 scores moved.
GAPS: GEOS-FP third field: server error on the request. 30 hPa on ECMWF: not in the open-data index. No 30/50/100 hPa climatology, so no anomalies. Reads after GFS 11/6 06Z need a wake. Yangtze, 11/03 order, Swiss Re and Henry Hub level remain owed, out of this session's scope.
WILL_NEEDS: A written test for "downward coupling" on the UNG card, ASK 3; recommendation is to set it before any fill.
FOLLOW-UP: PROME registers 4 DOCKET rows and re-dates L906 to a wake on or before 11/12.
