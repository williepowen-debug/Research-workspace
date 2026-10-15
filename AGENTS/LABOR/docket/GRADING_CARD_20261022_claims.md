# 🔒 FROZEN GRADING CARD — Initial Claims w/e Oct 17, 2026

**Print:** Thu **2026-10-22, 08:30 ET** — initial claims w/e **Oct 17** (+ continuing claims w/e **Oct 10**).
**Frozen:** 2026-10-15 08:32 ET, **in the session that graded the 10/15 card** (C2a recurring-print trigger) — **7 days ahead of the print.** PROME-spawned session (prome-73, WQ-184 Tier-1 due-row wake + crash recovery).
**Built from:** `docket/TEMPLATE_claims_card.md` + the 10/15 card (now `docket/graded/GRADING_CARD_20261015_claims.md`). **§1 · §3 · §5a REGENERATED from the 10/15 as-published window; §5b/§5c streak counts regenerated; §2 · §4 · §6 · §7 bands carried (no STATUS band changed on 10/15).**
**Why a card is owed:** multi-loaded — **T-01, T-02, vector 13 (band C re-escalation), Kill B**, plus CARL's kill-rule leg 1.

> 🔴 **No letter returns v13 1 → 2 or v7 2 → 3** (STATUS pickup 2, RE-PARKED to a non-print-day session 10/16–10/21). If that session writes a return letter effective from this print, it enters this card as a dated **AMENDMENT** block before 10/22 08:30 ET — never by editing a band in place; without one, the absent cell stays absent (L-27). **On this print the only score-moving axes are §2 bands C/D/E and §5a T-01.** §5b and §5c are **record-only**.
> ⚠️ **`R` is 198,000** (w/e Sep 19). Same `R` value as last week (198,000) but a different week (w/e Sep 19, not Sep 12). The retained trio is now `199,000 + 198,000 + 199,000 = 596,000`, so a 199,000 repeat moves the MA **+250** again; the zero-change print is 198,000.

---

## §1 — INPUTS FROZEN AT CURRENT VINTAGE *(REGENERATED from the DOL release of 2026-10-15 08:30 ET — AS-PUBLISHED vintage; KB-LAB-217)*

| Series | Value | Obs week | Source |
|---|---|---|---|
| Initial claims, latest (`W4`) | **199,000** | w/e 2026-10-10 | DOL/ETA advance release 2026-10-15 [CONF] (PDF text-extracted) |
| 4-week window `W1/W2/W3/W4` | **198,000 / 199,000 / 198,000 / 199,000** | w/e Sep 19 · Sep 26 · Oct 3 · Oct 10 | DOL 2026-10-15 (53-week SA table + summary table) |
| 4-week MA (`MA_cur`) | **198,500** | w/e 2026-10-10 | DOL 2026-10-15 |
| Continuing claims (`CC_cur`) | **1,710,000** | w/e 2026-10-03 | DOL 2026-10-15 |
| Kill B (`n_kb`) | **0 of 5** | — | STATUS |
| v13 `<200,000` streak (record-only) | **5** (Sep 12 · Sep 19 · Sep 26 · Oct 3 · Oct 10) — v13 at floor 1 | — | graded 10/15 |
| v7 CC `<1,750,000` streak (record-only) | **5** (Sep 5 · Sep 12 · Sep 19 · Sep 26 · Oct 3) — v7 at 2 | — | graded 10/15 |

**Reconciliation (division written):** `(198,000 + 199,000 + 198,000 + 199,000) / 4 = 794,000 / 4 = 198,500` ✅ **equals the published MA exactly.**
**Vintage note:** the 10/15 print revised w/e Oct 3 197,000 → **198,000** (initial) and w/e Sep 26 CC 1,716,000 → **1,714,000**. FRED ICSA/CCSA had **not** updated at 08:31 ET — §1 is built from the DOL primary only. Expect `W4` (199,000) to revise at the 10/22 print.

---

## §2 — PRE-COMMITTED BANDS *(carried verbatim — no STATUS band changed on 10/15)*

