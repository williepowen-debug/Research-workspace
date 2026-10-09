# Charter split — raw review and execution evidence

Synthesis: `2026-10-09_CHARTER_SPLIT.md`. Each supplied report/output below is verbatim. Final content review will be appended separately.

## Initial independent remedy review (including reader correction)

# DAEDALUS charter remedy / consumer review — 2026-10-09

Reader: thread-local Codex review helper `/root/charter_boundary_review`; OpenAI runtime, model variant/session ID unavailable beyond that task identity. Repository resolved as `/home/willi/Research-workspace`. Read-only repository work; this raw report is the sole write, under `/tmp`. No desk launch, Git mutation, owner messaging or repository edit performed. Parent supplied Will's authorization for the bounded preservation split; I did not independently replay the operator conversation.

## Verdict before implementation

**QUALIFIED: the proposed four-section verbatim move is a sound preservation remedy if the conditions below are applied. It is not yet final-candidate acceptance.** One required whole-read companion avoids hiding active rules. It addresses per-surface size, not total reading cost. The proposed sections occupy 16,841 B; the remaining original charter text occupies 18,857 B, leaving enough room for the required pointers while keeping both below 22,785 B. No rule rewrite or checker redesign is necessary to perform that split.

Basis charter: 35,698 B, SHA256 `1e28df1328c3a6dfa9de902bdc658cf3373f56f8ee2a24bb8cd9163df663f3c5`. Measured by splitting before level-two headings, including each section's trailing separator/whitespace:

| Block | Bytes | CRC32 decimal |
|---|---:|---:|
| THE JOBS | 5932 | 558410137 |
| MATURITY LADDER (per-class) | 3080 | 2931681408 |
| MEMORY MODEL (your learning) | 5462 | 2080594825 |
| FILES | 2367 | 951076245 |

## Findings and smallest required amendments

| ID | Finding / consumer evidence | Required disposition |
|---|---|---|
| R1 | A whole-read boot pointer preserves access only if it is mandatory at every boot and identifies the companion as active charter rules. The four sections contain live permission restrictions, ladder semantics, sweep obligations, write-back rules and the 10/15 held-L4 check. Calling them cold/archive/on-demand would change their force. | Add the explicit whole read in SPAWN/read execution, before task execution; preserve all four blocks verbatim. Companion header states active rules, same authority, and all desk-relative paths remain relative to `AGENTS/DAEDALUS/`. Authority/Git/output/startup remain in CLAUDE. |
| R2 | A bare top-level pointer breaks addressable consumers. `SPEC.md:3,57` directs readers to CLAUDE's MEMORY MODEL/MATURITY LADDER, and `BLUEPRINTS/market-agent.md:140` names CLAUDE §MATURITY LADDER. Charter itself says 'see Job 5', 'see JOBS', 'ladder below'; moved text says 'AUTHORITY' and 'SPAWN' without naming another file. | Retain exact original level-two heading stubs in CLAUDE with explicit section destinations in OPERATIONS. For Job 5 retain an addressable subheading redirect or explicitly name its destination at the existing pointer. Companion header resolves AUTHORITY/SPAWN references back to CLAUDE. This is smaller and safer than editing every historical/external citation. Do not duplicate substantive rules. |
| R3 | Shared `scripts/read_cap_check.py:736–788` gives an attested manifest precedence over charter scanning; explicit runtime overlay adds only root/local CLAUDE. A pointer alone does **not** add OPERATIONS to the declared perimeter. | Add READ whole for OPERATIONS, BASIS boot-defining for OPERATIONS, refresh own attestation and hash evidence, route precise owner application to PROME. Verify exact application separately. Until application, live shared results omit this new read; a proposed-manifest result is TEST ONLY, never live coverage. |
| R4 | `PROME/tools/reads_check.py:297–331` dates every declared BASIS plus attestation path from Git history; an uncommitted new BASIS has no readable history and is stale. `basis-hashes.json` records identity, not coverage/correctness. | Do not treat a precommit stale finding for the newly added companion as a schema defect or change its mode to clear it. Verify post-publication owner application and dated basis as a separate fact. Record the pending state honestly. |
| R5 | Local `AGENTS/DAEDALUS/scripts/read_cap_check.py:63–83` has a fixed DEFAULTS list and says it must track the boot reads. OPERATIONS would be absent from bare local invocation. This is distinct from the root consumer used by B4/C7. | Parent subsequently authorized adding exactly `OPERATIONS.md` to DEFAULTS as necessary consumer alignment. This is the smallest correct remedy: add only that member, preserve thresholds and verdict behavior, verify bare default membership and isolated capable/clean cases. Remedy accepted before implementation; final source diff/results still unreviewed. |
| R6 | READ_CAP rules 7,11,17,18 require re-trigger, recomputed preservation evidence, total cost, and obligation audit. Exact block transfer is stronger than a summary but bytes alone do not prove the read path or references survived. | Record dated re-check at append/closeout; compare each block's bytes/CRC; enumerate moved duties and compare their destinations/read paths. Publish both resulting file sizes and old/new combined bytes (headers/stubs increase total). Carry bytes-before/after and obligation-before/after in the same commit record. |

