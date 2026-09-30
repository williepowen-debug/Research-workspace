# HEARTBEAT dashboard projections

Derived display text, not independent authority. Source: `../HEARTBEAT.md`.
Each amendment requires exactly one numbered projection. Review all affected
one/channel/ticker fields when changing source prose; refresh source_sha256 over
the exact > AMENDMENT paragraph without its trailing newline. Later amendments
win. Missing, malformed or stale projections withhold the dashboard summary and
levels. Hash agreement proves synchronization, not semantic completeness.
At a HEARTBEAT re-base, remove projections for amendments folded into the base.
This companion keeps render metadata outside the boot-read byte budget.

*Twenty-second base 2026-09-25 (post-close) — chain 0: the twenty-first base's amendment #1 was folded into the base at the re-base, so its projection is REMOVED; zero projections stood until amendment #1 (2026-09-26 17:5x ET, PROME, Will-directed correction).*

*Twenty-third base 2026-09-28 (post-close, PROME prome-64) — chain 0: the twenty-second base's amendments #1–#3 were folded into the base at the re-base, so their projections are REMOVED; three projections then accumulated (am.#1 9/28 22:1x · am.#2 9/29 10:5x · am.#3 9/29 15:5x).*

*Twenty-fourth base 2026-09-29 (post-close, PROME prome-f4) — chain 0: the twenty-third base's amendments #1–#3 were folded into the base at the re-base, so their projections are REMOVED; zero projections stood until amendment #1 (2026-09-30 11:1x ET, PROME `prome-f4` midday): projection below. The folded projections are preserved verbatim in the snapshot's commit history (`git log -p -- PROME/HEARTBEAT_DASHBOARD.md`).*

*Amendment #1 (2026-09-30 11:1x ET, PROME `prome-f4` midday; BRENT/TERRY 11:0x deliveries · the Dec pin · WPSR wk-9/25 · the 9/29 credit cells · August PCE · the WQ-316 refresh): projection below.*

