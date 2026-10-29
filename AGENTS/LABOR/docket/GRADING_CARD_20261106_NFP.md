# 🔒 FROZEN GRADING CARD — NFP OCTOBER + HOUSEHOLD SURVEY · Fri 2026-11-06, 08:30 ET

**Written:** 2026-10-21, 16 days before the print (C2a freeze-by 10/30). No October data exists. **Status: FROZEN. Grade off this card.**
**Author:** LABOR (PROME-spawned session af287aee, Will-approved 09:38 ET) · **Consume at:** B5b.
**Release date VERIFIED** at the BLS Employment Situation schedule (`bls.gov/schedule/news_release/empsit.htm`, fetched 2026-10-21 09:39 ET, HTTP 200): *"October 2026 · Nov. 06, 2026 · 08:30 AM"*.
**Companion (evidence types):** `docket/INDEPENDENCE_MAP_20260904_NFP.md`. CES legs are ONE witness; CPS legs are ONE witness.
**Why a card:** multi-loaded: **freeze-thaw v2 LEG A draw 2 (the bull-side kill) · LEG B · Kill A · T-03 · T-04 · T-06 · T-08 · T-13 · vectors 6, 8, 10, 12 · LAB-12 · LAB-18 draw 2 · LAB-19 draw 2 · the §3g August third-estimate watch.**
**Input from an earlier card:** **LEG C is graded on 11/3** by `docket/GRADING_CARD_20261103_JOLTS.md` §3b. Its result is written into §2.4 below as a dated note before 11/6. Until then §3d is conditional on it.

---

## 1. INSTRUMENT, SOURCE DOCUMENT, OBSERVATION BASIS

| Leg | Instrument | Source document | Observation basis |
|---|---|---|---|
| `X`, `A'`, `S'` (LEG A, Kill A, v8) | **Total nonfarm payrolls (CES), SA, monthly change, thousands**. `X` = October first print; `A'`, `S'` = August and September **as revised in this release** | BLS *The Employment Situation — October 2026*, 2026-11-06 08:30 ET, Table B-1 + the revisions paragraph; read from the SAVED release text (L-33) | Changes computed **within one vintage** as `level(m) − level(m−1)`; never mix vintages (L-02) |
| U-3, LFPR, EPOP, LF (CPS) | household survey, SA: unemployment rate, participation rate, employment-population ratio, civilian labor force | same release, Table A-1 | one decimal for rates; LF in thousands |
| LT share (v6) | share of unemployed jobless ≥27 weeks, as **BLS's own text/Table A-12** states it | same | as printed |
| Health care, federal (T-08, T-13) | CES Table B-1 lines | same | thousands |
| AHE | all private employees, YoY | same | one decimal as printed |
| §3g | August PAYEMS MoM, ALFRED vintage `20261106` | ALFRED via `scripts/alfred_vintages.py` | within-vintage change |

## 2. 🔒 PRE-COMPUTED ARITHMETIC — as FORMULAS (regenerate on the as-published vintage BEFORE reading October)

**Inputs (BLS USDL-26-1549 vintage, 2026-10-02; FRED pulled 2026-10-21 09:39 ET):** PAYEMS Jun 158,892 · Jul 158,882 · Aug 159,015 · Sep 159,044 ⇒ Jul `−10K` · Aug `+133K` · Sep `+29K`. U-3 Sep **4.2** · LFPR **61.8** · EPOP **59.2** (Jul **58.9**, Apr **59.1**) · LF **170,262K** · LT share **27.1%** · health care **+16.7K** · federal **−1K** · AHE **+3.0%** YoY.

