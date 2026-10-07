# FORGE — Trading Operations

Dashboard management mapping → [position_management.tsv](position_management.tsv); maintenance contract → [dashboard notes](DASHBOARD.md). Holdings remain in this file; approval, order and fill evidence are separate. A changed evidence source invalidates its management mapping until reviewed.

> ✅ **2026-10-01 (Thu) — RECONCILE BY ANVIL to Will's END-OF-DAY capture (posted 16:15 ET): every Fidelity mark `[10/1 pc]` = `[10/1 post-close capture, clock not shown]` — whether the option marks are final closing marks is NOT shown.** Source `PROME/data/2026-10-01b_broker-capture-TRANSCRIPTION.md` (PROME's transcription of ONE screenshot: **Fidelity positions, 10/1 session, "Today" populated**; NO Activity / Pending / Orders view) + Will's word *"here is how we are looking end of day"*. ANVIL re-verified from the table (no image access): value = last × qty (×100) ✓ and G/L = value − basis ✓ on 15 of 15 rows; Σ positions $20,552.34 + cash $14,147.60 + pending +$1,377.10 = **$36,077.04 to the cent** ✓; Σ Today −$368.56 ✓; Σ G/L +$2,242.09 ✓ on Σ basis $18,310.25 (= the intraday mirror's $18,190.26 − $770.66 + $890.65 ✓). **Vs the 10/1 intraday mirror (`dac72b4ae`): 1 GONE (QQQ $740P Oct-01 ×4 — disposition UNBOOKED / INFERRED, D-71) · 1 NEW (QQQ $740P Oct-02 ×4, basis $890.65, EXPIRES FRI 10/02) · 0 QTY CHANGE · 14 Fidelity rows MARK ONLY** (quantities and bases identical to the cent). Robinhood NOT captured — its 9/29 card stands. The superseded intraday header, settled row notes, discrepancy list and footer pass-notes → `_archive/STATUS_ROTATION_2026-10-01.md` (verbatim chunks A–F; whole file = `git show dac72b4ae:FORGE/STATUS.md`).
>
> ⚠️ **ACCOUNT SCOPE — Fidelity: ONE account; the capture's header shows "Traditional IRA", number redacted by Will ⇒ *****1326 INFERRED by position-set match. Robinhood Individual: NOT in this capture — rows carried from the 9/29 card, unverified today.** Rows absent from a view are retained and flagged; a dated contract past its own expiry leaves the live tables, its disposition UNBOOKED unless a broker row shows it.
>
> **Updated:** 2026-10-01 = last broker-view reconcile (the date token machine consumers read as the export vintage — see footer) · marks = 2026-10-01 POST-CLOSE capture (all Fidelity lines `[10/1 pc]`) · **Fidelity cash (money market):** $14,147.60 (39.22%) + **Pending activity +$1,377.10** (was +$2,245.00 intraday ⇒ −$867.90, composition NOT SHOWN — D-71) — cash unchanged since the intraday view, still +$53.54 above the 9/30-implied figure (D-69) · **Fidelity account total:** $36,077.04 (Today −$368.56 / −1.01%; open G/L +$2,242.09 / +12.25%) — was $37,727.55 `[10/1 intraday]` ⇒ −$1,650.51 (= positions −$782.61 + pending −$867.90 + cash $0.00; intraday vs post-close) and $36,384.93 `[9/30 post-close]` ⇒ −$307.89 · **Realized 10/1:** broker-shown +$982.02 (the two midday partial sales, Pending list 12:24 ET) · **NOT broker-shown: ≈ −$747.91 on the Oct-01 $740P ×4 (PROME-supplied inference, D-71 — unbooked)** · **Robinhood:** $295.15 / BP $8.94 `[9/29 13:4x intraday]` — not re-captured. Rotations → `_archive/STATUS_ROTATION_2026-10-01.md`, `…_2026-09-29.md`, `…_2026-09-27.md`, `…_2026-09-20.md`, `…_2026-09-10.md`, `_archive/RECONCILE_2026-08-29_RECORD.md`.

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (7/18 re-base + amendment #1 = current). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All cells `[10/1 pc]`. All six MARK ONLY vs the intraday mirror. Settled fill notes (AAPL / GLD / TBT 9/15, VLO 9/18) → rotation 10/01 chunk B. % cells are the broker's as shown (5 rows sit 0.01 from value ÷ basis — a display trait also present on prior captures).*

| Ticker | Type | Qty | Cost | Mark 10/1 | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | 10 | $23.65 | $328.80 | $3,288.00 | +$3,051.55 / +1,290.56% | Today −$42.20. 9/15 sale of 5 sh (≈+$1,534.92, derived) in the rotation record; pre-7/30 5-sh sale = D-1 |
| GLD | Stock | 17 | $374.74 | $382.77 | $6,507.09 | +$136.59 / +2.14% | Today +$32.81. MIDAS domain; largest line |
| USO | Stock | 37 | $122.28 | $150.00 | $5,550.00 | +$1,025.73 / +22.67% | Today +$160.58. **WQ-200 DECLINED by Will 9/10 — NO harvest/give-back rule live; Will manages by hand.** BRENT thesis (Hormuz-gap entry) |
| VLO | Stock | 1 | $412.00 | $406.59 | $406.59 | −$5.41 / −1.32% | Today +$18.98. Bought 9/18 @ $412.00 (fill TIME not shown — D-55). **Holding confirmed by Will 2026-10-07: “Yes, still one share”** (operator statement, no new broker mark). WQ-213: 1 of 3; **the remaining 2 sh STAND DOWN** under `PROME/GATES.tsv` GATE-TERRY-VLO-SCALE, TERMINAL on the 9/25 F1 fire (TERRY 4ad672c43; optional CME source-① override remains as written). **Exit rule on the held share: `GATE-TERRY-VLO-HELD-01` REGISTERED 9/28 18:36 ET (WQ-330, Will "both"): Nov crack settlement < $90.16 ⇒ sell rec (< $95 notice); signed US distillate export-restriction text at primary ⇒ SELL at the next regular session (Will may act without the desk; TERRY recs if he has not); A: TERRY grades, Will executes; not adjudicated here (rule 7)** — **WQ-386 approved 10/7: Nov through 10/14; Dec HOZ26×42−CLZ26 from 10/15 through 11/19, no roll suppression; review 11/18; prior exits remain owed; B1 unchanged.** Exact amendment: `PROME/proposals/2026-10-07_VLO-december-management-RULED.md`. The gate reads the crack and the text, not the share's mark |
| APD | Stock | 2 | $294.79 | $272.63 | $545.26 | −$44.31 / −7.52% | Today −$7.58 (−$3.79/sh). "D" badge still shown. Last − chg = $276.42, the same reference as intraday, NOT the mirror's $278.23 `[9/30c]` — an ex-dividend adjustment would produce the $1.81/sh gap (INFERRED; no dividend row, amount and pay date UNKNOWN). Thesis tag unassigned since 7/30 |
| TBT | Stock | 10 | $34.65 | $42.24 | $422.40 | +$75.94 / +21.91% | Today −$2.50. Duration-short leg (BOND/TERRY); no management rule |

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

*No live event-box rows — the VIX $20C/$25C spread (CLOSED 2026-07-30, realized −$111.60) and the five Aug-21-2026 EXPIRED rows (realized −$2,816.72 total) are terminal → rotation records.*

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, owned by no agent — recorded so it is not invisible. **Rail = Will's standing practice, SELL-OR-ROLL before expiry** (`USER.md`, 9/30 19:03 ET — a pre-expiry sale is not a deviation). TERRY management cards: `MGMT-QQQ735P-OCT05` + `MGMT-USO150C-OCT09` (`5ce609f80`); **the Oct-02 $740P ×4 has NO card of its own.** **QQQ $740P Oct-01 (bought 9/30 ×9 @ $1.92, −$1,733.97): 5 SOLD TO CLOSE midday 10/1 for +$1,853.66 ⇒ +$890.35 (broker Pending list; fills → rotation 10/01 chunk C); the last ×4 (basis $770.66) are ABSENT from the end-of-day view and past their expiry — row removed, disposition UNBOOKED: no broker row shows it; PROME infers net +$22.75 ⇒ ≈ −$747.91 (D-71).** USO $150C: 1 of 2 sold 10/1 @ $3.92 ⇒ +$91.67 (chunk C). Older terminal records → `git show 33bc8c293:FORGE/STATUS.md`; tickets 9/04–9/25 → `_archive/STATUS_ROTATION_2026-09-27.md` § Ticket record.

| Ticker | Strike | Expiry | Qty | Cost | Mark 10/1 | Value | P&L | Note |
|--------|--------|--------|-----|------|-----------|-------|-----|------|
| QQQ | $740P | Oct-02-2026 | 4 | $2.23 | $2.32 | $928.00 | +$37.35 / +4.19% | `[10/1 pc]`; **NEW 10/1**, broker basis $890.65. Today's gain = Total gain ⇒ opened today (read off the shown cells); fill price, time and order NOT SHOWN (D-66). **⚠️ EXPIRES FRI 10/02 — 0 DTE tomorrow.** QQQ ≈$742.03 `[vendor 16:06 ET, PROME-supplied, not broker-verified]` ⇒ ≈$2.03 OTM. If ITM at expiry: exercise of ×4 = a sale of 400 QQQ at $740 ($296,000) the IRA does not hold — handling UNOBSERVED (D-60). Working order: UNKNOWN. No TERRY card on this line; the Oct-01 card's roll table rated an Oct-02 roll *"⛔ The costliest time per session. It puts this same question back on the card tomorrow (rule #16)"* (`36959ad0f`, on the Oct-01 line — recorded, not adjudicated). +4.19% is a mark; no price gate exists on this line (rule 7) |
| QQQ | $735P | Oct-05-2026 | 5 | $2.74 | $2.27 | $1,135.00 | −$233.32 / −17.06% | `[10/1 pc]`; today −$650.00 (was +$531.68 at the intraday mark $3.80). MARK ONLY. Bought 9/30 ×5 @ $2.73 limit, −$1,368.32. ≈$7.03 OTM at QQQ ≈$742.03 (16:06, PROME-supplied). Card *"SELL-OR-ROLL BY MON 10/05 15:00 ET — no action owed today"*, re-read Monday morning — a time rail, not a price trigger. 4 DTE (Mon 10/05) |
| USO | $150C | Oct-09-2026 | 1 | $3.00 | $4.15 | $415.00 | +$115.34 / +38.49% | `[10/1 pc]`; today +$125.00. MARK ONLY vs intraday (×1, basis $299.66). USO $150.00 `[10/1 pc]` ⇒ AT the strike. Rail *"Hard stop Fri 10/09 15:00 ET"* (TERRY notes); no harvest rule registered — the notes' *"any Fidelity bid ≥ $5.98"* is a suggested form, not a gate, and $4.15 is a last, not a bid (rule 7). ⚠️ Not the stock line (USO 37 sh, § Longs) — WQ-297 A flag (PROME), not adjudicated. 8 DTE (Fri 10/09) |

## Fidelity — Thesis Puts

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

*TLT $77P Sep-30 ×15 (TRY-FIRE-004's last lot): SOLD TO CLOSE 9/30 ⇒ −$154.64; no replacement TLT line; detail → rotation 10/01 chunk D.*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $82P | Oct-16-2026 | 1 | $1.68 | $4.25 | $425.00 | +$257.33 / +153.47% (today −$35) `[10/1 pc]`. MARK ONLY; broker basis $167.67. 9/28: sold 1 of 2 @ $3.60 ⇒ +$191.66. **Card `MGMT-TLT82P-OCT16`** (TERRY `40e12ee0a`, built on ×2 — WQ-292 / WQ-302); Will's A/B/C by **Wed 10/14 close** now concerns ×1. ⚠️ +153.47% (2.53× basis) is a mark — the card's options are a CHOICE (A harvest · B hold to expiry · C hold then sell by 10/14), not a price trigger; nothing fired (rule 7). ITM-expiry handling in the IRA = named UNKNOWN on the card, UNOBSERVED in the ledger (D-60). 15 DTE |

### KRE — regional banks (REGINALD)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
*All three rows `[10/1 pc]`. KRE $60P Sep-30 ×2 sold 9/30 @ $0.01 ⇒ −$451.48 (leg 1 of the roll into the Dec-31 65P; detail + the D-67 mark note → rotation 10/01 chunk D). Rail on the 65P: *"hard stop Thu 12/31 15:00 ET"* (`MGMT-KRE65P-DEC31`, `5ce609f80`).*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $60P | Dec-18-2026 | 2 | $2.57 | $0.61 | $122.00 | −$391.34 / −76.24% (today −$4). MARK ONLY. 78 DTE |
| $60P | Dec-18-2026 | 3 (M) | $2.93 | $0.61 | $183.00 | −$695.02 / −79.16% (today −$6) — Fidelity multi-lot marker; **five** Dec-18 KRE 60P across the two lots. MARK ONLY. 78 DTE |
| $65P | Dec-31-2026 | 2 | $1.69 | $1.60 | $320.00 | −$17.33 / −5.14% (today −$16) — MARK ONLY. Bought 9/30 ×2 @ $1.68, −$337.33 (roll leg 2). Will's own add; management notes `MGMT-KRE65P-DEC31` (`5ce609f80`). 91 DTE |

### WAL (REGINALD) — Sep-18 pair EXPIRED

*$70P + $67.5P Sep-18 ×1 each: **EXPIRED as of 9/18, broker-confirmed** (ledger rows posted 9/21) ⇒ realized **−$768.67 and −$750.67 = −$1,519.34** (full basis) — the WQ-168 ①② LAPSE as ruled. Rows → rotation record. Duration roll = the Robinhood WAL Dec-18 $70P ×1 below. The RH WAL $77.5P Aug-21 sale: P&L UNRECORDED — D-18.*

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18-2026 | 1 | $11.85 | $1.25 | $125.00 | −$1,059.67 / −89.45% | `[10/1 pc]` MARK ONLY. BROCK thesis vehicle; today −$10; 78 DTE. Will ruled HOLD 2026-08-13 (`PROME/proposals/2026-08-13_private-credit-batch-RULED.md` §②; BROCK owner; vehicle-mismatch flag live) |
| HBAN | $16P | Oct-16-2026 | 2 | $0.96 | $0.90 | $180.00 | −$11.34 / −5.93% | `[10/1 pc]` MARK ONLY. Today +$30. ITM (TERRY 9/26). The 7/18 *"rides to expiry"* ruling stands as written but its premise failed — **card `MGMT-HBAN16P-OCT16`**, re-rule options for Will by **Wed 10/14** (WQ-302). 15 DTE |

## Robinhood — satellite account (Individual)

> ⚠️ **NOT CAPTURED 9/30 OR 10/1 — every cell below is the 9/29 card, unverified today.** **Home card 9/29 intraday: account $295.15 (Today +$35.00 / +13.45%), BP $8.94** `[9/29 13:4x intraday]` — was $228.15 / $8.94 `[RH card 9/27]` ⇒ +$67.00. Lines + BP = $290.15 ⇒ **$5.00 UNEXPLAINED (D-64)**. Per-line cost/value DERIVED from shown P/L ÷ P/L% (no Mark column ⇒ machine class `unverified` by design). **Prediction market:** Nithya Raman "Yes" 26.22 @ 58¢ ≈ $15.21 (+65.71% ⇒ cost ≈$9.18, derived — price and % identical to 9/27) — recorded, not adjudicated. **Recent activity 9/01→9/25 books the dead-by-date lines:** USO $159C Sep-11 (bought 9/10 $152, expired $0 — D-58) · QQQ $713C Sep-16 (bought 9/16 $167) + USO $165C Sep-16 (bought 9/14 $150), both expired $0 (D-57).

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **WAL $70P** | **Dec-18-2026** | 1 | **$2.20 ($220)** — bought 9/02 @ $2.20 (RH activity) ✓ | ≈$265.00 *(derived; mark ≈$2.65)* | ✅ **ON CARD 9/29 — +$45.00 / +20.45%** | TRY-WAL-ROLL70 (filled in Robinhood). Guard **`GATE-TERRY-ROLL70-EXIT`** *"WAL OFFICIAL CLOSE ≥ $81.90 on THREE CONSECUTIVE sessions"* — **0-of-3 as last recorded here** (REGINALD through 9/23, per TERRY STATUS 9/24; not re-read this pass). The option's +20.45% is not the gate — the gate reads WAL's close (rule 7). **$4.40 GTC sell order: CANCELLED / not there — Will 9/28** (`PROME/inbox/processed/2026-09-28_from-WAL_WQ-324-325-ruled-verbatim-and-4.40-GTC-cancelled.md`) ⇒ **no resting exit order; any take-profit is Will's manual act.** Time stop Fri 12/4. 78 DTE. **D-47** |
| **KRE $25P** | 1/15/2027 | 1 | $53.00 — card-derived ✓ | ≈$1.00 *(derived)* | ✅ **ON CARD 9/29 — −$52.00 / −98.11%** | Deep-OTM lottery; entry pre-7/16, never recorded — **D-54** (before the 9/01 activity view). 106 DTE |
| T | stock | 1 | — | — | ⚠️ no stocks card 9/29; no T row in RH activity 9/01→9/25 | Hypothesis: sold before 9/01, unconfirmed — **D-20**. The card no longer closes to the cent (D-64), so the 9/27 "no stock line" inference is weaker |

## Account UNATTRIBUTED — receipted fills not yet attributed to an account

*No rows. VLO ×1 (this section's only row since 9/19) moved to § Fidelity — Longs on the 9/25 ledger (D-55 account leg CLOSED). The section stays as the landing place for a receipt that names no account (the parser admits it — TERRY `cfd9b9115`).*

---

## ⚠️ Reconcile discrepancies (10/1 end-of-day reconcile, built 2026-10-01)

> Built against ONE view: the Fidelity positions, 10/1 post-close (clock not shown). No Activity / Pending / Orders view; Robinhood not captured. **Nothing resolved by invention; every conjecture labeled; broker view > Will's word > desk record; PROME-supplied items are marked so.** Ranked by decision urgency, expiring first. **Permanently UNKNOWN by WQ-167 (never asks):** the 9/2 USO 135C sale price. **One standing gap, not re-asked per row:** fill TIMES for every Fidelity ledger row (D-66). Prior list (10/1 intraday build, incl. its CLOSED list: the 10/1 sales, D-67, D-68) → rotation 10/01 chunk E.

### EXPIRING — Fri 10/02 → Fri 10/16 (every option line's rail = SELL-OR-ROLL before expiry, `USER.md` 9/30)

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| WQ-347 | **QQQ $740P Oct-02 ×4 — EXPIRES TOMORROW, Fri 10/02** | 🔴 0 DTE tomorrow | NEW on the 10/1 end-of-day view: ×4, basis $890.65, $2.32 / $928.00 / +$37.35 `[10/1 pc]`. QQQ ≈$742.03 `[vendor 16:06 ET, PROME-supplied, not broker-verified]` ⇒ ≈$2.03 OTM. If ITM at expiry, exercise of ×4 = sell 400 QQQ at $740 ($296,000); the IRA holds 0 QQQ. No TERRY card on this line; no price gate | Opened today as the roll of the Oct-01 ×4 (Today = Total gain; PROME reading — no order row seen). Basis fits 4 @ $2.22 + $2.65 fees — conjecture. Working order: NOT SHOWN | **Will** (his hand, before Fri's close per his standing practice); TERRY card = TERRY's call at its wake |
| **D-60** | **Fidelity expiry-day handling — the ITM leg is still UNOBSERVED** | 🔴 bears on the 740P ×4 Fri, then 735P Mon, 82P / HBAN 10/16 | OTM leg OBSERVED ×4 (penny "OPTION LIQUIDATION" rows on the expiry day: IWM 293P 9/04 · QQQ 716P 9/08 · QQQ 710P 9/18 · QQQ 730P Sep-25 9/25); three others EXPIRED with no cash row (QQQ 716P Sep-21; WAL 70P + 67.5P Sep-18). 9/30 added none (Will's sales). **10/1: the Oct-01 740P ×4 left on their expiry day by a route NOT SHOWN (D-71)** | If D-71 was Fidelity's liquidation it is a 5th observation of the OTM-class leg (QQQ ≈$742.03 > $740 at 16:06, PROME-supplied) — UNVERIFIED. **OPEN: (i) an ITM long option at expiry in the IRA; (ii) what decides LIQUIDATE vs EXPIRED — both UNKNOWN** | **Will** — one Fidelity question; the 10/1 Activity view answers D-71 |
| **D-71** 🆕 | **QQQ $740P Oct-01 ×4 — GONE from the view; disposition UNBOOKED** | 🔴 record; sizes the 10/1 realized figure | Row absent `[10/1 pc]`; was ×4, basis $770.66, $2.65 / $1,060.00 `[10/1 intraday]`. Pending moved +$2,245.00 → +$1,377.10 (−$867.90). No Activity / Pending view; Will's word on the capture says nothing about the roll | **PROME-SUPPLIED INFERENCE, not broker-verified:** −$867.90 = −$890.65 (the Oct-02 purchase at its basis) + $22.75 ⇒ the four left for net +$22.75 ⇒ realized ≈ −$747.91; the whole Oct-01 lot ≈ +$142.44 and the 10/1 day ≈ +$234.11 (both derived from it). **Sale by Will OR Fidelity's expiry-day liquidation: UNKNOWN.** ANVIL note: 4 lots at one price less the ≈$0.66–0.67/contract fee seen midday gives ≈$21.3 (@ $0.06) or ≈$25.3 (@ $0.07), not $22.75 ⇒ split fills, a different fee, or a pending row not shown — UNKNOWN. NOT booked as a fill | **Will** — the Fidelity Activity / Pending view for 10/1 (closes D-71; may add a D-60 observation) |
| WQ-347 | **QQQ $735P Oct-05 ×5 — expires Mon 10/05** | 🟠 2 sessions | $2.27 / $1,135.00 / −$233.32 `[10/1 pc]` (was +$531.68 intraday), MARK ONLY; ≈$7.03 OTM at QQQ ≈$742.03 (16:06, PROME-supplied). Card `MGMT-QQQ735P-OCT05`: *"SELL-OR-ROLL BY MON 10/05 15:00 ET — no action owed today"*; re-read Monday morning | — | **Will**; TERRY card |
| — | **USO $150C Oct-09 ×1 — expires Fri 10/09** | 🟠 6 sessions | ×1, basis $299.66; $4.15 / $415.00 / +$115.34 `[10/1 pc]`; USO $150.00 ⇒ at the strike. Rail *"Hard stop Fri 10/09 15:00 ET"* (`MGMT-USO150C-OCT09`); no harvest rule registered | WQ-297 A ties it to the USO stock line (one oil bet) — PROME's read, not adjudicated | **Will**; TERRY notes |
| WQ-302 | **TLT $82P Oct-16 ×1 + HBAN $16P Oct-16 ×2 — cards on file** | 🟠 Wed 10/14 close | TLT $4.25 / $425.00 (+153.47%), HBAN $0.90 / $180.00 (−5.93%) `[10/1 pc]`, MARK ONLY. Cards are A/B/C choices, not price triggers | — (×1 re-read of the TLT card = TERRY) | **Will** chooses; TERRY cards |

### Will decides / PROME re-reads — facts owed

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-69** | **Cash +$53.54 above the 9/30-implied figure, no row shown** | 🟡 cash, not quantity | 9/30 cash $18,102.04 − pending $4,007.98 = $14,094.06 expected; both 10/1 views show $14,147.60 (unchanged midday → end of day) | A September money-market dividend credited at month-end (plausibility only: ≈3.5%/yr on $18,102) — UNVERIFIED. Kept separate from D-63 (different window) | **Will** — one Activity view 9/29→10/01 answers D-69, D-63 and D-71 |
| **D-70** (re-stated) | **Records behind the mirror** | 🟡 record | `FORGE/position_management.tsv` row 18 still carries the **Oct-01 $740P ×4 as live** (*"Will sells or rolls the remaining four"*) and there is **no row for the Oct-02 $740P ×4**; rows 19–21 quote 9/30 or intraday marks. This edit changes `source_sha256` again ⇒ every mapping sourced here is withheld until re-review. TERRY's `MGMT-QQQ740P-OCT01` addresses a line that is gone. BRENT leg CLOSED (`AGENTS/BRENT/TRADE.md` reads the 159C sold 9/30 — checked at the artifact) | Expected lag, not an error | **PROME** (TSV rows + re-review) · **TERRY** (cards at next touch) — ANVIL edits none |
| **D-66** (widened) | **Fill TIMES — 9/30 (9 fills, 5 cancels), 10/1 midday (4 fills, 1 cancel); 10/1 afternoon: the Oct-01 ×4 exit and the Oct-02 ×4 entry show NEITHER price NOR time** | 🟡 | Midday: per-share fills + net amounts shown, sequence = row order only | — | Will (order detail); the afternoon legs ride D-71's view |
| **D-62** | **Fidelity ledger — $0.45 break in the broker's own running balance** | 🟡 carried | 17,740.43 + 359.34 (TLT 82P, 9/28) = 18,099.77 vs 18,099.32 shown; 33 of 34 links hold | A fee/adjustment without its own row, OR a transcription digit misread | **PROME** re-reads the 9/29 image cell |
| **D-63** | **Cash bridge +$2.27 unattributed** | 🟡 carried | 9/25-close cash + pending + the 9/28 rows = $18,099.77 vs cash $18,102.04; the Sep-30 Activity showed no dividend / interest row; 9/29 rows (if any) not captured | Money-market dividend, the APD dividend, or interest — ANVIL picks none (see D-69) | **Will** — Activity 9/29 (low) |
| **D-64** | **Robinhood card — $5.00 unexplained** | 🟡 carried | $290.15 of lines + BP vs $295.15 shown `[9/29 13:4x intraday]`; not re-captured 9/30 or 10/1 | BP ≠ cash, a line valued off another price, or a line not on the card | **Will** — RH cash/account detail |
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

### Owner decides — ruled / gated (nothing owed by Will today)

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-47** | **RH WAL Dec-18 $70P ×1 — `GATE-TERRY-ROLL70-EXIT`** | 🟡 78 DTE | ≈$265.00 derived `[9/29 13:4x intraday]` (not re-captured); entry bought 9/02 @ $2.20; 0-of-3 as last recorded; time stop 12/4; no resting exit order | — | **Will** (manual harvest); REGINALD grades / TERRY proposes |
| VLO-SCALE | **2 additional VLO sh STOOD DOWN** | TERMINAL | 9/25 F1 FIRED; TERRY 4ad672c43, PROME/GATES.tsv. Optional official-CME override only as that row specifies | — | TERRY grades → Will |
| WQ-200 | **USO 37 sh — no line live** | ⚪ | Card DECLINED 9/10; $150.00 `[10/1 pc]` informational | — | Will's hand |
| — | **APD thesis tag + "D" badge** | ⚪ | Unassigned since 7/30; last − chg = $276.42 on both 10/1 views vs the $278.23 9/30 close (−$1.81/sh) | An ex-dividend adjustment — INFERRED, amount/pay date not shown | PROME / Will |

### This pass (end of day 10/1) — nothing CLOSED on a broker row

- **GONE:** QQQ $740P Oct-01 ×4 — row removed (absent from the view, past its expiry); disposition UNBOOKED, D-71. **NEW:** QQQ $740P Oct-02 ×4, basis $890.65.
- **14 Fidelity rows MARK ONLY:** quantities and bases identical to the intraday mirror to the cent. Cash unchanged $14,147.60.
- D-70's BRENT leg closed at the artifact. Earlier closures (the 10/1 midday sales, D-67, D-68) → rotation 10/01 chunk E.

---

## Immediate Actions (10/1 end-of-day reconcile state)

| Item | State | Owner |
|---|---|---|
| 🔴 **QQQ $740P Oct-02 ×4 expires TOMORROW (Fri 10/02) — ≈$2.03 OTM at QQQ ≈$742.03 (16:06, PROME-supplied); no card on the line; D-60's ITM leg UNOBSERVED** (rail: sell-or-roll before expiry; working order UNKNOWN) | 0 DTE Fri | **Will** (hand) / TERRY |
| 🔴 **D-71** — how the Oct-01 $740P ×4 left (sale or Fidelity liquidation; ≈ −$747.91 is an inference): the 10/1 Fidelity Activity / Pending view | one view | **Will** |
| 🟠 **QQQ $735P Oct-05 ×5** (Mon 10/05 15:00 rail) · **USO $150C Oct-09 ×1** (Fri 10/09 15:00 rail) | dated | **Will** / TERRY |
| 🟠 **WQ-302** TLT 82P ×1 + HBAN 16P ×2 by Wed 10/14; the one Fidelity question also answers D-60 | dated | **Will** |
| 🟡 **D-70** — TSV row 18 names the gone Oct-01 line, no row for the Oct-02 ×4, mappings withheld by this edit's hash change; the Oct-01 card is moot | record | **PROME · TERRY** |
| 🟡 **D-69** cash +$53.54 · **D-63** +$2.27 — the same Activity view 9/29→10/01 | one view | **Will** |
| 🟡 Transcription re-reads D-62 · D-65 | image | **PROME** |
| 🟡 **Robinhood** (not captured 9/30 or 10/1) — D-64 · before 9/01: D-28 · D-54 · D-18 · D-20 · D-37 | one view | **Will** |
| 🟡 **Fidelity Activity** 8/28–8/31 (D-45 +$43.81); older: D-1 · D-17 | one view | **Will** |
| 🟡 VLO staged 2 sh (VLO-SCALE) · USO 37 hand-managed · APD tag | carried | TERRY / Will / PROME |

---

*History → `_archive/JOURNAL.md` | Prior reconciles (10/1 intraday, 9/30, 9/29, 9/27, 9/20 standing write-in, 9/10, 9/3, 8/29, 8/14, 8/2, 7/30, 7/20, 7/16, 5/21) in git history + `_archive/` | Full-portfolio Feb snapshot → `PORTFOLIO.md` (**FROZEN/superseded, historical only — never cite as live**) | Position truth = Will/broker direct (off-repo) | Marks-of-record transcription → `PROME/data/2026-10-01b_broker-capture-TRANSCRIPTION.md` (Fidelity positions 10/1 end of day); prior `…2026-10-01_…` (10/1 intraday + Pending list) · `…_2026-09-30_…` · `…_2026-09-29_…` (the RH rows' source)*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumers: `AGENTS/TERRY/scripts/positions_from_forge.py` (sections `^## (Fidelity|Robinhood)` + `^## Account <NAME>`; table headers by prefix; cell text — emphasis and strikethrough visible) · `PROME/tools/desk_attention.py` `holdings()` (same sections; `Qty` + `Ticker|Strike|Position` headers; expiry year from `**Updated:**`) · `PROME/tools/will_brief.py` `parse_money()` (header before the first `## `: `account total:**`, `money market):** $X (Y%)`, `**Updated:** YYYY-MM-DD`, `marks = [Fri ]YYYY-MM-DD`) · `FORGE/position_management.tsv` `source_sha256` (any byte change here withholds every mapping sourced to this file until PROME re-reviews) · `AGENTS/BRENT/scripts/pending_receipts.py` (text-level closure candidates). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself here in the same commit that starts parsing. *(Pass notes 9/27 → 10/1 intraday → rotation 10/01 chunk F. Conventions they set, still binding: the header money line keeps the shape `will_brief.py` reads; option expiries carry the year; the `Mark <m/d>` header is prefix-bound; terminal records live in italic lines, which no parser reads as rows.)* *(10/1 end-of-day pass: no structural change — same sections, headers and row conventions; `Mark 10/1` unchanged; one Off-thesis row replaced in place (Expiry `Oct-01-2026` → `Oct-02-2026`, Qty 4), no table added or removed; header money line same shape; `**Updated:** 2026-10-01`, `marks = 2026-10-01` = a POST-CLOSE capture.)*
