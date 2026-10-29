# HOMER profile refresh — Reader 1 of 3 (ARCHITECTURE cluster)

**Date:** 2026-10-28 · **Reader:** DAEDALUS helper (Mode-A fan-out, R1), read-only on all tracked files · **HOMER live?** No (last HOMER commit `454435973` 2026-10-19) · **Repo HEAD at read:** `c6d77fc1f`
**Paths below are relative to `AGENTS/HOMER/` unless prefixed.** Byte figures from `wc -c` on 2026-10-28; % = share of the 32,550 B budget; rotation trigger = 24,412 B (75%); hard cap = 54,250 B.

**Coverage (whole reads, every line):** `CLAUDE.md` 1–277 (3 chunks: 1–90, 91–180, 181–277) · `STATUS.md` 1–164 (1–60, 61–164) · `LESSONS.md` 1–174 (1–80, 81–174) · `OBLIGATIONS_OTHERS.md` 1–36 · `NEXUS_BRIEF.md` 1–101 · `MEMORY.md` 1–28 · `SCRATCH.md` 1–27 · `LAST_COMPLETION.md` 1–30 · old profile `AGENTS/DAEDALUS/profiles/HOMER.md` 1–67 · `_TEMPLATE.md` 1–52. **Header only (lines 1–40, wide lines cut at 600 chars):** `STATUS_COLD.md`, `LESSONS_COLD.md`, `LESSONS_COLD_2.md` (its 11 `## §` headings grepped too). **Spot checks outside the cluster** (named in §9): `thesis/THESIS.md` 1–24 plus a grep, `docket/CATALYSTS.tsv` (an awk enumeration), `inbox/WALTER/*` titles, `board_log.tsv` (grep only), `KB.tsv` header, `PREDICTIONS.tsv` line 1, `FLEET_MAP.tsv` HOMER row, `READ_CAP.md` rule 20, `docs/GIT_WORKTREE_PROCEDURES.md:16-21`.

---

## 1. Identity

| Field | Value | Evidence |
|---|---|---|
| One line, in HOMER's words | "Monitor U.S. housing market stress across the foreclosure pipeline, multifamily delinquency (GSE + CMBS books), mortgage rates/demand, builder distress, inventory/pricing dynamics, and state-level housing fragility (FL/TX/NV/CA priority). Own the asset-market and housing-credit-structure domain — the largest household asset/liability class in the transmission chain." | `CLAUDE.md:7` |
| Domain / class | "U.S. Housing & Mortgage Stress — asset-market + credit-structure"; Market, graded against `market-agent.md` | `CLAUDE.md:9-10` |
| Standing peer edges (not "reports to") | HOMER → CARL (consumer transmission; CARL keeps the K-shape interpretation) · → REGINALD (Path C collateral, "first-class chain edge") · → HENRY (wealth effect). Routine via `NEXUS_BRIEF.md`; acute 🔴 → packet INTO the recipient's `inbox/` | `CLAUDE.md:11` |
| ★-ruled ownerships | Trepp CMBS-MF row + GSE-vs-CMBS divergence + Sun-Belt-MF realization (`CLAUDE.md:26`); mortgage-specific rate surface — PMMS, 10Y-FRM spread, FHA-vs-Conv spread (`CLAUDE.md:29`); builder data owner for CRL-23 (`CLAUDE.md:18`, `:277`) | as cited |
| Header gaps | Still no `Reports to` / `Spawnable by` line (the 8/7 🟡 flag); the charter carries "Standing peer edges (not 'reports to')" instead | `CLAUDE.md:3-11` |
| Runtime as actually operated | The last session (10/19) ran on "independent Will-launched Codex/OpenAI, launch-selected gpt-6.1-sol". It was orchestrated ("HOMER (orch)" commit subjects), and PROME coordinated the push | `SCRATCH.md:3`; git log 10/19 |

### FL boundary vs CORAL, as operated now

| Item | Rule now | Evidence | vs 8/7 profile |
|---|---|---|---|
| Statewide FL figures | "**HOMER PUBLISHES NO STATEWIDE FLORIDA FIGURE. CORAL RULES.**" Standing since 7/17, re-affirmed 8/22 | `CLAUDE.md:35`; mirrored on `STATUS.md:89` | **Stronger.** 8/7 had HOMER citing CORAL's statewide figure. The rule now forbids publishing one |
| FL statewide foreclosure rate | CORAL-canonical, HOMER cites. STATUS carries "H1 FC rate *(CORAL-canonical)* #1: 0.27% … +32.7% YoY" | `CLAUDE.md:35`; `STATUS.md:94` | same |
| FL statewide condo median/inventory | CORAL's. STATUS **withholds** a current read: "current statewide read withheld pending owner reconcile … source address sent to CORAL" (the "publish the ADDRESS" rule, LESSONS §29) | `STATUS.md:93`; `LESSONS.md:94-95` | **CHANGED.** The broken 8.9-vs-8.1 lock is gone. The withhold-and-route mechanism replaced it |
| HOMER-owned inside FL | METRO foreclosure rates (Punta Gorda, Lakeland, Cape Coral, Jacksonville, Ocala) + the **Miami-Dade condo cut** | `CLAUDE.md:35`; `STATUS.md:95` | same |
| FL annual + ratio bands | Owned by HOMER as bands, evaluable once a year (ATTOM year-end, ~January); a monthly/H1 ratio is an OBSERVATION | `CLAUDE.md:96-97,145`; `OBLIGATIONS_OTHERS.md:30` | new since 8/7 (7/31 build, 8/22 basis restriction) |
| Lock re-verification | No cadence. Supersession is caught by the citer's-obligation rule (LESSONS §28) plus routing to the owner | `LESSONS.md:91-92` | the 8/7 open question has a rule but still no mechanism |

