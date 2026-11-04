# L835 saved candidate — one independent acceptance review

## User authorization, verbatim (2026-11-04)

> I would authorize one independent acceptance review of the saved L835 candidate, with these requirements:
> 1. Reproduce the latest embedded-** failure and confirm it is eliminated.
> 2. Retest the previously discovered counterexamples.
> 3. Examine overlapping wildcard rules and first-match precedence for additional false negatives.
> 4. Verify that genuinely excluded directories don't unnecessarily block routine closeout.
> 5. Exercise the behavior in a disposable repository, including the actual closeout consumer.
> 6. Stop on any blocking finding. No automatic additional repair cycle.
> If it passes, PROME can return with an installation recommendation.
>
> If it fails again, I'd pause the incremental corrections and reconsider the underlying approach. After this many rounds, a simpler conservative implementation might prove more reliable than continuing to extend the witness-analysis machinery.

## Scope

One read-only Codex gpt-6.1-sol helper `/root/l835_saved_acceptance`; saved patch against b24422282, verified against candidate hashes, not live dirty implementation. No installation, repair, further reviewer or owner launch. Verdict pending; L835 OPEN. Existing dirty work preserved. This is a bounded review continuation, not a full boot/Standard closeout.

## Independent verdict — NOT ACCEPTED

Reviewer `/root/l835_saved_acceptance`, explicitly selected gpt-6.1-sol. The saved candidate fixes the reproduced silent-pass defect but unnecessarily blocks closeout for a genuinely excluded directory, violating requirement 4. Review stopped immediately on confirmation through the actual consumer.

### HIGH — unrelated embedded double-star blocks excluded-directory closeout

Saved `argus_contract.py:237–240` treats every earlier non-EXCLUDED pattern with an embedded `**` as potentially overlapping, regardless of its fixed prefix:

```python
earlier_cls != 'EXCLUDED' and (
    any('**' in segment and segment != '**' for segment in earlier.split('/'))
    or _ignore_witness(sc, earlier, parent) is not None)
```

Independent counterexample:

```python
rules = [
    ('other/a**/target', 'OWNED', 'unrelated crossing wildcard'),
    ('root/**', 'EXCLUDED', 'whole excluded subtree'),
    ('PROME/**', 'OWNED', 'delivery'),
]
```

Every path below root/ is EXCLUDED: the earlier fixed prefix other/ cannot match root/. Executed results:

```text
classify(root/a/b/target)                    EXCLUDED
_ignore_witness(other/a**/target, root)      None
_wholly_excluded(root)                      False
never_advisory(root/.gitignore)             True
```

Actual closeout consumer in a real disposable Git repository, with pinned rules, recorded baseline and frozen ordinary PROME/result delivery:

```text
Before ignore-file arrival: sc.verify_review() rc 0
  contract unchanged; verdict FROZEN; delivery working tree;
  snapshot working tree; 1 inventory paths retained
After root/.gitignore = "*.csv\n": sc.verify_review() rc 1
  UNCLASSIFIED: root/.gitignore (new or changed observed version)
```

The failing working-tree run has only that error. A separate `verify_review(ref=HEAD)` invocation also flagged the ignore file but included delivery/ref mismatch diagnostics; it is not needed to establish this finding. No claim that the FROZEN control was independently reviewed: rc 0 here establishes unchanged inventory, not final Standard acceptance.

Resolution shape, NOT a commissioned repair: distinguish provably disjoint rules from uncertain overlap while retaining no-false-advisory protection. Declared conservatism cannot waive the user's excluded-directory requirement. The helper docstring says wholly excluded research/inbound-only subtrees stay advisory without stating this limitation. The candidate report discloses it, but disclosure does not satisfy requirement 4.

## Identity and reproduction evidence

Read charter first, root rules, completion/runtime references, acceptance history, prior receipts and all four recovered reviewer texts. Reconstructed saved patch against b24422282 in `/tmp/l835-accept-l52wdlzu`:

