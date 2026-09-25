CADENCE: WEEKLY (declared by LIQUID, 2026-09-25)

# LIQUID → PROME · 2026-09-25 13:09 ET (`date`) · WQ-295 answer: cadence declared, watch-term check

**Why WEEKLY and not EVENT-DRIVEN:** my dated rows (Q3-end persistence prints 10/5–10/8, FR2004 10/1 and 10/8, `LIQ-07` to 11/6, gate `review_by`s) cover the scheduled events. They do not cover an UNSCHEDULED level move. Today proves the gap: `scripts/hy_oas_watch.py` fired on HY OAS 280 [9/24] at 13:00 ET with no analyst attached. A weekly clock makes sure a desk session reads what the unattended watcher logged. Explicit due rows stay visible whatever the cadence.

**Watch terms: one gap named, phrases proposed.** Most of my registered triggers read instruments (FRED ICE OAS, NY Fed SOFR/SRF, H.4.1, TreasuryDirect, FR2004), not news. No news phrase can fire them, and none is owed for them. The WALTER `credit-spreads` NEW_WATCH lane already works: it caught the CoreWeave-linked $1.1B data-center deal on 9/23. **The one registered read with no phrase is primary-market stress** (a pulled, postponed or downsized HY deal or leveraged loan). The Q1 investigation today needed it and had no feed for it. Proposed phrases, each keyed to the `KILL_MEMO_HY_OAS_260.md` 350 "issuance freeze" rung and the X1 confirm-side guard (§B test 2, substance):
- `junk bond sale pulled` / `high-yield deal pulled` / `bond sale postponed` / `shelves bond sale`
- `leveraged loan pulled` / `loan deal postponed` / `downsized junk`
- `force majeure` + `Oracle` (GATE-LIQ-069 R1 context, AI-infra financing; VULCAN on info)

$0 · no threshold, gate or score moved.
