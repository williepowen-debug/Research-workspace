# Utility-Cohort Firming Pass — read-only assessment (WALTER / RED / TERRY / NEXUS / YEYOU)

**By:** DAEDALUS · **Date:** 2026-07-03 · **Status:** ✅ ASSESSMENT COMPLETE (read-only, nothing touched) · **Apply-proposals: 🟡 HELD for Will per-item review.**
**Method:** 5 parallel read-only assessors, each graded its agent vs the live `BLUEPRINTS/utility-agent.md` + `SPEC.md §5` (the firm-next7 pattern). Graded CONTENT-not-filename (PAT-030), floor-not-ceiling (PAT-015), gaps tagged missing-HANDLE vs missing-SUBSTANCE (PAT-022). ORACLE was already firmed 6/28-29 (L4) → this completes the utility cohort.

---

## Maturity headline — the mechanical map under-rated the cohort again (PAT-024 confirms fleet-wide)

| Agent | Was (map) | Firmed | Δ | CONTRACT block | Held below next level by |
|---|---|---|---|---|---|
| **WALTER** | L3 (M) | **L4 (H)** | +1 conf | absent (scattered) | YEYOU-clean unverified · STATUS spine staleness (self-flagged) · consume-loop Phase-2-partial |
| **RED** | L3 (M) | **L4 (H)** | +1 conf | absent (scattered) | 4 hygiene/label items: CONTRACT+BOTTOM-LINE handles, FLOW.tsv silent-rot, SCRATCH push-drift |
| **NEXUS** | L2 (L) | **L4 (H, prov)** | **+2 levels** | absent (scattered) | CONTRACT+BOTTOM-LINE handles, PAT-031 boot gaps, STATUS not current |
| **TERRY** | L3 (M) | **L3 (H, prov-L4)** | +1 conf | absent (scattered) | CONTRACT+BOTTOM-LINE handles, PAT-031 partial break; card-product un-exercised (env, PAT-028) |
| **YEYOU** | L2 (M) | **L2 (H, firmed)** | +1 conf | absent (scattered) | ledger never accrued (empty REVIEW_LOG) blocks L2→L3 *verification* — "hasn't launched," not a defect |

**Net:** utility cohort is now **4×L4 (ORACLE, WALTER, RED, NEXUS-prov) + TERRY L3-prov-L4 + YEYOU L2-firmed.** NEXUS was under-rated **two levels** (the firm-next7 pattern repeats). This is a **mislabel correction, not a capability gain** — the map is a hygiene input, never the scoreboard ([[project_daedalus_maturity_map_hygiene_input]]).

---

## THE convergent finding — a CONTRACT-block sweep (parallel to the market Independence sweep)

**All 5 agents (and ORACLE before them) LACK a labeled `CONTRACT` block** — the utility blueprint's *defining* handle (§2 THE SPINE: PRODUCES / CONSUMED BY / PROOF OF CONSUMPTION). In every case the three elements are **fully present in substance but scattered** across CLAUDE.md/STATUS. This is **enforcement, not standard**: the cohort predates the 2026-06-28 utility blueprint. Exactly the market cohort's Independence/ACTION situation → **one consolidated CONTRACT-block sweep, not 5 per-agent items** (PAT-011 / [[finding_fleet_selfreport_convergence]]). ORACLE's block (applied 7/3, BATCH_03) is the worked template.

Each agent's PROOF line carries a **PAT-028 ceiling NOTE** where consumption is un-instrumentable (RED's steelman shifting a decision; TERRY's card un-fired; NEXUS/YEYOU's consumer-side non-telemetry) — qualitative proof counts; do NOT grade down.

---

## Consolidated apply-proposals (🟡 ALL HELD for Will per-item review)

### Sweep A — labeled CONTRACT block (encode-existing; 5 agents)
WALTER · RED · TERRY · NEXUS · YEYOU. Each: assemble the scattered PRODUCES/CONSUMED-BY/PROOF into the 3-line block (ORACLE 7/3 = template), with the PAT-028 ceiling NOTE where proof is un-instrumentable. **Live agents (WALTER active) → task-packet; idle → direct on approval.**

### Sweep B — labeled BOTTOM LINE (encode-existing; 4 agents)
WALTER · RED · TERRY · NEXUS lack a *labeled* §8 BOTTOM LINE (all have a de-facto one — RED's footer, WALTER's "Overall:" line, TERRY's header synthesis, NEXUS's header block). Label + place at tail. **YEYOU already has one ✓.**

