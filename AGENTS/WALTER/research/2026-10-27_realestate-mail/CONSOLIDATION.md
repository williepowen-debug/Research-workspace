# Real estate mailbox consolidation — October 27, 2026

**Result: 965 → 294 emails in Gmail (671 fewer, 69.5%).** This is a reduction in email containers, not a count of valuable signals discovered or rejected.

Will explicitly approved: “Yes—consolidate, then trash the newsletters.” The question specified saving unique article links and notes in a local research index before moving roundup emails to Trash. No new source research, collector, recurring filter, external send or permanent deletion was requested.

## Source preservation before deletion

Private searchable index: `AGENTS/WALTER/debug/realestate-library-2026-10-27/index.html`.
Adjacent `catalog.json` stores the source records and grouped links; `source-backup.zip` preserves all 965 source records, including delivered plain/HTML content where captured, dates, provenance, original URLs and source-text hashes. These files are verified gitignored and remain local. The public repository contains only the reusable consolidation script, aggregate checks and this receipt.

The index supports text search, topic and disposition filters, source-text expansion, original-link variants and CSV link export. Repeated normalized destinations are grouped. For opaque tracking links, an exact headline may group navigation entries, while every dated original link remains available; this does not establish that separate publishers independently confirmed an event. Publisher claims, linked articles, gated reports and podcasts remain unverified unless separately researched. Navigation/ad filtering affects the index display; the source backup retains the delivered text and URLs.

## Gmail changes

| Consolidated newsletter type | Emails moved to Trash |
|---|---:|
| Connect CRE digests | 277 |
| GlobeSt roundups | 220 |
| National Mortgage News digests | 83 |
| Trepp podcast pointers | 50 |
| Commercial Observer issue/interview pointers | 29 |
| CRE Daily podcast pointers | 12 |
| **Total** | **671** |

Remaining 294 emails include substantive analysis/reports and protected records. All three Research Highlights remain in Gmail. Starred/personal/highlighted messages, account records and detected attachments were excluded from consolidation. The current starred/category-personal/highlight queries were checked before mutation. Real Estate and other user labels were retained; only Inbox was removed if present when Trash was added. The messages remain recoverable through Gmail's Trash, which was not emptied.

## Actual verification

- Fresh body/label reads for all 671 selected messages before building the library.
- All 965 records written to the ZIP, CRC checked and restored; restored objects and source-body hashes matched the catalog one for one before Gmail mutation.
- JavaScript compiled and ran in Node's VM with a DOM stub: initial 100-card rendering, multiword search, topic/disposition filters, link view and HTML escaping passed. No automatic external content fetch. A real browser preview was unavailable (Playwright absent), so no visual browser-validation claim.
- Both Gmail modification batches succeeded (500 + 171). Independent paginated Trash search found every one of the 671 exact IDs, zero missing. Total Real Estate-labelled Trash is 854, including the preceding pass's 183 messages.
- Final Gmail label counts: Real Estate 294; Research Highlights three. 965 − 671 = 294.
- BM-20261027-10 closed 965/965 for source-transfer/message-operation accounting. This does not certify article-level novelty or research integration.

Private coverage and mutation proof: `coverage-proof.json`, `mutation-receipts.json`, `trash-verification.json` and `dispositions.tsv` beside the library. No mailbox body/ID dump is staged. Broad boot, lifecycle, prior source gaps and WQ approvals stay in LAST_COMPLETION. The two earlier research cards remain qualified; this pass adds no signal or owner handoff. Routine publication remains coordinated, with foreign shared edits precluding pull/push.
