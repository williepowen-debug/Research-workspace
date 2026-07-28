# BOND SCRATCH — 2026-07-28 (Tue, ~03:00–04:30 ET — boot + full mail drain, CLOSED OUT)

**Purpose:** Ephemeral session handoff. Read at boot, rewritten at closeout. Learnings → `MEMORY.md` / auto-memory; thesis → `thesis/THESIS.md`; live state → `STATUS.md`.

**Session shape:** boot (5 days dark) → live-event override (grade + FROZEN 7Y pre-reg before the print) → Will-tasked **full mail drain, 12 items** → CLOSEOUT.

---

## CHANGES SINCE LAST SESSION (7/23 Thu eve → 7/28 Tue)

**Rates (FRED direct, `fredgraph.csv` — 7/24 is the last full curve print; 7/27 exists only for T10YIE/T5YIFR):**
- 10Y: 4.67 [7/22] → **4.71 [7/23] peak** → 4.69 [7/24]; live ^TNX **4.64** [7/28] on a pre-FOMC bid
- 2Y: 4.31 → **4.37 [7/23]** → 4.33 — **+19bp on the 7/17→7/23 bear leg, biggest on the curve**, then only −4bp back on the crude collapse
- 30Y: 5.15 → 5.16; **29-day run above 5%** (~19% of all 2026 sessions vs 50 days in 2007)
- **DFII10: 2.39 → 2.43 SERIES HIGH — now 7bp from the 2.5 re-arm** (was 11bp)
- **T10YIE: 2.28 → 2.26 → 2.21 [7/27] = −7bp** · T5YIFR 2.27 → 2.24 (band-top drift **reversed**)
- ^MOVE 80.08 [7/23 peak] → 76.82 [7/24] → **77.21** [7/28] · TLT **$83.75** [7/28]

**Credit — the thing I was blind to:**
- **HY OAS 268 [7/22] → 277 [7/23] → 279 [7/24] = +11bp in TWO sessions** out of a nine-session range that never moved >5bp
- CCC 981 → **996** (4bp from 1000) · IG 78 → **80**
- Tranche pull (WALTER -016): BB 157→168, single-B 285→296, index 268→279 — **absolute-parallel, proportionally largest at the TOP** (BB +7.0% > CCC +1.5%) ⇒ broad repricing, NOT quality-sorted
- *My dashboard carried **275 [CONF FRED, 7/2]** for 26 days.*

**Regime read: UNCHANGED and now out-of-sample tested.** Across the ~11% two-session crude collapse (Brent ~$100.50 [7/23] → ~$90.57 [7/27]), **DFII10 held 2.43 → 2.43 (zero) while T10YIE fell −7bp.** The entire rates response ran through inflation compensation; the real/policy leg did not move. Oil shock = breakeven event, not policy-path event — exactly what KB-BND-080/088 predict.

---

## WHAT I DID THIS SESSION

**Pass 1 — Boot + live-event override.** Repo already in sync (0/0). Pulled FRED direct + TreasuryDirect. Found the 7Y prices **today 1PM** and FOMC decides **tomorrow 2PM** → wrote and committed (`7a18ec13`, ~03:00 ET, **~10h pre-print**) `analysis/2026-07-28_grade_7-27-2Y-5Y_prereg_7-28-7Y.md`:
- **7/27 grade off TD primaries** (n=250; 50×5Y, 50×2Y, 49×7Y back to Jun-2022) → **HOLDING-with-a-marker**
- **Claim audit** of the NEXUS/HENRY packets (see corrections below)
- **FROZEN 7Y pre-reg**, keyed on **composition**, **tail-free by construction**, 4 branches + explicit tie-break

**Pass 2 — Will-tasked full mail drain (12 items → all `processed/`).** 6 general + 6 WALTER. Full disposition table in `RECEIPT.md`. Three items carried enough weight for their own KB rows (FOMC odds, HY OAS, basis trade); the rest consolidated.

**Pass 3 — Closeout.** 5 KB rows (089–093), 10 VX rows, STATUS (state line + 11 dashboard rows + matrix + catalysts + BOTTOM LINE), CATALYSTS.tsv, RECEIPT, this file, 2 auto-memories promoted.

---

## THE THREE THINGS THAT MATTER

1. **🔴 FOMC is two-sided and I had it wrong by ~25pp.** My surfaces said "HOLD ~90% priced (FedWatch 7/16) → guidance TONE is the event." Live: **~65% hold / ~34% hike** (10.7% [7/15] → 34.7% [7/22] → 34.3% [7/27]), **forward guidance REMOVED** by Warsh. **At ~1-in-3 the decision is itself the event.** Decision **Wed 7/29 2:00PM ET**, presser 2:30. The 5Y auction priced 48h into this.
2. **🟠 Credit stopped being inert, and my row was plausible-stale.** 275 [7/2] sat between the 263 trough and the real 279, so it read as current every session for 26 days. HY market function **1 → 2**.
3. **🟠 First real cover marker of the cycle — and I conceded a spec error.** 5Y BTC **2.28**, lowest since Sept-2022 (by 0.01). Fired my own pre-registered `BTC<2.3` trigger → **VX-01 2 → 3**, despite having a benign story. **But composition HELD: indirect ROSE with duration (2Y 56.59% → 5Y 59.24%), dealers not stuffed (13.53%, +0.64pp).** Cover thinned, mechanism intact.

**Composite 12 → 14/35.**

---

## NEXT SESSION (dated, future-verifiable)

