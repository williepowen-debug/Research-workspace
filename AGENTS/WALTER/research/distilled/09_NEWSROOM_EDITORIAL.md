# Prompt 9 Distilled: Newsroom Editorial Judgment — What We Keep

**Source discipline:** Wire services (AP, Reuters), newspaper editorial workflow, journalism studies (Galtung-Ruge news values, gatekeeping research)
**Core question answered:** How do editors make triage decisions under time pressure — what to lead with, what to bury, what to kill — and what breaks when they get it wrong?

---

## The Big Idea: WALTER Is an Editor, Not a Wire

AP puts everything on the wire. The editor decides what makes the front page. The 1950 "Mr. Gates" study found a wire editor rejected **90% of incoming copy**. That's not a failure rate — that's the natural operating point of a well-functioning filter.

If WALTER is routing more than 10-20% of incoming information onto the COP, the filter is too loose. The COP is the front page. Most signals belong on inside pages (archive) or in the trash (kill log).

---

## Five Patterns to Implement

### 1. The Breaking News Sequence (Progressive Disclosure)

AP and Reuters don't publish one thing — they publish a **sequence** of increasing depth:

| Stage | AP Term | Timing | Content | Our Equivalent |
|-------|---------|--------|---------|---------------|
| 1 | Flash/Alert | Seconds | One sentence, headline-length | Telegram ping to Will |
| 2 | Bulletin | Minutes | 1-2 paragraphs, usable immediately | COP IMMEDIATE entry |
| 3 | Urgent/Update | 20-30 min | 6-20 paragraphs, reaction + analysis | Signal file in archive |
| 4 | Writethru | Ongoing | Complete narrative, replaces all prior versions | Full signal with sources |

**Key insight:** The Writethru REPLACES all previous versions. It doesn't append — it supersedes. This is exactly how COP.md works: each update overwrites, giving the current picture, not a history.

**The Flash is extremely rare.** AP averages 1-2 per year. A veteran wire journalist wrote exactly ONE Flash in 50 years. If WALTER is firing FLASH signals weekly, the threshold is wrong.

### 2. The News Budget = The COP

AP's daily "digest" is a comprehensive inventory of available stories — the full list. Twice daily, AP also transmits a **Page One Advisory** — a curated subset recommending what deserves prominent display.

Two layers:
- **Digest** = our signals/ archive (everything that exists)
- **Page One Advisory** = COP.md (what matters right now)

This two-layer system — comprehensive inventory + curated recommendation — is exactly what we built. The research confirms the architecture.

**Budget meetings** are 20-minute standing meetings (literally standing, to keep them short) focused on exactly two questions: (1) what gets prominent display, and (2) how long should each item be. WALTER's COP update process should be equally disciplined: what goes on the COP, and how much space does it get.

### 3. Additive News Value Scoring

Galtung and Ruge's 1965 taxonomy identified factors that make a story newsworthy. The key property: **additivity** — the more factors a story satisfies, the higher its probability of selection.

Factors most relevant to WALTER:

| News Value | Our Translation | Example |
|-----------|----------------|---------|
| **Threshold/Magnitude** | How many agents/positions does this affect? | HY OAS crossing 320 affects LIQUID + REGINALD + BROCK |
| **Unexpectedness** | Does this contradict existing data? | NFP beating when JOLTS is inverted |
| **Continuity** | Is this part of an ongoing tracked thread? | Another data point in the CRE maturity wall |
| **Consonance** | Does this confirm what we expected? | Gas hitting $4 after CARL predicted the breakpoint |
| **Composition** | Does the COP need balance? | All bear signals — should counter-signals be more prominent? |
| **Negativity** | Bad news is more actionable than good | Gating events, threshold breaches, downgrades |

**The composition principle is underappreciated:** Editors choose stories partly to balance the overall page. If the COP is wall-to-wall bear signals, WALTER should make counter-signals MORE visible, not less. This is why the Counter-Signals section exists — it's compositional balance, not weakness.

### 4. Graduated Confidence Language

Journalists don't just say "true" or "false." They use a specific vocabulary:

| Confidence Level | Journalistic Language | WALTER Equivalent |
|-----------------|----------------------|-------------------|
| Highest | "Confirmed" | Multiple agents verified, data released |
| High | "Sources tell us" | Single credible source with direct knowledge |
| Medium | "We're getting reports" | Multiple signals match but understanding preliminary |
| Low | "It appears" | Observable evidence, not yet confirmed |
| Lowest | "Unconfirmed reports suggest" | Single signal, no corroboration |

