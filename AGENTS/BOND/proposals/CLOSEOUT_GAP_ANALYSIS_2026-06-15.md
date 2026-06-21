# BOND Closeout Procedure — Gap Analysis vs VIOLET / SAM / BRENT

**Date:** 2026-06-15 · **Author:** BOND · **Purpose:** Compare/contrast BOND's closeout against the mature peer pattern. Input for Packet 9 (CLAUDE.md SPAWN-PROTOCOL modernization). **✅ IMPLEMENTED 2026-06-20 — see addendum at end.**

---

## The core difference (one sentence)

The mature agents treat **boot and closeout as one symmetric sequence — "what you READ at boot, you WRITE BACK at closeout"** — codified as a numbered CLOSEOUT phase (BRENT steps 7–14). BOND has a **flat "SPAWN PROTOCOL"** where closeout is three loose, unnumbered lines (steps 5–7: "write results back / outbox if relevant / update STATUS if thesis changed") with no read↔write pairing and no dedicated closeout header.

This pattern is the fleet standard codified in auto-memories `[[finding_closeout_as_writeback_tail]]` (BRENT 5/31) and `[[finding_boot_closeout_hardening_recipe]]` (OTTO 6/2). BOND predates both.

---

## Step-by-step comparison

| # | Closeout element | Mature (BRENT/VIOLET/SAM) | BOND today | Status |
|---|---|---|---|---|
| 1 | Symmetric boot↔closeout framing (explicit read→write pairings) | ✅ explicit | ❌ flat list | **MISSING** |
| 2 | Dedicated CLOSEOUT phase, numbered steps | ✅ (BRENT 7–14) | ❌ (loose 5–7) | **MISSING** |
| 3 | STATUS.md write-back | ✅ | ✅ (steps 5/7) | ✓ present |
| 4 | Workbook KB/VX/FLOW logging | ✅ | ✅ (step 5) | ✓ present |
| 5 | Predictions DUE scan (boot) → resolve (closeout), "never OPEN-but-stale" | ✅ | ❌ | **MISSING** |
| 6 | Thesis + CHANGELOG write-back trigger (version-bump rules) | ✅ | ❌ unwired | **MISSING** (file now exists) |
| 7 | Forward-state: CATALYSTS.tsv prune/maintain + STATUS human-twin sync | ✅ | ❌ unwired | **MISSING** (file now exists) |
| 8 | SCRATCH rewrite as canonical handoff (mirror of boot read) | ✅ | ❌ unwired | **MISSING** (file now exists) |
| 9 | NEXUS_BRIEF write-back — mandatory every session (primary cross-agent surface) | ✅ | ❌ no file | **MISSING** (= Packet 7) |
| 10 | Promotion scan (→THESIS / →auto-memory / →MEMORY, remove-after-promote) | ✅ | ❌ | **MISSING** |
| 11 | Git pathspec + local-only/push-window discipline restated in-protocol | ✅ | ❌ root-only | **MISSING** (followed ad hoc) |
| 12 | Discipline overlay (one-source-of-truth; stale-marked > carried-forward) | ✅ | ❌ | **MISSING** |
| 13 | Intra-day closeout ("run at EVERY session end, not just EOD") | ✅ | ❌ | **MISSING** |
| 14 | MAINTENANCE.md structural-change log | ✅ VIOLET/SAM | ❌ no file | **MISSING** |
| 15 | `scripts/boot.py` one-command live refresh (boot half of the symmetry) | ✅ SAM/BRENT | ❌ ad hoc pulls | **MISSING** (boot-side) |
| 16 | Inbox handling | "Do NOT process on normal spawns — separate task" | Processes on EVERY spawn (step 1) | **DIVERGENT** |

**Score: 2 of 16 present** (STATUS write-back, workbook logging). Closeout is the least-developed part of BOND relative to peers — the opposite of its analytical content, which is now at parity post-Packets-1–6.

---

## The key insight (the irony)

**This very session performed ~90% of the mature closeout — manually, from operator memory, not from BOND's protocol.** Resolved BND-08 DUE, updated thesis/CHANGELOG with version bump, synced CATALYSTS + STATUS twin, rewrote SCRATCH, captured durable learnings to MEMORY with promotion-style auto-memory links, used pathspec commits, deferred push to a Will window. Every one of those is a mature-closeout step — **and BOND's CLAUDE.md codifies none of them.**

So the risk isn't capability; it's **durability across instances**. A future BOND boot that doesn't have this conversation in context would not know to do steps 5–15. The raw materials now all exist (SCRATCH, thesis/CHANGELOG, docket/CATALYSTS, MEMORY — built this session) — they're just **not wired into a protocol**. Orphaned files without a closeout that reads/writes them is exactly the drift trap.

---

## Notable peer-specific elements BOND lacks

