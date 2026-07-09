# FIRE CARD — TLT — Duration short / TLT puts (deploy-on-trigger)
**Setup ID:** TRY-FIRE-004 · **Trigger class:** FLOW/VELOCITY discriminator (explicitly NOT the bare level)
**Thesis owner:** BOND (BND-11 / VX-BND-05) + LIQUID (demand-hole workbook, now secondary context post-7/9 re-scope) + SAM/ZHAO (TIC flow) — routed by PROME 2026-07-06 xdomain synthesis. **Primary channel re-scoped 2026-07-09 (Will-ratified) to inflation/term-premium (BOND HEN-40 two-channel frame) — see CHANGELOG.**
**Card pre-built:** 2026-07-09 (spec routed to TERRY inbox 2026-07-06 as a PRE-BUILD task, ID-corrected 2026-07-08; the card file itself was not actually written until this session — flagged as a process gap in the outbox note to PROME)
**Fired:** ____ (fill at fire)
**Status:** PROPOSE-ONLY — Will [Approve] required (rule #5). Confidence: **LOW / contingent** — readiness, not a lean (7/6 xdomain synthesis: "demand-hole convergence" graded MIXED-leaning-refuted, one correlated term-premium root, not independent votes).

**CHANGELOG**
- **2026-07-09 PM patch (red-team F5/F6/F9/F10, Will-approved):** card re-scoped, NOT lapsed, despite BOND's 7/9 30Y-reopen grade (indirect 77.74%, no tail — maximally clean) literally reading as a card-global lapse trigger under the old wording. Fix: (1) F5 — invalidations re-scoped per-arm, card-level lapse now requires ALL THREE arms individually dead; arm-#1 formally DEAD as of 7/9, arm-#2/#3 still live; (2) thesis re-scoped from demand-hole to inflation/term-premium channel (BOND's HEN-40 two-channel frame), consistent with the 7/6 synthesis and 7/9 auction read; (3) F6 — added disarm-dominates-arm precedence + arm latch rule; (4) F9 — pinned arm-#2 five-consecutive-close semantics + reset rule + close source; (5) F10 — arm-#3 respecified to valuation-adjusted TIC transactions (not bare holdings-down, which fires on pure valuation with zero selling).

