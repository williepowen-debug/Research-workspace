#!/bin/bash
# Check all agent OUTBOX files for 🔴 priority signals
# If found, exit 0 (urgent). If not, exit 1 (no urgent signals).
# Usage: Prome runs this after agent spawns. Exit 0 = spawn HERMES.

AGENTS_DIR="/home/moltbot/.openclaw/workspace/AGENTS"
AGENT_WS="/home/moltbot/.openclaw/agents"

found=0

# Check domain outboxes
for outbox in "$AGENTS_DIR"/*/OUTBOX.md "$AGENTS_DIR"/REGINALD/BROCK/OUTBOX.md; do
    [ -f "$outbox" ] || continue
    if grep -q '🔴' "$outbox" 2>/dev/null; then
        agent=$(echo "$outbox" | grep -oP 'AGENTS/\K[^/]+')
        echo "🔴 URGENT signal found in $agent OUTBOX"
        found=1
    fi
done

# Also check agent workspace outboxes (in case symlinks are broken)
for agent_dir in "$AGENT_WS"/*/workspace/OUTBOX.md; do
    [ -f "$agent_dir" ] || continue
    if grep -q '🔴' "$agent_dir" 2>/dev/null; then
        agent=$(echo "$agent_dir" | grep -oP 'agents/\K[^/]+')
        echo "🔴 URGENT signal found in $agent workspace OUTBOX"
        found=1
    fi
done

if [ $found -eq 1 ]; then
    echo "→ HERMES delivery recommended"
    exit 0
else
    echo "No urgent signals pending"
    exit 1
fi
