# 🔒 FROZEN GRADING CARD — CHALLENGER JOB-CUT REPORT, NOVEMBER 2026 · Thu 2026-12-03, 05:30 ET

**Written:** 2026-11-26, 7 days before the release (C2a freeze-by 11/26; owed under PROME D:L1273). No November data exists. **Status: FROZEN. Grade off this card.**
**Author:** LABOR (Claude Code, Opus 5.5, Will's window; task from PROME prome-80) · **Consume at:** B5b.
**Release date:** confirmed at Challenger's 2026 release calendar, fetched 2026-11-05 (`docket/CATALYSTS.tsv` row): *"Thursday, December 3, 2026 · November · 5:30 AM EST"*. Not re-fetched today.
**Why a card — four live tests ride it:** vector 2 re-spike counter · T-09 (AI share >40% ×2) · **vector 5 demote conjunction** (AI share <20% ×2 **and** tech YTD growth <+20%) · **LAB-20** (55%, resolves on this report).
**Carried design rule:** the 10/1 card's **Amendment 1**: grade on EXACT ratios computed from printed integers; round for display only.

---

## 1. INSTRUMENT, SOURCE DOCUMENT, OBSERVATION BASIS (named before any value exists)

| Leg | Instrument | Source document | Observation basis |
|---|---|---|---|
| `X` (v2) | announced US job cuts, **November 2026** | Challenger, Gray & Christmas *"November 2026 Challenger Report"*, PDF at `challengergray.com/wp-content/uploads/2026/12/`, read through `scripts/fetch_primary.py URL --expect <fig>` (saved, text-extracted, date lines checked, each figure FOUND; L-33) | integer count as printed |
| `s` (v5 share, T-09) | `s = AI-cited cuts (November) / X` | same PDF, reasons table | exact ratio from two printed integers; never a printed percentage |
| `g` (v5 tech, LAB-20) | `g = Tech YTD₂₀₂₆ / Tech YTD₂₀₂₅ − 1`, both **through November** | same PDF, industry table | exact ratio from the two printed LEVELS. **If the report prints no levels, `g` is UNGRADED**, never graded off a rounded percentage |

⛔ A refusal of the client string `research-bot/1.0` is final (WQ-723 A, WQ-735): the reading is UNAVAILABLE, named to PROME, nothing graded off a summary or a relay.

## 2. INPUTS FROZEN (October report, Challenger PDF released 2026-11-05, text-extracted; KB-LAB-232; graded card `docket/graded/GRADING_CARD_20261105_Challenger.md` §8)

| Series | October 2026 |
|---|---|
| Announced cuts | **43,994** (Sep 43,281) |
| AI-cited cuts / share | 1,265 ⇒ `1,265 / 43,994 = 0.02875`; AI YTD 121,401 |
| Tech cuts YTD, 2026 vs 2025 (through Oct) | **171,501 vs 141,159** ⇒ `171,501 / 141,159 − 1 = 0.2149` |
| Tech cuts, November 2025 (base month added this report) | **12,377** (Challenger report of 2025-12-04, as recorded on LAB-20) ⇒ 2025 base through Nov `141,159 + 12,377 = 153,536` |

**Counters going in:** v2 re-spike **0 of 2** · T-09 **0 of 2** · v5 share leg **2 of 2 MET** (Sep 0.0915, Oct 0.02875) · v5 tech leg **NOT met** (0.2149) ⇒ v5 at **4** · score **22/80**.
⚠️ **Share-leg rule, stated before the print:** "share <20% ×2" reads the two most recent months, so November's share pairs with October's (0.02875). A November `s < 0.20` keeps the leg at 2 of 2 MET; `s ≥ 0.20` resets it to 0 of 2.
**The tech-leg condition (arithmetic, not a forecast; illustration on the printed levels):** `g < 0.20` needs `(171,501 + T) / 153,536 < 1.2` ⇔ `T < 1.2 × 153,536 − 171,501 = 184,243.2 − 171,501 = 12,742.2`, where `T` is November 2026 tech cuts. **Grade on the levels this report prints, not on this illustration** (Challenger can revise either year's base). Jul to Oct monthly tech cuts were 9,867 · 6,103 · 10,799 · 5,576, all under 12,742. The probability is LAB-20's (55%); I add none here.

## 3. PRE-COMMITTED BANDS

### 3a. Announced job cuts, November (`X`)

<!-- partition-axis: column="Announced job cuts, November" -->
| Band | Announced job cuts, November | Assignment |
|---|---|---|
| **3a-1** | ≤ 80,000 | v2 re-spike counter **stays 0 of 2**. No action |
| **3a-2** | ≥ 80,001 | v2 counter **1 of 2** — no score move (restore to 4 needs December too). Record |

### 3b. AI share, exact (`s`)

| Band | AI share, exact | Assignment |
|---|---|---|
| **3b-1** | `s < 0.20` | v5 share leg **stays 2 of 2 MET** (Oct + Nov) → §3d. T-09 0 of 2 |
| **3b-2** | `0.20 ≤ s ≤ 0.40` | v5 share leg **resets 0 of 2**. T-09 0 of 2 |
| **3b-3** | `s > 0.40` | **T-09 counter 1 of 2** (fires only if December is also >40%). v5 share leg resets 0 of 2 |

### 3c. Tech YTD growth, exact (`g`) — v5 tech leg

| Band | Tech YTD growth, exact | Assignment |
|---|---|---|
| **3c-1** | `g < 0.20` | v5 tech leg **MET** |
| **3c-2** | `g ≥ 0.20` | v5 tech leg not met |
| **3c-U** | levels not printed | **UNGRADED** — v5 cannot demote this month (a conjunction with an unknown leg is not met) |

### 3d. Vector 5 demote — FULL cross-product (L-27: 2 share states × 3 tech states = 6 cells)

| Share leg | Tech leg | Assignment |
|---|---|---|
| MET (3b-1) | MET (3c-1) | 🟠 **v5 DEMOTES 4 → 2** (score −2 on the then-current total; 22 → 20/80 if nothing else moved). Direct packet CARL + HENRY; NEXUS brief |
| MET (3b-1) | not met (3c-2) | **v5 HOLDS at 4** — conjunction not relaxed |
| MET (3b-1) | UNGRADED (3c-U) | **v5 HOLDS at 4**; record that the tech leg could not be computed |
| reset (3b-2/3b-3) | MET (3c-1) | **v5 HOLDS at 4**; share leg restarts |
| reset (3b-2/3b-3) | not met (3c-2) | **v5 HOLDS at 4** |
| reset (3b-2/3b-3) | UNGRADED (3c-U) | **v5 HOLDS at 4** |

### 3e. LAB-20 resolution (its own registered letter, 2026-11-05; separate from §3c)

| Band | Tech YTD growth, exact | LAB-20 |
|---|---|---|
| **3e-1** | `g < 0.199` | ✅ **TRUE** — Brier `(1 − 0.55)² = 0.2025` |
| **3e-2** | `0.199 ≤ g < 0.201` | **NO-VERDICT** (about ±190 cuts) |
| **3e-3** | `g ≥ 0.201` | ❌ **FALSE** — Brier `0.55² = 0.3025` |
| **3e-U** | levels not printed | **NO-VERDICT** |

⚠️ **§3c and §3e differ at the edge by design:** `0.199 ≤ g < 0.20` is v5 tech leg MET with LAB-20 NO-VERDICT; `0.20 ≤ g < 0.201` is v5 tech leg not met with LAB-20 NO-VERDICT. Each letter is applied as written; neither borrows the other's edge.
**Gate #14(a), the bands reproduce the headline:** post-print value is 1.00 on 3e-1 and 0 on 3e-3; NO-VERDICT voids the row. `Σ P × V = P(3e-1) = 0.55` ✅. **A TRUE does not itself demote v5** (LAB-20 notes); §3d decides that.

## 4. MECHANISM vs THRESHOLD

All four tests are counter or threshold mechanics on what employers **say**. The AI share is a **labelling statistic**: no share move is read as a change in displacement, in either direction. A v5 demote means the *announcement* signal faded, not that AI displacement ended. Announced cuts are intentions, not realized separations (gate #9); realization is claims and JOLTS layoffs.

## 5. ATTRIBUTION DISCIPLINE

1. **Single large announcements** can carry a band alone (Kroger corporate cuts toward 3,000, title only, KB-LAB-278; Qualcomm, Block and Google headlines in the window, sizes unread). Record the largest named contributor beside the grade; **do not re-band ex-that-firm.**
2. **Voluntary exit programs** (Microsoft's offers to 60,000): Challenger books them on acceptances or a stated target. If one enters November, record it; **do not re-band without it.**
3. **H-1B order (signed 2026-09-18):** no attribution of any share or tech move to it, in either direction.
4. **Hiring plans: no band.** Record only.

## 6. FALSIFIERS + ROUTING

**Falsifiers:** ① no release on 12/3 ⇒ card rolls unchanged · ② Challenger revises the 2025 tech base ⇒ grade `g` on the levels THIS report prints · ③ summary-sourced or relayed figures ⇒ do not grade · ④ client string refused ⇒ UNAVAILABLE, named to PROME.

| Outcome | Route | Priority |
|---|---|---|
| v5 demote (§3d cell 1) | STATUS + score; direct packet CARL + HENRY; NEXUS brief; TERRY one line (tradeability) | 🟠 |
| LAB-20 resolves (3e-1, 3e-3) | PREDICTIONS.tsv + SCOREBOARD §A; STATUS | — |
| Counter moves (3a-2, 3b-3) | STATUS matrix + brief only — counters are not signals | — |
| Everything else | STATUS only; `combo:ai-restructuring` (KB-LAB-271) and `combo:corporate-cuts` (KB-LAB-278) updated, scores nothing | — |

## 7. CHECKER SCOPE AT FREEZE (BD-31)

🧾 **Checker receipt at freeze (2026-11-26 11:44 EST, `card_partition_check.py`, rc=2):** `5 band table(s) — 1 verified, 4 unverified, 0 with defects` · `[✓] table 3: VERIFIED — axis 'Announced job cuts, November', 2 bands, precision 1`. The rest fall under the BD-31 one-axis limit (the §2 input table is counted as a band table but is not); the band tables are proved by hand below. **Freeze authorized on `0 defects` + the hand proof.**

| Table | Complement holds because |
|---|---|
| §3a | `≤ 80,000 / ≥ 80,001` — integer counts, true complement |
| §3b | `s < 0.20 / 0.20 ≤ s ≤ 0.40 / s > 0.40` covers the real line with no gap or overlap |
| §3c | `g < 0.20 / g ≥ 0.20` covers the real line; `3c-U` is the no-data state, disjoint by definition |
| §3d | 2 × 3 = **6 of 6 cells written** |
| §3e | `g < 0.199 / 0.199 ≤ g < 0.201 / g ≥ 0.201` covers the real line; `3e-U` is the no-data state |

## 8. GRADE (write 2026-12-03 off this frozen card — never re-read a band)

*Blank until print. Order: ① source through `fetch_primary.py`, figures FOUND · ② compute `X`, `s`, `g` exactly, with a no-free-parameter cross-check (printed November tech figure = YTD₂₀₂₆ − 171,501 if the base is unrevised) · ③ letters §3a–§3e · ④ STATUS, PREDICTIONS, SCOREBOARD, KB, combo themes · ⑤ `git mv` to `docket/graded/`.*
