# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-02 09:55 ET (OpenClaw Prome — post-clear state rehab)

## What Just Happened

Will requested a clean `/clear` after compacting, then explicitly redirected: **do not worry about trade positions right now; get Prome updated and caught up.**

Completed so far:
- Confirmed repo is synced to GitHub/source-of-truth: `master` at `origin/master` / HEAD `e17a4c90`.
- Earlier stale local generated edits (`AGENTS/PROME/LAST_COMPLETION.md`, `PROME/FLEET_SCAN.md`) were discarded with Will approval before pull.
- Ran live dashboard 2026-06-02 ~09:45 ET.
- Spawned bounded read-only fleet scan (`fleet-scanner-2026-06-02`); result confirmed Prome boot files were stale even though agent dirs advanced through Jun 1.
- Began Prome boot-surface rehab: rewrite SCRATCH / TODAY / STATUS / FLEET_SCAN / ACTIVE_DECISIONS as current June 2 state surfaces.

## Current Operating Posture

**Priority:** State hygiene, not trade recommendations.

Prome's own state files were stale around May 26-27 while agent work continued through Jun 1. Treat old Prome action rails as historical until reconciled. Do not surface stale `BROKER_PENDING` / trigger language as current without broker/Will verification.

**Core regime read from current evidence:** public credit and vol remain calm while stress persists in Japan/FX, energy, BDC/private-credit marks, and duration. This is still divergence, not confirmed broad cascade.

## Live Dashboard — Jun 2 ~09:45 ET

FRED/date-stamped rows:
- HY OAS **272bps [6/1]** 🟢
- CCC OAS **946bps [6/1]** 🟡
- Gas weekly **4.47 [5/25]** 🔴
- Initial claims **215k [5/23]** 🟢; shadow-adjusted estimate **270k**
- Continuing claims **1.786M [5/16]** 🟢
- SOFR **3.65 [6/1]** 🟡
- 10Y **4.45 [5/29]** 🟡
- CP-TBill spread **0.14 [5/27]** 🟢
- SOFR-IORB **0.00 [6/1]** 🟢

Live/price rows:
- Brent **~$95.05** 🟡
- USD/JPY **159.79** 🔴
- KRE **~$69.20** 🟢
- WAL **~$79.55** 🟢
- APO **~$128.71** 🟡
- ARES **~$127.67** 🟡
- OZK **~$48.36** 🟡
- FXY **~$57.45** 🟡
- TLT **~$85.75** 🟡
- BIZD **~$12.74** 🔴
- VIX **16.18** 🟢

## Fresh Agent Changes to Integrate Mentally

| Agent | Freshness | Current state |
|---|---|---|
| SAM | Jun 1 | BOJ Jun 16 is dominant single-path; market priced hike ~88%, SAM 70%; USD/JPY near 160 intervention zone; Sep $60 calls not warranted under v1.5. |
| BRENT | Jun 1 | Phase 1 re-armed: Iran suspended talks, Kuwait missile volley, Brent back near $95; Trump deal rhetoric downgraded to tape noise unless substance follows. |
| VIOLET | Jun 1 | R11 analog dead / gradual fade won; R12 technically terminated but spot/SKEW watch near re-establishment; coiled-spring class validated for later timing windows. |
| MARCO | Jun 1 | Thesis refined: acute crisis softened, structural ag-labor + Canadian-travel channels persist. |
| CARL | May 31 | Consumer/stagflation state hardened via GDP/PCE; important but not immediate Prome state-rehab blocker. |
| WALTER | May 27 | Operationally stale relative to Jun 1 Iran/BRENT shift; routing owner, likely needs anchor refresh after Prome surfaces are fixed. |
| REGINALD / BROCK / HENRY / LIQUID / BOND | May 20-21 domain heads, later housekeeping commits | Important but state-stale; revive only after Prome boot surfaces are clean or a trigger/signal requires it. |

## Current Prome File Trust

| File | Status |
|---|---|
| `PROME/SCRATCH.md` | ✅ Current Jun 2 handoff. |
| `PROME/TODAY.md` | ✅ Current Jun 2 state-rehab surface. |
| `PROME/STATUS.md` | ✅ Current Jun 2 operational surface. |
| `PROME/FLEET_SCAN.md` | ✅ Current Jun 2 bounded fleet scan. |
| `PROME/ACTIVE_DECISIONS.md` | ✅ Current Jun 2 safety index; old trade rails marked verification-required. |
| `HEARTBEAT.md` | Injected but stale vs Jun 1 agent changes; do not quote old levels. |

## Next Work

1. Review final diff/stat for the Jun 2 boot-surface refresh.
2. Ask Will whether to commit/push the Prome refresh to GitHub source-of-truth.
3. After state files are safe, decide whether to refresh WALTER Iran anchor / news routing.

## Guardrails

- No trade execution. No trade recommendation unless explicitly requested.
- No external/public messages without approval.
- No `git add .` / `git add -A`.
- Do not spawn persistent agents casually: CARL, REGINALD, OZK, SAM, RED, BRENT, Claude Code Prome.
- GitHub/origin remains source-of-truth; local edits are subordinate until committed/pushed intentionally.
