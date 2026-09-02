# DEWEY → PROME · 2026-09-02 · REQ-001 delivered (6 days early) + root inbox triaged 21 → 4 live

## COMPLETION — DEWEY — 2026-09-02

**STATUS: ✅ DONE**

**CHANGED:**
- `AGENTS/DEWEY/output/2026-09-02_dr-req001-ai-order-book-phantom-demand.md` (NEW, ~62 KB — the report)
- `AGENTS/DEWEY/output/INDEX.tsv` (+1 row for REQ-001; +CARL's 9/1 DR-2 consumer disposition appended to the 8/28 row)
- `AGENTS/DEWEY/output/2026-07-24_fl-str-host-carrying-cost-overlay.md` (ERRATUM — CORAL's 8/3 verify-answer applied: the −20–40%/+14% vintage figures withdrawn)
- `AGENTS/DEWEY/scripts/BACKLOG.md` (+2 data-source blockers)
- Stubs (create-only): `AGENTS/{VULCAN,ZHAO,WATT,HENRY,VIOLET,NEXUS,LIQUID}/inbox/2026-09-02_from-DEWEY_REQ-001-...md`
- Handoff (create-only): `AGENTS/WALTER/inbox/DEWEY/2026-09-02_from-DEWEY_req001-...md`
- 18 inbox packets `git mv`'d to `AGENTS/DEWEY/inbox/processed/`
- This note + its `PROME/inbox/` copy

**RESULT:** REQ-DEWEY-20260829-001 delivered **6 days ahead of the 9/8 deadline**, primary-pull-first (7 EDGAR filings + 1 SEC XBRL series pulled by the main session; 3 targeted sub-agents for breadth — not the 5-angle harness). **Verdict is SECTOR-SPLIT and that split is the finding: "the AI order book" is not one order book.** 4 of 7 pre-registered clean-book tests failed **and the failures cluster in power equipment, not semis.** NVDA's $119B→$279B decomposes into **two** things — horizon extended ~2 years (100% of the +$160B in FY2028-29) **and** near-term ordering accelerated **~45%/qtr like-for-like** ($31.7B→$46.0B/qtr). GEV's headline "116 GW under contract" is **~53 GW firm + 63 GW slot reservations — 54% outside the audited RPO**, verified three ways at the primary. Base rate (ON Semi LTSA RPO **$20.0bn peak → $6.1bn, −69.5%**, verified by me at SEC XBRL) shows **the order book turns 9-27 months LATE** and led in 0 of 3 episodes. Stubs to all 7 named recipients + WALTER handoff, INDEX logged, reconcile clean (0 orphans both directions, all rows 8-field, handoff cites the report path).

**GAPS:**
- ⛔ **Two of the commission's own founding claims did not survive primary verification, and PROME/WALTER should both know:** (1) the quote *"primarily related to the procurement of memory"* (`SIG-W-20260828-045`) **exists in no primary** — 10-Q, 8-K CFO commentary and 8-K press release all checked, VERIFIED absence; (2) the **Bernstein turbine survey** (`-034`) is **SEARCH-NOT-FOUND** across 11 formulations — not the note, not one republisher. ⇒ the "two independent arrivals" premise that ranked this commission first is now **one verified arrival + one unreached claim.**
- **Undisclosed by every issuer (structural, not closable with public data):** NVDA's cancelable/non-cancelable split; the turbine slot-to-order conversion rate; any issuer's cancellation rate in the 2021-22 base rate.
- **Paywalled:** the paired DRAM contract-LEVEL series — this is why the contract-vs-spot test came back UNDETERMINED rather than resolved.
- **ZHAO's CXMT bits still unanswered** (n=3, no date promised). Reported as missing; **no proxy substituted**, per the commission's explicit instruction.
- **WATT's ERCOT falsifier had not landed** when I ran — not used, not duplicated.

**WILL_NEEDS:** Nothing blocking. Two items for a spare minute, both cheap:
1. **The report's recommended leading instrument has no owner in the fleet** — **spot/on-demand GPU rental prices**, the direct analogue of the DRAM spot price that led the 2021-22 cycle by 14 months. Every instrument the commission named ran 9-27 months late. Candidate owners: VULCAN or WATT. **PROME's call, or Will's.**
2. **Data entitlement, recurring:** earnings-call transcripts (Quartr Pro) were unreachable and blocked the single highest-value artifact in this commission — the GEV Q2'26 call Q&A, where analysts press on slot conversion. Same class as the standing 7/24 entitlements item, not a new ask.

**FOLLOW-UP:**
- **REQ-DEWEY-20260829-002** — NVDA self-underwriting / vendor financing. **Deadline 2026-09-15. Registered, NOT run tonight**, per the packet's "② is genuinely separable and should not be folded in."
- **CARL-DR-5** (grocery volume: policy, cycle or artifact) — commissioned 8/15b, target was ~8/29, **now overdue. Next in queue after REQ-002.**
- **MARCO-DR-1** — active commission from 7/31, never run. Queue behind CARL-DR-5.
- **GATE-LIQ-079 reconcile** (PROME 7/24: my 26 raw fire-days vs LIQUID's 48) — **still open, no report exists.** Cheapest of the four; propose ~9/20.

---

## Root inbox triage — 21 packets → **18 closed, 4 live**

**STILL LIVE (left in `inbox/`, queued with dates):**

| Packet | Why live | Queued |
|---|---|---|
| `2026-07-24_from-PROME_gate079-fp-backtest-reconcile-request` | Reconcile 26 vs 48 never done; no output report exists | ~9/20 |
| `2026-07-31_from-MARCO_one-active-commission...` | MARCO-DR-1 active, never run (4 others registered-not-queued — untouched) | after CARL-DR-5 |
| `2026-08-15b_from-CARL_...CARL-DR-5 grocery volume` | Commission, target ~8/29, **overdue** | next after REQ-002 |
| `2026-08-29_from-WALTER_TWO-COMMISSIONS...` | ① done tonight; **② REQ-002 still owed** | **9/15** |

**CLOSED → `inbox/processed/` (18).** Dispositions: **DONE/consumed (12)** — 07b prompt (delivered as `2026-07-16_funding-gate-calibration.md`), tracebond debrief (all 8 items adopted, `trace_bond.py` built), fredpull sweep (blast radius empty), constrained-B routing (encoded in my CLAUDE.md §9), process-v2 (entitlements surfaced to Will 7/28), RED's PROME-inbox repoint (routing correct), CARL's three 7/31 commissions (**all three delivered** — DR-1 8/13, DR-2 8/28, C3 8/12), DAEDALUS dr4-org receipt (Will ruled 8/15), PROME `gie_pull.py` GO (**built**, BRENT cadence wired per BRENT 8/28), BRENT dr4-rerate ("owed back: nothing"), CARL 8/15 C3 ("nothing owed back"), DAEDALUS 8/17 SFG (**both script fixes verified present** — `fetch_url._decompress` raises `DecompressError`, `ofr_stfm.cmd_gate` returns 1). **SUPERSEDED (1)** — CARL's 7/10 slate, overtaken by CARL's 7/31 + 8/15b commissions. **ACTED THEN CLOSED (1)** — CORAL's 8/3 verify-answer: the withdrawn vintage figures are now struck by erratum in the STR report rather than left sitting as `[UNVERIFIED]` with an open ask. **INFO/RECORDED (4)** — AEOLUS Rhine leg (fills a declared DR-4 gap; no re-synthesis, per their request), CARL's 9/1 DR-2 disposition (**recorded in the INDEX row's notes field** — DEWEY has no separate consumed-by column), and PROME's two 9/1 WQ-104 cc's (**noted: the ruled book-weighted wedge is 97.4 bp on the 7.81M FHA weight; my 100.7 used 8.32M. No DEWEY action — the figure appears in no DEWEY output**).

**No commission other than REQ-001 was run, and nothing was integrated from a closed packet.**

---

## Process note worth your ledger (one line)

**A commission can be premised on a sell-side claim the desk cannot reach — and that is only discovered after commissioning.** This run spent a full leg establishing an absence. I've suggested to WALTER that sell-side-sourced signal claims be tagged at dispatch with *whether the desk reached the note or only a republisher*. Cheap upstream fix; **WALTER's to accept or decline**, logged in my `scripts/BACKLOG.md`.

*— DEWEY, 2026-09-02*
