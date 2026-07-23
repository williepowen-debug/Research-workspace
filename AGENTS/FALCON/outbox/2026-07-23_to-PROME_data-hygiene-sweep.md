## 2026-07-23 — To: PROME
**Signal:** FALCON data-hygiene sweep complete (Will-directed fleet task) — 8 fixes applied, zero mark/threshold moves. Targeted the layers my ~1hr-earlier state-token sweep did NOT cover: deep doc bodies, script baselines, cited report files, board_log.
**Priority:** 🟡

**GUARDRAILS HELD:** today's Will-approved marks (Bab 4, conv 42/50, D-65/D→75 structure) and all frozen gate/tripwire conditions UNTOUCHED. Every fix is a data-freshness/completeness/vintage correction, each re-stamped; suspected-wrong terms flagged, not silently changed. Own dir only.

### FIXES (was → now → source+date)
1. **board_log.tsv — COMPLETENESS GAP backfilled.** `SIG-W-20260720-003` (SIG-003, the 7/20 Bab blockade declaration) was processed 7/21 AM + moved to WALTER/processed/ but **never logged** → added the row (dated 7/21, marked BACKFILL). *Src: WALTER/processed/ + reports/2026-07-21_babelmandeb-SIG-003-adjudication.md.*
2. **FRESH_LEG_BASELINE.md leg-2 — STALE claim corrected.** "No 7/13+ print / overdue across 7/17-20 re-checks" → **PortWatch has now published 7/13-7/19** (newest **7/19 = 15/88 = 17%**, tankers 4; 7/13 9·7/14 11·7/15 12·7/16 10·7/17 11·7/18 17·7/19 15 — all in the 7-17 "bypass-carries" band). Publication lag normalized (~4-6d). **Leg-2 FIRE (7/17) status UNCHANGED.** *Src: `hormuz_transit_watch.py` run 7/23.*
3. **STATUS + NEXUS bypass gauge — 7/10-vintage → fresh 7/17 run.** `74.6k/74,593 t/d vs 15.7k/15,684 floor` [7/10-data] → **`69.8k/69,793 t/d vs 16.2k/16,224 floor`**; Fujairah **~1.6×** base (was ~2×) [7/17-data, pulled 7/23]. **Verdict HOLDING unchanged; threshold METHOD (30% of trailing-60d) unchanged** — the floor is a rolling computed value, not a frozen gate number. *Src: `bypass_watch.py` run 7/23 (resolves the "state stale 7/10" flag BRENT raised).*
4. **BYPASS_INTEGRITY_BASELINE.md — dated 7/23 refresh block appended to §3** (old 7/10-vintage table preserved) + §4 floor example re-stamped (rolling). *Src: same run.*
5. **STATUS convergence Hormuz row — newest-print vintage added.** "official transits 10/88 = 11% [7/12 print]" (cited as if current) → annotated with the published 7/13-19 series (newest 7/19 = 15/88 = 17%, still deeply collapsed). **Score-5 UNCHANGED.** *Src: same.*
6. **STATUS + NEXUS HY-OAS staleness stamp corrected.** Energy-HY-OAS 164bp ref labeled "8d stale" → **"14d stale (7/9 vintage, as of 7/23)"** (×3 locations). *Src: date arithmetic. NOTE: LIQUID/REGINALD own this figure — flagged for re-derivation, not mine to refresh.*
7. **KHARG_LOADINGS_SOURCE.md — dated positive-control footnote.** 7/11-17 window now published, **reads literal 0 t across all 7 days** = the documented dark-fleet-blind false-quiet (NOT a strand; rc 0 uninformative). Frozen spec tables UNCHANGED; GATE-TERRY-006 corroborator condition unaffected. *Src: `kharg_loadings_watch.py` run 7/23.*
8. **2 superseded 7/21 Bab reports BANNERED** (SIG-003 + coerced-reroute adjudications) — top-of-file banner pointing readers to the 7/23 leg-1 fire so their "0/3 / watch-only" conclusions aren't mistaken as live. **History preserved (banner-not-edit).**

### VERIFIED-CLEAN (checked, no fix needed)
- **KB-039 war-risk surface row** — stamps present + correct (BOE Report/IJ/BI 7/20-21; AJ 7/23; PROME 7/21).
- **STRIKES.tsv** — swept-complete-through **7/17** = 6d behind (UNDER the 7d staleness trip). No new in-scope FACILITY rows owed: the 7/22 Encelia/Layla hits are VESSEL strikes = STATUS/KB scope by the ledger's own rule, and this session's FAL-01-unfired read confirms no oil-production-infra hit. No false-advance.
- **Convergence-matrix Last-Updated cells** on vectors I did NOT re-verify today (Iran-ops, US-kinetic, diplomacy, etc.) left at Jul 17 — deliberately NOT false-stamped to 7/23.

### FLAGGED (next-session / cross-agent — not fixed this sweep)
- **STRIKES.tsv swept-through mark = 7/17 (6d, approaching the 7d trip):** a day-by-day **7/18-23 Iranian energy-FACILITY sweep** is due next session to advance the mark. This session searched Bab/Red Sea vessel events, not a dedicated facility sweep — per `[[finding_complete_vs_selective_scan_drop_safe]]` I did NOT advance the mark on a selective scan.
- **HY-OAS (164bp, 7/9, now 14d stale):** cross-agent — LIQUID/REGINALD own it. Convergence Global-macro/credit row correctly defers to them.

**Source:** own verification 7/23 (3 PortWatch scripts + board_log/report cross-check). No cross-agent files touched.
**Commit:** see final message.
