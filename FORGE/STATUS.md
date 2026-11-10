# FORGE — Trading Operations

Dashboard management mapping → [position_management.tsv](position_management.tsv); maintenance contract → [dashboard notes](DASHBOARD.md). Holdings remain in this file; approval, order and fill evidence are separate. A changed evidence source invalidates its management mapping until reviewed.

> ✅ **2026-11-10 (Tue) — RECONCILE BY ANVIL to Will's captures posted 15:13 ET in the PROME window: Fidelity positions view + Past-30-days Activity as visible (Nov-02 APD row, clipped, → Nov-10) + the Robinhood Individual card. INTRADAY: marks are Fidelity last prices in the November 10 session — NOT a close, NOT settles, NOT executable quotes; no clock on the captures.** Source `PROME/data/2026-11-10_broker-capture-TRANSCRIPTION.md` (PROME prome-07; ANVIL re-read all three images). ANVIL independently verified **21/21** row values and open G/L to the cent: positions **$13,789.35** + cash **$31,871.13** + pending **−$1,053.33** = **$44,607.15** = displayed total; Σ Today −$1,018.82 and Σ open G/L −$6,659.28 tie; 23/23 running-balance steps tie; pending = the 11/10 QQQ 668P buy. Against last mirror `6db8d1d6f` (11/5 intraday, 19 Fidelity rows): **2 NEW (QQQ Nov-13 668P ×2, QQQ Nov-10 670P ×2) / 0 QTY CHANGE / 0 GONE / 19 MARK ONLY.** Two more contracts opened and closed between captures, off the positions view (D-100).
>
> ⚠️ **ACCOUNT SCOPE — ONE Fidelity Traditional IRA (•1326; last four only, the repo is public) for every Fidelity row. Robinhood Individual: separate card 11/10, own section, not in the Fidelity total (D-98). Absence from a Fidelity view proves no closure. No Orders panel in this capture: working orders UNKNOWN (D-89).**
>
> **Updated:** 2026-11-10 · marks = 2026-11-10 intraday (Fidelity last prices, posted 15:13 ET; quote clock not displayed; not a close, not settles) — all Fidelity cells `[11/10 intraday]` · **Fidelity cash (money market):** $31,871.13 (71.45%) + **Pending activity −$1,053.33** (= the 11/10 QQQ 668P buy, still "Processing"; already in the total, never add again) · **Fidelity account total:** $44,607.15 (Today −$1,018.82 / −2.23%; open G/L −$6,659.28 / −32.57% on displayed basis $20,448.63). Snapshot change vs 11/5: **−$234.29 = positions +$1,119.76 + cash +$3,652.95 + pending −$5,007.00** = realized −$1.01 + unexplained cash +$3.62 (D-101) + open G/L change −$236.90; not a daily return. **Realized booked this pass, DERIVED: −$1.01 (D-100).** Robinhood $440.86 `[RH 11/10 intraday]` (D-98). Prior header, rows and terminal records → `FORGE/_archive/STATUS_ROTATION_2026-11-10.md` chunks A–G, byte-exact, and Git (`6db8d1d6f`, `a478aa399`); no history rebooked.

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (its own header names the current base and amendment count). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All Fidelity marks `[11/10 intraday]`; no clock on the capture; intraday lasts, not closes. Cost = basis ÷ qty (DERIVED); Mark = the displayed last (value = last × qty, verified); not exact fills.*

| Ticker | Type | Qty | Cost | Mark 11/10 intraday | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| GLD | Stock | 18 | $373.93 | $369.3522 | $6,648.33 | −$82.34 / −1.23% | Today −$183.21; MARK ONLY; basis $6,730.67 (value is 1¢ below last × qty, D-79). **`MGMT-GLD-SHARES-OCT24` (TERRY rails, MIDAS WQ-451 lines): 1-month lines "GLD close < $360.71" (TERRY recorded it crossed at the 10/30 close $355.78; card note 1: a price-path line, "not by itself a trim signal") and "GLD close > $391.08". This $369.3522 is an INTRADAY last, $8.64 above the first and $21.73 below the second; the lines read the CLOSE — not graded here.** The card's choices are Will's, none recommended. 28→18 sale history → chunk B. MIDAS; largest line. |
| USO | Stock | 30 | $122.40 | $141.48 | $4,244.40 | +$572.39 / +15.58% | Today −$35.40; MARK ONLY; basis $3,672.01. **WQ-200 DECLINED 9/10: NO harvest/give-back rule live; Will manages by hand** — the +15.58% is a mark, not a gate reading. 10/23 sale history → chunk B. BRENT thesis. |
| VLO | Stock | 2 | $442.37 | $350.81 | $701.62 | −$183.11 / −20.70% | Today −$11.88; MARK ONLY; basis $884.73 = the two added shares. `GATE-TERRY-VLO-HELD-01` RESOLVED 2026-11-05 EXECUTED in PROME/GATES.tsv (the original $412.00 share sold 11/5, −$45.33 booked then; chunk B). The −20.70% is a mark and no gate reads it (D-78). `GATE-TERRY-VLO-SCALE` stays TERMINAL. |

