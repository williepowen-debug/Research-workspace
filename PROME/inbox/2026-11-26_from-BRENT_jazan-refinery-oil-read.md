# BRENT -> PROME: Jazan REFINERY hit Thu 11/26: oil read, barrels, grades (SIG-W-20261126-003)

**Written:** 2026-11-26 22:5x EST, BRENT desk, in-process spawn by PROME prome-80. $0. Energy arm RETIRED; WQ-192 STAND DOWN; nothing armed. Full record: `AGENTS/BRENT/research/2026-11-26_jazan-refinery/NOTE.md`. Boot: four instruction files read to `eof` (root CLAUDE.md 4 pages, AGENTS.md 1, USER.md 3, BRENT charter 4); COMPLETION_SPEC 4 pages. `boot.py` rc 2 (5 FINDINGS: threshold monitor HY OAS and two ungraded LNG rows, EIA monitor, D-104 elapsed expiry rows, instruments CUSHING-20M stale / EU-STORAGE / TANKER-LIVENESS, ledger staleness). No pull, no push (your instruction).

## Lead table

| Item | Reading | Basis |
|---|---|---|
| Brent January BZF27 | **96.48** vendor last (bar dated 11/26 = Thursday plus tonight's evening, INFERRED trade date 11/27); secondhand Thursday settle **$96.57, +1.96 (+2.1%)** | vendor (f1 22:37 EST); Startup Fortune citing Reuters (aggregator, not ICE) |
| Brent February BZG27 (= vendor `BZ=F`) | 92.19 (last trade 22:27 ET); 91.37 at 08:08 ET Thu, before the news | fetch.py 22:38 EST; FinanceFeeds via same article. The $92.19 vs $96.48 FALCON flagged is two contract months (M1−M2 +4.29) |
| WTI January CLF27 | 85.68 (last trade 22:29 ET), +1.26 after the last pre-news bar (84.42, Wed 23:58 ET) | fetch.py; capture f1 |
| Diesel HO−CL January | **71.09** (+1.16 after the news; 69.81 at Wed window); gasoline crack flat (+0.11) | vendor; ICE gasoil NOT READ |
| Jazan's share of the move | **not separable; at most about $1.1–1.3 of January's +1.96.** +0.67 came Wed evening before the news; WTI rose the same after the news and Brent−WTI did not widen (10.82 → 10.79): no Saudi-specific premium priced. Kuwait deaths and a Hormuz mine claim landed in the same hours | f1; vendor has NO one-minute bars dated 11/26 |
| Barrels plausibly lost | **Crude: none** (a refinery outage frees crude). **Products: probably little or none now** (plant SHUT since 7/27, no restart ever confirmed; Kpler 10/21 expected it back end-December). If a partial restart had begun (not established), up to about 200 kb/d of mostly diesel/gasoil and naphtha exports, duration unstated. 400 kb/d is capacity, never a loss | INCIDENTS RF-039/RF-044; Kpler; ministry via Arab News |
| BRT-32 (Yanbu halt) | **NOT MET; OPEN** (registered 20% frozen; my unscored view to 12/31 now about 25%) | not Yanbu; no stated loading stop |
| BG-02 | **NOT MET** (no capacity named: C4; no clean FAL-01; no vessel) | ministry "suspension of some operations", unquantified; FALCON production rung NOT FIRED |
| Frame-breaker instances | **none met** | |
| BRT-33 | **not graded** (grades at first read after 11/27; 11/26 = no observation, no bars). Daily-last M1−M3 +7.19 | row text |
| GATE-BRENT-COT-35B | **not due** (11/30) | |
| Energy arm R1 | **not graded** (standing guard) | ACTIVE_DECISIONS row |
| OPEC+ 11/29 (D:L913) | **no change in expectation:** outcome (1) a fourth hold about 75%, deferral about 15%, an increment about 10% (unscored) | Reuters sources via aggregator: hold through Q1 2027 |

## Forward view (unscored)

Two weeks: front bid, curve steep while the Houthi–coalition exchange runs; February BZG27 about $88–96. Alternative (about 35%): premium fades by 12/09 with no barrel lost, February back to $85–87. Tail (about 10%): a stated loading stop at Yanbu, Jeddah or Rabigh. Diesel: modest further firming relative to gasoline if a Jazan restart slips past end-December; about 25% the January diesel crack is back above $80 by 12/18. Change my mind: crude-unit damage with weeks of outage on a plant that had restarted; any Yanbu/Rabigh/Jeddah-terminal hit; Brent−WTI widening more than about $1.

## Unknown

Jazan's pre-hit state (FALCON also UNKNOWN); which units and for how long; the event's clock time; ICE gasoil; whether $96.57 is ICE's settle.

## Rulings encoded (your WQ-754/755 packet; quote of every edited line)

1. **WQ-754 B:** `thesis/PREDICTIONS.tsv` BRT-23 outcome cell, prefix added: *"RULED FAILED ON THE LETTER BY WILL 2026-11-25 23:05 ET (WQ-754 B, verbatim ...); encoded by BRENT 2026-11-26): reading B governs, the two-reading question below is CLOSED. ||"*. Status stays FAILED. BRT-28 untouched.
2. **WQ-755 A, three files made to agree; no level, operator, instrument or consequence changed** (the instance-(4) lapse keeps its NOT MET consequence):
   - `setups/SPECS_GATES.md` § BG-02 "Unchanged by this amendment". Before: *"the window **closing Fri 2026-09-25 17:00 ET** (lapse = NOT MET = premium, not destroyed capacity) · the three gates"*. After: same words, then *"— that window belonged to instance (4), the Petroline strike of 9/10, which LAPSED NOT MET on 2026-09-25 17:0x ET; BG-02 itself did not lapse and remains in force (WQ-755 A, Will 2026-11-25, verbatim "still in force"; record PROME/proposals/2026-11-25_wq754-755-RULED.md) · the three gates"*.
   - `workbook/REGISTRY.tsv` header line 79. Before: *"BG-02 is lapsed; this binds its successor resolver."* After: *"BG-02 is NOT lapsed: only its instance (4) window (Petroline, 9/10) lapsed NOT MET on 2026-09-25; BG-02 remains binding (WQ-755 A, Will 2026-11-25). This base binds the successor resolver (abandoned, WQ-533 (a))."*
   - `TRADE.md` § POSITIONS header (governing; unchanged in meaning). Before: *"BG-02 remains binding."* After: *"BG-02 remains binding (WQ-755 A, Will 2026-11-25, verbatim "still in force"; the 9/25 lapse was instance (4)'s alone)."*
   - ⚠️ One reading point found while grading, for a future event only (both readings give NOT MET tonight; I do not choose): R1's "a named figure ≥0.7 mb/d of throughput" exceeds Jazan's whole 0.4 mb/d capacity, so a refinery of that size can meet R1 only on R1's other branch ("a named capacity figure the operator/state says reduced exports or loadings"), whose floor the text does not state outside the instance-(4) pair rule.

## WQ-735 recipes packet

- `domain/HORMUZ_TRANSIT_BASELINE.md` § 7 line 135 switched `Mozilla/5.0` → `research-bot/1.0`; ran once 22:42 EST: **works** (691 rows; newest Hormuz print 11/22: 1 transit; 11/18–11/22: 3, 3, 4, 4, 1).
- **GIE: HANS's finding holds.** Honest name + the fleet's existing `AGSI_API_KEY` returned data (EU storage 67.2% full, gas day 11/25). `scripts/instrument_check.py` probe_gie now sends the key (x-key header); `--id EU-STORAGE` reads reachable and fresh. **No new key or account needed: the GIE item comes off the 12/07 list.**

## Inbox

`inbox_census.py BRENT` before (22:36 EST): top-level 5 · WALTER/ 4; during the session FALCON's packet and WALTER 006 arrived (6 · 5). After: top-level 0 · WALTER/ 0 (11 consumed, 11 board_log rows, 11 `git mv`). Packets sent: TERRY (tradeability, WQ-696), ORACLE (pin answers: do-not-pin crude all-time-high pair; pin the Russian-diesel 3/31/27 leg as context).

**Commits:** a070f53725 (BRENT desk files), cf31cd324c (TERRY packet), 7403877fda (ORACLE packet), this memo committed separately. Not pushed (your instruction). Closeout: STATUS, SCRATCH, NEXUS_BRIEF, TRACKER stamp, CATALYSTS, RULINGS, CHANGELOG reconciled; orphan, claim and ledger-nudge checks run; consumer check N/A (no figure superseded); calendar --check clean; read-cap rc 0.

## COMPLETION — BRENT — 2026-11-26
STATUS: ✅ DONE
CHANGED: AGENTS/BRENT/ research/2026-11-26_jazan-refinery/*, STATUS.md (+archive/STATUS_dated_2026-11-26_rotation.md), SCRATCH.md, NEXUS_BRIEF.md, TRADE.md, RULINGS.md, thesis/PREDICTIONS.tsv, thesis/CHANGELOG.md, setups/SPECS_GATES.md, workbook/REGISTRY.tsv, docket/CATALYSTS.tsv, refinery_damage/INCIDENTS.tsv (RF-060), demand_destruction/TRACKER.md, domain/HORMUZ_TRANSIT_BASELINE.md, scripts/instrument_check.py, board_log.tsv, 11 inbox moves; packets to TERRY, ORACLE, PROME
RESULT: Jazan refinery hit removes no crude and probably little or no product now (plant shut since 7/27); January Brent BZF27 96.48 vendor (secondhand settle 96.57, +1.96), at most about $1.1–1.3 Jazan-attributable and no Saudi-specific premium (WTI +1.26 in step); diesel crack +1.16 to 71.09. BRT-32 NOT MET (OPEN), BG-02 NOT MET, no frame-breaker instance; BRT-33 and COT not due. WQ-754 B and 755 A encoded (three BG-02 files agree, no level moved); 11 inbox items drained.
GAPS: No one-minute vendor bars for 11/26, so no minute anchor for attribution; ICE gasoil and CME settles unreadable (CME IP block since 10/28); Jazan's pre-hit state UNKNOWN.
WILL_NEEDS: None.
FOLLOW-UP: Mon 11/30 after 15:30 ET: BRT-33 11/27 window and grade, COT #16; Sun 11/29 OPEC+ grade on the statement (D:L913).
