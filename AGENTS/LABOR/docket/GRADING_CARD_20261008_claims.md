# 🔒 FROZEN GRADING CARD — Initial Claims w/e Oct 3, 2026

**Print:** Thu **2026-10-08, 08:30 ET** — initial claims w/e **Oct 3** (+ continuing claims w/e **Sep 26**).
**Frozen:** 2026-10-01 12:20 ET, **in the session that graded the 10/1 card** (C2a recurring-print trigger) — **7 days ahead of the print.** PROME-spawned session (`prome-0c` slate, WQ-184).
**Built from:** the 10/1 card (now `docket/graded/GRADING_CARD_20261001_claims.md`). **§1 · §3 · §5a · §5b/§5c counts REGENERATED from the 10/1 as-published window; §2 · §4 · §6 · §7 bands carried (no STATUS threshold changed on 10/1).**
**Why a card is owed:** multi-loaded — **T-01, T-02, vector 13, vector 7, Kill B**, plus CARL's kill-rule leg 1. (LAB-03 resolved 10/1 — no prediction rides this print.)

> 🔴 **TWO COUNTERS SIT AT 3 OF 4 — THIS PRINT CAN MOVE THE SCORE.** A print `≤199,000` (on an unrevised-or-still-qualifying run) completes **vector 13 → 4 of 4 ⇒ v13 2 → 1**; continuing claims `<1,750,000` for w/e Sep 26 completes **vector 7 → 4 of 4 ⇒ v7 3 → 2**. Both together ⇒ **28 → 26/75.** Said now so neither is read as news on the day: these are the pre-registered drop letters of `STATUS.md` (v13 `<200K ×4 → drop to 1`; v7 `CC <1,750K ×4 → drop to 2`), executed, not argued with.
> ⚠️ **`R` is 207,000 AGAIN** (w/e Sep 5) — same mechanical term as last week, `(X − 207,000)/4`, but the retained trio changed (603,000 → 593,000), so `MA_next` and the T-01 bound both moved.

---

## §1 — INPUTS FROZEN AT CURRENT VINTAGE *(REGENERATED from the DOL release of 2026-10-01 08:30 ET — AS-PUBLISHED vintage; KB-LAB-200)*

| Series | Value | Obs week | Source |
|---|---|---|---|
| Initial claims, latest (`W4`) | **197,000** | w/e 2026-09-26 | DOL/ETA advance release 2026-10-01 [CONF] (PDF text-extracted) |
| 4-week window `W1/W2/W3/W4` | **207,000 / 198,000 / 198,000 / 197,000** | w/e Sep 5 · Sep 12 · Sep 19 · Sep 26 | DOL 2026-10-01; FRED ICSA agrees |
| 4-week MA (`MA_cur`) | **200,000** | w/e 2026-09-26 | DOL 2026-10-01 |
| Continuing claims (`CC_cur`) | **1,701,000** | w/e 2026-09-19 | DOL 2026-10-01; FRED CCSA agrees |
| Kill B (`n_kb`) | **0 of 5** | — | STATUS |
| Vector-7 (`n_v7`) | **3 of 4** (Sep 5 1,717,000 · Sep 12 1,712,000 rev · Sep 19 1,701,000) | — | graded 10/1 |
| Vector-13 (`n_v13`) | **3 of 4** (Sep 12 198,000 · Sep 19 198,000 rev · Sep 26 197,000) | — | graded 10/1 |

**Reconciliation (division written):** `(207,000 + 198,000 + 198,000 + 197,000) / 4 = 800,000 / 4 = 200,000` ✅ **equals the published MA exactly.**
**Vintage note:** the 10/1 print revised w/e Sep 19 197,000 → 198,000 (initial) and w/e Sep 12 CC 1,719,000 → 1,712,000. Expect `W4` (and possibly an older week — 9/24 revised a two-weeks-back week) to move at the 10/8 print.

---

## §2 — PRE-COMMITTED BANDS *(carried verbatim — no STATUS threshold changed on 10/1)*

