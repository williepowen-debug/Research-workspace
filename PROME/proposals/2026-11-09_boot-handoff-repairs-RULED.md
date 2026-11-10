# Boot-handoff repairs: RULED (Will, 2026-11-09 19:16 ET, PROME chat)

**Source of the recommendations:** CATO's review `AGENTS/CATO/runs/2026-11-09_1906_prome-boot-review.md` (commit ad52b2f43d), findings PB1 to PB3, on PROME's blank-slate boot dry run (raw log preserved by CATO beside that review).

## Will's words, verbatim

> I approve the four bounded repairs identified in CATO's blank-slate review:
>
> 1. Session disposition: Add a compact NOW header identifying the working session, its last recorded disposition, the timestamp, and a pointer to existing checkpoint or closeout evidence. This records disposition, not live process status. Before taking over unfinished work or issuing closeout instructions, establish that the previous PROME yielded ownership or is confirmed stopped. An idle session may still own the work. If ownership is uncertain, resolve it before taking dependent actions.
> 2. Launch allowances: Clearly distinguish launches individually authorized by me from launches consuming autonomous allowances. Preserve existing limits and approval scopes.
> 3. Obsolete references: Correct the Telegram delivery-evidence clause and the removed SCRATCH heading reference. Preserve the requirement for actual delivery evidence; a saved file alone does not prove I received a briefing.
> 4. Update timestamp: Keep NOW's document-update timestamp accurate. Do not imply that updating the page refreshes underlying market observations.
>
> This authorization covers the necessary bounded instruction edits and applicable review requirements despite the earlier migration review budget being spent. Preserve existing boot checks and the spawn-slate read. Do not start a broader redesign, new registry, checker, or evaluation exercise.
>
> Complete the repairs, report the exact changes and any unresolved conditions here, then return to authorized research. Use the next ordinary boot to observe how the handoff works.

## What changed (one episode, the diff of the commit that adds this record)

| # | File | Change |
|---|---|---|
| 1 | `PROME/SCRATCH.md` header | Three lines replace the single "Updated" line: Session · Last recorded disposition (OPEN / RESTART CHECKPOINT / CLOSED OUT, clock time, evidence pointer, the takeover rule) · Page last edited |
| 1 | `PROME/BOOT.md` step 2 | One sentence: the disposition line is a record, not liveness; establish the earlier PROME yielded or is stopped before taking over unfinished work or sending closeout asks; uncertain means resolve first |
| 1, 2, 4 | `PROME/CLOSEOUT.md` § one home per fact, SCRATCH row | The page's contract now names the header (disposition, edit time from `date`, dates the page and never a market reading) and the split of Will-worded launches from autonomous allowances |
| 2 | `PROME/SCRATCH.md` § This session | Launches listed with Will's time for each; autonomous allowances listed separately against their existing caps; touches without a launch listed apart |
| 3 | `PROME/BOOT.md` step 8, delta brief | "names the Telegram message and time" replaced by "a dated receipt of actual delivery to Will, or Will says he has it; a saved WALTER file alone is not delivery" |
| 3 | `HEARTBEAT.md` § Skip | Pointer "SCRATCH ★ NEXT" replaced by "SCRATCH § Next, in order" (pointer only; no claim, level or grade in the memo changed) |
| 3 | `.claude/agents/argus.md` and `PROME/.claude/agents/argus.md` | Same removed-heading pointer corrected in the auditor's instructions; copies identical |
| bytes | `PROME/BOOT.md` header, `PROME/archive/BOOT_STAMP_CHAIN_2026-10-16.md` | To stay under the 75% rotation tier: the 10/25 editorial-amendment line and the 11/7 prior stamp moved to the stamp archive; two provenance phrases in step 2 dropped ("WQ-578 batch 2:", "moved out of SCRATCH 2026-10-20 on Will's word"). No instruction removed |

No cap, grant, approval scope, boot check or the spawn-slate read was changed. No new file class, registry, checker or tool.

## Review and state

One bounded diff read (Sonnet cold reader, 19:19 ET 11/9, its own counterexamples): ❌ 0 · ⚠️ 5. Conditions 1, 3, 4 MET; condition 2 PARTLY at the read.

Two fixes made AFTER the read (unreviewed):
- W2: the NOW page had listed the seven 12:07 ET launches as consuming no allowance. They were due-row desks launched on Will's blanket word. The page now says so, says none was PROME's own choice, and says whether his word counts against the four-per-boot cap is NOT RULED; the cap is treated as spent this session.
- W3: the two step-2 provenance phrases cut from BOOT.md were added to the stamp archive.

