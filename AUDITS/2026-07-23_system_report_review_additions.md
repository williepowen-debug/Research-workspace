# Review, Verification & Research Additions — "Research Workspace: System Analysis and Critical Assessment" (July 22, 2026)

**Reviewer:** Claude Code session (Will-directed), 2026-07-23
**Subject:** External assessment report dated 2026-07-22 (evidence snapshot)
**Method:** (1) Repo-level verification of the report's ~20 load-bearing factual claims via direct file reads + three parallel search agents; (2) live web research verifying and expanding every external citation, plus four new research threads the report did not cover.
**Caveat:** This session ran on a shallow clone (50 commits), so the three cited commit hashes (257f535, bb427ab, 48d69ac) could not be resolved directly; the file-level evidence behind all three was verified instead.

---

## Part 1 — Verification results (repo-level)

Every spot-checked claim verified. Summary:

| Report claim | Verdict | Evidence |
|---|---|---|
| STATUS density table (§6.3) | ✅ Within 1 day's drift | `wc -lc`: PROME 94/56,929 · SAM 311/67,983 · BRENT 194/39,188 · NEXUS 168/36,016 · RED 132/21,987 (2026-07-23) |
| MESSAGING docs contradiction (§3.2) | ✅ Still present 7/23 | `MESSAGING/README.md:3` "NOT YET LIVE" vs `IMPLEMENTATION_STATUS.md:23` live allowlist + root `CLAUDE.md` "Will-approved 2026-07-14" |
| OZK roster staleness (§3.1/§6.2) | ✅ but see Edit E2 | `PROME/ROSTER.md:64` "cold since 4/24; revival-gated on Q2 print Jul-21" vs DAEDALUS 7/22 sweep treating OZK live |
| SAM–RED V1.6 dialogue (§4.2), all 5 outcomes | ✅ | `AGENTS/SAM/V16_RED_DIALOGUE.md` — baton, round cap, SURVIVES bars, CONCEDE turns, flip conditions all present |
| SAM ledger: 48h falsifier, ESR letter/spirit split (§5.2) | ✅ | `AGENTS/SAM/thesis/PREDICTIONS.tsv` SAM-32 (Meiji Yasuda >¥2T, 48h), SAM-25 ("true-in-letter / false-in-spirit") |
| SAM CFTC grading lag (§6.1) | ✅ | PREDICTIONS.tsv preamble: SAM-30 "print public 7/6, adjudicated 7/10" |
| DM v1 SAM + BRENT integrations (§4.1) | ✅ | `inbox/processed/MSG-PROME-20260714-001/-002` + `messages/receipts/` ACCEPTED→INTEGRATED with canonical targets |
| BRENT gate sequence incl. "pass on chase" (§4.3) | ✅ | Outbox memos 7/10 (DENY, 1-of-2 legs), 7/16 (re-arm; "PASS ON CHASE… OVX ~61"), 7/17 (COT "de-grossing, NOT clean short-covering"; $85×3 = "premium, NOT supply loss") |
| BRENT failure memory + never-fired grading (§5.2) | ✅ | PREDICTIONS.tsv header BRT-23/24 "systematically OVER-confident" (third-order); BRT-20/25 "NOT-FIRED-PRECONDITION ≠ resolution" |
| VIOLET MOVE gate, no-double-exposure, TERRY route (§4.4) | ✅ | GATE-VIO-116 fired 7/21 (`PROME/GATES.tsv:18`); "NO new trade" (30× TLT Sep-30 77P live); TERRY inbox 7/21 |
| KB-VIO-110 → GATES.tsv origin (§3.4) | ✅ | `PROME/GATES.tsv:2` "fired 7/2 into a frozen VIOLET session… found 7/9" |
| AEOLUS negative control (§6.4) | ✅ worse now | STATUS self-dated 7/9 (14d stale at review); 7 inbox items unprocessed; wrong "did NOT break 2006 record" figure still live in STATUS + `THESIS.md:45` despite 7/16 PROME correction order |
| WATT overdue + band-discipline (§5.4/§6.1) | ✅ | WATT-05 (resolve 7/20) still OPEN; 7/16 EEA-1 held 🟠 not 🔴 (LMP $410.55<$1,000, demand 92.1%<97%) |
| REGINALD git-fresh/content-stale (§6.1) | ✅ but see Edit E1 | Uniform 7/21 19:20 bulk commit over April-vintage THESIS.md v1.4 — but file self-banners "⚠️ STALE-VINTAGE" and STATUS.md is genuinely current |
| ORACLE CLARITY miss → tool change (§4.5) | ✅ | Commits 9bc564bf + 031b0524 in local log; root-cause + coverage subcommand as described |

