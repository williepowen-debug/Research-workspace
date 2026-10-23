# Broker booking — Fidelity IRA activity 2026-10-23 (root rule #10)

**Written:** 2026-10-23 13:26 ET (clock from `date`), TERRY (Claude Opus 5.5, Claude Code), Will-launched session. **Commission:** PROME prome-03 cross-session message 13:2x ET (book per root rule #10; TERRY arithmetic for the USO closes).
**Source:** `PROME/data/2026-10-23_broker-activity-TRANSCRIPTION.md` (PROME transcription of Will's Fidelity "Pending" view screenshot, ~13:2x ET; **uncommitted at read**; TERRY did not view the image). Activity list only, not a positions capture. Fill clocks not displayed. Bases from `FORGE/STATUS.md` (ANVIL reconcile of the 10/22 11:01 ET capture), a mirror, not the broker.
**Basis class:** every realized figure below is **DERIVED** (proceeds − mirror basis), not a broker realized-P/L report. IRA: no tax lot consequence; lot method matters only for which figure is quoted.

## 1. Fills booked

| Line | Fill | Broker amount | Basis removed | Realized (DERIVED) | Qty after (INFERRED, capture owed) |
|---|---|---:|---:|---:|---|
| QQQ Nov-20 690P BTO ×2 | $13.39 | −$2,679.33 | — | open | 2 |
| QQQ Nov-20 670P STO ×2 (same spread order, net limit $4.67) | $8.72 | +$1,742.63 | — | open | −2 |
| QQQ Oct-26 705P BTO ×2 (limit $4.32) | $4.30 | −$861.33 | — | open | 2 (new line) |
| USO 5 shares, sell at market | $168.595 | +$842.96 | $609.49 (avg $121.898/sh = $4,266.43 ÷ 35) | **+$233.47** | 30 sh, basis $3,656.94 |
| USO Oct-30 165C STC ×1 (limit $7.15) | $7.15 | +$714.32 | $270.66 (10/19 lot) / $315.66 (10/20 lot) / $293.16 avg | **+$398.66 to +$443.66** (avg +$421.16) | 1 |
| USO Oct-23 163C STC ×1 (limit $4.27) | $4.36 | +$435.34 | $289.66 (single lot, bought 10/19 @ $2.89) | **+$145.68** | 0 (line closed) |
| AAPL 1 share, sell at market | $346.635 | +$346.64 | $23.645 (avg = $94.58 ÷ 4) | **+$323.00** (+$322.995) | 3 sh, basis $70.935 |

**USO realized today: +$777.81 to +$822.81 (average-cost +$800.31).** The range is the Oct-30 165C lot choice only; the broker's lot assignment is not in the transcription.
**All five closes today: +$1,100.81 to +$1,145.81 (avg +$1,123.31).**
**Not fills:** USO Oct-23 163C STC limit $4.50 = Verified Canceled; QQQ Oct-22 717C STC (10/22) = Verified Canceled; **FLG Mar-19-2027 10P BTO ×4 limit $0.52 = OPEN, unfilled at capture** (Will's own order; not a position, not booked).
**Not reconciled here:** the 10/19 USO 37→35 disposal (FORGE D-84) stays UNKNOWN; this booking starts from the mirror's 35.

## 2. IDEA-QQQ-PUTWALL-OCT22 — fired by Will's hand

| Item | Figure |
|---|---|
| Net debit | $936.70 for 2 spreads = $4.67 × 200 ($934.00) + $2.70 fees |
| Max loss | **$936.70** (closing fees ~$2.60 extra if sold rather than expired) — 1.87× the $500 default; Will's explicit per-card choice |
| Max gain | $4,000 − $936.70 = **$3,063.30** at QQQ ≤ $670 on 11/20 |
| Breakeven at expiry | QQQ **$685.32** |
| Harvest line (card §6) | spread mark ≥ $10.00 on the broker bid ⇒ ~$2,000 proceeds ⇒ ~+$1,063.30 before closing fees |
| Screening mark 13:24 ET | 690P 13.32/13.36 · 670P 8.66/8.70 ⇒ spread mid $4.66, sell-side $4.62 (vendor, not broker — durable finding 5b) |

**Card conditions vs the fill (recorded, not adjudicated against Will):**

| Card condition | State at fill | Met? |
|---|---|---|
| T1: SPX cash close < 7,650 | not graded yet: SPX 7,629.53 intraday (−0.44%) at 13:23 ET; 10/22 close 7,663.43 | **NO — fired AHEAD of T1** |
| Entry on first green QQQ session after T1 | QQQ $705.65 (+0.17%) at 13:23 ET: green | colour MET; sequence not (no T1 yet) |
| T2 gamma NEGATIVE (HENRY latest) | not re-read at entry | UNKNOWN |
| SPX < 7,745 | 7,629.53 | MET |
| Do not chase: net debit > $5.00 | $4.67 | MET |
| Do not chase: QQQ < $685 | $705.65 | MET |
| Size ×1 / $500 default | ×2, $936.70 | Will's choice above the default |
| X1 sizing gate | closed (DON'T-SIZE) | filled against it — Will's choice |

Paper book: `PB-0008` opened `lane=real` at the broker fill, flagged that the paper algorithm would NOT have filled (T1 unfired) — the RULING C divergence signal.

## 3. Combined Nasdaq downside — ONE bet (card §5 book overlap)

| Line | Qty | Basis | Screening bid 13:23–13:24 ET | Value at bid |
|---|---|---:|---:|---:|
| QQQ Oct-26 710P | 1 | $457.66 (10/22) | 7.54 | $754 |
| QQQ Oct-26 705P | 2 | $861.33 (today) | 4.95 | $990 |
| QQQ Nov-20 690/670P spread | 2 | $936.70 (today) | 4.62 | $924 |
| **Total** | | **$2,255.69** | | **≈ $2,668** |

Forward max loss = the remaining value, ≈ **$2,668** at screening bids (construction rule #20 (d)); all three lose on the same event (QQQ holds or rallies). The 710P is held per the 10/22 capture; no disposition appears in today's view, so it is assumed held, not confirmed. **One falsifier: QQQ/SPX recovers (SPX ≥ 7,750 two closes).** The Oct-26 lines and the Nov-20 spread differ only in tenor — the Oct-26 legs carry no card and no management line.
