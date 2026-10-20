# FORGE — Trading Operations

Dashboard management mapping → [position_management.tsv](position_management.tsv); maintenance contract → [dashboard notes](DASHBOARD.md). Holdings remain in this file; approval, order and fill evidence are separate. A changed evidence source invalidates its management mapping until reviewed.

> ✅ **2026-10-20 (Tue) — RECONCILE BY ANVIL to Will's Fidelity positions + October20 Activity (Pending panel), received ~10:43 ET; exact capture/quote/fill clocks UNKNOWN. These are October20 INTRADAY session marks, NOT closes and NOT executable quotes.** Source `PROME/data/2026-10-20_broker-capture-TRANSCRIPTION.md` (built from TERRY `AGENTS/TERRY/research/2026-10-20_broker-receipt/source.json` + `ACTIVITY.tsv`, `ef82d240d`; PROME independent re-read); no post-snapshot events supplied. ANVIL independently verified **23/23** values and G/L to the cent: positions **$20,870.62** + cash **$17,053.29** − pending **$83.00** = **$37,840.91**. Against last mirror `ba1a41e09`: **1 NEW / 1 QTY CHANGE / 1 GONE (sold close, broker-verified) / 21 MARK ONLY (transcription §④ says 20; parser diff shows 21 — 23 − 1 new − 1 qty)**.
>
> ⚠️ **ACCOUNT SCOPE — ONE Fidelity Traditional IRA (•1326 on file; identifier obscured in the capture; continuity INFERRED, not independently verified). Robinhood Individual NOT provided: every 9/29 row remains unverified today; absence proves no closure. Activity is a cropped Pending panel of five October20 orders (3 filled, 2 Verified Canceled); earlier activity and a complete working-order census are UNSEEN.**
>
> **Updated:** 2026-10-20 · marks = 2026-10-20 intraday, clock UNKNOWN (all Fidelity cells `[10/20 intraday rcv]` = `[broker export received 2026-10-20 ~10:43 ET; capture/quote time UNKNOWN; intraday, not a close]`) · **Fidelity cash (money market):** $17,053.29 (45.07%) + **Pending activity −$83.00** · **Fidelity account total:** $37,840.91 (Today −$2,480.70 / −6.15%; open G/L −$2,340.98 / −10.09%; exact basis $23,211.60). Snapshot change vs10/19: **−$2,046.38 = positions −$1,963.38 + cash −$1,520.92 + pending +$1,437.92**, not a daily/realized return. Cash continuity: 10/19 cash $18,574.21 − 10/19 pending $1,520.92 = $17,053.29 ✓. Visible fills: sell $665.32 − buys $432.66 − $315.66 = $83.00 debit = pending exactly; already included, never add again. Cash+pending $16,970.29 is not certified settled cash/buying power. **DERIVED realized 10/20: QQQ Oct20 720P ×1 STC net $665.32 − basis $190.66 = +$474.66 (booked once, here).** Robinhood $295.15 / BP$8.94 `[9/29 13:4x intraday]`, 21 days old. Prior tables/history remain in Git (`ba1a41e09`, `6fbf39cd0`) and existing rotations; no history rebooked.

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (its own header names the current base and amendment count). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All Fidelity marks `[10/20 intraday rcv]`; capture/quote clocks UNKNOWN. Cost = basis ÷ qty (DERIVED); Mark = value ÷ qty (DERIVED); not exact fills.*

