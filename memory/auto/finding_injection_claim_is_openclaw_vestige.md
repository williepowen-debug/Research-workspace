---
name: finding_injection_claim_is_openclaw_vestige
description: "verify a file is actually boot-loaded before calling it load-bearing; SOUL/USER/AGENTS \"always injected\" is vestigial"
metadata: 
  node_type: memory
  type: finding
  originSessionId: d57ee8fe-0139-4656-99e7-3fc535618b68
---

PROME boot docs (`SYSTEM.md` "Boot Trust Stack", `BOOT.md`) bill `AGENTS.md` / `SOUL.md` / `USER.md` as "always injected in main sessions" with high trust. **This is an OpenClaw-era vestige and is FALSE in Claude Code:** only `CLAUDE.md` files (root + nested) and the auto-memory `MEMORY.md` are truly auto-injected. SOUL.md was NOT `@`-imported by any CLAUDE.md and was NOT in PROME's boot context (verified 2026-06-30 — PROME booted without it and nothing changed).

This is the **same class** as the HEARTBEAT.md mislabel corrected 2026-06-27 (docs claimed auto-injection; reality = explicit-read only).

**Why:** trusting the doc's claim led me to almost call SOUL.md "load-bearing / strips PROME's persona at boot" when Will deleted it — but it was harmless, because it was never actually loaded. A doc's *injection claim* is not evidence the file is *actually in context*.

**How to apply:** before calling a file load-bearing because "the docs say it's injected," verify it was actually in the boot context (or `@`-imported by a CLAUDE.md). If not, the claim is vestigial — say so, don't propagate it. Fix these specific stale claims during the public-prep dangling-ref sweep: `PROME/{BOOT,SYSTEM,CLAUDE,AUTONOMY}.md`. Related: [[finding_governance_doc_stale_default_drift]], [[finding_just_read_artifact_frame_contamination]].
