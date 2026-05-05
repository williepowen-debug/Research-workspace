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
- [2026-05-05] **Sub-agent independent verdict before structural moves.** Pass 1 + Pass 2 of the BOARD INDEX cluster refactor each got an independent read-only sub-agent verification spawn between draft and execute. Pass 1 spawn returned `[LOOKS-GOOD]` with 0 forced edits + 1 marginal flag + observations on 2 small-cluster naming risks. Pass 2 spawn returned `[PASS]` 6/6 checks including byte-level row-content fidelity diff against `git show {pre-rewrite-commit}:file`. Cost ~$0.03-0.04 per spawn. Pattern: when about to ship a structural change (file rewrite, schema migration, taxonomy lock-in), spawn a sub-agent to verify against the rubric before execute — same cost as one verify-research, much higher leverage. Apply: any structural pass with an independent rubric (taxonomy doc / spec / mapping table) gets a verify spawn before commit. Will-invitation pattern works well; can also be unprompted if confidence in the structural change is shaky.

## Findings

- [2026-05-05] **Structural refactor pattern: sequenced passes + per-pass Will checkpoint + persisted running list.** May 4-5 STATUS.md refactor (204→110 lines / ~80k→~27.5k bytes, 7 commits) worked because: (a) **diagnostic before plan, plan before exec** — read all the boot docs, sent a 6-pattern diagnostic, then a 4-pass plan, then per-pass Will-approval; (b) **one or two file changes per pass** with explicit checkpoint (per `feedback_break_multifile_updates`); (c) **POV check mid-flight** surfaced Pass-4 prerequisite (REGISTRY refresh) Will hadn't asked for but mattered; (d) **canonical running list in `LAST_COMPLETION.md` FOLLOW-UP** survives session handoff (also pointed at from CLAUDE.md IDENTITY + boot step 3 for discoverability). Anti-pattern avoided: trying to do trim + restructure + content-rewrite in one big sweep.
- [2026-05-05] **"verified-as-of" stamp + re-verify trigger pattern** (introduced in `anchors/IRAN_WAR.md`) — load-bearing macro state goes in a single-purpose anchor file with explicit "verified-as-of {date}" + re-verify trigger ("kinetic state-change OR every 7d OR pre-dispatch on cluster"). Beats embedding the same content in STATUS.md NETWORK AWARENESS where it goes stale invisibly. Currently a one-off; second anchor (Fed-framework / BOJ / OPEC+) would canonize it as a pattern.
- [2026-05-05] **Regenerate-at-closeout vs snapshot-and-let-go-stale.** Pass 4 dropped the embedded NETWORK AWARENESS table (which duplicated REGISTRY.tsv on Status/Updated columns and went stale silently) and replaced it with a regenerated "today's routing + stale agents" subsection sourced from REGISTRY.tsv at each closeout. Pattern applies to any state that has a canonical source elsewhere — don't snapshot, regenerate.
- [2026-05-05 PM] **Cluster as discovery axis, not routing axis.** The BOARD INDEX cluster refactor formalized the distinction. **Domain** (LABOR, OIL_ENERGY, BANK_CRE — owned by FORMAT_SPEC) is the recipient-routing axis: which agent does the signal go to? **Cluster** (IRAN_HORMUZ, PC_STRESS, BANK_COLLATERAL — owned by CLUSTER_TAXONOMY) is the thematic-narrative axis: where does this signal sit in the network's mental map? One signal has one domain (routing) and one primary cluster (discovery); they are NOT the same axis and conflating them is the failure mode. Apply: when designing other categorization layers, ask "is this for routing or discovery?" — answer changes the rules. Cross-cluster signals get one primary (substance > mechanism > action-recipient resolution) and a secondary tag in the body, NOT multi-cluster placement.
- [2026-05-05 PM] **Cluster meta-tracking moved from MEMORY findings to BOARD INDEX cluster sections.** Prior MEMORY entries that tracked "PC-stress ≥9 nodes / hydrocarbon-infra ≥5 geographies / bank-collateral ≥6 nodes / consumer-stagflation 4 nodes / Iran day-cluster ≥16 channels" are now superseded — live counts come from `/BOARD/INDEX.md` cluster section headers. MEMORY findings file durable patterns (overstatement skews, framing rules, base-rate cautions); cluster-size-tracking files itself.
- [2026-04-11] **Trust disk over memory.** `/COP.md` existed since Apr 7 while NEXT_SESSION claimed otherwise. `ls` the file before believing handoff doc.
- [2026-04-11] **Stale-agent flagging is highest-leverage boot output.** Agents with Status/Updated/Focus columns >5 days old should be surfaced explicitly in STATUS, not buried.
- [2026-04-11] **`git pull --rebase --autostash`** for dirty-tree cases. Captures tracked changes only; leaves untracked files (other agents' new work) untouched.
- [2026-04-15] **Iran state can stale within 24h.** Spot-check Iran/Hormuz state before anchoring downstream signal framing.
- [2026-04-15] **Regional outperformance is mechanical, not thesis-killing.** XLF underperformance is V/MA/GS/MS/BX/KKR/BRK — KRE has zero exposure. Don't confuse "thesis isn't showing in YTD" with "thesis is wrong."
- [2026-04-20] **False-petro-geopolitics cluster on X.** Apr 19-20 saw 3 hoax claims (WhaleInsider Hormuz "zero/first" MISFRAMED, Kazakhstan ban FALSE, Don Johnson 14.5mbpd-short pattern-killed). All X-platform, unsourced/secondhand, extreme-absolute. Policy: assume hoax on unsourced petro-geopolitics headlines until primary confirms.
- [2026-04-20] **"% of 2009" and "vs peak" framings are often portfolio-size artifacts, not rate moves.** FHA "180% of 2009" was count-basis on a portfolio ~1.65x larger → rate-basis ~1.08x; actual FHA SDQ ~45% of 2009 peak. When headline compares current to prior-crisis peak using COUNTS not RATES, flag it. CORRECTED-FRAMING verdicts here are the norm.
- [2026-04-24] **Telegram inbound flake was multi-bot token competition.** `enabledPlugins.telegram` at user-scope → every claude session spawned its own `bun server.ts` polling same token; Telegram's `getUpdates` delivers each message to ONE poller. Diagnosis: `ps -ef | grep bun.*telegram` — multiple processes = bug. Fix: move config to project-scope, kill orphan bots. Only WALTER + PROME on Telegram per root CLAUDE.md.
- [2026-04-26 → moved to anchor file 2026-05-04 → cluster-tracking superseded 2026-05-05] **Iran-war anchor → `anchors/IRAN_WAR.md`.** Verified-as-of stamp + re-verify trigger (kinetic state-change / 7d / pre-dispatch on cluster). Iran-cluster live state in BOARD INDEX `IRAN_HORMUZ` section (22 signals as of May 5).
- [2026-04-28] **Phoenix housing channel base-rate overstatement skew, 2/2 confirmed.** SIG-026-014 (Roger @rdd147 multi-family rents −20-25% → Yardi −4-5%) + SIG-028-004 (Hancock Builders "entire industry nationwide is shut down" → BTR new-deal financing freeze, in-flight projects continuing). Both Phoenix-area Twitter/local-news housing claims overstate. Apply: signals from Phoenix housing channels enter with prior on overstatement; verify-research is mandatory for extreme-absolute claims; calibrate confidence to ≤0.65 even after verify directional-confirms.

## References

- **Root `CLAUDE.md`** — git protocol, agent lifecycle rules, cost model, status hierarchy.
- **`AGENTS/WALTER/CLAUDE.md`** — spawn protocol, canonical-source lookup table, RULES, closeout checklist git steps 16a-16f.
- **`AGENTS/WALTER/design/`** — all spec docs. FORMAT_SPEC for signal schema, ROUTING_TABLE for routing, FILTER_SPEC for filter, CHECKLIST for process.
- **`/COP.md`** at repo root (paused Apr 14). Template at `design/COP_TEMPLATE.md`.
- **Market data:** `.venv/bin/python3 FORGE/tools/market-data/dashboard.py`.

## Session Notes

### CHANGES SINCE LAST SESSION (May 5 PM Tue — BOARD INDEX 3-pass cluster-organization refactor + 2 sub-agent verifications, 0 BOARD dispatches, 4 commits)

Single-arc Will-driven categorization session. End-to-end boot test of May 4-5 STATUS structure passed. Will asked about pruning/merging BOARD; I surfaced 3 goals (α/β/γ); Will picked α (categorize by cluster). 4-pass plan with checkpoints; sub-agent verification spawns between Pass 1↔2 and Pass 2↔3. Full session log entry in STATUS.md SESSION LOG.

**Commits:** `e450a128` Pass 1 (CLUSTER_TAXONOMY.md v0.1 + cluster_assignment_v1.tsv 98-row mapping + CHECKLIST v0.9 + CLAUDE.md ownership row) → `8b332361` Pass 2 (INDEX flat→10 cluster sections + ToC + FORMAT_SPEC v0.7 `cluster:` field; sub-agent verified [PASS]) → `8084961a` Pass 3 (STATUS lead-paragraph + CLAUDE.md boot/protocol/key-files alignment) → this closeout.

**Findings filed today:** Sub-agent independent verdict before structural moves (Feedback). Cluster as discovery axis not routing axis (Finding). Cluster meta-tracking moved from MEMORY to BOARD INDEX (Finding — supersedes 7 prior cluster-size-tracking entries which were trimmed).

**Spec changes:** FORMAT_SPEC v0.6→v0.7 (`cluster:` YAML header field). CHECKLIST v0.8→v0.9 (Phase 2 cluster-assignment step). New canonical-source `design/CLUSTER_TAXONOMY.md` v0.1.

**0 BOARD dispatches.** **0 kills.** **0 signal verify-research spawns** (the 2 spawns this session were structural-review, not Phase-1.5). **Push state clean** — all 4 commits shipped to origin.

### NEXT SESSION

**Time-sensitive:**
1. **NFP Friday May 8** — LABOR carry-forward.
2. **OBDC Q1 Wed May 6** — BROCK pre-built threshold reads.
3. **Q1 Call Report window May 1-10** — REGINALD recheck.
4. **Iran-war anchor re-verify** — `anchors/IRAN_WAR.md` verified-as-of 2026-05-04, refresh boundary 2026-05-11 minimum OR earlier on visible kinetic state-change. Spot-check BRENT/HAWK/HANS at boot.

**Today's structural changes that need a boot test:**
5. **End-to-end boot test of new BOARD INDEX cluster structure** — does cluster ToC scan cleanly? Do anchor links work? Does the new boot-step 7 instruction read sensibly? Net context-budget effect of clustered INDEX vs flat?

**Cluster taxonomy v0.1 watch items:**
6. **FED_FRAMEWORK at 2 signals** — sub-agent flagged for v0.2 rename to UST_PLUMBING if it doesn't grow. Watch what next 2-3 macro-plumbing signals look like before deciding.
7. **AI_INFRA_CAPEX at 3 signals** — has forward-momentum (META/MSFT capex advisory event-pending). Hold.
8. **IRAN_HORMUZ at 22 signals** — internally heterogeneous (kinetic / sanctions / oil-supply-downstream / diplomatic). Pass 4 sub-cluster breakdown candidate IF reads dense in next session's boot.

**Carry-forward open items (full list in `LAST_COMPLETION.md` FOLLOW-UP):**
- HAWK + HANS framing predates May 4 ceasefire-break (refresh via Will or self-spawn).
- OZK Q1 post-mortem (REGINALD pickup pending since Apr 16).
- NEXUS classification overdue 6+ active clusters (now NEXUS reads INDEX cluster sections directly).
- BOARD_CONSUMPTION_SPEC propagation to 14 Tier 1 agent CLAUDE.md files.
- HENRY + RED SIGNAL_INTAKE.md prompts.
- Filter v2 Segment D (~1hr, decided Apr 20 option A).
- COP refresh resume (paused Apr 14).
- "verified-as-of" pattern extension (second anchor candidate).
- MEMORY.md vs LAST_COMPLETION.md duplication (Pattern D, Pass 5 territory).

### OPEN DESIGN DECISIONS (need Will — full list in LAST_COMPLETION.md)

- **Pass 4 of cluster refactor** — sub-cluster breakdown for IRAN_HORMUZ + POSITIONING_VALUATION? Decide after boot test in next session.
- **FED_FRAMEWORK rename to UST_PLUMBING** — watch 2-3 next macro-plumbing signals before deciding v0.2 taxonomy edit.
- **Cluster status flags** (🟢/🟡/🔴/⚫) — reserved for v0.2 in CLUSTER_TAXONOMY.md; ship when stale-cluster identification becomes useful.
- Pre-existing: "verified-as-of" pattern extension / MEMORY-LAST_COMP duplication / lead-paragraph cadence / Filter v2 Segment D / autonomous news-scan policy / BOARD_CONSUMPTION rollout / COP refresh resume / NEXUS classification cadence.
