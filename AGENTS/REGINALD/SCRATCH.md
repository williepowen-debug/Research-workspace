# REGINALD SCRATCH

*Loose notes, intra-day workspace, observations that don't fit anywhere else yet.*

**Purpose:** Capture stuff during the work — half-thoughts, things noticed in passing, quotes worth remembering, format gotchas, draft language.

**What this is NOT:**
- Not a task list (use MEMORY NEXT SESSION)
- Not curated memory (use MEMORY)
- Not a thesis (use THESIS / sub-bank THESIS files)
- Not a research backlog (use ROADMAP — Investigations Backlog section)
- Not a session-bridge (MEMORY Session Notes does that)

**Maintenance discipline:**
- Date each entry / section
- Promote to KB / ROADMAP / STATUS / MEMORY when it grows up; delete when it's done
- Prune aggressively — if a note is older than ~2 weeks and hasn't earned a promotion, delete it

---

## 2026-05-01 PM — Wave 1 chunks 3-6 + Q1 CR sweep

**Format gotchas / data hygiene:**
- KB.tsv pattern confirmed: APPEND new rows + use `DerivedFrom` column to point back to old rows. Old rows STAY ACTIVE — KB is event log not state table. Don't try to mark old rows SUPERSEDED in Status column; that's not the convention.
- Pre-existing column-drift in KB.tsv on KB-WAL-056 and KB-WAL-057 — both have 14 columns instead of 13. Stray tab inserted before "→KB-WAL-039" / "→KB-WAL-021" pattern — looks like the Stale_By column was skipped. Out of scope to fix mid-Wave-1; flagged in ROADMAP open questions.
- `awk -F'\t' 'NR>1 && NF!=13 {print NR": "NF" cols: "substr($0,1,80)}' KB.tsv` is the column-drift detection one-liner.

**FFIEC Q1 access — what works / what doesn't:**
- FDIC SDI (banks.data.fdic.gov, after redirect to api.fdic.gov) — clean JSON; lags 30-60d post-quarter. risview index timestamp = SDI refresh date (not bank filing date).
- SEC EDGAR (data.sec.gov/submissions/CIK<padded>.json) — clean JSON; UA header required ("REGINALD research willie@research.local" works). 10-Qs typically file May 4-10 for accelerated filers.
- FFIEC CDR ManageFacsimiles.aspx — heavy ASP.NET with viewstate; can't curl without browser session.
- FFIEC NIC Institution Profile — returns 403 to standard UA. Different UA might work; not pursued today.

**Useful one-liners cached:**
```
# Get bank's latest SDI quarter
curl -sL "https://api.fdic.gov/banks/financials?filters=CERT:<cert>&fields=REPDTE,ASSET&sort_by=REPDTE&sort_order=DESC&limit=3"

# Get bank's RSSD + holding co linkage
curl -sL "https://api.fdic.gov/banks/institutions?filters=CERT:<cert>&fields=CERT,NAME,FED_RSSD,RSSDHCR,STALP&limit=1"

# Get latest 10-Q from EDGAR
curl -s -A "REGINALD research willie@research.local" "https://data.sec.gov/submissions/CIK<10-digit-padded>.json"
```

**WAL Q1 transcript line-numbers (useful for future quoting):**
- L22: opening — "decisive actions taken on two previously disclosed fraud-related credits"
- L28: LAM — "fully charged off the remaining $126.4 million balance of the loan to a fund of Leucadia Asset Management" + "we will not provide further commentary"
- L34: Cantor — "$29.6 million specific reserve... validated by current as-is appraisal values" + "$26 million" charged + recovery sources (UHNW springing guarantees, mortgage fraud policy)
- L40: HFI loans 3.2% LQ ann, 8% YoY
- L106: leading-vs-lagging — "criticized assets were largely stable... special mention loans increased $78 million quarter-over-quarter, the change was not thematic"
- L154: revised guide — "core net charge-off guidance of 25-35 basis points... at or slightly above the midpoint of this range, with charge-offs declining in the back half"

**Things I noticed but didn't dig into:**
- WAL Apr 30 8-K = pure $0.42/sh dividend declaration. Auto-skip pattern candidate: when an 8-K is dated within 1 trading day of a print and content header is "Quarterly Common and Preferred Stock Dividend," it's noise. Build skip-list?
- The ~$10/sh underwater on WAL's $50M Q1 buyback at $71.61 avg vs current $81.22 → mgmt actually got *good* price relative to current; from short-thesis view this is a small bull point (mgmt timing was correct). But irrelevant in scale.
- The "Juris banking" line item is mentioned multiple times in transcript as the "real surprise driver." We don't have a KB row capturing what Juris banking actually IS. Quick research add: what business / counterparty / how does it monetize?
- SCENARIOS rewrite revealed $65P Jun has only $0.75 EV. That's a position discipline finding — shouldn't have been added at this size in the first place; was vestigial from v1.0 fast-transmission framing.

**Convention question for next session:**
- Should KB rows capture the *quote* verbatim in the Fact column, or paraphrase + put quote in Notes column? Today I mostly paraphrased. Quote-in-Fact would be better for future LLM consumption but inflates row size. Decide per-style after a few more Q reads.

---

## TEMPLATE FOR FUTURE DAYS

```
## YYYY-MM-DD <morning/PM> — <one-line context>

**<Section header>:**
- bullet
- bullet

**Things I noticed but didn't dig into:**
- ...

**One-liners cached:**
```bash
# ...
```

**Convention question / open-thread for next session:**
- ...
```

---

*Companion: `ROADMAP.md` (persistent state across sessions) | `MEMORY.md` (curated cross-session memory) | `STATUS.md` (live dashboard)*
