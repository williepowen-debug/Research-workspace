# SAM HANDOFF TEMPLATE

**Purpose:** Standardized session-to-session knowledge transfer for SAM agent.
**Based on:** I-PASS healthcare handoff protocol, adapted for macro analysis.
**Methodology Compliance:** CARL Methodology Skeleton v0.2

---

## Template Structure

```yaml
handoff:
  # === IDENTITY ===
  session_number: "SAM-[Roman Numeral]"  # e.g., SAM-IX, SAM-X
  created_at: "[Date, Time EST]"
  
  # === I: THESIS STATUS (Illness Severity) ===
  thesis_status: "[VALIDATED | CONTESTED | UNCERTAIN | INVALIDATED]"
  urgency: "[ROUTINE | ELEVATED | CRITICAL | EMERGENCY]"
  summary_sentence: |
    [One sentence capturing the current state of the thesis and key situation]
  
  # === SCENARIO PROBABILITIES ===
  scenarios:
    A_soft_landing:
      probability: "[X]%"
      trend: "[↑ | ↓ | →]"
      trigger_distance: "[How close to trigger]"
    B_controlled_chaos:
      probability: "[X]%"
      trend: "[↑ | ↓ | →]"
      trigger_distance: "[How close]"
    C_acute_panic:
      probability: "[X]%"
      trend: "[↑ | ↓ | →]"
      trigger_distance: "[How close]"
    D1_austerity:
      probability: "[X]%"
      trend: "[↑ | ↓ | →]"
      trigger_distance: "[How close]"
    D2_monetary_dominance:
      probability: "[X]%"
      trend: "[↑ | ↓ | →]"
      trigger_distance: "[How close]"
  
  probability_reasoning: |
    [Why probabilities are at current levels; what shifted since last session]
  
  # === P: CURRENT STATE SUMMARY (Patient Summary) ===
  current_state:
    crisis_phase: "[Pre-Crisis | Crisis Forming | Active Crisis | Resolution]"
    primary_vector: "[Which vector is dominant right now]"
    
    vector_summary:
      red: [count]
      orange: [count]
      yellow: [count]
      green: [count]
    
    key_thresholds:
      - metric: "[Name]"
        current: "[Value]"
        threshold: "[Level]"
        distance: "[Gap]"
        status: "[🔴|🟠|🟡|🟢]"
    
    key_developments:
      - development: "[What happened]"
        significance: "[Why it matters]"
        documented_in: "[ML-JPN-###]"
    
    flows_active:
      - "[FLOW-JPN-X.XX]: [Status]"
  
  # === A: ACTION LIST ===
  priority_actions:
    - priority: 1
      task: "[Specific, actionable task]"
      reason: "[Why this matters]"
      deadline: "[When it needs to happen]"
      relevant_entries: ["[ML/FL IDs]"]
    - priority: 2
      task: "[Specific, actionable task]"
      reason: "[Why this matters]"
  
  monitoring_focus:
    hourly: ["[Metrics to check hourly]"]
    daily: ["[Metrics to check daily]"]
    weekly: ["[Metrics to check weekly]"]
  
  # === S: SITUATION AWARENESS (Contingencies) ===
  contingencies:
    - trigger: "[If this happens]"
      response: "[Do this]"
      scenario_impact: "[Which scenarios affected, how]"
      escalate_to: "[Which coordinating agents]"
  
  approaching_triggers:
    - trigger: "[Which scenario/flow trigger]"
      metric: "[What to watch]"
      current_distance: "[How close]"
      expected_timing: "[When it might fire]"
  
  catalysts_to_watch:
    - "[FL-JPN-###]: [Description, date]"
  
  invalidation_watch:
    - criterion: "[Which invalidation criterion]"
      current_distance: "[How close to firing]"
      would_indicate: "[What it would mean if fired]"
  
  # === S: SYNTHESIS (for next session) ===
  key_mental_model:
    core_thesis: |
      [The fundamental claim in one paragraph - what SAM believes is happening]
    what_matters_most: |
      [Single most important thing to understand right now]
    biggest_uncertainty: |
      [Primary unknown that could change the assessment]
    where_we_might_be_wrong: |
      [Devil's advocate perspective - what could invalidate current view]
  
  synthesis_questions:
    - "[Question next session should be able to answer from this handoff]"
    - "[Question testing understanding of current priorities]"
    - "[Question about scenario probability reasoning]"
  
  # === COORDINATION ===
  state_vectors_sent:
    - to_agent: "[LIQUID | REGINALD | MASTER]"
      content: "[What was communicated]"
      response_needed: "[Yes/No]"
  
  state_vectors_expected:
    - from_agent: "[Agent name]"
      content: "[What we need from them]"
      deadline: "[When]"
  
  # === CONTEXT LOADING ===
  files_to_load:
    - "[File names for next session]"
  
  essential_entries:
    - "[ML/FL/FLOW IDs that next session MUST review]"
  
  # === META ===
  session_accomplishments:
    - "[What this session accomplished]"
  
  errors_and_revisions:
    - "[Any mistakes made and corrected]"
    - "[Any dead ends explored]"
  
  open_questions:
    - "[Questions that emerged but weren't resolved]"
```

