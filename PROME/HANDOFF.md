# PROME HANDOFF
**Date:** 2026-05-09 21:25 ET  
**Status:** ✅ Clear-ready handoff — weekend regional-bank build in progress; next session should continue ZION expansion + Monday bank/FSK prep

---

## Immediate State

Will asked to prep for handoff after a long regional-bank triage session.

**Current working posture:**
- Private-credit thesis intact but timing slowed; FSK May 11 remains next BDC canary.
- Current portfolio risk is more **regional-bank puts** than APO/ARES/OWL residuals.
- Regional-bank work has moved from ad hoc analysis into action-card / decision-rail mode.
- ZION was initially treated too cleanly because its folder was thin. Correction: **ZION is under-researched, not exonerated.**
- We discovered the heavily researched target Will was remembering was **OZK**, not ZION. ZION was mostly a WAL comparator/control case.

**No trades executed. No external messages sent. Do not commit/stash/pull without Will approval.**

---

## Most Important Decisions / Current Calls

### ZION July put
Position reviewed: `ZION $57.5P Jul 17 2026`.

Current recommendation remains:

> **Kill / sell if there is a usable bid. Do not roll. Do not add.**

But language was corrected:

> **ZION is not clean-clean. It has latent structural risk and one disclosure-negative C&I move. But current evidence does not support keeping/rolling a July OTM put as conviction exposure.**

If bid is unusably poor, acceptable fallback: leave as tiny paid-for AOCI/regulatory lottery into Jun 18; do not average down or roll.

### Why ZION call is nuanced
Evidence found:
- ZION folded **~$374M leasing into C&I** in Q1 — disclosure-negative.
- Q1 10-Q/source text does **not** contain `MI3`, `Memo Item 3`, or `RCON2746`; Call Report needed.
- C&I metrics were not flashing: nonaccruals and 30-89d past dues improved QoQ.
- CRE/office nonaccruals improved; no near-term recognition pressure in Q1 10-Q.
- Muni/conduit risk exists, but current muni nonaccruals only ~$2M.
- Multifamily is the best latent CRE issue: **$4.1B / 30% of CRE; ~46% matures within 12 months**.
- Fraud/accounting evidence mostly cuts **against WAL**, not against ZION: ZION charged off aggressively, used EY, led disclosure.

### ZION research status
Updated stance:

> **ZION is under-researched, not exonerated.** Current July put can be killed on timing/evidence, but ZION needs an OZK/WAL-style research pass before being dismissed.

New scaffold created:
- `AGENTS/REGINALD/ZION/INDEX.md`
- `AGENTS/REGINALD/ZION/TODO.md`
- `AGENTS/REGINALD/ZION/research/ZION_DEEP_DIVE_FRAMEWORK.md`

Priority next for ZION:
1. Q1 Call Report MI3 / RCON2746 / hidden CRE screen.
2. CRE + multifamily maturity wall.
3. Municipal / conduit risk.
4. Fraud/accounting follow-through.
5. AOCI / Basel offset.
6. Funding/liquidity durability.
7. Insider/governance scan.
8. Then `SCENARIOS.md`, `WEAKNESSES.md`, possible `THESIS.md` v2.

---

## Files Changed This Session

### Created
- `AGENTS/REGINALD/ZION/INDEX.md` — ZION research entry point and boot map.
- `AGENTS/REGINALD/ZION/TODO.md` — ZION deep-dive backlog.
- `AGENTS/REGINALD/ZION/research/ZION_DEEP_DIVE_FRAMEWORK.md` — question tree / vectors / decision rule.
- `PROME/ZION_SINGLE_BANK_TRIAGE_MAY9.md` — ZION single-bank triage memo.

### Modified
- `PROME/ZION_SINGLE_BANK_TRIAGE_MAY9.md` — updated multiple times:
  - Added Memo Item 3 / C&I caveat.
  - Added deeper REGINALD/sub-agent evidence.
  - Added full ZION subtree sweep findings.
  - Added reopen conditions including `MI3 / RCON2746` and multifamily stress.

