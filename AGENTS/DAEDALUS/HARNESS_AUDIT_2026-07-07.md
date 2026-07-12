# Fleet Harness Audit — LOOPS.md-derived (one-shot)

**By:** DAEDALUS · **Date:** 2026-07-07 · **Tasked by:** PROME packet 7/6 (Will-approved) · **Status:** findings delivered; **BATCH ONE (S1+S4+S5+S6) APPLIED 2026-07-08, Will-approved** — root Output Canon single-home + 18 agent files canon-pointered + live HERMES/OpenClaw instructions rewritten (the "lives in removed" scrub artifact turned out to be a 6-file class, all fixed/packeted) + dup File>verbal strikes; verified by fleet grep counters (residuals = dormant-skipped + ZHAO/TERRY packeted + historical keeps). Commits `1d2bb77`+`bb7c02c`+`f147b06`+`30a4acd`+`22d2608`. **S2 APPLIED 2026-07-08 (Will-approved, ran against current root canon — pointer lines survive any future R2 rewrite unchanged):** 24 files to cite-form via 4-editor fan-out; exceptions preserved verbatim (WALTER multi-dir scope/sanity/trailer, YEYOU manual-branch Decision-C on both surfaces, BROCK T1b, HAWK untracked-inbox rule, SHADE bash-mv guard, DEWEY crash-salvage); **both live push contradictions (OTTO, TERRY-packeted) + a THIRD drift class (stale non-ff flag-Will semantics, ≥6 files) + CORAL's drifted pull-variant eliminated**; blueprints now prescribe cite-form for new builds. Residual: WALTER `design/BOOT_PROTOCOL.md:92` (inbox-noted, WALTER-lane); NEXUS live-concurrent incident note = root-promotion candidate. **S3 APPLIED 2026-07-08 (Will-approved, per-agent verification pass — completed inline after a subagent credit outage):** result = the fleet had ALREADY deleted its manual steps when wiring boot kits — 10/10 verifiable adopters clean (one 1-line covers-clause fix, SAM); **the real finding was the INVERSE class: 4 orchestrators installed-but-UNWIRED** (CARL — plus a catalyst/docket countdown twin-script ambiguity, HAWK, HENRY, REGINALD — boot protocols never invoke their own boot.py) → wire-or-retire inbox notes routed, **PAT-040** banked (check both directions: steps the script covers AND scripts no step invokes). TERRY/ZHAO left to their pending packets; OZK dormant. **All strike items (S1-S6) now dispositioned. Remaining open: R1/R2 rewrites + roadmap builds (#1/#11) — Will/PROME.** *(Sweep-#3 registration struck 2026-07-12 — Falsification Freshness Sweep registered `sweeps/REGISTRY.tsv`.)*
**Rubric:** LOOPS.md Rules 8 (delete), 5 (rewrite-not-patch), + encode-vs-convention on `PROME/proposals/2026-07-06_skills_mcp_roadmap.md` items. *(Concepts borrowed on merit; attribution unverified per WALTER's packet — not propagated.)*
**Evidence base:** full-fleet harness survey (33 agent CLAUDE.md, 150–539 ln, 9–37 numbered steps each; PROME BOOT 93 + CLOSEOUT 243; 3 standalone CLOSEOUT.md) + grep quantification + this week's deep reads (OTTO 4-reader, ZHAO full-core, + the 20-agent profiles corpus).

---

## 0. The deletion criterion, made explicit (the packet's ask)

WALTER's 6/28 boot-split (113→61 ln, −34% per-boot cost) is the proven template. Generalized:

> **A harness step earns its inline cost iff ALL THREE hold:**
> **(a) ACTION or behavior-gate** — it changes what the agent *does* at execution time. WHY / provenance / incident-history → an on-demand rationale doc with `[→ §x]` pointers + a mechanized cross-ref guard (WALTER's `boot_protocol_xref` pattern).
> **(b) Not mechanizable** — if a script/hook can do or check it, the step becomes one line invoking the mechanism (boot.py, SessionStart hook, ledger_staleness).
> **(c) Not owned canonically elsewhere** — cite-not-restate. Restatement is where drift breeds: both confirmed push-policy contradictions in the fleet (TERRY, OTTO) live in *restated* git sections, never in root canon itself.
> **Model-upgrade trigger:** re-test (a) against the current model — instructions that exist because a weaker model wouldn't do X unprompted (style rules, read-before-edit hand-holding, repeated ⚠️ blocks) fail (a) on a stronger model and get struck.

## 1. Rule 8 — STRIKE-LIST (delete; batched, per-item rationale)

| # | Strike | Evidence / scale | Rationale | Risk |
|---|---|---|---|---|
| S1 | **Per-agent output-style rules** ("Tables > prose" ×22 files, "Numbers > narrative" ×7, source-your-claims variants) | ~6–10 ln × 22+ files ≈ 150–200 boot-loaded lines | Weaker-model compensation, verbatim-duplicated. Current models do this from ONE root-level statement. Keep domain-specific rules (e.g. ZHAO's "China data is opaque — flag confidence"), strike the generic style block | Low — root CLAUDE.md gains a 3-line style canon; agents cite |
| S2 | **Restated git protocol in agent files** (25 files carry stash/add-A/safe-push/pull-rebase recipes) | 10–25 git-keyword lines per file; 2 confirmed drift-contradictions (TERRY L161, OTTO L202-19 "push Will-coordinated" vs root auto-push) | Root CLAUDE.md owns git canon. Restatement = the documented drift mechanism. Replace each agent's git section with: "Follow root CLAUDE.md Git Protocol; my pathspec: `AGENTS/<NAME>/`" + agent-specific exceptions only (TERRY/WALTER/YEYOU keep their exception lines) | Low-medium — needs the one root improvement in R2 first, else agents lose the recipes |
| S3 | **Manual boot-read sequences superseded by boot.py** (17/33 agents have boot.py; several still carry the pre-script manual step list alongside) | e.g. price-check/staleness/predictions-due steps listed manually AND wired in the script | Fails (b): mechanized. Keep the invocation line + `--quick` fallback; strike the duplicated manual steps. Do NOT force boot.py on the 16 non-adopters (DARWIN lesson — mechanize on need) | Low |
| S4 | **Repeated ⚠️ FILE > VERBAL blocks** (×22 files, often 2+ per file) | 2 near-identical blocks in ZHAO alone | One statement is a behavior-gate; the second+ is weak-model nagging. Keep one per file (or move to root) | Trivial |
| S5 | **Dead-platform vestiges: live-instruction HERMES/OpenClaw refs** (HERMES in 23 CLAUDE.md; OpenClaw in 4 harness docs) | Split: correct deprecation-*notes* (AEOLUS — keep) vs live *instructions* ("delivered by HERMES twice daily" — ZHAO, OTTO OUTBOX; GLM/OpenClaw runtime — YEYOU, TERRY, WALTER, ORACLE) | Platform cut 6/26. Currently lazy-swept one agent at a time — 11 days on, 23 files still carry it. **One classify-and-strike sweep beats 23 lazy sweeps** | Low — grep-classify first; keep deprecation-notes |
| S6 | **DAEDALUS's own SPAWN step 4** ("skim EVOLUTION.md" every boot) | self-dogfood | Fails (a) marginally: EVOLUTION is my changelog — needed when the *standard* is in question, not every spawn. Demote to conditional read | Trivial |

**Not struck (tested and kept):** anti-hallucination gates (root Critical Rule 3 — model-independent, incident-born); TERRY's numbered-API rules 6/7 (stable API); evidence-grade tag systems (behavior-gates); the two-guard AUTHORITY model; per-agent inbox "don't process on normal spawns" (behavior-gate; messaging-overhaul lane owns any redesign — root Data Hygiene explicitly out-of-scopes it here).

## 2. Rule 5 — REWRITE-NOT-PATCH LIST

| # | Surface | Rot evidence | Prescription | Owner |
|---|---|---|---|---|
| R1 | **OTTO CLAUDE.md (539 ln, 33 steps — fleet's largest)** | 3-way version-stamp drift (v2.5 header / v2.7 footer / unversioned 7/4 edit), dead SIGNALS.md instruction, push-policy contradiction, MAINTENANCE.md holding the real version history | Past patching: apply the **WALTER split** — lean executable checklist + `design/`-style rationale doc + cross-ref guard. Its machinery is exemplar; only the *doc* is rotted | OTTO (card already routed 7/7) |
| R2 | **Root CLAUDE.md Git Protocol section (~90 dense lines)** | Grown by caveat-accretion (incident cites, rollout parentheticals, nested numbered sub-protocols); it is the most-restated-downstream text in the fleet — its density is WHY agents restate locally | Rewrite lean: numbered recipes (commit / push / pull / abort paths), incident-history + rationale → `docs/` or auto-memory refs. **Precondition for S2.** Will+PROME-owned — recommend only | Will/PROME |
| R3 | **STATUS lead-paragraph accretion (fleet-wide pattern, incl. DAEDALUS's own)** | OTTO's 3-generation boot-pointer stack w/ a Jun-9 mega-paragraph; DAEDALUS STATUS line-3 now spans 3 sessions of prepends | Rule 5 applied to state files: **STATUS leads get rewritten each session, not prepended** — PROME's SCRATCH.md "full rewrite" + CLOSEOUT tiering is the in-fleet model. Blueprint note candidate (§8) | each agent; blueprint next pass |
| R4 | **MATURITY_MAP.md (DAEDALUS's own)** | Frozen 6/27 first-scan snapshot; distribution table now wrong (lists as L2 six agents since firmed L4); readable-map role superseded by FLEET_MAP+profiles | Two-state it: FROZEN banner pointing at FLEET_MAP.tsv (applied this session — own file, dogfoods the audit) | DAEDALUS ✅ |
| R5 | *(borderline, watch)* ZHAO CLAUDE.md | 6-instance rot cluster — but fix-cluster D1-D6 already routed; below rewrite threshold | Patch-lane; escalate to rewrite only if next session surfaces more | ZHAO |

**New pattern candidate (n=2, watch):** *reactivation rot* — a reactivated agent's rehab fixes STATE files first (STATUS/workbook) and boot-loaded DURABLE docs last (ZHAO's CLAUDE carried the old regime's numbers into its new session; OTTO's punchlist policed staleness while itself stale). Add "durable-doc layer check" to any future reactivation scan (OZK/FERT candidates).

## 3. Encode vs convention vs kill — roadmap dispositions

| # | Item | Disposition | Audit rationale |
|---|---|---|---|
| 1 | calibration skill | **ENCODE (skill)** — co-signed with new evidence | The one convention that's high-value + ~15-agent-duplicated + drift-prone. **Fresh proof from this week's reads:** OTTO's calibration scoreboard diverged between its two homes (ARCHIVE stale at 5/5 vs THESIS fresh 5/7) — exactly the drift a versioned single procedure prevents. Prototype on ONE agent per PROME sequencing |
| 2 | EDGAR MCP | **KILL** (stay demoted) | Concur; audit adds nothing new. Single-machine tax + scripted coverage |
| 3 | SessionStart hook | **DONE — validated live** | Fired correctly in THIS session twice (env_doctor FAIL, ahead/dirty flags, incl. across a resume). Encode-confirmed |
| 4 | signal-routing skill | **WALTER-owned; recommend-don't-build** | Concur. WALTER already self-applying the §5 borrowables |
| 5 | nexus-brief skill | **CONVENTION** | Locked template + NEXUS schema-ownership already enforce it; a skill = second home for the schema (PAT-006 two-truths risk). Live evidence the convention works: ZHAO built a fleet-best brief from the template cold on 7/4. Revisit only if Production Reviews show brief drift |
| 6 | FRED MCP | **KILL** (stay demoted) | Concur |
| 7 | red-review skill | **CONVENTION — do not encode** (RED co-sign required anyway) | The standing-adversary'S value IS the live counterparty; a self-serve checkbox version recreates the failure it guards against (PAT-028 logic). If RED wants a lightweight intake form, that's RED's call |
| 8 | repo-git-protocol skill | **NOT a skill — root REWRITE + restatement strikes** | The problem is duplication drift (25 restating files, 2 live contradictions), not invocability. A skill = a THIRD home. Fix = R2 rewrite + S2 strikes + (later, gated) the deferred cite-not-restate scanner check with a zero-FP baseline |
| 9 | market-data MCP | **KILL** | Concur |
| 10 | walter-skill retirement | **DONE 7/6** | Closed |
| 11 | PreCompact write-back hook | **ENCODE (hook)** — strongest yes after #1 | Compensates for a *harness* limitation (compaction), not model weakness — Rule 8 doesn't strike it and model upgrades won't obsolete it. Observed incident class; #3's flag-not-force shape proven |

**Audit-surfaced additions (new, small):** (A) ZHAO's boot.py **release-watch pattern** ("should a newer print exist by now?") → blueprint §8 candidate for every scheduled-release domain (TIC/NFP/PMI/earnings). (B) **PAT-039 content-date fallback** for `ledger_staleness.py` when git times are degenerate (cloud clones) — gated, shared-script. (C) Rule-2 role-separation and Rule-3 contract-first are *already fleet practice* (RED standing evaluator; JOINT_PROPOSAL/LIAISON) — no build needed; noted so nobody builds them again.

## 4. Org recommendation (the Will question) — **extend DAEDALUS; do NOT revive DARWIN; no new agent**

**How much recurring work did the audit actually surface?** Modest and episodic:
- **One-shot:** the S1–S5 strike sweep (one batched changelist, mostly mechanical), R1/R2 rewrites (owner-lane), 2 builds (#1 skill, #11 hook — PROME-lane).
- **Recurring:** re-running THIS audit on model upgrades + ~quarterly. That's 2–4 runs/year of a pass that took one session — **not a standing agent's worth of work.** Rule 9 answered: the bottleneck the audit found is *deletion discipline*, not a missing owner.

**Why DAEDALUS:** the audit's machinery IS my existing machinery — the sweep registry (`sweeps/`, cadence-checked at boot), the conformance scanner, PAT-031/033/035 enforcement, the gated-batch apply model. A harness audit is structurally identical to my staleness sweep: detect autonomously, disposition gated. **Why not DARWIN:** reviving a dormant identity to own 2–4 episodic runs/year recreates PAT-001/002 (an open-ended "watch the harness landscape" mandate with no daily work — the exact DARWIN failure), and WALTER's Rule-8-against-itself point stands: don't grow the agent count to serve a pruning discipline.

**Proposed shape (NOT institutionalized this pass, per the packet):** `sweeps/` entry #3 — **Harness Audit**, trigger = model upgrade OR 90d, detection read-only, strike-lists batched for Will approval. If approved, I register it next session; the strike sweep S1–S5 can run as its first execution.

---
*Deliverable complete. Nothing above is applied except R4 (MATURITY_MAP freeze banner — DAEDALUS's own file). Outbox pointer routed to PROME. Disposition write-back on Will/PROME review → this file's header + STATUS (PAT-032).*
