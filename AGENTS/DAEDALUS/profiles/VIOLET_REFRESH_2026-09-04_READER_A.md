# VIOLET — Profile refresh, Cluster A (identity · state · handoff)

**Reader A (Mode-A, READ-ONLY) · 2026-09-04 (Fri) · for DAEDALUS.** Paths relative to `AGENTS/VIOLET/` unless prefixed. No VIOLET script executed. **Context:** 9/4 = 11 desk commits 08:47→17:17, a crash, and two Codex review rounds that found VIOLET's "5/5 green" closeout defective twice. Most findings are residue of that day, not chronic rot; the standing gap is **diagnosis written → not mechanized**.

---

## 1. Boot reads and byte sizes (`CLAUDE.md:20-40`)

| Step | Read | Bytes | Seen by `read_cap_check`? |
|---|---|---|---|
| 0 | `git pull` (`:21`) | — | n/a |
| 1 | `STATUS.md` (`:22`) | **32,546** | ✅ |
| 2 | `SCRATCH.md` (`:23`) | **17,997** | ❌ **INVISIBLE — §9-1** |
| 3 | `MEMORY.md` hot half (`:24`) | **21,457** | ✅ |
| 4 | `CALENDAR.md` + `workbook/CATALYSTS.tsv` (`:25`) | **20,880** + **3,930** | ✅ |
| 5·5a·5b·5c | `boot.py` (13 stages) · `ledger_staleness.py` ×2 · WALTER lane · `corrections_boot_check.py` (rc=0) | opaque | ❌ |

**Total whole-read = 96,810 B against a 54,250 B cap = 178%.** `read_cap_check.py --agent VIOLET` returns **rc=0** because it grades **per file, never the sum** (`:221-222` — only counts of over-budget files); STATUS.md is flagged `rotate-tier` in that same clean run. **Pointer-defined/opaque:** everything inside `boot.py` (tool: *"boot.py-internal reads … NOT seen"*). Two lines correctly carry `WRITE/append target — never a boot whole-read` markers (`CLAUDE.md:47`, `:54`).

---

## 2. Write-back: mechanism vs sentence (`CLAUDE.md:45-63`)

Blocking code = `closeout_guard.py:67-72` (5 contracts) + `:73-75` (1 advisory).

| Step | Mechanized? | Evidence |
|---|---|---|
| 7 STATUS + BOTTOM LINE | ⚠️ vintage only | `closeout_guard.py:71` |
| 8 workbook/ledgers | ✅ blocking — **KB.tsv only** | `:70`; gap at `STATUS.md:172` |
| 9 thesis bump | 🟡 **advisory, never blocks** | `:74`, `CLAUDE.md:60` |
| 10 CATALYSTS↔CALENDAR twin | ✅ blocking (built 9/4) | `:72` |
| 11/11a/12 SCRATCH·LAST_COMPLETION·BRIEF | ✅ **vintage only** | `writeback_order_check.py` |
| **13 promotion scan (auto-memory/MEMORY)** | 🔴 **SENTENCE ONLY** | `CLAUDE.md:54` |
| **13a MAINTENANCE structural entry** | 🔴 **SENTENCE ONLY** | `:55` |
| 13b closeout guard · 14 git+safe-push | ✅ | `CLAUDE.md:56-63` |
| **root 1b–1e** (orphan·consumer·ledger·memory·claim) | 🔴 **NOT NAMED IN THE CHARTER AT ALL** | `CLAUDE.md:63` cites only §Git Protocol |

**Remaining SENTENCE-ONLY: 13, 13a, and the whole root 1b–1e battery.** `consumer_check` did run 9/4 (`LAST_COMPLETION.md:10`) — from session memory, not a step. Two caps also claim a mechanism that does not exist (§6).

---

## 3. Handoff agreement TODAY — 8 contradictions