1. **Kill A** (NFP ≥+200K ×3, revised): needs `A' ≥ 200`, `S' ≥ 200` and `X ≥ 200`. On this vintage that means August revised +67K and September revised +171K. **Cannot fire unless both revise that far.**
2. **LEG A** = revised single month ≥+150K **AND** revised 3-month average ≥+100K ⇒ **`X ≥ max(150, 300 − (A' + S'))`** thousand. On this vintage `300 − (133 + 29) = 138` ⇒ **bar +150K**. The average leg binds if `A' + S' < 150` (a net revision below −12K: plausible). **Recompute before reading `X`.**
3. **LEG B** = EPOP not lower than 3 months prior ⇒ **Oct EPOP ≥ 58.9** (July referent; CPS is not revised month to month).
4. **LEG C** = JOLTS NET >0 in both latest months (Aug rev ∧ Sep P), **graded 11/3**. *Dated note to be written here on/after 11/3: "LEG C = MET / LOST per JOLTS card §3b, cell …"*
5. **T-06** (TRADE.md §1, re-specced 8/7, BD-15) = `X < 100K` **AND** (U-3 rose ≥0.2pp **OR** EPOP fell ≥0.3pp over 3 months) ⇒ U-3 leg: **Oct U-3 ≥ Sep + 0.2 = 4.4**; EPOP leg: **Oct ≤ 58.6**. ⚠️ STATUS KEY THRESHOLDS still prints the old U-3 bar *"≥4.3%"* and omits the EPOP leg; **this card's formula governs** (flagged for the STATUS row).
6. **T-03 🟠** = EPOP fell ≥0.3pp over 3 months ⇒ **Oct ≤ 58.6** (`58.9 − 0.3`). **T-04 🔴** = fell ≥0.5pp over 6 months (Apr 59.1 ⇒ ≤58.6) **AND** T-03 ⇒ **Oct ≤ 58.6 fires T-03 and T-04 together**: one move, not two confirmations.
7. **LAB-18** resolves ✅ at **Oct EPOP ≤ 58.6**. **LAB-19** resolves ✅ at **Oct LF MoM > 0** (`LF_Oct − 170,262K`, within the same release). **LAB-12** resolves ✅ only at **U-3 ≥ 5.0**.

## 3. 🔒 PRE-COMMITTED BANDS

### 3a. Headline payrolls, October first print (`X`) — shown at the +150K bar; if §2.2 re-solves the bar, 3a-1's lower edge moves to it and 3a-2's upper edge to one below it

<!-- partition-axis: column="October payrolls, first print" -->
| Band | October payrolls, first print | Assignment |
|---|---|---|
| **3a-1** | ≥ 150,000 | **LEG A SATISFIED** (if the re-solved bar is still +150K) → §3d decides whether v2 fires |
| **3a-2** | 100,000 – 149,000 | No action. Record |
| **3a-3** | 0 – 99,000 | T-06 payroll leg satisfied; fires with the §2.5 slack leg |
| **3a-4** | ≤ -1,000 | Negative print. **Moves no vector by itself** (§5 declared gap). T-06 payroll leg satisfied |

### 3b. U-3 × LFPR — FULL cross-product (L-27: 4 × 3 = 12 cells), read against Sep U-3 4.2 / LFPR 61.8

LFPR: down = ≤61.7 · flat = 61.8 · up = ≥61.9.

| U-3 | LFPR | Assignment |
|---|---|---|
| ≥5.0 | down | ✅ **LAB-12 RESOLVES**; T-06 U-3 leg met. ⚠️ LFPR caveat on the packet |
| ≥5.0 | flat | ✅ **LAB-12 RESOLVES**; T-06 U-3 leg met |
| ≥5.0 | up | ✅ **LAB-12 RESOLVES**; strongest slack read; T-06 U-3 leg met |
| 4.4–4.9 | down | ⚠️ T-06 U-3 leg met (the letter has no LFPR clause); caveat on the packet |
| 4.4–4.9 | flat | 🔴 Genuine slack rising; T-06 U-3 leg met |
| 4.4–4.9 | up | 🔴 Genuine slack rising on entrants; T-06 U-3 leg met |
| 4.3 | down | No band. Record |
| 4.3 | flat | No band. Record |
| 4.3 | up | No band. Record |
| ≤4.2 | down | ⚠️ NO-SIGNAL: the rate held on a shrinking denominator. Score nothing |
| ≤4.2 | flat | No band. Record |
| ≤4.2 | up | 🟡 **Absorption cell:** entrants absorbed at a flat-or-lower rate (third month running if it prints). No vector; written into CORE TENSION |

### 3c. EPOP (Oct)