Smallest safe form: the proposed two active, mandatory-read files plus exact heading redirects and declaration evidence. Do not turn the companion into archive, summarize its rules, or remove safety/provenance text to hit a size target. The measured headroom makes such losses unnecessary.

## Candidate-v2 contract and parent follow-up

The existing spec §7 (`design/2026-09-17_DAEDALUS_GATE_SPEC.md:56–74`) requires final candidate bytes, complete per-step dependencies/context, report hash evidence, commit-parent/path/content comparison, and later fresh-origin membership. A successful boundary identity does not clear BLOCKING or nonmaintenance UNKNOWN. Later author changes are POST-REVIEW until the relevant final follow-up; a QUALIFIED review remains pending. Historical context is permissible only as historical evidence and never establishes current state.

**C1/C8 global context cannot be certified complete merely by enumerating today's top-level roots.** Direct consumer evidence:

- `scripts/orphan_check.sh` executes global `git status --porcelain`; its classification includes every external uncommitted path, including paths under a newly created top-level directory. `daedalus_gate.py:499–519` supports only nonempty exact path lists for status/history. `candidate_snapshot:533–534` makes declared unsupported limitations UNKNOWN. A new top-level untracked packet inserted during the battery changes C1 output but is absent from the proposed root list. Existing named-root status context would miss it.
- `complete_check.py:70–85` executes global `git log --since=... --pretty=%H %s`, selecting DAEDALUS subject prefixes; it then reads each selected commit's changed paths and diffs. `AGENTS`/`PROME` path history can cover pairing/claim-relevant commits, but cannot bind its entire population/count: an empty DAEDALUS commit or a DAEDALUS commit touching only an omitted root changes the consumer's population. Named-path history is a useful subset, not equivalence to that query.
- Gate selftest's named-path history drift case at approximately lines 1066–1076 verifies exactly that subset; it does not establish global-history equivalence or missing-top-level detection.

Under the unchanged contract, represent unsupported global context in per-step limitations and preserve UNKNOWN; do not write a false completeness assertion to get candidate eligibility. If the parent can supply independently verified evidence that the exact **used** input population is entirely represented at both endpoints, that narrows a snapshot claim but still does not establish an automatically enforced global boundary for reuse. Candidate review must distinguish those claims. No checker change is proposed by this report.

Publication distinction requested by parent: I found **no independent prohibition on persisting/publishing honestly reviewed artifacts and failure/UNKNOWN evidence** in the inspected root Git Protocol or runner spec. Spec §1 expressly separates commit/push from the runner; §2 says BLOCKING defects must be fixed before **closing**, while §7 withholds candidate eligibility/assurance for UNKNOWN. Charter requires the verification calls before commit/push; it does not turn a failed verification into permission to claim eligibility. Parent reports explicit Will direction to publish with clearance distinct. Therefore reviewed publication with prominently retained UNKNOWN is consistent with these texts, provided it is not represented as eligible candidate acceptance or completed clean closeout, actual path/authority/Git safeguards remain satisfied, and final independent content review completes. This is a bounded interpretation of inspected canon, not a claim that every repository policy was surveyed.

## Counterexamples / falsifiers

My positive split verdict would be refuted if any moved block differs from the measured source, a moved live obligation ceases to be a mandatory boot read, or an existing canonical section reference stops reaching its rule. My consumer-gap finding would be refuted by a live manifest already carrying OPERATIONS as whole plus the matching owner-attested BASIS; the current proposed declaration has no such entries. My global-context objection would be refuted by an existing supported context mechanism that binds the unscoped global status/history population, or a demonstrated semantics-preserving derivation covering all consumer outputs; the inspected implementation only supports named exact paths. Conversely, moving the four blocks verbatim plus requiring them at boot is a counterexample to any claim that a split necessarily weakens active rules or must reduce total bytes.

