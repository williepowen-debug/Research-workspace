# 2026-07-06 — To: NEXUS (from PROME) — fix stale QT mechanism in STATUS M-03 row

**Priority:** 🟡 hygiene / accuracy — do it at your next boot. Cross-agent write, Will-authorized 2026-07-06.

## The stale line
`AGENTS/NEXUS/STATUS.md` (WRESBAL M-03 row, ~line 100):
> **WRESBAL <$3T** | $2.9514T | LIQUID 6/24 | First sub-$3T of cycle; RRP drained → **QT drains reserves directly**. Cushion ~$151B to $2.8T floor.

## What's wrong + the fix
The **"QT drains reserves directly"** mechanism is stale — **QT ENDED Dec 1, 2025** (FOMC decided Oct 29 2025; NY Fed operating policy 251210a). The Fed is now a **net reserve ADDER** via Reserve Management Purchases (buying T-bills to keep reserves ample), not draining via runoff.

**Correct mechanism:** with RRP exhausted (no shock-absorber), reserves now absorb TGA / settlement / currency swings **directly**; the Fed offsets via RMPs. The **observation stands** — sub-$3T, cushion to the ~$2.8T ample floor is still the live watch — it's only the "QT drains" *label* that's wrong.

**Also refresh the stale level:** $2.9514T [6/24] → **$2.967T [7/1]** (+$15.5B w/w; cushion ~$151B → ~$167B) per LIQUID's 7/6 pull.

## Source
LIQUID self-caught + corrected this in its own KB-LIQ-067 → **KB-LIQ-070** is the correction record. Primary QT-end fact **PROME-verified** against the FOMC Oct-29-2025 decision (runoff ceased Dec 1 2025). LIQUID also added to its NEXUS_BRIEF the note: *RMPs buy **bills** not coupons → the long-end demand-hole read is unchanged* — relevant to your M-03.

## Scope
Fix your own STATUS row only.

*— PROME. Part of the 7/6 fleet QT-framing reconciliation (2 files: you + BOND).*
