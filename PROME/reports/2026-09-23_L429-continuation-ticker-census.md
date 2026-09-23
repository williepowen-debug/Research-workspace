# L429 census — continuation-ticker (`=F`) exposure, fleet-wide · 2026-09-23

**Commissioned by** PROME `prome-68` (DOCKET L429, due 9/24). **Enumerated by** a read-only Explore sweep (Opus, 2026-09-23 ~11:0x ET). The body below is the sweep's report VERBATIM.

**PROME verification at the artifact before filing (11:0x ET), all VERIFIED:**
- `AGENTS/HANS/scripts/boot.py:120` grades the HANS-T-07 ladder on generic `"TTF=F"`, and `TTFV26` has 0 hits in that script.
- `FORGE/tools/market-data/config.py:72` is pinned to `"BZX26.NYM"`, with a comment saying to re-pin at each roll.
- `AGENTS/BRENT/workbook/REGISTRY.tsv:57` reads "UNSAFE FOR A DELTA and FINE FOR A LEVEL".
- `AGENTS/TERRY/RISK_RULES.md:141` (rule 22) reads "safe for a LEVEL and unsafe for a DELTA".
- `AGENTS/HANS/workbook/VX.tsv:40` (VX-HANS-8.04) carries bands 10/15/20.

**⛔ The class finding:** two desks' written canon (BRENT REGISTRY L57 · TERRY rule 22) states the OPPOSITE of L429 mode (ii): a roll moves a LEVEL too, by the calendar spread. HANS sized one instance at −€1.38 on TTF, crossing no rung by luck of the curve. Every mode-(ii) row below rests on that premise. PROME does not edit either desk's canon; both are packeted.

**Grades nothing.** Each row is its owner's. This census is the population L429 asked for, not a fix.

---

# L429 census: continuation (`=F`) futures tickers, as of 2026-09-23

Nothing was edited. I found **30 dangerous-class rows across 13 desks** (1 fixed, 3 historical), 10 display-only surfaces, and the recorded roll dates.

**Four things to know first:**
- **HANS-T-07 is only half fixed.** The registry row now names `TTFV26.NYM`, but `AGENTS/HANS/scripts/boot.py:121` still grades the L1–L4 ladder on generic `TTF=F`. I found no pin in the script. The ladder has L1 and L2 fired, and TTF rolls on 9/29.
- **Two written rules say the opposite of mode (ii).** BRENT `REGISTRY.tsv:57` says a `=F` ticker is "UNSAFE FOR A DELTA and FINE FOR A LEVEL". TERRY `RISK_RULES.md:141` rule 22 says the same. HANS-T-07's own note says a level ladder does inherit the roll. Every mode-(ii) row below rests on those two rules.
- **FORGE's pinned Brent row is about to go stale.** `config.py:72` pins Brent to `BZX26.NYM` (November). `BZ=F` has already moved to December `BZZ26` (SAM `oil_roll_check.py:5`, 9/18), and `BZX26` expires around 10/01.
- **The NG=F / TTF=F ratio does have bands.** `VX-HANS-8.04` carries 10/15/20 bands. HANS's outbox says "no threshold reads it", which is wrong at the row level.

## A. Dangerous class (mode ii = level threshold, mode iii = derived multi-leg, mode i = change only)

