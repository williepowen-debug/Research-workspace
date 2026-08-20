# Bank Exposure Matrix — **v2.0**, rebuilt 2026-08-20

> ## 🔴 THE SCORES CHANGED, AND THE RANKING INVERTED. Read this box before citing any number.
>
> **v1 scores are DEAD** (EGBN 20 · WAL 20 · CFG 15 · OZK 13 · SSB 11 · ZION ~8-9 · FLG 8). They were **not reproducible** — see §5. Do not carry them.
> **The new scale is 0-6, not 0-20+.** A v1 number and a v2 number are not comparable; **compare RANKS, never points.**
>
> | | v1 rank | **v2 rank** | |
> |---|---|---|---|
> | **FLG** | **7th (last)** | **🔴 1st** | ⬅ **the biggest inversion, and it is the finding** |
> | EGBN | 1st= | 2nd= | holds up |
> | **AMTB** | *unscored* | **2nd=** | was never in the v1 table at all |
> | **WAL** | **1st=** | **mid (5th=)** | its bear was always single-credit, never concentration |
> | **CFG** | **3rd** | **last** | clean on both scored channels — ⚠️ **read §4 before concluding "safe"** |
>
> **Why FLG inverted:** it holds the cohort's **highest CRE concentration (327.5%, above the SR 07-1 300% supervisory line)**, the **highest nonaccrual rate (4.88% — 5.5× the cohort median)**, and the **thinnest reserve coverage (ACL/nonaccrual 29%)**. ⚠️ **v1 already knew this** — its own FLG note read *"NYC MF rent-reg"* — **and still scored it last.** A score that contradicts its own notes is the signature of a score nobody could recompute.

**Owner:** REGINALD · **Vintage:** all figures **FFIEC Call Report 2026-06-30**, pulled at the primary 2026-08-20 · **Cohort:** the 14 named MI3-cohort filers (bank-level RSSDs)
**Reproduce:** `AGENTS/REGINALD/scripts/mi3_cohort_screen.py` machinery (FFIEC CDR REST/JWT, `RetrieveFacsimile`/SDF). ⚠️ **JWT expires 2026-11-05.**

---

## 1. THE METHOD — stated, so a reader can recompute the score

**A channel is scored ONLY if it has (a) a named instrument at a primary source and (b) a band anchored to something outside my own judgment.** Channels failing either test are **reported, not scored** (§4) or **pointed at their owner** (§6). *This is the v1 defect the rebuild exists to fix: v1 scored 8 channels, and **not one of them named an instrument**.*

### Scored channel 1 — CRE concentration (0-3)
- **Instrument:** SR 07-1 CRE concentration = **(construction `RCONF158+F159` + multifamily `RCON1460` + non-owner-occupied NFNR `RCONF161`) ÷ total risk-based capital `RCOA3792`**. Owner-occupied NFNR (`RCONF160`) is **excluded**, per the standard.
- **Band anchor — external, not invented:** the **300% supervisory line** in SR 07-1 itself.
- `≥300% = 3` · `200-299% = 2` · `100-199% = 1` · `<100% = 0`
- ✅ **VALIDATED against a company disclosure before use:** computed EGBN **258.2%** vs EGBN's own Q2-2026 disclosed **267.6%** → **−9.4pp (3.5% relative)**. ⚠️ **v1 carried EGBN at 497% AND 547% — both ~2× wrong**, from an ambiguous denominator (its section header cited SR 07-1's total-risk-based-capital while its column header read "CRE/Tier 1"; on Tier 1 the figure is 279.9%, still nowhere near 497%).

### Scored channel 2 — Credit quality (0-3)
- **Instrument:** nonaccrual loans `RCON1403` ÷ total loans `RCON2122`; reserve coverage = ACL `RCON3123` ÷ nonaccrual.
- **Band:** nonaccrual `≥2.0% = 2` · `1.0-1.99% = 1` · `<1.0% = 0`; **plus 1 if ACL/nonaccrual < 100%** (reserves do not cover the nonaccruals already recognised). Capped at 3.
- **Why this band is defensible:** the coverage leg is not a judgment call — **<100% means the reserve is arithmetically insufficient for loans already on nonaccrual**, independent of any view.

**TOTAL = channel 1 + channel 2. Maximum 6.**

---

## 2. THE SCORES — with the arithmetic shown

