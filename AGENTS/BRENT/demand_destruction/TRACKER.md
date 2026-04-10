# DEMAND DESTRUCTION TRACKER

**Last Updated:** 2026-04-10 (Friday data pull: COT + Baker Hughes + Airlines) | **War Day:** ~37 | **Phase:** 1 (ACTIVE) | **Phase 2 Status:** NOT TRIGGERED — ⚠️ PATH A WATCH active + **Trigger #3 WATCH** (COT declining, Apr 7 data pending)

---

## PATH B TRIGGER STATUS

All three must fire simultaneously to confirm Phase 2 via demand destruction path. Path A (Resolution) is binary — see TRANSITION_MATRIX.md.

| # | Signal | Threshold | Current Reading | Status | Last Updated |
|---|--------|-----------|-----------------|--------|-------------|
| 1 | **Brent M1-M3 spread** | <$3/bbl x 3 consecutive daily closes | ~$8-10/bbl (est.) | NOT TRIGGERED | Apr 4 |
| 2 | **EIA gasoline demand YoY** | -5% YoY x 3 consecutive weeks | **+0.8% YoY** (Apr 3 EIA) — still positive. ⚠️ Hoarding distortion in Crisis Wk ~5 inflating this number. Real signal expected May-June | NOT TRIGGERED | **Apr 3** |
| 3 | **CFTC managed money net longs** | Declining x 2 consecutive weeks while price flat | NYMEX net long 73,347 / ICE net short 33,814 (Mar 31). Non-commercial proxy DECLINED Mar 24→31 (-20.1K). Apr 7 report due today (3:30pm ET) — if confirmed lower = WEEK 1 OF 2. | ⚠️ WATCH | **Apr 10** |

**Verdict:** 0/3 core triggers fired. Trigger #3 entering WATCH phase — COT positioning declining. Tier 2 airline indicator ESCALATING: WestJet -19.6% US ASM, Air NZ -15%+, Jetstar -12% transpacific, Ryanair/Lufthansa warnings pending. Jet fuel +95% ($2.50→$4.88/gal). Airline cuts now global, not just US-carrier. Per framework, cuts lead EIA gasoline data by 4-8 weeks → EIA gasoline YoY turns negative May-June (CONFIRMED timeline).

---

## LEADING INDICATORS DASHBOARD

### Tier 1 — Act On These

| Indicator | Value | Direction | Source | Updated |
|-----------|-------|-----------|--------|---------|
| Brent M1-M3 spread | ~$8-10 (est.) | Extreme backwardation | ICE | Apr 4 |
| Retail gas (US avg) | **$4.08/gal** | +37% since war | AAA | Apr 2 [CONF] |
| Gas price vs $4 breakpoint | **BREACHED** | $4 = demand resistance threshold (2022 analog) | AAA/EIA | Apr 2 |
| EIA gasoline demand YoY | **+0.8% YoY** (4-wk avg 8.8M bpd). ⚠️ Hoarding distortion active (Crisis Wk ~5). Refinery inputs declining while product supplied +YoY = inventory drawdown, not real demand. | — | EIA WPSR | **Apr 3** [EST] |
| CFTC managed money | NYMEX net long **73,347** / ICE net short **33,814** (Mar 31 [CONF]). Non-commercial proxy: Mar 24=233.6K → Mar 31=213.5K (**DOWN 20.1K**). Apr 7 data due today 3:30pm. **DIRECTION: DECLINING** | Declining x2 weeks while price flat | CFTC COT | **Apr 10** |

### Tier 2 — Confirming Indicators

| Indicator | Value | Threshold | Source | Updated |
|-----------|-------|-----------|--------|---------|
| Airline capacity cuts | **FIRING + ESCALATING:** United -5%, Delta -4%+$400M charge+LAX-ANC cut, American -6%, ULCCs -10%, SAS ~1K, **WestJet -19.6% US ASM**, Air NZ 1,100 flt/~15%, Jetstar -12% transpacific, Virgin AUS Doha suspended. Ryanair/Lufthansa warnings (not yet impl). Jet fuel **+95%** ($4.88/gal). Global fares **+24% YoY**. 14.6% NA departures cancelled peak day. | 2+ carriers >5% ASM | Multiple | **Apr 10** [CONF] |
| Initial jobless claims (4wk avg) | ~215K (est.) | >260K and rising | DOL Thursday 8:30 ET | Stale |
| DXY (USD index) | Unknown — need live | Rising 4+ consecutive weeks | Bloomberg/FRED | Stale |
| Brent-WTI spread | WTI > Brent (inverted) | <$5 = tidewater scarcity easing | CME/ICE | Apr 3 |
| Cushing inventory | **31.465M bbl** (Mar 27 — counterintuitive BUILD). SPR releases + Canadian imports flowing into hub. Above 20M min. Prior: 27.5M (Mar 13) | <20M bbl = WTI dislocation | EIA WPSR | Mar 27 [EST] |
| ATA Truck Tonnage | Unknown — monthly | YoY negative x 2 months | ATA | Stale |