| # | file:line | desk | ticker(s) | mode | pinned? | threshold or derivation | conf |
|---|---|---|---|---|---|---|---|
| 1 | AGENTS/HANS/registry/THRESHOLDS.tsv:8 | HANS | TTF=F | ii | **FIXED (registry)**: names `TTFV26.NYM` | `HANS-T-07 … L1 >60 / L2 >66 / L3 >100 / L4 >200` | VERIFIED |
| 1b | AGENTS/HANS/scripts/boot.py:121 (bands at :100-106) | HANS | TTF=F | ii | **generic** | `("TTF front-month (EUR/MWh)", "TTF=F", _ttf)`; `_ttf` = 200/100/66/60 `[HANS-T-07]` | VERIFIED |
| 2 | AGENTS/HANS/workbook/VX.tsv:40 | HANS | TTF=F ÷ NG=F (plus EURUSD) | iii | the source column names no contract; NGV26 (9/28) and TTFV26 (9/29) roll a day apart | `TTF/Henry Hub RATIO … 9.22 … bands 10/15/20` | VERIFIED |
| 3 | AGENTS/HANS/workbook/VX.tsv:37 | HANS | TTF=F | ii | generic; the note defers to T-07 | `VX-HANS-8.01 … 79.38 bands 60/66/100 ORANGE` | VERIFIED |
| 4 | AGENTS/HANS/workbook/VX.tsv:39 | HANS | NG=F | ii | names NGV26.NYM | `VX-HANS-8.03 Henry Hub 2.90 bands 5/7/10` | VERIFIED |
| 5 | AGENTS/BRENT/workbook/REGISTRY.tsv:93 | BRENT | CL=F | ii | generic, with a roll-caveat note (9/21) | **L427** `MKT-CL-F-ABOVE-100 … above 100` | VERIFIED |
| 6 | …REGISTRY.tsv:94 | BRENT | CL=F | ii | generic, caveat cloned in | `MKT-CL-F-BELOW-70 below 70` | VERIFIED |
| 7 | …REGISTRY.tsv:87-92 | BRENT | BZ=F | ii | generic ("BZ=F continuous") | `MKT-BZ-F-ABOVE-140/120/100, BELOW-85/75/70` | VERIFIED |
| 8 | …REGISTRY.tsv:106-107 | BRENT | NG=F | ii | generic, no caveat | `MKT-NG-F-ABOVE-4 / -5 "Natgas >$4 / >$5"` | VERIFIED |
| 9 | …REGISTRY.tsv:126 | BRENT | CL=F − BZ=F | iii | generic; the note requires matched maturity for a human read | `THESIS-WTI-BRENT … WTI-Brent >$5 = US dislocation` | VERIFIED |
| 10 | …REGISTRY.tsv:132 | BRENT | HO=F vs BZ=F | iii + i (t-4 net change) | generic; note says re-resolve both legs each pull | `DIESEL-CRACK … Net-change / t-4 basis` | VERIFIED |
| 11 | …REGISTRY.tsv:125 | BRENT | BZ=F | ii (instrument only) | generic | `THESIS-BRENT … >$100 fired 7/23; >$120 live watch` | VERIFIED |
| 12 | AGENTS/HAWK/scripts/thresholds.py:31-37, 44 | HAWK | BZ=F | ii | generic | `THRESHOLDS = [(150,"D-EXTREME"),(120,…),(100,…),(80,"C"),(60,"B")]` plus ±10% proximity | VERIFIED |
| 13 | AGENTS/HAWK/scripts/thresholds.py:186 | HAWK | BZ=F − CL=F | iii (printed, no threshold) | generic | `spread = price - wti` | VERIFIED |
| 14 | AGENTS/CARL/scripts/thresholds.py:84-85 | CARL | BZ=F | ii | generic | `("BZ=F","above",120.0,…) ("BZ=F","above",100.0,…)` | VERIFIED |
| 15 | AGENTS/CARL/thesis/PREDICTIONS.tsv:11 | CARL | BZ=F | ii (OPEN) | generic ("BZ=F front-month") | CRL-08 falsifier `Brent drops below $80 sustained 2 weeks`; pass-through levels `$104.85 BZ=F` | VERIFIED |
| 16 | AGENTS/REGINALD/scripts/thresholds.py:29 | REGINALD | BZ=F | ii | generic | `("BZ=F","above",120.0,"Stagflation — oil shock")` | VERIFIED |
| 17 | AGENTS/REGINALD/workbook/VX.tsv:58 | REGINALD | BZ=F | ii | generic | `VX-REG-15.04 Brent … >$100/>$130/>$150 … market.py live (BZ=F)` | VERIFIED |
| 18 | AGENTS/HENRY/workbook/VX.tsv:61 | HENRY | BZ=F | ii (row looks stale, 6/23) | generic | `VX-HEN-20.02 Brent >$100 … $85/$95/$100 … yf BZ=F` | VERIFIED |
| 19 | AGENTS/RED/scripts/boot.py:79 → RED/registry/FALSIFICATION_TRIGGERS.tsv:4-5 | RED | BZ=F | ii (hard triggers WALTER auto-fires on, with sustain counts) | the live evaluator is generic; OUTCOME_SPEC.tsv:5 says "named contract at grade time" | `"BRENT-PAPER": ("yf","BZ=F","price",1)`; FT-03 `>130 ×5`, FT-04 `<75 ×3` | VERIFIED |
| 20 | AGENTS/RED/docket/WATCHLINES.tsv:12 | RED | BZ=F | ii (soft) | generic | `WL-11 BRENT yf BZ=F price < 95` | VERIFIED |
| 21 | AGENTS/RED/scripts/base_rate_review.py:72 | RED | BZ=F | ii (base rates from continuous history) | generic | `"BRENT-PAPER": ("yf","BZ=F",1.0)` | INFERRED |
| 22 | AGENTS/ZHAO/scripts/boot.py:54-62 | ZHAO | BZ=F | ii (context band) | generic | `if v > 100: ("🟠","energy-shock zone >$100")` | VERIFIED |
| 23 | AGENTS/MIDAS/workbook/PREDICTIONS.tsv:2 | MIDAS | GC=F | ii (OPEN, resolves 9/30) | generic | MIDAS-01 `gold (GC=F) close vs $4,113.70 … <$3,702.33` | VERIFIED |
| 24 | AGENTS/MIDAS/workbook/PREDICTIONS.tsv:3 | MIDAS | HG=F | ii (OPEN, resolves 9/30) | generic | MIDAS-02 `copper (HG=F) spot QoQ vs $5.75 … >20%` | VERIFIED |
| 25 | AGENTS/MIDAS/metals_watch.py:343-346 | MIDAS | GC=F ÷ SI=F | iii with bands | generic legs; the identity guard (`FRONT_MONTHS` :104) only prints warnings; MIDAS calls GSR "basis-robust" | `gsr = fut["GC=F"]["price"] / fut["SI=F"]["price"]`; bands 85/90/95 → rc=1 | VERIFIED |
| 26 | AGENTS/MIDAS/metals_watch.py:358-397 | MIDAS | GC=F (90-day history) | i (sign classifier, DIVERGE → rc=1) | generic | `gold_chg_pct = (gold_now - gold_then)/gold_then*100` | VERIFIED |
| 27 | AGENTS/WATT/workbook/VX.tsv:5 + power_watch.py:234 | WATT | NG=F (other leg PJM LMP) | iii (one continuation leg) | generic | P4 `spread compresses 50%/negative sustained 3+ sessions … yfinance NG=F` | VERIFIED |
| 28 | AGENTS/HENRY/workbook/PREDICTIONS.tsv:42 | HENRY | HO=F×42 − CL=F | iii + ii (ACTIVE) | generic series with a roll disclosure; F3 window 9/30–10/14 spans the HO and CL desync | `crack = HO=F*42-CL=F … F1 <$95 stand down, <$90.16 dead` | VERIFIED |
| 29 | AGENTS/TERRY/setups/BRENT_refiner-distillate-strong-leg_2026-08-27.md:315, 381 (+ SETUPS.tsv:6) | TERRY | HO=F×42 − CL=F | iii + ii | the card is generic; SETUPS.tsv:6 now quotes "matched-Nov" (pinned in practice) | `ULSD crack HO=F × 42 − CL=F … F1 <$95` | VERIFIED (card) / INFERRED (practice) |
| 30 | AGENTS/WALTER/design/ROUTING_OVERLAYS.md:67, 69 | WALTER | RB=F − CL=F; Brent 3:2:1 | iii + ii (routing triggers) | **no month named** (L79: "#8's letter is the bare string") | `#6 Gasoline crack re-cross ≥$30 / spike ≥$50`; `#8 Brent 3:2:1 crack > $50/bbl` | VERIFIED |
| 31 | FORGE/tools/market-data/fetch.py:112-113, 1477 | FORGE | BZ=F, CL=F | i (`--delta` emission gate) | generic | `TIER1_PRICES = {"BZ=F":…, "CL=F":…}`; `price_fetch(…, delta_threshold=flags["delta"])` | VERIFIED |
| 32 | FORGE/tools/market-data/config.py:72 | FORGE (HENRY row) | BZX26.NYM | ii | **pinned, but to the expiring month**; front is now BZZ26 | `"id": "BZX26.NYM" … red (100, None)` | VERIFIED |

