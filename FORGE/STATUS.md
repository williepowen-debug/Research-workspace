# FORGE — Trading Operations

🧊 Management mapping table [position_management.tsv](position_management.tsv) is FROZEN 2026-11-11 (WQ-674 A): not maintained, no re-review after a capture; [dashboard notes](DASHBOARD.md) are history. Holdings remain in this file; approval, order and fill evidence are separate.

> ✅ **2026-11-18 (Wed) — RECONCILE BY ANVIL to Will's Fidelity positions capture posted 13:21 ET in the PROME window (ONE screenshot: no Activity view, no Orders panel, no Robinhood card). INTRADAY: marks are Fidelity last prices in the November 18 session — NOT a close, NOT settles, NOT executable quotes; no clock on the capture.** Source `PROME/data/2026-11-18_broker-capture-TRANSCRIPTION.md` (PROME prome-6e; ANVIL re-read the image: every cell agrees). ANVIL independently verified **21/21** row values, Today and open G/L to the cent: positions **$13,095.33** + cash **$32,243.61** = **$45,338.94** = displayed total (no pending line shown); Σ Today −$1,978.05 and Σ open G/L −$7,199.96 tie. Against the mirror at HEAD `eb49e8a9a5` (the 11/10 reconcile `c4022901e8` as amended by PROME `a58dfd5ba3`, `0f73d6643d`; 21 Fidelity rows): **3 NEW (NVDA Nov-18 155P, QQQ Nov-19 648P, QQQ Nov-18 655P, each ×1; buys UNSEEN, D-103) / 0 QTY CHANGE / 3 GONE (QQQ Nov-13 668P ×2, QQQ Nov-10 670P ×2, USO Nov-11 172C ×1; absent from the 11/18 view, disposition UNSEEN, nothing booked, D-104) / 18 MARK ONLY.**
>
> ⚠️ **ACCOUNT SCOPE, TWO VINTAGES — ONE Fidelity Traditional IRA (•1326; last four only, the repo is public; blacked out on the 11/18 capture, carried from 11/10) for every Fidelity row, marks 11/18 intraday. The Robinhood Individual section is NOT covered by the 11/18 capture: its rows and its 11/10 intraday vintage stand as they were, not in the Fidelity total (D-98). Absence from a Fidelity view proves no closure. No Orders panel: working orders not shown (D-89).**
>
> **Updated:** 2026-11-18 · marks = 2026-11-18 intraday (Fidelity last prices, posted 13:21 ET; quote clock not displayed; not a close, not settles) — all Fidelity cells `[11/18 intraday]` · **Fidelity cash (money market):** $32,243.61 (71.12%) · **Pending activity: no line shown** (not proof of none; the 11/10 −$1,053.33 668P buy no longer shows) · **Fidelity account total:** $45,338.94 (Today −$1,978.05 / −4.18%; open G/L −$7,199.96 / −35.48% on displayed basis $20,295.29). Snapshot change vs 11/10: **+$731.79 = positions −$694.02 + cash +$372.48 + pending +$1,053.33** = open G/L change −$540.68 + other flows +$1,272.47 (DERIVED, UNVERIFIED, composition not shown: D-105); not a daily return. **Realized booked this pass: none.** Robinhood $440.86 `[RH 11/10 intraday]`, not refreshed (D-98). Bare "chunk X" below = `FORGE/_archive/STATUS_ROTATION_2026-11-10.md`; this pass moved the 11/10 header, off-thesis records, discrepancy section and actions to `FORGE/_archive/STATUS_ROTATION_2026-11-18.md` ("rotation 11/18 chunk A–D"), byte-exact, and Git (`eb49e8a9a5`); no history rebooked.

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (its own header names the current base and amendment count). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All Fidelity marks `[11/18 intraday]`; no clock on the capture; intraday lasts, not closes. Cost = basis ÷ qty (DERIVED); Mark = the displayed last (value = last × qty, verified); not exact fills.*

