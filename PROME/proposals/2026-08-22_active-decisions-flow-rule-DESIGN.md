# ACTIVE_DECISIONS.md flow rule + first rotation pass — DESIGN (DOCKET row 2026-08-22)
**Author:** PROME · **Date:** 2026-08-22 (Sat, closed-market session, full context budget — the row's own precondition, met)
**Status:** ★ RULED — **Will, 2026-08-22 ~10:32 EDT, verbatim: "you have my approval"** (in-session, after the §6 relayed review + §7 dispositions were filed and folded in). All four asked items + both riding amendments approved as one word. Execution record → §8.
**Provenance:** Will-directed 2026-08-16 eve (PROME systems review, "docket ACTIVE_DECISIONS"); DOCKET date-key 2026-08-22 row; precedent = STATUS.md flow rule (Will-approved 8/16, `5ae4f2fee`) + MEMORY.md flow rule (8/12) + HEARTBEAT re-base pattern.

---

## 1. Diagnosis (measured 2026-08-22)
*(Unit correction, tagged post-execution 8/22: the per-row "size" figures in this section and §3's "B now" column were `awk length()` CHARACTER counts mislabeled as bytes — ~2% under true UTF-8 bytes (e.g. VIXCS 4,519 chars vs 4,628 B; energy 5,982 vs 6,078). The file-total 53,819 was `wc -c`, correct. The rotation manifest's figures are true bytes and canonical. Caught by the blind cold-reader test cross-citing the manifest; nothing gated on the per-row numbers.)*

| Fact | Number |
|---|---|
| File size | **53,819 B** |
| STATUS-precedent budget | 51,200 B → file is at **105%** |
| Read-truncation reality | **Boot Read truncated at line 47 of 82 this morning** — the boot-read decision index no longer fits one Read call; a boot reader sees an unannounced fragment (the exact failure class the 8/8 STATUS rotation fixed) |
| Header stamp chain (line 2) | 9,041 B — 17% of the file is prior-stamp history |
| Live Decision Index table | 39,730 B (74%) |
| Largest single rows | energy 5,982 · roster 5,384 · **VIXCS 4,519 (TERMINAL 7/30, self-requests archive)** · TERRY-004 3,306 · FORGE 3,122 · DAEDALUS 2,949 |
| File's own law already violated | Purpose: "It is an index, not a thesis document" · Rules: "Remove or archive when terminal" (VIXCS terminal 23 days) · "Keep this file short" |

Root cause (same class as STATUS pre-8/16): resolved sub-states are **appended as dated records** instead of replacing the language they supersede, and audit fix-rounds annotate in place — so rows only ever grow. A byte cap alone would get walked around (PAT-086); the fix is convention + backstop, mirroring STATUS.

## 2. Design

### 2a. Flow rule (the backstop — CLOSEOUT Chunk 1 wiring, mirrors STATUS verbatim in shape)
> **Flow rule (BYTE-keyed):** `wc -c < PROME/ACTIVE_DECISIONS.md` ≥ **38,400 B** (75% of the 51,200 B budget) at closeout ⇒ rotate, **verbatim + crc32-verified round-trip**, into `PROME/archive/ACTIVE_DECISIONS_ROTATION_<date>.md` until **< 35,840 B** (70%), recorded in the commit. *(Budget derivation, not inheritance — amended 8/22 per review finding 4: the binding failure is the measured ~53-54 KB Read-truncation cap, where this file's boot Read actually truncated on 2026-08-22 at 53,819 B; the 38,400 B trigger sits ≈29% below that bite point. If Read-cap behavior or row density shifts materially, re-derive the budget from the cap — don't carry the number.)* Rotation order: ① terminal rows whole (this is the file's existing Rules law, now with an enforcement point) → ② header prior-stamp chain (keep the current stamp + a one-line pointer) → ③ oldest superseded dated-records inside live rows, via §2b's snapshot-then-rewrite (never clause-splicing). Rotation-not-deletion; history never trimmed in place.

### 2b. Row re-base pattern (HEARTBEAT's pattern at row granularity — this is what protects audit date-anchors)
When a live row rotates under ③, **never splice clauses out**. Instead:
1. **Snapshot the full pre-edit row verbatim** into the rotation file under its row NAME, crc32 per chunk, round-trip verified in-process.
2. **Rewrite the live row current-state-only:** state cell + owner + next + backstop + source, **plus every standing guard**.
3. Leave one dated pointer in the rewritten row: *"(re-based YYYY-MM-DD; prior form + dated-record/audit-tag history verbatim → ROTATION_<date>)"*.

**Why this preserves date-anchors:** spine audits cite rows by name + dated inline tags ("fixed 8/9 audit #8 on the energy row"). Under snapshot-then-rewrite, every such cite resolves: name → live row → pointer → archived verbatim full row containing the cited tag. Nothing an audit ever anchored on is deleted or paraphrased — it relocates whole, checksummed.

**Guard-vs-history discriminator (the one genuinely new rule):** a dated clause is rotation-eligible ONLY if it records a resolved past state AND carries no live directive. Lines like "do NOT treat the arm as live," kill-on-sight entries, no-re-present clauses, and verification-required fences are **STANDING GUARDS — they stay in the live row regardless of age** (they govern the next read; `[[finding_banner_is_a_warning_not_a_fix]]` class). A rewrite that drops a guard is the failure mode of this whole design; the snapshot makes it recoverable, the discriminator makes it checkable.

### 2c. Row-weight convention (what makes rotation rare — the STATUS headline-convention analogue)
A Live Decision Index row is an INDEX row: current state, owner, next, backstop, source, standing guards — target **≤ ~2 KB**. When a sub-state resolves, the resolution **replaces** the pending language (the superseded text is preserved by git and by the next rotation snapshot if material); full logic stays in action cards / owner artifacts, per the file's own Purpose line. Audit fix-rounds keep annotating in place as today — the flow rule absorbs the growth.

### 2d. Archive shape + header pointer (learning from HANDOFF's archive-line bloat)
One rotation file per pass: `PROME/archive/ACTIVE_DECISIONS_ROTATION_<date>.md`, header carries the pass manifest (what rotated, from where, per-chunk crc32, byte counts, **and — amended 8/22 per review finding 1 — `guard-bytes retained: N`**: the total bytes of standing-guard text the discriminator kept in the live file this pass. Guards are rotation-immune by design, so they accrete monotonically; a rising N across passes is the visible signal that a guard-retirement review — discharge by ruling, never rotation — is owed before the guard floor binds the budget). The live file's header carries ONE standing line — *"Rotated history → `PROME/archive/ACTIVE_DECISIONS_ROTATION_*.md` (per-pass manifest + crc in each file's header)"* — **never a per-pass enumeration with checksums** (HANDOFF's archive paragraph shows where that road goes: the pointer line itself becomes a whale).

### 2e. Explicitly out of scope
- No change to the file's Rules states/lifecycle, GATES/DOCKET relationships, or any decision's substance.
- Current Mode, Rules, tail sections stay (≈3.9 KB total, cheap and load-bearing).
- No scripted check at adoption — closeout-prose-side only, a **DECLARED CHOICE with a revisit trigger** *(amended 8/22 per review finding 3, which also corrected this bullet's original "matching STATUS/MEMORY precedent exactly" claim — MEMORY's check IS scripted [`check_memory_length.sh`, rc-keyed]; only STATUS's is prose, and the prose form has run late twice [121% and 97.7% before rotation, PAT-055])*: **if this file is found >100% of budget at any boot, the check gets scripted (rc-keyed, MEMORY pattern) — no re-litigation needed, the trigger is the ruling.**

## 3. First rotation pass (execute on approval, this session)

| Target | B now | Action | Est. B after |
|---|---:|---|---:|
| Header stamp chain | 9,041 | keep current 8/16 stamp; rotate priors | ~1,600 |
| VIXCS row (terminal) | 4,519 | rotate WHOLE (its own request, 23d overdue) | 0 |
| TLT-Jun18 / theta-cluster / FXY rows | 1,625 | rotate whole — the month-past-expiry holdovers Current Mode already says to fold; its Key-supersessions lines stay as the guard | 0 |
| Energy watch row | 5,982 | snapshot + rewrite (live: fragile-watch state, HY two-sided watch, Cushing auto-re-arm, tail-rider position, arm-RETIRED guard) | ~1,800 |
| Roster migration row | 5,384 | snapshot + rewrite (live: Phase-2 confirms owed DAEDALUS/WALTER · Phases 3-4 HELD) | ~1,200 |
| TERRY 004 row | 3,306 | snapshot + rewrite (live: ARMED · NO-ADD · harvest ×25 · concentration flag) | ~1,200 |
| FORGE row | 3,122 | snapshot + rewrite (live: PROME owns · open legs transferred to DAEDALUS) | ~1,000 |
| DAEDALUS onboarding row | 2,949 | snapshot + rewrite | ~800 |
| Memory-restructure row | 2,656 | snapshot + rewrite (live: DEWEY/RED confirms + boot-read cohort check) | ~900 |
| RESEARCH-INTAKE row | 2,090 | snapshot + rewrite | ~700 |
| DEWEY row | 2,032 | snapshot + rewrite (live: entitlement spec + batch-3 state) | ~700 |
| Reshape row | 1,956 | snapshot + rewrite (live: X1 gate + fenced legs + RIDE guard) | ~800 |
| **Projected file total** | **53,819** | | **≈ 20-23 K (~40-45% of budget)** |

Untouched: Kharg row (1,280 — but see rider), CORAL/WALTER/isolation rows (small), Current Mode/Rules/tail.

**Rider (content, not structure — disclosed, not smuggled):** the Kharg row still presents GATE-TERRY-006 as LIVE; HEARTBEAT records it **RETIRED 8/20 on instrument grounds, premise NOT refuted**. That's a decision-state sync, normal PROME maintenance on its own file — I'll update that state cell in the same pass, cited to the 8/20 ruling, flagged in the commit message. *(Amended 8/22 per review: the cell carries the FULL form — "RETIRED 8/20 on instrument grounds, premise NOT refuted" — never a bare RETIRED token; the impeachment killed the instrument, not the claim, and a bare token would over-state what died. Independently corroborated at the design layer's registry-check notes.)*

## 4. Verification plan
1. Every rotated chunk: crc32 computed pre-move, archive written, chunk re-read from archive, crc compared in-process — recorded in the commit message (STATUS pattern).
2. Post-rewrite guard sweep, **grep-assisted, not diff-eyeball** *(amended 8/22 per review finding 2)*: the diff against the snapshot is the outer check; the inner check greps the DROPPED text for directive markers (`do NOT`, `never`, `kill-on-sight`, `⛔`, `must`, `no re-present`, `re-verify`, `VERIFICATION_REQUIRED`) and **every hit is dispositioned in the manifest** — present in the rewrite, or intentionally retired with a reason. A human diff-read of nine rewritten whale rows is exactly where a guard slips through; the grep costs one command.
3. `wc -c` before/after in the commit. Boot-readability confirmed by a full single Read of the finished file.
4. DOCKET 2026-08-22 row → RESOLVED(executed) with byte counts; CLOSEOUT Chunk 1 gains the flow-rule bullet.

## 5. The ask (one batch word covers all four)
1. Adopt the flow rule (§2a) — budget/thresholds identical to STATUS.
2. Adopt snapshot-then-rewrite + guard discriminator (§2b) as the row-rotation mechanism.
3. Adopt the row-weight convention (§2c).
4. Execute the first pass (§3, incl. the Kharg rider) this session.

PROME rec: approve all four. The file is past the Read cap today — every boot until rotation reads a truncated decision index.

---

## 6. RELAYED REVIEW (filed verbatim per the n+3 file-before-disposition rule)
**Provenance:** arrived 2026-08-22 in-session via Will's channel, immediately after PROME's 4-item ask. Voice and content are consistent with the DAEDALUS design layer (PAT-123/PAT-055 self-references, STATUS-convention track record, GATE-TERRY-006 registry corroboration); authorship unconfirmed by the operator at filing time. Filed before disposition; existed nowhere durable until this block.

> Four findings from the design layer — two worth landing in the same approval word, two noted-not-blocking:
>
> Amendments I'd fold into the approval (both cheap):
>
> 1. Count guard-bytes in the rotation manifest. "Standing guards never rotate, however old" is correct — but it makes the guard class monotonically accreting by construction: rotation can never relieve it, so guard-bytes ratchet toward the cap over months and the flow rule slowly loses its relief capacity (PAT-123's joint-bind, where the only honest relief is discharge, not rotation). One manifest line per pass — "guard-bytes retained: N" — makes the floor visible before it binds, and signals when a guard-retirement review is owed.
> 2. Make the guard sweep grep-assisted, not diff-eyeball. §4.2's diff shows everything that changed; the discriminator check should specifically grep the dropped text for directive markers (do NOT, never, kill-on-sight, ⛔, must) with every hit dispositioned. A human diff-read of nine rewritten whale rows is exactly where a guard slips through; the grep costs one command.
>
> Noted, not blocking:
>
> 3. The trigger is a prose closeout step, and my own record says those run late. §2e declines a scripted check as "matching STATUS/MEMORY precedent exactly" — but the MEMORY precedent is scripted (check_memory_length.sh, rc-keyed, closeout step 1d), and the prose-only precedent's track record is mine: my STATUS byte convention hit 121% and 97.7% before rotation ran, twice (PAT-055 — closeout-willpower hygiene decays in ~10 days). Closeout-side-only is a legitimate choice for today; I'd just make it a declared choice with a revisit trigger (e.g., "if this file is found >100% at any boot, the check gets scripted") rather than a default — the ZHAO encode-the-choice rule.
> 4. The 51,200 B budget is inherited, not derived. It works here (38,400 B trigger vs. the ~54 KB where the Read cap actually bit — real headroom), but one sentence recording that arithmetic in the rule text anchors the threshold to the failure it prevents instead of to precedent, so a future density shift doesn't silently invalidate it (finding_inherited_default_threshold_is_a_silent_decision).
>
> On the Kharg rider: approve — and I can independently corroborate the fact: my own registry-check notes carry GATE-TERRY-006 as retired 8/20 with the state cell holding the worked example. One request: the cell should carry the full form — "RETIRED 8/20 on instrument grounds, premise NOT refuted" — not a bare RETIRED. The impeachment killed the instrument, not the claim, and a bare token would over-state what died.
>
> Net: approve all four as asked; amendments 1–2 are one manifest line and one grep, executable inside today's pass with no re-litigation

## 7. PROME disposition of the review (all four accepted; design amended in place above — see dated tags)
| # | Finding | Disposition |
|---|---|---|
| 1 | Guard-bytes accrete monotonically; manifest must count them | **ACCEPTED — folded into §2d/§4**: every rotation manifest carries `guard-bytes retained: N`; a rising N across passes is the signal a guard-retirement review (discharge, not rotation) is owed. Correct catch: the discriminator as drafted had no relief valve. |
| 2 | Guard sweep grep-assisted, not diff-eyeball | **ACCEPTED — folded into §4.2**: dropped text is grepped for directive markers (`do NOT`, `never`, `kill-on-sight`, `⛔`, `must`, `no re-present`, `re-verify`), every hit dispositioned in the manifest. The diff stays as the outer check; the grep is the inner one. |
| 3 | Prose closeout trigger runs late on the record; declare the choice + revisit trigger | **ACCEPTED as declared choice — folded into §2e**: closeout-prose-only is today's deliberate choice; revisit trigger encoded = *if this file is found >100% of budget at any boot, the check gets scripted (rc-keyed, MEMORY pattern)*. The "matching precedent exactly" wording was wrong as stated — MEMORY's check IS scripted; corrected. |
| 4 | Budget inherited, not derived — record the arithmetic | **ACCEPTED — folded into §2a**: the rule text now records that the budget anchors to the measured ~53-54 KB Read-truncation cap with the 75% trigger at 38,400 B ≈ 29% headroom below where truncation bit on 2026-08-22. |
| — | Kharg cell full form | **ACCEPTED**: the state cell will carry "RETIRED 8/20 on instrument grounds, premise NOT refuted" verbatim — instrument died, claim didn't. |

**Approval status:** the review's "approve all four" is a relayed recommendation, not an operator word (`[[finding_relayed_recommendation_is_not_an_approval]]`). Execution holds for Will's own word on the amended package.

---

## 8. EXECUTED (2026-08-22, same hour as the word)
| Step | Result |
|---|---|
| Rotation archive | `PROME/archive/ACTIVE_DECISIONS_ROTATION_2026-08-22.md` — 15 chunks, per-chunk crc32, **round-trip verified twice** (post-write + post-manifest-edit) |
| Live file | 53,819 → **23,466 B (46% of budget)**, 80 lines — **full single Read verified, no truncation** (the boot-Read failure that motivated the pass is cleared) |
| Guard sweep | grep-assisted per amendment 2; all hits dispositioned in the rotation file; **guard-bytes retained: 1,594 B** per amendment 1; **the sweep caught one genuinely dropped guard** (Kharg "trigger = FLOW state, never headline") and it was restored same pass — first live validation of the mechanism |
| Kharg rider | state cell synced, full form carried: "RETIRED 2026-08-20 on instrument grounds, premise NOT refuted" |
| Wiring | CLOSEOUT Chunk 1 flow-rule bullet (incl. revisit trigger + budget derivation) · ACTIVE_DECISIONS Rules gained the row-weight bullet · header carries rule + standing archive pointer |
| DOCKET | 2026-08-22 design-pass row → RESOLVED(EXECUTED) with byte counts |
