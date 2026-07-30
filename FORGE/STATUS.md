# FORGE — Trading Operations

> **Structured position-truth mirror — reconciled 2026-07-30 (~09:40 AM ET broker export) from Will's Fidelity Traditional IRA •1326 position export (PROME-transcribed; the screenshot itself stays off-repo per the public-prep rule). Position truth is off-repo (Will/broker direct); this file is the fleet's parseable mirror and goes stale from the moment it's written — do NOT cite marks/P&L below as current without a fresh broker reconcile.** Refresher flow = Will-on-broker-export → PROME transcribes → ANVIL reconciles (this pass; prior reconciles 2026-07-20, 2026-07-16, 2026-05-21). Old execution ledger + per-trade folders → `FORGE/_archive/`.
>
> ⚠️ **THIS EXPORT COVERS ONE ACCOUNT ONLY — Fidelity Traditional IRA •1326.** The Robinhood satellite was **not** captured this pass, and at least one live card (USO 150/165 Sep-18 spread) does **not** appear in it. See **§ Reconcile discrepancies (7/30)** before treating any absence below as a closed position.

**Updated:** 2026-07-30 ~09:40 AM ET [broker export] | **Fidelity cash (money market):** $20,549.75 (50.64%) | **Fidelity positions market value:** $18,527.27 | **Pending activity:** $1,500.00 *(unidentified — see discrepancy D-7)* | **Fidelity account total:** $40,577.02 | **Robinhood:** small satellite — **NOT captured this export; rows below are 7/20-vintage and unverified today**

*Export arithmetic verified by ANVIL: positions $18,527.27 + cash $20,549.75 + pending $1,500.00 = $40,577.02 account total, exact to the cent; cash 50.64% checks. The transcription is internally consistent.*

*Deltas vs the 7/20 reconcile: **account total +$1,132.29** ($39,444.73 → $40,577.02) while **cash fell $2,981.02** ($23,530.77 → $20,549.75) and the cash share dropped **59.66% → 50.64%** — capital was deployed over the gap. **Four position changes are NOT on any PROME/TERRY rail: AAPL 20→15 sh · GLD 10→13 sh · USO 20→35 sh · QQQ Jul-30 $675P ×1 NEW (expires TODAY).** Recorded-and-confirmed changes: **TLT Sep-30 $77P ×30 present** (TRY-FIRE-004 re-fire, now **+116.2%** — the first live TERRY card is the book's best position) · **VIXCS event box CLOSED 7/30 ~09:50 ET at −$111.60** (the export's 09:40 snapshot still carries both VIXW legs — it pre-dates the exit by ~10 min). The **entire thesis put book is position-for-position unchanged** in strike/expiry/qty/basis vs 7/20 (KRE ×4 lots, WAL ×2, OZK ×2, APO, HBAN, KELYA) — no adds, no trims, no rolls.*

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (7/18 re-base + amendment #1 = current). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

*All marks/values `[broker export 2026-07-30 ~09:40 ET]`.*

| Ticker | Type | Qty | Cost | Mark 7/30 | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | **15** | $23.64 | $334.245 | $5,013.67 | **+1,313.6%** | ⚠️ **qty 20 → 15 (−5 sh) vs 7/20 — no PROME/TERRY record of the sale.** Basis/unit unchanged → a partial sale, not a re-basis. See D-1 |
| GLD | Stock | **13** | $374.57 | $373.95 | $4,861.35 | −0.2% | MIDAS domain. ⚠️ **qty 10 → 13 (+3 sh), basis $375.89 → $374.57** → 3 sh added at ~$370.17 implied. No rail. See D-2 |
| USO | Stock | **35** | $121.88 | $127.1102 | $4,448.85 | **+4.3%** | Will's Hormuz-gap entry (BRENT). ⚠️ **qty 20 → 35 (+15 sh), basis $115.75 → $121.88** → 15 sh added at ~$130.06 implied. Position ~doubled off-rail. See D-3 |
| APD | Stock | 2 | $294.79 | $309.445 | $618.89 | **+5.0%** | thesis tag still unassigned (`ACTIVE_DECISIONS` candidate row) |
| TBT | Stock | 14 | $34.63 | $37.9657 | $531.51 | **+9.6%** | 2× UST short — live duration-short leg (BOND/TERRY); the grind is paying |
| XLE | $65C Sep-30 | 2 | $2.28 | $0.53 | $106.00 | −76.7% | energy calls (BRENT); **deteriorated from −69.3% on 7/20** as the closure rally faded |

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)

