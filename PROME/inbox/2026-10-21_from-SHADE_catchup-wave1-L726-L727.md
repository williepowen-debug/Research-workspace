# SHADE → PROME — catch-up wave 1: L726 and L727 delivered as proposals; inbox 5 → 0

**From:** SHADE (PROME spawn prome-56; Claude Code; model Opus 5.5; repo `/home/willi/Research-workspace`, branch master). **Written:** 2026-10-21T22:17 ET. **Desk commit:** `07531f341`.

## What landed

| Item | Result | File |
|---|---|---|
| **DOCKET L726** — illiquidity basis | Exact criterion: an ABS holding counts as illiquid only with a cited **Transfer** record (Schedule D-1-2 Restricted Asset Code `R`, or a documented sale restriction), **Redemption** record (fund-dependent paper with no redemption right, or >7 days, or discretionary) or **Executable-market** record (SEC 17 CFR 270.22e-4 seven-day standard). Pledge/lending codes (`C`, `CF`, …) go to a separate encumbrance companion, never illiquidity. Unknown rule: holdings split into Confirmed / evidenced-Liquid / Proxy / Unclassified; **RED only if FLOOR >30%, NOT RED only if CEILING ≤30%, otherwise INDETERMINATE** with break-even dollars; proxies never grade; no fund look-through on top of carrying values. DLIC FY2025 illustration (no grade): **9.75%–32.50% → INDETERMINATE**; a breach would need **$9,295M** of confirmed-illiquid ABS (89% of the book), clearing needs **$1,146M** evidenced-liquid (11%). 30% unchanged; no retrospective regrade. | `AGENTS/SHADE/research/L726_ILLIQUIDITY_BASIS_2026-10-21.md` |
| **DOCKET L727** — TSR method | **TSR stays UNAVAILABLE**: the creator's formula is (investments + ceded reinsurance, both "higher-risk/less-transparent") ÷ surplus, but the category definitions are proprietary, the 2019 category set does not map to the 2026 statutory blank, and the creator's own arithmetic does not hold (8,300% ⇒ 1.2% write-down, not 1.6%). Proposed instead: **SHADE-R v1** (all ABS + affiliated bonds + affiliated stock + Schedule BA, exact NAIC 2026 lines) ÷ surplus and **SHADE-T v1** (Schedule S Part 3 Section 1 affiliate rows: reserve credit col 9 + modco reserve col 14) ÷ surplus (Page 3 Line 38). Never summed, never called TSR, no bands. Nothing computed yet. | `AGENTS/SHADE/research/L727_TSR_METHOD_2026-10-21.md` |
| Inbox drain (whole, every sender) | **5 → 0**: PROME 10/15 WQ-364/WQ-422 packet **acted** (ruling recorded on STATUS §0m ① and the W1 calendar row); SIG-W-20261015-005 noted; -015 acted; -20261019-003 info-only; -20261021-028 (FEMA/Florida, arrived 22:11 ET mid-session) info-only. board_log +5; `consume:SHADE` in the commit. Corrections COR-20261015-15 APPLIED, COR-20261015-05 NO-OP; check rc 0. | `AGENTS/SHADE/board_log.tsv`, `registry/corrections_receipts.tsv` |
| Owner write-back | STATUS re-stamped, §0t added; §0r/§0o/§0n + old bottom lines rotated verbatim (crc32 `11d53b30`, verified) → STATUS 22,642 B; SCRATCH rewritten; NEXUS folded last; MAINTENANCE entry. | `AGENTS/SHADE/STATUS.md` etc. |

## Rulings for Will (PROME registers the WQ rows — SHADE does not)

1. **L726:** adopt the GA-matched definition and unknown rule prospectively; keep >30%; no retrospective regrade. Sub-choice: accept or strike the **agency-category liquid rule (L1)**. SHADE recommends **adopt + accept L1**.
2. **L727:** keep TSR UNAVAILABLE; adopt SHADE-R v1 and SHADE-T v1 as named diagnostics without thresholds; reject a labelled R + T sum. SHADE recommends **yes / yes / reject the sum**.
3. Both imply a charter wording change to Key Ratios #2 and #4 — a ratio-definition change, so Will-gated; SHADE edits its charter only after the word.

## Skipped or not run (named, with reason)

- **`T-SHADE-01` not re-assessed** — outside this spawn's task list; the 10/15 NOT MET is a dated reading. HY 331 [10/16] completing >320 ×3 is not a 280 crossing, so no fresh sign-leg read was obliged by the charter.
- **Retirement scan not re-run** — reused the 10/12 closeout determination. **MEMORY rotation (98% of budget)** and the rest of the 10/23 owed list (PREDICTIONS.tsv / declared-flat TRADE / thesis falsifier, ARI DEFM14A, SVO count, NB5–NB7) **not worked**.
- Raw sources fetched this session (NAIC 2026 instructions, eCFR, creator essay/book, ARC deck) kept in session scratch only, not committed; URLs + SHA256 are in the research files. TheTSRratio.com did not resolve (DNS) — UNKNOWN, not proof of absence.
- No auto-memory written; no consumer_check run (no figure superseded — proposals only).

## COMPLETION — SHADE — 2026-10-21
STATUS: ✅ DONE
CHANGED: AGENTS/SHADE/research/L726_ILLIQUIDITY_BASIS_2026-10-21.md, AGENTS/SHADE/research/L727_TSR_METHOD_2026-10-21.md, AGENTS/SHADE/{STATUS,SCRATCH,NEXUS_BRIEF,MAINTENANCE}.md, board_log.tsv, registry/corrections_receipts.tsv, archive/STATUS_ROTATED_SECTIONS_2026-10-21.md, 5 inbox files → processed/
RESULT: L726 exact illiquidity test + floor/ceiling unknown rule delivered; DLIC FY25 reads INDETERMINATE 9.75%–32.50% (breach needs $9,295M confirmed-illiquid ABS, clear needs $1,146M evidenced-liquid). L727: TSR stays UNAVAILABLE; SHADE-R v1 / SHADE-T v1 proposed with exact NAIC 2026 lines. Inbox 5→0, 2 corrections receipted, STATUS 26,298→22,642 B.
GAPS: Nothing computed under either definition (waits on the ruling); T-SHADE-01 not re-assessed; rest of the 10/23 owed list and MEMORY rotation not worked (outside this spawn's task).
WILL_NEEDS: Rulings on L726 (adopt + L1 agency rule) and L727 (TSR UNAVAILABLE + R/T diagnostics, no sum) — PROME to register WQ rows.
FOLLOW-UP: On YES, SHADE classifies DLIC FY25 ABS and computes R/T v1 on DLIC and AAIA. If WQ-422 Clear Spring documents arrive, the same L726 classification runs on its filing; nothing in L726/L727 changes on receipt.
