# WALTER Signal Processing Checklist
**Version:** 0.9 | **Date:** May 5, 2026 (Cluster assignment step added to Phase 2 per CLUSTER_TAXONOMY.md v0.1 — every dispatched signal lands in exactly one primary cluster) | **v0.8:** April 20, 2026 (Filter v2 Segment C — Phase 1 step 2.5 verify-research trigger check added) | **v0.7:** April 20, 2026 (Filter v2 Segment B — Phase 1b same-theme combine step added) | **v0.6:** April 11, 2026 PM (canonical Domain Vocabulary referenced — Gap C resolved) | **v0.5:** April 11, 2026 PM (Phase 1 reconciled with FILTER_SPEC v0.2 unified filter model) | **v0.4:** April 11, 2026 (header schema reconciled, conflict_zone clarified) | **v0.3:** April 10, 2026 (confidence model reconciled) | **v0.2:** April 10, 2026 (worked example added) | **v0.1:** April 7, 2026

One-page operational reference for processing incoming signals. Derived from 10 research prompts across emergency medicine, military communications, ATC, pub/sub systems, intelligence dissemination, emergency dispatch, scientific alerts, open output systems, newsroom editorial, and trading desk operations.

> **Canonical source cross-references:**
> - `SIGNAL_FORMAT_SPEC.md` owns the signal file format, header fields, **and the Domain Vocabulary** (13 canonical codes: LABOR, MACRO_INFLATION, TARIFF_TRADE, CONSUMER_CREDIT, BANK_CRE, FUNDING_LIQUIDITY, PRIVATE_CREDIT, INSURANCE_SHADOW, OIL_ENERGY, GEOPOL_ENERGY, GEOPOL_NON_ENERGY, JAPAN_BOJ, MARKET_VOL).
> - `FILTER_SPEC.md` owns Gate 1 filter logic (System-Critical bypass → Novelty → Relevance → Credibility).
> - `ROUTING_TABLE.md` owns domain → recipient routing rules, using the canonical Domain Vocabulary codes in every row.
>
> This CHECKLIST is the operational *process* — it describes how to execute those specs, not what they define. On any divergence, the owning spec wins and this CHECKLIST is updated to match.

---

## PHASE 1: INTAKE (Kill or Keep — under 10 seconds)

Per FILTER_SPEC v0.2 unified filter model. Pre-gate bypass first, then two hard kill gates, then soft credibility check.

```
0. SYSTEM-CRITICAL BYPASS  → If held position hit, safety net trigger,
                             falsification rule pierced, or Will FLASH:
                             SKIP all gates, route FLASH immediately.

1. NOVELTY (HARD KILL)     → Already in any agent's STATUS or routed <48h?
                             Yes: KILL, log to kill_log.tsv ("already known").

2. RELEVANCE (HARD KILL)   → Touches held position / active thesis /
                             watched metric / transmission chain / catalyst?
                             No: KILL, log to kill_log.tsv ("not thesis-relevant").

2.5 FRAMING AUDIT (SOFT)   → Any of the 4 verify-research trigger patterns
                             present (see Phase 1.5 below)? If yes, spawn
                             verify-research sub-agent before Gate 3.
                             Verdict adjusts Gate 3 inputs — confirms,
                             corrects framing, kills as false, or flags
                             indeterminate (lowers confidence).

3. CREDIBILITY (SOFT)      → Sets confidence tier (0.30-1.0 based on source
                             quality + specificity). Not a hard kill UNLESS
                             final confidence after adjustments < 0.30 floor.
                             Low-credibility-but-novel-and-relevant signals
                             pass to Phase 2 flagged, don't die outright.
```

Most signals die at Novelty or Relevance. That's correct. Target: 80-90% filtered.

**Key change from v0.1/v0.2/v0.3 of this file:** Novelty and Relevance are AND-gates (must pass BOTH), not pass-any-of-three. Credibility is a confidence modifier, not a hard gate. System-Critical is a pre-gate bypass that precedes all filtering. See FILTER_SPEC.md for full rationale.

---

## PHASE 1.5: VERIFY-RESEARCH TRIGGER (Framing Audit)

Runs between Gate 2 pass and Gate 3. Purpose: catch framing errors in shaky source language before credibility is scored. This month (Apr 2026) caught 4 framing issues that would have routed with bad framing otherwise — BOJ ¥330B misframing, WhaleInsider Hormuz "zero tankers / first in history", Blue Owl "co-founders / alt-collateral" overstatement, SIG-029 "first NATO state-response" inaccuracy.