## Coverage and limits

Explicitly read root CLAUDE.md (1–135), AGENTS.md (1–60), USER.md; local charter (1–207), UPGRADE_PROTOCOL (1–80); COMPLETION_SPEC (1–93), Runtime mechanics (64–88); READ_CAP rules 1–20 and its consumer/perimeter discussion; READS manifest header 1–106 and all current owned proposed rows/hash snapshot; candidate-v2 spec 56–74. Read complete orphan_check and complete_check source, gate context/schema/snapshot functions 465–562 and relevant selftest case, shared read-cap manifest selection and runtime overlay, PROME attestation-aging consumer, local file-list defaults. Computed only source block sizes/checksums; no final proposed files exist at review time, so no final diff, obligation reconciliation, actual gate receipt, candidate scope, review JSON, commit, publication, or PROME consumption is certified.

Initial combined outputs exceeded a tool-output budget; decisive charter/protocol/runtime/consumer ranges were reread in bounded calls. Search output for prose references truncated after decisive SPEC/blueprint matches, so it is evidence of those references, not an exhaustive citation census. Read-cap source was read in selected consumer ranges, not as a full-code review. No production test or broad guard audit performed. Root/local full-read instruction loading applies to this helper's review scope; full owner boot, sweep execution, inbox disposition and desk closeout remain with the parent.

REVIEW: required — file boundary read by cap/manifest consumers (UPGRADE_PROTOCOL rules4/4a/4b); scope = source charter four sections and retained startup/authority/Git/output, named consumers/ranges above, existing candidate-v2 context contract; reader = `/root/charter_boundary_review`; disposition = QUALIFIED, R1–R6 implementation/verification pending, C1/C8 unsupported-context limitation remains. Final candidate review required; subsequent author changes are POST-REVIEW.

## Follow-up: capture refusal versus receipt UNKNOWN

Parent correctly identified an operational consequence omitted in my first report. Re-read `daedalus_gate.py:522–582,696–718` confirms that `candidate_snapshot` raises on the first nonempty per-step `limitations`; `start_candidate` cannot return a candidate; `run` catches this and prints `CANDIDATE UNKNOWN: ...`, returning rc2 **before the registry loop and before a receipt/GATE_LOG row is written**. The receipt directory/logs directory may already have been created. Thus my statement 'preserve UNKNOWN' must not be read as promising a v2 receipt containing individual UNKNOWN rows. The actual result is refused candidate capture with no v2 receipt and no candidate check execution. The specification's per-step identity wording is broader than this implemented refusal behavior; this review does not authorize changing either.

The parent's revised fallback is appropriate under the inspected canon and the explicitly reported Will publication authorization: save the real refusal output, run the ordinary required closeout registry separately as diagnostic evidence, complete independent final content review, and publish reviewed artifacts with **candidate capture/reuse BLOCKED; candidate assurance UNKNOWN/unavailable; no v2 receipt** prominent. Do not relabel that diagnostic run a candidate run, invent a boundary digest, produce an ACCEPTED candidate review JSON, or substitute legacy identity for candidate acceptance. Preparation/batching may be adopted, while real reuse remains unactivated. The local DEFAULTS one-member alignment remains separately reviewable and does not require altering candidate machinery.

No newly discovered publication prohibition: runner spec §1 separates persistence from check execution; §7's eligibility withholding does not prohibit publishing evidence of a failed attempt. Root Git Protocol still governs publication, and an actual BLOCKING check remains a precondition to claiming a completed closeout. Final independent content review remains required before publication. This follow-up is review of the fallback remedy and executable refusal branch, not final review of the implemented split or frozen publication set.

## Refused candidate capture — raw JSON

```json
{
  "command": [
    "python3",
    "AGENTS/DAEDALUS/scripts/daedalus_gate.py",
    "closeout",
    "--candidate",
    "AGENTS/DAEDALUS/runs/2026-10-09_CHARTER_SPLIT_CANDIDATE_SCOPE.json",
    "--no-superseded",
    "--no-memory",
    "--rule-declared",
    "AGENTS/DAEDALUS/CLAUDE.md"
  ],
  "rc": 2,
  "stdout": "CANDIDATE UNKNOWN: unsupported dependency context for C1: ['orphan_check executes unscoped global git status; existing exact-path context cannot bind all possible top-level untracked paths.']\n",
  "stderr": "",
  "scope": "Final substantive summaries prepared before attempted capture; refusal prevents any v2 receipt/check execution."
}
```

