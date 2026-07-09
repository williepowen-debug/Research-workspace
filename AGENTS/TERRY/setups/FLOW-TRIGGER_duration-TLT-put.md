# FIRE CARD — TLT — Duration short / TLT puts (deploy-on-trigger)
**Setup ID:** TRY-FIRE-004 · **Trigger class:** FLOW/VELOCITY discriminator (explicitly NOT the bare level)
**Thesis owner:** BOND (BND-11 / VX-BND-05) + LIQUID (demand-hole workbook) + SAM/ZHAO (TIC flow) — routed by PROME 2026-07-06 xdomain synthesis
**Card pre-built:** 2026-07-09 (spec routed to TERRY inbox 2026-07-06 as a PRE-BUILD task, ID-corrected 2026-07-08; the card file itself was not actually written until this session — flagged as a process gap in the outbox note to PROME)
**Fired:** ____ (fill at fire)
**Status:** PROPOSE-ONLY — Will [Approve] required (rule #5). Confidence: **LOW / contingent** — readiness, not a lean (7/6 xdomain synthesis: "demand-hole convergence" graded MIXED-leaning-refuted, one correlated term-premium root, not independent votes).

══════════════════════════════════════════════════════════════
ZONE 1 — PRE-LOCKED (do NOT re-derive at fire)
══════════════════════════════════════════════════════════════
- **Trigger condition (exact):** ARM only on **ANY ONE** of 3 flow/velocity discriminators — **never the bare level** (30Y touching 5.00% alone does not arm this card):
  1. **BND-11 ACUTE at the 7/9 30Y reopen** (BOND grades): indirect (%-of-competitive-accepted) **<52%** AND (**BTC <2.15** OR tail >2bp) AND **dealer >18–20%**. *(BTC threshold reconciled 2026-07-09 per BOND: canonical is <2.15, not the earlier 2.3 — the 2.3 figure was a mis-ported 5Y-auction line.)*
  2. **10Y five consecutive closes ≥4.50** — the 10Y-sustain escalation leg of BOND's **VX-BND-05**. *(ID note: this is NOT "BND-12" — BND-12 is BOND's separate 30Y>5.00-sustain call. Corrected by PROME 2026-07-08, HENRY-flagged.)*
  3. **Soft May TIC 7/16** (ZHAO/LIQUID/SAM): China **AND** Japan UST holdings actually **DOWN** (converts Japan from correlation-amplifier to a real flow-subtractor — PACKET-C flow test).
- **One-line setup:** duration short / TLT puts expressing a rates-channel duration *shock* if a flow/velocity discriminator actually confirms — not a bet on the bare term-premium level poke.
- **Structure:** TLT puts, **Sep expiry** (captures the 7/9→7/16 window plus buffer), strike ladder **8–12% OTM** — confirm exact strikes at fire against live chain.
- **Why this expression:** the 7/9→7/14 CPI downside is asymmetric with near-zero buffer if a duration shock confirms (soft reopen → 10Y gaps through 4.50 → into CPI) — a convex options structure captures that asymmetry better than outright TLT short.
- **Alternatives rejected:** outright TLT short = unbounded + margin; long-dated (2027) puts = wrong tenor for a velocity-window catalyst; arming on the 30Y level alone = the exact mis-read the 7/6 xdomain synthesis warned against (level is one correlated root, not independent confirmation).
- **Max-loss budget:** $500 per card (Will 2026-06-26 standing rule).
- **Invalidation (thesis/price/time):** 30Y retraces **<5.00%** post-auction, OR 10Y mean-reverts **<4.50%**, OR a **clean 7/9 print** (indirect holds ≥58%, no tail) → card lapses unfired.
- **Kill line:** any one DISARM condition above fires.
- **Confirm line:** any ONE arm discriminator fires; CPI 7/14 hot core (MoM ≥+0.3%) is a compound amplifier on an already-armed card, not itself an arm condition (CPI grade owned by HENRY/CARL/LIQUID).

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

**Terry verdict (as of 2026-07-09):** **NO TRADE — NO-ARM.** Card remains PRE-BUILT/SHELVED, 0 fired.
**Decision:** [ ] APPROVE  [ ] REJECT  [x] HOLD — awaiting discriminator

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**
