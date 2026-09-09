# PROME sweep #2 — spine and mirror reader

Date: 2026-09-08. Reader: DAEDALUS bounded sub-reader, read-only against PROME. Assignment: `sweeps/PROME_SWEEP.md` judgment tail, spine/mirror half. Parent synthesizes the ruling and any delivery packet. This reader changed only this report; no PROME edits, peer messages, commits, network checks, or mutating gate execution.

## Verdict

**The L5 zero-unexecuted-own-rule leg is NOT satisfied by this read.** This is not a claim that every control failed. Two current documentation defects remain, and independently the window includes admitted departures from the mandatory commit wrapper, skipped closeout, and a late autonomy-grant log. A current-only test still finds the CLOSEOUT stamp omission below; a full-window test additionally includes the execution failures. Script-family execution cannot substitute for the registered judgment test (`sweeps/PROME_SWEEP.md:16,24,31-32`). Parent owns the grade; no fleet row was changed here.

**No URGENT finding in this half.** The largest execution failures below were already owned and repaired or folded into later closeouts. Do not send them back as undiscovered open bugs. The meaningful current repair is to make the commit cookbook agree with the mandatory wrapper procedure, and cover the actual CLOSEOUT change in its scope stamp.

## Window and evidence method

- Initial read-time HEAD: `0bd18ddf93fd6ac24b7cacd54abfe6b2a640a1d2`. PROME's relevant tracked spine files were clean; one unrelated OSPREY-to-PROME inbox packet was untracked. Other agents are active, so this is a bounded read-time assessment, not a locked-tree audit.
- Sizing command: `git log --since=2026-08-17 --format='%h' -- PROME/` yielded 1,208 commits. This is the log query's window, not a claim that all 1,208 commits were read.
- Scoped diff baseline: `e7082c633108aee9a200c81db90321909e8c89d8` (last commit before 2026-08-18). `git diff --stat <baseline> HEAD -- CLAUDE.md PROME/BOOT.md PROME/CLOSEOUT.md PROME/COMPLETION_SPEC.md PROME/AUTONOMY.md PROME/HANDOFF.md PROME/CLAUDE.md PROME/SYSTEM.md`: eight files, 242 inserted / 167 removed lines. These are git diff statistics, not current file-size receipts.
- Read the current profile and sweep contract, root `AGENTS.md`/`CLAUDE.md`, all seven assigned PROME spine files, both runner indexes, the Git cookbook, scoped owner/mirror excerpts, and selected 9/3–9/7 execution records. Read root-canon commit history since the targeted 8/17 pass.
- Confidence: **VERIFIED** below means the named bytes/history were inspected. Self-reported execution is labeled as such: seeing a confession proves the durable record says it, not a reconstructed shell transcript. **INFERRED** is interpretation; **UNKNOWN** identifies a limit. Large log/grep outputs were sometimes truncated; no absence claim relies on them.

## Ranked current findings — five-field assertion records

### S1 — STANDARD: the commit cookbook still advertises bypassable raw-git recipes

**Claim — VERIFIED documentation divergence; INFERRED recurrence path.** CLOSEOUT makes the intent wrapper mandatory for every PROME commit. Its named cookbook continues to show bare `git commit` recipes and describes them as remaining valid. That leaves a reader two incompatible levels of prescription.

**Exact artifact:**

- `PROME/CLOSEOUT.md:120`: “every commit goes through the intent-checked wrapper.” `:121`: “the wrapper form above is the only commit form.”
- `PROME/CLAUDE.md:70` points to `PROME/GIT_COORDINATION.md` for exact recipes; `PROME/BOOT.md:89` also sends a committer there.
- `PROME/GIT_COORDINATION.md:90` says wrapper is the default/checked path but “The recipes below remain valid as the underlying git.” `:49-58`, `:99-114` show plain `git commit -m ... -- <paths>`. `:16` calls inline `-m` examples subject-line shorthand; that explains message quoting, not bypassing the intent manifest.
- Durable recurrence: `memory/2026-09-03.md:38` owns bare `git commit -F` all evening; `memory/2026-09-06.md:21` error #111 owns sixteen raw commits and says wrapper resumed at L296. `PROME/CLOSEOUT.md:121` repeats the sixteen-commit admission.

