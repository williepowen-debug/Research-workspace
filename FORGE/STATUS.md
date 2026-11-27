# FORGE — Trading Operations

🧊 Management mapping table [position_management.tsv](position_management.tsv) is FROZEN 2026-11-11 (WQ-674 A): not maintained, no re-review after a capture; [dashboard notes](DASHBOARD.md) are history. Holdings remain in this file; approval, order and fill evidence are separate.

> ✅ **2026-11-18 (Wed) — RECONCILE BY ANVIL to Will's Fidelity positions capture posted 13:21 ET in the PROME window (ONE screenshot: no Activity view, no Orders panel, no Robinhood card). INTRADAY: marks are Fidelity last prices in the November 18 session — NOT a close, NOT settles, NOT executable quotes; no clock on the capture.** Source `PROME/data/2026-11-18_broker-capture-TRANSCRIPTION.md` (PROME prome-6e; ANVIL re-read the image: every cell agrees). ANVIL independently verified **21/21** row values, Today and open G/L to the cent: positions **$13,095.33** + cash **$32,243.61** = **$45,338.94** = displayed total (no pending line shown); Σ Today −$1,978.05 and Σ open G/L −$7,199.96 tie. Against the mirror at HEAD `eb49e8a9a5` (the 11/10 reconcile `c4022901e8` as amended by PROME `a58dfd5ba3`, `0f73d6643d`; 21 Fidelity rows): **3 NEW (NVDA Nov-18 155P, QQQ Nov-19 648P, QQQ Nov-18 655P, each ×1; buys UNSEEN, D-103) / 0 QTY CHANGE / 3 GONE (QQQ Nov-13 668P ×2, QQQ Nov-10 670P ×2, USO Nov-11 172C ×1; absent from the 11/18 view, disposition UNSEEN, nothing booked, D-104) / 18 MARK ONLY.**
>
> ⚠️ **ACCOUNT SCOPE, TWO VINTAGES — ONE Fidelity Traditional IRA (•1326; last four only, the repo is public; blacked out on the 11/18 capture, carried from 11/10) for every Fidelity row, marks 11/18 intraday, NOT refreshed 11/27 (no Fidelity view supplied). The Robinhood Individual section is refreshed to Will's 11/27 card and Recent list (posted 17:06 ET, after the 13:00 ET half-day close), not in the Fidelity total, and does not tie by $2.00 (D-107). Absence from a single view proves no closure. No Fidelity Orders panel: working orders not shown (D-89).**
>
> **Updated:** 2026-11-18 · marks = 2026-11-18 intraday (Fidelity last prices, posted 13:21 ET; quote clock not displayed; not a close, not settles) — all Fidelity cells `[11/18 intraday]` · **Fidelity cash (money market):** $32,243.61 (71.12%) · **Pending activity: no line shown** (not proof of none; the 11/10 −$1,053.33 668P buy no longer shows) · **Fidelity account total:** $45,338.94 (Today −$1,978.05 / −4.18%; open G/L −$7,199.96 / −35.48% on displayed basis $20,295.29). Snapshot change vs 11/10: **+$731.79 = positions −$694.02 + cash +$372.48 + pending +$1,053.33** = open G/L change −$540.68 + other flows +$1,272.47 (DERIVED, UNVERIFIED, composition not shown: D-105); not a daily return. **Realized booked 11/18 (Fidelity): none.** Robinhood $2,305.45 / buying power $1,760.45 `[RH 11/27 after the half-day close]`, does not tie by $2.00 (D-107); RH realized +$1,629.00 booked 11/27 = ten round trips +$2,427.00 + two Nov-27 expiries −$798.00 (Robinhood section). Bare "chunk X" below = `FORGE/_archive/STATUS_ROTATION_2026-11-10.md`; the 11/18 pass moved the 11/10 header, off-thesis records, discrepancy section and actions to `FORGE/_archive/STATUS_ROTATION_2026-11-18.md` ("rotation 11/18 chunk A–D"), byte-exact, and Git (`eb49e8a9a5`); the 11/27 pass moved the 11/10 RH section and the 11/18 discrepancy, actions and header text to `FORGE/_archive/STATUS_ROTATION_2026-11-27.md` ("rotation 11/27 chunk A–D"), byte-exact; no history rebooked.

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
| WAL | $70P | Dec-18-2026 | 2 | $2.76 | $1.95 | $390.00 | −$161.33 / −29.27% | `[11/18 intraday]`; basis $551.33; Today +$40.00. MARK ONLY; buy fill/date unseen (D-84, permanently unsupplied). Will's own trade, no desk card; thesis desk WAL for information only (WQ-702 A). **Fidelity 2 is DISTINCT from Robinhood 1 (Nov-20); no inherited RH gate.** |
| WAL | $65P | Dec-18-2026 | 4 | $1.71 | $0.70 | $280.00 | −$402.65 / −58.99% | `[11/18 intraday]`; basis $682.65; Today −$80.00. MARK ONLY; bought 10/7 (Activity). WQ-429 SELL card windows passed, line rides, no order seen (DOCKET L709). Thesis ownership UNKNOWN (D-74). |
| ZION | $62.5P | Nov-20-2026 | 2 | $2.18 | $0.15 | $30.00 | −$405.33 / −93.11% | `[11/18 intraday]`; basis $435.33; Today −$44.00. MARK ONLY; broker "NE" badge (D-102); buy fill/date unseen (D-84, permanently unsupplied). Will's own trade, no desk card; thesis desk REGINALD for information only (WQ-702 A). |
| VLY | $12P | Dec-18-2026 | 1 | $0.16 | $0.10 | $10.00 | −$5.66 / −36.15% | `[11/18 intraday]`; basis $15.66; Today $0.00. MARK ONLY; the 10/22 $0.15 limit order filled (basis consistent, DERIVED); fill date UNSEEN. Will's own trade, no desk card; thesis desk REGINALD for information only (WQ-702 A). |
| FLG | $10P | Mar-19-2027 | 1 | $0.71 | $0.55 | $55.00 | −$15.66 / −22.17% | `[11/18 intraday]`; basis $70.66; Today −$10.00. MARK ONLY; buy UNSEEN (D-90). Will's own trade, no desk card; thesis desk FLG for information only (WQ-702 A). |


