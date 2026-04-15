# OTTO MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or delete, never just accumulate.*

---

## Feedback
- [2026-04-15] **Cross-agent signals route through WALTER, not direct-to-recipient.** Will directive this session. Drop signals as `AGENTS/WALTER/inbox/SIG-OTTO-WALTER-YYYYMMDD-[topic].md` using the standard frontmatter (to: WALTER (ACTION), info: [target]). Do not write directly into other agents' inbox/outbox paths. Archived superseded Feb 16 direct-to-REGINALD draft.
- [2026-04-15] **Bank monitoring is REGINALD's domain, not OTTO's.** When a priority list touches bank-level sizing, loss disclosures, or counterparty risk, hand to REGINALD via WALTER. OTTO's cut is fraud mechanics + ABS recovery metrics + transmission-to-bank identification — stop at "the bank is exposed," REGINALD sizes it.
- [2026-04-15] **OZK is REGINALD scope, not OTTO.** `AGENTS/REGINALD/OZK/` has full build (160-row KB, EARNINGS_PREP.md, scenarios, call questions, position mgmt). Don't duplicate. OTTO touches OZK only at auto-fraud crosslinks (e.g., First Brands recovery → WAL V2).
- [2026-04-15] Will prefers the plain-English punchline up front, then the structure. Example: the Tricolor "recovery outcome" question was reframed mid-session when it turned out the question itself was wrong (Mar 31 ≠ deadline, vehicle auction ≠ signal-rich metric). He wanted that said directly before the data table.

## Findings
- [2026-04-15] **Tricolor vehicle-sale deadline is Apr 30, 2026, not Mar 31.** STATUS.md had Mar 31 from an earlier target; trustee motion specified Apr 30. Creditor meeting continued to Jun 17 2026 — trustee distribution plan / per-lender split ETA post-Jun 17.
- [2026-04-15] **Tricolor ABS notes trade <10¢ on the dollar** per Feb 2026 noteholder suit (Janus Henderson + One William St + Ellington vs JPM/BCS/FITB, $230M+ holdings). Market-implied noteholder loss >90% — 3–4× worse than OTTO's 🔴 "recovery <25%" threshold. Strengthens Cockroach magnitude thesis (invalidation framework said >40% would weaken).
- [2026-04-15] **Tricolor vehicle cost basis $125M** (Bloomberg Dec 19 2025) — this is the auction ceiling, not a recovery indicator. Manheim +2.2% YoY early-Sep 2025 was favorable but storage/title/legal frictions erode. Per-warehouse-lender distribution only surfaces after Apr 30.
- [2026-04-15] **Tricolor borrower composition validates Invisible Exit thesis structurally:** 75% undocumented Hispanic immigrants, 68% no credit score, 50% no driver's license (Wolf Street Oct 17 2025). Vervent's bilingual "Fresh Start" loan modification program rather than aggressive collection = implicit concession that this cohort can't be recovered against.
- [2026-04-15] **Bank exposure ring is wider than 4 — now 5 named:** MTB escalated Apr 15 from "watch" to confirmed litigation exposure (American Banker). ACV Auctions disclosed $18.7M Tricolor-linked loss Feb 23 (non-bank, but expands the ring).
- [2026-04-15] **Apr 3 CNBC "systematic fraud" headline was re-coverage of Dec 17 2025 indictment**, not new charges. Kollar (CFO) + Seibold guilty pleas were Dec 16 — already in ML-OTTO-005 (Jan 26). No signal escalation required on cooperating witnesses.
- [2026-04-15] **STATUS.md "Prediction #24" and "#25" were mis-labeled signal triggers**, not formal predictions (archived SKELETON had them as cross-agent routing triggers). Fixed by moving "Carvana 10-K delayed / First Brands Ch.7" into a separate "Signal Triggers" section.
- [2026-04-15] **PSEC dividend at $0.045 vs historical $0.06** suggests OTTO-26 is confirmed, but specific Feb 20 2026 announcement timing not verified in public search. 5-minute PSEC 8-K check resolves it — flagged in LAST_COMPLETION.md.
- [2026-04-15] **FSK cut base dividend $0.70 → $0.48 Q1 2026.** Direct coverage disclosure: NII ran $0.57–$0.65 vs $0.70 old distribution Q4 2024–Q3 2025. Q1 2026 NII guide $0.44 vs new $0.48 div = 0.92× coverage. OTTO-27 → CONFIRMED.

