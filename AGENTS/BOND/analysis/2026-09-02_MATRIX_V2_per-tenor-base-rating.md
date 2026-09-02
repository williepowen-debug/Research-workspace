# MATRIX_V2 `I'` — PER-TENOR BASE-RATING (owed 9/4, delivered 9/2)

**Session:** BOND 2026-09-02 (Wed) ~19:3x–20:xx ET, PROME-spawned Tier-1 (bond-28) · **Obligation:** Will-ruled 2026-08-20 (MATRIX_V2 adoption) + 2026-08-27 (`PROME/proposals/2026-08-27_matrix-v2-kill-scope-RULED.md`) — *"the 9/4 base-rating MUST report hit-rate and separation PER TENOR"* (`KB-BND-174`) · **Tool:** `monitors/matrix_v2_base_rate.py` (new, no fitted parameters; run under `.venv`) · **Inputs:** `data/auction_history_v2_prome-spawned.csv` (390 rows, 2023-01-10 → 2026-08-13) + TA_WS overlay (5 prints to 8/27) via `grade_auction.load()`; TLT unadjusted closes via yfinance 2022-12-01 → 2026-09-02 (n=940).
**Position impact:** NONE. Nothing here moves a threshold — the ruled dual-print stands until the kill next evaluates 9/8–9/10; **one Will-gated question is raised in §5 and NOT answered here.**

---

## 0. ⚠️ A DEFECT FOUND BEFORE THE TABLE, AND IT CHANGES EVERY 2Y NUMBER THIS DESK HAS PUBLISHED

**The 2Y pool contained 2-Year FLOATING RATE NOTES.** Verified at the TreasuryDirect primary (`TA_WS/securities/search?cusip=…`, 19:3x ET): `91282CRD5` — the "2Y reopening" graded 8/26 with direct 0.36% / dealer 33.08% — is `securityType Note · originalSecurityTerm 2-Year · securityTerm 1-Year 11-Month · floatingRate **Yes**`. So is `91282CPX3` (3/25: indirect 50.91 / dealer 49.09 — **the print that set the 2Y indirect MIN and dealer MAX carried on `PROTOCOL.md` since 8/27**). The corpus files them as `tenor 2Y, security_type Note` with no floating flag; `grade_auction.py` keyed the 2Y bench on `originalSecurityTerm` and filtered only `securityType ∈ {Note, Bond}` — FRNs pass every field the tool looked at. **43 FRN rows sat in the 2Y pool** (TA_WS `type=FRN` returns 51 CUSIPs 2014→2026-08-26; cached to `data/frn_cusips_ta_ws.json`).

| 2Y figure | published (FRN-contaminated) | FRN-clean, same method | Δ |
|---|---:|---:|---:|
| trailing-12 indirect MIN (OLD bar) | 50.91 | **53.21** | +2.30pp |
| trailing-12 dealer MAX (OLD bar) | 49.09 | **24.12** | −24.97pp |
| `I'` 15th pctile, 8/27 snapshot | 55.75 | **54.82** | −0.93pp |
| trailing-12 indirect median (BND-19 leg 1 bar) | 57.65 | **56.54** | −1.11pp |
| 8/27 snapshot "bar − min" | +4.84pp | **+1.61pp** | the "wildly uneven bite" at the 2Y was mostly FRN contamination |

**Verdicts do NOT change:** the 8/25 2Y printed indirect **66.01** — +11.19pp clear of the clean bar (was "+10.26pp"); BND-19 leg 1 passes either bar. **`BND-18/19/20` are frozen letters and grade as written (ruling scope note).** What changes: the `PROTOCOL.md` 2Y outbound-trigger row, the `AUCTION_HEALTH.md` snapshot row, and the sentence *"the 2Y dealer MAX of 49.09 is genuinely that wide"* — **it was not; it was an FRN.** The 8/26 "compositional fact, interpretation withheld" (`KB-BND-175`) is also explained: FRN auctions structurally have ~zero directs.

