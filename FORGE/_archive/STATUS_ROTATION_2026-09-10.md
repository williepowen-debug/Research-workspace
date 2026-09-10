# FORGE/STATUS.md — ROTATION RECORD 2026-09-10 (terminal material, verbatim)

> **Source:** `FORGE/STATUS.md` as edited by ANVIL 2026-09-10 (reconcile to the 9/10 ~10:3x ET intraday capture + Fidelity activity ledger; working copy at rotation time — chunk F1 is taken from `git show HEAD:FORGE/STATUS.md`, HEAD `8e7a399a8`). **Rotated:** 2026-09-10 ~11:0x ET, PROME-authorized (byte-cap relief; `prome-6d`). **Rotation 2 — 2026-09-10 ~16:5x ET, ANVIL on PROME's instruction (cap relief for the CLOSE + 16:10 pass): Chunks G–H below, verbatim; source working copy pre-rotation = `31891 B (wc -c)  168 lines (wc -l)  crc32 698795158  crc32-no-final-nl 1885830741`.** **Cite as history, never current** — every row here is terminal (expired, closed, or a discrepancy resolved by the 9/10 ledger); the live mirror is `FORGE/STATUS.md`. Rows are verbatim; the table header each chunk belonged under is named in the chunk title. crc32 per chunk = `PROME/tools/measure.py` on the chunk's lines (each line newline-terminated).

## Chunk A — 9/9 USO 135C execution-update note (header blockquote; receipt detail)
*measure.py: 478 B (wc -c)  1 lines (wc -l)  crc32 1569397136  crc32-no-final-nl 3966296790*

> **Execution update — September 9, 2026:** USO Oct-16 $135C remaining ×1 SOLD @ $17.55, net $1,754.30, settlement date 9/10 ([broker receipt](../PROME/reports/2026-09-09_USO135C-sale-receipt.md)); realized +$1,043.64 on the $710.66 remaining-lot basis; B/C management checks discharged. **The 9/10 reconcile below carries the post-sale balances** — the capture shows the call absent and cash + pending up $2,597.73 vs 9/3, of which this receipt explains $1,754.30 (D-45).

## Chunk B — Fidelity Event boxes: Aug-21-2026 EXPIRED rows (table header: `| Position | Expiry | Qty | Cost | Outcome |`)
*measure.py: 843 B (wc -c)  5 lines (wc -l)  crc32 2978293685  crc32-no-final-nl 2175066391*

| ~~**KRE $60P**~~ | Aug-21-2026 | ~~3~~ | $2.70 | **✅ EXPIRED — broker-confirmed (activity row Aug-24). REALIZED −$809.02.** Ruled LAPSE 8/14 |
| ~~**QQQ $710P**~~ | Aug-21-2026 | ~~1~~ | $2.4566 | **✅ EXPIRED — broker-confirmed (activity row Aug-24). REALIZED −$245.66.** Day-trade class; bought 8/20, never on a positions view |
| ~~**OZK $45P**~~ | Aug-21-2026 | ~~4~~ | $3.69 | **✅ EXPIRED — broker-confirmed (activity row Aug-24). REALIZED −$1,474.70.** Ruled RIDE to OPEX 8/4 |
| ~~**OZK $42.5P**~~ | Aug-21-2026 | ~~1~~ | $2.12 | **✅ EXPIRED — broker-confirmed (activity row Aug-24). REALIZED −$211.67.** Ruled RIDE to OPEX 8/4 |
| ~~**KELYA $7.5P**~~ | Aug-21-2026 | ~~1~~ | $0.76 | **✅ EXPIRED — broker-confirmed (activity row Aug-24). REALIZED −$75.67.** Ruled LAPSE 8/14; LABOR thesis-grade at OPEX |

## Chunk C — Fidelity Off-thesis / day-trade class: July–Aug QQQ put rows (table header: `| Position | Expiry | Qty | Cost | Mark | Value | P&L | Note |`)
*measure.py: 747 B (wc -c)  4 lines (wc -l)  crc32 3295973451  crc32-no-final-nl 447775701*

