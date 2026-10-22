# FORGE — Trading Operations

Dashboard management mapping → [position_management.tsv](position_management.tsv); maintenance contract → [dashboard notes](DASHBOARD.md). Holdings remain in this file; approval, order and fill evidence are separate. A changed evidence source invalidates its management mapping until reviewed.

> ✅ **2026-10-22 (Thu) — RECONCILE BY ANVIL to Will's Fidelity positions + Activity & Orders, pasted 11:01 ET (Will's stated clock; the quote clock is not displayed). These are October22 INTRADAY session marks, NOT closes and NOT executable quotes.** Source `PROME/data/2026-10-22_broker-capture-TRANSCRIPTION.md` (PROME transcription of two images; no TERRY read exists for this capture). Post-snapshot events: none beyond the capture's own ledger (all broker-verified, transcription § ③). ANVIL independently verified **25/25** row values, open G/L and basis to the cent: positions **$22,399.20** + cash **$15,807.97** + pending **+$1,668.89** = **$39,876.06** = displayed total. Against last mirror `100c63edc` (10/20 intraday, 23 rows): **5 NEW / 1 QTY CHANGE / 3 GONE (2 broker-verified closes, 1 disposition NOT evidenced, D-88) / 19 MARK ONLY**; 3 between-captures round trips (never mirror rows) booked as history below.
>
> ⚠️ **ACCOUNT SCOPE — ONE Fidelity Traditional IRA (•1326 on file; identifier obscured in the capture; continuity INFERRED, not independently verified). Robinhood Individual NOT provided: every 9/29 row remains unverified today; absence proves no closure. Activity = Orders page 1 of 2 (10 of 11 orders shown) + the "Past 30 days" ledger back to the 10/20 QQQ 719P liquidation; anything earlier and the 11th order are UNSEEN.**
>
> **Updated:** 2026-10-22 · marks = 2026-10-22 intraday, 11:01 ET per Will (all Fidelity cells `[10/22 11:01 ET intraday rcv]` = `[broker export received 2026-10-22 11:01 ET, Will's stated clock; quote clock not displayed; intraday, not a close]`) · **Fidelity cash (money market):** $15,807.97 (39.64%) + **Pending activity +$1,668.89** · **Fidelity account total:** $39,876.06 (Today −$797.28 / −1.96%; open G/L −$1,659.13 / −6.90%; exact basis $24,058.33). Snapshot change vs 10/20: **+$2,035.15 = positions +$1,528.58 + cash −$1,245.32 + pending +$1,751.89**, not a daily/realized return. Cash continuity: ledger balance after the last 10/21 row $15,807.97 = displayed cash ✓. Pending = the eight 10/22 "Processing" rows: sells $3,067.94 − buys $1,399.05 = +$1,668.89 exactly; already included, never add again. Cash+pending $17,476.86 is not certified settled cash/buying power. Cash bridge 10/20 capture → 10/20 ledger close leaves **+$17.34 unexplained (D-88)**. **DERIVED realized, five lines closed since the 10/20 mirror: +$1,537.62, or +$1,536.62 on the 10/20 display basis (D-85); allocation-independent: four lines +$1,605.29 and the QQQ 719P cohort −$120.99. Not a broker realized-P/L report.** Robinhood $295.15 / BP$8.94 `[9/29 13:4x intraday]`, 23 days old. Prior tables/history remain in Git (`100c63edc`, `ba1a41e09`, `6fbf39cd0`) and existing rotations; no history rebooked.

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (its own header names the current base and amendment count). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All Fidelity marks `[10/22 11:01 ET intraday rcv]`; quote clock not displayed. Cost = basis ÷ qty (DERIVED); Mark = the displayed last (value = last × qty, verified); not exact fills.*

