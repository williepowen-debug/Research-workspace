# TLT Jun 18 $85P Decision Action Card
**Created:** 2026-05-22 ~15:00 ET
**State:** `BROKER_PENDING`
**Owner:** Will for broker execution; Prome for post-fill file updates.
**Next:** Will places 2 orders at broker Tue 5/27 open if C3/C5 have not invalidated.
**Window:** Execute by 2026-06-06 EOD unless conditional trigger fires earlier.
**Backstop:** 2026-06-06 EOD.
**Default:** Execute approved 2/1 roll; do not let Jun theta decay continue by default.
**Source:** `AGENTS/HENRY/outbox/REPLY-PROME-2026-05-22-tlt-decision.md`
**Sister SIG:** `AGENTS/HENRY/inbox/SIG-PROME-HENRY-2026-05-22_tlt-decision-and-vix-trigger-calibration.md`
**Position:** `FORGE/STATUS.md` (5/21 19:30 ET) + live 5/22 marks below

**State note:** Will approved the plan, but orders were NOT placed before the computer crash. Memorial Day Monday 5/25 closed; earliest execution window is Tuesday 5/27 open.

---

## ⭐ EXECUTION TICKET — for Will to place at broker

**Approval received:** 2026-05-22 — Will acknowledged macro read is general directional (not catalyst-specific), accepted HENRY's 2/1 + Sep $85P as the horizon-matched expression.

### Two orders (place separately for cleaner fills)

**Order 1 — Sell-to-close (close out all Jun):**
- **Sell-to-close 3 × TLT Jun 18, 2026 $85.00 Put**
- Limit: at mid or better; expected mid ~$0.85–0.95 per contract
- Expected cash in: **~$255–285**
- Order type: limit; GTC or day's choice

**Order 2 — Buy-to-open (open new Sep):**
- **Buy-to-open 1 × TLT Sep 19, 2026 $85.00 Put** (recommended monthly; cleaner basis than Sep 30 quarterly)
- Limit: at mid or better; expected mid ~$2.80–3.20 per contract
- Expected cash out: **~$280–320**
- Order type: limit; GTC or day's choice

### Net economics (estimated at TLT $84.54 spot, 5/22 ~15:00 ET)

| Item | $ |
|---|---:|
| Cash in (close 3 Jun) | +$255 to +$285 |
| Cash out (open 1 Sep) | -$280 to -$320 |
| **Net cash** | **~flat to -$50** |
| Crystallized gain on Jun (vs $246 cost) | +$9 to +$39 |
| New Sep position cost basis | $280–320 |

### Execution timing recommendation

**Either today PM (5/22) or Tuesday open (5/27)** — both defensible. Markets close Memorial Day Monday 5/25.

- **Today PM:** locks the decision; avoids weekend/holiday gap risk; market makers may tighten spreads pre-holiday. Modest liquidity-thinness risk in last 30 min.
- **Tuesday open:** fresh marks; risk is TLT continues bouncing over the weekend (Jun sell at lower price + Sep buy at higher price) — wrong-direction drift for the trade.

**Slight bias to today PM** to lock the decision and remove the "wait one more day" loop, but Will's call.

### After fills, post-execution tasks (Prome owns)

1. Update `FORGE/STATUS.md` TLT position table with new 1 × Sep 19 $85P + remove 3 × Jun 18 $85P.
2. Log fills in `PROME/TRADE_DECISIONS.md` (entry stub appended on Will-approval).
3. Update `AGENTS/HENRY/STATUS.md` with execution close (or HENRY does on next boot).
4. Mark this action card **Status: Completed** with fill prices once Will reports.

---

## Objective

Decide disposition of **TLT Jun 18 $85P × 3 contracts** (the only winner in the 6/18 expiry cluster) ahead of the final-2-week theta cliff. HENRY validated 2/1 split, Sep $85P roll target, 6/06 EOD time backstop, and conditional triggers below.

This card is **not** a trade order. It defines the allowed actions, the conditional triggers, and the decision Will needs to approve.

---

## Current Position State

| Strike | Expiry | Qty | Cost basis | 5/21 close P&L | Live 5/22 view |
|---|---|---:|---:|---:|---|
| **$85P** | **Jun 18** | **3** | **$0.82** ($246 total) | **+92.22%** ($471) | **$84.51 spot → $0.49 ITM; est. ~$0.80–0.95/contract = ~$240–285 value, basically break-even on cost basis after today's $0.95 bounce** |
| $85P | Sep 30 | 2 | $2.52 | +16.81% ($588) | Held — not in scope of this card |
| $82P | Oct 16 | 2 | $1.68 | +6.75% ($358) | Held — not in scope of this card |

**Key implication:** Today's TLT bounce ($83.56 → $84.51, +$0.95) compressed the Jun $85P from $1.57 to roughly $0.85–0.95. Much of the +92% gain crystallized yesterday has evaporated intraday. Whatever decision Will makes, it's now a thesis-positioning decision more than a gain-locking decision.

---

## HENRY Verdicts (5/22 ~14:50 ET reply)

| Q | HENRY's call | Why (1-line) |
|---|---|---|
| **Q1 split** | **2/1 (strawman holds)** | Bounce + TIPS softens near-term R11 imminence but doesn't break structural setup. 2/1 monetizes bounce-fragile intrinsic; keeps Sep contract live for substance-side acceleration that hasn't flipped. |
| **Q2 strike** | **Sep $85P** (NOT $82P) | Conservative-ITM while thesis cooling-but-intact. $82P needs another leg lower to monetize; don't bet on demand-hole urgency BOND just qualitatively weakened. |
| **Q3 time trigger** | **6/06 EOD** (NOT 6/13) | 6/13 backstops into the worst of the theta cliff. 6/06 gives 12 days runway and still respects 28-day setup. |
| **Q4 conditional level** | **$85.50 + velocity floor** | Single close ≥$85.50 OR 2-session close ≥$85.20 — catches the grind without firing on intraday noise. |