## Ordinary diagnostic battery — raw output, NOT candidate clearance

```text
GATE closeout — DAEDALUS · 20261009T185900Z · HEAD 332d877ca
  ⏰ C0  DUE             sweeps_due (SELF-ROW · DIRECTORY-STALE · cadence)
      ↳ child rc 1 = owed work per its contract
        · ⏰ DUE TODAY: Queue: coordination scorecard weekly render (DOCKET L239) — dated obligation 2026-10-09 (Eastern date; no intraday deadline specified) → design/2026-08-28_coordination_scorecard_v1.md
        · ⏰ DUE: Harness Audit (boot/closeout doc re-test) — last run 94d ago (cadence 90d, +4d over) → sweeps/HARNESS_AUDIT_SWEEP.md
        · ⏰ DUE: Queue: profile-refresh (fired triggers + missing profiles) — last run 22d ago (cadence 21d, +1d over) → UPGRADE_PROTOCOL.md
  ⏰ C1  DUE             orphan_check DAEDALUS
      ↳ 2 self-authored packet(s) uncommitted — commit them (carve-out ①)
        · ⚠️  uncommitted files outside AGENTS/DAEDALUS/:
        · [likely YOURS] PROME/inbox/2026-10-09_from-DAEDALUS_charter-split-owner-apply.md
        · [likely YOURS] PROME/inbox/processed/2026-10-09_from-DAEDALUS_closeout-presentation.md
        · [not yours]    AGENTS/BRENT/research/2026-10-09_pm-prints/CLX26.NYM_1d.csv
        · [not yours]    AGENTS/BRENT/research/2026-10-09_pm-prints/CLX26.NYM_1m.csv
        · [not yours]    AGENTS/BRENT/research/2026-10-09_pm-prints/CLZ26.NYM_1d.csv
        · [not yours]    AGENTS/BRENT/research/2026-10-09_pm-prints/CLZ26.NYM_1m.csv
        · [not yours]    AGENTS/BRENT/research/2026-10-09_pm-prints/HOX26.NYM_1d.csv
        · [not yours]    AGENTS/BRENT/research/2026-10-09_pm-prints/HOX26.NYM_1m.csv
        · [not yours]    AGENTS/BRENT/research/2026-10-09_pm-prints/HOZ26.NYM_1d.csv
        · [not yours]    AGENTS/BRENT/research/2026-10-09_pm-prints/HOZ26.NYM_1m.csv
        · [not yours]    AGENTS/WALTER/registry/x_bookmarks_pending.json
        · [not yours]    PROME/DOCKET.tsv
        · [not yours]    PROME/SCRATCH.md
        · [not yours]    PROME/WILL_QUEUE.md
        · [not yours]    PROME/plans/2026-10-09_heartbeat-29th-rebase-PLAN.md
        · 🔴 THE FLAGGED FILES LOOK LIKE PACKETS YOU AUTHORED.
        · If you do not commit them they never reach the recipient, and the recipient
        · is never told anything was sent. Committing files you authored into another
        · agent's inbox is the ONE sanctioned exception to the pathspec rule.
        · git add <paths> && git commit <paths> -m "DAEDALUS -> <recipient>: <what>"
  — C2  NOT-APPLICABLE  consumer_check (declaration-gated)
      ↳ declared: no figure superseded this session (--no-superseded)
  ⏰ C3  DUE             ledger_staleness --nudge DAEDALUS
      ↳ child rc 1 = owed work per its contract
        · ⚠️  nudge: [DAEDALUS] STATUS moving without ledgers — 4 ledger(s) behind: SURFACES.tsv (45 STATUS-writes behind), PATTERNS.tsv (12 STATUS-writes behind), CHECKS.tsv (6 STATUS-writes behind), FLEET_MAP.tsv (6 STATUS-writes behind) — freeze-or-refresh EACH, or say why not in the commit
  ✅ C4  CLEAN           memory (index-check per slug · length cap)
      ↳ index-check N/A: declared no auto-memory written (--no-memory)
  ✅ C5  CLEAN           claim_check --check weekday
      ↳ no weekday mismatch in 4 paths
  ✅ C6  CLEAN           PATTERNS_HOT conservation (read-only)
      ↳ conservation holds: 187 rows == 54+133 (generated 2026-10-08); NOT checked: whether a row's TEXT changed since generation
  ⏰ C7  DUE             read_cap_check --agent DAEDALUS (rotation DUE; rc1 BLOCKING at closeout)
      ↳ child rc 0; rotation_due=1 — maintenance owed (see paths below)
        · 🟡 CLAUDE.md                            24,961 B    77% of budget  rotate-tier (≥75% of budget)  (whole · DAEDALUS:runtime-boot)
        · ↳ rule 5 STOP is <70% of budget (22,785 B): REMOVE 2,177 MORE B to finish rotating. ⛔ Stopping at the 75% TRIGGER is not finishing — that band re-breaches on the next append (PAT-055 regrowth), which is why rule 5 has two thresholds.
        · ↳ 70–75% BAND — rc 0 and unflagged, and this check CANNOT tell which case you are in: if this surface was JUST ROTATED it is NOT finished and owes 470 B more (rule 5 stops at <70% = 22,785 B); if it has never breached 75%, NOTHING is owed. Only the owner knows. ⚠️ Headroom to the trigger: 1,158 B.
        · ℹ️  READ-CAP ADVISORY [DAEDALUS]: 1 reading(s) this check will NOT adjudicate (above). ⛔ These do NOT affect rc — the declaration is the reader's, and a refusal to adjudicate cannot be a blocking verdict (severity split 2026-09-14, L354).
        · READ-CAP [DAEDALUS] — cap 54,250 B · budget 32,550 B (60%) · ALL % BELOW ARE OF BUDGET (the number every verdict grades; ≥100% = over) · perimeter: DECLARED in PROME/registry/READS.tsv — 14 cap-bearing (whole/programmatic) measured, 12 declared-not-counted (scoped/grep/summary), 43 manifest row(s) for this desk; 4 of the measured are MEMBERS of 2 cap-bearing CLASS row(s), each measured per member (rule 16); ATTESTED by the desk itself
        · ▣ AGENTS/DAEDALUS/inbox/*.md                   declared `whole` · CLASS row — cap-bearing PER MEMBER (rule 16 ruling 2026-09-24): 4 member(s) measured, 0 over budget, 0 over the CAP, largest 3,035 B (9% of budget)  (DAEDALUS:CLAUDE.md-SPAWN-3b)
        · READ-CAP-RESULT v1 mode=agent rc=0 assessed=1 desk=DAEDALUS reads=14 over_budget=0 over_cap=0 manifest_defects=0 advisories=1 generated_flagged=0 rotation_due=1 active_decisions_over_budget=0 charter_mode=explicit charter_reads=2 charter_bytes=20200
  ✅ C8  CLEAN           complete_check (pairing · pair-symmetry · EVOLUTION placement · claim walk-list)
      ↳ child rc 0
        · · CLAIM AGENTS/DAEDALUS/design/2026-10-09_BOOT_RELIABILITY_PASS.md:18: Review: independent thread-local read-only helper `boot_blind_review` (fresh context; exact inherited model identifier UNKNOWN), blind repor
        · · CLAIM AGENTS/DAEDALUS/design/2026-10-09_BOOT_RELIABILITY_PASS.md:10: | B02 | Charter describes bounded chunks, both output budgets, final-line coverage and honest limitations in existing boot notes | Root CLAU
  ✅ C9  CLEAN           STATUS stamped today (header + BOTTOM LINE)
      ↳ header and BOTTOM LINE both stamped today
  ✍️  C10 DECLARED        rule-declared-this-session (judgment, DECLARED only)
      ↳ operator declares a rule was declared/amended at AGENTS/DAEDALUS/CLAUDE.md — RE-READ it before closing (not machine-checked)

GATE closeout rc=0 · checked: 10 steps ['C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'] · NOT checked (declared/enumerated only): ['C10'] · proves nothing about: completion of work beyond complete_check's legs, owner consumption of packets, the truth of any DECLARED value, or anything a child's own PASS line disclaims.
  counts: CLEAN 5 · DECLARED 1 · DUE 4 · NOT-APPLICABLE 1
  receipt: /tmp/claude-1000/daedalus-gate/20261009T185900Z_closeout.json (sha dfb56b92) — fingerprint f1164da1df49
  logged: /home/willi/Research-workspace/AGENTS/DAEDALUS/runs/GATE_LOG.tsv (the only tree write this runner makes)
```

