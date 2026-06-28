# FORGE Rehab Reconciliation — 2026-05-21

**Built by:** Claude Code Prome (CC), Will-authorized
**Purpose:** Ground-truth reconciliation table for FORGE STATUS.md rebuild. Maps every Fidelity CSV line → thesis bucket → agent owner.
**Source 1:** `AGENTS/RED/inbox/processed/Portfolio_Positions_May-21-2026.csv` — Fidelity export, account 216461326 Traditional IRA, downloaded 2026-05-21 2:03 PM ET
**Source 2:** `AGENTS/SAM/TRADE.md` v1.4 — for FXY position validation (one discrepancy flagged)
**Status:** DRAFT — Will-review checkpoint before Step 2 (STATUS.md rebuild)

---

## Discrepancies / Open questions for Will

| # | Item | CSV says | Other source says | Action needed |
|---|---|---|---|---|
| 1 | **FXY Jun-18 $58C × 1** | NOT IN CSV (no call line; pending -$288.28 matches Tranche 2 shares only, not shares + call) | SAM `TRADE.md` v1.4: "1 × June 18 2026 $58 call @ $0.40 premium ($40 total cost). Executed May 21 pre-CPI." | **Confirm:** call in a separate account / executed post-2:03 PM / didn't fill / SAM error? Reconciliation depends on this. |
| 2 | **AAPL trim** | 30 shares @ avg $23.64 cost | Mar 25 STATUS: 80 shares @ $23.84 | 50 shares trimmed between Mar 25 and May 21. Date/proceeds unknown — flag as JOURNAL gap, no P&L reconstruction. |
| 3 | **18 equity closures** | Not present | Mar 25 STATUS / Feb 19 PORTFOLIO list these as held: SLV, SLVP, USO sh, GOOG, OKLO, PALL, GLD, GDX, PPLT, CPER, PLTR, RKLB, XAR, ITA, AMH, INVH, CEPT, UMAC | All closed Mar 25 → May 21. JOURNAL gap. |
| 4 | **APD new long** | 2 shares @ $294.79 cost | Not in any FORGE doc | New position, thesis unknown — leave Notes blank, flag for Will to tag. |
| 5 | **~12 new option opens** | Present in CSV | Not in Mar 25 STATUS | See "NEW since Mar 25" tag in recon table below. No documented entry thesis for most. |

---

## Cash + Equities

| Symbol | Description | Qty | Avg cost | Last | Current value | P&L % | Thesis bucket | Agent owner | Notes |
|---|---|---|---|---|---|---|---|---|---|
| SPAXX | Money market | — | — | $1.00 | **$25,138.80** | — | Cash | — | 55.17% of account; heavy cash posture |
| *(Pending activity)* | Tranche 2 FXY settling | — | — | — | **-$288.28** | — | Cash | SAM | Matches Tranche 2: 5 × $57.66 = $288.30 |
| AAPL | Apple Inc | 30 | $23.64 | $305.03 | $9,150.90 | +1190.07% | Longs | non-thesis | **Trimmed 80→30 Mar 25→May 21** (JOURNAL gap) |
| TBT | ProShares Ultrashort 20+ Yr | 14 | $34.63 | $37.025 | $518.35 | +6.91% | Longs | HENRY/duration short-side | Unchanged from Mar 25 |
| FXY | Invesco Yen ETF | 13 | $58.32 | $57.785 | $751.20 | -0.93% | Longs | SAM | T1 (8 @ $57.36) + T2 (5 @ $57.66, executed 5/21); SAM v1.4 reports $57.48 blended on $747.18 entry — minor drift, likely Fidelity blended-cost convention |
| APD | Air Products and Chemicals | 2 | $294.79 | $289.125 | $578.25 | -1.93% | Longs | **unassigned** | **NEW since Mar 25**, no FORGE thesis doc, Will to tag |

---

## Options — Thesis Puts

### KRE (regional banks — REGINALD)

