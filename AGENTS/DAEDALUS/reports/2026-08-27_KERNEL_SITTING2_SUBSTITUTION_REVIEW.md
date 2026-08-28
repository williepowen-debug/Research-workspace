# DAEDALUS — Sitting-2 reviewer review: substitution rule BLESSED (2 conditions) · LIQUID timing commit STANDS · F3 ENDORSED

**Date:** 2026-08-27 late eve · **Reviewer:** DAEDALUS, as the named substitute for RED's seat, on Will's in-session word ("can you review KERNEL now?") — seat eligibility per the C8 packet §7 and tonight's transcript close line ("Closeout reviewer: RED or DAEDALUS, never PROME"). DAEDALUS has authored nothing in `KERNEL/`.
**Brief:** `AGENTS/RED/inbox/2026-08-27_from-PROME_sitting2-reviewer-seat-substitution-rule-blessing-is-the-long-pole.md` · prep state `KERNEL/GATE_C_SITTING2_PREP_2026-08-27.md` · R3 baseline from the mid-sitting ruling (`PROME/proposals/2026-08-27_increment2-window-RULED.md`).
**Method:** every claim below was independently re-derived this session (own tool runs, own diffs, own hash computations from `git show` bytes) — not read off PROME's prep doc. Commands and outputs reproducible from the file paths and commits cited.

---

## 1. VERDICT — Ask 1: the substitution rule is BLESSED, with the rule stated precisely and two conditions

**Blessed rule (this is what Monday may rely on):** when a command is REFUSED at preflight/acceptance, its correction is a **NEW command file with a NEW command_id** at the same desk's C1 submission path; the refused original remains at its path, immutable, never edited or deleted; the corrected file's delta vs. its refused predecessor is **exactly**: new `command_id` · `depends_on` re-pointed to sibling new ids · corrected/augmented `native_refs` (including added companion refs and re-cut `source_commit`) · refreshed `submitted_at` — with `question_id`/`forecast_id` and payload semantics **unchanged** unless the refusal reason itself indicts the payload. Activation drafts pin the new bytes by sha256.

**Why bless rather than force re-review of the whole book:** the only alternatives are editing refused files (violates the stronger immutability rule) or discarding and re-reviewing all 12 from scratch (cost with no gain — the delta discipline plus byte pins make the change fully auditable, and I audited it). RED's R3 baseline governed re-cutting a *reviewed* doc into activation subsets; a refusal-correction is a different act and gets its own rule — supplied above — rather than a stretched R3.

### Evidence, all independently re-derived

| Check | Result |
|---|---|
| Deep-diff refused→corrected, CREED 101→111 · 102→112 (sampled) + LIQUID both pairs (full) | Deltas are **exactly** the blessed-rule fields, nothing else. `question_id`/`forecast_id`/payload absent from every diff |
| 12/12 draft pins (A `LIVE-2026-0007` · B 0008 · C 0009 · D 0010) vs on-disk submission bytes | **12/12 MATCH** (sha256 recomputed by me) |
| 16/16 native refs in the corrected set (CREED 111–116 ×2 refs, LIQUID pair ×2 refs) vs committed Git objects | **16/16 MATCH** — my own TSV row selection (`+LF` convention confirmed) and JSON-pointer selection + canonical hashing against `git show <source_commit>:<path>` bytes. The LIQUID re-pin (`1f3ed513…`) verifies; the refused pin (`8315a740…`) is dead |
| REGINALD a1/a2/a6/a7 pins in drafts C/D vs the ORIGINAL reviewed 12-command doc (`GATE_C_INCREMENT2_ACTIVATION_DRAFT.json`) | **Byte-identical** — review-covered, zero exceedance; the exceedance set is exactly CREED 6 + LIQUID 2 as briefed |
| R2 rider: policy/identity pins across A–D | Identical across all four AND match live `actors.json` / `capability-grants.json` / `custody-policy.json` (hashes recomputed) |
| Fail-closed state of drafts | `window_start`/`window_end` = `TO-BE-RULED`, `source_commit` = non-hex `TO-BE-RECUT-AT-MINT` — cannot validate as-is ✓ |
| Event-id hygiene | 12 event ids, all distinct, 1:1 with commands, no reuse of pilot ids 0033/0034 |
| Superseded originals immutable | CREED 101 and LIQUID old pair: single-commit history each, never edited; remain at paths as history ✓ |
| Stop-2/stop-3 refusal records | Confirmed in the tee'd transcript: all-material-field `NATIVE_RECORD_MISMATCH` (CREED, companions absent) at line 145ff; `NATIVE_BLOB_MISMATCH` on the LIQUID pair at preflight C. The corrections address exactly these causes |

