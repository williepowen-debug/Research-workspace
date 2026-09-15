# L335 — preserve OPEN-row source content in event history

**Authority:** Will, after the September 14 recommendation to fix L335: “ok approved go ahead”. **Scope:** source-to-ledger coverage of OPEN queue rows; no Deck interaction/ruling change. Acceptance written before implementation. Because rollout appends newly captured content across existing OPEN rows, use one blind plan read and one independent result read under PROME's existing review discipline.

## Problem and chosen representation

`wq_ledger.live_state()` projects OPEN rows to capped summaries and selected derived facts. Ordinary Notes and Item-body changes can leave that projection unchanged, so `diff_state` correctly compares two identical but incomplete records and writes no history.

Keep the existing TSV schema and all historical bytes. For rows returned by the canonical `decision_deck.parse_open`, populate the previously empty `record` field with deterministic JSON:

```json
{"format":"wq-open-source-v1","item":"...","kind":"...","by_raw":"...","since":"...","rec":"...","notes":"..."}
```

Values are the complete parsed cells, without ledger truncation or markdown stripping. `kind` and `since` are already normalized by the shared parser; that parser remains the owner. JSON escapes embedded control characters so TSV round-trip retains them. Preserve Unicode, links and markdown inside Item/Notes/rec. Sort keys, fix JSON separators, and omit generated metadata. Do not add a second queue parser.

`record` continues to hold the existing ruling record for terminal rows. This explicitly supersedes the historical WQ-203 installation note that OPEN `record` is empty. It does not reinterpret a source snapshot as a ruling: `status_after`, `verdict` and `will_verbatim` retain their existing derivations, and the Deck's ledger reader only consumes terminal rows. New `record` content is compared by the existing semantic-payload mechanism.

## Acceptance conditions

1. A change anywhere in parsed OPEN Item or Notes yields exactly one UPDATED event, including changes beyond the title/summary caps, URL targets with unchanged labels, and changes back to an earlier value.
2. Retain all six parsed OPEN cells named above, including complete rec and raw Needed-by text. Source snapshot content round-trips through the TSV, without hashes substituting for the evidence itself.
3. Unchanged parsed source produces no new event, even on repeated same-minute syncs. Table padding and unrelated prose outside OPEN rows do not fabricate events. Removing notes is a change; absent optional Notes and an empty Notes cell are equivalent through the existing parser.
4. Existing status transitions, quote extraction, OPEN precedence over archives, terminal Deck records and the schema remain unchanged. New snapshots are not a ruling and never enter Decided while their row remains OPEN/ANSWERED/BLOCKED.
5. Existing sealed ledgers remain readable. First upgraded sync appends one observed-current snapshot event for each existing OPEN row missing that content; it does not rewrite history or assert that the content was just edited by Will. A repeat sync adds zero. Historical missing amendments cannot be reconstructed by this repair.
6. Tool-only append, seal validation and consecutive-no-op detection remain active. Failed seal checks leave ledger and sidecar unchanged. Rollout preserves the old ledger as an exact byte prefix.
7. Full snapshots remain readable beyond the CSV module's default field limit. Set reader capacity from the file size while reading, restore the caller's previous CSV limit afterward, and test a Notes cell exceeding 128 KiB through append/read/repeat-sync/check.

## Verification and rollout

- Reproduce Notes and Item-body omissions on the original code using disposable fixtures.
- Extend the existing L336 test file with fixture-driven source→sync→stored-event cases, including long tails, deletion, A→B→A, control characters, link target changes, unchanged repeats and legacy upgrade.
- Run the existing ledger selftest and Deck selftest; prove terminal Deck projection unchanged in a temporary migration copy.
- Freeze the live queue, archives, ledger and seal into `/tmp`; generate a migration candidate there. Identify the exact added WQ numbers and events, prove old bytes preserved, second sync a no-op and `check` green. Do not backfill over or rebuild the live ledger.
- Independent reader inspects final code and candidate rollout, devises a counterexample beyond the author's tests, and names reviewed source hashes. Fix blocking findings only, declare warnings.
- Before live sync, verify source/ledger/seal snapshots are still current; changed inputs require a fresh candidate, not overwriting concurrent work. Apply through `cmd_sync`, verify expected appended rows and full original prefix, run `check` and a repeat sync, then commit exact owned paths and safe-push.

## Neighbours considered

- **Ordinary:** unchanged queue and one ordinary correction.
- **Overlap:** live OPEN plus older terminal/archive row; existing legacy rows plus new snapshots; A→B→A.
- **Wrong owner:** mutate WQ-901 only; WQ-902 and decided rows remain unchanged. Exclude foreign desk work from staging.
- **Missing information:** missing/empty/deleted notes and legacy empty record; no invention of historical amendments.
- **Concurrent activity:** check source and ledger hashes before rollout; no new multiwriter locking contract. The existing writer remains serial for this bounded operation. Concurrent edits invalidate a frozen migration candidate.

## Completion and declared limits

IMPLEMENTED / TESTED / INDEPENDENTLY VERIFIED / STILL UNRESOLVED will be recorded after execution. Historical hosted tap-loss remains UNKNOWN; this repair neither inspects nor certifies the hosted rulings database. Existing parser limitations and terminal-row summary truncation are outside the OPEN-source coverage repair. The ledger grows because it now retains full evidence; it is not a boot-read surface. The independent review must verify that this does not inflate the terminal Deck projection.

### Blind plan read

`docket_plan_read` identified one blocker before production edits: unbounded snapshots can exceed `csv.DictReader`'s default field limit. Its independent 140,000-character Notes fixture parsed correctly upstream but failed at ledger read. Condition 7 and a corresponding regression cover the repair. Read-only closeout confirmed.

**Declared nonblocking residue:** the existing full Deck archive fallback can still show an older terminal row for an OPEN number. Condition 4 prevents the new snapshot itself from entering the terminal ledger projection; it does not repair that pre-existing archive behavior. The rollout check must treat archive membership as part of its frozen input, since hashing only known files cannot detect a newly selected archive. Historical amendment loss and terminal truncation remain outside scope.

### Result and rollout receipt

**Completed:** `PROME/reports/2026-09-14_L335-ledger-completion.md`. Final code hash `49aeb2da11305637e25aefb3511452cd753504d37a54b56a228e2fa06ac35ece` independently accepted with no blockers. Regression suite 24/24; ledger and Deck selftests PASS. Candidate and live rollout append the same 28 semantic UPDATED snapshots, preserve the baseline prefix, leave Decided unchanged, and add zero on repeat sync. Input hashes and archive membership checked before live write. Existing declared limits remain.
