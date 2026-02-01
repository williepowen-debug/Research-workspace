# META DOMAIN SKELETON

# Purpose: Structural scaffold for LLM methodology research and system design
# Domain:  LLM Multi-Agent Architecture, Methodology Design, Knowledge Management,
#          Session Continuity, Analytical Frameworks
# Agent:   META (Methodology & Architecture Research)
#
# Version: 1.1
# Created: 2026-01-19
# Updated: 2026-01-19
# Author:  META-1 Session (Initial Architecture), META-2 Session (Context Optimization)
#
# Usage:
#   - Load this file at the start of any META session
#   - Provides vocabulary, frameworks, and architecture for methodology research
#   - Companion to METHODOLOGY_SKELETON which governs process
#   - This skeleton governs the CONTENT of methodology research
#
# Note: This is a meta-project—we're building the tools to build other agents.

metadata:
  name: "META Domain Skeleton"
  domain: "LLM System Design, Methodology Research, Multi-Agent Architecture"
  version: "1.1"
  created: "2026-01-19"
  last_updated: "2026-01-19"

  phase_model: |
    Phase 1 (Research) → Phase 2 (Synthesis) → Phase 3 (Implementation) →
    Phase 4 (Testing) → Phase 5 (Refinement)

    Research identifies frameworks. Synthesis extracts applicable principles.
    Implementation produces artifacts. Testing validates in live systems.
    Refinement iterates based on operational feedback.

  primary_agent: "META (Methodology & Architecture)"

  core_thesis:
    name: "Structured Methodology Improves LLM System Performance"
    description: |
      Multi-agent LLM systems suffer from predictable failure modes:

      1. SESSION DISCONTINUITY: Each instance starts with zero tacit knowledge.
         Handoffs lose context. Analytical intuition evaporates.

      2. COORDINATION FRICTION: Agents with different domains struggle to
         share information without losing meaning at boundaries.

      3. COGNITIVE BIAS: LLMs exhibit confirmation bias, anchoring, and
         coherence-seeking that degrades analytical quality.

      4. AUDIT OPACITY: Reasoning paths are not preserved, making it
         impossible to reconstruct how conclusions were reached.

      The thesis: STRUCTURED METHODOLOGY (principles, protocols, templates,
      boundary objects) measurably reduces these failure modes compared to
      ad-hoc operation.

    confidence: "Theoretical 85%, Empirical 50% (limited testing)"
    validation_status: "PARTIALLY VALIDATED - CARL operational, methodology v0.2 untested"

  current_status:
    phase: "Phase 2 → Phase 3 Transition (Synthesis to Implementation)"
    frameworks_researched: 6
    artifacts_produced: 3  # Methodology skeleton v0.2, Research Digest, META skeleton v1.1
    agents_operational: 1  # CARL
    agents_planned: 6  # POLLY, DOC, NICK, POP, GIG
    note: "Core methodology skeleton complete. Context optimized. Ready for operational testing."

#
# SECTION 1: RESEARCH FRAMEWORKS
#
# Frameworks studied and their contributions to the methodology.
# NOTE: Full research documents are REFERENCE ONLY. Load RESEARCH_DIGEST.md for routine sessions.

