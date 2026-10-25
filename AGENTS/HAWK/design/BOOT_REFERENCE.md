# HAWK boot provenance — reference only

Moved verbatim from CLAUDE.md October 25 to preserve current boot headroom. On-demand history, not a whole-read boot dependency. Current operating steps remain in CLAUDE.md.

**🏗️ SPLIT 2026-07-12:** HAWK's two acute, independent war-tracking loads (Russia/Ukraine, US-Israel-Iran) spun out into sibling domain agents — **OSPREY** (`AGENTS/OSPREY/`) and **FALCON** (`AGENTS/FALCON/`). Root cause: one agent holding two acute wars predictably starves the secondary theater (the HAW-15 Ukraine-crude-terminal miss + the HAW-03 Venezuela ~5.5mo-stale miss are the two documented instances). Splitting the load is the structural fix, not another ledger patch. Spec: `design/2026-07-12_war-agent-split-spec.md`. Build record: `AGENTS/DAEDALUS/builds/OSPREY_FALCON_BUILD.md`. HAWK's pre-split historical record (KB, PREDICTIONS HAW-01..17, board_log, the 36-row strike ledger) freezes/continues in place here per `FILES.md` — **HAWK remains a live agent, narrower in scope, not retired.**



---

 *(Read-cap remedy executed 2026-09-02 under DAEDALUS's 8/28 ruling. The file measures 96,616 B as measured 2026-10-25, over the single-read cap, so a whole read silently returns a **TRUNCATED** file — every line-count guard still passes, and the tail is where the resolution clauses live. The honest fix is a protocol statement of what IS read, not a smaller file: these rows are the permanent calibration record and are not compressible. `[[finding_output_shape_implies_more_than_the_measurement]]`.)*

---

     - ⚠️ **Two traps, both found 2026-07-28 when this step was audited after lying dormant since 6/12 (46 days).** ① **`grep -i hawk` matches "hawkish"** — and macro/Fed signals say "hawkish" constantly. That inflated the apparent gap **20×** (40 un-dispositioned → **2**). **Match the agent name on a word boundary and exclude the adjective:** `grep -nE "\bHAWK\b" BOARD/INDEX.md | grep -vEi hawkish`. Then restrict to routing columns, because cluster-description rows also contain the name. ② **Reconcile on the KEY (signal ID), not a substring** — pulling IDs off any line that mentioned "hawk" attributed other agents' signals to HAWK.
     - 🎯 **What the audit found, and it re-scopes this step rather than retiring it: real coverage was 56/58 despite the step never running, because the WALTER lane hand-delivers everything routed `to:` HAWK.** Both leaks were rows where HAWK sat in **`info:`** on another agent's primary route — the class WALTER does not hand-deliver. **⇒ The routine residual is the `info:`/cc lane.** Join by ID before reading; an unmatched ACTION row found during a coverage audit remains a separate explicit gap, never assumed consumed merely because direct delivery normally covers it.


## Pre-consolidation operating text, October 25

Historical instruction copy; current CLAUDE.md governs.

## SPAWN PROTOCOL

**Boot and closeout are one symmetric sequence: what you READ at boot, you WRITE BACK at closeout.** The CLOSEOUT phase is the write-back tail — run it at **EVERY session end, not just end-of-day** (per auto-memory `[[feedback_intra_day_closeout_discipline]]`). Read→write pairings: STATUS (read 1 → write 10), SCRATCH (read 2 → write 14), predictions (surface 6 → resolve 11), NEXUS_BRIEF (cross-agent synthesis twin of SCRATCH → write 15, **mandatory every session**).

### BOOT (read phase)
0. Resolve the repository root. Explicitly read root `CLAUDE.md`, `AGENTS.md`, `USER.md` and this desk's instructions. Record the actual runtime, exposed model identity, session ID and tool coverage under `PROME/COMPLETION_SPEC.md`; UNKNOWN stays UNKNOWN. Follow `PROME/ORCHESTRATION_PLAYBOOK.md` Runtime mechanics. Run Git operations from the repository root. Before any pull, follow `docs/GIT_WORKTREE_PROCEDURES.md`; foreign dirty work defers pull, never authorizes a stash or rebase.
1. **Read `STATUS.md`** — cross-war reconciliation dashboard + dormant book. *(Mirror of closeout step 10.)*
2. **Read `SCRATCH.md`** — ephemeral handoff from last session. *(Mirror of closeout step 14.)*
3. **Read `LESSONS.md`** — mistake patterns to avoid (incl. the dormant-vector re-sweep discipline, item 3 — HAWK's own operating lesson post-split).
4. **Read `AGENTS/OSPREY/NEXUS_BRIEF.md` + `AGENTS/FALCON/NEXUS_BRIEF.md`** — the synthesis inputs (per SYNTHESIS DISCIPLINE above). Reconcile into your own view; do not re-narrate their event logs.
5. **Read `AGENTS/VOCABULARIES.tsv` + `workbook/SCHEMA.tsv` before any KB write** — VOCABULARIES: NETWORK_GROUPS (Group), CANONICAL_ENTITIES (Entity), SOURCE_TAGS (Source); use closest term + note the gap if no match. SCHEMA: validate enum fields (Conf, Epistemic, Status) against `allowed_values`, use `default` when unsure.
6. **Surface due/stale predictions** — ⛔ **`thesis/PREDICTIONS.tsv` IS NEVER READ WHOLE AND THIS STEP DOES NOT ASK YOU TO.** The permanent calibration file is 96,616 B as measured October 25; scoped reads only. **Read exactly these two scoped slices:**
   - **(a) the calibration scoreboard preamble** — `head -20 thesis/PREDICTIONS.tsv` (the HIGH-CONFIDENCE-FAILURES block; read it before writing any new prediction).
   - **(b) the OPEN rows only** — `awk -F'\t' 'NR==1 || $6=="OPEN"' thesis/PREDICTIONS.tsv` — HAW-18+ synthesis/dormant-book rows; HAW-01..17 are the frozen pre-split historical record.
   Then open a **single row's** Prediction/Resolution cells in full **only** when you are actually resolving that row. Flag any whose Timeframe has passed or whose Status can now be resolved. (Closed-prediction full post-mortems live in `thesis/PREDICTIONS_ARCHIVE.md` — reference-only, NOT loaded at boot; keyed by `#hawk-NN` anchor.)
6a. **Ledger staleness check** — run `python3 "$(git rev-parse --show-toplevel)/scripts/ledger_staleness.py" HAWK --quiet`; surface any ⚠️ stale-ledger alert and freeze-or-refresh it at closeout (root CLAUDE.md Data Hygiene).
6a-2. **R1 corrections check (fleet-wide — FORUM-6 ruling ①, Will-approved 2026-08-17):** `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" HAWK` — §9 rc 0/1/2; **rc=1 = a NAMED correction is unreceipted:** read the pointer, then receipt in the **WQ-399 form** (Will 2026-10-08; the writer refuses an incomplete receipt with rc 2 and writes nothing): `--receipt <id> --action APPLIED --artifact <path#key> --validation-ref <path#key|NONE>` · `--action NO-OP --scope <text>` · `--action DEFERRED --review YYYY-MM-DD` · `--action CONTESTED` (optional `--scope`/`--artifact`/`--note`); then commit `registry/corrections_receipts.tsv`. *(Receipt line updated 2026-10-10 on WALTER SIG-W-20261008-033, C4-class own-charter edit.)* *(Wired 2026-08-28, DAEDALUS wiring sweep leg ①, batch Will-approved in-session.)*
6a-3. **Derived-input check (byte fingerprints only; not quote freshness, semantic consistency, completeness or band reachability):** run `python3 AGENTS/HAWK/scripts/derived_freshness.py` from repo root (absolute script path works from any cwd). rc1: read changed owner inputs and reconcile BOTH aggregates; rc2: missing/invalid evidence, do not certify. Capture inputs with `--capture /tmp/hawk-inputs.json` before review; after reconciliation use `--record /tmp/hawk-inputs.json` and rerun. This checks bytes, not external data age or semantic truth. Update the explicit dated-analysis dependency list when a newer owner analysis is adopted.
6a-4. **Native Europe check:** inspect the dated six-rung review table in `domain/europe-rearm/LADDER.md` on demand. Its 14-day evidence rule is separate from VX's 45-day backstop. Missing primary evidence stays UNMEASURED after a search; a review date is not an evidence date. The workbook staleness pass does not cover `INCURSIONS.tsv`.
6b. **Dormant-book re-sweep check** — for each of the **11** dormant `workbook/VX.tsv` rows *(count corrected 2026-08-15 from a stale "8" — the TWN-01/TWNMIL-01 7/28 split and the CODIF-01 8/10 registration both landed without this line being updated; corrected again 2026-09-18 from "10" on the EURMIL-01 registration, **in the same commit as the row**, which is the only thing that has ever stopped this drifting)*, compare `Last_Updated` against a **45-day re-sweep cadence**. Any row past cadence is a **re-sweep-due trigger against external primaries, not a carry-forward** — this is the direct lesson from HAW-03/Venezuela sitting stale ~5.5 months while Iran absorbed bandwidth (`LESSONS.md` #3). Use each row’s `Guard` and `Watch_Source`; exclude SUPERSEDED CEASEFIRE from scheduling. The45-day backstop remains for every active row. A partial review date never closes missing evidence legs: retain their earlier follow-up in STATUS/CATALYSTS. Flag due rows here; execute the re-sweep at closeout step11.
7. **Signal intake** — check both inbox lanes at every boot for thesis falsifiers/corrections; process pending signals within the current task scope (see MAIL).
   - **a. `inbox/`** — cross-agent signals (INTEGRATE / LOG / DISCARD); log a one-line KB.tsv entry per integrated signal; `git mv` to `inbox/processed/`.
   - **b. BOARD scan** — parse `/BOARD/INDEX.md` signal rows for exact HAWK recipients in the routing field; verify `to`/`info` at the signal frontmatter, excluding parenthetical routing commentary. Join exact signal IDs against ALL existing `board_log.tsv` sources, read the signal, decide disposition (`acted`/`noted`/`deferred`/`info-only`/`skipped`), append a row. Spec: current `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md` §5. Never read the whole INDEX into context; retrieve only unmatched signal files in bounded chunks.
     - Read `design/BOOT_REFERENCE.md` on demand for historical BOARD matching failures. Current rule above is exact recipient/frontmatter plus exact-ID membership, not a keyword-title search.
   - **c. WALTER lane** — list `inbox/WALTER/*.md`; test each exact signal ID by a full-file search of `board_log.tsv` (never a whole-file context read). Check `source=INBOX_WALTER` separately; a prior BOARD disposition is not a new signal. Read any correction note independently even if its parent ID is present. For each unconsumed item, read → decide disposition → append `board_log.tsv` row → **`git mv`** (never bash `mv`) to `inbox/WALTER/processed/`. Canon: WALTER BOARD_CONSUMPTION_SPEC §5.2.
   - Let `acted` items inform this session.
8. **`web_search`** — for dormant-vector re-sweeps due (step 6b) and any cross-war synthesis question that OSPREY's/FALCON's briefs don't resolve. Do NOT re-search theater events already covered in their briefs.

### EXECUTE
9. **Execute the task.**

### CLOSEOUT (write-back — run at EVERY session end)
10. **`STATUS.md`** — write the cross-war reconciliation dashboard + dormant book back: reconciliation deltas, double-count check, war-risk/shipping aggregate, dormant book table. Threshold breaches + active decisions go to the top. **Byte gate: `python3 scripts/read_cap_check.py --agent HAWK` from repo root; `rotation_due=1` ⇒ rotate the named surface (or record a dated deferral).** ≤120 lines is a thinness heuristic only (this is a thin synthesis surface, not a theater tracker — if it's growing toward 250, you're re-narrating, see SYNTHESIS DISCIPLINE). *(DAEDALUS Prose-Remedy #1, 2026-10-08; C4-class edit 2026-10-10.)* *(Mirror of boot step 1.)*
11. **Workbook / ledgers + predictions** — log new synthesis/dormant facts → `workbook/KB.tsv` (KB-HAWK-224+; pre-split rows ≤223 are frozen history); dormant-vector state changes → `workbook/VX.tsv` (11 rows, including the superseded historical anchor); the shared decoupling thesis + any cross-war transmission pathway updates → `workbook/FLOW.tsv` (FLOW-HAWK-19 is the live canonical row). **Execute any dormant re-sweep flagged at boot step 6b** — verify against external primaries, don't carry-forward. **Resolve every prediction flagged DUE at boot** in `thesis/PREDICTIONS.tsv` (HAW-18+ only).
12. **Synthesis-consistency check** — does HAWK's combined read still match what OSPREY and FALCON are independently saying this session? Flag any divergence lasting >1 session to both siblings. Did any dormant vector's Red band trigger? If so, that vector likely needs to graduate out of the dormant book (flag to Will/PROME, don't silently promote).
13. **Cross-war strike aggregate** — refresh `domain/energy-strikes/CROSS_WAR_SUMMARY.md` (thin, **regenerated** from OSPREY's + FALCON's own ledgers — never independently maintained; see FILES table). **When regenerating, read the source artifact's own header/ANALYSIS, not just its row count** — the 7/12 version reported FALCON "thin/unbuilt, backfill not yet run" for 13 days after FALCON had executed it, and that same header carried a partial falsifier for HAW-18 (`LESSONS.md` 2026-07-25 item 2).
13a. **Cross-theater war-risk aggregate (standing lane, Will-approved 2026-07-25)** — refresh `domain/war-risk/CROSS_THEATER_WAR_RISK.md`. Same derived-not-owned convention: theater legs belong to FALCON (Gulf/Hormuz/Red Sea/Bab + JWC/P&I) and OSPREY (Black Sea); HAWK contributes the **cross-leg comparison** and catches **stale owner carries**. **Flag any leg whose print is >10 days old**, and re-stamp `Refreshed:` even on a no-change pass — this surface is derived, which means it rots at the cadence of its regeneration, not on its own. *(The ~8/1 sunset on the market-wide insurer cc lane was cancelled by Will 2026-07-25 — this lane is now permanent, so it needs a mechanized refresh rather than a remembered one.)*
13a-2. **Record and check derived fingerprints** after both aggregates are reconciled (boot6a-3); if an owner changed during review, capture/read the delta and repeat. Never record merely to silence drift.
13b. **Falsification page:** re-read `thesis/FALSIFICATION.md` against canonical FLOW/VX/prediction rows and received owner corrections; update derived readings and the refresh stamp, preserving registered conditions.
14. **Rewrite `SCRATCH.md`** using `templates/SCRATCH.template.md` — CHANGES SINCE / WHAT I DID / NEXT SESSION (dated, future-verifiable) / OPEN THREADS / pending decisions / one-line mail state. *(Mirror of boot step 2.)*
15. **`NEXUS_BRIEF.md`** — write-back the cross-war synthesis brief (schema `AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md`). **Mandatory every session, even no-change** — minimum is refreshing the `As of:` stamp + `STATUS commit:` hash. NEXUS reads this at its boot in place of raw STATUS.
16. **Promotion scan + Git** — thesis-level finding → `thesis/`; transferable cross-agent lesson → auto-memory; HAWK-specific durable learning → local `MEMORY.md`. Cross-agent signals → `outbox/` (see Outbox Protocol). **Git: commit own files per root CLAUDE.md §Git Protocol (pathspec `AGENTS/HAWK/`) + auto-push via `scripts/safe-push.sh`** (fast-forward gated; no force). Apply root session-end checks 1b–1e, including orphan, consumer, ledger nudge, applicable memory-index and claim checks. Every commit follows `docs/GIT_WORKTREE_PROCEDURES.md`. Non-fast-forward recovery follows the root dirty-path overlap rule, never an unconditional pull/rebase.

**MAIL:** Boot always checks for pending corrections/falsifiers (LESSONS 2026-07-25). Process active intake when the task includes it; archival backlog processing is separate. Keep unresolved work visible and do not claim consumption from a filename or a move alone.

**⚠️ Messaging system status:** File-based mail is being overhauled (auto-memory `[[project_messaging_overhaul]]`). Don't invest in inbox/outbox hygiene infrastructure. For time-sensitive cross-agent signals, prefer **Convention B** (own-outbox routing, scanned by PROME at boot), direct-drop into the target inbox **with Will's explicit authorization**, or surface to Will directly. **Steady-state cross-agent synthesis flows through `NEXUS_BRIEF.md`** — outbox is reserved for 🔴 acute signals.

All mail lives under `AGENTS/HAWK/`:
- **Inbox:** `inbox/` — inbound signals from other agents
- **Outbox:** `outbox/` — outbound signals you write for other agents
- **Processed:** `inbox/processed/` — signals you've integrated
- **Delivered:** `outbox/delivered/` — signals marked delivered (manually, on direct-drop)

### Outbox Protocol
Write a single `.md` file to `outbox/` per signal:
- **Filename:** `YYYY-MM-DD_to-[target]_[short_description].md`
- **Format:**
```
## YYYY-MM-DD — To: [TARGET_AGENT]
**Signal:** [one-line headline]
**Detail:** [2-3 sentences — what changed, why it matters]
**Source:** [data release / own analysis]
**Priority:** 🔴/🟠/🟡
```
- Delivery is direct — there is no HERMES sweep layer. With Will's authorization, copy the packet to the target `inbox/` (rename `to-X` → `from-HAWK`), then move your copy to `outbox/delivered/`; otherwise `outbox/` is scanned by PROME at boot (Convention B).
- **Write a signal when:** a reconciliation produces an actionable divergence, a dormant vector fires, or a prediction resolves. **Do NOT write for:** routine STATUS updates.

If a cross-agent threshold breaches during your work, append to `AGENTS/SIGNALS.md`:
```
| DATE | HAWK | TARGET | 🔴/🟠 | Description |
```

### Git (fleet standard — root CLAUDE.md §Git Protocol owns the rules; cite, don't restate)

- Pathspec: `AGENTS/HAWK/` — path-scoped commits only, run from repo root.
- Auto-push at closeout via `scripts/safe-push.sh` (ff-gated, fails safe). Non-ff abort → `git pull --rebase` + re-push; NEVER force.
- Self-authored inbox packets follow root Git Protocol carve-out ①. Delivery authorization is separate; do not leave an authorized self-authored packet uncommitted.

---

