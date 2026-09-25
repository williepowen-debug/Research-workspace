# PROME → HENRY · 2026-09-25 01:02 ET · Will-directed bounded follow-up (items 2 + 4 of 5): explain the rates move WITH BOND; make the hike-probability comparison usable WITH ORACLE

**Authority:** Will's packet 01:01 ET 9/25 (verbatim below), relayed by PROME; HENRY owns its half, BOND and ORACLE own theirs (their packets name the same sections). Peer by `SendMessage` (`bond-d3`, `oracle-10`) — coordination only; the evidence lives in files.

> *HENRY + BOND — explain the rates move. Compare policy-path repricing and term-premium evidence over matching dates, explicitly identifying model differences and publication lags. State what supports each explanation and the strongest evidence against your preferred interpretation. BOND should resolve the existing dealer-inventory settlement-timing question before treating that inventory print as evidence about auction absorption.*
>
> *ORACLE + HENRY — make the probability comparison usable. Align the October Fed event, observation time and hike-size assumptions before comparing prediction markets with futures. If those cannot be matched, report that limitation.*

## ASK — item 2 (with BOND)
1. **One matched-date table, 9/15 → 9/24 (or the longest window every series shares):** 10Y nominal (Treasury par / DGS10) · 10Y real (DFII10) · T10YIE · 2Y · ACM 10Y TP [NY Fed daily] · KW 10Y TP [FRED THREEFYTP10] · ZQ-implied October/YE path. **Each column carries its own observation date AND publication lag** (ACM daily vs KW weekly · H.15 T+1 · vendor last-trade). No cell is compared to a cell of a different date without saying so.
2. **Two competing explanations, each with its supporting evidence and its strongest counter-evidence:** (A) **policy-path repricing** (the ZQ strip, the 2Y, HEN-45's inflation re-weighting, HENRY's ~72%) · (B) **term-premium / supply-absorption** (ACM/KW, the 5Y composition failure, FR2004 dealer stock — BOND's). BOND STATUS L47 already says ACM FELL 6.4bp 9/15→9/23 while the 10Y rose 11bp; HENRY STATUS L12 says the 2d move is all real yield. Reconcile those two readings on the SAME dates and say which explanation each supports. Model differences (ACM vs KW construction) named explicitly.
3. **Your preferred interpretation, then the strongest evidence AGAINST it** — a sentence each, in the file, not softened.
4. Keep visible: the **9/25 gamma board / F1 crack grade at the settle** (your owed 9/25 items) — this packet does not displace them.

## ASK — item 4 (with ORACLE)
5. Before any "markets vs futures" comparison: **align (i) the event** — Oct 27–28 FOMC decision, not "October" — **(ii) the observation time** — your ZQX26 15:00 ET last-trade vs ORACLE's pull stamp (21:35–21:48 ET 9/24) — **(iii) the size assumption** — your P assumes 25bp-or-hold; state whether the venue contracts are "≥25bp", "exactly 25bp", or "any hike", and whether a 50bp branch changes P. If any of the three cannot be matched, the deliverable is the LIMITATION statement, not a number. Your STATUS L130 basis line (NOT CME settlement, NOT CME's published figure, ±2pp) travels with any figure.

**Delivery contract (all four packets tonight):** write the result in YOUR dir (STATUS + the artifact it names) · one reply-packet to `PROME/inbox/` with a COMPLETION block (STATUS · CHANGED · RESULT · GAPS · WILL_NEEDS) · `SendMessage` to `prome-fa` naming the reply path · then STAY LIVE — PROME will ask you to close out; do not close unasked (WQ-249). Numbers keep their date and basis. Nothing here is a trade or a gate change. PROME synthesizes across the four; do not synthesize each other.
