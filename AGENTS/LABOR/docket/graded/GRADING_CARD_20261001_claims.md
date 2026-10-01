# 🔒 FROZEN GRADING CARD — Initial Claims w/e Sep 26, 2026

**Print:** Thu **2026-10-01, 08:30 ET** — initial claims w/e **Sep 26** (+ continuing claims w/e **Sep 19**).
**Frozen:** 2026-09-24 14:5x ET, **in the session that graded the 9/24 card** — C2a's recurring-print trigger. **7 days ahead of the print.**
**Built from:** the 9/24 card's structure (itself built from `docket/TEMPLATE_claims_card.md`). **§1 · §3 · §5a REGENERATED from the 9/24 as-published window; §2 · §4 · §5b · §5c bands · §6 · §7 carried (no STATUS threshold changed on 9/24). Counters carried: v13 2 of 4 · v7 2 of 4.** 🆕 **§5b/§5c now carry an explicit REVISED-VINTAGE counting rule** (written because the 9/24 print revised the streak's first week up 2,000).
**Why a card is owed:** multi-loaded — **T-01, T-02, vector 13, vector 7, Kill B, LAB-03 (resolves at this print)**, plus CARL's kill-rule leg 1.

> 🔴 **THE ROLL-OFF WEEK CHANGED AGAIN: `R` moves 204,000 → 207,000.** Last card's term was `(X − 204,000)/4`; **this card's is `(X − 207,000)/4`.** On a **197,000 repeat** the MA move is **−2,500** (last week's 197,000 gave −1,750) — same print, `2,500/1,750 = 1.43×` larger, because a *larger* week rolls off. ⚠️ **And the T-01 bound moved 388,000 → 398,000** because a 197,000 replaced a 207,000 in the retained trio.

---

## §1 — INPUTS FROZEN AT CURRENT VINTAGE  *(REGENERATED from the DOL release of 2026-09-24 08:30 ET — the AS-PUBLISHED vintage)*

| Series | Value | Obs week | Source |
|---|---|---|---|
| Initial claims, latest (`W4`) | **197,000** | w/e 2026-09-19 | **DOL/ETA advance release 2026-09-24** [CONF] (PDF text-extracted) |
| 4-week window `W1/W2/W3/W4` (oldest→newest) | **207,000 / 207,000 / 198,000 / 197,000** | w/e Aug 29 · Sep 5 · Sep 12 · Sep 19 | DOL 2026-09-24 (+ r539cy for Aug 29) |
| 4-week MA (`MA_cur`) | **202,250** | w/e 2026-09-19 | DOL 2026-09-24 |
| Continuing claims (`CC_cur`) | **1,719,000** | w/e 2026-09-12 | DOL 2026-09-24 |
| Kill B count (`n_kb`) | **0 of 5** | — | STATUS § KEY THRESHOLDS |
| Vector-7 count (`n_v7`) | **2 of 4** (w/e Sep 5 1,717,000 rev · w/e Sep 12 1,719,000) | — | STATUS § KEY THRESHOLDS |
| Vector-13 count (`n_v13`) | **2 of 4** (w/e Sep 12 198,000 rev · w/e Sep 19 197,000) | — | STATUS § CONVERGENCE MATRIX v13 |

**Reconciliation (division written out):** `(207,000 + 207,000 + 198,000 + 197,000) / 4 = 809,000 / 4 = **202,250**` ✅ **equals the published 4-wk MA exactly.**

**Vintage note — TWO retained weeks revised at the 9/24 print (w/e Sep 5 206,000 → 207,000; w/e Sep 12 196,000 → 198,000).** §1 above carries the revised values; STATUS carries the same after this session's write-back. ⚠️ **The w/e Sep 5 change is a TWO-weeks-back revision** — outside DOL's usual prior-week revision. Expect that a retained week other than `W4` can move at the 10/1 print.

---

## §2 — PRE-COMMITTED BANDS *(carried verbatim — no STATUS threshold changed on 9/24)*

<!-- partition-axis: column="Initial claims, single print" -->
| Band | Initial claims, single print | Pre-committed assignment |
|---|---|---|
| **A** | ≤ 185,000 | **Kill B leg 1 of 5** — count 0 → 1 |
| **B** | 186,000 – 229,000 | **NO ACTION** (drift band, `<230,000`) |
| **C** | 230,000 – 250,000 | **Accelerating** — vector 13: 2 → **3** |
| **D** | 251,000 – 300,000 | **ARM T-01 provisional** (confirm on a 2nd consecutive `>250,000`) |
| **E** | ≥ 301,000 | 🔴 **T-02 FIRE** → REGINALD (all ORANGE→RED) + HENRY |

**Distance to the live triggers from the 197,000 base:** T-01 is `250,000 − 202,250 = **47,750**` away on the MA basis; T-02 is `300,000 − 197,000 = **103,000**` away. **Band B is again the modal outcome and I am not dressing it up as informative.**

---

## §3 — 🔴 THE MECHANICAL-DECLINE TRAP, PRE-COMPUTED  *(REGENERATED — the roll-off week CHANGED)*

The week **rolling off** is **w/e Aug 29 = 207,000** (`R = 207,000`). *(Last week it was w/e Aug 22 = 204,000.)*

`MA_next(X) = (207,000 + 198,000 + 197,000 + X)/4 = (602,000 + X)/4`  ⚠️ **[VINTAGE-DEPENDENT — moves if ANY retained week revises]**
**`ΔMA(X) = (602,000 + X)/4 − 809,000/4 = (X − 207,000)/4`**  ✅ **[depends only on `R`]**

**The MA falls for any print below 207,000, is unchanged at exactly 207,000, and rises above it.**

🔧 **TWO COLUMNS, TWO CLOCKS (L-31).** On 9/24 `ΔMA` was exact to the unit while the `MA_next` column rotted by +750 (two retained weeks revised +3,000 in sum). **Regenerate the `MA_next` column at the print even if `R` did not move.**

⚠️ **THE LINE CUTS ACROSS BAND B.** Band A and 186,000–206,000 of band B decline; **207,000 is the zero point**; 208,000–229,000 and all of bands C, D and E rise. ⛔ No band set has "the MA declines" true of every member and false of every non-member.

| Worked point (not a band) | `X` | `MA_next` ⚠️ | `ΔMA` ✅ |
|---|---|---|---|
| Kill-B edge | 185,000 | 196,750 | −5,500 |
| **Modal — a 197,000 repeat** | **197,000** | **199,750** | **−2,500** |
| **Zero-change point** | **207,000** | **202,250** | **0** |
| Accelerating edge | 230,000 | 208,000 | +5,750 |
| T-02 edge | 301,000 | 225,750 | +23,500 |

🔴 **PRE-COMMITTED READING RULE (carried):** a falling 4-week MA on a band-B print is **mechanical, not signal.** ⚠️ **This week the trap is sharper: a 197,000 repeat drops the MA to 199,750 — the first sub-200,000 MA since w/e Aug 8 (199,750, r539cy) — and that is ENTIRELY the 207,000 roll-off.** I will report "MA below 200,000, mechanically" and will not narrate it as improvement.

---

## §4 — WHAT THIS PRINT DOES **NOT** DO *(carried)*

- **A single weekly print is a realization gauge, not a demand-vs-supply discriminator.**
- **A benign print is not hawkish fuel — it is nothing.** Rate path / market repricing → BOND, HENRY, ORACLE.
- 🔴 **REVISION JITTER — ORDERED, NOT OPTIONAL (L-02), THREE quantities:** BEFORE reading the new level, regenerate ① `ΔMA` (moves only if `R` = w/e Aug 29 revises) · ② the `MA_next` column (moves if ANY retained week revises — it did on 9/10 and 9/24) · ③ §5a's T-01 bound. **If the as-published window differs from §1, those are void and regenerated on the spot; the BANDS in §2/§5b/§5c key on fixed levels and are unaffected.**
- ⛔ **No WARN cohort is registered for the w/e Sep 26 week.** If one appears before the print, size it against the **L-08 floor (~20,000 weekly claims)** and write the ratio **before** the print.
- 🟡 **NSA / YoY are colour and graded by NOTHING.** ⚠️ **Quarter-end week:** w/e Sep 26 precedes the Oct-1 quarter turn; some states see quarter-change filing effects in the following week, not this one — colour only, no band.

---

## §5a — 🔴 T-01 ON THE **MA BASIS** — re-solve every week

`(W2 + W3 + W4 + X)/4 > 250,000` ⟺ **`X > 1,000,000 − (W2+W3+W4)`**

On §1's window (`W2+W3+W4 = 207,000 + 198,000 + 197,000 = 602,000`): **`X > 398,000`.**
`398,000 → MA 250,000` (**not** `>250,000`, does **not** fire) · `399,000 → MA 250,250` (**fires**).

⚠️ **VOID THE MOMENT THE WINDOW REVISES** (moved 391,000 → 388,000 on the 9/24 revisions, then 388,000 → 398,000 on the roll).

<!-- partition-axis: column="Initial claims, single print (T-01 MA axis)" -->

| T01 | Initial claims, single print (T-01 MA axis) | Pre-committed assignment |
|---|---|---|
| **T01-a** | ≤ 398,000 | 4-wk MA ≤ 250,000 ⇒ **T-01 does NOT fire on the MA basis.** Bound re-solved at the print |
| **T01-b** | ≥ 399,000 | 🔴 **T-01 FIRES on the MA basis** → **CARL + REGINALD** — *in addition to* band E's T-02. Bound re-solved at the print |

🔴 **ROUTING UNION (carried):** any print ≥ the T01-b bound fires BOTH triggers; recipients = `CARL + REGINALD + HENRY`.

## §5b — VECTOR-13's `<200,000` COUNTER *(separate axis)*

`STATUS.md` vector 13: **`<200K ×4 → drop to 1`**, count **2 of 4**.

🆕 **REVISED-VINTAGE COUNTING RULE (pre-committed 2026-09-24, before the print):** the counter is the **trailing run of consecutive weeks `<200,000` on the 10/1 AS-PUBLISHED vintage** — each retained week counts at its REVISED value. Grade in this order: ① read the revised w/e Sep 12 and w/e Sep 19 values; if either is now `≥200,000`, the run restarts at the first qualifying week after it · ② then apply the table below to `X`. ⚠️ **Margins are thin: w/e Sep 12 = 198,000 (2,000 inside), w/e Sep 19 = 197,000 (3,000 inside); w/e Sep 12 already revised up 2,000 once.**

<!-- partition-axis: column="Initial claims, single print (vector-13 axis)" -->

| V13 | Initial claims, single print (vector-13 axis) | Pre-committed assignment |
|---|---|---|
| **V13-a** | ≤ 199,000 | counter = (revised trailing run) + 1 — **3 of 4 if both retained weeks still `<200,000`**. Independent of band A's Kill B leg; both can apply |
| **V13-b** | ≥ 200,000 | counter **RESETS to 0 of 4** — `200,000` is not `<200,000` |

## §5c — CONTINUING CLAIMS, w/e Sep 19 (separate letter)

Current **1,719,000** [w/e Sep 12]. Bar `<1,750,000`: **`1,750,000 − 1,719,000 = 31,000` INSIDE, 2 of 4 banked.** 🆕 **Same revised-vintage counting rule as §5b** (w/e Sep 5 already revised 1,730,000 → 1,717,000 on 9/24).

<!-- partition-axis: column="Continuing claims" -->
| Band | Continuing claims | Assignment |
|---|---|---|
| **CC-1** | < 1,750,000 | vector-7 count = (revised trailing run) + 1 — **3 of 4 if w/e Sep 5 + Sep 12 still `<1,750,000`** |
| **CC-2** | ≥ 1,750,000 | count **RESETS to 0 of 4** |

⚠️ CC is a **cost/duration** gauge — **not** an early-warning instrument. A **4th** consecutive week (earliest: the 10/8 print) is what moves vector 7 to 2; **3 of 4 moves nothing.**

---

## §6 — MECHANISM vs THRESHOLD (gate #3) — **no new prediction is registered on this card**

**Every band on this card is a THRESHOLD call** (0-for-5 at ≥60% on threshold calls; `workbook/PREDICTIONS_SCOREBOARD.md` §A).

🔴 **LAB-03 (claims breach 250K, live 7%, as-made 65%, due 2026-09-30) RESOLVES AT THIS PRINT.** Pre-committed: **❌ unless X ≥ 251,000** (the prediction is "breach 250K"; `250,000` is not a breach). On ❌: Brier on the **as-made 65%** (first-call book) AND on the live 7% only if a contemporaneous machine-field receipt exists for it (latest-mark book, WQ-112 — per `CLAUDE.md` C2 it does NOT for pre-9/7 marks). **Do not re-arm it.**

---

## §7 — ROUTING (pre-committed) *(carried)*

| Outcome | Route | Priority |
|---|---|---|
| **Band E** (T-02 fire) | **WALTER** (signal) → REGINALD (all ORANGE→RED), HENRY — **+ CARL if ≥ the §5a bound** | 🔴 |
| **Band D** (ARM T-01) | **WALTER** (signal) → CARL, REGINALD | 🟠 |
| **Band C** | STATUS + brief only | 🟡 |
| **Bands A / B** | STATUS only — **no packet** | — |
| CC-1 / V13-a (count → 3 of 4) | STATUS only — three weeks is not four | — |
| LAB-03 resolution | STATUS + PREDICTIONS.tsv + SCOREBOARD §A | — |

---

## §8 — DEFECT LOG (fill at grade time — defects in MY work, not the data's)

Pre-registered at freeze:
1. ✅ **L-31 split carried; both columns marked with their inputs.**
2. ✅ **Counters carried with RESET branches (V13-b, CC-2) AND the new revised-vintage rule** — bought by the 9/24 revision of the streak's first week.
3. 🔴 **L-33 reader guard carried:** the print is read from the extracted text of the saved DOL PDF; an Akamai `Access Denied` stub (382 B, HTML) is a loud failure — check `file` before parsing.

## §8b — 🔧 CHECKER SCOPE AT FREEZE (BD-31, expected)

`card_partition_check.py` run at freeze: **see the receipt line below.** Expected `4 band table(s) — 1 verified, 3 unverified, 0 with defects`, rc=2, `UNVERIFIED` only. ⛔ **`UNVERIFIED` is not a pass.** BD-31: one file-global `partition-axis` declaration; the load-bearing single-print axis (5 bands) is the one machine-verified.

🧾 **Checker receipt at freeze (2026-09-24, `card_partition_check.py`, rc=2):** `GRADING_CARD_20261001_claims.md: 4 band table(s) — 1 verified, 3 unverified, 0 with defects` · `[✓] table 2: VERIFIED — axis 'Initial claims, single print', 5 bands, precision 1,000, bounds as written` · tables 4/5/6 `[BAD-DECLARATION]` = the BD-31 one-declaration limit, hand-proved below. **Freeze authorized on `0 defects` + the written hand proof.**

**Hand proof of the three unverified tables:**

| Table | Bands | Complement holds because |
|---|---|---|
| §5c continuing claims | `< 1,750,000` / `≥ 1,750,000` | **true complement — exhaustive at any precision** |
| §5b vector-13 axis | `≤ 199,000` / `≥ 200,000` | **exhaustive on DOL's whole-thousand grid ONLY** — `199,500` cannot be printed |
| §5a T-01 MA axis | `≤ 398,000` / `≥ 399,000` | **whole-thousand grid only.** `398,000` included deliberately: `MA = 250,000` is **not** `> 250,000`. Bound moves on revision — §5a |

---

## §9 — GRADE (write 2026-10-01 off this frozen card — never re-read a band)

*Blank until print. Order: **①** regenerate the THREE quantities §4 names on the as-published vintage · **②** apply the §5b/§5c revised-vintage rule to the retained weeks, THEN grade the four axes (§2 · §5a · §5b · §5c) separately · **③** resolve LAB-03 per §6 · **④** write into `STATUS.md` (KEY THRESHOLDS + matrix v7/v13 + calendar + PREDICTIONS) · **⑤** `git mv` this card to `docket/graded/` **and build the 2026-10-08 card in the same session**.*

### §9 GRADE — written 2026-10-01 12:1x ET (PROME-spawned session `prome-0c` slate, WQ-184) off the frozen card

**Primary:** DOL/ETA news release 2026-10-01 08:30 ET, `dol.gov/ui/data.pdf` saved (`file`: PDF 1.7, 9 pages), text-extracted; release-date line *"8:30 A.M. (Eastern) Thursday, October 1, 2026"* checked; every figure below grepped in the extracted text. FRED ICSA agrees on all five weeks. KB-LAB-200.

**① Three quantities regenerated on the as-published vintage (the window DID revise — w/e Sep 19 197,000 → 198,000):**

| Quantity | Card (9/24 vintage) | As-published 10/1 | Moved? |
|---|---|---|---|
| `R` (w/e Aug 29) | 207,000 | 207,000 | no ⇒ **`ΔMA = (X − 207,000)/4` exact** |
| Retained trio `W2+W3+W4` | 602,000 | `207,000 + 198,000 + 198,000 = 603,000` | +1,000 |
| `MA_next(197,000)` | 199,750 | `(603,000 + 197,000)/4 = 800,000/4 = 200,000` = **published 200,000 exactly** | **+250 — the L-31 column rotted again** |
| `ΔMA(197,000)` | −2,500 | `(197,000 − 207,000)/4 = −2,500` vs revised prior MA 202,500 = **published −2,500** | exact ✅ |
| T-01 MA bound | `X > 398,000` | `X > 1,000,000 − 603,000 = 397,000` | −1,000 |

**② Four axes, graded separately (X = 197,000; CC = 1,701,000):**

| Axis | Read | Band | Assignment |
|---|---|---|---|
| §2 single print | 197,000 | **B** (186,000–229,000) | **NO ACTION** |
| §5a T-01 MA basis | 197,000 ≤ 397,000 | **T01-a** | T-01 does not fire; MA 200,000 is `250,000 − 200,000 = 50,000` below |
| §5b v13 `<200,000` | revised run Sep 12 198,000 · Sep 19 198,000 (2,000 inside each) · Sep 26 197,000 | **V13-a** | **counter 3 of 4.** w/e Sep 5 207,000 bounds the run. 4th week = the 10/8 print |
| §5c v7 CC `<1,750,000` | revised run Sep 5 1,717,000 · Sep 12 1,712,000 (rev from 1,719,000) · Sep 19 1,701,000 | **CC-1** | **counter 3 of 4.** w/e Aug 29 1,765,000 bounds the run. 3 of 4 moves nothing (§5c) |
| Kill B | 197,000 > 185,000 | — | 0 of 5 |

🔴 **Reading rule applied (§3):** the MA fell 2,500 to **200,000** — **entirely the 207,000 roll-off; mechanical, not improvement.** ⚠️ The card's pre-written sentence ("MA below 200,000, mechanically") does **not** apply: the w/e Sep 19 revision put the MA at **exactly 200,000**, not below it.

**③ LAB-03 — ❌ FALSIFIED** (197,000 < 251,000). As-made **65%** (verified at `STATUS.md` blob `575fd4039`, 2026-02-02) ⇒ Brier `0.65² = 0.4225`. Latest-mark book N/A (last mark 7% on 7/31, pre-receipt rule). Not re-armed. → `PREDICTIONS.tsv` + SCOREBOARD §A (n=13, mean 0.348).

**Routing (§7):** Band B ⇒ STATUS only, no packet. No WALTER signal.

**Colour, graded by nothing:** NSA 156,738 (−4.8% vs seasonal −4.1%; yr-ago 179,162) · Hawaii **+1,524** in w/e Sep 19 (state detail; the Kauai hurricane week) — stated, not graded.

**§8 defect log at grade:** ① L-31 two-clocks split worked as designed — `ΔMA` exact, `MA_next` off by +250, caught because it was regenerated, not carried · ② the §3 pre-written prose sentence assumed the modal print's MA would land below 200,000; a +1,000 revision to a retained week moved it to exactly 200,000 — **prose pre-written about a vintage-dependent quantity rots with that quantity.** No band affected.
