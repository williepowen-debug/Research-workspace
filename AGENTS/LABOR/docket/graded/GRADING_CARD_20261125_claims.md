# 🔒 FROZEN GRADING CARD — Initial Claims w/e Nov 21, 2026

**Print:** **Wed 2026-11-25, 08:30 ET** — initial claims w/e **Nov 21** (+ continuing claims w/e **Nov 14**). Thanksgiving is Thu 11/26. ⚠️ **Release day INFERRED, 3 of 3 precedent:** ALFRED ICSA realtime_start shows DOL released Thanksgiving-week claims on the **Wednesday** before Thanksgiving in 2023 (11/22), 2024 (11/27) and 2025 (11/26) [FRED API, read 2026-11-19 ~09:22 ET]. DOL's own schedule page (`dol.gov/newsroom/economicdata`) returned **403** to this box on 2026-11-19; not bypassed. If no release appears Wed 11/25 by 09:00 ET, check Thu/Fri before grading anything as missing.
**Frozen:** 2026-11-19 (stamp on the commit), **in the session that graded the 11/19 card** (C2a recurring-print trigger) — **6 days ahead of the print.** PROME wake prome-36.
**Built from:** `docket/TEMPLATE_claims_card.md` + the 11/19 card (now `docket/graded/GRADING_CARD_20261119_claims.md`). **§1 · §3 · §5a · §5c · §5d REGENERATED from the 11/19 as-published window; §2 · §6 · §7 bands carried (no STATUS band changed on 11/19).**
**Why a card is owed:** multi-loaded — **T-01, T-02, vector 13 (band C re-escalation + R13-c return), Kill B**, plus CARL's kill-rule leg 1.

> 🔴 **On this print the score-moving axes are §2 bands C/D/E, §5a T-01 and §5d R13-c** (higher v13 assignment governs; R13-c never lowers a score). §5b and §5c are **record-only**; v7 has **no** return letter (decided 10/21).
> ⚠️ **`R` is 195,000** (w/e Oct 24). The retained trio is `191,000 + 202,000 + 203,000 = 596,000`, so a 203,000 repeat moves the MA **+2,000**; the zero-change print is 195,000.

---

## §1 — INPUTS FROZEN AT CURRENT VINTAGE *(REGENERATED from the DOL release of 2026-11-19 08:30 ET — AS-PUBLISHED vintage; KB-LAB-270)*

| Series | Value | Obs week | Source |
|---|---|---|---|
| Initial claims, latest (`W4`) | **203,000** | w/e 2026-11-14 | DOL/ETA advance release 2026-11-19 [CONF] (PDF text-extracted, sha256 `a11a33cbd30081e8`); FRED ICSA agrees |
| 4-week window `W1/W2/W3/W4` | **195,000 / 191,000 / 202,000 / 203,000** | w/e Oct 24 · Oct 31 · Nov 7 · Nov 14 | DOL 2026-11-19 (Nov 7 revised 200,000 → 202,000); FRED ICSA agrees |
| 4-week MA (`MA_cur`) | **197,750** | w/e 2026-11-14 | DOL 2026-11-19; FRED IC4WSA agrees |
| Continuing claims (`CC_cur`) | **1,763,000** | w/e 2026-11-07 | DOL 2026-11-19; FRED CCSA agrees |
| Kill B (`n_kb`) | **0 of 5** | — | STATUS |
| v13 `<200,000` run (record-only) | **0** (203,000 is not `<200,000`) · v13 at floor 1 | — | graded 11/19 |
| v7 CC `<1,750,000` run (record-only) | **0** — ended at 9 on 11/19 (1,763,000) · v7 at floor 1 | — | graded 11/19 |

**Reconciliation (division written):** `(195,000 + 191,000 + 202,000 + 203,000) / 4 = 791,000 / 4 = 197,750` ✅ **equals the published MA exactly.**
**Vintage note:** the 11/19 print revised w/e Nov 7 200,000 → **202,000** (initial; its MA 195,250 → 195,750) and w/e Oct 31 CC 1,697,000 → **1,693,000**. Expect `W4` (203,000) to revise at the 11/25 print.

---

## §2 — PRE-COMMITTED BANDS *(carried verbatim — no STATUS band changed on 11/19)*

<!-- partition-axis: column="Initial claims, single print" -->
| Band | Initial claims, single print | Pre-committed assignment |
|---|---|---|
| **A** | ≤ 185,000 | **Kill B leg** — count 0 → 1 of 5 |
| **B** | 186,000 – 229,000 | **NO ACTION** (drift band, `<230,000`) |
| **C** | 230,000 – 250,000 | **Accelerating** — vector 13: 1 → **3** (KEY THRESHOLDS letter "230–250K accelerating (v13 → 3)") |
| **D** | 251,000 – 300,000 | **ARM T-01 provisional** (confirm on a 2nd consecutive `>250,000`) |
| **E** | ≥ 301,000 | 🔴 **T-02 FIRE** → REGINALD (all ORANGE→RED) + HENRY |

