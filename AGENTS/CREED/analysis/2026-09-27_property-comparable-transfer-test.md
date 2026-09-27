# Do the loss comparables transfer? — property-evidence challenge to the CRE→bank loss bridge (FLG · EGBN · OZK) and Nano Banc

**Written:** 2026-09-27 (Sun), CREED, on PROME task (Will 17:24 ET; plan `PROME/plans/2026-09-27_cre-to-bank-loss-transmission-PLAN.md`, `e614dee5e`).
**Under test:** `AGENTS/REGINALD/reports/2026-09-26_CRE_top3_loss_bridge.md` (`b93e3ac58`) + its machinery `AGENTS/REGINALD/scripts/cre_loss_bridge.py` (pools/rates/anchors read at source), and the Nano Banc loss scenario in `AGENTS/CREED/analysis/2026-09-27_nano-banc-collateral-read.md` §2.
**Method:** reuse only. Built from my 9/26 vulnerability map + property test, REGINALD's dossiers, the specialist desks, and today's corrections. **No new pulls.** The one path fix: PROME's `scripts/cre_loss_bridge.py` is shorthand for `AGENTS/REGINALD/scripts/…`; it exists and is committed.
**Scope:** for every comparison the bridge and Nano scenario use, I grade whether it **transfers** to the target portfolio across six dimensions — **property type · market · loan vintage · appraisal date · seniority/lien · performing vs defaulted** — and name the pools where **no defensible comparable exists.** This grades evidence. It re-ranks nothing, moves no CREED letter/band/score, and is not a trade view (TERRY owns that).

---

## §0. The answer first

1. **The bridge's *arithmetic* is sound; its *anchors* mostly aren't market comparables.** Of the ~35 stressed pools across the three banks, only a handful carry a comparable that transfers on all six dimensions. Most rates are either **the pool's own LTV/coverage** (property-specific, valid *in kind* but with no clearing-price magnitude behind them) or **explicit ASSUMPTIONS with no anchor at all.** REGINALD labels these honestly; the reader must not read the labelled-assumption pools as evidenced.
2. **The single structural gap: there is essentially no bank-held-loan clearing price on the entire board.** Every realized comp CREED holds is **CMBS** (Trepp liquidations) or a **one-off property sale**. Not one is a bank small-balance CRE **loan pool.** So every bank pool's *magnitude* rests on the bank's own appraisals/exits or on a transferred CMBS/office sale of imperfect fit. This is exactly why the Nano FDIC disposition (§ below) is worth registering — it would be the first of its kind.
3. **The best-transferring comps are OZK's own same-bank same-type exits** (Seattle office at 58% of appraisal; the Concord lab appraisal −32%). They are the right kind of evidence and they cut *against* OZK's OREO marks — but each is **n=1**, on an **appraisal** basis, and matched appraisal dates/characteristics decide asset by asset.
4. **The worst-transferring comps have already been removed or corrected** (FLG's office-sale −61/−72% transferred onto an accruing non-office pool — removed; EGBN's 39.6% office-era haircut on an MF book — replaced with 13.3%). Today's corrections finish that clean-up and **reverse one of my own 9/26 findings** (see "What today's corrections change").
5. **Nano is *consistent with, not confirming*, the 2026 severity distribution.** No comp matches its property type or its lien position; four named liens are **second liens**, where a sale price measures the lien, not the building.

---

## §A. OBSERVED — what the comparables actually are (cited, dated, with tier)

These are the real transactions/marks the scenarios lean on. Everything here is a fact on file; the *transfer* judgment is in §B.

