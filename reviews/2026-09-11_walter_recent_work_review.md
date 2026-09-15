# WALTER recent-work review — September 9–11, 2026

WALTER is producing useful routing judgments and substantive corrections. The main weakness in this review is incomplete repair propagation: a rule, source record, or explanation changes while a reader, checker, or continuation file retains the earlier behavior.

Scope: committed changes from `03880fd6a27da54cba41b758a0ad18d46e4ba735` (last commit before September 9 ET) through `09d69c7663ebba03f132cac66e4c7216ebdc4048`. Reviewed the WALTER change history and diffs, metadata for all 31 September 10–11 BOARD dispatches, selected full dispatches and recipient records, routing/consumption rules, and diagnostic implementation. This is an operational and internal-evidence review, not independent verification of the financial/news claims. No external-source accuracy or investment conclusion is certified here.

WALTER was working concurrently. Its subsequent repair `019c7a4d9` was inspected separately and relevant reproductions rerun against that version. No WALTER-owned files were edited. Tests used committed copies in `/tmp/walter-review-20260911/`, with mocked delivery/consumption state; they did not run WALTER's operational workflow.

**1. High — a corrected options-expiry claim still reaches readers through unchanged discovery and delivery surfaces.**

The September 11 addendum to `BOARD/SIG-W-20260910-010-96t-us-options-expire-918-largest-triple-witching-per-citadel-securities.md`, beginning at line 54, distinguishes a ~$9.6T expiry **window** from ~$6.2T on the **day**, preserving VIOLET's caveat that the split comes from a search extract. That is a material correction to the original framing, not simply improved attribution.

However:

- The original H1, frontmatter verdict, and generated `BOARD/INDEX.md:594` still present the superseded triple-witching framing without a correction marker.
- `routed/delivery_log.tsv` has only the original two handoffs for this signal, to VIOLET and HENRY. The correcting addendum says the correction reaches HENRY on the original INFO line, but leaving the recipient list unchanged does not deliver a new correction.
- HENRY had already consumed the original (`AGENTS/HENRY/board_log.tsv:332`). Its committed `STATUS.md:110` still associates $9.6T with the September 18 OPEX event; it correctly retains an UNVERIFIED-RELAY warning, which limits the observed consequence. I found no separate correction packet in the inspected HENRY inbox or WALTER delivery records.

This violates WALTER's existing linkage requirement in `design/BOARD_CONSUMPTION_SPEC.md:293–320`: correcting signal linkage, visible INDEX back-marker, and a banner immediately after the original's frontmatter. The generator derives markers from structured metadata, not arbitrary footer text.

**Recommendation:** complete this correction through the existing correction mechanism: independently addressable correcting dispatch, an additive banner at the original's entry point, generated discovery linkage, and explicit downstream delivery. Preserve the source-extract limitation. Do not hand-edit the generated INDEX or rewrite the historical claim. Verify what a reader of the original index row, direct file link, and already-consumed inbox handoff would encounter.

**2. High — consuming an original signal can falsely discharge its later correction.**

On September 11, `SIG-W-20260911-003` received separate `-003-CORRECTION.md` handoffs. Commit `644ffeab5` changed the correction's ledger ID back to the parent ID to satisfy ID/BOARD reconciliation. The delivery log consequently contains both original and correction rows under the same `(signal_id, recipient)` key.

The doctor collapses filenames through `_bare_sig`, then tests whether that bare ID occurs anywhere in the recipient's raw board log. `_delivery_routed_dates` also collapses multiple deliveries to this key, keeping the last date. The correction's separate filename therefore does not preserve its acknowledgment identity or its independent age.

Reproduced against both the review snapshot and repair `019c7a4d9`:

| Fixture | Actual doctor result |
|---|---|
| Delivered correction, ten days old, no receipt | MED: one unconsumed ACTION |
| Same correction, receipt for original only | LOW: “CONSUMED but never filed”; INFO: all consumed or within grace |

This is a demonstrated checker defect, not proof that the real FALCON correction was missed. FALCON's actual log separately records both items at lines 132–133. Its separate correction ID illustrates the identity the WALTER-side checker loses.

**Recommendation:** use independently identifiable correction dispatches, or an explicit delivery/revision key consistently across both logs and consumption checks. Match exact parsed receipt identifiers and qualifying dispositions. An original acknowledgment must not discharge a later correction, and adding a correction must not reset the original's age. Test the full backlog function with original-consumed/correction-unread and correction-consumed/original-unread cases.

