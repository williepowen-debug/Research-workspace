# Independent falsification rc/help review — 2026-11-04

Reader: `/root/owner_followthrough`, Codex/OpenAI, exact model variant UNKNOWN. Separate parent-requested review after owner follow-through; no code/test/owner edits and no commits/push. Parent authored the patch. Read acceptance record, actual diff, CLI tests whole, scanner header1–65, groups/classes208–255, main448–584 (initial combined truncation recovered454–508), CHECK_STANDARD§3/§9 and actual CHECKS producer row; UPGRADE_PROTOCOL4/4a/4b supplied in inherited parent read. Detection helpers unchanged and not reread whole. Scope is existing omitted market/no-visible-rail finding rc, CLI usage/refusal, and TSV comment only.

## Round 1: HOLD on new empty-name regression

Own counterexample, derived independently of author's test list: an explicitly supplied empty agent name must not mean 'no selection' and silently expand to the whole fleet. This is plausible when a shell variable is unset: `--agent "$desk"`. Tested both separated empty value and `--agent=`. Current patch `if only:` skips validation for empty strings and scans46 directory agents/41 surfaces; original explicit `--agent` branch rejects empty name rc2. New source returns fleet rc1. This violates acceptance3's invalid-agent refusal and materially changes selected scope.

Smallest remedy: distinguish None (flag omitted) from an empty provided value before validation; no new scope or checker. Tests should include both explicit empty forms. No code modified by this reader.

Other independent results: all11 regression tests pass; real BROCK before0→after1; lowercase brock still names BROCK; DAEDALUS TSV returns0 with empty market candidate comment and named nonmarket bucket. Old/new fleet TSV surface data rows are byte-identical (42 lines including header); only intended comment/output/rc change observed. Both sources executed under identical __file__/repo binding to avoid temporary-path root drift.

Consumer survey: `git grep -n -E 'falsification_scan(\.py)?' -- '*.py' '*.sh'` found producer, existing STATUS-rail test, and two pipeline_rc_guard recognition regexes. New untracked CLI test separately read. No tracked executable rc-keyed consumer was found; scanner invocation remains FALSIFICATION_SWEEP step5, which requires judgment reading flags. This survey covers tracked Python/shell callers, not every external scheduler or untracked script. No consumer migration established as needed.

CHECK_STANDARD9 says 0 clean/1 findings/2 cannot-certify; current old groups() loader can still exit1 on missing/empty directory and missing FLEET_MAP silently yields empty classes. These are explicitly excluded existing debts in the parent acceptance record, not fixed here and not grounds for claiming universal cannot-certify correctness. The bounded patch can be accepted after its introduced empty-name regression is fixed. rc0 still cannot establish full rail visibility or real market truth.

Round1 hash provenance correction: **UNKNOWN**. The original round1 source/test snapshots were not retained; the first table was calculated after the parent had already applied the fix, so it incorrectly repeated round2 hashes. Those hashes cannot identify the failing revision. The observed round1 source diff, empty-agent failure and raw probes below remain evidence of the tested behavior; no exact-byte round1 identity is claimed. Final accepted round2 hashes below are unchanged and were rechecked after the fix.

| Path | Round1 SHA256 |
|---|---|
| `AGENTS/DAEDALUS/scripts/falsification_scan.py` | UNKNOWN — captured after fix; original byte snapshot not retained |
| `AGENTS/DAEDALUS/scripts/tests/test_falsification_cli.py` | UNKNOWN — captured after fix; original byte snapshot not retained |

Raw independent old/new evidence:

```json
{
  "old['--agent', '']": {
    "rc": 2,
    "first": [
      "\ud83d\udd34 falsification_scan CANNOT-CERTIFY: agent '' not in FLEET_DIRECTORY \u2014 0 surfaces scanned (a typo here previously produced a clean-looking zero report)"
    ]
  },
  "old['--tsv']": {
    "rc": 1,
    "first": [
      "Agent\tGroup\tSurface\tClass\tVerdict\tStamp\tLiveRef\tAgeDays\tCitedVer\tLiveVer\tWhy",
      "CORAL\tACTIVE\tthesis/CHANGELOG.md\tchangelog/pivot log\tSTALE-FLAGGED\t2026-09-28\t2026-10-29\t31\t-\tv1.1\tstamp 2026-09-28 is 31d behind live ref 2026-10-29 (threshold 21d) \u2014 vintage = NEWEST ENTRY (append-only surface) \u2014 \u26a0 header also carries 2026-11-04, 37d newer than its own stamp: check which one describes the surface",
      "FALCON\tACTIVE\tworkbook/EXIT_PROTOCOL.md\tthesis/validation\tSTALE-FLAGGED\t2026-10-01\t2026-10-30\t29\t-\tv3.0\tstamp 2026-10-01 is 29d behind live ref 2026-10-30 (threshold 21d) \u2014 \u26a0 header also carries 2026-10-26, 25d newer than its own stamp: check which one describes the surface"
    ]
  },
  "old['--agent', 'BROCK']": {
    "rc": 0,
    "first": [
      "# Falsification Freshness Sweep \u2014 detection layer \u00b7 run 2026-11-04 \u00b7 in-content stamps only",
      "",
      "**Searched:** 0 falsification surfaces across 0 agents (of 46 in FLEET_DIRECTORY) \u00b7 threshold 21d behind live STATUS/thesis ref"
    ]
  },
  "new['--agent', '']": {
    "rc": 1,
    "first": [
      "# Falsification Freshness Sweep \u2014 detection layer \u00b7 run 2026-11-04 \u00b7 in-content stamps only",
      "",
      "**Searched:** 41 falsification surfaces across 29 agents (of 46 in FLEET_DIRECTORY) \u00b7 threshold 21d behind live STATUS/thesis ref"
    ]
  },
  "new['--tsv']": {
    "rc": 1,
    "first": [
      "Agent\tGroup\tSurface\tClass\tVerdict\tStamp\tLiveRef\tAgeDays\tCitedVer\tLiveVer\tWhy",
      "CORAL\tACTIVE\tthesis/CHANGELOG.md\tchangelog/pivot log\tSTALE-FLAGGED\t2026-09-28\t2026-10-29\t31\t-\tv1.1\tstamp 2026-09-28 is 31d behind live ref 2026-10-29 (threshold 21d) \u2014 vintage = NEWEST ENTRY (append-only surface) \u2014 \u26a0 header also carries 2026-11-04, 37d newer than its own stamp: check which one describes the surface",
      "FALCON\tACTIVE\tworkbook/EXIT_PROTOCOL.md\tthesis/validation\tSTALE-FLAGGED\t2026-10-01\t2026-10-30\t29\t-\tv3.0\tstamp 2026-10-01 is 29d behind live ref 2026-10-30 (threshold 21d) \u2014 \u26a0 header also carries 2026-10-26, 25d newer than its own stamp: check which one describes the surface"
    ]
  },
  "new['--agent', 'BROCK']": {
    "rc": 1,
    "first": [
      "# Falsification Freshness Sweep \u2014 detection layer \u00b7 run 2026-11-04 \u00b7 in-content stamps only",
      "",
      "**Searched:** 0 falsification surfaces across 0 agents (of 46 in FLEET_DIRECTORY) \u00b7 threshold 21d behind live STATUS/thesis ref"
    ]
  },
  "data_rows_equal": true,
  "data_rows_with_header": 42
}
```

