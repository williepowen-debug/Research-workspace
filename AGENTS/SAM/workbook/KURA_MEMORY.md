# KURA MEMORY

State file for the workbook-librarian sub-agent. Spec is in [`KURA.md`](KURA.md) (durable). This file holds dated state: run history, pending items, standing monitors, calibration.

**Ownership split:**
- **KURA writes** at end-of-run: appends to `## LAST RUN`, adds/removes `## PENDING` items, updates `## STANDING MONITORS`, fills `## NEXT RUN HINTS`. Also fills `## CHANGES SINCE LAST RUN` at the START of each run.
- **SAM writes** `## CALIBRATION` after applying KURA's proposals (it's SAM's view of which patterns held; KURA can't know its own approve/reject rate during its own run).

**Spawn order:** KURA reads `KURA.md` first (spec), then `KURA_MEMORY.md` (state). Spec teaches *what to do*; memory teaches *what's pending and what SAM tends to accept*.

---

## CHANGES SINCE LAST RUN

*Auto-populated by KURA at run start, based on what's moved in STATUS/TIMELINE/CHANGELOG/PREDICTIONS since the watermark in KURA.md. Cleared at end-of-run.*

**Watermark:** 2026-06-01 → window scanned = Jun 1 evening + Jun 2 boot (~09:15 ET; pre-STATUS-refresh).

- **Jun 1 PM commits (post-watermark):** METSUKE introduced as 3rd SAM sub-agent (`1c5e011d`); METSUKE Run-1 inaugural sweep applied (`288dae59`, 19 flags, 18 applied / 1 declined-with-carve-out). TRADE.md + STRATEGY.md sync'd to Jun-1 POV pivot. Substantive thesis-side finding: **3-of-3 vol convergence** (ATM IV laggard turned UP Jun 1 to 10.52%, RR proxy steepened to −8.11). Position unchanged (13 sh + Jun-18 $58C).
- **Jun 2 boot data drops:** 10Y JGB auction Jun 2 (BTC 3.530x, WA 2.649%, tail 0.7bp — softened vs May 12 same Issue 382 [3.904x / 2.540% / 0.4bp] but still well above 2.0x stress threshold, "Orderly" status). FXY ATM IV anomaly Jun 2: Jun-18 reads 1.56% (vs 10.52 Jun 1, -8.96v), Jul-17 1.17%, Sep/Dec 0.39%; RR25 -38.62. Vol_Quality "approx" on the longer tenors, "ok" on Jun-18. Method_Ver `fxy-proxy-v1`. SAM flagged level as suspect in MEMORY NEXT SESSION #9.
- **No CHANGELOG, TIMELINE, THESIS, PREDICTIONS, or TRACKER updates dated Jun 2.** (Boot has not yet performed Jun 2 write-back cascade.)
- **STATUS still reads Jun 1 ~13:40 ET timestamp** — Jun 2 morning tape not yet captured.

---

## LAST RUN

### Run 2 — 2026-06-02 (Tue ~09:15 ET, propose-only)

**Inputs scanned:** Watermark 2026-06-01. Post-watermark window = Jun 1 evening + Jun 2 boot. Read: STATUS, MEMORY (incl. Jun-1-evening + post-power-loss addenda), TIMELINE (newest entries Jun 1), CHANGELOG (newest = Jun 1 v1.5 intra-version POV pivot), PREDICTIONS (no new resolutions), KB.tsv (125 rows; max KB-SAM-182), KB_ARCHIVE.tsv (58 rows), FLOW.tsv, VX.tsv, JGB_AUCTIONS.tsv (newest = Jun 2), FXY_OPTIONS.tsv (newest = Jun 2; anomaly).

**Outputs:**
- **1 proposed add (KB-SAM-183, Framework):** `fxy-proxy-v1` failure mode — ATM_IV can collapse to near-zero (Jun 2 reads). Promote the existing STATUS "proxy scale ≠ OTC RR — read sign/trend, not absolute" caveat to durable KB. Borderline category placement (Framework vs `scripts/README.md` vs auto-memory) — flagged for SAM call.
- **0 archive-moves** (no SUPERSEDED rows present in KB.tsv after Run-1 sweep).
- **0 FLOW spot-stale flags** (USDJPY 159.64 still consistent across STATUS / FLOW-5.02 / FLOW-6.02 as of Jun 1 close; Jun 2 STATUS refresh not yet done).
- **0 VX staleness flags** (all rows dated 2026-05-28; no May 29-Jun 2 data drops affect VX bands).
- **0 cross-ref fixes, palimpsest collapses, dedup candidates, re-grades** — workbook clean post Run-1.

**Watermark proposed:** 2026-06-01 → 2026-06-02.