### The two conditions

**S1 — the substitution diff goes in the transcript, machine-produced, per pair.** For every future refused→corrected substitution, the sitting transcript records a field-level diff of each pair showing only the blessed-rule fields changed (the F2 mint-diff discipline, applied one layer down). For THIS set, the diffs in this report discharge S1.
**S2 — a superseded command_id in any future activation draft is a STOP.** "No Monday activation references them" is currently prose. Supersession map for the record: 101→111 · 102→112 · 103→113 · 104→114 · 105→115 · 106→116 · `CMD-01a044fc-…abc09a0`→`CMD-01a04562-…2ec64473` · `CMD-01a044fc-…e9fafb`→`CMD-01a04562-…af5d65`. A draft citing any left-column id fails closed. (Ids 0004/0006 stay never-reused, as prep §3 already states.)

---

## 2. VERDICT — Ask 2: LIQUID's 22:42:03Z commit STANDS AS-IS; no re-execution; one wording fix owed to the successor runbook

**Facts (verified):** `c3b89dc9d` = exactly 2 files, both at LIQUID's own submission path, pure additions, byte-identical to the draft-C pins, landed 23s after the 22:41:40Z affirmative revocations, inside the ruled window bounds [21:45, 23:45Z). Zero events accepted tonight; the post-revocation refusal proof shows acceptance was already closed (`LIVE_WINDOW_REFUSED`, end=22:41:40.639389Z).

**Adjudication:** the commit stands.
1. **The rule as worded is not executable by the party it binds.** Carve-out ④'s desk grant keys on an activation being live — a state a desk cannot observe at commit time (a 23-second-old revocation is invisible without a fetch between add and commit). A condition the complying party cannot evaluate at act time is a defect in the rule, not the party. LIQUID complied with every condition it *could* evaluate: own path, own authorship, ruled window bounds, immutable after.
2. **The boundary that matters held.** The ledger's protection is acceptance, which was affirmatively closed 23 seconds earlier and refused everything after; submission files are inert by design.
3. **Re-execution is the worse act.** Re-committing identical bytes manufactures history to cure an ambiguity, and touching the files at all violates the stronger never-edit-after-submission rule. PROME's recommendation (nothing) is correct.

**The owed fix (successor wording, not retroactive):** scope the desk-commit grant to the **ruled window bounds** — the one temporal fact a desk can read from the ruling record — not to instance liveness; and on any mid-window pause, the custodian doorbells submitting desks so the window is affirmatively closed desk-side, symmetric with N3's ledger-side affirmative close. Owner: PROME (runbook §), with the carve-out-④ mirror line riding the next Will-gated root edit.

---

## 3. F3 ENDORSED (re-run by me) + consumed items

- `test_verification_disagreement_must_use_dispute`: **re-run this session, OK** — mismatch verification is REFUSED (`TRANSITION_FORBIDDEN`), no event written, durable REJECTED receipt path confirmed at `writer.py::build_rejected_receipt`. Full suite: **212 OK, re-run by me.** The sitting consequence stated in prep §1 (a live verifier disagreement = designed refusal → pause-and-rule, since `DisputeResolution` is outside Monday's command set) is the correct reading.
- Prep §0 scoreboard items ③④⑦ consumed as closed; ② (grants draft + fail-closed verifier sentinel) is PROME-lane and its catch (`question.close_own`) is the right F1-class find — no reviewer objection.

## 4. Monday consequence

Precondition ① is DISCHARGED by this review. With §4's byte-verification standing, CREED/LIQUID/REGINALD need not attend the sitting; remaining path is exactly prep §5: MIDAS authors (Friday) → PROME finalizes grants/E-F drafts → Will's window Monday. S1 costs nothing Monday (already discharged for this set); S2 is a one-line check at mint.

*Reviewer-independence note: this report used the kernel's file formats but none of its verdict machinery — selections and hashes are my own re-implementation, which doubles as an independent confirmation of the `+LF` TSV row convention and canonical-JSON value hashing.*
