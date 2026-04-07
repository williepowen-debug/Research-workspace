# WALTER Signal Processing Checklist
**Version:** 0.1 | **Date:** April 7, 2026

One-page operational reference for processing incoming signals. Derived from 10 research prompts across emergency medicine, military communications, ATC, pub/sub systems, intelligence dissemination, emergency dispatch, scientific alerts, open output systems, newsroom editorial, and trading desk operations.

---

## PHASE 1: INTAKE (Kill or Keep — under 10 seconds)

```
1. Already known?          → KILL. Log: "already in [AGENT] STATUS."
2. In our thesis chain?    → If no: KILL. Log: "not thesis-relevant."
3. System-critical?        → If yes: skip to PHASE 3, route FLASH.
```

Most signals die here. That's correct. Target: 80-90% filtered.

---

## PHASE 2: CLASSIFY (For signals that survive intake)

**Precedence** — how fast:
| Level | Criteria | Target |
|-------|----------|--------|
| FLASH | Portfolio damage imminent, system-threatening | Immediate |
| IMMEDIATE | Thesis-critical, threshold breach, confirmed catalyst | <30 min |
| PRIORITY | Meaningful new information, requires agent analysis | Next agent boot |
| ROUTINE | Background context, monitoring update | Archive only |

**Confidence** — how much to trust:
| Language | Meaning |
|----------|---------|
| Confirmed | Multiple agents verified OR official data release |
| Reports | Single credible source with direct knowledge (Bloomberg, SEC filing) |
| Assessed | Strong indicators, inference, not direct evidence |
| Unconfirmed | Single source, no corroboration — flag heavily |

**Two-source rule:** Don't promote to IMMEDIATE+ unless corroborated. Exception: "golden source" with direct knowledge.

**Conflict zone** — relationship to thesis:
- 🟢 Confirms thesis (gas hits $4 as CARL predicted)
- 🟡 Tension — doesn't break thesis but doesn't confirm (HY OAS tightening)
- 🔴 Contradicts thesis or threatens position (major counter-signal)

**Superevent check:** Do any signals from this session GROUP into a convergence event more significant than its parts?

---

## PHASE 3: OUTPUT (Write the signal)

**Disposition** — exactly one of:
| Disposition | What happens | When |
|------------|-------------|------|
| **PUSHED** | Archive + COP update + Telegram ping to Will | FLASH / IMMEDIATE only |
| **ARCHIVED** | Signal file + COP update, agents pull at boot | PRIORITY / ROUTINE |
| **FILTERED** | Kill log entry only | Below threshold, already known, not relevant |

**Signal file structure** (three-layer tearline):

```yaml
# Layer 1 — Header (machine-scannable)
signal_id: SIG-W-YYYYMMDD-NNN
date: YYYY-MM-DD
precedence: FLASH | IMMEDIATE | PRIORITY | ROUTINE
domain: ENERGY | LABOR | CONSUMER | BANKING | JAPAN | CREDIT | PRIV_CREDIT
confidence: confirmed | reports | assessed | unconfirmed
conflict_zone: green | yellow | red
to: AGENT_NAME (action)
info: AGENT_NAME, AGENT_NAME (awareness)
```

```
# Layer 2 — Summary (human-scannable tearline, 2-3 sentences)
What happened. Why it matters. What the receiving agent should consider.
```

```
# Layer 3 — Body (full detail, read on demand)
Source material, data, cross-references, context, WALTER's analysis.
```

**Push notification format** (for FLASH/IMMEDIATE — 200 words max):
```
Signal: SIG-W-YYYYMMDD-NNN
Precedence: [LEVEL]
Pre-arrival context: [What happened + so what + what agent should do]
Full signal: AGENTS/WALTER/signals/SIG-W-YYYYMMDD-NNN.md
```

---

## QUALITY CHECKS (Before finalizing)

**ADViCE** (from trading desk morning calls):
- ☐ **Conclusion-oriented** — key fact in first sentence?
- ☐ **Differentiated** — what's NEW vs what we already knew?
- ☐ **Validated** — source cited, confidence language applied?
- ☐ **Easy to consume** — numbers with context (direction + threshold + comparison), no jargon?

**Editorial discipline** (from newsroom):
- ☐ Don't prescribe the fix — identify the conflict, let the agent decide
- ☐ Every number has context ("$977M — 5x prior record since 2010")
- ☐ Would this surprise someone who already knows the current network status? If no → don't route
- ☐ Immutable once written — supersede with new signal, never edit

**Breaking news sequence** (if story is developing):
1. Alert (now): minimum viable signal, flagged as unconfirmed
2. Update (when corroborated): upgrade confidence, expand detail
3. Writethru (when complete): supersedes all prior versions

---

## COP UPDATE DECISION

After processing all signals in a session:
- Did any FLASH/IMMEDIATE signals fire? → Update COP ⚡ section
- Did any convergence events emerge? → Update Convergence section
- Did any domain status change? → Mark with △, update domain entry
- Did any new counter-signals appear? → Update Counter-Signals section
- Did any catalysts resolve or appear? → Update Catalysts section
- Is any domain's data now >48h old? → Add [stale] flag

If nothing changed: update timestamp only. A COP with just a new timestamp honestly says "I checked and nothing moved."

---

## WHAT NOT TO DO

- Don't route signals just because they're interesting — route because they CHANGE something
- Don't write a 500-word signal when 50 words convey the same information
- Don't promote single-source claims to IMMEDIATE without corroboration
- Don't filter counter-signals harder than confirming signals (confirmation bias)
- Don't process COP updates last in a session — do it first, when judgment is freshest
- Don't edit published signals — write a new one that supersedes

---

*Operational checklist — derived from 10 research prompts | April 7, 2026*