**Fix shipped:** `grade_auction.py` now excludes `floatingRate == Yes` on the TA_WS path and FRN CUSIPs (live TA_WS list, cached fallback, **raises** with neither) on the corpus path, and prints the exclusion count. **Class:** `[[finding_instrument_measures_a_superset_of_the_thesis_subject]]` — the named series was real, current and reproducible and CONTAINED the subject; every structural check passed. Found only because the base-rating printed the 2Y window (12 auctions in 5 months) beside the other tenors (12 in 11–12 months). **`KB-BND-221`.**

---

## 1. FROZEN `I'` BARS — trailing-12 same-tenor same-TIPS, strictly prior to 2026-09-02, % of COMPETITIVE ACCEPTED, 15th percentile by linear interpolation (the 8/27 7Y = 57.24 reproduces)

| Tenor | n | window | **`I'` bar (P15)** | of-offering | OLD min | median | **bar − min** | prints ≤1pp of bar | dealer max (descriptive) |
|---|--:|---|--:|--:|--:|--:|--:|--:|--:|
| 2Y | 12 | 2025-08-26 → 2026-08-25 | **54.82** | 54.17 | 53.21 | 56.84 | +1.61 | 1 | 24.12 |
| **3Y** ← 9/8 | 12 | 2025-09-09 → 2026-08-11 | **58.90** | 58.65 | 56.50 | 63.34 | +2.40 | 1 | 19.50 |
| 5Y | 12 | 2025-10-27 → 2026-08-26 | **60.27** | 60.16 | 59.24 | 61.75 | +1.03 | 2 | 15.61 |
| 7Y | 12 | 2025-09-25 → 2026-08-27 | **57.24** | 57.15 | 56.42 | 59.91 | +0.82 | 3 | 13.14 |
| **10Y** ← 9/9 R | 12 | 2025-09-10 → 2026-08-12 | **65.05** | 64.88 | 63.95 | 69.94 | +1.10 | 2 | 13.38 |
| 20Y | 12 | 2025-09-16 → 2026-08-19 | **61.72** | 61.10 | 55.17 | 64.95 | +6.55 | 0 | 17.59 |
| **30Y** ← 9/10 R | 12 | 2025-09-11 → 2026-08-13 | **62.93** | 62.83 | 59.95 | 65.99 | +2.98 | 2 | 14.74 |

**Reopening question, disclosed not buried.** The tool's tenor key POOLS reopenings with new issues (10Y/20Y/30Y). The 9/9 and 9/10 legs are reopenings. Reopening-only trailing-12 bars: **10Y 66.32** (Δ +1.27pp vs pooled) · 20Y 64.66 (+2.94) · **30Y 60.28** (−2.65). **The POOLED bar governs** — it is the method every frozen bar, every prior grade and the 8/27 snapshot used, and switching method the week the kill first evaluates would be a mid-flight retune. **If a print lands between the pooled and reopening-only bars (10Y 65.05–66.32 · 30Y 60.28–62.93) the verdict is reported CONVENTION-DEPENDENT and graded both ways** — the same rule adopted 8/27 for the of-offering gap.

**Of-offering vs of-competitive:** gap ≤0.65pp at every tenor (max 20Y 0.62). Same CONVENTION-DEPENDENT rule inside the gap.

---

## 2. HISTORICAL BASE RATE — rolling, strictly out-of-sample (each auction graded on its OWN trailing-12 priors; 224 nominal coupon auctions 2024-01 → 2026-08-27 with ≥12 priors)

| Tenor | N | `I'` fires | **fire rate** | OLD min-only | OLD conjunctive | hit \| fire | med TLT-5d \| fire | n | hit \| no-fire | hit \| all | med \| all |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 2Y | 31 | 8 | 25.8% | 4 | 0 | 25.0% | +0.71% | 8 | 52.2% | 45.2% | +0.26% |
| 3Y | 32 | 5 | 15.6% | 2 | 0 | 100.0% | −1.19% | 5 THIN | 55.6% | 62.5% | −0.53% |
| 5Y | 32 | 9 | 28.1% | 3 | 1 | 33.3% | +0.67% | 9 | 54.5% | 48.4% | +0.01% |
| 7Y | 33 | 9 | 27.3% | 3 | 0 | 44.4% | +0.51% | 9 | 47.8% | 46.9% | +0.14% |
| 10Y | 32 | 5 | 15.6% | 3 | 0 | 60.0% | −1.04% | 5 THIN | 55.6% | 56.2% | −0.12% |
| 20Y | 32 | 7 | 21.9% | 5 | 3 | 42.9% | +0.42% | 7 | 52.0% | 50.0% | +0.09% |
| 30Y | 32 | 9 | 28.1% | 2 | 0 | 66.7% | −0.44% | 9 | 60.9% | 62.5% | −0.32% |
| *pooled (context only)* | 224 | 52 | 23.2% | 22 | 4 | 50.0% | +0.14% | 52 | 54.1% | 53.2% | −0.12% |

