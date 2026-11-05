# 🔒 FROZEN GRADING CARD — Initial Claims w/e Nov 7, 2026

**Print:** Thu **2026-11-12, 08:30 ET** — initial claims w/e **Nov 7** (+ continuing claims w/e **Oct 31**). Date modeled from the weekly Thursday schedule; Veterans Day is Wed 11/11, so a Thursday release should stand (INFERRED, not checked at DOL).
**Frozen:** 2026-11-05 (stamp on the commit), **in the session that graded the 11/5 card** (C2a recurring-print trigger) — **7 days ahead of the print.** WQ-618 A session.
**Built from:** `docket/TEMPLATE_claims_card.md` + the 11/5 card (now `docket/graded/GRADING_CARD_20261105_claims.md`). **§1 · §3 · §5a · §5d REGENERATED from the 11/5 as-published window; §5b/§5c counts regenerated; §4 WARN line regenerated; §2 · §6 · §7 bands carried (no STATUS band changed on 11/5).**
**Why a card is owed:** multi-loaded — **T-01, T-02, vector 13 (band C re-escalation + R13-c return), Kill B**, plus CARL's kill-rule leg 1.

> 🔴 **On this print the score-moving axes are §2 bands C/D/E, §5a T-01 and §5d R13-c** (higher v13 assignment governs; R13-c never lowers a score). §5b and §5c are **record-only**; v7 has **no** return letter (decided 10/21).
> ⚠️ **`R` is 200,000** (w/e Oct 10). The retained trio is `195,000 + 195,000 + 189,000 = 579,000`, so a 189,000 repeat moves the MA **−2,750**; the zero-change print is 200,000.

---

## §1 — INPUTS FROZEN AT CURRENT VINTAGE *(REGENERATED from the DOL release of 2026-11-05 08:30 ET — AS-PUBLISHED vintage; KB-LAB-231)*

| Series | Value | Obs week | Source |
|---|---|---|---|
| Initial claims, latest (`W4`) | **189,000** | w/e 2026-10-31 | DOL/ETA advance release 2026-11-05 [CONF] (PDF text-extracted); FRED ICSA agrees |
| 4-week window `W1/W2/W3/W4` | **200,000 / 195,000 / 195,000 / 189,000** | w/e Oct 10 · Oct 17 · Oct 24 · Oct 31 | DOL 2026-11-05; FRED ICSA agrees |
| 4-week MA (`MA_cur`) | **194,750** | w/e 2026-10-31 | DOL 2026-11-05; FRED IC4WSA agrees |
| Continuing claims (`CC_cur`) | **1,718,000** | w/e 2026-10-24 | DOL 2026-11-05; FRED CCSA agrees |
| Kill B (`n_kb`) | **0 of 5** | — | STATUS |
| v13 `<200,000` run (record-only) | **3** (Oct 17 · Oct 24 · Oct 31) · v13 at floor 1 | — | graded 11/5 |
| v7 CC `<1,750,000` run (record-only) | **8** (Sep 5 through Oct 24) — v7 at 2 | — | graded 11/5 |

**Reconciliation (division written):** `(200,000 + 195,000 + 195,000 + 189,000) / 4 = 779,000 / 4 = 194,750` ✅ **equals the published MA exactly.**
**Vintage note:** the 11/5 print revised w/e Oct 24 194,000 → **195,000** (initial) and w/e Oct 17 CC 1,701,000 → **1,695,000**. Expect `W4` (189,000) to revise at the 11/12 print.

---

## §2 — PRE-COMMITTED BANDS *(carried verbatim — no STATUS band changed on 11/5)*

<!-- partition-axis: column="Initial claims, single print" -->
| Band | Initial claims, single print | Pre-committed assignment |
|---|---|---|
| **A** | ≤ 185,000 | **Kill B leg** — count 0 → 1 of 5 |
| **B** | 186,000 – 229,000 | **NO ACTION** (drift band, `<230,000`) |
| **C** | 230,000 – 250,000 | **Accelerating** — vector 13: 1 → **3** (KEY THRESHOLDS letter "230–250K accelerating (v13 → 3)") |
| **D** | 251,000 – 300,000 | **ARM T-01 provisional** (confirm on a 2nd consecutive `>250,000`) |
| **E** | ≥ 301,000 | 🔴 **T-02 FIRE** → REGINALD (all ORANGE→RED) + HENRY |

