> ✅ **RESOLVED / HISTORICAL (marked 7/17 audit).** May-15 expiry decision memo — outcomes recorded in POSITIONS.md 5/21 (SSB $95P + WAL $75P both gone per Will confirm). Kept as decision-process record only.

# MAY 15 EXPIRY CLUSTER — Decision Memo

**Created:** 2026-05-08 (Fri night, market closed) | **Expiry:** Friday May 15 2026 (T-5 trading days) | **Scope:** REGINALD-thesis positions only — see `../OZK/` for OZK May 15 cluster, `FORGE/STATUS.md` for TLT $88P May 15.

---

## Executive Read

| Position | Mark (Fri close) | Spot | Distance | Verdict |
|---|---|---|---|---|
| **WAL $75P May-15** | bid $0.15 / ask $0.45 / mid $0.30 / IV 51.9% / OI 203 | $81.90 | **+9.20% OTM** | **LET EXPIRE** — don't roll. Sep coverage at $67.5P + $70P already plays same Q2-print thesis with better strike geometry. |
| **SSB $95P May-15** | bid **$0.00** / ask $3.10 / last $2.00 / IV 70.1% / OI 4 | $96.28 | **+1.35% OTM (NTM)** | **HOLD AND WATCH** — cannot sell at $0 bid; pin-risk play; outcome determined by SSB next 5 days. |

**Headline:** Both decisions are LOW-ACTION. WAL $75P is dead premium — let theta finish it. SSB $95P has no liquid exit — wait for the underlying to decide. The aggressive moves (rolling, force-selling) are NOT the right play here.

---

## WAL $75P May 15

### Mark (Fri 5/8 close)
- bid $0.15 / ask $0.45 / mid **$0.30** (~$30/contract residual)
- IV 51.9% (elevated by short-dated nature — NOT a vol-floor)
- OI 203 — decent liquidity
- Spot $81.90, +9.20% OTM

### Trajectory
- Last 5 days: **+1.36%** — drifting AWAY from strike
- 8 of last 12 sessions green; recovered from Apr 21 print-low $77.83 → May 6 $84.50 high
- Q1 print never sustained breach; tape -2% recovered within days
- 20-day RV 24.4% → 5d 1-σ ≈ 3.4%

### What needs to happen for ITM
- WAL must drop **−8.4% in 5 trading days** = ~−2.5σ move
- Realized-vol odds: **<5%**
- IV-implied odds higher (~15-20%) but trend is wrong direction

### Roll math (sell May 15 $75P, buy later-dated)

| Roll target | Mid | OI | IV | Net debit | Coverage analysis |
|---|---|---|---|---|---|
| **Jun 18 $75P** | $1.62 | 632 | 43.4% | $1.32 | **Expires before Q2 print** (Q2 ~late Jul). Bad timing for thesis. |
| **Sep 18 $75P** | $4.50 | 810 | 40.7% | $4.20 | Captures Q2 print + Investor Day. **But duplicates existing Sep $67.5P + $70P** with weaker delta geometry per dollar. |

### Why LET EXPIRE wins over ROLL

1. **Existing Sep coverage already plays the thesis.** Sep $67.5P + $70P (currently held) capture the same Q2-print + Investor Day catalyst at lower strikes with better $-per-delta payoff if the move comes.
2. **$30/contract residual is below execution-cost noise.** Unless Monday opens with a volatility spike + spot drop, the bid won't lift much.
3. **V2.0 thesis ("compounder with concentrated CRE tail risk") is multi-quarter grind, not 5-day move.** Office maturity wall = $946M maturing through 2026; recognition is event-driven (10-Q May 4-10, Q2 print Jul). May 15 is the wrong bet on the right thesis.
4. **Capital preservation.** $4.20/contract redirected → higher-conviction add (e.g., extending existing Sep $67.5P or tactical short-vol structure) gets more thesis-aligned exposure.

### Pre-registered triggers (Monday-Friday)

| Trigger | Action | Why |
|---|---|---|
| 🟢 WAL <$78 by Tue (T-3) on real catalyst (10-Q surprise, Investor Day leak May 12) | Sell-to-close $75P May at lifted IV | Bid will widen; capture residual + IV bump |
| 🟢 Investor Day May 12 (T-3) reveals NEGATIVE thesis-vector | Re-evaluate; consider rolling to deeper Sep strike if conviction rises | Don't add at $75P — go $67.5P/$65P if rolling |
| 🔴 No catalyst, WAL holds $80+ through Wed | Do nothing; let expire Friday | Default outcome |
| Backstop | May 15 close, expire worthless | No action required |

---

## SSB $95P May 15

### Mark (Fri 5/8 close)
- bid **$0.00** / ask $3.10 / last $2.00 — broken bid; **cannot sell without giving it away**
- IV 70.1% — very elevated (matches NTM pin)
- OI **4** — abysmal liquidity
- Spot $96.28, +1.35% OTM (NTM)

