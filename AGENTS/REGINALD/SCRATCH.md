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

*FFIEC access patterns promoted to MEMORY findings (2026-05-01). Most other content stale; keeping these durable bits:*

**KB.tsv hygiene (still relevant):**
- KB.tsv pattern: APPEND new rows + use `DerivedFrom` column to point back to old rows. Old rows STAY ACTIVE — KB is event log not state table. Don't mark old rows SUPERSEDED in Status; that's not the convention.
- Pre-existing column-drift on KB-WAL-056/057 (14 cols not 13) — out of scope; flagged in ROADMAP open questions.
- Detection one-liner: `awk -F'\t' 'NR>1 && NF!=13 {print NR": "NF" cols: "substr($0,1,80)}' KB.tsv`

**WAL Q1 transcript line-numbers (useful for future quoting):**
- L22: opening — "decisive actions taken on two previously disclosed fraud-related credits"
- L28: LAM — "fully charged off the remaining $126.4 million balance of the loan to a fund of Leucadia Asset Management" + "we will not provide further commentary"
- L34: Cantor — "$29.6 million specific reserve... validated by current as-is appraisal values" + "$26 million" charged + recovery sources (UHNW springing guarantees, mortgage fraud policy)
- L106: leading-vs-lagging — "criticized assets were largely stable... special mention loans increased $78 million quarter-over-quarter, the change was not thematic"
- L154: revised guide — "core net charge-off guidance of 25-35 basis points... at or slightly above the midpoint of this range"

**Open backlog item (didn't get to):**
- "Juris banking" line — mentioned multiple times in WAL transcript as the "real surprise driver." We don't have a KB row capturing what Juris banking actually IS. Research add: what business / counterparty / how does it monetize?

---

## 2026-05-08 PM — Long Friday: REG-20/gitignore close + KRE phantom + POSITIONS refresh + MAY15 + 10-Q sweep

**Patterns / one-liners cached (durable bits promoted to MEMORY findings):**

```python
# yfinance option chain (Friday-night-friendly; close marks)
import yfinance as yf
chain = yf.Ticker('SYM').option_chain('YYYY-MM-DD')  # expiry ISO-format
puts = chain.puts.copy()  # DataFrame: strike/lastPrice/bid/ask/volume/openInterest/impliedVolatility
# NOTE: greeks NOT in output. Use Black-Scholes manually if needed.
```

```bash
# 10-Q text extraction (XBRL-heavy; ~3-4MB raw → ~350KB stripped)
curl -s -H "User-Agent: REGINALD research willie@research.local" \
  "https://www.sec.gov/Archives/edgar/data/<CIK-no-leading-zeros>/<accession-no-dashes>/<filename>.htm" \
  -o /tmp/file.htm
python3 -c "
import re
text = re.sub(r'<[^>]+>', ' ', open('/tmp/file.htm').read())
text = re.sub(r'\s+', ' ', text)
# Search for narrow terms; banks categorize differently than expected
"
```

```
# Gitignore directory-exclude breaks negation — use file-level wildcard:
dir/*           # not "dir/" — git refuses to traverse ignored dirs
!dir/*.md
# Verify: git check-ignore -v <file>
```

**Things I noticed but didn't dig into:**
- CFG's "Other finance and insurance" sub-line grew +13.7% QoQ (vs Capital call +2%, Secured PC finance +3.4%). What's in "Other"? If it's shadow-bank lending, that's the line that maps to the BROCK domain. Decomposition not in 10-Q narrative I scanned.
- CFG's $1.5B reconciliation gap (Slide 24 prelim $19.6B vs 10-Q $18.12B) might just be inclusion of Schedule O off-balance-sheet items. Worth a Schedule O grep next session.
- VLY 10-Q has 22 charge-off + 38 provision references — unusual disclosure density even for a Q1. Suggests management is preparing the table for a larger Q2 disclosure. Or they're explaining the -66% YoY drop defensively.
- EGBN's "transfer of certain loans to HFS" phrase is the recognition mechanism. Need to compare HFS balance Q1 vs Q4 to see the magnitude — pulled from Note: Loans Held for Sale.
- Friday-night option chain quirk: SSB May 15 weekly has 4 OI total; bid showed $0 even with last $2.00. Mon open could revalidate or kill — Mon AM check is high-leverage.

**Convention question for next session:**
- Should I treat unprocessed-inbox-signals as ROADMAP open threads (current pattern after this session) or as a separate "INBOX" section? RED counter and CARL handover both went into open threads with 🔴/🟠 markers. Works for now; revisit if the inbox queue grows.

**Mistake / lesson this session:**
- Initial gitignore attempt put `!dir/*.md` AFTER `dir/`. Didn't work — git refuses to traverse ignored dirs. Fixed via file-level wildcard `dir/*` + negation. ALWAYS test gitignore changes with `git check-ignore -v` before committing.
- Phantom-detection lesson: when a position is referenced in dashboard files but doesn't appear in POSITIONS.md AND doesn't appear in FORGE/STATUS.md, treat as phantom by default. Closing positions needs a propagation step to dependent docs/agents. (Promoted to MEMORY findings.)

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