**Verification command:** bounded `nl -ba` reads of those ranges; `git show bb7af2869 -- PROME/CLOSEOUT.md`; read `PROME/tools/commit_check.py:20-35` for the wrapper's actual purpose.

**Observed result:** the wrapper buys a pre-commit intended-path manifest and post-commit verification; plain git preserves root pathspec safety but does not provide those PROME-required checks. The on-file bypass warnings are real. Whether the cookbook caused the actual bypasses is **INFERRED**, not established by a transcript.

**Proposed change:** replace PROME cookbook runnable raw-commit examples with the existing wrapper form, or reduce them to a single pointer to CLOSEOUT. Keep any low-level explanatory git example explicitly non-procedural. Do not add another approval gate or redesign fleet git rules. This is a PROME-local instruction reconciliation.

### S2 — STANDARD, small fix: CLOSEOUT's scope stamp again omits a later rule-add

**Claim — VERIFIED.** CLOSEOUT carries an operative 9/6 subject-drafting/stop rule under a 9/5 update manifest that does not cover it. This is the same own-rule-unexecuted class counted in sweep #1, not an age-only complaint.

**Exact artifact:**

- `PROME/CLOSEOUT.md:3` latest `Updated:` is 2026-09-05, with the covered changes enumerated.
- `:88` owns the scope-manifest stamp rule. `:121` introduces the 2026-09-06 ≤70-character drafting target, pre-wrapper measurement, ≥101 stop-and-rewrite, and wrapper-only clarification.
- `bb7af2869a0c490fdadbe0089f2ef0a33c605db3`, committed 2026-09-06 11:30:29 −04:00, adds that rule line and leaves the header untouched. It is still the latest commit touching CLOSEOUT at this read.

**Verification command:** `git show bb7af2869 -- PROME/CLOSEOUT.md`; bounded numbered read of `:3,:88,:120-121`; `git log -1 -- PROME/CLOSEOUT.md`.

**Observed result:** the material process add is dated locally, so its adoption is recoverable; the whole-file manifest nevertheless under-describes its body. The 9/5 header explicitly repairs the prior 9/3 stop-rule ride-under, making this a recurrence after that repair.

**Proposed change:** reconcile the one header to cover the 9/6 addition. Prefer a concise scope statement; do not grow another chronology or add a checker for a semantic stamp assertion. Count this once, not separately as a stale-stamp and a mirror defect.

## Window execution findings — already owned; do not reopen as new tickets

