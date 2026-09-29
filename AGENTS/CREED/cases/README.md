# CREED Case Ledger — named CRE distress cases

**Created:** 2026-09-29 · **Owner:** CREED · **Directed by:** Will, 2026-09-29, in WALTER's session, relayed in `inbox/2026-09-29_from-WALTER_cre-case-ledger-will-directed.md` @`dffcb78e0`: *"start trying to track major cases ... search for patterns or other helpful connextions."*
**Not a boot read.** Open it on demand. The read-cap budget doesn't bind it, but keep each file under 32,550 B anyway so it can be read whole in one call.

## What it's for

It holds one row per named distressed property or loan, so connections *across* cases become visible: the same lender, holder or special servicer turning up in different cities; the mix of triggers (tenant exit vs. maturity default); building vintage and loan vintage; time from special servicing to resolution; and loss severity by property type.

## ⚠️ The limit that governs every pattern read (read before counting anything)

**This is a sample of cases that got reported, not a sample of the market.** A case enters because a newsletter, a court filing or a news story named it. That over-weights large, dramatic office cases in major metros, and cases whose outcome is already public. Cases that resolve quietly (a modification, a discounted payoff, a bank loan nobody writes about) are under-weighted.

⇒ **Frequencies computed here measure what gets reported.** "70% of our cases are tenant exits" is a fact about press coverage until it's tested against an aggregate (Trepp / CREFC by trigger, MBA, FDIC).
⇒ **A pattern found here is a HYPOTHESIS with a named test, never a finding on its own.** Write the aggregate that would test it beside it.
⇒ **Never quote a ledger severity as "the loss rate" for a property type.** The same-basis severity distribution is `KB-CREED-041` (CREFC monthlies).

## Rules

1. **One case = one loan on one property.** For a portfolio loan: one case, with the properties listed in `notes`. For senior + mezz on one property: one case, with both loans in `loan_amount_usd`.
2. **UNKNOWN, never blank.** A blank cell can't be told apart from "not checked".
3. **Status carries a date.** `latest_status` is paired with `status_as_of`, the date the status was *true*, not the date we read it.
4. **Every value mark names its basis and date** (appraisal / sale price / net proceeds / tax-assessor value / model value). **Never compare across bases** (root trap #2: a real number on the wrong basis).
5. **Implied loss names its basis** (e.g. "net proceeds vs senior balance, BEFORE servicer advances"). A figure without a basis goes in `notes` as UNRECONCILED, not in `implied_loss_pct`.
6. **Originator ≠ holder.** A lender's name on a loan does NOT say whose balance sheet carries it. `holder_type` stays UNKNOWN until the trust or bank is established. A Ladder-originated CMBS loan is not Ladder's credit loss (the -015 caveat).
7. **Source tier on every row**: `PRIMARY-READ` / `PRIMARY-CITED` / `SECONDARY` / `SEARCH-SUMMARY`. The search-summary tier exists so a figure seen only in a search listing isn't dressed up as read.
8. **Events are dated separately from when they were reported.** `CASE_EVENTS.tsv` carries `event_date` (when it happened; `UNKNOWN` or `≤YYYY-MM-DD` allowed) and `reported` (the source date). Duration statistics use `event_date` only.
9. **The ledger is not a trigger instrument.** No case moves a CREED score, band or trigger by being entered. `trigger_eligibility` states, per case, whether a registered trigger's own rules would count it (e.g. `CREED-T-06`: excludes obsolete/vacant collateral by name).
10. **Other desks keep their cases.** CORAL (Florida), HOMER (multifamily) and the bank desks (WAL, FLG, OZK, REGINALD) own their named credits. A row here cites their record in `fleet_links` and reconciles to their one figure. It never forks a second number.
11. **A case that's dated wrong is the commonest error here.** The -015 video sold a 2025 foreclosure (Houston Gateway I/II) as a 2026 pattern. Check the event year at intake.

## Files

| File | Grain | Role |
|---|---|---|
| `CASES.tsv` | one row per case | current state, identity, loan/holder, marks, fleet links |
| `CASE_EVENTS.tsv` | one row per dated event | the timeline, structured so durations are computable |

**Controlled vocabularies** (extend by editing this list in the same commit):
- `property_type`: OFFICE · MULTIFAMILY · RETAIL · LODGING · INDUSTRIAL · MIXED_USE · LIFE_SCIENCE · DATA_CENTER · LAND · OTHER
- `trigger` (primary first; `+` joins a secondary): TENANT_EXIT · MATURITY_DEFAULT · RATE_RESET · OPERATING_SHORTFALL · FRAUD_OR_LEGAL · SPONSOR_WALKAWAY · UNKNOWN
- `holder_type`: CMBS_CONDUIT · CMBS_SASB · CRE_CLO · BANK · DEBT_FUND · INSURER · MREIT_BALANCE_SHEET · GSE · UNKNOWN
- `latest_status`: WATCHLIST · SPECIAL_SERVICING · DEFAULT · FORECLOSURE · REO · NOTE_SALE · SOLD · MODIFIED · EXTENDED · PAID_OFF · BANKRUPTCY · UNKNOWN
- `event_type`: ACQUIRED · ORIGINATED · LEASE_EXPIRY · TENANT_VACATE · TRANSFER_SS · DEFAULT · APPRAISAL · FORECLOSURE · REO · LISTED · SALE · NOTE_SALE · MODIFICATION · EXTENSION · BANKRUPTCY_FILING · LOSS_REALIZED · OTHER

## Intake

- **Feed:** WALTER proposes tagging every signal that names a specific distressed property or loan with `case:` and copying CREED. The routing change is WALTER's to make under its own spec and `AGENTS/_NETWORK.md`. CREED is only the recipient.
- **Cadence: NONE PROMISED.** CREED is Tier-2 and event-driven. Rows are added when CREED is live, and case signals wait in `inbox/WALTER/` until then. *(The multifamily courier died in 2026-08 precisely because a spawn-on-need desk had promised a cadence. Don't repeat it.)*
- **At intake:** check the event year (rule 11), set the source tier honestly (rule 7), state `trigger_eligibility`, and add the events.
- **The WALTER seed** (`AGENTS/WALTER/research/2026-09-29_cre-case-seed.tsv` + `-NOTES.md`) is a DRAFT built from fleet files only. **Adopt row by row after verification.** Its IDs (`CASE-0001`…) are drafts, and CREED assigns `CASE-CREED-NNN` on adoption.

## Pattern questions: the registered list

Each answer is a hypothesis until tested against the aggregate named beside it.

| Question | Test aggregate |
|---|---|
| Is single-tenant lease-end obsolescence a distinct failure path from maturity default in office? | Trepp newly-delinquent composition (matured balloon vs other), `VX-CREED-3.04/3.05` |
| Same special servicer / originator across metros? | none (the ledger is the instrument, but n is press-sampled) |
| Time from special servicing to resolution, by type | Trepp SS resolution commentary; CREFC |
| Loss severity by type/vintage | `KB-CREED-041` CREFC severity distribution |
| Building vintage (pre-2000 office) vs outcome | CBRE/Avison Young class-split vacancy |
