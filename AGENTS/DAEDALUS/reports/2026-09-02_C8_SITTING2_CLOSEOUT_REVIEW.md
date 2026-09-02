# Gate C — Sitting 2 C8 CLOSEOUT REVIEW (DAEDALUS, reviewer seat) — 2026-09-02

**Reviewer:** DAEDALUS (`daedalus-05`, live through the sitting) · **Packet reviewed:** `KERNEL/GATE_C_C8_CLOSEOUT_PACKET_2026-09-02.md` (`582600d5c`) · **Transcript:** `KERNEL/rehearsals/2026-09-02_sitting2-transcript.txt` (814 lines) · **Ruling record:** `PROME/proposals/2026-09-02_sitting2-RULING-RECORD.md` · **Range:** `915af2e8b..78d8b5b37` · **Review clock:** 14:15Z–14:2xZ, same box, same clone, nothing pulled.

**Method:** every load-bearing claim in the packet re-derived at the artifact by me, not read from the packet. Registered tools re-run under my own invocation; independent `git` re-derivation beside each tool result. Research truth of the resolution is RED's leg (verifier seat), read but not relitigated.

## 1. Verdict

**C8 recommendation to Will: CONTINUE.** Zero integrity failures. Every mechanical claim in the packet reproduces independently. The two live refusals (MIDAS 14:04Z, post-revocation preflight 14:13Z) are the fail-closed design working, not defects. Conditions in §4 — all doc/process, none blocking, none silent.

## 2. Re-derivation table (what I checked, how, result)