<!-- partition-axis: column="Initial claims, single print" -->
| Band | Initial claims, single print | Pre-committed assignment |
|---|---|---|
| **A** | ≤ 185,000 | **Kill B leg** — count 0 → 1 of 5 |
| **B** | 186,000 – 229,000 | **NO ACTION** (drift band, `<230,000`) |
| **C** | 230,000 – 250,000 | **Accelerating** — vector 13: 1 → **3** (KEY THRESHOLDS letter "230–250K accelerating (v13 → 3)") |
| **D** | 251,000 – 300,000 | **ARM T-01 provisional** (confirm on a 2nd consecutive `>250,000`) |
| **E** | ≥ 301,000 | 🔴 **T-02 FIRE** → REGINALD (all ORANGE→RED) + HENRY |

**Distances from the 199,000 base:** T-01 `250,000 − 198,500 = 51,500` on the MA basis; T-02 `300,000 − 199,000 = 101,000` to the bar; the first firing print (band E, 301,000) is `102,000` away; band C's floor is `230,000 − 199,000 = 31,000` away. Band B is modal.

---

## §3 — 🔴 THE MECHANICAL-DECLINE TRAP, PRE-COMPUTED *(REGENERATED)*

Rolling off: **w/e Sep 19 = 198,000** (`R = 198,000`).

`MA_next(X) = (199,000 + 198,000 + 199,000 + X)/4 = (596,000 + X)/4` ⚠️ **[VINTAGE-DEPENDENT — moves if ANY retained week revises]**
**`ΔMA(X) = (596,000 + X)/4 − 794,000/4 = (X − 198,000)/4`** ✅ **[depends only on `R`]**

`R = 198,000` lies inside band B, so band B is **cut** by the zero-change line: prints 186,000–197,000 lower the MA, 198,000 leaves it unchanged, 199,000–229,000 raise it. Bands C, D, E lie wholly above `R` (MA rises); band A wholly below (MA falls).

| Worked point (not a band) | `X` | `MA_next` ⚠️ | `ΔMA` ✅ |
|---|---|---|---|
| Kill-B edge | 185,000 | `781,000/4 = 195,250` | −3,250 |
| **Modal — a 199,000 repeat** | 199,000 | `795,000/4 = 198,750` | +250 |
| **Zero-change point** | 198,000 | `794,000/4 = 198,500` | **0** |
| Accelerating edge | 230,000 | `826,000/4 = 206,500` | +8,000 |
| T-02 edge | 301,000 | `897,000/4 = 224,250` | +25,750 |

🔴 **READING RULE (carried, conditional form):** a falling MA on a band-B print is **mechanical**. I will describe the MA move only from the **as-published** MA and the regenerated `ΔMA`, never from this table's `MA_next` column (the `MA_next` column has rotted with the retained-week revisions on most recent cards while `ΔMA` stayed exact — L-31).

---

## §4 — WHAT THIS PRINT DOES **NOT** DO *(carried; WARN line regenerated)*

- A single weekly print is a realization gauge, not a demand-vs-supply discriminator.
- **A benign print is not hawkish fuel — it is nothing.** Rate path → BOND, HENRY, ORACLE.
- 🔴 **REVISION JITTER (L-02), THREE quantities regenerated BEFORE reading the level:** ① `ΔMA` (moves only if `R` revises) · ② `MA_next` column · ③ §5a bound. The BANDS key on fixed levels and are unaffected.
- ⛔ **No WARN cohort is registered for w/e Oct 17.** Nearest registered: Trinity Health 557 (`[2ND]`, eff ~10/25 ⇒ w/e Oct 31), Oracle ~800 (eff 11/13 ⇒ w/e Nov 14), Workday 142 (`[CONF EDD]`, eff 11/30 ⇒ w/e Dec 5). Netflix ~1,000 global (KB-LAB-209): no CA EDD notice found through 10/07. L-08: largest `800 / 20,000 = 4.0%` of the national floor — state-level only, no national attribution in either direction.
- ⚠️ **A streak break is not an escalation.** A `≥200,000` print in band B ends the v13 `<200,000` streak and moves **no** score (§5b). Do not read the end of a streak as news.
- 📅 **Shutdown risk is not on this print:** the CR expiry that would halt the weekly release is **Dec 11** (STATUS calendar). A missing release on 10/22 is graded UNKNOWN, never as a band.

---

## §5a — 🔴 T-01 ON THE **MA BASIS** — re-solved

`X > 1,000,000 − (W2+W3+W4) = 1,000,000 − 596,000` ⇒ **`X > 404,000`.** `404,000 → MA 250,000` (does **not** fire) · `405,000 → MA 250,250` (**fires**). ⚠️ Void the moment the window revises — re-solve at the print.

