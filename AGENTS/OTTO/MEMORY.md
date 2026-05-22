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
- [2026-05-22] **First Brands Ch.7 conversion IN MOTION — US Trustee driven.** Apr 28 PMG Ch.11 plan proposes 111 of 112 debtors → Ch.7 + PMG litigation trust. May 13 US Trustee Epstein filed dismiss-or-convert motion attacking the Global Settlement as "sleight of hand"; cited $245M advisory fees paid + $223M unpaid admin (administratively insolvent) + no realistic reorg prospect. May 20 disclosure hearing held (outcome pending sweep). May 25 omnibus next. **NEW transmission mechanic: when admin expenses exceed estate value, recoveries fall toward zero regardless of underlying asset quality — UST is weaponizing this framing in First Brands.** OTTO-32 prediction opened at 85%.

## References
- [2026-04-15] Verita Global — Tricolor Ch.7 docket: https://veritaglobal.net/tricolor (WebFetch fails on cert verification; titles surface via WebSearch but contents blocked)
- [2026-04-15] Kroll — First Brands docket (primary source for hearing dates, adjournments)
- [2026-04-15] SEC EDGAR CIK 0001569650 = OZK (REGINALD scope)
- [2026-04-15] DOJ/SDNY — Judge Lewis J. Liman presides over Tricolor criminal case; trial Oct 19 2026
- [2026-05-21] Octus — paid source for ABS litigation coverage; referenced Fifth Third Apr 24 supplemental motion but didn't quote (paywalled to OTTO)
- [2026-05-21] Auto Finance News (autofinancenews.net) — primary press source for auction proceeds + missing vehicles; WebFetch hits 403 but search snippets reliable
- [2026-02-16] Prior cross-agent exposure map: `AGENTS/OTTO/archive/CROSS_AGENT_SIGNAL_REGINALD_APR15_draft_superseded.md`

## Session Notes

### CHANGES SINCE LAST SESSION (May 21 evening → May 22, continuing arc)
- Same operational arc; re-spawned post-/clear.
- Inbox cleared (May 9 $1.68T + May 16 CNBC) → both logged as no-STATUS integrations.
- 5-agent parallel sweep on P0 backlog: PSEC, CVNA May 5, First Brands, NY Fed Q1 HDC, Q1 bank sweep.

### LAST SESSION (May 22 — Inbox + P0 backlog sweep + First Brands Ch.7 follow-up)
- Inbox processed: ML-OTTO-153 (May 9 $1.68T = no-substance integration); ML-OTTO-154 (May 16 CNBC = re-coverage confirmed). No outbound replies.
- 5-agent parallel sweep: 4/5 actionable, 1 tooling-gap (First Brands sub-agent had no WebFetch — retried in-session, see below)
- **PSEC OTTO-26 FALSIFIED on date** — cut May 7 not Feb 20 ($0.045→$0.035 confirmed)
- **CVNA May 5 vote:** split passed (5-for-1, eff May 7-8 — option strikes adjusted 5x); chairman separation FAILED 96%; GT ratified (disconfirms "GT resigns" trigger)
- **NY Fed Q1 2026 HDC (May 12):** $1.685T total auto (+1.08% QoQ, ATH); transition-to-90+ 2.97% flat — diverges from ABS-level subprime stress (consistent with Invisible Exit)
- **Origin Bancorp (OBK)** surfaces as previously-undiscovered Tricolor-exposed bank ($74.7M, Oct 23 2025) — sharpens named-banks to 6 but doesn't auto-confirm OTTO-30 (forward-discovery spirit)
- **First Brands Ch.7 retry (in-session WebFetch):** Apr 28 PMG plan + May 13 UST dismiss-or-convert motion + May 20 disclosure hearing + May 25 omnibus. Ch.7 trigger PENDING→IN MOTION. WALTER signal routed (REGINALD primary, BROCK + CARL + LIQUID info-cc). OTTO-32 opened at 85%.
- STATUS.md: new May 22 sweep section + dashboard refresh + 5 new timeline rows + First Brands Ch.7 IN MOTION subsection + OTTO-26/30/31 row updates + signal trigger update
- ML.tsv: 8 entries appended (155-162)
- PREDICTIONS.tsv: OTTO-26 FALSIFIED; OTTO-30 conf 65→45%; OTTO-32 NEW (First Brands Ch.7, 85%)
- WALTER signal drop: SIG-OTTO-WALTER-20260522-firstbrands-ch7-in-motion.md (REGINALD primary, BROCK + CARL + LIQUID info-cc) — untracked per protocol