### Trajectory
- Last 5 days: **−1.23%** — drifting TOWARD strike
- Apr 24 already CLOSED BELOW $95 ($94.86) — strike has been crossed once
- Pinned $95-$98 range since
- 20-day RV 24.7% → 5d 1-σ ≈ 3.5%

### What needs to happen for ITM
- SSB must drop **−1.4% in 5 trading days** = <0.5σ move
- Realized-vol odds: **30-40% probability** — meaningful, not negligible
- Already happened once two weeks ago

### Roll math (problematic)

| Roll target | Mid | OI | Notes |
|---|---|---|---|
| Jun 18 $95P | $3.05 | **3** | Wide spread $1.20/$4.90; not investable |
| **Sep 18 $95P** | — | **0** | **Zero bid, zero ask** — broken market; not investable |
| Sep 18 $90P | $4.15 | 1 | Same problem; spread $2.10/$6.20 |

**SSB option market is genuinely thin.** Roll is not a viable instrument. Must let underlying decide.

### Pre-registered triggers (Monday-Friday)

| Trigger | Action | Why |
|---|---|---|
| 🔴 SSB closes <$95 any day next week | Sell at intrinsic + remaining time value | Option becomes ITM; bids should appear; only liquid window |
| 🟢 SSB rallies >$98 by Tue (T-3) | Try to close at any reasonable bid | Liquidity may improve at slight bid; salvage scrap |
| 🟡 SSB pins $95-$98 through Wed | Accept pin; let expire | Default outcome at thin liquidity |
| Backstop | May 15 close — outcome determined by where SSB lands | No active decision needed |

### Caveat: Friday-close mark
SSB May 15 chain has 4 OI total. Monday open could easily move bids 25%+ either way. If SSB $95P bid wakes up >$1 Monday because someone wants exposure, sell-to-close becomes attractive at any reasonable fill — that overrides the "hold and watch" default.

---

## What this memo is NOT

- **Not a roll instruction.** Default = no action; triggers required for action.
- **Not a thesis revision.** WAL V2.0 ("compounder with concentrated CRE tail risk") and SSB FL/TX cohort-fade thesis both intact. May 15 expiry is wrong-tool / wrong-time, not wrong-thesis.
- **Not the only May 15 cluster.** OZK $42.5P + $47.5P May 15 are at peer-agent OZK. TLT $88P May 15 is FORGE territory. This memo covers REGINALD scope only.

## What changes the verdict

- **WAL:** A real -3%+ down catalyst Mon-Wed (10-Q surprise, leaked Investor Day, broader regional shock, KRE <$66 break) lifts bid significantly → sell-to-close becomes meaningful, not hold-to-expiry. Watch headline tape Mon AM.
- **SSB:** Any close <$95 → option goes ITM, find the liquidity window. Otherwise: default = expire.

---

*Companion files:* `POSITIONS.md` (canonical position state) | `WAL/THESIS.md` (V2.0 framing) | `STATUS.md` (May 15 cluster row in KEY CATALYSTS)

---

## EXECUTION DAY — Friday May 15, 2026 (~12:21 ET intraday)

### Tape moved decisively in our direction overnight + intraday

| Metric | 5/8 close (memo date) | 5/11 close (ITM trigger fire) | 5/15 ~12:21 ET (intraday) |
|---|---|---|---|
| **SSB spot** | $96.28 (+1.35% OTM) | $93.89 (-1.17% ITM) | **$91.21** (-3.99% ITM) |
| **Day move (5/15)** | — | — | open $93.17 → low $91.15 (-2.17% intraday) |
| **$95P bid** | $0.00 (broken) | (unknown, likely $0) | **$1.55** — live! |
| **$95P ask** | $3.10 | — | $4.30 |
| **$95P last** | $2.00 | — | $3.23 |
| **$95P intrinsic** | $0.00 (OTM) | $1.11 | **$3.79** |
| **$95P IV** | 70.1% | — | **93.3%** (pin vol) |
| **Volume / OI** | 0 / 4 | — | 1 / 1 |

**Read:** The pre-registered 🔴 trigger from this memo ("SSB closes <$95 any day next week → Sell at intrinsic + remaining time value | Option becomes ITM; bids should appear; only liquid window") fired Mon 5/11 ($93.89 close) and is now significantly ITM at $91.21. The bid HAS appeared ($0 → $1.55) per the trigger logic. However, the **bid at $1.55 is $2.24 BELOW intrinsic value of $3.79** — selling at bid forfeits ~$224/contract.

### Roll math (still not viable)

| Target | Bid / Ask / Last | OI | Verdict |
|---|---|---|---|
| Jun 18 $95P | $3.10 / $6.80 / $3.04 | 3 | Wide spread $3.70; thin OI; net debit vs $95P May 15 ≈ wash. Not investable. |
| Sep 18 $95P | $0.00 / $0.00 | 0 | **Still broken market.** Zero bid/ask. Not investable. |
| Sep 18 $90P | $3.70 / $6.90 / $3.37 | 1 | Spread $3.20; thin OI. Not investable. |

