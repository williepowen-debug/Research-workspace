---
name: finding_triage_summary_compression_inversion
description: A triage/fan-out one-liner can INVERT (not just lose) a nuanced source finding; re-check load-bearing compressed summaries against the source before acting
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c3467da9-d753-4937-bddd-b04d7a80e022
---

When you fan out a triage/classification workflow that compresses each item to a one-line summary, the compression can **invert the meaning** of a nuanced finding — not merely lose detail. RED hit this on a 98-signal inbox drain: the triage one-liner rendered a DEWEY credit decomposition as *"June HY/CCC widening = genuine sector-BROAD, not a composition artifact"* — the **opposite** of DEWEY's actual verdict, *"genuine but CONCENTRATED (AI-equity-driven), not broad."* Broad → bear (transmission firing); concentrated → bull (idiosyncratic noise). The one-liner flipped the trade direction.

**Why:** a summarizer optimizing for brevity drops the qualifier that carries the *sign* ("but concentrated", "not yet", "except at the tail"). Two-sided or hedged findings are the ones most likely to invert under compression.

**How to apply:** treat triage one-liners as a *routing* layer, not as evidence. Before banking any load-bearing summarized item into a state file, a weight, or a trade, re-read it against the full source (or send a second, deeper agent). RED's Chunk-1 inbox triage was only corrected because Chunk-2 read the peers' full digests. Related: [[finding_verify_reader_before_source]], [[finding_schema_conformance_not_clean_text]], [[feedback_evidence_standalone]].
