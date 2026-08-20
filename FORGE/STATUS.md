# FORGE — Trading Operations

> **Structured position-truth mirror — reconciled 2026-08-14 (Will screenshot pair, PROME-transcribed; basis: "Will screenshot pair, intraday marks") from ① Will's Fidelity Traditional IRA •1326 positions view and ② the Robinhood Individual account view. ⚠️ MARKS ARE INTRADAY (~09:45 ET, Fri 2026-08-14, market OPEN) — they are NOT closes and NOT settles; do not cite any mark, value or P&L below as a settle. Position truth is off-repo (Will/broker direct); this file is the fleet's parseable mirror and goes stale from the moment it's written.** Refresher flow = Will-on-broker-capture → PROME transcribes → ANVIL reconciles (prior reconciles 2026-08-02, 07-30, 07-20, 07-16, 05-21). Old execution ledger + per-trade folders → `FORGE/_archive/`.
>
> ⚠️ **ACCOUNT SCOPE — TWO ACCOUNTS CAPTURED THIS PASS (first Robinhood capture since 7/20):** Fidelity Traditional IRA •1326 (presumed; D-10 naming confirm still open) **and** Robinhood Individual. **Neither capture is an activity/transactions view** — both are positions views, so *what closed, when, and for how much is NOT in this data*. The Robinhood view additionally warns that **event contracts are not shown** and its stated account value does not fully decompose into the visible rows (**$15.85 unexplained — D-20**). Absence from a positions view is **not** evidence of closure: see **§ Reconcile discrepancies (8/14)** before treating any absence below as closed.

**Updated:** 2026-08-14 [broker capture, **INTRADAY marks ~09:45 ET — not closes**] | **Fidelity cash (money market):** $16,806.53 (45.95%) | **Fidelity positions market value:** $19,772.40 | **Pending activity:** **none shown** *(positions + cash close to the account total exactly, so pending = $0 or is absent from this view — labeled; the 8/2 pending −$1,754.94 has cleared)* | **Fidelity account total:** $36,578.93 *(today +$243.75 / +0.67%; open-position total G/L −$2,215.64 / −10.08%)* | **Robinhood Individual:** **CAPTURED** — account value $102.85 (today +$4.74 / +4.83%), buying power $6.94

*Export arithmetic verified by ANVIL: Fidelity positions $19,772.40 + cash $16,806.53 = **$36,578.93 exact to the cent**; every per-row G/L$ = value − cost basis exactly (21/21 rows); every row's mark × qty (×100 for options) = the stated value exactly (21/21); every row's cost basis / qty rounds to the displayed avg cost (21/21, fees-in); account total G/L −$2,215.64 = the exact sum of open-position G/L, −10.077% on $21,988.04 open basis vs the displayed −10.08% (truncation, benign) — and it **excludes realized**. The Robinhood view's three visible rows back-compute cleanly from their G/L pairs (VLY cost $40.00 / value $1.00 · **USO 150/165 spread net debit $300.00 exactly** / value $85.00 · KRE 25P cost $53.00 / value $1.00), but the visible rows + buying power reach only $93.94 of the stated $102.85 — see D-20. Both transcriptions are internally consistent; the Fidelity one is arithmetically complete.*