| Ticker | Type | Qty | Cost | Mark 10/20 intraday rcv | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | 4 | $23.65 | $342.245 | $1,368.98 | +$1,274.40 / +1347.43% | Today −$2.78; MARK ONLY; exact basis $94.58. Prior10/15 sale1 net$347.02 ⇒ DERIVED +$323.38; prior sales/lot gaps D-76/D-1 remain historical, not rebookable. |
| GLD | Stock | 24 | $375.81 | $380.60 | $9,134.40 | +$115.03 / +1.28% | Today +$21.84; MARK ONLY; exact basis $9,019.37. 10/19 residual2 fill unseen (D-84); prior GLD+3 gap D-80 survives. MIDAS; largest line. |
| USO | Stock | 35 | $121.90 | $156.29 | $5,470.15 | +$1,203.72 / +28.21% | Today −$158.20; MARK ONLY; exact basis $4,266.43. 10/19 37→35 disposal/proceeds/realized UNKNOWN (D-84). **WQ-200 DECLINED9/10: NO harvest/give-back rule live; Will manages by hand.** BRENT thesis. |
| VLO | Stock | 3 | $432.24 | $427.34 | $1,282.02 | −$14.71 / -1.13% | Today −$17.91; MARK ONLY; exact basis $1,296.73. 10/19 third-share fill unseen (D-84). **Additional-share authorization/management scope UNKNOWN (D-78); no scale approval inferred.** Original9/18 share @$412, fill clock D-55. Original held-share exit letter (condition AND consequence, incl. who acts) remains `GATE-TERRY-VLO-HELD-01` in `PROME/GATES.tsv`, amended WQ-38610/7. Remaining2-sh scale instruction WQ-213 remains STAND DOWN/TERMINAL under `GATE-TERRY-VLO-SCALE` (9/25 F1; optional CME source-① override unchanged). Gate reads crack/text, not stock mark. Prior10/12 added share net$440, gross/time gap D-76. No scope extension inferred. |
| APD | Stock | 2 | $294.79 | $298.735 | $597.47 | +$7.90 / +1.34% | Today +$0.17; MARK ONLY; exact basis$589.57. Historical10/1 D badge/$1.81 reference adjustment unverified; no dividend row supplied; thesis tag unassigned since7/30. |
| TBT | Stock | 5 | $34.40 | $39.72 | $198.60 | +$26.59 / +15.46% | Today −$4.50; MARK ONLY; exact basis$172.01. PROME-supplied WQ-357 SELL approved; 5 still held; no sale fill evidenced (D-82). Prior10/12 sale5 net$210.40, DERIVED +$35.95 (D-76) historical. BOND/TERRY duration-short leg. |

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

*No live event-box rows — the VIX $20C/$25C spread (CLOSED 2026-07-30, realized −$111.60) and the five Aug-21-2026 EXPIRED rows (realized −$2,816.72 total) are terminal → rotation records.*

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, owned by no agent unless separately recorded. **Will manages his own expiries** (`USER.md` § No expiry nagging, 10/20 11:32 ET; supersedes the 9/30 sell-or-roll rail as an instruction): no expiry reminders or sell pushes, and a collapsed line may expire. This mirror records holdings and evidence only; dispositions are read from his captures, never inferred. The capture establishes holdings/fills, not contract-specific cards or approvals; grouping is navigation, not a thesis or scope ruling. Last marks are not executable bids; working orders UNKNOWN. Receipt-day DTE is scheduling only.

| Ticker | Strike | Expiry | Qty | Cost | Mark 10/20 intraday rcv | Value | P&L | Note |
|--------|--------|--------|-----|------|---------------|-------|-----|------|
| QQQ | $715P | Oct-22-2026 | 1 | $4.33 | $2.99 | $299.00 | −$133.66 / -30.89% | `[10/20 intraday rcv]`; basis $432.66; Today −$133.66. NEW; BOUGHT OPEN10/20 @$4.32 ×1 net−$432.66 (Activity row3, broker-verified; fill clock UNKNOWN; a $4.26 limit was Verified Canceled). Card/owner/approval UNKNOWN (D-77). |
| QQQ | $719P | Oct-20-2026 | 1 | $2.78 | $0.98 | $98.00 | −$179.66 / -64.71% | `[10/20 intraday rcv]`; basis $277.66 (10/19 display $276.66; +$1.00, D-85); Today −$241.00. MARK ONLY; expires TODAY 10/20. Card/owner/approval UNKNOWN (D-77). |
| QQQ | $715P | Oct-20-2026 | 1 | $2.01 | $0.37 | $37.00 | −$163.66 / -81.56% | `[10/20 intraday rcv]`; basis $200.66; Today −$161.00. MARK ONLY; expires TODAY 10/20. Card/owner/approval UNKNOWN (D-77). |
| USO | $165C | Oct-30-2026 | 2 | $2.93 | $1.85 | $370.00 | −$216.32 / -36.89% | `[10/20 intraday rcv]`; basis $586.32 = $270.66 (10/19 lot) + $315.66; Today −$280.66. QTY CHANGE1→2; BOUGHT OPEN10/20 @$3.15 ×1 net−$315.66 (Activity row1, broker-verified; fill clock UNKNOWN; a $3.15 limit was Verified Canceled). Card/owner/approval UNKNOWN (D-77). |
| CMG | $28P | Oct-30-2026 | 1 | $0.55 | $0.41 | $41.00 | −$13.66 / -24.99% | `[10/20 intraday rcv]`; basis $54.66; Today −$4.00. MARK ONLY; 10/19 2→1 disposal/proceeds/realized UNKNOWN (D-84). Card/owner/approval UNKNOWN (D-77). |
| CRWV | $56P | Oct-23-2026 | 1 | $1.80 | $0.45 | $45.00 | −$134.66 / -74.95% | `[10/20 intraday rcv]`; basis $179.66; Today −$51.00. MARK ONLY; buy fill/date unseen (D-84). Card/owner/approval UNKNOWN (D-77). |
| USO | $165C | Oct-28-2026 | 1 | $3.36 | $1.39 | $139.00 | −$196.66 / -58.59% | `[10/20 intraday rcv]`; basis $335.66; Today −$128.00. MARK ONLY; bought open10/19 @$3.35. Card/owner/approval UNKNOWN (D-77). |
| USO | $163C | Oct-23-2026 | 1 | $2.90 | $0.82 | $82.00 | −$207.66 / -71.69% | `[10/20 intraday rcv]`; basis $289.66; Today −$133.00. MARK ONLY; bought open10/19 @$2.89. Card/owner/approval UNKNOWN (D-77). |