| Ticker | Type | Qty | Cost | Mark 11/18 intraday | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| GLD | Stock | 18 | $373.93 | $342.195 | $6,159.51 | −$571.16 / −8.49% | Today −$185.13; MARK ONLY; basis $6,730.67 (value = last × qty to the cent this capture, D-79). **`MGMT-GLD-SHARES-OCT24` (TERRY rails, MIDAS WQ-451 lines): 1-month lines "GLD close < $360.71" (TERRY recorded it crossed at the 10/30 close $355.78; card note 1: a price-path line, "not by itself a trim signal") and "GLD close > $391.08". This $342.195 is an INTRADAY last, $18.515 below the first and $48.885 below the second; the lines read the CLOSE — not graded here.** The card's choices are Will's, none recommended. 28→18 sale history → chunk B. MIDAS; largest line. |
| USO | Stock | 30 | $122.40 | $135.40 | $4,062.00 | +$389.99 / +10.62% | Today −$145.20; MARK ONLY; basis $3,672.01. **WQ-200 DECLINED 9/10: NO harvest/give-back rule live; Will manages by hand** — the +10.62% is a mark, not a gate reading. 10/23 sale history → chunk B. BRENT thesis. |
| VLO | Stock | 2 | $442.37 | $344.41 | $688.82 | −$195.91 / −22.15% | Today −$38.72; MARK ONLY; basis $884.73 = the two added shares. `GATE-TERRY-VLO-HELD-01` RESOLVED 2026-11-05 EXECUTED in PROME/GATES.tsv (the original $412.00 share sold 11/5, −$45.33 booked then; chunk B). The −22.15% is a mark and no gate reads it (D-78). `GATE-TERRY-VLO-SCALE` stays TERMINAL. |

*CLOSED stock lines AAPL ×3 and APD ×2 (11/2–11/5, booked on the 11/5 mirror) → chunk B. No live AAPL, APD or TBT line.*

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

*No live event-box rows; terminal records → rotation 10/30 chunk D, byte-exact.*

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, owned by no agent unless separately recorded. **Will manages his own expiries** (`USER.md` § No expiry nagging, 10/20 11:32 ET; supersedes the 9/30 sell-or-roll rail as an instruction): no expiry reminders or sell pushes, and a collapsed line may expire. This mirror records holdings and evidence only; dispositions are read from his captures, never inferred. The capture establishes holdings, not fills, cards or approvals; grouping is navigation, not a thesis or scope ruling. Last marks are not executable bids. Receipt-day DTE is scheduling only.

| Ticker | Strike | Expiry | Qty | Cost | Mark 11/18 intraday | Value | P&L | Note |
|--------|--------|--------|-----|------|---------------|-------|-----|------|
| NVDA | $155P | Nov-18-2026 | 1 | $3.96 | $3.40 | $340.00 | −$55.66 / −14.07% | `[11/18 intraday]`; basis $395.66; Today −$275.00. **NEW: buy date and fill UNSEEN** (no Activity view; held before the 11/18 session, INFERRED from Today ≠ total; ×1 by fee cents .66) (D-103). Broker "NE" and "E" badges (D-102). Not `IDEA-NVDA-CEOGAP-NOV12` (a Jan-15 call spread, DEAD 11/17, never entered: TERRY TRADE_BOOK). No card seen (D-77). |
| QQQ | $655P | Nov-18-2026 | 1 | $5.73 | $0.87 | $87.00 | −$485.66 / −84.81% | `[11/18 intraday]`; basis $572.66; Today −$439.00. **NEW: buy date and fill UNSEEN** (held before the 11/18 session, INFERRED) (D-103). Broker "NE" badge (D-102). No card seen (D-77). |
| QQQ | $648P | Nov-19-2026 | 1 | $7.68 | $2.80 | $280.00 | −$487.66 / −63.53% | `[11/18 intraday]`; basis $767.66; Today −$284.00. **NEW: buy date and fill UNSEEN** (held before the 11/18 session, INFERRED) (D-103). Broker "NE" badge (D-102). No card seen (D-77). |
| USO | $170C | Nov-20-2026 | 1 | $6.28 | $0.01 | $1.00 | −$626.66 / −99.85% | `[11/18 intraday]`; basis $627.66; Today −$2.00. MARK ONLY; bought open 10/27. Will 10/29 (PROME-supplied): his own hand; WQ-491 idea NOT taken — this line is not that card. Broker "NE" badge (D-102). Card/owner/approval UNKNOWN (D-77). |

