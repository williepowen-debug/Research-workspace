# POSITION INTAKE — Required for Existing Position Triage

Terry cannot triage an existing position from memory. Fill or paste enough broker truth to answer the fields below.

## Required Fields

| Field | Value |
|---|---|
| Ticker / instrument |  |
| Direction | Long / short / options / spread |
| Quantity / contracts |  |
| Entry price / debit / credit |  |
| Current mark |  |
| Expiry |  |
| Strike(s) |  |
| Current P/L |  |
| Original thesis / source |  |
| Original invalidation, if any |  |
| Upcoming catalyst(s) |  |
| Will's desired action | hold / add / trim / exit / roll / unsure |
| Max additional loss tolerated |  |

## If Any Required Field Is Missing

Terry may give a **conditional** read, but must label it `[POSITION_STATE_INCOMPLETE]` and must not recommend execution. Missing position truth can turn a good roll into hidden over-sizing or accidental doubling-down.

## Existing Position Output

Use a normal trade card, but set:
- **Terry verdict:** `HOLD / TRIM / EXIT / ROLL / ADD / NO ACTION — CONDITIONAL`
- **Data freshness:** include broker truth timestamp
- **Risk:** include current loss if stopped now and max additional loss if held/rolled

---

# TRADE-ASSESSMENT REQUEST — the handoff line (WQ-696, Will 2026-11-16 16:17 ET)

**Ruled:** Will, PROME's chat, 2026-11-16 16:17 ET, verbatim "okay go with option a"; record `PROME/proposals/2026-11-16_wq696-RULED.md`, `PROME/WILL_QUEUE.md` row 696. TERRY's charter is unchanged. This is an intake expectation only.

A finding a desk sends to TERRY **for a trade assessment** carries one line in the sender's own words, covering four things:

| Field | What the sender states |
|---|---|
| Implication | what the evidence implies for prices or positioning (no ticker and no forced direction required) |
| Horizon | over what period |
| Invalidation | what would make that reading wrong |
| Unknowns | what remains unknown |

**OR** the sender writes that the evidence supports no investment implication, and why.

**When the line is absent:**
- TERRY says once, in its answer, that no implication was stated and names the sender, e.g. "no implication stated by <DESK> (packet <id>)". It does not supply one itself (Hard Boundary 3).
- TERRY then answers what it can: instrument, liquidity, price and timing. NO CARD remains a complete answer.

**Unchanged:** every Hard Boundary (3 included), construction rules 14 to 23, every card cap and gate, the $500 per-card default, the X1 sizing gate, and root rule #6. A stated implication is an input to TERRY's assessment, never an approval; Will approves every card (root rule #5).