<!-- partition-axis: column="Initial claims, single print (T-01 MA axis)" -->
| T01 | Initial claims, single print (T-01 MA axis) | Pre-committed assignment |
|---|---|---|
| **T01-a** | ≤ 404,000 | MA ≤ 250,000 ⇒ **T-01 does NOT fire.** Bound re-solved at the print |
| **T01-b** | ≥ 405,000 | 🔴 **T-01 FIRES on the MA basis** → CARL + REGINALD, in addition to band E's T-02 |

## §5b — VECTOR-13 `<200,000` STREAK — **record-only** (v13 at floor 1)

<!-- partition-axis: column="Initial claims, single print (vector-13 axis)" -->
| V13 | Initial claims, single print (vector-13 axis) | Pre-committed assignment |
|---|---|---|
| **V13-a** | ≤ 199,000 | streak 5 → 6 (on the revised trailing run) — **record only; no score change** (v13 already at its floor, 1) |
| **V13-b** | ≥ 200,000 | streak **ends** — **record only; no score change.** No registered letter returns v13 1 → 2; only band C (→ 3) or T-01/T-02 move it |

## §5c — CONTINUING CLAIMS, w/e Oct 10 — v7 streak **record-only** (v7 at 2)

Current **1,710,000** [w/e Oct 3]; `1,750,000 − 1,710,000 = 40,000` inside.

<!-- partition-axis: column="Continuing claims" -->
| Band | Continuing claims | Assignment |
|---|---|---|
| **CC-1** | < 1,750,000 | streak 5 → 6 — **record only; no score change** |
| **CC-2** | ≥ 1,750,000 | streak **ends** — **record only; no score change.** No registered letter returns v7 2 → 3 (STATUS pickup 2, RE-PARKED) |

⚠️ CC is a cost/duration gauge, not early warning.

---

## §6 — MECHANISM vs THRESHOLD — **no prediction resolves or is registered on this card.** Every band is a threshold/counter call.

## §7 — ROUTING *(carried)*

| Outcome | Route | Priority |
|---|---|---|
| Band E | **WALTER** → REGINALD (all ORANGE→RED), HENRY — + CARL if ≥ §5a bound | 🔴 |
| Band D | **WALTER** → CARL, REGINALD | 🟠 |
| Band C (v13 1 → 3) | STATUS score + NEXUS brief; **direct 🟡 note to CARL** (its kill-rule leg 1 reads claims) | 🟡 |
| Bands A / B | STATUS only | — |
| §5b / §5c streak changes | STATUS only — record, not a signal | — |

---

## §8 — CHECKER SCOPE AT FREEZE (BD-31)

🧾 **Checker receipt at freeze (2026-10-15 08:33 ET, `card_partition_check.py`, rc=2):** `GRADING_CARD_20261022_claims.md: 6 band table(s) — 1 verified, 5 unverified, 0 with defects` · `[✓] table 2: VERIFIED — axis 'Initial claims, single print', 5 bands, precision 1,000, bounds as written` · tables 1, 3–6 `[BAD-DECLARATION]` = the BD-31 one-declaration limit. **Table 1 is §1's inputs table and table 3 is §3's worked-point table — neither is a band table** (no assignment column). Tables 4–6 hand-proved below. ⛔ `UNVERIFIED` is not a pass; **freeze authorized on `0 defects` + the hand proof.**

| Table | Complement holds because |
|---|---|
| §5c CC | `< 1,750,000` / `≥ 1,750,000` — true complement at any precision |
| §5b v13 | `≤ 199,000` / `≥ 200,000` — exhaustive on DOL's whole-thousand grid only |
| §5a T-01 | `≤ 404,000` / `≥ 405,000` — whole-thousand grid only; `404,000 → MA 250,000` is not `> 250,000` |

---

## §9 — GRADE (write 2026-10-22 off this frozen card — never re-read a band)

*Blank until print. Order: ① regenerate the three §4 quantities on the as-published vintage · ② grade §2 · §5a · §5b · §5c separately · ③ write into `STATUS.md` (KEY THRESHOLDS, matrix v13 if band C+, score, calendar) · ④ `git mv` to `docket/graded/` and build the 10/29 card the same session.*
