# CLAUDE.md - Trump Financial-Policy Network

## WHAT THIS IS

Political-financial intelligence project mapping conflicts of interest between Trump 2.0 officials and companies benefiting from their policy decisions. Focus on tradeable positions and documented patterns.

---

## BOOT SEQUENCE

1. Read this file
2. Read `STATE.md` (current status, active triggers)
3. Read latest session handoff in `handoffs/`
4. **Check `C:/Projects/AGENT_COMMS/TRUMP-NETWORK_INBOX/`** — Process any cross-agent messages
5. Load domain files as needed for the task

### Inbox Processing (Step 4)
If messages exist in inbox:
- Read each message
- Acknowledge by creating response in sender's inbox (if required)
- Update relevant domain files with cross-agent intel
- Move processed messages to `TRUMP-NETWORK_INBOX/processed/`
- Note in handoff: "Processed N messages from [AGENTS]"

---

## STRUCTURE

```
/TRUMP-NETWORK
├── CLAUDE.md              # This file - read first
├── STATE.md               # Current status, triggers, quick reference
├── domains/
│   ├── defense/           # C1, C5, C12 - 1789, Pentagon, Rocket Lab
│   ├── housing/           # C10, C11 - Pulte, Turner, SFR/BTR
│   ├── energy/            # C7 - Wright, Zeldin, Burgum
│   ├── finance/           # C2, C3, C4 - SEC, Cantor, Treasury
│   ├── media/             # C6 - FCC, Rumble
│   └── cross-domain/      # Leo, Miller, P2025, SCOTUS
├── reference/
│   ├── PATTERNS.md        # 27 validated patterns
│   ├── EXHAUSTED.md       # Dead ends - DO NOT RE-INVESTIGATE
│   └── METHODOLOGY.md     # Research methods, evidence standards
├── handoffs/              # Session handoff notes
├── research/
│   ├── prompts/           # Research prompts for external LLM
│   └── results/           # External research results
├── data/                  # Original unified TSV files (backup)
└── archive/               # Pre-reorganization backups
```

---

## DOMAIN QUICK REFERENCE

| Domain | Clusters | Key Tickers | Key Nodes |
|--------|----------|-------------|-----------|
| defense | C1, C5, C12 | PLTR, RKLB, VLD | Feinberg, Witt, 1789 |
| housing | C10, C11 | PHM, INVH, AMH | Pulte, Turner |
| energy | C7 | OKLO, LBRT, CVX | Wright, Zeldin, Kushner |
| finance | C2, C3, C4 | BTGO, SECZ, XXI | Atkins, Sacks, Lutnick |
| media | C6 | RUM, SBGI, NXST | Carr, Sinclair |
| crypto | C13 | XRP, BTGO, COIN | Sacks, Lutnick, Garlinghouse, Atkins, Witkoff |
| cross-domain | ALL | - | Leo, Miller, Vought |

---

## WORKING IN A DOMAIN

When user asks about a topic:
1. Identify the relevant domain
2. Read `domains/[domain]/OVERVIEW.md`
3. Load that domain's TSV files (`nodes.tsv`, `edges.tsv`, `catalysts.tsv`)
4. Check `cross-domain/` for related connections

---

## OPERATIONAL PREFERENCES

**Autonomy:** Run research threads autonomously. Report back with findings. Check in for major direction changes.

**Low-profile:** No FOIA, no paper trails, passive monitoring only, OSINT only.

**Documentation:**
- Update TSV files as you work (don't batch)
- Session handoffs: focus on deltas, decisions, system changes
- Document dead ends immediately in RESEARCH_STATUS.md
- Always note sources

**Evidence standards:**
- CONFIRMED = primary source (SEC, OGE 278, official)
- HIGH = strong circumstantial, multiple sources
- Speculative okay if flagged

---

## CRITICAL RULES

1. **CHECK EXHAUSTED FIRST**: Before suggesting any research direction, check `reference/EXHAUSTED.md`. Topics there require non-OSINT to unlock.

2. **AUTO-GENERATE PROMPTS**: When new threads emerge, write research prompts to `research/prompts/` without waiting to be asked.

3. **PATTERNS HAVE LIMITS**: 84-Day OSC Loop only works for rare earths. Defense tech follows Reverse Signal pattern.

---

## OUTPUT FORMAT FOR NEW DATA

```
N-XXX	Name	Type	Cluster	Role	Policy_Control	Holdings	Tickers	Status
E-XXX	N-From	N-To	TYPE	Evidence	CONFIRMED	Source	2026-XX-XX
```

---

## SESSION CLOSING PROTOCOL

Before ending a session:

1. **Update domain files** — Add new nodes/edges/catalysts to relevant domain TSVs
2. **Update STATE.md** — If triggers, confidence, or thesis changed
3. **Check invalidation criteria** — Note any that moved closer to firing
4. **Cross-agent signals** — If findings relevant to other agents, send to their inbox
5. **Create handoff** — Use `handoffs/HANDOFF_TEMPLATE.md` format
   - File name: `TRUMP-NETWORK_NNN_HANDOFF.md` (3-digit session number)
6. **Update reference files** — If new patterns discovered, add to `reference/PATTERNS.md`

---

## HANDOFF RULES

1. **DO NOT repeat:** Full pattern list, all tickers, complete node roster
2. **DO include:** What changed, what's new, what to do next
3. **Target length:** 80-120 lines
4. **Cross-agent signals:** Note if sent to other agent inboxes

---

*For questions about Claude Code itself, use Task tool with subagent_type='claude-code-guide'*
