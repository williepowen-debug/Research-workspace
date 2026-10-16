# Simplification wave 2 — three queued changes, prepared before implementation (PROME; Will 2026-10-15 21:35 ET)

**Written:** 2026-10-15 21:5x ET (PROME `prome-be`). Will's order (verbatim items): ① finish WQ-446 / L738 · ② backlog #10 (the WILL_QUEUE "Prior" stamp chain) · ③ backlog #7 (SCRATCH's generated docket view). Source records: `reports/2026-10-15_waste-survey.md` (items 7 · 10 · 17), `plans/2026-10-15_simplification-PLAN.md` (sequence 1), DOCKET L738, WQ-446 (RULED A 2026-10-15 16:16 ET, "approved."), CATO's advice in `AGENTS/CATO/runs/2026-10-15_2025_prome-simplification-oversight.md` § Next-work advice (prefer the generated view; preserve overdue/unknown obligations and the full-source path; generated-page timestamps are not a republish trigger). **Rules carried:** one process change per sitting (WQ-299 R1; WQ-445's exception is limited to its named wiring plan, not a general waiver); acceptance written before the edit (WQ-229); the tool changes (① and ③) each get one independent read; due research and position work first at every sitting; **the publication hold stands — nothing in this plan is pushed except inside a compliant reviewed (Standard) closeout**; WQ-448 still needs its bounded addendum (CATO 21:23 / 21:31 ET: SP3 stable snapshot during the gate · SP5 immutable push target through the actual push, explicit attribution for SHARED/UNATTRIBUTED work that is not PROME's, intent-journal cutover · initiator-independent enforcement at the installed `pre-push` hook) before any implementation of it — that addendum is a separate, bounded document, not part of this wave.

**Observed savings so far (L739 accounting — read off records, not estimated):** at the 20:01 ET boot after change 1, the four standalone step-5 runs did not happen (4 tool calls) and the 51 firetime flags printed once instead of twice; the gate's own logs were still read to EOF (orchestration log 15 pages, session evidence 6, firetime 5 — the item-15 class, unchanged). Time per boot is NOT measured; A7's OBSERVED half (the next ordinary boot report runs the gate once and names no skipped control for those four) is still pending. What remains unobserved: whether reading goes faster, and the closeout side (nothing in change 1 touched closeout).

---

## ① WQ-446 / L738 — decide the Deck republish from the owed set, before reading the page (process change; the NEXT sitting's slot)

**Recurring work it removes (survey #17, measured 10/15 post-close):** 7 Read calls / ~100 KB of the hosted page read in full to learn whether a republish was owed, when the answer was NO-OP; plus one hand-written PUBLISH row judgment at every Standard+ closeout. After the change the gate prints the answer; the page is read only when a republish is owed (and then once, at the publish).

**Already approved — do not ask again.** WQ-446 A: the Deck OWED view republishes ONLY when the owed set changed since the last hosted build. L738 names the four encode sites (CLOSEOUT step 11 · a gate check · the runner's publish line + § Delivery · the symmetry row).

**What "the owed set" is (so the comparison covers the explanatory text):** every row `decision_deck.parse_open` returns from `PROME/WILL_QUEUE.md` § OPEN — open cards AND answered/hands-owed cards (the page renders both) — as its raw cells (n · item · kind · needed-by · since · rec · notes), PLUS, for each such `n`, the whole `PROME/registry/WQ_EXPLAINERS.tsv` row (name · what · why_yours · if_yes · if_no · if_nothing · rec_reason · options · options_source · domains). Nothing else: the build stamp, git sha, build id, the reference-page note and the Docket panel are NOT in the set (CATO: generated timestamps are not a trigger). The digest = sha256 over a canonical serialization (rows sorted by n; cells tab-joined; explainer appended per row).

**Smallest edit (reuse, no new reader):**
1. `PROME/tools/decision_deck.py`: `owed_digest(text, expl) -> str` built from the existing `parse_open` + `load_explainers`; CLI `--owed-digest` prints it; CLI `--record-hosted-owed <version>` writes `PROME/state/deck_owed_hosted.json` `{digest, version, published_at, build_sha}` (the sibling of the existing `deck_reference_hosted.json`, same shape discipline).
2. `PROME/tools/prome_gate.py` `mode_closeout`: ONE advisory check "Deck republish (WQ-446 A)": state file absent/unreadable ⇒ `UNKNOWN — no hosted owed digest on record: republish at this Standard+ closeout and record it` (never NO-OP on silence); digest equal ⇒ `NO-OP (owed set unchanged since v<N>, <published_at>)`; differs ⇒ `OWED — owed set changed since v<N>: +<added n> −<removed n> ~<changed n>` (changed = same n, different bytes — covers explainer edits).
3. `PROME/CLOSEOUT.md` step 11: replace "the Deck OWED view at its private URL at every Standard+ closeout" with "the Deck OWED view when the gate's WQ-446 check reads OWED or UNKNOWN; NO-OP is recorded, not published; after a hosted publish run `decision_deck.py --record-hosted-owed <version>` in the same sitting"; § Delivery: PUBLISHED/PARTIAL judged against that check; symmetry row's Deck cell follows; the `/closeout` runner's step 6 line names the check (both copies identical).
4. `CLOSEOUT_PROCEDURES.md`: no change unless its Deck pointer restates the old rule (check at implementation; delete-and-point, never a correction beside).

**Acceptance evidence (write `PROME/tools/tests/ACCEPTANCE_L738_deck_owed_digest.md` first; tests in `test_deck_owed_digest_L738.py`, fixture queue + explainers, never the live files):**
- A1 Ordinary: two renders of the same queue/explainers minutes apart ⇒ identical digest (stamp/sha excluded).
- A2 Ordinary: a changed `notes` cell on an OPEN row, a changed explainer `what` cell, an added row, a row ruled out of OPEN ⇒ four different digests, and the gate line names +/−/~ correctly.
- A3 🔴 Overlap: an answered (hands-owed) row still in OPEN counts; a row that moves to RECENTLY DONE no longer counts (it is the page's own membership rule).
- A4 Missing information: no state file ⇒ UNKNOWN ⇒ republish owed (the first run after implementation republishes once and seeds the record — the 17:56 ET NO-OP judgment was a reading, never a digest, so no retroactive seed).
- A5 Wrong owner: the Helm and the REFERENCE view are untouched (WQ-382 a/b): the check reads and writes nothing about them.
- A6 Concurrent activity: N/A — one writer (`--record-hosted-owed`), run by PROME in the publishing sitting.
- A7 Wiring: CLOSEOUT step 11 + runner + § Delivery + symmetry row name the check (WIRED); the next Standard closeout's record shows the gate line deciding the publish (OBSERVED).
- Replaces: the full-page read at every Standard+ closeout and the hand judgment. One independent read (Opus: a gate check on a Will-facing delivery, WQ-447).

---

## ② Backlog #10 — move the WILL_QUEUE "Prior" stamp chain to an archive (hygiene on a PROME state surface; no rule, tool, gate or charter changes — NOT the sitting's process change; executed tonight under that classification, disclosed so Will or CATO can object)

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
