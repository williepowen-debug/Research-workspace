# 🔒 FROZEN GRADING CARD — Initial Claims w/e Oct 24, 2026

**Print:** Thu **2026-10-29, 08:30 ET** — initial claims w/e **Oct 24** (+ continuing claims w/e **Oct 17**).
**Frozen:** 2026-10-22 08:4x ET, **in the session that graded the 10/22 card** (C2a recurring-print trigger) — **7 days ahead of the print.** PROME-spawned session (84affa50, WQ-479 A / WQ-184 Tier-1 due-row wake DOCKET L719).
**Built from:** `docket/TEMPLATE_claims_card.md` + the 10/22 card (now `docket/graded/GRADING_CARD_20261022_claims.md`). **§1 · §3 · §5a · §5d REGENERATED from the 10/22 as-published window; §5b/§5c counts regenerated; §2 · §4 · §6 · §7 bands carried (no STATUS band changed on 10/22).** §5d carries the R13-c return letter adopted 10/21 (10/22 card §8a) as a regenerated band.
**Why a card is owed:** multi-loaded — **T-01, T-02, vector 13 (band C re-escalation + R13-c return), Kill B**, plus CARL's kill-rule leg 1.

> 🔴 **On this print the score-moving axes are §2 bands C/D/E, §5a T-01 and §5d R13-c** (higher v13 assignment governs; R13-c never lowers a score). §5b and §5c are **record-only**; v7 has **no** return letter (decided 10/21).
> ⚠️ **`R` is 199,000** (w/e Sep 26). The retained trio is `198,000 + 200,000 + 194,000 = 592,000`, so a 194,000 repeat moves the MA **−1,250**; the zero-change print is 199,000.

---

## §1 — INPUTS FROZEN AT CURRENT VINTAGE *(REGENERATED from the DOL release of 2026-10-22 08:30 ET — AS-PUBLISHED vintage; KB-LAB-221)*

| Series | Value | Obs week | Source |
|---|---|---|---|
| Initial claims, latest (`W4`) | **194,000** | w/e 2026-10-17 | DOL/ETA advance release 2026-10-22 [CONF] (PDF text-extracted); FRED ICSA agrees (fredgraph 08:34 ET) |
| 4-week window `W1/W2/W3/W4` | **199,000 / 198,000 / 200,000 / 194,000** | w/e Sep 26 · Oct 3 · Oct 10 · Oct 17 | DOL 2026-10-22 (53-week SA table + summary table) |
| 4-week MA (`MA_cur`) | **197,750** | w/e 2026-10-17 | DOL 2026-10-22; FRED IC4WSA agrees |
| Continuing claims (`CC_cur`) | **1,728,000** | w/e 2026-10-10 | DOL 2026-10-22 (FRED CCSA lagged at 08:34 ET) |
| Kill B (`n_kb`) | **0 of 5** | — | STATUS |
| v13 `<200,000` run (record-only) | **1** (Oct 17) — the run was cut by the w/e Oct 10 revision to 200,000 · v13 at floor 1 | — | graded 10/22 |
| v7 CC `<1,750,000` run (record-only) | **6** (Sep 5 · Sep 12 · Sep 19 · Sep 26 · Oct 3 · Oct 10) — v7 at 2 | — | graded 10/22 |

**Reconciliation (division written):** `(199,000 + 198,000 + 200,000 + 194,000) / 4 = 791,000 / 4 = 197,750` ✅ **equals the published MA exactly.**
**Vintage note:** the 10/22 print revised w/e Oct 10 199,000 → **200,000** (initial) and w/e Oct 3 CC 1,710,000 → **1,703,000**. Expect `W4` (194,000) to revise at the 10/29 print.

---

## §2 — PRE-COMMITTED BANDS *(carried verbatim — no STATUS band changed on 10/22)*

<!-- partition-axis: column="Initial claims, single print" -->
| Band | Initial claims, single print | Pre-committed assignment |
|---|---|---|
| **A** | ≤ 185,000 | **Kill B leg** — count 0 → 1 of 5 |
| **B** | 186,000 – 229,000 | **NO ACTION** (drift band, `<230,000`) |
| **C** | 230,000 – 250,000 | **Accelerating** — vector 13: 1 → **3** (KEY THRESHOLDS letter "230–250K accelerating (v13 → 3)") |
| **D** | 251,000 – 300,000 | **ARM T-01 provisional** (confirm on a 2nd consecutive `>250,000`) |
| **E** | ≥ 301,000 | 🔴 **T-02 FIRE** → REGINALD (all ORANGE→RED) + HENRY |

