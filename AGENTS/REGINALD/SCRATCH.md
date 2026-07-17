# REGINALD SCRATCH

*Loose notes, intra-day workspace, observations that don't fit anywhere else yet.*

**Purpose:** Capture stuff during the work — half-thoughts, things noticed in passing, quotes worth remembering, format gotchas, draft language.

**What this is NOT:**
- Not a task list (use MEMORY NEXT SESSION)
- Not curated memory (use MEMORY)
- Not a thesis (use THESIS / sub-bank THESIS files)
- Not a research backlog (use ROADMAP — Investigations Backlog section)
- Not a session-bridge (MEMORY Session Notes does that)

**Maintenance discipline:**
- Date each entry / section
- Promote to KB / ROADMAP / STATUS / MEMORY when it grows up; delete when it's done
- Prune aggressively — if a note is older than ~2 weeks and hasn't earned a promotion, delete it

---

## 2026-07-17 — Boot + CFG print read + tripwire fire-fade + 3-packet integration

**Noticed during the session:**
- **The tripwire's pre-registered driver-decomp rule earned its keep.** VX-REG-18.04 technically hard-fired 7/13 (3 consec >3.6×: 3.607/3.606/3.613 — all within 0.013 of the line) then reset 7/14. Without the 6/25-built decomp rule ("HY-tightening=beta=no escalate") I'd have faced a judgment call on escalating a marginal, already-faded fire; the rule pre-decided it. The design lesson: the escalation clause keying on the DRIVER (CCC-led vs HY-led), not just the level, is what kept a denominator artifact from becoming a false 🔴 to LIQUID/BROCK.
- **CFG −3.27% the day AFTER a clean beat** — on a broad risk-off tape (SPY −1%, KRE −2.1%, VIX +9.8%). Post-beat profit-taking + beta. Watch that Monday: a WAL/OZK sell-off into/after the print needs the same beta-vs-substance decomposition before reading it as thesis-confirming.
- **Brent +$11.67/wk and the 7/10 "sustain verdict" framing is overtaken** — the question was whether $76 sustains; the tape answered with $87.67. HAWK/BRENT own the verdict; my STATUS rows now carry the escalation read (oil leg FIRING).
- **WALTER's BB/B sub-index gap flag (SIG-717-003) is worth remembering when citing REG-T-03/04:** blended HY at 8.3 pctile while CCC at 87.8 pctile — the blended >320/>350 triggers may lag a tail-led break. Not actionable now; lane fix is PROME's.

**Threads carried (ROADMAP):** 7/21 double-print grading (frames done, ALLY pin added); POSITIONS broker refresh gate; BROCK bank→BDC map fill (CFG data now in hand); post-7/21 rewrite buckets.

---

## 2026-07-10 — Core-files staleness sweep + triaged remediation

**Noticed during the session:**
- **PAT-043 in the wild.** The audit's headline — live thesis in STATUS, thesis-of-record fossilized — is exactly decay-from-the-durable-end. The tell: refresh loops touch STATUS because it's convenient mid-session; THESIS/TIMELINE/INDEX/MATRIX only move on a deliberate rewrite that never gets scheduled. Banner-guard is the cheap interim; the real fix is *scheduling* the rewrite (post-7/21).
- **The two-clock header silences its own nag.** Adding a STALE-VINTAGE header to KB/FLOW resets the git-commit-time the staleness script keys on → boot-7a stops flagging them. Caught it before committing; moved the refresh-debt to a ROADMAP thread so it's not lost. The human-readable "Last real data refresh" date is the honest artifact, but you MUST re-home the auto-nag or it vanishes (PAT-044 laundering).
- **CCC/HY quietly walked back to the tripwire line.** 3.49× [6/24] → 3.61× [7/9], AT the 3.6× line, ARMED 1-of-3. But the driver is HY compression (270 vs 276 6/24), not a CCC blowout — a denominator-shrink move, beta-ish, not tail-substance. Don't over-read the single close. *(RESOLVED 7/17: it went on to complete the 3-consec fire 7/13 then reset 7/14 — graded beta/benign per the decomp rule, no escalation. See 7/17 section + VX.tsv.)*

**Threads carried (ROADMAP):** post-Jul-21 thesis-of-record rewrite (bucket 2) + KB reconstruction (bucket 3); VX-REG-18.04 X1-root reframe; inbox (2 PROME + 5 WALTER) not processed.

---

*(6/25 section pruned 2026-07-17 — >3wk; tripwire def promoted to research/CCC_HY_TRIPWIRE + VX row; Q2 grid/axis-split live in research/Q2_* files + grading frame; un-done leftovers [ZION 6/30 AOCI re-pull, boot.py consec-counter] promoted to ROADMAP backlog.)*

*(6/22 section pruned 2026-07-17; 6/20 + 6/19 pruned 2026-07-10 — >2wk, substance in ROADMAP Recently Resolved / MEMORY Findings.)*

## TEMPLATE FOR FUTURE DAYS

```
## YYYY-MM-DD <morning/PM> — <one-line context>

**<Section header>:**
- bullet
- bullet

**Things I noticed but didn't dig into:**
- ...

**One-liners cached:**
```bash
# ...
```

**Convention question / open-thread for next session:**
- ...
```

---

*Companion: `ROADMAP.md` (persistent state across sessions) | `MEMORY.md` (curated cross-session memory) | `STATUS.md` (live dashboard)*
