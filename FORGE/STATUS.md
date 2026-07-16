# FORGE — Trading Operations

> **Structured position-truth mirror — reconciled 2026-07-16 (~10:05-10:09 ET marks) from Will's broker screenshots (Fidelity IRA full position list incl. account total + Robinhood options list). Position truth is off-repo (Will/broker direct); this file is the fleet's parseable mirror and goes stale from the moment it's written — do NOT cite marks/P&L below as current without a fresh broker reconcile.** Refresher flow = Will-on-broker-export → PROME transcribes (this pass; prior reconcile was 2026-05-21). Old execution ledger + per-trade folders → `FORGE/_archive/`.

**Updated:** 2026-07-16 ~10:09 ET | **Fidelity cash:** $23,523.18 (60.05%) | **Fidelity account total:** $39,169.72 (day −$374.20 / −0.95%; open-position G/L −$2,913.50) | **Robinhood:** small satellite (options + 1 T share; account total not captured)

*Deltas vs the 5/21 reconcile: AAPL trimmed 30→20 · FXY 13 sh EXITED · GLD 10 sh NEW (cost $375.89) · USO 20 sh NEW (cost $115.75, ~7/14 entry) · KRE Dec-18 trimmed 7→5 · HBAN Oct-16 trimmed 4→2 · IWM 292P 7/17 NEW · all Jun-18/Jun-30 cluster positions expired off (HYG/FITB/EGBN/CF/AAL-Jun/SOFI/OWL/IWM-Jun gone) · Robinhood satellite added to mirror (first time).*

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (7/16 amendment = current). Per-domain reads in agent STATUS files. Forward catalysts → `PROME/DOCKET.tsv` (canonical).

---

## Fidelity — Longs

| Ticker | Type | Qty | Cost | Mark 7/16 | Value | P&L | Owner note |
|--------|------|-----|------|-----------|-------|-----|-----|
| AAPL | Stock | 20 | $23.64 | $330.005 | $6,600.10 | **+1295.7%** | trimmed 10 sh since 5/21 |
| GLD | Stock | 10 | $375.89 | $366.01 | $3,660.12 | −2.6% | NEW since 5/21 (MIDAS domain) |
| USO | Stock | 20 | $115.75 | $120.92 | $2,418.40 | **+4.5%** | NEW ~7/14 — Will's Hormuz-gap entry (BRENT) |
| APD | Stock | 2 | $294.79 | $291.45 | $582.90 | −1.1% | |
| TBT | Stock | 14 | $34.63 | $36.93 | $517.02 | **+6.6%** | 2× UST short — live duration-short leg (BOND/TERRY) |
| XLE | $65C Sep-30 | 2 | $2.28 | $0.47 | $94 | −79.4% | energy calls, deep underwater (BRENT) |

## Fidelity — Thesis Puts

### TLT — duration short (BOND/HENRY/TERRY) — ⚠️ overlaps armed TRY-FIRE-004; see TERRY packet 7/16

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $85P | Sep-30 | 2 | $2.52 | $2.17 | $434 | −13.8% (+13.0% day 7/16) |
| $82P | Oct-16 | 2 | $1.68 | $0.99 | $198 | −41.0% (+15.1% day 7/16) |

### KRE — regional banks (REGINALD)

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $60P | Dec-18 | 2 | $2.57 | $0.73 | $146 | −71.6% |
| $60P | Dec-18 | 3 (M) | $2.93 | $0.73 | $219 | −75.1% |
| $60P | Sep-30 | 2 | $2.27 | $0.21 | $42 | −90.7% |
| $60P | Aug-21 | 3 | $2.70 | $0.11 | $33 | −95.9% |

### WAL (REGINALD) — Sep-18s capture the 7/21 print

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $70P | Sep-18 | 1 | $7.69 | $1.10 | $110 | −85.7% |
| $67.5P | Sep-18 | 1 | $7.51 | $0.80 | $80 | −89.4% |
| $65P | Jul-17 | 1 | $4.36 | $0.05 | $5 | −98.9% (dies pre-print, as recorded) |

### OZK (REGINALD) — Aug-21s capture the 7/21 print

