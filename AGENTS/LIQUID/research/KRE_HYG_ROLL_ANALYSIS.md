# KRE/HYG JUN→DEC ROLL PRICING ANALYSIS
**Generated:** 2026-03-26 | **Agent:** LIQUID | **Priority:** 🔴 URGENT (Q-end Mar 31 = worse fills)

---

## Current Jun Positions (Roll Candidates)

| Position | Qty | Current Value | Est. KRE/HYG Price | Status |
|----------|-----|--------------|-------------------|--------|
| KRE $67P Jun 30 | 1 | $475 | ~$63-64 | +45.85% ITM |
| KRE $65P Jun 30 | 4 | $1,520 | ~$63-64 | +35.14% ITM |
| KRE $63P Jun 30 | 1 | $305 | ~$63-64 | +9.44% ~ATM |
| KRE $60P Jun 18 | 3 | $641 | ~$63-64 | +47%/-19% OTM |
| HYG $75P Jun 18 | 8 | $288 | ~$78-79 | OTM |

**NOTE:** KRE $60P Sep x2 + KRE $60P Dec x3 already exist. Rolling Jun $60P = redundant at same strike.

---

## Roll Analysis Table

| Position | Current Value | Dec Equiv Strike | Est. Dec Premium | Roll Debit/Contr | Net Roll Cost | Theta Runway Added | Key Dec Catalyst |
|----------|--------------|-----------------|-----------------|-----------------|---------------|--------------------|-----------------|
| KRE $67P Jun→Dec | $475 (1x) | $67P Dec | ~$8.00 | ~+$3.25 | **~$325** | +6 months | Q3 credit break, FHLB stress |
| KRE $65P Jun→Dec | $1,520 (4x) | $65P Dec | ~$7.00 | ~+$3.20 | **~$1,280** | +6 months | Demand destruction Q4 |
| KRE $63P Jun→Dec | $305 (1x) | $63P Dec | ~$5.80 | ~+$2.75 | **~$275** | +6 months | PC contagion Stage 4-5 |
| KRE $60P Jun→Dec | $641 (3x) | Already have Dec | Roll to $63P Dec | ~+$1.50 | **~$450** | +6 months | Avoid duplication |
| HYG $75P Jun→Dec | $288 (8x) | $75P Dec | ~$1.40 | ~+$1.05 | **~$840** | +6 months | OAS >400 Jul cascade |

**Est. Dec premiums assume KRE ~$63, HYG ~$79, VIX elevated 22-25 (not compressed).**
**Roll debit = Dec premium - Jun premium currently received. All are debits (Dec costs more).**

---

## Total Roll Program Cost

| Roll | Net Debit |
|------|-----------|
| KRE $67P x1 | ~$325 |
| KRE $65P x4 | ~$1,280 |
| KRE $63P x1 | ~$275 |
| KRE $60P x3 (→ $63P Dec) | ~$450 |
| HYG $75P x8 | ~$840 |
| **TOTAL** | **~$3,170** |

*Range: $2,600–$3,800 depending on fills and IV at execution.*

---

## Recommendation Framework

### Roll FIRST (Highest Urgency)
**1. KRE $65P Jun x4 — Roll by Mar 28**
- Largest cluster ($1,520 value, $1,280 roll cost)
- Jun 30 expiry = only 96 days. Theta burn accelerates post-Apr earnings
- 4 contracts = liquidity risk; stagger as 2+2 (Mon + Tue) to avoid market impact
- Jun has the Apr 16-21 earnings catalyst BUT: if KRE drops hard on earnings, roll becomes expensive. Roll BEFORE earnings, not after
- Dec captures full demand destruction thesis (Hamilton Q4 peak)

**2. KRE $67P Jun x1 — Roll by Mar 28**
- Deepest ITM → highest theta bleed per dollar
- Roll to $67P Dec or consider stepping up to $70P Dec (wider theta premium)
- Single contract = easy fill

**3. HYG $75P Jun x8 — Roll by Apr 4**
- OTM ($0.36/contract) = cheap roll debit (~$840 total)
- NEXUS cascade: OAS >400 = Jul window. Jun barely catches it; Dec = full thesis
- Low liquidity risk (HYG options are deep market)
- Can wait 1 week post-quarter-end (Apr 1-4) for better fills — small $ stakes

### Consider Holding Jun (Catalyst Window)
**KRE $60P Jun x3 — Conditional hold**
- Already have Sep x2 + Dec x3 at $60P — Jun is redundant at this strike
- If Apr 16 earnings spike vol → harvest Jun, roll proceeds into $63-65P Dec
- "Roll by": Apr 17 (morning of OZK earnings, harvest on vol spike)

**KRE $63P Jun x1 — Secondary priority**
- ~ATM = highest gamma for Apr 16-21 catalyst
- Argument FOR holding Jun: if KRE breaks $60 on earnings, this doubles
- Argument FOR rolling: only $305 value, $275 roll cost = cheap insurance extension
- Recommendation: HOLD through Apr 21 (WAL), then roll on strength

---

## Stagger vs. All-At-Once

**STAGGER. Execute in 3 tranches:**

| Tranche | Date | Positions | Rationale |
|---------|------|-----------|-----------|
| **T1** | Mar 27-28 | KRE $67P x1, KRE $65P 2/4 | Pre-quarter-end. Best fills while window dressing = KRE arb active |
| **T2** | Apr 1-4 | KRE $65P 2/4, HYG $75P x8 | Post-quarter-end. Market normalized. HYG deep market = easy |
| **T3** | Apr 17 | KRE $60P x3, KRE $63P x1 | Harvest on earnings vol spike; roll into Dec on premium |

---

## Priority Roll List (Will Executes In Order)

| # | Action | Position | Roll To | Roll By | Est. Cost | Urgency |
|---|--------|----------|---------|---------|-----------|---------|
| 1 | ROLL | KRE $65P Jun x2 | KRE $65P Dec | **Mar 28** | ~$640 | 🔴 HIGHEST |
| 2 | ROLL | KRE $67P Jun x1 | KRE $67P Dec | **Mar 28** | ~$325 | 🔴 HIGH |
| 3 | ROLL | KRE $65P Jun x2 | KRE $65P Dec | **Apr 2** | ~$640 | 🟠 HIGH |
| 4 | ROLL | HYG $75P Jun x8 | HYG $75P Dec | **Apr 4** | ~$840 | 🟡 MEDIUM |
| 5 | HARVEST→ROLL | KRE $60P Jun x3 | KRE $63P Dec | **Apr 17** | ~$450 | 🟡 MEDIUM |
| 6 | ASSESS | KRE $63P Jun x1 | KRE $63P Dec | **Apr 21** | ~$275 | 🟢 LOW |

**Total capital required: ~$3,170 (range $2,600–$3,800)**

---

## Risks to This Plan

- **SOFR spike Mar 27-28** (zero RRP): KRE vol could spike → better roll premium on Thu-Fri. Watch before executing T1.
- **Dimona escalation before Mar 28**: Risk-off → KRE could drop → deeper ITM → higher roll cost. Bias toward rolling sooner.
- **VIX compression post-Iran ceasefire**: If VIX drops, Dec premiums cheap → ideal roll window. Wait for VIX >22 for T1.
- **Jun fills worse post-Mar 31**: Confirmed. Window dressing + quarter-end = wider spreads on regional bank options specifically.
