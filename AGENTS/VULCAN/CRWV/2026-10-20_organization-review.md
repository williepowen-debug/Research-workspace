# CoreWeave organization review

Observed 2026-10-20T14:57:41-04:00. Will requested a review and recommendations, then asked whether CRWV should maintain KB rows inside its subfolder. Structure, snapshots and KB ownership have not been changed by this review.

## Findings

| Finding | Evidence | Significance |
|---|---|---|
| Exact duplicates | 86 source copies have74 unique contents; four groups contain16 copies,12 redundant,58,645 redundant bytes | Primarily reading clutter and repeated witnesses, not storage pressure |
| Routing overlap | Eight signal-ID families span37 documents; recipient summaries differ | Prefer one full source in the reading path; preserve recipient-specific judgments and provenance |
| Near duplicates | Five DEWEY DDTL correction packets; four compare90–94% character similarity to the VULCAN version | Same underlying correction, not five independent witnesses; do not merge differing instructions blindly |
| Snapshot drift | Original TRADE changed; frozenKB051/076/079 lack later qualifications | Expected for an archive, confusing if read as current |
| Omitted evidence | KB243 existed at capture but its CRWV0.120919 string missed the whole-token company selector | Literal matching does not establish completeness |
| New evidence after capture | KB246/247 added later | Frozen36-row extract cannot be treated as the maintained companyKB |
| Data versions | Three January option screens, minutes apart, have distinct timestamps/content | Sequential observations, not exact duplicates; distinguish selected card inputs from intermediate captures |
| Mixed purposes | Prompts, broad fleet reports, company research, trade preparation and historical cards share the owner-based inventory | Organize the reader’s path by question and document role |
| Primary evidence access | Filings are linked; no PDF/HTML/XML filing bodies in this folder | A filing index is not a source-document archive |

All86 original paths resolved at audit. No broken local Markdown links were found in copied documents under the narrow inline-link check; bare code paths and links inside code blocks were not certified. Current selection/provenance is documented in MANIFEST.json, not a company-completeness guarantee.

## Recommendation on company KB ownership

Yes: a maintained company KB inside CRWV is a sensible eventual home for CoreWeave-specific evidence. Each fact should have one authoritative row. Preserve existing KB-VULCAN IDs and source ownership; relocation must not reset a claim’s source date or confidence.

Company financing, contracts, concentration and delivery facts belong in the company collection. Broad AI financing comparisons and VULCAN channel judgments belong in the desk collection, referencing company rows where needed. LIQUID market grades and TERRY trade decisions remain their records; company rows link to dated owner evidence rather than create competing grades.

Today, workbook/KB.tsv is authoritative and CRWV/archive/extracts/KB.tsv is frozen. A maintained company location would require checking and updating validators, schema readers, boot/closeout checks and direct consumers before relocating rows. The lower-risk interim is a generated current company view of the existing authoritative ledger. Do not create a second manually edited ledger.

## Recommended reading structure

- README: short entry point with preferred current sources, explicit owner links and review date.
- Company facts: one maintained authority or a generated view; source, period, basis and confidence accompany each row.
- Analysis: dated judgments and models, linking facts instead of restating full datasets.
- History and corrections: a compact map of which claims were withdrawn or qualified and what governs now.
- Source catalogue: one preferred reading entry per source/event with topic and document-role tags; retain all origin aliases.
- Archive: preserve the existing frozen capture and sequential raw data, with intermediate trade screens outside the main reading path.

First improve the reading layer and correction map. Physical deduplication of the immutable capture is optional and lower priority; if later authorized, retain all provenance aliases, update hashes/manifests and verify references. This review does not delete or move evidence, implement a KB migration, commission another desk or create an automatic refresh service.
