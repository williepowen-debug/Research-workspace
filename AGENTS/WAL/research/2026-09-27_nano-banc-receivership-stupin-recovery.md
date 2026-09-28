# Nano Banc receivership → the WAL Stupin/Cantor recovery leg

**Written:** 2026-09-27 (Sun), WAL session #8 (Will-launched; PROME packet `17a205519`, `prome-09`). **Research only — no card, no trade.** Budget 60–120 min; delivered **COMPLETE** on WAL's four asks, with named open items (§6).
**Shared fact base:** `PROME/plans/2026-09-27_nano-banc-failure-investigation-PLAN.md` §1 — not re-derived here. **Loss severity / implied haircut = REGINALD's figure** (`AGENTS/REGINALD/reports/2026-09-27_nano-banc-failure-forensics.md` — landed mid-session, consumed in §7; this file carries no second number). DEWEY's document pull — not landed at write time either.

---

## 0. Bottom line (four asks, four answers)

| Ask | Answer | Basis |
|---|---|---|
| **1. Arc** | "Facing receivership" → **CONFIRMED 9/25/2026** (DFPI closure, FDIC receiver, Sunwest acquirer). But **two of the corpus's other Nano claims are wrong or stale**: the "Fed C&D [Mar-4-2025]" (ML-REG-044 wording) was actually the **termination** (3/20/2025) of the 1/18/2022 order; and the MOM Investcos Ch.11 was **dismissed in 2025**, so it is not a live venue | §1 |
| **2. Recovery mechanics** | ★ **The fleet framing "the WAL link is indirect, not a WAL loan to Nano" is incomplete.** WAL's own verified complaint (8/18/2025) shows **Nano Banc ~~holds~~ held (per the complaint; holder at failure unproven — §9, corrected 9/28) deeds of trust SENIOR to WAL on 5 of the 10 collateral loans it pleads — 4 DOTs, $28.04M face.** Those liens (if Nano still held them) are now receivership assets. **Net for WAL: slower near-term, potentially better on the senior-lien leg, marginally worse on the guaranty leg. No new loss mechanism; everything sits inside the existing $72.4M gross residual (Q1 10-Q).** ⤵ **UPDATED same day by DEWEY O1–O3 (§8): guaranty leg WORSE than "marginal" (Stupin in Ch.11 since 4/17/2026; the FDIC now holds ~$27.7M of accelerated Marcil loans ⤵ *(9/28: holder after 9/25 unproven — FDIC-R or Sunwest; KB-207)*), plus a NEW risk: two borrower debtors are investigating avoidance of the Cantor V liens WAL holds.** ⤵ **RESTATED 2026-09-28 (§9): who held each of Nano's four liens AT FAILURE (9/25) is NOT PROVEN for any of them (DEWEY `b9887abd2`), so the senior-lien leg is carried as OPEN BRANCHES, not "mixed". §10 = the pre-registered read-sheet for the 9/29 Ontario hearing.** | §2–§3, §9 |
| **3. Peer facts** | REGINALD's forensics landed mid-session and are consumed in §7 (consistent; no conflict). DEWEY's pull had not landed by delivery. Nothing here depends on it. ⤵ *(9/28: it landed the same day; §8–§10 depend on it.)* Two items were routed to them (§6) | §6 |
| **4. WAL-01 / WAL-02 / ROLL70-EXIT** | **NO CHANGE (2026-09-27).** WAL-01 = office-classified at deck slide 12, and WAL-02 = ex-fraud NCO; **a Cantor charge-off is EXCLUDED from WAL-02 under W2 only when the filing EXPLICITLY attributes it to Cantor** (it did in Q1; no inferred adjustment). ROLL70-EXIT is a price letter (≥$81.90 ×3), and no filing or price rule keys on a third-party failure. **Q3 frames untouched.** The 10-Q frame §8 gets a dated, non-gating annotation (allowed until filing) | §4 |

---

## 1. The arc — what the corpus said vs what is true

