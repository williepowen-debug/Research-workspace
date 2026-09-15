---
name: finding_flat_pdf_parse_returns_a_perfectly_counted_wrong_alignment
description: A flat multi-page PDF text extract can yield a column alignment that counts perfectly and is entirely wrong; the ratio survives the corruption, so it certifies nothing.
symptoms: "pdf parse looks right but dates are wrong; extract_text columns misaligned; ratio matched but rows wrong; PDF table shifted across pages; schedule parsed to the wrong month; counts line up but values don't; pdfminer wrong column"
metadata:
  type: reference
---

Parsing a multi-page PDF with a FLAT text extract (`pdfminer.high_level.extract_text`) can return a column
alignment that is **arithmetically perfect and semantically wrong**, with no error and no tell.

**The 2026-09-15 instance (BOND, Treasury Tentative Auction Schedule):** a flat parse yielded 213 securities
and 639 dates — an exact 3:1 ratio — so slicing `[0:n] / [n:2n] / [2n:3n]` as announce/auction/settle produced
a clean, correctly formatted table. **It placed the AUGUST 3-year auction in OCTOBER.** A multi-page PDF's flat
text does not preserve column blocks across page boundaries; the three date columns interleave *by page*.

🔑 **The ratio survives the corruption, so it certifies nothing.** The count matching is exactly what makes the
output convincing — this failure has no exception, no missing field, and a plausible result. It is the
wrong-reference class with the strongest disguise.

**What caught it:** reading ONE KNOWN-TRUE ANCHOR out of the output (the August refunding auctioned 8/11–8/13,
not in October). Nothing else would have.

**Practice:**
- Use `extract_pages()` with per-page y/x cell grouping for any multi-page tabular PDF; never a flat extract.
- **Before trusting any unknown row, verify one row you already know independently.** Make this the habit, not
  the exception — it is the only cheap check that detects this class.
- Agreement between your parse and someone else's *reading of the same document* raises confidence in the
  reading, not in the document: that is two readers of one primary, not two sources. Say so.

Related: [[finding_instrument_reports_clean_against_the_wrong_reference]] ·
[[finding_a_charitable_reading_of_your_work_is_the_one_to_check]] ·
[[finding_lenient_parser_reports_unparseable_as_a_behavior]]
