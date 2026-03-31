# How Fast Does PE-Insurer Stress Transmit to Banks? (Monoline Comparison Reframed)

## What I Need

A timeline model for PE-insurer stress transmission — not a "run" (FABNs are bullet-maturity, non-puttable, no fast run possible) but a slow-motion funding squeeze that accelerates if the FHLB backstop fails simultaneously.

## What We Already Know (from FABN research — treat as confirmed)

- FABNs are 3-5yr bullet maturity, non-puttable, no investor acceleration. The 2007 XFABN structure (puttable, MMF-held) is dead — though NAIC admits it can't confirm zero XFABNs outstanding.
- **Athene total wholesale funding: $69B** ($30.4B FABNs + $21B FHLB + $18B FABR). Largest single FHLB borrower among insurers at $17.2B in advances.
- **$378B total industry wholesale funding** (FABNs + FHLB) = 106% of capital and surplus, 3x cash holdings.
- ~56% of FABNs mature by YE 2028 = ~$155B refinancing wall.
- In 2007-08, when FABNs froze, **FHLB absorbed 3/4 of the contraction** — insurers substituted frozen FABN funding with FHLB advances. FHLB was the lender of last resort.
- PE-insurer private placements earn +80bps over public corporates, +156bps for ABS. $50B of the $82B industry increase in private ABS is affiliated-entity paper.
- Athene rated A+ (S&P, AM Best). 4-6 notches above IG loss. Everlake downgraded A+→A in May 2024.
- Fed classifies FABS as "runnable money-like financial liabilities" in every FSR since 2023.
- Foley-Fisher, Narajabad, Verani (JPE 2020): 40% of 2007 XFABN withdrawals were self-fulfilling runs.

## The Transmission I Want You to Model

This is NOT the monoline cascade (monolines had guarantees — binary pays/doesn't). PE-insurers have an asset-liability mismatch against illiquid private credit. Different failure mode. The sequence:

```
PC asset deterioration (defaults, markdowns on affiliated ABS)
    ↓
Insurer balance sheet weakens (surplus erodes, RBC ratios decline)
    ↓
Rating agencies put on watch / downgrade
    ↓
FABN market access closes (can't issue new notes at viable economics)
    ↓
$155B refinancing wall hits (56% matures by YE 2028)
    ↓
Insurer turns to FHLB as sole backstop (as in 2007-08)
    ↓
KEY BRANCH: Does FHLB tighten simultaneously?
    → If no: slow squeeze over quarters. Insurer shrinks balance sheet gradually.
    → If yes: no backstop. Forced liquidation of illiquid PC assets into thin markets.
```

## Questions

1. **Reconstruct the monoline timeline with specific dates.** First downgrade watch → actual downgrade → bank writedown announcements → systemic cascade. Total elapsed time from first warning to peak impact. I need this as the speed benchmark even though the mechanism is different.

2. **What are the RBC regulatory tripwires for life insurers?** Specific thresholds:
   - Company Action Level (what ratio?)
   - Regulatory Action Level (what ratio?)
   - Authorized Control Level (what ratio?)
   - Where are Athene, Global Atlantic, and F&G currently vs these thresholds?

3. **When has FHLB tightened on insurers?** The critical variable is whether FHLB acts as backstop (2007-08 outcome) or pulls back (SVB/First Republic precedent where FHLB pulled advances). Under what conditions do FHLBs haircut collateral, refuse to roll, or reduce advance limits for insurance members? Has this ever happened?

4. **How fast does the FHLB-tightens scenario play out?** If FABN market closes AND FHLB simultaneously restricts advances to a PE-insurer with $69B in wholesale funding:
   - What's the timeline from funding loss to forced asset sales?
   - Can the insurer sell illiquid private credit fast enough? (Secondary market for private ABS/middle-market loans is thin — what's realistic liquidation timeline?)
   - Does forced selling by one PE-insurer mark down identical assets on other PE-insurers' books? (They hold the same affiliated paper.)

5. **What's different that could make this faster or slower than monolines?**
   - Faster: no Fed cutting room, oil shock compressing borrower cash flows, NAIC already has SVO re-rating authority, Egan-Jones investigation removing rating cover, cross-counterparty exposure between PE-insurers (F&G holds recoverables from Aspida Re and Everlake)
   - Slower: bullet FABNs give years of runway, insurers less leveraged than monolines, state regulation decentralized (slower to coordinate but also slower to rescue)

## What I Want Back

A timeline model with two branches: FHLB-backstops (slow, quarters) vs FHLB-tightens (fast, weeks-to-months). Specific dates on the monoline benchmark. RBC thresholds with numbers. Assessment of which branch is more likely given current conditions. Cite regulatory sources for all thresholds.
