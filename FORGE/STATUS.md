# FORGE — Trading Operations

> **Structured position-truth mirror — reconciled 2026-08-02 (broker export screenshot, Sunday 8/2 evening; marks = Friday 2026-07-31 close) from Will's Fidelity Traditional IRA •1326 position export + the Fidelity activity tab (Past-30-days view, PROME-transcribed 8/2 — visible window reaches Jul-29, may be cropped below; both screenshots stay off-repo per the public-prep rule). Position truth is off-repo (Will/broker direct); this file is the fleet's parseable mirror and goes stale from the moment it's written — do NOT cite marks/P&L below as current without a fresh broker reconcile.** Refresher flow = Will-on-broker-export → PROME transcribes → ANVIL reconciles (this pass, two rounds same evening; prior reconciles 2026-07-30, 2026-07-20, 2026-07-16, 2026-05-21). Old execution ledger + per-trade folders → `FORGE/_archive/`.
>
> ⚠️ **THIS EXPORT COVERS ONE ACCOUNT ONLY — Fidelity Traditional IRA •1326 (presumed; D-10 naming confirm still open).** The Robinhood satellite was **not** captured this pass either (second consecutive export). The USO 150/165 Sep-18 spread is now **Will-confirmed Robinhood (8/2)** — see **§ Reconcile discrepancies (8/2)** before treating any absence below as a closed position.

**Updated:** 2026-08-02 [broker export screenshot + activity tab; **marks = Fri 2026-07-31 close**] | **Fidelity cash (money market):** $20,864.90 (52.80%) | **Fidelity positions market value:** $20,404.32 | **Pending activity:** **−$1,754.94** *(RESOLVED-itemized: the four Jul-31 trades exactly — D-15)* | **Fidelity account total:** $39,514.28 *(7/31 day chg: +$138.30 / +0.35%)* | **Robinhood:** small satellite — **NOT captured this export; rows below are 7/20-vintage and unverified today**

*Export arithmetic verified by ANVIL: positions $20,404.32 + cash $20,864.90 + pending −$1,754.94 = $39,514.28 account total, exact to the cent; every per-row G/L$ = value − basis exactly; account "total G/L" −$1,004.38 = the exact sum of open-position G/L (−4.69% on $21,408.70 open basis — it excludes realized losses). **Activity tab verified: all 11 transcribed rows' running balances chain to the cent; pending −$1,754.94 = GLD −$1,108.14 + QQQ 687P −$841.99 + TLT 5-lot +$186.68 + QQQ 680P liq +$8.51 EXACT; the settled-cash equation closes to a single stated residue of +$67.71** (see D-15). A few G/L% cells sit ±0.01% from recomputation — broker display truncation, benign. Both transcriptions are internally consistent.*