## Robinhood — satellite account (Individual)

*All cells `[RH 11/27 after the half-day close, posted 17:06 ET]`, T excepted. Cost and value DERIVED from the shown $ ÷ %, checked against the Recent-list fills ("r" = Recent row, transcription § ②; no Mark column ⇒ machine class `unverified` by design).*

> ⚠️ **AFTER THE 11/27 HALF-DAY CLOSE (NYSE 13:00 ET), NOT A SETTLE; DOES NOT TIE BY $2.00 (D-107).** One card and one pasted "Recent" list (into 11/20), posted 17:06 ET; `PROME/data/2026-11-27_robinhood-capture-TRANSCRIPTION.md` (ANVIL re-verified its arithmetic; ANVIL did not have the image). **Account value $2,305.45 · buying power $1,760.45 · Past week +$992.01 / +75.53% (ties).** Lines $543.00 DERIVED + buying power = $2,303.45. No cash line, stock list or orders panel. Vs HEAD `15d399b3e3` (the 11/10 card): **3 NEW / 0 QTY CHANGE / 5 GONE / 1 MARK ONLY / T UNKNOWN.** The 11/10 section → rotation 11/27 chunk A, byte-exact.

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **CRWV $41P** | Dec-04-2026 | 1 | $2.92 ($292.00, r4) | ≈$165.00 *(DERIVED)* | 🆕 **NEW: −$127.00 / −43.49%** | Bought 11/25 (r4); year INFERRED. TERRY (`15d399b3e3`): Will's own trade, separate from WQ-745 (D-108). |
| **USO $139C** | Dec-04-2026 | 1 | $2.51 ($251.00, r2) | ≈$263.00 *(DERIVED)* | 🆕 **NEW: +$12.00 / +4.78%** | Bought 11/27 (r2); year INFERRED. TERRY (`15d399b3e3`): Will's own trade (D-108). |
| **HYG $76P** | 1/15/2027 | 2 | $0.76 ($152.00, r8) | ≈$114.00 *(DERIVED)* | 🆕 **NEW: −$38.00 / −25.00%** | Bought 11/25 (r8). Same contract as the long leg of TERRY's HYG card (WQ-615); held: 2 long puts, no short $73 leg shown. TERRY (`15d399b3e3`): card FILLED DIFFERENTLY, spread never placed (D-108). |
| **KRE $25P** | 1/15/2027 | 1 | $0.53 ($53) | ≈$1.00 *(DERIVED)* | ✅ **MARK ONLY: −$52.00 / −98.11%**, as 9/29 and 11/10 | "KRE $25 Put" as displayed. Entry never recorded — **D-54**, NOT PURSUED (Will 11/27). Will's own trade, no desk card; thesis desk REGINALD for information only (WQ-702 A). |
| T | stock | 1 | — | — | ⚠️ UNKNOWN: no stock list shown 11/27 (nor 11/5, 11/10) | Hypothesis: sold before 9/01, unconfirmed — **D-20**, NOT PURSUED (Will 11/27). |

