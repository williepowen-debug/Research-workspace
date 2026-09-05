---
name: finding_a_registry_reclassification_is_an_interface_consumers_guard_one_way
description: "Changing an agent's classification in a registry (ROSTER retire/promote/re-class) is an INTERFACE change, not a local edit — downstream consumers (generators, boot-read indexes, co-registration guards) may guard only ONE direction and be structurally blind to the other. A co-registration guard that catches 'live agent missing from the map' can be blind to 'retired agent still hardcoded in the map', so a retirement propagates silently as a boot-read index advertising a dead desk as LIVE, rc=0. When you change a registry classification, audit consumers for BOTH directions. PROME/YEYOU 2026-09-05."
metadata:
  node_type: memory
  type: feedback
symptoms: "retired an agent and a generated index still lists it · boot-read directory advertises a dead desk as live · the guard only checks one direction · co-registration guard blind to retirement · a hardcoded map kept a name after ROSTER dropped it · rc=0 while the output is wrong · ROSTER change broke a downstream tool silently · classification change is an interface"
---

**A registry classification change (retire, promote, re-class an agent in ROSTER / a fleet map) is an INTERFACE change — it has consumers, and a consumer can be structurally blind to the direction you just changed.** The edit looks local (one line moved between sections); its blast radius is every tool that reads the registry.

**Concrete (PROME retiring YEYOU, 2026-09-05):** the ROSTER edit moved YEYOU SPECIAL→RETIRED. DAEDALUS's `render_directory.py` kept YEYOU in its **hardcoded** SPECIAL map for hours and exited **rc=0** — so the boot-read directory index was advertising a **retired desk as live**. The co-registration guard existed, but it only ever fired on the *opposite* direction (a live ACTIVE/TIER-2 agent MISSING from FLEET_MAP); it was blind to a retired agent still PRESENT in the map. One-directional guard, silent failure, wrong boot-read surface.

**Why it's the session's recurring shape:** a guard that only works one way is the same family as a flag resolved in the wrong direction (`[[finding_a_flag_resolved_in_the_wrong_direction_launders_the_defect]]`) and a default-zero leg that certifies by never firing (PAT-060) — the check runs, returns green, and the defect ships. The common tell: **rc=0 is not evidence the output is right; it's evidence nothing that ran objected.**

**How to apply:**
- **Treat a ROSTER/registry reclassification as an interface change with a consumer list.** After it, ask "what reads this section, and does each reader handle the direction I changed?" — not just "is my edit correct?"
- **Record a reclassification BOTH ways** where readers key off form: the RETIRED section AND a bold `NAME — RETIRED` line where the agent used to sit, so a consumer keyed on either surface sees it (this is what let DAEDALUS's fixed guard read the retirement).
- **A guard that has only ever fired one direction is untested in the other** — a retirement/removal is rarer than an addition, so the removal path ships unexercised. Falsify it on the rare direction before trusting it.
- PROME owns ROSTER, so PROME owns the interface: at least one consumer (a boot-read index) had no retirement guard, and others keyed off ROSTER sections may share the blind spot — the consumer audit is the owner's, not the reader's.
- **The blast radius is EVERY surface that enumerates the fleet, not just tools that key off the registry** (n=2 within one afternoon: DAEDALUS's `render_directory.py` AND a **hardcoded six-desk list in a blueprint scope line** that was not keyed off ROSTER at all — which is exactly why nothing caught it). **Enumerations do not announce themselves.** So the retirement audit must sweep hardcoded name-lists (blueprint scope lines, adjudication rosters, per-agent maps) as well as registry-reading tools — grep the retired name fleet-wide, don't just check the declared consumers.
