<!--
================================================================================
HARVEST PROVENANCE — prepended 2026-07-10 by KORE (editor agent) for DAEDALUS.
Context: Will-approved META sub-agent retirement (DAEDALUS CARL sub-agent audit,
2026-07-10). Original at AGENTS/CARL/sub_agents/META/core/RESEARCH_DIGEST.md — now
FROZEN. This is the SOLE surviving copy of the 6-framework methodology digest: its
source documents (HEUER_CONDENSED, CARL_NONAKA_RESEARCH_SECTION, CARL_BOUNDARY_
OBJECTS_RESEARCH_SECTION, Lab_notebooks, Military_notes, CARL_HOSPITAL_HANDOFFS_
RESEARCH_SECTION) were pruned from the repo. Relevance to DAEDALUS: maps onto the
PATTERNS / BLUEPRINTS layer (design doctrine for how agents are built).
Content below is byte-identical to the frozen original (diff-verified at harvest).
================================================================================
-->

# RESEARCH DIGEST

**Purpose:** Consolidated summary of six research frameworks informing CARL methodology. Load this instead of full research documents for routine sessions. Reference full documents when revising specific methodology sections or needing detailed provenance.

**Version:** 1.0 | **Created:** 2026-01-19

---

## Quick Reference: Framework → Methodology Mapping

| Framework | Primary Contribution | Methodology Sections |
|-----------|---------------------|---------------------|
| Heuer | Hypothesis evaluation, bias mitigation | §3, §7, Appendix B |
| Nonaka | Externalization imperative, knowledge transfer | §1.2, §1.10, §5 |
| Boundary Objects | Multi-agent coordination, State Vectors | §1.9, §6 |
| Lab Notebooks | Immutability, audit trails, ALCOA+ | §1.4, §2, Appendix A |
| Military C2 | Intent-based guidance, degraded comms | §1.5, §1.6, §4, §5 |
| Hospital Handoffs | Structured transfer, I-PASS adaptation | §1.3, §1.8, §5 |

---

## 1. HEUER — Intelligence Analysis

**Source:** Richards Heuer, *Psychology of Intelligence Analysis* (CIA, 1999)

**Core Insight:** The goal is to DISPROVE hypotheses, not confirm them. The surviving hypothesis is not the one with the most supporting evidence—it's the one with the LEAST contradictory evidence. This is counterintuitive but essential: LLMs naturally generate coherent narratives and seek confirmation. Structured disconfirmation counteracts this tendency.

**Key Principles:**
- **Diagnostic value:** Evidence consistent with ALL hypotheses has zero analytical value. Prioritize evidence that discriminates.
- **Separate generation from evaluation:** Different cognitive modes. Consider different agent roles or session types.
- **Pre-commit tripwires:** Define invalidation conditions BEFORE you need them to prevent motivated reasoning.
- **Preserve rejected alternatives:** Document why hypotheses were rejected. The reasoning may need revisiting.
- **Fresh eyes catch blind spots:** Analysts entering late often see what veterans miss due to accumulated framing.

**CARL Parallel:** When evaluating the Front-Loading thesis, the question isn't "what supports it?" but "what contradicts it?" Maintain competing hypotheses (e.g., Soft Landing) with equal structural rigor. Tag evidence by diagnostic value. Implement Devil's Advocate sessions.

**Full Document:** HEUER_CONDENSED.md (~800 words)

---

## 2. NONAKA — Knowledge Management

**Source:** Nonaka & Takeuchi, *The Knowledge-Creating Company* (1995); SECI papers

**Core Insight:** Knowledge creation involves dynamic conversion between tacit knowledge (intuition, pattern recognition, "feel") and explicit knowledge (documentation, data). The SECI model describes four modes: Socialization (tacit→tacit), Externalization (tacit→explicit), Combination (explicit→explicit), Internalization (explicit→tacit). LLM systems operate primarily in Combination mode and struggle with Externalization—the critical bottleneck.

