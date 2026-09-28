# Paid data: existing-entitlements check (DEFERRED; nothing purchased or requested)

**2026-09-28, BRENT, Will scope item 6 (WQ-329):** *"Defer paid data. Bring back the provider, cost, exact instruments/history, demonstrated access and the decision it would improve. Check existing entitlements first."* Context: **WQ-300 (Will 9/26)** declined the proposed paid lines and preserved unavailable inputs as explicit gaps. $0.

## Entitlements found (checked 9/28)

| Source | Status on this box | What BRENT gets | Gap for the diesel/VLO question |
|---|---|---|---|
| EIA v2 API (key in repo `.env`, via FORGE `fetch.py`) | ✅ **Demonstrated today** | Daily spot (NYH/USGC ULSD and gasoline, Brent, WTI) with ~4 business days' lag; weekly WPSR; retail | Lag; spot only; no ICE gasoil; no futures settlements |
| yfinance (free) | ✅ Demonstrated today | NYMEX/ICE-listed named futures (BZ/CL/HO/RB/NG `.NYM`), equities | **Single vendor; not official settlements**; thin months go blank; no ICE gasoil ticker found |
| FRED (free) | ✅ Boot uses it | Mirrors EIA (DCOILBRENTEU, GASREGW) | Same lag |
| CME settlements page | ❌ **Blocked from this box** (standing) | — | Official HO/CL settles for F1 |
| **LSEG connector** (claude.ai MCP, listed in this harness) | ⚠️ **Present but NOT authenticated. Not attempted:** starting a sign-in is Will's call | *If* Will's account carries a data licence: ICE gasoil, CME settles, Platts-type assessments | **Entitlement UNKNOWN**: the connector's presence ≠ a data licence |
| **S&P Global connector** (claude.ai MCP; also a Capital IQ plugin) | ⚠️ Same: present, NOT authenticated, not attempted | *If* licensed: Commodity Insights (Platts) product assessments; Capital IQ refiner financials | **Entitlement UNKNOWN** |

## The one gap that matters for today's question
**US-vs-world diesel (NYMEX HO vs ICE gasoil).** This is the most direct instrument for an export restriction: a ban should push HO down relative to gasoil. Free sources on this box don't carry ICE gasoil. The VLO observables note lists this as a limitation.

## If it is ever brought back (the template Will set)
- **Provider:** first establish whether the existing LSEG or S&P Global connectors carry a licence (one authentication, Will's action).
- **Cost:** UNKNOWN until then; nothing priced here.
- **Instruments/history:** ICE Low Sulphur Gasoil futures (front 3 months, daily settles, 2021→) and CME HO/CL official settlements.
- **Demonstrated access:** none yet.
- **Decision improved:** TERRY's VLO F1 grade (official settle instead of a proxy) and the export-restriction read (HO−gasoil).

**Recommendation:** none now (deferred). The cheapest next step is Will saying whether either connector is licensed.
