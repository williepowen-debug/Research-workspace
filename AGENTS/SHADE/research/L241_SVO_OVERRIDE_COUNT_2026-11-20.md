# D:L241 — NAIC SVO override COUNT, with its evidence limit (2026-11-20)

**Session:** PROME prome-77 task letter (D:L241, last open item), SHADE on Claude Code / Opus 5.5, laptop. Read 2026-11-20 11:5x ET. **Assignment letter:** the count with its evidence limit; no new threshold or grade. **Nothing graded; charter band (<5 / 5–20 / >20) not applied.**

## Verdict

| Question | Answer | Basis |
|---|---|---|
| Public aggregate count of SVO filing-exemption (FE) rating removals ("overrides") in 2026 | **UNAVAILABLE: not published by design as of 2026-11-20.** Not zero. | P&P Manual ¶149–151 (below); no anonymized summary found in public search 11/20; Mayer Brown 10/15/2026 says the process is "now fully operational" and gives no count |
| Holder-side count, 2 PE-owned insurer groups, transaction slice | **0 "ER" symbols in 8,567 designation cells** across 5 statements (table below) | PRIMARY statutory statements, issuer sites, pulled 11/20 |
| What that 0 means | **Not "zero overrides".** It covers only securities bought or sold in each quarter (Sch D Pt 3/4), plus BA Pt 2/3 and DA/E. A held security whose rating was removed and which did not trade does not appear until the FY2026 annual's Schedule D Part 1 (~2027-03-01) | Quarterly blank perimeter |

## The disclosure design (PRIMARY: NAIC P&P Manual, "As of December 2024", Vol 24 Iss 1, pp. 96–98)

Copy obtained from the State of Indiana mirror (`in.gov/dA/5bbb0d7fb2/publications-ppm-manual.pdf`, HTTP 200, 2,205,988 B, sha256 `1985ea75…c37072`). The NAIC's own site was not tried (it has refused this box before). The Indiana General Assembly copy of the 2026 edition is a script-loaded app shell, not a block. ⚠️ **This is the December 2024 edition. A 2025 or 2026 amendment to ¶149–151 was not checked.**

- **¶146** — if the VOS/TF sub-group agrees the rating misses by the Materiality Threshold (3+ notches, ¶140), the IAO blocks that CRP rating from the automated FE process.
- **¶149** — "The IAO Director(s) will prepare an anonymized summary that does not disclose specific securities, CRPs or impacted insurers of the removed from Filing Exemption Eligibility actions taken over the prior calendar year." ⇒ **the first possible annual count covers CY2026 and arrives in 2027.** Secondary sources (NAIC issue brief, law-firm summaries) say it is presented at each Spring National Meeting, which puts the first one around March 2027. The edition I read names no venue.
- **¶150** — within 45 days of each removal, an anonymized summary of each unique situation, published "on an **insurer accessible** web location". Not shown to be public; none found 11/20.
- **¶151** — the SVO symbol **"ER"** replaces "FE" on the insurer's statutory investment schedules for the affected security. ⇒ **the holder-side route used below.** (¶145 also names a "UR" under-review symbol; the manual does not say it is reported on the schedules. It was scanned anyway: 0.)
- Effective 2026-01-01 (Recent Changes, p. ~xv). Early-2026 secondary: initially not operational (systems/agreements); Mayer Brown 2026-10-15: "now fully operational".

## Holder-side scan (PRIMARY)

Method: text extraction (pymupdf; pdfminer for DLIC Q1), regex `[1-6]\.[A-G]\s*(SYMBOL)\b` over designation cells. **Positive control: the same regex finds "FE" 831 / 1,168 / 106 times**, so the instrument sees symbols in this format. Bare-word `ER` search across all text: 6 hits, all Schedule Y entity names (Ottumwa ER, LLC; PRMC ER Group, Inc.), none a designation.

