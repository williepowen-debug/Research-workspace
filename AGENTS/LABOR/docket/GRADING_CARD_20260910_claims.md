# 🔒 FROZEN GRADING CARD — Initial Claims w/e Sep 5, 2026

**Print:** Thu **2026-09-10, 08:30 ET** — initial claims w/e **Sep 5** (+ continuing claims w/e **Aug 29**).
**Frozen:** 2026-09-07 ~17:5x ET, **3 days ahead of the print** (C2a asks for ~1 week; this is the first card built from `TEMPLATE_claims_card.md`, which exists so the *next* one is frozen at the prior closeout — see §9).
**Built from:** `docket/TEMPLATE_claims_card.md` (BD-19, built this session).
**Why a card is owed:** multi-loaded — **T-01, T-02, vector 13, Kill B, LAB-03**, plus CARL's kill-rule leg 1.

> 🔴 **THIS CARD'S FIRST ACT WAS TO REFUTE ITS OWN DOCKETED SETUP.** `docket/CATALYSTS.tsv` and `STATUS.md` PICKUP item 5 both stated: *"ROLL-OFF: w/e Aug 8 (200K per 9/3 vintage) drops out … mechanical term = (X-200)/4."* **Both halves are wrong.** w/e Aug 8 printed **212,000**; the **200,000** is w/e **Aug 1**, which had *already* rolled off at the Aug 29 print. The true term is **`(X − 212)/4`**. **The error inverts the sign of the MA move at the modal outcome:** on a 206,000 repeat, the docketed term says the MA *rises* +1,500; it actually *falls* −1,500. This is **BD-19's predicted failure mode, realized in the docket before the card was written** — the register said *"the mechanical term flips sign as different weeks roll off, and a copied card would carry the previous week's roll-off logic as if it still held."* It did.

---

## §1 — INPUTS FROZEN AT CURRENT VINTAGE (FRED, pulled 2026-09-07 17:43 ET)

| Series | Value | Obs week | Source |
|---|---|---|---|
| Initial claims, latest | **206,000** | w/e 2026-08-29 | FRED `ICSA` [DOL] |
| 4-week window (oldest→newest) | **212,000 / 207,000 / 204,000 / 206,000** | w/e Aug 8 · Aug 15 · Aug 22 · Aug 29 | FRED `ICSA` |
| 4-week MA | **207,250** | w/e 2026-08-29 | FRED `IC4WSA` |
| Continuing claims | **1,779,000** | w/e 2026-08-22 | FRED `CCSA` |
| Kill B count (`n_kb`) | **0 of 5** | — | STATUS § KEY THRESHOLDS |
| Vector-7 count (`n_v7`) | **0 of 4** | — | STATUS § KEY THRESHOLDS |

**Reconciliation (division written out, root OUTPUT RULES (a)):**
`(212,000 + 207,000 + 204,000 + 206,000) / 4 = 829,000 / 4 = 207,250` ✅ **equals FRED `IC4WSA` exactly.**

🔧 **VINTAGE DEFECT FOUND IN MY OWN STATUS — w/e Aug 22 is 204,000, not 203,000.**
`STATUS.md` § KEY THRESHOLDS carries the run `200/212/207/**203**/206`. That run implies a MA of `(212+207+203+206)/4 = 207,000` — but the same STATUS row carries **207,250**, and FRED confirms 207,250. **The MA is right and the run digit is wrong**; `829,000 − 212,000 − 207,000 − 206,000 = 204,000` forces it. **It is an unfollowed REVISION, and that is now established, not guessed:** w/e Aug 22 printed **203,000** on 8/27 (recorded in `NEXUS_BRIEF` and `workbook/PUBLISHED.tsv` row 59) and was revised to **204,000**. STATUS's MA followed the revision (FRED-refreshed each boot); STATUS's run digit did not (hand-carried). 🔴 **This is the THIRD consecutive claims card to catch a revision STATUS had not followed** (8/13, 8/20, now 9/10) — which is the argument for §4's revision-jitter step being ORDERED rather than advisory. ⚠️ **The B2a spine gate could not catch this: it compares observation DATES, not VALUES, and the dates were fresh.** Corrected in STATUS this session; logged as a template-fill step (`MA_cur` must equal the mean of the four W's, or stop).

