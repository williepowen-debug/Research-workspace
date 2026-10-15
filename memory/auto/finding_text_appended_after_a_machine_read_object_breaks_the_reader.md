---
name: finding_text_appended_after_a_machine_read_object_breaks_the_reader
description: A ledger cell that ends in a machine-read object (JSON) must END there — a receipt appended after it makes the reader fail on the whole row, silently turning evidence into UNKNOWN
metadata:
  type: feedback
symptoms: "Extra data" from json.loads on a TSV cell; closeout reader reports UNKNOWN for rows that visibly carry receipts; "the row has the receipt but the check says missing"; append-only receipts to a notes cell
---

**Fact (PROME, 2026-10-14):** `PROME/state/ORCH_LOG.tsv` notes cells end in a `closeout_v1={…}` JSON object that `orch_closeout.py` reads with `raw_decode` from the `closeout_v1=` marker. PROME appended receipts AFTER the object (` · RECEIPT 21:34 ET …`) on 12 rows in one evening; the reader raised "Extra data" and classified each row UNKNOWN — the receipt existed, was readable by a human, and was invisible to the only instrument that grades it. 17 older rows (9/21–10/1) had the same shape. A fresh-context survey found it; PROME's own self-check never did, because `cat` shows the receipt.

**Why:** n=29 rows across four sessions, all by the same reflex — "append the newest fact at the end." A cell with a machine-read tail has a fixed END; new prose belongs BEFORE the object. The failure is silent and self-flattering: the row looks MORE complete to a human the more it breaks for the reader (`[[finding_raw_and_rendered_readers_disagree_with_no_tell]]`, `[[finding_record_of_an_action_is_not_the_action]]`).

**How to apply:** before writing to any cell or line that carries a parsed object (JSON, a `key=value` tail, a crc), locate the object and insert BEFORE it, re-serialising the object last; after the write, run the reader that consumes the cell (`orch_closeout.py` for ORCH_LOG) and look for parse errors, not for the presence of your text. A tool that writes such cells (the receipt command idea) enforces JSON-last by construction. Repair recipe used 10/14: `raw_decode` the object, move the trailing text ahead of the marker, re-dump — content-preserving, verified by the reader's parse-error count going 28 → 0.