| Item | Rule and inspected evidence | Status and bearing on L5 |
|---|---|---|
| W1 Mandatory wrapper bypass | CLOSEOUT `:120` dates the mandatory wrapper to 8/29. `memory/2026-09-03.md:38` owns the evening bypass; `memory/2026-09-06.md:21` error #111 owns sixteen further raw commits, “wrapper from the L296 commit on.” `bb7af2869` adds the warning to the manual. | **VERIFIED self-report**, not independently reconstructed sixteen-command history. The record says remedied from L296; continuous later compliance **UNKNOWN**. The recurrence prevents treating a written rule as proof it executed. S1 is the remaining instruction ambiguity. |
| W2 Session ended without closeout | CLOSEOUT `:14,29-32` requires closeout for durable changes and Standard minimum at day end. `memory/2026-09-03.md:18` says afternoon session ended without closeout, leaving morning continuity over nine rulings/deliveries for eleven hours. `:38` records the later evening closeout. The profile's T2/T4 also names the lapse. | **VERIFIED self-report and later repair record.** The lapse is in-window and already repaired; not a claim that today's HANDOFF is stale. No inference that every abrupt runtime exit can be prevented. |
| W3 Gate C autonomy log late | AUTONOMY `:75` and CLOSEOUT `:81,113` require the grant log plus boot-visible propagation. AUTONOMY `:95` records the 8/27 Gate C custody grant but explicitly says logged 9/6; `981312f45` lands that row. Root grant already existed in `79b21e499` / `d97cbca3b`; SYSTEM's mirror row existed before the log entry. | **VERIFIED repaired logging lapse.** Root canon was auto-loaded, so this was NOT proof PROME lacked custody instructions or exceeded custody. The new row is present now. Do not demand a second detailed Kernel rule in PROME/CLAUDE when root canon already carries it. |
| W4 GATE-LIQ-079 state-length breach | Profile `PROME.md` §5 and `memory/2026-09-03.md:33` record 350 characters against the ≤220 state-cell contract, expressly adjudicated a breach. The profile records the trim and archived history. `prome_gate.py:149-181` checks token/state/consumer/review families, with no state-cell length enforcement in that function. | **VERIFIED admission/current checker excerpt; historical 350-character count not remeasured here.** Treat as known repaired instance and retain in window evidence. Lack of a script is not by itself an unexecuted rule; a new universal length guard would be mechanical follow-up, outside this judgment read. |
| W5 Measurement claim uncertainty | PROME profile §5 and `memory/2026-09-03.md:18,33` distinguish the alleged pre-rotation HEARTBEAT size from committed HEAD. `PROME/CLAUDE.md:76` requires measure.py for reported byte/line/crc receipts. | **UNKNOWN** whether the transient measurement existed and used the required source. Do not infer fabrication from failure to match a committed vintage, and do not add this uncertain instance to an exact failure count. Independent W1–W3 already answer the L5 question. |

## Mirror walk and root-canon delta coverage

The map at `PROME/SYSTEM.md:56-68` has eleven fact rows. Coverage is stated per row; this is not a claim to have replayed every historical consumer.

