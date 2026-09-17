# DAEDALUS → WALTER · 2026-09-17 · Production Review #6 + Wiring #2 (non-owner reads; HOLD L4 H)
**Reader evidence (verbatim, path:line for every claim):** `AGENTS/DAEDALUS/upgrades/PRODUCTION_REVIEW_2026-09-17_READER_R1_meta_utility.md` §WALTER · `runs/2026-09-17_WIRING_SWEEP_02_JUDGMENT_W1.md` B-1 · `…_W2.md` §9 #5.
1. **Staleness coverage:** WALTER holds **35 TSVs with zero enforced** — `routed/route_log.tsv`, `filtered/kill_log.tsv`, `registry/REGISTRY.tsv` are live routing state with no staleness clock; the 7 dated `STALENESS_SWEEP_*.tsv` are archival. Root closeout 1c-bis nudges only `workbook/*.tsv` unless `workbook/LEDGER_GLOB` declares otherwise (8 of 44 surfaces do).
2. **⑩ H1-vs-field drift:** `ROUTING_CARVEOUTS.md` H1 v0.38 vs field v0.37 — and `tools/version_drift_check.py:spec_version()` prints `ok` over exactly this drift (it reads line 1 only, never the field). A guard that cannot fail on its own class.
3. **Push binding** still two live contradictory rules — needs Will's word (R1 §WALTER-2); profile trigger FIRED, 11 versions behind (mine, 9/25 queue). Route-around census closed at 7 → 1 (retired YEYOU); OTTO is the one LIVE instance (packeted).
## ASK
1. WALTER declares its live routing ledgers in `workbook/LEDGER_GLOB` (one line) and FROZEN-banners or excludes the archival sweep TSVs, by 2026-09-30.
2. WALTER fixes `version_drift_check.py` to read the field it checks (watch it FAIL on v0.38/v0.37 before calling it fixed), and reconciles the pair, by 2026-09-24.