**Key Principles:**
- **Externalization is the bottleneck:** Converting tacit understanding to explicit documentation is difficult and lossy. It's also the only mechanism for cross-session transfer.
- **Some knowledge resists articulation:** Accept that handoffs will never capture everything. Design for partial transfer.
- **Metaphors carry meaning:** Domain metaphors ("zombie borrower," "cockroach thesis") transfer understanding that formal definitions cannot.
- **Ba (shared context) matters:** Knowledge is embedded in context. Without shared context, explicit knowledge loses meaning.
- **Combination ≠ creation:** Moving data between spreadsheets is knowledge organization, not creation. Creation happens through externalization and dialogue.

**CARL Parallel:** Each session develops tacit understanding that evaporates at session end. Handoffs attempt externalization under time pressure. The methodology skeleton is explicit doctrine; session dialogue is the externalization process. Acknowledge what's lost—don't design for perfection.

**Full Document:** CARL_NONAKA_RESEARCH_SECTION.md (~3,000 words)

---

## 3. BOUNDARY OBJECTS — Coordination Theory

**Source:** Star & Griesemer (1989); Carlile extensions (2002, 2004)

**Core Insight:** Boundary objects enable coordination between different communities WITHOUT requiring consensus on meaning. They maintain common structure while allowing local interpretation. This is exactly what State Vectors and handoffs must do—be meaningful to sender when creating, meaningful to receiver when consuming, despite different contexts.

**Key Principles:**
- **Coordination without consensus:** Agents don't need to fully agree on what a metric means—they need artifacts structured enough to communicate.
- **Three boundary types:** Syntactic (vocabulary), Semantic (interpretation), Pragmatic (interests). Each requires different intervention.
- **Four object types:** Repositories (indexed collections), Ideal types (abstract models), Coincident boundaries (shared scope, different content), Standardized forms (templates).
- **Design for minimum structure:** Engineered boundary objects tend toward over-specification. Let use refine format over time.
- **Boundary objects can fail:** Too rigid loses flexibility; too vague loses coherence; imposed objects lack buy-in.

**CARL Parallel:** State Vectors are the critical boundary object for multi-agent coordination. They must include syntactic layer (shared vocabulary), semantic layer (interpretation), and pragmatic layer (recommended action). Handoffs are boundary objects across time—same principles apply to session continuity as to agent coordination.

**Full Document:** CARL_BOUNDARY_OBJECTS_RESEARCH_SECTION.md (~3,500 words)

---

## 4. LAB NOTEBOOKS — Audit Trail Discipline

**Source:** NIH Guidelines, FDA GLP Regulations, ALCOA+ framework

**Core Insight:** Laboratory notebooks represent centuries of refined practice for maintaining defensible evidence of what was known, when, and how conclusions were reached. The discipline has been legally tested—courts and regulators have determined what makes records credible. Core principle: NEVER delete, only correct with preserved history.

**Key Principles:**
- **ALCOA+:** Attributable, Legible, Contemporaneous, Original, Accurate + Complete, Consistent, Enduring, Available.
- **Contemporaneous recording:** Log observations when made, not reconstructed later. Timestamp reflects observation time.
- **Immutability:** Never erase, never obliterate. Strike through errors, write correction, initial and date. Original remains readable.
- **Errors are information:** The error itself may prove relevant. Preserved errors demonstrate good faith, not cover-up.
- **Witnessing = comprehensibility:** If another reader can't understand it, it's not properly documented.

**CARL Parallel:** ML entries should be immutable once created. Corrections create new versions with preserved history. Include reasoning chains, not just conclusions. Cross-reference everything—isolated entries are effectively lost. Design for forensics: assume someone will need to reconstruct the analytical path.

**Full Document:** Lab_notebooks.docx (~3,000 words)

---

## 5. MILITARY C2 — Command and Control

**Source:** US Army ADP 6-0 (2019); Boyd OODA; McChrystal *Team of Teams*

**Core Insight:** Mission Command philosophy: centralized intent, decentralized execution. Commanders tell subordinates WHAT to achieve and WHY, not HOW. This enables autonomous action when communication fails—critical for session discontinuity. The handoff is the last transmission before contact is lost.

**Key Principles:**
- **Commander's Intent:** Purpose + Key Tasks + End State. Enables subordinates to act appropriately without explicit instruction.
- **Degraded communications protocols:** Plan for the break. Define rally points, time-based actions, default responses.
- **Shared consciousness before empowerment:** McChrystal's lesson—don't empower agents to act autonomously until they have sufficient shared context.
- **Orientation is central:** Boyd's insight—what gets lost at session boundaries is orientation, not just data. Everything flows from how you frame the situation.
- **Doctrine enables self-synchronization:** Shared frameworks make compatible independent action possible without explicit coordination.

