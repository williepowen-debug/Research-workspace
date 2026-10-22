# Explicit delivery contract (ARGUS schema 2)

Use this workflow for concurrent closeouts after the October19 repair acceptance. `argus_scope.py --record-review` without `--contract` retains the legacy strict behavior; it does not silently migrate or downgrade an existing review. Receipt exclusions and the legacy consumed-move workflow are unchanged. A new schema2 closeout classifies its PENDING observed inventory (any porcelain state, untracked included) and its own OWNED-lane paths; **committed-only paths outside PROME's OWNED lane are attributed by their own commits and need no `observed` entry (WQ-485 A, Will 2026-10-22 12:10 ET; recorded in the manifest as `attributed_by_commit`; acceptance `PROME/tools/tests/ACCEPTANCE_argus_contract_wq485_2026-10-22.md`). Before 10/22 every committed path since the baseline needed a classification (307 paths, four freeze iterations on 10/22);** outside that exemption, path ownership and commit subjects remain reading hints, never proof of delivery or non-reliance; inside it, a `PROME` commit subject or a from-PROME filename REMOVES the exemption (PROME must deliver or observe such a path), it never grants one.

Prepare a JSON plan outside the repository, or include that plan itself in delivery. Its shape is:

```json
{
  "delivered": {"PROME/report.md": "Authored in this session; exact task/provenance"},
  "evidence": [{"path": "AGENTS/OWNER/report.md", "commit": "persisted commit SHA",
    "mode": "historical", "claims": {"PROME/report.md": "Dated owner result being consumed"}}],
  "observed": {"AGENTS/OTHER/pending.md": {"owner": "OTHER", "not_relied_on": true,
    "reason": "Actual contribution provenance and why no delivered claim relies on this version",
    "basis": {"path": "AGENTS/OTHER/receipt.md", "commit": "persisted commit SHA"},
    "quote": "Exact attribution passage from that receipt"}}
}
```

Delivery includes all claimed changes since the recorded baseline, including earlier commits, pending edits, deletions and nested/shared paths. Evidence requires a persisted version; `historical` pins that version, while `current` additionally requires matching current/delivered bytes. Both roles may apply to a delivered file. A changed live version of historical evidence needs its own unrelated-version classification; the pinned claim remains unchanged. Uncommitted evidence actually needed by a claim remains a real blocker. Never commit another owner's work merely to clear it.

From repo root:

```sh
python3 PROME/tools/argus_scope.py --record-review --contract /tmp/prome-delivery-plan.json
```

Review the frozen contract and classifications, then run `--mark-reviewed "actual reviewer receipt"`. Promotion, the normal gate and post-commit verification use the same contract. The immutable contract digest binds delivered bytes, earlier versions and dependencies. Observed attribution remains an accountable human judgment, not automated authorship authentication.

If proven unrelated work arrives or changes, supply only its attributed classifications in a JSON mapping and run `--observe /tmp/prome-observed.json`. This appends captured versions and leaves the contract/review intact. No blanket exclusions; ambiguous arrivals fail. New delivery or relied-on evidence requires re-freeze and changed-portion review. Do not use observation to remove a delivered/current-evidence obligation.

After the exact-path commit, resolve and save its full SHA as A, then run `--verify-review --ref <A> --paths <exact commit paths>`. The verifier also checks actual commit paths, the complete delivery set and full inventory; an omitted/truncated list does not hide an added path. Never pass an empty list. Run the ordinary closeout gate and existing safe-push procedure; no new Git wrapper is installed here.

If HEAD advances to P before push, retain A as the reviewed delivery and check `--verify-review --ref <A> --snapshot <P>`. Unrelated carried changes need classification; `--observe ... --observe-at <P>` supports a fetched snapshot absent from local HEAD. After safe-push, fresh-fetch and record the actual full remote SHA R, establish A's ancestry, and repeat the snapshot comparison at R. Ancestry alone proves inclusion, not unchanged current artifacts. Relevant changes withhold current/publication certification while A remains historical. Never claim unrelated carried content was reviewed, or certify changes after R. Advance the existing baseline only through successful closeout delivery, not to hide a failed comparison.

Acceptance and independent review: `PROME/tools/tests/ACCEPTANCE_closeout_boundaries_2026-10-19.md`. WQ448 remains a separate pending push-enforcement proposal; Deck A remains paused.