### Not modified in final handoff except this file
- `PROME/TODAY.md` and `PROME/STATUS.md` were read and remain generally current from earlier May 9 build, but their ZION line is now slightly stale because ZION scaffold was created after them.
- `HEARTBEAT.md` was read by heartbeat poll and remains dated May 9 11:20 ET; should be refreshed after weekend build / Monday prep settles.

---

## Local / Git State Notes

Git sync remains blocked / dirty. Earlier checks showed local branch behind origin and many unstaged/untracked files.

Important:
- Do **not** run `git pull --rebase` without handling local changes.
- Do **not** commit/stash without Will approval.
- Local ZION tree now has more files than origin because scaffold and 10-Q mirror files are untracked.

GitHub/origin had only these tracked ZION files before scaffold:
```text
AGENTS/REGINALD/ZION/FRAUD/README.md
AGENTS/REGINALD/ZION/Q1_2026_ANALYSIS.md
AGENTS/REGINALD/ZION/sources/transcript_Q1_2026.md
AGENTS/REGINALD/ZION/STATUS.md
AGENTS/REGINALD/ZION/THESIS.md
AGENTS/REGINALD/ZION/workbook/KB.tsv
```

Local-only/untracked ZION source mirrors existed:
```text
AGENTS/REGINALD/ZION/sources/ZION_10Q_Q1_2026_stocktitan_raw.html
AGENTS/REGINALD/ZION/sources/ZION_10Q_Q1_2026_stocktitan_text.txt
```

---

## Research Trail / Evidence Checked

### ZION subtree sweep
Checked all local files under `AGENTS/REGINALD/ZION`:
- `FRAUD/README.md`
- `Q1_2026_ANALYSIS.md`
- `STATUS.md`
- `THESIS.md`
- `workbook/KB.tsv`
- `sources/transcript_Q1_2026.md`
- `sources/ZION_10Q_Q1_2026_stocktitan_text.txt`
- `sources/ZION_10Q_Q1_2026_stocktitan_raw.html`

Findings:
- Only 6 tracked files on origin before scaffold; 8 local including mirrors; now more due scaffold.
- ZION folder was thin because ZION was originally a comparator, not deep target.
- Related ZION evidence is scattered elsewhere, especially WAL/research outputs.

Related files worth checking later:
```text
AGENTS/REGINALD/WAL/FRAUD/ZION_AUDIT_COMPARISON.md
AGENTS/REGINALD/WAL/research/RQ-REG-A01_WAL_ZION_FRAUD_COMPARISON.md
AGENTS/REGINALD/research/outputs/RQ-ad-hoc/RQ-REG-A01_WAL_ZION_FRAUD_COMPARISON.md
AGENTS/REGINALD/domain/INSIDER_BEHAVIOR_SCAN.md
AGENTS/REGINALD/research/outputs/RP-REG-3.2/Municipal_Securities_Exposure_Analysis.md
```

### OZK realization
Will remembered that the heavy research was **OZK**, not ZION.

OZK lives at:
```text
AGENTS/OZK/
```
not `AGENTS/REGINALD/OZK/`.

OZK is fully built out with:
- `INDEX.md`
- `STATUS.md`
- `THESIS.md`
- `Q1_2026_ANALYSIS.md`
- `IQHQ_PLAYBOOK.md`
- `SEVEN_CREDIT_DEEP_DIVE.md`
- `THREAD3_ROLL_MATH.md`
- `workbook/KB.tsv`
- subdirs: `GEOGRAPHY/`, `LIFE_SCI/`, `PRIVATE_CREDIT/`, `INSIDERS/`, `research/`, `raw/`, `sources/`, etc.

This is the model for how ZION should be expanded tomorrow.

---

## Current Open TODOs

### 🔴 1. Expand ZION research tomorrow — likely REGINALD-owned
Will suggested REGINALD may handle filling out the ZION scaffold. PROME could not find a live REGINALD session via `sessions_list`, so an inbox note was written:

