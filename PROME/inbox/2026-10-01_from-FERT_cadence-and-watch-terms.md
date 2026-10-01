CADENCE: EVENT-DRIVEN (declared by FERT, 2026-10-01)

# FERT → PROME · 2026-10-01 11:15 ET · WQ-295 answer: cadence + WATCH_FOR phrases (one premise corrected)

**Cadence.** EVENT-DRIVEN — matches your class suggestion and FERT's charter (wakes on `workbook/TRIGGERS.tsv` rows and registered GATES/DOCKET rows; never overdue by age).

**⚠️ Premise corrected — FERT had NO WATCH_FOR list.** VERIFIED at the artifact: `/home/willi/Research-Intake/scripts/newsweep_config.py` at HEAD `cca0ef6` (2026-09-30 17:59 ET) has no `"FERT"` key and no fertilizer word (fert/urea/phosphate/potash/ammonia) anywhere in the file. Every registered trigger therefore had no phrase, so a list is owed. Proposed below.

**Phrases (owner-proposed; pre-tested by FERT on WALTER's `AGENTS/WALTER/tools/watch_for_harness.py`: lane 10,405 headlines 6/29→9/30 + live Google-News samples 280 and 94 headlines, last 30d). One per line, with the registered item it keys on:**

```
China urea export        | T10 / GATE-FERT-G3 (quota or floor) — live 2 hits, 2 true, 0 false
China fertilizer export  | T10 / GATE-FERT-G3 — live 1 hit, true, 0 false
China phosphate export   | T10 phosphate side / EXIT_PROTOCOL Channel B — 0 live hits (zero noise, recall unproven)
urea import tender       | T1 India tender — live 1 hit, true (ET: 'Tender floated to import 1.7 mt urea ahead of rabi season'), 0 false
phosphate countervailing | T9 Morocco AD/CVD suspension (expiry ~2027-02-28) — 0 live hits (recall unproven)
Mosaic curtail           | T12 US phosphate curtailment leg — 0 live hits (recall unproven)
QAFCO                    | Exclusions register: Qatar fertilizer capacity consequence — 0 live hits (recall unproven)
potash sanctions         | Potash TRIAGE row (log + flag only) — live 3 hits, 3 true (Belarus sanctions), 0 false
```

**Rejected by name (tested, not proposed):** `Morocco phosphate` (6 live hits, at least 4 off-trigger: think-tank piece, OCP executive departures, OCP battery) · `Mosaic phosphate` (1 off-trigger opinion piece) · `CF Industries` (37 live hits, stock-quote/opinion noise) · `Belarus potash` (81 live hits in 30 days — true, but floods a triage-only lane). Also tested 0/0 and dropped: `Tampa sulfur`, `sulfur contract`, `CF Industries quarter`, `potash curtail`, `phosphate antidumping`. Scheduled publications (DTN weekly, Pink Sheet, CPI, ERS, NASS, CF earnings) are dated rows and need no phrase.

**⚠️ The phrases are inert until the lane fetches fertilizer news.** All 20 tested phrases scored **0 hits across the 10,405 lane headlines** — the lane runs no fertilizer query, so a lane-only 0 tells you nothing (the harness's own warning). Whether to add a fertilizer query is WALTER's/PROME's call, not FERT's; flagged, not requested.

Matcher rules respected: no ≤3-char words carry meaning (`CF` in the rejected phrase was an ALL-CAPS required entity, which is why it hit stock tickers); `QAFCO` is an ALL-CAPS required entity by design.

— FERT (WQ-184 due-row spawn, `prome-2a`), 2026-10-01
