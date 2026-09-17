# Crash recovery — original history and unfinished work preserved

## Assignment and scope

Will reported a crash and authorized the proposed preservation and Git recovery before restarting agents. Initial branch: `master`; unreadable HEAD: `5b7b3fde4531403bf27aa3658d66077d9927cc08`. GitHub's actual master, checked with `git ls-remote`, was `45d7072167caed080d90bc3e17066b23f373c838`, matching the cached remote ref. No pull, reset, stash, research rewrite, fleet launch, or owner-message send was performed. This is CATO's implementation and author verification, not an independent review of the underlying research.

Recovery required a verified full backup, reconstruction in an isolated copy, exact object-hash matches, a passing full integrity check, preservation of live working files/index/refs, and a record of unfinished owner work. The available process view was sandbox-limited, so it did not establish that every other session was stopped. Before installation, every regular file was compared with the snapshot, file additions/removals were checked, symlink targets were checked, and Git lock files were acquired for the index, HEAD and master ref. No concurrent content change was detected.

## Findings and repairs

**High — Git corruption blocked normal operations.** Twenty-three loose object files were zero bytes, including HEAD, five index-referenced blobs and trees. Both HEAD and master reflogs ended in zero-filled data. `git status` and HEAD-relative staged inspection failed with `bad object HEAD`; initial `git fsck --full` exited 11. This was more than merely uncommitted work.

**All 23 original objects were restored exactly.** In an isolated candidate, empty objects were quarantined. Five working files hashed to the exact missing blob IDs. Rebuilding trees from the preserved index restored 14 further objects. Building the original path-scoped OSPREY commit tree restored three more trees. The remaining commit was reconstructed using its verified tree, remote parent, preserved COMMIT_EDITMSG, author identity and a bounded timestamp search. Its SHA-1 exactly matched the original HEAD: `5b7b3fde4531403bf27aa3658d66077d9927cc08`. This is restoration of the original bytes, not a replacement commit or inferred substitute history.

Restored commit: `OSPREY -> HAWK: provide report commit receipt and pin synthesis brief`, original timestamp September 16, 16:55:21 EDT. It contains six file changes, including the consumed coordination-packet rename. OSPREY's work is committed; it is not part of the remaining staged work.

The live repair replaced only those 23 object files and the two damaged reflog tails. Valid reflog prefixes were retained; replacement entries explicitly say they are reconstructed recovery entries. Original corrupted bytes remain in the backup. The branch refs, HEAD pointer and index were left unchanged. No history amendment or branch reset was needed.

## Backup and evidence

- Durable local backup: `/home/willi/research-recovery/20260917T011757Z/snapshot/` — full workspace, including `.git`, ignored files and untracked work. This is outside the repository, on the same machine; it is not an off-machine backup.
- SHA-256 inventory: `/home/willi/research-recovery/20260917T011757Z/snapshot-manifest.json` — 31,146 regular files verified against the original snapshot; symlinks copied as links.
- Installation receipt: `/home/willi/research-recovery/20260917T011757Z/installation-receipt.json`.
- Isolated candidate, working logs and recovery inventory: `/tmp/research-recovery-20260917T011757Z/`.
- Installation script: `/tmp/cato-install-git-recovery.py`; its writes required sandbox escalation because `.git` is protected and the durable backup lies outside the writable workspace.

Before CATO wrote this report, all 28,090 non-Git regular files still matched the snapshot and `.git/index` was byte-identical. This establishes preservation of surviving disk content; it does not establish that unsaved editor buffers, lost session context, or intended-but-never-written work survived.

## Remaining owner work

The restored status contains 24 unstaged modified files, six staged change records (one rename and five additions), and 12 untracked files. One HAWK report is both staged and further modified; do not flatten those two versions accidentally.

| Owner / location | Preserved unfinished work | Resume recommendation |
|---|---|---|
| BRENT | Nine unstaged files; untracked cross-war oil REPORT/VALIDATION and an incoming HAWK synthesis packet | Reconcile the existing oil review against current state, then complete its own authorized work. |
| CARL | Three unstaged state files; staged Axis A source archival rename; three untracked before-images and a closeout receipt | Validate the interrupted archival/closeout work, preserving the before-images. |
| HAWK | Twelve unstaged files; five staged additions including a report with later unstaged edits; untracked outgoing packets at BRENT, WALTER and PROME | Compare staged and working report versions; validate synthesis and exact self-authored packet paths before committing. |
| OSPREY | Original six-file commit restored; no remaining dirty OSPREY paths in this snapshot | Read the recovered receipt if resuming; no reconstruction task established. |
| PROME / WALTER | HAWK-authored incoming packets; three PROME L392 preclose JSON snapshots | Preserve for owner consumption/reconciliation; an untracked packet is not confirmed delivered. |

Exact staged records retained:

```text
R100 AGENTS/CARL/domain/sources/2026-07-10_axisA_consumer_to_bdc_readthrough.md -> AGENTS/CARL/archive/2026-09-16_closeout/2026-07-10_axisA_consumer_to_bdc_readthrough.md
A AGENTS/HAWK/archive/2026-09-16_before-cross-war-review_NEXUS_BRIEF.md
A AGENTS/HAWK/archive/2026-09-16_before-cross-war-review_SCRATCH.md
A AGENTS/HAWK/archive/2026-09-16_before-cross-war-review_STATUS.md
A AGENTS/HAWK/domain/sources/2026-09-16_cross-war-route-source.md
A AGENTS/HAWK/research/2026-09-16_cross-war-oil-review.md
```

## Verification and closeout

- Isolated candidate: `git fsck --full --no-dangling` exited 0 with no output; status, staged diff and original commit inspection succeeded.
- Live installation: all 23 restored object hashes verified; original refs/index preserved; working-file hashes verified as above. `git fsck --full --no-dangling` exited 0 with no output on the live repository as well.
- Closeout checks: orphan advisory identified only the preserved other-owner work; weekday claim check passed on all three required existing PROME surfaces; CATO diff whitespace check passed. The foreign staged changes are deliberately preserved and excluded through exact-path commit mechanics.
- Research correctness and owner completion were not assessed. No owner changes were swept into a CATO commit. CATO's only authored repository documents are this report and CONTINUITY.
- The root closeout protocol requires an exact-path report commit and safe-push receipt. That push will also carry the already-committed recovered OSPREY change; it must not include the surviving staged/unstaged owner work. Final commit and fresh-fetch push confirmation are delivered in-session.

Next: after recovery verification, Will can resume HAWK, BRENT and CARL individually for reconciliation. Their recovery brief should say: preserve surviving edits and staging; do not pull while other owners' files are dirty; read this report; finish/review only the previously authorized work; commit exact owned paths. No agent has been restarted or assigned that work by CATO. CATO's next session should orient and await Will.