*hit = TLT close(t) → close(t+5) < 0, i.e. yields UP after the print — the MATRIX_V2 draft's own yardstick. Auction 1PM, so the auction-day close carries the print.*

### 2a. What the table says, per tenor, in the order the ruling asked for

1. **Fire rate is NOT 15% — it is 15.6% to 28.1% by tenor, 23.2% pooled.** A 15th percentile of a trailing window on a series with a downtrend in indirect share fires above its nominal rate; at the 5Y/7Y/30Y it fires more than one auction in four. **The realized rate is a per-tenor fact and it was measured, not assumed.**
2. **Separation on the draft's yardstick is ZERO or wrong-signed at 5 of 7 tenors.** Pooled: fires hit 50.0% vs 53.2% for all auctions, median TLT-5d **+0.14% after a fire vs −0.12% overall** — a weak-indirect print has been followed by a TLT RALLY more often than not. 2Y/5Y/7Y/20Y hit BELOW their own base rates. Only **30Y (66.7% vs 62.5%, n=9)** is at-or-above base, and 3Y/10Y (100% / 60%) are n=5 THIN and printed only so they are not silently dropped.
3. **Going deeper does not help — it hurts.** Margin tiers (pooled): ≤−1pp hit 43.2% · ≤−2pp 39.3% · **≤−3pp 31.6%** · ≤−5pp 25.0%; **OLD min-only 40.9% (n=22)**; **OLD conjunctive 25.0% median +0.94% (n=4, THIN)**. Two consecutive same-tenor fires: 13/224 = 5.8%, hit 46%, median +0.35%. **Every indirect-keyed variant of "composition failure" this desk has ever carried is followed by TLT UP at the median.** That matches the draft's own dealer finding (>15% median TLT +0.39%, >20% +1.45%): **a print that clears cheap gets bought.**
4. **The difficulty shift Will ruled on is measured: OLD conjunctive 4/224 (1.8%) → `I'` 52/224 (23.2%) — 13× more fires.** 30 of the 52 `I'` fires (58%) would not have fired the OLD min-only test either.
5. **P(≥1 `I'` fire across the three refunding legs) ≈ 49%** at the per-tenor rates (3Y 15.6 · 10Y 15.6 · 30Y 28.1, independence assumed). **On base rate alone it is a coin flip that the thesis KILL fires next week.**

---

## 3. WHAT THIS MEANS FOR THE MATRIX (holds) AND THE KILL (does not, and I am not touching it)

- **Escalation matrix — `I'` as the 🟠 standalone vector escalation STANDS as ruled.** A vector marker is allowed to be a rarity flag; it says "this tenor's foreign/custodial share printed in its own bottom sixth" and nothing more. No claim of TLT predictiveness was ever attached to the vector, and none is now.
- **Thesis kill — the ruled extension gives the kill a ~23%/auction base rate and NO outcome separation.** *"A composition failure at any coupon auction kills the thesis"* under the new definition is a kill that fires on **one auction in four** on history, and the tape after those fires ran AGAINST the direction the kill is supposed to confirm. ⛔ **That is a threshold that cannot discriminate, and the desk that benefits from it firing is this one** (a fire "confirms" the bear thesis). **Disclosed direction, as on 8/27: the new test is easier to fire AND its fires are historically bullish for TLT — so it is wrong in the direction that flatters me.**
- **Nothing moves.** The 8/27 ruling dual-prints both definitions until the kill next evaluates (9/8–9/10). **I will grade the refunding on the dual-print exactly as ruled and report both.** The finding above is the base rate the ruling itself asked for, delivered before the first evaluation, which is the only honest time to deliver it.

