# Gate C Increment 2 — activation packet (LIVE-2026-0002)

**Prepared:** 2026-08-27 evening by PROME (builder/custodian — not reviewer). **State:** REVIEWED — **RED verdict PROCEED, GATED on F1+F2 (report of record `AGENTS/RED/reports/2026-08-27_KERNEL_INCREMENT2_REVIEW.md`, `23263d43a`); both fixes LANDED below ~17:1x ET (stamps this section drifted +~1h when first written; corrected against commit times), RED re-verify requested; then Will's window ruling.** Original state line: pins complete, draft fails closed.

## 0. C8-style amendments on RED's verdict (landed 2026-08-27 ~17:1x ET; heading stamp corrected with the others — one drifted stamp survived the first correction pass, the correction-pass class in miniature)

- **F1 🔴 FIXED — the grants half of the identity, which the packet had forgotten** (PROME defect, 3rd instance of the C7-Finding-1 class on this workstream, confirmed by PROME at the enforcement file before fixing): `KERNEL/policies/capability-grants.json.increment2-draft` prepared — CREED/LIQUID/REGINALD each gain exactly `question.register` + `forecast.submit_own`, nothing else; sha256 `6e73c29e…60de` now pinned as the draft activation's `capabilities_sha256`, so the mint validates only after BOTH policy bumps land in order at step 2. **F1's Monday rider REGISTERED:** `resolution.propose`/`resolution.verify` are granted to NOBODY — MIDAS-06's resolution refuses identically unless Monday's second activation ships its own grants bump (MIDAS's grants ride there too; its actors entry stays in this increment's registry draft, harmless and already hash-pinned).
- **F2 🟠 FIXED — the step nobody was assigned:** step 1 of the sitting is explicitly **each desk's own commit** (carve-out ④, active at the ruling): CREED, LIQUID, REGINALD copy their staged bytes to their pinned `outbox/kernel/submissions/` paths, verify sha256s, commit with explicit pathspecs only — three desk commits, in-window, before step 2. **The custodian then re-cuts `source_commit` at mint** (desk commits move HEAD); **mint byte-diff discipline vs the draft = the two window fields + `source_commit`, and nothing else** (capabilities pin already in the draft).
- **F3 registered as a MONDAY PRECONDITION, not a tonight item:** before the resolution activation, answer at fixture level — does acceptance REFUSE a `VerifyResolution` whose `verified_outcome_value` differs from the proposed value, or RECORD the mismatch? A preflight answer, never a live discovery. (Quick grep of `acceptance.py` is non-obvious; needs the real fixture run.)
- RED's §6 sign-offs recorded: `policy_version` stays `kernel.policy.1` (the hash does the integrity work) · `source_commit` composition legal WITH the re-cut rider above · `mode` reuse is FORCED (`live_shadow.py` const-validates `LIVE_SHADOW_PILOT`) — no code change, as the proposal forswears. Judgment items: SAM-33 reachability pattern = house standard · `closes_at` convention ENDORSED · REG-01 `opens_at` BLESSED w/ tightened no-backfill discriminator · re-mark-before-stage = standing discipline · PRED-007 shape BLESSED. RED's disclosure on the record: named verifier on 3 of 6 questions.
**Companion:** proposal `GATE_C_INCREMENT2_PROPOSAL.md` · draft activation `GATE_C_INCREMENT2_ACTIVATION_DRAFT.json` (window fields `TO-BE-RULED` — verified unusable until replaced; at step-2 mint the byte-diff vs this draft must be **the two window fields + `source_commit`, and nothing else** — the C7 discipline as extended by F2's re-cut rider, §0; reconciled ~17:25 ET on RED's re-verify residual (stamp corrected from ~19:0x same minute — the clock-not-narrative drift, self-caught at `date`), the stale-line-beside-fresh-fix class) · corrected runbook `GATE_C_C7_RUNBOOK.md` governs steps 0–9 verbatim.

## 1. The book: 12 commands, 3 desks, every pin independently reproduced by PROME

