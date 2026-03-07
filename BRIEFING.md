# MONDAY BRIEFING — Mar 10, 2026
**Written:** Mar 7, 2026 (Saturday) | **For:** Sunday night / Monday morning review

---

## SITUATION

NFP -92K confirmed. Hormuz Day 7+. Brent $90. WAL $70 (-13%). KRE $64. Account $51.2K (+173% all-time). Cash ~$7,300. Harvested $3,056 on Friday (5 positions closed).

Four TRADE.md files now live (BRENT, REGINALD, HENRY, LABOR). System is producing structured, non-overlapping trade recommendations for the first time.

---

## 🔴 IMMEDIATE ACTIONS (Monday Open)

### 1. SSB $90P Jun — TRIM 50%
**Why:** +125%. REGINALD unanimous: Q1 earnings may look clean because FL UI cliff (Mar 24) hits AFTER Q1 close. Jun theta accelerating. Protect the gain.
**How:** Market order or limit at current mid. GTC limit at $15-16 on remaining 50%.
**Priority:** FIRST action at open.

### 2. WAL Position Confirmation
**Question:** Is $85P Jun still open or was it harvested with $82.5P Jun on Friday?
- We SOLD: WAL $82.5P Jun (+288%), WAL $77.5P Mar 20 (+340%)
- STATUS says $85P Jun at +156% — believed still open. CONFIRM.

---

## 📊 LIVE DATA PULLS (Monday Morning)

| # | Data | Source | Why | Agent |
|---|------|--------|-----|-------|
| 1 | **Brent M1-M3 spread** | ICE / Bloomberg / barchart.com | Phase 2 transition matrix — currently ~$8-10, trigger at <$3 | BRENT |
| 2 | **CFTC COT report** (Friday's data) | cftc.gov (Commitments of Traders) | Managed money net long direction — Phase 2 signal #6 | BRENT |
| 3 | **LNG (Cheniere) options chain** | Broker / options chain | Verify $270C/$300C May spread actual debit cost ($5-8 target) | BRENT |
| 4 | **LNG stock price** | Market | If red day → entry window for debit spread | BRENT |
| 5 | **EOG stock price** | Market | Strike selection for calls (need $10-15 OTM) | BRENT |
| 6 | **Cheniere Q1 earnings date** | lngir.cheniere.com / EDGAR | Determines optimal option expiry | BRENT |
| 7 | **VIX level + term structure** | CBOE / VIX Central | Coiled spring thesis — VIX 23.61 Friday, HENRY expects 30-38 | HENRY |
| 8 | **VVIX + skew** | CBOE | Vol-of-vol signal for VIX 25/35 call spread entry | HENRY |
| 9 | **HY OAS** | FRED (BAMLH0A0HYM2) | Was 297bps Friday — 320bps = HENRY/LIQUID threshold | HENRY |
| 10 | **TLT price** | Market | Stagflation put entry — 10Y sold on jobs miss | HENRY |
| 11 | **Dar es Salaam sulphur spot** | Argus Media | BRT-22: >$800/t within 30 days (was $615-630) | BRENT |
| 12 | **GEX / dealer positioning** | SpotGamma / SqueezeMetrics | Negative gamma confirmation for HENRY | HENRY |

### Earnings Date Verification (not urgent Monday but this week)
| Bank | Estimated | Verify At |
|------|-----------|-----------|
| OZK | Apr 16 (confirmed) | ozk.com/ir |
| WAL | ~Apr 22-24 | ir.westernalliancebancorporation.com |
| EGBN | ~Apr 22-28 | eaglebancorp.com/ir |
| ZION | ~Apr 22-24 | zionsbancorporation.com/ir |
| SSB | ~Apr 22-24 | southstatecorporation.com/ir |

---

## 📅 THIS WEEK'S CALENDAR

| Date | Event | Impact | Action |
|------|-------|--------|--------|
| **Mon Mar 10** | Market open | — | SSB trim, data pulls, position review |
| **Tue Mar 11** | **CPI** | Potential relief rally (green day) → ENTRY WINDOW for LNG spread, EGBN add | HENRY: if hot → stagflation deepens, if cool → crowded hedge unwind risk |
| **Wed Mar 12** | **Initial Claims** | CRITICAL — first clean read post-DHS. >300K = all-agents ORANGE→RED | LABOR: threshold playbook in TRADE.md |
| **Thu Mar 13** | **PCE + GDP + BOJ** | Triple event day. BOJ = SAM carry trade. GDP = recession signal? | HENRY + SAM |
| **Fri Mar 14** | Gas pump stress begins | CARL: peak stress window Mar 14-21 | CARL |
| **Mar 17-18** | **FOMC** | Hold expected. Stagflation language = key. "Patient" = dovish, "vigilant on inflation" = hawkish | HENRY: language matrix in TRADE.md |

---

## 🎯 TRADE PRIORITIES (Ordered)

### Enter This Week (if conditions met)
1. **LNG $270C/$300C May debit spread** — BRENT #1 priority. Enter on red day. Need live chain first. Conviction 4/5.
2. **VIX 25/35 call spread** — HENRY #1 priority. Coiled spring thesis. Need term structure data. Conviction 4/5.
3. **TLT puts** — HENRY #2. Stagflation trade that works without cascade. Conviction 4/5.

### Hold / Monitor
4. **EGBN $25P Jun** — REGINALD 5/5 conviction. Add on bounce to $28-30 (conditional).
5. **All KRE/OZK/ZION** — Hold through earnings wave. No action needed yet.
6. **USO** — Add on 2-3% dip. CPI Tuesday could create entry.

### Conditional (watch for triggers)
7. **CPER add** — only if Dar es Salaam >$800/t or DRC force majeure announced.
8. **KRE $55P Aug add** — only if claims >300K or HY OAS >320bps.

---

## ⚠️ RISK WATCH

- **Hormuz resolution** — any diplomatic signal (Oman/Qatar FM) = exit ALL Phase 1 longs within 4 hours (BRENT Path A protocol)
- **CPI relief rally** — if cool CPI triggers a broad rally, crowded hedges unwind. Use as entry window, not a reason to panic.
- **Claims >300K** — threshold breach. All agents upgrade. Portfolio adds across the board.
- **VIX sub-20** — if VIX falls further despite NFP -92K, the coiled spring thesis needs reassessment.

---

## 🔧 INFRASTRUCTURE TODO

- [ ] HERMES delivery run (backlogged: HAWK 3 outbox + BRENT→SAM v2 + BRENT→HAWK)
- [ ] Run Prompts C & D (fertilizer chain, SPR/transformers)
- [ ] TRADE.md rollout: BROCK, CARL, HAWK
- [ ] HERMES cron automation
- [ ] BRIEFING.md auto-generation concept

---

*Next full briefing rewrite: after FOMC (Mar 18) or on major thesis change.*
