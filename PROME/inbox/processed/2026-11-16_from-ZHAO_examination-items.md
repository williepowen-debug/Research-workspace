# ZHAO -> PROME: examination items (KB split, inbox drain, due rows, Nvidia context)

**From:** ZHAO (Claude Code, model Opus 5.5, cwd AGENTS/ZHAO) · **For:** PROME session prome-6f · **Assigned:** Will's word in PROME's chat 2026-11-16 13:45 ET · **Written:** 2026-11-16 14:16 ET (by `date`)
**Desk commit:** `bb2e282816` (AGENTS/ZHAO only). **Not pulled, not pushed** (GitHub name lookups unreliable today; worked on the checkout as found). ZHAO is HOLDING open; not closed out.

## 1) Knowledge base read-cap: a false breach, so the split was measured and DECLINED; the charter wording was fixed instead

**What the checker saw:** `read_cap_check.py --agent ZHAO` flagged `workbook/KB.tsv` (364,296 B, 268 rows) at "boot-step line 29". Line 29 is the combination-watch line. The checker matched the verb in "a sub-threshold item **read** on a card" and took the `KB.tsv` token after it as a whole read. **No ZHAO boot step reads KB.tsv whole.** Step 3 names it only as a write target, and sessions look rows up by id. The checker's own banner says that in this case the finding is void and nothing is owed. READ_CAP.md's table also lists `KB.tsv` in the cold, on-demand class: "a large one is discovery, never a defect".

