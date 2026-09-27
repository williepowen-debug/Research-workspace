# PROME → ORACLE · 2026-09-27 12:24 ET · ONE question: is the 2026 bank-failure count (or a next-failure event) priced anywhere, and what did it do across Fri 9/25? (Will-spawned you for this; bounded)

**Shared fact base (read first, do not re-derive):** `PROME/plans/2026-09-27_nano-banc-failure-investigation-PLAN.md` §1 — every figure dated and sourced (FDIC PR · DFPI PR · FDIC BankFind cert 58590 · American Banker 9/25 21:17 ET). **Research only — no card, no trade; if a bank in Will's book perimeter is named, packet TERRY, never propose.** **ONE shared figure:** the loss severity / implied haircut on the retained pool — REGINALD OWNS it, CREED CONSUMES it (cite REGINALD's file, never a second number). **Delivery (COMPLETION_SPEC):** your artifact in your dir + a dated packet to `PROME/inbox/` (carve-out ① commit) + SendMessage `prome-09` the doorbell; then close out when PROME asks (WQ-249). Budget: 60–120 min; deliver what is done at 120 min with an explicit PARTIAL if so. Will present (`prome-09`, 2026-09-27 12:24 ET).

**Context:** Nano Banc (Irvine CA, $736M) failed Fri 9/25 — the SIXTH US failure of 2026 vs two in each of 2024 and 2025 (FDIC failed-bank list: Metropolitan Capital 1/30 · Community B&T West GA 5/1 · Kentland 7/10 · Small Business Bank 7/17 · Tioga-Franklin 8/21 · Nano Banc 9/25). Your charter lists "Polymarket: bank failure markets (monthly)" and "Kalshi: bank stress".

## The one ask (deliverable: `AGENTS/ORACLE/analysis/2026-09-27_bank-failure-markets.md`; watchlist rows if a market exists)
1. `polymarket.py pull --log` + `kalshi.py pull --log`: every open market on US bank failures (count in 2026, "another bank fails by <date>", any named-bank market), with open interest / volume and the price series around 9/25 (before the 21:17 ET news vs after; the Monday 9/28 open if you run again). Say NONE with the query terms tried if none exists — that absence is the finding.
2. If a market exists: does it imply more than the FDIC base rate (six by late September ⇒ ~8 for the year on a naive pace), and did it move on Nano Banc at all? One table.
3. Do not register a prediction or a gate; this is a read. Route the file to PROME; WALTER gets the watch term `bank failure` only if a market exists.

— PROME (`prome-09`)
