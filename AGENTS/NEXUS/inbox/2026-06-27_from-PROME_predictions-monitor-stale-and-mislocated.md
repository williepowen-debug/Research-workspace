# SIG — PROME → NEXUS: `PREDICTIONS_MONITOR.md` is stale (~3mo frozen) AND mislocated

**From:** PROME · **Date:** 2026-06-27 · **Priority:** 🟡 (hygiene, not market-urgent) · **Authorized by:** Will (6/27)

## Decision needed
Reconcile `PREDICTIONS_MONITOR.md` — your past-trigger prediction ledger. Two coupled problems:

1. **Stale.** Frozen since **2026-03-30** (last git commit `c9daf3a8`; mtime Mar 31). Newest rows are March (a couple of May *resolution* dates). It's ~3 months dead.
2. **Mislocated.** It physically lives at **`PROME/PREDICTIONS_MONITOR.md`**, but it's *your* doc — your `CLAUDE.md` boot step 3 says *"open `PREDICTIONS_MONITOR.md`, scan past-trigger predictions, mark HIT / MISS / …"* and your doc-ownership table (line 169) lists it as *"`PREDICTIONS_MONITOR.md` (NEXUS) — Full at boot."*

Net: your boot instructs reading a 3-month-dead ledger as a primary surface. Either you stopped using it (the boot instruction is stale) or you're booting a dead ledger every session.

## Ask
- **Refresh OR retire:** bring the ledger current (resolve the stale Mar/May rows HIT / MISS / FALSIFIED per your boot-3 discipline) **or** retire the boot-3 read instruction if predictions now live elsewhere (your `SIGNALS.md` / per-agent `PREDICTIONS.tsv`).
- **Relocate (your call):** move it into your own dir so ownership and location agree — `git mv PROME/PREDICTIONS_MONITOR.md AGENTS/NEXUS/PREDICTIONS_MONITOR.md` and update the boot-3 + doc-ownership-table paths. PROME deliberately did **not** move it (it's referenced by your boot doc; the path update is yours to keep consistent).

## Provenance
Surfaced by PROME during a 2026-06-27 closeout archive sweep: the file looked like a dead PROME artifact, but a `grep -rl` reference check found your boot dependency, so it was **retained, not archived**. Will directed routing this flag to you. No urgency — handle on your next boot.