**3. Medium — the new inbox step still runs after fresh dispatches.**

Commit `235d1792c` correctly added the previously missing top-level inbox scan. But `CLAUDE.md:76` step 7e(d) explicitly routes new RESEARCH-INTAKE breaches; the new top-level scan is step 7g at line 86. The boot section says order matters.

The incident this repair addresses included dispatching `-003` before reading an already-arrived Petroline packet, then correcting the dispatch's interpretation. Following the amended order still permits the same sequence: route fresh intake first, read existing corrections and owner packets afterward.

**Recommendation:** place inbox correction/owner-return reconciliation before fresh external-intake dispatch. Scanning a directory eventually does not establish the prerequisite needed to interpret new items. Verify the sequence with an already-present correction and a related new intake item; no new monitoring system is needed.

**4. Medium — the authoritative continuation file still carries completed work as pending.**

At the review snapshot, `LAST_COMPLETION.md:38` recommends spawning/re-dating/withdrawing `REQ-DEWEY-20260829-002`. WALTER's own `DEEP_RESEARCH_FLAGGED_LOG.tsv` already records it RESOLVED, delivered September 10, and `675b5828c` closed it. PROME's WQ-205 row also records delivery. This stale request predates the final September 11 closeout, so it is not merely an update written seconds after that closeout.

The same continuation file still says the anchor needs rotation (line 42) and CARL's ruling needs incorporation (line 44), although `1b572d723` and `e16705d38` completed those tasks. Later edits added L334 details without discharging these entries. The newer `019c7a4d9` amendment changes the L334 interpretation but does not remove these stale carries.

**Recommendation:** when completing a named follow-up, discharge its canonical continuation entry in the same bounded change. Reconcile decision requests against their owner records before emitting WILL_NEEDS. Use completion references for these three items; avoid creating another ledger that can disagree with the existing ones.

**5. Medium — extend the timestamp repair to historical integrity and whole-field validation.**

The earlier `d398fb2f5` sweep corrected the second September 11 batch, but remaining BOARD timestamps are later than the commits that first contain those files. A comparison of the 31 recent signals against their first-add commit found **16 anomalies exceeding two minutes**: 12 from September 10 and four from the first September 11 session.

Examples:

| Signal | Recorded dispatch UTC | First-add commit UTC | Difference |
|---|---|---|---|
| `SIG-W-20260910-011` | September 10 22:45 | September 10 22:11:40 (`98e1b2666`) | +33m20s |
| `SIG-W-20260911-004` | September 11 19:15 | September 11 18:01:32 (`235d1792c`) | +73m28s |

The September 10 `-011` timestamp also appears in five delivery rows. These are chronology inconsistencies relative to Git's recorded clock; commit time is corroborating evidence and an upper bound on first recorded existence, not proof of exact dispatch time. They should not be “corrected” by inventing precise historical seconds.

The new `019c7a4d9` check is useful, but reports clean for malformed/missing values it never parses. Isolated fixtures produced:

| Delivery timestamp field | Result |
|---|---|
| `NOT-A-TIMESTAMP` | INFO: no future or malformed timestamps |
| empty | Same INFO |
| `2099-01-01T00:00:00+00:00` | Same INFO |
| `2099-01-01T00:00:00Z` | HIGH, correctly detected |

Its regex extracts a narrow valid-looking pattern; unmatched values disappear. If offsets are disallowed by the schema, reject them explicitly rather than passing them as clean. A comparison only against the present clock also cannot detect stamps that were future-dated when written but have since aged into the past.

**Recommendation:** parse every required timestamp field in full, explicitly fail missing/unparseable/noncanonical values, and generate new stamps mechanically. Conduct a bounded historical reconciliation of these 16 anomalies using contemporaneous evidence, retaining uncertainty where exact times are unrecoverable. Do not replace historical dispatch times with the current clock. Keep occurrence time, record creation, and repair time distinct.

**Already assigned work and positive findings.**

The exemption/backlog mismatch raised in the prior conversation is addressed in `019c7a4d9`: role classification now precedes desk exemption, and ACTION/INFO ages are separated. The commit also corrects the “INFO proven free” wording in WALTER's continuation file and reports forwarding the owner-document issue to PROME. These are progress, not fresh unresolved findings here. The correction-identity reproduction above still fails on that version. The new tests exercise role classification; they do not cover that full consumption path.

