# FORGE — Trading Operations

Dashboard management mapping → [position_management.tsv](position_management.tsv); maintenance contract → [dashboard notes](DASHBOARD.md). Holdings remain in this file; approval, order and fill evidence are separate. A changed evidence source invalidates its management mapping until reviewed.

> 🟠 **2026-09-20 (WQ-272) — STANDING QUANTITY / TOTAL WRITE-IN BY ANVIL, operator-authorized (Will 2026-09-20 18:55 ET, *"Proceed with WQ-272 using the export."*). THIS IS NOT A TRANSACTION RECONCILE AND NO BROKER EXPORT EXISTS.** The six cells the 9/10 mirror was known-contradicted on (D-56) are now written to the **2026-09-16 13:57 ET Will-supplied visual capture** — two UNDATED screenshots, NO Activity view, NO fill dates/prices (`PROME/reports/2026-09-16_prefed-sell-review.md` lines 5, 7): **AAPL 15→10 · TBT 14→10 · GLD 16→17 · Fidelity cash $19,335.00→$22,192.87 (55.79%) · Fidelity total $39,885.25→$39,779.11 · Robinhood $946.13→$454.33 (BP $129.37)**; **USO 37 unchanged** (the control cell that matched). Each changed cell carries a capture tag — **STANDING VALUES ONLY, NOT transaction-reconciled**: the fills behind AAPL −5 / TBT −4 / GLD +1 have NO date and NO price (D-56, OPEN), and any MARK below not in the capture is **still a 9/10 CLOSE mark**.
>
> ⛔ **BASIS (honest):** standing quantities + account totals = **2026-09-16 13:57 ET visual capture**; **VLO 1 sh @ $412.00 = 9/18 receipted fill** (§ Account UNATTRIBUTED — account + time UNKNOWN, D-55); all remaining option/stock MARKS and per-row G/L = **9/10 CLOSE (Fidelity) / 9/10 16:10 ET (Robinhood)**, stale from that date. Position truth is off-repo (Will/broker direct); this file is the fleet's parseable mirror. A broker export + Activity view is still OWED to transaction-reconcile (D-56 · D-49 · D-53 · D-45 · D-44).
>
> ⚠️ **ACCOUNT SCOPE — Fidelity: ONE account (Traditional IRA 216461326, INFERRED by position-set match; header cropped). Robinhood: account value + BP from the 9/16 capture; per-line P/L from the 9/10 16:10 card.** Anything not in a capture stays "unverified today"; rows absent from a view are retained and flagged, never deleted. **Dated rows past their dates, unbooked → D-58 · D-57; absence is not closure.**
>
> **Updated:** 2026-09-20 (WQ-272 standing write-in) · standing quantities/totals `[9/16 13:57 visual capture]`, VLO `[9/18 receipt]`, all marks `[9/10 CLOSE]`. **Fidelity cash:** $22,192.87 (55.79%) `[9/16 capture]` · **Fidelity total:** $39,779.11 `[9/16 capture]` · **Robinhood:** $454.33, BP $129.37 `[9/16 capture]`. Prior reconcile vintage **9/10 CLOSE** (`PROME/data/2026-09-10_*-TRANSCRIPTION.md`). 9/10-vintage header, verification receipt, terminal rows and verbose discrepancy prose → `_archive/STATUS_ROTATION_2026-09-20.md` (whole-block crc32 379804408); earlier → `_archive/STATUS_ROTATION_2026-09-10.md`, `_archive/RECONCILE_2026-08-29_RECORD.md`.

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (7/18 re-base + amendment #1 = current). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*Standing quantities `[9/16 13:57 visual capture]`; all marks/values `[Fidelity positions, 9/10 CLOSE]` and stale from that date. DTE counted from 9/10.*

| Ticker | Type | Qty | Cost | Mark 9/10 | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | **10** `[9/16 capture — standing qty only, not txn-reconciled]` | $23.64 | $326.57 `[9/10]` | — | see note | **qty 15→10 (−5), 9/16 capture.** The −5 sh has NO recorded date/price (D-56); the pre-7/30 5-sh sale is D-1. No 9/16 mark/value in the capture ⇒ Value + G/L NOT recomputed; $326.57 is the stale 9/10 CLOSE mark. 52-wk 225.95–344.57 |
| GLD | Stock | **17** `[9/16 capture — standing qty only, not txn-reconciled]` | $373.59 | $396.36 `[9/10]` | — | see note | **qty 16→17 (+1), 9/16 capture.** The +1 sh has NO recorded date/price (D-56). No 9/16 mark/value in the capture ⇒ Value + G/L NOT recomputed; $396.36 is the stale 9/10 CLOSE mark. MIDAS domain; largest position by value. 52-wk 326.19–509.70 |
| USO | Stock | 37 | $122.28 | $158.38 `[9/10]` | $5,860.06 `[9/10]` | **+29.52%** `[9/10]` | **qty 37 — the 9/16 capture AGREES with this mirror (control cell that matched; no change).** +$1,335.79 (9/10; +$619.75 vs 9/3). Mark/value/G/L are stale 9/10 CLOSE. Will's Hormuz-gap entry (BRENT). ⚠️ **WQ-200 DECLINED by Will 9/10 11:15 ET — NO harvest/give-back rule live on the 37 sh; Will manages by hand. $158.38 informational only.** |
| APD | Stock | 2 | $294.79 | $293.65 | $587.30 | **−0.39%** | −$2.27 (today −$3.18) Thesis tag still unassigned (open since 7/30). 52-wk 229.11–314.87 |
| TBT | Stock | **10** `[9/16 capture — standing qty only, not txn-reconciled]` | $34.63 | $39.22 `[9/16 implied]` | **$392.20** `[9/16 capture]` | see note | **qty 14→10 (−4) + value $392.20 both from the 9/16 capture.** The −4 sh has NO recorded date/price (D-56). 9/16 implied mark $39.22 = $392.20/10 (vs the 9/10 $39.51); G/L NOT recomputed against an undated basis. 2× UST short — duration-short leg (BOND/TERRY). 52-wk 31.69–39.67 |
| XLE | $65C Sep-30 | **0 — SOLD 9/11** | $2.28 | $1.51 fill | $150.34 net | −33.97% | **SOLD TO CLOSE 9/11 ~10:07 ET at $1.51 ×1 (Will's Fidelity activity row via TERRY bcc962bbd; net $150.34 vs lot basis $227.67 ⇒ −$77.33 realized) — line FLAT; not yet in a broker export, ANVIL reconciles at the next capture.** 9/10 CLOSE cells were: mark $1.47, value $147.00, −$80.67 (today −$23 / −13.53%). **qty 2→1 BROKER-VERIFIED — one contract SOLD, NOT among the ledger's visible rows (all Sep-10, morning AND close views) ⇒ before today or outside the crop; date/price UNKNOWN; basis $227.67 = ½ × $455.34.** WQ-168 ⑦ ruled SELL BOTH at the bid on the 9/9 open unless XLE closed ≥$66.50 on 9/8 (DOCKET L252/L253 — fill UNKNOWN). **The surviving ×1 has NO ruling on file.** 20 DTE. See **D-49** |

*Not on the 9/10 view: **VLO** (TRY-BRENT-REFINER, 3× approved 8/27) ⇒ unfilled in the IRA **as of 9/10 — ⚠️ 1 share has since FILLED 9/18 @ $412.00 in an account this file cannot name: see § Account UNATTRIBUTED + D-55**; Robinhood stocks card unread · **STNG** (D-17) · **QQQ** shares (day-trade class, D-44) · **TLT $85P** (SOLD 9/10) · **QQQ $715P Sep-10** + **USO $153C Sep-11** (day-trade class, both SOLD 9/10).*

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book. The five Aug-21-2026 EXPIRED rows (KRE 60P · QQQ 710P · OZK 45P/42.5P · KELYA 7.5P; broker-confirmed, realized −$2,816.72 total) were rotated 9/10 → the rotation record.

*No live event-box rows — the VIX $20C/$25C spread (CLOSED 2026-07-30, realized −$111.60) and the five Aug-21-2026 EXPIRED rows (realized −$2,816.72 total) are terminal → rotation records.*

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, on no PROME rail and owned by no agent. Recorded so it is not invisible. The two 9/10 Fidelity day-trade tickets (QQQ 715P Sep-10 SOLD +$399.66 · USO Sep-11 153C SOLD, entry UNKNOWN — D-53) are terminal → rotation record; full 7/20–8/28 ticket history at `183068dd1` + the 8/29 transcription. WQ-97 (20 of 23 QQQ sold by 8/28); residual 3 sh absent 9/3 & 9/10 (D-44). Robinhood same-class rows are in the Robinhood table.

*No live day-trade rows here — the two 9/10 Fidelity day-trade tickets (QQQ 715P Sep-10, USO 153C Sep-11) both SOLD 9/10 → rotation record. Robinhood day-trade rows are in the Robinhood table below.*

## Fidelity — Thesis Puts

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| **$77P** | **Sep-30** | **20** | **$0.12** *(broker basis $231.26 = 20/25 × $289.08; fees-in $0.11563)* | $0.08 | $160.00 | **−$71.26 / −30.82%** (today +$80 / +100%). **qty 25→20 — 5 contracts SOLD 9/10 @ $0.06 (limit $0.06 Day), net $28.44 `[Fidelity activity, 9/10]` vs lot basis $57.82 ⇒ −$29.38 realized; WQ-168 ④ had ruled HOLD ×25 to expiry — a deviation, recorded not graded (D-50 closed).** 20 DTE. ⚠️ Gate proximity, NOT adjudication (rule 7): harvest line *"half at ≥3×"* (PB-0002b: 10 ct at ≥$0.3469 fees-in) — at $0.08 = **0.69× fees-in basis**; exit gate GATE-TERRY-007 *"FIVE CONSECUTIVE official FRED DGS10 closes <4.50% ⇒ TERRY builds exit proposal → Will [Approve]"* — **0 of 5** as last owner-graded (9/1 DGS10 4.79); no DGS10 in this capture. 7/31 harvest 5 ct @ $0.37336 = +$128.86 realized (PB-0002a). See **D-31** |
| $82P | Oct-16 | 2 | $1.68 | $1.96 | $392.00 | **+$56.65 / +16.89%** (today +$134 / +51.93%, the put book's mover — from 1.02 on 9/3). 36 DTE. No ruling recorded on this file |


### KRE — regional banks (REGINALD)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $60P | Dec-18 | 2 | $2.57 | $0.35 | $70.00 | −$443.34 / −86.37% (today −$22). 99 DTE |
| $60P | Dec-18 | 3 (M) | $2.93 | $0.35 | $105.00 | −$773.02 / −88.05% (today −$33) — Fidelity multi-lot marker; **five** Dec-18 KRE 60P total across the two lots. 99 DTE |
| $60P | Sep-30 | 2 | $2.27 | $0.01 | $2.00 | −$451.35 / −99.56% (today −$8) — **20 DTE. RULED WQ-168 ⑥: LAPSE.** Rides to $0 |

### WAL (REGINALD) — Sep-18s (the 7/21 print resolved NOT-FIRED)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $70P | Sep-18 | 1 | $7.69 | $0.05 | $5.00 | −$763.67 / −99.35% (today −$8) — **8 DTE. RULED WQ-168 ①: LAPSE** (**re-opens only if WAL closes <$71 in the week of 9/14**; no WAL price in this capture). Duration-rolled to the Robinhood Dec-18 $70P ×1, now broker-verified (D-47) |
| $67.5P | Sep-18 | 1 | $7.51 | $0.05 | $5.00 | −$745.67 / −99.34% (today $0) — **8 DTE. RULED WQ-168 ②: LAPSE** |

*(The Robinhood **WAL $77.5P Aug-21 ×1** — Will confirmed the sale in-session 2026-08-18; date/proceeds still unrecorded ⇒ P&L UNRECORDED, not zero — D-18. Struck-through in the Robinhood table, retained.)*

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18 | 1 | $11.85 | $0.85 | $85.00 | −$1,099.67 / −92.83% | BROCK thesis vehicle. 0.60 [9/3] → 0.85 (today −$19). 99 DTE. No ruling on file |
| HBAN | $16P | Oct-16 | 2 | $0.96 | $0.25 | $50.00 | −$141.34 / −73.87% | EXIT-THESIS dust (Will 7/18) — rides to expiry, zero effort. 0.20 [9/3] → 0.25 (today −$14). 36 DTE |

## Robinhood — satellite account (Individual)

> ⚠️ **Account value / BP = 2026-09-16 13:57 capture: $454.33 / BP $129.37** `[9/16 capture]` (was $946.13 / $489.69 on 9/10 16:10 ⇒ −$491.80; D-56). **Per-line detail (cost/value DERIVED, no Mark column) = the 9/10 16:10 Options card + Recent activity** — costs = P/L ÷ P/L%, labeled; block stays machine-class `unverified` by design. Rows absent from a capture are retained, not deleted. Prediction market (Nithya Raman "Yes" 36¢, ≈$9.44) recorded 9/10, not adjudicated, no D-row.

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **WAL $70P** | **Dec-18-2026** | 1 | **$2.20 ($220)** — card-derived $219.97 ✓ | ≈$230.00 *(derived: $220 + $10.00)* | ✅ **BROKER-VERIFIED 9/10 16:10 — card +$10.00 / +4.55%** (was +$13.00 / +5.91% ~10:3x) | Existence + cost verified (D-47 existence half CLOSED; was Will's word 9/2). TRY-WAL-ROLL70 filled in ROBINHOOD, not the IRA the card named (TERRY card §5c). Guard = **GATE-TERRY-ROLL70-EXIT** *"WAL OFFICIAL CLOSE ≥ $81.90 on THREE CONSECUTIVE sessions"* — **0-of-3 as last graded (9/2 close $79.12)**; no WAL price in this capture (REGINALD grades; rule 7, not adjudicated). $4.40 harvest GTC resting status **permanently UNKNOWN (WQ-167), not an ask**. Time stop Fri 12/4. 99 DTE. See **D-47** |
| **USO $159C** | **Sep-11-2026 — TOMORROW (CPI day)** | 1 | **$1.52 ($152.00)** — bought 9/10 ~15:1x | ≈$216.00 *(derived: $152 + $64; ≈$2.16/ct)* | ✅ **BROKER-VERIFIED 9/10 16:10 — card +$64.00 / +42.11%** `[Robinhood recent + options card, 9/10 16:10]` | **Day-trade class — Will-managed, no card, no rail, no owner.** 1 DTE; dies at Fri's close or by Will's hand. Recorded so it is not invisible |
| **KRE $25P** | 1/15/2027 | 1 | $53.00 — card-derived $53.00 ✓ | ≈$1.00 *(derived)* | ✅ **BROKER-VERIFIED 9/10 16:10 — card −$52.00 / −98.11%** (unchanged from ~10:3x; **existence corroborated by the 9/16 13:57 capture**) | Deep-OTM lottery. On the mirror since the 7/16 reconcile (−$52 / −98.1%; −$38 / −71.7% on 7/20) ⇒ entry predates 7/16; **entry date/price never recorded — D-54**. 127 DTE |
| T | stock | 1 | — | — | ⚠️ **absent 8/14 + 8/28; stocks card not captured 9/10** | 1 share (~$22 on 7/20) — larger than the $8.67 residue, so "hidden" does not fit. **Hypothesis: sold**, unconfirmed. See D-20 |

## Account UNATTRIBUTED — receipted fills not yet attributed to an account

> ⛔ **This section exists because the account is genuinely UNKNOWN, not because it is undecided.** The receipt Will pasted carries ticker, quantity, order type and fill price and **no account and no time**; both were asked of him on 9/18 and are unanswered. **An inferred account in a position mirror is worse than a blank one** — nothing here moves into the Fidelity or Robinhood tables without Will's own word. ⚠️ **Machine note: `positions_from_forge.py` binds only `^## (Fidelity|Robinhood)`, so this section is INVISIBLE to it and the row below does not reach TERRY's dashboard** — logged in the footer as a consumer sweep OWED.

| Position | Acct | Qty | Cost | Mark 9/18 | Value | P&L | Note |
|----------|------|-----|------|-----------|-------|-----|------|
| **VLO** | **UNKNOWN** | 1 sh | $412.00 | $413.28 | $413.28 | **+$1.28 / +0.31%** | **BUY 1 VLO, Limit $412.00 Day, FILLED $412.00 on 2026-09-18 by Will's own hand — 1 of the 3 shares approved (`WQ-213` 8/27, re-affirmed 9/17; `DOCKET L412` RESOLVED).** Receipt verbatim → TERRY `0d59d9b72` / `PROME/inbox/processed/2026-09-18_from-TERRY_wq213-FILL-RECEIPT-1-of-3-VLO-412.00_L412.md`; card record `AGENTS/TERRY/setups/BRENT_refiner-distillate-strong-leg_2026-08-27.md` § FILL RECORD, `PB-0007`. **Account UNKNOWN · fill time UNKNOWN** (bounded at-or-before **12:33 ET** only because that is when Will pasted the receipt — a bound, not the time). Mark is the **vendor 9/18 close $413.28 (+0.18%)** `[FORGE fetch.py, pulled 2026-09-19 13:0x ET — A DATED CLOSE, NOT A BROKER MARK; markets closed]`; value and P&L are arithmetic on it. **2 shares remain STAGED on TERRY's card for a day of Will's choosing — NOT a lapse and NOT a re-ask** (the approval covers 3). **No exit rule exists on the held share.** See **D-55** |

---

## ⚠️ Reconcile discrepancies (9/10 reconcile · **+ 9/19 receipt-pass rows D-55…D-58**)

> 🆕 **Discrepancy provenance:** **D-56** (the 9/16 capture's six contradicted cells) was WRITTEN INTO THE ROWS as standing values on 2026-09-20 under WQ-272 (operator-authorized), NOT transaction-reconciled — it stays OPEN for the fills' dates/prices. **D-55** VLO fill's unknown account/time · **D-57** the two RH Sep-16 contracts · **D-58** dated rows past their dates, unbooked. Rows D-1..D-54 are the 9/10 build; none was closed 9/19–9/20 (closures need a broker Activity view; none was taken).
>
> Built against the 9/10 CLOSE Fidelity view + Activity ledger + the 9/10 16:10 Robinhood re-capture; augmented 9/16→9/20 by the visual capture (standing quantities only). **Nothing resolved by invention; every conjecture labeled; broker view > Will's word > PROME queue.** Ranked by decision urgency, expiring first; "Will decides" vs "owner decides" separated. **Permanently UNKNOWN by WQ-167 (never asks):** the 9/2 USO 135C sale price · the ROLL70 $4.40 GTC status. **Closed at the 9/10 pass** (text → `_archive/STATUS_ROTATION_2026-09-10.md`): D-43/D-51 · D-50 · D-52 · D-46→D-49 · D-48 · D-47 existence half · WQ-168 ③. **Still owed:** the Fidelity Activity view rows before 9/10/9/16 (date D-49 · D-53 · D-44, attribute D-45) and the fills behind D-56.

### EXPIRING / DATED — Will decides

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-56** | 🟠 **THE 9/16 13:57 CAPTURE'S SIX CONTRADICTED CELLS — NOW WRITTEN AS STANDING VALUES (WQ-272, Will 2026-09-20); OPEN for the fills' dates/prices** | 🟠 standing values current; transaction detail still missing | Written to the rows 2026-09-20 from `PROME/reports/2026-09-16_prefed-sell-review.md` (visual read of two UNDATED screenshots, no Activity view): **AAPL 15→10 · TBT 14→10 · GLD 16→17 · cash $19,335.00→$22,192.87 (55.79% ✓) · Fidelity total $39,885.25→$39,779.11 · Robinhood $946.13→$454.33 (BP $129.37); USO 37 unchanged (control ✓).** Internal checks: 22,192.87/39,779.11 = 55.79% ✓; TLT 77P ×20 basis $231.26 ✓ | **Labeled arithmetic, NOT a fill record:** 9/10 cash $19,335.00 + pending $1,288.44 + XLE 9/11 net $150.34 = $20,773.78 ⇒ capture cash **+$1,419.09**; AAPL −5×$333.05 + TBT −4×$39.12 − GLD +1×$398.35 = **+$1,423.38** at 9/16 closes ⇒ residual **−$4.29**. Corroboration to ~$5, NOT dates/prices/proof — fills happen at fill prices | **Will** (Activity view) → **PROME** (transcribe to `PROME/data/`) → ANVIL transaction-reconciles. Standing quantities/totals are now citable as "9/16 capture, standing only"; the −5 AAPL / −4 TBT / +1 GLD fills are NOT dated or priced |
| **D-55** 🆕 | **VLO ×1 FILLED 9/18 @ $412.00 — ACCOUNT and FILL TIME UNKNOWN** | 🟠 a live position the mirror cannot place in an account | The receipt is the whole evidence (TERRY `0d59d9b72`, pasted 12:33 ET): *"Sep-18-2026 · Buy 1 Share of VLO Limit at $412.00 (Day) · Filled at $412.00 · $412.00"* — **it names no account and no time.** Both were asked of Will on 9/18 and are unanswered. Position row → § Account UNATTRIBUTED | ⛔ **ANVIL infers nothing and names no account.** One datum is recorded because suppressing it would be worse, and it settles nothing: **Robinhood buying power read $129.37 at the 9/16 capture, below $412.00** — a deposit, a sale or margin each defeat that. **It is NOT evidence of Fidelity.** Against it: VLO was absent from the 9/10 IRA view, and the WAL roll went to Robinhood, so neither account is a default | **Will** — one line: which account, and the fill time |
| **D-57** 🆕 | **`WQ-169` fact 4 — two Robinhood Sep-16 contracts DISAGREE between surfaces. Recorded AS A DISAGREEMENT, not as an expiry** | 🟠 dated 9/16, already passed; disposition unbooked | The 9/16 13:57 capture reads **QQQ $713C ×1 and USO $165C ×1 both expiring Sep-16**, beside WAL 70P Dec-18 ×1 and KRE 25P Jan-15-2027 ×1. **This mirror holds neither contract:** its QQQ 713C is a **Sep-10** day trade closed 9/10 (−$11.00) and its 165C is the short leg of the **Sep-18** USO 150/165 spread closed 9/10 (+$330.00). BRENT verified that the public contract `USO260916C00165000` exists (**a contract check, NOT a broker check**) and quoted $0.01/$0.02 at 18:28Z 9/16 — indicative only | Three readings, **ANVIL picks none**: (a) two genuinely NEW positions opened 9/11–9/16, so the capture is right and this mirror is merely stale · (b) the capture's expiry dates were misread off a screenshot — both strikes, 713 and 165, recur in this mirror at other expiries · (c) one of each. **Either way the disposition — sold / expired worthless / assigned — is UNKNOWN, and "expired" must not be booked at $0** | **Will** — one broker line per contract. ⛔ **Do not resolve this from the tape, the public chain, or this mirror's older rows** |
| **D-58** 🆕 | **Dated rows now PAST their dates with no mirrored outcome — a reader hazard, not a capital ask** | 🟡 nothing owed today; the rows read as if live | **RH USO $159C Sep-11 ×1** — row still says *"TOMORROW (CPI day)"*; absent from the 9/16 capture (consistent with expiry, **not proof**). **Fidelity WAL $70P and $67.5P Sep-18 ×1 each** — TERRY reported both bid 0.00 `NOBID` at 11:0x on 9/18 and *"lapse worthless at today's close"* per `WQ-168` ①②, which is **an owner's read of a quote, not a broker confirmation of expiry**. Plus the two Sep-16 contracts of D-57 | Each most likely expired worthless; **none is booked**, and a worthless expiry is still a realized loss that must be recorded as one, not absorbed silently. ⛔ **ANVIL did not strike these rows** — striking a row asserts a broker event | **Will / the next capture.** Rows stay live-shaped and flagged, never deleted — absence is not closure |
| — | **RH USO $159C Sep-11 ×1 — expires TOMORROW (CPI day); Will-managed day trade, no rail** | 🔴 1 DTE · no ask | Bought 9/10 ~15:1x @ $1.52; card +$64.00 / +42.11% ⇒ ≈$2.16 at 16:10 | None — fully specified; outcome needs the next Recent view | **Will** (his hand) |
| **D-49** | **XLE $65C Sep-30 — the FIRST of two contracts sold has no date and no price; the line is FLAT** | 🟠 first contract's date/price UNKNOWN — no live contract | qty 2→1 broker-verified 9/10 (basis $227.67 = ½ × $455.34); the survivor was SOLD 9/11 at $1.51, net $150.34, −$77.33 realized (TERRY `bcc962bbd`, WQ-210 DONE). The FIRST contract is not among the 9/10 ledger's four visible rows ⇒ sold before 9/10 or outside the crop | (a) partial fill of a 2-lot · (b) a deliberate 1-lot · (c) 9/8 closed ≥$66.50, sale unrelated to WQ-168 ⑦. **ANVIL picks none.** (Full 9/10-vintage derivation + the 9/14 self-correction note → rotation record.) | **Will** — the FIRST contract's sale date and price only (Activity-view scroll-back). Nothing owed on the survivor |
| **D-53** | **USO Sep-11 $153C ×1 — SOLD 9/10 @ $2.14, net $213.34; ENTRY unrecorded; on no positions view** | 🟠 entry owed (leg closed) | Ledger row only `[Fidelity activity, 9/10]`; absent from the 9/3, 9/9 and 9/10 views ⇒ opened and closed between captures | Entry between 9/3 and 9/10, cost UNKNOWN ⇒ realized UNKNOWN, not zero; the −$190.35 bridge residual (D-45) is the only constraint | **Will** — entry date/price, or the ledger's earlier rows |
| **D-45** | **Cash bridge 9/3 → 9/10: −$190.35 unattributed after the ledger** | 🟠 earlier ledger rows owed | $18,025.71 + 135C $1,754.30 (in cash — pending = today's four fills to the cent) − QQQ 715P buy $254.66 = **$19,525.35 expected vs $19,335.00 cash ⇒ −$190.35** | = XLE ×1 proceeds − USO 153C entry − anything else (interest, an unseen ticket); labeled arithmetic, **not a claim** | **Will** — the Activity view scrolled to before 9/10 |
| **D-44** | **QQQ 3 sh — GONE 9/3, absent 9/10; sale date/price UNKNOWN** | 🟡 fact owed | 8/28: 3 @ $716.43, basis $714.74; absent both views since | SOLD — labeled, supported by the 8/28→9/3 bridge, still not proof | **Will** — the same activity view dates it |

### RULED / GATED — owner decides (nothing owed by Will today)

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| WQ-168 ①② | **WAL $70P + $67.5P Sep-18 (Fidelity) ×1 each — LAPSE** | 🟡 8 DTE | Both $0.05 / $5.00; −99.35% / −99.34%. 70P re-opens only if WAL closes <$71 in the week of 9/14; no WAL price in this capture | Nothing — the rule is fully specified | REGINALD watches the <$71 trigger |
| WQ-200 | **USO 37 sh — management card DECLINED by Will 9/10 11:15 ET (Decision Deck); no line is live** | ⚪ closed | 9/10 CLOSE $158.38 `[Fidelity positions, 9/10 CLOSE]` — informational; TERRY parked the card (TRY-EXIT-USO35 PARKED, 9/10) | Will's hand |
| **D-31** | **TLT $77P Sep-30 ×20 — HOLD (WQ-168 ④, as it stands after D-50)** | 🟡 20 DTE / 14 sessions | $0.08 / $160 on $231.26 (−30.82%). 0.69× fees-in; harvest *"half at ≥3×"* far away. GATE-TERRY-007 **0-of-5** as last graded 9/1 (DGS10 4.79) | Registry's own logic: *"NO-VERDICT is the correct read if expiry beats the count"* — five sub-4.50 official closes inside 14 sessions | TERRY grades DGS10 daily → Will only on a proposal |
| WQ-168 ⑥ | **KRE $60P Sep-30 ×2 — LAPSE** | 🟡 20 DTE | $0.01 / $2.00 (−99.56%) | Nothing | Rides to $0 |
| **D-47** | **RH WAL Dec-18 $70P ×1 — existence + cost BROKER-VERIFIED 9/10; guard un-graded since 9/2** | 🟡 99 DTE | Card +$10.00 / +4.55% at 16:10 (+$13.00 / +5.91% ~10:3x) ⇒ cost ≈$220 ✓, value ≈$230 derived. GATE-TERRY-ROLL70-EXIT **0-of-3 at the 9/2 close $79.12**; time stop 12/4 | $4.40 GTC status permanently UNKNOWN (WQ-167) ⇒ harvest is a manual act by Will, not a control. Residue = the guard needs a WAL close series REGINALD owns | REGINALD grades / TERRY proposes |

### CARRIED — need a capture or one line from Will

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-28** | **Robinhood QQQ $715P ×1 — expired 8/31, outcome UNRECORDED** | 🟡 carried | Cost ≈$193.24; QQQ closed 716.43 on 8/28. No QQQ line on either 9/10 card (consistent, not a booking). TERRY ④ 9/3: UNRECORDED, not an ask. **8/28→9/10 cash bridge (labeled):** $183.57 − WAL $220 + spread $630 − 159C $152 − 713C $11 − prediction ≈$9.18 = ≈$421 vs BP $489.69 ⇒ **≈+$68 unattributed** (715P proceeds and/or an inflow) | Expired OTM (≈−$193) / sold / exercised — none verified | Next Robinhood history view |
| **D-17** | **STNG — appears in no capture, nowhere in FORGE (carried)** | 🟠 carried | Absent from every capture since 8/2 and the 7/30–8/28 activity window. March-2026 record (STNG ×2 @ $70.01, sold next day) | (a) the 7/21 note recalled the March position · (b) closed pre-7/30 · (c) a third account. ANVIL picks none | **Will** — one line |
| **D-20** | **Robinhood: T share absent ×2 + event contracts invisible + ≈$8.67 residue (8/28)** | 🟡 carried | No stocks card 9/10 (either pass). **16:10 sum closes to the cent with no stock line ⇒ T not held (INFERRED; needs buying power = cash)**; ≈$8.67 residue gone | Hypothesis: T sold; event-contract exposure of unknown size remains the live risk | **Will** — a full Robinhood view |
| **D-1** | **AAPL 5-sh sale — date + price unrecorded** | 🟡 carried | qty 15 Will-confirmed 8/2 and on every view since; no AAPL activity 7/30–8/28 ⇒ predates 7/30 | ~$565 cash class | Will / an older activity window |
| **D-18** | **Robinhood WAL $77.5P Aug-21 — sale CONFIRMED (8/18), P&L UNRECORDED** | 🟡 carried | Existence closed 8/18 | Date/proceeds need a Robinhood history view; do not book at $0 | Will (not urgent) |
| **D-54** | **RH KRE $25P Jan-15-2027 ×1 — entry date/price never recorded** | 🟡 carried | Card −$52.00 / −98.11% at 16:10 ⇒ cost $53.00 derived, mark ≈$1. On the mirror since the 7/16 reconcile (−$52 / −98.1%; −$38 / −71.7% 7/20). **NOT new** — the 16:10 transcription's "not previously on the mirror" is refuted at the artifact (`6568be33e`) | Entry pre-7/16 at ≈$0.53 — a derivation, not a fill | Will — activity view when convenient |
| **D-37** | **Robinhood ≈$360 inflow (8/14→8/28) + "13 days left" banner** | 🟡 carried | Arithmetic recorded 8/29; nothing trades off it. 16:10: $946.13 / $489.69; the ≈+$68 residual sits in D-28 | Deposit/transfer hypothesis; banner referent unknown | Will (one line) |

---

## Immediate Actions (9/10 session state · **+ 9/19 receipt-pass rows at the top**)

| Item | State | Owner |
|---|---|---|
| 🟠 **9/16 capture's six cells WRITTEN as standing values (WQ-272, 9/20)** — **D-56** | 🟠 Standing quantities/totals now current + tagged; a broker Activity view is still owed to date/price the AAPL −5 / TBT −4 / GLD +1 fills and transaction-reconcile | **Will** (Activity view) → **PROME** → ANVIL |
| 🆕 **VLO ×1 @ $412.00 filled 9/18 — which account, what time?** (**D-55**) | 🟠 Mirrored with both cells blank. **2 shares stay STAGED for Will's day — not a lapse, not a re-ask** | **Will** — one line |
| 🆕 **Two RH Sep-16 contracts: mirror and capture disagree** (**D-57**) · **four dated rows past their dates, unbooked** (**D-58**) | 🟠/🟡 Both recorded as-is; nothing struck, nothing resolved | **Will / next capture** |
| **★ Fidelity Activity view — rows BEFORE 9/10** (D-49 · D-53 · D-45 · D-44) | 🟠 Dates the XLE ×1 sale and the USO 153C entry; attributes −$190.35 | **Will** — scroll back and post |
| **WQ-200 USO 37-share card — DECLINED 9/10 11:15 ET** | ⚪ no line live; $158.38 close informational | **Will's hand** |
| **Sep-18 cluster** (WAL pair LAPSE; RH USO 150/165 **CLOSED 9/10 +$330.00** — WQ-207 / TERRY card / BRENT row to close) | 🟡 8 DTE; bookkeeping only | REGINALD / PROME / TERRY-BRENT |
| **TLT 77P ×20 HOLD; 5 sold 9/10 off-ruling; GATE-TERRY-007 0-of-5** (D-31) | 🟡 20 DTE | TERRY |
| **Robinhood dated history + stocks card owed** (D-28 · D-54 · D-18 · D-20 · D-37) | 🟡 Account $946.13 read 16:10; ≈+$68 residual | **Will** |
| **STNG · AAPL 5-sh** (D-17 · D-1) | 🟡 Carried; one line each | **Will** |
| **APD thesis tag** | 🟡 Unassigned since 7/30; −0.36% | PROME / Will |

---

*History → `_archive/JOURNAL.md` | Prior reconciles (9/3, 8/29, 8/14, 8/2, 7/30, 7/20, 7/16, 5/21) in git history | Full-portfolio Feb snapshot → `PORTFOLIO.md` (**FROZEN/superseded, historical only — never cite as live**) | Position truth = Will/broker direct (off-repo) | Marks-of-record transcriptions → `PROME/data/2026-09-10_fidelity-close-capture-TRANSCRIPTION.md` (Fidelity CLOSE) · `PROME/data/2026-09-10_robinhood-capture-1610-TRANSCRIPTION.md` (RH 16:10) | 9/16 standing capture (untranscribed) → `PROME/reports/2026-09-16_prefed-sell-review.md`*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumer: `AGENTS/TERRY/scripts/positions_from_forge.py` (desk-dashboard Positions tab; keys on table headers, section names, and cell text — markdown emphasis and struck-through rows are visible to it). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069). New consumers: add yourself to this list in the same commit that starts parsing. *(9/20 WQ-272 pass: NO header/section/column change — only cell text in existing rows updated + terminal rows removed by rotation; parser re-run receipt in the ANVIL report.)*
>
> 🔴 **CONSUMER SWEEP OWED (from the 9/19 pass, still unresolved):** the **`## Account UNATTRIBUTED`** section (VLO ×1) is NOT PARSED — `positions_from_forge.py` binds `^##\s+(Fidelity|Robinhood)\b` and sets `in_region=False` on every other `##`, so the VLO share is ABSENT from TERRY's dashboard (fail-safe: missing, not fabricated). ⛔ **ANVIL does not edit TERRY's script.** **ASK OF TERRY, via PROME:** extend `POS_SECTION_RE` to admit the section with `group="UNATTRIBUTED"` (an account FIELD, never a guessed account), or declare the omission acceptable. The row leaves this section the moment Will names the account. ⚠️ **Pre-existing, not ANVIL's to fix:** the parser still emits `XLE $65C Sep-30 qty 0` as LIVE. *(The 9/20 WQ-272 pass RESOLVED the parser's stale AAPL 15 / GLD 16 / TBT 14 emissions — those cells now carry the 9/16 standing quantities.)*
