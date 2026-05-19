# QUARTER-END SOFR/REPO PLAYBOOK — MAR 27-31, 2026
**LIQUID | Built:** 2026-03-26 03:52 UTC | **PRED-23: 90% confidence SOFR spike at quarter-end**

---

## STRUCTURAL SETUP
- RRP: ~$1.1B (effectively ZERO — no shock absorber)
- Reserves: $3.020T (floor $2.7T → $320B cushion; 60% concentrated at 5 G-SIBs)
- 20Y settlement: $17B+ on EXACT quarter-end (Mar 31)
- Fed T-Bills: $352B (stealth injection; exceeds COVID peak)
- FHLB: +31% YoY (SVB-era pre-stress pattern)
- 2019 analog ACTIVE: zero RRP + settlement collision → SOFR spike mechanism intact

---

## DAILY MONITORING BRIEF

### MON MAR 27
**What happens:** Window dressing begins in force. Banks start shrinking repo books (balance sheet trim for Q-end). OBDCII starts reporting window (Mar 27–Apr 3).
**Watch:**
| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| SOFR | ≤3.65% | 3.66–3.70% | >3.70% |
| RRP | >$2B | $1–2B | <$1B |
| FRA-OIS spread | <10bps | 10–15bps | >15bps |
| Dealer repo vol | Normal | -10% WoW | -20% WoW |
**Key flag:** If SOFR moves >3.68 on Monday, window dressing is tighter than expected → escalate immediately.

### TUE MAR 28
**What happens:** Window dressing peak day. Dealers at max balance sheet constraint. PC redemption windows close at many fund-end dates. OBDCII ongoing.
**Watch:**
| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| SOFR | ≤3.68% | 3.69–3.75% | >3.75% |
| SOFR-IORB spread | <-7bps | -7 to 0bps | >0bps (above IORB) |
| RRP | Any uptick | Flat | Further decline |
| HY OAS | <320bps | 320–335bps | >335bps |
**Key flag:** SOFR > IORB (3.75%) = acute stress → SRF activation watch (stigmatized but available).

### WED MAR 26 [NOTE: Mar 26 = Thursday prior week — treat as pre-positioning day]
### WED MAR 26 IS ALREADY PASSED. THIS PLAYBOOK COVERS MAR 27–31.

### THU MAR 27 (see above) / FRI MAR 28 (see above)

### MON MAR 31 — CRITICAL DAY
**What happens:**
1. **20Y Treasury settles (~$17B+)** — dealers must fund positions overnight
2. **Quarter-end** — all window dressing hits simultaneously; bank balance sheets at minimum
3. **Zero RRP** — no shock absorber; any overnight cash demand goes direct to reserve accounts
4. **Pension rebalancing** — SPX -7.1% from ATH triggers equity→bond rebalancing flows
5. **Japan FY-end** — final repatriation trades settle; life insurer hedges may roll
**Watch:**
| Metric | Green | Yellow | Red |
|--------|-------|--------|-----|
| SOFR | ≤3.71% (+8bps) | 3.72–3.78% (+9–15bps) | >3.78% (>15bps spike) |
| GC repo vs SOFR | <5bps divergence | 5–10bps | >10bps = dealer stress |
| Fed H.4.1 (reserves) | >$2.85T | $2.75–2.85T | <$2.75T (near floor) |
| SRF usage | Zero | Any usage = yellow | Confirmed usage = red |
| Brent | <$108 | $108–$112 | >$112 (tail activation) |
**IORB = 3.75%. SOFR above IORB = 2019 analog triggering.**

### TUE APR 1 — NORMALIZATION CHECK
**What happens:** Quarter-end pressure releases. Banks re-expand repo books. SOFR should revert.
**Signal:** If SOFR does NOT revert to ≤3.65% by Apr 1 close → structural stress, not technical quarter-end. Escalate to REGINALD and HENRY immediately.

---

## SCENARIO FRAMEWORK

### BASE CASE (60%) — Orderly Quarter-End
**Mechanics:** SOFR spikes 3–8bps (peaks Mar 31 ~3.66–3.71%), normalizes Apr 1. 20Y settlement absorbed. Window dressing compresses repo but no cascade. RRP zero = uncomfortable but manageable at current reserve level.
**Signal confirmation:** SOFR peak ≤3.71%, no SRF usage, GC-SOFR divergence <5bps, Brent <$110.

