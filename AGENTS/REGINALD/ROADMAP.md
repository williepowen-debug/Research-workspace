# REGINALD ROADMAP — "Where are we"
**Updated:** 2026-05-01 PM (created — Wave 1 closed; seeded with this session + carried-over threads) | **Status:** ACTIVE

Persistent state-of-REGINALD tracker across sessions. **SCRATCH** = loose notes, intra-day workspace. **MEMORY.md Session Notes** = session-bridge handoff (what just happened, what's next). **STATUS** = live dashboard. **ROADMAP** = what threads are open, what data we're waiting on, what questions are unresolved, what we want to investigate next, what just got done.

**Maintenance discipline:** Updated at session end before commit. If a thread is moved to RESOLVED, that's the audit trail of what each session shipped. Pruned aggressively — promote to thesis/KB/research or delete; do not just accumulate.

---

## OPEN THREADS
*Active work spanning multiple sessions. Each entry: what / status / next step / last-touched.*

| Thread | Status | Next Step | Last Touched |
|--------|--------|-----------|--------------|
| **Other LAM/Leucadia-era credits in WAL book** (V2 PRIMARY post-print) | Mgmt lockdown Apr 21: "no further commentary while matter is ongoing." Latent inventory unknown — LAM operates multi-strategy funds; disclosed credit was singular fund. KB-WAL-086 captures the unknown. | (a) 10-Q Table 16 read May 4-10 for Jefferies-platform credit names, (b) WAL Investor Day May 12 — analyst Q&A pressure on Leucadia inventory | 2026-05-01 |
| **Cantor residual recovery tracking** | ~$70M residual on book post-Q1 charge. Recovery via $13M senior liens + UHNW springing guarantees + mortgage fraud policy. Mgmt: "complex and potentially of long duration." | Quarterly monitoring of incremental specific reserve build above ~$70M residual = recovery posture deteriorated; full $70M write = bear case | 2026-05-01 |
| **Q1 10-Q deep drill (3 banks filed)** | CFG May 4, VLY May 7, EGBN May 7 — initial scan May 8 (`research/Q1_10Q_SWEEP_2026-05-08.md`). WAL + OZK still not filed. | (1) EGBN HFS transfer $ quantification — watchlist score depends on it; (2) VLY NCO + ACL coverage trajectory — verify "mask" thesis; (3) CFG $1.5B NDFI reconciliation gap; (4) Cross-bank Office classified $ comparison; (5) WAL 10-Q recheck May 11-13. | 2026-05-08 |
| **MI3 / RCON2746 — FFIEC bulk update wait** | Q1 10-Qs do NOT contain MI3 (FFIEC Call Report only). Bulk PDD update ~mid-May. | Recheck FFIEC PDD ~May 14-16. | 2026-05-08 |
| **WAL Investor Day prep** (May 12) | Forcing event for Q&A pressure on cross-credit inventory. T-3 from now (May 9). Outline not yet built. | Build 1-page "what would change the thesis" outline before May 11. Track analyst Q's on the day. Forcing-function: Leucadia inventory pressure + Office de-risk story. | 2026-05-08 |
| **APO Q1 post-print integration** (printed May 6) | Print 3 days old; not yet integrated. WAL V3 warehouse-counterparty link via Atlas SP $6.9B at PFSI = 78% concentration. | Read transcript/release: Atlas SP segment, warehouse book size, non-bank servicer counterparty commentary, MFS/First Brands/Tricolor overhang. Cross-link to KB-WAL rows on warehouse exposure. | 2026-05-08 |
| **🔴 May 15 expiry cluster — execution week** | Decision memo `MAY15_DECISIONS.md` done 2026-05-08. WAL $75P → let expire (don't roll). SSB $95P → hold and watch (cannot sell at $0 bid). Pre-registered triggers documented. | Mon-Fri execution per triggers. Watch WAL for -3% catalyst (sell-to-close window) and SSB for <$95 break (ITM trigger). Default: no action; let market decide. | 2026-05-08 |
| **🔴 RED counter on WAL v2.0 — inbox signal not yet processed** | RED filed 2026-05-06 at `inbox/SIG-RED-REGINALD-20260506-wal-v20-overcorrected.md` — 9.5KB content, 2 days unread. Challenges THESIS v2.0 ("compounder with concentrated CRE tail risk") shipped May 1. RED's mandate: present strongest bull case as steel-man. | Read the signal carefully. Evaluate counter-arguments. Either (a) revise THESIS v2.0 if RED's case has merit (CHANGELOG entry; possibly v2.1 or v3.0 framing); (b) write outbox response defending v2.0 with explicit address of RED's points; (c) hybrid — partial revision + partial defense. **High priority — fresh thesis under direct challenge.** | NEW (surfaced 2026-05-08; not yet processed) |
| **🟠 CARL handover signal — inbox not yet processed** | CARL filed 2026-05-02 at `inbox/SIG-CARL-REGINALD-20260502-misplaced-banking-rows-handover.md` — 5.8KB content, 6 days unread. Topic: misplaced banking rows handover. | Read the signal. Determine: (a) what banking-domain rows are being handed over, (b) integrate into KB.tsv if applicable, (c) reply via outbox if needed. Lower priority than RED counter but still pending. | NEW (not yet processed) |
| **MTB Baltimore Sun primary verification** (SIG-W-20260426-009) | -$1B / 29% reassessed CRE per Will signal Apr 26. Primary source verification required before trade-thesis weight. | Quick Sun article pull + MTB BAL CRE % calc + watchlist score update if confirmed | 2026-04-26 |
| **Wave 2 cross-agent outbox signals** | Wave 1 fully closed → Wave 2 unblocked. Targets: BROCK / CARL / OTTO / PROME / LIQUID / HAWK. Now expanded with 10-Q sweep findings (5/8). | Compose signals: (1) WAL V2 resolution → BROCK; (2) LAM rail → BROCK; (3) sector silence → OTTO; (4) Office single-point → PROME; (5) Apollo Atlas linkage → LIQUID; (6) **NEW:** EGBN "high-risk office" primary-source admission → BROCK + PROME; (7) **NEW:** VLY provision -66% YoY → CARL (cohort fade pattern); (8) **NEW:** CFG capital call $8.76B + secured PC finance $4.10B trajectory → BROCK. | 2026-05-08 |
| **✅ WALTER ↔ REGINALD LIAISON — Turn 5 CLOSE-CONVERGED** | Turns 1-5 in <13 hr UTC. All 8 Qs LOCKED both sides; 5 instantiated files end-to-end (REGINALD: THRESHOLDS.tsv + BOARD_LOG.tsv 32-row stub + CLAUDE.md Boot 9b + JOINT_PROPOSAL §1+§3; WALTER: CROSS_REFS/REGINALD.md v0.1 + REG_THRESHOLDS_FIRED_LOG + ROUTING_TABLE v0.9 By Convergence + spawn-protocol 6b). `bank_transmission` enum 8-val pre-cosigned for V0_9_STACK alongside BRENT enums. Channel state: POST-WRAP CALIBRATION-PENDING. | **Calibration cycle 1 trigger:** 2026-05-25 (14d) OR N=15 forward BOARD dispositions, synced w/ BRENT. **Open externalities (not LIAISON-blockers):** (a) CARL DATA_RELEASE_CALENDAR.md pattern landing ~May 17-20 → REGINALD CALENDAR_DATA.tsv ~7d later; (b) BOARD_LOG full disposition pass on 16 missed-action signals = separate REGINALD-session task; (c) Will-stitch JOINT_PROPOSAL at repo root `design/JOINT_PROPOSAL_2026-05-11.md`; (d) FORMAT_SPEC v0.9 batched ship adds `bank_transmission` enum. Move to **RECENTLY RESOLVED** at next session-end audit. | UPDATED 2026-05-11 — CONVERGED |

---

## AWAITING DATA
*Known external prints with dates. Order = chronological.*

| Date | Item | Test / Implication |
|------|------|-------------------|
| **~Mid-May** | **MI3 / FFIEC PDD bulk update** (Q1 Call Reports) | MI3 / RCON2746 trajectory for WAL (V1 acceleration test ≥25%), OZK (37.6% baseline), EGBN (23.7% baseline post strategic-de-risk). 10-Qs do NOT contain MI3 — wait for PDD bulk. |
| **May 11-13** (est) | **WAL + OZK 10-Qs** (SEC EDGAR) | WAL: highest-impact for V2.0 thesis — Office Slide 12/23 Q1 numbers in 10-Q form, Schedule O / Table 16 large credits (Jefferies-platform names?), Cantor residual disclosure, Apollo Atlas SP counterparty. OZK: RESG classified detail, specific reserves on 11 problem credits. |
| **May 4-10 ✅ partial** | ~~10-Qs (SEC EDGAR) for WAL/OZK/EGBN/VLY/CFG~~ | CFG May 4, VLY May 7, EGBN May 7 ✅ scanned May 8. WAL + OZK pending. |
| ~~May 6~~ ✅ printed | ~~APO Q1 (pre-market 8:30 ET)~~ — moved to OPEN THREAD `APO Q1 post-print integration` | — |
| ~~May 6~~ ⏸ data not yet integrated | BLS state jobs March (LABOR primary; REGINALD = FL signal CARL/CORAL) | LABOR/CARL own integration; check for cross-domain signals next session |
| ~~May 8~~ ⏸ data not yet integrated | BLS Apr NFP (LABOR/CARL primary) | LABOR/CARL primary; check claims for >300K trigger violation next session |
| **May 12** | **WAL Investor Day** | Mgmt response to thesis vectors; possible Leucadia inventory Q&A pressure; Office de-risking story |
| **~Mid-May** | FDIC Quarterly Banking Profile Q1 | Aggregate CRE DQ, NDFI growth, provision trends |
| **~Mid-May** | FFIEC PDD Q1 bulk update | MI3 ratios bulk-queryable |
| **May 21** | Epstein class action deadline (APO) | PC sector headline risk |
| **TBD May** | ROAD to Housing Act House vote | Sec 901 survival post-76-lawmaker bipartisan letter Apr 22 |
| **Jun 1** | FL property reinsurance renewals | FL property insurance pricing, carrier exits — CORAL primary |
| **Jun 18** | AOCI capital rewrite comment period closes | Final rule direction; Cat III/IV impact $49.5B aggregate |
| **Jun 18** | Options expiry cluster | WAL $85P/$65P, SSB $90P, KRE multi, IWM $250P, HYG $75P — position management decisions ~Jun 11 |
| **~Late Jul** | WAL Q2 print | NCO ex-fraud test (REG-25); Office classified migration test (REG-24); leading-bucket trend |
| **Aug 2026** | IQHQ loan maturity (OZK) | Sponsor support test (OZK primary) |
| **Oct 1 2026** | OZK $350M sub notes reprice (2.75%→SOFR+209) | Tier 2 capital -20% (OZK primary) |
| **Oct 2026** | Affinius Capital $2.7B bond maturity | OZK link — NOT mentioned on Q1 call |

---

## OPEN QUESTIONS
*Flagged but not actively worked. Decide before next acting on them.*

| Question | Surfaced | Action Owed |
|----------|----------|-------------|
| **WAL pre-existing column-drift in KB.tsv** (rows 056/057 have 14 cols not 13) | 2026-05-01 | Low priority. Find stray tab, normalize to 13 cols. Out of scope this session — fix on next workbook hygiene pass. |
| **HERMES revival vs alternative messaging** | 2026-04 ongoing | Defer per messaging-overhaul direction (don't patch); REGINALD outbox is currently undelivered (per WALTER GAPS) |
| **BROCK status — top-level peer vs sub-agent** | 2026-04 | SUB_AGENTS.md still lists BROCK; CLAUDE.md says BROCK is top-level peer. Sync. Low priority. |
| **"Sector silence" reliability** | 2026-05-01 | When does silence (RITM Apr 28, WAL Apr 21 on First Brands/Tricolor) mean immateriality vs hidden? Develop heuristic via Q2 print pattern. |
| **REGINALD MEMORY.md vs SCRATCH.md naming** | 2026-05-01 | Other agents use SCRATCH.md for what REGINALD calls MEMORY Session Notes. Possible harmonization later. |

---

## INVESTIGATIONS BACKLOG
*Research / deep-dive ideas not yet started. Each: what / why / scope. Pull from here when there's a research session and no urgent catalyst.*

| Topic | Why interesting | Scope |
|-------|-----------------|-------|
| **Apollo Atlas SP warehouse counterparty mapping** | $7.155B WAL warehouse exposure + Atlas SP $6.9B PFSI 78% concentration = transmission landing point analysis. APO May 6 print may surface. WAL/CFG/MTB/etc. exposure to Atlas SP needs explicit mapping. | Medium (1 session, possibly cross-agent with BROCK) |
| **Cantor mortgage-fraud-policy precedent** | WAL Cantor recovery cited mortgage fraud insurance policy. Industry precedent? Other banks reaching for same? Insurance industry exposure to bank-loan-fraud claims at scale? | Quick-Medium |
| **First Brands transmission landing at peer banks** | Jefferies took $17M Q1; WAL silent in Q1 — where else did the loss land? PE/credit fund chain analysis (BROCK has primary). | Medium (cross-agent) |
| **Sector silence pattern as data — meta-thesis on disclosure quality** | WAL Apr 21 + RITM Apr 28 both went silent on broader sector stress. Reliability of "silence = no material exposure" needs Q2 print confirmation. Develop disclosure-quality scoring framework. | Medium |
| **Cohort fade pattern continuation** | 12/12 in Q1. Does Q2 break the model? If yes, why; if no, when does this become consensus? | Light tracking; Q2 print monitoring (~late Jul) |
| **Hidden CRE methodology v2** | If banks migrate classification again post-MI3 (mark-to-model, off-balance-sheet), need new screening method. Track Q1/Q2 RC-C composition shifts beyond Memo Item 3. | Medium |
| **DEF 14A pass (~90pp WAL proxy)** | Audit fees YoY (RSM hours up?), governance signals, audit committee composition, RSM 32-yr tenure | One session post-Wave 2 |
| **Cross-bank Hidden CRE comparison v2** | Update Mar 25 baseline screen (WAL 24.2%, OZK 37.6%, EGBN 23.7%) with Q1 26 Call Report data once available; identify new outliers | Quick (post-PDD release ~mid-May) |
| **Office maturity wall — bank-by-bank quantification** | WAL $946M known; need similar for OZK/CFG/SSB/EGBN. Bridge structure exposure mapped against 2026 maturity calendar. | Medium |
| **Convergence Day pricing decay analysis** | Feb 27 -10.64% / Mar 2 -10.82% events on zero firm-specific news. Has the "vulnerability premium" decayed? Re-pricing odds for next event? | Quick (chart + Greek analysis) |
| **WAL leading-bucket rate-of-build forecast** | 30-89d PD +45% QoQ; Special Mention +24% QoQ. Historical bank patterns: how often does leading-bucket buildup translate to lagging deterioration in 1-2 quarters? | Medium |
| **MTB Baltimore CRE expansion** | If SIG-026-009 verifies (Sun primary), MTB joins active watchlist. Build MTB exposure file. | Quick once verified |

---

## RECENTLY RESOLVED
*Last ~2 weeks. Top of mind so the audit trail is visible without reading commits.*

| Date | What | Result |
|------|------|--------|
| **2026-05-08 PM** | **Q1 10-Q sweep — 3 of 5 watchlist banks filed (CFG / VLY / EGBN)** | Initial scan delivered findings file `research/Q1_10Q_SWEEP_2026-05-08.md`. Headline reads: (1) **CFG** NDFI breaks out at $18.12B (Capital call $8.76B + Secured PC $4.10B + Other $5.27B) — $1.5B gap to Slide 24 prelim $19.6B; "Other finance/insurance" +13.7% QoQ highest-growth line; (2) **VLY** provision **−66% YoY** = "provisions mask deterioration" thesis gaining ground; (3) **EGBN** 🔴 strategic de-risk + "high-risk loans concentrated in CRE office segment" CONFIRMED in primary filing text; HFS transfer mechanism cited — V1 Hidden CRE thesis getting direct primary-source validation. WAL + OZK 10-Qs still pending (likely May 11-13 for WAL). MI3/RCON2746 awaiting FFIEC PDD ~mid-May. |
| **2026-05-08 PM** | **MAY15_DECISIONS.md memo created** | WAL $75P May 15 → LET EXPIRE (don't roll; Sep $67.5P/$70P already plays Q2-print thesis better). SSB $95P May 15 → HOLD AND WATCH (cannot sell at $0 bid; pin-risk play; outcome determined by underlying). Pre-registered triggers documented for both. |
| **2026-05-08** | **POSITIONS.md broker refresh** | Apr 2 → May 8, 5 weeks of activity caught up. New names FITB ($45P Jun-18) + HBAN ($16P Oct-16) added. Real May 15 cluster surfaced (was hidden by KRE $70P phantom). Quantity column dropped (broker list was strike/expiry only — points to FORGE for qty). Scope held thesis-pure. |
| **2026-05-08** | **"KRE $70P May 15" stale-tracking caught + REGINALD scope cleaned** | Will confirmed at broker: position does not exist. Memory journals (`memory/2026-02-11.md`, `2026-02-12.md`) show position WAS real in early Feb (P/L tracked +26%); closed/exited between Feb 12 and Apr 2 broker screenshot, **never propagated to dependent docs**. REGINALD-scope cleanup (CALENDAR / ROADMAP×2 / MEMORY×2 / VLY brief) done. **Out-of-scope still affected:** AGENTS/RED (5 files — STATUS, CALENDAR, TIMELINE, 2 challenges) actively using May 12 T-3 close trigger; AGENTS/TRADES/JUNE_2026_CANDIDATES.md. RED's invalidation framework references a position that doesn't exist — flagged to Will. Lesson: closing a position requires a propagation step to dependent agents (RED especially), not just a POSITIONS.md update. |
| **2026-05-08** | **REG-20 RESOLVED → CONFIRMED-PARTIAL** | Will called by literal-text reading. Q1 print Apr 21 delivered earnings-miss trigger (1 of 3 OR-conditions; GAAP -4.6% + $152.5M fraud + V2 confirmed in 8-K). PARTIAL credit notation on row to keep calibration honest (modest tape reaction; no capital raise; no regulatory action). PREDICTIONS.tsv + STATUS.md updated. |
| **2026-05-08** | **Synthesis-files gitignore RESOLVED → Option A negation rule** | Will picked negation `!AGENTS/REGINALD/*/sources/q[1-4]_*/*.md` below line 38. One-time fix; auto-applies to all future quarter dirs. Unblocks 4 .md files in `WAL/sources/q1_2026/` (DROPZONE, transcript, 2 synthesis). `.gitignore` is shared-root file — Will to commit separately. |
| **2026-05-01 PM** | **Wave 1 chunks 3-6 closed** | FRAUD/STATUS + FRAUD/SYNTHESIS_V2 post-print rewrite (V2 RESOLVED public; Leucadia inventory primary open thread); KB.tsv 80→105 rows (Q1 print evidence 081-105); KB_INDEX 16 groups (added LEADING_CREDIT) + post-Apr 21 quick-reference + REG-20/24/25 prediction-to-row mapping; SCENARIOS re-weighted Bear 45→30 / Base 30→38 / Bull 20→25 / Tail 5→7 (EV $57→$72.32, current $81.22 → 11% over); INDEX refresh (Q4 25→Q1 26 numbers, KB count, file map). 597 insertions / 385 deletions across 8 files. Pushed `551d8c9b`. |
| **2026-05-01 PM** | **Q1 Call Report sweep** | Confirmed cert/RSSD/CIK for all 5 watchlist banks (now in MEMORY References). FDIC SDI: all banks' most recent REPDTE = 20251231 (Q4 2025); SDI lags 30-60d; risview index Feb 18 2026. SEC EDGAR: no Q1 10-Q filed for any of WAL/OZK/EGBN/VLY/CFG (most recent Nov 7, 2025). FFIEC CDR public ManageFacsimiles is ASP.NET viewstate-locked. Background: Nelnet Bank filed Q1 2026 Call Report Apr 29 — window IS open at FFIEC, just not query-friendly. |
| **2026-05-01 AM** | **WAL THESIS v1.0→v2.0 release** | "Compounder With Concentrated CRE Tail Risk" framing (was "fast-transmission failure"). V1 STRENGTHENED (Office single-point Slide 12 + $946M maturity wall Slide 23). V2 RESOLVED in public 8-K ($152.5M LAM+Cantor). V3 directionally DISCONFIRMED at aggregate (Slide 24 cohort median). PT $47-60→$55-70. New predictions REG-24 (Office classified >$500M Q3, 60%) + REG-25 (ex-fraud NCO >40bps Q2/Q3, 55%). |
| **2026-05-01 AM** | **WAL/CHANGELOG.md created** + master `thesis/CHANGELOG.md` entry | First entry pins v1.0 baseline + documents v2.0 transition. |
| **2026-05-01 AM** | **WAL/STATUS.md refresh** Apr 2→May 1 | Header 🔴🔴 HIGH CONVICTION SHORT → 🟠 SHORT THESIS ACTIVE. Q1 print snapshot table; V1/V2/V3 compact sections; mgmt outlook tensions; live price; positions pointer. |
| **2026-04-30** | OWL Q1 print (BROCK primary) | REGINALD info-pickup deferred to BROCK ownership |
| **2026-04-29** | 5-day catch-up integration (Apr 23 cohort + RITM Apr 28 + BOJ Apr 28) | Cohort fade 12/12 confirmed. RITM transcript pull DONE — soft fail on "DQ will reverse Q1" mgmt claim. BOJ hold + 3 dissents → June hike pricing 74%. |
| **2026-04-24** | WAL Q1 Round 2 deep-mine | Slide 12/23/24 deck synthesis; Office single-point thesis identified; 3 synthesis files in `sources/q1_2026/`. |
| **2026-04-22** | WAL Q1 Round 1 analysis | `Q1_2026_ANALYSIS.md` from 8-K + press release; V2 fraud confirmed in print; LAM = Leucadia Asset Management identified. |
| **2026-04-21** | **WAL Q1 print** | $152.5M fraud charge ($126.4M LAM + $26.1M Cantor); GAAP $1.65 miss / Adj $2.22 beat; tape -2%; mgmt "two fraud-related credits" + "largely behind us." |

---

*Companion files: `MEMORY.md` (curated cross-session memory + session-bridge handoff) | `SCRATCH.md` (loose intra-day notes) | `STATUS.md` (live dashboard) | `CALENDAR.md` (forward dates) | `LESSONS.md` (verified mistake patterns)*
