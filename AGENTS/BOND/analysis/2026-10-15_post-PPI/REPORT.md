# BOND — 2026-10-15 (Thu) boot catch-up: CPI-day official close, PPI-day rally, credit, bars

**Session:** Claude Code, Opus 5.5 (claude-opus-5-5), Will-launched, boot 13:49 ET. Capture `capture.py` → `raw/` (manifest in `raw/manifest.json`). Boot receipts: `docket_check` rc=0 (verified only through 10/22, blind span 10/23→11/05 UNVERIFIED) · `boot_recompute` rc=0 · corrections rc=1 → COR-20261014-36 receipted NO-OP · root pull not needed (HEAD == origin/master at boot fetch; foreign dirty WALTER/TERRY paths untouched).

## 1. October 14 (CPI day) — official close confirms the vendor read

| Treasury par, official | 10/13 | 10/14 | Δ bp |
|---|---:|---:|---:|
| 2Y | 4.79 | 4.82 | +3 |
| 5Y | 5.00 | 5.00 | 0 |
| 10Y | 5.21 | 5.19 | −2 |
| 20Y | 5.60 | 5.57 | −3 |
| 30Y | 5.56 | 5.52 | −4 |
| Real 10Y | 2.88 | 2.84 | −4 |
| Real 30Y | 3.28 | 3.24 | −4 |
| 10Y nominal − real | 2.33 | 2.35 | +2 |
| 30Y nominal − real | 2.28 | 2.28 | 0 |
| 2s10s / 5s30s | 42 / 56 | 37 / 52 | −5 / −4 |

[CONF PRIMARY Treasury daily nominal + real CSV, pulled 2026-10-15 13:50 ET]. **Bull flattener:** the front rose on hike pricing, the long end fell on lower real yields. The 10/14 vendor pair (real −2.1 / compensation +1.5) had the direction right; official real move is larger (−4). Nominal − real is a fitted-par subtraction, not a pure expectations measure. Morning TIPS split at the 08:30 print itself remains unmeasured.

## 2. October 15 (PPI day) — the rally came BEFORE the print

| Yahoo 5-min (vendor, not close) | 10/14 last | 08:20 first bar | 08:30 bar high | Session low | 13:35 |
|---|---:|---:|---:|---:|---:|
| ^FVX 5Y | 4.992 | 4.894 | 4.928 | 4.835 @09:55 | 4.899 |
| ^TNX 10Y | 5.190 | 5.081 | 5.106 | 5.037 @10:00 | 5.085 |
| ^TYX 30Y | 5.525 | 5.419 | 5.433 | 5.380 @08:40 | 5.421 |
| ^IRX 3M | 4.085 | 4.085 | 4.088 | 4.072 | 4.088 |

