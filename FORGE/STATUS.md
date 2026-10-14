# FORGE — Trading Operations

Dashboard management mapping → [position_management.tsv](position_management.tsv); maintenance contract → [dashboard notes](DASHBOARD.md). Holdings remain in this file; approval, order and fill evidence are separate. A changed evidence source invalidates its management mapping until reviewed.

> ✅ **2026-10-14 (Wed) — RECONCILE BY ANVIL to Will's Fidelity positions and two filled orders received Wednesday 10/14. Exact capture/mark/fill times UNKNOWN; marks are NOT certified live or closes.** Source `PROME/data/2026-10-14_broker-capture-TRANSCRIPTION.json`; account continuity inferred from matching holdings/pending, not independently verified. All **17/17** position value-minus-basis rows verified: positions **$20,913.51** + cash **$14,027.08** + pending **+$1,491.64** = **$36,432.23 to the cent**. Vs Activity-adjusted prior mirror: **0 NEW, 1 CLOSED** (QQQ Oct-14 744P ×1 sold close), **1 QTY CHANGE** (QQQ Oct-15 740P 4→3), **1 VERIFIED/REVALUED** (AAPL5, previously derived/unvalued), **15 MARK ONLY** (other unchanged-quantity holdings). USO quote/value now ties; prior D-79 precision difference remains historical/unexplained.
>
> ⚠️ **ACCOUNT SCOPE — Fidelity: ONE Traditional IRA; account id redacted, identity not independently verified. Robinhood Individual NOT provided — carried 9/29 rows unverified today; absence establishes no closure.**
>
> **Updated:** 2026-10-14 = receipt date only · marks = UNKNOWN (all Fidelity cells `[10/14 rcv]` = `[broker export received 2026-10-14; time UNKNOWN ET]`; exact capture time UNKNOWN) · **Fidelity cash (money market):** $14,027.08 (38.50%) + **Pending activity +$1,491.64** · **Fidelity account total:** $36,432.23 (Today +$1,750.40 / +5.05%; open G/L +$1,589.64 / +8.23%). Vs prior original snapshot $33,729.03: **+$2,703.20 = positions −$495.98 + cash +$1,709.51 + pending +$1,489.67**; snapshot change, not daily/realized P&L. Pending exactly equals today's two QQQ sale proceeds **$670.32 + $821.32**; already included in total, never add again. Cash+pending **$15,518.72** is not verified settled cash/buying power. **QQQ740P sold1 @$6.71, net$670.32; QQQ744P sold1 @$8.22, net$821.32; derived realized +$139.66 / +$545.66 = +$685.32**, not additive to displayed daily P&L. AAPL5/basis$118.22 now directly verified; conditional prior-sale realized+$1,589.31 assumes no unseen basis adjustment (D-76). Prior10/12–13 five non-AAPL outcomes+$99.29 remain historical, not today's result; prior realized records retained below/in rotations. **Robinhood:** $295.15 / BP $8.94 `[9/29 13:4x intraday]`, not re-captured. Prior mirror in git; rotations `_archive/STATUS_ROTATION_2026-10-11.md` and `_archive/STATUS_ROTATION_2026-10-08.md`; earlier rotations remain there.

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (its own header names the current base and amendment count). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*Quoted cells `[10/14 rcv]` (received 2026-10-14, capture/mark time UNKNOWN). All six stock quantities/bases directly verified. Rounded average costs and percentages are preserved as displayed, not exact fills. Settled fill notes → rotation 10/01 chunk B.*