**Trigger patterns** — any ONE fires a verify-research spawn:

| # | Pattern | Examples | NOT triggered by |
|---|---------|----------|------------------|
| (a) | Secondhand citing primary | Aggregator or X-repost of a primary source you haven't read yourself (WSJ-via-X-aggregator, Bloomberg-via-retweet, FT-summarized-by-newsletter) | Reading the primary directly |
| (b) | Summarizing plurals | "co-founders", "all three", "both", "every", "each of the", "the trio" | Named specifics ("Owl Rock's Doug Ostrover and Marc Lipschultz") |
| (c) | Mechanism-assertions not yet in primary coverage | "replaced with", "swapped for", "backed by", "triggered by", "in exchange for" — when the underlying filing/source doesn't yet carry that language | Mechanism claims that quote the primary source directly |
| (d) | Extreme-absolute extraordinary claims | "zero", "first in history", "largest ever", "never before", "unprecedented" | Falsifiable comparatives like "record high" / "biggest since 2021" / "5th largest" (these self-bound and are routinely checkable) |

**Spawn discipline** (per auto-memory Sub-agent Prompt Discipline):
- Lead the prompt with the routing decision that depends on the answer ("WALTER is about to route this to CARL as IMMEDIATE; need to know if the framing holds").
- Set a hard total word cap on the sub-agent's response (e.g., 200 words).
- Require a single-line VERDICT at the top of the response — everything else is optional.
- Ask for decision-usefulness, not comprehensiveness. Don't template — write the prompt each time.

**Verdict handling:**
| Verdict | What it means | WALTER action |
|---------|---------------|---------------|
| **CONFIRMED** | Framing holds; primary source supports the claim as written | Proceed to Gate 3 as normal. Cite verification in signal body. |
| **CORRECTED-framing** | Primary source exists but the summary overstated or misframed | Rewrite signal body with corrected framing before Gate 3. Lower confidence by one band. |
| **FALSE** | Primary source contradicts the claim, or no primary source exists to support it | KILL. Log to kill_log.tsv with reason "framing-false, verify-research verdict". |
| **INDETERMINATE** | Primary exists but is ambiguous, or verification inconclusive within time budget | Route with lowered confidence (move to `unconfirmed` tier) and add note to signal body flagging the unverified framing. |

**Discretion:** If you already have the primary source open in the current session and the claim matches, no spawn required — note the inline-verification in the signal body and proceed. The trigger applies when you are relying on the secondhand framing.

---

## PHASE 1b: SAME-THEME COMBINE CHECK (Before Phase 2)

Once 2+ items have survived Phase 1 filters (in the current drafting session — items not yet dispatched to route_log.tsv), ask: **do any of them point at the same underlying event or specific sub-theme within the same canonical domain?**

```
For each pair of surviving items (i, j):
  Same canonical domain (per FORMAT_SPEC Domain Vocabulary)?   [hard requirement]
  AND same underlying event OR same specific sub-theme?        [soft test — domain alone is too broad]
  AND each origin adds independent value (not identical dup)?  [identical dup → kill the extra, don't combine]
  → YES to all three: COMBINE into one signal with multi-origin header
                      (origin becomes array per FORMAT_SPEC Multi-Origin Signals)
  → NO: process each item independently
```

**Pre-dispatch only.** While drafting, items from any arrival path — same Telegram batch, different batch, separate Will message, WALTER-found article — may fold in. Once a signal has been appended to route_log.tsv, it is immutable; later items become dup-kill or follow-up signals that cite the prior SIG-ID. No retroactive merging.

**Common cases the check catches:**
- Paired-chart posts by the same author (Bilello VIX + SPX 3-wk extremity — MARKET_VOL, extremity-counter)
- Cross-source same-event (disclosetv carrier build-up + BRICSinfo talks rejected — GEOPOL_ENERGY, Iran-escalation)
- Visual + analytical versions of the same physical event (Flightradar24 Doha overflight + Celestyal cruise Hormuz transit — GEOPOL_ENERGY, Hormuz operational state)
- Bundled macro prints on the same sub-theme (CPI + UMich prelim — MACRO_INFLATION, stagflation-pressure)

