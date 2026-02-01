---
name: carl
description: Initialize a CARL (Consumer Aggregate Risk Ledger) session. Loads boot document, latest handoff, checks for incoming state vectors, and prompts for session type.
---

# CARL Session Initialization

You are initializing a CARL (Consumer Aggregate Risk Ledger) session. Follow these steps precisely:

## Step 1: Load Core Documents

Read these files in parallel:
1. `CORE/CARL_BOOT.md` - Current system state and operations manual
2. `CORE/CLAUDE read me first.md` - Quick reference

## Step 2: Load Latest Handoff

Find the most recent handoff file in `handoffs/` (highest CARL number). Read it to understand:
- What was accomplished last session
- Current priorities
- Open questions
- Synthesis questions to verify understanding

## Step 3: Check Incoming State Vectors

Check `SUB-AGENT COMMUNICATIONS/state_vectors/incoming/` for any new state vectors from subordinate agents (NICK, POLLY, DOC, POP, GIG). List any found.

## Step 4: Session Initialization

After loading documents, present:

1. **Quick Status Summary:**
   - Thesis status and confidence
   - Phase position
   - Vectors status (BREACHED/CRITICAL/ELEVATED/WATCH counts)
   - Any incoming state vectors to process

2. **Synthesis Check:** Answer the synthesis questions from the latest handoff to confirm understanding

3. **Priority Catalysts:** List upcoming FL entries by date

4. **Ask user to declare session type:**
   - UPDATE - Ingest new data, process state vectors
   - ANALYSIS - Deep dive on specific question
   - RECONCILIATION - Cross-reference audit, cleanup
   - DEVIL'S ADVOCATE - Challenge thesis (Red Team)

5. **Confirm priorities** from the handoff and ask if the user wants to adjust

## Working Directory

All file paths are relative to the CARL project root:
`C:\Projects\CARL (CONSUMER STRENGTH)\CARL`

## Session Protocol Reminder

- Log observations immediately (ML for current state, FL for future-dated, FLOW for mechanisms)
- Include interpretation, not just data
- Tag diagnostic value (HIGH/MEDIUM/LOW/ZERO)
- Cross-reference everything
- At session end: Create lean handoff, update boot doc if state changed
