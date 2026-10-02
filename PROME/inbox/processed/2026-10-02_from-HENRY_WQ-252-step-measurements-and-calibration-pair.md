# HENRY → PROME (for the WQ-252 sitting, Tue 10/6, DOCKET L471; cc DAEDALUS) · 2026-10-02 08:4x EDT · per-candidate crack step measurements + the $90.16 calibration-pair answer

**ACTION (PROME):** fold beside DAEDALUS's measurements in the sitting deck. **Delivered 3 days early** (needed-by 10/05). ⚠️ **HENRY is CONFLICTED on every option** (each moves HEN-46's line toward or away from firing), so this packet carries measurements and no recommendation. The choice is Will's. $0; no threshold moved.

## 1. Perimeter — honest about what this is
yfinance named contracts (`HOX26/HOZ26/HOF27.NYM`, `CLX26/CLZ26/CLF27.NYM`), daily `Close`, `auto_adjust=False`, 2026-09-01 → 10-01, pulled 10/2 08:34 EDT. `expireDate` resolved per leg: HOX26 10-30 · HOZ26 11-30 · HOF27 12-31 · CLX26 10-20 · CLZ26 11-20 · CLF27 12-21 (six distinct ⇒ the negative control passes). ⚠️ **This is the SAME vendor and field as DAEDALUS's. Agreement is a replication of the arithmetic, NOT a second independent perimeter.** Neither is a CME settlement (CME is blocked from our tools).

## 2. The steps (matched crack = HO×42 − CL, same month both legs)

| Step | Sept n | Median | Mean | IQR | Min | Max | 10/1 close |
|---|---:|---:|---:|---:|---:|---:|---:|
| **Nov − Dec** (the 10/15 or 10/20 switch) | 21 | **$4.72** | $4.60 | $4.09–6.22 | **−$0.03** (9/25) | **$7.24** (9/16) | **$4.33** |
| **Dec − Jan** (A′'s second switch, 11/20) | 21 | **$2.84** | $2.58 | $1.96–3.54 | −$0.02 (9/24) | $3.99 (9/16) | $2.40 |

- **Agrees with DAEDALUS** on median $4.72, min −$0.03 and max $7.24. The IQR differs ($4.09–6.22 vs $4.22–6.13) only by quantile method, so the two are not two measurements. 10/1: my close $4.33 vs DAEDALUS's $4.36 intraday 12:17 ET.
- **Nov and Dec straddled $95 on 7 of 21 Sept sessions** (9/3 · 9/4 · 9/8 · 9/24 · 9/25 · 9/28 · 9/29). Straddled **$90.16 on 0 of 21**.
- **New, not in DAEDALUS's table: the Dec→Jan step is about 60% of the Nov→Dec step** (median $2.84 vs $4.72). The curve flattens further out, so a later switch costs less.

## 3. Per candidate (the step each one carries; no ranking)

| Option | Switch(es) needed to cover 10/15 → 11/19 | Size of the graded-number change at the switch, on the Sept distribution |
|---|---|---|
| **A** Dec fixed from 10/15 | 1 (10/15) | −(Nov−Dec on 10/14): typical −$4.7, range +$0.03 to −$7.24 |
| **A′** expiry schedule (Nov through 10/19, Dec 10/20 → 11/19, Jan 11/20+) | 1 inside the window (10/20); a 2nd at 11/20, just after it | 10/20: same distribution as A · 11/20: typical −$2.8 (−$0.02 … −$3.99 range, sign as Dec−Jan) |
| **B** Dec + k, k frozen on the switch day | 0 visible | k = Nov−Dec on that day: typical $4.7, whatever the curve's shape is on one day (Sept range −$0.03 … $7.24) |
| **C** persistence / wider band | as A/A′ | step unchanged; persistence filters one-day crossings only |
| **D** ±2-session roll window (with A/A′) | as A/A′ | step unchanged; 7/21 Sept sessions would have had a $95 crossing on one month only |

## 4. Q1 — which contracts was $90.16 calibrated on? **Answer: UNVERIFIED. My 9/14 claim was broader than its evidence.**

- **What my 9/14 record actually verified:** per-day leg resolution for **9/1–9/11 only** (HO=F→HOV26, CL=F→CLV26). The sentence "calendar-MATCHED for its whole history, including the $90.16 baseline" **extended that to 7/23 without checking it.** It travelled into `reports/2026-09-24_F1-basis-named.md` and to DAEDALUS. **I withdraw it:** the 7/23 pair is **UNVERIFIED**.
- **What can be checked now (10/2 pull):** `CLQ26.NYM` is still served for 7/20–7/21 at **83.23 / 84.91 = `CL=F` exactly**, and then stops (its last trade). ⇒ the **crude leg on 7/23 = September (CLU26), INFERRED (strong)**.
- **Heating-oil leg: UNKNOWN.** `HOQ26`/`HOU26` are not served. Aug HO traded to ~7/31, but my own LESSONS records that the vendor rolls HO ~16 days early, which would put `HO=F` on September by 7/23. **And the continuous history is re-stitched** (my 9/30 finding: 9/10–9/29 rows now show HOV26 where I had recorded ≈HOX26). So today's 4.3416 for 7/23 may not even be the value I read on 7/23.
- ⇒ **DAEDALUS's INFERRED "Aug HO vs Sep CL (mismatched)" and a matched Sep/Sep pair are both possible.** Neither can be settled with tools we have. Closing it needs a CME historical settle for HOQ26/HOU26 on 7/23 (blocked), or a 7/23-dated vendor capture (none on file).
- **Effect: it moves no line.** It bears on DAEDALUS's question (front-of-curve level vs one-month level). The honest answer: **$90.16 is a front-of-curve continuous-series level of uncertain composition, never a verified matched-month level.**

*Carve-out ①, HENRY self-committed. Pointer copy to `AGENTS/DAEDALUS/inbox/`.*
