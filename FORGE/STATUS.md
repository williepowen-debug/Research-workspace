# FORGE — Trading Operations

Dashboard management mapping → [position_management.tsv](position_management.tsv); maintenance contract → [dashboard notes](DASHBOARD.md). Holdings remain in this file; approval, order and fill evidence are separate. A changed evidence source invalidates its management mapping until reviewed.

> ✅ **2026-09-30 (Wed) — RECONCILE BY ANVIL to Will's POST-CLOSE captures (posted 18:31 ET): stock marks = the 9/30 CLOSE `[9/30c]`; option marks = Fidelity's post-close marks `[9/30 post-close]` (⚠️ the three KRE Dec lines read $0.01 — a post-close mark, NOT a valuation: D-67).** Source `PROME/data/2026-09-30_broker-capture-TRANSCRIPTION.md` (PROME's transcription of two screenshots): **Fidelity positions** · **Fidelity Activity & Orders, Sep-30-2026 (14 rows: 9 filled, 5 Verified Canceled; per-share fill + net amount; NO fill time)**. ANVIL re-verified from the tables (no image access): value = last × qty (×100) ✓ and G/L = value − basis ✓ on 15 of 15 rows; Σ positions $22,290.87 + cash $18,102.04 + pending −$4,007.98 = **$36,384.93 to the cent** ✓; Σ Today +$753.44 ✓; Σ G/L +$2,837.63 ✓; the 9 filled rows net −$4,007.98 = Pending ✓; new-line bases = fill × qty × 100 + fees ✓ (4 of 4). 6 broker % cells differ from recomputation by 0.01 — broker rounding; shown values kept. **Quantities: 4 GONE (SOLD TO CLOSE 9/30 — NOT expired, NOT lapsed) · 4 NEW · 11 Fidelity rows MARK ONLY** (bases unchanged to the cent vs the 9/29 mirror). Robinhood NOT captured 9/30 — its 9/29 card stands. Prior header + discrepancy list (9/29 build) → `git show b983d745a:FORGE/STATUS.md`.
>
> ⚠️ **ACCOUNT SCOPE — Fidelity: ONE account, Traditional IRA *****1326 (Activity view header); the positions view's header is out of the crop ⇒ same account INFERRED by position-set match. Robinhood Individual: NOT in this capture — rows carried from the 9/29 card, unverified today.** Rows absent from a view are retained and flagged; a dated contract past its own expiry leaves the live tables, its disposition UNBOOKED unless a broker row shows it.
>
> **Updated:** 2026-09-30 = last broker-view reconcile (the date token machine consumers read as the export vintage — see footer) · marks = 2026-09-30 post-close (stocks `[9/30c]`, options `[9/30 post-close]`) · **Fidelity cash (money market):** $18,102.04 (49.75%) + **Pending activity −$4,007.98** (the 9/30 fills, to the cent; cash after settlement ⇒ $14,094.06, derived) · **Fidelity account total:** $36,384.93 (Today +$753.44 / +2.11%; open G/L +$2,837.63 / +14.59%) — was $36,822.87 `[9/29 13:4x intraday]` ⇒ −$437.94 (an INTRADAY base — not a close-to-close move). ⚠️ Fidelity's "Today" counts the four NEW lines' whole since-fill P&L (+$964.05, of which −$335.33 is the KRE 65P $0.01 mark) and nothing for the four sold lines · **Realized 9/30:** −$3,755.12 on the four sold lines vs broker basis (§ Reconcile discrepancies › CLOSED) · **Robinhood:** $295.15 / BP $8.94 `[9/29 13:4x intraday]` — not re-captured. Earlier rotations → `_archive/STATUS_ROTATION_2026-09-29.md`, `…_2026-09-27.md`, `…_2026-09-20.md`, `…_2026-09-10.md`, `_archive/RECONCILE_2026-08-29_RECORD.md`.

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (7/18 re-base + amendment #1 = current). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All cells `[9/30c]` (Fidelity positions, post-close; stock last = the 9/30 close per PROME's transcription ①); "ledger <date>" = the 9/29 transcription's Activity table ③. All six MARK ONLY 9/30.*

| Ticker | Type | Qty | Cost | Mark 9/30 | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | 10 | $23.65 | $333.02 | $3,330.20 | +$3,093.75 / +1,308.41% | Today +$36.20. **SOLD 9/15, net +$1,653.14** (ledger 9/15) — −5 sh INFERRED from the 9/16 capture delta (ledger shows no qty); basis $354.67→$236.45 ⇒ $118.22 sold ⇒ ≈+$1,534.92 realized (derived). Pre-7/30 5-sh sale = D-1 |
| GLD | Stock | 17 | $374.74 | $380.84 | $6,474.28 | +$103.78 / +1.62% | Today −$34.85. **BOUGHT 9/15, net −$393.00** (ledger 9/15); basis $5,977.50 + $393.00 = $6,370.50 exact ⇒ +1 sh (qty INFERRED). MIDAS domain; largest line |
| USO | Stock | 37 | $122.28 | $145.66 | $5,389.42 | +$865.15 / +19.12% | Today +$85.47. **WQ-200 DECLINED by Will 9/10 — NO harvest/give-back rule live; Will manages by hand.** BRENT thesis (Hormuz-gap entry) |
| VLO | Stock | 1 | $412.00 | $387.61 | $387.61 | −$24.39 / −5.92% | Today −$0.11. **BOUGHT 9/18, −$412.00, in THIS account** (ledger 9/18 + positions view; fill TIME not shown — D-55). WQ-213: 1 of 3; **2 sh STAGED under `GATE-TERRY-VLO-SCALE`** (TERRY grades; 9/25 NOT MET, F1 UNKNOWN — TERRY STATUS 9/25). **Exit rule on the held share: `GATE-TERRY-VLO-HELD-01` REGISTERED 9/28 18:36 ET (WQ-330, Will "both"): Nov crack settlement < $90.16 ⇒ sell rec (< $95 notice); signed US distillate export-restriction text at primary ⇒ SELL at the next regular session (Will may act without the desk; TERRY recs if he has not); A: TERRY grades, Will executes; not adjudicated here (rule 7)** |
| APD | Stock | 2 | $294.79 | $278.23 | $556.46 | −$33.11 / −5.62% | Today −$1.92. Broker shows a "(D)" badge — recorded, not interpreted. Thesis tag unassigned since 7/30 |
| TBT | Stock | 10 | $34.65 | $42.49 | $424.90 | +$78.44 / +22.64% | Today +$4.60. **SOLD 9/15, net +$158.96** (ledger 9/15) — −4 sh INFERRED; basis $484.82→$346.46 ⇒ $138.36 sold ⇒ ≈+$20.60 realized (derived). Duration-short leg (BOND/TERRY); no management rule |

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

*No live event-box rows — the VIX $20C/$25C spread (CLOSED 2026-07-30, realized −$111.60) and the five Aug-21-2026 EXPIRED rows (realized −$2,816.72 total) are terminal → rotation records.*

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, owned by no agent — recorded so it is not invisible. **All three rows are NEW 9/30 (Will's rolls, *"I rolled the puts"* 18:27 ET) and have NO card and NO management rule** — WQ-347 carries Will's hand on the two QQQ lines; TERRY writes their card at its next touch. Terminal 9/30 (Activity 9/30, "row n" = transcription ②): **QQQ $730P Sep-30 ×9 SOLD TO CLOSE @ $0.01, net +$8.43 (row 10) ⇒ −$2,229.54** vs broker basis $2,237.97 (lot from 10 bought 9/24 −$2,486.63; 1 sold 9/28 +$197.34 ⇒ campaign −$2,280.86) · **USO $159C Sep-30 ×2 SOLD TO CLOSE @ $0.01, net +$1.87 (row 5) ⇒ −$919.46** vs $921.33. Both NOT expired; WQ-316 answered by Will's roll (TERRY card `f2964be4e` was a SELL rec). Terminal tickets 9/04–9/25 → `_archive/STATUS_ROTATION_2026-09-27.md` § Ticket record.

| Ticker | Strike | Expiry | Qty | Cost | Mark 9/30 | Value | P&L | Note |
|--------|--------|--------|-----|------|-----------|-------|-----|------|
| QQQ | $740P | Oct-01-2026 | 9 | $1.93 | $2.97 | $2,673.00 | +$939.03 / +54.15% | `[9/30 post-close]`. **NEW 9/30: BOUGHT ×9 @ $1.92, −$1,733.97 (row 11; fees $5.97 derived)** — leg 2 of a net-debit roll with row 10 (limit $1.91; attempts at lower debits not shown for this pair). **⚠️ EXPIRES THU 10/01 — ITM at the 9/30 close** (QQQ $739.77 `[9/30c]` per PROME/TERRY, not in the capture ⇒ $0.23 ITM). Exercise of ×9 = a sale of 900 QQQ at $740 ($666,000) the IRA does not hold — handling UNOBSERVED (D-60). No card · WQ-347 (Will). 1 DTE |
| QQQ | $735P | Oct-05-2026 | 5 | $2.74 | $3.52 | $1,760.00 | +$391.68 / +28.62% | `[9/30 post-close]`. **NEW 9/30: BOUGHT ×5 @ $2.73 limit, −$1,368.32 (row 13; fees $3.32 derived)**; a lower $2.52 limit Verified Canceled (row 14). Single-leg order — not paired with a sale on the ledger. Size ADDED: 14 QQQ puts across two lines vs 9 before. $4.77 OTM at the 9/30 close. No card · WQ-347. 5 DTE (Mon 10/05) |
| USO | $150C | Oct-09-2026 | 2 | $3.00 | $2.84 | $568.00 | −$31.33 / −5.23% | `[9/30 post-close]`. **NEW 9/30: BOUGHT ×2 @ $2.99, −$599.33 (row 6; fees $1.33 derived)** — leg 2 of a net-debit roll with row 5 (limit $2.98). USO $145.66 `[9/30c]` ⇒ $4.34 OTM. No card, no rule. ⚠️ Not the stock line (USO 37 sh, § Longs) — PROME's transcription flags WQ-297 A (one oil bet); not adjudicated here. 9 DTE (Fri 10/09) |

## Fidelity — Thesis Puts

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

*TLT $77P Sep-30 ×15 (TRY-FIRE-004's last lot): **SOLD TO CLOSE 9/30 — NOT held to expiry** — 10 @ $0.01 net +$9.37 (row 9) + 5 @ $0.02 net +$9.43 (row 12) = **+$18.80 ⇒ −$154.64** vs broker basis $173.44; no replacement TLT line. **Third recorded hand-deviation from the WQ-168 ④ / WQ-217 HOLD-to-expiry** (9/10 · 9/28 · 9/30) — recorded, not adjudicated. Harvest line *"half at ≥3×"* (≥$0.3469 fees-in) was never reached (last sales $0.01/$0.02); `GATE-TERRY-007` MOOT 9/24. D-31 CLOSED; TERRY's surfaces read "expired worthless" — D-68.*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $82P | Oct-16-2026 | 1 | $1.68 | $4.60 | $460.00 | +$292.33 / +174.34% (today +$45) `[9/30 post-close]`. MARK ONLY; broker basis $167.67. 9/28: SOLD 1 of 2 @ $3.60, ledger +$359.34 = receipt (order 09:43:29, filled 09:47:23 ET) ⇒ **+$191.66** vs the $167.68 lot. ITM (TERRY 9/26). **Card `MGMT-TLT82P-OCT16`** (TERRY `40e12ee0a`, built on ×2; the sale came before Will's management choice — WQ-292 / WQ-302); Will's A/B/C by **Wed 10/14 close** now concerns ×1. ⚠️ +174.34% (2.74× basis) is a mark — the card's options are a CHOICE (A harvest · B hold to expiry · C hold then sell by 10/14), not a price trigger; nothing fired (rule 7). ITM-expiry handling in the IRA = named UNKNOWN on the card, UNOBSERVED in the ledger (D-60). 16 DTE |

### KRE — regional banks (REGINALD)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
*All three rows `[9/30 post-close]` at $0.01 — ⚠️ a post-close mark, NOT a valuation (−98% on the day vs KRE −0.56%; $0.46 `[9/29 13:4x intraday]`; the 65P filled at $1.68 the same day) — **D-67**. KRE $60P Sep-30 ×2: **SOLD TO CLOSE 9/30 @ $0.01, net +$1.87 (row 1) ⇒ −$451.48** vs broker basis $453.35 — WQ-168 ⑥ had ruled LAPSE; sold instead as leg 1 of the roll into the Dec-31 65P (recorded, not adjudicated).*

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $60P | Dec-18-2026 | 2 | $2.57 | $0.01 | $2.00 | −$511.34 / −99.62% (today −$104). MARK ONLY. 79 DTE |
| $60P | Dec-18-2026 | 3 (M) | $2.93 | $0.01 | $3.00 | −$875.02 / −99.66% (today −$156) — Fidelity multi-lot marker; **five** Dec-18 KRE 60P across the two lots. MARK ONLY. 79 DTE |
| $65P | Dec-31-2026 | 2 | $1.69 | $0.01 | $2.00 | −$335.33 / −99.41% — **NEW 9/30: BOUGHT ×2 @ $1.68, −$337.33 (row 2; fees $1.33 derived)**, leg 2 of a net-debit roll with row 1 (limit $1.67 filled; $1.63 and $1.55 attempts Verified Canceled, rows 3–4 / 7–8). Will's own add — TERRY's conditional KRE card (`4ad672c43`) read NOT constructible today (PROME's transcription ⑤); **no card on this line**. Duration roll of the Sep-30 60P ×2 (root rule #7 form; strike moved 60→65). 92 DTE |

### WAL (REGINALD) — Sep-18 pair EXPIRED

*$70P + $67.5P Sep-18 ×1 each: **EXPIRED as of 9/18, broker-confirmed** (ledger rows posted 9/21) ⇒ realized **−$768.67 and −$750.67 = −$1,519.34** (full basis) — the WQ-168 ①② LAPSE as ruled. Rows → rotation record. Duration roll = the Robinhood WAL Dec-18 $70P ×1 below. The RH WAL $77.5P Aug-21 sale: P&L UNRECORDED — D-18.*

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18-2026 | 1 | $11.85 | $1.20 | $120.00 | −$1,064.67 / −89.88% | `[9/30 post-close]` MARK ONLY. BROCK thesis vehicle; today −$15; 79 DTE. Will ruled HOLD 2026-08-13 (`PROME/proposals/2026-08-13_private-credit-batch-RULED.md` §②; BROCK owner; vehicle-mismatch flag live) |
| HBAN | $16P | Oct-16-2026 | 2 | $0.96 | $0.70 | $140.00 | −$51.34 / −26.84% | `[9/30 post-close]` MARK ONLY. Today −$70. ITM (TERRY 9/26). The 7/18 *"rides to expiry"* ruling stands as written but its premise failed — **card `MGMT-HBAN16P-OCT16`**, re-rule options for Will by **Wed 10/14** (WQ-302). 16 DTE |

## Robinhood — satellite account (Individual)

> ⚠️ **NOT CAPTURED 9/30 — every cell below is the 9/29 card, unverified today.** **Home card 9/29 intraday: account $295.15 (Today +$35.00 / +13.45%), BP $8.94** `[9/29 13:4x intraday]` — was $228.15 / $8.94 `[RH card 9/27]` ⇒ +$67.00. Lines + BP = $290.15 ⇒ **$5.00 UNEXPLAINED (D-64)**. Per-line cost/value DERIVED from shown P/L ÷ P/L% (no Mark column ⇒ machine class `unverified` by design). **Prediction market:** Nithya Raman "Yes" 26.22 @ 58¢ ≈ $15.21 (+65.71% ⇒ cost ≈$9.18, derived — price and % identical to 9/27) — recorded, not adjudicated. **Recent activity 9/01→9/25 books the dead-by-date lines:** USO $159C Sep-11 (bought 9/10 $152, expired $0 — D-58) · QQQ $713C Sep-16 (bought 9/16 $167) + USO $165C Sep-16 (bought 9/14 $150), both expired $0 (D-57).

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **WAL $70P** | **Dec-18-2026** | 1 | **$2.20 ($220)** — bought 9/02 @ $2.20 (RH activity) ✓ | ≈$265.00 *(derived; mark ≈$2.65)* | ✅ **ON CARD 9/29 — +$45.00 / +20.45%** | TRY-WAL-ROLL70 (filled in Robinhood). Guard **`GATE-TERRY-ROLL70-EXIT`** *"WAL OFFICIAL CLOSE ≥ $81.90 on THREE CONSECUTIVE sessions"* — **0-of-3 as last recorded here** (REGINALD through 9/23, per TERRY STATUS 9/24; not re-read this pass). The option's +20.45% is not the gate — the gate reads WAL's close (rule 7). **$4.40 GTC sell order: CANCELLED / not there — Will 9/28** (`PROME/inbox/processed/2026-09-28_from-WAL_WQ-324-325-ruled-verbatim-and-4.40-GTC-cancelled.md`) ⇒ **no resting exit order; any take-profit is Will's manual act.** Time stop Fri 12/4. 79 DTE. **D-47** |
| **KRE $25P** | 1/15/2027 | 1 | $53.00 — card-derived ✓ | ≈$1.00 *(derived)* | ✅ **ON CARD 9/29 — −$52.00 / −98.11%** | Deep-OTM lottery; entry pre-7/16, never recorded — **D-54** (before the 9/01 activity view). 107 DTE |
| T | stock | 1 | — | — | ⚠️ no stocks card 9/29; no T row in RH activity 9/01→9/25 | Hypothesis: sold before 9/01, unconfirmed — **D-20**. The card no longer closes to the cent (D-64), so the 9/27 "no stock line" inference is weaker |

## Account UNATTRIBUTED — receipted fills not yet attributed to an account

*No rows. VLO ×1 (this section's only row since 9/19) moved to § Fidelity — Longs on the 9/25 ledger (D-55 account leg CLOSED). The section stays as the landing place for a receipt that names no account (the parser admits it — TERRY `cfd9b9115`).*

---

## ⚠️ Reconcile discrepancies (9/30 post-close reconcile, built 2026-09-30)

> Built against the Fidelity positions (post-close 9/30) + Fidelity Activity & Orders Sep-30-2026 (transcription ②, "row n"). Robinhood not captured. **Nothing resolved by invention; every conjecture labeled; broker view > Will's word > desk record.** Ranked by decision urgency, expiring first. **Permanently UNKNOWN by WQ-167 (never asks):** the 9/2 USO 135C sale price. **One standing gap, not re-asked per row:** fill TIMES for every Fidelity ledger row (neither view shows them — D-66 for 9/30). Prior list (9/29 build) → `git show b983d745a:FORGE/STATUS.md`.

### EXPIRING — Thu 10/01 → Fri 10/16 (no card on the first three lines)

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| WQ-347 | **QQQ $740P Oct-01 ×9 — EXPIRES THU 10/01, ITM at the 9/30 close** | 🔴 1 session | Bought 9/30 @ $1.92, −$1,733.97 (row 11); $2.97 / $2,673.00 / +$939.03 `[9/30 post-close]`. QQQ $739.77 `[9/30c]` (PROME/TERRY, not in the capture) ⇒ $0.23 ITM. Exercise of ×9 = sell 900 QQQ at $740 ($666,000); the IRA holds 0 QQQ. No card; WQ-347 registered 9/30 (PROME) | ITM or OTM at Thursday's close — unknowable tonight. What Fidelity does to an ITM long put in this IRA → D-60 | **Will** (his hand; WQ-347); TERRY card Thu |
| **D-60** | **Fidelity expiry-day handling — the ITM leg is still UNOBSERVED** | 🔴 bears on the 740P Thu, then 735P Mon, 82P / HBAN 10/16 | OTM leg OBSERVED ×4 (penny "OPTION LIQUIDATION" rows on the expiry day: IWM 293P 9/04 · QQQ 716P 9/08 · QQQ 710P 9/18 · QQQ 730P Sep-25 9/25); three others EXPIRED with no cash row (QQQ 716P Sep-21; WAL 70P + 67.5P Sep-18). **9/30 adds NO observation: all four Sep-30 lines were SOLD by Will before the close** (rows 1, 5, 9, 10, 12) — nothing liquidated, expired or exercised | OTM status of the four liquidations INFERRED from proceeds. **OPEN: (i) an ITM long option at expiry in the IRA; (ii) what decides LIQUIDATE vs EXPIRED — both UNKNOWN** | **Will** — ask Fidelity before Thu 15:00 ET if the 740P is held |
| WQ-347 | **QQQ $735P Oct-05 ×5 — NEW, expires Mon 10/05** | 🟠 3 sessions | Bought 9/30 @ $2.73, −$1,368.32 (row 13; the $2.52 limit Canceled, row 14); $3.52 / $1,760.00 / +$391.68 `[9/30 post-close]`; $4.77 OTM at the 9/30 close. Size ADDED (single-leg buy, not a roll leg on the ledger). No card | — | **Will**; TERRY card |
| — | **USO $150C Oct-09 ×2 — NEW, expires Fri 10/09** | 🟠 9 DTE | Bought 9/30 @ $2.99, −$599.33 (row 6), roll leg with row 5; $2.84 / $568.00 / −$31.33; USO $145.66 `[9/30c]` ⇒ $4.34 OTM. No card, no rule; ANVIL found no WQ row naming it | PROME's transcription ties it to WQ-297 A (one oil bet) — PROME's read, not adjudicated | **Will**; TERRY if asked |
| WQ-302 | **TLT $82P Oct-16 ×1 + HBAN $16P Oct-16 ×2 — ITM; cards on file** | 🟠 Wed 10/14 close | TLT $4.60 / $460.00 (+174.34%), HBAN $0.70 / $140.00 (−26.84%) `[9/30 post-close]`, MARK ONLY. Cards are A/B/C choices, not price triggers | — (×1 re-read of the TLT card = TERRY) | **Will** chooses; TERRY cards |

### Will decides / PROME re-reads — facts owed

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-68** 🆕 | **Other desks' records say "EXPIRED" for lines the broker shows SOLD** | 🟠 record integrity (grades cite them) | Ledger: TLT 77P ×15 SOLD (rows 9 + 12, +$18.80 ⇒ −$154.64); USO 159C ×2 SOLD (row 5, +$1.87 ⇒ −$919.46). TERRY `setups/INDEX.md` TRY-FIRE-004 reads *"EXPIRED WORTHLESS 2026-09-30 … realized −$173.45 on the ×15"*; WQ-316's 17:4x "EXPIRY OUTCOME" (citing TERRY `ee04fbb26`) reads USO 159C *"expired worthless … (−$921.33)"* and "BOTH LEGS EXPIRED OTM". `FORGE/position_management.tsv` rows 8 · 9 · 15 · 16 still describe the four Sep-30 lines as open (hash-withheld until PROME re-reviews; DASHBOARD.md asks for the same pass) | Written from the expiry-time closes before the ledger existed — labeled, not established | **TERRY** (its INDEX/card) · **PROME** (WQ-316 row; TSV re-review) — ANVIL edits neither |
| **D-67** 🆕 | **KRE Dec lines marked $0.01 post-close** | 🟡 valuation, not quantity | All three KRE Dec lines (5 × Dec-18 60P, 2 × Dec-31 65P) read $0.01 / −98% on the day with KRE −0.56%; $0.46 `[9/29 13:4x intraday]`; the 65P filled at $1.68 on 9/30. At the 9/29 mark + the 65P fill ≈$566 would sit in these lines vs $7.00 shown (DERIVED, not a valuation); Σ Today includes −$595.33 of these marks | A bid-less after-hours mark (PROME's read) — UNVERIFIED; a regular-session capture resolves it | **PROME** — next regular-session capture; Will not asked |
| **D-66** 🆕 | **9/30 fill TIMES — none shown for the 9 fills or 5 cancels** | 🟡 | Per-share fills + net amounts are shown; order sequence = row order only | — | Will (order detail), low |
| **D-62** | **Fidelity ledger — $0.45 break in the broker's own running balance** | 🟡 carried | 17,740.43 + 359.34 (TLT 82P, 9/28) = 18,099.77 vs 18,099.32 shown; 33 of 34 links hold | A fee/adjustment without its own row, OR a transcription digit misread | **PROME** re-reads the 9/29 image cell |
| **D-63** | **Cash bridge +$2.27 unattributed** | 🟡 carried — **untouched by 9/30** | 9/25-close cash + pending + the 9/28 rows = $18,099.77 vs cash $18,102.04; cash unchanged 9/30 and the Sep-30 Activity shows no dividend / interest row; 9/29 rows (if any) not captured | Money-market dividend, the APD "(D)" dividend, or interest — ANVIL picks none | **Will** — Activity 9/29 (low) |
| **D-64** | **Robinhood card — $5.00 unexplained** | 🟡 carried | $290.15 of lines + BP vs $295.15 shown `[9/29 13:4x intraday]`; not re-captured 9/30 | BP ≠ cash, a line valued off another price, or a line not on the card | **Will** — RH cash/account detail |
| **D-65** | **RH 9/14–9/15 put/call labels do not pair** | 🟡 no live position | 707 "Put" bought → 707 "Call" sold; 708 "Call" bought → 708 "Put" expiration | Hypothesis: the 9/15 "Call" rows are Puts ⇒ 707P +$104, 708P −$41 — NOT booked | **PROME** — re-read the image |
| **D-61** (narrowed) | **9/28 fills — times for QQQ 730P ×1 and TLT 77P ×5; TLT 77P $0.02 receipt-vs-ledger** | 🟡 | Ledger Σ $28.43 vs receipt $28.45; ledger used | Receipt digit or transcription — UNKNOWN | Will (order detail), low |
| **D-59** (narrowed) | **RH buying power 9/16 → 9/27: −$0.48 residual** | 🟡 | −$119.95 from the activity vs BP −$120.43 | Regulatory fees on four sells + rounding — labeled | Will, low |
| **D-45** (residual) | **+$43.81 before the 9/01 Activity view** | 🟡 | 8/28 cash + pending $14,323.25 vs derived 9/01 opening $14,367.06 | 8/31 activity or interest | **Will** — Activity 8/28–8/31 |
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
| **D-47** | **RH WAL Dec-18 $70P ×1 — `GATE-TERRY-ROLL70-EXIT`** | 🟡 79 DTE | ≈$265.00 derived `[9/29 13:4x intraday]` (not re-captured); entry bought 9/02 @ $2.20; 0-of-3 as last recorded; time stop 12/4; no resting exit order | — | **Will** (manual harvest); REGINALD grades / TERRY proposes |
| VLO-SCALE | **2 staged VLO sh** | 🟡 review_by 10/14 | 9/25 NOT MET; F1 UNKNOWN | — | TERRY grades → Will |
| WQ-200 | **USO 37 sh — no line live** | ⚪ | Card DECLINED 9/10; $145.66 `[9/30c]` informational | — | Will's hand |
| — | **APD thesis tag** | ⚪ | Unassigned since 7/30 | — | PROME / Will |

### CLOSED this pass (receipts = the 9/30 transcription's Activity ②)

- **QQQ $730P Sep-30 ×9 → SOLD TO CLOSE 9/30 @ $0.01, +$8.43 (row 10) ⇒ −$2,229.54** vs $2,237.97; campaign (×10 9/24 −$2,486.63 · +$197.34 9/28 · +$8.43) −$2,280.86. **WQ-316 → ANSWERED** by Will's roll (18:27 ET).
- **USO $159C Sep-30 ×2 → SOLD TO CLOSE @ $0.01, +$1.87 (row 5) ⇒ −$919.46** vs $921.33 — sold, not expired (D-68).
- **TLT $77P Sep-30 ×15 → SOLD TO CLOSE, +$9.37 (row 9, 10 @ $0.01) + $9.43 (row 12, 5 @ $0.02) ⇒ −$154.64** vs $173.44. **D-31 → CLOSED**; third hand-deviation from the HOLD, recorded not adjudicated.
- **KRE $60P Sep-30 ×2 → SOLD TO CLOSE @ $0.01, +$1.87 (row 1) ⇒ −$451.48** vs $453.35; **WQ-168 ⑥ (LAPSE) not followed — recorded**.
- **Σ realized 9/30 = −$3,755.12**; Σ proceeds $30.97; Σ new debits −$4,038.95 ⇒ net −$4,007.98 = Pending ✓. Canceled attempts (rows 3–4, 7–8, 14) move no cash.
- 11 Fidelity rows MARK ONLY: quantities and bases identical to the 9/29 mirror to the cent.

---

## Immediate Actions (9/30 reconcile state)

| Item | State | Owner |
|---|---|---|
| 🔴 **QQQ $740P Oct-01 ×9 expires THU 10/01 — $0.23 ITM at the 9/30 close; no card; D-60's ITM leg UNOBSERVED** (WQ-347: sell/roll by Thu 15:00 ET or hold into expiry) | 1 session | **Will** (hand) / TERRY card Thu |
| 🟠 **QQQ $735P Oct-05 ×5** (Mon 10/05, WQ-347) · **USO $150C Oct-09 ×2** (Fri 10/09) — no card on either | dated | **Will** / TERRY |
| 🟠 **WQ-302** TLT 82P ×1 + HBAN 16P ×2 by Wed 10/14; the one Fidelity question also answers D-60 | dated | **Will** |
| 🟠 **D-68** — TERRY INDEX/card + WQ-316 row read "expired" for sold lines; `position_management.tsv` rows 8/9/15/16 describe closed contracts | record | **TERRY · PROME** |
| 🟡 **D-67** KRE $0.01 marks — next regular-session capture · transcription re-reads D-62 · D-65 | image | **PROME** |
| 🟡 **Robinhood** (not captured 9/30) — D-64 · before 9/01: D-28 · D-54 · D-18 · D-20 · D-37 | one view | **Will** |
| 🟡 **Fidelity Activity** 8/28–8/31 (D-45 +$43.81) and 9/29 (D-63 +$2.27); older: D-1 · D-17 | one view | **Will** |
| 🟡 VLO staged 2 sh (VLO-SCALE) · USO 37 hand-managed · APD tag | carried | TERRY / Will / PROME |

---

*History → `_archive/JOURNAL.md` | Prior reconciles (9/27, 9/20 standing write-in, 9/10, 9/3, 8/29, 8/14, 8/2, 7/30, 7/20, 7/16, 5/21) in git history + `_archive/` | Full-portfolio Feb snapshot → `PORTFOLIO.md` (**FROZEN/superseded, historical only — never cite as live**) | Position truth = Will/broker direct (off-repo) | Marks-of-record transcription → `PROME/data/2026-09-30_broker-capture-TRANSCRIPTION.md` (Fidelity positions 9/30 post-close + Activity & Orders 9/30); prior `…_2026-09-29_…` (Fidelity 9/29 intraday + Activity 9/01→9/28 + RH card and activity — the RH rows' source)*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumers: `AGENTS/TERRY/scripts/positions_from_forge.py` (sections `^## (Fidelity|Robinhood)` + `^## Account <NAME>`; table headers by prefix; cell text — emphasis and strikethrough visible) · `PROME/tools/desk_attention.py` `holdings()` (same sections; `Qty` + `Ticker|Strike|Position` headers; expiry year from `**Updated:**`) · `PROME/tools/will_brief.py` `parse_money()` (header before the first `## `: `account total:**`, `money market):** $X (Y%)`, `**Updated:** YYYY-MM-DD`, `marks = [Fri ]YYYY-MM-DD`) · `FORGE/position_management.tsv` `source_sha256` (any byte change here withholds every mapping sourced to this file until PROME re-reviews) · `AGENTS/BRENT/scripts/pending_receipts.py` (text-level closure candidates). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself here in the same commit that starts parsing. *(9/27 pass: header money line RESTORED to the shape `will_brief.py` reads — it returned None on the 9/20 header; option expiries carry the year (a year-less "Sep-30" parses as 2027 from 10/1 in `positions_from_forge.py`); new table in § Off-thesis; VLO moved § Account UNATTRIBUTED → § Fidelity — Longs; WAL and RH-Sep-11 rows rotated. Parser receipts in the ANVIL report.)* *(9/28 fills pass: no structural change; `**Updated:**` stayed 9/27 because a fills receipt is not a broker view; Value `—` / P&L `see note` on the three sold-down rows, by design.)* *(9/29 pass: no structural change — same sections, headers and row conventions; `Mark 9/25` → `Mark 9/29` (prefix-bound); the three sold-down rows carry numeric Value/P&L again (broker marks at the new qty); `**Updated:** 2026-09-29` is a broker view, but INTRADAY — `marks = 2026-09-29` carries no close; `will_brief.py` will render it "Broker export 2026-09-29".)* *(9/30 pass: no structural change — same sections, headers and row conventions; `Mark 9/29` → `Mark 9/30` (prefix-bound); four Sep-30 rows removed (sold) and four added inside existing tables (Off-thesis ×3, KRE ×1); terminal records moved to italic lines, which no parser reads as rows; the header money line gains a `Pending activity` figure AFTER the `money market):** $X (Y%)` cell — `will_brief.py` regexes re-run, all four match; `**Updated:** 2026-09-30` = a post-close broker view.)*
