# ACCEPTANCE — WQ-289 (b): the narrow L367 form in `argus_scope.py --verify-review --paths`

**Written 2026-09-25 01:05 ET, BEFORE the edit** (WQ-229 discipline). Ruling: Will 2026-09-24 23:37 ET *"Approve WQ-289 with your rec and push"*; DOCKET L473; WILL_QUEUE WQ-289. Origin: the prome-1f third-leg closeout was HELD at step 10 because the two paths of a consumed packet's `git mv` (`PROME/inbox/X.md → PROME/inbox/processed/X.md`, R100, bytes already on origin under the sender's commit) are EXCLUDED by the perimeter, can never enter a review manifest, and the explicit-list form flags every unreviewed path (`PROME/reports/2026-09-24_prome-1f-c-closeout.md` § PUSHED).

## The ruled form (verbatim from the WQ-289 rec)

> a byte-identical `git mv` of an EXCLUDED inbound packet whose bytes are already on origin satisfies `argus_scope.py --verify-review --paths` when ARGUS has confirmed R100 at the artifact; every other addition at an EXCLUDED path keeps blocking.

## Properties the repair must hold (the defect's terms, not the symptom's)

- **P1 — Declared, never inferred.** A consumed move is exempt only if PROME DECLARED it in the review manifest at freeze time (`--record-review --consumed-move ORIGIN DEST`, repeatable). The tool never scans the tree for "things that look like moves". Undeclared move ⇒ UNREVIEWED, blocks.
- **P2 — ARGUS confirmed = the manifest verdict is REVIEWED.** A declared move under a FROZEN manifest still blocks. (`--mark-reviewed` is the only writer of REVIEWED and it is the audit's outcome; ARGUS's agent file gains one instruction: confirm each declared consumed move at the artifact.)
- **P3 — Bytes already on origin, established by the tool itself at verify time**, never trusted from the declaration: sha256(`origin/master:ORIGIN`) == sha256(DEST in `--ref` if given, else the working tree). Any difference (R<100, an edit after the move, a different file) ⇒ blocks.
- **P4 — A move, not a copy, AS GIT RECORDS IT (amended after reader round 1, ❌1/❌3/❌4):** git's own rename detection reports the pair as `R100` — staged (`--cached`) in the working-tree form, inside `ref^..ref` in the `--ref` form — so the rename SOURCE was in the parent with identical bytes. ORIGIN absent (`lexists`, so a dangling link counts as present), DEST present and not a symlink, no unstaged edit on DEST, an unstaged plain `mv` refused. An addition that merely matches an origin blob is not a move.
- **P5 — PROME's own inbox only (authorship by PATH, never by subject):** ORIGIN matches `PROME/inbox/**` and is NOT under `processed/`; DEST matches `PROME/inbox/processed/**`; same basename. Any other pair (another desk's inbox, a non-inbox EXCLUDED path, a rename out of inbox into a PROME surface) ⇒ blocks with the reason. Consumption in `AGENTS/*/inbox/processed/` is the RECIPIENT's act (perimeter row 17) and never PROME's.
- **P6 — Fail closed on missing information (amended, ❌6):** the tool FETCHES `origin master` before reading the blob (step 10 runs before `safe-push.sh`, so the tracking ref may be stale); fetch failure, `origin/master` unresolvable, ORIGIN not on origin, manifest unreadable, baseline unusable ⇒ the exemption does NOT apply; the existing rc (1 UNREVIEWED / 2 CANNOT-EVALUATE) stands. The tool never prints an R100 receipt it could not establish.
- **P7 — Every other caller and form is UNTOUCHED:** the manifest-only form (`paths=None`) behaves byte-for-byte as before (discovery already drops EXCLUDED paths, so these moves never reached it); `--mark-reviewed`'s refusal logic unchanged; content comparison of reviewed paths unchanged; `RECEIPT_PATHS` unchanged; rc semantics unchanged.
- **P8 — Visible, not silent (amended, ❌5/❌2):** the exemption applies only when BOTH halves are in `--paths` and no ORIGIN is declared twice; an exempted move prints one `R100-CONSUMED-MOVE` line naming ORIGIN → DEST and the origin commit-ish it was matched against, so the receipt shows what was let through and why.

## Test list (derived from P1–P8; the file is `test_argus_r100_consumed_move_WQ289.py`)

1. ordinary: declared R100 move of a PROME-inbox packet whose bytes are on origin, manifest REVIEWED, `--paths` includes both rename paths ⇒ rc 0, R100 line printed (P1 P2 P3 P4 P5 P8)
2. undeclared identical move ⇒ rc 1 UNREVIEWED (P1)
3. declared but manifest FROZEN (ARGUS not run) ⇒ rc 1 (P2)
4. declared, DEST edited after the move (R<100) ⇒ rc 1 (P3; also the OVERLAP neighbour: a path both renamed and edited)
5. declared, ORIGIN's bytes were never pushed (a local-only packet) ⇒ rc 1 with the reason (P3 P6)
6. declared, no `origin/master` at all ⇒ rc 1, no R100 receipt printed (P6 — missing information)
7. declared, ORIGIN still present (a copy) ⇒ rc 1 (P4)
8. wrong owner: identical move inside `AGENTS/BRENT/inbox/` ⇒ rc 1 (P5)
9. wrong owner: DEST outside `processed/` (`PROME/inbox/X.md → PROME/reports/X.md`) ⇒ rc 1 (P5)
10. a NEW file at an EXCLUDED path in the same commit set still blocks beside an exempt move (the ruled "every other addition keeps blocking")
11. `--ref HEAD` form: the committed move passes; the same commit with a content change blocks (P3 in the committed reader)
12. manifest-only form unchanged: `paths=None` over the same tree returns what it returned before the edit (P7)
13. concurrent: origin advanced so that ORIGIN no longer exists on `origin/master` (a peer moved or deleted it) ⇒ rc 1 (P6, category 5)