---

## §2 — PRE-COMMITTED BANDS (assignments fixed before the print)

Keyed to `STATUS.md` § KEY THRESHOLDS. Verified to PARTITION the axis at 1,000 granularity — no gap, no overlap, no unenumerated branch.

<!-- partition-axis: column="Initial claims, single print" -->
| Band | Initial claims, single print | Pre-committed assignment |
|---|---|---|
| **A** | ≤ 185,000 | **Kill B leg 1 of 5** — count 0 → 1 |
| **B** | 186,000 – 229,000 | **NO ACTION** (drift band, `<230,000`) |
| **C** | 230,000 – 250,000 | **Accelerating** — vector 13: 2 → **3** |
| **D** | 251,000 – 300,000 | **ARM T-01 provisional** (confirm on a 2nd consecutive `>250,000`) |
| **E** | ≥ 301,000 | 🔴 **T-02 FIRE** → REGINALD (all ORANGE→RED) + HENRY |

**Distance to the live triggers, from the 206,000 print:** T-01 is `250,000 − 207,250 = 42,750` away on the MA basis; T-02 is `300,000 − 206,000 = 94,000` away on the single-print basis. **Band B is the modal outcome and I am not dressing it up as informative.**

---

## §3 — 🔴 THE MECHANICAL-DECLINE TRAP, PRE-COMPUTED (this is the card's main job)

The week **rolling off** is **w/e Aug 8 = 212,000** (`R = 212,000`).

`MA_next(X) = (207,000 + 204,000 + 206,000 + X)/4 = (617,000 + X)/4`
**`ΔMA(X) = (617,000 + X)/4 − 829,000/4 = (X − 212,000)/4`**

**The MA falls for any print below 212,000, is unchanged at exactly 212,000, and rises above it.**

⚠️ **THE LINE CUTS ACROSS BAND B — say it that way or not at all.** `212,000` is a weekly print, not a band edge. **Band A and the part of band B from 186,000–211,000 decline; the part of band B from 212,000–229,000 and all of bands C, D and E rise** (212,000 itself is the zero point). ⛔ There is **no** band set for which "the MA declines" is true of every member and false of every non-member. Writing one would be the BD-30 defect the 8/13 card shipped.

| Worked point (not a band) | `X` | `MA_next` | `ΔMA` |
|---|---|---|---|
| Kill-B edge | 185,000 | 200,500 | −6,750 |
| Modal — a 206,000 repeat | 206,000 | 205,750 | **−1,500** |
| **Zero-change point** | **212,000** | **207,250** | **0** |
| Accelerating edge | 230,000 | 211,750 | +4,500 |
| T-02 edge | 301,000 | 229,500 | +22,250 |

🔴 **PRE-COMMITTED READING RULE:** a falling 4-week MA on a print in band B is **mechanical, not signal.** The MA can fall while the level rises (e.g. `X = 208,000` → level +2,000 WoW, MA −1,000). **I will report the level and the MA move separately and will not narrate a declining MA as improvement.**

---

## §4 — WHAT THIS PRINT DOES **NOT** DO (attribution discipline, both directions)

- **A single weekly print is a realization gauge, not a demand-vs-supply discriminator.** Claims is the CORE TENSION's discriminating test *in aggregate over time*, not in one week.
- 🔴 **MSFT/Xbox WARN cohort (763 workers) became effective 2026-09-04 and falls in THIS claims week. It will NOT be attributed, in either direction.** Pre-committed and unchanged: `763 / 20,000 = 3.8%` of the L-08 national detection floor — `20,000 / 763 = 26.2×` below it. **If claims rise this week, that cohort is not the reason; if they fall, the cohort's absence is not evidence either.**
- **A benign print is not hawkish fuel — it is nothing** (7/29 FOMC grade: labor is a satisfied side-constraint, not a policy input).
- **Rate path / market repricing are not my call** → BOND, HENRY, ORACLE.
- 🔴 **REVISION JITTER — ORDERED, NOT OPTIONAL (L-02):** w/e Aug 29 revises with this print. **On print morning, recompute `ΔMA` against the AS-PUBLISHED vintage BEFORE reading the new level.** A frozen threshold computed off a revisable series is not actually frozen — this card's own §1 found a 1,000-unit vintage discrepancy three days out, and the 8/13 and 8/20 cards each caught a revision STATUS had not followed. **If the as-published window differs from §1, §3's table is void and is regenerated on the spot; the BANDS in §2 are unaffected.**

