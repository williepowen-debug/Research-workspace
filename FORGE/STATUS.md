# FORGE — Trading Operations

**Updated:** 2026-05-21 ~14:03 ET (Fidelity export) | **Cash:** $25,138.80 (55.17%) | **Pending:** -$288.28 | **Account total:** see broker for live

*Reconciled against Fidelity CSV 2026-05-21 14:03 ET (account 216461326 Traditional IRA) + SAM TRADE.md v1.4. Recon worksheet: `FORGE/scratch/REHAB_RECON_2026-05-21.md`. Per-trade folders KRE/WAL/OZK are Mar 17 historical reference, not refreshed in this pass.*

---

## Thesis

Current regime + scenario weights → `HEARTBEAT.md` (refreshed 2026-05-21 ~16:25 ET). Per-domain reads in agent STATUS files (BROCK / REGINALD / HENRY / SAM / VIOLET / BOND / BRENT).

---

## Thesis Puts (Holding)

### KRE — 19 contracts (REGINALD)

| Strike | Expiry | Qty | Cost | P&L | Value |
|--------|--------|-----|------|-----|-------|
| $60P | Dec 18 | 7† | $2.72 wt avg | **-16.1%** | $1,568 |
| $60P | Sep 30 | 2 | $2.27 | -34.27% | $298 |
| $60P | Aug 21 | 3 | $2.70 | -64.04% | $291 |
| $67P | Jun 30 | 1 | $3.26 | -54.87% | $147 |
| $65P | Jun 30 | 4 | $2.81 | -66.57% | $376 |
| $63P | Jun 30 | 1 | $2.79 | -79.55% | $57 |
| $60P | Jun 18 | 1 | $2.66 | -93.98% | $16 |

† Merged: 4 contracts cash @ $2.57 + 3 contracts margin @ $2.93. Weighted avg cost $2.72.

### WAL — 8 contracts (REGINALD)

| Strike | Expiry | Qty | Cost | P&L | Value |
|--------|--------|-----|------|-----|-------|
| $85P | Jun 18 | 1 | $5.91 | **+18.50%** | $700 |
| $77.5P | Jun 18 | 1 | $5.51 | -53.70% | $255 |
| $67.5P | Jun 18 | 2 | $4.91 | -91.85% | $80 |
| $65P | Jun 18 | 1 | $4.50 | -94.45% | $25 |
| $70P | Sep 18 | 1 | $7.69 | -57.07% | $330 |
| $67.5P | Sep 18 | 1 | $7.51 | -64.04% | $270 |
| $65P | Jul 17 | 1 | $4.36 | -80.49% | $85 |

### TLT — 7 contracts (HENRY / BOND)

| Strike | Expiry | Qty | Cost | P&L | Value |
|--------|--------|-----|------|-----|-------|
| $85P | Jun 18 | 3 | $0.82 | **+92.22%** | $471 |
| $85P | Sep 30 | 2 | $2.52 | +16.81% | $588 |
| $82P | Oct 16 | 2 | $1.68 | +6.75% | $358 |

### APO — 2 contracts (BROCK)

| Strike | Expiry | Qty | Cost | P&L | Value |
|--------|--------|-----|------|-----|-------|
| $95P | Dec 18 | 1 | $11.85 | -76.79% | $275 |
| $100P | Jun 18 | 1 | $7.71 | -98.71% | $10 |

BROCK 5/21 disposition: Dec hold (thesis vehicle); Jun let-expire.

### OZK — 7 contracts (REGINALD)

| Strike | Expiry | Qty | Cost | P&L | Value |
|--------|--------|-----|------|-----|-------|
| $45P | Aug 21 | 4 | $3.69 | -59.32% | $600 |
| $42.5P | Aug 21 | 1 | $2.12 | -57.49% | $90 |
| $42.5P | Jul 17 | 2 | $1.02 | -50.83% | $100 |

---

## Other Puts

### Regional banks (REGINALD)

| Ticker | Strike | Expiry | Qty | Cost | P&L | Value |
|--------|--------|--------|-----|------|-----|-------|
| HBAN | $16P | Oct 16 | 4 | $0.96 | **+14.97%** | $440 |
| FITB | $45P | Jun 18 | 2 | $0.91 | -61.41% | $70 |
| ZION | $57.5P | Jul 17 | 1 | $4.01 | -70.06% | $120 |
| FLG | $13P | Jul 17 | 3 | $0.95 | -63.29% | $105 |
| EGBN | $25P | Jun 18 | 1 (M) | $1.57 | -87.24% | $20 |

