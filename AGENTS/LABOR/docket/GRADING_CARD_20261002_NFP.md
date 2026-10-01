# 🔒 FROZEN GRADING CARD — NFP SEPTEMBER + HOUSEHOLD SURVEY · Fri 2026-10-02, 08:30 ET

**Written:** 2026-09-24 ~15:xx ET · **8 days before the print** (C2a target was 9/25) · **Status: FROZEN. Grade off this card.**
**Author:** LABOR (PROME-spawned session, WQ-184) · **Consume at:** B5b.
**Companion (evidence TYPES, still valid):** `docket/INDEPENDENCE_MAP_20260904_NFP.md` §1–§3 — CES legs (payrolls, private, revisions, sectors, AHE, hours) are **ONE Type-A witness**; CPS legs (U-3, LFPR, EPOP, LF, LT share) are **ONE Type-B witness.** Write the type, not the count.
**Why a card:** multi-loaded — **freeze-thaw v2 LEG A/LEG B · T-03 · T-04 · T-06 · Kill A · vectors 6, 8, 10, 12 · LAB-12 · LAB-18 · LAB-19 · the WQ-175 ② revision watch.**
**Two carried design rules applied:** **L-27** (§3b is the full U-3 × LFPR cross-product — 12 cells, none omitted) · **L-02** (every bar on a revisable series is frozen as a FORMULA; the number is its value on the 9/4 vintage).

---

## 1. SPINE GOING IN (FRED pulled 2026-09-24 ~15:0x ET; BLS USDL-26-1435 vintage of 2026-09-04)