**Not verified:** external literature citations (checked in Part 2), trade P&L (off-repo by design), Research-Intake feed uptime.

---

## Part 2 — External research: verification + expansion (live web, 2026-07-23)

### 2.1 The report's citations — all check out; the report under-quotes them

| Source | Verified specifics the report omitted |
|---|---|
| [Google Research, "Towards a science of scaling agent systems"](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/) (Jan 28, 2026) | Centralized coordination **+80.9%** on parallelizable financial reasoning; **−39% to −70%** on sequential tasks (every MAS variant); error amplification **17.2×** (independent agents) vs **4.4×** (centralized w/ orchestrator validation); tool-use degrades past **~16 tools**; predictive model (R²=0.513) picks the right architecture for **87%** of unseen tasks from decomposability + tool density |
| [Tran & Kiela (Stanford), arXiv:2604.02460](https://arxiv.org/html/2604.02460v1) (Apr 2, 2026) | SAS ≥ MAS at matched budgets (100–10k thinking tokens) — but scope is **text-only multi-hop QA (FRAMES, MuSiQue), no tool use**; and MAS becomes competitive when single-agent **context degrades** (corruption/noise). Both caveats matter for this repo (below) |
| [Anthropic multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) | Multi-agent beat single Opus 4 by **90.2%** on internal research eval (breadth-first); token use alone explains **80%** of BrowseComp variance; multi-agent ≈ **15×** chat tokens; explicitly bad fit: shared-context / high-interdependency tasks (most coding) |
| [Rabanser, Kapoor, Narayanan et al., arXiv:2602.16666v3](https://arxiv.org/html/2602.16666v3) (June 2026) | Four reliability dimensions: **consistency, robustness, predictability, safety**; agents "silently degrade" as conditions shift → temporal re-evaluation required; reliability needs **multi-run protocols**, not single-run accuracy; financial-accuracy violations the most prevalent safety class |

### 2.2 New sources the report missed — and what they change

**A. MAST: the multi-agent failure taxonomy ([arXiv:2503.13657](https://arxiv.org/abs/2503.13657), NeurIPS 2025 D&B; [MAST repo](https://github.com/multi-agent-systems-failure-taxonomy/MAST))**
1,600+ annotated traces across 7 MAS frameworks; 14 failure modes in 3 root categories: **specification 41.8% · inter-agent coordination 36.9% · verification gaps 21.3%**.
*Implication:* the workspace's observed failures map almost entirely onto MAST's **coordination + verification** classes (unread inboxes, unpropagated OZK transition, ungraded WATT-05, orphaned KB-VIO-110) — while its heavy CLAUDE.md/contract investment has largely suppressed the *specification* class that dominates elsewhere. That is quantified external support for the report's central thesis (analytical institution ahead of operational control plane), and it makes the exception-view recommendation (P5) legible as a *verification-gap countermeasure* with a literature behind it.

**B. Debate/adversarial-review literature — RED's design is on the right side of it**
- [Heterogeneous LLM debate under adversarial peers, arXiv:2606.19826](https://arxiv.org/html/2606.19826v1) (Jun 18, 2026): an honest heterogeneous peer cut harmful revisions **89%→35%** (Llama-3.1-70B, MATH-hard); a malicious peer erased the gain (→90%); net-positive unless peers are adversarial with 77–98% probability.
- [Debate enhances truthfulness (Khan et al.)](https://www.emergentmind.com/papers/2402.06782) and [AI debate aids assessment of controversial claims, arXiv:2506.02175](https://arxiv.org/pdf/2506.02175): debate lifts weak-judge accuracy (~76% vs consultancy baselines) and pushes evidence-driven argument.
- Known failure modes: **sycophancy** and "hallucinated consensus" when majority priors are wrong ([collective truth-seeking, arXiv:2605.30391](https://arxiv.org/html/2605.30391v1); [controlled MAD study, arXiv:2511.07784](https://arxiv.org/pdf/2511.07784)).
*Implication:* RED's bounded-baton design (pre-registered SURVIVES bars, round caps, forced verdicts, flip conditions) is precisely the structure the literature says converts debate from consensus-drift into measurable gains. The report's P6 should adopt **harmful-revision rate** (did a challenge make the thesis *worse*?) as a RED metric alongside "did it change the outcome" — the V1.6 ledger already contains the raw material.

**C. Structured analytic techniques: the tradecraft canon is weaker than §9.1 implies**
Empirical literature: **ACH lacks empirical support** — trained analysts don't follow its steps, and the ACH-style matrix does not reduce confirmation bias or improve evidence-credibility sensitivity ([Dhami et al. 2019, Applied Cognitive Psychology](https://onlinelibrary.wiley.com/doi/full/10.1002/acp.3550); [critical review, Intelligence & National Security 2024](https://www.tandfonline.com/doi/abs/10.1080/02684527.2024.2304934); [Revisiting the Psychology of SATs, IJIC 2024](https://www.tandfonline.com/doi/abs/10.1080/08850607.2023.2243803)). What **does** have empirical support: **devil's advocacy and brainstorming**.
*Implication:* §9.1's implicit "ICD-203 analogy = validation" should be reframed. The workspace happens to have built the empirically supported piece (RED = devil's advocacy with teeth) and *not* the unsupported one (no ACH matrix machinery) — a better position than the tradecraft canon itself. Corollary: do not add competing-hypotheses matrices merely because the primer recommends them.

**D. ForecastBench: the human-parity picture changed materially since the report's citation**
As of July 2026, top systems are **statistically indistinguishable from superforecasters**: superforecasters 70.6% Brier Index vs best LLMs 67.9% (0.017 Brier-point gap); dataset-question parity reached ~May 2026; full parity extrapolated ~Nov 2026 (95% CI Jan 2026–Nov 2027). ([FRI: parity post](https://forecastingresearch.substack.com/p/ai-models-have-likely-reached-parity), [closing-the-gap post](https://forecastingresearch.substack.com/p/llms-are-closing-the-gap-on-human), [Brier Index](https://forecastingresearch.substack.com/p/introducing-the-brier-index), [updated methodology](https://www.forecastbench.org/assets/pdfs/forecastbench_updated_methodology.pdf))
*Implication (two-sided):* (1) strengthens P3/P4 — external calibration baselines now exist to benchmark agent ledgers against; (2) sharpens the moat question — if raw LLM forecasting skill is commoditizing to superforecaster level, the workspace's durable edge is exactly what the report says it is: the *institutional layer* (ownership, gates, falsification, failure memory), not model judgment per se.

**E. Persistent-agent systems are now a named research area**
[Always-On Agents: a survey of persistent memory, state, and governance (arXiv:2606.30306, Jun 2026, 136pp)](https://arxiv.org/pdf/2606.30306) names the workspace's exact pain points as open problems: staleness, state recovery after interruption, drift, exception handling in continuous operation. Memory-benchmark line ([LongMemEval](https://mem0.ai/blog/ai-memory-benchmarks-in-2026), [MemProbe hidden-user-state recovery, arXiv:2605.11325](https://arxiv.org/pdf/2605.11325)) treats **cross-session state recovery as a measurable task** — direct precedent for P2's "state recovery benchmark," which can borrow protocol (frozen answer key, blinded fresh-session grading) rather than inventing one.

### 2.3 Net effect on the report's §8.2 argument

The expanded evidence **narrows the report's agnosticism** in a specific direction:

1. The workspace's workload is dominated by **parallel-by-domain monitoring + tool-heavy retrieval + context-exceeding history** — the regime where Google (+80.9% parallelizable) and Anthropic (90.2%, breadth-first) find multi-agent gains, and explicitly *outside* the Stanford paper's scope (text-only, no tools; MAS competitive precisely when context degrades — and dense STATUS recovery *is* a context-degradation regime).
2. The workspace's PROME-centralized topology matches the architecture with **4.4× (not 17.2×) error amplification**.
3. The costs are also confirmed: ~15× tokens, and MAST-class coordination/verification failures — which the repo demonstrably has.

So the honest position after research is no longer "general advantage unproven, direction unknown" but: **the architecture is well-matched to task structure per current evidence; what remains unproven is the magnitude of net value after coordination costs — which is still exactly what P6's budget-matched test should measure.** P6 survives; its framing sharpens.

---

## Part 3 — Concrete edits to the report

| # | Section | Edit |
|---|---|---|
| E1 | §6.1 REGINALD | Soften "concealed": thesis file self-banners "⚠️ STALE-VINTAGE" and points to a genuinely current STATUS.md. Real failure = bulk-commit timestamps mask content vintage (git-fresh ≠ content-fresh); intent framing overstates. |
| E2 | §3.1/§6.2 OZK | Sharpen: ROSTER wasn't misclassifying — it registered "revival-gated on Q2 print Jul-21"; the gate fired and propagation lagged. Diagnosis = **transition-propagation lag**, not stale classification. Strengthens §6.2's transition-completeness point. |
| E3 | §6.4 contrast cases | Add **HAWK** as the starker negative control: FLEET_MAP 7/22 "SUNSET ARMED — zero sessions since 7/12 re-cut, synthesis pass never run, inbox accreting 21 unconsumed items." Cuts both ways: worse rot than AEOLUS, but caught by the fleet's own machinery (DAEDALUS), not by Will. |
| E4 | P3/P4 | Acknowledge **LABOR's existing Brier scoreboard** (`workbook/PREDICTIONS_SCOREBOARD.md`, built+wired 7/10, 8 preds scored) as the in-repo prototype to generalize; also note DAEDALUS's L2–L5 ladder already covers part of §6.4's six-state distinction (circularity caveat stands). |
| E5 | P1+P5 | **Merge** the open-obligation view and the exception view into one read-only projection — same sources (receipts, ledgers, gates, brief map), same operator question. Rank the merged item first; the verified failure cases (AEOLUS correction, WATT-05, OZK transition, SAM lag, HAWK inbox) are its acceptance-test suite. |
| E6 | §6.1/§7.2 | Add the **machine-local layer**: env health is per-box and invisible in git (e.g., env_doctor FAIL on the FRED-dependent pipeline at this session's boot; serial desktop⇄laptop model per `PROME/MACHINE_LOCAL.md`). Another operational-fragility class the repo-only review couldn't see. |
| E7 | §4.2 SAM | Nuance: the "two necessary failure legs" are a **union** invalidation (either leg fires → LOW), i.e., the conjunction's failure surface — the report's phrasing implies conjunction-only. |
| E8 | §8.2 | Replace the three-sentence external-evidence summary with the specific numbers and scope caveats in Part 2.1, and the task-structure match argument in Part 2.3. |
| E9 | §8.2/§6 | Add MAST (Part 2.2-A): name the repo's failure classes in taxonomy terms; note the suppressed specification class as an unclaimed strength. |
| E10 | §9.1 | Correct the tradecraft framing per Part 2.2-C: ACH is empirically unsupported; devil's advocacy is supported; the workspace built the supported piece. Delete or caveat the implication that ICD-203 alignment is itself validation. |
| E11 | §9.3 | Update ForecastBench per Part 2.2-D (parity reached/near); add the two-sided implication for the moat argument. |
| E12 | P2 | Cite the memory-benchmark line (LongMemEval/MemProbe) as protocol precedent for the state-recovery benchmark. |
| E13 | P6 | Add **harmful-revision rate** as a RED metric; note the debate literature's net-positive conditions match RED's bounded-baton design (Part 2.2-B). |
| E14 | §15.3 | Append the new sources (MAST, debate-under-adversarial-peers, Dhami 2019 + 2024 SAT reviews, FRI parity posts, Always-On Agents survey, MemProbe). |

**What should not change:** sequencing (contracts before runtime), shadow-mode discipline, §13's preservation list, and the report's refusal to claim proven aggregate edge. P6 remains the decisive experiment; the research above sharpens its prior, it does not replace it.

---

## Part 4 — Extended theme expansion (second research pass, 2026-07-23)

Six themes the report touches lightly or not at all, each with new sources and a workspace-specific implication.

### 4.1 Finance-specific LLM agent systems — the academic homologues

| Source | Finding |
|---|---|
| [TradingAgents (Xiao, Sun, Luo, Wang), arXiv:2412.20138](https://arxiv.org/abs/2412.20138) (Dec 2024, rev. Jun 2025) | Multi-agent trading firm simulation: fundamental/sentiment/technical analysts, **bull-vs-bear researcher debate**, risk-management team, traders with varied risk profiles. Claims improved cumulative return, Sharpe, and max drawdown vs baselines — **backtest only** |
| [LiveTradeBench, arXiv:2511.03628](https://arxiv.org/html/2511.03628) (Nov 2025; [trade-bench.live](https://trade-bench.live/)) | **50-day live evaluation of 21 LLMs** on U.S. stocks + Polymarket betting. Headline: **LMArena/general-benchmark scores do not predict trading performance**; static benchmark proficiency ≠ robust real-time decision-making; models show distinct persistent risk appetites and allocation styles |
| [AlphaForgeBench, arXiv:2602.18481](https://arxiv.org/pdf/2602.18481) (Feb 2026) | End-to-end strategy-design benchmarking — the eval infrastructure for LLM trading is professionalizing fast |

**Implications.** (1) The fleet is structurally homologous to TradingAgents (bull/bear ≈ RED, risk team ≈ TERRY, role analysts ≈ domain agents) — but differs in exactly the dimensions the academic frameworks lack: *longitudinal* memory across months, preserved failure ledgers, human capital authority, and refusal to auto-execute. That comparison belongs in §7.3's alternatives table. (2) LiveTradeBench's live-eval philosophy is the report's P4 "prospective, not retrospective" recommendation implemented at field scale — and its Polymarket leg overlaps ORACLE's domain, offering an external reference class for ORACLE's calibration. (3) The benchmark-skill ≠ trading-skill result is more external support for the moat argument: raw model capability is not where edge lives.

### 4.2 Memory consolidation — closeout discipline is a hand-rolled version of an emerging paradigm

| Source | Finding |
|---|---|
| ["Language Models Need Sleep" (Behrouz, Hashemi, Javanmard, Mirrokni), arXiv:2606.03979](https://arxiv.org/abs/2606.03979) (Jun 2026) | "Sleep" paradigm: distill short-term fragile memories into stable long-term knowledge with replay; "dreaming" = self-generated rehearsal |
| [Memory for Autonomous LLM Agents survey, arXiv:2603.07670](https://arxiv.org/abs/2603.07670); [Memory in the LLM Era, arXiv:2604.01707](https://arxiv.org/html/2604.01707v1) (2026) | Field consensus: consolidation is **active and lossy-by-design** — destroys raw detail in favor of compressed meaning, resolves contradictions, builds structured knowledge; five mechanism families cataloged |

**Implications.** The workspace's closeout protocol (STATUS rewrite → LESSONS extraction → >60d archive rule → NEXUS_BRIEF compression) *is* a file-native consolidation pass — the repo independently converged on what the literature now names. Two refinements follow: (1) the research treats consolidation as a **separate scheduled activity** from task execution — DAEDALUS sweeps and the NEXUS hygiene pass already approximate this; making "consolidation session" an explicit session type (distinct from research sessions) would formalize it; (2) "lossy-by-design, contradictions resolved" is the design spec for P2's current-state card — the card should *resolve* contradictions between surfaces, not mirror them.

### 4.3 Human oversight — a counterweight to the report's §6.8

| Source | Finding |
|---|---|
| ["Keeping an Eye on AI" oversight framework (Gaube, Langer, Miller et al.), arXiv:2605.16278](https://arxiv.org/pdf/2605.16278) (2026) | Effective vs **procedural** oversight; failure modes: cognitive overload, complacency/automation bias, **skill degradation from reduced task involvement**, inadequate transparency; recommends tiered authority + mechanisms that maintain operator competence through continued engagement |
| [Automation-bias systematic review (35 studies), AI & Society 2025](https://dl.acm.org/doi/10.1007/s00146-025-02422-7); [EDPS TechDispatch 2/2025](https://www.edps.europa.eu/data-protection/our-work/publications/techdispatch/2025-09-23-techdispatch-22025-human-oversight-automated-making_en) | Oversight of fluent, authoritative AI tends to become procedural; radiology evidence: expert accuracy *declines* when AI suggestions are wrong; mitigations: delayed disclosure, cognitive forcing functions |

**Implications.** This cuts against §6.8's framing more than anything else found. The report treats Will's routine exception-hunting purely as toil to automate away — the oversight literature warns that removing routine engagement is exactly how operators lose the situation awareness and skill that make their *high-value* oversight effective. Design consequence for the merged P1+P5 exception view: it should **queue exceptions for operator adjudication, not auto-clear them** — a cognitive-forcing design, not a green-dashboard design. (The report's own P5 risk note — "hiding missing fields behind green indicators" — gestures at this; the literature says it's the central risk, not a side risk.) Note also the workspace's existing rules already encode anti-automation-bias discipline the report doesn't credit: Critical Rule 3 ("agent data can be hallucinated — verify against SEC filings"; the PSEC 8.6%-not-35% incident) is a cognitive forcing function born from a live automation-bias failure.

### 4.4 Calibration — the ledgers align with elicitation best practice; add intervals

| Source | Finding |
|---|---|
| [Calibration survey line (When to Trust LLMs, arXiv:2404.17287; EmergentMind topic)](https://www.emergentmind.com/topics/confidence-calibration-in-llms) | LLMs default **overconfident**; for RLHF models, **verbalized confidence beats token probabilities**; asking for explanations alongside confidence further improves calibration |
| [QuantSightBench, arXiv:2604.15859](https://arxiv.org/pdf/2604.15859) (2026) | Evaluates quantitative forecasting with **prediction intervals**, not just point probabilities |
| [Prophet Arena, arXiv:2510.17638](https://arxiv.org/pdf/2510.17638) | Live predictive-intelligence arena for LLMs — same prospective-grading philosophy as ForecastBench |

**Implications.** (1) The fleet's practice — verbal confidence bands with written mechanism rationale, graded later — is the elicitation format the literature finds best-calibrated; that's an unclaimed strength for §5.2. (2) BRENT's measured "systematically OVER-confident on third-order transmission" is the documented LLM default failure mode, *detected and counter-weighted in-repo* via the ledger preamble — a concrete instance of the failure-memory loop doing what the calibration literature prescribes. (3) P3's normalization envelope should add an optional **prediction-interval field** for quantitative claims (price/level forecasts), per QuantSightBench — bands, not just event probabilities.

### 4.5 Durable execution — P7's feasibility cost has collapsed; its logic still holds

[Temporal Replay 2026](https://byteiota.com/temporal-replay-2026-serverless-workers-ai-agents/) shipped serverless workers and workflow streams for agent infrastructure; the [LangGraph-for-logic + Temporal-for-durability pattern](https://www.spheron.network/blog/ai-agent-workflow-orchestration-temporal-inngest-restate-gpu-cloud/) is now a commodity enterprise stack; checkpoint/journal overhead is [single-digit milliseconds per activity](https://zylos.ai/research/2026-04-24-durable-execution-agent-runtimes/) (<0.1% for long-running steps).

**Implication.** The report's P7 caution ("pilot durable runtime only after contracts stabilize") was arguably over-weighted toward infrastructure difficulty. The infrastructure is now cheap and standard; the binding constraint is exactly and only what the report's *shadow-plan* logic says: unstable message/state contracts would be automated into two sources of truth. Restate P7 as contract-gated, not effort-gated — and note the first candidate loop (overdue-prediction detection) could run on a plain cron + the exception view long before a workflow engine is warranted.

### 4.6 The intelligence community is converging on this exact design

| Source | Finding |
|---|---|
| [CIA AI co-workers announcement (Deputy Director Michael Ellis, Apr 9, 2026)](https://techstrong.ai/features/cia-moves-to-embed-ai-across-intelligence-workflows/) | CIA to embed generative-AI "co-workers" in **every analytic platform by 2028**; 300+ AI projects in 2025; first AI-generated intelligence report in agency history |
| [Defense AI Weekly LLM-adoption survey](https://defenseaiweekly.com/llm-adoption-defense/) | GCHQ: **~35% analyst-workload reduction** via automated first-pass review; doctrine across CIA/GCHQ/NGA: AI drafts, triages, and flags — **humans decide** |
| [RAND RR-1408, Assessing the Value of SATs](https://www.rand.org/pubs/research_reports/RR1408.html) | Even pre-LLM, the IC's own evidence base for SAT effectiveness was thin — consistent with Part 2.2-C |

**Implications.** The workspace's division of labor — agents monitor/draft/flag, WALTER triages, Will decides — is the doctrine the IC publicly adopted in April 2026, implemented here earlier and with a fuller audit trail than the announcements describe. For §11's "portfolio/case-study" lens this is the strongest external validation available: the design isn't idiosyncratic, it's convergent. The GCHQ 35% figure also gives P4's cost layer a public reference point for what "operationally worthwhile" looks like.

### 4.7 Consolidated: what Part 4 changes in the recommendations

| Rec | Refinement |
|---|---|
| P1+P5 (merged, Edit E5) | Exception view must be an **adjudication queue**, not a status dashboard — operator clears each exception explicitly (cognitive-forcing design per 4.3) |
| P2 | State card spec = "lossy-by-design, contradiction-resolving" consolidation artifact (4.2), benchmarked hidden-state-recovery style (Part 2.2-E) |
| P3 | Add optional prediction-interval field for quantitative claims (4.4) |
| P4 | Anchor cost/benefit against public reference points: GCHQ 35% first-pass reduction (4.6), ForecastBench/Prophet Arena live-grading norms (4.4, 2.2-D) |
| P6 | Add TradingAgents-style backtest-only framing as the *negative* template — the workspace's test must stay prospective/live per LiveTradeBench's benchmark-skill ≠ field-skill finding (4.1) |
| P7 | Re-frame as contract-gated, not effort-gated; first loop = cron + exception view, workflow engine later (4.5) |
| §6.8 | Balance "automate the toil" with the skill-degradation/complacency literature — keep the operator actively adjudicating (4.3) |
| §7.3 | Add TradingAgents/LiveTradeBench row to the alternatives table (4.1) |
| §11 | Add IC-convergence as external validation of the operating doctrine (4.6) |
