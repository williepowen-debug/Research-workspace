# `scripts/docket_view.py` — BUILD + ACCEPTANCE REPORT · 2026-09-03 (Thu) ~21:0x ET

**Commission:** PROME 2026-08-16 (Will-directed) · **Window:** Will 9/2 "build the docket view renderer 9/3-9/5" · **DOCKET checkpoint:** L197 (9/5) · **Delivered:** 9/3, day 1 of 3.
**Tool:** `scripts/docket_view.py` (repo-root `scripts/`, DAEDALUS grant) · **Selftest:** `--selftest` 23/23 · **CHECKS.tsv:** row added · **Render sample:** `builds/2026-09-03_DOCKET_VIEW_SCRATCH_RENDER_SAMPLE.md` (a marked COPY of live SCRATCH — the live file was NOT touched; `--write PROME/SCRATCH.md` today returns rc 2 "marker count BEGIN=0 END=0", which is the missing-marker drill on a real file).

## 1. What was built (commission §2, both modes)

| Mode | Behaviour | Guards |
|---|---|---|
| `--write PROSE` | Renders DOCKET's PENDING rows into `<!-- DOCKET-VIEW BEGIN/END -->` in PROSE: stamp line (source · as-of · window · live/in-window/OVERDUE/beyond/undated counts · **docket-crc32 content vintage**) → **OVERDUE** line (every PENDING row dated before as-of, `L# M/D` + ᶜ COVERED-annotated / ᵒ OVERDUE-annotated) → **UNDATED** line (session-keyed rows) → the calendar (bold computed weekday for ≤7d, `M/D` beyond; window rows show `(→end)` or `(since start →end)`; every item cites `(L#)`) → beyond-window count + next row. | ragged DOCKET ⇒ rc 2 no write · zero rows ⇒ rc 2 · 0 or >1 markers ⇒ rc 2 no write · `.tmp`+`os.replace` · idempotent (same DOCKET + same `--as-of` ⇒ byte-identical, reports "unchanged") · `--budget` advisory on block size · `--dry-run` |
| `--check PROSE…` | Extracts dated claims from any prose file (bold day headers set context; ` — `, ` · `, table cells split segments), matches each to DOCKET rows — **an explicit `(L#)` citation is the strongest anchor and is graded against the cited row**; otherwise rare-token overlap (IDs match by containment: `FLG-T08` ⊂ `GATE-FLG-T08`) restricted to rows within ±60d — and flags a claim whose date no matching PENDING row covers. Weekday-vs-date on headers. | never writes · rc 0/1/2 · `--section HEADING` scopes to one section (naming no heading ⇒ rc 2) · `--ignore REGEX` mutes and PRINTS the muted count · a claim matching only RESOLVED rows = INFO "unregistered next instance?", never a divergence · zero matched claims prints its own blind-spot line |

Constraints §3.1–3.7 all encoded (docstring). §3.5: the hand-annotation line sits OUTSIDE the markers (line after END); no DOCKET column added.

## 2. Acceptance tests (commission §5) — results

