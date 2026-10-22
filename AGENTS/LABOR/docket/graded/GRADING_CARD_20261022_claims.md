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

## §8a — 📎 AMENDMENT 2026-10-21 09:04 ET (before the print; STATUS pickup 2 decided; nothing above is edited)

Basis: `domain/sources/2026-10-21_C2_BASE_RATES_PREREG.md` (definitions committed `f95654e55` before computing; results + script in the same file set).

| Axis | Rule (a FORMULA, L-27 — the level is an illustration) | Assignment |
|---|---|---|
| **§5d v13 return (R13-c)** | `rel = MA_published(w/e Oct 17) / min(published 4-week MA over the 52 weeks before w/e Oct 17)` — recompute the minimum on the vintage at grade time (FRED IC4WSA, or the DOL table where FRED lags). Illustration: min 198,250 (w/e Oct 3) ⇒ bar `1.15 × 198,250 = 227,988` ⇒ needs `X ≥ 315,952` this week (inside band E) | **rel ≥ 1.15 ⇒ v13 1 → 2.** If §2 bands C/D/E also fire, the HIGHER v13 assignment governs; R13-c never lowers a score. rel < 1.15 ⇒ no action |
| **§5c v7 return** | — | **DECIDED: NO RETURN LETTER** (every candidate failed the calm-regime test, fires 21–25% of weeks since 2022). CC-2 stays record-only, as a decision now rather than a gap |

Routing: R13-c alone ⇒ STATUS score + NEXUS brief, no packet (a watch-level move).
🧾 Checker after the amendment (`card_partition_check.py`, 2026-10-21 09:04 ET): 7 band tables — 1 verified, 6 unverified, **0 defects** (BD-31 one-declaration limit). Hand proof for §5d: `rel ≥ 1.15` / `rel < 1.15` is a true complement at any precision.

## §9 — GRADE (write 2026-10-22 off this frozen card — never re-read a band)

*Blank until print. Order: ① regenerate the three §4 quantities on the as-published vintage · ② grade §2 · §5a · §5b · §5c separately · ③ write into `STATUS.md` (KEY THRESHOLDS, matrix v13 if band C+, score, calendar) · ④ `git mv` to `docket/graded/` and build the 10/29 card the same session.*

### §9 GRADE — written 2026-10-22 08:36 ET (PROME-spawned session 84affa50, WQ-479 A / WQ-184 Tier-1 due-row wake DOCKET L719) off the frozen card + §8a amendment

**Primary:** DOL/ETA news release 2026-10-22 08:30 ET, `dol.gov/ui/data.pdf?release=20261022a` fetched ~08:32 ET via the fetch tool (bare `curl` got the 384 B Akamai 403 stub this morning — L-24, the wall flipped again); the tool's summary was NOT used (it returned none); the saved binary (548,860 B, sha256 `6bc739a9…74f8`) was text-extracted with pdfminer; embargo line *"8:30 A.M. (Eastern) Thursday, October 22, 2026"* checked; every figure below grepped in the extracted text (saved: `domain/sources/2026-10-22_DOL_UI_claims_release_text.txt`); the 53-week SA table read by row reconstruction (pdfminer layout). **FRED cross-check (fredgraph.csv, 08:34 ET):** ICSA obs 2026-10-17 194,000 and obs 2026-10-10 200,000; IC4WSA obs 2026-10-17 197,750 — agree with DOL. **CCSA had NOT updated** (newest obs 2026-10-03 1,710,000, the pre-revision vintage) — CC graded on DOL only. KB-LAB-221.

**① Three quantities regenerated on the as-published vintage BEFORE reading the level (the window DID revise — w/e Oct 10 199,000 → 200,000):**

| Quantity | Card (10/15 vintage) | As-published 10/22 | Moved? |
|---|---|---|---|
| `R` (w/e Sep 19) | 198,000 | 198,000 (53-week SA table) | no ⇒ **`ΔMA = (X − 198,000)/4` exact** |
| Retained trio `W2+W3+W4` | 596,000 | `199,000 + 198,000 + 200,000 = 597,000` | **+1,000** |
| `MA_next(194,000)` | `(596,000 + 194,000)/4 = 790,000/4 = 197,500` | `(597,000 + 194,000)/4 = 791,000/4 = 197,750` = **published 197,750 exactly** | **+250 — the vintage-dependent column rotted a fifth week running (L-31)** |
| `ΔMA(194,000)` | `(194,000 − 198,000)/4 = −1,000` | published 197,750 − revised prior 198,750 = **−1,000** | exact ✅ |
| T-01 MA bound | `X > 404,000` | `X > 1,000,000 − 597,000 = 403,000` | −1,000 |

**② Six axes, graded separately (X = 194,000 w/e Oct 17; CC = 1,728,000 w/e Oct 10):**

