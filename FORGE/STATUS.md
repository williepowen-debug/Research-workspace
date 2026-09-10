# FORGE — Trading Operations

Dashboard management mapping → [position_management.tsv](position_management.tsv); maintenance contract → [dashboard notes](DASHBOARD.md). Holdings remain in this file; approval, order and fill evidence are separate. A changed evidence source invalidates its management mapping until reviewed.

> **Structured position-truth mirror — reconciled 2026-09-10 (Thu) by ANVIL from THREE Will screenshots (PROME-transcribed → `PROME/data/2026-09-10_broker-capture-TRANSCRIPTION.md`): the Fidelity positions view, a Robinhood Options card (P/L only) and — round 2, 10:42 ET — a Fidelity Activity & Orders view (four rows, all Sep-10; date window not visible). ⚠️ MARKS ARE LIVE INTRADAY Thu 9/10 ~10:3x ET, NOT CLOSES ("Today's gain/loss" populated; USO last 153.455 vs a 10:26 ET live fetch 153.23) — cite as `[Fidelity positions, 9/10 ~10:3x ET intraday]`. Position truth is off-repo (Will/broker direct); this file is the fleet's parseable mirror and stales from the moment it's written.** Prior vintage: the 9/3 ~15:07 ET intraday reconcile (`PROME/data/2026-09-03_broker-capture-TRANSCRIPTION.md`; this file at `f8fc48869`, +9/9 receipt edits at `8e7a399a8`). Earlier reconciles in git history (8/29's record → `FORGE/_archive/RECONCILE_2026-08-29_RECORD.md`). Refresher flow = Will-on-broker-capture → PROME transcribes → ANVIL reconciles. Old ledgers → `FORGE/_archive/`.
>
> ⚠️ **ACCOUNT SCOPE — Fidelity: ONE account, id NOT visible on this image (header cropped) — attributed to the Traditional IRA 216461326 by position-set match with 9/3 and 8/29, INFERRED not read.** Positions view only. **Robinhood: PARTIAL — Options card only** (per-line P/L $ and %; no qty, marks, cash, stocks card, event contracts, timestamp) ⇒ three option rows are broker-verified for existence + P/L, everything else in that account stays "not in this capture, unverified today." **The activity view dates and prices three of the four quantity changes vs 9/3** (TLT 77P ×5 · TLT 85P ×1 · QQQ 715P ×1 — all SOLD 9/10; Σ four fills $1,288.44 = the pending line to the cent) **and surfaces a fifth leg on no positions view** (USO Sep-11 $153C ×1, sold 9/10, entry UNKNOWN — D-53); **XLE 65C 2→1 is NOT among the visible rows** ⇒ date/price still UNKNOWN (D-49). The cash bridge (D-45) is arithmetic, not an attribution. Absence from a positions view is not itself proof of closure; rows absent today are **retained and flagged, never deleted**. See **§ Reconcile discrepancies (9/10)**.

> **Events since the 9/3 reconcile, by label.** **BROKER-VERIFIED (positions view + activity ledger `[Fidelity activity, 9/10]`):** USO $135C Oct-16 absent (matches the 9/9 receipt) · **XLE $65C Sep-30 qty 2→1** (one SOLD — NOT in the ledger's visible rows, date/price UNKNOWN; ⑦ had ruled SELL BOTH 9/9) · **TLT $77P ×5 SOLD 9/10 @ $0.06, net $28.44** (④ had ruled HOLD ×25 — a deviation, recorded not graded) · **TLT $85P ×1 SOLD 9/10 @ $3.93, net $392.34** (limit $3.92 — Will re-priced the $2.60) · **QQQ $715P Sep-10 ×1 SOLD 9/10 @ $6.55, net $654.32** · **USO Sep-11 $153C ×1 SOLD 9/10 @ $2.14, net $213.34 — a leg on no positions view** · cash + pending +$2,597.73 · Robinhood card: **WAL $70P Dec-18 ×1 +$13.00** (was PROME-supplied, D-47) · USO 150/165 +$201.00 · KRE 25P −$52.00. **PROME-SUPPLIED context (queue, not broker):** WQ-201 (TLT 85P limit) — answered by the 85P fill, PROME closes the row · WQ-200 (USO 37-sh card LINE-1 harvest, *"≥$152.96 official close"*) OPEN, due 9/11. **Standing rulings (WQ-168, 9/3) and GATE-TERRY-ROLL70-EXIT:** not amended by this pass; two deviations from WQ-168 are recorded above (④: 5 of 25 sold; ⑦: consumed, the surviving ×1 has no rule) — see the position rows.

**Updated:** 2026-09-10 [Fidelity positions, 9/10 ~10:3x ET intraday] | **Fidelity cash (money market):** $19,335.00 (48.88%) — was $18,025.71 on 9/3 ⇒ **+$1,309.29** | **Pending activity:** **$1,288.44** = today's four ledgered sales to the cent ⇒ cash + pending **+$2,597.73** vs 9/3 = 135C $1,754.30 (in cash) + today's fills $1,288.44 − QQQ 715P buy $254.66 **− $190.35 unattributed = XLE ×1 proceeds − USO 153C entry − anything else (D-45)** | **Fidelity positions market value:** $18,928.66 (was $20,233.73) | **Fidelity account total:** $39,552.10 (was $38,259.44 ⇒ **+$1,292.66**) *(9/10 session to 10:3x: +$130.35 / +0.33%; open-position G/L **+$1,463.49 / +8.38%** on $17,465.17 open basis — basis fell $1,247.83 = 135C $710.66 + 85P $251.67 + XLE ×1 $227.67 + 77P ×5 $57.82, ±1¢)* | **Robinhood Individual:** Options card only, no account value (last read 8/28: $414.81)

*ANVIL re-verified every capture cell independently: 15 rows + cash + pending = $39,552.10 to the cent; Σ today +$130.35; Σ open G/L +$1,463.49; per-row G/L = value − cost ✓ ×15. Half-cent display rounding on four rows — USO 153.455 × 37 = $5,677.835 → $5,677.83 · TBT 39.2599 × 14 = $549.6386 → $549.63 (today $8.3986 → $8.39) · AAPL 319.415 × 15 = $4,791.225 → $4,791.22 · APD 293.7525 × 2 = $587.505 → $587.50 — broker display precision, not transcription errors. Lot arithmetic: 77P $231.26 = 20/25 × $289.08 ✓ and XLE $227.67 = ½ × $455.34 ✓ ⇒ sales at lot basis, not re-basings. RH card-derived costs match the recorded $300 / $220 / $53 ✓. Ledger: gross − costs = net ✓ ×4 ($30.00−1.56 · $214.00−0.66 · $393.00−0.66 · $655.00−0.68); Σ $1,288.44 = pending ✓. **Closed this pass:** D-43/D-51 (85P SOLD 9/10) · D-50 (77P ×5 SOLD 9/10) · D-52 (QQQ 715P SOLD 9/10) · D-46 → D-49 · D-48 · D-47 existence half. Closed rows' full text → the rotation record.*

*📦 **Rotated 2026-09-10 → `_archive/STATUS_ROTATION_2026-09-10.md` (cite as history, never current):** the 9/9 USO 135C execution-update note · Aug-21 EXPIRED event-box + thesis-put rows (incl. the OZK subsection) · July–Aug QQQ put rows · Robinhood VLY 14P / USO 128C / QQQ 696P · closed D-43/46/48 text and the round-1 D-50/51/52 text, each with its 9/10-ledger resolution.*

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (7/18 re-base + amendment #1 = current). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All marks/values `[Fidelity positions, 9/10 ~10:3x ET intraday]`. DTE counted from 9/10.*

| Ticker | Type | Qty | Cost | Mark 9/10 | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | 15 | $23.64 | $319.415 | $4,791.22 | **+1,250.89%** | +$4,436.55 (today +$61.12). qty 15 unchanged; the 5-sh sale predates 7/30, date/price unrecorded (D-1). 52-wk 225.95–344.57 |
| GLD | Stock | 16 | $373.59 | $400.28 | $6,404.48 | **+7.14%** | +$426.98 (today −$49.12; −$180.32 vs 9/3). MIDAS domain. Largest position by value; last add 7/31. 52-wk 326.19–509.70 |
| USO | Stock | 37 | $122.28 | $153.455 | $5,677.83 | **+25.49%** | +$1,153.56 (today +$128.94, the book's mover; +$437.52 vs 9/3). Will's Hormuz-gap entry (BRENT). ⚠️ Gate proximity, NOT adjudication (rule 7): **WQ-200 LINE-1 harvest** *"≥$152.96 official close"* (OPEN, due 9/11 — PROME context) — 9/9 official close = 153.455 − 3.485 = **$149.97 (derived from the capture's Δ), BELOW the line**; 10:3x intraday 153.455 is above it, but the gate keys on the CLOSE. IRA energy sleeve = 37 sh + XLE 65C ×1 = **$5,806.83 = 14.7%** (RH 150/165 spread ≈$501 derived, separate). 52-wk 65.99–154.83 (new high) |
| APD | Stock | 2 | $294.79 | $293.7525 | $587.50 | **−0.36%** | −$2.07 (today −$2.98) Thesis tag still unassigned (open since 7/30). 52-wk 229.11–314.87 |
| TBT | Stock | 14 | $34.63 | $39.2599 | $549.63 | **+13.36%** | +$64.81 (today +$8.39). 2× UST short — duration-short leg (BOND/TERRY). 52-wk 31.69–39.41 |
| ~~**USO**~~ | **$135C Oct-16** | **0** | $7.11 | — | $0.00 | **CLOSED** | SOLD 9/9 ×1 @ $17.55, net $1,754.30 ([receipt](../PROME/reports/2026-09-09_USO135C-sale-receipt.md)); realized +$1,043.64; absence broker-verified 9/10; first sale 9/2 price UNKNOWN (WQ-167). D-48 closed |
| XLE | $65C Sep-30 | **1** | $2.28 | $1.29 | $129.00 | −43.34% | −$98.67 (today −$41 / −24.12%). **qty 2→1 BROKER-VERIFIED — one contract SOLD, NOT among the ledger's visible rows (all Sep-10) ⇒ before today or outside the crop; date/price UNKNOWN; basis $227.67 = ½ × $455.34.** WQ-168 ⑦ ruled SELL BOTH at the bid on the 9/9 open unless XLE closed ≥$66.50 on 9/8 (DOCKET L252/L253 — fill UNKNOWN). **The surviving ×1 has NO ruling on file.** 20 DTE. See **D-49** |

*Not on the 9/10 view: **VLO** (TRY-BRENT-REFINER, 3× approved 8/27) ⇒ unfilled in the IRA; Robinhood stocks card unread · **STNG** (D-17) · **QQQ** shares (day-trade class, D-44) · **TLT $85P** (SOLD 9/10) · **QQQ $715P Sep-10** + **USO $153C Sep-11** (day-trade class, both SOLD 9/10).*

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book. The five Aug-21-2026 EXPIRED rows (KRE 60P · QQQ 710P · OZK 45P/42.5P · KELYA 7.5P; broker-confirmed, realized −$2,816.72 total) were rotated 9/10 → the rotation record.

| Position | Expiry | Qty | Cost | Outcome |
|----------|--------|-----|------|---------|
| ~~**VIX $20C/$25C call debit spread** (`VIXW`)~~ | Aug-05-2026 | ~~4~~ | $0.70 net debit | **✅ CLOSED 2026-07-30 ~09:50 ET — REALIZED −$111.60 (−38.8%).** `TRY-VIOLET-VIXCS`. One spread ticket at net $0.45 credit on the mandatory date; exit legs broker-confirmed 8/2 + 8/29 (+$176.10 net). Open: TERRY card §10 grade + PB-0003 close; VIOLET settle re-grade |

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, **on no PROME rail and owned by no agent**. Recorded so it is not invisible, not because the fleet manages it. Full ticket record 7/20–8/28 (**class ≈ −$1,812.89 8/3–8/28, ≈ −$4,080 since 7/20**; the July–Aug rows → the rotation record) → this file at `183068dd1` + the 8/29 transcription. WQ-97 ("23 QQQ, rec SELL") was executed on 20 of 23 by 8/28; **the residual 3 sh are ABSENT from the 9/3 and 9/10 views.** 9/10 ledger: QQQ 715P SOLD @ $6.55 (+$399.66) and a **USO Sep-11 $153C ×1** SOLD @ $2.14 — a leg on no view, entry UNKNOWN (D-53).

| Position | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|----------|--------|-----|------|------|-------|-----|------|
| ~~**QQQ $715P**~~ | Sep-10-2026 — **SOLD 9/10 (ledger)** | ~~1~~ | $2.55 *(basis $254.66)* | — | — | **+$399.66 realized** | Sell to Close ×1, limit $6.45 (Day), **filled $6.55, net $654.32** `[Fidelity activity, 9/10]` vs basis $254.66 on the 9/9 screenshot (`PROME/research/2026-09-09-position-review/snapshot.csv`; a $255.67 figure in PROME's round-2 note is not in that artifact — $254.66 used). Bought 9/9, between captures. Separate from Robinhood's 8/31 put (D-28). D-52 closed |
| ~~**USO $153C**~~ | Sep-11-2026 — **SOLD 9/10 (ledger); ENTRY unrecorded** | ~~1~~ | UNKNOWN | — | — | **UNRECORDED (entry)** | Sell to Close ×1, limit $2.06 (Day), **filled $2.14, net $213.34** `[Fidelity activity, 9/10]`. **On no positions view (9/3 · 9/9 · 9/10) — opened and closed between captures.** Entry date/price UNKNOWN ⇒ realized UNKNOWN, not zero. Will-direct, no rail, no owner. See **D-53** |
| ~~**QQQ**~~ | — | ~~3~~ | $714.74 | — | — | **UNRECORDED (sale)** | **GONE 9/3, still absent 9/10** (8/28: 3 sh @ $716.43; basis $2,144.23). Labeled reading SOLD (the 8/28→9/3 bridge fit it), date/price UNKNOWN. Struck so the parser carries no phantom. See **D-44** |

## Fidelity — Thesis Puts

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| **$77P** | **Sep-30** | **20** | **$0.12** *(broker basis $231.26 = 20/25 × $289.08; fees-in $0.11563)* | $0.06 | $120.00 | **−$111.26 / −48.12%** (today +$40 / +50%). **qty 25→20 — 5 contracts SOLD 9/10 @ $0.06 (limit $0.06 Day), net $28.44 `[Fidelity activity, 9/10]` vs lot basis $57.82 ⇒ −$29.38 realized; WQ-168 ④ had ruled HOLD ×25 to expiry — a deviation, recorded not graded (D-50 closed).** 20 DTE. ⚠️ Gate proximity, NOT adjudication (rule 7): harvest line *"half at ≥3×"* (PB-0002b: 10 ct at ≥$0.3469 fees-in) — at $0.06 = **0.52× fees-in basis**; exit gate GATE-TERRY-007 *"FIVE CONSECUTIVE official FRED DGS10 closes <4.50% ⇒ TERRY builds exit proposal → Will [Approve]"* — **0 of 5** as last owner-graded (9/1 DGS10 4.79); no DGS10 in this capture. 7/31 harvest 5 ct @ $0.37336 = +$128.86 realized (PB-0002a). See **D-31** |
| ~~$85P~~ | ~~Sep-30~~ — **SOLD 9/10 (ledger)** | ~~1~~ | $2.52 *(basis $251.67)* | — | — | **+$140.67 realized** — Sell to Close ×1, limit $3.92 (Day), **filled $3.93, net $392.34** `[Fidelity activity, 9/10]`. WQ-168 ⑤ had ruled SELL @ $2.60 (TRY-EXIT-TLT85P); Will re-priced the limit to $3.92 himself — the ledger answers WQ-201 (PROME closes the row). D-43/D-51 closed; TERRY logs the card |
| $82P | Oct-16 | 2 | $1.68 | $1.67 | $334.00 | **−$1.35 / −0.41%** (today +$76 / +29.45%, the put book's mover — back to basis from 1.02 on 9/3). 36 DTE. No ruling recorded on this file |

*Duration-short complex (TBT + two TLT legs) open G/L at 10:3x: +$64.81 − $111.26 − $1.35 = **−$47.80** (9/3: −$276.80 across four legs — not like-for-like: 9/10 realized 85P +$140.67, 77P ×5 −$29.38), against the +$128.86 realized on the 7/31 harvest.*

### KRE — regional banks (REGINALD)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $60P | Dec-18 | 2 | $2.57 | $0.35 | $70.00 | −$443.34 / −86.37% (today −$22). 99 DTE |
| $60P | Dec-18 | 3 (M) | $2.93 | $0.35 | $105.00 | −$773.02 / −88.05% (today −$33) — Fidelity multi-lot marker; **five** Dec-18 KRE 60P total across the two lots. 99 DTE |
| $60P | Sep-30 | 2 | $2.27 | $0.05 | $10.00 | −$443.35 / −97.80% (today $0) — **20 DTE. RULED WQ-168 ⑥: LAPSE.** Rides to $0 |

### WAL (REGINALD) — Sep-18s (the 7/21 print resolved NOT-FIRED)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $70P | Sep-18 | 1 | $7.69 | $0.05 | $5.00 | −$763.67 / −99.35% (today −$8) — **8 DTE. RULED WQ-168 ①: LAPSE** (**re-opens only if WAL closes <$71 in the week of 9/14**; no WAL price in this capture). Duration-rolled to the Robinhood Dec-18 $70P ×1, now broker-verified (D-47) |
| $67.5P | Sep-18 | 1 | $7.51 | $0.05 | $5.00 | −$745.67 / −99.34% (today $0) — **8 DTE. RULED WQ-168 ②: LAPSE** |

*(The Robinhood **WAL $77.5P Aug-21 ×1** — Will confirmed the sale in-session 2026-08-18; date/proceeds still unrecorded ⇒ P&L UNRECORDED, not zero — D-18. Struck-through in the Robinhood table, retained.)*

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18 | 1 | $11.85 | $0.80 | $80.00 | −$1,104.67 / −93.25% | BROCK thesis vehicle. 0.60 [9/3] → 0.80 (today −$24). 99 DTE. No ruling on file |
| HBAN | $16P | Oct-16 | 2 | $0.96 | $0.30 | $60.00 | −$131.34 / −68.65% | EXIT-THESIS dust (Will 7/18) — rides to expiry, zero effort. 0.20 [9/3] → 0.30 (today −$4). 36 DTE |

## Robinhood — satellite account (Individual)

> ⚠️ **PARTIAL CAPTURE 2026-09-10 — Options card ONLY** (per-line P/L $ and %; no qty, marks, cash, stocks card, event contracts, timestamp). Costs/values **DERIVED** (cost = P/L ÷ P/L%; value = cost + P/L), labeled. Account value / buying power last read 8/28 (**$414.81 / $174.90**; "13 days left" banner + ≈$8.67 residue = D-37/D-20); event-contract exposure invisible. The block stays machine-class `unverified` by design (no Mark column). Rows absent from a capture are **retained, not deleted**.

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **WAL $70P** | **Dec-18-2026** | 1 | **$2.20 ($220)** — card-derived $219.97 ✓ | ≈$233.00 *(derived: $220 + $13.00)* | ✅ **BROKER-VERIFIED 9/10 — RH Options card +$13.00 / +5.91%** | Existence + cost verified (D-47 existence half CLOSED; was Will's word 9/2). TRY-WAL-ROLL70 filled in ROBINHOOD, not the IRA the card named (TERRY card §5c). Guard = **GATE-TERRY-ROLL70-EXIT** *"WAL OFFICIAL CLOSE ≥ $81.90 on THREE CONSECUTIVE sessions"* — **0-of-3 as last graded (9/2 close $79.12)**; no WAL price in this capture (REGINALD grades; rule 7, not adjudicated). $4.40 harvest GTC resting status **permanently UNKNOWN (WQ-167), not an ask**. Time stop Fri 12/4. 99 DTE. See **D-47** |
| ~~**QQQ $715P**~~ | ~~8/31/2026~~ — **EXPIRED 8/31, outcome UNRECORDED** | ~~1~~ | ≈$193.24 | — | ⚠️ **UNRECORDED — not an ask (TERRY ④, 9/3)** | No QQQ line on the 9/10 Options card — consistent with expired/closed, still not a booked outcome (expired OTM / sold intraday / exercised — none verified). D-28 carried |
| **USO $150/$165 call spread** | Sep-18 | 1 | **$300.00 net debit** — card-derived $300.00 ✓ | ≈$501.00 *(derived: $300 + $201.00)* | ✅ **BROKER-VERIFIED 9/10 — card +$201.00 / +67.00%** | **RULED WQ-168 ③: HOLD.** 8 DTE. BRENT tail-rider; BE ~$153 vs USO 153.455 [Fidelity 10:3x]; max $1,500 at ≥$165. Was ≈$41 on 8/28 |
| **KRE $25P** | 1/15/2027 | 1 | $53.00 — card-derived $53.00 ✓ | ≈$1.00 *(derived)* | ✅ **BROKER-VERIFIED 9/10 — card −$52.00 / −98.11%** | Deep-OTM lottery, carried since 7/20; unchanged since 8/28. 127 DTE |
| ~~**WAL $77.5P**~~ | **Aug-21** | ~~1~~ | — | — | ✅ **CONFIRMED SOLD (Will 8/18)** | Absent 8/14, 8/28, 9/10 card. **Date/proceeds unrecorded ⇒ P&L UNRECORDED, not zero.** See **D-18** |
| T | stock | 1 | — | — | ⚠️ **absent 8/14 + 8/28; stocks card not captured 9/10** | 1 share (~$22 on 7/20) — larger than the $8.67 residue, so "hidden" does not fit. **Hypothesis: sold**, unconfirmed. See D-20 |

---

## ⚠️ Reconcile discrepancies (9/10)

> Built by ANVIL against the 9/10 ~10:3x ET intraday Fidelity positions view + the Robinhood Options card + the Fidelity Activity & Orders view (four rows, all 9/10; earlier rows outside the crop) — no Robinhood cash/stocks. **Nothing here has been resolved by invention**; every conjecture is labeled; broker view > Will's word > PROME queue/SCRATCH context. Ranked by decision urgency, **expiring first** (Sep-10 → Sep-18 → Sep-30 → the rest); "Will decides" separated from "owner decides." **Permanently UNKNOWN by WQ-167 — never listed as asks:** the 9/2 USO 135C sale price · the ROLL70 $4.40 GTC's resting status. **Closed this pass:** D-43/D-51 (85P SOLD 9/10 @ $3.93) · D-50 (77P ×5 SOLD 9/10 @ $0.06) · D-52 (QQQ 715P SOLD 9/10 @ $6.55) · D-46 → D-49 · D-48 · D-47 existence half. **Still owed: the activity view's rows BEFORE 9/10** — they date the XLE ×1 sale (D-49), the USO 153C entry (D-53) and the QQQ 3 sh (D-44), closing D-45.

### EXPIRING / DATED — Will decides

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-49** | **XLE $65C Sep-30 — ONE of two SOLD; the ruling was SELL BOTH; the survivor has no rule** | 🟠 20 DTE · live contract, no ruling | qty 2→1; basis $227.67 = ½ × $455.34 ⇒ one contract left at lot basis. **Not among the ledger's four visible rows (all 9/10)** ⇒ sold before today or outside the crop. Mark 1.29 / $129 (−43.34%; today −$41). WQ-168 ⑦: hold through OPEC+ 9/6; **XLE 9/8 close ≥ $66.50 ⇒ hold on; else SELL BOTH at the bid on the 9/9 open** (DOCKET L252/L253 — recorded fill UNKNOWN) | (a) partial fill of a 2-lot at the 9/9 open · (b) a deliberate 1-lot · (c) 9/8 closed ≥$66.50 and the sale is unrelated to ⑦. **ANVIL picks none.** Either way ⑦ is consumed and the ×1 rides without a rule | **Will** — sale date/price + is the ×1 intended? TERRY re-registers or closes TRY-EXIT-XLE65C on the answer |
| **D-53** | **USO Sep-11 $153C ×1 — SOLD 9/10 @ $2.14, net $213.34; ENTRY unrecorded; on no positions view** | 🟠 entry owed (leg closed) | Ledger row only `[Fidelity activity, 9/10]`; absent from the 9/3, 9/9 and 9/10 views ⇒ opened and closed between captures. Will-direct, day-trade class, no rail | Entry between 9/3 and 9/10, cost UNKNOWN ⇒ realized UNKNOWN, not zero; the −$190.35 bridge residual (D-45) is the only constraint | **Will** — entry date/price, or the ledger's earlier rows |
| **D-45** | **Cash bridge 9/3 → 9/10: −$190.35 unattributed after the ledger** | 🟠 earlier ledger rows owed | $18,025.71 + 135C $1,754.30 (in cash — pending = today's four fills to the cent) − QQQ 715P buy $254.66 = **$19,525.35 expected vs $19,335.00 cash ⇒ −$190.35** | = XLE ×1 proceeds − USO 153C entry cost − anything else (interest, an unseen ticket). Labeled arithmetic — e.g. XLE ≈$130–190 against a 153C entry ≈$320–380 would fit; **not a claim** | **Will** — the Activity view scrolled to before 9/10 |
| **D-44** | **QQQ 3 sh — GONE 9/3, absent 9/10; sale date/price UNKNOWN** | 🟡 fact owed | 8/28: 3 @ $716.43, basis $714.74; absent both views since | SOLD — labeled, supported by the 8/28→9/3 bridge, still not proof | **Will** — the same activity view dates it |

### RULED / GATED — owner decides (nothing owed by Will today)

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| WQ-168 ①② | **WAL $70P + $67.5P Sep-18 (Fidelity) ×1 each — LAPSE** | 🟡 8 DTE | Both $0.05 / $5.00; −99.35% / −99.34%. 70P re-opens only if WAL closes <$71 in the week of 9/14; no WAL price in this capture | Nothing — the rule is fully specified | REGINALD watches the <$71 trigger |
| WQ-168 ③ | **RH USO $150/$165 Sep-18 spread ×1 — HOLD** | 🟡 8 DTE · in the money | Card +$201.00 / +67% ⇒ ≈$501 derived on $300; USO 153.455 vs BE ~$153; max $1,500 at ≥$165 | Realizable value not on the card (spread bid unknown) | TERRY / BRENT — a harvest is a proposal to Will, not a gate |
| WQ-200 | **USO 37 sh — LINE-1 harvest *"≥$152.96 official close"* (PROME context, due 9/11)** | 🟡 grade at tonight's close | 9/9 official close $149.97 (derived: 153.455 − 3.485) = **below the line**; 10:3x intraday 153.455 = above it. +$1,153.56 / +25.49% | None — gate keys on the CLOSE; ANVIL reports proximity only (rule 7) | TERRY grades the 9/10 official close → Will (WQ-200) |
| **D-31** | **TLT $77P Sep-30 ×20 — HOLD (WQ-168 ④, as it stands after D-50)** | 🟡 20 DTE / 14 sessions | $0.06 / $120 on $231.26 (−48.12%). 0.52× fees-in; harvest *"half at ≥3×"* far away. GATE-TERRY-007 **0-of-5** as last graded 9/1 (DGS10 4.79) | Registry's own logic: *"NO-VERDICT is the correct read if expiry beats the count"* — five sub-4.50 official closes inside 14 sessions | TERRY grades DGS10 daily → Will only on a proposal |
| WQ-168 ⑥ | **KRE $60P Sep-30 ×2 — LAPSE** | 🟡 20 DTE | $0.05 / $10.00 (−97.80%) | Nothing | Rides to $0 |
| **D-47** | **RH WAL Dec-18 $70P ×1 — existence + cost BROKER-VERIFIED 9/10; guard un-graded since 9/2** | 🟡 99 DTE | Card +$13.00 / +5.91% ⇒ cost ≈$220 ✓, value ≈$233 derived. GATE-TERRY-ROLL70-EXIT **0-of-3 at the 9/2 close $79.12**; time stop 12/4 | $4.40 GTC status permanently UNKNOWN (WQ-167) ⇒ harvest is a manual act by Will, not a control. Residue = the guard needs a WAL close series REGINALD owns | REGINALD grades / TERRY proposes |

### CARRIED — need a capture or one line from Will

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-28** | **Robinhood QQQ $715P ×1 — expired 8/31, outcome UNRECORDED** | 🟡 carried | Cost ≈$193.24; QQQ closed 716.43 on 8/28. No QQQ line on the 9/10 Options card (consistent, not a booking). TERRY ④ 9/3: UNRECORDED, not an ask | Expired OTM (≈−$193) / sold / exercised — none verified | Next Robinhood history view |
| **D-17** | **STNG — appears in no capture, nowhere in FORGE (carried)** | 🟠 carried | Absent from every capture since 8/2 and the 7/30–8/28 activity window. March-2026 record (STNG ×2 @ $70.01, sold next day) | (a) the 7/21 note recalled the March position · (b) closed pre-7/30 · (c) a third account. ANVIL picks none | **Will** — one line |
| **D-20** | **Robinhood: T share absent ×2 + event contracts invisible + ≈$8.67 residue (8/28)** | 🟡 carried | Stocks card and cash not captured 9/10 | Hypothesis: T sold; event-contract exposure of unknown size remains the live risk | **Will** — a full Robinhood view |
| **D-1** | **AAPL 5-sh sale — date + price unrecorded** | 🟡 carried | qty 15 Will-confirmed 8/2 and on every view since; no AAPL activity 7/30–8/28 ⇒ predates 7/30 | ~$565 cash class | Will / an older activity window |
| **D-18** | **Robinhood WAL $77.5P Aug-21 — sale CONFIRMED (8/18), P&L UNRECORDED** | 🟡 carried | Existence closed 8/18 | Date/proceeds need a Robinhood history view; do not book at $0 | Will (not urgent) |
| **D-37** | **Robinhood ≈$360 inflow (8/14→8/28) + "13 days left" banner** | 🟡 carried | Arithmetic recorded 8/29; nothing trades off it | Deposit/transfer hypothesis; banner referent unknown | Will (one line) |

---

## Immediate Actions (9/10 session state)

| Item | State | Owner |
|---|---|---|
| **★ Fidelity Activity view — rows BEFORE 9/10** (D-49 · D-53 · D-45 · D-44) | 🟠 Dates the XLE ×1 sale and the USO 153C entry; attributes −$190.35 | **Will** — scroll back and post |
| **XLE 65C ×1 survivor — no ruling on file** (D-49) | 🟠 20 DTE; ⑦ consumed | **Will** intent → TERRY re-registers or closes the card |
| **WQ-200 USO LINE-1 harvest ≥$152.96 official close** | 🟡 9/9 close $149.97 (derived) below; intraday above — grade the CLOSE | TERRY grades → **Will** (due 9/11) |
| **Sep-18 cluster** (WAL pair LAPSE; RH USO 150/165 HOLD ≈$501) | 🟡 8 DTE; nothing owed | REGINALD / TERRY-BRENT |
| **TLT 77P ×20 HOLD; 5 sold 9/10 off-ruling; GATE-TERRY-007 0-of-5** (D-31) | 🟡 20 DTE | TERRY |
| **Robinhood full capture owed** (D-20 · D-37 · D-28 · D-18) | 🟡 Account value still 8/28 vintage | **Will** |
| **STNG · AAPL 5-sh** (D-17 · D-1) | 🟡 Carried; one line each | **Will** |
| **APD thesis tag** | 🟡 Unassigned since 7/30; −0.36% | PROME / Will |

---

*History → `_archive/JOURNAL.md` | Prior reconciles (9/3, 8/29, 8/14, 8/2, 7/30, 7/20, 7/16, 5/21) preserved in git history | Full-portfolio Feb snapshot → `PORTFOLIO.md` (**FROZEN/superseded, historical only — never cite as live**) | Position truth = Will/broker direct (off-repo) | Transcription of record for this pass (Fidelity positions + activity, Robinhood Options card) → `PROME/data/2026-09-10_broker-capture-TRANSCRIPTION.md`*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumer: `AGENTS/TERRY/scripts/positions_from_forge.py` (desk-dashboard Positions tab; keys on table headers, section names, and cell text — markdown emphasis and struck-through rows are visible to it). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069 n=3 — the 7/30 reconcile broke the parser silently). New consumers: add yourself to this list in the same commit that starts parsing. *(9/10 pass: no section/header renames except the Longs column `Mark 9/3` → `Mark 9/10`, which the parser binds by prefix (hardening #3, same rename class as every prior pass); no new columns; THREE rows newly struck-through (`~~`) = the parser's CLOSED marker — the day-trade QQQ $715P Sep-10 and TLT $85P Sep-30 (both SOLD 9/10 per the ledger) and a NEW struck day-trade row, USO $153C Sep-11 (sold 9/10, never on a view); the Robinhood block keeps no Mark column ⇒ class `unverified` unchanged. 9/10 ROTATION (PROME-authorized): terminal rows moved to `_archive/STATUS_ROTATION_2026-09-10.md` — the `### OZK` subsection removed whole (only struck rows), no other section/header change; live set unchanged. Parser re-run post-rotation: 15 live / 12 withheld (7 closed · 1 event_box · 4 unverified), 0 warnings, selftest PASS — figures in the 9/10 reconcile report.)*