| # | Test | Result |
|---|---|---|
| 1 | **Would-have-caught (blocking class)** — `--check` vs the 8/16-morning surfaces at `7ca6b0bdf`, `--as-of 2026-08-16 --skip-ragged` | ✅ **SCRATCH §calendar: exactly 1 divergence = `Colorado ROD [8/25]` vs L132 2026-08-30** (8 claims matched). ✅ **HEARTBEAT §Near Gates: `AEOLUS Colorado ROD [8/25]` flagged** (11 claims) **+ a second drift the audit did not list: `delegation-tier grade + GATE-NEXUS-SEAT-01` dated 9/30 on HEARTBEAT vs DOCKET L27 2026-10-07** — PROME to verify which was right. ⚠️ **#7 HHDC shape (98b795d15, as-of 8/3): NOT reproduced by construction** — SCRATCH said "~8/11", DOCKET's row was the WINDOW 2026-08-04..2026-08-11, and a date inside a window is covered; modal-vs-window drift is invisible to date-in-window semantics (declared blind spot, §4). The same run DID flag a real one: **`HEN-42` 8/28 on SCRATCH vs L62 2026-08-29**. |
| 2 | **Reproduction** — `--write` vs current DOCKET (as-of 9/3) | ✅ 121 live rows = 35 in window + 39 OVERDUE + 42 beyond + 5 undated; facts match the hand calendar where both carry the row (PJM →9/8 L249, OPEC+ 9/6 L123, CRMT 9/7 L189, Forum falsifiers L39, renderer checkpoint L197 …). Block 5,848 B; SCRATCH would go 17,799 → 23,584 B = 72% of the 32,550 B budget (under the 75% tier; the 1,002 B OVERDUE line shrinks as PROME's ㉙ COVERED-row reconcile lands). |
| 3 | **Guard drills** | ✅ ragged ⇒ rc 2 + no write · missing marker ⇒ rc 2 + no write (also observed on the LIVE file) · duplicated markers ⇒ rc 2 · zero-row docket ⇒ rc 2 · past-due PENDING above the window · undated + beyond COUNTED · RESOLVED excluded · outside-marker text untouched — all in `--selftest`. |
| 4 | **Idempotence** | ✅ second run: "unchanged — block byte-identical (5,848 B)". |

**The 8/16 DOCKET snapshot carries 2 legacy short rows (L34 = 3 fields, L167 = 5 fields)**, so the strict guard refused it; `--skip-ragged` (loud, snapshot/forensic only) was added for the test. The LIVE file is clean: 251 rows × 6 fields, 6 comment lines.

## 3. Check mode on the LIVE landing target (`PROME/SCRATCH.md` §"Live-catalyst calendar", as-of 9/3)

20 dated claims matched · **5 divergences + 1 info**, classified by hand:
- **3 = PROME's ㉙ class, real:** `COT → GATE-BRENT-COT-35B` 9/4 (nearest L5 8/21ᶜ) · `Baker Hughes` 9/4 (L7 8/21ᶜ) · `FERT DTN → G5` 9/9 (L203 8/20ᶜᵒ) — the calendar has moved to the NEXT instance while the prior instance's row is still PENDING-COVERED and overdue. Resolving those rows (or registering the next instance) clears them.
- **2 = GATES-lane reviews, out of DOCKET scope by design:** `LIQ-069 review` 9/15 · `LIQ-076 + HY-REKILL reviews` 9/30 (they matched L256, which quotes those gate IDs). **Mute with `--ignore '\breviews?\b'`** — the muted count prints every run.
- **1 INFO:** `NFP → LABOR re-ping` 9/4 — only the RESOLVED July NFP row (L117) matches ⇒ unregistered next instance, not a divergence.

## 4. Declared blind spots (say them, don't discover them at audit #10)
1. **Modal-inside-window drift is invisible** (HHDC #7 shape): a window row covers every date in it. Fix would be a `modal:` token in the row or a DOCKET column — a ruling, not a renderer change (§3.5 says don't add columns).
2. **Prose-only catalysts with NO similar row anywhere are unmatched, not flagged** — the check can only diverge from a row it finds. The other direction stays the spine audit's (commission §4 says so).
3. **Precision is token-based**: a row that QUOTES other gate IDs (L256) attracts their mentions. `--ignore` + the printed nearest-row text keep a false flag dismissible in one read.
4. `--check` without `--section` on a whole hot file reads position/dashboard prose as claims (33 flags on live SCRATCH whole-file) — **always scope to the calendar section**.

## 5. Adoption flip (commission §6 — PROME's, Will-acked at delivery)
1. In `PROME/SCRATCH.md`, under `## Live-catalyst calendar`, insert `<!-- DOCKET-VIEW BEGIN -->` / `<!-- DOCKET-VIEW END -->` on their own lines; keep the current hand calendar line as the **annotation line immediately after END** (★ stars + "Read" stay there) or trim it to editorial only.
2. `PROME/CLOSEOUT.md`: replace the hand-maintenance step with `python3 scripts/docket_view.py --write PROME/SCRATCH.md` (rc 2 blocks: fix DOCKET or markers, never bypass).
3. `PROME/tools/prome_gate.py`: add ADVISORY row `python3 scripts/docket_view.py --check PROME/SCRATCH.md --section "catalyst calendar" --ignore '\breviews?\b'` with `ok_rc=(0, 1)` at boot + closeout; HEARTBEAT's hot file is pointers-only post-split, so no HEARTBEAT check until it carries dated catalyst claims again (confirm at flip; the cold half can be checked with `--section`).
4. Spine audit keeps both surfaces for ≥2 cycles as the renderer's external verifier (`finding_freshness_check_cannot_catch_a_fresh_lie`).

**Nothing needs a Will ruling except the flip itself.** DOCKET L197 (9/5 checkpoint) resolves on PROME's touch.
