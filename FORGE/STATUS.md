# FORGE — Trading Operations

> **Structured position-truth mirror — reconciled 2026-07-20 (~8:27 AM ET pre-market marks) from Will's broker screenshots (Fidelity IRA full position list incl. account total + Robinhood options list). Position truth is off-repo (Will/broker direct); this file is the fleet's parseable mirror and goes stale from the moment it's written — do NOT cite marks/P&L below as current without a fresh broker reconcile.** Refresher flow = Will-on-broker-export → PROME transcribes (this pass; prior reconciles 2026-07-16, 2026-05-21). Old execution ledger + per-trade folders → `FORGE/_archive/`.

**Updated:** 2026-07-20 ~8:27 AM ET (pre-market) | **Fidelity cash:** $23,530.77 (59.66%) | **Fidelity account total:** $39,444.73 (day +$103.34 / +0.26%; open-position G/L −$312.34 / −1.92%) | **Robinhood:** small satellite (options + 1 T share; account total not captured)

*Deltas vs the 7/16 reconcile: **entire Jul-17 expiry dust cluster expired off as recorded** (Fidelity: WAL 65P · ZION 57.5P · FLG ×3 · CCL ×2 · DIS ×2 · AAL · IWM 292P · OZK 42.5P ×2 — and Robinhood: USO 120C/127C [TERRY triage resolved by expiry] · WAL 75P · both QQQ 0DTEs) · **cash ~flat (+$7.59) = NO fills over the gap — the 7/16 NO-ADD held** · core Fidelity thesis book position-for-position UNCHANGED · **Robinhood NEW ×3 (Will direct entries): QQQ $696P 7/20 (expires TODAY, ITM at QQQ ~$695.3 pre-market) · USO $128C 7/22 (Hormuz leg re-entered post-7/17 expiry) · WAL $77.5P Aug-21 (nearer-money print exposure, post-print expiry — changes the 7/21 WAL line)*.*

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (7/18 re-base + amendment #1 = current). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

| Ticker | Type | Qty | Cost | Mark 7/20 | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | 20 | $23.64 | $333.74 | $6,674.80 | **+1311.5%** | |
| GLD | Stock | 10 | $375.89 | $368.41 | $3,684.10 | −2.0% | MIDAS domain |
| USO | Stock | 20 | $115.75 | $123.96 | $2,479.20 | **+7.1%** | Will's Hormuz-gap entry (BRENT); +3.9% pre-market 7/20 |
| APD | Stock | 2 | $294.79 | $295.62 | $591.24 | +0.3% | |
| TBT | Stock | 14 | $34.63 | $36.33 | $508.62 | **+4.9%** | 2× UST short — live duration-short leg (BOND/TERRY) |
| XLE | $65C Sep-30 | 2 | $2.28 | $0.70 | $140 | −69.3% | energy calls (BRENT); recovering w/ the closure rally |

## Fidelity — Thesis Puts

### TLT — duration short (BOND/HENRY/TERRY) — ⚠️ overlaps armed TRY-FIRE-004 (NO-ADD stands; live entry read = TERRY 7/20)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $85P | Sep-30 | 2 | $2.52 | $1.78 | $356 | −29.3% (TLT $84.52 → strike slightly ITM) |
| $82P | Oct-16 | 2 | $1.68 | $0.79 | $158 | −52.9% |

### KRE — regional banks (REGINALD)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $60P | Dec-18 | 2 | $2.57 | $0.80 | $160 | −68.8% |
| $60P | Dec-18 | 3 (M) | $2.93 | $0.80 | $240 | −72.7% |
| $60P | Sep-30 | 2 | $2.27 | $0.28 | $56 | −87.7% |
| $60P | Aug-21 | 3 | $2.70 | $0.10 | $30 | −96.3% |

### WAL (REGINALD) — Sep-18s + RH Aug-21 capture the 7/21 print

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $70P | Sep-18 | 1 | $7.69 | $1.55 | $155 | −79.8% |
| $67.5P | Sep-18 | 1 | $7.51 | $1.35 | $135 | −82.0% |

*(+ Robinhood WAL $77.5P Aug-21 ×1 below — the nearest-money WAL leg, ~5.8% OTM at $82.30.)*

### OZK (REGINALD) — Aug-21s capture the 7/21 print

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $45P | Aug-21 | 4 | $3.69 | $0.35 | $140 | −90.5% |
| $42.5P | Aug-21 | 1 | $2.12 | $0.21 | $21 | −90.1% |

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18 | 1 | $11.85 | $3.00 | $300 | −74.7% | BROCK thesis vehicle |
| HBAN | $16P | Oct-16 | 2 | $0.96 | $0.40 | $80 | −58.2% | EXIT-THESIS dust (Will 7/18) — rides to expiry, zero effort |
| KELYA | $7.5P | Aug-21 | 1 | $0.76 | $0.05 | $5 | −93.4% | LABOR thesis |

## Robinhood — satellite account (options + 1 T share)

| Position | Expiry | Qty | P&L (RH display) | Note |
|----------|--------|-----|------------------|------|
| **QQQ $696P** | **7/20 (TODAY)** | 1 | +$74 / +16.0% | NEW — Will day-trade class; ITM at QQQ ~$695.3 pre-market — same-day decision |
| **USO $128C** | 7/22 | 1 | −$2 / −1.1% | NEW — Hormuz leg re-entered (3.3% OTM at $123.96); expires EIA post-closure-print day |
| **WAL $77.5P** | Aug-21 | 1 | $0.00 / 0.0% | NEW (~7/17-7/20 fill) — nearest-money WAL print exposure, survives the 7/21 AMC |
| KRE $25P | 1/15/2027 | 1 | −$38 / −71.7% | deep-OTM lottery |
| T | stock | 1 | +$1.18 / +5.7% | |

---

## Immediate Actions (7/20 session state)

| Item | State | Owner |
|---|---|---|
| **QQQ $696P expires TODAY** | ITM pre-market (QQQ $695.33); sell-or-exercise-or-expire decision intraday | Will (day-trade class) |
| **TRY-FIRE-004 TLT ladder — live go/no-go entry read** | Card ARMED / NO-ADD stands; $500 banked; TERRY packet live (rule-#6 day-color = arm-LIT + TLT-GREEN; TLT green pre-market 7/20) — now FILLABLE with this export | Will + TERRY |
| **7/21 four-rail cluster (WAL+OZK AMC · ALLY 7:30a · $85×3 · FL emp)** | Live captures: WAL Sep-18 70/67.5P + **RH 77.5P Aug-21** · OZK Aug-21 45P ×4 + 42.5P — reshape arithmetic rebuilds from THIS export (position-vintage warning satisfied) | REGINALD/PROME/TERRY |
| USO $128C 7/22 | Will-monitored (his Hormuz leg); 2 DTE, decays into the 7/22 EIA print | Will + BRENT |
| Energy convex arm (BRENT card) | Pass-on-chase stands; re-entry ~$80-82 pullback; Will holds USO 20 sh + 128C | Will + BRENT |

---

*History → `JOURNAL.md` | Prior reconciles (7/16, 5/21) preserved in git history | Full-portfolio Feb snapshot → `PORTFOLIO.md` (superseded, historical only) | Position truth = Will/broker direct (off-repo)*