**CARL Parallel:** The Front-Loading thesis functions as commander's intent—it tells new sessions what they're trying to determine. The methodology skeleton is CARL's "doctrine." Handoffs should include delegated authorities (what you can do) and constraints (what you must not do). Pre-commit contingencies before they're needed.

**Full Document:** Military_notes.md (~4,000 words)

---

## 6. HOSPITAL HANDOFFS — Structured Transfer

**Source:** I-PASS research (Starmer et al., NEJM 2014); SBAR; Joint Commission

**Core Insight:** Healthcare discovered that handoffs were "remarkably haphazard"—and that 67% of sentinel events involved communication failures during transitions. Structured protocols (I-PASS) reduced preventable adverse events by 47%. The mechanism: transferring INTERPRETATION, not just data, and confirming shared understanding.

**Key Principles:**
- **Data ≠ understanding:** Transferring facts without interpretation leaves receiver to reconstruct meaning (often incorrectly).
- **Prioritization signal is critical:** "Illness Severity" equivalent (one word: stable/watcher/unstable) allows immediate calibration.
- **Contingency planning is pre-commitment:** "If X, then Y" statements prepare for scenarios and survive cognitive overload.
- **Synthesis by Receiver:** The step most often skipped is the step that confirms transfer worked. Receiver paraphrases back.
- **Structure reduces cognitive load:** Predictable format frees mental capacity for comprehension.

**CARL Parallel:** Handoff template adapts I-PASS: Thesis Status (illness severity), Current State (patient summary), Action List, Situation Awareness (contingencies), Synthesis Questions (for receiver confirmation). Opening protocol requires synthesis confirmation before proceeding with analysis.

**Full Document:** CARL_HOSPITAL_HANDOFFS_RESEARCH_SECTION.md (~3,500 words)

---

## Framework Conflicts and Resolutions

| Tension | Framework A | Framework B | Resolution |
|---------|-------------|-------------|------------|
| Speed vs. rigor | C2: Act decisively | Heuer: Evaluate systematically | Speed for execution, rigor for assessment |
| Trust intuition | C2: Trust commanders | Heuer: Distrust as bias source | Externalize intuition, then evaluate |
| Completeness | Lab Notebooks: Record everything | Nonaka: Some knowledge is inarticulable | Aim for completeness, acknowledge limits |
| Structure | Hospital Handoffs: Standardize | Boundary Objects: Allow flexibility | Minimum viable structure; let use refine |

---

## When to Load Full Documents

| If revising... | Load... |
|----------------|---------|
| Hypothesis management (§3) | HEUER_CONDENSED.md |
| Handoff specification (§5) | CARL_HOSPITAL_HANDOFFS_RESEARCH_SECTION.md |
| Multi-agent coordination (§6) | CARL_BOUNDARY_OBJECTS_RESEARCH_SECTION.md, Military_notes.md |
| Bias mitigation (§7) | HEUER_CONDENSED.md |
| Audit trail / entry templates | Lab_notebooks.docx |
| Knowledge transfer principles | CARL_NONAKA_RESEARCH_SECTION.md |

---

## Ten Core Principles (Consolidated)

These principles, derived from six frameworks, form the methodology's foundation:

1. **Disprove, Don't Confirm** (Heuer)
2. **Externalize Before the Break** (Nonaka, Hospital Handoffs)
3. **Transfer Interpretation, Not Just Data** (Hospital Handoffs)
4. **Immutability Preserves Trust** (Lab Notebooks)
5. **Intent Enables Autonomy** (Military C2)
6. **Pre-Commit Contingencies** (Hospital Handoffs, Military C2)
7. **Diagnostic Value Over Volume** (Heuer)
8. **Structure Reduces Cognitive Load** (Hospital Handoffs)
9. **Boundary Objects Enable Coordination** (Boundary Objects)
10. **Acknowledge What's Lost** (Nonaka)

---

*End of Research Digest*

*Total: ~1,900 words*
