# FIRE CARD — KRE — Regional-bank puts (fresh deploy)
**Setup ID:** TRY-FIRE-001 · **Trigger class:** PRICE
**Thesis owner:** REGINALD (regional/CRE) + NEXUS (regime) · **Card pre-built:** 2026-06-26 · **Fired:** ____ (fill at fire)
**Status:** PROPOSE-ONLY — Will [Approve] required (rule #5). Detection owned by LIQUID/SENTRY.

══════════════════════════════════════════════════════════════
ZONE 1 — PRE-LOCKED (do NOT re-derive at fire)
══════════════════════════════════════════════════════════════
- **Trigger condition (exact):** **HY OAS breaks ≥ 280 bps** (from ~276 baseline 6/24) AND sustains
  the level (not a single intraday print — thin-liquidity discipline). This is the credit-regime
  widening tell that pulls broad-regional transmission forward from the Q1–Q2 2027 base case.
- **One-line setup:** credit is repricing risk in real time — buy liquid regional-bank downside
  before the equity tape catches the spread move.
- **Structure:** **KRE puts**, **~3–6 month** expiry (capture the widening momentum, not the 2027 grind),
  **~8–12% OTM** strike ladder. KRE = most liquid regional expression; tight option spreads.
- **Why this expression:** HY-break is a *path/level* trigger, not a single-name event → ETF beta is
  the clean vehicle. Puts (not duration/TBT) because the channel is credit-spread, not rates.
- **Alternatives rejected:** single-name (WAL/OZK) puts = idiosyncratic, miss the broad move;
  equity short = unbounded + margin; long-dated 2027 puts = wrong tenor for a momentum break.
- **Max-loss budget:** [SET WITH WILL — e.g. $400–600 / fresh-capital tranche; dry powder, rule: trigger-only]
- **Invalidation (thesis/price/time):** HY round-trips back < 270 sustained → credit-stress false alarm.
- **Kill line:** HY back < 270 sustained, OR KRE reclaims prior range high → exit.
- **Confirm line:** HY sustains > 280 **and** KRE breaks key support **and** CCC-HY ratio widening
  (REGINALD/NEXUS corroboration) → hold / consider 2nd tranche on next red day.

══════════════════════════════════════════════════════════════
ZONE 2 — LIVE MARKS (fill ONLY this at fire — rule #4)
══════════════════════════════════════════════════════════════
- **Timestamp (ET):** ____
- **Trigger-level confirm:** HY OAS ___ bps (≥280 & sustained?) [Y/N] · CCC-HY ratio ___ · `fetch.py fred BAMLH0A0HYM2`
- **Spot:** KRE $____ (as-of ____) · `fetch.py price KRE --json`
- **Green/red day check (rule #6):** KRE today ___% → puts on green ✓ / breaking & why: ____
- **Chain marks:** `chain_fetch.py KRE <EXPIRY> --type put --no-cache`
  | Strike | Mark | Spread% | IV% | OI | Moneyness% |
  |---|---|---|---|---|---|
  | | | | | | |
- **Liquidity OK?** [spread/OI per chain flags — Y/N]
- **Broker position truth:** existing KRE puts in book (FORGE/STATUS shows KRE Dec/Sep/Aug ladder) — net new vs overlap? [check live]
- **Sizing:** `risk_calc.py --premium <mark> --max-loss <budget>` → ____ contracts

══════════════════════════════════════════════════════════════
ZONE 3 — TRIGGER CONFIRM + DECISION
══════════════════════════════════════════════════════════════
- [ ] HY actually ≥280 & sustained (not near-miss) · [ ] Live marks < 15 min · [ ] Green/red OK
- [ ] Liquidity OK · [ ] Max loss ≤ budget · [ ] Position truth known (overlap with existing KRE ladder checked)

**Terry verdict:** CLEAN / CONDITIONAL / NO TRADE
**Decision:**  [ ] APPROVE   [ ] REJECT   [ ] REWORK: ____

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**
