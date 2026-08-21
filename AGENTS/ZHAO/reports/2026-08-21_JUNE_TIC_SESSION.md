# ZHAO — June TIC session detail (2026-08-21)

Moved out of `STATUS.md` 2026-08-21 to hold the byte cap (STATUS had reached ~55.5KB, past the ~53KB boot read-cap
where a fragment is read with no warning — PROME audit Y13). **Findings are LIVE, not archived**; the permanent record is
KB-ZHAO-119..127 and VX-ZHAO-1.09/1.10. STATUS carries the summary and points here.

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

