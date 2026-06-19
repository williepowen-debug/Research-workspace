# ORACLE — SCRATCH (canonical session handoff)

**Last session:** 2026-06-18 (revival + gap-audit hardening, Will-directed)

## CHANGES SINCE
- ORACLE revived from 79-day dormancy (session 1), then gap-audited and hardened (session 2).

## WHAT I DID
- **Session 1:** built + pushed the live Polymarket fetcher and plumbing (`a647b97` on origin).
- **Session 2:** watchlist 8→14 (bailout, named-bank, 2× WTI rungs, MSTR, unemployment); slug-expiry detection; added NEXUS_BRIEF + SIGNAL_INTAKE + WALTER delivery lane + MAINTENANCE; flagged fleet-wiring to PROME.
- **Live reads:** Iran de-escalation now **oil-corroborated** (🔴 → HAWK/BRENT); recession 63pp divergence (→ RED); Fed no-cuts 81% (→ LIQUID); complacency 82.5% (→ VIOLET); bank cluster benign (→ REGINALD).

## NEXT SESSION (priority order)
1. Re-pull (`polymarket.py pull --log`); **3-day re-check ~6/22** on the thin movers.
2. **Roll the Jun-30 / Jul-1 markets** (bank-failure, named-bank, Iran, both WTI) before they resolve.
3. Chase **RED** for a current fleet recession probability — the divergence math depends on it.
4. If Will provides **Kalshi** creds → wire Kalshi (recession/Fed/CPI corroboration).
5. **Replace/drop** the dead June-unemployment market ($63 vol).

## CARRY-FORWARD
- **Push:** session-1 commit on origin (`a647b97`). Session-2 commit pending — Will-coordinated push.
- **Fleet-wiring** depends on PROME/WALTER/NEXUS acting on the `outbox/` request — until then ORACLE's signals don't auto-deliver.

## OPEN HYPOTHESES
- Broad crowd-calm (recession↓, NEH↑, banks benign, Iran de-escalating) is either a contrarian setup or thesis decay — RED adjudicates. Don't resolve it here.