| Strike-Expiry | Qty | Avg cost | Last | Value | P&L % | Notes |
|---|---|---|---|---|---|---|
| Dec 18 2026 $60P | 7 | **$2.72 wt avg** | $2.24 | $1,568 | -16.1% | **Merged: 4 cash @ $2.57 + 3 margin @ $2.93** |
| Sep 30 2026 $60P | 2 | $2.27 | $1.49 | $298 | -34.27% | Unchanged from Mar 25 |
| Aug 21 2026 $60P | 3 | $2.70 | $0.97 | $291 | -64.04% | **NEW since Mar 25** |
| Jun 30 2026 $67P | 1 | $3.26 | $1.47 | $147 | -54.87% | Deep OTM at KRE $69.21 |
| Jun 30 2026 $65P | 4 | $2.81 | $0.94 | $376 | -66.57% | Deep OTM |
| Jun 30 2026 $63P | 1 | $2.79 | $0.57 | $57 | -79.55% | Deep OTM |
| Jun 18 2026 $60P | 1 | $2.66 | $0.16 | $16 | -93.98% | **🔴 THETA-KILLER, 28d to expiry** |

KRE total: 19 contracts · ~$2,753 market value · weighted P&L roughly -45%

### WAL (single-name bank — REGINALD)

| Strike-Expiry | Qty | Avg cost | Last | Value | P&L % | Notes |
|---|---|---|---|---|---|---|
| Jun 18 2026 $85P | 1 | $5.91 | $7.00 | $700 | +18.50% | Still in the money at WAL $78.53 |
| Jun 18 2026 $77.5P | 1 | $5.51 | $2.55 | $255 | -53.70% | |
| Jun 18 2026 $67.5P | 2 | $4.91 | $0.40 | $80 | -91.85% | **🔴 THETA-KILLER, 28d** |
| Jun 18 2026 $65P | 1 | $4.50 | $0.25 | $25 | -94.45% | **🔴 THETA-KILLER, 28d** |
| Sep 18 2026 $70P | 1 | $7.69 | $3.30 | $330 | -57.07% | |
| Sep 18 2026 $67.5P | 1 | $7.51 | $2.70 | $270 | -64.04% | |
| Jul 17 2026 $65P | 1 | $4.36 | $0.85 | $85 | -80.49% | **NEW since Mar 25** |

WAL total: 8 contracts · $1,745 market value · weighted P&L roughly -50%

### TLT (duration / Treasuries — HENRY / BOND)

| Strike-Expiry | Qty | Avg cost | Last | Value | P&L % | Notes |
|---|---|---|---|---|---|---|
| Jun 18 2026 $85P | 3 | $0.82 | $1.57 | $471 | +92.22% | Strong; consider roll-out |
| Sep 30 2026 $85P | 2 | $2.52 | $2.94 | $588 | +16.81% | |
| Oct 16 2026 $82P | 2 | $1.68 | $1.79 | $358 | +6.75% | |

TLT total: 7 contracts · $1,417 market value · weighted P&L roughly +35%
*(May 15 $88P × 2 from Mar 25 STATUS expired/closed — was +99% at Mar 25, decision was "pending Will" — needs JOURNAL note)*

### APO (alt-mgr / private credit — BROCK)

| Strike-Expiry | Qty | Avg cost | Last | Value | P&L % | Notes |
|---|---|---|---|---|---|---|
| Dec 18 2026 $95P | 1 | $11.85 | $2.75 | $275 | -76.79% | BROCK 5/21: **hold** (thesis vehicle) |
| Jun 18 2026 $100P | 1 | $7.71 | $0.10 | $10 | -98.71% | **🔴 THETA-KILLER**; BROCK 5/21: **let expire** |

APO total: 2 contracts · $285 market value · weighted P&L roughly -88%
*(Apr 17 $100P from Mar 25 STATUS expired worthless — JOURNAL gap)*

### OZK (single-name bank — REGINALD)

| Strike-Expiry | Qty | Avg cost | Last | Value | P&L % | Notes |
|---|---|---|---|---|---|---|
| Aug 21 2026 $45P | 4 | $3.69 | $1.50 | $600 | -59.32% | |
| Aug 21 2026 $42.5P | 1 | $2.12 | $0.90 | $90 | -57.49% | |
| Jul 17 2026 $42.5P | 2 | $1.02 | $0.50 | $100 | -50.83% | **NEW since Mar 25**, likely roll from May 15 $42.5P (-31.88% at Mar 25) |

OZK total: 7 contracts · $790 market value · weighted P&L roughly -57%

---

## Options — Other Puts

### Regional banks (REGINALD)

