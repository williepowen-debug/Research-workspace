# Gate C — Sitting 2 CLOSEOUT PACKET (C8 class) — 2026-09-02

**Custodian/author:** PROME (`prome-94`, DESKTOP) · **Reviewer:** DAEDALUS (RED was a participant — verifier seat; PROME never reviews) · **Window (WQ-103):** `[2026-09-02T14:00:00.000000Z, 2026-09-02T17:00:00.000000Z)`, **affirmatively closed 14:13:08.190997Z** on all six activations (`78d8b5b37`) · **Transcript:** `KERNEL/rehearsals/2026-09-02_sitting2-transcript.txt` (tee'd live, 814 lines; line cites below) · **Ruling record:** `PROME/proposals/2026-09-02_sitting2-RULING-RECORD.md` · **Runbook:** `KERNEL/GATE_C_C7_RUNBOOK.md` · **Prep:** `KERNEL/GATE_C_SITTING2_PREP_2026-08-27.md`.

## 1. Results

| Activation | id | Commands (actor) | Mint | Submission commit | Events commit | Preflight / apply / retry / check-views / additions-only |
|---|---|---|---|---|---|---|
| A | LIVE-2026-0007 | CREED 111 Q · 112 F←111 · 113 Q | `0a857e4f3` | `8dc211f94` (8/27) | `21ddfdf40` | all PASS (T42–270) |
| B | LIVE-2026-0008 | CREED 114 F←**113 cross-activation** · 115 Q · 116 F←115 | `3b23fdc7c` | `8dc211f94` | `579f71ce5` | all PASS (T284–367) |
| C | LIVE-2026-0009 | LIQUID Q …2ec64473 · LIQUID F …c3af5d65 · REGINALD a1 Q | `b7c3f55be` | `c3b89dc9d` (8/27; REG a1 `e4a51fb35` ancestor) | `d63a63be3` | all PASS (T380–447) |
| D | LIVE-2026-0010 | REGINALD a2 F←**a1 cross-activation** · a6 Q · a7 F←a6 | `7de7bb54c` | `e4a51fb35` (8/27) | `0f879395f` | all PASS (T461–528) |
| — | grants promotion | `capability-grants.json` ← `.sitting2-draft`, sha256 `a1fec819…` verified | `53293f461` | — | — | T530–539 |
| E | LIVE-2026-0011 | MIDAS 006a RegisterQuestion · 006b SubmitForecast · 006c CloseQuestion (MIDAS-06) | `813d40e06` | **`3a4d996a9` (MIDAS, 14:06:27Z, in-window)** | `879158dc0` | all PASS (T571–638) |
| F | LIVE-2026-0012 | MIDAS `CMD-01a05d61` ProposeResolution **YES** (v2→3) · RED `CMD-01a06273` VerifyResolution **YES** (v3) | `16a47364c` | **`20caea9aa` (RED, 14:11:26Z, in-window)** | `d37277f90` | all PASS (T728–790) |

**17 events accepted, 0 refusals, 0 rejected receipts, 0 stop conditions on screen.** Every activation: mint diff vs draft = exactly `source_commit` + two window fields (F2); idempotent retry = `outcome=EXISTING` ×n, zero event writes, events byte-identical, views identical modulo `render_as_of`; `git_policy_check` PASS; exact-pathspec commits only. **MIDAS-06 is the Kernel's first live RESOLVED + VERIFIED question** (branch (a): DFII10 2.42 [8/28] ≥ 2.40, GC=F 4478.10 / GCZ26 4529.90 ≥ 4340.70; MIDAS and RED derived YES independently; no DisputeResolution). Post-revocation preflight on F refused `LIVE_WINDOW_REFUSED` (T800–808) — fail-closed proved live. **Post-sitting suite: 220 passed + 77 subtests** (T811–814), identical to the pre-sitting baseline.

## 2. Timeline (tool-output stamps, UTC)
14:00:15 step 0 PASS (staged index empty · custody clean · 6 hashes · S2 clean) · 14:00:31 A mint · 14:01:18 A events · 14:02:28 B events · 14:03:03 C · 14:03:13 D · 14:03:35 grants promotion · **14:04 MIDAS REFUSES its step-1 commit (E still `_DRAFT`) — correct under root ④** · 14:05:23 E minted first · 14:06:27 MIDAS commits · 14:07:02 E events · 14:0x RED authors Verify un-staged, reports sha256 · 14:10:10 F minted from both desks' bytes · 14:11:26 RED commits · 14:12:00 F preflight (commit HELD: REGINALD renames staged in the shared index) · 14:12:31 REGINALD commits `3b45aa60c` · 14:12:42 F events · 14:13:08 six affirmative closes · 14:13:22 suite re-run green.

## 3. Discrepancies & stop dispositions (complete; none silent)
1. **Runbook step order 1→2 is unexecutable under root carve-out ④ for a desk named only in an unminted packet.** MIDAS refused (T541 header; ruling record 14:04Z) — the second desk in two days (RED 9/1). Custodian disposition, no Will ruling needed: mint FIRST, desk commits under the live packet; for F, RED authored un-staged → PROME minted pinning the reported hash → RED committed. **Feeds WQ-150** (root ④ liveness key vs runbook §successor scope): under the ruled-bounds key MIDAS could have committed at 14:04Z. Runbook step 1/2 wording should say so once WQ-150 is ruled (DAEDALUS blueprint pointer).
2. **WQ-149 row text "E ALSO pins the pair" was not executable** (a Verify cannot exist at E's mint). Executed per DAEDALUS's ruling table + PREP §5.6: E as drafted, pair on F. Flagged to Will pre-sitting (09:4x); DAEDALUS concurred 09:5x; row annotated `fe833c220`. Will's explicit confirm of the F carrier is **still owed** (his 09:49 word covered the spawns).
3. **Shared-index stop-check fired once** (F step 7): REGINALD's two staged renames — cleared by the owner's own commit within 30 s; nothing swept (pathspec commits throughout). Other desks' UNSTAGED in-flight files outside custody paths recorded per C8 D1 (CARL ×3, SAM ×1, PROME board cursor).
4. **`CALIBRATION.tsv` row 14 (MIDAS-06, forecast 0.45 YES, outcome YES) carries `OUTCOME_VOCABULARY_MISMATCH`** — the registered projection-exclusion reason (`render.py:18`): the frozen letter is four-branch (YES/NO/AMBIGUOUS mass 0.45/0.20/0.35) in a binary-const ledger. **Designed exclusion, not a defect** — MIDAS's 8/27 §4 scoring-vocabulary item, carried in PREP §0 ⑤ as a Will item; still un-ruled. The first live resolution is therefore accepted, verified, and **unscored by projection** until Will rules the vocabulary.
5. **Suppression noted, not a stop:** MIDAS's observation that E pins `a1fec819…` while A–D pinned `6e73c29e…` is the designed promotion boundary (verified by MIDAS at the artifact, flag withdrawn).

## 4. Burden
- **Wall-clock, window open → six closes:** 13 min 08 s (14:00:00 → 14:13:08); of which ~7 min was the two desk round-trips (MIDAS refusal→mint→commit; RED author→mint→commit) — the attended-sitting design working.
- **Operator rulings required during the sitting: 0** (window ruled 9/1; WQ-149/150 ruled 9/1; spawns Will's 09:49 word). Two owed AFTER: F-carrier confirm (item 2) · scoring vocabulary (item 4).
- **Commits: 20** (6 mints · 6 event commits · grants promotion · 6-file revocation · MIDAS ×1 · RED ×1 [+ RED companion `ab909bb63`] · REGINALD ×1 index-clear) + this packet/transcript commit.
- **Sessions: 4 Kernel-touching** (PROME custodian · MIDAS · RED · REGINALD index-clear) + DAEDALUS reviewer live; 0 spawns by PROME.
- **Code changed during the sitting: none.** Policy file changed: `capability-grants.json` (registered version promotion, hash-verified).

## 5. Audit completeness
- `additions-only` PASS per activation over each `BASE..HEAD`; **full-sitting range `915af2e8b..78d8b5b37` = reviewer's re-derivation ask** (protected: `KERNEL/audit/commands/`, `KERNEL/shadow/events/`).
- `durable-results` PASS at every apply (17 explicit submissions ↔ 17 durable results); `view-reproduction` PASS at every committed `render_as_of`.
- Not covered (each check's printed does-not-prove line): state outside printed perimeters; research truth of the resolution (RED's independent primary re-derivation is the research check, in `AGENTS/RED/reports/2026-09-02_KERNEL_GATE_C_SITTING2_MIDAS06_VERIFICATION.md`).
- Declared gaps from packet v2 (rehearsal not re-run post-delta · lock-path VERIFIED-LOW · `write_views` opt-in) — status unchanged; none fired.

## 6. Rollback / push
- **No rollback needed; nothing to unwind.** All durable writes = 17 events + 4 views + 1 promoted policy file; events additions-only-verified; views replaceable projections.
- All six activations carry `revoked_at`; nothing can run under them (proved T800–808).
- **Push:** the sitting's commits are local at packet time; per runbook step 9 Will words any push (transport only). PROME's standard auto-push at closeout will carry them and every desk's ride-along otherwise.

## 7. C8 decision for Will (after DAEDALUS review)
Per READINESS_PLAN row C8: continue, pause, remediate, or end Gate C. PROME's input is the facts above. Items needing Will regardless of the C8 verdict: **WQ-150 root ④ key** (now with a second live refusal as evidence) · **scoring vocabulary** (MIDAS §4; the first live resolution is unscored until ruled) · **F-carrier confirm** on WQ-149.
