# PROPOSAL — closeout tier selection and the resume point (from the 2026-10-02 `prome-70` Light closeout)

**Status:** PROPOSAL — nothing here is in force. **Decision:** Will (WQ-367). **Author:** PROME `prome-70`, written 2026-10-02 11:3x ET on Will's word (*"write it"*, 11:33 ET), minutes after the failure it describes and BEFORE a context reset, so the evidence is first-hand. ⚠️ **The author made the mistakes below. A rule drafted by the author straight after a failure tends to fix the reported shape and miss its neighbours — this record is evidence and candidate text, to be cold-read before any of it is encoded.**

**No manual, skill, gate or charter text was changed by this record.** Encoding any item is a canon amendment: plan read here, one transplant, result read (`PROME/CLAUDE.md` § Session Process Controls — Canon drafts; Read budget). The section FREEZE (WQ-299 R3) runs to 2026-10-25: items that would add a bullet to that section must be paired with a named consolidation; items that amend `PROME/CLOSEOUT.md` are outside that section but still inside the process ceiling (R1, one process change per session).

---

## 1. What happened (facts, each checkable)

| # | Fact | Where to check |
|---|---|---|
| F1 | `prome-70` booted 08:27 ET, ran ~3 hours: nine desk sessions (eight due-row wakes + TERRY), four new WILL_QUEUE rows (WQ-363–366), six new DOCKET rows (L585–L590), two commissions, seven desk event calendars. | `PROME/state/ORCH_LOG.tsv` 2026-10-02 rows · `memory/2026-10-02.md` § prome-70 |
| F2 | Will asked for a closeout so he could clear the context and boot again immediately. PROME chose the **Light** tier from the manual's table (keyed to how long the session is paused) and committed it at 11:19 ET. | commit `e63270e6f` · `PROME/CLOSEOUT.md` tier table |
| F3 | `prome_gate.py closeout --tier light` returned PASS (11 blocking) on that candidate. | commit body of `e63270e6f` |
| F4 | PROME reported the closeout complete and told Will he could reset — twice (after the commit, and again when asked what else was needed). | the session transcript; not otherwise recorded |
| F5 | Will then asked PROME to review SCRATCH. The review found: **(a)** two live instruction sets — the 10/1 night "Owed at the next boot" block still sat under the new resume block, including a wake list for desks already woken and a superseded TERRY lean; **(b)** six desks with waiting work absent from the new "not yet woken" list (SAM · HANS · BOND · FALCON · RED · CREED); **(c)** the operator card still described the 10/1 night book (no Robinhood put, no WQ-365/366, no G7 release); **(d)** the header stamp read 10/1 23:15 and called the 10/1 credit cell unpublished; **(e)** the rule "no new watch-list set is landed until L570 is fixed (L565)" lived only in the old block. | `git diff e63270e6f 390456338 -- PROME/SCRATCH.md` |
| F6 | The fix to F5 itself left two stale sentences (an intro pointing at a "block below" that the fold had removed; a `flng_watch` line calling a completed read pending), caught on PROME's own read-back and fixed in a second pass. | `48b3e7173` |
| F7 | Will then asked for the other boot-read files. Found: STATUS still said the GATE-LIQ-069 anchor re-base was HELD and WQ-301 open (ruled 10/1, encoded 10/2 — PROME had mirrored GATES at 10:2x and not run the consumer check on the lines it superseded; LIQUID's own closeout consumer check named PROME/STATUS as a live consumer at 11:15 and PROME did not act on it until the review) · ACTIVE_DECISIONS and HANDOFF untouched (correct for Light, but HANDOFF's top entry carried the previous night's "Decisions needed") · DOCKET L127 PENDING for a prediction BROCK graded RESOLVED-TRUE on 2026-09-03 · DOCKET L170 carrying an unannounced WAL date as 10/13 · WQ-347 describing four puts and a withdrawn roll. | `493cd5bbb` |
| F8 | HEARTBEAT was found stale against 10/2 and deliberately NOT amended (an amendment needs a structured dashboard projection; a malformed one withholds the dashboard summary). | SCRATCH header · `PROME/HEARTBEAT_DASHBOARD.md` |
| F9 | None of the three correction commits (`390456338` · `48b3e7173` · `493cd5bbb`) had an independent reader. | — |

**What it did not cost:** no trade was placed or missed; no gate was mis-stated in GATES.tsv; every desk's work was committed and pushed before the first "complete" report.

## 2. Why it happened (PROME's reading — INFERRED, not established)

1. **The tier table has one input.** Light is defined by absence length ("short session paused for hours; 1–2 artifacts"). The session matched "paused briefly" and did not match "1–2 artifacts", and PROME read only the first half.
2. **Light has no reader.** Standard's ARGUS audit is the step that catches stale carried claims (six ❌ on 10/1 night, seven on 9/30). At Light the author is the only reviewer, minutes after writing.
3. **The gate checks form, not truth.** It verified commits, row shapes and COVERED annotations. Nothing in it asks whether SCRATCH's resume block contradicts the block beneath it, or whether a status row agrees with a ruling.
4. **The resume block was APPENDED above the old one** with a label ("PARTLY CONSUMED") instead of replacing it — the documented failure `finding_correction_beside_an_instruction_leaves_two_live_instructions`.
5. **The wake list was written from memory of the session**, not from `spawn_list.py` / the old block's own enumeration.
6. **L127 is a class, not an instance:** a DOCKET row that mirrors a desk prediction has no check against the owner's ledger state.

## 3. Candidate changes (each stands alone; approve by number)

| # | Change | Home if approved | Cost | PROME rec |
|---|---|---|---|---|
| P1 | **Tier by weight as well as absence.** Add a second input to the tier table: a session with any of — ≥3 desk touches · a new WILL_QUEUE row · a new GATES row or state flip · a commission — closes out **Standard** however short the pause, unless Will names the tier. | `PROME/CLOSEOUT.md` tier table (one row/sentence) | A Standard closeout is ~20–30 min incl. ARGUS and publication | **Approve in a weaker form (P1b):** such a session may still close Light, but then P2 is mandatory. A forced Standard before a five-minute reset is the paperwork reflex. |
| P2 | **One blind read at a heavy Light closeout.** When the P1 conditions hold and the tier is Light or Bounce, one `coldreader` pass over `PROME/SCRATCH.md` ★ NEXT runs before the closeout is reported; ❌ fixed, ⚠️ to residue. | `PROME/CLOSEOUT.md` Pre-closeout item 4 (or the tier table's Light row) | One Opus read, ~3–5 min | **Approve.** It is the control that was missing today. |
| P3 | **A resume block REPLACES its predecessor.** At any tier, writing a new ★ NEXT block removes the previous one in the same edit; its unconsumed items are carried as a named list and its full text is a `git show <sha>:PROME/SCRATCH.md` pointer. Never two blocks. | `PROME/CLOSEOUT.md` symmetry table, SCRATCH row "Never" column | None; it also keeps SCRATCH under its byte line | **Approve.** This is an existing lesson without a home in the manual. |
| P4 | **The wake list is the instrument's output.** The "not yet woken / owed desks" list in a resume block is produced from `PROME/tools/spawn_list.py` (+ the prior block's carried list), named as such, never recalled. | `PROME/CLOSEOUT.md` routine step 3, one clause | Seconds | **Approve.** |
| P5 | **Docket-vs-owner-ledger staleness check.** A check that flags a PENDING DOCKET row citing a desk prediction id whose owner ledger reads RESOLVED/FALSE/TRUE. | A tool — DAEDALUS's lane; acceptance conditions first (WQ-229) | A build; not PROME's process slot | **Send to DAEDALUS as a candidate**, not a PROME edit. |
| P6 | **Report wording.** A closeout report does not say "complete" or "clear to reset" until the resume block has been READ BACK (by the cold reader under P2, or by PROME where P2 does not apply) after the commit. | `PROME/CLOSEOUT.md` § Delivery, one sentence | None | **Approve with P2**; alone it is a self-caution, which the fleet's memory says is not a control. |

**Not a proposal — a skipped control, reported as such:** the consumer check on a figure PROME itself superseded (root session-end step 1c `--self`) was not run when the GATE-LIQ-069 anchor lines were mirrored. The rule exists. (Skipped-control reporting rule, 2026-09-17.)

**Deliberately NOT proposed:** a gate check for "resume block contradicts the block below" (P3 removes the condition instead of detecting it) · any new bullet in `PROME/CLAUDE.md` § Session Process Controls (the freeze; every item above homes in `CLOSEOUT.md` or a tool).

## 4. What a reader should test before any of this is encoded

- Does P1b's trigger list catch today's session and NOT catch a genuinely light one (a 20-minute session with one doorbell)?
- P2 names SCRATCH only. Today's F7 was in STATUS and DOCKET — would a SCRATCH-only read have surfaced it? (PROME's answer: no. Is a wider perimeter worth its cost at Light, or is that what Standard is for?)
- P3: is there a case where the previous block must stay verbatim (a crash recovery mid-closeout)?
- P4: `spawn_list.py` lists rows due by date; desks with only inbox packets (RED, CREED today) are not rows. What produces THAT half of the list?
- Is the whole set an instance of "add a control" where promoting an existing one would do (WQ-229's own caution)? The existing control is the Standard tier.

## 5. Residue

- Evidence F4 rests on the transcript, which the context reset discards; this table is its only record.
- Section 2 is the author's account of the author's error.
- No reader has seen this file.
