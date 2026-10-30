# 🔒 FROZEN GRADING CARD — EMPLOYMENT COST INDEX, Q3 2026 (September reference) · Fri 2026-10-30, 08:30 ET

**Written:** 2026-10-21, 9 days before the release (C2a target ~10/23). No Q3 ECI data exists. **Status: FROZEN. Grade off this card.**
**Author:** LABOR (PROME-spawned session af287aee, Will-approved 09:38 ET) · **Consume at:** B5b.
**Release date VERIFIED** at the BLS ECI schedule page (`bls.gov/schedule/news_release/eci.htm`, fetched 2026-10-21 09:02 ET, HTTP 200): *"Third Quarter 2026 · Oct. 30, 2026 · 08:30 AM"*. Next: Q4 2026 on Jan 29, 2027.
**Why a card:** quarterly composition gauge (C2a), and the **last print on the current weighting basis before the December re-weighting** (CLAUDE.md C2a). Two registered letters ride it: **(1)** the ECI level band (STATUS § KEY THRESHOLDS) · **(2)** the AHE↔ECI wedge letter (`docket/CATALYSTS.tsv` 10/30 row).

---

## 1. INSTRUMENT, SOURCE DOCUMENT, OBSERVATION BASIS (named before any value exists)

| Leg | Instrument (the exact series) | Source document | Observation basis |
|---|---|---|---|
| **E1 — level** | ECI **civilian workers, total compensation, 12-month percent change** | BLS news release *"Employment Cost Index — September 2026"*, 2026-10-30 08:30 ET, **Table A**, read from the SAVED release text (L-33), never a summary | **Not seasonally adjusted 12-month change**, one decimal as published; September 2026 vs September 2025 |
| **E2 — wedge** | `w = AHE_YoY(Sep) − ECI_PW` | AHE: BLS *Employment Situation — September 2026* (USDL-26-1549, 2026-10-02), **frozen below**. ECI_PW: same 10/30 release, Table A | ECI_PW = **private industry workers, wages and salaries, 12-month percent change, NSA**, one decimal. AHE = all private employees, YoY, one decimal as BLS printed it |
| E3 — direction (feeds E2's implication line only) | `ECI_PW(Q3) − ECI_PW(Q2)` | same | one-decimal difference |

⛔ Graded only on the one-decimal figures BLS prints. If the release prints a different decimal for the same series in text and table, **the table governs**.

## 2. INPUTS FROZEN (current vintage)

| Series | Value | Source |
|---|---|---|
| ECI civilian total comp, 12-mo | **3.4%** (Q2 2026; Q1 3.4; Q2 2025 3.6) | BLS USDL-26-1270 (2026-07-31), Table A — STATUS_DETAIL § Signal Dashboard |
| ECI private wages & salaries, 12-mo (`ECI_PW` Q2) | **3.1%** (Q1 3.4) | USDL-26-1270 |
| AHE all private, YoY, **September** (`AHE_Sep`) | **+3.0%** ($37.81) | USDL-26-1549 (2026-10-02). **Frozen at this vintage:** the next revision of September AHE lands 11/6, after this grade, so it cannot move the wedge |
| June wedge, for reference | `3.5 − 3.1 = 0.4pp` (AHE Jun 3.5%) | 7/31 grade, re-stated 8/7 |

## 3. PRE-COMMITTED BANDS

### 3a. E1 — civilian compensation, 12-month (`C`)

<!-- partition-axis: column="Civilian compensation 12-month change" -->
| Band | Civilian compensation 12-month change | Assignment |
|---|---|---|
| **E1-a** | ≥ 3.6 | **WAGE-PRESSURE PREMISE REAL** — the supply-artifact framing weakens. 1c packet CARL + HENRY. Write into CORE TENSION (DETAIL) and FED TRAP: labour is no longer a satisfied side-constraint *on this gauge* |
| **E1-b** | 3.5 – 3.5 | **INDETERMINATE.** Record. No packet |
| **E1-c** | ≤ 3.4 | **No pressure on the composition-controlled gauge.** Whether the COMPOSITION branch fires is decided by §3b (the letter's "while AHE accelerates" clause), not by this band alone |

### 3b. The registered COMPOSITION letter is a CONJUNCTION — full cross-product (L-27: E1 state × AHE direction)

The STATUS letter reads *"≤3.4% flat-or-down **while AHE accelerates** = COMPOSITION."* AHE direction for Q3 is **already known and frozen**: September YoY **3.0%** vs June **3.5%** ⇒ **AHE DECELERATED** (−0.5pp). Every cell is written; the AHE-accelerating column is unreachable this quarter and says so.

| E1 band | AHE accelerating (unreachable: AHE fell 3.5 → 3.0) | AHE decelerating (the live column) |
|---|---|---|
| E1-a ≥3.6 | — unreachable | **PRESSURE REAL** (as §3a) — with AHE falling, the gauges disagree in the opposite direction from Q2; record that explicitly |
| E1-b 3.5 | — unreachable | INDETERMINATE |
| E1-c ≤3.4 | — unreachable | ⚠️ **COMPOSITION branch does NOT fire** — its "while AHE accelerates" leg is false. **No band for this cell by letter** (this is the absent cell, now named): record "both gauges soft; no mix wedge to explain" |

### 3c. E2 — wedge `w = 3.0 − ECI_PW` (AHE side frozen at 3.0)

<!-- the checker's single axis is §3a; this table is proved by hand in §7 -->
| Wedge `w` (pp) | Equivalent `ECI_PW` | Assignment (CATALYSTS letter) |
|---|---|---|
| `w ≥ 0.4` | `ECI_PW ≤ 2.6` | **WEDGE PERSISTS/WIDENS** — composition read CONFIRMED a 2nd quarter; AHE stays demoted as a wage-pressure gauge |
| `0.1 ≤ w ≤ 0.3` | `2.7 ≤ ECI_PW ≤ 2.9` | **NARROWING — no band** (the letter names only persist/widen and close). Record |
| `w ≤ 0.0` | `ECI_PW ≥ 3.0` | **WEDGE CLOSES** → read §3d for WHICH side closed it |

### 3d. IMPLICATION LINE for a closed wedge (card-design rule (b): the consequence is gradable separately from the branch)

| E3: `ECI_PW(Q3) − 3.1` | Implication when §3c = CLOSES |
|---|---|
| `≥ +0.1` (ECI re-accelerated) | **"The Q2 print was noise/base-effect; the supply-shrink framing must be RE-OPENED"** (the CATALYSTS letter's consequence) — write the re-open into CORE TENSION; 1c packet CARL + HENRY |
| `≤ 0.0` (ECI flat or down) | **Closed from the AHE side** — AHE fell to meet the composition-controlled gauge. **The re-open consequence does NOT apply**; the composition read is not refuted. Record only |

⚠️ Stated now so it is not discovered on the day: because AHE is frozen at 3.0, **any `ECI_PW` from 3.0 to 3.1 closes the wedge with ECI flat or down** (row 2 of §3d). Only `ECI_PW ≥ 3.2` triggers the re-open.

## 4. MECHANISM vs THRESHOLD

- E1 and E2 are **threshold/level reads**. The mechanism question, whether wage growth is supply-driven (immigration shrink) or demand-driven, is **not** graded by a single ECI print. **No prediction is registered or resolved on this card.**
- **Real wages** (ECI_PW minus CPI-U 12-mo) are recorded **with no band**. The real-income read is CARL's.

## 5. ATTRIBUTION DISCIPLINE (what I will NOT attribute)

1. **Health-benefit costs.** Benefits ran 3.8% (Q2) on health 6.0%. A total-comp rise carried by benefits is **not** wage pressure. Record the wages-vs-benefits split beside E1; **E1's band does not change** on it.
2. **The December re-weighting** has not happened yet; this print is on the current basis. Nothing in this grade is attributed to it.
3. **No Fed-path inference.** The rate path is BOND/HENRY/ORACLE's (STATUS § FED TRAP).

## 6. FALSIFIERS OF THIS CARD + ROUTING

**Falsifiers:** ① BLS does not publish on 10/30 (CR runs to 12/11, so not expected) ⇒ the card rolls to the actual date unchanged. ② BLS changes the series definition or weights in this release ⇒ E1/E2 do not grade until the break is measured. ③ A figure read from a summary instead of the saved release ⇒ do not grade.

| Outcome | Route | Priority |
|---|---|---|
| E1-a (≥3.6) | 1c packet CARL + HENRY direct; NEXUS brief | 🟠 |
| §3d re-open | 1c packet CARL + HENRY; CORE TENSION rewritten | 🟠 |
| Everything else | STATUS (KEY THRESHOLDS ECI row) + brief | — |

## 7. CHECKER SCOPE AT FREEZE (BD-31)

🧾 **Checker receipt at freeze (2026-10-21 09:41 EDT, `card_partition_check.py`, rc=2):** `5 band table(s) — 1 verified, 4 unverified, 0 with defects` · `[✓] table 3: VERIFIED — axis 'Civilian compensation 12-month change', 3 bands, precision 0.1`. The other four are `[BAD-DECLARATION]` under the BD-31 one-axis limit; one is §2's inputs table read as a band table, and the rest are proved by hand below. **Freeze authorized on `0 defects` + the hand proof.**

| Table | Complement holds because |
|---|---|
| §3a E1 | `≥3.6 / 3.5 / ≤3.4` partitions BLS's one-decimal grid |
| §3b | 3 E1 states × 2 AHE states = **6 of 6 cells written**; one column declared unreachable with its reason |
| §3c wedge | `w ≥ 0.4 / 0.1–0.3 / ≤ 0.0` partitions the one-decimal grid (`w` is a difference of two one-decimal figures, so it is itself on that grid) |
| §3d | `≥ +0.1 / ≤ 0.0` on the one-decimal grid |

## 8. GRADE (write 2026-10-30 off this frozen card — never re-read a band)

*Order followed: ① save + text-extract the release; check the reference-period line · ② read C and ECI_PW from Table A · ③ grade §3a, read §3b's cell, grade §3c, then §3d if closed · ④ write into STATUS (ECI row, CORE TENSION pointer), `git mv` to `docket/graded/`.*

**GRADED 2026-10-30 09:08 EDT (`date` at the card write) by LABOR (PROME-spawned, DOCKET L764). No band was re-read or moved; every figure below is the one-decimal figure BLS printed.**

**① Source (L-33).** BLS news release **USDL-26-1620**, *"Employment Cost Index — September 2026"*, embargoed until **8:30 a.m. ET Friday, October 30, 2026** — fetched 09:06 EDT from `bls.gov/news.release/eci.nr0.htm` by `scripts/fetch_primary.py` (bare curl HTTP 403 rejected; research-bot UA HTTP 200, 66,235 B html, sha256 prefix `abdc9dde713a8cea`); tag-stripped text saved at `domain/sources/2026-10-30_USDL-26-1620_eci_sep2026.txt`. Re-read with `--file … --expect` on the release number and both narrative sentences: **3 of 3 FOUND, rc 0**. Reference period: *"12-month period ending in September 2026"* ✓ (observation September 2026 vs September 2025, NSA).

**② Table A (12-month, NSA, current dollar — Sep 2025 · Jun 2026 · Sep 2026):**

| Series | Sep 2025 | Jun 2026 | **Sep 2026** | Text agrees? |
|---|---|---|---|---|
| Civilian compensation (`C`, E1) | 3.5 | 3.4 | **3.4** | ✓ "increased 3.4 percent, not seasonally adjusted" |
| Civilian wages and salaries | 3.5 | 3.2 | 3.1 | ✓ |
| Civilian benefits | 3.5 | 3.8 | 3.9 | ✓ |
| Private wages and salaries (`ECI_PW`, E2/E3) | 3.6 | 3.1 | **3.1** | ✓ "Wages and salaries increased 3.1 percent" (private paragraph) |
| Private compensation | 3.5 | 3.3 | 3.4 | ✓ |
| Private benefits / health benefits | 3.5 / 6.1 | 3.8 / 6.0 | 3.9 / **6.4** | ✓ (benefits); health from Table A only |
| Private wages, constant dollar | — | −0.4 | **−0.6** | ✓ "decreased 0.6 percent" |

Frozen inputs check: Jun 2026 civilian comp 3.4 and private wages 3.1 in today's Table A = the §2 frozen values (no revision).

**③ Grades.**

| Step | Arithmetic | Result |
|---|---|---|
| §3a E1 | `C = 3.4` ⇒ `3.4 ≤ 3.4` | **E1-c — no pressure on the composition-controlled gauge** |
| §3b cell | E1-c × AHE decelerating (frozen 3.5 → 3.0) | **COMPOSITION branch does NOT fire** (its "while AHE accelerates" leg is false). No band by letter — recorded: **"both gauges soft; no mix wedge to explain."** |
| §3c E2 | `w = 3.0 − 3.1 = −0.1` ⇒ `w ≤ 0.0` | **WEDGE CLOSES** |
| §3d E3 | `3.1 − 3.1 = 0.0` ⇒ `≤ 0.0` | **Closed from the AHE side** — AHE fell to meet the composition-controlled gauge. **The re-open consequence does NOT apply; the composition read is not refuted.** Record only |

**④ Records, no-band lines, attribution (§4–§5).**
- **No prediction registered or resolved** on this card (§4). LAB-xx book unchanged.
- **Real wages (no band, CARL's read):** private wages 3.1 against CPI-U 3.7% y/y (Sep; STATUS AHE row, BLS 10/14) ⇒ `3.1 − 3.7 = −0.6`, which equals BLS's own constant-dollar figure (−0.6, from −0.4 in June).
- **Wages-vs-benefits split (§5.1):** total civilian comp held 3.4 with benefits 3.9 over wages 3.1; private health benefits **6.4%** (Jun 6.0). Benefit costs, not wages, hold total compensation up. E1's band does not change on it.
- **Re-weighting (§5.2 / falsifier ②):** the release's own notice says updated fixed weights and the removal of workers' compensation begin **with December 2026 data** (Jan 29, 2027 release). This print is on the current basis ⇒ falsifier ② NOT triggered; E1/E2 grade.
- **Quarterly (3-month SA) context, no band:** civilian comp 0.9 → 0.8, civilian wages 0.9 → 0.7, private wages 0.9 → 0.8. Union private wages 4.3% y/y vs nonunion 3.0%.
- **No Fed-path inference (§5.3).** Rate path is BOND/HENRY/ORACLE's.

**⑤ Routing (§6):** outcome is "everything else" ⇒ STATUS (KEY THRESHOLDS ECI row) + NEXUS brief. **No 1c packet** (neither E1-a nor the §3d re-open fired). Card moved to `docket/graded/` this session.
