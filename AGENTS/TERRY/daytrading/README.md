# TERRY — Day-Trading Review System

**Purpose:** A recurring feedback loop on Will's discretionary **day-trading** (separate from the thesis put-book). Will feeds TERRY a trade log periodically; TERRY reconstructs P&L, marks open positions live, scores behavior against the rulebook, and tracks whether the named mistakes are shrinking over time.

**Scope:** Day-trading only. Thesis/position trades live in `FORGE/` + domain-agent STATUS files. Don't mix them here.

---

## The loop (what happens each review)

1. **You feed me a trade log** (see Intake) and say *"Terry, run a day-trading review."*
2. I **reconstruct realized P&L** by instrument thread (cash-flow method) and **mark open positions** against live closes.
3. I **score the session against the 5 rules** in `PROFILE.md` and tally the tracked tendencies.
4. I **append** a narrative entry to `JOURNAL.md` and a metrics row to `LEDGER.tsv`.
5. I **flag repeat mistakes** (same leak two reviews running) and call out what improved.

Heavy lifting (P&L reconstruction + behavior mining) runs as a Terry workflow; the output lands in the three files below.

---

## Intake — how to feed me data (best → acceptable)

- **Best: broker history / positions CSV export.** Captures the two things the activity feed hides — **assignment/exercise outcomes** and **roll strikes/expiries**. Without these, realized P&L is a *range*, not a number. (Session 1 was +$719 to +$3,336 purely because four short options' assignment status was invisible.)
- **Acceptable: pasted activity feed** (what you gave me 6/23). Works, but I mark assignment-gated and roll-book figures `UNKNOWN`.
- Either way, tell me: the **broker**, the **window** (dates) covered, and whether the **market is open or closed** when I pull marks.

---

## Cadence

Ad-hoc / "somewhat regularly." **Weekly or per-cluster** is the sweet spot — frequent enough to catch a repeating leak before it compounds, rare enough that there's signal. You drive it.

---

## Files

| File | What |
|---|---|
| `PROFILE.md` | Living behavioral fingerprint + the 5 enforceable rules. The rulebook. |
| `JOURNAL.md` | Append-only narrative, one entry per review (newest on top). |
| `LEDGER.tsv` | Quantified metrics per review — the trend tracker. |

*TERRY prime directive carries here: if you can't define the loss, you didn't make the money.*
