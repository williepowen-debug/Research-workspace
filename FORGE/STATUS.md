# FORGE — Trading Operations

Dashboard management mapping → [position_management.tsv](position_management.tsv); maintenance contract → [dashboard notes](DASHBOARD.md). Holdings remain in this file; approval, order and fill evidence are separate. A changed evidence source invalidates its management mapping until reviewed.

> ✅ **2026-10-08 (Thu) — RECONCILE BY ANVIL to Will's Fidelity capture RECEIVED ≤15:26 ET TODAY: positions + Activity. INTRADAY; exact capture time UNKNOWN; marks are NOT closes.** Source `PROME/data/2026-10-08_broker-capture-TRANSCRIPTION.md`; ANVIL re-verified 19/19 rows (Decimal) and the tie: Σ positions **$21,945.52** + cash **$11,421.19** + pending **+$1,283.98** = **$34,650.69 to the cent**. **Vs 10/7 (`git show e8fd99acf:FORGE/STATUS.md`): 1 NEW (QQQ $750C Oct-09 ×1) · 0 GONE · 2 QTY CHANGE (755P Oct-09 2→1 · 745P Oct-15 2→1, sold to close 10/8) · 16 MARK ONLY.** Full receipt → rotation 10/08 chunk A.
>
> ⚠️ **ACCOUNT SCOPE — Fidelity: ONE Traditional IRA; account number redacted ⇒ *****1326 INFERRED by position-set match. Robinhood Individual: NOT in this capture — rows carried from 9/29, unverified today.** Absence from this Fidelity view establishes no Robinhood closure.
>
> **Updated:** 2026-10-08 = broker-capture date (received ≤15:26 ET) · marks = 2026-10-08 INTRADAY capture, exact time UNKNOWN (all Fidelity lines `[10/8 rcv]`) · **Fidelity cash (money market):** $11,421.19 (32.96%) + **Pending activity +$1,283.98** (the three 10/8 fills, shown) · **Fidelity account total:** $34,650.69 (Today +$1,734.39 / +5.27%; open G/L +$2,087.31 / +10.51%) — versus 10/7 intraday $31,898.27: +$2,752.42 = positions +$1,468.43 + cash −$1,572.63 + pending +$2,856.62 (a snapshot change, not a P&L figure). **Realized 10/8 (derived from the broker's lot basis):** 755P ×1 +$596.65 · 745P ×1 +$321.65 = **+$918.30**. **Booked from Activity (derived):** Oct-02 740P ×4 −$886.90 · Oct-05 735P ×5 −$1,302.97 (D-72). Oct-01 740P ×4 exit still unbooked (D-71). **Robinhood:** $295.15 / BP $8.94 `[9/29 13:4x intraday]`, not re-captured. Prior header/details preserved at `git show e8fd99acf:FORGE/STATUS.md`; rotations → `_archive/STATUS_ROTATION_2026-10-08.md`, `_archive/STATUS_ROTATION_2026-10-01.md`, `…_2026-09-29.md`, `…_2026-09-27.md`, `…_2026-09-20.md`, `…_2026-09-10.md`, `_archive/RECONCILE_2026-08-29_RECORD.md`.

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (its own header names the current base and amendment count). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All cells `[10/8 rcv]` (capture 2026-10-08 intraday, time UNKNOWN); all six MARK ONLY versus 10/7. Rounded average costs and percentages are preserved as displayed, not exact fills. Settled fill notes → rotation 10/01 chunk B.*

| Ticker | Type | Qty | Cost | Mark 10/8 rcv | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | 10 | $23.65 | $340.535 | $3,405.35 | +$3,168.90 / +1340.19% | Today +$38.65. 9/15 sale of 5 sh (≈+$1,534.92, derived) in rotation; pre-7/30 5-sh sale = D-1 |
| GLD | Stock | 17 | $374.74 | $378.43 | $6,433.31 | +$62.81 / +0.98% | Today +$43.35. MIDAS domain; largest line by this capture’s value |
| USO | Stock | 37 | $122.28 | $147.9101 | $5,472.67 | +$948.40 / +20.96% | Today +$148.00. **WQ-200 DECLINED by Will 9/10 — NO harvest/give-back rule live; Will manages by hand.** BRENT thesis (Hormuz-gap entry) |
| VLO | Stock | 1 | $412.00 | $445.995 | $445.99 | +$33.99 / +8.25% | Today +$21.89. Bought 9/18 @ $412.00 (fill TIME not shown — D-55). **Holding confirmed by Will 2026-10-07: “Yes, still one share”**. WQ-213: 1 of 3; **the remaining 2 sh STAND DOWN** under `PROME/GATES.tsv` GATE-TERRY-VLO-SCALE, TERMINAL on the 9/25 F1 fire (TERRY 4ad672c43; its optional CME source-① override remains as written there). **The held share's exit rule is `GATE-TERRY-VLO-HELD-01` — the letter (condition AND consequence cells, incl. who acts on each leg) is read at `PROME/GATES.tsv`, as amended by WQ-386 (`PROME/proposals/2026-10-07_VLO-december-management-RULED.md`, approved 10/7); nothing of it is restated here.** The gate reads the crack and the text, not the share's mark. The prior note, which restated the letter, is verbatim in rotation 10/08 chunk H |
| APD | Stock | 2 | $294.79 | $278.45 | $556.90 | −$32.67 / −5.55% | Today +$0.66. Historical 10/1 "D" badge / $1.81 reference-price adjustment remains unverified; no dividend row in the 10/2–10/8 Activity. Thesis tag unassigned since 7/30 |
| TBT | Stock | 10 | $34.65 | $42.13 | $421.30 | +$74.84 / +21.60% | Today −$8.50. Duration-short leg (BOND/TERRY). **WQ-357 LATER 10/3: HELD on path C while BOND researches; 10/14 decision clock remains; no exit order inferred.** |

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

*No live event-box rows — the VIX $20C/$25C spread (CLOSED 2026-07-30, realized −$111.60) and the five Aug-21-2026 EXPIRED rows (realized −$2,816.72 total) are terminal → rotation records.*

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, owned by no agent — recorded so it is not invisible. **Rail = Will's standing practice, SELL-OR-ROLL before expiry** (`USER.md`, 9/30 19:03 ET). TERRY cards (recommendations; the order is Will's): `MGMT-USO150C-OCT09` (Fri 10/09 15:00 ET hard stop) · `MGMT-QQQ755P-OCT09` · `MGMT-QQQ745P-OCT15` / `MGMT-QQQ740P-OCT15` (`AGENTS/TERRY/setups/`). **The NEW QQQ Oct-09 750C has its own card since 10/8 19:05 ET: `MGMT-QQQ750C-OCT09` (TERRY beb763aa3) — SELL Fri 09:45–10:30 ET, no later than 12:00, never into the close, roll NONE; with the 755P ×1 held, at ANY Friday close at least one Oct-09 QQQ line is in the money.** Entry dates/net amounts below = the 10/8 Activity view; per-contract buy prices and all times NOT shown (D-66).