**Historical or consumed rows (same class, no longer live):**
- MARCO `docket/CATALYSTS.tsv:3`: 8/24 Brent >$85 check, with a "cross-check BZ=F == BZV26" instruction.
- MIDAS `settle_check.py:131`: GC=F is labelled "CROSS-ROLL, bound only"; the grade is MIDAS-06, which is consumed.
- MIDAS `grade_midas07.py:66`: `--gold GC=F close`, grade `B_GOLD 4300`; MIDAS-07 is already graded INDETERMINATE.
- BRENT `thesis/PREDICTIONS.tsv:34`: BRT-21, VOID.

**Brent levels with no instrument named at all (outside the `=F` grep, possible extra population):**
- WALTER `ROUTING_OVERLAYS.md:62-63`: Brent ≥$120 and ≤$75, sustained 3 sessions.
- WALTER `ROUTING_OVERLAYS.md:58`: Brent ≤$95 ×5 and ≥$115 ×5.
- I did not search for other unnamed-instrument rows (SEARCH-NOT-FOUND).

## B. Display only (no threshold or derivation reads the value)

- BRENT `scripts/thresholds.py:127-128, 593-595` (the `NG=F` in the context list is display only; its levels are row A8)
- SAM `scripts/thresholds.py:22, 120` ("automated oil thresholds suspended")
- LIQUID `scripts/boot.py:532` (band is always 🟢 "price ref")
- HENRY `scripts/boot.py:51, 89` and `update_data.py:23` (writes into the MARKET_DATA.tsv ledger)
- HANS `boot.py:125` NG=F `_ctx` (but it feeds row A2)
- VIOLET `scripts/analog_pull.py:87` (GC=F history dataset, mode i latent)
- TERRY `scripts/snapshot.py:98` (BZ=F/CL=F relative to USO, mode i latent)
- SAM `trade_balance_japan.py:245-248` (3-month mean of BZ=F across rolls, derived, no threshold)
- MIDAS `metals_watch.py:81` FUTURES spot print
- PROME `tools/fleet_dashboard.py:416` (Brent tile reads the FORGE config row A32)

