# ZHAO RECON DRY RUN EVALUATION
**Written:** 2026-03-15 (dry run, pre-deployment)
**Purpose:** Evaluate Stage 1 RECON prompt before live deployment

---

## 1. Does the prompt make sense?

Yes — the task is clear. Read three files, identify what's stale/unknown, produce structured search targets for Stage 2. The two-stage architecture (recon → live search) is logical and matches how this domain actually works: KB/STATUS contains hard data with known staleness, so the first step is always gap-mapping.

One minor confusion: the prompt header says "Today is March 15" and "TIC January 2026 data released today (March 15)" — but STATUS.md (last updated Mar 12) explicitly corrects this: *"TIC date correction: Mar 18 = Jan 2026 flows."* So the context block contains a factual error vs. what's in my STATUS file. In a live run, this creates a conflict: do I trust the injected context or my STATUS? Recommend clarifying the authority hierarchy (injected context > STATUS? or vice versa?). This matters because the Belgium $500B trigger is the single most important near-term data point for this domain.

---

## 2. File Coverage

**STATUS.md + KB.tsv + TRADE.md = correct and sufficient** for the core recon task.

- **STATUS.md** is the right primary file — it has the current signal dashboard, convergence matrix, open predictions (ZHA-01 through ZHA-08), calendar, and exit rules. High signal-to-noise for identifying what's stale and what catalysts are coming.
- **KB.tsv** provides the underlying evidence layer — useful for checking Conf/Epistemic flags and Stale_By dates. The `Stale_By` column is particularly valuable and makes structured staleness detection easy.
- **TRADE.md** is useful because it ties domain signals directly to trade implications. Good for prioritizing search targets by "does this move our positions?"

**What's missing (minor):**
- `sources/RP-ZHAO-2_LGFV_BANKING_TRANSMISSION.md` — referenced in STATUS but not included. For the LGFV/banking slow-burn vector, the latest NPL data and PBOC injection timeline live here. Not critical for recon, but a live agent might want it for context on Situation 2.
- `sources/LNG_CRISIS_CHINA_ANALYSIS_MAR2.md` — referenced but excluded. Fine for recon purposes.
- No `FLOW.md` or equivalent. FLOW-ZHAO-12 (Gulf recycling active) is referenced but the flows log isn't readable. For this domain, knowing *which* flows have fired recently matters. Consider including or at minimum referencing the flow log date.

**Nothing included that's not useful** — all three files pull weight.

---

## 3. Context Gaps

The context block is mostly good. Issues:

