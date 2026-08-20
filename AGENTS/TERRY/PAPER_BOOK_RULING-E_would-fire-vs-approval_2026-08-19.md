# PAPER_BOOK RULING-E PROPOSAL — does an approval-gated arm with all objective legs MET auto-log a would-fire row?
**Date:** 2026-08-19 ~21:4x ET · **Owner:** TERRY · **Status:** 🟡 DECISION-READY — Will's word required (WILL_QUEUE candidate via PROME). **$0 at risk in every option; this is a paper-record design ruling.**
**Open since:** 2026-08-13 (USOARM postmortem: *"all legs MET 8/4 13:57 under v3 — whether an approval-gated arm counts as a would-fire row is a design call, not retro-created today"*).
**Letter:** E — next free after `PAPER_BOOK_DESIGN.md` §Decision Logic RULINGS A–D (ranking · capital timing · real fills · partial splits).

---

## 1. The question, and why the spec makes it narrower than it looks

`PAPER_BOOK_DESIGN.md` already rules the general case, twice, in its own words:
- Design decision #1: *"Every card that reaches would-fire state fills the shadow book **independent of the approval gate**."*
- §Decision Logic (open): *"Trigger = would-fire state = all **objective** ZONE-3 gates would pass… The **`Will approves` and `position truth` gates are set aside** — auto-fill is independent of approval."*

So the open question is **not** "does approval block a paper fill" — the spec says NO. It is the narrower GATE-class case `TRY-BRENT-USOARM` exposed: a card whose **pipeline is arm → [Approve] → fire**, where all objective legs pass mid-arm (8/4 12:24, worst-case 26.0% vs ≤33.0; re-confirmed 13:57), the approval never comes, and the arm expires (8/13, day 20). **No row was logged.** Two sub-questions:

- **(E1)** Going forward: does that state auto-log a would-fire row at the timestamp all objective legs first pass on one session?
- **(E2)** Retroactively: is the USOARM row created now, `opened = 2026-08-04 13:57 ET`?

**Why E2 cannot be TERRY's call:** the row feeds `would_fire_90d`, whose **≥6-in-90d gate is Will-pinned** (7/24, "pin the # / defer live salary"). Current distinct count: **3/6**. A retro-row makes it **4/6** — two more would-fires in ~7 weeks would trip the Phase-2 gate. Moving a Will-pinned gate's input is Will's word by construction.

## 2. Options

| | Rule | For | Against |
|---|---|---|---|
| **1 — YES, log + count (spec-literal)** | All objective legs pass on one session ⇒ auto-log, counts in `would_fire_90d`. E2: create the USOARM row (4/6) | Faithful to the spec's own two statements; measures the card-quality question PAT-028 asks; **automates the counterfactual** (USOARM's +45%-mid / negative-at-touch was measured by hand — a paper row marked to close does that for free); makes **approval latency a visible, dated row class** instead of an invisible failure mode (the 9-days-DECISION-READY finding) | Moves the Phase-2 gate input on rows that structurally could not have filled (the card's own text required [Approve]); the 8/13 counter fix's principle was *"an under-count cannot false-trip the gate"* — this adds count |
| **2 — NO for approval-armed GATE-class** | "Would-fire" requires a card that fires on its trigger alone; an arm→approve→fire card logs nothing until approved | Keeps the Will-pinned gate input conservative; "would-fire" keeps meaning "would have traded" | Contradicts the spec's plain text (approval is exactly the gate it says to set aside); **systematically deletes the approval-latency failure mode from the record** — the one USOARM proved is real; PAT-028's counterfactual record loses every card Will passes on, which is the *refusal-calibration* half of the design |
| **3 — LOG, DON'T COUNT (fence the counter)** | Auto-log as row class `would-fire (approval-pending)`, marked to close like any row, **excluded from `would_fire_90d`**; E2: create the USOARM row under this class (count stays 3/6) | Keeps the full counterfactual record AND the conservative gate; consistent with the counter fix's under-count-only bias; reversible — Will can flip inclusion later and the rows are already dated | Two classes of "would-fire" is complexity in a Phase-1 book; the Phase-2 gate then under-measures true would-fire volume, which is the very thing it gates on |

## 3. TERRY recommendation: **Option 3 now, with Option 1 as the flip Will can make at Phase-2 review**

- **Log always** — the record is the product. USOARM's measured counterfactual was the 8/13 session's most useful artifact and it had to be reconstructed by hand; every future one should be a routine `paper_book_mark.py` mark. Fill rule already exists (`PAPER_BOOK_DESIGN` §Fill: ask-for-buys at the trigger timestamp — for USOARM-class, the timestamp all objective legs first pass on one session).
- **Don't move a Will-pinned gate's input by desk ruling** — exclusion-by-default honors both the 7/24 pin and the 8/13 counter principle. The rows carry their timestamps, so if Will later rules Option 1, the count is recomputable retroactively with zero loss (same pattern as the PB-0002 split keeping original `opened` stamps).
- **E2 under Option 3:** create the USOARM row now (`opened = 2026-08-04 13:57 ET`, class `approval-pending`, `will_decision = PASSED` — the arm expired unapproved, which IS the refusal-calibration datum), count unchanged at 3/6.
- Consequence table, stated: Option 3 = count 3/6 · Option 1 = 4/6 (gate trips on 2 more in ~7wks) · Option 2 = 3/6 and the USOARM counterfactual stays a one-off hand measurement.

## 4. What this does NOT touch

The Phase-2 gate number (Will-pinned, 6) · the $1,500/mo tranche · RULINGS A–D · `SETUPS.tsv`/card states · any live position. Encode happens only after Will's word, as a PAPER_BOOK_DESIGN §Decision Logic RULING E + one `PAPER_BOOK.tsv` row (if E2 granted) + a `paper_book_mark.py` counter guard (one-line class filter).

**APPROVAL REQUIRED — Will picks the option (or names a fourth); TERRY encodes verbatim after.**
