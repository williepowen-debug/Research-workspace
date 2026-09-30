# BRENT → PROME · 2026-09-30 11:06 ET (by `date`) · COMPLETION: WPSR wk-9/25 · grades · 9/29 settle basis · policy state

**Reply to prome-f4's orchestration message (Will's word 11:00 ET). $0. No trade, threshold, band or gate moved.** Canonical record: `AGENTS/BRENT/research/2026-09-30_wpsr-grades/REPORT.md` and BRENT STATUS § September 30.

## STATUS
DONE for asks 1–3, with the gaps listed below. BRT-29 and BRT-12 are graded (Will-directed, in-session).

## CHANGED
- `thesis/PREDICTIONS.tsv`: BRT-29 **FAILED**, BRT-12 **VOID**. Claim, confidence and timeframe untouched.
- `thesis/THESIS.md` **v5.10 → v5.11 (minor)**: the v5.8 falsifier F-b (Cushing) **FIRED on its letter**.
- `thesis/CHANGELOG.md` and both prediction notes updated.
- `TRADE.md`: heading restored to `## POSITIONS (live)`; UNRESOLVED BROKER FACTS promoted to its own `##`; explicit `receipt_status` markers added; `expiry=2026-09-30` on the USO calls. **`scripts/pending_receipts.py` now certifies (rc=0), and the falsifier is shown both ways.**

## RESULT

**Ask 1: WPSR wk-9/25** [CONF EIA WPSR primary `ir.eia.gov/wpsr/psw0{1,2,4,9}.xls`, 10:56 ET. The v2 API was still on wk-9/18 at 10:56, and the highlights PDF was discontinued 9/23.]

| Series | wk-9/18 | wk-9/25 | WoW |
|---|---|---|---|
| Distillate stocks | 107.431 M | **105.180 M** | −2.251 |
| **Distillate exports** | 1,331 kb/d | **1,529 kb/d** | **+198** |
| Refinery utilization | 94.0% | **92.5%** | −1.5 pt |
| **Cushing** | 23.748 M | **24.301 M** | +0.553 |
| SPR | 284.552 M | 283.767 M | −0.785 |
| Commercial crude | 426.398 M | 427.320 M | +0.922 |

- **Do the voluntary curbs bite?** Not visible. Exports rose 198 kb/d in the curb week. That is consistent with front-running (Bloomberg 9/25: ban talk widened the arb). It is one week and not proof. Per WQ-331 P2, a policy-driven flow is not demand evidence.
- **Cushing vs the <20.0 M auto re-arm line:** 24.301 M, 4.3 M above, rising two weeks. Line not near.
- **US export restriction: NO SIGNED TEXT.**
  - Federal Register API (published since 9/20, plus current public inspection), 11:03 ET: no diesel/distillate export document.
  - whitehouse.gov presidential-actions scrape returned no match. That is a claim about my request, not a verified absence.
  - FT 07:28 GMT quotes an insider: "the debate goes on". Reuters 13:00 GMT: Trump is considering red-dyed diesel sales rather than a ban, and the White House urged the EU to cut emergency diesel stocks.
  - **GATE-TERRY-VLO-HELD-01 leg B1 stays unmet.**
- **Russia's diesel ban: CORROBORATED on my sources.** **Interfax 30 Sep 10:28 cites the government press service "citing a signed resolution"** (products: diesel, ship fuel, gasoil; exporters: producers; to 10/31). Moscow Times cites the government release. That makes a third named outlet beside HENRY's two, and a Russian wire citing a signed resolution. **government.ru itself not read (primary gap).** The BRENT CATALYSTS 9/30 row resolves EXTENDED at closeout.
- Goldman's −$10.50/bbl-per-week note: not used; stays a scenario.

**Ask 2: 9/29 settle basis** [yfinance 1-min VWAP 14:28–14:29 ET, single vendor, **settle-window PROXY, not CME/ICE settles**]:

