# MIDAS — STATUS

**Last Updated:** 2026-07-11 (build session — DAEDALUS scaffold) · **Status:** 🟠 elevated (M1 gold-debasement live; spot reads await `metals_watch.py`)
**Class:** Market-agent (metals as macro tells: monetary + industrial) · **Spawnable by:** PROME or Will · **Maturity:** L1 (scaffold; DAEDALUS FLEET_MAP)

> **Newborn agent, 2026-07-11.** No day-1 spot instrument yet (`metals_watch.py` = the priority first-session increment). The value at birth is the **dual-channel structure + clean seams**. M1 carries the confirmed real-yield read (FRED); **M2/I1/I2 need spot pulls — flagged as gaps** (channels-first #1 guard).

---

## CONVERGENCE MATRIX (universal 5-pt + local state)

| # | Channel | Score (1–5) | Local state | Independence | Key signal [src, date] | Upgrade trigger |
|---|---|:---:|---|---|---|---|
| **M1** | Gold — debasement / real-rates | **3 🟠** | debasement premium live, needs spot | monetary root (shared w/ M2) | 10Y real yield **DFII10 2.31** [FRED, 2026-07-09] — elevated; gold structurally bid *despite* positive real yields = debasement premium. **MIDAS owes the gold-spot + divergence quantification** | gold up while real yields up, extreme + sustained → 5 |
| **M2** | Silver + gold/silver ratio | **2 🟡** *(gap)* | no live read | monetary root (shared w/ M1) + industrial overlap | ⚠️ **MIDAS owes first silver-spot + GSR pull** | GSR >95 (risk-off) → 4 |
| **I1** | Copper — Dr. Copper / China | **2 🟡** *(gap)* | no live read | industrial/China root | ⚠️ **MIDAS owes first copper-spot + LME-inventory pull** | copper −20% + LME inv +100% → 5 |
| **I2** | PGMs (platinum/palladium) | **2 🟡** *(gap)* | no live read | supply root (SA/Russia) | ⚠️ **MIDAS owes first Pt/Pd-spot + SA/Russia supply pull** | major SA/Russia outage/sanction → 4 |

**Composite: 9/20** *(M1 3 + M2 2 + I1 2 + I2 2). Provisional — re-score after `metals_watch.py` lands the spot legs. M1 carries the live thesis (debasement); the industrial channel awaits its first reads.*

**Independence note:** a risk-off shock drives M1 (gold up) AND I1 (copper down) via the same macro root — count once in a composite-stress call. A monetary/debasement root drives M1+M2 together; the industrial channel (I1/I2) is a distinct root. **Monetary and industrial channels can diverge legitimately** (gold up on debasement + copper up on growth is not a contradiction).

---

## LIVE CHANNEL READS (sourced + dated)

- **M1 — Gold — debasement / real-rates** [FRED DFII10, 2026-07-09]: 10Y real yield = **2.31**, elevated. The live signal is the *divergence*: positive/rising real yields are a classic gold headwind, yet gold has stayed structurally bid — the gap between the two is the **fiscal-debasement + central-bank-buying premium**. **MIDAS owes** the gold-spot pull to quantify the divergence (the `metals_watch.py` first increment). Routes to BOND (owns the real-yield level) + LIQUID (safe-haven).
- **M2 — Silver + gold/silver ratio** ⚠️ GAP: no live read. **MIDAS owes** the first silver-spot + gold/silver-ratio pull (risk-appetite/monetary gauge).
- **I1 — Copper — Dr. Copper / China** ⚠️ GAP: no live read. **MIDAS owes** the first copper-spot + LME/COMEX-inventory + China-imports pull. Cross-flag ZHAO (China demand).
- **I2 — PGMs** ⚠️ GAP: no live read. **MIDAS owes** the first Pt/Pd-spot + SA/Russia supply-concentration pull. Cross-flag HAWK (supply geopol).

**Inherited cross-agent context:** BOND owns the real-rate level MIDAS's M1 diverges from; ZHAO owns the China demand MIDAS's copper reads; the debasement/de-dollarization macro backdrop is the slow thesis the daily prices test.

---

## EXIT / INVALIDATION (standing-rule-vs-state triad)

| Channel | Standing rule | Current state @ level | FIRED? |
|---|---|---|---|
| M1 | gold up while real yields up, extreme + sustained (debasement premium) | real yield 2.31 elevated; divergence live but unquantified | NOT-SCORED (needs gold spot) |
| M2 | gold/silver ratio >95 sustained (risk-off) | needs first pull | NOT-SCORED |
| I1 | copper −20% AND LME inventory +100% (demand collapse) | needs first pull | NOT-SCORED |
| I2 | major SA/Russia PGM supply outage/sanction | needs first pull | NOT-SCORED |

**Fired-count: 0 of 4** (newborn; M1 armed on the real-yield divergence). **Thesis-kill vs channel-kill:** a copper rally kills I1's growth-worry read — NOT the monetary thesis (M1), which is independent. The monetary and industrial channels are separate tells; one dying doesn't kill the other. Whole-thesis death = gold converges back to real rates (debasement premium gone) AND copper/China normalizes — multi-quarter.

**Cleanest bidirectional flip (BRENT discipline):** M1 — if gold sells off as real yields rise (converging), the debasement premium is falsified; if gold holds/rises through rising real yields, it's confirmed. Testable at each CPI/FOMC.

---

## OPEN ON MIDAS (next session)

1. **Build `metals_watch.py`** (priority first increment, PAT-041-wired) — real yield (FRED DFII10, confirmed) + gold/silver/copper/Pt/Pd spot (ETF proxies GLD/SLV/CPER/PPLT/PALL via shared FORGE `fetch.py`; validate — futures GC=F errored on test) + gold/silver ratio. Wire into boot.py.
2. **M1 quantification** — gold spot vs real-yield divergence (the debasement premium). Route to BOND/LIQUID.
3. **I1 first pull** — copper spot + LME inventory + China imports. Route to ZHAO. (The cleanest China-growth tell.)
4. **M2 / I2 first pulls** — silver+GSR; Pt/Pd + SA/Russia supply.
5. **Seed PREDICTIONS** — real-rate-divergence call, copper-inflection call, GSR call.
6. **Process inbox** — BOND/ZHAO seam packets (the two-way ones), LIQUID/HAWK/HENRY handshakes.

---

## BOTTOM LINE

**MIDAS is live as of 2026-07-11** — the dual-channel metals agent (monetary gold/silver + industrial copper/PGM), built to own two of the tape's best macro tells that had no owner. The most important reading is **M1**: with 10Y real yields elevated at 2.31 (FRED 7/9), gold's continued structural bid *despite* positive real yields is a live fiscal-debasement + central-bank-buying signal — MIDAS's first job is to quantify that divergence (gold spot), then hand the read to BOND (real rates) and LIQUID (safe-haven). The industrial channel (copper as the Dr.-Copper/China thermometer, PGMs on SA/Russia supply) plus silver/GSR are honest gaps awaiting the `metals_watch.py` instrument — the priority first-session build. Next: build metals_watch, quantify the gold divergence, pull copper for ZHAO.
