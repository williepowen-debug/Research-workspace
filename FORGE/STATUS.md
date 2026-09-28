# FORGE — Trading Operations

Dashboard management mapping → [position_management.tsv](position_management.tsv); maintenance contract → [dashboard notes](DASHBOARD.md). Holdings remain in this file; approval, order and fill evidence are separate. A changed evidence source invalidates its management mapping until reviewed.

> 🧾 **2026-09-28 (Mon) — FILLS PASS BY ANVIL from Will's pasted fills receipt (PROME transcription, `PROME/reports/2026-09-28_will-fills-receipt.md`); marks UNCHANGED at the Fri 9/25 close; cash/account totals NOT refreshed (no broker view today).** Three sales by Will's own hand (root rule #5), each a PARTIAL: **QQQ Sep-30 $730P 1 of 10 @ $1.98, net $197.34** · **TLT Sep-30 $77P 5 of 20 @ $0.06, net $28.45** · **TLT Oct-16 $82P 1 of 2 @ $3.60, net $359.34** (order 09:43:29 ET, filled 09:47:23 ET — the only line with a time) ⇒ Σ net **$585.13** (arithmetic on the receipt; NOT added to the cash figure below). **USO Sep-30 $159C ×2 NOT sold.** Plus, from WAL's window (`PROME/inbox/processed/2026-09-28_from-WAL_WQ-324-325-ruled-verbatim-and-4.40-GTC-cancelled.md`): the Robinhood WAL Dec-18 $70P **$4.40 GTC sell order is CANCELLED / not there** (Will 9/28) — D-47. **Three vintage clocks in this file — do not mix them:** standing quantities of the four changed lines `[9/28 fills receipt]` (QQQ 730P ×9 · TLT 77P ×15 · TLT 82P ×1 · RH WAL 70P ×1, GTC cancelled) · every mark, value and G/L cell `[9/25c]` · VLO fill `[9/18 receipt]`. On the three sold-down rows the Value and P&L cells read `—` / *see note* (the 9/20 pass's convention for a changed qty with no new mark — a 9/25 value at the old qty would be wrong, a 9/25 mark × new qty would be arithmetic posing as a broker value); the 9/25c mark stays in its column with its stamp. Account for the three sales: not named in the paste ⇒ Fidelity **INFERRED** (the only mirrored account holding these contracts, quantities matched); fill time + account for lines 1–2 → **D-61**. Superseded 9/27 row text is in git (`f39c70073`).
>
> ✅ **2026-09-27 (Sun) — TRANSACTION RECONCILE BY ANVIL to the Fri 2026-09-25 CLOSE.** Source `PROME/data/2026-09-27_broker-capture-TRANSCRIPTION.md` (three Will screenshots, supplied 9/27 ~15:58 ET): **Fidelity positions `[9/25 CLOSE]`** · **Fidelity Activity "Past 30 days", 26 rows 9/04→9/25 — net amounts + running cash balance; view cut at 9/04; NO qty / per-share price / fill time** · **Robinhood home card `[9/27, weekend ⇒ 9/25 close]`**. ANVIL re-verified from the tables: value = last × qty (×100) ✓ and G/L = value − basis ✓ on 15 of 15 rows; Σ positions $19,559.68 + cash $17,512.69 + pending $1.97 = **$37,074.34 to the cent** ✓; Σ Today −$1,956.92 ✓; Σ G/L −$114.86 ✓; ledger chain prior + amount = balance on all 23 amount rows ✓; ledger close $17,514.66 = cash + pending ✓; RH $203.00 + $1.00 + $15.21 + BP $8.94 = **$228.15** ✓ (line values DERIVED). Three broker % cells differ from recomputation by 0.01 (VLO · USO · QQQ 730P) — broker rounding; shown values kept.
>
> ⚠️ **ACCOUNT SCOPE — Fidelity: ONE account; header cropped on both images ⇒ Traditional IRA 216461326 INFERRED by position-set match (as 9/10); the Activity view is the same account (its close = cash + pending to the cent). Two ledger rows (QQQ 710P, 9/17–9/18) carry a "(Margin)" type tag — recorded as seen, not interpreted. Robinhood Individual: home card only — no history view, no stocks card.** Rows absent from a view are retained and flagged; a dated contract past its own expiry leaves the live tables, its disposition UNBOOKED unless a broker row shows it (D-58 · D-57).
>
> **Updated:** 2026-09-27 = last broker-view reconcile (the date token machine consumers read as the export vintage — see footer) · **+ 2026-09-28 FILLS PASS: quantities of four lines `[9/28 fills receipt]`** (block above); everything else as the 9/27 reconcile · marks = Fri 2026-09-25 CLOSE `[Fidelity positions 9/25c]` / `[RH card 9/27]` · ⚠️ cash + total below are `[9/25c]`, NOT refreshed for the 9/28 sales (+$585.13 net, receipt arithmetic; settlement not seen) · **Fidelity cash (money market):** $17,512.69 (47.24%) + pending $1.97 · **Fidelity account total:** $37,074.34 (Today −$1,956.92 / −5.01%; open G/L −$114.86 / −0.58%) — was $39,779.11 `[9/16 capture]` ⇒ −$2,704.77 · **Robinhood:** $228.15, BP $8.94 — was $454.33 / $129.37 `[9/16]`. Superseded header, rows, discrepancy prose + the 9/04–9/25 Fidelity ticket record → `_archive/STATUS_ROTATION_2026-09-27.md`; earlier → `_archive/STATUS_ROTATION_2026-09-20.md`, `…_2026-09-10.md`, `_archive/RECONCILE_2026-08-29_RECORD.md`.

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (7/18 re-base + amendment #1 = current). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All cells `[Fidelity positions, 9/25 CLOSE]`; "row N" = the transcription's Activity table ③.*

| Ticker | Type | Qty | Cost | Mark 9/25 | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | 10 | $23.65 | $341.07 | $3,410.70 | +$3,174.25 / +1,342.46% | Today +$51.50. **SOLD 9/15, net +$1,653.14** (row 14) — −5 sh INFERRED from the 9/16 capture delta (ledger shows no qty); basis $354.67→$236.45 ⇒ $118.22 sold ⇒ ≈+$1,534.92 realized (derived). Pre-7/30 5-sh sale = D-1 |
| GLD | Stock | 17 | $374.74 | $393.41 | $6,687.97 | +$317.47 / +4.98% | Today +$29.24. **BOUGHT 9/15, net −$393.00** (row 12); basis $5,977.50 + $393.00 = $6,370.50 exact ⇒ +1 sh (qty INFERRED). MIDAS domain; largest line |
| USO | Stock | 37 | $122.28 | $148.33 | $5,488.21 | +$963.94 / +21.30% | Today −$176.12. **WQ-200 DECLINED by Will 9/10 — NO harvest/give-back rule live; Will manages by hand.** BRENT thesis (Hormuz-gap entry) |
| VLO | Stock | 1 | $412.00 | $387.18 | $387.18 | −$24.82 / −6.03% | Today +$4.32. **BOUGHT 9/18, −$412.00, in THIS account** (row 7 + positions view ⇒ D-55 account leg CLOSED; fill TIME not shown). WQ-213: 1 of 3; **2 sh STAGED under `GATE-TERRY-VLO-SCALE`** (TERRY grades; 9/25 NOT MET, F1 UNKNOWN — TERRY STATUS 9/25). **No exit rule exists on the held share** |
| APD | Stock | 2 | $294.79 | $281.76 | $563.52 | −$26.05 / −4.42% | Today −$5.46. Broker shows a "(D)" badge — recorded, not interpreted. Thesis tag unassigned since 7/30 |
| TBT | Stock | 10 | $34.65 | $40.91 | $409.10 | +$62.64 / +18.08% | Today +$1.60. **SOLD 9/15, net +$158.96** (row 13) — −4 sh INFERRED; basis $484.82→$346.46 ⇒ $138.36 sold ⇒ ≈+$20.60 realized (derived). Duration-short leg (BOND/TERRY); no management rule |

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

*No live event-box rows — the VIX $20C/$25C spread (CLOSED 2026-07-30, realized −$111.60) and the five Aug-21-2026 EXPIRED rows (realized −$2,816.72 total) are terminal → rotation records.*

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, owned by no agent — recorded so it is not invisible. **9/27: no card found** (SEARCH-NOT-FOUND then). **9/28: TERRY disposition card now exists for both rows** (`AGENTS/TERRY/setups/QQQ730P-USO159C_sep30-disposition_2026-09-28.md`, `f2964be4e`, a RECOMMENDATION — SELL both) and **WQ-316** carries Will's decision; no management RULE exists on either row. The 9/04–9/25 terminal tickets (IWM 293P · QQQ 716P/715P/710P/716P/730P-Sep-25 · USO 153C; **−$521.58** across the six with both legs visible) → `_archive/STATUS_ROTATION_2026-09-27.md` § Ticket record.

| Ticker | Strike | Expiry | Qty | Cost | Mark 9/25 | Value | P&L | Note |
|--------|--------|--------|-----|------|-----------|-------|-----|------|
| QQQ | $730P | Sep-30-2026 | 9 | $2.49 | $1.30 | — | see note | **qty 10→9 `[9/28 fills receipt]`: SOLD 1 @ $1.98, net $197.34** (Will's own order; fill time + account not in the paste — D-61) ⇒ ≈−$51.32 realized vs $248.66/ct average basis (derived; broker lot method UNKNOWN); remaining 9 ≈$2,237.97 basis (derived). At 9/25c: $1.30 / $1,300.00 on ×10 (−$1,186.63 / −47.73%; today −$1,520.00) — not restated at ×9. **BOUGHT 9/24, −$2,486.63** (row 2). **Expires Wed 9/30.** Card: TERRY `QQQ730P-USO159C_sep30-disposition_2026-09-28.md` (`f2964be4e`) rec SELL all 10 — **WQ-316 still awaits Will's explicit sell/hold on the remaining ×9; hard stop Wed 9/30 15:00 ET.** A 1-of-10 sale is a partial (root rule #7 frames trims) — recorded, not adjudicated. Not the Sep-25 $730P (bought 9/21 −$463.33, liquidated 9/25 +$1.97) |
| USO | $159C | Sep-30-2026 | 2 | $4.61 | $0.65 | $130.00 | −$791.33 / −85.89% | Today −$240.00. **NOT sold 9/28 — ×2 OPEN `[9/28 fills receipt]`.** **BOUGHT 9/18, −$921.33** (row 8). **Expires Wed 9/30.** Card: TERRY `f2964be4e` rec SELL; **WQ-316 awaits Will's sell/hold; hard stop Wed 9/30 15:00 ET.** ⚠️ Not the Robinhood $159C Sep-11 (D-58) |

## Fidelity — Thesis Puts

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| **$77P** | **Sep-30-2026** | **15** | **$0.12** *(broker basis $231.26 on ×20 `[9/25c]`; ×15 ≈$173.45 derived; fees-in $0.11563)* | $0.04 | — | see note — at 9/25c on ×20: $80.00, **−$151.26 / −65.41%** (today −$40); not restated at ×15. **qty 20→15 `[9/28 fills receipt]`: SOLD 5 @ $0.06, net $28.45** (fill time + account not in the paste — D-61) ⇒ ≈−$29.37 vs 5 × $11.563 = $57.82 (derived). **Second recorded hand-deviation from the WQ-168 ④ / WQ-217 HOLD-to-expiry** (first 9/10: 5 sold net **$28.43**, row 18 ⇒ −$29.39). **NO ADD (WQ-280) unaffected. Expires Wed 9/30.** ⚠️ Gate proximity, NOT adjudication (rule 7): harvest *"half at ≥3×"* (PB-0002b: 10 ct at ≥$0.3469 fees-in — sized when ×20) — **NOT reached**: the $0.06 fill = 0.52× the $0.11563 fees-in basis (salvage, not harvest); the 9/25c $0.04 = 0.35×; exit gate `GATE-TERRY-007` **TERMINATED `MOOT ⇒ NO-VERDICT` 9/24** (TERRY STATUS, DGS10 9/22 4.96). See **D-31** |
| $82P | Oct-16-2026 | 1 | $1.68 | $3.02 | — | see note — at 9/25c on ×2: $604.00, **+$268.65 / +80.11%** (today −$26); not restated at ×1. **qty 2→1 `[9/28 fills receipt]`: SOLD 1 @ $3.60, net $359.34** — order 09:43:29 ET, filled 09:47:23 ET (the execution line reads $359.99 before the $359.34 net — recorded as seen) ⇒ ≈+$191.67 vs $167.68/ct average basis (derived: ($604.00 − $268.65) ÷ 2; broker lot method UNKNOWN); remaining ×1 ≈$167.68 basis (derived). ITM (TERRY 9/26). **Card `MGMT-TLT82P-OCT16`** (TERRY `40e12ee0a`) was built on ×2 — **this sale came before any card choice (WQ-292 / WQ-302)**; Will's choice A/B/C by **Wed 10/14 close** now concerns ×1; broker handling of an ITM long put in the IRA = named UNKNOWN on the card. 21 DTE at 9/25 |

### KRE — regional banks (REGINALD)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $60P | Dec-18-2026 | 2 | $2.57 | $0.42 | $84.00 | −$429.34 / −83.64% (today $0). 84 DTE |
| $60P | Dec-18-2026 | 3 (M) | $2.93 | $0.42 | $126.00 | −$752.02 / −85.65% (today $0) — Fidelity multi-lot marker; **five** Dec-18 KRE 60P across the two lots. 84 DTE |
| $60P | Sep-30-2026 | 2 | $2.27 | $0.02 | $4.00 | −$449.35 / −99.12% (today −$6) — **Expires Wed 9/30. RULED WQ-168 ⑥: LAPSE.** Rides to $0 |

### WAL (REGINALD) — Sep-18 pair EXPIRED

*$70P + $67.5P Sep-18 ×1 each: **EXPIRED as of 9/18, broker-confirmed** (Activity rows 4–5, posted 9/21) ⇒ realized **−$768.67 and −$750.67 = −$1,519.34** (full basis) — the WQ-168 ①② LAPSE as ruled. Rows → rotation record. Duration roll = the Robinhood WAL Dec-18 $70P ×1 below. The RH WAL $77.5P Aug-21 sale: P&L UNRECORDED — D-18.*

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18-2026 | 1 | $11.85 | $1.25 | $125.00 | −$1,059.67 / −89.45% | BROCK thesis vehicle; today $0; 84 DTE. Will ruled HOLD 2026-08-13 (`PROME/proposals/2026-08-13_private-credit-batch-RULED.md` §②; BROCK owner; vehicle-mismatch flag live) |
| HBAN | $16P | Oct-16-2026 | 2 | $0.96 | $0.80 | $160.00 | −$31.34 / −16.38% | Today −$30. ITM (TERRY 9/26). The 7/18 *"rides to expiry"* ruling stands as written but its premise failed — **card `MGMT-HBAN16P-OCT16`**, re-rule options for Will by **Wed 10/14** (WQ-302). 21 DTE |

## Robinhood — satellite account (Individual)

> **Home card 9/27 (weekend ⇒ 9/25 close): account $228.15, BP $8.94** `[RH card 9/27]` — was $454.33 / $129.37 at the 9/16 capture ⇒ −$226.18; **BP −$120.43 unattributed (D-59)**. Per-line cost/value DERIVED from shown P/L ÷ P/L% (no Mark column ⇒ machine class `unverified` by design). **Prediction market:** Nithya Raman "Yes" 26.22 @ 58¢ ≈ $15.21 (+65.71% ⇒ cost ≈$9.18, derived; was 36¢ on 9/10) — recorded, not adjudicated. **Not on the card:** USO $159C Sep-11 (dead by date, disposition UNBOOKED — D-58) and the 9/16 capture's QQQ $713C / USO $165C Sep-16 (D-57).

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **WAL $70P** | **Dec-18-2026** | 1 | **$2.20 ($220)** — card-derived $219.92 ✓ | ≈$203.00 *(derived)* | ✅ **ON CARD 9/27 — −$17.00 / −7.73%** | TRY-WAL-ROLL70 (filled in Robinhood). Guard **`GATE-TERRY-ROLL70-EXIT`** *"WAL OFFICIAL CLOSE ≥ $81.90 on THREE CONSECUTIVE sessions"* — **0-of-3 as last graded** (REGINALD through 9/23, per TERRY STATUS 9/24); clause (d) REGINALD CONCUR `377b595ce`. Not adjudicated here (rule 7). **$4.40 GTC sell order: CANCELLED / not there — Will 9/28** (answer *"Cancelled / not there"* in WAL's session; `PROME/inbox/processed/2026-09-28_from-WAL_WQ-324-325-ruled-verbatim-and-4.40-GTC-cancelled.md`; supersedes the WQ-167 "permanently UNKNOWN") ⇒ **no resting exit order; any take-profit is Will's manual act.** Qty ×1 unchanged. Time stop Fri 12/4. 84 DTE at 9/25. **D-47** |
| **KRE $25P** | 1/15/2027 | 1 | $53.00 — card-derived ✓ | ≈$1.00 *(derived)* | ✅ **ON CARD 9/27 — −$52.00 / −98.11%** | Deep-OTM lottery; entry pre-7/16, never recorded — **D-54**. 112 DTE |
| T | stock | 1 | — | — | ⚠️ no stocks card 9/27; the card closes to the cent with no stock line ⇒ not held (INFERRED; needs BP = cash) | Hypothesis: sold, unconfirmed — **D-20** |

## Account UNATTRIBUTED — receipted fills not yet attributed to an account

*No rows. VLO ×1 (this section's only row since 9/19) moved to § Fidelity — Longs on the 9/25 ledger (D-55 account leg CLOSED). The section stays as the landing place for a receipt that names no account (the parser admits it — TERRY `cfd9b9115`).*

---

## ⚠️ Reconcile discrepancies (9/25-close reconcile, built 2026-09-27; amended by the 9/28 fills pass)

> Built against the 9/25 CLOSE Fidelity positions + Activity 9/04→9/25 + the RH card 9/27. **Nothing resolved by invention; every conjecture labeled; broker view > Will's word > desk record.** Ranked by decision urgency, expiring first; "Will decides" vs "owner decides" separated. **Permanently UNKNOWN by WQ-167 (never asks):** the 9/2 USO 135C sale price. *(The ROLL70 $4.40 GTC status left this list 9/28 — Will volunteered it: CANCELLED / not there; D-47.)* **One standing gap, not re-asked per row:** fill TIMES and per-share prices for every ledger row (the view's rows are collapsed). Prior D-row text → `_archive/STATUS_ROTATION_2026-09-27.md` Chunk C.

### EXPIRING WED 2026-09-30 (after the 9/28 fills: Tue 9/29 · Wed 9/30 remain; hard stop for further sales Wed 9/30 15:00 ET — WQ-316)

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| — | **QQQ $730P Sep-30 ×9** `[9/28 fills receipt]` — card (rec, not rule); WQ-316 open | 🔴 2 sessions | Bought 9/24 −$2,486.63 (row 2); $1.30 / −47.73% at the 9/25 close on ×10. **9/28: 1 of 10 SOLD @ $1.98, net $197.34** (receipt; time/account → D-61). TERRY card `f2964be4e` rec SELL all; WQ-316 awaits Will's explicit sell/hold on ×9 | None on the position. A 1-of-10 sale is a partial (root rule #7 frames trims) — recorded, not adjudicated. Expiry-day mechanics → D-60 | **Will** (his hand; WQ-316) |
| — | **USO $159C Sep-30 ×2** — $130 at 9/25c; card (rec, not rule); WQ-316 open | 🔴 2 sessions | Bought 9/18 −$921.33 (row 8); $0.65 / −85.89% at 9/25c. **NOT sold 9/28** (receipt). TERRY card `f2964be4e` rec SELL | — | **Will** (his hand; WQ-316) |
| **D-60** | **Fidelity expiry-day "OPTION LIQUIDATION" rows — mechanism UNKNOWN** | 🟠 bears on all four Sep-30 lines (after 9/28: QQQ 730P ×9 · TLT 77P ×15 · USO 159C ×2 · KRE 60P ×2) | Four rows read *"YOU SOLD CLOSING TRANSACTION OPTION LIQUIDATION"* on the contract's own expiry day: IWM 293P 9/04 +$1.97 · QQQ 716P 9/08 +$0.99 · QQQ 710P 9/18 +$3.77 · QQQ 730P 9/25 +$1.97. One contract EXPIRED instead (QQQ 716P Sep-21, row 3) | **Hypothesis:** the broker closes some expiring options itself on expiry day; the description text is the only evidence and what decides liquidate vs expire is UNKNOWN. Same class of broker-mechanics unknown as the WQ-302 cards' ITM-IRA-put question | **Will** — ask Fidelity alongside the WQ-302 question |
| **D-31** | **TLT $77P Sep-30 ×15 `[9/28 fills receipt]` — HOLD (WQ-168 ④ / WQ-217); quantity changed, posture not** | 🟡 ruled | **9/28: 5 of 20 SOLD @ $0.06, net $28.45** (receipt; time/account → D-61) — the **second** recorded hand-deviation from HOLD-to-expiry (first 9/10, 5 @ net $28.43). Harvest line ≥$0.3469 fees-in NOT reached ($0.06 = 0.52×; salvage, not harvest). At 9/25c: $0.04 / $80 on ×20 (0.35×). `GATE-TERRY-007` MOOT ⇒ NO-VERDICT 9/24; NO ADD (WQ-280) unaffected | Nothing — the ×15 rides to expiry unless the harvest line prints or Will sells by hand again. The PB-0002b "10 ct" harvest size was written on ×20 — TERRY's to re-read, not ANVIL's | TERRY watches harvest → Will executes; TERRY records the 9/28 fill on card 004 (its 9/30 wake) |
| WQ-168 ⑥ | **KRE $60P Sep-30 ×2 — LAPSE** | 🟡 ruled | $0.02 / $4.00 (−99.12%) | Nothing | Rides to $0 |

### Will decides — facts owed (no same-week expiry)

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| WQ-302 | **TLT $82P Oct-16 ×1 `[9/28 fills receipt]` + HBAN $16P Oct-16 ×2 — ITM; cards on file** | 🟠 Wed 10/14 close | At 9/25c: TLT $604 on ×2 (+80.11%), HBAN $160 (−16.38%); ×2 each CONFIRMED on the 9/25 view (the account's IRA identity is still INFERRED). **9/28: TLT 82P 1 of 2 SOLD @ $3.60, net $359.34, filled 09:47:23 ET — before any card choice** (WQ-292 / WQ-302); card `MGMT-TLT82P-OCT16` was built on ×2 | — (the cards carry the options; whether the ×1 changes the card's options is TERRY's re-read, not adjudicated here) | **Will** chooses; TERRY cards |
| **D-61** 🆕 | **9/28 fills — fill TIME + ACCOUNT not in the paste for QQQ 730P ×1 and TLT 77P ×5; account not named for TLT 82P ×1 either** | 🟡 (no decision rides on it; cash refresh does) | Receipt gives date, qty, limit = fill price and net for all three; order 09:43:29 / fill 09:47:23 ET + order no. only for TLT 82P. Implied deductions (gross − net, arithmetic): $0.66 · $1.55 · $0.66 — recorded, not checked against a fee schedule. TLT 82P's execution line reads $359.99 vs 1 × 100 × $3.60 = $360.00 — recorded as seen | **Account = Fidelity IRA, INFERRED** (only mirrored account holding the three contracts; quantities matched; "Trade type Cash"). The 9/28 cash (+$585.13 net, arithmetic) is not in the header until a broker view shows it settled | **Will** — the Fidelity Activity view (same scroll as D-45/D-44) |
| **D-59** 🆕 | **Robinhood buying power −$120.43 (9/16 → 9/27) with no line to show for it** | 🟠 | BP $129.37 → $8.94; account $454.33 → $228.15; lines ≈$324.96 [9/16] → ≈$219.21 [9/27] | An expiry does not lower BP ⇒ a purchase since closed/expired, a transfer out, or BP ≠ cash. ANVIL picks none | **Will** — Robinhood history view |
| **D-57** | **RH Sep-16 QQQ $713C / USO $165C (9/16 capture) — disposition** | 🟠 | Absent from the 9/27 card; past their date ⇒ not held. The mirror never held them (its 713C was Sep-10, its 165C the Sep-18 spread leg) | Sold / expired / a 9/16 misread — ANVIL picks none; **never book "expired" at $0** | **Will** — RH history |
| **D-58** (RH leg) | **RH USO $159C Sep-11 ×1 — dead by date; disposition UNBOOKED** | 🟡 | Bought 9/10 @ $1.52 (card +$64 at 9/10 16:10); absent 9/16 and 9/27. TERRY's refiner card lists it *"expired/closed 9/11 — GONE"* — a desk record, not a broker row | Expired OTM or sold 9/11 — unknown; realized ≠ $0 by default | **Will** — RH history |
| **D-45** (residual) | **Fidelity cash 9/3 ~15:07 → the 9/04 ledger rows: −$85.33 unattributed** | 🟡 | 9/3 capture cash $18,025.71; ledger opening before row 26 = $17,940.38 (derived). Of the old −$190.35, **−$105.02 is now attributed** (IWM liq +$1.97 · QQQ 716P −$199.66 / +$0.99 · XLE +$169.34 · USO 153C −$77.66) | Candidate: the IWM 293P Sep-04 entry (liquidated 9/04 for $1.97; never on any mirror) — labeled, not a fill | **Will** — Activity scrolled to 9/03 |
| **D-44** | **QQQ 3 sh — gone by 9/3; sale date/price UNKNOWN** | 🟡 | 8/28: 3 @ $716.43; the ledger view is cut at 9/04 | SOLD 8/28–9/03 (labeled) | **Will** — same scroll-back |
| **D-55** (residual) | **VLO fill TIME** | 🟡 | Account CLOSED this pass (Fidelity, row 7); date 9/18 only | — | Will (order detail), low |
| **D-28** | **RH QQQ $715P ×1 — expired 8/31, outcome UNRECORDED** | 🟡 carried | Cost ≈$193.24; QQQ 716.43 on 8/28; ≈+$68 unattributed in the 8/28→9/10 RH bridge | Expired OTM / sold / exercised — none verified | RH history |
| **D-18** | **RH WAL $77.5P Aug-21 — sale CONFIRMED 8/18, P&L UNRECORDED** | 🟡 carried | Existence closed 8/18 | Do not book at $0 | Will (not urgent) |
| **D-54** | **RH KRE $25P Jan-15-2027 — entry never recorded** | 🟡 carried | Cost $53.00 derived; on the mirror since 7/16 | Entry pre-7/16 ≈$0.53 — a derivation | Will |
| **D-20** | **RH T share — absent; event contracts** | 🟡 carried | Card closes to the cent with no stock line ⇒ not held (INFERRED) | Sold, unconfirmed | Will — full RH view |
| **D-37** | **RH ≈$360 inflow (8/14→8/28) + "13 days left" banner** | 🟡 carried | Arithmetic recorded 8/29 | Deposit/transfer; banner referent unknown | Will (one line) |
| **D-17** | **STNG — in no capture, nowhere in FORGE** | 🟡 carried | Absent since 8/2; March-2026 record only | Recalled March position / closed pre-7/30 / a third account | Will — one line |
| **D-1** | **AAPL 5-sh sale pre-7/30 — date + price unrecorded** | 🟡 carried | Predates the 7/30–8/28 window | ~$565 cash class | Will / an older window |

### Owner decides — ruled / gated (nothing owed by Will today)

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-47** | **RH WAL Dec-18 $70P ×1 — `GATE-TERRY-ROLL70-EXIT`** | 🟡 84 DTE at 9/25 | ≈$203 derived (−7.73%) `[RH card 9/27]`; 0-of-3 through 9/23; time stop 12/4. **$4.40 GTC sell order: CANCELLED / not there — Will 9/28** (answer *"Cancelled / not there"* to WAL's in-session question; WAL packet `PROME/inbox/processed/2026-09-28_from-WAL_WQ-324-325-ruled-verbatim-and-4.40-GTC-cancelled.md`, WAL `00b5b72c3`). Position ×1 unchanged | Nothing conjectured. When/why it was cancelled is not in the answer — not asked (the WQ-167 never-ask stands for the history) | **Harvest = Will's manual act** (no resting order); REGINALD grades / TERRY proposes; TERRY records on the ROLL70 card |
| VLO-SCALE | **2 staged VLO sh** | 🟡 review_by 10/14 | 9/25 NOT MET; F1 UNKNOWN (CME settle read = Will) | — | TERRY grades → Will |
| WQ-200 | **USO 37 sh — no line live** | ⚪ | Card DECLINED 9/10; $148.33 at 9/25c informational | — | Will's hand |
| — | **APD thesis tag** | ⚪ | Unassigned since 7/30 | — | PROME / Will |

### RESOLVED this pass (receipts = Activity rows; full ticket table → rotation record)

- **9/28 fills pass — D-47's GTC leg → RESOLVED:** $4.40 GTC CANCELLED / not there (Will 9/28, WAL packet above); D-47 itself stays open (the gate and the position are live). Three partial sales recorded on their rows (QQQ 730P ×10→9 · TLT 77P ×20→15 · TLT 82P ×2→1); USO 159C unchanged ×2. Open gaps → D-61.

- **D-49 → CLOSED:** the FIRST XLE $65C sold **9/09, net +$169.34** (row 22; ≈$1.70/ct INFERRED) ⇒ −$58.33 vs lot $227.67; with 9/11 +$150.34 (row 15, −$77.33) the XLE line realized **−$135.66**. It sold on WQ-168 ⑦'s day; whether ⑦'s condition held is not adjudicated here.
- **D-53 → CLOSED:** USO $153C entry **9/09, −$77.66** (row 20); exit 9/10 +$213.34 ⇒ **+$135.68**.
- **D-56 → CLOSED (dates + nets):** all **9/15** — AAPL SOLD +$1,653.14 · TBT SOLD +$158.96 · GLD BOUGHT −$393.00 (rows 14/13/12). Qty −5/−4/+1 INFERRED (9/16 delta), corroborated by the basis deltas. The old labeled −$4.29 residual is gone: Σ nets +$1,419.10 = ledger 9/11 → 9/15 cash change exactly.
- **D-55 account leg → CLOSED:** Fidelity (row 7 + positions view).
- **D-58 Fidelity leg / WQ-168 ①② → CLOSED:** WAL $70P + $67.5P EXPIRED as of 9/18 (rows 4–5) ⇒ **−$1,519.34** realized.
- **TLT 77P ×5 9/10 net → $28.43** (row 18; mirror had $28.44) ⇒ −$29.39. **D-45 → partial** (above).
- **9/19 consumer sweep (Account UNATTRIBUTED unparsed) → CLOSED** by TERRY `cfd9b9115` (parser admits the section — re-run 9/27). The pre-existing XLE "qty 0" live emission is gone with the row's rotation.

---

## Immediate Actions (9/27 reconcile state + 9/28 fills)

| Item | State | Owner |
|---|---|---|
| 🔴 **Four Sep-30 lines expire Wed 9/30 (quantities after the 9/28 fills):** QQQ 730P ×9 (no rule; WQ-316 open) · USO 159C ×2 (no rule; WQ-316 open) · TLT 77P ×15 (HOLD) · KRE 60P ×2 (LAPSE) — plus **D-60** (broker expiry-day liquidation). **Hard stop for further sales Wed 9/30 15:00 ET** | 2 sessions | **Will** (hand) / TERRY (77P harvest watch; re-reads quotes Wed AM) |
| 🟠 **WQ-302** TLT 82P (now ×1) + HBAN 16P (×2) choices by Wed 10/14; the one Fidelity question also answers D-60 | dated | **Will** |
| 🟠 **Robinhood history view** — D-59 · D-57 · D-58 RH · D-28 · D-18 · D-54 · D-20 · D-37 | one view | **Will** |
| 🟡 **Fidelity Activity scrolled to 9/03 and before** — D-45 residual · D-44 · D-1 · D-17; **the 9/28 rows in the same view close D-61** (time + account of the QQQ 730P / TLT 77P sales) and refresh cash | one view | **Will** |
| 🟡 VLO staged 2 sh (VLO-SCALE) · USO 37 hand-managed · APD tag | carried | TERRY / Will / PROME |

---

*History → `_archive/JOURNAL.md` | Prior reconciles (9/20 standing write-in, 9/10, 9/3, 8/29, 8/14, 8/2, 7/30, 7/20, 7/16, 5/21) in git history + `_archive/` | Full-portfolio Feb snapshot → `PORTFOLIO.md` (**FROZEN/superseded, historical only — never cite as live**) | Position truth = Will/broker direct (off-repo) | Marks-of-record transcription → `PROME/data/2026-09-27_broker-capture-TRANSCRIPTION.md` (Fidelity 9/25 CLOSE + Activity 9/04→9/25 + RH card 9/27)*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumers: `AGENTS/TERRY/scripts/positions_from_forge.py` (sections `^## (Fidelity|Robinhood)` + `^## Account <NAME>`; table headers by prefix; cell text — emphasis and strikethrough visible) · `PROME/tools/desk_attention.py` `holdings()` (same sections; `Qty` + `Ticker|Strike|Position` headers; expiry year from `**Updated:**`) · `PROME/tools/will_brief.py` `parse_money()` (header before the first `## `: `account total:**`, `money market):** $X (Y%)`, `**Updated:** YYYY-MM-DD`, `marks = [Fri ]YYYY-MM-DD`) · `FORGE/position_management.tsv` `source_sha256` (any byte change here withholds every mapping sourced to this file until PROME re-reviews) · `AGENTS/BRENT/scripts/pending_receipts.py` (text-level closure candidates). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself here in the same commit that starts parsing. *(9/27 pass: header money line RESTORED to the shape `will_brief.py` reads — it returned None on the 9/20 header; option expiries carry the year (a year-less "Sep-30" parses as 2027 from 10/1 in `positions_from_forge.py`); new table in § Off-thesis; VLO moved § Account UNATTRIBUTED → § Fidelity — Longs; WAL and RH-Sep-11 rows rotated. Parser receipts in the ANVIL report.)* *(9/28 fills pass: no structural change. The `**Updated:**` date token stays the last BROKER-VIEW date (9/27) because `will_brief.py` renders it as "Broker export <date>" and `desk_attention.py` as "<date> broker positions"; a fills receipt is neither. Value = `—` and P&L = `see note` on the three sold-down rows (QQQ 730P · TLT 77P · TLT 82P) ⇒ `value` None in `positions_from_forge.py`, by design until a broker mark at the new qty exists.)*