**Distances from the 189,000 base:** T-01 `250,000 − 194,750 = 55,250` on the MA basis; T-02 `300,000 − 189,000 = 111,000` to the bar; the first firing print (band E, 301,000) is `112,000` away; band C's floor is `230,000 − 189,000 = 41,000` away; Kill B's edge is `189,000 − 185,000 = 4,000` below. Band B is modal.

---

## §3 — 🔴 THE MECHANICAL-DECLINE TRAP, PRE-COMPUTED *(REGENERATED)*

Rolling off: **w/e Oct 10 = 200,000** (`R = 200,000`).

`MA_next(X) = (195,000 + 195,000 + 189,000 + X)/4 = (579,000 + X)/4` ⚠️ **[VINTAGE-DEPENDENT — moves if ANY retained week revises]**
**`ΔMA(X) = (579,000 + X)/4 − 779,000/4 = (X − 200,000)/4`** ✅ **[depends only on `R`]**

`R = 200,000` lies inside band B, so band B is **cut** by the zero-change line: prints 186,000–199,000 lower the MA, 200,000 leaves it unchanged, 201,000–229,000 raise it. Bands C, D, E lie wholly above `R` (MA rises); band A wholly below (MA falls).

| Worked point (not a band) | `X` | `MA_next` ⚠️ | `ΔMA` ✅ |
|---|---|---|---|
| Kill-B edge | 185,000 | `764,000/4 = 191,000` | −3,750 |
| **Modal — a 189,000 repeat** | 189,000 | `768,000/4 = 192,000` | −2,750 |
| **Zero-change point** | 200,000 | `779,000/4 = 194,750` | **0** |
| Accelerating edge | 230,000 | `809,000/4 = 202,250` | +7,500 |
| T-02 edge | 301,000 | `880,000/4 = 220,000` | +25,250 |

🔴 **READING RULE (carried, conditional form):** a falling MA on a band-B print is **mechanical**. I will describe the MA move only from the **as-published** MA and the regenerated `ΔMA`, never from this table's `MA_next` column (that column has rotted with retained-week revisions seven weeks running while `ΔMA` stayed exact — L-31).

---

## §4 — WHAT THIS PRINT DOES **NOT** DO *(carried; WARN line regenerated)*

