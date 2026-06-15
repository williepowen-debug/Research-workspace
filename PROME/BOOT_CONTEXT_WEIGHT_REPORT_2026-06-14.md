# Prome Boot / Injected Context Weight Report — 2026-06-14

**Generated:** 2026-06-14 21:55 ET  
**Scope:** injected/root docs, mandatory boot path, conditional boot docs, and large on-demand Prome references after handoff merge/prune + BOOT slim-down + root MEMORY prune.  
**Method:** local file character/word/line counts; token estimate is rough `chars / 4`.

---

## Executive Read

The context cleanup is now materially better.

1. **Handoff merge/prune worked:** former live continuity burden fell from roughly **62k chars / 8.8k words** to roughly **5.7k chars / 721 words** live. Bulk history now sits in `PROME/archive/HANDOFF_2026Q2.md` and is on-demand only.
2. **BOOT slim-down worked:** `PROME/BOOT.md` fell from **13,067 chars / ~3,267 tokens** to **5,342 chars / ~1,336 tokens** after a clarity pass — a ~59% reduction in that file.
3. **Mandatory boot path fell:** mandatory boot docs dropped from **41,264 chars / ~10,316 tokens** to **33,539 chars / ~8,385 tokens** — about a 19% reduction.
4. **Injected root memory fell:** `MEMORY.md` dropped from **11,969 chars** to **7,665 chars**, with the original archived at `memory/archive/MEMORY_ROOT_PRE_PRUNE_2026-06-14.md`.

Current practical live boot/injected burden:

| Bucket | Files | Chars | Rough tokens | Words |
|---|---:|---:|---:|---:|
| Injected root docs | 7 | **26,812** | **~6,701** | 3,782 |
| Mandatory boot path | 6 | **33,265** | **~8,316** | 4,748 |
| Conditional boot docs | 6 | **48,958** | **~12,238** | 7,130 |
| Large on-demand refs | 9 | **138,132** | **~34,533** | 20,236 |

**Practical live load after new boot path + MEMORY prune + STATUS correction:** injected root + mandatory boot = about **60.2k chars / ~15.0k rough tokens** before user/task context. Conditional docs are no longer automatically loaded unless relevant.

---

## Heaviest Current Live / Boot-Relevant Files

| Rank | File | Bucket | Chars | Rough tokens | Words | Notes |
|---:|---|---|---:|---:|---:|---|
| 1 | `MEMORY.md` | injected root | **7,663** | ~1,916 | 964 | Pruned to durable kernels with pre-prune archive preserved. |
| 3 | `PROME/STATUS.md` | mandatory boot | **7,376** | ~1,844 | 1,018 | Slimmed; agent map corrected after Jun14 status mtime check; no longer duplicates full dashboard. |
| 2 | `HEARTBEAT.md` | injected root | **7,554** | ~1,888 | 1,115 | Injected; owns regime/thresholds/near gates. Overlaps TODAY. |
| 5 | `PROME/ACTIVE_DECISIONS.md` | mandatory boot | **6,318** | ~1,580 | 853 | Safety-critical; trim carefully only after position reconciliation. |
| 6 | `PROME/TODAY.md` | mandatory boot | **6,270** | ~1,568 | 1,026 | Duplicates HEARTBEAT levels/gates; can become shorter operator card. |
| 7 | `PROME/HANDOFF.md` | mandatory boot | **5,242** | ~1,310 | 665 | Reasonable after merge; keep latest 3–5 live. |
| 8 | `PROME/BOOT.md` | mandatory boot | **5,342** | ~1,336 | 700 | Now acceptable; clarity pass added safe-pull/staged-file guidance. |
| 8 | `USER.md` | injected root | 3,243 | ~811 | 455 | High-signal; leave alone. |
| 9 | `AGENTS.md` | injected root | 3,221 | ~805 | 546 | High-signal roster/spawn rules; leave alone. |
| 10 | `TOOLS.md` | injected root | 3,130 | ~782 | 382 | Still overlaps some tool pointers, but small enough. |
| 11 | `PROME/SCRATCH.md` | mandatory boot | 2,717 | ~679 | 353 | Reasonable. |
| 12 | `SOUL.md` | injected root | 1,986 | ~496 | 318 | Small/high-signal; leave alone. |

---

## Conditional / On-Demand Heavy Files

These are heavy, but no longer normal boot material.

| File | Chars | Rough tokens | Status |
|---|---:|---:|---|
| `PROME/archive/HANDOFF_2026Q2.md` | **62,361** | ~15,590 | Archive only. Do not boot-read. |
| `PROME/ORCHESTRAL_LAYER_DESIGN.md` | 16,221 | ~4,055 | Only when scoring/spawning/orchestration design matters. |
| `PROME/CLOSEOUT.md` | 12,653 | ~3,163 | Read before closeout, not boot. Now includes manual write-back contract. |
| `PROME/SYSTEM.md` | 11,608 | ~2,902 | Architecture reference; not normal boot. |
| `PROME/TRADE_DECISIONS.md` | 10,331 | ~2,583 | On-demand for position reconciliation. |
| `PROME/CLAUDE_CODE_PROME_PLAN.md` | 9,765 | ~2,441 | Claude Code Prome build only. |
| `PROME/CLAUDE_CODE_PROME_TASKS.md` | 9,578 | ~2,394 | Claude Code Prome build only. |
| `PROME/FLEET_SCAN.md` | 8,866 | ~2,216 | Conditional boot only. |

---

## Best Remaining Cleanup Opportunities

### 1. `STATUS.md` + `TODAY.md` + `HEARTBEAT.md` overlap

**Problem:** These three carry overlapping regime, levels, gates, and follow-ups.

**Target owner model:**
- `HEARTBEAT.md` owns regime/thresholds/near gates because it is injected.
- `TODAY.md` owns today-specific operator task list and immediate catalysts.
- `STATUS.md` owns agent/system health and work queue, not dashboard/regime narrative.

**Recommended next pass:**
- Remove full dashboard anchor from `STATUS.md`; reference `HEARTBEAT.md` / `TODAY.md`.
- Shorten `TODAY.md` to top gates, do/do-not, current tasks.
- Keep `HEARTBEAT.md` as compressed regime card; avoid duplicating every level in `TODAY` unless actively used.

**Potential live reduction:** **5–8k chars**.

### 2. `MEMORY.md`

**Status:** pruned successfully to durable kernels. Original preserved in `memory/archive/MEMORY_ROOT_PRE_PRUNE_2026-06-14.md`.

### 3. `ACTIVE_DECISIONS.md`

**Recommendation:** Do **not** trim first. It prevents stale trade-action mistakes. After position reconciliation, archive dead/candidate rows and keep only true live decisions + explicit dead rows.

### 4. `CLOSEOUT.md`

Now heavier because it includes the manual write-back contract. That is acceptable because it is not boot-loaded; read only before closeout. Do not optimize yet.

---

## Bottom Line

The first two cleanup moves were successful:

- Handoff live burden removed.
- BOOT converted from mini-manual into executable checklist.

The next best cleanup is **deduplicating `TODAY.md` and `HEARTBEAT.md`** now that `STATUS.md` and `MEMORY.md` have been pruned/corrected.