*GONE from the 11/18 view, disposition UNSEEN (no Activity view; sold, expired, liquidated or exercised not shown; nothing booked, D-104):* **QQQ Nov-13-2026 668P ×2** (basis $1,053.33, the 11/10 pending buy) · **QQQ Nov-10-2026 670P ×2** (basis $303.33) · **USO Nov-11-2026 172C ×1** (basis $532.66). Their 11/10 rows → rotation 11/18 chunk B, byte-exact.

*Prior terminal records: 11/5→11/10 closes (QQQ Nov-09 650P +$522.65, Nov-09 655P −$523.66; −$1.01 booked 11/10) → rotation 11/18 chunk B; 10/30→11/5 closes (+$4,168.14) and the 10/23 exits (+$30.47) → chunk C; 10/30 closes +$4,634.95 and 10/23–10/26 outcomes −$698.90 → `git show 3064691ae:FORGE/STATUS.md`; 10/22 and earlier → rotation 10/30 chunk A, byte-exact — never add again.*

## Fidelity — Thesis Puts

*Instrument grouping is navigation, not approval: the Fidelity WAL/OZK rows below are Will-direct holdings (bought 10/7, Activity); thesis/desk ownership and management approval are NOT established by the broker view.*

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

*No live TLT line; terminal records → rotation 10/30 chunk B, byte-exact.*

### KRE — regional banks (REGINALD)