## References
- [2026-04-15] Verita Global — Tricolor Ch.7 docket: https://veritaglobal.net/tricolor (note: WebFetch fails on cert verification; use WebSearch pointed at veritaglobal.net URLs, or pull specific document IDs directly)
- [2026-04-15] Kroll — First Brands docket (primary source for hearing dates, adjournments)
- [2026-04-15] SEC EDGAR CIK 0001569650 = OZK (REGINALD scope — don't monitor from OTTO)
- [2026-04-15] DOJ/SDNY — Judge Lewis J. Liman presides over Tricolor criminal case; trial Oct 19 2026
- [2026-04-15] FDIC OIG press releases — bank fraud charge announcements
- [2026-02-16] Prior cross-agent exposure map: `AGENTS/OTTO/archive/CROSS_AGENT_SIGNAL_REGINALD_APR15_draft_superseded.md` (context on RF $68M, HBAN 44% consumer, CFG fund finance channel)

## Session Notes

### CHANGES SINCE LAST SESSION (Apr 15 midday → Apr 15 evening)
- Remote had a parallel morning OTTO session (`e43c9e3f`, 10:18 AM, Prome/OpenClaw) that reached opposite verdicts on OTTO-26/-27 (both FALSIFIED) using stale data. Resolved via manual rebase — local verdicts (OTTO-26 NEEDS_VERIFY, OTTO-27 CONFIRMED with 247 Wall St / SignalBloom / Seeking Alpha sources) preserved; remote's unique scripts and workbook TSVs pulled into our tree.
- `workbook/PREDICTIONS.tsv` question resolved: file now exists (created earlier today) — CLAUDE.md reference is valid.

### LAST SESSION (Apr 15 evening — reconcile with remote OTTO, push)
- Rebased 3 OTTO local commits onto origin (`378e90d8`, `e2ffa06a`, `a69c78d5`). Resolved 2 conflicts: STATUS.md (kept ours) and PREDICTIONS.tsv root (kept deleted; archived copy preserved).
- Pulled in from remote `e43c9e3f`: `scripts/abs_issuance_tracker.py`, `scripts/extension_proxy.py`, `workbook/ABS_ISSUANCE.tsv`, `workbook/EXTENSION_PROXY.tsv`, `workbook/CROSS_AGENT_LOG.tsv`. Not yet reviewed for content or usefulness — next session triage.
- Pushed 15 commits to origin/master. Branch up to date.
- Backup branch `otto-backup-pre-rebase-20260415` retained locally (safe to delete after next session confirms everything is fine).

### NEXT SESSION
1. **P0: Review remote-inherited files** — `scripts/abs_issuance_tracker.py`, `scripts/extension_proxy.py`, `workbook/{ABS_ISSUANCE,EXTENSION_PROXY,CROSS_AGENT_LOG}.tsv`. Decide: keep, refactor, or retire. Check CROSS_AGENT_LOG against our WALTER-routing convention.
2. **P0: OTTO-26 PSEC manual verification** — 5-min check of PSEC 8-K filings Feb 2026. Remote's AM run claimed FALSIFIED ("$0.54 annual maintained" — but $0.54/12 = $0.045, matching the post-cut amount, so their conclusion was internally inconsistent). Resolve definitively.
3. **P0: Apr 30–May 5 — Tricolor trustee filings re-check.** Post-deadline proceeds quantification; any extension motion; per-lender distribution preview.
4. **P1: Inbox processing** — 3 prior items already moved to `inbox/processed/`. Remote added `OTTO_2026-04-15_Tricolor_Bank_Losses.md` in WALTER's inbox — confirm WALTER processed it.
5. **P1: First Brands docket check** — Apr 9 hearing was adjourned, no new date when last checked.
6. **P1: Delete `otto-backup-pre-rebase-20260415` branch** if rebase result looks clean on next review.
6. **P2: WAL / Jefferies / Point Bonita $715M thread** from Apr 6 auto-parts research inbox.
7. **P2: CVNA short-seller scan pre-May 5 split vote** (Gotham / Hindenburg monitoring per CLAUDE.md).
8. **P3: Ally Q1 print (late Apr)** — OTTO-28 watch for Carvana-specific DQ/NCO break-out.
9. **P3: Jun 17 creditor meeting** — OTTO-29 resolution trigger; check for trustee distribution plan.

### INFRASTRUCTURE CHANGES (persistent)
- **MEMORY.md created** (this file). Add to boot sequence and closing protocol in OTTO CLAUDE.md when convenient.
- **Cross-agent signal routing via WALTER** (not direct-to-recipient). Supersedes Feb 16 direct-write pattern.
- **OZK de-scoped** from OTTO domain (REGINALD owns). STATUS.md timeline updated to reflect.
- **STATUS.md boot-pointer added** at top (directs new spawns to read LAST_COMPLETION.md first).
