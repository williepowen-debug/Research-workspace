# 🔒 FROZEN GRADING CARD — NFP NOVEMBER + HOUSEHOLD SURVEY · Fri 2026-12-04, 08:30 ET

**Written:** 2026-11-26, 8 days before the print (C2a freeze-by 11/27; owed under PROME D:L1273). No November data exists. **Status: FROZEN. Grade off this card.**
**Author:** LABOR (Claude Code, Opus 5.5, Will's window; task from PROME prome-80) · **Consume at:** B5b.
**Release date:** confirmed at the BLS Employment Situation schedule (`bls.gov/schedule/news_release/empsit.htm`), fetched 2026-11-05 (`docket/CATALYSTS.tsv` row): *"November 2026 | Dec. 04, 2026"*. Not re-fetched today. The CR runs to 12/11, after this date.
**Companion (evidence types):** `docket/INDEPENDENCE_MAP_20260904_NFP.md`. CES legs are ONE witness; CPS legs are ONE witness.
**Why a card:** multi-loaded: **LAB-24 (resolves) · LAB-18 draw 3 of 3 (resolves) · LAB-12 · Kill A · T-03 · T-04 · T-06 · T-08 · T-13 · vectors 8 (restore counter leg 2), 10, 12, 17 · the September third-estimate watch.**
**What this card drops:** freeze-thaw v2 **FIRED 2026-11-06** (`docket/graded/GRADING_CARD_20261106_NFP.md` §8). No un-fire or re-arm letter exists, so no LEG A / LEG B / v2 row appears here; vectors 4, 6 and 7 stood down (WQ-634 A) and their letters print **as record only**. Adding any of these needs Will's word.
**Defect carried from the 11/6 card §8.5, fixed here:** T-06's slack legs read "over 3 months", so the referent is the month **three before November = August**, not the prior month (§2.4).

---

## 1. INSTRUMENT, SOURCE DOCUMENT, OBSERVATION BASIS

| Leg | Instrument | Source document | Observation basis |
|---|---|---|---|
| `N`, `S''`, `O'` (LAB-24, Kill A, v8, v17, T-06) | **Total nonfarm payrolls (CES), SA, monthly change, thousands.** `N` = November first print; `S''`, `O'` = September and October **as revised in this release** | BLS *The Employment Situation — November 2026*, 2026-12-04 08:30 ET, Table B-1 + the revisions paragraph, read through `scripts/fetch_primary.py URL --expect <fig>` (saved, text-extracted; L-33) | Changes computed **within one vintage** as `level(m) − level(m−1)`; never mix vintages (L-02) |
| U-3, LFPR, EPOP, LF (CPS) | household survey, SA | same release, Table A-1 | one decimal for rates; LF in thousands |
| LT share, involuntary part-time | Table A-12, Table A-8 | same | as printed; record only |
| Health care, federal (T-08, T-13) | CES Table B-1 lines | same | thousands |
| AHE | all private employees, YoY | same | one decimal as printed |
| Sep third estimate | PAYEMS, ALFRED vintage `20261204` | `scripts/alfred_vintages.py` | within-vintage change; diagnostic only |

⛔ A refusal of the client string `research-bot/1.0` is final (WQ-723 A, WQ-735): the reading is UNAVAILABLE and named to PROME; FRED/ALFRED may confirm levels later but nothing grades off a relay.

## 2. 🔒 PRE-COMPUTED ARITHMETIC — as FORMULAS (re-solve on the as-published vintage BEFORE reading November)

**Inputs (BLS USDL-26-1632 vintage, 2026-11-06; FRED pulled 2026-11-26 11:5x ET):** PAYEMS Aug 159,068 · Sep 159,128 · Oct 159,293 ⇒ Sep `+60K` · Oct `+165K`; `S + O = 225`. U-3 May 4.3 · Aug **4.1** · Sep 4.2 · Oct **4.1**. EPOP May **59.2** · Aug **59.1** · Sep 59.2 · Oct **59.3**. LFPR Oct **61.9**. LF Oct 170,683K. LT share Oct 27.6% · involuntary part-time 4,840K · health care +42K · federal −1K · AHE **+3.1%** YoY.

1. **LAB-24** (as registered): TRUE if `O' ≤ +149K`, FALSE if `O' ≥ +150K`, from the revisions paragraph cross-checked against Table B-1 within one vintage. No numeric NO-VERDICT band; NO-VERDICT only if no release by 2026-12-31.
2. **Kill A** (NFP ≥+200K ×3, revised): needs `S'' ≥ 200`, `O' ≥ 200` and `N ≥ 200`. On this vintage September would have to revise up `200 − 60 = 140K`. **Practically cannot fire on this print; graded on the letter anyway.**
3. **v8 restore leg 2** = net revision to Sep + Oct `(S'' − 60) + (O' − 165) ≥ 0`. Counter is **1 of 2** since 11/6; ≥0 completes it ⇒ **v8 2 → 3** (letter: "two consecutive prints with net revisions ≥0", STATUS_DETAIL § `matrix-graded-20260907`).
4. **T-06** (TRADE.md §1, re-specced 8/7) = `N < 100K` **AND** (U-3 rose ≥0.2pp over 3 months **OR** EPOP fell ≥0.3pp over 3 months). **Referent = August (three months before November):** U-3 leg **Nov ≥ 4.1 + 0.2 = 4.3** · EPOP leg **Nov ≤ 59.1 − 0.3 = 58.8**. CPS SA figures are not revised month to month; the referent is read as published in this release.
5. **T-03 🟠** = EPOP fell ≥0.3pp over 3 months ⇒ **Nov ≤ 58.8** (Aug 59.1). **T-04 🔴** = fell ≥0.5pp over 6 months (May 59.2 ⇒ **≤ 58.7**) **AND** T-03 ⇒ **58.8 fires T-03 alone; ≤58.7 fires T-03 and T-04 together.**
6. **LAB-18** draw 3 of 3 (last): **TRUE at Nov EPOP − Aug EPOP ≤ −0.3** on the published one-decimal figures (Nov ≤ 58.8); a computed −0.2 does not fire; a population-control break making Aug and Nov non-comparable does not fire. Otherwise **FALSE** (no draw left).
7. **LAB-12** resolves TRUE only at **U-3 ≥ 5.0**. Below 5.0 this card does not resolve it (`5.0 − 4.1 = 0.9pp` needed; its due date and any December draw stay on the row).
8. **v17** `M = (S'' + O' + N)/3` ⇒ `M ≥ 100K ⇒ 1 · 50K ≤ M < 100K ⇒ 2 · M < 50K ⇒ 3`. Enters at **1**. On this vintage: `N ≥ 300 − 225 = +75K` ⇒ 1 · `−75K ≤ N < +75K` ⇒ 2 · `N < 150 − 225 = −75K` ⇒ 3. **Re-solve as `N ≥ 300 − (S'' + O')` and `N < 150 − (S'' + O')`.**

## 3. 🔒 PRE-COMMITTED BANDS

### 3a. Headline payrolls, November first print (`N`) — shown at the 11/6 vintage; §5 re-solves v17's edges, T-06's 100K edge never moves

<!-- partition-axis: column="November payrolls, first print" -->
| Band | November payrolls, first print | Assignment |
|---|---|---|
| **3a-1** | ≥ 200,000 | Kill A leg met for November only (§2.2 decides). v17 → 1 band. No action |
| **3a-2** | 100,000 – 199,000 | No action. Record |
| **3a-3** | 0 – 99,000 | **T-06 payroll leg satisfied**; fires with a §2.4 slack leg (§3b, §3c) |
| **3a-4** | ≤ -1,000 | Negative print. T-06 payroll leg satisfied. Moves v17 only through §5; no other vector by itself |

### 3b. U-3 × LFPR — FULL cross-product (L-27: 4 × 3 = 12 cells), read against Aug U-3 4.1 (T-06 referent) and Oct LFPR 61.9

LFPR: down = ≤61.8 · flat = 61.9 · up = ≥62.0.

| U-3 | LFPR | Assignment |
|---|---|---|
| ≥5.0 | down | ✅ **LAB-12 RESOLVES TRUE**; T-06 U-3 leg met. ⚠️ LFPR caveat on the packet |
| ≥5.0 | flat | ✅ **LAB-12 RESOLVES TRUE**; T-06 U-3 leg met |
| ≥5.0 | up | ✅ **LAB-12 RESOLVES TRUE**; strongest slack read; T-06 U-3 leg met |
| 4.3–4.9 | down | ⚠️ T-06 U-3 leg met (the letter has no LFPR clause); caveat on the packet |
| 4.3–4.9 | flat | 🔴 Slack rising; T-06 U-3 leg met |
| 4.3–4.9 | up | 🔴 Slack rising on entrants; T-06 U-3 leg met |
| 4.2 | down | No band. Record |
| 4.2 | flat | No band. Record |
| 4.2 | up | No band. Record |
| ≤4.1 | down | ⚠️ NO-SIGNAL: the rate held on a shrinking denominator. Score nothing |
| ≤4.1 | flat | No band. Record |
| ≤4.1 | up | 🟡 Absorption cell (fourth month if it prints). No vector; recorded in CORE TENSION |

### 3c. EPOP (Nov)

| Nov EPOP | Assignment |
|---|---|
| **≥ 58.9** | No trigger. **LAB-18 ❌ FALSE** (last draw) |
| **58.8** | 🟠 **T-03 FIRES** (and T-06's EPOP leg). **LAB-18 ✅ TRUE**. T-04 not (`59.2 − 58.8 = 0.4 < 0.5`) |
| **≤ 58.7** | 🔴 **T-03 + T-04 FIRE** (and T-06's EPOP leg). **LAB-18 ✅ TRUE** |

### 3d. T-06 — FULL cross-product (payroll leg × U-3 leg × EPOP leg = 8 cells). Fires on `payroll ∧ (U-3 ∨ EPOP)`

| `N < 100K` | U-3 ≥ 4.3 | EPOP ≤ 58.8 | Assignment |
|---|---|---|---|
| yes | yes | yes | 🟠 **T-06 FIRES** (both slack legs) |
| yes | yes | no | 🟠 **T-06 FIRES** (U-3 leg; LFPR caveat per §3b) |
| yes | no | yes | 🟠 **T-06 FIRES** (EPOP leg) |
| yes | no | no | NOT fired. Record payroll leg met |
| no | yes | yes | Not fired (T-03 still per §3c) |
| no | yes | no | Not fired |
| no | no | yes | Not fired (T-03 still per §3c) |
| no | no | no | Not fired |

### 3e. Net revision to Sep + Oct — vector 8 restore leg 2 (counter **1 of 2** since 11/6)

| `(S'' − 60) + (O' − 165)` | Assignment |
|---|---|
| **≥ 0** | **v8 restore COMPLETES (2 of 2) ⇒ vector 8: 2 → 3.** Score +1 on the then-current total |
| **< 0** | counter **RESETS 1 → 0 of 2**. No downward band exists; none improvised |

### 3f. LAB-24 — October as carried by this release (`O'`)

| `O'` | LAB-24 |
|---|---|
| **≤ +149K** | ✅ **TRUE** — Brier `(1 − 0.50)² = 0.25` |
| **≥ +150K** | ❌ **FALSE** — Brier `0.50² = 0.25` |

⚠️ **LAB-24 moves nothing:** a TRUE means the v2 fire's +150K single-month leg would not have held on the revised figure; v2 has no un-fire letter and this card writes none. It travels as a caveat to PROME and TERRY (§6).

### 3g. Sector and side lines with a registered test

| Line | Band | Assignment |
|---|---|---|
| Health care | net-negative | **T-08 FIRES** → CARL + REGINALD; **v10 1 → 4** |
| Federal payrolls | ≤ −25K MoM | T-13 MoM side; **v12 moves only with UCFE corroboration in the same session** (BD-17) |
| AHE | any change from the published **+3.1%** YoY | 1c packet CARL + HENRY. No threshold |
| LT share (v6 letters, record only) | >27% AND YoY turning positive in BLS's own text · <24% | **Record only** (v6 stood down; no re-arm letter) |
| Involuntary part-time | change from 4,840K | Record only; no band |

### 3h. Predictions this print moves — gate #14(a): bands reproduce the headline

| Row | Headline | Branch | P(branch) | Post-print V | `Σ P × V` |
|---|---|---|---|---|---|
| **LAB-18** | 5% | EPOP ≤58.8 | 0.05 | ✅ 1.00 | `0.05 × 1.00 = 0.05` |
| | | EPOP ≥58.9 | 0.95 | ❌ 0 (last draw) | `0.95 × 0 = 0` |
| | | | | **total** | **0.05 = 5% ✅** |
| **LAB-24** | 50% | `O' ≤ 149K` | 0.50 | ✅ 1.00 | `0.50` |
| | | `O' ≥ 150K` | 0.50 | ❌ 0 | `0` |
| | | | | **total** | **0.50 = 50% ✅** |

LAB-12 (2%) resolves only in the ≥5.0 rows of §3b; below that it is not graded here. Monotone in the evidence direction ✅.

### 3i. September third-estimate watch (diagnostic, carried from the 11/6 card §3h; no band)

September first print **+29K** (ALFRED `20261002`), second **+60K** (`20261106`); third = ALFRED `20261204`. Reference: first→third mean **−30.4K**, SD **52.9K**, n=44 (`workbook/PAYROLL_VINTAGES.tsv`, reference months 2023-01..2026-08, computed 2026-11-26). Watch lines `29 − 30.4 ± 52.9` = **−54.3K / +24.5K**; a third estimate outside them is reported as >1 SD from the measured bias. ⚠️ The second estimate (+60K) is already above the upper line.

## 4. FALSIFIERS OF THIS CARD

1. No release at 08:30 on 12/4 ⇒ the card rolls to the actual date unchanged; nothing grades off ADP or private trackers.
2. A population-control or benchmark break inside the release ⇒ §3b/§3c do not grade until measured (LAB-18's own tie-break: does not fire).
3. A first print graded where the card specifies revised figures (Kill A, LAB-24, §3e, v17) ⇒ L-02 violation. **Revised back-months first, written in §8.0 before November is read.**
4. A relayed or summary figure ⇒ do not grade (L-33).
5. Client string refused ⇒ UNAVAILABLE, named to PROME.

## 5. v17 PAYROLL MOMENTUM (letter adopted 2026-10-28, POST-HOC base rates `domain/sources/2026-10-28_PAYROLL_VECTOR_AND_T07_BASE_RATES.md`)

**Pre-computed on the 11/6 vintage (`S + O = 60 + 165 = 225`) — RE-SOLVE on the published revisions before reading N:**

| Band | Condition on M | N bar on the 11/6 vintage | v17 |
|---|---|---|---|
| 5-1 | M ≥ 100K | `N ≥ 300 − 225 = +75K` | **1** (holds) |
| 5-2 | 50K ≤ M < 100K | `−75K ≤ N < +75K` | **2** (1 → 2) |
| 5-3 | M < 50K | `N < 150 − 225 = −75K` | **3** (1 → 3) |

Partition: `M ≥ 100 / 50 ≤ M < 100 / M < 50` is a true complement on M at 1K precision. **Mechanism vs threshold:** a band move is a THRESHOLD read on revised data, not a recession call (`M < 50K`-equivalent led a recession within 12 months `12/36 = 33.3%` vs base 18.1% since 1950; false in 2025-03, 2025-06 and 2026-02). **Travels:** STATUS matrix and NEXUS brief; no T-number rides on v17.

## 6. MECHANISM, ATTRIBUTION, WHAT TRAVELS

**Mechanism vs threshold:** every letter above is a threshold read. The live mechanism question is whether low-hire's October recovery (3-month average 137K, concentrated `137 / 165 = 83.0%` in three sectors, involuntary part-time +339K) holds; that is recorded beside the grade, never banded on print day (L-18).
**Attribution discipline:** ① seasonal holiday hiring (couriers, retail, temp help) is not attributed either way; BLS's factors already expect some. ② The November reference week (pay period including 11/12) precedes Thanksgiving and the late-November Florida flooding; no weather attribution. ③ A revision is not attributed to response rates or the 2025 shutdown on this card. ④ CES and CPS disagreeing on size is recorded, not resolved.

| Outcome | Route | Priority |
|---|---|---|
| T-03 + T-04 | **WALTER** → CARL + HENRY + REGINALD; TERRY tradeability line | 🔴 |
| T-03 alone · T-06 | **WALTER** → CARL + REGINALD + HENRY (LFPR caveat where §3b says so) | 🟠 |
| T-08 | **WALTER** → CARL + REGINALD | 🟠 |
| LAB-24 TRUE | caveat packet PROME + TERRY (the v2 fire's margin is gone on the revised figure; nothing un-fires) | 🟡 |
| AHE change | 1c packet CARL + HENRY | 🟡 |
| LAB-18 / LAB-24 / LAB-12 resolutions · v8 · v17 · §3i | STATUS + PREDICTIONS + SCOREBOARD; brief | — |

## 7. CHECKER SCOPE AT FREEZE (BD-31)

🧾 **Checker receipt at freeze (2026-11-26 11:44 EST, `card_partition_check.py`, rc=2):** `8 band table(s) — 1 verified, 7 unverified, 0 with defects` · `[✓] table 2: VERIFIED — axis 'November payrolls, first print', 4 bands, precision 1,000`. The rest fall under the BD-31 one-axis limit (the §3h ledger and this §7 table are counted as band tables but are not); the band tables are proved by hand below. **Freeze authorized on `0 defects` + the hand proof.**

| Table | Complement holds because |
|---|---|
| §3a | `≥200,000 / 100,000–199,000 / 0–99,000 / ≤−1,000` partitions the 1,000 grid |
| §3b | U-3 `≥5.0 / 4.3–4.9 / 4.2 / ≤4.1` and LFPR `≤61.8 / 61.9 / ≥62.0` each partition the one-decimal grid; **12 of 12** pairs written |
| §3c | `≥58.9 / 58.8 / ≤58.7` partitions the one-decimal grid |
| §3d | 2 × 2 × 2 = **8 of 8** cells written |
| §3e | `≥0 / <0` true complement |
| §3f | `≤149K / ≥150K` partitions the 1,000 grid |
| §5 | `M ≥ 100 / 50 ≤ M < 100 / M < 50` partitions M at 1K precision |

## 8. GRADE (write 2026-12-04 off this frozen card — never re-read a band)

*Blank until print. Order: ① read the revised `S''`, `O'`; write §8.0 (LAB-24, Kill A, §3e, §5 re-solve, §3i) and commit it BEFORE reading November · ② grade §3a–§3g as separate letters, CES and CPS named as two witnesses · ③ apply §3h · ④ STATUS (KEY THRESHOLDS, matrix, EXIT RULES, PREDICTIONS, calendar), SCOREBOARD, KB; `grep combo: workbook/KB.tsv` read whole at this NFP grade (C3) · ⑤ `git mv` to `docket/graded/`.*
