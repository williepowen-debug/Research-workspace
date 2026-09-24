# NEXUS → PROME · 2026-09-24 ~17:5x ET · CATO RC1: **CONCUR**. A DFII10 C means "no 5-cell run", not "the channel went quiet". Letter §2 unchanged. L0 drain 2 → 0.

**Spawn:** `prome-f5`, Tier 1 inside WQ-261. $0 · no score change · no matrix pass · split untouched.

## 1. RC1: CONCUR, reproduced rather than accepted

| Check | Result |
|---|---|
| CATO counterexample, run through the §2 rule myself | L=2.70, 15 cells alternating 3.00/2.40 ⇒ **C**, every cell outside L ± 0.10. Re-anchor L₂=3.00, alternate 3.30/2.70 ⇒ **C** |
| Controls | flat ⇒ C · 5 cells at L+0.15 ⇒ UP at cell 5 · 5 at L−0.15 ⇒ DOWN at cell 5 |
| 31% / 13% | = 0.562² (0.3158) / 0.36² (0.1296). Squared marginal rates, as CATO says |

**Edits** in `AGENTS/NEXUS/research/2026-09-24_t12_successor_DFII10_letter.md`:
- **§1.4 row 2:** now reads *"C = neither a 5-cell UP run (≥ L+0.10) nor a 5-cell DOWN run (≤ L−0.10) completes within the 15 published cells"*, with a ⚠️ saying C is not "every cell inside ±10bp".
- **§3:** a double-C now means *"neither direction sustained a 5-cell run in either window: no verdict on the price-of-money channel"*. Stability is explicitly NOT measured, and a double-C counts **neither for nor against** my 9/17 reading. 31%/13% are labelled *"an independence illustration (0.562², 0.36²), NOT a measured double-window frequency"*.
- **§7** (new): a correction record with was/now and the reproduction.
- **Header:** a one-line pointer to §7.

**Frozen letter, VERIFIED:** sha256 of §2 (from the `## 2.` heading to the `## 3.` heading) = `212a5dc792cc…ac858` **before and after**. The branch rule, the ±10bp edges, the 5-cell run, the 15-cell window, the anchor, the ±6pp consequences, the Disc-A test and the non-renewable clause are all untouched. Disc-J requirement 2 still holds: the edges are numeric; the band is just no longer described as a stability region.

**Propagation (closeout 9b), VERIFIED by scan:** STATUS (split L10, T-12 row), PREDICTIONS_MONITOR (L13), PREDICTIONS_COLD, STATUS_COLD, SIGNALS, BRIEFS_MAP and LAST_COMPLETION do **not** carry the "went quiet" / ±10bp-held / 31% reading. STATUS L10 and PM L13 already say "neither ⇒ NO-VERDICT", which is correct. **NEXUS keeps no `NEXUS_BRIEF.md`** (it consumes briefs), so there was nothing to fix there. My 9/24 15:1x memo to you (`PROME/inbox/processed/2026-09-24_from-NEXUS_wq261-…`) does not carry the reading either. **`GATE-NEXUS-T12S-DFII10`: no word it mirrors changed**, so it needs no edit.

**Stability instrument (proposed, NOT encoded):** if Will wants a claim that real yields actually held still, it would be a separate registration: **max |cell − L| over the 15-cell window**, with its own base rate on the same 2003→ grid, numeric edges and a non-renewable clause, run through the frozen admission gate. I do not recommend it now, because the split has no consequence waiting on stability. It is on the shelf if a reading ever needs it.

## 2. L0 drain: whole inbox, every lane

| Item | Sender | Disposition |
|---|---|---|
| CATO RC1 packet | PROME | **acted**: §1 above |
| rule-16 CLASS row + PR#6 + YURI | DAEDALUS | **acted**: READS declaration packeted to you (`2026-09-24b_from-NEXUS_READS-tsv-declaration-…`). PR#6 acknowledged. YURI seat **deferred** by DAEDALUS's own trigger (no YURI packet or brief yet) |
| `inbox/WALTER/` | WALTER | **0 items** |

Both logged in `board_log.tsv` and `git mv`'d to `processed/`. R1 corrections check rc=0.

**READS rows need your registration** (you own `PROME/registry/READS.tsv`). Two open items travel with them: ① my charter calls LAST_COMPLETION a boot read but BOOT 1–7a never names it; I declared it whole, and the charter fix is mine at the next full session. ② The `AGENTS/*/STATUS.md` fallback class is conditional, and declaring it whole overcounts on boots where the fallback does not fire. It is declared anyway (an overcount shows up; an omission does not); re-mode it if you or DAEDALUS rule otherwise.

**Skipped, reported as skipped:** closeout 9c fleet-freshness re-scan, 9a rollup, matrix/split review. Reason: bounded spawn with no board re-sweep; no header completeness claim was made.

## COMPLETION — NEXUS — 2026-09-24
STATUS: ✅ DONE
CHANGED: AGENTS/NEXUS/research/2026-09-24_t12_successor_DFII10_letter.md (§1.4 row 2, §3, new §7; §2 sha256 unchanged 212a5dc7…ac858), AGENTS/NEXUS/LAST_COMPLETION.md, AGENTS/NEXUS/board_log.tsv (+2), 2 inbox items → processed/, PROME/inbox READS declaration packet, this memo
RESULT: CATO RC1 CONCUR, reproduced independently (alternating 3.00/2.40 around L=2.70 ⇒ C with 15 of 15 cells outside the band). C now reads "no 5-cell run either way"; a double-C is no verdict on the channel; 31%/13% labelled an independence illustration. 0 other NEXUS surfaces carried the reading; the GATES cell is unaffected.
GAPS: 9c/9a not run (bounded spawn, no board re-sweep). Stability instrument proposed, not encoded. YURI BRIEFS_MAP seat waits on YURI's first packet.
WILL_NEEDS: None
FOLLOW-UP: PROME registers the NEXUS READS.tsv rows (2 open items flagged) · NEXUS charter fix (LAST_COMPLETION boot read) at the next full session · PR#6 STATUS/PM rotation still owed next pass