**Declared residue (not fixed):**
- W1: nothing instructs a booting PROME to write its own session and OPEN disposition into the header on arrival, so a header can read CLOSED OUT while a later session works. The takeover check is required but its method is not specified here (BOOT_MODULES § Resume and the Desk-spawn preflight carry the existing methods). To be observed at the next ordinary boot, per Will.
- W4: "a dated receipt of actual delivery to Will" names no channel, because the record does not establish what replaced Telegram for WALTER's briefs. Until it does, the practical evidence is Will saying he has it; otherwise prior delivery is UNKNOWN and the full context is given.
- W5: "the PROME that wrote it" reads oddly when the same session re-reads its own header after a context reset.

**State:** IMPLEMENTED · TESTED (read-cap rotation_due=0, WILLQ view check passes, skill and agent copies identical) · INDEPENDENTLY VERIFIED for the text as read, except the two post-read fixes, which are unreviewed · STILL UNRESOLVED: W1, W4, the due-row cap question.

## Observation at the next ordinary boot (PROME prome-1e, laptop, 2026-11-09 20:13 ET; Will's instruction above)

- **W1 (disposition):** the header read CLOSED OUT with its evidence pointer. Before taking over, the booting PROME established yield by three checks: hostname `WilliePOwen` against the header's `DESKTOP-BC6EF81`; `git fetch` then 0/0 against origin/master with the closeout commit 8dfc5baea1 present; ListAgents empty at 20:09 ET. It then wrote its own session and OPEN disposition into the header. Nothing instructed that write; the three checks were sufficient on a machine switch. On a same-machine restart the hostname check is void, and ListAgents plus the run-directory receipt carry it.
- **W4 (delivery evidence):** no WALTER brief to Will since 19:42 ET; prior delivery was PROME's own chat brief at 14:5x ET and its closeout report at 19:4x ET, so the delta brief rested on PROME's own record and no channel question arose.
- **Due-row cap:** nothing fell due between 19:42 and 20:07 ET, so the question did not arise. Will opened ten desk windows himself at about 20:11 ET; tomorrow's due rows are taps to live owners, not launches.
- **What the NOW page did not carry:** the ARGUS residue list (found in the daily note it points to) and WALTER's routing need for 11/10 (its `LAST_COMPLETION.md`). Both were one pointer away; neither blocked the boot.
- **Defects met:** the pre-CPI brief draft § 1 China row was stale (ARGUS had flagged it) and is corrected this boot. `fetch.py price` returned empty tables on a ten-ticker loop and worked on single retries; cause UNKNOWN (vendor or load). The header's model name ("Fable 5.2") does not match this runtime's model id (`claude-fable-5-1`); left as the prior session's record.
- **State of W1, W4, the cap question:** W1's method is now recorded here; W4 and the cap question stay STILL UNRESOLVED as written.

## W1 closed: arrival write added to BOOT step 2 (2026-11-09 20:44 ET, PROME prome-1e, on Will's instruction pasted in chat 20:42 ET, under the approval above)

**Changed:** `PROME/BOOT.md` step 2 gains one sentence: ownership established, the booting session writes its identity, OPEN disposition, time from `date` and evidence pointer into the NOW header before other work. Boot runner pointer added in both skill copies. Byte offset: the prior header stamp and two step-3 provenance phrases moved verbatim to `PROME/archive/BOOT_STAMP_CHAIN_2026-10-16.md`; no instruction removed. Same sitting, separate corrections: `scripts/docket_view.py` over-budget message now names the block size only and warns against closing open obligations to shrink it; `PROME/MACHINE_LOCAL.md` and the NOW page record approximately 16 GB physical RAM with WSL capped at 6 GB; the NOW page keeps individually authorized, blanket-instruction and autonomous launches apart, the blanket-instruction cap question NOT RULED.

**Review:** one bounded diff read (Sonnet cold reader, its own three counterexamples): four conditions MET, ❌ 0, ⚠️ 5.

**Declared residue (not fixed):** no explicit rule for a session meeting its own OPEN header after a context reset (W5 above, same item) · what a session may do while ownership is unresolved is not stated · the runner pointer omits the `date` and evidence detail (pointer only, by design) · the next reader is not told to verify the evidence pointer · the reader did not open this record.

**State:** IMPLEMENTED · TESTED (read-cap rotation_due=0, skill copies identical, docket_view compiles and runs) · INDEPENDENTLY VERIFIED for the diff as read · STILL UNRESOLVED: W4 and the due-row cap question; the six OVERDUE COVERED rows await reconciliation on completion evidence, not started.

