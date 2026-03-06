# MEMORY — Key Insights & Lessons

**Last Updated:** 2026-03-06 16:45 UTC

---

## CORE DISCOVERIES

### Hidden CRE (Memo Item 3) — Feb 22-23
Banks hide CRE in C&I via FFIEC Schedule RC-C Memo Item 3 (RCON2746). Metropolitan Capital failed with 61% true CRE (labeled 10.7%). Three masking levels: extend-and-pretend, mark-to-model, **classification** (our discovery).

**Screen results:** OZK 37.6% (worst), WAL 24.2% (growing), EGBN 23.7%. Clean: ZION 1.8%, SSB 0.9%.

**How to screen:** Pull Call Report RC-C Part I → Item 4 (C&I) → Memo Item 3 → ratio >20% = flag.

### WAL Thesis (Grade: A+)
$2.73B hidden CRE, ratio GROWING (15.5% → 24.2%), management confirmed relabeling on call. 474% CRE/Tier 1. NDFI removed as risk (68% mortgage warehouse). Three vectors: hidden CRE, Jefferies double-pledging, SSFA arbitrage ($17.2B).
*Detail → `FORGE/WAL/STATUS.md`*

### OZK 10-K Verified — Feb 25
Construction reserves CUT 41% while losses accelerated. Illinois = 67% NPLs. $19B unfunded > $14B liquidity. All C-suite selling, zero insider buys. SI 14-15% (crowded — WAL less crowded at 4.4%).
*Detail → `AGENTS/REGINALD/OZK/`*

---

## THESIS FRAMEWORK

### Consumer Finance Broken (Feb 16)
All 5 consumer names (SYF/BFH/ALLY/CACC/AFRM) showed improvement. **K-Shape:** underwater homeowners ≠ employed cardholders. Housing → banks directly, bypasses consumer credit. Consumer credit only cracks if employment cracks (>250K claims).

### Two-Phase Oil (Feb 18)
Phase 1 (Feb-Mar): Supply squeeze → tankers (STNG/TNP). Phase 2 (Apr-May): 140M barrel flush → short crude. Alpha is the sequencing.
*Detail → LIQUID/HAWK STATUS.md*

### RED Team (Feb 14) — 80% Confidence
Betting on ACKNOWLEDGMENT of existing stress, not predicting new stress. 5 transmission paths. Falsification: exit 50% if claims <240K + CBRE >-5%; exit 100% if BTFP 2.0 / HY OAS <260bps.
*Full report → `AGENTS/RED/RED_TEAM_REPORT_2026-02-14.md`*

### Session Management Protocol — Mar 5-6
`/clear` stacks compaction summaries (lossy). Observed: 17% → 54% → 56% → 65% across 4 clears. Practical limit: 2-3 clears before `/new`. Two-tier handoff: checkpoint (quick block + git commit) before `/clear`, full handoff (daily notes + STATUS + MEMORY + push) before `/new`.

### Agent Schema Standardization — Mar 5-6
REGINALD's TSV schemas are the gold standard. HENRY migrated to match: VX (7→12 cols with Y/O/R thresholds), KB (7→14 cols with Entity/Data_Quote/Thesis_Impact), FLOW (5→10 cols with Speed/Layer/Status/Current_Position), PREDICTIONS (+Invalidation). Key win: agents now have mechanically triggerable vectors instead of vibes-based status calls.

### TRADE.md Concept — Mar 6
Per-agent trade targets from siloed research. Each domain maintains specific targets based on their analysis. Synthesize at PROME level. Not yet codified.

### Convergence Day — Feb 27 (MAJOR)
Best single day of thesis confirmation. Multiple independent vectors fired simultaneously:

**New signals discovered via EOD agent run:**
- **MFS Collapse (UK):** £2B fraud, double-pledging. Barclays £600M, Jefferies £100M, Apollo/Atlas SP exposed. Reuters "cockroach" framing. Drove bank rout.
- **Apollo Triple Stress:** MFIC dividend cut (2nd BDC in 48hrs) + Atlas SP/MFS + Medallia 78¢. Most exposed alt manager. Athene insurance = Stage 4 risk.
- **Block 4K Layoffs:** 50% of workforce, AI-cited. Leading indicator for white-collar labor.
- **H.8 Systemic:** CRE +1.1% (from +5.9%), C&I +14.4%. Industry-level Memo Item 3 reclassification CONFIRMED.
- **Credit Widening:** HY OAS 2.98% (+12bps/week). First sustained widening off Jan tights.
- **PPI Core +0.8%** (2.6x expected). Fed trap closed — can't cut into hot inflation while employment cracks.

**Key conclusion:** Private credit → bank equity transmission is LIVE. MFS → Jefferies/Barclays → sector derisking → WAL -10.64%. WAL had NO specific catalyst — pure vulnerability premium.

**New watchlist:** APO puts (very high conviction).
**Threshold:** HY OAS 320bps = credit transmission confirmed.

### Energy Dominance Thesis — Mar 2 (WILL'S INSIGHT)
US running integrated supply consolidation: Venezuela (blockade/regime change) + Iran (strikes/Hormuz) + Russia (Ukraine drone campaign, 58+ refinery strikes) + ghost fleet crackdown (623 vessels sanctioned 2025). MBS/Trump financial alignment (crypto, Kushner/PIF). Saudi is last man standing BY DESIGN. Not temporary war premium — structural repricing over 2-3 months. 16M+ bpd at risk across all theaters.
*Detail → `HAWK/domain/sources/OIL_INFRASTRUCTURE_DISRUPTIONS.md` + `ENERGY_DOMINANCE_STRATEGY.md`*