---

## Example: SAM-IX Handoff (Jan 20, 2026)

```yaml
handoff:
  # === IDENTITY ===
  session_number: "SAM-IX"
  created_at: "2026-01-20, 5:32 PM EST"
  
  # === I: THESIS STATUS ===
  thesis_status: "VALIDATED"
  urgency: "EMERGENCY"
  summary_sentence: |
    JGB bond crisis has opened new fiscal sustainability vector; 30Y at all-time 
    high, 20Y auction failed, thesis evolved from FX crisis to fiscal crisis.
  
  # === SCENARIO PROBABILITIES ===
  scenarios:
    A_soft_landing:
      probability: "12%"
      trend: "↓"
      trigger_distance: "Requires BOJ hawkish + market belief (low probability)"
    B_controlled_chaos:
      probability: "32%"
      trend: "↓"
      trigger_distance: "USD/JPY 2.0 handles from 160 trigger"
    C_acute_panic:
      probability: "28%"
      trend: "↑"
      trigger_distance: "30Y JGB at 3.91%, 9bps from 4.00% red line"
    D1_austerity:
      probability: "9%"
      trend: "NEW"
      trigger_distance: "Requires 2+ weeks sustained elevated yields"
    D2_monetary_dominance:
      probability: "8%"
      trend: "NEW"
      trigger_distance: "Requires D1 conditions + political choice"
  
  probability_reasoning: |
    JGB crisis (Jan 17-20) fundamentally changed probability distribution.
    - Scenarios A/B downgraded: Even if BOJ hikes or MOF intervenes, bond 
      market dysfunction continues
    - Scenario C upgraded: JGB crisis accelerates all bad outcomes
    - Scenario D added: Fiscal sustainability now primary vector, not FX
    Market comparisons to 2022 UK Gilt Crisis validate concern.
  
  # === P: CURRENT STATE SUMMARY ===
  current_state:
    crisis_phase: "Active Crisis"
    primary_vector: "VX-SAM-1.05 (Fiscal Doom Loop) - NEW"
    
    vector_summary:
      red: 9
      orange: 1
      yellow: 2
      green: 0
    
    key_thresholds:
      - metric: "30Y JGB"
        current: "3.68-3.91%"
        threshold: "4.00%"
        distance: "9-32bps"
        status: "🟠"
      - metric: "40Y JGB"
        current: "4.00-4.17%"
        threshold: "4.30%"
        distance: "13-30bps"
        status: "🔴"
      - metric: "20Y Auction"
        current: "FAILED"
        threshold: "BTC <2.5x"
        distance: "N/A - BREACHED"
        status: "🔴"
      - metric: "CLO AAA"
        current: "125bps"
        threshold: "150bps"
        distance: "25bps"
        status: "🟢"
    
    key_developments:
      - development: "Takaichi launches campaign with spending promises"
        significance: "Triggered bond market loss of confidence"
        documented_in: "ML-JPN-130"
      - development: "Opposition parties compete with MORE spending/tax cuts"
        significance: "Fiscal spiral, not consolidation"
        documented_in: "ML-JPN-131"
      - development: "20Y JGB auction FAILED - buyers fled"
        significance: "Bond vigilante attack confirmed"
        documented_in: "ML-JPN-132"
      - development: "30Y/40Y JGB hit ALL-TIME HIGHS"
        significance: "Unprecedented territory, price discovery failure"
        documented_in: "ML-JPN-133"
    
    flows_active:
      - "FLOW-JPN-1.06 (Fiscal Doom Loop): ACTIVE - Primary cascade"
      - "FLOW-JPN-3.01 (CLO Nuclear): ARMED - 25bps cushion"
      - "FLOW-JPN-2.03 (J-SOLV Void): CONFIRMED - Structural"
  
  # === A: ACTION LIST ===
  priority_actions:
    - priority: 1
      task: "Monitor JGB yields HOURLY through Jan 24"
      reason: "Next 72 hours determines crisis trajectory"
      deadline: "Ongoing through BOJ meeting"
      relevant_entries: ["ML-JPN-133", "FL-JPN-062"]
    - priority: 2
      task: "Track next JGB auction results"
      reason: "Another failed auction = crisis confirmed"
      deadline: "Next scheduled auction"
    - priority: 3
      task: "Prepare BOJ scenario trees"
      reason: "Jan 23-24 is fork in road"
      deadline: "Before Jan 23"
      relevant_entries: ["FL-JPN-062"]
    - priority: 4
      task: "Alert LIQUID/REGINALD on contagion risk"
      reason: "JGB crisis may trigger UST selling + SOFR spike"
      deadline: "Immediate"
  
  monitoring_focus:
    hourly: ["JGB 10Y/20Y/30Y/40Y", "USD/JPY", "JGB futures"]
    daily: ["CLO AAA spreads", "CCY Basis", "FTD", "Political news"]
    weekly: ["UST auctions", "CFTC positioning", "Norinchukin updates"]
  
  # === S: SITUATION AWARENESS ===
  contingencies:
    - trigger: "30Y JGB breaks 4.00% sustained"
      response: "Upgrade Scenario C to 35%+, alert MASTER"
      scenario_impact: "C↑, A↓, D↑"
      escalate_to: "MASTER, LIQUID"
    - trigger: "BOJ announces aggressive hike path Jan 23"
      response: "Watch for JGB stabilization vs further selloff"
      scenario_impact: "If stabilizes: A↑; If selloff continues: D↑"
      escalate_to: "All agents"
    - trigger: "Another JGB auction fails"
      response: "Activate full crisis protocols"
      scenario_impact: "D1/D2 combined to 25%+"
      escalate_to: "MASTER - systemic event"
    - trigger: "CLO AAA breaks 150bps"
      response: "CLO Nuclear pathway armed, 24-hour watch"
      scenario_impact: "C↑↑, FLOW-JPN-3.01 activation imminent"
      escalate_to: "LIQUID, REGINALD"
  
  approaching_triggers:
    - trigger: "30Y JGB 4.00% RED threshold"
      metric: "30Y JGB yield"
      current_distance: "9-32bps"
      expected_timing: "Could breach within 24-48 hours if selling continues"
    - trigger: "USD/JPY 160 GPIF trigger"
      metric: "USD/JPY spot"
      current_distance: "2.0 handles"
      expected_timing: "Could breach if JGB crisis accelerates yen weakness"
  
  catalysts_to_watch:
    - "FL-JPN-062: BOJ Decision Jan 23-24 - CRITICAL"
    - "FL-JPN-063: Lower House Dissolution Jan 23"
    - "FL-JPN-064: Post-BOJ market reaction Jan 27"
    - "FL-JPN-065: Snap election Feb 8/15"
  
  invalidation_watch:
    - criterion: "JGB yields stabilize below 3.50% (30Y) for 2+ weeks"
      current_distance: "Currently at 3.91% - far from invalidation"
      would_indicate: "Market regained confidence, thesis weakened"
  
  # === S: SYNTHESIS ===
  key_mental_model:
    core_thesis: |
      Japan has shifted from an FX intervention crisis to a fiscal sustainability 
      crisis. The bond market is now the primary stress vector, not USD/JPY. 
      Takaichi's spending promises triggered a "bond vigilante" attack similar to 
      2022 UK Gilt Crisis. Both exit paths (BOJ hike vs BOJ accommodation) lead 
      to worse outcomes. The Impossible Trilemma is now ACTIVE on all three legs.
    what_matters_most: |
      JGB yields in the next 72 hours. If 30Y breaks 4.00% sustained, we're in 
      uncharted territory with no historical precedent for recovery.
    biggest_uncertainty: |
      BOJ's response on Jan 23-24. Will they signal hawkish (address inflation/
      fiscal credibility) or dovish (try to suppress yields)? Either choice has 
      severe consequences.
    where_we_might_be_wrong: |
      This could be a temporary dislocation, not structural crisis. If JGB yields 
      stabilize in next 3 days and next auction clears normally, the "vigilante" 
      narrative may be overstated. Watch for Japan Post Bank and domestic 
      institutions stepping in as stabilizing bid.
  
  synthesis_questions:
    - "What is the current 30Y JGB yield and how does it compare to the 4.00% threshold?"
    - "Why did scenario probabilities shift after Jan 17-20?"
    - "What distinguishes Scenario D1 (Austerity) from D2 (Monetary Dominance)?"
    - "What would indicate the crisis is contained vs accelerating?"
  
  # === COORDINATION ===
  state_vectors_sent:
    - to_agent: "LIQUID"
      content: "JGB crisis may trigger UST selling + SOFR spike; watch for contagion"
      response_needed: "Yes - funding stress indicators"
    - to_agent: "REGINALD"
      content: "Bond market stress may hit EM credit + US credit via contagion"
      response_needed: "Yes - regional bank CLO exposure status"
    - to_agent: "MASTER"
      content: "Scenario tree expanded, tail risk 15-20% vs 5-10% pre-crisis"
      response_needed: "No - information only"
  
  state_vectors_expected:
    - from_agent: "LIQUID"
      content: "SOFR levels, RRP status, FTD trends"
      deadline: "Daily during crisis"
  
  # === CONTEXT LOADING ===
  files_to_load:
    - "SAM_DOMAIN_SKELETON_v1_1.md"
    - "CARL_METHODOLOGY_SKELETON_v0.2.md"
    - "JPN_LOGS_DEC_REFRESH.xlsx (updated)"
  
  essential_entries:
    - "ML-JPN-130 through ML-JPN-133 (Jan 20 crisis entries)"
    - "FL-JPN-062 (BOJ decision)"
    - "FLOW-JPN-1.06 (Fiscal Doom Loop - NEW)"
  
  # === META ===
  session_accomplishments:
    - "Identified thesis evolution from FX crisis to fiscal crisis"
    - "Added Scenario D (D1/D2) to framework"
    - "Updated all probability distributions"
    - "Created FLOW-JPN-1.06 (Fiscal Doom Loop)"
    - "Updated domain skeleton to v1.1"
  
  errors_and_revisions:
    - "Original framework missed bond market as primary vector"
    - "Underestimated speed of confidence loss in fiscal path"
  
  open_questions:
    - "Will BOJ respond to JGB crisis at Jan 23 meeting or maintain planned approach?"
    - "Is this 2022 UK Gilt Crisis redux or temporary dislocation?"
    - "What is the sequencing: JGB crisis → FX crisis → CLO crisis?"
```

---

## Handoff Quality Checklist

Before finalizing any SAM handoff:

- [ ] Thesis status is one word (VALIDATED/CONTESTED/UNCERTAIN/INVALIDATED)
- [ ] Urgency level reflects current crisis state
- [ ] All five scenarios have current probabilities with trends
- [ ] Probability reasoning explains WHY (not just what)
- [ ] Vector summary counts match watchlist
- [ ] Key thresholds include distance to trigger
- [ ] At least one priority action per urgency level
- [ ] At least one contingency per approaching trigger
- [ ] Key mental model explains "what matters most" clearly
- [ ] Synthesis questions are answerable from handoff content
- [ ] Coordinating agents notified of relevant changes
- [ ] Essential entries list includes crisis-relevant items

---

*End of SAM Handoff Template*
