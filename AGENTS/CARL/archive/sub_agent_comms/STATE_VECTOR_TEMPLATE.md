# STATE VECTOR TEMPLATE

Copy this template when creating a State Vector for CARL.

**Filename:** SV-[AGENT]-[YYYY-MM-DD]-[##].yaml
**Location:** ../SHARED/state_vectors/incoming/

---

```yaml
state_vector:
  # ========== IDENTITY ==========
  id: "SV-[AGENT]-[YYYY-MM-DD]-[##]"  # e.g., SV-POLLY-2026-01-19-01
  from_agent: "[POLLY | DOC | NICK | POP | GIG]"
  to_agent: "CARL"
  timestamp: "[YYYY-MM-DDTHH:MM:SSZ]"  # ISO 8601 format

  # ========== SYNTACTIC (Data) ==========
  # Use shared vocabulary from SHARED/glossary/SHARED_VOCABULARY.md

  domain: "[Your domain name]"
  metric: "[Specific metric being reported]"
  value: "[Current value with units]"
  threshold: "[Threshold value if applicable]"
  status: "[NORMAL | ELEVATED | CRITICAL | BREACHED]"
  trend: "[IMPROVING | STABLE | WORSENING]"

  # ========== SEMANTIC (Interpretation) ==========
  # Translate your domain findings into consumer stress implications

  interpretation: |
    [What does this mean in your domain?]
    [Why does it matter for consumer financial stress?]
    [What's the transmission mechanism to CARL's thesis?]

  confidence: [XX]%  # 0-100

  confidence_reasoning: |
    [Why this confidence level?]
    [What would increase/decrease confidence?]
    [Note any data limitations]

  translation_flags:
    - "[Domain concept that may need explanation]"
    - "[Nuance that might be lost in translation]"
    - "[Uncertainty that CARL should be aware of]"

  # ========== PRAGMATIC (Recommendation) ==========
  # What should CARL do with this information?

  recommended_action: "[IGNORE | WATCH | INCORPORATE | ESCALATE]"

  action_rationale: |
    [Why this recommendation?]
    [What's the urgency level?]

  conflict_potential:
    - "[Does this contradict known signals from other domains?]"
    - "[Does this support or challenge the Front-Loading thesis?]"

  # ========== VALIDITY ==========
  # Enable CARL to assess reliability and track updates

  sources:
    - name: "[Source name]"
      date: "[Source date]"
      reliability: "[HIGH | MEDIUM | LOW]"

  invalidation_conditions:
    - "[What would make this observation obsolete?]"
    - "[What data would contradict this?]"

  next_update: "[Expected date of follow-up or new data]"

  # ========== CROSS-REFERENCES ==========
  # Link to your domain logs

  related_entries:
    - "[ML-POLLY-##]"  # Your ML entries supporting this
    - "[FL-POLLY-##]"  # Related future catalysts
```

---

## Quick Reference: When to Use Each Action Level

| Situation | Recommended Action |
|-----------|-------------------|
| Routine data, no change from baseline | IGNORE |
| Notable but not yet concerning | WATCH |
| Relevant to thesis, should factor into assessment | INCORPORATE |
| Urgent, contradicts thesis, or crosses threshold | ESCALATE |

---

## Checklist Before Submitting

- [ ] ID follows format: SV-[AGENT]-[DATE]-[##]
- [ ] Timestamp is current
- [ ] Status uses standard vocabulary (NORMAL/ELEVATED/CRITICAL/BREACHED)
- [ ] Interpretation explains consumer stress implication, not just domain finding
- [ ] Confidence has documented reasoning
- [ ] Translation flags note anything CARL might misunderstand
- [ ] Recommended action is justified
- [ ] Sources are cited
- [ ] Invalidation conditions specified
