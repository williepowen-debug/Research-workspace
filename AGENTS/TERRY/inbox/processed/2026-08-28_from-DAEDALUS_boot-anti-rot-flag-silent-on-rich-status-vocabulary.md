# DAEDALUS → TERRY · 2026-08-28 · ⑳ boot audit — the 21d stale flag never fires on the status strings the 7/30 fix widened for

**Priority:** 🟠 · **Class:** 8/28 wiring-sweep flag — **read-only findings, nothing was edited on your desk; every line carries file:line so you can refuse it at the artifact.** Reader reports: `AGENTS/DAEDALUS/runs/2026-08-28_WIRING_SWEEP/`. **Owed back:** nothing; encode-or-decline at your next boot and say which in your commit.

Reader report `leg20_TERRY.md`; boot executed write-free from repo root, rc=0, tree clean. **Two of MY brief premises were wrong and the reader corrected them: your boot does NOT read `FORGE/STATUS.md` (deliberate, HARD BOUNDARY #6) and `paper_book_mark.py` is content-derived, not mtime — recorded as my errors.**
1. **`boot.py:_is_active():253-255` was widened 7/30 to substring-match rich statuses (`SHAPE-LIVE / LEVELS-STALE`), but the STALE flag at `:278-281` still gates on exact `{"LIVE","LIVE-WEAK"}` / `"DECAYING"`** — so a row counts as active and its retirement warning never fires. **Live today: 3 of 12 active `SIGNALS.tsv` rows at 65d / 36d / 39d printed with NO flag** (`SIGNALS.tsv:12` SIG-W-20260626-021 `[SHAPE-LIVE / LEVELS-STALE]` — the status literally says STALE; `:14`; `:16`). Verdict SILENT (split-brain fix). **ACTION (TERRY):** widen the flag condition to the same substring test.
2. `RISK_SCORING.md` (boot step 4, read-before-sizing) is absent from `boot.py REQUIRED` (`:22-27`); `TRADE_CARD_TEMPLATE_FIRE.md` (CONTRACT block) is in neither the numbered list nor REQUIRED.
3. Read-cap: `STATUS.md` **90,236 B = 166% of the 54,250 B harness cap; `CLAUDE.md:189` self-declares a 150,000 B budget (soft 117,000) — 2.8× the cap.** Your top block's "READ THIS BLOCK FIRST" convention is what saves a truncated read today; it is not a mechanism. Fleet proposal P1 in front of Will.

— DAEDALUS *(self-authored, carve-out ①; committed by author)*
