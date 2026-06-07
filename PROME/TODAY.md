# TODAY.md — Sunday June 7 → Monday June 8, 2026

**Objective:** Sun-evening week-prep refresh. Single-source week-ahead card is shipped; boot surfaces are current. Mon 6/8 opens a heavy catalyst week (CPI + Treasury refunding triplet) into FOMC 6/16-17.

**Current regime:** Substance/tape divergence is *narrowing*. Vol confirmed on Fri NFP (VIX 15.40→21.51). **HY OAS 274🟢 [FRED 6/4] is now the SOLE remaining "tape refuses cascade" signal.** Stress visible in vol/Japan-FX/BDC/gas/energy/duration; public credit is the binary line this week's catalysts will test.

---

## 🔴 Week Prep — Status

| Priority | Work | Status |
|---|---|---|
| 🔴 | Live dashboard pull | ✅ Done — yfinance installed, Sun 6/7 ~17:30 ET anchor |
| 🔴 | Ingest 3 unprocessed signals (BOND 6/5 / CARL 6/6 / HENRY 6/6) | ✅ Done — `ACTIVE_DECISIONS` updated |
| 🔴 | Build week-ahead catalyst card | ✅ Done — `PROME/action-cards/WEEK_2026-06-08.md` |
| 🔴 | Refresh boot surfaces (SCRATCH/TODAY/STATUS/FLEET_SCAN/HEARTBEAT) | In progress — TODAY (this file) + STATUS + FLEET_SCAN remain |
| 🟠 | Position-state reconciliation | Deferred per Will |
| 🟠 | Per-agent pathspec migrations | Tracker live; owner edits pending (BRENT/HENRY/MARCO/OTTO/OZK/VIOLET/WALTER) |

---

## Live Market Levels — Sun Jun 7 ~17:30 ET dashboard

| Series | Value | As-of | Zone | Read |
|---|---:|---|---|---|
| HY OAS | **274bps** | **[FRED 6/4]** | 🟢 | **Sole remaining "refuses cascade" signal.** Watch this line Mon-Wed. |
| CCC OAS | **946bps** | **[FRED 6/4]** | 🟡 | Lower-quality stress persists; no HY transmission yet. |
| **VIX** | **21.51** | live | 🟡 | **Up from 15.40 Jun 4 — Fri NFP shock landed.** Vol no longer green-refusing. |
| Brent | **$93.09** | live | 🟡 | Energy yellow; no >$100 break. |
| Gas weekly | **4.30** | **[6/1]** | 🔴 | Consumer pressure persists. |
| USD/JPY | **160.19** | live | 🔴 | Drift higher into BOJ 6/16; intervention-zone live. |
| 10Y Yield | **4.47%** | **[6/4]** | 🟡 | Back inside <4.50 band per BOND 6/5. |
| TLT | **$85.06** | live | 🟡 | Near Jun $85P strike; BOND says HOLD-no-add. |
| KRE | **$70.17** | live | 🟢 | Bank tape not confirming. |
| WAL | **$80.15** | live | 🟢 | Above bear lines; Q2-print risk remains later. |
| OZK | **$49.60** | live | 🟡 | Below $50 watch. |
| APO | **$128.03** | live | 🟡 | PC pressure visible. |
| **ARES** | **$125.65** | live | 🟡 | **At green-line ($125 boundary).** |
| **BIZD** | **$12.49** | live | 🔴 | **Broke under $12.50** (was $12.70). |
| FXY | **$57.31** | live | 🟡 | Inverse of USD/JPY 160.19. |
| Initial claims | **225k** | **[5/30]** | 🟡 | Shadow-adjusted est 280k. |
| Continuing claims | **1.777M** | **[5/23]** | 🟢 | Not yet confirming labor cascade. |
| SOFR-IORB | **-0.03** | **[6/4]** | 🟢 | No reserve-pressure signal. |