```dashboard-amendment
{
  "amendment": 1,
  "source_sha256": "a9034a63ce6b2a891a4fd4599b63f1a86df508277da660beb565dd9802b12789",
  "set": {
    "one": "🔴 THE BOND SELL-OFF's FIFTH DAY STANDS (official 30Y 5.59 · 10Y 5.26 [9/29]); HY 308 / B 316 / CCC 1,157 [9/29] — nearest line HY >320 (12bp), LIQUID grades LIQ-07; BRENT PUBLISHED: 9/29 Nov crack $100.01 PROXY, VLO-SCALE TERMINAL (both staged shares stand down), HELD-01 A/B1 NOT FIRED; the Dec pin is in (a roll step, not a signal); WQ-316 REFRESHED — SELL the QQQ 730P ×9 by 15:00, LET the USO 159C expire; 004 ×15 ARMED; $0 moved by PROME; STAND DOWN holds (WQ-192).",
    "channels": {
      "Energy": {
        "headline": "🟠 Dec pin IN; BRENT 9/29 PROXIES: Nov crack $100.01 / Dec $94.73, BZZ26 96.12; WPSR wk-9/25 exports +198 kb/d (curbs NOT visible), Cushing 24.301M (F-b FIRED on its letter); no signed US export text (B1 UNMET); Russia ban EXTENDED to 10/31",
        "body": "BRENT c4eab03b8 (settle-window proxies, single vendor, exchange settles NOT FOUND): BZX26 102.56 (thin) · BZZ26 96.12 · CLX26 89.37 · HOX26 4.5090; Nov ULSD crack $100.01 (TERRY $100.04). Headline BZ=F −$4.39 = −$6.43 calendar + ~+$2 real (the market was UP, P1). WPSR wk-9/25: distillate exports 1,529 kb/d (+198) · stocks 105.180M · util 92.5% · Cushing 24.301M (+0.553) · SPR 283.767M. Russia's ban extended to 10/31 (Interfax, signed resolution; government.ru unread) ⇒ HEN-F3 NOT FIRED, WQ-344 (10/6). BRT-29 FAILED · BRT-12 VOID. STAND DOWN (WQ-192) holds."
      },
      "Rates": {
        "headline": "🔴 Session 5 stands (official 30Y 5.59 · 10Y 5.26 [9/29]); August PCE core +0.25% MoM / +3.01% YoY (PROME arithmetic, HENRY logs); 004 TLT 77P ×15 ARMED — TLT 77.75 at 11:10, $0.75 above $77",
        "body": "BEA 08:30 (FRED index levels): core PCE +0.25% MoM / +3.01% YoY · headline +0.31% / +3.42% · savings rate 4.1% (July vintage differs from CARL's log) · Q2 GDP 3rd 2.2%; HENRY's 08:04 spawn ran pre-open — doorbelled to log it. 9/29 H.15 cells NOT posted at 11:09. 004: hold ×15 to expiry (WQ-168 ④ / WQ-217), ⛔ NO ADD (WQ-280); TERRY grades after 16:00 (D-60 flag < ~$77.25). FR2004 Thu 10/1 (WQ-291)."
      },
      "Credit": {
        "headline": "🟠 9/29 cells POSTED: HY 308 · B 316 · CCC 1,157 · IG 84 — HY >320 is 12bp, IG >94 is 10bp; B 316 vs LIQ-07's ≥304 leg is LIQUID's grade",
        "body": "FRED 9/29 (posted 9/30): HY OAS 308 (+6) · BB 189 · B 316 (+7) · CCC 1,157 (+11) · IG 84 · BBB 102 · HY yield 8.08. RED-FT-01 EXIT complete (302), X1 CLOSED; nearest lines HY >320 (RED FT-02 / LIQUID send) 12bp · IG >94 (GATE-LIQ-072) 10bp. LIQ-07 leg 2 (B ≥304 on the 9/29 cell) — LIQUID grades, never PROME. GATE-LIQ-069 letter governs (WQ-301 b, 10/02)."
      },
      "Equity-vol": {
        "headline": "🟡 HENRY 9/30 08:1x: gamma NEGATIVE both horizons, flip ~7,693 — SPX 7,711 at 11:02 is ABOVE it, so the read has EXPIRED on its own terms",
        "body": "HENRY 00a94e3e8: negative gamma both horizons with a ~7,693 flip; TERRY used it as input only (item 4) and SPX above the flip retires it. Any current gamma-sign claim needs a fresh HENRY measure (KOS). WQ-316: SELL the QQQ 730P ×9 by 15:00 at the live bid (≈$57 net, ≈4% ITM, removes the −900 QQQ IRA path, D-60); LET the USO 159C ×2 expire (no bid). VIOLET 9/28 WATCH stands."
      }
    },
    "ticker": {
      "Brent": "Brent Dec `BZZ26` 96.12 [9/29 settle-window PROXY, single vendor, BRENT c4eab03b8; exchange settles NOT FOUND]",
      "Dec": "Dec pin IN 9/30 (L461); Nov `BZX26` 102.56 [9/29 proxy, thin]",
      "WTI": "WTI `CLX26` 89.37 [9/29 proxy, BRENT]",
      "F1 crack": "F1 crack Nov $100.01 / Dec $94.73 [9/29 settle-window proxy, BRENT; TERRY $100.04]",
      "**HY OAS": "**HY OAS 308",
      "CCC": "CCC 1,157",
      "IG": "IG 84",
      "BB": "BB 189",
      "B": "B 316",
      "HY yield": "HY yield 8.08% [9/29]**",
      "**Cushing": "**Cushing 24.301M",
      "SPR": "SPR 283.8M [wk-9/25; WPSR 9/30, BRENT]**"
    }
  }
}
```

*Amendment #2 (2026-09-30 17:5x ET, PROME `prome-94` post-close, after the box crash; the four Sep-30 expiries · the 9/29 H.15 cells · August PCE logged · ZHA-16 and OTTO L524 grades · the 9/30 closes · the 25th re-base owed Thu): projection below.*

