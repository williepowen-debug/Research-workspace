# L701 and certified-settlement evidence bundle

Retrieval: October 26, 2026 ET / October 27 UTC. `access.json` records exact URLs, status, size, retrieval time and SHA-256. Initial ordinary requests to Nornickel indexes returned 403; existing curl_cffi public access obtained the release page and issuer-linked PDFs. The English page renders the content through embedded `App` JSON: `issuer_release_item.json` retains that exact item, including the full-release URL. The visible HTML text alone misses it. One guessed Russian URL returned 404; the actual English canonical page and linked primary PDFs supplied the evidence.

- `issuer_full.pdf` / `.txt`: issuer's October 26 nine-month release; page 2 mechanism, page 3 guidance/production.
- `issuer_h1.pdf` / `.txt`: July 27 H1 release; page 3 reported H1 totals and guidance. The original H1 Pd 1,199 koz differs by 1 koz from summing rounded quarter rows.
- `issuer_full_table.png`, `issuer_h1_table.png`: page 3 rendered using installed pypdfium2 and visually checked. `pdftoppm` is unavailable; rendering succeeded with the installed alternative.
- `broker_20261022/23.html` / `.txt`: Hammerstone editorial reports hosted by eOption; settlement wording and third-party/non-endorsement notice retained. MIRROR, not broker-certified records.
- `ap_contracts_20261022.html` / `.txt`: AP via Raymond James/Barchart; distinct October and December gold rows, field Last. Contract reconciliation only.
- `treasury_real.csv`: PRIMARY Treasury 2026 real par yields; October 22/23 10 YR 2.64/2.66 percent.
- `reuters_future_overhaul.html` / `.txt`: MEDIA report of planned 2027–28 furnace effects; underlying issuer briefing not held. Not a current outage or a PRIMARY supply cut.
- `calculate.py` / `calculations.json`: fixed-input arithmetic, rounding discrepancy, conditional gold conjunction and unchanged-letter hashes. No production-code change or new monitor.

No CME endpoint was probed. Neither editorial settlement wording nor the AP Last column certifies exchange settlement. Raw futures/ETF startup diagnostics are preserved in the existing startup receipt, not relabelled as official settlements here. Reports: `shared/research/2026-10-26_nornickel-9M-L701.md` and `gold/research/2026-10-26_certified-settlement-review.md`, relative to MIDAS.
