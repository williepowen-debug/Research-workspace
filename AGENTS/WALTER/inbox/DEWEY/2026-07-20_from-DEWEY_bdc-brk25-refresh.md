# DEWEY → WALTER handoff — BRK-25 print-hunt REFRESH (update to an already-routed report)

**State:** NEW · **From:** DEWEY · **Date:** 2026-07-20 · **Type:** REFRESH (not a new report)
**Flag:** REQ-DEWEY-20260702-012 (Batch-2 #16) — the SAME flag routed 7/16; this is a 4-day incremental, Will-directed
**Report (addendum appended):** `AGENTS/DEWEY/output/2026-07-16_bdc-brk25-print-hunt.md` → see **REFRESH ADDENDUM 2026-07-20** at the end

> **Context for routing:** prompt 16 was already executed 7/16 (High-confidence no-fire; you routed it, handoff in `processed/`). The prompt file had never been moved to `processed/` so it resurfaced in DEWEY's queue; Will asked to run it, DEWEY caught the dup and did a **targeted 4-day refresh** instead of a duplicate fan-out. The orphaned prompt is now `git mv`'d to `processed/`. **You may not need to re-route** — if you already routed 7/16, this is an FYI update; route only the delta below if useful.

## The delta (verdict UNCHANGED — BRK-25 still does NOT fire)
1. **No new arms-length sub-90¢ loan print 7/16→7/20.** MFIC sale still unresolved (0 merger/strategic EFTS hits, no filing since the 6/23 distribution cut; next catalyst MFIC Q2 **8/6**). No Q2 tender finals filed yet (all pending to August).
2. **Fitch gap CLOSED** (the 7/16 report's #1 completeness hole) — and it found **2 in-window Fitch actions the original missed:** FSK cut to **junk BB+ on 4/9**; Fitch **7/13 peer review** = 3-of-13 negative outlooks (FSK confirmed; other 2 unnamed), 10 stable, 12 IDRs affirmed. **Agency opinions, NOT prints — they corroborate, don't fire.** Sweep completeness now Med→High; **S&P is the one remaining uncovered agency.**
3. **MFIC listed discount widened** 0.716×→**0.695×** ($9.60). Illustrates `[[finding_terms_volume_lead_price_private_structures]]` — terms/volume/opinion all deteriorating; the arms-length loan-mark print BRK-25 needs still hasn't happened (price-only watch under-firing by design).

## Routing (DEWEY suggestions)
| Recipient | Why | Disposition |
|---|---|---|
| **BROCK** | BRK-25 owner — no-fire holds into the 7/25-28 marks; Fitch/FSK now covered; forward flags: MFIC Q2 8/6, Q2 tender finals (Aug), any S&P action. | ACTION (update) |
| **NEXUS** | PRED-27 — Fitch now adds FSK (junk 4/9 + neg-outlook 7/13) to the Moody's GBDC/BXSL cluster; recognition still at opinion/terms level, not the print. | info |
| **REGINALD** | BDC/PC stress surface — Fitch sector "deteriorating," PC default rate 5.8% TTM. | info |

*Refresh: direct pulls only (EDGAR + rating-action search + live price), ~6 tool calls, no fan-out. Stubs written to BROCK/NEXUS/REGINALD. Per README: DEWEY only CREATES here; WALTER owns the `git mv`.*
