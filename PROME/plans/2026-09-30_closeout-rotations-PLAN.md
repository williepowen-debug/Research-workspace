# PLAN — three byte-flow rotations at the `prome-2a` Standard closeout (2026-09-30)

**Written:** 2026-09-30 23:19 ET (`date`), before any of the three live files is edited. Candidates are built by two scripts in the session scratchpad (`rot/build_ad_status.py`, `rot/build_scratch.py`) into `rot/cand/`; installing is the same scripts with `--install`.
**reads: 2 — the episode's budget is spent** (plan read delivered 23:35 ET, result read delivered 23:56 ET; both coldreader on Opus; no third read: no ❌ fix changed a rule's meaning)

**Why:** the boot gate read three boot-read-whole files at rotate-tier (`read_cap_check` rotation_due=3): `PROME/SCRATCH.md`, `PROME/ACTIVE_DECISIONS.md`, and `PROME/STATUS.md` at its trigger. Rule (READ_CAP rule 5, `PROME/CLOSEOUT_PROCEDURES.md` § Byte-flow): rotate verbatim until under 70% of the 32,550 B budget. Sizes come from `PROME/tools/measure.py`, never from this file.

## What moves, per file
| File | Rotated out (verbatim, crc'd) | To | Rewritten in place |
|---|---|---|---|
| `PROME/SCRATCH.md` | the header stamp line · the history-pointer line · the `prome-8c` resume block · the `prome-94` block and its owed list · the FLNG line · the carried-pointers paragraph · the operator card's As-of line · the HEARTBEAT amendment-queue paragraph (eight cuts; the eighth added after the plan read, ❌73) | `PROME/archive/SCRATCH_ROTATED_2026-09-30_prome-2a.md` | a `prome-2a` resume block; ONE owed list for the Thursday boot (items ①–⑧); shorter FLNG and carried-pointers paragraphs |
| `PROME/ACTIVE_DECISIONS.md` | the whole TERRY 004 row (pre-rewrite) · one stale clause of the CORAL row · one prior header stamp | `PROME/archive/ACTIVE_DECISIONS_ROTATION_2026-09-30.md` · `…STAMP_PRIORS_2026-09-12.md` | the TERRY row current-state-only, standing guards byte-for-byte; the CORAL clause replaced with the 9/28 ruling's state |
| `PROME/STATUS.md` | seven prior sitting statements in the WQ-299 row (9/28 16:0x → 9/29 21:4x) | `PROME/archive/STATUS_HISTORY.md` § 2026-09-30 | the header stamp; this sitting's WQ-299 statement |

## Invariants the reads check
1. **Verbatim and recoverable.** Every rotated block in an archive equals the bytes that left the live file at HEAD, and its stated crc32 recomputes.
2. **No live obligation lost.** Every owed item, directive or reminder in the rotated SCRATCH blocks is either carried into the new owed list, registered on a DOCKET / WILL_QUEUE / GATES row the new text names, or stated as done with where the evidence is.
3. **Standing guards untouched.** The TERRY row's `Standing guards (never rotate)` block is byte-identical before and after; guard-bytes retained is stated in the manifest.
4. **New statements are true at their sources.** Sample at the artifact: the 004 sale (`FORGE/STATUS.md`), VLO gate states and the CORAL re-fire registration (`PROME/GATES.tsv`), WQ-241 (`PROME/WILL_QUEUE.md`), DOCKET L524 and L559–L562, OTTO's dispositions (`AGENTS/OTTO/thesis/PREDICTIONS.tsv`).
5. **A stranger can resume.** From the new SCRATCH alone a cold reader can say what is owed first on Thursday, by when, and where each pointer leads.
6. **No figure a reader can recompute** is restated as a current size, and every clock in the new text came from `date`.

## Declared before the read
- The operator card is carried unchanged except its As-of line: no market or book fact moved tonight.
- STATUS's seven rotated statements (two of them) were marked "stay LIVE" at the 9/28 rotation; they are session history once their successors exist, and the latest prior (prome-94) stays beside tonight's.
- The scanner's disposition is deliberately NOT restated in SCRATCH or STATUS: both point at the acceptance file, which the third independent read may still change tonight.

## Reads and residue
### Read 1 — the PLAN read (blind, Opus; ledger kept in the session scratchpad, verdicts transcribed here 2026-09-30 23:42 ET)
**Verdict: 78 claims · 54 ✅ · 20 ⚠️ · 4 ❌ — "NO, do not install as they are."** All eleven verbatim moves and crc figures recomputed clean; the four ❌ were in NEW text.

| ❌ | Finding | Fix applied before install |
|---|---|---|
| 22 | SCRATCH dropped a live instruction: WQ-346 is research judgment and its delegation class must be classified in the WQ-348 inventory. | Added to owed item ⑤, with CATO's run as the source. |
| 45 | Owed item ③ told Thursday to register HOMER's cross-tab offer. It is WQ-335, RULED NOT NOW 9/30. PROME had also registered a duplicate (WQ-349) while the read ran. | ③ rewritten: register nothing; WQ-349 withdrawn (`PROME/WILL_QUEUE.md` RECENTLY DONE); WALTER packeted (de4b6a942); every surface that carried the false claim corrected; memory `finding_scan_keyed_on_naming_reads_local_form_as_absence` extended. |
| 46 | The TERRY row pointed D-49 at `FORGE/STATUS.md`, which no longer holds it. | Pointer → `FORGE/position_management.tsv` (the XLE $65C row). |
| 73 | The amendment-queue paragraph said "fold am.#1 + am.#2" and "chain would read 3"; HEARTBEAT is at chain 3 with am.#3. | Paragraph rewritten ("fold am.#1–#3"; an intraday amendment would be am.#4, over the <4 advisory); the prior paragraph rotates verbatim as CUT 8. |

**Also fixed (one-token, the rule's typo exception):** ⚠️65 "six" statements → seven (this file) · ⚠️71 "21:2x boot gate" → "21:20" in three archive headers (the boot run directory carries the clock).
**Folded into the ❌45 fix:** ⚠️68 (the R4 step is gone with ③) · ⚠️69 (SCRATCH and STATUS now name the acceptance file's § Disposition after read 3, the three operating limits and WQ-350) · ⚠️78 (the overtaken facts are now stated as they stand).

**Declared residue — ⚠️ NOT fixed (read budget: ❌ only):**
- ⚠️13 the prome-94 statement's tail sentence and one prior header stamp were rewritten, not archived — recoverable from `git log -p -- PROME/STATUS.md` only.
- ⚠️18 the "byte trip before then follows the 24th plan record's prune order" conditional was dropped; the plan record it named carries no prune order.
- ⚠️26 the archive header says the Standard steps skipped at the Light closeout were "run tonight" — true only once this closeout completes; no `prome-8c` HANDOFF entry was ever written (its account is `memory/2026-09-30.md` § prome-8c).
- ⚠️30 dropped sub-clauses: WD3 "keep 'candidate'" · LIQUID/FERT "never PROME's grade" · fred CDN "not written up" · the Abqaiq watch (WALTER's) · SCRATCH's own 10/02 size date.
- ⚠️34 "guard-bytes retained" counts through the card pointer and the kill-on-sight list, not only the bolded passage; the boundary is the builder's, byte-identical old vs new.
- ⚠️41 the CORAL clause calls the GATES condition cell "the letter"; the owner-side canonical letter is `AGENTS/CORAL/STATUS.md` (the GATES row is summary + pointer).
- ⚠️50 slate labels name rows, not always desks: CARL-DR-3 L468's owner is DEWEY; CRMT L479's owner is BROCK and its effective wake is the 10/2 boot.
- ⚠️66 owed item ① does not state the consequence of a miss (auto-exercise into a short-stock position in the IRA) or that the order is Will's own; both live on WQ-347.
- ⚠️67 "cap 4 per boot — bring Will a slate" does not say whether four spawn before the slate; `PROME/CLAUDE.md` (WQ-184) governs: four due-row spawns, the rest slated.
- ⚠️72 recomputable sizes carried in prose (HENRY's STATUS, BOOT.md, HEARTBEAT, BOND/NEXUS brief sizes) — stale by their next edit; the instruments are `scripts/read_cap_check.py` and `PROME/tools/measure.py`.
- ⚠️74 the operator card body still says "am.#2 … (chain 2)" under a stamp that says "carried UNCHANGED"; HEARTBEAT is at am.#3, chain 3. The card is rebuilt at the 25th re-base.
- ⚠️75 the retained STATUS prior stamp points at "SCRATCH ★ NEXT" for the Light closeout's skipped steps; they are now in the SCRATCH archive, CUT 3.
- ⚠️76 wording: D-66/67 are not "expired" items (only D-68 is); "four rolled lines" includes five NEW QQQ Oct-05 puts; the manifest says one leading sentence was added to the Next cell where two were.
- ⚠️77 the TERRY row is now a guard-holder plus TERRY's to-do list, against the file's own "remove or archive when terminal" rule — a restructure for a later pass, not tonight's.
- ⚠️64 was a count the reader could not verify: the builder now says eight memory extensions, counted from git.

### Read 2 — the RESULT read (blind, Opus; ledger in the session scratchpad, verdicts transcribed here 2026-09-30 23:57 ET)
**Verdict: 60 claims · 52 ✅ · 7 ⚠️ · 1 ❌ — "NO, because of the HANDOFF line alone; everything else holds."** All 13 archive blocks recompute and are byte-exact copies of the HEAD text; the standing-guards passage is byte-identical; the four fixes from read 1 check out at their sources; both generated views are fresh; 95 of 95 pointers resolve.

| ❌ | Finding | Fix applied after the read |
|---|---|---|
| 47 | The new HANDOFF entry listed "WQ-346 / 344 10/6" under decisions Will still owes. Both rows were RULED under his 19:32 ET blanket word and sit in RECENTLY DONE; the clause was copied from the prior entry, written before that ruling. | The clause is removed; the line now names WQ-347, WQ-350 and the Friday rows, and points at the queue's § OPEN for the rest. |

**Also fixed (one word):** ⚠️48 the HANDOFF entry said "seven memory extensions" where STATUS and git say eight.

**State of that fix: IMPLEMENTED, not independently verified by a rotation read** — it was made after the episode's final read. The closeout audit (ARGUS) reads HANDOFF as part of the commit candidate; that is a different review, and it is the only one this line gets.

**Declared residue from read 2 — ⚠️ NOT fixed:**
- ⚠️20 the prior owed list's item on CREED's two crash-lost items is neither carried nor named as done in PROME's files; CREED's own record closes both (KB-049; the student-housing packet folded into its next-boot move).
- ⚠️34 owed item ① reads as one packet per ask; TERRY's first packet carries both asks and the second is the standing-practice notice.
- ⚠️52 nothing but SCRATCH item ① triggers TERRY's Thursday wake — no DOCKET or GATES row names TERRY for 10/1, so the tier and whether it counts against the cap of four are not stated. PROME's reading: a follow-up inside an approved workstream (Tier 1), outside the due-row cap.
- ⚠️53 LIQUID and FERT are both ACTIVE owners by the spawn-list test, so the WQ-184 rule asks for a consumer read at the owner's artifact before any spawn; SCRATCH item ② does not say so.
- ⚠️57 the HANDOFF archive header carries 23:30 ET and the other archive headers 23:42 ET — two real write times for one closeout.
- ⚠️61 "WALTER: 22 intake items unrouted since its 9/29 closeout" is carried unrefreshed; WALTER closed out again on 9/30 and the count may be stale.
