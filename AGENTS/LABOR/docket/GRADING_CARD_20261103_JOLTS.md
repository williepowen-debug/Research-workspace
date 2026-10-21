# 🔒 FROZEN GRADING CARD — JOLTS SEPTEMBER 2026 (August revised) · Tue 2026-11-03, 10:00 ET

**Written:** 2026-10-21, 13 days before the release (C2a freeze-by 10/27). No September JOLTS data exists. **Status: FROZEN. Grade off this card.**
**Author:** LABOR (PROME-spawned session af287aee, Will-approved 09:38 ET) · **Consume at:** B5b.
**Release date VERIFIED** at the BLS November 2026 release calendar (`bls.gov/schedule/2026/11_sched.htm`, fetched 2026-10-21 09:40 ET, HTTP 200): *"3 · Job Openings and Labor Turnover Survey · September 2026 · 10:00 AM"*.
**Why a card — multi-loaded:** freeze-thaw v2 **LEG C** (the bull-side kill's flow leg) · vector 4 re-escalation letters · the **layoffs-rate ≥1.2%** same-day trigger to CARL + REGINALD · T-10 · the openings level (no band, decided 10/21). **This print lands three days BEFORE the 11/6 NFP draw of LEG A**, so its LEG C result is an input to `docket/GRADING_CARD_20261106_NFP.md`.

---

## 1. INSTRUMENT, SOURCE DOCUMENT, OBSERVATION BASIS (named before any value exists)

| Leg | Instrument | Source document | Observation basis |
|---|---|---|---|
| **NET** (LEG C, v4) | `NET = hires − total separations`, **total nonfarm, levels in thousands, seasonally adjusted**, computed for **August (revised)** and **September (preliminary)** | BLS news release *"Job Openings and Labor Turnover — September 2026"*, 2026-11-03 10:00 ET, hires and total-separations level tables; read from the SAVED release text (L-33) | Integer thousands as printed. **Never computed from rates.** Cross-check: BLS public API `JTS000000000000000HIL` / `…TSL` (identical by construction) |
| Hires rate (v4 leg) | hires rate, total nonfarm, SA, **September** | same release, hires table | one decimal as printed |
| Hires level (T-10, "thawed") | hires level, SA, Aug (rev) and Sep | same | thousands |
| Layoffs & discharges rate (trigger) | layoffs & discharges rate, total nonfarm, SA, **September (preliminary)** | same release, layoffs table | one decimal as printed |
| Openings (record only) | job openings level and rate, SA, Sep | same | thousands / one decimal — **no band** (`domain/sources/2026-10-21_C2_BASE_RATES_PREREG.md`) |

## 2. INPUTS FROZEN (current vintage: BLS 2026-09-29 release; FRED pulled 2026-10-21 09:39 ET)

| Series | Aug 2026 (P) | Jul 2026 (rev) | Source |
|---|---|---|---|
| Hires | **5,192K** (rate 3.3%) | 5,146K (3.2%) | JTSHIL / JTSHIR |
| Total separations | **5,070K** | 5,128K | JTSTSL |
| **NET** | **`5,192 − 5,070 = +122K`** | `5,146 − 5,128 = +18K` | computed |
| Layoffs & discharges | 1,641K / **1.0%** | 1,702K / 1.1% | JTSLDL / JTSLDR |
| Openings | 7,079K | 7,335K | JTSJOL |

**State going in:** LEG C **MET** (Jul +18K ∧ Aug +122K, graded 9/29) · v4 at **2** · layoffs rate `1.2 − 1.0 = 0.2pp` below the trigger · hires `5,192 − 5,000 = 192K` above the T-10 line.
⚠️ **The pair rolls:** after this release LEG C reads **Aug (revised) ∧ Sep (preliminary)**. July drops out.

## 3. PRE-COMMITTED BANDS

### 3a. September NET (preliminary), thousands

<!-- partition-axis: column="September NET, thousands" -->
| Band | September NET, thousands | Assignment |
|---|---|---|
| **N-1** | ≤ 0 | September NET non-positive → §3b decides LEG C (LOST) and v4 |
| **N-2** | ≥ 1 | September NET positive → §3b decides with August revised |

### 3b. LEG C × vector 4 — the FULL cross-product (L-27: Aug-rev NET sign × Sep NET sign × Sep hires rate = 2 × 2 × 2 = 8 cells)

v4 letter (STATUS matrix): *"→ 3 on NET ≤0 in a month; → 4 on NET ≤0 ×2 AND hires rate ≤3.2%."* A revised August ≤0 is "a month" under that letter. The hires-rate leg reads **September**.

| Aug (rev) NET | Sep NET | Sep hires rate | LEG C | v4 |
|---|---|---|---|---|
| > 0 | > 0 | ≥ 3.3 | **STAYS MET** | holds 2 |
| > 0 | > 0 | ≤ 3.2 | **STAYS MET** | holds 2 (the rate leg acts only with NET ≤0 ×2) |
| > 0 | ≤ 0 | ≥ 3.3 | **LOST** | **2 → 3** |
| > 0 | ≤ 0 | ≤ 3.2 | **LOST** | **2 → 3** (one month only) |
| ≤ 0 | > 0 | ≥ 3.3 | **LOST** | **2 → 3** |
| ≤ 0 | > 0 | ≤ 3.2 | **LOST** | **2 → 3** |
| ≤ 0 | ≤ 0 | ≥ 3.3 | **LOST** | **2 → 3** (×2 met, rate leg not) |
| ≤ 0 | ≤ 0 | ≤ 3.2 | **LOST** | **2 → 4** |

**Implication line (separate, gradable):** LEG C LOST ⇒ on 11/6 freeze-thaw v2 can fire only as **LEG A ∧ LEG B** (EPOP ≥ the July referent). LEG C MET ⇒ LEG A alone fires v2 on 11/6. **Write which one into the NFP card's §2 before 11/6.**
Score effect: v4 2 → 3 = +1 (26 → 27/75); 2 → 4 = +2 (→ 28/75), on the 10/21 total.

### 3c. Layoffs & discharges rate, September (preliminary)

| Sep layoffs rate | Assignment |
|---|---|
| **≥ 1.2** | 🔴 **Firing side waking ⇒ CARL + REGINALD SAME DAY** (via WALTER, signal) |
| **≤ 1.1** | No action. Record |

### 3d. Hires level, two months (Aug rev, Sep P)

| Both months | Assignment |
|---|---|
| **both < 5,000K** | 🟠 **T-10 FIRES** → CARL + HENRY (via WALTER) |
| **both > 5,500K** | **"Thawed"** per the v4 row. ⚠️ The letter names no score for it: record only; no score improvised (L-27 absent cell, stated) |
| any other combination | No action. Record |

### 3e. Openings — record only

Level, rate and the 3-month change `Sep / Jun − 1` (Jun 7,182K on the current vintage, re-read from the release) are written beside the grade. **No band, no route** (decided 10/21, KB-LAB-218).

## 4. MECHANISM vs THRESHOLD

All letters are threshold/counter reads. **No prediction is registered or resolved.** JOLTS is ratio-estimated to CES, so a NET move is partly the same payroll witness the 11/6 print will show; say so on any v4 move, and never count JOLTS and NFP as two confirmations.

## 5. ATTRIBUTION DISCIPLINE

1. **August is revised in this release.** Grade on the revised figure; the 9/29 preliminary is history. A LEG C loss caused only by the August revision is recorded as such, not narrated as new September weakness.
2. **Response-rate noise:** JOLTS preliminary months revise by tens of thousands. I will not call a NET within ±50K of zero a regime change in prose; the letter still grades it exactly.
3. **No openings-based demand narrative** (decided 10/21: no measured lead).

## 6. FALSIFIERS + ROUTING

**Falsifiers:** ① no release on 11/3 (the CR runs to 12/11) ⇒ the card rolls unchanged · ② JOLTS annual benchmark/seasonal revision inside this release ⇒ write the revised July too and grade on as-published Aug/Sep; note the break · ③ summary-sourced figures ⇒ do not grade.

| Outcome | Route | Priority |
|---|---|---|
| Layoffs ≥1.2 | **WALTER** → CARL + REGINALD same day | 🔴 |
| T-10 | **WALTER** → CARL + HENRY | 🟠 |
| LEG C LOST | STATUS EXIT RULES + NFP card §2 + NEXUS brief; direct note to HENRY + REGINALD (the v2 consumers) | 🟡 |
| v4 moves | STATUS score + brief | — |

## 7. CHECKER SCOPE AT FREEZE (BD-31)

🧾 **Checker receipt at freeze (2026-10-21 09:42 EDT, `card_partition_check.py`, rc=2):** `4 band table(s) — 1 verified, 3 unverified, 0 with defects` · `[✓] table 3: VERIFIED — axis 'September NET, thousands', 2 bands, precision 1`. The rest fall under the BD-31 one-axis limit and are proved by hand below. **Freeze authorized on `0 defects` + the hand proof.**

| Table | Complement holds because |
|---|---|
| §3a | `≤ 0 / ≥ 1` on BLS's integer-thousands grid |
| §3b | 2 × 2 × 2 = **8 of 8 cells written** |
| §3c | `≥1.2 / ≤1.1` on the one-decimal grid |
| §3d | "both <5,000 / both >5,500 / any other" is exhaustive by its third row |

## 8. GRADE (write 2026-11-03 off this frozen card — never re-read a band)

*Blank until release. Order: ① save + extract the release; check the reference-month line · ② read August REVISED first, then September · ③ compute both NETs from printed levels (division-free, subtraction written) · ④ grade §3a–§3d as separate letters; record §3e · ⑤ write LEG C's state into the NFP card §2 and STATUS EXIT RULES, then `git mv` this card to `docket/graded/`.*