---

## 4. FROZEN FOR THE REFUNDING (pre-registered here, 9/2, before any of the three prints)

| Leg | CUSIP | `I'` bar (kill, NEW) | OLD conjunctive (kill dual-print + TLT ADD re-arm, WQ-99) | cover marker (BTC < trailing-12 min) | reopening-only `I'` (disclosed alt) |
|---|---|--:|---|--:|--:|
| Tue 9/8 3Y new | `91282CRL7` | **ind < 58.90** | ind < 56.50 AND dlr > 19.50 | BTC < 2.53 (re-derive at grade) | n/a |
| Wed 9/9 10Y-R | `91282CRF0` | **ind < 65.05** | ind < 63.95 AND dlr > 13.38 | re-derive | 66.32 |
| Thu 9/10 30Y-R | `912810UW6` | **ind < 62.93** | ind < 59.95 AND dlr > 14.74 | re-derive | 60.28 |

**Registered `BND-23`** (55%): `I'` fires at NONE of the three legs — the base-rate complement is 51%, nudged for the 18-benign streak and the 8/11–8/13 refunding's above-median indirect at all three tenors; each leg recorded individually at resolution regardless of the first failure (`BND-19` rule). ⚠️ **`grade_auction.py` still prints the OLD test only** — the `I'` line is read from THIS table until the tool is patched (owed before the old print retires).

---

## 5. FOR WILL, VIA PROME — one question, not answered here

**Does the thesis-kill composition-failure leg stay on `I'` standalone through the refunding, given a measured 23%/auction fire rate with no TLT separation (49% chance of a "kill" on base rate alone across 9/8–9/10)?** Options I can see, each with what I can and cannot base-rate tonight: **(a) leave it** — the ruling's dual-print already prints the OLD test beside it, and the kill is evaluated by a human, not fired by a script; **(b) kill on `I'` + a NON-auction mechanism confirmation** (dealer long-end inventory UP in the FR2004 covering the auction week, or SOFR−IORB > 0 for 3 sessions) — the `DEALER_CAPACITY` discriminator, **not base-rated tonight** (weekly FR2004 join owed); **(c) revert the kill leg to the OLD conjunctive test** — 1.8% base rate, n=4, also no separation. **I recommend (a) for the refunding and (b) for a ruling after it, with the FR2004 join delivered first** — a kill definition should not change the week it first evaluates, and (b) is the only option that tests the MECHANISM the kill is named for rather than the price after it. **Root rule: no threshold moves without a pre-registered letter; this is the letter's base rate, not the letter.**

---

## 6. Apparatus, so it can be attacked

- `monitors/matrix_v2_base_rate.py --asof 2026-09-02` reproduces every number above; `--no-tlt` runs A/B offline. Percentile = numpy linear interpolation on 12 points (P15 sits between the 2nd and 3rd order statistics: 0.35·x(2) + 0.65·x(3)) — a different interpolation moves bars by ≤0.5pp; the 8/27 7Y reproduces at 57.24 so the method is the one already in force.
- TLT-5d is ONE yardstick and a price one; the kill is a mechanism claim. I used it because the draft did, so the comparison is like-for-like with the dealer-drop evidence Will already ruled on. A mechanism yardstick (next-week FR2004, SOFR−IORB) is the owed follow-up, not a substitute I chose silently.
- Independence assumed for the 49% figure; same-cluster fires co-occur (14 pairs ≤3 days apart in the sample), which would push it UP, not down.
- Self-challenge on the apparatus, not the argument: the corpus is a PROME-spawned CSV refreshed to 2026-08-13 whose refresh script carries a documented destroy-on-empty defect (`AUCTION_HEALTH.md` §TOOLING DEFECT) — I did not run it; the overlay is TA_WS's 250-row cap window. A CUSIP present in both was de-duplicated on (cusip, date). The FRN fix depends on TA_WS's `type=FRN` search being complete; 51 CUSIPs 2014→2026 at ~4/yr is the right count.

— BOND
