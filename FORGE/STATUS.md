# FORGE — Trading Operations

Dashboard management mapping → [position_management.tsv](position_management.tsv); maintenance contract → [dashboard notes](DASHBOARD.md). Holdings remain in this file; approval, order and fill evidence are separate. A changed evidence source invalidates its management mapping until reviewed.

> ✅ **2026-09-29 (Tue) — RECONCILE BY ANVIL to Will's INTRADAY captures ~13:4x ET (market OPEN — live vendor marks, NOT a close; every mark `[9/29 13:4x intraday]`).** Source `PROME/data/2026-09-29_broker-capture-TRANSCRIPTION.md` (PROME's transcription of five Will screenshots posted 13:46 ET): **Fidelity positions** · **Fidelity Activity 9/01→9/28 (35 rows: net amount + running balance; NO qty / per-share price / fill time)** · **Robinhood home card + "Recent" activity 9/01→9/25**. ANVIL re-verified from the tables (the clerk has no image access): value = last × qty (×100) ✓ and G/L = value − basis ✓ on 15 of 15 rows; Σ positions $18,720.83 + cash $18,102.04 = **$36,822.87 to the cent** ✓ (no pending shown); Σ Today −$845.38 ✓; Σ G/L −$479.55 ✓; ledger chain 33 of 34 links ✓ (the break = D-62). 14 broker % cells and 2 avg-cost cells differ from recomputation by 0.01 — broker rounding; shown values kept. **Quantities: all 15 Fidelity rows + both RH option lines = MARK ONLY — no NEW, no QTY CHANGE, no GONE**; the capture CONFIRMS the four `[9/28 fills receipt]` quantities (QQQ 730P ×9 · TLT 77P ×15 · TLT 82P ×1 · RH WAL 70P ×1). Superseded 9/27 + 9/28 header blocks and the 9/27-built discrepancy list → `_archive/STATUS_ROTATION_2026-09-29.md`.
>
> ⚠️ **ACCOUNT SCOPE — Fidelity: ONE account; header reads "Traditional IRA", number redacted ⇒ 216461326 INFERRED by position-set match. The Activity view is the same account (INFERRED: its chain passes through the 9/25-close cash + pending to the cent and its amounts land $2.27 short of today's cash — D-63). Two ledger rows (QQQ 710P, 9/17–9/18) carry a "(Margin)" tag — recorded, not interpreted. Robinhood Individual: home card + Recent activity 9/01→9/25 — no stocks card, nothing before 9/01.** Rows absent from a view are retained and flagged; a dated contract past its own expiry leaves the live tables, its disposition UNBOOKED unless a broker row shows it.
>
> **Updated:** 2026-09-29 = last broker-view reconcile (the date token machine consumers read as the export vintage — see footer) · marks = 2026-09-29 intraday ~13:4x ET `[9/29 13:4x intraday]` — NOT a close · **Fidelity cash (money market):** $18,102.04 (49.16%), no pending shown · **Fidelity account total:** $36,822.87 (Today −$845.38 / −2.24%; open G/L −$479.55 / −2.50%) — was $37,074.34 `[9/25c]` ⇒ −$251.47; cash was $17,512.69 + pending $1.97 ⇒ +$587.38 = the 9/28 ledger rows +$585.11 + an unattributed +$2.27 (D-63) · **Robinhood:** $295.15 (Today +$35.00 / +13.45%), BP $8.94 — was $228.15 / $8.94 `[RH card 9/27]` ⇒ +$67.00. Earlier rotations → `_archive/STATUS_ROTATION_2026-09-27.md`, `…_2026-09-20.md`, `…_2026-09-10.md`, `_archive/RECONCILE_2026-08-29_RECORD.md`.

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (7/18 re-base + amendment #1 = current). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All cells `[9/29 13:4x intraday]` (Fidelity positions); "ledger <date>" = the 9/29 transcription's Activity table ③.*

| Ticker | Type | Qty | Cost | Mark 9/29 | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | 10 | $23.65 | $332.02 | $3,320.20 | +$3,083.75 / +1,304.18% | Today −$63.80. **SOLD 9/15, net +$1,653.14** (ledger 9/15) — −5 sh INFERRED from the 9/16 capture delta (ledger shows no qty); basis $354.67→$236.45 ⇒ $118.22 sold ⇒ ≈+$1,534.92 realized (derived). Pre-7/30 5-sh sale = D-1 |
| GLD | Stock | 17 | $374.74 | $379.94 | $6,458.98 | +$88.48 / +1.38% | Today +$34.51. **BOUGHT 9/15, net −$393.00** (ledger 9/15); basis $5,977.50 + $393.00 = $6,370.50 exact ⇒ +1 sh (qty INFERRED). MIDAS domain; largest line |
| USO | Stock | 37 | $122.28 | $145.25 | $5,374.25 | +$849.98 / +18.78% | Today −$176.12. **WQ-200 DECLINED by Will 9/10 — NO harvest/give-back rule live; Will manages by hand.** BRENT thesis (Hormuz-gap entry) |
| VLO | Stock | 1 | $412.00 | $387.30 | $387.30 | −$24.70 / −6.00% | Today −$2.27. **BOUGHT 9/18, −$412.00, in THIS account** (ledger 9/18 + positions view; fill TIME not shown — D-55). WQ-213: 1 of 3; **2 sh STAGED under `GATE-TERRY-VLO-SCALE`** (TERRY grades; 9/25 NOT MET, F1 UNKNOWN — TERRY STATUS 9/25). **Exit rule on the held share: `GATE-TERRY-VLO-HELD-01` REGISTERED 9/28 18:36 ET (WQ-330, Will "both"): Nov crack settlement < $90.16 ⇒ sell rec (< $95 notice); signed US distillate export-restriction text at primary ⇒ SELL at the next regular session (Will may act without the desk; TERRY recs if he has not); A: TERRY grades, Will executes; not adjudicated here (rule 7)** |
| APD | Stock | 2 | $294.79 | $279.10 | $558.20 | −$31.37 / −5.33% | Today +$0.70. Broker shows a "(D)" badge — recorded, not interpreted. Thesis tag unassigned since 7/30 |
| TBT | Stock | 10 | $34.65 | $42.29 | $422.90 | +$76.44 / +22.06% | Today +$7.60. **SOLD 9/15, net +$158.96** (ledger 9/15) — −4 sh INFERRED; basis $484.82→$346.46 ⇒ $138.36 sold ⇒ ≈+$20.60 realized (derived). Duration-short leg (BOND/TERRY); no management rule |

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

*No live event-box rows — the VIX $20C/$25C spread (CLOSED 2026-07-30, realized −$111.60) and the five Aug-21-2026 EXPIRED rows (realized −$2,816.72 total) are terminal → rotation records.*

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, owned by no agent — recorded so it is not invisible. **TERRY disposition card for both rows** (`AGENTS/TERRY/setups/QQQ730P-USO159C_sep30-disposition_2026-09-28.md`, `f2964be4e`, a RECOMMENDATION — SELL both); **WQ-316** carries Will's decision; no management RULE exists on either row. Terminal tickets 9/04–9/25 → `_archive/STATUS_ROTATION_2026-09-27.md` § Ticket record; the 9/03 IWM 293P entry (−$85.33, liquidated 9/04 +$1.97 ⇒ −$83.36) is now visible (ledger 9/03).

| Ticker | Strike | Expiry | Qty | Cost | Mark 9/29 | Value | P&L | Note |
|--------|--------|--------|-----|------|-----------|-------|-----|------|
| QQQ | $730P | Sep-30-2026 | 9 | $2.49 | $1.27 | $1,143.00 | −$1,094.97 / −48.93% | Today −$684.00. **×9 CONFIRMED by the 9/29 view.** 9/28: SOLD 1 of 10 @ $1.98, ledger +$197.34 = receipt ⇒ **−$51.32** vs the $248.66 lot (broker basis $2,486.63 → $2,237.97); fill time not shown (D-61). **BOUGHT 9/24, −$2,486.63** (ledger). **Expires Wed 9/30.** Card rec SELL (not a rule) — **WQ-316 = Will's sell/hold on ×9; hard stop Wed 9/30 15:00 ET.** IN-the-money expiry handling in the IRA = UNOBSERVED (D-60). A 1-of-10 sale is a partial (root rule #7 frames trims) — recorded, not adjudicated. Not the Sep-25 $730P (bought 9/21 −$463.33, liquidated 9/25 +$1.97) |
| USO | $159C | Sep-30-2026 | 2 | $4.61 | $0.01 | $2.00 | −$919.33 / −99.79% | Today −$82.00. **×2 OPEN, CONFIRMED** (not sold 9/28). **BOUGHT 9/18, −$921.33** (ledger). **Expires Wed 9/30.** Card rec SELL; **WQ-316 = Will's sell/hold; hard stop Wed 9/30 15:00 ET.** ⚠️ Not the Robinhood $159C Sep-11 (D-58, closed) |

## Fidelity — Thesis Puts

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| **$77P** | **Sep-30-2026** | **15** | **$0.12** *(broker basis $173.44 on ×15; fees-in $0.11563)* | $0.08 | $120.00 | **−$53.44 / −30.82%** (today +$45). **×15 CONFIRMED.** 9/28 sale of 5 = THREE ledger rows +$5.69 / +$11.37 / +$11.37 = **$28.43** (1+2+2 ct @ $0.06 INFERRED from the amounts; the receipt said $28.45 — D-61) ⇒ **−$29.39** vs the $57.82 lot (broker basis $231.26 → $173.44). **Second recorded hand-deviation from the WQ-168 ④ / WQ-217 HOLD-to-expiry** (first 9/10: 5 sold net $28.43 ⇒ −$29.39). **NO ADD (WQ-280) unaffected. Expires Wed 9/30.** ⚠️ Gate proximity, NOT adjudication (rule 7): harvest *"half at ≥3×"* (PB-0002b: ≥$0.3469 fees-in; its "10 ct" size was written on ×20) — **NOT reached**: $0.08 = 0.69× the $0.11563 basis; exit gate `GATE-TERRY-007` **TERMINATED `MOOT ⇒ NO-VERDICT` 9/24**. See **D-31** |
| $82P | Oct-16-2026 | 1 | $1.68 | $4.30 | $430.00 | +$262.33 / +156.45% (today +$60). **×1 CONFIRMED**, broker basis $167.67. 9/28: SOLD 1 of 2 @ $3.60, ledger +$359.34 = receipt (order 09:43:29, filled 09:47:23 ET) ⇒ **+$191.66** vs the $167.68 lot (basis $335.35 on ×2 → $167.67). ITM (TERRY 9/26). **Card `MGMT-TLT82P-OCT16`** (TERRY `40e12ee0a`, built on ×2; the sale came before Will's management choice — WQ-292 / WQ-302); Will's A/B/C by **Wed 10/14 close** now concerns ×1. ⚠️ +156.45% is a mark, not a card option firing (rule 7). ITM-expiry handling in the IRA = named UNKNOWN on the card, UNOBSERVED in the ledger (D-60). 17 DTE |

### KRE — regional banks (REGINALD)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $60P | Dec-18-2026 | 2 | $2.57 | $0.46 | $92.00 | −$421.34 / −82.08% (today +$12). 80 DTE |
| $60P | Dec-18-2026 | 3 (M) | $2.93 | $0.46 | $138.00 | −$740.02 / −84.29% (today +$18) — Fidelity multi-lot marker; **five** Dec-18 KRE 60P across the two lots. 80 DTE |
| $60P | Sep-30-2026 | 2 | $2.27 | $0.02 | $4.00 | −$449.35 / −99.12% (today $0) — **Expires Wed 9/30. RULED WQ-168 ⑥: LAPSE.** Rides to $0; expiry-day handling → D-60 |

### WAL (REGINALD) — Sep-18 pair EXPIRED

*$70P + $67.5P Sep-18 ×1 each: **EXPIRED as of 9/18, broker-confirmed** (ledger rows posted 9/21) ⇒ realized **−$768.67 and −$750.67 = −$1,519.34** (full basis) — the WQ-168 ①② LAPSE as ruled. Rows → rotation record. Duration roll = the Robinhood WAL Dec-18 $70P ×1 below. The RH WAL $77.5P Aug-21 sale: P&L UNRECORDED — D-18.*

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18-2026 | 1 | $11.85 | $1.10 | $110.00 | −$1,074.67 / −90.72% | BROCK thesis vehicle; today −$15; 80 DTE. Will ruled HOLD 2026-08-13 (`PROME/proposals/2026-08-13_private-credit-batch-RULED.md` §②; BROCK owner; vehicle-mismatch flag live) |
| HBAN | $16P | Oct-16-2026 | 2 | $0.96 | $0.80 | $160.00 | −$31.34 / −16.38% | Today $0. ITM (TERRY 9/26). The 7/18 *"rides to expiry"* ruling stands as written but its premise failed — **card `MGMT-HBAN16P-OCT16`**, re-rule options for Will by **Wed 10/14** (WQ-302). 17 DTE |

## Robinhood — satellite account (Individual)

> **Home card 9/29 intraday: account $295.15 (Today +$35.00 / +13.45%), BP $8.94** `[9/29 13:4x intraday]` — was $228.15 / $8.94 `[RH card 9/27]` ⇒ +$67.00. Lines + BP = $290.15 ⇒ **$5.00 UNEXPLAINED (D-64)**. Per-line cost/value DERIVED from shown P/L ÷ P/L% (no Mark column ⇒ machine class `unverified` by design). **Prediction market:** Nithya Raman "Yes" 26.22 @ 58¢ ≈ $15.21 (+65.71% ⇒ cost ≈$9.18, derived — price and % identical to 9/27) — recorded, not adjudicated. **Recent activity 9/01→9/25 books the dead-by-date lines:** USO $159C Sep-11 (bought 9/10 $152, expired $0 — D-58) · QQQ $713C Sep-16 (bought 9/16 $167) + USO $165C Sep-16 (bought 9/14 $150), both expired $0 (D-57).

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **WAL $70P** | **Dec-18-2026** | 1 | **$2.20 ($220)** — bought 9/02 @ $2.20 (RH activity) ✓ | ≈$265.00 *(derived; mark ≈$2.65)* | ✅ **ON CARD 9/29 — +$45.00 / +20.45%** | TRY-WAL-ROLL70 (filled in Robinhood). Guard **`GATE-TERRY-ROLL70-EXIT`** *"WAL OFFICIAL CLOSE ≥ $81.90 on THREE CONSECUTIVE sessions"* — **0-of-3 as last recorded here** (REGINALD through 9/23, per TERRY STATUS 9/24; not re-read this pass). The option's +20.45% is not the gate — the gate reads WAL's close (rule 7). **$4.40 GTC sell order: CANCELLED / not there — Will 9/28** (`PROME/inbox/processed/2026-09-28_from-WAL_WQ-324-325-ruled-verbatim-and-4.40-GTC-cancelled.md`) ⇒ **no resting exit order; any take-profit is Will's manual act.** Time stop Fri 12/4. 80 DTE. **D-47** |
| **KRE $25P** | 1/15/2027 | 1 | $53.00 — card-derived ✓ | ≈$1.00 *(derived)* | ✅ **ON CARD 9/29 — −$52.00 / −98.11%** | Deep-OTM lottery; entry pre-7/16, never recorded — **D-54** (before the 9/01 activity view). 108 DTE |
| T | stock | 1 | — | — | ⚠️ no stocks card 9/29; no T row in RH activity 9/01→9/25 | Hypothesis: sold before 9/01, unconfirmed — **D-20**. The card no longer closes to the cent (D-64), so the 9/27 "no stock line" inference is weaker |

## Account UNATTRIBUTED — receipted fills not yet attributed to an account

*No rows. VLO ×1 (this section's only row since 9/19) moved to § Fidelity — Longs on the 9/25 ledger (D-55 account leg CLOSED). The section stays as the landing place for a receipt that names no account (the parser admits it — TERRY `cfd9b9115`).*

---

## ⚠️ Reconcile discrepancies (9/29 intraday reconcile, built 2026-09-29)

> Built against the Fidelity positions `[9/29 13:4x intraday]` + Fidelity Activity 9/01→9/28 + the RH card and Recent activity 9/01→9/25. **Nothing resolved by invention; every conjecture labeled; broker view > Will's word > desk record.** Ranked by decision urgency, expiring first. **Permanently UNKNOWN by WQ-167 (never asks):** the 9/2 USO 135C sale price. **One standing gap, not re-asked per row:** fill TIMES and per-share prices for every Fidelity ledger row (the view shows none). Prior list (9/27 build + 9/28 amendments) → `_archive/STATUS_ROTATION_2026-09-29.md` Chunk B.

### EXPIRING WED 2026-09-30 (one session left after today; hard stop for further sales Wed 9/30 15:00 ET — WQ-316)

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| — | **QQQ $730P Sep-30 ×9** — card (rec, not rule); WQ-316 open | 🔴 expires 9/30 | ×9 CONFIRMED; $1.27 / $1,143.00 / −48.93% `[9/29 13:4x intraday]`; 9/28 1-of-10 sale on the ledger (+$197.34). TERRY `f2964be4e` rec SELL; WQ-316 awaits Will's sell/hold | None on the position. ITM-at-expiry handling → D-60 | **Will** (his hand; WQ-316) |
| — | **USO $159C Sep-30 ×2** — card (rec, not rule); WQ-316 open | 🔴 expires 9/30 | ×2 CONFIRMED; $0.01 / $2.00 / −99.79% `[9/29 13:4x intraday]`. TERRY rec SELL | — | **Will** (his hand; WQ-316) |
| **D-60** | **Fidelity expiry-day handling — NARROWED: the OTM leg is OBSERVED, the ITM leg is not** | 🟠 bears on QQQ 730P ×9 (Wed) and TLT 82P ×1 (10/16) | Four ledger rows *"YOU SOLD CLOSING TRANSACTION OPTION LIQUIDATION"*, each on the contract's own expiry day, for pennies: IWM 293P 9/04 +$1.97 · QQQ 716P 9/08 +$0.99 · QQQ 710P 9/18 +$3.77 (Margin tag) · QQQ 730P Sep-25 9/25 +$1.97. Three others show **EXPIRED** with no cash row (QQQ 716P Sep-21, posted 9/22; WAL 70P + 67.5P Sep-18, posted 9/21) | Penny liquidation of near-worthless long options = OBSERVED; their OTM status is INFERRED from the proceeds (the ledger shows no underlying price). **OPEN: (i) an IN-the-money long option at expiry in the IRA — UNOBSERVED in any view; (ii) what decides LIQUIDATE vs EXPIRED — UNKNOWN** | **Will** — ask Fidelity alongside the WQ-302 question |
| **D-31** | **TLT $77P Sep-30 ×15 — HOLD (WQ-168 ④ / WQ-217)** | 🟡 ruled | ×15 CONFIRMED; $0.08 / $120.00 (0.69× the $0.11563 fees-in basis). Harvest line ≥$0.3469 NOT reached. Two hand-deviations on record (9/10, 9/28; 5 ct each, net $28.43 each per ledger). `GATE-TERRY-007` MOOT ⇒ NO-VERDICT 9/24; NO ADD (WQ-280) unaffected | Nothing — the ×15 rides to expiry unless the harvest line prints or Will sells by hand. The PB-0002b "10 ct" size was written on ×20 — TERRY's re-read | TERRY watches harvest → Will executes |
| WQ-168 ⑥ | **KRE $60P Sep-30 ×2 — LAPSE** | 🟡 ruled | $0.02 / $4.00 (−99.12%) | Nothing | Rides to $0 |

### Will decides / PROME re-reads — facts owed (no same-week expiry)

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| WQ-302 | **TLT $82P Oct-16 ×1 + HBAN $16P Oct-16 ×2 — ITM; cards on file** | 🟠 Wed 10/14 close | ×1 / ×2 CONFIRMED 9/29; TLT $4.30 / $430.00 (+156.45%), HBAN $0.80 / $160.00 (−16.38%). The TLT sale (9/28) came before Will's management choice; card built on ×2 | — (whether ×1 changes the card's options is TERRY's re-read) | **Will** chooses; TERRY cards |
| **D-62** 🆕 | **Fidelity ledger — $0.45 break in the broker's own running balance** | 🟡 | 17,740.43 + 359.34 (TLT 82P, 9/28) = 18,099.77; the view shows 18,099.32. The other 33 links hold to the cent | A fee/adjustment posted without its own row, OR a transcription digit misread (two digits differ). ANVIL cannot re-read the image. The positions cash ties better to the arithmetic balance (+$2.27) than to the shown one (+$2.72) — a lean, not proof | **PROME** re-reads the image cell → Will only if the image confirms |
| **D-63** 🆕 | **Cash bridge: ledger close → positions cash, +$2.27 unattributed** | 🟡 | 9/25-close cash + pending $17,514.66 + the five 9/28 rows $585.11 = $18,099.77 vs positions cash $18,102.04 ⇒ **+$2.27** (+$2.72 against the shown 18,099.32) | Money-market dividend, the APD "(D)" dividend, or interest — ANVIL picks none; no row shows it | **Will** — Activity view on/after 9/29 (low) |
| **D-64** 🆕 | **Robinhood card — $5.00 unexplained** | 🟡 | $265.00 + $1.00 + $15.21 + BP $8.94 = $290.15 vs $295.15 shown. The 9/27 card closed to the cent by the same method. The WAL line's +$45.00 / +20.45% is internally consistent on $220 | BP ≠ cash (e.g. a held deposit), a prediction-market line valued off another price, or a line not on the card — ANVIL picks none | **Will** — RH cash/account detail |
| **D-65** 🆕 | **RH activity 9/14–9/15 — put/call labels do not pair (transcription check)** | 🟡 no live position | Bought QQQ $707 **Put** 9/15 (9/14, $116) → "Sell QQQ $707 **Call** 9/15 $220"; "Buy QQQ $708 **Call** 9/15 $41" → "QQQ $708 **Put** Expiration" 9/15, while both 708P buys read Canceled | Hypothesis: the 9/15 "Call" rows are Puts (transcription or display slip) ⇒ 707P +$104, 708P −$41 — labeled, NOT booked. Outside the D-59 window | **PROME** — re-read the image |
| **D-61** (narrowed) | **9/28 fills — fill TIMES for QQQ 730P ×1 and TLT 77P ×5; TLT 77P net $0.02 apart** | 🟡 | Account leg CLOSED (below). Ledger TLT 77P = three rows Σ $28.43 vs the receipt's $28.45; ledger used for cash and realized | Receipt digit or PROME transcription — UNKNOWN | Will (order detail), low |
| **D-59** (narrowed) | **RH buying power 9/16 → 9/27: −$0.48 left after the activity** | 🟡 | 9/17→9/24: buys −$380.00 (713P $105 · 730P $59 · 744P $87 · NCLH 14P $16 · 740P $35 · 734P $78) · sells +$27.00 · deposits +$233.05 ⇒ **−$119.95** vs BP −$120.43. Window start INFERRED (the 9/16 capture shows the 713C bought that day ⇒ taken after the last 9/16 row) | Regulatory fees on the four sells + rounding — labeled | Will, low |
| **D-45** (pre-view residual) | **Original 8/28 → 9/03 bridge (+$3,702.46): +$43.81 before the view** | 🟡 | 8/28 cash + pending $14,323.25 (8/29 record); ledger's derived 9/01 opening $14,367.06; 9/01–9/02 rows +$3,658.65 | Something posted 8/28 close → 9/01 (8/31 activity, interest) — the view starts 9/01 | **Will** — Activity scrolled to 8/28–8/31 |
| **D-55** (residual) | **VLO fill TIME** | 🟡 | Fidelity, 9/18 | — | Will (order detail), low |
| **D-28** | **RH QQQ $715P ×1 — expired 8/31, outcome UNRECORDED** | 🟡 carried | Cost ≈$193.24; before the 9/01 activity view | Expired OTM / sold / exercised — none verified | RH history before 9/01 |
| **D-54** | **RH KRE $25P Jan-15-2027 — entry never recorded** | 🟡 carried | Cost $53.00 derived; on the mirror since 7/16; before the 9/01 view | Entry pre-7/16 ≈$0.53 — a derivation | Will |
| **D-18** | **RH WAL $77.5P Aug-21 — sale CONFIRMED 8/18, P&L UNRECORDED** | 🟡 carried | Existence closed 8/18 | Do not book at $0 | Will (not urgent) |
| **D-20** | **RH T share — absent; event contracts** | 🟡 carried | No stocks card; no T row 9/01→9/25 | Sold before 9/01, unconfirmed | Will — full RH view |
| **D-37** | **RH ≈$360 inflow (8/14→8/28) + "13 days left" banner** | 🟡 carried | Arithmetic recorded 8/29 | Deposit/transfer; banner referent unknown | Will (one line) |
| **D-17** | **STNG — in no capture, nowhere in FORGE** | 🟡 carried | Absent since 8/2; March-2026 record only | Recalled March position / closed pre-7/30 / a third account | Will — one line |
| **D-1** | **AAPL 5-sh sale pre-7/30 — date + price unrecorded** | 🟡 carried | Predates the 7/30–8/28 window | ~$565 cash class | Will / an older window |

### Owner decides — ruled / gated (nothing owed by Will today)

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-47** | **RH WAL Dec-18 $70P ×1 — `GATE-TERRY-ROLL70-EXIT`** | 🟡 80 DTE | ≈$265.00 derived (+20.45%) `[9/29 13:4x intraday]`; **entry CONFIRMED: bought 9/02 @ $2.20 = $220.00** (two same-day attempts Canceled); 0-of-3 as last recorded; time stop 12/4; $4.40 GTC CANCELLED (Will 9/28) | Nothing conjectured | **Harvest = Will's manual act**; REGINALD grades / TERRY proposes |
| VLO-SCALE | **2 staged VLO sh** | 🟡 review_by 10/14 | 9/25 NOT MET; F1 UNKNOWN (CME settle read = Will) | — | TERRY grades → Will |
| WQ-200 | **USO 37 sh — no line live** | ⚪ | Card DECLINED 9/10; $145.25 `[9/29 13:4x intraday]` informational | — | Will's hand |
| — | **APD thesis tag** | ⚪ | Unassigned since 7/30 | — | PROME / Will |

### RESOLVED this pass (receipts = the 9/29 transcription's ledger ③ / RH activity ⑤)

- **9/28 quantities → broker-CONFIRMED** by the 9/29 positions view (QQQ 730P ×9 · TLT 77P ×15 · TLT 82P ×1 · USO 159C ×2 · RH WAL 70P ×1). **D-61 account leg → CLOSED:** all 9/28 sales are rows in the Fidelity ledger (QQQ 730P +$197.34 and TLT 82P +$359.34 = the receipt; TLT 77P three rows).
- **D-44 → CLOSED:** "YOU SOLD INVESCO QQQ TR" **9/02, net +$2,125.00** ⇒ $708.33/sh on 3 sh (qty INFERRED from the 8/28 holding; the ledger shows none) ⇒ ≈−$19.23 vs the broker 3-sh basis $2,144.23 (8/29 record; derived).
- **D-45 (9/3 → 9/04 residual, −$85.33) → CLOSED:** the 9/3 capture cash $18,025.71 = the ledger balance after the 9/02 row to the cent; the next row, **9/03 IWM $293P Sep-04 BOUGHT −$85.33**, is the residual exactly (capture before that posting — INFERRED). The original 8/28→9/03 bridge leaves +$43.81 before the view (row above).
- **D-57 → CLOSED:** RH QQQ $713C Sep-16 bought 9/16 $167.00 @ $1.67, Expiration $0.00 9/16 ⇒ −$167.00 · USO $165C Sep-16 bought 9/14 $150.00 @ $1.50, Expiration $0.00 9/16 ⇒ −$150.00. (RH lists an expiration row below a same-day buy — same pattern as the 9/21 QQQ 730P bought and expired that day.)
- **D-58 RH leg → CLOSED:** USO $159C Sep-11 bought 9/10 $152.00 @ $1.52, Expiration $0.00 9/11 ⇒ −$152.00.
- **D-47 entry leg → CONFIRMED** (above). **D-60 / D-59 → NARROWED** (above).
- Recorded as seen, not re-derived: RH "9/10 USO Call Debit Spread $630.00" (direction not in the transcription; PROME reads it as the close) · RH 9/11 withdrawal −$200.00 · deposits 9/01–9/24.

---

## Immediate Actions (9/29 reconcile state)

| Item | State | Owner |
|---|---|---|
| 🔴 **Four Sep-30 lines expire Wed 9/30:** QQQ 730P ×9 (no rule; WQ-316 open) · USO 159C ×2 (no rule; WQ-316 open) · TLT 77P ×15 (HOLD) · KRE 60P ×2 (LAPSE) — plus **D-60** (ITM expiry handling UNOBSERVED). **Hard stop for further sales Wed 9/30 15:00 ET** | 1 session after today | **Will** (hand) / TERRY (77P harvest watch; re-reads quotes Wed AM) |
| 🟠 **WQ-302** TLT 82P ×1 + HBAN 16P ×2 choices by Wed 10/14; the one Fidelity question also answers D-60 | dated | **Will** |
| 🟡 **Transcription re-reads** — D-62 ($0.45 balance cell) · D-65 (9/15 put/call labels) | image | **PROME** |
| 🟡 **Robinhood** — D-64 ($5.00) · history before 9/01: D-28 · D-54 · D-18 · D-20 · D-37 | one view | **Will** |
| 🟡 **Fidelity Activity** 8/28–8/31 (D-45 +$43.81) and on/after 9/29 (D-63 +$2.27); older: D-1 · D-17 | one view | **Will** |
| 🟡 VLO staged 2 sh (VLO-SCALE) · USO 37 hand-managed · APD tag | carried | TERRY / Will / PROME |

---

*History → `_archive/JOURNAL.md` | Prior reconciles (9/27, 9/20 standing write-in, 9/10, 9/3, 8/29, 8/14, 8/2, 7/30, 7/20, 7/16, 5/21) in git history + `_archive/` | Full-portfolio Feb snapshot → `PORTFOLIO.md` (**FROZEN/superseded, historical only — never cite as live**) | Position truth = Will/broker direct (off-repo) | Marks-of-record transcription → `PROME/data/2026-09-29_broker-capture-TRANSCRIPTION.md` (Fidelity positions 9/29 intraday + Activity 9/01→9/28 + RH card and activity)*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumers: `AGENTS/TERRY/scripts/positions_from_forge.py` (sections `^## (Fidelity|Robinhood)` + `^## Account <NAME>`; table headers by prefix; cell text — emphasis and strikethrough visible) · `PROME/tools/desk_attention.py` `holdings()` (same sections; `Qty` + `Ticker|Strike|Position` headers; expiry year from `**Updated:**`) · `PROME/tools/will_brief.py` `parse_money()` (header before the first `## `: `account total:**`, `money market):** $X (Y%)`, `**Updated:** YYYY-MM-DD`, `marks = [Fri ]YYYY-MM-DD`) · `FORGE/position_management.tsv` `source_sha256` (any byte change here withholds every mapping sourced to this file until PROME re-reviews) · `AGENTS/BRENT/scripts/pending_receipts.py` (text-level closure candidates). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself here in the same commit that starts parsing. *(9/27 pass: header money line RESTORED to the shape `will_brief.py` reads — it returned None on the 9/20 header; option expiries carry the year (a year-less "Sep-30" parses as 2027 from 10/1 in `positions_from_forge.py`); new table in § Off-thesis; VLO moved § Account UNATTRIBUTED → § Fidelity — Longs; WAL and RH-Sep-11 rows rotated. Parser receipts in the ANVIL report.)* *(9/28 fills pass: no structural change; `**Updated:**` stayed 9/27 because a fills receipt is not a broker view; Value `—` / P&L `see note` on the three sold-down rows, by design.)* *(9/29 pass: no structural change — same sections, headers and row conventions; `Mark 9/25` → `Mark 9/29` (prefix-bound); the three sold-down rows carry numeric Value/P&L again (broker marks at the new qty); `**Updated:** 2026-09-29` is a broker view, but INTRADAY — `marks = 2026-09-29` carries no close; `will_brief.py` will render it "Broker export 2026-09-29".)*
