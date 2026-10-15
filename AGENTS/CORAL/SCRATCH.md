# CORAL — SCRATCH (ephemeral session handoff)

**Session:** 2026-10-15 ~08:03 → ~08:3x ET (Thu) — **coral-1015**, PROME (`prome-73`) WQ-184 Tier-1 crash-recovery spawn on GATES `GATE-CORAL-MSI-01` review_by 10/15, desktop. Model Opus 5.5 in Claude Code (Agent-tool `desk` spawn; root CLAUDE.md, AGENTS.md, USER.md and the CORAL charter read explicitly). No researchers. Other desks' uncommitted work in the tree (CARL, FERT, HOMER, LABOR, …) untouched; no pull/stash/reset.
**Previous:** coral-a5 (Will's own window, 10/14 evening; doorbelled by PROME 23:56 ET) — **died ~03:08 ET 10/15 with the machine**, no closeout. Before that: 2026-10-09 coral-1009pm (Isaias post-landfall).

---

## CHANGES SINCE 10/9 (what the world did)

- Isaias went post-tropical 10/10; NHC dropped all FL warnings at Adv 15 (10/10 4 AM CDT); last advisory #20 (10/11).
- FEMA: **EM-3655-FL** (emergency, not a major disaster; PA only; 27 Panhandle/Big Bend counties) declared 10/9; also EM-3656 AL, EM-3657 GA. **No Isaias DR anywhere** (OpenFEMA 10/15 12:05Z).
- Parcl stamp 10/15: Tampa 7.21 (high on CORAL's readings), Cape Coral 5.91 again.
- Redfin Sep (snapshot 10/07): Miami 158.9% #1 of 50, widening — on modelled buyers.

## WHAT I DID

1. **Crash residue:** `sources/redfin/redfin_buyers_sellers_FL_metros_snap2026-10-07.csv` VERIFIED against the re-downloaded primary (924/924 rows, 0 diffs) → committed unchanged. **Found coral-a5's committed board_log rows (`0e31ff152`) claiming three write-backs that never reached disk** (STATUS OQ §A EM-3655, RECONCILE line, NEXUS wait) → all three done today.
2. **GATE-CORAL-MSI-01 reading #9 (stamp 10/15, pull 2 08:05:33 ET):** 4-of-5 > 6.00, Cape Coral 5.91 in band ⇒ no rule applies, leg 🟠. Pull 1 mixed-stamp (Tampa 10/14, STALE cache) = not a reading (§ U1, KB -110).
3. **Storm rule S2 NOT met** — NHC adv 14–20 read; OpenFEMA EM-3655 only (EM ≠ DR, no graded county) ⇒ unflagged (§ U2, KB -112). Panhandle S4 context pull (descriptive only, § U3).
4. **Inbox 3/3:** WALTER -035 + -006 (Redfin Sep, § U4, KB -111; correction packet → WALTER on the FL listings columns), PROME brief. `consume:CORAL`.
5. STATUS rows + OQ §A + RECONCILE + BOTTOM LINE updated; old blocks rotated verbatim → `STATUS_DETAIL.md` § U0. CALENDAR (10/15 ✅, 10/22 added). NEXUS_BRIEF (10/15 block; 10/01 block rotated out, git `66746cd28`).

## NEXT SESSION / OWED

- **10/22 MSI-01 reading #10** — single-stamp pull (re-pull if mixed; a STALE Vercel serve regenerates on the next hit); **check OpenFEMA for an Isaias DR naming a graded county (last S2 reading; window to 10/23).** All five > 6.00 = first qualifying re-fire reading (Cape Coral is the swing).
- **Miami discriminator:** MIAMI REALTORS September (Miami-Dade, own basis) — do actual sales fall near the modelled −25%? Until then Miami #1 = model swing.
- **10/16 FL Realtors Sept** (four legs) · Citizens 9/30 month-end + county file (re-run the Panhandle cut; reconcile the Sept round 10,250 vs 10,210 at the primary) · OIR Isaias data call · **10/21 BKU Q3** (rail) · SFBS 10/19 / HWC 10/20 storm commentary (descriptive) · 11/15 falsify grade.
- Carried: SIG-W-20261008-040 Pembroke Lakes Mall (Broward clerk / trust 10-D) · OQ L Wayback residual · Orange County records · PACER spend not authorized · Avidia 10-Q ~mid-Nov · **MEMORY rotation owed before the next append** (none added today).

## OPEN THREADS

- Gate-Basis #2 (MSI-01 page URLs + reading cadence) — Will's letter via PROME; not self-applied.
- INFERRED: Parcl page stamp = UTC build date (§ U1) — a mixed-stamp pull is usually cache, cured by a re-pull.
- Citizens tower figures ($0.842B retention) still a researcher read of a chart image — re-read before citing as CORAL's own.
- MARCO's STATUS Florida line still says "Cat 3 landfall forecast" (landfall was Cat 2) — flagged to PROME, MARCO's file.

## MAIL STATE

`inbox/WALTER/` empty · legacy inbox empty · outbound: CORAL → WALTER correction packet (`AGENTS/WALTER/inbox/2026-10-15_from-CORAL_sig-035-fl-listings-columns-correction.md`, carve-out ①) · PROME memo `PROME/inbox/2026-10-15_from-CORAL_msi01-reading9-s2-crash-recovery.md`.
