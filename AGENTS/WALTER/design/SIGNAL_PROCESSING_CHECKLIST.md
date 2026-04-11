# WALTER Signal Processing Checklist
**Version:** 0.3 | **Date:** April 10, 2026 (confidence model reconciled with FORMAT_SPEC) | **v0.2:** April 10, 2026 (worked example added) | **v0.1:** April 7, 2026

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

**Confidence** — how much to trust. TWO bound fields, both required:

| `confidence_language` | `confidence` band | Meaning |
|-----------------------|-------------------|---------|
| `confirmed` | **0.90–1.0** | Official data release (BLS, FRED, SEC, central bank) OR multiple independent authoritative sources verifying same fact |
| `reports` | **0.75–0.89** | Single credible named source with direct knowledge (Bloomberg, Reuters, SEC filing, named analyst) |
| `assessed` | **0.50–0.74** | Strong indicators, agent synthesis or inference, not direct evidence |
| `unconfirmed` | **0.30–0.49** | Single source, no corroboration — flag heavily, usually shouldn't route |
| (filtered) | **<0.30** | Below threshold — kill log, not the archive |

The numerical score lives in the YAML header for machine routing. The language tier is a SECOND header field bound to the score. They cannot disagree. See SIGNAL_FORMAT_SPEC.md "Confidence Model" section for full mapping rules and adjustment factors.

**Two-source rule:** Don't promote to IMMEDIATE+ unless corroborated. Exception: "golden source" with direct knowledge (single official release like a BLS print can stand alone at `confirmed`).

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
# NOTE: SIGNAL_FORMAT_SPEC.md is the canonical schema. This shows the
#       confidence-related fields only. See FORMAT_SPEC for the full header.
signal_id: SIG-W-YYYYMMDD-NNN
precedence: FLASH | IMMEDIATE | PRIORITY | ROUTINE
confidence: 0.0–1.0           # numerical score for machine routing
confidence_language: confirmed | reports | assessed | unconfirmed   # human tier, bound to score
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

## WORKED EXAMPLE: CPI March + UMich April Preliminary (2026-04-10)

This example walks the checklist top-to-bottom on a real input. It shows what each step LOOKS LIKE in practice and validates that the checklist produces a clean routing decision.

### Raw Input

- **Source:** Will Telegram message ("CIP and UM sentiment - can you pull that data up?") → fetched CPI from FRED via FORGE/tools/market-data, fetched UMich Apr preliminary via WebSearch
- **Time:** 2026-04-10 ~17:30 UTC
- **Content:** CPI March: headline +0.86% MoM / +3.28% YoY, core +0.21% MoM / +2.61% YoY. UMich April preliminary 47.6 (record low, below 50 Biden trough). 1Y inflation expectations 4.8% (from 3.8%), 5-10Y expectations 3.4% (from 3.2%). 98% of UMich interviews conducted before Iran ceasefire announcement.

### PHASE 1: Intake — Kill or Keep?

| Check | Result | Reason |
|-------|--------|--------|
| Already known? | NO — KEEP | Both prints released today, fresh information |
| In our thesis chain? | YES — KEEP | Touches LABOR_DOWNSTREAM (CARL), market structure (HENRY), credit (LIQUID), thesis (RED), Japan (SAM via Fed reaction) |
| System-critical? | NO — continue to Phase 2 | Not portfolio-damaging or stop-loss adjacent. Important but not FLASH-tier |

**Outcome:** SURVIVED intake. Proceed to classify.

### PHASE 2: Classify

**Precedence:** IMMEDIATE
- Threshold breach (UMich record low)
- Confirmed catalyst (scheduled CPI release)
- Multiple thesis components affected
- Action window: now

**Confidence:** `confidence: 0.97` / `confidence_language: confirmed`
- BLS official release for CPI (golden source) → 0.95+ baseline
- University of Michigan official Surveys of Consumers for sentiment (second golden source) → +0.05 corroboration adjustment
- Two-source rule satisfied via two independent authoritative releases corroborating the stagflation reading
- Lands at 0.97 → snaps to "confirmed" tier per SIGNAL_FORMAT_SPEC mapping (0.90–1.0 range)
- The 0.03 short of 1.0 captures the UMich pre-ceasefire interview caveat

**Conflict zone:** 🟡 Yellow → 🔴 Red mixed
- 🟢 Confirms CARL's consumption stress quarter framework
- 🟢 Confirms HENRY's Fed-cuts-pushed-to-H2-2027 thesis
- 🔴 Strengthens RED's Stagflation Spiral hypothesis (currently 41% — likely needs upward revision)
- 🟡 Tension: ceasefire announcement post-survey may cause partial recovery in next print
- Net: 🔴 because the dominant story is stagflation lock-in, with the ceasefire caveat as secondary

**Superevent check:** YES — bundle.
- CPI and UMich are TWO independent inputs pointing at ONE underlying cause (stagflation pressures + Fed paralysis)
- Both released same day, same window
- Routing them as separate signals would fragment the story
- Decision: ONE signal as superevent, citing both data sources in body

### PHASE 3: Output

**Disposition:** PUSHED
- Precedence is IMMEDIATE → push to recipient inboxes + Telegram ping to Will

