# FORGE — Trading Operations

Dashboard management mapping → [position_management.tsv](position_management.tsv); maintenance contract → [dashboard notes](DASHBOARD.md). Holdings remain in this file; approval, order and fill evidence are separate. A changed evidence source invalidates its management mapping until reviewed.

> ✅ **2026-10-07 (Wed) — RECONCILE BY ANVIL to the Fidelity screenshot RECEIVED TODAY. Will confirmed capture date October 7 (verbatim "yes today"); exact TIME UNKNOWN. Intraday capture (received before the regular close), not closing marks.** Source `PROME/data/2026-10-07_broker-capture-TRANSCRIPTION.md`; image `AGENTS/WALTER/inbox/WILL/Capture.JPG` viewed independently. All Fidelity cells `[10/7 rcv]` = `[broker capture 2026-10-07 intraday, exact time UNKNOWN]`; "Today" means the confirmed October 7 session. No Activity / Pending detail / Orders supplied. ANVIL independently verified 18 rows: value − basis = G/L; quantity × last × multiplier = value at displayed cent precision (VLO $422.605 last / $422.60 displayed value is valid half-cent rounding). Σ positions **$20,477.09** + cash **$12,993.82** − pending **$1,572.64** = **$31,898.27 to the cent**; Σ basis $20,223.90; Σ G/L +$253.19; Σ Today −$241.93. **Vs `git show 5d978cf73:FORGE/STATUS.md` (10/1 post-close): 5 NEW identities · 2 GONE · 0 QTY CHANGE · 13 MARK ONLY. NEW means newly present versus that mirror, not bought today.** No intervening fills or realized result inferred.
>
> ⚠️ **ACCOUNT SCOPE — Fidelity: ONE Traditional IRA; account number redacted ⇒ *****1326 INFERRED by position-set match. Robinhood Individual: NOT in this capture — rows carried from 9/29, unverified today.** Absence from this Fidelity view establishes no Robinhood closure. The two older Fidelity QQQ contracts are absent and past expiry; disposition/proceeds remain UNKNOWN without Activity.
>
> **Updated:** 2026-10-07 = confirmed broker-capture date (Will "yes today") · marks = 2026-10-07 INTRADAY capture, exact time UNKNOWN (all Fidelity lines `[10/7 rcv]`) · **Fidelity cash (money market):** $12,993.82 (40.74%) + **Pending activity −$1,572.64** (composition NOT SHOWN) · **Fidelity account total:** $31,898.27 (Today −$241.93 / −0.75%; open G/L +$253.19 / +1.25%) — versus 10/1 post-close $36,077.04: −$4,178.77 = positions −$75.25 + cash −$1,153.78 + pending −$2,949.74. This is a snapshot account-value change, NOT a trading-loss figure; transactions and cash flows are unshown. **Realized since 10/1: UNKNOWN; none booked in this pass.** Prior broker-shown realized 10/1 +$982.02 (midday partial sales); the Oct-01 QQQ ×4 roll is Will-confirmed (WQ-347), exact exit proceeds/realized still unbooked (D-71). **Robinhood:** $295.15 / BP $8.94 `[9/29 13:4x intraday]`, not re-captured. Prior header/details preserved at `git show 5d978cf73:FORGE/STATUS.md`; rotations → `_archive/STATUS_ROTATION_2026-10-01.md`, `…_2026-09-29.md`, `…_2026-09-27.md`, `…_2026-09-20.md`, `…_2026-09-10.md`, `_archive/RECONCILE_2026-08-29_RECORD.md`.

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (7/18 re-base + amendment #1 = current). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All cells `[10/7 rcv]` (capture 2026-10-07 intraday, time UNKNOWN); all six MARK ONLY versus 10/1 post-close. Rounded average costs and percentages are preserved as displayed, not exact fills. Settled fill notes → rotation 10/01 chunk B.*

| Ticker | Type | Qty | Cost | Mark 10/7 rcv | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | 10 | $23.65 | $336.62 | $3,366.20 | +$3,129.75 / +1323.64% | Today +$29.90. 9/15 sale of 5 sh (≈+$1,534.92, derived) in rotation; pre-7/30 5-sh sale = D-1 |
| GLD | Stock | 17 | $374.74 | $376.89 | $6,407.13 | +$36.63 / +0.57% | Today −$91.46. MIDAS domain; largest line by this capture’s value |
| USO | Stock | 37 | $122.28 | $143.30 | $5,302.10 | +$777.83 / +17.19% | Today −$59.57. **WQ-200 DECLINED by Will 9/10 — NO harvest/give-back rule live; Will manages by hand.** BRENT thesis (Hormuz-gap entry) |
| VLO | Stock | 1 | $412.00 | $422.605 | $422.60 | +$10.60 / +2.57% | Today +$3.38. Bought 9/18 @ $412.00 (fill TIME not shown — D-55). **Holding confirmed by Will 2026-10-07: “Yes, still one share”** (operator statement; current broker mark separately stamped `[10/7 rcv]`). WQ-213: 1 of 3; **the remaining 2 sh STAND DOWN** under `PROME/GATES.tsv` GATE-TERRY-VLO-SCALE, TERMINAL on the 9/25 F1 fire (TERRY 4ad672c43; optional CME source-① override remains as written). **Exit rule on the held share: `GATE-TERRY-VLO-HELD-01` REGISTERED 9/28 18:36 ET (WQ-330, Will "both"): Nov crack settlement < $90.16 ⇒ sell rec (< $95 notice); signed US distillate export-restriction text at primary ⇒ SELL at the next regular session (Will may act without the desk; TERRY recs if he has not); A: TERRY grades, Will executes; not adjudicated here (rule 7)** — **WQ-386 approved 10/7: Nov through 10/14; Dec HOZ26×42−CLZ26 from 10/15 through 11/19, no roll suppression; review 11/18; prior exits remain owed; B1 unchanged.** Exact amendment: `PROME/proposals/2026-10-07_VLO-december-management-RULED.md`. The gate reads the crack and the text, not the share's mark |
| APD | Stock | 2 | $294.79 | $280.255 | $560.51 | −$29.06 / −4.93% | Today −$1.49. Historical 10/1 "D" badge / $1.81 reference-price adjustment remains unverified; no dividend Activity supplied. Current capture does not establish that badge. Thesis tag unassigned since 7/30 |
| TBT | Stock | 10 | $34.65 | $42.855 | $428.55 | +$82.09 / +23.69% | Today +$0.95. Duration-short leg (BOND/TERRY). **WQ-357 LATER 10/3: HELD on path C while BOND researches; 10/14 decision clock remains; no exit order inferred.** |

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

*No live event-box rows — the VIX $20C/$25C spread (CLOSED 2026-07-30, realized −$111.60) and the five Aug-21-2026 EXPIRED rows (realized −$2,816.72 total) are terminal → rotation records.*

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, owned by no agent — recorded so it is not invisible. **Rail = Will's standing practice, SELL-OR-ROLL before expiry** (`USER.md`, 9/30 19:03 ET). Existing card `MGMT-USO150C-OCT09` retains its Fri 10/09 15:00 ET hard stop; **no card/time registered for the NEW QQQ Oct-09 755P or either Oct-15 QQQ line.** WQ-347's Oct-01 four were ROLLED on Will's 10/1 Deck word; fills still unbooked (D-71). USO 1 of 2 sold 10/1 @ $3.92 ⇒ +$91.67 (rotation 10/01 chunk C). Holdings-only evidence does not establish new roll linkage.

| Ticker | Strike | Expiry | Qty | Cost | Mark 10/7 rcv | Value | P&L | Note |
|--------|--------|--------|-----|------|---------------|-------|-----|------|
| QQQ | $755P | Oct-09-2026 | 2 | $2.39 | $2.24 | $448.00 | −$29.33 / −6.15% | `[10/7 rcv]`; **NEW versus 10/1 mirror**, basis $477.33; Today +$0.00. Entry date/price/time, approval and working orders UNKNOWN. **EXPIRES FRI 10/09; 2 calendar DTE from 10/7. Sell-or-roll before expiry; no new 15:00 card deadline.** |
| USO | $150C | Oct-09-2026 | 1 | $3.00 | $0.26 | $26.00 | −$273.66 / −91.33% | `[10/7 rcv]`; MARK ONLY; basis $299.66. Today −$48.00. **WQ-366 DECLINE 10/3: early sale declined; hold to Fri 10/09 15:00 ET hard stop** (`MGMT-USO150C-OCT09`). USO stock last $143.30 in the same intraday view: $6.70 below strike. $0.26 is last, NOT an executable bid. No price harvest gate; not the 37-share line. 2 calendar DTE from 10/7; working order UNKNOWN |
| QQQ | $745P | Oct-15-2026 | 2 | $2.84 | $2.64 | $528.00 | −$39.33 / −6.94% | `[10/7 rcv]`; **NEW versus 10/1 mirror**, basis $567.33; Today −$39.33. Entry date/price/time, approval and working orders UNKNOWN. **EXPIRES THU 10/15; 8 calendar DTE from 10/7. Sell-or-roll before expiry; contract-specific card unrecorded.** |
| QQQ | $740P | Oct-15-2026 | 4 | $5.31 | $1.79 | $716.00 | −$1,406.65 / −66.27% | `[10/7 rcv]`; **NEW versus 10/1 mirror**, basis $2,122.65; Today −$24.00. Entry date/price/time, approval and working orders UNKNOWN. **EXPIRES THU 10/15; 8 calendar DTE from 10/7. Sell-or-roll before expiry; contract-specific card unrecorded.** |

*GONE from this Fidelity view: QQQ $740P Oct-02 ×4 (prior basis $890.65) and QQQ $735P Oct-05 ×5 (prior basis $1,368.32). Past expiry; removed from live tables. Sold / rolled / liquidated / expired, proceeds and realized results UNKNOWN — D-72; do not book as worthless. Their old cards do not govern the new contracts.*

## Fidelity — Thesis Puts

*Instrument grouping is navigation, not approval: the NEW Fidelity WAL/OZK rows below are Will-direct holdings; thesis/desk ownership and management approval are NOT established by the image.*

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

*TLT $77P Sep-30 ×15 (TRY-FIRE-004's last lot): SOLD TO CLOSE 9/30 ⇒ −$154.64; no replacement TLT line; detail → rotation 10/01 chunk D.*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $82P | Oct-16-2026 | 1 | $1.68 | $4.70 | $470.00 | +$302.33 / +180.31% (today −$6.00) `[10/7 rcv]`. MARK ONLY; basis $167.67. 9/28: sold 1 of 2 @ $3.60 ⇒ +$191.66. **WQ-357 LATER 10/3 selects path C: HELD to 10/14 while BOND researches.** Research delivered 10/5 (`ff0992bf1`), not a new trade ruling. `MGMT-TLT82P-OCT16` (×2 original, ×1 remaining) / WQ-302: **Wed 10/14 close** clock remains; no undecided A/B/C choice asserted here. 2.80× basis is a last-mark multiple, not a price trigger; nothing adjudicated. ITM expiry handling in the IRA UNOBSERVED (D-60). 9 calendar DTE from 10/7 |

### KRE — regional banks (REGINALD)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
*All three rows `[10/7 rcv]` (capture 2026-10-07 intraday, time UNKNOWN). KRE $60P Sep-30 ×2 sold 9/30 @ $0.01 ⇒ −$451.48 (leg 1 of the roll into the Dec-31 65P; detail + the D-67 mark note → rotation 10/01 chunk D). Rail on the 65P: *"hard stop Thu 12/31 15:00 ET"* (`MGMT-KRE65P-DEC31`, `5ce609f80`).*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $60P | Dec-18-2026 | 2 | $2.57 | $0.65 | $130.00 | −$383.34 / −74.68% (today +$30.00). MARK ONLY; basis $513.34. 72 calendar DTE from 10/7 |
| $60P | Dec-18-2026 | 3 (M) | $2.93 | $0.65 | $195.00 | −$683.02 / −77.80% (today +$45.00) — multi-lot marker; basis $878.02; **five** Dec-18 KRE 60P across two lots. MARK ONLY. 72 calendar DTE from 10/7 |
| $65P | Dec-31-2026 | 2 | $1.69 | $1.41 | $282.00 | −$55.33 / −16.41% (today +$28.00) — MARK ONLY; basis $337.33. Bought 9/30 ×2 @ $1.68 (roll leg 2). Will's own add; `MGMT-KRE65P-DEC31` (`5ce609f80`): hard stop Thu 12/31 15:00 ET, not a price gate. 85 calendar DTE from 10/7 |

### WAL (REGINALD) — Sep-18 pair EXPIRED

*$70P + $67.5P Sep-18 ×1 each: **EXPIRED as of 9/18, broker-confirmed** (ledger rows posted 9/21) ⇒ realized **−$768.67 and −$750.67 = −$1,519.34** (full basis) — the WQ-168 ①② LAPSE as ruled. Rows → rotation record. Duration roll = the Robinhood WAL Dec-18 $70P ×1 below. The RH WAL $77.5P Aug-21 sale: P&L UNRECORDED — D-18.*

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18-2026 | 1 | $11.85 | $1.25 | $125.00 | −$1,059.67 / −89.45% | `[10/7 rcv]`; basis $1,184.67; Today −$10.00. MARK ONLY; BROCK thesis vehicle. Will ruled HOLD 2026-08-13 (`PROME/proposals/2026-08-13_private-credit-batch-RULED.md` §②; vehicle-mismatch flag live). 72 calendar DTE from 10/7 |
| HBAN | $16P | Oct-16-2026 | 2 | $0.96 | $0.85 | $170.00 | −$21.34 / −11.16% | `[10/7 rcv]`; basis $191.34; Today +$6.00. MARK ONLY. The 7/18 ride-to-expiry premise failed per TERRY 9/26; `MGMT-HBAN16P-OCT16` / WQ-302 re-rule due **Wed 10/14**. Current moneyness not verified from this image; no live underlying quote supplied. 9 calendar DTE from 10/7 |
| OZK | $40P | Nov-20-2026 | 4 | $0.81 | $0.65 | $260.00 | −$62.66 / −19.42% | `[10/7 rcv]`; basis $322.66; Today −$62.66. **NEW versus 10/1 mirror; Will-direct.** Entry date/fill/time, thesis/desk ownership and management approval UNRECORDED; holdings do not autoapprove research or a trade. Sell-or-roll before expiry; no contract-specific card recorded. 44 calendar DTE from 10/7 |
| WAL | $65P | Dec-18-2026 | 4 | $1.71 | $1.60 | $640.00 | −$42.65 / −6.25% | `[10/7 rcv]`; basis $682.65; Today −$42.65. **NEW versus 10/1 mirror; Will-direct.** Entry date/fill/time, thesis/desk ownership and management approval UNRECORDED; holdings do not autoapprove research or a trade. Sell-or-roll before expiry; no contract-specific card recorded. Distinct from Robinhood WAL Dec-18 $70P ×1. 72 calendar DTE from 10/7 |


## Robinhood — satellite account (Individual)

*All holdings/figures below retained from the 9/29 source; carried DTE annotations are historical, not a current freshness assertion.*

> ⚠️ **NOT CAPTURED IN THIS 10/7 RECEIPT (nor 9/30 or 10/1) — every cell below is the 9/29 card, unverified today.** **Home card 9/29 intraday: account $295.15 (Today +$35.00 / +13.45%), BP $8.94** `[9/29 13:4x intraday]` — was $228.15 / $8.94 `[RH card 9/27]` ⇒ +$67.00. Lines + BP = $290.15 ⇒ **$5.00 UNEXPLAINED (D-64)**. Per-line cost/value DERIVED from shown P/L ÷ P/L% (no Mark column ⇒ machine class `unverified` by design). **Prediction market:** Nithya Raman "Yes" 26.22 @ 58¢ ≈ $15.21 (+65.71% ⇒ cost ≈$9.18, derived — price and % identical to 9/27) — recorded, not adjudicated. **Recent activity 9/01→9/25 books the dead-by-date lines:** USO $159C Sep-11 (bought 9/10 $152, expired $0 — D-58) · QQQ $713C Sep-16 (bought 9/16 $167) + USO $165C Sep-16 (bought 9/14 $150), both expired $0 (D-57).

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **WAL $70P** | **Dec-18-2026** | 1 | **$2.20 ($220)** — bought 9/02 @ $2.20 (RH activity) ✓ | ≈$265.00 *(derived; mark ≈$2.65)* | ✅ **ON CARD 9/29 — +$45.00 / +20.45%** | TRY-WAL-ROLL70 (filled in Robinhood). Guard **`GATE-TERRY-ROLL70-EXIT`** *"WAL OFFICIAL CLOSE ≥ $81.90 on THREE CONSECUTIVE sessions"* — **0-of-3 as last recorded here** (REGINALD through 9/23, per TERRY STATUS 9/24; not re-read this pass). The option's +20.45% is not the gate — the gate reads WAL's close (rule 7). **$4.40 GTC sell order: CANCELLED / not there — Will 9/28** (`PROME/inbox/processed/2026-09-28_from-WAL_WQ-324-325-ruled-verbatim-and-4.40-GTC-cancelled.md`) ⇒ **no resting exit order; any take-profit is Will's manual act.** Time stop Fri 12/4. 78 DTE. **D-47** |
| **KRE $25P** | 1/15/2027 | 1 | $53.00 — card-derived ✓ | ≈$1.00 *(derived)* | ✅ **ON CARD 9/29 — −$52.00 / −98.11%** | Deep-OTM lottery; entry pre-7/16, never recorded — **D-54** (before the 9/01 activity view). 106 DTE |
| T | stock | 1 | — | — | ⚠️ no stocks card 9/29; no T row in RH activity 9/01→9/25 | Hypothesis: sold before 9/01, unconfirmed — **D-20**. The card no longer closes to the cent (D-64), so the 9/27 "no stock line" inference is weaker |

## Account UNATTRIBUTED — receipted fills not yet attributed to an account

*No rows. VLO ×1 (this section's only row since 9/19) moved to § Fidelity — Longs on the 9/25 ledger (D-55 account leg CLOSED). The section stays as the landing place for a receipt that names no account (the parser admits it — TERRY `cfd9b9115`).*

---

## ⚠️ Reconcile discrepancies (10/7 intraday capture, built 2026-10-07)

> Fidelity positions only; capture date October 7 confirmed by Will ("yes today"), exact time UNKNOWN. No Activity / Orders / pending-detail view; Robinhood not captured. **Broker view > Will's word > desk record; conjectures labeled; nothing resolved by invention.** DTE below is calendar days from 10/7, not a quote-time assertion. **Permanently UNKNOWN by WQ-167 (never asks):** the 9/2 USO 135C sale price. Historical list/details → `git show 5d978cf73:FORGE/STATUS.md`, rotation 10/01 chunk E.

### EXPIRING — Fri 10/09 → Fri 10/16 (sell-or-roll before expiry, `USER.md`)

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| WQ-347 | **QQQ $755P Oct-09 ×2** | 🔴 Fri 10/09; 2 DTE | NEW versus 10/1; basis $477.33; last $2.24 / $448.00 / −$29.33 `[10/7 rcv]`. Sell-or-roll before expiry; **no card or new 15:00 deadline registered** | Entry/fill date, roll linkage, working order UNKNOWN; last is not bid; underlying QQQ quote absent | **Will** (order); TERRY (card); PROME records |
| WQ-366 | **USO $150C Oct-09 ×1** | 🔴 Fri 10/09 15:00 ET; 2 DTE | MARK ONLY; basis $299.66; last $0.26 / $26.00 / −$273.66 `[10/7 rcv]`. **Will DECLINED early sale 10/3: hold to the existing hard stop** (`MGMT-USO150C-OCT09`; DOCKET L605). USO $143.30 in capture, $6.70 below strike. No harvest gate | Working order UNKNOWN; no executable bid shown | **Will** (order); TERRY (existing card) |
| **D-60** | **Fidelity expiry handling — ITM leg UNOBSERVED** | 🔴 relevant before 10/09, then 10/15–16 | Prior OTM liquidation observations ×4; three other lines EXPIRED without cash rows (prior detail in git). Oct-01 ×4 were **ROLLED on Will's confirmed word** (WQ-347); do not count them as a fifth broker-liquidation observation. IRA holds no QQQ or TLT shares | ITM long-option handling and what decides LIQUIDATE versus EXPIRED remain UNKNOWN. Conditional exercise: QQQ Oct-09 ×2 = 200 shares at $755 ($151,000); Oct-15 ×2 at $745 ($149,000) plus ×4 at $740 ($296,000); these are contract mechanics, not a claim of actual exercise | **Will** — Fidelity's handling / Activity |
| WQ-302 / WQ-357 | **TLT $82P Oct-16 ×1 + HBAN $16P Oct-16 ×2** | 🟠 Wed 10/14 management clock; 9 DTE | TLT $470.00 / +180.31%; HBAN $170.00 / −11.16% `[10/7 rcv]`. **TLT path C chosen by Will's LATER 10/3**, held to 10/14 during research; BOND research delivered 10/5, not a new trade ruling. HBAN re-rule remains due 10/14. Neither percentage is a fired price trigger | Working orders / current underlying moneyness UNKNOWN in this capture | **Will**; TERRY cards / BOND research |
| WQ-347 | **QQQ $745P Oct-15 ×2 + $740P Oct-15 ×4** | 🟠 Thu 10/15; 8 DTE | Both NEW versus 10/1; bases $567.33 and $2,122.65; last values $528.00 and $716.00 `[10/7 rcv]`. Sell-or-roll before expiry; no contract-specific time card recorded | Entry dates / fills / new roll linkage / working orders UNKNOWN; Today = total on the 745P is consistent with same-session entry, not proof without Activity | **Will**; TERRY card; PROME records |

### Will supplies / PROME re-reads — facts owed

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-72** | **Old QQQ Oct-02 $740P ×4 + Oct-05 $735P ×5 — GONE** | 🟡 record / realized | Both absent `[10/7 rcv]`, past expiry; prior bases $890.65 + $1,368.32 = $2,258.97. Removed from live tables; **no realized result booked**. Their cards do not govern the new identities | Sold / rolled / liquidated / expired, proceeds and realized results UNKNOWN; not booked worthless from absence | **Will** — Activity 9/29→10/7 (WQ-347) |
| **D-73** | **Five NEW identities — fills / pending bridge unshown** | 🟡 record / cash | QQQ 755P Oct-09 ×2, 745P Oct-15 ×2, 740P Oct-15 ×4, WAL 65P Dec-18 ×4, OZK 40P Nov-20 ×4; Σ bases $4,172.62. Σ basis $18,310.25 + $4,172.62 − $2,258.97 = $20,223.90. Cash −$1,153.78 to $12,993.82; pending −$2,949.74 to −$1,572.64 versus 10/1 | Entry dates / actual fills / roll relationships / intervening cash flows / pending composition UNKNOWN. Snapshot total −$4,178.77 is **not a realized trading-loss figure** | **Will** — same Activity + pending detail |
| **D-71** (narrowed) | **Oct-01 QQQ 740P ×4 — ROLL confirmed, exact fill unbooked** | 🟡 record | Will's Deck tap 10/1 17:04 ET: "this has been complete already - I rolled them." WQ-347 identifies the four Oct-01 contracts; it does not answer later Oct-02 disposition. Prior basis $770.66 | Prior pending inference net +$22.75 ⇒ ≈ −$747.91 remains **PROME-supplied, not broker-verified**, not booked. Exact exit prices/proceeds/fees/realized UNKNOWN | **Will** — Activity 10/1 |
| **D-70** | **Management mappings / cards follow-through** | 🟡 re-review / consumption | Any byte change to this file invalidates mappings pinned to its old `source_sha256` until re-review. **PROME reports mappings UPDATED for Oct-01/02/05 QQQ, USO Oct-09 and all five NEW identities; remaining old FORGE hash pins intentionally withheld pending review**; ANVIL edits no TSV or owner card. Existing exact VLO amendment retained | Completion/consumption remains PROME's verification; do not treat holdings as a card approval | **PROME** (mapping re-review); **TERRY** (cards at authorized touch) |
| **D-74** | **New Fidelity bank puts — ownership / management unrecorded** | 🟡 record | WAL Dec-18 65P ×4, basis $682.65, $640.00; OZK Nov-20 40P ×4, basis $322.66, $260.00 `[10/7 rcv]`. WAL differs from RH Dec-18 70P ×1 | Thesis/desk owner/approval not established by holdings; no autoapproved research or trade | **PROME** routes scope; **Will** / TERRY management |
| **D-69** | **Prior cash +$53.54 above 9/30-implied** | 🟡 carried | Expected $18,102.04 − $4,007.98 = $14,094.06 versus both 10/1 views $14,147.60 | September money-market dividend — conjecture only, separate from D-63; current cash does not close this gap | **Will** — same Activity 9/29→10/7 |
| **D-66** | **Fill TIMES / new fill details unshown** | 🟡 carried | 9/30: 9 fills/5 cancels; 10/1 midday: 4 fills/1 cancel without times. Later Oct-01 exit, Oct-02 entry and all new/gone identities lack Activity fills | Sequence from row order only; no time invented | **Will** — order detail / Activity |
| **D-62** | **Fidelity ledger — $0.45 break in the broker's own running balance** | 🟡 carried | 17,740.43 + 359.34 (TLT 82P, 9/28) = 18,099.77 vs 18,099.32 shown; 33 of 34 links hold | A fee/adjustment without its own row, OR a transcription digit misread | **PROME** re-reads the 9/29 image cell |
| **D-63** | **Cash bridge +$2.27 unattributed** | 🟡 carried | 9/25-close cash + pending + the 9/28 rows = $18,099.77 vs cash $18,102.04; the Sep-30 Activity showed no dividend / interest row; 9/29 rows (if any) not captured | Money-market dividend, the APD dividend, or interest — ANVIL picks none (see D-69) | **Will** — Activity 9/29 (low) |
| **D-64** | **Robinhood card — $5.00 unexplained** | 🟡 carried | $290.15 of lines + BP vs $295.15 shown `[9/29 13:4x intraday]`; not re-captured in the 10/7 receipt | BP ≠ cash, a line valued off another price, or a line not on the card | **Will** — RH cash/account detail |
| **D-65** | **RH 9/14–9/15 put/call labels do not pair** | 🟡 no live position | 707 "Put" bought → 707 "Call" sold; 708 "Call" bought → 708 "Put" expiration | Hypothesis: the 9/15 "Call" rows are Puts ⇒ 707P +$104, 708P −$41 — NOT booked | **PROME** — re-read the image |
| **D-61** (narrowed) | **9/28 fills — times for QQQ 730P ×1 and TLT 77P ×5; TLT 77P $0.02 receipt-vs-ledger** | 🟡 | Ledger Σ $28.43 vs receipt $28.45; ledger used | Receipt digit or transcription — UNKNOWN | Will (order detail), low |
| **D-59** (narrowed) | **RH buying power 9/16 → 9/27: −$0.48 residual** | 🟡 | −$119.95 from the activity vs BP −$120.43 | Regulatory fees on four sells + rounding — labeled | Will, low |
| **D-45** (residual) | **+$43.81 before the 9/01 Activity view** | 🟡 | 8/28 cash + pending $14,323.25 vs derived 9/01 opening $14,367.06 | 8/31 activity or interest (an August month-end credit would match D-69's form — conjecture) | **Will** — Activity 8/28–8/31 |
| **D-55** (residual) | **VLO fill TIME** | 🟡 | Fidelity, 9/18 | — | Will, low |
| **D-28** | **RH QQQ $715P ×1 — expired 8/31, outcome UNRECORDED** | 🟡 carried | Cost ≈$193.24; before the 9/01 view | Expired OTM / sold / exercised — none verified | RH history before 9/01 |
| **D-54** | **RH KRE $25P Jan-15-2027 — entry never recorded** | 🟡 carried | Cost $53.00 derived; on the mirror since 7/16 | Entry pre-7/16 ≈$0.53 — a derivation | Will |
| **D-18** | **RH WAL $77.5P Aug-21 — sale CONFIRMED 8/18, P&L UNRECORDED** | 🟡 carried | Existence closed 8/18 | Do not book at $0 | Will (not urgent) |
| **D-20** | **RH T share — absent; event contracts** | 🟡 carried | No stocks card; no T row 9/01→9/25 | Sold before 9/01, unconfirmed | Will — full RH view |
| **D-37** | **RH ≈$360 inflow (8/14→8/28) + "13 days left" banner** | 🟡 carried | Arithmetic recorded 8/29 | Deposit/transfer; banner referent unknown | Will (one line) |
| **D-17** | **STNG — in no capture, nowhere in FORGE** | 🟡 carried | Absent since 8/2 | Recalled / closed pre-7/30 / a third account | Will — one line |
| **D-1** | **AAPL 5-sh sale pre-7/30 — date + price unrecorded** | 🟡 carried | Predates the 7/30–8/28 window | ~$565 cash class | Will / an older window |

### Owner decides — ruled / gated

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-47** | **RH WAL Dec-18 $70P ×1 — `GATE-TERRY-ROLL70-EXIT`** | 🟡 stale source | ≈$265.00 derived `[9/29 13:4x intraday]`; entry 9/02 @ $2.20; 0-of-3 as last recorded, not regraded; no resting exit order (cancelled by Will 9/28); time stop 12/4 | Current existence/mark unverified today; new Fidelity WAL is a different contract/account | **Will** manual harvest; REGINALD grades / TERRY proposes |
| WQ-386 / VLO-SCALE | **VLO held share ×1 management APPROVED; 2 additional shares STOOD DOWN** | registered / scale TERMINAL | Held-share Nov through 10/14; Dec 10/15–11/19, no roll suppression; review 11/18. Prior exits owed / B1 unchanged; exact rule/ref retained in Longs. $422.605 last / $422.60 value `[10/7 rcv]` does not adjudicate crack/text gate | No buy, sale or new order inferred; optional official-CME scale override only as GATES specifies | **TERRY** grades; **Will** executes; PROME integrates |
| WQ-200 | **USO 37 sh — no management rule live** | ⚪ | Card DECLINED 9/10; $143.30 last / $5,302.10 value `[10/7 rcv]` informational | No inherited option rule on stock | **Will** hand |
| — | **APD thesis tag / historical "D" badge** | ⚪ | Tag unassigned since 7/30; historical 10/1 last − change reference $276.42 versus 9/30 $278.23 ($1.81 gap) remains an unverified adjustment; current badge not established | Ex-dividend adjustment conjectured; no dividend Activity / amount / pay date shown | **PROME / Will** |

### This pass — no new fill or realized result booked

- **5 NEW versus the mirror:** three QQQ identities + Fidelity WAL 65P ×4 + OZK 40P ×4; total new basis $4,172.62. **2 GONE:** QQQ Oct-02 740P ×4 and Oct-05 735P ×5; disposition UNKNOWN (D-72).
- **13 MARK ONLY:** all six Fidelity stocks; TLT; HBAN; APO; KRE 65P and both KRE 60P lots; matched quantities/bases unchanged. Σ 18 positions $20,477.09; basis $20,223.90; cash/pending/account arithmetic ties.
- D-71 narrowed by Will's existing Oct-01 roll word. No historical cash/fill gap closed by this holdings-only view. Robinhood remains 9/29, unverified today.

---

## Immediate Actions (10/7 intraday reconcile state)

| Item | State | Owner |
|---|---|---|
| 🔴 **QQQ Oct-09 755P ×2** — sell-or-roll before Fri 10/09 expiry; no new 15:00 card time | 2 calendar DTE | **Will** / TERRY card |
| 🔴 **USO Oct-09 150C ×1** — Will declined early sale; existing Fri 10/09 15:00 ET hard stop retained (WQ-366 / L605) | existing clock | **Will** / TERRY |
| 🟠 **TLT 82P ×1 path C / HBAN 16P ×2**, Wed 10/14 management clock; **QQQ Oct-15 745P ×2 + 740P ×4**, Thu expiry | dated | **Will** / TERRY |
| 🟡 **D-72 / D-73 / D-71 / D-69 / D-63 / D-66** — one Fidelity Activity 9/29→10/7 + pending detail books old exits, new entries and cash | one view | **Will** |
| 🟡 **D-60** — IRA ITM option-expiry handling still unobserved | broker answer | **Will** |
| 🟡 **D-70 / D-74** — named mappings updated; remaining old hashes withheld; owner card consumption / new bank ownership unrecorded; no autoapproval | owner integration | **PROME / TERRY** |
| 🟡 **D-62 / D-65** — historical image re-reads; **Robinhood** D-64 / D-28 / D-54 / D-18 / D-20 / D-37, account not captured | carried | **PROME / Will** |
| 🟡 Older Activity / detail: D-61 / D-59 / D-45 / D-55 / D-17 / D-1 | carried | **Will** |

---

*History → `_archive/JOURNAL.md` | Prior reconciles in git history + `_archive/`; immediately prior whole mirror = `git show 5d978cf73:FORGE/STATUS.md` | Full-portfolio Feb snapshot → `PORTFOLIO.md` (**FROZEN/superseded, historical only — never cite as live**) | Position truth = Will/broker direct (off-repo) | Marks-of-record transcription → `PROME/data/2026-10-07_broker-capture-TRANSCRIPTION.md` (Fidelity October 7 intraday, date confirmed by Will, exact time UNKNOWN); prior `…2026-10-01b_…` (post-close) · `…2026-10-01_…` (intraday + Pending list) · `…_2026-09-30_…` · `…_2026-09-29_…` (RH rows' source)*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumers: `AGENTS/TERRY/scripts/positions_from_forge.py` (sections `^## (Fidelity|Robinhood)` + `^## Account <NAME>`; table headers by prefix; cell text — emphasis and strikethrough visible) · `PROME/tools/desk_attention.py` `holdings()` (same sections; `Qty` + `Ticker|Strike|Position` headers; expiry year from `**Updated:**`) · `PROME/tools/will_brief.py` `parse_money()` (header before the first `## `: `account total:**`, `money market):** $X (Y%)`, `**Updated:** YYYY-MM-DD`, `marks = [Fri ]YYYY-MM-DD`) · `FORGE/position_management.tsv` `source_sha256` (any byte change here withholds every mapping sourced to this file until PROME re-reviews) · `AGENTS/BRENT/scripts/pending_receipts.py` (text-level closure candidates). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself here in the same commit that starts parsing. *(Pass notes 9/27 → 10/1 intraday → rotation 10/01 chunk F. Conventions they set, still binding: the header money line keeps the shape `will_brief.py` reads; option expiries carry the year; the `Mark <m/d>` header is prefix-bound; terminal records live in italic lines, which no parser reads as rows.)* *(10/7 pass: same sections, table header prefixes and row conventions; `Mark 10/7 rcv` binds by prefix; explicit option years retained; 18 Fidelity rows plus stale Robinhood rows. Five new rows and two removed past-expiry identities do not change parser shape. `**Updated:** 2026-10-07`, `marks = 2026-10-07` are Will-confirmed October 7 intraday capture date; exact time UNKNOWN. Remaining semantic consumer limitations: desk_attention's hard-coded Robinhood observation is stale; date-only consumers cannot show the unknown clock. Source hashes still require PROME re-review.)*
