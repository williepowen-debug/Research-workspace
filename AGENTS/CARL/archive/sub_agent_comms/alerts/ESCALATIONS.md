# ESCALATIONS LOG

**Purpose:** High-priority alerts that any agent can post for immediate cross-agent visibility.

---

## Active Escalations

*None currently active.*

---

## Escalation Template

When posting an escalation, add an entry below "Active Escalations":

```markdown
### [DATE] - [AGENT] - [Brief Title]

**Severity:** [HIGH | CRITICAL]
**Posted by:** [AGENT]
**Timestamp:** [ISO 8601]

**Signal:**
[What was observed]

**Implication:**
[Why this matters for the system]

**Recommended Response:**
[What should happen next]

**Addressed:** [ ] No / [x] Yes - [Date, by whom, action taken]
```

---

## Example Entry

### 2026-01-19 - NICK - Major BNPL Lender Distress

**Severity:** HIGH
**Posted by:** NICK
**Timestamp:** 2026-01-19T15:30:00Z

**Signal:**
Affirm stock down 40% in one week; multiple analysts downgrading on deteriorating loan performance. Internal data suggests 90+ DQ rate doubled in Q4.

**Implication:**
Cockroach thesis activation for BNPL sector. If Affirm is struggling, smaller BNPL players likely worse. Hidden consumer leverage may be unwinding.

**Recommended Response:**
CARL should reassess shadow credit exposure. NICK will post full State Vector with details.

**Addressed:** [ ] No

---

## Rules for Escalation

**DO escalate:**
- Threshold breaches
- Evidence that contradicts system thesis
- Lender/company failures in your domain
- Sudden trend reversals
- Cross-domain implications you've identified

**DON'T escalate:**
- Routine observations (use State Vectors)
- Low-confidence signals without interpretation
- Things already captured in your normal State Vector

---

## Resolution Protocol

When an escalation is addressed:
1. Check the "Addressed" box
2. Note the date and who addressed it
3. Briefly note action taken
4. Move to "Resolved Escalations" section below after 30 days

---

## Resolved Escalations

*Archive of addressed escalations (older than 30 days).*

*None yet.*
