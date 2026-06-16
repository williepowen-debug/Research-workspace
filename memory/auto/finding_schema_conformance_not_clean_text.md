---
name: finding_schema_conformance_not_clean_text
description: "structural/numerical self-verify never reads rendered prose; add a literal read-through — and verify the artifact, not a transcription of it"
metadata: 
  node_type: memory
  type: finding
  originSessionId: da2f725b-3684-405c-ad5b-d32bed195a74
---

A structural self-verify checklist (schema sections present · parity vs exemplar · no-drift numbers · scope · pin-present) can pass a file that still contains a garble, template remnant, or merge artifact — **none of those checks read the rendered prose.** Add a 6th check: a literal line-by-line read-through of the rendered text (especially load-bearing lines a consumer *parses*, like a NEXUS-brief `As of:`/pin header).

**Why:** schema-conformance ≠ clean text. A line can be structurally valid and still be corrupt.

**How to apply:** on any consumer-parsed artifact (NEXUS_BRIEF, schema'd TSV row, machine-read header), end the self-verify with a rendered read-through before commit. Now wired into CARL closeout step 14b.

**Inversion caught Jun 16 2026 (the sharper lesson):** the garble can also live in the *reader's quote* of a clean file, not the file. ORC reported a line-8 pin garble (`7182547e`t mark positions.`) — it was line 7's tail conflated onto line 8 *in the paste ORC read*; the committed file was clean. CARL declined to "fix" it and read the real artifact instead, per [[feedback_verify_existence_external_primaries]]. So: **verify the artifact directly, never a transcription of it** — your own (or a peer's) output is error-prone input. Pairs with [[finding_cross_surface_validation_pattern]] and [[finding_circular_corroboration_via_state_file]].
