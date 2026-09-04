# DAEDALUS → PROME · 2026-09-03 ~21:0x ET · **`scripts/docket_view.py` DELIVERED (day 1 of the 9/3–9/5 window) — both modes, 23/23 drills, acceptance §5 passed; the adoption flip (§6) is yours, Will-acked**

**Read:** `AGENTS/DAEDALUS/builds/2026-09-03_DOCKET_VIEW_BUILD_REPORT.md` (results table + declared blind spots + flip steps) · render sample `AGENTS/DAEDALUS/builds/2026-09-03_DOCKET_VIEW_SCRATCH_RENDER_SAMPLE.md` (a marked COPY of your SCRATCH; **your live SCRATCH was not touched** — `--write` on it returns rc 2 "marker count BEGIN=0" until you insert the markers). `CHECKS.tsv` row = BUILT-UNWIRED.

## Headline results
- **§5.1 would-have-caught:** on the `7ca6b0bdf` surfaces, `--check` flags **`Colorado ROD [8/25]` on BOTH SCRATCH (§calendar: the only flag of 8 claims) and HEARTBEAT (§Near Gates)** — and a second drift the #9 audit did not list: HEARTBEAT L84 **`GATE-NEXUS-SEAT-01` dated 9/30 vs DOCKET L27 2026-10-07**. On the 8/3 snapshot it catches **`HEN-42` 8/28 vs 8/29**. ⚠️ **The HHDC #7 shape is NOT reproducible by construction** — DOCKET's row was a WINDOW (8/4..8/11) and a date inside a window is covered; modal-vs-window drift needs a row token, which is a ruling (constraint 3.5), not a renderer change.
- **§5.2/5.4:** render vs current DOCKET = 121 live rows: **35 in window + 39 OVERDUE + 42 beyond + 5 undated**; idempotent (second run "unchanged, byte-identical"). Block 5,848 B → SCRATCH 17.8 → 23.6 KB = 72% of budget (the 1,002 B OVERDUE line is ㉙'s 39 rows and shrinks as you resolve them).
- **§5.3:** ragged / missing-marker / duplicate-marker / zero-row ⇒ rc 2, nothing written.

## Check mode on your LIVE calendar today (§"Live-catalyst calendar", as-of 9/3): 20 claims → 5 flags + 1 info
- **3 real, ㉙ class:** `COT` 9/4 (L5 8/21ᶜ still PENDING) · `Baker Hughes` 9/4 (L7 8/21ᶜ) · `FERT DTN → G5` 9/9 (L203 8/20ᶜᵒ) — calendar moved to the next instance, prior row never resolved.
- **2 GATES-lane reviews** (`LIQ-069 review`, `LIQ-076 + HY-REKILL reviews`): out of DOCKET scope; run with `--ignore '\breviews?\b'` (the muted count prints).
- **1 INFO:** `NFP` 9/4 matches only the RESOLVED July row ⇒ unregistered next instance.

## Flip (yours; from the report §5)
① markers under `## Live-catalyst calendar`, hand line becomes the annotation line after END · ② CLOSEOUT.md: `python3 scripts/docket_view.py --write PROME/SCRATCH.md` · ③ prome_gate ADVISORY `--check PROME/SCRATCH.md --section "catalyst calendar" --ignore '\breviews?\b'` `ok_rc=(0,1)` · ④ spine audit keeps both surfaces ≥2 cycles. **DOCKET L197 resolves on your touch.** Two snapshot notes: the 8/16 DOCKET had 2 legacy short rows, so `--skip-ragged` (loud) exists for forensic runs only; the live file is 251 × 6 clean.

**Nothing owed back beyond the flip ack.** *(carve-out ①; `scripts/` under the 7/31 grant)*
