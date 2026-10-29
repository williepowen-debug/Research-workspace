# FORGE — Trading Operations

Dashboard management mapping → [position_management.tsv](position_management.tsv); maintenance contract → [dashboard notes](DASHBOARD.md). Holdings remain in this file; approval, order and fill evidence are separate. A changed evidence source invalidates its management mapping until reviewed.

> ✅ **2026-10-29 (Thu) — RECONCILE BY ANVIL to Will's Fidelity positions capture, posted 18:25 ET in the PROME window (a post-close view of the October29 session; quote clock not displayed). Marks are Fidelity's last prices at the close, NOT exchange settles and NOT executable quotes.** Source `PROME/data/2026-10-29_broker-capture-TRANSCRIPTION.md` (PROME transcription of one positions image). **No Activity & Orders ledger came with this capture: every sale, buy, expiry outcome and cash movement between 10/22 and 10/29 is UNSEEN (D-90); nothing realized is booked.** ANVIL independently verified **28/28** row values and open G/L to the cent: positions **$24,810.30** + cash **$13,386.72** + pending **+$962.00** = **$39,159.02** = displayed total; Σ Today +$527.49 and Σ open G/L −$2,726.32 tie to the header. Against last mirror `ec5a7058b` (10/22 11:01 ET intraday, 25 rows): **10 NEW + 1 NEW SHORT / 4 QTY CHANGE / 7 GONE (outcomes unseen) / 13 MARK ONLY**.
>
> ⚠️ **ACCOUNT SCOPE — ONE Fidelity Traditional IRA (•1326; last four only, the repo is public). Robinhood Individual NOT provided: its rows below are not in this export's account, unverified today; Will's word 10/29 (PROME-supplied via TERRY's note) is that they are "all dead" — written off by him, not evidenced by a capture. Absence proves no closure. No Activity, no Orders page: working orders UNKNOWN.**
>
> **Updated:** 2026-10-29 · marks = 2026-10-29 post-close (Fidelity last prices at the October29 session close, posted 18:25 ET; quote clock not displayed; not settles) — all Fidelity cells `[10/29 close rcv 18:25 ET]` · **Fidelity cash (money market):** $13,386.72 (34.19%) + **Pending activity +$962.00** (Fidelity labels it "Margin credit balance $962.00" — Will 10/29 11:58 ET, PROME-supplied via TERRY's note; already in the total, never add again) · **Fidelity account total:** $39,159.02 (Today +$527.49 / +1.37%; open G/L −$2,726.32 / −8.79% on displayed basis $31,021.88, which counts the short leg's $1,742.63 as basis). Snapshot change vs 10/22: **−$717.04 = positions +$2,411.10 + cash −$2,421.25 + pending −$706.89**, not a daily/realized return. The same day's ~11:2x ET intraday capture (TERRY, bucket sums only) showed identical cash and pending ⇒ no cash movement between 11:2x and the close. **No realized P/L booked this pass (D-90).** Robinhood $295.15 / BP $8.94 `[9/29 13:4x intraday]`, 30 days old, written off by Will's word. Prior tables/history remain in Git (`ec5a7058b`, `100c63edc`, `ba1a41e09`, `6fbf39cd0`) and existing rotations; no history rebooked.

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (its own header names the current base and amendment count). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All Fidelity marks `[10/29 close rcv 18:25 ET]`; quote clock not displayed. Cost = basis ÷ qty (DERIVED); Mark = the displayed last (value = last × qty, verified); not exact fills.*

| Ticker | Type | Qty | Cost | Mark 10/29 close rcv 18:25 ET | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | 3 | $23.64 | $348.91 | $1,046.73 | +$975.80 / +1375.72% | Today +$15.24; broker "E" badge. **QTY CHANGE 4→3:** basis $94.58 → $70.93 (−$23.65 = one share at average cost); sale date/price/proceeds UNSEEN (D-90), nothing realized booked. Prior lot gaps D-76/D-1 historical. |
| GLD | Stock | 28 | $374.63 | $368.57 | $10,319.96 | −$169.57 / -1.62% | Today −$138.32; **QTY CHANGE 25→28:** basis $9,390.78 → $10,489.53 (+$1,098.75 ⇒ $366.25/sh on the added 3, DERIVED, assumes plain adds); buy dates/prices UNSEEN (D-90). Will adopted 28 on TERRY's card 10/29 (PROME-supplied). **`MGMT-GLD-SHARES-OCT24` (TERRY rails, MIDAS WQ-451 lines): 1-month downside line "GLD close < $360.71" — this $368.57 is a Fidelity last, $7.86 / 2.13% above it, not a close and not a grade;** the card's choices are Will's, none recommended. MIDAS; largest line. |
| USO | Stock | 30 | $122.40 | $168.19 | $5,045.70 | +$1,373.69 / +37.40% | Today +$48.60; **QTY CHANGE 35→30:** basis $4,266.43 → $3,672.01 (−$594.42, vs 5 × average $609.49 — lot-specific relief or unseen offsetting trades, D-90); sale date/price/proceeds UNSEEN, nothing realized booked. **WQ-200 DECLINED 9/10: NO harvest/give-back rule live; Will manages by hand** — the +37.40% is a mark, not a gate reading. BRENT thesis. |
| VLO | Stock | 3 | $432.24 | $384.57 | $1,153.71 | −$143.02 / -11.03% | Today −$11.73; MARK ONLY; exact basis $1,296.73. **Additional-share authorization/management scope UNKNOWN (D-78).** Held-share exit letter `GATE-TERRY-VLO-HELD-01` (PROME/GATES.tsv): leg A = "the matched ULSD crack SETTLEMENT (HOZ26×42 − CLZ26 for 2026-10-15 through 2026-11-19) closes BELOW $90.16" — a **crack-basis gate, not a stock price gate**; this −11.03% is a mark and reads nothing on it. Scale instruction WQ-213 remains STAND DOWN/TERMINAL under `GATE-TERRY-VLO-SCALE`. Fill-clock gaps D-55/D-76 historical. |
| APD | Stock | 2 | $294.79 | $311.75 | $623.50 | +$33.93 / +5.75% | Today +$9.10; MARK ONLY; exact basis $589.57. Historical 10/1 D badge/$1.81 reference adjustment unverified; thesis tag unassigned since 7/30. |
| TBT | Stock | 10 | $36.56 | $38.57 | $385.70 | +$20.09 / +5.49% | Today −$4.40; **QTY CHANGE 5→10:** basis $172.01 → $365.61 (+$193.60 ⇒ $38.72/sh on the added 5, DERIVED, assumes plain adds); buy dates UNSEEN (D-90). Will 10/29: "I did rebuy a couple" — WQ-357 RESOLVED, no sale owed (PROME-supplied, TERRY packet `561117033`); `MGMT-DURSHORT-EXIT-WQ291` CLOSED at TERRY. BOND/TERRY duration-short leg. |

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

*No live event-box rows — the VIX $20C/$25C spread (CLOSED 2026-07-30, realized −$111.60) and the five Aug-21-2026 EXPIRED rows (realized −$2,816.72 total) are terminal → rotation records.*

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, owned by no agent unless separately recorded. **Will manages his own expiries** (`USER.md` § No expiry nagging, 10/20 11:32 ET; supersedes the 9/30 sell-or-roll rail as an instruction): no expiry reminders or sell pushes, and a collapsed line may expire. This mirror records holdings and evidence only; dispositions are read from his captures, never inferred. The capture establishes holdings, not fills, cards or approvals; grouping is navigation, not a thesis or scope ruling. Last marks are not executable bids; working orders UNKNOWN. Receipt-day DTE is scheduling only.

| Ticker | Strike | Expiry | Qty | Cost | Mark 10/29 close rcv 18:25 ET | Value | P&L | Note |
|--------|--------|--------|-----|------|---------------|-------|-----|------|
| QQQ | $711P | Oct-30-2026 | 2 | $3.44 | $6.75 | $1,350.00 | +$662.67 / +96.41% | `[10/29 close rcv 18:25 ET]`; basis $687.33; Today +$1,026.00. NEW; buy date/price UNSEEN (D-90). 1 calendar DTE from receipt. +96.41% is a mark; no harvest/disarm line is registered for this contract in this file. Card/owner/approval UNKNOWN (D-77). |
| QQQ | $710P | Oct-30-2026 | 1 | $6.62 | $6.13 | $613.00 | −$48.66 / -7.36% | `[10/29 close rcv 18:25 ET]`; basis $661.66; Today +$468.00. NEW; buy UNSEEN (D-90). Distinct from the GONE Oct-26 710P; no roll linkage inferred. 1 calendar DTE. Card/owner/approval UNKNOWN (D-77). |
| USO | $163C | Oct-30-2026 | 1 | $3.59 | $5.45 | $545.00 | +$186.34 / +51.95% | `[10/29 close rcv 18:25 ET]`; basis $358.66; Today +$45.00. MARK ONLY; bought open 10/21 (10/22 ledger). 1 calendar DTE. Card/owner/approval UNKNOWN (D-77). |
| QQQ | $715P | Nov-02-2026 | 1 | $4.85 | $10.47 | $1,047.00 | +$562.34 / +116.02% | `[10/29 close rcv 18:25 ET]`; basis $484.66; Today +$710.00. NEW; buy UNSEEN (D-90). 4 calendar DTE. **+116.02% is a mark; no harvest/disarm line is registered for this contract in this file — not a gate reading.** Card/owner/approval UNKNOWN (D-77). |
| GLD | $375C | Nov-02-2026 | 2 | $3.26 | $0.51 | $102.00 | −$549.33 / -84.34% | `[10/29 close rcv 18:25 ET]`; basis $651.33; Today −$386.00. NEW; buy UNSEEN (D-90). 4 calendar DTE. Not a GLD-share rail; card/owner/approval UNKNOWN (D-77). |
| USO | $170C | Nov-20-2026 | 1 | $6.28 | $7.65 | $765.00 | +$137.34 / +21.88% | `[10/29 close rcv 18:25 ET]`; basis $627.66; Today +$15.00. NEW; buy UNSEEN (D-90). Will 10/29 (PROME-supplied): added USO exposure by his own hand; WQ-491 idea NOT taken — this line is not that card. 22 calendar DTE. Card/owner/approval UNKNOWN (D-77). |

*GONE since the 10/22 mirror — absent from this capture; outcome, proceeds and realized UNSEEN, nothing booked, no worthless expiry inferred (D-90):* expiry date passed — **QQQ Oct-22 717C ×1** (basis $154.66) · **CRWV Oct-23 56P ×1** ($179.66) · **USO Oct-23 163C ×1** ($289.66) · **QQQ Oct-26 710P ×1** ($457.66; marked +$325.34 on 10/22) · **USO Oct-28 165C ×1** ($335.66). Gone BEFORE expiry (sold or otherwise closed) — **USO Oct-30 165C ×2** ($586.32) · **CMG Oct-30 28P ×1** ($54.66). Removed basis $2,058.28.

*Prior terminal records remain historical in Git: the 10/22 closes and between-capture round trips (DERIVED realized +$1,537.62, D-85) → `git show ec5a7058b:FORGE/STATUS.md` — never add again; the 10/20 QQQ Oct-20 720P close (+$474.66) → `100c63edc`; the 10/19 call round trips (+$27.69) → `ba1a41e09`; QQQ Oct-15 740P ×3 and USO Oct-14 150C ×2 SOLD CLOSE 10/14 (+$1,882.94 / +$385.35) → rotation 10/22 chunk A. QQQ Oct15 715P, Oct16 735C, HBAN Oct16 16P absent after expiry, outcome UNKNOWN (D-86). No prior result rebooked.*

## Fidelity — Thesis Puts

*Instrument grouping is navigation, not approval: the Fidelity WAL/OZK rows below are Will-direct holdings (bought 10/7, Activity); thesis/desk ownership and management approval are NOT established by the broker view.*

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

*No live TLT line. Terminal records (TLT $77P Sep-30 ×15 sold close 9/30 ⇒ −$154.64; TLT Oct-16 $82P sold 9/28 and 10/12 ⇒ +$191.66 and +$232.67; WQ-357 and `MGMT-TLT82P-OCT16` historical) → rotation 10/22 chunk B, byte-exact.*

### KRE — regional banks (REGINALD)

*All seven rows `[10/29 close rcv 18:25 ET]`; six MARK ONLY, one NEW (buy UNSEEN, D-90); grouping is not approval/ownership (D-74). Prior Sep30 roll/exits remain historical in Git/rotation 10/01 chunk D.*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $66P | Nov-20-2026 | 3 | $0.45 | $0.12 | $36.00 | −$97.99 / -73.14%; basis $133.99; Today −$72.00; MARK ONLY `[10/29 close rcv 18:25 ET]`; bought 10/22 @$0.44 (10/22 ledger); card/owner UNKNOWN (D-74) |
| $70P | Nov-27-2026 | 2 | $1.41 | $0.49 | $98.00 | −$183.33 / -65.17%; basis $281.33; Today −$102.00; MARK ONLY `[10/29 close rcv 18:25 ET]`; bought 10/22 @$1.40 (10/22 ledger); card/owner UNKNOWN (D-74) |
| $68P | Nov-27-2026 | 10 | $0.73 | $0.18 | $180.00 | −$546.63 / -75.23%; basis $726.63; Today −$450.00 (so held before 10/29); NEW `[10/29 close rcv 18:25 ET]`; buy date/price UNSEEN (D-90); card/owner UNKNOWN (D-74) |
| $67P | Nov-27-2026 | 4 | $1.28 | $0.05 | $20.00 | −$490.65 / -96.09%; basis $510.65; Today −$196.00; MARK ONLY `[10/29 close rcv 18:25 ET]`; bought 10/12 net $510.65; card/owner UNKNOWN (D-76/D-77) |
| $60P | Dec-18-2026 | 2 | $2.57 | $0.05 | $10.00 | −$503.34 / -98.06%; basis $513.34; Today −$42.00; MARK ONLY `[10/29 close rcv 18:25 ET]` |
| $60P | Dec-18-2026 | 3 (M) | $2.93 | $0.05 | $15.00 | −$863.02 / -98.30%; basis $878.02; Today −$63.00; MARK ONLY `[10/29 close rcv 18:25 ET]`; broker "M" badge (PROME's transcription legend reads it as margin-flagged; earlier mirrors read a multi-lot marker — UNVERIFIED); total 5 Dec-18 60P across 2 lots |
| $65P | Dec-31-2026 | 2 | $1.69 | $0.85 | $170.00 | −$167.33 / -49.61%; basis $337.33; Today $0.00; MARK ONLY `[10/29 close rcv 18:25 ET]`; `MGMT-KRE65P-DEC31`: hard stop Thu 12/31 15:00 ET (5ce609f80) — a time stop, not a price gate |

### WAL (REGINALD) — Sep-18 pair EXPIRED

*$70P + $67.5P Sep-18 ×1 each EXPIRED as of 9/18, broker-confirmed ⇒ realized −$1,519.34 → rotation 10/22 chunk C, byte-exact. Duration roll = the Robinhood WAL Dec-18 $70P ×1 below; RH WAL $77.5P Aug-21 sale P&L UNRECORDED (D-18).*

### Other puts

*QQQ Nov-20 690P ×2 / 670P ×(−2) = one 690/670 put spread ×2, TERRY card `IDEA-QQQ-PUTWALL-OCT22` (`AGENTS/TERRY/setups/QQQ_nov20-690-670P_gamma-negative-putwall_2026-10-22.md`), bought 10/23 by Will's hand per that card and his 10/29 word (WQ-490 CLOSED as moot; PROME-supplied). The 670P row is a SHORT: signed Qty −2, value shown negative by the broker, basis = the opening credit. Net basis $2,679.33 − $1,742.63 = **$936.70** (= the card's net debit and max loss); net value $1,922.00 − $1,168.00 = **$754.00** (−$182.70 / −19.50%), i.e. $3.77 per spread from two Fidelity lasts. **Card § 6 lines, stated so the number is not read as a gate: harvest "sell the spread when it marks ≥ $10.00 … on the broker bid" — $3.77 is a last-price difference, not a bid; kill "SPX cash close ≥ 7,750 on two consecutive sessions" — not read here; time stop "sell by the close Fri 2026-11-13". No line adjudicated this pass.***

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| QQQ | $690P | Nov-20-2026 | 2 | $13.40 | $9.61 | $1,922.00 | −$757.33 / -28.27% | `[10/29 close rcv 18:25 ET]`; basis $2,679.33; Today +$776.00. NEW; long leg of the 690/670 spread ×2 (above); broker "M" badge. Fill prices UNSEEN (D-90). |
| QQQ | $670P | Nov-20-2026 | −2 | $8.71 | $5.84 | −$1,168.00 | +$574.63 / +32.97% | `[10/29 close rcv 18:25 ET]`; SHORT ×2, opening credit $1,742.63; Today −$500.00. NEW; short leg of the 690/670 spread ×2; broker "M" badge. Signed-qty convention new 10/29 (D-91). |
| APO | $95P | Dec-18-2026 | 1 | $11.85 | $0.60 | $60.00 | −$1,124.67 / -94.94% | `[10/29 close rcv 18:25 ET]`; basis $1,184.67; Today −$85.00. MARK ONLY; broker "E" badge; BROCK vehicle; HOLD ruled 8/13 (private-credit batch §②), vehicle-mismatch flag live. |
| OZK | $40P | Nov-20-2026 | 4 | $0.81 | $0.10 | $40.00 | −$282.65 / -87.61% | `[10/29 close rcv 18:25 ET]`; basis $322.65; Today $0.00. MARK ONLY; bought 10/7 (Activity). PROME-supplied WQ-428 SELL approved 10/14; **4 still held at the 10/29 close** (D-82). Thesis ownership UNKNOWN (D-74). |
| WAL | $70P | Dec-18-2026 | 2 | $2.76 | $0.90 | $180.00 | −$371.33 / -67.36% | `[10/29 close rcv 18:25 ET]`; basis $551.33; Today −$190.00. MARK ONLY; buy fill/date unseen (D-84); ownership/card/approval UNKNOWN (D-74). **Fidelity 2 is DISTINCT from Robinhood 1; no inherited RH gate.** |
| WAL | $65P | Dec-18-2026 | 4 | $1.71 | $0.25 | $100.00 | −$582.65 / -85.36% | `[10/29 close rcv 18:25 ET]`; basis $682.65; Today −$200.00. MARK ONLY; bought 10/7 (Activity). PROME-supplied WQ-429 SELL approved 10/14; **4 still held at the 10/29 close** (D-82). Thesis ownership UNKNOWN (D-74). |
| ZION | $62.5P | Nov-20-2026 | 2 | $2.18 | $0.45 | $90.00 | −$345.33 / -79.33% | `[10/29 close rcv 18:25 ET]`; basis $435.33; Today −$110.00. MARK ONLY; buy fill/date unseen (D-84); ownership/card/approval UNKNOWN (D-74). |
| VLY | $12P | Dec-18-2026 | 1 | $0.16 | $0.10 | $10.00 | −$5.66 / -36.15% | `[10/29 close rcv 18:25 ET]`; basis $15.66; Today $0.00. NEW — the 10/22 open order (buy-to-open limit $0.15, D-89) is now a position; basis = $0.15 × 100 + $0.66 is CONSISTENT with a fill at the limit (DERIVED); fill date/price UNSEEN. Card/owner UNKNOWN (D-74). |
| FLG | $10P | Mar-19-2027 | 1 | $0.71 | $0.50 | $50.00 | −$20.66 / -29.24% | `[10/29 close rcv 18:25 ET]`; basis $70.66; Today −$35.00. NEW; buy UNSEEN (D-90). Card/owner UNKNOWN (D-74). |


## Robinhood — satellite account (Individual)

*All holdings/figures below retained from the 9/29 source; carried DTE annotations are historical, not a current freshness assertion.*

> ⚠️ **NOT IN THIS EXPORT'S ACCOUNT — UNVERIFIED TODAY (not captured 10/29, 10/22, 10/20, 10/19, 10/14, 10/13, 10/11, 10/7, 10/1 or 9/30 — 30 days since the 9/29 card). Will's word 10/29 (TERRY window, PROME-supplied via `AGENTS/TERRY/research/2026-10-29_ira-snapshot/NOTE.md`): Robinhood positions "all dead" — written off by him; no capture evidences closure or values, so the rows stay.** 9/29 card: **account $295.15, BP $8.94** `[9/29 13:4x intraday]`; lines + BP = $290.15 ⇒ **$5.00 UNEXPLAINED (D-64)**. Per-line cost/value DERIVED from P/L ÷ P/L% (no Mark column ⇒ machine class `unverified` by design). The prediction-market line and the 9/01→9/25 dead-by-date bookings — USO $159C Sep-11 (bought 9/10, expired $0 — D-58) · QQQ $713C Sep-16 + USO $165C Sep-16 (both expired $0 — D-57) — verbatim → rotation 10/08 chunk B.

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **WAL $70P** | **Dec-18-2026** | 1 | **$2.20 ($220)** — bought 9/02 @ $2.20 (RH activity) ✓ | ≈$265.00 *(derived; mark ≈$2.65)* | ✅ **ON CARD 9/29 — +$45.00 / +20.45%** | TRY-WAL-ROLL70 (filled in Robinhood). Guard **`GATE-TERRY-ROLL70-EXIT`** *"WAL OFFICIAL CLOSE ≥ $81.90 on THREE CONSECUTIVE sessions"* — **0-of-3 as last recorded here** (REGINALD through 9/23, per TERRY STATUS 9/24; not re-read this pass). The option's +20.45% is not the gate — the gate reads WAL's close (rule 7). **$4.40 GTC sell order: CANCELLED / not there — Will 9/28** (`PROME/inbox/processed/2026-09-28_from-WAL_WQ-324-325-ruled-verbatim-and-4.40-GTC-cancelled.md`) ⇒ **no resting exit order; any take-profit is Will's manual act.** Time stop Fri 12/4. 78 DTE. **D-47** |
| **KRE $25P** | 1/15/2027 | 1 | $53.00 — card-derived ✓ | ≈$1.00 *(derived)* | ✅ **ON CARD 9/29 — −$52.00 / −98.11%** | Deep-OTM lottery; entry pre-7/16, never recorded — **D-54** (before the 9/01 activity view). 106 DTE |
| T | stock | 1 | — | — | ⚠️ no stocks card 9/29; no T row in RH activity 9/01→9/25 | Hypothesis: sold before 9/01, unconfirmed — **D-20**. The card no longer closes to the cent (D-64), so the 9/27 "no stock line" inference is weaker |

## Account UNATTRIBUTED — receipted fills not yet attributed to an account

*No rows. VLO ×1 (this section's only row since 9/19) moved to § Fidelity — Longs on the 9/25 ledger (D-55 account leg CLOSED). The section stays as the landing place for a receipt that names no account (the parser admits it — TERRY `cfd9b9115`).*

---

## ⚠️ Reconcile discrepancies (received 2026-10-29 18:25 ET; October29 post-close Fidelity lasts; quote clock not displayed; no ledger)

> Broker view > Will's word > desk record. Last prices are NOT settles. DTE from the receipt date only; no current executable bids. **Will manages his own expiries (`USER.md` § No expiry nagging, 10/20): DATED rows below are records, not prompts.** All prior duties survive unless explicitly closed. Prior section = `git show ec5a7058b:FORGE/STATUS.md`; older history = `100c63edc`, `ba1a41e09`, `6fbf39cd0` and existing rotations. Permanently UNKNOWN WQ-167: 9/2 USO135C sale price, never ask. This list records evidence and owners only; it carries no sell recommendation.

### Will supplies / PROME re-reads — facts owed

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| DATED | QQQ Oct-30 711P ×2 (NEW) · QQQ Oct-30 710P ×1 (NEW) · USO Oct-30 163C ×1 | 🔴 1 calendar DTE (expire Fri 10/30) | Values $1,350.00 / $613.00 / $545.00 `[10/29 close rcv 18:25 ET]`; bases $687.33 / $661.66 / $358.66. No contract-specific cards (D-77). Exercise mechanics under D-60 | Moneyness at expiry not verified (no QQQ/USO quote supplied); no thesis or approval inferred | **Will** (his expiries); **PROME** records |
| **D-60** | Fidelity expiring-option handling | 🔴 next expiry 10/30 | Prior ledgers show Fidelity "SOLD CLOSING OPTION LIQUIDATION" rows on expiry day (QQQ Oct-20 719P +$208.99; Oct-21 715P +$1.99; Oct-02 740P +$3.75). Five more expiry dates passed this window (10/22, 10/23 ×2, 10/26, 10/28) with outcomes UNSEEN (D-90). Mechanics only: an exercised put SELLS 100 shares per contract at the strike | INFERRED: the broker liquidates some expiring contracts itself; trigger, timing and ITM exercise/IRA handling never observed | **Will** broker policy |
| DATED | QQQ Nov-02 715P ×1 (NEW) · GLD Nov-02 375C ×2 (NEW) | 🟠 4 calendar DTE | Values $1,047.00 (+116.02%, a mark, no registered line) / $102.00; bases $484.66 / $651.33. No cards (D-77) | No scale approval or roll linkage inferred | **Will**; PROME scope |
| **D-90** NEW | Unseen 10/22→10/29 ledger | 🟠 record before any realized claim | No Activity/Orders supplied. UNSEEN: AAPL −1 (basis −$23.65); USO −5 (basis −$594.42 ≠ 5 × avg $609.49); GLD +3 (+$1,098.75); TBT +5 (+$193.60); ten NEW long lines (basis $6,604.92) + the short 670P (credit $1,742.63); seven GONE lines (basis $2,058.28); VLY fill. **Cash+pending $17,476.86 → $14,348.72 = −$3,128.14.** DERIVED identity (assumes basis = cash paid/received): window sales + other cash flows − round-trip buys = −$3,128.14 + net basis added $6,154.64 = **+$3,026.50**; less removed basis $2,676.35 ⇒ **window realized + other flows +$350.15 — an aggregate, not booked** | HYPOTHESIS: the +$350.15 splits across AAPL, USO, the seven GONE lines and any between-capture round trips; split, dates, prices and whether any line lapsed are UNKNOWN. Pending changed character (10/22 = processing trades; 10/29 = "margin credit balance") | **Will** supplies Activity & Orders 10/22→10/29 (PROME asked, round 2); **PROME** records |
| **D-91** NEW | Short-leg representation (consumer interface) | 🟠 before commit | QQQ Nov-20 670P written with signed Qty `−2`, negative value, opening credit as basis. `positions_from_forge.py` parses qty −2 and value −1,168.00 (verified this pass). `desk_attention.py holdings()` requires an unsigned Qty (`^\d+`) and reports this row as "quantity unknown" | A consumer that sums value or qty without a sign check could mis-total; no consumer sweep has been run beyond these two | **PROME** (consumer sweep; owns `desk_attention.py`); **TERRY** (`positions_from_forge.py`) |
| **D-88** | QQQ Oct-20 715P ×1 disposition | 🟡 record | Unchanged: absent since 10/22; basis $200.66; +$17.34 unexplained in the 10/20 cash bridge | HYPOTHESIS (unchanged): consistent with a sale near $0.18 ⇒ conditional −$183.32; nothing booked | **Will** 10/20 Activity below the cut; **PROME** records |
| **D-89** | Working-order census | 🟡 NARROWED | VLY Dec-18 12P ×1 now a position (basis $15.66, consistent with the $0.15 limit, DERIVED). No Orders page this capture ⇒ working orders at 10/29 UNKNOWN | INFERRED (unchanged): the unseen 11th 10/22 order was the QQQ Oct-26 710P buy; VLY fill date UNKNOWN | **Will**; **PROME** books fills only from a capture |
| **D-82** | Approved sells not evidenced | 🟡 NARROWED | **TBT leg CLOSED by Will's word** (WQ-357 RESOLVED 10/29: rebought, 10 held, "no sale owed"; PROME-supplied). Still open: WQ-428 OZK 40P ×4 ($40.00) and WQ-429 WAL 65P ×4 ($100.00), both still held at the 10/29 close | Ordered/working/cancelled UNKNOWN (no Orders page); approvals are not executions | **Will** (disposition of his approvals); **PROME** records |
| **D-85** | QQQ Oct-20 719P basis allocation | 🟡 NARROWED (unchanged) | Cohort −$120.99 booked on the 10/22 mirror; per-leg split −$67.67 or −$68.67 | Which per-leg basis the broker treats as authoritative UNKNOWN | **PROME** records; **Will** lots if ever needed |
| **D-74** | Fidelity bank-put ownership / new-line scope | 🟡 record | Bank/credit put cluster now 41 contracts / 14 lines, basis $6,644.24, value $1,401.00 (vs 28 / $4,646.62 on TERRY's 10/24 view, TERRY packet). NEW KRE Nov-27 68P ×10, VLY Dec-18 12P ×1, FLG Mar-19-2027 10P ×1: owner/card/approval UNKNOWN; also Fidelity WAL70P2, ZION62.5P2, KRE 66P/70P. WAL65P4/OZK40P4 cards = D-82 | No inherited gate or approval from same symbol/heading | **PROME** scope; **Will/REGINALD/TERRY** |
| **D-77** | Off-thesis ownership/cards | 🟡 record | No contract-specific card: QQQ Oct-30 711P/710P, QQQ Nov-02 715P, GLD Nov-02 375C, USO Oct-30 163C, USO Nov-20 170C (Will's hand; WQ-491 idea not taken), KRE67P. The 690/670 spread HAS a card (TERRY `IDEA-QQQ-PUTWALL-OCT22`) | TERRY's card mentions "the two short-dated QQQ put lines" as the same Nasdaq-downside bet; which contracts is not stated here | **PROME** scope; **Will/TERRY** |
| **D-70** | Management mappings | 🟡 source changed — re-review owed | This file's bytes changed ⇒ every `position_management.tsv` mapping sourced to it is withheld until PROME re-reviews. Rows for seven GONE contracts now describe absent lines; no reviewed mapping for the 11 NEW rows or the GLD/TBT quantity changes | Mapping is not a card or trade approval | **PROME** mapping; **TERRY** cards |
| **D-84** | Unseen 10/19 entries and quantity changes | 🟡 evidence | Unchanged: CRWV56P1 (now GONE), Fidelity WAL70P2, ZION62.5P2 buys unseen; GLD residual2 $764.28; VLO 2→3; USO 37→35; CMG 2→1 (CMG now GONE) | Dates/prices/proceeds/realized UNKNOWN | **Will** earlier Activity; **PROME** records |
| **D-86** | Three expired contracts absent (Oct-15/16) | 🟡 outcome evidence owed | QQQ Oct15 715P, Oct16 735C, HBAN Oct16 16P; unchanged | Sale/exercise/lapse UNKNOWN | **Will** earlier Activity; **PROME** records |
| **D-78** | VLO extra-share scope | 🟡 scope before action | 3 sh, basis $1,296.73, unchanged; `GATE-TERRY-VLO-HELD-01` letter unchanged (crack-basis) | Neither added share extends original management scope | **Will** authorization; **PROME/TERRY** scope |
| **D-76** | Detailed fills/lots | 🟡 evidence | This capture carries no fills at all (D-90). USO lot relief ≠ average cost (D-90). Prior 10/22 fill prices historical | No broker realized-P/L report; all realized DERIVED | **Will** lots/fills; **PROME/TERRY** integrate |
| **D-80** | Prior unseen GLD+3 / HBAN−1 / QQQ Oct16 725P opening | 🟡 carried | 10/15 gaps unchanged | Nothing resolved by later holdings | **Will** earlier Activity; **PROME** records |
| **D-87** | 10/19 marks vs Fidelity's prior-day reference | 🟡 record | Unchanged; not testable on this capture (a week of sessions since the mirror) | INFERRED (unchanged) | **PROME** record |
| **D-83** | Clock / Robinhood | 🟡 standing | Receipt 10/29 18:25 ET; post-close view, quote clock not displayed; lasts not settles. Robinhood 9/29 card is 30 days old; Will's word 10/29: "all dead", written off — rows retained, unverified | RH values may be ≈$0; no closure booked without a capture | **Will** RH view if he wants it closed out; **PROME** records |
| **D-81** | Historical 10/14 cash mismatch | 🟡 record | +$16.58 vs post-744P balance; later captures tie | Different cut or unseen item UNVERIFIED | **PROME** record |
| **D-79** | Quote/value precision | 🟡 record | 10/29: all 28 values and open G/L tie to the cent; 11 rows' displayed open % differ by 0.01 pt from G/L ÷ basis (USO, QQQ 715P, APD, VLY, QQQ 710P, KRE66P, KRE65P, OZK, WAL70P, KRE67P, both KRE60P). Option avg cost × qty differs from basis by $0.33–$3.37 (fees in basis) | Rounding source UNVERIFIED; no figure affected | **PROME** evidence |
| **D-75 · D-66 · D-69 · D-62 · D-63 · D-64 · D-65 · D-61 · D-59 · D-45 · D-55 · D-28 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1** | **Carried discrepancies (18) — every row still OPEN; rows verbatim → rotation 10/08 chunk D1 (D-75) + D2 (the other 17)** | 🟡 carried | None closed, re-dated or re-owned; every cell unchanged in the record. Ticker-bearing items, for the text scan: STNG (D-17) · RH QQQ $715P Aug-31 (D-28) · RH KRE $25P entry (D-54) · RH WAL $77.5P Aug-21 sale (D-18) · the RH T share (D-20) · AAPL 5-sh sale pre-7/30 (D-1) · D-75 (OZK 40P basis 1¢; mirror carries $322.65, record only) | Returns to this table when its state changes | As recorded, per row: **Will** — D-66 · D-69 · D-63 · D-64 · D-61 · D-59 · D-45 · D-55 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1; **RH history before 9/01** — D-28; **PROME** — D-62 · D-65 (re-reads of desktop-local images) · D-75 (record) |

*D-69 missing +$53.54 remains OPEN. D-66 now includes every 10/22→10/29 fill clock (D-90). D-71 broker leg remains CLOSED (cohort +$142.44, rotation 10/15 chunk A); D-72/D-73 historical closures unchanged. No duty closed by silence; this pass closed only D-82's TBT leg (Will's word) and narrowed D-89 (VLY filled).*

*Guards: each management line's text sits beside its number in the rows above (QQQ 690/670 spread card, GLD rails, VLO crack-basis letter, KRE65P time stop, USO no live rule). D-47 RH WAL70P `GATE-TERRY-ROLL70-EXIT` last recorded 0-of-3 (stale). Option P/L percentages are marks, not harvest/disarm readings; no gate adjudicated this pass.*

---

## Immediate Actions (10/29 18:25 ET post-close receipt) — evidence and records only

| Item | State | Owner |
|---|---|---|
| 🔴 Three Oct-30 lines (QQQ 711P ×2, 710P ×1, USO 163C ×1) at 1 calendar DTE; D-60 handling only partly observed | record, not a prompt | **Will** (his call) |
| 🟠 D-90 Activity & Orders 10/22→10/29 unseen (all changes, seven GONE outcomes, −$3,128.14 cash bridge); D-91 short-leg Qty vs `desk_attention.py` | evidence / consumer sweep | **Will** ledger; **PROME** |
| 🟡 D-70 mapping re-review (11 NEW rows unmapped, 7 GONE); D-82 OZK/WAL approved sales still held; D-74/D-77 new-line ownership; all other D-rows and 18 carried duties remain | integration / scope | **PROME/TERRY/Will** |

---

*History → `_archive/JOURNAL.md`, existing rotations and Git; immediately prior whole mirror = `git show ec5a7058b:FORGE/STATUS.md` | `PORTFOLIO.md` FROZEN Feb snapshot, never live | Truth = Will/broker off-repo | Current evidence → `PROME/data/2026-10-29_broker-capture-TRANSCRIPTION.md` (28 Fidelity positions incl. one short leg; no Activity, no Orders; posted 18:25 ET, post-close lasts; quote clock not displayed). Robinhood source remains 9/29; prior evidence/history survives in Git.*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumers: `AGENTS/TERRY/scripts/positions_from_forge.py` (sections `^## (Fidelity|Robinhood)` + `^## Account <NAME>`; table headers by prefix; cell text — emphasis and strikethrough visible) · `PROME/tools/desk_attention.py` `holdings()` (same sections; `Qty` + `Ticker|Strike|Position` headers; expiry year from `**Updated:**`) · `PROME/tools/will_brief.py` `parse_money()` (header before the first `## `: `account total:**`, `money market):** $X (Y%)`, `**Updated:** YYYY-MM-DD`, `marks = [Fri ]YYYY-MM-DD`) · `FORGE/position_management.tsv` `source_sha256` (any byte change here withholds every mapping sourced to this file until PROME re-reviews) · `AGENTS/BRENT/scripts/pending_receipts.py` (text-level closure candidates). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself here in the same commit that starts parsing. *(Pass notes 9/27 → 10/8 → rotation 10/08 chunk G. Conventions they set, still binding: the header money line keeps the shape `will_brief.py` reads; option expiries carry the year; the `Mark <m/d>` header is prefix-bound; terminal records live in italic lines, which no parser reads as rows. 10/29: a SHORT option leg carries a signed Qty `−N` and a negative value — D-91.)*
