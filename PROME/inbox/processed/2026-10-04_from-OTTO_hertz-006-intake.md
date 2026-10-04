# OTTO -> PROME: Hertz SIG-W-20261004-006 intake: ADDS A WATCH (the Australian sale itself has no effect)

**Date:** 2026-10-04 (Sun), session 027 · **Assignment:** PROME packet `60e6ccb36` (explicit intake, bounded to one item; Will's word 17:23 ET) · **Records commit:** `ab12815c6`

## Answer
**No.** The reported sale of Hertz's Australian business does **not** imply fleet disposal relevant to OTTO's used-car thesis. It is case (a), a business changing owner, not case (b), vehicles liquidated into the used market, and even under (b) the cars would be sold in Australia. **Disposition recorded: ADDS A WATCH.** The one route by which Hertz's distress could reach US used-car supply is now a dated row: an **HVF III amortization event or a Hertz Chapter 11**, tested around **2026-12-01**. WALTER's withdrawal of "strengthens OTTO's fleet channel" (`7747ea125`) is **confirmed**.

## (a) Owner change vs (b) liquidation

| Test | Evidence | Grade |
|---|---|---|
| Where the cars are | Australia, a right-hand-drive market. They cannot enter US wholesale supply. | EST (physical) |
| How they are financed | Their own ABS: HA Fleet Pty, **$226M** at 6/30/26; upsized to **AUD$400M max** and extended to **Sep 2028** in July 2026 | CONF 10-Q Q2-26 (0001657853-26-000046), Note 5 / Note 14 |
| Scale | $226M = **1.8%** of Hertz's **$12,710M** vehicle debt. For comparison, Americas sold **$4,495M** of vehicles in H1-26 in normal course. | CONF 10-Q, arithmetic |
| What the stand-alone financing implies | A whole-business sale where fleet and financing transfer together (case a) | INFERRED |
| Direction of the "forced seller" read | A business sale raises corporate cash **without** dumping cars, the opposite of the 2020 mechanism. It can also signal tight liquidity, which is why the watch stays. | EST |

## The US channel: the watch, and why it is not a fire today

| Item | Figure | Source |
|---|---|---|
| Route to forced US sales | HVF III amortization events include "defaults by … THC, as administrator". Principal then repays from US vehicle sales (the card's 2020 template). | CONF 8-K 0001657853-26-000054 (8/27) |
| Platform access at creation | **$834.75M** third-party HVF III notes priced 8/27 (Class A 5.51% / 5.87%; Class D 9.62% / 10.70%) | same 8-K |
| Headroom | VFN availability **$1,893M**, cash **$631M** at 6/30; liquidity "approximately **$984 million**" at Q2 end | CONF 10-Q; 8-K Ex.99.1 (8/6) |
| Dated test | **HVF III Series 2021-2 $2,000M (2.12%)** AND the **$200M 4.63% senior notes** both mature **12/2026**. The Dec-1 day comes from Bloomberg via -017; the 10-Q gives the month only. | CONF 10-Q / PRESS |
| Direction | Hertz **reads** OTTO's hinge, it does not drive it: Americas depreciation per unit is **$304 vs $248 (+22% YoY Q2; H1 +1%)**, residual weakness already carried at ML-OTTO-180. It becomes a driver only on a forced US sale. | CONF 10-Q MD&A |

Watch row: `AGENTS/OTTO/docket/CATALYSTS.tsv` ~2026-12-01, with a mirror in the STATUS CRITICAL TIMELINE. **FIRE** = an amortization event or a Ch.11. **NOT a fire** = a non-US business sale, a corporate amend-and-extend, or normal-course disposals. **CLOSE** if the notes are paid or extended and 2021-2 is refinanced with no amortization event. The credit read is LIQUID's; OTTO reads only the fleet consequence. ⚠️ A US sale at a young fleet (94% MY2025–26, per the 8/6 release) would hit late-model wholesale first. Transmission to subprime collateral would be indirect [EST].

## What was new, and to whom (CATO BF1)
- **"Already delivered on 10/1" holds per recipient, not fleet-wide.** -017 went to LIQUID, BROCK, CARL and SHADE. **OTTO was not on its routing**, so the PJT, maturity and liquidity content reached OTTO for the first time through -006.
- **New to everyone and still UNVERIFIED:** the Australian-sale specifics (AFR via a commentator's screenshot) and the "50s" term-loan marks (one account's read). Neither changes this disposition: if both are true, the grade above still holds.
- **What OTTO's pull added beyond the card:** the HVF III platform state, the 12/2026 fleet-ABS maturity, and the scale of the Australian unit, all from filings.

## EDGAR check (query stated)
`data.sec.gov/submissions/CIK0001657853.json` (Hertz Global Holdings) and `CIK0000047129.json` (The Hertz Corporation), fetched 2026-10-04 17:25 ET. The latest filing is 10/2. **No 8-K on an Australian sale.** The 8-Ks since August are: 8/6 Item 2.02 earnings (the release has 0 hits for "Australia"), 8/20 voting agreement, 8/27 HVF III notes, 9/10 officer changes, and 10/1 board changes. The Q2 10-Q mentions Australia only in its debt and location lists. **SEARCH-NOT-FOUND at filings. The sale is not refuted:** a sell-side process normally precedes any 8-K.

## Incidental: LIQUID's lane, not acted on (routing is PROME's call)
- **8-K 10/1 (0001657853-26-000061), Item 5.02:** three directors resigned (Blake, Clark Dougherty, Wagner; the filing says "not because of any disagreement"). Three were appointed, including **Adam Zirkin, "associated with Knighthead Capital Management"**, at $1/yr. This is a primary dated fact that neither card carries.
- The **$2.0B HVF III 2021-2 December maturity** sits beside the $200M notes LIQUID already holds.

## Skipped controls (named, with reasons)
- **SKIPPED:** the sweep of the 10/1 fired CATALYSTS rows (10-D cycle and repair, Tricolor Counts 7–8, CRMT L479). Reason: bounded spawn. They are still owed and flagged in STATUS and MEMORY.
- **SKIPPED:** WALTER handoffs `SIG-W-20261002-021` and `-022`. They were left unread and unconsumed (bounded to one item).
- **N/A:** CHANGELOG (no pivot), MAINTENANCE (no structural change), PREDICTIONS (0 overdue, 0 due within 14d per boot.py), consumer_check (no figure superseded), memory_index_check (no auto-memory written).
- **RUN:** boot.py rc 0 · corrections_boot_check rc 0 · claim_check weekday clean (4 files) · read_cap_check rc 0. ⚠️ STATUS.md is at **74% of budget, 293 B under the 75% rotation trigger**, so the next writing session should rotate. Orphan check: only foreign paths (CATO, FALCON, WALTER, PROME), none swept.
- **Push:** not pushed (PROME pushes).

## COMPLETION — OTTO — 2026-10-04
STATUS: ✅ DONE
CHANGED: AGENTS/OTTO/workbook/ML.tsv, docket/CATALYSTS.tsv, STATUS.md, board_log.tsv, MEMORY.md, LAST_COMPLETION.md, NEXUS_BRIEF.md, inbox→processed (2 files), PROME/inbox/2026-10-04_from-OTTO_hertz-006-intake.md
RESULT: Hertz -006 = ADDS A WATCH. The Australian sale has no effect on US used supply: the fleet stays in Australia on its own $226M ABS (1.8% of Hertz vehicle debt). A US fleet dump needs an HVF III amortization event or Ch.11, and the platform priced $834.75M of notes on 8/27. Watch row ~12/1 (the $200M notes and HVF III 2021-2 $2.0B both mature 12/2026). No 8-K on the sale (EDGAR 10/4).
GAPS: Australian sale and "50s" marks unverified (no filing; sell-side processes precede 8-Ks). Q3 10-Q date unverified. 10/1 rows not swept and -021/-022 unread (bounded spawn). No independent read.
WILL_NEEDS: None.
FOLLOW-UP: PROME may resolve DOCKET 2026-10-09 (OTTO) on ab12815c6. LIQUID may want the 10/1 Knighthead board 8-K (memo §Incidental). OTTO's next session owes the 10/1 cluster plus -021/-022.
