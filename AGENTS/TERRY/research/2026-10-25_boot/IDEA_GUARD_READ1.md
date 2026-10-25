# Independent result review — TERRY ledger guard

Date: 2026-10-25. Reviewer: Codex helper `/root/terry_guard_review`, OpenAI GPT-6 runtime; exact model/session identifiers beyond the exposed helper name UNKNOWN. Read-only review of implementation `3be3db220fb5ca61ef165e598b114c82e9c7911b`, compared with its parent. Scope: `AGENTS/TERRY/scripts/ledger_sweep.py`, IDEA identity coverage for A/G/H, preserving existing comparison policy. No desk boot, desk edits, commits, external calls, or TERRY contact. Root/local instructions and COMPLETION_SPEC reviewer exemption explicitly read.

Episode: parent reports no prior independent reads; this is the first independent result read, with reviewer-devised counterexamples. Acceptance file was read before testing. It has no `reads:` field; that durable history limitation remains for PROME to reconcile. This is not a retrospective plan review.

**Verdict: PARTIAL / full acceptance STILL UNRESOLVED.** VERIFIED: namespace inclusion works for A and H in the tested cases; existing policy expressions are unchanged; author selftest passes. One blocking acceptance gap remains for G in the normal IDEA table/card layout. This review conveys no operational or trading approval.

## Blocking finding F1 — normal IDEA structures can still disagree while G returns no findings

**VERIFIED, acceptance condition 2 not established end to end.** `index_md_states()` (lines 351–360) supplies only `cells[1]`, the state cell. INDEX stores the actual structure in `cells[3]`. `gather_live()` (lines 969–985) supplies only each card's verdict, and SETUPS only verdict/status. Thus a normal IDEA can contribute its only parsed strike/expiry fingerprint through TRADE_BOOK. `check_structure_agreement()` deliberately needs two asserting surfaces, so changing the real structure column or changing that sole TRADE_BOOK fingerprint stays clean.

Independent snapshot reproduction uses the existing `IDEA-QQQ-PUTWALL-OCT22` row at `3be3db220`, not the author's handcrafted G claims:

1. Export exact committed TERRY scripts, cards, INDEX, SETUPS, TRADE_BOOK and PAPER_BOOK into `/tmp/prome-terry-guard-snapshot` (throwaway Git repository).
2. In an injected read of INDEX only, change the ID's fourth data cell from `QQQ Nov-20 690/670P x2 (card default x1)` to `QQQ Nov-20 690/665P x2 (card default x1)`; keep every state and other surface unchanged.
3. Run `claims, cards, _ = gather_live()` then `check_structure_agreement(claims)`.
4. Observed IDEA findings: `[]`; observed INDEX claim is still the unchanged state text beginning `FIRED / LIVE — Will's hand...`, with no strike pair. TRADE_BOOK still asserts `690/670P`.

Exact complete mutated inputs are preserved separately at `/tmp/prome-terry-guard-failing-INDEX.md` and `/tmp/prome-terry-guard-failing-TRADE_BOOK.md`; each is tested alone against the unchanged snapshot.

Second counterexample: change only the last TRADE_BOOK status to `FIRED / LIVE — QQQ Nov-20 690/665P x2`; INDEX's real structure column remains `690/670P`. G again returns `[]`. Control: put the differing pair directly in the INDEX *state* cell and G does fire with `INDEX.md=690/665 · TRADE_BOOK.md=690/670`.

The author test at lines 1109–1113 constructs the G claims dictionary directly and therefore bypasses precisely this reader gap. The gap predates this commit's generic readers; it is an unmet broad acceptance condition, not evidence that adding IDEA to the regex introduced a regression. The narrow namespace implementation and unchanged fingerprint policy can both be correct while the promised real-surface G coverage remains incomplete. PROME should keep that distinction in the completion disposition. An owner remedy or an explicit acceptance/scope disposition is needed before calling full A/G/H coverage independently verified; do not widen COMPATIBLE or the fingerprint rules to make the test pass.

## Tests and positive evidence

