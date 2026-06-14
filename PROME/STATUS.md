# PROME STATUS.md
**Updated:** 2026-06-14 PM ET (OpenClaw Prome — post-pull boot-surface refresh Phase 3)

## Core State

**Operational priority:** boot-surface catch-up after the large GitHub pull. The repo is fresh; Prome state was stale. Will approved a staged refresh with one explicit constraint: **do not edit agents**.

**Regime:** **Surface tape de-risked; tail/private/physical stress stayed sticky.** Broad cascade is not confirmed: HY OAS remains tight at **278bps [FRED 6/11]**, VIX faded to **17.68**, banks rallied, and Brent collapsed sub-$90. But the structural/tail side did not heal: CCC **956bps**, SKEW held 142+, private-credit gates/BDC stress remain hot, consumer-credit stress persists, Japan/BOJ risk is live, and physical energy/chokepoint stress remains severe despite the price collapse.

**Live dashboard anchor from Phase 0:** HY OAS **278bps [FRED 6/11]** 🟢, CCC **956bps [FRED 6/11]** 🟡, VIX **17.68** 🟢, Brent **$87.33** 🟡, gas weekly **4.15 [6/8]** 🔴, USD/JPY **160.18** 🔴, 10Y **4.45 [FRED 6/11]** 🟡, SOFR-IORB **-0.05 [6/11]** 🟢, KRE **$73.41** 🟢, WAL **$83.67** 🟢, OZK **$52.10** 🟢, APO **$133.88**, ARES **$134.90** 🟡, BIZD **$12.71** 🔴, FXY **$57.26** 🟡, TLT **$85.77** 🟡, initial claims **229k [6/6]** 🟡 / shadow **284k**, continuing claims **1.795M [5/30]** 🟢.

---

## Sync / Repo State

| Item | Status | Note |
|---|---|---|
| GitHub sync | ✅ Clean/synced at Phase 0 | Baseline: `master`, `HEAD/origin c87c00ac`, ahead/behind `0/0`. |
| Local working tree | 🟡 Prome refresh files modified/untracked | Phase notes + boot surfaces are local until Will approves commit/push. |
| Agent files | ✅ Untouched | Explicit Will constraint: no agent edits. |
| Push discipline | ✅ Will-coordinated | Commit locally only if approved; push only on Will's explicit call. |
| GitHub source-of-truth rule | ✅ Active | Avoid broad staging/reset. Pathspec only. |
| Dashboard health | 🟡 Check later | Dashboard output usable but process exited code 1; likely alert/red-zone behavior. |

---

## Prome Boot Surface Trust

| Surface | Current trust | Note |
|---|---|---|
| `PROME/SCRATCH.md` | ✅ Current Jun 14 | Phase 3 rewritten. |
| `PROME/TODAY.md` | ✅ Current Jun 14/15 | Phase 3 rewritten with near gates. |
| `PROME/STATUS.md` | ✅ Current Jun 14 | This file. |
| `PROME/ACTIVE_DECISIONS.md` | 🟠 Next in Phase 3 | Needs CPI/refunding/HYG cleanup; verification-required remains. |
| `PROME/FLEET_SCAN.md` | 🔴 Stale Jun 7 | Rewrite from Phase 1 map. |
| `HEARTBEAT.md` | 🔴 Stale Jun 7 | Rewrite last because it is the regime surface. |
| Phase notes | ✅ Current | `PROME/BOOT_SURFACE_REFRESH_2026-06-14_PHASE0.md`, `PHASE1.md`, `PHASE2_EDIT_MAP.md`. |
| `memory/2026-06-14.md` | ✅ Current | Compaction-safe memory checkpoint. |
| `PROME/PATHSPEC_MIGRATION_STATUS.md` | 🟡 Unchanged | Owner edits still pending; bundle with separate-clones cutover. |

---

## Agent / Domain State for Prome

