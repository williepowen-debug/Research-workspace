# Fleet Protocol Standardization Audit — 2026-06-27 (Sat)
**Owner:** Prome · **Method:** 20-agent read-only Workflow fan-out (Explore agents, evidence-quoted, schema-structured) judged against the fleet standard (root `CLAUDE.md` Git Protocol + Data Hygiene + the BRENT/SAM session-spine exemplars). Findings PROME-verified before this writeup.

**Scope:** 20 active agents (+ CREED Tier-2 attempted). DEWEY (Tier-2, swept) / OZK (dormant, git-rehabbed 6/27) out of scope. PROME self-audited inline (clean; 2 low-sev self-notes below).

---

## Headline

**The "auto-push migration 18/21 COMPLETE" claim in HANDOFF/STATUS/ACTIVE_DECISIONS was over-counted.** The audit verifies **only ~13/20 on auto-push; 7 agents are genuinely still on the old defer-push model** (never swept, or half-swept). The migration counted agents it never actually checked. This is the #1 correction — my own state docs need fixing too.

Second headline: the biggest *convergent* gap is **data hygiene — 8 agents have silently-rotting LIVE ledgers**. The root `CLAUDE.md` Data Hygiene RULE exists ("FROZEN or LIVE-with-boot-alert"), but **no agent has actually wired the boot-time staleness alert** — the rule has no enforcement mechanism. One shared mechanism closes all 8.

---

## Verified findings by tier

### TIER A — GIT PROTOCOL: auto-push lazy-sweep incomplete (7 agents)
Genuine defer-push / contradictory drift (NOT intentional holdouts). Same one-line fix pattern each (the canonical auto-push block):

| Agent | State | Evidence |
|---|---|---|
| **NEXUS** | defer-push (+ worst overall) | CLAUDE.md L76 "Push deferred by default… Will coordinates the push" |
| **BRENT** | defer-push *(an exemplar — ironic)* | L55 "commit locally only. Push only when Will has explicitly opened a push window… Root CLAUDE.md … is overridden" |
| **VIOLET** | defer-push / no safe-push wired | CLAUDE.md L54 + SCRATCH "Defer push to a Will-coordinated window" |
| **REGINALD** | defer-push | L83 "note pending push in MEMORY … and defer" |
| **BROCK** | defer-push | L60 "note the pending push and defer" |
| **SHADE** | defer-push (never swept; spun up 6/26) | L106 "Push only when Will coordinates" |
| **HAWK** | **contradictory** (half-swept) | L52 "commit locally, defer push" vs Git-step-4 "auto-push at closeout via safe-push.sh" |

Intentional holdouts (correctly defer — leave): **TERRY** (live/self-sweep), **WALTER** (architectural, BOARD_CONSUMPTION_SPEC §7). Verified-clean auto-push: SAM, CARL, LIQUID, RED, HENRY, LABOR, MARCO, BOND, CORAL, ORACLE.

### TIER B — DATA HYGIENE: silent-rot ledgers (8 agents — CONVERGENT → fleet-layer fix)
LIVE workbook TSVs, months stale, no FROZEN banner, no boot-time alert:
- **REGINALD** — 7 TSVs, FLOW.tsv **114d**, VX_HISTORY **161d**
- **BROCK** — BANK_BDC_MATRIX.tsv **3.5mo**
- **SAM** — FLOW (15d) / VX (28d); **HENRY** — multiple; **MARCO** — FLOW/ML; **LIQUID** — PREDICTIONS (14d); **HAWK** — files fresh but no alert infra; **SHADE** — board_log
- Plus VIOLET/ORACLE/RED have ledgers with no boot alert (lower urgency).

Per `[[finding_fleet_selfreport_convergence]]`: don't ad-hoc-fix 8 times. **Build the missing mechanism once** (a shared `scripts/` boot-time mtime staleness checker) + wire each agent's boot to call it, OR freeze the dead ledgers with banners. This is the genuinely-new "improve the network" infrastructure.

### TIER C — SESSION SPINE: retired patterns + stale briefs/spines
- **Retired LAST_COMPLETION.md as canonical handoff** (should be SCRATCH per BRENT): **NEXUS** (high), **HENRY** (high). *(WALTER uses it by design — intentional.)*
- **Retired-agent refs as live:** **NEXUS** lists HERMES + DARWIN as live Tier-2 (both retired/archived); **BOND** treats HERMES as live delivery.
- **Stale NEXUS_BRIEF** (As-of behind STATUS — owner-lane refresh): BRENT (6/24<6/26), HENRY (6/23), **LABOR (6/16<6/26)**, BROCK (6/20<6/26).
- **Stale STATUS spine** (header/body/commit-date mismatch — owner-lane): REGINALD, LABOR, BROCK (hdr 6/20 vs commit 6/26), NEXUS.
- **SHADE NEXUS_BRIEF absent** — intentional bootstrap (its CLAUDE.md L75 says "add in a later pass").

### TIER D — minor / cosmetic
- Pre-commit `git status -- AGENTS/<NAME>/` not restated in most per-agent CLAUDE.md (root covers it as mandatory; low value to duplicate).
- BRENT L67 typo "All mail lives in removed:".
- MARCO ML.tsv documented-FROZEN but lacks the banner line (folds into Tier B).

### PROME self-audit (clean, 2 low-sev)
- PROME/CLAUDE.md "Ask First → commits/pushes" not reconciled with auto-push-at-closeout (CLOSEOUT.md is correct). Add the standing-exception note.
- CLOSEOUT.md L57 stale "COMM mailbox" ref from OpenClaw cutover.

---