## Neighbour categories (contract: CONSIDER, justified N/A allowed)

| # | Category | Disposition |
|---|---|---|
| 1 | Ordinary | test 1, 11 |
| 2 | Overlap | test 4 (renamed AND edited); test 10 (an exempt move beside a blocking addition in one list) |
| 3 | Wrong owner | tests 8, 9 (another desk's inbox; a destination that is a PROME surface, not consumption) |
| 4 | Missing information | tests 5, 6 (bytes not on origin; no origin ref) — fail LOUD, exemption withheld, existing rc stands |
| 5 | Concurrent | test 13 (origin moved under us) |

## Completion note format (four states, never merged)

IMPLEMENTED · TESTED (`python3 -W error::ResourceWarning -m unittest …`, count by `grep -c 'def test_'`) · INDEPENDENTLY VERIFIED (an Opus reader who did not write the fix devises ≥1 counterexample of its own; its ledger path named) · STILL UNRESOLVED (anything the reader found and PROME did not fix, verbatim).

## Reader round 1 (2026-09-25 01:16 ET, Opus, ledger `scratchpad/wq289reader_ledger.md` of session `prome-fa`): 7 ❌ · 8 ⚠️ · 12 ✅ against the first implementation — NOT VERIFIED

❌1 addition matching an origin blob passed (CE1) · ❌2 one ORIGIN two DESTs passed (CE2) · ❌3 rename+edit matching a newer origin blob passed (CE3) · ❌4 symlinks (CE4/CE5) · ❌5 half-listed pair passed silently (CE8) · ❌6 stale tracking ref passed; docstring claimed a fetch the closeout order does not provide (CE3b) · ❌7 the ARGUS instruction repeated the tool's own check. **All seven fixed in the second implementation; each has a regression test named `test_ce*` in the suite.** ⚠️ dispositions: ⚠️8 P7 'byte-for-byte' is false for a malformed manifest (stricter: rc 2 vs 0) — ACCEPTED as the intended direction, P7 wording stands as 'ordinary inputs'; ⚠️9 null value TypeError — FIXED (rc 2); ⚠️10 dotted DEST — FIXED (refused); ⚠️11 CLI silent inputs — FIXED (errors); ⚠️12 runner/manual unaware of the flag and a re-freeze erases declarations — CLOSEOUT.md + the closeout skill carry one sentence now; re-declare at every re-freeze; ⚠️13 one REVIEWED verdict for the whole manifest, no per-pair verdict — RESIDUE (design; the `--mark-reviewed` note carries ARGUS's per-pair word, not a machine field); ⚠️14 argus.md '0 insertions / 0 deletions' ambiguous — FIXED ('prints NOTHING'); ⚠️15 neighbour coverage — FIXED by the CE tests.

## Reader round 2 (2026-09-25 01:26 ET, Opus, ledger `scratchpad/wq289reader2_ledger.md` of session `prome-fa`): 4 ❌ · 9 ⚠️ · 13 ✅ against the second implementation — NOT VERIFIED

❌A the short name `origin/master` is shadowed by a local branch/tag of that name, and a repo without the standard refspec updates only FETCH_HEAD — an unpushed packet passed `--ref HEAD` (R2-6/R2-7) → FIXED: fetch by explicit refspec into `refs/remotes/origin/master`, resolve the commit sha once per verify, read blobs by sha, print the sha in the receipt · ❌B the working-tree form hashed the file on disk while git's R100 describes the index (assume-unchanged / CRLF filters) (R2-1/R2-2) → FIXED: hash the INDEX blob and require disk == index · ❌C the ARGUS instruction claimed legs 'the tool does NOT make' while every leg was the tool's own → FIXED: legs split into (a) second execution and (b) three the tool cannot make — read-only `ls-remote` sha, the origin commit that ADDED the packet is another desk's, the packet's consumption named in a PROME record · ❌D the skill pointed at CLOSEOUT step 5 → step 8. **Regressions `test_r2_*` added. ⛔ These fixes are UNREAD — the WQ-178 read budget (one result read + the one allowed further read) is spent and the two-correction stop has tripped on `argus_scope.py`; the file is closed for this session.**

**Declared residue (round 2 ⚠️, un-fixed):** ⚠️1 ARGUS-and-fetch — RESOLVED by design (ARGUS now uses `ls-remote`, never fetches) · ⚠️2 '④ legs' wording — FIXED in CLOSEOUT.md · ⚠️3 one fetch per verify + sha in receipt — FOLDED into ❌A · ⚠️4 a network failure reads rc 1 UNREVIEWED rather than rc 2 CANNOT-EVALUATE (a `CANNOT-ESTABLISH` line is printed; rc stays 1) — open, fail-closed · ⚠️5 a move committed EARLIER than `ref` is refused as 'not a rename' — open, fail-closed; `--paths` at step 10 is the closeout commit's own set so it should not arise · ⚠️6 a non-ASCII packet name is refused (git quotePath) — open, fail-closed · ⚠️7 a DEST hand-placed inside the reviewed manifest exempts ORIGIN with no receipt — open, needs a hand-edited manifest · ⚠️8 the verify now writes `.git` (fetch) at step 10 — accepted; fail-closed noise · ⚠️9 round-1 ⚠️13 (one REVIEWED verdict for the whole manifest, no per-pair machine field) — open, design. **Round 3 owed at the next session before the exemption is relied on for a real closeout (it was not exercised tonight: every consumed packet was committed before the closeout).**
