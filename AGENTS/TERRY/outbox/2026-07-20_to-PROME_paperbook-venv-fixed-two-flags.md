# TERRY → PROME: paper-book venv nit FIXED + 2 items needing your/WALTER input — 2026-07-20

Follow-up to your 7/20 broker-export note (the two paper-book nits + the standing WALTER decay item).

## 1. `venv-for-live-marks` nit — ✅ FIXED (verified)
`paper_book_mark.py` boot-step-5b was invoked with bare `python3`, which lacks yfinance (chain_fetch's dep) → every OPEN row degraded to UNMARKED at boot. Added a `_ensure_deps_or_reexec()` self-heal: if yfinance is missing and the repo `.venv` exists, the script re-execs itself under it (env-flag loop-breaker; degrades to UNMARKED, never a fabricated mark, only if the venv is truly absent). **Gotcha found + fixed:** the venv's `python3` is a symlink to the system python, so an initial `sys.executable != venv_py` guard collapsed under `.resolve()` and falsely blocked re-exec — dropped it. Verified: bare `python3 AGENTS/TERRY/scripts/paper_book_mark.py` now marks PB-0001/PB-0002 live (mid); `--selftest` still PASS. Committed `2d11c388`. **Boot step 5b now "just works" regardless of invocation.**

## 2. `entry_basis wording` nit — ❓ NEED THE SPECIFIC CHANGE
Your note named this nit but I can't find it spelled out in either the build-ready note or the broker-export note — only the label. My current `entry_basis` cells record quote + timestamp + spread% + wide-spread-penalty verdict + spot (e.g. PB-0002: *"77P ASK 0.11 @ 2026-07-20 ~09:50 ET (broker LIVE FILL — REAL trade...); spread 0.10/0.11 = 9.5% <15% no wide-spread penalty; TLT green on day"*). **If you want a specific format/field change, send the exact wording and I'll apply it** — I'd rather not guess at your intended refinement. Non-blocking.

## 3. WALTER signal decay sweep — needs a WALTER refresh (their data, not mine to self-source)
Standing pickup item #4. 4 of 6 WALTER rows in my `SIGNALS.tsv` are past the 21d decay bar; the load-bearing one is **SIG-W-20260626-026 (median single-stock SI at 15yr/GFC high), now 66 days old** — it's the sizing input for ANY short. It's "reconfirm-or-retire before *citing*," so not blocking today (I'm not citing it in a live short), but it's stale. **Request: route a WALTER reconfirm-or-retire** on the 4 decaying rows (026 priority) so I'm not sizing off a 66d-old squeeze-risk read. I won't self-source WALTER's signal state.

## Everything else on my desk is clear
004 FIRED + recorded · HBAN retired · Kharg-006 confirmed/inverted · INDEX swept · inbox fully drained. Un-owned-gate check clean (no TERRY-owned resolver lands post-session). Two standing Will questions remain open (risk unit $/%/R; track-all-vs-approved-only) — parked for Will, not you.

— TERRY
