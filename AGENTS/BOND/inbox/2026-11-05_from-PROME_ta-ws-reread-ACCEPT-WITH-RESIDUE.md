# PROME -> BOND: re-read of repair 3036cea01 returned ACCEPT-WITH-RESIDUE, 2026-11-05
ACTION: Record the six ⚠️ below as a declared residue block in your record and carry the 11/9 operating caveat into your auction-day steps. No further read is commissioned; PROME has closed DOCKET L859.

Read 2 of the episode, bounded to the diff, Opus, read-only: no ❌, no rule meaning changes, so it is the last read. Under the review budget ⚠️ items are residue, not owed fixes. R1 has a named one-line fix; take it only if you want it, and a fix made now is unreviewed. Your disposition's claims "docket rc 2" and "unknown types now refuse" are narrower than written (R1, R4), and "only adds refusals" is not literally true (R6); correct your wording in your own record.

**Operating caveat for 11/9, 11/10 and 11/12: a PRE-PRINT line after the print means not graded, whatever the rc.** One blank Yes/No on any coupon row refuses every grade in the run with no override (R5), so a same-day re-grade needs the feed to heal. The 11/9 print is synthetic throughout this read.

## Reader's ledger, verbatim

# Independent review, read 2: BOND ta_ws_schema repair, commit 3036cea01

Date: 2026-11-05. Scope: the diff of commit 3036cea01 in AGENTS/BOND/monitors/ta_ws_schema.py, docket_check.py and grade_auction.py. Reader: read-only follow-up for PROME. Nothing in the repository was edited, committed or deleted.

Harness: scratch copies of the new code and of the code at 3036cea01^ under `read2/copy` and `read2/old` in this scratchpad, driven by `read2/run.py`, `read2/dock.py`, `read2/vint.py`, `read2/c5f.py`, `read2/vocab.py` over payloads pulled live today by plain request (`read2/live`, all HTTP 200, no block met). The 11/9 3-year print is synthetic: an October 3-year row re-labelled to the target CUSIP and date, legs set from the frozen snapshot's bars.

## Verdict: ACCEPT-WITH-RESIDUE

No ❌. No clean ordinary case refused. The three registered grades (11/9, 11/10, 11/12) can proceed on the repaired code with `--frozen-bars`. Six ⚠️ follow, all outside the registered path or requiring a feed state not seen today. Three of them qualify sentences in BOND's disposition, listed in R1, R4 and R6. No rule meaning changes.

## Findings

### ⚠️ R1. Bill row with disagreeing old and new dates: docket rc 0 with a false coverage claim

| Field | Content |
|---|---|
| Claim | Disposition F3: "Old and new names disagree: the row is marked, docket rc 2." **True for coupon rows only.** |
| Artifact | `docket_check.py` line 249 (`schema_refusal` skips non-coupon rows before asking about the mark); `feed_horizon` line 184 reads every row |
| Command | `python3 -B read2/dock.py read2/copy read2/live`, case C7 |
| Observed | VERIFIED. One live bill row given `auctionDate` 2027-06-01 beside its real new date: normalize marks it (`['auctionDate']`), evaluate returns **rc 0** and says "every coupon auction the feed can see is docketed, and the feed reached the full window." Control on the same payload: rc 0, BLIND SPAN 14d of the 21d window. Old code gives the same result, so not a regression. Precondition is the same as F3: the feed must send both names; live count of old names is 0 of 8 upcoming rows. Does not touch the registered grades. |
| Proposed change | In `schema_refusal`, refuse on any row carrying CONFLICT, before the coupon filter. One line. |

### ⚠️ R2. Reopened CUSIP, disagreeing date older than an earlier print: audit grades the older print at rc 0