**Position Impact:**
- **KRE puts (~$4,864):** NEUTRAL-SLIGHTLY BEARISH. SOFR spike raises regional bank funding costs marginally; confirms NIM compression thesis but not acute enough for immediate price move. Hold.
- **HYG $75P Jun ($288):** NEUTRAL. HY OAS stays 315–325bps. Position retains optionality. No delta event.
- **TLT puts (~$1,544):** SLIGHTLY BULLISH for position. Flight-to-safety demand at quarter-end (pension rebalancing into bonds) may push TLT up temporarily — this is a HEAD-FAKE. 20Y settlement and Japan repatriation are structural headwinds. Hold TLT puts through any Q-end rally.

### STRESS CASE (30%) — SOFR Spike >15bps
**Trigger conditions:** SOFR >3.78% Mar 31, GC repo diverges >10bps, SRF usage confirmed, dealer repo volumes fall >20% WoW.
**Mechanics:** 20Y settlement + window dressing + zero RRP overwhelms reserve distribution. G-SIB concentration means smaller banks can't access reserves. FHLB emergency draws activate (+31% YoY already primed). PC fund credit facility draws add $2–5B+ pressure on G-SIBs same day.

**Position Impact:**
- **KRE puts (~$4,864):** ✅ HIGH VALUE. Regional bank funding stress = direct KRE thesis confirmation. SOFR >3.78% = NIM compression + potential deposit flight headlines. Puts move in-the-money faster.
- **HYG $75P Jun ($288):** ✅ ACTIVATED. Repo stress → credit market contagion path. If FRA-OIS blows out >15bps, HY OAS likely cracks through 320bps trigger. CDX already at 9-mo high (head-fake resolving bearishly). Consider adding HYG puts on stress confirmation.
- **TLT puts (~$1,544):** ⚠️ MIXED. Short-term: flight-to-safety bid may hurt TLT puts (TLT rallies). Medium-term: repo stress = forced UST selling by dealers to fund positions = bearish TLT. **Do NOT cut TLT puts in repo stress — the spike is transient, structural selling resumes Apr 1+.**

**What to add/trim in stress:**
- ADD: KRE puts (delta increase justified)
- ADD: HYG puts if OAS >328bps with SRF usage confirmed
- TRIM: Nothing. All positions are directionally correct in stress scenario.
- WATCH: EUR/USD basis swap — if >-50bps negative, ECB swap line imminent = systemic confirmation

### TAIL CASE (10%) — Brent >$110 + Repo Stress + Margin Calls
**Trigger conditions:** Dimona→Fordow→Kharg sequence (HANS Scenario D 78%), SOFR >3.78%, Brent >$110, energy position margin calls hitting dealer books simultaneously.
**2019 Analog:** Sep 17, 2019: overnight repo 2%→10%+ in hours. Fed injected $75B emergency repo. Current differences: reserves $3T (vs $1.4T then) but RRP = zero (vs partial buffer then). SRF exists but stigmatized.
**Amplification path:** Energy margin calls → dealers sell USTs to fund → 20Y settlement adds to same-day UST supply → SOFR spike → PC fund credit facility draws → G-SIB reserve drain → SOFR spikes further (reflexive).

**Positions that BENEFIT:**
- **KRE puts (~$4,864):** ✅✅ MAX VALUE. Repo crisis = direct regional bank stress. 2019 crisis: bank stocks sold off sharply. KRE puts are the right instrument.
- **HYG $75P Jun ($288):** ✅✅ MAX VALUE. Tail scenario = HY OAS >350bps (freeze threshold). Jun $75P becomes deep ITM territory. Do NOT exit early.
- **TLT puts (~$1,544):** ✅ HOLD. Initial flight-to-safety = TLT spike (hurts puts temporarily). Then: forced UST selling by dealers + energy margin calls + Japan repatriation = structural TLT decline. Tail scenario ultimately bearish for TLT.

**What to do in tail:**
1. Do NOT add TEN calls (already held — let them run; Dimona→Kharg = thesis confirmation)
2. Monitor for Fed emergency repo announcement (SRF usage public = buy KRE/HYG puts aggressively)
3. If Brent >$115: PROP-03 crude short still ON HOLD (thesis: Dimona→Kharg could spike to $120+ before correction)
4. Check EUR/USD basis: <-50bps = ECB swap line watch = systemic dollar funding stress

---

## POSITION-LEVEL ACTIONS

