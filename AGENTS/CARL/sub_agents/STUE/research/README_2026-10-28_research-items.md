# STUE research items — 2026-10-28 (Will-directed, evening)

Five backlog items worked in one pass. Each entry: question → finding → source (primary unless marked) → what it changes. Source files in this directory are listed at the end with sha256.

## 1. OQ#14 leg (b) — Treasury vendor build-out: ⚠️ the 9/5 "validated null" was WRONG

**Question:** is Treasury building collection capacity for defaulted student loans?

**Finding (USAspending / FPDS, primary, pulled 2026-10-28 via `api.usaspending.gov/api/v2`):**

| Task order | Vendor | Signed | Obligated | Termination | Deobligated |
|---|---|---|---:|---|---|
| 2033H626F00085 | The CBE Group | 2026-05-19 | $8,000,000 | for convenience, effective **2026-06-03** | −$8,000,000 (6/04); options $15.76M cancelled |
| 2033H626F00086 | Coast Professional | 2026-05-21 | $8,000,000 | same | −$8,000,000 (6/04); options $15.76M cancelled |
| 2033H626F00087 | Continental Service Group (ConServe) | 2026-05-21 | $8,000,000 | same | −$8,000,000 (6/04); options $15.76M cancelled |
| 2033H626F00088 | Pioneer Credit Recovery | 2026-05-26 | $8,000,000 | same | −$7,975,472.05 (7/02); **$24,527.95 retained** |
| 2033H626F00089 | Transworld Systems | 2026-05-29 | $8,000,000 | same | −$8,000,000 (6/04) |

All five: description **"PRIVATE COLLECTION AGENCY (PCA) SERVICES - EDUCATION PILOT"**, awarding/funding = Treasury / **Bureau of the Fiscal Service**, PSC "Support-Management: Debt Collection", period of performance 2026-06-01 → 06-03. Parent BPAs **2033H625A00007–00011** (one per vendor). ⇒ **A ~$40M obligated (~$119M with options) Education PCA pilot was stood up May 19–29 and terminated for convenience on June 3 2026, before it ran.** Why: not stated in any record read.

Context in the same pull: the same five firms hold **general** Fiscal Service PCA task orders, **$12M each, 2026-01-05 → 2027-01-04** (e.g. 2033H626F00033 Pioneer, outlays $4.77M), which succeeded the 2025-05-18 → 2026-08-17 **bridge** orders. ⚠️ **So STUE's 9/5 line "latest PCA capacity action is a 2025-05-18 bridge contract — a stopgap" was also wrong:** a successor BPA with task orders from Jan 2026 existed. Those general orders are **all-agency Cross-Servicing**, not student-loan-specific evidence.

**Why the 9/5 null missed it:** the query terms were "default resolution" and "student"; the award text says "EDUCATION PILOT". A scan keyed on naming read the agency's own wording as absence. The controls fired, so the null looked validated. **Lesson: a fired control proves the endpoint works, not that the target vocabulary was covered.**

**What it changes:** the press reports of "private collectors possibly from November" now have a concrete precedent; **a re-award would appear as new task orders under parent BPAs 2033H625A00007–11.** That is the instrument to poll. **Still no evidence of custody transfer or of involuntary collections restarting.**

## 2. OQ#19 — which SAVE notice-completion date is right: ✅ RESOLVED (servicer-specific; the "Aug 15" was Edfinancial's window generalised)

| Servicer | Notice window | Source |
|---|---|---|
| Edfinancial | Jul 1 – Aug 15 2026 | Edfinancial page, primary (CARL KB-CARL-501, read 10/01) |
| **MOHELA** | **"between July and September 2026"** — ⚠️ **revised from the Jul–Oct STUE carried** | MOHELA SAVE FAQ, **primary, read 2026-10-28**: *"These notifications were sent between July and September 2026. If you have not yet selected a new repayment plan, you will receive a final notice reminding you to do so."* |
| Nelnet | originally Jul 2026 – Mar 2027; revised to "by end of 2026" | **secondary** (College Investor; Traders Union); Nelnet page 403 to curl and empty to WebFetch |
| Aidvantage, CRI | not found | — |

**Final notice:** existence confirmed at **primary** (MOHELA FAQ). The **30-day** length is **secondary** (College Investor 10/15, Forbes 10/16, Newsweek). ⇒ Full-population last auto-enrolments ≈ last notice (Nelnet, ~Dec 31) + 90 + ~30 days ≈ **end-Apr 2027**. The Aug-15 claim is not wrong; it is one servicer's window presented as everyone's.

**What it changes for ES-02 / CRL-28:** MOHELA's notices **finished by Sep 30, not Oct 31.** Its 90-day windows therefore close **by ~Dec 29 2026**, and its first auto-enrolments started **~Sep 29 (+ ~30 days final notice ⇒ ~Oct 29)**. The window in which a MOHELA servicing failure should show in complaints is **Oct 2026 – Jan 2027**, not "after Oct 31". DOCKET L154 ("MOHELA waves complete 10/31") rests on the superseded FAQ text.

## 3. OQ#12 — the −87 to −171 score-drop band: ✅ SOURCED at primary, and a post-on-ramp update EXISTS