**Routing decision:**
- **Action recipient:** CARL (consumer/consumption stress is the first-order domain — UMich at record low + headline CPI hot is squarely his lane)
- **Info recipients:** HENRY (Fed reaction function), RED (stagflation hypothesis re-weight), LIQUID (HY OAS implications), SAM (USD/JPY via Fed locked)
- **Group:** THESIS_CORE (CARL is a member; HENRY/RED/LIQUID/SAM listed individually as info — this is normal when info recipients span multiple groups)

**Signal file:** SIG-W-20260410-001-cpi-umich-stagflation.md (drafted, currently in WALTER/outbox/ awaiting approval)

**Push notification format** (when dispatched):
```
Signal: SIG-W-20260410-001
Precedence: IMMEDIATE
Pre-arrival context: Stagflation signature locked in.
  CPI Mar headline +0.86% MoM (gas/food pass-through), core contained +0.21%.
  UMich Apr prelim 47.6 RECORD LOW. 1Y inflation exp jumped to 4.8%, long-run
  expectations un-anchoring at 3.4% (Fed red line).
  Caveat: 98% of UMich interviews preceded ceasefire — final print may show partial recovery.
  CARL: update consumption stress framework. Others: see relevance section.
Full signal: AGENTS/WALTER/signals/SIG-W-20260410-001-cpi-umich-stagflation.md
```

### Quality Checks (ADViCE)

- ☑ **Conclusion-oriented:** First sentence states the conclusion ("stagflation signature locked")
- ☑ **Differentiated:** Calls out what's NEW (UMich record low, expectations jumping) — not just what persists
- ☑ **Validated:** Sources cited (BLS, U Michigan SCA, Axios, Spectrum), confidence language used (Confirmed)
- ☑ **Easy to consume:** All numbers in table form with context (current vs prior, YoY comparison, threshold reference)

### Editorial Discipline

- ☑ Doesn't prescribe the fix — describes the data and lets agents decide
- ☑ Every number has context (vs prior month, vs year ago, vs threshold)
- ☑ Surprise check: would this surprise an agent who already knows current network status? YES — UMich record low + un-anchoring expectations are NEW data
- ☑ Will be immutable once dispatched

### Anti-patterns I Avoided

- Did NOT route as two separate signals (CPI vs UMich) — caught by superevent check
- Did NOT draft a 500-word essay — kept Signal+Data ≤200 words per spec
- Did NOT skip the safety net check — flagged convergence (2+ agents on stagflation theme already)
- Did NOT default to "everyone gets a copy" — selected recipients based on first-order domain impact

### Initial Mistake (Recovered)

I initially drafted a SECOND signal (SIG-W-20260410-002, CPI-only with HENRY action) thinking the spec required separate signals per data release. Will challenged the benefit. On re-read of SIGNAL_FORMAT_SPEC, I realized "one file per action recipient" means **one file per inbox during dispatch**, not "one signal per data release." The correct model is ONE master signal that becomes multiple files (one per recipient inbox) at dispatch time. SIG-002 was duplication and is being deleted.

**Lesson:** When two data points land same day on same theme → bundle as superevent. When the ROUTING produces multiple recipients → that's the dispatch step creating multiple files, not the drafting step creating multiple signals.

### Gaps This Example Exposed

1. **~~Header confidence field divergence~~** ✅ RESOLVED in v0.3. SIGNAL_FORMAT_SPEC.md now defines TWO bound fields: `confidence` (numerical 0.0–1.0) AND `confidence_language` (confirmed/reports/assessed/unconfirmed). The two are bound by the mapping table — they cannot disagree. CHECKLIST and FORMAT_SPEC now use the same model.

2. **No routing log:** I have no place to record this routing decision for later review. Need a `WALTER/log/routing_log.tsv` to capture: timestamp, signal_id, gates passed, recipients, push/pull, why. (Open — next round candidate.)

3. **No capability/load check:** I picked CARL as action recipient without verifying his current load. CARL was updated today (not stale), but if he had been overloaded I should have considered re-routing or downgrading. Need a load check sub-step before final routing. (Open — next round candidate.)

4. **No backup recipient defined:** If CARL were unavailable, the spec doesn't say where the signal goes. Need backup mappings in ROUTING_TABLE.md. (Open — next round candidate.)

5. **Header schema divergence between FORMAT_SPEC and CHECKLIST:** Beyond confidence, the two specs still describe slightly different headers (CHECKLIST mentions `domain` and `conflict_zone` fields that aren't in FORMAT_SPEC; FORMAT_SPEC has `timestamp`, `source`, `origin`, `group`, `signal_type`, `resources`, `safety_net`, `word_count` not in the CHECKLIST example). FORMAT_SPEC is canonical but CHECKLIST should reference it explicitly. (Open — next round candidate.)

6. **Filter model divergence:** FILTER_SPEC Gate 1 has Novelty/Relevance/Credibility. CHECKLIST Phase 1 has Already Known/In Thesis Chain/System-Critical. These overlap but use different categories. Need reconciliation. (Open — next round candidate.)

---

*Operational checklist — derived from 10 research prompts | v0.1: April 7, 2026 | v0.2: April 10, 2026 (worked example added) | v0.3: April 10, 2026 (confidence model reconciled with FORMAT_SPEC)*
