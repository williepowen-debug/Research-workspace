# CORAL -> PROME — 2026-10-29 — L784 triggers taken · GATE-CORAL-MSI-01 reading #11 · inbox drain 21/21

**Written:** 2026-10-29 00:19 EDT (Thu) · session coral-1029 · PROME prome-92 Tier-1 wake (WQ-184) on Will's 00:03 ET word · Opus 5.5 (claude-opus-5-5), Claude Code, Agent-tool desk spawn, cwd inherited from PROME/.
**Boot reads (bounded reader, each to `eof: true`):** root CLAUDE.md 4 pages · AGENTS.md 1 · USER.md 2 · AGENTS/CORAL/CLAUDE.md 5. Desk boot: STATUS, SCRATCH, THESIS, LESSONS read; CALENDAR read in part (rows touched).
**Commits (local, on master):** `5e85abbed` CORAL desk work + 21 consume moves (`consume:CORAL`) · `e2e4a24fc` CORAL -> AEOLUS packet · `1effd5fe7` CORAL -> NEXUS packet · this memo (next commit). ⛔ **NOT pushed:** the tree carries other desks' uncommitted work (BRENT, MIDAS, BROCK, LIQUID, SHADE…) and the shared index holds other sessions' staged renames (PROME/inbox ZHAO, LIQUID) — per the spawn brief, push is PROME's.

## 1. DOCKET L784 — the three dated triggers

| Trigger | Result (dated, sourced) | What it moves |
|---|---|---|
| (b) FEMA decision on FL's Isaias DR request (hard check was Fri 10/30) | **DECIDED 10/27: DR-4955-FL** (request 10/15). **Public Assistance categories A–G in all 15 requested counties; Individual Assistance in NONE of the 8 requested; Hazard Mitigation not designated.** Cost share **UNKNOWN** (no FEMA release on fema.gov/disaster/4955; Federal Register `FEMA-4955-DR` = 0 docs at 00:09 ET). **Last OpenFEMA record:** DR-4955-FL, `lastRefresh` 2026-10-28T11:09:04Z; dataset rundate 2026-10-29T04:08:55Z. | L784 § 5's **"deny" branch did NOT fire.** "75% flat vs enhanced" stays undecidable until the cost share publishes. ⚠️ The IA gap is NOT evidence of the posture: FEMA's ordinary IA factors (small uninsured home damage; insured FL claims ~$582M at 10/15, PRESS-relayed OIR) predict the same "PA yes, IA no". |
| (a) FHCF October capacity report | **PRIMARY, report dated 10/22/2026:** claims-paying **$22.26B vs $17B** (131%; May $21.43B) = YE fund $12.91B + $2.25B pre-event + $7.10B borrowing (0–12 mo, unchanged). **2027-28: $24.13B no covered event / $13.61B limit exhausted** (May $23.09B / $12.78B). Isaias not in it (losses as of 9/30). | L784 row 5 re-based **$21.43B → $22.26B**. FEMA $ at stake to FHCF stays $0 direct. |
| (c) 11/3 ballot (Amendment 3; HJR 5019) | Calendar entries, unchanged. | — |
| AEOLUS cell (satellites + carry ack) | **Still OWED by AEOLUS** — 10/21 packet unconsumed in `AGENTS/AEOLUS/inbox/`; no AEOLUS self-commit since 10/21. | — |
| SHADE cell (FHCF/Citizens/FL-muni bond holders) | **Still OWED by SHADE** — 10/21 packet unconsumed in `AGENTS/SHADE/inbox/` (SHADE shows uncommitted work tonight — may be live). | — |
| One number with AEOLUS | KB-AEO-210 "no DR" superseded ⇒ CORAL carries **DR-4955-FL**; packet `e2e4a24fc`. No figure shared with MARCO moved here. | — |