| Strike | Expiry | Qty | Cost | Mark | Value | P&L |
|--------|--------|-----|------|------|-------|-----|
| $45P | Aug-21 | 4 | $3.69 | $0.30 | $120 | −91.9% |
| $42.5P | Aug-21 | 1 | $2.12 | $0.05 | $5 | −97.6% |
| $42.5P | Jul-17 | 2 | $1.02 | $0.10 | $20 | −90.2% |

### Other puts

| Ticker | Strike | Expiry | Qty | Cost | Mark | Value | P&L | Note |
|--------|--------|--------|-----|------|------|-------|-----|------|
| APO | $95P | Dec-18 | 1 | $11.85 | $2.85 | $285 | −76.0% | BROCK thesis vehicle |
| HBAN | $16P | Oct-16 | 2 | $0.96 | $0.10 | $20 | −89.6% | trimmed 4→2; TERRY 7/9 stub exists |
| IWM | $292P | Jul-17 | 1 | $1.63 | $0.33 | $33 | −79.7% | NEW since 5/21 |
| ZION | $57.5P | Jul-17 | 1 | $4.01 | $0.01 | $1 | −99.8% | dies 3d pre-print (recorded) |
| FLG | $13P | Jul-17 | 3 | $0.95 | $0.02 | $6 | −97.9% | |
| CCL | $25P | Jul-17 | 2 | $1.96 | $0.01 | $2 | −99.5% | |
| DIS | $90P | Jul-17 | 2 | $1.99 | $0.02 | $4 | −99.0% | |
| AAL | $10P | Jul-17 | 1 | $0.57 | $0.01 | $1 | −98.2% | |
| KELYA | $7.5P | Aug-21 | 1 | $0.76 | $0.10 | $10 | −86.8% | LABOR thesis |

## Robinhood — satellite account (options + 1 T share)

| Position | Expiry | Qty | P&L (RH display) | Note |
|----------|--------|-----|------------------|------|
| QQQ $714C | 7/16 (0DTE) | 1 | +$65 / +77.4% | Will day-trade, expires today |
| QQQ $707P | 7/16 (0DTE) | 1 | −$78 / −51.0% | Will day-trade, expires today |
| USO $120C | 7/17 | 1 | −$61 / −23.0% | Hormuz-gap entry — TERRY triage 7/16 live |
| USO $127C | 7/17 | 1 | −$27 / −52.9% | Hormuz-gap entry — TERRY triage 7/16 live |
| WAL $75P | 7/17 | 1 | −$69 / −98.6% | dies pre-print |
| KRE $25P | 1/15/2027 | 1 | −$52 / −98.1% | deep-OTM lottery |
| T | stock | 1 | +$1.12 / +5.4% | |

---

## Immediate Actions (7/16 session state)

| Item | State | Owner |
|---|---|---|
| **USO 120C + 127C exp 7/17** | TERRY hold-vs-salvage triage IN FLIGHT (7/16); FAL-02 + post-closure COT land 7/17 | Will + TERRY/BRENT |
| **TRY-FIRE-004 TLT add** | Card ARMED 7/16, structure Will-approved; portfolio-aware final comparison in flight (book already holds TBT + 85P/82P ≈ $1,150 duration-short) | Will + TERRY |
| 7/17 expiry dust (WAL 65P · ZION 57.5P · FLG ×3 · OZK 42.5P ×2 · CCL ×2 · DIS ×2 · AAL · IWM 292P · RH WAL 75P) | ~$77 combined residual value — let-expire class unless Will salvages | Will (mechanical) |
| 7/21 triple print (WAL+OZK+ALLY) | Live captures: WAL Sep-18 70/67.5P · OZK Aug-21 45P ×4 + 42.5P — reshape-(c) gate reads at fire-time | REGINALD/PROME/TERRY |
| Energy convex arm (BRENT card) | Re-arm CONFIRMED 7/16; deploy = pass-on-chase, re-entry ~$80-82 pullback; Will already holds USO 20 sh + 2 calls | Will + BRENT |

---

*History → `JOURNAL.md` | Prior reconcile (5/21) preserved in git history | Full-portfolio Feb snapshot → `PORTFOLIO.md` (superseded, historical only) | Position truth = Will/broker direct (off-repo)*