### NEXUS Agent Created — Mar 2
Synthesis engine. Cross-agent convergence detection. 5 frameworks. Catches patterns individual agents miss (SAM×ZHAO synch stress, etc). First run seeded with 4 convergences, 2 contradictions, threshold proximity matrix.

### APO + AAL + OZK + WAL + STNG Entered — Mar 2
6 new positions. APO $100P Jun ($770), AAL $10P Jul x4 ($227), OZK $45P Aug x2 ($663), WAL $77.5P Jun ($551), STNG 2 shares ($156), USO $90C Mar 13 ($287). Sold PLTR/INVH/SSB/1xKRE to fund.

### Eisman/Gober Confirms BROCK Thesis — Mar 2
Podcast Ep 48: PE/insurance = "slow boiling frog." Athene **$37.9B deposit-type contracts** (duration mismatch = run risk). Affiliated paper $10B→$40B. Captive financials: $7B liabilities vs $200M real assets. Sellside analysts covering APO are NOT insurance analysts — nobody reads statutory filings. Eisman sees the structure but not the trigger. We see both (war + credit cycle = catalyst).
*Detail → `BROCK/domain/sources/EISMAN_GOBER_TRANSCRIPT_ANALYSIS_MAR2.md`*

### LNG Crisis + Three-Anchor UST Stress — Mar 2
QatarEnergy halted ALL production. TTF +45%. **Insurance cliff Mar 5** — Hormuz UNINSURABLE after Thursday. ZHAO upgrades to three-anchor stress (Japan + China + Korea): combined UST selling $50-70B/month. USD/CNY 7.30 now 2-4 weeks. HANS: Ukraine ceasefire Mar/Apr base case (85%), Russia max leverage.
*Detail → `HAWK/domain/sources/LNG_DISRUPTION_MAR2.md`, `HANS/sources/RP-HANS-10`*

### Mar 5 > NFP Friday — Mar 2
Insurance withdrawal date is the most important catalyst this week. If Hormuz becomes uninsurable, disruption is structural regardless of military situation. Takes weeks to reinstate coverage even if fighting stops.

### NFP -92K — Thesis Confirmed — Mar 6
First negative NFP this cycle. Dec revised to -17K (two negative months). Stagflation locked: earnings +3.8% YoY, Fed can't cut. WAL -13% ($70), KRE -3.6% ($64). Harvested 5 short-dated positions for $3,056 realized profit (+183% to +340%). Account $51.2K, +173% all-time. **Rule validated: harvest short-dated on red days, re-enter on green days.**

### Poisoned Reference Files — Mar 6
Agent self-audit (BROCK) discovered EXPECTED_SIGNALS.md still contained PSEC PIK at 35% (corrected to 8.6% months ago) and FSK dividend at $0.70 (cut to $0.48). BDC_CASH_COVERAGE.tsv had same problem. **Lesson: separate methodology from live data.** Methodology docs should contain thresholds/interpretation only, never current values. Live data lives in STATUS.md + VX.tsv. Agent self-audits catch things Prome misses — high value practice.

### Hormuz Storage Crisis — Mar 6
Kuwait/Qatar curtailing production — can't export, storage filling. If Hormuz stays closed 4 weeks, ALL Gulf producers (Iraq, Kuwait, UAE, Qatar) forced to shut wells. Brent $90. Iran FM: "no ceasefire, no negotiations." HAWK scenario C raised 20→35%.

---

## CHART ANALYSIS (Feb 24)

**6-bank watchlist:** KRE, WAL, OZK, ZION, FLG, EGBN — all topped Feb 2026 and reversed. GFC 2007 is the template (slow grind), not SVB (shock). KRE P/C ratio 2.27 (institutional confirmation). Confidence 75-80% this is THE TOP, but Feb new high complicates pattern.
*Detail → `FORGE/STATUS.md`*

---

## SYSTEM ARCHITECTURE (Mar 4-5)

- **INBOX siloed from spawn protocol.** Agents don't check inbox on normal tasks — separate spawn for inbox processing. Different cognitive mode = silo it.
- **Reply rule:** Only reply to signals if (a) new info sender doesn't have, (b) error correction, or (c) threshold trigger. Silence = received and integrated.
- **Inbox = folder, not file.** Individual signal files in `inbox/`, move to `inbox/processed/` when done. Standardized across all 13 agents.
- **Root TSVs are canonical.** workbook/ is archive/reference. When in doubt, root files are source of truth.
- **Agent STATUS.md ≤250 lines.** Archive resolved analysis to workbook, keep STATUS as a dashboard.
- **HERMES delivers signals.** Agents write to OUTBOX, HERMES runs 2x daily (9AM + 5PM ET) to deliver.
- **Stale data rules in CLAUDE.md.** Skip VX.tsv rows >5 trading days old. Pull live before citing STATUS values >24h old.

---

## KEY CORRECTIONS (Persistent)

- OZK next earnings: **April 16, 2026**
- NYCB rebranded to **FLG (Flagstar Financial)** Oct 2024
- CMA bought by **FITB (Fifth Third)**, Feb 2, 2026
- PSEC PIK was **8.6%**, not 35% (agent hallucinated)
- Always verify agent data against primary SEC filings before trading

---
