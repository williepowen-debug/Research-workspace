# 🔒 FROZEN GRADING CARD — Initial Claims w/e Sep 19, 2026

**Print:** Thu **2026-09-24, 08:30 ET** — initial claims w/e **Sep 19** (+ continuing claims w/e **Sep 12**).
**Frozen:** 2026-09-17 08:4x ET, **in the session that graded the 9/17 card** — C2a's recurring-print trigger, not a date-based one. **7 days ahead of the print.**
**Built from:** `docket/TEMPLATE_claims_card.md`. **§1 · §3 · §5a REGENERATED from the live window; §2 · §4 · §5b · §5c · §6 · §7 carried verbatim (no STATUS threshold changed on 9/17). Counters carried: v13 1 of 4 · v7 1 of 4.**
**Why a card is owed:** multi-loaded — **T-01, T-02, vector 13, Kill B, LAB-03**, plus CARL's kill-rule leg 1.

> 🔴 **THE ROLL-OFF WEEK CHANGED AND SO DID THE SIGN POINT. `R` moves 207,000 → 204,000 this week.** Last card's term was `(X − 207,000)/4`; **this card's is `(X − 204,000)/4`.** On a **196,000 repeat** the MA move is **−2,000** (last week's 196,000 gave **−2,750**) — same print, `2,750/2,000 = 1.375×` smaller, because a *smaller* week rolls off. ⚠️ **AND THE T-01 BOUND MOVED 8,000 WITHOUT ANY REVISION: 383,000 → 391,000**, because a 196,000 replaced a 204,000 in the retained trio. **This is precisely why §1/§3/§5a are regenerated and never copied.**

---

## §1 — INPUTS FROZEN AT CURRENT VINTAGE  *(REGENERATED from the DOL release of 2026-09-17 08:30 ET — the AS-PUBLISHED vintage, not FRED's ingest)*

| Series | Value | Obs week | Source |
|---|---|---|---|
| Initial claims, latest (`W4`) | **196,000** | w/e 2026-09-12 | **DOL/ETA advance release 2026-09-17** [CONF] |
| 4-week window `W1/W2/W3/W4` (oldest→newest) | **204,000 / 207,000 / 206,000 / 196,000** | w/e Aug 22 · Aug 29 · Sep 5 · Sep 12 | DOL 2026-09-17 |
| 4-week MA (`MA_cur`) | **203,250** | w/e 2026-09-12 | DOL 2026-09-17 |
| Continuing claims (`CC_cur`) | **1,730,000** | w/e 2026-09-05 | DOL 2026-09-17 |
| Kill B count (`n_kb`) | **0 of 5** | — | STATUS § KEY THRESHOLDS |
| Vector-7 count (`n_v7`) | **1 of 4** (CC-1 fired 9/17) | — | STATUS § KEY THRESHOLDS |
| Vector-13 count (`n_v13`) | **1 of 4** (V13-a fired 9/17) | — | STATUS § CONVERGENCE MATRIX v13 |

**Reconciliation (division written out, root OUTPUT RULES (a)):**
`(204,000 + 207,000 + 206,000 + 196,000) / 4 = 813,000 / 4 = **203,250**` ✅ **equals the published 4-wk MA exactly.**

**Vintage note — NO revision to any retained week on 9/17 (w/e Sep 5 stood at 206,000), so §1 and STATUS agree at freeze.** ⛔ **The "card catches a revision STATUS had not followed" count stays at THREE (8/13, 8/20, 9/10).**

---

## §2 — PRE-COMMITTED BANDS *(carried verbatim — no STATUS threshold changed on 9/17)*

<!-- partition-axis: column="Initial claims, single print" -->
| Band | Initial claims, single print | Pre-committed assignment |
|---|---|---|
| **A** | ≤ 185,000 | **Kill B leg 1 of 5** — count 0 → 1 |
| **B** | 186,000 – 229,000 | **NO ACTION** (drift band, `<230,000`) |
| **C** | 230,000 – 250,000 | **Accelerating** — vector 13: 2 → **3** |
| **D** | 251,000 – 300,000 | **ARM T-01 provisional** (confirm on a 2nd consecutive `>250,000`) |
| **E** | ≥ 301,000 | 🔴 **T-02 FIRE** → REGINALD (all ORANGE→RED) + HENRY |

**Distance to the live triggers from the 196,000 base:** T-01 is `250,000 − 203,250 = **46,750**` away on the MA basis (**WIDENED 2,750 on 9/17** as the MA fell 206,000→203,250); T-02 is `300,000 − 196,000 = **104,000**` away on the single-print basis. **Band B is again the modal outcome and I am not dressing it up as informative.**

---

## §3 — 🔴 THE MECHANICAL-DECLINE TRAP, PRE-COMPUTED  *(REGENERATED — the roll-off week CHANGED)*

The week **rolling off** is **w/e Aug 22 = 204,000** (`R = 204,000`). *(Last week it was w/e Aug 15 = 207,000.)*

`MA_next(X) = (207,000 + 206,000 + 196,000 + X)/4 = (609,000 + X)/4`  ⚠️ **[VINTAGE-DEPENDENT — see §4]**
**`ΔMA(X) = (609,000 + X)/4 − 813,000/4 = (X − 204,000)/4`**  ✅ **[depends only on `R`]**

**The MA falls for any print below 204,000, is unchanged at exactly 204,000, and rises above it.**

🔧 **TWO COLUMNS, TWO CLOCKS (L-31).** `ΔMA` is a function of **`R` alone**; `MA_next` is a function of the **retained three weeks**. On 9/17 neither moved (no revision); on 9/10 the retained sum moved +1,000 and every `MA_next` value rotted by +250 while `ΔMA` was exact. **Regenerate the `MA_next` column at the print even if `R` did not move.**

⚠️ **THE LINE CUTS ACROSS BAND B — say it that way or not at all.** `204,000` is a weekly print, not a band edge. **Band A and the part of band B from 186,000–203,000 decline; 204,000 is the zero point; 205,000–229,000 and all of bands C, D and E rise.** ⛔ There is **no** band set for which "the MA declines" is true of every member and false of every non-member.

| Worked point (not a band) | `X` | `MA_next` ⚠️ | `ΔMA` ✅ |
|---|---|---|---|
| Kill-B edge | 185,000 | 198,500 | −4,750 |
| **Modal — a 196,000 repeat** | **196,000** | **201,250** | **−2,000** |
| **Zero-change point** | **204,000** | **203,250** | **0** |
| Accelerating edge | 230,000 | 209,750 | +6,500 |
| T-02 edge | 301,000 | 227,500 | +24,250 |

🔴 **PRE-COMMITTED READING RULE (carried):** a falling 4-week MA on a print in band B is **mechanical, not signal.** **I will report the level and the MA move separately and will not narrate a declining MA as improvement.** ⚠️ **This week: a 196,000 repeat gives `ΔMA = −2,000` against last week's −2,750 on the identical level — `2,750/2,000 = 1.375×` — purely from which week left the window. A ≥204,000 print makes the MA RISE while the level is still in band B; say "level flat-to-up, MA mechanically up," not "deterioration."**

---

## §4 — WHAT THIS PRINT DOES **NOT** DO *(carried verbatim, with the A1.2a extension folded in as an ordered step)*

- **A single weekly print is a realization gauge, not a demand-vs-supply discriminator.**
- **A benign print is not hawkish fuel — it is nothing** (7/29 FOMC grade). **Rate path / market repricing → BOND, HENRY, ORACLE.**
- 🔴 **REVISION JITTER — ORDERED, NOT OPTIONAL (L-02), and it governs THREE quantities:** w/e Sep 12 revises with this print. **BEFORE reading the new level, regenerate:** ① §3's **`ΔMA`** term (moves only if `R` = w/e Aug 22 revises) · ② §3's **`MA_next`** column (moves if ANY retained week revises — it did on 9/10) · ③ **§5a's T-01 bound** below. **If the as-published window differs from §1, those three are void and regenerated on the spot; the BANDS in §2 and §5b are unaffected — they key on fixed levels.**
- ⛔ **No WARN cohort is registered for the w/e Sep 19 week.** If one appears before the print, size it against the **L-08 national detection floor (~20,000 weekly claims)** and state the ratio **before** the print, not after. **Absent a cohort ≥ that floor, no claims move is attributable to any named employer in either direction.**
- 🟡 **NSA / YoY are reported as colour and graded by NOTHING.** No band of mine is denominated in unadjusted claims, in the seasonal-factor gap, or in a year-ago comparison.

---

## §5a — 🔴 T-01 ON THE **MA BASIS** — the bound must be re-solved every week *(promoted out of last card's Amendment 1 into the standing card, where it belongs)*

**The FORMULA is the pre-commitment; the number below it is only its value on the frozen vintage.**

`(W2 + W3 + W4 + X)/4 > 250,000` ⟺ **`X > 1,000,000 − (W2+W3+W4)`**

On §1's window (`W2+W3+W4 = 207,000 + 206,000 + 196,000 = 609,000`): **`X > 391,000`.**
`391,000 → MA 250,000` (**not** `>250,000`, does **not** fire) · `392,000 → MA 250,250` (**fires**).

⚠️ **VOID THE MOMENT THE WINDOW REVISES.** On 9/10 this bound moved 383,000 → 382,000 on a 1,000-unit revision to one retained week; on 9/17 it stood. **It moved 383,000 → 391,000 THIS week with no revision at all — the roll-off did it.** Re-solve it at the print.

<!-- partition-axis: column="Initial claims, single print (T-01 MA axis)" -->

| T01 | Initial claims, single print (T-01 MA axis) | Pre-committed assignment |
|---|---|---|
| **T01-a** | ≤ 391,000 | 4-wk MA ≤ 250,000 ⇒ **T-01 does NOT fire on the MA basis.** Bound re-solved at the print |
| **T01-b** | ≥ 392,000 | 🔴 **T-01 FIRES on the MA basis** → **CARL + REGINALD** — *in addition to* band E's T-02. Bound re-solved at the print |

🔴 **ROUTING (corrected on the 9/10 card and carried):** band E routes REGINALD + HENRY (T-02). **Any print ≥ the T01-b bound fires BOTH triggers and the union of recipients is `CARL + REGINALD + HENRY`.** For `301,000 ≤ X <` the bound, band E's routing (REGINALD + HENRY) is correct as written.

## §5b — VECTOR-13's `<200,000` COUNTER IS A SEPARATE AXIS *(promoted from Amendment 1)*

`STATUS.md` vector 13: **`<200K ×4 → drop to 1`**, count **1 of 4** (V13-a fired 9/17 on 196,000). **The boundary is 200,000, which is not a §2 band edge** — it splits band B. A **197,000** print is band **B / NO ACTION** on the single-print axis **and simultaneously starts the vector-13 counter at 1 of 4.**

<!-- partition-axis: column="Initial claims, single print (vector-13 axis)" -->

| V13 | Initial claims, single print (vector-13 axis) | Pre-committed assignment |
|---|---|---|
| **V13-a** | ≤ 199,000 | **vector-13 counter 1 → 2 of 4** (and, if also ≤185,000, band A's Kill B leg — independent, BOTH apply) |
| **V13-b** | ≥ 200,000 | counter **RESETS 1 → 0 of 4** — `200,000` is not `<200,000`, and the streak must be consecutive |

⚠️ **Grade §2, §5a and §5b as three separate readings of the same number.** A print can be NO ACTION on one axis and state-changing on another; that is not a contradiction and must not be resolved by picking one.

## §5c — CONTINUING CLAIMS, w/e Sep 5 (separate letter — do NOT fold into the initial-claims band)

Current **1,730,000** [w/e Sep 5]. The drop-to-2 bar is `<1,750,000`: **`1,750,000 − 1,730,000 = 20,000` INSIDE the bar, 1 of 4 weeks banked (CC-1 fired 9/17).**

<!-- partition-axis: column="Continuing claims" -->
| Band | Continuing claims | Assignment |
|---|---|---|
| **CC-1** | < 1,750,000 | vector-7 drop-to-2 count 1 → **2 of 4** |
| **CC-2** | ≥ 1,750,000 | count **RESETS 1 → 0 of 4** — the streak must be consecutive |

⚠️ CC has changed direction repeatedly inside a ~1,770–1,800K range. It is a **cost/duration** gauge — **not** an early-warning instrument, and it will not be used as one. A second sub-1,750,000 print moves the count to 2, and nothing else. ⚠️ **CC also revises: w/e Aug 29 went 1,774,000 → 1,769,000 on 9/17.** Read the as-published prior before pricing the distance.

---

## §6 — MECHANISM vs THRESHOLD (gate #3) — **no new prediction is registered on this card** *(carried)*

**Every band on this card is a THRESHOLD call.** As-made record: **0-for-5 at ≥60% on threshold calls**, **3-for-3 on mechanism calls** (`workbook/PREDICTIONS_SCOREBOARD.md` §A). Gate #3 **caps** what may be asserted; gate #5 is not reached because nothing here is stated as a probability.

⛔ **NO new prediction.** **LAB-03** (claims breach 250K, **7%**, due 2026-09-30) is the only live forecast this print can touch, and a band-B print in a 54,000-wide gap does not move it; **it resolves ❌ at the 10/1 print unless a ≥250,000 print lands.** **Writing a fresh "claims stay benign" row would be a threshold call in the exact bucket where I am 0-for-5.**

---

## §7 — ROUTING (pre-committed) *(carried)*

| Outcome | Route | Priority |
|---|---|---|
| **Band E** (T-02 fire) | **WALTER** (signal) → REGINALD (all ORANGE→RED), HENRY — **+ CARL if ≥ the §5a bound** | 🔴 |
| **Band D** (ARM T-01) | **WALTER** (signal) → CARL, REGINALD | 🟠 |
| **Band C** | STATUS + brief only | 🟡 |
| **Bands A / B** | STATUS only — **no packet.** Silence = received and integrated | — |
| CC-1 (count → 2 of 4) | STATUS only — two weeks is not four | — |

---

## §8 — DEFECT LOG (fill at grade time — defects in MY work, not the data's)

Pre-registered at freeze:
1. ✅ **L-31 split (`ΔMA` vs `MA_next`) carried; both columns marked with their inputs.**
2. ✅ **Counters carried onto the card with their RESET branches written (V13-b, CC-2)** — a streak rule needs its reset enumerated or the card ships silent on the branch that ends it.
3. 🔴 **L-33 reader guard (new 9/17): the print is read from the extracted text of the saved DOL PDF, never from a fetch tool's summary** — the 9/17 summary fabricated 213,000 / 216,000 / 1,641,000 for a document that says 206,000 / 207,000 / 1,774,000.

## §8b — 🔧 CHECKER SCOPE AT FREEZE: 1 of 4 tables machine-verified, 3 HAND-PROVED (BD-31, expected)

`card_partition_check.py` run at freeze: **see the receipt line appended below §8b** (expected `4 band table(s) — 1 verified, 3 unverified, 0 with defects`, rc=2, `UNVERIFIED` only). ⛔ **`UNVERIFIED` is the tool refusing to certify what it could not read — it is NOT a pass and I am not reporting it as one.** The cause is **BD-31**: the checker reads **one file-global** `partition-axis` declaration and applies it to every table, so a card with four axes can machine-verify only the one declared. **I declared the load-bearing single-print axis (5 bands).** `0 with defects` is the number that must hold, and it holds.

**Hand proof of the three unverified tables** — each is a two-band dichotomy, and ⚠️ **they are NOT all exhaustive on the same terms:**

| Table | Bands | Complement holds because |
|---|---|---|
| §5c continuing claims | `< 1,750,000` / `≥ 1,750,000` | **true complement — exhaustive at any precision.** `<c` and `≥c` partition the reals |
| §5b vector-13 axis | `≤ 199,000` / `≥ 200,000` | **exhaustive on the whole-thousand grid DOL publishes ONLY** — `199,500` is uncovered and cannot be printed |
| §5a T-01 MA axis | `≤ 391,000` / `≥ 392,000` | **whole-thousand grid only**, same caveat. `391,000` is included deliberately: `MA = 250,000` is **not** `> 250,000`. ⚠️ Bounds move on revision — §5a |

🧾 **Checker receipt at freeze (2026-09-17, `card_partition_check.py`, rc=2):** `GRADING_CARD_20260924_claims.md: 4 band table(s) — 1 verified, 3 unverified, 0 with defects` · `[✓] table 2: VERIFIED — axis 'Initial claims, single print', 5 bands, precision 1,000, bounds as written` · tables 4/5/6 `[BAD-DECLARATION]` = the BD-31 one-declaration limit, hand-proved above.

**Freeze authorized on `0 defects` + this written hand proof, exactly as `TEMPLATE_claims_card.md` prescribes for the `UNVERIFIED`-only case.**

---

## §9 — GRADE (write 2026-09-24 off this frozen card — never re-read a band)

**GRADED 2026-09-24 14:4x ET** (PROME-spawned WQ-184 session; the desk was dark at 08:30) — primary: DOL/ETA release PDF, embargo line *"8:30 A.M. (Eastern) Thursday, September 24, 2026"*, `https://www.dol.gov/ui/data.pdf`, **text extracted from the saved binary** (sha256 `4705665b…1b618`, 9 pages) per the L-33 guard. ⚠️ **Reader note:** the first two fetches returned an Akamai `Access Denied` HTML stub (382 B) — a LOUD failure, caught by `file`, never parsed; a browser-header retry returned the PDF. Retained-week cross-check from a second DOL surface: `oui.doleta.gov/unemploy/wkclaims/report.asp` (r539cy national table) — w/e Aug 15 207,000 · Aug 22 204,000 · Aug 29 207,000.

**① Regeneration on the as-published vintage — TWO retained weeks REVISED, so two of the three quantities are VOID and re-solved (as §4 ordered):**

| Week | §1 frozen | As-published 9/24 | Revision |
|---|---|---|---|
| w/e Aug 22 (`R`, rolls off) | 204,000 | **204,000** | none |
| w/e Aug 29 | 207,000 | **207,000** | none |
| w/e Sep 5 | 206,000 | **207,000** | **+1,000** (two-weeks-back; table column + identity below) |
| w/e Sep 12 | 196,000 | **198,000** | **+2,000** (DOL: *"revised up by 2,000 from 196,000 to 198,000"*) |
| **w/e Sep 19 (`X`)** | — | **197,000** | advance |

- Identity check (zero free parameters — every term read from a DOL surface): revised prior MA `(204,000 + 207,000 + 207,000 + 198,000)/4 = 816,000/4 = 204,000` ✅ = DOL *"revised up by 750 from 203,250 to 204,000"*. New MA `(207,000 + 207,000 + 198,000 + 197,000)/4 = 809,000/4 = 202,250` ✅ = DOL. Had w/e Sep 5 stayed 206,000 the prior MA would have been 203,750, not DOL's 204,000 — so the check could have failed.
- **`ΔMA` ✅ STOOD** (`R` unrevised): `(197,000 − 204,000)/4 = −1,750` = DOL *"a decrease of 1,750 from the previous week's revised average"*, to the unit. ⚠️ Against the **as-published 9/17 MA (203,250)** the level move is only `202,250 − 203,250 = −1,000` — the other 750 is the upward revision. Both stated; neither narrated as improvement (§3 rule).
- **`MA_next` column ❌ VOID:** retained sum `207,000 + 207,000 + 198,000 = 612,000` (frozen 609,000, +3,000) ⇒ `MA_next(X) = (612,000 + X)/4`; every frozen `MA_next` value rotted by `3,000/4 = +750` (frozen 197,000 point would have read 201,500; true 202,250).
- **§5a bound ❌ VOID, re-solved:** `X > 1,000,000 − 612,000 = 388,000` (frozen 391,000; moved −3,000 on revision). `388,000 → MA 250,000` does not fire · `389,000 → MA 250,250` fires.

**② Four axes, graded separately:**

| Axis | Reading | Band | Result |
|---|---|---|---|
| §2 single print | 197,000 | **B** | **NO ACTION** |
| §5a T-01 MA | 197,000 ≤ 388,000 (re-solved) | **T01-a** | does not fire; MA 202,250, `250,000 − 202,250 = 47,750` away (vs 46,750 as published 9/17 → +1,000) |
| §5b vector-13 | 197,000 ≤ 199,000 | **V13-a** | **counter 1 → 2 of 4.** Streak re-checked on the REVISED vintage: week 1 (w/e Sep 12) is now **198,000 — still `<200,000`, streak intact** |
| §5c continuing claims | **1,719,000** [w/e Sep 12] < 1,750,000; prior revised **1,730,000 → 1,717,000** (still inside) | **CC-1** | **vector-7 count 1 → 2 of 4.** `1,750,000 − 1,719,000 = 31,000` inside; CC 4-wk MA 1,744,000 |
| band A / Kill B | 197,000 > 185,000 | — | count 0 of 5; `197,000 − 185,000 = 12,000` above |
| T-02 | 197,000 | — | `300,000 − 197,000 = 103,000` away |

⚠️ **Counter fragility, stated so nobody mistakes 2-of-4 for momentum:** the v13 streak rides a **1,000–3,000 margin** (`200,000 − 198,000 = 2,000`; `200,000 − 197,000 = 3,000`), and w/e Sep 12 just revised UP 2,000. **A +3,000 revision to w/e Sep 19 at the 10/1 print would RESET it** — the 10/1 card re-checks week 2 on the revised vintage before counting week 3.

**Colour (graded by NOTHING, §4):** NSA 163,811, `+10,243` WoW (+6.7%) vs seasonal-factor expectation +6.8% — the SA flat is a seasonal-factor-exact week, no gap to explain. NSA YoY `163,811 / 180,992 − 1 = −9.5%`. UCFE 362 (w/e Sep 12). No state in the "largest increases" list above +1,041 (Kentucky).

**③ Written into `STATUS.md`** KEY THRESHOLDS (initial-claims rows + CC row), matrix v7/v13, calendar; narrative → `STATUS_DETAIL.md` § `calendar-graded-20260924`. **Routing (§7): band B + CC-1 ⇒ STATUS only. Nothing routed. Score UNCHANGED 29/75** — a counter at 2 of 4 moves no vector. **No WARN cohort appeared** for the w/e Sep 19 week, so nothing is attributable to a named employer in either direction. **④ Card moved to `docket/graded/`; 10/1 card built same session.**

**§8 defect log at grade:** 0 defects in the card's arithmetic — the void quantities are the ones §4 said would void, and they were re-solved before the level was read. **0 reader defects** (the Access-Denied stub failed loud). **One card-design note:** §1's vintage note ("no revision to any retained week on 9/17") was true at freeze and is not a defect; a **two-weeks-back** revision (w/e Sep 5) is outside the normal prior-week revision and the 10/1 card should expect it can recur.