| Desk | Files | Rows | Staged at (bytes frozen, committed) | Verifiers (≠ author) |
|---|---|---|---|---|
| CREED | 6 (3 Q + 3 F) | PRED-001 p=.40 · PRED-004 p=.60 · PRED-007 p=.15 | `AGENTS/CREED/registry/kernel_staged/` @ `9d8231ad2` | REGINALD · LIQUID · RED |
| LIQUID | 2 (1 Q + 1 F) | LIQ-04 p=.25 (its ONLY open forward-resolving row — one not three, honest) | `AGENTS/LIQUID/kernel_staging/` @ `f939dff94` | RED |
| REGINALD | 4 (2 Q + 2 F) | REG-01 p=.90 · REG-06 p=.10 (re-marked 50→10 BEFORE staging, `3ae52ac59`) | `AGENTS/REGINALD/kernel/staged_increment2/` @ `a8b3ea760` | CREED · RED |

Exact command_ids, submission paths, and sha256s: the draft JSON is canonical — 12 commands, event_ids minted 1:1. All 12 hashes reproduced by PROME's own `sha256sum` against the committed staged bytes (not taken from reports). Declines on the record: CREED excluded PRED-010 (live basis question); REGINALD excluded REG-03 (threshold-family, unreconciled figures) and REG-07 (rate/level ambiguity + pending re-mark) under the do-not-manufacture instruction.

## 2. Registry bump (step-2 custodian commit, inside this ruled packet)

`KERNEL/policies/actors.json` gains CREED, LIQUID, REGINALD, **and MIDAS** (added now so Monday's resolution activation needs no second policy touch; MIDAS submits nothing under LIVE-2026-0002). Prepared verbatim at `KERNEL/policies/actors.json.increment2-draft`, sha256 `ad16ca28…aa20f` — **the draft activation pins THIS hash**, so the mint only validates after the bump lands, in order, at step 2. Capability-grants and custody-policy pinned UNCHANGED from C7 (hashes re-verified tonight).

## 3. Window options (Will rules; MIDAS + first Resolution ride a SECOND activation ~Mon 8/31 post-16:15 either way)

- **Path A:** rule LIVE-2026-0002 TONIGHT (~60 min attended) — the 12-command book lands today; Monday's activation adds MIDAS + ProposeResolution/VerifyResolution for MIDAS-06.
- **Path B:** rule LIVE-2026-0002 for MONDAY post-16:15, folded beside the resolution activation — one attended block, everything lands together.

## 4. Open items FOR THE REVIEWER (flagged, not silently decided)

1. **Perimeter gap (LIQUID, live-proven):** "forward-resolving" ≠ "resolvable by a REACHABLE source" — LIQ-04's named LCD series isn't retrievable-as-a-series; registered SAM-33-style (negative_search_procedure + CONSTRUCTED-labeled EDGAR fallback). Rule whether that pattern is the house standard or reachability becomes a registration requirement.
2. **`closes_at` convention (LIQUID, prospective):** deadline > measurement-window end for lagged-publication resolvers (2027-02-15 vs 12/31) — endorse as house convention?
3. **`opens_at` before submission (REGINALD's REG-01, 2026-02-23):** C7 precedent supports it (SAM-33 opens 6/30, submitted 8/27); no-backfill read as "already-RESOLVED history does not enter." Bless or require re-cut.
4. **No-amend perimeter property (REGINALD):** with Amend/Withdraw OUT, every stale confidence becomes load-bearing at submission — REGINALD re-marked BEFORE staging for exactly this reason. Should the verdict instruct all future submitters to re-mark-before-stage as standing discipline?
5. **PRED-007 native-correction shape (CREED):** the kernel question's resolution_rule explicitly tightens a loosely-true-at-authoring TSV row; the TSV row is FROZEN until post-sitting (it is the pinned native_ref). Bless the shape.
6. **Draft assumptions needing reviewer sign-off:** `policy_version` stays `kernel.policy.1` (registry addition assumed non-bumping — confirm) · `source_commit` = repo HEAD at packet-cut (`a8b3ea760…`) while each native_ref carries its own pin commit internally (CREED/LIQUID @ `8326b5ce…`, REGINALD @ `fb108a9f…`) — confirm composition is legal vs the tool's checks · `mode` reuses `LIVE_SHADOW_PILOT` — confirm or require a new mode token.

## 5. Standing constants (unchanged, not re-argued)

Attended · Will-worded half-open UTC window in canonical form · PROME sole writer · N2 tee-transcript from invocation one · N3 affirmative close · D5 push-train reality · stop conditions verbatim · additions-only · closeout packet → reviewer = RED or DAEDALUS, never PROME. ⛔ Desk TSV rows named as native_refs are FROZEN until the sitting closes — an edit breaks its pin (CREED's PRED-007 row explicitly so).