**Roll path confirmed CLOSED.** This was the case 5/8 and is the case 5/15. SSB option chain past May is not transactable at thesis-relevant strikes.

### Auto-exercise risk (the new factor)

If SSB closes <$95 today (near-certain at intraday $91.21), the long $95P will auto-exercise at 4:00 PM ET unless explicit DNE instruction. Result: **SHORT 100 shares of SSB per contract at $95 strike.**

| Broker | Default behavior | Risk |
|---|---|---|
| Schwab / Fidelity | Auto-exercise if account supports short equity | Margin call possible if intraday loss + overnight gap |
| IBKR | Auto-exercise ≥$0.01 ITM | Short stock position carries hard-to-borrow + overnight risk |
| Robinhood / E*Trade | Auto-close ITM options if account can't support short | May force-close at bid (could be unfavorable mark) |

**For thesis-pure exit (which is what this memo prescribed):** close before market close TODAY. Holding through assignment converts a clean options exit into an open short-equity position with overnight + borrow + margin complications.

### TACTICAL RECOMMENDATION — Sell-to-Close TODAY before 4:00 PM ET

| Phase | Time | Action |
|---|---|---|
| **Phase 1 — Patient limit** | NOW – 2:00 PM ET | Place STC limit @ **$3.50** (92% of intrinsic at $91.21 spot; ~$5 above bid). Wait. |
| **Phase 2 — Step-down** | 2:00 – 3:00 PM ET | If unfilled, cancel and re-place @ **$3.00** (79% of intrinsic). |
| **Phase 3 — Clear-the-book** | 3:00 – 3:30 PM ET | If unfilled, re-place @ **$2.50** (66% of intrinsic; mid is currently $2.93). |
| **Phase 4 — Forced exit** | 3:30 – 3:50 PM ET | Market order or STC @ bid ($1.55 currently) to avoid auto-exercise. |
| **Phase 5 — DNE backstop** | Before 3:45 PM ET | If still unfilled AND Will does not want to take short SSB exposure: contact broker to file **Do-Not-Exercise (DNE)** instruction on the long $95P contract. Option expires worthless ($-$ paid premium lost); no assignment. |

### EV math at each phase (per contract, intrinsic $3.79 at current $91.21)

| Phase fill | $/contract | vs intrinsic | vs original premium (if entered $2.00) |
|---|---|---|---|
| Phase 1 ($3.50) | +$350 | -$29 | +$150 (+75%) |
| Phase 2 ($3.00) | +$300 | -$79 | +$100 (+50%) |
| Phase 3 ($2.50) | +$250 | -$129 | +$50 (+25%) |
| Phase 4 ($1.55 bid) | +$155 | -$224 | -$45 (-23%) |
| Phase 5 (DNE) | $0 (premium lost) | -$379 | -$200 (-100%) |
| Auto-exercise → short SSB @ $95 | +$379 intrinsic captured BUT overnight short equity exposure | matches intrinsic | +$179 (+90%) BUT carries borrow + margin + Mon-gap risk |

### Decision logic

- **If Will wants clean thesis-pure exit + no overnight short equity exposure:** Execute Phase 1-4 today. Best case Phase 1 fills @ $3.50 = +$350/contract win.
- **If Will is comfortable holding short SSB at $95 into Mon 5/18 + believes thesis continues (cohort-fade + FL/TX exposure intact):** Let auto-exercise → start short at $95; capture intrinsic + retain directional exposure. **Requires margin/buying power capacity for 100 × $95 = $9,500 per contract short equity position.**
- **Recommendation:** **Phase 1-4 execution.** Reasoning: (1) the memo's pre-registered design was thesis-relevant options exit, not a stealth pivot to short equity exposure; (2) SSB FL/TX thesis can be re-expressed via Sep $90P (currently bid $3.70 / ask $6.90 / OI 1 — same problem the memo flagged 5/8) or new positions if conviction warrants; (3) overnight + assignment complexity is operational risk that didn't get pre-registered consent.

### ⚠️ Unknown: position quantity

POSITIONS.md does NOT carry the quantity column (dropped in 5/8 broker refresh). FORGE/STATUS.md is Mar 25 stale. **Will needs to confirm contract count at broker.** All per-contract math above scales linearly.

### Open question for Will (REPLY-REQUIRED if possible before 2:00 PM ET)

1. **Confirm contract quantity** (typical recent REGINALD positions = 1-2 contracts; assume 1 for math unless told otherwise)
2. **Confirm execution approach** — Phase 1-4 (sell-to-close ladder) or hold-and-let-exercise (short SSB at $95)?
3. **Confirm DNE backstop willingness** — if liquidation fails, file DNE before 3:45 PM ET to avoid forced short equity position?

### Default (if no Will reply before 3:30 PM ET)

Execute Phase 4 (sell-to-close at bid by 3:30 PM ET) and Phase 5 (file DNE by 3:45 PM ET) — protects against unwanted short equity assignment at the cost of taking suboptimal fills. Captures whatever bid is live. This is the operationally-safe default for an illiquid expiry with no Will input.

---

