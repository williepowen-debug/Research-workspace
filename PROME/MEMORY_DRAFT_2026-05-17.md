# MEMORY.md — Candidate Entries (April–May 2026)

**Drafted:** 2026-05-17 evening ET by Claude Code Prome
**Purpose:** Candidate CORE DISCOVERY entries for Telegram/OpenClaw Prome to review, edit, and integrate into root `MEMORY.md`. The MEMORY.md weekly-review cadence has lapsed since 2026-04-05; ~6 weeks of substantive agent work is unreflected at the index level.

**Owner of integration:** Telegram/OpenClaw Prome. Claude Code Prome drafts; Telegram Prome curates. Do not auto-merge — the curation judgment about what rises to "lasting discovery" is a Will-facing call, and entry phrasing should match Will's voice for the file.

**Process suggestion:**
1. Telegram Prome reads this draft against the existing MEMORY.md format and tone.
2. Picks the 3–5 that meet the lasting-discovery bar (the rest get dropped or pushed to daily `memory/` instead).
3. Rephrases to match Will's voice and existing entry density.
4. Updates the "Last Updated" stamp at top of MEMORY.md.
5. Considers restoring the weekly-review habit (BOOT.md Memory Lifecycle table).

---

## Candidate Entries

### 1. WAL Investor Day → Bucket E B3 fire (REGINALD, May 17)

WAL Investor Day Q&A confirmed Bucket E B3: management held 25–35bps NCO guide despite Q1 ex-fraud running at 39bps. REG-25 promoted **55% → 65%+**; bear-slow path **23% → 27%**. No V2.2 (Strong Bear) promotion yet — gated on WAL 10-Q integration (filed 5/11, Schedule O / Table 16 cross-credit inventory test pending) and MI3 / FFIEC PDD mid-May update window status check. → `AGENTS/REGINALD/STATUS.md` + WAL trade folder.

### 2. FSK Q1 validates BDC vehicle-level stress (BROCK / Prome, May 11)

FSK Q1 print landed Strong Bear / near Max Bear and validates BDC/private-credit mark/income stress at the vehicle level. PIK ran 8.6% (NOT the 35% initially feared — first hallucinated agent-data falsification of the operation; verify-against-filings rule applied). Fresh downside discussion allowed; public-credit cascade still **unconfirmed** (HY OAS <300, VIX <20 = constraint against broad cascade adds, not all-clear). → `PROME/action-cards/FSK_MAY11_ACTION_CARD.md` + BROCK domain.

### 3. WALTER signal/news routing codification (May 17)

Root-level operating-model split made explicit and codified across `AGENTS/PROME/CLAUDE.md`, `PROME/SYSTEM.md`, and `AGENTS_DIRECTORY.md`: **WALTER owns signal/news routing** (ingest, classify, filter, dedupe, archive to BOARD/FORGE/signals, route to domain agents). **Prome owns operational tasking** (assigns decision work, writes Will-facing decision memos). Prome should avoid becoming a parallel signal router for recurring news/filing flows. → `AGENTS/PROME/CLAUDE.md` §"Operating Model — Chief of Staff."

### 4. OZK spinout to peer agent (Apr 24)

OZK promoted from `REGINALD/OZK/` sub-scope to top-level `AGENTS/OZK/` as peer agent. Driven by distinct failure mode vs WAL: OZK is the reservoir (losses accumulate behind interest reserves, SI 13.81% = crowded edge) vs WAL the fast-transmission (losses bypass DQ pipeline → straight to P&L, SI 3.54% = uncrowded edge). Different put-expiry logic, different catalyst calendars. **WAL is the next candidate** for similar promotion when ready. Marks a systems-organization direction: spin out sub-scopes that have outgrown their parent's coordination bandwidth. → `AGENTS/OZK/`.

### 5. Claude Code Prome scaffold + Phase 3 dry run passed (May 15–17)

