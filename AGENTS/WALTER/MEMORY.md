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

## References

- **Root `CLAUDE.md`** — git protocol, agent lifecycle rules, cost model, status hierarchy.
- **`AGENTS/WALTER/CLAUDE.md`** — spawn protocol, canonical-source lookup table, RULES, closeout checklist git steps 16a-16f.
- **`AGENTS/WALTER/design/`** — all spec docs. FORMAT_SPEC for signal schema, ROUTING_TABLE for routing, FILTER_SPEC for filter, CHECKLIST for process.
- **`/COP.md`** at repo root (paused Apr 14). Template at `design/COP_TEMPLATE.md`.
- **Market data:** `.venv/bin/python3 FORGE/tools/market-data/dashboard.py`.

## Session Notes

### CHANGES SINCE LAST SESSION (Apr 26 Sun — Will-driven heavy intake, 15 dispatches + 4 verify-spawns + 1 kill, BOARD 71→86; Iran-war network anchor verified mid-session)

Boot completed normally. Will pinged Telegram (msgs 1068, 1070) "look at signals." 5 sub-batches processed across ~9 hours.

**Batches:**
1. **Beckworth Substack 4-msg article** on Fed Overton-window-shifting-to-demand-driven framework → SIG-001, verify CORRECTED-FRAMING 0.72 (Mar 3 trio not joint, Hill at ABA Mar 9-11, DW-LCR from Bessent not Bowman, Miran 1of4 authors, $1.2-2.1T not $1-2T, Warsh nominee not seated).
2. **5-image Twitter batch** (msgs 1082-1086) → SIG-002 housing combined Phase 1b (Zillow ZHVI 35.5% top-200 metros + Realtor.com SQFT −2.3% YoY 13wk) / SIG-003 St. Helena LA pipeline / SIG-004 AAL $4B fuel / SIG-005 farm bankruptcies CORRECTED-FRAMING 0.75 / SIG-006 Goldman Mei oil-shock-jobs CORRECTED-FRAMING 0.80 ROUTINE / SIG-007 USS Pinckney/Sevan CONFIRMED 0.95.
3. **UMich text** (msg 1088) → SIG-008 April final 49.8 + 1Y inflation expectations 4.7% jump CORRECTED-FRAMING 0.88, refinement of -010-001.
4. **ZH Baltimore CRE article** (msgs 1089-1090) → SIG-009 0.65 (ZH source layer + Sun primary not pulled; MTB BAL-HQ angle).
5. **5-image batch** (msgs 1092-1096) → SIG-010 Apollo foreign-private > foreign-CB UST / SIG-011 UKMTO 045-26 Mareeyo Somalia hijack / SIG-012 Bloomberg Apr 11 Fed-PC inquiry / SIG-013 Iran delegation Pakistan corrected / SIG-014 Phoenix/Denver multi-family CORRECTED-FRAMING 0.75 (Yardi −4-5% NOT −20-25%) / KILL Bloomberg climate-inflation Novelty / SIG-015 NBC bases damage HELD pending Will input → reframed as historical pre-ceasefire damage.

**MAJOR MID-SESSION CORRECTION via Will-input + WebSearch verify:** the 2026 Iran war (Feb 27 onset, Apr 8 ceasefire mediated by Pakistan, day 58-59 today, US naval blockade ongoing during ceasefire = SIG-007 context, Hormuz at standstill, Israel-Lebanon kinetic continuing) was incompletely framed in my session-context. STATUS NETWORK AWARENESS now has explicit IRAN-WAR ANCHOR callout at top + new MEMORY findings.

**Clusters built/refined:** Iran day-cluster ≥14+ channels (added Sevan + Mareeyo + delegation + retrospective bases damage); PC-stress ≥7 nodes (added Bloomberg Fed-PC inquiry); consumer-stagflation-stack 4 nodes (UMich + CC delinq + FL LABOR + farm bankruptcies); bank-collateral-compression 4 nodes (residential + Baltimore + office vacancy + multi-family); maritime-energy-security 3-vector (Hengli + Pinckney + Mareeyo); hydrocarbon-infra 5 geographies (now adds LA).

**Verify-discipline lesson:** verify-research can have right-history-wrong-tense (BRICS bases case). Cross-check current-state against MEMORY/STATUS network anchor before accepting framing wholesale.

**Will's procedure exchange (msg 1102):** asked me to clarify confused "framing-hallucination" passage. I overcorrected — the agent had real history but wrong tense. Cleaned up framing in subsequent reply (msg 1103) and STATUS/MEMORY anchors fixed.

**No spec changes. Verify-research sub-agents 48h cumulative: 9 → 13.**

### NEXT SESSION

**TOP PRIORITY (time-sensitive):**
1. **Iran cluster state-update** — Araghchi return-to-Islamabad outcome; ceasefire-resolution direction; any blockade-related kinetic incident; Hormuz traffic any resumption.
2. **OZK Q1 earnings post-mortem** — REGINALD pickup still pending on SIG-024-001/-005/-007 + new SIG-026-009 Baltimore.
3. **Apr 30 OWL Q1 earnings** — pairs SIG-W-20260420-004 (Blue Owl founders unwind) + SIG-W-20260424-012 (SoftBank pledge) + SIG-W-20260426-012 (Fed-PC inquiry).
4. **Brent Mon pre-market open** — combined Iran-cluster + Hormuz-standstill + UKMTO Mareeyo-hijack risk.

**Housekeeping (deferrable):**
5. **Filter v2 Segment D implementation** — Will picked A confidence_note Apr 20 msg 856; ~1hr.
6. **Path B (CHAT_BUFFER hooks)** ship-or-clean — no cold-start friction surfaced; lean clean up.
7. **BOARD_CONSUMPTION_SPEC propagation** to 14 Tier 1 CLAUDE.md still pending.
8. **NEXUS cluster classification** OVERDUE across 6+ active clusters (Iran post-ceasefire, hydrocarbon-infra, PC-stress, consumer-stagflation-stack, bank-collateral-compression, maritime-energy-security).
9. **HAWK / HANS / ZHAO stale 22-31d** — routing pressure; Will-decide spawn or refresh.
10. **RED refresh** still overdue.
11. **HENRY + RED SIGNAL_INTAKE.md** prompts still transcript-only.
12. **COP refresh** still OFF — resume trigger? (extra-load-bearing now that Iran-war anchor needs visible network-state).

### OPEN DESIGN DECISIONS (need Will)
- **Filter v2 Segment D** — DECIDED option A confidence_note; implementation deferred. ~1hr next session.
- **BOARD_CONSUMPTION rollout cadence** — Will hand-routing still; durable rollout requires propagation to 14 agent CLAUDE.md files.
- **COP refresh cadence** — resume trigger? (Iran-war state would benefit from visible COP node).
- **NEXUS cluster classification** — does WALTER continue informal cluster tracking via STATUS, or NEXUS-spawn forcing function?