SAM `oil_roll_check.py` and MIDAS `check_contract_identity()` are roll guards, not exposures.

## C. Recorded roll and expiry dates

| generic | current / next contract | recorded date | source |
|---|---|---|---|
| NG=F | NGV26.NYM | expires **2026-09-28** | HANS outbox 2026-09-18_local-enumeration.md:8, KB-HANS-082 |
| TTF=F | TTFV26.NYM → TTFX26 | expires **2026-09-29** | HANS THRESHOLDS.tsv:8, STATUS.md:101 |
| BZ=F | already rolled to BZZ26 (~9/18); BZX26 expire 2026-10-01 | 10/01 is the vendor expiry of the dying pin | SAM oil_roll_check.py:5; WALTER THRESHOLD_SCAN.md:54 |
| CL=F | rolled to CLX26 on 9/18–9/21 (CLV26 expired 9/22) | CLX26 expires **2026-10-20** | BRENT SCRATCH.md:4; HENRY PREDICTIONS.tsv:42 |
| HO=F / RB=F | HOX26 / RBX26 | expire **2026-10-30**; HO likely rolls ~10/14 | HENRY PREDICTIONS.tsv:42 |
| next months | BZF27 2026-12-01 · CLZ26 2026-11-20 · HOZ26 2026-11-30 | as recorded | WALTER THRESHOLD_SCAN.md:56 area |
| GC/SI/HG/PL/PA=F | GCZ26 / SIZ26 / HGZ26 / PLV26 / PAZ26 | front months hand-maintained; expiry dates SEARCH-NOT-FOUND | MIDAS metals_watch.py:104-105 |

## Absence claims (all SEARCH-NOT-FOUND)

- No `=F` in PROME/GATES.tsv, FORGE `dashboard.py`, or PROME `fleet_dashboard.py`.
- No Brent/oil rows in REGINALD, CREED, or LIQUID threshold registries.
- No live `=F` threshold for ZC, ZW, ES, NQ, JKM or 6J outside KB, inbox and log files.
- No `TTFV26` in HANS `boot.py`.

## Search commands (run from /home/willi/Research-workspace)

```
grep -rnoE --exclude-dir={archive,_archive,.git,__pycache__} '\b[A-Z0-9]{1,4}=F\b' AGENTS PROME/GATES.tsv FORGE/tools/market-data PROME/tools/fleet_dashboard.py | cut -d: -f1 | sort | uniq -c
grep -rhoE --exclude-dir={archive,_archive,.git} '\b[A-Z0-9]{1,4}=F\b' AGENTS FORGE/tools/market-data PROME/GATES.tsv PROME/tools/fleet_dashboard.py | sort | uniq -c
find AGENTS -path '*/archive' -prune -o -path '*/_archive' -prune -o -name '*.py' -print | grep -v /research/ | xargs grep -nE '\b[A-Z0-9]{1,4}=F\b'
grep -nE '\b[A-Z0-9]{1,4}=F\b' FORGE/tools/market-data/{config,dashboard,fetch}.py PROME/tools/fleet_dashboard.py PROME/GATES.tsv
grep -rnE --include='*.py' "['\"]=F['\"]|\{[a-z_]+\}=F" AGENTS FORGE/tools/market-data PROME/tools
find AGENTS … \( -name '*.tsv' -o -name '*.json' \) | grep -vE 'KB\.tsv|board_log|…' | xargs grep -lE '\b[A-Z]{1,3}=F\b'
find AGENTS … \( -name STATUS.md -o -name THESIS.md -o -name TRADE.md -o -name CLAUDE.md -o -name NEXUS_BRIEF.md -o -name SCRATCH.md \) | xargs grep -nE '\b[A-Z0-9]{1,4}=F\b'
find AGENTS … \( -iname '*THRESHOLD*' -o -iname '*GATES*' -o -iname 'CATALYSTS*' -o -iname 'WATCHLINES*' -o -iname 'TRIGGERS*' \)
grep -niE 'brent|wti|ttf|crack|gold|NYM|=F' PROME/GATES.tsv PROME/tools/fleet_dashboard.py
```

**Scope exclusions:** I left out `inbox/`, `outbox/`, `research/*/before/`, SESSION_LOG files, STATUS archives, and KB.tsv / board_log files. They mention these tickers as history or knowledge, not as live thresholds, and I did not check them row by row.