| Ticker | Type | Qty | Cost | Mark 10/14 rcv | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | 5 | $23.64 | $345.16 | $1,725.80 | +$1,607.58 / +1,359.82% | Today +$19.45; exact basis $118.22 now broker-verified. Prior10/13 sale5 @$341.515 net$1,707.54; prior basis$236.45−remaining$118.22=$118.23 removed basis ⇒ conditional realized+$1,589.31, assuming no unseen basis adjustment; not broker-reported realized P&L (D-76). Prior9/15 sale5 ≈+$1,534.92 remains historical; pre7/30 sale5 remains D-1 |
| GLD | Stock | 17 | $374.74 | $374.32 | $6,363.44 | −$7.06 / −0.12% | Today −$124.95; exact basis $6,370.50. MIDAS domain; largest line by this capture’s value |
| USO | Stock | 37 | $122.28 | $153.30 | $5,672.10 | +$1,147.83 / +25.37% | Today +$7.77; exact basis $4,524.27. Current last×37 ties; prior D-79 precision discrepancy historical. **WQ-200 DECLINED by Will 9/10 — NO harvest/give-back rule live; Will manages by hand.** BRENT thesis (Hormuz-gap entry) |
| VLO | Stock | 2 | $426.00 | $455.85 | $911.70 | +$59.70 / +7.00% | Today −$1.22; exact basis $852.00. **Prior10/13 QTY CHANGE 1→2**; Activity confirms10/12 buy net$440; added1share is derived from quantity bridge, individual gross fill/time absent (D-76). Authorization/management scope remain UNKNOWN (D-78). Original share bought 9/18 @ $412.00 (fill TIME not shown — D-55). **Historical Will confirmation 2026-10-07: “Yes, still one share”; superseded on quantity only by this two-share view.** WQ-213 originally 1 of 3; **its remaining 2-sh scale instruction was STAND DOWN** under `PROME/GATES.tsv` GATE-TERRY-VLO-SCALE, TERMINAL on the 9/25 F1 fire (TERRY 4ad672c43; its optional CME source-① override remains as written there). **The additional share does not autoapprove the terminal scale rule or establish extension of the original management scope. The originally held share's exit rule is `GATE-TERRY-VLO-HELD-01` — the letter (condition AND consequence cells, incl. who acts on each leg) is read at `PROME/GATES.tsv`, as amended by WQ-386 (`PROME/proposals/2026-10-07_VLO-december-management-RULED.md`, approved 10/7); nothing of it is restated here.** The gate reads the crack and the text, not the share's mark. The prior note, which restated the letter, is verbatim in rotation 10/08 chunk H |
| APD | Stock | 2 | $294.79 | $290.61 | $581.22 | −$8.35 / −1.42% | Today +$3.30; exact basis $589.57. Historical 10/1 "D" badge / $1.81 reference-price adjustment remains unverified; no dividend row in the 10/2–10/8 Activity. Thesis tag unassigned since 7/30 |
| TBT | Stock | 5 | $34.40 | $41.65 | $208.25 | +$36.24 / +21.06% | Today +$0.05; exact basis $172.01. **Prior10/13 QTY CHANGE 10→5**, basis $346.46→$172.01; Activity confirms10/12 sale net$210.40; removed basis$174.45 is derived from the two holdings views, yielding realized+$35.95. Sold5 derived from quantity bridge; gross fill/time absent (D-76). Duration-short leg (BOND/TERRY). **WQ-357 LATER 10/3 selected path C while BOND researches; 10/14 decision clock remains for the surviving holding, no new order inferred.** |

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

*No live event-box rows — the VIX $20C/$25C spread (CLOSED 2026-07-30, realized −$111.60) and the five Aug-21-2026 EXPIRED rows (realized −$2,816.72 total) are terminal → rotation records.*

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, owned by no agent unless separately recorded. **SELL-OR-ROLL before expiry** (`USER.md`, 9/30 19:03 ET); TERRY recommends, Will orders. The capture establishes holdings/fills, not contract-specific cards or approvals; grouping is navigation, not a thesis or scope ruling. Last marks are not executable bids; working orders UNKNOWN. Receipt-day DTE is scheduling only; broker capture time UNKNOWN.