All four committed together at `f4950fa8b` 17:17 (Amendment-10 ordering satisfied). **Posture agrees cleanly** — FLAT · nothing fired · nothing proposed · FT-10 1-of-4 (`STATUS.md:24,143` · `SCRATCH.md:85` · `LAST_COMPLETION.md:3` · `NEXUS_BRIEF.md:94`). Eight disagreements:

| # | Claim | Side A | Side B |
|---|---|---|---|
| **C1** | Convergence score | `STATUS.md:97` "**25/55**"; `NEXUS_BRIEF.md:18` "**26 → 25**" | `STATUS.md:113` "**FLAT at 26**"; `SCRATCH.md:85` "**26/55**"; `NEXUS_BRIEF.md:94` "**26/55, unchanged in total**" |
| **C2** | KB rows since v4.0 | `STATUS.md:180` "**12** KB rows (214→225)" | `STATUS.md:167` "**29** rows, 2 retractions"; `NEXUS_BRIEF.md:94` "**20** rows (1 retraction)" |
| **C4** | Post-NFP measurement | `STATUS.md:28-51` graded; `NEXUS_BRIEF.md:94` "discharged" | `STATUS.md:135` "**owed, not taken**"; `:137` "Owed: the post-open reaction measurement" |

**C7** short-vol book, *within one file*: `NEXUS_BRIEF.md:18` "−26,258 … **deepening STOPPED**" vs `:73` "**−30,143 deepened three reports running**". **C3** sessions on 9/4: `STATUS.md:3` "**THREE SESSIONS**" / `SCRATCH.md:1` "third session" vs `STATUS.md:12` "**SIX SESSIONS RAN 2026-09-04**". **C5** inbox: `:5` "**DRAINED 7/7**" (empty on disk) vs `:137` "the **6-item** top-level inbox lane as its own pass". **C6** vintage: commit `f4950fa8b` **17:17** vs `:188` "*Last write-back: …**~09:0x ET***". **C8** cap: `LAST_COMPLETION.md:4` "**cap cleared**" vs `SCRATCH.md:63` "**317 lines vs ~300 cap**" (§6).

**C1/C2/C4/C6 share one mechanism:** STATUS's `## BOTTOM LINE`, `## THESIS CONNECTION` and footer were **not rewritten** in the 13:1x→17:17 passes while header, dashboard, matrix and queue were — the limitation VIOLET wrote into its own guard's docstring (*"compares VINTAGE, never CONTENT"*, `NEXUS_BRIEF.md:25`), landing on its author one session later.

---

## 4. STATUS.md — size, rotation, headroom

**32,546 B** against a **32,550 B** budget (60% of the 54,250 cap) ⇒ **4 bytes of headroom = 99.99%**; 188 lines vs the 250 cap (`CLAUDE.md:46`). Guard verdict: 🟡 `rotate-tier` **but rc=0**.

**Rotation:** manual, byte-verbatim + crc32 → `archive/STATUS_SESSION_LOG_<date>.md`; ran **three times on 9/4** (crc `d6091a4c` at `STATUS.md:12`; archive 9,530 B). Nothing *triggers* it — the only guard is rc=0 at 99.99%, so the next 5-byte edit breaches silently.

**Movable cold (~6-8 KB ≈ 20% headroom):** `:28-51` (completed, graded NFP event → session log); `:149-158` `## CROSS-AGENT SIGNALS`, **verbatim duplicated** at `NEXUS_BRIEF.md:39-58`; `:182-186` thesis narrative → `CHANGELOG.md`.

---

## 5. MEMORY.md (21,457 B, boot step 3)

