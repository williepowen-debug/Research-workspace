# Upgrade Card — LIQUID (read-only assessment, no agent files touched)

> 🗄 **ROUTED 2026-07-12 — CLOSED AS A QUEUE 2026-08-17 (self-audit F5 banner pass).** This card's findings were routed to the owner/FLEET_MAP when written; per-row states below are historical. Not maintained — current gaps live on the agent's FLEET_MAP row. Do not work rows from here without re-verifying at the agent.

**By:** DAEDALUS · **Date:** 2026-07-04 · **Class:** Market (liquidity/Treasury-plumbing; the amplification node; holds NO trade book — signal/DATA agent, like CARL)
**Method:** `UPGRADE_PROTOCOL.md` (one section at a time) · graded vs `BLUEPRINTS/market-agent.md` · comprehension in `profiles/LIQUID.md`
**Verdict: L4 (conf H), 2-level under-rate corrected** (was L2 Conf-L) — **the fleet's highest under-rate bet, confirmed.** LIQUID holds the **fleet-best falsification pattern** (PAT-013: channel-kill-vs-thesis-kill + migration theorem, verbatim at THESIS.md:98) and is the blueprint's **named source for §1 migration-legs, §3 conjunction + KILL_MEMO, §6 crisis-outbox**. The 6/27 scan's "exit-rules lack session counts" is **factually wrong** (13+ instances, PAT-024); "no conv-matrix" is *half* right — the convergence substance exists in code/KILL_MEMO but the **5-pt handle is genuinely absent**. Every item below is an *added handle*, a *build-back*, or a *staleness fix* — never a rewrite (PAT-015). **Nothing applied — this is the queue.**

> **Application gate:** all edits touch LIQUID's files → gate on **permission + a fresh idle-check** (AUTHORITY). LIQUID committed **today (7/4)** — treat as **live**; route **task-packets to `inbox/`**, do NOT direct-edit. Re-read the live file (PAT-009) before any change.

---

| § | Blueprint section | LIQUID current state | Applies? | Gap type | Proposed minimal handle | Priority |
|---|---|---|---|---|---|---|
| 1 | **Thesis structure** | THESIS.md v2.0 — **three independent failure-legs (A/B/C) + migration theorem** ("channel migration is normal; abandonment requires multiple legs failing simultaneously"; KB-LIQ-052 "changed addresses") | ✅ APPLIES | **exemplary — named source** | None — the fleet's reference instance of §1 failure-legs+migration | 0 |
| 2 | **Convergence matrix** | **5-pt score ABSENT**; local **DORMANT→ARMED→TAGGED→TRIGGERED** states; working convergence structure in `boot.py` (CCC-BB pin, X1) + KILL_MEMO, but no STATUS 5-pt matrix; Independence in prose only | ✅ APPLIES | **missing-handle (the one structural gap)** | Add a thin **`Score (1-5)` overlay + `Independence` column** on the STATUS Triggers table, mapping the DORMANT→TRIGGERED states onto the universal scale. *Add ALONGSIDE; the local states stay canonical (blueprint §2 carve-out).* More than a column-add since convergence currently lives in code → **M**. | **2** |
| 3 | **Thresholds** | textbook **durable-vs-live split** (CREDIT_THRESHOLDS frozen → THESIS §5 → KILL_MEMO → STATUS live); **X1 conjunction** (HY OAS>280 AND BROCK wrapper-leads, KB-LIQ-062, solo-vs-paired logic); **two-sided KILL_MEMO** (fired 7/1) | ✅ APPLIES | **exemplary — named source** | None — the blueprint's reference instance of conjunction + KILL_MEMO | 0 |
| 4 | **Invalidation / exit** | **channel-kill vs thesis-kill (PAT-013 fleet-best, verbatim THESIS.md:98)**; per-channel kill table §7; **13+ N+session counts** (KILL_MEMO rungs, STRATEGY, STATUS); FIRED/NOT-FIRED = TAGGED/ARMED + drill-log fire history | ✅ APPLIES | **exemplary** | None — the "lacks session counts" flag is **factually wrong**. Local TAGGED/ARMED vocab is functionally richer than HENRY's literal FIRED/NOT-FIRED. | 0 |
| 5 | **Predictions** | workbook/PREDICTIONS.tsv live; **boot.py due-scan** flags OVERDUE/DUE≤7d (built after LIQ-02 aged 3mo unnoticed); LIQ-03 flipped by adversarial verify → LIQ-04 | ✅ APPLIES | conformant | None *required*. *Optional owner polish: EMPIRICAL/ESTIMATE/ASSUMPTION tier tags + a per-row if-falsified consequence (analogue = channel-reweight + consumer-notify, no book).* | 3 |
| 6 | **Cross-agent routing** | CLAUDE.md:112-123 route-matrix; **crisis-only outbox EXEMPLARY** (6 files/6wk, codified — named source) | ✅ APPLIES | strong; **1 missing-substance (deferred)** | **NEXUS_BRIEF** absent — but **deliberately deferred** ("low priority per advisor focus-protection"). **NOT an auto-build: reviving it re-opens a design call → route to Will/PROME**, don't scaffold. | **3 (gated)** |
| 7 | **Standing disciplines** | **strongest anti-staleness discipline in fleet** ("no live levels in state files"); boot fail-loud parsers; schema selftest | ✅ APPLIES | strong; **1 missing-substance (stranded)** | **★ EXPECTED_SIGNALS revival** — see L4→L5 table. The pre-registered "absence-is-data" discipline is stranded in `archive/legacy/` since Feb; ~5 signal-types have no live tracker. | **2** |
| 8 | **BOTTOM LINE** | **ABSENT** — existed in the Feb archive, dropped; STATUS ends at "Durable Signals Log" | ✅ APPLIES | **missing-handle + regression** | Add a labeled **`## BOTTOM LINE`** (2-4 sentences) to STATUS. Cheap; restores a dropped handle. | **1** |