frameworks:

  completed:

    heuer:
      name: "Heuer - Psychology of Intelligence Analysis"
      source: "Richards Heuer, CIA (1999)"
      key_contributions:
        - "Analysis of Competing Hypotheses (ACH)"
        - "Diagnostic value principle: evidence consistent with all hypotheses has zero value"
        - "Disprove, don't confirm"
        - "Cognitive bias taxonomy and countermeasures"
      applied_to:
        - "§3 Hypothesis Management"
        - "§7 Bias Mitigation (Devil's Advocate protocol)"
        - "Diagnostic value tagging in ML entries"
      research_document: "HEUER_CONDENSED.md"
      load_when: "Revising §3 or §7"
      status: "COMPLETE"

    nonaka:
      name: "Nonaka & Takeuchi - Knowledge Management"
      source: "The Knowledge-Creating Company (1995); SECI papers"
      key_contributions:
        - "SECI model: Socialization, Externalization, Combination, Internalization"
        - "Tacit vs explicit knowledge distinction"
        - "Externalization as bottleneck for LLM systems"
        - "Concept of Ba (shared context)"
      applied_to:
        - "Principle 1.2: Externalize Before the Break"
        - "Principle 1.10: Acknowledge What's Lost"
        - "Handoff structure (forcing externalization)"
      research_document: "CARL_NONAKA_RESEARCH_SECTION.md"
      load_when: "Revising knowledge transfer principles"
      status: "COMPLETE"

    boundary_objects:
      name: "Star & Griesemer - Boundary Objects"
      source: "Institutional Ecology paper (1989); Carlile extensions"
      key_contributions:
        - "Coordination without consensus"
        - "Syntactic, semantic, pragmatic boundaries"
        - "Four types: repositories, ideal types, coincident boundaries, standardized forms"
        - "State Vectors as boundary objects"
      applied_to:
        - "Principle 1.9: Boundary Objects Enable Coordination"
        - "§6 Multi-Agent Coordination"
        - "State Vector specification"
      research_document: "CARL_BOUNDARY_OBJECTS_RESEARCH_SECTION.md"
      load_when: "Revising §6 or State Vector design"
      status: "COMPLETE"

    lab_notebooks:
      name: "Laboratory Notebook Discipline"
      source: "NIH, FDA GLP, ALCOA+ framework"
      key_contributions:
        - "ALCOA+: Attributable, Legible, Contemporaneous, Original, Accurate"
        - "Immutability principle"
        - "Error correction protocol (never delete)"
        - "Witnessing and audit trails"
      applied_to:
        - "Principle 1.4: Immutability Preserves Trust"
        - "ML entry versioning"
        - "Correction protocols"
      research_document: "Lab_notebooks.docx"
      load_when: "Revising audit trail or entry templates"
      status: "COMPLETE"

    military_c2:
      name: "Military Command & Control"
      source: "Mission Command doctrine; Boyd OODA; McChrystal"
      key_contributions:
        - "Commander's Intent: Purpose + Key Tasks + End State"
        - "Auftragstaktik: decentralized execution within intent"
        - "Degraded communications protocols"
        - "Shared consciousness before empowered execution"
      applied_to:
        - "Principle 1.5: Intent Enables Autonomy"
        - "Thesis + invalidation criteria as commander's intent"
        - "Handoff as last transmission before contact lost"
      research_document: "Military_notes.md"
      load_when: "Revising §4, §5, or multi-agent hierarchy"
      status: "COMPLETE"

    hospital_handoffs:
      name: "Healthcare Handoff Protocols"
      source: "I-PASS research (Starmer et al., NEJM 2014); SBAR; Joint Commission"
      key_contributions:
        - "67% of sentinel events from communication failure"
        - "Structured handoffs reduce adverse events 30-47%"
        - "I-PASS: Illness severity, Patient summary, Action list, Situation awareness, Synthesis"
        - "Receiver synthesis confirmation"
      applied_to:
        - "Principle 1.3: Transfer Interpretation, Not Just Data"
        - "Principle 1.6: Pre-Commit Contingencies"
        - "§5 Handoff Specification (I-PASS adapted)"
        - "Opening protocol synthesis confirmation"
      research_document: "CARL_HOSPITAL_HANDOFFS_RESEARCH_SECTION.md"
      load_when: "Revising §5 or handoff templates"
      status: "COMPLETE"

  pending:

    accounting_audit:
      name: "Accounting & Audit Principles"
      potential_contributions:
        - "Materiality thresholds"
        - "Separation of duties"
        - "Reconciliation protocols"
        - "Double-entry / self-balancing systems"
      status: "NOT STARTED"
      priority: "LOW - may not be needed"

    medical_soap:
      name: "Medical Records / SOAP Notes"
      potential_contributions:
        - "Problem list continuity"
        - "Subjective/Objective/Assessment/Plan structure"
        - "Longitudinal record keeping"
      status: "NOT STARTED"
      priority: "LOW - partially covered by hospital handoffs"

#
# SECTION 2: ARTIFACT REGISTRY
#
# Methodology artifacts produced by this project.

