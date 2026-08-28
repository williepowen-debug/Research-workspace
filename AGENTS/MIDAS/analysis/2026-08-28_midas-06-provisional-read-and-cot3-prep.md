# MIDAS-06 — PROVISIONAL READ (Fri 2026-08-28) + Gold COT #3 pre-registration

**Written:** 2026-08-28 ~10:5x ET, **markets OPEN, PRE-SETTLE** (COMEX gold settles 13:30 ET; CFTC COT releases 15:30 ET).
**Author:** MIDAS (orchestrated desk touch under PROME's Will-approved Friday 8/28 slate).
**Status:** ⛔ **PROVISIONAL — NOTHING GRADED HERE.** The final MIDAS-06 grade **STRIKES MON 2026-08-31.**
**Scope:** market legs only. Zero capital. No score, band, threshold or frozen letter touched.

---

## 0. THE RULES THAT GOVERN THIS PAGE (cited, not re-derived)

| Rule | Source | What it forces |
|---|---|---|
| **Frozen letter, NO EDIT** | Will 2026-08-21, WILL_QUEUE row 68 · `PROME/proposals/2026-08-21_midas-rows-65-69-RULED.md` (encoded 8/23) | MIDAS-06 grades on the letter as written. **(d) INDETERMINATE is a legitimate outcome of a frozen spec, not a defect to patch mid-flight.** |
| **Grade-date CLASS ruling, option (i)** | Will 2026-08-27 · `PROME/proposals/2026-08-27_lagged-series-grade-date-RULED.md` | For a lagged-publication series the **named observation date governs** and the grade **waits for publication**. No substitute print instantiates the cell. |
| **L-19 (basis)** | MIDAS 2026-08-21 | A continuous front-month ticker re-points at each roll ⇒ **print the basis with every gold figure**, both bases at grade time. |
| **L-37 (provisional bars)** | MIDAS 2026-08-27 | A date label cannot falsify itself; a settled price can. **Pull twice and diff. Re-confirm T+1.** |

⇒ **MIDAS-06 is a two-day event.** Gold leg reads the **Fri 8/28 settle**, held PROVISIONAL. DFII10 leg is the **8/28-DATED observation**, which FRED publishes **Mon 8/31 ~16:15 ET (H.15)**. **FINAL GRADE STRIKES MON 8/31.** DOCKET row 45 is annotated so nothing reads it overdue over the weekend.

---

## 1. WHICH PRINT EACH LEG WOULD USE

The frozen letter's resolution criteria: *"GC=F close vs $4,340.70 … and $4,050 …; DFII10 [FRED, T+1] vs 2.40 / 2.20 **on 2026-08-28**."*

| Leg | Instrument in the letter | The print that instantiates the cell | Published |
|---|---|---|---|
| **Gold** | `GC=F` close vs **$4,340.70** (branch a) / **$4,050** (branch b) | the **8/28 COMEX settle** | **today ~13:30 ET** — T+1-confirmable **Mon 8/31** |
| **DFII10** | FRED `DFII10` vs **2.40** (a, b) / **2.20** (c) | the **8/28-DATED observation** | **Mon 8/31 ~16:15 ET** ← **THE GRADED CELL** |

**Two DFII10 prints stand between the last published value and the graded cell:**

| Observation date | Publishes | Role |
|---|---|---|
| **2026-08-27** | **today ~16:15 ET** | 🟡 **INTERIM-INFORMATIVE ONLY.** It does **not** instantiate the cell. It narrows what the 8/28 print must do from a two-session move to a one-session move. |
| **2026-08-28** | **Mon 8/31 ~16:15 ET** | 🔴 **THE GRADED CELL.** Nothing substitutes for it. |

⚠️ **Verified at the FRED primary 2026-08-28 10:36 ET:** the series' last observation is **2026-08-26**. The 8/27-dated observation **had not published** at the time of writing. *(Path: 2.44 [8/17] → 2.41 → 2.35 → 2.35 → **2.40 [8/21]** → 2.38 [8/24] → 2.32 [8/25] → **2.34 [8/26]**.)*

---

## 2. LIVE STATE — PRE-SETTLE, EVERY FIGURE LABELLED

### 2.1 The gold leg, on every candidate basis (L-19)

| Basis | 8/27 | Pre-settle 8/28 [~10:4x ET] | vs $4,340.70 | vs $4,050 |
|---|---|---|---|---|
| **`GC=F` live quote** (= GCZ26; see §5) | — | **$4,608.00** | **+6.16%** ✅ | +13.78% above ✅ fails (b) |
| **`GCZ26.CMX`** explicit contract | $4,664.00 | **$4,608.00** | **+6.16%** ✅ | +13.78% above |
| **`GC=F` daily-history bar** (expiring contract — see §5) | $4,609.70 | *(re-points at settle)* | +6.20% ✅ | +13.82% above |
| **`GLD`** ETF cross-check | $422.60 | **$418.60** | *(corroborates; not the graded instrument)* | |

⛔ **PRE-SETTLE. These are in-flight bars, not closes.** Per L-37 the settle must be re-pulled at/after 13:30 ET and re-confirmed T+1 on Monday.

**The gold leg is not close and is not the question.** Every candidate basis clears branch (a)'s $4,340.70 by **≥ +6.16%**.

**Branch (b) is effectively unreachable today.** From $4,608.00 it needs **−12.11%** at the settle, ~2h45m away. On the trailing 2 years of `GC=F` 1-session closes (n=503, sd 1.50%, p05 −2.49%, p01 −3.66%), **zero sessions fell ≥12.11%**; the single worst print is −11.37% and even that sits inside a continuous series that re-points at rolls, so the tail extreme is itself suspect. *(Stated as a distance, not a forecast.)*

### 2.2 The DFII10 leg

| | Value | Source |
|---|---|---|
| **Last published** | **2.34** | FRED `DFII10`, observation **2026-08-26**, verified at primary 8/28 10:36 ET |
| **Branch (a) needs** | ≥ **2.40** | **fails by 6bp**, direction **TOWARD** (was 2.32 [8/25]) |
| **Branch (c) needs** | < **2.20** | fails by 14bp |

**Distance stated as a base rate, explicitly NOT a forecast** — trailing 2y of DFII10 daily observations, n=496 two-session pairs, sd of the signed 2-session change **5.57bp**:

| Event the graded cell would need | Realised frequency, trailing 2y |
|---|---|
| signed 2-session change **≥ +6bp** (⇒ branch (a) yield leg) | **71 / 496 = 14.3%** |
| signed 2-session change **≤ −14bp** (⇒ branch (c)) | **1 / 496 = 0.2%** |
| \|2-session change\| ≥ 6bp (either direction) | 136 / 496 = 27.4% |

⚠️ **These are UNCONDITIONAL rates. They condition on no calendar, no Fed speak, no auction.** They say how far the cell is from each boundary in units this series actually moves — nothing more. **6bp is inside one session's range on this series** (\|1-session Δ\| p90 = 6bp, max 14bp): **a live gap, never a forecast.** *(This is the exact cell where a directional adjective went stale twice — KB-071, n=2. No adjective is attached here.)*

---

## 3. BRANCH-BY-BRANCH PROVISIONAL

| Branch | Frozen condition | Gold leg [pre-settle 8/28] | DFII10 leg [last published, obs 8/26] | Provisional |
|---|---|---|---|---|
| **(a)** DIVERGE PERSISTS → M1 → 4 | gold ≥ $4,340.70 **AND** DFII10 ≥ 2.40 | ✅ **PASS** +6.16% | ❌ **FAIL by 6bp** (2.34) | ❌ **fails on the yield leg — the binding leg** |
| **(b)** decoupling CLOSED → M1 → 2 | gold < $4,050 **AND** DFII10 ≥ 2.40 | ❌ FAIL (+13.78% above) | ❌ FAIL | ❌ fails on **both** |
| **(c)** VOIDED → NO-CALL | DFII10 < 2.20 | n/a | ❌ FAIL by 14bp | ❌ fails |
| **(d)** anything else → **INDETERMINATE**, hold M1 at 3 | residual | — | — | ✅ **SATISFIED — the live provisional grade** |

### ⇒ **PROVISIONAL GRADE: (d) INDETERMINATE.**

**(d) was the pre-registered outcome for exactly this state** and is Will-ruled legitimate (row 68). Prep only. **I will not grade early, and I will not patch the spec.**

**A useful reduction, available once today's settle confirms.** Branch (b)'s gold leg is determined **today**; on any plausible settle it fails. After that, the partition collapses and **MIDAS-06 becomes a ONE-NUMBER grade:**

| The 8/28-dated DFII10 observation [publishes Mon 8/31 ~16:15 ET] | Grade |
|---|---|
| **≥ 2.40** | **(a)** — DIVERGE persists, M1 → 4, re-escalate BOND/LIQUID |
| **2.20 ≤ x < 2.40** | **(d)** — INDETERMINATE, hold M1 at 3 |
| **< 2.20** | **(c)** — test VOIDED as a divergence test, NO-CALL, re-derive |

*(Conditional on the 8/28 gold settle confirming ≥ $4,340.70, which §2.1 prices; the settle is re-pulled at 13:30 ET and re-confirmed T+1 Monday per L-37.)*

---

## 4. WHAT MONDAY NEEDS — the complete list

1. **The 8/28-dated `DFII10` observation** (FRED H.15, ~16:15 ET Mon 8/31). **This is the whole grade.**
2. **T+1 confirmation of the 8/28 `GC=F` settle**, both bases printed (L-19 + L-37). The confirmation and the graded cell land the **same day** — convenient, and not a coincidence to rely on.
3. Then, and only then: author **Kernel activation 2 (`ProposeResolution`)**, whose `outcome_value` **is** the grade. ⛔ Not before. *(Out of scope today by PROME's instruction; noted here so the sequence is not lost.)*

**Interim, today ~16:15 ET:** the 8/27-dated DFII10 observation publishes. It changes nothing about the grade; it converts "6bp over two sessions" into "N bp over one session." **PROME may want the re-ping.**

---

## 5. 🔴 BASIS FINDING — `GC=F` now carries a **three-way** disagreement on a single date, and it sits on the graded instrument

**KB-050 → KB-052 → this. Third instance, and the first one living inside the graded cell.**

The frozen letter names **`GC=F`**. Today that ticker returns **three different values for 2026-08-27** from the same vendor:

| What was asked for | 2026-08-27 value | Volume | What it actually is |
|---|---|---|---|
| `GC=F` **daily history** bar | **$4,609.70** | **1,051** | the **expiring** contract — O=H=L=C flat bar |
| `GCZ26.CMX` **daily history** bar | **$4,664.00** | **151,459** | the real front month |
| `GC=F` **`fast_info.previousClose`** | **$4,631.40** | — | ✅ **IDENTIFIED 11:1x ET — the INTRADAY series' last bar** (KB-087). `GC=F`'s intraday-last for 8/27 is $4,631.40 exactly. **`fast_info` is intraday-sourced, not daily-sourced — never take a settle from it.** |

**Spread: $54.30 (1.18%) across bases on one date.**

**And the discontinuity is live TODAY.** `GC=F`'s 8/28 bar returns **O 4656.00 / H 4688.00 / L 4594.60 / C 4603.00, vol 111,542** — **identical OHLC and volume to `GCZ26.CMX`'s own 8/28 bar.** Meanwhile `GC=F`'s 8/19–8/27 history bars carry volumes of **311–1,336** against GCZ26's **151,459–250,482**.

⇒ **`GC=F`'s history is stitched to the dying contract while its current bar is GCZ26.** The series contains a **~$55 contract gap at the 8/27→8/28 boundary — precisely the boundary MIDAS-06 grades across.**

**Materiality: NOT outcome-determinative, and stated as such.** Every basis clears $4,340.70 by ≥ +6.16% and sits ≥ +13.7% above $4,050. **The binding leg is DFII10, exactly as row 68's own filed observation said.** But per L-19 **both bases are printed at grade time**, and the T+1 confirmation on Monday must record which one the settle came from.

⚠️ **Second-order flag, not built upon:** `GC=F` reports **identical volume for 8/26 and 8/27** (1,051), and so does `GCZ26.CMX` (151,459). A duplicated volume field on consecutive sessions suggests a partly carried 8/27 bar on **both** tickers. Flagged; no figure here rests on it.

### 5.1 L-37's first T+1 confirmation — and it fired

STATUS carried the 8/27 bars as **PROVISIONAL** with an explicit re-pull instruction. The re-pull is done:

| Leg | STATUS 8/27 **provisional** [pulled 21:5x ET 8/27] | **T+1 confirmed** [pulled 10:38 ET 8/28] | Error |
|---|---|---|---|
| Gold `GC=F` | ~$4,633.6 | **$4,609.70** | **+$23.90 (+0.52%) HIGH** |
| Silver `SI=F` | ~$69.50 | **$69.429** | +$0.07 (+0.10%) high |
| Copper `HG=F` | ~$6.6925 | **$6.5870** | **+$0.1055 (+1.60%) HIGH** ← worst |
| Palladium `PA=F` | ~$1,364.5 | **$1,337.60** | **+$26.90 (+2.01%) HIGH** |
| Platinum `PL=F` | ~$1,845.1 | **$1,845.30** | −$0.20 (−0.01%) — **effectively exact** |
| **GLD** (ETF) | **$422.60** | **$422.60** | **EXACT to the cent** |

**Every provisional futures bar that moved was HIGH, and the ETF leg was exact.** GLD closes 16:00 ET on an equity exchange with no Globex roll; futures bars pulled past 18:00 ET absorb the next trade date. ⚠️ **The mechanism is not uniform — `PL=F` was exact too**, so "futures wrong / ETF right" is a tendency, not a law. **L-37's remedy (pull twice, diff, re-confirm T+1) caught all of it; the date label caught none of it.** → **KB-MIDAS-079.**

---

## 6. 🔴 LIVE I2 SIGNAL — palladium is running, the trigger is ON TRACK, and I am NOT firing it pre-settle

**Not part of MIDAS-06.** Reported because it is the largest metals move on the tape today and nobody else on the fleet owns PGMs.

At **10:4x ET (PRE-SETTLE)**: **Pd `PA=F` $1,451.50** · Pt `PL=F` $1,881.60 · gold $4,608.00.

**Betaed, per L-32 (raw percentages across instruments with different betas are not a comparison).** Regression re-run here and it **reproduces the canonical report exactly** — Pt 8/4 residual +6.26% = **3.11σ**, Pd 8/4 +6.72% = **2.69σ**, Pt 8/19 +1.19% = **0.59σ**, matching `reports/2026-08-27_pgm-surge-attribution.md`:

| | β to gold | intercept | residual σ | n |
|---|---|---|---|---|
| **Pd `PA=F`** | **1.1095** | −0.0703 | **2.494%** | 665 (2024-01-03 → 2026-08-26) |
| **Pt `PL=F`** | **1.1492** | −0.0225 | **2.012%** | 665 |

*(n=665 vs the report's 666 = the L-22 missing-value convention fork, one observation. The report stays canonical; these figures corroborate it, they do not re-base it.)*

**The gold denominator has a live contract discontinuity (§5), so the residual is computed on every candidate basis pair rather than one:**

| Basis pair | gold | Pd | Pt | **Pd residual** | **Pd σ** | Pt σ |
|---|---|---|---|---|---|---|
| **A** — GCZ26 both ends *(only internally consistent futures pair)* | −1.20% | +8.52% | +1.97% | **+9.92%** | **+3.98σ** | +1.67σ |
| **B** — `GC=F` daily-history *(cross-roll contaminated; shown to bound only)* | −0.04% | +8.52% | +1.97% | +8.63% | **+3.46σ** | +1.01σ |
| **C** — ⚠️ **MIS-LABELLED WHEN FIRST PUBLISHED; CORRECTED 11:2x ET.** Called *"vendor previousClose"*, which implies a **close**. It is an **INTRADAY LAST**, on a **different contract** than the daily series, and **it is not a settle** (KB-087). Kept as a bound only. | −0.51% | +5.91% | +1.67% | +6.54% | **+2.62σ** | +1.13σ |

**I2 re-open condition (b)** *(`reports/2026-08-27_pgm-surge-attribution.md` §7)*: *a third Pd-led PGM tail event — Pt or Pd residual **>2.5σ** vs gold, **Pd leading** — n=3 is a pattern and demands a mechanism, not another filing.*

- **Pd clears 2.5σ on ALL THREE basis pairs** (+2.62σ to +3.98σ). The finding is **robust to the basis fork**, which is why it is worth reporting despite §5.
- **Pd leads Pt decisively on all three** (+5.91/+8.52% vs +1.67/+1.97%) — the 8/4 signature, and the opposite of the retracted "Pt outrunning Pd ⇒ monetary-adjacent" read.
- **News check (one search, NOT exhaustive):** no dated SA/Russia supply event and no §232 / anti-dumping action surfaced. The named drivers are **standing conditions** — Fed path, supply concentration, hybrid demand. Per the report §4, **a standing condition cannot explain a single-session tail.** ⚠️ **HAWK owns the geopol leg**; this is a prompt to ask, not an attribution.

⛔ **NOT FIRED. NOT GRADED. NO SCORE MOVED. I2 stays 2 🟡.** These are **in-flight bars at 10:4x ET with ~2h45m to the 13:30 settle** — L-37 says a bar that can still move is not a close, and this desk published a mislabelled in-flight bar to Will on 8/20 doing exactly this. **The grade is at the settle, re-run T+1 on Monday.** What is reported here is that the trigger is **live and on track on every basis**, so PROME knows before 13:30 rather than after.

---

## 7. GOLD COT VINTAGE #3 — PRE-REGISTRATION (release 15:30 ET today)

**Release:** Fri 2026-08-28 **15:30 ET** · CFTC **legacy futures-only** · COMEX **full-size** gold, **code 088691** · positions **as-of Tue 2026-08-25**.
**Command:** `python3 AGENTS/MIDAS/cot_gold.py --expect 2026-08-25 --poll 60 --max-wait 3600` (exits 3 = WAIT on a stale vintage).
⛔ **NEVER grade the first response after 15:30** — both the raw file and Socrata serve a clean 200 carrying **last** week's vintage. Poll until the **in-row** as-of date equals 2026-08-25.
**Tool health verified 10:38 ET:** returned the 8/18 vintage, OI reconciled on **both** sides.

### 7.1 The base — independently reproduced

Pulled the CFTC annual history files **2010–2026** directly and re-extracted code 088691. **The 8/18 row reproduces `cot_gold.py`'s print EXACTLY on all five fields.**

| as-of Tue | OI | NC long | NC short | net NC long | **net/OI** | ΔOI | Δnet | **Δ net/OI** |
|---|---|---|---|---|---|---|---|---|
| 2026-07-28 | 384,603 | 219,622 | 37,552 | 182,070 | 47.34% | — | — | — |
| 2026-08-04 | 371,551 | 227,013 | 29,379 | 197,634 | **53.19%** | −13,052 | +15,564 | **+5.85pp** |
| 2026-08-11 | 400,309 | 250,936 | 32,996 | 217,940 | **54.44%** | +28,758 | +20,306 | **+1.25pp** |
| 2026-08-18 | 406,260 | 256,902 | 34,713 | 222,189 | **54.69%** | +5,951 | +4,249 | **+0.25pp** |
| **2026-08-25** | | | | | | | | ← **today 15:30 ET** |

**Level context:** 54.69% = **98.6th percentile** of the 2010–2026 level distribution (median 36.61%, p95 51.67%, max **57.67% [2024-09-17]**). ⚠️ **This window is not truncating the upper tail** — the all-time max on the full 1986–2026 series previously published by this desk (**57.7%**) is the same print and sits **inside** this window. *(Window declared on purpose: L-18 was bought by silently inheriting one.)*

**This is the first print spanning the 8/19–8/21 surge.** The prior vintage's snapshot predates it.

### 7.2 What it keys on — and what it does NOT

- **Keys:** `reports/2026-08-23_gld-rates-attribution.md` **§6 falsifier #3** — the registered positioning falsifier for the 8/19 write-up. *If vintage #3 shows the 8/19–21 surge was **chased**, a meaningful part of that residual is **spec flow**, not premium, and "unexplained" must be re-read as "explained by positioning I hadn't measured yet."*
- ⛔ **Does NOT key:** any `MIDAS-NN` prediction, any DOCKET row, any GATES row. **MIDAS-07 already graded (d) on the 8/11 print.** **Nothing scored moves on this release.** It moves the *interpretation* of the 8/19 residual, and that is a real stake — but it is not a gate.

### 7.3 ⚠️ The falsifier's boundary is a WORD. Pre-registering the number, BEFORE the print.

§6 #3 says **"a large net/OI ratchet from 54.69%"**. Per **L-12**, an unquantified boundary has two defensible answers and the grader picks one under pressure — at 15:31, looking at the number. The only honest fix is to fix it **now**.

**Empirical basis — WoW Δ(net/OI), n=867 weeks, 2010-01-05 → 2026-08-18:**

| | Δ net/OI (pp) |
|---|---|
| mean / sd | +0.01 / **3.31** |
| p25 / p50 / p75 | −1.92 / −0.03 / +1.78 |
| p90 / p95 / p99 | **+4.19** / +5.80 / +9.16 |
| min / max | −12.69 / +15.26 |

⚠️ **A naive "+1.0pp = large" would fire on 34.5% of ALL weeks** — an ordinary week, not a ratchet.
⚠️ **And the unconditional p90 (+4.19pp) would be UNTRIPPABLE from this level** — see below. That is the **L-13 disease**: a band that cannot score the regime you are actually in.

**Conditional on the prior level already ≥ 54.0%** *(n=15 in 16.6 years — small, and stated as small)*:

| | value |
|---|---|
| mean Δ | **−0.46pp** |
| median Δ | **−0.54pp** |
| p90 Δ | **+1.39pp** |
| **max Δ ever observed from ≥54%** | **+2.44pp** |
| P(Δ ≥ +1.0pp) | **13.3%** |

**From an already-extreme level the base case is mean reversion, and the largest ratchet ever recorded from ≥54% is +2.44pp.**

> ### 📌 PRE-REGISTERED BOUNDARY (MIDAS, 2026-08-28 ~10:5x ET, **before the 15:30 print**)
> **"A large net/OI ratchet from 54.69%" ⇒ Δ(net/OI) ≥ +1.4pp WoW, i.e. net/OI ≥ 56.1%** — the **conditional p90** given a ≥54% starting level.

**Authority, stated plainly.** This is a **disambiguation of an unquantified word in my own unregistered write-up** — no MIDAS-NN, no DOCKET row, no GATES row keys on it (checked). It is **not** a re-tune of any registered spec; L-20 / tier test 4 bars that and is not engaged here. **If PROME or Will prefers a different boundary, substitute it** — because:

**No single boundary will be load-bearing.** At 15:30 I will print: **OI · NC long · NC short · net · net/OI · Δ vs 8/18 · the percentile of that Δ against BOTH the unconditional (n=867) and the ≥54%-conditional (n=15) distributions**, and only then the boundary call. The distribution travels with the verdict, so a reader who rejects my boundary can still grade it. *(L-18: the honest interval held where the point estimate failed.)*

---

## 8. WHAT DID NOT HAPPEN

- **No grade.** MIDAS-06 strikes Mon 8/31.
- **No spec touched.** Frozen letter untouched; no threshold, band, or matrix score moved. **Composite stays 7/20; M1 3 🟠; kill-cond #3 FIRED 1/4.**
- **No I2 firing** despite a live >2.5σ Pd residual on every basis — pre-settle bars are not closes.
- **No Kernel work.** Activation-2 authoring is Monday, post-publication, by PROME's instruction.
- **No capital, no trade, nothing trade-shaped.**

---

## 9. RETURNED TO PROME (gated — not mine)

1. **Row 66 (DFII10 NO-VERDICT band)** — design draft written at `analysis/2026-08-28_row66-noverdict-band-DESIGN-DRAFT.md`. **HELD by Will, prospective for successors only. Not applied to any live row.**
2. **The COT boundary in §7.3** — pre-registered by me as a disambiguation of my own unregistered word, and **flagged for substitution** if PROME/Will wants a different one.
3. **I2 band blindness, now at n=3 if tonight's settle confirms** — the evidence packet is mine; **the band change is not** (L-20). If Pd's settle residual clears 2.5σ, the report's own §7 says n=3 "demands a mechanism, not another filing."
4. **`fetch.py` metals settlement source** (KB-047, PROME/FORGE-gated) — §5's three-way basis split is the fourth instance of the defect this would close.