> Distinct class: these carry a **pre-registered exit DATE** and die on the clock, not on a thesis. They must not be read as part of the standing book.

| Position | Expiry | Qty | Cost | Outcome |
|----------|--------|-----|------|---------|
| ~~**VIX $20C/$25C call debit spread** (`VIXW`)~~ | Aug-05-2026 | ~~4~~ | $0.70 net debit | **✅ CLOSED 2026-07-30 ~09:50 ET — REALIZED −$111.60 (−38.8%).** `TRY-VIOLET-VIXCS` (VIOLET thesis / TERRY construction). Exited as **one spread ticket** at **net $0.45 credit** — StC 4× 20C @ $0.63 / BtC 4× 25C @ $0.18, limit walked 0.50→0.45 per TERRY runbook §10; Will-approved at live marks, Will-executed. **Proceeds $176.10 vs $287.70 all-in.** Exited **on the mandatory date, un-killed** (all 5 stand-downs ZERO-tripped at the 7/29 settle) with **no roll**, per spec. Filled 7/27 ~11:35 ET (long 20C $1.23 / short 25C $0.53); the overnight VIX fade (20.66 settle → ~18.6 at ticket) pre-empted the sell-into-strength branch — VIOLET falsified its own brief's headline branch pre-open and told TERRY before the open. **Open items:** TERRY owns card §10 grade + PB-0003 close; VIOLET owns the settle re-grade. `PROME/DOCKET.tsv` row 61 = RESOLVED. *(The 09:40 export still shows both VIXW legs at $240.00 / −$104.00 — it pre-dates the exit by ~10 minutes; see D-8.)* |

## Fidelity — Off-thesis / day-trade class

> Same class as the 7/20 QQQ $696P: Will-direct, short-dated, **on no PROME rail and owned by no agent**. Recorded here so it is not invisible, not because the fleet manages it.

| Position | Expiry | Qty | Cost | Mark 7/30 | Value | P&L | Note |
|----------|--------|-----|------|-----------|-------|-----|------|
| **QQQ $675P** | **Jul-30-2026 — ★ EXPIRES TODAY** | 1 | $3.92 | $3.70 | $370.00 | −5.5% | ⚠️ **NEW since 7/20 — first appearance in any FORGE surface.** In the **Fidelity IRA**, not Robinhood (unlike the 7/20 QQQ 696P precedent). **OTM and moving away:** QQQ **$678.36, +2.51% [live fetch 2026-07-30 11:02 ET]** vs the $675 strike = **$3.36 OTM on a strongly green tape.** Needs a Will decision by ~3:45 PM — see D-4 and Immediate Actions |

## Fidelity — Thesis Puts

### TLT — duration short (BOND/HENRY/TERRY) — TRY-FIRE-004 FILLED 7/20 (first live TERRY card)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| **$77P** | **Sep-30** | **30** | **$0.12** *(broker basis, fees-in)* | $0.25 | $750.00 | **★ +$403.11 / +116.2%** — the book's best live position. **Card ZONE-3 harvest gate is "half at ≥3×"; at 2.16× it is NOT yet triggered.** Fill was $0.11/contract premium ($330) + $16.89 fees = $346.89 all-in → broker shows $0.12/unit. BE 76.89. TERRY/PB-0002 |
| $85P | Sep-30 | 2 | $2.52 | $3.00 | $600.00 | **+$96.65 / +19.2%** — **flipped positive** (was −29.3% on 7/20) |
| $82P | Oct-16 | 2 | $1.68 | $1.52 | $304.00 | −$31.35 / −9.3% — **recovered hard** (was −52.9% on 7/20) |

*The duration-short complex (TBT 14 sh + all three TLT put legs) is **the only part of the book working**: +$46.69 + $403.11 + $96.65 − $31.35 = **+$515.10** combined open G/L.*

