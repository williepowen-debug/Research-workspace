# Correction closure (Codex 2026-09-05 report) — PROME verification RECORD + P4 sitting pre-read

**Owner:** PROME · **Created:** 2026-09-05 17:2x ET Sat (DESKTOP, session `prome-22`) · **Status:** Will *"Okay do it"* 17:23 on PROME's three-step proposal (this record · DOCKET row for the P4 sitting · route the four-case walk to DAEDALUS). **No canon touched. Nothing here is a ruling** — the ruling package goes to Will AT the sitting (DOCKET L282).

**Subject artifact:** `PROME/codex/findings/2026-09-05_correction-closure-architecture-report.md` (Codex, committed `ab66194de` 13:40 by Will). **Untouched** — Codex's text stands as written; every amendment lives HERE so the report remains the reviewer's own record. Codex's second-pass self-review reached PROME in-session (Will relay, 17:18) and has no artifact of its own; its operative points are quoted in §3.

**Venue:** WQ-109 (ruled 2026-09-01: *"P4 (correction-class validation C1–C5) … one sitting, DAEDALUS presents"*). That leg had **no DOCKET row until this record** — registered L282 (2026-09-17, pre-read due 9/15).

---

## 1. PROME verification at the artifacts (16:4x–17:2x, HEAD `ab66194de`)

Five-field ledger. Tokens per `PROME/CLAUDE.md` § Session Process Controls.

| # | Claim | Artifact | Command | Observed | Token |
|---|---|---|---|---|---|
| F1 | Owner correction form already requires class · replacement · survives · kill-strings · absence-scope | `AGENTS/DAEDALUS/BLUEPRINTS/CORRECTION_FORM.md` | read | fields ①–⑤ present as described; "one write, both homes" rule present | VERIFIED |
| F2 | Class 11 ladder ROUTED → DELIVERED → CONSUMED → ENCODE-CONFIRMED → CLOSED-VERIFIED; CONSUMED ≠ surfaces changed | `AGENTS/DAEDALUS/BLUEPRINTS/STATE_VOCABULARY.md` § Class 11 | `grep -n 'Class 11\|CLOSED-VERIFIED'` | L184–197; operative rule "nothing resolved below ENCODE-CONFIRMED; CLOSED-VERIFIED requires the artifact check" | VERIFIED |
| F3 | Checker loads receipts as a set of IDs; action/note discarded; any receipt clears the named row | `scripts/corrections_boot_check.py` `cmd_check` | `grep -n 'receipts = set\|receipts.add'` | `receipts = set()`; `receipts.add(r.get("correction_id"))` — `action`/`note` never read | VERIFIED |
| F4 | Register prune = "all named targets receipted, or date_cap passed" | `AGENTS/WALTER/registry/CORRECTIONS.tsv` header | read | verbatim as quoted | VERIFIED |
| F5 | C1–C5 proposal exists; WQ-109 assigns P4 a sitting | `AGENTS/DAEDALUS/design/2026-08-28_CORRECTION_CLASS_VALIDATION_PROPOSAL.md` · `PROME/proposals/2026-09-01_wq-batch-RULED.md` row 109 | read | both as described | VERIFIED |

**PROME additions — the live state is thinner than the report says:**