### PAT-031 cwd-proof fixes (2 agents — real latent breaks the scanner SUPPRESSES)
- **TERRY** — canonical boot card is wrapped ✓, but BOOT steps 11-13 (snapshot/risk_calc/chain_parse) + README invocations are **bare `AGENTS/TERRY/scripts/…`** → break from TERRY's own launch cwd. → task-packet.
- **NEXUS** — boot step 7 + closeout step 16 use bare root-relative `AGENTS/NEXUS/…` git/mv paths; **zero `rev-parse`** in CLAUDE.md → the idiom-unaware case; would trip the scanner if not for... it has no rev-parse so it SHOULD flag. *(Re-check: NEXUS is genuinely idiom-unaware → the scanner's agent-level heuristic SHOULD catch it. Verify at apply.)* → direct on approval (NEXUS idle-check) or task-packet.
- **Note:** TERRY is the *partial-idiom* case (has rev-parse on the boot card, bare elsewhere) → the scanner's agent-level heuristic **suppresses** it (idiom_aware=True). The firming READ caught it — live evidence for PROME flag-2's "fail-loud-at-boot + human-read is the backstop." (Banked as a PATTERN.)

### Stale/drift routing (through-owner; the TERRY items you flagged + more)
- **TERRY (3):** (a) CLAUDE.md L5 "Spawn-on-demand in OpenClaw" (cut 6/26); (b) L161 "Push is Will-coordinated" (contradicts root canon — TERRY is the *live self-sweep* exception); (c) **NEW** CLOSEOUT.md L67 same stale push model (must fix WITH (b) or they re-diverge). *(Behavior already matches canon; only the written policy is stale.)*
- **YEYOU (stalest of cohort):** CLAUDE.md:4 "Runtime: GLM (Z.ai) on the VM — persistent" + "always-on" claims (OpenClaw-era, contradict manual/branch); CLOSEOUT.md:5 "OpenClaw + Claude Code"; dangling `HANDOFF.md` (doesn't exist, "cross-runtime" vestige); "HERMES delivers" (dangling); "Codex" reviewer entity (verify vs roster). *(Manual/branch → apply when Will next spins it up, or task-packet.)*
- **RED:** OUTBOX.md:3 HERMES vestige; SCRATCH.md push-canon drift (defer model vs CLAUDE canon); **FLOW.tsv silent-rot ~3mo (L5 blocker)** → FROZEN banner or refresh (RED's data-liveness call).
- **WALTER:** STATUS spine anchor stale (NETWORK AWARENESS block "2026-06-22" under a 6/28 lead) — self-flagged "trim owed"; OpenClaw mentions are correct tombstones (NOT stale).
- **NEXUS:** minor — OpenClaw ref in a historical dated audit artifact; BRIEFS_MAP self-flagged internal drift; STATUS not current (6/27).

### DAEDALUS-lane (my file — correctness) — ✅ APPLIED this pass
- **`utility-agent.md` NEXUS_BRIEF naming error:** the §-role table lists NEXUS PRODUCES = "NEXUS_BRIEF," but the per-agent `NEXUS_BRIEF.md` files are **INPUTS to** NEXUS; NEXUS **consumes** ~12 briefs and **produces the synthesis** + **owns the brief schema/template.** Corrected in the blueprint so the CONTRACT sweep doesn't encode a wrong PRODUCES for NEXUS.

---

## DO-NOT-TOUCH highlights (comprehension — full detail feeds the fast-follow profiles)
- **RED** legitimately owns KB/VX/FLOW as *adversarial-flavored* schema (VX = counter-evidence vectors + bull/bear weights + Flip_If) — NOT forced market machinery; do NOT DARWIN-strip. `registry/FALSIFICATION_TRIGGERS.tsv` is WALTER's auto-fire surface (RED writes `docket/WATCHLINES.tsv` instead).
- **WALTER** commits OUTSIDE its own dir BY DESIGN (BOARD at repo root; create-only `inbox/{recipient}/WALTER/`) — the ratified architectural/auto-push exception; create-only/append-only is what keeps it Utility not Meta. `delivery_log.written_state` records write-time state, doesn't advance (git-derived doctor check is truth).
- **NEXUS** uses `LAST_COMPLETION.md` in place of SCRATCH (documented divergence); its convergence matrix + PREDICTIONS_MONITOR are its *core output* + calibration loop, NOT forced market constructs (do not DARWIN-strip); owns `templates/` + cross-dir NEXUS_BRIEF authorship by design.
- **TERRY** RISK_RULES #6/#7 AND root Critical-Rules #4/#5/#6 are BOTH stable numbered APIs (fire cards cite by number — do NOT renumber either); dual-surface (spawn + Desk Mode) by design; `inbox/WILL/` gitignored by design; scaffold-only trade ledgers are correct (no trigger fired).
- **YEYOU** manual/branch runtime (low cadence, short STATUS, sparse ledger CORRECT); flag-never-fix read-only identity; auto-push EXCEPTION (Will-coordinated — canonical, do NOT "fix"); escalation budget + two-reviewer funnel intentional.

---

## Next steps
1. **Will per-item review** of the apply-proposals above (Sweep A CONTRACT / Sweep B BOTTOM LINE / PAT-031 TERRY+NEXUS / stale-drift routing). On approval: idle-check + direct-edit the idle agents, task-packet the live ones (WALTER active; TERRY/RED/NEXUS/YEYOU per idle-check at apply-time).
2. **Fast-follow (DAEDALUS-lane):** formal `profiles/{WALTER,RED,TERRY,NEXUS,YEYOU}.md` + `upgrades/{…}_CARD.md` — this doc holds the comprehension in the interim (mirrors firm-next7: grades first, profiles/cards as the fast-follow).
3. FLEET_MAP rows re-scored this pass; STATUS/EVOLUTION/PATTERNS updated.