**~95% settled lessons, ~5% live state** (principles `:9-18` · pointers `:24,:49` · analogs `:36-43` · patterns `:55-104` · semantics `:108-138` · data sources `:156-173`). The 9/2 hot/cold split (21,363 B verbatim, cksum-verified) was clean. **Stale / contradicted:**
1. 🔴 **`:168`** *"CFTC TFF release schedule — Tue close → Fri 3:30 PM ET release; `cftc_cot.py --boot` … 'use prior week's Tuesday'."* — the synthesized calendar VIOLET got **wrong three times on 9/4** and then removed (*"v4 makes no calendar claim at all"*, `NEXUS_BRIEF.md:13`, KB-VIO-243). The boot-read memory still teaches the retracted model.
2. 🟠 **The 9/4 `^SKEW` two-mode defect is absent from `## Known data caveats` (`:164-173`)** — omission 8/28 + value disagreement 2025-12-24, 2/253 = 0.79% (KB-VIO-215/221/236/241). It lives only in STATUS/BRIEF, which rotate; step 13 should carry it.
3. 🟡 **`:169`** cites *"SCRATCH 7f"* — no such item; dangling. **`:84`** *"6/7 historical episodes with SKEW peak >150 produced STRESS +50%"* — unqualified against the desk's own rule (`README.md:42`), and `^SKEW` printed 150.63 today, so it is live-load-bearing.

---

## 6. MAINTENANCE.md

Cap **~300 lines** (`MAINTENANCE.md:9`, `:131`) · current **259 lines / 49,179 B** · headroom 41 lines (86%). **Mechanized? 🔴 NO** — `check_maintenance_cap()`, named at `:131` as *"enforced at boot"*, has **0 hits repo-wide**, and `boot.py` never reads MAINTENANCE; `README.md:12,17` calls both this cap and STATUS's 250-line cap *"boot-enforced"*. The 9/4 archival (317 → 268, `:168`) was by hand; `SCRATCH.md:63` still carries the pre-archival count **and** the false "boot flags it" claim.

---

## 7. Inbox / outbox

**Inbox clean** — top level and `inbox/WALTER/` empty, the deferred `git mv` at `board_log.tsv:33` completed (`SCRATCH.md:47`); `board_log.tsv` = 112 rows, v0.2 header, well-formed. **Outbox: 8 packets at top level = "NOT YET DELIVERED" (`outbox/README.md:15`); 7 are >7 days old.**

| Packet (age d) | Delivery evidence |
|---|---|
| `2026-08-04b_to-PROME_BIN-A-return-leg` (31) · `2026-08-20_to-PROME_rising-vol-DESIGN-v1` (15) · `2026-08-27_to-PROME_F2-KILLED` (8) · `2026-08-27_to-PROME_GATE-VIO-RV1-FIRED` (8) · `2026-09-02_to-PROME_31-drained` (2) | ✅ all five in `PROME/inbox/processed/` |
| `2026-08-04c_to-LIQUID_issue-level-HY-breadth` (31) · `2026-08-27_to-TERRY_beta-0274-bucketing-bug` (8) · `2026-08-27_to-PROME_GATE-VIO-RV1-transcription-verified` (8) | ❌ **no trace anywhere** |

**5 of 8 are provably delivered and were never `git mv`'d to `delivered/`.** The two 9/4 packets bypassed the outbox entirely (straight to `PROME/inbox/` — now `processed/` — and `AGENTS/VULCAN/inbox/`). The 7/30 lifecycle has stopped being run; the directory's signal is inverted.

---

## 8. Self-corrections, last 7 days (`corrections_boot_check` rc=0, 0 unreceipted)