| Domain | Freshness | Current state for Prome |
|---|---|---|
| **LIQUID / Funding-duration-credit** | ✅ Jun 13 | TEN closed winner; HYG $75P written off / let expire 6/19; HY OAS 278 tight; duration oscillation, not regime; FOMC/TIC next. |
| **VIOLET / Vol** | ✅ Jun 14 | VIX 17.68 complacency; VIX9D/VIX 0.976; M1:M2 +9.41%; SKEW 142.6 held; Bin-B credit block still governs. |
| **BRENT / Energy** | ✅ Jun 13 | Brent sub-$90 despite severe physical/chokepoint stress; Path A diplomacy and Path B demand-destruction/curve flattening both advancing. |
| **HAWK / Geopolitics** | ✅ Jun 13 | C/Grind 42%, B-Deal-Reopen 32%, D-Reescalation 26%; formal Hormuz closure fired but Brent fell same session. HAW-11 window through Jun 22. |
| **SAM / Japan** | 🟠 Jun 14 partial | BOJ Jun 16 live; MOF/intervention probability re-derived ~72% → ~30%; FXY Jun18 $58C hold already decided by Will; some CFTC/carry details pending. |
| **CARL / Consumer** | ✅ Jun 14 | LEN guide cut + consumer-credit stress intact; UMich expectations relief lowered CRL-08 confidence, no score move. SAVE Jul 1 remains structural drag. |
| **LABOR** | ✅ Jun 14 | NFP +172k and +93k revisions strengthened hard data; claims drift to 229k, AI cuts record; labor cliff not firing. |
| **RED / Adversarial** | ✅ Jun 13 | Net bear 57, confidence 70; managed decline and stagflation co-modal; near-term tape bull-side into catalysts. |
| **BROCK / Private credit** | 🟠 Jun 8 but load-bearing | PC gate cascade / BDC cuts / 6.0% PC default hot; macro HY still refuses. Keep 6/18 rails verification-required. |
| **REGINALD / Banks** | 🟠 Jun 8 | Broad cohort bank fade retired; WAL bear now idiosyncratic/Q2-print gated; bank tape green. |
| **BOND / Duration-auctions** | 🟠 Jun 9 partially superseded | Pre-auction read superseded by LIQUID Jun 13 integration: 10Y strong, 30Y soft-but-cleared; duration oscillation, not regime. |
| **HENRY / Market structure** | 🔴 Stale/dark post-CPI | Needed for GEX-suppression / dealer flip level; do not lean on Jun 9 header for current mechanics. |
| **NEXUS / Synthesis** | 🔴 Stale Jun 8 | T-08 correlated-fragility useful as awareness, not trade rail; needs post-6/12 refresh. |
| **WALTER / Routing-news** | 🟠 Jun 10 | Registry refresh active, but Iran anchor stale vs HAWK/BRENT Jun 13. Use HAWK/BRENT for current Iran-energy truth until refreshed. |
| **OTTO / Auto** | 🟠 Infra refreshed, domain stale | Structural auto/fraud vectors remain important, but not a primary boot-surface driver until refreshed. |

---

## Current Work Queue

| Action | Pri | Status |
|---|---:|---|
| Phase 0 baseline | ✅ | Saved to `PROME/BOOT_SURFACE_REFRESH_2026-06-14_PHASE0.md`. |
| Phase 1 bounded agent inspection | ✅ | Saved to `PROME/BOOT_SURFACE_REFRESH_2026-06-14_PHASE1.md`. |
| Phase 2 edit map | ✅ | Saved to `PROME/BOOT_SURFACE_REFRESH_2026-06-14_PHASE2_EDIT_MAP.md`. |
| Phase 3: rewrite `TODAY` + `SCRATCH` | ✅ | Done. |
| Phase 3: rewrite `STATUS` + `ACTIVE_DECISIONS` | 🔴 | STATUS done; ACTIVE next. |
| Phase 3: rewrite `FLEET_SCAN` | 🟠 | Pending. |
| Phase 3: rewrite `HEARTBEAT` | 🟠 | Pending last. |
| Verify stale language / diff | 🟠 | Pending after writes. |
| Position-state reconciliation | 🟠 | Deferred; separate future pass unless Will pivots. |
| HENRY/NEXUS/WALTER refresh | 🟠 | After boot surfaces; do not mix into Phase 3. |
| Separate-clones migration | 🟠 | Post-Jun16/FOMC calm-window decision packet; M3 slate still SAM/HENRY/REGINALD/OZK/CARL. |

---

## Rules of Engagement

- **No agent edits** unless Will explicitly changes the constraint.
- **No trade execution without Will approval.**
- **No trade recommendations unless explicitly requested.**
- **No external/public messages without approval.**
- **Old trade rails are verification-required** until broker/Will reconciliation.
- **WALTER routes signals/news; Prome maintains state, tasking, rails, and Will-facing synthesis.**
- **Pathspec commits only;** never `git add .`, `git add -A`, or `git reset HEAD`.
- **Push is Will-coordinated** — commit locally only if approved, push only on Will's explicit call.
- Read current files before editing; verify after edits.

---

## Next Best Action

Finish Phase 3 in order: rewrite `PROME/ACTIVE_DECISIONS.md`, then `PROME/FLEET_SCAN.md`, then `HEARTBEAT.md` last. After that, run diff/stat + stale-language grep and ask Will whether to keep/archive/commit phase notes.
