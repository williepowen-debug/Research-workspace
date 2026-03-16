# SCRATCH — Ephemeral Working Memory

**Updated:** 2026-03-16 ~13:30 UTC (Monday)

---

## QUICKSTART
Scenario C, War Day 14. Brent $101.07. Account ~$57K (+187%).
**FOMC MON-TUE, presser WED 2:30 PM ET.** BOJ THU (HOLD, hawkish hold 35-40%).
**PCE 3.1% + GDP 0.7% + NFP -92K = stagflation locked.** SPX 6,632 = CTA trigger breached, $80B systematic selling queued.
**HY OAS 317bps — LIQ-01 NOT triggered (3bps below 320).** Credit absorbing shocks. Jun rolls more urgent.
**Mar 18-19 = max density window:** FOMC decision + TIC data (Mar 18) → 20Y auction + BOJ + Shunto auto Yamaba (Mar 19) → quarter-end (Mar 31).

## SESSION WORK (Mar 16 Monday)
- Morning heartbeat: flagged FOMC/BOJ Super-Week
- Processed overnight briefing (shutdown Day 31, Shuntu pre-settlement, 300+ TSA quits)
- CARL daily check-in: clean, no new data. 0 dots = no consumer relief valve.
- Handoff to fresh session

## SESSION WORK (Mar 15 afternoon)
- Built two-stage agent recon system (Stage 1: gap analysis → Stage 2: live search)
- Dry-ran prompts with HENRY + LIQUID, iterated on feedback
- **Batch 1 complete:** HENRY + LIQUID (Stage 1 + Stage 2 ✅)
- **Batch 2 complete:** SAM + ZHAO (Stage 1 + Stage 2 ✅)
- All findings in `AGENTS/<NAME>/recon/STAGE2_FINDINGS_2026-03-15.md`
- STATUS.md and KB/VX files updated for all 4 agents
- Committed: `3a93894`

## KEY FINDINGS FROM RECON SWEEP

### HENRY
- PCE Core 3.1% YoY (hot vs 2.9% consensus) — Fed can't cut
- SPX 6,632 — first close below CTA trigger (6,707). $80B selling queued.
- UMich 5-10yr 3.2% — de-anchoring confirmed
- IWM $246.59 — $250P ITM by $3.41
- USDJPY 159.7 — carry unwind DELAYED (yen weakened, not strengthened)
- JOLTS 6.9M < 7.5M threshold — labor demand freeze confirmed
- WAL $67.97 — Sep $70P ITM by $2.03

### LIQUID
- HY OAS 317bps (FRED confirmed) — NOT at 320 trigger. War reaction "muted" in HY.
- DIFC: 3 banks (Citi + StanChart + HSBC Qatar), not just Citi
- SOFR 3.65% — repo stable, no SRF trigger
- 20Y auction Mar 19 (same day as BOJ). Settlement Mar 31 = quarter-end.
- Primary credit loans rising (+$2B YoY) — directional concern
- HYG $79.20 — Jun $75P OTM by $4.20

### SAM
- Real wages +1.4% (Jan) — first positive in 13 months. Base salary fastest since 1992.
- Auto Yamaba (Toyota/Honda) due WED MAR 18 = same day BOJ meeting opens
- Reuters BOJ sources: Iran war ACCELERATES hawkish push. Hawkish hold 35-40%.
- JGB 30Y 3.48% (+20bp in 8 days) — approaching life insurer threshold
- JGB 10Y 2.25% — 5bp from YELLOW
- Taiwan LNG 22/22 secured — TSMC curtailment risk reduced this window

### ZHAO
- DXY reversed 99.08 → 100.50 — stronger dollar = more pressure on CNY/KRW
- Japan-Korea JOINT FX STATEMENT Mar 14 — dual anchor confirmed
- Saudi PIF scaling back US equity — first confirmed Gulf capital reallocation
- PBOC gold 16-month streak — defensive wall persists
- USD/CNY 6.91, USD/KRW 1,501 — both anchors under pressure
- Hormuz selectively open to non-Western vessels (Turkish ship Mar 13)

## 🔴 OPEN ITEMS (PRIORITY ORDER)

### Market Open Monday
1. **Jun→Dec rolls** — KRE, WAL, HYG, APO, IWM. Green day needed. WAL $85P Jun (+179%) first.
2. **APO Apr (+34%)** — roll or exit, near-term expiry risk
3. **Dead money cuts** — VLY Mar20 (expires THIS WEEK), OWL Apr, EGBN Jun
4. **HY OAS Monday FRED update** — Mar 13 data releases Mar 16. Could flip LIQ-01.

