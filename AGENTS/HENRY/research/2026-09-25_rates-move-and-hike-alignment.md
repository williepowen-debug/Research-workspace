# The rates move 9/15→9/24 (with BOND) + aligning the October-hike probability (with ORACLE)

*PROME packet `2026-09-25_from-PROME_bounded-follow-up-…` (commit `40915c8c0`), Will items 2 + 4. Written 2026-09-25 ~01:1x ET. HENRY owns the rates/futures columns and the alignment method; **BOND owns ACM/KW/auction columns, ORACLE owns venue prices — cited from their files, not re-derived.** $0 · no threshold, gate or row moved.*

## Item 2 — matched-date table

**Column bases and lags (read before any cell):**

| Column | Source | Observation | Publication lag |
|---|---|---|---|
| 10Y nom · 2Y | U.S. Treasury par curve (= FRED DGS10/DGS2, identical on every shared date 9/15–9/23) | session close | Treasury same evening; FRED T+1 |
| 10Y real | Treasury real curve (= FRED DFII10) | close | same evening; FRED T+1 |
| 10Y BE | FRED T10YIE (= nom − real) | close | FRED, 9/24 already posted |
| **KW TP** | FRED `THREEFYTP10` (Kim-Wright: 3-factor, **fits survey forecasts of short rates**) | daily cells | **~1 week — frontier 9/18; cannot see 9/21–9/24** |
| **ACM TP** | NY Fed ACM (5-factor, **yields only, no surveys**) — **BOND's column** | daily | **frontier 9/23 (BOND); cannot see 9/24** |
| post-Oct EFFR | 100 − ZQX26 (no Nov FOMC ⇒ full post-10/28 month) | **vendor last trade ≤15:00 ET** — not CME settlement | same day |
| post-Dec EFFR | ZQZ26 with days 1–9 at post-Oct level: (31·Z − 9·X)/22 | same | same day |
| SR3Z27 · SR3Z28 | 100 − 3M SOFR futures (Dec-27, Dec-28 reference quarters) | same | same day |

| Date (close) | 10Y nom | 2Y | 10Y real | 10Y BE | KW TP | post-Oct EFFR (ZQX26) | post-Dec EFFR (ZQX+ZQZ) | SR3Z27 | SR3Z28 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9/15 | 5.00 | 4.67 | 2.62 | 2.38 | 0.9641 | 3.985 | 4.154 | 4.630 | 4.550 |
| 9/16 | 5.01 | 4.74 | 2.68 | 2.33 | 0.9719 | 4.020 | 4.210 | 4.695 | 4.565 |
| 9/17 | 4.94 | 4.67 | 2.61 | 2.33 | 0.9396 | 4.020 | 4.203 | 4.615 | 4.490 |
| 9/18 | 5.01 | 4.76 | 2.68 | 2.33 | 0.9595 | 4.025 | 4.215 | 4.725 | 4.590 |
| 9/21 | 4.96 | 4.76 | 2.62 | 2.34 | — | 4.025 | 4.222 | 4.710 | 4.560 |
| 9/22 | 4.96 | 4.71 | 2.63 | 2.33 | — | 4.020 | 4.217 | 4.705 | 4.560 |
| 9/23 | 5.11 | 4.85 | 2.76 | 2.35 | — | 4.050 | 4.247 | 4.885 | 4.765 |
| 9/24 | 5.18 | 4.87 | 2.85 | 2.33 | — | 4.060 | 4.257 | 4.895 | 4.785 |
| **Δ 09-15→09-22 (bp)** | -4 | +4 | +1 | -5 | — | +3.5 | +6.3 | +7.5 | +1.0 |
| **Δ 09-22→09-24 (bp)** | +22 | +16 | +22 | +0 | — | +4.0 | +4.0 | +19.0 | +22.5 |
| **Δ 09-15→09-24 (bp)** | +18 | +20 | +23 | -5 | — | +7.5 | +10.3 | +26.5 | +23.5 |

*KW "—" = not yet published, not zero. ACM cells: see BOND's file (pending — `SendMessage` asked 01:0x ET). BOND's standing reading (STATUS L47, `KB-BND-325`): **ACM 10Y TP fell 6.4bp 9/15→9/23 while the 10Y rose 11bp** (same dates in this table: 10Y 5.00→5.11, +11 ✓).*