| # | Comparable | Value | Basis | Property type | Market | Perf/def | Tier |
|---|---|---:|---|---|---|---|---|
| C1 | **BCB Bancorp problem-loan sale** (8-K 9/25, acc 0001193125-26-402710) | $43.3M pre-tax loss on $205.3M face; **≤79% of face** a ceiling, true price undisclosed | vs carrying / face | 88% CRE/MF; rent-reg share **undisclosed** | **NJ/NY** | problem/defaulted | PRIMARY (8-K) |
| C2 | **ARI ~$9B book → Athene** | cleared **99.7% of commitments** (0.3% loss) | commitments | national CRE **lending** book | national | **performing** | PRIMARY (`VX-5.02`) |
| C3 | **OZK own Seattle office exit** | **58% of appraisal** | appraisal | office | **Seattle** | foreclosed sale | OZK desk (issuer) |
| C4 | **OZK Boston office / Chicago land exits** | 80% of appraisal / −34% vs loan | appraisal / loan | office / land | Boston / Chicago | foreclosed sale | OZK desk |
| C5 | **Concord (MA) lab analog appraisal** | **−32% in 13 months** | appraisal move (not a sale) | **life-science lab** | Concord MA (≈Boston) | mark | REGINALD dossier |
| C6 | **EGBN own H1-26 non-office exit haircut** | **13.3%** (transfer basis) | loan cost | **non-office, type not shown** | DC metro | HFS/sale | REGINALD pack `q2_EGBN.md` |
| C7 | **EGBN own re-appraisals** | **−14% to −29%** | appraisal | office | DC metro | mark | REGINALD dossier |
| C8 | **CMBS liquidation severity, Jul / Aug 2026** | **48.8% / 72.6%** | balance before disposition | 93% / 47% office | national | defaulted | PRIMARY-READ (CREFC/Trepp, `KB-041`) |
| C9 | **CMBS dispositions YTD: all / office** | **35.2% / 49.3%** | severity | all / office | national | defaulted | SECONDARY (JPM via CREFC) |
| C10 | **SoCal CMBS office: BofA Plaza / 315 S Beverly / La Terraza** | 44% / 100% / 31% | balance before disposition | **all office** | LA / Beverly Hills / Escondido | defaulted | PRIMARY-READ (CREFC/Trepp) |
| C11 | **205 W Randolph / Glendale Plaza / Aon** | −72% / −61% / −58% | **sale vs 2017 purchase** / mark | office | Chicago / LA | sale / mark | SECONDARY — **wrong-basis, do not use as a loss rate** |

**Vintage note (applies throughout):** appraisal dates are the quiet hazard. **~70% of FLG's LTV appraisals predate 1/1/24; ~89% of EGBN's office LTVs predate 6/30/25.** Both are mostly *before* the June-2026 NYC rent freeze and the Sept-2026 rate move (10y 4.38→5.18%). Deutsche Bank's read (secondary, via CREFC Jul) is that 2026 distressed office sales clear **~20% below the latest appraisal** — so even a *fresh* appraisal lags an executable price, and a stale one lags it further. This biases every appraisal-anchored mark **high.**

---

## §B. SCENARIO ASSUMPTIONS — does each anchor transfer? (six-dimension grade)

Legend: **✓** match · **~** partial · **✗** no match · **n/a** not applicable (e.g. an assumption with no comp).

### B1. FLG — 10-Q basis, 6/30/26

