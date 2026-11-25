# 🔒 FROZEN GRADING CARD — Initial Claims w/e Nov 28, 2026

**Print:** **Thu 2026-12-03, 08:30 ET** — initial claims w/e **Nov 28** (+ continuing claims w/e **Nov 21**). ⚠️ **Release day MODELED** on the normal Thursday schedule; not checked at DOL. If nothing posts Thu 12/3 by 09:00 ET, check the DOL release page before grading anything as missing.
**Frozen:** 2026-11-25 (stamp on the commit), **in the session that graded the 11/25 card** (C2a recurring-print trigger) — **8 days ahead of the print.** PROME wake prome-77.
**Built from:** `docket/TEMPLATE_claims_card.md` + the 11/25 card (now `docket/graded/GRADING_CARD_20261125_claims.md`). **§1 · §3 · §5a · §5b · §5c · §5d REGENERATED from the 11/25 as-published window; §2 · §6 · §7 bands carried (no STATUS band changed on 11/25).**
**Why a card is owed:** multi-loaded — **T-01, T-02, vector 13 (band C re-escalation + R13-c return), Kill B**, plus CARL's kill-rule leg 1.

> 🔴 **On this print the score-moving axes are §2 bands C/D/E, §5a T-01 and §5d R13-c** (higher v13 assignment governs; R13-c never lowers a score). §5b and §5c are **record-only**; v7 has **no** return letter (decided 10/21).
> ⚠️ **`R` is 191,000** (w/e Oct 31). The retained trio is `202,000 + 202,000 + 189,000 = 593,000`, so a 189,000 repeat moves the MA **−500**; the zero-change print is 191,000.

---

## §1 — INPUTS FROZEN AT CURRENT VINTAGE *(REGENERATED from the DOL release of 2026-11-25 08:30 ET — AS-PUBLISHED vintage)*

| Series | Value | Obs week | Source |
|---|---|---|---|
| Initial claims, latest (`W4`) | **189,000** | w/e 2026-11-21 | DOL/ETA advance release 2026-11-25 [CONF] (PDF text-extracted, sha256 `c26ef0b407589af8`); FRED ICSA agrees |
| 4-week window `W1/W2/W3/W4` | **191,000 / 202,000 / 202,000 / 189,000** | w/e Oct 31 · Nov 7 · Nov 14 · Nov 21 | DOL 2026-11-25 (Nov 14 revised 203,000 → 202,000); FRED ICSA agrees |
| 4-week MA (`MA_cur`) | **196,000** | w/e 2026-11-21 | DOL 2026-11-25; FRED IC4WSA agrees |
| Continuing claims (`CC_cur`) | **1,697,000** | w/e 2026-11-14 | DOL 2026-11-25; FRED CCSA agrees |
| Kill B (`n_kb`) | **0 of 5** | — | STATUS |
| v13 `<200,000` run (record-only) | **1** (189,000; restarted 11/25) · v13 at floor 1 | — | graded 11/25 |
| v7 CC `<1,750,000` run (record-only) | **1** (1,697,000; restarted 11/25) · v7 at floor 1 | — | graded 11/25 |

**Reconciliation (division written):** `(191,000 + 202,000 + 202,000 + 189,000) / 4 = 784,000 / 4 = 196,000` ✅ **equals the published MA exactly.**
**Vintage note:** the 11/25 print revised w/e Nov 14 203,000 → **202,000** (its MA 197,750 → 197,500) and w/e Nov 7 CC 1,763,000 → **1,792,000**. Expect `W4` (189,000) to revise at the 12/3 print.

---

## §2 — PRE-COMMITTED BANDS *(carried verbatim — no STATUS band changed on 11/25)*

<!-- partition-axis: column="Initial claims, single print" -->
| Band | Initial claims, single print | Pre-committed assignment |
|---|---|---|
| **A** | ≤ 185,000 | **Kill B leg** — count 0 → 1 of 5 |
| **B** | 186,000 – 229,000 | **NO ACTION** (drift band, `<230,000`) |
| **C** | 230,000 – 250,000 | **Accelerating** — vector 13: 1 → **3** (KEY THRESHOLDS letter "230–250K accelerating (v13 → 3)") |
| **D** | 251,000 – 300,000 | **ARM T-01 provisional** (confirm on a 2nd consecutive `>250,000`) |
| **E** | ≥ 301,000 | 🔴 **T-02 FIRE** → REGINALD (all ORANGE→RED) + HENRY |

**Distances from the 189,000 base:** T-01 `250,000 − 196,000 = 54,000` on the MA basis; T-02 `300,000 − 189,000 = 111,000` to the bar; band C's floor is `230,000 − 189,000 = 41,000` away; Kill B's edge is `189,000 − 185,000 = 4,000` below. Band B is modal.

---

