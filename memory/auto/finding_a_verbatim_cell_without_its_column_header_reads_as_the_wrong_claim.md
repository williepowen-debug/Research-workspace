---
name: finding_a_verbatim_cell_without_its_column_header_reads_as_the_wrong_claim
description: A table cell copied verbatim but detached from its column header carries the wrong claim — a "forward max loss" cell joined under "Then:" read as a payoff; verbatim is a property of (header + cell), and every reader who checked the words agreed they were verbatim.
metadata:
  type: feedback
symptoms: "copied verbatim but reads backwards; loss column looks like a payoff; consequence joined with ' · ' loses which column it came from; three readers passed the text and the fourth read the meaning; a verbatim check that compares strings can never catch it"
---

**What happened (PROME, 2026-10-09, Decision Deck Change A, DOCKET L660/L662):** the generator copied an owner card's option-table row cells verbatim (TERRY's TLT put card §3: `what you get` · `what you give up` · `forward max loss from here`) and joined them under one "Then:" label. Every string matched the card; three independent reads verified "verbatim". The fourth reader read the page as a stranger: option B appeared to pay "~$475 … if TLT closes ≥ $82" when that cell was the LOSS column. A tap would have stored that string as what Will agreed to.

**Why:** "verbatim" was tested as a string property of each cell, but a table cell's meaning is (header, cell). Dropping the header is a paraphrase that no string comparison detects, and the readers who checked word-for-word were checking the wrong unit. Same family as `finding_output_shape_implies_more_than_the_measurement` (the number is right, the presentation implies a wider claim) and `finding_unqualified_identifier_is_a_defect_waiting_for_a_reader`.

**How to apply:** when copying table cells onto another surface, carry each column header WITH its cell whenever the row has more than one consequence column (`forward max loss from here: ~$475 …`), and make the build check compare the HEADED string. When commissioning a verbatim-copy read, ask the reader to read the rendered result as a stranger acting on it, not only to diff the words. A loss/payoff ambiguity on a trade surface is a ❌, never residue.