**What the check does NOT catch:**
- Different domains, same broad narrative ("recession fears" spanning LABOR + CONSUMER_CREDIT + BANK_CRE) — route separately; NEXUS owns cross-domain synthesis.
- Different events in same domain (Hormuz shipping + Iran nuclear talks, both GEOPOL_ENERGY but different events) — route separately.
- Second source arriving post-dispatch — dup-kill or follow-up, never retroactive merge.

See FORMAT_SPEC v0.6 Multi-Origin Signals section for full combine rule, origin array syntax, body conventions, and historical examples.

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

**Conflict zone** — relationship to thesis (analytical step, NOT a header field):
- 🟢 Confirms thesis (gas hits $4 as CARL predicted)
- 🟡 Tension — doesn't break thesis but doesn't confirm (HY OAS tightening)
- 🔴 Contradicts thesis or threatens position (major counter-signal)

> **Why this is not a header field:** A signal's conflict_zone is recipient-dependent — the same signal can be 🟢 for CARL (confirms consumer stress) and 🔴 for HENRY (contradicts Fed-trap resolution). Baking one conflict_zone label into the header would collapse that nuance. Instead: use this step to sharpen the **Relevance** body section so each recipient sees the signal through their own thesis lens. If you need a header-level marker for machine filtering, use `signal_type` (which IS in FORMAT_SPEC) — e.g. `counter-evidence` vs `thesis-confirmation`.

**Cluster assignment** (added v0.9, 2026-05-05): Every dispatched signal lands in exactly one primary cluster per `design/CLUSTER_TAXONOMY.md`. Decide before writing the signal file:

```
1. Which cluster does this fit? Pick from the 10 buckets in CLUSTER_TAXONOMY.md.
2. Does it fit two? Apply edge-case rules (substance > mechanism > action-recipient).
3. Doesn't fit any? → MISC. New cluster only with explicit Will sign-off (≥3 signals on a coherent new theme + expected forward-momentum).
```

The cluster is written to the signal YAML header (`cluster: <NAME>`) AND determines which section of `/BOARD/INDEX.md` the dispatch row lands in. CLUSTER_TAXONOMY.md is canonical-source for the bucket names — don't invent.

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
# Full schema per SIGNAL_FORMAT_SPEC.md. All fields required unless marked optional.
---
signal_id: SIG-W-YYYYMMDD-NNN
precedence: FLASH | IMMEDIATE | PRIORITY | ROUTINE
timestamp: 2026-MM-DDTHH:MM:SSZ
source: WALTER
origin: "Free text — where raw info came from (e.g. BLS, Reuters, agent inbox)"

to: AGENT (ACTION)
info: AGENT, AGENT                    # optional
group: AIG_NAME                       # optional; see FORMAT_SPEC AIGs

signal_type: threshold-crossed | pattern-match | catalyst | divergence | research | position-risk | context | manual-flag
confidence: 0.0–1.0                   # numerical score, bound to language tier
confidence_language: confirmed | reports | assessed | unconfirmed
resources: 0 | 1 | 2                  # processing resource estimate
safety_net: clear | triggered         # override fired?

word_count: NNN                       # FLASH/IMMEDIATE must be ≤200
---
```

**Optional/conditional fields** (WALTER adds these at dispatch time, not drafting):
```yaml
dispatched: 2026-MM-DDTHH:MM:SSZ      # added when dispatched to recipient inboxes
dispatch_note: "Free text reason for trim/re-route/downgrade"
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
Full signal: /BOARD/SIG-W-YYYYMMDD-NNN.md
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

Walked per FILTER_SPEC v0.2 unified model (System-Critical bypass → Novelty → Relevance → Credibility).

| Check | Result | Reason |
|-------|--------|--------|
| **0. System-Critical bypass?** | NO | Not portfolio-damaging, no stop-loss adjacent, no safety net trigger, no falsification rule firing. Continue through normal gates. |
| **1. Novelty (hard kill)?** | PASS | Both prints released today, fresh information, not in any agent's STATUS as of this morning. |
| **2. Relevance (hard kill)?** | PASS | Touches LABOR_DOWNSTREAM (CARL), market structure (HENRY), credit (LIQUID), thesis (RED), Japan (SAM via Fed reaction). Multi-domain. |
| **3. Credibility (soft modifier)?** | HIGH → conf 0.95+ base | BLS official release (golden source) + University of Michigan official Surveys of Consumers (second golden source) = TWO independent authoritative sources. Maps to 0.90–1.0 band. |