---

## 2. File anatomy

**Boot-read set (`CLAUDE.md:191-205`):** STATUS (step 2: "Read `STATUS.md` (dashboard + BOTTOM LINE)"), SCRATCH (step 3: "Read `SCRATCH.md` (last session handoff)"), LESSONS (step 4: "Read `LESSONS.md` (mistake patterns — apply, don't re-learn)"), PREDICTIONS (step 8: "Predictions due-scan: read `thesis/PREDICTIONS.tsv` (HOM-xx) for past-trigger rows"), and the inbox (step 9). The charter is runtime-loaded.

| File / dir | Purpose (HOMER's words) | Bytes | Boot whole-read? | % budget | Flag |
|---|---|---|---|---|---|
| `CLAUDE.md` | "This file — agent instructions" (`:237`); "This file carries rules only" (`:3`) | 38,671 | Harness-injected (not a Read step) | 118.8% | **Exempt under READ_CAP rule 20** (a context-cost surface, not a truncation surface; `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md:32,40`). `read_cap_check` reports "OUT OF PERIMETER … injection UNCONFIRMED". ⚠️ The 10/19 Codex session (`SCRATCH.md:3`) is the case where the injection premise may not hold. Grew from the "trim to 37KB" of 9/29 (`d66ba9ce1`) |
| `STATUS.md` | "Current state dashboard + BOTTOM LINE (hot surface)" (`:238`); "VALUES + BANDS + OBLIGATIONS ONLY" (`STATUS.md:6`) | 22,157 | **YES**, step 2 | **68.1%** | Under the trigger. **628 B under HOMER's own soft target of 22,785 B** (`CLAUDE.md:212`) |
| `SCRATCH.md` | "Ephemeral session handoff — read at boot, rewritten at closeout" (`:239`) | 3,908 | **YES**, step 3 | 12.0% | — |
| `LESSONS.md` | "Mistake patterns + prevention rules (read at boot)" (`:241`); "INDEX over cold registers" (`LESSONS.md:5`) | 23,910 | **YES**, step 4 | **73.5%** | ⚠️ **502 B under the 24,412 B rotation trigger** (`read_cap_check`: "Headroom to the trigger: 502 B"). One more index row will likely cross it |
| `thesis/PREDICTIONS.tsv` *(outside the cluster; size only)* | "HOM-xx prediction ledger" (`:244`) | 36,472 | **YES in effect**, step 8 ("read … for past-trigger rows"). Under READ_CAP rule 16, a predicate over unindexed rows is a WHOLE read | **112.1%** | 🟠 **OVER BUDGET** (but under the 54,250 B hard cap). `read_cap_check` did **not** list it (it found 3 whole-read files) |
| `NEXUS_BRIEF.md` | "Cross-agent sync brief — VIEW / CALIBRATION / SENDING / WAITING-FOR" (`:240`) | 13,447 | Not by HOMER. NEXUS reads it whole (NEXUS:6, per `read_cap_check`); CARL/REGINALD/HENRY read it at their own boot (`CLAUDE.md:11`) | 41.3% | OK. Rotated 9/24 from 109,239 B (`NEXUS_BRIEF.md:7`) |
| `MEMORY.md` | "Durable findings, Will's preferences, do-not-touch notes" (`:242`); "Thin by design" (`MEMORY.md:3`) | 4,278 | **NO.** No boot step names it | 13.1% | ⚠️ The do-not-touch notes live in a file the boot never reads (see §6). Last commit 9/29 |
| `OBLIGATIONS_OTHERS.md` | "OBLIGATIONS OWED BY OTHERS … Nothing here is mine to edit" (`:1-3`) | 5,947 | **NO** ("Not boot-read", `:4`) | 18.3% | Not listed in the charter FILES table |
| `LAST_COMPLETION.md` | "FROZEN 2026-10-15 — historical completion record" (`:1`); "Future completions go to dated PROME delivery memos" (`:5`) | 2,676 | NO | 8.2% | Frozen. Not in the FILES table |
| `STATUS_COLD.md` | "COLD REGISTER (full pre-split dashboard, verbatim) … FROZEN AT THE 2026-09-02 SPLIT" (`:1,10`); crc32 `3627953216` (`:8`) | 150,761 | NO (`:11`) | 463% | Cold; never cite as current. Not in the FILES table |
| `LESSONS_COLD.md` | "COLD REGISTER (full text, verbatim)" §1–43; crc32 `3365692365` (`:1,8`); dated re-trigger **2026-12-02** (`:11`) | 98,868 | NO (`:10`) | 303.7% | Frozen, crc-pinned. Not in the FILES table |
| `LESSONS_COLD_2.md` | "SHARD 2 (post-split entries)" (`:1`), §44–§54 (11 headings) | 13,389 | NO | 41.1% | Append target for new lessons. Not in the FILES table |
| `board_log.tsv` | "WALTER BOARD signal disposition log" (`:243`) | 70,745 (97 lines) | **NO.** Grep-only by rule: "Membership test is a SEARCH, never a read … ⛔ Never rotate" (`:205`) | n/a (COLD-class) | Correct as designed |
| `archive/` (22 files) | "Pre-promotion build artifacts …; charter incident history" (`:258`) | — | NO | — | The description is incomplete: it also holds 9 STATUS bottom-line rotations, the verbatim pre-rotation STATUS and NEXUS, and `CATALYSTS_RESOLVED_2026-09.tsv` |
| `docket/` (1 file) | `CATALYSTS.tsv` "Forward catalyst calendar" (`:246`) | 120,296 | Boot step 5 runs an **awk projection** (cols 1–2 of unresolved rows), not a Read | n/a | 40 unresolved rows on 10/28 |
| `inbox/` (0 top-level · `processed/` 60 · `WALTER/` 29 pending + `WALTER/processed/` 85 = 174 total) | "Inbound signals; `processed/` subdirs hold actioned items" (`:259`) | — | YES, step 9 (both lanes) | — | 🔴 **29 WALTER packets pending, all UNLOGGED in board_log** (§8 R1) |
| `outbox/` (3 top-level + `delivered/` 2 = 5) | "Copies/record only — NOT a delivery channel" (`:260`) | — | NO | — | The 3 top-level files (9/02, 9/14 ×2) are the documented non-deliveries (LESSONS §48) |
| `registry/` (1) | `corrections_receipts.tsv` (named in boot 6a, `:200`) | 1,827 | NO | — | Not in the FILES table |
| `reports/` (19 top-level · 67 recursive, 5 evidence subdirs) | "Session reports, drafts-for-ratification and grading sheets … Not boot-read" (`:256`) | — | NO | — | Anything actionable must also have a docket row (`:256`) |
| `state_vectors/` (4 + `corrected/` 1) | "Historical record of the retired SV channel" (`:257`) | — | NO | — | DO-NOT-TOUCH (§6) |
| `thesis/` (2) | `THESIS.md` (23,077 B): "Not boot-read" (`:245`) · `PREDICTIONS.tsv` (36,472 B) | — | THESIS NO; PREDICTIONS yes in effect (above) | — | — |
| `tools/` (1) | `rent_breadth.py` (5,993 B), the enforcement of the rent-breadth rules (`:114`) | — | NO | — | Not in the FILES table |
| `workbook/` (10 files + `rent_breadth_inputs/`; 12 recursive) | the "record" vs STATUS the "dashboard" (`:202`) | KB_LIVE 71,786 · PRICING 97,910 · MULTIFAMILY 89,022 · PIPELINE 61,902 · BUILDER 58,735 · RATES 53,951 · STATE_HSG 42,491 · KB 30,499 (FROZEN) · SCHEMA 5,320 · RENT_BREADTH_ROSTER 3,650 | Header-line eyeball only (step 7) | — | `RENT_BREADTH_ROSTER.tsv` is not in the FILES table. SCHEMA now covers KB_LIVE/RATES/PRICING (`SCRATCH.md:11`), so the 8/7 🟡 is closed |

**Size flags:** no boot whole-read file is over 32,550 B **except `thesis/PREDICTIONS.tsv` (36,472 B)**, which the fleet checker cannot see. `LESSONS.md` sits 502 B under the trigger. The charter is over 32,550 B but exempt under rule 20.

---

## 3. Boot protocol (`CLAUDE.md:187-207`) and closeout checks (`:209-227`)

| Step | Command / action | What a PASS proves | What it cannot see |
|---|---|---|---|
| B1 (`:189-190`) | `git status` from the root; STOP if any other agent's files are dirty; else `git stash push -- AGENTS/HOMER/` → `git pull --rebase` → `git stash pop` | No foreign dirty paths at that instant; a clean rebase | Restates `docs/GIT_WORKTREE_PROCEDURES.md:16-21`, which agrees today but omits its step 4 (failed stash-pop / drop rule). Cannot see a concurrent session that pushes later |
| B2–B4 (`:191-193`) | Read STATUS, SCRATCH, LESSONS | — (read steps) | LESSONS is an index: rows ending `…` are truncated and require the cold register before acting (`LESSONS.md:5`). **MEMORY.md is not read** |
| B5 (`:194-197`) | `awk -F'\t' 'NR>1 && $1 !~ /^RESOLVED/ {print $1" \| "$2}' docket/CATALYSTS.tsv`, then ask "due / near-due / lapsed?" of each row | Every unresolved local row is printed (40 on 10/28) | `PROME/DOCKET.tsv` rows owed by HOMER; a NEXT date buried in a RESOLVED key (LESSONS §50, `LESSONS.md:161-162`); actions in `reports/` or `OBLIGATIONS_OTHERS.md` that lack a row (`CLAUDE.md:256`) |
| B6 (`:198-199`) | `python3 "$(git rev-parse --show-toplevel)/scripts/ledger_staleness.py" HOMER --quiet` | Workbook ledger vintages are not behind STATUS | Measures ledgers **relative to STATUS**, so a uniformly idle desk reads green (old profile `:58`; LESSONS §18 "`rc=0` from a globbed checker certifies THE GLOB", `LESSONS.md:61-62`). Does not cover the docket or PREDICTIONS. On 10/19 it reported "five source ledgers behind later administrative STATUS writes" (`SCRATCH.md:21`) |
| B6a (`:200`) | `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" HOMER` (rc 0/1/2; WQ-399 receipt fields) | No NAMED correction is unreceipted | Unnamed or un-registered corrections |
| B7 (`:201-203`) | Manual eyeball of the `# LIVE — Last real data refresh: … \| Next:` header on 6 LIVE ledgers; KB.tsv FROZEN | — (no command, cannot fail mechanically) | Whether the `Next:` dates have lapsed, unless the reader computes them |
| B8 (`:204`) | Read `thesis/PREDICTIONS.tsv` for past-trigger rows | — (manual) | A 36,472 B file, over budget (§2). Under a Read-tool runtime, completeness depends on the reader |
| B9 (`:205`) | `inbox/` + `inbox/WALTER/`; membership is a grep: `for f in inbox/WALTER/*.md; do id=$(basename "$f" .md); grep -qF "$id" board_log.tsv \|\| echo "UNLOGGED $id"; done` | Every WALTER packet id appears somewhere in board_log | Logged ≠ actioned (any row matches, including a partial). There is no equivalent test for top-level `inbox/`. **Boot DOES scan `inbox/WALTER/`**, so HOMER is **not** blind to the lane the 10/22 bank review flagged. Re-run read-only 10/28: **29 UNLOGGED** |
| B10–B11 (`:206-207`) | Web check on due catalysts; execute | — | — |
| *Absent from boot* | Runtime/model/tool identification and an explicit load of root + charter (root `CLAUDE.md` §How The System Works); `read_cap_check` (closeout only); MEMORY.md; PROME DOCKET owed-row check | — | — |
| C1/C1b (`:211-218`) | `python3 -c "…getsize('STATUS.md')…"` gives OK / SOFT-BREACH (>22,785) / HARD-BREACH (>32,550). It is "the binding check"; `read_cap_check.py --agent HOMER` is "the fleet floor" | STATUS.md bytes vs the soft and hard tiers | **Measures STATUS only.** LESSONS (502 B headroom) and PREDICTIONS (over budget) are unmeasured at closeout, though `LESSONS.md:6` says "Re-measure at every append" |
| C1c (`:219-221`) | Ruling-residue grep for the superseded term, excluding archive/processed | No undemoted live assertion of a superseded rule | Misses residue phrased differently. Missed `LESSONS.md:113` (§8 R8) |
| C4b (`:225`) | Same awk as B5: "did this session produce this row's output?" plus re-derive conditions built on changed facts | Rows produced this session get closed | — |
| C5 (`:226`) | NEXUS brief folded last, after the final STATUS write ("brief's commit timestamp ≥ the session's last STATUS commit") | Amendment-10 ordering | Verified for 10/19: STATUS, NEXUS and SCRATCH all last committed in `454435973` |
| C6 (`:227`) | Root 1b–1e, explicit-path commit, carve-out ①, `scripts/safe-push.sh` | — | The 10/19 session did not push (PROME coordinated: `SCRATCH.md:3,9-11`) |

---

## 4. Current judgment

| Field | Value | Evidence |
|---|---|---|
| Heading / date | `## BOTTOM LINE` — "**2026-10-19 — documentation maintenance after the domain sweep.**" | `STATUS.md:158-160` |
| Exact judgment line | "**Thesis 0/5 killed, handle 19/25; formal review 11/20.** Source-access and denominator gaps remain explicit. **Will decision required: none.**" | `STATUS.md:162` |
| Thesis statement (v. kill rail re-derived 2026-09-29, criteria FROZEN; handle §8 built 10/15) | "U.S. housing credit stress has moved from ACCUMULATION to CONVERSION … **Current state: 🔴.**" 2 CORE legs (C1 residential conversion, C2 MF realization) + 3 AMPLIFIERS (A1 FHA-bottom inflow, A2 rate, A3 builder) | `thesis/THESIS.md:3,6,12-22` (spot check) |
| Handle | "4 + 4 + 4 + 4 + 3 = 19/25 across 5 legs. Independent roots: 3." C2's upgrade trigger is MET (Trepp 8.04%) but "Not re-scored … §8a re-scores at the formal grade (2026-11-20)" | `THESIS.md:157,190`; `NEXUS_BRIEF.md:27` |
| Conviction | "direction-H (credit conversion; MF realization) · timing-M · level-M (three bands topped out — PMMS, Freddie MF, EHS)" | `NEXUS_BRIEF.md:53` |
| Brief status line | "🔴 New Trepp cohort coverage warning; rental-demand counterweight. Nine sweep additions; thesis counts unchanged." | `NEXUS_BRIEF.md:3` |
| Predictions | HOM-01 CLOSED MISSED (early-kill) 8/31; HOM-02 (FHA SA DQ ≥12.00%, 65%) OPEN, early-kill arm 1 of 2 FIRED, decided by Q3 NDS ~mid-Nov | `STATUS.md:150-151` |
| Last HOMER-authored STATUS update | **2026-10-19**, commit `454435973` "HOMER (orch): close desk session at Will request". No HOMER commit of any kind since | `git log -1 -- AGENTS/HOMER/STATUS.md`; table below |
| Data vintage now | **9 days old.** The newest live values are dated 10/15–10/19 (PMMS 7.40% [10/15] `STATUS.md:60`). WALTER has since delivered PMMS **7.32% [wk 10/22]** (`inbox/WALTER/SIG-W-20261022-029.md` title) and NAR Sept pending **−7.3% MoM** (`SIG-W-20261020-001.md`), neither integrated | §8 R1 |

### Git log since 2026-09-15 on `AGENTS/HOMER/` (103 commits, counted by subject prefix)

| Author class | Count | Commits |
|---|---|---|
| **HOMER-authored** (subject begins "HOMER") | **35** | 9/24 ×3 (`1c9372bf6`, `1578b7f6f`, `72e63a82a`) · 9/29 ×19 (`0f5d28b76` … `9a90512ff`, including thesis + kill rail `74089ab84`, band rulings `6a04e7f59`, charter trim `d66ba9ce1`) · 10/02 ×2 (`10d0d1d79`, `32aab7230`) · 10/15 ×3 (`370ef09a0`, `cb323a73d`, `b9041531b`) · 10/19 ×8 "HOMER (orch)" (`2556731f0`, `7413581cb`, `076910b8f`, `3c7e5fb3a`, `cf1443a51`, `2f9b4117c`, `4c8a8f6c6`, `454435973`) |
| **WALTER packets / routing** | **47** | e.g. `2414245ea`, `9d2492d61`, `0a8557a07`, `22591a862` (10/27); `5901e6a98`, `c3b138f7a` (10/26); `3e0333f30` (10/25); `e339dd997`, `d38416532`, `0d0a91709` (10/22); `4373f4566`, `06a9c5d58`, `70b8667a7` (10/20) |
| **Other desks' packets** | **21** | DAEDALUS ×6 (`f86fd682c`, `fcdcf9254`, `8234db284`, `c8daef7e6`, `536480c90`, `47bd8f55d`) · PROME ×7 (`a35b55065`, `c7305fff0`, `f39972f32`, `79cc5646f`, `be8b72644`, `021e2e792`, `5fbf68060`) · CREED ×3 (`afbf56264`, `9e8a9013e`, `a73880d06`) · DEWEY ×3 (`e6f065cb5`, `9232d7829`, `eb1213301`) · CARL `d9d9eeede` · FLG `3845ea0a6` |

*For 9/29 I give the count, not every hash. After `454435973` (10/19) there are **13 commits on 10/20–10/27, all WALTER, and zero HOMER commits**.*

---

## 5. Where the richness lives (top 5 for a future section-task)

| # | Surface | Why |
|---|---|---|
| 1 | `CLAUDE.md:87-149` Key Thresholds + RUNG CENSUS + band derivations | The desk's strongest dimension. Every level traces to a sourced year or a stated bracket (`:139-143`). Per-rung census (`:107-110`), the binding reporting rule "highest UNCROSSED rung and the distance" (`:112`), two Will-ruled re-arms 9/29 (`:114`, `:119-120`), basis discipline across four ATTOM bases (`:147`), and a self-declared open band defect (`:149`) |
| 2 | `thesis/THESIS.md` (§3 FROZEN kill rail, §4 pre-registered decision rule, §6 defect register, §8 handle, §9 fired-count ledger) | The L3 legs the 8/7 profile said were absent. Grading reads this file. Not boot-read (`CLAUDE.md:245`) |
| 3 | `STATUS.md:18-97` signal dashboard + `:99-101` standing caveats | Live values with as-of, issuer and "say both halves" annotation (e.g. `:38`, `:75`). Three rows have no uncrossed rung (`:21`) |
| 4 | `LESSONS.md` index + `LESSONS_COLD*.md` (54 lessons) | Best-in-fleet Mistake→Rule→Tell corpus (retraction culture). Calibration rows §16/§23/§29/§31/§34/§41 are design-grade material, reusable fleet-wide |
| 5 | `NEXUS_BRIEF.md:60-77` DO-NOT-CITE table + `:51-58` CALIBRATION | A kill-on-sight register of 17 dead claims, each with why and where. It is the cross-agent retraction vehicle (it replaced the old MARQUEE retired-frame role) |

---

## 6. DO-NOT-TOUCH quirks

| # | Quirk | Evidence |
|---|---|---|
| 1 | `workbook/KB.tsv` FROZEN 2026-07-10: never append or renumber (row-ID contract with CARL's KB via `CARL_ID`). New rows → `KB_LIVE.tsv` | `CLAUDE.md:201,248,264`; `MEMORY.md:15`; KB.tsv line 1 banner |
| 2 | `state_vectors/` historical only; `corrected/` is a retrieval hazard. Never file anything there | `CLAUDE.md:231,257`; `MEMORY.md:16` |
| 3 | The struck FL-YoY threshold row + its RETIRED/do-not-evaluate paragraph | `CLAUDE.md:95,122` |
| 4 | **Frozen thesis criteria and the 11/20 formal grade**: "Criteria FROZEN from this commit · Next formal grade: 2026-11-20". C2's handle upgrade is recorded but deliberately **not** re-scored until 11/20. FLEET_MAP: "Do not … alter frozen November 20 scoring cadence" | `THESIS.md:3,190`; `STATUS.md:109,140`; `AGENTS/DAEDALUS/FLEET_MAP.tsv` HOMER row |
| 5 | GSE-MF band letter frozen (WQ-248 C, Will 9/17); an ungraded leg above the top rung is CORRECT | `STATUS.md:43,108` |
| 6 | Re-levelling any pinned rung is a Will-gated RETUNE. Rent roster change = re-spec, Will-gated. Ratio band annual-only | `CLAUDE.md:112,114,145` |
| 7 | `board_log.tsv`: never rotate (grep-class). The AMENDED-SAME-SESSION pair (row 13) stays | `CLAUDE.md:205`; `board_log.tsv:13` |
| 8 | `LESSONS_COLD.md` and `STATUS_COLD.md` are byte-for-byte, crc-pinned (3365692365 / 3627953216). Appending breaks verification, so new lessons go to `LESSONS_COLD_2.md`. LESSONS.md stays an INDEX ("never a Mistake paragraph here") | `LESSONS_COLD.md:6-8`; `STATUS_COLD.md:6-8`; `LESSONS_COLD_2.md:3-4`; `LESSONS.md:6` |
| 9 | PREDICTIONS line-1 preamble carries the CRL-06/23 parent-retain ruling | `PREDICTIONS.tsv:1`; `CLAUDE.md:37` |
| 10 | `Date_Resolved`/`Outcome` stay EMPTY while only one arm of a two-arm kill has fired | `STATUS.md:154` |
| 11 | `LAST_COMPLETION.md` frozen 10/15 under COMPLETION_SPEC; future completions → PROME delivery memos | `LAST_COMPLETION.md:1-5` |
| 12 | Builder price ≠ the discount (incentive masking); the negative-equity version is rejected on HOMER's arithmetic (KB-HOMER-021) | `CLAUDE.md:20-25` |
| 13 | Retired figures stay dead: the $160B/$270B MF wall (replacement is a 13% share), Trepp maturity-adjusted MF (dated kill executed 10/15), Google Trends | `CLAUDE.md:53-54,84`; `STATUS.md:53-54,118-120` |
| 14 | `NEXUS_BRIEF.md` `## VIEW` ceiling is schema-owned and unenforced: "do not cut brief content against it" | `OBLIGATIONS_OTHERS.md:12` |
| 15 | Spread convention: PMMS minus the **Wednesday** nominal 10Y close (survey-matched), never a same-date-label pairing | `STATUS.md:62`; `LESSONS.md:143-144` |
| 16 | The 7/24 HOM-01 grading sheet: never edit post-print (HOM-01 is now closed) | `reports/2026-07-24_HOM-01-grading-sheet.md` exists; old profile `:55` |

---

## 7. Old-profile reconciliation (`profiles/HOMER.md`, 2026-08-07 body)

| Old section | Verdict | Evidence |
|---|---|---|
| §Identity (`:26-27`) | **STILL TRUE, with additions.** National housing asset-market + credit-structure; both MF books; ★ rate surface; feeds CARL/REGINALD/HENRY plus LABOR edge. **CHANGED:** the "CREED couriers the Trepp row" clause is dead. The courier was killed 8/13 and "The PULL obligation is MINE" | `CLAUDE.md:7-11,26,29`; `OBLIGATIONS_OTHERS.md:11` |
| §FL boundary (`:29-30`) | **CHANGED.** The broken lock (8.9 vs 8.1) is GONE. The rule hardened to "HOMER PUBLISHES NO STATEWIDE FLORIDA FIGURE", and statewide condo is now withheld and routed by address | `CLAUDE.md:35`; `STATUS.md:89,93` |
| §File anatomy (`:32-38`) | **CHANGED materially.** CLAUDE 231 → 277 lines / 38,671 B. STATUS rotated to a ~22 KB hot surface (9/14); the MARQUEE section is GONE from STATUS. LESSONS split into index + 2 cold shards (54 lessons, not 7). New: OBLIGATIONS_OTHERS, LAST_COMPLETION, STATUS_COLD, `thesis/THESIS.md`, `tools/`, `registry/`, RENT_BREADTH_ROSTER. SCHEMA gap closed. Outbox now 3 documented non-deliveries, not 0 | §2 above; `STATUS.md:5`; `LESSONS.md:5`; `SCRATCH.md:11` |
| §"Two L3-blocking absences" (`:40-41`) | **GONE (resolved).** THESIS.md + FROZEN kill rail built 9/29; handle built 10/15 (19/25) | `THESIS.md:3,6,157`; `CLAUDE.md:245` |
| §DO-NOT-TOUCH (`:54-55`) | Items 1, 2, 3, 6, 7, 8 **STILL TRUE** (§6 rows 1, 2, 3, 16, 7, 9). Item 4 (MARQUEE retired-frame sentence) **GONE**: no MARQUEE on the hot STATUS; its retraction role passed to NEXUS DO-NOT-CITE. Item 5 (archive banners) **STILL TRUE / unchanged**. **New items** since: §6 rows 4, 5, 6, 8, 10, 11, 13, 15 | grep "marquee" over STATUS/NEXUS/SCRATCH → 0 hits |
| §Owner-lane flags (`:57-58`) | **All 8/7 flags CLOSED or GONE.** NEXUS 94% residue fixed (STATUS:47 95.8%); 5 lapsed `Next:` dates superseded; SCRATCH bands gone; SCHEMA fixed; MF wall re-sourced and retired. **The shape recurs**: lapsed self-registered dates plus unprocessed inbox (now 29, §8 R1) | — |
| §Standing strengths (`:60-61`) | **STILL TRUE, and stronger.** Retraction culture continues: UWM Class A found 53 days late and self-flagged (`STATUS.md:36`); a withdrawn 9/14 "bounded ~9/06" (`:120`); lessons §45/§47/§53/§54 are self-caught | as cited |
| §Open questions (`:66-67`) | (a) CORAL-lock re-verification cadence: **STILL OPEN as a mechanism.** Rule-level answer: LESSONS §28/§29. (b) GSE-MF interim rule: **CHANGED.** Ruled WQ-248 C locally (`STATUS.md:108`); fleet promotion unknown. (c) Uniformly-idle blind spot in ledger_staleness: **STILL TRUE.** HOMER is in that state now (9 days, no session) | as cited |

---

## 8. Routing candidates (ranked)

| # | Sev | Owner | Finding | Evidence |
|---|---|---|---|---|
| R1 | 🔴 | PROME (spawn) → HOMER | **Desk dark 9 days, intake unworked: 29 WALTER packets in `inbox/WALTER/`, all UNLOGGED in board_log (18 marked Role: ACTION), oldest 10/20.** About 10 registered docket clocks lapsed with no session: NRC/PHSI 10/20, PMMS + PHM 10/22, NVR ~10/21-23, ICE First Look ~10/22-28, GSE MF ~10/23-30, NHS + Case-Shiller 10/27, MTH 10/28. The NEXUS brief that CARL/REGINALD/HENRY/NEXUS read still carries PMMS 7.40% as live, although WALTER delivered 7.32% [wk 10/22] | boot B9 grep re-run 10/28; `STATUS.md:128-138`; `NEXUS_BRIEF.md:21,84`; `inbox/WALTER/SIG-W-20261022-029.md`; `docket/CATALYSTS.tsv` rows 4,5,11,13,14,16,20,24,28,30,31 |
| | | | *Where I may be wrong:* another orchestrated session could have integrated some of these outside `AGENTS/HOMER/` (I checked only HOMER-path commits and board_log membership). Several 10/27 WALTER packets are batch-review products and may be low-yield. "Dark" may be deliberate: HOMER is on-demand and the last close was Will-requested (`SCRATCH.md:19`) | |
| R2 | 🟠 | HOMER (+ PROME for READS.tsv) | **`thesis/PREDICTIONS.tsv` 36,472 B = 112% of budget** is effectively whole-read at boot step 8. Under READ_CAP rule 16 a predicate scan of unindexed rows is a WHOLE read, and the fleet checker cannot see it | `CLAUDE.md:204`; `read_cap_check` output (3 files found) |
| R3 | 🟠 | PROME / HOMER | **No `PROME/registry/READS.tsv` declaration for HOMER**, so the read-cap verdict is "clean within what the scan found, NOT a clean bill" | `read_cap_check --agent HOMER` RESULT line (`reads=3`, `charter_mode=unspecified`) |
| R4 | 🟠 | HOMER | **`LESSONS.md` 502 B from the 75% trigger.** One more lesson row crosses it. Closeout 1b measures STATUS only, so the next append will not trip HOMER's binding check | `LESSONS.md:6`; `CLAUDE.md:216-217` |
| R5 | 🟡 | HOMER | `STATUS.md` 22,157 B is 628 B under the desk's own soft target of 22,785 B. The catch-up session in R1 will breach it unless it archives first (retention rule `CLAUDE.md:213`) | `STATUS.md:6` |
| R6 | 🟡 | HOMER | Charter boot lacks a runtime-identification / explicit charter-and-root load step. The last session ran on Codex (`SCRATCH.md:3`), where READ_CAP rule 20's harness-injection premise (charter 38,671 B, exempt) may not hold. *May be wrong:* `PROME/COMPLETION_SPEC.md` may cover this generically | `CLAUDE.md:187-207`; root `CLAUDE.md` §How The System Works; `READ_CAP.md:32` |
| R7 | 🟡 | HOMER | `MEMORY.md` is stale and never boot-read. It holds the do-not-touch notes (`:13-18`), but `domain/` "exists but is empty" (`:18`) no longer exists. "attomdata.com" listed as working (`:28`) contradicts "ATTOM access UNRESOLVED 10/19: issuer paths 403" | `MEMORY.md:18,28`; `STATUS.md:136`; `NEXUS_BRIEF.md:36`; `ls AGENTS/HOMER/` |
| R8 | 🟡 | HOMER | Ruling residue in the boot-read index: LESSONS §35 row still says "Adopted here: soft **150KB** / hard **170KB**". The charter killed that tier (re-pointed 9/29). Annotate the index row; the cold text stays frozen | `LESSONS.md:113`; `CLAUDE.md:212` |
| R9 | 🟡 | HOMER | Index-integrity line is stale: "§44–53 ↔ `LESSONS_COLD_2.md` (10)", but §54 exists (11 headings). "Counts must match" is false on disk | `LESSONS.md:141,173`; `LESSONS_COLD_2.md:61` |
| R10 | 🟡 | HOMER | `OBLIGATIONS_OTHERS.md` B9 (DAEDALUS D1 confirm) is still listed as open, though `THESIS.md:122` D7 records "D1 CLOSED" (DAEDALUS packet 10/01). B7 disposition has been UNKNOWN since 9/24. B8's 10/02 matcher re-test result is not recorded | `OBLIGATIONS_OTHERS.md:13,15-16`; `inbox/processed/2026-10-01_from-DAEDALUS_D1-five-elements-confirmed.md` |
| R11 | 🟡 | HOMER | The charter FILES table omits OBLIGATIONS_OTHERS, LAST_COMPLETION, STATUS_COLD, LESSONS_COLD, LESSONS_COLD_2, `registry/`, `tools/`, and `RENT_BREADTH_ROSTER.tsv`. The `archive/` description is out of date | `CLAUDE.md:233-260` |
| R12 | 🟡 | HOMER | Counter drift: STATUS "YEAR TRAP, now n=4" vs LESSONS §46 "n=3" | `STATUS.md:14`; `LESSONS.md:149` |
| R13 | 🟡 | DAEDALUS (self) | The FLEET_MAP note "Profile FIRED; body August 7 remains historical" should be retired once this refresh lands. The old profile carries 3 stacked STALE banners | `profiles/HOMER.md:3-22`; FLEET_MAP HOMER row |

---

## 9. Not read / coverage limits

| Item | Status |
|---|---|
| `STATUS_COLD.md` lines 41–227, `LESSONS_COLD.md` 41–326, `LESSONS_COLD_2.md` 41–63 | **NOT read** (header-only by scope). Wide lines 21–38 of STATUS_COLD were cut at 600 chars. Cold crc pins were **not recomputed** |
| `thesis/THESIS.md` | Lines 1–24 plus a grep of headings/handle lines only. §3–§9 bodies not read (other cluster) |
| `thesis/PREDICTIONS.tsv` | Line 1 and size only |
| `docket/CATALYSTS.tsv` | Header plus awk projection of unresolved rows (cols 1–2, cut at 90 chars). Not read whole |
| `board_log.tsv` | grep only (membership test, AMENDED row, tail). Not read, by design |
| `inbox/WALTER/*` (29) | Title / Priority / Role lines only, plus the first ~20 lines of 2 packets. Content not adjudicated |
| `workbook/*`, `reports/*`, `archive/*`, `outbox/*`, `state_vectors/*`, `tools/rent_breadth.py`, `registry/corrections_receipts.tsv` | Listed and sized only (other clusters) |
| Git log authorship split | By commit-subject prefix. Per-hash enumeration complete for 10/02–10/27; 9/29 counted, not every hash listed |
| Checks run | `scripts/read_cap_check.py --agent HOMER` (RESULT line rc=0; my echoed `rc` was the pager's, so the RESULT line is the evidence). The B9 membership grep, re-run read-only. Not run: `ledger_staleness.py`, `corrections_boot_check.py`, `claim_check.py` |
| Writes | This file only (plus its directory). No git writes. Nothing under `AGENTS/HOMER/` touched: `git status --porcelain -- AGENTS/HOMER/` was empty. Other dirty DAEDALUS/`scripts/` paths seen at the end of the read (FLEET_MAP, CHECKS, SCORECARD, `claim_check.py`, inbox renames) belong to the concurrent caller session and are not mine |
