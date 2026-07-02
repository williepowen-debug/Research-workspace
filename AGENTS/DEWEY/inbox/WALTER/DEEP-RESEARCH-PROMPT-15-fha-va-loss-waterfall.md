---
request_id: REQ-DEWEY-20260702-011
from: PROME (Will-directed batch 2026-07-02 — fleet-mined slate; WALTER logs + routes, see AGENTS/WALTER/inbox/2026-07-02_from-PROME_dewey-batch2-13-prompts.md)
to: DEWEY
created: 2026-07-02T04:00:00Z
state: NEW
flag_trigger: T3 (load-bearing-but-thin)
originating_evidence: "Whether 2022+ FHA/VA negative equity translates into bank/GSE loss-given-default (vs being absorbed by FHA/VA insurance) is unresolved and is the key open question for REGINALD" (AGENTS/DEWEY/output/2026-06-27_housing-distress-inflection.md — DEWEY's own recommended follow-up). Three miners converged (WALTER+DEWEY-followups+CARL).
clusters: Path C housing→banks / BANK_COLLATERAL / servicer plumbing
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv (WALTER logs row at next boot, disposition QUEUED)
run_order: 11 of 13
deliver_by: 2026-07-14 (before ~Jul-16 bank Q2 prints; REGINALD bank-transmission WAITING-FOR open)
---

# DEEP-RESEARCH PROMPT 15 — FHA/VA loss-absorption waterfall + Ginnie nonbank-servicer stress map

**Decision question:** Does Sun-Belt FHA/VA housing distress transmit to tradeable bank/GSE/servicer credits REGINALD can position on, or is it federally insurance-absorbed (kill/reroute the channel)?

**Materiality gate:**
- **(a) What a cheap verify can't answer:** the waterfall spans HUD MMI actuarial reports, VA guaranty/loss-mit policy, Ginnie Mae issuer advance rules, and per-servicer DQ/liquidity evidence (SEC filings for public names, rating-agency servicer reports for private ones) — an assembly job across federal program mechanics no single source documents end-to-end.
- **(b) Consequence:** REGINALD's housing→bank residential-collateral leg lives or dies; decides whether a Ginnie-advance-drain leg enters Path C scoring before Q2 bank earnings; names the exposed servicers; informs CARL's foreclosure-inflection read.

## `/deep-research` prompt (paste-and-go)

> When 2022+ Sun-Belt FHA/VA thin-equity vintages default, who absorbs the loss — and does the channel reach tradeable credits? IN-BOUNDS: (1) Loss waterfall from primaries — FHA MMI fund claim mechanics + current capital ratio (latest HUD FY2025 annual actuarial report), VA 25% guaranty + 2025-26 loss-mitigation policy after VASP termination, Ginnie Mae issuer advance obligations/buyout mechanics (MBS Guide, APM memos), and exactly where bank/GSE LGD can arise (bank-portfolio FHA holdings, non-reimbursable servicing expenses/curtailments, GSE exposure); (2) servicer stress map across Lakeview/Bayview, Freedom Mortgage, Mr. Cooper (COOP — note Rocket acquisition status), Carrington, PennyMac (PFSI): latest FHA DQ, advance/servicing-expense trajectory, liquidity posture and covenants (SEC filings for public names; KBRA/Fitch/Moody's servicer ratings, bond docs, Ginnie issuer data for private names) — rank the weakest link; (3) whether the FICO-580 student-loan-defaulter cohort is feeding FHA DQ (FHA policy + DQ composition evidence, 2025-26). DELIVERABLE: verdict — federally insurance-absorbed (kill/reroute REGINALD's residential-collateral leg) vs transmits to named bank/GSE/servicer credits (Ginnie-advance-drain leg enters Path C scoring), plus weakest-servicer ranking. OUT-OF-BOUNDS: bank warehouse-line counterparty mapping (answered Apr-14 in-repo — lands on Apollo/Atlas SP, do not redo); GSE CRT deep-dive; FL condo/insurance overlay (CORAL's); re-litigating the national foreclosure inflection call (6/27 report); trade construction. TIMEFRAME: policy/data as of mid-2026, DQ series Q4-2025→latest. ENTITIES: HUD/FHA, VA, Ginnie Mae, Lakeview/Bayview, Freedom Mortgage, Mr. Cooper/Rocket, Carrington, PennyMac.

**On return:** hand back to WALTER via `AGENTS/WALTER/inbox/DEWEY/` naming flag REQ-DEWEY-20260702-011; WALTER routes as a `research-output` signal (→ REGINALD action / CARL, CORAL, RED info) and closes the ledger row.