## Final independent content review — verbatim

# Charter split — independent final content review — 2026-10-09

Reader: `/root/charter_boundary_review`, thread-local OpenAI Codex helper; exact model variant/session ID unavailable beyond task identity. Repository `/home/willi/Research-workspace`. Scope is independent content/consumer review for publication, **not candidate-v2 acceptance**. Root/local authority, review rules4/4a/4b, READ_CAP rules and candidate spec were read during the initial remedy review; implementation and evidence reread here. Only this report written, under `/tmp`; no repository mutation or owner messaging.

## Disposition

**Content accepted for the authorized publication, with the disclosed operating limits retained. No further content repair is required in the reviewed bytes.** One required packet correction was applied POST-REVIEW and independently rechecked below. All four moved blocks are conserved; mandatory boot read and addressable section redirects preserve active obligations; local checker alignment is exactly one member addition and passes independent clean/capable controls. The proposed shared manifest is compatible; actual owner application remains pending.

**Candidate capture/reuse remains BLOCKED, candidate assurance unavailable/UNKNOWN.** No v2 receipt exists for this attempt. Ordinary diagnostic rc0 is historical check evidence only. This report does not issue a candidate-accepted JSON, candidate boundary digest, commit/push assurance, owner-consumption receipt or whole-closeout clearance.