REVIEW: required — scope named scanner main/CLI and CLI regression tests; reader /root/owner_followthrough; disposition HOLD1 (explicit empty agent broadens scope), other bounded acceptance legs PASS. Parent fix after this read is POST-REVIEW until independently rechecked.

## Round 2: ACCEPT bounded patch after independent recheck

Parent's POST-REVIEW fix changes the validation condition to `if only is not None:` and adds both empty-string CLI spellings to invalid-argument tests. Full diff reread: no other producer behavior change since round1. Both empty forms and a whitespace-only unknown name now return2 before scanning. Lowercase brock+TSV still returns1 with the named candidate, DAEDALUS returns0, and help prints usage without scanning. All11 tests rerun PASS, including the negative directory-loader help test and six pre-existing STATUS-rail tests.

The full final source/test hashes below bind this acceptance. The one-line validation change cannot alter valid fleet/no-selection data traversal; round1 fleet data-row conservation remains valid for that path. Existing class-map/loading/rail-heuristic limitations remain outside acceptance and explicitly open. No guard scope/threshold/freshness/owner judgment change authorized or inferred.

| Final accepted path | SHA256 |
|---|---|
| `AGENTS/DAEDALUS/scripts/falsification_scan.py` | `b15d52f8b10895794bcfb86ed0dc3decc312b21e917e01e2c993069237c49a42` |
| `AGENTS/DAEDALUS/scripts/tests/test_falsification_cli.py` | `9faf08cf5bc81a11bfcc61401761b1d3d01e8fae0abc9328b7d5b2c8dbd9a40e` |

Round2 actual probes:

```json
{
  "['--agent', '']": {
    "rc": 2,
    "scanned": false,
    "empty_refusal": true,
    "market_candidate": false,
    "usage": false
  },
  "['--agent=']": {
    "rc": 2,
    "scanned": false,
    "empty_refusal": true,
    "market_candidate": false,
    "usage": false
  },
  "['--agent', ' ']": {
    "rc": 2,
    "scanned": false,
    "empty_refusal": false,
    "market_candidate": false,
    "usage": false
  },
  "['--agent', 'brock', '--tsv']": {
    "rc": 1,
    "scanned": false,
    "empty_refusal": false,
    "market_candidate": true,
    "usage": false
  },
  "['--agent', 'DAEDALUS']": {
    "rc": 0,
    "scanned": true,
    "empty_refusal": false,
    "market_candidate": false,
    "usage": false
  },
  "['--help']": {
    "rc": 0,
    "scanned": false,
    "empty_refusal": false,
    "market_candidate": false,
    "usage": true
  }
}
```

REVIEW: required — existing market-candidate rc inclusion, main/argparse validation/help and TSV perimeter comment; scope source diff/header/main plus CLI tests whole and STATUS-rail regression suite; reader /root/owner_followthrough; disposition ACCEPT at final hashes, initial HOLD1 repaired and rechecked, RESIDUE existing missing-map/directory/error/heuristic limitations. Any later code/test edits are POST-REVIEW and outside these hashes.

## COMPLETION — independent patch reader — 2026-11-04
STATUS: ✅ DONE
CHANGED: runs/2026-11-04_CATCHUP_FALSIFICATION_REVIEW.md
RESULT: Found1 introduced empty-agent scope regression; parent fixed it and independent recheck accepts final hashes. Eleven tests PASS; named defective and clean population cases both observed.
GAPS: Existing missing-map/loader/error and rail-detection limitations remain outside this repair; no whole-checker clearance.
WILL_NEEDS: None.
FOLLOW-UP: Parent may publish the exact accepted source/test revisions with retained caveats. Reader has stopped; no owner edits, commits, launches or running processes.