| Statement | sha256 (prefix) | Designation cells | FE | PL | FM | Z | none/other | **ER** | UR |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| DLIC Q1 2026 | (pdfminer text) | 1,191 | 906 | 84 | 60 | 138 | 3 YE | **0** | 0 |
| DLIC Q2 2026 | `cc658b8d` | 1,678 | 758 | 74 | 60 | 129 | 655 + 2 YE | **0** | 0 |
| DLIC Q3 2026 | `76f86bcc` (= 11/18 record) | 1,735 | 831 | 78 | 54 | 139 | 632 + 1 PLGI | **0** | 0 |
| AANY Q3 2026 (Athene NY) | `a3c5ce4a` | 326 | 106 | 15 | 146 | 16 | 43 | **0** | 0 |
| AAIA Q3 2026 (Athene Annuity & Life, 4,450 pp) | `7e6abafb` | 3,637 | 1,168 | 216 | 1,611 | 146 | 496 | **0** | 0 |
| **Total** | | **8,567** | | | | | | **0** | **0** |

⚠️ The "none" column is a regex bucket (designations with no symbol, plus some false matches in text); it is not used for anything. The cell counts are cells, not unique securities: a CUSIP traded twice counts twice.

**Not scanned:** Athene AADE / ALIRT / ARE4, Global Atlantic, F&G, Corebridge, Brighthouse, Clear Spring and every non-PE insurer. AAIA Q1 and Q2 were not scanned.

## Evidence limit, in one sentence

**No public count exists before the SVO's first annual anonymized summary (CY2026 actions, expected with the Spring 2027 National Meeting); the only measurable proxy, ER symbols in the quarterly transaction schedules of Delaware Life (Q1–Q3) and Athene AAIA/AANY (Q3), reads 0 of 8,567 cells. That is a transaction-slice reading of two groups, not a held-book count and not zero overrides.**

## Resolvers, in date order

1. **~2027-03-01** — FY2026 annual statements, **Schedule D Part 1 symbol column** (full held book): DLIC, AAIA, AANY. First complete holder-side count for these entities.
2. **Spring 2027 National Meeting (~March 2027)** — the SVO's CY2026 anonymized annual summary (¶149). The first fleet-wide count. **This is the instrument the charter band can be graded on.**
3. Any public posting of the ¶150 45-day summaries (opportunistic).

## PROJECTION (not evidence; does not move any score or band)

I expect the CY2026 annual summary to show a **small count, single digits**: the authority was not operational at the start of 2026, every removal needs a credit-committee case plus a VOS/TF sub-group call with domiciliary regulators (¶141–146), and the 0-of-8,567 slice shows no removal touched what two large PE-owned insurers traded this year. **P(CY2026 count ≥ 5) ≈ 25%; P(> 20) ≈ 5%** (event: the ¶149 summary for CY2026 reports at least that many removals; horizon: its publication, ~March 2027). The meaningful alternative is a batch action against one CRP's private-letter book, which would land many removals at once. A single structural finding of that kind could exceed 20. What would change my mind: any public anonymized ¶150 summary before then, or an ER symbol in a FY2026 annual Schedule D Part 1. **Unscored. Not registered:** the publication date and venue are not fixed in the text I read, so a row could grade NO-VERDICT by construction (MEMORY: pre-register against the instrument's publication cadence).

## Trade assessment (WQ-696 form)

Supports **no investment implication**. A zero in a partial slice of two insurers is an absence reading on a regulatory process whose first count is months away. It neither raises nor lowers the probability of capital pressure at Athene or Delaware Life on any horizon a card could use. **No card.** Invalidation would be an ER symbol on a large position at a PE-owned insurer, or a ¶149 summary showing a batch action against one rating agency. That would route to TERRY then.

## Inbox drain (same session)

7 → 0. See `board_log.tsv` rows stamped 2026-11-20. The Delaware item (WALTER 20261120-006 #6, "Delaware regulator says it was misled", NYT/WSJ titles): **no Delaware DOI release on Walter** on the official insurance-commissioner news feed (news.delaware.gov, read 11/20, five newest items unrelated). **Ladder rung (3) "Delaware DOI action" is NOT MET:** a press-attributed statement is not an action. Logged under combo:pe-insurer-governance.
