# 🔒 FROZEN GRADING CARD — JOLTS OCTOBER 2026 (September revised) · Tue 2026-12-01, 10:00 ET

**Written:** 2026-11-25, 6 days before the release. ⚠️ **LATE against C2a:** the freeze window opened 2026-11-24 (`card_required_check.py` reported it MISSING at the 11/25 boot); no October JOLTS data exists at writing, so the lateness costs nothing on the bands. **Status: FROZEN. Grade off this card.**
**Author:** LABOR (PROME wake prome-77, D:L1221) · **Consume at:** B5b.
**Release date VERIFIED** at the BLS December 2026 release calendar (`bls.gov/schedule/2026/12_sched.htm`, fetched 2026-11-25 09:12 ET as `research-bot/1.0`, HTTP 200, sha256 `fbc2aabbec415ca7`, page last modified November 09, 2026): *"1 · Job Openings and Labor Turnover Survey · October 2026 · 10:00 AM"*.
**Why a card — multi-loaded:** the **layoffs-rate ≥1.2%** same-day trigger to CARL + REGINALD · **T-10** · **LAB-21** resolves here (September layoffs level as revised) · the v2 LEG C pair and the v4 letters as **record-only** reads since v2 fired on 11/6 · the openings level (no band, decided 10/21).

---

## 1. INSTRUMENT, SOURCE DOCUMENT, OBSERVATION BASIS (named before any value exists)

| Leg | Instrument | Source document | Observation basis |
|---|---|---|---|
| **NET** (LEG C record, v4 record) | `NET = hires − total separations`, **total nonfarm, levels in thousands, SA**, for **September (revised)** and **October (preliminary)** | BLS news release *"Job Openings and Labor Turnover — October 2026"*, 2026-12-01 10:00 ET, hires and total-separations level tables; read from the SAVED release text through `scripts/fetch_primary.py` (L-33) | Integer thousands as printed. **Never computed from rates.** Cross-check: FRED JTSHIL / JTSTSL |
| Hires rate | hires rate, total nonfarm, SA, **October** | same, hires table | one decimal as printed |
| Hires level (T-10) | hires level, SA, Sep (rev) and Oct (P) | same | thousands |
| Layoffs & discharges rate (trigger) | layoffs & discharges rate, total nonfarm, SA, **October (preliminary)** — the preliminary month only (LAB-21 notes) | same, layoffs table | one decimal as printed |
| Layoffs & discharges level, **September** (LAB-21) | level, SA, thousands, September column as carried by this release | same | thousands as printed |
| Openings (record only) | level and rate, SA, Oct | same | thousands / one decimal — **no band** |

⚠️ If the saved fetch is refused (honest name only, WQ-723 A), the reading is UNAVAILABLE from that source: grade nothing from a summary, use the BLS API or FRED for the levels and say so on the grade.

## 2. INPUTS FROZEN (current vintage: BLS 2026-11-03 release, USDL-26-1630; FRED pulled 2026-11-25 09:12 ET)

| Series | Sep 2026 (P) | Aug 2026 (rev) | Jul 2026 | Source |
|---|---|---|---|---|
| Hires | **5,402K** (rate 3.4%) | 5,271K (3.3%) | 5,146K (3.2%) | JTSHIL / JTSHIR |
| Total separations | **5,319K** | 5,175K | 5,128K | JTSTSL |
| **NET** | **`5,402 − 5,319 = +83K`** | `5,271 − 5,175 = +96K` | `5,146 − 5,128 = +18K` | computed |
| Layoffs & discharges | **1,641K / 1.0%** | 1,768K / 1.1% | 1,702K / 1.1% | JTSLDL / JTSLDR |
| Openings | 7,523K | 7,190K | 7,335K | JTSJOL |

**State going in:** v2 **FIRED 11/6** (card `docket/graded/GRADING_CARD_20261106_NFP.md` §3d row 1); LEG C met on Aug rev ∧ Sep P · v4 **stood down at the floor of 1** (WQ-634 A, Will 11/6), its letters print as **record only**, no re-arm letter exists · layoffs rate `1.2 − 1.0 = 0.2pp` below the trigger · hires `5,402 − 5,000 = 402K` above the T-10 line · LAB-21 open at 68%.
⚠️ **The pair rolls:** after this release LEG C reads **Sep (revised) ∧ Oct (preliminary)**. August drops out.

## 3. PRE-COMMITTED BANDS

### 3a. LEG C pair × v4 letters — RECORD ONLY (v2 fired; v4 at the floor)

<!-- partition-axis: column="October NET, thousands" -->
| Band | October NET, thousands | Assignment |
|---|---|---|
| **N-1** | ≤ 0 | October NET non-positive ⇒ the LEG C pair is **not met** on the rolled pair; v4's "NET ≤0 in a month" letter is **met as record** |
| **N-2** | ≥ 1 | October NET positive ⇒ §3b decides with September revised |

### 3b. The full cross-product (Sep-rev NET sign × Oct NET sign × Oct hires rate = 2 × 2 × 2 = 8 cells)

v4 letters (STATUS matrix, record only since 11/6): *"NET ≤0 in a month; NET ≤0 ×2 AND hires rate ≤3.2%."* A revised September ≤0 is "a month". The rate leg reads **October**.

