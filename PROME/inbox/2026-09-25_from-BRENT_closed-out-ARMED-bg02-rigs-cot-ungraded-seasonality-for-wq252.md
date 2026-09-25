## 2026-09-25 ~11:50 ET — To: PROME (from BRENT, live session brent-f6, Will-directed) — closed out ARMED
**Signal:** BRENT closed out **before** the afternoon prints. **Three items are UNGRADED and owed today:**
1. **BG-02, 17:00 ET** (L329): ARMED. The decision tree is in `AGENTS/BRENT/setups/2026-09-25_BG-02-grade-PREP.md`; modal LAPSE = NOT MET. Your 17:00 re-touch stands.
2. **Baker Hughes rigs** (~13:00): the final BRT-26 print against the frozen 457 (last 452, needs +5). The grading tree, including "no grade off an aggregator alone", is in `AGENTS/BRENT/setups/2026-09-25_Q3-predictions-grade-PREP.md`.
3. **COT #7** (as-of 9/22, ~15:30): `GATE-BRENT-COT-35B` review_by today. Run `cot_grade.py --expect 2026-09-22` against the raw f_disagg file.
Items 2 and 3 must be graded before the 10/2 prints (no stacking).

**Detail:**
- **Input for the WQ-252 sitting (10/06), for the sitting pack:** `AGENTS/BRENT/research/2026-09-25_crack-seasonality/NOTE.md` (commit `9f32d1e5c`). Realised 3:2:1 on EIA spot 2010–25: Nov→Jan median **−10.6%** (12/16 winters down), against the 9/14 forward's −10.3%. So #8 read on a rolling month drifts below $50 on season plus roll alone, and a Dec/Jan read under $50 is not evidence of eased stress. ULSD Dec/Jan are priced flat to Nov, so F1 has no roll step. **Basis caveat:** spot, not the futures the bars are specified on; the shape transfers, the levels do not. Registers nothing.
- **WQ-295 (your packet):** DEFERRED per your timing. I will answer after the BG-02 grade with `CADENCE: WEEKLY` plus a WATCH_FOR list.
- **Also this session:**
  - JWC re-read: NOT FIRED; blocking STALE cleared.
  - Roll artefacts packet to WALTER (-008 relayed).
  - WATT P4 basis answered.
  - HENRY blind-read ASK for BRT-12 (due 9/29); your 6b doorbell was sent.
  - STATUS rotated to 70%.
  - $0; no row or band moved.
- **Closeout claim_check, a flag on YOUR surface (look, don't find-replace):** `PROME/WILL_QUEUE.md:27` reads "2026-09-29 (Mon". 2026-09-29 is a **Tuesday**.

**Source:** BRENT session 09:05–11:50 ET; commits `56be75521` · `f2ec6f370` · `f7bbdc42e` · `9f32d1e5c` · Q3 PREP · HENRY ASK · this closeout.
**Priority:** 🟠 · **ASK of PROME:** carry items 1–3 into your 17:00 re-touch (a desk spawn, or Will's word for a live session).
