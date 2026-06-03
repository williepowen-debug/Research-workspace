# OTTO — Stale-Intel Punch-List

**Produced:** 2026-06-02 (Phase-3b cross-doc audit) | **Status:** discovery only — *no content fixed yet*

Each row is a rotted/duplicated copy whose live value lives elsewhere. Remediation is deferred
execution (a separate pass). Ranked by behavioral impact — does a stale read make OTTO *do*
something wrong? — not by line count. Resolve at a dedicated content-refresh, marking
`[STALE <date>]` on anything that can't be refreshed rather than carrying it forward as current.

| # | File | Last touched | What's rotted (behavioral risk) | Canonical source |
|---|------|--------------|----------------------------------|------------------|
| 1 | **`TRADE.md`** | 2026-02-16 | **HEADLINE.** Pre-5:1-split CVNA prices (~$343 / ATH $486.89 — post-split spot is ~⅕ that); dead entry/anti-triggers (GT resignation, 10-K delay "beyond Feb 18", "Feb 18 catalyst") — same dead triggers retired from Invalidation in 3a; ALLY "~$37 (need to verify)"; cross-refs to nonexistent `POSITIONS.md` / `PREDICTIONS.md`. A trader reading this acts on a position thesis that no longer exists. | STATUS § THESIS / dashboard; live prices via `FORGE/tools/market-data/fetch.py`; PREDICTIONS.tsv |
| 2 | **`RESEARCH_STATUS.md`** | 2026-02-14 | ACTIVE MONITORING still lists "Carvana **Feb 18** earnings 🔴", "PrimaLend confirmation **THIS WEEK Feb 17**", "First Brands examiner **~Feb 25**", "Tricolor trial **Aug 2026**" (now Oct 19); RESEARCH QUEUE entirely Feb-18-centric. Completed-research index itself is sound but missing post-Feb work (e.g. recon STAGE2 Mar 16). Misroutes "what's next" at boot. | STATUS § CRITICAL TIMELINE (live monitoring); index half stays here |
| 3 | **`workbook/VX.tsv`** | 2026-02-04 (VX-001) | `Current_Value` column Feb-stale (VX-OTTO-001 "6.80% 60+ DQ" vs STATUS 7.1%; statuses last set 2026-02-04). **3-way threshold duplication**: VX rungs ↔ CLAUDE threshold rules ↔ STATUS dashboard. Decide: VX owns the structured registry; current values reference STATUS. | STATUS dashboard (live); CLAUDE § Thresholds (rules) |
| 4 | **`EDGAR_8K_MONITOR.md`** | 2026-03-09 | Watch windows expired (OZK Apr 16, WAL Apr 22-24 passed); "Next mandatory sweep **March 25 2026**" long past; Status table pre-Q1-earnings. Heavy REGINALD overlap (bank 8-Ks are REGINALD's domain). Method is durable; the dated watchlist is rot. | STATUS / REGINALD for live bank state; method stays here |
| 5 | **`workbook/KB.tsv`** | (varies) | `STALE_BY` dates passed (e.g. First Brands row `STALE_BY 2026-04-30`) — the file's own freshness convention is firing and being ignored. | Refresh facts or mark superseded |
| 6 | **`workbook/ABS_ISSUANCE.tsv`, `EXTENSION_PROXY.tsv`** | 2026-04-14 | Script-fed series ~7 weeks stale; `scripts/` not re-run since Apr. (The "remote-inherited Apr 15 scripts" MEMORY follow-up.) | Re-run `scripts/*.py`; verify data sources still resolve |
| 7 | **`workbook/FLOW.tsv`** | 2026-02-04 | `Last_Validated` 2026-02-04 across rows — validation stale even where mechanisms are intact. Low behavioral risk; re-validate dates. | Re-validate against current transmission reads |
| 8 | **`LESSONS.md`** | (durable) | Content fine, but overlaps MEMORY § Feedback + the new § Evidence & Hygiene Conventions (lessons 2/3/7 ≈ `[STALE]` / `[ALLEG]` / date-your-data). Consolidation candidate — pick one home. | MEMORY § Feedback / CLAUDE conventions |
| 9 | **`OUTBOX.md`** | (vestigial) | Deprecated by the messaging overhaul ("HERMES delivers twice daily" is stale); cross-agent routing now goes via WALTER inbox. Decommission candidate — but messaging overhaul is its own workstream; don't patch piecemeal. | WALTER inbox routing (per Closing Protocol step 7) |

## Notes
- **Do not fix content from this list opportunistically** — it's a coherent refresh pass. Items 1–3 carry real behavioral risk (a wrong trade/research/threshold read); 4–9 are hygiene.
- TRADE.md (#1) is the case the `[STALE]` convention exists to prevent — it rotted silently 3.5 months.
- Items 8–9 are *structural consolidation* calls, not value-refreshes — Will-decision before action.
