# LIAISON Channel Playbook

*Generic process doc — captures the WALTER ↔ CARL pilot pattern (2026-05-05 → 06, 6 turns) as repeatable process for future LIAISON channels (BRENT, RED, HENRY, beyond). Distinct from instance-specific PREP docs (e.g., BRENT_LIAISON_PREP.md). Reusable.*

*Created 2026-05-06 (Phase 1 scaffolding) per Will direction msg 1339 + 1344. Maintenance: when a new LIAISON cycle ships and produces process refinements, update this playbook. Don't duplicate per-cycle retrospectives here — those live in MEMORY.md findings.*

---

## 1. Purpose

The LIAISON channel is **WALTER ↔ paired-agent architectural-alignment dialogue**. It is NOT signal routing (BOARD does that) and NOT inbox messaging (deprecating). It IS the meta-conversation about routing rules, edge cases, calibration, and shared structure.

**Distinct from:**
- `/BOARD/INDEX.md` — outbound signal feed (broadcast, one-way)
- `AGENTS/{AGENT}/board/BOARD_LOG.tsv` — recipient agent's disposition ledger
- `AGENTS/WALTER/outbox/REQ-*.md` — one-shot requests to other agents (queue files)

**LIAISON is bidirectional, sustained, and architectural in scope.**

## 2. When to spawn a LIAISON

Trigger criteria (any one):
- WALTER has 3+ accumulated questions or routing-rule ambiguities about a specific agent
- Recipient agent has flagged multiple signals as INFO_ONLY / REFERRED / unclear-fit
- A new cluster-spawn or sub-cluster-breakdown decision pending Will sign-off involves the agent's domain
- Cross-cluster narrative-arbitration question keeps surfacing (calls for NEXUS, but blocked)
- Recipient agent expresses interest in tighter routing-rule alignment

**Don't spawn for:**
- Single-signal disputes (use `**Q:**` in dispatch_note instead)
- Coordination tasks (use outbox REQ-*)
- Status updates on shared work (STATUS.md NETWORK AWARENESS)

## 3. Setup conventions

### File paths (canonical naming — required for boot-step glob discovery)

```
AGENTS/{TARGET_AGENT}/handoff_WALTER/LIAISON.md     # Canonical dialog file
AGENTS/{TARGET_AGENT}/handoff_WALTER/README.md      # Channel conventions (created by target agent)
```

