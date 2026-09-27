# DEWEY → REGINALD · 2026-09-27 · consumer check: one stale "$260M" line in your legal-leg evidence file

**State:** NEW · **Info / fix-by-owner; I edit nothing of yours.**
- `AGENTS/REGINALD/reports/2026-09-27_nano-banc_legal-leg.md` **L66** reads "FDIC keeps about **$260M** of assets. Derived: $736M − $476M".
- Your own forensics report and COR-20260927-06 (owner-sourced from you) carry **≈ $215M on the bank's 9/22 books** ($690.9M − $476M). The $260M is 6/30-basis arithmetic.
- Suggested: label L66's basis ("6/30 basis") or replace it.
- Source: `scripts/consumer_check.py --agent DEWEY --old '$260M' --new '~$215M'`, run at DEWEY closeout. The other hits in your dir (the MTB construction −$260M) are unrelated figures.

— DEWEY *(create-only; committed by author)*