| Ticker | Strike | Expiry | Qty | Cost | Mark 10/14 rcv | Value | P&L | Note |
|--------|--------|--------|-----|------|---------------|-------|-----|------|
| USO | $150C | Oct-14-2026 | 2 | $1.88 | $2.95 | $590.00 | +$214.67 / +57.19% | `[10/14 rcv]`; MARK ONLY; BOUGHT OPEN 10/9 net −$375.33; exact basis $375.33. Today −$70.00. **Wednesday 10/14 expiry TODAY, 0 calendar DTE from receipt.** Distinct from closed Oct-09 call and 37 shares; no roll/linkage inferred. No inherited 10/09 hard stop; existing delivered TERRY card reused (PROME receipt); 10/12 sell1 limit$2.66 Day VERIFIED CANCELED, not a fill/resting order; any replacement order UNKNOWN |
| QQQ | $740P | Oct-15-2026 | 3 | $5.31 | $8.37 | $2,511.00 | +$919.01 / +57.72% | `[10/14 rcv]`; QTY CHANGE 4→3; remaining basis $1,591.99. Bought4 10/2 net−$2,122.65; sold1 10/14 limit$6.65 Day, FILLED @$6.71 net$670.32, time UNKNOWN. Removed basis$530.66 (prior−current, assumes no unseen basis adjustment) ⇒ derived realized+$139.66. Pending proceeds already included in account total. Today +$1,704.00. **Thu 10/15 expiry TOMORROW, 1 calendar DTE.** `MGMT-QQQ740P-OCT15`: SELL-OR-ROLL BEFORE THURSDAY; Wed10/14 times remain a PROPOSAL for Will. If exercised: sell300 QQQ at$740 ($222,000), mechanics only, D-60 |
| CMG | $28P | Oct-30-2026 | 2 | $0.55 | $0.46 | $92.00 | −$17.33 / −15.86% | `[10/14 rcv]`; MARK ONLY; basis $109.33; Today +$0.00. 16 calendar DTE. BOUGHT OPEN10/12 net−$109.33; gross fill/time, thesis/desk ownership and contract-specific management approval UNKNOWN; no inferred replacement, research approval or trade card (D-76/D-77) |

*QQQ Oct-14 744P ×1 (BOUGHT OPEN10/12 net−$275.66) **SOLD CLOSE10/14**, limit$8.00 Day, FILLED @$8.22, net$821.32−basis$275.66=derived realized+$545.66; fill time UNKNOWN. Absent from current holdings, closure confirmed by filled order. No further expiry task for this contract; proceeds already in pending. QQQ740P partial realized+$139.66 plus this close = +$685.32, not additional daily/account P&L. No roll linkage inferred.*

*Disposition now evidenced by Activity (§4): QQQ Oct-12 755C ×1 **EXPIRED as of10/12, posted10/13**, basis$144.66 ⇒ realized−$144.66; its canceled market sell is not a sale. QQQ Oct-15 745P remaining1 **SOLD CLOSE10/12**, net$393.34−remaining basis$283.66=+$109.68. Earlier10/8 partial+$321.65 is already recorded; full cohort$605.32+$393.34−$567.33=+$431.33, never add that total again. Prior `MGMT-QQQ745P-OCT15` before-Thu deadline/Wed proposed times are historical; contract disposal established, formal decision-record integration belongs to PROME/TERRY. No roll linkage inferred.*

*QQQ Oct-13 750C roundtrip, absent from both saved holdings views: BOUGHT OPEN10/12 in two net rows$67.66+$68.66=$136.32; SOLD CLOSE OPTION LIQUIDATION10/13 ×2 at$0.01, net$1.97 ⇒ realized−$134.35. Initiator/future policy UNKNOWN. This$1.97 already sits in earlier snapshot pending; order/activity rows are duplicate evidence, not additional cash.*

*Oct-09 QQQ 755P/750C and USO 150C CLOSED by 10/9 sell-closing rows. Net proceeds $361.94 / $237.34 / $0.99 respectively; derived realized +$123.28 / +$80.68 / −$298.67. 750C +$80.68 already booked; USO “expired worthless” prior disposition superseded by sell-closing receipt. Gross prices, fill times and initiator UNKNOWN. Prior 10/8 realized +$918.30; Oct-02 740P −$886.90 and Oct-05 735P −$1,302.97 remain historical bookings. No exercise/short-stock outcome inferred.*

## Fidelity — Thesis Puts