*GONE since 11/10, disposition NOT SHOWN (on the 11/10 card, not on the 11/27 card, no Recent row): **QQQ $675P Nov-10-2026 ×1** (cost ≈$244.76 DERIVED) · **QQQ $669P Nov-10-2026 ×1** ($41.00) · **KRE $71.5P Nov-13-2026 ×2** (≈$169.99) · **WAL $70P Nov-20-2026 ×1** ($40) · **UNG $10.5C Dec-24-2026 ×1** ($55; NOTE-UNG105C-DEC24, TERRY). Sold, lapsed or other NOT SHOWN; nothing booked; NOT PURSUED (Will 11/27 17:59 ET; nobody asks him again) (D-98).*

*Round trips the list closes, both legs shown, 1 contract each, as displayed, fees not shown; realized **+$2,427.00** booked 11/27 (buy / sell):* QQQ $620P Nov-20 $279.00 r30 / $1,024.00 r27 **+$745.00** · QQQ $627C Nov-20 $277.00 r31 / $17.00 r28 **−$260.00** · QQQ $649P Nov-23 $419.00 r24 / $12.00 r21 **−$407.00** · QQQ $650P Nov-24 $572.00 r22 / $1,597.00 r19 **+$1,025.00** · QQQ $634P Nov-24 $299.00 r17 / $35.00 r14 **−$264.00** · QQQ $636C Nov-24 $188.00 r16 / $315.00 r15 **+$127.00** · NVDA $160P Nov-25 $385.00 r23 / $900.00 r18 **+$515.00** · QQQ $635P Nov-25 $501.00 r12 / $2,240.00 r10 **+$1,739.00** · QQQ $640C Nov-25 $384.00 r13 / $2.00 r7 **−$382.00** · QQQ $610P Nov-25 $411.00 r9 / expiration $0.00 r11 **−$411.00** (list order puts the buy above its expiration row; as shown).

*Sold in the list, bought before its reach, NOT booked (not on the 11/10 card, so opened after it, INFERRED):* **KRE $69P Nov-20** sold 1 at $0.35, $35.00 (r25; r26 a canceled sell) · **QQQ $635P Nov-20** sold $1,106.00 (r32; count and price cut off). Proceeds $1,141.00; the buys are NOT PURSUED (Will 11/27 17:59 ET; nobody asks him again) (D-98).

