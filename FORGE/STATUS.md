# FORGE — Trading Operations

Dashboard management mapping → [position_management.tsv](position_management.tsv); maintenance contract → [dashboard notes](DASHBOARD.md). Holdings remain in this file; approval, order and fill evidence are separate. A changed evidence source invalidates its management mapping until reviewed.

> ✅ **2026-10-15 (Thu) — RECONCILE BY ANVIL to Will's Fidelity positions view + Activity & Orders (Pending + Past 30 days) received Thursday 10/15 10:10 ET. Marks are 10/15 INTRADAY at an UNKNOWN clock (after the three 10/15 fills; not certified live, not closes).** Source `PROME/data/2026-10-15_broker-capture-TRANSCRIPTION.md`; account continuity INFERRED from matching holdings, not independently verified. All **17/17** rows value = last × qty × multiplier and value − basis = G/L; positions **$18,415.11** + cash **$18,155.75** + pending **+$923.68** = **$37,494.54 to the cent** (ANVIL re-verified). Vs the 10/14 mirror (`c5a1d40fa`): **2 NEW** (QQQ Oct-16 735C ×1 · QQQ Oct-15 715P ×1 — expires TODAY), **2 CLOSED** (QQQ Oct-15 740P ×3 · USO Oct-14 150C ×2, both sold to close 10/14, broker-verified), **3 QTY CHANGE** (AAPL 5→4 broker-verified · GLD 17→20 and HBAN Oct-16 16P 2→1 — fills NOT in the visible ledger, bases DERIVED), **1 ROUND TRIP not held** (QQQ Oct-16 725P: sold close 10/15, opening buy unseen), **10 MARK ONLY**.
>
> ⚠️ **ACCOUNT SCOPE — Fidelity: ONE Traditional IRA; account id redacted, identity not independently verified. Robinhood Individual NOT provided — carried 9/29 rows unverified today; absence establishes no closure. The Past-30-days Activity view is CUT OFF below the 10/14 QQQ 735C buy — anything older or posted between the 10/14 capture and that row is UNSEEN.**
>
> **Updated:** 2026-10-15 = receipt date (10:10 ET) · marks = UNKNOWN clock, 10/15 intraday (all Fidelity cells `[10/15 rcv]` = `[broker export received 2026-10-15 10:10 ET; capture time UNKNOWN]`) · **Fidelity cash (money market):** $18,155.75 (48.42%) + **Pending activity +$923.68** · **Fidelity account total:** $37,494.54 (Today −$616.48 / −1.62%; open G/L −$390.05 / −2.07%). Vs the 10/14 mirror $36,432.23: **+$1,062.31 = positions −$2,498.40 + cash +$4,128.67 + pending −$567.96**; snapshot change, not daily/realized P&L. Pending exactly equals today's three Processing rows **+$347.02 (AAPL) + $769.32 (QQQ 725P close) − $192.66 (QQQ 715P open)**; already inside the total, never add again. Cash+pending **$19,079.43** is not verified settled cash/buying power. Cash $18,155.75 equals the last balance in the Activity cash-balance column (10/14 postings), which the column reproduces to the cent bottom-to-top from $12,428.50; the 10/14 mirror's cash $14,027.08 matches NO balance in that column (D-81). **DERIVED realized this pass (never broker-reported): QQQ 740P ×3 +$1,882.94 (cohort +$2,022.60 incl. the +$139.66 already booked) · USO 150C ×2 +$385.35 · AAPL 1 sh +$323.38; QQQ 725P round trip UNKNOWN (open leg unseen); HBAN −1 UNKNOWN.** **Robinhood:** $295.15 / BP $8.94 `[9/29 13:4x intraday]`, not re-captured (16 days). Rotations → `_archive/STATUS_ROTATION_2026-10-15.md` (10/14 table, terminal records, 10/14 actions) and earlier.

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (its own header names the current base and amendment count). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*Quoted cells `[10/15 rcv]` (received 2026-10-15 10:10 ET, capture/mark time UNKNOWN, intraday). All six stock quantities/bases directly read; the GLD and AAPL changes are explained in their rows. Rounded average costs and percentages are preserved as displayed, not exact fills. Settled fill notes → rotation 10/01 chunk B.*