| Pool (rate base/stress) | Anchor used | type | mkt | vint | appr | lien | perf/def | Verdict |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|---|
| MF NA, NYC ≥50% RR (8/20) | **~20.45% already recognised** (own) + **C1 BCB ≤79%** | ~ | ~ | ✗ | n/a | ✓ | **PARTIAL.** Own-recognition figure transfers (it's FLG's own book). BCB is a **classified-book cross-check, not evidence of the rent-regulation mechanism**: rent-reg share undisclosed, self-selected pool, ≤79% is a ceiling not a price. Implied cumulative severity on original **≈24–34%** at base/stress (charge-offs + rate×book, one basis; **20.45%** already recognised) runs at/above BCB's realized ~21% — so the base is *not contradicted* (if anything conservative vs the one comp). |
| MF NA, other (8/20) | same | ~ | ~ | ✗ | n/a | ✓ | Rides B1's anchor; "other" MF type/geography undisclosed. Assumption-grade. |
| CRE NA (10/25) | **"ASSUMPTION ONLY — no market anchor"** | n/a | n/a | n/a | n/a | n/a | **NO COMPARABLE.** Parent CRE is 40% industrial / 22% office; this pool's own mix is undisclosed. Named as a pool with no defensible comp. |
| MF SM+SS accruing, NYC RR (5/15) | pool's own **78% LTV / 1.01× / reset** | ✓ | ✓ | ✗ | ✗ | ✓ (accruing) | **In-kind valid, magnitude unsupported.** It's the pool's own LTV/coverage, not a transferred sale. No NYC rent-stabilized clearing price exists on any fleet surface. Par payoffs argue the base isn't too low; the 2027 reset argues the stress isn't too high. |
| MF SM+SS accruing, other (3/10) | **"ASSUMPTION"** | n/a | | | | | **NO COMPARABLE.** |
| CRE SM+SS accruing (3/10) | **"ASSUMPTION ONLY"** | n/a | | | | | **NO COMPARABLE — and this is where the invalid office-sale transfer (C11) used to live.** Removed (Fix 2 accepted). ✅ |
| MF pass NYC RR (0/1); MF pass other (0/.5); CRE pass (0/0) | **C2 ARI 99.7%** as a *cap* | ~ | ✗ | ~ | n/a | ✓ | **Directionally valid as a ceiling** — a large performing book cleared at par, so pass-book stress is held near zero. But ARI is a *national, mixed* lending book, not NYC rent-regulated MF; it vouches for "performing books can clear at par," not for these specific loans. |

### B2. EGBN — holding-company basis, 6/30/26

| Pool (base/stress) | Anchor | type | mkt | vint | appr | lien | perf/def | Verdict |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|---|
| Office pass (2/8) | **C7 EGBN own re-appraisals −14/−29%** + stale-appraisal argument | ✓ | ✓ | ✓ | ✗(stale is the point) | ✓ | **Transfers as an appraisal signal, not a sale.** ~89% of LTVs pre-6/30/25; the stress is a re-appraisal-vintage argument, which is the right argument. Loss sits in the high-LTV tail (Fairfax 96%, a $60M Montgomery loan at 80%), not the 61%-LTV average. |
| Office SM/SS/NA | named loans (Fairfax 96% LTV matures 9/25; DC loan at ~40% LTV) | ✓ | ✓ | ~ | ~ | ✓ | Property-specific; reasonable in kind. |
| **MF SS accruing (13.3/30)** | **C6 EGBN own non-office haircut 13.3%** (base); **−35% on 84–88% LTV** (stress) | **~** | ✓ | ~ | ~ | ✓ (accruing) | **Right bank, property type still not established as MF.** 13.3% is EGBN's own *non-office* H1-26 exit — better than the withdrawn 39.6%, but not shown to be *multifamily*. Stress 30% ≈ −35% value on the high-LTV tail (PG County apt DSCR 0.63; DC apt DSCR 0.15) — defensible **on the tail**, not on the 58%-avg-LTV book. Split by type/LTV before applying. |
| MF pass/SM/NA | pool's own DSCR 0.67–0.89; 3.5% implied cap rate | ✓ | ✓ | ✗ | ✗ | ✓/✗ | In-kind; appraisals imply a 3.5% cap rate (rich), which the stale-appraisal argument says is too low a loss. |
| Other IPCRE — hotel $373M (0/1) | **hotel 30% 2026 maturity share** (MBA, secondary) | ✓ | — | n/a | n/a | n/a | **A refinancing-schedule anchor, not a loss comp.** Says hotels *mature* heavily, not what they *lose.* 1% pass stress is a placeholder. |
| Owner-occ CRE criticized (8/20); Other IPCRE SM (3/10); Construction criticized (8/25) | **"ASSUMPTION"** | n/a | | | | | **NO COMPARABLE.** |

### B3. OZK — Bank OZK basis, 6/30/26