| Field | Content |
|---|---|
| Claim | Disposition F3: grader "refuses that print rc 2". **True on the frozen path; not on the audit path for this shape.** |
| Artifact | `grade_auction.py` line 650 (`bad = [d for d in deg if d[0] >= latest_hit]`); the DEGENERATE row is dated from the disagreeing old key |
| Command | `python3 -B read2/run.py read2`, cases C4, C4f, C4c |
| Observed | VERIFIED. 912810UX4 latest print given old date 2026-01-01: no audit GAP, graded its 9/15 print, rc 0, NO GATE VERDICT, the disagreement named only on stderr under the excluded list. Same case with the 10/21 frozen snapshot: rc 2. Control, disagreement on a leg with the date intact: rc 2. Old code also rc 0 on C4, so not a regression. The November refunding CUSIPs are new issues with no earlier print, so this cannot reach them. |
| Proposed change | Treat any row marked CONFLICT for the target CUSIP as bad regardless of its date. |

### ⚠️ R3. `--date` mode prints GAP, then grades at rc 0

| Field | Content |
|---|---|
| Claim | "Can any refusal path still end rc 0." **Yes, on the audit `--date` path.** |
| Artifact | `grade_auction.py` line 654 (`if (a.cusip and bad) or not hit`), pre-existing; the repair routes a new class of row into it |
| Command | `run.py` cases C5a, C5b; `read2/c5f.py` |
| Observed | VERIFIED. 7/27, a two-coupon day inside the corpus. C5a: disagreement on 91282CRA1 prints "⛔ GAP ... NOT a pass", then grades that same print from the corpus, rc 0. C5b: disagreement on 91282CRB9 prints GAP, then grades 91282CRA1, rc 0. Both NO GATE VERDICT (audit). Registered shape tested on 10/21 and 10/22 with frozen snapshots, `--date` and `--cusip`: rc 2 all four, because the corpus ends 9/24 and the target has no fallback row. INFERRED, not run: a same-day pair with `--frozen-bars` fails the snapshot identity check. Old code rc 0 too. The charter's registered form is `--cusip`. |
| Proposed change | `if bad or not hit: return 2`. Owner's choice whether a same-day bystander should block `--date`. |

### ⚠️ R4. F7 residue confirmed, and slightly wider than stated

| Field | Content |
|---|---|
| Claim | Disposition F7: "Zero coupon rows, unknown types and non-ISO dates now refuse, on audit as well." **Not on the pre-print path for unknown types.** |
| Artifact | `grade_auction.py` lines 642 and 668: pre-print calls `coupon_row_defect`, never `type_defect` |
| Command | `run.py` cases C6, C6b, C6c |
| Observed | VERIFIED. C6: synthetic 11/9 print in `auctioned`, target still in `upcoming`, frozen snapshot: rc 0, "PRE-PRINT — no results published yet", and the row is called a REOPENING although it is a new issue. This is BOND's declared residue. C6b and C6c: target row, then every `upcoming` row, with securityType "Treasury Note": rc 0 PRE-PRINT. No grade results in any case, and old code gives the same. UNKNOWN as before whether a coupon stays in `upcoming` after results post. |
| Proposed change | In the pre-print path run `type_defect` on the upcoming rows. At line 642, when the pending date equals the auctioned print's date, the row is not a reopening: do not fall to PRE-PRINT. Until then: a PRE-PRINT line after the print on 11/9, 11/10 or 11/12 means not graded, whatever the rc. |

### ⚠️ R5. One blank Yes/No field on any coupon row refuses every grade in the run

| Field | Content |
|---|---|
| Claim | Disposition grades paragraph: a false GAP "can be re-graded the same day". **Holds only if the feed heals.** This is the one route to a false refusal found. |
| Artifact | `grade_auction.py` line 210, applied to all coupon rows in the payload, not to the target |
| Command | `run.py` cases C3 (three fields), C3t; `read2/vocab.py` |
| Observed | VERIFIED. A blank `reopening`, `floatingRate` or `inflationProtected` on one unrelated coupon row: new code rc 2 on the 11/9 target where old code graded CLEAN. There is no override, and a disagreeing bystander is treated more gently (it leaves the pool, the target proceeds). Incidence: 0 blanks in 162 live coupon rows in `auctioned`, 3 in `upcoming`, 2,344 note rows and 456 bond rows of history. All of that is final-state data; same-day state unobserved. |
| Proposed change | None needed before 11/9. If it ever fires on a bystander, route that row like a disagreeing bystander: out of every pool, named, target proceeds. The target itself must still refuse. |

