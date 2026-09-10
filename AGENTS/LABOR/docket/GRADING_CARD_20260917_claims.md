# 🔒 FROZEN GRADING CARD — Initial Claims w/e Sep 12, 2026

**Print:** Thu **2026-09-17, 08:30 ET** — initial claims w/e **Sep 12** (+ continuing claims w/e **Sep 5**).
**Frozen:** 2026-09-10 ~10:5x ET, **at the closeout of the session that graded the 9/10 card** — which is C2a's recurring-print trigger, not a date-based one. **7 days ahead of the print.**
**Built from:** `docket/TEMPLATE_claims_card.md`. **§1 and §3 REGENERATED from the live window; §2 · §4 · §6 · §7 carried verbatim (no STATUS threshold changed on 9/10).**
**Why a card is owed:** multi-loaded — **T-01, T-02, vector 13, Kill B, LAB-03**, plus CARL's kill-rule leg 1.

> 🔴 **THE ROLL-OFF WEEK CHANGED AND SO DID THE SIGN POINT. `R` moves 212,000 → 207,000 this week.** Last card's term was `(X − 212,000)/4`; **this card's is `(X − 207,000)/4`.** On a **206,000 repeat** the MA move goes from **−1,500** (last week) to **−250** (this week) — same print, `1,500/250 = 6.0×` smaller move, because a *smaller* week is rolling off. **This is precisely why §1/§3 are regenerated and never copied** (BD-19's stated failure mode, realized in the docket on 9/7).

---

## §1 — INPUTS FROZEN AT CURRENT VINTAGE  *(REGENERATED from the DOL release of 2026-09-10 08:30 ET — the AS-PUBLISHED vintage, not FRED's ingest)*

| Series | Value | Obs week | Source |
|---|---|---|---|
| Initial claims, latest (`W4`) | **206,000** | w/e 2026-09-05 | **DOL/ETA advance release 2026-09-10** [CONF] |
| 4-week window `W1/W2/W3/W4` (oldest→newest) | **207,000 / 204,000 / 207,000 / 206,000** | w/e Aug 15 · Aug 22 · **Aug 29** · Sep 5 | DOL 2026-09-10 |
| 4-week MA (`MA_cur`) | **206,000** | w/e 2026-09-05 | DOL 2026-09-10 |
| Continuing claims (`CC_cur`) | **1,774,000** | w/e 2026-08-29 | DOL 2026-09-10 |
| Kill B count (`n_kb`) | **0 of 5** | — | STATUS § KEY THRESHOLDS |
| Vector-7 count (`n_v7`) | **0 of 4** | — | STATUS § KEY THRESHOLDS |
| Vector-13 count (`n_v13`) | **0 of 4** | — | STATUS § CONVERGENCE MATRIX v13 |

**Reconciliation (division written out, root OUTPUT RULES (a)):**
`(207,000 + 204,000 + 207,000 + 206,000) / 4 = 824,000 / 4 = **206,000**` ✅ **equals the published 4-wk MA exactly.**

**Vintage note — no discrepancy to report this week, and that is a first.** w/e Aug 29 was **revised 206,000 → 207,000 with this release** and STATUS was refreshed to the revised figure in the same session, so §1 and STATUS agree at freeze. ⛔ **This does NOT extend the "card catches a revision STATUS had not followed" run — that count stays at THREE (8/13, 8/20, 9/10).** A same-print revision is not an unfollowed one.

---

## §2 — PRE-COMMITTED BANDS *(carried verbatim — no STATUS threshold changed on 9/10)*

<!-- partition-axis: column="Initial claims, single print" -->
| Band | Initial claims, single print | Pre-committed assignment |
|---|---|---|
| **A** | ≤ 185,000 | **Kill B leg 1 of 5** — count 0 → 1 |
| **B** | 186,000 – 229,000 | **NO ACTION** (drift band, `<230,000`) |
| **C** | 230,000 – 250,000 | **Accelerating** — vector 13: 2 → **3** |
| **D** | 251,000 – 300,000 | **ARM T-01 provisional** (confirm on a 2nd consecutive `>250,000`) |
| **E** | ≥ 301,000 | 🔴 **T-02 FIRE** → REGINALD (all ORANGE→RED) + HENRY |

**Distance to the live triggers from the 206,000 base:** T-01 is `250,000 − 206,000 = **44,000**` away on the MA basis (**WIDENED 1,250 on 9/10** as the MA fell 207,250→206,000); T-02 is `300,000 − 206,000 = **94,000**` away on the single-print basis. **Band B is again the modal outcome and I am not dressing it up as informative.**

---

## §3 — 🔴 THE MECHANICAL-DECLINE TRAP, PRE-COMPUTED  *(REGENERATED — the roll-off week CHANGED)*

The week **rolling off** is **w/e Aug 15 = 207,000** (`R = 207,000`). *(Last week it was w/e Aug 8 = 212,000.)*

`MA_next(X) = (204,000 + 207,000 + 206,000 + X)/4 = (617,000 + X)/4`  ⚠️ **[VINTAGE-DEPENDENT — see §4]**
**`ΔMA(X) = (617,000 + X)/4 − 824,000/4 = (X − 207,000)/4`**  ✅ **[depends only on `R`]**

**The MA falls for any print below 207,000, is unchanged at exactly 207,000, and rises above it.**

🔧 **TWO COLUMNS, TWO CLOCKS — installed from the 9/10 grade's defect 3 (L-31).** `ΔMA` is a function of **`R` alone**; `MA_next` is a function of the **retained three weeks**. On 9/10 the retained sum revised `617,000 → 618,000`: `ΔMA` survived untouched and **every `MA_next` value went stale by +250.** **Regenerate the `MA_next` column at the print even if `R` did not move.**

⚠️ **THE LINE CUTS ACROSS BAND B — say it that way or not at all.** `207,000` is a weekly print, not a band edge. **Band A and the part of band B from 186,000–206,000 decline; 207,000 is the zero point; 208,000–229,000 and all of bands C, D and E rise.** ⛔ There is **no** band set for which "the MA declines" is true of every member and false of every non-member.

| Worked point (not a band) | `X` | `MA_next` ⚠️ | `ΔMA` ✅ |
|---|---|---|---|
| Kill-B edge | 185,000 | 200,500 | −5,500 |
| **Modal — a 206,000 repeat** | **206,000** | **205,750** | **−250** |
| **Zero-change point** | **207,000** | **206,000** | **0** |
| Accelerating edge | 230,000 | 211,750 | +5,750 |
| T-02 edge | 301,000 | 229,500 | +23,500 |

🔴 **PRE-COMMITTED READING RULE (carried):** a falling 4-week MA on a print in band B is **mechanical, not signal.** **I will report the level and the MA move separately and will not narrate a declining MA as improvement.** ⚠️ **Extra caution this week: `ΔMA` at the modal print is only −250, which is 1/6th of last week's −1,500 on the identical level.** A reader comparing the two MA moves without the roll-off would read a "slowing improvement" that is entirely an artifact of which week left the window.

---

## §4 — WHAT THIS PRINT DOES **NOT** DO *(carried verbatim, with the A1.2a extension folded in as an ordered step)*

- **A single weekly print is a realization gauge, not a demand-vs-supply discriminator.**
- **A benign print is not hawkish fuel — it is nothing** (7/29 FOMC grade). **Rate path / market repricing → BOND, HENRY, ORACLE.**
- 🔴 **REVISION JITTER — ORDERED, NOT OPTIONAL (L-02), and it governs THREE quantities:** w/e Sep 5 revises with this print. **BEFORE reading the new level, regenerate:** ① §3's **`ΔMA`** term (moves only if `R` = w/e Aug 15 revises) · ② §3's **`MA_next`** column (moves if ANY retained week revises — it did on 9/10) · ③ **§5a's T-01 bound** below. **If the as-published window differs from §1, those three are void and regenerated on the spot; the BANDS in §2 and §5b are unaffected — they key on fixed levels.**
- ⛔ **No WARN cohort is registered for the w/e Sep 12 week.** If one appears before the print, size it against the **L-08 national detection floor (~20,000 weekly claims)** and state the ratio **before** the print, not after. **Absent a cohort ≥ that floor, no claims move is attributable to any named employer in either direction.**
- 🟡 **NSA / YoY are reported as colour and graded by NOTHING.** No band of mine is denominated in unadjusted claims, in the seasonal-factor gap, or in a year-ago comparison.

---

## §5a — 🔴 T-01 ON THE **MA BASIS** — the bound must be re-solved every week *(promoted out of last card's Amendment 1 into the standing card, where it belongs)*

**The FORMULA is the pre-commitment; the number below it is only its value on the frozen vintage.**

`(W2 + W3 + W4 + X)/4 > 250,000` ⟺ **`X > 1,000,000 − (W2+W3+W4)`**

On §1's window (`W2+W3+W4 = 204,000 + 207,000 + 206,000 = 617,000`): **`X > 383,000`.**
`383,000 → MA 250,000` (**not** `>250,000`, does **not** fire) · `384,000 → MA 250,250` (**fires**).

⚠️ **VOID THE MOMENT THE WINDOW REVISES.** On 9/10 this exact bound moved 383,000 → 382,000 on a 1,000-unit revision to a single retained week — **that was written as a hypothetical on 9/7 and occurred to the unit three days later.** Re-solve it at the print.

<!-- partition-axis: column="Initial claims, single print (T-01 MA axis)" -->

| T01 | Initial claims, single print (T-01 MA axis) | Pre-committed assignment |
|---|---|---|
| **T01-a** | ≤ 383,000 | 4-wk MA ≤ 250,000 ⇒ **T-01 does NOT fire on the MA basis.** Bound re-solved at the print |
| **T01-b** | ≥ 384,000 | 🔴 **T-01 FIRES on the MA basis** → **CARL + REGINALD** — *in addition to* band E's T-02. Bound re-solved at the print |

🔴 **ROUTING (corrected on the 9/10 card and carried):** band E routes REGINALD + HENRY (T-02). **Any print ≥ the T01-b bound fires BOTH triggers and the union of recipients is `CARL + REGINALD + HENRY`.** For `301,000 ≤ X <` the bound, band E's routing (REGINALD + HENRY) is correct as written.

## §5b — VECTOR-13's `<200,000` COUNTER IS A SEPARATE AXIS *(promoted from Amendment 1)*

`STATUS.md` vector 13: **`<200K ×4 → drop to 1`**, count **0 of 4**. **The boundary is 200,000, which is not a §2 band edge** — it splits band B. A **197,000** print is band **B / NO ACTION** on the single-print axis **and simultaneously starts the vector-13 counter at 1 of 4.**

<!-- partition-axis: column="Initial claims, single print (vector-13 axis)" -->

| V13 | Initial claims, single print (vector-13 axis) | Pre-committed assignment |
|---|---|---|
| **V13-a** | ≤ 199,000 | **vector-13 counter 0 → 1 of 4** (and, if also ≤185,000, band A's Kill B leg — independent, BOTH apply) |
| **V13-b** | ≥ 200,000 | counter **stays 0 of 4** — `200,000` is not `<200,000`, and the streak must be consecutive |

⚠️ **Grade §2, §5a and §5b as three separate readings of the same number.** A print can be NO ACTION on one axis and state-changing on another; that is not a contradiction and must not be resolved by picking one.

## §5c — CONTINUING CLAIMS, w/e Sep 5 (separate letter — do NOT fold into the initial-claims band)

Current **1,774,000** [w/e Aug 29]. The drop-to-2 bar is `<1,750,000`: **`1,774,000 − 1,750,000 = 24,000` away, 0 of 4 weeks banked.**

<!-- partition-axis: column="Continuing claims" -->
| Band | Continuing claims | Assignment |
|---|---|---|
| **CC-1** | < 1,750,000 | vector-7 drop-to-2 count 0 → **1 of 4** |
| **CC-2** | ≥ 1,750,000 | count **stays 0 of 4** |

⚠️ CC has changed direction repeatedly inside a ~1,770–1,800K range. It is a **cost/duration** gauge — **not** an early-warning instrument, and it will not be used as one. A single sub-1,750,000 print moves the count to 1, and nothing else. ⚠️ **CC also revises: w/e Aug 22 went 1,779,000 → 1,775,000 on 9/10.** Read the as-published prior before pricing the distance.

---

## §6 — MECHANISM vs THRESHOLD (gate #3) — **no new prediction is registered on this card** *(carried)*

**Every band on this card is a THRESHOLD call.** As-made record: **0-for-5 at ≥60% on threshold calls**, **3-for-3 on mechanism calls** (`workbook/PREDICTIONS_SCOREBOARD.md` §A). Gate #3 **caps** what may be asserted; gate #5 is not reached because nothing here is stated as a probability.

⛔ **NO new prediction.** **LAB-03** (claims breach 250K, **7%**, due Q2–Q3) is the only live forecast this print can touch, and a band-B print in a 44,000-wide gap does not move it. **Writing a fresh "claims stay benign" row would be a threshold call in the exact bucket where I am 0-for-5.**

---

## §7 — ROUTING (pre-committed) *(carried)*

| Outcome | Route | Priority |
|---|---|---|
| **Band E** (T-02 fire) | **WALTER** (signal) → REGINALD (all ORANGE→RED), HENRY — **+ CARL if ≥ the §5a bound** | 🔴 |
| **Band D** (ARM T-01) | **WALTER** (signal) → CARL, REGINALD | 🟠 |
| **Band C** | STATUS + brief only | 🟡 |
| **Bands A / B** | STATUS only — **no packet.** Silence = received and integrated | — |
| CC-1 (count → 1 of 4) | STATUS only — one week is not a streak | — |

---

## §8 — DEFECT LOG (fill at grade time — defects in MY work, not the data's)

Pre-registered at freeze:
1. ✅ **Carried forward from the 9/10 grade (L-31):** §3 now splits the vintage-robust `ΔMA` column from the vintage-dependent `MA_next` column and marks both. The 9/10 card presented them as one object and `MA_next` rotted silently on a 1,000-unit revision.
2. ✅ **Amendment-1 content promoted into the standing card (§5a/§5b).** On the 9/10 card, T-01's MA basis and vector 13's counter reached the card only via a post-freeze amendment — i.e. §2 shipped silent on two axes the same print moves. **They are now frozen in the body, not bolted on.**

## §8b — 🔧 CHECKER SCOPE AT FREEZE: 1 of 4 tables machine-verified, 3 HAND-PROVED (BD-31, expected)

`card_partition_check.py` run at freeze: **`4 band table(s) — 1 verified, 3 unverified, 0 with defects`** (rc=2, `UNVERIFIED` only, **no DEFECT**). ⛔ **`UNVERIFIED` is the tool refusing to certify what it could not read — it is NOT a pass and I am not reporting it as one.** The cause is **BD-31**: the checker reads **one file-global** `partition-axis` declaration and applies it to every table, so a card with four axes can machine-verify only the one declared. **I declared the load-bearing single-print axis (5 bands).** `0 with defects` is the number that must hold, and it holds.

**Hand proof of the three unverified tables** — each is a two-band dichotomy, and ⚠️ **they are NOT all exhaustive on the same terms:**

| Table | Bands | Complement holds because |
|---|---|---|
| §5c continuing claims | `< 1,750,000` / `≥ 1,750,000` | **true complement — exhaustive at any precision.** `<c` and `≥c` partition the reals |
| §5b vector-13 axis | `≤ 199,000` / `≥ 200,000` | **exhaustive on the whole-thousand grid DOL publishes ONLY** — `199,500` is uncovered and cannot be printed |
| §5a T-01 MA axis | `≤ 383,000` / `≥ 384,000` | **whole-thousand grid only**, same caveat. `383,000` is included deliberately: `MA = 250,000` is **not** `> 250,000`. ⚠️ Bounds move on revision — §5a |

**Freeze authorized on `0 defects` + this written hand proof, exactly as `TEMPLATE_claims_card.md` prescribes for the `UNVERIFIED`-only case.**

---

## §9 — GRADE (write 2026-09-17 off this frozen card — never re-read a band)

*Blank until print. At grade time, in this order: **①** regenerate the THREE quantities §4 names on the as-published vintage · **②** grade the four axes (§2 · §5a · §5b · §5c) separately · **③** write the outcome into `STATUS.md` (KEY THRESHOLDS + calendar row) · **④** `git mv` this card to `docket/graded/` **and build the 2026-09-24 card in the same session**.*
