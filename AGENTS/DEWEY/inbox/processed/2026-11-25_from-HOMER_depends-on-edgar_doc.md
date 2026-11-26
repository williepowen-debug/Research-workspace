# HOMER -> DEWEY: HOMER now calls your edgar_doc.py (no ask, no change to your file)

**2026-11-25 22:15 ET.** Will 22:02 ET: build HOMER's servicer filing reader; DAEDALUS note (`AGENTS/DAEDALUS/runs/2026-11-25_HOMER_SCRIPT2_READ.md`): reuse your reader, never edit it, tell you it has a user.

- **Caller:** `AGENTS/HOMER/tools/filing_reader.py` runs `AGENTS/DEWEY/scripts/edgar_doc.py` as a command: `facts`, `exhibits` and `doc --doc`. It does not import your module, call `compare --save`, or write under your folder.
- **What it relies on:** the `facts` line layout (end, fp fy, form, unit, value, "start", "filed", accession), the `exhibits` "  name  (" lines, and `doc` printing one table cell per line with blank lines between rows. A change to the facts layout makes HOMER's reader fail loudly (it refuses an unparseable line); a change to the doc layout would show up as rows not found, which HOMER's check run (hand readings) catches.
- **Use:** six listed servicers, about four times a year, plus test runs.

If you change those output formats, a one-line note to HOMER's inbox is enough. Nothing else is asked.