| Oct EPOP | Assignment |
|---|---|
| **≥ 58.9** | **LEG B satisfied** |
| **58.7 – 58.8** | LEG B not met. No band otherwise. Record |
| **≤ 58.6** | 🔴 **T-03 + T-04 FIRE** (and T-06's EPOP leg). **LAB-18 ✅ RESOLVES**. LEG B not met |

### 3d. Freeze-thaw v2 — FULL cross-product (L-27: LEG A × LEG B × LEG C = 8 cells). Fires on `LEG A ∧ (LEG B ∨ LEG C)`

| LEG A | LEG B | LEG C (from 11/3) | Assignment |
|---|---|---|---|
| met | met | met | 🔴 **v2 FIRES** (B ∧ C) → stand down vectors 4/6/7, re-grade the book |
| met | met | lost | 🔴 **v2 FIRES** (B only) |
| met | not | met | 🔴 **v2 FIRES** (C only). Caveat on the packet: Sep JOLTS is preliminary and can revise C away after the fire |
| met | not | lost | **NOT fired.** Record LEG A met |
| not | met | met | Not fired |
| not | met | lost | Not fired |
| not | not | met | Not fired |
| not | not | lost | Not fired |

### 3e. Net revision to Aug + Sep — vector 8 restore counter (at **0 of 2** since 10/2)

| `(A' − 133) + (S' − 29)` | Assignment |
|---|---|
| **≥ 0** | v8 restore counter **0 → 1 of 2** (two consecutive prints needed). No score move |
| **< 0** | counter stays **0 of 2**. No downward band exists; none improvised |

### 3f. Sector and side lines with a registered test

| Line | Band | Assignment |
|---|---|---|
| Health care | net-negative | **T-08 FIRES** → CARL + REGINALD; **v10 1 → 4** |
| LT share | >27% AND YoY turning positive **in BLS's own text** | v6 restores 3 → 4 (both legs; a FRED-inferred YoY does not count) |
| LT share | <24% | v6 drop counter 1 of 2 (October alone cannot complete it) |
| Federal payrolls | ≤ −25K MoM | T-13 MoM side; **v12 moves only with UCFE corroboration in the same session** (BD-17) |
| AHE | any change from the published **+3.0%** YoY | 1c packet CARL + HENRY. No threshold |

### 3g. Predictions this print moves — gate #14(a): bands reproduce the headline

| Row | Headline | Branch (Oct) | P(branch) | Post-print V | `Σ P × V` |
|---|---|---|---|---|---|
| **LAB-18** | 10% | EPOP ≤58.6 | 0.053 | ✅ 1.00 | `0.053 × 1.00 = 0.053` |
| | | EPOP ≥58.7 | 0.947 | **5%** = `0.053` (one draw left, Nov) | `0.947 × 0.053 = 0.050` |
| | | | | **total** | **0.103 ≈ 10% ✅** |
| **LAB-19** | 81% | LF MoM >0 | 0.567 | ✅ 1.00 | `0.567 × 1.00 = 0.567` |
| | | LF MoM ≤0 | 0.433 | **57%** = `0.567` (needs Nov >0) | `0.433 × 0.567 = 0.246` |
| | | | | **total** | **0.813 ≈ 81% ✅** |

Per-draw rates are the registered ones (LAB-18 survival `0.85^(1/3) = 0.947`; LAB-19 `p = 0.567`). Monotone in the evidence direction ✅.

### 3h. August third-estimate watch (WQ-175 ②, carried from the 10/2 card §3g)

August first print **+162K** (ALFRED `20260904`), second **+133K** (`20261002`); third = ALFRED `20261106`. Reference: first→third mean **−33.5K**, SD **55K** (`workbook/PAYROLL_VINTAGES.tsv`, n=39). **Diagnostic only, no band:** a third estimate below **+73.5K** or above **+183.5K** is reported as >1 SD from the measured bias.

## 4. FALSIFIERS OF THIS CARD

1. No release at 08:30 on 11/6 (the CR runs to 12/11) ⇒ the card rolls to the actual date unchanged; nothing grades off ADP or private trackers.
2. A population-control or benchmark break inside the release ⇒ §3b/§3c do not grade until measured.
3. A first-print figure graded where the card specifies revised ones (Kill A, LEG A, §3e) ⇒ L-02 violation. **Revised back-months first.**
4. A relayed or summary figure ⇒ do not grade (L-33).
5. **LEG C not yet written into §2.4 at grade time** ⇒ grade LEG C from the graded JOLTS card first, then §3d.

## 5. 🔴 DECLARED GAP (carried) — there is no payrolls vector (BD-26)

A negative print moves nothing in the /75 by itself. ⛔ No vector is created on print day (L-18).

### 5a. 🔒 AMENDMENT 2026-10-28 (9 days before the print): v17 Payroll momentum CREATED (Will, BD-26 discharged) — this section supersedes §5's "no payrolls vector" from this date

**Letter (adopted 2026-10-28; base rates `domain/sources/2026-10-28_PAYROLL_VECTOR_AND_T07_BASE_RATES.md`, POST-HOC):** revised 3-month average of payroll changes `M = (A' + S' + X)/3`, where `A'` and `S'` are Aug and Sep as REVISED in this release and `X` is the October first print ⇒ **M ≥ 100K ⇒ v17 = 1 · 50K ≤ M < 100K ⇒ 2 · M < 50K ⇒ 3.** The value entering 11/6 is **2** (Jul–Sep on the 10/2 vintage: `(−10 + 133 + 29)/3 = 50.7K`).

**Pre-computed on the 10/2 vintage (`A' + S' = 133 + 29 = 162`) — RE-SOLVE on the published revisions before reading X (L-02):**

| Band | Condition on M | X bar on the 10/2 vintage | v17 |
|---|---|---|---|
| 5a-1 | M ≥ 100K | `X ≥ 300 − 162 = +138K` | **1** (2 → 1) |
| 5a-2 | 50K ≤ M < 100K | `−12K ≤ X < +138K` | **2** (holds) |
| 5a-3 | M < 50K | `X < 150 − 162 = −12K` | **3** (2 → 3) |

Partition: `M ≥ 100 / 50 ≤ M < 100 / M < 50` is a true complement on M at 1K precision. Re-solved bars are `X ≥ 300 − (A' + S')` and `X < 150 − (A' + S')`. **Mechanism vs threshold:** a band move here is a THRESHOLD read on revised data, not a recession call. In the 1950–2026 base, `M < 50K`-equivalent is followed by a recession within 12 months `12/36 = 33.3%` vs base `18.1%`, and it fired falsely in 2025-03, 2025-06 and 2026-02. **Attribution discipline:** a 5a-3 print is not attributed to demand vs supply on this card (that stays §3b/§3c). **Travels:** a v17 move goes into the STATUS matrix and the NEXUS brief; no new outbox packet (no T-number rides on v17).

## 6. WHAT TRAVELS

| Outcome | Route | Priority |
|---|---|---|
| v2 FIRES | **WALTER** → CARL, REGINALD, HENRY, NEXUS; the book is re-graded | 🔴 |
| T-03 + T-04 | **WALTER** → CARL + HENRY + REGINALD | 🔴 |
| T-06 | **WALTER** → CARL + REGINALD + HENRY (LFPR caveat where §3b says so) | 🟠 |
| T-08 | **WALTER** → CARL + REGINALD | 🟠 |
| AHE change | 1c packet CARL + HENRY | 🟡 |
| LAB resolutions · v8 counter · §3h watch | STATUS + PREDICTIONS + SCOREBOARD; brief | — |

## 7. CHECKER SCOPE AT FREEZE (BD-31)

🧾 **Checker receipt at freeze (2026-10-21 09:43 EDT, `card_partition_check.py`, rc=2):** `7 band table(s) — 1 verified, 6 unverified, 0 with defects` · `[✓] table 2: VERIFIED — axis 'October payrolls, first print', 4 bands, precision 1,000`. The rest fall under the BD-31 one-axis limit (the §1 instrument table and the §3f/§3g/§6 ledgers are counted as band tables but are not); the band tables are proved by hand below. **Freeze authorized on `0 defects` + the hand proof.**

| Table | Complement holds because |
|---|---|
| §3b | U-3 `≥5.0 / 4.4–4.9 / 4.3 / ≤4.2` and LFPR `≤61.7 / 61.8 / ≥61.9` each partition the one-decimal grid; **12 of 12** pairs written |
| §3c | `≥58.9 / 58.7–58.8 / ≤58.6` partitions the one-decimal grid |
| §3d | 2 × 2 × 2 = **8 of 8** cells written |
| §3e | `≥0 / <0` true complement |
| §5a (added 2026-10-28) | `M ≥ 100 / 50 ≤ M < 100 / M < 50` partitions M at 1K precision; re-run 10/28: `card_partition_check.py` 8 tables, 1 verified, **0 with defects**, §5a UNVERIFIED under the same BD-31 one-axis limit |

## 8. GRADE (write 2026-11-06 off this frozen card — never re-read a band)

*Blank until print. Order: ① confirm §2.4 carries the 11/3 LEG C result · ② read revised `A'`, `S'`; re-solve §2.2 and §3e before reading October · ③ grade §3a–§3f as separate letters, CES and CPS named as two witnesses · ④ apply §3g, record §3h · ⑤ write into STATUS (KEY THRESHOLDS, matrix, EXIT RULES, PREDICTIONS, calendar), `git mv` to `docket/graded/`.*