<!-- partition-axis: column="Initial claims, single print" -->
| Band | Initial claims, single print | Pre-committed assignment |
|---|---|---|
| **A** | ≤ 185,000 | **Kill B leg 1 of 5** — count 0 → 1 |
| **B** | 186,000 – 229,000 | **NO ACTION** (drift band, `<230,000`) |
| **C** | 230,000 – 250,000 | **Accelerating** — vector 13: 2 → **3** |
| **D** | 251,000 – 300,000 | **ARM T-01 provisional** (confirm on a 2nd consecutive `>250,000`) |
| **E** | ≥ 301,000 | 🔴 **T-02 FIRE** → REGINALD (all ORANGE→RED) + HENRY |

**Distances from the 197,000 base:** T-01 `250,000 − 200,000 = 50,000` on the MA basis; T-02 `300,000 − 197,000 = 103,000`. Band B is modal.

---

## §3 — 🔴 THE MECHANICAL-DECLINE TRAP, PRE-COMPUTED *(REGENERATED)*

Rolling off: **w/e Sep 5 = 207,000** (`R = 207,000`).

`MA_next(X) = (198,000 + 198,000 + 197,000 + X)/4 = (593,000 + X)/4` ⚠️ **[VINTAGE-DEPENDENT — moves if ANY retained week revises]**
**`ΔMA(X) = (593,000 + X)/4 − 800,000/4 = (X − 207,000)/4`** ✅ **[depends only on `R`]**

| Worked point (not a band) | `X` | `MA_next` ⚠️ | `ΔMA` ✅ |
|---|---|---|---|
| Kill-B edge | 185,000 | `778,000/4 = 194,500` | −5,500 |
| **Modal — a 197,000 repeat** | **197,000** | **`790,000/4 = 197,500`** | **−2,500** |
| **Zero-change point** | **207,000** | **200,000** | **0** |
| Accelerating edge | 230,000 | `823,000/4 = 205,750` | +5,750 |
| T-02 edge | 301,000 | `894,000/4 = 223,500` | +23,500 |

🔴 **READING RULE (carried):** a falling MA on a band-B print is **mechanical**. A 197,000 repeat takes the MA to **197,500 — below 200,000, entirely on the 207,000 roll-off.** I will report "MA below 200,000, mechanically" **only if the as-published MA is actually below 200,000** (the 10/1 lesson: a pre-written sentence about a vintage-dependent quantity rots with it).

---

## §4 — WHAT THIS PRINT DOES **NOT** DO *(carried)*

- A single weekly print is a realization gauge, not a demand-vs-supply discriminator.
- **A benign print is not hawkish fuel — it is nothing.** Rate path → BOND, HENRY, ORACLE.
- 🔴 **REVISION JITTER (L-02), THREE quantities regenerated BEFORE reading the level:** ① `ΔMA` (moves only if `R` revises) · ② `MA_next` column · ③ §5a bound. The BANDS key on fixed levels and are unaffected.
- ⛔ **No WARN cohort is registered for w/e Oct 3.** Oracle's Sep round (≈800 US) lands w/e Nov 14 (`800 / 197,000 = 0.4%` of a week — L-08, state-level only).
- 🟡 **Quarter-start week:** w/e Oct 3 contains the Oct-1 quarter turn; some states see new-benefit-year filing effects. **Colour only, no band, no attribution of a rise to it after the fact** (and none of a fall away from it).
- ⚠️ **10/2 NFP lands between this card's freeze and its print.** It moves no band here; a v2 freeze-thaw fire on 10/2 (see the NFP card) stands down vectors 4/6/7 **before** this print — if it fires, §5c's v7 assignment is graded and recorded but the vector is already stood down, and the grade says so.

---

## §5a — 🔴 T-01 ON THE **MA BASIS** — re-solved

`X > 1,000,000 − (W2+W3+W4) = 1,000,000 − 593,000` ⇒ **`X > 407,000`.** `407,000 → MA 250,000` (does **not** fire) · `408,000 → MA 250,250` (**fires**). ⚠️ Void the moment the window revises.

<!-- partition-axis: column="Initial claims, single print (T-01 MA axis)" -->
| T01 | Initial claims, single print (T-01 MA axis) | Pre-committed assignment |
|---|---|---|
| **T01-a** | ≤ 407,000 | MA ≤ 250,000 ⇒ **T-01 does NOT fire.** Bound re-solved at the print |
| **T01-b** | ≥ 408,000 | 🔴 **T-01 FIRES on the MA basis** → CARL + REGINALD, in addition to band E's T-02 |

