# OTTO MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to thesis or delete, never just accumulate.*

---

## Feedback
- [2026-04-15] **Cross-agent signals route through WALTER, not direct-to-recipient.** Drop signals as `AGENTS/WALTER/inbox/SIG-OTTO-WALTER-YYYYMMDD-[topic].md` using standard frontmatter (to: WALTER (ACTION), info: [target]). Do not write directly into other agents' inbox/outbox paths.
- [2026-04-15] **Bank monitoring is REGINALD's domain, not OTTO's.** OTTO's cut = fraud mechanics + ABS recovery metrics + transmission-to-bank identification — stop at "the bank is exposed," REGINALD sizes it.
- [2026-04-15] **OZK is REGINALD scope, not OTTO.** Don't duplicate. OTTO touches OZK only at auto-fraud crosslinks.
- [2026-04-15] **Plain-English punchline first, then structure.** Especially when reframing a question mid-session (e.g., Apr 15 Tricolor recovery question turned out to be the wrong question — Will wanted that said directly before the data table).
- [2026-05-21] **When a prior recalibration turns out wrong, say so plainly and supersede the ML/STATUS entries** rather than layering corrections. Apr 15 OTTO said real Tricolor deadline was Apr 30; May 21 sourced docket shows Mar 31 was operative. ML-OTTO-145 explicitly supersedes ML-OTTO-140's deadline assertion. Don't soft-pedal "may have been incorrect" — be definite when sources support it.
- [2026-05-21] **Verita docket has cert-verification failure** — WebFetch fails on `veritaglobal.net/tricolor/document/*` URLs. Search surfaces titles but not contents. PACER would be the right channel; OTTO doesn't have access. Flag as tooling gap when blocking; don't churn on workarounds.
- [2026-05-22] **Date-specific predictions at low confidence (≤40%) — date is the weakest link.** OTTO-26 (PSEC Feb 20 cut, 40% conf) falsified on date though directionally correct ($0.045→$0.035 cut DID happen, but May 7 Q3 FY26 not Feb 20). When making date-specific predictions on event-driven outcomes, either raise the resolve window or lower the date specificity — don't pin both tight when conf is <50%.
- [2026-05-22] **Forward-discovery prediction spirit vs literal reading.** When a prediction's literal text would be satisfied by pre-existing public data the agent didn't know about (Origin Bancorp Oct 23 2025 Tricolor disclosure for OTTO-30), default to forward-discovery spirit, not retroactive confirmation. Logged the data, kept prediction OPEN, dropped confidence.
- [2026-05-22] **General-purpose sub-agents may not auto-load WebSearch/WebFetch.** First Brands docket lookup returned no data because tools weren't loaded. When a sub-agent task requires web work, either confirm tooling presence in prompt or do the lookup in-session.
- [2026-05-22 PM] **Plaintiff-allegation-only signals should be weighted ≤40% confidence pending corporate-side or independent corroboration.** OTTO-31 (Wilmington full non-mortgage custodial exit) was opened 5/21 at 60% on a Jan 14 noteholder complaint allegation. 5/22 PM research surfaced a direct M&T-side denial (American Banker, anon source, on the record) + active-business counter-evidence (#2 ABS/MBS trustee 1H 2025; Outlook 2026 thought-leadership). Confidence dropped to 30%. Pattern: litigation rhetoric routinely over-claims the strategic implication of operational facts. Apply this prior at prediction-open time, not only on rework.
- [2026-05-22 PM] **Separate the narrow corporate-confirmed event from the broader litigation framing in STATUS active vectors.** When a plaintiff allegation includes both a real narrow fact (Wilmington Tricolor resignation Sep 20 2025) and an expansive broader claim (full non-mortgage custodial exit), structure the vector around the corroborated narrow fact and add the broader framing only when corporate-side evidence supports it. Saves later rework and avoids overweighting a single transmission row.

## Findings
- [2026-05-21] **Tricolor Vehicle Sales Deadline was Mar 31, NOT Apr 30** (corrects Apr 15 OTTO recalibration). No formal extension motion in public records. Auctions ran on the original schedule; proceeds data lagged into May.
- [2026-05-21] **Tricolor auction proceeds (~May 14):** 5,857 of ~9,500 vehicles sold for $39.5M net. ~32% of cost basis on sold fraction. Full-auction projection ~$64M / $2B+ debt = ~3.2% recovery from vehicles alone. Confirms <10¢ ABS market pricing.
- [2026-05-21] **Phantom Tricolor inventory: ~30,000 vehicles MISSING, up to $1.1B.** Distinct from the 29,000 double-pledged loans. Industrial-scale validation of Invisible Exit thesis. Vervent "Fresh Start" mod program to 30,000+ delinquent borrowers is the institutional concession this cohort can't be pursued.
- [2026-05-21] **Tricolor $113M distribution gridlock** — receivables held in escrow because Wilmington Trust + JPM + Fifth Third + bankruptcy trustee dispute ownership. Vervent BLOCKED from initial servicer report. NEW transmission mechanic: banks can't book losses cleanly even when substance is clear. Likely pushes Jun 17 distribution-plan ETA past OTTO-29's Sep 30 resolve date.
- [2026-05-21] **🔴🔴 Wilmington Trust reportedly exiting entire non-mortgage ABS custodial business** (billions of $ ABS; Tricolor alone = 7 trusts 2018-2025 / $1.8B+). Source: Jan 14 subordinated noteholder complaint (plaintiff allegation). Needs corporate-side confirmation. New prediction OTTO-31 created (60%, resolve 2026-12-31). Watch M&T parent earnings + ABS surveillance trustee-substitution filings.
- [2026-05-21] **Fifth Third Tricolor exposure precise at $178M** (was $170-200M range). Source: Banking Dive Mar 2.
- [2026-05-21] **Two parallel noteholder lawsuits** clarified as distinct: (1) Jan 14 vs Wilmington Trust + Vervent (post-default reserve-fund breach, "asleep at the wheel"); (2) Feb 27 vs JPM/Barclays/Fifth Third (concealed/misrepresented fraud despite 2022+2024 auditor warnings). 30 investors holding ~$270M total subordinated ABS.
- [2026-05-21] **ACV Capital subpoenaed** via Trustee Rule 2004 motion May 14. Affiliate of ACV Auctions ($19M Tricolor-linked loss Feb 23). Fraud surface expanding to auction-side counterparty.
- [2026-05-21] **Apr 24 Fifth Third supplemental motion exists** (per Octus May 8) but contents opaque from OTTO — Verita cert verification blocks direct fetch. Same day, separate filing: Trustee Rule 2004 motion against four Tricolor affiliates (Tricolor Financial, Tricolor Auto Receivables, TAG Asset Funding, Apoyo Financial) — likely tracking inter-entity transfers underlying the $113M dispute.
- [2026-04-15] **Tricolor borrower composition validates Invisible Exit:** 75% undocumented Hispanic immigrants, 68% no credit score, 50% no driver's license. (Now reinforced by 30K missing vehicles + Fresh Start program — see May 21 entries.)
- [2026-04-15] **Apr 3 CNBC "systematic fraud" was re-coverage of Dec 17 2025 indictment**, not new charges. No signal escalation. ✅ May 16 CNBC piece confirmed re-coverage (ML-OTTO-154).
- [2026-05-22] **PSEC cut $0.045 → $0.035 on May 7 2026** (Q3 FY26 earnings 8-K). Falsifies OTTO-26 on date but confirms direction. Run-rate distribution now ~$0.42/yr.
- [2026-05-22] **CVNA May 5 stockholder meeting — three reads:** (a) 5-for-1 split passed, eff May 7-8 — option strikes adjusted 5x, verify all old CVNA put quotes are split-adjusted before sizing. (b) Chairman/CEO separation defeated 96% against — Garcia governance entrenched, *thesis-confirming* on related-party concern. (c) Grant Thornton ratified — DISCONFIRMS the "GT resigns" red-line trigger; remove from active watchlist. Quorum 832.5M / 850.1M. No new short-seller activity Mar 15 – May 21.
- [2026-05-22] **NY Fed Q1 2026 HDC (May 12 release): total auto $1.685T (+1.08% QoQ, ATH); auto transition-to-90+ 2.97% (flat QoQ, +3bps YoY).** Aggregate consumer-level flow is FLAT — does NOT confirm acceleration narrative at the headline. ABS-level subprime stress (60+ at 32-yr high per Fitch) diverges from consumer-level flow. Divergence is structurally consistent with Invisible Exit (skip bypasses standard DQ chain). Refresh dashboard $1.66T → $1.685T.
- [2026-05-22] **Origin Bancorp (OBK) — previously-undiscovered Tricolor-exposed bank.** Disclosed Oct 23 2025 (Q3 2025 earnings clarification): $16.2M exec mortgages + $28.4M charge-off + $30.1M commitments = $74.7M total. OTTO never logged it. Sharpens named-banks list to 6 (JPM/5-3/BCS/Regions/MTB/OBK) but doesn't auto-confirm OTTO-30. Q1 2026 sweep otherwise clean — Truist explicitly disclaimed Tricolor (First Brands only).
- [2026-05-22] **Q1 2026 was first quarter major GSIBs disclosed aggregate NDFI exposure** (BAC, C, GS, JPM, MS, WFC). Aggregate-only, no Tricolor-specific names. Useful REGINALD baseline for bank-NDFI cross-tracking.
- [2026-06-02] **First Brands Ch.7 — mechanism ADVANCING (sweep resolved boot-flagged May 20/25/29).** 4 Evolution SPV debtors already converted to Ch.7 (Apr 9 Lopez order) — first concrete partial conversion. PMG single-debtor Ch.11 liquidating plan filed May 15 / DS May 18 (Global Settlement → Litigation Trust; all other debtors → Ch.7 post-effective). May 20 conditional-DS approval **DENIED** by Judge Lopez on creditor-rights + admin-insolvency grounds (= the UST's May 13 dismiss-or-convert basis — denial cuts TOWARD OTTO-32). May 25/29 superseded; plan-confirmation re-targeted **Jun 17 2026**; UST motion still contested. OTTO-32 held 85%. Transmission mechanic intact: admin expenses > estate value → recoveries toward zero regardless of asset quality. Sources: Law360 / CreditSights / Trucks-Parts-Service (Kroll docket still auth-gated; news cleared it).
- [2026-05-22 PM] **Wilmington Trust full non-mortgage custodial exit DENIED corporate-side.** American Banker (Feb 19-20 2026) reports M&T-side anonymous source on record denied the plaintiff allegation; said unit "is accepting new clients." M&T 10-Q says Wilmington will "vigorously defend itself." Active-business evidence: #2 US ABS/MBS trustee 1H 2025; Outlook 2026 thought-leadership; no non-Tricolor trustee-substitution filings; no rating-agency notes flagging substitutions. OTTO-31 confidence dropped 60% → 30%. Plaintiff allegation = litigation rhetoric not franchise exit.
- [2026-05-22 PM] **Wilmington Trust Tricolor-specific resignation IS corporate-confirmed (narrow).** 30-day notice given Sep 20 2025 to step down as indenture trustee on Tricolor ABS only. Successor-trustee role being shunned by other major trustees (Auto Finance News). KBRA Oct 2025 commentary on Tricolor servicing transition didn't extend to other Wilmington-administered deals. This is a real cockroach #1 mechanic and a structural signal (successor vacuum) — but narrow, not franchise-level.

## References
- [2026-04-15] Verita Global — Tricolor Ch.7 docket: https://veritaglobal.net/tricolor (WebFetch fails on cert verification; titles surface via WebSearch but contents blocked)
- [2026-04-15] Kroll — First Brands docket (primary source for hearing dates, adjournments)
- [2026-04-15] SEC EDGAR CIK 0001569650 = OZK (REGINALD scope)
- [2026-04-15] DOJ/SDNY — Judge Lewis J. Liman presides over Tricolor criminal case; trial Oct 19 2026
- [2026-05-21] Octus — paid source for ABS litigation coverage; referenced Fifth Third Apr 24 supplemental motion but didn't quote (paywalled to OTTO)
- [2026-05-21] Auto Finance News (autofinancenews.net) — primary press source for auction proceeds + missing vehicles; WebFetch hits 403 but search snippets reliable
- [2026-02-16] Prior cross-agent exposure map: `AGENTS/OTTO/archive/CROSS_AGENT_SIGNAL_REGINALD_APR15_draft_superseded.md`

## Session Notes

### CHANGES SINCE LAST SESSION (May 22 PM → Jun 2, 11-day gap)
- Will-directed boot/closeout **protocol redesign** (not domain work). Multi-phase, collaborative — Will drafted each phase, OTTO refined then applied. Closed with a domain task (First Brands sweep).
- 12+ commits by other agents during the gap; May 22 PM OTTO work reached origin via push-train (commit `1d2e4ace`).

### LAST SESSION (Jun 2 — boot/closeout protocol hardening + First Brands sweep)
- **CLAUDE.md → v2.1 (Phases 1-3b):**
  - P1 Startup Protocol: git-pull step 0 (+blocked-pull fallback); PREDICTIONS scan flags due-in-7d AND passed-but-OPEN; new calendar past-due-catch (unswept vs acknowledged-pending); report-last.
  - P2 Closing Protocol = write-back mirror of boot (read→write spine); catalyst-sweep BEFORE prediction-resolve (deliberate cross).
  - P3a stripped live-state: Current Thesis → framing only; Thresholds drop Current col + labeled single-metric-trigger vs STATUS composite (STATUS operative); Domain Scope drop $9.3B; Invalidation de-dated Carvana + retired spent GT-resigns trigger.
  - P3b graduated overlay → top-level `## Evidence & Hygiene Conventions` (tags `[CONF]/[PRESS]/[ALLEG]/[EST]`, `[STALE]` composes; Doc Ownership table, audit-finalized 19 rows).
- **Cross-doc audit → `STALE_PUNCHLIST.md`** (9 items, behavioral-impact ranked). TRADE.md = headline rot (Feb 16, pre-split CVNA prices, dead triggers); VX.tsv = 3rd home for thresholds. **NO content fixed — remediation DEFERRED.**
- **First Brands sweep** = the new past-due-catch's first live catch (resolved May 20/25/29 — see Finding 2026-06-02). STATUS timeline + signal-trigger + OTTO-32 + ML-171 updated. No WALTER signal (Will: let it ride).
- Git: `e9932373` (P1-3a) + `4caa2b36` (push-note fix) + this closeout commit — all local, push-deferred (push-train).

### NEXT SESSION

1. **P1: STALE_PUNCHLIST.md remediation** — content-refresh pass. Behavioral-risk items first: #1 TRADE.md (pre-split prices + dead triggers), #2 RESEARCH_STATUS.md (Feb-stale monitoring), #3 VX.tsv (3-way threshold dup). Items #8-9 (LESSONS/OUTBOX consolidation) need Will-decision before action.
2. **P1: Phase 4 — build `workbook/CATALYSTS.tsv`** on SAM's schema; backfill from CRITICAL TIMELINE; flip boot step 5 to read it as primary (the boot/closeout redesign's final phase).
3. **P1: OBK 10-Q Q1 2026** — Tricolor exposure quantum vs $74.7M (Oct 23) disclosure.
4. **P1: M&T Q2 earnings (Jul)** — Wilmington segment language (OTTO-31 hard-signal watch).
5. **P2: Jun 17** — First Brands plan-confirmation hearing (KEY OTTO-32) + Tricolor creditor mtg (same day); **Jun 12** Carvana discovery production 2.
6. **P2: re-run scripts** (`abs_issuance_tracker.py`, `extension_proxy.py` — data Apr-stale).
7. **P2: War-transmission row re-check** — Apr 1 Iran/oil/ABS row stale post-ceasefire.
8. **P3: WAL/Jefferies/Point Bonita $715M thread; Ally Q1 for OTTO-28; delete `otto-backup-pre-rebase-20260415` branch.**

### PENDING PUSH
- May 22 PM work already on origin (`1d2e4ace`; old `3d715270` SHA rewritten by rebases). No May deferral outstanding.
- Jun 2 work committed locally, **not yet pushed** (push-train — SAM ×2 + REGINALD also ahead): `e9932373` (P1-3a), `4caa2b36` (push-note fix), + this closeout commit (P3b + First Brands sweep + closeout writes).