---

## §5 — CONTINUING CLAIMS, w/e Aug 29 (separate letter — do NOT fold into the initial-claims band)

Current **1,779,000** [w/e Aug 22]. The drop-to-2 bar is `<1,750,000`: **`1,779,000 − 1,750,000 = 29,000` away, 0 of 4 weeks banked.**

| Band | Continuing claims | Assignment |
|---|---|---|
| **CC-1** | < 1,750,000 | vector-7 drop-to-2 count 0 → **1 of 4** |
| **CC-2** | ≥ 1,750,000 | count **stays 0 of 4** |

🔧 **CC IS HAND-VERIFIED, NOT MACHINE-VERIFIED — and here is exactly why.** `card_partition_check.py` reads **one file-global** `partition-axis` declaration and applies it to every table, so a card with **two** band tables on different axes can only have one of them machine-checked. I declared the load-bearing initial-claims axis (5 bands, VERIFIED); this CC table therefore returns **UNVERIFIED [BAD-DECLARATION]**, which is the tool correctly refusing to certify what it did not check. ⛔ **That is not a pass and I am not reporting it as one.** Hand proof, since the dichotomy is trivial: the two bands are `< 1,750,000` and `≥ 1,750,000` — **complementary by construction**, so they cover the axis with no gap and no overlap at any precision. **Every claims card will have this shape** → registered as **BD-31**; not fixed here, because fixing it is checker work and this session's job is the card.

⚠️ CC has changed direction four times in six weeks inside 1,777–1,799K. It is a **cost/duration** gauge — **not** an early-warning instrument, and it will not be used as one. A single sub-1,750,000 print moves the count to 1, and nothing else.

---

## §6 — MECHANISM vs THRESHOLD (gate #3) — **no new prediction is registered on this card**

**Every band in §2 is a THRESHOLD call.** My as-made record is **0-for-5 at ≥60% on threshold calls** and **3-for-3 on mechanism calls at the same confidence** (`workbook/PREDICTIONS_SCOREBOARD.md` §A). Gate #3 therefore **caps** what may be asserted here, and gate #5 (>80% STOP) is not reached because nothing on this card is stated as a probability at all.

⛔ **I am registering NO new prediction on this print.** LAB-03 (claims breach 250K, **7%**) already carries the only forecast this print can resolve, and a 206,000 print in a 42,750-wide gap does not move it. **Writing a fresh high-confidence "claims stay benign" row would be a threshold call in the exact bucket where I am 0-for-5** — the honest action is to let the existing row stand and grade it on its own due date (Q2–Q3).

---

## §7 — ROUTING (pre-committed)

| Outcome | Route | Priority |
|---|---|---|
| **Band E** (T-02 fire) | **WALTER** (signal) → REGINALD (all ORANGE→RED), HENRY | 🔴 |
| **Band D** (ARM T-01) | **WALTER** (signal) → CARL, REGINALD | 🟠 |
| **Band C** | STATUS + brief only | 🟡 |
| **Bands A / B** | STATUS only — **no packet.** Silence = received and integrated | — |
| CC-1 (count → 1 of 4) | STATUS only — one week is not a streak | — |

---

## §8 — DEFECT LOG (fill at grade time — defects in MY work, not the data's)

Pre-registered at freeze:
1. ✅ **Found at freeze:** docketed roll-off week/value and mechanical term both wrong, sign-inverting at the modal print (see banner).
2. ✅ **Found at freeze:** STATUS claims run carries `203` where FRED and STATUS's own MA force `204`.

## §9 — GRADE (written 2026-09-10 off this frozen card — never re-read a band)

*Blank until print. At grade time: recompute §3 on the as-published vintage FIRST (§4), then assign the band, then write the outcome into `STATUS.md` (KEY THRESHOLDS + calendar row) and `git mv` this card to `docket/graded/`.*