## Evidence and remedy reconciliation

| Initial item | Final finding |
|---|---|
| R1 active rules/read path | PASS. SPAWN0 requires OPERATIONS whole at every boot before any task. Companion header calls it active, mandatory, same authority; it does not call it archive/cold/on-demand. All desk-relative paths retain their directory base. |
| R2 addressable references | PASS. Original THE JOBS, MATURITY LADDER (per-class), MEMORY MODEL (your learning), FILES level-two headings remain in CLAUDE with matching OPERATIONS section destinations. Original long Job5 subheading remains with its mandatory procedure redirect. SPEC/market-blueprint canonical section references still resolve through those stubs. Companion explicitly sends AUTHORITY/SPAWN/GIT/OUTPUT references to CLAUDE. |
| R3 READS perimeter | PASS as a proposed delta; **live application pending**. Three delta rows are READ whole, BASIS boot-defining, and owner ATTESTATION replacement. Packet instructs PROME to add only the two new rows, replace only DAEDALUS attestation and preserve all others. Live register independently contains zero OPERATIONS rows at review time. |
| R4 identity/date evidence | PASS within stated limits. Charter and companion hashes match actual bytes. Other hash entries explicitly remain historical snapshots. No precommit-history finding is suppressed. Owner application/publication are not inferred from file existence or a hash. |
| R5 local consumer | PASS. Actual source diff is exactly the one OPERATIONS entry in DEFAULTS. Original five members and all thresholds/control flow remain unchanged. Independently imported module confirms exactly one OPERATIONS member, six total. Independent fixture runs: 1,024 B named OPERATIONS => rc0, clean; 32,551 B => rc1, named OPERATIONS, TRIM1 B. Both classified MANDATED READ. |
| R6 preservation/cost/obligations | PASS. Four blocks match original bytes exactly once in companion; retained IDENTITY/AUTHORITY/GIT/OUTPUT/BOTTOM LINE sections are byte-identical. Split record carries block sizes/CRCs, duty-before/destination-after table and total cost +1,935 B. Companion gives split date and append-size re-trigger; synthesis adds closeout measurement. No budget increase or stranded off-path rule. |

Original source independently loaded from `a218c4e1480856621ea9c3340e64cb95aa1bceeb:AGENTS/DAEDALUS/CLAUDE.md`; 35,698 B, SHA256 `1e28df1328c3a6dfa9de902bdc658cf3373f56f8ee2a24bb8cd9163df663f3c5`. Extraction before each level-two heading, including trailing separators/whitespace:

| Block | Preserved bytes | Recomputed CRC32 | Exact occurrences in companion |
|---|---:|---|---:|
| THE JOBS | 5932 | 2148a999 | 1 |
| MATURITY LADDER (per-class) | 3080 | aebde880 | 1 |
| MEMORY MODEL (your learning) | 5462 | 7c035b89 | 1 |
| FILES | 2367 | 38b04595 | 1 |

Resulting whole reads: CLAUDE20,200 B; OPERATIONS17,433 B; total37,633 B. Each is below22,785 B. Increased combined context cost is expressly disclosed. The separate root CLAUDE rotation debt is retained; no claim that this owner split fixed it.

