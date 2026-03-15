# CARL RECON DRY RUN EVALUATION
**Written:** 2026-03-15 (Sunday, War Day 14)
**Purpose:** Evaluate the Stage 1 RECON prompt before live deployment.

---

## 1. Does the prompt make sense?

**Yes — clearly structured and unambiguous.** The task distinction (produce a RECON REPORT identifying what to search for, not a research report) is well-explained. The "do NOT search for Confirmed Data" instruction is helpful and prevents wasted search budget. No confusion about what's being asked.

One minor clarity note: the prompt says "Your last STATUS update was approximately Mar 12" — this is accurate (STATUS.md header says Mar 13, 13:15 UTC), but close enough. No issue.

---

## 2. File coverage

**Core three files are the right set.** Assessment:

| File | Useful? | Notes |
|------|---------|-------|
| `STATUS.md` | ✅ Essential | Contains all active metrics, convergence matrix, danger windows, signal dashboard, cross-agent links. Primary reference for identifying stale data and known unknowns. |
| `workbook/KB.tsv` | ✅ Essential | 91 entries. Timestamps per entry allow precise staleness detection. Pending flags, fraud signals, and structural KB items all here. Critical for identifying gaps that never got followed up. |
| `TRADE.md` | ✅ Useful | Keeps output focused on what moves positions. Good anchor — prevents RECON from drifting into general macro research. |

**What's potentially missing:**
- `workbook/VX.tsv` — vector threshold file. Contains specific trigger values for each metric. Useful for knowing exactly what threshold I'm watching, but STATUS.md largely duplicates this for active vectors. Low-priority omission.
- `workbook/FL.tsv` — forward-looking calendar. Contains upcoming data release dates I'm watching. Could improve SEARCH TARGETS section by revealing scheduled releases I haven't listed. Worth considering for Stage 2 prep, but not essential if STATUS catalysts section is read carefully.
- `workbook/ABS_BASELINE.tsv` — explicitly listed as not yet collected (KB-CARL-002: "Baseline still not collected as of Mar 10"). This is a **known gap** the prompt should surface but won't because the file is empty/sparse. Flagging this explicitly: the ABS baseline sprint was proposed but never executed. This will appear as a Known Unknown when reading KB, which is correct.

**Nothing included that's not useful.**

---

## 3. Context gaps

The context section is **largely sufficient**. A few gaps worth noting:

**What's well-covered:**
- War context (Day 14, Hormuz) — critical for understanding why energy vectors are structural
- Key macro datapoints (PCE, GDP, JOLTS, claims) — prevents me from re-searching already-verified data
- Calendar anchors (FOMC, BOJ, UI cliff Mar 24) — shapes priority scoring correctly
- Financial market levels — prevents stale market data from anchoring my search targets

**What's missing or thin:**
- **No mention of continuing claims result from Mar 13.** STATUS.md flagged this as the single most important data release of the week ("FIRST CLEAN READ post-DHS suppression — could gap through YELLOW 1.9M in single print"). Was it 1,868K confirmed again? Did it gap through? This is the highest-stakes unknown going into FOMC week and it's not in Confirmed Data. I would have to search for it in Stage 2 even though it already happened Thursday. **Recommend adding the Mar 13 claims print to Confirmed Data before live deployment.**
- **No mention of gas price as of Mar 14-15.** AAA daily is publicly available. $3.60/gal was the Mar 13 read per STATUS. With WTI at $101.07 (lower than the $107 that set $3.60), the pump price trajectory has changed. The gas squeeze behavioral breakpoint math ($4/gal timing) will be a key search target and having a current AAA reading would help calibrate.
- **No mention of Goeasy (GSY.TO) post-Mar 10.** US comps (CACC, SYF, OMF, WRLD) showed Feb improvement that the STATUS flagged as potentially survivor-bias-distorted. Cross-referencing these is a TRADE.md-relevant search target.

---

## 4. Output format

