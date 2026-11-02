# D:L888 — Monday 11/02 pre-open gamma re-pull (successor of L885)

Run: `gamma_flip.py --both --publish` on SPX, QQQ (`--spot 690.49`), NDX (`--spot 28384.85`), 08:48 ET 11/02 (`run_stamp.txt`), before the 09:30 open. HENRY, PROME-spawned (prome-40), Claude Code, Opus 5.5.

## OI vintage — 10/30-trade (OCC Monday post), established at the chain

Cboe delayed-quote payload timestamps: QQQ 2026-11-02 13:37:58 UTC, SPX 13:48:19 UTC (08:37 / 08:48 ET). The `volume` field still carries Friday 10/30's volume (QQQ Nov-20 680P 30,191 = Friday's printed volume), while `open_interest` has moved on contracts that traded Friday — so the OI now includes 10/30 trading. Check script `oi_vintage_check.py`; full put-OI delta table vs the 10/30 ladder (10/29-trade OI) in `oi_delta_1102.txt` (`oi_delta.py`). Raw chain JSONs (17 MB) kept off-repo.

| Contract (put OI) | 10/29-trade (10/30 map) | 10/30-trade (now) | Δ |
|---|---:|---:|---:|
| QQQ Nov-20 680 | 82,664 | 89,505 | +6,841 |
| QQQ Nov-20 670 | 40,772 | 52,149 | +11,377 |
| QQQ Nov-20 700 | 50,278 | 41,161 | −9,117 |
| QQQ Nov-20 690 | 37,143 | 39,216 | +2,073 |
| QQQ Nov-06 680 | 25,801 | 34,980 | +9,179 |
| SPX Nov-06 7550 | 2,885 | 7,330 | +4,445 |
| SPX Nov-06 7400 | 4,896 | 8,009 | +3,113 |
| SPX Nov-20 7500 | 52,934 | 52,181 | −753 |

The 347,333 QQQ 690P volume on Friday was the **10/30-expiry** contract (0DTE); it expired and is out of every map. Friday's Nov-20 put volume is now in OI: net put OI was ADDED at 680/670/660 and CLOSED at 700/710 (strike-down roll shape; opening vs closing by side remains unknown).

## Monday regime (spot = 10/30 close unless noted)

| Chain | Flip 14d / 35d | Net GEX per 1% 14d / 35d | Put wall | Call wall | vs 10/30 map |
|---|---:|---:|---|---|---|
| SPX | ~7,706 / ~7,711 | −$39.4B / −$59.8B | WITHHELD: 14d 7,550 (near-tie band 7,550–7,600) vs 35d 7,500 clean → band **7,500–7,600** | WITHHELD: 14d 7,650 vs 35d 7,700 → band 7,650–7,700 | flip −26 / −25 (was 7,732 / 7,736) |
| QQQ | ~718.2 / ~721.3 | −$2.5B / −$4.6B | **680 PUBLISHED** (clean both: +10% / +40%) | **700 PUBLISHED** (clean both: +42% / +26%) | flip −7 / −6 (was 725.5 / 727.0); call wall was WITHHELD 710 vs 720 |
| NDX | ~28,779 / ~28,913 | −$0.6B / −$1.3B | WITHHELD: 14d 28,500 (band 28,000–28,500) vs 35d 27,500 | WITHHELD: 28,700 vs 29,675 | flip −158 / −134 (was 28,937 / 29,047) |

**Regime: NEGATIVE at both horizons on all three — unchanged from the 10/30 read.** The 7,700 SPX put wall did **not** re-form; the 7,500–7,600 put band did **not** publish clean (the horizons still disagree, now 7,550-ish vs 7,500).

## Distance to the flip (pre-market, vendor 08:48 ET)

| | Friday close | Pre-market | Flip band | Close → flip | Pre-market → flip |
|---|---:|---:|---:|---:|---:|
| SPX (via ES Dec +0.55%) | 7,580.07 | ~7,622 implied | 7,706–7,711 | +1.7% | +1.1–1.2% |
| QQQ (Cboe feed) | 690.49 | 694.63 | 718–721 | +4.0–4.5% | +3.4–3.8% |
| NDX (via NQ Dec +0.92%) | 28,384.85 | ~28,646 implied | 28,779–28,913 | +1.4–1.9% | +0.5–0.9% |

VIX 19.45 (vendor 08:48 ET, +0.15%). Implied index levels are close × futures % change, basis ignored. Free-tier proxy: sign and flip are the robust reads; $B assumption-dependent. QQQ is American-style and only part of Nasdaq-100 gamma — the QQQ (+4%) and NDX (+1.4–1.9%) distances disagree, as they did on 10/30.

Files: `gamma_spx_both_1102pre.txt` · `gamma_qqq_both_1102pre.txt` · `gamma_ndx_both_1102pre.txt` · ledger rows `workbook/PUBLISHED.tsv` dated 2026-11-02.