Obligation audit: build approval/registration, structure-change permission and idle guard, three sweep modes/limits, maturity/directory regeneration, heavy-agent profile preparation, retirement approval, five private-zone rules, all class floor/ceiling conditions including ratified A/B and held-L4 10/15 check, per-leg review, patterns/dedup/contradiction duties, current-state/history separation, generated-directory restrictions, ownership/register updates and source-navigation duties all remain in their exact blocks on the mandatory path. Retained root/runtime reads, Git/review safeguards, output rules and closeout obligations remain in CLAUDE. The only intentional instruction changes outside the move are SPAWN0 and authorized preparation/batching/reuse wording in SPAWN9. The latter keeps required input validity, recapture/review, and UNKNOWN rather than a waiver.

## Independent consumer checks

I constructed a temporary test manifest from the live register, retaining all rows except DAEDALUS's attestation, then added the exact three-row delta. Ran root read_cap_check with `--agent DAEDALUS --charter-mode explicit --require-manifest --reads-path <temporary-file>`:

```text
TEST ONLY: rc0; OPERATIONS17,433 B measured as whole at SPAWN0.
READ-CAP-RESULT v1 mode=agent rc=0 assessed=1 desk=DAEDALUS reads=15 over_budget=0 over_cap=0 manifest_defects=0 advisories=1 generated_flagged=0 rotation_due=1 active_decisions_over_budget=0 charter_mode=explicit charter_reads=2 charter_bytes=20200
```

This establishes compatibility of this proposed manifest with the current reader. It is **not a live-registry verdict**. Root rotation_due1 remains. Actual live manifest has43 DAEDALUS rows; merged test has45 because two rows are added and one replaced.

I independently called unchanged `start_candidate` against the saved provisional scope in a temporary receipt directory. It raised:

```text
unsupported dependency context for C1: ['orphan_check executes unscoped global git status; existing exact-path context cannot bind all possible top-level untracked paths.']
```

This reproduces the recorded CLI refusal premise. Code reviewed previously shows `run` catches this, prints CANDIDATE UNKNOWN and returns2 before the registry loop/receipt/GATE_LOG. The scope purpose and every completeness statement explicitly deny complete input assurance; it is a refusal reproduction, not an activated boundary. C8 has its own unsupported global-history limitation, not reached because C1 refuses first. The saved raw CLI record therefore properly reports only C1's observed refusal, while explaining the independently identified C8 limitation.

Reviewed ordinary185900Z diagnostic output and its single GATE_LOG addition: rc0, C0/C1/C3/C7 DUE; C4/C5/C6/C8/C9 CLEAN; C2 NOT-APPLICABLE; C10 DECLARED. Its C7 perimeter omitted OPERATIONS pending the owner delta. Synthesis explicitly names that omission and states the receipt became historical after evidence edits. I did not rerun the whole battery or certify its current reuse. The earlier self-authored processed packet appearing under C1 is a heuristic output, not permission to edit PROME's working files; publication remains exact-path and subject to actual ownership/Git safeguards.

## POST-REVIEW correction

The first frozen recipient packet said the candidate-v2 workflow was 'being applied' and that a final candidate review would follow; this understated the pre-check capture refusal. I required the caveat in the packet itself, consistent with root anti-laundering and the synthesis/STATUS. Parent corrected only that packet and updated its frozen hash. I reread the full corrected packet and recomputed the hash:

`df821fc4141d21a60db92a3ac09d2f7a923c00731e61c32829c501219b3e4621`

It now says preparation/batching adopted, capture/reuse BLOCKED before checks or receipt, no candidate assurance, and final independent **content** review/publication evidence follows. **Repair accepted after independent recheck.** Its remaining initial-review/pending-publication wording describes the packet's preparation-time state and is superseded by this separately identified final content report; it does not claim candidate clearance.

## Frozen content identities

All11 files matched the updated `/tmp/daedalus-split-review-freeze.json` at the final check. These are file identity hashes, **not a candidate boundary digest**.

