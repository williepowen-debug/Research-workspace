# WQ-176 leg ② PLAN — ten cells, old → new (no TSV change until --apply)

Rule (WQ-176 design, Will 09:52): cap `consequence_on_fire` · `last_checked` · `source` · `review_by` at ≤400 B. The cell keeps the STATE — the latest dated read, its verdict tokens, the load-bearing levels and the ruling/commit cites — and points at the archive; DETAIL (sub-levels, secondary cites, rationale prose) moves to PROME/archive/GATES_STATE_HISTORY_2026-09-04_leg2.md, where the pre-cut cell is preserved VERBATIM with an entry-crc32 (the crc is computed at --apply and printed in that file's section banners; the plan shows text only). Nothing is lost from the repo; what the LIVE cell loses is detail a grader reaches through the pointer. HY-REKILL consequence exempt (WQ-162).

### GATE-HY-REKILL · last_checked: 431 → 307 B
OLD:
2026-09-03 12:5x (PROME, step-2 package; observation-chain gloss, no count moved): 263 is the AS-OF value on BOTH 8/27 and 8/31 — two observations, one level; the 8/28 as-of print = 260, PUBLISHED 8/31 (as-of vs publication dates labelled). Then: 2026-09-02 21:3x WQ-162 EXECUTED on Will's word (letter rewritten self-grading; state UNCHANGED: NOT FIRED 0-of-2, HY 265 [9/1], 260 [8/28] ON the line) · hist→GATES_STATE_HISTORY
NEW:
2026-09-03 12:5x PROME step-2 package (gloss only, no count moved): 263 = the AS-OF value on both 8/27 and 8/31; the 8/28 as-of print = 260, published 8/31. 2026-09-02 21:3x WQ-162 EXECUTED (self-grading letter; NOT FIRED 0-of-2; HY 265 [9/1], 260 [8/28] ON the line) · hist→STATE_HISTORY_2026-09-04_leg2

### GATE-LIQ-079 · consequence_on_fire: 864 → 394 B
OLD:
funding-seizure pre-emption memo -> PROME/NEXUS/BROCK/HENRY same session — X1 SEMANTICS SIGNED OFF (BROCK 7/20, riders R1-R4 BAKED IN): R1 SEPARATE funding root, NEVER log a 079 fire as "X1 MET" (X1 unchanged = wrapper-leads AND HY>280 BOTH); R2 a 079 fire does NOT open the X1-governed LIQUID credit-bear SIZING gate (funding/liquidity posture only — different bear, different sizing rail); R3 a live 079 fire SUSPENDS BROCK's wrapper-leads read (forced-delever contamination; re-adjudicate on a clean post-event leg); R4 regime caveat REVISED (KB-LIQ-087): not "buffer gone" but "RRP level is the wrong regime variable" — recalibration judged off reserve-demand-curve slope; LIQUID call at fire-time. Verdict memo AGENTS/LIQUID/inbox/processed/2026-07-20_from-BROCK_gate-liq-079-x1-signoff.md (also retires the KB-LIQ-074 sign-off chase — 079 supersedes)
NEW:
funding-seizure pre-emption memo → PROME/NEXUS/BROCK/HENRY under X1 riders R1–R4 (BROCK 7/20): R1 separate funding root, never 'X1 MET' (X1 = wrapper-leads AND HY>280) · R2 opens NO X1 sizing gate · R3 SUSPENDS BROCK's wrapper-leads read · R4 RRP = wrong regime variable; LIQUID call at fire-time. Memo: BROCK→LIQUID 7/20 (supersedes KB-LIQ-074) · hist→STATE_HISTORY_2026-09-04_leg2

### GATE-FALCON-001 · last_checked: 464 → 339 B
OLD:
2026-09-01 OWNER (FALCON combined touch abdf4efe5: 9/1 consumer date CONFIRMED/CONSUMED; FALCON's own Kharg GATE 1 (NOT this row's leg 1, which stays FIRED 7/23) FIRM-NEGATIVE adjudicated on CENTCOM's no-target release + the Iranian-media list, re-adjudicate on any CENTCOM list/BDA; Kharg GATE 2 (same FALCON pair, not this row's leg 2) NOT FIRED, IRGC mine claim CENTCOM-denied; D 60→65 / C 35→30 re-mark, KB-FALCON-116/117/120) · hist→GATES_STATE_HISTORY
NEW:
2026-09-01 OWNER (FALCON abdf4efe5): 9/1 consumer date CONSUMED; FALCON's own Kharg GATE 1 FIRM-NEGATIVE (CENTCOM no-target release; re-adjudicate on any CENTCOM list/BDA) and Kharg GATE 2 NOT FIRED — neither is this row's leg 1 (FIRED 7/23) or leg 2; D 60→65 / C 35→30 (KB-FALCON-116/117/120) · hist→STATE_HISTORY_2026-09-04_leg2

