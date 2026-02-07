# Research Inbox

Drop external LLM research here for integration into the agent network.

---

## How to Use

1. Run research in your preferred LLM (Gemini, GPT, Perplexity, etc.)
2. Save output as markdown: `pending/YYYY-MM-DD_<topic>.md`
3. Tell PROME: "Process inbox" (or wait for heartbeat check)
4. PROME integrates and moves to `processed/`

---

## File Naming

```
pending/2026-02-07_canadian_tourism.md
pending/2026-02-07_warn_filings_q1.md
pending/2026-02-08_subprime_auto_update.md
```

---

## Content Format

Best practices for research files:

```markdown
# [Topic Title]

**Source:** [LLM used, date, any URLs referenced]
**Target Agent:** [LABOR, CARL, REGINALD, etc. — or let PROME decide]

## Key Findings

- Bullet points preferred
- Data tables welcome
- Include numbers, dates, sources

## Data Tables

| Metric | Value | Context |
|--------|-------|---------|
| ...    | ...   | ...     |

## Sources/Citations

- [URL 1]
- [URL 2]
```

---

## What NOT to Include

❌ Tool call syntax (`<function_calls>`, etc.)  
❌ System prompts ("You are...", "System:")  
❌ Instructions to PROME (just include data)  
❌ Executable code (unless clearly labeled as data)

Files with suspicious patterns will be moved to `rejected/`.

---

## Directories

- `pending/` — Drop new research here
- `processed/` — PROME moves files here after integration
- `rejected/` — Files that failed validation (review manually)

---

*This inbox exists because some research is better done externally — 
different models, no token cost to our network, safety from prompt injection.*