artifacts:

  skeletons:

    methodology_skeleton:
      name: "Agent Methodology Skeleton"
      current_version: "0.2"
      file: "CARL_METHODOLOGY_SKELETON_v0.2.md"
      purpose: "Governs HOW agents operate - principles, protocols, templates"
      word_count: "~4,500"
      sections:
        - "§0 Quick Start"
        - "§1 Core Principles (10)"
        - "§2 Log System Architecture"
        - "§3 Hypothesis Management"
        - "§4 Session Protocols"
        - "§5 Handoff Specification"
        - "§6 Multi-Agent Coordination"
        - "§7 Bias Mitigation"
        - "Appendix A: Entry Templates"
        - "Appendix B: Decision Trees"
        - "Appendix C: Checklists"
      load: "EVERY SESSION"
      status: "COMPLETE - Ready for testing"

    carl_domain_skeleton:
      name: "CARL Domain Skeleton"
      current_version: "1.2"
      file: "__CARL_DOMAIN_SKELETON.md"
      purpose: "Defines WHAT CARL monitors - vectors, entities, glossary"
      owner: "CARL project"
      load: "CARL sessions only"
      status: "OPERATIONAL"

    meta_domain_skeleton:
      name: "META Domain Skeleton"
      current_version: "1.1"
      file: "META_DOMAIN_SKELETON_v1.1.md"
      purpose: "Defines WHAT META monitors - frameworks, artifacts, principles"
      word_count: "~1,800"
      owner: "Methodology project"
      load: "EVERY SESSION"
      status: "THIS DOCUMENT"

  consolidated:

    research_digest:
      name: "Research Digest"
      current_version: "1.0"
      file: "RESEARCH_DIGEST.md"
      purpose: "Consolidated summary of six research frameworks (~1,900 words)"
      replaces: "Loading six separate research documents (~22,000 words)"
      word_count: "~1,900"
      contents:
        - "Framework → Methodology mapping table"
        - "Each framework: core insight, 5 principles, CARL parallel"
        - "Conflict resolution table"
        - "When to load full documents guide"
        - "Ten core principles with provenance"
      load: "EVERY SESSION (replaces full research docs)"
      status: "COMPLETE"

  research_documents:
    note: "REFERENCE ONLY - Load via RESEARCH_DIGEST.md for routine sessions"

    - name: "Heuer Condensed"
      file: "HEUER_CONDENSED.md"
      word_count: "~800"
      load_when: "Revising hypothesis management or bias mitigation"

    - name: "Nonaka Research Section"
      file: "CARL_NONAKA_RESEARCH_SECTION.md"
      word_count: "~3,000"
      load_when: "Revising knowledge transfer principles"

    - name: "Boundary Objects Research Section"
      file: "CARL_BOUNDARY_OBJECTS_RESEARCH_SECTION.md"
      word_count: "~3,500"
      load_when: "Revising multi-agent coordination or State Vectors"

    - name: "Lab Notebooks Research"
      file: "Lab_notebooks.docx"
      word_count: "~3,000"
      load_when: "Revising audit trails or entry templates"

    - name: "Military C2 Notes"
      file: "Military_notes.md"
      word_count: "~4,000"
      load_when: "Revising session protocols or handoffs"

    - name: "Hospital Handoffs Research Section"
      file: "CARL_HOSPITAL_HANDOFFS_RESEARCH_SECTION.md"
      word_count: "~3,500"
      load_when: "Revising handoff specification"

  templates:

    - name: "ML Entry Template"
      location: "Methodology Skeleton Appendix A.1"

    - name: "FL Entry Template"
      location: "Methodology Skeleton Appendix A.2"

    - name: "FLOW Entry Template"
      location: "Methodology Skeleton Appendix A.3"

    - name: "Handoff Template"
      location: "Methodology Skeleton Appendix A.4"

    - name: "State Vector Template"
      location: "Methodology Skeleton §6.2"

#
# SECTION 3: CONTEXT LOADING STRATEGY
#
# Tiered approach to manage context window consumption.

