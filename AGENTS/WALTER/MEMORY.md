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

## References

- **Root `CLAUDE.md`** — git protocol, agent lifecycle rules, cost model, status hierarchy.
- **`AGENTS/WALTER/CLAUDE.md`** — spawn protocol, canonical-source lookup table, RULES, closeout checklist git steps 16a-16f.
- **`AGENTS/WALTER/design/`** — all spec docs. FORMAT_SPEC for signal schema, ROUTING_TABLE for routing, FILTER_SPEC for filter, CHECKLIST for process.
- **`/COP.md`** at repo root (paused Apr 14). Template at `design/COP_TEMPLATE.md`.
- **Market data:** `.venv/bin/python3 FORGE/tools/market-data/dashboard.py`.

## Session Notes

### CHANGES SINCE LAST SESSION (Apr 24-25 Fri-night Will-driven heavy intake — 13 dispatches + 4 verify-spawns + 3 kills, BOARD 58→71)

Boot completed (STATUS / MEMORY / LAST_COMP / REGISTRY / ROUTING / BOARD). Telegram inbound clean throughout (single bun PID 89881, Apr 24 morning multi-bot fix held).

**4 image batches processed** (msgs 1018-1023, 1027-1030, 1033-1038, 1045-1050). 13 signals dispatched (SIG-W-20260424-001 through -013), 3 killed (msg 1023 FL drought / msg 1034 WSJ teaser / msg 1037 Wake new-home analog), 4 verify-research sub-agents spawned (FL Scott unemp CORRECTED-FRAMING 0.70 / Hengli identity+novelty CONFIRMED 0.85 / Corpus Christi water+petrochem CONFIRMED-w-nuance 0.80 / USAF ME airlift+3-carrier CONFIRMED 0.85 despite RT-origin source-flag).

**Major clusters built:** Iran day-cluster ≥12 channels Apr 19-24 (8 Apr 19 + Tuapse + Hengli OFAC + diplomacy cascade + USAF airlift + Ukraine-Russia kinetic adjacent); Hydrocarbon-infra-stress ≥4-5 geographies; Asset-manager stress 3 nodes (TCW writedown / Blue Owl pledged-unwind / Man Group $6B pull) + AI-leverage opposite-direction (SoftBank levering vs Blue Owl founders de-risking); Positioning-extreme cluster ≥14 channels (added Kobeissi Nasdaq futures); Consumer-credit + LABOR convergence (FL state-above-US + CC 90+ approaching 2009 peak with unemployment-asymmetry frame).

**OZK Q1 earnings day adjacency on -001 (FL LABOR), -005 (office vacancy MSA), -007 (CC delinq).** REGINALD pickup pending — Will hand-routing in interim per his Apr 24 23:07 UTC confirmation that BOARD-consumption rollout is in-progress.

**Will's procedure question (msg 1041)** — answered honestly: "dispatched" = BOARD/INDEX/route_log persisted, NO push to recipient inboxes per his Apr 14 BOARD-only policy, agents only consume if their CLAUDE.md has BOARD-boot-step (currently only WALTER does), so signals reach Will via Telegram + WALTER cluster synthesis but not yet downstream agents until rollout. Offered 3 options; Will confirmed hand-routing in interim. **Will's context question (msg 1043)** — gave concrete numbers (~25K per mid-batch, safe envelope ~3 mid-batches before degradation). Closeout requested at ~145K (msg 1053).

**No spec changes. Verify-research sub-agents 48h: 5 → 9 (cumulative).**

### NEXT SESSION

**TOP PRIORITY (time-sensitive):**
1. **Brent Mon pre-market open (Sun evening ET)** — SIG-009 Ukraine mass strike on Russian oil-infra geography risks gap-up; SIG-002 Hengli OFAC + 003 diplomacy contradictions set up asymmetric move either direction.
2. **OZK Q1 earnings post-mortem** — REGINALD pickup pending on SIG-005, -007, -001. Will hand-routing in motion.
3. **Iran cluster monitoring** — Witkoff+Kushner travel verify within 48-72h; Araghchi-Islamabad meetings outcome.

**Housekeeping (deferrable):**
4. **Filter v2 Segment D implementation** — Will picked A (optional `confidence_note`) Apr 20 msg 856; ~1hr (FORMAT_SPEC + CHECKLIST edits, no migration).
5. **Path B (CHAT_BUFFER hooks)** ship-or-clean — no cold-start friction surfaced; lean clean up.
6. **BOARD_CONSUMPTION_SPEC propagation** to 14 Tier 1 CLAUDE.md still pending.
7. **NEXUS cluster classification** OVERDUE across 5 active clusters (Iran, hydrocarbon-infra, asset-manager, positioning-extreme, consumer-credit + LABOR).
8. **HAWK / HANS / ZHAO stale 22-31d** — routing pressure; Will-decide spawn or refresh.
9. **RED refresh** still overdue.
10. **Apr 30 OWL Q1 earnings** — pairs SIG-W-20260420-004 (Blue Owl founders) + SIG-W-20260424-012 (SoftBank pledge-loan).
11. **HENRY + RED SIGNAL_INTAKE.md** prompts still transcript-only.
12. **COP refresh** still OFF — resume trigger?

### OPEN DESIGN DECISIONS (need Will)
- **Filter v2 Segment D** — DECIDED option A confidence_note; implementation deferred. ~1hr next session.
- **BOARD_CONSUMPTION rollout cadence** — Will hand-routing today; durable rollout requires propagation to 14 agent CLAUDE.md files.
- **COP refresh cadence** — resume trigger?
- **NEXUS cluster classification** — does WALTER continue informal cluster tracking via STATUS, or NEXUS-spawn forcing function?
