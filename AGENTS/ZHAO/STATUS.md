# ZHAO STATUS

**Updated:** 2026-08-21 ~13:10 ET (three-part session: June TIC pulled + graded · **ZHA-15 graded RESOLVED NO** · **Korea falsification tripwire graded FIRED**. Two of the three falsify or stand down parts of ZHAO's own thesis.)
**Overall Status:** 🟠 ELEVATED — **the $650B line broke, and the Belgium proxy that was supposed to interpret it does not work.** June TIC: **China $633.4B, −$25.9B MoM, the lowest reading in the 78-month series** and the first breach of the <$650B line after two near-misses held (Mar $653.3B, Apr $651.1B) and May rebounded. **It is genuine selling, not valuation** — reported net sales **−$21.96B, of which LT/coupon −$15.77B**, the first month this cycle China sold *duration* in size. **ZHA-04 FIRED (TRUE at 42%).** Trailing-12m China net sales are **−$122.3B**, ~3x the figure this thread has been quoting. Against that: **Belgium hit an all-time series high ($482.5B) on +$17.56B of buying**, which under my own written methodology would read as ~80% custody relabeling — **so I tested the rule instead of applying it, and it failed**: rho(China, Belgium net sales) = **+0.05 over n=41 months**, ~zero on every window, Belgium buying in only **56%** of China-selling months. June's mirror pattern is chance. **ZHA-03 RESOLVED NO** (window expired $17.5B short). Korea **bought** +$2.70B, first net-buying month in five — supports ZHA-12. Wider: foreign **official sold $45.4B while non-official bought $23.2B**. Convergence Matrix **~28/60** (+2: vector 1 re-armed 4→5, vector 3 cut 3→2 on the falsified proxy).

---

## 📌 AUG 21 — **JUNE TIC: the threshold broke, and the interpretation instrument broke with it**

**Source:** Treasury TIC Table 5 + Table 3, direct ZHAO pull, retrieved 2026-08-21 (curl w/ UA header — `ticdata.treasury.gov` 403s bare; recipe from HANS 7/16). ⚠️ The *release date* (~8/18 on the standard calendar) is **PUBLIC-AND-UNFETCHED** — the press release was not retrieved; the data files are the primary and carry a complete `2026-06` column. KB-ZHAO-119..124.

### 1. 🔴 China broke $650B — and the composition is what matters

| | May | June | Δ |
|---|---|---|---|
| Holdings | $659.3B | **$633.4B** | **−$25.9B** |
| Total net sales (reported flow) | +$5.95B | **−$21.96B** | swing −$27.9B |
| — LT / coupon | −$0.13B (flat) | **−$15.77B** | **duration sold** |
| — ST / bills | +$6.08B | −$6.19B | |
| LT valuation | +$1.71B | −$5.47B | |

**~85% of the level drop is transacted, ~15% price.** May's rebound was bills with coupon flat; **June is the first month this cycle China sold duration in size.** $633.4B is the **series low, rank 1 of 78 months** (2020-01 on). The −$21.96B sale is the **4th most-negative of 41 months** with flow data — large, **not unprecedented** (Mar-26 −$34.5B was bigger).

> **ZHA-04 RESOLVED YES / FIRED at 42% confidence**, in-window (Q2-Q3 2026). I had cut this twice, 65%→30%→42%, because Mar and Apr stalled $1-3B above the line and May reversed. The cuts were reasonable and the hit was not lucky — the breach came with a composition change the prior near-misses lacked.
>
> ⚠️ **The "18-year low" framing carried in prior STATUS text is INHERITED and NOT re-verified** — this pull spans 2020-01 only. Certify **"lowest since at least Jan 2020"** until sourced further back.

### 2. 🔴 The trailing-12-month number is ~3x what this thread has been quoting — and levels *understate* it

China TTM net sales **Jul-2025 → Jun-2026 = −$122.3B**, against a level change of only **−$98.0B** ($731.4B → $633.4B). **Valuation added ~$24.3B back over the year, so reading levels understates China's annual selling by ~25%.**

> ⚠️ **The direction of the level-vs-flow bias INVERTS with horizon** — on June alone valuation *flattered* the decline (−$25.9B level vs −$21.96B sold); over the TTM it *masked* it. One month and one year point opposite ways, which is exactly how a level-only reader gets confidently wrong.
>
> ⚠️ **This corrects a figure embedded in the Will-approved KB-ZHAO-102 reframe**, which contrasts China's ~$300B Agency holdings against *"the ~$40B Treasury decline this thread has tracked."* That $40B was the **Feb-Apr window**, not the annual run-rate. **The reframe's logic survives intact** — Agency rotation and off-SAFE state channels are still untested, so this remains a *SAFE-reported Treasury-line reduction*, not demonstrated de-dollarization. But the magnitude it contrasts against was understated ~3x, which means the Agency-rotation explanation has to carry **more** weight to stay sufficient, not less. ✅ **WILL-RULED 8/21 in-session (*"Do the reframe fix"*) — executed. See §3b: the datum is out of canon and the rotation mechanism is struck.**
>
> ⚠️ **Self-correction on the record:** I first wrote −$46.4B into VX-ZHAO-1.03 as an asserted figure without running the sum, then computed it. Wrong for one edit cycle, corrected in KB-ZHAO-124.

### 3. 🔴 **I tested my own Belgium-proxy rule against the data and it failed**

Belgium printed **$482.5B — an all-time high of the 78-month series** (rank 78/78), on **+$17.56B of genuine net buying** (4th largest of 41 months), with valuation working *against* it (−$5.87B LT). Three straight monthly rises: 454.0 → 459.9 → 472.0 → 482.5.

My `CLAUDE.md` §BELGIUM PROXY METHODOLOGY says, as a flat rule: *"Belgium rising while China TIC falls = custody migration to offshore, NOT a reduction. Net neutral."* **June is exactly that pattern** (China −$21.96B, Belgium +$17.56B, net −$4.4B) and the rule would have me report ~80% of China's sale as relabeling.

**Tested instead of applied:**

| Window | rho(China net sales, Belgium net sales) | LT-only |
|---|---|---|
| Full, n=41 (2023-02→2026-06) | **+0.050** | +0.055 |
| Last 12m | −0.040 | −0.102 |
| Last 24m | +0.023 | −0.023 |
| Last 36m | +0.005 | +0.004 |

**Every window is indistinguishable from zero. None is materially negative — which is what a custody mirror requires.** Base rate: of the **27 months China was a net seller, Belgium was a net buyer in 15 (56%)** — a coin flip. June's pattern is further explained by both legs simply being large this month: China's sale ranks 4th most-negative of 41, Belgium's buy 4th largest of 41. Two big independent moves in opposite directions look like a mirror and aren't one.

> **This is the mirror-image of the Will-approved 7/16 reframe, and completes it.** 7/16 established that *"Belgium flat while China falls"* does not prove genuine exit. This establishes that **"Belgium up while China falls" does not prove custody migration.** Both arms of the rule were over-claiming.
>
> ⚠️ **Honest limit:** this refutes *systematic monthly mirroring*, **not** the existence of an episodic migration channel — lumpy real events would be diluted by a full-sample correlation. The operational claim is the narrow one: **a single month's China-down/Belgium-up cannot be read as migration, because that pattern occurs at chance frequency.**
>
> ⚠️ The rule has been applied as if deterministic for ~5 months and **was never base-rated.** New instrument registered: **VX-ZHAO-1.09** (rho, with bands for when the proxy would become usable again: rho < −0.5 ORANGE, < −0.7 RED). **ZHAO owns `CLAUDE.md` and will rewrite §BELGIUM PROXY METHODOLOGY from identities to probabilistic language.** Flagged to PROME because **HANS and LIQUID both consume this proxy.**

### 3b. 🔴 **I tested the reframe's own mechanism too — Treasury→Agency rotation is REFUTED**

Will asked how to fix the ~$40B magnitude error inside the Will-approved KB-ZHAO-102 reframe. Chasing the number surfaced something larger: **the reframe's primary MECHANISM can be tested directly, and it fails.**

The reframe explains the falling SAFE Treasury line as *"more likely Treasury→Agency rotation or entity-shifting."* **Rotation predicts Agency holdings RISE as Treasuries fall.** TIC Table 1 carries Agency flows by country, so this is measurable:

| China, TTM Jul-25 → Jun-26 | Net sales ($M) |
|---|---|
| Treasuries (LT) | **−91,269** |
| **Agency bonds** | **−40,305 — SOLD, not bought** |
| Corp. bonds | +398 |
| Equities | +12,242 |
| **All LT US securities** | **−118,934** |

Agency **holdings** went $179.9B (Jul-25) → **$142.0B** (Jun-26) = **−$37.9B over 12 months.** rho(Treasury net sales, Agency net sales) = **−0.025 over n=41** — indistinguishable from zero, where rotation needs a materially negative number. June itself: Treasuries −$15.8B **and** Agency −$1.1B, same month. **China sold both.**

> **The reframe's CONCLUSION survives — but on valuation, not on either mechanism it named.** Total LT US-securities holdings moved only **$1,173.2B → $1,161.6B = −$11.6B (−1.0%)** against **−$118.9B sold**: markets added back **~$107.3B**. So *"China's aggregate USD exposure is not meaningfully reduced"* is **true on the stock** — because prices rose, not because China rotated.
>
> ⚠️ **Mechanism (a) rotation: REFUTED. Mechanism (b) off-SAFE entity-shifting: NOT TESTABLE from TIC** — TIC attributes by custodian/country, not by Chinese owning entity, so intra-China entity shifts don't move this line at all. And the one re-routing channel that *would* be detectable — Belgium custody — was falsified as an instrument in §3 above, the same session.
>
> ⚠️ **PERIMETER — two correct TTM figures are now in ZHAO's record:** **−$122.3B** = all Treasuries incl. bills (Table 3) · **−$91.3B** = coupons only (Table 1 is a long-term table). They reconcile to the dollar (−91,269 + −31,017 = −122,286). **Cite the perimeter with the number.**
>
> ⚠️ The reframe's **~$300B Agency figure (CFR/Setser 5/2026) is ~2x the raw TIC Agency line ($142.0B)** — a custodial-adjusted estimate being contrasted against a raw TIC Treasury line, i.e. a perimeter mismatch inside the reframe itself. **The refutation does not depend on that dispute: the DIRECTION of the raw series is wrong for rotation at any level.**
>
> 🔴 **DOWNSTREAM — LIQUID banked this as one of four independent demand-hole refutations** (`AGENTS/LIQUID/CALENDAR.md`, Jul-16 row: *"demand-hole now refuted 4 ways — auctions · Japan MOF · Korea · China rotation"*). **The China-rotation leg must be withdrawn; the other three are untouched.** Packet owed.
>
> **ZHAO is NOT editing the Will-approved reframe text.** Recommendation routed to Will — see NEXT ACTIONS. (VX-ZHAO-1.10, KB-ZHAO-127.)

### 4. 🟠 Official sold, private bought — and the aggregate decline is mostly valuation

| Cut | June net sales |
|---|---|
| **Foreign Official** | **−$45.40B** |
| **Foreign Non-Official** | **+$23.15B** |
| Grand Total | −$22.25B |
| **Total Asia** | **−$47.19B** (≈ all Japan −$26.86B + China −$21.96B) |
| Other large sells | France −$20.92B · Hong Kong −$9.33B · Israel −$6.24B |
| Large buys | Canada +$21.26B · **Belgium +$17.56B** · Caribbean +$9.87B · Thailand +$7.41B |

Official **holdings** fell $3,848.0B → $3,778.1B (−$69.9B) against −$45.4B sold — **~35% of the official decline was price.** For the Grand Total the gap is far wider ($9,371.1B → $9,299.0B = −$72.1B level vs −$22.3B sold): **the aggregate June decline is majority valuation.**

> ⚠️ **Anyone quoting "foreign holdings fell $72B in June" as selling overstates it ~3x.** China is the exception — its drop is ~85% transacted. A level-only read of this release lands badly wrong on the aggregate and roughly right on China, by luck.
>
> **Not mine, routed:** **Japan's −$26.86B is almost entirely BILLS** (ST −$23.11B, LT only −$3.75B) — a roll-off, not duration selling, and the second such month (May ST −$59.79B) → **SAM**. **France −$20.92B** → **HANS**. The **official/non-official divergence** is the demand-hole-relevant cut → **LIQUID**: the private bid is absorbing official supply, a different market structure from "nobody is buying."

### 5. 🟡 Korea bought — first net-buying month in five

Korea **+$2.70B** (LT +$0.39B flat, ST/bills +$2.31B), $132.3B → $134.7B. Breaks a Feb-May seller streak (−$1.4/−$1.9/−$1.2/−$2.3B). Grades **NEUTRAL on the buying side** of ZHA-13's ±$5B band. **This is the post-hike test ZHA-13's own note called for** and it **supports ZHA-12 (80%)**: Korea stopped selling in the same month the won strengthened — the rate lever is doing the defense work, not reserve liquidation. USD/KRW live **1,385.70**. ⚠️ Scope caveat unchanged (VX-ZHAO-2.07): Table 3 is all-residents, no official/private split. **ZHA-13 stays RESOLVED on the May print — this is context, not a re-grade.**

### 6. ⚠️ ZHA-11's registered arbiter was the wrong dataset

STATUS's CALENDAR and NEXT ACTIONS both named **June TIC** as a ZHA-11 arbiter. **It cannot be.** ZHA-11 is about participation in the **9 July 2026** 30Y auction; June TIC covers flows **through 30 June** and predates the event entirely. **Correct arbiter: the July TIC print, ~16 September 2026.** ZHA-11 was already graded SURVIVES on 7/16 within its registered "pre-TIC 7/16" window; June changes nothing. Recorded because a resolver was pointed at a dataset that structurally cannot answer it.

---

## 📌 AUG 3 — P3 SOLO LEAD (verdict live, detail archived 8/21)

**VERDICT (unchanged): the direction flip is SUPPORTED. The USSR analogy is NOT.** Surviving claim: *China is the more exhausted of the two, on a slow fuse with no cliff — and its external invulnerability is administratively maintained rather than structurally given.* China carries ~2.5 of 3 P0 kill-mechanism axes (structural stagnation ✓, revenue shock ✓ land revenue −31.5% H1'26, external dependence ✗) vs US ~0. **Not tradeable like a collapse thesis** — every cliff-producing falsifier is un-triggered; **the absence of a forcing function is itself the finding.**

**Live tripwires:** ⚠️ **B1 capital-control integrity** (VX-ZHAO-1.08) · ⚠️ **B4 partial** — debt-swap quota **94% consumed, the 6% headroom is the number to watch.** **A2 strongly rejected.**

> ⚠️ **8/21 amendment to finding 1:** the P3 memo quotes China's Treasury decline at the Feb-Apr scale. **The TTM figure is −$122.3B** (KB-ZHAO-124). Does not change the verdict — the debt stock/flow argument is independent — but any restatement of the memo's external leg should use the corrected magnitude.

**Full detail** → `archive/STATUS_section_aug03_P3_archived_20260821.md` · **Memo** → `outbox/2026-08-03_to-PROME_P3-direction-flip-adjudication.md` · **Pre-registration** → `reports/2026-08-03_P3_PREREGISTRATION.md` · KB-ZHAO-111..118.

---

## 📌 ARCHIVED SESSION NARRATIVES

**JUL 4 / JUL 9 / JUL 16** → `archive/STATUS_sections_jul04-jul09_archived_20260803.md`, `archive/STATUS_section_jul16_tic_pregrade_archived_20260803.md` · **AUG 3 catch-up + P3 detail + Q2 GDP + May-TIC recap** → four `archive/*_20260821.md` files. Permanent record is `workbook/KB.tsv` throughout.

---

## SIGNAL DASHBOARD

### Capital Flows
| Metric | Value | Threshold | Status | Source |
|--------|-------|-----------|--------|--------|
| China Official UST | **$633.4B** (Jun, **−$25.9B MoM**) | <$650B = RED | 🔴 **BREACHED** | [CONF] TIC Jun 2026, ZHAO direct pull 8/21 — **series low, rank 1 of 78 months**. Net sales −$21.96B (LT −$15.77B): genuine selling, ~85% transacted. ZHA-04 FIRED (KB-ZHAO-119) |
| China UST — trailing 12m | **−$122.3B net sold** (Jul-25→Jun-26) | — | 🔴 | [CONF] ZHAO computation over TIC Table 3, 8/21 — vs only −$98.0B level change; **valuation masks ~25% of the annual selling** (KB-ZHAO-124) |
| Belgium TIC (proxy) | **$482.5B** (Jun, +$10.4B MoM) | >$500B = RED | 🟠 **series record high** | [CONF] TIC Jun 2026 — rank 78/78, +$17.56B genuine buying, 3rd straight rise. ⚠️ **NOT readable as custody migration — see next row** (KB-ZHAO-120) |
| **Belgium↔China flow correlation** | **rho = +0.050 (n=41)** | rho < −0.5 = proxy usable | 🟢 **PROXY FALSIFIED** | [CONF] ZHAO computation, TIC Table 3, 8/21 — ~zero on every window; Belgium buys in only 56% of China-selling months. **June's mirror pattern is chance** (VX-ZHAO-1.09, KB-ZHAO-121) |
| Foreign Official vs Non-Official | **official −$45.4B / non-official +$23.2B** (Jun) | — | 🟠 | [CONF] TIC Jun 2026 — official supply absorbed by the private bid. Aggregate level fall (−$72.1B) is **majority valuation**, only −$22.3B sold (KB-ZHAO-122) |
| Combined Anchor Selling | **Jun: China −$22.0B, Korea +$2.7B — anchors DIVERGED** | >$50B/qtr = 🔴 to LIQUID | 🟠 | [CONF] TIC Jun. **Q2 China total −$14.8B — does NOT trip the >$50B/quarter route** (VX-ZHAO-7.01) |
| Brent crude | **$93.94** (live) | Asia shock transmission | 🟠 | [CONF] ZHAO boot.py live pull **8/21 ~11:04 ET** (yfinance `BZ=F`). ⚠️ **Was $76.01 on this row since 7/9 — a 43-day-stale copy of someone else's number.** ⚠️ Do NOT compute a % move from the old row: `BZ=F` is a continuous front contract and a delta across a roll is fabricated. **HAWK/BRENT own the price** — ZHAO owns only Asia energy-shock transmission |
| Hormuz flows | 🧊 **[STALE 7/9]** recovered-then-RE-ESCALATED (Iran tanker strikes 7/8) | — | ⚪ **not ZHAO-refreshed** | HAWK/BRENT domain — **43 days stale, do not cite as current.** Reference their live value rather than this row |

### Currency / HK Peg
| Metric | Value | Threshold | Status | Source |
|--------|-------|-----------|--------|--------|
| USD/CNY | **6.71** | >7.30 = 🟠 | 🟢 | [CONF] ZHAO boot.py live pull, **8/21 ~11:04 ET** (yfinance) — stronger still vs 6.74 on 8/3 |
| HK Aggregate Balance | **HK$54,108M** | <$45B = 🟡 | 🟢 | [CONF] HKMA public API, daily interbank-liquidity series, **live 8/3**. Flat vs 7/31 (54,108) and 7/16 (54,056). No peg defense. Closes the 18d 🔴 STALE flag. (KB-ZHAO-108) |
| 1-mo HIBOR | **2.65589%** | — | 🟢 | [CONF] HKMA API 8/3 — fell from the 2.94% late-Jun print on file |
| HIBOR-SOFR Spread | **~-164bps** (widened ~28bps) | >-200bps = 🟠 | 🟢 still inside | ⚠️ **HIBOR leg [CONF] HKMA 8/3; SOFR leg [EST] ~4.30%, NOT re-verified — NY Fed *and* FRED both HTTP 403 this session.** Direction is certain (HIBOR-driven, primary-sourced); the level is not. Re-source SOFR before citing -164 as load-bearing. |
| USD/KRW | **1,385.70** (live 8/21; was 1,426.87 on 8/3) | >1,500 = BoK selling | 🟢 EASED THROUGH | [CONF] ZHAO boot.py live **8/21 ~11:04 ET** (yfinance). Through 1,400. **June TIC shows Korea BOUGHT +$2.70B — first net-buying month in 5** (KB-ZHAO-123), supporting ZHA-12's rate-lever read over reserve-defense-selling. ⚠️ Partly SK hynix listing-proceeds conversion, not purely the rate lever; foreign equity selling has NOT reversed (KB-ZHAO-107) |

### Domestic Stress
| Metric | Value | Threshold | Status |
|--------|-------|-----------|--------|
| **China Mfg PMI (Jul)** | **49.2** (Jun 50.3; missed 50.0 cons.) | <50 = contraction | 🔴 **CONTRACTION** [CONF] NBS 7/31 — first sub-50 since Feb. New orders **48.5, lowest since 2023**; production 49.9 (first output decline in 5mo); foreign orders back in contraction (KB-ZHAO-104) |
| **China Construction PMI (Jul)** | **47.0** | — | 🔴 **RECORD LOW** [CONF] NBS 7/31 — typhoon distortion bites hardest exactly here |
| **China Composite PMI (Jul)** | **49.3** | <50 = contraction | 🔴 **lowest since 2022** [CONF] NBS 7/31 — services gauge weakest since the initial Covid lockdowns; weakness no longer confined to property |
| China FX reserves / gold | **$3.4163T** end-Jun (-$26B MoM); gold **75.44Moz (~2,346t)**, 20th straight month | — | 🟢 [CONF] SAFE 7/7 — decline is USD-valuation, not a crunch. Gold only **8.8% of reserves** vs ~27% global CB avg → re-confirms gold is too small to be the Treasury-line destination (KB-ZHAO-109) |
| China Q2 GDP | **+4.3% YoY** (miss vs 4.5% consensus, down from Q1's 5.0%) | <4.5% = miss | 🟠 [CONF] NBS 7/15 via FXStreet (KB-ZHAO-095) — first deceleration print of 2026 |
| Land sales rev (H1) | **-6.5% to -27% YoY** | <-20% = RED | 🟠 [CONF] fiscal drag persists |
| LGFV Total Debt | ~60T RMB (fresh IMF range 44-58T, definitional variance) | >65T = RED | 🟠 [CONF] cross-checked 7/16, not clearly superseded |
| Debt swap program (2024-26 quota) | **94% utilized** (~1.62T RMB raised H1'26) | — | 🟢 [CONF] Caixin/NPC Observer 7/16 — hidden debt down 65% (14.3T→~5T RMB) since end-2023, program working better than stale data implied |
| Regional Bank NPL (Guizhou/Zhengzhou) | 11.6% / 9.55% 🧊 FROZEN | >12% = RED | 🟠 FROZEN 7/16 — attempted refresh, no bank-specific 2026 primary found (only province-level, different metric) |
| Small banks consolidated (2026 H1) | **130+** by Jun 4, accelerating | ZHA-06 >250 full-yr | 🟠 [CONF] NFRA via Yicai 7/16 — run-rate implies ~310+ full-year |
| PBOC 7d repo / LPR | **1.4%** / **3.00%–3.50%, HELD 14th mo** | <1.0% = RED | 🟠 [CONF] PBOC fixing **7/20** — restraint not incapacity: FX room existed (CNY 6.74), PBOC declined; cited bank NIM + yuan stability. Resolves ZHA-14 NO-FIRE (KB-ZHAO-105) |
| PBOC gold streak | **20 months** (+14.93t Jun, largest single-mo since 2023) | — | 🟢 [CONF] reserve diversification continues — NOT the primary UST-reallocation channel (too small by size, KB-ZHAO-099/102) |
| Korea CPI (Jun) | **3.2%** | — | 🟠 BoK HIKED +25bp to 2.75% 7/16 in response (KB-ZHAO-093) |
| China real property (BIS index) | **~86** vs 2021 peak ~113 | below 2006 level | 🟠 [CONF] WALTER SIG-W-20260706-017, orig. Hedgeye 7/5 — 20yr gains erased |

**Q2 GDP decomposition (Jul 15) → archived 8/21** to `archive/STATUS_q2gdp_decomposition_archived_20260821.md`. Accurate as Q2 *history*; **superseded as a current read** by July's PMI break. Headline retained: H1 real-estate investment **−18% YoY**, FAI ex-property only −2.7% — property did almost all the damage, but the July composite/services break means that containment frame no longer stands unaided. **Aug 31 PMI arbitrates.**

---

## CONVERGENCE MATRIX (rescored Jul 4; **per-vector freshness stamps added 7/16** so the table-level "rescored" date can't mask stale inputs — sweep item #11)

| # | Vector | Score | Current State | Data As-Of |
|---|--------|-------|---------------|------------|
| 1 | Four-Anchor UST Selling | 🔴 5 ↑ | **RE-ARMED 8/21: China broke $650B to $633.4B on −$21.96B of genuine sales (LT −$15.77B), TTM −$122.3B.** But the anchors DIVERGED — Korea BOUGHT +$2.70B. Foreign official sold $45.4B fleet-wide while non-official bought $23.2B. Q2 China −$14.8B does not trip the >$50B/qtr route. | China/Korea TIC **Jun'26, live 8/21** |
| 2 | Korea Crisis | 🟢 1 ↓ | **UPDATED 8/21 — the falsification tripwire FIRED 8/12.** KRW **1,385.47** live; 17 consecutive closes <1,450 (resolver needed 10, met 8/12), basis-independent. **Two independent instruments agree the node is cooling:** price (tripwire) and flow (June TIC — Korea BOUGHT +$2.70B, first net-buying month in 5). ZHA-12 at 80% holds. Downgraded 🟡→🟢. **Still not a full stand-down:** the two 8/3 caveats — foreign KOSPI selling not reversed, SK hynix listing-proceeds conversion — were **not re-checked** and are unverified rather than resolved. | **live 8/21 — TRIPWIRE FIRED 8/12** |
| 3 | Custodial Arbitrage | 🟡 2 ↓ | **DOWNGRADED 8/21 — not because the risk fell, because THE INSTRUMENT FAILED.** Belgium is at a series-record $482.5B on +$17.56B of buying, but rho(China,Belgium net sales) = **+0.05 over n=41** (~zero every window; Belgium buys in 56% of China-selling months). **The custody-migration inference is not supported month-to-month**, so this vector can no longer be scored off the Belgium level. Scored 2 = *cannot currently be measured*, NOT *benign*. **HANS owns the hub table; ZHAO does not re-pull.** | Belgium **Jun'26, live 8/21** |
| 4 | LGFV/Banking | 🟡 2 ↓ | **UPDATED 7/16 — mixed-freshness vector, see per-input dates:** Guizhou/Zhengzhou bank-specific NPL still FROZEN (no primary found); but debt-swap program now 94% of quota utilized + hidden debt down 65% since end-2023 (materially more constructive than stale data implied) and small-bank consolidation accelerating (130+ H1, ZHA-06 upgraded to 72%). Net: downgraded 🟠→🟡 — the fresh data leans more constructive (swap program working) than concerning, though the bank-specific NPL canaries remain unconfirmed. | **mixed: NPL Feb'26 🧊 FROZEN / debt-swap Jun'26 / small-banks Jul'16** |
| 5 | Property Zombification | 🔴 4 ↑ | **UPGRADED 8/3:** July **construction PMI 47.0 = RECORD LOW** (KB-ZHAO-104) on top of H1 real estate investment -18% YoY. Vanke ¥9.4B maturing 6mo; multi-year deleverage. Typhoon caveat applies hardest to this vector — ~8/31 print arbitrates. | construction PMI **Jul 31**; Vanke **Jul 4**; FAI decomposition **Jul 15** |
| 5b | **Domestic Demand / Broad Activity** *(new vector 8/3)* | 🔴 4 | **NEW — the session's headline.** Composite PMI **49.3, lowest since 2022**; services weakest since the initial Covid lockdowns; mfg new orders **48.5, lowest since 2023**. Breaks ZHAO's prior "property-only" containment frame. Discriminator vs the NBS typhoon attribution = **August PMI ~8/31**. | **Jul 31** |
| 6 | PBOC Defensive Wall | 🟢 1 ↓ | **UPDATED 8/3:** yuan stronger still at **6.74**; 7d repo 1.4%; **LPR held a 14th month (7/20)**. Zero defensive pressure — and the hold with FX room available is *restraint*, which is a stronger signal of comfort than the level alone. | yuan **live 8/3**; LPR **Jul 20** |
| 7 | HK Peg Channel | 🟢 1 | **LIVE-VERIFIED 8/3 via HKMA API:** AB HK$54,108M flat, no peg defense; 1M HIBOR 2.656%; spread widened to ~-164bps but still inside -200. Stale flag closed. ⚠️ SOFR leg unverified (403s). | **live 8/3** (SOFR leg [EST]) |
| 8 | LNG/Energy Shock | 🟠 3 (↑ 7/9) | RE-ARMED: US-Iran truce collapsed 7/7-7/8, Brent $76.01 settle 7/9, Iran tanker strikes. Capital-gated on Fri 7/10 sustain verdict (BRENT/HAWK domain) — not a ZHAO-owned re-score, marked up for consistency only. | **BRENT/HAWK-owned, Jul 9** |
| 9 | USD/CNY Defense | 🟢 1 | **6.74**, appreciation bias intact. | **live 8/3** |
| 10 | Gulf Recycling | 🟡 2 | Revenue recovering with oil exports; acute collapse over. | **BRENT/HAWK-owned, Jul 4** (not re-verified since) |
| 11 | Gulf Infra Destruction | 🟡 2 | Rebuild underway; capacity recovering. | **BRENT/HAWK-owned, Jul 4** (not re-verified since) |

**Total: ~27/60 — 🟠 ELEVATED** *(8/21: vector 1 re-armed 4→5 on the $650B breach; vector 3 cut 3→2 on the falsified proxy; **vector 2 Korea cut 2→1 on the fired tripwire**. Net +1.)*

> **8/21 addendum:** the +2 again understates a rotation. **Vector 1 is now the live one** and it re-armed on hard *flow* data, not a level. **Vector 3's cut is a measurement failure, not an all-clear** — read it as *instrument down*, because scoring a vector low for the wrong reason is exactly how a custody channel would hide. Prior 8/3 note follows.

*(8/3)* (denominator now 60: vector 5b added 8/3. Was ~25/55 on 7/16. Net +1 on a **compositional rotation, not a level change** — the *financial/external* vectors eased further [2 Korea 3→2, 6 PBOC 2→1, 7 HK live-verified 1] while the *domestic-activity* vectors deteriorated [5 property 3→4, plus the new 5b domestic demand at 4].)

> **The number moved by +1 and that badly understates what changed.** The risk **relocated**: away from currency/peg/policy-defense stress, which is now about as quiet as this matrix has scored it, and into China's real domestic economy, which just printed its weakest composite activity since 2022. A flat total across a rotation like that is the matrix working as designed, not a quiet quarter. Risk is now concentrated in vectors **5 + 5b** (domestic activity, both 🔴), with vector 1 (China TIC) dormant until June TIC ~Aug 17-18.

---

## CROSS-AGENT TRANSMISSION

| Agent | Signal | State |
|-------|--------|-------|
| **LIQUID / PROME** | **June TIC: China breached $650B → $633.4B on −$21.96B genuine sales (LT −$15.77B), TTM −$122.3B. Foreign official −$45.4B vs non-official +$23.2B. Belgium proxy FALSIFIED as an interpretation instrument (rho +0.05, n=41).** 🟠 route fires on ZHAO's own table (China TIC <$650B); Q2 −$14.8B does NOT trip the 🔴 >$50B/quarter route | 🟠 **OUTBOX 8/21, awaiting PROME route** |
| **PROME** | **`CLAUDE.md` §BELGIUM PROXY METHODOLOGY needs rewriting** from deterministic identities to probabilistic language. ZHAO owns and will edit — flagged because **HANS and LIQUID both consume this proxy**. Plus: a magnitude inside the Will-approved KB-ZHAO-102 reframe is understated ~3x (not rewritten unilaterally) | 🟠 **OUTBOX 8/21** |
| **SAM** | **Japan −$26.86B in June is BILLS, not duration** (ST −$23.11B, LT only −$3.75B) — second such month (May ST −$59.79B). A roll-off, not duration selling. Not ZHAO's to deep-dive | 🟠 **listed 8/21**, route via PROME |
| **HANS** | France −$20.92B (June, large seller) · Belgium at series-record $482.5B — **hub table is HANS's**, ZHAO does not re-pull. ⚠️ **The custody-migration inference HANS may be carrying is falsified month-to-month** (VX-ZHAO-1.09) | 🟠 **listed 8/21**, route via PROME |
| **VULCAN** | CXMT ask (n=3: 8/3, 8/13, 8/21). Bit-output/node-mix **not ZHAO's, UNCHECKED (not "unavailable")**; WFE export-control bindingness **IS ZHAO's and also not done** — scoped for next session, no date given. Sent them the Belgium-proxy falsification as a **shape caution** for their FL-VULCAN-10 (one event / two channels / opposite signs — same shape that fooled me today) + suggested they base-rate the semicap-vs-memory divergence before citing the mechanism | 🟢 **REPLIED 8/21 — disposition, not an answer** |
| MIDAS | July PMI break — copper seam reconciled toward MIDAS's read (China weak, copper firm for non-China reasons) | 🟠 outbox 8/3, awaiting PROME route |
| LIQUID | China TIC $651.1B (Apr) — 7/5 delivery, and the 7/16 reframe routed by PROME directly | 🟢 DELIVERED (superseded by the 8/21 packet above) |
| HENRY | Yuan strong (6.71), HK carry eased — China *financial* stress leg still quiet; the stress is in flows and domestic activity | 🟢 |

---

## EXIT RULES

### Thesis Kill
- Belgium <10% YoY for 2 prints AND China >$700B for 3 prints *(neither close: Belgium +12.1% YoY, China $633.4B)*
- Massive fiscal stimulus >5% GDP with LGFV full backstop

### Falsification tripwires now
- **China TIC >$680B for 2 consecutive months** → the selling was noise. *(Moved further away 8/21 — China at $633.4B, a series low.)*
- 🆕 **8/21 — the live test is now COMPOSITION, not level:** if **July TIC (~Sep 16) shows China's LT/coupon selling stopping** (LT net ≥ −$5B), June was a one-month portfolio event and the $650B breach is a level, not a trend. **Continuation at ≈−$15B/month in duration** is the first hard-flow re-opening of the demand-hole thread since spring.
- 🆕 **8/21 — Belgium proxy re-usability:** the custody-migration reading may be reinstated **only if rho(China, Belgium net sales) falls below −0.5** on a rolling 24m window (VX-ZHAO-1.09). Until then the Belgium level is **not** evidence about China's true position in either direction.
- ✅ **Korea KRW <1,450 sustained → contagion node cooling: FIRED 2026-08-12, graded 8/21 (9d late).** Run began 7/30 (close 1442.28); **10th consecutive qualifying close was 8/12 at 1412.18.** Now 17 closes unbroken, live 1385.47. ✅ **Basis-independent** — re-tested on the stricter intraday-HIGH basis because spot FX has no official close (WALTER N5 rule, still unprocessed in ZHAO's lane): **0 of 10 days printed a high ≥1450** (max 1447.46). Same fire date both ways. **This falsifies ZHAO's Korea-as-UST-selling-anchor leg**, and June TIC agrees independently (Korea BOUGHT +$2.70B). ⚠️ **NOT a full stand-down — two 8/3 caveats are UNVERIFIED, not resolved:** foreign KOSPI selling had not reversed, and part of the won move is **SK hynix listing-proceeds conversion**, not the rate lever (KB-ZHAO-126).
- **USD/CNY 7.30:** near-invalidated — yuan at 6.71. Reinstate only on a DXY spike + PBOC resuming aggressive defense.

---

## CALENDAR

*(July rows and the Aug 7/9/13 prints resolved or elapsed — moved to `archive/`. Forward-looking only from 8/21.)*

| Date | Event | Priority |
|------|-------|----------|
| ~Aug 17-18 | **June TIC** — ✅ **DONE 8/21**: China $633.4B (breach), Belgium $482.5B (record), Korea +$2.70B. ZHA-04 FIRED, ZHA-03 resolved NO | ✅ done, KB-ZHAO-119..124 |
| **Mon Aug 31** | **China August PMI — the (a)-broadening vs (b)-typhoon discriminator** for July's 49.2/47.0/49.3 break | 🔴 **registered arbiter, 10 days out — highest-value scheduled read ZHAO owns** |
| ~Sep 7 | China Aug trade data + SAFE FX reserves/gold | 🟠 |
| ~Sep 9-10 | China Aug CPI / PPI | 🟡 deflation check |
| **~Sep 16** | **July TIC** — ⚠️ **the CORRECT arbiter for ZHA-11** (the 7/9 30Y auction is a July event; June TIC structurally cannot test it — see §6). Also: does China's June duration-selling continue? | 🔴 |
| ~Sep 22 | China LPR fixing — 15th month of hold? | 🟠 |
| **September 2026** | **Xi → Washington, White House summit with Trump** (Bessent–He Lifeng prep) — truce-extension venue | 🟠 (KB-ZHAO-110) |
| **October 2026** | **Fifth Plenum, 20th CPC Central Committee** — 15th Five-Year-Plan venue; realistic home for any large fiscal figure | 🟠 (KB-ZHAO-106) |
| Nov 10 2026 | Reciprocal-tariff suspension expiry (truce clock) — re-verified 8/3, an "Aug 12" claim was a 2025 decoy | 🟠 |
| ~May 2027 | Rare-earth control postponement expiry (1yr clock) | 🟡 |
| Dec 2026 | SEC Cash Clearing mandate | 🟡 |

⚠️ **The 8/3 CALENDAR named June TIC as a ZHA-11 arbiter. It cannot be** — corrected above and in PREDICTIONS.tsv.
⚠️ **`scripts/boot.py`'s `CATALYSTS` list is hardcoded and was never updated with these rows** — it printed *"nothing within ±30d"* at this morning's boot while ZHA-15 was 8 days overdue and the Aug-31 PMI was 10 days out. **Fix registered in NEXT ACTIONS.**

---

## PREDICTIONS (status Aug 21)

| ID | Prediction | Conf | Status |
|----|-----------|------|--------|
| ZHA-01 | USD/CNY breaks 7.30 | 18% ↓ | OPEN — yuan appreciated further to **6.71** (live 8/21), thesis weaker still |
| ZHA-02 | 10Y rises on risk-off | — | ✅ CONFIRMED (Mar) |
| ZHA-03 | Belgium >$500B | 25% | ❌ **RESOLVED NO 8/21** — Q1-Q2 window closed; peak in-window $482.5B (Jun), **$17.5B short**. FALSE at 25% = well-calibrated miss. ⚠️ **Trajectory disagrees with the grade**: series-record high, 3 straight rises, +$17.56B bought. **Recommend re-registering for H2 — but NOT on the custody-migration story, which is falsified** (KB-ZHAO-120/121) |
| ZHA-04 | China <$650B | **42%** | ✅ **RESOLVED YES — FIRED 8/21.** June **$633.4B**, breaches by $16.6B, in-window (Q2). Series low of 78 months. **Genuine selling**: net −$21.96B, LT/coupon −$15.77B. TRUE at 42% after two cuts — the near-misses (Mar/Apr) lacked this composition change (KB-ZHAO-119) |
| ZHA-05 | Regional NPL >12% | 50% | OPEN — Guizhou 11.6% (stale) |
| ZHA-06 | >250 small banks consolidated | 60% | OPEN |
| ZHA-07 | Liquidity crunch forcing UST sales | 60% | OPEN |
| ZHA-08 | Gulf recycling >$50B/qtr | — | ❌ FALSIFIED — Hormuz reopened, exports 90%+, Brent $72 |
| ZHA-09 | Saudi TIC <$120B by Jun 2026 | 10% ↓ | ❌ LIKELY MISSED — Saudi ~$148.8B, oil recovered |
| ZHA-10 | Yuan oil settlement >$5B cumulative | 40% | OPEN |
| ZHA-11 | China NOT the 30Y 7/9 indirect-bid (77.74%) driver | 68% | OPEN — SURVIVES (graded 7/16 in-window). ⚠️ **June TIC is the WRONG arbiter** — a July event cannot be tested by June flows. Correct arbiter: **July TIC ~Sep 16** |
| ZHA-12 | BoK hike (delivered) succeeds as currency defense (won holds/strengthens, EASES demand-hole) | **80% ↑↑** | OPEN — branch (i) satisfied on BOTH legs: won **1,426.87** (strongest since late Feb, ~+6.96%/mo) and BoK reiterating tightening. Runs through the Aug FX print; not graded early (KB-ZHAO-107) |
| ZHA-13 | Korea May TIC shows net UST SELLING (reserve defense, deepens demand-hole) | 50% | ✅ RESOLVED NEUTRAL (May print, 7/16). **June follow-up 8/21 (context, not a re-grade): Korea BOUGHT +$2.70B, first net-buying month in 5** — the post-hike test this row itself called for; supports ZHA-12 (KB-ZHAO-123) |
| ZHA-14 | PBOC cuts 1yr/5yr LPR at the **7/20** fixing | 30% | ❌ **RESOLVED NO (7/20)** — HELD 3.00%/3.50%, 14th month. FALSE at 30% conf = well-calibrated miss. Graded 8/3, 14d late (KB-ZHAO-105) |
| ZHA-15 | Politburo late-Jul meeting signals STIMULUS branch (concrete new fiscal measure + RMB figure) | **18%** | ❌ **RESOLVED NO — STEADY-COURSE (graded 8/21, 9d late).** Nothing with an RMB figure inside the 7/30→8/13 window; leaders pledged to accelerate **already-budgeted** spending, *"no major policy bazooka"* (OCBC). **FALSE at 18% = well-calibrated CORRECT call.** ⚠️ **A real package landed 8/21 — 8 days late** (subsidy ceilings 3,000→5,000 / 50M→75M / 10M→20M yuan). Letter failed at 2wk; thesis vindicated at ~3wk (KB-ZHAO-125) |

---

## NEXT ACTIONS

**Done Aug 21 (June TIC session):** June TIC pulled direct from Treasury primary (Table 5 + Table 3) ✓ · **ZHA-04 graded RESOLVED YES/FIRED**, in-window, on the flow composition not just the level ✓ · **ZHA-03 graded RESOLVED NO**, window expired, with the trajectory disagreement recorded ✓ · **Belgium-proxy interpretation rule tested and falsified** (rho +0.05, n=41), new instrument VX-ZHAO-1.09 registered with re-usability bands ✓ · China TTM net sales computed −$122.3B, correcting a ~3x understatement carried in the reframe text ✓ · self-correction logged after asserting −$46.4B unchecked (KB-ZHAO-124) ✓ · ZHA-11's wrong-arbiter defect found and corrected on both surfaces ✓ · Korea post-hike test logged as ZHA-12 support ✓ · VX 1.01/1.02/1.03/1.04/7.01 refreshed off 48-day-stale Apr/Mar vintages ✓ · KB-ZHAO-119..124 ✓

**Owed / next boot, in priority order:**
1. ✅ **ZHA-15 GRADED 8/21** — RESOLVED NO / STEADY-COURSE, 9d late. FALSE at 18% = well-calibrated correct call. ⚠️ **Spec defect found at resolution: my STIMULUS bar required 'a concrete RMB figure' with NO MAGNITUDE FLOOR** — it would have fired on the modest 8/21 ceiling-raises, i.e. on exactly the 'measured not expansive' outcome it was designed to exclude. Next registration of this type gets a size floor in NEW outlay (KB-ZHAO-125).
1b. ✅ **Korea <1,450 tripwire GRADED 8/21** — FIRED 8/12, basis-independent. Falsifies ZHAO's Korea anchor leg. **Owed next: re-check the two unverified caveats** (foreign KOSPI selling; SK hynix conversion share) before calling Korea risk closed (KB-ZHAO-126).
2. 🔴 **Aug 31 August PMI — 10 days out.** The registered (a)-broadening vs (b)-typhoon discriminator for July's break. Highest-value scheduled read ZHAO owns.
3. ✅ **REFRAME FIX EXECUTED 8/21 — Will-ruled in-session** (*"Do the reframe fix and send LIQUID the withdrawal"*). Doctrine KEPT; **rotation mechanism STRUCK** (refuted, VX-ZHAO-1.10); entity-shifting demoted to *possible*; **datum removed from canon entirely** — `CLAUDE.md` now points at VX-ZHAO-1.03/1.02 and hardcodes no live magnitude. Recorded that the doctrine now rests on **valuation** (~$107.3B appreciation vs $118.9B sold), which is weaker and reverses if markets stop rising. KB-ZHAO-102 **amended, not rewritten** — the 7/16 statement of record is intact, Status→CORRECTED. Applied to `CLAUDE.md`, KB-102, STATUS (×3 surfaces), NEXUS_BRIEF.
3a. ✅ **LIQUID WITHDRAWAL SENT AND ROUTED 8/21.** PROME routed all three packets same-session; **verified on origin by md5, byte-identical** — LIQUID inbox ×2 (withdrawal + TIC/Belgium), NEXUS inbox ×1, plus PROME routing stubs to SAM (Japan bills-not-duration leg) and HANS (France leg + a carry-confirm ASK on the falsified Belgium proxy, reply-to-ZHAO cc-PROME). PROME ruled: KB-ZHAO-102 handling **stands** (record-beside, no separate Will pass — the rotation half was already amended under Will's own word); Belgium §METHODOLOGY rewrite **proceed, ZHAO's canon**, with a rider to keep the retired identity-rule as a dated dead record — **done, recovered verbatim from git and stamped DO-NOT-APPLY.**
✅ **HOLD RELEASED AND PACKETS FILED 8/21.** PROME made both stubs **move-tolerant** (they now carry owner + filename + convention-dir, so the citation survives the move) and all three packets are now in `outbox/delivered/`. ⚠️ **ORDER MATTERED AND WAS CHECKED:** PROME's tolerance commit existed only **locally, unpushed** — the stubs *on origin* still hard-cited the outbox path, so moving first would have left a window where a desk booting from origin followed a dead link. **Verified before acting, swept PROME's commit to origin via the push-train, re-verified tolerance live on both stubs, then moved.** **Standing lesson for this desk:** a peer's "you're clear to go" describes their **local** state; the shared source of truth is origin. **Check the fix is where the consumer reads, not where the fixer wrote it.** `[[finding_record_of_an_action_is_not_the_action]]` · `[[finding_push_train_hides_a_failed_commit]]`
3b. ✅ **`CLAUDE.md` §BELGIUM PROXY METHODOLOGY REWRITTEN 8/21** — identities → probabilistic language, with the rho evidence, the base rate, the honest limit, and re-usability bands (VX-ZHAO-1.09) in a read-first box.
4. 🔴 **Fix `scripts/boot.py`** — three defects found at this morning's boot: (a) `CATALYSTS` hardcoded and never updated, so §4 printed *"nothing within ±30d"* with a grade 8 days overdue and the Aug-31 arbiter 10 days out; (b) `KEY_FIGURES` points at **VX-ZHAO-4.01** (Jun PMI 50.3) when the live row is **VX-ZHAO-6.11** (Jul 49.2) — two rows for one metric, boot resolves to the dead one and reported both the age and the sign wrong; (c) §3's TIC watch was one print off because VX lagged STATUS by two vintages. **(c) is closed by this session's VX refresh; (a) and (b) are open.**
5. 🟠 **Outbox routing owed to PROME** — `2026-08-21_to-LIQUID-PROME_june-tic-650-breach-and-belgium-proxy-falsified.md`. 🟠 route to LIQUID fires on ZHAO's own table (China TIC <$650B). Q2 −$14.8B does **not** trip the 🔴 >$50B/quarter route.
6. 🟠 **Cross-agent legs I did not deep-dive** (boundary rule): Japan's −$26.86B is **bills, not duration** → SAM. France −$20.92B → HANS. Belgium hub table → HANS. HK sold $9.33B while the peg is quiet — that one *is* mine, log next session.
7. 🟠 **VULCAN CXMT ask, n=3** (8/3, 8/13, 8/21) — **replied 8/21; the reply was a disposition, not an answer.** Asks (1) bit output and (2) time-to-market are **not ZHAO's domain and are UNCHECKED — explicitly NOT stamped "unavailable,"** because I have not looked and classifying my own inaction as a property of the world is the wrong close (`finding_unfetched_is_not_unavailable`). Ask (3) **WFE export-control bindingness on Chinese DRAM IS ZHAO's** and is **also not done** — committed as a scoped next-session item, sourced, answer as a range with unknowns named. **No date promised to VULCAN** (ZHA-15's overdue grade is ahead of it in the queue). ⚠️ Declined to give a same-session read because it would feed VULCAN's FL-VULCAN-10, which they registered CANDIDATE precisely to stop mechanism-by-repetition.
8. 🟡 **Re-register ZHA-03 for H2-2026** with a mechanism that survives the rho test — do not re-file it on custody migration.
9. 🟡 **Inbox: 10 items + 17 in the WALTER lane, oldest 7/16.** Needs a dedicated inbox spawn.
10. 🟡 Re-source SOFR (NY Fed + FRED both 403'd 8/3) — HIBOR-SOFR level still unverified on its SOFR leg.

## BOTTOM LINE

**AUG 21 — the threshold I have tracked for five months broke, and on the same print the instrument I use to interpret it failed.**

**China's SAFE-reported Treasury line fell to $633.4B**, breaching the $650B line by $16.6B after two near-misses held and May rebounded. This is not a valuation artifact: **China sold $21.96B, of which $15.77B was coupons** — the first month this cycle it sold *duration* in size, where May's rebound was bills with the coupon leg flat. It is the lowest reading in the 78-month series. **ZHA-04 fired at 42% confidence**, a prediction I had cut twice; the cuts were right about the near-misses and the breach came with a composition change those lacked. Zooming out makes it larger, not smaller: **trailing-12-month net sales are −$122.3B against a level change of only −$98.0B**, so valuation has been *masking* about a quarter of the annual selling. That figure is ~3x the "~$40B decline" this thread has been quoting.

**But the interesting half of the session is that I could have written a much cleaner story and it would have been wrong.** Belgium printed an all-time series high of $482.5B on $17.56B of genuine buying. My own `CLAUDE.md` says, flatly, that Belgium rising while China falls means custody migration and a net-neutral true position — which would have let me report ~80% of China's sale as relabeling. **I tested the rule rather than applying it. rho(China, Belgium net sales) = +0.05 over 41 months, indistinguishable from zero on every window I tried, and Belgium buys in only 56% of the months China sells — a coin flip.** June's textbook mirror pattern is two large independent moves that happened to point opposite ways. The rule has been applied as if deterministic for ~5 months and was never base-rated. **I am marking my own methodology wrong rather than reporting the tidier finding it would have produced.**

**What that leaves me with, honestly stated:** China is genuinely selling Treasuries, in size, in duration, and has been for a year. **I cannot currently tell you where the money went** — the Belgium channel can't answer it, Agency rotation and off-SAFE state channels remain untested, and the Will-approved KB-ZHAO-102 reframe stands: this is a *SAFE-reported Treasury-line reduction*, not demonstrated de-dollarization. The custodial-arbitrage vector is scored down to 2 because it *cannot be measured*, not because it is benign — and a vector scored low for the wrong reason is precisely how a custody channel would hide.

**The wider print cuts against a simple demand-hole read.** Foreign official sold $45.4B in June; foreign non-official **bought $23.2B**. The private bid is absorbing official supply — a different market structure from "nobody is buying," and the distinction is LIQUID's to price. And the aggregate is a trap: total foreign holdings fell $72.1B but only $22.3B was sold, so **anyone quoting the level as selling overstates it ~3x.** China is the exception that makes the rule dangerous — its drop *is* ~85% real, so a level-only reader gets the aggregate badly wrong and China roughly right, by luck.

**Korea went the other way and that matters:** +$2.70B bought, the first net-buying month in five, in the same month the won ran to 1,385. That is the post-hike test ZHA-13 asked for, and it supports ZHA-12 — the rate lever is doing Korea's defense work, not reserve liquidation. **The two Asian anchors have diverged.**

**A late addition that matters more than the arithmetic.** Will asked how to repair the ~$40B magnitude error sitting inside the Will-approved reframe. Chasing it turned up something bigger: **the reframe's primary mechanism is testable, and it fails.** The reframe explains China's falling Treasury line as *Treasury→Agency rotation*. Rotation requires Agency holdings to rise as Treasuries fall. **China's Agency holdings fell $37.9B over the same twelve months, and it sold both in June.** The correlation between the two flow series is −0.025 — zero. **So today I falsified two of my own interpretation instruments, not one:** the Belgium proxy in the morning and the rotation mechanism in the afternoon, both by testing a rule I had been applying rather than continuing to apply it.

**The reframe's conclusion still stands, and I want to be precise about why.** China's total US long-term securities holdings are down only 1.0% over the year — but that is because markets appreciated ~$107.3B against $118.9B of net selling. *"Aggregate exposure roughly unchanged"* is true on the stock and false on the flow, and the thing holding it up is price, not portfolio construction. **That is a materially weaker support than the reframe claimed, and it is contingent on markets continuing to rise.**

**What would change my mind:** if July TIC (~Sep 16) shows China's coupon selling stopping, June was a one-month portfolio event and the $650B breach is a level, not a trend. If it continues at −$15B/month in duration while foreign official keeps selling and the private bid stops absorbing, the demand-hole thread re-opens on hard flow evidence for the first time since spring. **Before then, Aug 31's PMI is the bigger read** — a second sub-50 composite turns July's break into a thesis.

---

**🚩 THESIS RE-FRAMED 7/16 (Will-approved, KB-ZHAO-102) — AMENDED 2026-08-21, Will-ruled in-session (*"Do the reframe fix"*).** Canonical text now lives in `CLAUDE.md` §BELGIUM PROXY METHODOLOGY; this is the STATUS summary.

**THE DOCTRINE — unchanged and still correct:** ZHAO does **not** describe the $650B threshold as "genuine exit" or "de-dollarization." **The line tracks SAFE's own narrowly-defined, TIC-visible, Treasury-specific holdings — a real, mechanical, market-moving threshold that grades exactly as before — but a breach is NOT a reliable signal of China's aggregate US-dollar exposure.** Use **"SAFE-reported Treasury-line reduction."**

**THE MECHANISMS — amended. Both of the reframe's named explanations are gone:**
- ~~**Treasury→Agency rotation**~~ 🔴 **REFUTED by direct measurement 8/21.** China's Agency holdings **fell** $179.9B→$142.0B (−$37.9B TTM) on −$40.3B of net sales; rho(Treasury, Agency) = −0.025, n=41. It sold both. **Do not cite rotation.**
- **Off-SAFE entity-shifting** — **demoted from evidence to possibility.** Not testable from TIC country lines, which attribute by custodian, not by Chinese owning entity.

**WHAT HOLDS THE DOCTRINE UP NOW — valuation, which is weaker and contingent.** Total LT US-securities holdings moved **−$11.6B (−1.0%)** against **−$118.9B sold**; markets added back ~$107.3B. *"Aggregate exposure roughly unchanged"* is **true on the stock, false on the flow.** **If markets stop appreciating, this support goes and the doctrine needs re-examining.**

⚠️ **NO LIVE MAGNITUDE IS HARDCODED IN CANON ANY MORE** — the old "~$40B" welded a datum into a doctrine, where it rotted ~5 weeks and was ~3x understated. Figures live in **VX-ZHAO-1.03** (TTM) and **VX-ZHAO-1.02** (level) only.

⚠️ **PERIMETER — two correct TTM figures; always say which:** **−$122.3B** all Treasuries incl. bills (Table 3) · **−$91.3B** coupons only (Table 1). They reconcile to the dollar.

⚠️ **The MIRROR ARM was also established 8/21:** 7/16 showed "Belgium flat while China falls" ≠ exit; this session shows **"Belgium up while China falls" ≠ custody migration** (rho +0.05, n=41). Both arms of the Belgium rule over-claimed — `CLAUDE.md` §BELGIUM PROXY rewritten from identities to probabilistic language, with re-usability bands at **VX-ZHAO-1.09**.

🔴 **DOWNSTREAM: LIQUID banked "China rotation" as one of four independent demand-hole refutations. Withdrawal packet SENT 8/21.** The other three legs are untouched.

**June TIC (8/21) graded on this framing:** China **$633.4B, −$25.9B MoM, BREACHES $650B** on −$21.96B of genuine sales (LT −$15.77B) — ZHA-04 **FIRED** at 42%. Belgium **$482.5B, series record**, +$17.56B bought — ZHA-03 **RESOLVED NO**, window expired $17.5B short. Korea **+$2.70B bought**, first net-buying month in 5 — supports ZHA-12. Foreign official −$45.4B vs non-official +$23.2B. *May-TIC grading recap → `archive/STATUS_tail_may-tic-recap_archived_20260821.md`.*

**Long-standing gaps (unchanged):** Guizhou/Zhengzhou bank-specific NPL 🧊 FROZEN, no primary · Korea official-vs-all-residents scope split (VX-ZHAO-2.07) · SOFR leg of HIBOR-SOFR unverified (NY Fed + FRED 403) · CNH-CNY spread.

*Prior April-and-earlier check-ins → `archive/STATUS_archive_20260704.md`. Research corpus RP-ZHAO-1..9 in `sources/`.*
