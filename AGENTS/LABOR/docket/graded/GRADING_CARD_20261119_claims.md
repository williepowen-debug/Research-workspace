# 🔒 FROZEN GRADING CARD — Initial Claims w/e Nov 14, 2026

**Print:** Thu **2026-11-19, 08:30 ET** — initial claims w/e **Nov 14** (+ continuing claims w/e **Nov 7**). Date modeled from the weekly Thursday schedule (INFERRED, not checked at DOL). ⚠️ The **following** week's release falls in Thanksgiving week (Thu 11/26) and is normally moved earlier; that is the 11/26-week card's problem, not this one's.
**Frozen:** 2026-11-12 (stamp on the commit), **in the session that graded the 11/12 card** (C2a recurring-print trigger) — **7 days ahead of the print.** PROME wake prome-e8, WQ-184 C6.
**Built from:** `docket/TEMPLATE_claims_card.md` + the 11/12 card (now `docket/graded/GRADING_CARD_20261112_claims.md`). **§1 · §3 · §5a · §5d REGENERATED from the 11/12 as-published window; §5b/§5c counts regenerated; §4 WARN line regenerated; §2 · §6 · §7 bands carried (no STATUS band changed on 11/12).**
**Why a card is owed:** multi-loaded — **T-01, T-02, vector 13 (band C re-escalation + R13-c return), Kill B**, plus CARL's kill-rule leg 1.

> 🔴 **On this print the score-moving axes are §2 bands C/D/E, §5a T-01 and §5d R13-c** (higher v13 assignment governs; R13-c never lowers a score). §5b and §5c are **record-only**; v7 has **no** return letter (decided 10/21).
> ⚠️ **`R` is 195,000** (w/e Oct 17). The retained trio is `195,000 + 191,000 + 200,000 = 586,000`, so a 200,000 repeat moves the MA **+1,250**; the zero-change print is 195,000.

---

## §1 — INPUTS FROZEN AT CURRENT VINTAGE *(REGENERATED from the DOL release of 2026-11-12 08:30 ET — AS-PUBLISHED vintage; KB-LAB-267)*

| Series | Value | Obs week | Source |
|---|---|---|---|
| Initial claims, latest (`W4`) | **200,000** | w/e 2026-11-07 | DOL/ETA advance release 2026-11-12 [CONF] (PDF text-extracted, sha256 `28b7ce89fb1b954a`); FRED ICSA agrees |
| 4-week window `W1/W2/W3/W4` | **195,000 / 195,000 / 191,000 / 200,000** | w/e Oct 17 · Oct 24 · Oct 31 · Nov 7 | DOL 2026-11-12 (Oct 31 revised 189,000 → 191,000); FRED ICSA agrees |
| 4-week MA (`MA_cur`) | **195,250** | w/e 2026-11-07 | DOL 2026-11-12; FRED IC4WSA agrees |
| Continuing claims (`CC_cur`) | **1,697,000** | w/e 2026-10-31 | DOL 2026-11-12; FRED CCSA agrees |
| Kill B (`n_kb`) | **0 of 5** | — | STATUS |
| v13 `<200,000` run (record-only) | **0** — ended at 3 on 11/12 (200,000 is not `<200,000`) · v13 at floor 1 | — | graded 11/12 |
| v7 CC `<1,750,000` run (record-only) | **9** (Sep 5 through Oct 31) — v7 at floor 1 | — | graded 11/12 |

**Reconciliation (division written):** `(195,000 + 195,000 + 191,000 + 200,000) / 4 = 781,000 / 4 = 195,250` ✅ **equals the published MA exactly.**
**Vintage note:** the 11/12 print revised w/e Oct 31 189,000 → **191,000** (initial) and w/e Oct 24 CC 1,718,000 → **1,717,000**. Expect `W4` (200,000) to revise at the 11/19 print.

---

## §2 — PRE-COMMITTED BANDS *(carried verbatim — no STATUS band changed on 11/12)*

<!-- partition-axis: column="Initial claims, single print" -->
| Band | Initial claims, single print | Pre-committed assignment |
|---|---|---|
| **A** | ≤ 185,000 | **Kill B leg** — count 0 → 1 of 5 |
| **B** | 186,000 – 229,000 | **NO ACTION** (drift band, `<230,000`) |
| **C** | 230,000 – 250,000 | **Accelerating** — vector 13: 1 → **3** (KEY THRESHOLDS letter "230–250K accelerating (v13 → 3)") |
| **D** | 251,000 – 300,000 | **ARM T-01 provisional** (confirm on a 2nd consecutive `>250,000`) |
| **E** | ≥ 301,000 | 🔴 **T-02 FIRE** → REGINALD (all ORANGE→RED) + HENRY |

