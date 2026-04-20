# MEMORY.md — HAWK Cross-Session Memory

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or delete, never just accumulate.*

---

## Feedback
- [2026-02-18] VIX event trades on geopolitical catalysts have poor risk/reward (Aug 2024 lesson: 85% of VIX 65 spike was artificial). Equity puts (direct sector exposure) are better expression than VIX calls.
- [2026-02-18] Refiners already priced — VLO above consensus target, ceasefire risk enormous. Position sizing must account for binary event risk.
- [2026-04-01] Ceasefire fade protocol validated: 0/3 "diplomatic breakthroughs" were real (all Tier 4). Extension framing as "diplomacy working" was narrative trap.
- [2026-04-01] Phase 5 activation (Houthi entry + multi-front war) invalidated C scenario assumptions. Controlled burns framework requires bilateral conflict + Hormuz bypass intact — both now false.

## Findings
- [2026-04-01] **ADCOP fire = Hormuz bypass architecture eliminated.** No safe Gulf crude export route exists. This is structural, not tactical.
- [2026-04-01] **Kuwait strike = non-combatant targeting.** Iran abandoned bilateral conflict framing; now regional war with 3 Gulf states under direct attack.
- [2026-04-01] **AWACS destruction = $300M US asset loss on allied soil.** Raises domestic US political pressure to escalate, not de-escalate.
- [2026-04-01] **Al Taweelah/EGA = aluminium supply shock (4% global).** New commodity vector beyond oil/gas/fertilizer/helium.
- [2026-04-06] **WTI > Brent inversion.** Hormuz closure Day 36 causing physical supply squeeze. Asia/Europe paying $30-40/barrel premiums for US crude.
- [2026-04-06] **Petrodollar loop fractured.** 50-year Kissinger 1974 deal breaking — US as combatant, not stabilizer; Gulf SWFs rethinking US investments.
- [2026-04-14] **IMF GFSR confirms stress.** Global equities down 8% since Feb; sovereign yields risen sharply; private credit explicitly named as vulnerability channel.
- [2026-04-14] **Baker Hughes rig count flat despite elevated oil.** US shale NOT rushing to fill gap; standard elasticity model predicts ~90 days lag. Supply response absent.

## References
- [2026-04-01] Hormuz status tracker: `domain/OIL_FACILITY_DAMAGE_TRACKER.md`
- [2026-04-01] Ceasefire fade protocol: `workbook/CEASEFIRE_FADE_PROTOCOL.md`
- [2026-04-01] Four structural breaks framework: `workbook/FOUR_STRUCTURAL_BREAKS_MAR18.md`
- [2026-04-14] IMF GFSR April 2026: https://www.imf.org/en/publications/gfsr/issues/2026/04/14/global-financial-stability-report-april-2026
- [2026-04-14] Baker Hughes rig count: Weekly North America Rotary Rig Count (bakerhughes.com)
- [2026-04-20] Brent price source: FORGE/tools/market-data/ or `python3 FORGE/tools/market-data/fetch.py price BRENT`

## Session Notes

### CHANGES SINCE LAST SESSION (Apr 1 → Apr 20)
- **Ceasefire declared Apr 12-13:** Israel-Iran ceasefire announced after 43 days of war. Trump administration brokered deal.
- **Brent collapsed to $64.50:** From $108-116 range (Day 32) to ~$64.50 — one of the sharpest oil collapses on record. War risk premium fully evacuated.
- **Scenario D reduced to 82%:** From 92% at Day 32. Ceasefire + supply response expectations = de-escalation pricing.
- **4 inbox signals unprocessed (Apr 6-14):**
  - Apr 6: Hormuz supply squeeze (WTI premiums explode)
  - Apr 6: Petrodollar fracture thesis
  - Apr 14: IMF GFSR liquidity dysfunction warning
  - Apr 14: Baker Hughes rig count flat despite elevated oil
- **Infrastructure gaps identified:** No CALENDAR.md, no thesis/ folder, no automation scripts (unlike SAM which has scripts/ toolkit).

### LAST SESSION (Apr 1)
- **Status frozen at Day 32, Scenario D 92%, Brent $108-116.**
- **6 signals processed in batch:** Phase 5 fully active, 3 Gulf states under attack, Apr 6 deadline 5 days out.
- **Key actions:** Raised D to 92% (largest shift since Day 18), flagged ceasefire fade protocol to RED, updated facility damage tracker with ADCOP/Al Taweelah/Kuwait strikes.
- **Convergence:** 45/45 🔴🔴 MAXIMUM at session end.
- **Outgoing:** Routed signals to CARL (gas prices), SAM (Japan energy), LIQUID (risk-off), HENRY (vol), BRENT (infrastructure), RED (ceasefire fade).

### NEXT SESSION
1. **Process 4 unprocessed inbox signals (Apr 6-14):** Hormuz squeeze, petrodollar fracture, IMF GFSR, Baker Hughes rig count. Assess post-ceasefire relevance.
2. **Reassess scenario probabilities:** Ceasefire changes D/C/B weights. Need fresh framework for "post-war" monitoring (spoiler: war risk ≠ zero, just repriced).
3. **Build CALENDAR.md:** Forward-looking catalyst tracker (like SAM's). Key dates: OPEC+ meetings, US-Iran follow-up talks, Israeli nuclear program inspections.
4. **Create thesis/ folder:** Capture post-ceasefire HAWK thesis — what ends the ceasefire? What monitoring framework replaces "war day" tracking?
5. **Automation scripts:** Port SAM's `boot.py` pattern to HAWK — `scripts/hawk_boot.py` for one-command morning refresh of oil prices, rig count, geopolitical feeds.
6. **Cross-agent update:** Signal to BRENT (primary oil now), SAM (Japan energy import pricing post-collapse), LIQUID (risk-on/risk-off regime shift), RED (ceasefire durability assessment).
7. **Facility damage reassessment:** Which infrastructure is actually repaired? Qatar LNG, ADCOP pipeline, Al Taweelah — duration estimates vs. reality.