| Symbol Strike-Expiry | Qty | Avg cost | Last | Value | P&L % | Notes |
|---|---|---|---|---|---|---|
| HBAN Oct 16 2026 $16P | 4 | $0.96 | $1.10 | $440 | +14.97% | **NEW since Mar 25** |
| FITB Jun 18 2026 $45P | 2 | $0.91 | $0.35 | $70 | -61.41% | **NEW since Mar 25** |
| ZION Jul 17 2026 $57.5P | 1 | $4.01 | $1.20 | $120 | -70.06% | Unchanged from Mar 25 |
| FLG Jul 17 2026 $13P | 3 | $0.95 | $0.35 | $105 | -63.29% | Unchanged |
| EGBN Jun 18 2026 $25P | 1 (margin) | $1.57 | $0.20 | $20 | -87.24% | **🔴 THETA-KILLER, 28d** |

### Credit / Private credit (BROCK)

| Symbol Strike-Expiry | Qty | Avg cost | Last | Value | P&L % | Notes |
|---|---|---|---|---|---|---|
| HYG Jun 18 2026 $75P | 8 | $0.31 | $0.03 | $24 | -90.22% | **🔴 THETA-KILLER, 28d** — Hamilton roll Jun→Dec never executed (BROCK LESSONS #16, execution-rails gap) |
| ARES Jun 18 2026 $95P | 1 | $8.03 | $0.40 | $40 | -95.02% | **🔴 THETA-KILLER, 28d**; BROCK 5/21: **let expire** |
| OWL Jun 05 2026 $9.5P | 2 | $0.59 | $0.20 | $40 | -65.92% | **NEW since Mar 25**, rolled from Apr 2 $9.5P |

### Consumer / Other (mostly unassigned)

| Symbol Strike-Expiry | Qty | Avg cost | Last | Value | P&L % | Agent owner | Notes |
|---|---|---|---|---|---|---|---|
| AAL Jun 18 2026 $10P | 2 | $0.90 | $0.05 | $10 | -94.43% | unassigned | **🔴 THETA-KILLER, 28d** |
| AAL Jul 17 2026 $10P | 1 | $0.57 | $0.14 | $14 | -75.30% | unassigned | |
| CCL Jul 17 2026 $25P | 2 | $1.96 | $1.62 | $324 | -17.21% | unassigned | **NEW since Mar 25** |
| DIS Jul 17 2026 $90P | 2 | $1.99 | $0.44 | $88 | -77.86% | unassigned | **NEW since Mar 25** |
| SOFI Jun 05 2026 $16P | 1 | $0.71 | $0.80 | $80 | +13.20% | unassigned (CARL-adjacent) | **NEW since Mar 25**, rolled from May 1 $16P |
| KELYA Aug 21 2026 $7.5P | 1 | $0.76 | $0.75 | $75 | -0.89% | LABOR-adjacent | Unchanged |

### Index (HENRY)

| Symbol Strike-Expiry | Qty | Avg cost | Last | Value | P&L % | Notes |
|---|---|---|---|---|---|---|
| IWM Jun 30 2026 $250P | 1 | $7.69 | $1.17 | $117 | -84.78% | Down from +63% at Mar 25 |
| IWM Jun 18 2026 $257P | 1 | $9.39 | $1.16 | $116 | -87.65% | **NEW since Mar 25** |
| QQQ May 21 2026 $698P | 1 | $3.82 | $0.01 | $1 | -99.74% | **🔴 EXPIRES TODAY — let expire** |

---

## Options — Calls / Longs

| Symbol Strike-Expiry | Qty | Avg cost | Last | Value | P&L % | Thesis bucket | Agent owner | Notes |
|---|---|---|---|---|---|---|---|---|
| USO Jun 12 2026 $155C | 1 | $10.08 | $3.95 | $395 | -60.81% | Oil | BRENT | **NEW since Mar 25**, rolled from Mar 27 $118C (-89% at Mar 25) |
| XLE Sep 30 2026 $65C | 2 | $2.28 | $1.59 | $318 | -30.17% | Oil/Energy | BRENT | **NEW since Mar 25** |
| CF Jun 18 2026 $130C | 1 | $11.67 | $3.30 | $330 | -71.72% | Ag/Fertilizer | unassigned | Unchanged from Mar 25; thesis doc `FORGE/CF-trade-thesis.md` (Mar 17) |
| **FXY Jun 18 2026 $58C** | **1** | **$0.40** | — | **$40 cost** | — | **Japan** | **SAM** | **⚠️ NOT IN CSV** — per SAM v1.4 only; reconciliation pending |

---

## Position rollup by thesis bucket

| Bucket | Contracts/shares | Market value | Agent owner |
|---|---|---|---|
| Cash (SPAXX) | — | $25,138.80 | — |
| AAPL long | 30 sh | $9,150.90 | non-thesis |
| TBT long | 14 sh | $518.35 | HENRY |
| FXY long | 13 sh (+1C?) | $751.20 (+$40?) | SAM |
| APD long | 2 sh | $578.25 | unassigned |
| KRE puts | 19 contracts | ~$2,753 | REGINALD |
| WAL puts | 8 contracts | ~$1,745 | REGINALD |
| TLT puts | 7 contracts | ~$1,417 | HENRY/BOND |
| APO puts | 2 contracts | ~$285 | BROCK |
| OZK puts | 7 contracts | ~$790 | REGINALD |
| Regional bank puts (HBAN/FITB/ZION/FLG/EGBN) | 11 contracts | ~$755 | REGINALD |
| Credit puts (HYG/ARES/OWL) | 11 contracts | ~$104 | BROCK |
| Consumer puts (AAL/CCL/DIS/SOFI/KELYA) | 9 contracts | ~$591 | mostly unassigned |
| Index puts (IWM/QQQ) | 3 contracts | ~$234 | HENRY |
| Calls (USO/XLE/CF/FXY?) | 5 contracts | ~$1,083 | BRENT / unassigned / SAM |
| **Pending activity** | — | **-$288.28** | SAM |

**Computed approximate account total:** ~$45,400 (cash $25,138 + equities $10,998 + options ~$9,535 + pending -$288). Mar 25 STATUS reported $52,007 — ~$6,600 decline driven by options book bleed + AAPL trim proceeds going to cash.

*Note: this rollup is for sanity-check only. Use live broker for canonical totals.*

---

## What's missing / needs Will input before Step 2

1. **FXY Jun-18 $58C reconciliation** (discrepancy #1 above) — single biggest blocker. Without confirmation, STATUS can either (a) include the call with "per SAM v1.4 — not in 5/21 2:03 PM CSV" footnote, (b) exclude entirely. My default: include with footnote, flag for next CSV refresh.
2. **APD thesis tag** (discrepancy #4) — leave as "unassigned" or assign? Doesn't block Step 2.
3. **Consumer puts (AAL/CCL/DIS/SOFI) thesis owner** — currently "unassigned." CARL would be the historical owner (do-not-spawn). My default: leave as unassigned, flag in Notes.

Other:
- TLT May 15 $88P × 2 from Mar 25 was +99% with "sell decision pending Will" — closed/expired between then and now. JOURNAL gap, no P&L reconstructable.
- OZK May 15 $42.5P × 2 from Mar 25 (-31.88%) → likely closed at expiry, rolled to new Jul 17 $42.5P × 2. JOURNAL gap.
- KRE Jun 18 $60P trimmed 2→1 contract since Mar 25 (or one was closed at a different price). JOURNAL gap.
- SOFI/OWL replacements as documented = roll pattern, but no entry-thesis doc.

---

## Reconciliation provenance

- CSV: `AGENTS/RED/inbox/processed/Portfolio_Positions_May-21-2026.csv` (Fidelity export, downloaded 2026-05-21 2:03 PM ET, account 216461326 Traditional IRA)
- SAM TRADE.md: `AGENTS/SAM/TRADE.md` v1.4 (refreshed 2026-05-21)
- BROCK decisions: `AGENTS/BROCK/domain/sources/POSITION_DECISIONS_MAY21.md` (used for APO + ARES + HYG dispositions)
- Prior STATUS: `FORGE/STATUS.md` (Mar 25) — referenced for "unchanged" vs "NEW" classification
- Prior PORTFOLIO: `FORGE/PORTFOLIO.md` (Feb 19) — referenced for equity-closure list

**Not consulted (out of scope for Step 1):** REGINALD per-trade docs, HENRY STATUS, BRENT STATUS — would refine thesis-bucket tagging but not change position-state. Will-decide if worth pulling in for Step 2.
