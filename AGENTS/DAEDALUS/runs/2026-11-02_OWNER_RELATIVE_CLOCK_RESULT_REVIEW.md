# Owner-relative profile clock — independent RESULT review

**Disposition: HOLD.** One blocking boundary class permits historical/example text to supply a nonexistent owner header and return CLEAN. No profile-refresh or maintenance-clearance claim is established. Reader `/root/prome_spine_read`, OpenAI Codex, exact model variant UNKNOWN. No code/owner edits or commits; sole write is this report. Final code fixes after this read are POST-REVIEW until separately checked.

## Scope

Read current `scripts/profile_clock_check.py` whole, test changes plus existing whole suite context, HEAD diff for those two paths, prior acceptance plan and own remedy review. Compared consumer `sweeps_due.py` rc aggregation and DAEDALUS gate B1/C0 mappings previously inspected; `git diff` on caller files is empty. Examined frozen production-fixture diff (empty) and ran the manifest hash regression. This is the clock result read only; optional L911 representation diff not examined.

## Observed tests

`python3 scripts/tests/test_profile_clock_check.py`: **16/16 passing**. Frozen provenance test passes. Existing OSPREY snapshot is unchanged and continues to refuse when its disposable named owner is absent. Tests no longer depend on production owner directories because `--owners-root` is supplied in the helper.

Independent disposable cases, body August 7 and as-of November 2 (wall age 87 days), expected outcomes written from the accepted contract:

| Case | Expected | Actual |
|---|---:|---:|
| Owner Last owner update August 28 (21-day lead) | 0 CLEAN | 0 |
| Owner Last Updated August 29 (22-day lead) | 1 ALERT | 1 |
| Same 21-day lead plus hard floor October 31 | 1 ALERT for floor | 1, floor independently named |
| Malformed November 99 header then valid As of header | 2 CANNOT-EVALUATE | 2 |
| STATUS-relative21 OR no-update7 mixed referents | 2 CANNOT-EVALUATE | 2 |
| No real header; `## History` then dated declaration | 2 CANNOT-EVALUATE | 2 |
| No real header; `# History` after title then dated declaration | 2 CANNOT-EVALUATE | **0 CLEAN** |
| No real header; Setext `History` / `-------` then dated declaration | 2 CANNOT-EVALUATE | **0 CLEAN** |
| No real header; fenced example containing dated declaration | 2 CANNOT-EVALUATE | **0 CLEAN** |

The first two cases discriminate an erroneous wall-clock implementation. The absolute floor remains as-of-based. New generic footer properly distinguishes supported relative comparisons from unsupported predicates. Missing/future/conflicting/before-body checks in the shipped suite pass.

## Blocking finding F1 — owner header parser crosses declared content boundary

**Claim:** the accepted plan limits owner date declarations to the header before the first content section and forbids arbitrary history/exemplar dates. `owner_stamp` instead stops only on `^\s*#{2,}\s`; it never stops on a subsequent H1/Setext section and does not exclude code fences.

**Artifact / exact reproduction:** `scripts/profile_clock_check.py:owner_stamp` reads this owner file:

```markdown
# STATUS
# History
Last Updated: 2026-08-28
```

with profile:

```markdown
**Profile vintage:** 2026-08-07
**Staleness:** STATUS stamp leads body >21d
```

Call main with disposable `--profiles`, disposable `--owners-root` and `--as-of 2026-11-02`. Output includes `owner stamp 2026-08-28, lead 21d` and `PROFILE-CLOCK 0: 1 evaluated dated clocks inside window`, rc0. There is no actual current owner header. Replacing the History heading with Setext or a fenced `Last Updated` example reproduces the false clean.

**Consequence:** a supported-looking date in a historical/example block can clear the day clock on rc0 instead of preserving UNKNOWN. The parser's correctness on the two current production owners does not establish its declared generic header boundary.

**Minimal remedy:** keep the narrow named-field reader; conservatively terminate/exclude content at subsequent top-level headings, Setext sections and fenced examples as well as existing H2+ headings. Preserve the first document title and actual owner header before it. Unsupported/ambiguous header structure should refuse rather than search farther. Add the independent no-real-header counterexamples above; keep all existing boundary/fixture results. No general Markdown parser, new state token, owner edit or new checker is required.

**Own refuter:** an explicit, reviewed contract restricting allowed owner STATUS syntax to only H2+ content sections and forbidding all H1/Setext/code content before them would remove these cases from the supported population, but the accepted plan instead says “before the first content section” and the tool advertises named header dates without that restriction. No such narrowed contract was present in the reviewed plan/code. Merely passing HENRY/OSPREY does not refute this class.

## Acceptance and remaining limits