*EXPIRED WORTHLESS 11/27, basis Will's word 17:59 ET 11/27, no broker row shown:* **QQQ $627P Nov-27** 1 at $4.32 (r5) **−$432.00** · **QQQ $625P Nov-27** 1 at $3.66 (r6) **−$366.00**, both bought 11/25; realized **−$798.00** booked 11/27 (D-106 CLOSED). **Robinhood realized booked 11/27: +$1,629.00 = ten round trips +$2,427.00 + two expiries −$798.00.**

*Orders and transfers:* r1 buy QQQ $646P Nov-30 CANCELED (11/27); r26, r29 sells CANCELED (11/20); r3 withdrawal −$1,000.00 to an external bank (11/27); r20 deposit +$126.00 (11/24); settlement NOT SHOWN (D-107).

*Earlier GONE lines (QQQ $640P, USO $148C Nov-06; QQQ $651P Nov-05, WAL $70P Dec-18; nothing booked; `GATE-TERRY-ROLL70-EXIT` RETIRED 11/5, WQ-610 A) → rotation 11/27 chunk A and chunk E.*

## Account UNATTRIBUTED — receipted fills not yet attributed to an account

*No rows. Landing place for a receipt that names no account (the parser admits it — TERRY `cfd9b9115`); history → rotation 10/30 chunk E.*

---

## ⚠️ Reconcile discrepancies (received 2026-11-27 17:06 ET; Robinhood card and Recent list after the November 27 half-day close; no Fidelity view, Fidelity rows stand at 11/18 intraday)

> Broker view > Will's word > desk record. RH: after a half-day close, not settles; Fidelity: 11/18 intraday lasts. **Will manages his own expiries (`USER.md` § No expiry nagging, 10/20): DATED rows below are records, never prompts; this list carries no sell, roll or timing recommendation, and no disposition is inferred for a line that left a view.** Ranked by how soon the evidence ages, dated contracts first. All prior duties survive unless explicitly closed. The 11/18 section, every row verbatim → rotation 11/27 chunk B. **WQ-548 DECLINED by Will 2026-11-10 15:42 ET (no broker history export from 8/8): the rows it names are PERMANENTLY UNSUPPLIED and never asked for again; realized results before 11/2 stay DERIVED.** Permanently UNKNOWN WQ-167: 9/2 USO135C sale price, never ask.