| Corpus claim (`FRAUD/STUPIN_CRE.md:92-96`, from REGINALD `ML-REG-044`, "External Research Agent", 2026-02-02) | Truth, dated | Source | Tier |
|---|---|---|---|
| "Facing receivership" | **CONFIRMED:** closed by DFPI **Fri 2026-09-25**; FDIC receiver; Sunwest Bank (Sandy UT) assumes substantially all deposits and ~$476M of assets; DIF cost ≈ **$114M**. Equity fell below the 3% statutory floor; FY2025 net loss ≈ $75.3M; a March-2026 DFPI order demanding 9.5% tangible equity was not met | [FDIC PR 9/25/2026](https://www.fdic.gov/news/press-releases/2026/sunwest-bank-assumes-all-deposits-and-certain-assets-nano-banc-irvine) · [DFPI PR 9/25/2026](https://dfpi.ca.gov/press_release/california-seizes-nano-banc/) | A1 |
| "Fed C&D issued [Mar-4-2025]" | ⛔ **WRONG, inverted.** The Fed's C&D was issued **1/18/2022** and **TERMINATED effective 3/20/2025** (Fed release 4/1/2025). The corpus read a termination as an issuance. The DFPI's 9/25 release also says the Fed action ended in April 2025. **This settles the discrepancy PROME declared in plan correction `f53bc8bd1`.** | [Fed enforcement PR 4/1/2025](https://www.federalreserve.gov/newsevents/pressreleases/enforcement20250401a.htm) · [Fed C&D 1/18/2022](https://www.federalreserve.gov/newsevents/pressreleases/enforcement20220118a.htm) | A1 |
| "Found liable for fraudulent inducement" (Honarkar arbitration) | **Narrow it.** JAMS No. 5220003126: the **partial interim award (2/21/2025)** found Makhijani/Continuum liable for fraudulent inducement and **Nano liable for CONSPIRACY and AIDING-AND-ABETTING** that inducement; the **partial final award is dated 5/23/2025**. Separately, Nano **WON a complete defense verdict** in *Security National Guaranty v. Evariste Group* (OC Superior, Judge Nelson, jury, announced 12/18/2025): $0 against Nano, $83.25M against the other defendants. **Nano was liable in one forum and cleared in another.** "Participant, not victim" is the arbitrator's finding in ONE proceeding, not a settled fact | [award excerpt (claimant-published)](https://issuu.com/savelaguna/docs/jams_arbitration_no._5220003126_partial_interim_aw) · [Jus Mundi index of the 5/23/25 award](https://jusmundi.com/en/document/decision/en-mohammad-honarkar-and-4g-wireless-inc-individually-and-on-behalf-of-mom-as-investco-llc-mom-bs-investco-llc-and-mom-ca-investco-llc-v-mahender-makhijani-continuum-analytics-inc-mom-as-investor-group-llc-mom-bs-investor-group-llc-mom-ca-investor-group-llc-mom-as-manager-llc-mom-bs-manager-llc-mom-ca-manager-llc-and-nano-banc-partial-final-award-friday-23rd-may-2025) (403 to fetch) · [Hunton release 12/18/2025](https://www.hunton.com/news/hunton-wins-significant-defense-verdict-for-nano-banc-defining-limits-of-aiding-and-abetting-liability-for-banks) | B2 (award text is claimant-published; award amount against Nano NOT established) |
| "Officers permanently banned. FBI warrants executed." | Two former executives were prohibited (DFPI 9/25). Co-founder Gressak was banned in 2024 over $15.5M of PPP fraud (American Banker). The FBI searched **Continuum Analytics**, not Nano (KB-WAL-137, Reuters 10/20/2025). "FBI warrants" attached to Nano is **not supported** by anything this desk holds | DFPI PR · [American Banker 9/25/2026](https://www.americanbanker.com/news/embattled-california-bank-is-latest-to-fail) · KB-WAL-137 | A1 / A2 |
| MOM CA Investco Ch.11 (~$382M) as a live venue (PROME ask 2c) | **STALE PREMISE: the MOM Investcos Ch.11 cases (D. Del., filed 2/28/2025) were DISMISSED.** The dismissal was on Honarkar's motion, "allowing Honarkar and 4G to return to California state court to pursue damages under the arbitration award." The date is August 2025 per a secondary source; Polsinelli's news item is dated 10/15/2025. **Confirm at the docket (DEWEY)** | [Polsinelli 10/15/2025](https://www.polsinelli.com/news/polsinelli-represents-mo-honarkar-4g-wireless-in-dismissal-of-bankruptcy-cases) · [Bondoro case summary](https://bondoro.com/mom-investcos/) | B2 |

**What the corpus did NOT have, and it is the WAL arc's biggest omission:** ★ **Mahender Makhijani** (Continuum; per the complaint, the person running Cantor Group V day to day) was **arrested on a federal criminal complaint in early June 2026: bank fraud and falsified loan documents, "defrauded bank out of nearly $100 million"**. "Bank #1" is Western Alliance. The alleged scheme ran 9/2024–4/2025. He pleaded not guilty in Santa Ana, and trial was set for **8/11/2026** before Judge David O. Carter (C.D. Cal.). **Current status (continued? plea?) is UNKNOWN — DEWEY/PACER.** ⤵ *(Resolved §8(5): trial CONTINUED to 1/12/2027, status conference 11/30/2026, detained pending trial 8/17.)* No WAL KB row existed before this session → `KB-WAL-203`. Sources: [DOJ C.D. Cal. release](https://www.justice.gov/usao-cdca/pr/orange-county-man-arrested-federal-criminal-complaint-alleging-he-defrauded-bank-out) (403 to fetch; content via secondaries) · [American Banker 6/11/2026](https://www.americanbanker.com/news/california-financier-arrested-for-100-million-bank-fraud) · [OC Lawyers 8/4/2026](https://www.orangecountylawyers.com/news/trial-set-for-oc-financier-in-100m-fraud-case/). The investigating agencies include **FDIC-OIG** and the **Fed/CFPB OIG**.

---

## 2. ★ The direct WAL–Nano link: Nano's liens sit AHEAD of WAL's collateral

**Primary:** *Western Alliance Bank v. Cantor Group V, LLC, Gerald J. Marcil, Andrew Stupin*, **Verified Complaint**, LA Superior (25STCV24263, KB-WAL-137), dated **2025-08-18** (Ballard Spahr; verified by Al Thuma for WAB). Copy retrieved from Bloomberg's document host (`assets.bwbx.io/…/rNbUA3uuSlq0`); text extracted locally with pdfminer. Tier **A2** (court filing via a third-party host, not the court portal).

The complaint pleads 10 "Fraudulent Title Report" collateral loans. For each, Cantor's employee supplied a title policy showing **WAB first**, and the title insurer's own copy showed older, still-of-record deeds of trust:

| Collateral loan | Property | Senior DOT(s) the doctored policy omitted | Nano? |
|---|---|---|---|
| 26 | 2522 S. Grove Ave, Ontario | Preferred Bank $10.4M (7/11/2017) | — |
| **32** | 23750 Alessandro Blvd, Bldg G/H/I, Moreno Valley | **Nano Banc $9,720,000 (dated 8/29/2019, rec. 9/9/2019), FIRST priority** | ✅ |
| **33** | 23750 Alessandro Blvd, Bldg A/B/O/N, Moreno Valley | **Nano Banc $9,720,000 (same DOT), FIRST priority**; **Notice of Default recorded 5/20/2025** | ✅ |
| 35 | 2460 S. Grove Ave, Ontario | Preferred Bank $10.4M (7/11/2017) | — |
| 37 / 38 / 39 | 28207 / 28251 / 28301 Newhall Ranch Rd, Valencia | Preferred Bank $48.93M (2/28/2017) + $1.5M (12/4/2023) | — |
| **43** | 3700 Inland Empire Blvd, Ontario | Preferred $25.9M (3/30/2022) 1st; **Nano $4,333,151.35 (11/10/2022)** 2nd; **NOD on the Nano DOT recorded 5/20/2025** | ✅ |
| **44** | 12233 Central Ave, Chino | Preferred $22.4M (8/4/2016) 1st; **Nano $5,990,000 (1/26/2023)** 2nd | ✅ |
| **45** | 9826 Cedar St, Bellflower | Umpqua $6.47M (11/6/2018) 1st; **Nano $8,000,000 (9/16/2024)** 2nd | ✅ |

**Nano count: 4 distinct DOTs ($9.72M + $4.33M + $5.99M + $8.00M = $28.04M ORIGINAL FACE) ahead of WAL on 5 of the 10 pleaded collateral loans.** ⚠️ These are face amounts at origination, not current balances, and the pleaded list is the complaint's examples, not necessarily the whole collateral pool. The other senior holder is **Preferred Bank** (a public bank: PFBC). Per American Banker 6/11/2026 it carries **$115M of nonaccrual loans** tied to Makhijani entities. That is REGINALD's lane, flagged in §6.

**Does WAL still sit behind Nano on 9/25/2026? UNKNOWN, and nothing public says who sold WAL its liens.** WAL bought a **$13M non-performing senior-lien loan in Q1-26** and "plans to acquire additional non-performing senior lien loans" (Q1 10-Q, KB-WAL-143). Senior protective liens reached **$64M by Q2** (Q2 deck fn, KB-WAL-123). **The filings name no seller.** Three states are possible, and nothing distinguishes them today:

| State | What the receivership does to it | Evidence for |
|---|---|---|
| (a) WAL already bought Nano's senior liens (they'd fit inside the $64M) | Nothing. WAL is already senior on those properties; the failure is irrelevant to them | Magnitudes allow it ($28.04M face < $64M). **Inference only, never promoted** |
| (b) Nano still held them at failure | They pass to **FDIC as receiver** or to Sunwest. Noncurrent/foreclosure-stage loans are typically retained (retained pool ≈ $215M on the 9/22 books — REGINALD §3, superseding PROME plan §1's ~$260M). The FDIC must dispose of them: a structured or loan sale, typically 3–9 months ⤵ *(B1 only — if FDIC-retained; under B2 Sunwest is a going-concern holder, not a forced seller → §9)* | NODs on Nano's DOTs (5/20/2025) = Nano was enforcing, not selling, as of mid-2025 |
| (c) Nano foreclosed before failure | A senior trustee's sale extinguishes WAL's junior interest in that property unless WAL bid or bought. Loss would already be inside the Q1 $26.1M charge-off ("updated as-is appraisals") ⤵ *(inference — no filing states it; §9a row C)* | NODs recorded 5/20/2025, so a trustee's sale was legally possible from ~late 2025 |

---

## 3. Receivership mechanics → the WAL-specific consequence

**Mechanisms (FIRREA, 12 U.S.C. §1821). This is the statutory frame, not legal advice; DEWEY owns the documents.**

| Mechanism | What it does | Nano status |
|---|---|---|
| **Succession** §1821(d)(2)(A) | FDIC-R succeeds to all of Nano's rights, powers and assets: its **deeds of trust, its guaranty claims against Marcil/Stupin, its lawsuits** — and its liabilities | Automatic 9/25 |
| **Administrative claims process** §1821(d)(3)–(6), (d)(13)(D) | Anyone with a claim against Nano (Honarkar's award, Marcil's C.D. Cal. suit) must file with the receiver by a **bar date ≥90 days after first published notice**. The receiver has 180 days to decide. Courts lack jurisdiction until the process is exhausted | **Bar date NOT published** in the FDIC FAQ (checked 9/27). Claims go to FDIC-R Nano Banc, Dallas, or the FBCSC portal |
| **90-day stay** §1821(d)(12) | The receiver may stay any pending action where Nano is a party | Applies to Marcil v. Nano (C.D. Cal. 8:26-cv-01143, filed 5/11/2026), Nano's suits against Stupin/Marcil, and the Honarkar confirmation proceedings |
| **Depositor preference** §1821(d)(11) | Admin expenses → deposits (the FDIC stands in for the transferred deposits) → general unsecured → subordinated → equity | DIF loss ≈ $114M ⇒ **general unsecured creditors of Nano ≈ zero recovery.** A money award against Nano is now worth ~nothing |
| **Repudiation** §1821(e) | The receiver may disaffirm burdensome contracts; damages are limited to actual direct compensatory damages as of 9/25 | Relevant to any intercreditor, subordination or standstill Nano signed with other lenders on shared collateral. **None is known for WAL** |
| **No injunctions** §1821(j) | No court may restrain the receiver's exercise of its powers | WAL cannot enjoin an FDIC foreclosure or sale of the Nano senior liens |
| **D'Oench / §1823(e)** | Unwritten or unrecorded side agreements can't diminish the FDIC's interest in an asset | Weakens any equitable-subordination theory ("Nano's liens should rank behind WAL because Nano was in on it") against the FDIC as holder. The arbitrator's conspiracy finding runs to Honarkar, not WAL |

**WAL-specific consequence by leg.** Every dollar sits inside the **$72.4M gross residual / $3.5M specific allowance (Q1 10-Q, KB-WAL-143)** plus the $64M liens bought on top (KB-WAL-123). **No new exposure is created.**

| Leg | Direction | Why |
|---|---|---|
| **(a) WAL claims running through Nano** (PROME ask 2a; the "contribution-agreement loop", `ML-REG-039`) | **NEUTRAL, since nothing is carried.** WAL's suit names Cantor V, Marcil and Stupin, not Nano. No primary this desk holds shows a WAL claim against Nano. If one exists it is a general unsecured claim ⇒ ~0 recovery, and it must be filed by the bar date. **The "contribution-agreement loop" is a secondhand Feb-2026 characterization that no WAL primary supports** | Complaint caption; §1821(d)(11) |
| **(b) Senior liens on WAL collateral** (state (b) above) | ⤵ *(B1-only, superseded as a finding by §9)* **Potentially BETTER, and possibly FASTER.** WAL's stated plan to buy senior NPL liens now faces a counterparty that must sell for cash, doesn't litigate the fraud narrative, and runs a known disposition process. **Risk side:** §1821(j) + D'Oench mean WAL can't block an FDIC foreclosure, so WAL must buy or bid, not sue. **Observable bonus:** an FDIC sale of Nano's Stupin-web loans would **print a market price on liens against the same properties as WAL's collateral** (Moreno Valley, Ontario, Chino, Bellflower). That is the closest outside mark WAL's 26.5% loss-to-date (vs ZION 83%) will ever get | Complaint ¶¶44–88; FDIC P&A |
| **(c) Guaranty leg: Stupin 45% / Marcil 5% of the Credit, payment guaranties** (complaint ¶¶113–115) | **Marginally WORSE / SLOWER.** ⤵ *(superseded §8: WORSE)* The FDIC-R inherits Nano's pursuit of Marcil (Nano made demand; Marcil sued Nano 5/11/2026), and it is a persistent, well-funded competing creditor for the same guarantor assets. **Honarkar's award against Nano is now worth ~0**, so Honarkar's collection pressure turns fully onto Makhijani/Continuum/Stupin, the same pockets. The receiver's stays add months | §1821(d)(12); Justia/PACER docket 8:26-cv-01143 |
| **(d) Honarkar / MOM CA properties** (ask 2b–c) | **NOT a WAL leg.** The Laguna Beach / MOM properties are **not** among WAL's pleaded collateral (Inland Empire / LA County / Santa Clarita). The Laguna deed "assigned to Nano Banc" collided with **ZION's** expected first lien (ZeroHedge relaying Bloomberg/court filings, Oct 2025), which is **ZION → REGINALD's lane.** The Nano $20M loan on Honarkar's properties is now an FDIC-R or Sunwest asset; its fight is Honarkar-vs-FDIC | Complaint collateral list; B3 secondary on ZION |
| **(e) Criminal case (Makhijani)** | **Two-way, slow.** A conviction supports WAL's fraud-policy and title claims and brings a restitution order. Restitution rarely makes a lender whole, and **FDIC-OIG and Fed OIG investigate the same scheme that now includes a failed Fed member bank**, so it may broaden. Trial status unknown ⤵ *(resolved §8(5): continued to 1/12/2027)* | §1 |

⤵ *(Superseded: by §8's net line, and its senior-lien clause by §9.)* **Net (2026-09-27): slower near-term, potentially better on the senior-lien leg, marginally worse on the guaranty leg. No change to the magnitude this desk carries. No P&L event expected in Q3 from the failure itself.** Any Q3 effect shows up in the Q3 10-Q "Legal Disputes → Cantor Group V" paragraph, which the frame already grades (§4).

---

## 4. WAL-01 / WAL-02 / ROLL70-EXIT / the Q3 frames — dated statement

**2026-09-27: NO CHANGE to any of the four.**
- **WAL-01** (office classified >$500M at deck slide 12): unrelated. The Cantor collateral is retail, commercial and multifamily in the Inland Empire, financed through the Note Finance line (the complaint's notice address is notefinancing@westernalliancebank.com), not office.
- **WAL-02** (ex-fraud NCO >40bps): **W2 subtracts only charge-offs the filing EXPLICITLY attributes to Cantor/LAM** (10-Q frame :25; print frame :31). An explicitly attributed Q3 Cantor charge-off (should one follow an FDIC sale mark) moves the excluded line, not the graded one. An UNattributed one would count, exactly as the frame already says. Nothing here changes that.
- **`GATE-TERRY-ROLL70-EXIT`** (close ≥$81.90 ×3): a price letter. The tape moved +2.7% 9/23→9/25 ($75.60 → $77.61, Fri close) with the failure announced after the close on 9/25. **0-of-3**, per REGINALD's exit log through 9/25.
- **Q3 frames (L170/L171):** not edited in any grading cell. **`Q3_10Q_GRADING_FRAME_2026-09-24.md` §8 gets one dated, NON-GATING annotation** (permitted until the filing lands): if the Q3 10-Q names the seller of any senior-lien purchase, or a Nano/FDIC counterparty, log it. **It does not change the §3 "$64M candidate tie" rule** (explicit connection only; never by inference).

---

## 5. What this file changes on WAL surfaces (this session)

| Surface | Change |
|---|---|
| `FRAUD/STUPIN_CRE.md` §Nano Banc | The UNVERIFIED "facing receivership" line and the inverted Fed-C&D date are replaced by the dated facts; a pointer to this file is added |
| `workbook/KB.tsv` | **+4 rows:** KB-WAL-201 (receivership, A1) · KB-WAL-202 (Nano senior DOTs on WAL collateral, A2) · KB-WAL-203 (Makhijani criminal case, A2) · KB-WAL-204 (Fed C&D terminated 3/20/2025, A1; corrects the corpus) |
| `workbook/RETIRED_CLAIMS.tsv` | +1: "Fed C&D [Mar-4-2025]" (ML-REG-044 wording) (issuance) — dead |
| `Q3_10Q_GRADING_FRAME_2026-09-24.md` §8 | One dated non-gating annotation |
| `board_log.tsv` | WALTER SIG-W-20260927-004 rowed; framing correction noted |

## 6. Open items and routing

| # | Item | Owner | Why it matters to WAL |
|---|---|---|---|
| O1 | **Were Nano's four DOTs still Nano's at 9/25?** Recorder assignments or reconveyances (Riverside / San Bernardino / LA County), and whether they sit in the FDIC-retained pool | **DEWEY** (documents) — *status 9/28: answered then withdrawn to branches; all four DOTs = U (§9)* | Decides state (a)/(b)/(c) in §2 |
| O2 | Makhijani C.D. Cal. docket: trial held 8/11? continued? plea? restitution? | **DEWEY** (PACER) — *status: RESOLVED §8(5)* | Criminal leg (§3e) |
| O3 | MOM Investcos Ch.11 dismissal date and docket (D. Del.) | **DEWEY** — *status: RESOLVED §8(5), dismissed 8/18/2025* | Closes PROME's stale premise (ask 2c) |
| O4 | FIRREA bar date once the FDIC publishes notice | DEWEY / WALTER WATCH_FOR | Deadline for any WAL claim against Nano (none carried) |
| O5 | **ML-REG-044 correction:** "Fed C&D [Mar-4-2025]" (ML-REG-044 wording) = the termination (3/20/2025) of the 1/18/2022 order; "found liable" = conspiracy/aiding-abetting in ONE forum, cleared in *Security National* (12/2025); "FBI warrants" not supported for Nano | **REGINALD** (owner of the row; this desk does not edit it) | Their row is the fleet's upstream |
| O6 | **Preferred Bank (PFBC)** is the larger senior holder on WAL's collateral ($10.4M, $50.4M, $25.9M, $22.4M DOT face) with $115M of Makhijani-linked nonaccrual (AB 6/11/2026) | **REGINALD** (peer bank) | Cohort read; an FDIC sale of Nano's liens also marks PFBC's collateral |
| O7 | FDIC retained-asset sale of Nano's Stupin-web loans, as a mark on WAL-collateral properties | **CREED** (S6 forced-sale comp) + WAL consumes | §3(b) observable bonus; WATCH_FOR `Nano Banc loan sale` — *B1-only premise (FDIC-retained); Sunwest assumed ~$227M of Nano's loans (Banking Dive 9/28, NEWS)* |
| O8 | Loss severity / implied haircut | **REGINALD** (sole owner) | Cite only; not produced here |

*Sources not fetched (403/timeout), used only via secondaries and labelled as such: DOJ C.D. Cal. release, Jus Mundi award page, Justia/PACER docket, Real Deal, CNBC, US News/Reuters.*

---

## 7. Peer file consumed (landed during this session)

**REGINALD `reports/2026-09-27_nano-banc-failure-forensics.md`** (read ~13:4x ET, **uncommitted at read time**; cite by path, figures owner-canonical, NOT restated as WAL's):
- **The ONE shared figure REGINALD owns (his §3), CURRENT CITE (verified at his report :109, 2026-09-27 ~14:3x ET): the FDIC expects to lose ≈ $120M on Nano's assets beyond what the bank had booked by 9/22/26 ≈ 17% of $690.9M (9/22 books, net of allowance; range $110–120M).** Retained pool ≈ $215M; haircut **ceiling ≤ ~51–56%, unallocable** without the FDIC's bid terms (CREED §2a). *The 6/30 basis (≈ $153M ≈ 21%) is trajectory only; the $33M gap is Q3 loss the bank booked itself. Correction trail, same day: my first draft credited him with "DIF cost 15.5% of assets", which is the FDIC's $114M ÷ $736M; he then gave the 6/30 figure, then superseded it with the 9/22 base. Always name the base.* ⇒ **There is still no point estimate for any mark on Stupin-web collateral**; §3(b)'s "observable bonus" waits for an actual FDIC sale print, not this ceiling.
- His grade of `ML-REG-044`: direction right; timing, cause-mix and severity not predicted. **The capital drain was litigation-driven; credit provisions were 22% of the 2025 loss.** ⇒ the corpus's "death spiral via inability to collect Stupin loans" is NOT what the Call Reports show. That supports this file's §1 narrowing. He independently traced the March-2025 date to an advocacy page (Issuu) and agrees the Fed order was terminated (my KB-WAL-204 has the Fed primary).
- Lookalike screen: **WAL meets 0 of the 4 Nano legs** (book perimeter: no TERRY packet). Consistent with §4.

---

## 8. DEWEY O1–O3 folded (same day, ~15:xx ET) — `AGENTS/DEWEY/output/2026-09-27_nano-banc-primary-documents.md` §4c/§4x (commit `6a90ca732`)

*Read at DEWEY's artifact. DEWEY quotes the bankruptcy documents verbatim with doc numbers; WAL did not re-read PACER ⇒ tier A2. DEWEY's inferences stay labelled.*

**O1 — the §2 state table resolved for two of four (KB-WAL-205):**

| Nano DOT | State at ~9/11–9/25/2026 | Consequence |
|---|---|---|
| Ontario (3700 Inland Empire) | **Nano-held PER THE DEBTOR AS OF 9/8/2026; Nano filed as creditor 9/11/2026. Ownership at 9/25 NOT PROVEN.** Owed ~$5,131,969 behind Preferred ~$23,131,053. Nano was foreclosing (rents receiver Dec 2025) until the borrower's Ch.11 of 3/30/2026 stopped it | ⛔ *Corrected 2026-09-28 (was: "STILL NANO, state (b)" ⇒ "passes to the FDIC receiver ⇒ forced seller"). That read a 9/8–9/11 observation as ownership at failure, and "forced seller" further assumed the FDIC retained the loan rather than Sunwest taking it. Branches → §9.* |
| Chino (12125/12233 Central) | **A "Nano Banc" lien per the debtor AS OF 8/26/2026. Ownership at 9/25 NOT PROVEN; property match (12125 vs 12233, 65.91% TIC) UNRESOLVED; priority NOT stated in the 2026 filing.** Liens "in favor of Western Alliance Bank and Nano Banc … ~$19.1 million"; Preferred "was then the senior lender" (2/2025) | *DEWEY inference, not a finding:* WAL bought Preferred's senior Chino loan = the Q1 "$13M non-performing senior lien loan" (arithmetic + sequence only). ⛔ *Corrected 2026-09-28 (was: "STILL NANO, state (b) — but junior to WAL … the FDIC holds a JUNIOR position under WAL"). Branches → §9.* |
| Moreno Valley (Alessandro, $9.72M 1st) | UNKNOWN. Owner Ch.11 8/18/2026 to halt a trustee sale; beneficiary unconfirmed | — |
| Bellflower ($8.0M 2nd) | UNKNOWN (no LA online index) | — |

**New facts this desk did NOT have (KB-WAL-206/-207):**
1. ★ **WAL's GUARANTY claims left LA Superior on 6/25/2026:** the **Stupins** removed WAL's breach-of-guaranty and declaratory claims against **Stupin and Marcil** as adversary **8:26-ap-01076-SC**; the claims against **Cantor V were not removed** (notice of removal Doc 1, read by WAL at CourtListener 9/27, KB-WAL-208). WAL moved to remand 7/27. KB-137's "no development found" watched only half the case.
2. ★ **Stupin (45% payment guarantor) has been in Ch.11 since 4/17/2026** (8:26-bk-11202-SC). **WAL Claim No. 5 ≈ $173,021,165.87.** Collection on the guaranty is stayed. ⚠️ The claim vs the $98,643,500 balance is **UNRECONCILED**; never infer the bridge. **WAL's own read of Stupin's schedules (Doc 57, 5/15/2026; KB-WAL-208, A1):** assets $92.2M, secured $38.6M, scheduled unsecured $39.2M, which **excludes** WAL (listed "Unknown", contingent/unliquidated/**disputed**). On the debtors' own values that leaves ~$53.6M for all unsecured claims, before other disputed claims (Zions, Preferred, the FDIC-R for Nano) and admin costs. ⇒ **the Stupin guaranty cannot pay near face.** Illustrative ceiling only, never a recovery estimate.
3. **Nano is Marcil's lender:** $19.18M + $8.5M, accelerated 5/1/2026. ⤵ *(9/28: "FDIC-R" = Nano's successor, FDIC-R or Sunwest, unproven per loan)* The FDIC-R now competes with WAL's 5% Marcil guaranty for the same assets (plus the $24.25M Security National judgment against Marcil).
4. ⚠️ **Collateral-avoidance risk (NEW):** the Ontario and Chino debtors are investigating avoidance of the **Cantor V liens WAL holds as pledgee**. That is a direct, two-way risk to WAL's own collateral, independent of Nano.
5. **O2:** Makhijani trial **continued to 1/12/2027** (status conf. 11/30/2026); detained pending trial 8/17. **O3:** MOM Investcos **dismissed 8/18/2025** (dkt 769).

**Revised WAL net (2026-09-27, supersedes §3's net line; ⛔ its senior-lien clause is itself SUPERSEDED 2026-09-28 by §9):** **slower** (guarantor Ch.11 + a removed suit + receiver stays) · ~~senior-lien leg MIXED: Ontario = an FDIC forced seller ahead of WAL (buyable); Chino = WAL already senior with the FDIC junior~~ *(struck 9/28: both halves rested on lien states DEWEY withdrew in `b9887abd2`; the leg is OPEN across three branches → §9)* · **guaranty leg WORSE** (Stupin in Ch.11; the FDIC holds Marcil's loans) · **collateral leg: NEW avoidance risk**. **Still no new exposure beyond the carrying value ($72.4M gross, Q1 10-Q). WAL-01/02 + ROLL70-EXIT: NO CHANGE. Q3 frames: no grading cell touched.** V2 is excluded from the composite, so no score or weight moves; this raises the bar for any Q3 Cantor *recovery* cell without pre-judging it.

**Observables / open:** Tue **9/29 1:30pm** Plaza Continental hearing (8:26-bk-10986): who appears for Nano's lien, the FDIC or Sunwest? · WAL's remand motion (8:26-ap-01076) · the $173.0M claim bridge · a **2-minute human recorder check** (Riverside + San Bernardino; reCAPTCHA-gated, spec in DEWEY §4x) for Moreno Valley · Bellflower needs an in-person LA RR/CC search.

*§8 addendum (~16:xx ET, Will: "can you do this?" re the recorder search): the county recorders are reCAPTCHA-gated, a human-only control, so WAL did **not** attempt them. The Alessandro Group (Moreno Valley) bankruptcy schedules were tried as a CAPTCHA-free substitute: they are **not** on CourtListener RECAP (unpurchased), so Moreno Valley stays UNKNOWN. The same search surfaced the removal notice and the Stupin schedules (KB-WAL-208) read above.*

---

## 9. Revised WAL net, ownership branches OPEN (2026-09-28 14:4x ET, WAL session #10; PROME `prome-7f` doorbell)

**Supersedes the senior-lien clause of §8's net line (struck above) and §3(b)'s "forced seller" framing wherever it is read as a finding.** Basis: DEWEY `b9887abd2` (27b correction) and DEWEY §4x as it now reads. **Who held each of Nano's four DOTs at failure (9/25), and how they rank against WAL, is NOT PROVEN for any of the four.** No branch is resolved below. Every dollar figure is from a named filing, and none is a recovery estimate.

**Two WAL positions, never merged:** (i) the **Cantor V liens WAL holds as pledgee**, the collateral in WAL's suit. Per the complaint these sit **junior** to Nano's DOTs on 5 of 10 pleaded loans, and nothing since shows a subordination or reordering. (ii) any **senior lien WAL bought** under its protective-purchase program ($13M in Q1, $64M by Q2; KB-143, KB-123; **no seller or property named in any filing**). "WAL senior" below means position (ii) ranks ahead of Nano's DOT. **It never means position (i) moved up.**

### 9a. The branches (one row each)

| Branch | What it means | Dollar consequence for WAL | Evidence for / against, dated (per DOT) | What document closes it |
|---|---|---|---|---|
| **A — WAL senior** (old state (a)) | WAL (position ii) holds a lien ahead of Nano's DOT: it bought Nano's DOT, or bought the lien ranking above it | **$0 new.** The purchase cost already sits inside the **$64M protective senior liens** (Q2 deck, KB-123). Nano's failure does not change WAL's recovery on that property; recovery = property value vs WAL's senior balance | **Ontario:** evidence AGAINST, dated 9/8–9/11 only (debtor lists Nano as the 2nd lienholder; Nano filed as creditor 9/11). **Chino:** WAL is named as a lienholder 8/26 beside Nano, **priority not stated**; the $19.1M − ~$6M ≈ $13M match to the Q1 purchase is **arithmetic + sequence, not identification** (DEWEY). **Moreno Valley · Bellflower:** none either way | A **recorded Assignment of DOT to WAL**, identified by recording instrument no. and matched on **APN/legal description**; or a **FRBP 3001(e) transfer notice** / proof of claim (Form 410) by WAL on that DOT in the borrower's Ch.11. **Chino also needs** a title report or subordination agreement for priority, plus parcel records reconciling 12125 vs 12233 Central and the 65.91% TIC |
| **B — Nano senior** (old state (b)) | Nano held the DOT at failure, so it now sits with its successor, ranking ahead of WAL's Cantor V lien. **Sub-branch B1:** FDIC-R **retained** it ⇒ a disposition seller, typically a loan or structured sale within ~3–9 months; WAL can bid or buy, but cannot enjoin (§1821(j)); a sale prints a mark on the same properties. **Sub-branch B2:** it **went to Sunwest** ⇒ a going-concern holder, **not** a forced seller; ordinary workout or foreclosure | **Senior claims stay ahead of WAL's Cantor V interest on that property.** Ontario, on the debtor's 9/8 figures: Preferred ~$23,131,053 + Nano ~$5,131,969 = **~$28,263,022 ahead of WAL's lien**. This desk holds **no current Ontario value**, so no residual to WAL is computed. **If WAL buys the Nano lien**, the cash outlay is ≤ the owed amount (Ontario ≤ ~$5.13M, less any discount). That is a **deployment** into the same protective-lien program, not a new loss. **Loss stays bounded by the $72.4M gross residual (Q1 10-Q, KB-143).** Four-DOT total = **$28.04M original face**, not balances | **Ontario:** FOR, dated 9/8–9/11 only. A transfer between 9/11 and 9/25 fits every observation. **Chino:** FOR on 8/26 only; property match unresolved. **Moreno Valley · Bellflower:** none. **B1 vs B2:** no per-loan evidence (DEWEY §4x: FAQ says only "certain lines of credit" went to Sunwest). *Inference, labelled:* nonperforming liens inside borrower Ch.11s, one facing a lender-liability counterclaim (Ontario), are the class the FDIC typically retains | Ownership at failure: a **3001(e) notice**, **substitution/appearance by "FDIC as Receiver for Nano Banc"** or by **Sunwest** on that claim, or a recorded assignment dated after 9/25 from the FDIC-R. **B1 vs B2:** the P&A agreement (~10/5–10/9) narrows it by **category only** (DEWEY: posted P&As rarely list loans); the per-loan answer is the successor's appearance in each borrower Ch.11 |
| **U — Unresolved** *(the CURRENT state of all four DOTs)* | Neither A nor B is established | **No dollar moves.** Carry the booked perimeter only: **$72.4M gross Cantor residual** (Q1 10-Q) **+ $64M purchased protective senior liens** (Q2 deck). **The $173.0M Stupin Ch.11 claim is a CLAIM amount, not booked exposure** (CATO NB3) | — | Any of the documents in rows A or B, loan by loan. **A clean county-recorder name search alone does NOT close it** (DEWEY §4x completion condition) |
| *(for completeness) C — Extinguished* (old state (c)) | Nano completed a trustee's sale **before** 9/25, which wipes WAL's junior Cantor V interest on that property unless WAL bid | WAL's collateral on that property is gone. **Whether that loss already sits in the Q1 $26.1M charge-off is NOT established by any filing** (the 9/27 transmission leg's "benign" reading is an inference) | **No trustee's deed found for any of the four** (an absence, not proof). **Ontario:** the borrower's Ch.11 (3/30/2026) stopped Nano's sale and the case is live ⇒ C is unlikely for Ontario on the docket. **Moreno Valley:** the owner filed Ch.11 8/18/2026 to halt a scheduled trustee sale; the beneficiary is not confirmed as Nano | A **recorded Trustee's Deed Upon Sale** (instrument no. + APN), dated before 9/25 |

### 9b. Per-DOT state, 2026-09-28

| # | DOT (original face) · property · county | State now | Last dated observation |
|---|---|---|---|
| 1 | $9.72M 1st · 23750 Alessandro Blvd, Moreno Valley · **Riverside** | **U** | Owner Ch.11 8/18/2026 (8:26-bk-12516-SC); beneficiary unconfirmed |
| 2 | $4,333,151 2nd (behind Preferred) · 3700 Inland Empire Blvd, Ontario · **San Bernardino** | **U** (B-leaning on 9/8–9/11 evidence; **not** promoted) | Plaza Continental 8:26-bk-10986-MH Doc 88 (9/8), Doc 90 (9/11) |
| 3 | $5.99M 2nd (per 2025 complaint) · 12233 Central Ave, Chino · **San Bernardino** | **U** (property match + priority open) | Chino Central 8:26-bk-10925-SC Doc 122 (8/26) |
| 4 | $8.0M 2nd (behind Umpqua) · 9826 Cedar St, Bellflower · **Los Angeles** | **U** | none; LA RR/CC has no online index |

### 9c. The net, restated

**Slower** (guarantor Ch.11 + a removed suit + receiver stays) · **senior-lien leg OPEN, across branches A / B(1|2) / U, with C carried** (it was not "mixed"; nothing yet sorts any DOT into A or B) · **guaranty leg WORSE** (Stupin Ch.11; Nano's successor — FDIC-R or Sunwest, unproven per loan — holds Nano's accelerated Marcil loans; *corrected 9/28 audit, the same branch discipline as the liens*) · **collateral leg: NEW avoidance risk** (Ontario + Chino debtors investigating avoidance of the Cantor V liens WAL holds as pledgee) · **no new exposure beyond the booked $72.4M gross + $64M liens.** **WAL-01/02, ROLL70-EXIT, the Q3 frames, V2 (excluded from the composite): NO CHANGE.** No branch outcome, A or B, moves a score or weight. The branches decide **speed and recovery path**, not the thesis.

**Open inputs this desk does NOT hold:** the four DOTs' **recording instrument numbers** and **APNs**. DEWEY §4x says the recorder search should start from them. The complaint (¶¶52, 75, 81, 86) is the likely source; this desk's 9/27 extract was not cached, and a one-shot re-find 9/28 failed. Recording DATES held: Moreno Valley rec. 9/9/2019 · Ontario rec. 1/13/2023 · Chino rec. 6/30/2023 · Bellflower rec. 9/27/2024 (DEWEY corrections to §2's DOT dates).

---

## 10. PRE-REGISTERED read-sheet: Plaza Continental hearing, Tue 2026-09-29 1:30pm PT (written 2026-09-28 ~14:5x ET, BEFORE the hearing)

**Case:** *In re Plaza Continental Group LLC*, C.D. Cal. Bankr. **8:26-bk-10986-MH** (Judge Houle, Ctrm 6C). Stipulation hearing; **Nano is a stipulating party with Preferred** (DEWEY §4x). **Scope: this moves DOT #2 (Ontario) ONLY.** Chino, Moreno Valley and Bellflower move only if a filing in their own docket shows the same fact.
**Read from (primary only):** the docket entries dated 9/28–10/2: minute entry or order, any posted tentative ruling, notices of appearance, substitutions of attorney, **FRBP 3001(e) transfer notices**, amended proofs of claim, and any stay request. **PACER/RECAP lags 1–3 days: an empty docket on 9/29 evening is NOT evidence. Re-check through Fri 10/2; if still nothing, record NO-VERDICT.**

| # | If the docket shows… | Branch move (Ontario) | Also do |
|---|---|---|---|
| H1 | A pleading, appearance or minute entry by **"FDIC as Receiver for Nano Banc"** on Nano's claim/lien | **U → B1** (Nano held it at failure; FDIC-R retained it). Record as **docket-evidenced**, not recorded-instrument-proven: the receiver succeeds only to what Nano held at 9/25 | KB-205 dated line; §9b row 2; tell PROME. Recovery path = FDIC disposition (the "buyable forced seller" reading becomes live, **for Ontario only**) |
| H2 | **Sunwest Bank** appears as holder/successor on Nano's claim | **U → B2** (held at failure; went to Sunwest). **Not** a forced seller | same |
| H3 | A **3001(e) transfer notice** or assignment naming **Western Alliance** as transferee | Transfer dated **before 9/25 → A** (WAL bought it pre-failure). Dated **after 9/25 → A going forward** (WAL bought from the successor); any disclosed price = the first mark on WAL-collateral property | + route OTTO 🟠 (Cantor residual movement, desk `CLAUDE.md` signal table); note for the Q3 10-Q $64M tie (**explicit connection only**) |
| H4 | A transfer to a **third party** (a note buyer, as Conejo Loan Investors bought 2460 S. Grove from Preferred) | **U → third-party senior**: the B-consequence for WAL (someone else still ranks ahead), not a forced seller | same as H1 |
| H5 | **"Nano Banc"** appears through its pre-failure counsel, with **no** receivership mention | **NO-VERDICT.** Four days after closing, a lag in FDIC substitution is ordinary. This supports neither "Nano still holds it" nor a transfer | log only |
| H6 | Hearing **continued**, or the stipulation approved on the papers with no appearance on Nano's side | **NO-VERDICT.** Nothing moves | log only |
| H7 | A current **balance owed** on the Nano lien (vs ~$5,131,969 at 9/8) | none | update the amount in KB-205 |
| H8 | **Relief from stay, a sale or a foreclosure authorized** on the Ontario property | **none** (ownership is untouched) | **WAL consequence regardless of branch:** a senior foreclosure can extinguish the Cantor V junior lien WAL holds unless WAL bids ⇒ log a new KB row; a court-approved **sale price** is a clearing mark ⇒ flag REGINALD (severity owner) + CREED (collateral) |
| H9 | An **avoidance complaint**, or stipulation terms aimed at the **Cantor V liens** WAL holds as pledgee | none | Avoidance risk escalates from "investigating" to "filed/terms" ⇒ new KB row; route OTTO 🟠 |
| H10 | A **§1821(d)(12) stay request** by the FDIC-R | **= H1** | also confirms "slower" |
| H11 | A **priority statement** (e.g. Preferred 1st, Nano 2nd, Cantor V junior) | none | confirms the complaint's ranking; KB-205 note |

**Never moves a branch:** a press or secondary account without docket text · an empty docket before Fri 10/2 · a clean county-recorder **name** search on its own · any inference from the amount matching (the $13M/$19.1M arithmetic stays inference).
**Grading consequences: NONE.** No WAL-01/02 cell, ROLL70-EXIT letter or Q3-frame cell keys on this hearing. V2 is excluded from the composite. **The consume is mechanical:** read the docket → match the row → apply its "branch move" and "also do" → a dated line in KB-205 and §9b → one line to PROME.