### What the table says

1. **Two different weeks.** 9/15→9/22 (FOMC week) did almost nothing to the 10Y (−4bp). **The whole move is 9/22→9/24: 10Y +22 = real +22, breakeven 0.**
2. **The near path barely moved; the far path moved as much as the 10Y.** 9/22→9/24: expected EFFR after October **+4.0bp**, after December **+4.0bp** — but 3M SOFR for Dec-2027 **+19.0bp** and Dec-2028 **+22.5bp**. ⇒ **The repricing is "higher for longer" in 2027–28, not the October meeting.** The ~72% October odds (56% → 72%, 9/22→9/24) is a ~4bp event inside a ~22bp move.
3. **Reconciling BOND L47 with HENRY L12 on the same dates:** both are true and they are about different things. HENRY L12 ("all real yield") is a **nominal = real + breakeven** split — it says the move is not inflation compensation; it is silent on path vs premium. BOND L47 (ACM TP −6.4bp while 10Y +11bp, 9/15→9/23) is a **path + premium** split — it says, under ACM, the real-rate rise was expected path. **They are compatible: a real-yield rise can be either path or premium; ACM assigns it to path.** Neither covers 9/24 (+7bp nominal, +9 real).

### (A) Policy-path repricing
- **Support:** SR3Z27 +19 / SR3Z28 +22.5bp in the same two sessions the 10Y rose 22 · 2Y +16 · October odds 56→72% (HENRY FedWatch-method) · ACM TP fell while yields rose (BOND, through 9/23) · breakeven flat (not inflation) · hawkish primary text in the window (Barr 9/23 "further policy adjustments are likely"; flash PMI composite 58.4, input costs steepest in 4 years).
- **Strongest counter:** **3M SOFR futures 2–3 years out are not pure expectations — they carry their own risk premium**, so a term-premium shock also lifts SR3Z27/Z28. The evidence that most supports (A) cannot, by construction, separate (A) from (B) at that horizon. And ACM's "path" is a statistical decomposition that attributes to path whatever its factors cannot price as premium.

### (B) Term-premium / supply absorption
- **Support:** the curve **bear-steepened, belly-led** (9/22→9/24: 2Y +16, 5Y +20, 10Y +22, 30Y +18 [Treasury]) — a hiking-Fed repricing classically flattens (as 8/26→9/16 did, LIQUID) · the move landed on the 9/23 **5Y auction composition failure** (indirect 54.31%, lowest 5Y since 2020-03; BTC 2.21) — BOND · 30Y 5.47 highest since 2004 · KW TP at a 2026 high 0.9719 on 9/16.
- **Strongest counter:** **both models say term premium did NOT rise through their frontiers** — ACM fell 6.4bp to 9/23, KW 0.9641 → 0.9595 over 9/15→9/18 · funding calm (SOFR−IORB −3bp; LIQUID: NONE on every observable) · 5Y dealer takedown 15.77% is ordinary vs 2023–24 (BOND) · **the FR2004 as-of-9/16 print is NOT evidence either way until BOND settles the settlement-timing question (`KB-BND-327`).**

### Preferred interpretation, and the best evidence against it
**Preferred:** **(A), extended — the market repriced the policy path for 2027–28 upward ("higher for longer"), not the October meeting; term premium is not shown to have risen on either model through its frontier.**
**Strongest evidence against:** **the 2-day move is exactly the part no term-premium model can see yet (KW frontier 9/18; ACM misses 9/24), it bear-steepened on a failed 5Y auction, and the futures that carry my path reading embed premium themselves — so on 9/24 I cannot rule out that a supply/term-premium shock is being read as path.** The test that decides it: ACM for 9/24 and KW for 9/21–9/24 when published; if either shows TP up ≥ ~10bp over 9/22→9/24, (A) is wrong for this leg.

## Item 4 — aligning the October probability with ORACLE

