# ARM-#3 GRADING TEMPLATE — Soft May TIC (releases 2026-07-16 ~4:00 PM ET)
**Card:** TRY-FIRE-004 · **Gate:** GATE-TERRY-ARM3 · **Pre-staged:** 2026-07-16 AM (grade at/after 4pm release)
**Status when built:** PENDING — data not yet released. Do NOT grade off intraday/leaked numbers; grade only the official Treasury TIC release.

---

## ⚠️ WORDING RECONCILIATION (flag — grade the CARD, not GATES.tsv)
- **GATES.tsv ARM3 row says:** "China AND Japan UST **holdings** both down" ← **STALE / WRONG measure.**
- **Card F10 (canonical, red-team patched 7/9) says:** China AND Japan both net **SELLERS in net TRANSACTIONS** of long-term Treasuries, **April vs May 2026 transactions data.**
- **Why it matters:** bare holdings-DOWN fires on **pure valuation** (yields rose in May → mark-to-market holdings fall with ZERO actual selling). That is not a flow signal. **The transactions measure governs.** Flag the GATES.tsv drift to PROME (already in the SendMessage).

## ARM CONDITION (canonical — F10)
**ARM ⟺ China AND Japan are BOTH net SELLERS of long-term U.S. Treasuries in the MAY transactions data** (valuation-adjusted flow, Apr→May comparison). If **either** is flat or a net buyer → **arm-#3 DEAD.**

## DATA SOURCE CHECKLIST (where to read the flow, not the level)
Official release: **home.treasury.gov / ticdata.treasury.gov** — "Treasury International Capital (TIC) Data," May 2026, posted ~4:00 PM ET 7/16.
1. **PRIMARY (flow-clean):** country-level **net foreign purchases/sales of long-term U.S. Treasury bonds & notes** (the *transactions* tables, not the holdings table). Net sales = negative = "net seller." Read China (Mainland) and Japan lines, May vs April.
2. **CONTEXT ONLY (do NOT arm on this alone):** "Major Foreign Holders of Treasury Securities" (MFH) table = month-end **holdings levels**. Valuation-contaminated. Use only to sanity-check direction, never as the arm trigger.
3. Cross-check with **SAM (Japan)** and **ZHAO (China)** domain reads if they publish a TIC flow note — the transactions decomposition is their domain; TERRY grades the arm mechanically once the signed flow is in hand.

## FILL-IN GRID (complete at release)
| Country | Apr net txns (LT USTs, $B) | May net txns (LT USTs, $B) | May sign | Net seller in May? |
|---|---:|---:|---|---|
| China (Mainland) | ____ | ____ | +/− | Y / N |
| Japan | ____ | ____ | +/− | Y / N |

**Holdings (context only — do NOT arm on this):**
| Country | Apr holdings ($B) | May holdings ($B) | Δ | valuation vs flow? |
|---|---:|---:|---:|---|
| China | ____ | ____ | ____ | note if move is yield-driven |
| Japan | ____ | ____ | ____ | note if move is yield-driven |

## GRADE DECISION TREE
- **Both China AND Japan net SELLERS (transactions, May):** → **arm-#3 ARMS.** Consequence: reinforces TRY-FIRE-004 (already armed via arm-#2) — a SECOND live arm; note in card discriminator log + notify PROME. (Card only needs ONE arm to be armed; this is confirmation depth, not a new trade.)
- **Either China OR Japan flat / net buyer (transactions):** → **arm-#3 DEAD.** Card stays armed on arm-#2 alone; log the DEAD grade.
- **FALLBACK — transactions-level granularity NOT available at release** (only MFH holdings posted): → **DO NOT arm on holdings-down.** Grade **arm-#3 = UNDETERMINED**, flag the data-granularity gap to PROME, hold pending a transactions-level read. (F10 fallback rule — never arm on a valuation-contaminated holdings print.)

## POST-GRADE WRITE-BACK
1. Fill this grid; append a dated entry to the card DISCRIMINATOR LOG (TRY-FIRE-004).
2. Update GATE-TERRY-ARM3 state note for PROME (ARM / DEAD / UNDETERMINED).
3. If ARMS → note it does NOT change the trade (card already armed on arm-#2); it deepens confirmation.

**No trade action off this grade without Will [Approve] on the arm packet. TERRY never executes.**