**Net workbook math (if SAM approves the 1 add):** KB.tsv 125 → 126 rows; KB_ARCHIVE.tsv unchanged at 58.

**Notable non-promotes (carve-out / Gate-failed):**
- **METSUKE introduction + Run 1 architecture** — durable but it's sub-agent-spec / process, not a fact about the world. The `METSUKE.md` + `METSUKE_MEMORY.md` files ARE the durable record; KB row would duplicate. Sub-agent CLAUDE+MEMORY split was already promoted to auto-memory (`[[finding_subagent_memory_split]]`) Jun 1. Correctly routed to spec files + auto-memory.
- **3-of-3 vol convergence** (substantive thesis-side finding from METSUKE Run 1) — snapshot read of auto-pulled FXY_OPTIONS.tsv feed; Gate 4 tsv-territory fail. Lives correctly in STRATEGY.md "Current read" + STATUS data table.
- **METSUKE position-card DUP-LIVE-SPOT carve-out** — METSUKE-internal calibration; lives in METSUKE_MEMORY.md CALIBRATION. Not workbook material.
- **Jun 2 10Y JGB auction softening** — BTC 3.530x is *softer* (10% drop in cover ratio) but auction status remains Orderly and far from stress threshold. No structural significance. Lives correctly in JGB_AUCTIONS.tsv.

