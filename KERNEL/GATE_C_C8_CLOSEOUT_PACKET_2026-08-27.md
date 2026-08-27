# Gate C C8 Closeout Packet — the first live shadow pilot

**Prepared:** 2026-08-27 ~16:5xZ, inside the window, by PROME (writer/builder — **NOT the C8 reviewer**; reviewer = RED or DAEDALUS per the 2026-08-26 ruling, Will picks).
**State:** DRAFT FOR C8 REVIEW — nothing here is self-graded; every claim cites a commit, a tool transcript line, or a Will ruling.
**Activation:** `LIVE-2026-0001` (`KERNEL/GATE_C_C7_ACTIVATION_2026-08-27.json`), window **[2026-08-27T16:30:00Z, 18:00:00Z)**, Will-ruled in-session (record: `PROME/proposals/2026-08-27_c7-pilot-window-RULED.md`, committed `d68a0736b`). Day-boundary rider: waived by Will in-session 2026-08-27 AM (supersedes packet v2's "earliest ruling date 2026-08-28" line — the rider was his to waive and he waived it before selecting the window).

## 1. Results

- **2 events accepted** (the entire authorized perimeter, nothing more):
  - `KERNEL/shadow/events/2026/08/EVT-019305f8-ec00-7000-8000-000000000033.json` (RegisterQuestion, SAM-33)
  - `KERNEL/shadow/events/2026/08/EVT-019305f8-ec00-7000-8000-000000000034.json` (SubmitForecast, SAM-33)
- **4 registered views rendered** (CALIBRATION.tsv · EXCEPTIONS.md · OPEN_QUESTIONS.md · RESOLUTION_QUEUE.md), committed `render_as_of=2026-08-27T16:32:47.037821Z`.
- **0 rejected receipts** — no command refused at apply.
- **Kernel commit:** `01478b659`, exactly the six operator-staging paths the tool printed, staged path-by-path. **Not pushed** (push = Will's word only).

## 2. Timeline (all stamps from tool output / `git log`, not narrative)

| UTC | Step | Record |
|---|---|---|
| ~16:16 | Will's go word ("can we just do the pilot now?"), window selected [16:30, 18:00) | `d68a0736b` |
| 16:23 | Step 0: 6 hashes byte-exact, staged empty, custody paths clean; tree deviation put to Will → **PROCEED** | same record |
| 16:29:01 / 16:29:48 | SAM's first two attempts **HALTED by its own window guard** (pre-16:30) | SAM report |
| 16:30:23 | Step 1: SAM's submission commit, 2 files, dest-hashes pin-exact, in-window | `bb606994a` |
| 16:31:18 | Step 2: activation minted; byte-diff vs draft = window fields only | `2eacbeba7` |
| 16:31:23 | **Step 3 first preflight: REFUSED** `LIVE_ACTIVATION_INVALID $.window_start` (non-canonical timestamp — see Discrepancy D2) | transcript |
| 16:32:10 | Correction committed (`.000000` micros; instants unchanged); **preflight PASS rc=0**, 0 writes | `cb8979041` = **BASE** |
| 16:32:16 | Step 5 apply: **all checks PASS**, 2 events + 4 views written, staging list printed | transcript |
| 16:32:25 | Step 6 retry rc=0: **events byte-identical; views differ by `render_as_of` only** → stop condition (D3) | transcript |
| 16:32:47 | Diagnostic third apply (D3 isolation: diff = 1 line/view, the stamp) | scratchpad diff |
| ~16:35 | D3 put to Will → **PROCEED to 7-8** | AskUserQuestion record |
| 16:47:35 | Step 7: `git_policy_check` PASS · 6 exact paths staged (`--cached` verified = exactly 6) · kernel commit | `01478b659` |
| 16:47:46 | Step 8: **check-views PASS** (deterministic at committed stamp) · **additions-only PASS** over `cb8979041..01478b659` | transcript |

## 3. Discrepancies & stop dispositions (complete list; none silent)

- **D1 — step-0 "clean tree" deviation.** sam-59 (live session) held 3 unstaged in-flight files in its own `AGENTS/SAM/` working set, unrelated to every custody path; staged index empty, KERNEL clean. **Ruled PROCEED by Will** before step 1; recorded in the window-ruling record. *Reviewer note: the runbook's "clean tree" precondition assumes a single-session repo; the shared-desk reality needs the criterion its substance already used — staged-empty + custody-paths-clean.*
- **D2 — first preflight refusal, PROME authoring defect.** PROME minted `…T16:30:00Z`; custody canon is `%Y-%m-%dT%H:%M:%S.%fZ`. Refusal fired **before any write** — the fail-closed posture's first live demonstration was against the custodian's own document. Fixed `cb8979041` (instants unchanged from Will's bounds). *Defect owned by PROME; the draft's `TO-BE-RULED` placeholder gave no format example to copy — successor drafts should carry a canonical-form comment.*
- **D3 — step-6 criterion vs tool design.** Runbook step 6 expects the retry "byte-identical"; **events were, across all three runs**, but views embed `captured_utc_now()` and live modes refuse injected time (the same mechanism enforcing the window), so raw view bytes can never repeat. Isolated to exactly the `render_as_of` line (run2-vs-run3 diff). View integrity is instead carried by step 8's `--check-views`, which re-renders **at the committed stamp** and passed. **Ruled PROCEED by Will.** *Reviewer note: re-word step 6 to "events byte-identical + views differ only in `render_as_of`", or have apply skip re-rendering unchanged view content. The C6 rehearsal did not surface this because its transcript reconciliation didn't compare live view bytes across two applies.*
- **D4 — window guard fired twice on the submitter side** (SAM, 16:29:01 / 16:29:48) and halted both times; SAM waited for 16:30:01 rather than rounding down. Not a defect — logged as the guard doing its job on the other side of the C1 contract, per SAM's own report.

## 4. Burden (per the C8 dimension; measures a reviewer can re-derive)

- **Wall-clock, go-word → step-8 green:** ~32 min (~16:16 → 16:47:46), of which ~17 min was the ruling/stop-condition round-trips — the attended-sitting design working as designed, not overhead to engineer away.
- **Operator rulings required: 3** (window · D1 · D3) + go word. Zero rulings were requested that the runbook didn't mandate.
- **Commits: 5** (ruling record · SAM submission · mint · correction · kernel commit) + this packet.
- **Sessions: 2** (PROME + SAM's step 1). No spawns, no other desk touched.
- **Test suite untouched** (212 green at packet v2; no code changed during the sitting — the D2 fix was data, not code).

## 5. Audit completeness

- `additions-only` PASS over the full sitting history `cb8979041..01478b659` (protected paths: `KERNEL/audit/commands/`, `KERNEL/shadow/events/`).
- `durable-results` PASS at apply (2 explicit submissions ↔ 2 durable results).
- `view-reproduction` PASS post-commit.
- Not covered (known, per each check's printed does-not-prove line): state outside the printed perimeters; the D3 reviewer note above is the one runbook-spec gap this sitting surfaced.
- Declared gaps 1–3 from packet v2 (rehearsal not re-run post-delta · lock-path VERIFIED-LOW · `write_views` opt-in parameter) — **status unchanged by the pilot; none fired.**

## 6. Rollback / stop disposition

- **No rollback needed; nothing to unwind.** All durable writes are the two events + four views in `01478b659`; events are additions-only-verified; views are replaceable projections.
- Window closes 18:00:00Z or at Will's word; nothing further runs under `LIVE-2026-0001` after this packet — the activation is single-window and expires by its own bounds.
- **Push:** deferred to Will's word (runbook step 9). The commits are local until the next worded push/closeout sweep.

## 7. C8 decision for Will (after review)

Per READINESS_PLAN row C8: **continue, pause, remediate, or end Gate C.** PROME's input is limited to the facts above; the recommendation belongs to the reviewer. **Reviewer = RED or DAEDALUS (Will picks; never PROME).**