### Will supplies / PROME re-reads — facts owed

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-98** | Robinhood flow since 11/5 | ⚪ older moves NOT PURSUED (Will 11/27) | **Closed:** the 11/10 vintage, replaced by the 11/27 card; realized +$1,629.00 booked (ten round trips +$2,427.00, two Nov-27 expiries −$798.00, D-106). **NOT PURSUED, Will in PROME's chat 17:59 ET 11/27, verbatim *"I do not think necessary to go in depth on older moves not seen.  Better to be forward looking(in my opinion)"*; nobody asks him again; nothing booked, no value invented:** ⓐ the five GONE lines' dispositions; ⓑ activity 11/10 → 11/20, incl. the buys of r25 KRE $69P and r32 QQQ $635P (r32 count, price cut off); ⓒ 11/5 → 11/10 gaps ①–④ (rotation 11/18 chunk C; ①–③ chunk F). **DERIVED identity 11/10 → 11/27:** value +$1,864.59 = list and card effects +$2,617.00 (realized $2,427.00 + r25/r32 proceeds $1,141.00 − r5/r6 costs $798.00 − open-line change $153.00) − the five GONE lines' 11/10 values $415.75 + Z, so **Z = −$336.66** | Z = their proceeds − the two unseen buys + unseen flows before 11/20 + whichever listed transfer the value reflects; NOT SHOWN and not pursued. Nothing booked | Nobody asks; **PROME** records only if seen incidentally |
| **D-103 · D-104 · D-105** | Fidelity 11/18 asks, UNCHANGED 11/27 (no Fidelity view) | 🟠 nothing closed | D-103: buys unseen of NVDA Nov-18 155P, QQQ Nov-19 648P, QQQ Nov-18 655P (basis $1,735.98). D-104: QQQ Nov-13 668P ×2, Nov-10 670P ×2, USO Nov-11 172C left the 11/18 view ($1,889.32), disposition unseen. D-105: cash bridge +$1,272.47 unexplained. Verbatim → rotation 11/27 chunk B. Fidelity rows carry 11/18 marks; state since NOT SHOWN | As written there | **Will** Fidelity Activity 11/10 → now; **PROME** records |
| **D-107** 🆕 | RH card does not tie; transfers; fees | ⚪ $2.00 recorded, unexplained, NOT PURSUED (Will 11/27) | $543.00 + $1,760.45 = $2,303.45 vs $2,305.45 (implied cash $1,762.45). Values = ledger cost + shown P/L. Past week ties to $1,313.44. r3 −$1,000.00 and r20 +$126.00: settlement, and whether "Past week" nets them, NOT SHOWN. No fee on any row: +$1,629.00 is gross | CONJECTURE: in-week trading as listed (realized 11/23 → 11/25 +$1,942.00, open lines −$153.00, r5/r6 expired −$798.00) = +$991.00, $1.01 short of +$992.01 with NO transfer in it; fits transfers excluded or not yet in the value; assumes the week opened with only KRE $25P (not shown). The $2.00: buying power ≠ cash, or an unshown item | Nobody asks; **PROME** records |
| **D-108** 🆕 | RH NEW lines vs desk cards | 🟡 record | HYG $76P 1/15/2027 ×2 at $0.76 (r8, 11/25) is the same contract as the long leg of TERRY's HYG card (Jan-15-2027 76/73 put spread ×5, `GATE-TERRY-HYG-FOLLOW-01`, WQ-615); held: 2 long puts on Robinhood, no short $73 leg shown. CRWV $41P Dec-04 ×1 at $2.92 (r4, 11/25): WQ-745 (TERRY's CoreWeave card, RULED A 11/25, NOT-FIRED) as written names a Feb-19-2027 40/30 put spread ×1 (ANVIL read the row). USO $139C Dec-04 ×1 (r2): no card shown | None by ANVIL. **TERRY's word, packet `15d399b3e3` (17:08 ET), relaying Will 17:01 ET in TERRY's window, verbatim *"I did not make a spread I just added a put"*:** HYG card `IDEA-HYG-FOLLOW-NOV05` FILLED DIFFERENTLY, the 76/73 ×5 spread never placed; CRWV = WILL-OWN-2026-11-25-CRWV, separate from WQ-745 (stays APPROVED NOT-FIRED); USO = WILL-OWN-2026-11-27-USO. TERRY's card files carrying this are uncommitted at ANVIL's read; recording the HYG gate is PROME's (TERRY's ask) | **TERRY** (cards), **Will**; **PROME** records the gate |
| **D-83** | Clock / two vintages | 🟡 standing | Fidelity 11/18 intraday (13:21 ET, lasts). Robinhood 11/27 after the 13:00 ET half-day close (17:06 ET, not a settle). `**Updated:**` stays 2026-11-18: it dates the Fidelity total `will_brief.py` and `desk_attention.py` read | No closure booked without a row showing it | **Will** Fidelity capture if wanted; **PROME** records |
| **D-54** | RH KRE $25P entry | ⚪ NOT PURSUED (Will 11/27) | Card 11/27: −$52.00 / −98.11%, cost $53.00 DERIVED, value ≈$1.00, as 9/29 and 11/10. No KRE $25P row in the list (into 11/20). Entry date and fill never shown; before 7/16 (DOCKET L1200) | Only a history export older than the list answers it. NOT PURSUED (Will 11/27 17:59 ET; nobody asks him again); nothing booked, no value invented | **PROME** records only if seen incidentally |
| **D-20** | RH T share | ⚪ NOT PURSUED (Will 11/27) | No stock list on the 11/27 card (nor 11/5, 11/10); no T row in the list | Hypothesis: sold before 9/01, unconfirmed. NOT PURSUED (Will 11/27 17:59 ET; nobody asks him again); nothing booked | **PROME** records only if seen incidentally |
| **D-102 · D-89 · D-60 · D-100 · D-101 · D-74 · D-77 · D-91 · D-79 · D-78** | **Carried 11/18 Fidelity rows (10), UNCHANGED 11/27; verbatim → rotation 11/27 chunk B** | 🟡 carried | No Fidelity view 11/27. For the text scan: badges, KRE Dec-18 60P (D-102) · orders (D-89) · expiry paths (D-60) · QQQ Nov-09 650P (D-100) · cash +$3.62 (D-101) · KRE 68P ×10, 66P, 70P (D-74) · NVDA 155P, QQQ 655P, 648P, USO 170C, KRE67P (D-77) · short legs, L870 (D-91) · GLD (D-79) · VLO (D-78). RH: no badge on the 11/27 transcription; three CANCELED rows, no orders panel | Returns to this table when its state changes | As recorded per row in chunk B: **Will** — D-102 · D-89 · D-60 · D-100 · D-101 · D-78 (evidence, authorization); **PROME** — D-74 · D-77 (scope, with Will/TERRY/REGINALD), D-79, D-91 (L870, with **TERRY**) |
| **D-106** ✅ CLOSED 11/27 | RH QQQ $627P and $625P Nov-27, bought 11/25 | ✅ closed on Will's word | r5 $432.00, r6 $366.00; no sell or expiration row in the list at 17:06 ET, not on the panel. **Will in PROME's chat 17:59 ET 11/27, verbatim *"The two QQQ puts dated today expired worthless."*:** booked EXPIRED WORTHLESS, realized −$798.00; basis Will's word, no broker row shown | None | **PROME** records |
| **D-87 · D-85 · D-81** | **Carried 11/5 rows (3), PROME-owned — still OPEN; verbatim → chunk F** | 🟡 carried | 14-row prior-day reference gap (D-87) · QQQ Oct-20 719P basis split (D-85) · 10/14 cash +$16.58 (D-81) | Returns when its state changes | **PROME** |
| **D-75 · D-66 · D-69 · D-62 · D-63 · D-64 · D-65 · D-61 · D-59 · D-45 · D-55 · D-28 · D-18 · D-37 · D-17 · D-1** | **Carried discrepancies (16) — still OPEN; verbatim → rotation 10/08 chunk D1 (D-75) + D2** | 🟡 carried | STNG (D-17) · RH QQQ $715P Aug-31 (D-28) · RH WAL $77.5P Aug-21 sale (D-18) · AAPL 5-sh sale pre-7/30 (D-1) · OZK 40P basis 1¢ (D-75). D-54 and D-20 now have their own rows above | Returns when its state changes | **Will** — D-66 · D-69 · D-63 · D-64 · D-61 · D-59 · D-45 · D-55 · D-18 · D-37 · D-17 · D-1; **RH history before 9/01** — D-28; **PROME** — D-62 · D-65 · D-75 |
| **D-76 · D-80 · D-84 · D-86 · D-88 · D-90 · D-94 · D-95 · D-96 · D-97** | **PERMANENTLY UNSUPPLIED (WQ-548 DECLINED, Will 2026-11-10 15:42 ET)** | ⚪ not owed | Never asked for again; rows and ticker list → rotation 11/27 chunk B and the chunks named there | — | **PROME** records only if seen incidentally |