| Ticker | Type | Qty | Cost | Mark 10/22 11:01 ET intraday rcv | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | 4 | $23.65 | $344.195 | $1,376.78 | +$1,282.20 / +1355.67% | Today +$0.82; MARK ONLY; exact basis $94.58. Prior10/15 sale1 net$347.02 ⇒ DERIVED +$323.38; prior sales/lot gaps D-76/D-1 remain historical, not rebookable. |
| GLD | Stock | 25 | $375.63 | $372.08 | $9,302.00 | −$88.78 / -0.95% | Today −$164.21; **QTY CHANGE 24→25:** BOUGHT 1 on 10/22 @$371.4109, net −$371.41 (order + ledger, broker-verified; fill clock UNKNOWN); exact basis $9,019.37 + $371.41 = $9,390.78 ✓ ties to the displayed basis. 10/19 residual2 fill unseen (D-84); prior GLD+3 gap D-80 survives. MIDAS; largest line. |
| USO | Stock | 35 | $121.90 | $160.87 | $5,630.45 | +$1,364.02 / +31.97% | Today +$37.45; MARK ONLY; exact basis $4,266.43. 10/19 37→35 disposal/proceeds/realized UNKNOWN (D-84). **WQ-200 DECLINED9/10: NO harvest/give-back rule live; Will manages by hand** — the +31.97% is a mark, not a gate reading. BRENT thesis. |
| VLO | Stock | 3 | $432.24 | $420.02 | $1,260.06 | −$36.67 / -2.83% | Today −$50.19; MARK ONLY; exact basis $1,296.73; broker "E" (earnings) badge shown. 10/19 third-share fill unseen (D-84). **Additional-share authorization/management scope UNKNOWN (D-78); no scale approval inferred.** Original9/18 share @$412, fill clock D-55. Original held-share exit letter (condition AND consequence, incl. who acts) remains `GATE-TERRY-VLO-HELD-01` in `PROME/GATES.tsv`, amended WQ-38610/7. Remaining2-sh scale instruction WQ-213 remains STAND DOWN/TERMINAL under `GATE-TERRY-VLO-SCALE` (9/25 F1; optional CME source-① override unchanged). Gate reads crack/text, not stock mark. Prior10/12 added share net$440, gross/time gap D-76. No scope extension inferred. |
| APD | Stock | 2 | $294.79 | $304.055 | $608.11 | +$18.54 / +3.14% | Today +$2.79; MARK ONLY; exact basis$589.57. Historical10/1 D badge/$1.81 reference adjustment unverified; no dividend row supplied; thesis tag unassigned since7/30. |
| TBT | Stock | 5 | $34.40 | $38.76 | $193.80 | +$21.79 / +12.66% | Today −$5.30; MARK ONLY; exact basis$172.01. PROME-supplied WQ-357 SELL approved; 5 still held at 10/22 11:01 ET; no sell order among the 10 visible orders (D-82). Prior10/12 sale5 net$210.40, DERIVED +$35.95 (D-76) historical. BOND/TERRY duration-short leg. |

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

*No live event-box rows — the VIX $20C/$25C spread (CLOSED 2026-07-30, realized −$111.60) and the five Aug-21-2026 EXPIRED rows (realized −$2,816.72 total) are terminal → rotation records.*

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, owned by no agent unless separately recorded. **Will manages his own expiries** (`USER.md` § No expiry nagging, 10/20 11:32 ET; supersedes the 9/30 sell-or-roll rail as an instruction): no expiry reminders or sell pushes, and a collapsed line may expire. This mirror records holdings and evidence only; dispositions are read from his captures, never inferred. The capture establishes holdings/fills, not contract-specific cards or approvals; grouping is navigation, not a thesis or scope ruling. Last marks are not executable bids; working orders UNKNOWN. Receipt-day DTE is scheduling only.