*CLOSED stock lines AAPL ×3 and APD ×2 (11/2–11/5, booked on the 11/5 mirror) → chunk B. No live AAPL, APD or TBT line.*

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

*No live event-box rows; terminal records → rotation 10/30 chunk D, byte-exact.*

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, owned by no agent unless separately recorded. **Will manages his own expiries** (`USER.md` § No expiry nagging, 10/20 11:32 ET; supersedes the 9/30 sell-or-roll rail as an instruction): no expiry reminders or sell pushes, and a collapsed line may expire. This mirror records holdings and evidence only; dispositions are read from his captures, never inferred. The capture establishes holdings, not fills, cards or approvals; grouping is navigation, not a thesis or scope ruling. Last marks are not executable bids. Receipt-day DTE is scheduling only.

| Ticker | Strike | Expiry | Qty | Cost | Mark 11/10 intraday | Value | P&L | Note |
|--------|--------|--------|-----|------|---------------|-------|-----|------|
| QQQ | $668P | Nov-13-2026 | 2 | $5.27 | $5.07 | $1,014.00 | −$39.33 / −3.74% | `[11/10 intraday]`; basis $1,053.33; Today −$39.33 (bought today). **NEW: BOUGHT OPENING 11/10 −$1,053.33** (Activity, "Processing" = the pending; ×2 by fee cents .33). Broker "NE" badge (D-102). No card seen (D-77). |
| QQQ | $670P | Nov-10-2026 | 2 | $1.52 | $0.11 | $22.00 | −$281.33 / −92.75% | `[11/10 intraday]`; basis $303.33; Today −$292.00. **NEW: BOUGHT OPENING 11/9 −$303.33** (Activity; ×2 by fee cents). Broker "NE" badge (D-102). No card seen (D-77). |
| USO | $172C | Nov-11-2026 | 1 | $5.33 | $0.01 | $1.00 | −$531.66 / −99.82% | `[11/10 intraday]`; basis $532.66; Today $0.00. MARK ONLY; bought open 10/30 (Activity). Broker "NE" badge, as 11/5 (D-102). Card/owner/approval UNKNOWN (D-77). |
| USO | $170C | Nov-20-2026 | 1 | $6.28 | $0.48 | $48.00 | −$579.66 / −92.36% | `[11/10 intraday]`; basis $627.66; Today −$22.00. MARK ONLY; bought open 10/27. Will 10/29 (PROME-supplied): his own hand; WQ-491 idea NOT taken — this line is not that card. Card/owner/approval UNKNOWN (D-77). |

*CLOSED since the 11/5 capture (Activity, broker-verified amounts; quantities not displayed, ×1 by fee cents; realized DERIVED):* **QQQ Nov-09 650P ×1** bought 11/5 −$739.66, sold 11/5 +$1,262.31 ⇒ **+$522.65** (pairing INFERRED by elimination, D-100) · **QQQ Nov-09 655P ×1** bought 11/6 −$523.66, EXPIRED as of 11/9 (row 11/10, no amount) ⇒ **−$523.66**. **Total −$1.01.** The QQQ Nov-04 680P rows in view (+$127.66 round trip, −$464.66 expiry) were booked on the 11/5 mirror — not booked again.

*Prior terminal records: 10/30→11/5 closes (+$4,168.14) and the 10/23 exits (+$30.47) → chunk C; 10/30 closes +$4,634.95 and 10/23–10/26 outcomes −$698.90 → `git show 3064691ae:FORGE/STATUS.md`; 10/22 and earlier → rotation 10/30 chunk A, byte-exact — never add again.*

