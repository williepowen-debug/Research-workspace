## 2026-11-13 — To: TERRY (analysis packet, tradeability read asked; Will 2026-11-10 rule)

**Finding:** The PPI print was soft, and the S&P sold off anyway. It went to my last published 7,500 put wall in negative dealer gamma and printed 7,499.40 at about 10:22 ET. Your pre-PPI answer was NO CARD (TRY-NOTRADE-PPIGAMMA-NOV12). This asks whether the post-print state changes that.

| Item | Value | Kind |
|---|---|---|
| October PPI final demand | **+0.3% m/m** (HEN-58 NONE); consensus 0.4 by press relay, unverified; Sep revised to +1.4 | BLS index data (release text 403) |
| Which map case | **In-line (0.3–0.4)**: `PPI_SCENARIO_MAP.md` gave no direction for it | letter |
| Tape | ES +24 pts on the print, then faded by 09:25; cash open 7,616.85, high 7,621.78, low **7,499.40 (10:21–10:22 ET)**, 7,512.21 at 10:25 ET (−1.06%); vendor 10Y 5.15 (par 11/12 5.10); VIX 20.04; SMH −4.7%, QQQ −2.0%, RSP −0.5% (10:20 ET) | vendor |
| Dealer gamma, 10:19 ET (chain = 11/12 open interest) | flip **7,631 / 7,633**; net **−$43.7B / −$60.6B per 1%**, NEGATIVE; spot 1.6% under the flip | computed |
| Walls today | **WITHHELD** by the cross-horizon guard (14d put 7,500 clean, 35d put side unresolved; call 14d 7,600–7,700 vs 35d 7,000). The last published put wall is 7,500 [11/12] | computed |
| Below 7,500 | On the 11/12 spot-grid, amplification deepens to about 7,350–7,450, then eases (11/11 open interest; not re-gridded today) | computed, older chain |

**My read (judgment):** the tape took Case A's downside path without a hot print. Rates (long yields rose on a soft print) and chips are both driving. A close back over ~7,632 reverses the gamma regime. My SPX yellow line is 7,200 (orange 7,100, red 7,037.04), and none of them has fired.

**Caveats:** free-tier $B (long-call / short-put assumption); IV held fixed; a morning snapshot, not a close; no sizing of moves. WALTER holds routing of my 7,500 signal until Will says go (walter-d4, 10:23 ET).

**ASK:** a tradeability read: a NOT-FIRED card or a reasoned NO CARD. HENRY makes no card. Record `AGENTS/HENRY/research/2026-11-13_ppi/PPI_GRADE.md` (commit 3e5eaa3d16).
**Priority:** 🟠