| Ticker | Strike | Expiry | Qty | Cost | Mark 10/22 11:01 ET intraday rcv | Value | P&L | Note |
|--------|--------|--------|-----|------|---------------|-------|-----|------|
| QQQ | $717C | Oct-22-2026 | 1 | $1.55 | $0.38 | $38.00 | −$116.66 / -75.43% | `[10/22 11:01 ET intraday rcv]`; basis $154.66; Today −$116.66. NEW; BOUGHT OPEN 10/22 @$1.54 ×1 net −$154.66 (order + ledger, broker-verified; fill clock UNKNOWN; a $1.52 limit was Verified Canceled). Expires 10/22, the capture day. Broker "Last chg −8.31" is displayed but inconsistent with a $0.38 last; mark taken from the last, which ties to value. Card/owner/approval UNKNOWN (D-77). |
| CRWV | $56P | Oct-23-2026 | 1 | $1.80 | $0.98 | $98.00 | −$81.66 / -45.46% | `[10/22 11:01 ET intraday rcv]`; basis $179.66; Today +$62.00. MARK ONLY; buy fill/date unseen (D-84). Card/owner/approval UNKNOWN (D-77). |
| USO | $163C | Oct-23-2026 | 1 | $2.90 | $0.99 | $99.00 | −$190.66 / -65.83% | `[10/22 11:01 ET intraday rcv]`; basis $289.66; Today −$29.00. MARK ONLY; bought open10/19 @$2.89. Card/owner/approval UNKNOWN (D-77). |
| QQQ | $710P | Oct-26-2026 | 1 | $4.58 | $7.83 | $783.00 | +$325.34 / +71.08% | `[10/22 11:01 ET intraday rcv]`; basis $457.66; Today +$325.34. NEW; BOUGHT OPEN 10/22 net −$457.66 (ledger, broker-verified; its order row is not on the visible page — INFERRED to be the 11th order; fill price/clock UNKNOWN). +71.08% is a mark; no harvest/disarm line is registered for this contract in this file. Card/owner/approval UNKNOWN (D-77). |
| USO | $165C | Oct-28-2026 | 1 | $3.36 | $2.29 | $229.00 | −$106.66 / -31.78% | `[10/22 11:01 ET intraday rcv]`; basis $335.66; Today −$6.00. MARK ONLY; bought open10/19 @$3.35. Card/owner/approval UNKNOWN (D-77). |
| USO | $165C | Oct-30-2026 | 2 | $2.93 | $3.10 | $620.00 | +$33.68 / +5.74% | `[10/22 11:01 ET intraday rcv]`; basis $586.32 = $270.66 (10/19 lot) + $315.66 (10/20 lot); Today +$28.00. MARK ONLY. Card/owner/approval UNKNOWN (D-77). |
| USO | $163C | Oct-30-2026 | 1 | $3.59 | $3.80 | $380.00 | +$21.34 / +5.94% | `[10/22 11:01 ET intraday rcv]`; basis $358.66; Today +$10.00. NEW; BOUGHT OPEN 10/21 net −$358.66 (ledger, broker-verified; fill price/clock UNKNOWN). Distinct from the Oct-23 163C; no roll linkage inferred. Card/owner/approval UNKNOWN (D-77). |
| CMG | $28P | Oct-30-2026 | 1 | $0.55 | $0.93 | $93.00 | +$38.34 / +70.14% | `[10/22 11:01 ET intraday rcv]`; basis $54.66; Today −$13.00. MARK ONLY; 10/19 2→1 disposal/proceeds/realized UNKNOWN (D-84). Card/owner/approval UNKNOWN (D-77). |

*Closed since the 10/20 mirror — broker ledger rows (transcription § ③); DERIVED realized, not a broker realized-P/L report; fill clocks UNKNOWN (D-66); no roll linkage inferred:* **QQQ Oct-22 715P ×1 SOLD CLOSE 10/22** @$7.31 net +$730.32 − basis $432.66 ⇒ **+$297.66**. **QQQ Oct-20 719P ×1 OPTION LIQUIDATION 10/20** +$208.99; cohort (10/19 BTO2 −$554.32, 10/19 STC1 +$224.34, this liquidation) ⇒ **−$120.99, allocation-independent**; this leg −$67.67 or −$68.67 (D-85). **QQQ Oct-20 715P ×1** (basis $200.66): absent; disposition NOT evidenced — the ledger view starts at the 10/20 719P liquidation; nothing booked, no worthless expiry inferred (D-88).
*Round trips between captures (never mirror rows; broker ledger):* QQQ Oct-21 715P bought 10/20 −$223.66, OPTION LIQUIDATION 10/21 +$1.99 ⇒ **−$221.67** · QQQ Oct-23 717P bought 10/21 −$373.66, sold 10/22 @$9.82 +$981.31 ⇒ **+$607.65** · QQQ Oct-26 720P bought 10/21 −$434.66, sold 10/22 @$13.57 +$1,356.31 ⇒ **+$921.65** (a $13.93 limit Verified Canceled). Five-line total +$1,537.62 / +$1,536.62 (D-85).

*Working order at capture, NOT a position: VLY Dec-18-2026 $12P ×1 buy-to-open, limit $0.15 (Day), status Open — not booked; a later capture books it only if it fills (D-89).*

*QQQ Oct15 715P ×1, Oct16 735C ×1 and HBAN Oct16 16P ×1 are ABSENT after expiry: actual sale/exercise/lapse and realized UNKNOWN (D-86); no resulting QQQ/HBAN shares visible. Absence does not establish worthless expiry.*

*Prior terminal records remain historical in Git: the 10/20 QQQ Oct-20 720P close (+$474.66) → `git show 100c63edc:FORGE/STATUS.md`; the 10/19 QQQ call round trips (+$27.69; 712C and Oct21 700P proceeds only) → `git show ba1a41e09:FORGE/STATUS.md`; QQQ Oct16 725P opening basis UNKNOWN (D-80). No prior result rebooked.*

*QQQ Oct-15 740P ×3 and USO Oct-14 150C ×2 **SOLD CLOSE 10/14** (DERIVED realized +$1,882.94 and +$385.35, booked on the 10/15 mirror — never add again) → rotation 10/22 chunk A, byte-exact.*

## Fidelity — Thesis Puts

*Instrument grouping is navigation, not approval: the Fidelity WAL/OZK rows below are Will-direct holdings (bought 10/7, Activity); thesis/desk ownership and management approval are NOT established by the broker view.*

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

