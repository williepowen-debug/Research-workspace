# MEMORY.md — HOMER Durable Notes

*Will's working preferences, do-not-touch quirks, and provenance facts that don't belong in STATUS (live data) or LESSONS (mistake patterns). Thin by design — grows only with genuinely durable facts.*

---

## Promotion Provenance

- **2026-07-12:** Promoted from `AGENTS/CARL/sub_agents/HOMER/` to top-level `AGENTS/HOMER/` via `git mv` (history preserved). Will-directed, same-day execution — overrode CARL's own recommendation to wait until the post-7/24 quiet window (compressed review, not skipped; DAEDALUS structural review at `AGENTS/DAEDALUS/builds/homer_promotion/PROMOTION_REVIEW.md`). Case originated from CARL: `AGENTS/DAEDALUS/inbox/2026-07-12_from-CARL_homer-promotion-case.md`.
- Zero live external consumers existed outside CARL's tree at promotion time (verified by DAEDALUS's comprehension pack) — the lowest-risk promotion of the OZK/CORAL/AEOLUS/HOMER precedent set.
- HOMER jumped the ROSTER promotion queue ahead of WAL (Will's explicit 7/12 call, recorded not re-litigated — WAL remains next-candidate).

## Do-Not-Touch / Structural Quirks

- **`workbook/KB.tsv` is FROZEN (2026-07-10)** — parent-era canonical KB, ~65 rows, CARL_ID provenance column intact. Do not append to it; do not renumber it. New rows go to `workbook/KB_LIVE.tsv`. The freeze banner is the row-ID-stability contract — breaking it breaks the delegation provenance CARL's own KB still cites.
- **`state_vectors/corrected/` is a retrieval hazard, not a normal subdirectory.** It holds exactly one withdrawn/superseded SV (SV-HOMER-2026-06-08-01). CARL's old harvest globs (and any future search) do NOT descend into `corrected/` — a valid/live SV must never be filed there. Kept as historical record only; the SV channel itself is retired (see CLAUDE.md).
- **`archive/` holds pre-promotion build artifacts** (GAP_ANALYSIS.md, REPORT.md, SPAWN1_DATA_REFRESH.md, UPDATE_PLAN.md) — Apr-vintage, already flagged in-file as archive candidates by the 7/10 verification pass. Historical record; no action needed unless a future sweep wants to prune further per the Data Hygiene >60d rule.
- **`domain/` exists but is empty** — carried over from the pre-promotion structure, no files as of promotion. Leave as-is; a future session may populate it with research/deep-dives per the original CLAUDE.md's Key Files intent.

## Cross-Agent Facts Worth Remembering

- REGINALD cites the monthly Trepp CMBS-MF print in its own STATUS (its CRE row carried Apr-2026 7.71% when checked 2026-09-29). **Ownership is settled: HOMER primary (promotion ruling); REGINALD cites.** No reconciliation row exists on my docket — this line used to point at one that was never there (dangling pointer, found 2026-09-29). If REGINALD's cited value drifts from `workbook/MULTIFAMILY.tsv`, packet REGINALD's inbox; never edit their file.
- CREED now keeps its own `workbook/` (KB, FLOW, PREDICTIONS; checked 2026-09-29 — the July note that it had none is superseded). The MF seam is unchanged: CREED pulls the whole Trepp print and owns non-MF property types; the MF row is mine (`CREED-T-05`). Check `PROME/ROSTER.md` for CREED's current tier; don't infer it from here.
- **WALTER's RESEARCH-INTAKE lane does NOT fetch homebuilder earnings or the ATTOM monthly foreclosure report** (verified 2026-09-29 with WALTER's own read-only harness: 0 lane hits for Lennar/KB over 6/29–9/28 although both reported). ⇒ **HOMER pulls these itself off per-name / recurring docket rows; never assume "WALTER would have routed it."** Matcher fact: all-caps 2–5 char tokens (KB, NVR, LGI) ARE kept; other ≤3-char words drop.

## Infra — what this box can and cannot reach (as of 2026-09-29)

- **Works:** Freddie `freddiemac.com/pmms/docs/PMMS_history.csv` · Treasury daily par-curve CSV (`home.treasury.gov/...daily-treasury-rates.csv`) · Fannie monthly PDFs (`/media/document/pdf/MMDDYY.pdf`, slow) · ICE First Look pages · SEC EDGAR 8-Ks · attomdata.com.
- **Blocked / failing:** MBA (403 site-wide) · S&P press + spglobal (403 — Case-Shiller must come via a secondary) · miamirealtors.com (empty to curl) · therealdeal.com (403 — use CRE Daily / Yahoo syndication) · FRED CSV (HTTP/2 stream errors; retry `--http1.1`, or use the issuer file).