| Rank | Bank | CRE conc | pts | Nonaccrual % | ACL/NA % | pts | **SCORE** |
|---|---|---:|:--:|---:|---:|:--:|:--:|
| 🔴 1 | **FLG** | **327.5%** | 3 | **4.88%** | **29%** | 3 | **6** |
| 🟠 2= | **EGBN** | 258.2% | 2 | 2.05% | 88% | 3 | **5** |
| 🟠 2= | **AMTB** | 218.4% | 2 | 2.46% | 51% | 3 | **5** |
| 🟡 4 | VLY | 319.5% | 3 | 0.88% | 128% | 0 | **3** |
| 5= | OZK | 259.5% | 2 | 0.92% | 154% | 0 | **2** |
| 5= | WAL | 161.1% | 1 | 0.86% | 86% | 1 | **2** |
| 5= | SSB | 281.0% | 2 | 0.53% | 217% | 0 | **2** |
| 5= | BKU | 193.9% | 1 | 0.95% | 95% | 1 | **2** |
| 5= | SBCF | 229.6% | 2 | 0.66% | 210% | 0 | **2** |
| 10= | ZION | 151.7% | 1 | 0.47% | 226% | 0 | **1** |
| 10= | MTB | 103.9% | 1 | 0.84% | 180% | 0 | **1** |
| 10= | CUBI | 179.2% | 1 | 0.31% | 293% | 0 | **1** |
| 13= | CFG | 95.3% | 0 | 0.96% | 137% | 0 | **0** |
| 13= | HBAN | 83.4% | 0 | 0.84% | 204% | 0 | **0** |

**Three banks carry reserves that do not cover their own recognised nonaccruals: FLG 29% · AMTB 51% · EGBN 88%** (WAL 86% and BKU 95% are marginal). That is the single most decision-relevant column in this table.

---

## 3. WHAT THE RE-SCORE CONFIRMS — and it is consistent with everything else this desk found in 2026

**Severity is CONCENTRATED, not tier-wide** — the same verdict as the FL small-tier watch-card (4-of-4 REVERT, closed 8/10) and the Q1 cohort NCO decomposition (Hypothesis A, 6/8). **3 of 14 names carry a materially elevated score; 8 of 14 score ≤2.** The v1 framing — eight channels, six at 🔴+, a tier-wide detonation — is not what the instruments show.

⚠️ **But the concentration is at DIFFERENT NAMES than v1 believed.** The desk's attention has been on WAL and OZK; on instrumented CRE concentration and credit quality, **FLG, EGBN and AMTB** are the elevated names and **WAL and OZK are mid-pack**.

---

## 3b. ⚠️ FLG TRAJECTORY — added 2026-08-20 PM after a DAEDALUS challenge. **It qualifies the top score and I am not burying it.**

**DAEDALUS asked, against the standard set in §1:** *can the SR 07-1 ratio RISE on a SHRINKING denominator?* — i.e. is FLG's 327.5% an artifact of balance-sheet shrinkage rather than CRE risk? **The right question, and it is answerable at the primary. 11 contiguous quarters pulled:**

| | 2023Q3 | 2026Q2 | change |
|---|---:|---:|---|
| CRE numerator (constr + MF + non-OO) | $48.33B | **$32.76B** | **−32.2%** |
| Total risk-based capital (denominator) | $10.27B | $10.00B | **−2.6% — essentially FLAT** |
| **SR 07-1 ratio** | **470.5%** | **327.5%** | **−143pp, and it FELL IN ALL 11 QUARTERS** |

**⇒ HYPOTHESIS REFUTED, and not narrowly: the ratio is not rising — it has fallen 143pp — and the denominator is not shrinking (capital is flat), so a shrinkage artifact is arithmetically impossible here.** The fall is driven **entirely** by a numerator down a third.
✅ **But DAEDALUS's composition intuition was RIGHT:** multifamily *is* the stickiest leg — construction **−55.6%**, non-OO CRE **−40.8%**, multifamily only **−28.6%**. It just does not produce the artifact, because capital held.

### 🔴 What this DOES change — the level score stands, the story around it does not

**FLG's 3/3 on channel 1 is a LEVEL score and it is correct: 327.5% is above the 300% supervisory line today.** But **the direction is hard, monotonic de-risking, and at this rate it crosses below 300% in roughly two quarters.** Reading "cohort-worst CRE concentration" as *deterioration* is wrong. **This is the EGBN §5 discriminator again — de-risking through a shrinking book vs deterioration, same arithmetic, opposite conclusions** — and on channel 1 FLG is the EGBN case.

### ⚠️ The credit leg answers DIFFERENTLY, and this is where the real signal is

