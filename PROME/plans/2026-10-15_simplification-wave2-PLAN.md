# Simplification wave 2 — three queued changes, prepared before implementation (PROME; Will 2026-10-15 21:35 ET)

**Written:** 2026-10-15 21:3x–21:41 ET (PROME `prome-be`; committed ef7f44ecb 21:41 ET). Will's order (verbatim items): ① finish WQ-446 / L738 · ② backlog #10 (the WILL_QUEUE "Prior" stamp chain) · ③ backlog #7 (SCRATCH's generated docket view). Source records: `reports/2026-10-15_waste-survey.md` (items 7 · 10 · 17), `plans/2026-10-15_simplification-PLAN.md` (sequence 1), DOCKET L738, WQ-446 (RULED A 2026-10-15 16:16 ET, "approved."), CATO's advice in `AGENTS/CATO/runs/2026-10-15_2025_prome-simplification-oversight.md` § Next-work advice (prefer the generated view; preserve overdue/unknown obligations and the full-source path; generated-page timestamps are not a republish trigger). **Rules carried:** one process change per sitting (WQ-299 R1; WQ-445's exception is limited to its named wiring plan, not a general waiver); acceptance written before the edit (WQ-229); the tool changes (① and ③) each get one independent read; due research and position work first at every sitting; **the publication hold stands — nothing in this plan is pushed except inside a compliant reviewed (Standard) closeout**; WQ-448 still needs its bounded addendum (CATO 21:23 / 21:31 ET: SP3 stable snapshot during the gate · SP5 immutable push target through the actual push, explicit attribution for SHARED/UNATTRIBUTED work that is not PROME's, intent-journal cutover · initiator-independent enforcement at the installed `pre-push` hook) before any implementation of it — that addendum is a separate, bounded document, not part of this wave.

**Savings account (L739; corrected 21:5x ET on Will's point):** NO post-edit saving is established yet. The 20:01 ET boot PRECEDED the step-5 edit (made 20:07–20:10 ET): its four omitted standalone runs were a disclosed skipped control under the OLD manual, not evidence of the change. The gate's own logs were read to EOF at that boot (orchestration log 15 pages, session evidence 6, firetime 5 — the item-15 class, untouched by any change). The first observation of change 1 is the NEXT ordinary boot's report (A7's OBSERVED half): the gate runs once, the four do not run standalone, and no skipped-control line names them. Time per boot is not measured anywhere; the closeout side has no change to observe. #10's saving (a 21.6 KB line no longer read) is a measured size, not an observed time.

---

## ① WQ-446 / L738 — decide the Deck republish from the owed set, before reading the page (process change; the NEXT sitting's slot)

**Recurring work it removes (survey #17, measured 10/15 post-close):** 7 Read calls / ~100 KB of the hosted page read in full to learn whether a republish was owed, when the answer was NO-OP; plus one hand-written PUBLISH row judgment at every Standard+ closeout. After the change the gate prints the answer; the page is read only when a republish is owed (and then once, at the publish).

**Already approved — do not ask again.** WQ-446 A: the Deck OWED view republishes ONLY when the owed set changed since the last hosted build. L738 names the four encode sites (CLOSEOUT step 11 · a gate check · the runner's publish line + § Delivery · the symmetry row).

**What "the owed set" is (so the comparison covers the explanatory text):** every row `decision_deck.parse_open` returns from `PROME/WILL_QUEUE.md` § OPEN — open cards AND answered/hands-owed cards (the page renders both) — as its raw cells (n · item · kind · needed-by · since · rec · notes), PLUS, for each such `n`, the whole `PROME/registry/WQ_EXPLAINERS.tsv` row (name · what · why_yours · if_yes · if_no · if_nothing · rec_reason · options · options_source · domains). Nothing else: the build stamp, git sha, build id, the reference-page note and the Docket panel are NOT in the set (CATO: generated timestamps are not a trigger). The digest = sha256 over a canonical serialization (rows sorted by n; cells tab-joined; explainer appended per row).

**Smallest edit (reuse, no new reader) — amended 21:5x ET on Will's two additions:**
1. `PROME/tools/decision_deck.py`: `owed_fingerprints(text, expl) -> {n: sha256}` (one fingerprint per owed row over its raw cells + its whole explainer row) and `owed_digest(fps) -> sha256` over the sorted `n:fingerprint` pairs — the aggregate is derived from the per-row map, never computed alone, so added/removed/changed rows are identifiable. **The build captures what it rendered:** `build()` writes `PROME/state/deck_owed_build.json` `{digest, fingerprints, build_id, built_at, build_sha}` beside the rendered page (the build receipt — what this render contains). **The hosted record is written only after confirmed publication:** `--record-hosted-owed <version>` copies the BUILD receipt's digest and fingerprints (never a fresh computation from the queue) into `PROME/state/deck_owed_hosted.json` `{digest, fingerprints, version, published_at, build_id}` — so the record describes the page that reached the host, not the queue at record time. A failed or refused publish writes nothing; the previous hosted record stands.
2. `PROME/tools/prome_gate.py` `mode_closeout`: ONE advisory check "Deck republish (WQ-446 A)": it computes the CURRENT fingerprints from the queue + explainers and compares them with the HOSTED record: record absent/unreadable ⇒ `UNKNOWN — no hosted owed record: republish at this Standard+ closeout and record it` (never NO-OP on silence); all fingerprints equal ⇒ `NO-OP (owed set unchanged since v<N>, <published_at>)`; otherwise ⇒ `OWED — since v<N>: +<added n…> −<removed n…> ~<changed n…>` from the per-row map (changed = same n, different fingerprint — covers explainer edits). The BUILD receipt is not consulted by the check (a render is not a publish).
3. `PROME/CLOSEOUT.md` step 11: replace "the Deck OWED view at its private URL at every Standard+ closeout" with "the Deck OWED view when the gate's WQ-446 check reads OWED or UNKNOWN; NO-OP is recorded, not published; after a hosted publish run `decision_deck.py --record-hosted-owed <version>` in the same sitting"; § Delivery: PUBLISHED/PARTIAL judged against that check; symmetry row's Deck cell follows; the `/closeout` runner's step 6 line names the check (both copies identical).
4. `CLOSEOUT_PROCEDURES.md`: no change unless its Deck pointer restates the old rule (check at implementation; delete-and-point, never a correction beside).

**Acceptance evidence (write `PROME/tools/tests/ACCEPTANCE_L738_deck_owed_digest.md` first; tests in `test_deck_owed_digest_L738.py`, fixture queue + explainers, never the live files):**
- A1 Ordinary: two renders of the same queue/explainers minutes apart ⇒ identical digest (stamp/sha excluded).
- A2 Ordinary: a changed `notes` cell on an OPEN row, a changed explainer `what` cell, an added row, a row ruled out of OPEN ⇒ four different digests, and the gate line names +/−/~ correctly.
- A3 🔴 Overlap: an answered (hands-owed) row still in OPEN counts; a row that moves to RECENTLY DONE no longer counts (it is the page's own membership rule).
- A4 Missing information: no hosted record ⇒ UNKNOWN ⇒ republish owed (the first run after implementation republishes once and seeds the record — the 17:56 ET NO-OP judgment was a reading, never a digest, so no retroactive seed).
- **A4b (Will) — build A, queue changes to B, publish A:** render at queue state A (build receipt = A); edit the queue to B; publish A's page and run `--record-hosted-owed`; the hosted record must carry A's digest/fingerprints (from the build receipt), and the gate must then read OWED naming B's changed rows — never NO-OP from a fresh computation at record time.
- **A4c (Will) — failed publication preserves the previous record:** with a hosted record for v<N> on disk, a publish that fails or is refused (the test substitutes the publish step) leaves `deck_owed_hosted.json` byte-identical; `--record-hosted-owed` is never run on a failure, and if run with a build receipt that does not match the page the sitting published (build_id mismatch supplied by the test) it refuses.
- **A2b (Will) — row differences are real:** from a hosted record with rows {a,b,c} and a current set {a,b′,d}, the gate line reads `−c +d ~b` exactly; one aggregate digest alone is not accepted as the record.
- A5 Wrong owner: the Helm and the REFERENCE view are untouched (WQ-382 a/b): the check reads and writes nothing about them.
- A6 Concurrent activity: N/A — one writer (`--record-hosted-owed`), run by PROME in the publishing sitting.
- A7 Wiring: CLOSEOUT step 11 + runner + § Delivery + symmetry row name the check (WIRED); the next Standard closeout's record shows the gate line deciding the publish (OBSERVED).
- Replaces: the full-page read at every Standard+ closeout and the hand judgment. One independent read (Opus: a gate check on a Will-facing delivery, WQ-447).

---

## ② Backlog #10 — move the WILL_QUEUE "Prior" stamp chain to an archive (hygiene on a PROME state surface; no rule, tool, gate or charter changes — NOT the sitting's process change; executed 21:3x–21:41 ET (committed ef7f44ecb) under that classification, kept by Will 21:54 ET)

**Review status (disclosed 21:5x ET on Will's point — the hygiene label waives nothing):** a verbatim MOVE of text between files is in the `PROME/CLAUDE.md` § Read budget class — ONE plan read before the edit, ONE result read after. **The plan read was NOT done** and cannot be done now (the edit exists); that requirement is MISSED, not satisfied by anything below. **The result read** (coldreader on Sonnet, 21:55–21:57 ET, ledger scratchpad `coldread_wq10.md`): **RELEASE — 5/5 claims verified, 0 ❌, 4 ⚠️**; the reader recomputed the move itself (removed substring 21,618 B crc32 342662644 == archive body), re-ran the stamp regex (2026-10-15), found no `Prior:` consumer and no `WILL_QUEUE_*` glob collision, confirmed lines 1–15 and 17–142 identical before/after, and READ all 54 stamps (plus 22 nested) for live instructions — none live; two 'owed' phrasings are closed by later stamps. **reads: 1 (result only; the plan read is MISSED).** Declared residue, not fixed after the read: ⚠️1 the line's new sentence 'older stamps move to that archive at each spine audit' is a standing duty with no owning step — the commit's 'no rule change' overstated; owner = the next spine audit's fix round, which already reconciles header stamps (a one-line addition to `/spineaudit`, a process slot, or drop the sentence to a pointer); ⚠️2 the commit bundled five paths, so 'one line + one file' describes the MOVE, not the commit; ⚠️3 '54' counts top-level stamps (≈77 dated stamps including nested ones); ⚠️4 the archive carries no 'dated history, not instructions' banner although two stamps use 'owed' wording — add at the next touch of the archive. The receipts that DO exist are instrument receipts, not reads: moved-substring crc32-no-final-nl 342662644 == archive body; stamp regex match at the same date; `queue_parser_selftest` 26/26; `wq_ledger check` 1100 rows; `willq_view --check` agrees; the Deck build unchanged; `git diff --stat` one line + one new file.

**Recurring work it removes (survey #10, measured):** `PROME/WILL_QUEUE.md` line 16 is **22,227 B in one line** (measured 21:4x ET) — 54 "Prior:" stamps from 2026-09-17 to 2026-10-10 behind the live "Last reconciled" stamp — read at every boot and closeout by whoever opens the file whole, and copied into every Deck/ledger parse of the file (the parsers skip it, the bytes still travel). Only the FIRST stamp is consumed by anything: `prome_gate.check_will_queue` (`^\*\*Last reconciled:\*\*\s*(\d{4}-\d{2}-\d{2})`, line-anchored) and `queue_parser_selftest.py` (synthetic header, same shape). No reader consumes a "Prior:" clause (grep over `PROME/tools`, `scripts`, both `.claude` trees: none).

**Smallest edit:** keep line 16's first sentence (the current stamp with its own parenthetical) verbatim; replace everything from the first ` Prior: ` to the end of the line with one pointer sentence: ` Prior stamps (54, 2026-09-17 → 2026-10-10) → `PROME/archive/WILL_QUEUE_RECONCILE_CHAIN_2026-10-15.md`; this line keeps the latest stamp and at most ONE prior; older stamps move to that archive at each spine audit.` The removed text goes into that archive file VERBATIM under a four-line header. Every live decision row, every obligation and every other header line is untouched.

**Acceptance evidence (measured before and after, in the commit body):**
- A1 Ordinary: the stamp regex still matches line 16 at the same date (`2026-10-15`); `prome_gate closeout --tier light` advisory line for WILL_QUEUE unchanged in meaning; `queue_parser_selftest` rc 0.
- A2 🔴 Overlap: the OPEN table, RECENTLY DONE, the ledger (`wq_ledger.py check` 1100 rows unchanged) and the Deck parser see the same rows (`decision_deck.py` renders the same open/answered counts; `willq_view.py --check PROME/SCRATCH.md` agrees).
- A3 Missing information: the archive holds the moved substring byte-for-byte — crc32 of the removed substring (measure.py on a scratch file) equals crc32 of the archive body below its header; the archive is linked from the line that lost the text.
- A4 Wrong owner: no row of any other owner changes; the diff touches line 16 only (`git diff --stat` = 1 line changed in WILL_QUEUE + 1 new archive file).
- A5 Concurrent activity: N/A — one writer, one line.
- A6 Size: WILL_QUEUE.md 125,010 B → under 104,000 B (`measure.py`); the file is a `summary` read in the manifest, so no cap verdict changes; the regrowth rule (one prior kept, archive at each spine audit) is on the line itself.
- Replaces: ~21.6 KB read per boot/closeout open of the file and the growth of one stamp per sitting into it.

---

## ③ Backlog #7 — shrink SCRATCH's generated docket view through its generator (process change: a tool edit; the slot AFTER ①)

**Recurring work it removes (survey #7, measured 21:5x ET):** the generated block is **12,462 B** of SCRATCH's 26,292 B (47%) — read whole at every boot (SCRATCH is a `whole` read, at 81% of budget, rotate-tier since 10/14). By section: header 360 · OVERDUE 1,677 · UNDATED 1,269 · **forward window 9,015** · beyond 109. The forward window is 83 rows over 21 days, each with catalyst text (90 chars inside 7 days, ~48 beyond), owners and L#.

**What must be preserved (Will's conditions + CATO):** every OVERDUE row (72 tonight; **12 of them appear on no other boot surface** — not in the gate's spawn list and not COVERED-annotated: L40 · L263 · L358 · L361 · L362 · L364 · L367 · L370 · L403 · L467 · L686 · L696 — measured 21:4x ET; so the OVERDUE list stays whole), every UNDATED row (36; session-keyed unfinished work), the counts of everything not rendered, the docket-crc vintage, L# citations and the source path (the full-docket access).

**Smallest generator edit (`scripts/docket_view.py` `render()`):** beyond `detail_days` (7), render a forward row as `L# owner` only (no catalyst text), grouped by date as now; inside 7 days unchanged (90 chars). The far rows' text remains one `sed -n <L>p PROME/DOCKET.tsv` away and in the Helm's `docket.html`; the header gains the words "far rows: L# + owner only — text at the L#". Window (21 d) and the OVERDUE/UNDATED sections unchanged. Expected block ≈ 7.5–8 KB (forward ≈ 4.2 KB at ~30 B/row for the ~70 far rows + full text for the ~13 near rows), SCRATCH ≈ 21.8 KB ⇒ **below the 70% stop (22,785 B)** without a rotation — the rotation owed since 10/14 is discharged by the generator, not by hand.

**Acceptance evidence (write `PROME/tools/tests/ACCEPTANCE_docket_view_far_rows.md` first; drills added to the generator's own `--selftest`, which already uses a synthetic docket):**
- A1 Ordinary: a far row renders as `L# owner`; a near row (≤7 d) renders with its text as before; both still group under their date head.
- A2 🔴 Overlap: a window row that STARTED before as-of and ends far ahead (`(since …→…)`) is near (rendered in full) — the existing `max(start, as_of)` grouping decides, never the end date.
- A3 Missing information: OVERDUE and UNDATED sections byte-identical to today's output for the same docket; the counts line unchanged; `--check-generated` FRESH after `--write`; idempotent second write = zero diff.
- A4 Wrong owner: `prome_gate` "generated calendar freshness" and "handwritten calendar coverage" pass unchanged; the Helm's `docket.html` (its own renderer) untouched.
- A5 Concurrent activity: N/A — one generator, one marked block.
- A6 Size: block ≤ 8,000 B and SCRATCH < 22,785 B measured after the write; `--budget` default (6,000) revisited only if the measured block still exceeds it (then the budget line, not the content, is wrong).
- A7 Wiring: nothing to wire — the generator already runs at closeout (symmetry table) and the gate already checks freshness. One independent read (Sonnet: single-artifact, the rendered block vs the docket; WQ-447).
- Replaces: ~4.5 KB per boot read of SCRATCH and the pending hand rotation of SCRATCH.

---

## Order and slots
Tonight (prome-be, slot already spent on change 1): this plan; ② executed as hygiene (disclosed). Next sitting with a free slot and no due domain/position row ahead of it: ① (approved, L738 due 10/16). The sitting after: ③. The WQ-448 addendum is written when its slot comes and is not implemented before Will's word. Each implementation sitting ends in a reviewed Standard closeout so the held train (31062bfc6 and what follows) ships under the existing rule, never by the bypass.

---

## Will's word — session exception, 2026-10-15 23:55 ET (PROME session b486657a; pasted verbatim, nothing paraphrased)

> For this session only, I authorize two process changes: **L738 first, followed by backlog #7**, provided L738 passes its applicable checks and independent review.
>
> This is a specific exception, not a general lifting of the one-change-per-session ceiling. WQ-445's broader proposal remains a separate decision.
>
> **L738:** Complete the code, acceptance tests, manual updates, and runner integration before final independent review. Preserve the distinction between rendered, committed, and successfully hosted content. Include the amended publication-snapshot and row-difference tests.
>
> **Backlog #7:** Proceed only after L738 passes. Reduce the redundant SCRATCH docket content while preserving complete OVERDUE and UNDATED information, urgent preparation cues, counts, and access to the full authoritative docket.
>
> **WQ-448:** You may complete the bounded addendum, but do not implement the push-control redesign without separate approval.
>
> **Measurement:** Record that the four removed standalone checks did not recur during this boot. Do not claim elapsed-time or model-usage savings that haven't been measured. Preserve the known startup-banner exception.
>
> **Priorities:** Scheduled financial research, catalyst wakes, and position-facing work take precedence. Do not force both process changes to completion if doing so compromises those obligations.
>
> Complete delivery through the existing reviewed closeout requirements. Avoid creating new recurring documentation or verification obligations unless they replace something necessary.
>
> Our objective is less recurring operational work, not simply more completed process changes.

**PROME's reading (same minute):** the session ceiling is TWO for this session only (L738, then ③/#7 after L738 is INDEPENDENTLY VERIFIED); WQ-445 stays OPEN and unruled; the WQ-448 addendum may be written, nothing of WQ-448 implemented; the change-1 OBSERVED half is recorded at the acceptance file (A7) from this boot's gate log; no time or usage saving is claimed; the step-0 banner `env_doctor` path (W5) stays.

## Will's word — wave close-out priorities, 2026-10-16 00:44 ET (PROME session b486657a; pasted verbatim)

> Finish the current wave with these priorities:
>
> 1. Repair L738's publication binding. CATO reproduced this failure: build A, save A's page, change the queue and build B within the same minute, then record A as published. The tool accepts B's receipt and incorrectly returns NO-OP.
>
> Bind the receipt to the exact rendered page. Increasing timestamp precision alone is insufficient. Use CATO's reproduction at AGENTS/CATO/runs/2026-10-15_2025_prome-simplification-l738-collision-probe.py as a regression case. The result must either refuse mismatched evidence or correctly record A while B remains OWED.
>
> 2. Review the final L738 candidate. Within this existing episode, I authorize the bounded correction/read-budget exception needed for this repair and one targeted final independent review, covering the collision fix and the already-unreviewed post-read edits, including affected instructions. Preserve the review history; do not reset the episode or expand into unrelated cautions. Keep the publication-snapshot, row-difference, date-sensitive display and failed-publication tests passing. Do not rely on the new NO-OP mechanism until this is resolved.
>
> 3. Stop expanding #7. Preserve the seven-day detail window, urgent preparation cues, and complete overdue/undated sections. Report the actual reduction and A6's unmet target. Accurately disposition any remaining rotation work; do not compress further merely to meet the original estimate.
>
> 4. Complete the existing reviewed closeout. Distinguish COMMITTED, PUSHED and PUBLISHED, verify the actual hosted build, and record its matching receipt only after confirmed publication. Clearly name anything still pending.
>
> WQ-448's addendum remains a separate, unapproved proposal. No third optimization or additional broad audit is authorized. Due research and position work retains priority.

## Will's word — reboot closure, 2026-10-16 10:45 ET (PROME session b486657a; pasted verbatim)

> Finish this sitting with bounded closure, then stop for reboot.
>
> 1. Consume CATO's review, commit d46977765. Use its targeted checks as the evidence for L738's final command-line correction. Reconcile the outstanding hold and resume the already-approved NO-OP behavior if that was its sole remaining condition. Preserve the requirement to record from the downloaded copy after confirmed publication. Do not commission another identical review; name any specific surviving blocker.
>
> 2. Run the omitted fire-time check on the affected citing artifacts and disposition its results.
>
> 3. Keep WQ-448 unapproved. Record CATO's remaining D1 condition: checks must examine the same fixed snapshot that receives the receipt. Include the "change, check, change back" counterexample in its acceptance conditions. No implementation or broader redesign this sitting.
>
> 4. Preserve the seven-day docket cues. No further compression now. Leave WQ-445 and WQ-449 for their separate rulings.
>
> 5. Complete normal reviewed closeout, accounting for pending state files and distinguishing committed, pushed and published. Explicitly identify anything that legitimately carries forward.
>
> Leave a short reboot handoff with Friday's due research and position-facing work first. Then stop—no new process initiative before reboot.

**PROME's reading (same sitting):** the NO-OP hold's sole condition was one independent read of the `--page` change; CATO's d46977765 checks are that read ⇒ hold lifted, downloaded-copy recording preserved; no surviving blocker on the NO-OP mechanism (residue listed in the acceptance file). Fire-time rerun done and dispositioned. WQ-448 D1 corrected to a materialized snapshot + A17d; unapproved. #7 untouched. Reviewed closeout with the five carried state files; then stop.

## Carried items (moved here from SCRATCH ★ NEXT at the 2026-10-16 11:00 ET closure; this is their home)
- Next process slots, one per sitting: WQ-445 is Will's (10/16); then `plans/2026-10-15_simplification-PLAN.md` sequence 2 — retire unneeded generated outputs (#8 · #9 · #11; #8 and #11 touch Will-gated surfaces, his word first).
- #10 follow-up: at the next reconcile-stamp write of `PROME/WILL_QUEUE.md` line 16, replace the sentence 'this line keeps the latest stamp and at most ONE prior; older stamps move to that archive at each spine audit' with a PLAIN POINTER to the archive — no recurring duty (Will 22:36 ET 10/15); not a separate edit.
- The two-correction stop is TRIPPED on `PROME/tools/decision_deck.py` and `PROME/CLOSEOUT.md`: any further correction to either needs an independent read first (`PROME/CLAUDE.md` § Review budget).
- `test_gate_isolation_L294_F7` ×4 = the pre-existing L737 class, untouched.