*No live TLT line. Terminal records (TLT $77P Sep-30 ×15 sold close 9/30 ⇒ −$154.64; TLT Oct-16 $82P sold 9/28 and 10/12 ⇒ +$191.66 and +$232.67; WQ-357 and `MGMT-TLT82P-OCT16` historical) → rotation 10/22 chunk B, byte-exact.*

### KRE — regional banks (REGINALD)

*All six rows `[10/22 11:01 ET intraday rcv]`; four MARK ONLY, two NEW (10/22, broker-verified); grouping is not approval/ownership (D-74). Prior Sep30 roll/exits remain historical in Git/rotation10/01 chunk D.*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $66P | Nov-20-2026 | 3 | $0.45 | $0.40 | $120.00 | −$13.99 / -10.45%; basis $133.99; Today −$13.99; NEW `[10/22 11:01 ET intraday rcv]`; BOUGHT OPEN 10/22 @$0.44 ×3 net −$133.99 (order + ledger, broker-verified; fill clock UNKNOWN); card/owner UNKNOWN (D-74) |
| $70P | Nov-27-2026 | 2 | $1.41 | $1.22 | $244.00 | −$37.33 / -13.27%; basis $281.33; Today −$37.33; NEW `[10/22 11:01 ET intraday rcv]`; BOUGHT OPEN 10/22 @$1.40 ×2 (limit $1.46) net −$281.33 (order + ledger, broker-verified; fill clock UNKNOWN); card/owner UNKNOWN (D-74) |
| $67P | Nov-27-2026 | 4 | $1.28 | $0.50 | $200.00 | −$310.65 / -60.84%; basis $510.65; Today −$308.00; MARK ONLY `[10/22 11:01 ET intraday rcv]`; bought10/12 net$510.65; gross/time/card/owner UNKNOWN (D-76/D-77) |
| $60P | Dec-18-2026 | 2 | $2.57 | $0.29 | $58.00 | −$455.34 / -88.71%; basis $513.34; Today −$10.00; MARK ONLY `[10/22 11:01 ET intraday rcv]` |
| $60P | Dec-18-2026 | 3 (M) | $2.93 | $0.29 | $87.00 | −$791.02 / -90.10%; basis $878.02; Today −$15.00; MARK ONLY `[10/22 11:01 ET intraday rcv]`; broker "M" badge, meaning not shown in the capture (prior mirrors read it as a multi-lot marker — UNVERIFIED); total5 Dec18 60P across2lots |
| $65P | Dec-31-2026 | 2 | $1.69 | $0.82 | $164.00 | −$173.33 / -51.39%; basis $337.33; Today −$110.00; MARK ONLY `[10/22 11:01 ET intraday rcv]`; `MGMT-KRE65P-DEC31`: hard stop Thu12/31 15:00 ET (5ce609f80), not price gate |

### WAL (REGINALD) — Sep-18 pair EXPIRED

*$70P + $67.5P Sep-18 ×1 each EXPIRED as of 9/18, broker-confirmed ⇒ realized −$1,519.34 → rotation 10/22 chunk C, byte-exact. Duration roll = the Robinhood WAL Dec-18 $70P ×1 below; RH WAL $77.5P Aug-21 sale P&L UNRECORDED (D-18).*

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18-2026 | 1 | $11.85 | $1.25 | $125.00 | −$1,059.67 / -89.45% | `[10/22 11:01 ET intraday rcv]`; basis $1,184.67; Today −$55.00. MARK ONLY; BROCK vehicle; HOLD ruled8/13 (private-credit batch §②), vehicle-mismatch flag live. |
| OZK | $40P | Nov-20-2026 | 4 | $0.81 | $0.05 | $20.00 | −$302.65 / -93.81% | `[10/22 11:01 ET intraday rcv]`; basis $322.65; Today −$40.00. MARK ONLY; bought10/7 (Activity); broker "E" badge. PROME-supplied WQ-428 SELL approved; 4 still held at 10/22 11:01 ET; no sell order among the 10 visible orders (D-82). Thesis ownership UNKNOWN (D-74). |
| WAL | $70P | Dec-18-2026 | 2 | $2.76 | $1.60 | $320.00 | −$231.33 / -41.96% | `[10/22 11:01 ET intraday rcv]`; basis $551.33; Today −$90.00. MARK ONLY; buy fill/date unseen (D-84); broker "E" badge; ownership/card/approval UNKNOWN (D-74). **Fidelity2 is DISTINCT from Robinhood1; no inherited RH gate.** |
| WAL | $65P | Dec-18-2026 | 4 | $1.71 | $0.55 | $220.00 | −$462.65 / -67.78% | `[10/22 11:01 ET intraday rcv]`; basis $682.65; Today −$140.00. MARK ONLY; bought10/7 (Activity); broker "E" badge. PROME-supplied WQ-429 SELL approved; 4 still held at 10/22 11:01 ET; no sell order among the 10 visible orders (D-82). Thesis ownership UNKNOWN (D-74). |
| ZION | $62.5P | Nov-20-2026 | 2 | $2.18 | $0.65 | $130.00 | −$305.33 / -70.14% | `[10/22 11:01 ET intraday rcv]`; basis $435.33; Today −$60.00. MARK ONLY; buy fill/date unseen (D-84); broker "E" badge; ownership/card/approval UNKNOWN (D-74). |