- **Source:** Liberty Street Economics, **"Credit Score Impacts from Past Due Student Loan Payments,"** Daniel Mangrum and Crystal Wang, **Mar 26 2025**. Table by score band in the quarter before the delinquency: **<620 −87 · 620–659 −143 · 660–719 −165 · 720–759 −165 · 760+ −171.** Method: average change the quarter after a borrower's **first** new 90+ DPD report, **2016:Q1–2019:Q4 episodes**, Equifax Risk Score 3.0. ⇒ **It is a pre-pandemic, band-by-prior-score estimate, not an uncertainty range.** Quoting "−171" bare means "superprime borrowers, historical."
- **Post-on-ramp update:** Liberty Street, **"Student Loan Delinquencies Are Back, and Credit Scores Take a Tumble,"** Haughwout, Lee, Mangrum, Scally, van der Klaauw, **May 13 2025.** Observed **2024:Q4 → 2025:Q1**, borrowers current at Q4 and 90+ at Q1: **<620: 3.2M (56.6%), −74 · 620–719: 2.0M (35.9%), −140 · >720: 0.4M (7.5%), −177.** Count-weighted average ≈ **−105** (STUE arithmetic; defaulted-not-yet-reported borrowers are in counts but not in the averages). ">2.2M saw drops >100 points; >1M saw drops ≥150."
- **What it changes:** the SCORE-DROP RECONCILIATION gains a seventh figure (**−105**, Equifax 3.0, Q1 2025 new-90+ cohort). **−62 (FICO, H2 2025) remains the default**: different score model, later and broader cohort.

## 4. OQ#10 — TCF / Protect Borrowers study: harvested (release text; the report page 403s)

Source: Protect Borrowers release for *Trump's Student Loan Delinquency Crisis, Unmasked* (Granville and Zhang, TCF + PB, Feb 20 2026), credit-panel data for **the first three quarters of 2025**. **Advocacy co-author; figures below are the authors' own, not independently checked.**
- Delinquency **25%** of borrowers vs **9.2%** in 2019; **~7.9M** entered delinquency in Q1–Q3 2025; avg delinquent balance **~$34,000**.
- **~9M** in default; of 2025 delinquency→default movers, **three-quarters had never defaulted before.**
- Score: **−57 points** on average for delinquent borrowers (Q1–Q3 2025); three-quarters pushed into "deep subprime"; **2M** near-prime-or-better borrowers fell **680 → 580** on average (−100).
- Demographics: Black and Native borrowers' delinquency **near 50%**; Pell **27%** vs non-Pell **15%**; Louisiana **40%**, Mississippi **39%**.
- Admin: **328,000** IDR applications mass-rejected Aug 2025; **734,000** unprocessed as of December.
- Projection: SAVE's end "could bring the total number of borrowers **in distress** to **17 million or higher**."
- ⚠️ **Attribution defect found:** STUE's STATUS credits this study with the **"13M in default by EOY 2026"** projection. **The release does not contain 13M**; its projection is **17M "in distress"** (delinquent + default), a different quantity. The full report (tcf.org, 403 to curl) was not read, so the 13M may sit there. **Until it is found in a source, treat 13M as UNVERIFIED.**

## 5. OQ#13 — AFT Amended Complaint (Doc 50, filed 2026-01-15, 56 pp): read at primary

| STUE-carried figure | In the pleading? | What it actually says |
|---|---|---|
| **280K overcharged** | ✅ yes (¶4) | Oct 2023: "MOHELA used the wrong federal guidelines to calculate payments, causing **280,000** borrowers to make excessive payments." |
| **2.5M missed bills → 800K DQ** | ✅ yes (¶4, ¶120) | ED, **Oct 30 2023**: failed "to send billing statements on time to 2.5 million borrowers" and "**over 800,000** borrowers were delinquent." ⚠️ **STATUS labels this "2025 cumulative." It is an Oct-2023 figure.** |
| **~7× / >50× wait-time ratio** | ❌ **NOT in the pleading** | The complaint cites ED's Q4-2024 Loan Servicer Performance only qualitatively ("considerably worse") plus one borrower anecdote (144 / 149 / 50 minutes). SERVICER.tsv sources the ratio to the CFPB Ombudsman; **the "AFT complaint via PB/NCLC" attribution in `CLAUDE.md` is wrong.** |
| **Call deflection** | ✅ yes (¶¶161–164) | "'Call deflection' is the practice of diverting callers to MOHELA's website, ED's website, or other self-service features." |

**Docket bonus:** **Doc 54 (Jul 17 2026) is FREE on the Internet Archive** (`gov.uscourts.dcd.272123`); STUE had it as PACER-only. It asks to continue the stay **60 days** and sets a **joint status report due Sep 15 2026**. **That report is not in the free archive, and the CourtListener docket page still 404s** ⇒ the case's status after 9/15 is an **access gap**, not "quiet".

## Source files (this directory)

| File | sha256 |
|---|---|
| `AFTvMOHELA_Doc50_AmendedComplaint_2026-01-15.pdf` (archive.org `gov.uscourts.dcd.272123.50.0.pdf`) | `dd912ff7a6f335723d784f081fd2aa4a1a04544d9151ee844a09009a9f788049` |
| `AFTvMOHELA_Doc54_JointStatusReport_2026-07-17.pdf` (`…272123.54.0.pdf`) | `ac9bfc06734bac89472a7796f8da3fa71cbc88bab5b565c96a46d656a76b2bf4` |
| `USAspending_Treasury_PCA_awards_pulled-2026-10-28.json` | `3146b565a6e859245999ac88de4ab33120d0692a8f5447a2193e34f14282fe04` |

Web primaries read but not stored: MOHELA SAVE FAQ (`mohela.studentaid.gov/DL/resourceCenter/SAVEPlanFaq.aspx`), Liberty Street Mar 26 2025 and May 13 2025 posts, Protect Borrowers release (Feb 2026).
