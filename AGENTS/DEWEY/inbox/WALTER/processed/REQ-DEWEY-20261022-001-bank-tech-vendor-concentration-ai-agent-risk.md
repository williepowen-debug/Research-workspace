---
request_id: REQ-DEWEY-20261022-001
from: WALTER (Will-directed in the WALTER terminal, 2026-10-22 11:53 ET: "I think we should investigate ... I will spawn DEWEY and you will have to direct him what to research")
to: DEWEY
created: 2026-10-22T15:55:43Z
state: NEW
flag_trigger: T1 new-coverage-channel (bank operational/cyber concentration has no fleet owner) + T3 load-bearing-but-thin (Will's thesis rests on two news items)
originating_evidence: SIG-W-20261022-008 (Axios 10/22: JPM/BAC/C/MS restricting third-party AI agents in customer accounts; "rogue" claims anonymous, Morgan Stanley disputes) + Microsoft Threat Intelligence 10/21 (Storm-0940 used the agentic framework ARTEX to automate intrusions; attributed the ConnectWise multitenant supply-chain compromise to it)
clusters: BANK_COLLATERAL (secondary AI_INFRA_CAPEX)
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv row REQ-DEWEY-20261022-001
kill_condition: Moot as a forward study if a CONFIRMED multi-bank core-vendor or digital-banking-platform compromise occurs before the run starts; then stop and hand WALTER a live-event verify instead. At intake, re-verify that the Axios 10/22 report and the Microsoft Storm-0940 report have not been retracted or materially corrected.
deliver_by: no hard date; useful before the next regional-bank catalyst cluster (bank Q3 prints run through about 10/30)
---

# DEEP-RESEARCH REQUEST — US bank technology-vendor concentration and AI-agent/cyber risk

**Will's thesis, in his words (10/22):** regional banks "no doubt have lower tech and older software", so they look like an obvious target as AI agents start threatening banks. **WALTER's refinement, which this study should test:** the larger risk may not be each small bank being weak on its own. It may be that hundreds of banks rent the same few core and digital-banking systems, so one compromise can hit many at once.

**Decision question:** Is US regional and community bank technology concentrated enough in a few third-party vendors that one AI-accelerated compromise, or one failure of AI-agent access controls, could hit many banks at the same time? Which publicly traded regional banks sit on which vendors, and has such a correlated event ever moved deposits or bank stocks?

**Materiality gate:** (a) A cheap verify can't answer this. It needs vendor market-share data, bank-by-bank vendor attribution from scattered filings and conversion announcements, and an incident base rate assembled across many episodes. (b) The consequence: it tells REGINALD and GIBBS whether operational and cyber concentration is a real transmission channel for regional-bank stress, separate from credit. Will holds KRE puts opened 10/22 (trade construction is TERRY's; this study recommends no position).

## Scope (in bounds)

1. **Concentration map.** Market share of core banking processors (Fiserv, FIS, Jack Henry; also Temenos, Finastra, CSI and others) by bank COUNT and by ASSETS, split by tier: community (<$10B), regional ($10–100B), large (>$100B). Do the same for digital/online banking front-ends (e.g. Q2 Holdings, Alkami, Jack Henry Banno, NCR Voyix) and the data aggregators AI agents use (e.g. Plaid, MX, Finicity, Akoya). Name every source and its date; vendor 10-Ks, the regulators' significant-service-provider supervision program, interagency third-party risk guidance and industry surveys are candidates.
2. **Bank-to-vendor map** for the fleet's names and KRE's largest holdings: at minimum WAL, ZION, OZK, FLG, HBAN, VLY, SSB, EGBN, plus the top 15 KRE holdings by weight. Find each bank's disclosed core and digital-banking vendor where public (10-K risk factors, vendor customer announcements, conversion press releases). Mark each cell CONFIRMED (primary), REPORTED (secondary) or UNKNOWN. Do not infer.
3. **Correlated-incident base rate.** Find every documented event in which one vendor outage or breach hit many financial institutions at once. Known starting points to verify, not assume: the November 2023 ransomware at a credit-union service provider (Trellance/Ongoing Operations), MOVEit 2023, the 2024 Evolve Bank breach and its fintech partners, the July 2024 CrowdStrike outage, Finastra 2024, and any Fiserv, FIS or Jack Henry outages. For each: number of institutions affected, duration, customer and deposit impact, stock impact, regulatory action. Also count SEC Form 8-K Item 1.05 (material cybersecurity incident) filings by banks since the rule took effect in December 2023.
4. **The AI-agent access channel.** The Axios vector is customers giving AI agents their passwords. Banks without data-sharing APIs force agents to scrape screens with credentials. Establish whether smaller banks lag on API access, and the status of the CFPB Section 1033 open-banking rule and its phase-in by bank size. Collect regulator, FS-ISAC and industry statements on AI agents in accounts through 10/22/2026, plus who bears losses when a customer-authorized agent misbehaves (Regulation E; the reported JPMorgan CFO remark).
5. **Transmission to money.** Has any IT or cyber incident caused measurable deposit outflows or a lasting stock move at a bank, as opposed to a short dip? If so, what features did it have (duration, customer-facing, social-media speed)?
6. **Counter-evidence, required.** Evidence that vendor concentration REDUCES risk (vendor security budgets, regulator examinations of large service providers), that the largest banks are the primary targets, and that small banks' lower agent adoption limits their exposure.

## Out of bounds

Stock picks, position sizing, or grading REGINALD's or anyone's thesis. Cyber technique detail beyond what is needed to describe an incident's scope.

## Engine sizing (WALTER's suggestion; DEWEY decides)

Legs 1–3 are broad, multi-source and historical, which fits the full /deep-research harness. Leg 4 is a targeted regulatory read. Use scripts/ primary pulls wherever there is a spine (EDGAR for 8-K Item 1.05 and 10-K vendor disclosures).

## Deliverable

Tables over prose, every cell sourced and dated: (1) vendor market-share table by tier; (2) bank-to-vendor map with a confidence column; (3) incident base-rate table; (4) a regulatory timeline for AI-agent access and 1033; (5) counter-evidence; (6) explicit UNKNOWNs, especially where vendor attribution is not public.

**On return:** archive to AGENTS/DEWEY/output/, then hand back via a create-only handoff in AGENTS/WALTER/inbox/DEWEY/ naming REQ-DEWEY-20261022-001. WALTER routes it as a research-output signal: REGINALD action; GIBBS, VULCAN, OZK, WAL, FLG, LIQUID, RED, PROME and TERRY info.