| Ticker | Type | Qty | Cost | Mark 10/15 rcv | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | 4 | $23.65 | $345.08 | $1,380.32 | +$1,285.74 / +1,359.42% | Today +$8.48; exact basis $94.58. **QTY CHANGE 5→4 — SOLD 1 at market 10/15, FILLED $347.02 (Pending/Processing), broker-verified; fill time UNKNOWN.** Removed basis $118.22 − $94.58 = $23.64 ⇒ DERIVED realized +$323.38, assuming no unseen basis adjustment; not broker-reported realized P&L (D-76). Prior sales 10/13 (net $1,707.54, conditional +$1,589.31), 9/15 (≈+$1,534.92) and pre-7/30 (D-1) remain historical |
| GLD | Stock | 20 | $374.66 | $380.3649 | $7,607.29 | +$114.19 / +1.52% | Today +$87.49; exact basis $7,493.10 (value 380.3649 × 20 = 7,607.298 displays as 7,607.29). **QTY CHANGE 17→20 — the buy is NOT in the visible Activity (below the fold or between the 10/14 capture and the ledger's cut); added basis $7,493.10 − $6,370.50 = $1,122.60 ⇒ 3 sh @ $374.20 DERIVED; gross fill/time/initiator UNKNOWN (D-80).** MIDAS domain; largest line by this capture's value |
| USO | Stock | 37 | $122.28 | $155.089 | $5,738.29 | +$1,214.02 / +26.83% | Today +$56.57; exact basis $4,524.27; last × 37 = 5,738.293 ties as displayed (D-79 historical). **WQ-200 DECLINED by Will 9/10 — NO harvest/give-back rule live; Will manages by hand.** BRENT thesis (Hormuz-gap entry) |
| VLO | Stock | 2 | $426.00 | $450.69 | $901.38 | +$49.38 / +5.79% | Today −$18.18; MARK ONLY; exact basis $852.00. **Prior10/13 QTY CHANGE 1→2**; Activity confirms10/12 buy net$440; added1share is derived from quantity bridge, individual gross fill/time absent (D-76). Authorization/management scope remain UNKNOWN (D-78). Original share bought 9/18 @ $412.00 (fill TIME not shown — D-55). **Historical Will confirmation 2026-10-07: “Yes, still one share”; superseded on quantity only by this two-share view.** WQ-213 originally 1 of 3; **its remaining 2-sh scale instruction was STAND DOWN** under `PROME/GATES.tsv` GATE-TERRY-VLO-SCALE, TERMINAL on the 9/25 F1 fire (TERRY 4ad672c43; its optional CME source-① override remains as written there). **The additional share does not autoapprove the terminal scale rule or establish extension of the original management scope. The originally held share's exit rule is `GATE-TERRY-VLO-HELD-01` — the letter (condition AND consequence cells, incl. who acts on each leg) is read at `PROME/GATES.tsv`, as amended by WQ-386 (`PROME/proposals/2026-10-07_VLO-december-management-RULED.md`, approved 10/7); nothing of it is restated here.** The gate reads the crack and the text, not the share's mark. The prior note, which restated the letter, is verbatim in rotation 10/08 chunk H |
| APD | Stock | 2 | $294.79 | $295.015 | $590.03 | +$0.46 / +0.07% | Today +$4.97; exact basis $589.57; MARK ONLY. Historical 10/1 "D" badge / $1.81 reference-price adjustment remains unverified; no dividend row in any Activity view since. Thesis tag unassigned since 7/30 |
| TBT | Stock | 5 | $34.40 | $39.56 | $197.80 | +$25.79 / +14.99% | Today −$8.15; exact basis $172.01; MARK ONLY. Prior 10/12 sale 5 (net $210.40, DERIVED +$35.95; D-76) historical. Duration-short leg (BOND/TERRY). **WQ-357 LATER 10/3 selected path C while BOND researches; the Wed 10/14 decision clock for the surviving 5 has PASSED — outcome not in this capture, no order inferred.** |

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

*No live event-box rows — the VIX $20C/$25C spread (CLOSED 2026-07-30, realized −$111.60) and the five Aug-21-2026 EXPIRED rows (realized −$2,816.72 total) are terminal → rotation records.*

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, owned by no agent unless separately recorded. **SELL-OR-ROLL before expiry** (`USER.md`, 9/30 19:03 ET); TERRY recommends, Will orders. The capture establishes holdings/fills, not contract-specific cards or approvals; grouping is navigation, not a thesis or scope ruling. Last marks are not executable bids; working orders UNKNOWN. Receipt-day DTE is scheduling only; broker capture time UNKNOWN.

| Ticker | Strike | Expiry | Qty | Cost | Mark 10/15 rcv | Value | P&L | Note |
|--------|--------|--------|-----|------|---------------|-------|-----|------|
| QQQ | $715P | Oct-15-2026 | 1 | $1.93 | $0.93 | $93.00 | −$99.66 / −51.73% | `[10/15 rcv]`; **NEW — BOUGHT OPEN 10/15 limit $2.05 Day, FILLED @$1.92, net −$192.66 (Processing); exact basis $192.66; broker-verified, fill time UNKNOWN.** Today −$99.66 is measured from the fill (the displayed last-chg +$0.34 is vs the prior session's mark; cell copied as displayed). **⛔ EXPIRES TODAY Thu 10/15 — 0 calendar DTE — SELL-OR-ROLL before the close** (`USER.md` 9/30 19:03 ET); no card, no mapping row, no desk owner recorded (D-77). Moneyness NOT in the view (no QQQ quote); the transcription's ~10:04 ET vendor read is PROME's INFERRED context, not a broker mark. If exercised: sell 100 QQQ at $715 ($71,500), mechanics only — D-60 |
| QQQ | $735C | Oct-16-2026 | 1 | $2.53 | $0.46 | $46.00 | −$206.66 / −81.80% | `[10/15 rcv]`; **NEW — BOUGHT OPEN 10/14, net −$252.66 (Activity, broker-verified); exact basis $252.66; gross fill/time UNKNOWN.** A CALL opened on a red QQQ day — root rule #6 is TERRY's construction rule and no card exists; Will-direct, nothing inferred. Today −$164.00. **Fri 10/16 expiry TOMORROW, 1 calendar DTE — SELL-OR-ROLL.** If exercised: buy 100 QQQ at $735 ($73,500), mechanics only — D-60. Ownership/card UNKNOWN (D-77) |
| CMG | $28P | Oct-30-2026 | 2 | $0.55 | $0.29 | $58.00 | −$51.33 / −46.95% | `[10/15 rcv]`; MARK ONLY; basis $109.33; Today −$36.00. 15 calendar DTE. 10/14 sell-1 limit $0.46 Day **VERIFIED CANCELED** (Pending block) — not a fill; 2 still held; any replacement order UNKNOWN. BOUGHT OPEN 10/12 net −$109.33; gross fill/time, thesis/desk ownership and contract-specific management approval UNKNOWN (D-76/D-77) |

*QQQ Oct-15 740P ×3 **SOLD CLOSE 10/14** — three Activity rows net +$1,220.31 / +$1,155.31 / +$1,099.31 = $3,474.93 − remaining basis $1,591.99 ⇒ DERIVED realized +$1,882.94. Cohort: bought 4 10/2 net −$2,122.65; all proceeds $670.32 + $3,474.93 = $4,145.25 ⇒ +$2,022.60, of which +$139.66 (the first sale) was already on the 10/14 mirror — never add the partial and the cohort together. Gross fills DERIVED from the ~$0.69/contract fee pattern ≈ $12.21 / $11.56 / $11.00 (the first, $6.71, is broker-stated); times UNKNOWN (D-66). ⛔ No contract remained for today's expiry — `MGMT-QQQ740P-OCT15` SPENT; no exercise/assignment outcome. These proceeds posted to the cash-balance column on 10/14, not to pending.*

*USO Oct-14 150C ×2 **SOLD CLOSE 10/14** — two Activity rows net +$354.34 + $406.34 = $760.68 − basis $375.33 ⇒ DERIVED realized +$385.35 (gross ≈ $3.55 / $4.07 DERIVED; times UNKNOWN). Will's 10/14 word "i sold before close" is now broker-CONFIRMED. Expiry task retired; no exercise outcome. Distinct from the 37 shares and the closed Oct-09 call; no roll linkage inferred.*

*QQQ Oct-16 725P ×1 — **ROUND TRIP, NOT HELD**: SOLD CLOSE 10/15 limit $7.51 Day, FILLED @$7.70, net +$769.32 (Processing; inside pending $923.68). The OPENING BUY is NOT in the visible Activity and the contract was NOT in the 10/14 holdings ⇒ bought between the 10/14 capture and the 10/15 sale; basis and realized UNKNOWN (D-80). Proceeds already in the account total; never add again. Initiator/card UNKNOWN.*

*Older terminal records (QQQ 744P +$545.66 · 755C −$144.66 · 745P +$109.68 · 750C −$134.35 · the Oct-09 cohort) verbatim → `_archive/STATUS_ROTATION_2026-10-15.md` chunk B; none re-bookable.*

## Fidelity — Thesis Puts

*Instrument grouping is navigation, not approval: the Fidelity WAL/OZK rows below are Will-direct holdings (bought 10/7, Activity); thesis/desk ownership and management approval are NOT established by the broker view.*

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

*TLT $77P Sep-30 ×15 (TRY-FIRE-004's last lot): SOLD TO CLOSE 9/30 ⇒ −$154.64; no replacement TLT line; detail → rotation 10/01 chunk D.*

*TLT Oct-16 $82P remaining1 **SOLD CLOSE10/12** net$400.34−remaining basis$167.67=realized+$232.67. Prior9/28 partial1-of-2 sale@$3.60⇒+$191.66 remains separately booked. WQ-357 LATER10/3 pathC and `MGMT-TLT82P-OCT16`/WQ-302 Wed10/14 clock are historical management duties: disposal now evidenced, no current TLT holding asserted; PROME/TERRY integrate decision records. BOND research delivered10/5 (`ff0992bf1`) was not a new trade ruling. Prior2.50× mark multiple never a price trigger. D-60 future ITM handling remains UNKNOWN.*

### KRE — regional banks (REGINALD)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
*All four rows `[10/15 rcv]` (received 2026-10-15 10:10 ET, capture/mark time UNKNOWN); all MARK ONLY; the Nov-27 row does not establish ownership/management approval. KRE $60P Sep-30 ×2 sold 9/30 @ $0.01 ⇒ −$451.48 (leg 1 of the roll into the Dec-31 65P; detail + the D-67 mark note → rotation 10/01 chunk D). Rail on the 65P: *"hard stop Thu 12/31 15:00 ET"* (`MGMT-KRE65P-DEC31`, `5ce609f80`).*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $67P | Nov-27-2026 | 4 | $1.28 | $1.06 | $424.00 | −$86.65 / −16.97% (today −$84.00). MARK ONLY; basis $510.65; BOUGHT OPEN 10/12 net −$510.65; gross fill/time/card UNKNOWN (D-76/D-77). Grouping under KRE is not desk ownership/approval. 43 calendar DTE from receipt 10/15 |
| $60P | Dec-18-2026 | 2 | $2.57 | $0.50 | $100.00 | −$413.34 / −80.52% (today −$14.00). MARK ONLY; basis $513.34. 64 calendar DTE from receipt 10/15 |
| $60P | Dec-18-2026 | 3 (M) | $2.93 | $0.50 | $150.00 | −$728.02 / −82.92% (today −$21.00) — multi-lot marker; basis $878.02; **five** Dec-18 KRE 60P across two lots. MARK ONLY. 64 calendar DTE from receipt 10/15 |
| $65P | Dec-31-2026 | 2 | $1.69 | $1.42 | $284.00 | −$53.33 / −15.81% (today −$34.00) — MARK ONLY; basis $337.33. Bought 9/30 ×2 @ $1.68 (roll leg 2). Will's own add; `MGMT-KRE65P-DEC31` (`5ce609f80`): hard stop Thu 12/31 15:00 ET, not a price gate. 77 calendar DTE from receipt 10/15 |

### WAL (REGINALD) — Sep-18 pair EXPIRED

*$70P + $67.5P Sep-18 ×1 each: **EXPIRED as of 9/18, broker-confirmed** (ledger rows posted 9/21) ⇒ realized **−$768.67 and −$750.67 = −$1,519.34** (full basis) — the WQ-168 ①② LAPSE as ruled. Rows → rotation record. Duration roll = the Robinhood WAL Dec-18 $70P ×1 below. The RH WAL $77.5P Aug-21 sale: P&L UNRECORDED — D-18.*

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18-2026 | 1 | $11.85 | $1.25 | $125.00 | −$1,059.67 / −89.45% | `[10/15 rcv]`; basis $1,184.67; Today −$45.00. MARK ONLY; BROCK thesis vehicle. Will ruled HOLD 2026-08-13 (`PROME/proposals/2026-08-13_private-credit-batch-RULED.md` §②; vehicle-mismatch flag live). 64 calendar DTE from receipt 10/15 |
| HBAN | $16P | Oct-16-2026 | 1 | $0.96 | $0.60 | $60.00 | −$35.67 / −37.29% | `[10/15 rcv]`; basis $95.67; Today −$30.00. **QTY CHANGE 2→1 — the sale is NOT in the visible Activity; removed basis $191.34 − $95.67 = $95.67; proceeds, time and realized UNKNOWN (D-80).** **Fri 10/16 expiry TOMORROW, 1 calendar DTE — SELL-OR-ROLL for the remaining 1.** `MGMT-HBAN16P-OCT16` / WQ-302 re-rule was due Wed 10/14 — its outcome is not in this capture; the one-contract sale is not evidence of a ruling. Moneyness not verified (no underlying quote in the view); badge NE |
| OZK | $40P | Nov-20-2026 | 4 | $0.81 | $0.30 | $120.00 | −$202.65 / −62.81% | `[10/15 rcv]`; MARK ONLY; basis **$322.65** (10/7 view showed $322.66 — D-75); Today −$60.00. **Bought 10/7, −$322.65 (Activity); Will-direct.** PROME-supplied context (not broker): WQ-428 = Will's intention to sell ×4 before 10/20 — **no OZK order appears in the Pending block and 4 are still held**; order status UNKNOWN (D-82). Thesis/desk ownership and management approval UNRECORDED (D-74). Badge E (earnings — INFERRED). 36 calendar DTE from receipt 10/15 |
| WAL | $65P | Dec-18-2026 | 4 | $1.71 | $1.35 | $540.00 | −$142.65 / −20.90% | `[10/15 rcv]`; MARK ONLY; basis $682.65; Today −$160.00. **Bought 10/7, −$682.65 (Activity); Will-direct.** PROME-supplied context (not broker): WQ-429 = Will's intention to sell ×4 before 10/19 — **no WAL order appears in the Pending block and 4 are still held**; order status UNKNOWN (D-82). Thesis/desk ownership and management approval UNRECORDED (D-74). Distinct from Robinhood WAL Dec-18 $70P ×1. Badge E (earnings — INFERRED). 64 calendar DTE from receipt 10/15 |


## Robinhood — satellite account (Individual)

*All holdings/figures below retained from the 9/29 source; carried DTE annotations are historical, not a current freshness assertion.*

> ⚠️ **NOT CAPTURED IN THIS 10/15 RECEIPT (nor 10/14, 10/13, 10/11, 10/7, 10/1 or 9/30 — 16 days since the 9/29 card) — every cell below is the 9/29 card, unverified today.** 9/29 card: **account $295.15, BP $8.94** `[9/29 13:4x intraday]`; lines + BP = $290.15 ⇒ **$5.00 UNEXPLAINED (D-64)**. Per-line cost/value DERIVED from P/L ÷ P/L% (no Mark column ⇒ machine class `unverified` by design). The prediction-market line and the 9/01→9/25 dead-by-date bookings — USO $159C Sep-11 (bought 9/10, expired $0 — D-58) · QQQ $713C Sep-16 + USO $165C Sep-16 (both expired $0 — D-57) — verbatim → rotation 10/08 chunk B.

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **WAL $70P** | **Dec-18-2026** | 1 | **$2.20 ($220)** — bought 9/02 @ $2.20 (RH activity) ✓ | ≈$265.00 *(derived; mark ≈$2.65)* | ✅ **ON CARD 9/29 — +$45.00 / +20.45%** | TRY-WAL-ROLL70 (filled in Robinhood). Guard **`GATE-TERRY-ROLL70-EXIT`** *"WAL OFFICIAL CLOSE ≥ $81.90 on THREE CONSECUTIVE sessions"* — **0-of-3 as last recorded here** (REGINALD through 9/23, per TERRY STATUS 9/24; not re-read this pass). The option's +20.45% is not the gate — the gate reads WAL's close (rule 7). **$4.40 GTC sell order: CANCELLED / not there — Will 9/28** (`PROME/inbox/processed/2026-09-28_from-WAL_WQ-324-325-ruled-verbatim-and-4.40-GTC-cancelled.md`) ⇒ **no resting exit order; any take-profit is Will's manual act.** Time stop Fri 12/4. 78 DTE. **D-47** |
| **KRE $25P** | 1/15/2027 | 1 | $53.00 — card-derived ✓ | ≈$1.00 *(derived)* | ✅ **ON CARD 9/29 — −$52.00 / −98.11%** | Deep-OTM lottery; entry pre-7/16, never recorded — **D-54** (before the 9/01 activity view). 106 DTE |
| T | stock | 1 | — | — | ⚠️ no stocks card 9/29; no T row in RH activity 9/01→9/25 | Hypothesis: sold before 9/01, unconfirmed — **D-20**. The card no longer closes to the cent (D-64), so the 9/27 "no stock line" inference is weaker |

## Account UNATTRIBUTED — receipted fills not yet attributed to an account

*No rows. VLO ×1 (this section's only row since 9/19) moved to § Fidelity — Longs on the 9/25 ledger (D-55 account leg CLOSED). The section stays as the landing place for a receipt that names no account (the parser admits it — TERRY `cfd9b9115`).*

---

## ⚠️ Reconcile discrepancies (received 2026-10-15 10:10 ET; capture/mark time UNKNOWN, intraday)

> Broker view > Will's word > desk record; conjectures labeled; nothing resolved by invention. Robinhood not captured. DTE from receipt 10/15 only. **Permanently UNKNOWN by WQ-167 (never asks): 9/2 USO 135C sale price.** Immediately prior section → `_archive/STATUS_ROTATION_2026-10-15.md` chunk A (byte-exact); the 10/11-built section → `…_2026-10-11.md`; carried duty detail → rotation 10/08 chunks D1/D2. Urgency = decision clock, expiring first.

### Will supplies / PROME re-reads — facts owed

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| NEW | QQQ Oct-15 715P ×1 | 🔴 **EXPIRES TODAY Thu 10/15, 0 calendar DTE** | Bought open today @$1.92 net −$192.66; marks $0.93 (−$99.66); no card, no mapping, no owner. SELL-OR-ROLL before the close is the standing rule (`USER.md` 9/30) | Moneyness at capture INFERRED OTM from PROME's own 10:04 ET vendor read (not broker); intent (hedge vs day-trade) UNKNOWN; if it rides to expiry ITM the exercise mechanics are D-60 | **Will** orders; **TERRY** recommends if asked; PROME records |
| DATED | QQQ Oct-16 735C ×1 · HBAN Oct-16 16P ×1 | 🔴 **expire TOMORROW Fri 10/16, 1 calendar DTE** | 735C: value $46 / basis $252.66 (−81.80%), bought 10/14, no card (D-77). HBAN: 1 of 2 remains after an unseen sale (D-80); value $60 / basis $95.67; the Wed 10/14 WQ-302 re-rule outcome is not in this capture | Whether the HBAN sale WAS the re-rule's execution is conjecture; the remaining contract has no recorded instruction. 735C exercise = buy 100 QQQ at $735 ($73,500), mechanics only | **Will** orders; **TERRY** recommends; PROME records |
| **D-60** | Fidelity ITM-expiry handling — never observed | 🔴 next expiries TODAY / TOMORROW | Every prior expiry closed by sale or expired OTM/liquidated; no deterministic LIQUIDATE-vs-EXPIRE policy established. Exposures if held ITM: 715P sell 100 QQQ ($71,500) · 735C buy 100 QQQ ($73,500) · HBAN 16P sell 100 HBAN ($1,600) — mechanics only | Broker auto-liquidation time/threshold, initiator and IRA short-stock handling UNKNOWN; no outcome inferred | **Will** — broker policy |
| **D-80** NEW | Three fills UNSEEN below the ledger's fold + the 725P basis | 🟠 evidence owed before any realized figure is booked | GLD 17→20 (added basis $1,122.60 ⇒ 3 sh @ $374.20 DERIVED) · HBAN 16P 2→1 (removed basis $95.67; proceeds UNKNOWN) · QQQ Oct-16 725P opening buy (sold close 10/15 net +$769.32; basis UNKNOWN ⇒ realized UNKNOWN). All three happened after the 10/14 capture; the Past-30-days view is cut at the 10/14 735C buy | Hypothesis (labeled): they sit in the unseen lower rows of the same view, or posted 10/14 after the capture. Nothing booked for them; derived bases assume no other basis adjustment | **Will** supplies the lower part of the Activity ledger (or the three order confirmations); **PROME** records |
| **D-82** NEW | WQ-428 (OZK 40P ×4 sell before 10/20) · WQ-429 (WAL 65P ×4 sell before 10/19) — Will's orders per PROME, not visible | 🟠 10/19–10/20 clocks | Pending block shows only the three 10/15 fills and the canceled CMG limit; both lines still held ×4 at 10/15 marks ($120 / $540) | Hypothesis (labeled): orders not yet placed, placed after the capture, or placed as GTC in a view not captured. Not a fill; nothing retired | **Will** confirms order state; **PROME** records |
| **D-81** NEW | 10/14 mirror cash $14,027.08 matches no balance in the Activity cash-balance column | 🟡 record | Column reproduces to the cent bottom-to-top $12,428.50 → $18,155.75 across the eight 10/14 postings (= today's cash); the 10/14 cash sits $16.58 above the post-744P balance $14,010.50; that mirror's two pending fills are POSTED here | Hypothesis (labeled): a different cut (settled vs posting) or an unseen +$16.58 item; not reconciled, not invented. Today's cash ties | **PROME** records; **Will** / broker detail if ever needed |
| **D-83** NEW | Capture clock UNKNOWN; Robinhood not captured for 16 days | 🟡 standing | Marks are 10/15 intraday, after the three fills and before 10:10 ET receipt; no fill times in any Fidelity view (D-66). Robinhood at the 9/29 card: $295.15 (D-20 T question open) | RH lines may have moved — nothing inferred | **Will** supplies a Robinhood view when convenient; **PROME** records |
| **D-76** | Detailed fills / lots behind the DERIVED realized figures | 🟡 narrowed again | Broker-verified this pass: AAPL sold 1 @$347.02; QQQ 740P ×3 net proceeds; USO 150C ×2 net proceeds; QQQ 715P/725P/735C fills. DERIVED: AAPL +$323.38, 740P +$1,882.94 (cohort +$2,022.60), USO +$385.35 — none broker-reported realized P&L; gross per-contract prices for the 740P/USO closes derived from the fee pattern | Removed-basis arithmetic assumes no unseen adjustment. Prior 10/12–13 gross-fill gaps and all fill times remain open (D-66) | **Will** supplies lots/fills if wanted; **PROME** records; **TERRY** integrates |
| **D-78** | VLO second share — authorization/management scope | 🟠 scope before action | 2 sh, basis $852; original held-share rule `GATE-TERRY-VLO-HELD-01` (letter at `PROME/GATES.tsv`, WQ-386) unchanged; terminal scale rule unchanged. 10/15 mark $450.69 (−$9.09 today) is not a gate input — the gate reads the crack and the text | Second-share scope UNKNOWN; capture extends nothing | **Will** authorization; **PROME / TERRY** scope |
| **D-70** | Management mappings follow-through (`position_management.tsv` UNTOUCHED this pass) | 🟡 PROME re-review | Every mapping sourced to this file's hash is withheld on commit. Rows now describing CLOSED contracts: QQQ 740P Oct-15 (`MGMT-QQQ740P-OCT15` SPENT) and USO 150C Oct-14; HBAN row says ×2 vs broker ×1; no rows for QQQ 715P / 735C / 725P / CMG / KRE 67P | Holdings never approve a card; a mapping row is PROME's to change after re-review, not ANVIL's | **PROME** mapping re-review; **TERRY** cards |
| **D-77** | QQQ 715P / 735C / CMG 28P / KRE 67P — ownership, cards | 🟡 record (715P/735C urgent above) | All Will-direct entries 10/12–10/15 with no desk owner, approval or card; 744P closed and historical | No research approval or replacement linkage inferred | **PROME** routes scope; **Will / TERRY** |
| **D-74** | Fidelity bank-put ownership/management (WAL 65P ×4 · OZK 40P ×4) | 🟡 record (order clocks in D-82) | Bought 10/7; bases $682.65 / $322.65; marks down 22.86% / 33.34% today; both badged E (earnings, INFERRED) | Thesis/desk owner/approval unestablished | **PROME** routes scope; **Will / TERRY** |
| **D-79** | USO displayed quote/value precision (historical) | 🟡 historical | 10/15: 155.089 × 37 = 5,738.293 → $5,738.29 displayed, ties within display rounding; GLD likewise (7,607.298 → 7,607.29) | Prior 10/13 1¢ difference explained only as display truncation — UNVERIFIED | **PROME** retains evidence |
| **D-75 · D-66 · D-69 · D-62 · D-63 · D-64 · D-65 · D-61 · D-59 · D-45 · D-55 · D-28 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1** | **Carried discrepancies (18) — every row still OPEN; rows verbatim → rotation 10/08 chunk D1 (D-75) + D2 (the other 17)** | 🟡 carried | None closed, re-dated or re-owned; every cell unchanged in the record. Ticker-bearing items, for the text scan: STNG (D-17) · RH QQQ $715P Aug-31 (D-28) · RH KRE $25P entry (D-54) · RH WAL $77.5P Aug-21 sale (D-18) · the RH T share (D-20) · AAPL 5-sh sale pre-7/30 (D-1) · D-75 (OZK 40P basis 1¢; mirror carries $322.65, record only) | Returns to this table when its state changes | As recorded, per row: **Will** — D-66 · D-69 · D-63 · D-64 · D-61 · D-59 · D-45 · D-55 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1; **RH history before 9/01** — D-28; **PROME** — D-62 · D-65 (re-reads of desktop-local images) · D-75 (record) |

*D-69 remains OPEN (the 9/30→10/1 Activity still lacks +$53.54; nothing invented). D-66 now also carries the 10/14–15 fill times (none shown) and the DERIVED gross prices for the 740P/USO closes. D-71 broker-evidence leg stayed CLOSED (cohort +$142.44; detail → rotation 10/15 chunk A). No carried duty closed by silence.*

*Owner decisions/guards remain: D-47 RH WAL70P gate `GATE-TERRY-ROLL70-EXIT`, last recorded 0-of-3, no resting exit, time stop 12/4; REGINALD grades/TERRY proposes/Will harvests. VLO original held-share gate and terminal scale instruction in Longs/GATES remain; additional-share scope UNKNOWN (D-78). WQ-200 USO stock: no rule live. APD tag/adjustment unverified. No position crossed a pre-registered harvest/disarm line this pass; the QQQ 735C −81.80% and HBAN −37.29% are marks, not gate readings. D-72/D-73 closures remain history → rotation 10/08 chunk F.*

---

## Immediate Actions (10/15 10:10 ET receipt; intraday marks, not live/close)

| Item | State | Owner |
|---|---|---|
| 🔴 QQQ Oct-15 715P ×1 — **EXPIRES TODAY**; SELL-OR-ROLL before the close; bought this morning @$1.92, marks $0.93; no card | 0 calendar DTE | **Will** orders / **TERRY** if asked |
| 🔴 QQQ Oct-16 735C ×1 (−81.80%) and HBAN Oct-16 16P ×1 — SELL-OR-ROLL before Friday's close; HBAN's 10/14 re-rule outcome unseen | 1 calendar DTE | **Will / TERRY** |
| 🔴 D-60 — ITM handling at expiry never observed; three contracts expire today/tomorrow | today / tomorrow | **Will** broker policy |
| 🟠 D-82 — WQ-428 OZK ×4 (before 10/20) · WQ-429 WAL ×4 (before 10/19): no order visible, both still held | 10/19–10/20 | **Will** confirms; PROME records |
| 🟠 D-80 — three unseen fills (GLD +3 · HBAN −1 · QQQ 725P open leg); supply the lower Activity rows | evidence | **Will** supplies; **PROME** records |
| 🟠 D-78 — VLO second share: scope UNKNOWN; terminal scale instruction not autoapproved | scope | **Will / PROME / TERRY** |
| 🟡 D-70 — mappings withheld on the new hash; QQQ 740P Oct-15 + USO 150C Oct-14 rows are CLOSED contracts; TSV untouched by ANVIL | re-review | **PROME** |
| 🟡 D-76 / D-77 / D-74 / D-81 / D-83 — fills, ownership, cash-column, clock/Robinhood; all 18 carried discrepancies stay OPEN; D-69 missing +$53.54 | integration/evidence | **PROME / TERRY / Will** |

---

*History → `_archive/JOURNAL.md` | Prior reconciles in git history + `_archive/`; immediately prior whole mirror = `git show c5a1d40facecd5d0e4b581543b55ad7c149299aa:FORGE/STATUS.md` | Full-portfolio Feb snapshot → `PORTFOLIO.md` (**FROZEN/superseded, historical only — never cite as live**) | Position truth = Will/broker direct (off-repo) | Marks-of-record transcription → `PROME/data/2026-10-15_broker-capture-TRANSCRIPTION.md` (17 Fidelity rows + Pending block + Past-30-days Activity cut at the 10/14 735C buy; received Thursday 10/15 10:10 ET; capture/fill times UNKNOWN); prior `…2026-10-14_….json` · `…2026-10-13_….md` (positions + later Activity) · `…2026-10-11_…` (positions + Activity) · `…2026-10-07_…` · `…2026-10-01b_…` (post-close) · `…2026-10-01_…` (intraday + Pending list) · `…_2026-09-30_…` · `…_2026-09-29_…` (RH rows' source)*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumers: `AGENTS/TERRY/scripts/positions_from_forge.py` (sections `^## (Fidelity|Robinhood)` + `^## Account <NAME>`; table headers by prefix; cell text — emphasis and strikethrough visible) · `PROME/tools/desk_attention.py` `holdings()` (same sections; `Qty` + `Ticker|Strike|Position` headers; expiry year from `**Updated:**`) · `PROME/tools/will_brief.py` `parse_money()` (header before the first `## `: `account total:**`, `money market):** $X (Y%)`, `**Updated:** YYYY-MM-DD`, `marks = [Fri ]YYYY-MM-DD`) · `FORGE/position_management.tsv` `source_sha256` (any byte change here withholds every mapping sourced to this file until PROME re-reviews) · `AGENTS/BRENT/scripts/pending_receipts.py` (text-level closure candidates). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself here in the same commit that starts parsing. *(Pass notes 9/27 → 10/8 → rotation 10/08 chunk G. Conventions they set, still binding: the header money line keeps the shape `will_brief.py` reads; option expiries carry the year; the `Mark <m/d>` header is prefix-bound; terminal records live in italic lines, which no parser reads as rows.)*
