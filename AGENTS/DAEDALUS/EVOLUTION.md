# EVOLUTION — Architecture Changelog & Roadmap

**Owner:** DAEDALUS · The standard's history (what changed in *how we build agents*, and why) + where it's heading.
Newest first. Keep entries terse; archive build minutiae to `FLEET_MAP.tsv`.

---

## Changelog

### 2026-07-03 — cwd-proof boot invocations encoded (PAT-031) + baked into all 3 blueprints + scanner conformance check; template-debt retired
- **What:** Actioned PROME's 7/1 `cwd-proof-boot-invocation` packet — 3 asks, all own-file, all done. **(1)** PAT-031: every *runnable* boot-doc invocation must be cwd-proof (`python3 "$(git rev-parse --show-toplevel)/<path>"` or `(cd "$(git rev-parse …)[/<dir>]" && <cmd>)`), never a bare root-/own-dir-relative path — the root cause of BRENT's Jul-1 `rc=2` boot failure (misread as "script missing repo-wide"). **(2)** Baked the idiom into `market-agent.md` §8 (hygiene) / `utility-agent.md` §5 (disciplines) / `meta-agent.md` SPAWN PROTOCOL → post-AEOLUS builds inherit it. **(3)** Added an **agent-level** conformance check to `maturity_scan.py` (bare runnable root-relative invocation + zero `rev-parse` idiom-awareness).
- **Validated the check, not just wrote it:** exercised the helper — it **fires** on a synthetic violation and stays silent on cwd-proofed + idiom-aware-reference docs; a full-fleet run shows **0 false-positives.** ORACLE (the only agent with bare `python3 scripts/…` lines) is correctly SUPPRESSED because its 7/1 section cwd-note added `rev-parse` awareness — which doubles as evidence the 7/1 sweep landed. **Line-level strictness DEFERRED** (FP-prone on intentional reference-command docs, exactly as PROME's addendum flagged) — ship only with a validated zero-FP baseline.
- **Standard delta / debt RETIRED:** discovered Will **deleted `AGENTS/templates/`** (incl `CLAUDE_TEMPLATE.md`, 333ln) on 6/30 (`58c30516`) → the long-standing "bring `CLAUDE_TEMPLATE.md` under BLUEPRINTS + drop HERMES" roadmap/debt item is **MOOT**; the BLUEPRINTS variants are now the *sole* standard. Corrected the now-stale "supersedes template / redirect tracked" refs in the market + utility blueprints. Template half of PROME's ask (2) collapsed to the blueprint edits alone.
- **Surfaced (not fixed):** PROME-addendum conformance items — **TERRY** CLAUDE.md staleness ×2 (OpenClaw vestige line ~5 + push-canon contradiction line ~161; owner-fix, TERRY is a live self-sweep agent → fold into the utility firming pass) + a **root-canon cite-not-restate** scanner candidate (deferred with the line-level cwd check).
- **Next:** utility-cohort firming (DEFERRED by Will); fleet-wide TRADE.md staleness-sweep proposal (PAT-025).

### 2026-06-29 (later) — new instrument: the *handle sweep* (enforce existing blueprint handles fleet-wide) + conformance notes
- **What:** Consolidated the two recurring market-cohort handle gaps the firm7 cards surfaced — **§2 Independence column** + **§5 If-Falsified ACTION column** — into one fleet-wide **enforcement sweep** (`upgrades/HANDLE_SWEEP_independence-action.md`). The insight was only visible across all 7 cards at once: **both handles are ALREADY required by `market-agent.md` §2/§5** — so the gap is *enforcement* (agents predate the 6/27 standard), not the standard. [[finding_fleet_selfreport_convergence]] / PAT-011.
- **New review instrument:** the **handle sweep** — one approval applies an existing required handle across all in-scope agents, instead of N per-agent batch line-items. Directly answers the "BATCH_02 is aging / DAEDALUS out-produces review" lesson: fewer, consolidated review units. Scattered Independence/ACTION items in BATCH_01(done)/BATCH_02 now defer to the sweep; BATCH_02's non-handle items untouched.
- **Standard delta:** added a one-line "commonly-missing + N/A-exception" conformance note to `market-agent.md` §2 + §5 (check these two handles first when firming; N/A for single-channel [§2] and no-book/utility [§5] agents).
- **Routed (Will-approved):** BRENT KEY THRESHOLDS **line 168** correctness fix → BRENT (via PROME), pulled from candidate BATCH_03 — a boot-loaded durable rule ("<$75 = thesis break") contradicting live v5.0 ("sub-$75 = structural decoupling, confirming"). Correctness, routed immediately not batched.
- **Next:** utility-cohort firming (now with PAT-030 in hand); apply the sweep on approval; remaining candidate BATCH_03 = the non-handle net-new items only.

### 2026-06-29 — firm-next7 comprehension persisted: 7 profiles + 7 cards; re-read obsoleted an in-flight batch item (PAT-029)
- **What:** Built the durable `profiles/{REGINALD,CARL,LABOR,BOND,HAWK,BRENT,ORACLE}.md` + `upgrades/{…}_CARD.md` for the firm-next7 cohort (workflow `firm7-profiles-cards`, 14 agents = 7 comprehend → 7 grade, ~1.3M tok). Closes the BATCH_02 fast-follow. The 6 market agents graded vs `market-agent.md`, ORACLE vs the now-live `utility-agent.md`. FLEET_MAP rows re-scored 6/29.
- **The re-read was a re-verification, not just documentation (PAT-029):** rebuilding a profile from *live* files caught drift that post-dated the 6/28 grade — and **obsoleted an in-flight gated batch item.** **BRENT** migrated TRADE.md to a live boot/closeout-wired surface 6/29 → **BATCH_02 item 7 (its FROZEN-banner) is now OBSOLETE** (freezing a live surface would be *wrong*); struck in the batch doc + flagged to PROME. **REGINALD's** "KB/FLOW need an in-file FROZEN banner" was wrong — PROME's 6/27 hygiene pass already froze the 4 dead feeds; KB/FLOW are live-consumer ledgers → **refresh-not-freeze**. **HAWK's** STATUS hasn't absorbed REMARK_20260628 (6/28 kinetic re-escalation, HAW-14 kinetic-floor breached) — domain-lane, routed to owner.
- **Repurposed market-surface ≠ DARWIN debt (PAT-030):** ORACLE (utility) carries a convergence-matrix + TRADE.md, but both are *repurposed, filled, consumed* utility surfaces → EQUIVALENT, not DARWIN dead-scaffold. The card graded them N/A-by-design, not as violations. A discriminator for the upcoming utility-cohort firming (grade the content, not the filename).
- **Net-new handles catalogued for a candidate BATCH_03** (in the cards, not yet routed): REGINALD §5 ACTION + TRADE.md banner/refresh · CARL/LABOR/BRENT §2 Independence · BOND/LABOR §5 ACTION · HAWK 2nd dangling ref · BRENT CLAUDE threshold-drift line 168 · ORACLE §2 CONTRACT block.
- **Standard direction:** the comprehend→grade pipeline is now the proven heavy-agent profiling unit (Mode-A, PAT-017); pair it with a live re-read at apply-time so gated batches don't go stale before approval.

### 2026-06-28 — utility-agent blueprint built + ACTIVATED + YEYOU resolved → utility; **variant set complete**
- **What:** Authored `BLUEPRINTS/utility-agent.md` (🟢 ACTIVE — Will + PROME approved same day). **Led by the OUTPUT-CONSUMPTION CONTRACT** (produces / consumed-by / proof-of-consumption) per PROME framing — uniform coordination visibility across WALTER/NEXUS/RED/TERRY/ORACLE/YEYOU is the payoff; accurate grading is the byproduct. Thin shared floor + role-specific ceiling, with the **DARWIN lesson applied to its own rollout** (it grades, it does not mandate machinery to hit an L-number).
- **Completes the variant set:** market + meta + **utility** — every class now has a standard. Closes the long-open roadmap item.
- **Class call (PROME #3):** resolved YEYOU's double-bucket → **UTILITY** — read-only, flag-never-fix, produces consumed review verdicts (the per-push analogue of RED). New **PAT-027**: the meta-vs-utility discriminator is *mutation-authority*, not subject-matter. Fixed the stray YEYOU example in `meta-agent.md`.
- **Deflation (PROME #4):** the "2×L4 → ≥9×L4" firming result is a **mislabel correction, not a capability gain** — the agents are exactly as capable as before; the map was wrong. The win is (a) not wasting effort firming already-mature agents and (b) consumable outputs — not the L-count. The map stays a hygiene input, never the scoreboard.
- **PROME refinement baked in at activation (PAT-028):** the proof-of-consumption L4 gate must not recreate the false-negative it exists to prevent — informal/un-instrumentable consumption (RED's steelman, TERRY's construction) is a structural-ceiling NOTE, not fix-it debt; qualitative proof counts. The anti-DARWIN principle applied to the blueprint's own gate.
- **Next:** firm the utility cohort (NEXUS/RED/TERRY/YEYOU) against the live standard; bring `templates/CLAUDE_TEMPLATE.md` fully under BLUEPRINTS ownership (the redirect + drop stale HERMES refs). (Both ahead of the fleet-wide TRADE.md staleness sweep, per PROME.)

### 2026-06-28 — Firming pass begins: SHADE / BROCK / CREED read-verified (first false-negative caught)
- **What:** First judgment-read firming batch — comprehend → grade vs `market-agent.md` → adversarial-verify, 3 agents (workflow `grade-shade-brock-creed`, 6 agents / 624k tok). Persisted `profiles/{SHADE,BROCK,CREED}.md` + `upgrades/{…}_CARD.md` + 3 re-scored FLEET_MAP rows.
- **Maturity-map correction:** **BROCK L3 → L4** — the 6/27 mechanical scan carried a false-negative ("No TRADE.md caps at L3"; `trade/TRADE.md` exists, 275 ln, feeds a live position + signals flowing). SHADE L2 / CREED L1 *confirmed* but firmed Conf L→H / L→M with corrected notes (SHADE commit-count 13→28; CREED "thin KB" → frozen-legacy pull-forward).
- **New patterns:** PAT-020 (scanner **path-blindness** — harden `maturity_scan.py` to search recursively, or treat L3+ mechanical grades as provisional); PAT-021 (frozen-legacy KB ≠ thin — it's a pull-forward, not a build); PAT-022 (grade gaps as **missing-handle vs missing-substance** — predicts the climb cost).
- **Standard direction:** the firming pass is now the method for converting Conf-L rows to verified; the scanner needs the recursive-search fix *before* the next re-scan or it will keep manufacturing false-negatives.

### 2026-06-28 — Phase 3/4: first REAL build executed — AEOLUS (climate → economy)
- **What:** Built + wired AEOLUS, the fleet's macro climate→economy agent — DAEDALUS's first non-dry-run build (the build pipeline's maiden real use). Scaffolded `AGENTS/AEOLUS/` (CLAUDE.md, STATUS, THESIS, TRADE, full workbook) from `BLUEPRINTS/market-agent.md`, then wired into `PROME/ROSTER.md`, root `CLAUDE.md`, `_INDEX.md`, `_ENERGY.md`, transmission chain (`AEOLUS → {BRENT, CORAL, MARCO}`), + CORAL boundary task-packet.
- **Design (Will-decided):** channels-first (insurance / ag-food / energy-demand core; property + supply-chain tier-2), tiered horizon (live weather over structural backdrop), CORAL keeps Florida.
- **New patterns:** PAT-018 (bake the anti-drift guard into structure — empty-channel-is-failure — the operationalized DARWIN antidote); PAT-019 (new agent has no commit history → annotate ROSTER honestly, don't fake a cadence).
- **Self-level:** L4 trigger met — first build executed clean. Spec: `builds/AEOLUS_SPEC.md`.
- **Same-day amendment:** Will promoted both Tier-2 channels (C4 property, C5 supply-chain) to core → AEOLUS runs **5 core channels** (C1–C5). Built to full parity (transmission tables, thresholds, exit triad, matrix). Tradeoff noted: 5 channels = more live reads to keep current (PAT-018 upkeep), accepted for coverage of the climate→credit chain (C4) + tradeable freight events (C5).
- **Next:** AEOLUS's first live data pass (its own job); utility-agent blueprint; bring `templates/CLAUDE_TEMPLATE.md` under BLUEPRINTS ownership (it still references deprecated HERMES).

### 2026-06-27 — Phase 3 (partial): market-agent gold-standard blueprint composed
- **What:** Assembled `BLUEPRINTS/market-agent.md` best-of-breed from the harvest — each section sourced to the agent that does it best (REGINALD/LIQUID/OTTO structure, BOND/NEXUS scoring, HENRY/LIQUID thresholds, LIQUID/HENRY/BRENT exit, OTTO/CARL/VIOLET predictions, MARCO routing).
- **Design call (not harvested):** reconciled BOND-vs-HENRY threshold conflict via durable-rule-vs-live-value split (§3) — flagged for Will veto.
- **Held firm:** the universal 5-pt convergence scale is non-negotiable (cross-agent backbone); HENRY's loss of it is the cautionary tale.
- **Next:** utility-agent blueprint (WALTER/NEXUS/RED/YEYOU sources); then bring `templates/CLAUDE_TEMPLATE.md` under BLUEPRINTS ownership.

### 2026-06-27 — Best-practices harvest (full fleet structural survey)
- **What:** Surveyed 23 agents' STATUS structures (5 parallel reads) for best-of-breed patterns per dimension → `BLUEPRINTS/BEST_PRACTICES.md`.
- **Key finding:** the fleet has collectively out-designed the original template; **no single agent is the whole standard** (PAT-011). Best-of-breed is scattered: LIQUID (exit/migration), OTTO (predictions/transmission stages), BOND (comparable scoring), MARCO (routing/mechanism-split), NEXUS (synthesis discipline), REGINALD (cluster grid).
- **Corrected an earlier lean:** "promote HENRY's patterns up" was right for its INVALIDATION TRIAD + banded-routing, but **HENRY is weak on cross-agent-comparable scoring** — backfill BOND's transparent composite instead (PAT-012). Vindicated Will's instinct not to crown HENRY off n=1.
- **Consequence for Phase 3:** blueprints are ASSEMBLED best-of-breed, not cloned from one exemplar.

### 2026-06-27 — Phase 2: maturity engine + first full fleet scan
- **What:** Built `scripts/maturity_scan.py` (objective L0–L2 floor + structural flags) and ran the first full scan of 26 agents → `FLEET_MAP.tsv` + readable `MATURITY_MAP.md`.
- **Findings:** REGINALD L4 (exemplar); 8×L3; 12×L2; HERMES retire-candidate; DEWEY L0-by-design. Systemic: **14 agents missing the required BOTTOM LINE** (batch-fixable); 5 with session-count-less exit rules; SAM over line cap.
- **Self-dogfood:** the engine caught two bugs in its own scoring logic (PAT-007 missing-section≠skeleton; PAT-008 class-aware records) before they shipped — building the scorer hardened the ladder.
- **Open standard decision for Will:** enforce template section-titling vs. accept own-titled equivalents (HENRY case). See `MATURITY_MAP.md`.

### 2026-06-27 — DAEDALUS created; meta-agent class formalized
- **What:** Stood up DAEDALUS (fleet architect) and, from it, extracted the first `meta-agent` blueprint — formally splitting non-market agents off the market template.
- **Why:** The design/structure/maturity/lifecycle layer had no owner (scattered across PROME/FLEET_SCAN/ROSTER/YEYOU). DARWIN had proven that forcing the market template onto a system-facing agent yields dead files.
- **Delta to standard:** new `BLUEPRINTS/meta-agent.md`; per-class maturity ladder defined (`SPEC.md §5`); `templates/CLAUDE_TEMPLATE.md` now understood as the *market* variant, to be brought under `BLUEPRINTS/` ownership.

---

## Roadmap (where the standard should go)

| Priority | Item | Why | Phase |
|---|---|---|---|
| High | Assemble `market-agent` + `utility-agent` blueprints **best-of-breed** from `BEST_PRACTICES.md` (NOT cloned from one agent — sources: REGINALD/LIQUID/OTTO/BOND/MARCO for market; WALTER/NEXUS/RED/YEYOU for utility) | Complete the variant set; give the scorer a standard per class | 3 |
| High | Build the maturity scoring script (objective L0–L2 floor) | Makes the fleet map trustworthy + rerunnable | 2 |
| Med | First full fleet maturity scan → seed `FLEET_MAP.tsv` for all ~20 agents | The deliverable Will most wants | 2 |
| ~~Med~~ | ~~Bring `AGENTS/templates/CLAUDE_TEMPLATE.md` under `BLUEPRINTS/`~~ — ✅ **MOOT** (Will deleted `AGENTS/templates/` 6/30, `58c30516`; BLUEPRINTS are the sole standard) | ~~Stop template/reality drift~~ | ✅ 3 |
| Low | Decide cadence: on-demand vs light weekly map refresh | Avoid staleness without over-running | post-2 |