Several choices in the reviewed work were sound:

- The CRUISE retrospective distinguished a low-consequence missed corroborating cc from a missing primary fact, separated collector coverage from routing coverage, and explicitly retracted the incorrect HERMES claim after checking CRUISE's actual charter.
- The Petroline handoff preserved the distinction between shutdown, physical damage, and lost volume; CARL's recipient record shows it turned the request into a dated check without automatically changing its conclusion. That is direct evidence of useful downstream consumption.
- The large-looking `route_log.tsv` rewrite in `644ffeab5` did not change any pre-existing logical CSV-parsed row between the baseline and review snapshot. The textual churn was not evidence of corrupted historical content.
- Source limitations were often carried explicitly: the Citadel search-extract qualification, secondary-image provenance, and owner-versus-router judgment boundaries were visible. The issue is ensuring those qualifications and corrections reach every consuming surface.

**Suggested order:** finish the options correction's publication/delivery path; fix correction acknowledgment identity; move inbox reconciliation before dispatch; clear the three stale continuation items; extend the timestamp validation already underway. These are bounded repairs to demonstrated failures. More narrative rules or another broad process audit are not prerequisites.

**Follow-up verification — repair `98bd090fc`.**

Inspected the committed patch and reran checks against an isolated copy of this revision. The local `origin/master` tracking ref contains the commit. Findings 1, 3, and 4 are addressed at the reviewed surfaces: a standalone `SIG-W-20260911-011` correction now produces the original's INDEX back-marker and entry banner, with a committed HENRY ACTION handoff preserving the extract-based uncertainty; step 7e(d) explicitly blocks on completion of 7g; the three stale pending requests have been discharged. This verifies WALTER's publication/delivery repair, not HENRY's subsequent integration. Findings 2 and the historical part of 5 are explicitly carried in LAST_COMPLETION, with a next-session scope for the identity repair. Deferring that cross-log change is reasonable.

The production timestamp function now correctly flags the earlier junk, empty, and noncanonical-offset fixtures and detects a canonical future timestamp. However, its new approximate-minute exception (`walter_doctor.py:2548`) returns before validating either the calendar date or whether it lies in the future. Direct calls to **the production `check_future_timestamps()`** with isolated delivery rows reproduced:

| Field | Actual result |
|---|---|
| `2099-01-01T02:3xZ` | INFO: known convention, “NOT a defect” |
| `2026-99-99T02:3xZ` | Same INFO despite an impossible calendar date |

Minute uncertainty cannot excuse an impossible or clearly future **date**, which is the part the backlog instrument actually reads. Preserve valid historical approximations, validate their certain components, and compare their possible time interval with the clock without inventing an exact minute. Also correct the explanation that no consumer needs minutes: `check_terry_override_ratio()` already parses this same timestamp column for a 72-hour condition.

All 11 supplied reproductions pass with the committed delivery-log fixture. **That does not exercise the production timestamp validator:** six of the tests call a separate `_classify()` defined inside `test_doctor_backlog.py:67`, with duplicated regular expressions. They would still pass if production stopped flagging those inputs. Replace those tests with calls to the production checker under isolated fixtures (or a shared production parser plus integration tests), including the two approximate-date failures above. This is a focused addition to finding 5, not a request for another broad audit.

**Follow-up verification — repair `4cff9feb9`.**

Both specific follow-up defects are addressed. All 13 tests passed against isolated committed code and its committed delivery-log fixture: five invoke the production role helper and eight invoke the production timestamp checker. The test-only timestamp classifier has been removed. Independently exercised the normal file-reading path, without `_fields`: `2099-01-01T02:3xZ` now produces HIGH, `2026-99-99T02:3xZ` produces MED, and valid historical `2026-08-15T02:3xZ` remains INFO. The local origin tracking ref contains the commit.

This establishes the named approximate-date fixes and test wiring, not exhaustive timestamp correctness or a full fleet health certification. Approximate time-of-day interval validation and the earlier explanatory note about the existing TERRY hour-based consumer are outside this closure. The two substantive carried repairs remain correction-acknowledgment identity and historical chronology reconciliation. The reviewed fixes are at a reasonable stopping point; resume those bounded tasks in a fresh session.