| Ticker | Strike | Expiry | Qty | Cost | Mark 10/8 rcv | Value | P&L | Note |
|--------|--------|--------|-----|------|---------------|-------|-----|------|
| QQQ | $755P | Oct-09-2026 | 1 | $2.39 | $7.85 | $785.00 | +$546.34 / +228.91% | `[10/8 rcv]`; **QTY CHANGE 2→1.** Bought 10/6 −$477.33 (Activity). **1 SOLD TO CLOSE 10/8 @ $8.36, net +$835.32 ⇒ realized +$596.65** (derived: lot basis $477.33 − $238.66 = $238.67); 2nd sell (limit $8.50) Verified Canceled. Today +$582.00. **EXPIRES FRI 10/09; 1 DTE; ITM ≈$7.84 at QQQ $747.16 `[WALTER Yahoo screening 15:26:49 ET, not broker]`.** Card `MGMT-QQQ755P-OCT09`: *"Do not carry into Friday. No roll."* — not adjudicated. ITM handling UNOBSERVED (D-60). 3.29× last/avg is a mark multiple; no harvest gate. Working order UNKNOWN |
| QQQ | $750C | Oct-09-2026 | 1 | $1.57 | $1.79 | $179.00 | +$22.34 / +14.26% | `[10/8 rcv]`; **NEW — BOUGHT TO OPEN 10/8 ×1 @ $1.56, −$156.66 (Activity). Will-direct; card `MGMT-QQQ750C-OCT09` (TERRY 10/8 19:05 ET, beb763aa3): SELL at Fidelity's bid Fri 09:45–10:30 ET, ≤ 12:00, never into the close; roll NONE.** Today +$22.34. Broker "last change" −$7.14 shown verbatim, unexplained. **EXPIRES FRI 10/09; 1 DTE**; ≈$2.84 OTM at QQQ $747.16 (WALTER screening). Sell-or-roll before expiry (WQ-397 carries both Oct-09 QQQ lines). Linkage to the 755P not declared — none inferred; mechanically, at ANY Friday close at least one of the two is in the money (card § 4) |
| USO | $150C | Oct-09-2026 | 1 | $3.00 | $0.66 | $66.00 | −$233.66 / −77.98% | `[10/8 rcv]`; MARK ONLY; basis $299.66; Today +$27.00. **Still held: no USO option row in the 10/2–10/8 Activity.** **WQ-366 DECLINE 10/3: early sale declined; hold to Fri 10/09 15:00 ET hard stop** (`MGMT-USO150C-OCT09`). USO stock last $147.9101 in the same view: $2.09 below strike. $0.66 is last, NOT an executable bid. No price harvest gate; not the 37-share line. 1 DTE; working order UNKNOWN |
| QQQ | $745P | Oct-15-2026 | 1 | $2.84 | $5.73 | $573.00 | +$289.34 / +102.00% | `[10/8 rcv]`; **QTY CHANGE 2→1.** Bought 10/7 −$567.33 (Activity). **1 SOLD TO CLOSE 10/8 @ $6.06, net +$605.32 ⇒ realized +$321.65** (derived: $567.33 − $283.66 = $283.67 lot basis). Remaining basis $283.66; Today +$319.00. **EXPIRES THU 10/15; 7 DTE.** Card `MGMT-QQQ745P-OCT15`: *"SELL-OR-ROLL BEFORE THURSDAY 10/15"*; its Wed 10/14 times are *"a PROPOSAL for Will"* — not a registered deadline |
| QQQ | $740P | Oct-15-2026 | 4 | $5.31 | $4.05 | $1,620.00 | −$502.65 / −23.69% | `[10/8 rcv]`; MARK ONLY; basis $2,122.65 = bought 10/2 −$2,122.65 (Activity; contract count not in the row). Today +$932.00. **EXPIRES THU 10/15; 7 DTE.** Card `MGMT-QQQ740P-OCT15`, same text as the 745P. If ITM at expiry: ×4 = sell 400 QQQ at $740 ($296,000) — contract mechanics, not a claim (D-60) |