```bash
git archive b24422282 PROME/tools
# Extract into disposable directory, then run there:
git apply /home/willi/Research-workspace/PROME/reports/2026-11-04_L835-bounded-correction.patch
```

Initial `git apply --directory=/tmp/...` was refused (invalid absolute path); no application occurred. Applying from inside the disposable directory succeeded. Added baseline `PROME/state/AUDIT_PERIMETER.tsv` to that overlay for test import. Used PYTHONDONTWRITEBYTECODE=1. All three candidate hashes matched:

```text
dfdbc099cde2e433806d835e331d9d49890ea5af7a3bfe7aedb4b2c746051299  argus_contract.py
09199e67d551d7616edc6bbd4c438f334216dc712300dbefade318b088ae4026  test_argus_contract.py
8c17013617076a133e3409a8e8536aac66c4a027da2daefb71a511704af1dd48  ARGUS_CONTRACT.md
```

Latest failure, with root/a**/target OWNED before root/** EXCLUDED, parent root/a/b: target class OWNED; pre-correction guard False; candidate guard True. Pre-correction code loaded read-only from preserved live dirty source; candidate code exclusively from hash-verified overlay.

Five targeted regressions passed (0.165 s):

```text
test_l835_first_match_exclusion_does_not_hide_alternative_owned_witness
test_l835_later_broad_exclusion_does_not_override_earlier_owned_rule
test_l835_deeper_unattributed_descendant_stays_guarded
test_l835_embedded_double_star_cannot_prove_subtree_excluded
test_l835_prior_full_exclusion_still_wins_over_embedded_double_star
```

These cover the three completed recovered counterexamples, embedded prefix/suffix/infix variants for OWNED and SHARED with ignore/attributes names, and earlier-whole-exclusion precedence. The fourth recovered review was incomplete, with no confirmed additional counterexample.

Consumer reproduction used candidate ContractFixture only for disposable repository setup/cleanup:

```python
f = ContractFixture()
f.setUp()
try:
    f.write(sc.PERIMETER_FILE,
            'pattern\tclass\treason\n'
            + ''.join('\t'.join(r) + '\n' for r in rules))
    f.commit(sc.PERIMETER_FILE)
    f.base = f.git('rev-parse', 'HEAD')
    sc.record_baseline(f.base)
    f.freeze()
    print(sc.verify_review())  # rc 0
    f.write('root/.gitignore', '*.csv\n')
    print(sc.verify_review())  # rc 1, solely UNCLASSIFIED root/.gitignore
finally:
    f.doCleanups()
```

## Stop limits

Stopped on the blocker. Further overlapping-rule/first-match exploration for new false negatives, full contract/neighbour suites, fresh consumer integrations for each historical counterexample, and a complete committed/ref/snapshot matrix were NOT performed. These are uncompleted review requirements under the explicit stop rule, not inferred passes. No shared repository edits/Git writes or production installation. Fixture repos cleaned up; temporary candidate overlay remains.

## Closeout and PROME disposition

PROME consumed NOT ACCEPTED and requested closeout through collaboration.followup_task: “NOT ACCEPTED consumed; blocking consumer reproduction accepted as evidence. Incremental corrections paused, no repair/redesign/additional review. Please close out now and confirm no shared edits/Git writes, no outstanding processes and no further work. Return explicit receipt.”

Actual reply: “Closeout receipt: read-only acceptance review complete; NOT ACCEPTED delivered and consumed. No shared files edited, no shared Git writes, and no outstanding processes. No repair, redesign, additional review, or further work performed or planned.”

L835 remains OPEN / NOT ACCEPTED / NOT INSTALLED. Incremental corrections PAUSED on the user's stated failure branch. No installation recommendation. Reconsideration should compare a simpler conservative design against both safety and excluded-directory nonblocking requirements before any further code work; no design or implementation commission is created here. Previously accepted WQ-594–596 and L910 unchanged. This review-only continuation does not claim full boot, Standard ARGUS closeout or unrelated owner completion.