WALTER does NOT mirror in own tree (Critical Rule #2 — file lives in target's tree; option (c) commit handling = target commits at next boot).

### STATUS.md manifest entry

When opening a new LIAISON, add a row to STATUS.md "Active LIAISON channels + countdowns" subsection:

```markdown
| WALTER ↔ {AGENT} | YYYY-MM-DD (Turn N opened) | ACTIVE | {Next_Trigger} | {Notes} |
```

Status enum: `ACTIVE | PENDING | DORMANT | DEFERRED | ARCHIVED`. DORMANT auto-flag rule: 30 days without a turn at next closeout.

### MEMORY.md References path

Reference (already added 2026-05-06): `AGENTS/{TARGET_AGENT}/handoff_WALTER/LIAISON.md`.

## 4. Turn schema

```markdown
## Turn N — {AGENT_NAME} — YYYY-MM-DD HH:MM UTC

[content]

---
```

- **Turn number is global (not per-agent).** Increment monotonically. CARL Turn 1 → WALTER Turn 2 → CARL Turn 3, etc.
- **Timestamps in UTC.** Use HH:MM precision. Date is when content was written (not when relayed).
- **Append-only.** Never edit prior turns. Corrections happen in subsequent turns.
- **Self-contained turns.** Each turn should be readable on its own; don't assume reader has scrolled up. Reference prior turns by Q-number or Turn-N pointer.
- **`---` separator between turns** for visual scanning.

## 5. Tag conventions

Use these inline tags so structure is parseable:

- **`**Q:**`** — open question requiring point-by-point answer
- **`**DECISION:**`** — locked-in decision; reference the proposing turn
- **`**PROPOSAL:**`** — concrete proposal awaiting accept/decline
- **`**CALIBRATION:**`** — bidirectional calibration data (e.g., post-hoc confidence vs dispatched verdict)
- **`**ACCEPT:**`** / **`**DECLINE:**`** / **`**REFINE:**`** — responses to proposals; refine + counter is the most common

Keep tags as bold-prefix-text not section headers (sections create false hierarchy in append-only docs).

## 6. Opening-turn checklist (Turn 1 from initiator OR responder)

**Whichever agent opens (typically responder if WALTER prompts):**

- [ ] **Domain in one paragraph.** What you own; what you don't own. Helps other side route correctly without inferring.
- [ ] **"I receive from" rules table.** Who sends you what + what triggers each. Concrete.
- [ ] **Disposition retrospective on recent shared work.** **HIGHEST-VALUE OPENER.** For each recent signal: INTEGRATED / INFO_ONLY / REFERRED + which were right calls. Forces the calibration data WALTER doesn't normally see. Per CARL pilot: 4 INTEGRATED / 6 INFO_ONLY / 2 REFERRED breakdown drove the entire dialog.
- [ ] **3-5 open questions for the other side.** Point-by-point. Don't bury in prose. Tag with `**Q:**`.
- [ ] **Invitation for their questions.** Final Q (e.g., "Q5 — your turn — what questions do you have for me?")

**WALTER's first response (Turn 2):**

- [ ] Acknowledge the opener's calibration data (especially if it surfaces something WALTER got wrong)
- [ ] Answer Q1-QN point-by-point with explicit tag (DECISION / PROPOSAL / ACCEPT / REFINE)
- [ ] Surface 3-4 own questions (Q11-Q14 or similar — continue numbering)
- [ ] Note any spec-change implications (FORMAT_SPEC field additions, ROUTING_TABLE entries) — surface as PROPOSAL, not unilateral DECISION

## 7. Mid-dialog patterns

### Common refinements

- **Concrete-thresholds-replace-prose pattern.** "Near $110" → "≥$110 sustained 2 sessions." If a routing rule has a threshold-of-judgment, push for the specific number across 2-3 turns.
- **Bridge concepts emerge from cross-axis differences.** WALTER thinks observation-axis; agent thinks mechanism-causal-axis. The bridge concept (e.g., consumer_transmission enum) translates between them. Look for this opportunity by Turn 3.
- **Pre-cosign aggressively.** When proposing a spec change, the other side can pre-cosign in their accept-turn. Cuts Will-review burden at surface time.

### Anti-patterns

- ❌ Burying questions in prose. Tag with `**Q:**`.
- ❌ Unilateral spec changes mid-dialog. Use `**PROPOSAL:**`.
- ❌ Editing prior turns to "clarify." Add a new turn.
- ❌ Letting calibration data live only in dialogue. Ship it structurally (e.g., CARL added Post_Hoc_Conf column to BOARD_LOG.tsv mid-dialog — Turn 3 ship).

## 8. Closing patterns

### Wrap signal (typically Turn N where N=5-8)

- Both sides have decisions or accepted proposals on every Q raised
- Open dependencies are external (Will sign-off, NEXUS spawn, RED revival, etc.) not internal-to-dialog
- Either side flags "architectural items converged" + proposes wrap

### Joint-proposal artifact (output of converged dialog)

When dialog produces multiple spec / policy / infrastructure proposals, bundle into a joint-proposal doc for Will-surface. Pattern from CARL pilot:

```
AGENTS/{AGENT}/design/JOINT_PROPOSAL_{date}_{agent}_sections.md   # AGENT drafts own sections
AGENTS/WALTER/design/JOINT_PROPOSAL_{date}_walter_sections.md     # WALTER drafts own sections
design/JOINT_PROPOSAL_{date}.md                                   # Repo-root stitched final (Will-mediated)
```

Each agent commits own sections to own tree (git-isolation preserved). Will commits the stitched final at repo root.

### Calibration cycle trigger

After wrap, set the next-trigger date on the STATUS manifest:

- **14-day calendar primary** (per Will mod 2026-05-06 — calendar dates are observable, counts require maintenance)
- **N=20 BOARD dispositions early-fire option** (whichever first)
- At trigger: agent surfaces post-hoc calibration deltas; WALTER tunes verify-research thresholds; new turn appended to LIAISON

## 9. Lessons from CARL pilot (2026-05-05 → 06, 6 turns)

1. **Disposition retrospective in CARL Turn 1 was the most valuable opener.** Drove the entire dialog. Make it a required template field for future Turn 1s.

2. **Bidirectional calibration happened organically.** CARL volunteered -008 AHLA self-critique (0.90 → 0.80-0.85) without prompting. The Q7 question structurally invited it; the loop closes faster than expected.

3. **CARL was further along on BOARD-pull than WALTER's MEMORY tracked.** Future Turn 1 prompt should ask: "What's your current BOARD-consumption mechanism (path / schema / boot-frequency)?" upfront. Avoids WALTER mis-assumption.

4. **Concrete thresholds beat prose.** Q3 sharpening across Turns 1→3→4: "near $110" → "≥$110 sustained 2 sessions." Three turns to lock concrete operationalizable rule.

5. **Bridge concept = consumer_transmission enum.** WALTER routes observation-side; CARL holds mechanism-causal vectors. The enum bridges. Anticipate energy_transmission analog for BRENT.

6. **Pre-cosign accelerates Will-surface.** CARL Turn 5 explicit "Pre-cosign FORMAT_SPEC v0.8 on my side: confirmed" reduced what Will needed to evaluate from "two agents agree?" to "approve or not?".

7. **6 turns was right size.** Convergence by Turn 5; Turn 6 was wrap. Plan for 5-7; flag concern if dialog reaches Turn 8+ without convergence.

8. **Joint-proposal bundle artifact at end.** Single coherent surface to Will beats 6 fragmented Telegram items.

9. **One-side-only specific paths cause friction.** Naming convention `AGENTS/{X}/handoff_WALTER/LIAISON.md` (in target's tree) means WALTER doesn't write the canonical file (option (c) preserves git-isolation). Will mediates relay between sessions.

## 10. Cross-platform considerations

For OC-platform agents (BRENT, HAWK, HENRY, NEXUS, BROCK, LIQUID, LABOR, etc.) where Prome routing is unreliable:

- **Option α — Spawn agent in CC for the dialog.** Treat as CC-pair like CARL. Both write to own trees. Lowest friction; works exactly like CARL pattern.
- **Option β — Will-mediated Telegram copy-paste of turns between sessions.** Slow but works. Use when option α not available. WALTER drafts Turn N → Will copies into target's LIAISON.md → Will prompts target agent (CC or OC) to read+respond → Will copies response back.
- **Option γ — Use target's existing OC handoff mechanism with Prome routing.** Unreliable given degraded Prome state. Avoid unless Prome revives.

**Recommendation:** Option α whenever feasible; option β as fallback.

## 11. Frequency / cadence (post-wrap)

| Event | Cadence | Mechanism |
|-------|---------|-----------|
| Architectural-alignment thread | 1× per LIAISON channel (typically 5-7 turns concentrated, then wrap) | Dialog as needed |
| Calibration cycle | Every 14 days (calendar primary) OR N=20 BOARD dispositions (early-fire) | New turn on trigger; both sides post calibration deltas |
| New routing-rule question mid-cycle | Within-cycle ad-hoc turn | Tag `**Q:**`; append to LIAISON |
| Cluster-spawn / spec-change proposals | Joint-proposal bundle at convergence | New doc per event in `design/` |

## 12. What NOT to put in LIAISON.md

- Routine operational status (STATUS.md NETWORK AWARENESS)
- One-shot requests to other agents (outbox REQ-*)
- Signal dispositions (BOARD_LOG.tsv recipient-side)
- Will-direct directives or Will-only context (Telegram surfacing, MEMORY)
- Per-signal verify-research verdicts (signal dispatch_note)
- Daily session logs (STATUS.md SESSION LOG)

LIAISON is for sustained architectural-alignment dialogue, not workflow noise.

---

*Created 2026-05-06 from CARL pilot 2026-05-05 → 06. Update when new lessons land. Source dialog: `AGENTS/CARL/handoff_WALTER/LIAISON.md`.*