---

# 🔧 AMENDMENT 1 — 2026-09-07, PRE-PRINT (CODEX review of `e1f37d79b`)

> ⛔ **NOTHING ABOVE THIS LINE IS EDITED.** §1–§9 stand exactly as frozen at 17:5x ET. This amendment is **additive and pre-print**, so every band and assignment here is still committed before the outcome is known.
> 🔑 **These are EXISTING decision rules that §2's bands omitted — not new thresholds and not a re-read.** Both already live in `STATUS.md`; the card simply failed to enumerate them, which is the L-18/L-27 partition defect in its cross-axis form: **§2 partitions the single-print axis correctly and is silent on two OTHER axes that the same print moves.**

## A1.1 — Vector 13's `<200,000` counter is a SEPARATE AXIS and cuts across bands A and B

`STATUS.md` vector 13 carries: **`<200K ×4 → drop to 1`** (count now **0 of 4**, reset at w/e Aug 1's revision to 200K). **The boundary is 200,000, which is not a §2 band edge** — it splits band B and sits above all of band A. So a **197,000** print is band **B / "NO ACTION"** on the single-print axis **and simultaneously starts the vector-13 counter at 1 of 4**. Labelling it NO ACTION alone is wrong.

<!-- partition-axis: column="Initial claims, single print (vector-13 axis)" -->

| V13 | Initial claims, single print (vector-13 axis) | Pre-committed assignment |
|---|---|---|
| **V13-a** | ≤ 199,000 | **vector-13 counter 0 → 1 of 4** (and, if also ≤185,000, band A's Kill B leg — the two are independent and BOTH apply) |
| **V13-b** | ≥ 200,000 | counter **stays 0 of 4** — `200,000` is not `<200,000`, and the streak must be consecutive |

⚠️ **Grade §2 and A1.1 as two separate readings of the same number.** A print can be "NO ACTION" on one axis and state-changing on the other; that is not a contradiction and must not be resolved by picking one.

## A1.2 — T-01 is an **MA-basis** trigger, so it can fire on this print, and its routing includes CARL

`STATUS.md`: **`>250K sustained 4+wk = T-01`**, measured on the 4-week MA (the same row prices distance as *"42,750 below T-01 on MA basis"* = `250,000 − 207,250`). §2 only ever referenced T-01 through band D's **provisional ARM** on a single print. But the MA itself can cross on **this** print:

**The FORMULA is the pre-commitment; the number below it is only its value on the frozen vintage.**

`(W2 + W3 + W4 + X)/4 > 250,000` ⟺ **`X > 1,000,000 − (W2+W3+W4)`**

On §1's frozen window (`W2+W3+W4 = 617,000`): **`X > 383,000`** — `383,000 → MA 250,000` (**not** `>250,000`, does **not** fire) · `384,000 → MA 250,250` (**fires**).

🔴 **REGENERATE THIS BOUND AT THE PRINT, exactly as §3 is regenerated — the same L-02 rule, and A1.2 got it wrong first time.** The bound is a function of the *retained three weeks*, which revise. **If the retained sum revises 617,000 → 618,000, the bound moves to `X > 382,000`, and a 383,000 print then fires T-01 and requires CARL** — the frozen `384,000` would have missed it. ⚠️ **`383,000`/`384,000` are VOID the moment the window revises.** *(CODEX, 2026-09-07: I wrote a revision-regeneration rule for §3 in the same session I hard-coded a revisable bound in A1.2.)*

<!-- partition-axis: column="Initial claims, single print (T-01 MA axis)" -->

| T01 | Initial claims, single print (T-01 MA axis) | Pre-committed assignment |
|---|---|---|
| **T01-a** | ≤ 383,000 | 4-wk MA ≤ 250,000 ⇒ **T-01 does NOT fire on the MA basis.** Bound recomputed at the print |
| **T01-b** | ≥ 384,000 | 🔴 **T-01 FIRES on the MA basis** → **CARL + REGINALD** — *in addition to* band E's T-02. Bound recomputed at the print |

🔴 **ROUTING CORRECTION TO §7 BAND E:** §7 routed band E to **REGINALD + HENRY** (T-02's recipients) and **omitted CARL**, who is a required T-01 recipient. **Any print ≥ 384,000 fires BOTH triggers, and the union of recipients is `CARL + REGINALD + HENRY`.** For `301,000 ≤ X ≤ 383,000`, band E's original routing (REGINALD + HENRY) is correct as written.

## A1.2a — §4's revision step now governs TWO derived quantities, not one

⛔ **§4 is frozen text and is NOT edited** — this clause EXTENDS it, which is the only legitimate way to change a frozen card. *(I briefly edited §4 in place while writing this amendment and my own frozen-prefix check caught it; the byte-for-byte original is restored. The card's entire value is that §1–§9 cannot move, so an "improvement" to frozen text is exactly the defect it exists to prevent.)*

§4 orders: *"If the as-published window differs from §1, §3's table is void and is regenerated on the spot."* **Read that as covering BOTH window-derived quantities:**
1. §3's `ΔMA(X) = (X − R)/4` table, and
2. **A1.2's T-01 crossing bound `X > 1,000,000 − (W2+W3+W4)`.**

**The BANDS in §2 and A1.1 remain unaffected either way** — they key on fixed levels, not on the window.

## A1.2b — 🔧 CHECKER SCOPE AFTER THIS AMENDMENT: 1 of 4 tables machine-verified, 3 hand-proved

`card_partition_check.py` reads **one file-global** `partition-axis` declaration (BD-31), so adding two axes took the card from **1-of-2** to **1-of-4** machine-verified tables. **Result: `4 band table(s) — 1 verified, 3 unverified, 0 with defects`.** ⛔ **`0 with defects` is the number that must hold, and it holds. `UNVERIFIED` is the tool refusing to certify what it could not read — it is not a pass, and I am not reporting it as one.**

**Hand proof for all three unverified tables.** Each is a **two-band dichotomy**, but ⚠️ **they are not all exhaustive on the same terms and my first statement of this was wrong** — I wrote *"no gap and no overlap **at any precision**"* for all three. **That is false for two of them:** `199,500` falls between `≤199,000` and `≥200,000`, and `383,500` between `≤383,000` and `≥384,000`. Those two are exhaustive **on the whole-thousand grid DOL publishes**, which is the grid the print actually arrives on — a real and sufficient proof, but a narrower one than I claimed. *(CODEX, 2026-09-07.)*

| Table | Bands | Complement holds because |
|---|---|---|
| §5 continuing claims | `< 1,750,000` / `≥ 1,750,000` | **true complement — exhaustive at any precision.** `<c` and `≥c` partition the reals |
| A1.1 vector-13 axis | `≤ 199,000` / `≥ 200,000` | **exhaustive on the whole-thousand grid only** — adjacent at 1,000 granularity. `199,500` is uncovered and cannot be printed by DOL |
| A1.2 T-01 MA axis | `≤ 383,000` / `≥ 384,000` | **whole-thousand grid only**, same caveat. `383,000` is included deliberately: `MA = 250,000` is **not** `> 250,000`. ⚠️ Bounds move on revision — see A1.2 |

🔴 **BD-31 escalated 🟠 → 🔴 on this measurement.** It was opened as a 1-of-2 nuisance; it is now 3-of-4 unchecked on a card that gets graded in three days. **Not fixed in this pass** — Will scoped this session to the card and CODEX's review explicitly said no further partition-checker work was needed for these findings — **but the cost is now measured rather than asserted, which is what should drive the fix.**

## A1.3 — What this amendment does NOT do

- **No threshold moved.** T-01, T-02, Kill B and vector 13 keep the values `STATUS.md` already carried; the card now enumerates them.
- **No band in §2 changed.** The single-print partition A–E stands and re-verified after this amendment.
- **The §3 mechanical term is untouched** — `(X − 212,000)/4`, still recomputed on the as-published vintage before the level is read (§4).
- ⚠️ **Three independent boundaries now sit inside band B — `200,000` (vector 13), `212,000` (MA zero-change) and the band's own edges.** That is the standing argument against reading any single-print band as the whole verdict, and it is why the template carries all three axes from now on.