The intended comparison, strict > operator, original body date, chronological validation, consumer rc mappings, absolute floor and frozen fixtures are correct in tested cases. HOLD concerns the parser perimeter, not the formula or the need for the repair. Do not label the tool independently verified/fixed until F1 is resolved and its changed portion checked. A successful future result only evaluates existing profile predicates; it never certifies a whole-profile refresh, content/event trigger completion or a grade change.

No live production checker run was needed for this result decision; tests use disposable owners only. No L911 review performed.

Reviewed source SHA256: `52049177150624797a5f29767846b4bdb485f596fcd81860a507a5ef2a50b166`.
Reviewed test SHA256: `2c3b661061e10dd640abbd5b0f6a18fa2bd83c28e64ebebacb965af966405d49`.
Observed review time: 2026-11-02T10:09:38-05:00

## Bounded recheck after POST-REVIEW correction 1

**Disposition: HOLD remains on F1's short-Setext boundary variant.** Original evidence above is unchanged; the initially reported three reproductions are now repaired at the inspected code. Read changed owner_stamp and new regression test in full; reviewed their context against the prior accepted contract. No owner/code edits by reader.

`python3 scripts/tests/test_profile_clock_check.py`: **17/17 PASS**. Independently re-ran H1, seven-dash Setext, backtick fence and tilde-fence cases, each with (a) no real owner header and (b) a valid preceding August 29 header. All eight produce the expected outcomes: (a) rc2 CANNOT-EVALUATE, (b) rc1 ALERT with lead 22. The initial H1 title remains permitted. These are the author's correction now independently observed, not inferred from suite count.

The new lookahead recognizes Setext/horizontal-rule lines with `=+` or `-{3,}`. A short Setext underline remains outside that branch:

```markdown
# STATUS
History
--
Last Updated: 2026-08-28
```

With the same August 7 body/November 2 as-of fixture, observed **rc0 CLEAN**, expected **rc2 CANNOT-EVALUATE**. With a valid preceding `Last Updated: 2026-08-29`, observed rc2 conflicting owner dates instead of preserving rc1 lead 22. The two-hyphen line is still a Setext section underline; the accepted plan never restricted them to horizontal-rule length.

**Minimal same-class correction:** accept one-or-more hyphens in this existing Setext lookahead (`-+` rather than `-{3,}`), and include the short-underline variant in the existing regression. No new checker, parser library, state or scope is proposed. This is F1's incomplete boundary fix, not a new episode or a redefinition of the predicate. Further author correction is POST-REVIEW until its applicable disposition.

Caller rc meanings, strict day-boundary formula, independent floor, metadata source and frozen fixture guarantees are unchanged. This recheck does not certify any profile refreshed or authorize a clean maintenance/L5 verdict. Optional L911 review still not performed.

Recheck time: 2026-11-02T10:11:15-05:00

## Final bounded recheck — POST-REVIEW correction 2

**FINAL DISPOSITION: ACCEPT for the reviewed owner-relative clock repair.** This supersedes the earlier HOLD dispositions for the code revisions they examined; all original evidence remains above. The author changed the existing Setext lookahead from `-{3,}` to `-+`, and added one/two/seven-hyphen and one-equals cases to the existing boundary regression. No unrelated scope or owner mutation was part of this recheck.

Re-read the exact final `owner_stamp` function and changed test block against prior source/plan/consumer context. Re-ran the full focused suite: **17/17 PASS**, including immutable-production-fixture hash check, original OSPREY missing-owner refusal, strict 21/22 relative boundary, absolute-floor independence, invalid/future/conflicting/before-body owner headers and mixed-clock refusal. Independently ran eight disposable short/long Setext cases (one, two, seven hyphens and one equals; absent real header vs valid preceding August 29 header): **8/8 PASS**, expected rc2 for the former and rc1 lead 22 for the latter. The earlier independent H1/backtick/tilde checks also passed after correction1, and are rerun by the suite at this final revision.

One attempted independent recheck harness had a local Python `else2` typo and did not execute; it was corrected and the eight-case run above completed. No production code was changed by the reader.

Reviewed final source SHA256: `e6f1003671d8a38b39b0843fa5f32dbbd0ff1e67c83d2be1816eea59e8285beb`.
Reviewed final test SHA256: `aef38fcb840f930b51dbdd76c5c242e91e33381a927e96c54b62f36a733270b8`.

**Remaining limits:** this is a narrow header/date evaluator, not a general Markdown parser or a content/event-trigger certifier. Unknown/ambiguous headers must still refuse; these checks cannot prove the truth of declared owner dates or whole-profile refresh work. No HENRY/OSPREY profile refresh, grade promotion, whole-maintenance clearance or L911 certification follows from ACCEPT. No further code changes are covered by the named hashes. Caller rc mappings remain unchanged from the inspected source.

Final recheck time: 2026-11-02T10:12:03-05:00
