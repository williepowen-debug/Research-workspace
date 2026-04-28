# WALTER MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to design docs/CLAUDE.md or delete, never just accumulate.*

*Distinct from STATUS.md (operational state) and LAST_COMPLETION.md (latest session's deliverables). This file holds durable learnings that shape how WALTER works, not what WALTER did.*

---

## Feedback

- [2026-04-07] **Iterative architecture, not upfront design.** Will: "treat this as a living process, iterate as we learn." Apply: ship Layer 1 before designing Layer 2/3 in detail; budget infrastructure proposals against real session cadence.
- [2026-04-10] **One signal, multi-recipient.** Don't split same data into multiple signals because different agents care about different angles. Frame once, route via to/info fields. (FORMAT_SPEC dispatch mechanics ≠ content splitting.)
- [2026-04-14] **Honest read over thesis-defense.** When Will asks "is X positive for our position?" give the real read — mixed/negative if true, with strongest counter-data named. KRE-XLF gap reframed thesis as "may be early not wrong" — the rigorous answer.
- [2026-04-14] **BOARD-only delivery.** Every signal → BOARD archive always. FLASH = BOARD + Telegram-alert-Will only (no inbox push). IMMEDIATE/PRIORITY/ROUTINE = BOARD-only. Will spawns relevant agent if FLASH demands action. Codified as RULE 10 in CLAUDE.md.
- [2026-04-14] **Image-intake batch workflow.** Will sends batches via Telegram → WALTER processes + replies with batch summary (one line per signal: ID → domain → precedence → recipient → kill reason). Auto-spawn verify-research without per-spawn permission. Flag friction in real time, not at closeout.
- [2026-04-14] **Don't kill on lede alone.** Read the full body before classifying. Lede-only kill missed 3 hard data points in Seeking Alpha KRE piece. Distinguish weak author synthesis from named-aggregator stats (Morningstar, Redfin, BLS) — low-credibility authors can still surface real citable stats.
- [2026-04-14] **Domain vocabulary gaps surface from real signals.** When 2+ signals don't fit canonical 13 codes in one session, that's a vocab gap. Resolution: add to FORMAT_SPEC FIRST per canonical-source rule, propagate to ROUTING_TABLE. (Apr 14 ASIA_CONTAGION + UST_FOREIGN.)
- [2026-04-19] **Check target-agent KB before "missed context" findings.** Verify-research often surfaces domain knowledge target agent already holds. Apply: before filing "network is N weeks behind on X," grep target's own files first. WALTER doesn't need to hold BRENT's domain depth.
- [2026-04-20] **Residential-housing → REGINALD, not CARL.** Geo-narrow residential/HOA/builder-defect/insurance-withdrawal signals route REGINALD action + CARL info, not reverse. CARL = macro-national consumer-credit primary; REGINALD = bank/CRE primary with direct earnings-week coverage. Codified as ROUTING_TABLE v0.5 exception.
- [2026-04-20 evening] **Surface friction proactively in spec proposals.** Enumerate ambiguities/edge cases/double-counting risks in same message as draft, not after Will asks. Shortens review loop and catches problems before they're baked in.
- [2026-04-20] **Verify when origin uses summarizing-plurals or mechanism-assertions.** "co-founders" / "all three" / "replaced with" / "swapped for" / "backed by" — these framing slots most often misrepresent primary source. Verify-research cost ~$0.05 vs downstream-overstated-thesis cost: asymmetric. Codified as Phase 1.5 trigger pattern in CHECKLIST v0.8.
- [2026-04-25] **CORRECTED-FRAMING is becoming the dominant verify verdict** (FL Scott "43k" / FHA "180% of 2009" / DB call/put numerics / FHLB EO / Hengli novelty-framing was CONFIRMED but the recurring pattern is direction-confirmed-specifics-imprecise). Calibration: when CORRECTED-FRAMING fires, drop confidence to ~0.55, retain directional thesis, flag specifics as imprecise in dispatch_note. The verify is HIGHEST-VALUE here — separates "real thesis transmission" from "headline cherry-pick."
- [2026-04-26] **Verify-research can have right-history-wrong-tense.** Apr 26 session: verify-research framed BRICS bases-damage signal as "active 2026 Iran war from late February" with valid NBC News primary URL. The history claim was correct (war did happen, Iran did strike 100+ targets across 11 US bases) but the tense was wrong (currently in ceasefire since Apr 8). Cost of accepting framing wholesale: would have dispatched as ACTIVE-WAR signal when current state is post-ceasefire. Discipline: cross-check current-state against MEMORY/STATUS network anchor before accepting verify framing wholesale, especially for state-that-evolves-quickly domains (Iran/Hormuz, FL drought, retail bankruptcy waves, Fed rate path).
- [2026-04-26] **Boot with explicit war-state anchor.** Apr 26: my session-context had partial Iran-war awareness (STATUS line 36 COP-STALE + line 56 BRENT blockade) but no clean "war happened, ceasefire date, current day-count, blockade ongoing" pointer. Result: I framed Iran-cluster signals (Hengli, Pinckney, USAF airlift, M/V Sevan, Mareeyo, Pakistan diplomacy) as buildup/posture/cluster when correct frame is post-Apr-8-ceasefire dynamics under active US blockade. STATUS NETWORK AWARENESS now has explicit IRAN-WAR ANCHOR callout at top — read at boot, refresh weekly minimum or on visible state-change events.
- [2026-04-28] **Verify-research can surface a DIFFERENT-CATEGORY catalyst than the headline implies.** Apr 28 Phoenix BTR signal: headline framed as credit-cycle ("capital dries up, layoffs"), verify-research surfaced **regulatory** catalyst (21st Century ROAD to Housing Act Senate 89-10 Mar 10-12 forcing 7-yr forced disposal of institutional 350+ SF home portfolios → BTR institutional buyer pool collapse → new-start financing freeze). This is HIGHER-VALUE than CORRECTED-FRAMING-on-magnitude — the catalyst CATEGORY moved (financial → regulatory/legislative). Apply: when verify-research pulls a different-category catalyst, that's load-bearing for routing — adds POLITICAL/LEGISLATIVE vector to a cluster that was previously credit-only, opens BARON political-network-mapping pickup, changes the timing-pivot (House reconciliation date vs credit-cycle peak). Codify in dispatch_note explicitly: "catalyst category corrected from X to Y."

## Findings

- [2026-04-11] **Trust disk over memory.** `/COP.md` existed since Apr 7 while NEXT_SESSION claimed otherwise. `ls` the file before believing handoff doc.
- [2026-04-11] **Stale-agent flagging is highest-leverage boot output.** Agents with Status/Updated/Focus columns >5 days old should be surfaced explicitly in STATUS, not buried.
- [2026-04-11] **`git pull --rebase --autostash`** for dirty-tree cases. Captures tracked changes only; leaves untracked files (other agents' new work) untouched.
- [2026-04-15] **Iran state can stale within 24h.** Spot-check Iran/Hormuz state before anchoring downstream signal framing.
- [2026-04-15] **Regional outperformance is mechanical, not thesis-killing.** XLF underperformance is V/MA/GS/MS/BX/KKR/BRK — KRE has zero exposure. Don't confuse "thesis isn't showing in YTD" with "thesis is wrong."
- [2026-04-20] **False-petro-geopolitics cluster on X.** Apr 19-20 saw 3 hoax claims (WhaleInsider Hormuz "zero/first" MISFRAMED, Kazakhstan ban FALSE, Don Johnson 14.5mbpd-short pattern-killed). All X-platform, unsourced/secondhand, extreme-absolute. Policy: assume hoax on unsourced petro-geopolitics headlines until primary confirms.
- [2026-04-20] **"% of 2009" and "vs peak" framings are often portfolio-size artifacts, not rate moves.** FHA "180% of 2009" was count-basis on a portfolio ~1.65x larger → rate-basis ~1.08x; actual FHA SDQ ~45% of 2009 peak. When headline compares current to prior-crisis peak using COUNTS not RATES, flag it. CORRECTED-FRAMING verdicts here are the norm.
- [2026-04-24] **Telegram inbound flake was multi-bot token competition.** `enabledPlugins.telegram` at user-scope → every claude session spawned its own `bun server.ts` polling same token; Telegram's `getUpdates` delivers each message to ONE poller. Diagnosis: `ps -ef | grep bun.*telegram` — multiple processes = bug. Fix: move config to project-scope, kill orphan bots. Only WALTER + PROME on Telegram per root CLAUDE.md.
- [2026-04-25] **Iran day-cluster reached ≥12 channels Apr 19-24.** Iran-buildup-and-diplomacy themed signals are converging across multiple mechanisms (kinetic, sanctions, diplomacy, military posture). NEXUS classification overdue. Pattern: when a thematic cluster crosses ≥10 channels, formal cluster classification + Will-attention prompt is warranted.
- [2026-04-25] **Hydrocarbon-infra-stress meta-cluster crosses ≥4 geographies.** Geelong AU / Pachpadra+Jhagadia IN / Corpus Christi TX / Russia-strikes / Hengli OFAC supply-chain disruption. Different mechanisms (war / fire / sanctions / water / accidents) but same outcome (refining/petrochem capacity at risk). Aggregated framing has more thesis weight than individual incidents.
- [2026-04-26] **2026 Iran war anchor (verified Apr 26 via WebSearch).** War started ~Feb 27 2026 (US-Israel + Iran kinetic exchange); Iran struck 100+ targets across 11 US bases (Kuwait/Qatar/Bahrain/Saudi/UAE/Jordan); damage "far worse than publicly acknowledged" per NBC Apr 25; ceasefire Apr 8 mediated by Pakistan; Trump extended pending Iran "unified proposal." Today is day 58-59 post-ceasefire-start, ceasefire EXTENDED but FRAGILE. **US naval blockade on Iran ports ACTIVE during ceasefire (37+ vessels redirected = the SIG-007 context); Hormuz traffic at "screeching halt"; Iran has seized 2 ships near strait; mediated talks STALLED with little US-Iran demand-overlap; Israel-Lebanon kinetic continuing despite ceasefire (Netanyahu rejected Lebanon inclusion).** Iran-cluster framing: post-Apr-8-ceasefire dynamics under active US blockade, NOT pre-war buildup. Thesis weight is HIGHER than buildup framing implies. STATUS NETWORK AWARENESS has explicit IRAN-WAR ANCHOR callout for boot reading.
- [2026-04-26] **Hydrocarbon-infra cluster extended to 5+ geographies** (now adds St. Helena Parish LA pipeline explosion Apr 25). 6 mechanisms, 5 geographies. Same-outcome framing strengthens.
- [2026-04-26] **PC-stress meta-cluster ≥7 nodes.** TCW Red Lobster 98% (-014-002) / IMF GFSR (-014-004) / Blue Owl founder-pledged-loan unwind $1.1B (-020-004) / Fitch BDC redemptions +36% QoQ (-020-009) / Man Group $6B (-024-006) / SoftBank $10B OpenAI margin loan (-024-012) / Bloomberg Apr 11 Fed asking banks for PC exposure details (-026-012). Pattern: writedown / pledged-loan-unwind / BDC redemption surge / single-client AUM pull / hedge-fund margin-loan / regulatory inquiry. Six different transmission vectors all pointing same direction. NEXUS classification overdue.
- [2026-04-26] **Consumer-stagflation-stack 4 nodes** UMich record-low 49.8 + 1Y inflation expectations 4.7% (jump from 3.8%, largest since April 2025) + CC delinq 12.7% approaching 2009 peak + FL LABOR weakness + farm bankruptcies +46% YoY. Sentiment-trough + inflation-expectations-rising = worst Fed-reaction-function setup, ties Fed's hands on cuts.
- [2026-04-26] **Bank-collateral-compression cluster 4 nodes** residential housing weakening (-026-002 Zillow + Realtor) + Baltimore CRE -29% properties (-026-009) + US office vacancy 20.2% (-024-005) + Phoenix/Denver multi-family (-026-014). Macro-vs-micro divergence consistently the signal: headlines moderate, bottom-up special-servicing/distress more acute.
- [2026-04-28] **Bank-collateral-compression cluster extended to ≥6 nodes + NEW political/legislative vector.** Adds Louisville KY Home Life Building (-028-003 $15M→$4.67M credit bid, 69% erasure) + Phoenix BTR ROAD-Act regulatory financing freeze (-028-004). The ROAD Act vector is qualitatively new — prior cluster nodes were all market-mechanism (rents falling, vacancies rising, special-servicing rising); this is regulatory shock that collapses the institutional buyer pool for SFR. BARON political-network-mapping value is high here. PC-stress meta-cluster also extended to ≥8 nodes (added Boaz-Weinstein-cut-price-exit-rejected -028-005, pairs Blue Owl founder unwind -020-004 = two-sided OWL stock pressure pre-Q1 earnings Wed Apr 30).
- [2026-04-28] **Phoenix housing channel base-rate overstatement skew, 2/2 confirmed.** SIG-026-014 (Roger @rdd147 multi-family rents −20-25% → Yardi −4-5%) + SIG-028-004 (Hancock Builders "entire industry nationwide is shut down" → BTR new-deal financing freeze, in-flight projects continuing). Both Phoenix-area Twitter/local-news housing claims overstate. Apply: signals from Phoenix housing channels enter with prior on overstatement; verify-research is mandatory for extreme-absolute claims; calibrate confidence to ≤0.65 even after verify directional-confirms.

## References

- **Root `CLAUDE.md`** — git protocol, agent lifecycle rules, cost model, status hierarchy.
- **`AGENTS/WALTER/CLAUDE.md`** — spawn protocol, canonical-source lookup table, RULES, closeout checklist git steps 16a-16f.
- **`AGENTS/WALTER/design/`** — all spec docs. FORMAT_SPEC for signal schema, ROUTING_TABLE for routing, FILTER_SPEC for filter, CHECKLIST for process.
- **`/COP.md`** at repo root (paused Apr 14). Template at `design/COP_TEMPLATE.md`.
- **Market data:** `.venv/bin/python3 FORGE/tools/market-data/dashboard.py`.

## Session Notes

### CHANGES SINCE LAST SESSION (Apr 28 Tue AM — Will-driven 6-image batch, 7 dispatches + 2 verify-spawns + 0 kills, BOARD 86→93)

Boot completed normally; pull failed on auth (Apr 26 unresolved, branch +2 ahead origin). Will pinged Telegram msg 1108 "boot up, signals coming" → boot-confirm reply msg 1109. Single 6-image batch arrived msgs 1110-1115 at 12:43 UTC; processed in ~50 min including 2 parallel verify-spawns.

**6 images / 7 signals (image 5 split into Blue-Owl + Merz-Iran):**
1. **FRED chart China BIS Real Residential Property Prices** → SIG-001 ZHAO ROUTINE 0.85 (index <2005 baseline, two-decade real-appreciation erasure; ZHAO Tier 2 STALE 26d spawn-needed).
2. **ZH/WSJ OpenAI CFO Friar revenue/user miss + ~$600B data-center commitment** → SIG-002 BROCK PRIORITY, **verify CORRECTED-FRAMING 0.65** (Altman+Friar joint denial moderates "funding distress" framing; "board questioning wisdom" is paraphrase-stretch — more precisely Friar pushing discipline / board scrutinizing; ~$600B aggregate not Stargate $500B alone; Apr 28 premarket Oracle + AI-infra chip names tumbling).
3. **Louisville Courier Journal Kentucky Home Life Building** → SIG-003 REGINALD PRIORITY 0.85 ($15M 2021 → $4.67M credit bid 2026, ≥$7.5M secured loss; Fosco LLC non-bank lender NOT KRE constituent).
4. **ABC15 Arizona Phoenix BTR Hancock "industry shut down"** → SIG-004 REGINALD PRIORITY, **verify CORRECTED-FRAMING 0.60 with MAJOR DISCOVERY**: catalyst is the **21st Century ROAD to Housing Act** (Senate 89-10 Mar 10-12 2026) forcing 7-yr disposal of institutional 350+ SF home portfolios → BTR institutional buyer pool collapse → new-deal financing freeze pending House reconciliation. **Regulatory not credit-cycle.** In-flight projects continue (~64K BTR units under construction Q1 2026 per Arbor/Chandan); single-firm Hancock distress amplified by single-strategy concentration. NEW political/legislative vector added to bank-collateral-compression cluster — BARON pickup value high.
5a. **FT Blue Owl investors REJECTED Boaz Weinstein cut-price exit** → SIG-005 BROCK PRIORITY 0.85; pairs DIRECTLY with SIG-020-004 founder $1.1B unwind = two-sided pressure pre-OWL Q1 earnings Wed Apr 30.
5b. **FT discover-more block: Merz "US humiliated by Iran + no exit strategy"** → SIG-006 HAWK PRIORITY 0.85 (HANS Tier 2 STALE 35d, HAWK acting per backup-rule); Iran day-cluster ≥15 channels Apr 19-28 (+German-government-rhetoric vector).
6. **Coastal Journal substack + MarketWatch INTC CAO Gawel resigns post-earnings** → SIG-007 BROCK ROUTINE 0.55 (DJ Newswires factual + substack opinion-layer; pattern only, INTC not thesis-positioned).

**Clusters refined:**
- Bank-collateral-compression cluster ≥6 nodes Apr 24-28 (residential + Baltimore + office vacancy + Phoenix-Denver multi-family + Louisville + Phoenix-BTR-ROAD-Act) **+ NEW political/legislative vector**.
- PC-stress meta-cluster ≥8 nodes (added Boaz-Weinstein-cut-price-exit-rejected). Pre-OWL-Q1-earnings two-sided pressure stack: founders unwound $1.1B Apr 17 + Saba activist offering cut-price + investors rejecting.
- Iran day-cluster ≥15 channels Apr 19-28 (+ German-government-rhetoric vector via Merz).

**0 kills today.** **Verify-research 48h cumulative: 13 → 15.** **No spec changes.**

**Will batch summary sent via Telegram (msg 1116).** **Push from Apr 26 (commits 8b8af251 + 46067035) + today's still pending on auth — to retry at session end.**

### NEXT SESSION

**TOP PRIORITY (time-sensitive):**
1. **🔴 OWL Q1 earnings Wed Apr 30** — pairs SIG-W-20260428-005 (Boaz cut-price-rejected) + SIG-W-20260420-004 (founder $1.1B unwind) + SIG-W-20260424-012 (SoftBank pledge) + SIG-W-20260426-012 (Fed-PC inquiry) + SIG-W-20260428-002 (OpenAI capex stress). PC-stress meta-cluster ≥8 nodes — earnings is the catalyst.
2. **AI-bubble-cracks + AI-infra-chip Apr 28 repricing** — Oracle + chip names tumbling premarket per verify on SIG-028-002. Track market-vol response Apr 28 close.
3. **ROAD Act House reconciliation timing** — political-network-mapping the pivot (BARON pickup). When does House act? Grandfathering language? This is the catalyst that determines BTR-financing-freeze persistence.
4. **Iran cluster state-update** — Merz quote = ally-rhetoric drift; track follow-on European actions; Hormuz any resumption; ceasefire-resolution.
5. **Push retry** — auth issue from Apr 26 still unresolved; commits 8b8af251 + 46067035 + today's all sitting locally.

**Housekeeping (deferrable):**
6. **OZK Q1 earnings post-mortem** — REGINALD pickup still pending.
7. **Filter v2 Segment D implementation** — Will picked A confidence_note Apr 20 msg 856; ~1hr.
8. **NEXUS cluster classification OVERDUE across 6+ active clusters** — Iran post-ceasefire, hydrocarbon-infra, PC-stress, consumer-stagflation-stack, bank-collateral-compression (now with political vector), maritime-energy-security.
9. **HAWK / HANS / ZHAO stale 25-35d** — routing pressure mounting; Will-decide spawn or refresh.
10. **RED refresh** still overdue.
11. **HENRY + RED SIGNAL_INTAKE.md** prompts still transcript-only.
12. **COP refresh** still OFF — resume trigger? (extra-load-bearing now that Iran-war anchor + ROAD Act + PC-stress all need visible network-state).
13. **BOARD_CONSUMPTION_SPEC propagation** to 14 Tier 1 CLAUDE.md still pending.

### OPEN DESIGN DECISIONS (need Will)
- **Filter v2 Segment D** — DECIDED option A confidence_note; implementation deferred. ~1hr next session.
- **BOARD_CONSUMPTION rollout cadence** — Will hand-routing still; durable rollout requires propagation to 14 agent CLAUDE.md files.
- **COP refresh cadence** — resume trigger? (Iran-war state + ROAD Act + PC-stress would benefit from visible COP node).
- **NEXUS cluster classification** — does WALTER continue informal cluster tracking via STATUS, or NEXUS-spawn forcing function?
- **Push auth fix** — GitHub token / credentials need refresh (Will action; WALTER cannot self-resolve).