*QQQ Oct-20 720P ×1 **SOLD CLOSE 10/20** — Activity row5 (broker-verified, Filled; limit $6.44, filled $6.66; fill clock UNKNOWN) net +$665.32 − basis $190.66 (bought open10/19 @$1.90) ⇒ DERIVED realized **+$474.66**. Not a broker realized-P/L report. No roll linkage to the Oct-22 715P inferred.*

*QQQ Oct15 715P ×1, Oct16 735C ×1 and HBAN Oct16 16P ×1 are ABSENT after expiry: actual sale/exercise/lapse and realized UNKNOWN (D-86); no resulting QQQ/HBAN shares visible. Absence does not establish worthless expiry.*

*October19 QQQ call round trips (broker fills; DERIVED realized, booked on the 10/19 mirror — never add again):725C $1.99−$98.66=−$96.67;721C $313.34−$133.66=+$179.68;720C $110.34−$165.66=−$55.32; total+$27.69. QQQ712C sale net$739.32 and Oct21 700P sale net$91.34: opening bases unseen, realized UNKNOWN. No roll linkage inferred.*

*Prior terminal records and prior derived realizations remain historical in `git show 6fbf39cd0:FORGE/STATUS.md` and existing rotations; QQQ Oct16 725P opening basis remains UNKNOWN (D-80); no prior result rebooked.*

*QQQ Oct-15 740P ×3 **SOLD CLOSE 10/14** — three Activity rows net +$1,220.31 / +$1,155.31 / +$1,099.31 = $3,474.93 − remaining basis $1,591.99 ⇒ DERIVED realized +$1,882.94. Cohort: bought 4 10/2 net −$2,122.65; all proceeds $670.32 + $3,474.93 = $4,145.25 ⇒ +$2,022.60, of which +$139.66 (the first sale) was already on the 10/14 mirror — never add the partial and the cohort together. Gross fills DERIVED from the ~$0.69/contract fee pattern ≈ $12.21 / $11.56 / $11.00 (the first, $6.71, is broker-stated); times UNKNOWN (D-66). ⛔ No contract remained for today's expiry — `MGMT-QQQ740P-OCT15` SPENT; no exercise/assignment outcome. These proceeds posted to the cash-balance column on 10/14, not to pending.*
*USO Oct-14 150C ×2 **SOLD CLOSE 10/14** — two Activity rows net +$354.34 + $406.34 = $760.68 − basis $375.33 ⇒ DERIVED realized +$385.35 (gross ≈ $3.55 / $4.07 DERIVED; times UNKNOWN). Will's 10/14 word "i sold before close" is now broker-CONFIRMED. Expiry task retired; no exercise outcome. Distinct from the 37 shares and the closed Oct-09 call; no roll linkage inferred.*

## Fidelity — Thesis Puts

*Instrument grouping is navigation, not approval: the Fidelity WAL/OZK rows below are Will-direct holdings (bought 10/7, Activity); thesis/desk ownership and management approval are NOT established by the broker view.*

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

