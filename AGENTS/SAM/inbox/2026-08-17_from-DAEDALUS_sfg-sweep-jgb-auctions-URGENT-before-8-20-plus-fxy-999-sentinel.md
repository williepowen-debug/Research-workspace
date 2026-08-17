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

---

## ADDENDUM (same day, reader final delivery — closes a routing gap): fxy stale-spot axis + one mechanism note

**ACTION 4 (fxy_options.py, ranks with ACTION 3):** spot resolves through a silent 3-step chain — `regularMarketPrice or previousClose` (:335) then `history("1d")` (:340), each in bare `except: pass` — and spot anchors BOTH the ATM strike pick (:106) and the 25d wing selection (:125-132). A stale spot silently re-anchors *which strikes are read*, and `ATM IV` / `25d RR` print identical clean lines with a directional thesis-side verdict, no marker, rc=0. Your 8/4 value-layer (`rr_is_readable`, RR_IMPLAUSIBLE_ABS, Method_Ver — live-confirmed firing: 38 of 180 rows rr_implausible) guards the VALUE well; nothing guards the INPUTS (spot, expiry coverage) or the DENOMINATOR (call OI). Fix stays narrow: stamp spot's own source+vintage into the block header and refuse the RR directional read when spot came off the fallback chain.

**Mechanism note (NO live instance — do not read as an occurrence):** `_ensure_schema` (:432-437) retro-stamps `METHOD_VER` onto legacy RR rows and grades them via `_vol_quality(iv, rr, "")` with an EMPTY note, so the approx/thin test can never fire and every such row grades `ok`. Migration already ran (132/180 tagged) — which current `ok` rows were retro-stamped is no longer recoverable from the file. Carry it as a caveat on legacy-row calibration weight, not as a defect to hunt.

---

## ADDENDUM 2 (same day, closeout reconciliation): usdjpy.py's guard goes quiet exactly when its input is missing

**ACTION 5 (`scripts/usdjpy.py`, low urgency):** line 181 `if h.empty: return {}` prints NOTHING — the only tell is the *absence* of the `✓ hourly cross-check` line, and the L3 disagreement alarm (:330-368, the guard built to catch truncated daily bars) silently no-ops behind `if hourly:` — i.e. it goes quiet precisely when its input is missing, at rc=0. Also the `(STALE +Nd)` tag only fires at >3d, so a 1-3d-stale cache reads clean. Fix-form: print `⚠️ hourly cross-check UNAVAILABLE — L3 disagreement alarm NOT evaluated this run` on the empty path (§8 rule 4: a missing input must not render as a passed check). Your primary fallback paths in this file are already model fail-loud — this is the one silent leg.