1. **🔴 TODAY 7/28 1PM ET — grade the 7Y against the FROZEN pre-reg.** Branches A/B/C/D + tie-break in `analysis/2026-07-28_grade_...`. **Do not re-derive the thresholds** — they are frozen. Pull TD `/securities/Note`, compute % of **competitive accepted**. Route the verdict to HENRY + NEXUS (both are waiting on it).
2. **🔴 WED 7/29 2PM — FOMC.** Arm-#2 falsifier live test, frozen at `analysis/2026-07-18_fed-path-map_fomc-7-28.md`: arm BREAKS on 2Y<3.85 **AND** DFII10<2.15 **AND** 10Y<4.35 sustained 3 sessions. **DEEP-LIT against dovish** (2Y 4.33 / DFII10 2.43 / 10Y 4.69). A *hike* is the live tail, not just tone.
3. **🔴 DFII10 → 2.5 re-arm watch — 7bp away.** The nearest live TLT-puts add-gate.
4. **Fri 7/31 — BND-01 resolves FAILED** (HY 350 vs 279). Resolve at closeout on/after 7/31, don't leave OPEN-but-stale. Also BOJ 7/31 (SAM owns primary; FL-BND-11 FX leg).
5. **Mon 8/03 — P3 Batch-3 START GATE** (docketed). Two questions: reserve composition/mobility (reconcile to ONE figure with SAM) + where the **edge** of reserve-currency privilege is.
6. **DEFERRED / OWED:** **FR2004 now 5 prints owed** (6/24, 7/1, 7/8, 7/15, 7/22) — carried 4 weeks, NY Fed API caps pre-2026 in-env; **stop silently rolling this, flag Will/PROME**. · ECB GovC calendar verify from primary. · HENRY UST structural-demand corpus (Mar-vintage).

## OPEN THREADS / WATCHES

- 🔴 7Y today (tiebreaker) · 🔴 FOMC 7/29 two-sided · 🔴 DFII10 7bp from 2.5
- 🟠 HY 279 → 300 watch (21bp) · 🟠 CCC 996 → 1000 (4bp) · 🟠 30Y 29-day run >5%
- 🟡 **Basis-trade hypothesis (KB-092)** — testable at the 7Y: if it's the driver, cover stays thin **with composition intact** and does **not** resolve post-FOMC. LIQUID owns the call.
- 🟡 Auction *tail* is **unscoreable from primaries by construction** (no when-issued published) — every future auction leg must be composition-keyed.
- 🟢 EU peripheral benign (BTP-Bund 83 [7/17], trigger 200) — but the ECB row is a logged owned miss.

## POSITION DECISIONS

- **TLT puts: HOLD, no add.** Will NO-ADD 7/16 stands. **No pre-registered add-gate has fired** — DFII10 2.43 is 7bp short of 2.5. Live re-arm candidates unchanged: (a) DFII10 >2.5 sustained; (b) hawkish FOMC repricing 7/29; (c) a composition-failing 7Y (branch A or D).
- **HYG puts: stay closed** — but credit is no longer inert; reopen only on HY >300 with velocity.
- No new BOND trade rec (scoped).

## MAIL STATE

- **Inbox (general): EMPTY** — 7 consumed → `processed/`.
- **Inbox WALTER: EMPTY** — 6 consumed → `WALTER/processed/`.
- **Outbox:** 2 new — `2026-07-28_to-HENRY_falsifier-was-mine-and-misspecified-plus-you-over-retracted.md` (3 asks answered + over-retraction finding), `2026-07-28_to-NEXUS_727-grade-delivered-holding-with-a-marker.md` (owed grade + 3 corrections).
- **NEXUS_BRIEF.md:** NOT refreshed this session (last 7/23). Stale on the FOMC framing, the credit move and the 7/27 grade — **refresh next session.**

## CLOSEOUT (BOND protocol steps 9–17)

- **9 STATUS:** state line, 11 dashboard rows, matrix (**composite re-summed 14/35**, verified against VX.tsv), catalyst table, new BOTTOM LINE.
- **10 Workbook + PREDICTIONS:** KB-BND-089…093 (+5, CRLF preserved, 13-col validated). VX ×10 (**01 2→3, 02 1→2**). PREDICTIONS DUE-scan: **BND-01 still in-window until 7/31** — nothing DUE this session, nothing left OPEN-but-stale.
- **11 Thesis:** no version bump — evidence accumulation under v1.1.2. The out-of-sample oil→breakeven test (KB-091) *hardens* the 7/18 relabel; the falsifier mis-specification is a **method** defect, not a thesis change.
- **12 Forward state:** CATALYSTS.tsv is source-of-truth and STATUS mirrors the same event SET (7/27 resolved · 7/28 7Y · **7/29 FOMC re-dated off the old 7/28..29 span** · 7/31 BND-01 · 8/03 P3 gate).
- **13 SCRATCH:** this file.
- **14 RECEIPT:** overwritten with the full 12-item disposition + corrections table.
- **15 Promotion scan:** **2 auto-memories promoted** — `finding_claim_outlives_its_discredited_instrument`, `finding_plausible_stale_value_evades_review`. Both fleet-transferable, neither BOND-specific, so neither duplicated into local `MEMORY.md`.
- **16 Mirror-consistency:** STATUS matrix ↔ VX.tsv scores reconciled row-by-row; STATUS catalyst table ↔ CATALYSTS.tsv same event set; PREDICTIONS ↔ STATUS scoreboard (BND-01 OPEN, in-window). Durable docs carry no live values.
- **17 Git:** BOND-only pathspec commits, root cwd; `7a18ec13` pre-print + closeout commit; auto-push via `scripts/safe-push.sh`.