══════════════════════════════════════════════════════════════
ZONE 1 — PRE-LOCKED (do NOT re-derive at fire)
══════════════════════════════════════════════════════════════
- **Trigger condition (exact):** ARM only on **ANY ONE** of 3 flow/velocity discriminators — **never the bare level** (30Y touching 5.00% alone does not arm this card):
  1. **BND-11 ACUTE at the 7/9 30Y reopen** (BOND grades): indirect (%-of-competitive-accepted) **<52%** AND (**BTC <2.15** OR tail >2bp) AND **dealer >18–20%**. *(BTC threshold reconciled 2026-07-09 per BOND: canonical is <2.15, not the earlier 2.3 — the 2.3 figure was a mis-ported 5Y-auction line.)*
  2. **10Y five consecutive closes ≥4.50** — the 10Y-sustain escalation leg of BOND's **VX-BND-05**. *(ID note: this is NOT "BND-12" — BND-12 is BOND's separate 30Y>5.00-sustain call. Corrected by PROME 2026-07-08, HENRY-flagged.)* **Pinned semantics (2026-07-09 PM patch, F9):** five CONSECUTIVE closes ≥4.50; any close <4.50 resets the count to zero. Close source = Treasury CMT / FRED DGS10 daily. (BOND to co-ratify in its Friday packet — VX-BND-05 is BOND's framework; flag any divergence to PROME, do not edit BOND files.) **Current count: 2 entering 7/9** (7/7 close 4.55, 7/8 close 4.57). Today's (7/9) official close not yet confirmed via FRED/CMT at patch time (~15:40 ET) — live intraday read (`^TNX`) was **4.54**, consistent with the ~4.53 intraday level at spawn. If today's close prints ≥4.50, count becomes **3-of-5**; record the confirmed close in the discriminator log at/after 4PM ET, do not count off intraday.
  3. **Soft May TIC 7/16** (ZHAO/LIQUID/SAM): **respecified 2026-07-09 PM patch, F10** — valuation-adjusted flow, not bare holdings-level (holdings-DOWN can fire on pure valuation: yields up → mark-to-market holdings down with zero actual selling, which is not a flow signal). Arm condition: TIC **net TRANSACTIONS** in long-term Treasuries show China **AND** Japan both net **sellers**, comparison month = April 2026 vs May 2026 transactions data (converts Japan from correlation-amplifier to a real flow-subtractor — PACKET-C flow test). **Fallback if transactions-level granularity is unavailable at the 7/16 release:** do not treat bare holdings-down as sufficient to arm; flag the data-granularity gap to PROME and hold arm-#3 as UNDETERMINED pending a transactions-level read, rather than arming on a valuation-contaminated holdings print.
- **One-line setup:** duration short / TLT puts expressing a duration shock via the **inflation/term-premium channel** (BOND's HEN-40 two-channel frame) — **re-scoped 2026-07-09 PM patch, Will-ratified.** BOND's 7/9 30Y-reopen grade refuted the demand-hole channel at the flow level (indirect 77.74%, no tail, foreign demand surged) while confirming term-premium/inflation-driven duration pressure as the live channel. Arm-#2 (10Y five-close sustain) is this channel's natural discriminator; arm-#3 (TIC transactions) tests the flow-subtractor leg as a secondary, not primary, confirmation.
- **Structure:** TLT puts, **Sep expiry** (captures the 7/9→7/16 window plus buffer), strike ladder **8–12% OTM** — confirm exact strikes at fire against live chain.
- **Why this expression:** the 7/9→7/14 CPI downside is asymmetric with near-zero buffer if a duration shock confirms via the term-premium/inflation channel (hot CPI → 10Y sustains/extends through 4.50 → term premium re-prices) — a convex options structure captures that asymmetry better than outright TLT short. *(Re-scoped 2026-07-09: the original "soft reopen → gap through 4.50" framing was demand-hole-flavored; superseded per the thesis re-scope above.)*
- **Alternatives rejected:** outright TLT short = unbounded + margin; long-dated (2027) puts = wrong tenor for a velocity-window catalyst; arming on the 30Y level alone = the exact mis-read the 7/6 xdomain synthesis warned against (level is one correlated root, not independent confirmation).
- **Max-loss budget:** $500 per card (Will 2026-06-26 standing rule).
- **Invalidation — scoped PER-ARM, not card-global (2026-07-09 PM patch, F5):**
  - **Arm-#1 (BND-11 acute) DISARM:** a **clean 7/9 print** (indirect holds ≥58%, no tail) → **arm-#1 DEAD.** *Fired 7/9: indirect 77.74%, dealer 10.05%, BTC 2.44, no tail — arm-#1 confirmed DEAD (see discriminator log).* Arm-#1-adjacent: 30Y retraces **<5.00%** post-auction reads as the same auction-level signal family and also kills arm-#1 if not already dead.
  - **Arm-#2 (VX-BND-05 10Y-sustain) DISARM:** 10Y mean-reverts **<4.50%** — any close <4.50 resets the consecutive-close count to zero (this IS arm-#2's reset mechanism per F9 above, not a separate condition).
  - **Arm-#3 (soft TIC) DISARM:** 7/16 TIC transactions show China and Japan **not** both net sellers (i.e., flat/net-buyer on either leg) → arm-#3 DEAD.
  - **Card-level lapse:** fires ONLY when **ALL THREE arms are individually DEAD.** As of this patch: arm-#1 DEAD, arm-#2 LIVE WATCH (2-of-5, pending 7/9 close), arm-#3 PENDING (7/16). **Card stays ALIVE, re-scoped — not lapsed.**
- **Kill line:** a scoped arm DISARM kills that arm only; the card lapses only when all three arms are dead (see Invalidation above).
- **Precedence + latch (2026-07-09 PM patch, F6):** within a session, a firing DISARM dominates a firing ARM. An arm, once graded ARMED by PROME+Will, LATCHES until its scoped disarm fires — intraday oscillation does not un-arm.
- **Confirm line:** any ONE live arm discriminator fires; CPI 7/14 hot core (MoM ≥+0.3%) is a compound amplifier on an already-armed card, not itself an arm condition (CPI grade owned by HENRY/CARL/LIQUID).

══════════════════════════════════════════════════════════════
DISCRIMINATOR LOG (dated entries — record, don't re-derive ZONE 1)
══════════════════════════════════════════════════════════════

**2026-07-09 ~14:30 ET — NO-ARM (formal).** Source: BOND adjudication ~14:25 ET on BND-11 (2026-07-09 30Y reopen), PROME primary-verified vs TreasuryDirect API.

| Discriminator | State as of 7/9 | Arm threshold | Met? |
|---|---|---|---|
| #1 BND-11 acute (30Y reopen) | Indirect **77.74%**, dealer **10.05%**, BTC **2.44**, high yield **5.058%**. Foreign demand *surged* — inverse of a demand hole. 7th straight benign auction. | indirect <52% AND (BTC<2.15 OR tail>2bp) AND dealer>18–20% | **NO — every leg failed** |
| #2 VX-BND-05 10Y-sustain (5 closes ≥4.50) | 10Y ~4.53 **intraday** 7/9 — not a close yet. 2-of-5 entering today (7/7 4.55, 7/8 ~4.57). | 5 consecutive closes ≥4.50 | **Undetermined — do not count until 4PM ET close.** A ≥4.50 close today makes it 3-of-5. **Live watch, not yet armed.** |
| #3 Soft May TIC (7/16) | Not yet released. | China AND Japan holdings both DOWN | N/A — future date |

**Verdict: arm-#1 formally NO-ARM today (HIGH confidence per BOND).** Channel context: BOND grades the ~5.05% 30Y level as **oil/term-premium channel (orderly)**, NOT a demand-hole — consistent with the 7/6 synthesis's "one correlated root" read. **arm-#2 is now the live duration channel** pending the 7/9 4PM ET close. **Card stays PRE-BUILT/SHELVED — no trade proposal, no sizing.**

**2026-07-09 PM patch note:** per-arm re-read of the above (F5, see ZONE 1 Invalidation) — the clean 7/9 print (indirect 77.74%, no tail) is arm-#1's DISARM, formally confirming **arm-#1 DEAD**, not a card-global lapse. Card-level lapse requires arm-#2 AND arm-#3 also dead, which they are not (arm-#2 LIVE WATCH 2-of-5 pending close; arm-#3 PENDING 7/16). **Card stays ALIVE, re-scoped — PRE-BUILT/SHELVED status is about trade-readiness (no arm yet fired), not about the card being lapsed/dead.**

══════════════════════════════════════════════════════════════
ZONE 2 — LIVE MARKS (fill ONLY at actual fire — rule #4)
══════════════════════════════════════════════════════════════
- **Timestamp (ET):** ____
- **Trigger-level confirm:** [which discriminator fired] — DID IT ACTUALLY HIT? [Y/N]
- **Spot(s):** TLT $____ (from `fetch.py price TLT --json`) — as-of ____
- **Green/red day check (rule #6):** [puts on green ✓ / calls on red ✓ / breaking & why]
- **Chain marks:** `chain_fetch.py TLT <EXPIRY> --type put --no-cache`
  | Strike | Mark | Spread% | IV% | OI | Moneyness% |
  |---|---|---|---|---|---|
  | | | | | | |
- **Liquidity OK?** [Y/N]
- **Broker position truth:** `[POSITION_STATE_UNKNOWN]` until pulled live at fire.
- **Sizing:** `risk_calc.py --premium <mark> --max-loss 500` → ____ contracts

══════════════════════════════════════════════════════════════
ZONE 3 — TRIGGER CONFIRM + DECISION
══════════════════════════════════════════════════════════════
- [ ] A discriminator actually fired (not a near-miss) · [ ] Live marks < 15 min · [ ] Green/red OK
- [ ] Liquidity OK · [ ] Max loss ≤ $500 · [ ] Position truth known

**Terry verdict (as of 2026-07-09 PM patch):** **NO TRADE — NO-ARM.** Card remains PRE-BUILT/SHELVED, 0 fired. Arm-#1 DEAD (confirmed 7/9), arm-#2 LIVE WATCH (2-of-5, pending 7/9 close), arm-#3 PENDING (7/16) — card is ALIVE and re-scoped, NOT lapsed (per-arm invalidation, F5).
**Decision:** [ ] APPROVE  [ ] REJECT  [x] HOLD — awaiting discriminator

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**
