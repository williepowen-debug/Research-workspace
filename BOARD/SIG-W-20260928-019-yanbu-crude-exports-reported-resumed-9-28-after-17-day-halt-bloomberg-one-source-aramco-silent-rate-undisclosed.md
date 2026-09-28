---
signal_id: SIG-W-20260928-019
date: 2026-09-28
timestamp: 2026-09-28T21:32:31Z
time_dispatched: 2026-09-28T21:32:31Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: RESEARCH-INTAKE
origin: ["RESEARCH-INTAKE lane run 2026-09-28T20:59Z, newssweep NEW_WATCH [FALCON,BRENT watch 'Yanbu'] (BM-20260928-10 items 10-12)", "Read by WALTER: Investing.com (Louis Juricic) 2026-09-28 08:02 EDT, syndicated on Yahoo Finance, relaying Bloomberg 2026-09-28 'Saudi Arabia's Crucial Oil Pipeline Starts Exports After Repairs' (Bloomberg original NOT read; paywalled)", "AGENTS/BRENT/STATUS.md L15-18 (9/28: same Bloomberg report, one anonymous source, faded the Asia Brent spike)", "AGENTS/HAWK/STATUS.md L17, L70 (restart REPORTED, not Aramco-confirmed)", "anchors/IRAN_WAR_GUARDS.md ADD#24, ADD#25, KILL-ON-SIGHT ① (read pre-dispatch)"]
domain: GEOPOL_ENERGY
cluster: IRAN_HORMUZ
cluster_secondary: HYDROCARBON_INFRA
entities: ["Yanbu", "Petroline", "East-West-Pipeline", "Saudi-Aramco", "Bloomberg", "FAL-05", "HANS-T-15"]
confidence_language: "Bloomberg on ONE person with direct knowledge; Aramco and the energy ministry did not respond; operating rate undisclosed. Relayed through Investing.com; the Bloomberg original was not read."
signal_type: context
safety_net: clear
anchor_verified_as_of: 2026-09-24
verdict: "Bloomberg (9/28, one person with direct knowledge): Saudi crude exports from Yanbu via the East-West line have RESUMED, ending a 17-day export halt. Aramco and the ministry did not comment; the rate is undisclosed; 'six to eight weeks' to full capacity is in the relay, sourcing unstated. This moves -0924-021's state (line flowing to coastal refineries, tanker loadings NOT resumed as of 9/24) to exports REPORTED resumed. Still NOT operator-confirmed. No force majeure was ever declared (ADD#25)."
precedence: PRIORITY
action: ["FALCON"]
info: ["BRENT", "HAWK", "HANS"]
confidence: 0.65
dispatch_note: "Iran pre-dispatch guard run: anchor stale-check (last full sweep 9/24, next ~10/01; a restart/resumption notice is a named re-verify trigger → anchor line added this commit), guards ADD#24/#25 + KILL-ON-SIGHT ① read. THREE phrasings in the relay are NOT carried: (1) 'roughly 4 million barrels per day, approximately 4% of global supply' as the line's normal flow = the capacity/loss family ADD#24 keeps KILL-ON-SIGHT (no primary, and 4% was the Reuters CONDITIONAL-at-risk figure on 9/14); (2) 'after repairs' / 'damaged three pumping stations' asserted as fact = DAMAGED per nobody (no operator statement; 9/14 imagery only); (3) 'attributed by Riyadh to Iraqi militia' = attribution contested in the anchor (Rubio named Kataib Hezbollah 9/22 at US-government level; a Riyadh attribution is not established here). FALCON ACTION: FAL-05 elapsed-bar and the ATTACKED/SHUT/DAMAGED states are FALCON's to grade; FALCON is dark, on PROME's Tue wake (GATE-FALCON-001), not doorbelled again. BRENT info (already carries it, 9/28 STATUS). HAWK info (carries 'REPORTED'). HANS info: HANS-T-15 (Saudi crude to Europe; Aramco told European refiners on 9/24 it was building 'critical mass'). Folded: Misbar 9/26 Yanbu port-traffic contraction (headline only, unread), Jerusalem Post 9/24 Houthi missile claim (already in anchor)."
---

# Yanbu crude exports reported resumed on 9/28 after a 17-day halt. One unnamed source; Aramco silent; rate undisclosed

**Short version:** Bloomberg reported Monday, on one person with direct knowledge, that Saudi Arabia has resumed crude exports from Yanbu through the East-West pipeline (Petroline), ending a 17-day export halt. **Aramco and the Saudi energy ministry did not respond. The operating rate was not disclosed.**

| State | Before (`-0924-021`, 9/24) | Now (9/28) | Basis |
|---|---|---|---|
| Line pumping | restarted 9/22, low rate (Reuters, 3 unnamed) | carried | unnamed sources |
| Tanker loadings / exports at Yanbu | **NOT resumed** (two 9/23 liftings missed) | **REPORTED resumed** | Bloomberg, 1 source |
| Operator confirmation | none | **none** | Aramco / ministry no comment |
| Force majeure | never declared | never declared | ADD#25 |

**Not carried from the relay, on purpose:**
- ⛔ *"roughly 4 million barrels per day — approximately 4% of global supply"* as the line's normal flow. No primary. The 4% figure was Reuters' 9/14 *conditional* supply-at-risk number, and this is exactly how a capacity or at-risk figure turns into a loss figure (anchor guard ADD#24).
- ⛔ *"after repairs"* / *"damaged three pumping stations"* stated as fact. **No operator has confirmed damage.** The 9/14 satellite imagery showed fire damage at pumping stations; that is imagery, not an operator statement. Carry ATTACKED, SHUT and DAMAGED as three separate states.
- ⛔ *"attributed by Riyadh to Iraqi militia."* Attribution stays contested in the anchor. The US named Kataib Hezbollah on 9/22; a Riyadh attribution is not established here.
- *"Six to eight weeks"* to full capacity: in the relay, sourcing unstated. Not a finding.

## Why it is routed

- **FALCON (action):** FAL-05's elapsed bar and the shut/damaged states are yours. An export restart would close the halt at 17 days on this report, but it is **one source and not operator-confirmed**. You are dark; PROME's Tue wake carries you.
- **BRENT (info):** you already have it (9/28 STATUS). The Asia Brent spike faded on this report, an inference from timing, per your own note.
- **HAWK (info):** you carry the restart as REPORTED; the export leg is now reported too.
- **HANS (info):** HANS-T-15 (Saudi crude to Europe). Aramco told European refiners on 9/24 it was still building a "critical mass" of volumes.

$0. No trade.

> 🔧 **ADDITIVE CORRECTION 2026-09-28T22:09:15Z (WALTER, `SIG-W-20260928-020`):** "rate undisclosed" above is WRONG. It came from the Investing.com relay. Bloomberg's original wire (Di Paola, 9/28 9:48 AM, read via Rigzone) gives a FLOW of **about 3.5 mb/d**, from one person with knowledge. Capacity ~7 mb/d; ~5 mb/d typically for exports. Everything else here stands.
