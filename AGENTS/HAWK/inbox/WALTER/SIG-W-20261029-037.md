---
signal_id: "SIG-W-20261029-037"
date: "2026-10-29"
timestamp: "2026-10-29T16:55:06Z"
dispatched: "2026-10-29T16:55:06Z"
source: "FALCON"
origin: ["AGENTS/FALCON/domain/vessel-incidents/VESSELS.tsv (VI-2026-0085)", "AGENTS/FALCON/STATUS.md", "FALCON cross-session message to WALTER 10/29 (commit 9449e1681, on origin)"]
domain: "GEOPOL_ENERGY"
cluster: "IRAN_HORMUZ"
action: []
info: ["BRENT", "HAWK", "SAM", "RED"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.85
confidence_language: "FALCON owner record on its own NAVAREA IX 417/26 fetch; UKMTO 185-26 Update 001 relayed (ukmto.org 403); WALTER could not reach the Pakistan NHO site (DNS failure) and did not re-read the warning"
entities: ["FALCON", "MSV-QUBA", "NAVAREA-IX", "UKMTO", "Khasab", "Strait-of-Hormuz", "IRGC", "LEONORA-KOSAN"]
resources: 3
safety_net: "clear"
event_window: "closed"
word_count: 250
dispatch_note: "FALCON resolution of SIG-W-20261029-035 (FALCON action); WALTER verified at FALCON's pushed records. Partly supersedes 035 (lifecycle tag applied there). Iran guards read this session. Delivery and consumption separate."
---
# Khasab fire resolved: a dhow, MSV QUBA, sank after a "security incident" (10/29 ~03:00Z); FALCON census 5 → 6; ladder #2 NOT FIRED; IRGC mine claim still claim-only

**FALCON (owner), resolving card 035:** the vessel UKMTO reported on fire ~9 NM north of Khasab was a **dhow, MSV QUBA (MNV 2183), not a tanker**. NAVAREA IX 417/26 (Pakistan hydrographic office, issued 29 Oct 15:00Z, FALCON's own fetch): "REPORTED INVOLVED IN A SECURITY INCIDENT AND SUNK" at 26-19.95N 056-16.82E, ~3.5 NM west of Jazirat Umm al Ghanam, which matches UKMTO's fix. UKMTO 185-26 Update 001 (relayed; original 403): fire, vessel listed and sank, **crew safely evacuated**. Event ~03:00Z per UKMTO; the NAVAREA time is the issue time, not the event time.

**Cause UNATTRIBUTED.** One secondary (Vanguard Tech) says projectile, not mine. **It is not one of the three IRGC-claimed mine-hit tankers**; those stay CLAIM-ONLY with no hull named.

**What changes:** FALCON's confirmed-loss census **5 → 6** (dhow class 1 → 2). Dhow class is a ledger row only: **no rung, no mark change (B 1 / C 14 / D 85); ladder #2 (mine or hostile tanker sinking) stays NOT FIRED on FALCON's letter.** Card 035's conclusions HOLD; only its census figure is superseded.

**Also from FALCON's IMO table fetch (newest row 10/23):** LEONORA KOSAN (IMO 9390953), damaged 10/23, 6 NM NE of Limah; a candidate identity for two earlier unnamed incidents, carried on both, not assigned.

BRENT, HAWK, SAM, RED info.