### Credit / Private credit (BROCK)

| Ticker | Strike | Expiry | Qty | Cost | P&L | Value |
|--------|--------|--------|-----|------|-----|-------|
| HYG | $75P | Jun 18 | 8 | $0.31 | -90.22% | $24 |
| ARES | $95P | Jun 18 | 1 | $8.03 | -95.02% | $40 |
| OWL | $9.5P | Jun 05 | 2 | $0.59 | -65.92% | $40 |

BROCK 5/21: ARES let-expire. HYG Jun→Dec roll never executed during dark window (LESSONS #16, execution-rails gap).

### Consumer / Other

| Ticker | Strike | Expiry | Qty | Cost | P&L | Value |
|--------|--------|--------|-----|------|-----|-------|
| AAL | $10P | Jun 18 | 2 | $0.90 | -94.43% | $10 |
| AAL | $10P | Jul 17 | 1 | $0.57 | -75.30% | $14 |
| CCL | $25P | Jul 17 | 2 | $1.96 | -17.21% | $324 |
| DIS | $90P | Jul 17 | 2 | $1.99 | -77.86% | $88 |
| SOFI | $16P | Jun 05 | 1 | $0.71 | **+13.20%** | $80 |
| KELYA | $7.5P | Aug 21 | 1 | $0.76 | -0.89% | $75 |

### Index (HENRY)

| Ticker | Strike | Expiry | Qty | Cost | P&L | Value |
|--------|--------|--------|-----|------|-----|-------|
| IWM | $250P | Jun 30 | 1 | $7.69 | -84.78% | $117 |
| IWM | $257P | Jun 18 | 1 | $9.39 | -87.65% | $116 |
| QQQ | $698P | May 21 | 1 | $3.82 | -99.74% | $1 |

---

## Longs

| Ticker | Type | Qty | Cost | P&L | Value |
|--------|------|-----|------|-----|-------|
| **AAPL** | Stock | 30 | $23.64 | **+1190.07%** | $9,150.90 |
| TBT | Stock | 14 | $34.63 | +6.91% | $518.35 |
| FXY | Stock | 13 | $58.32 | -0.93% | $751.20 |
| APD | Stock | 2 | $294.79 | -1.93% | $578.25 |
| FXY | $58C Jun 18 | 1‡ | $0.40 | — | $40 (cost) |
| USO | $155C Jun 12 | 1 | $10.08 | -60.81% | $395 |
| XLE | $65C Sep 30 | 2 | $2.28 | -30.17% | $318 |
| CF | $130C Jun 18 | 1 | $11.67 | -71.72% | $330 |

‡ FXY $58C per SAM `TRADE.md` v1.4 — **not in 5/21 2:03 PM Fidelity CSV**. May be in separate account, executed post-CSV, or unsettled at export time. Reconciliation pending next CSV refresh.

FXY share cost basis: Fidelity reports $58.32 blended; SAM v1.4 reports $57.48 blended ($747.18 entry). Minor drift, likely Fidelity blended-cost convention with Tranche 2 unsettled.

---

## Immediate Actions

*Decisions needed, who owns them, by when. Surfaced not prescribed. See PROTOCOL.md (advisor not authority).*

### Expiring today — mechanical

| Position | State | Decision | Owner |
|---|---|---|---|
| QQQ $698P May 21 × 1 | $0.01, -99.74% | Let expire (already decided by tape) | — |

### 6/18 expiry cluster — theta-killer dispositions (28 days)

*BROCK LESSONS #16: previous dark-window rolls (HYG Jun→Dec) died for lack of execution mechanism. Same gap repeats here unless decisions are made and a path to execute exists.*

| Position | Last | P&L | Disposition status | Owner |
|---|---|---|---|---|
| HYG $75P × 8 | $0.03 | -90% | Roll vs let-expire — undecided since Apr dark window | Will + BROCK |
| APO $100P × 1 | $0.10 | -99% | **Let expire** (BROCK 5/21) | BROCK ✅ |
| ARES $95P × 1 | $0.40 | -95% | **Let expire** (BROCK 5/21) | BROCK ✅ |
| EGBN $25P × 1 (margin) | $0.20 | -87% | Roll vs let-expire — undecided | Will + REGINALD |
| AAL $10P × 2 | $0.05 | -94% | Roll vs let-expire — undecided | Will |
| WAL $65P × 1 | $0.25 | -94% | Roll vs let-expire — undecided | Will + REGINALD |
| WAL $67.5P × 2 | $0.40 | -92% | Roll vs let-expire — undecided | Will + REGINALD |
| KRE $60P × 1 | $0.16 | -94% | Roll vs let-expire — undecided | Will + REGINALD |

### 6/18 expiry cluster — still-live (Will-decide closer to date)

| Position | Last | P&L | Note | Owner |
|---|---|---|---|---|
| WAL $77.5P × 1 | $2.55 | -54% | At WAL $78.53 → near the money | Will + REGINALD |
| WAL $85P × 1 | $7.00 | +18% | In the money | Will + REGINALD |
| TLT $85P × 3 | $1.57 | +92% | Roll-out decision worth running (May 15 $88P from Mar STATUS at +100% appears unclosed-into-expiry — JOURNAL gap) | Will + HENRY/BOND |
| IWM $257P × 1 | $1.16 | -88% | Index, near-money | Will + HENRY |
| FITB $45P × 2 | $0.35 | -61% | Regional bank, deep OTM | Will + REGINALD |
| CF $130C × 1 | $3.30 | -72% | Long call, ag thesis | Will |

### SAM exit watches (SAM-owned)

| Trigger | State | Owner |
|---|---|---|
| FXY Jun-18 $58C × 1 expiry | 28d; per SAM v1.4 (reconciliation pending; not in 5/21 CSV) | SAM |
| FXY $55.05 share stop | FXY $57.77; -2.72 buffer | SAM |
| Sep-18 $60C × 5-10 contracts pending entry | Awaiting post-CPI cheaper window | SAM + Will |

### Other near-dated (5-40 days)

| Position | Days to expiry | Last | P&L | Note |
|---|---|---|---|---|
| OWL $9.5P × 2 (Jun 05) | 15d | $0.20 | -66% | Rolled from Apr 2 |
| SOFI $16P × 1 (Jun 05) | 15d | $0.80 | +13% | Rolled from May 1 |
| USO $155C × 1 (Jun 12) | 22d | $3.95 | -61% | Rolled from Mar 27 $118C; BRENT-domain |
| KRE Jun 30 cluster ($63P/$65P × 4/$67P) | 40d | varies | -55% to -80% | Will + REGINALD — same disposition question as 6/18 |
| IWM $250P × 1 (Jun 30) | 40d | $1.17 | -85% | Was +63% at Mar 25 |

### Pending review — INBOX

| Item | Filed | Status |
|---|---|---|
| VIOLET VIX/SKEW divergence trade idea | 2026-04-15 | Never adjudicated — 60d window from 4/13 closes ~6/12; decision overdue |
| Silver Squeeze (Twitter, unverified) | 2026-02-19 | Stale; recommend archive without action |

---

## Catalysts

Live catalysts → `PROME/TODAY.md` (stale 5/17) + `CALENDAR.md` (3/27 stale; contains 6/16 FOMC + 6/18 expiry cluster + 5/25 Memorial Day).

---

## Watchlist — Not Yet Entered

| Ticker | Trade | Conviction | Thesis | Wait For | Current status |
|--------|-------|-----------|--------|----------|---|
| **PC single-names** | APO/ARES/ARCC fresh puts | 70% | BROCK catalyst clock | Green day re-entry | ✅ **Resolved 5/21 — BROCK: no fresh entry; entry triggers documented (HY OAS <270 sustained, GCRED/OTF release in 30d, bank PC loss disclosure, sub-90¢ arms-length BDC loan)** |
| **FXY add** | Shares | 60% | Need BOJ hike or oil catalyst | Signal | ✅ **Resolved 5/21 — Tranche 2 executed (5 shares @ $57.66); 13 total. Sep $60C entry still pending post-CPI per SAM** |
| **HYG add** | More puts | 60% | CDX divergence = real stress masked | Next credit widening | ⚠️ **Stale — existing HYG $75P × 8 now -90%, Hamilton roll never executed. BROCK 5/21: no fresh PC premium; would go to BIZD or ARCC if triggers fire** |
| **SOFI thesis** | Research needed | TBD | Consumer pain angle | Investigation | ⚠️ **SOFI Jun 05 $16P × 1 already in book (+13%); deeper thesis work never done** |

---

*Trade history → `JOURNAL.md` | Watchlist → `WATCHLIST.md` | Risk rules → `PROTOCOL.md`*
*Thesis diary → `ACTIVE_TRADES.md` | Will's journal → `WILL/trading-journal`*