| | peak | 2026Q2 | read |
|---|---:|---:|---|
| Nonaccrual $ | $3.51B [25Q1] | $2.99B | **−15% off peak — improving** |
| Nonaccrual % | 5.49% [25Q3] | 4.88% | **past peak — improving** |
| **ACL $** | $1.27B [24Q2] | **$0.87B** | 🔴 **−31.5%, and it has fallen in EVERY ONE of the last 8 quarters** |
| **ACL / nonaccrual** | 87% [24Q1] | **29%** | 🔴 **monotonic deterioration** |

**⇒ The reserve is being drawn down ~1.7× faster than the problem book is resolving** (ACL −26% vs nonaccrual −15% from their respective peaks). **Nonaccruals improving while coverage deteriorates monotonically for 8 quarters is NOT the de-risking signature** — at EGBN the ACL was *consumed by disposition*; here the ACL is falling against a book that is still $3.0B of nonaccruals.

**⇒ NET, and it is a better read than the one shipped this morning: FLG's score of 6 SURVIVES, but its two legs point in opposite directions. Channel 1 is de-risking (level high, trajectory good). Channel 2 is the live concern, and the load-bearing figure is the 29% coverage — NOT the 4.88% nonaccrual rate, which is past its peak.** Anyone acting on FLG should act on the reserve line.

### 🔴 §3b-ii — ACL ROLL-FORWARD (added same evening, answering FLG-desk's promoted Q2b). **The drawdown is NEITHER disposition NOR release.**

Schedule RI-B Part II, FLG, 2026 H1 — **ties to the dollar**: begin $1,029,999K + recoveries $55,488K + **provision $15,923K** − **charge-offs $232,410K** = **$869,000K**.

**⇒ NOT "release"** — provision is POSITIVE every quarter; reserves were never reversed into income. **⇒ NOT clean "disposition"** either — at EGBN the ACL was consumed by disposition *and* the concentration left the balance sheet; here the reserve is eaten by realized losses **and not replenished.**

| | provision | charge-offs | CO/prov |
|---|---:|---:|---:|
| FY2023 | $781.1M | $210.7M | **0.3× building** |
| FY2024 | $1,101.6M | $874.5M | 0.8× |
| FY2025 | $180.3M | $436.1M | **2.4× draining** |
| **2026 H1 ×2** | **$31.8M** | **$464.8M** | **🔴 14.6×** |

**Provisioning collapsed −97.1% from FY2024 to the 2026 annualised rate while charge-offs held near half a billion a year.**
🔴 **$869M reserve ÷ ~$465M annualised charge-offs ≈ 1.9 YEARS of runway** at the current pace, against a still-**$2,988M** nonaccrual book.
⚠️ **And it reframes the "improving" nonaccrual leg: a nonaccrual rate falling while $232M is charged off in six months is partly MECHANICAL. A rate falling by charge-off is not a rate falling by cure, and the roll-forward nets — it cannot separate them.** Composition is single-name depth ⇒ **FLG-desk's, not mine.**
⚠️ **Caveats carried: `RIAD` is YTD (the ×2 is my annualisation, not a company figure); 6 of 11 quarters do not tie by the identity (adjustments/M&A, gaps −$12.9M…+$64.8M) though BOTH 2026 quarters tie exactly; and there is no peer base rate on CO/provision yet — 14.6× is not yet established as unusual.**

⚠️ **This is exactly why §7 says "do not read direction from this table."** A level score cannot distinguish a bank getting worse from one working down a large legacy book — **only the series can, and the series had to be pulled to find that the two channels disagree.** `[[finding_verified_figures_do_not_verify_the_shape_claim]]`

---

## 3c. 🔴 RESERVE RUNWAY — a THIRD instrument, built 2026-08-20 eve. **It reorders the cohort and it needs a companion to be read at all.**

**Runway = ACL ÷ TTM charge-offs.** Data: `workbook/RUNWAY_COHORT.tsv` (168 rows, per-quarter charge-offs derived from YTD with the Q1 reset handled).

| | EGBN | WAL | AMTB | OZK | **FLG** | CFG | MTB | HBAN | ZION | VLY | SSB | SBCF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **runway (yr)** | **0.53** | 1.44 | 1.59 | 1.93 | **2.15** | 2.69 | 3.02 | 5.03 | 6.27 | 6.63 | 7.51 | 11.14 |

*Cohort p10 1.43 · p25 2.22 · **median 2.97** · p75 5.08 · p90 6.89.*

### ⛔ THE INSTRUMENT'S BIAS IS INVERTED — read this before using any number above

**Runway assumes the trailing charge-off rate PERSISTS. A bank taking DISPOSITION-driven charge-offs therefore prints a catastrophic runway *because it is cleaning up*.** ⇒ **the metric fires hardest on the healthiest subject.**

