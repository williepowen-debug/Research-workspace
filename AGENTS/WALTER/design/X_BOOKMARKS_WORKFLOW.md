# Bookmark review and completion — current operator procedure

Owner: WALTER. Behavior/authority canon: X_BOOKMARKS_ACCEPTANCE.md §10, Will-directed2026-10-19. Existing WQ458 continuation decision, read-only scopes, per-invocation request limit and human-watched execution remain unchanged. Implementation approval is not pilot renewal.

## Will's part

Bookmark posts and article links normally. WALTER can follow accessible links and inspect attached screenshots; a paywall does not make the whole bookmark unusable. If consequential content remains inaccessible, WALTER identifies the specific article/table/clip and explains why it matters. Supply a screenshot/text if convenient; no need to do this for every saved article.

For urgency, send the link directly in the WALTER conversation with the urgency stated. For reconsideration, send the link with “look again.” Re-bookmarking an already-processed ID does not requeue it. Processing happens in an authorized human-watched WALTER session, not continuously.

## WALTER's part

1. Run the normal scan from the repository root only when the pilot/run is authorized. The tool prints posts and media/link pointers, stages exactly those IDs, and reports whether it resumed old pages or left older coverage incomplete. Fetched does not mean read.
2. Execute the existing §9/§9a retrieval and filtering workflow. Read plausible source bodies/media before disposition; preserve distinctions among full source, partial source, and unread source. Full content is not certified merely by a download/link expansion. “fully_read” describes the material actually needed for this item, including consequential attached/linked content; it is WALTER's attestation.
3. Write normal BOARD/disposition/follow-up artifacts before consuming. Create the review template with the command below, then fill every staged ID. No copied post/article bodies: just disposition, reading label, an optional repository-relative follow-up artifact and an optional concise WALTER-written missing-content request. Link important findings to their BOARD/home artifacts. For material partial/unread DISPATCH/FOLD, supply an existing follow-up artifact or a selective request; keep reading gaps visible after intake disposition.
4. Mark using the completed review. New stages refuse an absent, unfilled, duplicate, incomplete or mismatched review. The tool never re-fetches while marking. Legacy stages can still be marked with reading status explicitly unrecorded.
5. Give Will a short receipt in the current authorized conversation: last head check; items reviewed; material findings by reference; duplicates/folds; partially read/unread items and selected requests; incomplete/resumed coverage. The tool-generated receipt supports this message but does not send it, certify factual claims or establish recipient consumption. Match actual runtime/channel permissions. Authorization-only activity says no bookmark scan performed.

Commands (repository root; the JSON review is filled by WALTER, not Will):

    .venv/bin/python3 AGENTS/WALTER/tools/x_bookmarks_scan.py
    .venv/bin/python3 AGENTS/WALTER/tools/x_bookmarks_scan.py --review-template AGENTS/WALTER/research/<session>/bookmark-review.json
    .venv/bin/python3 AGENTS/WALTER/tools/x_bookmarks_scan.py --mark --review AGENTS/WALTER/research/<session>/bookmark-review.json
    .venv/bin/python3 AGENTS/WALTER/tools/x_bookmarks_scan.py --receipt

Template creation is create-only. Choose a fresh path for each scan, including repeat scans of the same IDs; the timestamp binds the review to its stage. Review files contain schema/staged_at/items, each item with id/disposition/read_state/follow_up/ask_user. Dispositions use the existing DISPATCH/FOLD/DUP/NOTE/KILL/NO-ACTION tokens; read_state uses fully_read/partly_read/unread. Optional fields are null unless needed. An ask_user request states the missing content and why it matters. Receipt timestamps measure scan/mark events, not when Will saved the bookmark or hands-on research time.

## Continuation and recovery

The request budget stays10bookmark-read attempts/invocation,50rows/page. Refresh failures, rate limits and network errors do not mark IDs. A401retry consumes a read-attempt slot and retries the same page, avoiding cursor loss. OAuth refresh itself is separate from the bookmark-read budget.

A partial traversal retains its original seen baseline and opaque page cursor. Newly marked IDs cannot terminate that traversal early. The cursor proposal is bound to staged IDs and committed after their mark. Interrupted mark retries are idempotent. Zero-new-ID segments can advance immediately because no new content needs disposition.

Opaque pagination state/proposals are local ignored *_token.json sidecars beside the seen ledger. The committed seen ledger adds only a boolean scan_complete guard. If local state is missing after incomplete coverage, safely restart from the head and ignore all-seen prefixes. A rejected cursor produces a loud failure and prepares a conservative restart for the next human-watched invocation. Corrupt state fails closed. The first upgraded traversal also audits to the end instead of trusting a potentially truncated legacy prefix; it may return0newIDs while older coverage remains incomplete.

A resumed traversal does not inspect the newest head that run. Its receipt says so; a subsequent authorized head scan checks later additions. Upstream changes/removals can affect opaque pagination, so these receipts do not promise a consistent snapshot of a changing remote collection. Do not label a resumed tail or failed/capped scan “all caught up.” X's documented pagination uses the returned next_token as pagination_token: https://docs.x.com/xdks/python/pagination . Live cursor lifetime/behavior is not certified by offline fixtures.

No raw source bodies or credentials enter state/review receipts automatically. Seen/stage isolation, unchanged scopes and a real live run remain separate verification questions. The repair is implemented/tested only to the scope recorded in the dated repair result; independent review and live confirmation are reported explicitly.
