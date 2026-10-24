# NEXUS Brief Schema — LOCKED (R3 + amendments 7, 9, 10, 11, 12) · 🔒 AMENDMENT CAP IN FORCE (12 of 12)

**Owner-of-record (2026-08-07, PROME Roster-migration Phase 2, Will-accepted):** this file is the owner-of-record for WHICH desks owe a `NEXUS_BRIEF.md` and in WHAT FORM and ORDER — the synthesis-read requirement, the form invariants (FULL vs COMPACT, amendment 9) and the ordering invariant (brief fold = the session's LAST write-back, amendment 10). `PROME/ROSTER.md` points here and restates nothing. The LIVE coverage census is `AGENTS/NEXUS/BRIEFS_MAP.md`; no count is carried here. **Roster classes change nothing here:** the descriptive classes ROSTER introduced 8/5 add or remove no brief duty, read tier, form or ordering requirement.

**Status:** Locked 2026-06-07 as R3 (NEXUS's R3 consumer-review amendments 1, 2, 3, 5, 6 and 8 converged with SAM and are part of R3; **amendment 4's drop-rule was REJECTED by Will — the single SENDING table is Will's arbitration, decision row 17**) + amendment 7 (Expected-by column) + **9** (COMPACT variant — Will-approved 2026-07-31, decision row 19) + **10** (closeout ORDERING — Will-approved 2026-07-31, row 20) + **11** (`pin-follows-STATUS-HEAD` — NEXUS self-ruled 2026-08-07 under `AGENTS/DAEDALUS/BLUEPRINTS/DELEGATION_TIER.md`, row 21) + **12** (SECTION ORDER, CROSS-DOMAIN first — Will-approved 2026-09-01 via PROME WQ-105, row 22). **No amendment is pending and none may be proposed — see §4.6.** Section numbers §4.1–§4.6 are a stable citation API (the charter and `BRIEFS_MAP.md` cite §4.4 and §4.6).
**Repair 2026-10-24 (Will-authorized, Stage 2 of the bounded repair; NOT an amendment):** the ratified text of R3 amendments 1–3 (thesis-pivot line, tensions REQUIRED, WATCH → FORWARD CATALYSTS), amendment 9's form (decision row 19), the 2026-08-28 §4.4 pin-token ruling and the amendment-11 read-time carve-out (rollup #4) had lived only in the cold archive while this file was declared canonical; they are written in below, as ratified, with no addition. **NEXUS reads this repair as outside the §4.6 cap because no rule's content changed; if Will reads it otherwise, the repair stands as a defect for his word, not as amendment 13.** History, superseded text and the 2026-06 proposal sections moved verbatim (crc32) to `archive/2026-08-28_BRIEF_SCHEMA_decision-log_and_review-history.md` §A13. Decision rows are still cited by number and read in the cold file.
**WQ-519 (i), Will 2026-10-24 17:10 ET (record `PROME/proposals/2026-10-24_wq519-nexus-charter-split-RULED.md`): restoring previously ratified schema text is NOT a new amendment against the 12 of 12 cap, provided the restoration is faithful to the approved text; any genuinely new behavioural change still needs normal approval.** The 2026-10-24 repair above is held to that faithfulness condition (its sources: decision rows 11–13, 17, 19, 21 and the 8/28 §4.4 ruling, all in the cold archive).
**Canonical location:** `AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` (this file) + `NEXUS_BRIEF_TEMPLATE.md` (fleet-rollout template; this file wins on any disagreement). **Canonical brief path:** `AGENTS/<NAME>/NEXUS_BRIEF.md` (agent-owned). **Author / pilot:** SAM (R1–R3); reviewers PROME → NEXUS.
**Scope:** required for Tier-1 active desks (membership → `PROME/ROSTER.md`; the 2026-06-07 list is in the cold archive, not here); Tier-2 desks may skip and NEXUS reads their STATUS directly when active; **every brief that exists is read** (NEXUS charter BOOT 6). A desk that is brief-less by design is recorded as such in `BRIEFS_MAP.md`, never here.

---

## 1. DESIGN INTENT — connective-tissue-first

The brief serves **NEXUS's exclusive value: cross-agent connective-tissue detection** (PROME's Type B). Type A — a miss inside one domain — is the desk's job, or RED's, or lives in CALIBRATION's "uncertain about." Type B detection is a *comparison* problem across desks, and comparison needs N inputs on one schema. The brief is optimized for "see the whole board at once," not for compressing tokens.

**Section priority under cap pressure (load-bearing → scaffolding):** 1 **CROSS-DOMAIN** (the graph of overlapping edges — protect first) · 2 **CALIBRATION** (divergence + counter-signal lines) · 3 **VIEW** (context, compressible) · 4 **NEXT DECISION POINT** · 5 **FORWARD CATALYSTS** (most compressible). Trim upward from FORWARD CATALYSTS / VIEW; never compress CROSS-DOMAIN or CALIBRATION's divergence line.

---

## 2. SCHEMA — FULL variant (amendment 12 order: CROSS-DOMAIN is the first body section)

```markdown
# <AGENT> — NEXUS Brief

**Status:** [🟢🟡🟠🔴] vX.Y.Z — <ONE primary claim, ≤120 chars>        ← emoji per root CLAUDE.md key only (amendment 5)
**Domain:** <one-line scope — what this desk owns + the transmission edges it sits on>
**Thesis version:** vX.Y.Z (optional — desks that version; decision row 5)
**Recent thesis pivot:** <old> → <new> (<date>) — <one-clause reason>        ← REQUIRED single line (amendment 1); if no version pivot, the most recent material view shift
**As of:** YYYY-MM-DD HH:MM ET | STATUS commit: `<hash>`        ← canonical pin token, §4.4; the hash = STATUS HEAD at commit (amendment 11)

---

## CROSS-DOMAIN

**SENDING:**        ← ONE table (Will's arbitration, decision row 17: no STANDING / THIS-CYCLE split, no drop rule — amendment 4 was rejected; refresh at closeout)
| To | Signal | Priority | Mechanism it triggers in recipient's domain |
|----|--------|----------|---------------------------------------------|

**WAITING FOR:**        ← "Expected by" REQUIRED (amendment 7)
| From | Input | Expected by | Why it matters | How it changes my view |
|------|-------|-------------|----------------|------------------------|

---

## VIEW

<3-5 bullets — the current read in domain terms; compressed claims, not a STATUS recap.>

---

## CALIBRATION

- **Conviction (decomposed if applicable):** direction-[H/M/L] · timing-[H/M/L] · level-[H/M/L]   (single letter allowed — amendment 6)
- **Diverge from market by:** <claim, magnitude, why — preserve the framing>
- **Cross-agent tensions known to me:** <REQUIRED (amendment 2) — write "None active this cycle" if empty; never delete the bullet>
- **Uncertain about:** <what I don't know that would change my view; tag which desk owns the answer>
- **Failure patterns to mind:** <1-2 anchor patterns + reference to the desk's PREDICTIONS ledger — never a restated scoreboard>
- **RED counter-frame (if applicable):** <strongest current counter + my response, 1-2 lines; anchor to the red/ log>

---

## NEXT DECISION POINT        ← the agent-ACTIONED subset of the forward list (amendment 3)

- **What:** <the next thing this desk will act on>
- **When:** <date or trigger condition>
- **What would falsify the trigger:** <1-2 conditions — decision-falsification lives here, view-uncertainty lives in CALIBRATION>

---

## FORWARD CATALYSTS (next 2-4 weeks)        ← renamed from WATCH (amendment 3)

| Date | Event | Threshold / Signal |
|------|-------|---------------------|
```

### 2b. SCHEMA — COMPACT variant (amendment 9, Will-approved 2026-07-31; decision row 19 — restated, nothing added)

For **utility / single-seam desks** (narrow domain, few live edges — WATT, MIDAS, AEOLUS, VULCAN at ratification): a *curated cross-agent sync*. **Routing table FIRST — the per-recipient SENDING rows ARE the body;** no `## VIEW` / `## CALIBRATION` headers required; **header stamp, As-of + pin, and WAITING FOR retained.** Nothing else is required of a COMPACT brief. **Revert to FULL** when the desk grows to **≥3 persistent live edges** or carries a **thesis version**. Amendment 12 does not touch it.

```markdown
# <AGENT> — NEXUS Brief (compact)
**Status:** [🟢🟡🟠🔴] — <ONE primary claim, ≤120 chars>   **Domain:** <one line>
**As of:** YYYY-MM-DD HH:MM ET | STATUS commit: `<hash>`

**SENDING:** | To | Signal | Priority | Mechanism it triggers in recipient's domain |
**WAITING FOR:** | From | Input | Expected by | Why it matters | How it changes my view |
```
A brief that carries `## VIEW` but no `## CROSS-DOMAIN` matches neither variant's header set and is marked `n/a` on the conformance cell — "the amendment cannot apply," never "this brief is fine."

---

## 3. SECTION DESIGN NOTES

- **3.1 VIEW** — 3-5 declarative bullets, "what I'm thinking right now"; cite levels/dates/probabilities where load-bearing; the one section that generates novel content. If it will not compress, the thesis has not matured into a 1-2 sentence shape.
- **3.2 CALIBRATION** — the most load-bearing line is *Diverge from market by*: preserve the FRAMING ("70% vs market 96% — earned discount from two prior failures"), not only the number. *Cross-agent tensions* is REQUIRED because optional fields decay silently; "None active this cycle" forces the look each pass. Failure patterns and RED counter-frames are REFERENCED, never restated — a restated scoreboard forks from canon.
- **3.3 CROSS-DOMAIN** — the single most important section. SENDING's 4th column forces the desk to say what the signal DOES in the recipient's domain ("net selling >¥1T/month → reduces UST demand → upward 10Y pressure"), not what it IS. WAITING FOR's *Expected by* lets NEXUS detect waiting-on-waiting deadlock fleet-wide; use `Wed Jun 10` for hard dates, `Open — watch X` for conditions. Empty tables are fine; no placeholder rows. **No P/L, no money figures, no position $ amounts** — reference positions structurally only.
- **3.4 NEXT DECISION POINT** — three tight bullets: what · when · what would falsify the trigger. Decision-falsification lives here; view-uncertainty lives in CALIBRATION.
- **3.5 FORWARD CATALYSTS** — 2-4 weeks forward, 3-6 rows, the subset of the desk's calendar that matters for THIS view; NEXT DECISION's "what" appears as one row (cross-referenced, not dual-maintained).

---

## 4. MAINTENANCE DISCIPLINE

### 4.1 Update trigger
- **Mandatory write-back at the desk's closeout, every session.** A no-change session still refreshes the As-of stamp and the pin; a material STATUS change updates brief content the same session.
- **Amendment 10 (ORDERING):** the brief fold is the LAST write-back of the session — after the final STATUS write, immediately before the git commit. A brief written mid-session and left while STATUS work continues is the fleet's dominant content-stale mechanism (7/31 audit: 5 of 5).
- **Amendment 11 (INVARIANT, `pin-follows-STATUS-HEAD`):** the brief's pinned STATUS commit must EQUAL that desk's STATUS HEAD at the moment the brief is committed; a later same-session STATUS commit means re-pin and re-commit. This is a CHECK on the obligation above, not a new duty, and it is never shipped as an added closeout step in any desk's instructions (the self-ruling's scope constraint; five-test record → cold §A13).
- **Amendment 12 (SECTION ORDER):** in the FULL variant `## CROSS-DOMAIN` is the first body section — zero text added, ORDER only (origin: HOMER's truncation defect; §1 had ranked CROSS-DOMAIN first since R1 while the layout put it third, so every truncation cut the highest-value section first).

#### 4.1-R Rollout rule — the missing half of every amendment (2026-09-07)
> **An amendment that changes what a WRITER does is NOT IN FORCE when ratified; it is in force when every full-variant brief conforms, and until then its state is `RATIFIED-NOT-ROLLED-OUT` and its protection is ZERO.**
1. **TRIGGER** — each desk conforms at its NEXT re-pin (no new duty: the fold is already mandatory every session). A desk is non-conformant only after its next re-pin.
2. **OWNER — NEXUS**, discharged by the `order` conformance cell in `BRIEFS_MAP.md` (`A12` · `pre-A12` · `n/a`), regenerated by command each full pass — never by a one-time packet round (a packet to N owners is a sample that rots at the N+1th brief).
3. **ESCALATION** — NEXUS packets ONLY desks whose non-conformance is currently LOAD-BEARING: the byte offset of `## CROSS-DOMAIN` exceeds the single-read cap (54,250 B, READ_CAP rule 1). Protection is positional; sort by consequence, not conformance.
**Standing consequence:** no amendment (and no R4 clause) is ratifiable without its trigger, owner and observable-conformance surface named in the same word that ratifies it.

### 4.2 Cap discipline — HISTORICAL PILOT (2026-06) → cold §A13; number retained so citations resolve

### 4.3 Reference, never restate (the anti-drift rule)
| Content | Lives in | Brief format |
|---|---|---|
| Failure patterns | the desk's PREDICTIONS ledger preamble | 1-2 anchor names + reference |
| RED counter-frames | `red/<file>.md` | 1-line summary + reference |
| Full thesis | the desk's thesis file | version stamp in header |
| Forward catalysts | the desk's CALENDAR | FORWARD CATALYSTS = the subset that matters for VIEW |
| Cross-agent signals | `inbox/`, packets | CROSS-DOMAIN tables (steady-state surface) |
| Live market data | `STATUS.md` | specific levels only when load-bearing for VIEW / CALIBRATION |
VIEW is the exception: it generates compressed novel claims — it must compress STATUS, never restate it.

### 4.4 Stale-check + STATUS fallback (Q7 amendment) — the pin, the triggers, the token
**Mechanical stale-check:** NEXUS compares the pinned STATUS hash to the desk's STATUS HEAD. Mismatch → "N commits stale."
**NEXUS reads raw STATUS when ANY of:** **(a) mechanical staleness** — pin ≠ HEAD by >1 commit (a single-commit lag is tolerated); **(b) convergence drill-down** — two or more briefs hint at a thread neither names; **(c) cross-domain uncertainty** — a CALIBRATION "uncertain about" names another desk's domain. (a) is mechanical and always fires; (b) and (c) are NEXUS-side judgment. Drill-down chases cross-agent threads; it never audits within-domain work.
**Amendment-11 read-time carve-out (rollup #4, 2026-08-28):** a pin behind STATUS HEAD only by SAME-DAY commits is the multi-workstream case amendment 11 exists for and is not read as stale. **Precedence:** trigger (a) fires when the pin is >1 commit behind HEAD AND the lag is not same-day; a single-commit lag is tolerated as before. `BRIEFS_MAP.md`'s legend carries the historical PIN-STALE / CONTENT-STALE reading (content-fresh ⇒ not a trigger); where the two disagree this schema governs, and the disagreement is flagged to Will rather than re-ruled here.
**Pin token (RULED 2026-08-28, NEXUS's own §4.4 — form, not fleet policy):**
1. **Canonical token: `STATUS commit: \`<hash>\`` — that exact string, hash in backticks, 7+ hex.** The four pre-ruling variants (`STATUS commit \`h\`` · `STATUS pin: \`h\`` · `STATUS-HEAD PIN: \`h\`` and the canonical form) are grandfathered and must NOT be rewritten; any checker accepts all four until the owner next touches the header. `scripts/brief_pin_check.py` is the fleet checker.
2. **A pointer is not a pin.** "see `git log …`" / "refresh at close" / "rides the same commit" does not satisfy §4.4 — amendment 10 puts the fold after the STATUS write, so the hash is knowable; write it, or write `STATUS commit: NONE (reason)` so it fails loudly. An UNPINNED or pointer-valued pin is a §4.1 conformance gap owed at the owner's next fold.
3. **Any pin sweep reports COVERAGE and CLASS (A hash present · B field absent · C field present, value absent), never a bare defect count** — a rate over a population the instrument cannot see is not a rate.
4. **Never publish an "N lack X" figure off a single string grep; sample-re-read the hits first** (two detectors once disagreed on 7 of 26 desks while their totals differed by one).

### 4.5 Length
No line ceiling is enforced (ruled 2026-08-28: line count is nearly uncorrelated with byte load and a line cap rewards compression into longer lines). **The binding controls are (i) the root read budget — 32,550 B per brief, because NEXUS reads each brief whole — and (ii) POSITION (amendment 12).** A brief over budget is the owner's to rotate (verbatim, crc32, to a cold companion in its own dir); NEXUS flags it, never edits it. "N/A" sections are allowed with a one-line reason (`N/A — no active cross-agent threads this cycle`).

### 4.6 🔒 AMENDMENT CAP — the schema stops at 12 (RATIFIED 2026-09-01, Will-approved via PROME WQ-105, in the same word as amendment 12)
| | |
|---|---|
| **The number** | **12**, reached 2026-09-01. |
| **What is capped** | Numbered amendments — anything that changes what a brief IS, its form, section set, ordering or invariants. |
| **What is NOT capped** | Typo / link / path repair · re-measuring a figure the schema cites · the LIVE census (`BRIEFS_MAP.md`, no schema authority) · hot/cold splits of this file for the read cap (a storage change, not a schema change). |
| **What happens at the cap** | ⛔ Not a 13th amendment — a **RE-SPEC SITTING**: the first change that would have been amendment 13 re-opens the whole schema as one versioned document (**R4**), ratified in a single sitting, every amendment 7–12 re-argued from its evidence or dropped. A trigger, never a schedule. Will-gated (R4 changes what a brief is for ~29 desks). |
**The cap's own falsifier:** if a clear, cheap, zero-text defect repair is refused solely because the cap is reached, and the defect persists on the fleet's briefs for more than one full pass, the cap is wrong and must be re-ruled — grade at the first refusal.

---

## 5. History → cold
§§6–7 (design decisions, review history) → `archive/2026-08-28_BRIEF_SCHEMA_decision-log_and_review-history.md` (verbatim, crc32 3f13bf74; decision rows cited by number). The superseded amendment-11 header text, the 2026-06-07 scope list, the §4.1-R rollout-state measurement, the amendment-11 five-test record, the 100-line-ceiling ruling text, the 2026-06 §5 integration proposal and the PROME cap rationale → the same file, **§A13** (rotated 2026-10-24, verbatim, crc32 per block). Nothing governing lives only there.
