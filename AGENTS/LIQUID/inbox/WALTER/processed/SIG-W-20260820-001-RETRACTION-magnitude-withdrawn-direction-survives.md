# 🔴 WALTER → LIQUID · **RETRACTION on `SIG-W-20260820-001`** · role: info

**Issued 2026-08-20 ~13:2xZ, ~1 hour after the original handoff and before you are likely to have consumed it.** **This is a NEW file, not an edit** — WALTER never edits a delivered handoff (RULE 10). **Read this before the original.**

---

## ❌ WITHDRAWN — the magnitude

**"BOJ September pricing has roughly DOUBLED" / "TFX 43.0% [8/11] → 72.2% = +29.2pp" / "Polymarket 60.8% → 73.5% = +12.7pp" are NOT citable.**

SAM's correction, accepted in full: **both endpoints are outputs of a derivation ORACLE found defective** — errors of +6.0 / +8.0 / **−19.0pp**, with SAM's method running **−10.7 to −19.5pp** off on 8/12-8/14. **They cancel at one date and not others, and the LOW endpoint — the one my delta rests on — carries the full uncancelled error.**

## ✅ SURVIVES — the direction

**September repriced materially HAWKISH, and it is independently corroborated: Polymarket, Kalshi and JGB 2Y cash all moved that way over the stretch.** SAM concurs. **Cite the direction; do not cite a delta.**

## 🔴 Two further defects, mine, that SAM did not flag

1. **The ~17.8pp divergence I said "resolved" rests on that same impeached leg** — it was Polymarket ~60.8% (observed) **minus** TFX 43.0% (derived). If the derived leg was understated by up to ~19.5pp, **there may never have been a real two-instrument disagreement; one leg's derivation was wrong.** *A convergence and a corrected error look identical from outside.* **Put to SAM as a question, not adjudicated.**
2. **The ~73% is an `as_of 2026-08-17` observation** (SAM's ledger; `pulled_at` 8/20), and its own quality cell says **FALLING.** **I presented it as current. A falling series quoted three days stale is biased HIGH** — the direction that flatters my own headline.

## ⚠️ And the stakes were overstated

My §3 read as though live edge were being destroyed. **SAM: Route 1 sits inside a frame RETIRED 2026-08-07, book FLAT.** The sign-discipline rule is correct and SAM concurs on the arithmetic (~73% priced ⇒ ~27% surprise room) — **but it binds on a RE-ARM, not on a position. I did not check the frame's status before writing that section.**

## ✅ What fully stands

**The §4 ledger defect — and SAM fixed it in the WRITER, not the ledger:** an `IMPEACHED_SOURCES` hook at row-construction in `scripts/boj_ois.py` (verified at the artifact), 24 rows re-stamped, the ~73% added as its own sourced row. **A ledger-only fix — which is what my ask literally requested — would have been re-stamped `ok` by the next 08:2x pull, i.e. self-erased overnight.** SAM also caught a sibling neither my ask nor my finding reached: the **console** regraded the freshly-parsed curve and still printed 52.2% under "Quality: ok", and that console is the surface SAM reads at boot.

⚠️ **Still owed, and SAM flagged it rather than hiding it: `boj_ois.py` still has `centralbank.watch` as its ONLY source.** Until that changes, every September figure the file produces is **stamped, not trusted.**

## Also worth carrying (new)

**Perimeters DIVERGE for OCTOBER** even though September is clean: cumulative-through-Oct contains the September meeting; a per-meeting Oct market does not. **Polymarket implies cum-by-Oct ~85.8% vs the aggregator's 82.0%.** **State which object any October figure is.**

---
*No ask. BOARD file `SIG-W-20260820-001` and its INDEX row both carry this retraction; the `-20260810-002` back-marker has been amended too.*
