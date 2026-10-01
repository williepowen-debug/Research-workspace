# $350M sub-notes reset — 2026-10-01 (DOCKET L126 · read L463 Fri 10/2)

**Written:** 2026-10-01 Thu ~12:30 ET · OZK (PROME L0 spawn `prome-0c`) · $0 · no grade, threshold, weight or conviction moved.

## 1. What happened today — SCHEDULED-UNCONTRADICTED (never "confirmed")

| Check | Result | Basis |
|---|---|---|
| FDIC FLNG cert 110 (`scripts/flng_watch.py`) | **rc 0 QUIET** — 182 filings, schema + coverage OK, none after id 11981 (the 8/5 Q2'26 10-Q) | run 2026-10-01 12:14 ET |
| Web search, "Bank OZK" sub-notes redemption/refinancing 2026 | nothing on these notes (the hits were OZK's 2021 redemption of its old 5.50% notes due 2026 and other banks' calls) | search 2026-10-01 |
| Mgmt guidance | "Given the favorable terms … we currently have no plans to replace them" | Q2'26 MC p.32-33 (8-K FLNG 11969) |

⚠️ **Why rc 0 is not proof:** the note's redemption notice goes to holders through the agent/DTC (Fiscal Agency Agreement §8: **at least 10, no more than 60 days** before the redemption date) and needs any required regulatory approval. Neither has to appear as an FDIC filing. So a 10/1 call would have needed a holder notice by **2026-09-21** — nothing at FLNG or in the press says one was given, and none is required to be filed. **Record: reset SCHEDULED-UNCONTRADICTED.**

## 2. The indenture — read at primary (VERIFIED)

Source: FDIC FLNG **5869** (8-K, "Sub Debt Closing", 2021-09-16) — Fiscal Agency Agreement + Form of Global Note (CUSIP 06417N A94); offering circular FLNG 5866.

| Term | Text / value |
|---|---|
| Floating rate from 2026-10-01 | "the Benchmark rate (which is expected to be Three-Month Term SOFR) plus 209 basis points", floor 0 |
| "Three-Month Term SOFR" | "Term SOFR for a tenor of three months that is published by the Term SOFR Administrator [CME] at the Reference Time" |
| **Reference Time (the fixing date)** | **Not fixed in the document.** It is "the time determined by the calculation agent after giving effect to the Three-Month Term SOFR Conventions" (market practice). **The initial calculation agent is the Bank or an affiliate** |
| Day count, floating | **Actual/360** ("360-day year and the actual number of days elapsed") — the 9/24 estimate used 30/360 arithmetic |
| Payment dates | quarterly Jan 1 / Apr 1 / Jul 1 / Oct 1, first floating payment **2027-01-01** |
| Optional call | at par on 2026-10-01 or any later interest payment date, "subject to any required regulatory approval" |

So the 9/24 "indenture SOFR convention unverified" question is answered: **the benchmark is CME 3M Term SOFR (not overnight SOFR), Actual/360, fixing time = calculation-agent market practice.** The usual market practice is two U.S. Government Securities business days before the period starts — **Tue 2026-09-29** for a 10/1 start. That date is **INFERRED** (market practice, not stated in the note).

## 3. Reset coupon

| 3M CME Term SOFR print | Coupon (+2.09%) | Annual interest (Act/360 × 365d) | Q4 period (92d) |
|---|---|---|---|
| 2026-09-24 4.07433% | 6.16433% | $21.875M | $5.514M |
| 2026-09-28 4.07457% | 6.16457% | — | — |
| **2026-09-29 4.09580% (T−2, INFERRED fixing)** | **6.18580%** | **$21.951M** | **$5.533M** |
| 2026-09-30 4.08330% | 6.17330% | $21.907M | $5.522M |

Source of the Term SOFR prints: global-rates.com "3-month CME Term SOFR" page, read 2026-10-01 — **SINGLE-SOURCE secondary** (CME Term SOFR is licensed; sofrrate.com says it is not freely redistributable and shows none). Cross-check on level: overnight SOFR 3.88% (9/29), 3.90% (9/30) [FRED via FORGE fetch.py], after the 9/16 hike to 3.75–4.00%; a 3M term ~20bp over overnight is consistent with the curve pricing some further tightening. Whatever the fixing day in 9/24–9/30, the coupon sits in **6.164–6.186%**.

**Cost versus the old fixed coupon** (2.75% × $350M = $9.625M/yr):
- **≈+$12.3M/yr pre-tax** at 6.18580% (Act/360, 365-day year); **≈+$3.13M** in the first floating quarter alone (92 days).
- **≈$0.09/yr diluted EPS** after tax (22.5% = midpoint of mgmt's 22–23% FY26 guide; 109.6M diluted shares = Q2 NI to common $163.3M ÷ $1.49).
- **Supersedes the 9/24 figure ≈+$11.2M / 5.96% / ≈$0.08**, which used overnight SOFR (3.87%) as a proxy for 3M term and 30/360 arithmetic. The original "+$12.8M / $0.09" (April) was closer than the 9/24 correction — by luck of the SOFR level, not method.
- Tier 2: unchanged — 80% eligible from 10/1 (≈$280M, principal-only simplification) [10-Q p.59; KB-OZK-234].

**When this becomes VERIFIED rather than INFERRED:** the calculation agent is OZK itself, so the bank's own disclosure is the primary — the **Q3'26 10-Q** (FDIC, ~early Nov) should state the floating rate on the notes, or the Q3 MC's sub-notes paragraph. Until then the coupon is DERIVED from an INFERRED fixing date and a single-source print; the range is narrow enough (2.2bp) that no conclusion depends on which.

## 4. What the 10/2 read (DOCKET L463) must check

1. `.venv/bin/python3 AGENTS/OZK/scripts/flng_watch.py` — rc 0 ⇒ log rc + row count + time; record the reset as **SCHEDULED-UNCONTRADICTED** (unchanged rule). rc 1 ⇒ read every new filing: a redemption/refi = 🟠 REGINALD + PROME, and **recalculate** (THESIS §Invalidation 4 — redeem removes the $12.3M cost AND ~$280M of Tier 2); a Q3 earnings-date 8-K ⇒ set CALENDAR's Q3 row. rc 2 ⇒ UNKNOWN, re-run, never quiet.
2. One web search for "Bank OZK" + "subordinated" / "redemption" dated 9/1–10/2 (a press release is the other place a call would show).
3. Nothing else is needed for L126/L463 to close: the coupon question is answered here to the precision available before the Q3 10-Q.

**Forward, not owed on 10/2:** the next par-call date is **2027-01-01**; a call then needs holder notice between **2026-11-02 and 2026-12-22**. `flng_watch.py` stays in boot.py. Recommendation to PROME (its call): a DOCKET row for the Q3 10-Q's floating-rate disclosure (VERIFY the coupon) can ride the existing L520 Q3 row rather than a new one.
