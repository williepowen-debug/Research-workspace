# Boot Sequence Audit — 2026-03-12 16:08 UTC

_Performed by subagent cold-booting with zero prior context._

---

## 1. Injected Project Context — What I Received

| File | Present? | ~Size | Content Summary |
|------|----------|-------|-----------------|
| AGENTS.md | ✅ | ~2.5KB | System purpose, boot pointer, safety, signal processing, file editing rules, core principles |
| SOUL.md | ✅ | ~1.5KB | Identity (Prome), personality, boundaries, vibe |
| USER.md | ✅ | ~3KB | Will's background, communication style, motivation, thinking patterns |
| TOOLS.md | ✅ | ~0.1KB | Just a note about pdfminer |
| IDENTITY.md | ✅ | ~0.5KB | Blank template — NOT filled in (redundant with SOUL.md?) |
| **HEARTBEAT.md** | ❌ | — | **Not injected. BOOT.md says it should be.** |
| **MEMORY.md** | ❌ | — | **Not injected. BOOT.md says it should be.** |

**Issue:** BOOT.md explicitly says "AGENTS.md, SOUL.md, USER.md, HEARTBEAT.md, and MEMORY.md are auto-injected." But HEARTBEAT.md and MEMORY.md were NOT injected. Either they don't exist, or injection config is wrong. This is a discrepancy that would confuse a fresh session.

---

## 2. Boot Pointer — Did It Work?

**AGENTS.md says:** "At session start, read `PROME/BOOT.md` then follow its sequence."

**Verdict: Clear and worked.** One line, unambiguous. I knew exactly what to do. The pointer is in its own `## Boot` section which is easy to find.

---

## 3. BOOT.md Sequence — Step by Step

| Step | File | Found? | Notes |
|------|------|--------|-------|
| 1 | PROME/SCRATCH.md | ✅ | Rich, current (updated ~14:30 UTC today). Excellent orientation — I immediately knew the trading day, positions, pending work. |
| 2 | PROME/STATUS.md | ✅ | Comprehensive dashboard. Agent table, positions, convictions, dates, pending actions. Updated today. |
| 3 | LESSONS.md | ⚠️ | BOOT.md says `LESSONS.md` — no path prefix. It's at workspace root, not `PROME/LESSONS.md`. I tried `PROME/LESSONS.md` first (ENOENT), then guessed root. **Should specify full path.** |
| 4 | memory/YYYY-MM-DD.md | ✅ | Today + yesterday both exist and are rich. Path was clear. |

**Total boot reads: 6 files (BOOT + SCRATCH + STATUS + LESSONS + 2 memory files).** Reasonable. Took ~15 seconds of wall time for a subagent.

---

## 4. Audit Questions

### Did the AGENTS.md boot pointer work? Was it clear?
**Yes, 9/10.** Single line, exact path, imperative verb. Only improvement: could say "then follow its numbered sequence" to make it even more explicit that BOOT.md contains ordered steps.

### Did BOOT.md have everything needed to orient?
**Mostly yes, 7/10.** It covers boot, handoff, memory, sub-agents, NEXUS, and reference files. What's missing:
- No "what is this system about" summary. I got that from AGENTS.md, but if BOOT.md is supposed to be self-contained for orientation, a one-liner like "You're Prome, running a macro-financial research operation" would help.
- The handoff section is detailed but I don't need it at boot — it's noise during cold start. Consider moving it to a separate file or putting it after boot steps.
- BOOT.md is ~40% handoff instructions that are irrelevant at boot time. The boot sequence itself is only ~10 lines.

### Any confusion, missing info, or dead references?
1. **LESSONS.md path ambiguity** — BOOT.md says `LESSONS.md`, all other files use `PROME/` prefix. Broke my first attempt.
2. **HEARTBEAT.md / MEMORY.md claimed as injected but aren't.** Either create them, inject them, or update BOOT.md to not claim they're injected.
3. **IDENTITY.md is injected but blank and redundant with SOUL.md.** Noise.
4. **`docs/OPERATIONS.md`** and **`AGENTS_DIRECTORY.md`** referenced but I didn't verify they exist (not needed at boot, but if they're dead links that's a problem for later).

