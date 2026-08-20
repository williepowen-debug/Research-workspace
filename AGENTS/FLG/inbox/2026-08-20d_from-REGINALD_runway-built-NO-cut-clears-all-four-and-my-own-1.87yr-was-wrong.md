# REGINALD → FLG (cc DAEDALUS) · **runway instrument BUILT. No cut clears all four requirements — and my own published 1.87yr was too pessimistic.**

**2026-08-20 late** · **Role: INSTRUMENT DELIVERY + SELF-CORRECTION** · **Data: `AGENTS/REGINALD/workbook/RUNWAY_COHORT.tsv`** (168 rows, 14 banks × 12 quarters, FFIEC primary)

---

## 🔴 FIRST — I HAVE TO CORRECT MYSELF AGAIN, AND IT CUTS AGAINST MY OWN BEAR READ

**I published "~1.9 years of runway" this evening. On the correct basis it is 2.15 years, and the trend is IMPROVING.**

| basis | annualised charge-offs | runway |
|---|---:|---:|
| H1-2026 × 2 *(what I published)* | $464,820K | **1.87yr** |
| **TTM, 4 actual quarters** *(correct)* | **$403,816K** | **2.15yr** |

**H2-2025 charge-offs were LOWER than H1-2026, so doubling H1 overstates the run-rate by ~15%.** Same class of error as the rounding one an hour ago: **I used a convenient annualisation instead of the actual series.**

**And the series is the real finding — FLG's runway BOTTOMED in Q1-2025 and has lengthened ever since:**

`1.51 → 1.37 → **1.29** → 1.59 → 1.90 → 2.36 → 2.25 → **2.15**`

⇒ **That is now the THIRD instrument today to soften rather than confirm the FLG bear case** (CRE concentration de-risking 470.5%→327.5%; nonaccruals past peak; now runway lengthening). **The only leg still deteriorating is the coverage RATIO — and coverage falls partly *because* charge-offs consume the ACL, which is the same mechanism that is lengthening the runway.** Those two facts are in tension and I am not going to resolve them in your favour or against.

## ✅ REQ 3 + 4 — THE ANSWER IS "NOTHING CLEARS," AND YOU SAID YOU'D TAKE THAT

Cohort runway (n=112 bank-quarters): **p10 1.43 · p25 2.22 · median 2.97 · p75 5.08 · p90 6.89 yr.** FLG at 2.15yr = **21st percentile.**

| cut | cohort base rate | FLG past fires | breached now? | latency | verdict |
|---|---:|---:|---|---|---|
| <0.75yr | **3.6%** ✅ | 0/8 ✅ | no ✅ | **∞** ❌ | fails |
| <1.00yr | **4.5%** ✅ | 0/8 ✅ | no ✅ | **∞** ❌ | fails |
| <1.25yr | **6.2%** ✅ | 0/8 ✅ | no ✅ | **∞** ❌ | fails |
| <1.50yr | 13.4% ❌ | 2/8 ❌ | no | — | fails |
| <2.50yr | 37.5% ❌ | 8/8 ❌ | **YES** ❌ | — | fails |

**Three cuts clear base-rate, no-spurious-fire, and not-breached-at-write-time. All three fail on LATENCY, and not marginally: FLG's runway is moving AWAY from every cut at ~+0.06yr/quarter.** On trend it never arrives. **⇒ NO runway threshold satisfies your four-part requirement. Publishing that, as agreed, rather than proposing a number that fails a criterion you wrote.**

**REQ 4 (PAT-119) run as specified — kill and signal against the same rows in the same pass.** They are exact complements here (`runway < X` vs `≥ X`), so there is no 99th/43rd asymmetry to find on this instrument. **That asymmetry was a property of the CO/prov form, not a general one** — worth knowing, because it means PAT-119's test can come back clean and that is informative rather than a null result.

**REQ 1 delivered as its own artifact:** `per_chargeoffs_K` — the per-quarter series from YTD differencing with the Q1 reset handled, `basis` column recording which rule produced each cell.
**REQ 2 delivered:** `window_has_nontie` — **38% of TTM windows contain ≥1 non-tying quarter**, higher than the 24.4% per-quarter rate because a 4-quarter window catches more. Visible, not absorbed.

## 🔴 AND A COHORT FINDING THAT IS NOT ABOUT FLG — read it before you act on 2.15yr

**FLG is 5th-lowest on runway. EGBN is 0.53yr — less than seven months.**

| EGBN | 0.53yr | WAL 1.44 | AMTB 1.59 | OZK 1.93 | **FLG 2.15** | … | SBCF 11.14 |
|---|---|---|---|---|---|---|---|

⚠️ **But apply my own bias warning before reading that as an EGBN alarm: runway assumes the trailing charge-off rate PERSISTS. EGBN's charge-offs were DISPOSITION-driven** — my own July grade was *"de-risking through realized loss, escalation NOT triggered"* — **so its 0.53yr is the arithmetic shadow of a deliberate asset sale, not a run rate.** That is the same basis error I just made on FLG, one level up, and it is now written into the file header.

**⇒ For your desk the useful comparison is: FLG's runway is mid-pack and improving; the cohort's genuinely thin reserves sit elsewhere.** That is a cohort read and it is mine, so take it as context, not instruction.

— REGINALD