| # | Packet claim | My check (independent of the packet) | Result |
|---|---|---|---|
| 1 | additions-only over `915af2e8b..78d8b5b37` (reviewer's ask) | `live_shadow.py --audit-additions` full SHAs, own invocation 14:19:12Z **+** `git diff --name-status` on `KERNEL/audit/commands` `KERNEL/shadow/events` | **PASS** both: 17 `A`, 0 `M/D/R` |
| 2 | 17 events accepted, 0 rejected receipts | count of `A` under `shadow/events` = 17; under `audit/commands` = 0 | **matches** |
| 3 | event set = the six command sets | event_type tally 7 QuestionRegistered · 7 ForecastSubmitted · 1 QuestionClosed · 1 ResolutionProposed · 1 ResolutionVerified vs command tally from the six activation files (A 2Q1F · B 1Q2F · C 2Q1F · D 1Q2F · E 1Q1F1C · F 1P1V) | **identical, 17=17** |
| 4 | six activations LIVE-2026-0007..0012, window per WQ-103, all affirmatively closed 14:13:08.190997Z | parsed all six minted files: window `[14:00:00.000000Z,17:00:00.000000Z)` ×6; `revoked_at` `2026-09-02T14:13:08.190997Z` ×6; `78d8b5b37` stat = exactly 6 files, 6 insertions, 6 deletions | **matches** |
| 5 | mint diff vs draft = `source_commit` + two window fields (F2) | `diff DRAFT vs minted` for A–E | **A–E: exactly 3 fields** (+`revoked_at` at close). **F: NO DRAFT EXISTS** — see finding R1 |
| 6 | F pins MIDAS `CMD-01a05d61` (8bb18ca2…) + RED `CMD-01a06273` (51763d23…) | `sha256sum` of both committed files vs F's `commands[].sha256` | **both equal** |
| 7 | grants promoted, live file = `a1fec819…` | `sha256sum KERNEL/policies/capability-grants.json`; E and F pin `a1fec819`, A–D pin `6e73c29e` | **matches; promotion boundary sits between D and E as designed** |
| 8 | post-revocation preflight refuses | transcript T804–808: `LIVE_WINDOW_REFUSED $.window_end … rc=1` | **seen** |
| 9 | suite 220 passed + 77 subtests pre and post | **re-run by me:** `.venv/bin/python3 -m pytest KERNEL -q` → `220 passed, 77 subtests passed in 9.03s` | **reproduces** |
| 10 | view-reproduction PASS | `live_shadow.py --check-views` own invocation 14:19:14Z, `render_as_of=2026-09-02T14:12:42.149129Z` | **PASS** |
| 11 | exact-pathspec commits only; nothing swept | every non-`KERNEL/` file in range mapped to its commit: MIDAS ×3 → `3a4d996a9` (MIDAS) · RED ×3 → `20caea9aa`/`ab909bb63` (RED) · REGINALD ×3 → `3b45aa60c` (REGINALD) · PROME ×3 → PROME commits. Kernel commits touching non-Kernel paths: **one** — `0a857e4f3` (A mint) also carried `PROME/proposals/…RULING-RECORD.md` | **owner boundaries hold**; the one mixed commit is inside the custody grant (sitting rulings) — finding R5 |
| 12 | MIDAS-06 RESOLVED YES / VERIFIED YES, independent | RED's report re-derives at primaries THIS session: DFII10 2.42 (8/28) ≥ 2.40; GC=F 4478.10 and GCZ26 4529.90 ≥ 4340.70 on both bases → branch (a) → YES; verifier ≠ proposer ≠ custodian | **independent, both legs, both bases** |
| 13 | 8/27 C8 ruling's six conditions honoured this sitting | 1 retry semantics (events byte-identical, views modulo `render_as_of`) — transcript ×6 ✅ · 2 no hold-local dependence ✅ · 3 affirmative close + rulings appended at ruling time ✅ · 4 durable transcript committed with packet (`582600d5c`) ✅ · 5 suite green ✅ · 6 READINESS_PLAN row for Sitting 2 — **not yet advanced** | **5/6 done; #6 is closeout housekeeping (R4)** |

## 3. The packet's five discrepancies — reviewer's read

| Packet item | Reviewer verdict |
|---|---|
| 1 MIDAS refusal → mint-first | **Correct disposition, within custodian authority.** Integrity is preserved because acceptance re-tests commit-existence + byte-equality at APPLY (`load_live_submissions`), which ran after both desk commits. What moved is WHEN the pin is verified against committed bytes: mint-time → apply-time. Encode (R2); fleet memory `finding_liveness_gate_keyed_on_an_artifact_that_must_exist_first` (written by a sitting desk today) is the same shape from the desk side. Second live refusal → WQ-150 evidence, agreed. |
| 2 WQ-149 row text not executable → pair on F | Concurred 09:5x pre-sitting; row annotated `fe833c220`. **Will's explicit F-carrier confirm still owed** — the change from a ruled row's text needs the operator's own word, however sound. |
| 3 shared-index stop-check fired once | Cleared by the owner's own commit in 30 s, nothing swept — verified at `3b45aa60c` (REGINALD paths only). Working as designed. |
| 4 CALIBRATION row 14 `OUTCOME_VOCABULARY_MISMATCH` | Registered exclusion (`projection-exclusions.json`), by design. **The first live resolution is unscored until Will rules the four-branch vocabulary** — a Will item, and it should land BEFORE the next resolution sitting or the unscored set grows. |
| 5 grants-hash boundary observation | Correctly withdrawn by MIDAS at the artifact. |

## 4. Reviewer findings (beyond the packet) and conditions

| ID | Finding | Class | Condition / owner |
|---|---|---|---|
| **R1** | Packet §1 says *"Every activation: mint diff vs draft = exactly source_commit + two window fields."* **F had no draft**, so that check could not run for F. Transcript T640–683 shows the actual check: diff vs **minted E**, expected differences enumerated (id · source_commit · commands · event_ids) — a sound substitute, but not the check the packet names. The line a reader reads names a check that did not run (PAT-137 shape, PAT-074). | description over-claim, not execution | PROME corrects the packet line. **Runbook gains a mint form for DRAFTLESS (sitting-authored) activations:** referent = the most recent minted sibling; expected-diff set enumerated; recorded in the transcript. Doc-only. |
| **R2** | Mint-first (E) and mint-from-reported-hash (F) pin paths that existed in **no commit at mint time**. Acceptable because apply re-verifies at the committed bytes — but the runbook should say so, and require the custodian's post-commit re-hash at the target path before apply as a named step (done live for E per ruling record; for F the tool's own apply check carried it). | encode | Runbook steps 1/2 re-worded with WQ-150: mint-first sequence + post-commit re-hash step. Doc-only, after WQ-150 ruled. |
| **R3** | The durable transcript records the suite's OUTPUT but not its INVOCATION (no `$` line before T811). I reproduced it by inference (`.venv` python, `-m pytest KERNEL -q`). A transcript that omits the command line is reproducible only by guessing. | transcript form (C8 N2 extension) | Every check in the transcript carries its command line. Doc-only. |
| **R4** | READINESS_PLAN has no Sitting-2 row; the 8/27 C8 row still reads as the latest. Condition 6 of the 8/27 ruling (housekeeping) is owed for this sitting. | housekeeping | PROME at closeout. |
| **R5** | `0a857e4f3` (A mint) also committed the ruling record. Inside the custody grant, but a mint commit that carries a second file blurs the mint-diff audit. | hygiene | Mints commit alone; ruling-record edits commit separately. Doc-only. |
| **R6** | 21 commits including the whole sitting are LOCAL at review time (`ahead 21`). Root: GitHub is truth. Packet §6 defers transport to PROME's closeout push. Not a defect; a timing exposure if the box switches first. | transport | PROME's closeout push carries it (or Will words an earlier one). |

**Owed to Will regardless of the C8 verdict (packet §7, confirmed):** ① WQ-149 F-carrier confirm · ② scoring vocabulary (MIDAS 8/27 §4) — before the next resolution sitting · ③ WQ-150 root ④ key (~9/8), now with two live refusals as evidence.

## 5. What this review does not prove
State outside the printed perimeters; research truth beyond RED's re-derivation (read, not repeated); anything about pushes not yet made. My tool runs used activation F's document as the perimeter binding for the range audit and the views check — the tool requires one; the range and the views are activation-independent.

**ACTION — DAEDALUS recommends CONTINUE to Will. PROME applies R1/R3/R4/R5 at closeout (doc-only). R2 rides WQ-150.**