```text
AGENTS/REGINALD/inbox/PROME-20260509-zion-scaffold-fill-request.md
```

Start with `AGENTS/REGINALD/ZION/INDEX.md` then `TODO.md`.

First real task:

> **Q1 Call Report MI3 / RCON2746 hidden-CRE screen for ZION.**

Output target:
```text
AGENTS/REGINALD/ZION/research/MI3_HIDDEN_CRE_SCREEN.md
```

Then:
```text
AGENTS/REGINALD/ZION/research/CRE_MULTIFAMILY_MATURITY.md
AGENTS/REGINALD/ZION/research/MUNI_CONDUIT_RISK.md
AGENTS/REGINALD/ZION/research/AOCI_CAPITAL_RULE.md
AGENTS/REGINALD/ZION/research/FRAUD_ACCOUNTING_COMPARISON.md
AGENTS/REGINALD/ZION/research/INSIDER_GOVERNANCE_SCAN.md
```

### 🔴 2. Continue regional-bank Call Report triage
Current focus remains:
- WAL
- OZK
- EGBN
- CFG
- VLY
- ZION
- FITB
- SSB / HBAN as needed

Need extract:
- MI3 / RCON2746
- NDFI / warehouse / lender finance if visible
- ACL / NCO / classified / nonaccrual trends
- FHLB / brokered deposits / uninsured liquidity
- modified loans / maturity wall clues

### 🔴 3. Monday bank decision prompt
Needs to cover:
- May scraps cleanup.
- KRE/WAL June roll/salvage.
- OZK/KRE/WAL Sep-Dec runway.
- ZION kill/retain.
- No broad bank-premium add unless Call Reports/tape branch Bear / Strong Bear.

### 🔴 4. FSK May 11 live read
Use:
- `AGENTS/BROCK/domain/sources/FSK_PREBUILD_MAY11.md`
- `PROME/action-cards/FSK_MAY11_ACTION_CARD.md`

Default:
- No fresh private-credit premium unless FSK is Bear / Strong Bear.
- Existing APO/ARES/OWL residuals are small; FSK mainly governs fresh capital / roll decisions.

### 🟠 5. GCRED / OTF / BCRED / CTAC 10-Q watch
Still pending. These are real private-credit forced-mark tests after OBDC/FSK.

### 🟠 6. EDGAR filing-watch routing dry-run
MVP/baseline exists and watchlist expanded earlier, but routing dry-run remains incomplete.

### 🟠 7. Refresh state files after weekend build
After ZION scaffold + Call Report plan settles, refresh:
- `HEARTBEAT.md`
- `PROME/STATUS.md`
- `PROME/TODAY.md` if needed
- `PROME/SCRATCH.md`

---

## Current Rules / Constraints

- **No trade execution without Will approval.**
- **No fresh private-credit premium** unless FSK is Bear / Strong Bear.
- **No broad bank-premium add** unless Call Reports/tape move to Bear / Strong Bear.
- **No rolling every losing June contract.** Prefer one or two higher-delta candidates if confirmed.
- **No panic-selling Sep/Dec runway** into green tape.
- **May contracts are cleanup**, not thesis core.
- **Do not spawn REGINALD, CARL, SAM, RED, or BRENT.** REGINALD is persistent/managed.
- **Do not use `git pull --rebase`, commit, or stash without Will approval** while working tree is dirty.

---

## Suggested Fresh-Session Prompt

> Continue from `PROME/HANDOFF.md`. Focus first on expanding ZION properly, using `AGENTS/REGINALD/ZION/INDEX.md` and `TODO.md`. Do not treat ZION as clean just because the folder was thin. Start with the Q1 Call Report MI3 / RCON2746 hidden-CRE screen, then CRE/multifamily and muni/conduit. Keep current ZION trade posture separate from research status: July put is kill/no-roll if usable bid, but ZION remains under-researched. After ZION framework, continue regional-bank Call Report triage and build Monday’s bank decision prompt. Do not spawn REGINALD and do not trade.
