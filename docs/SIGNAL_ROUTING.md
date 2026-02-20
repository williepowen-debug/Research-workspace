# Signal Routing Protocol

**Purpose:** Clean handoff of market signals from Prome (intake) to specialist agents (processing).

---

## The Model

```
Will sends signal (screenshot, article, data)
              ↓
    Prome (Sorting Hat)
      - Extracts key info
      - Filters noise vs signal
      - Routes to correct agent(s)
              ↓
    Agent INBOX.md
              ↓
    Agent processes on next run
      - Integrates into STATUS.md
      - Updates workbooks if needed
      - Archives or discards
```

---

## Prome's Role (Intake)

### SAVE to inbox if:
- Updates a tracked metric (claims, DQ rates, yields, auction results, etc.)
- Confirms or challenges an active thesis
- New catalyst or timeline shift
- Quote from key voice (Fed official, CEO, policymaker, analyst)
- Crosses a defined threshold
- Connects dots between agents (cross-agent signal)

### SKIP if:
- Already captured in agent's STATUS.md or recent inbox
- Noise / no actionable content
- Stale (older data than what we have)
- Tangential to any active thesis
- Pure speculation without data

### ASK Will if:
- Uncertain about relevance
- Could go to multiple agents (route to primary, note secondaries)
- Potentially sensitive or position-affecting

---

## Inbox Format

Each signal entry in `AGENTS/[AGENT]/INBOX.md`:

```markdown
---
## [YYYY-MM-DD HH:MM UTC] Signal Title

**Source:** Publication, date, author if notable

**Signal:** 2-3 sentence summary of what matters

**Key Data:**
- Metric: Value (vs prior/expected)
- Quote: "exact words if important"

**Relevance:** Why this matters to this agent's thesis

**Cross-agent:** Tag other agents if relevant (e.g., "Also relevant to HENRY")

---
```

---

## Agent's Role (Processing)

**On every session start, agents must:**

1. Check `INBOX.md` for new entries
2. For each entry, decide:
   - **INTEGRATE:** Add to STATUS.md in appropriate section
   - **UPDATE:** Modify existing data/section
   - **ARCHIVE:** Move to `inbox_archive/YYYY-MM.md` (useful but not STATUS-worthy)
   - **DISCARD:** Delete (noise that slipped through)
3. Clear processed entries from INBOX.md

**Integration guidelines:**
- Update Signal Dashboard if it's a tracked metric
- Add to relevant thematic section if analysis/context
- Create new section only if significant new vector
- Note the source and date for audit trail

---

## Inbox Locations

| Agent | Inbox Path |
|-------|------------|
| LABOR | `AGENTS/LABOR/INBOX.md` |
| CARL | `AGENTS/CARL/INBOX.md` |
| SAM | `AGENTS/SAM/INBOX.md` |
| HENRY | `AGENTS/HENRY/INBOX.md` |
| LIQUID | `AGENTS/LIQUID/INBOX.md` |
| REGINALD | `AGENTS/REGINALD/INBOX.md` |
| HAWK | `AGENTS/HAWK/INBOX.md` |
| MARCO | `AGENTS/MARCO/INBOX.md` |

Sub-agents (BROCK, CREED, GIG) receive signals via their parent agent.

---

## Cross-Agent Signals

Some signals touch multiple agents. Prome routes to **primary** agent and notes secondaries:

| Signal Type | Primary | Secondary |
|-------------|---------|-----------|
| Employment data | LABOR | CARL, REGINALD |
| Consumer credit | CARL | REGINALD |
| BOJ/Japan | SAM | LIQUID, HENRY |
| Fed policy | LIQUID | HENRY, REGINALD |
| Geopolitical | HAWK | SAM (if Japan), LIQUID (if oil) |
| Market structure | HENRY | LIQUID |
| Bank stress | REGINALD | CARL |

Primary agent can forward to secondaries or note in their STATUS.md cross-agent section.

---

## Archive Structure

Processed signals that have lasting reference value:

```
AGENTS/[AGENT]/inbox_archive/
  2026-02.md   # February 2026 archived signals
  2026-03.md   # March 2026 archived signals
```

Keeps inbox clean while preserving audit trail.

---

## Example Flow

**Will sends:** Screenshot of Bloomberg article "US Jobless Claims Drop to 206,000"

**Prome:**
1. Extracts: Claims 206K, down 23K, lowest since Jan, Oxford Economics quote
2. Filters: Yes — updates tracked metric, relevant to thesis
3. Routes: Primary = LABOR, Secondary = CARL (employment firewall debate)
4. Writes to `AGENTS/LABOR/INBOX.md`

**LABOR (on next run):**
1. Reads INBOX.md
2. Decides: INTEGRATE — update Signal Dashboard + add analysis section
3. Updates STATUS.md
4. Clears entry from INBOX.md (or archives if reference value)

---

*Protocol established: 2026-02-20*