## §5b — VECTOR-13's `<200,000` COUNTER — **3 of 4**

**REVISED-VINTAGE COUNTING RULE (carried):** trailing run of consecutive weeks `<200,000` on the **10/8 as-published** vintage. Grade in order: ① read the revised w/e Sep 12 / Sep 19 / Sep 26 values; if any is now `≥200,000`, the run restarts after it · ② apply the table to `X`. ⚠️ **Margins: 2,000 / 2,000 / 3,000** — w/e Sep 19 already revised up 1,000 once.

<!-- partition-axis: column="Initial claims, single print (vector-13 axis)" -->
| V13 | Initial claims, single print (vector-13 axis) | Pre-committed assignment |
|---|---|---|
| **V13-a** | ≤ 199,000 | counter = (revised trailing run) + 1 — **4 of 4 if all three retained weeks still `<200,000` ⇒ v13 2 → 1 (score −1)**; otherwise the count as computed |
| **V13-b** | ≥ 200,000 | counter **RESETS to 0 of 4** |

## §5c — CONTINUING CLAIMS, w/e Sep 26 — vector 7 **3 of 4**

Current **1,701,000** [w/e Sep 19]; `1,750,000 − 1,701,000 = 49,000` inside. Same revised-vintage rule as §5b over w/e Sep 5 / 12 / 19.

<!-- partition-axis: column="Continuing claims" -->
| Band | Continuing claims | Assignment |
|---|---|---|
| **CC-1** | < 1,750,000 | count = (revised trailing run) + 1 — **4 of 4 if the three retained weeks still `<1,750,000` ⇒ v7 3 → 2 (score −1)** |
| **CC-2** | ≥ 1,750,000 | count **RESETS to 0 of 4** |

⚠️ CC is a cost/duration gauge, not early warning. Its drop is a pre-registered de-escalation letter, executed as written.

---

## §6 — MECHANISM vs THRESHOLD — **no prediction resolves or is registered on this card.** Every band is a threshold/counter call.

## §7 — ROUTING *(carried, + the two counter completions)*

| Outcome | Route | Priority |
|---|---|---|
| Band E | **WALTER** → REGINALD (all ORANGE→RED), HENRY — + CARL if ≥ §5a bound | 🔴 |
| Band D | **WALTER** → CARL, REGINALD | 🟠 |
| Band C | STATUS + brief | 🟡 |
| Bands A / B | STATUS only | — |
| **V13-a completes 4 of 4 (v13 → 1) and/or CC-1 completes 4 of 4 (v7 → 2)** | STATUS score + NEXUS brief; **direct 🟡 note to CARL** (its kill-rule leg 1 reads claims) — a de-escalation is not a WALTER signal | 🟡 |

---

## §8 — CHECKER SCOPE AT FREEZE (BD-31)

🧾 **Checker receipt at freeze (2026-10-01 12:20 ET, `card_partition_check.py`, rc=2):** `GRADING_CARD_20261008_claims.md: 5 band table(s) — 1 verified, 4 unverified, 0 with defects` · `[✓] table 2: VERIFIED — axis 'Initial claims, single print', 5 bands, precision 1,000, bounds as written` · tables 3–6 `[BAD-DECLARATION]` = the BD-31 one-declaration limit. **Table 3 is §3's worked-point table — not a band table** (no assignment column). Tables 4–6 hand-proved below. ⛔ `UNVERIFIED` is not a pass; **freeze authorized on `0 defects` + the hand proof.**

| Table | Complement holds because |
|---|---|
| §5c CC | `< 1,750,000` / `≥ 1,750,000` — true complement at any precision |
| §5b v13 | `≤ 199,000` / `≥ 200,000` — exhaustive on DOL's whole-thousand grid only |
| §5a T-01 | `≤ 407,000` / `≥ 408,000` — whole-thousand grid only; `407,000 → MA 250,000` is not `> 250,000` |

---

## §9 — GRADE (write 2026-10-08 off this frozen card — never re-read a band)

*Blank until print. Order: ① regenerate the three §4 quantities on the as-published vintage · ② apply the revised-vintage rule, grade §2 · §5a · §5b · §5c separately · ③ write into `STATUS.md` (KEY THRESHOLDS, matrix v7/v13, score, calendar) · ④ `git mv` to `docket/graded/` and build the 10/15 card the same session.*