*Deltas vs the 7/30 reconcile (~09:40 ET export): **account total −$1,062.74** ($40,577.02 → $39,514.28), **cash +$315.15** ($20,549.75 → $20,864.90), pending swung **+$1,500.00 → −$1,754.94** (the 7/30 +$1,500 is now evidenced as a deposit/transfer that landed ~Jul-29 — ledger balance $22,049.75 = $20,549.75 + $1,500.00 exact). Position changes in the window, all now broker-documented: **TLT Sep-30 $77P 30 → 25 — Will-confirmed intentional partial profit-take, +$186.68 net = 3.23× fees-in basis (D-11 RESOLVED)** · **GLD 13 → 16 sh — broker-confirmed buy −$1,108.14 (D-13 RESOLVED)** · **QQQ $687P Aug-03 ×3 NEW — expires MONDAY 8/3; Will (8/2) plans to SELL Monday (D-12)** · **QQQ short-dated put history RECONSTRUCTED from the activity tab — the put sold 7/30 was the $675P after all, plus three previously invisible Jul-31-expiry puts bought 7/30 (672P, 680P ×2 fills); realized −$1,811.81 on QQQ puts in two sessions (D-14)** · both VIXW legs gone, exit legs broker-confirmed +$248.15/−$72.05 = +$176.10 net, matching the recorded exit to the cent. Prior-pass confirmations from Will: **AAPL 15 sh** (sale details still open, D-1) · **USO 35 sh** (7/29 tranche visible: −$643.40 ≈ 5 sh @ ~$128.68). The rest of the thesis put book is position-for-position unchanged in strike/expiry/qty/basis (KRE ×4 lots, WAL ×2, OZK ×2, APO, HBAN, KELYA, TLT 85P/82P) — no adds, no trims, no rolls.*

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (7/18 re-base + amendment #1 = current). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All marks/values `[broker export 8/2, marks = Fri 2026-07-31 close]`.*

| Ticker | Type | Qty | Cost | Mark 7/31 | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | 15 | $23.64 | $308.91 | $4,633.65 | **+1,206.5%** | qty 15 **CONFIRMED by Will**; sale date/price of the 5 sh still unrecorded — the activity window (≥Jul-29) doesn't reach it. See D-1 |
| GLD | Stock | **16** | $373.59 | $371.54 | $5,944.64 | −0.5% | MIDAS domain. qty 13 → 16 (+3 sh) **broker-confirmed: activity row 7/31 BOUGHT −$1,108.14** (~$369.4/sh) — **D-13 RESOLVED.** Second consecutive off-rail add (10→13→16, ~$2.2k cumulative); MIDAS routing = PROME |
| USO | Stock | 35 | $121.88 | $129.17 | $4,520.95 | **+6.0%** | Will's Hormuz-gap entry (BRENT). qty 35 **CONFIRMED by Will**; latest tranche visible in activity: 7/29 BOUGHT −$643.40 (≈5 sh @ ~$128.68), earlier tranches predate the window. BRENT/TERRY concentration arithmetic still owed from the 7/30 flag |
| APD | Stock | 2 | $294.79 | $294.89 | $589.78 | +0.0% | thesis tag still unassigned (`ACTIVE_DECISIONS` candidate row); round-tripped from +5.0% on 7/30 |
| TBT | Stock | 14 | $34.63 | $38.45 | $538.30 | **+11.0%** | 2× UST short — live duration-short leg (BOND/TERRY); the grind is paying |
| XLE | $65C Sep-30 | 2 | $2.28 | $0.76 | $152.00 | −66.6% | energy calls (BRENT); recovered from −76.7% on 7/30 |

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

| Position | Expiry | Qty | Cost | Outcome |
|----------|--------|-----|------|---------|
| ~~**VIX $20C/$25C call debit spread** (`VIXW`)~~ | Aug-05-2026 | ~~4~~ | $0.70 net debit | **✅ CLOSED 2026-07-30 ~09:50 ET — REALIZED −$111.60 (−38.8%).** `TRY-VIOLET-VIXCS` (VIOLET thesis / TERRY construction). Exited as one spread ticket at net $0.45 credit (StC 4× 20C @ $0.63 / BtC 4× 25C @ $0.18), on the mandatory date, un-killed, no roll — full exit record in the 7/30 reconcile (git history). **Exit legs broker-confirmed in the activity tab (8/2): +$248.15 / −$72.05 = +$176.10 net proceeds, matching the recorded exit to the cent.** Open items: TERRY card §10 grade + PB-0003 close; VIOLET settle re-grade |

## Fidelity — Off-thesis / day-trade class

> Will-direct, short-dated, **on no PROME rail and owned by no agent**. Recorded here so it is not invisible, not because the fleet manages it. **The activity tab exposed a larger pattern than any surface knew: seven short-dated QQQ put tickets since 7/20** (696P, 675P, then 672P + 680P ×2 fills bought 7/30, now 687P ×3) — **realized on the class ≈ −$2,267** (696P ≈−$455 + the 7/30–7/31 puts −$1,811.81), with the 687P ×3 still open.

| Position | Expiry | Qty | Cost | Mark 7/31 | Value | P&L | Note |
|----------|--------|-----|------|-----------|-------|-----|------|
| **QQQ $687P** | **Aug-03-2026 — ★ EXPIRES MONDAY** | 3 | $2.81 | $3.47 | $1,041.00 | **+23.6%** | ⚠️ NEW since 7/30; basis $841.99 [activity: BOUGHT 7/31 −$841.99]. **Will (8/2): PLANS TO SELL Monday 8/3 — intent recorded, execution + fill owed.** Backstop stands: if ITM at Monday's close it auto-exercises into short QQQ **the IRA cannot hold**. See D-12 |
| ~~QQQ $680P~~ | Jul-31-2026 — CLOSED 7/31 | ? (2 fills) | — | — | — | **−$1,005.48 realized** | Bought 7/30 in two fills (−$599.33, −$414.66; per-fill qty not expanded in the activity view); SOLD closing (OPTION LIQUIDATION) 7/31 **+$8.51**. **Inferred (labeled): the liquidation closed BOTH fills** — no 680P EXPIRED row appears while the 672P has one; caveat: expiry rows post late ("Processing"), so a second-fill expiry row could be not-yet-visible. **Realized −$1,005.48 either way.** This — not the Jul-30 put — is the "680" of Will's 7/30 correction; see D-14 |
| ~~QQQ $672P~~ | Jul-31-2026 — EXPIRED WORTHLESS | ? | — | — | — | **−$416.66 realized** | Bought 7/30 −$416.66; EXPIRED row dated Aug-03 (as of 7/31), "Processing". 1-day put, total loss |
| ~~QQQ $675P~~ | Jul-30-2026 — SOLD 7/30 | 1 | $3.92 | — | — | **−$389.67 realized** | ★ **STRIKE RECORD CORRECTED BACK (D-14): the put sold 7/30 WAS the $675P** — activity row: SOLD closing (OPTION LIQUIDATION) +$1.99 vs $391.66 basis. The 7/30 in-session "strike is 680, 675 was a transcription error" correction is itself REVERSED: the original transcription was right, and Will's "680" matched the NEW Jul-31 680Ps bought the same day, which no surface knew existed. Broker record > verbal recall |

## Fidelity — Thesis Puts

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| **$77P** | **Sep-30** | **25** | **$0.12** *(broker basis, fees-in)* | $0.35 | $875.00 | **★ +$585.92 / +202.7%** — best position in the book. **7/31 trim RESOLVED (D-11): Will confirms intentional partial profit-take ("sold 5 just to try to take some profits"). Activity actuals: SOLD 5-lot 7/31 for +$186.68 net = $0.3734/sh = 3.23× the $0.11563 fees-in basis — the card's ZONE-3 "half at ≥3×" line was genuinely met at the fill; realized ≈ +$128.87 on the 5 lots. Trim was ⅙, not the card's half — TERRY re-grades PB-0002 Monday (PROME packet).** Original 30× fill record stands. BE 76.89 (premium) / ~76.884 (all-in). TERRY/PB-0002 |
| $85P | Sep-30 | 2 | $2.52 | $3.60 | $720.00 | **+$216.65 / +43.0%** — extended (was +19.2% on 7/30) |
| $82P | Oct-16 | 2 | $1.68 | $1.87 | $374.00 | **+$38.65 / +11.5%** — **flipped positive** (was −9.3% on 7/30) |

*The duration-short complex (TBT 14 sh + all three TLT put legs) is **the only part of the book working — and it accelerated**: +$53.48 + $585.92 + $216.65 + $38.65 = **+$894.70** combined open G/L (was +$515.10 on 7/30), after banking **+$128.87 realized** on the TLT 5-lot trim.*

### KRE — regional banks (REGINALD)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $60P | Dec-18 | 2 | $2.57 | $0.70 | $140.00 | −$373.34 / −72.7% |
| $60P | Dec-18 | 3 (M) | $2.93 | $0.70 | $210.00 | −$668.02 / −76.1% |
| $60P | Sep-30 | 2 | $2.27 | $0.25 | $50.00 | −$403.35 / −89.0% |
| $60P | Aug-21 | 3 | $2.70 | $0.06 | $18.00 | −$791.02 / −97.8% — **effectively dead; 19 days to expiry** |

### WAL (REGINALD) — Sep-18s (the 7/21 print resolved NOT-FIRED)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $70P | Sep-18 | 1 | $7.69 | $0.85 | $85.00 | −$683.67 / −89.0% |
| $67.5P | Sep-18 | 1 | $7.51 | $0.85 | $85.00 | −$665.67 / −88.7% |

*(Robinhood WAL $77.5P Aug-21 ×1 — **not in this export's account, unverified today**; see Robinhood section.)*

### OZK (REGINALD) — Aug-21s (the 7/21 print resolved NOT-FIRED)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $45P | Aug-21 | 4 | $3.69 | $0.15 | $60.00 | −$1,414.70 / −95.9% |
| $42.5P | Aug-21 | 1 | $2.12 | $0.15 | $15.00 | −$196.67 / −92.9% — mark tripled off the low ($0.05 → $0.15) |

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18 | 1 | $11.85 | $2.67 | $267.00 | −$917.67 / −77.5% | BROCK thesis vehicle |
| HBAN | $16P | Oct-16 | 2 | $0.96 | $0.40 | $80.00 | −$111.34 / −58.2% | EXIT-THESIS dust (Will 7/18) — rides to expiry, zero effort; recovered from −73.9% |
| KELYA | $7.5P | Aug-21 | 1 | $0.76 | $0.05 | $5.00 | −$70.67 / −93.4% | LABOR thesis |

## Robinhood — satellite account (options + 1 T share)

> ⚠️ **NOT CAPTURED IN THE 7/30 OR 8/2 EXPORTS.** These rows are **7/20-vintage — 13 days unverified** — retained, not deleted, because absence from a single-account export is not evidence of closure. Every row here needs a Robinhood export to resolve.

| Position | Expiry | Qty | State | Note |
|----------|--------|-----|-------|------|
| ~~QQQ $696P~~ | 7/20 EXPIRED | 1 | **CLOSED ~−$455** | RESOLVED (Will-reported 7/20 PM): recovered only ~$8 of premium; QQQ closed knife-edge ATM $696. Day-trade class, off-thesis |
| ~~USO $128C~~ | **7/22 — EXPIRED 11 DAYS AGO** | 1 | ⚠️ **OUTCOME UNRECORDED** | Hormuz leg. **USO closed 7/22 well below the $128 strike on the available record → presumed expired worthless (~−$100 class), but this is a HYPOTHESIS, not a confirmation.** See D-5 |
| **USO $150/$165 call spread** | Sep-18 | ~1 | **✅ ACCOUNT CONFIRMED: Robinhood (Will, 8/2)** | FILLED 7/24, net debit ~$300 [Will verbal 7/25; TERRY mid was $2.98]. BRENT tail-rider card. **D-6 RESOLVED — account is Robinhood per Will; residue: exact fill price/qty still owed at next Robinhood capture (card mark still unpriced).** BE USO ~$153 · max profit ~$1,200 (~4:1) · defined-risk. Rule-#6-clean red-day entry; mgmt = BRENT card frozen terms |
| **WAL $77.5P** | Aug-21 | 1 | unverified today | Nearest-money WAL leg (~5.8% OTM at $82.30 on 7/20). **19 days to expiry, 13 days unverified** |
| KRE $25P | 1/15/2027 | 1 | unverified today | deep-OTM lottery; −$38 / −71.7% at the 7/20 mark |
| T | stock | 1 | unverified today | +$1.18 / +5.7% at the 7/20 mark |

---

## ⚠️ Reconcile discrepancies (8/2) — pass 2 (evening: Will's answers + activity tab folded in)

> Built by ANVIL against the 8/2 export (7/31-close marks), then updated the same evening with Will's direct answers and the Fidelity activity tab (Past-30-days view, 11 rows, balance-chain verified). **Nothing here has been resolved by invention** — hypotheses are labeled; broker records outrank verbal recall. Ranked: open items first by decision urgency, then this pass's resolutions kept for the record. **Closed earlier on 8/2 pass 1:** D-2/D-3 (GLD/USO qty), D-4 (residue → D-14), D-7 (→ D-15 + D-1), D-8 (VIXW), D-9 (benign).

| # | Item | What the record says | What the broker record says | Disposition / smallest action that closes it |
|---|------|----------------------|----------------------|-------------|
| **D-12** | **★ QQQ $687P ×3 — expires MONDAY 8/3** | On no rail; first surfaced this reconcile | 3 contracts, basis $841.99 (bought 7/31), value $1,041.00 (+23.6%) at Friday's close, [NE] flag | **INTENT RECORDED (Will, 8/2): SELL Monday.** Open until executed. Backstop stands: ITM at Monday's close → auto-exercise into short QQQ **the IRA cannot hold**. **Smallest action: Will executes Monday; fill lands at next capture** |
| **D-14** | **QQQ short-dated put history — reconstructed; one inferred leg remains** | 7/30 record: ONE put, "sold for a loss — strike 680, not 675" | **Five positions, not one.** 7/30: SOLD the **$675P** +$1.99 (vs $391.66 basis = **−$389.67**) — *the original 675 transcription was RIGHT; the 7/30 "strike is 680" correction is REVERSED* — then BOUGHT three Jul-31-expiry puts: 672P −$416.66, 680P −$599.33, 680P −$414.66. 7/31: 680P liquidated **+$8.51** (= **−$1,005.48** on the pair); 672P **EXPIRED WORTHLESS** (−$416.66; row dated Aug-03, "Processing"). **Realized QQQ puts 7/30–7/31 = −$1,811.81** | **Mostly resolved by the activity tab.** Residue, labeled: **(a)** second 680P fill's closure is **INFERRED** inside the +$8.51 liquidation (no 680P EXPIRED row exists while the 672P has one; caveat: expiry rows post late) — realized total −$1,005.48 either way; **(b)** per-fill quantities not expanded in the view; **(c)** 675P buy row predates the window (basis from the 7/30 export). **Smallest action: next activity capture confirms (a); (b)/(c) cosmetic** |
| **D-1** | **AAPL 5-sh sale — details** | qty 15 Will-confirmed; sale itself unrecorded | Activity window (≥Jul-29) does not reach the sale | OPEN. Smallest action: **Will states date + price** — retires the last 7/30-window cash residual (~$565 class) |
| **D-5** | **Robinhood USO $128C — expired 7/22, outcome unrecorded 11 days** | Live row in FORGE since 7/20 | Not covered (Robinhood) | OPEN. Presumed expired worthless (~−$100 class) — **hypothesis, not confirmation**. Smallest action: **one Robinhood capture or Will's one-line confirm** (bundles with the D-6 fill-price residue + the WAL 77.5P verify) |
| **D-10** | **Account naming: "MAIN book" vs Traditional IRA •1326** | TERRY cards / FORGE say **"MAIN book"** | Fill records + both exports say Traditional IRA •1326 | OPEN — nothing renamed. The IRA short-stock constraint recurred again via D-12. Smallest action: **Will confirms "MAIN book" ≡ IRA •1326; then one fleet-wide label sweep** |
| **D-15** | **Pending −$1,754.94 + cash-flow window — ✅ RESOLVED (residue stated)** | Pass-1 hypothesis: structure right, figures estimated | **Pending = GLD −$1,108.14 + QQQ 687P −$841.99 + TLT 5-lot +$186.68 + QQQ 680P liq +$8.51 = −$1,754.94 EXACT** (the four Jul-31 trades, T+1-unsettled at the snapshot). **Settled cash:** $20,549.75 [7/30 09:40 position-view] + $1,500.00 *(the 7/30 pending — LANDED: Jul-29 ledger $22,049.75 = $20,549.75 + $1,500.00 exact; deposit/transfer class is a labeled hypothesis)* − $1,252.56 *(Jul-30 trades net: +1.99 +248.15 −72.05 −416.66 −599.33 −414.66)* = **$20,797.19 = activity ledger through Jul-30 EXACT**; money market $20,864.90 − $20,797.19 = **+$67.71 residue** (labeled hypothesis: money-market month-end dividend posted 7/31 — right size for ~4% on ~$20.8k — not among the transcribed rows). Cross-check: $20,864.90 − ledger-end $19,042.25 = $1,822.65 = $1,754.94 + $67.71 exact | **RESOLVED.** Pass-1's alternate reading ("$1,500 never landed; QQQ 680P netted $139.05") is **FALSIFIED** — the balancing items were the three then-invisible Jul-30 put buys. Residue action: **confirm the $67.71 at next capture (expect a dividend row)** |
| **D-11** | **TLT 77P 30 → 25 — ✅ RESOLVED** | TRY-FIRE-004 fill 30× @ $0.11 ($346.89 all-in); trim unrecorded | SOLD closing 5-lot 7/31 **+$186.68 net** = $0.3734/sh = **3.23×** the $0.11563 fees-in basis; realized ≈ **+$128.87** | **Will confirms: intentional partial profit-take ("sold 5 just to try to take some profits").** Original 30× fill record stands (per-unit basis identical to 5 decimals). The ≥3× gate line was genuinely met at the fill; trim = ⅙ vs the card's "half." Residual action: **TERRY re-grades PB-0002 Monday (PROME packet — not this file)** |
| **D-13** | **GLD 13 → 16 sh — ✅ RESOLVED** | Off-rail add, no record | Activity row 7/31: BOUGHT GLD **−$1,108.14** (~$369.4/sh) | **Broker-confirmed.** Cumulative off-rail 10→16 (~$2.2k, two windows). Residual action: **MIDAS routing = PROME** |
| **D-6** | **USO 150/165 Sep-18 spread — account — ✅ RESOLVED** | Absent from two consecutive IRA exports; Robinhood-by-elimination pending confirm | Not in this account | **Will CONFIRMS Robinhood (8/2).** Residue: exact fill price/qty at next Robinhood capture (card mark still unpriced) |

---

## Immediate Actions (8/2 session state, post pass-2)

| Item | State | Owner |
|---|---|---|
| **★ QQQ $687P ×3 — SELL Monday 8/3 (Will's stated intent)** | 🔴 Intent recorded (8/2), execution + fill owed; backstop: ITM at Monday's close → auto-exercise into short QQQ the IRA cannot hold (D-12) | **Will**; PROME surfacing |
| **TLT PB-0002 re-grade** (trim = ⅙ at 3.23×; card says half at ≥3×) | 🟡 D-11 resolved on the record (+$186.68 net, realized ≈ +$128.87); re-grade packet Monday | TERRY (PROME packet) |
| **Robinhood capture** — D-5 USO 128C outcome + D-6 spread fill price + WAL 77.5P (19 DTE, 13 days unverified) | 🟠 One capture closes all three | Will |
| **AAPL sale date/price** | 🟡 Last open leg of D-1; predates/below the activity window | Will |
| **GLD off-rail pattern → MIDAS** | 🟢 D-13 broker-confirmed; routing only (pattern recurring: 10→13→16) | PROME → MIDAS |
| **$67.71 settled-cash residue** | 🟢 Stated + hypothesized (money-market month-end dividend); confirm at next capture | ANVIL next pass |
| **680P second-fill closure confirm** (D-14a, inferred) | 🟢 Realized figure robust either way (−$1,005.48); confirm at next activity capture | ANVIL next pass |
| Aug-21 dust cluster (KRE 60P ×3 · OZK 45P ×4 + 42.5P ×1 · KELYA 7.5P ×1) | 🟡 19 days out, −93% to −98%; ~$98 residual value combined. EXIT-THESIS/ride-to-expiry class — zero effort, but pre-decide so it doesn't rot like D-5 | REGINALD / LABOR / Will |
| **TRY-FIRE-004 remainder (TLT Sep-30 77P ×25)** | 🟢 **+202.7% / +$585.92** — disarm gate = DGS10 <4.50; harvest state → PB-0002 re-grade | Will + TERRY |

---

*History → `_archive/JOURNAL.md` | Prior reconciles (7/30, 7/20, 7/16, 5/21) preserved in git history | Full-portfolio Feb snapshot → `PORTFOLIO.md` (**FROZEN/superseded, historical only — never cite as live**) | Position truth = Will/broker direct (off-repo)*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumer: `AGENTS/TERRY/scripts/positions_from_forge.py` (desk-dashboard Positions tab; keys on table headers, section names, and cell text — markdown emphasis and struck-through rows are visible to it). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069 n=3 — the 7/30 reconcile broke the parser silently). New consumers: add yourself to this list in the same commit that starts parsing.
