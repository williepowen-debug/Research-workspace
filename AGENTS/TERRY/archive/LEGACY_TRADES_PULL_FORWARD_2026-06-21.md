# TERRY Legacy Pull-Forward — Old TRADES Candidate List

**Created:** 2026-06-21  
**Source:** `AGENTS/TRADES/JUNE_2026_CANDIDATES.md`  
**Status:** historical playbook / verification pattern, not an active trade list.

---

## Bottom Line

The old `AGENTS/TRADES/` folder was a proto-TERRY candidate scratchpad. It should not remain a live trade agent now that TERRY owns trade construction.

What is worth preserving is not the stale Feb 2026 ticker list. The useful artifact is the **verification workflow**:

> candidate idea → agent claim → primary-source verification → aggregate-data cross-check → conviction update → trade/no-trade decision.

This is now a TERRY pattern.

---

## Durable Lessons To Keep

### 1. Agent claims require verification

The old TRADES file caught major agent-data errors:

- PSEC PIK claim: agent claim was **35%**, verified value was **8.6%**.
- FSK PIK claim: agent claim was **27%**, verified value was **8.5%**; 27% referred to loans with a PIK feature, not PIK income.

TERRY rule:
- never build a trade card from agent-reported numbers alone.
- cross-check against primary filings, ABS data, transcripts, or source documents before an actionable proposal.

### 2. Trends beat scary levels

The old card-thesis failure was useful:

- card lenders had high charge-offs/delinquencies, but verified trends were improving.
- high-but-improving is usually not a clean put setup unless the market is pricing continued improvement and the next print can break it.

TERRY rule:
- distinguish **bad level** from **worsening trend**.
- a short/put needs deterioration, surprise, or catalyst timing — not just an ugly absolute number.

### 3. Candidate lists are not trade rails

`JUNE_2026_CANDIDATES.md` mixed thesis, verification, candidate ranking, old positions, and action items. That was useful as a scratchpad, but it is not an execution rail.

TERRY rule:
- candidate list = research input.
- trade card = actionable rail with entry, structure, max loss, invalidation, target, time stop, and Will approval gate.

### 4. “Removed / avoid” is as valuable as “add”

The old file’s strongest contribution was killing weak ideas:

- SYF / BFH / AFRM / SC removed after verification showed improving credit or business strength.
- PSEC / FSK removed after data errors.

TERRY rule:
- every reviewed setup should be eligible for `NO TRADE` or `REJECTED` status.
- rejected setups should preserve the reason so the same stale idea does not re-enter later.

### 5. Catalyst timing must survive structure

The old CVNA/KELYA notes had catalyst logic, but modern TERRY must additionally specify:

- option liquidity / spread
- IV / expected move
- strike selection
- max premium at risk
- time stop after catalyst
- no-chase rule

TERRY rule:
- catalyst without structure is not a trade.

---

## Pattern For Future TERRY Reviews

Use this mini-checklist before writing a full trade card:

| Step | Question | Required evidence |
|---|---|---|
| Claim | What is the domain-agent or Will claim? | named source / file / thesis owner |
| Primary verification | Does filing/transcript/source data confirm it? | 10-K/Q, ABS, FDIC, Trepp, transcript, company deck |
| Aggregate check | Does macro/industry data agree or contradict? | Fed/CFPB/FRED/industry data |
| Trend check | Is the metric worsening, improving, or only high? | sequential and YoY direction |
| Catalyst | What forces repricing before expiry/time stop? | date/event/print/default path |
| Structure | Is the expression liquid and survivable? | option chain/price/tape/liquidity |
| Kill reason | What would make this no-trade? | explicit invalidation / counterevidence |

---

## Historical Examples From TRADES

Treat these as examples only. Do **not** treat as active recommendations.

| Example | Historical lesson | Current owner if revived |
|---|---|---|
| CVNA | Subprime-auto “extend and pretend” required ABS + filing verification before trade construction | OTTO/CARL thesis → TERRY structure |
| KELYA | Staffing weakness can be a leading labor signal before claims | LABOR thesis → TERRY structure |
| KRE | CRE stress path bypassed failed card thesis; thesis owner matters | REGINALD/CREED/NEXUS → TERRY structure |
| SYF/BFH/AFRM/SC | Ugly consumer-credit levels were not enough when trends improved | CARL/OTTO → TERRY no-trade review |
| PSEC/FSK | Wrong PIK interpretation killed BDC put thesis | BROCK → TERRY verification gate |

---

## Archive Decision

`AGENTS/TRADES/` remains as a historical source archive only. Live trade construction belongs to:

- `AGENTS/TERRY/` for trade cards, structure, sizing, invalidation, postmortems.
- `PROME/ACTIVE_DECISIONS.md` for non-terminal decision state.
- `FORGE/` only when position/P&L artifacts are explicitly refreshed with broker/Will truth.

Do not launch or revive `TRADES` unless Will explicitly asks for a historical archaeology pass.