**Format is well-designed.** No structural friction. Specific notes:

- **STALE DATA** section is the right starting point — forces me to anchor to what I actually know vs. what I'm assuming.
- **KNOWN UNKNOWNS** is distinct and important. STATUS.md has several unfollowed flags (ABS baseline never collected, SoFi 2025-2 vintage check proposed but not done, Santander trust DQ acceleration monitoring flagged but not executed). These belong in their own section, not lumped with stale data.
- **SEARCH TARGETS** format (Query / Why / Last Known / Priority) is excellent. The "Last Known" field forces me to state what I'm updating FROM, which prevents lazy "check this topic" targets.
- **CROSS-AGENT NEEDS** section is smart — prevents me from generating duplicate search targets that another agent will handle more efficiently. Works especially well for HAWK (energy), LABOR (claims, NFP), and HENRY (wealth effect/SPX) domains.

**One friction point:** The Priority emoji system (🔴/🟠/🟡) is intuitive but the definition "🔴 = FOMC/BOJ week critical" is a bit narrow. Some of my highest-priority consumer credit targets (FL UI cliff Mar 24, Dave 28DPD canary) aren't FOMC/BOJ-related but are extremely time-sensitive. Suggest either broadening the 🔴 definition to "time-sensitive/high market impact" or adding a fourth tier. Not a blocker — I can interpret in spirit.

---

## 5. Scope concerns

**8-20 targets is the right range.** Reasoning:

- My domain has ~8-10 genuinely high-priority search targets for this window (claims, gas price, SoFi ABS vintages, consumer earnings guidance, FL-specific DQ signals, Goeasy US comps, BNPL charge-off data, ABS trustee reports).
- Below 8 would miss meaningful signals. Above 20 would include noise.
- The "not vague topics" constraint does most of the work. If I follow it strictly, 8-20 stays achievable. Risk: with all the active vectors in STATUS, I might over-generate targets. The TRADE.md anchor ("Focus on what moves positions") is the right check.
- One practical note: some of my highest-value targets (ABS trustee reports, SoFi deal docs) require SEC EDGAR access that web search won't easily surface. These are valid search targets but may return low-yield in Stage 2. Worth flagging as "may need manual pull" vs. "web search ready."

---

## 6. Questions for Prome

1. **Was the Mar 13 continuing claims print published?** This is the single most important piece of missing data. If it printed, it should be in Confirmed Data. If it was delayed/unreleased, I need to know that's a search target.

2. **Current AAA gas price as of Mar 14-15?** The $4/gal behavioral breakpoint timing math is central to my positioning thesis. If you have a current print, add it to Confirmed Data and I won't waste a search slot on it.

3. **Did the Dave 28DPD canary (GIG subagent, ~2.0%, stress >2.10%) update since Mar 12?** STATUS.md references GIG as an active subagent but the last read I have is not timestamped clearly. This is a leading indicator for CC stress and I'd want to search for it or have it confirmed stale.

4. **Is the ABS baseline sprint still open?** KB-CARL-002 flagged this as uncollected as of Mar 10. KB-CARL-082/083 escalated it to highest priority. If it's still undone, it should be a Stage 2 search target (Santander/Exeter trustee report DQ data). Confirm scope.

5. **FOMC presser focus area for CARL?** The dots/statement itself is macro (PROME domain), but Powell language around consumer health, credit conditions, or labor market softening is directly in my domain. Should I generate a search target for post-FOMC consumer credit commentary, or is NEXUS handling that synthesis?

---

## Summary Assessment

**Prompt is ready to deploy with one recommended fix:** Add the Mar 13 continuing claims result to Confirmed Data before live run. That's the only gap that would materially degrade output quality. Everything else is minor (FL.tsv/VX.tsv omission, gas price staleness) and would surface naturally as search targets.

The format, scope, file set, and output structure are all well-designed. This will produce a clean, actionable RECON REPORT in Stage 1.

**Confidence in prompt quality: HIGH.**