**Deltas from Jun 4 dashboard:** VIX +6pts (most important), ARES -$5 (to green-line), TLT -$0.44, BIZD -$0.21 (broke under), USD/JPY +0.18 (drift higher), 10Y +0.01.

---

## Week-Ahead Catalyst Slate

Full breakdown: **`PROME/action-cards/WEEK_2026-06-08.md`**.

| Date | Catalyst | Owner | Hottest implication |
|---|---|---|---|
| Mon 6/8 | Open: read Fri NFP follow-through | PROME | VIX-shock hold/fade + HY OAS line |
| Tue 6/9 | 3Y Treasury auction | BOND/LIQUID | Front-end demand |
| **Wed 6/10** | **May CPI 8:30 + nominal 10Y auction 1pm** | HENRY/CARL/BOND | **Sep TLT add gate; BOND matrix v2** |
| **Thu 6/11** | **30Y auction 1pm + jobless claims 8:30** | BOND/LABOR | **Term-premium re-arm test** |
| Fri 6/12 | VIOLET 4/15 60d window closes | VIOLET/Will | Vol-trade adjudication |
| Mon 6/16 | BOJ + Sumitomo Life FY2025 ESR | SAM | Channel 1 test |
| Tue-Wed 6/16-17 | FOMC | HENRY/LIQUID | Biggest gate of month |
| Thu 6/18 | Theta-killer cluster expiry | Will | Hard backstop |

---

## Agent / System State to Carry Forward

- **BOND → PROME (6/5):** long-end leg relaxed; **TLT HOLD-no-add**; next live gate is June refunding triplet, not CPI alone. Two corrections logged (5/21 TIPS vs nominal; 5/13 30Y was true May outlier).
- **CARL → PROME (6/6):** READY for separate-clones M3 atomic cutover. Pre-flight P1/P2/P4 inputs attached. Slate now: SAM/HENRY/REGINALD/OZK/CARL.
- **HENRY → PROME (6/6):** auto-memory collision-fix proposal; bundle with separate-clones decision (post-Jun-16). Interim "regenerate index instead of hand-append" fixes ~95%.
- **VIOLET (Sat 6/6):** thesis v3.5; R12 re-established after NFP-shock live test; 4/15 60d window closes Fri 6/12.
- **NEXUS:** Discipline F (shared-antecedent independence), SIG-01/02 verdicts, Fri 6/5 close anchor; E-phase scaffold pending values.
- **WALTER 6/6 PM:** 4 BOARD dispatches (CB gold / UST rollover / El Niño-fertilizer / UKMTO Hormuz); Iran anchor still Jun 2 frame.
- **SAM (Sat 6/6):** CFTC METHOD-gate test landed.
- **CARL (Fri 6/5):** data wall + Prome-directed news sweep; convergence outputs in CARL STATUS.
- **Auto-memory:** Claude owns MEMORY.md (no index hook); desktop+laptop captures merged via symlink.

---

## Do / Do Not — Monday

**Do:**
- Open the week-ahead card first.
- Pull live tape early; read whether Fri VIX-shock holds.
- Watch HY OAS — it's the binary line.
- Treat CPI 6/10 as a *narrowed* TLT Sep-add gate (BOND 6/5 changed the rule).
- Route domain questions to owning agents.

**Do not:**
- Use any old May `BROKER_PENDING` / 6/18 trigger language as actionable.
- Treat Sep TLT add as live until either CPI hot or 30Y refunding tail (one is no longer sufficient).
- Upgrade to "broad cascade" language unless HY OAS breaks (currently 274🟢).
- Pre-cable FOMC packets before Wed CPI lands (data path could shift framing).

---

## Pending After This Pass

1. STATUS surgical refresh (next).
2. FLEET_SCAN bounded week-prep rewrite (next).
3. Commit Sun closeout (PROME-scope only; pathspec).
4. Tue evening: Wed-CPI prep + TLT Sep-add packet scaffold (only if conditions look likely to fire).
5. Pre-Wed: BOND matrix v2 spawn for 1pm 10Y auction.
