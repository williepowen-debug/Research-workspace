# Q1: what would hurt the book most from here? Exposure map under four scenarios
**TERRY · 2026-09-25 Fri, written 03:03 ET (`date`) · DOCKET L477 · Will-directed (02:55 ET) via PROME packet `c29e4ca60`**
**$0 moved. NO PROPOSAL. No gate moved or shaved. No new threshold.** A management change would go on a card for Will (root rule #5), never in this memo.

## Answer first
1. **The scenario that hurts most is (b): oil falls AND yields fall.** In the measured window, that is also the most common kind of oil-down day: **39 of 56 oil-down sessions (70%)**.
   - On those days, every directional line in the book loses together: USO, the held VLO share, TBT, both TLT puts, and all four credit-put lines.
   - The only offsets are the two lines that are not part of the thesis: GLD and AAPL.
2. **§9 claim: the book is one "Mideast stays hot" bet with a single shared falsifier.** ⚠️ **SEARCH-NOT-FOUND:** I cannot find where this desk wrote that sentence. I searched TERRY's surfaces, PROME's inbox and processed folders, and the reports. The nearest artifact of mine is the 9/11 ⑦ grouping (`archive/STATUS_ARCHIVE_2026-09-14b.md`), which found **three** separate falsifiers: regional-bank credit, private credit and duration. The map below tests the claim as PROME quoted it. **The verdict is split:**
   - ✅ **ACCEPTED by Will 2026-09-25 14:16 ET, WQ-297 A** (verbatim *"297 - A"*; record `PROME/proposals/2026-09-25_wq297-298-RULED.md`). The concentration is accepted in writing. There is no offset card (option B was not chosen), no trim (root rule #7), and no line's rule changes.
   - **CONFIRMED for the directional sleeve** (USO · VLO held · TBT · TLT 77P/82P · KRE ×3 lines · WAL · HBAN · APO). Measured co-movement puts all of them on one side of one falsifier: *oil falls and takes yields down with it*, which is scenario (b).
   - **REFUTED for the book as a whole, by dollars.** GLD ($6,659) and AAPL ($3,359) are **$10,018 of the ~$18.5k marked book** (stocks $17,042 + options ~$1,460 at the 9/24 basis) and gain in (b). Treat them as an offset that exists **only while those lines are held.** WQ-274 applies: GLD's +1 share and AAPL's −5 shares carry no date and no price.
   - **REFUTED for the rates leg's current driver.** The 9/23 move was led by real yields (SIG-W-20260924-009: DFII10 +13bp, with breakevens not leading). In scenario (a), oil down with yields up, the duration shorts **gain** while USO loses. So the rates leg has a second driver that does not depend on the Mideast. The same holds for the held VLO share in (a): refiners rose +0.74% on an average (a) day.
3. **In dollars, the book's scenario P/L comes from the long-stock sleeve.** Stock lines are $17,042 and option lines about $1,460 at the 9/24 close. In the worst measured episode that looks like (b), the 5 sessions to 2026-05-27, the stock lines alone would have lost about **$800**. Nearly all of that is USO (−14.34% ⇒ −$812). AAPL (+$133) offset part of it.

## Basis (every figure dated)
- **Positions:** from the `FORGE/STATUS.md` mirror, which has three vintages.
  - Standing quantities and totals come from the **9/16 13:57 ET visual capture**: AAPL 10 · TBT 10 · GLD 17 · USO 37. These are standing values only and are not transaction-reconciled (D-56, WQ-274).
  - The VLO share is the **9/18 receipt** (account and time UNKNOWN, D-55).
  - Fidelity option quantities come from the **9/10 CLOSE** view. Robinhood lines come from the 9/10 16:10 card. WAL 70P and KRE 25P were also seen beside the 9/16 capture (D-57 note).
  - Fidelity cash was **$22,192.87 (55.79%)** at the 9/16 capture.
- **Prices:** `FORGE/tools/market-data/fetch.py` run 02:59 ET 9/25. Every equity is the **9/24 close** (markets were shut). Futures are overnight 9/25 quotes and are not used for grading.
- **Option values:** the live chain was DEAD (0.00/0.00) on every held strike at 03:00 ET, which is normal overnight. **No mark was fabricated.** Values below use the contract's **last trade** (yfinance `lastPrice`, with the trade time shown) × quantity × 100. Two exceptions: 004 and ROLL70 use this desk's **9/24 13:51 ET two-sided quote**. A last trade is a stale reference, not a mark.
- **Co-movement:** daily returns over **120 sessions, 2026-04-01 → 2026-09-24** (yfinance adjusted closes). Scenarios are mapped to sign-quadrants of daily returns. No level and no threshold was chosen.
  - (a) USO↓ & TLT↓ (yields up), n=17
  - (b) USO↓ & TLT↑ (yields down), n=39
  - (c) USO↑ & HYG↓ (credit widening), n=40
  - (d) quiet: |USO| and |TLT| both below their own median, n=38
  - ⚠️ These are **means of single days in a war-regime window**, not forecasts of multi-day scenarios. The quadrants are small samples and they overlap. Raw output is in the session scratchpad; the recipe can be re-run from this paragraph.

### Measured co-movement (120 sessions)
| corr with | TBT | TLT | HYG | KRE | WAL | HBAN | APO | VLO | GLD | AAPL | APD |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **USO** | +0.53 | −0.55 | −0.52 | −0.39 | −0.36 | −0.34 | −0.32 | +0.51 | −0.32 | −0.24 | +0.03 |
| **TLT** | −0.99 | 1 | +0.71 | +0.27 | +0.38 | +0.28 | +0.27 | −0.28 | +0.29 | +0.22 | −0.17 |

**Reading:** in this window, oil up has meant yields up and credit down. **That one factor is why the shorts and USO have paid together, and it is the same factor that makes them lose together.**

## The map: one row per held line (14) + the 2 staged VLO shares
Scenario cells show the underlying's **mean move on that quadrant's days** and **what it does to the line**: ▲ gains · ▼ loses · ≈ roughly flat or decay.

| # | line (mirror vintage) | value 9/24 (basis) | (a) oil↓ real yields↑ | (b) oil↓ yields↓ | (c) credit broadens, oil↑ | (d) quiet thru 9/30 | EXISTING management rule (card · rule) | needs WQ-274? |
|---|---|---:|---|---|---|---|---|---|
| 1 | **USO 37 sh** [9/16 capture, control cell matched] | $5,664 (153.09c) | ▼ −1.55% ⇒ −$88/day | ▼ **−3.21% ⇒ −$182/day** | ▲ +3.50% ⇒ +$198/day | ≈ +0.04% | **NONE.** `TRY-EXIT-USO35` PARKED; WQ-200 DECLINED 9/10, so Will manages by hand. Standing rule: `$500`/card cap (the cap governs cards; this line has none) | **N** for direction and size (the 9/16 cell matched) |
| 2 | **VLO 1 sh held** [9/18 receipt] | $383 (382.86c; −$29.14 vs $412) | ▲ +0.74% (the crack widens when crude falls) | ▼ −0.97% | ▲ +1.27% | ≈ +0.61% | **NONE on the held share** (card `BRENT_refiner-distillate-strong-leg_2026-08-27.md` § ⑦) | **Y for account only** (D-55). N for direction |
| 2s | **VLO 2 sh STAGED** | $0 held | would-add read: see Q5 | — | — | — | **`GATE-TERRY-VLO-SCALE`** (WQ-282): (A gate day OR B ≤20-SMA) AND NOT F1. F1 = matched Nov `HOX26×42−CLX26` at settlement `<$95` ⇒ stand-down/terminal. review_by 10/14 | N |
| 3 | **TBT 10 sh** [9/16 capture] | $408 (40.75c) | ▲ +0.71% | ▼ −0.96% | ▲ +1.04% | ≈ +0.04% | **NONE.** `FORGE/position_management.tsv`: "no inherited TLT77P rule", review date **not registered** | **Y for size** (−4 sh undated fill, D-56). N for direction |
| 4 | **TLT Sep-30 77P ×20 (004)** [9/10 CLOSE + activity] | $20–40 (0.01/0.02 at 13:51 9/24; last 0.04 at 15:57) vs basis $231.26 | ▲ TLT −0.33%/day; needs **−3.05% in 4 sessions** to reach the strike | ▼ | ▲ TLT −0.51%/day | ▼ **expires worthless 9/30**, losing ≤$40 | **`TRY-FIRE-004`**: HOLD to 9/30 expiry (WQ-168 ④, WQ-217) · harvest 10 ct at ≥`$0.3469` fees-in (PB-0002b) · **NO ADD (WQ-280)** · `GATE-TERRY-007` RESOLVED MOOT 9/24 · roll REFUSED 9/22 (root rule #7 was considered and not triggered) | N |
| 5 | **TLT Oct-16 82P ×2** [9/10 CLOSE] | ~$630 (last 3.15 at 16:12 9/24; ITM by $2.58 ⇒ intrinsic $516); cost $336 | ▲ | ▼ ITM put, high delta: **the largest option loser in (b)** | ▲ | ≈ theta | **NONE.** No card, review date not registered (`position_management.tsv`) | **Y for size** (9/10 view only) |
| 6 | **KRE Dec-18 60P ×5** (2+3 lots) [9/10 CLOSE] | ~$210 (last 0.42 at 14:44 9/24; 15.4% OTM); cost $1,393 | ▼ KRE +0.29% | ▼ KRE +0.50% | ▲ KRE −0.61% | ▼ KRE +0.29% + decay | **NONE on file.** No TERRY card, no mirror ruling | **Y for size** |
| 7 | **KRE Sep-30 60P ×2** [9/10 CLOSE] | ~$0 (last 0.05 on **9/9**; 15.4% OTM, 4 sessions) | ▼ | ▼ | ≈ (too far OTM) | ▼ **expires worthless 9/30** | **WQ-168 ⑥ LAPSE**: rides to $0 | N |
| 8 | **KRE Jan-15-2027 25P ×1 (RH)** [9/10 card; seen 9/16] | ~$5 (last 0.05 on **7/28**; 65% OTM) | ≈ | ≈ | ≈ | ≈ | **NONE.** Lottery; entry never recorded (D-54) | N |
| 9 | **WAL Dec-18 70P ×1 (RH)** [9/10 card; seen 9/16] | $250–270 (2.50/2.70 at 13:51 9/24); cost $220 | ≈ WAL +0.01% | ▼ WAL +0.66% | ▲ WAL −0.95% | ▼ WAL +0.57% + decay | **`TRY-WAL-ROLL70`**: `GATE-TERRY-ROLL70-EXIT` WAL official close ≥$81.90 ×3 ⇒ exit proposal (REGINALD grades; 0-of-3 through 9/23; WAL $76.26 9/24c) · time stop **Fri 12/4** · $4.40 GTC permanently UNKNOWN (WQ-167) | N |
| 10 | **HBAN Oct-16 16P ×2** [9/10 CLOSE] | ~$200 (last 1.00 at 15:58 9/24; **ITM by $0.69** ⇒ intrinsic $138); cost $192 | ▼ HBAN +0.39% | ▼ HBAN +0.53% | ▲ HBAN −0.89% | ▼ | **"HBAN stub" RETIRED 7/18**: EXIT-THESIS dust, rides to expiry, do not pay to close (Will) | **Y for size** |
| 11 | **APO Dec-18 95P ×1** [9/10 CLOSE] | ~$125 (last 1.25 at 12:59 9/24; 21% OTM); cost $1,185 | ▼ APO +0.68% | ▼ APO +0.67% | ▲ APO −1.04% | ▼ APO +0.44% | **NONE.** "No ruling on file" (mirror); BROCK thesis vehicle | **Y for size** |
| 12 | **GLD 17 sh** [9/16 capture] | $6,659 (391.69c) | ▼ −0.15% ⇒ −$10/day | ▲ **+0.36% ⇒ +$24/day (OFFSET)** | ▼ **−0.78% ⇒ −$52/day** | ≈ +0.16% | **NONE.** No card; MIDAS domain | **Y. This line carries the verdict's offset** (+1 sh undated, D-56) |
| 13 | **AAPL 10 sh** [9/16 capture] | $3,359 (335.92c) | ▲ +0.38% | ▲ **+0.70% ⇒ +$24/day (OFFSET)** | ≈ −0.04% | ▲ +0.44% | **NONE** | **Y for size** (−5 sh undated, D-56) |
| 14 | **APD 2 sh** [9/10 CLOSE] | $569 (284.49c) | ▲ +1.06% | ≈ −0.24% | ≈ −0.13% | ≈ | **NONE.** Thesis tag unassigned since 7/30 | N |

**Stock-sleeve net per average quadrant day** (value × the quadrant's mean move; lines 1, 2, 3, 12, 13, 14): **(a) −$74 · (b) −$143 · (c) +$153 · (d) +$30.** In (b) every option line also loses, so the book is worse than −$143 on an average (b) day.

### Realized episodes (5-session windows inside the same 120 sessions, measured, not scenarios)
| episode (window end) | USO | VLO | TBT | TLT | KRE | WAL | HBAN | APO | GLD | AAPL | resembles |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| best TLT rise, **5/27** | −14.34% | −8.05% | −5.04% | +2.75% | +2.99% | +3.04% | +3.69% | −0.67% | −0.73% | +3.97% | **(b): everything directional loses; APO the only credit exception** |
| worst USO fall, **6/17** | −14.94% | −7.06% | −3.39% | +1.71% | −0.68% | −3.85% | +0.96% | +5.92% | +3.74% | +1.50% | (b) with credit **mixed**: WAL fell and APO rose |
| worst HYG fall, **9/15** | +10.84% | +3.71% | +3.72% | −1.81% | −0.35% | −1.14% | −0.06% | −3.65% | −1.39% | +4.78% | (c): the book's best case |

## What loses together, what offsets
- **Lose together, (b):** USO · VLO held · TBT · TLT 82P · TLT 77P · KRE Dec 60P · WAL 70P · HBAN 16P · APO 95P. This is the single shared falsifier: *oil falls and yields and credit follow it down*.
- **Offsets in (b):** GLD and AAPL only. **Neither is part of the thesis, neither has a card, and both carry undated quantity changes (D-56).**
- **(a) splits the book:** USO loses. The rates shorts and the VLO share **gain**. The credit puts decay slightly. **This is the regime of 9/23**, when real yields led. It is why the rates leg is not purely a Mideast bet.
- **(c) is the book's best case:** every short and USO gain together. GLD is the main loser at −$52 per average day.
- **(d) quiet through 9/30:** two lines die on the clock, 004 TLT 77P ×20 (≤$40 left) and KRE Sep-30 60P ×2 (~$0). The credit puts decay while their underlyings drift up (+0.3% to +0.6% per quiet day). The stock sleeve is roughly flat to +$30 per day. **Quiet costs little in dollars because most of the premium is already gone:** the 9/11 ⑦ measurement had long premium at `$5,306.67 → $682.00` (−87.1%).

## Two facts for a card (NOT proposed here; each would be a card for Will)
1. **Two "dust/no-rule" puts are now IN THE MONEY:** HBAN 16P (ITM $0.69, rule written 7/18 for an OTM stub) and TLT 82P (ITM $2.58, no rule at all). Both expire **Oct-16**.
   - An ITM long put held to expiry in an IRA **with no shares to deliver** raises a mechanics question the 7/18 "ride to expiry" ruling did not consider: the broker may exercise, may close the position, or may deliver nothing. The answer is broker-specific and **UNKNOWN to this desk.**
   - Flagged, not proposed.
2. **Of 14 held lines, 10 have NO management rule:** USO · VLO held · TBT · TLT 82P · KRE Dec · KRE Jan · APO · GLD · AAPL · APD. **Those rule-less lines hold ~$18.0k of the ~$18.5k marked value.**
   - The lines with a rule are 004 · KRE Sep-30 · WAL ROLL70 · HBAN, plus the staged VLO.
   - ⇒ **In scenario (b), the book's largest loss would come from lines that no rule governs.** This is a fact about coverage, not a recommendation to add rules near today's levels.

## Needs the broker reconciliation (WQ-274) before it can be trusted
- **Direction conclusions: NO.** Every ▲/▼ holds as long as the line exists with quantity > 0.
- **Dollar sizes: YES** for AAPL · GLD · TBT (D-56 undated fills) · every Fidelity option line (quantity from the 9/10 view, and Will trades by hand) · VLO's account (D-55).
- **The verdict's OFFSET half depends on GLD 17 and AAPL 10 still being held.** If either was sold since 9/16, the book becomes *more* purely the single bet, not less.
- **USO 37 is the one line that the 9/16 capture confirmed.**
- **PROME's mirror-derived rows:** not received at the time of writing. This map was built independently from the same mirror, and PROME said it would send them within the hour. Reconcile on receipt; any disagreement would be a count or vintage difference. My count: 14 held lines, matching PROME's `2026-09-25_domain-state-report.md` line 59 list.

---
**APPROVAL REQUIRED — none; no trade is proposed.** `$0` moved · no order · no gate moved or shaved · no new threshold. — TERRY

## Reconciliation with PROME's mirror rows (`PROME/reports/2026-09-25_Q1-exposure-map-mirror-rows.md`, `fb9a9299a`) · 2026-09-25 03:07 ET (`date`)
**Line set:** the same 14 held lines + the staged VLO. **No count disagreement.** Where the two maps differ on direction, the cell below is settled on the measured 120-session quadrant means above, not on reasoning.

| # | PROME's read | TERRY verdict | evidence |
|---|---|---|---|
| R1 | Option quantities tagged `[9/16]`; 004 "is the one cell the 9/16 capture corrected" | **REFUTE (vintage).** The 9/16 capture corrected six cells: AAPL · TBT · GLD · cash · Fidelity total · RH total. **Every Fidelity option quantity is the 9/10 CLOSE view.** 004's 25→20 is the **9/10 activity** row (D-50), not the 9/16 capture | `FORGE/STATUS.md` header lines 6, 12, 24 and the 004 row |
| R2 | (a): USO and GLD are "the two largest lines [and they] lose together"; the duration shorts "gain little"; AAPL "loses mildly" | **PARTLY CONFIRM.** Agree that (a) is not one bet. **But GLD's loss in (a) is small (−0.15%/day ⇒ −$10) and the offsets are not marginal:** TBT +0.71%, TLT 82P ITM gains (TLT −0.33%/day), VLO +0.74%, AAPL **+0.38%** (it gains), APD +1.06%. USO −$88/day is nearly all of the stock-sleeve −$74/day. **(a) is "USO alone loses", not "USO + GLD".** 004's one-cent bid is right but irrelevant: the duration exposure that matters is the ITM 82P (~$630) plus TBT | quadrant (a) n=17 |
| R3 | (b): the genuine single-shared-falsifier case; everything except GLD and AAPL loses | **CONFIRM, with one correction.** HBAN 16P is not "~0/dust": it is **ITM $0.69 (~$200 at the 15:58 9/24 last trade)**, so it loses in (b) (HBAN +0.53%/day) | quadrant (b) n=39; 5/27 episode |
| R4 | (c): "the book's only diversifying scenario"; GLD gains (flight to safety); TBT mixed; AAPL loses | **REFUTE.** In the measured window, (c) is **the same factor in reverse, i.e. the book's best case**: USO +3.50%, TBT +1.04%, TLT −0.51% (puts gain), and every credit put gains. **GLD LOSES (−0.78%/day ⇒ −$52, the main loser)**; AAPL is flat (−0.04%). Diversification would need a line that pays when the thesis fails. **In (c) the thesis pays in full.** Worst-HYG episode 9/15: USO +10.84%, TBT +3.72%, GLD −1.39% | quadrant (c) n=40; 9/15 episode |
| R5 | KRE Dec-18 60P "gain if real ↑" in (a); needs reconcile N | **REFUTE on direction, and Y for size.** KRE +0.29%/day in (a) ⇒ the put decays slightly. The quantity is 9/10-view (R1) | quadrant (a) |
| R6 | §9 sleeve totals kill-on-sight until a broker mark | **CONFIRM the principle.** This map's $ figures are 9/24 closes (or last trades, timed) × mirror quantities. That is a **screening** size, not a mark of record, and WQ-274 applies to every one. No figure here was taken from a 9/10 mark | basis § above |

**Net §9 verdict: unchanged.** ✅ *ACCEPTED by Will 2026-09-25 14:16 ET, WQ-297 A (no offset card, no trim).* A single shared falsifier exists (scenario b) for the directional sleeve. It is refuted for the whole book by GLD + AAPL, and for the rates leg by its real-yield driver. **PROME's "(c) diversifies" is the one reading that would change a decision if left standing:** the book has **no** scenario in which the thesis fails and something other than GLD/AAPL pays.