**HENRY's one-line take:** Duration regime cooling at surface (TIPS absorbed, today's bounce) but substance (10Y 4.67%, real yields rising, breakeven flat, PPI 6.0%) hasn't flipped — noise inside an intact setup.

**Key HENRY flag:** R11 clock still running 5/28–6/02. **3/0 (sell all) would leave you naked on the exact window where vol-spike pathway transitions from clock-running to firing.** 2/1 is the right hedge.

---

## Proposed Execution (pending Will [Approve])

### Leg A — Trim 2 of 3 Jun contracts
- **Order:** Sell-to-close 2 × TLT Jun 18, 2026 $85P
- **Limit guidance:** mid or better; expected fill ~$0.85–0.95 each → realize ~$170–190 cash
- **Crystallized result:** ~$6–24 gain over cost basis ($164 cost on those 2 contracts)

### Leg B — Close last Jun contract (theta dump)
- **Order:** Sell-to-close 1 × TLT Jun 18, 2026 $85P
- **Limit guidance:** mid or better; expected fill ~$0.85–0.95 → realize ~$85–95 cash
- **Crystallized result:** ~$3–13 gain over cost basis ($82 cost on this contract)

### Leg C — Open Sep roll
- **Order:** Buy-to-open 1 × TLT **Sep 19, 2026 $85P** (monthly) ⚠️ see sub-decision below
- **Limit guidance:** mid or better; expected fill ~$2.80–3.20 → ~$280–320 debit
- **Net new position:** 1 × Sep 19 $85P joining existing 2 × Sep 30 $85P

### Net cash impact (estimated at current marks)
- Cash in (A+B): ~$255–285
- Cash out (C): ~$280–320
- **Net: approximately flat to -$50**
- The economics are now a **thesis re-positioning**, not a gain lock-in (yesterday's marks would have been ~+$170 net; today's bounce ate it)

### ⚠️ Sub-decision Will needs to choose: Sep monthly vs Sep 30 quarterly

Existing TLT Sep 30 $85P × 2 are at $2.52 basis (+16.81% → ~$2.94 current). HENRY said "Sep $85P" without specifying the date.

| Option | Pro | Con |
|---|---|---|
| **Sep 19, 2026 (monthly)** — recommended default | Clean separate basis; standard third-Friday liquidity; doesn't entangle with existing Sep 30 position | Marginally less duration runway (11 days less than Sep 30) |
| **Sep 30, 2026 (quarterly)** — basis-mix | Stacks onto existing position (3 × Sep 30 $85P after); 11 more days runway | Mixes basis from $2.52 (old) and ~$2.94 (new) — accounting friction in JOURNAL/FORGE |

**Recommend Sep 19 monthly** (cleaner books, negligible duration difference). Will may overrule.

---

## Conditional Trigger Watch Card (live until 2026-06-06 EOD)

| Trigger | Level | Action | Status (5/22 intraday) |
|---|---|---|---|
| **C1 — TLT cooled (single)** | TLT closes ≥ **$85.50** any session | Execute 2/1 split same/next session | $84.51 spot → $0.99 to fire |
| **C2 — TLT cooled (grind)** | TLT closes ≥ **$85.20** on **2 consecutive sessions** | Execute 2/1 split | First session would be today if EOD ≥$85.20 |
| **C3 — TLT breaks lower** | TLT closes **< $82** | **Hold full 3 contracts**, roll into expiry week (more exposure, not less) | $84.51 → $2.51 cushion |
| **C4 — Time backstop** | 2026-06-06 EOD reached with no other trigger fired | Execute 2/1 split regardless of mark | 15 days runway |
| **C5 — Regime-break (substance)** | HY OAS ≥ 290 sustained OR R11 vol-spike trigger fires (5/28–6/02 window) | **Hold all 3 contracts**, defer decision; thesis activating | Watching |

**Rule:** If C1, C2, or C4 fires → execute Legs A+B+C as drafted. If C3 or C5 fires → hold full size, re-decide.

---

## Forbidden Actions

- No execution without Will explicit [Approve].
- No partial fills outside the 2/1 split (e.g., trim 1 / hold 2 / no roll) unless C5 fires.
- No revenge-adds if Jun $85P expires worthless after this restructure.
- No re-entering Jun expiry on the dump leg (Leg B); the close is to dodge the final-2-week cliff, not to flip.

---

## Open Will-decisions in this card

1. **Approve / reject** the 2/1 split with Sep $85P roll.
2. **Pick Sep 19 monthly** (recommended) vs **Sep 30 quarterly** (basis-mix).
3. **Approve conditional triggers C1–C5** as drafted, or adjust levels.
4. **Confirm 6/06 EOD time backstop** (HENRY-set, pull-forward from 6/13).
5. *Optional:* if Will wants to wait for today's EOD TLT print before deciding, defer to Tuesday 5/27 open (Monday closed for Memorial Day).

---

## Expiration / Supersession

This card expires after:
- Will logs approval and execution completes, OR
- 2026-06-06 EOD reached and time-backstop fires, OR
- C5 substance-regime-break fires and supersedes the decision, OR
- Will explicitly cancels.

Update `PROME/TRADE_DECISIONS.md` and `AGENTS/HENRY/STATUS.md` on execution. Update `FORGE/STATUS.md` TLT position table on fill.
