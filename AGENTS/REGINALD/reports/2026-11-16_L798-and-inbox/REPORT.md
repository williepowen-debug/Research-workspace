# REGINALD 2026-11-16: D:L798 vendor-guidance comment read, inbox drain, carried reserve-release count, REG-T-06 REVIEW

**Session:** reginald, Claude Code, Opus 5.5 (claude-opus-5-5), woken by PROME prome-6f under WQ-184. Started 10:09 ET (`date`). Desktop. Report written 10:19 ET onward.

## 0. Boot facts

| Item | Reading | Basis |
|---|---|---|
| Git | 3 commits ahead of origin at start; PROME's two dirty files (`PROME/state/ORCH_INFLIGHT.md`, `ORCH_LOG.tsv`) block a rebase pull, so **no pull**, worked on the checkout as it stood (root rule) | `git status` 10:09 ET |
| Vendor quotes, intraday, NOT settles | WAL $74.12, KRE $72.63, FLG $10.35, VLY $14.32, ^TNX 5.13, ^VIX 20.83 | `scripts/market.py` 10:09 ET |
| Settled closes | **NOT GRADED.** The Yahoo daily-history route fails (`TypeError: 'NoneType' object is not subscriptable`) for WAL, KRE and FLG; `settled_bars.py` refuses (exit 2 path), `vx_ladder_check.py` rc 1 DATA ERROR. REG-T-02 log stays at 50 rows through 11/10; 11/11, 11/12, 11/13 closes are owed | own runs 10:09–10:12 ET |
| HY OAS (FRED `BAMLH0A0HYM2`) | **323 [11/13]**, 320 [11/12], 330 [dated 11/11], no 11/10 row; 334 [11/09] | `fetch.py fred` 10:1x ET |
| CCC OAS | 1,316 [11/13], 1,314 [11/12], 1,330 [dated 11/11] | same |
| boot.py | rc 2: Insider Activity and 8-K Monitor FAILED (each ~110 s, SEC route); FLG ladder ALERT (state unchanged, RED since 10/7); corrections rc 1 (COR-20261111-25, receipted below); peer channels 0 new entries above my ACK | own run |

## 1. D:L798: interagency third-party (vendor) risk guidance, comment period

**What closes today.** The proposal (91 FR 58536, 9/15/2026; OCC, Fed, FDIC, NCUA) replaces the 2023 third-party guidance; the Fed's separate community-bank guide (91 FR 58438) closes the same day. regulations.gov lists `commentEndDate` 2026-11-17T04:59:59Z = **11:59 PM ET Mon 11/16**, so the file is not complete when this is written. [PRIMARY: regulations.gov API, documents OCC-2026-0793-0001, NCUA-2026-1684-0001, FDIC-2026-1750-0001, FRS-2026-4028-0001, FRS-2026-4027-0001, read 10:14 ET]

**What was posted at 10:15 ET:** 48 comments on OCC-2026-0793, 48 on NCUA-2026-1684 (many duplicates across the two). FDIC and Fed comments are posted on their own sites; **not read**. I read the bank-side and agency-relevant letters in full text (PDFs via downloads.regulations.gov):

| Letter | Who | What it says on core-vendor dependence or AI |
|---|---|---|
| OCC-0021 / NCUA-0018 (10/29) | ABA, BPI, CBA, ICBA | **Only a request for a 30-day extension.** No substance yet; the trade groups' full letters may land today or later |
| NCUA-0009 | Axos Bank | Quotes the agencies' own 9/11 Joint Statement: "market concentration limits negotiating power" and institutions "struggle to obtain diligence information, negotiate terms, or monitor effectively"; mid-size banks "routinely interact with core processors and cloud providers that have vastly greater market power". **No vendor named, no dependence figure** |
| OCC-0030 | Independent Bankers Association of Texas | "Community institutions often have little leverage when negotiating with large core service providers"; asks for a safe harbor, since banks spend "duplicative resources evaluating the same core platforms used by thousands of" banks. No vendor named |
| NCUA-0030 | New York Credit Union Association | "dependence on a small, highly concentrated set of core processing providers" |
| OCC-0008 | Truliant FCU | A core processor "presents a fundamentally different risk profile" |
| NCUA-0049 | Capital Bank and Trust | no hit on core, vendor names or AI |
| OCC-0026 | CCG Catalyst (consultant) | Proposes listing "concentration and switching costs that materially limit alternatives" and "technology approaching end of support" as higher-risk traits |
| NCUA-0035 | Microsoft | Asks that concentration risk not create "a presumption that each service must be deployed across multiple providers"; same-provider multi-region backup should count |
| OCC-0039 | Sultan Meghji (personal capacity) | **"The proposal never mentions [AI]"**, and the Fed's April 2026 model-risk guidance (SR 26-2, footnote 3) says "Generative AI and agentic AI models … are not within the scope of this guidance." So third-party agentic AI sits between two documents. He asks for one sentence putting it inside this guidance |

