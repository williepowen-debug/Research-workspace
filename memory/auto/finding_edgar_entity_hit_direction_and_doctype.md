---
name: finding_edgar_entity_hit_direction_and_doctype
description: "Mining fund/issuer filings for a counterparty relationship — an EDGAR keyword hit for entity X in fund Y's filings does NOT establish an X↔Y relationship; classify by document type AND direction before banking it."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 80cd63c7-95a7-47a3-9e8d-eaca96dab15c
  modified: 2026-07-21T01:58:28.823Z
---

When mining SEC/EDGAR filings to confirm a **counterparty relationship** (does insurer X lend to / hold fund Y?), a full-text keyword HIT for X in Y's filings is a **claim of relevance, not a confirmed relationship**. Before banking it, classify by **document type AND direction**:

- **Credit-agreement exhibit (EX-10.x)** → the actual lender/party register. Insurer absent here = not a named lender (a real negative). This is the only doc that confirms a *lender* relationship.
- **NPORT-P / portfolio-holdings filing** → the fund's OWN assets. An entity name here means **the fund is a CREDITOR TO / holder OF that entity — the REVERSE direction.** (2026-07-20: "Global Atlantic" 16 hits in CCLFX's NPORT = CCLFX lends to GA-linked issuers, NOT GA holding/lending to CCLFX. Misreading this inverts the exposure.)
- **Code of Ethics (EX-99.(R)), prospectus (424B3), merger proxy (DEFM14A), IPO registration (S-1)** → affiliation / transaction / boilerplate context, NOT a holding or lending disclosure. (ADS-"Athene" 44 hits = shared Apollo/Athene Code of Ethics; Corebridge-"Blackstone PC" 96 = 2021-22 IPO partnership docs; Brighthouse-"Apollo Debt Solutions" = merger-proxy / variable-product menu.)
- **Eligible-lender DEFINITION inside a credit agreement** → a structural *door* ("...any commercial bank, investment bank or insurance company..."), NOT a named lender. Permitting ≠ present.

**Why:** raw EFTS hit-counts are systematically misleading — on the 5-gated-funds double-jeopardy run, every high-count insurer hit (44/22/16/96) decomposed to boilerplate, reverse-direction, or partnership context; zero were actual lender/holder relationships. Counting would have manufactured false exposures.

**How to apply:** never bank an entity relationship from a hit-count — pull the doc, read the context, and specifically ask "which direction, and is this doc even a holdings/lender register?" Complements [[finding_edgar_fts_refutes_tradepress_negatives]] (FTS as a positive tool) and [[finding_verify_reader_before_source]] (a failed doc-fetch also manufactures a false "none" — re-read with the correct path before concluding absent). Also: per-insurer NAIC Schedule BA (fund-level holdings) is NOT publicly obtainable — insurer 10-Ks/NAIC special reports disclose at asset-CLASS level only, so "insurer holds fund Y" is often correctly answered "not publicly confirmable," which is NOT the same as "no exposure."