### GATE-FALCON-001 · source: 617 → 376 B
OLD:
AGENTS/FALCON/reports/2026-08-15_gate-falcon-001-leg3-yanbu-wc0803-fire-adjudication.md (leg-3 fire adjudication) + AGENTS/FALCON/reports/2026-08-06_commissioned-session.md (8/6 real session — window basis + ratification) + AGENTS/FALCON/reports/2026-08-05_yanbu-leg3-recheck.md (8/5 re-check) + AGENTS/FALCON/reports/2026-08-02_yanbu-leg3-repull-adjudication.md (leg-3 basis) + AGENTS/FALCON/reports/2026-07-23_babelmandeb-leg1-adjudication.md (fire adjudication) + AGENTS/FALCON/outbox/2026-07-23_to-PROME_bab-leg1-adjudication.md + frozen spec AGENTS/FALCON/reports/2026-07-21_babelmandeb-SIG-003-adjudication.md
NEW:
AGENTS/FALCON/reports/2026-08-15_gate-falcon-001-leg3-yanbu-wc0803-fire-adjudication.md (leg-3 fire) · AGENTS/FALCON/reports/2026-07-23_babelmandeb-leg1-adjudication.md (leg-1 fire) · frozen spec AGENTS/FALCON/reports/2026-07-21_babelmandeb-SIG-003-adjudication.md · the 8/06 · 8/05 · 8/02 basis/re-check reports + the 7/23 outbox → hist→STATE_HISTORY_2026-09-04_leg2

### GATE-OSPREY-001 · last_checked: 692 → 397 B
OLD:
2026-09-02 OWNER GRADE (OSPREY e82b1f79b/735cb857c, ANALYSIS_2026-09-02.md §6): (a) NOT FIRED — no assessment result for the July episode published 8/20→9/2; every SPM-damage claim is still the 2025-11-29 SPM-2 arc (on the letter's rejection list); net-new moves AWAY from firing: CPC back to full loading capacity with SPM-2 repaired · (c) NOT FIRED — SEARCH-NOT-FOUND for any Aug/Sep 2026 Tengiz FM; every FM headline is the Jan-2026 GTES-4 arc (the letter's registered false-leg-(c) trap); Chevron downplaying extended-shutdown risk · (b) FIRED 7/24 unchanged. Grade quality: fresh verification, not absence-by-default (the 8/15 grade was the latter) · hist→GATES_STATE_HISTORY
NEW:
2026-09-02 OWNER GRADE (OSPREY e82b1f79b, ANALYSIS_2026-09-02.md §6): (a) NOT FIRED — no July-episode assessment 8/20→9/2; every SPM claim = the 2025-11-29 SPM-2 arc; CPC full loading · (c) NOT FIRED — SEARCH-NOT-FOUND for any Aug/Sep 2026 Tengiz FM (all = the Jan-2026 GTES-4 arc) · (b) FIRED 7/24. Fresh verification (8/15 was absence-by-default) · hist→STATE_HISTORY_2026-09-04_leg2

### GATE-FERT-G3 · last_checked: 524 → 390 B
OLD:
2026-09-02 OWNER GRADE (FERT 9a9e6fff5): NOT FIRED both legs — quota 3.3 Mt UNCHANGED (SEARCH-NOT-FOUND on any down-revision at MOFCOM/NDRC relays, CF commentary, Profercy); the $660/$670 floor lifted early June and REPLACED by a lower unpublished guidance; China offers into India <$400/mt CFR vs prevailing intl ~$415-445/mt [Profercy 8/13] — behaviour dispositive. ⛔ kill-on-sight: 'quota expanded to 5-5.5 Mt' = China's HISTORICAL export range (2025 actual 4.9 Mt), not a quota action · hist→GATES_STATE_HISTORY
NEW:
2026-09-02 OWNER GRADE (FERT 9a9e6fff5): NOT FIRED both legs — quota 3.3 Mt UNCHANGED (SEARCH-NOT-FOUND); $660/$670 floor lifted June, lower unpublished guidance; China offers into India <$400/mt CFR vs ~$415–445/mt intl [Profercy 8/13]. ⛔ kill-on-sight: '5–5.5 Mt quota' = the historical export range (2025 actual 4.9 Mt), not a quota action · hist→STATE_HISTORY_2026-09-04_leg2

### GATE-TERRY-007 · review_by: 593 → 374 B
OLD:
2026-09-08 RE-DATED at PROME 9/3 closeout — the 9/2 review passed with TERRY dark; PROME's CONSUMER read of the 9/1 official (DGS10 4.79, +4bp, window high; counter stays 0-of-5, 29bp from 4.50; DFII10 2.44 add-gate NO-ADD) is in GATES_STATE_HISTORY_2026-09-03_step2.md (GATE-TERRY-007 · last_checked; the OWNER grade of 9/1 is the live last_checked) and is NOT the grade; TERRY grades the 9/2–9/4 officials at its next boot (owed with the Sep-18/Sep-30 expiry pass), then weekly at DGS10's T+1 cadence; expiry 9/30 may moot — NO-VERDICT if expiry beats it · hist→GATES_STATE_HISTORY
NEW:
2026-09-08 RE-DATED at PROME 9/3 closeout (9/2 review passed, TERRY dark). PROME consumer read 9/1: DGS10 4.79 window high, 0-of-5, 29bp; DFII10 2.44 NO-ADD (GATES_STATE_HISTORY_2026-09-03_step2.md) — NOT a grade; TERRY grades 9/2–9/4 at next boot (with the Sep-18/30 expiry pass), then weekly; expiry 9/30 may moot ⇒ NO-VERDICT · hist→STATE_HISTORY_2026-09-04_leg2