```dashboard-amendment
{
  "amendment": 2,
  "source_sha256": "b517de546d0a3d42868661e3d8c55c0ee19725459376ff015507d2110757326c",
  "set": {
    "one": "🔴 THE BOND SELL-OFF's FIFTH DAY STANDS (official 30Y 5.59 · 10Y 5.26 · DFII10 2.91 [9/29 H.15, posted]); HY 308 / B 316 / CCC 1,157 [9/29] — nearest line HY >320 (12bp), LIQ-07 leg 2 is LIQUID's grade; THE FOUR SEP-30 LINES EXPIRED OTM (TLT 77.78 · QQQ 739.77 · USO 145.66 · KRE 69.44 [9/30c]) — the QQQ ×9 disposition is WILL's word, PENDING; the duration-short sleeve is one Oct-16 82P (WQ-339 Fri); August PCE core 3.01% y/y logged (mostly revision), October hike odds 36% — the hike case WEAKENED; ZHA-16 MISS, OTTO 9/30 set 1 of 4; Micron printed, VULCAN grades Thu; 25th re-base OWED Thu post-close; $0 moved.",
    "channels": {
      "Rates": {
        "headline": "🔴 Session 5 stands (9/29 H.15 POSTED: DGS30 5.59 · DGS10 5.26 · DFII10 2.91 · DGS2 4.89); the 004 leg EXPIRED OTM (TLT 77.78 [9/30c]); August PCE core 3.01% y/y logged, October hike odds 36% ⇒ the hike case WEAKENED",
        "body": "FRED 9/29 cells by cache-busted CSV (fetch.py fred served 9/24). 9/30: TLT −0.58% · TBT +1.09% · MOVE 110.45 [9/30c, vendor]; HENRY's vendor 10Y 5.29 / 30Y 5.64 — the official 9/30 curve is BOND's (dark). HENRY d3ed5a6d2: core PCE +0.25% m/m / 3.01% y/y · headline +0.31% / 3.42% · saving 4.1% (July 4.6 on the 9/30 vintage — BEA annual update; the y/y 'miss' is mostly revision) · Q2 GDP 3rd 2.2%; ZQX26 close prices October at 36%. 004 TLT 77P ×15 expired OTM (−$173.45; card all lots ≈ −$103.33), HOLD rail discharged, PB-0002b NOT-REACHED; the sleeve is TLT Oct-16 82P ×1; WQ-339 Fri decides a successor."
      },
      "Credit": {
        "headline": "🟠 9/29 cells stand (HY 308 · B 316 · IG 84 · CCC 1,157); HYG 77.21, BDCs red [9/30c]; the 9/30 cells publish Thu; LIQ-07 leg 2 (B ≥304) is LIQUID's grade, not yet logged",
        "body": "FRED 9/29 (posted 9/30): HY OAS 308 (+6) · BB 189 · B 316 (+7) · CCC 1,157 (+11) · IG 84 · BBB 102. Nearest lines HY >320 (RED FT-02 / LIQUID send) 12bp · IG >94 (GATE-LIQ-072) 10bp. 9/30 closes: HYG 77.21 (−0.19%) · BIZD 12.89 · FSK 10.99 · OBDC 10.49 (−2.9%). LIQUID's last commit 9/29 — LIQ-07 leg 2 and the HY-REKILL / LIQ-072 review_by rows (9/30) are its next-touch grades. GATE-LIQ-069 letter governs (WQ-301 b, 10/02)."
      },
      "Equity-vol": {
        "headline": "🟡 WQ-316 SETTLED BY THE TAPE: QQQ 730P ×9 and USO 159C ×2 both expired OTM (QQQ 739.77 · USO 145.66 [9/30c]); whether the QQQ puts were SOLD before 15:00 or held is Will's word, PENDING; VIX 16.34, no gamma read",
        "body": "TERRY ee04fbb26: USO 159C ×2 expired worthless (−$921.33) as recommended; QQQ ×9 OTM by $9.77 — no exercise path, D-60 unobserved; the 15:02 ask to Will died with the box crash. VIX 16.34 (+0.30) · VVIX n/a · MOVE 110.45 [9/30c]; SPY 762.63 (−0.21%) · QQQ 739.77 (+0.25%). Any current gamma-sign claim needs a fresh HENRY measure (not re-measured at the 9/30 close). Micron printed 16:30 — VULCAN's grade Thu (L547)."
      },
      "Energy": {
        "headline": "🟠 Brent Dec `BZZ26` 97.92 (+1.76) [9/30 DAY bar read 17:29 ET, NOT a settle — BRENT dark]; USO 145.66 (+1.61%) · XLE 61.50 · VLO 387.61 [9/30c]; nothing fired; the 9/29 proxies (am.#1) stand",
        "body": "Dec Brent day bar 97.92 read before the 18:00 evening open (L462 class avoided by the clock; still never a settle). BRENT published nothing after 11:2x (settle-window proxies: Nov crack $100.01 / Dec $94.73 [9/29]). VLO-SCALE TERMINAL, HELD-01 A/B1 NOT FIRED (am.#1). USO 37 sh ≈ $5,389 [145.66 × 37, arithmetic]. STAND DOWN (WQ-192) holds."
      }
    },
    "ticker": {
      "Brent": "Brent Dec `BZZ26` 97.92 [9/30 day bar 17:29 ET, NOT a settle; BRENT dark; 9/29 proxy 96.12]",
      "SPY": "SPY 762.63",
      "QQQ": "QQQ 739.77",
      "TLT": "TLT 77.78",
      "GLD": "GLD 380.84",
      "WAL": "WAL 75.10",
      "KRE": "KRE 69.44",
      "OZK": "OZK 45.96",
      "FLG": "FLG 11.67",
      "USO": "USO 145.66",
      "XLE": "XLE 61.50",
      "VLO": "VLO 387.61",
      "TBT": "TBT 42.49",
      "APO": "APO 116.06",
      "HBAN": "HBAN 15.26",
      "AAPL": "AAPL 333.02",
      "APD": "APD 278.23",
      "HYG": "HYG 77.21 [all 9/30c]",
      "**VIX": "**VIX 16.34",
      "MOVE": "MOVE 110.45 [9/30c; vendor]",
      "**DGS10": "**DGS10 5.26",
      "DFII10": "DFII10 2.91",
      "DGS2": "DGS2 4.89",
      "DGS30": "DGS30 5.59 [9/29]**"
    }
  }
}
```