**Distances from the 200,000 base:** T-01 `250,000 − 195,250 = 54,750` on the MA basis; T-02 `300,000 − 200,000 = 100,000` to the bar; the first firing print (band E, 301,000) is `101,000` away; band C's floor is `230,000 − 200,000 = 30,000` away; Kill B's edge is `200,000 − 185,000 = 15,000` below. Band B is modal.

---

## §3 — 🔴 THE MECHANICAL-DECLINE TRAP, PRE-COMPUTED *(REGENERATED)*

Rolling off: **w/e Oct 17 = 195,000** (`R = 195,000`).

`MA_next(X) = (195,000 + 191,000 + 200,000 + X)/4 = (586,000 + X)/4` ⚠️ **[VINTAGE-DEPENDENT — moves if ANY retained week revises]**
**`ΔMA(X) = (586,000 + X)/4 − 781,000/4 = (X − 195,000)/4`** ✅ **[depends only on `R`]**

`R = 195,000` lies inside band B, so band B is **cut** by the zero-change line: prints 186,000–194,000 lower the MA, 195,000 leaves it unchanged, 196,000–229,000 raise it. Bands C, D, E lie wholly above `R` (MA rises); band A wholly below (MA falls).

| Worked point (not a band) | `X` | `MA_next` ⚠️ | `ΔMA` ✅ |
|---|---|---|---|
| Kill-B edge | 185,000 | `771,000/4 = 192,750` | −2,500 |
| **Zero-change point** | 195,000 | `781,000/4 = 195,250` | **0** |
| **Modal — a 200,000 repeat** | 200,000 | `786,000/4 = 196,500` | +1,250 |
| Accelerating edge | 230,000 | `816,000/4 = 204,000` | +8,750 |
| T-02 edge | 301,000 | `887,000/4 = 221,750` | +26,500 |

🔴 **READING RULE (carried, conditional form):** a rising MA on a band-B print above 195,000 is **mechanical** (a lower week rolls off), as a falling MA was on the way down. I will describe the MA move only from the **as-published** MA and the regenerated `ΔMA`, never from this table's `MA_next` column (that column rotted again on 11/12, +500, while `ΔMA` stayed exact — L-31).

---

## §4 — WHAT THIS PRINT DOES **NOT** DO *(carried; WARN line regenerated)*