| ~~**QQQ $687P**~~ | Aug-03-2026 — **LIQUIDATED 8/3** | ~~3~~ | $2.81 | — | — | **−$839.18 realized** | Activity-confirmed 8/29 (D-12 closed). Basis $841.99; Will's "sold at a loss" recall was right in direction, near-total in size |
| ~~QQQ $680P~~ | Jul-31-2026 — CLOSED 7/31 | ? (2 fills) | — | — | — | **−$1,005.48 realized** | Bought 7/30 in two fills (−$599.33, −$414.66); sold 7/31 +$8.51 (D-14 = fill-pairing inference only) |
| ~~QQQ $672P~~ | Jul-31-2026 — EXPIRED WORTHLESS | ? | — | — | — | **−$416.66 realized** | Bought 7/30 −$416.66; EXPIRED row dated Aug-03 |
| ~~QQQ $675P~~ | Jul-30-2026 — SOLD 7/30 | 1 | $3.92 | — | — | **−$389.67 realized** | Liquidation +$1.99 on 7/30 (activity) |

## Chunk D — Thesis-put tables: struck Aug-21 rows — KRE row (from `### KRE`, header `| Strike | Expiry | Qty | Cost | Mark | Value | P&L |`), the whole `### OZK` subsection, KELYA row (from `### Other puts`, header `| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |`)
*measure.py: 1011 B (wc -c)  8 lines (wc -l)  crc32 3249632547  crc32-no-final-nl 3741513746*

| ~~$60P~~ | ~~Aug-21~~ — **✅ EXPIRED 8/21, broker-confirmed** | ~~3~~ | $2.70 | — | — | **−$809.02 realized** — activity row Aug-24. Ruled LAPSE 8/14; event-box entry is the record, row retained (D-36) |
### OZK (REGINALD) — Aug-21s (the 7/21 print resolved NOT-FIRED)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| ~~$45P~~ | ~~Aug-21~~ — **✅ EXPIRED 8/21, broker-confirmed** | ~~4~~ | $3.69 | — | — | **−$1,474.70 realized** — activity row Aug-24. Ruled RIDE to OPEX 8/4. Row retained (D-36) |
| ~~$42.5P~~ | ~~Aug-21~~ — **✅ EXPIRED 8/21, broker-confirmed** | ~~1~~ | $2.12 | — | — | **−$211.67 realized** — activity row Aug-24. RIDE to OPEX. Row retained (D-36) |
| ~~KELYA~~ | ~~$7.5P~~ | ~~Aug-21~~ — **✅ EXPIRED 8/21, broker-confirmed** | ~~1~~ | $0.76 | — | — | **−$75.67 realized** | LABOR thesis. Activity row Aug-24. Ruled LAPSE 8/14; LABOR's thesis-grade at OPEX. Row retained (D-36) |

## Chunk E — Robinhood satellite: terminal rows (table header: `| Position | Expiry | Qty | Cost | Value | State | Note |`)
*measure.py: 562 B (wc -c)  3 lines (wc -l)  crc32 1403096131  crc32-no-final-nl 494207966*

| ~~**VLY $14P**~~ | ~~8/21~~ — **EXPIRED 8/21 (presumed worthless)** | ~~1~~ | $40.00 | — | **presumed −$40.00** | Not on the 9/10 card (consistent). Ruled LAPSE 8/14; no RH activity view ⇒ $0 is a labeled presumption (D-36). TERRY EbE write-back owed |
| ~~USO $128C~~ | 7/22 — **EXPIRED** | 1 | — | — | **presumed worthless** | Hormuz leg (~−$100 class). D-5 closed as far as a view can close it |
| ~~QQQ $696P~~ | 7/20 EXPIRED | 1 | — | — | **CLOSED ~−$455** | Will-reported 7/20: recovered ~$8; QQQ closed ATM $696. Day-trade class |

## Chunk F1 — Closed discrepancy rows D-43 · D-46 · D-48, verbatim from `git show HEAD:FORGE/STATUS.md` (9/3 reconcile text, HEAD `8e7a399a8`); header `| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |`
*measure.py: 1732 B (wc -c)  3 lines (wc -l)  crc32 1463774635  crc32-no-final-nl 1488125528*