## Robinhood — satellite account (Individual)

*All holdings/figures below retained from the 9/29 source; carried DTE annotations are historical, not a current freshness assertion.*

> ⚠️ **NOT CAPTURED IN THIS 10/22 RECEIPT (nor 10/20, 10/19, 10/14, 10/13, 10/11, 10/7, 10/1 or 9/30 — 23 days since the 9/29 card) — every cell below is the 9/29 card, unverified today.** 9/29 card: **account $295.15, BP $8.94** `[9/29 13:4x intraday]`; lines + BP = $290.15 ⇒ **$5.00 UNEXPLAINED (D-64)**. Per-line cost/value DERIVED from P/L ÷ P/L% (no Mark column ⇒ machine class `unverified` by design). The prediction-market line and the 9/01→9/25 dead-by-date bookings — USO $159C Sep-11 (bought 9/10, expired $0 — D-58) · QQQ $713C Sep-16 + USO $165C Sep-16 (both expired $0 — D-57) — verbatim → rotation 10/08 chunk B.

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **WAL $70P** | **Dec-18-2026** | 1 | **$2.20 ($220)** — bought 9/02 @ $2.20 (RH activity) ✓ | ≈$265.00 *(derived; mark ≈$2.65)* | ✅ **ON CARD 9/29 — +$45.00 / +20.45%** | TRY-WAL-ROLL70 (filled in Robinhood). Guard **`GATE-TERRY-ROLL70-EXIT`** *"WAL OFFICIAL CLOSE ≥ $81.90 on THREE CONSECUTIVE sessions"* — **0-of-3 as last recorded here** (REGINALD through 9/23, per TERRY STATUS 9/24; not re-read this pass). The option's +20.45% is not the gate — the gate reads WAL's close (rule 7). **$4.40 GTC sell order: CANCELLED / not there — Will 9/28** (`PROME/inbox/processed/2026-09-28_from-WAL_WQ-324-325-ruled-verbatim-and-4.40-GTC-cancelled.md`) ⇒ **no resting exit order; any take-profit is Will's manual act.** Time stop Fri 12/4. 78 DTE. **D-47** |
| **KRE $25P** | 1/15/2027 | 1 | $53.00 — card-derived ✓ | ≈$1.00 *(derived)* | ✅ **ON CARD 9/29 — −$52.00 / −98.11%** | Deep-OTM lottery; entry pre-7/16, never recorded — **D-54** (before the 9/01 activity view). 106 DTE |
| T | stock | 1 | — | — | ⚠️ no stocks card 9/29; no T row in RH activity 9/01→9/25 | Hypothesis: sold before 9/01, unconfirmed — **D-20**. The card no longer closes to the cent (D-64), so the 9/27 "no stock line" inference is weaker |

## Account UNATTRIBUTED — receipted fills not yet attributed to an account

