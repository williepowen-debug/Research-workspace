# IQHQ RaDD Aug-2026 Maturity Window — CLOSE-DAY DISCLOSURE SWEEP

**Run:** 2026-08-31, 14:44–15:00 ET (window's last business day; PROME-orchestrated touch — the sweep MEMORY §NEXT-SESSION item 1① owed since 8/23)
**Verdict:** **SWEPT AND EMPTY — no disclosure event found in the Aug-2026 window.** Not "silence": every named instrument below was checked and is listed with its result. ⚠️ Sweep timestamp precedes end-of-day — an 8-K filed late 8/31 would postdate this sweep; the Q3-call cadence makes that unlikely (mgmt 7/22: "~92 days").
**Scope fence:** $0 — no grades, thresholds, weights, probabilities or conviction moved. OZK-09 stays 45%, A30/B45/C8/D17, Option-2 window FROZEN.

## What "no disclosure at window close" means under the desk's own letters

| Letter | Reading |
|---|---|
| STATUS.md:6 + BOTTOM LINE (8/23-28 vintage) | Quiet August is the **pre-registered modal path** of RESERVOIR v1.5 (recognition appraisal-gated + back-loaded; mgmt 7/22: extension+recap in negotiation, "~92 days" → Q3-call disclosure). A quiet window-close **confirms the predicted cadence**, it does not grade anything. |
| Option-2 recognition-window RULING (7/23, Will-approved, FROZEN — `IQHQ_PLAYBOOK.md` §4) | OZK-09's resolver is **event-anchored, not calendar-anchored**: if the maturity resolves without an executed extension, recognition counts through the **Q4'26 print (late Jan '27)**; an executed A/C with <$140M recognition resolves FALSE immediately. **Window-close silence neither resolves nor moves OZK-09.** |
| MEMORY.md §NEXT SESSION 1 (8/28) | *"If ① runs and finds nothing, say 'swept, nothing found' — never report it as silence."* Complied — this file is the swept-and-empty record. |
| WAL 8/28 packet (inbox/processed) | WAL pre-registered a **NO-VERDICT band**: August passing quietly resolves nothing on WAL's side either; carrying instrument re-pointed to OZK's Q3 call. Ping owed → sent (`outbox` + `AGENTS/WAL/inbox/`). |

## Instruments checked (assertion ledger)

| # | Claim | Artifact | Command/query | Observed | Token |
|---|---|---|---|---|---|
| 1 | **No OZK 8-K (or any filing) with event date in Aug 2026 except the 8/5 10-Q** | FDIC securities-filings API, cert 110 — the desk's own named instrument (MEMORY 7/06 finding (c)) | GET `securitiesfilings.fdicconnect.fdic.gov/api/instflng/cert/110` (browser UA), full list parsed | **182 filings total; ZERO with event date > 2026-08-05.** Post-7/1 rows: 7/21 Q2 8-K (FLNG id 11969, already integrated) · **8/5 Form 10-Q (id 11981)**. No other Aug filing of any type. | **VERIFIED** (owner-declared path checked in full — upgrade per WQ-140 rule) |
| 2 | **The one in-window filing (Q2'26 10-Q, 8/5) names no IQHQ/RaDD disclosure** | `raw/Q2_2026_10Q.pdf` (69 pp, retrieved this session via `/api/instflng/11981/attachment/1`) | pdfminer extract (223,377 chars) + keyword grep | 0 hits: `iqhq`, `radd`, `research and development district`, `life science`, `subsequent event`. 6 `extension` hits = mod-table/boilerplate (largest term-extension mod $40.4M C&I — not RaDD-scale). Consistent with OZK's aggregate-only disclosure practice (Call Report card, 8/07). | **VERIFIED** for the keyword pass. ⚠️ **NOT the S4 full read** — that stays owed; a keyword sweep is not a read. |
| 3 | **No press/trade-press disclosure event dated Aug 2026** | WebSearch, 3 passes | ① "IQHQ RaDD San Diego loan maturity extension Bank OZK August 2026" ② "\"IQHQ\" RaDD extension recapitalization August 2026 news" ③ "\"IQHQ\" OR \"RaDD\" San Diego default foreclosure \"August 2026\"" | No August-2026-dated item. All extension/recap language traces to the **7/22 Q2 call** ("constructive, terms not fully developed"). ⚠️ The **June-2024 "two-year extension → Aug 2028" trap resurfaced in pass ①** and was discarded on vintage — third recurrence of [[finding_deep_research_stale_vintage_headline]] (MEMORY 7/04). | **SEARCH-NOT-FOUND** (press has no owner-declared enumerable path; queries named above) |
| 4 | RaDD assignments / NOD at SD County Recorder | Named in `IQHQ_PLAYBOOK.md` §5 monitoring column | — | **NOT CHECKED** — no scripted access from this desk; never checked in desk history. The absence claim in #1–3 does NOT cover recorder-side instruments. | **UNKNOWN** |

## Byproduct

- **Q2'26 Form 10-Q is now local:** `raw/Q2_2026_10Q.pdf` (913,988 B, 69 pp, text-extractable). **S4 (full read) remains owed** — the Q1 10-Q read produced the debt-on-debt pillar; nobody has read the Q2 one.
- Campus-at-Horton leasing check (owed item ②) **NOT run** — out of this touch's scope, still owed.

## Disposition

Window **CLOSED 8/31 swept-and-empty** → the live carrying instrument for RaDD resolution is now the **Q3 earnings call (~Oct, mgmt's self-set "~92-day" report-back)**, with the Q3 Call Report (~Nov) and Q4'26 print (OZK-09 outer bound) behind it. Recorded in STATUS.md + CALENDAR.md; WAL pinged (their pre-registered ask); PROME report in `outbox/`.