| Pool (base/stress) | Anchor | type | mkt | vint | appr | lien | perf/def | Verdict |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|---|
| **Boston 10 Prospect (30/50)** | **C5 Concord lab appraisal −32%/13m**; counter: $330M pending sale | ✓ | ~ | ~ | ✗(mark) | ✓ | **Best-matched OZK anchor by TYPE (lab) and near-market.** But it's an *appraisal* move, not a sale, and the **$330M pending sale (vs ~$186M implied appraisal) doesn't reconcile**, so it counts as neither support nor loss. This one loan swings the case; the 91% LTV rests on a Nov-25 appraisal. |
| **The Jack, Seattle office (5/40)** | **C3 OZK own Seattle exit 58% of appraisal** | ✓ | ✓ | ~ | ✓(same basis) | ✓ | **The strongest transfer in the whole file** — same bank, same type, same market, same (appraisal) basis. Caveat: **n=1**; and it's a *different* Seattle asset, so matched appraisal date/characteristics still decide. |
| **OREO office — Seattle/Santa Monica/Atlanta (15.2/40.2)** | **C3+C4** own exits 58–80% vs carried 89–100% | ✓ | ~ | ~ | ✓ | foreclosed | **Right kind of comp, applied across three assets from one/two sales.** Atlanta carries a *fresh* Jun-26 appraisal; Santa Monica's is ~11 months old — so the 58% Seattle print does **not** transfer uniformly. Asset-by-asset appraisal dates decide. |
| OREO life-sci (5/27.5); OREO LA land (0/30) | "near conversion value" / "LOI at/above carrying" | ~ | ~ | | | | Soft anchors; assumption-grade. LA land: LOI, 3 years in OREO, one failed buyer. |
| Other nonaccrual (10/25); Tahoe SS (10/25) | **"ASSUMPTION"** (composition not disclosed) | n/a | | | | | **NO COMPARABLE.** |
| Special mention (3/12) | pool's own — condo at 105.6% LTV | ✓ | ~ | | ~ | ✓(accruing) | In-kind; the named condo is already underwater on its appraisal. |
| **RaDD life-science pass (0/65)** | **OZK desk severity 65–70%** — collateral condition (≈3.3% leased; interest from reserves; IQHQ deed-in-lieu analog) | ✓ | ~ | ~ | n/a | ✓ | **The one case a distressed severity on a PASS-rated loan transfers** — justified by *collateral condition* (empty building), not a borrowed sale haircut. It's an internal desk model, not a market print. Moves the OZK stress by ~$250M — more than every other OZK pool combined. |

### B4. Nano Banc retained pool (my own §2 scenario, re-tested)

| Comp leaned on | type | mkt | vint | appr | lien | perf/def | Verdict |
|---|:--:|:--:|:--:|:--:|:--:|:--:|---|
| **C8/C9 CMBS severity 35–73%** | ✗ | ~ | ✗ | n/a | ✗ | ✓ | **No type match** (CMBS is office-heavy; Nano is neighbourhood retail / medical office / small MF) and **no lien match** (CMBS = first-mortgage trust; 4 named Nano liens are **seconds**). Consistent-with, not confirming. |
| **C10 SoCal CMBS office (31–100%)** | ✗ | ✓ | ✗ | n/a | ✗ | ✓ | **Location matches, type doesn't.** All three are office; none is retail/medical/small-MF. Range 31→100% shows *location is not the variable.* |
| **C2 ARI 0.3%** | ✗ | ✗ | | | ✓ | ✗ | Opposite pool (performing national) — a lower bound only. |

**Nano: no comparable matches property type or lien position.** The retained pool is INFERRED to be mostly the non-performing book; a mark up to the **≤~56% ceiling** (REGINALD, 9/22 base) sits inside the 2026 range but is unallocable and n=1 from a **fraud-origin** bank. **Second-lien prices are excluded from any property-value read.**

### B5. Pools where NO defensible comparable exists (named, as the contract asks)