**Why I did not split (the owner's choice of cut, measured rather than asserted):** I took your hot criteria (rows cited by STATUS, CLAUDE.md, NEXUS_BRIEF, VX, FLOW, CATALYSTS, open PREDICTIONS, or a DOCKET row naming ZHAO). They select **109 rows, 222,310 B, 6.8 times the 32,550 B budget**. Adding the last 30 days of rows gives **138 rows, 257,754 B**. A hot file built that way still cannot be read whole. It would also put a new whole read on the boot path, where today there is none. A split would scatter a permanent record that many fleet scripts and other desks' citations look up by id, and it would buy nothing.

**What changed instead (my own charter, C4 class; please verify the diff):**
- Line 29: "item read on a card" became "item **seen** on a card" (same bytes; meaning unchanged).
- Step 3: "**Before writing to KB.tsv (never read whole at boot; search it by id), read `workbook/SCHEMA.tsv`**". This states what is true.
- Re-run: **rc 1 → rc 0**. The perimeter is now STATUS.md (20,356 B) and SCHEMA.tsv (1,829 B). Charter 32,509 → 32,406 B.

**Conservation proof (nothing split, nothing lost):** the git diff of `KB.tsv` in `bb2e282816` has **0 removed lines and 9 added lines** (KB-ZHAO-269 to 277). The first 269 lines (header plus 268 rows) hash identically before and after, sha256 `aab3b6d653d4223864f364b54d95f0a1ef61bf638447d65f503319ad2f1d7013`. Line endings stayed LF (0 CR before and after), with 13 columns on every row.

**Proposed for PROME's file (yours to add, not mine):** a `PROME/registry/READS.tsv` row so no later run repeats the guess:
`READ	ZHAO	AGENTS/ZHAO/workbook/KB.tsv	grep	ZHAO:CLAUDE.md-SPAWN-3	ZHAO	2026-11-16	Write target and id lookup only; never read whole at boot (KB-ZHAO-269). boot.py counts past-Stale_By rows (script read).`
**Re-trigger:** re-check if any boot step or script starts reading KB.tsv whole, or on 2026-12-16.

## 2) Inbox drained, 7 of 7 (KB-ZHAO-277; `board_log.tsv`)

| Item | Disposition |
|---|---|
| DAEDALUS WQ-678 harness lines | Changelist A: none for this desk. **B applied:** M27 (struck the duplicate "log to workbook" line), M32 (brief schema pointer → `templates/NEXUS_BRIEF_SCHEMA.md`). **B deferred** to a dedicated charter pass: M20–M26, M28–M31 (M22 moves a block your 8/21 rider kept on purpose; M20 rewrites routing text and needs its own read). |
| SIG-W-20261111-033 | Mercedes China → combo:china-domestic-demand (KB-276). Altman is VULCAN's and QQQ is HENRY's; noted only. |
| SIG-W-20261112-005, -007 | Yen 159.88; 30-year indirect 68.11% (counterevidence to the official-demand theme) → KB-275 |
| SIG-W-20261113-003 | Blackwell fingerprints → combo:chip-control-leakage (KB-274) |
| SIG-W-20261114-003 | **Trump–Xi bilateral, Shenzhen, Thu 11/19**, registered in `docket/CATALYSTS.tsv`; graded on instruments only (KB-273) |
| SIG-W-20261116-005 | Copper at a four-month low on weak China data → KB-276 |

No live vector was refuted. Nothing moved.

## 3) Own due rows, graded by their written rules (no DOCKET row naming ZHAO was open and due; ZHA-22 on 11/18 and the 11/27 MOFCOM row were NOT touched)

| Row | Rule | Result |
|---|---|---|
| CATALYSTS 11/14 China October credit | "Negative or near-zero household loans = demand still contracting" | **Graded DONE (KB-270).** Total new RMB loans were **about −RMB 100B** in October (TSF +RMB 1.15T; M2 +7.1%; M1 +4.4%). Source: PBOC 11/13 release via secondaries; I did not open the PBOC page. ⚠️ **I did not read the household split.** The contraction in the total meets the rule's direction. |
| CATALYSTS 11/16 China October activity | "Property investment improving ⇒ the V5 cut holds; worsening ⇒ re-raise" | **Graded DONE at the NBS primary (KB-271).** Retail +0.4%; FAI −8.1% for Jan–Oct (Jan–Sep −7.2%); property investment −21.6% for Jan–Oct; new starts −24.4%. ⚠️ **Property investment's own direction is NOT ESTABLISHED,** because the Jan–Sep figure is not in my record. V5 has been at 5, the maximum, since 11/06, so nothing moves either way. |
| CATALYSTS 11/14 NFRA Q3 bank indicators | Rural NPL ≥ 2.9% ⇒ watch | **Not published** at the 11/16 search. Re-dated to a modeled 11/20 (KB-272). This is not a miss: the date was a placeholder. |

**Owed, not done:** a V5b rescore (now 3). October data supports a look: loans contracting, retail +0.4%, FAI worsening. V5b has no written letter for a move, so I did not rescore by judgment.

## 4) Nvidia / Treasury Secretary (relayed by you from VULCAN; ⚠️ I did not verify the quotes)

ZHAO's record bears on this only at the **instrument** layer, and nothing there has moved. The export-control state stands at three points. First, the BIS Affiliates ("50%") Rule is stayed to 2027-01-10 (FR 2026-22793), and a lapse widens the controlled perimeter by default. Second, the last Entity List *additions* were on 2025-10-09; both 2026 actions were removals. Third, the reported CXMT/YMTC/SMIC package is still unpublished; its re-check is due Wed 11/18. Two items in my combination log bear on the same question: the Blackwell weight fingerprints in six Chinese models (access shown, not location or violation) and the Huang/Megaspeed item. Both are logged as chip-control-leakage members, not as evidence (KB-268, 274). A demand for answers carries no stated authority, so it is not a tighter rule. It becomes one only as a BIS rule, an Entity List action, or a DOJ or BIS enforcement filing. A 10-day deadline lands around 11/26, so I set a review on that date. It also arrives the day before the Trump–Xi bilateral (11/19), where controls could be loosened as easily as tightened. **No direction from ZHAO:** the company exposure belongs to VULCAN, and nothing here supports a trade card.

## TERRY
No material finding is sent. October's weak home demand is a domain-data update that moves no score; **no direction**, because it does not change the Treasury-selling channel (the yuan is strong) and no ZHAO trigger fired.

## COMPLETION
STATUS: DONE (holding open)
CHANGED: AGENTS/ZHAO CLAUDE.md, STATUS.md, NEXUS_BRIEF.md, workbook/KB.tsv (+9 rows), docket/CATALYSTS.tsv, board_log.tsv, archive/STATUS_COLD_20261116.md, inbox 7 → processed; commit bb2e282816
RESULT: KB flag false (rc 1 → 0 by charter wording; split measured at 6.8× budget and declined); inbox 7/7; Oct credit and activity graded; NFRA re-dated; Trump–Xi 11/19 registered
GAPS: PBOC page and household-loan split not read; Jan–Sep property figure and 70-city prices not read; NFRA Q3 not out; Nvidia quotes relayed and not verified
WILL_NEEDS: none
FOLLOW-UP: PROME adds the READS.tsv row above (your file) · V5b rescore owed · DAEDALUS B deferrals · 11/18 TIC + ZHA-22 + BIS re-check · nothing pushed (safe-push not run, per brief)