| Axis | Read | Band | Assignment |
|---|---|---|---|
| §2 single print | 194,000 | **B** (186,000–229,000) | **NO ACTION** |
| §5a T-01 MA basis | 194,000 ≤ 403,000 (re-solved) — also ≤ the frozen 404,000 | **T01-a** | T-01 does not fire; MA 197,750 is `250,000 − 197,750 = 52,250` below |
| §5b v13 `<200,000` | 194,000 ≤ 199,000 | **V13-a** | **record only; no score change** (v13 at floor 1). ⚠️ **The cell's "streak 5 → 6" does NOT hold on the revised trailing run the cell itself names:** w/e Oct 10 revised 199,000 → **200,000**, which is not `<200,000`, so the 5-week run Sep 12–Oct 10 is cut at 4 (Sep 12 198,000 · Sep 19 198,000 · Sep 26 199,000 · Oct 3 198,000) and **the live run is 1 (Oct 17)**. The qualifier governs the number; the count is written as **1**, not 6. Moves nothing either way |
| §5c v7 CC `<1,750,000` | run Sep 5 1,717,000 · Sep 12 1,712,000 · Sep 19 1,699,000 · Sep 26 1,714,000 · **Oct 3 1,703,000 (rev −7,000)** · **Oct 10 1,728,000** (+25,000); `1,750,000 − 1,728,000 = 22,000` inside; w/e Aug 29 1,765,000 bounds the run | **CC-1** | **streak 5 → 6 — record only; no score change** (v7 at 2) |
| §5d R13-c (§8a) | `rel = 197,750 / 198,250 = 0.9975` — min of the published 4-wk MA over the 52 weeks before w/e Oct 17 = **198,250 (w/e Oct 3)**, read in this release's 53-week table (w/e Oct 11 2025 – Oct 10 2026); FRED IC4WSA same | **rel < 1.15** | **no action** |
| Kill B | 194,000 > 185,000 (`9,000` above) | — | 0 of 5 |

**Score 26/75 unchanged** (`26/75 = 34.7%`). **Nothing fired. No cell forced a consequence.**

🔴 **Reading rule applied (§3):** the as-published MA fell **−1,000 to 197,750** — entirely arithmetic: the new week (194,000) is 4,000 under the 198,000 week rolling off, `−4,000/4 = −1,000`. The headline "−6,000" is against a prior week revised UP to 200,000. ⚠️ **Context, graded by nothing:** 197,750 is the lowest 4-wk MA on FRED IC4WSA's current vintage since w/e 2022-10-01 (197,500) — a level fact, not a band; a single benign print is not hawkish fuel, it is nothing (§4).

**Routing (§7):** band B + T01-a + R13-c no action ⇒ **STATUS only**; §5b/§5c are records, not signals. No WALTER signal, no packet.

**Colour, graded by nothing:** NSA initial **172,390** (−19,321, **−10.1%** vs seasonal **−7.4%** expected); yr-ago 205,653 · SA yr-ago 231,000 · CC 4-wk MA 1,711,000 · IUR 1.1% · NSA insured 1,481,260 (+18,771 vs seasonal −3,405 expected) — the CC rise is the one quantity that moved against the seasonal expectation this week; CC is a cost/duration gauge, not early warning (§5c), and no band reads it. UCFE initial 544 (w/e Oct 10, +81). **Florida (NSA, record-only, no card cell):** advance w/e Oct 17 **4,844** (prior week 6,014; DOL notes advance and prior-week state figures are on different bases — not directly comparable); ETA 539 (oui.doleta.gov ar539.csv pulled 08:35 ET, newest state week w/e Oct 10): FL w/e Oct 10 **6,014** vs yr-ago 6,340 (`6,014/6,340 − 1 = −5.1%`); 4-wk `21,737/4 = 5,434` vs yr-ago `23,764/4 = 5,941` ⇒ `21,737/23,764 − 1 = −8.5%` — below year-ago in 13 of 13 weeks w/e Jul 18 – Oct 10 (checked week by week in the CSV). FL insured unemployment w/e Oct 10 26,454 (prior 29,827).

**§8 defect log at grade:** ① L-31 two-clocks split held a fifth week — `ΔMA` exact, `MA_next` off by +250, caught because it was regenerated. ② **NEW, card-design class:** §5b's V13-a cell pre-wrote a streak COUNT ("5 → 6") that a retained-week revision falsified; the band assignment (record-only) was unaffected. Next card writes the count as "regenerated at the print on the revised run", never as a pre-computed number. ③ Instrument, not card: `tools/state_claims_breadth.py` hardcodes `latest='2026-09-05'` and printed the 9/17 numbers verbatim on today's 10/10-vintage file — a reader that looks current and is not; FL figures above computed directly from the CSV. Logged BD-39.
