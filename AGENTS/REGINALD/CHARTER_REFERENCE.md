# REGINALD — Charter Reference (cold half of `CLAUDE.md`, read on demand — NOT a boot read)

*Split out of `AGENTS/REGINALD/CLAUDE.md` on 2026-11-16 (DOCKET L810 and L889 item 5, READ_CAP hot/cold split; class C4: no authority, route or threshold moved). Each section is **verbatim** from `CLAUDE.md` at commit `02d4345664`; crc32 is of the bytes between the markers (R2 without its trailing blank lines). The hot charter keeps a one-line pointer per section.*

## §1. Cleanup provenance (was the line under **Domain:**)

<!-- REF R1 begin crc32 df967f63 -->
**Cleanup:** PROME accepted; READS registered (`55cfb3982`). Review→`inbox/processed/2026-10-20_from-PROME_cleanup-review-accepted-reads-registered.md`. The 10/20 move hold was **lifted by Will 2026-10-22 14:11 ET**; retirements → `archive/RETIREMENT_2026-10-22.md`. Originals→`archive/2026-10-20_organisation-cleanup_CLAUDE.md` §§B01–B13; map/CRCs→`reports/2026-10-20_organisation-cleanup/RECEIPT.md`. Re-check any append or 2026-11-20.
<!-- REF R1 end -->

## §2. Hidden CRE methodology (was § HIDDEN CRE METHODOLOGY; read before any MI3 / RCON2746 / FFIEC CDR work)

<!-- REF R2 begin crc32 3f285686 -->
## HIDDEN CRE METHODOLOGY (Original Discovery) — ✅ COHORT RE-RUN SHIPPED 2026-08-13

Banks hide CRE exposure in C&I via FFIEC Schedule RC-C Memo Item 3 (RCON2746). **Canonical numbers, method, and every caveat now live in `reports/2026-08-13_MI3_cohort_rerun.md` (14 banks × 4 quarters, 56/56 rows at the FFIEC primary, both bases) + `workbook/MI3_COHORT.tsv` (machine-readable) + `scripts/mi3_cohort_screen.py` (reproducible).** Do not restate per-bank ratios here — one source of truth per metric; this section keeps only what a reader must know *before* opening them:

1. **Two bases, always report both.** `v1` = Memo3 ÷ item 4 (legacy, kept for continuity against v1-vintage records). `v1a` = Memo3 ÷ (item 4 + item 9) = the numerator's OWN stated parent, and **the only basis valid for cross-bank claims** — item-9 share of the base runs 5.5%→65.8% across the cohort, so **the basis choice inverts the rank** (WAL is #1 on v1 and #3 on v1a; EGBN is #4 and #1).
2. **`37.6%` (OZK) is KILL-ON-SIGHT** — no reproducible provenance at any quarter. But 4 of the 5 legacy cells reproduce to 2 decimals at the 12/31/2025 vintage, so it is a **single-cell data defect**, *not* a screen-level one. The screen-level defect is item 1's denominator.
3. **"Item 4" and "item 9" are CONCEPTS, not MDRMs.** FFIEC 031 filers (foreign offices — CFG/MTB/HBAN/FLG/VLY/AMTB here) report **RCFD** series and do **not** print the item-4 or item-9b totals; a naive `RCON1766` screen returns `None` for them, which reads as "no hidden CRE." The script resolves by fallback chain and records the MDRM chain used per row. **Zero ≠ unknown ≠ not-applicable** — a reported `RCON2746 = 0` (SBCF, AMTB) is data; a missing part is never coerced to 0.
4. ⚠️ **Scope fence, V1a ≠ V1:** MI3 = CRE *not secured* by RE. Secured books (WAL office + the $99M life-science credit, OZK RESG) are a different object and untouched by any of it.
5. **Instrument:** FFIEC CDR **REST + JWT** (header is literally `Authentication:`; a 403 is a WAF/UA block — use `curl`, don't debug the token). Creds `FORGE/tools/market-data/.env`, **JWT expires 2027-01-31** (renewed 2026-11-01; was 2026-11-05).

Masking taxonomy (extend-and-pretend, mark-to-model, classification) and bucket-migration mechanism stand; old per-bank ratios do not. Metropolitan example/numbers→charter archive HIDDEN CRE. Re-run above governs.

---
<!-- REF R2 end -->