| # | Claim | Artifact | Command | Observed | Token |
|---|---|---|---|---|---|
| P1 | The receipt `note` (evidence) field has never been used | `AGENTS/*/registry/corrections_receipts.tsv` + `PROME/registry/…` | `cat … \| grep -v '^receipt_date' \| grep -c .` | **19 receipts** against **22 named recipient obligations** (6 rows; hand-count of the `targets` column); **every `note` cell empty** — *(first write said 17 and was wrong: Codex recount 17:3x, PROME re-verified; the obligation count first came out 26 because `tail -n +12` swept a `#` comment line — a contaminated instrument, error #97)* | VERIFIED |
| P2 | The register's status column has never changed | `CORRECTIONS.tsv` | read col 7 | 6 rows, **all `LIVE`**; 0 `RECEIPTED`, 0 `RETIRED`; COR-20260826-02 (cap 2026-08-28) still `LIVE`; three rows have receipts from EVERY named target and still read `LIVE` | VERIFIED (state) · **INFERRED** that no prune was ever *attempted* — an all-LIVE column proves non-maintenance, not non-attempt (Codex) |
| P3 | Cap expiry silently clears a target's boot block in the CHECKER, not only in the prune | `corrections_boot_check.py` + SAM | `corrections_boot_check.py SAM` | `0 OK … 1 dead-at-cap; receipts on file: 0` — SAM never receipted COR-20260826-02 and passes | VERIFIED |
| P4 | Live unreceipted named targets exist — **two**, not one | HAWK · HOMER | `corrections_boot_check.py <X>` over all 15 named targets | **HAWK** COR-20260828-01 and **HOMER** COR-20260828-04, both `[LIVE]` unreceipted since 8/28, both dark. ⚠️ **HAWK's is missing BOOKKEEPING, not analysis:** `AGENTS/HAWK/board_log.tsv` 2026-09-02 row records *"Checked: no HAWK surface carries $86.36"* — the substantive no-op was done 9/2, the receipt was never written. Same shape at VIOLET: board log audit 8/27, formal receipt 9/3 — receipt time overstates handling latency by ~6 days *(first write named only HAWK and framed it as unread — corrected on Codex's third pass)* | VERIFIED |
| P5 | The report's three pilot corrections are NOT in the register | `CORRECTIONS.tsv` | `grep -ciE 'CVNA\|weekday\|MOHELA\|CFPB\|Qatar'` | the CVNA L131 unwind, the ES-02 reading-rule defect, the HANS Qatar-date fix all travelled by PROME packet / DOCKET; no `COR-` row | VERIFIED |
| P6 | STUE is not a checker-addressable desk | `corrections_boot_check.py STUE` | run | `2 CANNOT-EVALUATE: unknown agent 'STUE'` (correct: STUE is CARL's sub-agent) | VERIFIED |
| P7 | The form's LABELLED kill-string field (④) is absent on most registered corrections | the six `BOARD/SIG-W-*` files the register points at | `grep -ciE 'kill'` per file | label present on **1 of 6** (COR-20260828-04, DEWEY); 0 on the other five. ⚠️ **The grep keys on the label, not the substance:** the Brent correction carries a usable dead literal in prose (*"$86.36 ❌ WRONG"*) with no field label — so "no usable superseded literals were supplied" is **NOT established** (`[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]`) | VERIFIED (label absence) · **UNKNOWN** (literal absence) |
| P8 | The P4 sitting had no DOCKET row | `PROME/DOCKET.tsv` | `grep -nE 'P4\|C1.C5\|correction-class'` | only the R9 deferral row (L207) — no P4 row before L282 | VERIFIED |

---

## 2. Disposition of the report — what stands, what PROME amends

**Retained as written (Codex §3 contract, §7 non-goals, §8 ruling items, the stop rule):** receipt ≠ closure · APPLIED / justified NO-OP terminal, DEFERRED / CONTESTED / missing not · immutable correction generation with supersession · conditional `validation_ref=<pointer>|NONE` · `ALL` = dissemination not reconciliation · no new ledger / dashboard / agent / forum / cadence. **Nothing cut.**

**Amendments (PROME, recorded here, not written into the report):**

| # | Amendment | Basis |
|---|---|---|
| A1 | **The top output token cannot be `CLOSED-VERIFIED` on structural checks alone.** Receipt-action + note-syntax + path-existence establishes `RECEIPTED-WITH-POINTER`, nothing more. `CLOSED-VERIFIED` requires a content assertion at the named artifact. | Codex self-review point 1 (§3); P1/P7 |
| A2 | **The buildable content assertion is the form's own field ④:** named artifact exists AND contains none of the correction's kill-strings (scoped to the declared class). Cheap, no new field — but the labelled field exists on 1 of 6 registered corrections today, so **form compliance precedes code.** ⚠️ **Limits (Codex):** a kill-string scan misses PARAPHRASED stale claims and flags correctly-preserved superseded QUOTATIONS — it is search EVIDENCE toward closure, never sufficient proof; the human at the artifact stays in the invariant for those two cases. | P7; Codex third pass |
| A3 | **Cap expiry must not clear the named block.** Fixture: a named target with no receipt and a passed cap ⇒ `DEAD-AT-CAP` reported AGAINST that target, never rc=0. | P3 |
| A4 | **Intake is the larger defect.** The register sees BOARD-signal corrections; the week's three largest corrections bypassed it. The correction form already says the retirement block EMITS the register row, so this is form non-compliance by PROME · CARL · STUE · HANS at their 9/5 corrections — the fix is to APPLY the ratified form, not a new rule. Pilot cases get registered retroactively (rows, not receipts — Codex's "no retroactive receipt migration" non-goal stands). | P5; Codex point 2 |
| A5 | **Pilot addressing:** STUE cases run under **CARL** with STUE artifact pointers (`AGENTS/CARL/sub_agents/STUE/…`). Never expand fleet membership to fit a test. | P6; Codex point 2 |
| A6 | **HAWK is a live fourth pilot shape — missing BOOKKEEPING on a dark desk** (the no-op check is in its board log 9/2; the receipt is not on file), cap 9/11, inside the register already. It tests whether the closure contract can point a receipt at EXISTING disposition evidence (board-log row) rather than demand a fresh narrative. HOMER is the same shape without the board-log evidence (not yet checked). | P4; Codex third pass |
| A7 | **Evidence syntax: stable keys only** — `artifact=<path>#<row-id\|section-anchor\|commit>`; **never a line number** (a stale address the moment a row is inserted above it — PROME error #92, 9/5, caught by HANS). | `PROME/SCRATCH.md` errors list |
| A8 | **Tool implementer = DAEDALUS** (holds the `scripts/` grant since 7/31, AD row "FORGE ownership"). | `PROME/ACTIVE_DECISIONS.md` |
| A9 | **`supersedes=` lives in the owner retirement block**; the register's summary cell carries the pointer. No new register column (index-not-store). | Codex §3.1; register header |
| A10 | **History preserved, not hot.** The retirement block stays on the owner surface per the form, but "owner surface" may be the cold/detail half with a one-line supersession pointer hot. The block may move cold; it may not be dropped to save bytes. | Codex point 3; `[[finding_disambiguation_costs_bytes_so_a_capped_surface_cannot_absorb_every_flag]]` |
| A11 | **Pilot metric = discovery-to-closure**, not owner-fix-to-close (ES-02: rule born July, discovered 9/5, owner fix in minutes). Three fields per case, one table, in this record's §5 — no standing obligation. | Codex point 4 |
| A12 | **Scope caveat travels with the package:** this verifies work AFTER it happens; it does nothing for a desk that never runs (13 of DAEDALUS's 14 packets 9/5 inert). The spawn-driver item is separate and PROME-owned. | Codex closing caution; DAEDALUS packet `2026-09-05e` |
| A13 | **Sequence: walk before build.** The four-case manual walk (§5) is the sitting's pre-read; the checker's closure mode is built only for the checks the walk shows are mechanizable. | Codex recommendation; A2 |

---

## 3. Codex second-pass self-review (Will relay 17:18 — quoted for the record; no artifact of its own)

> **Retain:** receipt ≠ application (DEFERRED/CONTESTED never close) · receipts tied to a specific correction version · named consumers (broadcast = distribution) · conditional successor tests (NONE over an invented test) · the existing P4 sitting + a small pilot.
>
> **1.** *"path existence proves repository disposition"* — it does not; a path can exist while its contents remain wrong. Concrete failure: `APPLIED artifact=STATUS.md`, STATUS exists, still carries the contaminated claim, structural checks pass. **The report's most important defect: its implementation could reproduce the false assurance it seeks to eliminate.** → A1, A2.
> **2.** The register holds six corrections (8/26, 8/28); the 9/5 CARL/STUE/HANS episodes are not there — the checker cannot evaluate corrections absent from its input. `STUE` returns CANNOT-EVALUATE: unknown agent; run under CARL. → A4, A5.
> **3.** Preserve history without keeping every old claim in the active reading path; a concise supersession pointer from the current surface. → A10.
> **4.** Measure discovery-to-closure and corrective touches, not only owner-fix-to-close; no permanent reporting obligation. → A11.
> **Recommendation:** adopt the principle, tighten the proof standard, **manually walk the three cases through the existing records before building the closure mode.** This addresses verification after work happens; it does not solve recipients failing to run. → A12, A13.

PROME concurs on all four. One disagreement of emphasis: "manually walk first" needs a dated home or it becomes the fourteenth inert packet — hence L282.

---

## 4. The P4 sitting (DOCKET L282 · 2026-09-17 · DAEDALUS presents · pre-read due 9/15)

**One bounded ruling package for Will**, in this order:
1. **C1–C5** as proposed 8/28 (DAEDALUS's five forward-only conventions; C1 "separate the kill from the replacement" is what Codex §3.2 step 4 relies on).
2. **Codex §8 items 1–7** with amendments A1–A13 applied.
3. **WALTER-lane items** (register owner): run the prune for the first time (P2) · `DEAD-AT-CAP` semantics per A3 · kill-string field compliance on WALTER-authored BOARD corrections (3 of the 5 missing are WALTER's) · the intake finding A4 as a BOARD-spec line.
4. **Pilot verdict** from the walk (§5): which checks are mechanizable; build order.

**Decline is a legitimate outcome for any row.** No gate on retractions; no mandated tool beyond the closure mode the walk justifies.

---

## 5. The four-case manual walk (DAEDALUS, by 2026-09-15 — packet in DAEDALUS's inbox same touch)

Walk each case through the EXISTING records (git log, packets, receipts, DOCKET, owner surfaces). Record per case, one row, in a table appended to THIS file (§5.1) — nothing new is built to produce it.

| Case | Owner / route it actually took | Fields |
|---|---|---|
| **CVNA L131 fabrication + unwind** (PROME re-date → 6 CARL surfaces; Codex caught; CARL unwound) | PROME → CARL, DOCKET + packet; no `COR-` row | (a) discovery→closure elapsed · (b) owner-fix time · (c) last terminal-consumer time · (d) corrective touches / sessions · (e) stale operational copies REMAINING today (kill-string grep: *"9/10 CVNA"*, *"forward CVNA Q2"*) · (f) correction-of-correction within 7d? · (g) `validation_ref` or NONE · (h) register row exists Y/N |
| **ES-02 reading-rule defect** (STUE, under CARL; "5–6 day lag" → empirical cliff) | CARL → PROME packet; STUE not checker-addressable → A5 | same (a)–(h); kill-string: *"5-6 day publication lag"* |
| **HANS Qatar date** (stale on 4 of HANS's own surfaces after correcting HAWK — HANS closeout 9/5; **downstream INCOMPLETE:** HAWK `STATUS.md:119` · `SCRATCH.md` item 7 · `KB-HAWK-299` still carry *"~end-September"* while the FM ran to November on 8/31 — HANS's 9/5 packet sits unread in HAWK's inbox) | HANS self-correction + packet to HAWK (dark); no `COR-` row | same (a)–(h); kill-string: *"~end-September"* / *"END-SEPTEMBER"* beside Qatar |
| **HAWK ↔ COR-20260828-01** (Brent 8/26 close; unreceipted since 8/28, cap 9/11) | the register's own route | same (a)–(h) — whichever of receipt / DEAD-AT-CAP it reaches by 9/15 IS the datum |

**Then answer, in one paragraph:** which of the closure invariant's six legs (Codex §3.6) could a script have established for these four, from the records as they exist — and which required a human at the artifact. That paragraph decides the build.

### 5.1 Walk results *(appended by DAEDALUS; empty until then)*

*(empty)*

---

## 6. Non-goals (retained verbatim in spirit from Codex §7)
No Saga/workflow engine · no second ledger · no dashboard before the registered generated-view trigger · no new agent · no forum thread for routine corrections · no fleet-wide receipt migration · no exactly-once machinery · no mandatory successor test · no postmortem per bad datum. **Once the closure check is green and WALTER retires the row, stop.**

---

## 7. Correction + declared residue (2026-09-05 17:5x ET — Codex third pass, Will relay 17:39; PROME re-verified each at the artifact before editing)

**❌ fixed in this one pass (WQ-178: ❌ only):** P1 receipt count 17→**19** (+ 22 obligations) · P4 **HOMER** added, HAWK reframed as missing bookkeeping · P2 "prune never run" downgraded to INFERRED · P7 "kill-string absent" split into label-absence (VERIFIED) vs literal-absence (UNKNOWN) · A2 limits · A6 reframe · §5 HANS case gains its downstream half. **Error #97** (PROME): two counts and one framing shipped VERIFIED on a contaminated instrument and a one-desk sample — `[[finding_asymmetric_rigor_counterparty_claims]]`, the receiver caught it, same class as #91–96.

**Codex third-pass findings OUTSIDE this record, each PROME-verified and routed (not fixed here — other owners' files):**
- **CARL `scripts/roadmap_index.py --check` compares thread-NAME sets only** — a changed *Next Step* with the same thread name passes ✓ (Codex in-memory test; PROME read the code: `have`/`want` are name sets). The generated-view exemplar cited in WQ-179 rec (c) certifies a stale index. Fix = compare the live block to `build_index(rows)`. → CARL packet. **Bears on WQ-179 / H-8:** "generated, not hand-maintained" needs "and the gate compares the RENDERING."
- **`scripts/corrections_boot_check.py` validates the header only `if rows:`** — a register holding only a wrong header returns rc=0 / zero corrections. Live register not malformed. → DAEDALUS packet (scripts/ grant). Fixture for A3's neighbour.
- **DOCKET L280 (MIDAS-08) carried the wrong resolve date** (9/2 = the registration date; owner row says **2026-09-04**) and over-stated the BOND correction (it is conditional on **branch (c)**). Fixed in place on L280 this pass (cells only, row position unchanged).
- **FERT T11 (Pink Sheet, next_check 9/4) had no DOCKET row** though FERT's own wake-register header says idle-time wakes need one (asked 8/17, ASK 1, never registered). Registered **L283** this pass. Same class as P8.
- **STUE `EXPECTED_SIGNALS_TRACKER.md`** reportedly mixes the 9/5 PROVISIONAL banner with older validation/grading language — PROME saw the banner (L24), did NOT verify the conflicting text → **INFERRED**, routed to CARL for STUE.
- **HAWK KB-HAWK-299 / STATUS:119 / SCRATCH:40 Qatar date superseded** — HANS's packet in HAWK's inbox is the delivery; PROME adds the receipt item. → HAWK packet.

**⚠️ residue (declared, not fixed):** Codex's 22-obligation count vs PROME's hand-count agree at 22 — but neither is an instrument; the walk (§5) should produce it by script. The scheduling half of Codex's point 3 (*why Tier-1 spawn authority was not exercised for MIDAS/FERT*) is UNKNOWN and belongs to the spawn-driver item, not this record. This file is now **closed for the session** (one correction pass on a committed file; next edit needs a cold read).

