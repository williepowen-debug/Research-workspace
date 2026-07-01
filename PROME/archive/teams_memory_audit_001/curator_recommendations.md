# Curator Recommendations — MEMORY Draft Audit

**Author:** curator (memory-audit-001)
**Date:** 2026-05-18
**Source:** `PROME/MEMORY_DRAFT_2026-05-17.md` (8 candidates)
**Bar applied:** existing root `MEMORY.md` style — event-dated, terse, quantitative anchor, ends with `→ <pointer>`. CORE DISCOVERIES = thesis-relevant findings durable over 4-12 mo. SYSTEM ARCHITECTURE = operating-model patterns load-bearing across sessions. Anything that's "what changed this session" is not the bar.

---

## Summary table

| # | Candidate | Verdict | Layer | Notes |
|---|---|---|---|---|
| 1 | WAL Investor Day → Bucket E B3 | **KEEP** (rephrase) | root CORE | Compress ~50%; thesis milestone, but specifics will move |
| 2 | FSK Q1 + PSEC 8.6 hallucination | **KEEP** (rephrase, SPLIT) | root CORE + SYSTEM ARCH | Two discoveries muddled; split FSK (CORE) from PSEC verify rule (SYS ARCH, fold w/ #8) |
| 3 | WALTER routing codification | **KEEP** (rephrase, compress hard) | root SYSTEM ARCH | Operating-model pattern; verbose in draft |
| 4 | OZK spinout to peer | **REPHRASE** (short pointer) | root SYSTEM ARCH + update existing Mar 25 entry | Most thesis content already in Mar 25 "WAL+OZK Complementary"; keep only the org-change |
| 5 | Claude Code Prome scaffold | **KEEP** (rephrase) | root SYSTEM ARCH + update "Persistent Agents" entry | "One Prome, two surfaces" is a real arch pattern |
| 6 | Agent View + teams experiment | **REJECT** for root | SCRATCH/HANDOFF only | Operational install, not lasting discovery; revisit after teams experiment yields findings |
| 7 | Hash-drift staleness | **REJECT** for root | auto-memory | Draft self-flags as feedback memory; correct call |
| 8 | Verify-against-filings rule | **REPHRASE** (fold w/ #2) | root SYSTEM ARCH | Already in CLAUDE.md Rule #3; MEMORY.md anchor with PSEC origin is worth one entry |

**Net: from 8 candidates → 4 new root entries + 2 updates to existing entries + 1 auto-memory write.**

---

## Per-candidate detail

### 1. WAL Investor Day → Bucket E B3 (May 17) — **KEEP, rephrase**

**Why keep:** Bucket E B3 confirmation is a tracked thesis-tree milestone (REG-25 scenario weight moved 10pts on confirmed Q&A admission). This is exactly the cadence of CORE DISCOVERIES like "Blue Owl Dual Gating (Apr 2)" — discrete event with quantitative scenario impact.

**Why rephrase:** Draft is 4 sentences + caveats about pending gates. Existing entries are tighter. The "no V2.2 promotion yet, gated on X+Y" is in-flight session state — belongs in REGINALD STATUS.md, not MEMORY.md. Strip it.

**Tone-match risks:** "Bucket E B3 fire" jargon is opaque without context; existing MEMORY entries use plain-language framings. Replace with the management admission itself as the anchor.

**Proposed rephrasing (Will's voice / existing density):**

> **WAL Bucket E Confirmed (May 17)** — Investor Day Q&A: management held 25–35bps NCO guide despite Q1 ex-fraud running at 39bps. Concrete admission they're under-reserving against current run rate. REG-25 scenario 55%→65%; bear-slow 23%→27%. → `AGENTS/REGINALD/STATUS.md` + `FORGE/WAL/`

**Layer:** root `MEMORY.md` CORE DISCOVERIES.

---

### 2. FSK Q1 validates BDC vehicle stress (May 11) — **KEEP, rephrase, SPLIT**

**Critical issue:** Draft entry packs TWO different discoveries together — (a) FSK Q1 as a vehicle-level BDC stress confirmation, and (b) PSEC PIK 8.6% (not 35%) as the first agent-data falsification. These have different durability profiles and belong in different sections. Splitting them also de-duplicates draft #8.

**(a) FSK Q1 — KEEP as CORE DISCOVERY.** This extends the PC Contagion Mechanics / Blue Owl chain with a new vehicle data point. Tracks the existing entry style.

**Proposed rephrasing (a):**

> **FSK Q1 Validates BDC Vehicle Stress (May 11)** — FSK Q1 print landed Strong Bear / near Max Bear: vehicle-level mark/income stress confirmed. Public-credit cascade still **unconfirmed** (HY OAS <300, VIX <20 = constraint on broad cascade adds, not all-clear). → `PROME/action-cards/FSK_MAY11_ACTION_CARD.md` + BROCK domain.

**(b) PSEC hallucination — fold into the verify-rule entry (see draft #8 below).** This is a system-architecture lesson, not a thesis discovery.

**Layer:** (a) root CORE DISCOVERIES; (b) root SYSTEM ARCHITECTURE (consolidated with #8).

---

### 3. WALTER signal/news routing codification (May 17) — **KEEP, rephrase HARD**

**Why keep:** Operating-model split between WALTER (routing) and Prome (tasking) is now a load-bearing convention that affects which agent gets new signal types. That's exactly the "Persistent Agents — Do Not Spawn" tier of system-architecture rule.

**Why rephrase hard:** Draft is 3 sentences enumerating both roles. SYSTEM ARCHITECTURE existing entries are tighter (1-2 sentences). The triple-file-path list ("codified across X, Y, Z") is process detail — drop it.

**Proposed rephrasing:**

> **WALTER Owns Routing, Prome Owns Tasking (May 17)** — Operating-model split codified: WALTER ingests, classifies, dedupes, and routes incoming signals to domain agents. Prome assigns decision work and writes Will-facing memos. Prome should not become a parallel signal router for recurring news/filing flows. → `AGENTS/PROME/CLAUDE.md` §"Operating Model — Chief of Staff."

**Layer:** root `MEMORY.md` SYSTEM ARCHITECTURE.

---

### 4. OZK spinout to peer agent (Apr 24) — **REPHRASE (short pointer) + update Mar 25 entry**

**Overlap with existing Mar 25 "WAL + OZK Complementary Shorts":** Confirmed real. The Mar 25 entry already captures the thesis content (uncrowded edge / crowded edge, fast-transmission / reservoir). Draft #4 mostly restates that thesis and adds the org change (sub-scope → peer agent).

**Correct treatment:** Don't add a second long entry covering the same thesis. Instead:
- **Update the Mar 25 entry** with a one-clause tail noting peer-agent promotion.
- Optionally add a thin SYSTEM ARCHITECTURE entry on "spin-out-when-bandwidth-exceeded" as a transferable pattern.

**Proposed Mar 25 update (append clause only — don't rewrite the entry):**

> ... OZK Q1 Apr 16, WAL Q1 Apr 21. OZK promoted to peer agent `AGENTS/OZK/` (Apr 24) reflecting distinct failure-mode; WAL is next candidate. → `AGENTS/REGINALD/STATUS.md`, `AGENTS/OZK/`

**Optional new SYSTEM ARCH entry (if Will wants the meta-pattern captured):**

> **Sub-Agent Spinout Pattern (Apr 24)** — Sub-scopes that outgrow a parent's coordination bandwidth get promoted to peer agents. OZK was the first (`REGINALD/OZK/` → `AGENTS/OZK/`). WAL is the next candidate. → `AGENTS/OZK/`.

**Layer:** update existing Mar 25 CORE DISCOVERY entry + optional SYSTEM ARCH addition.

---

### 5. Claude Code Prome scaffold (May 15–17) — **KEEP, rephrase + update "Persistent Agents"**

**Why keep:** "One Prome, two surfaces" with shared file-state-as-source-of-truth is a genuinely new architecture pattern — first time a Telegram/OpenClaw agent has had a coordinated Claude Code surface with the same identity. The propose-then-approve discipline boundary outside `PROME/` is the load-bearing operating rule.

**Why rephrase:** Draft is 5 sentences enumerating phases, audits, file pointers. Existing SYSTEM ARCH entries (e.g. News Sweep Tool) are 2-3 sentences with the operating rule as the headline.

**Overlap with "Persistent Agents — Do Not Spawn" (Apr 6):** Confirmed — Claude Code Prome is now a persistent agent. That entry needs OZK + RED + Claude Code Prome appended (the draft's own note flags this).

**Proposed new SYSTEM ARCH entry:**

> **One Prome, Two Surfaces (May 15–17)** — Prome now runs as a single identity across two surfaces: Telegram/OpenClaw (Will-facing conversation, synthesis, approvals, external sends) and Claude Code (repo-native docs/tools/audits/handoffs). Shared state files are single source of truth — no forked memory. Claude Code Prome operates scoped-autonomous in `PROME/` + `AGENTS/PROME/`; propose-then-approve elsewhere. → `PROME/CLAUDE.md`, `PROME/CLAUDE_CODE_PROME.md`.

**Proposed update to "Persistent Agents — Do Not Spawn" (Apr 6):**

> **Persistent Agents — Do Not Spawn (updated May 17)** — CARL, REGINALD, OZK, RED, SAM, BRENT, Claude Code Prome run as persistent agents on Claude Code/Telegram. Spawning sub-agents for these disrupts their workflows. Spawn restriction: LABOR, HENRY, LIQUID, BROCK, SHADE, HAWK, MARCO, ZHAO, OTTO, NEXUS only. → `AGENTS.md`

**Layer:** root SYSTEM ARCHITECTURE.

**Optional auto-memory cross-write:** The surface-rule ("Claude Code Prome operates scoped-autonomous in PROME/; propose-then-approve elsewhere") is a workflow rule that fits auto-memory's feedback-pattern shape. Could dual-write — but I'd defer to Will's decision on the open question raised in the draft's footer rather than do it preemptively.

---

### 6. Agent View installed → teams experiment opens (May 17) — **REJECT for root**

**Why reject:** This is installation-state, not lasting discovery. Existing MEMORY.md entries don't memorialize tooling install events ("News Sweep Tool Deployed" is the closest, but that entry is about the *operational thesis-tagged monitoring system*, not about the act of installing). Agent View is runtime infrastructure that will be assumed within a week.

**Forward-looking note ("teams layer is active frontier"):** That's session-state, not memory-state. Belongs in `PROME/HANDOFF.md` and `PROME/CLAUDE_CODE_HANDOFF.md` Active Thread — which the draft already says is where it lives.

**When this DOES become memory-worthy:** After the teams experiment (which this audit is part of) produces a verdict on whether adversarial-pair patterns add value. THAT finding could be a SYSTEM ARCH entry. Not yet.

**Layer:** nowhere in MEMORY.md. SCRATCH / HANDOFF only.

---

### 7. Hash-drift staleness pattern (May 17) — **REJECT for root, route to auto-memory**

**Why reject for root:** Draft self-flags this as "more feedback memory than core discovery." That assessment is correct. The lesson — "state files that pin commit hashes decay faster than state files that describe behavior" — is a workflow/feedback rule about file-update discipline, not a thesis-level discovery.

**Where it belongs:** Claude Code auto-memory layer (`~/.claude/projects/-home-willi-Research-workspace/memory/`). The existing auto-memory index already includes "Verify State Before Propagating" and "Check Existing Design Docs" — same shape.

**Proposed auto-memory entry (terse, auto-memory style):**

> **Behavior-Language Over Hash-Pinning** — State files that name commit hashes decay 2-3 commits stale within 48h despite refresh discipline. Favor behavior-language ("clean, synced to origin") over hash references when describing repo state.

**Layer:** auto-memory ONLY. Do not write to root MEMORY.md.

**Note for team-lead:** This audit cannot directly write auto-memory entries (out of scope of our write permissions). Route this as a separate action item to whichever surface owns auto-memory writes.

---

### 8. Verify-against-filings rule (April, ongoing) — **REPHRASE, fold with draft #2(b)**

**Why fold:** Draft #2(b) and draft #8 describe the same discovery — PSEC PIK 8.6% (not 35%) was the first agent-data hallucination caught only because Will pulled the 10-K. This rule already lives as Critical Rule #3 in root CLAUDE.md. Adding it to MEMORY.md SYSTEM ARCHITECTURE serves as the historical anchor explaining why the rule exists.

**Proposed consolidated SYSTEM ARCH entry:**

> **Verify Agent-Reported Data Against Filings (Apr origin, ongoing)** — Agent-reported numbers can hallucinate. PSEC PIK was reported as 35% but the 10-K showed 8.6% — caught only because Will pulled the filing. Standing rule: cross-check any agent-cited number against primary source before trading. → root `CLAUDE.md` Critical Rule #3.

**Why this entry earns MEMORY.md space despite already living in CLAUDE.md:** CLAUDE.md is operational ("here's the rule"). MEMORY.md is historical ("here's the discovery that produced the rule, with the specific PSEC anchor"). The two layers serve different recall purposes. The Apr 5 "PC Contagion Mechanics" entry follows the same pattern — operational mechanics live in BROCK's research file, MEMORY.md captures the historical synthesis.

**Layer:** root SYSTEM ARCHITECTURE.

---

## Open question (passthrough to team-lead)

The draft's footer flags an open Will question: should the "Claude Code Prome scaffold" item dual-write to BOTH root MEMORY.md AND auto-memory? My recommendation:

- **System-architecture half** (one Prome / two surfaces / shared state) → root MEMORY.md SYSTEM ARCHITECTURE.
- **Surface-rule half** (Claude Code Prome operates scoped-autonomous in PROME/, propose-then-approve elsewhere) → auto-memory.

These are different facts at different abstraction levels. Single-layer placement of either would lose context for the other. But I'd defer to Will's call on whether to formalize the dual-write pattern broadly — this audit shouldn't decide that for him.

---

## Process notes for joint reconciliation (T3)

Where I expect critic pushback:
1. **#1 (WAL Bucket E):** Critic may argue this is mid-session state and the V2.2-gating caveat proves it. My counter: the management admission itself is the durable anchor; gating is in-flight detail to strip.
2. **#3 (WALTER routing):** Critic may argue this is operational tasking, not discovery. My counter: the "Persistent Agents — Do Not Spawn" entry sets precedent for codified-operating-rule entries.
3. **#5 (Claude Code Prome):** Critic may argue this is internal infrastructure of no interest to thesis work. My counter: the two-surfaces architecture is what makes coordinated repo work possible — load-bearing for the entire fleet's git protocol.
4. **#8 (Verify rule):** Critic may argue this is duplicative of CLAUDE.md and shouldn't be doubled. My counter: anchor-the-rule-to-its-origin discovery is a recurring MEMORY.md pattern (Blue Owl, IHAM, etc.).

Open to changing my mind on any of these if critic surfaces evidence I missed.