*TLT $77P Sep-30 ×15 (TRY-FIRE-004's last lot): SOLD TO CLOSE 9/30 ⇒ −$154.64; no replacement TLT line; detail → rotation 10/01 chunk D.*

*TLT Oct-16 $82P remaining1 **SOLD CLOSE10/12** net$400.34−remaining basis$167.67=realized+$232.67. Prior9/28 partial1-of-2 sale@$3.60⇒+$191.66 remains separately booked. WQ-357 LATER10/3 pathC and `MGMT-TLT82P-OCT16`/WQ-302 Wed10/14 clock are historical management duties: disposal now evidenced, no current TLT holding asserted; PROME/TERRY integrate decision records. BOND research delivered10/5 (`ff0992bf1`) was not a new trade ruling. Prior2.50× mark multiple never a price trigger. D-60 future ITM handling remains UNKNOWN.*

### KRE — regional banks (REGINALD)

*All four rows `[10/20 intraday rcv]`; MARK ONLY; grouping is not approval/ownership. Prior Sep30 roll/exits remain historical in Git/rotation10/01 chunk D.*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $67P | Nov-27-2026 | 4 | $1.28 | $0.67 | $268.00 | −$242.65 / -47.52%; basis $510.65; Today −$240.00; MARK ONLY `[10/20 intraday rcv]`; bought10/12 net$510.65; gross/time/card/owner UNKNOWN (D-76/D-77) |
| $60P | Dec-18-2026 | 2 | $2.57 | $0.35 | $70.00 | −$443.34 / -86.36%; basis $513.34; Today −$20.00; MARK ONLY `[10/20 intraday rcv]` |
| $60P | Dec-18-2026 | 3 (M) | $2.93 | $0.35 | $105.00 | −$773.02 / -88.04%; basis $878.02; Today −$30.00; MARK ONLY `[10/20 intraday rcv]`; multi-lot marker; total5 Dec18 60P across2lots |
| $65P | Dec-31-2026 | 2 | $1.69 | $1.05 | $210.00 | −$127.33 / -37.75%; basis $337.33; Today −$64.00; MARK ONLY `[10/20 intraday rcv]`; `MGMT-KRE65P-DEC31`: hard stop Thu12/31 15:00 ET (5ce609f80), not price gate |

### WAL (REGINALD) — Sep-18 pair EXPIRED

*$70P + $67.5P Sep-18 ×1 each: **EXPIRED as of 9/18, broker-confirmed** (ledger rows posted 9/21) ⇒ realized **−$768.67 and −$750.67 = −$1,519.34** (full basis) — the WQ-168 ①② LAPSE as ruled. Rows → rotation record. Duration roll = the Robinhood WAL Dec-18 $70P ×1 below. The RH WAL $77.5P Aug-21 sale: P&L UNRECORDED — D-18.*

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18-2026 | 1 | $11.85 | $1.35 | $135.00 | −$1,049.67 / -88.60% | `[10/20 intraday rcv]`; basis $1,184.67; Today −$45.00. MARK ONLY; BROCK vehicle; HOLD ruled8/13 (private-credit batch §②), vehicle-mismatch flag live. |
| OZK | $40P | Nov-20-2026 | 4 | $0.81 | $0.10 | $40.00 | −$282.65 / -87.60% | `[10/20 intraday rcv]`; basis $322.65; Today −$88.00. MARK ONLY; bought10/7 (Activity). PROME-supplied WQ-428 SELL approved; 4 still held; no sale fill evidenced; order census incomplete (D-82). Thesis ownership UNKNOWN (D-74). |
| WAL | $70P | Dec-18-2026 | 2 | $2.76 | $1.70 | $340.00 | −$211.33 / -38.33% | `[10/20 intraday rcv]`; basis $551.33; Today −$210.00. MARK ONLY; buy fill/date unseen (D-84); ownership/card/approval UNKNOWN (D-74). **Fidelity2 is DISTINCT from Robinhood1; no inherited RH gate.** |
| WAL | $65P | Dec-18-2026 | 4 | $1.71 | $0.80 | $320.00 | −$362.65 / -53.12% | `[10/20 intraday rcv]`; basis $682.65; Today −$280.00. MARK ONLY; bought10/7 (Activity). PROME-supplied WQ-429 SELL approved (window ended10/19); 4 still held; no sale fill evidenced; order census incomplete (D-82). Thesis ownership UNKNOWN (D-74). |
| ZION | $62.5P | Nov-20-2026 | 2 | $2.18 | $1.10 | $220.00 | −$215.33 / -49.46% | `[10/20 intraday rcv]`; basis $435.33; Today −$210.00. MARK ONLY; buy fill/date unseen (D-84); ownership/card/approval UNKNOWN (D-74). |


## Robinhood — satellite account (Individual)

*All holdings/figures below retained from the 9/29 source; carried DTE annotations are historical, not a current freshness assertion.*

> ⚠️ **NOT CAPTURED IN THIS 10/20 RECEIPT (nor 10/19, 10/14, 10/13, 10/11, 10/7, 10/1 or 9/30 — 21 days since the 9/29 card) — every cell below is the 9/29 card, unverified today.** 9/29 card: **account $295.15, BP $8.94** `[9/29 13:4x intraday]`; lines + BP = $290.15 ⇒ **$5.00 UNEXPLAINED (D-64)**. Per-line cost/value DERIVED from P/L ÷ P/L% (no Mark column ⇒ machine class `unverified` by design). The prediction-market line and the 9/01→9/25 dead-by-date bookings — USO $159C Sep-11 (bought 9/10, expired $0 — D-58) · QQQ $713C Sep-16 + USO $165C Sep-16 (both expired $0 — D-57) — verbatim → rotation 10/08 chunk B.

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **WAL $70P** | **Dec-18-2026** | 1 | **$2.20 ($220)** — bought 9/02 @ $2.20 (RH activity) ✓ | ≈$265.00 *(derived; mark ≈$2.65)* | ✅ **ON CARD 9/29 — +$45.00 / +20.45%** | TRY-WAL-ROLL70 (filled in Robinhood). Guard **`GATE-TERRY-ROLL70-EXIT`** *"WAL OFFICIAL CLOSE ≥ $81.90 on THREE CONSECUTIVE sessions"* — **0-of-3 as last recorded here** (REGINALD through 9/23, per TERRY STATUS 9/24; not re-read this pass). The option's +20.45% is not the gate — the gate reads WAL's close (rule 7). **$4.40 GTC sell order: CANCELLED / not there — Will 9/28** (`PROME/inbox/processed/2026-09-28_from-WAL_WQ-324-325-ruled-verbatim-and-4.40-GTC-cancelled.md`) ⇒ **no resting exit order; any take-profit is Will's manual act.** Time stop Fri 12/4. 78 DTE. **D-47** |
| **KRE $25P** | 1/15/2027 | 1 | $53.00 — card-derived ✓ | ≈$1.00 *(derived)* | ✅ **ON CARD 9/29 — −$52.00 / −98.11%** | Deep-OTM lottery; entry pre-7/16, never recorded — **D-54** (before the 9/01 activity view). 106 DTE |
| T | stock | 1 | — | — | ⚠️ no stocks card 9/29; no T row in RH activity 9/01→9/25 | Hypothesis: sold before 9/01, unconfirmed — **D-20**. The card no longer closes to the cent (D-64), so the 9/27 "no stock line" inference is weaker |

## Account UNATTRIBUTED — receipted fills not yet attributed to an account

*No rows. VLO ×1 (this section's only row since 9/19) moved to § Fidelity — Longs on the 9/25 ledger (D-55 account leg CLOSED). The section stays as the landing place for a receipt that names no account (the parser admits it — TERRY `cfd9b9115`).*

---

## ⚠️ Reconcile discrepancies (received 2026-10-20 ~10:43 ET; intraday marks; capture/quote/fill clocks UNKNOWN)

> Broker view > Will's word > desk record. October20 intraday marks are NOT closes. DTE from receipt date only; no current executable bids. All prior duties survive unless explicitly closed. Prior table/history = `git show ba1a41e09:FORGE/STATUS.md`, `git show 6fbf39cd0:FORGE/STATUS.md` and existing rotations. Permanently UNKNOWN WQ-167:9/2 USO135C sale price, never ask. This list records evidence and owners only; it carries no sell recommendation.

### Will supplies / PROME re-reads — facts owed

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| DATED | QQQ Oct20 719P ×1 · 715P ×1 | 🔴 expire TODAY10/20, 0 calendar DTE | Values $98/$37 `[10/20 intraday rcv]`; bases $277.66/$200.66; no contract-specific cards; the Oct20 720P was sold close 10/20 (+$474.66 DERIVED). Capture marks are not bids | Moneyness/exercise risk not verified without an underlying QQQ quote; no card/approval inferred | **Will** orders; **TERRY** recommends if asked; **PROME** records |
| **D-60** | Fidelity ITM-expiry handling | 🔴 next expiry TODAY10/20 | Policy never observed. If exercised: each QQQ put sells 100 shares at $719/$715 ($71,900/$71,500 per contract), mechanics only. No underlying QQQ quote supplied | Auto-liquidation timing/threshold, initiator and IRA short-stock handling UNKNOWN; no deterministic policy inferred | **Will** broker policy |
| DATED | QQQ Oct22 715P ×1 (NEW) · CRWV Oct23 56P ×1 · USO Oct23 163C ×1 | 🟠 2/3/3 calendar DTE | Bases $432.66/$179.66/$289.66; values $299/$45/$82. The 715P buy is broker-verified (row3); CRWV buy unseen (D-84). No contract-specific card/owner (D-77) | No thesis, roll linkage (720P→Oct22 715P) or management approval inferred from entry | **Will / TERRY**; PROME scope |
| DATED | USO Oct28 165C ×1 · CMG Oct30 28P ×1 · USO Oct30 165C ×2 | 🟡 8/10/10 calendar DTE | USO Oct30 165C now ×2, basis $586.32 = $270.66 + $315.66 (row1 broker-verified). No contract-specific card/owner (D-77) | Second lot not proof of a card or scale approval | **Will / TERRY**; PROME scope |
| **D-82** | Approved sells not evidenced | 🟠 WAL window ended10/19; OZK backstop 15:30 ET 10/20; TBT overdue evidence | PROME-supplied WQ-429 WAL65P4, WQ-428 OZK40P4, WQ-357 TBT5 SELL approvals. All still displayed in the 10/20 capture ($320/$40/$198.60); no sell fill in the five-row Pending crop | Working-order census incomplete; whether ordered/working/filled later UNKNOWN; approvals are not executions. Will 10/20 11:10 ET stated preference not to sell lines whose value has collapsed — recorded as context, not a ruling on these approvals | **Will** confirms orders/fills or disposition of approvals; **PROME** records |
| **D-85** | QQQ719P basis allocation | 🟠 expires today; record before any realized claim | 10/19: BTO2 net $554.32, STC1 net $224.34, displayed remaining basis $276.66. 10/20 display: remaining basis **$277.66** (+$1.00). If $277.66 is authoritative, removed basis $276.66 ⇒ conditional realized −$52.32; prior conditional −$53.32; equal allocation $277.16 ⇒ −$52.82 | Lot/basis adjustment or display re-allocation UNKNOWN; TERRY flags, not certified; no unconditional realized figure certified | **Will** broker lots; **PROME** preserves mismatch |
| **D-87** NEW | 10/19 capture marks vs Fidelity's prior-day reference | 🟡 record | For 10 option rows the 10/20 Today G/L differs from (10/20 value − 10/19 mirror value): 719P −$2 · 715P-Oct20 −$2 · CRWV −$3 · USO165C-Oct28 −$9 · USO163C −$14 · APO −$10 · OZK −$28 · WAL70P −$10 · WAL65P −$40 · ZION −$20; USO165C-Oct30 −$15 after the added lot. Six stock rows and five other option rows tie exactly | INFERRED: the 10/19 post-close capture marks were not Fidelity's prior-close reference marks (consistent with D-83 labeling). Nothing rebooked | **PROME** record |
| **D-86** | Three expired contracts absent | 🟠 outcome evidence owed | QQQ Oct15 715P, Oct16 735C, HBAN Oct16 16P absent; no resulting QQQ/HBAN stock visible | Sale/exercise/lapse/other disposal and realized UNKNOWN; cannot book full-basis losses or infer lapse | **Will** supplies earlier Activity; **PROME** records |
| **D-84** | Unseen entries and quantity changes (10/19) | 🟠 evidence before realized/scope | CRWV56P1 basis$179.66, Fidelity WAL70P2 $551.33, ZION62.5P2 $435.33: buys unseen. GLD20→24 residual2 basis$764.28 DERIVED; VLO2→3 added$444.73; USO37→35 removed$257.84; CMG2→1 removed$54.67. Unchanged by the 10/20 capture | Dates/gross prices/initiators and disposal methods/proceeds/realized UNKNOWN. Not proof of authority or roll linkage | **Will** earlier Activity/lots; **PROME** records |
| **D-78** | VLO extra-share scope | 🟠 scope before action | 3sh basis$1,296.73; third-share buy unseen; second-share scope already UNKNOWN. Original `GATE-TERRY-VLO-HELD-01` letter/WQ-386 and terminal scale instruction unchanged (Longs/GATES) | Neither added share extends original management scope or revives scale authority | **Will** authorization; **PROME/TERRY** scope |
| **D-80** | Prior unseen GLD+3 / HBAN−1 / QQQ Oct16 725P opening | 🟡 carried evidence | 10/15 gaps unchanged: GLD added basis$1,122.60; HBAN removed$95.67/proceeds unknown; QQQ725P sale net$769.32/opening basis unknown | Earlier fills remain outside the 10/19 and 10/20 crops; nothing resolved by later holdings | **Will** earlier Activity; **PROME** records |
| **D-76** | Detailed fills/lots behind historical and new results | 🟡 evidence | 10/20 720P round trip DERIVED +$474.66 (both legs broker-visible). 10/19 call round trips DERIVED +$27.69; QQQ712C net$739.32 and Oct21 700P net$91.34 proceeds only, realized UNKNOWN. Prior results stay historical | No broker realized-P/L report; D-85 conditional not certified. All fill clocks UNKNOWN (D-66) | **Will** lots/fills; **PROME/TERRY** integrate |
| **D-70** | Management mappings | 🟡 source changed — re-review owed | This file's bytes changed ⇒ every `position_management.tsv` mapping sourced to it is withheld until PROME re-reviews; Oct20 720P mapping (if any) now describes a CLOSED contract; Oct22 715P and the second USO Oct30 165C lot have no reviewed mapping | Mapping is not a card or trade approval | **PROME** mapping; **TERRY** cards |
| **D-77** | Off-thesis ownership/cards | 🟡 record; near expiry above | All eight off-thesis rows (incl. NEW Oct22 715P and the added USO Oct30 165C lot) plus KRE67P lack contract-specific owner/card/approval. Prior715P-Oct15/735C-Oct16 cards/outcomes remain historical duty | Grouping does not establish thesis or authorization | **PROME** scope; **Will/TERRY** |
| **D-74** | Fidelity bank-put thesis ownership / new-line scope | 🟡 record | Existing WAL65P4/OZK40P4 thesis ownership UNKNOWN; their management cards and SELL approvals are established by WQ-429/428 (D-82). Fidelity WAL70P2/ZION62.5P2 ownership/card/approval UNKNOWN; RH WAL70P1 separate | No inherited RH gate or new-line approval from same symbol/strike | **PROME** scope; **Will/TERRY** |
| **D-81** | Historical10/14 cash mismatch | 🟡 record | Prior mirror$14,027.08 was$16.58 above post-744P balance$14,010.50. 10/19 and 10/20 captures tie; historical mismatch unresolved | Different cut or unseen+$16.58 item UNVERIFIED | **PROME** record; **Will** broker detail if needed |
| **D-83** | Clock / Robinhood | 🟡 standing | Receipt10/20 ~10:43 ET, intraday; exact capture/quote/fill clocks UNKNOWN; marks not closes. Robinhood9/29 $295.15/BP$8.94 is 21 days old | RH positions may have moved; no inference | **Will** RH view when convenient; **PROME** records |
| **D-79** | Historical quote/value precision | 🟡 historical | Prior10/15 USO155.089×37=$5,738.293→$5,738.29; GLD380.3649×20=$7,607.298→$7,607.29. Current 23 values tie exactly | Prior10/13 1¢ truncation explanation still UNVERIFIED | **PROME** evidence |
| **D-75 · D-66 · D-69 · D-62 · D-63 · D-64 · D-65 · D-61 · D-59 · D-45 · D-55 · D-28 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1** | **Carried discrepancies (18) — every row still OPEN; rows verbatim → rotation 10/08 chunk D1 (D-75) + D2 (the other 17)** | 🟡 carried | None closed, re-dated or re-owned; every cell unchanged in the record. Ticker-bearing items, for the text scan: STNG (D-17) · RH QQQ $715P Aug-31 (D-28) · RH KRE $25P entry (D-54) · RH WAL $77.5P Aug-21 sale (D-18) · the RH T share (D-20) · AAPL 5-sh sale pre-7/30 (D-1) · D-75 (OZK 40P basis 1¢; mirror carries $322.65, record only) | Returns to this table when its state changes | As recorded, per row: **Will** — D-66 · D-69 · D-63 · D-64 · D-61 · D-59 · D-45 · D-55 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1; **RH history before 9/01** — D-28; **PROME** — D-62 · D-65 (re-reads of desktop-local images) · D-75 (record) |

*D-69 missing+$53.54 remains OPEN. D-66 includes10/19–20 fill clocks plus historical10/14–15 clocks/derived gross prices. D-71 broker leg remains CLOSED (cohort+$142.44, rotation10/15 chunk A); D-72/D-73 historical closures unchanged. No duty closed by silence.*

*Guards: D-47 RH WAL70P `GATE-TERRY-ROLL70-EXIT`, last recorded0-of-3, no resting exit, time stop12/4; REGINALD grades/TERRY proposes/Will harvests. That stale count is not a current reading. VLO original letter/terminal scale unchanged; extra-share scope D-78. WQ-200 USO stock no live rule. APD tag/adjustment unverified. Option P/L percentages are marks, not harvest/disarm readings; no gate adjudicated this pass.*

---

## Immediate Actions (10/20 intraday receipt; clocks UNKNOWN) — evidence and records only

| Item | State | Owner |
|---|---|---|
| 🔴 QQQ Oct20 719P/715P ×1 each expire today; no cards; D-60 ITM policy UNKNOWN | 0 calendar DTE | **Will** (his call) / **TERRY** if asked |
| 🟠 QQQ Oct22 715P; CRWV56P/USO163C Oct23; USO165C Oct28; CMG28P/USO165C×2 Oct30 — no contract-specific cards/ownership (D-77) | 2/3/3/8/10 calendar DTE | **Will/TERRY/PROME** |
| 🟠 D-82 approved WAL/OZK/TBT sales: no fill evidenced; D-86 absent expired contracts: disposal unseen | evidence | **Will**; **PROME** records |
| 🟠 D-85 QQQ719P basis now $277.66 (+$1.00); D-84 unseen 10/19 fills/qty changes; D-78 VLO extra-share scope | evidence/scope | **Will/PROME/TERRY** |
| 🟡 D-70 mapping re-review (source bytes changed); D-87 new; D-76/77/74/80/81/83 and 18 carried duties remain; D-69 missing+$53.54 | integration/evidence | **PROME/TERRY/Will** |

---

*History → `_archive/JOURNAL.md`, existing rotations and Git; immediately prior whole mirror = `git show ba1a41e09:FORGE/STATUS.md` | `PORTFOLIO.md` FROZEN Feb snapshot, never live | Truth = Will/broker off-repo | Current evidence → `PROME/data/2026-10-20_broker-capture-TRANSCRIPTION.md` + TERRY `AGENTS/TERRY/research/2026-10-20_broker-receipt/` (23 Fidelity positions, 5 Activity orders incl 2 Verified Canceled; received ~10:43 ET intraday; exact clocks UNKNOWN). Robinhood source remains9/29; prior evidence/history survives in Git.*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumers: `AGENTS/TERRY/scripts/positions_from_forge.py` (sections `^## (Fidelity|Robinhood)` + `^## Account <NAME>`; table headers by prefix; cell text — emphasis and strikethrough visible) · `PROME/tools/desk_attention.py` `holdings()` (same sections; `Qty` + `Ticker|Strike|Position` headers; expiry year from `**Updated:**`) · `PROME/tools/will_brief.py` `parse_money()` (header before the first `## `: `account total:**`, `money market):** $X (Y%)`, `**Updated:** YYYY-MM-DD`, `marks = [Fri ]YYYY-MM-DD`) · `FORGE/position_management.tsv` `source_sha256` (any byte change here withholds every mapping sourced to this file until PROME re-reviews) · `AGENTS/BRENT/scripts/pending_receipts.py` (text-level closure candidates). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself here in the same commit that starts parsing. *(Pass notes 9/27 → 10/8 → rotation 10/08 chunk G. Conventions they set, still binding: the header money line keeps the shape `will_brief.py` reads; option expiries carry the year; the `Mark <m/d>` header is prefix-bound; terminal records live in italic lines, which no parser reads as rows.)*