**This is better than our 0.0-1.0 confidence score.** Real language conveys more than a number. COP entries should use this vocabulary:
- "BANKING 🔴🔴🔴 — BCRED gate exceeded [CONFIRMED — Blackstone filing]"
- "PRIVATE CREDIT 🔴🔴 — Stage 3 gating spreading [reports from multiple funds]"
- "LABOR — UI exhaustion accelerating [WALTER estimate, unconfirmed]"

### 5. The Two-Source Rule

Major claims require two independent sources before publication. Exception: a "golden source" — someone in a position of direct knowledge — can stand alone.

**Our translation:** Before WALTER promotes a signal to IMMEDIATE or puts it on the COP as a convergence event, it should be corroborated:
- Two agents seeing the same pattern independently = strong
- One agent's analysis confirmed by released data = strong
- Single agent's inference with no corroboration = note as "assessed" or "estimated"

This isn't bureaucracy — it's the same reason LIGO runs four independent detection pipelines. Redundancy catches false positives.

---

## The Story Fatigue Problem

Two-thirds of Americans report feeling "worn out" by news volume. Global interest in news dropped from 71% to 56% between 2015-2024.

**Our risk:** When the same thesis has been running for weeks (CRE stress, regional bank convergence), agents stop paying attention to COP entries about it. "Yeah, REGINALD is still at red, we know."

**The fix — second-day lede technique:** Don't repeat the status. Find the NEW angle:
- BAD: "BANKING 🔴🔴🔴 — 8-channel convergence continues."
- GOOD: "BANKING 🔴🔴🔴 — Leveraged loan market collapse (-34% YoY) is NEW this week. Confirms funding channel stress that wasn't present in March."

Lead with what CHANGED, not what persists. The delta markers (△) on the COP serve this purpose, but the text itself should also lead with the new information.

---

## Failure Modes That Will Bite Us

### 1. Authority Bias
The NYT held the NSA wiretapping story for 13 months because the White House said it would damage national security. NBC killed Farrow's Weinstein story because senior leadership yielded to pressure.

**Our risk:** WALTER defers to an agent's assessment because the agent is "senior" or established, even when the signal contradicts it. If CARL says consumer stress is moderate but data shows CC DQ at 92% of GFC, WALTER should flag the gap, not defer.

**Fix:** Precedence belongs to the information, not the sender (Military Messaging principle). Data beats agent opinion on the COP.

### 2. Confirmation Bias
The Iraq WMD coverage placed front-page stories presenting unverified claims because they fit the expected narrative.

**Our risk:** WALTER over-promotes signals that confirm the bear thesis and under-promotes counter-signals. The COP becomes an echo chamber.

**Fix:** The Counter-Signals section is mandatory, not optional. RED always gets a line. The composition principle says: if the COP is all bear, make the bull case MORE visible.

### 3. Narrative Gravity
Once a story fits a pre-existing frame, contradicting evidence is systematically downweighted.

**Our risk:** Once the "convergence is happening" narrative takes hold, signals that suggest it ISN'T happening (HY OAS tightening, NFP holding) get buried.

**Fix:** Internal dissent was present in virtually every major editorial failure but was overruled by seniors. RED exists specifically for this. RED's line on the COP is the structural safeguard against narrative gravity.

### 4. Decision Fatigue
Editors make up to 35,000 decisions per day. Late-day decisions are systematically worse — favoring default options and familiar patterns.

**Our risk:** WALTER making COP curation decisions at the end of a long session, after processing many signals, may default to "everything is the same as last time."

**Fix:** COP update should happen FIRST in a session, not last. Read STATUS files → update COP → then do other work. The COP curation requires the freshest judgment.

---

## What We Don't Need From Newsroom Research

- Journalism ethics debates (objectivity, false balance) — not building a news organization
- Teletype bell codes and physical wire infrastructure — historical interest only
- Headline point sizes and column count constraints — we have markdown, not print
- FCC regulations on media ownership — irrelevant
- Social media shareability metrics — no audience engagement to optimize
- Advertiser pressure dynamics — no commercial pressures
- Defamation law and source protection — no legal exposure
- Paywall and subscription strategy — not monetizing
- Detailed NIEM/CMS/editorial calendar software features — we use flat files

---

*Distilled from PROMPT9_NEWSROOM_EDITORIAL_MASTER.md + PROMPT9B_NEWSROOM_EDITORIAL_SUPPLEMENT.md | April 7, 2026*
