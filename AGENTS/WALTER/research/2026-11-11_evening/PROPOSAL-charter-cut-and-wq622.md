# Proposal: trim WALTER's instruction file, and WALTER's part in the combination watch (WQ-622)

Drafted 2026-11-12 (walter-b2, laptop) at Will's request (20:36 ET 11/11). **Status: RULED by Will in the WALTER terminal, answer received before 2026-11-12T02:01:44Z = 21:01 ET (stamp from `date`; AskUserQuestion): Part A "Approve all 7 (Recommended)"; Part B "Approve router role (Recommended)".** Authority: WALTER `CLAUDE.md` Rule 8 (removals, renames and mapping changes need Will's approval); `design/SPEC_OWNERSHIP.md` (charter = action home, `BOOT_PROTOCOL.md` = rationale home); root READ_CAP (rotate at 75% of 32,550 B, stop under 70% = 22,785 B).

## Part A: the size cut

**Now:** `AGENTS/WALTER/CLAUDE.md` = 25,925 B (80%). It loads whole into every WALTER session. **Target:** under 22,785 B *including* the Part B line, so about 3,450 B out.

**Method:** nothing is deleted except exact duplicates (item 1). Everything else moves **verbatim** to the file that already owns that subject, leaving a one-line pointer in the charter. Conservation is checked mechanically (`tools/split_verify.py`): every moved sentence must exist byte-for-byte at its destination. No step number changes; retired step numbers stay as stable IDs.

| # | What | Moves to | Saves (approx.) | Meaning change |
|---|---|---|---|---|
| 1 | Telegram retirement is stated five times (header paragraph, two memory bullets, Rules 6 and 12). Keep one statement in the header; drop the four repeats | stays in the header | 450 B | none: duplicates only |
| 2 | Step 6b's four per-desk registry bullets (RED, REGINALD, CREED, HANS) | `design/THRESHOLD_SCAN.md`, new section "Registry loading (charter 6b)". 6b then says: read THRESHOLD_SCAN whole first, then the four registries by its rules | 1,100 B | none; THRESHOLD_SCAN is already read whole at boot, one step later; 6b now reads it first |
| 3 | Retired-step tombstones 5, 7b, 7c, 7e(f), 10 shrink to one line each; full wording to their existing BOOT_PROTOCOL sections | `design/BOOT_PROTOCOL.md` §5, §7b, §7c, §7e | 400 B | none; each keeps "do not revive by deleting this line" |
| 4 | Step 15's closeout-runner mechanics (flags, checks.json, rerun rules) | `BOOT_PROTOCOL.md` § closeout | 500 B | none; step 15 keeps "run closeout_run.py, resolve REVIEW or report UNKNOWN, re-run closeout_check after publication" |
| 5 | Rule 10's exemption and NOTE-lane detail (TERRY restore condition, decision-changing items get full dispatch, NOTE cadence) | `design/BOARD_CONSUMPTION_SPEC.md` §3.5 | 500 B | none; charter keeps the pull-complete list (CARL, RED, PROME, TERRY), "every directed ask goes on ACTION" and the pointer |
| 6 | Step 10.8's named-CRE class list (default, servicing, foreclosure, receivership, REO, note sale, distressed modification, below-loan sale, payoff; exclusions) | `design/ROUTING_CARVEOUTS.md` named-case section | 250 B | none; charter keeps "named CRE distress: case entry and CREED INFO per that section; never edit CREED's ledger" |
| 7 | Closeout Tier 0/1 deferral detail | `BOOT_PROTOCOL.md` § closeout | 250 B | none; tier triggers stay in the charter |
| | **Total** | | **about 3,450 B** | |

**Trade-off, stated plainly:** items 4 to 7 move detail out of the file WALTER reads at every start into files it opens only when the step runs. The risk is the one WALTER's own memory names: "a pointer nobody travels is how a rule dies." Items 2 and 3 carry no such risk (THRESHOLD_SCAN is read at every boot; tombstones are retired steps). Items 4 to 7 sit on steps that already point to those files, and the tools enforce the core of each: closeout_run, the delivery reconciler, and the doctor's delivery checks.

**Not proposed:** any change to what WALTER does; any removal of a rule; the held "checkpoint / pick up WALTER" idea (Will 11/11 10:20 ET: hold).

**After the edit:** re-run read-cap, the doctor's static checks (`--spec-changed`), boot_basis re-attestation for the changed files, and one cold read on Sonnet of the new charter against the old (Will's reader rule, WQ-447) before commit.

## Part B: WALTER's part in the combination watch (WQ-622)

**Fact:** about 25 desks already keep their own themes (`combo:<theme>` rows in their ledgers; examples `ai-financing-repricing`, `diesel-buffer`, `lender-standstills`). PROME's guide says a theme crossing another desk's domain goes to that owner, and WALTER keeps no domain ledger.

**Recommendation: WALTER keeps no themes of its own.** It is the router, so its job is to make sure small items reach the right owner's theme, and to notice small items that no desk's theme covers.

- **Charter line (new step 10.6, about 250 B):** "Small items (WQ-622 A, PROME/COMBINATION_WATCH.md): fold each onto the session's small-items card, tagged `combo:<OWNER>/<theme>` when an owner's live theme fits, else `combo:none`. At Tier 2 closeout, name to PROME any `combo:none` subject that keeps recurring. Logging is not scoring."
- **Ledger:** the small-items BOARD cards WALTER already writes. No new file, script or checker.
- **Tell PROME:** one packet saying WALTER has no domain themes and uses the owner tags plus `combo:none` (guide step 4).
- **Why `combo:none` matters:** tonight's examples were Paraguay's Ueno bank, the Mercedes China quote and the MSCI watchlist names. None is in a desk's theme today. If one subject keeps coming back with no owner, PROME decides whether a desk should take it.

**Alternative, not recommended:** WALTER keeps 3 to 5 cross-domain themes of its own in a new file. That duplicates owners' themes and adds the new file PROME's guide asks desks not to create.
