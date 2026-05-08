# Key State Header — STATUS.md interface for SENTRY

**Audience:** Top-level agents (CARL, REGINALD, OZK, MARCO, HAWK, BRENT, LABOR, LIQUID, HENRY, BROCK, SAM, etc.)
**Maintainer:** SENTRY
**Effort:** ~2 minutes per session, when state actually changes

---

## What this is

A standardized 4-field block at the top of your `STATUS.md` so SENTRY can scan your state in seconds when building cross-domain briefings. You stay free to structure the rest of STATUS.md however your domain demands — this is just an interface contract for the first 30-50 lines, not a constraint on your work.

## Why it matters

SENTRY reads 4-6 agents' STATUS files plus the raw feed when generating each briefing. Without a standard header, SENTRY parses each agent's custom shape (signal dashboards, narrative refreshes, multi-section status lines) — slow and high-noise. With a standard header, SENTRY extracts your state in <100 tokens and spends the rest of its budget on cross-domain pattern recognition.

## Template

Place this block in the first 30-50 lines of your `STATUS.md`, after the header line(s):

```markdown
## Key State

**Active theses:**
- [thesis 1, one line]
- [thesis 2, one line]

**Open questions:**
- [what would change your mind / falsifier you're watching for]

**Recent signals (last 48-72h):**
- [item — how you read it, 1 line]

**Currently demanding attention:**
- [what you're working on next, 1 line]
```

## Example (from `AGENTS/SENTRY/STATUS.md`)

```markdown
## Key State

**Active theses being tracked:**
- Scenario D dominant (82%) — credit cascade, war escalation, demand destruction
- Credit transmission: LABOR → CARL → REGINALD → repricing
- Energy shock: HAWK → BRENT → HENRY (demand destruction)
- Japan carry unwind: SAM → LIQUID
- PE-insurer cascade: BROCK → SHADE → LIQUID

**Open questions:**
- Will HY OAS <280 sustained kill credit stress thesis?
- Does eSLR reform mask or solve Treasury auction stress?

**Recent signals of note:**
- BOND refreshed May 5 — thesis softened (17/35)
- WALTER active — cluster taxonomy built
- Brent $110+ — war premium intact

**Currently demanding attention:**
- Pipeline build (fetch_feeds.py, GitHub Action)
- Fleet Key State header standardization
```

## Rules

1. **Bullets, not paragraphs.** Scannable beats complete.
2. **Update when state actually changes** — not every session, not on routine maintenance.
3. **Empty fields:** if a field has nothing meaningful, write `—` rather than padding.
4. **First 30-50 lines.** SENTRY reads only this region by default.
5. **Doesn't replace your structure.** Add this block; don't reorganize your STATUS around it.

---

*Spec authored 2026-05-08. Pinged by Will at agent boot per the light/organic rollout (option a). Questions → SENTRY.*
