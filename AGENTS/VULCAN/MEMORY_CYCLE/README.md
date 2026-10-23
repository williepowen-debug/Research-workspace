# MEMORY_CYCLE — VULCAN's memory-cycle working home (S2)

**Created:** 2026-10-23 at Will's request ("create a memory specific subfolder"). **Owner:** VULCAN. **Channel:** S2 (memory cycle). Not a new channel and not a new score: **`STATUS.md` stays canonical for S2's score, band and live read; facts stay in `workbook/KB_GENERAL.tsv` (channel `S2`); dated obligations stay in `docket/CATALYSTS.tsv`.** This folder holds the working model and the research that explains them, so a cold reader finds the memory story in one place. Named `MEMORY_CYCLE` (not `MEMORY`) so it is never confused with the fleet's session-notes `memory/` directories.

## Working model (as of 2026-10-23, not a registered forecast)

Memory equities have priced a downturn the price data has not shown. **The question is no longer whether contract prices turn, but how hard.**

| Read | Figure | Date · source |
|---|---|---|
| Contract forecast | DRAM **+10–15%** / NAND **+15–20%** QoQ 4Q26, unrevised; no 1Q27 forecast yet | TrendForce 9/30 [KB-187, KB-282] |
| Spot | DDR5 **$61.27** (+1.1% w/w); NAND wafer spot −1.3% | 10/23 [KB-280, KB-282] |
| Equities from June peaks | MU **−27.7%** ($877.55) · SNDK −47.0% · SK hynix −56.3% · Samsung −40.6% | 10/23 close [KB-282] |
| Valuation | MU ~5.0x FY27 consensus EPS, **7.2x book** (past troughs ~1.0–1.3x) | 10/23 [KB-282] |
| AI demand tell | H100 rent indexes up (OCPI $3.15, +15% w/w) | 10/22–23 [KB-281] |
| Bear legs | Phones −22.0% YoY (IDC Q3); 2027 WFE >$200B = 2027–28 supply wave (Lam call); CXMT/YMTC 2027–28 | [KB-230, KB-272, KB-282] |

**Analogs (n=2):** equity led the contract turn by ~4–5 months both times; MU peaked 6/25/2026 (month 4 now). **2018** steep turn (−8% then ~−20%) ⇒ second leg, MU −28% → −54%. **2021** shallow turn (−3 to −8%) ⇒ the low came within three weeks. New in 2026: >35% of MU revenue on multi-year contracts with floor/ceiling bands [KB-188] — may make the turn shallower; unproven.

## Pre-stated test for SK hynix (10/28) and Samsung (10/29)

Written 2026-10-23 before either print (first public: none). Registered at `docket/CATALYSTS.tsv` (10/28 row) and KB-282.

| Outcome | Condition | Consequence |
|---|---|---|
| **2021 path (bounce)** | Neither cites customer order cuts; at least one says 2027 supply is sold out/contracted; neither guides 4Q DRAM price down | Equity drawdown read as thermometer; S2 stays 2 |
| **2018 path (second leg)** | Either cites SERVER order cuts, OR guides both 4Q bit shipments AND price down | **S2 2 → 3** (existing upgrade leg) |
| Ambiguous | Cuts limited to phones/PCs | Record; no score change |
| Override | TrendForce publishes 1Q27 DRAM ≤ 0% | Treat as the 2018 path regardless |

## Instrument caveat

`tools/semi_watch.py`'s "memory" basket is **MU/SNDK/WDC/STX** — half of it is hard-disk makers with their own supply shock. Quote MU + SNDK separately when the claim is about memory (MU+SNDK −14.8% on the 10/16 row vs −17.9% basket) [KB-282]. Changing the tool is a separate decision; not done.

## Files

**In this folder**

| File | What | Kind |
|---|---|---|
| `README.md` | Working model, pre-stated print test, instrument caveat (this file) | Live — update per the rule below |
| `2026-10-23_divergence-investigation.md` | Full 10/23 investigation: contract/spot, drawdowns, valuation, 2018/2021 analogs, bear case, supply (moved here from `reports/2026-10-23_puck/`) | Dated research record |
| `S2_FACTS.tsv` | Every KB row on channel S2 plus other-channel rows that name memory (`match` = channel-S2 / keyword) | **GENERATED** by `build_views.py` — never edit |
| `S2_PREDICTIONS.tsv` | Every live or resolved S2 forecast (VULCAN-02, -04, -11, -12, -16) | **GENERATED** — never edit |
| `HISTORY.md` | Verbatim copies of rotated S2 STATUS cells (10/08, 10/09, 10/15) with crc32 | Frozen copy; `CHANNEL_DETAIL.md` is the record |
| `build_views.py` | Rebuilds the two views from the canonical ledgers | Tool |

**Elsewhere (linked, not copied — live or canonical)**

| File | What |
|---|---|
| `../STATUS.md` (S2 row and live read) | Canonical score, band, current read |
| `../THESIS.md` § S2 | Live causal stages |
| `../workbook/EXIT_PROTOCOL.md` §3 | S2 kill/flip rules |
| `../workbook/KB_GENERAL.tsv` | Canonical facts (the view above is a filtered copy) |
| `../workbook/S2_SERIES.tsv` · `../tools/semi_watch.py` | Weekly equity + DDR spot series |
| `../workbook/MU_FQ4_RESOLVER.md` | Spent Micron FQ4 resolver (frozen) |
| `../archive/THESIS_ARCHIVE_2026-10-20_S1-S2.md` | Earlier S2 thesis text (frozen) |
| `../reports/2026-09-25_newsweep-raw_semis-memory-geo.md` | 9/25 raw news sweep incl. memory |
| `../docket/CATALYSTS.tsv` (10/28 row) | Registered hynix/Samsung test date |

## Update rule

At each S2 event (hynix/Samsung/Micron prints, TrendForce revisions), update the working-model table here **after** STATUS and KB, with the KB row cited, then run `python3 AGENTS/VULCAN/MEMORY_CYCLE/build_views.py` so the views match the ledgers. If this README disagrees with STATUS, STATUS wins.