*Instrument grouping is navigation, not approval: the Fidelity WAL/OZK rows below are Will-direct holdings (bought 10/7, Activity); thesis/desk ownership and management approval are NOT established by the broker view.*

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

*TLT $77P Sep-30 ×15 (TRY-FIRE-004's last lot): SOLD TO CLOSE 9/30 ⇒ −$154.64; no replacement TLT line; detail → rotation 10/01 chunk D.*

*TLT Oct-16 $82P remaining1 **SOLD CLOSE10/12** net$400.34−remaining basis$167.67=realized+$232.67. Prior9/28 partial1-of-2 sale@$3.60⇒+$191.66 remains separately booked. WQ-357 LATER10/3 pathC and `MGMT-TLT82P-OCT16`/WQ-302 Wed10/14 clock are historical management duties: disposal now evidenced, no current TLT holding asserted; PROME/TERRY integrate decision records. BOND research delivered10/5 (`ff0992bf1`) was not a new trade ruling. Prior2.50× mark multiple never a price trigger. D-60 future ITM handling remains UNKNOWN.*

### KRE — regional banks (REGINALD)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
*All four rows `[10/14 rcv]` (received 2026-10-14, capture/mark time UNKNOWN); Nov27 row does not establish ownership/management approval. KRE $60P Sep-30 ×2 sold 9/30 @ $0.01 ⇒ −$451.48 (leg 1 of the roll into the Dec-31 65P; detail + the D-67 mark note → rotation 10/01 chunk D). Rail on the 65P: *"hard stop Thu 12/31 15:00 ET"* (`MGMT-KRE65P-DEC31`, `5ce609f80`).*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $67P | Nov-27-2026 | 4 | $1.28 | $1.35 | $540.00 | +$29.35 / +5.74% (today +$32.00). MARK ONLY; basis $510.65; BOUGHT OPEN10/12 net−$510.65; gross fill/time/card UNKNOWN (D-76/D-77). Grouping under KRE is not desk ownership/approval. 44 calendar DTE from receipt10/14 |
| $60P | Dec-18-2026 | 2 | $2.57 | $0.52 | $104.00 | −$409.34 / −79.75% (today +$14.00). MARK ONLY; basis $513.34. 65 calendar DTE from receipt10/14 |
| $60P | Dec-18-2026 | 3 (M) | $2.93 | $0.52 | $156.00 | −$722.02 / −82.24% (today +$21.00) — multi-lot marker; basis $878.02; **five** Dec-18 KRE 60P across two lots. MARK ONLY. 65 calendar DTE from receipt10/14 |
| $65P | Dec-31-2026 | 2 | $1.69 | $1.54 | $308.00 | −$29.33 / −8.70% (today −$10.00) — MARK ONLY; basis $337.33. Bought 9/30 ×2 @ $1.68 (roll leg 2). Will's own add; `MGMT-KRE65P-DEC31` (`5ce609f80`): hard stop Thu 12/31 15:00 ET, not a price gate. 78 calendar DTE from receipt10/14 |

### WAL (REGINALD) — Sep-18 pair EXPIRED

*$70P + $67.5P Sep-18 ×1 each: **EXPIRED as of 9/18, broker-confirmed** (ledger rows posted 9/21) ⇒ realized **−$768.67 and −$750.67 = −$1,519.34** (full basis) — the WQ-168 ①② LAPSE as ruled. Rows → rotation record. Duration roll = the Robinhood WAL Dec-18 $70P ×1 below. The RH WAL $77.5P Aug-21 sale: P&L UNRECORDED — D-18.*

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18-2026 | 1 | $11.85 | $1.60 | $160.00 | −$1,024.67 / −86.50% | `[10/14 rcv]`; basis $1,184.67; Today +$35.00. MARK ONLY; BROCK thesis vehicle. Will ruled HOLD 2026-08-13 (`PROME/proposals/2026-08-13_private-credit-batch-RULED.md` §②; vehicle-mismatch flag live). 65 calendar DTE from receipt10/14 |
| HBAN | $16P | Oct-16-2026 | 2 | $0.96 | $0.85 | $170.00 | −$21.34 / −11.16% | `[10/14 rcv]`; basis $191.34; Today +$12.00. MARK ONLY. The 7/18 ride-to-expiry premise failed per TERRY 9/26; `MGMT-HBAN16P-OCT16` / WQ-302 re-rule due **Wed 10/14**. Current moneyness not verified (no underlying quote in the view). 2 calendar DTE from receipt10/14 |
| OZK | $40P | Nov-20-2026 | 4 | $0.81 | $0.30 | $120.00 | −$202.65 / −62.81% | `[10/14 rcv]`; basis **$322.65** (10/7 view showed $322.66 — D-75); Today −$52.00. **Bought 10/7, −$322.65 (Activity); Will-direct.** Thesis/desk ownership and management approval UNRECORDED; holdings do not autoapprove research or a trade. Sell-or-roll before expiry; no contract-specific card recorded. 37 calendar DTE from receipt10/14 |
| WAL | $65P | Dec-18-2026 | 4 | $1.71 | $1.75 | $700.00 | +$17.35 / +2.54% | `[10/14 rcv]`; basis $682.65; Today +$160.00. **Bought 10/7, −$682.65 (Activity); Will-direct.** Thesis/desk ownership and management approval UNRECORDED; holdings do not autoapprove research or a trade. Sell-or-roll before expiry; no contract-specific card recorded. Distinct from Robinhood WAL Dec-18 $70P ×1. 65 calendar DTE from receipt10/14 |


## Robinhood — satellite account (Individual)

*All holdings/figures below retained from the 9/29 source; carried DTE annotations are historical, not a current freshness assertion.*

> ⚠️ **NOT CAPTURED IN THIS 10/14 RECEIPT (nor 10/13, 10/11, 10/7, 10/1 or 9/30) — every cell below is the 9/29 card, unverified today.** 9/29 card: **account $295.15, BP $8.94** `[9/29 13:4x intraday]`; lines + BP = $290.15 ⇒ **$5.00 UNEXPLAINED (D-64)**. Per-line cost/value DERIVED from P/L ÷ P/L% (no Mark column ⇒ machine class `unverified` by design). The prediction-market line and the 9/01→9/25 dead-by-date bookings — USO $159C Sep-11 (bought 9/10, expired $0 — D-58) · QQQ $713C Sep-16 + USO $165C Sep-16 (both expired $0 — D-57) — verbatim → rotation 10/08 chunk B.

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **WAL $70P** | **Dec-18-2026** | 1 | **$2.20 ($220)** — bought 9/02 @ $2.20 (RH activity) ✓ | ≈$265.00 *(derived; mark ≈$2.65)* | ✅ **ON CARD 9/29 — +$45.00 / +20.45%** | TRY-WAL-ROLL70 (filled in Robinhood). Guard **`GATE-TERRY-ROLL70-EXIT`** *"WAL OFFICIAL CLOSE ≥ $81.90 on THREE CONSECUTIVE sessions"* — **0-of-3 as last recorded here** (REGINALD through 9/23, per TERRY STATUS 9/24; not re-read this pass). The option's +20.45% is not the gate — the gate reads WAL's close (rule 7). **$4.40 GTC sell order: CANCELLED / not there — Will 9/28** (`PROME/inbox/processed/2026-09-28_from-WAL_WQ-324-325-ruled-verbatim-and-4.40-GTC-cancelled.md`) ⇒ **no resting exit order; any take-profit is Will's manual act.** Time stop Fri 12/4. 78 DTE. **D-47** |
| **KRE $25P** | 1/15/2027 | 1 | $53.00 — card-derived ✓ | ≈$1.00 *(derived)* | ✅ **ON CARD 9/29 — −$52.00 / −98.11%** | Deep-OTM lottery; entry pre-7/16, never recorded — **D-54** (before the 9/01 activity view). 106 DTE |
| T | stock | 1 | — | — | ⚠️ no stocks card 9/29; no T row in RH activity 9/01→9/25 | Hypothesis: sold before 9/01, unconfirmed — **D-20**. The card no longer closes to the cent (D-64), so the 9/27 "no stock line" inference is weaker |

## Account UNATTRIBUTED — receipted fills not yet attributed to an account

*No rows. VLO ×1 (this section's only row since 9/19) moved to § Fidelity — Longs on the 9/25 ledger (D-55 account leg CLOSED). The section stays as the landing place for a receipt that names no account (the parser admits it — TERRY `cfd9b9115`).*

---

## ⚠️ Reconcile discrepancies (received 2026-10-14; capture/mark time UNKNOWN)

> Broker view > Will's word > desk record; conjectures labeled. Robinhood not captured. DTE from receipt10/14 only. **Permanently UNKNOWN by WQ-167 (never asks): 9/2 USO 135C sale price.** Immediately prior section → `7a7d8dccfe7ecbe10a18184711e9d602fa524c37:FORGE/STATUS.md`; earlier section byte-exact → `_archive/STATUS_ROTATION_2026-10-11.md`; carried duty detail → rotation 10/08 chunks D1/D2.

### Will supplies / PROME re-reads — facts owed

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| NEW | USO Oct-14 150C ×2 | 🔴 Wednesday10/14 TODAY, 0 calendar DTE | Value$590; basis$375.33; SELL-OR-ROLL before expiry. QQQ744P×1 sold close today @$8.22, net$821.32; closure verified | USO card delivered per PROME; prior sell1@$2.66 Day VERIFIED CANCELED. Current replacement/order/disposition UNKNOWN; no inherited Oct09 stop or roll linkage | **Will** orders; **TERRY** recommendations; PROME records |
| DATED | QQQ Oct-15 740P ×3 / HBAN Oct-16 16P ×2 / TBT5 | 🟠 Wednesday10/14 management, expiries10/15–16 | QQQ4→3 confirmed; sold1 @$6.71 net$670.32; remaining3 value$2,511/basis$1,591.99. Sell-or-roll before Thu; Wed times proposals. HBAN re-rule Wed; TBT5 retain10/14 clock | Broker fills do not approve/cancel remaining management. Remaining working orders UNKNOWN; formal records integration PROME/TERRY | **Will / TERRY** |
| **D-60** | Fidelity future ITM expiry handling | 🔴 next expiries10/14–16 | Historical OPTION LIQUIDATION sales/QQQ755C expiry establish no future policy. USO calls×2 exercise buys200 at$150 ($30,000); remaining QQQ740P×3 exercise sells300 at$740 ($222,000), mechanics only. QQQ744P closed; no QQQ/TLT shares in view | Moneyness at liquidation, initiator, deterministic LIQUIDATE vs EXPIRED policy UNKNOWN; no future outcome inferred | **Will** — broker policy |
| **D-76** | Activity supplied; refreshed AAPL/QQQ evidence, detailed fills remain | 🟡 narrowed evidence duty | Current AAPL5/basis$118.22/value$1,725.80 verified. Prior5 sale net$1,707.54 minus conditional removed basis$118.23 yields+$1,589.31. Today QQQ740P sell1@$6.71 net$670.32 and QQQ744P sell1@$8.22 net$821.32 match pending$1,491.64; combined derived realized+$685.32. Prior five non-AAPL outcomes+$99.29 remain historical | AAPL removed basis assumes no unseen adjustment, not broker lot/realized report. Exact fill times missing; prior10/12–13 gross fills/quantities gaps remain. Cash/BP settlement status unverified. No roll linkage inferred | **Will** supplies detailed fills/lots; **PROME** records; **TERRY** integrates evidence |
| **D-78** | VLO additional share authorization and management scope | 🟠 scope before action | Broker2 shares, basis$852. Original1-share WQ-213 holding and terminal GATE-TERRY-VLO-SCALE remain historical approved scope; original held-share rule referenced in Longs | Second-share10/12 net$440 entry now evidenced; authorization/management scope UNKNOWN; capture does not override terminal scale rule or extend original gate to the additional share | **Will** authorization; **PROME / TERRY** scope reconciliation |
| **D-70** | Management mappings/cards follow-through | 🟡 review | Every changed source hash withholds old mappings until PROME re-review; QQQ740P retains proposal/deadline distinction; absent rows cannot remain live mappings | Receipt/consumption requires PROME verification; holdings never approve a card | **PROME** mapping re-review; **TERRY** cards |
| **D-77** | KRE67P / CMG28P ownership/cards; QQQ744P historical scope | 🟡 record | KRE67P×4 basis$510.65; CMG28P×2 basis$109.33 remain. QQQ744P now closed10/14; no live expiry/card duty | Contract-specific approval/desk ownership unestablished; closed QQQ card history not inferred. No research approval or replacement linkage inferred | **PROME** routes scope; **Will / TERRY** |
| **D-74** | Fidelity bank-put ownership/management | 🟡 record | WAL Dec18 65P×4 basis$682.65/value$700; OZK Nov20 40P×4 basis$322.65/value$120. Bought10/7; Will-direct | Thesis/desk owner/approval unestablished; no autoapproved research/trade | **PROME** routes scope; **Will / TERRY** |
| **D-79** | USO prior displayed quote/value precision | 🟡 historical record | Current$153.30×37=$5,672.10 ties. Prior10/13 last$152.748×37 rounded$5,651.68 vs displayed$5,651.67; prior gain/account sum tied | Current discrepancy cleared; explanation of prior hidden precision/asynchrony UNVERIFIED. Prior source cells retained in transcription/history | **PROME** retains evidence; broker detail if available |
| **D-75 · D-66 · D-69 · D-62 · D-63 · D-64 · D-65 · D-61 · D-59 · D-45 · D-55 · D-28 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1** | **Carried discrepancies (18) — every row still OPEN; rows verbatim → rotation 10/08 chunk D1 (D-75) + D2 (the other 17)** | 🟡 carried | None closed, re-dated or re-owned; every cell unchanged in the record. Ticker-bearing items, for the text scan: STNG (D-17) · RH QQQ $715P Aug-31 (D-28) · RH KRE $25P entry (D-54) · RH WAL $77.5P Aug-21 sale (D-18) · the RH T share (D-20) · AAPL 5-sh sale pre-7/30 (D-1) · D-75 (OZK 40P basis 1¢; mirror carries $322.65, record only) | Returns to this table when its state changes | As recorded, per row: **Will** — D-66 · D-69 · D-63 · D-64 · D-61 · D-59 · D-45 · D-55 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1; **RH history before 9/01** — D-28; **PROME** — D-62 · D-65 (re-reads of desktop-local images) · D-75 (record) |

*D-69 remains OPEN: the supplied 9/30→10/1 Activity still lacks +$53.54 (latest 9/30 $14,094.06 − Oct1 buy $890.65 = $13,203.41 versus $13,256.95 shown). No dividend/adjustment invented; Will supplies missing row. D-66 also retains all fill-time/gross-price unknowns, including10/9 entries/exits; prior §4 supplies AAPL$341.515/QQQ750C$0.01 gross fills, current orders QQQ740P$6.71/744P$8.22, but none supplies fill times. Remaining10/12–14 detailed-fill gaps are tracked in D-76. D-75 remains record-only, unchanged $322.65 basis confirmed. No carried duty closed by silence.*

*D-71 broker-evidence leg CLOSED: four Oct1 QQQ740P sell-closing cash rows $343.34 + $396.34 + $1,113.98 + $22.75 = $1,876.41 against Sep30 opening $1,733.97 ⇒ full-cohort realized +$142.44. Prior final-lot-only inferred −$747.91 is superseded as a cohort result; do not double-book earlier partial results. Quantities per fill, times and gross prices absent, not inferred; record under D-66. WQ-347 evidence now supplied. WQ-397 disposition supplied: remaining QQQ755P sold close net $361.94; full 755P cohort +$719.93. USO full Oct09 cohort −$207.00; WQ-396 earlier worthless word is history, not broker outcome. PROME updates decision records; ANVIL does not.*

*Owner decisions/guards remain: D-47 RH WAL70P gate `GATE-TERRY-ROLL70-EXIT`, last recorded 0-of-3, no resting exit, time stop12/4; REGINALD grades/TERRY proposes/Will harvests. VLO original held-share gate and terminal scale instruction in Longs/GATES remain; additional-share scope UNKNOWN (D-78); WQ-200 USO stock no rule live; APD tag/adjustment unverified. D-72/D-73 prior closures remain history → rotation10/08 chunkF.*

---

## Immediate Actions (10/14 receipt; marks not live/close)

| Item | State | Owner |
|---|---|---|
| 🔴 USO Oct14 150C×2 — SELL-OR-ROLL before expiry TODAY; card delivered; prior1@$2.66 canceled, current orders UNKNOWN. QQQ744P CLOSED10/14 | 0 calendar DTE | **Will / TERRY** |
| 🟠 QQQ Oct15 740P×3 remaining after sold1@$6.71 — SELL-OR-ROLL before Thursday; Wed times proposals only | 1 calendar DTE | **Will / TERRY** |
| 🟠 HBAN16P×2 re-rule Wed10/14, Fri10/16 expiry; TBT5 retain10/14 decision clock | dated | **Will / TERRY** |
| 🔴 D-60 — future ITM handling UNKNOWN; liquidation history establishes no deterministic policy | next expiries | **Will** broker policy |
| 🟡 D-76 — AAPL5/basis now verified; conditional prior realized+$1,589.31, not broker lot report. Current QQQ fills verified; fill times/prior detail gaps remain | narrowed evidence | **Will** supplies; **PROME / TERRY** reconcile |
| 🟠 D-78 — VLO second share is real; authorization/management scope UNKNOWN; terminal scale instruction not autoapproved | scope | **Will / PROME / TERRY** |
| 🟡 D-70/D-74/D-77 — mappings/cards/ownership; all18 carried discrepancies stay OPEN; D-69 missing+$53.54; D-79 historical precision; Robinhood stale | integration/evidence | **PROME / TERRY / Will** |

---

*History → `_archive/JOURNAL.md` | Prior reconciles in git history + `_archive/`; immediately prior whole mirror = `git show 7a7d8dccfe7ecbe10a18184711e9d602fa524c37:FORGE/STATUS.md` | Full-portfolio Feb snapshot → `PORTFOLIO.md` (**FROZEN/superseded, historical only — never cite as live**) | Position truth = Will/broker direct (off-repo) | Marks-of-record transcription → `PROME/data/2026-10-14_broker-capture-TRANSCRIPTION.json` (17 Fidelity rows plus two filled orders received Wednesday10/14; capture/mark/fill times UNKNOWN); prior `PROME/data/2026-10-13_broker-capture-TRANSCRIPTION.md` (positions + later Activity) · `…2026-10-11_…` (positions + Activity) · `…2026-10-07_…` · `…2026-10-01b_…` (post-close) · `…2026-10-01_…` (intraday + Pending list) · `…_2026-09-30_…` · `…_2026-09-29_…` (RH rows' source)*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumers: `AGENTS/TERRY/scripts/positions_from_forge.py` (sections `^## (Fidelity|Robinhood)` + `^## Account <NAME>`; table headers by prefix; cell text — emphasis and strikethrough visible) · `PROME/tools/desk_attention.py` `holdings()` (same sections; `Qty` + `Ticker|Strike|Position` headers; expiry year from `**Updated:**`) · `PROME/tools/will_brief.py` `parse_money()` (header before the first `## `: `account total:**`, `money market):** $X (Y%)`, `**Updated:** YYYY-MM-DD`, `marks = [Fri ]YYYY-MM-DD`) · `FORGE/position_management.tsv` `source_sha256` (any byte change here withholds every mapping sourced to this file until PROME re-reviews) · `AGENTS/BRENT/scripts/pending_receipts.py` (text-level closure candidates). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself here in the same commit that starts parsing. *(Pass notes 9/27 → 10/8 → rotation 10/08 chunk G. Conventions they set, still binding: the header money line keeps the shape `will_brief.py` reads; option expiries carry the year; the `Mark <m/d>` header is prefix-bound; terminal records live in italic lines, which no parser reads as rows.)*
