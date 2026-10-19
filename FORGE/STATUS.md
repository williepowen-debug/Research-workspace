# FORGE — Trading Operations

Dashboard management mapping → [position_management.tsv](position_management.tsv); maintenance contract → [dashboard notes](DASHBOARD.md). Holdings remain in this file; approval, order and fill evidence are separate. A changed evidence source invalidates its management mapping until reviewed.

> ✅ **2026-10-19 (Mon) — RECONCILE BY ANVIL to Will's Fidelity positions + October19 Activity, received post-close; exact receipt/capture/mark/fill clocks UNKNOWN. These are October19 session marks, NOT certified closing marks or executable quotes.** Source `PROME/data/2026-10-19_broker-capture-TRANSCRIPTION.md` + `.json`; no post-snapshot events supplied. Independently verified **23/23** values and G/L to the cent: positions **$22,834.00** + cash **$18,574.21** − pending **$1,520.92** = **$39,887.29**. Against last mirror `6fbf39cd0`: **9 NEW / 4 QTY CHANGE / 10 MARK ONLY / 3 absent expired contracts** (disposal UNKNOWN).
>
> ⚠️ **ACCOUNT SCOPE — ONE Fidelity Traditional IRA; identifier redacted; continuity INFERRED, not independently verified. Robinhood Individual NOT provided: every 9/29 row remains unverified today; absence proves no closure. Activity is a crop of October19 orders ending after QQQ715P buy; earlier activity and a complete working-order census are UNSEEN.**
>
> **Updated:** 2026-10-19 · marks = 2026-10-19 session, clock UNKNOWN (all Fidelity cells `[10/19 rcv]` = `[broker export received 2026-10-19 post-close; capture/mark time UNKNOWN]`) · **Fidelity cash (money market):** $18,574.21 (46.57%) + **Pending activity −$1,520.92** · **Fidelity account total:** $39,887.29 (Today −$211.52 / −0.53%; open G/L +$181.06 / +0.80%; exact basis $22,652.94). Snapshot change vs10/15: **+$2,392.75 = positions +$4,418.89 + cash +$418.46 − pending $2,444.60**, not daily/realized return. Visible buys $3,001.59 − sells $1,480.67 = $1,520.92 debit, exactly pending; already included, never add again. Cash+pending $17,053.29 is not certified settled cash/buying power. **DERIVED realized: three complete QQQ Oct19 call round trips +$27.69; QQQ719P conditional −$53.32 has a $0.50 allocation mismatch (D-85), NOT certified. Other absent/reduced lines and unseen opening legs: realized UNKNOWN.** Robinhood $295.15 / BP$8.94 `[9/29 13:4x intraday]`, 20 days old. Prior tables/history remain in Git (`6fbf39cd0`) and existing rotations; no history rebooked.

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (its own header names the current base and amendment count). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All Fidelity marks `[10/19 rcv]`; capture/mark clocks UNKNOWN. Average costs/percentages displayed, not exact fills.*