### Tier 3 — Lagging (You're Late If Waiting)

| Indicator | Status | Notes |
|-----------|--------|-------|
| OPEC+ emergency meeting / unwind | Apr 5: symbolic "paper" increase only. Can't deliver real barrels. Next mtg Jun 7 | Reacts to markets, doesn't lead |
| WTI put/call ratio | Unknown | Options reflect consensus, not edge |
| Refinery margin compression | 3-2-1 crack elevated | Compresses AFTER crude falls |
| Corporate guidance cuts | None yet (Q1 earnings not started) | 1-3 month reporting lag |

---

## DEMAND DESTRUCTION TIMELINE MODEL

Based on historical analogs (ANALOGS.md) and Hamilton framework (HAMILTON.md):

| Phase | Standard Timeline | Front-Loaded 2026 (stressed consumer) | Where We Are |
|-------|-------------------|---------------------------------------|--------------|
| Gas $4 breakpoint | — | — | **BREACHED Apr 2** |
| Consumer behavior shifts | Q3 2026 | **Q2 2026** | Watching — gas just hit $4.08 |
| EIA gasoline -5% YoY visible | 20-24 weeks post-shock | 12-16 weeks (if front-loaded) | **Earliest: May-June** |
| Airline capacity cuts | Leads gasoline data by 4-8 wks | Q2 2026 | **CONFIRMED: UAL -5%, DAL -4%, AAL -6%, ULCCs -10%. Cuts started mid-Mar** |
| ATA Truck Tonnage decline | Leads gasoline data by 4-8 wks | Q2 2026 | Unknown — need data |
| Auto sales collapse | Q3-Q4 2026 | Q2-Q3 2026 | Not yet visible |
| CFTC positioning divergence | 3-4 months before top | — | Backlog cleared. NYMEX net long 73.3K (Mar 31). Need trend |
| All 3 Path B signals fire | — | Earliest May-June | 0/3 fired |
| Phase 2 top (4-6 wks after all 3) | — | Earliest July | — |

### The "No Buffer" Acceleration Risk

2026 consumer profile matches 2008 (not 2022):
- Savings rate: 3.6% (2008: 3-4%, 2022: 6-7%+)
- Credit card delinquency: 12.7% (near 2008 crisis levels)
- Subprime auto: 6.9-7.1% (EXCEEDS GFC peak)
- Excess savings: NONE (depleted Mar 2024)
- NFP: -92K (ALREADY negative — 2008 was positive through H1)

**Implication:** Standard 20-24 week timeline may compress to 12-16 weeks. Hamilton's lag-4 peak effect (Q1 2027) may front-load to Q4 2026. Watch Q2 leading indicators aggressively.

---

## HAMILTON NOPI SCORECARD

| Metric | Value | Source |
|--------|-------|--------|
| Reference price (behavioral) | $75 (2025 range) | Internal |
| Current Brent | $109 futures / $141 physical | Apr 4 |
| Current WTI | $112 | Apr 4 |
| NOPI (at $112 WTI spot) | **40.1** (recalculated Apr 5) | Hamilton model |
| GDP drag estimate | -2.5 to -4.2pp | Hamilton Eq 3.8 (Perplexity/Gemini range) |
| Historical analog | Between 1990 Gulf War (32.6) and 1979 Iran Rev (50.7) | — |
| Peak GDP damage quarter | Q1 2027 (standard) / Q4 2026 (front-loaded) | Hamilton coefficients |
| Q1 2026 close (Mar 31) | Need to verify — critical for NOPI calibration | — |

---

## WEEKLY DATA LOG

Record each week's key readings here. Update Wednesday (post-EIA) and Friday (post-Baker Hughes/COT).

