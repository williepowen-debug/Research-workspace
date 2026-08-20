# BOND → PROME · 2026-08-19 (~22:xx ET) — tasking 3: VX-18 FHLB test EXECUTED (the report was out, and the trigger fired)

**The classification question you fenced never arose: the Q2 FHLB Combined Financial Report is PUBLISHED (8/13; Combined Operating Highlights 7/30) — not unfetched, not not-yet-published.** Pulled the Operating Highlights PDF from the OF primary and extracted it locally.

## The test, on the spec as written 8/18

| Leg (pre-registered) | Bar | Measured | Verdict |
|---|---|---|---|
| Re-arm condition | next quarterly CFR published | **pub 8/13** | **MET → vector RE-ARMS** |
| Trigger leg A | advances +15% Q/Q | **+10.4%** ($734B [3/31] → **$810.7B** [6/30], OF primary) | not met |
| Trigger leg B | single-bank spike news | **FHLBank Pittsburgh $36.8B [YE25] → $77.7B [6/30] = +111% in H1** [med-conf: 2 independent wire copies of its own 7/23 release; 10-Q unread] | **FIRES** |
| Escalation | >$900B system-wide OR depletion narrative | $810.7B (11% below); no narrative | not met |

**⇒ VX-BND-18: 1 → 2 🟡 WATCH, RE-ARMED** — on the trigger's letter, not on discretion. NOT →3 (neither escalation leg met). **The vector sits OUTSIDE the composite by construction — composite untouched at 12/35.** No label move, no threshold change, no new prediction: an existing registered trigger fired on published evidence.

**The substance:** a **+20% H1 system build "resulting primarily from an increase in advances to large members"** (primary's own words), with one bank doubling, at ~19% below the SVB-era ~$1.0T peak (was ~30% below at the 7/1 baseline). This is a bank-funding-demand datum, not yet a stress datum — **the discriminator is WHY large members are borrowing, and that is REGINALD's lane: packeted** (`AGENTS/REGINALD/inbox/2026-08-19_from-BOND_fhlb-advances-...md`), which also reverses the 8/18 dormancy coverage-reduction notice I sent them.

**Records:** `KB-BND-140` (new, ACTIVE, Stale_By 11/30 = ahead of the Q3 CFR); `KB-BND-067` flipped STALE → **SUPERSEDED** on its FHLB leg by 140 (its MBS leg stays merely stale — no MBS pull tonight, VX-17 stays dormant). STATUS new-coverage line updated; SCRATCH queue item closed. Parked items honored: no TIPS idle-wait, no v1.1.4, no P3, no CDS.

**One honest limit:** the Pittsburgh figure is the trigger-firing datum and it is **wire-sourced** (two independent copies of the bank's own release — issuer-consistent, but not the 10-Q). It moved a watch-tier score, which that confidence supports; anything above 2 on Pittsburgh specifically would need the 10-Q or REGINALD's read.

## COMPLETION — BOND — 2026-08-19 (tasking 3)
STATUS: ✅ DONE
CHANGED: workbook/VX.tsv (VX-18 1→2 RE-ARMED), workbook/KB.tsv (KB-140 added; KB-067→SUPERSEDED), STATUS.md (new-coverage line), SCRATCH.md, AGENTS/REGINALD/inbox/ packet (carve-out ①), outbox/(this memo)
RESULT: Q2 CFR was published (8/13) — no unavailability classification needed. System advances $810.7B at 6/30/26 (+20% vs YE25, +10.4% Q/Q, driver "large members" per OF primary); Pittsburgh +111% H1 fired the pre-registered single-bank-spike leg → VX-18 1→2 🟡 RE-ARMED; +15% Q/Q and both escalation legs NOT met ($810.7B is 11% below the $900B line). Composite unchanged 12/35 (vector outside it by construction).
GAPS: Pittsburgh attribution unread at its 10-Q (wire-sourced, med-conf — sufficient for watch-tier, capped there); MBS leg of KB-067 not refreshed (VX-17 stays dormant, out of tonight's scope).
WILL_NEEDS: None.
FOLLOW-UP: REGINALD owes the why-are-large-members-borrowing read (packet sent). Next BOND FHLB read: Q3 CFR ~mid-Nov, or earlier on any REGINALD flag / system >$900B.
