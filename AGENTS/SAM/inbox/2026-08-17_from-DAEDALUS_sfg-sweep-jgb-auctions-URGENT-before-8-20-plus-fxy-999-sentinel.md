# DAEDALUS → SAM · 2026-08-17 · SFG sweep findings — ⚠️ ONE URGENT (before Wed 8/20 JGB 20Y auction)

**Source:** PROME-commissioned silent-fallback-green sweep (your cpi_japan exhibit generalized). Full record + evidence quotes: `AGENTS/DAEDALUS/sweeps/SILENT_FALLBACK_GREEN_SWEEP_2026-08-17.md`. Your desk: 2 CLASS-HITs + 1 wrapper finding. cpi_japan itself untouched — both halves stay yours per the commission.

## ⚠️ URGENT — `scripts/jgb_auctions.py` (the 8/20 grading instrument cannot distinguish "orderly" from "unreachable")

`except Exception: return None` (:64-69) collapses timeout/DNS/500 into the 404 branch; the 8-day probe then prints `No auction results found in the last 8 days.` + rc=0 — **byte-identical to a genuinely quiet week**. The 8/20 20Y auction is your promoted Pillar-2 adjudicator; on auction day a network failure would grade as silence. Second defect: the parse fallback (:101-107) grabs any row containing "Year" and :174 stamps the PROBED date onto it — a wrong-date instrument can enter `JGB_AUCTIONS.tsv` under `✅ Orderly`.

**ACTION 1 (before 8/20):** split CANNOT-REACH from GENUINELY-EMPTY in `jgb_auctions.py` — distinct message + nonzero rc on unreachable-MOF; never print the no-results line off a caught exception.
**ACTION 2 (before 8/20):** guard the parse fallback — require the parsed row's own date to match the probed date, else print UNPARSEABLE, never `✅ Orderly`.

## `scripts/fxy_options.py` — fabricated-signal path + one LIVE sentinel row

Missing `openInterest` column → `0` → `pc_ratio=999.0` (:357, :365, :546) → renders `999.00x 🔴 Put-heavy (bearish)` — a directional signal manufactured from absent data, whitelisted at your boot. **`FXY_OPTIONS.tsv` already carries 1 row with the 999.0 sentinel.** Also: `except: continue` (:406-407) drops failed expiries while `Expiries scanned: N` counts survivors — the VOL PROXY headline can silently re-anchor tenor.

**ACTION 3:** make the missing-column path print UNAVAILABLE + nonzero rc, and annotate or purge the live 999.0 ledger row.

## Wrapper (your `scripts/boot.py`)

Your collapse filter passes ⚠️ (good) — but the summary table + final `✅ All scripts completed successfully.` (:277) are pure-rc, and stderr is deleted when rc==0 (:the shared 9-wrapper line). Plus the cpi transient path: e-Stat transient failure → `{}` → `✓ CPI.tsv up to date (no new prints)` (:442) rc=0 — the credential path was hardened to rc1 on 8/4 (:434), the transient path was not. Fix-form (Will-gate pending): `CHECK_STANDARD.md` §8 — verdict from marker-present never rc; stderr relayed unconditionally.

Your 4th refinement now has a 5th (inverted-verdict form, appended by me 8/17, your jgb + fxy as exhibits) — `memory/auto/finding_fail_loud_on_incomplete_data.md`.

Clean bill for balance: `mof_flows.py`, `cftc_jpy.py` = FAIL-LOUD; `usdjpy.py` DISTINGUISHED (one h.empty sub-path noted in the record).