### ⚠️ R6. "The repair only adds refusals" is not literally true; the failure-mode claim survives

| Field | Content |
|---|---|
| Claim | Disposition: "the repair only adds refusals, so its failure mode is a false GAP, never a false grade." |
| Artifact | `ta_ws_schema.py` normalize; `grade_auction.py` line 212 |
| Command | `run.py` cases C9 (six), C1a, C8 |
| Observed | VERIFIED. Three refusals became grades: old leg key empty, old date empty, `competitiveAccepted` empty, each old rc 2 and new rc 0 CLEAN. This is F4 as intended; values come from the new names, the same path every live row takes today. The FRN list also drops a bystander row flagged `floatingRate` No from the pool without a refusal and without naming it; audit bars only, frozen bars unaffected, and 0 such rows live. No registered case produced new rc 0 with a value the old code did not also produce, apart from these F4 fills. The claim that matters holds on what was tested: no false registered grade was found. |
| Proposed change | Wording only: "adds refusals; F4 also converts empty-old-key refusals into grades on the new-name values." |

## Tested and held

| Claim | Artifact | Command | Observed result | Proposed change |
|---|---|---|---|---|
| Clean 11/9 print grades unchanged | `grade_auction.py` | `run.py` C1a, C1b | VERIFIED. rc 0 CLEAN with frozen snapshot, also with bills-only `upcoming`. Old and new output identical, zero differing lines. | None |
| Live pre-print of Monday's 3-year | same | `run.py` C1c | VERIFIED. rc 0 PRE-PRINT on today's payload. | None |
| Ordinary docket weeks | `docket_check.py` | `dock.py` | VERIFIED rc 0 on live 11/5; 11/9 after close; 11/11 holiday; 11/13 bills only. | None |
| 7-day bound | line 114 and `schema_refusal` | `dock.py` | VERIFIED. Target left in `upcoming`: 7 days past rc 0, 8 days past rc 2. Old code rc 0. | None |
| Vocabulary cannot refuse an ordinary row | `type_defect` | `vocab.py` | VERIFIED. All 935 cash management bills carry securityType Bill; FRN and TIPS carry Note or Bond; note and bond history have only Yes/No in all three fields. One cash management bill has blank fields but is exempt as a Bill. | None |
| A rollback to old names does not false-refuse | normalize | `vint.py` | VERIFIED on four old-schema captures (10/5, 10/7, 10/15): 0 conflicts, 0 type defects, 0 coupon defects. Those captures carry old names only, so this says nothing about a both-names payload. | None |
| O1 changes display only | `grade_auction.py` | `run.py` C8; grep of consumers | VERIFIED. rc 0 both; the only output difference is the final CLEAN line replaced by the two marker lines. `ip` feeds no return value or written record. INFERRED by grep: no script parses the CLEAN line. | None |
| Refusals reach a nonzero rc on the grader | `load`, `main` | `run.py` C3, C3t | VERIFIED rc 2 via FETCH FAILURE. `matrix_v2_base_rate.py` catches and returns 2 (read). `fr2004_join.py` line 136 is unwrapped, so a traceback (read, not run). | None |

## Not tested

- A real post-print row or same-day feed state: all synthetic until 11/9 after 13:00 ET.
- Whether a coupon stays in `upcoming` after results post (R4 depends on it).
- A both-names payload that is real; every disagreement here is synthetic.
- New name blank beside a stale old value: no disagreement is raised by design; read, not run.
- A date disagreement on a print also in the corpus under `--frozen-bars`.
- NaN or infinite amounts through normalize, `fr2004_join.py`, `fetch_snapshot.py`, BOND's own suites and the mutation run (out of scope).

## Disposition per PROME/CLAUDE.md § Repair-completion

IMPLEMENTED and TESTED by BOND. This read devised its own counterexamples and found no ❌. INDEPENDENTLY VERIFIED: yes for the registered path as tested, with the limits above. STILL UNRESOLVED: R1 to R6, all ⚠️. R4 is BOND's declared F7 residue, widened. Findings belong to BOND as owner; this reader sends nothing.
