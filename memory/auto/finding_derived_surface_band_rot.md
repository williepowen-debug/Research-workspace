---
name: finding-derived-surface-band-rot
description: "Static threshold-band tables in derived/consumer docs rot silently into mis-routers — sweep derived surfaces when canon bands move; every band row needs owner+canonical-source"
metadata:
  node_type: memory
  type: feedback
---

**Finding (2026-07-01):** WALTER's routing guide (`skills/walter/references/agent-directory.md`) carried a static Green/Yellow/Red threshold table that canon had long moved past: HY OAS "<300 green" while the live X1 trigger was **>280** (so a 278 print — 5bp from trigger — would grade GREEN and route deprioritized); CCC/HY "red >2.8" vs the live 3.6× tripwire; USD/JPY "red >158" vs the 162-163 MOF zone. Nothing ever swept it because no row carried an owner or source — the canonical bands live in `config.py` / LIQUID's KILL_MEMO / intake-lane alerts, and updates there never propagated. Found only on a FULL file read during an adjacent fix (the spawn-column sweep, 40 lines above — [[finding_followup_audit_pass]]).

**Why:** a stale band table in a derived doc is worse than no table — it looks authoritative and silently mis-grades live signals at the routing layer, upstream of every consumer.

**How to apply:** (1) when a canonical trigger band changes, grep derived surfaces (`skills/`, `references/`, agent guides, dashboards) for hardcoded bands of the same indicator and sweep them in the same pass; (2) any threshold table outside the owner doc must carry owner + canonical source per row ([[finding-number-carries-threshold-unit-source]]) or be replaced with a pointer; (3) when fixing one defect in a reference doc, full-read it for siblings of the same class before committing.