- A single weekly print is a realization gauge, not a demand-vs-supply discriminator.
- **A benign print is not a tightness finding.** Rate path → BOND, HENRY, ORACLE (STATUS § FED TRAP: pricing has moved on labor prints before; that is theirs to read). A multi-decade MA low is a level fact, graded by no band.
- 🔴 **REVISION JITTER (L-02), FOUR quantities regenerated BEFORE reading the level:** ① `ΔMA` (moves only if `R` revises) · ② `MA_next` column · ③ §5a bound · ④ §5d's 52-week MA minimum. The §2 BANDS key on fixed levels and are unaffected.
- ⚠️ **Dated WARN cohort in this week: Oracle ~800 (CA 441 `[CONF EDD]` + WA 359 `[CONF WA ESD]`), effective 11/13 ⇒ w/e Nov 14.** L-08: `800 / 200,000 = 0.4%` of a week — **no national attribution in either direction**; a state-level read only (CA, WA advance NSA in the release's state table). Next: Workday 142 (`[CONF EDD]`, eff 11/30 ⇒ w/e Dec 5). WE Soda WY 350 is staged from Q1 2027 (KB-LAB-268), not this week.
- ⚠️ **A streak restart is not a de-escalation.** §5b/§5c counts move no score.
- 📅 **Shutdown risk is not on this print:** CR expiry **Dec 11**. A missing release on 11/19 is graded UNKNOWN, never as a band.

---

## §5a — 🔴 T-01 ON THE **MA BASIS** — re-solved

`X > 1,000,000 − (W2+W3+W4) = 1,000,000 − 586,000` ⇒ **`X > 414,000`.** `414,000 → MA 250,000` (does **not** fire) · `415,000 → MA 250,250` (**fires**). ⚠️ Void the moment the window revises — re-solve at the print.

<!-- partition-axis: column="Initial claims, single print (T-01 MA axis)" -->
| T01 | Initial claims, single print (T-01 MA axis) | Pre-committed assignment |
|---|---|---|
| **T01-a** | ≤ 414,000 | MA ≤ 250,000 ⇒ **T-01 does NOT fire.** Bound re-solved at the print |
| **T01-b** | ≥ 415,000 | 🔴 **T-01 FIRES on the MA basis** → CARL + REGINALD, in addition to band E's T-02 |

## §5b — VECTOR-13 `<200,000` RUN — **record-only** (v13 at floor 1)

<!-- partition-axis: column="Initial claims, single print (vector-13 axis)" -->
| V13 | Initial claims, single print (vector-13 axis) | Pre-committed assignment |
|---|---|---|
| **V13-a** | ≤ 199,000 | run **restarts at 1** (counted at the print on the revised trailing week: if w/e Nov 7 revises below 200,000, the run is counted from there) — **record only; no score change** |
| **V13-b** | ≥ 200,000 | run stays at **0** — **record only; no score change.** Only band C (→ 3), §5d R13-c (→ 2) or T-01/T-02 move v13 |

## §5c — CONTINUING CLAIMS, w/e Nov 7 — v7 run **record-only** (v7 at floor 1)

Current **1,697,000** [w/e Oct 31]; `1,750,000 − 1,697,000 = 53,000` inside.

<!-- partition-axis: column="Continuing claims" -->
| Band | Continuing claims | Assignment |
|---|---|---|
| **CC-1** | < 1,750,000 | run extends by one week on the revised run, counted at the print — **record only; no score change** |
| **CC-2** | ≥ 1,750,000 | run **ends** — **record only; no score change.** No v7 return letter exists (DECIDED 10/21, KB-LAB-218) |

⚠️ CC is a cost/duration gauge, not early warning.

## §5d — v13 RETURN LETTER R13-c *(adopted 10/21, KB-LAB-218; REGENERATED)*

`rel = MA_published(w/e Nov 14) / min(published 4-week MA over the 52 weeks before w/e Nov 14)` — **recompute the minimum on the vintage at grade time** (the DOL 53-week table, or FRED IC4WSA). Illustration on the 11/12 vintage: min **195,250 (w/e Oct 31 and w/e Nov 7)** ⇒ bar `1.15 × 195,250 = 224,537.5` ⇒ needs `(586,000 + X)/4 ≥ 224,537.5` ⇒ `X ≥ 898,150 − 586,000 = 312,150`, i.e. **`X ≥ 313,000`** on DOL's whole-thousand grid (inside band E).

| R13 | rel (formula axis — the level is an illustration, L-27) | Pre-committed assignment |
|---|---|---|
| **R13-a** | rel ≥ 1.15 | **v13 1 → 2.** If §2 bands C/D/E also fire, the HIGHER v13 assignment governs; R13-c never lowers a score |
| **R13-b** | rel < 1.15 | no action |

---

## §6 — MECHANISM vs THRESHOLD — **no prediction resolves or is registered on this card.** Every band is a threshold/counter call. *(LAB-22, ≥1 of 8 advance prints ≤185,000, reads this print as one of its frozen draws — its own row grades it, not this card.)*

## §7 — ROUTING *(carried)*

| Outcome | Route | Priority |
|---|---|---|
| Band E | **WALTER** → REGINALD (all ORANGE→RED), HENRY — + CARL if ≥ §5a bound | 🔴 |
| Band D | **WALTER** → CARL, REGINALD | 🟠 |
| Band C (v13 1 → 3) | STATUS score + NEXUS brief; **direct 🟡 note to CARL** (its kill-rule leg 1 reads claims) | 🟡 |
| R13-c alone (v13 1 → 2) | STATUS score + NEXUS brief, no packet (watch-level move) | — |
| Bands A / B | STATUS only | — |
| §5b / §5c run changes | STATUS only — record, not a signal | — |

---

## §8 — CHECKER SCOPE AT FREEZE (BD-31)

🧾 **Checker receipt at freeze (2026-11-12 08:56 EST, `card_partition_check.py`):** `GRADING_CARD_20261119_claims.md: 7 band table(s) — 1 verified, 6 unverified, 0 with defects` · `[✓] table 2: VERIFIED — axis 'Initial claims, single print', 5 bands, precision 1,000, bounds as written`. Tables 1 and 3 are §1's inputs and §3's worked points, not band tables; tables 4–7 hand-proved below (BD-31 one-declaration limit). ⛔ `UNVERIFIED` is not a pass; **freeze authorized on `0 defects` + the hand proof.** Arithmetic of §1/§3/§5a/§5d re-run in python at freeze: every figure reproduced (781,000/4 = 195,250; trio 586,000; bound 414,000; R13-c `X ≥ 312,150` ⇒ 313,000, `rel(313,000) = 1.1511`, `rel(312,000) = 1.1498`).

| Table | Complement holds because |
|---|---|
| §5a T-01 | `≤ 414,000` / `≥ 415,000` — whole-thousand grid only; `414,000 → MA (586,000 + 414,000)/4 = 250,000` is not `> 250,000` |
| §5b v13 | `≤ 199,000` / `≥ 200,000` — exhaustive on DOL's whole-thousand grid only |
| §5c CC | `< 1,750,000` / `≥ 1,750,000` — true complement at any precision |
| §5d R13-c | `rel ≥ 1.15` / `rel < 1.15` — true complement at any precision |

## §9 — GRADE (write 2026-11-19 off this frozen card — never re-read a band)

*Blank until print. Order: ① regenerate the four §4 quantities on the as-published vintage · ② grade §2 · §5a · §5b · §5c · §5d separately · ③ write into `STATUS.md` (KEY THRESHOLDS, matrix v13 if band C+ or R13-a, score, calendar) · ④ `git mv` to `docket/graded/` and build the next card the same session (Thanksgiving week: verify the release day at DOL).*

**GRADED 2026-11-19 by LABOR (PROME wake prome-36, launched late: release read 09:2x ET, after the 08:30 print).** Source: DOL/ETA advance release PDF `https://www.dol.gov/ui/data.pdf`, embargo line "Thursday, November 19, 2026", fetched through `scripts/fetch_primary.py` (sha256 `a11a33cbd30081e8`; `--expect 203,000` FOUND, `--expect 1,763,000` FOUND); FRED ICSA / IC4WSA / CCSA agree. WALTER's card SIG-W-20261119-001 (same sha) reads the same.

**① Four quantities regenerated on the as-published vintage:**
- Window w/e Oct 24 · Oct 31 · Nov 7 · Nov 14 = `195,000 + 191,000 + 202,000 + 203,000 = 791,000`; `791,000 / 4 = 197,750` ✅ = published MA. Revision: w/e Nov 7 200,000 → **202,000**; its MA 195,250 → **195,750**.
- `ΔMA = (203,000 − 195,000)/4 = +2,000` ✅ = DOL's "+2,000 from the previous week's revised average" (R did not revise). Against the unrevised 195,250 the move is +2,500 (+500 is revision). The rise is **mechanical** under §3's reading rule (a lower week rolled off; 203,000 sits in band B).
- `MA_next` column said `(586,000 + 203,000)/4 = 197,250` on the freeze vintage; actual 197,750 — off by +500, exactly the w/e Nov 7 revision (L-31: the column rots, `ΔMA` stays exact).
- §5a bound re-solved: `1,000,000 − (195,000 + 191,000 + 202,000) = 412,000` (was 414,000).
- §5d minimum re-computed (FRED IC4WSA, 52 weeks before w/e Nov 14): **195,250 (w/e Oct 31)**; w/e Nov 7 no longer ties (revised to 195,750).

**② Grades, each axis separately:**

| Axis | Read | Assignment |
|---|---|---|
| §2 bands | **203,000** | **Band B — NO ACTION** |
| §5a T-01 | 203,000 ≤ 412,000; MA 197,750 | **T01-a — does NOT fire** (`250,000 − 197,750 = 52,250` away) |
| §5b v13 run | 203,000 ≥ 200,000; trailing week revised 202,000 (also ≥ 200,000) | **V13-b — run stays 0**, record only |
| §5c CC w/e Nov 7 | **1,763,000** (+70,000; w/e Oct 31 revised 1,697,000 → 1,693,000) | **CC-2 — run ENDS at 9**, record only, no score change |
| §5d R13-c | `197,750 / 195,250 = 1.0128` | **R13-b — no action** |
| Kill B | 203,000 > 185,000 | 0 of 5 |
| LAB-22 draw 2 of 8 | 203,000 > 185,000 | not a hit (row grades itself) |

**CC context (record, no band):** the +70,000 SA jump is mostly seasonal-factor gap — NSA rose +42,996 where the factors expected −18,620 (`42,996 + 18,620 = 61,616`); NSA 1,542,726 vs 1,708,938 a year earlier (`1,542,726 / 1,708,938 − 1 = −9.7%`). SA 1,763,000 is the highest since w/e Aug 29 (1,765,000) [FRED CCSA]. IUR 1.1% unchanged.
**§4 state read (Oracle ~800 cohort, eff 11/13):** CA advance NSA 43,159 (−1,615 w/w), WA 6,574 (−925) — both fell; invisible at state level, as L-08 predicted.
**③ Written to `STATUS.md`** (KEY THRESHOLDS claims + CC rows, matrix v13/v7 cells, calendar, exit-rule sweep). No score moved: total stays 22/80. **④** Moved to `docket/graded/`; next card `docket/GRADING_CARD_20261125_claims.md` frozen the same session (Thanksgiving week: Wed 11/25, inferred from ALFRED 3 of 3; DOL schedule page 403).
