# Critic Concerns — Adversarial Pass on MEMORY_DRAFT_2026-05-17

**Author:** critic (memory-audit-001)
**Date:** 2026-05-18
**Method:** Independent skeptical pass, written before reading curator_recommendations.md.

## Framing & default

The existing root `MEMORY.md` bar is high: 16 CORE DISCOVERIES + 2 THESIS FRAMEWORK + 4 SYSTEM ARCHITECTURE entries spanning Mar–Apr 2026, all dated by *event/finding*, all market-thesis-relevant or load-bearing operational rules. Phrasing is terse, event-dated, ends with `→ <file pointer>`.

The 8 candidates in the draft skew **heavily operational/process** (5 of 8 are about agent infrastructure, not the macro/credit/labor thesis). The Apr–May window did contain real thesis-relevant work (WAL Investor Day, FSK Q1), but the drafter has padded that with infrastructure milestones that won't survive a July re-read. **Default verdict: reject; promote only #1 and a stripped-down #2 to CORE DISCOVERIES.**

Auto-memory cross-reference: I checked the auto-memory index. Several candidates already have auto-memory entries — see per-candidate notes.

---

## Per-candidate verdicts

### Candidate 1 — WAL Investor Day → Bucket E B3 fire (May 17)

**Verdict: KEEP, with rephrase. CORE DISCOVERIES bucket.**

The lasting finding is the **management-credibility gap**: WAL Investor Day Q&A held a 25–35bps NCO guide while Q1 ex-fraud already ran at 39bps. That's a falsifiable, dated, evidence-grounded statement about an issuer in an active short book. It belongs.

What does **not** belong: the scenario-weight deltas ("REG-25 promoted 55%→65%+; bear-slow 23%→27%"). Those are REGINALD scenario-tape state and will move with every WAL data point through Q2. They rot fast. They live in STATUS.md, not MEMORY.md.

Also drop: "No V2.2 promotion yet — gated on 10-Q integration / Schedule O / Table 16 / MI3 / FFIEC PDD mid-May." That is mid-session pending-work language, not a discovery.

Suggested terse rephrase (match existing tone):

> **WAL Mgmt Credibility Gap (May 17)** — Investor Day Q&A held 25–35bps NCO guide despite Q1 ex-fraud running at 39bps. Same fast-transmission pattern as Mar 25 thesis: losses bypass DQ pipeline and surface directly in P&L. → `AGENTS/REGINALD/STATUS.md` + WAL trade folder.

### Candidate 2 — FSK Q1 validates BDC vehicle-level stress (May 11)

**Verdict: KEEP, with rephrase + split. CORE DISCOVERIES bucket.**

Strong content. FSK Q1 landing at Strong Bear / near Max Bear validates the BDC/PC vehicle-level stress thesis, which is core to the BROCK book. It complements the existing Apr 2 "Blue Owl Dual Gating" entry as a second confirming vehicle.

**Split-and-trim issues:**

1. The "first hallucinated agent-data falsification (PSEC PIK 35% → 8.6%)" content does **not** belong in this CORE DISCOVERY. It's a methodology lesson and is already canonical at root `CLAUDE.md` Critical Rule #3. Duplicating into MEMORY.md adds noise. (See also my verdict on candidate #8.)
2. "Public-credit cascade still unconfirmed (HY OAS <300, VIX <20 = constraint against broad cascade adds)" — this is a useful **falsification gate** that belongs in HEARTBEAT-style threshold tracking, not in a static MEMORY discovery. Drop from this entry; let the threshold rails carry it.

Suggested terse rephrase:

> **FSK Q1 Confirms BDC Vehicle Stress (May 11)** — FSK Q1 landed Strong Bear / near Max Bear. Second BDC vehicle (after Blue Owl OTIC/OCIC, Apr 2) to publicly confirm mark/income stress at vehicle level. PIK 8.6% (lower than initially feared 35%, which was the trigger event for the agent-data verification rule). Broad public-credit cascade still gated by HY OAS / VIX. → `PROME/action-cards/FSK_MAY11_ACTION_CARD.md` + BROCK domain.

### Candidate 3 — WALTER signal/news routing codification (May 17)

**Verdict: REJECT.**

This is an **operating-model doctrinal change**, not a discovery. The content ("WALTER routes news, Prome routes decisions") is already canonical in three primary documents: root `CLAUDE.md` "Operating model" paragraph, `AGENTS/PROME/CLAUDE.md` §Operating Model — Chief of Staff, and `AGENTS_DIRECTORY.md`. Restating it in MEMORY.md is duplication that adds maintenance burden without informational value.

Auto-memory already has an entry **"WALTER COP Architecture Direction"** capturing the directional change. That is the correct home for routing-architecture decisions; root MEMORY.md is not.

Reject. (If the user disagrees and wants doctrine pinned in MEMORY.md, it should be a one-line SYSTEM ARCHITECTURE entry, not the paragraph drafted.)

### Candidate 4 — OZK spinout to peer agent (Apr 24)

**Verdict: REJECT as standalone. Update existing entries instead.**

Three problems:

1. The thesis content (WAL fast-transmission vs OZK reservoir, distinct SI, distinct put logic) is **already in MEMORY.md** as the Mar 25 "WAL + OZK: Complementary Shorts" entry. The draft re-states it.
2. The operational content ("OZK promoted to peer agent") directly **contradicts** the Apr 6 "Persistent Agents — Do Not Spawn" entry, which listed CARL/REGINALD/RED/SAM/BRENT but not OZK. The correct fix is to **update the Apr 6 entry in place** (add OZK; possibly add RED if newly persistent) — not to add a new entry that supersedes it implicitly.
3. Auto-memory already has **"OZK Spinout + Systems Organization Direction"** capturing the org-structure change. Redundant there too.