context_loading:

  rationale: |
    Full research documents total ~25,000 words. Loading everything every session
    wastes context and buries actionable content. Tiered strategy reduces default
    load to ~9,700 words (60% reduction) while preserving access to detail.

  tier_1_always_load:
    description: "Core context for every META session"
    total_words: "~9,700"
    documents:
      - file: "CARL_SYSTEM_CONTEXT_FOR_METHODOLOGY.md"
        words: "~1,500"
        purpose: "Bridge to target system"

      - file: "META_DOMAIN_SKELETON_v1.1.md"
        words: "~1,800"
        purpose: "This project's structure"

      - file: "CARL_METHODOLOGY_SKELETON_v0.2.md"
        words: "~4,500"
        purpose: "The deliverable artifact"

      - file: "RESEARCH_DIGEST.md"
        words: "~1,900"
        purpose: "Consolidated research summary"

  tier_2_load_when_needed:
    description: "Full research documents - load only when revising specific sections"
    trigger_table:
      - revising: "Hypothesis management (§3)"
        load: "HEUER_CONDENSED.md"

      - revising: "Bias mitigation (§7)"
        load: "HEUER_CONDENSED.md"

      - revising: "Handoff specification (§5)"
        load: "CARL_HOSPITAL_HANDOFFS_RESEARCH_SECTION.md"

      - revising: "Multi-agent coordination (§6)"
        load: "CARL_BOUNDARY_OBJECTS_RESEARCH_SECTION.md, Military_notes.md"

      - revising: "Audit trails / entry templates"
        load: "Lab_notebooks.docx"

      - revising: "Knowledge transfer principles"
        load: "CARL_NONAKA_RESEARCH_SECTION.md"

  tier_3_reference_only:
    description: "Pull specific quotes or principles as needed"
    note: "Full documents remain in project files for provenance"

#
# SECTION 4: AGENT REGISTRY
#
# Multi-agent ecosystem planned and operational.

agents:

  operational:

    carl:
      name: "CARL (Consumer Aggregate Risk Ledger)"
      domain: "US Consumer Financial Stress"
      status: "OPERATIONAL"
      sessions_completed: "6+"
      domain_skeleton: "__CARL_DOMAIN_SKELETON.md"
      workbook: "CARL_MLFLFLOWVX_S6.xlsx"
      thesis: "Front-Loading Paradigm"
      subordinates_planned:
        - "Employment sub-agent"
        - "Housing sub-agent"
        - "Credit sub-agent"
        - "Behavioral sub-agent"

  planned:

    polly:
      name: "POLLY"
      domain: "Insurance Stress (P&C, Health)"
      status: "PLANNED"
      reports_to: "CARL"

    doc:
      name: "DOC"
      domain: "Healthcare Cost Stress"
      status: "PLANNED"
      reports_to: "CARL"

    nick:
      name: "NICK"
      domain: "Shadow Credit / Non-Bank Lending"
      status: "PLANNED"
      reports_to: "CARL"

    pop:
      name: "POP"
      domain: "Small Business Stress"
      status: "PLANNED"
      reports_to: "CARL"

    gig:
      name: "GIG"
      domain: "Gig Economy Saturation"
      status: "PLANNED"
      reports_to: "CARL"

#
# SECTION 5: PROBLEM REGISTRY
#
# Core problems this methodology addresses.

problems:

  session_discontinuity:
    name: "Session Discontinuity"
    description: |
      Each LLM session starts with zero tacit knowledge. Handoffs capture
      explicit knowledge but lose analytical intuition, pattern recognition,
      and "feel" for the domain.
    frameworks_addressing:
      - "Nonaka (externalization bottleneck)"
      - "Hospital Handoffs (structured transfer)"
      - "Military C2 (degraded communications)"
    solutions_implemented:
      - "I-PASS adapted handoff template"
      - "Opening synthesis confirmation"
      - "Session reflection protocol"
    status: "ADDRESSED - awaiting validation"

  multi_agent_coordination:
    name: "Multi-Agent Coordination"
    description: |
      Agents with different domain expertise struggle to share information
      without losing essential meaning at boundaries.
    frameworks_addressing:
      - "Boundary Objects (coordination without consensus)"
      - "Military C2 (shared consciousness)"
    solutions_implemented:
      - "State Vector specification"
      - "Three-layer boundary crossing (syntactic, semantic, pragmatic)"
    status: "ADDRESSED - untested (single agent operational)"

  cognitive_bias:
    name: "Cognitive Bias in LLM Analysis"
    description: |
      LLMs exhibit confirmation bias, anchoring, and coherence-seeking
      that degrades analytical quality over time.
    frameworks_addressing:
      - "Heuer (ACH, bias taxonomy)"
    solutions_implemented:
      - "Competing hypothesis requirement"
      - "Diagnostic value tagging"
      - "Devil's Advocate protocol"
      - "Fresh Eyes protocol"
    status: "ADDRESSED - awaiting validation"

  audit_opacity:
    name: "Audit Trail Opacity"
    description: |
      Reasoning paths are not preserved, making it impossible to reconstruct
      how conclusions were reached or identify where analysis went wrong.
    frameworks_addressing:
      - "Lab Notebooks (ALCOA+, immutability)"
      - "Heuer (preserve rejected alternatives)"
    solutions_implemented:
      - "Reasoning chain in entries"
      - "Correction with preserved history"
      - "Cross-reference requirements"
    status: "ADDRESSED - awaiting validation"

  context_overload:
    name: "Context Window Overload"
    description: |
      Loading all documentation consumes excessive context, burying actionable
      content and reducing capacity for actual analysis.
    frameworks_addressing:
      - "Practical experience (META-2 session)"
    solutions_implemented:
      - "Research Digest consolidation"
      - "Tiered loading strategy"
      - "~60% reduction in default context load"
    status: "ADDRESSED - implemented in v1.1"

