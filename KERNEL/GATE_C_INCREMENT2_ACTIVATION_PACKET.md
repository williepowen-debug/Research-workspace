# Gate C Increment 2 — activation packet (LIVE-2026-0002)

**Prepared:** 2026-08-27 evening by PROME (builder/custodian — not reviewer). **State:** PINS COMPLETE, DRAFT FAILS CLOSED — awaiting ① independent review verdict (seat pending Will's direct word in RED's window; inputs transfer to DAEDALUS cleanly) and ② Will's window ruling.
**Companion:** proposal `GATE_C_INCREMENT2_PROPOSAL.md` · draft activation `GATE_C_INCREMENT2_ACTIVATION_DRAFT.json` (window fields `TO-BE-RULED` — verified unusable until replaced; at step-2 mint the byte-diff vs this draft must be the two window fields ONLY, the C7 discipline) · corrected runbook `GATE_C_C7_RUNBOOK.md` governs steps 0–9 verbatim.

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
