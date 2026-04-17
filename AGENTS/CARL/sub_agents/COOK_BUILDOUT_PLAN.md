# COOK Sub-Agent Buildout Plan

**Agent name:** COOK
**Domain:** Food cost + food security + SNAP/safety-net erosion
**Status:** PLANNED — not yet built
**Plan authored:** 2026-04-17 PM#3 (CARL)
**Target execution:** Next session

---

## WHY COOK

CARL's thesis explicitly cites food CPI as a load-bearing vector in the multi-vector cost squeeze ("triple nitrogen seizure, Q3-Q4 impact"), yet CARL tracks it directly with no dedicated watcher. Food is the **most sensitive bottom-60% canary** because:

- Non-deferrable and non-substitutable at the subsistence margin
- SNAP covers ~42M Americans — biggest single safety net by headcount
- OBBBA SNAP cuts load H2 2026 (ABAWD work rules, state match FY2027)
- Food-at-home CPI hits bottom quintile ~2x as hard as headline CPI
- **Pairs with DOC on OBBBA safety-net erosion:** Both SNAP cuts AND Medicaid redeterminations activate H2 2026. Two safety nets eroding in parallel = thesis-level convergence event.

Name rationale: **COOK** is short/punchy (matches DOC, POP, GIG), evocative of home kitchen and household food prep, and broader than PANTRY (covers both cost and access channels without cupboard-specific frame).

---

## SCOPE

**COOK owns:**
- Food-at-home CPI + subcomponents (eggs, meat, dairy, produce, cereals, beverages)
- Food-away-from-home CPI (substitution pressure signal)
- Grocer gross margin + mix trends (KR, ACI, WMT, COST, TGT, DG, DLTR)
- Private label share and trade-down behavior
- Commodity-to-retail lag tracking (corn, wheat, soy, cattle, hogs)
- SNAP enrollment + benefit levels (USDA FNS monthly)
- OBBBA SNAP implementation (ABAWD rules, state match, asset test, work requirements)
- School lunch / WIC / Meals on Wheels program changes
- Food bank demand (Feeding America + local)
- Household food insecurity rates (USDA ERS)
- Dollar store food category growth as trade-down proxy

**COOK does NOT own:**
- Restaurant bankruptcies / closures → POP
- Healthcare cost stress → DOC
- Housing / rent stress → HOMER
- Broader consumer credit stress → CARL direct

---

## THREE-PHASE BUILD

### Phase 1 — CARL scaffolds the agent (~10 min, Opus, ~$0.10)

CARL creates directory structure and writes agent instructions directly:

```
sub_agents/COOK/
  CLAUDE.md              # Agent instructions (adapted from POLLY/POP template)
  STATUS.md              # Dashboard skeleton with [INIT-PENDING] placeholders
  workbook/
    SCHEMA.tsv           # 13-column standard adapted
    VX.tsv               # Headers only
    ML.tsv               # Headers only
    FLOW.tsv             # Headers only
    PREDICTIONS.tsv      # Headers only with 4-6 initial predictions
    SNAP_STATE.tsv       # State-level SNAP enrollment (FL/TX/CA/NY priority)
    GROCER_MIX.tsv       # Grocer earnings mix data
    COMMODITY_LAG.tsv    # Commodity → retail transmission
  sources/               # Empty
  archive/               # Empty
```

CARL CLAUDE.md content areas:
- Role + relationship to CARL
- Key signals (cost channel + access channel + behavioral)
- Thresholds (see draft below; validate in Phase 2)
- Data sources table
- File structure
- State vector protocol
- Key concepts: terminal-stress canary, OBBBA parallel with DOC, K-shape relevance
- CARL cross-references

Also:
- Update `AGENTS/CARL/TEAM.md` — add COOK row to roster
- Update `AGENTS/CARL/CLAUDE.md` sub_agents line — register COOK

### Phase 2 — Sonnet sub-agent initial data pull (~15 min, ~$0.10-0.15)

Spawn COOK in "INITIAL DATA PULL" mode (variant of DATA REFRESH starting from empty).

Priority order for the spawn:

1. Food-at-home CPI March 2026 + all subcomponents (BLS)
2. SNAP enrollment latest USDA FNS monthly data
3. OBBBA SNAP implementation specifics (ABAWD work rules effective date, state match phase-in, asset test restoration, refugee/asylee)
4. Feeding America latest quarterly pulse / pressers since Jan 2026
5. Grocer Q4 2025 / Q1 2026 earnings: KR, ACI, WMT, COST, TGT, DG, DLTR — gross margin, private label %, mix commentary
6. Commodity snapshot: corn, wheat, soy, cattle, hog futures + retail lag status

Deliverables:
- Replace `[INIT-PENDING]` with real numbers in STATUS.md
- Populate VX rows for each vector, ML entries, SNAP_STATE, GROCER_MIX, COMMODITY_LAG
- Calibrate thresholds against actuals, flag any adjustments needed
- Note threshold breaches prominently at top of STATUS.md