### PRIOR SESSION (May 21 evening — Tricolor outcomes catch-up, STATUS rewrite, full closeout)
- Boot: read STATUS / LAST_COMPLETION / MEMORY / PREDICTIONS / daily memory log
- Research: Tricolor Apr 30 deadline question resolved (Mar 31 was operative; Apr 15 recalibration wrong)
- Research: Fifth Third Apr 24 supplemental motion opaque (Verita cert issue), but surfaced adjacent material (Wilmington exit, ACV subpoena, distribution gridlock, exposure precision)
- STATUS.md: new May 21 check-in section + 2 new active vectors + 4 new dashboard rows + thesis row enrichment + 64 net insertions
- ML.tsv: 8 entries appended (145-152)
- PREDICTIONS.tsv: OTTO-29 conf 75-80% + at-risk flag; OTTO-30 conf 60-65% + candidate list; OTTO-31 NEW (Wilmington exit)
- WALTER signal drop: SIG-OTTO-WALTER-20260521-tricolor-data-emerged-wilmington-exit.md (REGINALD primary, BROCK + CARL info-cc)
- Inbox NOT processed (separate-task convention per CLAUDE.md)

### NEXT SESSION

1. **P0: May 20 First Brands disclosure statement hearing outcome** + May 25 omnibus outcome — drives OTTO-32 resolution timeline
2. **P0: Wilmington Trust corporate-side confirmation** — M&T Q2 earnings, Wilmington press, ABS surveillance for trustee-substitution filings. OTTO-31 hinges on this.
3. **P1: OBK 10-Q Q1 2026** — verify Tricolor exposure quantum vs Oct 23 2025 disclosure ($74.7M)
4. **P1: Review remote-inherited Apr 15 scripts/TSVs** — `abs_issuance_tracker.py`, `extension_proxy.py`, `workbook/{ABS_ISSUANCE,EXTENSION_PROXY,CROSS_AGENT_LOG}.tsv`. Still black-boxes.
5. **P1: War-transmission row re-check** — Apr 1 STATUS Iran/oil/ABS row stale post-ceasefire (BRENT/HAWK scope, but OTTO ABS-spread read needs refresh)
6. **P2: WAL / Jefferies / Point Bonita $715M thread** (carryover from Apr 6 research inbox)
7. **P2: Ally Q1 print** for OTTO-28 Carvana-specific DQ/NCO break-out
8. **P3: Delete `otto-backup-pre-rebase-20260415` branch** (5+ weeks clean)
9. **Tooling gap to surface to Will/Prome:** Verita docket cert-verify blocks Tricolor doc fetches; sub-agents may not auto-load WebSearch/WebFetch — confirm in prompt or do lookups in-session.

### INFRASTRUCTURE NOTES
- War-transmission row in Apr 1 STATUS (Iran Day 32, oil >$100, gas $3.99) still stale — ceasefire dynamics in play (BRENT/HAWK scope). OTTO ABS-spreads-on-inflation reading needs refresh.
- Boot-pointer convention in STATUS.md refreshed for May 22.
- Sub-agent tooling: explicit web-tool requirement should be confirmed in prompt before delegating web research.

### PENDING PUSH
- May 21 closeout already in tree (commits `bc2b27e7` + `f233518f` upstream).
- This session's May 22 changes (STATUS / ML / PREDICTIONS / MEMORY) — not yet committed. Commit at end of arc per Will direction.