Artifacts: `AGENTS/CORAL/research/2026-10-21_L784_fema-cost-shift-florida.md` § 7 (10/29 update) · `STATUS_DETAIL.md` § X2–X4 · KB ML-CORAL-120/121. **Next L784 observable:** the Federal Register DR-4955 notice (cost share; any IA/HM amendment), then 11/3. Suggested DOCKET disposition: row stays PENDING on the FR notice + 11/3 (PROME's call; CORAL edits no DOCKET row).

## 2. GATE-CORAL-MSI-01 — reading #11 (owner grade; registration duty, four fields)

- **gate_id:** GATE-CORAL-MSI-01
- **condition (reading):** Parcl MSI, **data date 2026-10-27** (one build: metrics tile `20261028T091143Z`, bundles `20261028T091452Z`; first reading on the CURRENT series per WQ-475 A): **Tampa 7.27 · Punta Gorda 6.27 · North Port 6.30 · Cape Coral 5.89 · Lakeland 6.27 ⇒ 4-of-5 > 6.00 ⇒ re-fire reading FAILS, clock at zero; stand-down N/A (leg 🟠).** MSI = the 0–10 Motivated Seller Index, NOT months of supply (condo 7.7 / SF 4.4 Sept is a separate metric).
- **consequence:** none — leg stays 🟠; CORAL overall 🟠 and the bank-transmission rail untouched.
- **consumed_by:** CORAL at the next weekly reading — **review_by 2026-11-05 (reading #12)**.
- ⚠️ **New instrument fact:** the current series revises trailing days between builds (data date 10/20 read Cape Coral 5.88 in the 10/21 build, **5.93** in the 10/28 build; Tampa 7.22 → 7.24). Per WQ-475 (c) #10 stands as recorded; the #10 grade is identical on both vintages. No rule change proposed; CORAL logs the first build's value for a data date (the 9/28 letter's "first pull governs").

## 3. ACTIVE_DECISIONS row 7 — "does the GSE financing channel do what the credit channel did not?"

Waiting on **FL Realtors October monthly summaries (condo vs SF FINANCED closed units = closed − cash), release Mon 2026-11-16** — first full month under Full Review; November (~mid-Dec) confirms. Pointer now at STATUS OWED D. No new research.

## 4. Inbox drain — 21 of 21 (census at boot: top-level 5 = 4 packets + `.gitkeep`; WALTER/ 17)

| Sender | Items | Dispositions |
|---|---|---|
| CREED (10/21, aged 8 d) | 1 | acted (integrated 10/21; now moved) |
| DAEDALUS (10/23, WQ-508) | 1 | noted — B08/B34 already applied by `4da79f1ee`, verified at the charter, no contest |
| DEWEY (10/28) | 1 | info-only — MARCO-owned figure |
| FERT (10/28, Mosaic WARN) | 1 | acted — pillar labor (Polk = Lakeland metro), KB ML-CORAL-124; WARN primary 403 |
| WALTER | 17 | acted 8 · info-only 9 (board_log.tsv rows; KB ML-CORAL-123) |

Corrections: **COR-20261029-04 APPLIED** (MARCO: "MIA clean tell" withdrawn; STATUS tourism row + NEXUS_BRIEF now carry MARCO's MIA Sep −1.82%). Census after: top-level `.gitkeep` only, WALTER/ 0.
SIG-W-20261022-042 (Zillow peak drawdown) asked whether to add a series: **CORAL declines** — a smoothed level series moves the same way under the rival (mean reversion) and a new leg needs a proposal; logged as context.

## 5. State and skipped controls

- **Levels (fetch.py, pulled 00:11 ET 10/29; 10/28 closes):** KRE $72.11 · SSB $104.95 · SBCF $32.78 · BKU $42.81 · VLY $14.10 · USCB $19.92 · AMTB $29.65. Bank rail: REGINALD 10/28 "every read 8-K cell HOLDS at all four FL names; aggregate PROVISIONAL until the 10-Qs (~11/14)" — read, not re-graded.
- **SKIPPED:** git pull (tree dirty with other desks' work) · push (spawn brief) · `scripts/boot.py` (live prices pulled directly instead) · desk MEMORY.md read and its rotation (owed since 10/21) · structural STATUS rotation (STATUS 27,787 B = 85% of the read-cap, still rotate-tier; net −463 B tonight).
- consumer_check (1c) on the FHCF figure: 1 🔴 (NEXUS 10/23 digest, correctly dated) → packet `1effd5fe7`; DOCKET L784 is a 🟠 history-row candidate (PROME's). claim_check weekday: clean. orphan_check: only my AEOLUS packet (committed).

## COMPLETION — CORAL — 2026-10-29
STATUS: ✅ DONE
CHANGED: AGENTS/CORAL/{STATUS,STATUS_DETAIL,NEXUS_BRIEF,SCRATCH,CALENDAR}.md, board_log.tsv, workbook/KB.tsv, registry/corrections_receipts.tsv, research/2026-10-21_L784_fema-cost-shift-florida.md, sources/parcl/…build20261028T091452Z.csv, 21 inbox moves; packets AEOLUS + NEXUS inbox; this memo
RESULT: L784: FEMA declared DR-4955-FL 10/27 — PA in all 15 requested counties, IA in none of 8, HM none, cost share unpublished ("deny" branch not fired); FHCF Oct (10/22) $22.26B vs $17B, 2027-28 $24.13B/$13.61B. MSI-01 #11 (data 10/27): 4-of-5 > 6.00, Cape Coral 5.89 ⇒ re-fire fails, leg 🟠, next 11/5. Inbox 21/21 drained; COR-20261029-04 applied; GSE channel waits on FL Realtors Oct (11/16).
GAPS: AEOLUS and SHADE L784 cells still owed by those desks; DR-4955 cost share and the $237M basis UNKNOWN; STATUS still 85% of read-cap; MEMORY rotation owed; not pushed (others' work in tree).
WILL_NEEDS: None
FOLLOW-UP: PROME push via safe-push.sh; GATES MSI-01 review_by → 2026-11-05; L784 stays PENDING on the FR DR-4955 notice + 11/3; CORAL reads the FR notice and reading #12.
