# FLEET_SCAN — 2026-06-04

**Scanner:** OpenClaw Prome bounded synthesis after GitHub pull + Jun 3-4 signal ingestion
**Coverage:** live dashboard, Prome boot files, direct Prome outbox signals, recent commit summaries from pulled work.
**Purpose:** Boot-readable fleet situation report. This is not deep domain research and does not replace agent STATUS files.

---

## Executive Read

Prome is no longer in Jun 2 boot-rehab mode. GitHub pull was clean, direct Prome signals have been ingested, and the next state problem is narrower: keep root/boot surfaces current while avoiding shared-repo races and stale trade rails.

**Live tape Jun 4 ~17:30 ET:** HY OAS **275bps [FRED 6/3] 🟢**, CCC **947bps [FRED 6/3] 🟡**, VIX **15.40 🟢**, Brent **$95.14 🟡**, USD/JPY **160.01 🔴**, WAL **$80.74 🟢**, KRE **$69.98 🟢**, TLT **$85.50 🟡**, BIZD **$12.70 🔴**, initial claims **225k [5/30] 🟡** with shadow-adjusted est **280k**.

The read remains **substance/tape divergence**. Stress channels are active, but public credit/vol are not confirming broad cascade.

---

## 1. Top Updates Since Jun 2

| Area | Update | Prome implication |
|---|---|---|
| **GitHub sync** | Pull fast-forwarded cleanly to `687e2968`; Prome signal commit `55e5b634` pushed. | Repo is clean/source-of-truth aligned. |
| **TLT / HENRY** | Old 5/22 2/1 TLT roll ticket superseded by Will/HENRY Jun 3. | `ACTIVE_DECISIONS` updated; no stale TLT BROKER_PENDING action. |
| **Pathspec / SAM** | SAM reported 8 agents / 9 sites still had risky `git reset HEAD` instructions. | Tracker created; Prome/SAM fixed; remaining owner edits pending. |
| **Credit/vol tape** | HY OAS 275, VIX 15.40. | Still no cascade confirmation. |
| **Japan/FX** | USD/JPY 160.01. | SAM channel is the sharpest live red threshold. |
| **BDC/private credit** | BIZD 12.70 red; BROCK Jun 4 work added OTF/BCRED/OCIC reads and convergence reportedly 46→55. | PC/BDC remains active; read BROCK before any PC action. |
| **Labor** | Initial claims 225k [5/30], shadow-adjusted 280k. | LABOR channel deteriorated to yellow; not headline break yet. |
| **Duration** | TLT 85.50, 10Y 4.46 [6/2]. | TLT Jun $85P salvage is near-the-money; Sep add still CPI-gated. |
| **Banks** | WAL/KRE green, OZK yellow. | Bank tape not confirming bear acceleration. |
| **Root HEARTBEAT** | Still Jun 2. | Should be refreshed separately if injected state must be fully current. |

---

## 2. Prome Surface State

| Surface | Status | Note |
|---|---|---|
| `PROME/SCRATCH.md` | ✅ Current Jun 4 | Boot handoff rewritten. |
| `PROME/TODAY.md` | ✅ Current Jun 4 | Dashboard + work queue updated. |
| `PROME/STATUS.md` | ✅ Current Jun 4 | Jun 3-4 signals + live dashboard anchor. |
| `PROME/FLEET_SCAN.md` | ✅ Current Jun 4 | This file. |
| `PROME/ACTIVE_DECISIONS.md` | ✅ Current | TLT supersession ingested; non-TLT old rails still verification-required. |
| `PROME/PATHSPEC_MIGRATION_STATUS.md` | ✅ Current | Tracks owner migration of risky commit protocols. |
| `HEARTBEAT.md` | 🟡 Jun 2 | Directionally consistent, but stale levels; refresh next if desired. |
| `PROME/HANDOFF.md` | 🟡 Jun 2 top block | Fine for recent continuity; refresh on closeout or before clear/new. |

---

## 3. Agent / Domain Snapshot

| Agent/domain | Current Prome read | Action rule |
|---|---|---|
| **HENRY** | Duration gate updated TLT handling; old roll ticket superseded. | Use HENRY signal for TLT; do not revive old 5/22 action card. |
| **SAM** | USD/JPY at 160; also owns pathspec audit signal. | Persistent agent; do not spawn casually. Track owner edits. |
| **BROCK** | Jun 4 PC/BDC updates landed; BIZD red. | Read current BROCK before any APO/ARES/BIZD decision. |
| **LABOR** | Claims yellow; shadow-adjusted 280k. | Watch NFP/claims path; spawn LABOR only for concrete labor decision. |
| **BRENT** | Brent yellow near $95; gas red. | Energy pressure active but not >$100 red. Persistent; don't spawn casually. |
| **REGINALD** | WAL/KRE green; OZK yellow. | Bank tape not confirming; use persistent REGINALD if Q2/WAL decision emerges. |
| **RED** | Jun 3-4 maintenance/challenge updates landed. | Use for adversarial pass only when active thesis/decision requires it. |
| **MARCO/OTTO** | Updates landed; not immediate boot blockers. | Route domain-specific questions to owners. |
| **WALTER** | Still owns signal/news routing. | Prome should not absorb routine news routing. |

---

## 4. Cross-Agent Contradictions / Cautions

1. **Tape still argues patience.** HY and VIX are green despite PC/labor/FX/energy stress.
2. **TLT language is now split by expiry.** Jun $85P = salvage catalyst bet; Sep add = CPI-gated. Don't blend them.
3. **Pathspec migration is operationally load-bearing.** The shared `.git/index` race is real; broad reset/stage patterns are unsafe.
4. **Owner isolation matters.** Prome tracks other agents' CLAUDE.md migrations but should not bulk-edit their files without Will override.
5. **HEARTBEAT is the next stale injected surface.** If the goal is fully clean boot context, root `HEARTBEAT.md` should be the next refresh.

---

## 5. Top 5 Operational Moves

1. ✅ **Finish Prome boot refresh** — update SCRATCH/TODAY/STATUS/FLEET_SCAN and commit.
2. 🟠 **Refresh root HEARTBEAT** — Jun 2 levels are stale; live regime is similar but USD/JPY/claims/TLT moved.
3. 🟠 **Coordinate pathspec migration** — keep tracker current as agents fix own CLAUDE.md files.
4. 🟡 **Read current BROCK only if PC/BDC decision becomes live** — Jun 4 updates matter, but don't absorb by default.
5. 🟡 **Position-state reconciliation** — separate future task; required before old 6/18 non-TLT rails can be used.

---

## 6. Gaps

- No broker/fill reconciliation performed; intentionally deferred.
- No deep read of all Jun 3-4 domain commits; this is a boot scan, not a research pass.
- `HEARTBEAT.md` still needs root-level refresh if Will wants injected state current.

---

## 7. Follow-Up

After this file is written:
1. Inspect diff for `SCRATCH`, `TODAY`, `STATUS`, `FLEET_SCAN`.
2. Commit explicit paths only.
3. Next recommended lane: root `HEARTBEAT.md` refresh, unless Will pivots to positions.
