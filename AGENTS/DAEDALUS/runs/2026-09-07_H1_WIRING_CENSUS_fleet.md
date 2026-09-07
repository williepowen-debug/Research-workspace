# H1 — GUARD-WIRING CENSUS, fleet run · 2026-09-07 ~20:1x ET · DAEDALUS (harvest batch, Will-ruled)

**Tool:** `scripts/wiring_census.py --all` (built tonight). **Positive control:** LABOR's pre-fix `labor_data.py` + STATUS of `f2558c075^` → flags `SERIES-IN-STATUS-NOT-FETCHED EMRATIO` (the exact 31-day defect), `TEMPHELPS` fetched-but-undeclared, and the `1,900,000` CCSA constant (LABOR's own BD-28(b) orphan) — all three real. **Clean-side state: NOT clean.** The reverse leg (STATUS names a gauge no script fetches) keys on ALIAS words ("claims", "Brent", "VIX", "curve") on any line that looks trigger-shaped, and across 28 desks that fires on prose, on other desks' figures quoted in STATUS, and on the desk's own narrative. **Disposition: NO per-desk packets from this run** — sending a red-on-everything list is the permanent-red instrument CHECK_STANDARD §3(e) was written tonight to forbid. The forward legs (fetched-series-not-declared; compared-constant-not-in-STATUS) are usable as candidates; the reverse leg needs its scope cut to THRESHOLD TABLE ROWS (a `| … | >`/`≥` cell or a `T-\d` token on the same line) before it names a desk. **Home: `validate_all` v1 (9/10) — this file is its input.**

| Desk | flags (all legs, unfiltered) |
|---|---|
| AEOLUS | 7 |
| BROCK | 21 |
| CORAL | 3 |
| CREED | 1 |
| DAEDALUS | 4 |
| DEWEY | 4 |
| FLG | 20 |
| HAWK | 5 |
| HENRY | 4 |
| LABOR | 8 |
| LIQUID | 21 |
| MARCO | 4 |
| ORACLE | 5 |
| OTTO | 8 |
| OZK | 3 |
| RED | 10 |
| REGINALD | 11 |
| SAM | 17 |
| TERRY | 9 |
| VIOLET | 8 |
| VULCAN | 5 |
| WAL | 3 |
| YEYOU | 0 |
| ZHAO | 10 |

**CANNOT-VERIFY (no threshold/fetch script found under `scripts/` or `tools/`):** AEOLUS, BROCK, DEWEY, FLG, WAL — a census fact, not a defect: these desks may have no scripted sweep, or their sweep lives elsewhere.

**Forward-leg candidates worth an owner's eye (fetched series with no mention in the desk's threshold section):** CARL ×13 (housing/retail FRED IDs in a script vs a STATUS whose threshold section does not name them — probably a data script, not a guard) · LIQUID ×9 (repo/OAS series) · RED T5YIFR/BAMLH0A3HYC · TERRY VIXW/HY OAS · BRENT WGFUPUS2 · HANS IPMAN · VULCAN TICK. Owner reads, no packet tonight.