#
# SECTION 6: VALIDATION FRAMEWORK
#
# How we know if the methodology is working.

validation:

  success_criteria:

    - criterion: "Reduced ramp-up time"
      measure: "New session achieves analytical competence faster"
      baseline: "Not yet measured"
      target: "50% reduction in orientation time"

    - criterion: "Confidence reasoning persists"
      measure: "Next session can explain why confidence is at current level"
      baseline: "Often lost"
      target: "100% persistence"

    - criterion: "Competing hypotheses evaluated"
      measure: "Alternative hypotheses receive structured evaluation"
      baseline: "Informal"
      target: "Monthly Devil's Advocate sessions conducted"

    - criterion: "Multi-agent communication preserves meaning"
      measure: "State Vectors transfer essential information across boundaries"
      baseline: "Not yet tested"
      target: "Receiving agent correctly interprets >80% of signals"

    - criterion: "Audit trails enable reconstruction"
      measure: "Analytical path can be reconstructed from logs"
      baseline: "Partial"
      target: "Any conclusion traceable to evidence"

    - criterion: "Context load is manageable"
      measure: "Default session load under 10,000 words"
      baseline: "~25,000 words (all docs)"
      target: "<10,000 words"
      status: "ACHIEVED - ~9,700 words with tiered strategy"

  testing_plan:

    phase_1:
      name: "CARL Operational Testing"
      scope: "Run CARL sessions using methodology v0.2"
      duration: "2-4 weeks"
      metrics:
        - "Handoff quality (synthesis questions answerable?)"
        - "Session opening time"
        - "FL/ML confusion incidents"
        - "Checklist completion rate"
      status: "READY TO BEGIN"

    phase_2:
      name: "Second Agent Deployment"
      scope: "Create POLLY or sub-agent using methodology"
      duration: "TBD"
      metrics:
        - "Time to operational"
        - "State Vector effectiveness"
        - "Cross-agent coordination quality"
      status: "PENDING Phase 1"

    phase_3:
      name: "Methodology Refinement"
      scope: "Update methodology based on operational feedback"
      duration: "Ongoing"
      metrics:
        - "Sections removed as unused"
        - "Sections expanded due to gaps"
        - "Template modifications"
      status: "PENDING Phase 1"

#
# SECTION 7: GLOSSARY
#

