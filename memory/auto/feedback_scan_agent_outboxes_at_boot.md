---
name: scan-agent-outboxes-at-boot
description: "When booting PROME, scan AGENTS/*/outbox/ for PROME-targeted signals — not just AGENTS/PROME/inbox/ — to close the outbox-resident signal discovery gap"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 34d1328c-d6e8-433a-9a51-08ce3b96c4b3
---

When booting PROME (either Claude Code or OpenClaw surface), scan `AGENTS/*/outbox/` for files matching `*to-PROME*` (or similar conventions indicating PROME is the intended recipient) — not only `AGENTS/PROME/inbox/`.

**Why:** Agents follow two routing conventions when sending PROME-bound signals, and only one of them gets discovered without the outbox scan:

- **Convention A — Direct inbox write:** Sender writes directly to `AGENTS/PROME/inbox/`. Requires per-instance Will authorization per the [[cross-agent-inbox-writes-exception-only]] rule. Discovered at boot via standard PROME/inbox triage step.
- **Convention B — Own-outbox write:** Sender writes to own `AGENTS/<SELF>/outbox/` with a filename like `2026-05-21_to-PROME_<slug>.md` and expects PROME to scan for it. Avoids the Will-authorization gate. **Currently undiscovered without explicit outbox scanning.**

Convention B is more cautious and more common — agents prefer not to gate every routing decision on a Will-authorization. SAM uses it as his default. But Convention B requires PROME-side proactive scanning to close the loop. Without that, signals sit undiscovered in sender outboxes until something else surfaces them.

**Concrete instance (2026-05-21):** SAM filed `AGENTS/SAM/outbox/2026-05-21_to-PROME_sam-position-state-for-forge-rehab.md` at ~12:35 ET asking PROME to do FORGE rehab (FORGE/STATUS Mar 25 stale, FXY position shown wrong, 6 expired options listed as active). CC-Prome booted at ~15:35 ET — 3 hours later — and did NOT discover this signal. Only found it when Will explicitly told CC to verify SAM Tranche 2 status, which led CC to read SAM's outbox. The 3-hour discovery delay would have been longer if Will hadn't redirected.

**How to apply:**

1. **Add to boot procedure (PROME/BOOT.md) between COMM check (step 7) and inbox triage (step 8):**
   ```
   7.5. Scan agent outboxes for PROME-targeted signals — 
        `git log --since="3 days ago" --diff-filter=A --name-only -- 'AGENTS/*/outbox/*'` 
        then filter by `*to-PROME*` / `*to-prome*` / `*to_PROME*` patterns.
        Read any unfound signal; respond per its priority.
   ```
2. **3-day lookback window** is right for daily-active PROME; longer for revival scenarios.
3. **Filename convention matters.** Encourage agents to use `*to-PROME*` consistently in outbox filenames so the grep is reliable. If an agent uses a different convention (e.g., `*for-prome*`), update the search pattern.
4. **Per `[[messaging-system-overhaul]]` the file-based system is being replaced** — but until the replacement ships, this gap is real. Treat as an interim fix.
5. **The COMM mailbox** (`PROME/COMM/TO_CLAUDE_CODE/` and `TO_OPENCLAW/`) is a cleaner channel for cross-surface PROME-to-PROME work — but it does NOT cover agent-to-PROME signals, which still go through `AGENTS/PROME/inbox/` (Convention A) or `AGENTS/<SELF>/outbox/` (Convention B).

Related: [[cross-agent-inbox-writes-exception-only]] (Convention A authorization rule), [[messaging-system-overhaul]] (file-based system being replaced), [[verify-state-before-propagating]] (the structural-staleness corollary).