*Deltas vs the 8/2 reconcile (marks were 7/31 close): **Fidelity account total −$2,935.35** ($39,514.28 → $36,578.93), **cash −$4,058.37** ($20,864.90 → $16,806.53), **positions MV −$631.92**, pending −$1,754.94 → $0. **Only two book changes are visible between the two captures: QQQ $687P ×3 is GONE (outcome unrecorded — D-12) and USO $135C Oct-16 ×2 is NEW (on no rail — D-19).** Every other Fidelity line is position-for-position identical in strike/expiry/qty/cost basis to 8/2 — no adds, no trims, no rolls across 9 sessions. **The cash move does NOT reconcile to those two facts: an −$882.10 residue remains unexplained even before crediting any QQQ 687P proceeds (D-16) — a positions view cannot close it; an activity-tab capture can.** What moved on marks: **GLD ripped +$31.21/sh** ($371.54 → $402.75, −0.5% → **+7.80%**, +$499 value — the single biggest mover in the book) · APD +$12.93 (+0.0% → +4.42%) · XLE 65C 0.76 → 0.97 · AAPL −$3.65 · USO −$3.54 (+6.0% → +3.07%) · **the whole thesis-put book decayed hard**: TLT 77P 0.35 → 0.20 (+202.7% → +72.96%, though **+100% on the day today**), APO 95P 2.67 → **0.05**, WAL legs 0.85 → 0.05/0.10, KRE Sep 0.25 → 0.02, HBAN 0.40 → 0.05, TLT 82P flipped back negative. **Caveat (labeled): five rows now mark at exactly $0.05** (KELYA, HBAN, OZK 42.5P, WAL 67.5P, APO 95P) — on illiquid deep-OTM strikes a positions view's last/bid can be an artifact rather than an executable price; do not read the residual value as realizable (D-21).*

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (7/18 re-base + amendment #1 = current). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All marks/values `[broker capture 8/14 ~09:45 ET — INTRADAY, not closes]`.*

| Ticker | Type | Qty | Cost | Mark 8/14 | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | 15 | $23.64 | $305.26 | $4,578.90 | **+1,191.0%** | qty 15 CONFIRMED by Will (8/2); sale date/price of the 5 sh still unrecorded — no activity view this pass either. See D-1 |
| GLD | Stock | 16 | $373.59 | $402.7499 | $6,443.99 | **+7.8%** | MIDAS domain. **Biggest mover in the book: +$31.21/sh since 7/31, −0.5% → +7.8% (+$499 value).** qty unchanged since the 7/31 add (D-13 resolved 8/2); the 10→13→16 off-rail add pattern is still routed PROME → MIDAS |
| USO | Stock | 35 | $121.88 | $125.63 | $4,397.05 | **+3.1%** | Will's Hormuz-gap entry (BRENT). qty 35 unchanged. Gave back half the 7/31 gain (+6.0% → +3.1%). BRENT/TERRY concentration arithmetic still owed from the 7/30 flag — now larger: USO stock $4,397 + USO 135C $1,210 + the Robinhood USO 150/165 spread = three USO-linked lines |
| APD | Stock | 2 | $294.79 | $307.82 | $615.64 | **+4.4%** | thesis tag STILL unassigned (`ACTIVE_DECISIONS` candidate row, open since 7/30) |
| TBT | Stock | 14 | $34.63 | $38.63 | $540.82 | **+11.6%** | 2× UST short — live duration-short leg (BOND/TERRY); the grind still pays |
| **USO** | **$135C Oct-16** | **2** | **$7.11** | $6.05 | $1,210.00 | −14.9% | ⚠️ **NEW since the 8/2 capture — on no PROME rail, no TERRY card, no owner agent.** Cost basis $1,421.33; bought sometime 8/3–8/14 (exact date/fill not in a positions view). Third USO-linked line in the book. See **D-19** |
| XLE | $65C Sep-30 | 2 | $2.28 | $0.97 | $194.00 | −57.4% | energy calls (BRENT); recovered further (−66.6% on 7/31 → −57.4%) |

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

| Position | Expiry | Qty | Cost | Outcome |
|----------|--------|-----|------|---------|
| ~~**VIX $20C/$25C call debit spread** (`VIXW`)~~ | Aug-05-2026 | ~~4~~ | $0.70 net debit | **✅ CLOSED 2026-07-30 ~09:50 ET — REALIZED −$111.60 (−38.8%).** `TRY-VIOLET-VIXCS` (VIOLET thesis / TERRY construction). Exited as one spread ticket at net $0.45 credit (StC 4× 20C @ $0.63 / BtC 4× 25C @ $0.18), on the mandatory date, un-killed, no roll. Exit legs broker-confirmed in the 8/2 activity tab (+$248.15 / −$72.05 = +$176.10 net), matching the recorded exit to the cent. Open items: TERRY card §10 grade + PB-0003 close; VIOLET settle re-grade |

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, **on no PROME rail and owned by no agent**. Recorded here so it is not invisible, not because the fleet manages it. The 8/2 activity tab exposed **seven short-dated QQQ put tickets since 7/20** (696P, 675P, 672P, 680P ×2 fills, 687P ×3) — **realized on the class ≈ −$2,267** through 7/31. **As of the 8/14 capture the class is EMPTY: no QQQ position of any kind is on the book.**

| Position | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|----------|--------|-----|------|------|-------|-----|------|
| ~~**QQQ $687P**~~ | Aug-03-2026 — **OUTCOME UNRECORDED** | ~~3~~ | $2.81 | — | — | **⚠️ UNRECORDED** | **GONE from the book — but HOW it went is unknown.** Basis $841.99; last seen $1,041.00 (+23.6%) at the 7/31 close. Will's stated 8/2 intent was to SELL Monday 8/3; **no fill, no expiry row and no proceeds figure exist on any surface.** Three labeled hypotheses, none confirmed: (a) sold Monday as intended, proceeds unknown; (b) expired worthless; (c) **auto-exercised ITM into short QQQ the IRA cannot hold** — the registered backstop, which would carry buy-in mechanics and its own cash effect. The unexplained −$882.10 cash residue (D-16) means this **cannot** be closed by inference. **Smallest action: one Fidelity activity-tab capture.** See **D-12** |
| ~~QQQ $680P~~ | Jul-31-2026 — CLOSED 7/31 | ? (2 fills) | — | — | — | **−$1,005.48 realized** | Bought 7/30 in two fills (−$599.33, −$414.66); SOLD closing 7/31 **+$8.51**. Inferred (labeled): the liquidation closed BOTH fills. Realized −$1,005.48 either way. See D-14 |
| ~~QQQ $672P~~ | Jul-31-2026 — EXPIRED WORTHLESS | ? | — | — | — | **−$416.66 realized** | Bought 7/30 −$416.66; EXPIRED row dated Aug-03, "Processing". 1-day put, total loss |
| ~~QQQ $675P~~ | Jul-30-2026 — SOLD 7/30 | 1 | $3.92 | — | — | **−$389.67 realized** | Strike record corrected back on 8/2 (D-14): the put sold 7/30 WAS the $675P. Broker record > verbal recall |

## Fidelity — Thesis Puts

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| **$77P** | **Sep-30** | **25** | **$0.12** *(broker basis, fees-in $0.11563)* | $0.20 | $500.00 | **+$210.92 / +72.96%** — **still the best position in the book, but well off the 8/2 peak** (+202.7% at the 7/31 close, mark 0.35 → 0.20). **Today it DOUBLED: +$250.00 / +100% on the session** [intraday 8/14], i.e. it was ~$0.10 yesterday. ⚠️ **Gate proximity, NOT adjudication** — the TRY-FIRE-004 card's ZONE-3 harvest line reads *"half at ≥3×"*: at $0.20 the position is **1.73× the fees-in basis**, i.e. **below** that line (it was genuinely met at the 7/31 5-lot trim fill, 3.23×). Registered disarm gate reads *"DGS10 <4.50"* — **no DGS10 reading is carried in this capture; ANVIL does not fetch or adjudicate it.** BE 76.89 (premium) / ~76.884 (all-in). TERRY/PB-0002 (re-grade still owed from 8/2) |
| $85P | Sep-30 | 2 | $2.52 | $3.40 | $680.00 | **+$176.65 / +35.09%** — gave back some (+43.0% on 7/31) |
| $82P | Oct-16 | 2 | $1.68 | $1.67 | $334.00 | **−$1.35 / −0.41%** — **flipped negative again** (was +11.5% on 7/31); effectively flat to cost |

*The duration-short complex (TBT 14 sh + all three TLT put legs) is **still the only part of the book working, but it has more than halved**: +$56.00 + $210.92 + $176.65 − $1.35 = **+$442.22** combined open G/L (was +$894.70 at the 7/31 close), on top of the **+$128.87 realized** on the 7/31 TLT 5-lot trim.*

### KRE — regional banks (REGINALD)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $60P | Dec-18 | 2 | $2.57 | $0.36 | $72.00 | −$441.34 / −85.98% |
| $60P | Dec-18 | 3 (M) | $2.93 | $0.36 | $108.00 | −$770.02 / −87.70% |
| $60P | Sep-30 | 2 | $2.27 | $0.02 | $4.00 | −$449.35 / −99.12% |
| $60P | Aug-21 | 3 | $2.70 | $0.02 | $6.00 | −$803.02 / −99.26% — **dead; 7 days to expiry.** Aug-21 OPEX cluster, "KRE lapse" per the standing read |

### WAL (REGINALD) — Sep-18s (the 7/21 print resolved NOT-FIRED)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $70P | Sep-18 | 1 | $7.69 | $0.10 | $10.00 | −$758.67 / −98.70% |
| $67.5P | Sep-18 | 1 | $7.51 | $0.05 | $5.00 | −$745.67 / −99.34% |

*(The Robinhood **WAL $77.5P Aug-21 ×1** carried here since 7/20 is **NOT on the 8/14 capture and now CONFIRMED SOLD** — ✅ **Will confirmed the sale in-session 2026-08-18** (relayed via TERRY, whose session Will was in; upgrade is from the OPERATOR'S OWN word, not from an inference). ⚠️ **The confirm covers the FACT of the sale ONLY — date and proceeds remain unrecorded, so the P&L is UNRECORDED, NOT ZERO, and D-18's residual STANDS.** Struck-through in the Robinhood table, retained — see **D-18**.)*

### OZK (REGINALD) — Aug-21s (the 7/21 print resolved NOT-FIRED)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $45P | Aug-21 | 4 | $3.69 | $0.12 | $48.00 | −$1,426.70 / −96.75% — **7 DTE.** Standing ruling (8/4): **RIDE to OPEX** |
| $42.5P | Aug-21 | 1 | $2.12 | $0.05 | $5.00 | −$206.67 / −97.64% — **7 DTE.** Same ruling: RIDE to OPEX |

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18 | 1 | $11.85 | $0.05 | $5.00 | −$1,179.67 / −99.58% | BROCK thesis vehicle. **Mark collapsed 2.67 → 0.05 in 9 sessions on a Dec-18 expiry** while same-dated KRE legs only went 0.70 → 0.36 — arithmetically consistent in the capture, but see the **$0.05-cluster caveat (D-21)** before treating $5.00 as realizable |
| HBAN | $16P | Oct-16 | 2 | $0.96 | $0.05 | $10.00 | −$181.34 / −94.78% | EXIT-THESIS dust (Will 7/18) — rides to expiry, zero effort. Round-tripped: −58.2% at the 7/31 close → −94.8% |
| KELYA | $7.5P | Aug-21 | 1 | $0.76 | $0.05 | $5.00 | −$70.67 / −93.40% | LABOR thesis. **7 DTE — ★ RULED LAPSE 2026-08-14 (Will, afternoon batch §3): ride to expiry, no action, no re-present.** LABOR's thesis-grade happens at OPEX per normal grading |

## Robinhood — satellite account (Individual)

> ✅ **CAPTURED 2026-08-14 (positions view, intraday) — first Robinhood capture since 7/20 (25 days).** Account value **$102.85** (+$4.74 / +4.83% today), buying power **$6.94**. ⚠️ **This view is NOT complete on its own terms:** the on-screen note reads *"Event contracts can't be traded on the web, but may impact buying power"* — event-contract exposure (Kalshi-style) is **invisible here** — and the three visible rows + buying power reach only **$93.94 of the $102.85** stated value, leaving **$15.85 unexplained (D-20)**. Rows carry **no per-contract mark** in this view (only G/L $ and %), so costs/values below are **back-computed from the G/L pair** and the block stays machine-class `unverified` by design. Two rows carried here since 7/20 do **not** appear in this capture and are **retained, not deleted** (absence from an incomplete positions view is not evidence of closure).

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **USO $150/$165 call spread** | Sep-18 | 1 | **$300.00 net debit** | $85.00 | ✅ **BROKER-CONFIRMED 8/14** | **★ THIS ANSWERS BRENT'S FILL-DEBIT ASK (queue row 20): net debit = $300.00 exactly** (back-computed from −$215.00 / −71.67%, tight to ±$0.02) — the 7/25 "~$300 net debit" verbal estimate is now broker-confirmed, and the card can be marked. Currently **−$215.00 / −71.67%**. FILLED 7/24; account confirmed Robinhood (Will, 8/2 — D-6). BRENT tail-rider card. BE USO ~$153 · max profit ~$1,200 (~4:1) · defined-risk. Rule-#6-clean red-day entry; mgmt = BRENT card frozen terms. Residue: exact fill date/time + per-leg prices still not in a positions view |
| **VLY $14P** | **8/21** | 1 | $40.00 | $1.00 | ✅ **VERIFIED 8/14 · ★ RULED LAPSE same day** | −$39.00 / −97.50%. **7 DTE — ★ RULED LAPSE 2026-08-14 (Will, afternoon batch §3): ride to expiry, no action, no re-present.** Never carried in FORGE before this pass; on no rail, no owner agent. See D-22 |
| **KRE $25P** | 1/15/2027 | 1 | $53.00 | $1.00 | ✅ **VERIFIED 8/14** | −$52.00 / −98.11%. Deep-OTM lottery, carried here since 7/20 at −$38 / −71.7%; **basis now broker-confirmed** ($53.00, consistent with the 7/20-vintage figures). Not new to the mirror |
| ~~**WAL $77.5P**~~ | **Aug-21** | ~~1~~ | — | — | ✅ **CONFIRMED SOLD (Will in-session 2026-08-18)** | Carried at 7/20 vintage; absent from the 8/14 capture. **Was PRESUMED off Will's hedged 8/14 recall ("must have been sold too i think") + capture absence; Will CONFIRMED the sale in-session 8/18** — the hedge is discharged and the row is no longer inference-grade on the FACT. ⚠️ **Date and proceeds are STILL unrecorded ⇒ P&L UNRECORDED, not zero.** Sale window remains 7/20–8/14. Retained struck-through, not deleted. See **D-18** |
| T | stock | 1 | — | — | ⚠️ **NOT ON THE 8/14 CAPTURE — unresolved** | 1 share, +$1.18 / +5.7% at the 7/20 mark (implied value ~$21.9 then). **Absent from this capture, and a single T share is larger than the entire $15.85 residue** — so if it were merely hidden, the account value would not decompose as it does. RETAINED, not deleted. See D-20 |
| ~~USO $128C~~ | 7/22 — **EXPIRED** | 1 | — | — | **EXPIRED — presumed worthless** | Hormuz leg. **Absent from the 8/14 Robinhood capture, consistent with expiry** three weeks ago. Recorded as EXPIRED, outcome $0 presumed (~−$100 class). ⚠️ **A positions view cannot show close/exercise detail** — "presumed worthless" remains a labeled hypothesis, now supported by absence rather than resolved by it. Closes **D-5** to the extent a positions view can |
| ~~QQQ $696P~~ | 7/20 EXPIRED | 1 | — | — | **CLOSED ~−$455** | RESOLVED (Will-reported 7/20 PM): recovered only ~$8 of premium; QQQ closed knife-edge ATM $696. Day-trade class, off-thesis |

---

## ⚠️ Reconcile discrepancies (8/14)

> Built by ANVIL against the 8/14 screenshot pair. **Nothing here has been resolved by invention** — every conjecture is labeled as a hypothesis, and broker records outrank verbal recall. Ranked by **decision urgency, expiring items first**. The structural fact governing this whole pass: **both captures are POSITIONS views, not activity views — so every "what happened to X" question is unanswerable from this data by construction.** One Fidelity activity-tab capture would close D-12, D-16 and D-1 together.

### ASK WILL (cannot be resolved from any repo surface)

| # | Item | Urgency | What is known | What is conjectured (labeled) | Decision owner |
|---|------|---------|---------------|-------------------------------|----------------|
| **D-18** | **WAL $77.5P Aug-21 ×1 — carried in FORGE, NOT on today's Robinhood capture** | **🟠 downgraded from 🔴 (recall banked)** | Carried at 7/20 vintage. Today's WAL legs are the two Fidelity Sep-18s (67.5P + 70P) only. Not in either 8/14 capture. **★ Will 8/14 in-session, hedged verbal ("the WAL must have been sold too i think")** — recorded as RECALL/inference, direction-only, no date, no figure | **Working hypothesis: SOLD between 7/20 and 8/14** (Will's 8/14 recall + absence from the capture, mutually consistent; any proceeds sit inside the Robinhood balance). Residual branches: hidden-by-incomplete-view (weak — the $15.85 residue doesn't fit) · originally mis-transcribed. **Broker record > verbal recall — a Robinhood history view supplies the date/figure if ever needed; the 7-DTE urgency is DEFUSED by the working hypothesis** | Recall banked; Robinhood history view = optional closer |
| **D-12** | **★ QQQ $687P ×3 — gone from the book, outcome UNRECORDED** | **🔴 high** | Basis $841.99; $1,041.00 (+23.6%) at the 7/31 close; Will's 8/2 stated intent was to SELL Mon 8/3. Absent 8/14. No fill, no proceeds, no expiry row on any surface. **★ Will 8/14 in-session, hedged verbal ("the QQQ's were sold at a loss I believe")** — makes branch (a) the WORKING HYPOTHESIS and retires the auto-exercise worry as the modal branch; recorded as RECALL, direction-only, no figure | (a) **sold, at a loss — working hypothesis per Will's 8/14 recall** (⚠️ recall tension, labeled: the leg was +23.6% at the 7/31 close, so "at a loss" requires Monday 8/3 to have moved against it before the sale — possible — OR the recall blends the wider QQQ put class, which realized −$2,267 through 7/31) · (b) expired worthless · (c) auto-exercised — now residual branches. **Figure still unknown; broker record > verbal recall — the activity capture remains the closer, and D-16's gap GROWS by whatever proceeds landed** | **Will's recall banked**; activity capture for the figure |
| **D-16** | **★ Fidelity cash −$882.10 does not reconcile** | **🔴 high** | Bridge, stated in full: mm $20,864.90 [8/2] − $1,754.94 (the 8/2 pending, now cleared) − $1,421.33 (USO 135C basis) = **$17,688.63 expected**; actual mm 8/14 = **$16,806.53** → **−$882.10 unexplained, BEFORE crediting any QQQ 687P proceeds.** If the 687P sold near its 7/31 value the gap widens to ≈ **−$1,923.10**. The unresolved +$67.71 residue from D-15 is folded inside this and can no longer be separated | Unexplained outflow could be: a withdrawal/transfer · additional untranscribed trades in the 8/3–8/14 window (9 sessions, invisible to a positions view) · QQQ 687P assignment/buy-in mechanics (see D-12c) · fees/dividends. **All labeled; ANVIL resolves none of them** | **Will** → **one Fidelity activity-tab capture closes this, D-12 and D-1 at once** |
| **D-17** | **STNG — appears nowhere in either capture, and nowhere in FORGE** | 🟠 medium | Queue row 20 carried "STNG appears nowhere in FORGE (qty/cost from Will's 7/21 note, never broker-verified)." ANVIL confirms by grep: **zero STNG rows in `FORGE/STATUS.md` or `FORGE/PORTFOLIO.md`.** It is also on neither 8/14 capture. **Historical repo record (evidence, not a resolution):** `memory/2026-03-12.md` logs *"STNG ×2 @ $70.01 ($140.02) — RED team wrong submarket"* and *"DON'T ADD → sold next day"*; root `LESSONS.md` #9 cites STNG by name as the canonical closed-loop failure — *"the system recommended selling STNG, Will sold it, but a week later the same system re-flagged the position because nobody closed the loop"* | **Three dispositions, all labeled, none adopted:** (a) never existed as transcribed — the 7/21 note recalled the **March-2026** position that was already sold (this is the branch the March record and LESSONS.md #9 make *plausible*, and it would be the same failure mode recurring) · (b) closed before 8/2 · (c) lives in a **third account** neither capture covers. **ANVIL does not pick one** | **Will** — one line settles it |
| **D-20** | **Robinhood view does not decompose: $15.85 unexplained + event contracts invisible + T share absent** | 🟠 medium | Visible rows $87.00 + buying power $6.94 = **$93.94** vs stated account value **$102.85** → **$15.85 residue**. On-screen: *"Event contracts can't be traded on the web, but may impact buying power."* The 1 T share carried since 7/20 (~$21.9 implied then) is **not** in this view — and is **larger** than the residue | Residue could be: cash in excess of buying power · **event-contract positions** (invisible by construction) · a partially-shown row. The T share cannot be hiding inside a $15.85 residue at its 7/20 value — **hypothesis: T was sold**, unconfirmed. **Untranscribed event-contract exposure of unknown size is the live risk here** | **Will** — does the account hold event contracts, and is T still held? |
| **D-1** | **AAPL 5-sh sale — date + price still unrecorded** | 🟡 carried | qty 15 Will-confirmed (8/2); the sale itself has never been captured. No activity view this pass | Predates the 8/2 activity window (≥Jul-29); ~$565 cash class | **Will** — states date + price (or the activity capture reaches it) |
| **D-10** | **Account naming: "MAIN book" vs Traditional IRA •1326** | 🟡 carried | TERRY cards / FORGE say "MAIN book"; fill records and all three exports say Traditional IRA •1326. The IRA short-stock constraint is load-bearing again via D-12c | — | **Will** confirms the identity; then one fleet-wide label sweep |

### MIRROR-WRONG (the mirror said something the capture contradicts)

| # | Item | Mirror said (8/2) | Capture says (8/14) | Action taken |
|---|------|-------------------|---------------------|--------------|
| **D-23** | Robinhood block scope banner | "NOT CAPTURED IN THE 7/30 OR 8/2 EXPORTS… 7/20-vintage, 13 days unverified" | **Captured 8/14.** USO spread, VLY 14P and KRE 25P are broker-verified; WAL 77.5P and T are not in the view | ✅ **Fixed in-place**: banner rewritten, three rows verified with figures, two rows retained-and-flagged (D-18, D-20) |
| **D-24** | KRE $25P Jan-15-2027 was listed by the task packet as "new to mirror" | It was **already** in the mirror (7/20 row, −$38 / −71.7%) | Same position, basis now confirmed $53.00 | ✅ **Not new** — verified in place. Flagged so the packet's new-name list isn't propagated as-is |
| **D-25** | Task packet's "new-to-mirror" list omitted a name | Packet listed APD / KELYA / TLT 85P / TLT 82P / VLY / KRE 25P as candidates — **but APD, KELYA, TLT 85P and TLT 82P were all already in the mirror at identical qty/basis**, and the list **did not include USO $135C Oct-16 ×2**, which is genuinely new | Only **two** names are actually new to this mirror: **USO $135C Oct-16 ×2** (Fidelity, D-19) and **VLY $14P 8/21 ×1** (Robinhood, D-22) | ✅ Both added; report corrects the list |

### BOOK-CHANGED (position set moved between captures)

| # | Item | Detail | Disposition |
|---|------|--------|-------------|
| **D-19** | **USO $135C Oct-16 ×2 — NEW, on no rail** | Cost basis $1,421.33 ($7.11/contract), mark $6.05, value $1,210.00, −14.87%. Bought somewhere in the 8/3–8/14 window; **exact fill date/price not obtainable from a positions view.** No TERRY card, no PROME rail, no owner agent | **Recorded, unowned.** Note: this makes **three USO-linked lines** (35 sh stock + this + the Robinhood 150/165 spread) — **BRENT/TERRY's concentration arithmetic, owed since 7/30, is now materially bigger.** ANVIL states the fact; sizing is not ANVIL's call |
| **D-22** | **VLY $14P 8/21 ×1 — NEW to the mirror (Robinhood)** | Cost $40.00, value $1.00, −$39.00 / −97.50%. **7 DTE** — joins the Aug-21 OPEX cluster | Added to the Robinhood block. On no rail; no owner agent recorded. Will/REGINALD may want it in the cluster ruling |
| **D-26** | **Aug-21 OPEX cluster — 7 days out, verified against the mirror** | **Fidelity:** OZK 45P ×4 ($48) · OZK 42.5P ×1 ($5) · KRE 60P ×3 ($6) · KELYA 7.5P ×1 ($5) = **$64 residual**. **Robinhood:** VLY 14P ×1 (~$1). Cluster total ≈ **$65**. Mirror's standing notes now match the capture: **OZK = RIDE to OPEX (ruled 8/4)** · **KRE = lapse** | ✅ Cluster rows and notes reconciled. **★ RULING GAP CLOSED 2026-08-14 (Will, afternoon batch §3): KELYA 7.5P + VLY 14P both RULED LAPSE** — every Aug-21 member now carries a ruling: OZK ×5 RIDE (8/4) · KRE ×3 + KELYA + VLY lapse. Ruling of record `PROME/proposals/2026-08-14_afternoon-batch-RULED.md` |
| **D-5** | **Robinhood USO $128C — expired 7/22** | Absent from the 8/14 Robinhood capture, consistent with expiry three weeks ago | **Recorded as EXPIRED, outcome $0 presumed (~−$100 class).** ⚠️ Exact close/exercise detail is **unavailable from a positions view** — "worthless" stays a labeled presumption. Closed as far as this instrument can close it |
| **D-6** | **USO 150/165 Sep-18 spread — net debit** | **★ RESOLVED: $300.00 exactly**, back-computed from −$215.00 / −71.67% (tight to ±$0.02). Confirms the 7/25 "~$300" verbal estimate | ✅ **BRENT's queue-row-20 fill-debit ask is answered.** Residue: exact fill date/time and per-leg prices still need an activity view. Card can now be marked ($85.00 current value) |

### CAVEATS (data-integrity notes — not asks)

| # | Item | Detail |
|---|------|--------|
| **D-21** | **The $0.05 mark cluster (n=5)** | KELYA 7.5P, HBAN 16P, OZK 42.5P, WAL 67.5P and APO 95P **all mark at exactly $0.05**. On illiquid deep-OTM strikes a positions view's price can be a stale last-trade or a bid floor rather than an executable quote — **the ~$30 of combined residual value they represent should not be read as realizable.** Sharpest instance: **APO 95P fell 2.67 → 0.05 (−98%) in 9 sessions on a Dec-18 expiry** while same-dated KRE legs went only 0.70 → 0.36. The capture is internally consistent (value = mark × qty × 100 exactly), so this is a **quote-quality** caveat, not a transcription error. Labeled hypothesis; an activity/quote view would settle it |
| **D-27** | **Intraday marks, market open** | Every figure in this file is a **~09:45 ET intraday mark on Fri 2026-08-14** — not a close, not a settle. Same-day P&L (Fidelity +$243.75 / +0.67%; the TLT 77P alone +$250 / +100%) will move before the bell. Nothing here may be cited as a settle |
| **D-15** | **The +$67.71 residue from 8/2** | Hypothesised as a money-market month-end dividend. **No activity view this pass**, so it is unconfirmed and is now **absorbed inside the −$882.10 D-16 gap** — it can no longer be tested separately |
| **D-14** | **QQQ 680P second-fill closure (inferred)** | Unchanged from 8/2: realized −$1,005.48 either way; the inference stands, confirmable only by an activity capture |

---

## Immediate Actions (8/14 session state)

| Item | State | Owner |
|---|---|---|
| **★ One Fidelity activity-tab capture** — closes D-12 (QQQ 687P outcome), D-16 (−$882.10 cash gap) and D-1 (AAPL sale) together | 🔴 Three open items, one capture; the cash gap is the largest unexplained figure in the book | **Will** |
| ~~**WAL $77.5P Aug-21 — closed or missing?**~~ **(D-18) — EXISTENCE QUESTION CLOSED 8/18, P&L RESIDUAL OPEN** | ✅ Sale CONFIRMED by Will in-session 2026-08-18. ⚠️ **Residual is now narrower and different in kind: date + proceeds unrecorded ⇒ the P&L is UNRECORDED, not zero — do not book this leg at $0.** Closes on a Robinhood history view, not on another recall | **Will** (history view, not urgent — nothing trades off it) |
| **STNG disposition** (D-17) | 🟠 Absent from FORGE and from both captures; March-2026 record + LESSONS.md #9 make "already sold, re-flagged" a *plausible labeled* branch — unadopted | **Will** (one line) |
| **Robinhood event contracts + T share + $15.85 residue** (D-20) | 🟠 Untranscribed exposure of unknown size, invisible in the web view | **Will** |
| **Aug-21 OPEX cluster — 7 days** (D-26) | 🟡 ~$65 residual. OZK = RIDE to OPEX (ruled 8/4) · KRE = lapse · **KELYA 7.5P has no standing ruling (and needs none, −55% OTM)** · ~~VLY 14P no standing ruling~~ **← STALE HALF corrected 8/20 (TERRY tie-break flag, PROME-adjudicated): VLY 14P = RULED LAPSE 8/14 + re-affirmed "let it die" 8/20 — this file's own line 106 carried the ruling all along; ⚠️ EbE branch re-based 8/20: needs only a −0.92% VLY close (closed 14.12, −2.22% same day), base rate ~21%, NOT the "~2%" the ruling rode on — write-backs pre-registered both directions (TERRY `534545856`)** | REGINALD / LABOR / Will |
| **USO concentration arithmetic** (D-19) | 🟠 Now **three** USO-linked lines (35 sh + 135C ×2 + the RH 150/165 spread); owed since 7/30, and the new call leg is on no rail and has no owner | BRENT / TERRY (PROME routing) |
| **BRENT queue row 20 — USO spread fill debit** | 🟢 **ANSWERED: $300.00 net debit, broker-confirmed.** Card can be marked; per-leg fill detail still owed | PROME → BRENT |
| **TLT PB-0002 re-grade** (trim = ⅙ at 3.23× on 7/31; card says half at ≥3×) | ✅ **DISCHARGED — annotation added 2026-08-19 by PROME (FORGE owner since 7/30).** This cell read "🟡 Carried from 8/2, still owed" and was **stale from ~8/7-8/8**: TERRY re-graded and SPLIT the row (`AGENTS/TERRY/STATUS.md`) — **`PB-0002a` CLOSED** (5 ct @ $0.3734 = 3.23× fees-in, **+$128.86 / +222.9%**), **`PB-0002b` OPEN** (25 ct), **10 contracts still OWED at ≥$0.33** (the 7/31 partial did NOT consume the harvest gate; it was a HARVEST, not a rule-#7 trim). ⚠️ **Left as an annotation, not a rewrite — this file is a dated 8/14 09:45 ET snapshot and rewriting a snapshot destroys the evidence of the drift.** Class: mirror-behind-STATUS; STATUS is canonical. **Cost of this one: PROME cited it to Will on 8/19 as an overdue TERRY item, which it was not.** ~~Carried from 8/2, still owed.~~ Position is now **1.73×** — below the harvest line, and the DGS10 disarm gate is **unread in this capture** | TERRY (PROME packet) |
| **GLD off-rail add pattern → MIDAS** | 🟢 qty unchanged this pass; **+7.8% and the book's biggest mover.** Routing only | PROME → MIDAS |
| **APD thesis tag** | 🟡 Still unassigned since 7/30; position is +4.4% | PROME / Will |
| **$0.05 mark-cluster quote quality** (D-21) | 🟢 Caveat recorded; do not treat ~$30 of dust as realizable | ANVIL next pass |

---

*History → `_archive/JOURNAL.md` | Prior reconciles (8/2, 7/30, 7/20, 7/16, 5/21) preserved in git history | Full-portfolio Feb snapshot → `PORTFOLIO.md` (**FROZEN/superseded, historical only — never cite as live**) | Position truth = Will/broker direct (off-repo)*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumer: `AGENTS/TERRY/scripts/positions_from_forge.py` (desk-dashboard Positions tab; keys on table headers, section names, and cell text — markdown emphasis and struck-through rows are visible to it). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069 n=3 — the 7/30 reconcile broke the parser silently). New consumers: add yourself to this list in the same commit that starts parsing. *(8/14 pass: no section/header renames; the Robinhood table gained `Cost` and `Value` columns and deliberately still has **no `Mark` column**, so that block keeps parsing as class `unverified` — the capture gave G/L pairs, not per-contract marks. Parser re-run post-edit: clean, no defects.)*