🔴 **EGBN at 0.53yr is exactly that case, and this desk has the evidence in its own file: the July grade was *"DE-RISKING THROUGH REALIZED LOSS, escalation NOT triggered"* — CRE concentration 295.1%→267.6%, below the supervisory line, ACL consumed by disposition of classified assets.** **0.53yr is an asset sale's arithmetic shadow, not a run rate.**
⇒ **Do NOT rank on runway without a disposition discriminator.** Unqualified, this column would put EGBN top and be wrong about why.

### And it CORRECTED this desk's own published figure

**FLG runway was published earlier the same evening as ~1.87yr (H1-2026 × 2). TTM is 2.15yr** — H2-2025 charge-offs were lower, so doubling H1 overstates by ~15%. ⚠️ **A convenient annualisation standing in for the actual series** — the same shape as a threshold typed from a rounded display value.
**And the series inverts the story: FLG's runway BOTTOMED at 1.29yr [2025Q1] and has LENGTHENED every quarter since** → 1.29 · 1.59 · 1.90 · 2.36 · 2.25 · **2.15**.

⇒ **THREE of the four instruments now point AWAY from the FLG bear case** (CRE concentration de-risking · nonaccruals past peak · runway lengthening). **Only the coverage RATIO still deteriorates — and it falls partly BECAUSE charge-offs consume the ACL, which is the same mechanism lengthening the runway.** ⚠️ **Those two are in tension and this desk does not resolve it.**

### ★ The generalisation, and it is the day's main methodological output

**Every instrument built today needed a SECOND instrument to tell two opposite stories apart** — de-risking vs deterioration (CRE concentration), cure vs charge-off (nonaccrual), disposition vs release (ACL), asset-sale vs run-rate (runway). **A level scores a state; only the series says which direction produced it.** This is why §7's "do not read direction from this table" is a structural limit of the matrix and not a disclaimer.

---

## 4. 🔴 REPORTED, NOT SCORED — and a 0 here is NOT a clean bill of health

**These are measured at the primary and carried on every row, but they DO NOT enter the score, because no defensible band exists.** Scoring them would be inventing a threshold.

| Bank | MI3 v1a (hidden CRE) | PC-NDFI % of loans | NDFI nonaccrual |
|---|---:|---:|---:|
| EGBN | **10.77%** *(cohort max)* | 0.00% | $0 |
| MTB | 9.69% | 3.95% | $7.0M |
| WAL | 8.99% | 7.50% | **$122.5M** |
| CUBI | 5.96% | **19.96%** *(cohort max)* | $0 |
| OZK | 5.46% | 8.58% | $25.9M |
| **CFG** | 4.20% | **10.66%** | $0.1M |
| VLY / FLG / BKU / HBAN / ZION / SSB | 4.69 / 2.83 / 3.29 / 3.06 / 1.70 / 0.87 | 2.73 / 1.75 / 2.18 / 3.80 / 1.93 / 0.63 | — |

**Why unscored — the honest reason:** on 2026-08-13 this desk **base-rated** the MI3 ratio and retired its >20% flag **with no successor**, because any cut between 12-20% is a re-description of two banks' own volatility (EGBN's 4-quarter spread is 12.69pp, OZK's 16.37pp, every other bank ≤2.15pp; effective n≈14, not 56). **PC-NDFI has no base rate at all yet.** A threshold without a base rate is a number I would be picking to fit.