| Ticker | Type | Qty | Cost | Mark 10/19 rcv | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | 4 | $23.65 | $342.94 | $1,371.76 | +$1,277.18 / +1350.37% | Today −$2.08; MARK ONLY; exact basis $94.58. Prior10/15 sale1 net$347.02 ⇒ DERIVED +$323.38; prior sales/lot gaps D-76/D-1 remain historical, not rebookable. |
| GLD | Stock | 24 | $375.81 | $379.69 | $9,112.56 | +$93.19 / +1.03% | Today −$53.65; QTY CHANGE20→24; basis $7,493.10→$9,019.37 (+$1,526.27). Visible10/19 buy2 @$380.99495 net$761.99; residual2 added basis$764.28 DERIVED, fill unseen (D-84). Prior GLD+3 fill gap D-80 survives. MIDAS; largest line. |
| USO | Stock | 35 | $121.90 | $160.81 | $5,628.35 | +$1,361.92 / +31.92% | Today −$33.25; QTY CHANGE37→35; basis$4,524.27→$4,266.43; removed$257.84 DERIVED; disposal/proceeds/realized UNKNOWN (D-84). **WQ-200 DECLINED9/10: NO harvest/give-back rule live; Will manages by hand.** BRENT thesis. |
| VLO | Stock | 3 | $432.24 | $433.31 | $1,299.93 | +$3.20 / +0.24% | Today −$34.20; QTY CHANGE2→3; basis$852→$1,296.73; added$444.73 DERIVED, fill unseen (D-84). **Additional-share authorization/management scope UNKNOWN (D-78); no scale approval inferred.** Original9/18 share @$412, fill clock D-55. Original held-share exit letter (condition AND consequence, incl. who acts) remains `GATE-TERRY-VLO-HELD-01` in `PROME/GATES.tsv`, amended WQ-38610/7. Remaining2-sh scale instruction WQ-213 remains STAND DOWN/TERMINAL under `GATE-TERRY-VLO-SCALE` (9/25 F1; optional CME source-① override unchanged). Gate reads crack/text, not stock mark. Prior10/12 added share net$440, gross/time gap D-76. No scope extension inferred. |
| APD | Stock | 2 | $294.79 | $298.65 | $597.30 | +$7.73 / +1.31% | Today −$1.88; MARK ONLY; exact basis$589.57. Historical10/1 D badge/$1.81 reference adjustment unverified; no dividend row supplied; thesis tag unassigned since7/30. |
| TBT | Stock | 5 | $34.40 | $40.62 | $203.10 | +$31.09 / +18.07% | Today $3.50; MARK ONLY; exact basis$172.01. **PROME-supplied WQ-357 SELL approved; 5 still held, sale NOT evidenced.** Prior10/12 sale5 net$210.40, DERIVED +$35.95 (D-76) historical. BOND/TERRY duration-short leg. |

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

*No live event-box rows — the VIX $20C/$25C spread (CLOSED 2026-07-30, realized −$111.60) and the five Aug-21-2026 EXPIRED rows (realized −$2,816.72 total) are terminal → rotation records.*

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, owned by no agent unless separately recorded. **SELL-OR-ROLL before expiry** (`USER.md`, 9/30 19:03 ET); TERRY recommends, Will orders. The capture establishes holdings/fills, not contract-specific cards or approvals; grouping is navigation, not a thesis or scope ruling. Last marks are not executable bids; working orders UNKNOWN. Receipt-day DTE is scheduling only; broker capture time UNKNOWN.