- A single weekly print is a realization gauge, not a demand-vs-supply discriminator.
- **A benign print is not hawkish fuel — it is nothing.** Rate path → BOND, HENRY, ORACLE. A new multi-decade MA low (11/5: 194,750, lowest on FRED's current IC4WSA vintage since w/e 1969-09-27) is a level fact, graded by no band — and a level, not a rate.
- 🔴 **REVISION JITTER (L-02), FOUR quantities regenerated BEFORE reading the level:** ① `ΔMA` (moves only if `R` revises) · ② `MA_next` column · ③ §5a bound · ④ §5d's 52-week MA minimum. The §2 BANDS key on fixed levels and are unaffected.
- ⛔ **No dated WARN cohort is registered for w/e Nov 7.** JPMorgan Jersey City 91 (`[2ND]`, LEAD-UNVERIFIED) runs Oct 30 to Jan 24 2027; L-08: `91 / 20,000 = 0.5%` of the national floor, **no national attribution in either direction.** Next: Oracle ~800 (eff 11/13 ⇒ w/e Nov 14), Workday 142 (`[CONF EDD]`, eff 11/30 ⇒ w/e Dec 5).
- ⚠️ **A streak break is not an escalation.** §5b/§5c counts move no score.
- 📅 **Shutdown risk is not on this print:** CR expiry **Dec 11**. A missing release on 11/12 is graded UNKNOWN, never as a band.

---

## §5a — 🔴 T-01 ON THE **MA BASIS** — re-solved

`X > 1,000,000 − (W2+W3+W4) = 1,000,000 − 579,000` ⇒ **`X > 421,000`.** `421,000 → MA 250,000` (does **not** fire) · `422,000 → MA 250,250` (**fires**). ⚠️ Void the moment the window revises — re-solve at the print.

<!-- partition-axis: column="Initial claims, single print (T-01 MA axis)" -->
| T01 | Initial claims, single print (T-01 MA axis) | Pre-committed assignment |
|---|---|---|
| **T01-a** | ≤ 421,000 | MA ≤ 250,000 ⇒ **T-01 does NOT fire.** Bound re-solved at the print |
| **T01-b** | ≥ 422,000 | 🔴 **T-01 FIRES on the MA basis** → CARL + REGINALD, in addition to band E's T-02 |

## §5b — VECTOR-13 `<200,000` RUN — **record-only** (v13 at floor 1)

<!-- partition-axis: column="Initial claims, single print (vector-13 axis)" -->
| V13 | Initial claims, single print (vector-13 axis) | Pre-committed assignment |
|---|---|---|
| **V13-a** | ≤ 199,000 | run extends by one week **on the revised trailing run, counted at the print** (the count is NOT pre-written: a retained-week revision cut the 10/22 card's pre-written "5 → 6") — **record only; no score change** |
| **V13-b** | ≥ 200,000 | run **ends** — **record only; no score change.** Only band C (→ 3), §5d R13-c (→ 2) or T-01/T-02 move v13 |

## §5c — CONTINUING CLAIMS, w/e Oct 31 — v7 run **record-only** (v7 at 2)

Current **1,718,000** [w/e Oct 24]; `1,750,000 − 1,718,000 = 32,000` inside.

<!-- partition-axis: column="Continuing claims" -->
| Band | Continuing claims | Assignment |
|---|---|---|
| **CC-1** | < 1,750,000 | run extends by one week on the revised run, counted at the print — **record only; no score change** |
| **CC-2** | ≥ 1,750,000 | run **ends** — **record only; no score change.** No v7 return letter exists (DECIDED 10/21, KB-LAB-218) |

⚠️ CC is a cost/duration gauge, not early warning.

## §5d — v13 RETURN LETTER R13-c *(adopted 10/21, KB-LAB-218; REGENERATED)*

`rel = MA_published(w/e Nov 7) / min(published 4-week MA over the 52 weeks before w/e Nov 7)` — **recompute the minimum on the vintage at grade time** (the DOL 53-week table, or FRED IC4WSA). Illustration on the 11/5 vintage: min **194,750 (w/e Oct 31)** ⇒ bar `1.15 × 194,750 = 223,962.5` ⇒ needs `(579,000 + X)/4 ≥ 223,962.5` ⇒ `X ≥ 895,850 − 579,000 = 316,850`, i.e. **`X ≥ 317,000`** on DOL's whole-thousand grid (inside band E).

| R13 | rel (formula axis — the level is an illustration, L-27) | Pre-committed assignment |
|---|---|---|
| **R13-a** | rel ≥ 1.15 | **v13 1 → 2.** If §2 bands C/D/E also fire, the HIGHER v13 assignment governs; R13-c never lowers a score |
| **R13-b** | rel < 1.15 | no action |

---

## §6 — MECHANISM vs THRESHOLD — **no prediction resolves or is registered on this card.** Every band is a threshold/counter call.

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

🧾 **Checker receipt at freeze (2026-11-05 14:06 EST, `card_partition_check.py`, rc=2):** `GRADING_CARD_20261112_claims.md: 7 band table(s) — 1 verified, 6 unverified, 0 with defects` · `[✓] table 2: VERIFIED — axis 'Initial claims, single print', 5 bands, precision 1,000, bounds as written`. Tables 1 and 3 are §1's inputs and §3's worked points, not band tables; tables 4–7 hand-proved below (BD-31 one-declaration limit). ⛔ `UNVERIFIED` is not a pass; **freeze authorized on `0 defects` + the hand proof.** Arithmetic of §3/§5a/§5d re-run in python at freeze: every figure reproduced.

| Table | Complement holds because |
|---|---|
| §5a T-01 | `≤ 421,000` / `≥ 422,000` — whole-thousand grid only; `421,000 → MA (579,000 + 421,000)/4 = 250,000` is not `> 250,000` |
| §5b v13 | `≤ 199,000` / `≥ 200,000` — exhaustive on DOL's whole-thousand grid only |
| §5c CC | `< 1,750,000` / `≥ 1,750,000` — true complement at any precision |
| §5d R13-c | `rel ≥ 1.15` / `rel < 1.15` — true complement at any precision |

## §9 — GRADE (write 2026-11-12 off this frozen card — never re-read a band)

*Blank until print. Order: ① regenerate the four §4 quantities on the as-published vintage · ② grade §2 · §5a · §5b · §5c · §5d separately · ③ write into `STATUS.md` (KEY THRESHOLDS, matrix v13 if band C+ or R13-a, score, calendar) · ④ `git mv` to `docket/graded/` and build the 11/19 card the same session.*
