---
name: finding_market_data_venv_invocation
description: market-data fetch.py/dashboard.py need the repo .venv python — plain system python3 fails with ModuleNotFoundError (yfinance)
metadata: 
  node_type: memory
  type: reference
  originSessionId: f5e6203b-f897-49e7-a8c0-57c340964d14
---

`FORGE/tools/market-data/` (`fetch.py`, `dashboard.py`, `vix_futures.py`) MUST be run with the repo venv's interpreter, not the system `python3`. The venv is created with `include-system-site-packages = false`, so `/usr/bin/python3` sees none of the deps (yfinance, etc.) and dies with `ModuleNotFoundError: No module named 'yfinance'`.

**Correct invocation (either):**
- `.venv/bin/python FORGE/tools/market-data/fetch.py price CNY=X`
- `source .venv/bin/activate && python3 FORGE/tools/market-data/fetch.py ...`

**Trap:** the README shows `python3 fetch.py price KRE` — that shorthand assumes the venv is already activated. Running bare `python3` (or `Bash` tool default, which is `/usr/bin/python3`) is the failure mode. yfinance **is** installed (v1.4.1 in `.venv`); the tool is not broken.

**This is NOT machine-specific.** `.venv/` lives in the git repo and travels desktop⇄laptop, so the behavior is identical on both — do not mis-diagnose it as a laptop/machine-local gap. (Concrete instance of [[finding_verify_runtime_context_before_tool_broken]]: reproduce in the tool's actual runtime — here the venv — before calling it broken.) yfinance prices are intraday-live (FX/commodities/ETFs); FRED series lag T+1. Useful for a second-source cross-check of web-scraped FX (verified 2026-07-04: tool CNY=X 6.77 / KRW=X 1,530 / BZ=F $72.13 matched web figures).