### KRE PUTS (~$4,864)
**Best scenario:** Stress or Tail. Repo spike + SOFR >3.78% = NIM compression + deposit flight risk for regionals.
**Quarter-end specific:** Regional banks are the LEAST able to access Fed reserves (G-SIB concentration). They're forced into FHLB and more expensive funding.
**Action:** HOLD through Mar 31. No roll needed — thesis intact through Q2.

### HYG $75P JUN ($288)
**Best scenario:** Stress or Tail. HY OAS >350bps = freeze threshold = deep ITM.
**Roll Jun→Dec? (PROP-02 flag):** ⚠️ CONSIDER. Jun expiry gives 90 days. If quarter-end is orderly (base case 60%), HY contagion from PC Stage 3 and gas→DQ transmission hits May/June. Rolling to Dec captures Hamilton lag-3/lag-4 (mid-April misses → May/June DQ prints). **Recommend: Roll to Sep or Dec AFTER quarter-end (Apr 1–3), not before.** Pre-quarter-end roll loses potential spike gains.
**Action:** HOLD Jun through Mar 31. Evaluate roll Apr 1–3 post-stress read.

### TLT PUTS (~$1,544)
**Best scenario:** Base or Stress — but medium-term (Apr+), not Mar 31 itself.
**Quarter-end specific:** Pension rebalancing INTO bonds = TLT spike Mar 31 = temporary headwind for puts. DO NOT PANIC. The structural case (Japan $50–120B annual swing, $14T IG supply wall, 20Y settlement concession) is Apr+ thesis.
**Roll Jun→Dec? (PROP-02 flag):** ✅ YES — pre-positioning case is strong. Japan repatriation peaks Apr 20-25, April CPI embeds $108+ oil (print ~Apr 10-15), Warsh transition May = TLT puts are a multi-month thesis, not a Q-end trade. **Roll TLT puts Jun→Dec BEFORE quarter-end (Thu Mar 27 or Fri Mar 28).** Buy time at lower theta cost.
**Action:** 🚨 ROLL TLT PUTS JUN→DEC BY MAR 28. Structural thesis = 6–9 month timeline.

---

## PRE-POSITIONING CHECKLIST — THU MAR 27 / FRI MAR 28

**THU MAR 27:**
- [ ] Roll TLT puts Jun→Dec (before theta bleeds into quarter-end noise)
- [ ] Pull SOFR (publish time: 8 AM ET daily via FRED/NY Fed)
- [ ] Pull RRP (published ~4:30 PM ET prior day on FRED)
- [ ] Note HY OAS (FRED BAMLH0A0HYM2 — daily, 1-day lag)
- [ ] Watch Brent — if >$112 at open = tail scenario escalation

**FRI MAR 28:**
- [ ] SOFR check — flag if >3.68% (window dressing tightening faster than expected)
- [ ] Check FRA-OIS (Bloomberg/Refinitiv) — >12bps = yellow
- [ ] Note dealer GC repo volumes vs SOFR divergence
- [ ] Confirm HYG Jun puts — hold (do not roll yet)
- [ ] Confirm KRE puts — hold
- [ ] Pre-set alert: SOFR >3.70 = immediate notification

**MON MAR 31:**
- [ ] SOFR at 8 AM ET — day-of reading is prior business day (check Fri Mar 28 SOFR)
- [ ] Real-time: GC repo rate vs SOFR (Bloomberg GC repo = BGCR)
- [ ] Real-time: SRF usage (announced in H.4.1 following week — intraday signals via repo desk commentary)
- [ ] Brent check pre-open
- [ ] If SOFR >3.75% (above IORB): escalate to HENRY (VaR cascade watch) + REGINALD (bank funding)

---

## THRESHOLD SUMMARY (Quick Reference)

| Signal | Green | Yellow | Red |
|--------|-------|--------|-----|
| SOFR | ≤3.65% | 3.66–3.70% | >3.70% |
| SOFR (Mar 31 only) | ≤3.71% | 3.72–3.78% | >3.78% |
| RRP | >$2B | $1–2B | <$1B |
| FRA-OIS | <10bps | 10–15bps | >15bps |
| HY OAS | <315bps | 315–335bps | >335bps |
| Brent | <$108 | $108–$112 | >$112 |
| Reserves (H.4.1) | >$2.95T | $2.75–2.95T | <$2.75T |

---

*Generated by LIQUID | Sources: KB.tsv (KB-LIQ-016/017/022/023/046/044) | PRED-23 active*
