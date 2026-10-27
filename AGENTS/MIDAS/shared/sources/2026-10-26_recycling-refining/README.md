# October 26 authorized recycling and refinery research

Capture time is UTC October 27, still October 26 in New York. `capture.json` records exact URLs, retrieval timestamps, HTTP status, bytes and SHA256 for new raw captures. `capture.py` performs the bounded retrievals; no CME endpoint is accessed.

- `sibanye_h1.html` / `.txt`: SEC-filed H1 2026 issuer report. Table: ounces/lbs sold excluding mixed scrap. The report includes acquired North Carolina; no constant-perimeter global recovery inference.
- `umicore_h1.html` / `.txt`: issuer's German-domain English H1 release, July 31. Main-domain web fetch previously returned 402; this is a public issuer regional page, no paid access or credentials.
- `valterra_rns.html` / `.txt`: issuer-distributed RNS on Investegate, October 23. Use the announcement and tables, not the distributor's AI-generated summary. `valterra_tables.json` preserves detailed table cell boundaries. The direct issuer page is held and hash-linked from the earlier coverage bundle.
- `silver_survey.pdf`: full issuer April survey; `silver_page_11.png` and `.txt` show PDF page 11 / printed page 9. The earlier source locator agrees.
- `jm_page_6.png`: visually inspected table from the existing full May 14 primary PDF; source path/hash in `calculations.json`.
- `wpic_page_19.png`, `wpic_page_20.png`: visually inspected annual and quarterly tables from the existing primary September 9 Q2 report; source path/hash in `calculations.json`.
- WGC Q2 raw HTML and Nornickel full primary PDF are retained at their existing paths, SHA256-linked in `calculations.json`; no duplicate raw files required.

`calculate.py` holds the transcribed source-model/producer inputs, checks selected RNS table sequences, tests rounding tolerances, computes fixed-input sensitivities and issuer-guidance requirements, and verifies four frozen artifacts. `calculations.json` is its output. Rounding is retained: WPIC reported balance 265 versus rounded rows 264 koz; WPIC Q2 recycling components 465 versus headline 466 koz; silver annual rounded difference −46.2 versus reported −46.3 Moz.

Open-loop secondary supply, closed-loop returns, producer sales and refinery throughput are different objects. New processor figures are not added to existing global balances. Sensitivities hold all other inputs fixed and do not replace registered forecasts. The two reports make no new price observation or score/rule change. Aggregate October recovery, a matched Valterra audited inventory bridge and permanent-loss share are unmeasured; this bounded work is complete at those disclosure limits.