### KRE — regional banks (REGINALD)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $60P | Dec-18 | 2 | $2.57 | $0.62 | $124.00 | −$389.34 / −75.9% |
| $60P | Dec-18 | 3 (M) | $2.93 | $0.62 | $186.00 | −$692.02 / −78.8% |
| $60P | Sep-30 | 2 | $2.27 | $0.11 | $22.00 | −$431.35 / −95.2% |
| $60P | Aug-21 | 3 | $2.70 | $0.05 | $15.00 | −$794.02 / −98.2% — **effectively dead; 22 days to expiry** |

### WAL (REGINALD) — Sep-18s (the 7/21 print resolved NOT-FIRED)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $70P | Sep-18 | 1 | $7.69 | $0.55 | $55.00 | −$713.67 / −92.9% |
| $67.5P | Sep-18 | 1 | $7.51 | $0.30 | $30.00 | −$720.67 / −96.0% |

*(Robinhood WAL $77.5P Aug-21 ×1 — **not in this export's account, unverified today**; see Robinhood section.)*

### OZK (REGINALD) — Aug-21s (the 7/21 print resolved NOT-FIRED)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $45P | Aug-21 | 4 | $3.69 | $0.15 | $60.00 | −$1,414.70 / −95.9% |
| $42.5P | Aug-21 | 1 | $2.12 | $0.05 | $5.00 | −$206.67 / −97.6% |

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18 | 1 | $11.85 | $2.35 | $235.00 | −$949.67 / −80.2% | BROCK thesis vehicle |
| HBAN | $16P | Oct-16 | 2 | $0.96 | $0.25 | $50.00 | −$141.34 / −73.9% | EXIT-THESIS dust (Will 7/18) — rides to expiry, zero effort |
| KELYA | $7.5P | Aug-21 | 1 | $0.76 | $0.05 | $5.00 | −$70.67 / −93.4% | LABOR thesis |

## Robinhood — satellite account (options + 1 T share)

> ⚠️ **NOT CAPTURED IN THE 7/30 EXPORT.** These rows are **7/20-vintage and unverified today** — retained, not deleted, because absence from a single-account export is not evidence of closure. Every row here needs a Robinhood export to resolve.

| Position | Expiry | Qty | State | Note |
|----------|--------|-----|-------|------|
| ~~QQQ $696P~~ | 7/20 EXPIRED | 1 | **CLOSED ~−$455** | RESOLVED (Will-reported 7/20 PM): recovered only ~$8 of premium; QQQ closed knife-edge ATM $696. Day-trade class, off-thesis |
| ~~USO $128C~~ | **7/22 — EXPIRED 8 DAYS AGO** | 1 | ⚠️ **OUTCOME UNRECORDED** | Hormuz leg; 3.3% OTM at the 7/20 mark. **USO closed 7/22 well below the $128 strike on the available record → presumed expired worthless (~−$100 class), but this is a HYPOTHESIS, not a confirmation.** See D-5 |
| **USO $150/$165 call spread** | Sep-18 | ~1 | ⚠️ **ACCOUNT UNRESOLVED** | FILLED 7/24, net debit ~$300 [Will verbal 7/25; TERRY mid was $2.98]. BRENT tail-rider card, Will-driven w/ TERRY live re-quote. **Absent from the Fidelity IRA export — account not confirmed.** BE USO ~$153 · max profit ~$1,200 (~4:1) · defined-risk. Rule-#6-clean red-day entry; mgmt = BRENT card frozen terms. See D-6 |
| **WAL $77.5P** | Aug-21 | 1 | unverified today | Nearest-money WAL leg (~5.8% OTM at $82.30 on 7/20). Survived the 7/21 AMC, which resolved NOT-FIRED |
| KRE $25P | 1/15/2027 | 1 | unverified today | deep-OTM lottery; −$38 / −71.7% at the 7/20 mark |
| T | stock | 1 | unverified today | +$1.18 / +5.7% at the 7/20 mark |

---

## ⚠️ Reconcile discrepancies (7/30) — open items for Will

> Built by ANVIL against the 7/30 export. **Nothing here has been resolved by invention** — hypotheses are labeled as such. Ranked by decision urgency.

| # | Item | What the record says | What the export says | Disposition |
|---|------|----------------------|----------------------|-------------|
| **D-4** | **QQQ $675P expires TODAY** | **Nothing — absent from every FORGE/PROME surface** | 1 contract, basis $3.92, mark $3.70, value $370.00 | **★ NEEDS A WILL DECISION BY ~3:45 PM ET.** QQQ **$678.36 +2.51% [live 11:02 ET]** = **$3.36 OTM on a green tape**; time value is bleeding to zero. Two live risks: **(a)** let it expire → total loss of the remaining ~$370 of value; **(b)** if QQQ reverses **below $675** (−0.5%) it auto-exercises into a **short 100-share QQQ position the IRA cannot hold** → broker-forced liquidation. **On no rail, owned by no agent.** Recommend: Will decides sell-to-close vs. let-expire; if let-expire, confirm Fidelity's do-not-exercise handling |
| **D-6** | **USO 150/165 Sep-18 call spread — account unresolved** | FILLED 7/24, ~$300 net debit, recorded in FORGE + `ACTIVE_DECISIONS` + DOCKET 2026-09-18 (BRENT tail-rider card) | **ABSENT from the Fidelity IRA •1326 export** | **UNRESOLVED — do not conclude anything.** Hypothesis (labeled): it sits in the Robinhood satellite, which this export does not cover. **Not verified.** The 7/25 record itself says "exact debit/qty/account TBC at next broker export" — that TBC is still open because the export was single-account. **Ask: which account holds it, and pull that export** |
| **D-1** | **AAPL 20 → 15 shares** | 20 sh @ $23.64 [7/20 export] | **15 sh** @ $23.64 (basis/unit unchanged) | **5 shares left the account with no fleet record.** Basis/unit unchanged ⇒ a partial *sale*, not a re-basis or split. At today's $334.245 that is ~$1,671 of proceeds. **Ask Will: sold when, at what price, and why** (it is the largest unexplained cash event in the window and it feeds D-7) |
| **D-2** | **GLD 10 → 13 shares** | 10 sh @ $375.89 [7/20] | **13 sh** @ **$374.57** | **+3 sh added off-rail** at ~$370.17/sh implied (solving the blended basis). MIDAS domain — MIDAS has no record of it in any FORGE surface. **Ask Will: date/price; route to MIDAS** |
| **D-3** | **USO 20 → 35 shares** | 20 sh @ $115.75 [7/20] | **35 sh** @ **$121.88** | **+15 sh added off-rail** at ~$130.06/sh implied. **This ~doubles Will's outright oil exposure** ($2,315 → $4,266 at cost) while the standing rail is **PASS-ON-CHASE** (Will 7/16, reaffirmed at the 7/24 tail-rider fill — the main convex arm stays gated on the OVX cooldown). The add is Will's own book and not a rule break, but **BRENT's concentration arithmetic and TERRY's §9 "one Mideast-stays-hot bet" sizing both need rebuilding from 35 sh, not 20.** Route to BRENT + TERRY |
| **D-7** | **Cash-flow residual ~$565 + $1,500 pending activity unidentified** | — | Cash $23,530.77 → $20,549.75 (−$2,981.02); pending activity **$1,500.00** | **Two separate open items.** ① **Residual:** known outflows over the gap = TLT 77P $346.89 + VIXCS $287.70 + QQQ 675P $391.66 + GLD $1,110.51 + USO $1,950.90 = **$4,087.66**, which against the actual −$2,981.02 implies **$1,106.64 of inflow**. The only known inflow (AAPL −5 sh) would fetch ~$1,671 at today's price ⇒ **~$565 unexplained**. Hypotheses (labeled, unresolved): AAPL sold earlier/lower; another fill or fee not in any record; a withdrawal. ② **Pending $1,500.00** is a round number included in the account total but not in cash — reads like a **deposit in transit** rather than unsettled trade proceeds, but that is a hypothesis. **Ask Will both** |
| **D-5** | **Robinhood USO $128C 7/22 — expired 8 days ago, outcome unrecorded** | Live row in FORGE since 7/20 | Not covered (Robinhood) | The 7/20 reconcile's own lesson (the QQQ 696P) was that dated legs must be resolved on their date. This one **rotted through its expiry unresolved**. Presumed worthless (hypothesis). **Resolve at the Robinhood export** |
| **D-8** | **VIXW legs still present in the 09:40 export** | Exited 7/30 ~09:50 ET, realized −$111.60 | Both legs live: 20C $240.00 / 25C −$104.00 (net $136.00) | **Benign vintage artifact — the export pre-dates the exit by ~10 min.** Recorded so nobody re-opens the box. **Derived post-exit view (ANVIL arithmetic, NOT broker truth):** positions $18,391.27 · cash $20,725.85 · total ~$40,617.12 |
| **D-9** | **TLT 77P basis $0.12 vs the recorded $0.11 fill** | $0.11/contract, "$330 + ~$15 fees" | $0.12/unit; G/L implies total basis $346.89 | **BENIGN — verified, not merely assumed.** $330.00 premium + **$16.89** actual fees = $346.89 ⇒ $0.11563/unit, which the broker rounds to $0.12. FORGE records the *premium* price; the broker records *fees-in* basis. **Nothing to fix — but note BE is $76.89 off the premium, ~$76.844 off the all-in basis.** The card's estimate of "~$15 fees" was $1.89 light |
| **D-10** | **Account naming: "MAIN book" vs Traditional IRA •1326** | TERRY cards / FORGE say **"MAIN book"** | Fill records + this export say **Traditional IRA •1326** | **PENDING WILL CONFIRM — nothing renamed this pass.** If "MAIN book" ≡ IRA •1326, the label is harmless shorthand; if the fleet has been assuming a taxable account, then **every card's tax/assignment reasoning is wrong** (an IRA cannot hold the short stock that D-4 could create — which is exactly why this matters today, not eventually). **Ask Will, then sweep the label fleet-wide in one pass** |

---

## Immediate Actions (7/30 session state)

| Item | State | Owner |
|---|---|---|
| **★ QQQ $675P expires TODAY** | 🔴 **DECISION NEEDED BY ~3:45 PM ET** — $3.36 OTM (QQQ $678.36 +2.51% [live 11:02 ET]); ~$370 of value bleeding to zero, plus IRA auto-exercise risk if QQQ breaks back under $675. **On no rail** | **Will** (day-trade class) |
| **USO 150/165 Sep-18 spread — locate it** | 🟠 Absent from the only account exported; account unresolved (D-6). Blocks the BRENT card's mark and the 7/25 "exact debit/qty/account TBC" | Will → Robinhood export; PROME/BRENT |
| ~~TRY-VIOLET-VIXCS mandatory exit 7/30~~ | ✅ **DONE 7/30 ~09:50 ET** — net $0.45 credit, realized **−$111.60 (−38.8%)**, un-killed on the mandatory date, no roll. TERRY owes card §10 + PB-0003; VIOLET owes the settle re-grade | TERRY / VIOLET |
| **TRY-FIRE-004 (TLT Sep-30 77P ×30)** | 🟢 **+116.2% / +$403.11** — best position in the book. **Harvest gate is ≥3× and is NOT met at 2.16×**; disarm gate = DGS10 <4.50. Card rides unchanged | Will + TERRY |
| **Three off-rail position changes (AAPL −5 · GLD +3 · USO +15)** | 🟠 Unrecorded; the USO one ~doubles outright oil exposure and **invalidates the current concentration arithmetic** (D-1/2/3) | Will → confirm; route BRENT/MIDAS/TERRY |
| **$1,500 pending + ~$565 cash residual** | 🟡 Unidentified (D-7). Not urgent, but it is the class of gap that hides a real fill | Will → confirm |
| Aug-21 dust cluster (KRE 60P ×3 · OZK 45P ×4 + 42.5P ×1 · KELYA 7.5P ×1) | 🟡 22 days out, −93% to −98%; ~$85 of residual value combined. EXIT-THESIS/ride-to-expiry class — zero effort, but pre-decide so it doesn't rot like D-5 | REGINALD / LABOR / Will |

---

*History → `_archive/JOURNAL.md` | Prior reconciles (7/20, 7/16, 5/21) preserved in git history | Full-portfolio Feb snapshot → `PORTFOLIO.md` (**FROZEN/superseded, historical only — never cite as live**) | Position truth = Will/broker direct (off-repo)*

> 🤖 **PARSED BY MACHINE — this file's format is an interface.** Known consumer: `AGENTS/TERRY/scripts/positions_from_forge.py` (desk-dashboard Positions tab; keys on table headers, section names, and cell text — markdown emphasis and struck-through rows are visible to it). **Any structural change (headers, sections, row conventions) = a breaking change: sweep consumers BEFORE committing** (PAT-069 n=3 — the 7/30 reconcile broke the parser silently). New consumers: add yourself to this list in the same commit that starts parsing.
