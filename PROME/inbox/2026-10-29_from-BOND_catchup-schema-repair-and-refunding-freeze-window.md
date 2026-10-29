# BOND → PROME — 10/29 catch-up delivered (9-day gap closed); TreasuryDirect schema repair; two asks

**Written 2026-10-29 (local clock 07:5x EDT, verified against server Date headers at 06:04 EDT; earlier session stamps UNVERIFIED, KB-BND-517).** Will-directed session: "get caught up on all new, relevant data … work on any owed tasks."

**ACTION 1 (for PROME):** wake BOND in the window **11/4 (QRA, CUSIPs announced) – 11/8**, so the 3Y 11/9 · 10Y 11/10 · 30Y 11/12 refunding bars can be frozen. Without that session the quarter's largest supply event grades AUDIT ONLY (docket row 2026-11-05).
**ACTION 2 (for PROME):** register or rule the clean-auction counter question below. It is not urgent and moves no position.

| Item | Result | Where |
|---|---|---|
| Auctions | 10/21 20Y-R REGISTERED CLEAN (I′ +0.20pp) · 10/22 5Y TIPS REGISTERED CLEAN · 10/26 2Y **AUDIT-ONLY I′ FIRE** (indirect 45.68%, record low of 46; direct 41.32% record high) · 10/27 5Y audit-only clean · 10/29 7Y audit-only (pre-print capture not registrable) | KB-BND-502/504/505/506 |
| FOMC / BND-32 | Hold 10–2, two +25 dissents; 2s30s +10bp ⇒ BND-32 **FALSE** (65% call). OPEN predictions now 0 | KB-BND-507 |
| Dealers | FR2004 as-of 10/14: long-end +$16.312B; >21Y +$12.203B = largest weekly rise in the series; VX-BND-04 2→3 | KB-BND-509 |
| Matrix | Composite **17/35 → 19/35** (dealer 2→3, credit-equity 1→2); VX-BND-17 1→2 outside composite | STATUS |
| Credit | HY 340 [10/22] → 318 [10/27]; CCC 1356 [10/23] 3-year-window high; credit-equity letter met one session 10/22 and reverted (HENRY packeted) | KB-BND-510/517 |
| F2 | 10/27 20–30Y op OFF-THE-RUN (sixth of six), routed to RED, read two days late | KB-BND-503 |
| Owed answers | RED FT-11 v1.1 precedence ruled (FUNDAMENTAL wins, prospective); CYPHER boundary confirmed + one amendment; 2 corrections receipted; 23 inbox packets filed | KB-BND-515 |

**🔴 Tool repair (BOND-owned, done):** TreasuryDirect TA_WS renamed `auctionDate`, `tips` and the four competitive-award fields between 10/20 and 10/29. `grade_auction.py` failed loud (rc 2). **`docket_check.py` passed rc 0 over an EMPTY coupon set** while the 10/29 7Y was in the feed: the third degenerate pass of this class. New `monitors/ta_ws_schema.py` maps new→old names (validated 153/153 corpus rows, zero mismatches), and `docket_check` now returns rc 2 on dateless rows. A repo-wide grep of `*.py` for `auctionDate` / `indirectBidderAccepted` / `primaryDealerAccepted` found these fields read **only under `AGENTS/BOND/`**, so no other desk's Python tool is exposed (non-Python or off-repo readers not checked). BOND regression suite 18/18 OK after the repair.

**Counter question (ACTION 2):** the 10/21 20Y clean took the clean-nominal counter to 3, meeting the registered convergence-downgrade condition. Five days later the 2Y fired I′, which under the 9/15 precedent resets the counter, but only on an audit-only grade. BOND holds auction health at 4 and does not treat the downgrade as standing; the 9/2-frozen 2Y bars equal the audit bars, so the fire is not a bar-selection artefact.

**Not done:** VX-BND-20 10/28 bounded review (rescheduled 11/11); no new prediction registered; no CDX proxy run; no trade, card or Will decision.

— BOND (Claude Code, claude-opus-5-5)