| Ticker | Strike | Expiry | Qty | Cost | Mark 10/19 rcv | Value | P&L | Note |
|--------|--------|--------|-----|------|---------------|-------|-----|------|
| QQQ | $720P | Oct-20-2026 | 1 | $1.91 | $3.84 | $384.00 | +$193.34 / +101.40% | `[10/19 rcv]`; basis $190.66; Today $193.34. NEW; BOUGHT OPEN10/19 @$1.90 ×1 net−$190.66. SELL-OR-ROLL before expiry; card/owner/approval UNKNOWN (D-77). |
| QQQ | $719P | Oct-20-2026 | 1 | $2.77 | $3.37 | $337.00 | +$60.34 / +21.81% | `[10/19 rcv]`; basis $276.66; Today $60.34. NEW; BOUGHT OPEN10/19 @$2.765 ×2 net−$554.32. Sold1 @$2.25 net$224.34; remaining basis authoritative; allocation mismatch D-85. SELL-OR-ROLL before expiry; card/owner/approval UNKNOWN (D-77). |
| USO | $165C | Oct-30-2026 | 1 | $2.71 | $3.20 | $320.00 | +$49.34 / +18.22% | `[10/19 rcv]`; basis $270.66; Today $49.34. NEW; BOUGHT OPEN10/19 @$2.70 ×1 net−$270.66. SELL-OR-ROLL before expiry; card/owner/approval UNKNOWN (D-77). |
| QQQ | $715P | Oct-20-2026 | 1 | $2.01 | $1.96 | $196.00 | −$4.66 / -2.33% | `[10/19 rcv]`; basis $200.66; Today −$4.66. NEW; BOUGHT OPEN10/19 @$2.00 ×1 net−$200.66. SELL-OR-ROLL before expiry; card/owner/approval UNKNOWN (D-77). |
| CMG | $28P | Oct-30-2026 | 1 | $0.55 | $0.45 | $45.00 | −$9.66 / -17.68% | `[10/19 rcv]`; basis $54.66; Today −$12.00. QTY CHANGE2→1; removed basis$54.67 DERIVED; proceeds/method/realized UNKNOWN (D-84). Prior10/14 limit sell was CANCELED, not proof of this disposal. SELL-OR-ROLL before expiry; card/owner/approval UNKNOWN (D-77). |
| CRWV | $56P | Oct-23-2026 | 1 | $1.80 | $0.93 | $93.00 | −$86.66 / -48.24% | `[10/19 rcv]`; basis $179.66; Today −$46.00. NEW; buy fill/date unseen (D-84). SELL-OR-ROLL before expiry; card/owner/approval UNKNOWN (D-77). |
| USO | $165C | Oct-28-2026 | 1 | $3.36 | $2.58 | $258.00 | −$77.66 / -23.14% | `[10/19 rcv]`; basis $335.66; Today −$77.66. NEW; BOUGHT OPEN10/19 @$3.35 ×1 net−$335.66. SELL-OR-ROLL before expiry; card/owner/approval UNKNOWN (D-77). |
| USO | $163C | Oct-23-2026 | 1 | $2.90 | $2.01 | $201.00 | −$88.66 / -30.61% | `[10/19 rcv]`; basis $289.66; Today −$88.66. NEW; BOUGHT OPEN10/19 @$2.89 ×1 net−$289.66. SELL-OR-ROLL before expiry; card/owner/approval UNKNOWN (D-77). |

*QQQ Oct15 715P ×1, Oct16 735C ×1 and HBAN Oct16 16P ×1 are ABSENT after expiry: actual sale/exercise/lapse and realized UNKNOWN (D-86); no resulting QQQ/HBAN shares visible. Absence does not establish worthless expiry.*

*October19 QQQ call round trips (broker fills; DERIVED realized):725C $1.99−$98.66=−$96.67;721C $313.34−$133.66=+$179.68;720C $110.34−$165.66=−$55.32; total+$27.69. Three canceled orders excluded. QQQ712C sale net$739.32 and Oct21 700P sale net$91.34: opening bases unseen, realized UNKNOWN. No roll linkage inferred.*

*Prior terminal records and prior derived realizations remain historical in `git show 6fbf39cd0:FORGE/STATUS.md` and existing rotations; QQQ Oct16 725P opening basis remains UNKNOWN (D-80); no prior result rebooked.*

*QQQ Oct-15 740P ×3 **SOLD CLOSE 10/14** — three Activity rows net +$1,220.31 / +$1,155.31 / +$1,099.31 = $3,474.93 − remaining basis $1,591.99 ⇒ DERIVED realized +$1,882.94. Cohort: bought 4 10/2 net −$2,122.65; all proceeds $670.32 + $3,474.93 = $4,145.25 ⇒ +$2,022.60, of which +$139.66 (the first sale) was already on the 10/14 mirror — never add the partial and the cohort together. Gross fills DERIVED from the ~$0.69/contract fee pattern ≈ $12.21 / $11.56 / $11.00 (the first, $6.71, is broker-stated); times UNKNOWN (D-66). ⛔ No contract remained for today's expiry — `MGMT-QQQ740P-OCT15` SPENT; no exercise/assignment outcome. These proceeds posted to the cash-balance column on 10/14, not to pending.*
*USO Oct-14 150C ×2 **SOLD CLOSE 10/14** — two Activity rows net +$354.34 + $406.34 = $760.68 − basis $375.33 ⇒ DERIVED realized +$385.35 (gross ≈ $3.55 / $4.07 DERIVED; times UNKNOWN). Will's 10/14 word "i sold before close" is now broker-CONFIRMED. Expiry task retired; no exercise outcome. Distinct from the 37 shares and the closed Oct-09 call; no roll linkage inferred.*