| **D-43** | **★ TLT $85P Sep-30 — ONE of two contracts SOLD; the other may be a WORKING order** | **🔴 now** (order status) · 27 DTE | Qty 2→1 broker-verified; remaining basis $251.67 = exactly half of 8/28's $503.35 ⇒ one contract sold, not a re-basing. WQ-168 ⑤ (ruled 12:45 9/3) = SELL 2 @ $2.60 limit; TERRY holds TRY-EXIT-TLT85P as STAGED, placement unconfirmed. Last **2.72** at 15:07 (> $2.60) | (a) partial fill of today's 2-lot @ $2.60 with one still working · (b) a 1-lot order · (c) an earlier/separate sale. **ANVIL picks none.** A resting $2.60 limit with last at 2.72 would ordinarily be marketable — but Last ≠ bid, so this is a question, not a contradiction. **Ask: sale date + price, and is the second contract still working?** | **Will** — one line (TERRY logs it on the card) |
| **D-46** | **XLE $65C Sep-30 ×2 — DATED EXIT, 9/8 close → 9/9 open** | 🟡 3 sessions · 27 DTE | $1.60 / $320 (−29.73%). WQ-168 ⑦ RULED: hold through OPEC+ 9/6; **XLE 9/8 close ≥ $66.50 ⇒ hold on (TERRY registers a time stop); else SELL BOTH at the bid on the 9/9 open** — DOCKET L252/L253; PROME consumer-reads the 9/8 close if TERRY is dark | None — the rule is fully specified; ANVIL reports the mark only | Will's hand at the broker 9/9 (a fired dated rule is held, not re-litigated — TERRY RISK_RULES #12) |
| **D-48** | **USO $135C Oct-16 — CLOSED September 9** | RESOLVED | Remaining ×1 sold at $17.55; net $1,754.30; settles September 10. B/C discharged; zero remaining. | Remaining-lot realized gain $1,043.64 on $710.66 basis; first-sale price permanently UNKNOWN (WQ-167). | [Receipt](../PROME/reports/2026-09-09_USO135C-sale-receipt.md); owner records consume this closure |

## Chunk F2 — Discrepancy rows D-52 · D-51 · D-50 as written in ANVIL's 9/10 round-1 working copy (never committed; superseded the same morning by the activity ledger — resolutions below)
*measure.py: 1869 B (wc -c)  3 lines (wc -l)  crc32 3536219809  crc32-no-final-nl 3296799754*