**Scope discipline:** TIGHT initial pull — national-level cornerstones only. State-level SNAP detail and grocer deep dives defer to subsequent refreshes.

### Phase 3 — CARL synthesis + close (~5 min, Opus, ~$0.05)

1. Read COOK STATUS output — scan for breaches, status colors, material findings
2. Check OBBBA safety-net convergence with DOC as hypothesized dominant cross-domain signal
3. Add KB entry(ies) to CARL KB.tsv for thesis-relevant findings (1-2 entries likely)
4. Update CARL STATUS.md only if thesis-level shift warranted (likely not from initial build)
5. Update SCRATCH.md with build completion
6. Commit + push: `CARL: COOK sub-agent built (food + SNAP stress)`

---

## INITIAL THRESHOLDS (validate in Phase 2)

| Metric | Current (est.) | Yellow | Orange | Red | Source |
|--------|----------------|--------|--------|-----|--------|
| Food-at-home CPI YoY | ~3.0% (Mar 2026) | >4% | >6% | >8% | BLS |
| Egg CPI YoY | ~8% | >15% | >30% | >60% | BLS (volatile — own threshold) |
| SNAP enrollment | ~42M | Decline from benefit cut | 5%+ decline | 10%+ decline | USDA FNS |
| Food insecurity rate | ~13.5% | >14% | >16% | >18% | USDA ERS |
| Feeding America visits YoY | +8% (2025) | >10% | >15% | >20% | Feeding America |
| Dollar store food growth | ~6% | >8% | >12% | >15% | DG/DLTR earnings |
| Grocer GM compression | Stable | -50bp | -100bp | -150bp | KR/ACI/WMT |

---

## INITIAL PREDICTIONS (validate in Phase 2)

| ID | Prediction | Confidence | Timeframe |
|----|-----------|-----------|-----------|
| COOK-P01 | Feeding America Q3 2026 visits will exceed 2020 pandemic peak | 65% | Q3 2026 |
| COOK-P02 | Food-at-home CPI reaccelerates to >4% YoY by Q4 2026 | 60% | Q4 2026 |
| COOK-P03 | SNAP enrollment declines 5%+ from peak by Q2 2027 under OBBBA | 70% | Q2 2027 |
| COOK-P04 | Dollar stores outperform grocers in comparable food category growth FY2026 | 75% | FY2026 |

---

## TRANSMISSION TO CARL (initial cascade map)

| Cascade | Mechanism | Lag | Cross-agent tie |
|---------|-----------|-----|-----------------|
| Cost squeeze | Food-at-home +X% → bottom-60% budget exhaustion → CC/BNPL stacking | Immediate | CARL direct, PHAN |
| SNAP cut | OBBBA ABAWD/state match → enrollment drop → grocery sales drop | 30-90d | POP (grocers), HOMER (landlord rent in SNAP-heavy ZIPs) |
| Food bank exhaustion | Demand >> supply → families defer other bills → CC DQ | 60-120d | CARL CC DQ, STUE (student loan deferral) |
| School lunch cuts | Household food burden ↑ → energy/rent tradeoff | School-term | HOMER rent cascade |
| OBBBA safety-net parallel | SNAP + Medicaid both erode H2 2026 simultaneously | H2 2026+ | **DOC (Medicaid side) — thesis convergence** |

---

## DECISIONS DEFERRED TO EXECUTION TIME

- Whether to split SNAP into separate agent later (current plan: keep unified — simpler and coherent)
- Depth of initial pull (current plan: TIGHT — national cornerstones only)
- Whether to preemptively write outbox signal to PROME on OBBBA convergence (current plan: WAIT for COOK's numbers first)

---

## EXECUTION CHECKLIST (for next session)

- [ ] Read this plan at boot
- [ ] Phase 1: Build scaffolding
  - [ ] mkdir sub_agents/COOK/ with workbook/ sources/ archive/
  - [ ] Write COOK/CLAUDE.md
  - [ ] Write COOK/STATUS.md skeleton
  - [ ] Write SCHEMA.tsv + empty workbook TSVs with headers
  - [ ] Update AGENTS/CARL/TEAM.md (add COOK row)
  - [ ] Update AGENTS/CARL/CLAUDE.md (register COOK in sub_agents files listing)
- [ ] Phase 2: Spawn COOK in INITIAL DATA PULL mode (Sonnet)
- [ ] Phase 3: Synthesize
  - [ ] Read COOK STATUS output
  - [ ] Check OBBBA convergence signal strength vs hypothesis
  - [ ] Add CARL KB entries for material findings
  - [ ] Update CARL SCRATCH
  - [ ] Commit + push

---

*Plan authored CARL Apr 17 PM#3. Will approved name "COOK." Execute next session.*
