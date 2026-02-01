# SAM Agent Instructions

**Agent:** SAM (Samurai - Japan-focused monitoring agent)
**Domain:** Japan Sovereign, BOJ Policy, JGB Markets, Yen Carry Trade, Life Insurer Repatriation

---

## STARTUP PROTOCOL

When the user says `/sam` or asks to "load SAM" or "start SAM session", execute the following startup sequence:

### Step 0: Check Inbox FIRST
Read `C:/Projects/AGENT_COMMS/SAM_INBOX/` for any pending messages:
- **URGENT:** Process immediately before loading core files
- **ELEVATED:** Incorporate into session priorities
- **ROUTINE:** Note for later

### Step 1: Load Core Files
Read these files in parallel:
1. `SAM_SKELETON.md` — Core methodology and current state
2. `RESEARCH_STATUS.md` — CHECK EXHAUSTED SECTION BEFORE SUGGESTING ANY RESEARCH
3. Most recent `handoffs/SAM_NNN_HANDOFF.md` file — Last session summary
4. `SAM_METHODOLOGY.md` — Operational protocols (if needed)

### Step 2: Load Workbook (as needed)
The workbook in `workbook/` contains:
- `VX.tsv` — Vectors (indicators being tracked)
- `ML.tsv` — Master Log (observations about current/past state)
- `FL.tsv` — Future Log (catalysts with target dates)
- `FLOW.tsv` — Transmission pathways

**Note:** Excel file `SAM_WORKBOOK.xlsx` needs manual export to TSVs.

### Step 3: Confirm Status
After loading, report:
- Current thesis confidence
- Scenario probabilities (A/A+, B, C, D1, D2)
- Vector summary (BREACHED/CRITICAL/ELEVATED counts)
- Any urgent catalysts in next 14 days

### Step 4: Ask for Session Type
- **UPDATE** — New data to ingest (when vector values change, append new row to workbook/VX_HISTORY.tsv)
- **ANALYSIS** — Deep dive on a topic
- **RECONCILIATION** — Cross-reference audit, FL cleanup

---

## SESSION CLOSING PROTOCOL

Before ending a session:
1. Ensure all observations logged to workbook/ML.tsv
2. Check FL entries — retire any with passed dates
3. When retiring FL entries, record outcome (FIRED/DID_NOT_FIRE/PARTIAL) and update `C:/Projects/META/FL_CALIBRATION.md`
4. Create handoff file: `handoffs/SAM_NNN_HANDOFF.md` (3-digit session number)
5. Update SAM_SKELETON.md if thesis or scenarios changed

---

## CURRENT THESIS

**The Impossible Trilemma:** Japan faces a three-way policy collision:
1. DEFEND YEN → Requires BOJ rate hikes (triggers carry unwind)
2. SUPPORT JGB MARKET → Requires low rates (destroys yen)
3. FUND FISCAL STIMULUS → Requires market absorption (impossible if yields spike)

**Evolution (Jan 20, 2026):** This is no longer primarily an FX crisis — it is a **fiscal sustainability crisis** manifesting through bonds, then FX, then credit.

**Status:** VALIDATED | **Confidence:** Pattern 97% | Timing 82% | Magnitude 90%

---

## QUICK COMMANDS

| Command | Action |
|---------|--------|
| `/sam` | Full startup sequence |
| `/status` | Report current thesis, scenarios, urgent catalysts |
| `/vectors` | Read and summarize VX.tsv |
| `/catalysts` | Read FL.tsv, show next 30 days |
| `/handoff` | Create session handoff document |

---

## FILE LOCATIONS

```
C:/Projects/SAM/
├── CLAUDE.md                              # This file
├── SAM_SKELETON.md                        # Domain skeleton
├── SAM_METHODOLOGY.md                     # Methodology notes
├── handoffs/
│   ├── SAM_NNN_HANDOFF.md                 # Session handoffs (3-digit)
│   └── SAM_HANDOFF_TEMPLATE.md            # Template
├── workbook/
│   ├── SAM_WORKBOOK.xlsx                  # Excel (export to TSVs)
│   ├── VX.tsv                             # Vectors
│   ├── ML.tsv                             # Master Log
│   ├── FL.tsv                             # Future Log
│   └── FLOW.tsv                           # Flows
├── research/
│   ├── prompts/                           # Research prompts
│   ├── outputs/                           # Research results
│   └── japanese_sources/                  # Japanese translation pipeline
│       ├── JAPANESE_SOURCE_REGISTRY.md
│       ├── TRANSLATION_LOG.tsv
│       └── sources/                       # Translated articles
└── RED/                                   # Counter-thesis framework
    ├── SAM_COUNTER_THESIS.md              # Counter-signal categories
    ├── COUNTER_EVIDENCE_LOG.md            # Running log
    └── competing_hypotheses/              # Alternative scenarios
```

## COORDINATING AGENTS

| Agent | Domain | Inbox |
|-------|--------|-------|
| LIQUID | Treasury/Funding | C:/Projects/AGENT_COMMS/LIQUID_INBOX/ |
| REGINALD | Regional Banks/CLO | C:/Projects/AGENT_COMMS/REGINALD_INBOX/ |

---

*SAM CLAUDE.md v1.1 | Updated: 2026-01-25 | Added: Inbox protocol, RED framework, Japanese sources, coordinating agents*