**Distances from the 194,000 base:** T-01 `250,000 − 197,750 = 52,250` on the MA basis; T-02 `300,000 − 194,000 = 106,000` to the bar; the first firing print (band E, 301,000) is `107,000` away; band C's floor is `230,000 − 194,000 = 36,000` away; Kill B's edge is `194,000 − 185,000 = 9,000` below. Band B is modal.

---

## §3 — 🔴 THE MECHANICAL-DECLINE TRAP, PRE-COMPUTED *(REGENERATED)*

Rolling off: **w/e Sep 26 = 199,000** (`R = 199,000`).

`MA_next(X) = (198,000 + 200,000 + 194,000 + X)/4 = (592,000 + X)/4` ⚠️ **[VINTAGE-DEPENDENT — moves if ANY retained week revises]**
**`ΔMA(X) = (592,000 + X)/4 − 791,000/4 = (X − 199,000)/4`** ✅ **[depends only on `R`]**

`R = 199,000` lies inside band B, so band B is **cut** by the zero-change line: prints 186,000–198,000 lower the MA, 199,000 leaves it unchanged, 200,000–229,000 raise it. Bands C, D, E lie wholly above `R` (MA rises); band A wholly below (MA falls).

| Worked point (not a band) | `X` | `MA_next` ⚠️ | `ΔMA` ✅ |
|---|---|---|---|
| Kill-B edge | 185,000 | `777,000/4 = 194,250` | −3,500 |
| **Modal — a 194,000 repeat** | 194,000 | `786,000/4 = 196,500` | −1,250 |
| **Zero-change point** | 199,000 | `791,000/4 = 197,750` | **0** |
| Accelerating edge | 230,000 | `822,000/4 = 205,500` | +7,750 |
| T-02 edge | 301,000 | `893,000/4 = 223,250` | +25,500 |

🔴 **READING RULE (carried, conditional form):** a falling MA on a band-B print is **mechanical**. I will describe the MA move only from the **as-published** MA and the regenerated `ΔMA`, never from this table's `MA_next` column (that column has rotted with retained-week revisions five weeks running while `ΔMA` stayed exact — L-31).

---

## §4 — WHAT THIS PRINT DOES **NOT** DO *(carried; WARN line regenerated)*