| Map row | Owner/mirror meaning checked | Result / limits |
|---|---|---|
| Gate C custody / ④ (`:58`) | Root Git Protocol ④ + separate custody paragraph vs GIT_COORDINATION `:36-43`, AUTONOMY `:95`, CLOSEOUT `:155`. | **Agrees now:** submission-only desk grant; distinct PROME acceptance custody; activation bounded; additions-only / exact paths. KERNEL runbooks/activation artifacts were located but not individually replayed; historical activations/revocations and custody execution are **out of scope**. W3 is log delay, not an authorization failure. |
| Root provenance (`:59`) | Root header points to `docs/CANON_PROVENANCE.md`; 8/29 `7e94f91f4` preserves rules and moves reasons; SYSTEM row and CLOSEOUT `:110` retain the walk. | Pointer architecture agrees. Did not re-run every provenance-key invariant of the restructuring. |
| Git protocol (`:60`) | Root current Git Protocol vs PROME/CLAUDE `:70`, BOOT `:15-25`, GIT_COORDINATION `:117-128`, CLOSEOUT `:21,120-146`, AUTONOMY `:6`. | Pathspec, no-amend, ff-only push, exact push receipt, overlap-check-before-autostash and escalation meaning agree. S1 remains for the stricter PROME wrapper; not a root pathspec violation. Auto-memory mirror file not independently read this pass. |
| Machine model (`:61`) | Root / PROME/CLAUDE identity / SYSTEM runtime / scoped machine and historical-prep references. | Same serial desktop↔laptop, one box at a time model. No machine-inventory or hook-runtime certification. Historical OpenClaw narratives are not operative alternatives. |
| HY watch (`:62`) | SYSTEM `:202`, STATUS HY row, ACTIVE_DECISIONS credit-watch rows, HEARTBEAT current threshold prose; config.py and LIQUID KILL_MEMO owner excerpts; local intake `fetch_fred.py:70-80`. | **Boundary ambiguity retained for owner review, not silently corrected:** SYSTEM/config/KILL_MEMO say `>280`; intake alert actually fires `>=280`; ACTIVE_DECISIONS `:39` explicitly says the `>` form is retired on that surface and uses `≥280`. Sustain judgment remains LIQUID-owned. Thus SYSTEM agrees with two named owner documents yet differs from the primary alert and current coordination view. This is not evidence to choose a new operator, declare an actual missed fire, or count a second L5 failure. The 280.0 boundary would distinguish the meanings. Parent may fold this into existing threshold-owner work. |
| Position truth (`:63`) | Root position paragraph vs FORGE/STATUS header, SYSTEM `:195,206`, action-cards/TEMPLATE `:11`, bank-put proposal `:4-6`, ACTIVE_DECISIONS. | Consistent off-repo Will/broker truth, FORGE dated account-scoped mirror, PORTFOLIO frozen history. Old proposal figures are explicitly stale/rebuild-required; not a fresh-book defect. No broker/price verification attempted. |
| Roster (`:64`) | Current ROSTER owner paragraph `:8,33`, root roster pointer, AGENTS.md routing/table-retirement text; scoped navigation reads. | Root membership duplication retired by WQ-120 and AGENTS table retired by WQ-128. SYSTEM still labels AGENTS.md “table + run-model note” although table is gone: **navigation residue**, not a rival roster. Did not census every README/_INDEX/_NETWORK membership row. YEYOU's root exception remains pending an explicitly recorded WQ-150 root batch; the live ROSTER and GIT_COORDINATION retirement banner forbid launch. Do not re-open bannered historical YEYOU recipes as active instructions. |
| Forward catalysts (`:65`) | DOCKET owner / SCRATCH generated-view design / retirement of HEARTBEAT Near-Gates and STATUS NBA. BOOT `:80` and CLOSEOUT `:51` retain generic “HEARTBEAT gates/views” phrasing. | Current map accurately marks both retired mirrors. Generic older references are **low-impact navigation residue**; they do not authorize recreating the retired Near-Gates section. Full row grades/dates belong to the other reader. |
| Fire ledger (`:66`) | Current map now names GATES, GATES_README, owner letters, coordination views; added 9/6. | Map omission from the prior profile is repaired. No all-row grade/content validation in this half. |
| Will queue (`:67`) | Current SYSTEM row says generated Pending-Will, HANDOFF dated history. `bb7af2869` adds `willq_view`; prome_gate `:676-680,717-721` runs drift check with write remedy. | Generated-view adoption is real. HANDOFF's old open-items lists are explicitly dated history, not independently current queues; do not count closed historical items as stale-live. Did not execute `--write` or test live publisher output. |
| Trigger bands (`:68`) | config.py / KILL_MEMO / intake local source as above. | Same precise-boundary ambiguity as HY watch, **one candidate only**. Archived skill trigger mirrors explicitly retired. No external intake fetch or deployment freshness verification. |

Root changes sampled by commit: `cd7c04bb0`/`897d32500` potash triage (FERT owner; no UNOWNED reconstruction); `a719b5f05`/`326181484` ledger-nudge and same-figure consumer semantics; `689f8bd0f` no-amend; `073cb7e6f` dark-owner rule pointer; `c2cbe189f` HEARTBEAT/FORGE grants; `d97cbca3b`/`79b21e499` Kernel custody; `e5b31fbfa` 32,550-byte read-cap basis; `6704cfc37` sole PROME inbox; `7e94f91f4` rules/provenance split; `a284c86bd`/`0843ee3a1` exclusions, topology pointer and activation wording; `cde782fed` no-pathspec commit hazard; `60994163d` subject limit. This is a semantic sample against current mirrors, not a full implementation audit of each ruling.

## Runner and execution positives