*All seven rows `[11/18 intraday]`, MARK ONLY (qty and basis as 11/10); the 68P ×10 buy stays UNSEEN, permanently unsupplied (D-90, WQ-548); grouping is not approval/ownership (D-74). Prior Sep30 roll/exits remain historical in Git/rotation 10/01 chunk D.*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $66P | Nov-20-2026 | 3 | $0.45 | $0.01 | $3.00 | −$130.99 / −97.77%; basis $133.99; Today −$39.00; MARK ONLY; broker "NE" badge (D-102); bought 10/22 @$0.44 (10/22 ledger); card/owner UNKNOWN (D-74) |
| $70P | Nov-27-2026 | 2 | $1.41 | $0.59 | $118.00 | −$163.33 / −58.06%; basis $281.33; Today −$64.00; MARK ONLY; bought 10/22 @$1.40 (10/22 ledger); card/owner UNKNOWN (D-74) |
| $68P | Nov-27-2026 | 10 | $0.73 | $0.24 | $240.00 | −$486.63 / −66.98%; basis $726.63; Today −$250.00; MARK ONLY; buy date/price UNSEEN (D-90); card/owner UNKNOWN (D-74) |
| $67P | Nov-27-2026 | 4 | $1.28 | $0.15 | $60.00 | −$450.65 / −88.26%; basis $510.65; Today −$52.00; MARK ONLY; bought 10/12 net $510.65; card/owner UNKNOWN (D-76/D-77) |
| $60P | Dec-18-2026 | 2 | $2.57 | $0.18 | $36.00 | −$477.34 / −92.99%; basis $513.34; Today −$34.00; MARK ONLY |
| $60P | Dec-18-2026 | 3 (M) | $2.93 | $0.18 | $54.00 | −$824.02 / −93.85%; basis $878.02; Today −$51.00; MARK ONLY; broker "M" badge (PROME's transcription reads it as a margin lot; earlier mirrors read a multi-lot marker — UNVERIFIED); total 5 Dec-18 60P across 2 lots |
| $65P | Dec-31-2026 | 2 | $1.69 | $0.73 | $146.00 | −$191.33 / −56.72%; basis $337.33; Today −$20.00; MARK ONLY; `MGMT-KRE65P-DEC31`: hard stop Thu 12/31 15:00 ET (5ce609f80) — a time stop, not a price gate |

### WAL (REGINALD) — Sep-18 pair EXPIRED

*Sep-18 pair EXPIRED ⇒ −$1,519.34 → rotation 10/30 chunk C, byte-exact. RH WAL $77.5P Aug-21 sale P&L UNRECORDED (D-18).*

### Other puts

*QQQ Nov-20 690P: no live line since 11/5; history → chunk D; the second contract's close is D-94, permanently unsupplied (WQ-548). Card `IDEA-QQQ-PUTWALL-OCT22` CLOSED (TERRY `42b47b6b8`).*

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18-2026 | 1 | $11.85 | $0.35 | $35.00 | −$1,149.67 / −97.05% | `[11/18 intraday]`; basis $1,184.67; Today −$5.00. MARK ONLY; no badge 11/18 (D-102); BROCK vehicle; HOLD ruled 8/13 (private-credit batch §②), vehicle-mismatch flag live. |
| OZK | $40P | Nov-20-2026 | 4 | $0.81 | $0.05 | $20.00 | −$302.65 / −93.81% | `[11/18 intraday]`; basis $322.65; Today $0.00. MARK ONLY; broker "NE" badge (D-102); bought 10/7 (Activity). WQ-428 SELL card windows passed, line rides, no order seen (DOCKET L709). Thesis ownership UNKNOWN (D-74). |
| WAL | $70P | Dec-18-2026 | 2 | $2.76 | $1.95 | $390.00 | −$161.33 / −29.27% | `[11/18 intraday]`; basis $551.33; Today +$40.00. MARK ONLY; buy fill/date unseen (D-84, permanently unsupplied); ownership/card/approval UNKNOWN (D-74). **Fidelity 2 is DISTINCT from Robinhood 1 (Nov-20); no inherited RH gate.** |
| WAL | $65P | Dec-18-2026 | 4 | $1.71 | $0.70 | $280.00 | −$402.65 / −58.99% | `[11/18 intraday]`; basis $682.65; Today −$80.00. MARK ONLY; bought 10/7 (Activity). WQ-429 SELL card windows passed, line rides, no order seen (DOCKET L709). Thesis ownership UNKNOWN (D-74). |
| ZION | $62.5P | Nov-20-2026 | 2 | $2.18 | $0.15 | $30.00 | −$405.33 / −93.11% | `[11/18 intraday]`; basis $435.33; Today −$44.00. MARK ONLY; broker "NE" badge (D-102); buy fill/date unseen (D-84, permanently unsupplied); ownership/card/approval UNKNOWN (D-74). |
| VLY | $12P | Dec-18-2026 | 1 | $0.16 | $0.10 | $10.00 | −$5.66 / −36.15% | `[11/18 intraday]`; basis $15.66; Today $0.00. MARK ONLY; the 10/22 $0.15 limit order filled (basis consistent, DERIVED); fill date UNSEEN. Card/owner UNKNOWN (D-74). |
| FLG | $10P | Mar-19-2027 | 1 | $0.71 | $0.55 | $55.00 | −$15.66 / −22.17% | `[11/18 intraday]`; basis $70.66; Today −$10.00. MARK ONLY; buy UNSEEN (D-90). Card/owner UNKNOWN (D-74). |


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

## ⚠️ Reconcile discrepancies (received 2026-11-18 13:21 ET; November 18 INTRADAY Fidelity lasts, no clock on the capture; positions view only: no Activity, no Orders, no Robinhood card)

> Broker view > Will's word > desk record. Last prices are NOT settles and these are intraday. **Will manages his own expiries (`USER.md` § No expiry nagging, 10/20): DATED rows below are records, never prompts; this list carries no sell, roll or timing recommendation, and no disposition is inferred for a line that left the view.** Ranked by how soon the evidence ages, dated contracts first. All prior duties survive unless explicitly closed. The 11/10 section, every row verbatim → `FORGE/_archive/STATUS_ROTATION_2026-11-18.md` chunk C ("rotation 11/18 chunk C" below). **WQ-548 DECLINED by Will 2026-11-10 15:42 ET (no broker history export from 8/8): the rows it names are PERMANENTLY UNSUPPLIED and never asked for again; realized results before 11/2 stay DERIVED, never broker-verified.** Permanently UNKNOWN WQ-167: 9/2 USO135C sale price, never ask.

### Will supplies / PROME re-reads — facts owed

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-103** 🆕 | Three NEW Fidelity lines: buys not in view | 🟠 basis $1,735.98, no fill seen | NVDA Nov-18-2026 155P ×1 (basis $395.66), QQQ Nov-19-2026 648P ×1 ($767.66), QQQ Nov-18-2026 655P ×1 ($572.66); none on the 11/10 view. On each, Today ≠ total G/L (−$275.00 vs −$55.66; −$284.00 vs −$487.66; −$439.00 vs −$485.66), so each was held before the 11/18 session (INFERRED from the display convention: the 11/10 same-day 668P buy showed Today = total). ×1 by display and by fee cents (.66) | INFERRED: opened between the 11/10 15:13 ET capture and the 11/17 close. Dates, fills and whether any came from a working order NOT SHOWN | **Will** Activity 11/10→11/18; **PROME** records; card scope D-77 |
| **D-104** 🆕 | Three Fidelity lines GONE from the view | 🟠 basis $1,889.32, nothing booked | QQQ Nov-13-2026 668P ×2 ($1,053.33, the 11/10 pending buy), QQQ Nov-10-2026 670P ×2 ($303.33), USO Nov-11-2026 172C ×1 ($532.66): on the 11/10 view, absent from the 11/18 view; each expiry date precedes 11/18. Sold, expired, liquidated or exercised: NOT SHOWN | None adopted. Earlier lines took each path (D-60); that is not evidence for these three | **Will** Activity 11/10→11/18; **PROME** records |
| **D-105** 🆕 | Fidelity cash bridge 11/10 → 11/18 | 🟠 +$1,272.47 unexplained | Cash $31,871.13 → $32,243.61 (+$372.48); the 11/10 pending −$1,053.33 no longer shown; no pending line 11/18 (not proof of none). DERIVED identity: +$372.48 = −$1,053.33 (pending settled, INFERRED) − $1,735.98 (D-103 bases taken as cash paid, INFERRED) + X, so **X = +$3,161.79** of other flows; X − D-104 bases $1,889.32 = **+$1,272.47**, the same figure as total change +$731.79 minus open G/L change −$540.68. D-101's +$3.62 now sits inside X. Not booked | Composition NOT SHOWN: proceeds of the D-104 lines, round trips opened and closed between captures (the D-100 form), money-market interest, fees | **Will** Activity 11/10→11/18; **PROME** records |
| **D-98** | Robinhood flow since 11/5; NOT covered 11/18 | 🟠 nothing closed | No Robinhood card in the 11/18 capture: the section and its 11/10 intraday vintage stand unchanged (8 days old). RH QQQ $675P, $669P (Nov-10) and KRE $71.5P (Nov-13) carry dates before 11/18; no card since, nothing inferred or booked. Gaps ①–④ as written (rotation 11/18 chunk C; ①–③ in chunk F) | Hypotheses as written there; nothing booked | **Will** RH history 11/5→now and cash; **PROME** records |
| **D-102** | Unexplained broker badges | 🟡 record | 11/18: "NE" on NVDA Nov-18 155P, QQQ Nov-18 655P, QQQ Nov-19 648P and all four Nov-20 rows (ZION, OZK, KRE 66P, USO 170C); not on the Nov-27 rows or later. "E" on NVDA 155P (APO showed one 11/5, not 11/10 or 11/18). "M" on KRE Dec-18 60P ×3. On 11/10 the Nov-20 rows lacked "NE" at 10 days; on 11/5 USO 172C had it at 6 | CONJECTURE: "NE" = a near-expiration flag (fits all three captures: on at 0–6 days, off at 9–10). "E" and "M" meanings not stated on any capture. RH "6 days left" unchanged, no RH card | **Will** if wanted; **PROME** records |
| **D-89** | Working-order census | 🟡 record | No Orders panel 11/10 or 11/18; last panel 11/5 (three fills, no open order) | Working orders since 11/5 NOT SHOWN, including whether a D-103 line filled from one | **Will**; **PROME** books fills only from a capture |
| **D-60** | Fidelity expiring-option handling | 🟡 NARROWED (no new path 11/18) | Paths seen, as 11/10 (rotation 11/18 chunk C): sold by Will; OPTION LIQUIDATION on expiry day; lapse as an EXPIRED row posted next day, no amount. Mechanics only: an exercised put SELLS 100 shares per contract at the strike. The three D-104 lines left the view with no row seen | INFERRED: which contracts the broker liquidates vs lets lapse; trigger and timing never stated; ITM exercise never observed | **Will** broker policy |
| **D-100** | QQQ Nov-09 650P pairing (11/5) | 🟡 booked on an inference (+$522.65) | UNCHANGED: no Activity view 11/18. Row verbatim → rotation 11/18 chunk C | INFERRED one same-day round trip; alternative as written there | **Will** row detail if wanted; **PROME** records |
| **D-101** | Fidelity cash +$3.62 (11/10) | 🟡 evidence | UNCHANGED; now inside D-105's X, not separable without the Activity rows | CONJECTURE: a money-market accrual, as written (rotation 11/18 chunk C) | **Will** Activity; **PROME** records |
| **D-74** | Fidelity bank-put ownership / new-line scope | 🟡 record | Bank/credit put cluster 41 contracts / 14 lines, basis $6,644.24, value $1,477.00 `[11/18 intraday]` ($1,110.00 on 11/10). KRE Nov-27 68P ×10, VLY 12P, FLG 10P, Fidelity WAL70P2, ZION62.5P2, KRE 66P/70P: owner/card/approval UNKNOWN. WAL65P4/OZK40P4 card windows passed (L709) | No inherited gate or approval from same symbol/heading | **PROME** scope; **Will/REGINALD/TERRY** |
| **D-77** | Off-thesis ownership/cards | 🟡 record | No contract-specific card seen: NVDA Nov-18 155P, QQQ Nov-18 655P, QQQ Nov-19 648P (NEW), USO Nov-20 170C (Will's hand), KRE67P. ANVIL read TERRY's TRADE_BOOK: the NVDA card `IDEA-NVDA-CEOGAP-NOV12` is a Jan-15 call spread, DEAD 11/17, never entered; the QQQ card `IDEA-QQQ-200D-NOV05` is a Dec-18 call spread, NOT-FIRED. Left the view with no card seen: the three D-104 lines | Neither card describes these puts; whose lines they are is not stated anywhere ANVIL read | **PROME** scope; **Will/TERRY** |
| **D-91** | Short-leg representation (consumer interface) | 🟡 no short row live | No signed-Qty row on 11/18, so `desk_attention.holdings()` does not error. Convention kept in the footer | The next short re-trips `desk_attention.py` until DOCKET L870 lands | **PROME** (L870); **TERRY** (`positions_from_forge.py`) |
| **D-79** | Quote/value precision | 🟡 record | 11/18: all 21 rows tie to the cent, GLD included (18 × $342.195 = $6,159.51; Today 18 × −$10.285 = −$185.13). The 11/10 GLD 1¢ gap (rotation 11/18 chunk C) did not recur | Rounding source UNVERIFIED (a truncated last is one fit); no total ever affected | **PROME** evidence |
| **D-78** | VLO extra-share scope | 🟡 scope before action | UNCHANGED: 2 sh, basis $884.73, the added shares; the $412.00 original sold 11/5. TERRY card 11/5: "Added 2 shares: Will's hand, no TERRY rule" | Neither added share extends original management scope | **Will** authorization; **PROME/TERRY** scope |
| **D-83** | Clock / two vintages | 🟡 standing | Receipt 11/18 13:21 ET; INTRADAY lasts, no clock on the capture; not closes. Robinhood stays at its 11/10 intraday vintage (D-98): this file carries two vintages | No RH closure booked without a row showing it | **Will** RH card if wanted; **PROME** records |
| **D-76 · D-80 · D-84 · D-86 · D-88 · D-90 · D-94 · D-95 · D-96 · D-97** | **PERMANENTLY UNSUPPLIED: WQ-548 DECLINED by Will 2026-11-10 15:42 ET**, verbatim *"Lets not worry about 8/8.  I dont really care about making sure we have everything documented since august."* | ⚪ not owed | Each gap stays recorded as it stood; never asked for again; realized results before 11/2 stay DERIVED. Rows verbatim → rotation 11/18 chunk C (D-76, D-90, D-94 to D-97) and chunk F (D-80, D-84, D-86, D-88). Ticker-bearing items, for the text scan: fills/lots (D-76) · GLD+3, HBAN−1, QQQ Oct-16 725P opening (D-80) · WAL70P2, ZION62.5P2, GLD, VLO, USO, CMG 10/19 changes (D-84) · QQQ Oct-15 715P, Oct-16 735C, HBAN Oct-16 16P (D-86) · QQQ Oct-20 715P (D-88) · 10/22→10/29 ledger incl. KRE 68P ×10, FLG, VLY buys (D-90) · second QQQ Nov-20 690P close, basis $1,339.665 unbooked (D-94) · $44.43 gap (D-95) · QQQ Nov-02 680P / Nov-05 685P opens (D-96) · share counts per sale row (D-97) | If a later capture shows one incidentally, PROME records it; nobody asks | **PROME** records only |
| **D-87 · D-85 · D-81** | **Carried 11/5 rows (3), PROME-owned — every row still OPEN; verbatim → chunk F** | 🟡 carried | None closed, re-dated or re-owned. Ticker-bearing items, for the text scan: 14-row prior-day reference gap, untestable 11/18 because the mirror base is 11/10, not the 11/17 close (D-87) · QQQ Oct-20 719P basis split (D-85) · 10/14 cash +$16.58 (D-81) | Returns to this table when its state changes | **PROME** — D-87 · D-85 · D-81 |
| **D-75 · D-66 · D-69 · D-62 · D-63 · D-64 · D-65 · D-61 · D-59 · D-45 · D-55 · D-28 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1** | **Carried discrepancies (18) — every row still OPEN; rows verbatim → rotation 10/08 chunk D1 (D-75) + D2 (the other 17)** | 🟡 carried | None closed, re-dated or re-owned; every cell unchanged in the record. Ticker-bearing items, for the text scan: STNG (D-17) · RH QQQ $715P Aug-31 (D-28) · RH KRE $25P entry (D-54) · RH WAL $77.5P Aug-21 sale (D-18) · the RH T share (D-20) · AAPL 5-sh sale pre-7/30 (D-1) · D-75 (OZK 40P basis 1¢; mirror carries $322.65, record only) | Returns to this table when its state changes | As recorded, per row: **Will** — D-66 · D-69 · D-63 · D-64 · D-61 · D-59 · D-45 · D-55 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1; **RH history before 9/01** — D-28; **PROME** — D-62 · D-65 (re-reads of desktop-local images) · D-75 (record) |

*This pass opened D-103, D-104, D-105; updated D-98 (not covered), D-102, D-89, D-60, D-74, D-77, D-79, D-83; marked D-76, D-80, D-84, D-86, D-88, D-90, D-94, D-95, D-96, D-97 PERMANENTLY UNSUPPLIED (WQ-548 DECLINED, DOCKET L1111); D-100, D-101, D-91, D-78 unchanged; D-70 (CLOSED 11/11) left the table with the 11/10 section (rotation 11/18 chunk C). No row closed on evidence: this capture has no Activity view. D-69 +$53.54 and D-66 (every fill clock not shown) remain OPEN. D-71/D-72/D-73 historical closures unchanged.*

*Guards: each management line's text sits beside its number in the rows above (GLD rails, KRE65P time stop, USO no live rule; VLO HELD-01 RESOLVED 11/5). D-47 RH WAL Dec-18 70P: gate RETIRED (WQ-610 A). Option P/L percentages are marks, not harvest/disarm readings; no gate adjudicated this pass.*

---

## Immediate Actions (11/18 13:21 ET intraday receipt) — evidence and records only

| Item | State | Owner |
|---|---|---|
| 🟠 D-103 / D-104 / D-105: one Fidelity Activity view 11/10→11/18 answers all three (the three buys, the three gone lines, the cash bridge) | PROME asks Will once; record on receipt | **Will**; **PROME** |
| 🟠 D-98 Robinhood not covered since 11/10 | record from Will's next RH card if he supplies one | **Will**; **PROME** |
| 🟡 D-102 badges; D-89 orders; D-100; D-101 | evidence | **Will**; **PROME** |
| ⚪ D-76, D-80, D-84, D-86, D-88, D-90, D-94 to D-97: permanently unsupplied (WQ-548) | not owed; record if seen incidentally | **PROME** |
| 🟡 D-74/D-77, all other D-rows and the 21 carried duties remain | evidence / integration / scope | **Will** ledger; **PROME/TERRY** |

---

*History → `_archive/JOURNAL.md`, existing rotations and Git; immediately prior whole mirror = `git show eb49e8a9a5:FORGE/STATUS.md` (its moved parts also in `FORGE/_archive/STATUS_ROTATION_2026-11-18.md`; the one before, `6db8d1d6f`, in `STATUS_ROTATION_2026-11-10.md`) | `PORTFOLIO.md` FROZEN Feb snapshot, never live | Truth = Will/broker off-repo | Current evidence → `PROME/data/2026-11-18_broker-capture-TRANSCRIPTION.md` (21 Fidelity positions, positions view only; posted 13:21 ET, intraday, no clock on the capture). Robinhood source → `PROME/data/2026-11-10_broker-capture-TRANSCRIPTION.md` and its section; prior evidence/history survives in Git.*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumers: `AGENTS/TERRY/scripts/positions_from_forge.py` (sections `^## (Fidelity|Robinhood)` + `^## Account <NAME>`; table headers by prefix; cell text — emphasis and strikethrough visible) · `PROME/tools/desk_attention.py` `holdings()` (same sections; `Qty` + `Ticker|Strike|Position` headers; expiry year from `**Updated:**`) · `PROME/tools/will_brief.py` `parse_money()` (header before the first `## `: `account total:**`, `money market):** $X (Y%)`, `**Updated:** YYYY-MM-DD`, `marks = [Fri ]YYYY-MM-DD`) · `FORGE/position_management.tsv` `source_sha256` (any byte change here withholds every mapping sourced to this file until PROME re-reviews) · `AGENTS/BRENT/scripts/pending_receipts.py` (text-level closure candidates). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself here in the same commit that starts parsing. *(Pass notes 9/27 → 10/8 → rotation 10/08 chunk G. Conventions they set, still binding: the header money line keeps the shape `will_brief.py` reads; option expiries carry the year; the `Mark <m/d>` header is prefix-bound; terminal records live in italic lines, which no parser reads as rows. 10/29: a SHORT option leg carries a signed Qty `−N` and a negative value — D-91.)*
