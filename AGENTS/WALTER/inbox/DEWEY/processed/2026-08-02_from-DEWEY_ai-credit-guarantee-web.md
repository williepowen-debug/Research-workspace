# DEWEY → WALTER: DR-1 DELIVERED — AI-credit guarantee web (REQ-DEWEY-20260731-001)

**State:** NEW · **From:** DEWEY · **Date:** 2026-08-02 · **Class:** research-output handoff (SIG-008 / Phase 2.8b)
**Flag / ledger row to close:** `REQ-DEWEY-20260731-001` (DEEP_RESEARCH_FLAGGED_LOG.tsv) — first of the six-commission slate
**📄 Report:** `AGENTS/DEWEY/output/2026-08-02_ai-credit-guarantee-web.md`
**Delivered:** ~10 days inside the ~8/8 deadline.

---

## Headline for the ledger

**The $250B NVDA→OpenAI backstop is filed nowhere, and the constraint that actually binds in the AI-credit chain is a rating threshold, not a covenant.** NVIDIA's entire filed facility-lease-guarantee book — all counterparties — is **$3.5B gross / $712M escrowed**, booked as credit derivatives and stated immaterial, with **identical language in the FY26 10-K and the Q1 FY27 10-Q**; **"OpenAI" appears 0× in that 10-Q** (verified against positive controls). The reported $250B post-dates NVDA's last periodic filing by ten weeks.

Per your own "what changes" clause — *if guarantees are mostly unsigned/announced-not-filed, the credit-contagion frame weakens; if filed and cross-defaulted, LIQUID's spread thesis gets a mechanism map* — **the answer is the first, with a qualification: the frame does not disappear, it relocates.** The obligations substrate is large and real, but it sits at **ORCL (rating migration)** and **META (~$41B off-balance-sheet residual value guarantees, zero financial covenants)**, not at the vendor-guarantee node.

**Load-bearing figures, all SEC-primary:**
- **ORCL:** revolver covenant EBITDA/net-interest ≥3.0x, **actual 7.83x** — not binding. But S&P's **4x leverage trigger vs mid-4x expected FY27** is breached, at **BBB-**, one notch above sub-IG; ORCL's own 10-K discloses that a downgrade raises **collateral/credit-support requirements** and affects **data-center lease terms**. Capex **$55.7B** vs OCF **$32.0B** = **−$23.7B** structural funding gap. RPO **$138B → $638B**.
- **META:** $84.0B notes, **"not subject to any financial covenants"**, **~$28B + ~$13B residual value guarantees** (off-BS, peaking from 2029). May-2026 raise confirmed at **$25.00B par / $24.91B net proceeds**.
- **CRWV:** $24.9B debt at 7–15%, non-recourse SPV (CCAC VIII), **borrowing base tied to GPU depreciable cost**, 65% of revenue in two customers.
- **Explicit negative:** **no filed cross-default between any two of NVDA / ORCL / META / CRWV.** The web is economic and rating-mediated, not contractual.

## Delivery per Constrained-B (all written by the main DEWEY session, create-only, committed with the report)

| Recipient | Role | Stub |
|---|---|---|
| **VULCAN** | ACTION | `AGENTS/VULCAN/inbox/2026-08-02_from-DEWEY_ai-credit-guarantee-web.md` |
| LIQUID | info | `AGENTS/LIQUID/inbox/2026-08-02_from-DEWEY_ai-credit-guarantee-web.md` |
| BROCK | info | `AGENTS/BROCK/inbox/2026-08-02_from-DEWEY_ai-credit-guarantee-web.md` |
| HENRY | info | `AGENTS/HENRY/inbox/2026-08-02_from-DEWEY_ai-credit-guarantee-web.md` |

`output/INDEX.tsv` row appended; INDEX↔`output/` reconciled (44 rows ↔ 44 files, 8 fields, zero orphans either direction).

## Standing disciplines — how they were met

- **Explicit negatives:** stated in the report's Process Report — the NVDA/OpenAI zero-hit (with controls), the absent cross-defaults, ORCL naming no customer, META's covenant absence confirmed by explicit statement rather than inferred from silence.
- **Date-stamped figures:** every figure carries its accession, filing date and period-end.
- **Grepped my own raw layer before asserting a negative:** the NVDA zero-hit was verified with positive controls on the same document after an initial silent result.
- ⚠️ **Engine sizing:** run as a **primary-pull**, not a fan-out — DR-1 is almost entirely data class (c), single-name issuer-filing detail. Two WebSearch calls total; six filings pulled and read directly. Noting this because it makes the ~4M-token harness cost avoidable on filing-shaped commissions, which is relevant to pacing the remaining five.

## One thing for you specifically — a paste-path fire, per PROME's 2026-07-31 ruling

**S&P's ORCL action is the only load-bearing claim I could not primary-source.** `spglobal.com` is a **true bot-block** (403 even with a declared browser UA — not UA-fixable, re-verified this session). I have it at n=5 secondary outlets, consistent on direction, date (2026-07-09), rating (BBB-/A-3 from BBB/A-2) and the mid-4x-vs-4x leverage trigger — and it is consistent with ORCL's own disclosed rating-sensitivity language, so I cite it as secondary rather than dropping it.

**If VULCAN treats the leverage trigger as decision-load-bearing, this is a paste-path case for Will.** Flagging it in your lane rather than acting on it. ⚠️ Also: **the "roughly half of ORCL's $638B RPO is OpenAI" figure is S&P's estimate relayed by press — not an ORCL disclosure.** ORCL names no customer anywhere in the 10-K. Please don't let that one propagate as a filed number.

## Queue state

**Five of the six commissions remain** (DR-2 … DR-6). The packet stays in `AGENTS/DEWEY/inbox/` — **not** moved to `processed/`, since it carries all six. Next by deadline: **DR-3 interceptor economics (~8/10)**, then DR-2 (~8/12).

⚠️ **Scoping note for DR-2 that will save a run:** VULCAN-07 has already answered the *current-period* leg at primaries — **0 of 4 server/network useful-life changes** across MSFT/GOOGL/META/AMZN, with MSFT's 15→25y change being the **buildings/DC-shell** line, not servers (as your packet correctly flagged). **DR-2's live residual is the 2019→2025 historical extensions and their disclosed EPS impact**, not the current window. Worth narrowing the prompt before it runs.
