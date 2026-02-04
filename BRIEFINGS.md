# BRIEFINGS.md — Audio Briefing Framework

*How to request and produce narrative audio briefings for any agent/domain.*

---

## What Is An Audio Briefing?

A **long-form narrative explanation** designed for text-to-speech listening. Unlike STATUS.md (dashboard format) or research outputs (data-heavy), briefings are:

- **Conversational** — Written to be heard, not skimmed
- **Comprehensive** — 15-25 minutes (~2,500-4,000 words)
- **Structured** — Clear progression from basics to synthesis
- **Standalone** — No tables, no markdown formatting, no visual dependencies

---

## How To Request

**Simple:**
> "Give me an audio briefing on [AGENT]"

**With parameters:**
> "Give me a 10-minute briefing on HENRY focused on the gamma dynamics"

**Cross-agent:**
> "Give me a briefing on the full transmission chain from LABOR to REGINALD"

---

## Standard Structure

### 1. The Hook (1-2 min)
- What is this about and why does it matter?
- Set the stakes
- Preview the journey

### 2. The Foundation (3-5 min)
- Background/context the listener needs
- Key concepts explained simply
- How we got here

### 3. The Current Situation (5-8 min)
- What's happening now
- Key data points (spoken naturally, not as a list)
- Evidence and sources
- Who the players are

### 4. The Mechanics (3-5 min)
- How the system/mechanism works
- Transmission pathways
- Cause and effect chains

### 5. The Implications (3-5 min)
- What we expect to happen
- Scenario analysis
- Timeline and triggers
- Cross-agent connections

### 6. The Close (1-2 min)
- Summary of key points
- What would change our view
- What we're watching next

---

## Style Guidelines

**Do:**
- Use conversational transitions ("Let me explain...", "Here's what's interesting...", "Now let's zoom out...")
- Speak numbers naturally ("about two billion dollars", not "$2B")
- Explain jargon when first introduced
- Use analogies and examples
- Build narrative momentum
- Reference sources casually ("according to the DOJ indictment...")

**Don't:**
- Use markdown tables (can't be spoken)
- Use bullet lists (convert to prose)
- Use abbreviations without explanation
- Assume prior knowledge
- Rush through complex points
- End abruptly

---

## Agent-Specific Briefing Templates

### LABOR Briefing
1. Current employment picture (surface metrics)
2. Leading indicators (temp, WARN, hires rate)
3. The "Hotel California" dynamic
4. Danger window timing
5. What triggers the break
6. Downstream effects (CARL, REGINALD)

### CARL Briefing
1. Consumer financial health (surface vs reality)
2. Latent vulnerability (the 37%/60% populations)
3. Phantom debt and hidden leverage
4. Conversion velocity when shocked
5. Payment hierarchy
6. Geographic hotspots
7. Link to employment trigger

### REGINALD Briefing
1. Regional bank landscape
2. Key risk exposures (CRE, NDFI, consumer)
3. Specific banks on watch
4. Stress transmission mechanics
5. Historical parallels
6. What breaks and when

### HENRY Briefing
1. Current market positioning
2. Gamma/dealer dynamics
3. Key levels and triggers
4. Cascade mechanics
5. Leading indicators sequence
6. What a selloff looks like

### LIQUID Briefing
1. Plumbing 101 (RRP, reserves, SOFR)
2. Current state of the system
3. Where stress could emerge
4. Quarter-end dynamics
5. Fed response function
6. "Metastable" concept

### SAM Briefing
1. Japan macro picture
2. BOJ policy evolution
3. Carry trade mechanics
4. Yen dynamics
5. Trigger scenarios
6. Global transmission

### OTTO Briefing
1. The fraud cases (Tricolor, First Brands, PrimaLend)
2. How the fraud worked (double-pledging)
3. The "cockroach" thesis
4. Systemic picture ($1.7T NDFI)
5. ABS market stress
6. What we're watching

### MARCO Briefing
1. Migration patterns
2. Border city economics
3. State-level exposures
4. Labor market implications
5. Leading indicators (H-2A, remittances)
6. Regional transmission

---

## Output Location

Save briefings to: `AGENTS/[AGENT]/briefings/[AGENT]_Briefing_YYYY-MM-DD.md`

Example: `AGENTS/OTTO/briefings/OTTO_Briefing_2026-02-04.md`

---

## Cross-Agent Briefings

For briefings that span multiple agents, save to: `briefings/[TOPIC]_Briefing_YYYY-MM-DD.md`

Examples:
- `briefings/Transmission_Chain_Briefing_2026-02-04.md`
- `briefings/Q2_Risk_Overview_Briefing_2026-02-04.md`

---

## Duration Guide

| Request | Target Length | Word Count |
|---------|---------------|------------|
| "Quick briefing" | 5-7 min | 750-1,000 |
| "Briefing" (default) | 15-20 min | 2,500-3,500 |
| "Deep dive briefing" | 25-35 min | 4,000-5,500 |
| "Full briefing" | 35-45 min | 5,500-7,000 |

---

## Example Requests

**Basic:**
> "Give me a LABOR briefing"

**Timed:**
> "I have 10 minutes, brief me on SAM"

**Focused:**
> "Briefing on REGINALD, focus on the DC corridor banks"

**Cross-agent:**
> "Brief me on how employment breaks through to bank stress"

**Update-style:**
> "What's changed since last week? Brief me on the updates"

---

*This framework ensures consistent, high-quality audio briefings across all domains.*