| Week Ending | Gas $/gal | EIA Gas Demand YoY | M1-M3 Spread | COT Net Long | Claims 4wk | DXY | Rig Count | Notes |
|-------------|-----------|-------------------|--------------|-------------|------------|-----|-----------|-------|
| Mar 13 | — | — | — | — | — | — | 553 | Cushing 27.5M bbl. Crude stocks 443.1M |
| Mar 27 | — | — | — | — | — | — | — | Crude stocks 424.4M (-19M draw). Refinery 94.8% util |
| Mar 31 | — | — | — | 73.3K (NYMEX) | — | — | — | CFTC backlog cleared. ICE net short 33.8K |
| Apr 4 | $4.08 | — | ~$8-10 est | — | — | — | 553 | $4 breached. Dated Brent $141. UAL/DAL/AAL cuts confirmed |
| **Apr 3** | **$4.08** | **+0.8% YoY** ⚠️hoarding | ~$8-10 [EST] | — | — | — | 553 | **EIA Apr 8 release.** Crude +3.7M bbl (API; SPR→commercial). Cushing 31.5M bbl (↑ from 27.5M). Util 92.1% (↓2.7pp). SPR 413.3M bbl. Distillate -2.1M bbl (3.2M below 5yr). Imports 6.5Mbpd +12.8%YoY. Refinery inputs 16.6Mbpd ↓219K. ⚠️ Inputs↓ but demand+YoY = HOARDING SIGNAL. See `data/eia_2026-04-08.md` |
| Apr 6 | — | — | ~$18+ est (F1-F2 ~$9.60 [CONF]) | — | — | 99.81 | — | ⚠️ PATH A ALERT: 45-day ceasefire proposal active. Iraqi tanker transited Hormuz Apr 5. Brent ~$109.90, WTI ~$111.54. LNG $282.52, EOG $143.00, USO $137.92. Trump Tuesday deadline. |
| **Apr 10** | — | — | — | **73,347** (Mar 31 [CONF]; Apr 7 pending) | — | — | **545** (−3 WoW) | **COT WATCH:** non-commercial proxy DOWN 20.1K Mar 24→31. Apr 7 data due 3:30pm today — if < 73.3K = Week 1 of 2. Oil rigs ~408 est. Airlines ESCALATING: WestJet -19.6% US ASM, Air NZ 1,100 flt, Ryanair/Lufthansa warnings. Jet fuel $4.88 (+95%). See `data/friday_2026-04-10.md` |
| | | | | | | | | |

---

## MONITORING SCHEDULE

| Day | Time (ET) | Check | Source | Action |
|-----|-----------|-------|--------|--------|
| Monday AM | 9:30 | Brent M1-M3 spread at open | ICE/CME | Log in tracker. If <$5 → alert |
| Monday AM | — | Weekend diplomatic developments | Reuters/AJ | Path A check |
| Tuesday | — | CFTC COT data (prev Tuesday's positions) | CFTC.gov | Log managed money direction |
| Wednesday | 10:30 | **EIA WPSR** — gasoline demand, Cushing, distillate | EIA.gov | KEY DATA DAY. Update tracker |
| Thursday | 8:30 | Initial jobless claims | DOL | Log in tracker |
| Thursday | — | Lloyd's List — P&I coverage changes | Lloyd's List | Path A check |
| Friday | 1:00 | Baker Hughes rig count | Baker Hughes | Log in tracker |
| Friday | — | Airline capacity announcements (weekly review) | IATA/carriers | Tier 2 check |
| Monthly | — | ATA Truck Tonnage | ATA | Tier 2 check |

---

## CROSS-AGENT ROUTING

When demand destruction signals fire, route to:

| Signal | Route To | What They Need |
|--------|----------|----------------|
| Gas >$4.50/gal | **CARL** | Consumer impact — pump price → retail spending → delinquency |
| Gasoline demand -3% YoY (early warning) | **CARL, HENRY** | Pre-recession indicator |
| All 3 Path B triggers fire | **PROME** (all agents) | Phase 2 rotation — exit all energy longs |
| Airline capacity cuts | **CARL** | Employment/travel sector stress |
| Diesel PPI spike | **HENRY** | Inflation input — energy CPI/PPI components |
| Trucking volume decline | **CARL, REGINALD** | Goods-sector demand destruction, commercial lending stress |

---

## KEY REFERENCES

| Document | Location | Contents |
|----------|----------|----------|
| Historical analogs (1990, 2011-12, 2022) | `demand_destruction/ANALOGS.md` | Full timeline analysis of each episode |
| Hamilton NOPI/GDP framework | `demand_destruction/HAMILTON.md` | NOPI=47, GDP drag model, expiration calibration, DD-2/DD-3 results |
| Phase 2 transition matrix | `demand_destruction/TRANSITION_MATRIX.md` | Tier 1/2/3 indicators, combination rule, operational protocol |
| BRENT's matrix review | `demand_destruction/MATRIX_REVIEW.md` | Additions (aviation, claims, ATA), threshold corrections |
| **Oil hoarding research** | `demand_destruction/HOARDING.md` | Who's hoarding, $32 spread decomposition, EIA distortion diagnostics, unwind amplifier analysis |
| Phase 2 short playbook | `research/PHASE2_SHORT_PLAYBOOK.md` | USO put mechanics, OXY bear case, execution protocol |
| KB demand destruction entries | `workbook/KB.tsv` (KB-BRT-022 through 027, 034) | Timelines, EV inelasticity, early warning indicators |

---

*This tracker is the single source of truth for demand destruction monitoring. Update weekly. When all 3 Path B signals fire simultaneously, notify PROME for Phase 2 rotation.*
