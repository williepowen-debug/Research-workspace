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
| Treasury auction **composition failure**: indirect <56.4% **AND** dealer >13.2% (of competitive accepted) | LIQUID, ZHAO | 🔴 |
| Treasury auction BTC <2.3 **alone** (cover marker, composition intact) | LIQUID, ZHAO | 🟠 — *note explicitly that the mechanism did NOT fail* |
| ~~tail >2bps~~ | — | ❌ **RETIRED 2026-07-28 — UNSCOREABLE** |

> ⚠️ **Thresholds reviewed 2026-07-28.** Two changes, both load-bearing:
>
> **1. The `tail >2bps` trigger is RETIRED as unscoreable.** A tail requires the when-issued yield at the bid deadline and **TreasuryDirect does not publish it** — so a tail-keyed trigger cannot be graded from primaries *by construction*, not merely "this session." This retires the pending `MATRIX_V2_DRAFT` per-tenor tail percentiles too: the problem is the *measurement*, not the calibration. Wire-reported tails are `[med-conf]` and may be recorded in notes but must **never** fire a trigger. *(This exact defect produced a mis-specified falsifier that passed by construction — see THESIS v1.1.3.)*
>
> **2. Grade COMPOSITION, not the headline cover.** A demand hole requires **indirect falling AND dealers absorbing**; a thin cover with intact composition is a *price* concession. Worked example: the 7/27 5Y printed the lowest BTC since Sept-2022 while indirect **rose** with duration and dealers were not stuffed — a marker worth firing 🟠 on, but categorically not a demand hole. Thresholds above are % of **competitive accepted** (the fleet-reconciled denominator), benchmarked to trailing-12 per tenor.
>
> Also unchanged and still true: per GAO the note/bond BTC norm has drifted ~3.0→2.5, so **2.3 sits just under the new structural floor** — read 2.3–2.4 as "below new-normal," not "fine."
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