## Fidelity — Thesis Puts

*Instrument grouping is navigation, not approval: the Fidelity WAL/OZK rows below are Will-direct holdings (bought 10/7, Activity); thesis/desk ownership and management approval are NOT established by the broker view.*

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

*No live TLT line; terminal records → rotation 10/30 chunk B, byte-exact.*

### KRE — regional banks (REGINALD)

*All seven rows `[11/10 intraday]`, MARK ONLY (qty and basis as 11/5); the 68P ×10 buy is still UNSEEN (D-90); grouping is not approval/ownership (D-74). Prior Sep30 roll/exits remain historical in Git/rotation 10/01 chunk D.*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $66P | Nov-20-2026 | 3 | $0.45 | $0.05 | $15.00 | −$118.99 / −88.81%; basis $133.99; Today −$21.00; MARK ONLY; bought 10/22 @$0.44 (10/22 ledger); card/owner UNKNOWN (D-74) |
| $70P | Nov-27-2026 | 2 | $1.41 | $0.43 | $86.00 | −$195.33 / −69.44%; basis $281.33; Today −$38.00; MARK ONLY; bought 10/22 @$1.40 (10/22 ledger); card/owner UNKNOWN (D-74) |
| $68P | Nov-27-2026 | 10 | $0.73 | $0.23 | $230.00 | −$496.63 / −68.35%; basis $726.63; Today +$10.00; MARK ONLY; buy date/price UNSEEN (D-90); card/owner UNKNOWN (D-74) |
| $67P | Nov-27-2026 | 4 | $1.28 | $0.14 | $56.00 | −$454.65 / −89.04%; basis $510.65; Today −$72.00; MARK ONLY; bought 10/12 net $510.65; card/owner UNKNOWN (D-76/D-77) |
| $60P | Dec-18-2026 | 2 | $2.57 | $0.15 | $30.00 | −$483.34 / −94.16%; basis $513.34; Today −$18.00; MARK ONLY |
| $60P | Dec-18-2026 | 3 (M) | $2.93 | $0.15 | $45.00 | −$833.02 / −94.88%; basis $878.02; Today −$27.00; MARK ONLY; broker "M" badge (PROME's transcription reads it as a margin lot; earlier mirrors read a multi-lot marker — UNVERIFIED); total 5 Dec-18 60P across 2 lots |
| $65P | Dec-31-2026 | 2 | $1.69 | $0.44 | $88.00 | −$249.33 / −73.92%; basis $337.33; Today −$92.00; MARK ONLY; `MGMT-KRE65P-DEC31`: hard stop Thu 12/31 15:00 ET (5ce609f80) — a time stop, not a price gate |

### WAL (REGINALD) — Sep-18 pair EXPIRED

*Sep-18 pair EXPIRED ⇒ −$1,519.34 → rotation 10/30 chunk C, byte-exact. RH WAL $77.5P Aug-21 sale P&L UNRECORDED (D-18).*

### Other puts

*QQQ Nov-20 690P: no live line since 11/5; history → chunk D; the second contract's close is D-94. Card `IDEA-QQQ-PUTWALL-OCT22` CLOSED (TERRY `42b47b6b8`).*

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18-2026 | 1 | $11.85 | $0.25 | $25.00 | −$1,159.67 / −97.89% | `[11/10 intraday]`; basis $1,184.67; Today −$30.00. MARK ONLY; the 11/5 "E" badge is not shown 11/10 (D-102); BROCK vehicle; HOLD ruled 8/13 (private-credit batch §②), vehicle-mismatch flag live. |
| OZK | $40P | Nov-20-2026 | 4 | $0.81 | $0.05 | $20.00 | −$302.65 / −93.81% | `[11/10 intraday]`; basis $322.65; Today $0.00. MARK ONLY; bought 10/7 (Activity). WQ-428 SELL card windows passed, line rides, no order seen (DOCKET L709). Thesis ownership UNKNOWN (D-74). |
| WAL | $70P | Dec-18-2026 | 2 | $2.76 | $1.15 | $230.00 | −$321.33 / −58.29% | `[11/10 intraday]`; basis $551.33; Today +$18.00. MARK ONLY; buy fill/date unseen (D-84); ownership/card/approval UNKNOWN (D-74). **Fidelity 2 is DISTINCT from Robinhood 1 (Nov-20); no inherited RH gate.** |
| WAL | $65P | Dec-18-2026 | 4 | $1.71 | $0.45 | $180.00 | −$502.65 / −73.64% | `[11/10 intraday]`; basis $682.65; Today −$80.00. MARK ONLY; bought 10/7 (Activity). WQ-429 SELL card windows passed, line rides, no order seen (DOCKET L709). Thesis ownership UNKNOWN (D-74). |
| ZION | $62.5P | Nov-20-2026 | 2 | $2.18 | $0.20 | $40.00 | −$395.33 / −90.82% | `[11/10 intraday]`; basis $435.33; Today −$80.00. MARK ONLY; buy fill/date unseen (D-84); ownership/card/approval UNKNOWN (D-74). |
| VLY | $12P | Dec-18-2026 | 1 | $0.16 | $0.10 | $10.00 | −$5.66 / −36.15% | `[11/10 intraday]`; basis $15.66; Today $0.00. MARK ONLY; the 10/22 $0.15 limit order filled (basis consistent, DERIVED); fill date UNSEEN. Card/owner UNKNOWN (D-74). |
| FLG | $10P | Mar-19-2027 | 1 | $0.71 | $0.55 | $55.00 | −$15.66 / −22.17% | `[11/10 intraday]`; basis $70.66; Today −$5.00. MARK ONLY; buy UNSEEN (D-90). Card/owner UNKNOWN (D-74). |


## Robinhood — satellite account (Individual)

*All cells `[RH 11/10 intraday, posted 15:13 ET]`, T excepted. $ and % per line only: cost and value DERIVED from $ ÷ % (no Mark column ⇒ machine class `unverified` by design).*

> ⚠️ **INTRADAY 11/10, OPTIONS LIST ONLY; NOTHING TIES TO THE CENT (D-98).** One card Will posted 15:13 ET; transcription § ②. **Account value $440.86 · Today −$93.04 / −17.43%, so $533.90 at the prior close (DERIVED).** No buying power, Recent list or stock list shown. Σ DERIVED line values $416.75 leaves $24.11 unshown (cash or rounding, DERIVED). Per-line $ figures read as total return, INFERRED: on the three carried lines they reproduce the 11/5 costs exactly. A yellow "6 days left" badge, subject not shown (D-102). Vs `6db8d1d6f` (11/5 after close): **3 NEW / 0 QTY CHANGE / 2 GONE / 3 MARK ONLY / T UNKNOWN.** 11/5 section → chunk E, byte-exact.

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **QQQ $675P** | Nov-10-2026 | 1 | ≈$2.45 ($244.76 DERIVED; range $244.33–$245.18 from the rounded %) | ≈$237.76 *(DERIVED)* | 🆕 **NEW: −$7.00 / −2.86%** | Fill and date NOT SHOWN. No card seen. |
| **QQQ $669P** | Nov-10-2026 | 1 | $0.41 ($41.00 DERIVED) | ≈$8.00 *(DERIVED)* | 🆕 **NEW: −$33.00 / −80.49%** | Fill and date NOT SHOWN. No card seen. |
| **KRE $71.5P** | Nov-13-2026 | 2 | ≈$0.85 ($169.99 DERIVED; range $169.98–$170.00) | ≈$37.99 *(DERIVED)* | 🆕 **NEW: −$132.00 / −77.65%** | Card reads "2 Buys"; fills NOT SHOWN; year 2026 INFERRED (card shows 11/13). No card seen. |
| **WAL $70P** | Nov-20-2026 | 1 | $0.40 ($40) | ≈$38.00 *(DERIVED)* | ✅ **MARK ONLY: −$2.00 / −5.00%** | Open unseen. No card seen. Not the Dec-18 line. |
| **UNG $10.5C** | Dec-24-2026 | 1 | $0.55 ($55) | ≈$94.00 *(DERIVED)* | ✅ **MARK ONLY: +$39.00 / +70.91%** | Will: "I did buy UNG". NOT the WQ-573 card. Mapped NOTE-UNG105C-DEC24, TERRY. |
| **KRE $25P** | 1/15/2027 | 1 | $0.53 ($53) | ≈$1.00 *(DERIVED)* | ✅ **MARK ONLY: −$52.00 / −98.11%**, as 9/29 | "KRE $25 Put" as displayed. Entry never recorded — **D-54**. |
| T | stock | 1 | — | — | ⚠️ UNKNOWN: the 11/10 card shows the Options list only; no stock line seen 11/5 either | Hypothesis: sold before 9/01, unconfirmed — **D-20**. |

*GONE since 11/5, disposition NOT SHOWN: **QQQ $640P Nov-06-2026 ×1** (cost $524 DERIVED) and **USO $148C Nov-06-2026 ×1** ($236): both dated 11/6, on the 11/5 after-close card, not on the 11/10 card. Sold or expired NOT SHOWN; no price; nothing booked (D-98).*

*Earlier GONE lines (QQQ $651P Nov-05, WAL $70P Dec-18; nothing booked; `GATE-TERRY-ROLL70-EXIT` RETIRED 11/5, WQ-610 A) → chunk E.*

## Account UNATTRIBUTED — receipted fills not yet attributed to an account

*No rows. Landing place for a receipt that names no account (the parser admits it — TERRY `cfd9b9115`); history → rotation 10/30 chunk E.*

---

## ⚠️ Reconcile discrepancies (received 2026-11-10 15:13 ET; November 10 INTRADAY Fidelity lasts, no clock on the captures; Activity Nov-02 → Nov-10 as visible; Robinhood card intraday)

> Broker view > Will's word > desk record. Last prices are NOT settles and these are intraday. **Will manages his own expiries (`USER.md` § No expiry nagging, 10/20): DATED rows below are records, never prompts; this list carries no sell, roll or timing recommendation.** Ranked by how soon the evidence ages, dated contracts first. All prior duties survive unless explicitly closed. The 11/5 section, every row verbatim → `FORGE/_archive/STATUS_ROTATION_2026-11-10.md` chunk F ("chunk F" below). Permanently UNKNOWN WQ-167: 9/2 USO135C sale price, never ask.

### Will supplies / PROME re-reads — facts owed

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-100** 🆕 | QQQ Nov-09 650P: one buy row, one sale row, both 11/5 | 🟠 booked on an inference | Both rows post after the 11/5 ~10:0x capture: neither its positions view nor its Activity shows a Nov-09 650P. The running balance is unbroken $20,079.09 → $31,867.51 (23/23 steps), so no unseen money row sits 11/2→11/9. No Nov-09 650P in the 11/10 positions view and no EXPIRED row for it, while the same-expiry 655P's EXPIRED row did post 11/10. Fee cents: −$739.66 = ×1 buy (.66), +$1,262.31 = ×1 sale (.31). The sale sits below the buy in balance order, the same pattern as the same-day Nov-06 680P and Nov-04 680P trips on 11/2 (row order is not execution order). **Booked +$522.65** | INFERRED by elimination: one same-day round trip. PROME's § ④ reading (buy disposition NOT SHOWN; the sale's opening not in view) is REFUSED on the tests above. ALTERNATIVE, low weight: two separate lots, which needs an opening older than any view and a closing row absent from this one; no displayed quantity excludes it | **Will** row detail if wanted; **PROME** records |
| **D-98** | Robinhood flow 11/5 → 11/10; GONE and NEW lines | 🟠 nothing closed | 11/10 card: $440.86, so $533.90 prior close (DERIVED); options list only. **GONE:** QQQ $640P and USO $148C, both Nov-06, sold or expired NOT SHOWN. **NEW:** QQQ $675P, $669P (11/10), KRE $71.5P ×2 (11/13); fills and dates NOT SHOWN; costs $455.75 DERIVED. **④ DERIVED identity, if the $24.11 residual is cash:** 11/5 BP $865.15 → $24.11 = −$841.04 = −$455.75 new costs + X (640P/148C proceeds, ≥ 0) + Y, so **Y ≤ −$385.29**: at least that much outflow unseen. Per-line $ sum −$187.00 vs Today −$93.04, so the line figures are not today's change (INFERRED total return). 11/5 gaps ①–③ ($1,058.37, $20.00, ≥ $66.22 outflow) unchanged, verbatim in chunk F | HYPOTHESIS: 640P/148C lapsed 11/6; Y = losing trades between captures, a withdrawal, or the residual is not cash. Nothing booked | **Will** RH history 11/5→11/10 and cash; **PROME** records |
| **D-102** 🆕 | Unexplained broker badges | 🟡 record | Fidelity "NE" on QQQ Nov-10 670P, USO Nov-11 172C, QQQ Nov-13 668P; not on any Nov-20 or later row. USO 172C carried it on 11/5 at 6 days; Nov-20 rows lack it at 10 days. APO's 11/5 "E" badge is not shown 11/10. Robinhood "6 days left" (11/16 counting from 11/10): no RH line expires 11/16 (11/10, 11/13, 11/20, 12/24, 1/15) | CONJECTURE: "NE" = a near-expiration flag (fits both captures); the RH badge = an account-level countdown (offer or subscription). Neither meaning is stated on a capture | **Will** if wanted; **PROME** records |
| **D-101** 🆕 | Fidelity cash +$3.62 | 🟡 evidence | Positions-screen cash $31,871.13 vs last settled balance $31,867.51 (11/9 row). The 11/10 rows are the 668P buy (in pending, already in the total) and a no-amount expiry; no visible row carries $3.62. Not booked | CONJECTURE only: a money-market dividend or accrual not yet posted, the form of D-95 +$44.43, D-69 +$53.54, D-45 +$43.81; never displayed | **Will** Activity; **PROME** records |
| **D-94** | Second QQQ Nov-20 690P ×1: close not in view | 🟠 basis $1,339.665 unbooked | UNCHANGED: this view ends at Nov-02 (clipped APD row) and shows one 690P sale only (11/5 +$2,882.28, booked 11/5). Close INFERRED on 10/30 after that capture; the 10/30 $17.95 Day order NOT shown filled | HYPOTHESIS: a $17.95 fill nets ≈$1,794.30; price, date and order UNKNOWN; nothing booked. Full row → chunk F | **Will** Activity 10/30; **PROME** records; **TERRY** whole-line result |
| **D-96** | Opens not in view; QQQ row pairing | 🟡 evidence | UNCHANGED: QQQ Nov-02 680P +$52.34 and Nov-05 685P +$1,202.31 sales still have no opening in view (10/30 after capture, INFERRED); not booked. Its fee-cents table now also reads the 11/5–11/10 rows (D-100) | Nov-04 680P pairing INFERRED, alternative as written. Full row → chunk F | **Will** Activity; **PROME** records |
| **D-95** | $44.43 running-balance gap | 🟡 evidence | UNCHANGED: between the 10/30 USO row and the 11/2 APD row; this view clips the APD row and shows nothing earlier. Not booked | CONJECTURE: a month-end money-market dividend (D-45, D-69 form); never displayed | **Will** Activity 10/30–11/2; **PROME** records |
| **D-97** | Share counts per stock sale row | 🟡 record | UNCHANGED: Activity rows still collapsed, amounts only. GLD 5 + 5 implied; AAPL 3→2→0 per the 11/5 Orders panel | The 5 + 5 split is implied, not displayed. Full row → chunk F | **PROME** corrects the 11/5 transcription note; **Will** order detail if wanted |
| **D-90** | 10/22→10/29 ledger (WQ-548, L921) | 🟡 NARROWED (unchanged 11/10) | Nothing before Nov-02 in this view. **STILL UNSEEN:** GLD +3 · TBT +5 · KRE 68P ×10, GLD 375C ×2, VLY, FLG buys · USO Oct-28 165C ×1, USO Oct-30 165C ×1, CMG 28P outcomes · 10/28–10/29 rows · the 10/23 Buy 4 FLG @ $0.52 order. +$770.04 residual DERIVED | HYPOTHESIS: on 10/22 after 11:01 ET or below the cut. Full row → chunk F | **Will** rest of Activity 10/22→10/29; **PROME** records |
| **D-89** | Working-order census | 🟡 record | No Orders panel in the 11/10 capture. 11/5 panel: three fills, no open order | Working orders since 11/5 UNKNOWN | **Will**; **PROME** books fills only from a capture |
| **D-60** | Fidelity expiring-option handling | 🟡 NARROWED | Paths seen: sold by Will; OPTION LIQUIDATION on expiry day (CRWV Oct-23 56P, QQQ Oct-26 710P/705P); lapse as an EXPIRED row posted next day, no amount (QQQ Oct-22 717C, GLD Nov-02 375C, QQQ Nov-04 680P, **QQQ Nov-09 655P: row 11/10, as of 11/9**). Mechanics only: an exercised put SELLS 100 shares per contract at the strike | INFERRED: which contracts the broker liquidates vs lets lapse; trigger and timing never stated; ITM exercise never observed | **Will** broker policy |
| **D-74** | Fidelity bank-put ownership / new-line scope | 🟡 record | Bank/credit put cluster 41 contracts / 14 lines, basis $6,644.24, value $1,110.00 `[11/10 intraday]`. KRE Nov-27 68P ×10, VLY 12P, FLG 10P, Fidelity WAL70P2, ZION62.5P2, KRE 66P/70P: owner/card/approval UNKNOWN. WAL65P4/OZK40P4 card windows passed (L709) | No inherited gate or approval from same symbol/heading | **PROME** scope; **Will/REGINALD/TERRY** |
| **D-77** | Off-thesis ownership/cards | 🟡 record | No contract-specific card: QQQ Nov-13 668P ×2 and Nov-10 670P ×2 (NEW), USO Nov-11 172C, USO Nov-20 170C (Will's hand), KRE67P. Closed with no card seen: QQQ Nov-09 650P, 655P, plus the 11/5 list (chunk F) | TERRY's spread card mentioned "the two short-dated QQQ put lines"; which contracts is not stated | **PROME** scope; **Will/TERRY** |
| **D-70** | Management mappings | 🟡 new lines unmapped | No mapping for the two new Fidelity QQQ lines or the three new RH lines. This byte change withholds every mapping sourced to this file until PROME re-reviews (footer) | Mapping is not a card, approval or proof of a current position | **PROME** mapping/record; **TERRY** card owner |
| **D-91** | Short-leg representation (consumer interface) | 🟡 no short row live | No signed-Qty row live, so `desk_attention.holdings()` does not error. Convention kept in the footer | The next short re-trips `desk_attention.py` until DOCKET L870 lands | **PROME** (L870); **TERRY** (`positions_from_forge.py`) |
| **D-79** | Quote/value precision | 🟡 record | 11/10: GLD 18 × $369.3522 = $6,648.34 vs displayed $6,648.33; Today 18 × −$10.1778 = −$183.20 vs −$183.21. Every other value ties to the cent; the total ties on displayed values | Rounding source UNVERIFIED (a truncated last is one fit); no total affected | **PROME** evidence |
| **D-78** | VLO extra-share scope | 🟡 scope before action | 2 sh, basis $884.73: the added shares; the $412.00 original sold 11/5. TERRY card 11/5: "Added 2 shares: Will's hand, no TERRY rule" | Neither added share extends original management scope | **Will** authorization; **PROME/TERRY** scope |
| **D-76** | Detailed fills/lots | 🟡 evidence | Activity rows carry net amounts only; no fill prices or lots for 11/5–11/10. Quantities ×1/×2 read from fee cents only | No broker realized-P/L report; all realized DERIVED | **Will** lots/fills; **PROME/TERRY** integrate |
| **D-83** | Clock / Robinhood | 🟡 standing | Receipt 11/10 15:13 ET; INTRADAY lasts, no clock on any capture; not closes. Robinhood intraday, options list only (D-98) | No RH closure booked without a row showing it | **Will** rest of the RH view; **PROME** records |
| **D-88 · D-87 · D-86 · D-85 · D-84 · D-81 · D-80** | **Carried 11/5 rows (7) — every row still OPEN; verbatim → chunk F** | 🟡 carried | None closed, re-dated or re-owned. Ticker-bearing items, for the text scan: QQQ Oct-20 715P disposition (D-88) · 14-row prior-day reference gap, 11/10 untestable (D-87) · QQQ Oct-15 715P, Oct-16 735C, HBAN Oct-16 16P (D-86) · QQQ Oct-20 719P basis split (D-85) · WAL70P2, ZION62.5P2, GLD, VLO, USO, CMG unseen 10/19 changes (D-84) · 10/14 cash +$16.58 (D-81) · GLD+3, HBAN−1, QQQ Oct-16 725P opening (D-80) | Returns to this table when its state changes | **Will** — D-88 · D-86 · D-84 · D-80; **PROME** — D-87 · D-85 · D-81 |
| **D-75 · D-66 · D-69 · D-62 · D-63 · D-64 · D-65 · D-61 · D-59 · D-45 · D-55 · D-28 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1** | **Carried discrepancies (18) — every row still OPEN; rows verbatim → rotation 10/08 chunk D1 (D-75) + D2 (the other 17)** | 🟡 carried | None closed, re-dated or re-owned; every cell unchanged in the record. Ticker-bearing items, for the text scan: STNG (D-17) · RH QQQ $715P Aug-31 (D-28) · RH KRE $25P entry (D-54) · RH WAL $77.5P Aug-21 sale (D-18) · the RH T share (D-20) · AAPL 5-sh sale pre-7/30 (D-1) · D-75 (OZK 40P basis 1¢; mirror carries $322.65, record only) | Returns to this table when its state changes | As recorded, per row: **Will** — D-66 · D-69 · D-63 · D-64 · D-61 · D-59 · D-45 · D-55 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1; **RH history before 9/01** — D-28; **PROME** — D-62 · D-65 (re-reads of desktop-local images) · D-75 (record) |

*This pass opened D-100, D-101, D-102; rebuilt D-98 for 11/5 → 11/10; narrowed D-60; closed D-99 (ANSWERED and recorded 11/5, row in chunk F). D-94, D-95, D-96, D-97, D-90, D-89 and D-76 are unchanged: this capture's Activity starts at Nov-02 and has no Orders panel. D-69 +$53.54 and D-66 (every fill clock not shown; none on the 11/10 rows) remain OPEN. D-71/D-72/D-73 historical closures unchanged.*

*Guards: each management line's text sits beside its number in the rows above (GLD rails, KRE65P time stop, USO no live rule; VLO HELD-01 RESOLVED 11/5). D-47 RH WAL Dec-18 70P: gate RETIRED (WQ-610 A). Option P/L percentages are marks, not harvest/disarm readings; no gate adjudicated this pass.*

---

## Immediate Actions (11/10 15:13 ET intraday receipt) — evidence and records only

| Item | State | Owner |
|---|---|---|
| 🟠 D-100 650P pairing; D-98 Robinhood flow 11/5 → 11/10 | record from Will's next capture if he supplies one | **Will**; **PROME** |
| 🟠 D-94 / D-96 / D-95: Activity on 10/30, below every view so far | record from Will's next capture | **Will**; **PROME** |
| 🟡 D-101 cash +$3.62; D-102 badges; D-70 mappings for the new lines | evidence / re-review | **Will**; **PROME** |
| 🟡 D-90, D-74/D-77, all other D-rows and the 25 carried duties remain | evidence / integration / scope | **Will** ledger; **PROME/TERRY** |

---

*History → `_archive/JOURNAL.md`, existing rotations and Git; immediately prior whole mirror = `git show 6db8d1d6f:FORGE/STATUS.md` (its moved parts also in `FORGE/_archive/STATUS_ROTATION_2026-11-10.md`) | `PORTFOLIO.md` FROZEN Feb snapshot, never live | Truth = Will/broker off-repo | Current evidence → `PROME/data/2026-11-10_broker-capture-TRANSCRIPTION.md` (21 Fidelity positions, Activity Nov-02 → Nov-10 as visible, Robinhood options card; posted 15:13 ET, intraday, no clock on the captures). Robinhood source → its section; prior evidence/history survives in Git.*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumers: `AGENTS/TERRY/scripts/positions_from_forge.py` (sections `^## (Fidelity|Robinhood)` + `^## Account <NAME>`; table headers by prefix; cell text — emphasis and strikethrough visible) · `PROME/tools/desk_attention.py` `holdings()` (same sections; `Qty` + `Ticker|Strike|Position` headers; expiry year from `**Updated:**`) · `PROME/tools/will_brief.py` `parse_money()` (header before the first `## `: `account total:**`, `money market):** $X (Y%)`, `**Updated:** YYYY-MM-DD`, `marks = [Fri ]YYYY-MM-DD`) · `FORGE/position_management.tsv` `source_sha256` (any byte change here withholds every mapping sourced to this file until PROME re-reviews) · `AGENTS/BRENT/scripts/pending_receipts.py` (text-level closure candidates). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself here in the same commit that starts parsing. *(Pass notes 9/27 → 10/8 → rotation 10/08 chunk G. Conventions they set, still binding: the header money line keeps the shape `will_brief.py` reads; option expiries carry the year; the `Mark <m/d>` header is prefix-bound; terminal records live in italic lines, which no parser reads as rows. 10/29: a SHORT option leg carries a signed Qty `−N` and a negative value — D-91.)*
