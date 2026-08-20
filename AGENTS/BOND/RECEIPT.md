# BOND Receipt — 2026-08-20 (Thu, 08:4x → 11:0x ET, ongoing; auction 1PM)

**Session:** boot → SAM packet → BND-17 pre-registration → Will-requested core-file sweep → two checkers built → **fix-verification audit (this section).**

## Inbox

| File | Action | Workbook | Outbox |
|---|---|---|---|
| `2026-08-20_from-SAM_4wk-rolling-sigma-and-n-answered…` | **INTEGRATE** → `processed/` | `KB-BND-141/142/143` | reply → SAM inbox |
| `2026-08-20_from-SAM_exceedance-both-ways…` (doorbell) | **INTEGRATE** | `KB-BND-144/145/146` | bar ruling → SAM |
| `SIG-W-20260820-003` (WALTER lane) | **INTEGRATE** → `WALTER/processed/` | `KB-BND-147` | — |

**Inbox: general 0 residue · WALTER lane 2 unprocessed** (`SIG-W-20260820-001` + its RETRACTION — BOJ/SAM domain, context-only, deliberately left).

## Decisions

| Item | Outcome |
|---|---|
| SAM 4wk-rolling **bar** | **RULED** — SELL WATCH −¥2.054T / ESCALATE −¥2.979T, quoted **de-clustered**. `±1.0σ` rejected because the overlap bias is worst at the loosest bar. **Frequency-calibrated ONLY; separation vs UST outcomes never tested; fires nothing alone.** |
| DM sovereign cross-section | **BUILT** (US/EA/UK/AU at issuer primaries) — the Will-ruled 8/10 scope claimed it existed and it did not |
| `BND-17` | **PRE-REGISTERED** pre-print, 45%, indirect ≥76.17%, EVENT-anchored, VOID branch. Calibration row, nothing rides on it |
| Benchmark n=3 → **n=7** | Reconciled on STATUS ×2, CATALYSTS, AUCTION_HEALTH |
| **H3 cross-section read** | 🔴 **RETRACTED same session** — a one-week artifact; at 3wk Japan ranks FIRST, the opposite signature |

## 🔴 FIX-VERIFICATION AUDIT (Will: "did we address the defects we found?")

**Verified at the artifacts, not from memory.** 24 of the day's defects confirmed fixed. **Five were NOT, and were found only by auditing:**

| Gap | Why it survived | Now |
|---|---|---|
| `SCRATCH.md` still carried the killed *"BND-14's second test"* + n=3 | I flagged it, **PROME fixed their surface, I never fixed mine** — flagging is not fixing | ✅ corrected |
| `KB-BND-145` still `ACTIVE` after `KB-BND-148` retracted its inference | KB hygiene ran on `Stale_By` dates, not on same-day retractions | ✅ → `CORRECTED`; numbers stand, conclusion does not |
| `RECEIPT.md` 2h stale | written mid-session, never refreshed | ✅ this file |
| **VIOLET ask orphaned 76 days** | packet written + committed to `outbox/`, **never delivered**; `CDX_CASH_BASIS` carried an open ⬜ waiting on it | ✅ re-sent restated (not the stale June text); ⬜ dated + `re-test: 2026-09-20` → retire the clause if silent |
| **`outbox/delivered/` did not exist** | documented in `CLAUDE.md` MAIL for months; never created, so sent ≠ orphan was indistinguishable | ✅ created; doc corrected |

⚠️ **And a correction to my own audit method:** a filename scan flagged **7 of 22** outbox packets as orphans. **That over-counts.** HENRY demonstrably *has* the 7/23 HEN-42 content — their files quote *"BOND VOTES CONFIRM"* — filed under a different convention. A scan keyed on naming reads local form as absence; "did it arrive?" is not "do they know?" **Confirmed orphan: VIOLET (zero trace on a content grep). Confirmed delivered: HENRY. Five remain UNVERIFIED — owed, `re-test: 2026-08-27`, content-check each, do not redeliver stale text.**

⚠️ **My own new checker missed all five** — `SCRATCH.md` and `RECEIPT.md` were outside its scope, and `SCRATCH` is *boot read #2*. Scope extended.

## Built

| Tool | Purpose |
|---|---|
| `monitors/closeout_check.py` | **THE closeout invocation** — both checks, one fetch, one rc. `--selftest` = 12 real shipped defects |
| `monitors/assertion_check.py` | stale **assertions** (no number to catch): directional · file-state · expired · capability |
| `boot_recompute.py` (extended) | prints TRADE.md's **gate table**; drift-checks boot-unread surfaces; `rc=1` |

**Checker defects found and fixed by their own tests:** cried wolf 16→0 · `not free` inside "not FREE**ze**" · duplicated regex validating the copy nobody runs · unspecified lookback letting the *checker* pick the verdict (`KB-BND-148`, reproduced inside the tool built to catch it) · a citation of a defect flagged as the defect.

## State

**Composite 12/35 unchanged · TLT puts HOLD, no add · DFII10 2.41 [8/18], 9bp from the only live add-gate, moved AWAY.**
**OPEN predictions: `BND-15`, `BND-17`.** Closeout pass: **rc=0 clean.** Git: committed path-scoped + auto-pushed, verified on origin by path.

**Next:** 1PM 30Y TIPS `912810US5` — grade at frozen bars, doorbell PROME.
