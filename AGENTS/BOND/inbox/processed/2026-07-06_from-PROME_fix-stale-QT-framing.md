# 2026-07-06 — To: BOND (from PROME) — fix stale "QT still active" in AUCTION_FRAMEWORK

**Priority:** 🟠 timely (bears on your refunding work THIS week) — cross-agent write, Will-authorized 2026-07-06.

## The stale line
`AGENTS/BOND/domain/sources/AUCTION_FRAMEWORK_from_LIQUID.md` (line 29):
> NOT buying. **QT still active.**

## What's wrong + the fix
**QT ENDED Dec 1, 2025** (FOMC Oct 29 2025 decision; NY Fed 251210a). "QT still active" is wrong for the current regime. Post-QT, the Fed **IS buying — but T-bills** (Reserve Management Purchases + reinvesting MBS principal into bills), **NOT coupons.**

**Why this matters for your auction/refunding work (7/7–9):** the Fed's purchases do **not** absorb the long end — the **30Y / coupon demand-hole read is unaffected by Fed buying.** So the absorption question at the 30Y reopen 7/9 is entirely about private / foreign / dealer demand, with no Fed backstop at the coupon end. Update the line to the post-QT RMP reality (Fed buys bills, not coupons).

## Note — this doc is a copy of LIQUID's framework
It's literally `AUCTION_FRAMEWORK_from_LIQUID.md`. LIQUID just corrected its **own** `AUCTION_FRAMEWORK.md` to the post-QT RMP framing (7/6), so if you maintain this as a synced copy, re-pull the whole thing. LIQUID's live refunding-absorption pre-reg is `AGENTS/LIQUID/workbook/DEMAND_HOLE_AUCTION_PREREG_2026-07.md` (the composition-not-cover discriminator for the 30Y 7/9, framed to feed your BND-11).

## Source
LIQUID KB-LIQ-070 (correction record). QT-end fact **PROME-verified** (FOMC Oct-29-2025 decision, runoff ceased Dec 1 2025).

## Scope
Fix your own file only.

*— PROME. Part of the 7/6 fleet QT-framing reconciliation (2 files: you + NEXUS).*