- **FLG CRE nonaccrual** ($471M, 10/25%) — assumption only; parent mix industrial/office, pool mix undisclosed.
- **FLG MF SM+SS accruing "other"** ($4,274M, 3/10%) — assumption.
- **FLG CRE SM+SS accruing** ($1,367M, 3/10%) — assumption (invalid office comp already removed).
- **EGBN owner-occupied CRE criticized** ($64.6M), **Other IPCRE SM** ($92.1M), **Construction criticized** ($62.0M) — assumption.
- **OZK "Other nonaccrual"** ($48.5M) and **Tahoe SS** ($29.4M) — assumption, composition undisclosed.
- **OZK OREO life-sci / LA land** — soft/LOI anchors only.
- **The Nano retained pool as a whole** — no comp of matching type + lien.

These are not errors — REGINALD flags each as an assumption. The finding is that **the dollar weight in "no-comp" pools is not trivial** (FLG's three alone carry ~$6.1B of balance at 3–25% stress), so the bridge's *stress* total is more assumption-driven than its *base*.

---

## §C. UNKNOWNS — what is missing, and why it can't be closed from the desk

1. **No NYC rent-stabilized clearing price after June 2026 exists on any fleet surface.** The obvious historical comp — the FDIC's 2023 Signature Bank rent-regulated loan-portfolio sale — is **not in any fleet record** and would need a primary pull. Until one exists, FLG's NYC RR magnitude sits between "par payoffs are happening" and "78% LTV on pre-freeze appraisals," and only a clearing price decides.
2. **No EGBN multifamily-specific exit haircut.** Every haircut on file is portfolio-wide (and probably not MF). The 13.3% base and 30% stress are borrowed from a non-office mixed book.
3. **No DC-area multifamily *market* data** (rents, supply, collections, sales) anywhere in the fleet — HOMER has no metro layer. The "DC-area MF" framing rests entirely on EGBN's own 34-loan book.
4. **The Boston 10 Prospect $330M sale cannot be reconciled** with the ~$186M implied appraisal; it is neither counted as support nor as loss.
5. **RaDD's real collateral position** (any signed material lease at Campus at Horton; new sponsor equity vs more time) is undisclosed — owed on the OZK desk since late July.
6. **Nano retained-pool composition and lien positions** are undisclosed until the FDIC P&A agreement posts (~10/05–10/09); the DIF cost is an estimate, not a sale, and is unallocable between purchased and retained assets.
7. **Appraisal-date coverage** — I can state the *share* of stale appraisals (FLG ~70%, EGBN ~89%) but not a per-loan revaluation; the Deutsche Bank "−20% vs latest appraisal" is secondary.

---

## The next observation that would change the conclusion — named, dated, with direction

| Bank | Next observation | When | If it prints… → direction |
|---|---|---|---|
| **FLG** | (a) The **$133M charge-off-gap split** at Q3; (b) any **NYC rent-stabilized loan sale post-June-2026** | Q3 10-Q ~late Oct; ad hoc | Discounted "par payoffs" or a below-par NYC RR sale → **raises FLG loss, weakens the par-payoff defence.** Payoffs confirmed at par → **base holds, stress caps lower.** |
| **EGBN** | Whether the **4 criticized MF loans ($155.8M, Aug–Dec maturities, DSCR 0.15–0.89)** pay off, extend, or go HFS — and at what haircut; plus **reserve by collateral type** *(4/$155.8M is the MF-specific set per REGINALD D5, re-verified at deck 8-K acc …-000088; the wider "$249M/7 loans" is all-types DSCR<1, incl. 2 storage + Fairfax office)* | **Q3 10-Q ~early Nov** | HFS at a deep haircut → **validates the 30% MF stress, raises loss.** Payoff/extension → **base holds; the borrowed 13.3% overstates.** *Their resolution IS the first EGBN multifamily comparable.* |
| **OZK** | (a) **10 Prospect $330M sale closes or fails**; (b) any **Q3 OREO office sale price vs carrying**; (c) **RaDD leasing/recap** report-back | Q3 call mid/late Oct | Sale closes → **removes the single biggest loss (~$85–169M).** Sale fails / OREO clears <80% → **validates the 40% office & 50% lab stress.** RaDD material lease + new equity → **base**; no lease → **65% stress holds** (±~$250M swing). |
| **Nano** | **P&A agreement** (composition); **9/29 Plaza Continental hearing** (one lien retained vs sold); the **FDIC pool sale** (first bank-held SoCal CRE clearing price) | ~10/05–10/09; **Tue 9/29 1:30pm**; +3–9 mo (DOCKET **L515**) | A **performing** pool clearing <70% UPB → T-06 candidate. An **NPL** pool below 70% → expected, not a signal. **Record by lien position** — second-lien prices never read as property marks. |

**The highest-value single observation across all four:** EGBN's Q3 10-Q, because it would convert the fleet's *only* missing evidence class — a **bank multifamily exit haircut** — from a borrowed number into a measured one, and EGBN's reserve coverage swings 2.0×→0.67× entirely on that haircut.

---

## What today's corrections change (since my 9/26 property test)

1. **`5d71521b8` / `b93e3ac58` — FLG "20.45% recognised" stands; the "17.5%" was the double-count.** ⚠️ **This REVERSES my own 9/26 cross-cutting finding #4**, which called 20.5% the post-charge-off basis and ~17.5% the "original" basis with "direction holds, level shifts." That was **wrong**: $2,088M *is* the pre-charge-off/original balance (2,088 − 351 charged off = 1,737 current), so (351 + 76)/2,088 = **20.45% is already the original basis**; the 17.5% erroneously re-added the $351M charge-offs into the denominator. **My 9/26 finding #4 is superseded — recognition on the resolved NYC RR book is ~20.45%, not ~17.5%, and there is no level shift to make.**
2. **`8f7152096` / `60a155175` — FLG "loss-at-exit" withdrawn as the leading reading of the $133M gap** (the gap runs 11%–350% of payoffs across FY23–Q2-26, 3.5× in FY23; it does not scale with payoff volume). **Effect on my 9/26 conclusion #2** ("the best price evidence points *against* large losses — FLG par payoffs"): the par-payoff evidence is **modestly weakened, not refuted** — some "par payoffs" may carry an undisclosed discount, but FLG's own counter-point (gap doesn't move with payoff volume) argues against a *pure* exit-discount reading. So par payoffs remain FLG's best contrary evidence, held with less certainty.
3. **The invalid transfers I flagged on 9/26 are now removed at source:** the office −61/−72% comp (C11) no longer anchors FLG's accruing CRE (labelled ASSUMPTION ONLY), and EGBN's 39.6% office-era haircut is replaced by the 13.3% non-office figure. **My 9/26 corrections were adopted; the "office-driven" direction I gave for EGBN's FY-25 haircut was itself wrong** (office ≤41% of transfer value; no office loan to HFS after 9/30/25) — the fix stands for the narrower reason that the haircut came from a *different book mix*, not a *different property type shown to be office*.

**What does NOT change:** the ranking (FLG, EGBN, OZK); the no-solvency-breach reading at FLG/EGBN; OZK's RaDD as the swing; the Q3 prints as the test. **No CREED band, score, trigger or prediction moves from anything here.**

---

## Sources
- Bridge + machinery: `AGENTS/REGINALD/reports/2026-09-26_CRE_top3_loss_bridge.md` (`b93e3ac58`); `AGENTS/REGINALD/scripts/cre_loss_bridge.py` (pools/rates/anchors read at source 2026-09-27).
- CREED prior: `research/2026-09-26_CRE_VULNERABILITY_MAP.md`; `research/2026-09-26_REGINALD_TOP3_PROPERTY_TEST.md`; `analysis/2026-09-27_nano-banc-collateral-read.md` (§2 comps, `KB-041`).
- Corrections: FLG `8f7152096`, REGINALD→CREED `5d71521b8` / `b93e3ac58`, FLG→REGINALD `60a155175`.
- Comps at primary: CREFC monthlies (Trepp data) Jul/Aug 2026 (`KB-CREED-041`); ARI/Athene (`VX-CREED-5.02`); BCB 8-K acc 0001193125-26-402710.
- Appraisal-lag: Deutsche Bank Research 8/10/26 via CREFC July (SECONDARY).