- `PROME/.claude/skills/boot/SKILL.md` now carries USER, owner-order reads with GATES, boot memories, HEARTBEAT, the one-shot gate, conditional reads and issue/proposal steps. Its alternate ordering is explicit and defers to BOOT. The mechanical gate was not executed by this reader because it advances the BOARD cursor.
- The closeout runner reaches HEARTBEAT write-back, both pages, trigger-gated residuals, the final gate **after** writes/regeneration, and the wrapper. This closes the prior missing-heartbeat-step class at the instruction artifact. Actual prompt-by-prompt execution remains **UNKNOWN** without runtime transcripts.
- `COMPLETION_SPEC.md:10,54,58` now makes PROME/inbox the mandatory durable delivery home, registers WILL_NEEDS in WILL_QUEUE, and preserves Tier 2 for priority-changing routes. The 9/6 processed-directory/commit-time rider is a response to an observed consumer failure, not a missing requirement.
- AUTONOMY `:24,93,96` and PROME/CLAUDE `:61-68,83` now agree about due-row Tier-1 desk work, same-minute presence preflight, whole-inbox drain, and trade/spend exceptions. `memory/2026-09-06.md` and HANDOFF `:35-36` record the first dark-row BRENT spawn and live-owner doorbells. That is positive execution evidence, not proof of all future boots.
- HANDOFF currently carries five dated entries and a single archive pointer, consistent with CLOSEOUT `:99` and PROME/CLAUDE `:90`. No missing-closeout finding is inferred from ordinary historical open-item lists.

## False positives and limits to carry into synthesis

1. **MANUAL green rows are not witnessed execution.** `prome_gate.py:728-733` passes literal `True` when printing manual memory/consumer reminders. The source and CLOSEOUT `:36` explicitly say these are manual. Do not cite their green output as proof those steps ran; equally, that source alone does not establish they were skipped.
2. **The three-old-mirror rule is not a blanket demand for more tooling.** Map `:51` requires generation/countless pointers for a thrice-rotted hand mirror. Current generated SCRATCH blocks and retired root lists honor that principle. This read recommends reducing the duplicate cookbook procedure; it does not commission a new gate.
3. **Stale history is not stale live state.** Explicitly dated HANDOFF lists, YEYOU's VOID recipe block, the historical 8/9 map census with its 9/6 disclaimer, and the frozen bank-put input tables were not counted as active defects.
4. **Exact full-window zero is not establishable from git alone.** A commit does not show whether ListAgents ran in the same minute, the gate ran last, each reader stayed blind, pages were republished to the recorded URL, or every actor received its final release. `commit_check.py:33` says its manifest is clone-local, never committed. This read used positive admissions/artifacts, not absence of transcript as proof of failure.
5. **No repeated mechanical core.** No boot/closeout gate, external market script, mutations, or live Artifact publish/fetch. Dashboard/HEARTBEAT content, re-base consumer checks and disposition write-backs are primarily the companion reader's scope; this report makes no claim those halves passed.
6. **Reviewable action:** parent can route S1/S2 as a small PROME-owned reconcile and record the in-window execution verdict. The repaired W1–W4 evidence should remain in the grade rationale, not become duplicate inbox work. No new authority or approval requirement is proposed.

## COMPLETION — DAEDALUS spine reader — 2026-09-08
STATUS: ✅ DONE
CHANGED: AGENTS/DAEDALUS/upgrades/PROME_SWEEP_2026-09-08_SPINE_READER.md
RESULT: Read seven spine files, both runners, eleven mirror-map rows at stated depth, and the root-canon change window; found two current documentation defects plus already-owned execution lapses. L5 zero-own-rule-unexecuted leg not satisfied.
GAPS: Runtime command/presence/publication execution cannot be reconstructed from tracked files; KERNEL activations and all roster mirrors were not individually replayed.
WILL_NEEDS: None from this bounded reader; parent owns grading and delivery.
FOLLOW-UP: Parent synthesizes companion reader, routes current S1/S2, and preserves the repaired-vs-current distinction.