*This pass (Robinhood only): opened D-106 to D-108; narrowed D-98; updated D-83, D-54, D-20 (own rows); carried D-103 to D-105 and ten Fidelity rows unchanged; carried-18 now 16. Nothing closed on evidence. Round 2 (Will 17:59 ET): D-106 CLOSED on his word (−$798.00 booked); the Robinhood older-move gaps (D-98 ⓐ–ⓒ, D-54, D-20) NOT PURSUED; D-107 kept as a recorded difference, not pursued. No Fidelity row changed.*

*Guards: GLD rails, KRE65P time stop, USO no-rule note sit beside their Fidelity rows. `GATE-TERRY-HYG-FOLLOW-01` is an entry gate (PROME/GATES.tsv); the RH HYG −25.00% is a mark, not a gate reading. No gate adjudicated.*

---

## Immediate Actions (11/27 17:06 ET Robinhood receipt) — evidence and records only

| Item | State | Owner |
|---|---|---|
| 🟠 D-103 / D-104 / D-105: one Fidelity Activity view 11/10 → now answers all three | PROME asks Will once; record on receipt | **Will**; **PROME** |
| 🟡 D-108 HYG card FILLED DIFFERENTLY (TERRY `15d399b3e3`) | PROME records it on `GATE-TERRY-HYG-FOLLOW-01` | **PROME**; **TERRY** |
| ⚪ D-98 Robinhood older moves, D-54, D-20, D-107: NOT PURSUED (Will 11/27) | not owed; record if seen incidentally | **PROME** |
| ⚪ D-76, D-80, D-84, D-86, D-88, D-90, D-94 to D-97: permanently unsupplied (WQ-548) | not owed; record if seen incidentally | **PROME** |
| 🟡 all other D-rows and the 19 carried duties remain | evidence / integration / scope | **Will** ledger; **PROME/TERRY** |

