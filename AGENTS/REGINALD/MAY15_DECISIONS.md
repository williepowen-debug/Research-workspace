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