Persistent Claude Code Prome bootstrapped as repo-native implementation surface — same identity as Telegram/OpenClaw Prome, different work surface. **One Prome, two surfaces.** Telegram/OpenClaw owns Will-facing conversation, synthesis, approvals, external sends; Claude Code owns docs, tools, audits, action-card scaffolds, handoffs. Shared files are single source of truth — no forked memory. Phase 3 readiness audit passed 2026-05-17. Operating discipline: scoped autonomous edits in `AGENTS/PROME/` and `PROME/`, propose-then-approve elsewhere, show-diff-then-approve for every commit. → `PROME/CLAUDE.md`, `PROME/CLAUDE_CODE_PROME.md`, `PROME/CLAUDE_CODE_PROME_PLAN.md`, `PROME/CLAUDE_CODE_HANDOFF.md`.

### 6. Agent View installed → teams experiment opens (May 17)

Agent View (persistent dashboard / session manager) installed and operational on this machine + laptop. During install, discovered `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` maps more directly than vanilla Agent View onto the architecture we've been building — chief-of-staff lead, named teammates, mailbox messaging, shared task lists. Agent View is now runtime infrastructure; the **teams layer** is the active frontier work for whether it's a useful coordination surface for the fleet. → `PROME/HANDOFF.md` Active Thread; `PROME/CLAUDE_CODE_HANDOFF.md` Current Session.

---

## Lower-confidence candidates (Telegram Prome may drop these)

These reach lasting-discovery threshold less clearly. Including for completeness.

### 7. Hash-drift staleness pattern (cleanup pass, May 17)

State files (`STATUS.md`, `TODAY.md`, `HANDOFF.md`, `SCRATCH.md`, `CLAUDE_CODE_HANDOFF.md`) drifted 2–3 commits stale from current HEAD over <48h despite intentional refresh discipline. Pattern: handoff says "local master at X" then 2 commits land and the references become misleading without any single file feeling "wrong." Phase 3 dry run caught it; cleanup pass fixed it. **Lesson:** state files that name a commit hash decay faster than state files that describe behavior — favor behavior-language ("clean, synced to origin") over hash-pinning when possible. This is more "feedback memory" than "core discovery" — may belong in auto-memory not root MEMORY.md.

### 8. Verify-against-filings rule (April, ongoing)

Agent-reported facts can hallucinate. PSEC PIK reported as 35% was actually 8.6% — caught only because Will pulled the 10-K. Standing rule now lives at root `CLAUDE.md` Critical Rule #3 ("Agent data can be hallucinated. Verify against SEC filings before trading."). Already partially captured but may merit a MEMORY.md SYSTEM ARCHITECTURE entry given how often it's load-bearing.

---

## Notes for Telegram Prome

- Existing MEMORY.md CORE DISCOVERIES are dated by event/finding, not by entry date. I matched that style.
- Density of existing entries varies (some are 2 sentences + pointer, some are paragraph-length). I leaned toward the longer end; trim as needed.
- The Apr-5 "Persistent Agents — Do Not Spawn" entry is now contradicted by my draft #4 (OZK promotion) in spirit — OZK is now also a persistent Claude Code agent and shouldn't be spawned. Worth updating that entry to include OZK + RED rather than adding a new one.
- The Mar-25 "WAL + OZK: Complementary Shorts" entry is still accurate but the OZK promotion to peer agent (draft #4) is the operational follow-up. Could fold them or keep distinct.
- I have NOT touched `MEMORY.md` itself. This file is for review only.

---

## Open question for Will (passthrough to Telegram Prome)

The auto-memory at `~/.claude/projects/.../memory/MEMORY.md` (the Claude Code persistent memory layer) is separate from root `MEMORY.md` (the curated thesis-level discoveries). Both index "memory" but they serve different purposes: auto-memory captures user preferences and feedback patterns; root MEMORY.md captures thesis-level discoveries. The Claude Code Prome scaffold (draft #5) probably belongs in BOTH — system-architecture in root MEMORY.md, surface-rule in auto-memory. Worth a Will decision on whether to formalize that dual-write pattern or keep them strictly separated.