## DISCARDED (verified false-positives)
- **CREED "directory missing / significant-drift"** → reader-error (auditor used wrong path `PROME/AGENTS/`). CREED exists. *(Real residual: CREED CLAUDE.md has no git section — Tier-2, low-pri.)*
- **"Remove `[[feedback_defer_push_coordinate]]` citation"** (CARL/MARCO/CORAL/LABOR/HENRY) → the slug was rewritten to mean auto-push; the citations are **correct**. Not a fix.
- **SAM "archive/LAST_COMPLETION.md" retired-ref** → auditor self-noted it's archived/not-live. No action.

---

## Proposed execution plan (4 lanes)

**Lane 1 — PROME-direct mechanical (needs Will OK; established migration pattern):**
Complete the auto-push lazy-sweep on the 7 drift agents (NEXUS, BRENT, VIOLET, REGINALD, BROCK, SHADE + dedupe HAWK's L52) — same canonical block PROME applied 6/26-6/27. None are live (live=ORACLE/TERRY/WALTER), so no collision. Then **correct my own state docs** (HANDOFF/STATUS/ACTIVE_DECISIONS/ROSTER/AUTOPUSH_MIGRATION_PLAN): "18/21" → verified "13/20 + 7 swept this pass."

**Lane 2 — Fleet infrastructure (the centerpiece):** build the boot-time ledger-staleness checker so the root Data Hygiene rule is enforceable; freeze the clearly-dead ledgers (REGINALD ×7, BROCK matrix) with banners; wire the live ones.

**Lane 3 — Owner-routed SIGs (content changes I shouldn't make unilaterally):** NEXUS (LAST_COMPLETION→SCRATCH, drop HERMES/DARWIN, flip push, refresh spine — bundle with the pending PREDICTIONS_MONITOR migration flag), HENRY (LAST_COMPLETION decision), BOND (drop HERMES-live refs).

**Lane 4 — Owner-lane flags (no PROME action):** stale NEXUS_BRIEF / STATUS spine refreshes (BRENT/LABOR/BROCK/REGINALD) — each owner fixes at its next closeout.

---

## EXECUTION RECORD — 2026-06-27 PM (Will approved Lanes 1 + 2)

**Lane 1 — DONE (commit `c7d216e1`):** auto-push sweep on all 7 drift agents (NEXUS/BRENT/VIOLET/REGINALD/BROCK/HAWK/SHADE) — canonical block, tailored per agent's handoff file; verified residual defer-push = 0. State-record corrected (this commit): AUTOPUSH_MIGRATION_PLAN / ACTIVE_DECISIONS / STATUS — "18/21" → verified "17 auto-push + 2 intentional holdouts (TERRY/WALTER)". Lesson: a self-reported migration count ≠ verification (`[[finding_verify_counts_before_propagating]]`).

**Lane 2 — DONE (commit `4a9e70cd`):** built `scripts/ledger_staleness.py` — the missing enforcement mechanism for the root Data Hygiene rule (boot-time git-mtime alert vs STATUS; FROZEN-aware; by-name exemptions for schema/archive/backup/history/template; `--all`/`--quiet`/`--strict`/`--days`). Ran fleet-wide → ground truth replaces the haiku auditors' secondhand claims.

### Ledger ground-truth (refined scan, 30d-behind-STATUS, active agents)
| Agent | Genuinely-rotting LIVE ledgers | Disposition |
|---|---|---|
| **REGINALD** | DARKPOOL, OPTIONS_OI, SHORT_INTEREST, SHORT_VOL (70-78d) | **FROZEN this session** — verified dead (0 live consumers, not in file-table, abandoned ~Apr feeds) |
| **REGINALD** | FLOW (113d), KB (77d) | **HELD for owner** — FLOW is live (6 refs + documented) → needs *refresh* not freeze; KB is the knowledge base (age ≠ rot) |
| **BROCK** | BANK_BDC_MATRIX (106d) | **HELD for owner** — documented in BROCK's file-table (slow-moving reference, not orphaned); owner decides freeze-vs-refresh |
| **CARL** | ABS_BASELINE (71d) | flag owner *(CARL already froze 5 others — good hygiene)* |
| **HAWK** | PRICE_BREACHES (67d) | flag owner |
| **RED** | FLOW (77d) | flag owner |
| **BRENT** | GROUP_MAP (110d) | flag owner *(mapping file, borderline)* |

*Tier-2/dormant/archive (OTTO/REITS/HANS/ZHAO) show stale ledgers as expected — not actioned.*

**Judgment surfaced to Will:** I deliberately did NOT blind-freeze the live/documented ledgers (REGINALD FLOW+KB, BROCK matrix) despite the Lane-2 "freeze REGINALD/BROCK" framing — `[[finding_workbook_demote_by_verification]]`: a consumer-grep proved FLOW/KB are live and BROCK matrix is documented. Freezing them would have been wrong. Only the 4 verified-orphaned feeds were frozen.

### Still open (not in Lanes 1+2)
- **Wiring the alert into agent boots** — ✅ DONE for the 6 rotting agents (BRENT/REGINALD/BROCK/HAWK/RED/CARL; commit `63e90d53`, Will-directed targeted wiring). Each now runs `ledger_staleness.py <NAME> --quiet` at boot. Fleet-wide wiring (the other 13 active agents) remains optional/later.
- **Lane 3 (deferred):** NEXUS (LAST_COMPLETION→SCRATCH, drop HERMES/DARWIN, refresh spine — bundle w/ PREDICTIONS_MONITOR migration), HENRY (LAST_COMPLETION), BOND (HERMES-live refs).
- **Lane 4:** owner brief/STATUS-spine refreshes (BRENT/LABOR/BROCK/REGINALD).
- **CREED Tier-2** CLAUDE.md has no git-protocol section (low-pri).
- **PROME self-notes:** CLAUDE.md "ask before push" vs auto-push reconcile; CLOSEOUT.md stale "COMM" ref.