### Agent Recon (remaining batches)
5. **Batch 3: CARL + LABOR** — next up. Both have Thu claims catalyst.
6. **Batch 4: BRENT + HAWK** — oil + geopolitical. War Day 14, Kuwait curtailment Fri.
7. **Batch 5: REGINALD + BROCK** — banks + private credit. Earnings approaching.
8. **Batch 6: MARCO + OTTO** — migration + auto DQ.
9. **Batch 7: HANS** — Europe. Stage 1 only may be sufficient.

### Research/System (from prior session, still open)
10. **Ceasefire unwind playbook** — low urgency given escalation, but needed eventually
11. **Russia sanctions relief modeling** — RED flagged
12. **Quarter-end repo stress (Mar 31)** — RRP buffer gone
13. **Will's new signals** — he mentioned having signals to process

### Parked
- Thesis deck — evidence + outline complete, slides TBD
- Publishing research (Memo Item 3 first piece)

## CONFIRMED DATA BLOCK (inject into remaining agent prompts)
```
- Brent: $101.07 (Mar 13 close)
- SPX: 6,632.19 (Mar 13 close, 2026 low, below CTA trigger 6,707)
- VIX: 27.19 (Mar 13 close)
- 10Y yield: ~4.25% (Mar 13)
- TLT: $86.56 (Mar 13 close)
- IWM: $246.59 (Mar 13 close)
- USDJPY: 159.717 (Mar 13 close)
- DXY: 100.50 (Mar 14, reversed from 99.08)
- USD/CNY: 6.91 (Mar 14)
- USD/KRW: 1,501 (Mar 14)
- HY OAS: 317bps (Mar 12, FRED confirmed). LIQ-01 NOT triggered.
- SOFR: 3.65% (Mar 12). Repo stable.
- PCE Core Jan: +3.1% YoY (hot vs 2.9% consensus)
- GDP Q4 revised: 0.7%
- UMich 5-10yr inflation expectations: 3.2% (de-anchoring)
- JOLTS Jan: 6.9M (below 7.5M threshold)
- Real wages Jan: +1.4% (first positive in 13 months)
- BOJ: expected HOLD Mar 19. Rate 0.75%. Hawkish hold 35-40%.
- FOMC: Mon-Tue, presser Wed 2:30 PM ET. Dots likely 0-1 cuts.
- TIC Jan 2026: releases Mar 18 (same day as FOMC decision)
- 20Y auction: Mar 19 (same day as BOJ). Settlement Mar 31.
- DIFC: Citi + StanChart evacuated, HSBC closed Qatar branches
- Japan-Korea joint FX statement Mar 14
- Taiwan LNG: 22/22 March-April cargoes secured
- Shunto auto Yamaba (Toyota/Honda): due Wed Mar 18
- Saudi PIF: scaling back US equity holdings (first confirmed Gulf reallocation)
- PBOC gold: 16-month buying streak, 2,308 tonnes
```

## Handoff
**Last context:** Monday Mar 16 ~1:30 PM UTC. Super-Week starts TOMORROW. CARL check-in clean (no new weekend data). Overnight briefing processed: shutdown Day 31 (300+ TSA quits, airline CEO coalition lobbying), Shuntu pre-settlement signals strong (Mar 18 = main settlement day, 5.94% demand). Agent recon Batches 1-2 done (HENRY, LIQUID, SAM, ZHAO). Batches 3-7 still open.
**Next tide:**
1. **IMMEDIATE:** HY OAS FRED update — Mar 13 data should post today. 317bps last. 320 = LIQ-01 trigger.
2. **IMMEDIATE:** Jun→Dec rolls — need a green day. WAL $85P Jun (+179%) first priority.
3. **IMMEDIATE:** Dead money — VLY Mar20×10 expires THIS FRIDAY (-41%). Cut or let expire? OWL Apr (-29%), EGBN Jun (-36%) also flagged.
4. **TODAY/TUE:** Retail Sales Feb releases Mar 17 (same day FOMC opens). If negative again, compounds stagflation.
5. **FOMC:** Mon-Tue, presser Wed 2:30 PM ET. Dots 0-1 cuts. PCE 3.1% + GDP 0.7% = trapped.
6. **BOJ:** Mar 18-19. Shuntu auto Yamaba (Toyota/Honda) Mar 18 = same day. Ueda presser Mar 19.
7. **Agent recon:** Batch 3 CARL+LABOR next. Then 4-7.
8. **Will's signals:** He mentioned having new signals to process (Sunday). Still pending.
**Open questions:** HY OAS level. Roll execution timing. Remaining recon batch depth.
**Positions:** No changes. VLY Mar20 expires Fri.
**Rhythm note:** Monday, Super-Week. Will engaged and prepped. Execution mode.