**Distances from the 203,000 base:** T-01 `250,000 − 197,750 = 52,250` on the MA basis; T-02 `300,000 − 203,000 = 97,000` to the bar; band C's floor is `230,000 − 203,000 = 27,000` away; Kill B's edge is `203,000 − 185,000 = 18,000` below. Band B is modal.

---

## §3 — 🔴 THE MECHANICAL-DECLINE TRAP, PRE-COMPUTED *(REGENERATED)*

Rolling off: **w/e Oct 24 = 195,000** (`R = 195,000`).

`MA_next(X) = (191,000 + 202,000 + 203,000 + X)/4 = (596,000 + X)/4` ⚠️ **[VINTAGE-DEPENDENT — moves if ANY retained week revises]**
**`ΔMA(X) = (596,000 + X)/4 − 791,000/4 = (X − 195,000)/4`** ✅ **[depends only on `R`; measured against the REVISED prior MA, which is what DOL's "change from the previous week's revised average" reports]**

`R = 195,000` lies inside band B, so band B is **cut** by the zero-change line: prints 186,000–194,000 lower the MA, 195,000 leaves it unchanged, 196,000–229,000 raise it. Bands C, D, E lie wholly above `R` (MA rises); band A wholly below (MA falls).

| Worked point (not a band) | `X` | `MA_next` ⚠️ | `ΔMA` ✅ |
|---|---|---|---|
| Kill-B edge | 185,000 | `781,000/4 = 195,250` | −2,500 |
| **Zero-change point** | 195,000 | `791,000/4 = 197,750` | **0** |
| **Modal — a 203,000 repeat** | 203,000 | `799,000/4 = 199,750` | +2,000 |
| Accelerating edge | 230,000 | `826,000/4 = 206,500` | +8,750 |
| T-02 edge | 301,000 | `897,000/4 = 224,250` | +26,500 |

🔴 **READING RULE (carried, conditional form):** a rising MA on a band-B print above 195,000 is **mechanical** (a lower week rolls off). I will describe the MA move only from the **as-published** MA and the regenerated `ΔMA`, never from this table's `MA_next` column (L-31). **11/19 check of the rule:** card `ΔMA(203,000) = (203,000 − 195,000)/4 = +2,000` = DOL's published "+2,000 from the previous week's revised average" exactly; against the unrevised 195,250 the move was +2,500, of which +500 was the revision.

---

## §4 — WHAT THIS PRINT DOES **NOT** DO *(carried; WARN line regenerated)*

- A single weekly print is a realization gauge, not a demand-vs-supply discriminator.
- **A benign print is not a tightness finding.** Rate path → BOND, HENRY, ORACLE.
- 🔴 **REVISION JITTER (L-02), FOUR quantities regenerated BEFORE reading the level:** ① `ΔMA` (moves only if `R` revises) · ② `MA_next` column · ③ §5a bound · ④ §5d's 52-week MA minimum. The §2 BANDS key on fixed levels and are unaffected.
- ⚠️ **Holiday-week seasonals:** Thanksgiving-week NSA claims move sharply and the seasonal factors are large; a band-B print here is graded as printed, and no holiday story is attributed to it in either direction.
- ⚠️ **Dated WARN cohort in this week: none in `docket/WARN_COHORT.tsv`.** Next: Wells Fargo Roanoke 87 (eff 11/28 ⇒ w/e Nov 28) and Workday 142 (`[CONF EDD]`, eff 11/30 ⇒ w/e Dec 5). L-08: both under 0.1% of a week. The 11/19 state read of the Oracle ~800 cohort (eff 11/13): CA advance NSA 43,159 (−1,615) and WA 6,574 (−925) both FELL in w/e Nov 14 — invisible even at state level.
- ⚠️ **A streak restart is not a de-escalation.** §5b/§5c counts move no score.
- 📅 **Shutdown risk is not on this print:** CR expiry **Dec 11**. A missing release is graded UNKNOWN, never as a band.

---

## §5a — 🔴 T-01 ON THE **MA BASIS** — re-solved

`X > 1,000,000 − (W2+W3+W4) = 1,000,000 − 596,000` ⇒ **`X > 404,000`.** `404,000 → MA 250,000` (does **not** fire) · `405,000 → MA 250,250` (**fires**). ⚠️ Void the moment the window revises — re-solve at the print.

<!-- partition-axis: column="Initial claims, single print (T-01 MA axis)" -->
| T01 | Initial claims, single print (T-01 MA axis) | Pre-committed assignment |
|---|---|---|
| **T01-a** | ≤ 404,000 | MA ≤ 250,000 ⇒ **T-01 does NOT fire.** Bound re-solved at the print |
| **T01-b** | ≥ 405,000 | 🔴 **T-01 FIRES on the MA basis** → CARL + REGINALD, in addition to band E's T-02 |

## §5b — VECTOR-13 `<200,000` RUN — **record-only** (v13 at floor 1)

<!-- partition-axis: column="Initial claims, single print (vector-13 axis)" -->
| V13 | Initial claims, single print (vector-13 axis) | Pre-committed assignment |
|---|---|---|
| **V13-a** | ≤ 199,000 | run **restarts at 1** (counted at the print on the revised trailing week) — **record only; no score change** |
| **V13-b** | ≥ 200,000 | run stays at **0** — **record only; no score change.** Only band C (→ 3), §5d R13-c (→ 2) or T-01/T-02 move v13 |

## §5c — CONTINUING CLAIMS, w/e Nov 14 — v7 run **record-only** (v7 at floor 1)

Current **1,763,000** [w/e Nov 7]; `1,763,000 − 1,750,000 = 13,000` above the line. ⚠️ The 11/19 jump (+70,000 SA) was mostly a seasonal-factor gap: NSA +42,996 where the factors expected −18,620; NSA 1,542,726 vs 1,708,938 a year earlier (DOL 11/19).

<!-- partition-axis: column="Continuing claims" -->
| Band | Continuing claims | Assignment |
|---|---|---|
| **CC-1** | < 1,750,000 | run **restarts at 1**, counted at the print on the revised run — **record only; no score change** |
| **CC-2** | ≥ 1,750,000 | run stays at **0** — **record only; no score change.** No v7 return letter exists (DECIDED 10/21, KB-LAB-218) |

⚠️ CC is a cost/duration gauge, not early warning.

## §5d — v13 RETURN LETTER R13-c *(adopted 10/21, KB-LAB-218; REGENERATED)*

`rel = MA_published(w/e Nov 21) / min(published 4-week MA over the 52 weeks before w/e Nov 21)` — **recompute the minimum on the vintage at grade time** (the DOL 53-week table, or FRED IC4WSA). Illustration on the 11/19 vintage: min **195,250 (w/e Oct 31 only; w/e Nov 7 revised to 195,750)** ⇒ bar `1.15 × 195,250 = 224,537.5` ⇒ needs `(596,000 + X)/4 ≥ 224,537.5` ⇒ `X ≥ 898,150 − 596,000 = 302,150`, i.e. **`X ≥ 303,000`** on DOL's whole-thousand grid (inside band E).

| R13 | rel (formula axis — the level is an illustration, L-27) | Pre-committed assignment |
|---|---|---|
| **R13-a** | rel ≥ 1.15 | **v13 1 → 2.** If §2 bands C/D/E also fire, the HIGHER v13 assignment governs; R13-c never lowers a score |
| **R13-b** | rel < 1.15 | no action |

---

## §6 — MECHANISM vs THRESHOLD — **no prediction resolves or is registered on this card.** Every band is a threshold/counter call. *(LAB-22, ≥1 of 8 advance prints ≤185,000, reads this print as its draw 3 of 8; its own row grades it, not this card.)*

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

🧾 **Checker receipt at freeze (2026-11-19 09:24 EST, `card_partition_check.py`):** `GRADING_CARD_20261125_claims.md: 7 band table(s) — 1 verified, 6 unverified, 0 with defects` · `[✓] table 2: VERIFIED — axis 'Initial claims, single print', 5 bands, precision 1,000, bounds as written`. Tables 1 and 3 are §1's inputs and §3's worked points, not band tables; tables 4–7 hand-proved below (BD-31 one-declaration limit; the 11/19 card froze on the identical receipt). ⛔ `UNVERIFIED` is not a pass; **freeze authorized on `0 defects` + the hand proof.**

| Table | Complement holds because |
|---|---|
| §5a T-01 | `≤ 404,000` / `≥ 405,000` — whole-thousand grid only; `404,000 → MA (596,000 + 404,000)/4 = 250,000` is not `> 250,000` |
| §5b v13 | `≤ 199,000` / `≥ 200,000` — exhaustive on DOL's whole-thousand grid only |
| §5c CC | `< 1,750,000` / `≥ 1,750,000` — true complement at any precision |
| §5d R13-c | `rel ≥ 1.15` / `rel < 1.15` — true complement at any precision |

Arithmetic re-run in python at freeze: 791,000/4 = 197,750; trio 596,000; bound 404,000; R13-c `X ≥ 302,150` ⇒ 303,000, `rel(303,000) = 1.1511`, `rel(302,000) = 1.1498`.

## §9 — GRADE (write 2026-11-25 off this frozen card — never re-read a band)

*Blank until print. Order: ① regenerate the four §4 quantities on the as-published vintage · ② grade §2 · §5a · §5b · §5c · §5d separately · ③ write into `STATUS.md` (KEY THRESHOLDS, matrix v13 if band C+ or R13-a, score, calendar) · ④ `git mv` to `docket/graded/` and build the next card the same session (w/e Nov 28, Thu 12/3).*

**GRADED 2026-11-25 by LABOR (PROME wake prome-77, read 09:02 ET, after the 08:30 print).** The inferred release day held: DOL published on **Wednesday, November 25, 2026** (embargo line). Source: DOL/ETA advance release PDF `https://www.dol.gov/ui/data.pdf`, fetched through the edited `scripts/fetch_primary.py` in ONE request as `research-bot/1.0` (HTTP 200, 614,495 B, sha256 `c26ef0b407589af8`); `--expect 189,000` FOUND, `--expect 1,697,000` FOUND. FRED ICSA / IC4WSA / CCSA agree (read 09:04 ET).

| Print (as published 11/25) | Value |
|---|---|
| Initial claims, w/e Nov 21 (advance, SA) | **189,000** (−13,000 vs revised prior) |
| w/e Nov 14 revision | 203,000 → **202,000** |
| 4-week MA | **196,000** (−1,500 vs revised prior); prior MA revised 197,750 → 197,500 |
| Continuing claims, w/e Nov 14 | **1,697,000** (−95,000); w/e Nov 7 revised **1,763,000 → 1,792,000** (+29,000) |
| CC 4-week MA | 1,724,750 (+500); prior revised 1,717,000 → 1,724,250 |
| IUR (SA) | 1.1% (w/e Nov 14); prior revised 1.1 → 1.2 |
| NSA initial | 212,945, +15,894 (+8.1%) where the seasonal factors expected +30,549 (+15.5%); year-ago week 244,713 (`212,945 / 244,713 − 1 = −13.0%`) |
| NSA insured unemployment | 1,562,814, −5,578 where the factors expected +82,453; year-ago 1,781,543 |

**① Four quantities regenerated on the as-published vintage.** `R` (w/e Oct 24) did not revise: revised prior MA `197,500 × 4 = 790,000 = 195,000 + 191,000 + 202,000 + 202,000` ✅. (i) **`ΔMA = (189,000 − 195,000)/4 = −1,500`** = DOL's published "−1,500 from the previous week's revised average" exactly. (ii) `MA_next` on the revised trio `191,000 + 202,000 + 202,000 = 595,000`: `(595,000 + 189,000)/4 = 784,000/4 = 196,000` = DOL. (iii) T-01 bound re-solved on the revised trio: `X > 1,000,000 − 595,000 = 405,000`. (iv) R13-c minimum: published 4-week MA over the 52 weeks before w/e Nov 21 on FRED IC4WSA (current vintage, read 09:04 ET) = **195,250 (w/e Oct 31)**, unchanged.

**② Grades, each axis separately:**
- **§2: band B** (186,000 – 229,000) ⇒ **NO ACTION.** Not band A: `189,000 − 185,000 = 4,000` above the Kill B edge ⇒ Kill B stays **0 of 5**.
- **§5a: T01-a** (`189,000 ≤ 405,000`) ⇒ T-01 does not fire. MA 196,000 is `250,000 − 196,000 = 54,000` below.
- **§5b: V13-a** (`189,000 ≤ 199,000`) ⇒ the `<200,000` run **restarts at 1** (trailing week w/e Nov 14 revised 202,000 is not `<200,000`). Record only; no score change.
- **§5c: CC-1** (`1,697,000 < 1,750,000`) ⇒ the CC run **restarts at 1** (trailing w/e Nov 7 revised to 1,792,000 is above the line). Record only; no score change.
- **§5d: R13-b** — `rel = 196,000 / 195,250 = 1.0038 < 1.15` ⇒ no action.
- **§6:** LAB-22 draw 3 of 8 = 189,000, not ≤185,000 and not the 186,000 no-verdict value ⇒ **no**; graded on its own row.

**Reading rule applied (§3):** the MA fell 1,500 because a print below `R` replaced the 195,000 week; that is mechanical, stated from DOL's published move. **Holiday week (§4):** graded as printed. On the record and attributed to nothing: the SA fall came with NSA claims rising 15,894 where the factors expected +30,549, and the CC fall of 95,000 SA came with NSA −5,578 where the factors expected +82,453, the reverse of last week's +70,000 gap; w/e Nov 7 CC itself revised up 29,000 to 1,792,000.

**③ Written to STATUS 2026-11-25** (KEY THRESHOLDS claims and CC rows, matrix v13 and v7 record cells, Kill B, calendar). No score moves; total stays 22/80. **Routing (§7): bands A/B ⇒ STATUS only.** **④** `git mv` to `docket/graded/` this session; next card `docket/GRADING_CARD_20261203_claims.md` (w/e Nov 28, Thu 12/3) built the same session.
