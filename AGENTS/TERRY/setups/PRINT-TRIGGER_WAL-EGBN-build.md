# FIRE CARD — WAL — single-name puts (fresh deploy, post-print)
**Setup ID:** TRY-FIRE-002 · **Trigger class:** PRINT
**Thesis owner:** REGINALD/CARL + grading instrument (`PROME/synthesis/2026-06-25_Q2-bank-print-grading-instrument.md`) · **Card pre-built:** 2026-06-26 · **Fired:** ____
**Status:** PROPOSE-ONLY — Will [Approve] required (rule #5).

══════════════════════════════════════════════════════════════
ZONE 1 — PRE-LOCKED (do NOT re-derive at fire)
══════════════════════════════════════════════════════════════
- **Trigger condition (exact):** a Q2 bank print **GRADES AS TRANSMISSION** per `grade_print.py`:
  - **WAL Jul-30** path (c) full charge-off: ex-fraud NCO **>55bps** (vs Q1 39bps ADJUSTED — grade adj-vs-adj)
    AND majority of the $99M life-sci credit charged off in-Q2; **OR**
  - **path (a) fires** = **≥2 of {CFG, OZK, EGBN, WAL} SPECIFIC-bucket builds** (collective/macro = beta, non-counting);
    EGBN (Jul 22) is the single most likely + needs a 2nd.
  - GATE: monoline BEAT Jul 21 fades this; monoline BREAK raises build odds. Confirm gate state first.
- **One-line setup:** the print confirmed genuine credit transmission — buy the named bank's downside
  before the multiple re-rates lower.
- **Structure:** **WAL puts** (or EGBN if EGBN is the firing name), **post-print duration**:
  if WAL Jul-30 fires → **Sep-18-26 / Jan-15-27** WAL puts (the live book already holds Sep WAL puts);
  **~8–12% OTM**. For EGBN, nearest liquid expiry past the print.
- **Why this expression:** path (c)/(a) is *single-name credit substance* → single-name put, not ETF.
  Duration must sit PAST the print so the re-rate has room to play out.
- **Alternatives rejected:** KRE/ETF put = dilutes the idiosyncratic signal; pre-print entry =
  gambling the grade (we deploy AFTER the grade confirms, rule: trigger-only).
- **Max-loss budget:** [SET WITH WILL — fresh-capital tranche]
- **Invalidation (thesis/price/time):** grade = RELEASE or COLLECTIVE-only (beta) → no transmission → no trade.
  $99M cures / sponsor returns → WAL path (c) off.
- **Kill line:** classified continues its −9bp trend + H2-decline guide affirmed → thesis defers → exit.
- **Confirm line:** ≥2 SPECIFIC builds (path a fires) OR COF both-segments build (synchronized) → hold / add.

══════════════════════════════════════════════════════════════
ZONE 2 — LIVE MARKS (fill ONLY this at fire — rule #4)
══════════════════════════════════════════════════════════════
- **Timestamp (ET):** ____
- **Trigger-level confirm:** `grade_print.py WAL …` verdict = ____ (BUILD/transmission? specific?) ·
  path-(a) tally ___/2 · gate state (monoline Jul-21) = ____
- **Spot:** WAL $____ (or EGBN $____) as-of ____ · `fetch.py price WAL --json`
- **Green/red day check (rule #6):** WAL today ___% → puts on green ✓ / breaking & why: ____
- **Chain marks:** `chain_fetch.py WAL <EXPIRY> --type put --no-cache`
  | Strike | Mark | Spread% | IV% | OI | Moneyness% |
  |---|---|---|---|---|---|
  | | | | | | |
  ⚠️ WAL Jan-27 puts were ILLIQUID/wide (20% spread, OI 25 per 6/26 proposal) — check flags; Sep may be cleaner.
- **Liquidity OK?** [spread/OI per chain flags — Y/N]
- **Broker position truth:** existing WAL puts (FORGE: Sep 70/67.5 ladder + reshape Sep 75) — net new vs overlap?
- **Sizing:** `risk_calc.py --premium <mark> --max-loss <budget>` → ____ contracts

══════════════════════════════════════════════════════════════
ZONE 3 — TRIGGER CONFIRM + DECISION
══════════════════════════════════════════════════════════════
- [ ] grade_print.py confirms transmission (specific build / full charge-off — NOT collective/release)
- [ ] Gate state checked (monoline Jul-21) · [ ] Live marks < 15 min · [ ] Green/red OK
- [ ] Liquidity OK (esp. WAL Jan-27 spread) · [ ] Max loss ≤ budget · [ ] Position truth known (Sep WAL overlap)

**Terry verdict:** CLEAN / CONDITIONAL / NO TRADE
**Decision:**  [ ] APPROVE   [ ] REJECT   [ ] REWORK: ____

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**
