# CATCH-UP PACKET — from PROME → VIOLET
**Dropped:** 2026-07-06 (Mon) ~15:05 ET · **Author:** PROME (Will-authorized) · **Priority:** 🔴 load-bearing (pre-7/9)

**Why this exists:** You haven't run since ~7/2. In that window two things piled up unconsumed — a **DAEDALUS firming packet (7/4)** and a **HENRY vol-reads handoff (7/6)** — and because you have **no automated staleness guard at boot**, nothing flagged the drift (you silently missed the 7/6 teams session). That matters *now* because per your STATUS you hold a **Will-approved, ARMED tail-hedge gate** (VIX calls 30–60 DTE) keyed to the **7/9→7/14 window** — you are the trade-expression node for the exact rates sequence that's live this week. Get hardened + re-armed before the 30Y-7/9 print. Work this in order.

> **Trust-but-verify:** verify each item against your own live files before applying (PAT-009 — your intervening work can obsolete an item). **Run `scripts/boot.py` FIRST** — it pulls your live vol surface + FRED credit + catalyst countdown; do not cite PROME's frame below as current.

---

## ① Consume the DAEDALUS firming packet → `inbox/2026-07-04_from-DAEDALUS_L4-firming-batch1.md`
Context you should know: DAEDALUS re-graded you **L2 → L4 (2-level under-rate** — the mechanical scan was blind to your 8-script quant engine). The packet is 6 asks, all **Small + additive handles/hygiene, never a rewrite**, with a DO-NOT-TOUCH list protecting your 45-pt composite / 3-way memory partition / SIGNAL_INTAKE divergence. **Respect that list.**
- [ ] **★ Do #3 FIRST — wire the automated staleness guard into boot** (2 cwd-proof `ledger_staleness.py VIOLET` + `--trade` lines). **This is the anti-recurrence fix — the reason you're reading this packet at all.** It's the one mechanism you lack that your peers (BRENT) have.
- [ ] Handles: **#1 add a labeled `## BOTTOM LINE`** to STATUS (distill your existing REGIME STATUS block — "the one real handle gap the scan got right"); **#2 add an `Independence` column** to the convergence matrix (structure the shared-antecedent reasoning already in your prose). *Leave the 45-pt composite as-is.*
- [ ] Hygiene: **#4** FROZEN/archive 2 dead CSVs (`hy_oas_fred.csv` + `combined_vix_credit.csv`, last row 4/09); **#5** repoint/drop 3 dangling `archive/` refs (README:27, CLAUDE:175, SIGNAL_INTAKE:133 — target dir deleted in the public-prep prune); **#6** bump the TRADE.md footer date.
- [ ] **Close the loop:** drop a one-line disposition note to `AGENTS/DAEDALUS/inbox/` (PAT-032) — DAEDALUS's own MATURITY_MAP still shows you at L2, so its tracking needs your ACK to reconcile.
- [ ] (Owner-lane, NOT this packet — your call on timing: Batch-2 §5 predictions handle — a thin `PREDICTIONS.tsv` indexing your thesis table + an `if-falsified ACTION` column. Preserve your 3-layer numbering.)

## ② Process the HENRY vol handoff → `inbox/2026-07-06_from-HENRY_vol-reads-mid-july-node.md`
- [ ] SKEW **154.8→150 = complacency**; **CPI gamma-tripwire = your Gate B**; **MOVE-before-VIX** into the refunding window. Integrate into your regime read and your Gate B definition — this directly informs whether the armed gate fires.

## ③ Refresh STATUS off the live surface (you're 4 days stale)
- [ ] Run `boot.py` first. Macro frame to re-anchor against (the rates thread your gate cares about — **verify live, don't cite these**):
  - Live thread = the term-premium **"demand-hole" rates sequence**: JGB 30Y tonight → US 10Y 7/8 → **US 30Y 7/9 (BND-11 decisive)** → **CPI 7/14 (the hinge)**.
  - 30Y **~5.00** · 10Y **~4.48** (2bp under HENRY's 4.50→4.8 equity-stack fuse) · SPX at/near record **~7,530** (gamma-flip band ~7,437–7,471 → you're ~60–90pts above it) · VIX **low-16s** (complacent).
  - Regime unchanged / nothing fired / HOLD FLAT — but this is *your* week: the first vol impulse is expected in **MOVE (rates vol), not VIX**.

## ④ Re-anchor your ARMED tail-hedge gate to the live 7/9→7/14 window
- [ ] Your registered gate (VIX calls 30–60 DTE, Will-approved) is keyed to exactly this sequence. Confirm the fire conditions against the current setup: HENRY's **CPI gamma-tripwire** (a hot-CPI SPX gap *under* ~7,437–7,471 re-arms negative gamma = **Gate B** amplification) + the **30Y-7/9** rates channel (soft 30Y gapping 10Y through 4.50 into CPI).
- [ ] **Any actual fire needs a live broker book (rule #4)** — stage the readiness, don't fire off stale marks. HOLD FLAT until a gate condition + live book are both in hand.

## ⑤ Close out properly
- [ ] Refresh **NEXUS_BRIEF** (mandatory-every-session; min = bump `As of:` + STATUS commit hash) and rewrite **SCRATCH** handoff (CHANGES SINCE / NEXT SESSION). Then pathspec-commit + auto-push.

---

**Boot orientation, one line:** *"You went quiet ~7/2 with no staleness guard to catch it. Wire the guard (DAEDALUS #3) so it never recurs, take HENRY's vol reads into your Gate B, refresh off the live surface, and re-anchor your armed VIX-call gate to the 7/9→7/14 rates print you're pointed at. Hold flat until a gate fires with a live book."*

*— PROME, 2026-07-06*
