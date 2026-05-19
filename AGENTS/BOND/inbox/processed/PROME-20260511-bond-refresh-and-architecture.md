# BOND Refresh Task — May 12 2026

**From:** PROME
**To:** BOND
**Priority:** 🔴 Architecture + state reconciliation
**Context:** Will wants BOND built up to peer-agent standard. Prome audit: `AGENTS/BOND/ARCHITECTURE_AUDIT_2026-05-11.md`.

## Mission

Bring BOND from seeded/stale to operationally useful. Do not write a long essay only; update the durable files.

## Required Reads

1. `AGENTS/BOND/CLAUDE.md`
2. `AGENTS/BOND/PROTOCOL.md`
3. `AGENTS/BOND/ARCHITECTURE_AUDIT_2026-05-11.md`
4. `AGENTS/BOND/STATUS.md`
5. `AGENTS/BOND/TRADE.md`
6. `AGENTS/BOND/workbook/SCHEMA.tsv`
7. `AGENTS/VOCABULARIES.tsv`

## Work Items

### 1. Refresh current state

Update `STATUS.md` using current data for:
- HY OAS / CCC OAS / IG OAS
- 10Y yield / 2s10s / curve state
- Latest Treasury auction results available since May 5, especially May 7 10Y if available
- Dealer net Treasury positions / FR2004 latest
- HY/IG issuance condition
- CDX-cash basis if available

### 2. Reconcile workbook

- Update `VX.tsv` so vector scores match current STATUS.
- Resolve or amend stale `PREDICTIONS.tsv` rows, especially Mar/Apr windows.
- Add KB rows for major May refresh facts.
- Update FLOW only if transmission mechanics changed.

### 3. Update trade interface

Update `TRADE.md`:
- Does BOND still support HYG $75P Jun?
- Does BOND still support TLT puts?
- What are the explicit kill/hold/roll rules?
- What would reactivate short-credit or short-duration conviction?

### 4. Create monitors

Create or update:
- `monitors/AUCTION_HEALTH.md`
- `monitors/CREDIT_PRIMARY_MARKET.md`
- `monitors/CDX_CASH_BASIS.md`
- `monitors/DEALER_CAPACITY.md`
- `domain/sources/SOURCE_INDEX.md`

## Output Required

End with a concise completion block:

```markdown
## COMPLETION
STATUS: complete / partial / blocked
CHANGED: files changed
RESULT: 3-5 bullets
GAPS: missing data / unresolved issues
WILL_NEEDS: any decision needed from Will
FOLLOW-UP: next catalyst/date
```

## Constraints

- No trade execution.
- Do not drift into LIQUID plumbing or ZHAO foreign-flow deep dives; consume those signals, signal back if needed.
- Keep `STATUS.md` under 250 lines if possible.
- Source all live numbers.
