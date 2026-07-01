# Joint Decision — MEMORY Draft Audit

**Authors:** curator + critic (memory-audit-001)
**Date:** 2026-05-18
**Source:** `PROME/MEMORY_DRAFT_2026-05-17.md` (8 candidates)
**Inputs:** `curator_recommendations.md`, `critic_concerns.md`, + per-candidate DM reconciliation.

---

## Headline

**3 new MEMORY.md entries + 2 in-place updates to existing entries + 1 auto-memory route + 5 rejects.**

Below the draft's "3–5 lasting-discovery" target, deliberately. The Apr–May window produced two genuinely thesis-relevant findings (WAL, FSK) plus one durable methodology rule (PSEC verify); the remaining draft candidates were operational milestones, mid-experiment state, or content already canonical in `CLAUDE.md` / `PROME/CLAUDE.md` / auto-memory.

## Summary table

| # | Candidate | Verdict | Layer | Notes |
|---|-----------|---------|-------|-------|
| 1 | WAL Investor Day → Bucket E B3 | **KEEP** (rephrase) | root MEMORY / CORE | Mgmt-credibility gap is the durable anchor; scenario-weight deltas stripped |
| 2(a) | FSK Q1 BDC vehicle stress | **KEEP** (rephrase) | root MEMORY / CORE | Complements Blue Owl Apr 2; PSEC origin retained inline |
| 2(b) + 8 | Verify-against-filings rule (PSEC origin) | **KEEP** (fold, new entry) | root MEMORY / SYSTEM ARCH | Anchors CLAUDE.md Rule #3 to its origin event |
| 3 | WALTER signal/news routing codification | **REJECT** | — | Doctrine in flux (WALTER COP evolution); pinning a moving target produces stale entries |
| 4 | OZK spinout to peer agent | **REJECT** standalone — update Mar 25 entry in place | existing CORE entry update | Thesis already captured Mar 25; org change is a one-clause append |
| 5 | Claude Code Prome scaffold | **REJECT** | — | Mid-substrate-transition (Messaging Overhaul, Telegram Prome degraded); canonical home is `PROME/CLAUDE.md` |
| 6 | Agent View + teams experiment | **REJECT** | SCRATCH/HANDOFF only | Premature — we are inside the experiment; revisit when result is in |
| 7 | Hash-drift staleness pattern | **REJECT** for root | auto-memory route | Self-flagged as feedback memory; correct call |

Plus: **Apr 6 "Persistent Agents — Do Not Spawn" requires an independent in-place staleness fix** (omits OZK, RED, CC Prome). Flagged in appendix below.

---

## Final phrasings — three new MEMORY.md entries

### 1. WAL Investor Day → Bucket E (May 17) — CORE DISCOVERIES

> **WAL Mgmt Credibility Gap (May 17)** — Investor Day Q&A held 25–35bps NCO guide despite Q1 ex-fraud running at 39bps. Same fast-transmission pattern as Mar 25 thesis: losses bypass DQ pipeline and surface directly in P&L. → `AGENTS/REGINALD/STATUS.md` + WAL trade folder.

**Drop from draft:** scenario-weight deltas (REG-25 55%→65%, bear-slow 23%→27%) — those are REGINALD scenario-tape state that will move with every WAL data point. They live in STATUS.md. The "V2.2 gated on 10-Q / Schedule O / FFIEC PDD" caveat is in-flight pending-work language and also drops.

### 2(a). FSK Q1 (May 11) — CORE DISCOVERIES

> **FSK Q1 Confirms BDC Vehicle Stress (May 11)** — FSK Q1 landed Strong Bear / near Max Bear. Second BDC vehicle (after Blue Owl OTIC/OCIC, Apr 2) to publicly confirm mark/income stress at vehicle level. PIK 8.6% (lower than initially feared 35%, which was the trigger event for the agent-data verification rule). Broad public-credit cascade still gated by HY OAS / VIX. → `PROME/action-cards/FSK_MAY11_ACTION_CARD.md` + BROCK domain.

### 2(b) folded with 8. Verify rule (Apr origin) — SYSTEM ARCHITECTURE

> **Verify Agent-Reported Data Against Filings (Apr origin, ongoing)** — Agent-reported numbers can hallucinate. PSEC PIK was reported as 35% but the 10-K showed 8.6% — caught only because Will pulled the filing. Standing rule: cross-check any agent-cited number against primary source before trading. → root `CLAUDE.md` Critical Rule #3.

---

## Two in-place updates to existing MEMORY.md entries

### Mar 25 "WAL + OZK: Complementary Shorts" — append one clause

**Current trailing sentence:** `... OZK Q1 Apr 16, WAL Q1 Apr 21. → AGENTS/REGINALD/STATUS.md`

**Proposed updated trailing sentence:**

> ... OZK Q1 Apr 16, WAL Q1 Apr 21. OZK promoted to peer agent `AGENTS/OZK/` (Apr 24) reflecting distinct failure-mode; WAL is the next candidate. → `AGENTS/REGINALD/STATUS.md`, `AGENTS/OZK/`

Rationale: the OZK org change is real and worth recording, but the thesis content (uncrowded/crowded edge, fast/reservoir transmission) is already captured in the Mar 25 entry. Appending a clause is parsimonious; a standalone entry would duplicate.