## §3 — 🔴 THE MECHANICAL-DECLINE TRAP, PRE-COMPUTED *(REGENERATED)*

Rolling off: **w/e Oct 31 = 191,000** (`R = 191,000`).

`MA_next(X) = (202,000 + 202,000 + 189,000 + X)/4 = (593,000 + X)/4` ⚠️ **[VINTAGE-DEPENDENT — moves if ANY retained week revises]**
**`ΔMA(X) = (593,000 + X)/4 − 784,000/4 = (X − 191,000)/4`** ✅ **[depends only on `R`; measured against the REVISED prior MA, which is what DOL's "change from the previous week's revised average" reports]**

`R = 191,000` lies inside band B, so band B is **cut** by the zero-change line: prints 186,000–190,000 lower the MA, 191,000 leaves it unchanged, 192,000–229,000 raise it. Bands C, D, E lie wholly above `R` (MA rises); band A wholly below (MA falls).

| Worked point (not a band) | `X` | `MA_next` ⚠️ | `ΔMA` ✅ |
|---|---|---|---|
| Kill-B edge | 185,000 | `778,000/4 = 194,500` | −1,500 |
| **Modal — a 189,000 repeat** | 189,000 | `782,000/4 = 195,500` | −500 |
| **Zero-change point** | 191,000 | `784,000/4 = 196,000` | **0** |
| Accelerating edge | 230,000 | `823,000/4 = 205,750` | +9,750 |
| T-02 edge | 301,000 | `894,000/4 = 223,500` | +27,500 |

🔴 **READING RULE (carried, conditional form):** a rising MA on a band-B print above 191,000 is **mechanical** (a lower week rolls off), and so is a falling MA on a print below it. I will describe the MA move only from the **as-published** MA and the regenerated `ΔMA`, never from this table's `MA_next` column (L-31). **11/25 check of the rule:** card `ΔMA(189,000) = (189,000 − 195,000)/4 = −1,500` = DOL's published "−1,500 from the previous week's revised average" exactly.

---

## §4 — WHAT THIS PRINT DOES **NOT** DO *(carried; WARN line regenerated)*

- A single weekly print is a realization gauge, not a demand-vs-supply discriminator.
- **A benign print is not a tightness finding.** Rate path → BOND, HENRY, ORACLE.
- 🔴 **REVISION JITTER (L-02), FOUR quantities regenerated BEFORE reading the level:** ① `ΔMA` (moves only if `R` revises) · ② `MA_next` column · ③ §5a bound · ④ §5d's 52-week MA minimum. The §2 BANDS key on fixed levels and are unaffected.
- ⚠️ **Holiday-week seasonals:** w/e Nov 28 contains Thanksgiving. The 11/25 print showed the factors at work (NSA +15,894 where they expected +30,549; CC NSA −5,578 where they expected +82,453). A band-B print here is graded as printed, and no holiday story is attributed to it in either direction.
- ⚠️ **Dated WARN cohort in this week:** Wells Fargo Roanoke 87 (eff 11/28 ⇒ w/e Nov 28), `87 / 189,000 = 0.05%` of a week. Next: Workday 142 (`[CONF EDD]`, eff 11/30 ⇒ w/e Dec 5). L-08: state-level only.
- ⚠️ **A streak restart is not a de-escalation.** §5b/§5c counts move no score.
- 📅 **Shutdown risk is not on this print:** CR expiry **Dec 11**. A missing release is graded UNKNOWN, never as a band.

---

## §5a — 🔴 T-01 ON THE **MA BASIS** — re-solved

`X > 1,000,000 − (W2+W3+W4) = 1,000,000 − 593,000` ⇒ **`X > 407,000`.** `407,000 → MA 250,000` (does **not** fire) · `408,000 → MA 250,250` (**fires**). ⚠️ Void the moment the window revises — re-solve at the print.

<!-- partition-axis: column="Initial claims, single print (T-01 MA axis)" -->
| T01 | Initial claims, single print (T-01 MA axis) | Pre-committed assignment |
|---|---|---|
| **T01-a** | ≤ 407,000 | MA ≤ 250,000 ⇒ **T-01 does NOT fire.** Bound re-solved at the print |
| **T01-b** | ≥ 408,000 | 🔴 **T-01 FIRES on the MA basis** → CARL + REGINALD, in addition to band E's T-02 |

## §5b — VECTOR-13 `<200,000` RUN — **record-only** (v13 at floor 1)

<!-- partition-axis: column="Initial claims, single print (vector-13 axis)" -->
| V13 | Initial claims, single print (vector-13 axis) | Pre-committed assignment |
|---|---|---|
| **V13-a** | ≤ 199,000 | run **1 → 2** if the trailing week (w/e Nov 21) is still `<200,000` on its revision, else restarts at 1 — **record only; no score change** |
| **V13-b** | ≥ 200,000 | run **resets to 0** — **record only; no score change.** Only band C (→ 3), §5d R13-c (→ 2) or T-01/T-02 move v13 |

## §5c — CONTINUING CLAIMS, w/e Nov 21 — v7 run **record-only** (v7 at floor 1)

Current **1,697,000** [w/e Nov 14]; `1,750,000 − 1,697,000 = 53,000` inside the line. ⚠️ Two weeks of seasonal-factor swing in opposite directions (11/19: +70,000 SA on NSA +42,996 vs factors −18,620; 11/25: −95,000 SA on NSA −5,578 vs factors +82,453), and w/e Nov 7 revised up 29,000 to 1,792,000 (DOL 11/25).

<!-- partition-axis: column="Continuing claims" -->
| Band | Continuing claims | Assignment |
|---|---|---|
| **CC-1** | < 1,750,000 | run **1 → 2** if w/e Nov 14 is still `<1,750,000` on its revision, else restarts at 1 — **record only; no score change** |
| **CC-2** | ≥ 1,750,000 | run **resets to 0** — **record only; no score change.** No v7 return letter exists (DECIDED 10/21, KB-LAB-218) |

⚠️ CC is a cost/duration gauge, not early warning.

## §5d — v13 RETURN LETTER R13-c *(adopted 10/21, KB-LAB-218; REGENERATED)*

`rel = MA_published(w/e Nov 28) / min(published 4-week MA over the 52 weeks before w/e Nov 28)` — **recompute the minimum on the vintage at grade time** (the DOL 53-week table, or FRED IC4WSA). Illustration on the 11/25 vintage: min **195,250 (w/e Oct 31)** [FRED IC4WSA, read 2026-11-25 09:04 ET; 52 weekly observations before w/e Nov 21, and w/e Nov 21's 196,000 does not lower it] ⇒ bar `1.15 × 195,250 = 224,537.5` ⇒ needs `(593,000 + X)/4 ≥ 224,537.5` ⇒ `X ≥ 898,150 − 593,000 = 305,150`, i.e. **`X ≥ 306,000`** on DOL's whole-thousand grid (inside band E).

| R13 | rel (formula axis — the level is an illustration, L-27) | Pre-committed assignment |
|---|---|---|
| **R13-a** | rel ≥ 1.15 | **v13 1 → 2.** If §2 bands C/D/E also fire, the HIGHER v13 assignment governs; R13-c never lowers a score |
| **R13-b** | rel < 1.15 | no action |

---

## §6 — MECHANISM vs THRESHOLD — **no prediction resolves or is registered on this card.** Every band is a threshold/counter call. *(LAB-22, ≥1 of 8 advance prints ≤185,000, reads this print as its draw 4 of 8; its own row grades it, not this card.)*

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

🧾 **Checker receipt at freeze (2026-11-25 09:07 EST, `card_partition_check.py`, rc 2):** `GRADING_CARD_20261203_claims.md: 7 band table(s) — 1 verified, 6 unverified, 0 with defects` · `[✓] table 2: VERIFIED — axis 'Initial claims, single print', 5 bands, precision 1,000, bounds as written`. Tables 1 and 3 are §1's inputs and §3's worked points, not band tables; tables 4–7 hand-proved below (BD-31 one-declaration limit; the 11/19 and 11/25 cards froze on the identical receipt). ⛔ `UNVERIFIED` is not a pass; **freeze authorized on `0 defects` + the hand proof.**

| Table | Complement holds because |
|---|---|
| §5a T-01 | `≤ 407,000` / `≥ 408,000` — whole-thousand grid only; `407,000 → MA (593,000 + 407,000)/4 = 250,000` is not `> 250,000` |
| §5b v13 | `≤ 199,000` / `≥ 200,000` — exhaustive on DOL's whole-thousand grid only |
| §5c CC | `< 1,750,000` / `≥ 1,750,000` — true complement at any precision |
| §5d R13-c | `rel ≥ 1.15` / `rel < 1.15` — true complement at any precision |

Arithmetic re-run in python at freeze: 784,000/4 = 196,000; trio 593,000; bound 407,000; worked points 194,500 / 195,500 / 205,750 / 223,500 and ΔMA −1,500 / −500 / +9,750 / +27,500; R13-c `X ≥ 305,150` ⇒ 306,000, `rel(306,000) = 1.1511`, `rel(305,000) = 1.1498`; WARN `87 / 189,000 = 0.05%`.

## §9 — GRADE (write 2026-12-03 off this frozen card — never re-read a band)

*Blank until print. Order: ① regenerate the four §4 quantities on the as-published vintage · ② grade §2 · §5a · §5b · §5c · §5d separately · ③ write into `STATUS.md` (KEY THRESHOLDS, matrix v13 if band C+ or R13-a, score, calendar) · ④ `git mv` to `docket/graded/` and build the next card the same session (w/e Dec 5, Thu 12/10).*