**Outcome:** SURVIVED intake. Confidence 0.97 (after +0.05 corroboration adjustment, capped at 0.97 to reflect UMich pre-ceasefire interview caveat). Proceed to classify.

**Note on the new model vs the old one:** Under v0.1's "fail-all-three" logic this would have passed trivially (all three questions gated pass). Under v0.2's AND-logic it still passes because Novelty AND Relevance both pass cleanly. The difference would matter on edge cases like a Bloomberg restating of a CPI print we'd already routed (fails Novelty as duplicate → now dies; under v0.1 would have passed on Credibility alone) or an anonymous Twitter post about WAL capital-raise rumors (passes Novelty + Relevance + Low Credibility = routes at ~0.35 confidence instead of dying outright).

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
Full signal: /BOARD/SIG-W-20260410-001-cpi-umich-stagflation.md
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

1. **~~Header confidence field divergence~~** ✅ RESOLVED in v0.3. SIGNAL_FORMAT_SPEC.md defines TWO bound fields: `confidence` (numerical 0.0–1.0) AND `confidence_language` (confirmed/reports/assessed/unconfirmed), bound by a mapping table.

2. **~~No routing log~~** ✅ RESOLVED Apr 11. `AGENTS/WALTER/routed/route_log.tsv` created per FILTER_SPEC schema. Today's dispatches backfilled. Going forward every dispatch appends a row.

3. **No capability/load check:** I picked CARL as action recipient without verifying his current load. CARL was updated today (not stale), but if he had been overloaded I should have considered re-routing or downgrading. **Partially addressed Apr 11** via Backup column in ROUTING_TABLE v0.2 with promotion semantics (use backup when primary stale >5d, in MINIMIZE, or spawning sub-agents). Still open: automated load check at routing time. (Open.)

4. **~~No backup recipient defined~~** ✅ RESOLVED Apr 11. ROUTING_TABLE v0.2 added a Backup column across all rows with explicit promotion semantics. CARL backup is HENRY for most domains.

5. **~~Header schema divergence between FORMAT_SPEC and CHECKLIST~~** ✅ RESOLVED Apr 11 (this file, v0.4). CHECKLIST Phase 3 header example now shows the full FORMAT_SPEC schema. `conflict_zone` clarified as an analytical step (informs Relevance prose) not a header field, because it's recipient-dependent. Header-level machine filter for thesis-vs-counter uses `signal_type` (counter-evidence vs thesis-confirmation) which is already in FORMAT_SPEC. The canonical-source rule is documented at the top of this file.

6. **~~Filter model divergence~~** ✅ RESOLVED Apr 11 (Gap B). FILTER_SPEC v0.2 and this CHECKLIST v0.5 now share a single unified filter model: System-Critical pre-gate bypass → Novelty (hard kill) → Relevance (hard kill) → Credibility (soft, confidence modifier with 0.30 floor). AND-logic on the hard gates. Model is versioned v1 and **provisional** — scheduled review after 10+ signals pass through or 30 days from Apr 11, whichever first.

---

*Operational checklist — derived from 10 research prompts | v0.1: April 7, 2026 | v0.2: April 10, 2026 (worked example added) | v0.3: April 10, 2026 (confidence model reconciled) | v0.4: April 11, 2026 (header schema reconciled; conflict_zone clarified) | v0.5: April 11, 2026 (Phase 1 reconciled with FILTER_SPEC v0.2 unified filter model — Gap B resolved) | v0.6: April 11, 2026 PM (canonical Domain Vocabulary referenced — Gap C resolved) | v0.7: April 20, 2026 (Filter v2 Segment B — Phase 1b same-theme combine check added between intake and classify, references FORMAT_SPEC v0.6 Multi-Origin Signals) | v0.8: April 20, 2026 (Filter v2 Segment C — Phase 1.5 verify-research framing audit codified with 4 trigger patterns, spawn discipline, and 4-verdict handling) | v0.9: May 5, 2026 (Cluster assignment step added to Phase 2 per CLUSTER_TAXONOMY.md v0.1 — every dispatched signal lands in exactly one primary cluster, header gets `cluster:` field, INDEX section is determined by cluster)*