### Apr 6 "Persistent Agents — Do Not Spawn" — staleness fix

**Current text:** `CARL, REGINALD, RED, SAM, BRENT run as persistent agents on Claude Code/Telegram. Spawning sub-agents for these five disrupts their workflows. Spawn restriction: LABOR, HENRY, LIQUID, BROCK, SHADE, HAWK, MARCO, ZHAO, OTTO, NEXUS only. → AGENTS.md`

**Proposed updated text:**

> **Persistent Agents — Do Not Spawn (updated May 17)** — CARL, REGINALD, OZK, RED, SAM, BRENT, Claude Code Prome run as persistent agents on Claude Code/Telegram. Spawning sub-agents for these disrupts their workflows. Spawn restriction: LABOR, HENRY, LIQUID, BROCK, SHADE, HAWK, MARCO, ZHAO, OTTO, NEXUS only. → `AGENTS.md`

This fix is **independent of the 8 candidates** — the existing entry is factually stale regardless of what gets added. See appendix.

---

## Auto-memory route (not root MEMORY.md)

**Candidate #7 (hash-drift staleness)** → write to auto-memory layer, not root. Suggested entry text in auto-memory style:

> **Behavior-Language Over Hash-Pinning** — State files that name commit hashes decay 2-3 commits stale within 48h despite refresh discipline. Favor behavior-language ("clean, synced to origin") over hash references when describing repo state.

**Note for team-lead:** This audit's write-scope is `joint_decision.md` only. Auto-memory edits are out of scope here — route this to whichever surface owns auto-memory writes as a separate action.

---

## Rejection rationale (compressed)

- **#3 WALTER routing codification:** Operating doctrine. Doctrine entries in MEMORY.md create stale-entry risk when the doctrine evolves (the Apr 6 entry is itself the failure-mode example). WALTER scope is currently in flux per auto-memory ("WALTER COP Architecture Direction — evolving from inbox router to COP integrator"). Pinning a snapshot of a moving target is bad timing. Doctrine already lives in three canonical operating docs.
- **#4 standalone:** Thesis content already in Mar 25 entry; org change appended there. No new entry.
- **#5 Claude Code Prome scaffold:** Substrate is in transition — auto-memory flags both `OpenClaw/Prome Degraded` (Telegram Prome unreliable) and `Messaging System Overhaul` (file-based coordination being replaced). Pinning "One Prome, Two Surfaces" while one surface may be going dark and the messaging substrate is being rewritten is premature. Canonical home is `PROME/CLAUDE.md` and `PROME/CLAUDE_CODE_PROME.md`.
- **#6 Agent View / teams experiment:** This audit IS run #1 of that experiment. Pinning an opening before the result is in is premature. Revisit if teams primitive produces a non-obvious coordination pattern after 2-4 weeks live.
- **#8 standalone:** Content folded into #2(b) SYS ARCH entry above. The fold preserves the discovery without a redundant third statement of the same rule.

---

## Appendix — Integrity issue independent of the 8 candidates

The existing root `MEMORY.md` Apr 6 SYSTEM ARCHITECTURE entry "Persistent Agents — Do Not Spawn" is **factually stale**:

- Omits OZK (promoted to peer agent Apr 24)
- Omits RED (persistent on Claude Code)
- Omits Claude Code Prome (persistent surface, May 15–17)

The entry is currently load-bearing — domain agents read it to determine which agents can be spawned. If it's wrong, future sessions may incorrectly spawn against persistent agents and disrupt their workflows.

**Recommended fix:** apply the in-place update proposed above ("Persistent Agents — Do Not Spawn (updated May 17)" text). This should happen regardless of which of the 8 candidates are accepted; it is a correctness fix to an existing entry, not a new addition.

This issue was independently flagged by both auditors before reconciliation — it is not a contentious recommendation.

---

## Process notes for team-lead

- Audit deliberately landed below the draft's "3–5 lasting-discovery" target (3 new entries vs. target of 3–5). Both auditors agreed signal-density beats hitting the volume target.
- Reconciliation produced two genuine flips: curator conceded on #3 (WALTER doctrine) and #5 (CC Prome scaffold); critic conceded on #8 (verify rule belongs as anchor entry). Net of flips: roughly even movement in both directions — neither auditor steamrolled.
- The biggest substantive disagreement was over whether MEMORY.md should pin operating doctrine that lives in `CLAUDE.md`. Final position: only when the doctrine has a discovery anchor (PSEC for verify-rule) and the doctrine itself is stable (which WALTER routing is not).

---

## Sign-offs

- **curator:** signed off. Final positions above match the joint walk-through.
- **critic:** signed off (2026-05-18). Reviewed full file against the DM walk-through; all per-candidate verdicts, final phrasings, and the appendix integrity flag match the reconciliation outcome. The two genuine flips (curator on #3/#5; critic on #2(b)/#8 fold) are recorded accurately. Independent note for team-lead: my standalone T2 file would have landed at 2 keeps; curator's T1 file at 4 keeps; reconciled joint output at 3 keeps + 2 in-place updates + 1 auto-memory route. The #3 and #5 rejections both emerged from substrate-in-flux evidence (auto-memory's WALTER COP and Prome-Degraded notes) that neither standalone file weighted heavily — surfaced specifically because of the adversarial walk-through. That is the part of the audit I would not expect solo curation to have produced.