| **D-52** | **★ QQQ $715P Sep-10 ×1 — EXPIRES TODAY; GONE from the 10:3x view** | **🔴 today** (0 DTE) | On Will's 9/9 screenshot at $2.40 / $240, basis $254.66. Absent 9/10 ~10:3x. QQQ $710.25 at 10:26 ET `[live fetch, PROME]` ⇒ ≈$4.75 ITM. Expiry is tonight, so it has NOT expired | (a) sold 9/10 before 10:3x (≈$475 gross at intrinsic — plausibility, not a figure) · (b) sold 9/9 after the screenshot · (c) exercised early (would leave −100 QQQ sh; none on the view ⇒ disfavored). **ANVIL picks none.** If still held: a live ITM 0-DTE contract needing a decision before 16:00 — flagged, not adjudicated | **Will** — one line: sold (date/price) or still held? |
| **D-51** | **TLT $85P Sep-30 ×1 — GONE (closes D-43's existence half); price UNKNOWN** | 🟠 fact owed (nothing live) | 9/3: ×1 @ $2.72, basis $251.67. Absent 9/10. WQ-168 ⑤ = SELL @ $2.60 limit (TRY-EXIT-TLT85P, STAGED per TERRY 9/3). **WQ-201 (that limit) is OPEN in `PROME/WILL_QUEUE.md`, due 9/10 — PROME context, not graded here** | (a) the $2.60 limit filled (≈$259 net) · (b) sold otherwise. The 9/3 question "is the second contract still working?" is answered by the view: nothing is | **Will** — date/price; the same line closes WQ-201 and D-43; TERRY logs the card |
| **D-50** | **TLT $77P Sep-30 qty 25→20 — 5 SOLD; the ruling was HOLD ×25 to expiry** | 🟡 20 DTE · deviation to record | Basis $231.26 = 20/25 × $289.08 ⇒ 5 contracts left at lot basis (not a re-basing). Mark 0.06 / $120 (−48.12%; today +$40). WQ-168 ④ ruled HOLD ×25 | Five contracts at $0.03–0.06 ≈ $15–30 gross less ≈$3.25 fees — de minimis; the significance is the deviation from ④, **recorded, never graded by ANVIL**. Changes the PB-0002b harvest-lot math (TERRY's) | **Will** — one line (date/price/intent); TERRY updates the card's lot history |

## Resolutions of chunk F2 by the 9/10 Fidelity Activity & Orders view `[Fidelity activity, 9/10]`
| Row | Resolution |
|---|---|
| D-52 | QQQ Sep-10 715P ×1 Sell to Close, limit $6.45 (Day), filled $6.55, net $654.32; basis $254.66 (9/9 snapshot) ⇒ realized +$399.66. CLOSED (sold, not held) |
| D-51 (and D-43) | TLT Sep-30 85P ×1 Sell to Close, limit $3.92 (Day), filled $3.93, net $392.34; basis $251.67 ⇒ realized +$140.67. Will re-priced the WQ-168 ⑤ $2.60 limit to $3.92 himself; WQ-201 answered. CLOSED |
| D-50 | TLT Sep-30 77P ×5 Sell to Close, limit $0.06 (Day), filled $0.06, net $28.44; lot basis $57.82 ⇒ realized −$29.38. Deviation from WQ-168 ④ HOLD ×25 — RECORDED, never graded. CLOSED |
| D-46 | Consumed: XLE 65C qty 2→1 on the 9/10 view; the survivor's status is the live row D-49 |
| D-48 | USO 135C absence broker-verified on the 9/10 view. CLOSED |

## Chunk G — "Events since the 9/3 reconcile, by label" (header blockquote; 10:3x pass + RH 16:10 events; rotated 16:5x)
*measure.py: 1556 B (wc -c)  1 lines (wc -l)  crc32 2991558360  crc32-no-final-nl 4260331669*

> **Events since the 9/3 reconcile, by label.** **BROKER-VERIFIED (positions view + activity ledger `[Fidelity activity, 9/10]`):** USO $135C Oct-16 absent (matches the 9/9 receipt) · **XLE $65C Sep-30 qty 2→1** (one SOLD — NOT in the ledger's visible rows, date/price UNKNOWN; ⑦ had ruled SELL BOTH 9/9) · **TLT $77P ×5 SOLD 9/10 @ $0.06, net $28.44** (④ had ruled HOLD ×25 — a deviation, recorded not graded) · **TLT $85P ×1 SOLD 9/10 @ $3.93, net $392.34** (limit $3.92 — Will re-priced the $2.60) · **QQQ $715P Sep-10 ×1 SOLD 9/10 @ $6.55, net $654.32** · **USO Sep-11 $153C ×1 SOLD 9/10 @ $2.14, net $213.34 — a leg on no positions view** · CLOSE view: same 15 rows, no qty change after ~10:3x, no new fills · cash + pending +$2,597.73 · **Robinhood `[9/10 16:10]`: USO $150/$165 Sep-18 spread CLOSED ~15:1x by Will's hand, $630.00 vs $300.00 debit ⇒ +$330.00 realized** (WQ-168 ③ had ruled HOLD) · **USO $159C Sep-11 ×1 BOUGHT @ $1.52** (day-trade class) · QQQ $713C 9/10 day trade −$11.00 · WAL 70P +$10.00 (was +$13.00 ~10:3x) · KRE 25P −$52.00 · account **$946.13**. **PROME-SUPPLIED context (queue, not broker):** WQ-201 (TLT 85P limit) — answered by the 85P fill, PROME closes the row · WQ-200 (USO 37-sh card LINE-1 harvest, *"≥$152.96 official close"*) OPEN, due 9/11. **Standing rulings (WQ-168, 9/3) and GATE-TERRY-ROLL70-EXIT:** not amended by this pass; two deviations from WQ-168 are recorded above (④: 5 of 25 sold; ⑦: consumed, the surviving ×1 has no rule) — see the position rows.

## Chunk H — Fidelity day-trade-class struck row: QQQ 3 sh (gone 9/3; D-44 carried live)
*measure.py: 278 B (wc -c)  1 lines (wc -l)  crc32 4254405913  crc32-no-final-nl 4169536310*

| Position | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|----------|--------|-----|------|------|-------|-----|------|
| ~~**QQQ**~~ | — | ~~3~~ | $714.74 | — | — | **UNRECORDED (sale)** | **GONE 9/3, still absent 9/10** (8/28: 3 sh @ $716.43; basis $2,144.23). Labeled reading SOLD (the 8/28→9/3 bridge fit it), date/price UNKNOWN. Struck so the parser carries no phantom. See **D-44** |
