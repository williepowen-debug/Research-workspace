# BOND Mail / Refresh Protocol

**Purpose:** Standard operating procedure for BOND when processing inbox signals or doing a refresh.

## Normal Refresh Sequence

1. Read `CLAUDE.md`.
2. Read `STATUS.md`.
3. Read this `PROTOCOL.md`.
4. Read `workbook/SCHEMA.tsv` and `AGENTS/VOCABULARIES.tsv` before writing workbook rows.
5. Process `inbox/*.md` only if the task asks for inbox processing.
6. Pull/update relevant data:
   - HY OAS, CCC OAS, IG OAS, DGS2/DGS10/DGS30 from FRED / market-data tool.
   - Auction results from Treasury/FiscalData.
   - Dealer positions from NY Fed FR2004.
   - Issuance from SIFMA / high-quality market news.
   - CDX levels from available market sources.
7. Update `STATUS.md` if state changed.
8. Update `TRADE.md` if state affects supported trades.
9. Update workbook files when evidence/predictions/vectors/flows change.
10. Write outbound signal files only for threshold breaches or cross-agent implications.

## Inbox Processing

For each file in `inbox/`:

| Step | Action |
|---|---|
| 1 | Read full signal. Identify sender, target, priority, claim, source. |
| 2 | Classify: `INTEGRATE`, `LOG_ONLY`, `DISCARD`, or `ROUTE_OUT`. |
| 3 | If factual and relevant, add one KB row with source and confidence. |
| 4 | If it changes a vector, update `VX.tsv` and `STATUS.md`. |
| 5 | If it changes transmission mechanics, update `FLOW.tsv`. |
| 6 | If it creates a cross-domain implication, write `outbox/YYYY-MM-DD_to-[target]_[slug].md`. |
| 7 | Move processed signal to `inbox/processed/`. |

## Outbox Format

```markdown
## YYYY-MM-DD — To: [TARGET_AGENT]
**Signal:** [one-line headline]
**Detail:** [2-3 sentences: what changed, why it matters]
**Source:** [data/report + date]
**Priority:** 🔴/🟠/🟡
```

## Thresholds for outbound signals

| Trigger | Target | Priority |
|---|---|---|
| Treasury auction BTC <2.3 or tail >2bps, especially repeated | LIQUID, ZHAO | 🔴/🟠 |
| Dealer take-down spikes / indirect demand weakens materially | LIQUID, ZHAO | 🟠 |
| HY OAS >350 or HY issuance freezes | HENRY, REGINALD, LIQUID | 🔴 |
| IG issuance freezes or blue-chip deal pulls | REGINALD, LIQUID | 🔴 |
| CDX widens ahead of cash for 2+ weeks | HENRY, LIQUID | 🟠 |
| Credit-equity lead activates while VIX remains complacent | HENRY, VIOLET, PROME | 🟠 |
| Bank funding backstop implied by issuance freeze | REGINALD | 🔴 |
| Public credit contradicts private-credit stress | BROCK, PROME | 🟠 |

## Receipt

After inbox work, overwrite `RECEIPT.md`:

```markdown
# BOND Receipt — YYYY-MM-DD

| File | Action | Why | Workbook rows | STATUS change | Outbox |
|---|---|---|---|---|---|
```