| Series | Level | Source / as-of |
|---|---|---|
| **NFP August** (first print) | **+162,000** | PAYEMS 159,075 − 158,913; BLS 9/4 |
| Revised run (Mar→Aug) | **214 / 148 / 63 / 31 / 21 / 162** | PAYEMS levels, 9/4 vintage |
| 3-month average | **+71.3K** = `(31 + 21 + 162)/3 = 214/3` | — |
| **U-3 / U-6** | **4.1% / 7.7%** | Aug |
| **LFPR** | **61.6%** (Jul 61.4) | Aug |
| **Labor force** | **169,777K** (+683K) | CLF16OV |
| **EPOP** + referents | **Aug 59.1** · Jul 58.9 · **Jun 59.0 (3-mo referent)** · May 59.2 · Apr 59.1 · **Mar 59.2 (6-mo referent)** | EMRATIO |
| LT unemployed share | **27.0%** (1.9M) | USDL-26-1435 (BLS's own SA share — not UEMP27OV/UNEMPLOY, which gives a different figure) |
| Health care | **+13K** (12-mo avg +32K) | USDL-26-1435 |
| Federal payrolls | **−5K** (ex-USPS −3.3K) | Table B-1 |
| AHE | **$37.75, +3.1% YoY** | USDL-26-1435 |
| 🔎 Diagnostic: aggregate private hours `AWHAE` | **117.2** (Jul 116.8) | FRED — **no band** |
| 🔎 Diagnostic: prime-age LF `LNS11000060` | **108,577K** (May 109,201K ⇒ `109,201 − 108,577 = 624K` below); prime-age LFPR **83.4** (May 83.9) | FRED — **no band** |
| Vectors riding it | v6 **3** · v8 **2** (restore counter **1 of 2**) · v10 **1** · v12 **1** | STATUS |

🔴 **CORRECTION CAUGHT AT FREEZE:** the `docket/CATALYSTS.tsv` 10/2 row carried **"Jun referent 59.1 ⇒ T-03 fires at ≤58.8; LEG B needs ≥59.1"**. **FRED EMRATIO June = 59.0**, so the true bars are **T-03 ≤58.7** and **LEG B ≥59.0** — which is what STATUS § KEY THRESHOLDS and LAB-18 already said. The row was wrong by 0.1pp in both places; repaired this session. **This card uses 59.0.**

---

## 2. 🔒 PRE-COMPUTED ARITHMETIC — as FORMULAS; regenerate on the as-published vintage BEFORE reading September (L-02)

Let `J`, `A` = July and August **as revised in the 10/2 release**; `X` = September first print.

1. **Kill A** (NFP ≥+200K ×3 consecutive, revised). July is +21K on the 9/4 vintage ⇒ ⛔ **Kill A CANNOT FIRE on 10/2** unless July revises to ≥+200K (a +179K revision — outside every observed revision in the vintage table, max +74K first→third). Best case otherwise: 2 of 3.
2. **Freeze-thaw v2 LEG A** = revised single month ≥+150K **AND** revised 3-mo avg ≥+100K. Single-month leg is read on **September** (as the 9/4 grade read it on August). ⇒ **`X ≥ max(150, 300 − (J + A))`** thousand. On the 9/4 vintage `J + A = 21 + 162 = 183` ⇒ `300 − 183 = 117` ⇒ **bar = +150K (the single-month leg binds)**. The average leg binds instead only if `J + A` revises below **150** (a net −33K revision — about the measured one-month mean, so **plausible; recompute**).
3. **LEG B** = EPOP not lower than 3 months prior ⇒ **Sep EPOP ≥ 59.0** (June referent, household data unrevised month to month).
4. **LEG C** = JOLTS NET >0 in both recent months — currently **−18K / −5K ✗**, and JOLTS August prints ~Oct 6, **after** this card. ⇒ **LEG C cannot be satisfied on 10/2**; v2 can fire only as **LEG A ∧ LEG B.**
5. **T-06** = NFP `X` < +100K **AND** U-3 ≥ 4.1 + 0.2 = **4.3%**. A conjunction; BD-13; not relaxed.
6. **T-03 🟠** = EPOP fell ≥0.3pp over 3 months ⇒ **Sep ≤ 58.7** (`59.0 − 0.3`).
7. **T-04 🔴** = fell ≥0.5pp over 6m (**Mar 59.2 ⇒ ≤58.7**) **AND** ≥0.3pp over 3m (≤58.7) ⇒ **Sep ≤ 58.7 fires BOTH T-03 and T-04** — one −0.4pp move from 59.1. Said now so a joint fire is not read as two independent confirmations.
8. **LAB-12** (U-3 ≥5.0%) resolves ✅ only at **U-3 ≥ 5.0%**.

---

## 3. 🔒 PRE-COMMITTED BANDS

### 3a. Headline payrolls, September first print (`X`, thousands) — bounds shown at the 9/4-vintage bar of +150K; if §2.2 re-solves the bar, the top band's lower edge moves to it and band 3a-2's upper edge to one below it

<!-- partition-axis: column="September payrolls, first print" -->
| Band | September payrolls, first print | Assignment |
|---|---|---|
| **3a-1** | ≥ 150,000 | 🔴 **LEG A SATISFIED** (if §2.2 re-solve still reads +150K). Then §3d decides: **EPOP ≥59.0 ⇒ v2 FIRES — stand down vectors 4/6/7 and re-grade the book.** EPOP <59.0 ⇒ not fired; log LEG A met. **This is the registered falsifier; I execute it, I do not argue with it.** |
| **3a-2** | 100,000 – 149,000 | **NO ACTION.** Record. |
| **3a-3** | 0 – 99,000 | T-06 payroll leg **SATISFIED**; fires only jointly with U-3 ≥4.3% (§3b). |
| **3a-4** | ≤ -1,000 | **Negative print.** 🔒 **Moves NO vector by itself** — declared gap §5 (no payrolls vector). T-06 payroll leg satisfied; U-3 decides. |

⛔ Private payrolls, the Jul/Aug revisions and `AWHAE` are **the same CES witness** as `X` — not confirmations of it.

### 3b. U-3 × LFPR — the FULL cross-product (L-27: 4 U-3 states × 3 LFPR states = 12 cells, every one written)

LFPR direction is read against **Aug 61.6%**: down = ≤61.5 · flat = 61.6 · up = ≥61.7.

| U-3 | LFPR | Assignment |
|---|---|---|
| ≥5.0 | down | ✅ **LAB-12 RESOLVES.** T-06 U-3 leg satisfied (fires with `X` <100K). ⚠️ LFPR caveat ON the packet, not instead of the fire |
| ≥5.0 | flat | ✅ **LAB-12 RESOLVES.** Genuine slack; T-06 U-3 leg satisfied |
| ≥5.0 | up | ✅ **LAB-12 RESOLVES.** Genuine slack on an expanding LF — the strongest slack read; T-06 U-3 leg satisfied |
| 4.3–4.9 | down | ⚠️ **NO-SIGNAL on slack** — but T-06's letter has no LFPR clause: **fires if `X` <100K**, caveat on the packet |
| 4.3–4.9 | flat | 🔴 **Genuine slack rising.** T-06 U-3 leg satisfied → fires with `X` <100K → 🟠 CARL + REGINALD + HENRY |
| 4.3–4.9 | up | 🔴 **Genuine slack rising** on entrants — T-06 U-3 leg satisfied, as above |
| 4.2 | down | **No band.** Record |
| 4.2 | flat | **No band.** Record |
| 4.2 | up | **No band.** Record |
| ≤4.1 | down | ⚠️ **NO-SIGNAL** — U-3 falling on the denominator (the CORE TENSION's supply reading). Score nothing |
| ≤4.1 | flat | **No band.** Stable rate on stable participation. Record |
| ≤4.1 | up | 🟡 **ABSORPTION CELL — the one the 9/4 card omitted and that printed.** Entrants absorbed at a flat-or-falling rate = evidence **against** the supply-artifact reading. **No vector moves**; it feeds LAB-19 through the LF letter (§3f), and it is written into CORE TENSION as a second consecutive month if it prints |

### 3c. Net revision to July + August (this release) — vector 8, restore leg 2

| Net revision `(J − 21) + (A − 162)` | Assignment |
|---|---|
| **≥ 0** | **v8 restore-to-3 COMPLETES (2 of 2) ⇒ vector 8: 2 → 3.** Score +1 ⇒ **30/75** |
| **< 0** | Counter **RESETS 1 → 0 of 2** (two CONSECUTIVE prints required, pre-committed 8/28). ⛔ No downward band for v8 exists; none improvised |

⚠️ **Base rate, stated so a ≥0 is not read as a surprise either way:** first→third revisions were negative in **28 of 39** stage-OK months (`workbook/PAYROLL_VINTAGES.tsv`, re-run 2026-09-24, gate PASS, no new vintage since 9/4). The ≥0 branch is the **less** common one. No prediction is registered on it.

### 3d. EPOP (Sep)

| Sep EPOP | Assignment |
|---|---|
| **≥ 59.0** | freeze-thaw **LEG B satisfied** (acts only with 3a-1) |
| **58.8 – 58.9** | No band. Record |
| **≤ 58.7** | 🔴 **T-03 + T-04 FIRE** → CARL + HENRY + REGINALD. **LAB-18 ✅ RESOLVES** on its first draw |

### 3e. Sector lines that carry a registered test *(carried from the 9/4 card, bars re-based)*

| Line | Band | Assignment |
|---|---|---|
| Health care | net-negative | **T-08 FIRES** → 🟠 CARL + REGINALD; **v10 1 → 4** |
| LT unemployed share | <24% ×2 consecutive | v6 3 → 2. Aug 27.0% ⇒ **September alone cannot complete it** |
| LT unemployed share | >27% AND YoY turning positive (issuer's own text) | v6 restores to 4. **Both legs; `27.0` is not `>27`, and a YoY inferred from FRED is not the issuer's text** |
| Federal payrolls | ≤ −25K MoM | T-13 MoM side. ⛔ **v12 moves only with UCFE corroboration in the same session** (BD-17) |
| AHE | any change to the published **+3.1% YoY** | **1c packet to CARL + HENRY.** No threshold, by design |

### 3f. Predictions this print moves — gate #14(a): the bands reproduce the headline

| Row | Headline | Branch (Sep) | P(branch) | Post-print V | `Σ P × V` |
|---|---|---|---|---|---|
| **LAB-18** (T-03 on ≥1 of Sep/Oct/Nov) | 15% | EPOP ≤58.7 | 0.053 | **✅ resolves (1.00)** | `0.053 × 1.00 = 0.053` |
| | | EPOP ≥58.8 | 0.947 | **10%** = `1 − 0.947² = 1 − 0.897` | `0.947 × 0.103 = 0.098` |
| | | | | **total** | **0.151 ≈ 15% ✅** |
| **LAB-19** (LF MoM >0 in ≥2 of Sep/Oct/Nov) | 60% | LF MoM >0 | 0.567 | **81%** = `1 − 0.433²` | `0.567 × 0.813 = 0.461` |
| | | LF MoM ≤0 | 0.433 | **32%** = `0.567²` | `0.433 × 0.321 = 0.139` |
| | | | | **total** | **0.600 ✅** |

Per-draw rates are the registered ones: LAB-18 `0.85^(1/3) = 0.947` survival/draw (registration 9/4); LAB-19 `p` solves `p³ + 3p²(1−p) = 0.60` ⇒ `p = 0.567`. **Monotone in the evidence direction ✅ for both.** ⚠️ **Simplification declared:** LAB-18's no-fire branch is one value; a Sep 58.8 (0.2 from Oct's ≤58.6 bar) deserves more than a Sep 59.2, and I have **not** modelled that split — the C2 grade may move it only with the arithmetic written. **LAB-12:** this card assigns **no** post-print confidence except its resolution letter (§3b); the C2-0 sweep owns any reprice.

### 3g. 🆕 WQ-175 ② REVISION WATCH — registered now, graded on 10/2 and 11/6

- **Object:** August 2026 PAYEMS MoM, **first print +162K** (ALFRED vintage `20260904`).
- **Resolving vintages:** second estimate = ALFRED `20261002`; third = ALFRED `20261106`. Graded **within one vintage** (`level(Aug) − level(Jul)`), exactly as `scripts/alfred_vintages.py` does.
- **Reference distribution** (`workbook/PAYROLL_VINTAGES.tsv`, n=39 stage-OK): first→third mean **−33.5K**, median **−39K**, SD **55K**.
- **Watch lines, diagnostic ONLY — no band, no vector, no threshold:** expected third ≈ `162 − 33.5 = +128.5K`; a third estimate **below `128.5 − 55 = +73.5K`** or **above `128.5 + 55 = +183.5K`** is reported as >1 SD from the measured bias, beside the regime tag (DECELERATING, from first prints).

---

## 4. FALSIFIERS OF THIS CARD

1. **BLS does not publish at 08:30 on 10/2** — ⚠️ **live risk this year: 10/1 is the fiscal-year start, and a lapse in appropriations delays BLS releases.** ⇒ the card **rolls to the actual print date unchanged**; a missing print is not a band, and nothing grades off secondary estimates (ADP, private trackers) in its place.
2. **New population controls or an off-cycle benchmark in the release** ⇒ CPS levels are not like-for-like with §1; §3b/§3d do not grade until the break is measured. *(Not expected — controls land in January.)*
3. **A first-print figure graded where the card specifies the revised series** (Kill A, LEG A, §3c) ⇒ L-02 violation. **Revised back-months FIRST.**
4. **A relayed figure graded instead of the BLS primary** ⇒ do not grade. The primary is read from the saved release text (L-33), never a fetch summary.

---

## 5. 🔴 DECLARED GAP (carried) — there is no payrolls vector

NFP feeds v6/v8/v10/v12 and the exit rules, but the count itself has no score; a negative print moves nothing in the /75. ⛔ **No vector is created on print day** (L-18; it changes the denominator of every published convergence figure).

---

## 6. WHAT TRAVELS

| Outcome | Route | Priority |
|---|---|---|
| **v2 FIRES** (3a-1 ∧ EPOP ≥59.0) | **WALTER** (signal) → CARL, REGINALD, HENRY, NEXUS — the book is re-graded | 🔴 |
| **T-03 + T-04** (EPOP ≤58.7) | **WALTER** → CARL + HENRY + REGINALD | 🔴 |
| **T-06** | **WALTER** → CARL + REGINALD + HENRY, with the §3b LFPR caveat attached where the cell says so | 🟠 |
| **T-08** | **WALTER** → CARL + REGINALD | 🟠 |
| AHE change | 1c packet → CARL + HENRY (direct) | 🟡 |
| v8 → 3 · LAB resolutions · revision watch | STATUS + PREDICTIONS + SCOREBOARD; brief | — |

---

## 7. CHECKER SCOPE AT FREEZE (BD-31)

`card_partition_check.py` receipt: **see line below.** The file-global axis is declared on §3a (load-bearing). §3b is a genuine two-axis table — **12 of 12 cells present by construction**; §3c/§3d are dichotomies/trichotomies proved by hand below.

🧾 **Checker receipt at freeze (2026-09-24, `card_partition_check.py`, rc=2):** `9 band table(s) — 1 verified, 8 unverified, 0 with defects` · `[✓] table 2: VERIFIED — axis 'September payrolls, first print', 4 bands, precision 1,000, bounds as written` · the other 8 are `[BAD-DECLARATION]` under the BD-31 one-declaration limit. ⚠️ **Five of those eight are not band tables at all** (§1 spine, §3e sector lines keyed on different series, §3f/§6/§7 ledgers) — the checker counts every pipe table. ⚠️ **The (a2) cross-product leg did NOT run on §3b** (it sits behind the declaration), so the 12-of-12 claim is **hand-proved, not machine-verified.** A first draft wrote band 3a-4 with a Unicode minus the checker could not parse (`UNVERIFIED-ROW`); rewritten ASCII before this receipt. **Freeze authorized on `0 defects` + the hand proof below.**

| Table | Complement holds because |
|---|---|
| §3b U-3 × LFPR | U-3 `≥5.0 / 4.3–4.9 / 4.2 / ≤4.1` partitions BLS's one-decimal grid; LFPR `≤61.5 / 61.6 / ≥61.7` likewise; all `4 × 3 = 12` pairs written |
| §3c net revision | `≥0` / `<0` — true complement |
| §3d EPOP | `≥59.0 / 58.8–58.9 / ≤58.7` — exhaustive on the one-decimal grid BLS publishes |

---

## 8. GRADE (write 2026-10-02 off this frozen card — never re-read a band)

*Blank until print. Order: ① read the revised J, A from the release; re-solve §2.2 (and §3a's top edge) and §3c's net revision **before** reading September · ② grade §3a–§3e as separate letters, CES and CPS named as two witnesses · ③ apply §3f's post-print values and §3g's watch · ④ write into STATUS (KEY THRESHOLDS, matrix, EXIT RULES LEG A/B, PREDICTIONS, calendar) · ⑤ `git mv` this card to `docket/graded/`.*

---

# 🔧 AMENDMENT 1 — 2026-09-29 10:28 EDT, PRE-PRINT (3 days before the print; no September data exists)

> ⛔ **THIS AMENDMENT CHANGES NO BAND EDGE, NO BAR, AND NO CONFIDENCE.** §3a's four bands, §3b's 12 cells, §3c, §3d's three EPOP bands, §3f and §3g are **exactly as frozen on 2026-09-24.** It corrects ONE frozen INPUT that a release has since overtaken, and the ONE assignment that input fed. The struck text above stays as the record of what was first committed.

**What overtook it.** §2.4 froze *"LEG C ✗ (−18K / −5K) … JOLTS August prints ~Oct 6, **after** this card ⇒ LEG C cannot be satisfied on 10/2."* **JOLTS August printed 2026-09-29 10:00 ET, three days BEFORE this card's print** — the `~Oct 6` date was a modeled date, never docketed in `CATALYSTS.tsv`, never re-verified. Figures at the issuer's own feed (BLS public API, pulled 2026-09-29; FRED agrees):

| Month | Hires | Total separations | NET = H − S |
|---|---|---|---|
| **Aug (P)** | 5,192K | 5,070K | **`5,192 − 5,070 = +122K`** |
| **Jul (revised)** | 5,146K (was 5,054K, **+92K**) | 5,128K (was 5,072K, **+56K**) | **`5,146 − 5,128 = +18K`** (was −18K) |
| Jun (unchanged) | 5,332K | 5,337K | −5K |

⇒ **LEG C = NET >0 in BOTH of the two most recent reference months = Jul +18K ∧ Aug +122K = ✅ SATISFIED on the current vintage.** No JOLTS release lands between now and 10/2 (JOLTS September ~early Nov), so it is the vintage the 10/2 grade reads.

**The corrected assignment (the v2 spec in STATUS § EXIT RULES governs, and it never changed: `LEG A ∧ (LEG B ∨ LEG C)`):**

| Frozen text | Amended |
|---|---|
| §2.4: "v2 can fire only as **LEG A ∧ LEG B**" | **LEG C is TRUE ⇒ v2 fires on LEG A alone.** LEG B (EPOP ≥59.0) is still graded and recorded, but **no longer gates the fire.** |
| §3a-1: "EPOP ≥59.0 ⇒ v2 FIRES … **EPOP <59.0 ⇒ not fired**; log LEG A met" | **3a-1 (LEG A met on the re-solved §2.2 bar) ⇒ v2 FIRES regardless of EPOP** — stand down vectors 4/6/7 and re-grade the book. Record which disjunct carried it: **B ∧ C** (EPOP ≥59.0) or **C only** (EPOP <59.0). |
| §6 routing: "v2 FIRES (3a-1 ∧ EPOP ≥59.0)" | **v2 FIRES (3a-1 ∧ (EPOP ≥59.0 ∨ LEG C))** — same recipients, same 🔴. |

**Caveats that travel with a C-only fire (write them on the packet, not instead of it):** ① July's leg is **`+18K` — 18,000 from zero**, carried there by a +36K NET revision; ② August is **preliminary** and revises with JOLTS September (~early Nov) — a C-only fire can lose its C leg **after** it fires. The spec has no "provisional" state and I will not invent one on print day; if August revises to NET ≤0, that is recorded as a post-fire revision against the fire, graded then.

**Why this is legitimate and not a re-write:** it is written pre-print, it moves the card toward the **bull-side falsifier of my own thesis firing more easily** (the direction a motivated reader would resist), and it restores the card to the spec it was written to execute. Precedent: `docket/graded/GRADING_CARD_20260803_to_0807.md` (pre-print amendment, originals preserved) and `docket/graded/GRADING_CARD_20260910_claims.md` Amendment 1.

**What bought it:** the second modeled-date miss on JOLTS in a month (9/1: docket `~Sep 2`, landed 9/1; 9/29: STATUS `~Oct 6`, landed 9/29). The fix is mechanical — JOLTS is now a dated row in `docket/CATALYSTS.tsv`, so `card_required_check.py` can see it.

*Amendment 1 written by LABOR, self-directed session, Will present. **Grade §3a–§3g off the frozen card; apply this amendment only to §2.4, §3a-1's EPOP clause, and the §6 v2 row.***

---

# 🔧 AMENDMENT 2 — ARMING NOTE, 2026-10-01 12:20 EDT, PRE-PRINT (no September data exists)

> ⛔ **CHANGES NO BAND, NO BAR, NO CONFIDENCE, NO ROUTE.** It writes down, the day before, what each outcome does on the letters above (Amendment 1 applied), the consensus and its source, and who consumes the result. Written by a PROME-spawned session (`prome-0c`) that closes out before the print; PROME re-spawns LABOR after 08:30 Friday to grade.

**1. Inputs unchanged since Amendment 1.** No JOLTS, CPS or CES release between 9/29 and 10/2. LEG C stays **MET** (Jul +18K ∧ Aug P +122K). Claims 10/1 (197,000; MA 200,000) and Challenger Sep (43,281) move no letter on this card. **Release on schedule:** CR runs to 12/11 (per HENRY `STATUS.md`, read 2026-10-01: "BLS/BEA schedules show no lapse notice") — §4 falsifier 1 not live.

**2. The kill bar, confirmed against this file — WALTER's "≥+150K" is right ONLY on the 9/4 vintage.** LEG A = `X ≥ max(150, 300 − (J + A))` thousand on the **revised** Jul/Aug. ⇒ bar stays **+150K** while `J + A ≥ 150K` (net revision to Jul+Aug ≥ −33K); **below that the average leg binds and the bar rises** — e.g. net revision −50K ⇒ `J + A = 133` ⇒ bar `300 − 133 = +167K`. **Recompute from the release before reading September.**

**3. Outcome map (each letter graded separately; CES = one witness, CPS = one witness):**

| If… | Then (pre-registered) | Routed to |
|---|---|---|
| `X` ≥ re-solved LEG A bar | 🔴 **freeze-thaw v2 FIRES** (LEG C carries it; LEG B recorded: **B ∧ C** if EPOP ≥59.0, **C only** if <59.0, with the two C-only caveats on the packet) ⇒ **stand down v4/v6/v7, re-grade the book** | **WALTER** → CARL, REGINALD, HENRY, NEXUS 🔴 |
| `X` 100K – bar−1K | No action | STATUS |
| `X` 0 – 99K | T-06 payroll leg met; **fires only with U-3 ≥4.3%** | if fired: WALTER → CARL, REGINALD, HENRY 🟠 |
| `X` ≤ −1K | moves no vector (no payrolls vector — declared gap §5); T-06 by U-3 | as above |
| Sep EPOP ≤58.7 | 🔴 **T-03 + T-04 fire together** (one move, not two confirmations); **LAB-18 ✅** | WALTER → CARL, HENRY, REGINALD 🔴 |
| Net Jul+Aug revision ≥0 | **v8 2 → 3** (restore counter 2 of 2) | STATUS + brief |
| Net revision <0 | v8 counter resets 1 → 0 of 2 | STATUS |
| U-3 ≥5.0% | LAB-12 ✅ (any LFPR cell) | STATUS |
| Health care net-negative | T-08 fires, v10 1 → 4 | WALTER → CARL, REGINALD 🟠 |
| AHE YoY ≠ +3.1% published | 1c packet | CARL + HENRY direct 🟡 |
| Kill A | **cannot fire** (Jul +21K) | — |
| Aug revision (ALFRED `20261002`) | §3g diagnostic only | STATUS |

**4. Consensus (context, never graded): NFP ≈ +90K, survey range +35K to +180K; U-3 4.1% (some calls 4.2% on a reversal of August's household jump); AHE +0.3% m/m.** Source: Bloomberg economist survey, *"US Jobs Report Seen Showing 90,000 Payrolls, 4.1% Unemployment Rate"* (2026-09-26) — **`[2ND]`, read via a search-tool summary, article not opened (L-33: a summary is a reader).** AHE YoY is quoted as **3.0% and 3.1% by different secondary lines — unresolved, not used.** ⚠️ **The +150K bar sits inside the top of the survey range (+180K), `150 − 90 = 60K` above the median;** August's consensus was ~+53K and it printed +162K. No probability is asserted.

**5. Consumers of the 10/2 result outside my routing (their letters, read at their files 2026-10-01 — not mine to grade):**
- **CARL** — `docket/CATALYSTS.tsv` 10/2: V16 drop-back resolver, print 2 of 2 — *"NFP positive WITH net up-revisions"*. ⚠️ **My v8 leg 2 is `net revision ≥ 0`; CARL's letter says "up-revisions". A net revision of exactly 0 satisfies mine and may not satisfy theirs** — flagged here, CARL owns its letter.
- **HENRY** — STATUS: the October-hike case "rests on ISM 10/1 · NFP 10/2 · CPI 10/14"; logs the market reaction ("LABOR owns the print").
- **BOND** — `docket/CATALYSTS.tsv` 10/2: 2Y / 1y1y reaction and October-hike pricing.
- **REGINALD, NEXUS** — on a v2 fire, T-03/T-04 or T-06 (my §6 routing, via WALTER).

*Amendment 2 by LABOR, PROME-spawned session. Grade off §2–§3g + Amendment 1; this amendment changes nothing gradable.*