| Sep (rev) NET | Oct NET | Oct hires rate | LEG C pair (record) | v4 letter (record) | Score |
|---|---|---|---|---|---|
| > 0 | > 0 | ≥ 3.3 | met | none met | **no change** |
| > 0 | > 0 | ≤ 3.2 | met | none met (rate leg acts only with NET ≤0 ×2) | **no change** |
| > 0 | ≤ 0 | ≥ 3.3 | not met | "≤0 in a month" met | **no change** |
| > 0 | ≤ 0 | ≤ 3.2 | not met | "≤0 in a month" met | **no change** |
| ≤ 0 | > 0 | ≥ 3.3 | not met | "≤0 in a month" met | **no change** |
| ≤ 0 | > 0 | ≤ 3.2 | not met | "≤0 in a month" met | **no change** |
| ≤ 0 | ≤ 0 | ≥ 3.3 | not met | "≤0 ×2" met, rate leg not | **no change** |
| ≤ 0 | ≤ 0 | ≤ 3.2 | not met | **both v4 letters met** | **no change** |

**Why every cell scores nothing:** v2 has no un-fire letter and v4/v6/v7 have no re-arm letter (STATUS EXIT RULES; WQ-634 A). A LEG C loss leaves v2 fired on row 2 (LEG A ∧ LEG B, EPOP 59.3 ≥ 58.9). None is improvised on the morning.
**Implication line (separate, gradable):** any "not met" cell ⇒ **packet to PROME the same session** naming the cell, because re-arming v4 or un-firing v2 is Will's call and the record should reach him; "met" ⇒ STATUS only.

### 3c. Layoffs & discharges rate, October (preliminary)

| Oct layoffs rate | Assignment |
|---|---|
| **≥ 1.2** | 🔴 **Firing side waking ⇒ CARL + REGINALD SAME DAY** (via WALTER, signal) |
| **≤ 1.1** | No action. Record |

### 3d. Hires level, two months (Sep rev, Oct P)

| Both months | Assignment |
|---|---|
| **both < 5,000K** | 🟠 **T-10 FIRES** → CARL + HENRY (via WALTER) |
| **both > 5,500K** | **"Thawed"** per the v4 row — record only; no score (the letter names none; L-27 absent cell, stated) |
| any other combination | No action. Record |

### 3e. LAB-21 — September layoffs level as carried by this release (the row's own GATE #15 text, copied)

| Sep L&D level, thousands | Assignment |
|---|---|
| **≥ 1,646** | **LAB-21 TRUE** (as-made 68%) |
| **1,637 – 1,645** | **NO-VERDICT** (within 5K of 1,641K) |
| **≤ 1,636** | **LAB-21 FALSE** |
| no release by 2026-12-31 | NO-VERDICT |

### 3f. Openings — record only

Level, rate and the 3-month change `Oct / Jul − 1` (Jul 7,335K on the current vintage, re-read from the release) are written beside the grade. **No band, no route** (decided 10/21, KB-LAB-218).

## 4. MECHANISM vs THRESHOLD

§3a–§3d and §3f are threshold/counter reads. **LAB-21 (§3e) is a measurement-revision call; it is the only prediction this card resolves, and it moves no letter.** JOLTS is ratio-estimated to CES, so a NET move is partly the same payroll witness the 12/4 print will show; never count JOLTS and NFP as two confirmations.

## 5. ATTRIBUTION DISCIPLINE

1. **September is revised in this release.** Grade on the revised figure; a "not met" cell caused only by the September revision is recorded as such, not narrated as new October weakness.
2. **Response-rate noise:** I will not call a NET within ±50K of zero a regime change in prose; the letter still grades it exactly.
3. **No openings-based demand narrative** (decided 10/21: no measured lead).
4. **Hiring-season mix:** October hires carry seasonal retail and courier hiring; the SA level is graded as printed and no seasonal story is attributed in either direction.

## 6. FALSIFIERS + ROUTING

**Falsifiers:** ① no release on 12/1 (the CR runs to 12/11) ⇒ the card rolls unchanged; LAB-21 stays open to 12/31 · ② a benchmark or seasonal revision inside this release ⇒ write the revised August too and grade on as-published Sep/Oct; note the break · ③ summary-sourced figures ⇒ do not grade.

| Outcome | Route | Priority |
|---|---|---|
| Layoffs ≥1.2 | **WALTER** → CARL + REGINALD same day | 🔴 |
| T-10 | **WALTER** → CARL + HENRY | 🟠 |
| Any §3b "not met" cell | STATUS EXIT RULES + NFP card + NEXUS brief; **packet to PROME** (re-arm / un-fire is Will's) | 🟡 |
| LAB-21 resolves | STATUS PREDICTIONS + `workbook/PREDICTIONS_SCOREBOARD.md` §A | — |

## 7. CHECKER SCOPE AT FREEZE (BD-31)

🧾 **Checker receipt at freeze (2026-11-25 09:13 EST, `card_partition_check.py`, rc 2):** `5 band table(s) — 1 verified, 4 unverified, 0 with defects` · `[✓] table 3: VERIFIED — axis 'October NET, thousands', 2 bands, precision 1, bounds as written`. The rest fall under the BD-31 one-axis limit and are proved by hand below. **Freeze authorized on `0 defects` + the hand proof.**

| Table | Complement holds because |
|---|---|
| §3b | 2 × 2 × 2 = **8 of 8 cells written**; NET `> 0 / ≤ 0` on the integer-thousands grid, rate `≥ 3.3 / ≤ 3.2` on the one-decimal grid |
| §3c | `≥ 1.2 / ≤ 1.1` on the one-decimal grid |
| §3d | "both <5,000 / both >5,500 / any other" is exhaustive by its third row |
| §3e | `≥ 1,646 / 1,637–1,645 / ≤ 1,636` on the integer-thousands grid, plus the no-release row — copied from LAB-21's GATE #15 text, not re-banded |

Arithmetic re-run in python at freeze: NET Sep `+83`, Aug `+96`, Jul `+18`; layoffs `1.2 − 1.0 = 0.2pp`; hires `5,402 − 5,000 = 402K`.

## 8. GRADE (write 2026-12-01 off this frozen card — never re-read a band)

*Blank until print.*
