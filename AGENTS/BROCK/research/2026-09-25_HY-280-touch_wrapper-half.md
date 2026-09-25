# HY 280 touch — the WRAPPER half (BROCK, Will-directed spawn via PROME prome-2e)

**Written:** 2026-09-25 Fri 13:1x ET (`date` 13:10:03 EDT at write start). **Scope:** W1–W4 of PROME's spawn prompt (Will: *"Okay I would like to investigate the HY credit spreads."*). LIQUID owns the HY tape; this file covers the wrapper side only. **$0 · no threshold moved, no score moved, no standing approval moved.** ⚠️ **One registered gate FIRED AS WRITTEN (GATE-BRK-R2 leg (a), §W1-C).** A fire is a change of state under the gate's own wording, not a move of its level, and no score changes (the vector is already at its 5 ceiling).

---

## HEADLINE (four lines)

1. 🔴 **GATE-BRK-R2 (a) FIRED, found at SEC primary this session: North Haven Private Income Fund LLC (Morgan Stanley's non-traded BDC, CIK 0001851322) accepted about 43.8% of units validly tendered in Q3-2026.** Source: SC TO-I/A acc 0001193125-26-395654, accepted 2026-09-18T20:41:23Z. That is its **third consecutive quarter below 100%** (Q1 47.8% final · Q2 41.6% final · Q3 43.8% preliminary). The preliminary sits far under P7's 94.0% buffer, which was pre-registered at commit `8a6cbcc93`, **2026-09-18 12:16:49 ET, 4h25m BEFORE the filing was accepted.** ⚠️ **The filing sat unread for 7 days** because my own cadence model dated it ~10/01 (see §LESSON).
2. **W1: on the widening leg itself (FRED cells 9/22 → 9/24, HY OAS 268 → 280), the wrappers LAGGED.** On price the wrapper basket fell −1.75% and the manager basket −3.23%. Beta-adjusted, the wrappers came out +0.47% versus their fitted move (noise: 0.3σ). The spread decomposition also points the wrong way: **CCC/BB COMPRESSED 6.891 → 6.780**. **Both legs of my pre-registered 8/28 arming test (b) fail.** The structural finding is **UNCHANGED**: no instrument that can grade "wrappers lead managers" has appeared since 8/28. The one new instrument, GATE-BRK-R2, is by its own letter "evidence for re-adjudication, not a re-arm".
3. **W2: APO's print is a sector-wide alt-manager move plus a hedge roll, not a wrapper-stress signal.** Over 9/22 → 9/24 APO fell −2.79%, the middle of its peers (OWL −6.38 · BX −5.48 · ARES −3.70 · KKR −2.84). Apollo's own wrapper, Apollo Debt Solutions BDC (ADS), says Q3 redemption requests *"declined sequentially"*.
4. **W3: the $1.1B CoreWeave-linked data-centre junk bond was sponsored by affiliates of Blue Owl. It priced at 98.5 to yield 9.25%, about 2.7pp over similarly-rated debt** (Bloomberg 9/23, secondary; read via search snippet, body not read). The same week, Oracle sent a force-majeure notice on Jupiter, where Blue Owl is landlord. **Blue Owl is the one node where the wrappers DID lead their peers: OBDC −3.05% and OTF −2.10%, versus ARCC −1.19, FSK −1.24 and BXSL −0.53.** That is a SPONSOR move, not a broad wrapper move.

---

## W1 — Are the wrappers LEADING or LAGGING?

### W1-A. Spread tape (FRED via `fetch.py fred`, pulled 2026-09-25 ~13:07 ET; LIQUID owns the series — cited, not scored)

| FRED cell | HY OAS | CCC | B | BB | IG | CCC/BB | 10Y (DGS10) |
|---|---|---|---|---|---|---|---|
| 9/11 | 265 | 1,076 | 273 | 150 | 80 | 7.173 | 4.96 |
| 9/16 | 270 | 1,076 | 278 | 155 | 78 | 6.942 | **5.01** |
| 9/17 | 270 | 1,076 | 277 | 156 | 78 | 6.897 | 4.94 |
| 9/18 | 268 | 1,083 | 273 | 155 | 77 | 6.987 | 5.01 |
| 9/21 | 266 | 1,077 | 270 | 153 | 77 | 7.039 | 4.96 |
| 9/22 | 268 | 1,075 | 271 | 156 | 77 | 6.891 | 4.96 |
| 9/23 | 273 | 1,093 | 278 | 159 | 77 | 6.874 | 5.11 |
| 9/24 | **280** | 1,112 | 286 | 164 | 79 | **6.780** | (n/a at pull) |

**Two normalizations, and they disagree** (`[[finding_level_and_rate_look_like_agreement_until_you_name_which]]`):
- **In bp, CCC led:** +37 vs B +15 vs BB +8 (9/22 → 9/24).
- **Proportionally, CCC lagged:** CCC +3.4% · B +5.5% · BB +5.1% · HY +4.5%. **My 8/28 test (b) is written on the RATIO: "CCC/BB EXPANDING through the move." It COMPRESSED.** On the normalization I pre-registered, this is a quality-broad, beta-led widening, not tail-led.
- The context fits that reading: the 10Y move was real-yield-led (HENRY via WALTER −003: +22bp real, breakeven flat), and a week of record AI-linked HY supply (SoftBank ~$11.1B, WALTER −006/−012; the $1.1B Blue Owl DC deal). **INFERRED, not tested.**
- ⛔ The standing guard is carried: BB-led widening is never logged as bank-convergence progress.

### W1-B. Wrapper equity vs HYG vs managers (yfinance, `auto_adjust=True` total return; pulled 2026-09-25 ~13:08 ET; 9/25 figures are INTRADAY)

| Window | HYG | Wrapper basket (ARCC·FSK·OBDC·BIZD) | Six-BDC card (OCSL·OBDC·OTF·ARCC·FSK·MFIC) | Manager basket (APO·ARES) | Test (b) price leg: wrappers fall MORE than managers? |
|---|---|---|---|---|---|
| **9/22 → 9/24** (the widening leg, 268 → 280) | −0.99% | **−1.75%** | −1.98% | **−3.23%** | ❌ **NO: managers led by 1.5pp. Sixth wrong-sign print** |
| 9/17 → 9/24 (HY 270 → 280) | — | −3.85% | −4.22% | −4.17% | ❌ NO (−3.85 vs −4.17) |
| 9/17 → 9/25 intraday | −1.21% (px) | −4.39% | −4.73% | −3.51% | ✅ raw yes, but the window ends on a day with no FRED HY cell yet, and CCC/BB compressed over it ⇒ (b) still fails on its decomposition leg |

**Beta-adjusted residuals.** Bivariate OLS on HYG and SPY daily total returns, 250 sessions to 9/16, fitted out of sample. Wrapper residual daily sd 1.19%, manager 2.12%.

| Basket | β_HYG | β_SPY | 9/22→9/24 actual / residual | 9/17→9/25 actual / residual |
|---|---|---|---|---|
| Wrappers | 1.87 | 0.33 | −1.75 / **+0.47** (0.3σ) | −4.39 / −2.23 (−0.8σ) |
| Six-BDC | 1.90 | 0.28 | −1.98 / +0.24 | −4.73 / −2.43 |
| Managers | 1.31 | 1.16 | −3.23 / −0.74 (−0.2σ) | −3.51 / −2.60 (−0.5σ) |
| OWL | 1.63 | 1.34 | −6.38 / **−3.16** | −7.18 / −5.32 |

**Read.**
- On the widening leg, the wrappers moved LESS than their credit-plus-equity beta implies: they lagged.
- The wrappers' extra weakness over the longer window is concentrated on **9/18** (ARCC −1.3%, OBDC −1.6%, FSK −3.8% close-to-close). **HY OAS TIGHTENED 2bp that day while the 10Y printed 5.01.** ⇒ Whatever weakness the wrappers showed before the widening co-moved with the RATE leg, not the credit leg. **INFERRED:** that fits my Duration vector (VX-BRK-020), not X1. None of the residuals clears 1σ.

**Sponsor split inside the wrapper basket (9/22 → 9/24):** OBDC −3.05 · OTF −2.10 · OCSL −2.34 · MFIC −1.99 · FSK −1.24 · ARCC −1.19 · BXSL −0.53 · BIZD −1.53. **Blue Owl's two vehicles are among the worst** (OBDC worst), and OWL itself fell −6.38%. That is the sponsor-bifurcation vector (already 🔴🔴 5, no rescore), not a broad wrappers-lead move.

### W1-C. NAV, marks and redemptions at primary (EDGAR submissions feed, pulled 2026-09-25 ~13:08 ET)

**Monthly non-traded NAV, August vs July** (every figure from the vehicle's own 8-K Item 8.01/7.01):

| Vehicle | 7/31 NAV/sh | 8/31 NAV/sh | Δ | 8-K (Aug NAV) |
|---|---|---|---|---|
| BCRED (Class I) | $23.64 | $23.60 | −0.17% | 0001803498-26-000053 (9/22); aggregate NAV $43.0B → $43.2B |
| OCIC (Class I) | $9.09 | $9.14 | **+0.55%** | 0001812554-26-000053 (9/23); aggregate $18.6B → $18.7B |
| ADS | $23.83 | $23.84 | +0.04% | 0001193125-26-397997 (9/22) |
| Monroe Income Plus | $9.77 | $9.75 | −0.20% | 0001742313-26-000059 (9/21) |
| North Haven LLC (purchase price, Aug-1 vs Sep-1 subs) | $17.89 | $17.86 | −0.17% | 0001193125-26-401046 (9/24) — ⚠️ purchase price, INFERRED = prior month-end NAV |

⇒ **The August marks are flat (−0.20% to +0.55%). They are month-end marks published about three weeks later, so they CANNOT lead a 9/22–9/24 move by construction.** The first September NAV prints arrive around 10/20–10/23. **No private-credit CDS or secondary-marks figure was found or attempted; I hold no instrument for it.** UNKNOWN, not zero.

**Redemptions — GATE-BRK-R2 legs since my 9/18 grade:**

| Vehicle | Filing | Q3-2026 issuer-stated figure | Effect on R2 |
|---|---|---|---|
| **North Haven PIF LLC (graded registrant)** | SC TO-I/A 0001193125-26-395654, 2026-09-18T20:41:23Z | *"accepted for purchase approximately **43.8%** of the Units … validly tendered and not withdrawn … on a pro rated basis"*; requests ~**11.4%** of units vs 5.0% cap; *"nearly two thirds of repurchase requests … associated with unitholders whose repurchase requests were prorated in the prior two repurchase offers"* | 🔴 **(a) FIRES: third consecutive sub-100% (47.8 → 41.6 → 43.8).** Preliminary ≤94.0% ⇒ counts immediately under P7. (b) not in play (43.8 > 25, and (b) grades on the FINAL only) |
| North Haven Fund A (not counted, P2) | SC TO-I/A 0001193125-26-395623 | 73.3%; requests ~6.8% | Corroborating parallel series only. Wedge 29.5pp (Q1 25.4 · Q2 27.8) — the structural wedge persists |
| ADS | 8-K 7.01 0001193125-26-398001 (9/22) | Requests ~**14.7%** of shares; *"will honor … 5%"*; *"requests declined sequentially"*; *"vast majority … re-tendering"*; net outflow ~$0.5B (~3% of NAV); preliminary | **ADS run 0 → 1** (first ISSUER-STATED sub-100% quarter; Q1/Q2 were inferred-only, and P9 says an inferred quarter breaks a run). No fire |
| ASIF (EXCLUDED by Will's WQ-219 ruling — data only) | SC TO-I/A 0001104659-26-110205 (9/24) | 13.1% tendered, **38.2%** to be repurchased (Q2 34.7%) | None: excluded vehicle |
| BCRED · OCIC · Monroe · CCLFX | NAV/credit-facility 8-Ks only (OCIC 1.01 revolver amendment 9/16) | none | No change: BCRED 2 · OCIC 2 (Q3 expires ~9/30, final ~late Oct) · Monroe 1 · CCLFX 0 |

⚠️ **The counter-evidence travels with the fire:**
- Demand at North Haven is **flat, not rising**: requests ~10.5% (Q1, derived) → ~12.0% (Q2, derived) → 11.4% (Q3, stated).
- **About two-thirds of Q3 requests are RE-TENDERS from prorated holders.** Fresh demand is roughly 3.8% of units (INFERRED: 1/3 × 11.4%), under the 5% cap.
- ADS says the same about its own queue.
- ⇒ The fire measures a **persistent queue behind a hard 5% cap**, i.e. a liquidity-mismatch structure that is holding. **It does not measure accelerating flight.** The gate was built to detect exactly this, and it fired on it; the gate does not size, and it opens no capital path.
- Under the 6/26 shared-antecedent verdict the fire adds **no convergence score**: the redemption-gates vector is already 🔴🔴 5.

### W1 — THE ANSWER TO PROME'S STRUCTURAL QUESTION

- **Level vs structure.** Everything since 8/28 moved the LEVEL (HY 263 → 280 · CCC/BB 6.739 → 7.173 → 6.780 · R2 fire). **Nothing changed the STRUCTURE.** X1's wrapper half is still a RELATIVE claim, and every new instrument is absolute:
  - R2 is a per-vehicle count.
  - Monthly NAVs are one vehicle at a time and lagged about three weeks.
  - LIQUID's KB-LIQ-083 is absolute, as ruled 8/28.
- **The R2 fire routes to LIQUID as "evidence for re-adjudication, not a re-arm"**, per the GATES row's own consequence cell. I am not re-opening the gate.
- **What WOULD change it (pre-registered 8/28, restated, not altered):**
  - **(b)** A down-leg in which the wrapper basket (ARCC/FSK/OBDC/BIZD) falls MORE than APO/ARES **while CCC/BB EXPANDS**. This week both legs failed. The ratio is the leg to watch: it fell from 7.173 [9/11] to 6.780 [9/24].
  - **(a)** A mark instrument that carries a MANAGER leg: wrapper FV/Cost + NAV ΔQoQ against a manager-marks comparator. **The first gradable window is Q3 reporting, ~10/28–11/10** (APO/ARES/BX/KKR earnings plus BDC 10-Qs).
- ⚠️ **Self-flag carried from 8/28:** "wrappers are beta-insensitive" is the WEAK explanation, and this week it partly held (the wrappers' residual on the widening leg is positive). The verdict still rests on the relative/absolute ground, not on that explanation.

---

## W2 — APO: wrapper stress, or an idiosyncratic/hedge print?

| Fact | Figure | Source |
|---|---|---|
| APO | **$121.18 (+0.41%)** live 2026-09-25 ~13:05 ET; $120.69 [9/24c] | `fetch.py price` / yfinance |
| APO 9/22 → 9/24 vs peers | APO −2.79 · KKR −2.84 · ARES −3.70 · BX −5.48 · OWL −6.38 | yfinance closes |
| Oct-16 put open interest after 9/24 | $105 **20,378** (9/24 vol 20,024) · $115 **20,269** · $110 3,044 (vol 10,521) · $125 1,972 | yfinance chain, 2026-09-25 ~13:09 ET |
| Dec-18 $95P (the book's contract) | bid 1.00 / ask 1.40, last $1.25 [9/24 16:59Z], vol 5, OI 266, IV 43.8% | yfinance chain, same pull |
| Apollo's own wrapper (ADS) | Q3 requests ~14.7%, *"declined sequentially"*, mostly re-tenders; Aug NAV $23.84 (+0.04% MoM) | 8-K 0001193125-26-398001 / -397997 |

**Read.**
- **This is not wrapper stress.**
  - APO sits in the middle of an alt-manager selloff led by OWL and BX, the two with named AI-data-centre nodes (see W3). It is not an outlier.
  - The record put volume matches a **~20k-lot matched roll**: $110/$125 closed, $105/$115 opened (KB-BRK-302, morning). The post-session open interest now confirms the two ~20k new legs.
  - A hedge being rolled down and up-sized is **HEDGE MANAGEMENT**. Whether it is a long hedging or a directional short is **unknowable from open interest.**
  - Apollo's own wrapper reports **falling** redemption demand and a flat NAV.
- **Rule on the Dec $95P:**
  - EXIT §2 "APO reclaims $130 sustained → reassess" FIRED 8/12. **Will ruled HOLD, no monetization, 2026-08-13** (`PROME/proposals/2026-08-13_private-credit-batch-RULED.md` §②).
  - ⚠️ **Correction to the spawn prompt's framing:** the prompt says the contract has *"NO ruling"*. It has one. FORGE's row was corrected today (`FORGE/STATUS.md` APO row: *"corrected 2026-09-25 from 'No ruling on file' on BROCK's flag, PROME-verified at the record"*).
  - Other live levels: cross-agent line "APO breaks $100 → ALL 🔴" is 17.5% away ($121.18); the §2 $130 reassess is 7.3% away.
  - The vehicle-mismatch flag stays live (a short on APO equity fights the fee-economics tailwind of a private-credit thesis).
  - **No trade proposal. Any disposition is Will's.**

---

## W3 — AI-infra / DC financing, from the wrapper side

| Item | Figure | Source / basis |
|---|---|---|
| CoreWeave-tied DC (Richmond VA), **developer sponsored by Blue Owl affiliates** | **$1.1B, 5-year, priced 98.5 to yield 9.25%, ~2.7pp above average yield for similarly-rated debt**; Goldman lead | Bloomberg 2026-09-23 (headline + search-engine summary; ⚠️ body NOT read — SECONDARY). Earlier: Goldman sounded out $1.15B (Bloomberg 8/19); a sister CoreWeave-tied DC raised $900M on 6/02 |
| Oracle Jupiter force majeure → Blue Owl/STACK (landlord) | 9/24 | VULCAN own read (WALTER −007); VULCAN owns the tenant side |
| OWL equity | −6.38% (9/22 → 9/24); −23.1% TR 8/28 → 9/25 | yfinance |
| Blue Owl BDCs | OBDC −3.05% · OTF −2.10% (9/22 → 9/24) vs ARCC −1.19 · BXSL −0.53 | yfinance |
| CRWV | $87.61 (−2.79%) live 9/25; +3.9% 9/22 → 9/24 | fetch.py / yfinance |

**Read.**
- The financing channel is **CONCENTRATED IN ONE SPONSOR THIS WEEK: Blue Owl.** It is the landlord on the Oracle project that just declared force majeure, it sponsors the CoreWeave-tied issuer that had to pay about 270bp over its rating cohort to clear, and it manages the two wrappers that underperformed the BDC complex.
- The market is **still clearing** AI data-centre paper, but at a **concession**. Two AI-linked HY deals cleared in one week (SoftBank >2× covered).
- **What I do NOT have:**
  - BDC-level exposure to these specific issuers. No Q3 Schedule of Investments exists before ~early Nov; Q2 SOIs are not re-read in this 60-minute scope.
  - Any private-credit DC loan mark.
  - ⇒ "Private-credit DC exposure repricing this week" is **UNKNOWN at the loan level.** Only the equity of the sponsor and its vehicles repriced.
- Routes: the credit-structure call on the deal is LIQUID's (AI-financing carve-out); the tenant side is VULCAN's. I own the sponsor/vehicle read above.

---

## W4 — CRMT (L479)

**Filings: unchanged since this morning's grade.** EDGAR feed through 2026-09-25 ~13:08 ET: last filing 8-K 0001171843-26-006216 (9/24 20:05Z); the STD is still Thu 10/1. **Price moved: $1.10 (−19.12%) live ~13:05 ET, from $1.36 [9/24c].** This is the first session to price the fourth bridge, and it priced it DOWN.

---

## LESSON (BROCK-local → LESSONS #28 candidate)

- **What P7 did:** it modelled North Haven's Q3 preliminary /A at ~10/01, from **one** cadence observation (Q2: expiry → preliminary +19d).
- **The register already held a second:** Q1 was expiry 3/07 → preliminary 3/11, **+4d**. Q3 came out expiry 9/14 → preliminary 9/18, +4d.
- **Cost:** the fire sat unread for **7 days**. My morning 9/25 session swept the EDGAR feed for CRMT only.
- **Rule:** a filing-date model built from n=1 of an n=2 series is a forecast I chose not to check. And a gate whose earliest read is MODELLED needs its population's feeds swept at every session, not on the modelled date (`[[finding_a_warning_dated_on_its_own_event_fires_too_late]]`, the early-arrival mirror of it).
- **Mechanical fix, proposed not built:** each session greps the six population CIKs' submissions for `SC TO-I/A` since the last session. The query above did it in one call.

## 10Y ATTRIBUTION CORRECTION (WALTER SIG-W-20260925-003, verified at FRED this session)

- FRED DGS10 shows **5.01 on 9/16**. My record said the 9/21 L347 downgrade premise ("10Y never closed >5.00") was *"true at its vintage and overtaken one print later."* **That is wrong: the premise was already false when written.** 9/16's 5.01 was published before 9/21.
- The VX-BRK-020 fire itself is unaffected, and the first red-rung close is **9/16**, not 9/18.
- Corrected in STATUS; no score change.
