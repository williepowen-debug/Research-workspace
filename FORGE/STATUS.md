# FORGE — Trading Operations

Dashboard management mapping → [position_management.tsv](position_management.tsv); maintenance contract → [dashboard notes](DASHBOARD.md). Holdings remain in this file; approval, order and fill evidence are separate. A changed evidence source invalidates its management mapping until reviewed.

> ✅ **2026-11-05 (Thu) — RECONCILE BY ANVIL to Will's Fidelity captures posted 10:01 ET in the PROME window: positions view + Orders panel (11/5) + Past-30-days Activity as visible (10/30 USO row → 11/5). INTRADAY: marks are Fidelity last prices at ~10:0x ET in the November 5 session — NOT a close, NOT settles, NOT executable quotes; quote clock not displayed.** Source `PROME/data/2026-11-05_broker-capture-TRANSCRIPTION.md` (PROME transcription of two images; ANVIL re-read both images). ANVIL independently verified **19/19** row values, open G/L and Today $ to the cent: positions **$12,669.59** + cash **$28,218.18** + pending **+$3,953.67** = **$44,841.44** = displayed total; Σ Today −$957.21 and Σ open G/L −$6,422.38 tie; pending = the three 11/5 fills. Against last mirror `083745bb1` (10/30 intraday, 23 rows): **1 NEW (USO Nov-11 172C) / 2 QTY CHANGE (GLD 28→18, VLO 3→2) / 5 GONE (AAPL, APD, QQQ Nov-02 715P, GLD Nov-02 375C, QQQ Nov-20 690P) / 16 MARK ONLY.** One closing row is outside the visible Activity (D-94).
>
> ⚠️ **ACCOUNT SCOPE — ONE Fidelity Traditional IRA (•1326; last four only, the repo is public). Robinhood Individual NOT provided: its rows below are not in this export's account, unverified today; Will's word 10/29 (PROME-supplied via TERRY's note) is that they are "all dead" — written off by him, not evidenced by a capture. Absence proves no closure. Orders panel shows TODAY's orders only: three fills, no open order (D-89); earlier working orders UNKNOWN.**
>
> **Updated:** 2026-11-05 · marks = 2026-11-05 intraday ~10:0x ET (Fidelity last prices, posted 10:01 ET; quote clock not displayed; not a close, not settles) — all Fidelity cells `[11/5 ~10:0x ET intraday]` · **Fidelity cash (money market):** $28,218.18 (62.93%) + **Pending activity +$3,953.67** (= the three 11/5 fills, still "Processing"; already in the total, never add again; the $962.00 "margin credit balance" no longer shows) · **Fidelity account total:** $44,841.44 (Today −$957.21 / −2.09%; open G/L −$6,422.38 / −33.64% on displayed basis $19,091.97). Snapshot change vs 10/30: **−$1,400.38 = positions −$14,257.93 + cash +$14,831.46 + pending −$1,973.91** = realized and other flows +$4,743.53 + open G/L change −$6,143.91; not a daily return. **Realized booked this pass, all DERIVED: +$4,168.14 (10/30→11/5 closes) and +$30.47 (four 10/23 exits, D-90); +$575.39 of the +$4,743.53 stays unbooked (D-94, D-95, D-96).** Robinhood $295.15 / BP $8.94 `[9/29 13:4x intraday]`, 37 days old, written off by Will's word. Prior tables/history remain in Git (`083745bb1`, `3064691ae`, `69f91a091`, `ec5a7058b`) and existing rotations; no history rebooked.

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (its own header names the current base and amendment count). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All Fidelity marks `[11/5 ~10:0x ET intraday]`; quote clock not displayed; intraday lasts, not closes. Cost = basis ÷ qty (DERIVED); Mark = the displayed last (value = last × qty, verified); not exact fills.*

| Ticker | Type | Qty | Cost | Mark 11/5 ~10:0x ET intraday | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| GLD | Stock | 18 | $373.93 | $376.53 | $6,777.54 | +$46.87 / +0.69% | Today +$72.72. **QTY 28→18: 10 sold 11/2** (+$1,814.51, +$1,818.46; shares per row D-97) vs basis relief $3,758.86 ⇒ **−$125.89 realized**. The 25→28 adds still UNSEEN (D-90). **`MGMT-GLD-SHARES-OCT24` (TERRY rails, MIDAS WQ-451 lines): 1-month lines "GLD close < $360.71" (TERRY recorded it crossed at the 10/30 close $355.78; card note 1: a price-path line, "not by itself a trim signal") and "GLD close > $391.08". This $376.53 is an INTRADAY last, $15.82 above the first and $14.55 below the second; the lines read the CLOSE — not graded here.** The card's choices are Will's, none recommended. MIDAS; largest line. |
| USO | Stock | 30 | $122.40 | $147.325 | $4,419.75 | +$747.74 / +20.36% | Today +$57.45; MARK ONLY. 35→30 = **5 sold 10/23 @ $168.595, $842.96** vs the $594.42 basis relief ⇒ **+$248.54** (quantity now displayed, 10/23 view). **WQ-200 DECLINED 9/10: NO harvest/give-back rule live; Will manages by hand** — the +20.36% is a mark, not a gate reading. BRENT thesis. |
| VLO | Stock | 2 | $442.37 | $368.15 | $736.30 | −$148.43 / -16.78% | Today +$5.62; exact basis $884.73. **QTY 3→2: 1 share SOLD 11/5 @ $366.665, $366.67 (Orders + Activity). Basis removal $1,296.73 → $884.73 = $412.00, which ties to the original share's 9/18 $412.00 fill ⇒ −$45.33 realized.** **`GATE-TERRY-VLO-HELD-01` consequence: "a SELL of the ONE held share (filled $412.00 9/18, WQ-213)" — that share is the one sold. Gate state is TERRY's and PROME's, not set here: PROME/GATES.tsv read RESOLVED 2026-11-05 EXECUTED at 10:07 ET (TERRY `42b47b6b8`).** The 2 shares left are the added ones; the −16.78% is a mark and no gate reads it (D-78). `GATE-TERRY-VLO-SCALE` stays TERMINAL. |

*CLOSED stock lines (Orders + Activity, broker-verified; realized DERIVED vs mirror basis):* **AAPL ×3 flat:** 1 sold 11/2 +$337.22 (D-97), 2 sold 11/5 @ $352.37, +$704.72, vs $70.93 ⇒ **+$971.01** · **APD ×2** sold 11/2 +$637.04 vs $589.57 ⇒ **+$47.47**. No live AAPL, APD or TBT line.

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

*No live event-box rows; terminal records → rotation 10/30 chunk D, byte-exact.*

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, owned by no agent unless separately recorded. **Will manages his own expiries** (`USER.md` § No expiry nagging, 10/20 11:32 ET; supersedes the 9/30 sell-or-roll rail as an instruction): no expiry reminders or sell pushes, and a collapsed line may expire. This mirror records holdings and evidence only; dispositions are read from his captures, never inferred. The capture establishes holdings, not fills, cards or approvals; grouping is navigation, not a thesis or scope ruling. Last marks are not executable bids. Receipt-day DTE is scheduling only.

| Ticker | Strike | Expiry | Qty | Cost | Mark 11/5 ~10:0x ET intraday | Value | P&L | Note |
|--------|--------|--------|-----|------|---------------|-------|-----|------|
| USO | $172C | Nov-11-2026 | 1 | $5.33 | $0.36 | $36.00 | −$496.66 / -93.25% | `[11/5 ~10:0x ET intraday]`; basis $532.66; Today −$20.00; broker "NE" badge. **NEW: BOUGHT OPEN 10/30 −$532.66** (Activity, broker-verified; after the 10/30 capture). Card/owner/approval UNKNOWN (D-77). |
| USO | $170C | Nov-20-2026 | 1 | $6.28 | $1.46 | $146.00 | −$481.66 / -76.74% | `[11/5 ~10:0x ET intraday]`; basis $627.66; Today +$14.00. MARK ONLY; bought open 10/27. Will 10/29 (PROME-supplied): his own hand; WQ-491 idea NOT taken — this line is not that card. Card/owner/approval UNKNOWN (D-77). |

*CLOSED 10/30→11/5 (Orders + Activity, broker-verified; proceeds net of fees; realized DERIVED; row quantities are not displayed, INFERRED where marked, D-96):* **QQQ Nov-02 715P ×1** sold 11/2 +$2,069.29 vs $484.66 ⇒ **+$1,584.63** · **GLD Nov-02 375C ×2** EXPIRED as of 11/2 (row 11/3, no amount) ⇒ **−$651.33** · **AAPL Nov-04 345C ×1** bought 11/2 −$440.66, sold 11/4 +$776.32 ⇒ **+$335.66** · **QQQ Nov-06 680P** bought 11/2 −$1,141.33 (×2 INFERRED), sold 11/2 +$1,105.31 and +$882.32 ⇒ **+$846.30** · **QQQ Nov-04 680P** two lots: bought 11/2 −$649.66, sold 11/2 +$777.32 ⇒ **+$127.66** (pairing INFERRED); bought 11/3 −$464.66, EXPIRED as of 11/4 (row 11/5, no amount) ⇒ **−$464.66** · **QQQ Nov-20 690P** 1 of 2 sold 11/5 @ $28.83, +$2,882.28 vs half basis $1,339.665 ⇒ **+$1,542.62** (the other: D-94). With VLO −$45.33, AAPL +$971.01, APD +$47.47, GLD −$125.89 above: **total +$4,168.14**. NOT booked, opening leg unseen: QQQ Nov-02 680P sale +$52.34 · QQQ Nov-05 685P sale +$1,202.31 (D-96). The three 11/5 sales sit in pending.

*10/23 exits from `PROME/data/2026-10-23_broker-activity-TRANSCRIPTION.md` (DOCKET L921; realized DERIVED vs mirror basis):* **USO Oct-30 165C ×1** sold @ $7.15, $714.32 vs half of $586.32 ⇒ **+$421.16** (average; by lot +$398.66 or +$443.66) · **USO Oct-23 163C ×1** sold @ $4.36, $435.34 vs $289.66 ⇒ **+$145.68** · **AAPL 1** sold @ $346.635, $346.64 vs $23.65 ⇒ **+$322.99** · **QQQ Oct-26 705P ×2** bought −$861.33, one liquidation row +$1.97 (taken as both contracts) ⇒ **−$859.36**. **Sum +$30.47.** Still UNSEEN, nothing booked: D-90.

*Prior terminal records: 10/30 closes +$4,634.95 and 10/23–10/26 outcomes −$698.90 → `git show 3064691ae:FORGE/STATUS.md`; 10/22 closes (+$1,537.62, D-85), 10/20 720P, 10/19 calls, 10/14 740P/150C, D-86 → rotation 10/30 chunk A, byte-exact — never add again.*

## Fidelity — Thesis Puts

*Instrument grouping is navigation, not approval: the Fidelity WAL/OZK rows below are Will-direct holdings (bought 10/7, Activity); thesis/desk ownership and management approval are NOT established by the broker view.*

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

*No live TLT line; terminal records → rotation 10/30 chunk B, byte-exact.*

### KRE — regional banks (REGINALD)

*All seven rows `[11/5 ~10:0x ET intraday]`, MARK ONLY; the 68P ×10 buy is still UNSEEN (D-90); grouping is not approval/ownership (D-74). Prior Sep30 roll/exits remain historical in Git/rotation 10/01 chunk D.*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $66P | Nov-20-2026 | 3 | $0.45 | $0.07 | $21.00 | −$112.99 / -84.33%; basis $133.99; Today −$18.00; MARK ONLY; bought 10/22 @$0.44 (10/22 ledger); card/owner UNKNOWN (D-74) |
| $70P | Nov-27-2026 | 2 | $1.41 | $0.24 | $48.00 | −$233.33 / -82.94%; basis $281.33; Today −$50.00; MARK ONLY; bought 10/22 @$1.40 (10/22 ledger); card/owner UNKNOWN (D-74) |
| $68P | Nov-27-2026 | 10 | $0.73 | $0.08 | $80.00 | −$646.63 / -89.00%; basis $726.63; Today −$410.00; MARK ONLY; buy date/price UNSEEN (D-90); card/owner UNKNOWN (D-74) |
| $67P | Nov-27-2026 | 4 | $1.28 | $0.12 | $48.00 | −$462.65 / -90.61%; basis $510.65; Today −$108.00; MARK ONLY; bought 10/12 net $510.65; card/owner UNKNOWN (D-76/D-77) |
| $60P | Dec-18-2026 | 2 | $2.57 | $0.08 | $16.00 | −$497.34 / -96.89%; basis $513.34; Today −$16.00; MARK ONLY |
| $60P | Dec-18-2026 | 3 (M) | $2.93 | $0.08 | $24.00 | −$854.02 / -97.27%; basis $878.02; Today −$24.00; MARK ONLY; broker "M" badge (PROME's transcription legend reads it as margin-flagged; earlier mirrors read a multi-lot marker — UNVERIFIED); total 5 Dec-18 60P across 2 lots |
| $65P | Dec-31-2026 | 2 | $1.69 | $0.26 | $52.00 | −$285.33 / -84.59%; basis $337.33; Today −$52.00; MARK ONLY; `MGMT-KRE65P-DEC31`: hard stop Thu 12/31 15:00 ET (5ce609f80) — a time stop, not a price gate |

### WAL (REGINALD) — Sep-18 pair EXPIRED

*Sep-18 pair EXPIRED ⇒ −$1,519.34 → rotation 10/30 chunk C, byte-exact. RH WAL $77.5P Aug-21 sale P&L UNRECORDED (D-18).*

### Other puts

*QQQ Nov-20 690P: **no live line at 11/5.** ×1 sold 11/5 (booked above); the other's close is outside the visible Activity (D-94). Opened 10/23 as the 690/670 spread ×2 ($2,679.33 long, $1,742.63 short; 10/23 view); short leg closed 10/30 +$141.30. Card `IDEA-QQQ-PUTWALL-OCT22` read CLOSED at 10:07 ET (TERRY `42b47b6b8`).*

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18-2026 | 1 | $11.85 | $0.15 | $15.00 | −$1,169.67 / -98.74% | `[11/5 ~10:0x ET intraday]`; basis $1,184.67; Today −$79.00. MARK ONLY; broker "E" badge; BROCK vehicle; HOLD ruled 8/13 (private-credit batch §②), vehicle-mismatch flag live. |
| OZK | $40P | Nov-20-2026 | 4 | $0.81 | $0.05 | $20.00 | −$302.65 / -93.81% | `[11/5 ~10:0x ET intraday]`; basis $322.65; Today $0.00. MARK ONLY; bought 10/7 (Activity). WQ-428 SELL card windows passed, line rides, no order (DOCKET L709). Thesis ownership UNKNOWN (D-74). |
| WAL | $70P | Dec-18-2026 | 2 | $2.76 | $0.45 | $90.00 | −$461.33 / -83.68% | `[11/5 ~10:0x ET intraday]`; basis $551.33; Today −$124.00. MARK ONLY; buy fill/date unseen (D-84); ownership/card/approval UNKNOWN (D-74). **Fidelity 2 is DISTINCT from Robinhood 1; no inherited RH gate.** |
| WAL | $65P | Dec-18-2026 | 4 | $1.71 | $0.15 | $60.00 | −$622.65 / -91.22% | `[11/5 ~10:0x ET intraday]`; basis $682.65; Today −$140.00. MARK ONLY; bought 10/7 (Activity). WQ-429 SELL card windows passed, line rides, no order (DOCKET L709). Thesis ownership UNKNOWN (D-74). |
| ZION | $62.5P | Nov-20-2026 | 2 | $2.18 | $0.20 | $40.00 | −$395.33 / -90.82% | `[11/5 ~10:0x ET intraday]`; basis $435.33; Today −$50.00. MARK ONLY; buy fill/date unseen (D-84); ownership/card/approval UNKNOWN (D-74). |
| VLY | $12P | Dec-18-2026 | 1 | $0.16 | $0.10 | $10.00 | −$5.66 / -36.15% | `[11/5 ~10:0x ET intraday]`; basis $15.66; Today $0.00. MARK ONLY; the 10/22 $0.15 limit order filled (basis consistent, DERIVED); fill date UNSEEN. Card/owner UNKNOWN (D-74). |
| FLG | $10P | Mar-19-2027 | 1 | $0.71 | $0.30 | $30.00 | −$40.66 / -57.55% | `[11/5 ~10:0x ET intraday]`; basis $70.66; Today −$16.00. MARK ONLY; buy UNSEEN (D-90). Card/owner UNKNOWN (D-74). |


## Robinhood — satellite account (Individual)

*All holdings/figures below retained from the 9/29 source; carried DTE annotations are historical, not a current freshness assertion.*

> ⚠️ **NOT IN THIS EXPORT'S ACCOUNT — UNVERIFIED TODAY (not captured 11/5, 10/30, 10/29, 10/22, 10/20, 10/19, 10/14, 10/13, 10/11, 10/7, 10/1 or 9/30 — 37 days since the 9/29 card). Will's word 10/29 (TERRY window, PROME-supplied via `AGENTS/TERRY/research/2026-10-29_ira-snapshot/NOTE.md`): Robinhood positions "all dead" — written off by him; no capture evidences closure or values, so the rows stay.** 9/29 card: **account $295.15, BP $8.94** `[9/29 13:4x intraday]`; lines + BP = $290.15 ⇒ **$5.00 UNEXPLAINED (D-64)**. Per-line cost/value DERIVED from P/L ÷ P/L% (no Mark column ⇒ machine class `unverified` by design). The prediction-market line and the 9/01→9/25 dead-by-date bookings — USO $159C Sep-11 (bought 9/10, expired $0 — D-58) · QQQ $713C Sep-16 + USO $165C Sep-16 (both expired $0 — D-57) — verbatim → rotation 10/08 chunk B.

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **WAL $70P** | **Dec-18-2026** | 1 | **$2.20 ($220)** — bought 9/02 @ $2.20 (RH activity) ✓ | ≈$265.00 *(derived; mark ≈$2.65)* | ✅ **ON CARD 9/29 — +$45.00 / +20.45%** | TRY-WAL-ROLL70 (filled in Robinhood). Guard **`GATE-TERRY-ROLL70-EXIT`** *"WAL OFFICIAL CLOSE ≥ $81.90 on THREE CONSECUTIVE sessions"* — **0-of-3 as last recorded here** (REGINALD through 9/23, per TERRY STATUS 9/24; not re-read this pass). The option's +20.45% is not the gate — the gate reads WAL's close (rule 7). **$4.40 GTC sell order: CANCELLED / not there — Will 9/28** (`PROME/inbox/processed/2026-09-28_from-WAL_WQ-324-325-ruled-verbatim-and-4.40-GTC-cancelled.md`) ⇒ **no resting exit order; any take-profit is Will's manual act.** Time stop Fri 12/4. 78 DTE. **D-47** |
| **KRE $25P** | 1/15/2027 | 1 | $53.00 — card-derived ✓ | ≈$1.00 *(derived)* | ✅ **ON CARD 9/29 — −$52.00 / −98.11%** | Deep-OTM lottery; entry pre-7/16, never recorded — **D-54** (before the 9/01 activity view). 106 DTE |
| T | stock | 1 | — | — | ⚠️ no stocks card 9/29; no T row in RH activity 9/01→9/25 | Hypothesis: sold before 9/01, unconfirmed — **D-20**. The card no longer closes to the cent (D-64), so the 9/27 "no stock line" inference is weaker |

## Account UNATTRIBUTED — receipted fills not yet attributed to an account

*No rows. Landing place for a receipt that names no account (the parser admits it — TERRY `cfd9b9115`); history → rotation 10/30 chunk E.*

---

## ⚠️ Reconcile discrepancies (received 2026-11-05 10:01 ET; November 5 INTRADAY Fidelity lasts ~10:0x ET; quote clock not displayed; 11/5 Orders + Activity 10/30–11/5 as visible)

> Broker view > Will's word > desk record. Last prices are NOT settles and these are intraday. DTE from the receipt date only; no current executable bids. **Will manages his own expiries (`USER.md` § No expiry nagging, 10/20): DATED rows below are records, not prompts.** All prior duties survive unless explicitly closed. Prior section = `git show 083745bb1:FORGE/STATUS.md`; older → the commits in the header and rotations. Permanently UNKNOWN WQ-167: 9/2 USO135C sale price, never ask. This list records evidence and owners only; it carries no sell recommendation.

### Will supplies / PROME re-reads — facts owed

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-94** 🆕 | Second QQQ Nov-20 690P ×1: close not in view | 🟠 basis $1,339.665 unbooked | 2 held 10/30 ~13:2x; 1 sold 11/5 @ $28.83; 0 held 11/5. Every row 11/2→11/5 was read: no other 690P row. So the close sits below the view, on 10/30 after the capture (INFERRED by elimination). The 10/30 Day order to sell 1 @ $17.95 (last $17.70) is NOT shown filled. Cash test: 10/30 cash + pending $19,314.30 − the 172C buy $532.66 = $18,781.64 vs displayed $19,397.62 ⇒ **+$615.98 net of unseen rows** = this close − the opens in D-96. Of the lines held at that capture, only this one left out of view | HYPOTHESIS: a $17.95 fill nets ≈$1,794.30, leaving ≈$1,178.32 for the opens; the fit does not prove the order filled. Price, date, order UNKNOWN; nothing booked | **Will** Activity 10/30 below the view; **PROME** records; **TERRY** whole-line result |
| **D-96** 🆕 | Opens not in view; QQQ row pairing | 🟡 evidence | Sales with no open in view, neither on the 10/30 ~13:2x positions: QQQ Nov-02 680P +$52.34 · QQQ Nov-05 685P +$1,202.31 (opens 10/30 after capture, INFERRED). Row order within a day is NOT execution order: Nov-06 680P lists both sales below its buy, yet 0 held. Fee cents fit 17/17 buys of known quantity (×1 .66, ×2 .33, ×3 .99, ×4 .65, ×10 .63) ⇒ −$1,141.33 is ×2, matched by two ×1 sales: no unseen Nov-06 open | INFERRED: Nov-04 680P +$777.32 pairs with the 11/2 −$649.66 buy. ALTERNATIVE: it closes an unseen open and both buys expired (the EXPIRED row shows no quantity), which lowers the line by that open's cost. Cents favour the pairing: 2 unseen ×1 opens leave D-94's close ending .30 (fee .70, fits); 3 leave .96 (no such fee). A test of fit, not proof | **Will** Activity; **PROME** records |
| **D-95** 🆕 | $44.43 running-balance gap | 🟡 evidence | $19,397.62 (10/30 USO row) + $637.04 (11/2 APD) = $20,034.66 vs displayed $20,079.09: **+$44.43**, no row in view. Every other step to $28,218.18 ties; figures match the image. Not booked | CONJECTURE only: a month-end money-market dividend, the form of D-45 +$43.81 (8/31) and D-69 +$53.54 (9/30); no such row has ever been displayed | **Will** Activity 10/30–11/2; **PROME** records |
| **D-97** 🆕 | Share counts per stock sale row | 🟡 record | Activity rows carry amounts only. GLD: 10 implied by 28→18; 5 + 5 ≈ $362.90 / $363.69 (DERIVED). AAPL: Orders displays 2 on 11/5, so the 11/2 row is 1 share and the path is **3→2→0**; transcription § ④ says 3→1→0, which conflicts with its own § ② | The 5 + 5 split is implied, not displayed. Line totals unaffected | **PROME** corrects the transcription note; **Will** order detail if wanted |
| **D-89** | Working-order census | 🟡 NARROWED | 11/5 Orders panel (today only): three fills, no open order. The 10/30 $17.95 order's outcome moves to D-94. Orders placed before 11/5 not shown | Earlier working orders UNKNOWN | **Will**; **PROME** books fills only from a capture |
| **D-90** | 10/22→10/29 ledger (WQ-548, L921) | 🟡 NARROWED | **L921 VERIFIED at the file: lines 11 and 14 of the 10/23 view are USO Oct-30 165C @ $7.15, $714.32 and USO Oct-23 163C @ $4.36, $435.34; both booked.** The same view also answers AAPL −1, the spread opening and the 705P ×2 buy. 11/5 cash = running balance, so the $962.00 step is gone from view. **STILL UNSEEN:** GLD +3 · TBT +5 · KRE 68P ×10, GLD 375C ×2, VLY, FLG buys · USO Oct-28 165C ×1, USO Oct-30 165C ×1, CMG 28P outcomes · any 10/28–10/29 rows · the fate of the 10/23 Buy 4 FLG @ $0.52 order (the held ×1 at $0.71 cannot be that limit). DERIVED: of the 10/29 identity's +$800.51 residual, +$30.47 is booked, leaving **+$770.04** for the three unseen outcomes and other flows; cash unexplained before the first visible row falls from −$1,604.84 to −$1,303.11 | HYPOTHESIS: these sit on 10/22 after 11:01 ET or below the cut | **Will** supplies the rest of Activity 10/22→10/29; **PROME** records |
| **D-60** | Fidelity expiring-option handling | 🟡 NARROWED | Three paths seen: sold by Will; OPTION LIQUIDATION on expiry day (CRWV Oct-23 56P, QQQ Oct-26 710P/705P); lapse as an EXPIRED row posted next day, no amount (QQQ Oct-22 717C, GLD Nov-02 375C, QQQ Nov-04 680P). Mechanics only: an exercised put SELLS 100 shares per contract at the strike | INFERRED: which contracts the broker liquidates vs lets lapse — trigger and timing never stated; ITM exercise/IRA handling never observed | **Will** broker policy |
| **D-88** | QQQ Oct-20 715P ×1 disposition | 🟡 record | Unchanged: absent since 10/22; basis $200.66; +$17.34 unexplained in the 10/20 cash bridge | HYPOTHESIS (unchanged): consistent with a sale near $0.18 ⇒ conditional −$183.32; nothing booked | **Will** 10/20 Activity below the cut; **PROME** records |
| **D-85** | QQQ Oct-20 719P basis allocation | 🟡 NARROWED (unchanged) | Cohort −$120.99 booked on the 10/22 mirror; per-leg split −$67.67 or −$68.67 | Which per-leg basis the broker treats as authoritative UNKNOWN | **PROME** records; **Will** lots if ever needed |
| **D-74** | Fidelity bank-put ownership / new-line scope | 🟡 record | Bank/credit put cluster 41 contracts / 14 lines, basis $6,644.24, value $554.00 `[11/5 ~10:0x ET intraday]` (28 / $4,646.62 on TERRY's 10/24 view). KRE Nov-27 68P ×10, VLY 12P, FLG 10P, Fidelity WAL70P2, ZION62.5P2, KRE 66P/70P: owner/card/approval UNKNOWN. WAL65P4/OZK40P4 card windows passed (L709) | No inherited gate or approval from same symbol/heading | **PROME** scope; **Will/REGINALD/TERRY** |
| **D-77** | Off-thesis ownership/cards | 🟡 record | No contract-specific card: USO Nov-11 172C (NEW), USO Nov-20 170C (Will's hand; WQ-491 idea not taken), KRE67P. Closed with no card seen: QQQ Nov-02 715P, GLD Nov-02 375C, AAPL Nov-04 345C, QQQ Nov-02/04/05/06 lines | TERRY's spread card mentions "the two short-dated QQQ put lines" as the same Nasdaq-downside bet; which contracts is not stated here | **PROME** scope; **Will/TERRY** |
| **D-70** | Management mappings | 🟡 source changed — 1 mapping withheld | PROME source-hash review 2026-11-04: 46 of 47 mappings match their recorded evidence; the sole withheld mapping is **Robinhood WAL Dec-18 70P**, sourced to TERRY's `WAL_dec18-70P-duration-roll_2026-09-01.md`. That card now reads DEAD / written off by Will 10/29, but the actual Robinhood holding or closure remains UNKNOWN. Its old hash stays unchanged and the mapping stays WITHHELD; no mapping is reactivated to complete the display. Other mappings' valid hashes are evidence-vintage checks, not current broker truth | Mapping is not a card, trade approval, or proof of a current position. Fresh Robinhood evidence is required only to book the actual holding/closure, not to correct this status | **PROME** mapping/record; **Will** supplies Robinhood evidence if closure is to be booked; **TERRY** card owner |
| **D-91** | Short-leg representation (consumer interface) | 🟡 no short row live | No signed-Qty row live, so `desk_attention.holdings()` does not error. Convention kept in the footer | The next short re-trips `desk_attention.py` until DOCKET L870 lands | **PROME** (L870); **TERRY** (`positions_from_forge.py`) |
| **D-87** | Fidelity prior-day reference vs mirror marks | 🟡 record | 10/30: on 14 option rows the reference ≠ the 10/29 post-close last, Σ gap **$3,053.00**; largest KRE Nov-27 68P $2.30 vs $0.18. 11/5 not testable: the mirror holds no 11/4 mark | INFERRED: options' reference is a closing mark/quote, not the last trade — UNVERIFIED. No value or G/L figure affected | **PROME** record |
| **D-84** | Unseen 10/19 entries and quantity changes | 🟡 evidence | Unchanged: Fidelity WAL70P2, ZION62.5P2 buys unseen; GLD residual2 $764.28; VLO 2→3; USO 37→35; CMG 2→1. CRWV now resolved (D-90) | Dates/prices/proceeds/realized UNKNOWN | **Will** earlier Activity; **PROME** records |
| **D-86** | Three expired contracts absent (Oct-15/16) | 🟡 outcome evidence owed | QQQ Oct15 715P, Oct16 735C, HBAN Oct16 16P; unchanged | Sale/exercise/lapse UNKNOWN | **Will** earlier Activity; **PROME** records |
| **D-78** | VLO extra-share scope | 🟡 scope before action | 2 sh, basis $884.73: the added shares; the $412.00 original sold 11/5. TERRY card 11/5: "Added 2 shares: Will's hand, no TERRY rule" | Neither added share extends original management scope | **Will** authorization; **PROME/TERRY** scope |
| **D-76** | Detailed fills/lots | 🟡 evidence | 11/5 fills carry prices (Orders); ledger rows carry net amounts only. Lot relief ≠ average: GLD $3,758.86 vs 10 × $374.63; USO $594.42 vs 5 × $121.90 | No broker realized-P/L report; all realized DERIVED | **Will** lots/fills; **PROME/TERRY** integrate |
| **D-80** | Prior unseen GLD+3 / HBAN−1 / QQQ Oct16 725P opening | 🟡 carried | 10/15 gaps unchanged | Nothing resolved by later holdings | **Will** earlier Activity; **PROME** records |
| **D-83** | Clock / Robinhood | 🟡 standing | Receipt 11/5 10:01 ET; INTRADAY lasts ~10:0x ET, quote clock not displayed; not closes. Robinhood 9/29 card is 37 days old; Will's word 10/29: "all dead", written off — rows retained, unverified | RH values may be ≈$0; no closure booked without a capture | **Will** RH view if he wants it closed out; **PROME** records |
| **D-81** | Historical 10/14 cash mismatch | 🟡 record | +$16.58 vs post-744P balance; later captures tie | Different cut or unseen item UNVERIFIED | **PROME** record |
| **D-79** | Quote/value precision | 🟡 record | 11/5: 19 values tie to the cent. VLO fill $366.665 → $366.67; half of the 690P basis = $1,339.665, a half cent inside the booked total. Option avg cost × qty ≠ basis by fees | Rounding source UNVERIFIED; no total affected | **PROME** evidence |
| **D-75 · D-66 · D-69 · D-62 · D-63 · D-64 · D-65 · D-61 · D-59 · D-45 · D-55 · D-28 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1** | **Carried discrepancies (18) — every row still OPEN; rows verbatim → rotation 10/08 chunk D1 (D-75) + D2 (the other 17)** | 🟡 carried | None closed, re-dated or re-owned; every cell unchanged in the record. Ticker-bearing items, for the text scan: STNG (D-17) · RH QQQ $715P Aug-31 (D-28) · RH KRE $25P entry (D-54) · RH WAL $77.5P Aug-21 sale (D-18) · the RH T share (D-20) · AAPL 5-sh sale pre-7/30 (D-1) · D-75 (OZK 40P basis 1¢; mirror carries $322.65, record only) | Returns to this table when its state changes | As recorded, per row: **Will** — D-66 · D-69 · D-63 · D-64 · D-61 · D-59 · D-45 · D-55 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1; **RH history before 9/01** — D-28; **PROME** — D-62 · D-65 (re-reads of desktop-local images) · D-75 (record) |

*D-69 missing +$53.54 remains OPEN. D-66 includes every fill clock not shown (the 11/5 fills carry no time). D-71 broker leg remains CLOSED (cohort +$142.44, rotation 10/15 chunk A); D-72/D-73 historical closures unchanged. This pass CLOSED D-93 (690P flat; card CLOSED) and D-82 (L709 RESOLVED 10/31, cards lapsed; OZK ×4 and WAL 65P ×4 still held 11/5, no order); narrowed D-90, D-89, D-60, D-77; opened D-94 to D-97.*

*Guards: each management line's text sits beside its number in the rows above (GLD rails, VLO HELD-01, KRE65P time stop, USO no live rule). D-47 RH WAL70P `GATE-TERRY-ROLL70-EXIT` last recorded 0-of-3 (stale). Option P/L percentages are marks, not harvest/disarm readings; no gate adjudicated this pass.*

---

## Immediate Actions (11/5 10:01 ET intraday receipt) — evidence and records only

| Item | State | Owner |
|---|---|---|
| 🟠 D-94 / D-96 / D-95: Activity on 10/30 below the view — second 690P close, two opens, the $44.43 | record from Will's next capture | **Will**; **PROME** |
| 🟡 D-97 transcription note AAPL 3→1→0 vs its own Orders panel (2 shares) | correct at the source | **PROME** |
| 🟡 D-90 rest of Activity 10/22→10/29; D-70 mappings; D-74/D-77; all other D-rows and 18 carried duties remain | evidence / integration / scope | **Will** ledger; **PROME/TERRY** |

---

*History → `_archive/JOURNAL.md`, existing rotations and Git; immediately prior whole mirror = `git show 083745bb1:FORGE/STATUS.md` | `PORTFOLIO.md` FROZEN Feb snapshot, never live | Truth = Will/broker off-repo | Current evidence → `PROME/data/2026-11-05_broker-capture-TRANSCRIPTION.md` (19 Fidelity positions, 11/5 Orders panel, Activity 10/30–11/5 as visible; posted 10:01 ET, intraday lasts ~10:0x ET; quote clock not displayed). Robinhood source remains 9/29; prior evidence/history survives in Git.*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumers: `AGENTS/TERRY/scripts/positions_from_forge.py` (sections `^## (Fidelity|Robinhood)` + `^## Account <NAME>`; table headers by prefix; cell text — emphasis and strikethrough visible) · `PROME/tools/desk_attention.py` `holdings()` (same sections; `Qty` + `Ticker|Strike|Position` headers; expiry year from `**Updated:**`) · `PROME/tools/will_brief.py` `parse_money()` (header before the first `## `: `account total:**`, `money market):** $X (Y%)`, `**Updated:** YYYY-MM-DD`, `marks = [Fri ]YYYY-MM-DD`) · `FORGE/position_management.tsv` `source_sha256` (any byte change here withholds every mapping sourced to this file until PROME re-reviews) · `AGENTS/BRENT/scripts/pending_receipts.py` (text-level closure candidates). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself here in the same commit that starts parsing. *(Pass notes 9/27 → 10/8 → rotation 10/08 chunk G. Conventions they set, still binding: the header money line keeps the shape `will_brief.py` reads; option expiries carry the year; the `Mark <m/d>` header is prefix-bound; terminal records live in italic lines, which no parser reads as rows. 10/29: a SHORT option leg carries a signed Qty `−N` and a negative value — D-91.)*