## Raw output
```
[AEOLUS] CANNOT-VERIFY: no threshold/fetch script found under scripts/ or tools/
[BRENT] scripts: AGENTS/BRENT/scripts/cot_grade.py, AGENTS/BRENT/scripts/eia_weekly.py, AGENTS/BRENT/scripts/instrument_check.py, AGENTS/BRENT/scripts/refiner_ratios.py, AGENTS/BRENT/scripts/thresholds.py · STATUS scope: WHOLE STATUS (no threshold-named section found) (71,972 B)
   AGENTS/BRENT/scripts/cot_grade.py: SERIES (none literal)
   AGENTS/BRENT/scripts/eia_weekly.py: SERIES ['WGFUPUS2']
      SERIES-NOT-IN-STATUS  WGFUPUS2  (aliases tried: ['WGFUPUS2'])
      CONST         92.0  line  269  in STATUS  :: if val > 92.0:
      CONST           56  line  338  in STATUS  :: if len(gv) >= 56:
      CONST            7  line  376  in STATUS  :: age_icon = "🟢" if age_days <= 3 else "🟠" if age_days <= 7 else "🔴"
   AGENTS/BRENT/scripts/instrument_check.py: SERIES (none literal)
      CONST          200  line  284  in STATUS  :: if resp.status != 200:
      CONST           64  line  287  in STATUS  :: if len(body) < 64:
      CONST           30  line  702  in STATUS  :: elif mins < 30:
      CONST           60  line  713  in STATUS  :: INCIDENT_ACTIVE_BUDGET_D = 60   # ACTIVE >=60d unverified => re-verify-or-downgr
      CONST           90  line  828  in STATUS  :: last_verified age 124 days, max 146; 18 unverified >=90d, and those 18 carry
      CONST            8  line  952  in STATUS  :: if len(inc) > 8:
      CONST            6  line  973  in STATUS  :: if len(unb) > 6:
   AGENTS/BRENT/scripts/refiner_ratios.py: SERIES (none literal)
      CONST           20  line  103  in STATUS  :: if len(pairs) < 20:
      CONST          1.0  line  127  in STATUS  :: if z <= -Z_WARN and chg_1d >= 1.0:
   AGENTS/BRENT/scripts/thresholds.py: SERIES ['STNG']
      CONST         1000  line  364  NOT IN STATUS ⚠️  :: if abs(value) > 1000:
      CONST           10  line  366  in STATUS  :: if abs(value) > 10:
      SERIES-IN-STATUS-NOT-FETCHED  ICSA  ('claims' on 2 trigger-shaped STATUS line(s); first: | **🟠 IRGC COUNTER-CLAIM 9/6 — CARRIED AS A CLAIM, ADJUDICATED AS NOTHING** | IRGC Navy cl)
      SERIES-IN-STATUS-NOT-FETCHED  VIXCLS  ('VIX' on 1 trigger-shaped STATUS line(s); first: | **📈 LIVE TAPE 2026-08-28 ~10:5x ET — LIVE BARS, CONTRACT NAMED, NOT SETTLES.** | **`BZV2)
      SERIES-IN-STATUS-NOT-FETCHED  T10Y2Y  ('curve' on 4 trigger-shaped STATUS line(s); first: | **📐 CURVE — `M1−M3` STILL BACKWARDATED, NOT NARROWING INTO THE RALLY** | **`+$7.07`** (N)
      SERIES-IN-STATUS-NOT-FETCHED  DCOILBRENTEU  ('Brent' on 8 trigger-shaped STATUS line(s); first: | **⚠️ THE ONE THING THAT WOULD CHANGE IT, AND IT IS NOT MINE** | **My own pre-stated clas)
      SERIES-IN-STATUS-NOT-FETCHED  DCOILWTICO  ('WTI' on 1 trigger-shaped STATUS line(s); first: | **📈 LIVE TAPE 2026-08-28 ~10:5x ET — LIVE BARS, CONTRACT NAMED, NOT SETTLES.** | **`BZV2)
   flags: 7  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[BROCK] CANNOT-VERIFY: no threshold/fetch script found under scripts/ or tools/
[CARL] scripts: AGENTS/CARL/scripts/abs_monitor.py, AGENTS/CARL/scripts/boot.py, AGENTS/CARL/scripts/consumer_pulse.py, AGENTS/CARL/scripts/gas_tracker.py, AGENTS/CARL/scripts/housing_pulse.py, AGENTS/CARL/scripts/thresholds.py · STATUS scope: threshold section(s) (840 B)
   AGENTS/CARL/scripts/abs_monitor.py: SERIES (none literal)
      CONST            5  line  167  in STATUS  :: if len(parts) >= 5:
   AGENTS/CARL/scripts/boot.py: SERIES ['THRESHOLDS']
      SERIES-NOT-IN-STATUS  THRESHOLDS  (aliases tried: ['THRESHOLDS'])
   AGENTS/CARL/scripts/consumer_pulse.py: SERIES ['CCSA', 'DSPIC96', 'ICSA', 'RSXFS', 'TOTALNS']
      SERIES-NOT-IN-STATUS  CCSA  (aliases tried: ['CCSA', 'continuing claims', 'CC '])
      SERIES-NOT-IN-STATUS  DSPIC96  (aliases tried: ['DSPIC96'])
      SERIES-NOT-IN-STATUS  RSXFS  (aliases tried: ['RSXFS'])
      SERIES-NOT-IN-STATUS  TOTALNS  (aliases tried: ['TOTALNS'])
      CONST           45  line  120  NOT IN STATUS ⚠️  :: if best and best_diff < 45:  # within ~6 weeks
      CONST            9  line  266  in STATUS  :: if len(row) >= 9:
   AGENTS/CARL/scripts/gas_tracker.py: SERIES ['GASREGW']
      SERIES-NOT-IN-STATUS  GASREGW  (aliases tried: ['GASREGW'])
      CONST            4  line  108  in STATUS  :: "diesel": cells[4] if len(cells) > 4 else None,
      CONST         3.50  line  159  NOT IN STATUS ⚠️  :: if price >= 3.50:
   AGENTS/CARL/scripts/housing_pulse.py: SERIES ['CSUSHPINSA', 'EXHOSLUSM495S', 'HOUST', 'HSN1F', 'MSACSR', 'MSPUS', 'PERMIT']
      SERIES-NOT-IN-STATUS  CSUSHPINSA  (aliases tried: ['CSUSHPINSA'])
      SERIES-NOT-IN-STATUS  EXHOSLUSM495S  (aliases tried: ['EXHOSLUSM495S'])
      SERIES-NOT-IN-STATUS  HOUST  (aliases tried: ['HOUST'])
      SERIES-NOT-IN-STATUS  HSN1F  (aliases tried: ['HSN1F'])
      SERIES-NOT-IN-STATUS  MSACSR  (aliases tried: ['MSACSR'])
      SERIES-NOT-IN-STATUS  MSPUS  (aliases tried: ['MSPUS'])
      SERIES-NOT-IN-STATUS  PERMIT  (aliases tried: ['PERMIT'])
      CONST         0.80  line  216  NOT IN STATUS ⚠️  :: mf_status = "RED" if mf_rate >= 0.80 else "ORANGE" if mf_rate >= 0.70 else "YELL
      CONST         0.70  line  216  NOT IN STATUS ⚠️  :: mf_status = "RED" if mf_rate >= 0.80 else "ORANGE" if mf_rate >= 0.70 else "YELL
   AGENTS/CARL/scripts/thresholds.py: SERIES ['CCSA', 'DCOILBRENTEU', 'ICSA']
      SERIES-NOT-IN-STATUS  CCSA  (aliases tried: ['CCSA', 'continuing claims', 'CC '])
      SERIES-NOT-IN-STATUS  DCOILBRENTEU  (aliases tried: ['DCOILBRENTEU', 'Brent'])
      CONST         1000  line  288  NOT IN STATUS ⚠️  :: if abs(value) > 1000:
      CONST           10  line  290  NOT IN STATUS ⚠️  :: if abs(value) > 10:
   flags: 21  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[CORAL] scripts: AGENTS/CORAL/scripts/boot.py · STATUS scope: WHOLE STATUS (no threshold-named section found) (26,686 B)
   AGENTS/CORAL/scripts/boot.py: SERIES ['FORGE', 'SBCF', 'USCB']
      SERIES-NOT-IN-STATUS  FORGE  (aliases tried: ['FORGE'])
      SERIES-NOT-IN-STATUS  USCB  (aliases tried: ['USCB'])
      CONST           48  line  111  NOT IN STATUS ⚠️  :: if age_h < 48:
   flags: 3  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[CREED] scripts: AGENTS/CREED/scripts/boot.py, AGENTS/CREED/scripts/s8a_relative.py · STATUS scope: threshold section(s) (1,504 B)
   AGENTS/CREED/scripts/boot.py: SERIES (none literal)
   AGENTS/CREED/scripts/s8a_relative.py: SERIES (none literal)
      CONST          -10  line    4  NOT IN STATUS ⚠️  :: Feeds `VX-CREED-7.01`, `CREED-T-08a` (< -10pp, Will-frozen 2026-07-21) and `PRED
   flags: 1  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[DAEDALUS] scripts: AGENTS/DAEDALUS/scripts/scorecard.py · STATUS scope: WHOLE STATUS (no threshold-named section found) (23,681 B)
   AGENTS/DAEDALUS/scripts/scorecard.py: SERIES (none literal)
      CONST            4  line  136  in STATUS  :: if len(f) < 4:
      SERIES-IN-STATUS-NOT-FETCHED  UNRATE  ('U-3' on 1 trigger-shaped STATUS line(s); first: **Last Updated:** 2026-09-07 (Mon, holiday, ~12:3x ET — **Will-directed LABOR PARITY ASSES)
      SERIES-IN-STATUS-NOT-FETCHED  ICSA  ('claims' on 3 trigger-shaped STATUS line(s); first: **Last Updated:** 2026-09-07 (Mon, holiday, ~12:3x ET — **Will-directed LABOR PARITY ASSES)
      SERIES-IN-STATUS-NOT-FETCHED  PAYEMS  ('payroll' on 1 trigger-shaped STATUS line(s); first: **Last Updated:** 2026-09-07 (Mon, holiday, ~12:3x ET — **Will-directed LABOR PARITY ASSES)
      SERIES-IN-STATUS-NOT-FETCHED  DCOILBRENTEU  ('Brent' on 3 trigger-shaped STATUS line(s); first: **Last Updated:** 2026-09-07 (Mon, holiday, ~12:3x ET — **Will-directed LABOR PARITY ASSES)
   flags: 4  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[DEWEY] CANNOT-VERIFY: no STATUS.md
[FALCON] scripts: AGENTS/FALCON/scripts/baghdad_watch.py, AGENTS/FALCON/scripts/bypass_watch.py, AGENTS/FALCON/scripts/hormuz_transit_watch.py · STATUS scope: WHOLE STATUS (no threshold-named section found) (45,038 B)
   AGENTS/FALCON/scripts/baghdad_watch.py: SERIES (none literal)
   AGENTS/FALCON/scripts/bypass_watch.py: SERIES (none literal)
   AGENTS/FALCON/scripts/hormuz_transit_watch.py: SERIES (none literal)
      SERIES-IN-STATUS-NOT-FETCHED  ICSA  ('claims' on 1 trigger-shaped STATUS line(s); first: > 6. **📬 INBOX 5/5.** WALTER `SIG-W-20260906-001` (Sirik, US investigation, expert read of)
      SERIES-IN-STATUS-NOT-FETCHED  VIXCLS  ('VIX' on 2 trigger-shaped STATUS line(s); first: | Global macro / credit | **3** | No credit stress beneath the repricing. **I carry NO cre)
      SERIES-IN-STATUS-NOT-FETCHED  DCOILBRENTEU  ('Brent' on 11 trigger-shaped STATUS line(s); first: **Last Updated:** 2026-09-07 Mon ~13:0x ET (PROME-spawned FALCON session `falcon-0907`, Ti)
      SERIES-IN-STATUS-NOT-FETCHED  DCOILWTICO  ('WTI' on 1 trigger-shaped STATUS line(s); first: | Oil price / energy tape | **5** | **Brent $90.21 (−0.58%), WTI $84.45** [own pull 7/30].)
   flags: 4  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[FLG] CANNOT-VERIFY: no threshold/fetch script found under scripts/ or tools/
[HANS] scripts: AGENTS/HANS/scripts/boot.py, AGENTS/HANS/scripts/fetch_eu.py, AGENTS/HANS/scripts/finding_check.py, AGENTS/HANS/scripts/pmi_ism_lead_test.py · STATUS scope: threshold section(s) (1,993 B)
   AGENTS/HANS/scripts/boot.py: SERIES (none literal)
      CONST          200  line   58  NOT IN STATUS ⚠️  :: if v > 200: return "🔴", "L4 CRISIS >200  [HANS-T-07]"
      CONST          100  line   59  NOT IN STATUS ⚠️  :: if v > 100: return "🔴", "L3 RED >100  [HANS-T-07]"
      CONST           66  line   60  NOT IN STATUS ⚠️  :: if v >= 66: return "🟠", "L2 ORANGE >=66  [HANS-T-07]"
      CONST           60  line   61  NOT IN STATUS ⚠️  :: if v >= 60: return "🟡", "L1 WATCH >=60  [HANS-T-07]"   # id was MISSING: only L2
      CONST         1.00  line   65  in STATUS  :: if v < 1.00: return "🔴", "CRISIS <1.00  [HANS-T-11]"     # id was missing on the
      CONST         1.05  line   66  NOT IN STATUS ⚠️  :: if v < 1.05: return "🟠", "WATCH <1.05  [HANS-T-11]"
      CONST          105  line   70  NOT IN STATUS ⚠️  :: return ("🟡", "dollar-strength zone >105") if v > 105 else ("🟢", "normal")
      CONST            7  line  192  in STATUS  :: em = "🔴" if a is None or a > KEY_STALE_DAYS else ("🟡" if a > 7 else "🟢")
      CONST          -14  line  204  in STATUS  :: elif a > -14: em, note = "🟠", f"due in {-a}d"
   AGENTS/HANS/scripts/fetch_eu.py: SERIES (none literal)
      CONST         4.50  line   98  in STATUS  :: em = "🔴" if v > 4.50 else "🟠" if v > 3.75 else "🟡" if v > 3.00 else "🟢"
      CONST         3.75  line   98  NOT IN STATUS ⚠️  :: em = "🔴" if v > 4.50 else "🟠" if v > 3.75 else "🟡" if v > 3.00 else "🟢"
      CONST         3.00  line   98  in STATUS  :: em = "🔴" if v > 4.50 else "🟠" if v > 3.75 else "🟡" if v > 3.00 else "🟢"
      CONST          200  line  127  NOT IN STATUS ⚠️  :: if sp > 200 and cv > 5.50: breached.append("HANS-T-09")
      CONST         5.50  line  127  NOT IN STATUS ⚠️  :: if sp > 200 and cv > 5.50: breached.append("HANS-T-09")
      CONST          100  line  130  NOT IN STATUS ⚠️  :: if sp > 100 and cv > 4.50: breached.append("HANS-T-10")
      CONST          -25  line  143  NOT IN STATUS ⚠️  :: em = "🔴" if gap < -25 else "🟠" if gap < -15 else "🟢"
      CONST          -15  line  143  NOT IN STATUS ⚠️  :: em = "🔴" if gap < -25 else "🟠" if gap < -15 else "🟢"
   AGENTS/HANS/scripts/finding_check.py: SERIES ['IPMAN']
      SERIES-NOT-IN-STATUS  IPMAN  (aliases tried: ['IPMAN'])
      CONST            8  line  104  in STATUS  :: if len(ys) >= 8:
      CONST           60  line  176  NOT IN STATUS ⚠️  :: if len(sub) < 60: return None
   AGENTS/HANS/scripts/pmi_ism_lead_test.py: SERIES ['IPMAN']
      SERIES-NOT-IN-STATUS  IPMAN  (aliases tried: ['IPMAN'])
      CONST           24  line   72  NOT IN STATUS ⚠️  :: if len(ks) < 24:
      CONST            6  line  156  in STATUS  :: if 0 in d and max(d) >= 6:
      CONST         0.15  line  166  NOT IN STATUS ⚠️  :: if avg > 0.15:
      CONST        -0.15  line  171  NOT IN STATUS ⚠️  :: elif avg < -0.15:
      CONST           60  line  183  NOT IN STATUS ⚠️  :: if len(sub) < 60: return None
      SERIES-IN-STATUS-NOT-FETCHED  DGS30  ('30Y' on 2 trigger-shaped STATUS line(s); first: 📌 **Now REGISTERED, not prose: `registry/THRESHOLDS.tsv` (HANS-T, **14 rows**) + `registry)
   flags: 20  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[HAWK] scripts: AGENTS/HAWK/scripts/boot.py, AGENTS/HAWK/scripts/thresholds.py, AGENTS/HAWK/scripts/war_monitor.py · STATUS scope: threshold section(s) (2,218 B)
   AGENTS/HAWK/scripts/boot.py: SERIES (none literal)
      CONST           10  line  182  NOT IN STATUS ⚠️  :: if len(all_alerts) > 10:
   AGENTS/HAWK/scripts/thresholds.py: SERIES (none literal)
      CONST           10  line   85  NOT IN STATUS ⚠️  :: if dist_pct <= 10:
      CONST          100  line  233  NOT IN STATUS ⚠️  :: if scenario.startswith("D") and price >= 100:
      CONST          120  line  235  NOT IN STATUS ⚠️  :: elif scenario.startswith("D") and price >= 120:
      CONST           60  line  237  NOT IN STATUS ⚠️  :: elif price < 60:
   AGENTS/HAWK/scripts/war_monitor.py: SERIES (none literal)
   flags: 5  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[HENRY] scripts: AGENTS/HENRY/scripts/boot.py, AGENTS/HENRY/scripts/credit_monitor.py, AGENTS/HENRY/scripts/gamma_flip.py, AGENTS/HENRY/scripts/status_figure_manifest.py · STATUS scope: threshold section(s) (4,861 B)
   AGENTS/HENRY/scripts/boot.py: SERIES ['FORGE']
      SERIES-NOT-IN-STATUS  FORGE  (aliases tried: ['FORGE'])
      CONST           16  line   94  in STATUS  :: if 16 * 60 <= hm < 16 * 60 + 15:
      CONST           14  line   97  in STATUS  :: if hm >= 14 * 60 + 30:
      CONST         0.25  line  223  NOT IN STATUS ⚠️  :: if n < 0.25 * HEALTHY_CONTRACTS:
      CONST            4  line  291  in STATUS  :: if len(c) >= 4:
      CONST           10  line  510  in STATUS  :: mark = "🔴" if len(unlogged) >= 10 or oldest >= 10 else "🟠" if unlogged else "✓"
      CONST            8  line  515  in STATUS  :: if len(unlogged) > 8:
   AGENTS/HENRY/scripts/credit_monitor.py: SERIES (none literal)
      CONST            5  line  158  in STATUS  :: d5 = round((last / float(closes.iloc[-6]) - 1) * 100, 2) if len(closes) > 5 else
   AGENTS/HENRY/scripts/gamma_flip.py: SERIES (none literal)
      CONST          2.5  line  102  in STATUS  :: if oi <= 0 or not (0.03 < iv < 2.5):
      CONST           10  line  202  in STATUS  :: NEAR_TIE = 0.10  # <10% between #1 and #2 = a coin flip, not a wall
   AGENTS/HENRY/scripts/status_figure_manifest.py: SERIES (none literal)
      SERIES-IN-STATUS-NOT-FETCHED  DGS2  ('2Y' on 1 trigger-shaped STATUS line(s); first: | **2Y** | **4.39% [DGS2 9/1]** | >4.25 | **>4.40** | >4.60 | 🟡 **Through yellow, 1bp unde)
      SERIES-IN-STATUS-NOT-FETCHED  VIXCLS  ('VIX' on 1 trigger-shaped STATUS line(s); first: | VIX | **14.16 [9/4 pre-open]** | >23 | >28 | >30 sust | NOT FIRED — **~8.8 under** the v)
   flags: 4  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[LABOR] scripts: AGENTS/LABOR/scripts/alfred_vintages.py, AGENTS/LABOR/scripts/boot.py, AGENTS/LABOR/scripts/labor_data.py, AGENTS/LABOR/scripts/spine_check.py, AGENTS/LABOR/scripts/warn_texas.py, AGENTS/LABOR/tools/form4_scanner.py, AGENTS/LABOR/tools/job_postings_tracker.py · STATUS scope: threshold section(s) (10,835 B)
   AGENTS/LABOR/scripts/alfred_vintages.py: SERIES (none literal)
      CONST           12  line  197  in STATUS  :: eom = date(y + (m == 12), 1 if m == 12 else m + 1, 1)
      CONST           45  line  199  NOT IN STATUS ⚠️  :: return "LATE-FIRST-RELEASE" if (fv - eom).days > 45 else ""
   AGENTS/LABOR/scripts/boot.py: SERIES (none literal)
   AGENTS/LABOR/scripts/labor_data.py: SERIES ['CCSA', 'EMRATIO', 'FORGE', 'IC4WSA', 'ICSA', 'PAYEMS', 'TEMPHELPS', 'UNRATE']
      SERIES-NOT-IN-STATUS  FORGE  (aliases tried: ['FORGE'])
      CONST       300000  line  131  in STATUS  :: if val > 300_000:
      CONST       251000  line  133  NOT IN STATUS ⚠️  :: elif val >= 251_000:
      CONST          250  line  134  in STATUS  :: flag = "🟠"   # ARM T-01 provisional (confirm on a 2nd consecutive >250K)
      CONST       230000  line  135  in STATUS  :: elif val >= 230_000:
      CONST       250000  line  140  in STATUS  :: if val > 250_000:
      CONST      1900000  line  151  NOT IN STATUS ⚠️  :: flag = "🟢" if val < 1_900_000 else "🟠"
      CONST            6  line  192  in STATUS  :: t6 = tenths(obs[6][1]) if len(obs) > 6 and obs[6][1] is not None else None
      CONST           -5  line  200  NOT IN STATUS ⚠️  :: if d6 <= -5 and d3 <= -3:
      CONST           -3  line  200  in STATUS  :: if d6 <= -5 and d3 <= -3:
      CONST          0.5  line  201  in STATUS  :: flag = "🔴"   # T-04: >=0.5pp over 6m AND >=0.3pp over 3m
      CONST          0.3  line  201  in STATUS  :: flag = "🔴"   # T-04: >=0.5pp over 6m AND >=0.3pp over 3m
      CONST          100  line  211  in STATUS  :: elif mom < 100:
      CONST          200  line  213  in STATUS  :: elif mom >= 200:
   AGENTS/LABOR/scripts/spine_check.py: SERIES ['FORGE', 'ICSA']
      SERIES-NOT-IN-STATUS  FORGE  (aliases tried: ['FORGE'])
   AGENTS/LABOR/scripts/warn_texas.py: SERIES (none literal)
      CONST           10  line   44  in STATUS  :: if isinstance(v, str) and len(v) >= 10:
   AGENTS/LABOR/tools/form4_scanner.py: SERIES (none literal)
   AGENTS/LABOR/tools/job_postings_tracker.py: SERIES (none literal)
      SERIES-IN-STATUS-NOT-FETCHED  CIVPART  ('LFPR' on 2 trigger-shaped STATUS line(s); first: | 🔴 **U-3 — DEMOTED TO A REPORTED GAUGE 2026-08-07 (BD-15); carries NO trigger** | **4.1%*)
      SERIES-IN-STATUS-NOT-FETCHED  JTSHIL  ('hires' on 2 trigger-shaped STATUS line(s); first: | JOLTS hires **(GROSS — read beside NET, never alone)** | **5,054K / rate 3.2%** [July, B)
   flags: 8  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[LIQUID] scripts: AGENTS/LIQUID/scripts/boot.py, AGENTS/LIQUID/scripts/cftc_tff_rates.py, AGENTS/LIQUID/scripts/fp_backtest_079.py, AGENTS/LIQUID/scripts/gate069_legs.py, AGENTS/LIQUID/scripts/hy_oas_watch.py, AGENTS/LIQUID/scripts/sofr_dispersion.py, AGENTS/LIQUID/scripts/t3_decoupling.py · STATUS scope: threshold section(s) (4,426 B)
   AGENTS/LIQUID/scripts/boot.py: SERIES ['BAMLC0A0CM', 'BAMLH0A0HYM2', 'BAMLH0A1HYBB', 'BAMLH0A3HYC', 'BAMLHE00EHYIOAS', 'CREDIT', 'DGS10', 'DGS2', 'DGS30', 'DOMESTIC', 'FORGE', 'IORB', 'PARTIAL', 'RPONMBSD', 'RPONTSYD', 'RRPONTSYD', 'SOFR', 'SOFR75', 'SOFR99', 'WRESBAL']
      SERIES-NOT-IN-STATUS  BAMLC0A0CM  (aliases tried: ['BAMLC0A0CM'])
      SERIES-NOT-IN-STATUS  BAMLH0A1HYBB  (aliases tried: ['BAMLH0A1HYBB'])
      SERIES-NOT-IN-STATUS  BAMLHE00EHYIOAS  (aliases tried: ['BAMLHE00EHYIOAS'])
      SERIES-NOT-IN-STATUS  DOMESTIC  (aliases tried: ['DOMESTIC'])
      SERIES-NOT-IN-STATUS  FORGE  (aliases tried: ['FORGE'])
      SERIES-NOT-IN-STATUS  PARTIAL  (aliases tried: ['PARTIAL'])
      SERIES-NOT-IN-STATUS  RPONMBSD  (aliases tried: ['RPONMBSD'])
      SERIES-NOT-IN-STATUS  RPONTSYD  (aliases tried: ['RPONTSYD'])
      SERIES-NOT-IN-STATUS  RRPONTSYD  (aliases tried: ['RRPONTSYD'])
      CONST          280  line   25  in STATUS  :: a red thesis trigger (HY >280 or <260, USD/JPY >160, SRF >50) still exits 0. Par
      CONST          260  line   25  in STATUS  :: a red thesis trigger (HY >280 or <260, USD/JPY >160, SRF >50) still exits 0. Par
      CONST          160  line   25  in STATUS  :: a red thesis trigger (HY >280 or <260, USD/JPY >160, SRF >50) still exits 0. Par
      CONST           50  line   25  in STATUS  :: a red thesis trigger (HY >280 or <260, USD/JPY >160, SRF >50) still exits 0. Par
      CONST          265  line  113  in STATUS  :: elif bps >= 265: m, n = "🟡", f"X1 APPROACH (265-280 band) — {280 - bps:.0f}bps t
      CONST         1000  line  166  NOT IN STATUS ⚠️  :: if ccc > 1000:  m, n = "🔴", "CCC tail >1000 trip" + _src
      CONST          400  line  184  in STATUS  :: if gap < 400:   m, n = "🔴", "PIN BROKEN (<400) — bifurcation falsified (NEXUS R3
      CONST          500  line  185  NOT IN STATUS ⚠️  :: elif gap < 500: m, n = "🟠", "tail-gap compressing toward the <400 falsifier"
      CONST          110  line  199  in STATUS  :: if ig_bps > 110:  m, n = "🔴", "REGIME (>110) — IG leads when transmission is bal
      CONST           94  line  200  in STATUS  :: elif ig_bps > 94: m, n = "🟠", "2026-HIGH BREAK (>94) — leading-indicator inflect
      CONST          250  line  209  NOT IN STATUS ⚠️  :: if basis > 250:   m, n = "🟠", "junk-specific DECOMPRESSION (2026 high 253, 3/30 
      CONST          180  line  210  in STATUS  :: elif basis < 180: m, n = "🟡", "complacency extreme (below the 2026 low 189)"
      CONST         3.70  line  238  in STATUS  :: m, n = ("🟠", "above 3.70") if v > 3.70 else ("🟢", "")
      CONST           30  line  296  in STATUS  :: if s99 >= 30:   m, n = "🔴", f"GATE-LIQ-079 ACUTE LEG AT/ABOVE +30bp — check non-
      CONST           20  line  297  in STATUS  :: elif s99 >= 20: m, n = "🟠", f"tail elevated — {30 - s99:.0f}bps under the +30 AR
      CONST         4.50  line  317  in STATUS  :: m, n = ("🟠", "ABOVE 4.50 pivot") if v > 4.50 else ("🟢", "below 4.50 pivot")
      CONST         5.00  line  325  in STATUS  :: if v > 5.00:    m, n = "🟠", "ABOVE 5.00 — duration regime re-establishing (need 
      CONST         4.90  line  326  in STATUS  :: elif v < 4.90:  m, n = "🟠", "BELOW 4.90 — duration UNWIND test firing"
      CONST          2.8  line  337  in STATUS  :: if t < 2.8:   m, n = "🟠", "BELOW $2.8T floor — escalate PROME"
      CONST          2.9  line  338  NOT IN STATUS ⚠️  :: elif t < 2.9: m, n = "🟡", f"cushion ${(t - 2.8) * 1000:.0f}B (<$100B) — Leg-A dr
      CONST            5  line  347  in STATUS  :: m, n = ("🟡", "ABOVE $5B — buffer re-activating? (check sustained vs month-end no
      CONST          130  line  370  in STATUS  :: ("APO",  "CREDIT",  "APO",     lambda p: ("🟡", "co-trigger satisfied (>$130) — N
      CONST        12.50  line  371  in STATUS  :: ("BIZD", "CREDIT",  "BIZD",    lambda p: ("🟡", "above $12.50 mark-stress line") 
      CONST           25  line  372  in STATUS  :: ("^VIX", "CREDIT",  "VIX",     lambda p: ("🟠", ">25") if p > 25 else (("🟡", "ele
      CONST            7  line  532  in STATUS  :: elif d <= 7:
      CONST            8  line  575  in STATUS  :: if len(p) != 8:
      CONST           13  line  612  in STATUS  :: if len(p) != 13:
      CONST           10  line  616  in STATUS  :: if not (sid.startswith("KB-LIQ-") and len(sid) == 10 and sid[7:].isdigit()):
   AGENTS/LIQUID/scripts/cftc_tff_rates.py: SERIES (none literal)
   AGENTS/LIQUID/scripts/fp_backtest_079.py: SERIES ['EFFR', 'FRED', 'IOER', 'IORB', 'RRPONTSYD', 'SOFR', 'SOFR99']
      SERIES-NOT-IN-STATUS  EFFR  (aliases tried: ['EFFR'])
      SERIES-NOT-IN-STATUS  IOER  (aliases tried: ['IOER'])
      SERIES-NOT-IN-STATUS  RRPONTSYD  (aliases tried: ['RRPONTSYD'])
      CONST            5  line   43  in STATUS  :: return d.weekday() < 5
      CONST           12  line   63  in STATUS  :: if m == 12:
      CONST            7  line  186  in STATUS  :: if (dt.date.fromisoformat(d) - dt.date.fromisoformat(cur[-1])).days > 7:
      CONST           30  line  192  in STATUS  :: if len(s) > 30:
      CONST           20  line  201  in STATUS  :: return (n, sum(vals)/n, vals_sorted[int(n*0.95)] if n > 20 else max(vals), max(v
   AGENTS/LIQUID/scripts/gate069_legs.py: SERIES (none literal)
      CONST          220  line    5  in STATUS  :: Registry letter: "ANY ONE of 5 legs: BB>220-while-CCC-flat · CoreWeave 5Y CDS re
      CONST            6  line   42  in STATUS  :: if len(d) < 6:
      CONST          -15  line   87  NOT IN STATUS ⚠️  :: l4_eq = worst is not None and worst[1] <= -15
   AGENTS/LIQUID/scripts/hy_oas_watch.py: SERIES ['BAMLH0A0HYM2', 'FORGE']
      SERIES-NOT-IN-STATUS  FORGE  (aliases tried: ['FORGE'])
   AGENTS/LIQUID/scripts/sofr_dispersion.py: SERIES ['IORB', 'SOFR75']
      CONST           10  line   56  in STATUS  :: if len(xs) < 10:
   AGENTS/LIQUID/scripts/t3_decoupling.py: SERIES ['BAMLH0A0HYM2', 'DTWEXBGS', 'VIXCLS']
      SERIES-NOT-IN-STATUS  DTWEXBGS  (aliases tried: ['DTWEXBGS'])
      CONST         0.15  line  107  NOT IN STATUS ⚠️  :: band = ("<0.15  => SHARED FACTOR IS THE DOLLAR" if r < 0.15
      CONST         0.45  line  108  NOT IN STATUS ⚠️  :: else ">=0.45 => ~1.5 NEAR THE CEILING" if r >= 0.45
   flags: 21  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[MARCO] scripts: AGENTS/MARCO/scripts/boot.py, AGENTS/MARCO/scripts/floor_controlled_test.py, AGENTS/MARCO/scripts/ml_to_kb.py, AGENTS/MARCO/tools/bts_airport_pull.py, AGENTS/MARCO/tools/fl_migration_proxies.py · STATUS scope: WHOLE STATUS (no threshold-named section found) (34,401 B)
   AGENTS/MARCO/scripts/boot.py: SERIES (none literal)
   AGENTS/MARCO/scripts/floor_controlled_test.py: SERIES (none literal)
      CONST         0.40  line  131  NOT IN STATUS ⚠️  :: if hi_missrate > 0.40:
      CONST          1.5  line  140  in STATUS  :: c1 = hi_mean is not None and hi_mean >= 1.5
      CONST          0.5  line  147  in STATUS  :: n1 = hi_mean is not None and hi_mean < 0.5
   AGENTS/MARCO/scripts/ml_to_kb.py: SERIES ['FRED']
      CONST           90  line   38  in STATUS  :: if conf >= 90:
      CONST           80  line   40  in STATUS  :: elif conf >= 80:
      CONST           70  line   42  in STATUS  :: elif conf >= 70:
      CONST           60  line   44  in STATUS  :: elif conf >= 60:
   AGENTS/MARCO/tools/bts_airport_pull.py: SERIES (none literal)
      CONST          200  line   79  in STATUS  :: if r.status_code != 200:
      CONST            5  line   88  in STATUS  :: if len(cells) >= 5 and re.fullmatch(r"(19|20)\d\d", cells[0]) \
   AGENTS/MARCO/tools/fl_migration_proxies.py: SERIES (none literal)
      CONST            9  line  131  in STATUS  :: if len(f) >= 9:
      SERIES-IN-STATUS-NOT-FETCHED  CIVPART  ('LFPR' on 2 trigger-shaped STATUS line(s); first: | LFPR — Less-Than-HS-Diploma, 25+ (7/9) | **43.1% Jun'26 vs 49.0% series-high Jul'25** (F)
      SERIES-IN-STATUS-NOT-FETCHED  ICSA  ('claims' on 3 trigger-shaped STATUS line(s); first: | FL Condo Inventory | **7.8mo July — CORAL-canonical 9/2, 4th straight tightening** (8.9 )
      SERIES-IN-STATUS-NOT-FETCHED  DCOILBRENTEU  ('Brent' on 1 trigger-shaped STATUS line(s); first: - 🔴 **THE 8/24 GRADE NEVER HAPPENED.** The re-arm was **PENDING-CONFIRM** on 8/21 with nin)
   flags: 4  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[ORACLE] scripts: AGENTS/ORACLE/scripts/kalshi.py, AGENTS/ORACLE/scripts/polymarket.py, AGENTS/ORACLE/tools/t6_pin.py · STATUS scope: WHOLE STATUS (no threshold-named section found) (20,097 B)
   AGENTS/ORACLE/scripts/kalshi.py: SERIES (none literal)
      CONST         1000  line  129  in STATUS  :: thin = (oi or 0) < 1000 and (liq or 0) < 1000
      CONST            7  line  177  in STATUS  :: if m.get("days_left") is not None and 0 <= m["days_left"] <= 7:
      CONST         0.99  line  197  NOT IN STATUS ⚠️  :: _book_ok = sp is not None and 0.03 <= sp < 0.99
      CONST         0.01  line  200  NOT IN STATUS ⚠️  :: and abs(yes - mid) >= 0.01):
      CONST            4  line  324  in STATUS  :: if len(parts) < 4:
   AGENTS/ORACLE/scripts/polymarket.py: SERIES (none literal)
      CONST            7  line   97  in STATUS  :: expiring = (not resolved) and days_left is not None and 0 <= days_left <= 7
      CONST         0.40  line  264  in STATUS  :: "spiky": (hi - lo) > 0.40 and (now - lo) < 0.15,
      CONST         0.15  line  264  NOT IN STATUS ⚠️  :: "spiky": (hi - lo) > 0.40 and (now - lo) < 0.15,
      CONST            4  line  330  in STATUS  :: "route": parts[4] if len(parts) > 4 else ""})
      CONST           10  line  628  in STATUS  :: s = sub.add_parser("pull"); s.add_argument("--log", action="store_true"); s.add_
   AGENTS/ORACLE/tools/t6_pin.py: SERIES ['KXFED']
      CONST            5  line   87  in STATUS  :: is_sess = "Y" if d.weekday() < 5 else "N"
      SERIES-IN-STATUS-NOT-FETCHED  DCOILBRENTEU  ('Brent' on 5 trigger-shaped STATUS line(s); first: 🔑 **The structural finding: NO option both escapes this parameter AND keeps the disruption)
      SERIES-IN-STATUS-NOT-FETCHED  DCOILWTICO  ('WTI' on 2 trigger-shaped STATUS line(s); first: `will-wti-reach-100-in-september-2026` is **LIVE: 39.5%** (Δ1d +7.0, Δ7d **+25.5**, vol **)
   flags: 5  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[OTTO] scripts: AGENTS/OTTO/scripts/abs_issuance_tracker.py, AGENTS/OTTO/scripts/boot.py, AGENTS/OTTO/scripts/extension_proxy.py, AGENTS/OTTO/scripts/panel_10d.py, AGENTS/OTTO/scripts/severity_divergence.py, AGENTS/OTTO/scripts/shelf_halt_monitor.py · STATUS scope: threshold section(s) (861 B)
   AGENTS/OTTO/scripts/abs_issuance_tracker.py: SERIES (none literal)
      CONST            8  line  155  NOT IN STATUS ⚠️  :: if len(latest) >= 8:
   AGENTS/OTTO/scripts/boot.py: SERIES ['FORGE']
      SERIES-NOT-IN-STATUS  FORGE  (aliases tried: ['FORGE'])
   AGENTS/OTTO/scripts/extension_proxy.py: SERIES (none literal)
      CONST           25  line  152  NOT IN STATUS ⚠️  :: if score < 25:
      CONST           50  line  154  NOT IN STATUS ⚠️  :: elif score < 50:
      CONST           75  line  156  NOT IN STATUS ⚠️  :: elif score < 75:
      CONST            8  line  200  NOT IN STATUS ⚠️  :: if len(latest) >= 8:
   AGENTS/OTTO/scripts/panel_10d.py: SERIES (none literal)
      CONST           25  line   15  NOT IN STATUS ⚠️  :: what broke OTTO-04 — deep-subprime 2022 collateral was >25% CNL while the blende
      CONST         0.01  line  114  NOT IN STATUS ⚠️  :: return abs(got - CONTROL["value"]) < 0.01
   AGENTS/OTTO/scripts/severity_divergence.py: SERIES (none literal)
   AGENTS/OTTO/scripts/shelf_halt_monitor.py: SERIES (none literal)
   flags: 8  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[OZK] scripts: AGENTS/OZK/scripts/boot.py · STATUS scope: WHOLE STATUS (no threshold-named section found) (30,592 B)
   AGENTS/OZK/scripts/boot.py: SERIES ['FORGE', 'OSERR', 'TIMEOUT']
      SERIES-NOT-IN-STATUS  OSERR  (aliases tried: ['OSERR'])
      SERIES-NOT-IN-STATUS  TIMEOUT  (aliases tried: ['TIMEOUT'])
      CONST          2.0  line   56  in STATUS  :: ("Past-due >$550M or >2.0% — Q2'26 $298M/0.92% (OZK-06 FALSE, improved from $465
      CONST            5  line   76  in STATUS  :: while d.weekday() >= 5:
      CONST          8.2  line  220  NOT IN STATUS ⚠️  :: ozk_line = f"  OZK  ${p:>8.2f}  ({chg:+.2f}%){vtag}   {'  '.join(flags) if flags
      CONST           14  line  249  in STATUS  :: soon = "⏰ " if cal <= 14 else "   "
      CONST            7  line  305  in STATUS  :: flag = " \u26a0\ufe0f STALE" if age > 7 else ""
   flags: 3  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[RED] scripts: AGENTS/RED/scripts/base_rate_review.py, AGENTS/RED/scripts/boot.py · STATUS scope: WHOLE STATUS (no threshold-named section found) (30,485 B)
   AGENTS/RED/scripts/base_rate_review.py: SERIES ['BAMLH0A0HYM2', 'BAMLH0A3HYC', 'DGS30', 'ICSA', 'T5YIFR', 'VIXCLS']
      SERIES-NOT-IN-STATUS  BAMLH0A3HYC  (aliases tried: ['BAMLH0A3HYC'])
      SERIES-NOT-IN-STATUS  T5YIFR  (aliases tried: ['T5YIFR'])
      CONST          1.5  line   17  in STATUS  :: a RED flag, >= 1.5x an ORANGE one. A missing/MANUAL cell prints as such.
      CONST          2.0  line  148  in STATUS  :: if ratio >= 2.0 or ratio <= 0.5:
      CONST          0.5  line  148  NOT IN STATUS ⚠️  :: if ratio >= 2.0 or ratio <= 0.5:
   AGENTS/RED/scripts/boot.py: SERIES ['BAMLH0A0HYM2', 'BAMLH0A3HYC', 'ICSA', 'T5YIFR', 'VIXCLS']
      SERIES-NOT-IN-STATUS  BAMLH0A3HYC  (aliases tried: ['BAMLH0A3HYC'])
      SERIES-NOT-IN-STATUS  T5YIFR  (aliases tried: ['T5YIFR'])
      CONST            5  line  136  in STATUS  :: d = date(y, m, 31) if m != 5 else date(y, 5, 31)
      CONST            6  line  141  in STATUS  :: return d - timedelta(days=1) if d.weekday() == 5 else (d + timedelta(days=1) if 
      CONST         2021  line  150  in STATUS  :: if y >= 2021:
      CONST          100  line  262  in STATUS  :: thr_s = f"{thr:,.2f}" if abs(thr) < 100 and thr != int(thr) else f"{thr:,.0f}"
      CONST           14  line  382  in STATUS  :: if days > 14 and not verbose:
      SERIES-IN-STATUS-NOT-FETCHED  EMRATIO  ('EPOP' on 2 trigger-shaped STATUS line(s); first: **Last Updated:** 2026-09-06 ~10:3x ET [`date`-verified] — **S41: FIRST WEIGHT MOVE IN 16 )
      SERIES-IN-STATUS-NOT-FETCHED  UNRATE  ('U-3' on 6 trigger-shaped STATUS line(s); first: **Last Updated:** 2026-09-06 ~10:3x ET [`date`-verified] — **S41: FIRST WEIGHT MOVE IN 16 )
      SERIES-IN-STATUS-NOT-FETCHED  CIVPART  ('LFPR' on 3 trigger-shaped STATUS line(s); first: **Last Updated:** 2026-09-06 ~10:3x ET [`date`-verified] — **S41: FIRST WEIGHT MOVE IN 16 )
      SERIES-IN-STATUS-NOT-FETCHED  PAYEMS  ('NFP' on 5 trigger-shaped STATUS line(s); first: **Confidence 68% (S41 9/6: 69→68, −1 discretionary — 16 sessions at 69 ends here). Net-bea)
      SERIES-IN-STATUS-NOT-FETCHED  DCOILBRENTEU  ('Brent' on 2 trigger-shaped STATUS line(s); first: | **Full Stagflation Spiral** | **32%** | **−2** | **−2 mechanical (FT-06), −4 discretiona)
   flags: 10  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[REGINALD] scripts: AGENTS/REGINALD/scripts/8k_monitor.py, AGENTS/REGINALD/scripts/darkpool.py, AGENTS/REGINALD/scripts/insider.py, AGENTS/REGINALD/scripts/options_oi.py, AGENTS/REGINALD/scripts/si_refresh.py, AGENTS/REGINALD/scripts/thresholds.py · STATUS scope: threshold section(s) (13,747 B)
   AGENTS/REGINALD/scripts/8k_monitor.py: SERIES (none literal)
   AGENTS/REGINALD/scripts/darkpool.py: SERIES ['EGBN', 'ZION']
      CONST            5  line   85  in STATUS  :: if d.weekday() >= 5:
      CONST          100  line   89  in STATUS  :: if data and len(data) > 100:
      CONST           10  line  164  in STATUS  :: if delta > 10:
   AGENTS/REGINALD/scripts/insider.py: SERIES (none literal)
      CONST            5  line   70  in STATUS  :: if len(LAST_ERRORS) < 5:
   AGENTS/REGINALD/scripts/options_oi.py: SERIES ['EGBN']
      CONST          1.5  line  148  NOT IN STATUS ⚠️  :: elif agg_pc > 1.5:
   AGENTS/REGINALD/scripts/si_refresh.py: SERIES ['EGBN', 'ZION']
      CONST            4  line   66  in STATUS  :: pct = float(parts[4]) if len(parts) > 4 and parts[4] else 0
      CONST           10  line  142  in STATUS  :: if d["pct_float"] > 10:
      CONST            5  line  144  in STATUS  :: elif d["pct_float"] > 5:
   AGENTS/REGINALD/scripts/thresholds.py: SERIES ['BREACHED', 'WARNING']
      SERIES-NOT-IN-STATUS  BREACHED  (aliases tried: ['BREACHED'])
      SERIES-NOT-IN-STATUS  WARNING  (aliases tried: ['WARNING'])
      SERIES-IN-STATUS-NOT-FETCHED  ICSA  ('claims' on 3 trigger-shaped STATUS line(s); first: | Claims >300K | → §THRESHOLD STATUS | LABOR → all ORANGE banks escalate to RED |)
      SERIES-IN-STATUS-NOT-FETCHED  IC4WSA  ('4-wk' on 1 trigger-shaped STATUS line(s); first: | Claims | >300K | **203K** [FRED ICSA w/e **8/22**] | 🟢 **97K of buffer** — and ⚠️ **the )
      SERIES-IN-STATUS-NOT-FETCHED  DGS10  ('10Y' on 2 trigger-shaped STATUS line(s); first: ## ⚠️ THRESHOLD STATUS (**price rows WAL/KRE re-pulled at the Tue 2026-09-01 SETTLED CLOSE)
      SERIES-IN-STATUS-NOT-FETCHED  DGS30  ('30Y' on 2 trigger-shaped STATUS line(s); first: ## ⚠️ THRESHOLD STATUS (**price rows WAL/KRE re-pulled at the Tue 2026-09-01 SETTLED CLOSE)
      SERIES-IN-STATUS-NOT-FETCHED  BAMLH0A0HYM2  ('HY OAS' on 7 trigger-shaped STATUS line(s); first: | HY OAS >320bps (`REG-T-03`) | → §THRESHOLD STATUS | CARL → credit transmission confirmed)
      SERIES-IN-STATUS-NOT-FETCHED  VIXCLS  ('VIX' on 2 trigger-shaped STATUS line(s); first: ## ⚠️ THRESHOLD STATUS (**price rows WAL/KRE re-pulled at the Tue 2026-09-01 SETTLED CLOSE)
      SERIES-IN-STATUS-NOT-FETCHED  DCOILBRENTEU  ('Brent' on 2 trigger-shaped STATUS line(s); first: ## ⚠️ THRESHOLD STATUS (**price rows WAL/KRE re-pulled at the Tue 2026-09-01 SETTLED CLOSE)
      SERIES-IN-STATUS-NOT-FETCHED  DCOILWTICO  ('WTI' on 1 trigger-shaped STATUS line(s); first: | Brent | n/a | **$95.16** [**9/1 CLOSE**, BZ=F, **+5.16%**] | 🟠 **RE-UPGRADED 🟡→🟠 — +$6.5)
   flags: 11  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[SAM] scripts: AGENTS/SAM/scripts/bis_gli.py, AGENTS/SAM/scripts/boj_ois.py, AGENTS/SAM/scripts/boot.py, AGENTS/SAM/scripts/cpi_japan.py, AGENTS/SAM/scripts/fxy_options.py, AGENTS/SAM/scripts/gpif_flows.py, AGENTS/SAM/scripts/grade_8_14_branch.py, AGENTS/SAM/scripts/jgb_auctions.py, AGENTS/SAM/scripts/jgb_yields.py, AGENTS/SAM/scripts/mof_flows.py, AGENTS/SAM/scripts/rate_differential.py, AGENTS/SAM/scripts/thresholds.py, AGENTS/SAM/scripts/trade_balance_japan.py, AGENTS/SAM/scripts/usdjpy.py, AGENTS/SAM/scripts/xccy_basis.py · STATUS scope: threshold section(s) (4,897 B)
   AGENTS/SAM/scripts/bis_gli.py: SERIES (none literal)
      CONST          200  line   75  in STATUS  :: if r.status != 200:
   AGENTS/SAM/scripts/boj_ois.py: SERIES (none literal)
      CONST        100.0  line  218  NOT IN STATUS ⚠️  :: if not (0.0 <= v <= 100.0):
   AGENTS/SAM/scripts/boot.py: SERIES (none literal)
   AGENTS/SAM/scripts/cpi_japan.py: SERIES (none literal)
      CONST           10  line  234  in STATUS  :: if len(tcode) != 10:
      CONST            6  line  267  in STATUS  :: if len(parts) >= 6:
      CONST            7  line  268  in STATUS  :: row_base = parts[6] if len(parts) >= 7 else "2020"
      CONST          1.2  line  359  in STATUS  :: if v < 1.2:
      CONST          1.5  line  361  in STATUS  :: if v < 1.5:
      CONST          1.8  line  363  in STATUS  :: if v < 1.8:
      CONST          2.2  line  375  NOT IN STATUS ⚠️  :: if v < 2.2:
      CONST          0.5  line  384  NOT IN STATUS ⚠️  :: if gap >= 0.5:
      CONST          0.2  line  386  in STATUS  :: if gap <= 0.2:
      CONST         -0.2  line  446  NOT IN STATUS ⚠️  :: if diff < -0.2:
      CONST          0.1  line  448  NOT IN STATUS ⚠️  :: elif diff > 0.1:
   AGENTS/SAM/scripts/fxy_options.py: SERIES (none literal)
      CONST          3.0  line   78  in STATUS  :: return v == v and 0.001 < v < 3.0
      CONST         0.12  line  139  NOT IN STATUS ⚠️  :: if abs(call25["delta"] - 0.25) > 0.12 or abs(put25["delta"] + 0.25) > 0.12:
      CONST           10  line  157  in STATUS  :: if iv_pct < 10:
      CONST           12  line  159  in STATUS  :: if iv_pct < 12:
      CONST           15  line  161  in STATUS  :: if iv_pct < 15:
      CONST           18  line  163  in STATUS  :: if iv_pct < 18:
      CONST         -0.5  line  198  NOT IN STATUS ⚠️  :: if rr <= -0.5:
      CONST          0.5  line  200  NOT IN STATUS ⚠️  :: if rr < 0.5:
      CONST         -1.0  line  307  in STATUS  :: if z <= -1.0:
      CONST          1.0  line  313  in STATUS  :: elif z < 1.0:
      CONST          1.5  line  606  in STATUS  :: elif agg_pc < 1.5:
      CONST           25  line  611  in STATUS  :: if zone_pct > 25:
   AGENTS/SAM/scripts/gpif_flows.py: SERIES (none literal)
      CONST            4  line  191  in STATUS  :: status = "OK" if comp_found == 4 and "asset_size" in out and "return_pct" in out
      CONST            5  line  214  in STATUS  :: if len(pairs) >= 5:
      CONST          0.5  line  219  NOT IN STATUS ⚠️  :: if abs(pct_sum - 100.0) < 0.5 and total[0] and abs(val_sum - total[0]) < max(1.0
      CONST          2.0  line  284  in STATUS  :: elif dist_to_edge < 2.0:
      CONST            6  line  377  in STATUS  :: if 4 <= month <= 6:
      CONST            7  line  379  in STATUS  :: elif month == 7:
   AGENTS/SAM/scripts/grade_8_14_branch.py: SERIES (none literal)
   AGENTS/SAM/scripts/jgb_auctions.py: SERIES (none literal)
      CONST          404  line   67  NOT IN STATUS ⚠️  :: EVERY failure — a dead `if e.code == 404: return None, url` / `return None, url`
      CONST           13  line  166  in STATUS  :: if len(cells) < 13:
      CONST          2.0  line  233  in STATUS  :: if btc < 2.0:
      CONST          2.8  line  235  NOT IN STATUS ⚠️  :: elif btc < 2.8 and (tail_bp is not None and tail_bp > 3):
      CONST            5  line  239  in STATUS  :: elif tail_bp is not None and tail_bp > 5:
   AGENTS/SAM/scripts/jgb_yields.py: SERIES (none literal)
      CONST            9  line   20  in STATUS  :: no other source. Measured instance: SAM was dark 8/27 -> 9/1 and 2026-08-27,
      CONST           16  line  184  in STATUS  :: if off is None or len(parts) < 16:
      CONST            6  line  469  in STATUS  :: if len(rows) >= 6:
   AGENTS/SAM/scripts/mof_flows.py: SERIES (none literal)
      CONST           12  line  134  in STATUS  :: if len(fields) < 12:
      CONST            4  line  367  in STATUS  :: if len(rows) >= 4:
   AGENTS/SAM/scripts/rate_differential.py: SERIES (none literal)
   AGENTS/SAM/scripts/thresholds.py: SERIES (none literal)
      CONST          9.2  line  231  in STATUS  :: price_str = f"{p['price']:>9.2f}" if sym.endswith("=X") else f"${p['price']:>8.2
      CONST          8.2  line  231  NOT IN STATUS ⚠️  :: price_str = f"{p['price']:>9.2f}" if sym.endswith("=X") else f"${p['price']:>8.2
   AGENTS/SAM/scripts/trade_balance_japan.py: SERIES (none literal)
      CONST          100  line  273  NOT IN STATUS ⚠️  :: if brent_spot is not None and brent_spot < 100:
      CONST          -20  line  279  in STATUS  :: if me_yoy is not None and me_yoy >= -20:
      CONST           20  line  385  in STATUS  :: if abs(dev) > 20:
   AGENTS/SAM/scripts/usdjpy.py: SERIES (none literal)
      CONST            5  line  245  in STATUS  :: if len(parts) >= 5:
      CONST           10  line  395  in STATUS  :: if len(recent) >= 10:
      CONST         0.20  line  398  in STATUS  :: and (r["high"] - r["low"]) > 0.20]
      CONST          160  line  412  in STATUS  :: if close >= 160:
      CONST          156  line  414  in STATUS  :: if close >= 156:
      CONST          150  line  416  NOT IN STATUS ⚠️  :: if close >= 150:
      CONST            6  line  450  in STATUS  :: if len(rows) >= 6:
   AGENTS/SAM/scripts/xccy_basis.py: SERIES (none literal)
      CONST          8.0  line   84  in STATUS  :: if not (0.0 < last[3] < 8.0):
      SERIES-IN-STATUS-NOT-FETCHED  DGS30  ('30Y' on 1 trigger-shaped STATUS line(s); first: | JGB 30Y 4.0% | v1.6.3: **demand FLOOR with a named bid under it** (Meiji Yasuda) — not a)
      SERIES-IN-STATUS-NOT-FETCHED  DGS2  ('2Y' on 1 trigger-shaped STATUS line(s); first: | **JGB 2Y** | **hike-path read** — front-end conviction; the CASH policy leg of the froze)
      SERIES-IN-STATUS-NOT-FETCHED  T10Y2Y  ('curve' on 1 trigger-shaped STATUS line(s); first: | **JGB 2Y** | **hike-path read** — front-end conviction; the CASH policy leg of the froze)
   flags: 17  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[TERRY] scripts: AGENTS/TERRY/scripts/chain_fetch.py, AGENTS/TERRY/scripts/chain_parse.py, AGENTS/TERRY/scripts/decoupling_series.py, AGENTS/TERRY/scripts/greeks.py, AGENTS/TERRY/scripts/paper_book_mark.py, AGENTS/TERRY/scripts/snapshot.py · STATUS scope: WHOLE STATUS (no threshold-named section found) (31,569 B)
   AGENTS/TERRY/scripts/chain_fetch.py: SERIES (none literal)
      CONST           12  line  409  in STATUS  :: if len(hard) > 12:
      CONST           25  line  420  in STATUS  :: if rate >= 25:
      CONST          130  line  645  NOT IN STATUS ⚠️  :: lock_row = [r for r in uso if r["strike"] == 130][0]
      CONST          127  line  692  NOT IN STATUS ⚠️  :: if r["strike"] != 127:
   AGENTS/TERRY/scripts/chain_parse.py: SERIES (none literal)
      CONST        1.325  line  132  NOT IN STATUS ⚠️  :: assert len(rows)==2 and rows[0]['mark']==1.325 and round(rows[1]['spread_pct'],2
      CONST        15.38  line  132  NOT IN STATUS ⚠️  :: assert len(rows)==2 and rows[0]['mark']==1.325 and round(rows[1]['spread_pct'],2
   AGENTS/TERRY/scripts/decoupling_series.py: SERIES (none literal)
   AGENTS/TERRY/scripts/greeks.py: SERIES (none literal)
      CONST          0.0  line  168  in STATUS  :: return "  clears FLAT" if x == 0.0 else ("  unreachable" if x is None
   AGENTS/TERRY/scripts/paper_book_mark.py: SERIES ['OPEN', 'VIXW']
      SERIES-NOT-IN-STATUS  VIXW  (aliases tried: ['VIXW'])
      CONST            5  line  238  in STATUS  :: if cur.weekday() < 5:
      CONST           90  line  365  in STATUS  :: if d is not None and 0 <= (today - d).days <= 90:
      CONST         0.11  line  538  in STATUS  :: assert m == 0.11 and a == now and n == "mid/live", (m, a, n)
      CONST         0.09  line  554  NOT IN STATUS ⚠️  :: assert m == 0.09 and n == "last/no-nbbo", (m, a, n)
      CONST         77.0  line  594  in STATUS  :: assert r1[0][0]["strike"] == 77.0 and calls["n"] == 2, calls
      CONST          0.7  line  612  NOT IN STATUS ⚠️  :: assert mk == 0.7 and note.startswith("net-mid/live"), (mk, note)  # 1.23 - 0.53
   AGENTS/TERRY/scripts/snapshot.py: SERIES ['BAMLH0A0HYM2', 'FORGE']
      SERIES-NOT-IN-STATUS  BAMLH0A0HYM2  (aliases tried: ['BAMLH0A0HYM2', 'HY OAS', 'HY spread'])
      CONST           80  line  194  in STATUS  :: if loc >= 80:
      CONST           20  line  196  in STATUS  :: if loc <= 20:
      SERIES-IN-STATUS-NOT-FETCHED  DCOILBRENTEU  ('Brent' on 1 trigger-shaped STATUS line(s); first: **What this session actually adds is a construction result, not a position.** BRENT base-r)
   flags: 9  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[VIOLET] scripts: AGENTS/VIOLET/scripts/backfill.py, AGENTS/VIOLET/scripts/boot.py, AGENTS/VIOLET/scripts/canary_staleness.py, AGENTS/VIOLET/scripts/cftc_cot.py, AGENTS/VIOLET/scripts/cheap_tail.py, AGENTS/VIOLET/scripts/convexity_read.py, AGENTS/VIOLET/scripts/diet_coiled_spring.py, AGENTS/VIOLET/scripts/feb2018_m1m2.py, AGENTS/VIOLET/scripts/fred_fetch.py, AGENTS/VIOLET/scripts/h3_basis_lead.py, AGENTS/VIOLET/scripts/implied_corr.py, AGENTS/VIOLET/scripts/jpy_vol.py, AGENTS/VIOLET/scripts/move.py, AGENTS/VIOLET/scripts/ovx.py, AGENTS/VIOLET/scripts/regime_termination.py, AGENTS/VIOLET/scripts/skew_integrity.py, AGENTS/VIOLET/scripts/skew_trajectory.py, AGENTS/VIOLET/scripts/sustain_run_query.py, AGENTS/VIOLET/scripts/thresholds.py, AGENTS/VIOLET/scripts/two_anchor_ladder.py, AGENTS/VIOLET/scripts/vix_options.py, AGENTS/VIOLET/scripts/vx_daily_gapcheck.py, AGENTS/VIOLET/scripts/vx_history.py · STATUS scope: WHOLE STATUS (no threshold-named section found) (31,212 B)
   AGENTS/VIOLET/scripts/backfill.py: SERIES (none literal)
      CONST           15  line   76  in STATUS  :: if vix < 15: return "COMPLACENCY"
      CONST           20  line   77  in STATUS  :: if vix < 20: return "LOW_VOL"
      CONST           30  line   78  in STATUS  :: if vix < 30: return "RISING_VOL"
      CONST           40  line   79  in STATUS  :: if vix < 40: return "HIGH_VOL"
      CONST          200  line  248  in STATUS  :: if r.status_code != 200:
      CONST            5  line  322  in STATUS  :: if d.weekday() >= 5:
      CONST       1.0000  line  474  in STATUS  :: written into BOTH vix and vix3m, yielding vix3m_vix_ratio == 1.0000 —
   AGENTS/VIOLET/scripts/boot.py: SERIES ['VERDICT']
   AGENTS/VIOLET/scripts/canary_staleness.py: SERIES (none literal)
      CONST            9  line    6  in STATUS  :: COT: >9 days)."* That contract was **UNENFORCED FROM v1.0 UNTIL 2026-07-28**, an
      CONST          500  line  140  NOT IN STATUS ⚠️  :: if k > 500:          # bounded; a decade of silence is already DARK
      CONST           12  line  289  in STATUS  :: if not (1 <= mon <= 12 and 1 <= day <= 31):
      CONST           31  line  289  in STATUS  :: if not (1 <= mon <= 12 and 1 <= day <= 31):
      CONST           -1  line  325  in STATUS  :: row = text[ls: le if le != -1 else len(text)]
   AGENTS/VIOLET/scripts/cftc_cot.py: SERIES (none literal)
      CONST           25  line   80  in STATUS  :: if len(fields) < 25:
      CONST           90  line  158  in STATUS  :: if pct >= 90:
      CONST           75  line  160  in STATUS  :: if pct >= 75:
      CONST           10  line  162  in STATUS  :: if pct <= 10:
      CONST            4  line  262  in STATUS  :: if wd >= 4:  # Fri/Sat/Sun
   AGENTS/VIOLET/scripts/cheap_tail.py: SERIES (none literal)
      CONST          500  line  156  NOT IN STATUS ⚠️  :: if len(series["vix"]) < 500:
      CONST            5  line  195  in STATUS  :: if len(parts) < 5:
      CONST            4  line  231  in STATUS  :: if met == 4:
      CONST            7  line  285  in STATUS  :: if (t - prev).days > 7:
   AGENTS/VIOLET/scripts/convexity_read.py: SERIES (none literal)
      CONST           60  line  147  in STATUS  :: if len(sub) >= 60:
      CONST          5.0  line  172  in STATUS  :: if m1m2 is not None and m1m2 > 5.0:
   AGENTS/VIOLET/scripts/diet_coiled_spring.py: SERIES (none literal)
   AGENTS/VIOLET/scripts/feb2018_m1m2.py: SERIES (none literal)
   AGENTS/VIOLET/scripts/fred_fetch.py: SERIES (none literal)
   AGENTS/VIOLET/scripts/h3_basis_lead.py: SERIES (none literal)
   AGENTS/VIOLET/scripts/implied_corr.py: SERIES (none literal)
      CONST           16  line   86  in STATUS  :: basis = "SETTLE" if (et.hour, et.minute) >= (16, 15) else "TICK"
      CONST           15  line  133  in STATUS  :: state = "DISPERSED (index vol suppressed)" if (cor1m or 99) < 15 else "correlati
   AGENTS/VIOLET/scripts/jpy_vol.py: SERIES (none literal)
      CONST          300  line   76  NOT IN STATUS ⚠️  :: if hist is None or len(hist) < 300:
      CONST           16  line  161  in STATUS  :: if not (9 <= now_et.hour < 16) or now_et.weekday() >= 5:
      CONST            5  line  161  in STATUS  :: if not (9 <= now_et.hour < 16) or now_et.weekday() >= 5:
   AGENTS/VIOLET/scripts/move.py: SERIES (none literal)
      CONST        0.005  line  176  NOT IN STATUS ⚠️  :: xc_state = "agrees" if delta < 0.005 else f"DISAGREES by {delta:.2f}"
   AGENTS/VIOLET/scripts/ovx.py: SERIES (none literal)
      CONST          500  line   77  NOT IN STATUS ⚠️  :: if ovx is None or len(ovx) < 500:
   AGENTS/VIOLET/scripts/regime_termination.py: SERIES (none literal)
      CONST            5  line  116  in STATUS  :: if len(t10) >= 5:
      CONST           -3  line  124  in STATUS  :: if m["final_5d_slope"] is not None and m["final_5d_slope"] < -3:
      CONST           -5  line  153  in STATUS  :: elif lag_td < -5 and vix_spike:
   AGENTS/VIOLET/scripts/skew_integrity.py: SERIES (none literal)
   AGENTS/VIOLET/scripts/skew_trajectory.py: SERIES (none literal)
      CONST          140  line  162  in STATUS  :: "d3_below_140": d3_skew < 140 if d3_skew is not None else None,
      CONST           15  line  230  in STATUS  :: elif vix_pct < 15:
      CONST           17  line  250  in STATUS  :: us = next((m for m in metrics if m["ep"] == 17), None)
      CONST          -10  line  352  in STATUS  :: if m.get("max_1d_drop_7d") is not None and m["max_1d_drop_7d"] <= -10]
   AGENTS/VIOLET/scripts/sustain_run_query.py: SERIES (none literal)
   AGENTS/VIOLET/scripts/thresholds.py: SERIES (none literal)
      CONST           15  line  194  in STATUS  :: if vix < 15: return "COMPLACENCY"
      CONST           20  line  195  in STATUS  :: if vix < 20: return "LOW_VOL"
      CONST           30  line  196  in STATUS  :: if vix < 30: return "RISING_VOL"
      CONST           40  line  197  in STATUS  :: if vix < 40: return "HIGH_VOL"
      CONST            5  line  222  in STATUS  :: if d.weekday() >= 5:  # Sat=5, Sun=6
      CONST           16  line  406  in STATUS  :: basis = "SETTLE" if (et_now.hour, et_now.minute) >= (16, 15) else "TICK"
   AGENTS/VIOLET/scripts/two_anchor_ladder.py: SERIES (none literal)
   AGENTS/VIOLET/scripts/vix_options.py: SERIES (none literal)
      CONST          100  line   36  in STATUS  :: NOTABLE_OI = 100_000  # flag individual strikes holding >= 100K contracts
      CONST           20  line  208  in STATUS  :: collapse to zero and the >20% test fires on garbage or, once dismissed as
      CONST         0.20  line  247  in STATUS  :: if p.call_oi and abs(t.call_oi - p.call_oi) / p.call_oi > 0.20 and t.call_oi > N
   AGENTS/VIOLET/scripts/vx_daily_gapcheck.py: SERIES (none literal)
      CONST          200  line   74  in STATUS  :: if r.status_code != 200:
   AGENTS/VIOLET/scripts/vx_history.py: SERIES (none literal)
      CONST           12  line   76  in STATUS  :: ny, nm = (year + 1, 1) if month == 12 else (year, month + 1)
      CONST            4  line   79  in STATUS  :: if (d + dt.timedelta(i)).month == nm and (d + dt.timedelta(i)).weekday() == 4]
      SERIES-IN-STATUS-NOT-FETCHED  PAYEMS  ('NFP' on 3 trigger-shaped STATUS line(s); first: **PRIMARY (VIX level) = OUTCOME D, NULL** — −0.21, inside the card's own 0.3 noise floor. )
      SERIES-IN-STATUS-NOT-FETCHED  VIXCLS  ('VIX' on 10 trigger-shaped STATUS line(s); first: > **② 🔑 THE DIVERGENCE SHARPENED IN A WAY STATUS COULD NOT SEE, BECAUSE THE CURVE LEGS WER)
      SERIES-IN-STATUS-NOT-FETCHED  T10Y2Y  ('curve' on 1 trigger-shaped STATUS line(s); first: > **② 🔑 THE DIVERGENCE SHARPENED IN A WAY STATUS COULD NOT SEE, BECAUSE THE CURVE LEGS WER)
   flags: 8  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[VULCAN] scripts: AGENTS/VULCAN/tools/edgar_watch.py, AGENTS/VULCAN/tools/mag7.py, AGENTS/VULCAN/tools/semi_watch.py, AGENTS/VULCAN/tools/tsmc_watch.py, AGENTS/VULCAN/boot.py · STATUS scope: WHOLE STATUS (no threshold-named section found) (30,917 B)
   AGENTS/VULCAN/tools/edgar_watch.py: SERIES ['TICK']
      SERIES-NOT-IN-STATUS  TICK  (aliases tried: ['TICK'])
      CONST          200  line  222  in STATUS  :: if 0 <= (fd - rd).days <= 200:
      CONST            4  line  240  in STATUS  :: if len(hist) < 4:
      CONST          400  line  286  NOT IN STATUS ⚠️  :: if not 60 <= spacing <= 400:
      CONST           12  line  293  in STATUS  :: return any(abs((fe + timedelta(days=364 * k) - d).days) <= 12
      CONST           75  line  349  in STATUS  :: prior = [e for e in ends if 0 < (fd - e).days <= 75]
      CONST           45  line  446  in STATUS  :: mark = "🔔" if d_open <= 0 else ("⏳" if d_open <= 45 else "  ")
      CONST           21  line  481  in STATUS  :: elif 0 < d_open <= 21:
   AGENTS/VULCAN/tools/mag7.py: SERIES ['AGENTS', 'VULCAN']
      CONST         40.0  line  131  in STATUS  :: if p >= 40.0:
      CONST           40  line  133  in STATUS  :: return "RED-UNGRADEABLE(level>=40 but breadth leg unavailable)"
      CONST         37.0  line  136  in STATUS  :: if p >= 37.0:
      CONST         33.0  line  138  in STATUS  :: if p >= 33.0:
      CONST        10000  line  149  NOT IN STATUS ⚠️  :: if len(raw) < 10_000 or raw[:2] != b"PK":
      CONST          450  line  166  in STATUS  :: if len(h) < 450:
      CONST          1.0  line  227  in STATUS  :: if worst < 1.0 else f"ERR:inconsistent-at-{d}-worst-err={worst:.3f}%")
   AGENTS/VULCAN/tools/semi_watch.py: SERIES (none literal)
      CONST            5  line  154  in STATUS  :: if len(nums) < 5:
   AGENTS/VULCAN/tools/tsmc_watch.py: SERIES (none literal)
      CONST      2000000  line  181  NOT IN STATUS ⚠️  :: if not (50_000 <= d["rev"] <= 2_000_000):
      CONST         31.6  line  210  NOT IN STATUS ⚠️  :: (cum YoY 43.5 -> 31.6) while 2026 OSCILLATES (36.8, 29.9, 35.1, 29.9, 30.0, 35.6
   AGENTS/VULCAN/boot.py: SERIES (none literal)
      CONST         33.0  line  210  in STATUS  :: if 32.0 <= pct < 33.0:
   flags: 5  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[WAL] CANNOT-VERIFY: no threshold/fetch script found under scripts/ or tools/
[WALTER] scripts: AGENTS/WALTER/tools/intake_scan.py, AGENTS/WALTER/tools/walter_doctor.py · STATUS scope: WHOLE STATUS (no threshold-named section found) (21,703 B)
   AGENTS/WALTER/tools/intake_scan.py: SERIES ['BAMLH0A0HYM2', 'HENRY', 'PROME']
   AGENTS/WALTER/tools/walter_doctor.py: SERIES (none literal)
      CONST           30  line   30  in STATUS  :: deep_research_pending_overdue  DEEP_RESEARCH_FLAGGED_LOG row PENDING past its de
      CONST            5  line  335  in STATUS  :: if d.weekday() < 5:
      CONST           14  line  397  in STATUS  :: while items sat there. REQ-* keep the >14d retry/escalate semantics; other
      CONST            4  line  706  in STATUS  :: if len(c) >= 4:
      CONST            8  line 1330  in STATUS  :: shown = ", ".join(pending[:8]) + (" …" if len(pending) > 8 else "")
      CONST            9  line 1754  in STATUS  :: if len(r) < 9:
      CONST           10  line 2145  in STATUS  :: if n >= 10 and overrides and len(overrides) / n > 0.10:
      CONST         0.10  line 2145  in STATUS  :: if n >= 10 and overrides and len(overrides) / n > 0.10:
      SERIES-IN-STATUS-NOT-FETCHED  PAYEMS  ('NFP' on 1 trigger-shaped STATUS line(s); first: - Pre-catalyst (≤72h before WAL/ZION/OZK earnings, Fed, CPI/NFP, **US–Iran MOU / negotiati)
      SERIES-IN-STATUS-NOT-FETCHED  VIXCLS  ('VIX' on 3 trigger-shaped STATUS line(s); first: | WALTER ↔ RED | **2026-06-06 (Turn 7 WALTER re-engagement sent — light substance + 2 open)
      SERIES-IN-STATUS-NOT-FETCHED  DCOILBRENTEU  ('Brent' on 3 trigger-shaped STATUS line(s); first: *Prior refresh — 2026-07-23 Tier-2 BROAD REFRESH, 27 rows: Status/Updated/Focus regenerate)
   flags: 3  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[YEYOU] scripts: AGENTS/YEYOU/scripts/boot.py · STATUS scope: WHOLE STATUS (no threshold-named section found) (4,620 B)
   AGENTS/YEYOU/scripts/boot.py: SERIES (none literal)
   flags: 0  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
[ZHAO] scripts: AGENTS/ZHAO/scripts/boot.py · STATUS scope: threshold section(s) (206 B)
   AGENTS/ZHAO/scripts/boot.py: SERIES (none literal)
      CONST         7.40  line   43  NOT IN STATUS ⚠️  :: if v > 7.40: return ("🔴", "RED >7.40")
      CONST         7.30  line   44  NOT IN STATUS ⚠️  :: if v > 7.30: return ("🟠", "ORANGE >7.30")
      CONST         7.20  line   45  NOT IN STATUS ⚠️  :: if v < 7.20: return ("🟢", "green <7.20")
      CONST         1500  line   49  NOT IN STATUS ⚠️  :: if v > 1500: return ("🔴", "RED >1500 (BoK selling)")
      CONST         1480  line   50  NOT IN STATUS ⚠️  :: if v > 1480: return ("🟠", "ORANGE >1480")
      CONST         1450  line   51  NOT IN STATUS ⚠️  :: if v > 1450: return ("🟡", "yellow >1450")
      CONST          100  line   56  NOT IN STATUS ⚠️  :: if v > 100: return ("🟠", "energy-shock zone >$100")
      CONST            9  line  117  NOT IN STATUS ⚠️  :: if len(r) >= 9:
      CONST           16  line  190  NOT IN STATUS ⚠️  :: exp_idx = (t.year * 12 + t.month) - (2 if t.day >= 16 else 3)
      CONST            8  line  296  NOT IN STATUS ⚠️  :: if len(aged) > 8:
   flags: 10  ⚠️ presence ≠ wiring — a RETIRED bar still mentioned in STATUS reads 'in STATUS' here
WIRING-CENSUS 2: CANNOT-VERIFY on >=1 desk — a census; owner reads script vs STATUS side by side
```