### GATE-REG-T02 · last_checked: 571 → 394 B
OLD:
2026-09-01 OWNER GRADE (REGINALD, own window 17:13, 5c94c9622; letter NOTES.md §REG-T-02 STATE RULING 2026-09-01): instrument scripts/market.py → Yahoo WAL regular-session close $77.26 (bar O 77.94 / H 78.93 / L 77.05), agrees with PROME fetch.py; distance $0.74 = 0.95% BELOW the line; attribution SECTOR-WIDE (WAL −1.11% vs KRE −1.28%, cohort median 14/26, Spearman ρ +0.253 wrong sign for PC repricing) ⇒ LEVEL fire, V1/V3 mechanism UNCHANGED — carry the attribution with the fire. REG-T-01 UN-FIRED (KRE $72.62, 21.0% buffer) · hist→GATES_STATE_HISTORY
NEW:
2026-09-01 OWNER GRADE (REGINALD 5c94c9622, NOTES.md §REG-T-02): scripts/market.py → Yahoo WAL close $77.26, $0.74 = 0.95% below; attribution SECTOR-WIDE (WAL −1.11% vs KRE −1.28%, cohort median 14/26, Spearman ρ +0.253 wrong sign) ⇒ LEVEL fire, V1/V3 UNCHANGED, carry the attribution with the fire. REG-T-01 UN-FIRED (KRE $72.62, 21.0% buffer) · hist→STATE_HISTORY_2026-09-04_leg2

### GATE-CORAL-MSI-01 · last_checked: 732 → 399 B
OLD:
2026-09-02 OWNER GRADE (CORAL 70025dcc3/fcbcf5be2, Parcl pulled direct ~22:0x ET, all five pages self-stamp 'Updated: 9/3/2026' = UTC): Tampa 7.01 · Punta Gorda 6.52 · North Port 6.29 · Cape Coral 5.95 · Lakeland 5.97 — 3-of-5 >6.0, all five FELL (first reading with no riser; Tampa rolls over after four rises); graded on the frozen 8/23 letter as sub-threshold reading 1 of 2 ⇒ 🔴 HOLDS, clock starts, nothing de-fires; second countable reading NOT BEFORE 2026-09-13 (≥10d after the 9/3 vintage; a pull before then is the SAME observation). ⚠️ Parcl per-metro listing counts / price-cut shares went client-side — SEARCH-NOT-FOUND, never zero; MSI values verified twice independently · hist→GATES_STATE_HISTORY
NEW:
2026-09-02 OWNER GRADE (CORAL 70025dcc3, Parcl direct, stamp 9/3/2026 UTC): Tampa 7.01 · Punta Gorda 6.52 · North Port 6.29 · Cape Coral 5.95 · Lakeland 5.97 = 3-of-5 >6.0, all FELL; sub-threshold reading 1 of 2 (8/23 letter) ⇒ 🔴 HOLDS; second countable reading NOT BEFORE 2026-09-13 (≥10d; nothing de-fires). listings SEARCH-NOT-FOUND (never zero) · hist→STATE_HISTORY_2026-09-04_leg2

### GATE-FLG-T08 · consequence_on_fire: 829 → 398 B
OLD:
ACTION ON FIRE: PROME spawns FLG (Tier 1 — a dated resolution on an idle desk inside an approved workstream) to grade T-08 against its multifamily book (rent-regulated exposure, provisioning already taken) and route to REGINALD/HOMER per its charter. No capital path registered · REFINED 8/28 (FLG, RGB Order #58 at primary, 2c1b48b7f): the freeze governs leases COMMENCING 2026-10-01→2027-09-30 and phases in as leases renew — FY2026 (reviewed Q2-2027) carries at most Oct–Dec partial exposure; FY2027 (reviewed Q2-2028) is the first year carrying most of a freeze; a 0% guideline CAPS revenue, it does not cut it (DSCR degrades as costs outrun frozen rents — grinding, not a step). Trigger, level and action UNCHANGED; only the downstream expectation moved (FLG T-11 2028-08-04 registered for the bite, T-09 demoted)
NEW:
ACTION ON FIRE: PROME spawns FLG (Tier 1) to grade T-08 vs its MF book, route REGINALD/HOMER; no capital path. REFINED 8/28 (FLG 2c1b48b7f, RGB #58): leases commencing 2026-10-01→2027-09-30, phased (FY2027 first full year); a 0% guideline CAPS revenue (DSCR grinds); trigger/level/action UNCHANGED; FLG T-11 2028-08-04 registered for the bite, T-09 demoted · hist→STATE_HISTORY_2026-09-04_leg2