---

*History → `_archive/JOURNAL.md`, existing rotations and Git; immediately prior whole mirror = `git show 15d399b3e3:FORGE/STATUS.md` (its moved parts also in `FORGE/_archive/STATUS_ROTATION_2026-11-27.md`; the two before, `eb49e8a9a5` and `6db8d1d6f`, in the 11-18 and 11-10 rotations) | `PORTFOLIO.md` FROZEN Feb snapshot, never live | Truth = Will/broker off-repo | Current evidence → `PROME/data/2026-11-18_broker-capture-TRANSCRIPTION.md` (21 Fidelity positions, positions view only; posted 13:21 ET, intraday, no clock on the capture). Robinhood source → `PROME/data/2026-11-27_robinhood-capture-TRANSCRIPTION.md` (card + Recent list, posted 17:06 ET 11/27, after the half-day close); prior evidence/history survives in Git.*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumers: `AGENTS/TERRY/scripts/positions_from_forge.py` (sections `^## (Fidelity|Robinhood)` + `^## Account <NAME>`; table headers by prefix; cell text — emphasis and strikethrough visible) · `PROME/tools/desk_attention.py` `holdings()` (same sections; `Qty` + `Ticker|Strike|Position` headers; expiry year from `**Updated:**`) · `PROME/tools/will_brief.py` `parse_money()` (header before the first `## `: `account total:**`, `money market):** $X (Y%)`, `**Updated:** YYYY-MM-DD`, `marks = [Fri ]YYYY-MM-DD`) · `FORGE/position_management.tsv` `source_sha256` (any byte change here withholds every mapping sourced to this file until PROME re-reviews) · `AGENTS/BRENT/scripts/pending_receipts.py` (text-level closure candidates). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself here in the same commit that starts parsing. *(Pass notes 9/27 → 10/8 → rotation 10/08 chunk G. Conventions they set, still binding: the header money line keeps the shape `will_brief.py` reads; option expiries carry the year; the `Mark <m/d>` header is prefix-bound; terminal records live in italic lines, which no parser reads as rows. 10/29: a SHORT option leg carries a signed Qty `−N` and a negative value — D-91.)*
