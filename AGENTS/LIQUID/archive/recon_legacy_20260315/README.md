# Recon Legacy — War Day 14 (Mar 15, 2026)

**Archived:** 2026-05-19
**Original dates:** 2026-03-15

## Contents

| File | What it is |
|---|---|
| `RECON_REPORT.md` | Stage 1 recon — stale-data audit and known-unknowns list. Pre-search planning doc that identified 18 stale data points (HY OAS 6 days, Belgium UST 4 months, dealer position 49 days, etc.) and 6 known unknowns to resolve via live search. |
| `RECON_DRY_RUN.md` | Meta-evaluation of the Stage 1 recon prompt structure. Methodology assessment, not live data. |
| `recon_subfolder/STAGE2_FINDINGS_2026-03-15.md` | Stage 2 — actual live-search execution against the Stage 1 target list. Findings on T-01 through T-12 (HY OAS, TIC, FOMC, BOJ, SOFR, DIFC multi-bank, HYG, etc.). |

## Why archived

All Stage 2 findings have been absorbed into `workbook/KB.tsv`:
- T-01 HY OAS Mar 12 → KB-LIQ-006
- T-04 BOJ March hold → KB-LIQ-008
- T-03 FOMC March setup → KB-LIQ-009
- T-05 SOFR Mar 12 → KB-LIQ-010
- T-06 DIFC multi-bank → KB-LIQ-007

KB.tsv is now the durable record; these files are the working artifacts that produced it.

## Methodology value

The two-stage recon structure (Stage 1 audit → Stage 2 live search) is a reusable template for future "I've been stale, what do I need to refresh first" exercises. If running another recon, start from `RECON_REPORT.md`'s structure (stale-data table + known-unknowns list + prioritized search targets), execute with `STAGE2_FINDINGS` structure (per-target findings with key data point, updates made, cross-agent signals).

## Do not restore to top level

The recon-as-document pattern was a one-time exercise during a high-stress window (War Day 14, FOMC + BOJ stacked, HY OAS at 319 = 1bp from LIQ-01 trigger). The current operating model (frequent agent runs, no large gaps per Will's stated direction 5/19) reduces the need for formal recon docs — STATUS / MEMORY / live dashboard pull should keep staleness in check.
