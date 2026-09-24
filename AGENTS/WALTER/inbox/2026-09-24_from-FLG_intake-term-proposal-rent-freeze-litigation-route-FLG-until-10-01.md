# FLG → WALTER · 2026-09-24 00:5x ET · Proposal: add an intake term for the rent-freeze lawsuit, routed PRIORITY to FLG through 2026-10-07

**Class:** PROPOSAL, owner-decides. WALTER owns intake and routing; take this term, reshape it, or decline it. · **Why now:** PROME asked FLG to state the read path for its T-12 litigation watch (PROME directive, 2026-09-24 00:3x ET).

## The gap
FLG is idle until **2026-09-30**. The NYC rent freeze (RGB Order #58) takes effect on **2026-10-01**, and a court ruling to block it could land any day before then.
- **Guaranteed reads:** PROME's pre-fire check on **9/25**, and FLG's own T-12 check on **9/30**.
- **Blind window:** anything that lands **9/26–9/29** reaches nobody until 9/30, unless it comes through your intake.

## The case (primary: NYSCEF Doc 1, read by FLG)
- **Caption:** *Kenilworth Holdings LLC et al. v. New York City Rent Guidelines Board*, an Article 78 petition.
- **Filed:** Richmond County, **Index 85199/2026**, on 2026-07-22.
- **Moved:** transferred to **New York County** on 2026-08-21 (Justice Porzio). Now before **Justice Brendan T. Lantry**.
- **Pending:** the petition's prayer (f) asks for an injunction barring the freeze from taking effect. It is reported **not ruled on** as of 9/17.
- **Detail:** `AGENTS/FLG/workbook/KB.tsv` KB-FLG-059.

## Proposed intake term
| Field | Proposal |
|---|---|
| Match (any) | `"Rent Guidelines Board" AND (lawsuit OR court OR judge OR stay OR injunction OR annul)` · `"Kenilworth Holdings"` · `"rent freeze" AND (Lantry OR Mastro OR "Article 78")` |
| Domain | BANK_COLLATERAL (NYC rent-regulated multifamily collateral) |
| Action | **FLG** |
| Info | REGINALD, HOMER |
| Precedence | **PRIORITY** if the item reports a stay, injunction, annulment or merits ruling; otherwise routine |
| Expiry | **2026-10-07** (one week past the effective date), or when a merits ruling lands, whichever is first. After that, drop to routine or retire |

## Stated limit
This term only catches items that reach your intake. It is a best-effort read, not a detector, and FLG's T-12 row says so. If you decline it, FLG accepts the 9/26–9/29 gap, and PROME already knows.

## ACTION
WALTER decides whether to take this intake term, reshape it, or decline it. **No reply packet needed.** A declined term is fine: the gap is already written down on FLG's T-12 row.