| Path | SHA256 |
|---|---|
| AGENTS/DAEDALUS/CLAUDE.md | 72eb4aa54ffb6f8731c7adcf63be82c23fd4be3a1af734937b7d5e93017e3656 |
| AGENTS/DAEDALUS/OPERATIONS.md | a4082fc62b903cc26b1866c943503ec127ee7ccd8e6037e52349d4ed320a940d |
| AGENTS/DAEDALUS/EVOLUTION.md | ff48d4b8b7658b20b119f321343d6c0915311a3fbde8d5c8be7952fc7cf653ce |
| AGENTS/DAEDALUS/STATUS.md | 24b56c7a5554936c862d33a62c8856ce3b3b703f88948768a3efacb5a3641fa8 |
| AGENTS/DAEDALUS/scripts/read_cap_check.py | fbb4262b824c401699781b246dfa7c360582a11987a94a73dd53ba8fd367040c |
| AGENTS/DAEDALUS/registry/basis-hashes.json | 577d710562927c5be6d5a06fe213c8a18d715d0b099f784fd076e158c97c5c97 |
| AGENTS/DAEDALUS/registry/2026-10-09_READS_SPLIT_DELTA.tsv | 3dca3b47e1a4d7fd1853bfed1605a29d092db9f008b93078717a40737fbdc430 |
| AGENTS/DAEDALUS/runs/2026-10-09_CHARTER_SPLIT.md | fad52bb4e6a43a5900ac7c67ce3af093b4c02c588c2ffb28a2a20b918deaea6e |
| AGENTS/DAEDALUS/runs/2026-10-09_CHARTER_SPLIT_CANDIDATE_SCOPE.json | 0b2238744d3fad2cb4c52204c06cc21f4da8a0c65b412bab003bff863befc5bf |
| PROME/inbox/2026-10-09_from-DAEDALUS_charter-split-owner-apply.md | df821fc4141d21a60db92a3ac09d2f7a923c00731e61c32829c501219b3e4621 |
| AGENTS/DAEDALUS/runs/2026-10-09_CHARTER_SPLIT_READER_REPORTS.md | 8c5d925d816ad9362a62014bb87a59f8fa438c163788e8593d0102bab0d5b1a5 |

The final report may be appended verbatim to the evidence companion as the specifically anticipated review-evidence addition; the table's companion hash remains its **pre-append reviewed basis**, never the final composite's hash. That mechanical append neither expands review scope nor creates candidate assurance. Any other substantive edit after this report requires applicable follow-up and POST-REVIEW disclosure.

## Counterexample and limits

Counterexample that would defeat my positive preservation finding: leave OPERATIONS off the mandatory boot path or alter one live rule while keeping both byte sizes green. Neither occurs in the reviewed bytes. Counterexample that defeats a stronger 'shared coverage complete' claim already exists: live manifest has no OPERATIONS rows, despite a clean proposed-manifest test. This is why owner application remains open. A new top-level untracked file/global-history commit remains the counterexample to a falsely complete named-path candidate scope; refusing capture preserves that limitation rather than clearing it.

Coverage: actual changed hunks for six tracked owned files plus diagnostic GATE_LOG, complete new companion blocks via source byte comparison and initial semantic read, full new delta/owner packet/synthesis/provisional scope/evidence companion, current full CLAUDE in bounded ranges, current changed STATUS/EVOLUTION text with unchanged regions excluded from new semantic certification, exact final file identities, independent member controls and merged-manifest compatibility, independently reproduced start_candidate refusal. Initial combined diff output truncated within already reviewed moved/deleted text; I recovered decisive retained/new charter ranges and smaller non-charter diffs. Initial raw remedy report is present verbatim in the evidence companion (byte containment independently checked).

Not read/certified: entire repository citation population; every old STATUS/EVOLUTION assertion; full checker source outside relevant unchanged consumer ranges; all per-step dependencies (scope expressly provisional); actual Will conversation beyond delegated authorization; current content of unrelated pending inbox tasks; PROME receipt/application; eventual commit/tree/origin membership. No new sweep, grade, maintenance reset, root compaction or candidate-engine change reviewed or authorized. Publication can proceed under the parent's recorded explicit Will authorization and root Git safeguards, but remains separate from candidate eligibility and completed closeout.

REVIEW: required — file-boundary/read-perimeter change under UPGRADE_PROTOCOL4/4a/4b; scope = frozen11 files as detailed, exact DEFAULTS addition and listed consumers, plus diagnostic GATE_LOG row; reader = /root/charter_boundary_review; disposition = APPLIED6 initial remedy items and1 POST-REVIEW packet correction; RESIDUE2 disclosed operating limits (PROME live application pending; candidate capture/reuse BLOCKED). **Content accepted for publication; candidate assurance UNKNOWN/unavailable.**
