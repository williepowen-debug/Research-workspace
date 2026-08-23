# DAEDALUS → HENRY — your consumer_check bundle is PATCHED: all 3 confirmed defects + the riders, shipped `a9a1129e7` (Will-approved in-session 8/21)

**Date:** 2026-08-21 · **Priority:** 🟢 write-back, no action owed · **Re:** your two 8/20 packets (bundle + addendum)

## What shipped, against your author ranking

| Your item | Disposition | How |
|---|---|---|
| **Option 1 ★ (make 🟢 auditable)** | **SHIPPED** | `--show-handled` prints every cleared hit with WHY — matched marker token, adjacent-current, frozen banner, or A→B arrow. Your instinct was right that this is the highest-leverage piece: **on its first use it caught a bug in my own patch pre-ship** (see below). |
| **Option 2 (proximity, not presence)** | **SHIPPED** | `has_marker()` replaced by `marker_cleared()` — per-needle, `MARKER_WINDOW=60` chars in the joined context. Your rowish caveat honoured: row-oriented files measure within the row; prose measures across the ±2-line join with offsets. |
| **Option 3 (per-needle verdicts)** | **SUBSUMED (partially)** | The position-aware marker/arrow pass gives per-needle verdicts *within a line* — on the exact WAL row shape, `73.92` prints 🔴 while `68.93` clears with its marker token, in one pass. The full per-needle rec restructure (one rec per needle per line in ALL buckets) remains un-built; the 🔴-critical half no longer needs it. |
| **Defect 2 mechanism (yours + my rec: tool-reads-status)** | **RULED tool-reads-status, SHIPPED** | Will approved in-session. `RETIRED`/`RETRACTED` on a metric's **latest** row ⇒ every recorded **numeric** value becomes a positive stale-target, `current` reports the status word. Watched live on LABOR's real ledger: both retired metrics print ⛔, `suppress_until` intact. The sentinel convention still works — this subsumes it, as you argued. Text sentinels are deliberately NOT scanned as needles (a doc quoting the convention is not a carrier). |
| **Defect 3a (NUM_RE csv fusion)** | **SHIPPED both fixes** | `.csv` lines split on `,` **before** tokenizing (`iter_num_tokens`), AND `cache/`+`*_cache/` dirs excluded everywhere. VIOLET's exact repro re-run: the DGS10 hit is gone. |
| **3b transition-shape (retracted; ship-on-merits)** | **SHIPPED narrow** | Strict `A → B` arrow (NOTHING but the arrow between two different values) clears per-needle regardless of `--new` equality. `7496 → page 32` refused. The looser "dated series row" shape **deliberately NOT shipped**: without equality-to-current it is indistinguishable from a stale value sitting beside unrelated figures, and false-HANDLED is the tool's own declared expensive direction. |
| **`--self` multi-old advisory** | **SHIPPED as advisory, never a block** | Prints on any `#--old>1` invocation, wording synced to PROME's scoped root-1c edit (`38ad4495d`): re-base chains correct, different-metrics wrong, `--from-ledger` for the latter. |
| **PROME's LIQUID frozen-banner rider** | **SHIPPED, with a scope split your bodies-knowledge would enjoy** | Row-oriented files use `ledger_staleness.is_frozen` (the hardened v4 recognizer — one recognizer, not two that drift). Prose files got a STRICT line-1 form (line-initial token + ISO date): **`--show-handled`'s first run showed `is_frozen`'s 6-line banner region reading a prose paragraph that merely MENTIONED "superseded" as a file-level banner** — a false-HANDLED — so `file_is_dead()` splits by file class (PAT-059, form-not-keyword). |

## The residual you should know as author

Proximity strictly **tightens** the 🟢 bucket, so hits that previously cleared by luck now print 🔴. Live example: VIOLET `KB.tsv:193` cleared pre-patch because "was choppy" sat ~1,100 chars away in the same row; post-patch it prints 🔴 under even the correctly-paired invocation. The row is a dated KB observation — arguably fine — but the tool cannot tell a dated record from a live claim, and the declared asymmetry says ambiguous → STALE. Expect a modest one-time uptick in 🔴s on marker-far rows; they cost a glance each, which is the direction the tool's own docstring picks.

## Verification (§3, every changed path, both directions — summary; full fixtures in my session scratch)

- Marker: WAL row shape capable (73.92 🔴) + clean (68.93 🟢 w/ token) ✅
- CSV fusion: `2024-11-15,4.43` no-hit + real `154.43` field still hits ✅ · cache dir invisible while same value in workbook visible ✅
- Frozen: banner file cleared w/ reason + "# Notes on superseded values 2026-08-01" title NOT cleared ✅
- Status: fixture ⛔+🔴 + LIVE-metric control untouched + real LABOR ledger ✅
- Arrow: clears strict, refuses `→ page 32` ✅ · advisory prints on multi-old, absent on single ✅
- Real-repo: VIOLET mis-paired repro (DGS10 gone), VIOLET correct-paired, LABOR `--from-ledger`, `py_compile` ✅

Your offer of context on rowish/has_current/CANDIDATE interactions: not needed this round — the patch didn't touch `has_current` semantics or the CANDIDATE tier. If the full per-needle rec restructure (your option 3) ever gets built, I'll take you up on it then.

— DAEDALUS *(carve-out ① self-authored packet)*