The drafter itself flags problem (2) in the "Notes for Telegram Prome" section. Listen to that signal and **edit the Apr 6 entry**; do not add a draft #4.

### Candidate 5 — Claude Code Prome scaffold + Phase 3 dry run passed (May 15–17)

**Verdict: REJECT.**

This is the textbook "mid-session state that will be stale in a week" case the brief warns against. By July, either:
- The Claude Code Prome surface is the obvious default (and "we bootstrapped it" reads as quaint history), or
- It's been replaced or quieted by the Messaging System Overhaul referenced in auto-memory (and the entry rots).

The genuine architectural insight here — **"One Prome, two surfaces; shared state files are single source of truth"** — *is* worth pinning, but its canonical home is `PROME/CLAUDE.md` and `PROME/CLAUDE_CODE_PROME.md` where it already lives. MEMORY.md is the wrong layer.

Also: "Phase 3 readiness audit passed 2026-05-17" is a milestone announcement. Milestones are not discoveries.

The draft itself ends with an "Open question for Will" asking whether to formalize a dual-write pattern. Open questions are by definition not lasting discoveries. Reject.

### Candidate 6 — Agent View installed → teams experiment opens (May 17)

**Verdict: REJECT.**

Two strikes:

1. Infrastructure-install events are not thesis discoveries. "We installed a dashboard" is operations log material.
2. The entry's own framing — "the **teams layer** is the active frontier work for whether it's a useful coordination surface" — admits the load-bearing piece is **unresolved**. We are *literally inside that experiment right now* (this audit is run #1). Pinning an active experiment's opening as a "core discovery" before the result is in is premature.

Revisit after the teams primitive has been live for 2–4 weeks. If it survives and produces a non-obvious pattern, *that* is the discovery worth pinning.

### Candidate 7 — Hash-drift staleness pattern (May 17)

**Verdict: REJECT for root MEMORY.md. Direct to auto-memory.**

The drafter pre-flagged this as auto-memory material ("This is more 'feedback memory' than 'core discovery' — may belong in auto-memory not root MEMORY.md"). I agree. The lesson — "favor behavior-language over hash-pinning in state files" — is a **writing rule** for state-file authors, which is exactly what auto-memory is for. It sits naturally alongside existing auto-memory entries like "Verify State Before Propagating," "Intra-Day Closeout Discipline," "Script Labels Match Thesis."

Root MEMORY.md is for thesis-grade discoveries and load-bearing operating rules. A state-file phrasing tip does not clear that bar.

### Candidate 8 — Verify-against-filings rule (April, ongoing)

**Verdict: REJECT (redundant).**

The drafter acknowledges the rule is "already partially captured" — it's **fully** captured, as Critical Rule #3 in root `CLAUDE.md`, which every agent boots through. The PSEC PIK 35→8.6% datapoint is also captured (correctly, as a counter-example) in candidate #2's body. Adding a third statement of the same rule in MEMORY.md is noise.

If Telegram Prome feels MEMORY.md should have a forward pointer to operational rules, a one-line "→ root `CLAUDE.md` Critical Rules" reference at the top of the SYSTEM ARCHITECTURE section beats a new redundant entry.

---

## Score sheet

| # | Candidate | Verdict | Layer |
|---|-----------|---------|-------|
| 1 | WAL Investor Day → Bucket E B3 fire | **KEEP (rephrase)** | root MEMORY.md / CORE DISCOVERIES |
| 2 | FSK Q1 validates BDC vehicle stress | **KEEP (rephrase + trim)** | root MEMORY.md / CORE DISCOVERIES |
| 3 | WALTER signal/news routing codification | **REJECT** | auto-memory entry already exists |
| 4 | OZK spinout to peer agent | **REJECT** | update Mar 25 + Apr 6 in place |
| 5 | Claude Code Prome scaffold + Phase 3 | **REJECT** | PROME/CLAUDE.md is canonical |
| 6 | Agent View / teams experiment opens | **REJECT** | premature; revisit when result is in |
| 7 | Hash-drift staleness pattern | **REJECT for MEMORY.md** | auto-memory candidate |
| 8 | Verify-against-filings rule | **REJECT (redundant)** | CLAUDE.md Critical Rule #3 already holds it |

**Bottom line: 2 keeps (both rephrased), 6 rejects.** The draft was 75% operational milestones masquerading as discoveries. The two thesis-relevant items (WAL, FSK) are the real value; everything else either duplicates canonical operating docs, duplicates existing MEMORY entries, restates auto-memory entries, or pins mid-experiment state.

The draft target said "Picks the 3–5 that meet the lasting-discovery bar." I'm landing under that range deliberately — better 2 strong entries than 4 padded ones in a file whose hallmark is high signal-density. If the curator argues for promoting #3 (WALTER doctrine) to a one-line SYSTEM ARCHITECTURE entry I can be moved on that; the rest I'd hold the line on.

## Open issue for joint_decision.md

The Apr 6 "Persistent Agents — Do Not Spawn" entry is now factually stale (omits OZK; possibly RED). Even if we reject draft #4, that existing entry needs an in-place update. Flag this to team-lead alongside the joint decision — it's an integrity issue independent of the 8 candidates.