| # | Correction | Propagated everywhere? |
|---|---|---|
| 1 | `^SKEW` "OMITS 8/28" → **transient/healed** (215→221); FT-10 margin 0.77 → **0.23**; one `^SKEW` defect mode → **two** (236) | ✅ `STATUS.md:16,83,8,166` · `NEXUS_BRIEF.md:60,58,43` · RED packet |
| 2 | MU ~9/29 → ~9/22 → **9/30 CONFIRMED** (235) | ✅ CATALYSTS · CALENDAR · `STATUS.md:6` · `NEXUS_BRIEF.md:46` · VULCAN packet; 11 fleet flags, 7 false (`LAST_COMPLETION.md:10`) |
| 3 | "gamma UNMEASURED" → **NEGATIVE, measured 9/2** (237); KB-VIO-242 "all four fixed" → CORRECTED | ✅ `STATUS.md:7,153` · `NEXUS_BRIEF.md:40` · `SCRATCH.md:91` · `LAST_COMPLETION.md:9` |
| 4 | COT guard v1/v2/v3 wrong → **v4, no calendar** (243) | ⚠️ **PARTIAL — `MEMORY.md:168` still teaches the retracted model** |
| 5 | "third consecutive COT deepening" → superseded | ⚠️ **PARTIAL — `NEXUS_BRIEF.md:73` still asserts it (C7)** |

**6 of 8 fully propagated; both survivors sit in *narrative* blocks** (a memory caveat, a standing-tension paragraph), not dashboards — same shape as C1/C2/C4/C6.

---

## 9. TOP 5 — what needs help

**1. 🔴 `SCRATCH.md` (17,997 B) is invisible to the read-cap guard, and nothing checks the SUM. — DAEDALUS (tooling).**
`CLAUDE.md:23` *"**Read `SCRATCH.md`** — ephemeral handoff **from last session** …"*; the substring `"last "` is in `SCOPE_MARKERS` (`scripts/read_cap_check.py:77-79`), so the file scores *scoped* and drops out. **Risk:** true boot load **96,810 B = 178% of cap** while the guard returns **rc=0**; every charter saying "from last session"/"the last N" under-counts identically, and the heuristic's own comment claims it *"can only OVER-count, never under"* (`:70-74`) — the bias runs opposite to its stated direction. Fixes: require the scope marker inside the verb→token window, not the free tail; and grade a **TOTAL** against the cap.

**2. 🔴 `MEMORY.md:168` still teaches the CFTC calendar VIOLET retracted the same day (§5-1). — VIOLET (desk).**
**Risk:** MEMORY.md is a boot whole-read and STATUS rotates, so within two sessions the retracted model is the only surviving statement and the desk re-derives v3 from its own memory. It survived because step 13 (`CLAUDE.md:54`) is sentence-only.

**3. 🟠 Two caps advertise a mechanism that does not exist (§6). — DAEDALUS (structure) → VIOLET (build).**
`MAINTENANCE.md:131` *"enforced at boot by `check_maintenance_cap()`"* (0 hits repo-wide); `README.md:12,17` *"boot-enforced"* for both caps; `SCRATCH.md:63` *"boot flags it every session"* for a 259-line file. **Risk:** a *named, non-existent* check reads as coverage — the class VIOLET logged **n=6 in one day** (`SCRATCH.md:82`), in the file that logs it.

**4. 🟠 STATUS.md's summary blocks are not rewritten with its body — C1/C2/C4/C6 (§3). — VIOLET; DAEDALUS guard opportunity.**
**Risk:** the convergence score (`:97` 25 vs `:113` 26) and the thesis-currency counter (`:180` 12 vs `:167` 29 vs `NEXUS_BRIEF.md:94` 20) are the two numbers other desks quote out of this surface, and a reader takes whichever they hit first. `writeback_order_check.py` is vintage-only **by construction**; a *within-file* numeric-consistency check (one metric name, two values, one document) is buildable and catches C1, C2, C7.

**5. 🟠 The `outbox/` lifecycle has stopped being run and now carries anti-signal (§7). — VIOLET (desk), PROME leg.**
`outbox/README.md:15`: *"**If anything is here, it is owed.**"* — 8 files, 5 provably delivered, oldest 31 days; the two packets shipped 9/4 never touched it. **Risk:** the 7/30 audit that created this lifecycle cost *"a directory-wide audit that should have been a `git mv` at send time"* (`:9`) — owed again five weeks later. PROME leg: `to-PROME` packets are structurally unverifiable from VIOLET's side (`:30`).

---

*Reader A · read-only.*