**Answer to the row's two questions, as of 10:15 ET 11/16:**
1. **Bank-side disclosure of core-vendor dependence:** none quantified. Every bank or bank-association letter describes the dependence qualitatively (little leverage, concentrated providers); **no letter names a vendor or gives a share of operations.** This matches DEWEY's 10/22 finding (only 4 of 22 banks have a primary-confirmed core vendor).
2. **Regulator statement on agentic-AI access:** **none in the proposal.** The only agency text on agentic AI I found is the SR 26-2 footnote 3 exclusion, quoted in a comment letter (SECONDARY quote of a Fed document; I did not open SR 26-2). Nothing published says how examiners treat customer-authorized AI agents reaching bank accounts.
3. **1033 rewrite (watch):** CFPB sent the reconsideration NPRM to OIRA 8/6/2026; I found nothing that publishes it as of October (SECONDARY: law-firm and trade sources; reginfo.gov not checked). Unpublished.

**So what for my book:** no consequence. The vendor channel stays a combination-watch theme (`bank-vendor-breaches`), not a scored channel. A final guidance that adds AI language or a core-provider safe harbor would be logged, not scored. GIBBS's leg is GIBBS's. **Not done:** the complete comment file. The read after the close (and after the trade groups' substantive letters post) is still owed; FDIC and Fed comment pages are unread.

## 2. Carried count (d): banks with nonaccrual UP and loan allowance DOWN (CALENDAR 11/07 row; PROME packet 11/02)

Route: DEWEY's saved primary files (FFIEC 9/30 individual Call Reports for all 4,267 filers; FDIC BankFind 6/30 and 3/31), read-only. DEWEY showed a fresh June FFIEC pull reproduces the FDIC June baseline. Script: `reserve_release_count.py` beside this report (reproducible, its output below).

| Quarter | Banks usable | Nonaccrual up AND allowance down | Share of banks | Share of total loans |
|---|---:|---:|---:|---:|
| 3/31 → 6/30 | 4,291 | 377 | 8.8% | 14.0% |
| **6/30 → 9/30** | **4,260** | **407** | **9.6%** | **15.7%** |
| *Diagnostic, both moves at least 1%:* 3/31 → 6/30 | | 200 | 4.7% | 5.5% |
| *Diagnostic, both moves at least 1%:* 6/30 → 9/30 | | 217 | 5.1% | 7.7% |

The largest Q3 names by loans: PNC, Huntington, Fifth Third, TD, Citizens, BMO, City National, Zions, Flagstar (allowance near flat), Valley. Many moves are tiny (Fifth Third allowance −$12M on $2.9B).

**Reading:** the Valley shape (reserve cut into rising nonaccrual) is a **minority pattern, about one bank in ten, not much wider than the prior quarter** (+0.8 points of banks, +1.7 points of loans; on the 1% diagnostic +0.4 points of banks, +2.2 points of loans). It is not broad. That answers my standing open question at the population level, descriptively. L801 (10/30) gave coverage decline no standalone weight; this does not re-grade it. **Still not done:** Friedberg four measures (a); modifications up while 30–89 down (e).

**DEWEY 003R population leg (consumed):** the $10–100B band's aggregate coverage *rose* 115.97% → 116.76% in Q3 and its problem-loan share was flat (1.164% → 1.163%), so the six-bank sample (coverage down at 6 of 6) does not describe the band. The $1–10B band fell 150.78% → 126.72%, but United Fidelity Bank is 69.1% of that band's noncurrent increase; without it, 150.41% → 143.53%. Both fit my live claim (severity concentrated, not tier-wide). The EagleBank $135K and $167K residual stays UNKNOWN (DEWEY 11/16 closeout: immaterial, 67.20% → 67.27%).

## 3. United Fidelity Bank: rule readings in PROME's synthesis §1–§2 (PROME asked for corrections)

Read at eCFR (versioner API, 2026-11-01 point in time): 12 CFR 6.3, 6.4(b)(3), 6.5(a), 337.6(b). Bank figures are DEWEY's from the 9/30 Call Report: total capital 7.2647%, Tier 1 6.6431%, leverage 5.8188%, CET1 above 4.5% by $13.239M.

| PROME's reading | Check | Verdict |
|---|---|---|
| "total capital 7.26% is under the 8.0% line of 12 CFR 6.4(b)(3)" | 6.4(b)(3)(i): undercapitalized if total risk-based ratio < 8.0%. Tier 1 6.64% ≥ 6.0, leverage 5.82% ≥ 4.0, CET1 above 4.5: it fails on **one** measure. "Significantly undercapitalized" needs total < 6.0%, not met | **Correct.** Add: undercapitalized on the total-capital measure alone |
| "The category the OCC assigned … UNKNOWN" | 6.3(a)–(b)(1): a bank is **deemed** to have notice of its category "as of the most recent date … a Call Report is required to be filed". No OCC assignment is needed | **Correct this.** By rule it has been undercapitalized since the Q3 Call Report due date, **Fri 10/30/2026**, unless the filing is amended or the OCC changes the category under 6.3(c) or 6.4(e). What stays UNKNOWN is any OCC reclassification or written notice, not the category |
| "12 CFR 337.6(b)(3) … may not accept, renew or roll over brokered deposits. … any FDIC waiver UNKNOWN" | 337.6(b)(2): only an **adequately** capitalized bank may get an FDIC waiver. (b)(3): an undercapitalized bank "may not accept, renew, or roll over any brokered deposit", with no waiver route | **Correct the waiver half: no waiver exists for an undercapitalized bank.** So the $510.5M of brokered deposits maturing within a year (researcher's read) cannot be rolled; brokered deposits fell $147.0M in Q3 |
| "a capital restoration plan would be due about 2026-12-14 (45 days from the filing date)" | 6.5(a)(1): within 45 days of the date the bank "receives notice or is deemed to have notice"; deemed date = Call Report **due** date 10/30 (Fri); 10/30 + 45 days = **Mon 12/14/2026** (`date -d`). The OCC may set a different period in writing | **Date right, basis wrong:** count from the required filing date, not the actual filing date. Still INFERRED: a different OCC period would not be public |
| Art. IV(8) of the 2023 order | Not read at the order text by me; DEWEY's reading (a disposition plan on specified failures plus written direction) agrees with PROME's | **Not checked** |
| Parent guarantee needed for the plan | Statutory (12 USC 1831o(e)(2)(C)); not opened this session | Not checked; consistent with my understanding |

**So what:** no change to my cohort. United Fidelity is a $3.06B-loan private bank outside my 14, no listed parent, no tradable instrument. It is the biggest single member of `late-loans-outside-14` so far (KB ML-REG-298). Its brokered-deposit bar is the live funding constraint; the transmission channels PROME names (brokered funding, collateral sales, Ginnie Mae and tax-credit counterparties) remain unevidenced.

## 4. CYPHER asks (P1 11/12, P2 11/13): consequence for my regional cohort

**No consequence, reasoned.** Sawyer Savings Bank is about $285M of assets; the five banks the Storm group lists total about $6.1B, so on average about $1.2B each (SECONDARY counts). None is in my 14 or KRE's top weights on the evidence given. The N-central exploit (21 servers, payload a Monero miner, no bank named) is a route into community banks that outsource IT (CSBS 91.2% via DEWEY), not into regional balance sheets. DEWEY's base rate: no IT or cyber event has a documented deposit run; lasting stock damage fell on vendors. What would change this: a bank in my 14 or a KRE constituent named as an MSP-route victim, or a regulator alert (CYPHER's 11/19 look). Logged as combination-watch members (KB ML-REG-299). The Microsoft 365 outage (SIG-W-20261114-002, about 24 hours, no bank named, cause given as a capacity upgrade) is context.

## 5. Threshold grades on WALTER's ask (SIG-W-20261113-002)

| Row | Letter | Reading | State |
|---|---|---|---|
| REG-T-03 | FIRED; exit ≤300 ×5 | 320 [11/12], 323 [11/13] | **Unchanged: FIRED, exit run 0** (320 is not ≤300) |
| REG-T-04 | >350 ×3 | max 330 | **NOT FIRED, run 0 of 3** |
| CCC/HY (VX-REG-18.04) | >3.6× ×3 | 4.11× [11/12], 4.07× [11/13] | HARD-FIRE continues. CCC widened while HY tightened: **CCC-led on 11/12 vs 11/09** (CCC +3, HY −14); the vector's rule escalates only on a CCC-LED **re-cross**; the ratio never left the fired state, so this is not a re-cross. **No escalation** (LIQUID owns re-entry) |
| HY dated 11/11 | FRED shows 330 dated 11/11 and no 11/10 row | Either the 11/10 close carries an 11/11 label or 11/10 is missing. **Not decided** (WALTER did not either). No state above depends on it: every reading sits between 300 and 350. My 11/06 note that an 11/11 bar would be a "forward-fill" is **wrong as a description**: 330 differs from 11/09's 334 |

10-year Treasury par 5.10% [11/12] (WALTER -008; BOND and HENRY own the line): rates context for bank securities marks; no letter of mine keys on it.

## 6. Not reached / skipped

- REG-T-02 settled closes 11/11, 11/12, 11/13: **not graded**, Yahoo route down (above). The vendor quote of $74.12 is under $78 and $81.90, so no exit is possible on these bars, but the log rows are owed.
- D:L798 full comment file after the 11:59 PM ET close; FDIC and Fed comment pages.
- Friedberg (a) and modifications (e) counts.
- 8-K and insider monitors failed in boot.py (SEC route, ~110 s each).
- No TERRY candidate: United Fidelity has no listed instrument; the vendor and cyber items are not bank credit; the reserve count is descriptive.

## 7. REG-T-06 graded: REVIEW (found while booting; due 11/13, graded three days late)

| Quarter | Official advances | Basis | Above $700B |
|---|---:|---|---|
| Q4 2025 | $676.711B | CFR statement of condition (12/31/2025 column of the Q3 CFR) | no (run reset) |
| Q1 2026 | $734B | CFR (prior grade, STATUS) | yes, 1 |
| Q2 2026 | $810.7B | CFR (prior grade, STATUS) | yes, 2 |
| **Q3 2026** | **$798.428B** (principal $803.776B, Table 4.1) | Q3 CFR, statement of condition, PDF last-modified 2026-11-13 19:11 GMT, sha256 `58c6ab33ad549960677a487ae4042b3bc2abc2416b10d7922a46ef450edbbacf`, read 11/16 10:2x ET | **yes, 3: REVIEW** |

The Q3 carrying value equals the 10/30 Highlights figure to the million. Q2 → Q3 system change −$12.3B (−1.5%): a level held, not new growth. Under `registry/NOTES.md` § REG-T-06, REVIEW requires both breadth measures (top-four borrowers' contribution to growth; borrower-side median on the matched SEC-filer panel) before any escalation is proposed. **Neither is recorded this session.** On Q2 → Q3 endpoints aggregate growth is negative, so the contribution share is NOT-APPLICABLE by rule; which endpoints the breadth read uses (H1 as on 10/10, or year to date) is open and referred to PROME. Routed: WALTER packet (registered chain PROME action, LIQUID info), `AGENTS/SIGNALS.md` row. Before this session the CFR read had not been made because it sat on "Next existing work" with no wake; the boot surfaced it.