- **Timing correction to the fleet framing.** WALTER/PROME carried "10Y rallied −14bp intraday *into* the print / despite hot PPI." On the vendor tape the 10Y was **already −11bp at the first 08:20 bar**, before the 08:30 release; the PPI bar added a **+2.5bp blip** that faded. The bid was set overnight, alongside the Asia equity selloff (SIG-W-20261015-002: KOSPI −8% circuit breaker, Nikkei −4%; **X-feed level, not verified at exchange primaries**). Yahoo has no pre-08:20 bars, so the overnight path itself is unobserved.
- **Shape:** roughly parallel −10bp 5Y/10Y/30Y; 3M bill flat. 5s30s ≈ 52bp, unchanged.
- **Policy path explains a minority of it.** CBOT fed-funds strip (evolving vendor bars, 13:49 ET): Nov 3.950 = +7.0bp vs EFFR 3.88 ≈ **28% of a 25bp hike on 10/28** (BOND's 10/14 13:58 read: 36%); 2027 contracts −3 to −6bp on the day; peak 4.650 Oct-2027. ORACLE companion (PROME packet 10/15): October hike Polymarket 31.5 (Gamma) / Kalshi 29.0 at 12:39Z. Contracts moved 3–6bp while the 10Y moved ~10bp, so most of the move sits outside the policy-path leg (term premium / haven demand). ACM 10Y TP 0.8086 [10/14], −4.3bp d/d, −13.8bp over 5 obs; KW 1.0729 [10/9]. Different models and windows: this is consistent with term-premium compression, **not a causal decomposition**.
- **PPI itself (relayed, not re-read — BLS returned 403 to BOND's fetch):** final demand +1.3% m/m, +6.3% y/y; core ex food/energy/trade +0.5% m/m, +5.0% y/y; gasoline +20.3% m/m [PROME BLS read via SIG-W-20261015-003].
- **Thesis read:** on a hot-inflation, risk-off day, long Treasuries were **bought as a haven**. That cuts against a sovereign-credibility / demand-hole reading *today*: the long end is expensive, but it still works as the safe asset. Supports "expensive, not broken."

## 3. Credit (FRED ICE BofA, 10/14 cells)

| OAS bp | 10/13 | 10/14 | Δ |
|---|---:|---:|---:|
| HY | 316 | 325 | +9 |
| CCC | 1267 | 1282 | +15 (window high) |
| B | 317 | 329 | +12 |
| BB | 191 | 199 | +8 |
| BBB | 103 | 104 | +1 |
| IG | 83 | 84 | +1 |

HY is 25bp below the 350 issuance-freeze line; first cell over the >320 bar (RED-FT-02 / REG-T-03 count 1 of 3 — RED/REGINALD own those). IG/BBB essentially flat, so stress is still concentrated in the weak tail plus an AI-infrastructure single-name cohort (CRWV 2032 YTW 15.83% at HYG fund evaluation, SIG-W-20261015-005, LIQUID's lane). 10/15 vendor tape: HYG +0.4%, LQD +0.8%, VIX 16.7. BOND matrix row 4 stays 3.

## 4. Funding (NY Fed, 10/14)

SOFR 3.88% (volume $2,974B, 99th percentile 3.97), TGCR/BGCR 3.86, EFFR 3.88; IORB 3.90 → SOFR−IORB −2bp, 99th pct +7bp. No repo stress on CPI day. LIQUID owns the verdict; individual fund cash needs remain unmeasured.

## 5. Other duties

| Item | Result |
|---|---|
| PMMS 10/15 | 30Y 7.40% (unch), 15Y 6.71; minus Treasury 10Y 5.19 [10/14] = 221bp, inside 180–230 (VX-BND-17 spread leg not fired) |
| Bund 10Y (Bundesbank fitted) | 3.45% [10/15], −12bp vs 3.57 [10/8] → WQ400 disorderly branch NOT MET (5th prospective evaluation) |
| 30Y ≥5.00 (Treasury basis) | 86 of 197 2026 sessions; trailing run 70 through 10/14 |
| Real 10Y ≥2.50 (Treasury basis) | 2.84 [10/14], 34bp through; trailing run 24 in the 2026 file |
| 20Y-R 912810UX4 bars (10/21, $13B) | frozen: I' indirect < **57.96%**; old conjunctive indirect<52.47 AND dealer>17.59; cover BTC<2.36 (`bars_912810UX4.txt`) |
| 5Y TIPS 91282CRR4 bars (10/22, $26B) | frozen: indirect<51.43 AND dealer>25.42; cover BTC<2.10; no I' for TIPS (`bars_91282CRR4.txt`) |
| F2 buyback op 10Y–20Y (cap $6.0B) | OFF-THE-RUN, 0.33% recent share — §6 |
| FR2004 as-of 10/7 | publishes ~16:15 ET — not yet read |

Tool note: the first `grade_auction.py` run used system python and printed **"I' NOT COMPUTED — not a pass"** (numpy missing). It failed loud as designed; the re-run in `.venv` produced the governing bar. Run it from the venv.

## 6. F2 buyback op (10Y–20Y, 2026-10-15)

Published 14:08 ET. **OFF-THE-RUN** — recent-issue share 0.33% vs the >50% on-the-run cut. Cap $6.0B fully filled ($6.000B accepted of $40.836B offered, 6.81x), 3 of 42 eligible CUSIPs accepted; **93.00% into 912810TC2 (2.00% Nov-2041)**, 6.67% 912810TH1 (3.25% May-2042), 0.33% 912810UL0 (5.00% May-2045). Detail rows sum to the ops row. Five in-scope stepped-up ops, five OFF-THE-RUN: Treasury is retiring deep-discount legacy paper, not supporting the benchmark. Read routed to RED (`AGENTS/RED/inbox/2026-10-15_from-BOND_F2-2026-10-15-10-20Y-off-the-run-read.md`, commit cbf40ee2b); ledger row `registry/f2_reads.tsv`. Cut is BOND-declared, not Will-ruled; a fire would be a marker, never a YCC-lite verdict.

## Gaps

Official 10/15 close (tonight) · FRED 10/15 HY cell (10/16 AM, decides the >320 count) · FR2004 10/7 as-of (16:15 ET) · Asia figures unverified at exchange primaries (HENRY/ZHAO lanes) · Kansas bank failure (SIG-W-20261015-013) is REGINALD's; BOND's FHLB lane has no read on it.
