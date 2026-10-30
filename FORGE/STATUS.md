# FORGE — Trading Operations

Dashboard management mapping → [position_management.tsv](position_management.tsv); maintenance contract → [dashboard notes](DASHBOARD.md). Holdings remain in this file; approval, order and fill evidence are separate. A changed evidence source invalidates its management mapping until reviewed.

> ✅ **2026-10-30 (Fri) — RECONCILE BY ANVIL to Will's Fidelity capture posted 13:21 ET in the PROME window: positions view + Pending orders panel + Past-30-days Activity as visible (10/23–10/30). INTRADAY: marks are Fidelity last prices at ~13:2x ET in the October30 session — NOT a close, NOT settles, NOT executable quotes; quote clock not displayed.** Source `PROME/data/2026-10-30_broker-capture-TRANSCRIPTION.md` (PROME transcription of two images). ANVIL independently verified **23/23** row values, open G/L and Today $ to the cent (VLO half cent, D-79): positions **$26,927.52** + cash **$13,386.72** + pending **+$5,927.58** = **$46,241.82** = displayed total; Σ Today +$789.92 and Σ open G/L −$278.47 tie; pending = today's six fills net $4,965.58 + the prior $962.00. Against last mirror `69f91a091` (10/29 post-close, 28 rows): **0 NEW / 0 QTY CHANGE / 5 GONE — all SOLD or BOUGHT TO CLOSE today, broker-verified, realized +$4,634.95 booked / 23 MARK ONLY**; the QQQ Nov-20 690P ×2 is now a **naked long** (short leg closed).
>
> ⚠️ **ACCOUNT SCOPE — ONE Fidelity Traditional IRA (•1326; last four only, the repo is public). Robinhood Individual NOT provided: its rows below are not in this export's account, unverified today; Will's word 10/29 (PROME-supplied via TERRY's note) is that they are "all dead" — written off by him, not evidenced by a capture. Absence proves no closure. Orders panel shows TODAY's orders only: one OPEN order at capture (D-89); earlier working orders UNKNOWN.**
>
> **Updated:** 2026-10-30 · marks = 2026-10-30 intraday ~13:2x ET (Fidelity last prices, posted 13:21 ET; quote clock not displayed; not a close, not settles) — all Fidelity cells `[10/30 ~13:2x ET intraday]` · **Fidelity cash (money market):** $13,386.72 (28.95%) + **Pending activity +$5,927.58** (= today's six fills net +$4,965.58, still "Processing", + the $962.00 "margin credit balance" carried from 10/29; already in the total, never add again) · **Fidelity account total:** $46,241.82 (Today +$789.92 / +1.74%; open G/L −$278.47 / −1.02% on displayed basis $27,205.99). Snapshot change vs 10/29 close: **+$7,082.80 = positions +$2,117.22 + cash $0.00 + pending +$4,965.58** = survivors' marks +$3,842.92 vs their 10/29 lasts + the five closed lines' exits +$3,239.88 vs their 10/29 marks; not a daily/realized return; Fidelity's Today +$789.92 differs by $3,053.00 (option prior-day reference, D-87). **Realized booked this pass: +$4,634.95 (today's five closes) and −$698.90 (three 10/23–10/26 outcomes now visible); USO 10/23 +$248.54 CONDITIONAL (D-90).** Robinhood $295.15 / BP $8.94 `[9/29 13:4x intraday]`, 31 days old, written off by Will's word. Prior tables/history remain in Git (`69f91a091`, `ec5a7058b`, `100c63edc`, `ba1a41e09`, `6fbf39cd0`) and existing rotations; no history rebooked.

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (its own header names the current base and amendment count). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All Fidelity marks `[10/30 ~13:2x ET intraday]`; quote clock not displayed; intraday lasts, not closes. Cost = basis ÷ qty (DERIVED); Mark = the displayed last (value = last × qty, verified); not exact fills.*

| Ticker | Type | Qty | Cost | Mark 10/30 ~13:2x ET intraday | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | 3 | $23.64 | $346.95 | $1,040.85 | +$969.92 / +1,367.43% | Today −$5.88; broker "E" badge. MARK ONLY. The 4→3 sale (basis −$23.65) is still UNSEEN in the visible ledger (D-90); nothing realized booked. Prior lot gaps D-76/D-1 historical. |
| GLD | Stock | 28 | $374.63 | $356.57 | $9,983.96 | −$505.57 / -4.82% | Today −$336.00; MARK ONLY. The 25→28 adds (+$1,098.75, $366.25/sh DERIVED) still UNSEEN (D-90). Will adopted 28 on TERRY's card 10/29 (PROME-supplied). **`MGMT-GLD-SHARES-OCT24` (TERRY rails, MIDAS WQ-451 lines): 1-month downside line "GLD close < $360.71" — a price-path line, "not by itself a trim signal" (the card's note 1). This $356.57 is an INTRADAY last, $4.14 / 1.15% BELOW the line's level; the line reads the CLOSE — not graded here.** The card's choices are Will's, none recommended. MIDAS; largest line. |
| USO | Stock | 30 | $122.40 | $171.57 | $5,147.10 | +$1,475.09 / +40.17% | Today +$101.40; MARK ONLY. The 35→30 change is now VISIBLE: **5 units SOLD 10/23 +$842.96** (ledger, broker-verified); vs the $594.42 basis relief ⇒ **+$248.54 CONDITIONAL** (holds only if no other USO share trade sits in the window, D-90). **WQ-200 DECLINED 9/10: NO harvest/give-back rule live; Will manages by hand** — the +40.17% is a mark, not a gate reading. BRENT thesis. |
| VLO | Stock | 3 | $432.24 | $394.065 | $1,182.19 | −$114.54 / -8.84% | Today +$28.48; MARK ONLY; exact basis $1,296.73. **Additional-share authorization/management scope UNKNOWN (D-78).** Held-share exit letter `GATE-TERRY-VLO-HELD-01` (PROME/GATES.tsv): leg A = "the matched ULSD crack SETTLEMENT (HOZ26×42 − CLZ26 for 2026-10-15 through 2026-11-19) closes BELOW $90.16" — a **crack-basis gate, not a stock price gate**; this −8.84% is a mark and reads nothing on it. Scale instruction WQ-213 remains STAND DOWN/TERMINAL under `GATE-TERRY-VLO-SCALE`. Fill-clock gaps D-55/D-76 historical. |
| APD | Stock | 2 | $294.79 | $314.21 | $628.42 | +$38.85 / +6.58% | Today +$4.92; MARK ONLY; exact basis $589.57. Historical 10/1 D badge/$1.81 reference adjustment unverified; thesis tag unassigned since 7/30. |

*TBT ×10 SOLD 10/30 @ $38.57 ($385.70; Orders + ledger, broker-verified) vs basis $365.61 ⇒ **+$20.09** realized. No live TBT line. WQ-357 RESOLVED by Will 10/29; `MGMT-DURSHORT-EXIT-WQ291` CLOSED at TERRY. The 5→10 rebuy (+$193.60) is still UNSEEN (D-90).*

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

*No live event-box rows; terminal records → rotation 10/30 chunk D, byte-exact.*

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, owned by no agent unless separately recorded. **Will manages his own expiries** (`USER.md` § No expiry nagging, 10/20 11:32 ET; supersedes the 9/30 sell-or-roll rail as an instruction): no expiry reminders or sell pushes, and a collapsed line may expire. This mirror records holdings and evidence only; dispositions are read from his captures, never inferred. The capture establishes holdings, not fills, cards or approvals; grouping is navigation, not a thesis or scope ruling. Last marks are not executable bids. Receipt-day DTE is scheduling only.

| Ticker | Strike | Expiry | Qty | Cost | Mark 10/30 ~13:2x ET intraday | Value | P&L | Note |
|--------|--------|--------|-----|------|---------------|-------|-----|------|
| QQQ | $715P | Nov-02-2026 | 1 | $4.85 | $25.41 | $2,541.00 | +$2,056.34 / +424.28% | `[10/30 ~13:2x ET intraday]`; basis $484.66; Today +$1,453.00; broker "NE" badge. **BOUGHT OPEN 10/27 −$484.66** (ledger, broker-verified; fill price not shown). **+424.28% is a mark; no harvest/disarm line is registered for this contract in this file — not a gate reading.** Card/owner/approval UNKNOWN (D-77). |
| GLD | $375C | Nov-02-2026 | 2 | $3.26 | $0.02 | $4.00 | −$647.33 / -99.39% | `[10/30 ~13:2x ET intraday]`; basis $651.33; Today −$102.00; broker "NE" badge. Buy still UNSEEN (D-90). Not a GLD-share rail; card/owner/approval UNKNOWN (D-77). |
| USO | $170C | Nov-20-2026 | 1 | $6.28 | $9.50 | $950.00 | +$322.34 / +51.35% | `[10/30 ~13:2x ET intraday]`; basis $627.66; Today +$170.00. **BOUGHT OPEN 10/27 −$627.66** (ledger, broker-verified). Will 10/29 (PROME-supplied): his own hand; WQ-491 idea NOT taken — this line is not that card. Card/owner/approval UNKNOWN (D-77). |

*CLOSED 10/30 — today's fills (§ ② Orders + § ③ ledger, broker-verified; proceeds net of fees; realized = proceeds − mirror basis, DERIVED):* **QQQ Oct-30 711P ×2** sold close 1 @ $17.67 (+$1,766.30) and 1 @ $16.63 (+$1,662.30) vs basis $687.33 (one ledger row: bought open 10/27, both contracts) ⇒ **+$2,741.27** · **QQQ Oct-30 710P ×1** sold @ $19.53 (+$1,952.29) vs $661.66 (bought open 10/26, ledger) ⇒ **+$1,290.63** · **USO Oct-30 163C ×1** sold @ $8.01 (+$800.32) vs $358.66 ⇒ **+$441.66** · **QQQ Nov-20 670P SHORT ×2** bought to close @ $8.00 (−$1,601.33, margin) vs opening credit $1,742.63 ⇒ **+$141.30** · TBT ×10 +$20.09 (Longs). **Total +$4,634.95.** Proceeds sit in pending ("Processing"); cash unchanged. Canceled orders, not fills: 711P limit $17.89 · 163C limit $8.17.

*GONE in the 10/22→10/29 window — outcomes now VISIBLE in the 10/30 ledger (§ ③, broker-verified; realized DERIVED vs mirror basis):* **QQQ Oct-22 717C ×1** EXPIRED (row posted 10/23, no amount) ⇒ −$154.66 · **CRWV Oct-23 56P ×1** option-liquidation sale 10/23 +$88.34 vs $179.66 ⇒ −$91.32 · **QQQ Oct-26 710P ×1** option-liquidation sale 10/26 +$4.74 vs $457.66 ⇒ −$452.92 (marked +$325.34 on 10/22). **Sum −$698.90.** Between-capture round trip, never a mirror row: **QQQ Oct-26 705P ×1** option-liquidation sale 10/26 +$1.97; buy UNSEEN, realized UNKNOWN. *Still UNSEEN — nothing booked, no worthless expiry inferred (D-90):* USO Oct-23 163C ×1 ($289.66) · USO Oct-28 165C ×1 ($335.66) · USO Oct-30 165C ×2 ($586.32) · CMG Oct-30 28P ×1 ($54.66).

*Prior terminal records (10/22 closes and round trips, DERIVED +$1,537.62, D-85; 10/20 720P; 10/19 calls; 10/14 740P/150C; D-86) → rotation 10/30 chunk A, byte-exact — never add again.*

## Fidelity — Thesis Puts

*Instrument grouping is navigation, not approval: the Fidelity WAL/OZK rows below are Will-direct holdings (bought 10/7, Activity); thesis/desk ownership and management approval are NOT established by the broker view.*

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

*No live TLT line; terminal records → rotation 10/30 chunk B, byte-exact.*

### KRE — regional banks (REGINALD)

*All seven rows `[10/30 ~13:2x ET intraday]`, MARK ONLY; the 68P ×10 buy is still UNSEEN (D-90); grouping is not approval/ownership (D-74). Prior Sep30 roll/exits remain historical in Git/rotation 10/01 chunk D.*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $66P | Nov-20-2026 | 3 | $0.45 | $0.26 | $78.00 | −$55.99 / -41.79%; basis $133.99; Today +$18.00; MARK ONLY `[10/30 ~13:2x ET intraday]`; bought 10/22 @$0.44 (10/22 ledger); card/owner UNKNOWN (D-74) |
| $70P | Nov-27-2026 | 2 | $1.41 | $1.02 | $204.00 | −$77.33 / -27.49%; basis $281.33; Today +$44.00; MARK ONLY `[10/30 ~13:2x ET intraday]`; bought 10/22 @$1.40 (10/22 ledger); card/owner UNKNOWN (D-74) |
| $68P | Nov-27-2026 | 10 | $0.73 | $0.50 | $500.00 | −$226.63 / -31.19%; basis $726.63; Today −$1,800.00 against a broker prior-day reference of $2.30 vs the $0.18 10/29 last (D-87); MARK ONLY `[10/30 ~13:2x ET intraday]`; buy date/price UNSEEN (D-90); card/owner UNKNOWN (D-74) |
| $67P | Nov-27-2026 | 4 | $1.28 | $0.37 | $148.00 | −$362.65 / -71.02%; basis $510.65; Today −$68.00; MARK ONLY `[10/30 ~13:2x ET intraday]`; bought 10/12 net $510.65; card/owner UNKNOWN (D-76/D-77) |
| $60P | Dec-18-2026 | 2 | $2.57 | $0.27 | $54.00 | −$459.34 / -89.49%; basis $513.34; Today +$14.00; MARK ONLY `[10/30 ~13:2x ET intraday]` |
| $60P | Dec-18-2026 | 3 (M) | $2.93 | $0.27 | $81.00 | −$797.02 / -90.78%; basis $878.02; Today +$21.00; MARK ONLY `[10/30 ~13:2x ET intraday]`; broker "M" badge (PROME's transcription legend reads it as margin-flagged; earlier mirrors read a multi-lot marker — UNVERIFIED); total 5 Dec-18 60P across 2 lots |
| $65P | Dec-31-2026 | 2 | $1.69 | $0.75 | $150.00 | −$187.33 / -55.54%; basis $337.33; Today −$20.00; MARK ONLY `[10/30 ~13:2x ET intraday]`; `MGMT-KRE65P-DEC31`: hard stop Thu 12/31 15:00 ET (5ce609f80) — a time stop, not a price gate |

### WAL (REGINALD) — Sep-18 pair EXPIRED

*Sep-18 pair EXPIRED ⇒ −$1,519.34 → rotation 10/30 chunk C, byte-exact. RH WAL $77.5P Aug-21 sale P&L UNRECORDED (D-18).*

### Other puts

*QQQ Nov-20 690P ×2 is now a **NAKED LONG**: the 670P ×(−2) short leg was BOUGHT TO CLOSE 10/30 @ $8.00 (−$1,601.33, margin; realized +$141.30, booked above). The 690/670 spread ×2 opened 10/23 by Will's hand on TERRY card `IDEA-QQQ-PUTWALL-OCT22` (`AGENTS/TERRY/setups/QQQ_nov20-690-670P_gamma-negative-putwall_2026-10-22.md`); its opening rows are not among the visible 10/23 ledger rows (D-90). Basis at risk on the long alone $2,679.33 (the spread's net was $936.70). **Card § 6 lines are written for the SPREAD, stated so no number is read as a gate: harvest "sell the spread when it marks ≥ $10.00 … on the broker bid"; kill "SPX cash close ≥ 7,750 on two consecutive sessions"; time stop "sell by the close Fri 2026-11-13". Whether any of them governs the naked long is TERRY's and Will's call — not adjudicated here (D-93).** OPEN ORDER at capture (§ ②, not a fill): Sell to Close 1 QQQ Nov-20 690P, limit $17.95, Day, vs last $17.70 (D-89).*

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| QQQ | $690P | Nov-20-2026 | 2 | $13.40 | $17.70 | $3,540.00 | +$860.67 / +32.12% | `[10/30 ~13:2x ET intraday]`; basis $2,679.33; Today +$1,570.00; broker "M" badge. NAKED LONG (paragraph above); open sell order 1 @ $17.95 (D-89), 2 held; +32.12% is a mark, not a card-line reading (D-93). Opening fills UNSEEN (D-90). |
| APO | $95P | Dec-18-2026 | 1 | $11.85 | $0.65 | $65.00 | −$1,119.67 / -94.52% | `[10/30 ~13:2x ET intraday]`; basis $1,184.67; Today −$55.00. MARK ONLY; broker "E" badge; BROCK vehicle; HOLD ruled 8/13 (private-credit batch §②), vehicle-mismatch flag live. |
| OZK | $40P | Nov-20-2026 | 4 | $0.81 | $0.10 | $40.00 | −$282.65 / -87.61% | `[10/30 ~13:2x ET intraday]`; basis $322.65; Today $0.00. MARK ONLY; bought 10/7 (Activity). PROME-supplied WQ-428 SELL approved 10/14; **4 still held at 10/30 ~13:2x** (D-82). Thesis ownership UNKNOWN (D-74). |
| WAL | $70P | Dec-18-2026 | 2 | $2.76 | $1.15 | $230.00 | −$321.33 / -58.29% | `[10/30 ~13:2x ET intraday]`; basis $551.33; Today −$120.00. MARK ONLY; buy fill/date unseen (D-84); ownership/card/approval UNKNOWN (D-74). **Fidelity 2 is DISTINCT from Robinhood 1; no inherited RH gate.** |
| WAL | $65P | Dec-18-2026 | 4 | $1.71 | $0.55 | $220.00 | −$462.65 / -67.78% | `[10/30 ~13:2x ET intraday]`; basis $682.65; Today −$80.00. MARK ONLY; bought 10/7 (Activity). PROME-supplied WQ-429 SELL approved 10/14; **4 still held at 10/30 ~13:2x** (D-82). Thesis ownership UNKNOWN (D-74). |
| ZION | $62.5P | Nov-20-2026 | 2 | $2.18 | $0.40 | $80.00 | −$355.33 / -81.63% | `[10/30 ~13:2x ET intraday]`; basis $435.33; Today −$38.00. MARK ONLY; buy fill/date unseen (D-84); ownership/card/approval UNKNOWN (D-74). |
| VLY | $12P | Dec-18-2026 | 1 | $0.16 | $0.05 | $5.00 | −$10.66 / -68.08% | `[10/30 ~13:2x ET intraday]`; basis $15.66; Today −$5.00. MARK ONLY; the 10/22 $0.15 limit order filled (basis consistent, DERIVED); fill date UNSEEN. Card/owner UNKNOWN (D-74). |
| FLG | $10P | Mar-19-2027 | 1 | $0.71 | $0.55 | $55.00 | −$15.66 / -22.17% | `[10/30 ~13:2x ET intraday]`; basis $70.66; Today −$5.00. MARK ONLY; buy UNSEEN (D-90). Card/owner UNKNOWN (D-74). |


## Robinhood — satellite account (Individual)

*All holdings/figures below retained from the 9/29 source; carried DTE annotations are historical, not a current freshness assertion.*

> ⚠️ **NOT IN THIS EXPORT'S ACCOUNT — UNVERIFIED TODAY (not captured 10/30, 10/29, 10/22, 10/20, 10/19, 10/14, 10/13, 10/11, 10/7, 10/1 or 9/30 — 31 days since the 9/29 card). Will's word 10/29 (TERRY window, PROME-supplied via `AGENTS/TERRY/research/2026-10-29_ira-snapshot/NOTE.md`): Robinhood positions "all dead" — written off by him; no capture evidences closure or values, so the rows stay.** 9/29 card: **account $295.15, BP $8.94** `[9/29 13:4x intraday]`; lines + BP = $290.15 ⇒ **$5.00 UNEXPLAINED (D-64)**. Per-line cost/value DERIVED from P/L ÷ P/L% (no Mark column ⇒ machine class `unverified` by design). The prediction-market line and the 9/01→9/25 dead-by-date bookings — USO $159C Sep-11 (bought 9/10, expired $0 — D-58) · QQQ $713C Sep-16 + USO $165C Sep-16 (both expired $0 — D-57) — verbatim → rotation 10/08 chunk B.

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **WAL $70P** | **Dec-18-2026** | 1 | **$2.20 ($220)** — bought 9/02 @ $2.20 (RH activity) ✓ | ≈$265.00 *(derived; mark ≈$2.65)* | ✅ **ON CARD 9/29 — +$45.00 / +20.45%** | TRY-WAL-ROLL70 (filled in Robinhood). Guard **`GATE-TERRY-ROLL70-EXIT`** *"WAL OFFICIAL CLOSE ≥ $81.90 on THREE CONSECUTIVE sessions"* — **0-of-3 as last recorded here** (REGINALD through 9/23, per TERRY STATUS 9/24; not re-read this pass). The option's +20.45% is not the gate — the gate reads WAL's close (rule 7). **$4.40 GTC sell order: CANCELLED / not there — Will 9/28** (`PROME/inbox/processed/2026-09-28_from-WAL_WQ-324-325-ruled-verbatim-and-4.40-GTC-cancelled.md`) ⇒ **no resting exit order; any take-profit is Will's manual act.** Time stop Fri 12/4. 78 DTE. **D-47** |
| **KRE $25P** | 1/15/2027 | 1 | $53.00 — card-derived ✓ | ≈$1.00 *(derived)* | ✅ **ON CARD 9/29 — −$52.00 / −98.11%** | Deep-OTM lottery; entry pre-7/16, never recorded — **D-54** (before the 9/01 activity view). 106 DTE |
| T | stock | 1 | — | — | ⚠️ no stocks card 9/29; no T row in RH activity 9/01→9/25 | Hypothesis: sold before 9/01, unconfirmed — **D-20**. The card no longer closes to the cent (D-64), so the 9/27 "no stock line" inference is weaker |

## Account UNATTRIBUTED — receipted fills not yet attributed to an account

*No rows. Landing place for a receipt that names no account (the parser admits it — TERRY `cfd9b9115`); history → rotation 10/30 chunk E.*

---

## ⚠️ Reconcile discrepancies (received 2026-10-30 13:21 ET; October30 INTRADAY Fidelity lasts ~13:2x ET; quote clock not displayed; today's Orders + Activity 10/23–10/30 as visible)

> Broker view > Will's word > desk record. Last prices are NOT settles and these are intraday. DTE from the receipt date only; no current executable bids. **Will manages his own expiries (`USER.md` § No expiry nagging, 10/20): DATED rows below are records, not prompts.** All prior duties survive unless explicitly closed. Prior section = `git show 69f91a091:FORGE/STATUS.md`; older → the commits in the header and rotations. Permanently UNKNOWN WQ-167: 9/2 USO135C sale price, never ask. This list records evidence and owners only; it carries no sell recommendation.

### Will supplies / PROME re-reads — facts owed

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-89** | Working-order census | 🟠 one OPEN Day order at capture | Orders panel (today only): **Sell to Close 1 QQQ Nov-20 690P, limit $17.95, Day — OPEN** (last $17.70); not a fill, not booked. Two of today's limits Verified Canceled (711P $17.89, 163C $8.17). Six filled (booked above). Orders placed before 10/30 not shown | A Day order fills or lapses by today's close; outcome UNKNOWN until the next capture | **Will**; **PROME** books fills only from a capture |
| **D-93** NEW | QQQ 690P ×2 after the short-leg close | 🟠 scope before next card read | Spread card `IDEA-QQQ-PUTWALL-OCT22` § 6 lines are written for the spread (harvest ≥ $10.00 spread mark on the bid; kill SPX cash close ≥ 7,750 ×2; time stop 11/13 close). Short leg bought back 10/30 (+$141.30); the long alone carries basis $2,679.33 | Whether the card still governs, or the naked long is a new Will-direct position, is NOT stated anywhere seen; nothing inferred | **TERRY** (card state); **Will** |
| DATED | QQQ Nov-02 715P ×1 · GLD Nov-02 375C ×2 | 🟡 3 calendar DTE (Mon 11/2) | Values $2,541.00 (+424.28%, a mark, no registered line) / $4.00; bases $484.66 / $651.33. 715P bought 10/27 (ledger); 375C buy unseen. No cards (D-77) | No scale approval or roll linkage inferred | **Will**; PROME scope |
| **D-60** | Fidelity expiring-option handling | 🟡 NARROWED | Today's three Oct-30 lines were SOLD by Will before expiry (Orders). Ledger now shows both paths: OPTION LIQUIDATION sales on expiry day (CRWV Oct-23 56P +$88.34 on 10/23; QQQ Oct-26 710P +$4.74 and 705P +$1.97 on 10/26) and a lapse (QQQ Oct-22 717C "EXPIRED", posted 10/23). Mechanics only: an exercised put SELLS 100 shares per contract at the strike | INFERRED: which contracts the broker liquidates vs lets lapse — trigger and timing never stated; ITM exercise/IRA handling never observed | **Will** broker policy |
| **D-90** | 10/22→10/29 ledger | 🟡 NARROWED | VISIBLE now (§ ③): USO −5 sold 10/23 +$842.96; CRWV, 717C, Oct-26 710P outcomes (−$698.90, booked); 705P round trip (+$1.97, buy unseen); buys of QQQ 710P/711P ×2/715P and USO 170C (bases match the mirror). Ledger arithmetic ties 10/23 $15,960.36 → 10/27 $14,348.72. STILL UNSEEN: AAPL −1; GLD +3; TBT +5; the 690/670 spread opening (TERRY's card dates it 10/23 — not among the visible 10/23 rows); KRE 68P ×10, GLD 375C ×2, VLY, FLG buys; USO Oct-23 163C, Oct-28 165C, Oct-30 165C ×2, CMG 28P outcomes; no 10/28 or 10/29 rows; the −$962.00 cash step 10/27 $14,348.72 → $13,386.72, matched by the +$962.00 "margin credit balance" (cash + pending unchanged). DERIVED from the 10/29 identity (+$350.15): visible realized −$450.36 (incl. USO +$248.54 CONDITIONAL) leaves **+$800.51** for the unseen lines, the 705P round trip and other flows | HYPOTHESIS: the unseen trades sit on 10/22 after 11:01 ET or below the visible cut — the 10/22 cash + pending $17,476.86 vs the $15,872.02 balance before the first visible row is −$1,604.84 unseen. The panel may be filtered (cash vs margin) rather than cut; UNVERIFIED | **Will** supplies the rest of Activity 10/22→10/29; **PROME** records |
| **D-88** | QQQ Oct-20 715P ×1 disposition | 🟡 record | Unchanged: absent since 10/22; basis $200.66; +$17.34 unexplained in the 10/20 cash bridge | HYPOTHESIS (unchanged): consistent with a sale near $0.18 ⇒ conditional −$183.32; nothing booked | **Will** 10/20 Activity below the cut; **PROME** records |
| **D-82** | Approved sells not evidenced | 🟡 record | WQ-428 OZK 40P ×4 ($40.00) and WQ-429 WAL 65P ×4 ($220.00) still held at 10/30 ~13:2x; today's Orders panel holds no order for either. TBT leg CLOSED 10/29 (Will's word); TBT then sold 10/30 | Earlier working/cancelled orders UNKNOWN; approvals are not executions | **Will** (disposition of his approvals); **PROME** records |
| **D-85** | QQQ Oct-20 719P basis allocation | 🟡 NARROWED (unchanged) | Cohort −$120.99 booked on the 10/22 mirror; per-leg split −$67.67 or −$68.67 | Which per-leg basis the broker treats as authoritative UNKNOWN | **PROME** records; **Will** lots if ever needed |
| **D-74** | Fidelity bank-put ownership / new-line scope | 🟡 record | Bank/credit put cluster 41 contracts / 14 lines, basis $6,644.24, value $1,910.00 `[10/30 ~13:2x ET intraday]` (28 / $4,646.62 on TERRY's 10/24 view). KRE Nov-27 68P ×10, VLY 12P, FLG 10P, Fidelity WAL70P2, ZION62.5P2, KRE 66P/70P: owner/card/approval UNKNOWN. WAL65P4/OZK40P4 cards = D-82 | No inherited gate or approval from same symbol/heading | **PROME** scope; **Will/REGINALD/TERRY** |
| **D-77** | Off-thesis ownership/cards | 🟡 record | No contract-specific card: QQQ Nov-02 715P, GLD Nov-02 375C, USO Nov-20 170C (Will's hand; WQ-491 idea not taken), KRE67P. Oct-30 711P/710P and USO 163C now CLOSED (booked) | TERRY's spread card mentions "the two short-dated QQQ put lines" as the same Nasdaq-downside bet; which contracts is not stated here | **PROME** scope; **Will/TERRY** |
| **D-70** | Management mappings | 🟡 source changed — re-review owed | This file's bytes changed ⇒ every `position_management.tsv` mapping sourced to it is withheld until PROME re-reviews. Five more lines closed 10/30 (QQQ 711P/710P, USO 163C, TBT, 670P short); the 690P is now a naked long; 10/29 NEW rows still unmapped | Mapping is not a card or trade approval | **PROME** mapping; **TERRY** cards |
| **D-91** | Short-leg representation (consumer interface) | 🟡 no short row live | 670P short closed 10/30; no signed-Qty row live, so `desk_attention.holdings()` no longer errors. Convention kept in the footer | The next short re-trips `desk_attention.py` until DOCKET L870 lands | **PROME** (`desk_attention.py`, L870); **TERRY** (`positions_from_forge.py`) |
| **D-87** | Fidelity prior-day reference vs mirror marks | 🟡 record — new instance | 10/30: on 14 option rows Fidelity's prior-day reference (last − Last chg) ≠ the 10/29 post-close last the mirror carried; Σ gap **$3,053.00** = exactly Today +$789.92 vs survivors' Δ +$3,842.92. Largest: **KRE Nov-27 68P reference $2.30 vs $0.18** (gap $2,120.00; Today −$1,800.00). Stock rows match exactly | INFERRED: options' reference is a closing mark/quote, not the last trade; the KRE 68P $2.30 looks like a stale or erroneous print — UNVERIFIED. No value or G/L figure affected | **PROME** record |
| **D-84** | Unseen 10/19 entries and quantity changes | 🟡 evidence | Unchanged: Fidelity WAL70P2, ZION62.5P2 buys unseen; GLD residual2 $764.28; VLO 2→3; USO 37→35; CMG 2→1. CRWV now resolved (D-90) | Dates/prices/proceeds/realized UNKNOWN | **Will** earlier Activity; **PROME** records |
| **D-86** | Three expired contracts absent (Oct-15/16) | 🟡 outcome evidence owed | QQQ Oct15 715P, Oct16 735C, HBAN Oct16 16P; unchanged | Sale/exercise/lapse UNKNOWN | **Will** earlier Activity; **PROME** records |
| **D-78** | VLO extra-share scope | 🟡 scope before action | 3 sh, basis $1,296.73, unchanged; `GATE-TERRY-VLO-HELD-01` letter unchanged (crack-basis) | Neither added share extends original management scope | **Will** authorization; **PROME/TERRY** scope |
| **D-76** | Detailed fills/lots | 🟡 evidence | Today's fills carry prices (Orders); the ledger rows carry net amounts only. USO lot relief $594.42 ≠ 5 × average $609.49 (D-90) | No broker realized-P/L report; all realized DERIVED | **Will** lots/fills; **PROME/TERRY** integrate |
| **D-80** | Prior unseen GLD+3 / HBAN−1 / QQQ Oct16 725P opening | 🟡 carried | 10/15 gaps unchanged | Nothing resolved by later holdings | **Will** earlier Activity; **PROME** records |
| **D-83** | Clock / Robinhood | 🟡 standing | Receipt 10/30 13:21 ET; INTRADAY lasts ~13:2x ET, quote clock not displayed; not closes. Robinhood 9/29 card is 31 days old; Will's word 10/29: "all dead", written off — rows retained, unverified | RH values may be ≈$0; no closure booked without a capture | **Will** RH view if he wants it closed out; **PROME** records |
| **D-81** | Historical 10/14 cash mismatch | 🟡 record | +$16.58 vs post-744P balance; later captures tie | Different cut or unseen item UNVERIFIED | **PROME** record |
| **D-79** | Quote/value precision | 🟡 record | 10/30: 23 values tie to the cent except VLO $394.065 × 3 = $1,182.195 shown $1,182.19 (Today $28.485 → $28.48), a half cent. Option avg cost × qty ≠ basis by fees | Rounding source UNVERIFIED; no total affected | **PROME** evidence |
| **D-75 · D-66 · D-69 · D-62 · D-63 · D-64 · D-65 · D-61 · D-59 · D-45 · D-55 · D-28 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1** | **Carried discrepancies (18) — every row still OPEN; rows verbatim → rotation 10/08 chunk D1 (D-75) + D2 (the other 17)** | 🟡 carried | None closed, re-dated or re-owned; every cell unchanged in the record. Ticker-bearing items, for the text scan: STNG (D-17) · RH QQQ $715P Aug-31 (D-28) · RH KRE $25P entry (D-54) · RH WAL $77.5P Aug-21 sale (D-18) · the RH T share (D-20) · AAPL 5-sh sale pre-7/30 (D-1) · D-75 (OZK 40P basis 1¢; mirror carries $322.65, record only) | Returns to this table when its state changes | As recorded, per row: **Will** — D-66 · D-69 · D-63 · D-64 · D-61 · D-59 · D-45 · D-55 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1; **RH history before 9/01** — D-28; **PROME** — D-62 · D-65 (re-reads of desktop-local images) · D-75 (record) |

*D-69 missing +$53.54 remains OPEN. D-66 includes every fill clock not shown (today's fills carry no time). D-71 broker leg remains CLOSED (cohort +$142.44, rotation 10/15 chunk A); D-72/D-73 historical closures unchanged. This pass closed nothing outright: it narrowed D-90 (seven items visible), D-60 (both expiry paths observed) and D-91 (no short row live), and opened D-93.*

*Guards: each management line's text sits beside its number in the rows above (QQQ 690P spread card, GLD rails, VLO crack-basis letter, KRE65P time stop, USO no live rule). D-47 RH WAL70P `GATE-TERRY-ROLL70-EXIT` last recorded 0-of-3 (stale). Option P/L percentages are marks, not harvest/disarm readings; no gate adjudicated this pass.*

---

## Immediate Actions (10/30 13:21 ET intraday receipt) — evidence and records only

| Item | State | Owner |
|---|---|---|
| 🟠 GLD intraday last $356.57 sits below the `MGMT-GLD-SHARES-OCT24` 1-month line level "GLD close < $360.71"; the line reads the close | gate read on the close, not here | **TERRY** (grade); **Will** (choices) |
| 🟠 D-93 QQQ 690P ×2 naked long — does the spread card still govern; D-89 open sell 1 @ $17.95 Day | card state / record the fill or lapse | **TERRY/Will**; **PROME** |
| 🟡 D-90 rest of Activity 10/22→10/29; D-70 mappings; D-82, D-74/D-77; all other D-rows and 18 carried duties remain | evidence / integration / scope | **Will** ledger; **PROME/TERRY** |

---

*History → `_archive/JOURNAL.md`, existing rotations and Git; immediately prior whole mirror = `git show 69f91a091:FORGE/STATUS.md` | `PORTFOLIO.md` FROZEN Feb snapshot, never live | Truth = Will/broker off-repo | Current evidence → `PROME/data/2026-10-30_broker-capture-TRANSCRIPTION.md` (23 Fidelity positions, today's Orders panel, Activity 10/23–10/30 as visible; posted 13:21 ET, intraday lasts ~13:2x ET; quote clock not displayed). Robinhood source remains 9/29; prior evidence/history survives in Git.*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumers: `AGENTS/TERRY/scripts/positions_from_forge.py` (sections `^## (Fidelity|Robinhood)` + `^## Account <NAME>`; table headers by prefix; cell text — emphasis and strikethrough visible) · `PROME/tools/desk_attention.py` `holdings()` (same sections; `Qty` + `Ticker|Strike|Position` headers; expiry year from `**Updated:**`) · `PROME/tools/will_brief.py` `parse_money()` (header before the first `## `: `account total:**`, `money market):** $X (Y%)`, `**Updated:** YYYY-MM-DD`, `marks = [Fri ]YYYY-MM-DD`) · `FORGE/position_management.tsv` `source_sha256` (any byte change here withholds every mapping sourced to this file until PROME re-reviews) · `AGENTS/BRENT/scripts/pending_receipts.py` (text-level closure candidates). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself here in the same commit that starts parsing. *(Pass notes 9/27 → 10/8 → rotation 10/08 chunk G. Conventions they set, still binding: the header money line keeps the shape `will_brief.py` reads; option expiries carry the year; the `Mark <m/d>` header is prefix-bound; terminal records live in italic lines, which no parser reads as rows. 10/29: a SHORT option leg carries a signed Qty `−N` and a negative value — D-91.)*
