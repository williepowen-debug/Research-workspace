# Codex workspace audit — RECORD + PROME verification (2026-09-03 21:2x ET, DESKTOP)

**Owner:** PROME · **Status:** Will *"ok approved go ahead"* 21:27 on PROME's four-step sequence (§3). This file exists so the review is an ARTIFACT desks can read; Will relayed it in-session, Codex anchored at commit `0a06b98141406b17836cdec9f8acb5e91330cf12`.

## 1. PROME verification (21:1x, at the artifacts on HEAD `c101dc953`)

| Codex claim | Token | Observed |
|---|---|---|
| ORCH_LOG.tsv has 4 malformed rows; L15 = two VULCAN records fused | VERIFIED | L11/L12/L14 9 cols; L15 18 cols (date + two 9-field copies) |
| scorecard parser pads/truncates (zip); `as_int` int-only | VERIFIED | `coordination_scorecard.py` load()/as_int() |
| "63 zero-drain touches" == 63 non-integer `drained` cells | VERIFIED | exact match |
| brief-defect coverage too thin | VERIFIED | renderer: 2 of 83 scored (prose cell); after v2 typing 41 of 83 carry a count |
| BOARD/INDEX.md ~1.63 MB; scanner reads signal files | VERIFIED | 1,627,433 B; `board_scan.py` globs `SIG-W-*.md`. **Readers CORRECTED 21:3x (WALTER caught PROME's `grep -l` reading filename MENTIONS as reads — error #85):** `staleness_sweep.py` and PROME's `reads_check.py` only NAME the file in a docstring/comment; **the sole code reader is `walter_doctor.py` (L232 · L1345 · L1459), and all three sites parse STRUCTURE only** (ToC rows, TOTAL row, `## NAME (N)` headings) — no tool in the repo parses a signal data row ⇒ a generated compact index satisfies every machine consumer with zero reader changes; the design question is what HUMAN readers need (WALTER's back-marker convention included). Cutover test = `walter_doctor` green on the new surface. |
| KERNEL/README.md L3 "NOT LIVE" while activations + events exist | VERIFIED | 17 accepted events in `shadow/events/2026/09`; IMPLEMENTATION_STATUS stamped 8/26 |
| commit subjects avg ~210 chars, 577/1,817 >200 | VERIFIED | avg 211, 581/1,817 (window moved) |
| VIOLET `test_daily_log.py` fails IndexError | VERIFIED | still fails 9/3 |
| no root CI workflow | VERIFIED | no `.github/workflows` |
| 9 of 37 desks over a read budget, 3 over the cap | VERIFIED 21:4x | `--all` was a usage error (fell through to the file path; DAEDALUS added an unknown-flag guard `503dbebe4`); PROME ran `read_cap_check.py --fleet`: **9/37 over budget · 3/37 over the cap** (BRENT board_log 536% · AEOLUS SCRATCH 140% · FALCON STATUS 119%) |
| root `scripts/tests` discovery aborts on a `sys.exit(0)` import | UNKNOWN | pytest not on system python; not reproduced |
| ~4,933 files under processed paths | VERIFIED (approx.) | 5,061 on HEAD |

## 2. PROME's read (as given to Will 21:1x)
Agree: scorecard repair with typed columns · short commit subjects · one read-only validation entrypoint over a manifest (CHECKS.tsv is the embryo) · KERNEL status derived from records · three separate meters (hot-read bytes / active-tree files+bytes / history size). Push back / constrain: consumed-handoff receipts are a FLEET rule (carve-out ①, every desk's `processed/`, the cold-read-at-a-path culture) → Will ruling + DAEDALUS blueprint with an obligation audit, not a sweep · BOARD index is WALTER's, safe only because the scan reads files · typed ledgers + generated digest for dates/levels/gate state, NOT for HEARTBEAT's judgment layer · binaries-out is a spend/infra choice (RESEARCH-INTAKE is the natural candidate) · "withdraw quantitative conclusions" — none exist yet, the renderer is descriptive-only until 4 renders; the damage was prospective (first render 9/4). Where Codex is thin: it prices the instrumentation as cost and not the silent rot it was built against; correction commits are often the checks working.

## 3. Sequence approved by Will 21:27
1. ORCH_LOG repair + typed columns (PROME) → **DONE `69ec68d43`**; renderer changes → DAEDALUS packet.
2. WQ-171: commit-subject rule (root Git Protocol) + KERNEL status-surface edit authorization + the receipt-lifecycle / binary-sidecar design commission.
3. WALTER packet on the BOARD index; KERNEL status fix on Will's word.
4. Receipt lifecycle + sidecar as a Will-ruled design with DAEDALUS after the canonical-state items.
Codex's own do-not list adopted: no history rewrite · no AGENTS reorg · no KERNEL expansion · no new validators before the ledgers are typed.

## 4. Codex text — VERBATIM as relayed by Will 21:1x

> ## Bottom line
>
> The workspace is disciplined but over-instrumented. Its biggest cost is not any single large subsystem; it is that provenance, operational state, delivery evidence, generated views, and historical records frequently coexist on the same hot path.
>
> This creates a loop: more state → more mirrors → more checks → more correction commits → more archived state
>
> The best simplification is to separate: 1. Small, structured canonical state. 2. Generated, disposable operator views. 3. Cold evidence retained outside active working paths.
>
> I anchored measurements to commit 0a06b98141406b17836cdec9f8acb5e91330cf12. Other sessions advanced the repository while I reviewed it, so I did not treat subsequent changes as part of the audit or modify anything myself.
>
> ## Highest-priority finding: the coordination scorecard is invalid
>
> The orchestration scorecard currently produces plausible-looking but unreliable results.
> - PROME/state/ORCH_LOG.tsv contains four malformed rows.
> - Line 15 contains two VULCAN records fused into one physical row.
> - The scorecard parser silently pads short rows and truncates long ones instead of rejecting them: AGENTS/DAEDALUS/scripts/coordination_scorecard.py:37.
> - Its integer parser accepts only plain integers: coordination_scorecard.py:58.
> - Consequently values such as 13→1, 6 (5 root + 1 WALTER), and n/a (drained at touch 1) become None.
> - The current "63 zero-drain touches" happens to equal the 63 non-integer drain cells. It is measuring parseability, not zero-drain behavior.
> - Brief-defect coverage is similarly too incomplete to support conclusions.
>
> This should be repaired before using the scorecard for system decisions: replace drained with typed columns such as inbox_before, inbox_after, and drained_count · give brief_defect_count its own numeric column · keep prose in a separate notes field · require exactly the declared number of columns · fail closed on malformed or nonconforming rows · append through the existing strict TSV helper only · regenerate, rather than patch, the scorecard report. This is a small-to-medium repair with very high correctness value.
>
> ## Where the weight is
>
> At the review anchor: 12,103 tracked files · about 313 MB of current tracked blobs · 10,862 commits · .git about 378 MB · AGENTS/ 8,970 files and 278.5 MB (~89% of tracked bytes) · ~4,933 files under processed paths · PDFs ~122 MB, DOCX+HTML another 62 MB · 384 sets of duplicate current blobs (~4.8 MB).
>
> Git already deduplicates identical blobs internally. Therefore, removing duplicate paths mainly improves navigation, search, checkout size, and cognitive load — not necessarily pack size.
>
> The recent "rotation" work illustrates the distinction: HEARTBEAT became much smaller as a hot read, but the current tracked tree grew by roughly 68 KB because snapshots and cold copies were added. Other GATES, NEXUS, TERRY, and DAEDALUS rotations also reduced hot-file size while increasing total stored material. That work was useful for model context, but it was not repository slimming. The system needs separate metrics for: hot-read/context cost · active-tree size and file count · Git-history size.
>
> ## The best clutter reduction
>
> ### 1. Stop retaining full consumed handoffs in the active tree
> BOARD already retains the canonical signal, and agent ledgers record disposition. Keeping complete per-recipient copies after consumption is usually a third copy of the same evidence. A cleaner lifecycle: pending handoff remains self-contained · consumption writes a compact receipt (signal ID, disposition, result, commit) · the full consumed handoff disappears from active HEAD; Git history remains the audit trail · if cold manifests are required, one monthly manifest instead of thousands of small files. Largest opportunity to reduce path count without redesigning agent ownership.
>
> ### 2. Generate the BOARD index
> BOARD/INDEX.md is about 1.63 MB, with extremely long rows, while the directory already contains 879 individual signal files. The actual board scanner parses signal files directly (PROME/tools/board_scan.py). Only a small number of live tools depend materially on the monolithic index. Make the index a compact generated view derived from signal frontmatter — or shard it by month/cluster. Store each signal's narrative once.
>
> ### 3. Put future source binaries outside the operational repository
> Current tracked PDFs, DOCX, HTML, raw captures, and source material dominate byte weight. Moving them to an internal archive does not remove their bytes from Git history. For future intake, use a private source sidecar or object store containing the binary, while this repository retains: stable locator · SHA-256 · retrieval date · source/provenance metadata · extracted text or concise research artifact. I would not rewrite the existing Git history. Too many records refer to commit hashes, and KERNEL depends on native provenance. If clone size eventually becomes intolerable, the safer answer is a compact v2 operational repository with this one preserved read-only.
>
> ## PROME is paying a high control-plane tax
> The explicit core/boot files totaled roughly 159 KB before auto-memory and conditional material. The existing measurement report previously found approximately 315 KB — around 79K tokens — at boot (PROME/proposals/2026-08-28_prome-slimdown-MEASUREMENT.md:4). The one-shot boot gate runs six subprocesses and roughly ten additional internal checks (PROME/tools/prome_gate.py:641). Some BOOT instructions also appear to request standalone checks that the gate already performs. More importantly, several dashboards and gates parse narrative Markdown or dense mixed-type TSV fields. Prior audits show those parsers can return nonempty but semantically wrong results.
>
> The long-term simplification should be: canonical structured ledgers for docket, gates, queue, orchestration, and decisions · one small generated operator digest · narrative reports generated from structured state, not parsed back into it · generated caches such as dashboard_state.json left untracked unless cross-machine comparison genuinely requires persistence · shared parser modules rather than duplicated regex implementations. Do not add another state ledger to accomplish this. Consolidate the existing ones.
>
> ## Validation and read-budget enforcement are incomplete
> Generally well tested: KERNEL 220 passed · MESSAGING 22 · PROME tool tests 4 · several agent suites. But: VIOLET's daily-log test (AGENTS/VIOLET/scripts/test_daily_log.py) still fails with an IndexError, matching a failure documented nine days earlier · root scripts/tests discovery aborts because one test executes sys.exit(0) during import, although running that test directly passes · no root CI workflow · the heuristic read-cap scan found 9 of 37 active/tier-2 desks over at least one read budget and 3 over the physical cap · the declared-read system covers only PROME and WALTER, and both attestations were stale.
>
> I recommend one read-only root validation command, optionally run in CI, which: runs all suites through a manifest · makes script-style tests import-safe · validates TSV widths and types · runs read-budget checks from executable declarations · never writes acceptance state or KERNEL events. The read declaration should come from the same manifest or runner that performs the reads. A separately maintained fleet-wide READS.tsv will continually drift.
>
> ## Other important cleanup opportunities
> - KERNEL itself is strong, but its status surfaces have drifted. KERNEL/README.md:3 says no live activation exists, while dated activation and shadow-event records now exist. KERNEL/IMPLEMENTATION_STATUS.md:5 is also stale. Derive current status from activation/event/closeout records and archive the implementation chronology.
> - Some live protocol documents have become changelogs. The WALTER board-consumption specification retains superseded wording inside the current spec. Move historical language to Git/history and leave one current rule.
> - Commit subjects average roughly 210 characters; 577 of the last 1,817 exceeded 200 characters. The commit subject has become another operational ledger. Use a short subject and put proof in the body or artifact.
> - Preserve small path-scoped commits where they prevent concurrent-agent collisions. The problem is not small commits themselves; it is correction churn and volatile measurements embedded across multiple surfaces.
> - Avoid reorganizing the flat AGENTS/<NAME> structure for now. Generated navigation or sparse checkout is safer than a directory-wide migration.
>
> ## Recommended sequence
> 1. Repair ORCH_LOG.tsv and the coordination scorecard; withdraw current quantitative conclusions. 2. Add one read-only root validation entrypoint and fix the persistent VIOLET/discovery failures. 3. Replace consumed handoff copies with compact disposition receipts. 4. Generate or shard BOARD/INDEX.md. 5. Enforce an external-storage boundary for new source binaries. 6. Consolidate PROME into typed canonical ledgers plus one generated hot digest. 7. Derive KERNEL status and move superseded protocol text out of live specifications.
>
> I would specifically avoid history rewriting, a large AGENTS directory reorganization, further KERNEL expansion, or adding more validators before the canonical-state problem is addressed.
