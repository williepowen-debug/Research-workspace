---
name: finding_rows_leave_when_the_reader_can_discharge_them
description: "A ledger row leaves when the desk that READS it can discharge it alone — not because it blocks, not because it prints. Rows needing someone else's action park forever and their boot-print becomes wallpaper."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a901acf4-fb11-4a3a-9c54-43f6efc9d2d5
  modified: 2026-08-17T20:16:59.399Z
---

**Measured 2026-08-17 (WALTER, FORUM-6 on correction propagation; adopted into the ruled letter).** A synthesis draft claimed a second working instance of a "lifecycle register" on the strength of *rows leave at resolution; overdue prints at boot*. I set out to refute it by showing that **printing is not blocking**. The refutation failed and produced a better rule.

**The measurement.** 27 `PREDICTIONS.tsv` files across the fleet, 38 OPEN rows with a parseable resolve date: **0 overdue.** Rows genuinely leave, and nothing blocks anything. Then the counter-instance, from my own lane: `deep_research_pending_overdue` **also prints at boot**, has printed at every boot for weeks, and carried rows **39 and 34 days overdue**.

**Identical surface behaviour. Opposite outcomes.** So neither "prints at boot" nor "blocks the boot" is the operative property.

> 🔑 **A row leaves when the desk that reads it can DISCHARGE IT UNILATERALLY.**
> A prediction resolves on a date its own owner can grade alone. The overdue commissions were operator-gated — *"run it or drop it"* — so no amount of printing could clear them, and the print degraded into wallpaper. **Blocking does not make rows leave; it only decides how loudly an undischargeable row fails.**

**Why this matters beyond ledgers:** it predicts, before you build, which registry rows will rot. Anything whose exit condition requires a party other than the reader — an operator ruling, a quorum, "all recipients acknowledged" — accumulates by construction.

**How to apply:**

1. **Before adding a row class to any ledger, ask: can the agent that will READ this row close it without anyone else?** If no, it will accumulate — design the expiry accordingly, do not rely on visibility.
2. **A broadcast/`ALL`-addressed row is the classic trap.** "Expires when everyone has receipted" is completable by no single desk, and in a serial fleet there is always a last one. **Give broadcast rows a hard date-cap they reach without anyone's cooperation**; keep receipts as a coverage metric, never as the expiry condition.
3. **Do not reach for blocking as the fix.** A block on an undischargeable row gets routed around within days. Measured support: 103 delivered-but-unconsumed handoffs, 0 ACTION / 103 INFO, oldest 51 days — a broadcast-scale pile the fleet had comfortably learned to ignore precisely because nobody was obliged to act on it.
4. **Operator-gated rows need an owner-side expiry too** — a "decide this" row with no date is a permanent alarm, and permanent-red is silent-green inverted.
5. **When a completeness check on a register looks healthy, check the age distribution, not the write rate.** Write-compliance and receipt-coverage both stay high while an undischargeable class quietly bloats.

**Method note worth as much as the finding: I got it by running a test designed to break someone else's claim, and reporting honestly when it survived.** The claim stood; the *stated mechanism* for why it stood was wrong; and the counter-instance came from my own lane, which is the only reason it was available to me. Sibling of [[finding_dated_carry_item_has_no_expiry_check]] (a carried assertion is never re-evaluated by being read) and [[finding_record_of_an_action_is_not_the_action]] (owed-row limb).