Replay: `python3 -B -W error::ResourceWarning /tmp/prome-terry-guard-tests.py > /tmp/prome-terry-guard-results.jsonl` (exit 0). Fixture inputs come solely from `git show 3be3db220:<path>`; parent implementation is separately exported. Full probe code and observations remain at those paths. The probe records results rather than hiding the known G failure behind a successful assertion count.

- Ordinary: committed snapshot A/G/H all return `[]`. Independently changing the IDEA card verdict, INDEX state, or last TRADE_BOOK state to CLOSED produces A disagreement for that ID each time. Matching surfaces stay clean.
- Structure control/counterexamples: preceding F1 cases exercise `gather_live()` before G. Existing strike/expiry extraction rules were preserved.
- Overlap: H sums two OPEN real IDEA lots, excludes CLOSED real and OPEN paper rows, and keeps the longer `...-OTHER` compound identity separate rather than truncating/merging it.
- Wrong owner: target's stale x1 rows still yield H drift against live x2 when unrelated IDEA rows mention the target with x2; cross-card rows do not donate a count. INDEX, last TRADE_BOOK row and SETUPS are all exercised through `check_contract_counts()` read injection. Matching x2 rows return `[]`.
- Missing information: regions without count claims return `[]`, consistent with the unchanged count-present policy; this does not establish count completeness. F1 separately demonstrates absent extracted structure information and the resulting silence.
- Concurrent activity: N/A to this bounded parser repair review; fixtures are immutable committed snapshots with one temporary reader. No concurrency/transactional-read guarantee is claimed or added. Same-ID multiple lots and distinct long IDs are covered above.
- TRY/MGMT: INDEX and TRADE_BOOK parsing agrees with the parent for representative TRY-FIRE, TRY-MGMT, MGMT option and MGMT share identities. H preserves tested TRY counts and now additionally recognizes standalone MGMT IDs (parent's TRY-only H reader returned none). This expansion follows `_SID_RE = SETUP_ID_RE`; it is disclosed rather than described as identical prior H namespace coverage.
- Policy invariants: `STATES`, `COMPATIBLE`, STRIKES_RE, EXPIRY_RE and all COUNT_RES patterns compare equal to the parent. No scoring, approval or trade-condition code changed in the reviewed script diff.
- Corroboration only: `selftest()` returns 0 with 111 PASS assertions under ResourceWarning-as-error. Output: `/tmp/prome-terry-guard-selftest.txt`. This is additional evidence, not the source of independent acceptance.

## Nonblocking limits and disposition

VERIFIED: no existing A/G/H mismatch was observed in the frozen committed TERRY fixture. No assertion about the concurrent live workspace or broker position truth follows. The inherited H policy requires the live count to be present among recognized counts; it does not prove every count mention is current, require absent quantities to be filled, or authenticate records. The normalizer/fingerprint/count grammars remain deliberately unchanged. Invalid/malformed IDs and new table dialects are not comprehensively certified by this review.

IMPLEMENTED: IDEA regex inclusion and common full-ID H reader at the named commit. TESTED: author suite and the independent probes above. INDEPENDENTLY VERIFIED: tested A/H namespace behavior and unchanged policy expressions. STILL UNRESOLVED: acceptance 2's normal-surface G coverage (F1); full repair completion must retain this qualification. Stop this read here; no unrequested extra review or owner correction was performed.

## COMPLETION — TERRY GUARD REVIEW — 2026-10-25
STATUS: ✅ DONE
CHANGED: /tmp/prome-terry-guard-review.md, /tmp/prome-terry-guard-tests.py, /tmp/prome-terry-guard-results.jsonl, /tmp/prome-terry-guard-selftest.txt, /tmp/prome-terry-guard-snapshot/
RESULT: Independent result review found 1 blocking acceptance gap in normal IDEA G structure coverage; A/H namespace probes and 111 author selftest assertions passed.
GAPS: Full acceptance remains unresolved because the G readers omit normal structure fields; review history has no durable reads field in the supplied acceptance file.
WILL_NEEDS: None.
FOLLOW-UP: PROME to record the review/disposition and retain F1 in repair-completion status; no operational approval given.