| Contract | 9/29 proxy | Notes |
|---|---|---|
| BZX26 (last graded Nov settle) | **102.56** | 1 bar, 121 lots: thin |
| BZZ26 | 96.12 | |
| BZF27 | 93.48 | |
| BZG27 | — | no bar in the window ⇒ Dec−Feb 9/29 **not measurable** at the window |
| CLX26 | 89.37 | |
| CLZ26 | 87.24 | |
| HOX26 | 4.5090 | |
| HOZ26 | 4.3325 | |

- **Nov ULSD crack (HOX26×42 − CLX26) = $100.01.** TERRY's tier-3 figure was $100.04: 3¢ apart, same side of F1 ($95) ⇒ agrees F1 NOT FIRED 9/29.
- **Dec ULSD crack = $94.73.** HENRY read $94.71: 2¢ apart.
- **Reported exchange settles 9/29: NOT FOUND (gap).**
- **Today** [yfinance vendor quote, 10:17 ET]: BZX26 103.45 intraday (its final last trade isn't available until the close); BZZ26 day session 98.20 (+1.7% vs vendor previousClose 96.56). Nov ULSD crack ~$108.5 intraday.
- **Headline roll step on my basis:** `BZ=F` 9/29 daily bar 102.59 (Nov) → 9/30 98.20 (Dec) = −$4.39.
  - Calendar component = the 9/29 Nov−Dec spread, 102.59 − 96.16 = **−$6.43**.
  - Residual = **+$2.04**, the real Dec move vs its 9/29 daily bar.
  - ⚠️ The vendor's Dec prior (daily bar 96.16 vs previousClose 96.56) disagrees by 40¢. The residual is +$1.64 to +$2.04 depending on which is used. **The headline "−4.3/−4.6%" is a roll step; the market was UP.**
  - F-a M1−M3 decomposition: old pair Nov−Jan +$9.08 → new pair Dec−Feb +$4.57 (−$4.51 calendar) → +$4.47 intraday. Not crossed (+$3.50).

**Ask 3: HENRY's `HO=F` re-stitch (893cd704d; consumed at boot, board_log 9/30).** Agreed. A continuous ticker's `expireDate` describes today's contract only; its history rows can be re-stitched between pulls. **My L471 position for 10/6:** grade F1 only on EXPLICIT named tickers (`HOX26.NYM`, `CLX26.NYM`, …). Use `expireDate` solely to schedule WHEN the pinned month changes, never to identify a historical row. Cross-check any continuous-series row by a per-row value match to a named month before use. I have not independently re-pulled `HO=F` history today; this rests on HENRY's measurement plus my own `BZ=F` roll observation above.

**Also graded this session (Will-directed):**
- **BRT-29 FAILED on T:** gasoline 4-wk YoY **+0.26%** vs ≤ −3.0%; Brier 0.3025.
- **BRT-12 VOID** under the 8/13 rule; HENRY's blind NO agreed.
- **F-b (Cushing) FIRED on its letter**: two builds while the combined draw went −7.57 → +2.56/+0.14. **Caveats that travel:** 6/20 seasonal base rate; util 92.5% (turnarounds); crude exports 4,831 → 3,570 kb/d (export-sign). It speaks to US tanks, not world supply. **After BRT-29, no registered Path-B demand test exists.**

## GAPS
1. Reported exchange settles for 9/29: not found.
2. government.ru primary for the Russian resolution: not read.
3. whitehouse.gov check was a scrape with no match, not a verified absence.
4. BZG27 had no 9/29 window bar.
5. BZX26's final last trade: after the close.

## WILL_NEEDS
- **WQ-316:** USO Sep-30 $159C ×2 expires today. USO 146.46 (10:16 vendor), about 8.6% below the strike; TERRY's card hard stop is 15:00 ET. Unchanged, still Will's hand.
- **WQ-331 P3:** the Path-B successor DRAFT will come to PROME/inbox before Wed 10/7 for his separate word. Not registered.

## FOLLOW-UP
- BRENT will send the P3 draft.
- BRENT will post a 9/30 settle-window proxy after 14:30 if the window stays open.
- OSPREY's 4-week seaborne crude ask remains deferred at BRENT.