**TIC Date Discrepancy (HIGH PRIORITY):** Context says TIC releases today (Mar 15). My STATUS.md says Mar 18 (explicitly corrected from Mar 15). This will cause the live agent to write a RECON_REPORT with the wrong date for one of the most important near-term catalysts. Fix this before live run — confirm whether TIC Jan 2026 is Mar 15 or Mar 18. (My STATUS noted the correction on Mar 12; if it's been re-corrected back to Mar 15, that needs to be reflected in STATUS too.)

**FOMC timing:** "FOMC Monday-Tuesday, presser Wednesday 2:30 PM ET" — useful, but doesn't tell me what the market is pricing. For my domain (UST demand), the Fed's stance on how it plans to handle demand shocks is material. Knowing if there's been any Fed commentary on foreign demand, UST market functioning, or emergency facilities would help. Not critical, but "Fed funds futures as of Friday close" would be a useful addition.

**BOJ context:** "BOJ Thursday" — helpful. But did BOJ hold or hike at Mar 13-14? My STATUS says BOJ was Mar 13-14, and I was monitoring it. The context implies it hasn't happened yet (presser Mar 19 listed as future), but my STATUS was written Mar 12 pre-BOJ. Was the BOJ decision already made? If so, what happened? This is a meaningful gap — Japan is my largest anchor ($20-30B/mo) and BOJ's rate decision directly affects it.

**Missing: DXY/10Y as of Friday close.** I have Brent ($101.07) but not DXY or 10Y yield. These are my two most watched variables for USD/CNY defense timing (ZHA-01) and the TLT puts thesis. Easy addition, high value.

**Missing: Korea situation.** USD/KRW at Friday close? KOSPI current level? These are active signals (BoK selling is live). Not knowing if Korea stabilized or worsened in the 3 days since my last update creates unnecessary blind spots.

---

## 4. Output Format

The requested structure (Stale Data → Known Unknowns → Search Targets → Cross-Agent Needs) is well-matched to how this domain's data actually works. No friction.

One suggestion: in Section 3 (Search Targets), the "Last Known" field should specify whether the value is from STATUS vs. KB.tsv vs. TRADE.md. When values conflict across files (see: TIC date discrepancy), provenance matters. Could add a **Source File:** field to each target, or at minimum a note to flag cross-file conflicts.

The Priority tiers (🔴/🟠/🟡) work well. The FOMC/BOJ framing for 🔴 is appropriate given this week's calendar.

---

## 5. Scope Concerns

**8-20 targets: roughly correct, but the lower bound is tight for this domain.**

This domain has at least 6 active signal streams that each warrant 2-3 distinct search targets:
1. Belgium TIC Jan 2026 data (the single most important print)
2. China official holdings (TIC Jan)
3. Japan/BOJ situation post-Mar 13-14 meeting
4. Gulf escalation: financial infrastructure, oil price, Hormuz traffic
5. Korea: USD/KRW, BoK selling status, KOSPI
6. PBOC/CNY: any new guidance since Feb 9 directive

That's easily 12-15 well-scoped queries without padding. 8 would feel cramped and force priority choices that may exclude material signals. 20 is the right ceiling — beyond that, Stage 2 starts to drift toward general news rather than surgical data retrieval.

**Recommendation:** Set floor at 10, keep ceiling at 20. The TIC data alone justifies 3-4 queries (Belgium, China official, Japan, any notable change in aggregate foreign holdings).

---

## 6. Questions for Prome

1. **TIC date — which is right?** My STATUS says Mar 18 (explicitly corrected). The prompt says Mar 15. One of them is wrong. This is the single most important upcoming data point for my domain (Belgium $500B trigger). Please confirm before live run.

2. **BOJ Mar 13-14 — what happened?** By March 15, the BOJ meeting is over. Did they hold/hike/cut? Was there emergency action? If the context window is "after BOJ," Japan anchor status may have changed materially. The live agent should have this answer injected rather than needing to search for it.

3. **Authority hierarchy for conflicts:** If injected context contradicts my STATUS.md, which wins? Assume injected context is more current (Prome's latest info), or assume STATUS is more carefully maintained? Suggest adding a note: *"If this context conflicts with STATUS.md, injected context takes precedence unless explicitly flagged."*

4. **Cross-agent context:** The prompt doesn't tell me what other agents are seeing. For my CROSS-AGENT NEEDS section, it would help to know roughly what SAM (Japan) already has on BOJ, and what LIQUID has on auction data. Would prevent me from listing searches that SAM is already covering. Even a one-line summary of each adjacent agent's last update date would help — or confirmation that cross-agent deduplication happens after all Stage 1 reports are in.

5. **Gulf financial infra (Vector 11):** My STATUS upgraded this to 5/5 on Mar 12 (Citi DIFC evacuation). Is there a separate "GULF" or "HAWK" agent covering operational Gulf events, or does ZHAO own this? If HAWK owns Hormuz/Gulf operations and ZHAO only owns the UST recycling impact, the search targets should be scoped accordingly. Currently I'd write 3-4 Gulf queries — is that in or out of scope for this agent's Stage 2 run?

---

## Summary Verdict

**Prompt is deployable with two fixes:**
1. Resolve the TIC date (Mar 15 vs Mar 18) — this is a blocking issue, not cosmetic
2. Add DXY/10Y Friday close and USD/KRW/KOSPI Friday close to the context block — 2 lines, high value

Everything else is a nice-to-have. The three-file structure, output format, and priority framework are all well-designed. The 8-20 target range is acceptable (10-20 would be tighter). The FOMC/BOJ week framing correctly identifies what this week's 🔴 priority should be.