*QQQ Oct-02 740P ×4 and Oct-05 735P ×5: CLOSED from the 10/8 Activity (D-72 → § Reconcile discrepancies, CLOSED this pass). Their old cards do not govern the live lines.*

## Fidelity — Thesis Puts

*Instrument grouping is navigation, not approval: the Fidelity WAL/OZK rows below are Will-direct holdings (bought 10/7, Activity); thesis/desk ownership and management approval are NOT established by the broker view.*

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

*TLT $77P Sep-30 ×15 (TRY-FIRE-004's last lot): SOLD TO CLOSE 9/30 ⇒ −$154.64; no replacement TLT line; detail → rotation 10/01 chunk D.*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $82P | Oct-16-2026 | 1 | $1.68 | $4.05 | $405.00 | +$237.33 / +141.54% (today −$82.00) `[10/8 rcv]`. MARK ONLY; basis $167.67. 9/28: sold 1 of 2 @ $3.60 ⇒ +$191.66. **WQ-357 LATER 10/3 selects path C: HELD to 10/14 while BOND researches.** Research delivered 10/5 (`ff0992bf1`), not a new trade ruling. `MGMT-TLT82P-OCT16` (×2 original, ×1 remaining) / WQ-302: **Wed 10/14 close** clock remains; no undecided A/B/C choice asserted here. 2.42× basis is a last-mark multiple, not a price trigger; nothing adjudicated. ITM expiry handling in the IRA UNOBSERVED (D-60). 8 calendar DTE from 10/8 |

### KRE — regional banks (REGINALD)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
*All three rows `[10/8 rcv]` (capture 2026-10-08 intraday, time UNKNOWN). KRE $60P Sep-30 ×2 sold 9/30 @ $0.01 ⇒ −$451.48 (leg 1 of the roll into the Dec-31 65P; detail + the D-67 mark note → rotation 10/01 chunk D). Rail on the 65P: *"hard stop Thu 12/31 15:00 ET"* (`MGMT-KRE65P-DEC31`, `5ce609f80`).*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $60P | Dec-18-2026 | 2 | $2.57 | $0.57 | $114.00 | −$399.34 / −77.80% (today −$22.00). MARK ONLY; basis $513.34. 71 calendar DTE from 10/8 |
| $60P | Dec-18-2026 | 3 (M) | $2.93 | $0.57 | $171.00 | −$707.02 / −80.53% (today −$33.00) — multi-lot marker; basis $878.02; **five** Dec-18 KRE 60P across two lots. MARK ONLY. 71 calendar DTE from 10/8 |
| $65P | Dec-31-2026 | 2 | $1.69 | $1.46 | $292.00 | −$45.33 / −13.44% (today +$38.00) — MARK ONLY; basis $337.33. Bought 9/30 ×2 @ $1.68 (roll leg 2). Will's own add; `MGMT-KRE65P-DEC31` (`5ce609f80`): hard stop Thu 12/31 15:00 ET, not a price gate. 84 calendar DTE from 10/8 |

### WAL (REGINALD) — Sep-18 pair EXPIRED

*$70P + $67.5P Sep-18 ×1 each: **EXPIRED as of 9/18, broker-confirmed** (ledger rows posted 9/21) ⇒ realized **−$768.67 and −$750.67 = −$1,519.34** (full basis) — the WQ-168 ①② LAPSE as ruled. Rows → rotation record. Duration roll = the Robinhood WAL Dec-18 $70P ×1 below. The RH WAL $77.5P Aug-21 sale: P&L UNRECORDED — D-18.*

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18-2026 | 1 | $11.85 | $1.25 | $125.00 | −$1,059.67 / −89.45% | `[10/8 rcv]`; basis $1,184.67; Today −$19.00. MARK ONLY; BROCK thesis vehicle. Will ruled HOLD 2026-08-13 (`PROME/proposals/2026-08-13_private-credit-batch-RULED.md` §②; vehicle-mismatch flag live). 71 calendar DTE from 10/8 |
| HBAN | $16P | Oct-16-2026 | 2 | $0.96 | $0.70 | $140.00 | −$51.34 / −26.84% | `[10/8 rcv]`; basis $191.34; Today −$34.00. MARK ONLY. The 7/18 ride-to-expiry premise failed per TERRY 9/26; `MGMT-HBAN16P-OCT16` / WQ-302 re-rule due **Wed 10/14**. Current moneyness not verified (no underlying quote in the view). 8 calendar DTE from 10/8 |
| OZK | $40P | Nov-20-2026 | 4 | $0.81 | $0.45 | $180.00 | −$142.65 / −44.22% | `[10/8 rcv]`; basis **$322.65** (10/7 view showed $322.66 — D-75); Today −$80.00. **Bought 10/7, −$322.65 (Activity); Will-direct.** Thesis/desk ownership and management approval UNRECORDED; holdings do not autoapprove research or a trade. Sell-or-roll before expiry; no contract-specific card recorded. 43 calendar DTE from 10/8 |
| WAL | $65P | Dec-18-2026 | 4 | $1.71 | $1.40 | $560.00 | −$122.65 / −17.97% | `[10/8 rcv]`; basis $682.65; Today −$160.00. **Bought 10/7, −$682.65 (Activity); Will-direct.** Thesis/desk ownership and management approval UNRECORDED; holdings do not autoapprove research or a trade. Sell-or-roll before expiry; no contract-specific card recorded. Distinct from Robinhood WAL Dec-18 $70P ×1. 71 calendar DTE from 10/8 |


## Robinhood — satellite account (Individual)

*All holdings/figures below retained from the 9/29 source; carried DTE annotations are historical, not a current freshness assertion.*

> ⚠️ **NOT CAPTURED IN THIS 10/8 RECEIPT (nor 10/7, 10/1 or 9/30) — every cell below is the 9/29 card, unverified today.** 9/29 card: **account $295.15, BP $8.94** `[9/29 13:4x intraday]`; lines + BP = $290.15 ⇒ **$5.00 UNEXPLAINED (D-64)**. Per-line cost/value DERIVED from P/L ÷ P/L% (no Mark column ⇒ machine class `unverified` by design). The prediction-market line and the 9/01→9/25 dead-by-date bookings — USO $159C Sep-11 (bought 9/10, expired $0 — D-58) · QQQ $713C Sep-16 + USO $165C Sep-16 (both expired $0 — D-57) — verbatim → rotation 10/08 chunk B.

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **WAL $70P** | **Dec-18-2026** | 1 | **$2.20 ($220)** — bought 9/02 @ $2.20 (RH activity) ✓ | ≈$265.00 *(derived; mark ≈$2.65)* | ✅ **ON CARD 9/29 — +$45.00 / +20.45%** | TRY-WAL-ROLL70 (filled in Robinhood). Guard **`GATE-TERRY-ROLL70-EXIT`** *"WAL OFFICIAL CLOSE ≥ $81.90 on THREE CONSECUTIVE sessions"* — **0-of-3 as last recorded here** (REGINALD through 9/23, per TERRY STATUS 9/24; not re-read this pass). The option's +20.45% is not the gate — the gate reads WAL's close (rule 7). **$4.40 GTC sell order: CANCELLED / not there — Will 9/28** (`PROME/inbox/processed/2026-09-28_from-WAL_WQ-324-325-ruled-verbatim-and-4.40-GTC-cancelled.md`) ⇒ **no resting exit order; any take-profit is Will's manual act.** Time stop Fri 12/4. 78 DTE. **D-47** |
| **KRE $25P** | 1/15/2027 | 1 | $53.00 — card-derived ✓ | ≈$1.00 *(derived)* | ✅ **ON CARD 9/29 — −$52.00 / −98.11%** | Deep-OTM lottery; entry pre-7/16, never recorded — **D-54** (before the 9/01 activity view). 106 DTE |
| T | stock | 1 | — | — | ⚠️ no stocks card 9/29; no T row in RH activity 9/01→9/25 | Hypothesis: sold before 9/01, unconfirmed — **D-20**. The card no longer closes to the cent (D-64), so the 9/27 "no stock line" inference is weaker |

## Account UNATTRIBUTED — receipted fills not yet attributed to an account

*No rows. VLO ×1 (this section's only row since 9/19) moved to § Fidelity — Longs on the 9/25 ledger (D-55 account leg CLOSED). The section stays as the landing place for a receipt that names no account (the parser admits it — TERRY `cfd9b9115`).*

---

## ⚠️ Reconcile discrepancies (10/8 intraday capture + Activity, built 2026-10-08)

> Fidelity positions + Activity (visible rows 10/2→10/8; the image is cut below the 10/2 rows); capture time UNKNOWN, received ≤15:26 ET; Robinhood not captured. **Broker view > Will's word > desk record; conjectures labeled; nothing resolved by invention.** DTE = calendar days from 10/8. **Permanently UNKNOWN by WQ-167 (never asks):** the 9/2 USO 135C sale price. Prior list → `git show e8fd99acf:FORGE/STATUS.md`; older → rotation 10/01 chunk E.

*EXPIRING — Fri 10/09: QQQ $755P ×1 · QQQ $750C ×1 (NEW; carded 10/8 19:05 ET, `MGMT-QQQ750C-OCT09`) · USO $150C ×1 (15:00 ET stop) · Thu 10/15: QQQ $745P ×1 + $740P ×4 · Fri 10/16: TLT $82P ×1 + HBAN $16P ×2. Facts and cards: the position rows above; urgency and owners: § Immediate Actions; the 10/8-built six-row table verbatim → rotation 10/08 chunk C. WQ-347 (cited there for the QQQ lines) now carries only D-71, the row after D-60 below. D-60 (ITM expiry handling UNOBSERVED) stays live, first row of the next table.*

### Will supplies / PROME re-reads — facts owed

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-60** | **Fidelity expiry handling — ITM leg UNOBSERVED** | 🔴 bears on the 755P ×1 Fri, then 10/15–16 | Liquidation leg now **×5** (adds Oct-02 740P, liquidated 10/2, its expiry day); expired-no-cash **×4** (adds Oct-05 735P, as of 10/5). IRA holds 0 QQQ / 0 TLT. Exercise of the 755P ×1 = sell 100 QQQ at $755 ($75,500) — mechanics, not a claim | ITM handling and what decides LIQUIDATE vs EXPIRED: UNKNOWN; moneyness of the two new observations not shown | **Will** — Fidelity's handling |
| **D-71** (narrowed, OPEN) | **Oct-01 QQQ 740P ×4 — ROLL confirmed, exit fill unbooked** | 🟡 record | Will 10/1 17:04 ET: "I rolled them." The 10/1 exit is **below the 10/8 image's cut** (rows start 10/2). Derived: 10/1 cash $14,147.60 + pending +$1,377.10 = **$15,524.70 = the balance before the first 10/2 row** ⇒ no net unseen cash. ⚠️ The +$3.75 liquidation closes the **Oct-02** contract (D-72), NOT this exit | PROME's net +$22.75 ⇒ ≈ −$747.91 stays an inference; pending composition NOT shown | **Will** — the same Activity, scrolled to 10/1 |
| **D-70** | **Management mappings / cards follow-through** | 🟡 re-review / consumption | Any byte change here invalidates mappings pinned to the old `source_sha256` until re-review. Cards now exist for 755P/745P/740P (10/7); none for the 750C; PROME → TERRY 10/8 asks TERRY to book the three 10/8 fills. ANVIL edits no TSV or card | Completion/consumption is PROME's verification; holdings are not a card approval | **PROME** (mapping re-review); **TERRY** (cards) |
| **D-74** | **New Fidelity bank puts — ownership / management unrecorded** | 🟡 record | WAL Dec-18 65P ×4 (bought 10/7, −$682.65), OZK Nov-20 40P ×4 (10/7, −$322.65); $560.00 / $180.00 `[10/8 rcv]`. WAL differs from RH Dec-18 70P ×1 | Thesis/desk owner/approval not established; no autoapproved research or trade | **PROME** routes scope; **Will** / TERRY |
| **D-75 · D-66 · D-69 · D-62 · D-63 · D-64 · D-65 · D-61 · D-59 · D-45 · D-55 · D-28 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1** | **Carried discrepancies (18) — every row still OPEN; rows verbatim → rotation 10/08 chunk D1 (D-75) + D2 (the other 17)** | 🟡 carried | None closed, re-dated or re-owned; every cell unchanged in the record. Ticker-bearing items, for the text scan: STNG (D-17) · RH QQQ $715P Aug-31 (D-28) · RH KRE $25P entry (D-54) · RH WAL $77.5P Aug-21 sale (D-18) · the RH T share (D-20) · AAPL 5-sh sale pre-7/30 (D-1) · D-75 (OZK 40P basis 1¢; mirror carries $322.65, record only) | Returns to this table when its state changes | As recorded, per row: **Will** — D-66 · D-69 · D-63 · D-64 · D-61 · D-59 · D-45 · D-55 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1; **RH history before 9/01** — D-28; **PROME** — D-62 · D-65 (re-reads of desktop-local images) · D-75 (record) |

*Owner-decides rows (D-47 — RH WAL Dec-18 $70P ×1, `GATE-TERRY-ROLL70-EXIT` 0-of-3 as last recorded, no resting exit order, time stop 12/4: Will harvests · REGINALD grades · TERRY proposes · WQ-386 / VLO-SCALE: TERRY grades, Will executes · WQ-200 — USO 37 sh, no rule live, Will's hand · the APD tag / "D" badge: PROME / Will) verbatim → rotation 10/08 chunk E; live letters: § Longs (VLO · USO · APD), the Robinhood WAL $70P row, `PROME/GATES.tsv` (canonical for every gate here).*

*CLOSED this pass (receipts = the 10/8 Activity view, transcription §①): **D-72** — Oct-02 740P ×4 −$886.90 · Oct-05 735P ×5 −$1,302.97 (derived; per-row contract counts NOT shown) · **D-73** — the five 10/2–10/7 entries; running balance $15,524.70 → $12,993.82 → $11,421.19, every link holds; the 10/7 pending −$1,572.64 settled at −$1,572.63 (D-75) · **QTY CHANGE ×2 + NEW ×1**, realized 10/8 +$918.30 (derived), 16 MARK ONLY. Bullets verbatim → rotation 10/08 chunk F.*

---

## Immediate Actions (10/8 intraday reconcile state)

| Item | State | Owner |
|---|---|---|
| 🔴 **QQQ Oct-09 755P ×1 — ITM; card says "Do not carry into Friday"; D-60 ITM handling unobserved** | 1 DTE | **Will** / TERRY card |
| 🔴 **QQQ Oct-09 750C ×1 — NEW; card `MGMT-QQQ750C-OCT09` (10/8 19:05 ET)**: SELL Fri 09:45–10:30 ET, never into the close | 1 DTE | **Will** / TERRY |
| 🔴 **USO Oct-09 150C ×1** — Will declined early sale; Fri 10/09 15:00 ET hard stop (WQ-366 / L605) | existing clock | **Will** / TERRY |
| 🟠 **TLT 82P ×1 path C / HBAN 16P ×2**, Wed 10/14 clock; **QQQ Oct-15 745P ×1 + 740P ×4**, Thu expiry | dated | **Will** / TERRY |
| 🟡 **D-71** — the same Activity scrolled to 10/1 (the roll's exit fill; = WQ-347) | one view | **Will** |
| 🟡 **D-70 / D-74** — mappings re-review; cards; new bank-put ownership · **carried discrepancies (18)** — the summary row in § facts owed, owners per row; Robinhood not captured (the four 10/8-built 🟡 rows → rotation 10/08 chunk I) | owner integration | **PROME / TERRY / Will** |

---

*History → `_archive/JOURNAL.md` | Prior reconciles in git history + `_archive/`; immediately prior whole mirror = `git show e8fd99acf:FORGE/STATUS.md` | Full-portfolio Feb snapshot → `PORTFOLIO.md` (**FROZEN/superseded, historical only — never cite as live**) | Position truth = Will/broker direct (off-repo) | Marks-of-record transcription → `PROME/data/2026-10-08_broker-capture-TRANSCRIPTION.md` (Fidelity 10/8 intraday positions + Activity, received ≤15:26 ET, exact time UNKNOWN); prior `…2026-10-07_…` · `…2026-10-01b_…` (post-close) · `…2026-10-01_…` (intraday + Pending list) · `…_2026-09-30_…` · `…_2026-09-29_…` (RH rows' source)*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumers: `AGENTS/TERRY/scripts/positions_from_forge.py` (sections `^## (Fidelity|Robinhood)` + `^## Account <NAME>`; table headers by prefix; cell text — emphasis and strikethrough visible) · `PROME/tools/desk_attention.py` `holdings()` (same sections; `Qty` + `Ticker|Strike|Position` headers; expiry year from `**Updated:**`) · `PROME/tools/will_brief.py` `parse_money()` (header before the first `## `: `account total:**`, `money market):** $X (Y%)`, `**Updated:** YYYY-MM-DD`, `marks = [Fri ]YYYY-MM-DD`) · `FORGE/position_management.tsv` `source_sha256` (any byte change here withholds every mapping sourced to this file until PROME re-reviews) · `AGENTS/BRENT/scripts/pending_receipts.py` (text-level closure candidates). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself here in the same commit that starts parsing. *(Pass notes 9/27 → 10/8 → rotation 10/08 chunk G. Conventions they set, still binding: the header money line keeps the shape `will_brief.py` reads; option expiries carry the year; the `Mark <m/d>` header is prefix-bound; terminal records live in italic lines, which no parser reads as rows.)* *(10/8 EVENING rotation pass, read-cap relief, no reconcile: no structural change inside any `## Fidelity` / `## Robinhood` / `## Account` region; the only position-row change is the VLO note cell (now a pointer to the gate letter); under § Reconcile discrepancies three `###` subsections → italic pointer lines, 18 carried rows → one summary row; the four parsed header shapes are byte-identical, that line carrying one appended rotation pointer; pinned mappings re-pinned in the installing commit.)*