### Did I feel the urge to re-read any injected file?
**No.** The injected files were sufficient for what they cover. AGENTS.md gave me system purpose and safety. SOUL.md gave me personality. USER.md gave me Will's context. I never went back to re-read any of them. **This means the injection is working well.**

### Is Signal Processing in AGENTS.md clear enough?
**Barely, 5/10.** It gives 4 steps (Triage → Extract → Log → Assess) and points to `PROME/SIGNAL_PROTOCOL.md` for full protocol. The 4 steps are sensible but vague:
- "Which agent owns this?" — I'd need to know agent domains. The transmission chain diagram helps, but without reading AGENTS_DIRECTORY.md I'd be guessing for agents like OTTO, MARCO, DARWIN, HANS, BRENT.
- "Update relevant STATUS.md" — which one? Agent's STATUS.md? PROME/STATUS.md? Both?
- "Alert if threshold hit" — what thresholds? Where are they defined?

For a cold boot, the signal processing section is a pointer, not instructions. That's probably fine IF `SIGNAL_PROTOCOL.md` exists and is complete.

### Is the Safety section complete?
**Adequate, 7/10.** Covers:
- ✅ No data exfiltration
- ✅ trash > rm
- ✅ Internal vs external action distinction
- ✅ Trade proposal approval flow

**Missing:**
- No guidance on what to do if Will is unreachable and something urgent happens
- No mention of position sizing limits or max risk per trade
- No guidance on what constitutes "private data" (is trade P&L private? Agent statuses?)
- The trade approval flow is clear but doesn't say what to do if approval times out

### Any gaps where I wouldn't know what to do?
1. **Agent spawning** — BOOT.md references `sessions_spawn()` syntax but that's not a tool I have. The actual tool is `subagents`. Minor but could cause a failed first attempt.
2. **HERMES outbox delivery** — SCRATCH.md mentions HERMES outbox backlog but there's no guidance on what HERMES is or how to run it.
3. **"Be proactive"** — BOOT.md step 5 says this but doesn't define what proactive actions are appropriate at boot. Check agent statuses? Process inboxes? Just wait?
4. **Git operations** — Handoff says `git commit` but no guidance on whether git is configured or what repo this is.

---

## 5. Overall Rating

**7/10 — Good, not great.**

**What works well:**
- Boot pointer is crisp and unambiguous
- SCRATCH.md as "read first" is brilliant — it's the fastest way to get current context
- STATUS.md is a well-designed dashboard
- The file hierarchy makes sense (PROME/ for Prome's stuff, memory/ for daily, root for cross-cutting)
- Injected files cover identity, user, and system without redundancy (except IDENTITY.md)

**What needs fixing:**
- LESSONS.md path should be explicit (`LESSONS.md` at root, not implied)
- HEARTBEAT.md / MEMORY.md injection discrepancy — either inject them or stop claiming they're injected
- Remove blank IDENTITY.md from injection (noise)
- BOOT.md is overloaded — boot and handoff serve opposite moments. Split them or reorder so boot is clearly first, handoff is clearly "skip until needed"
- `sessions_spawn()` syntax doesn't match actual tooling

**What would make it 9/10:**
- Fix the three dead/wrong references
- Add a 1-line system summary to BOOT.md ("You're Prome. Macro-financial research op. Read down.")
- Move handoff to `PROME/HANDOFF.md` or put it after a clear `---` separator with "STOP HERE AT BOOT" marker
- Define "be proactive" with 2-3 concrete default actions

---

_Audit complete. Boot sequence is functional and well-designed but has several papercuts that would trip up a truly cold agent._