glossary:

  abbreviations:
    ACH: "Analysis of Competing Hypotheses"
    ALCOA: "Attributable, Legible, Contemporaneous, Original, Accurate"
    C2: "Command and Control"
    FL: "Future Log (Catalyst Log)"
    FLOW: "Cascade Map"
    I-PASS: "Illness severity, Patient summary, Action list, Situation awareness, Synthesis"
    ML: "Master Log"
    OODA: "Observe, Orient, Decide, Act"
    SBAR: "Situation, Background, Assessment, Recommendation"
    SECI: "Socialization, Externalization, Combination, Internalization"
    VX: "Vector Registry"

  key_concepts:

    boundary_object:
      definition: |
        Artifact that enables coordination between different communities
        without requiring consensus on meaning. Maintains common structure
        while allowing local interpretation.
      example: "State Vectors, log entry templates"

    diagnostic_value:
      definition: |
        Measure of how much evidence discriminates between hypotheses.
        Evidence consistent with all hypotheses has zero diagnostic value.
      levels: "HIGH, MEDIUM, LOW, ZERO"

    externalization:
      definition: |
        Converting tacit knowledge (intuition, pattern recognition) into
        explicit knowledge (documentation). The critical bottleneck for
        LLM session continuity.
      source: "Nonaka SECI model"

    state_vector:
      definition: |
        Structured report from one agent to another, crossing domain
        boundaries. Contains syntactic (data), semantic (interpretation),
        and pragmatic (recommended action) layers.
      format: "See Methodology Skeleton §6.2"

    tacit_knowledge:
      definition: |
        Knowledge that is difficult or impossible to articulate—intuition,
        pattern recognition, "feel" for the domain. Lost at session boundaries.
      contrast: "Explicit knowledge (documented, transferable)"

    tripwire:
      definition: |
        Pre-committed threshold that triggers action when crossed.
        Defined before evidence arrives to prevent motivated reasoning.
      example: "If subprime auto DQ exceeds 7%, status becomes BREACHED"

#
# SECTION 8: OPEN QUESTIONS
#

open_questions:

  - question: "How much context is too much?"
    context: |
      Loading methodology skeleton + domain skeleton + handoff + workbook
      consumes significant context window. What's the minimum viable load?
    status: "ADDRESSED - tiered loading strategy implemented"
    resolution: "Research Digest + tiered loading reduces default to ~9,700 words"

  - question: "Can Fresh Eyes protocol actually work?"
    context: |
      Protocol requires loading raw data without interpretations. But
      separating data from interpretation may be impractical.
    status: "OPEN - needs testing"

  - question: "What's the right reconciliation frequency?"
    context: |
      Weekly may be too often; monthly may let drift accumulate.
      Optimal frequency likely depends on activity level.
    status: "OPEN - needs operational data"

  - question: "How do we measure handoff quality?"
    context: |
      Success criterion is "synthesis questions answerable" but this
      is subjective. Need objective measure.
    status: "OPEN"

  - question: "Should methodology skeleton be split?"
    context: |
      Current skeleton is ~4,500 words. Could split into core (always load)
      and extended (load as needed). Trade-off: simplicity vs completeness.
    status: "OPEN - defer until operational testing"

#
# SECTION 9: VERSION HISTORY
#

version_history:

  - version: "1.0"
    date: "2026-01-19"
    author: "META-1"
    changes:
      - "Initial architecture"
      - "Framework registry"
      - "Artifact registry"
      - "Problem registry"
      - "Validation framework"

  - version: "1.1"
    date: "2026-01-19"
    author: "META-2"
    changes:
      - "Added RESEARCH_DIGEST.md to artifacts"
      - "Added Section 3: Context Loading Strategy"
      - "Added 'load_when' guidance to research documents"
      - "Added word counts to artifacts"
      - "Added 'context_overload' to problems registry (ADDRESSED)"
      - "Updated open questions (context question ADDRESSED)"
      - "Added version history section"

# END OF SKELETON

# Usage Instructions:
#
# 1. LOAD AT SESSION START (Tier 1)
#    - CARL_SYSTEM_CONTEXT_FOR_METHODOLOGY.md
#    - META_DOMAIN_SKELETON_v1.1.md (this file)
#    - CARL_METHODOLOGY_SKELETON_v0.2.md
#    - RESEARCH_DIGEST.md
#    Total: ~9,700 words
#
# 2. LOAD WHEN REVISING SPECIFIC SECTIONS (Tier 2)
#    See Section 3 trigger table for which full research docs to load
#
# 3. FOR METHODOLOGY RESEARCH
#    Reference framework summaries in RESEARCH_DIGEST.md
#    Pull full documents only for deep provenance review
#
# 4. FOR NEW AGENT CREATION
#    Use methodology skeleton as template
#    Create domain skeleton following CARL pattern
#    Register in agent registry (Section 4)
#
# 5. FOR VALIDATION
#    Follow testing plan in Section 6
#    Track against success criteria
#    Update open questions as resolved
