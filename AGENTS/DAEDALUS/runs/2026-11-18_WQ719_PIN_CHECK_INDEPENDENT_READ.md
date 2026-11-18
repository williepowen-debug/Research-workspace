# Independent read: cd64583eae (`scripts/brief_pin_check.py` STALE-PIN advisory, WQ-719 A), with the fix round

**Assigned:** PROME prome-6e 15:30 ET 11/18 on Will's "go" (15:29 ET, PROME's window). **Reader:** one Opus subagent, diff-only, time-boxed, read-only to the repo, brief written without DAEDALUS's conclusions; it ran its own fixtures under `--root` (in scratch, since cleared). The harness refused the reader's own report file, so the ledger below is its returned text, saved here by DAEDALUS. The verbatim command transcript is in the session record, not in this file.

**Reader verdict: ACCEPT WITH RESIDUE.**

## Ledger (reader's, condensed wording, verdicts unchanged)

| # | Claim or case | Result | Verdict |
|---|---|---|---|
| 1 | selftest 14/14 | PASS, rc 0 | ✅ |
| 2 | STALE-PIN restored to blocking → 3 legs FAIL | 11/14, rc 1 | ✅ |
| 3 | "2 legs added, 2 re-pointed" | matches the diff | ✅ |
| 4 | PIN-UNRESOLVED alone (pin = commit that touched another file) | ⛔, rc 1 | ✅ |
| 5 | PIN-UNRESOLVED alone (pin `deadbee12`, names no commit) | ⛔, rc 1 | ✅ |
| 6 | PIN-UNRESOLVED + STALE-PIN | both lines, rc 1 | ✅ |
| 7 | PIN-UNRESOLVED + unknown desk | rc 1 (outranks rc 2) | ✅ |
| 8 | PIN-UNRESOLVED + STALE-PIN + unknown desk | all lines, rc 1 | ✅ |
| 9 | STALE-PIN + unknown desk | new rc 2; old rc 1 (old masked it) | ✅ real fix |
| 10 | STALE-PIN alone, with and without `--quiet` | ⚠️ line kept, rc 0 | ✅ |
| 11 | `--quiet` never hides a blocking line | ⛔ printed, rc 1 | ✅ |
| 12 | root not a git repo | CANNOT-EVALUATE, rc 2 | ✅ |
| 13 | uncommitted STATUS edit on a stale pin | note added, rc 0 | ✅ |
| 14 | whole fixture population | rc 1, all lines | ✅ |
| 15 | rc-1 summary tag still read `BRIEF-PIN 1 STALE`, although rc 1 now means only PIN-UNRESOLVED; NEXUS digests read that tag as the stale class | false label on a blocking run | ❌ |
| 16 | stale-pin reason said "STATUS was re-committed after the brief fold"; case W (two STATUS commits, then the brief committed on top still pinned to the older one) makes it false | false written claim | ❌ |
| 17 | case W now rc 0 (old rc 1); schema §4.1 at 397f330a33 still says the pin must equal STATUS HEAD when the brief is committed; the script could tell W from normal lag with its existing ancestor test | ruling's words met; schema case passes | ⚠️ NEXUS/Will to rule |
| 18 | routine `git pull --rebase` re-hashes an unpushed STATUS commit → correct pin becomes PIN-UNRESOLVED rc 1, and On_FAIL says fix "at the next brief commit", which may be weeks now | pre-existing case, lasts longer after WQ-719 | ⚠️ |
| 19 | `ADVISORY` set includes CANNOT-EVALUATE (rc 2), same ⚠️ mark as an advisory stale pin | naming only | ⚠️ minor |
| 20 | docstring rc line | behaviour matches; loose wording | ✅ |
| 21 | docstring reason vs schema §4.1/§4.4 | matches | ✅ |
| 22 | CHECKS Detects | matches | ✅ |
| 23 | CHECKS Null_meaning | true; omits git failure = rc 2 and PIN-UNRESOLVED outranking rc 2 | ✅ incomplete |
| 24 | CHECKS live counts (31 briefs, rc 0, FLG + OTTO stale 1 each) | reproduced | ✅ |
| 25 | CHECKS_HISTORY before-images for the 4 changed columns | present | ✅ |
| 26 | CHECKS On_FAIL for STALE-PIN | consistent for true lag; see #17 | ✅ |
| 27 | outside the diff: a named desk with no brief prints ✅ rc 0 and "1 brief(s) checked"; the script reads only `STATUS commit` pin forms though schema §4.4 lists four (CHECKS row discloses the second) | pre-existing | ⚠️ |

Live today: FLG and OTTO are true lag (each brief commit precedes STATUS HEAD), not case W.

## Fix round (❌ only), 2026-11-18 15:34 ET

| # | Fix | Verification |
|---|---|---|
| 15 | rc-1 tag is now `BRIEF-PIN 1 PIN-UNRESOLVED` | new selftest leg "rc-1 tag names PIN-UNRESOLVED, not STALE": PASS; with the old tag restored the leg FAILS (14/15, rc 1). No script in the repo parses the tag (grep `BRIEF-PIN 1` over *.py/*.sh: none). |
| 16 | reason text no longer asserts commit order: "pin X is N STATUS commit(s) behind HEAD Y — advisory (WQ-719 A): re-pin when the brief is next rewritten"; docstring says the order is not inspected | selftest 15/15; live run 15:34 ET rc 0, FLG and OTTO ⚠️ with the new text |

## Residue, declared (not fixed)

- **#17:** whether a brief committed with an already-stale pin should block again. That is NEXUS's (schema owner) or Will's call; routed to PROME.
- **#18:** a rebase-orphaned pin blocks until the desk's next brief commit. It's blocking as ruled; whether the fix instruction needs a sooner trigger goes with #17.
- **#19, #23, #27:** minor wording or pre-existing; next touch of the file.