**Section tally:** §1 exemplary(named) · §2 missing-handle · §3 exemplary(named) · §4 exemplary · §5 conformant · §6 strong (+deferred NEXUS_BRIEF) · §7 strong (+stranded EXPECTED_SIGNALS) · §8 missing-handle+regression. **Two genuine substance gaps** (§7 EXPECTED_SIGNALS stranding; §6 NEXUS_BRIEF — but that one is a *chosen* deferral), the rest handles.

---

### Separately — the real L4→L5 work
| Item | Why | Gap type | Effort |
|---|---|---|---|
| **★ EXPECTED_SIGNALS revival (the standout)** | A well-built 308-ln pre-registered "absence-is-data" discipline archived Feb-13 (`4894d8cc`), never revived; ~5 of ~12 signal-types (FHLB, sponsored-repo, MMF-WAM, FTD, CCY-basis) have **no living tracker**. **Sibling drift:** LABOR/SAM kept theirs live in `workbook/` in the *same* commit; blueprint even credits MARCO for a discipline LIQUID built *first*. **Scope call:** full 12-signal revival vs. re-home only the ~5 orphans into `workbook/` (template = LABOR/SAM). | missing-substance (partial) | **M** |
| **CLOSEOUT.md bare `boot.py --selftest` ×2** (lines 80, 186) | **Live PAT-031 asymmetric violation** — boot got the 7/1 cwd-proof fix; the closeout callsites to the *same script* didn't → fail rc=2 from an `AGENTS/LIQUID/` launch cwd. Wrap both `(cd "$(git rev-parse --show-toplevel)" && …)`. | hygiene bug | **S** |
| **IDENTITY.md 8-day stale** (6/25) no STATUS pointer | low-touch file by design, but gives no "current state → STATUS" pointer; add the pointer + a restamp | hygiene | **S** |
| **CATCHUP_PUNCHLIST.md** closed-episode, no closing banner | ~85% done, 3+wk stale; banner it + fork genuine remaining items (KILL_MEMO false-kill guard, VX/FLOW restamp) to STATUS/MEMORY | hygiene | **S** |
| **archive/{legacy,handoffs,status_snapshots} no README** | the rest of archive/ carries README-disposition (when/why/KB-pointer/do-not-restore); 3 short READMEs bring it to full standard | hygiene | **S** |
| **RP-LIQUID-5_INSURANCE_LEVEL3_CRE_TRANSMISSION.md** | 129d, unreferenced, still "Initial Research Framework," loose in domain/sources root = silent-rot middle. Archive **or** promote (note: the STATUS "Athene FABN" thread is a *different* SHADE-sourced mechanism — this file was never picked up) | hygiene | **S** |
| **STATUS_archive_20260227_full.md misfiled** | belongs in `archive/status_snapshots/` not `domain/sources/` | housekeeping | trivial |
| **"Telegram-persistent" FLEET_MAP claim unsubstantiated** | no Telegram mechanism found in the read; verify against a live mechanism or correct the roster note before it propagates | DAEDALUS-map fix | trivial (done this pass — FLEET_MAP note softened) |

---

## The queue
1. **FLEET_MAP / profile already reflect L4 (DAEDALUS's own files) — DONE 7/4** (corrected the L2→L4 false-negative + softened the unsubstantiated Telegram note; PAT-024). No concurrency risk.
2. **Batch 1 — quick handle + hygiene (task-packet, LIQUID is LIVE):** §8 BOTTOM LINE label · CLOSEOUT.md cwd-proof ×2 (real bug) · IDENTITY.md pointer+restamp · CATCHUP_PUNCHLIST banner+fork · 3 archive READMEs · orphan insurance-file disposition · STATUS_archive relocation. All **S**, additive/hygiene. Route to `inbox/`.
3. **Batch 2 — §2 5-pt convergence overlay + Independence column.** **M** (convergence lives in code today → needs a STATUS surface). Add alongside DORMANT→TRIGGERED; owner-lane.
4. **★ EXPECTED_SIGNALS revival** — ✅ **RESOLVED 7/11** (`AGENTS/LIQUID/workbook/EXPECTED_SIGNALS_TRACKER.md`, ES-LIQ-01..05). Scope call landed as the **~5-signal re-home**, not the full-12 revival. *(Closed 2026-07-12 per DAEDALUS self-sweep.)*
5. **NEXUS_BRIEF — do NOT auto-build.** Surface the deferred-design call to Will/PROME with the trade-off (crisis-outbox already covers 🔴; NEXUS_BRIEF adds routine sync). Gated.

> **DO-NOT-TOUCH (comprehension preserved — full list in `profiles/LIQUID.md §5`):** the migration-theorem framing (v2.0 load-bearing identity, redundant across §1/§4/§9 by design); the multi-doc thresholds split (CREDIT_THRESHOLDS frozen → THESIS §5 → KILL_MEMO → STATUS live — don't collapse); `KILL_MEMO_HY_OAS_260.md` filename LOCKED (7-file fan-in) + two-sided; CREDIT_THRESHOLDS HISTORICAL banner = correct hygiene; DORMANT→TRIGGERED vocab (add 5-pt alongside); "no live levels in state files"; VX/FLOW "POINT-IN-TIME registry" banner = compliant; board_log v0.2 schema; hy_oas_watch imports shared `config.py` (don't fork thresholds); boot.py exit=fetch-health-only (deliberate); research_foundations/frameworks "don't edit" (age is a feature); 7/1 mandate-extension still settling. **A no-book DATA agent — do NOT impose a TRADE.md or skeleton scaffolding.**