- A single weekly print is a realization gauge, not a demand-vs-supply discriminator.
- **A benign print is not hawkish fuel — it is nothing.** Rate path → BOND, HENRY, ORACLE. A new multi-year MA low (10/22: lowest since w/e 2022-10-01 on FRED's vintage) is a level fact, graded by no band.
- 🔴 **REVISION JITTER (L-02), FOUR quantities regenerated BEFORE reading the level:** ① `ΔMA` (moves only if `R` revises) · ② `MA_next` column · ③ §5a bound · ④ §5d's 52-week MA minimum. The §2 BANDS key on fixed levels and are unaffected.
- ⛔ **No WARN cohort is registered for w/e Oct 24.** Nearest registered: Trinity Health 557 (`[2ND]`, eff ~10/25 ⇒ w/e Oct 31), Oracle ~800 (eff 11/13 ⇒ w/e Nov 14), Workday 142 (`[CONF EDD]`, eff 11/30 ⇒ w/e Dec 5). L-08: largest `800 / 20,000 = 4.0%` of the national floor — state-level only, no national attribution in either direction.
- ⚠️ **A streak break is not an escalation.** §5b/§5c counts move no score.
- 📅 **Shutdown risk is not on this print:** CR expiry **Dec 11**. A missing release on 10/29 is graded UNKNOWN, never as a band.

---

## §5a — 🔴 T-01 ON THE **MA BASIS** — re-solved

`X > 1,000,000 − (W2+W3+W4) = 1,000,000 − 592,000` ⇒ **`X > 408,000`.** `408,000 → MA 250,000` (does **not** fire) · `409,000 → MA 250,250` (**fires**). ⚠️ Void the moment the window revises — re-solve at the print.

<!-- partition-axis: column="Initial claims, single print (T-01 MA axis)" -->
| T01 | Initial claims, single print (T-01 MA axis) | Pre-committed assignment |
|---|---|---|
| **T01-a** | ≤ 408,000 | MA ≤ 250,000 ⇒ **T-01 does NOT fire.** Bound re-solved at the print |
| **T01-b** | ≥ 409,000 | 🔴 **T-01 FIRES on the MA basis** → CARL + REGINALD, in addition to band E's T-02 |

## §5b — VECTOR-13 `<200,000` RUN — **record-only** (v13 at floor 1)

<!-- partition-axis: column="Initial claims, single print (vector-13 axis)" -->
| V13 | Initial claims, single print (vector-13 axis) | Pre-committed assignment |
|---|---|---|
| **V13-a** | ≤ 199,000 | run extends by one week **on the revised trailing run, counted at the print** (the count is NOT pre-written: a retained-week revision cut the 10/22 card's pre-written "5 → 6") — **record only; no score change** |
| **V13-b** | ≥ 200,000 | run **ends** — **record only; no score change.** Only band C (→ 3), §5d R13-c (→ 2) or T-01/T-02 move v13 |

## §5c — CONTINUING CLAIMS, w/e Oct 17 — v7 run **record-only** (v7 at 2)

Current **1,728,000** [w/e Oct 10]; `1,750,000 − 1,728,000 = 22,000` inside.

<!-- partition-axis: column="Continuing claims" -->
| Band | Continuing claims | Assignment |
|---|---|---|
| **CC-1** | < 1,750,000 | run extends by one week on the revised run, counted at the print — **record only; no score change** |
| **CC-2** | ≥ 1,750,000 | run **ends** — **record only; no score change.** No v7 return letter exists (DECIDED 10/21, KB-LAB-218) |

⚠️ CC is a cost/duration gauge, not early warning.

## §5d — v13 RETURN LETTER R13-c *(adopted 10/21, KB-LAB-218; REGENERATED)*

`rel = MA_published(w/e Oct 24) / min(published 4-week MA over the 52 weeks before w/e Oct 24)` — **recompute the minimum on the vintage at grade time** (the DOL 53-week table, or FRED IC4WSA). Illustration on the 10/22 vintage: min **197,750 (w/e Oct 17)** ⇒ bar `1.15 × 197,750 = 227,412.5` ⇒ needs `(592,000 + X)/4 ≥ 227,412.5` ⇒ `X ≥ 317,650`, i.e. **`X ≥ 318,000`** on DOL's whole-thousand grid (inside band E).

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

🧾 **Checker receipt at freeze (2026-10-22 08:37 ET, `card_partition_check.py`, rc=2):** `GRADING_CARD_20261029_claims.md: 7 band table(s) — 1 verified, 6 unverified, 0 with defects` · `[✓] table 2: VERIFIED — axis 'Initial claims, single print', 5 bands, precision 1,000, bounds as written` · tables 1, 3–7 `[BAD-DECLARATION]` = the BD-31 one-declaration limit. **Table 1 is §1's inputs table and table 3 is §3's worked-point table — neither is a band table** (no assignment column). Tables 4–7 hand-proved below. ⛔ `UNVERIFIED` is not a pass; **freeze authorized on `0 defects` + the hand proof.**

| Table | Complement holds because |
|---|---|
| §5a T-01 | `≤ 408,000` / `≥ 409,000` — whole-thousand grid only; `408,000 → MA (592,000 + 408,000)/4 = 250,000` is not `> 250,000` |
| §5b v13 | `≤ 199,000` / `≥ 200,000` — exhaustive on DOL's whole-thousand grid only |
| §5c CC | `< 1,750,000` / `≥ 1,750,000` — true complement at any precision |
| §5d R13-c | `rel ≥ 1.15` / `rel < 1.15` — true complement at any precision |

## §9 — GRADE (written 2026-10-29 off this frozen card — no band re-read)

**Primary:** DOL/ETA news release 2026-10-29 08:30 ET, `dol.gov/ui/data.pdf?release=20261029a`, fetched 09:02 ET by `scripts/fetch_primary.py` (bare curl, HTTP 200, 485,984 B, pdf; sha256 `1675cc12…82c7`); text-extracted with pdfminer (venv python — the system python lacks pdfminer, first extract returned UNKNOWN and was re-run, not waved through); embargo line *"8:30 A.M. (Eastern) Thursday, October 29, 2026"* checked; `--expect` 194,000 · 196,750 · 1,701,000 all FOUND verbatim; 53-week SA table read by column. Text saved: `domain/sources/2026-10-29_DOL_UI_claims_release_text.txt`. **FRED cross-check (fredgraph.csv, 09:02 ET):** ICSA obs 2026-10-24 194,000 · obs 2026-10-17 195,000; IC4WSA obs 2026-10-24 196,750; CCSA obs 2026-10-17 1,701,000 · obs 2026-10-10 1,722,000 — agree with DOL. KB-LAB-228.

**Prior-week revision (preserved, as published):** w/e Oct 17 initial **194,000 → 195,000** (+1,000); 4-wk MA w/e Oct 17 **197,750 → 198,000** (+250); CC w/e Oct 10 **1,728,000 → 1,722,000** (−6,000); CC 4-wk MA **1,711,000 → 1,709,500** (−1,500).

**① The four §4 quantities, regenerated on the as-published vintage:**

| Quantity | Card (10/22 vintage) | As-published 10/29 | Moved by |
|---|---|---|---|
| `ΔMA` | `(X − 199,000)/4` ⇒ at 194,000: **−1,250** | **−1,250** (`196,750 − 198,000`, DOL "decrease of 1,250 from the previous week's revised average") ✅ exact | nothing — `R` = 199,000 (w/e Sep 26) unrevised |
| `MA_next` | `(592,000 + 194,000)/4 = 196,500` | **196,750** — window `198,000 + 200,000 + 195,000 + 194,000 = 787,000`, `787,000 / 4 = 196,750` ✅ equals the published MA | the w/e Oct 17 revision (+1,000 ⇒ +250). Column rotted a sixth week; `ΔMA` exact again (L-31) |
| §5a T-01 bound | `X > 408,000` | **`X > 1,000,000 − 593,000 = 407,000`** | same revision |
| §5d 52-week MA minimum | 197,750 (w/e Oct 17) | **198,000 (w/e Oct 17, revised)** — lowest of the 52 published MAs before w/e Oct 24 in the 53-week table | same revision |

**② Grades, axis by axis:**

| Axis | Input | Band | Assignment |
|---|---|---|---|
| §2 single print | **194,000** (w/e Oct 24) | **B** (186,000–229,000) | **NO ACTION.** Kill B stays **0 of 5** (`194,000 − 185,000 = 9,000` above) |
| §5a T-01 MA basis | MA **196,750**; bound `X > 407,000` | **T01-a** | **T-01 does NOT fire** (`250,000 − 196,750 = 53,250` below) |
| §5b v13 `<200,000` run | 194,000 ≤ 199,000 | **V13-a** | run extends on the revised trailing run: w/e Oct 10 200,000 (breaks) · Oct 17 195,000 · Oct 24 194,000 ⇒ **run 2**, record-only, no score change |
| §5c CC w/e Oct 17 | **1,701,000** < 1,750,000 | **CC-1** | run extends on the revised run: Sep 5 1,717 · Sep 12 1,712 · Sep 19 1,699 · Sep 26 1,714 · Oct 3 1,703 · Oct 10 1,722 · Oct 17 1,701 (thousands) ⇒ **run 7**, record-only (`1,750,000 − 1,701,000 = 49,000` inside) |
| §5d R13-c | `rel = 196,750 / 198,000 = 0.99369` | **R13-b** (< 1.15) | **no action** — v13 stays **1** |

**Score:** unchanged — v13 1, v7 2, total **27/80**. No §7 route fires (bands A/B ⇒ STATUS only).

**Level facts graded by no band (§4):** the published MA 196,750 is the lowest 4-week MA on FRED's current IC4WSA vintage since **w/e 1969-10-18 (196,250)** — VERIFIED at fredgraph.csv 09:02 ET over 1967–2026; the 2022 low on this vintage is 197,500 (w/e 2022-09-24). ⚠️ A level, not a rate: covered employment is far larger than in 1969, so this is not "the tightest market since 1969," and a benign print is not hawkish fuel (§4). NSA initial 178,851 vs 203,012 a year earlier. IUR 1.1% SA unchanged.
**Anomaly, recorded not graded:** DOL's state text lists **Illinois at a 13.1% insured unemployment rate** for w/e Oct 10 (10/22 release: Illinois 1.3%). The national unadjusted IUR is 1.0% unchanged and national CC fell, so this is a state-table artifact (INFERRED — a decimal or covered-employment reporting error), not a national signal. Watch whether DOL corrects it next week.
**WARN:** no registered cohort for w/e Oct 24 (as §4 pre-stated) — nothing attributed.

**③ Written into `STATUS.md`** (header, KEY THRESHOLDS claims + CC rows, matrix v13 + v7 live-state text, EXIT RULES Kill B + break-confirm, calendar) 2026-10-29. **④** card `git mv` → `docket/graded/` this session; 11/5 card built from `TEMPLATE_claims_card.md` this session.
