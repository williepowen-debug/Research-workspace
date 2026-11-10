# SoftBank Group Q2 FY2026: the ¥597.2B power-equipment loss, read from SoftBank's own documents

Reader: VULCAN research reader (read-only; $0; no outreach). Written Tue 2026-11-10, about 17:30 EST (from `date`).
Labels: **PRIMARY** = a SoftBank document. **SECONDARY** = a named outlet, with its date. **INFERENCE** = my own arithmetic or reading, never a filing.

## Sources and page conventions

| Tag | Document | Where it came from | Page note |
|---|---|---|---|
| FR-EN | Consolidated Financial Report, six months to 9/30/2026 (English) | SAM's copy `sbq2/financial-report_q2fy2026_01_en.pdf` | Cited as **PDF p.N (printed p.N−2)** |
| FR-JA | Same report in Japanese, `financial-report_q2fy2026_01_ja.pdf` | Fetched today from group.softbank (same path pattern) | PDF page |
| ACC | Investor-accounting deck, `investor-accounting_q2fy2026_01_en.pdf` | SAM's copy. A fresh download today is byte-identical (sha256 2945557a…). Server Last-Modified **Tue 10 Nov 2026 16:08:28 GMT** | "Accounting N" = PDF page |
| EP | Earnings presentation, `earnings-presentation_q2fy2026_01_en.pdf` | SAM's copy | PDF page = printed page |
| IP | Investor Briefing deck, `investor-presentation_q2fy2026_01_en.pdf` | Fetched today. Server Last-Modified **Tue 10 Nov 2026 09:21:45 GMT** | PDF page |
| DS | Earnings data sheet `earnings-datasheet_q2fy2026_02.pdf` | SAM's copy | PDF page |
| Q1-FR / Q1-ACC / Q1-CALL | Q1 FY2026 financial report, accounting deck and conference-call transcript (August 2026) | Fetched today | PDF page |
| FY25-FR | FY2025 (year to 3/31/2026) financial report `financial-report_q4fy2025_01_en.pdf` | Fetched today | PDF page |
| Q2-CALL | `earnings-conference-call_q2fy2026_01_en.pdf` | **HTTP 404 at about 17:25 EST on 11/10** (SAM's copy is the same 404 HTML page). The Q1 file under the same path pattern returns 200, so the Q2 transcript is **not yet published** | — |

Local copies are at `/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-VULCAN/fa938f95-ad39-4639-ad15-44b33971db9e/scratchpad/dl/` (raw files) and `…/txt/` (extracted text).

---

## 0. Headline findings

| # | Finding | Label |
|---|---|---|
| 1 | SAM's figures all **VERIFY** at the primary: ¥597,248M = ¥457,030M + ¥140,218M (checked: 457,030 + 140,218 = 597,248), booked in "Other gain (loss)". Cumulative payments are ¥1,500,886M ($9.48B). Rebates of up to $2.1B are not recognised. The advance-payment balance is ¥1,065,097M at 9/30. | PRIMARY FR-EN PDF p.7, p.29, p.75 |
| 2 | **The $6.6B is not future spending.** It is the part of the **$9.5B already paid** that SB7 kept: $9.5B paid − $2.9B written off = **$6.6B balance at 9/30**. That balance is "allocated to equipment purchases for PORTS-Pike power generation project and others". Reading it as "$6.6B still to be bought" is wrong. | PRIMARY EP p.18; ACC 8 |
| 3 | **Cash still owed:** the ¥140.2B ($0.9B) for "contract modifications and settlements" has **not been paid yet**. ACC 8 says: "Cash payments for (2) expected from Q3 onward". Of the $3.7B loss, $2.9B had "already paid" (EP p.17). | PRIMARY ACC 8; EP p.17 |
| 4 | **Two versions of the same slide ("Accounting 8").** The Investor Briefing deck (Last-Modified 09:21Z) says the realignment covers projects "**including PORTS-Pike power generation project in Ohio**" and has **no** "unrelated" box. The standalone accounting deck (Last-Modified 16:08Z) drops "including PORTS-Pike…" and adds a red box: "**The loss of $3.7B is completely unrelated to PORTS-Pike**". | PRIMARY IP p.12 vs ACC 8; timestamps are server headers |
| 4a | It is **INFERENCE** that the 16:08Z file was revised after the briefing. Last-Modified is server metadata. I have not seen an earlier copy of the ACC file itself. | INFERENCE |
| 5 | **No supplier, equipment type or project other than PORTS-Pike is named** in any SoftBank document read. The words turbine, transformer, switchgear, fuel cell and battery, and the names GE Vernova, Siemens, Mitsubishi and Bloom Energy, appear **0 times**. (The only "Bloom" hits are "Bloomberg" in source footnotes.) | PRIMARY (negative search across FR-EN/JA, ACC, EP, IP, DS and Q1/FY25 documents) |
| 6 | The Japanese report adds a detail the English omits: the rebate right was obtained "**サプライヤーから**" ("from the suppliers"). | PRIMARY FR-JA PDF p.6 and p.62 |
| 7 | **Purpose, as stated by SoftBank:** "Made bridge investments in advance to secure power generation equipment in anticipation of shortages. Expect to recoup the investment through project financing". The CFO used the same "effectively bridge financing" framing back in August. | PRIMARY EP p.16; Q1-CALL p.5 |
| 8 | **Remaining purchase commitments: NOT DISCLOSED.** The Q2 report has no commitments or contractual-obligations note for power equipment. "Commitment" appears only for SVF2, the bridge facility and commitment lines. | PRIMARY (negative search, FR-EN) |
| 9 | **A separate U.S. AI-infrastructure hit:** a ¥72,543M impairment on property bought in **Lordstown, Ohio** "for the purpose of establishing a manufacturing facility for data center-related equipment". It is not part of the ¥597.2B. | PRIMARY FR-EN PDF p.75 |

---

## Q1. Every relevant sentence, quoted

### FR-EN, the Q2 financial report (PRIMARY, published 2026-11-10)

| PDF p. (printed) | Quote |
|---|---|
| p.4 (2) | "Energy Global — Energy Global, LP *1 … 1. A subsidiary engaged in the development, construction and operation of solar power plants, as well as the development and construction of data centers, in the U.S." |
| p.5 (3) | "Other loss of ¥663.8 billion (deterioration of ¥809.6 billion YoY), including a loss of ¥597.2 billion arising from the realignment of procurement plans for power generation-related equipment for AI data center projects in the U.S. and related factors" |
| p.7 (5) | "REVISION OF PROCUREMENT PLANS FOR POWER GENERATION-RELATED EQUIPMENT FOR AI DATA CENTER PROJECTS IN THE U.S. Silver Bands 7 LLC ("SB7"), a subsidiary in which the Company and SVF2 have invested, has entered into manufacturing capacity reservation agreements, equipment purchase contracts, and other arrangements for power generation-related equipment to secure robust power supply infrastructure for AI data center projects in the U.S., including the PORTS-Pike Technology Campus in Pike County, Ohio. SB7's cumulative payments related to such procurement from the previous fiscal year through September 30, 2026, totaled ¥1,500,886 million ($9.48 billion)." |
| p.7 (5) | "SB7 revised its equipment procurement strategy given the evolving requirements of its existing and planned projects. As a result of the realignment and SB7's obligations to its suppliers, the Company recognized a loss of ¥597,248 million ($3.73 billion) in "Other gain (loss)" … This loss comprised ¥457,030 million ($2.85 billion) related to non-refundable advance payments made to secure manufacturing capacity and purchase equipment, and ¥140,218 million ($0.88 billion) related to contract modifications and settlements." |
| p.7 (5) | "SB7 became entitled to receive rebates of up to $2.1 billion over the next 10 years on future equipment purchases, subject to certain conditions. As the amount of rebates could not be determined as of September 30, 2026, the Company did not recognize the rebate rights as an asset…" |
| p.9 (7) | "Investment losses of ¥364,387 million recorded in the SoftBank Vision Funds segment in relation to SB7, PayPay Corporation ("PayPay") and other companies are eliminated in consolidation and are therefore not recorded in the consolidated statement of profit or loss." |
| p.9 (7) | "…a derivative loss of ¥203,802 million was recorded due to an increase in the fair value of warrants granted by Energy Global to OpenAI as incentives under lessor lease arrangements related to data centers." |
| p.10 (8) | "H Other Loss: A loss of ¥597,248 million was recorded due to the realignment of procurement plans for power generation-related equipment for AI data center projects in the U.S. and related factors. This loss comprised ¥457,030 million related to non-refundable advance payments and ¥140,218 million related to contract modifications and settlements." |
| p.18 (16) | "Gain (loss) on investments in shares of the Company's subsidiaries, etc. for the period primarily comprised investment losses related to SB7 and PayPay." |
| p.29 (27) | "A Property, plant and equipment increased ¥956,612 million due to the acquisition of assets related to power generation and AI data centers in the U.S." |
| p.29 (27) | "E Other non-current assets: Advance payments related to the acquisition of assets for power generation and AI data centers in the U.S. increased by ¥386,371 million ($2.52 billion) to ¥1,065,097 million, primarily due to additional advance payments. Non-refundable advance payments were derecognized following the realignment of procurement plans…" |
| p.31 (29) | "A Trade and other payables: Payables increased due to the acquisition of assets related to power generation and AI data centers in the U.S." |
| p.32 (30) | "The terms of the warrants granted by Energy Global to OpenAI … were amended in August 2026 in conjunction with the execution of new data center lease agreements with OpenAI, and the warrants were partially forfeited." Also: "Following receipt of $1.5 billion in advance payments under a share issuance agreement, other financial liabilities of ¥262,250 million ($1.7 billion) were recognized at Energy Global" |
| p.36 (34) | "net cash outflows from investing activities of ¥5,372.8 billion, primarily for follow-on investments in OpenAI and the acquisition of assets related to power generation and AI data centers in the U.S." |
| p.37 (35) | "Payments of ¥1,687,203 million were made to acquire assets related to power generation and AI data centers in the U.S. Of this amount, ¥552,859 million was paid by Energy Global and ¥896,458 million was paid by SB7 for power generation-related equipment." |
| p.39 (37) | "Energy Global received advance payments of $1.5 billion (¥240,180 million) under a share issuance agreement entered into with NVIDIA." |
| p.60 (58) | "Segment income" in Other includes a loss relating to power generation-related equipment." |
| p.63 (61) | "¥364,387 million of loss on investments related to the Company's subsidiaries and others held by SVF1 and SVF2 (mainly Silver Bands 7 LLC and PayPay Corporation) is included in gain on investments in the above-mentioned segment income." |
| p.75 (73) | Note 12, "Other gain (loss)": the line "Loss relating to power generation-related equipment *1: (597,248)". Note 1 repeats the p.7 text word for word. |
| p.75 (73) | Note 2: "With respect to property, plant and equipment, including buildings, acquired in Lordstown, Ohio, United States, for the purpose of establishing a manufacturing facility for data center-related equipment, the Company reassessed their recoverable amount based on the intended use of the facility and its future plans. As a result, the Company recognized an impairment loss of ¥72,543 million…" |

### FR-JA, the Japanese report (PRIMARY, 2026-11-10), PDF p.6 (repeated on p.62)
"…この見直しに伴う調達計画の変更や**サプライヤーに対するSB７の契約上の義務**により…597,248百万円（37.3億米ドル）の損失を計上しました。" (Translation: the loss came from the procurement-plan changes under the review and from **SB7's contractual obligations to its suppliers**.)
"なお、SB７は、将来の設備購入に関して、一定の条件の下で今後10年間にわたり最大21億米ドルの割引を受ける権利を**サプライヤーから取得しました**。" (Translation: SB7 **obtained from the suppliers** the right to discounts of up to $2.1B over the next 10 years on future equipment purchases, subject to certain conditions.)

### ACC, the accounting deck (PRIMARY, Last-Modified 16:08Z on 11/10)

| Page | Quote |
|---|---|
| Accounting 6 | "Others (incl. reconciliations) ¥(1,083.6)B: ¥597.2B loss from revision of power generation-related equipment procurement plans in the U.S.; ¥203.8B Energy Global derivative loss" |
| Accounting 7 | "Loss relating to power generation-related equipment for AI data center projects in the U.S.: ¥(597.2)B" |
| **Accounting 8** | "SB7*1 entered into manufacturing capacity reservation agreements, equipment purchase contracts and other arrangements to secure equipment ahead of anticipated supply constraints → Cumulative payments from FY2025 through Q2 FY2026: $9.5B (¥1.5 trillion)*2 • Procurement plans realigned to reflect evolving requirements of existing and planned projects → $6.6B allocated to power generation-related equipment purchases for PORTS-Pike power generation project and others → Recognized a $2.9B loss on non-refundable advance payments for equipment purchases no longer in the revised procurement plans (1), and a $0.9B loss related to contract modifications and settlements (2) → Rights to receive rebates of up to $2.1B for future equipment purchases subject to certain conditions (3)". Diagram: "$9.5B → $6.6B PORTS-Pike power generation PJ and others / $2.9B Other than the above — No longer in the revised plan". "Cash payments for (2) expected from Q3 onward". "(3) … >No asset recognized; purchase timing and amounts undetermined." Red box: "**The loss of $3.7B is completely unrelated to PORTS-Pike**". Footnote *2: "Payments for power generation-related assets in the U.S. by SB7 included in 'Purchase of property, plant and equipment and intangible assets' in consolidated cash flows" |
| Accounting 10 | "Jan 2026: Granted warrants to OpenAI as lease incentives under the Milam County data center lease agreement. Aug 2026: Some of the warrants were forfeited in conjunction with the execution of the PORTS-Pike data center lease agreement with OpenAI." Share-based compensation at Energy Global: ¥(136.0)B |
| Accounting 14 | PP&E: "+¥956.6B". Other non-current assets: "Advance payments related to the acquisition of assets for power generation and AI data centers in the U.S.: +¥386.4B (for details, see p8)" |
| Accounting 17 | "Increase in payables arising from acquisition of U.S. power generation and AI data center assets" |
| Accounting 21 | "Acquisition of assets related to power generation and AI data centers in the U.S. (Including SB7 and SB Energy): ¥(1.7)T" |

### IP, the Investor Briefing deck (PRIMARY, Last-Modified 09:21Z on 11/10)

| Page | Quote |
|---|---|
| p.12 ("Accounting 8") | Same as ACC 8 except: "Procurement plans realigned to reflect evolving requirements of existing and planned projects, **including PORTS-Pike power generation project in Ohio**", and **no "completely unrelated to PORTS-Pike" box**. Checked visually (rendered page) and with a text grep: "unrelated" occurs 0 times in IP. |
| p.87 | SVF2 "TOP FV DRIVERS": "Silver Bands 7 … Revision of procurement plans for power generation-related equipment for AI data center projects in the US". "Revolut and Silver Bands 7 are SVF2 Investments." |
| p.84 | "PORTS-Pike Announced August 2026 … Campus 8GW-IT Secured in Ohio" (source: OpenAI blog, 2026-08-17) |

### EP, the earnings presentation (PRIMARY, 2026-11-10)

| Page | Quote |
|---|---|
| p.15 | "Loss on power generation-related equipment for AI data centers in the U.S.: -¥597.2B (-$3.7B)". "Raised $7.4B in Aug 2026 through prepaid forward contracts backed by Intel shares → Recorded a ¥321.9B derivative loss due to the increase in Intel share price following the contract". Q2 FY2026 net income: -¥1,115.3B (-$7.0B) |
| **p.16** | "Equipment for U.S. AI Data Center (1): **Made bridge investments in advance to secure power generation equipment in anticipation of shortages. Expect to recoup the investment through project financing**". Advance payments related to PORTS-Pike power generation project and others ($B): **FY2025 3.9 · FY2026 Q1–2 5.6 · Total 9.5**. "*Made by Silver Bands 7 (a subsidiary in which SBG and SVF2 have invested, and a separate entity from SB Energy)" |
| **p.17** | "Following a review of the project portfolio, revised certain power-generation equipment procurement strategy, recognized a related loss, and secured potential rebates on future qualifying purchases". "Recorded a loss related to non-refundable advance payments and modifications to signed contracts → $3.7B Loss (**$2.9B already paid**)". "Entitled to rebates on future equipment purchases → Rebates of up to $2.1B" |
| **p.18** | "Equipment for PORTS-Pike power generation project and others": Total Amount **9.5** · Loss Recorded in Q2 FY26 **-2.9** · **Balance as of Sep 30, 2026: 6.6** |
| p.42 | Source line: "Altman Solon forecast cited in SB Energy's S-1 filing dated Aug 31, 2026" |
| p.43 | Portfolio: "Milam County AI Data Center, Milam County, Texas, 753 MW-IT, Under construction" · "PORTS-Pike Technology Campus, Pike County, Ohio, 8.0 GW-IT, Preparing for construction" · "AI Data Center in France, 5.0 GW [gross power], Development and permitting underway" (as of 9/30/2026) |
| p.45 | "Full 8.0 GW-IT capacity, 20-year lease agreement signed (Aug 17, 2026)". "Credit support for OpenAI's leases covering at least 4.25 GW-IT". "Commitment to invest $3.0B in SB Energy ($1.5B funded)" [by NVIDIA]. "NVIDIA has an option to extend credit support to an additional 3.75 GW-IT." |
| p.47 | "Track record of developing 900 MW of power generation capacity in Milam County" (MWdc) |
| p.54 | SVF segment Q2: SVF2 + LatAm + others "Performance −1,924 [$M] … Primarily Silver Bands 7" |
| p.79 | Funding chart includes a "Data center and power generation-related expenditures" bar; "Acquisition of SB Energy stake from SBKK" |

### DS, the data sheet (PRIMARY)

| Page | Quote |
|---|---|
| p.11 | SVF2 portfolio: "Silver Bands 7 LLC — Initial Investment Date FY2025 Q4" (that is, January–March 2026) |
| p.12 and p.13 | "SB Energy, Inc., a subsidiary of Energy Global, LP, has filed to go public." |

**What this means for the entities.** SB7 is the procurement vehicle for power equipment, owned by SBG and SVF2 and "a separate entity from SB Energy" (EP p.16). SB Energy, Inc. is a subsidiary of **Energy Global, LP**. Energy Global is the data-center developer and lessor to OpenAI. It paid ¥552,859M of H1 U.S. power and data-center capital spending; SB7 paid ¥896,458M (FR-EN p.37). Crystal Land, Abilene and Stargate sites: **0 mentions** in any Q2 document. "Stargate" appears only in FY25-FR p.90 (announcement history) and in the Q1 call (below).

---

## Q2. Suppliers, equipment, projects, and what changed

| Item | What SoftBank discloses | Label |
|---|---|---|
| Supplier names | **None.** Only "suppliers" (FR-EN p.7) and, in Japanese, rebates obtained "サプライヤーから" ("from the suppliers") (FR-JA p.6). | PRIMARY |
| Equipment types | **None named.** Only "power generation-related equipment". The contract forms are "manufacturing capacity reservation agreements, equipment purchase contracts, and other arrangements". | PRIMARY FR-EN p.7 |
| Projects | Named: **PORTS-Pike** only. Otherwise "AI data center projects in the U.S." / "PORTS-Pike power generation project and others". Milam County (TX) appears in the portfolio and warrant context, not tied to SB7. | PRIMARY |
| What changed | "SB7 revised its equipment procurement strategy given the evolving requirements of its existing and planned projects" (FR-EN p.7). "Following a review of the project portfolio, revised certain power-generation equipment procurement strategy" (EP p.17). The write-off covers "equipment purchases **no longer in the revised procurement plans**" (ACC 8). No reason is given in the documents: timing, cancellation, design change and renegotiation are all unstated. | PRIMARY |
| CFO's stated reason | Goto said equipment takes a long time to arrive, so SB7 bought ahead, expecting to supply it to projects once they launched and recover the money. After a review aimed at a "better landing" (より良い着地), covering technology innovation and changes to the business model, the result was to book an accounting loss. | **SECONDARY** Reuters Japan via Yahoo!ファイナンス, 2026-11-10 |
| CFO's stated reason (English) | "as a result of reviewing the entire project, we revisited our procurement strategy" … "Things that seemed like a good idea a year ago increasingly give way to reasons to switch to an even better strategy." | **SECONDARY** BigGo Finance, 2026-11-10 (machine-translated; contains numeric errors such as "¥2.9 billion" and a "¥80 million" loss, so use for wording only) |
| ¥140.2B "contract modifications and settlements": with whom? | Counterparty **not named**. The FR says the loss arose from "SB7's obligations to its suppliers". The cash is **not yet paid**: "Cash payments for (2) expected from Q3 onward" (ACC 8). | PRIMARY |
| How the pieces fit | The suppliers that SB7 owes settlement money also granted up to $2.1B of conditional rebates on future purchases. That looks like a negotiated scale-back or modification of orders with the same supplier(s), not a walk-away. No document says this directly. | INFERENCE |

---

## Q3. Earlier disclosures: how the money built up

| Date / document | What was disclosed | Amount | Label |
|---|---|---|---|
| FY25-FR (published May 2026), year-end 3/31/2026, PDF p.33 and p.72 | "Advance payments for the acquisition of assets related to power plant and AI infrastructure construction projects in the U.S. were recorded as advances for property, plant and equipment amounting to ¥678,726 million ($4.2 billion)". Note: "Advance payment for property, plant and equipment *1: — [3/31/2025] / 678,726 [3/31/2026] … 1. Advance payments for the acquisition of assets related to power generation and AI infrastructure in the U.S." **SB7 is not named.** | ¥678.7B ($4.2B) | PRIMARY |
| FY25-FR PDF p.39 and p.41 | "Outlays of ¥1,733.8 billion were recorded for the purchase of property, plant and equipment and intangible assets, reflecting advance payments related to the construction of power plants and AI infrastructure in the U.S., as well as capital expenditures at SoftBank Corp., Energy Global…" | ¥1,733.8B (all entities) | PRIMARY |
| Q1-FR (August 2026), PDF p.27 | "Advance payments related to the acquisition of assets for power generation and data centers in the U.S. increased ¥613,087 million." PP&E up ¥725,871M on the same assets. | +¥613.1B | PRIMARY |
| Q1-FR PDF p.33 | "¥968,929 million was spent to acquire assets related to power generation and data centers in the U.S. Of this amount, ¥637,772 million represented advance payments for those assets." **SB7 is not named in Q1-FR.** | ¥968.9B / ¥637.8B | PRIMARY |
| Q1-ACC | "Advance payments related to the assets for power generation and data centers in the U.S.: +¥613.1B" | — | PRIMARY |
| **Q1-CALL** (August 2026), PDF p.5 | Analyst asked about "$6 billion spent on power generation and data center-related assets in the U.S." Goto: "SBG has temporarily acquired certain equipment required for those projects due to the timing of procurement… Once the projects commence, we expect the related funding to be refinanced through project financing. Accordingly, although this is effectively bridge financing, it is presented in this manner on our balance sheet." | — | PRIMARY (transcript) |
| Q1-CALL PDF p.4 | Asked whether the $6B was "primarily related to Stargate, SB Energy, or a combination", Goto replied: "Energy Global plays a central role in some projects, while there are also projects in which it is not involved. At present, Stargate is defined quite broadly and may encompass various data center projects undertaken by SBG, Oracle, and OpenAI…" | — | PRIMARY |
| Q1-CALL PDF p.1 | On the "10 GW Ohio data center": "We plan to begin work on the first site in 2026. We also expect the project to be financed through project financing supported by creditworthy offtakers." (Ohio was described as 10 GW then; it is **8.0 GW-IT** now. The units may differ: GW versus GW-IT.) | — | PRIMARY |
| Q2 (this quarter) | **First time SB7 is named.** SB7 cumulative ¥1,500,886M ($9.48B), split $3.9B in FY2025 and $5.6B in H1 FY2026 (EP p.16). Advance-payment balance ¥1,065,097M at 9/30. | — | PRIMARY |
| Commitments (契約上の義務 / purchase obligations) | **No quantified commitments note** in FY25-FR, Q1-FR or Q2-FR. A search for commitment/contractual/purchase obligation finds only SVF2 equity commitments, the bridge facility and commitment lines. I did **not** read the 有価証券報告書 (annual securities report, June 2026; EDINET). The `annual-report_fy2026_03_en.pdf` I fetched is a 1-page CFO-message extract. | n/a | PRIMARY (negative) / GAP |

**Arithmetic on the build-up (INFERENCE):**
- SB7 payments in FY2025 ≈ ¥1,500,886M − ¥896,458M = **¥604.4B** (about $3.9B at roughly ¥155/$), which matches EP p.16.
- The 3/31/2026 balance (¥678.7B) is higher than that ¥604.4B, so about ¥74B of the year-end balance probably belongs to other entities or reflects currency moves.
- Implied 6/30 balance ≈ ¥678.7B + ¥613.1B = ¥1,291.8B. The 9/30 balance is ¥1,065.1B, so Q2 change ≈ **−¥226.7B**. That means roughly ¥230B of gross Q2 additions, after the −¥457.0B write-off, currency moves and transfers to PP&E (this split is not disclosed).
- ¥1,065.1B at the 9/30 rate of ¥157.35 = **$6.77B**, against SB7's $6.6B. The balance line covers all "power generation and AI data centers in the U.S.", so it probably includes non-SB7 advances. **The reconciliation is not disclosed.**

---

## Q4. Commitments and what is still owed

| Item | Answer | Label |
|---|---|---|
| Remaining purchase commitments for power equipment | **Not disclosed** in the Q2 report. | PRIMARY (negative) |
| Known future cash out | **¥140.2B ($0.88B) settlement**, "expected from Q3 onward" (Q3 = October–December 2026). | PRIMARY ACC 8 |
| What the $6.6B buys | It is money **already paid** (advance payments still on the books), "allocated to equipment purchases for PORTS-Pike power generation project and others". The plan is to **recoup it through project financing** (EP p.16), that is, sell or transfer the equipment into project-level financed vehicles. | PRIMARY EP p.16 and p.18 |
| Whether any further cash is owed beyond the $9.48B and the ¥140.2B | **Unknown.** Rebates of up to $2.1B on "future equipment purchases" imply more purchases are planned, but there is "purchase timing and amounts undetermined". | PRIMARY ACC 8 |
| Balance-sheet hint | Trade and other payables rose "due to the acquisition of assets related to power generation and AI data centers in the U.S." No amount is split out for SB7 or for the settlement. | PRIMARY FR-EN p.31 |

---

## Q5. The 11/10 briefing (Q2 transcript not yet published)

| Topic | What was said | Source |
|---|---|---|
| Transcript | `earnings-conference-call_q2fy2026_01_en.pdf` returns **404** at about 17:25 EST on 11/10. | PRIMARY (absence) |
| **Ohio size** | Goto: "this is not a discussion about scaling back the Ohio project. The project is progressing very smoothly." | SECONDARY BigGo Finance, 2026-11-10 (machine-translated) |
| Ohio (Japanese) | 「日米関税合意に基づく米オハイオ州パイク郡の案件は順調に進んでいるとした」 (Translation: "said the Pike County, Ohio project, based on the Japan–U.S. tariff agreement, is progressing smoothly") | SECONDARY Reuters Japan via Yahoo!ファイナンス / d-menu, 2026-11-10 |
| Remaining $6.6B | "the remaining $6.6 billion to be absorbed by projects including the ongoing Ports Pike project" | SECONDARY BigGo, 2026-11-10 |
| Rebates | 割引確保は「中期計画的なわれわれの計画にはプラス材料として評価していいだろう」 (Translation: securing the discounts "can be counted as a positive for our medium-term plan"). Also: "データセンタープロジェクトはまだ始まったばかりで、これから５年、１０年かけてさらに規模が大きく成長していくだろう" (Translation: "the data center projects have only just begun and will grow much larger over the next 5 to 10 years") | SECONDARY Reuters Japan, 2026-11-10 |
| **Musk, 11/6 ("SoftBank is defaulting on their turbine orders")** | Goto: 「なぜああいうつぶやきがなされたか、全くその意図は分からない」「私たちは債務不履行なんかに陥っていない」 (Translation: "we have no idea at all why that post was made"; "we are not in any kind of default"). He also said the AI-infrastructure plan continues as planned. ITmedia's headline: 「全くの事実無根」 ("completely baseless"). | SECONDARY ITmedia NEWS, 2026-11-10 (read via the yayafa.com mirror; the ITmedia original was not fetched) |
| Musk (English) | "We have no idea why such a tweet was made, but to state the facts, it is completely baseless. We are not in default of any kind, and our AI infrastructure plans are progressing as scheduled." | SECONDARY BigGo, 2026-11-10 |
| Musk claim versus the filing | No SoftBank document uses the word "turbine". The filing describes **settlements and contract modifications with suppliers, paid in cash from Q3**, plus rebates from those suppliers. That is a negotiated change to orders, not a default. But an order reduction is consistent with what a supplier-side observer could describe as "defaulting". | INFERENCE |
| Stargate / Trump / midterms | Goto said he does not think the impact is closely tied to the election result, that each project's start is already decided, and 「（孫会長と）大統領の関係がどうこうということではないだろう」 (Translation: "it is probably not a question of the relationship between Chairman Son and the President"). Delays of pre-construction projects are 「当然あるかもしれない」 ("may well happen"), described as one of several scenarios, to be absorbed by re-scheduling. | SECONDARY ITmedia, 2026-11-10 |
| SB Energy / OpenAI / NVIDIA "circular financing" | "The characterization of circular financing as a risk would benefit from a bit more analysis and a calmer assessment." Lenders judge "the ultimate lender" credit, that is, hyperscalers 「雲の上ぐらいクレジットの高い企業ばかり」 ("all companies with credit far above ours, up in the clouds"). | SECONDARY BigGo, ITmedia, 2026-11-10 |
| NAV after quarter-end | Goto: NAV was ¥59.8T at 9/30 and **¥44.7T** at 11/9 prices and FX; LTV "well below 25%". | SECONDARY ITmedia, BigGo, 2026-11-10 |
| Press error to flag | w.media (11/10) wrote that SoftBank wrote down "payments to secure power-generation equipment for its 8 GW PORTS-Pike Technology Campus". That conflicts with ACC 8 ("completely unrelated to PORTS-Pike"). The FR only says the procurement served projects "including" PORTS-Pike. CNBC (11/10) phrases it correctly as "projects, like the PORTS-Pike Technology Campus". | SECONDARY versus PRIMARY |
| FirstSquawk 08:49Z | Not retrieved (no free archive). The BigGo wording above is the fullest version found. | GAP |

---

## Q6. Intel prepaid forwards: facts only

| Fact | Quote / figure | Source |
|---|---|---|
| Raise | "A wholly owned financing subsidiary raised $7.35 billion in August 2026 through prepaid forward contracts backed by **all of its Intel shares**." | PRIMARY FR-EN PDF p.6 (printed 4) |
| Yen proceeds | "raised ¥1,177,124 million ($7.35 billion) … The proceeds were used to fund part of the repayment of borrowings under the bridge facility agreement" | PRIMARY FR-EN PDF p.38 (printed 36) |
| What the bridge was for | "By September 15, 2026, the Company had prepaid the full $30.0 billion drawn under a $40.0 billion bridge facility agreement entered into in March 2026, primarily to fund follow-on investments in OpenAI. The remaining $10.0 billion undrawn facility was canceled effective September 30, 2026" | PRIMARY FR-EN PDF p.6 |
| So the chain is | Intel forwards → repay the bridge → the bridge had funded OpenAI follow-ons. Other repayment sources: an $11.87B term loan and $5.0B of extra Arm margin loan. | PRIMARY |
| Structure | "collar contracts under which the number of shares to be delivered at settlement is determined by reference to the market price of Intel shares at the valuation dates … a cap and a floor are set" | PRIMARY FR-EN notes (about PDF p.70–71) |
| Counterparties | "entered into prepaid forward contracts **with financial institutions**" (**not named**). Pledged Intel shares carried at ¥1,645,060M, of which ¥1,096,707M are "Intel shares over which financial institutions were granted rights of use" | PRIMARY FR-EN notes |
| Loss | Derivative loss ¥321,891M "as Intel's share price increased by the second quarter-end". Non-current derivative liability ¥337,869M ($2.1B). Financial liability ¥1,139,622M (prepaid-forward liabilities total ¥1,399.4B, including T-Mobile ¥259.7B) | PRIMARY FR-EN PDF p.9, p.13, p.27, p.32, p.34 |
| Earlier context | At the Q1 call, asked about monetising Intel, Goto said: "There are no particular restrictions." | PRIMARY Q1-CALL PDF p.4 |

---

## Known unknowns

1. **Supplier identity** for SB7's capacity reservations, purchase contracts, settlements and rebates: not named in any SoftBank document.
2. **Equipment type** (gas turbines, reciprocating engines, fuel cells, transformers, batteries): not stated anywhere.
3. **Which projects** the $2.9B write-off was meant for. It is "no longer in the revised plan" and, per ACC 8, "unrelated to PORTS-Pike". Not named.
4. **The cause** of the realignment (cancellation, design change, technology swap or timing): only "evolving requirements" in the documents, and "technology innovation / business model review" (CFO, via Reuters JP).
5. **Remaining purchase commitments** beyond the paid $9.48B and the ¥140.2B settlement: not disclosed. The 有価証券報告書 (June 2026) and any Q2 半期報告書 (semi-annual securities report) commitments note were **not read**.
6. **Rebate conditions** (volumes, timing, counterparties): undisclosed. The rebate is not recognised as an asset.
7. **Whether ACC 8 was revised after the briefing.** The 09:21Z IP version includes "including PORTS-Pike"; the 16:08Z ACC version has the "completely unrelated" box. There is no earlier ACC copy to prove an edit, and SoftBank has made no statement explaining the difference.
8. **How the $6.6B SB7 balance reconciles** with the ¥1,065.1B advance-payment line ($6.77B) and with PP&E. The entity split is not disclosed.
9. **The Q2 call transcript** (404 at 17:25 EST). The fuller Goto statement on Ohio comes only from machine-translated BigGo plus Reuters JP. FirstSquawk's original was not retrieved.
10. **Q2 SB7 payments alone.** Q1 advance payments of ¥637.8B are not split by entity, so the Q2 SB7 cash spend cannot be isolated from the documents.
11. **Intel forward counterparties and maturities:** "financial institutions" only; the valuation and settlement dates were not found in the pages read.