*No rows. VLO ×1 (this section's only row since 9/19) moved to § Fidelity — Longs on the 9/25 ledger (D-55 account leg CLOSED). The section stays as the landing place for a receipt that names no account (the parser admits it — TERRY `cfd9b9115`).*

---

## ⚠️ Reconcile discrepancies (received 2026-10-22 11:01 ET per Will; intraday marks; quote/fill clocks UNKNOWN)

> Broker view > Will's word > desk record. October22 intraday marks are NOT closes. DTE from the receipt date only; no current executable bids. **Will manages his own expiries (`USER.md` § No expiry nagging, 10/20): DATED rows below are records, not prompts.** All prior duties survive unless explicitly closed. Prior section = `git show 100c63edc:FORGE/STATUS.md`; older history = `ba1a41e09`, `6fbf39cd0` and existing rotations. Permanently UNKNOWN WQ-167:9/2 USO135C sale price, never ask. This list records evidence and owners only; it carries no sell recommendation.

### Will supplies / PROME re-reads — facts owed

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| DATED | QQQ Oct-22 717C ×1 (NEW) | 🔴 expires 10/22, the capture day, 0 calendar DTE | Value $38.00 `[10/22 11:01 ET intraday rcv]`; basis $154.66; bought open 10/22 @$1.54 (broker-verified). No contract-specific card | Moneyness at expiry not verified (no QQQ quote supplied); exercise mechanics under D-60 | **Will** (his expiry); **PROME** records |
| **D-60** | Fidelity expiring-option handling | 🔴 next expiry 10/22 | NARROWED: this ledger shows Fidelity "SOLD CLOSING OPTION LIQUIDATION" rows on expiry day for QQQ Oct-20 719P (10/20, +$208.99) and QQQ Oct-21 715P (10/21, +$1.99); position_management.tsv records the same row type for the Oct-02 740P (10/2, +$3.75). If exercised, a 717C buys 100 QQQ at $717 ($71,700), mechanics only | INFERRED: the broker liquidates some expiring contracts itself on expiry day; the trigger (moneyness threshold), timing and initiator are not displayed; ITM exercise/IRA handling still never observed | **Will** broker policy |
| DATED | CRWV Oct-23 56P ×1 · USO Oct-23 163C ×1 | 🟠 1 calendar DTE | Values $98/$99; bases $179.66/$289.66. CRWV buy unseen (D-84); USO bought 10/19 @$2.89. No contract-specific cards (D-77) | No thesis or management approval inferred from entry | **Will**; PROME scope |
| **D-88** NEW | QQQ Oct-20 715P ×1 disposition | 🟠 record before any realized claim | Absent from the 10/22 capture; basis $200.66; no row in the visible ledger (view ends at the 10/20 719P liquidation). Cash bridge: 10/20 capture cash+pending $16,970.29 − Oct-21 715P buy $223.66 + 719P liquidation $208.99 = $16,955.62 vs ledger 10/20 closing balance $16,972.96 ⇒ **+$17.34 unexplained** (10/21 rows then tie to $15,807.97 exactly). No QQQ share line visible | HYPOTHESIS: the $17.34 is consistent with a sale/liquidation of this 715P at about $0.18 less fees ⇒ conditional realized −$183.32; equally it could be another unseen credit. Nothing booked; no worthless expiry inferred | **Will** supplies 10/20 Activity below the cut; **PROME** records |
| **D-89** NEW | Working-order census | 🟠 open order at capture | VLY Dec-18 12P ×1 buy-to-open limit $0.15 (Day), status Open — not a position, not booked. Orders page 1 of 2: 10 of 11 orders shown | INFERRED: the unseen 11th order is the 10/22 QQQ Oct-26 710P buy (in the ledger, not on the visible page). Whether VLY filled or cancelled is UNKNOWN | **Will**; **PROME** books it only from a later capture |
| **D-85** | QQQ Oct-20 719P basis allocation | 🟡 NARROWED — cohort closed | Cohort CLOSED: 10/19 BTO2 −$554.32 + 10/19 STC1 +$224.34 + 10/20 liquidation +$208.99 ⇒ **−$120.99**, independent of allocation. Per-leg split: −$53.32/−$67.67 (10/19 removed-basis basis, already carried on the 10/19 mirror) or −$52.32/−$68.67 (10/20 displayed basis $277.66). PROME's transcription books −$68.67; with the 10/19 −$53.32 that double-counts $1.00 | Which per-leg basis the broker treats as authoritative is UNKNOWN; only the cohort is certified (DERIVED) | **PROME** records the cohort; **Will** broker lots only if a per-leg figure is ever needed |
| DATED | QQQ Oct-26 710P ×1 (NEW) · USO Oct-28 165C ×1 · CMG Oct-30 28P ×1 · USO Oct-30 165C ×2 · USO Oct-30 163C ×1 (NEW) | 🟡 4/6/8/8/8 calendar DTE | 710P value $783 on basis $457.66 (+71.08%, a mark; no gate registered here). Oct-30 163C bought 10/21 (ledger). No contract-specific cards (D-77) | No card, scale approval or roll linkage inferred from new lots | **Will**; PROME scope |
| **D-82** | Approved sells not evidenced | 🟡 record | PROME-supplied WQ-429 WAL65P4, WQ-428 OZK40P4, WQ-357 TBT5 SELL approvals. All three still held at 10/22 11:01 ET ($220.00/$20.00/$193.80); none among the 10 visible orders | Whether ordered/working/filled later is UNKNOWN; approvals are not executions. Will's 10/20 stated preference not to sell collapsed lines = context, not a ruling on these approvals | **Will** (disposition of his approvals); **PROME** records |
| **D-74** | Fidelity bank-put thesis ownership / new-line scope | 🟡 record | NEW KRE Nov-20 66P ×3 and KRE Nov-27 70P ×2 bought 10/22 (broker-verified); grouped under KRE for navigation only. WAL65P4/OZK40P4 cards/approvals established (D-82); Fidelity WAL70P2/ZION62.5P2 and both new KRE lines: owner/card/approval UNKNOWN; RH WAL70P1 separate | No inherited gate or approval from same symbol/heading | **PROME** scope; **Will/REGINALD/TERRY** |
| **D-77** | Off-thesis ownership/cards | 🟡 record | All eight off-thesis rows (incl. NEW 717C, 710P, USO Oct-30 163C) plus KRE67P lack contract-specific owner/card/approval | Grouping does not establish thesis or authorization | **PROME** scope; **Will/TERRY** |
| **D-70** | Management mappings | 🟡 source changed — re-review owed | This file's bytes changed ⇒ every `position_management.tsv` mapping sourced to it is withheld until PROME re-reviews. Rows for the Oct-20 719P/715P and Oct-22 715P (if any) now describe ABSENT contracts; no reviewed mapping for the five NEW rows or the added GLD share | Mapping is not a card or trade approval | **PROME** mapping; **TERRY** cards |
| **D-84** | Unseen entries and quantity changes (10/19) | 🟡 evidence | CRWV56P1 $179.66, Fidelity WAL70P2 $551.33, ZION62.5P2 $435.33 buys unseen; GLD20→24 residual2 $764.28 DERIVED; VLO2→3 +$444.73; USO37→35 −$257.84; CMG2→1 −$54.67. Unchanged: the 10/22 ledger starts at 10/20 | Dates/prices/disposal methods/proceeds/realized UNKNOWN; not proof of authority | **Will** earlier Activity; **PROME** records |
| **D-86** | Three expired contracts absent | 🟡 outcome evidence owed | QQQ Oct15 715P, Oct16 735C, HBAN Oct16 16P absent; no resulting stock visible. Unchanged (outside the ledger window) | Sale/exercise/lapse and realized UNKNOWN | **Will** earlier Activity; **PROME** records |
| **D-78** | VLO extra-share scope | 🟡 scope before action | 3sh basis $1,296.73; unchanged. Original `GATE-TERRY-VLO-HELD-01` letter/WQ-386 and terminal scale instruction unchanged (Longs/GATES) | Neither added share extends original management scope | **Will** authorization; **PROME/TERRY** scope |
| **D-76** | Detailed fills/lots | 🟡 evidence | 10/22 sell fill prices visible (715P $7.31, 717P $9.82, 720P $13.57); 710P and USO Oct-30 163C buys are ledger nets only (price unseen). All fill clocks UNKNOWN (D-66). Prior results historical | No broker realized-P/L report; all realized here DERIVED | **Will** lots/fills; **PROME/TERRY** integrate |
| **D-80** | Prior unseen GLD+3 / HBAN−1 / QQQ Oct16 725P opening | 🟡 carried | 10/15 gaps unchanged (GLD +$1,122.60 basis; HBAN −$95.67/proceeds unknown; 725P sale net $769.32, opening basis unknown) | Outside every later crop; nothing resolved by later holdings | **Will** earlier Activity; **PROME** records |
| **D-87** | 10/19 capture marks vs Fidelity's prior-day reference | 🟡 record | 10/20 finding unchanged (Today G/L vs mirror delta gaps on 11 option rows). Not testable on this capture: two sessions separate it from the 10/20 mirror and the 10/21 reference marks were not captured | INFERRED (unchanged): 10/19 post-close marks were not the broker's prior-close reference | **PROME** record |
| **D-83** | Clock / Robinhood | 🟡 standing | Receipt 10/22 11:01 ET per Will; quote clock not displayed; marks not closes. Robinhood 9/29 $295.15/BP $8.94 is 23 days old | RH positions may have moved; no inference | **Will** RH view when convenient; **PROME** records |
| **D-81** | Historical 10/14 cash mismatch | 🟡 record | Prior mirror $14,027.08 was $16.58 above post-744P balance $14,010.50; later captures tie | Different cut or unseen +$16.58 item UNVERIFIED | **PROME** record |
| **D-79** | Quote/value precision | 🟡 record | 10/22: all 25 values, open G/L and bases tie to the cent; 13 rows' displayed open % differs by 0.01 pt from G/L ÷ basis. Prior 10/15 1¢ truncations historical | Rounding source UNVERIFIED; no figure affected | **PROME** evidence |
| **D-75 · D-66 · D-69 · D-62 · D-63 · D-64 · D-65 · D-61 · D-59 · D-45 · D-55 · D-28 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1** | **Carried discrepancies (18) — every row still OPEN; rows verbatim → rotation 10/08 chunk D1 (D-75) + D2 (the other 17)** | 🟡 carried | None closed, re-dated or re-owned; every cell unchanged in the record. Ticker-bearing items, for the text scan: STNG (D-17) · RH QQQ $715P Aug-31 (D-28) · RH KRE $25P entry (D-54) · RH WAL $77.5P Aug-21 sale (D-18) · the RH T share (D-20) · AAPL 5-sh sale pre-7/30 (D-1) · D-75 (OZK 40P basis 1¢; mirror carries $322.65, record only) | Returns to this table when its state changes | As recorded, per row: **Will** — D-66 · D-69 · D-63 · D-64 · D-61 · D-59 · D-45 · D-55 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1; **RH history before 9/01** — D-28; **PROME** — D-62 · D-65 (re-reads of desktop-local images) · D-75 (record) |

*D-69 missing+$53.54 remains OPEN. D-66 now includes 10/20–22 fill clocks plus historical 10/14–15 clocks/derived gross prices. D-71 broker leg remains CLOSED (cohort+$142.44, rotation10/15 chunk A); D-72/D-73 historical closures unchanged. No duty closed by silence; none closed this pass (D-60 and D-85 narrowed).*

*Guards: D-47 RH WAL70P `GATE-TERRY-ROLL70-EXIT`, last recorded0-of-3, no resting exit, time stop12/4; REGINALD grades/TERRY proposes/Will harvests. That stale count is not a current reading. VLO original letter/terminal scale unchanged; extra-share scope D-78. WQ-200 USO stock no live rule. `MGMT-KRE65P-DEC31` is a time stop, not a price gate. APD tag/adjustment unverified. Option P/L percentages (e.g. QQQ 710P +71.08%, CMG 28P +70.14%) are marks, not harvest/disarm readings; no gate adjudicated this pass.*

---

## Immediate Actions (10/22 11:01 ET intraday receipt) — evidence and records only

| Item | State | Owner |
|---|---|---|
| 🔴 QQQ Oct-22 717C ×1 expires on the capture day; D-60 expiry handling only partly observed | 0 calendar DTE; record, not a prompt | **Will** (his call) |
| 🟠 D-88 QQQ Oct-20 715P disposition unseen (+$17.34 cash residual); D-89 VLY open order + unseen 11th order; CRWV 56P / USO 163C expire 10/23 | evidence / 1 calendar DTE | **Will**; **PROME** records |
| 🟡 D-70 mapping re-review (source bytes changed; five NEW rows unmapped); D-85 cohort −$120.99 booked, per-leg split open | integration | **PROME/TERRY** |
| 🟡 D-82 approved sales still held; D-74/D-77 new-line ownership; all other D-rows and 18 carried duties remain | evidence/scope | **Will/PROME/TERRY** |

---

*History → `_archive/JOURNAL.md`, existing rotations and Git; immediately prior whole mirror = `git show 100c63edc:FORGE/STATUS.md` | `PORTFOLIO.md` FROZEN Feb snapshot, never live | Truth = Will/broker off-repo | Current evidence → `PROME/data/2026-10-22_broker-capture-TRANSCRIPTION.md` (25 Fidelity positions; Orders page 1 of 2, 10 of 11 shown; Past-30-days ledger back to the 10/20 719P liquidation; received 11:01 ET per Will, intraday; quote/fill clocks UNKNOWN). Robinhood source remains9/29; prior evidence/history survives in Git.*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumers: `AGENTS/TERRY/scripts/positions_from_forge.py` (sections `^## (Fidelity|Robinhood)` + `^## Account <NAME>`; table headers by prefix; cell text — emphasis and strikethrough visible) · `PROME/tools/desk_attention.py` `holdings()` (same sections; `Qty` + `Ticker|Strike|Position` headers; expiry year from `**Updated:**`) · `PROME/tools/will_brief.py` `parse_money()` (header before the first `## `: `account total:**`, `money market):** $X (Y%)`, `**Updated:** YYYY-MM-DD`, `marks = [Fri ]YYYY-MM-DD`) · `FORGE/position_management.tsv` `source_sha256` (any byte change here withholds every mapping sourced to this file until PROME re-reviews) · `AGENTS/BRENT/scripts/pending_receipts.py` (text-level closure candidates). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself here in the same commit that starts parsing. *(Pass notes 9/27 → 10/8 → rotation 10/08 chunk G. Conventions they set, still binding: the header money line keeps the shape `will_brief.py` reads; option expiries carry the year; the `Mark <m/d>` header is prefix-bound; terminal records live in italic lines, which no parser reads as rows.)*
