# WILL QUEUE — Things Only You Can Do

**Updated:** 2026-03-25 23:00 UTC

**Purpose:** Canonical list of tasks that are blocked on Will's direct action. Prome surfaces these **batched at check-in**, not as they arrive. Items stay here until done or explicitly dropped.

**Exception:** If a WILL_NEEDS item is blocking a 🔴 time-sensitive proposal, Prome flags it immediately.

---

## Active

### W-001 | 🟡 | D-003 (LIQUID KB backfill)
WHAT: ABS trust trigger proximity analysis — which specific subprime auto ABS trusts are closest to early amortization triggers?
WHY: Requires Bloomberg/servicer report access — agents can't pull this data.
BLOCKING: CARL's credit transmission analysis (ABS → consumer DQ cascade)
ADDED: 2026-03-26

### W-002 | 🟠 | D-007 (RED adversarial refresh)
WHAT: Verify NDFI $1.54T methodology/source — is the FFIEC Q4 2025 figure accurate or inflated?
WHY: RED flags this as potential falsification-level data error if estimate is off by 30%+. We're using it as primary bank thesis number.
BLOCKING: Confidence in BROCK's loss scenario estimates ($37B-$150B range depends on this base)
ADDED: 2026-03-26

### W-004 | 🟡 | D-008 (FORGE refresh)
WHAT: Backfill entry thesis for 16 new positions in ACTIVE_TRADES.md (especially APO $95P Dec $1,185, CF $130C $1,167, ARES $95P $803)
WHY: Agents don't have entry dates or thesis context — only Will knows why these were opened.
BLOCKING: ACTIVE_TRADES completeness (entry thesis = how we evaluate exits)
ADDED: 2026-03-26

### W-003 | 🔴 | D-007 (RED adversarial refresh)
WHAT: APO Apr 17 puts — roll to Jun/Jul or take profit? IV spiked post-gate news.
WHY: RED flags highest urgency. -55%, 22 days to expiry. Gate news confirmed thesis but time decay is killing the position. Needs Will's judgment on roll vs cut.
BLOCKING: Position management
ADDED: 2026-03-26

---

## Format

```
### W-[NNN] | [Priority] | [Source]
WHAT: [One line — what Will needs to do]
WHY: [Why an agent can't do this]
BLOCKING: [What work is waiting on this]
ADDED: [date]
```

---

## Categories of "Only Will"

| Type | Examples |
|------|---------|
| **Eyes** | Read a brokerage screenshot, check a chart pattern, verify a physical document |
| **Hands** | Execute a trade, log into a site, pull data from an authenticated source |
| **Judgment** | Position sizing, risk tolerance call, thesis conviction check |
| **Access** | Credentials Will hasn't shared, paywalled content, personal contacts |
| **External** | Send an email, make a call, post something public |

---

## Completed

| ID | What | Completed | Outcome |
|----|------|-----------|---------|
| — | *None yet* | — | — |