⚠️ **⇒ READ THIS BEFORE CONCLUDING ANYTHING ABOUT CFG.** CFG scores **0** on the two scored channels and carries the **2nd-largest private-credit NDFI exposure in the cohort (10.66% of loans, ~$15.9B funded + $22.5B unfunded ≈ $44.5B committed).** **A 0 means "clean on CRE concentration and credit quality," NOT "low risk."** Same caution for CUBI (score 1, PC-NDFI 19.96%) and MTB (score 1, the cohort's largest absolute MI3 book at $4.95B).

---

## 5. 📛 WHY v1 WAS REBUILT RATHER THAN REFRESHED — the reproducibility failure, recorded

**The v1 scores could not be derived from v1's own method.**
- v1's stated rule: **🔴=3 · 🟠=2 · 🟡=1** across **8 channels** (CRE, NDFI, DC, BDC, CONS, FHLB, GEO, MUNI) → max 24.
- v1's own convergence table computes **EGBN 12** and **WAL 12**.
- `STATUS.md` carried **EGBN 20** and **WAL 20** as canonical.
- **There is no derivation of 20 anywhere in the repository.** Git archaeology found no rescale commit, no scale note, no method document. ⇒ **anyone citing "EGBN 20" could not reproduce it** — `[[finding_loadbearing_number_must_be_reproducible]]`.

**Compounding defects, all now moot:** v1's tables disagreed with `STATUS` *and with each other* (EGBN 11 vs 12, CFG 8 vs 9, ZION 6 vs 9); **OZK was absent from the scoring table entirely** despite being a live watchlist name; EGBN's CRE concentration appeared **twice at two values** (497% / 547%), both ~2× the primary; and the Hidden-CRE Screen table ranked banks on the **defective ÷item-4 basis** whose rank the basis itself inverts.

**Archived v1:** `archive/BANK_EXPOSURE_MATRIX_v1_2026-02-23.md` — history only.

---

## 6. UNSCORED CHANNELS → THEIR OWNERS (pointer-only; this desk does not re-derive them)

v1 scored these without instruments. They are real channels; they are **not mine to measure**, and a matrix that scores them on my impression is worse than one that points.

| Channel | Owner | Live state (consumed, not re-derived) |
|---|---|---|
| CMBS maturity / CRE recognition | **CREED** | `CREED-T-02` **FIRED** 8/20 (matured-balloon share >50, effective the June print). ⚠️ CREED's own read: **pre-transmission** — mechanism speed `QUARTERS`, perimeter is securitised paper, not bank-held. `CREED-T-03` (FDIC non-owner CRE PDNA) is the bank-relevant one and has **NOT** fired; **FDIC Q2 QBP ~8/24-29**. |
| Private credit / BDC | **BROCK** | BDC non-accruals ~2.8%, decade high (chart-read, conf 0.65). Bank-side exposure is §4 above. |
| Federal layoffs / DC | **LABOR** | Claims 206K [wk 8/15] — direction turned, +17K off the 7/18 low, but LABOR's read is a **low-fire freeze, not employment transmission**. |
| Consumer credit | **CARL** | — |
| Geography (FL / TX) | **CORAL / MARCO** | FL small-tier card CLOSED 4-of-4 REVERT (8/10). |
| Funding / FHLB | **REGINALD + BOND** | System advances **$810.7B** [6/30]; `REG-T-06` at **leg 2 of 3** on a sustain-3-quarters spec — does **not** fire; fires on the Q3 print if >700. |
| Rates / AOCI | **BOND** | 30Y 5.28%; `DFII10` 2.41 = ~96.7th pct of its own history. AOCI reinclusion nets to **capital RELIEF** for Cat III/IV, phase-in to 2032 — see `CALENDAR.md`. |
| Muni | *unowned* | ⚠️ v1 scored this channel; **no live instrument exists on this desk.** Dropped rather than carried on a Feb-vintage impression. |

---

## 7. WHAT THIS MATRIX DOES NOT DO

- **It is not a short-ranking.** v1 ended in a "SINGLE-NAME SHORT CANDIDATES (FINAL RANKING)" section that mixed exposure with M&A floor and expression. **Trade construction is TERRY's**; this file ranks *measured exposure* only.
- **It is a point-in-time cross-section, not a trajectory.** One quarter. `RCON2746` was shown cohort-wide to be **step-prone** (17/154 = 11.0% of QoQ transitions), so single-quarter Call Report levels move for reporting reasons as well as economic ones. **Do not read direction from this table.**
- **It scores 2 channels, not 8** — and that narrowing *is* a finding, not a gap. Six of v1's eight channels had no instrument on this desk; §6 points them at owners rather than pretending to measure them.
- **Cohort ≠ population.** These are 14 named filers selected by earlier MI3-era priors. **Extending the sample can move a rank** — demonstrated 8/20 when a cross-sectional coefficient collapsed from −0.559 (n=14) to −0.255 (n=26). `[[finding_extend_the_sample_before_publishing_a_coefficient]]`

---

## 8. REFRESH

**Cadence: QUARTERLY, alongside the MI3 cohort screen — next due 2026-11-07 (2026Q3).** Same credential, same RSSDs, same JWT (⚠️ expires **2026-11-05**, two days prior). This is a scheduled pull, not event-driven: the clock advances when the Call Report publishes.
**If this file reads stale after ~2026-11-10 that is neglect, not design.**

*Supersedes v1 (2026-02-23). Rebuild authorised by Will in-session 2026-08-20 ("okay lets rewrite the matrix"). Score changes propagated to `STATUS.md` §Convergence Matrix and `CLAUDE.md` §Bank Watchlist the same session.*