| Axis | HENRY (futures) | ORACLE (venues, from ORACLE STATUS L15, pull 21:35–21:48 ET 9/24) | Matched? |
|---|---|---|---|
| **(i) Event** | ZQX26 = November-average EFFR; no Nov FOMC ⇒ **10/27–28 decision + any intermeeting move** | PM "hike-25 at the 10/28 meeting"; Kalshi `KXFED-26OCT` (target upper bound after the Oct meeting) | ✅ **same decision**, with one conversion: futures settle on **EFFR**, venues on the **target range** — assumes EFFR moves 1:1 with the target (EFFR 3.88 = lower bound +13bp, stable since 9/17). Resolution wording: **ORACLE to confirm** |
| **(ii) Time** | 15:00 ET: 95.940. **At ORACLE's stamp: last trade 20:40 ET, 95.945** (no trades 20:40→00:50; 20:10–20:40 vol 126 contracts — thin) | 21:35–21:48 ET | ⚠️ **matched to within ~1h on a thin evening book** — usable, labelled |
| **(iii) Size** | futures measure an **expected change only**: +17.5bp at 20:40 (+18.0 at 15:00). "72%" assumes 25bp-or-hold | PM: +25 66.5 · hold 32.5 · remainder 1.0 (branch unassigned). Kalshi: P(>4.00)=67.0, P(>4.25)=2.0 ⇒ +25 ≈ 65.0, ≥+50 ≈ 2.0 | ✅ **matchable by converting venues to expected bp** instead of converting futures to % |

**Aligned comparison — expected change at the 10/27–28 decision, in bp.** ⭐ **Primary pair = 15:00 ET 9/24** (ORACLE §3 read both venues from each exchange's own price history at that minute; the futures regular session is liquid then). Venue figures cited from `AGENTS/ORACLE/research/2026-09-25_oct-hike-alignment-with-HENRY.md` (`c3695ad88`), not re-derived.

| Source | 15:00 ET 9/24 | ~21:4x ET 9/24 (secondary; thin futures book) |
|---|---:|---:|
| Futures ZQX26 (vendor last trade, not settlement; quote granularity 0.005 = 0.5bp) | **+18.0** | +17.5 (last trade 20:40 ET) |
| Polymarket (ORACLE §3; +50+ branch counted at 50 = lower bound) | **+16.5** | +16.7 |
| Kalshi (ORACLE §3; `>4.25` = whole ≥+50 mass, at the tick floor) | **+16.1 to +16.6** | +17.1 |

⇒ **At matched time the venues price ~+16–17bp and futures ~+18bp: a residual of ~1.5–2bp (≈6–8pp in 25bp-equivalent terms) at 15:00 ET, ~0.4–1bp in the thin evening.** ORACLE's prior "~11–12pp under futures" (KB-ORC-097) compared venues to a secondary 77.5% at an unmatched time and is **SUPERSEDED by ORACLE itself (KB-ORC-100).**

**What cannot be matched (the limitation statement — both desks agree):**
1. **P(hike) itself is not comparable** — futures price only an expected change; my "72%" exists only under a 25bp-or-hold assumption. The comparison is valid in **expected bp only**.
2. **Event basis:** futures settle on **average November EFFR**; venues on the **target upper bound** after 10/28. Sizing the terms (HENRY's domain): **(a) EFFR drift** — EFFR has printed 3.88 on every session 9/17→9/23 [FRED], 12bp under the 4.00 top; a 1bp drift in expected November EFFR moves the futures figure 1bp one-for-one. Month-end (11/30) is 1 of 30 days ⇒ a typical month-end dip of a few bp moves the average **<0.2bp**. **(b) intermeeting moves** — no pricing evidence of one; direction would raise futures, size unmeasured. **(c) futures risk premium** — unmeasured; in a hiking cycle it biases futures HAWKISH, i.e. in the direction of the residual. **(d) last trade vs settlement** — ≤0.5bp at 15:00 on 125K contracts.
⇒ **The ~1.5–2bp residual is the same size as (a)+(c), and (c) points the same way — so it is NOT evidence that venues and futures disagree.** Do not quote "venues lag futures by X". Quotable: *"At 15:00 ET 9/24 both venues priced about +16–17bp for the October meeting and futures about +18bp, before basis adjustments."*