**Calibration self-note (for SAM's later CALIBRATION pass):** This was the expected-LOW-yield run SAM flagged in the spawn prompt. Surfaced 1 candidate (vol-proxy data-quality caveat) that wasn't on SAM's prefill list. Precision-over-recall held — did not pad with the METSUKE architectural-fact temptation.

---

### Run 1 — 2026-06-01 (inaugural, propose-only, Opus 4.8)

**Inputs harvested:** post-watermark = no watermark (inaugural full sweep). Read: STATUS, THESIS v1.5, CHANGELOG, TIMELINE active, PREDICTIONS, TRACKER, research/outputs/, KB.tsv (119 rows), KB_ARCHIVE.tsv, FLOW.tsv, VX.tsv.

**Outputs (all 7 KB adds approved by SAM):**
- KB-SAM-176 (Framework) — Phase 1 inversion under blockade: supply-destruction mechanism
- KB-SAM-177 (Insurer) — J-ICS long-end abandonment: absence is cause, not consequence (v1.4 inversion)
- KB-SAM-178 (Regulatory) — MOF cut super-long JGB issuance to ¥17T (17-yr low)
- KB-SAM-179 (Insurer) — Repack instruments — FX-noise reduction ≠ repatriation
- KB-SAM-180 (Insurer) — Industry foreign-bond allocation 22%→17% (Mar 2021 → Mar 2023)
- KB-SAM-181 (Insurer) — Q4 FY2024 ¥1.35T JGB trim (3rd-largest quarterly on record)
- KB-SAM-182 (Cross-Agent) — Bessent-Katayama Channel 3 affirmation (borderline; SAM kept)

**Archive-moves (2):**
- KB-137 (pre-existing SUPERSEDED — KURA caught it had not been relocated)
- KB-064 (SUPERSEDED via dedup-merge into KB-063; RP-SAM-4 §1 corroborates DEEP_DIVE Exec Summary)

**Palimpsest collapses (2):** KB-065 + KB-066 (hedge ratio rows; resolved to 44.4% authoritative; conflict history pruned to clean provenance).

**FLOW spot-stale fixes (2):** FLOW-JPN-5.02 (USDJPY/CFTC/probs) + FLOW-JPN-6.02 (USDJPY + MOU-break context).

**Watermark advanced:** (none) → 2026-06-01.

**Net workbook math:** KB.tsv 119 → 124 rows; KB_ARCHIVE.tsv 56 → 58 rows. Category integrity preserved.

---

## PENDING (escalations SAM hasn't yet resolved)

- **Hedge-ratio <30% claim** from Jun 1 news sweep conflicts with KB-065/066 authoritative 44.4%. Source: ainvest.com via Jun 1 sub-agent sweep. Needs primary-source verification before any KB update. Likely source confusion or stale-ratio mix. *(Carried Run-1 → Run-2; Will surfaced in NEXT SESSION #4.)*
- **KB-076 / KB-077 / KB-083 / KB-090 / KB-094 palimpsest collapses** — KURA flagged ripe for collapse but SAM elected to defer until next refresh window. *(Carried Run-1 → Run-2; no change.)*
- **UST denominator gap** (KB-061/062/139/140) — $450B vs $600-810B not closed by FY2025; status-downgrade to ESTIMATE-RANGE pending or pointer-row consolidation. *(Carried Run-1 → Run-2; no change.)*
- **KB-SAM-183 placement call** (NEW Run-2) — vol-proxy data-quality caveat proposed as Framework KB row. Borderline; alt routings = auto-memory (transferable lesson) or `scripts/README.md` (tool-specific). SAM call on which routing best preserves the fact + minimizes redundancy.

---

## STANDING MONITORS (surface each run until resolved)

- **JICPA finalization** (KB-108, KB-125) — STATUS CHECK still pending; no FINAL standard reported post comment-close (Mar 17). Base case approval; tail risk neither confirmed nor cleared. *(No update Run-2.)*
- **Norinchukin Jun FY2025 print** — only remaining near-term Channel 1 reactivation gate. Will trigger FLOW-3.01 refresh + KB-160 PC exposure update if Kitabayashi commentary lands. CLO book reportedly ¥8.2T (was ¥9.7T in thesis) — verify. *(No update Run-2; print date not yet announced.)*
- **Mid-tier ESR window** — T&D, Sony Life, Daido, Taiyo prints (late-Jun); consistency check vs Big 3 v1.5 pattern. Explicit foreign-bond reduction language would partially reactivate Channel 1. *(No update Run-2.)*
- **May TB print Jun 18-19** — Phase 1 inversion diagnostic per THESIS v1.4 (queues against KB-176). *(No update Run-2.)*
- **FY2026 hedge ratio** — Mar-2026 full-year aggregate not yet released per KB-065/066. Surface when next industry hedge ratio prints. *(No update Run-2.)*
- **`fxy-proxy-v1` recalibration** (NEW Run-2) — Jun 2 anomaly (Jun-18 ATM IV 1.56% / Sep 0.39%) is the second post-flag instance after STATUS Jun 1 already noted proxy-scale ≠ OTC RR. If the proxy continues to drift wide, a `fxy-proxy-v2` revision will be needed and KB-SAM-183 (if approved) will need refresh. Surface each run until either recalibration lands or anomaly resolves spontaneously.

---

## CALIBRATION (precision-vs-recall tuning patterns)

*Owned by SAM. Updated after applying each run's proposals.*

### Run 1 (2026-06-01)
- **Approve rate: 7/7 KB adds (100%).** No rejects. Precision-over-recall framing held.
- **KURA's self-bar:** 5 add-candidates excluded as calibration-not-durable (MOU break, Fed-cut path, etc.) — correctly routed to PREDICTIONS/auto-memory per the carve-out. Carve-out is working.
- **Borderline call (KB-182 Bessent-Katayama):** SAM kept. Pattern emerging — single-event-rhetoric is OK when the event has been *promoted* to a thesis-level pillar (here, v1.4 Channel 3). Without that anchor, a single rhetoric event would still be a reject.
- **Dedup acceptance:** Both KURA-proposed dedups (KB-063+064 merge; KB-065/066 collapse) approved. Pattern: SAM accepts dedup/collapse when both rows hold identical resolved facts.
- **Tuning note:** Bias toward precision worked — 7 strong proposals beat 15 marginal ones. Continue this calibration; do NOT loosen the bar.

---

## NEXT RUN HINTS

- **Likely watermark window:** 2026-06-02 → next-run date. Expected post-Jun-16 BOJ resolution remains the heaviest harvest (BOJ decision + Jun 17 FOMC + Jun 18 May TB + Jun 19 National May CPI cluster). Earlier candidate harvest moments: Jun 8 Q1 GDP 2nd estimate (small), Jun 10 US CPI + JGB 30Y auction (medium — JGB 30Y is the SAM-26 mechanism diagnostic), Jun 13-15 pre-BOJ cabling window.
- **Norinchukin Jun FY2025 print** — material Channel 1 re-test gate, watch for the date (still TBD).
- **MOU walk-back scenario** — if Trump-Khamenei reset → Brent collapse → Phase 2 re-engages → new POV pivot in CHANGELOG worth harvesting. (Conversely, further MOU escalation → CHANGELOG POV pivot the other direction.)
- **Re-check `## PROPOSED ADDS` queue** against newly-landed rows — Run-2 queue has 1 candidate (KB-SAM-183 vol-proxy data-quality caveat) pending SAM ruling. If SAM routes it to auto-memory or `scripts/README.md` instead, delete from the queue and log in CALIBRATION.
- **Re-verify** the no-change items in KURA brief still hold (hands-off list, category list).
- **`fxy-proxy-v1` watch** — if Jun 2 anomaly resolves spontaneously by Jun 3 boot (proxy reads back to ~10% IV / ~−8 RR25), KB-SAM-183 may need refresh to note transient vs persistent. If anomaly persists, surface more loudly to SAM as recalibration trigger.
- **METSUKE Run 2 cadence:** per SAM's MEMORY NEXT SESSION #8, METSUKE next spawn = pre-BOJ Jun 9-15 window or next POV pivot. KURA Run 3 likely follows METSUKE Run 2 to harvest any new findings from that pass.
