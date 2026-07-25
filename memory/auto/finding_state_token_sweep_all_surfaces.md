---
name: finding_state_token_sweep_all_surfaces
description: "When a gate/decision state flips (e.g. FIRED-UNEXECUTED → RESOLVED), sweep the state-token across ALL surfaces — live ledgers (VX/KB.tsv) and live templates/setups too, not just STATUS/SCRATCH; scope the verification grep from repo root."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 04386644-14e3-4165-9c81-a09cd5ef209f
---

When a gate or decision state-token changes (e.g. `FIRED-UNEXECUTED` → `RESOLVED-ARMED / Will NO-ADD`), the stale token hides in **secondary live surfaces** beyond the obvious STATUS/SCRATCH prose: workbook **ledgers** (`VX.tsv` escalation-rationale column, `KB.tsv` disposition clause) and **live templates/setups** (a grading template PROME grades against at 4 PM is a live instrument, not a doc). Fixing only STATUS/SCRATCH leaves the ledger/template carrying the wrong gate-state — the secondary-surface-rot class ([[finding_seeded_selfsweep_secondary_surface_rot]], [[finding_ledger_drift_behind_narrative]]).

**Why:** PROME had to flag the same stale token three times because each pass I scoped the sweep too narrowly (STATUS prose → then STATUS+SCRATCH → then found VX+template myself). Distinguish LIVE surfaces (fix) from point-in-time **delivered artifacts** (outbox memos, sent messages) — those are true-when-written records; don't rewrite history, add a dated correction banner if miscitation risk is real.

**How to apply:** On any state-token flip, run the verification grep **from repo root** across `--include="*.md" --include="*.tsv"` covering STATUS, SCRATCH, workbook ledgers (VX/KB/FLOW), and setups/templates; exclude `outbox/` (delivered records). Grep must return empty before claiming clean. CRLF-safe edits on `.tsv` (byte-replace, preserve `\r\n`) per [[finding_crlf_textmode_tsv_flip]]. Confirm with the actual grep output line, not a claim.