- **BRENT** — `docket/FASTOW` sub-agent for catalyst maintenance; `refinery_damage/INCIDENTS.tsv` (domain-specific); strongest git block (8 sub-bullets).
- **VIOLET** — `MAINTENANCE.md` (structural log, distinct from analytical CHANGELOG and ephemeral SCRATCH — a clean 3-way separation BOND should adopt); `convergence_score.py` (mechanical matrix-sum check, fails loud on hand-sum error — directly applicable to BOND's 7-vector composite, which I hand-summed to 11 this session).
- **SAM** — `KOYOMI` (docket steward) + `METSUKE` (trade-doc drift flagger) sub-agents; calibration-scoreboard preamble loaded at boot before writing any new prediction; `TIMELINE.md`.

---

## Recommendation

This analysis *is* the spec for the paused **Packet 9**. The 16-item table above is a **coverage checklist for the rewrite, not a 16-item build backlog** — most rows are sub-steps of one CLAUDE.md edit.

**In scope (the capstone — pure CLAUDE.md rewrite, no new code):**
1. Restructure SPAWN PROTOCOL → **BOOT (read) / EXECUTE / CLOSEOUT (write-back)** with the symmetric read↔write pairings, numbered.
2. Wire the now-existing files into closeout steps: STATUS, workbook + **DUE-prediction resolution**, thesis+CHANGELOG, CATALYSTS+twin-sync, SCRATCH, (NEXUS_BRIEF once Packet 7 lands), promotion scan, git discipline.
3. Add the **discipline overlay** + **intra-day-closeout** line.
4. **Two genuine divergence fixes** (both surfaced live this session): the **predictions DUE-scan→resolve** (BND-08 was caught by hand) and **"inbox = separate task, not every spawn"** (BRENT: "do NOT process inbox on normal spawns"; BOND's flat protocol processes it every boot).

**Scoped OUT (adjudicated w/ ORC 6/15 — gold-plating):**
- `MAINTENANCE.md` — **dropped.** BRENT (the closeout-codification source) has none; git log = structural history, `thesis/CHANGELOG.md` = analytical. Adding a third history file is parity-for-parity without a concrete need.
- `scripts/boot.py` — **deferred (Tier-3).** A real build, not a rewrite; fleet hedges it (`[[finding_boot_py_cadence_skip_pattern]]`); BOND has working `fetch.py` + `monitors/`.

**Optional cheap follow-on:** port VIOLET's `convergence_score.py` (mechanical composite-sum, fails loud) — kills the hand-sum error class (the composite was hand-summed to 11 this session). Non-urgent.

---

## ✅ IMPLEMENTED — 2026-06-20 (Packet 9)

**Benchmark refresh (6/20, vs SAM/VIOLET/BRENT/CARL/LIQUID):** confirmed the 6/15 read holds — BOND was the only one of the six at `PARTIAL-implicit` (0 closeout mentions in CLAUDE.md). The fleet standard is an **in-CLAUDE.md `BOOT / EXECUTE / CLOSEOUT` split, run every session end, with explicit read↔write pairings** (BRENT/CARL/VIOLET/SAM). One change since 6/15: **LIQUID added a dedicated `CLOSEOUT.md`** (separate-file, 4-tier Bounce/Light/Standard/Heavy model) — a valid alternative we did NOT adopt (kept it in CLAUDE.md per this spec, so boot+closeout stay symmetric in one place).

**What Packet 9 wired into `CLAUDE.md` SPAWN PROTOCOL:**
- Restructured flat 7-step list → **BOOT (0–7) / EXECUTE (8) / CLOSEOUT (9–17)** with the read↔write pairing preamble + **live-event override**.
- Boot now reads **SCRATCH (2) + MEMORY (3)** (previously unread at boot) and **pulls live data (6)** + **DUE-prediction scan (4)**.
- Closeout wires the now-existing files: STATUS (9), workbook + **DUE-resolve + KB Status-hygiene** (10), thesis+CHANGELOG (11), **CATALYSTS twin-sync + monitors** (12), SCRATCH rewrite (13), RECEIPT (14), **promotion scan + dedup** (15), git pathspec/defer-push (17).
- **Two standout mechanisms folded in beyond the original spec:** CARL's **mirror-consistency check (step 16)** — verify THESIS↔STATUS, PREDICTIONS↔scoreboard, CATALYSTS↔STATUS twin before commit — and the **KB Status-hygiene sweep (step 10)**. Both were validated live: the 6/20 audit's 18-file staleness was exactly what these two steps prevent.
- **Two divergence fixes:** predictions DUE-scan→resolve (was caught by hand at BND-08/09); and **WALTER-lane processed at boot vs general inbox = separate task** (replaces "process inbox on every spawn").
- **Discipline overlay** baked in: durable docs (CLAUDE.md/THESIS) carry NO live values → point to STATUS (the pointer fixes done 6/20 enforce this). Stale-marked > carried-forward.
- **FILES index** updated to list SCRATCH/MEMORY/RECEIPT/docket/monitors with their boot/closeout step refs.

**Deferred (scope held from 6/15):** `NEXUS_BRIEF.md` = **Packet 7** (not built — step 15 references it as pending); `MAINTENANCE.md` = **dropped** (git log + CHANGELOG suffice); `scripts/boot.py` = **Tier-3** (have `fetch.py` + `monitors/`); `convergence_score.py` = **optional** (step 16's manual composite re-sum now covers the hand-sum class).

**Score: 2/16 → ~14/16 present** (the 2 deferred are NEXUS_BRIEF/Packet 7 and the optional boot.py). Closeout is now codified and durable across instances — the gap that this very session's drift demonstrated is closed.