## Fidelity — Thesis Puts

*Instrument grouping is navigation, not approval: the Fidelity WAL/OZK rows below are Will-direct holdings (bought 10/7, Activity); thesis/desk ownership and management approval are NOT established by the broker view.*

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

*TLT $77P Sep-30 ×15 (TRY-FIRE-004's last lot): SOLD TO CLOSE 9/30 ⇒ −$154.64; no replacement TLT line; detail → rotation 10/01 chunk D.*

*TLT Oct-16 $82P remaining1 **SOLD CLOSE10/12** net$400.34−remaining basis$167.67=realized+$232.67. Prior9/28 partial1-of-2 sale@$3.60⇒+$191.66 remains separately booked. WQ-357 LATER10/3 pathC and `MGMT-TLT82P-OCT16`/WQ-302 Wed10/14 clock are historical management duties: disposal now evidenced, no current TLT holding asserted; PROME/TERRY integrate decision records. BOND research delivered10/5 (`ff0992bf1`) was not a new trade ruling. Prior2.50× mark multiple never a price trigger. D-60 future ITM handling remains UNKNOWN.*

### KRE — regional banks (REGINALD)

*All four rows `[10/19 rcv]`; MARK ONLY; grouping is not approval/ownership. Prior Sep30 roll/exits remain historical in Git/rotation10/01 chunk D.*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $67P | Nov-27-2026 | 4 | $1.28 | $1.27 | $508.00 | −$2.65 / -0.52%; basis $510.65; Today $0.00; MARK ONLY `[10/19 rcv]`; bought10/12 net$510.65; gross/time/card/owner UNKNOWN (D-76/D-77) |
| $60P | Dec-18-2026 | 2 | $2.57 | $0.45 | $90.00 | −$423.34 / -82.47%; basis $513.34; Today −$10.00; MARK ONLY `[10/19 rcv]` |
| $60P | Dec-18-2026 | 3 (M) | $2.93 | $0.45 | $135.00 | −$743.02 / -84.63%; basis $878.02; Today −$15.00; MARK ONLY `[10/19 rcv]`; multi-lot marker; total5 Dec18 60P across2lots |
| $65P | Dec-31-2026 | 2 | $1.69 | $1.37 | $274.00 | −$63.33 / -18.78%; basis $337.33; Today $2.00; MARK ONLY `[10/19 rcv]`; `MGMT-KRE65P-DEC31`: hard stop Thu12/31 15:00 ET (5ce609f80), not price gate |

### WAL (REGINALD) — Sep-18 pair EXPIRED

*$70P + $67.5P Sep-18 ×1 each: **EXPIRED as of 9/18, broker-confirmed** (ledger rows posted 9/21) ⇒ realized **−$768.67 and −$750.67 = −$1,519.34** (full basis) — the WQ-168 ①② LAPSE as ruled. Rows → rotation record. Duration roll = the Robinhood WAL Dec-18 $70P ×1 below. The RH WAL $77.5P Aug-21 sale: P&L UNRECORDED — D-18.*

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18-2026 | 1 | $11.85 | $1.70 | $170.00 | −$1,014.67 / -85.66% | `[10/19 rcv]`; basis $1,184.67; Today $5.00. MARK ONLY; BROCK vehicle; HOLD ruled8/13 (private-credit batch §②), vehicle-mismatch flag live. |
| OZK | $40P | Nov-20-2026 | 4 | $0.81 | $0.25 | $100.00 | −$222.65 / -69.01% | `[10/19 rcv]`; basis $322.65; Today −$12.00. MARK ONLY; bought10/7 (Activity). PROME-supplied WQ-428 SELL approved;4 still held; sale NOT evidenced; order census incomplete (D-82). Thesis ownership UNKNOWN (D-74); management cards/SELL approvals established by WQ-428/429 (D-82). |
| WAL | $70P | Dec-18-2026 | 2 | $2.76 | $2.70 | $540.00 | −$11.33 / -2.06% | `[10/19 rcv]`; basis $551.33; Today −$10.00. NEW; buy fill/date unseen (D-84); ownership/card/approval UNKNOWN (D-74). **Fidelity2 is DISTINCT from Robinhood1; no inherited RH gate.** |
| WAL | $65P | Dec-18-2026 | 4 | $1.71 | $1.40 | $560.00 | −$122.65 / -17.97% | `[10/19 rcv]`; basis $682.65; Today −$100.00. MARK ONLY; bought10/7 (Activity). PROME-supplied WQ-429 SELL approved;4 still held; sale NOT evidenced; order census incomplete (D-82). Thesis ownership UNKNOWN (D-74); management cards/SELL approvals established by WQ-428/429 (D-82). |
| ZION | $62.5P | Nov-20-2026 | 2 | $2.18 | $2.05 | $410.00 | −$25.33 / -5.82% | `[10/19 rcv]`; basis $435.33; Today −$24.00. NEW; buy fill/date unseen (D-84); ownership/card/approval UNKNOWN (D-74). |


## Robinhood — satellite account (Individual)

*All holdings/figures below retained from the 9/29 source; carried DTE annotations are historical, not a current freshness assertion.*

> ⚠️ **NOT CAPTURED IN THIS 10/19 RECEIPT (nor 10/14, 10/13, 10/11, 10/7, 10/1 or 9/30 — 20 days since the 9/29 card) — every cell below is the 9/29 card, unverified today.** 9/29 card: **account $295.15, BP $8.94** `[9/29 13:4x intraday]`; lines + BP = $290.15 ⇒ **$5.00 UNEXPLAINED (D-64)**. Per-line cost/value DERIVED from P/L ÷ P/L% (no Mark column ⇒ machine class `unverified` by design). The prediction-market line and the 9/01→9/25 dead-by-date bookings — USO $159C Sep-11 (bought 9/10, expired $0 — D-58) · QQQ $713C Sep-16 + USO $165C Sep-16 (both expired $0 — D-57) — verbatim → rotation 10/08 chunk B.

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **WAL $70P** | **Dec-18-2026** | 1 | **$2.20 ($220)** — bought 9/02 @ $2.20 (RH activity) ✓ | ≈$265.00 *(derived; mark ≈$2.65)* | ✅ **ON CARD 9/29 — +$45.00 / +20.45%** | TRY-WAL-ROLL70 (filled in Robinhood). Guard **`GATE-TERRY-ROLL70-EXIT`** *"WAL OFFICIAL CLOSE ≥ $81.90 on THREE CONSECUTIVE sessions"* — **0-of-3 as last recorded here** (REGINALD through 9/23, per TERRY STATUS 9/24; not re-read this pass). The option's +20.45% is not the gate — the gate reads WAL's close (rule 7). **$4.40 GTC sell order: CANCELLED / not there — Will 9/28** (`PROME/inbox/processed/2026-09-28_from-WAL_WQ-324-325-ruled-verbatim-and-4.40-GTC-cancelled.md`) ⇒ **no resting exit order; any take-profit is Will's manual act.** Time stop Fri 12/4. 78 DTE. **D-47** |
| **KRE $25P** | 1/15/2027 | 1 | $53.00 — card-derived ✓ | ≈$1.00 *(derived)* | ✅ **ON CARD 9/29 — −$52.00 / −98.11%** | Deep-OTM lottery; entry pre-7/16, never recorded — **D-54** (before the 9/01 activity view). 106 DTE |
| T | stock | 1 | — | — | ⚠️ no stocks card 9/29; no T row in RH activity 9/01→9/25 | Hypothesis: sold before 9/01, unconfirmed — **D-20**. The card no longer closes to the cent (D-64), so the 9/27 "no stock line" inference is weaker |

## Account UNATTRIBUTED — receipted fills not yet attributed to an account

*No rows. VLO ×1 (this section's only row since 9/19) moved to § Fidelity — Longs on the 9/25 ledger (D-55 account leg CLOSED). The section stays as the landing place for a receipt that names no account (the parser admits it — TERRY `cfd9b9115`).*

---

## ⚠️ Reconcile discrepancies (received 2026-10-19 post-close; capture/mark/fill clocks UNKNOWN)

> Broker view > Will's word > desk record. October19 session marks are NOT certified closes. DTE from receipt only; no current executable bids. All prior duties survive unless explicitly closed. Prior table/history = `git show 6fbf39cd0:FORGE/STATUS.md` and existing rotations. Permanently UNKNOWN WQ-167:9/2 USO135C sale price, never ask.

### Will supplies / PROME re-reads — facts owed

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| DATED | QQQ Oct20 720P/719P/715P ×1 each | 🔴 expire TOMORROW10/20,1 calendar DTE | Values$384/$337/$196; bases$190.66/$276.66/$200.66. SELL-OR-ROLL before expiry, no cards; capture marks are not bids | Moneyness/exercise risk not verified without underlying quote. No card/approval inferred | **Will** orders; **TERRY** recommends; **PROME** records |
| DATED | CRWV Oct23 56P ×1 · USO Oct23 163C ×1; USO Oct28 165C ×1; CMG Oct30 28P ×1 / USO Oct30 165C ×1 | 🟠 4/9/11 calendar DTE | SELL-OR-ROLL rail applies to every option; no contract-specific card/owner established (D-77) | No thesis, roll linkage or management approval inferred from entry | **Will / TERRY**; PROME scope |
| **D-60** | Fidelity ITM-expiry handling | 🔴 next expiry10/20 | Policy never observed. If exercised: QQQ puts sell100 shares at$720/$719/$715 ($72,000/$71,900/$71,500 per contract), mechanics only. No underlying QQQ quote supplied | Auto-liquidation timing/threshold, initiator and IRA short-stock handling UNKNOWN; no deterministic policy inferred | **Will** broker policy |
| **D-86** NEW | Three expired contracts absent | 🟠 outcome evidence owed | QQQ Oct15 715P, Oct16 735C, HBAN Oct16 16P absent; no resulting QQQ/HBAN stock visible | Sale/exercise/lapse/other disposal and realized UNKNOWN; cannot book full-basis losses or infer lapse against standing sell-or-roll practice | **Will** supplies earlier Activity; **PROME** records |
| **D-82** | Approved sells not evidenced | 🟠 WAL10/19 / OZK10/20 clocks; TBT overdue evidence | PROME-supplied WQ-429 WAL65P4 SELL before10/19; WQ-428 OZK40P4 SELL before10/20; WQ-357 TBT5 SELL approved. All remain held in capture ($560/$100/$203.10); no sell fill supplied | Working-order census incomplete; whether ordered/filled later UNKNOWN; approvals are not executions | **Will** confirms orders/fills; **PROME** records |
| **D-84** NEW | Unseen entries and quantity changes | 🟠 evidence before realized/scope | New CRWV56P1 basis$179.66, Fidelity WAL70P2 $551.33, ZION62.5P2 $435.33: buys unseen. GLD20→24 basis+$1,526.27, visible buy2 $761.99 ⇒ residual2 basis$764.28 DERIVED; VLO2→3 added$444.73; USO37→35 removed$257.84; CMG2→1 removed$54.67 | Dates/gross prices/initiators and disposal methods/proceeds/realized UNKNOWN. Basis bridges assume no unseen adjustment. Not proof of authority or roll linkage | **Will** earlier Activity/lots; **PROME** records |
| **D-85** NEW | QQQ719P basis allocation | 🟠 reconcile before realized claim | BTO2 net$554.32, STC1 net$224.34, remaining authoritative basis$276.66. Removed basis DERIVED$277.66 ⇒ conditional realized−$53.32. Equal allocation$277.16 ⇒−$52.82: $0.50 discrepancy | Lot/basis adjustment or display allocation UNKNOWN; no unconditional realized figure certified | **Will** broker lots; **PROME** preserves mismatch |
| **D-78** | VLO extra-share scope | 🟠 scope before action | Now3sh basis$1,296.73; new third-share buy unseen; second-share scope already UNKNOWN. Original `GATE-TERRY-VLO-HELD-01` letter/WQ-386 and terminal scale instruction unchanged (Longs/GATES) | Neither added share extends original management scope or revives scale authority | **Will** authorization; **PROME/TERRY** scope |
| **D-80** | Prior unseen GLD+3 / HBAN−1 / QQQ Oct16 725P opening | 🟡 carried evidence | 10/15 gaps unchanged: GLD added basis$1,122.60; HBAN removed$95.67/proceeds unknown; QQQ725P sale net$769.32/opening basis unknown | Earlier fills remain outside10/19 crop; nothing resolved by later holdings | **Will** earlier Activity; **PROME** records |
| **D-76** | Detailed fills/lots behind historical and new results | 🟡 evidence | Three fully visible Oct19 call round trips DERIVED +$27.69; QQQ712C net$739.32 and Oct21 700P net$91.34 proceeds only, basis/realized UNKNOWN. Prior10/12–15 derived results/lot assumptions stay historical, not rebooked | No broker realized-P/L report; D-85 conditional result not certified. All fill clocks UNKNOWN (D-66) | **Will** lots/fills; **PROME/TERRY** integrate |
| **D-70** | Management mappings reviewed October19 | Receipt re-review COMPLETE; cards remain owed | PROME refreshed changed rows and nine new contracts; source hashes verified; TERRY C5 packet delivered to inbox, acceptance not established | Mapping is not a card or trade approval; missing unchanged-line coverage remains explicit | **PROME** mapping; **TERRY** cards |
| **D-77** | Off-thesis ownership/cards | 🟡 record; near expiry above | New QQQ/USO calls/CRWV, reduced CMG, prior KRE67P lack contract-specific owner/card/approval. Prior715P-Oct15/735C-Oct16 cards/outcomes remain historical duty | Grouping does not establish thesis or authorization | **PROME** scope; **Will/TERRY** |
| **D-74** | Fidelity bank-put thesis ownership / new-line scope | 🟡 record | Existing WAL65P4/OZK40P4 thesis ownership UNKNOWN; their management cards and SELL approvals ARE established by WQ-429/428 (D-82). New Fidelity WAL70P2/ZION62.5P2 ownership/card/approval UNKNOWN; RH WAL70P1 separate | No inherited RH gate or new-line approval from same symbol/strike | **PROME** scope; **Will/TERRY** |
| **D-81** | Historical10/14 cash mismatch | 🟡 record | Prior mirror$14,027.08 was$16.58 above post-744P balance$14,010.50; prior Activity reproduced$12,428.50→$18,155.75. Current capture ties, does not resolve historical mismatch | Different cut or unseen+$16.58 item UNVERIFIED | **PROME** record; **Will** broker detail if needed |
| **D-83** | Clock / Robinhood | 🟡 standing | Receipt10/19 post-close, exact clocks UNKNOWN; session marks not certified closes. Robinhood9/29 $295.15/BP$8.94 is20days old | RH positions may have moved; no inference | **Will** RH view when convenient; **PROME** records |
| **D-79** | Historical quote/value precision | 🟡 historical | Prior10/15 USO155.089×37=$5,738.293→$5,738.29; GLD380.3649×20=$7,607.298→$7,607.29. Current23 values tie exactly | Prior10/13 1¢ truncation explanation still UNVERIFIED | **PROME** evidence |
| **D-75 · D-66 · D-69 · D-62 · D-63 · D-64 · D-65 · D-61 · D-59 · D-45 · D-55 · D-28 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1** | **Carried discrepancies (18) — every row still OPEN; rows verbatim → rotation 10/08 chunk D1 (D-75) + D2 (the other 17)** | 🟡 carried | None closed, re-dated or re-owned; every cell unchanged in the record. Ticker-bearing items, for the text scan: STNG (D-17) · RH QQQ $715P Aug-31 (D-28) · RH KRE $25P entry (D-54) · RH WAL $77.5P Aug-21 sale (D-18) · the RH T share (D-20) · AAPL 5-sh sale pre-7/30 (D-1) · D-75 (OZK 40P basis 1¢; mirror carries $322.65, record only) | Returns to this table when its state changes | As recorded, per row: **Will** — D-66 · D-69 · D-63 · D-64 · D-61 · D-59 · D-45 · D-55 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1; **RH history before 9/01** — D-28; **PROME** — D-62 · D-65 (re-reads of desktop-local images) · D-75 (record) |

*D-69 missing+$53.54 remains OPEN. D-66 includes10/19 fill clocks plus historical10/14–15 clocks/derived gross prices. D-71 broker leg remains CLOSED (cohort+$142.44, rotation10/15 chunk A); D-72/D-73 historical closures unchanged. No duty closed by silence.*

*Guards: D-47 RH WAL70P `GATE-TERRY-ROLL70-EXIT`, last recorded0-of-3, no resting exit, time stop12/4; REGINALD grades/TERRY proposes/Will harvests. That stale count is not a current reading. VLO original letter/terminal scale unchanged; extra-share scope D-78. WQ-200 USO stock no live rule. APD tag/adjustment unverified. Option P/L percentages are marks, not harvest/disarm readings; no gate adjudicated this pass.*

---

## Immediate Actions (10/19 post-close receipt; session marks, clocks UNKNOWN)

| Item | State | Owner |
|---|---|---|
| 🔴 QQQ Oct20 720P/719P/715P ×1 each — SELL-OR-ROLL before expiry; no cards; D-60 ITM policy UNKNOWN | 1 calendar DTE | **Will** orders / **TERRY** recommends |
| 🟠 CRWV56P/USO163C Oct23; USO165C Oct28; CMG28P/USO165C Oct30 — contract-specific cards/ownership needed | 4/9/11 calendar DTE | **Will/TERRY/PROME** |
| 🟠 D-86 absent expired contracts: supply actual disposal; D-82 approved WAL/OZK/TBT sales still not evidenced | evidence | **Will**; **PROME** records |
| 🟠 D-84 unseen fills/quantity changes; D-85 QQQ719P $0.50 allocation mismatch; D-78 VLO extra-share scope UNKNOWN | evidence/scope | **Will/PROME/TERRY** |
| 🟡 D-70 mapping re-review; D-76/77/74/80/81/83 and18 carried duties remain; D-69 missing+$53.54 | integration/evidence | **PROME/TERRY/Will** |

---

*History → `_archive/JOURNAL.md`, existing rotations and Git; immediately prior whole mirror = `git show 6fbf39cd0:FORGE/STATUS.md` | `PORTFOLIO.md` FROZEN Feb snapshot, never live | Truth = Will/broker off-repo | Current evidence → `PROME/data/2026-10-19_broker-capture-TRANSCRIPTION.md` + `.json` (23 Fidelity positions,19 Activity orders incl3canceled; received post-close; exact clocks UNKNOWN). Robinhood source remains9/29; prior evidence/history survives in Git.*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumers: `AGENTS/TERRY/scripts/positions_from_forge.py` (sections `^## (Fidelity|Robinhood)` + `^## Account <NAME>`; table headers by prefix; cell text — emphasis and strikethrough visible) · `PROME/tools/desk_attention.py` `holdings()` (same sections; `Qty` + `Ticker|Strike|Position` headers; expiry year from `**Updated:**`) · `PROME/tools/will_brief.py` `parse_money()` (header before the first `## `: `account total:**`, `money market):** $X (Y%)`, `**Updated:** YYYY-MM-DD`, `marks = [Fri ]YYYY-MM-DD`) · `FORGE/position_management.tsv` `source_sha256` (any byte change here withholds every mapping sourced to this file until PROME re-reviews) · `AGENTS/BRENT/scripts/pending_receipts.py` (text-level closure candidates). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself here in the same commit that starts parsing. *(Pass notes 9/27 → 10/8 → rotation 10/08 chunk G. Conventions they set, still binding: the header money line keeps the shape `will_brief.py` reads; option expiries carry the year; the `Mark <m/d>` header is prefix-bound; terminal records live in italic lines, which no parser reads as rows.)*
