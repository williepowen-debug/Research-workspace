# PROME/SAM presence and file activity

Owner: PROME · Date: 2026-09-09

Will approved adding file activity and then completing session identification.
Scope and review contract: [plan](../plans/2026-09-09_presence-activity.md).

The presence view now shows pending files and the most recent desk-named commit
for each due owner, with `--desk SAM` including SAM even without a due row. Optional
local snapshots compare content/status across observations without using mtime as
proof of freshness. First observation is a baseline; unchanged dirty files do not
become fresh activity on every poll. File location does not identify its writer.

VERIFIED identity evidence: this caller exposes CODEX_THREAD_ID
`01a087c0-e34c-7e20-a64a-e54cafb7d13f`, which matches exact PROME cwd metadata in
the local Codex store. Helper records retain parent links and separate IDs.
SEARCH-NOT-FOUND: no exact SAM cwd record in the default Linux store during the
diagnostic, including an elevated host read; default Windows store path absent.
Broad home/repository-root records were not assigned to SAM by guesswork.

The optional store adapter uses read-only SQLite and an explicit field allowlist;
no titles, prompts, transcripts or credentials are queried. Stored records supply
identity candidates, never live working/idle status. The supported runtime route
remains loaded-thread metadata and status events from a usable App Server endpoint;
that endpoint is still unresolved here. [Official OpenAI documentation](https://learn.chatgpt.com/docs/app-server).

## Validation

New activity/identity fixtures initially passed all 11 cases: first/repeated/changed
observations including restored mtime; dirty/new/ignored/renamed/deleted paths;
foreign-authored commit/body-label filtering; corrupt/foreign/future/locked baseline;
large/symlink/special/sensitive-path exclusion; no writes inside the repo from
comparison snapshots; exact identities, multiple candidates, helpers, missing/schema
failure and a SAM overview even with runtime UNKNOWN and no due row.

Final validation: 12 activity/identity tests, 11 existing boot tests and 35 existing
session tests passed (58 total). Independent PLAN found no blocking issue. RESULT
found one failure-path defect: a failed file enumeration could look like a changed
self-commit. Corrected once; incomplete capture comparisons now return null/UNKNOWN
and preserve the baseline. The new regression exercises that failure explicitly.

The live trial found pending files and SAM commit `9899e223c`. Successful path
inventories at 2026-09-09T23:15:36Z and the following comparison identified PROME's
caller ID and retained SAM's file evidence, with no new changes among the measured
pending files between those observations. SAM's logs and some large data files
were explicitly unmeasured; they did not erase evidence from measurable files.
The CLI returns an advisory failure when content coverage is incomplete. Saved
PROME/SAM comparison: `2026-09-09_presence-activity-observation.json`.

No advancing boot gate was rerun. The existing closeout DOCKET disposition blocker
remains separate from this implementation; the saved closeout receipt preserves
its actual verdict. GATES, DOCKET, broker truth and market regime were not changed.

## Declared residue

UNKNOWN: SAM's actual session identity and working/idle state. Will's reported
open windows remain operator evidence, not a fabricated runtime reading. No new
session is launched or messaged, and no SAM files are modified by this task.

File hashing reads bounded regular file contents; output stores only hashes and
metadata. Gitignored files are outside coverage, and excluded/large/changing files
are explicitly unmeasured. This is observation on demand, not a daemon. The optional
SQLite schema is an implementation detail and may drift; absence/schema failures
stay UNKNOWN. Existing native spawn preflight and due-day operational blockers are
unchanged. Baseline timestamps and HEAD provenance are retained in comparisons;
the complete old baseline is not archived automatically. Missing parentage stays
UNKNOWN; a null parent does not prove a desk's main session.

RESULT warning (2026-09-09): content fingerprints cover working-tree bytes plus
Git status, not the staged index blob. An index-only content change that leaves
the same status and working-tree bytes is outside this detector's coverage.
